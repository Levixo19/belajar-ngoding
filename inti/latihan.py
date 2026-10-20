"""Logika latihan: nama berkas kerja, kerangka editor, dan kunci jawaban.

Dulu semua ini tinggal di `layar/exercises.py`, dan `webapp/api.py`
mengimpornya dari sana. AGENTS.md sudah lama mencatatnya sebagai warisan:
`bangun_tests`, `DIR_KERJA`, dan `_kerangka` adalah LOGIKA latihan, bukan
tampilan terminal, jadi lapisan web tidak seharusnya menarik seluruh paket
antarmuka terminal hanya untuk memakainya.

Yang ada di sini tidak mencetak apa pun. Kelulusan tetap ditentukan
`runner.periksa`, dan kunci jawabannya tetap diturunkan dengan menjalankan
solusi contoh -- satu definisi "lulus", seperti sebelumnya.
"""

import os
import re

from inti import berkas
from inti import runner


DIR_KERJA = os.environ.get(
    "BELAJAR_WORKSPACE",
    os.path.join(os.path.expanduser("~"), "belajar-ngoding", "kerjaanku"),
)

def _slug(teks):
    teks = re.sub(r"[^\w\s-]", "", teks).strip().lower()
    return re.sub(r"[\s_-]+", "-", teks) or "latihan"


def nama_kerja(ex, bahasa):
    """Nama berkas kerja untuk sebuah latihan. Fungsi MURNI, tanpa efek samping.

    Untuk Java, nama berkas wajib sama dengan nama kelas public. Versi lama
    membentuknya dari digit di judul (`"Latihan" + digit or "Latihan"`), yang
    punya dua cacat: presedensi `+` membuat cabang `or` jadi kode mati, dan dua
    judul tanpa angka -- atau bernomor "1 (bagian 2)" vs "12" -- memetakan ke
    berkas yang sama sehingga jawaban pelajar saling menimpa.
    """
    tc = runner.TOOLCHAINS.get(bahasa)
    ext = tc.ekstensi if tc else ".txt"

    if bahasa == "java":
        potongan = [p for p in _slug(ex["title"]).split("-") if p]
        kelas = "".join(p.capitalize() for p in potongan) or "Latihan"
        if not kelas[0].isalpha():
            kelas = "Latihan" + kelas
        return kelas + ext

    return _slug(ex["title"]) + ext


def _path_kerja(kategori, ex, bahasa, buat_folder=True):
    folder = os.path.join(DIR_KERJA, kategori)
    if buat_folder:
        os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, nama_kerja(ex, bahasa))


def _kerangka(bahasa, ex):
    """Template awal supaya user tidak mulai dari halaman kosong."""
    judul = ex["title"]
    if bahasa == "java":
        kelas = nama_kerja(ex, "java")[:-5]
        return (f"// {judul}\npublic class {kelas} {{\n"
                f"    public static void main(String[] args) {{\n"
                f"        // tulis kodemu di sini\n    }}\n}}\n")
    if bahasa == "c":
        return (f"// {judul}\n#include <stdio.h>\n\nint main(void) {{\n"
                f"    // tulis kodemu di sini\n    return 0;\n}}\n")
    if bahasa == "cpp":
        return (f"// {judul}\n#include <iostream>\nusing namespace std;\n\nint main() {{\n"
                f"    // tulis kodemu di sini\n    return 0;\n}}\n")
    if bahasa == "javascript":
        return f"// {judul}\n// tulis kodemu di sini\n"
    if bahasa == "go":
        return (f"// {judul}\npackage main\n\nimport \"fmt\"\n\nfunc main() {{\n"
                f"\t// tulis kodemu di sini\n\t_ = fmt.Sprint\n}}\n")
    if bahasa == "bash":
        return f"#!/usr/bin/env bash\n# {judul}\n# tulis kodemu di sini\n"
    if bahasa == "sql":
        return f"-- {judul}\n-- tulis query-mu di sini\n"
    if bahasa == "csharp":
        return (f"// {judul}\nusing System;\n\nclass Program\n{{\n"
                f"    static void Main()\n    {{\n"
                f"        // tulis kodemu di sini\n    }}\n}}\n")
    if bahasa == "vb":
        return (f"' {judul}\nImports System\n\nModule Program\n"
                f"    Sub Main()\n        ' tulis kodemu di sini\n"
                f"    End Sub\nEnd Module\n")
    if bahasa == "rust":
        return (f"// {judul}\nfn main() {{\n"
                f"    // tulis kodemu di sini\n}}\n")
    if bahasa == "php":
        return f"<?php\n// {judul}\n// tulis kodemu di sini\n"
    if bahasa == "ruby":
        return f"# {judul}\n# tulis kodemu di sini\n"
    if bahasa == "kotlin":
        return (f"// {judul}\nfun main() {{\n"
                f"    // tulis kodemu di sini\n}}\n")
    if bahasa == "typescript":
        return f"// {judul}\n// tulis kodemu di sini\n"
    if bahasa == "html":
        # Komentar HTML, bukan `#`: baris `# ...` di HTML adalah TEKS
        # halaman, jadi kerangka itu sendiri ikut jadi simpul di pohon yang
        # dinilai dan jawaban yang benar pun dinyatakan gagal.
        return f"<!-- {judul} -->\n<!-- tulis kodemu di sini -->\n"
    if bahasa == "css":
        # Sama: `# ...` di CSS menelan pemilih pertama sesudahnya.
        return f"/* {judul} */\n/* tulis kodemu di sini */\n"
    if bahasa == "fedora":
        return (f"#!/usr/bin/env bash\n#\n# {judul}\n\n"
                f"set -euo pipefail\n\n# tulis kodemu di sini\n")
    if bahasa == "git":
        # Setiap latihan Git bekerja di repositori sementara miliknya
        # sendiri. Kerangkanya sudah membuat dan membersihkan direktori itu,
        # supaya skrip yang salah ketik tidak pernah menyentuh repositori
        # sungguhan di komputer pelajar.
        return (f"#!/usr/bin/env bash\n#\n# {judul}\n\n"
                f"set -euo pipefail\n\n"
                f"# Bekerja di direktori sementara supaya repositorimu sendiri "
                f"tidak tersentuh.\n"
                f"kerja=\"$(mktemp -d)\"\n"
                f"trap 'rm -rf \"$kerja\"' EXIT\n"
                f"cd \"$kerja\"\n\n# tulis kodemu di sini\n")
    return f"# {judul}\n# tulis kodemu di sini\n"


