"""Menjawab satu pertanyaan pelajar: "kode ini perlu aku ketik ke file atau tidak?"

Sebelum ini, setiap contoh kode muncul begitu saja di dalam kotak tanpa
keterangan. Pemula tidak punya cara tahu apakah blok itu:

  * program utuh yang harus disimpan sebagai berkas lalu dijalankan,
  * potongan penggalan yang cuma menjelaskan sintaks dan akan error kalau
    dijalankan sendirian, atau
  * kumpulan perintah yang diketik langsung di sesi database/terminal.

Modul ini mengklasifikasikan blok kode ke salah satu dari tiga jenis itu,
lalu menyusun kalimat instruksi yang konkret: nama berkasnya apa dan
perintah untuk menjalankannya apa.

Deteksinya sengaja konservatif. Salah menyebut potongan sebagai "program utuh"
akan menyuruh pelajar menjalankan kode yang pasti gagal, dan itu jauh lebih
membingungkan daripada tidak memberi instruksi sama sekali. Kalau ragu,
kembalikan POTONGAN.
"""

import json
import re
import sys

PROGRAM = "program"      # berkas mandiri, bisa langsung dijalankan
POTONGAN = "potongan"    # penggalan penjelas, tidak berdiri sendiri
SESI = "sesi"            # diketik di dalam sesi database / shell interaktif
MULTI = "multi"          # satu contoh yang terdiri dari beberapa berkas
ILUSTRASI = "ilustrasi"  # diagram, tabel, atau struktur folder -- bukan kode

# Panjang maksimal slug nama berkas supaya perintahnya enak dibaca.
MAKS_SLUG = 20


class Petunjuk:
    """Instruksi siap tampil untuk satu blok kode."""

    __slots__ = ("jenis", "nama", "perintah", "instruksi", "keterangan", "berkas")

    def __init__(self, jenis, nama="", perintah=(), instruksi="", keterangan="",
                 berkas=()):
        self.jenis = jenis
        self.nama = nama
        self.perintah = list(perintah)
        self.instruksi = instruksi
        self.keterangan = keterangan
        self.berkas = list(berkas)   # dipakai saat jenis == MULTI

    @property
    def perlu_berkas(self):
        return self.jenis in (PROGRAM, MULTI)

    def __repr__(self):
        return f"Petunjuk({self.jenis!r}, {self.nama!r}, {self.perintah!r})"


# --------------------------------------------------------------- nama berkas

def slug(teks, maks=MAKS_SLUG):
    """'2. Variabel & Tipe Data' -> 'variabel-tipe-data'.

    Nomor urut di depan judul dibuang karena tidak menjelaskan isi, dan kata
    penghubung dibuang supaya nama berkasnya tetap pendek.
    """
    teks = re.sub(r"^\s*\d+[\.\):]?\s*", "", teks or "")
    teks = re.sub(r"[^\w\s-]", " ", teks, flags=re.UNICODE)
    kata = [k for k in re.split(r"[\s_-]+", teks.lower()) if k]

    buang = {"contoh", "dan", "atau", "di", "ke", "dari", "untuk", "dengan",
             "yang", "pada", "the", "a", "an", "dalam", "cara", "amp"}
    inti = [k for k in kata if k not in buang] or kata
    if not inti:
        return "contoh"

    hasil = inti[0]
    for k in inti[1:]:
        if len(hasil) + 1 + len(k) > maks:
            break
        hasil += "-" + k
    return hasil[:maks].strip("-") or "contoh"


def _kelas_java(kode):
    m = re.search(r"\bpublic\s+(?:final\s+|abstract\s+)?class\s+([A-Za-z_]\w*)", kode)
    if m:
        return m.group(1)
    m = re.search(r"\b(?:class|interface|enum|record)\s+([A-Za-z_]\w*)", kode)
    return m.group(1) if m else None


def _pascal(teks):
    potongan = [p for p in slug(teks, maks=40).split("-") if p]
    nama = "".join(p.capitalize() for p in potongan) or "Contoh"
    return nama if nama[0].isalpha() else "Contoh" + nama


EKSTENSI = {
    "python": ".py", "javascript": ".js", "java": ".java", "c": ".c",
    "cpp": ".cpp", "go": ".go", "bash": ".sh", "sql": ".sql",
    "html": ".html", "css": ".css",
    "csharp": ".cs", "vb": ".vb", "rust": ".rs", "php": ".php",
    "ruby": ".rb", "kotlin": ".kt", "typescript": ".ts",
    "fedora": ".sh", "git": ".sh",
}


def nama_berkas(bahasa, kode, konteks=""):
    """Nama berkas yang disarankan untuk sebuah blok kode."""
    if bahasa == "java":
        # javac mewajibkan nama berkas sama persis dengan nama kelas public.
        return (_kelas_java(kode) or _pascal(konteks)) + ".java"
    if bahasa == "go":
        # `go run` pada satu berkas package main; nama bebas, main.go paling lazim.
        return "main.go"
    if bahasa == "html":
        # index.html adalah nama yang dicari server web mana pun saat sebuah
        # folder dibuka. Membiasakannya sejak halaman pertama menghemat satu
        # kebingungan besar nanti.
        return "index.html"
    if bahasa == "css":
        return "gaya.css"
    if bahasa == "csharp":
        # MSBuild mengambil SEMUA berkas .cs di folder proyek; namanya bebas,
        # dan Program.cs adalah yang dibuat `dotnet new console`.
        return "Program.cs"
    if bahasa == "vb":
        return "Program.vb"
    if bahasa == "rust":
        # `rustc main.rs` pada satu berkas; main.rs juga nama yang dicari cargo.
        return "main.rs"
    if bahasa == "kotlin":
        # Nama berkas MENENTUKAN nama kelas yang dihasilkan: main.kt -> MainKt,
        # dan itulah yang dipanggil saat menjalankannya.
        return "main.kt"
    return slug(konteks) + EKSTENSI.get(bahasa, ".txt")


