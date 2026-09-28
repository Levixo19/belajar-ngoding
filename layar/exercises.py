"""Latihan coding: tulis kode sendiri, jalankan, dan diperiksa otomatis.

Jawaban benar tidak ditentukan dari kemiripan kode, tapi dari OUTPUT program.
Kalau sebuah latihan tidak menyertakan `tests`, ekspektasi dibuat otomatis
dengan menjalankan solusi contoh -- jadi data soal tidak perlu ditulis dua kali.

Yang membedakan versi ini dari sekadar "benar/salah":

* Kegagalan ditampilkan sebagai DIFF berbaris-nomor dengan penunjuk kolom dan
  tebakan penyebabnya (`beda.py`), bukan dua blok teks yang harus dibandingkan
  sendiri oleh pelajar.
* Pesan error compiler diterjemahkan ke bahasa Indonesia, path sementaranya
  diganti nama berkas pelajar, dan nomor barisnya digeser supaya cocok dengan
  berkas yang benar-benar dia edit (`galat.py`).
* Latihan yang memang tidak bisa dinilai mesin sekarang bisa ditandai selesai
  secara manual, supaya progres bahasa itu tidak mentok selamanya.

Importir: main.py, layar/navigasi.py, tests/test_solutions.py.
Berkas yang ditulis: kode pelajar di ~/belajar-ngoding/kerjaanku/<kategori>/
(override lewat BELAJAR_WORKSPACE).
"""

import os
import re
import shutil
import subprocess

from inti import beda
from inti import berkas
from inti import galat as modul_galat
from inti import runner
from inti import sorot
from inti import tema
from layar.utils import (
    C, paint, clear, press_enter, ask, ask_choice, confirm, header, rule, lebar,
)
from pelajar.progress import (
    record_exercise_viewed, record_exercise_passed, tandai_latihan_manual,
    batalkan_latihan_manual, load_progress, kunci,
)

try:
    from pelajar import konfigurasi
except ImportError:
    konfigurasi = None

# Tangga kesulitan: Mudah < Menengah < Lanjut < Sulit. Dulu "Sedang" dan
# "Menengah" dipakai sebagai dua jenjang berbeda padahal artinya sama, jadi
# kenaikannya tidak terbaca oleh pelajar.
WARNA_TINGKAT = {
    "Mudah": C.GREEN,
    "Menengah": C.YELLOW,
    "Lanjut": C.MAGENTA,
    "Sulit": C.RED,
}

PERAN_TINGKAT = {
    "Mudah": "tingkat_mudah",
    "Menengah": "tingkat_sedang",
    "Lanjut": "tingkat_menengah",
    "Sulit": "tingkat_sulit",
}

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
    if bahasa == "fedora":
        return (f"#!/usr/bin/env bash\n#\n# {judul}\n\n"
                f"set -euo pipefail\n\n# tulis kodemu di sini\n")
    return f"# {judul}\n# tulis kodemu di sini\n"


# ---------------------------------------------------------------- menulis kode

def _cari_editor():
    """Editor pertama yang benar-benar ada di PATH, atau None.

    `$EDITOR` yang isinya hanya spasi dulu membuat `kandidat.split()[0]`
    melempar IndexError dan menjatuhkan aplikasi -- padahal kasusnya cuma
    "variabel lingkungan kosong".
    """
    pilihan_user = konfigurasi.ambil("editor", "") if konfigurasi else ""
    kandidat = (pilihan_user, os.environ.get("EDITOR"), os.environ.get("VISUAL"),
                "nano", "vim", "vi", "micro", "notepad")
    for calon in kandidat:
        bagian = (calon or "").split()
        if bagian and shutil.which(bagian[0]):
            return calon
    return None


def _tulis_inline(awal):
    """Masukan multi-baris tanpa editor eksternal. Diakhiri baris berisi '.'."""
    print(tema.cat("\n  Ketik kodemu. Akhiri dengan baris berisi titik tunggal (.)", "aksen"))
    print(tema.cat("  Ketik '!batal' untuk membatalkan.", "redup"))
    print(rule("-", C.DIM, bold=False))

    baris = []
    while True:
        try:
            b = input()
        except EOFError:
            break
        if b.strip() == ".":
            break
        if b.strip() == "!batal":
            return None
        baris.append(b)
    teks = "\n".join(baris)
    return teks if teks.strip() else awal


