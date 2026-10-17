"""Menjalankan kode yang ditulis user, dengan batas waktu dan memori.

Kode latihan ditulis oleh pemula, jadi asumsikan yang terburuk: infinite loop,
alokasi memori kebablasan, atau output tak berujung. Semua dibatasi di sini.

Tiga pelajaran yang membentuk desain modul ini:

* **Output ditulis ke berkas, bukan ke pipe.** Dulu `capture_output=True`
  menampung seluruh keluaran anak di RAM proses INDUK dulu, baru dipotong
  sesudahnya -- `while True: print("halo")` sanggup menyedot 8 GB dan membuat
  aplikasi dibunuh OOM killer. Sekarang keluaran mendarat di berkas di dalam
  direktori sementara, sehingga RLIMIT_FSIZE menjadi plafon keras dan induk
  hanya membaca sekian ribu karakter pertama.
* **Anak dijalankan di sesi proses sendiri.** `subprocess` hanya membunuh anak
  langsung; cucu (subshell `&`, binari hasil `go run`) selamat dan terus
  membakar CPU. Sekarang seluruh process group dibunuh sekaligus.
* **RLIMIT_CPU bukan pengganti batas wall-clock.** Ia menjumlahkan waktu CPU
  semua thread, jadi program 4 thread yang sah mati di detik ke-4 dari jatah 10
  detik. Batas waktu ditegakkan oleh timeout; RLIMIT_CPU cuma jaring pengaman.

Ini BUKAN sandbox keamanan. Kode berjalan sebagai user yang sama dengan aplikasi.
Jangan pernah menjalankan kode dari sumber yang tidak dipercaya.
"""

import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field

try:
    import resource  # POSIX saja
except ImportError:
    resource = None

# Pembaca struktur HTML/CSS. Dijalankan sebagai subprocess seperti compiler
# mana pun, memakai penerjemah Python yang SAMA dengan yang menjalankan
# aplikasi ini — jadi tidak ada yang perlu dipasang, dan tidak ada versi yang
# bisa berbeda dari yang diuji.
_STRUKTUR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "struktur.py")

BATAS_WAKTU_DETIK = 10
BATAS_MEMORI_MB = 512
BATAS_FILE_MB = 16
BATAS_OUTPUT_CHAR = 20_000

_JUMLAH_CPU = os.cpu_count() or 1


@dataclass
class Hasil:
    sukses: bool
    keluaran: str = ""
    galat: str = ""
    kode_keluar: int = 0
    fase: str = "jalan"          # "kompilasi" | "jalan" | "setup"
    timeout: bool = False
    catatan: str = ""


@dataclass
class Toolchain:
    key: str
    label: str
    ekstensi: str
    butuh: list                       # program yang harus ada di PATH
    siapkan: object = None            # fn(dir, path) -> None; berkas pendamping
    kompilasi: object = None          # fn(dir, path) -> list[str] | None
    jalankan: object = None           # fn(dir, path) -> list[str]
    cek_sintaks: object = None        # fn(dir, path) -> list[str] | None
    batasi_memori: bool = True
    nama_file: object = None          # fn(kode) -> nama file
    catatan: str = ""
    stdin_dari_file: bool = False     # jalankan sebagai `cmd < file`
    argumen_ekstra: list = field(default_factory=list)
    batas_waktu: int = BATAS_WAKTU_DETIK
    lingkungan: dict = field(default_factory=dict)
    instalasi: dict = field(default_factory=dict)


def _nama_kelas_java(kode):
    """Ambil nama public class supaya nama file cocok dengan syarat javac."""
    m = re.search(r"\bpublic\s+(?:final\s+|abstract\s+)?class\s+([A-Za-z_]\w*)", kode)
    if m:
        return m.group(1)
    m = re.search(r"\bclass\s+([A-Za-z_]\w*)", kode)
    return m.group(1) if m else "Main"


def _sqlite_aman():
    """True kalau sqlite3 di mesin ini mengenal flag -safe.

    Tanpa flag itu, dot-command seperti `.output /path/apa/pun` yang diketik
    pelajar bisa menimpa berkas di luar direktori sementara. Flag ini baru ada
    di SQLite 3.34+, jadi keberadaannya diperiksa dulu, bukan diasumsikan.
    """
    if not shutil.which("sqlite3"):
        return False
    try:
        hasil = subprocess.run(
            ["sqlite3", "-safe", "-batch", ":memory:"],
            input=b"select 1;", capture_output=True, timeout=5,
        )
        return hasil.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


_SQLITE_AMAN = _sqlite_aman()


def _perintah_sqlite(d, p):
    dasar = ["sqlite3", "-batch", "-init", os.devnull]
    if _SQLITE_AMAN:
        dasar.insert(1, "-safe")
    return dasar + [":memory:"]


# ---------------------------------------------------------------- .NET

def _tfm_dotnet():
    """Target framework moniker yang cocok dengan SDK terpasang, misal "net8.0".

    Berkas proyek WAJIB menyebut satu TFM, dan menuliskannya mati di kode
    berarti setiap mesin yang SDK-nya lebih baru harus memasang runtime lama
    hanya untuk menjalankan satu latihan. Angkanya ditanyakan sekali saat
    modul dimuat -- pola yang sama dengan `_SQLITE_AMAN` di atas.
    """
    if not shutil.which("dotnet"):
        return "net8.0"
    # Jalur anak di LUAR `_lingkungan()`, jadi pagar FORCE_COLOR di sana tidak
    # menjangkaunya -- dan di sini keluarannya DIURAI, bukan cuma dilihat
    # returncode-nya: satu `ESC[32m` membuat `int()` gagal dan TFM jatuh diam ke
    # fallback. `pop`, bukan `= "0"`: CPython memaksa warna untuk nilai tak-kosong.
    lingkungan = os.environ.copy()
    lingkungan.pop("FORCE_COLOR", None)
    try:
        hasil = subprocess.run(["dotnet", "--version"], capture_output=True,
                               timeout=20, text=True, env=lingkungan)
        mayor = hasil.stdout.strip().split(".")[0]
        return f"net{int(mayor)}.0"
    except (OSError, ValueError, IndexError, subprocess.SubprocessError):
        return "net8.0"