def perintah_jalan(bahasa, nama):
    """Perintah shell untuk menjalankan berkas tersebut."""
    batang = nama.rsplit(".", 1)[0]
    return {
        "python": [f"python3 {nama}"],
        "javascript": [f"node {nama}"],
        "java": [f"javac {nama}", f"java {batang}"],
        "c": [f"gcc {nama} -o {batang}", f"./{batang}"],
        "cpp": [f"g++ {nama} -o {batang}", f"./{batang}"],
        "go": [f"go run {nama}"],
        "csharp": ["dotnet new console -o latihan  (sekali saja)",
                   f"Salin {nama} ke folder latihan, lalu: dotnet run"],
        "vb": ["dotnet new console -lang VB -o latihan  (sekali saja)",
               f"Salin {nama} ke folder latihan, lalu: dotnet run"],
        "rust": [f"rustc {nama} -o {batang}", f"./{batang}"],
        "php": [f"php {nama}"],
        "ruby": [f"ruby {nama}"],
        "kotlin": [f"kotlinc {nama} -include-runtime -d {batang}.jar",
                   f"java -jar {batang}.jar"],
        "typescript": [f"tsc {nama}", f"node {batang}.js"],
        "bash": [f"bash {nama}"],
        "fedora": [f"chmod +x {nama}", f"./{nama}"],
        "git": [f"bash {nama}"],
        "sql": [f"sqlite3 belajar.db < {nama}"],
        # HTML dan CSS tidak dijalankan dari terminal: keduanya dibuka browser.
        # Perintah yang benar-benar dipakai orang untuk melihat hasilnya adalah
        # membuka berkasnya, bukan mengetik apa pun.
        "html": [f"Buka {nama} di browser (klik dua kali, atau Ctrl+O)"],
        "css": ["Tautkan dari HTML: "
                f'<link rel="stylesheet" href="{nama}">',
                "lalu buka berkas HTML-nya di browser"],
    }.get(bahasa, [])


# ----------------------------------------------------------------- deteksi

def _diawali_indentasi(kode):
    """Baris berkode pertama menjorok ke dalam -> jelas cuplikan dari tengah blok."""
    for baris in kode.splitlines():
        if not baris.strip():
            continue
        if baris.strip().startswith(("#", "//", "--", "/*", "*")):
            continue  # komentar pembuka tidak menentukan
        return baris[:1] in (" ", "\t")
    return False


def _ada_elipsis(kode):
    """'...' di luar konteks Go/Python variadic menandakan kode sengaja dipotong."""
    return bool(re.search(r"^\s*(\.\.\.|…)\s*$", kode, re.MULTILINE))


def _ilustrasi(kode):
    """True kalau blok ini diagram, peta rute, atau pohon folder -- bukan kode.

    Materi konseptual memakai blok kode untuk menggambar relasi antar entitas
    dan struktur direktori. Menyebutnya "potongan kode" menyesatkan; pelajar
    bisa mengira ada yang perlu diketik.

    Penanda kode dihitung per baris, bukan sekali untuk seluruh blok, supaya
    diagram yang kebetulan memuat satu tanda kurung tidak salah dikira kode.
    """
    baris = [b for b in kode.splitlines() if b.strip()]
    if not baris:
        return False

    berkode = 0
    for b in baris:
        isi = b.strip()
        if isi.startswith(("#", "//", "--", "*", "/*")):
            continue
        # Tanda baca yang praktis selalu ada di kode sungguhan.
        # Kurung kurawal hanya dihitung kalau berperan sebagai pembatas blok
        # (di ujung baris atau sendirian), bukan placeholder seperti /items/{id}
        # pada peta rute.
        if re.search(r";\s*$"                # akhir pernyataan
                     r"|^[{}]\s*$"           # kurawal sendirian sebaris
                     r"|\{\s*$"              # kurawal pembuka di ujung baris
                     r"|^\}"                 # kurawal penutup di awal baris
                     r"|\w\s*=\s*\S"         # penugasan
                     r"|\w\s*\("             # pemanggilan fungsi
                     r"|::|=>", isi):
            berkode += 1

    if berkode / len(baris) >= 0.25:
        return False

    # Penanda visual khas diagram dan pohon direktori.
    penanda = re.search(r"-{2,}>|<-{2,}|─|│|├|└|\|\s{2,}\||^\s*\w+/\s*$",
                        kode, re.MULTILINE)
    kolom = sum(1 for b in baris if re.search(r"\S\s{3,}\S", b))
    return bool(penanda) or kolom / len(baris) >= 0.6


def _kurung_seimbang(kode):
    tanpa_teks = re.sub(r'"[^"\n]*"|\'[^\'\n]*\'', "", kode)
    return (tanpa_teks.count("{") == tanpa_teks.count("}")
            and tanpa_teks.count("(") == tanpa_teks.count(")"))


def _python_lengkap(kode):
    # Python punya pemeriksa sintaks bawaan, jadi tidak perlu menebak-nebak.
    try:
        compile(kode, "<materi>", "exec")
        return True
    except (SyntaxError, ValueError, TypeError, MemoryError):
        return False


# Komentar penanda seperti  /* ===== File: matematika.h ===== */
# atau  // ==== file: kalkulator/kalkulator.go ====
_PENANDA_BERKAS = re.compile(
    r"""(?:/\*|//|\#|--)\s*=*\s*[Ff]ile\s*:\s*([\w./-]+)""")