def tulis_kode(path, bahasa, ex):
    """Buka editor (atau mode inline) untuk file kerja user. Return isi kode."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(_kerangka(bahasa, ex))

    editor = _cari_editor()
    if editor:
        print(tema.cat(f"\n  Membuka {path}", "redup"))
        print(tema.cat(f"  dengan editor: {editor}", "redup"))
        press_enter("Tekan ENTER untuk mulai mengetik...")
        try:
            subprocess.call(editor.split() + [path])
        except OSError as e:
            print(tema.cat(f"  Editor gagal dibuka ({e}). Pakai mode ketik langsung.",
                           "galat"))
            editor = None

    if not editor:
        awal = ""
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                awal = f.read()
        baru = _tulis_inline(awal)
        if baru is None:
            return None
        with open(path, "w", encoding="utf-8") as f:
            f.write(baru)

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        print(tema.cat(f"  Gagal membaca file: {e}", "galat"))
        return None


# ----------------------------------------------------------------- pemeriksaan

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


def _cetak_galat(teks, ex, bahasa):
    """Tampilkan pesan error: dirapikan, lalu diterjemahkan."""
    if not teks or not teks.strip():
        return
    rapi = modul_galat.rapikan(teks, nama_kerja(ex, bahasa), baris_setup(ex))

    print(tema.cat("     Pesan dari komputer:", "galat"))
    for b in modul_galat.ringkas(rapi, maks_baris=10):
        print(tema.cat("       " + b, "galat"))

    penjelasan = modul_galat.terjemahkan(rapi)
    if penjelasan:
        print(tema.cat("     Artinya:", "peringatan", tema.TEBAL))
        for p in penjelasan:
            print(tema.cat("       - " + p, "peringatan"))


def _tampilkan_hasil_uji(hasil_uji, ex, bahasa):
    lulus_semua = all(h.lulus for h in hasil_uji)
    lbr = lebar()
    print(tema.cat("\n  " + "=" * (lbr - 4), "garis"))

    for h in hasil_uji:
        tanda = (tema.cat("LULUS", "sukses", tema.TEBAL) if h.lulus
                 else tema.cat("GAGAL", "galat", tema.TEBAL))
        print(f"  [{tanda}] {h.nama}")
        if h.lulus:
            continue

        if h.stdin:
            print(tema.cat("     Input   : " + h.stdin.replace("\n", " \\n "), "redup"))

        _cetak_galat(h.galat, ex, bahasa)

        # Kalau programnya gagal dikompilasi, tidak ada output untuk
        # dibandingkan. Menampilkan diff di sini cuma menambah kebisingan --
        # dan diagnosisnya ("sudah pakai perintah cetak?") justru menyesatkan.
        if h.galat.strip() and not runner.normalisasi(h.aktual):
            print(tema.cat("     Perbaiki dulu error di atas, baru jalankan lagi.",
                           "peringatan"))
            continue

        # Output sudah benar tapi program berakhir dengan error: kasus ini dulu
        # dinyatakan LULUS, menyembunyikan bug yang justru sedang dipelajari.
        if h.output_cocok and h.kode_keluar != 0:
            print(tema.cat(
                f"     Outputmu sudah benar, TAPI program berakhir dengan error "
                f"(kode keluar {h.kode_keluar}). Perbaiki dulu errornya.",
                "peringatan", tema.TEBAL))
            continue

        if h.mode in ("regex", "mengandung"):
            print(tema.cat(f"     Pola yang dicari ({h.mode}): {h.harapan[:80]}", "info"))
            print(tema.cat("     Hasilmu :", "peringatan"))
            for b in (runner.normalisasi(h.aktual) or "(kosong)").splitlines()[:12]:
                print(tema.cat("       " + b, "peringatan"))
            continue

        perbandingan = beda.bandingkan(h.harapan, h.aktual)
        for baris in beda.render(perbandingan, lebar=lbr):
            print("  " + baris)

    print(tema.cat("  " + "=" * (lbr - 4), "garis"))
    return lulus_semua


def periksa_jawaban(ex, kategori, bahasa, kode):
    """Jalankan pemeriksaan dan catat kelulusan. Return True kalau lulus."""
    print(tema.cat("\n  Menyiapkan kunci jawaban...", "redup"))
    tests, pesan_galat = bangun_tests(ex, bahasa)

    if pesan_galat:
        print(tema.cat("  " + pesan_galat, "galat"))
        print(tema.cat("  Latihan ini hanya bisa dijalankan, belum bisa dinilai otomatis.",
                       "peringatan"))
        return False
    if not tests:
        print(tema.cat("  Belum ada kunci jawaban untuk latihan ini.", "peringatan"))
        return False

    print(tema.cat("  Menjalankan kodemu...", "redup"))
    semua, hasil_uji, _ = runner.periksa(bahasa, gabung_setup(ex, kode), tests)
    lulus = _tampilkan_hasil_uji(hasil_uji, ex, bahasa) and semua
    ada_diff = any(not h.lulus and runner.normalisasi(h.aktual) for h in hasil_uji)

    if lulus:
        print(tema.cat("\n  BENAR! Outputmu sudah sesuai. Kerja bagus.",
                       "sukses", tema.TEBAL))
        badge = record_exercise_passed(kategori, ex["title"])
        for _, nama, deskripsi in badge:
            print(tema.cat(f"  [BADGE BARU] {nama} - {deskripsi}", "judul", tema.TEBAL))
    else:
        print(tema.cat("\n  Belum sesuai. Perbaiki kodemu lalu coba lagi.",
                       "peringatan", tema.TEBAL))
        if ada_diff:
            print(tema.cat("  Baris bertanda - adalah yang diharapkan, "
                           "+ adalah punyamu.", "redup"))
    return lulus


# -------------------------------------------------------------------- tampilan

def _blok_kode(kode, bahasa, awalan="  "):
    """Baris-baris kode siap cetak, disorot kalau pengaturannya menyala."""
    if konfigurasi is not None and not konfigurasi.ambil("sorot_sintaks", True):
        return [tema.cat(awalan + b, "kode_string") for b in kode.splitlines()]
    return sorot.sorot_baris(kode, bahasa, awalan=awalan)


def _status_latihan(ex, kategori, data):
    k = kunci(kategori, ex["title"])
    if k in data["latihan_lulus"]:
        return "lulus"
    if k in data["latihan_manual"]:
        return "manual"
    if k in data["latihan_dilihat"]:
        return "dibuka"
    return "baru"


def _cetak_petunjuk_berkas(ex, kategori, bahasa):
    """Beri tahu berkas apa yang akan ditulis dan bagaimana menjalankannya.

    Tanpa ini, pelajar tidak tahu apakah harus membuat berkas sendiri, apa
    namanya, dan perintah apa yang dipakai menjalankannya di luar aplikasi.
    Nama berkasnya ditentukan aplikasi (bukan bebas) karena Java mewajibkan
    nama berkas sama dengan nama kelas, dan karena tombol [2] dan [3]
    membaca berkas di jalur itu.
    """
    nama = nama_kerja(ex, bahasa)
    p = berkas.petunjuk_latihan(bahasa, nama)
    folder = os.path.join(DIR_KERJA, kategori)
    rumah = os.path.expanduser("~")
    if folder.startswith(rumah):
        folder = "~" + folder[len(rumah):]

    print(tema.cat("\n  BERKAS JAWABAN:", "info", tema.TEBAL))
    print(tema.cat(f"    Nama berkas : {nama}", "sukses", tema.TEBAL))
    if bahasa == "java":
        print(tema.cat(f"    Nama kelas  : {nama[:-5]}   "
                       "(javac mewajibkan sama dengan nama berkas)", "redup"))
    print(tema.cat(f"    Lokasi      : {folder}", "redup"))
    print(tema.cat("    Tekan [1] untuk membuat & membukanya di editor.", "redup"))

    if p.perintah:
        print(tema.cat("    Di terminal : " + "  lalu  ".join(p.perintah), "aksen"))


def _tampilkan_soal(ex, kategori, bahasa, hint_terbuka):
    clear()
    data = load_progress()
    status = _status_latihan(ex, kategori, data)
    subjudul = {"lulus": "SUDAH LULUS",
                "manual": "DITANDAI SELESAI MANUAL"}.get(status, "")
    header("LATIHAN: " + ex["title"], subjudul)

    diff = ex.get("difficulty", "Menengah")
    print(tema.cat(f"  Tingkat kesulitan: {diff}",
                   PERAN_TINGKAT.get(diff, "teks"), tema.TEBAL))

    boleh, alasan = bisa_dinilai(ex, bahasa)
    if not boleh:
        print(tema.cat(f"  Penilaian otomatis mati: {alasan}", "galat"))
        saran = runner.perintah_instalasi(bahasa)
        if saran and runner.program_hilang(bahasa):
            print(tema.cat(f"  Pasang dengan: {saran}", "info"))

    print(tema.cat("\n  SOAL:", "info", tema.TEBAL))
    for line in ex["question"]:
        print(tema.cat("  " + line, "teks"))

    _cetak_petunjuk_berkas(ex, kategori, bahasa)

    if ex.get("setup", "").strip():
        print(tema.cat("\n  KONDISI AWAL (sudah disiapkan, tak perlu kamu tulis):",
                       "info", tema.TEBAL))
        for line in _blok_kode(ex["setup"].strip(), bahasa, awalan="    "):
            print(line)

    hints = ex.get("hints") or []
    if hint_terbuka > 0:
        print(tema.cat(f"\n  HINT ({min(hint_terbuka, len(hints))}/{len(hints)}):",
                       "info", tema.TEBAL))
        for h in hints[:hint_terbuka]:
            print(tema.cat("  - " + h, "redup"))
    elif hints:
        print(tema.cat(f"\n  Tersedia {len(hints)} hint. Coba sendiri dulu ya.", "redup"))


def _tampilkan_solusi(ex, bahasa):
    clear()
    header("JAWABAN (Contoh Solusi)", ex["title"])
    for line in _blok_kode(ex["solution"], bahasa):
        print(line)
    print(tema.cat("  " + "-" * (lebar() - 4), "redup"))
    print(tema.cat("  Ini cuma SATU cara. Kode yang beda belum tentu salah,", "subjudul"))
    print(tema.cat("  selama outputnya sama.", "subjudul"))
    press_enter()


def _bandingkan_dengan_solusi(ex, bahasa, path):
    """Sandingkan kode pelajar dengan solusi contoh, baris demi baris."""
    if not os.path.exists(path):
        print(tema.cat("  Kamu belum menulis kode.", "galat"))
        press_enter()
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            milikku = f.read()
    except OSError as e:
        print(tema.cat(f"  Gagal membaca file: {e}", "galat"))
        press_enter()
        return

    clear()
    header("BANDINGKAN KODE", ex["title"])
    perbandingan = beda.bandingkan(ex["solution"], milikku)
    if perbandingan.sama:
        print(tema.cat("  Kodemu sama persis dengan solusi contoh.", "sukses"))
    else:
        print(tema.cat("  Baris - dari solusi contoh, + dari kodemu.", "redup"))
        print(tema.cat("  Beda tulisan itu wajar; yang penting outputnya sama.\n", "redup"))
        for baris in beda.render(perbandingan, lebar=lebar(), maks_baris=30):
            print("  " + baris)
    press_enter()


def _jalankan_saja(ex, bahasa, kode):
    stdin = ex.get("stdin", "")
    if ex.get("auto_check") is False:
        print(tema.cat(
            "\n  Catatan: latihan ini memang tidak dinilai otomatis "
            f"({ex.get('alasan_tidak_dicek', '')}).", "peringatan"))
        print(tema.cat("  Error di bawah bisa jadi WAJAR dan bukan berarti "
                       "jawabanmu salah.", "peringatan"))

    print(tema.cat("\n  Menjalankan...", "redup"))
    hasil = runner.jalankan(bahasa, gabung_setup(ex, kode), stdin=stdin)

    lbr = lebar()
    print(tema.cat("\n  " + "-" * (lbr - 4), "redup"))
    if hasil.keluaran.strip():
        print(tema.cat("  OUTPUT:", "info", tema.TEBAL))
        for b in hasil.keluaran.splitlines():
            print("  " + b)
    else:
        print(tema.cat("  (Program tidak menghasilkan output)", "redup"))

    if hasil.galat.strip():
        judul = "ERROR KOMPILASI:" if hasil.fase == "kompilasi" else "PESAN ERROR:"
        print(tema.cat("\n  " + judul, "galat", tema.TEBAL))
        rapi = modul_galat.rapikan(hasil.galat, nama_kerja(ex, bahasa), baris_setup(ex))
        for b in modul_galat.ringkas(rapi, maks_baris=15):
            print(tema.cat("  " + b, "galat"))
        penjelasan = modul_galat.terjemahkan(rapi)
        if penjelasan:
            print(tema.cat("\n  Artinya:", "peringatan", tema.TEBAL))
            for p in penjelasan:
                print(tema.cat("   - " + p, "peringatan"))

    if hasil.catatan:
        print(tema.cat("\n  Catatan: " + hasil.catatan, "redup"))
    print(tema.cat("  " + "-" * (lbr - 4), "redup"))
    akhiran = "  (0 = normal)" if hasil.kode_keluar == 0 else "  (bukan 0 = error)"
    print(tema.cat(f"  Kode keluar: {hasil.kode_keluar}{akhiran}", "redup"))
    press_enter()


def show_exercise(ex, kategori="latihan", bahasa="python"):
    record_exercise_viewed(kategori, ex["title"])
    hint_terbuka = 0
    path = _path_kerja(kategori, ex, bahasa, buat_folder=False)
    bisa_jalan = runner.tersedia(bahasa)
    boleh_dinilai = bisa_dinilai(ex, bahasa)[0]

    while True:
        _tampilkan_soal(ex, kategori, bahasa, hint_terbuka)
        hints = ex.get("hints") or []
        status = _status_latihan(ex, kategori, load_progress())

        print()
        if bisa_jalan:
            print(tema.cat("  [1] Tulis / ubah kodeku", "aksen"))
            print(tema.cat("  [2] Jalankan kodeku", "aksen"))
            if boleh_dinilai:
                print(tema.cat("  [3] Periksa jawaban (otomatis)", "sukses", tema.TEBAL))
        else:
            print(tema.cat("  [1] Tulis kodeku (runner nonaktif, hanya disimpan)", "redup"))
        if hint_terbuka < len(hints):
            print(tema.cat(f"  [h] Buka hint berikutnya ({hint_terbuka + 1}/{len(hints)})",
                           "peringatan"))
        print(tema.cat("  [j] Tampilkan jawaban", "subjudul"))
        print(tema.cat("  [d] Bandingkan kodeku dengan jawaban", "subjudul"))
        if not boleh_dinilai:
            if status == "manual":
                print(tema.cat("  [m] Batalkan tanda 'sudah selesai'", "redup"))
            else:
                print(tema.cat("  [m] Saya sudah menyelesaikannya, tandai selesai",
                               "sukses"))
        print(tema.cat("  [0] Kembali ke daftar", "redup"))

        pilih = ask("  Pilih > ", "0").lower()

        if pilih == "0":
            return
        if pilih == "h":
            hint_terbuka = min(hint_terbuka + 1, len(hints))
            continue
        if pilih == "j":
            perlu_konfirmasi = konfigurasi is None or konfigurasi.ambil(
                "konfirmasi_jawaban", True)
            if (perlu_konfirmasi and hint_terbuka < len(hints) and not confirm(
                    "Masih ada hint yang belum dibuka. Yakin mau langsung lihat jawaban?")):
                continue
            _tampilkan_solusi(ex, bahasa)
            continue
        if pilih == "d":
            _bandingkan_dengan_solusi(ex, bahasa, path)
            continue
        if pilih == "m" and not boleh_dinilai:
            if status == "manual":
                batalkan_latihan_manual(kategori, ex["title"])
                print(tema.cat("  Tanda selesai dibatalkan.", "redup"))
            else:
                badge = tandai_latihan_manual(kategori, ex["title"])
                print(tema.cat("  Ditandai selesai. Ingat: ini penilaian jujur "
                               "dari kamu sendiri.", "sukses"))
                for _, nama, deskripsi in badge:
                    print(tema.cat(f"  [BADGE BARU] {nama} - {deskripsi}",
                                   "judul", tema.TEBAL))
            press_enter()
            continue
        if pilih == "1":
            path = _path_kerja(kategori, ex, bahasa)
            kode = tulis_kode(path, bahasa, ex)
            if kode is None:
                continue
            print(tema.cat(f"\n  Tersimpan di: {path}", "sukses"))
            if boleh_dinilai and confirm("Langsung periksa jawaban sekarang?", default=True):
                periksa_jawaban(ex, kategori, bahasa, kode)
                press_enter()
            elif bisa_jalan and confirm("Jalankan kodenya sekarang?", default=True):
                _jalankan_saja(ex, bahasa, kode)
            continue
        if pilih == "3" and not boleh_dinilai:
            print(tema.cat("  Latihan ini tidak bisa dinilai otomatis.", "galat"))
            press_enter()
            continue
        if pilih in ("2", "3") and bisa_jalan:
            if not os.path.exists(path):
                print(tema.cat("  Kamu belum menulis kode. Pilih [1] dulu.", "galat"))
                press_enter()
                continue
            with open(path, "r", encoding="utf-8") as f:
                kode = f.read()
            if pilih == "2":
                _jalankan_saja(ex, bahasa, kode)
            else:
                periksa_jawaban(ex, kategori, bahasa, kode)
                press_enter()
            continue

        print(tema.cat("  Pilihan tidak valid.", "galat"))
        press_enter()


def _label(ex, kategori, data):
    status = _status_latihan(ex, kategori, data)
    tanda = {
        "lulus": tema.cat("[LULUS  ]", "sukses", tema.TEBAL),
        "manual": tema.cat("[selesai]", "sukses"),
        "dibuka": tema.cat("[dibuka ]", "peringatan"),
        "baru": tema.cat("[       ]", "redup"),
    }[status]
    diff = ex.get("difficulty", "-")
    return (f"{tanda} {ex['title']}  "
            + tema.cat(f"({diff})", PERAN_TINGKAT.get(diff, "teks")))


def exercise_menu(title, exercises, kategori="latihan", bahasa="python"):
    while True:
        clear()
        header("LATIHAN: " + title)

        data = load_progress()
        selesai = sum(1 for e in exercises
                      if _status_latihan(e, kategori, data) in ("lulus", "manual"))
        print(tema.cat(f"  Selesai {selesai}/{len(exercises)} latihan", "teks"))
        if runner.tersedia(bahasa):
            print(tema.cat("  Kode kamu dijalankan & dinilai otomatis dari output-nya.",
                           "sukses"))
        else:
            hilang = ", ".join(runner.program_hilang(bahasa))
            print(tema.cat(f"  Penilaian otomatis mati: {hilang} belum terpasang.", "galat"))
            saran = runner.perintah_instalasi(bahasa)
            if saran:
                print(tema.cat(f"  Pasang dengan: {saran}", "info"))
            print(tema.cat("  Latihan tetap bisa dikerjakan dan ditandai selesai manual.",
                           "redup"))
        print(tema.cat(f"  Folder kerja: {os.path.join(DIR_KERJA, kategori)}", "redup"))
        print(rule("-", C.DIM, bold=False))

        names = [_label(e, kategori, data) for e in exercises]
        pilih = ask_choice(paint("  Pilih latihan:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        show_exercise(exercises[pilih - 1], kategori, bahasa)
