"""Menjalankan kode yang ditulis user, dengan batas waktu dan memori.

Kode latihan ditulis oleh pemula, jadi asumsikan yang terburuk: infinite loop,
alokasi memori kebablasan, atau output tak berujung. Semua dibatasi di sini.

Ini BUKAN sandbox keamanan. Kode berjalan sebagai user yang sama dengan aplikasi.
Jangan pernah menjalankan kode dari sumber yang tidak dipercaya.
"""

import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field

try:
    import resource  # POSIX saja
except ImportError:
    resource = None

BATAS_WAKTU_DETIK = 10
BATAS_MEMORI_MB = 512
BATAS_FILE_MB = 16
BATAS_OUTPUT_CHAR = 20_000


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
    kompilasi: object = None          # fn(dir, path) -> list[str] | None
    jalankan: object = None           # fn(dir, path) -> list[str]
    cek_sintaks: object = None        # fn(dir, path) -> list[str] | None
    batasi_memori: bool = True
    nama_file: object = None          # fn(kode) -> nama file
    catatan: str = ""
    stdin_dari_file: bool = False     # jalankan sebagai `cmd < file`
    argumen_ekstra: list = field(default_factory=list)


def _nama_kelas_java(kode):
    """Ambil nama public class supaya nama file cocok dengan syarat javac."""
    m = re.search(r"\bpublic\s+(?:final\s+|abstract\s+)?class\s+([A-Za-z_]\w*)", kode)
    if m:
        return m.group(1)
    m = re.search(r"\bclass\s+([A-Za-z_]\w*)", kode)
    return m.group(1) if m else "Main"


TOOLCHAINS = {
    "python": Toolchain(
        key="python", label="Python", ekstensi=".py", butuh=["python3"],
        jalankan=lambda d, p: ["python3", "-I", p],
        cek_sintaks=lambda d, p: ["python3", "-m", "py_compile", p],
    ),
    "javascript": Toolchain(
        key="javascript", label="JavaScript", ekstensi=".js", butuh=["node"],
        jalankan=lambda d, p: ["node", p],
        cek_sintaks=lambda d, p: ["node", "--check", p],
        batasi_memori=False,  # V8 memesan address space besar sejak awal
    ),
    "java": Toolchain(
        key="java", label="Java", ekstensi=".java", butuh=["javac", "java"],
        nama_file=lambda kode: _nama_kelas_java(kode) + ".java",
        kompilasi=lambda d, p: ["javac", "-nowarn", "-d", d, p],
        jalankan=lambda d, p: ["java", "-XX:+UseSerialGC", "-Xmx256m", "-cp", d,
                               os.path.basename(p)[:-5]],
        batasi_memori=False,  # JVM butuh address space besar; dibatasi lewat -Xmx
    ),
    "c": Toolchain(
        key="c", label="C", ekstensi=".c", butuh=["gcc"],
        kompilasi=lambda d, p: ["gcc", "-std=c11", "-Wall", p, "-o",
                                os.path.join(d, "program"), "-lm"],
        jalankan=lambda d, p: [os.path.join(d, "program")],
    ),
    "cpp": Toolchain(
        key="cpp", label="C++", ekstensi=".cpp", butuh=["g++"],
        kompilasi=lambda d, p: ["g++", "-std=c++17", "-Wall", p, "-o",
                                os.path.join(d, "program")],
        jalankan=lambda d, p: [os.path.join(d, "program")],
    ),
    "sql": Toolchain(
        key="sql", label="SQL", ekstensi=".sql", butuh=["sqlite3"],
        jalankan=lambda d, p: ["sqlite3", "-batch", "-init", os.devnull, ":memory:"],
        stdin_dari_file=True,
        catatan=("Dijalankan pakai SQLite, bukan MySQL. Sebagian besar SQL standar "
                 "jalan normal, tapi fitur khas MySQL (AUTO_INCREMENT, ENGINE=InnoDB, "
                 "SHOW TABLES) tidak dikenali."),
    ),
    "bash": Toolchain(
        key="bash", label="Bash", ekstensi=".sh", butuh=["bash"],
        jalankan=lambda d, p: ["bash", p],
        cek_sintaks=lambda d, p: ["bash", "-n", p],
    ),
    "go": Toolchain(
        key="go", label="Go", ekstensi=".go", butuh=["go"],
        nama_file=lambda kode: "main.go",
        jalankan=lambda d, p: ["go", "run", p],
        batasi_memori=False,
    ),
}


def tersedia(bahasa):
    """True kalau semua program yang dibutuhkan bahasa ini ada di PATH."""
    tc = TOOLCHAINS.get(bahasa)
    if not tc:
        return False
    return all(shutil.which(prog) for prog in tc.butuh)


def program_hilang(bahasa):
    tc = TOOLCHAINS.get(bahasa)
    if not tc:
        return []
    return [p for p in tc.butuh if not shutil.which(p)]


def daftar_tersedia():
    return {k: tersedia(k) for k in TOOLCHAINS}


def _batas(tc, timeout):
    if resource is None:
        return None

    def terapkan():
        cpu = max(1, int(timeout) + 1)
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