def berkas_ganda(kode):
    """Daftar nama berkas kalau blok ini sengaja memuat beberapa berkas sekaligus.

    Materi tentang kompilasi multi-file dan struktur package menuliskan
    beberapa berkas dalam satu blok, dipisah komentar penanda. Menyuruh
    pelajar menyimpannya sebagai satu berkas pasti gagal dikompilasi.
    """
    nama = _PENANDA_BERKAS.findall(kode or "")
    # Satu penanda saja bisa jadi cuma judul; baru disebut multi kalau >= 2.
    hasil = []
    for n in nama:
        if n not in hasil:
            hasil.append(n)
    return hasil if len(hasil) >= 2 else []


# Tipe java.util yang lazim dipakai di contoh tanpa disertai import-nya.
_TIPE_BUTUH_IMPORT = ("List", "ArrayList", "Map", "HashMap", "Set", "HashSet",
                      "Scanner", "Arrays", "Collections", "Optional", "Queue",
                      "LinkedList", "TreeMap", "Iterator", "Comparator")


def _java_import_kurang(kode):
    """True kalau kode memakai tipe java.util tapi tidak mengimpornya.

    Contoh materi sering fokus pada satu konsep dan menghilangkan baris import
    supaya ringkas. Kode seperti itu tidak akan dikompilasi kalau pelajar
    menyalinnya apa adanya, jadi jangan disebut program utuh.
    """
    if re.search(r"^\s*import\s+java\.util\.\*\s*;", kode, re.MULTILINE):
        return False
    for tipe in _TIPE_BUTUH_IMPORT:
        dipakai = re.search(rf"\b{tipe}\s*[<(\[]|\b{tipe}\s+\w+\s*[=;)]", kode)
        if dipakai and not re.search(rf"^\s*import\s+[\w.]*\b{tipe}\s*;",
                                     kode, re.MULTILINE):
            return True
    return False


def _java_lengkap(kode):
    if _java_import_kurang(kode):
        return False
    return bool(re.search(r"\bstatic\s+void\s+main\s*\(", kode)
                and re.search(r"\b(class|record|enum)\s+\w+", kode)
                and _kurung_seimbang(kode))


def _go_lengkap(kode):
    return bool(re.search(r"^\s*package\s+main\b", kode, re.MULTILINE)
                and re.search(r"\bfunc\s+main\s*\(\s*\)", kode)
                and _kurung_seimbang(kode))


def _c_lengkap(kode):
    return bool(re.search(r"\b(?:int|void)\s+main\s*\(", kode)
                and _kurung_seimbang(kode))


def _js_lengkap(kode):
    # JavaScript tidak mewajibkan fungsi pembungkus, jadi apa pun yang utuh
    # secara struktur bisa dijalankan node.
    return _kurung_seimbang(kode)


def _csharp_lengkap(kode):
    # Sejak C# 9 ada top-level statement: berkas tanpa class dan tanpa Main
    # pun program yang sah. Jadi yang diperiksa DUA bentuk, bukan satu.
    punya_main = bool(re.search(r"\bstatic\s+(?:async\s+)?(?:void|int|Task)"
                                r"[\w<>\[\]]*\s+Main\s*\(", kode))
    if punya_main:
        return bool(re.search(r"\b(class|record|struct)\s+\w+", kode)
                    and _kurung_seimbang(kode))
    # Top-level: baris pertama berkode bukan deklarasi tipe, dan ada
    # pernyataan yang benar-benar mengerjakan sesuatu.
    ada_tipe = re.search(r"^\s*(?:public\s+|internal\s+)?"
                         r"(?:abstract\s+|sealed\s+|static\s+)?"
                         r"(class|interface|record|struct|enum)\s", kode,
                         re.MULTILINE)
    ada_panggilan = re.search(r"\w+\s*\([^)]*\)\s*;", kode)
    return bool(ada_panggilan and not ada_tipe and _kurung_seimbang(kode))


def _vb_lengkap(kode):
    return bool(re.search(r"^\s*(Module|Class)\s+\w+", kode,
                          re.MULTILINE | re.IGNORECASE)
                and re.search(r"^\s*Sub\s+Main\b", kode,
                              re.MULTILINE | re.IGNORECASE)
                and re.search(r"^\s*End\s+(Module|Class)\b", kode,
                              re.MULTILINE | re.IGNORECASE))


def _rust_lengkap(kode):
    return bool(re.search(r"\bfn\s+main\s*\(\s*\)", kode)
                and _kurung_seimbang(kode))


def _php_lengkap(kode):
    # Berkas PHP yang bisa dijalankan WAJIB dibuka dengan <?php. Tanpa itu,
    # seluruh isinya dicetak apa adanya sebagai teks -- bukan error, tapi juga
    # bukan yang dimaksud siapa pun.
    return bool(re.search(r"<\?php\b", kode) and _kurung_seimbang(kode))


def _ruby_lengkap(kode):
    # Ruby tidak punya titik masuk wajib: satu baris puts sudah program utuh.
    # Yang membuatnya BUKAN program cuma blok yang menggantung tanpa penutup.
    if not _kurung_seimbang(kode):
        return False
    pembuka = len(re.findall(r"^\s*(?:def|class|module|if|unless|case|while|"
                             r"until|begin|do)\b", kode, re.MULTILINE))
    penutup = len(re.findall(r"^\s*end\b", kode, re.MULTILINE))
    # `x if y` satu baris tidak butuh end; hitungan pembuka hanya mengambil
    # yang berada di AWAL baris, jadi bentuk itu tidak ikut terhitung.
    # Begitu juga method satu baris Ruby 3 (`def luas = @sisi**2`): tanpa
    # pengecualian ini, setiap program yang memakainya digolongkan potongan,
    # tombol Jalankan-nya hilang, dan blok Keluaran-nya tidak pernah diuji --
    # begitulah dua setter yang SyntaxError dan dua keluaran yang salah di
    # kurikulum Ruby lolos tanpa ketahuan.
    return penutup >= pembuka - _ruby_satu_baris(kode) - _ruby_def_satu_baris(kode)