_TFM_DOTNET = _tfm_dotnet()

# Properti yang sama untuk C# dan Visual Basic. Tiga di antaranya bukan selera:
#   ImplicitUsings          -- dinyalakan karena itulah BAWAAN
#                              `dotnet new console` sejak .NET 6. Mematikannya
#                              membuat contoh top-level statement gagal di sini
#                              padahal jalan di mesin pelajar sendiri.
#                              (Catatan: komentar XML tidak boleh memuat dua
#                              tanda hubung berurutan, jadi penjelasan seperti
#                              ini WAJIB tinggal di sisi Python.)
#   InvariantGlobalization  -- tanpa ini, format angka & tanggal ikut setelan
#                              wilayah mesin, dan kunci jawaban latihan jadi
#                              berbeda antara komputer ber-locale id-ID dan en-US.
#   GenerateAssemblyInfo    -- mematikan berkas turunan yang tidak dipakai.
#   NoWarn NU1900           -- diam saat mesinnya sedang tanpa jaringan.
_PROYEK_DOTNET = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>{tfm}</TargetFramework>
    <AssemblyName>program</AssemblyName>
    <RootNamespace>Latihan</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <InvariantGlobalization>true</InvariantGlobalization>
    <GenerateAssemblyInfo>false</GenerateAssemblyInfo>
    <EnableDefaultCompileItems>true</EnableDefaultCompileItems>
    <RestorePackages>false</RestorePackages>
    <NoWarn>$(NoWarn);NU1900;CS1591</NoWarn>
{ekstra}  </PropertyGroup>
</Project>
"""


def _siapkan_dotnet(nama_proyek, ekstra=""):
    """Kembalikan fungsi `siapkan` yang menuliskan berkas proyek MSBuild."""
    def tulis(d, p):
        isi = _PROYEK_DOTNET.format(tfm=_TFM_DOTNET, ekstra=ekstra)
        with open(os.path.join(d, nama_proyek), "w", encoding="utf-8") as f:
            f.write(isi)
    return tulis


def _bangun_dotnet(d, p):
    # -o out memastikan hasilnya selalu di tempat yang sama, apa pun konfigurasi
    # bawaan SDK-nya. Tanpa itu jalurnya ikut berubah antar versi .NET.
    return ["dotnet", "build", "--nologo", "-v", "q", "-o", os.path.join(d, "out")]


def _jalan_dotnet(d, p):
    return ["dotnet", os.path.join(d, "out", "program.dll")]


_LINGKUNGAN_DOTNET = {
    "DOTNET_CLI_TELEMETRY_OPTOUT": "1",
    "DOTNET_NOLOGO": "1",
    "DOTNET_SKIP_FIRST_TIME_EXPERIENCE": "1",
    # Membangun proyek tanpa satu pun PackageReference tetap menyentuh NuGet.
    # Mode offline membuatnya berhenti menunggu jaringan di mesin yang sedang
    # tidak tersambung -- kegagalan yang sama sekali tidak ada hubungannya
    # dengan kode yang sedang dinilai.
    "DOTNET_CLI_UI_LANGUAGE": "en",
    # .NET 7+ menyalakan W^X double-mapping: wilayah kode JIT dipetakan lewat
    # sebuah berkas besar demi keamanan. Berkas itu menabrak RLIMIT_FSIZE 16 MB
    # dan membunuh `dotnet` SEBELUM ia sempat mengompilasi apa pun -- yang
    # terlihat cuma "Program menulis lebih dari 16 MB", tanpa hubungan apa pun
    # dengan kode yang sedang dinilai. Mematikannya di sini menjaga pagar 16 MB
    # tetap berlaku untuk program pelajar sendiri.
    "DOTNET_EnableWriteXorExecute": "0",
}


# Git membaca tiga lapis konfigurasi: sistem (/etc/gitconfig), global
# (~/.gitconfig), dan repositori. `_lingkungan()` sudah memindahkan HOME ke
# direktori kerja, jadi lapis global milik pelajar tidak terbaca; lapis sistem
# dimatikan di sini. Yang tersisa cuma apa yang ditulis skrip itu sendiri --
# dan itulah yang membuat satu latihan memberi keluaran yang sama di komputer
# mana pun, termasuk komputer yang user.name-nya belum pernah diatur.
_LINGKUNGAN_GIT = {
    "GIT_CONFIG_NOSYSTEM": "1",
    # Perintah yang membuka editor (commit tanpa -m, rebase -i) akan menunggu
    # vi yang tidak pernah ditutup siapa pun sampai batas waktu habis. Dengan
    # editor `true`, commit tanpa pesan langsung dibatalkan Git sendiri dengan
    # pesan yang bisa dibaca.
    "GIT_EDITOR": "true",
    # Jangan pernah menunggu kredensial di terminal yang tidak ada orangnya.
    "GIT_TERMINAL_PROMPT": "0",
    # Tanggal dipatok supaya urutan riwayat yang dicetak latihan tidak
    # bergantung pada detik keberapa skripnya dijalankan.
    "GIT_AUTHOR_DATE": "2026-01-01T00:00:00+0000",
    "GIT_COMMITTER_DATE": "2026-01-01T00:00:00+0000",
}


TOOLCHAINS = {
    "python": Toolchain(
        key="python", label="Python", ekstensi=".py", butuh=["python3"],
        jalankan=lambda d, p: ["python3", "-I", p],
        cek_sintaks=lambda d, p: ["python3", "-m", "py_compile", p],
        lingkungan={"PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"},
        instalasi={
            "fedora": "sudo dnf install python3",
            "debian": "sudo apt install python3",
            "arch": "sudo pacman -S python",
            "mac": "brew install python",
            "windows": "Unduh dari https://python.org lalu centang 'Add to PATH'",
        },
    ),
    "javascript": Toolchain(
        key="javascript", label="JavaScript", ekstensi=".js", butuh=["node"],
        # V8 memesan address space besar sejak awal sehingga RLIMIT_AS tidak
        # bisa dipakai; --max-old-space-size adalah penggantinya yang setara.
        jalankan=lambda d, p: ["node", "--max-old-space-size=256", p],
        cek_sintaks=lambda d, p: ["node", "--check", p],
        batasi_memori=False,
        instalasi={
            "fedora": "sudo dnf install nodejs",
            "debian": "sudo apt install nodejs",
            "arch": "sudo pacman -S nodejs",
            "mac": "brew install node",
            "windows": "Unduh dari https://nodejs.org (versi LTS)",
        },
    ),
    "java": Toolchain(
        key="java", label="Java", ekstensi=".java", butuh=["javac", "java"],
        nama_file=lambda kode: _nama_kelas_java(kode) + ".java",
        # Berkas ditulis UTF-8, jadi javac harus diberi tahu. Tanpa ini, di
        # mesin ber-locale C setiap huruf beraksen jadi "unmappable character".
        kompilasi=lambda d, p: ["javac", "-nowarn", "-encoding", "UTF-8", "-d", d, p],
        jalankan=lambda d, p: ["java", "-XX:+UseSerialGC", "-Xmx256m",
                               "-Dfile.encoding=UTF-8", "-cp", d,
                               os.path.basename(p)[:-5]],
        batasi_memori=False,  # JVM butuh address space besar; dibatasi lewat -Xmx
        batas_waktu=25,
        instalasi={
            "fedora": "sudo dnf install java-latest-openjdk-devel",
            "debian": "sudo apt install default-jdk",
            "arch": "sudo pacman -S jdk-openjdk",
            "mac": "brew install openjdk",
            "windows": "Pasang Temurin JDK dari https://adoptium.net",
        },
    ),
    "c": Toolchain(
        key="c", label="C", ekstensi=".c", butuh=["gcc"],
        kompilasi=lambda d, p: ["gcc", "-std=c11", "-Wall", p, "-o",
                                os.path.join(d, "program"), "-lm"],
        jalankan=lambda d, p: [os.path.join(d, "program")],
        batas_waktu=20,
        instalasi={
            "fedora": "sudo dnf install gcc",
            "debian": "sudo apt install build-essential",
            "arch": "sudo pacman -S gcc",
            "mac": "xcode-select --install",
            "windows": "Pasang MinGW-w64 lewat MSYS2 (https://www.msys2.org)",
        },
    ),
    "cpp": Toolchain(
        key="cpp", label="C++", ekstensi=".cpp", butuh=["g++"],
        kompilasi=lambda d, p: ["g++", "-std=c++17", "-Wall", p, "-o",
                                os.path.join(d, "program")],
        jalankan=lambda d, p: [os.path.join(d, "program")],
        batas_waktu=25,
        instalasi={
            "fedora": "sudo dnf install gcc-c++",
            "debian": "sudo apt install g++",
            "arch": "sudo pacman -S gcc",
            "mac": "xcode-select --install",
            "windows": "Pasang MinGW-w64 lewat MSYS2 (https://www.msys2.org)",
        },
    ),
    "sql": Toolchain(
        key="sql", label="SQL", ekstensi=".sql", butuh=["sqlite3"],
        jalankan=_perintah_sqlite,
        stdin_dari_file=True,
        catatan=("Dijalankan pakai SQLite, bukan MySQL. Sebagian besar SQL standar "
                 "jalan normal, tapi fitur khas MySQL (AUTO_INCREMENT, ENGINE=InnoDB, "
                 "SHOW TABLES) tidak dikenali."),
        instalasi={
            "fedora": "sudo dnf install sqlite",
            "debian": "sudo apt install sqlite3",
            "arch": "sudo pacman -S sqlite",
            "mac": "sudah bawaan macOS (atau: brew install sqlite)",
            "windows": "Unduh sqlite-tools dari https://sqlite.org/download.html",
        },
    ),
    "bash": Toolchain(
        key="bash", label="Bash", ekstensi=".sh", butuh=["bash"],
        jalankan=lambda d, p: ["bash", p],
        cek_sintaks=lambda d, p: ["bash", "-n", p],
        instalasi={
            "fedora": "sudah bawaan",
            "debian": "sudah bawaan",
            "arch": "sudah bawaan",
            "mac": "sudah bawaan (versi lama; brew install bash untuk yang baru)",
            "windows": "Pakai WSL, Git Bash, atau MSYS2",
        },
    ),
    # ------------------------------------------------------------ HTML & CSS
    #
    # Dua-duanya tidak "dijalankan": tidak ada yang dieksekusi, tidak ada yang
    # dicetak. Yang dijalankan adalah struktur.py, yang MEMBACA berkasnya dan
    # mencetak strukturnya sebagai pohon. Dengan begitu keduanya masuk ke mesin
    # penilaian yang sama persis dengan Java atau Python — bandingkan keluaran,
    # tidak ada aturan kelulusan kedua di mana pun.
    #
    # `butuh` sengaja kosong. Itu bukan kelalaian melainkan yang paling
    # berharga dari keduanya: HTML dan CSS bisa dikerjakan DAN dinilai di
    # komputer mana pun yang sanggup menjalankan aplikasi ini, termasuk yang
    # tidak punya satu compiler pun. Buat orang yang baru mulai dan belum
    # sanggup memasang apa-apa, dua bahasa inilah pintu masuknya.
    "html": Toolchain(
        key="html", label="HTML", ekstensi=".html", butuh=[],
        nama_file=lambda kode: "index.html",
        jalankan=lambda d, p: [sys.executable, _STRUKTUR, "html", p],
        catatan="Struktur halaman dibaca dan ditampilkan sebagai pohon "
                "elemen: itulah yang browser lihat dari markup-mu.",
    ),
    "css": Toolchain(
        key="css", label="CSS", ekstensi=".css", butuh=[],
        nama_file=lambda kode: "gaya.css",
        jalankan=lambda d, p: [sys.executable, _STRUKTUR, "css", p],
        catatan="Aturan CSS dibaca dan ditampilkan setelah dirapikan: "
                "pemilih, lalu properti dan nilainya.",
    ),

    "go": Toolchain(
        key="go", label="Go", ekstensi=".go", butuh=["go"],
        nama_file=lambda kode: "main.go",
        jalankan=lambda d, p: ["go", "run", p],
        batasi_memori=False,   # toolchain Go memesan address space besar
        batas_waktu=40,        # kompilasi + jalan dalam satu perintah
        lingkungan={"GOMEMLIMIT": "256MiB"},
        instalasi={
            "fedora": "sudo dnf install golang",
            "debian": "sudo apt install golang",
            "arch": "sudo pacman -S go",
            "mac": "brew install go",
            "windows": "Unduh installer dari https://go.dev/dl",
        },
    ),

    # ------------------------------------------------------- .NET: C# & VB
    #
    # Keduanya TIDAK bisa dikompilasi dari berkas tunggal: MSBuild menolak
    # bekerja tanpa berkas proyek di direktori yang sama. Itulah satu-satunya
    # alasan kait `siapkan` ada. `dotnet build` dipilih ketimbang memanggil
    # csc.dll/vbc.dll langsung karena jalur Roslyn di dalam SDK berpindah antar
    # versi, sedangkan `dotnet build` permukaan resmi yang stabil sejak .NET 6.
    "csharp": Toolchain(
        key="csharp", label="C#", ekstensi=".cs", butuh=["dotnet"],
        nama_file=lambda kode: "Program.cs",
        siapkan=_siapkan_dotnet("latihan.csproj"),
        kompilasi=_bangun_dotnet,
        jalankan=_jalan_dotnet,
        batasi_memori=False,   # runtime .NET memesan address space besar
        batas_waktu=90,        # restore + build MSBuild pada jalan pertama
        lingkungan=_LINGKUNGAN_DOTNET,
        instalasi={
            "fedora": "sudo dnf install dotnet-sdk-8.0",
            "debian": "sudo apt install dotnet-sdk-8.0",
            "arch": "sudo pacman -S dotnet-sdk",
            "mac": "brew install --cask dotnet-sdk",
            "windows": "Unduh .NET SDK dari https://dotnet.microsoft.com/download",
        },
    ),
    "vb": Toolchain(
        key="vb", label="Visual Basic", ekstensi=".vb", butuh=["dotnet"],
        nama_file=lambda kode: "Program.vb",
        # OptionStrict=On mematikan konversi tipe diam-diam. Ini bukan selera:
        # tanpa itu, VB menerima `Dim n As Integer = "7"` tanpa sepatah kata
        # pun, dan seluruh materi tentang tipe data kehilangan penegaknya.
        siapkan=_siapkan_dotnet(
            "latihan.vbproj",
            ekstra="    <OptionStrict>On</OptionStrict>\n"
                   "    <OptionExplicit>On</OptionExplicit>\n"
                   "    <OptionInfer>On</OptionInfer>\n"
                   "    <MyType>Empty</MyType>\n"),
        kompilasi=_bangun_dotnet,
        jalankan=_jalan_dotnet,
        batasi_memori=False,
        batas_waktu=90,
        lingkungan=_LINGKUNGAN_DOTNET,
        catatan=("Yang dipakai di sini Visual Basic .NET, bukan VB6 atau VBA. "
                 "Option Strict dinyalakan, jadi konversi tipe harus ditulis."),
        instalasi={
            "fedora": "sudo dnf install dotnet-sdk-8.0",
            "debian": "sudo apt install dotnet-sdk-8.0",
            "arch": "sudo pacman -S dotnet-sdk",
            "mac": "brew install --cask dotnet-sdk",
            "windows": "Unduh .NET SDK dari https://dotnet.microsoft.com/download",
        },
    ),
    "rust": Toolchain(
        key="rust", label="Rust", ekstensi=".rs", butuh=["rustc"],
        nama_file=lambda kode: "main.rs",
        # Edisi 2021 dipilih, bukan yang terbaru: ia dikenali SEMUA rustc sejak
        # 1.56, sementara tidak satu pun latihan di sini memakai fitur yang cuma
        # ada di edisi sesudahnya. Kompiler yang sedikit tua di repositori
        # distribusi tetap bisa menilai jawaban pelajar.
        kompilasi=lambda d, p: ["rustc", "--edition", "2021", "-O",
                                "--crate-name", "latihan",
                                p, "-o", os.path.join(d, "program")],
        jalankan=lambda d, p: [os.path.join(d, "program")],
        # Linker LLD yang dipakai rustc membuat beberapa thread sekaligus, dan
        # tiap thread memesan address space sendiri. Dengan RLIMIT_AS 512 MB ia
        # gagal membuat thread lalu abort -- yang muncul di layar pelajar bukan
        # "kurang memori" melainkan crash LLVM sepanjang lima puluh baris.
        batasi_memori=False,
        batas_waktu=45,
        instalasi={
            "fedora": "sudo dnf install rust cargo",
            "debian": "sudo apt install rustc cargo",
            "arch": "sudo pacman -S rust",
            "mac": "brew install rust",
            "windows": "Pasang lewat https://rustup.rs",
        },
    ),
    "php": Toolchain(
        key="php", label="PHP", ekstensi=".php", butuh=["php"],
        # -n mengabaikan php.ini sistem supaya hasilnya sama di mesin mana pun:
        # satu ekstensi yang kebetulan aktif bisa mengubah keluaran latihan.
        jalankan=lambda d, p: ["php", "-n", "-d", "error_reporting=E_ALL", p],
        cek_sintaks=lambda d, p: ["php", "-n", "-l", p],
        instalasi={
            "fedora": "sudo dnf install php-cli",
            "debian": "sudo apt install php-cli",
            "arch": "sudo pacman -S php",
            "mac": "brew install php",
            "windows": "Unduh dari https://windows.php.net/download",
        },
    ),
    "ruby": Toolchain(
        key="ruby", label="Ruby", ekstensi=".rb", butuh=["ruby"],
        jalankan=lambda d, p: ["ruby", "--disable-gems", p],
        cek_sintaks=lambda d, p: ["ruby", "-c", p],
        instalasi={
            "fedora": "sudo dnf install ruby",
            "debian": "sudo apt install ruby-full",
            "arch": "sudo pacman -S ruby",
            "mac": "brew install ruby",
            "windows": "Pasang RubyInstaller dari https://rubyinstaller.org",
        },
    ),
    "kotlin": Toolchain(
        key="kotlin", label="Kotlin", ekstensi=".kt", butuh=["kotlinc", "kotlin"],
        # Nama berkas menentukan nama kelas yang dihasilkan: main.kt -> MainKt.
        # Itu sebabnya namanya dipatok, sama seperti main.go di Go.
        nama_file=lambda kode: "main.kt",
        kompilasi=lambda d, p: ["kotlinc", p, "-nowarn",
                                "-d", os.path.join(d, "kelas")],
        jalankan=lambda d, p: ["kotlin", "-cp", os.path.join(d, "kelas"), "MainKt"],
        batasi_memori=False,   # kompiler Kotlin berjalan di atas JVM
        batas_waktu=120,       # kompilasi Kotlin memang lambat, 2-4 detik wajar
        instalasi={
            "fedora": "sudo dnf install kotlin  (atau: sdk install kotlin)",
            "debian": "sudo snap install --classic kotlin",
            "arch": "sudo pacman -S kotlin",
            "mac": "brew install kotlin",
            "windows": "Pasang lewat SDKMAN/Chocolatey: choco install kotlinc",
        },
    ),
    # Kurikulum CLI Linux. Latihannya BERUPA SKRIP dan dijalankan bash, tapi
    # ia sengaja punya key sendiri: blok perintah di MATERINYA diperlakukan
    # sebagai sesi terminal (lihat inti/berkas.py), bukan program yang boleh
    # dieksekusi aplikasi.
    "fedora": Toolchain(
        key="fedora", label="CLI Linux", ekstensi=".sh", butuh=["bash"],
        jalankan=lambda d, p: ["bash", p],
        cek_sintaks=lambda d, p: ["bash", "-n", p],
        catatan=("Latihan dijalankan di direktori sementara dengan hak akses "
                 "pengguna biasa. Tidak ada satu pun latihan yang memerlukan "
                 "sudo atau mengubah sistemmu."),
        instalasi={
            "fedora": "sudah bawaan",
            "debian": "sudah bawaan",
            "arch": "sudah bawaan",
            "mac": "sudah bawaan (sebagian perintah GNU berbeda; brew install coreutils)",
            "windows": "Pakai WSL dengan Fedora, atau mesin virtual",
        },
    ),
    # Kurikulum Git & GitHub. Sama seperti Fedora: latihannya skrip bash yang
    # bekerja di mktemp -d, sedangkan blok perintah di MATERINYA sesi terminal
    # (lihat inti/berkas.py) -- `git push --force` dan `git reset --hard` di
    # repositori milik pelajar bukan sesuatu yang boleh dijalankan aplikasi
    # atas namanya.
    "git": Toolchain(
        key="git", label="Git", ekstensi=".sh", butuh=["bash", "git"],
        jalankan=lambda d, p: ["bash", p],
        cek_sintaks=lambda d, p: ["bash", "-n", p],
        catatan=("Setiap latihan membuat repositorinya sendiri di direktori "
                 "sementara (mktemp -d) dan menghapusnya saat selesai. "
                 "Repositori milikmu tidak pernah disentuh."),
        lingkungan=_LINGKUNGAN_GIT,
        instalasi={
            "fedora": "sudo dnf install git",
            "debian": "sudo apt install git",
            "arch": "sudo pacman -S git",
            "mac": "xcode-select --install  (atau: brew install git)",
            "windows": "Git for Windows dari git-scm.com (sudah termasuk Git Bash)",
        },
    ),
    "typescript": Toolchain(
        key="typescript", label="TypeScript", ekstensi=".ts", butuh=["tsc", "node"],
        nama_file=lambda kode: "program.ts",
        # --strict dinyalakan karena separuh gunanya TypeScript hilang tanpanya.
        # Tanpa strictNullChecks, `let x: string = null` lolos diam-diam dan
        # materi tentang null-safety kehilangan penegaknya.
        # es2023, bukan es2022: di situlah toSorted, toReversed, dan with
        # masuk -- tiga method yang mengembalikan SALINAN alih-alih mengubah
        # array di tempat, dan karena itu justru yang diajarkan di sini.
        kompilasi=lambda d, p: ["tsc", "--strict", "--target", "es2023",
                                "--module", "commonjs", "--outDir", d, p],
        jalankan=lambda d, p: ["node", "--max-old-space-size=256",
                               os.path.join(d, "program.js")],
        batasi_memori=False,   # V8 memesan address space besar sejak awal
        batas_waktu=60,
        instalasi={
            "fedora": "sudo dnf install nodejs && sudo npm install -g typescript",
            "debian": "sudo apt install nodejs npm && sudo npm install -g typescript",
            "arch": "sudo pacman -S nodejs npm && sudo npm install -g typescript",
            "mac": "brew install node && npm install -g typescript",
            "windows": "Pasang Node.js lalu: npm install -g typescript",
        },
    ),
}


_MEMO_TERSEDIA = {}
TTL_TERSEDIA = 30.0


def tersedia(bahasa):
    """True kalau semua program yang dibutuhkan bahasa ini ada di PATH."""
    tc = TOOLCHAINS.get(bahasa)
    if not tc:
        return False
    sekarang = time.monotonic()
    ada = _MEMO_TERSEDIA.get(bahasa)
    # Memo 30 detik: /api/awal menanyakan semua toolchain tiap muat, dan
    # shutil.which menyisir PATH. Pemasangan baru terbaca dalam setengah menit.
    if ada is not None and sekarang - ada[0] < TTL_TERSEDIA:
        return ada[1]
    hasil = all(shutil.which(prog) for prog in tc.butuh)
    _MEMO_TERSEDIA[bahasa] = (sekarang, hasil)
    return hasil


def program_hilang(bahasa):
    tc = TOOLCHAINS.get(bahasa)
    if not tc:
        return []
    return [p for p in tc.butuh if not shutil.which(p)]


def daftar_tersedia():
    return {k: tersedia(k) for k in TOOLCHAINS}


def batas_waktu(bahasa):
    tc = TOOLCHAINS.get(bahasa)
    return tc.batas_waktu if tc else BATAS_WAKTU_DETIK


# ------------------------------------------------------------ deteksi distro

def _distro():
    """Tebak keluarga sistem operasi untuk memilih perintah instalasi."""
    if os.name == "nt":
        return "windows"
    try:
        if os.uname().sysname == "Darwin":
            return "mac"
    except AttributeError:
        pass
    try:
        with open("/etc/os-release", "r", encoding="utf-8") as f:
            isi = f.read().lower()
    except OSError:
        return "debian"
    if any(x in isi for x in ("fedora", "rhel", "centos", "rocky", "alma")):
        return "fedora"
    if "arch" in isi or "manjaro" in isi:
        return "arch"
    return "debian"


def perintah_instalasi(bahasa):
    """Satu baris perintah pemasangan yang cocok untuk mesin ini, atau ""."""
    tc = TOOLCHAINS.get(bahasa)
    if not tc or not tc.instalasi:
        return ""
    return tc.instalasi.get(_distro(), "") or tc.instalasi.get("debian", "")


# ------------------------------------------------------------------ eksekusi

def _batas(tc, timeout):
    if resource is None:
        return None

    def terapkan():
        # RLIMIT_CPU menjumlahkan waktu CPU SEMUA thread, sementara `timeout`
        # adalah batas wall-clock. Dikalikan jumlah core supaya program
        # multithread yang sah tidak mati sebelum waktunya; batas sebenarnya
        # tetap ditegakkan oleh timeout di proses induk.
        cpu = max(1, int(timeout) + 1) * _JUMLAH_CPU
        resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu + 1))
        fsize = BATAS_FILE_MB * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_FSIZE, (fsize, fsize))
        if tc.batasi_memori:
            mem = BATAS_MEMORI_MB * 1024 * 1024
            resource.setrlimit(resource.RLIMIT_AS, (mem, mem))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))

    return terapkan


def _potong(teks):
    if len(teks) <= BATAS_OUTPUT_CHAR:
        return teks
    return teks[:BATAS_OUTPUT_CHAR] + f"\n...[output dipotong di {BATAS_OUTPUT_CHAR} karakter]"


def _baca_terbatas(path):
    """Baca sebagian awal berkas keluaran. Tidak pernah menyedot seluruh isinya."""
    try:
        besar = os.path.getsize(path)
        with open(path, "rb") as f:
            data = f.read(BATAS_OUTPUT_CHAR * 4)
        teks = data.decode("utf-8", errors="replace")
        if besar > len(data):
            teks = _potong(teks) + f"\n...[total {besar} byte, sisanya dibuang]"
            return teks
        return _potong(teks)
    except OSError:
        return ""


def _bunuh(proc):
    """Bunuh proses beserta seluruh keturunannya."""
    try:
        if os.name != "nt":
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        else:
            proc.kill()
    except (OSError, ProcessLookupError):
        try:
            proc.kill()
        except OSError:
            pass


def _bunuh_sisa(proc):
    """Bunuh keturunan yang masih hidup SESUDAH program utamanya selesai.

    `_bunuh` dulu cuma dipanggil saat timeout. Program yang selesai normal
    tapi meninggalkan anak di latar (`sleep 300 &`, `subprocess.Popen`, server
    kecil di latihan Bash/Python) membiarkan anak itu hidup sampai komputer
    dimatikan, bekerja di direktori sementara yang sudah dihapus. Proses
    dijalankan dengan `start_new_session`, jadi PID-nya juga nomor grupnya:
    grup itu bisa dibunuh walau pemimpinnya sudah dipanen `wait`.
    """
    if os.name == "nt":
        return
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except (OSError, ProcessLookupError):
        pass  # grupnya sudah kosong: kasus yang paling sering


def _lingkungan(cwd, tc):
    lingkungan = dict(os.environ)
    lingkungan["HOME"] = cwd
    lingkungan.pop("PYTHONPATH", None)
    # Saluran keluar anak SELALU berkas (lihat _proses), jadi warna yang
    # DIPAKSAKAN lingkungan induk cuma menyisipkan kode ANSI ke teks yang
    # ditampilkan apa adanya ke pelajar -- dan membuat regex penunjuk nomor
    # baris di galat.py berhenti cocok, jadi "loncat ke baris" ikut hilang.
    # Dibuang, bukan disetel "0": di CPython nilai tak-kosong apa pun
    # (termasuk "0") justru MEMAKSA warna nyala.
    lingkungan.pop("FORCE_COLOR", None)
    lingkungan["PYTHONDONTWRITEBYTECODE"] = "1"
    # Samakan locale supaya kompiler & program menulis/membaca UTF-8 di mesin
    # mana pun; kalau tidak, huruf beraksen di materi bisa menggagalkan javac.
    lingkungan.setdefault("LC_ALL", "C.UTF-8")
    lingkungan.setdefault("LANG", "C.UTF-8")
    if tc.key == "go":
        lingkungan.setdefault("GOCACHE", os.path.join(cwd, ".gocache"))
        lingkungan.setdefault("GOPATH", os.path.join(cwd, ".gopath"))
    lingkungan.update(tc.lingkungan)
    return lingkungan


_NAMA_SINYAL = {
    signal.SIGSEGV: ("Program berhenti mendadak (segmentation fault) -- biasanya "
                     "akibat pointer atau indeks array di luar batas."),
    signal.SIGFPE: "Pembagian dengan nol atau operasi aritmetika tidak sah.",
    signal.SIGABRT: "Program membatalkan dirinya sendiri (abort).",
    signal.SIGKILL: "Program dihentikan paksa (kemungkinan melebihi batas memori).",
}
if hasattr(signal, "SIGXFSZ"):
    _NAMA_SINYAL[signal.SIGXFSZ] = (
        f"Program menulis lebih dari {BATAS_FILE_MB} MB dan dihentikan.")
if hasattr(signal, "SIGXCPU"):
    _NAMA_SINYAL[signal.SIGXCPU] = "Program memakai waktu CPU jauh melebihi batas."


def _proses(cmd, cwd, tc, timeout, stdin_data=None, stdin_file=None):
    """Jalankan satu proses. Return (kode_keluar, stdout, stderr, timeout?).

    Keluaran ditulis ke berkas di dalam `cwd` (yang selalu direktori sementara)
    supaya RLIMIT_FSIZE membatasinya dan proses induk tidak pernah menampung
    output tak berujung di memori.
    """
    lingkungan = _lingkungan(cwd, tc)
    path_out = os.path.join(cwd, ".keluaran")
    path_err = os.path.join(cwd, ".galat")

    fh_in = f_out = f_err = None
    kena_timeout = False
    rc = 0
    try:
        f_out = open(path_out, "wb")
        f_err = open(path_err, "wb")
        if stdin_file:
            fh_in = open(stdin_file, "rb")
            stdin_arg = fh_in
        else:
            stdin_arg = subprocess.PIPE

        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            env=lingkungan,
            stdin=stdin_arg,
            stdout=f_out,
            stderr=f_err,
            preexec_fn=_batas(tc, timeout) if resource else None,
            start_new_session=(os.name != "nt"),
        )

        try:
            if stdin_arg is subprocess.PIPE:
                proc.communicate(input=(stdin_data or "").encode("utf-8"),
                                 timeout=timeout)
            else:
                proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            kena_timeout = True
            _bunuh(proc)
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass

        rc = 124 if kena_timeout else (proc.returncode or 0)
        _bunuh_sisa(proc)
    except (OSError, ValueError) as e:
        return 127, "", f"Gagal menjalankan: {e}", False
    finally:
        for fh in (fh_in, f_out, f_err):
            if fh:
                try:
                    fh.close()
                except OSError:
                    pass

    out = _baca_terbatas(path_out)
    err = _baca_terbatas(path_err)

    # Sinyal fatal muncul sebagai kode keluar negatif; terjemahkan yang paling
    # sering menimpa kode pemula supaya pesannya bisa dimengerti.
    if not kena_timeout and rc < 0:
        penjelasan = _NAMA_SINYAL.get(-rc)
        if penjelasan:
            err = (err + "\n" + penjelasan).strip()

    return rc, out, err, kena_timeout


def _tempdir():
    """TemporaryDirectory yang tidak meledak kalau proses yatim masih menulis."""
    try:
        return tempfile.TemporaryDirectory(prefix="belajar-", ignore_cleanup_errors=True)
    except TypeError:      # Python < 3.10
        return tempfile.TemporaryDirectory(prefix="belajar-")


def jalankan(bahasa, kode, stdin="", timeout=None):
    """Kompilasi (kalau perlu) lalu jalankan `kode`. Selalu return objek Hasil."""
    tc = TOOLCHAINS.get(bahasa)
    if tc is None:
        return Hasil(False, galat=f"Bahasa '{bahasa}' belum didukung runner.", fase="setup")

    if timeout is None:
        timeout = tc.batas_waktu

    hilang = program_hilang(bahasa)
    if hilang:
        saran = perintah_instalasi(bahasa)
        catatan = f"Pasang dulu {' & '.join(hilang)} untuk menjalankan kode {tc.label}."
        if saran:
            catatan += f"\nDi sistem ini: {saran}"
        return Hasil(False, galat=f"Program belum terpasang: {', '.join(hilang)}",
                     fase="setup", catatan=catatan)

    with _tempdir() as d:
        nama = tc.nama_file(kode) if tc.nama_file else ("program" + tc.ekstensi)
        path = os.path.join(d, nama)
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(kode)
        except OSError as e:
            return Hasil(False, galat=f"Gagal menulis file sementara: {e}", fase="setup")

        # Sebagian toolchain menuntut LEBIH dari satu berkas di direktori kerja:
        # MSBuild menolak bekerja tanpa berkas proyek, berapa pun jumlah berkas
        # sumbernya. Kait ini menuliskannya. Ia sengaja tidak boleh mengubah
        # kode pelajar -- yang dinilai tetap keluaran program, lewat
        # `runner.periksa` yang sama persis seperti bahasa lain.
        if tc.siapkan:
            try:
                tc.siapkan(d, path)
            except OSError as e:
                return Hasil(False, galat=f"Gagal menyiapkan proyek: {e}",
                             fase="setup")

        if tc.kompilasi:
            cmd = tc.kompilasi(d, path)
            rc, out, err, to = _proses(cmd, d, tc, timeout)
            if to:
                pesan = "Kompilasi terlalu lama, dihentikan."
                if err.strip():
                    pesan += "\n" + err.strip()
                return Hasil(False, keluaran=_potong(out), galat=pesan,
                             fase="kompilasi", timeout=True, catatan=tc.catatan)
            if rc != 0:
                return Hasil(False, keluaran=_potong(out),
                             galat=_potong(err or "Kompilasi gagal."),
                             kode_keluar=rc, fase="kompilasi", catatan=tc.catatan)

        cmd = tc.jalankan(d, path)
        if tc.stdin_dari_file:
            rc, out, err, to = _proses(cmd, d, tc, timeout, stdin_file=path)
        else:
            rc, out, err, to = _proses(cmd, d, tc, timeout, stdin_data=stdin)

        if to:
            pesan = (f"Program dihentikan setelah {timeout} detik. "
                     "Kemungkinan ada loop yang tidak pernah berhenti.")
            if err.strip():
                pesan += "\n--- pesan yang sempat tercetak ---\n" + err.strip()
            return Hasil(False, keluaran=_potong(out), galat=pesan,
                         fase="jalan", timeout=True, catatan=tc.catatan)

        return Hasil(rc == 0, keluaran=_potong(out), galat=_potong(err),
                     kode_keluar=rc, fase="jalan", catatan=tc.catatan)


# ------------------------------------------------------------- pengecek jawaban

def normalisasi(teks):
    """Samakan output supaya beda spasi/baris kosong tidak dianggap salah.

    Baris kosong di awal & akhir dibuang, dan spasi di UJUNG KANAN tiap baris
    diabaikan. Indentasi kiri dipertahankan -- termasuk pada baris pertama.
    Versi lama memanggil `.strip()` pada seluruh teks lebih dulu, sehingga
    indentasi baris pertama hilang tapi baris lain tetap utuh: latihan pola
    bintang jadi menampilkan "Hasilmu" yang tidak sesuai apa yang ditulis.
    """
    baris = [b.rstrip()
             for b in teks.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while baris and not baris[-1]:
        baris.pop()
    while baris and not baris[0]:
        baris.pop(0)
    return "\n".join(baris)


def _cocok(aktual, harapan, mode):
    a = normalisasi(aktual)
    h = normalisasi(harapan)
    if mode == "persis":
        return a == h
    if mode == "abaikan_kapital":
        return a.lower() == h.lower()
    if mode == "mengandung":
        return h.lower() in a.lower()
    if mode == "regex":
        try:
            return re.search(harapan, aktual, re.MULTILINE) is not None
        except re.error:
            return False
    if mode == "angka":
        angka_a = re.findall(r"-?\d+(?:\.\d+)?", a)
        angka_h = re.findall(r"-?\d+(?:\.\d+)?", h)
        return angka_a == angka_h
    return a == h


@dataclass
class HasilUji:
    nama: str
    lulus: bool
    harapan: str = ""
    aktual: str = ""
    galat: str = ""
    mode: str = "persis"
    stdin: str = ""
    kode_keluar: int = 0
    output_cocok: bool = False


def cek_sintaks(bahasa, kode, timeout=None):
    """Periksa sintaks tanpa menjalankan program.

    Untuk bahasa terkompilasi, kegagalan sintaks sudah tertangkap saat
    kompilasi. Untuk bahasa interpretasi seperti Python, error sintaks baru
    muncul saat dijalankan -- padahal kalau sintaksnya salah, SEMUA test case
    pasti gagal dengan pesan yang sama. Memeriksanya sekali di depan
    menghemat waktu dan memberi pesan yang lebih jelas.

    Return None kalau sintaks aman (atau tidak bisa diperiksa), atau objek
    Hasil berisi error kalau sintaksnya rusak.
    """
    tc = TOOLCHAINS.get(bahasa)
    if tc is None or tc.cek_sintaks is None or program_hilang(bahasa):
        return None
    if timeout is None:
        timeout = tc.batas_waktu

    with _tempdir() as d:
        nama = tc.nama_file(kode) if tc.nama_file else ("program" + tc.ekstensi)
        path = os.path.join(d, nama)
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(kode)
        except OSError:
            return None

        rc, out, err, to = _proses(tc.cek_sintaks(d, path), d, tc, timeout)
        if to or rc == 0:
            return None
        return Hasil(False, keluaran=_potong(out),
                     galat=_potong(err or out or "Sintaks tidak valid."),
                     kode_keluar=rc, fase="kompilasi", catatan=tc.catatan)


def periksa(bahasa, kode, tests, timeout=None):
    """Jalankan kode untuk tiap test case.

    Format satu test:
        {"nama": "...", "stdin": "", "harapan": "...", "mode": "persis"}

    Mode: persis | abaikan_kapital | mengandung | regex | angka

    Sebuah uji lulus hanya kalau outputnya cocok DAN programnya berakhir
    normal. Program yang mencetak jawaban benar lalu melempar exception tidak
    boleh dinyatakan benar -- itu justru menyembunyikan bug yang sedang
    dipelajari. `HasilUji.output_cocok` tetap merekam bahwa teksnya sudah pas,
    supaya tampilan bisa membedakan "salah jawab" dari "jawaban benar tapi
    program error".

    Return (semua_lulus, [HasilUji], Hasil_terakhir).
    """
    if timeout is None:
        timeout = batas_waktu(bahasa)

    hasil_uji = []
    hasil_jalan = None

    # Sintaks rusak = semua test pasti gagal. Laporkan sekali saja.
    rusak = cek_sintaks(bahasa, kode, timeout)
    if rusak is not None:
        t = tests[0] if tests else {}
        return False, [HasilUji(t.get("nama") or "Uji 1", False,
                                t.get("harapan", ""), "", rusak.galat,
                                t.get("mode", "persis"), t.get("stdin", ""),
                                rusak.kode_keluar)], rusak

    for i, t in enumerate(tests, start=1):
        nama = t.get("nama") or f"Uji {i}"
        stdin = t.get("stdin", "")
        harapan = t.get("harapan", "")
        mode = t.get("mode", "persis")

        hasil_jalan = jalankan(bahasa, kode, stdin=stdin, timeout=timeout)
        if not hasil_jalan.sukses and hasil_jalan.fase in ("kompilasi", "setup"):
            hasil_uji.append(HasilUji(nama, False, harapan, hasil_jalan.keluaran,
                                      hasil_jalan.galat, mode, stdin,
                                      hasil_jalan.kode_keluar))
            break  # kompilasi gagal -> test berikutnya pasti gagal juga

        cocok = _cocok(hasil_jalan.keluaran, harapan, mode)
        lulus = cocok and hasil_jalan.kode_keluar == 0 and not hasil_jalan.timeout
        hasil_uji.append(HasilUji(nama, lulus, harapan, hasil_jalan.keluaran,
                                  hasil_jalan.galat, mode, stdin,
                                  hasil_jalan.kode_keluar, cocok))

    semua = bool(hasil_uji) and all(h.lulus for h in hasil_uji)
    return semua, hasil_uji, hasil_jalan