def _proses(cmd, cwd, tc, timeout, stdin_data=None, stdin_file=None):
    """Jalankan satu proses, kembalikan (kode_keluar, stdout, stderr, timeout?)."""
    lingkungan = dict(os.environ)
    lingkungan["HOME"] = cwd
    lingkungan.pop("PYTHONPATH", None)
    lingkungan["PYTHONDONTWRITEBYTECODE"] = "1"
    if tc.key == "go":
        lingkungan.setdefault("GOCACHE", os.path.join(cwd, ".gocache"))
        lingkungan.setdefault("GOPATH", os.path.join(cwd, ".gopath"))

    fh = None
    try:
        # subprocess.run() menolak `stdin` dan `input` sekaligus, jadi pilih salah satu.
        opsi_stdin = {}
        if stdin_file:
            fh = open(stdin_file, "rb")
            opsi_stdin["stdin"] = fh
        else:
            opsi_stdin["input"] = (stdin_data or "").encode("utf-8")

        proc = subprocess.run(
            cmd,
            cwd=cwd,
            env=lingkungan,
            capture_output=True,
            timeout=timeout,
            preexec_fn=_batas(tc, timeout) if resource else None,
            **opsi_stdin,
        )
        return (
            proc.returncode,
            proc.stdout.decode("utf-8", errors="replace"),
            proc.stderr.decode("utf-8", errors="replace"),
            False,
        )
    except subprocess.TimeoutExpired as e:
        keluar = (e.stdout or b"").decode("utf-8", errors="replace")
        return 124, keluar, "", True
    except (OSError, ValueError) as e:
        return 127, "", f"Gagal menjalankan: {e}", False
    finally:
        if fh:
            fh.close()


def jalankan(bahasa, kode, stdin="", timeout=BATAS_WAKTU_DETIK):
    """Kompilasi (kalau perlu) lalu jalankan `kode`. Selalu return objek Hasil."""
    tc = TOOLCHAINS.get(bahasa)
    if tc is None:
        return Hasil(False, galat=f"Bahasa '{bahasa}' belum didukung runner.", fase="setup")

    hilang = program_hilang(bahasa)
    if hilang:
        return Hasil(
            False,
            galat=f"Program belum terpasang: {', '.join(hilang)}",
            fase="setup",
            catatan=f"Pasang dulu {' & '.join(hilang)} untuk menjalankan kode {tc.label}.",
        )

    with tempfile.TemporaryDirectory(prefix="belajar-") as d:
        nama = tc.nama_file(kode) if tc.nama_file else ("program" + tc.ekstensi)
        path = os.path.join(d, nama)
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(kode)
        except OSError as e:
            return Hasil(False, galat=f"Gagal menulis file sementara: {e}", fase="setup")

        if tc.kompilasi:
            cmd = tc.kompilasi(d, path)
            rc, out, err, to = _proses(cmd, d, tc, timeout)
            if to:
                return Hasil(False, galat="Kompilasi terlalu lama, dihentikan.",
                             fase="kompilasi", timeout=True, catatan=tc.catatan)
            if rc != 0:
                return Hasil(False, keluaran=_potong(out), galat=_potong(err or "Kompilasi gagal."),
                             kode_keluar=rc, fase="kompilasi", catatan=tc.catatan)

        cmd = tc.jalankan(d, path)
        if tc.stdin_dari_file:
            rc, out, err, to = _proses(cmd, d, tc, timeout, stdin_file=path)
        else:
            rc, out, err, to = _proses(cmd, d, tc, timeout, stdin_data=stdin)

        if to:
            return Hasil(False, keluaran=_potong(out),
                         galat=f"Program dihentikan setelah {timeout} detik. "
                               "Kemungkinan ada loop yang tidak pernah berhenti.",
                         fase="jalan", timeout=True, catatan=tc.catatan)

        return Hasil(rc == 0, keluaran=_potong(out), galat=_potong(err),
                     kode_keluar=rc, fase="jalan", catatan=tc.catatan)


# ------------------------------------------------------------- pengecek jawaban

def normalisasi(teks):
    """Samakan output supaya beda spasi/baris kosong tidak dianggap salah."""
    baris = [b.rstrip() for b in teks.replace("\r\n", "\n").strip().split("\n")]
    while baris and not baris[-1]:
        baris.pop()
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


def cek_sintaks(bahasa, kode, timeout=BATAS_WAKTU_DETIK):
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

    with tempfile.TemporaryDirectory(prefix="belajar-cek-") as d:
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


def periksa(bahasa, kode, tests, timeout=BATAS_WAKTU_DETIK):
    """Jalankan kode untuk tiap test case.

    Format satu test:
        {"nama": "...", "stdin": "", "harapan": "...", "mode": "persis"}

    Mode: persis | abaikan_kapital | mengandung | regex | angka

    Return (semua_lulus, [HasilUji], Hasil_terakhir).
    """
    hasil_uji = []
    hasil_jalan = None

    # Sintaks rusak = semua test pasti gagal. Laporkan sekali saja.
    rusak = cek_sintaks(bahasa, kode, timeout)
    if rusak is not None:
        t = tests[0] if tests else {}
        return False, [HasilUji(t.get("nama") or "Uji 1", False,
                                t.get("harapan", ""), "", rusak.galat,
                                t.get("mode", "persis"), t.get("stdin", ""))], rusak

    for i, t in enumerate(tests, start=1):
        nama = t.get("nama") or f"Uji {i}"
        stdin = t.get("stdin", "")
        harapan = t.get("harapan", "")
        mode = t.get("mode", "persis")

        hasil_jalan = jalankan(bahasa, kode, stdin=stdin, timeout=timeout)
        if not hasil_jalan.sukses and hasil_jalan.fase in ("kompilasi", "setup"):
            hasil_uji.append(HasilUji(nama, False, harapan, hasil_jalan.keluaran,
                                      hasil_jalan.galat, mode, stdin))
            break  # kompilasi gagal -> test berikutnya pasti gagal juga

        lulus = _cocok(hasil_jalan.keluaran, harapan, mode)
        if hasil_jalan.timeout:
            lulus = False
        hasil_uji.append(HasilUji(nama, lulus, harapan, hasil_jalan.keluaran,
                                  hasil_jalan.galat, mode, stdin))

    semua = bool(hasil_uji) and all(h.lulus for h in hasil_uji)
    return semua, hasil_uji, hasil_jalan