# Method satu baris: `def nama = ...`, `def nama(x) = ...`, `def +(lain) = ...`,
# `def self.nama = ...`. Tanda `=` dipisah spasi dari nama/argumen; setter
# biasa `def warna=(w)` (tanda `=` menempel pada nama) tetap butuh `end`.
_RUBY_DEF_SATU_BARIS = re.compile(
    r"^\s*def\s+(?:self\.)?(?:[A-Za-z_]\w*[?!]?|[-+*/%<>=!~^&|\[\]]+)"
    r"(?:\([^)]*\))?\s+=\s", re.MULTILINE)


def _ruby_def_satu_baris(kode):
    """Berapa banyak `def` yang berbentuk method satu baris (tanpa `end`)."""
    return len(_RUBY_DEF_SATU_BARIS.findall(kode))


def _ruby_satu_baris(kode):
    """Berapa banyak `if`/`while` di awal baris yang sebenarnya satu baris."""
    n = 0
    for baris in kode.splitlines():
        b = baris.strip()
        if re.match(r"^(if|unless|while|until)\b", b) and b.endswith(("end", ";")):
            n += 1
    return n


def _kotlin_lengkap(kode):
    return bool(re.search(r"\bfun\s+main\s*\(", kode)
                and _kurung_seimbang(kode))


def _ts_lengkap(kode):
    # Sama seperti JavaScript: tidak ada fungsi pembungkus yang wajib.
    #
    # Kecuali satu hal: berkas KONFIGURASI berformat JSON (tsconfig.json,
    # package.json) juga berupa kurung kurawal yang seimbang, dan tanpa
    # pemeriksaan ini ia disebut "program TypeScript" -- lengkap dengan tombol
    # Jalankan yang selalu berakhir dengan galat compiler. Isinya memang kode,
    # tapi bukan kode yang dijalankan.
    if kode.lstrip().startswith("{"):
        try:
            json.loads(kode)
            return False
        except ValueError:
            pass
    return _kurung_seimbang(kode)


def _html_lengkap(kode):
    """Halaman utuh, bukan potongan markup.

    Yang dicari <html> atau <!doctype — bukan sekadar adanya tag. Sebagian
    besar contoh di materi HTML memang cuma beberapa elemen untuk menunjukkan
    satu hal, dan menyuruh pelajar menyimpan tiap potongan itu sebagai berkas
    justru mengaburkan mana yang benar-benar sebuah halaman.
    """
    rendah = kode.lower()
    return "<!doctype" in rendah or "<html" in rendah


def _bash_lengkap(kode):
    if re.search(r"^\s*(fi|done|esac|\})\s*$", kode.splitlines()[0] if kode.splitlines() else ""):
        return False
    return True


# Modul bawaan Node: mengimpornya tidak butuh `npm install`.
_NODE_BAWAAN = frozenset({
    "assert", "async_hooks", "buffer", "child_process", "cluster", "console",
    "constants", "crypto", "dgram", "diagnostics_channel", "dns", "domain",
    "events", "fs", "http", "http2", "https", "inspector", "module", "net",
    "os", "path", "perf_hooks", "process", "punycode", "querystring",
    "readline", "repl", "stream", "string_decoder", "sys", "test", "timers",
    "tls", "trace_events", "tty", "url", "util", "v8", "vm", "wasi",
    "worker_threads", "zlib", "sqlite", "sea",
})