# ---------------------------------------------------------------- menulis kode



def bisa_dinilai(ex, bahasa):
    """(boleh_dinilai, alasan) -- sebagian latihan memang tidak bisa diperiksa.

    Contohnya latihan yang butuh pustaka eksternal (pytest, JUnit, driver JDBC)
    atau memakai fitur khas MySQL yang tidak ada di SQLite.
    """
    if ex.get("auto_check") is False:
        return False, ex.get("alasan_tidak_dicek",
                             "Latihan ini tidak bisa dinilai otomatis.")
    if not runner.tersedia(bahasa):
        hilang = ", ".join(runner.program_hilang(bahasa))
        return False, f"Toolchain belum terpasang: {hilang}"
    return True, ""


def baris_setup(ex):
    """Berapa baris yang ditempel di DEPAN kode pelajar oleh `gabung_setup`."""
    awal = ex.get("setup", "")
    if not awal.strip():
        return 0
    return len(awal.rstrip().splitlines()) + 1   # +1 untuk baris kosong pemisah


def gabung_setup(ex, kode):
    """Bungkus kode user dengan kode prasyarat dan kode pemeriksa.

    `setup`      ditempel SEBELUM kode user.
        Latihan SQL sering mengandalkan tabel yang dibuat di latihan
        sebelumnya, sementara tiap eksekusi memakai database kosong.
        Field ini menyediakan kondisi awal supaya latihan berdiri sendiri.

    `verifikasi` ditempel SESUDAH kode user.
        Untuk latihan yang tidak mencetak apa pun (misalnya INSERT murni),
        perbandingan output jadi tak bermakna karena kode kosong pun lolos.
        Field ini menampilkan kondisi akhir agar ada yang bisa dibandingkan.
    """
    bagian = []
    if ex.get("setup", "").strip():
        bagian.append(ex["setup"].rstrip())
    bagian.append(kode)
    if ex.get("verifikasi", "").strip():
        bagian.append(ex["verifikasi"].rstrip())
    return "\n\n".join(bagian)


# Kunci jawaban diturunkan dengan MENJALANKAN solusi contoh. Untuk Java dan Go
# itu berarti kompilasi penuh setiap kali pelajar menekan "periksa" -- belasan
# detik menunggu untuk hasil yang selalu sama. Solusi wajib deterministik
# (dijamin tests/test_solutions.py), jadi hasilnya aman di-cache selama sesi.
_CACHE_TESTS = {}


def bersihkan_cache():
    _CACHE_TESTS.clear()


def bangun_tests(ex, bahasa):
    """Tentukan test case untuk sebuah latihan.

    Prioritas:
      1. Field `tests` di data soal.
      2. Turunan otomatis: jalankan solusi contoh, output-nya jadi ekspektasi.

    Return (tests, pesan_error). `tests` kosong berarti hanya bisa mode jalankan.
    """
    boleh, alasan = bisa_dinilai(ex, bahasa)
    if not boleh:
        return [], alasan

    if ex.get("tests"):
        return list(ex["tests"]), ""

    stdins = ex.get("stdin_list") or [ex.get("stdin", "")]
    mode = ex.get("mode", "persis")
    kunci_cache = (bahasa, ex["title"], tuple(stdins), mode,
                   len(ex.get("solution", "")))
    if kunci_cache in _CACHE_TESTS:
        return list(_CACHE_TESTS[kunci_cache]), ""

    tests = []
    for i, stdin in enumerate(stdins, start=1):
        hasil = runner.jalankan(bahasa, gabung_setup(ex, ex["solution"]), stdin=stdin)
        if not hasil.sukses:
            return [], (f"Solusi contoh sendiri gagal dijalankan "
                        f"({hasil.fase}): {hasil.galat.strip()[:200]}")
        nama = "Bandingkan output dengan solusi contoh"
        if len(stdins) > 1:
            nama += f" (input #{i})"
        tests.append({"nama": nama, "stdin": stdin, "harapan": hasil.keluaran,
                      "mode": mode})

    _CACHE_TESTS[kunci_cache] = list(tests)
    return tests, ""