def paket_luar(bahasa, kode):
    """Paket pihak ketiga yang diimpor di TINGKAT ATAS sebuah blok kode.

    Kurikulum tech stack penuh contoh React, Flask, Express, dan kawan-kawan.
    Contoh seperti itu memang program utuh, tapi aplikasi ini wajib jalan
    offline dan tidak memasang paket apa pun, jadi menawarkan tombol
    Jalankan untuknya berarti tombol yang selalu berakhir "module not found".
    Yang dihitung hanya import di kolom 0: import di dalam `try` (contoh yang
    sengaja menangkap ModuleNotFoundError) tetap bisa dijalankan.
    """
    if not kode:
        return []
    hasil = set()
    if bahasa == "python":
        bawaan = getattr(sys, "stdlib_module_names", frozenset())
        for m in re.finditer(r"^(?:from\s+([\w.]+)\s+import\b|import\s+([\w.]+(?:\s*,\s*[\w.]+)*))",
                             kode, re.MULTILINE):
            nama = [m.group(1)] if m.group(1) else [x.strip() for x in m.group(2).split(",")]
            for x in nama:
                atas = x.split(".")[0]
                # `# file kalkulator.py` di blok yang sama: modul lokal, bukan pip.
                if (atas and not x.startswith(".") and atas not in bawaan
                        and atas != "__future__"
                        and not re.search(rf"\b{re.escape(atas)}\.py\b", kode)):
                    hasil.add(atas)
    elif bahasa in ("javascript", "typescript"):
        for m in re.finditer(r"""^(?:import\s+(?:[^'"\n]*?\s+from\s+)?|(?:const|let|var)\s+[^=\n]+=\s*require\(\s*)['"]([^'"]+)['"]""",
                             kode, re.MULTILINE):
            spek = m.group(1)
            if spek.startswith((".", "/")):
                continue
            if spek.startswith("node:"):
                continue
            atas = "/".join(spek.split("/")[:2]) if spek.startswith("@") else spek.split("/")[0]
            if atas not in _NODE_BAWAAN:
                hasil.add(atas)
    elif bahasa in ("c", "cpp"):
        # Contoh Qt, SDL, Arduino, ESP-IDF: header di luar pustaka standar C,
        # POSIX, dan C++ (yang terakhir dikenali dari namanya: huruf kecil
        # tanpa titik, seperti <vector> dan <cstdio>).
        for m in re.finditer(r"^\s*#\s*include\s*<([^>]+)>", kode, re.MULTILINE):
            h = m.group(1).strip()
            if h in _C_BAWAAN or h.startswith(_C_FOLDER_BAWAAN) or re.fullmatch(r"[a-z_0-9]+", h):
                continue
            hasil.add(re.split(r"[/.]", h)[0])
    elif bahasa in ("java", "kotlin"):
        bawaan = ("java.", "javax.", "jdk.", "sun.", "com.sun.") + (
            ("kotlin.",) if bahasa == "kotlin" else ())
        # Paket milik proyek itu sendiri (`package com.toko.x;`) bukan paket luar.
        sendiri = tuple(".".join(p.split(".")[:2]) + "."
                        for p in re.findall(r"^package\s+([\w.]+)", kode, re.MULTILINE))
        for m in re.finditer(r"^import\s+(?:static\s+)?([\w.]+)", kode, re.MULTILINE):
            nama = m.group(1)
            if not nama.startswith(bawaan + sendiri):
                bag = nama.split(".")
                hasil.add(".".join(bag[:2]) if bag[0] in ("org", "com", "io", "net", "dev")
                          else bag[0])
    elif bahasa == "rust":
        # Nama crate selalu huruf kecil; `use Daftar::{Kons, Kosong}` itu enum
        # lokal, dan `use utils::x` menunjuk `mod utils` di berkas yang sama.
        lokal = set(re.findall(r"^\s*(?:pub\s+)?mod\s+(\w+)", kode, re.MULTILINE))
        for m in re.finditer(r"^(?:pub\s+)?(?:use\s+([a-z]\w*)::|extern\s+crate\s+([a-z]\w*))",
                             kode, re.MULTILINE):
            nama = m.group(1) or m.group(2)
            if nama not in ("std", "core", "alloc", "self", "super", "crate") and nama not in lokal:
                hasil.add(nama)
    elif bahasa == "go":
        # Pustaka standar Go tidak pernah memuat titik di ruas pertamanya;
        # github.com/..., golang.org/x/... selalu.
        blok = re.findall(r"^import\s*\((.*?)^\)", kode, re.MULTILINE | re.DOTALL)
        jalur = re.findall(r'^import\s+(?:[\w.]+\s+)?"([^"]+)"', kode, re.MULTILINE)
        jalur += [x for b in blok for x in re.findall(r'"([^"]+)"', b)]
        hasil.update(j for j in jalur if "." in j.split("/")[0])
    elif bahasa == "csharp":
        for m in re.finditer(r"^(?:global\s+)?using\s+(?:static\s+)?([\w.]+)\s*;", kode,
                             re.MULTILINE):
            nama = m.group(1)
            if nama.split(".")[0] != "System" and nama not in _CS_BAWAAN:
                hasil.add(nama)
    return sorted(hasil)


_C_BAWAAN = frozenset("""
assert.h complex.h ctype.h errno.h fenv.h float.h inttypes.h iso646.h limits.h locale.h
math.h setjmp.h signal.h stdalign.h stdarg.h stdatomic.h stdbit.h stdbool.h stdckdint.h
stddef.h stdint.h stdio.h stdlib.h stdnoreturn.h string.h tgmath.h threads.h time.h
uchar.h wchar.h wctype.h unistd.h fcntl.h pthread.h dirent.h netdb.h poll.h regex.h
semaphore.h spawn.h strings.h termios.h dlfcn.h glob.h libgen.h pwd.h grp.h sched.h
syslog.h utime.h aio.h fnmatch.h getopt.h mqueue.h err.h malloc.h alloca.h endian.h
byteswap.h execinfo.h ftw.h iconv.h langinfo.h monetary.h nl_types.h search.h tar.h
ulimit.h utmpx.h wordexp.h ifaddrs.h
""".split())
_C_FOLDER_BAWAAN = ("sys/", "netinet/", "arpa/", "linux/", "bits/", "net/", "asm/")
_CS_BAWAAN = frozenset({"Microsoft.Win32", "Microsoft.VisualBasic", "Microsoft.CSharp"})


def perintah_pasang_paket(bahasa, paket):
    """Perintah pasang yang diketik pelajar di proyeknya sendiri."""
    if bahasa == "python":
        return "pip install " + " ".join(paket)
    return "npm install " + " ".join(paket)


def cara_pasang(bahasa, paket):
    """Kalimat "pasang dulu ..." untuk keterangan blok yang butuh paket luar."""
    if bahasa in ("python", "javascript", "typescript"):
        return "Pasang dulu dengan: " + perintah_pasang_paket(bahasa, paket)
    if bahasa == "rust":
        return "Pasang dulu dengan: cargo add " + " ".join(paket)
    if bahasa == "go":
        return "Pasang dulu dengan: go get " + " ".join(paket)
    if bahasa in ("java", "kotlin"):
        return "Tambahkan dulu dependensinya lewat Maven atau Gradle"
    if bahasa == "csharp":
        return "Tambahkan dulu paket NuGet-nya (dotnet add package) atau SDK engine-nya"
    return "Pasang dulu pustakanya (atau SDK papannya) lalu tautkan saat kompilasi"


# Bahasa yang muncul di kurikulum tech stack tapi tidak punya runner di
# aplikasi ini: konfigurasi (YAML, Dockerfile, HCL), template framework
# (JSX, Vue), dialek SQL selain SQLite, dan bahasa yang belum punya
# kurikulum sendiri (Swift, Dart, Elixir, ...). Bagian materi menyebutnya
# lewat `"bahasa"`. Nilainya (nama tampilan, aturan penyorot terdekat atau
# None untuk polos). Blok seperti ini tidak pernah PROGRAM: menyebutnya
# "potongan dari kode yang lebih besar" juga salah untuk Dockerfile yang
# utuh, jadi petunjuknya sendiri (lihat petunjuk_kode).
BAHASA_LUAR = {
    "jsx": ("JSX", "javascript"), "tsx": ("TSX", "typescript"),
    "vue": ("komponen Vue", "html"), "svelte": ("komponen Svelte", "html"),
    "astro": ("komponen Astro", "html"), "angular": ("template Angular", "html"),
    "jinja": ("template Jinja", "html"), "blade": ("template Blade", "html"),
    "erb": ("template ERB", "html"), "scss": ("SCSS", "css"), "less": ("Less", "css"),
    "json": ("JSON", "javascript"), "yaml": ("YAML", None), "toml": ("TOML", None),
    "xml": ("XML", "html"), "ini": ("INI", None), "env": ("berkas .env", "bash"),
    "markdown": ("Markdown", None), "http": ("permintaan HTTP", None),
    "dockerfile": ("Dockerfile", "bash"), "makefile": ("Makefile", "bash"),
    "hcl": ("HCL Terraform", None), "nginx": ("konfigurasi nginx", None),
    "nix": ("Nix", None), "bicep": ("Bicep", None), "rego": ("Rego", None),
    "powershell": ("PowerShell", "bash"), "cmake": ("CMake", None),
    "gradle": ("Gradle", "kotlin"), "graphql": ("GraphQL", None),
    "protobuf": ("Protocol Buffers", None), "prisma": ("skema Prisma", None),
    "postgresql": ("SQL PostgreSQL", "sql"), "mysql": ("SQL MySQL", "sql"),
    "tsql": ("T-SQL", "sql"), "plsql": ("PL/SQL", "sql"), "cql": ("CQL Cassandra", "sql"),
    "cypher": ("Cypher", None), "mongosh": ("shell MongoDB", "javascript"),
    "redis": ("perintah Redis", None), "promql": ("PromQL", None),
    "swift": ("Swift", None), "objectivec": ("Objective-C", "c"), "dart": ("Dart", None),
    "scala": ("Scala", None), "groovy": ("Groovy", None), "clojure": ("Clojure", None),
    "elixir": ("Elixir", None), "erlang": ("Erlang", None), "haskell": ("Haskell", None),
    "ocaml": ("OCaml", None), "fsharp": ("F#", None), "lua": ("Lua", None),
    "r": ("R", None), "julia": ("Julia", None), "perl": ("Perl", None),
    "zig": ("Zig", None), "nim": ("Nim", None), "crystal": ("Crystal", "ruby"),
    "gleam": ("Gleam", None), "v": ("V", None), "mojo": ("Mojo", "python"),
    "solidity": ("Solidity", None), "matlab": ("MATLAB", None), "fortran": ("Fortran", None),
    "cobol": ("COBOL", None), "ada": ("Ada", None), "pascal": ("Pascal/Delphi", None),
    "prolog": ("Prolog", None), "lisp": ("Lisp", None), "racket": ("Racket", None),
    "assembly": ("Assembly", None), "wat": ("WebAssembly teks", None),
    "gdscript": ("GDScript", "python"), "glsl": ("GLSL", "c"), "hlsl": ("HLSL", "c"),
    "cuda": ("CUDA C++", "cpp"), "arduino": ("Arduino C++", "cpp"),
    "micropython": ("MicroPython", "python"), "apex": ("Apex", "java"),
    "abap": ("ABAP", None), "vba": ("VBA", "vb"),
    "awk": ("Awk", "bash"), "tcl": ("Tcl", None), "raku": ("Raku", None), "d": ("D", "c"),
    "verilog": ("Verilog", None), "vhdl": ("VHDL", None), "rpg": ("RPG", None),
    "pli": ("PL/I", None), "apl": ("APL", None), "q": ("q/kdb+", None), "j": ("J", None),
    "xpp": ("X++", "csharp"), "cfml": ("CFML", "html"), "vyper": ("Vyper", "python"),
    "haxe": ("Haxe", None), "odin": ("Odin", None), "carbon": ("Carbon", "cpp"),
    "roc": ("Roc", None), "lean": ("Lean", None), "moonbit": ("MoonBit", None),
    "luau": ("Luau", None), "smalltalk": ("Smalltalk", None), "sas": ("SAS", None),
    "wolfram": ("Wolfram", None), "coffeescript": ("CoffeeScript", None),
    "elm": ("Elm", None), "purescript": ("PureScript", None), "rescript": ("ReScript", None),
    "idris": ("Idris", None), "agda": ("Agda", None), "rocq": ("Rocq (Coq)", None),
    "scheme": ("Scheme", None), "sml": ("Standard ML", None), "basic": ("BASIC", "vb"),
    "ballerina": ("Ballerina", None), "cairo": ("Cairo", None), "move": ("Move", None),
    "st": ("Structured Text", None), "hack": ("Hack", "php"), "rexx": ("REXX", None),
    "jcl": ("JCL", None), "terraform": ("HCL Terraform", None),
    # JavaScript yang memakai document/window: utuh, tapi cuma hidup di browser.
    "browser": ("JavaScript untuk browser", "javascript"),
    "forth": ("Forth", None), "gml": ("GML GameMaker", "javascript"),
    "batch": ("Batch Windows", None), "actionscript": ("ActionScript", "javascript"),
    "foxpro": ("Visual FoxPro", None),
    "razor": ("komponen Razor", "html"), "templ": ("templ Go", "html"),
    "heex": ("template HEEx", "html"), "jdl": ("JDL JHipster", None),
    "gherkin": ("Gherkin", None), "diff": ("diff", None),
    "firestore": ("aturan Firestore", "javascript"), "fastfile": ("Fastfile fastlane", "ruby"),
    "caddyfile": ("Caddyfile", None),
}


def sorot_untuk(bahasa):
    """Aturan penyorot untuk `"bahasa"` sebuah bagian materi."""
    if bahasa in ("terminal", "teks"):
        return "bash" if bahasa == "terminal" else "teks"
    if bahasa in BAHASA_LUAR:
        return BAHASA_LUAR[bahasa][1] or bahasa
    return bahasa


def jenis_kode(bahasa, kode, abaikan_paket=False):
    """Klasifikasikan blok kode: PROGRAM, MULTI, POTONGAN, atau SESI.

    `abaikan_paket=True` menjawab "seandainya paketnya terpasang": dipakai
    `butuh_paket` supaya petunjuk "butuh paket X" cuma muncul pada program
    utuh, bukan pada potongan yang kebetulan memuat import.
    """
    if not kode or not kode.strip():
        return POTONGAN
    if bahasa == "teks":
        # Diagram atau tabel yang ditandai eksplisit oleh penulisnya, jadi
        # tidak bergantung pada tebakan _ilustrasi().
        return ILUSTRASI
    if bahasa == "terminal":
        # Blok perintah di kurikulum tech stack (docker, kubectl, npm,
        # terraform, ...) memakai `"bahasa": "terminal"`. Semuanya diketik
        # pelajar di mesinnya sendiri dan bisa mengubah sistemnya, jadi tidak
        # ada satu pun yang boleh dijalankan aplikasi -- pagar yang sama
        # dengan materi Fedora, tanpa pengecualian shebang.
        #
        # Diperiksa SEBELUM _ilustrasi(): perintah berkolom seperti
        # `npm init -y   # bikin package.json` lolos tebakan diagram, dan
        # yang terbaca pelajar jadi "bukan kode, tidak perlu diketik" untuk
        # perintah yang justru harus ia ketik sendiri.
        return SESI
    if berkas_ganda(kode):
        return MULTI
    if bahasa in BAHASA_LUAR:
        return POTONGAN
    if _ilustrasi(kode):
        return ILUSTRASI
    if _ada_elipsis(kode) or _diawali_indentasi(kode):
        return POTONGAN

    if bahasa == "sql":
        # Query yang membuat tabelnya sendiri bisa disimpan sebagai berkas.
        # Selebihnya mengandalkan tabel dari materi sebelumnya, jadi harus
        # diketik di sesi database yang sudah berisi data.
        return PROGRAM if re.search(r"\bCREATE\s+TABLE\b", kode, re.I) else SESI

    if bahasa in ("fedora", "git"):
        # Blok materi CLI berisi PERINTAH yang diketik manusia di terminal --
        # termasuk `sudo dnf5 install` dan `systemctl enable`. Menyebutnya
        # "program utuh" berarti aplikasi menawarkan tombol Jalankan yang
        # benar-benar mengeksekusinya di mesin pelajar, mengubah sistemnya
        # tanpa ia memintanya. Hanya blok yang memang berupa SKRIP -- ditandai
        # shebang di baris pertama -- yang disebut berkas.
        #
        # Git ikut aturan yang sama persis. `git reset --hard`, `git push
        # --force`, dan `git clean -fd` di materinya ditujukan ke repositori
        # MILIK PELAJAR, dan satu-satunya tempat yang aman untuk itu adalah
        # terminalnya sendiri. Latihannya (bershebang) membuat repositori
        # sendiri di mktemp -d, jadi yang itu memang boleh dijalankan.
        return PROGRAM if kode.lstrip().startswith("#!") else SESI

    if bahasa == "html":
        return PROGRAM if _html_lengkap(kode) else POTONGAN
    if bahasa == "css":
        # Satu blok aturan pun sudah berupa berkas gaya yang sah dan bisa
        # ditautkan apa adanya. CSS tidak punya "titik masuk" yang harus ada.
        return PROGRAM if "{" in kode and "}" in kode else POTONGAN

    pemeriksa = {
        "python": _python_lengkap,
        "java": _java_lengkap,
        "go": _go_lengkap,
        "c": _c_lengkap,
        "cpp": _c_lengkap,
        "javascript": _js_lengkap,
        "bash": _bash_lengkap,
        "csharp": _csharp_lengkap,
        "vb": _vb_lengkap,
        "rust": _rust_lengkap,
        "php": _php_lengkap,
        "ruby": _ruby_lengkap,
        "kotlin": _kotlin_lengkap,
        "typescript": _ts_lengkap,
    }.get(bahasa)

    if pemeriksa is None:
        return POTONGAN
    if not pemeriksa(kode):
        return POTONGAN
    # Program utuh, tapi butuh paket yang tidak terpasang di aplikasi ini.
    if abaikan_paket:
        return PROGRAM
    return POTONGAN if paket_luar(bahasa, kode) else PROGRAM


def butuh_paket(bahasa, kode):
    """Paket luar sebuah blok yang sebenarnya program utuh; [] untuk lainnya."""
    paket = paket_luar(bahasa, kode)
    if paket and jenis_kode(bahasa, kode, abaikan_paket=True) == PROGRAM:
        return paket
    return []


# ------------------------------------------------------------------ petunjuk

LABEL_SESI = {
    "terminal": ("Ketik di terminalmu sendiri",
                 "Perintah ini dijalankan di mesinmu dan bisa memasang atau "
                 "mengubah sesuatu, jadi baca dulu. Aplikasi tidak menjalankannya."),
    "sql": ("Ketik langsung di sesi database (mysql atau sqlite3)",
            "Perlu tabel dari materi sebelumnya, jadi bukan berkas terpisah."),
    "fedora": ("Ketik langsung di terminal",
               "Perintah ini mengubah sistemmu sendiri, jadi BACA dulu sebelum "
               "menjalankannya. Yang berawalan sudo perlu hak administrator."),
    "git": ("Ketik langsung di terminal, di dalam repositorimu",
            "Perintah ini mengubah riwayat repositori yang sedang kamu buka, "
            "jadi BACA dulu; reset --hard dan push --force tidak bisa dibatalkan "
            "sembarangan."),
}


# Boleh tidak APLIKASI menjalankan sebuah blok atas nama pelajar?
#
# PROGRAM selalu boleh: itu memang berkas utuh, dan runner menjalankannya di
# direktori sementara dengan batas sumber daya.
#
# SESI yang menjebak. Namanya satu, konsekuensinya dua:
#
#   sql    : sesinya adalah sqlite3 yang dinyalakan aplikasi sendiri. Aman,
#            dan memang gunanya -- pelajar bisa mencoba query dari materi.
#   fedora : sesinya adalah TERMINAL MILIK PELAJAR. Blok seperti
#            `sudo dnf5 install`, `systemctl enable`, dan `mkfs.ext4` hanya
#            bermakna kalau ia sendiri yang mengetiknya. Menjalankannya atas
#            namanya berarti mengubah sistemnya tanpa ia meminta.
#   git    : sama dengan fedora -- sesinya repositori milik pelajar, dan
#            `reset --hard` atau `push --force` di sana mengubah riwayat
#            sungguhan. Yang boleh dijalankan cuma skrip latihan bershebang.
#
# Menyamakan keduanya PERNAH terjadi: `bisa_dijalankan` dulu berbunyi
# `jenis in (PROGRAM, SESI)`, dan halaman materi Fedora menawarkan tombol
# Jalankan pada empat blok perintah sekaligus -- salah satunya rm. Aturannya
# tinggal di sini, sebelah klasifikasinya, supaya tidak ada tempat kedua yang
# bisa melenceng.
SESI_BOLEH_DIJALANKAN = frozenset({"sql"})


def boleh_dijalankan_aplikasi(bahasa, jenis):
    """Boleh tidak aplikasi mengeksekusi blok ini atas nama pelajar?"""
    if jenis == PROGRAM:
        return True
    if jenis == SESI:
        return (bahasa or "").lower() in SESI_BOLEH_DIJALANKAN
    return False


def petunjuk_kode(bahasa, kode, konteks=""):
    """Susun instruksi lengkap untuk satu blok kode materi."""
    jenis = jenis_kode(bahasa, kode)

    if jenis == MULTI:
        daftar = berkas_ganda(kode)
        return Petunjuk(
            MULTI, berkas=daftar,
            instruksi="Buat " + str(len(daftar)) + " berkas terpisah: "
                      + ", ".join(daftar),
            keterangan="Pisahkan sesuai komentar penanda di dalam kode.",
        )

    if jenis == ILUSTRASI:
        return Petunjuk(
            ILUSTRASI,
            instruksi="Diagram / ilustrasi - bukan kode, tidak perlu diketik",
        )

    if jenis == SESI:
        instruksi, keterangan = LABEL_SESI.get(
            bahasa, ("Ketik langsung di sesi interaktif", ""))
        return Petunjuk(SESI, instruksi=instruksi, keterangan=keterangan)

    if bahasa in BAHASA_LUAR:
        nama = BAHASA_LUAR[bahasa][0]
        return Petunjuk(
            POTONGAN,
            instruksi=f"Contoh {nama}: dibaca di sini, dicoba di proyekmu",
            keterangan=f"Aplikasi ini tidak menjalankan {nama}. "
                       "Salin ke proyekmu sendiri kalau mau mencobanya.",
        )

    paket = butuh_paket(bahasa, kode) if jenis == POTONGAN else []
    if paket:
        return Petunjuk(
            POTONGAN,
            instruksi="Butuh paket " + ", ".join(paket) + ": coba di proyekmu sendiri",
            keterangan=cara_pasang(bahasa, paket)
                       + ". Aplikasi ini tidak memasang paket, jadi tidak menjalankannya.",
        )

    if jenis == POTONGAN:
        return Petunjuk(
            POTONGAN,
            instruksi="Potongan contoh - tidak perlu dibuat berkas",
            keterangan="Bagian dari kode yang lebih besar, akan error kalau dijalankan sendiri.",
        )

    nama = nama_berkas(bahasa, kode, konteks)
    perintah = perintah_jalan(bahasa, nama)
    return Petunjuk(PROGRAM, nama=nama, perintah=perintah,
                    instruksi=f"Buat berkas: {nama}")


def petunjuk_latihan(bahasa, nama):
    """Instruksi untuk latihan, di mana nama berkasnya sudah ditentukan aplikasi."""
    return Petunjuk(PROGRAM, nama=nama, perintah=perintah_jalan(bahasa, nama),
                    instruksi=f"Berkas jawabanmu: {nama}")
