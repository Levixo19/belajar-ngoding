"""Latihan coding: tulis kode sendiri, jalankan, dan diperiksa otomatis.

Jawaban benar tidak ditentukan dari kemiripan kode, tapi dari OUTPUT program.
Kalau sebuah latihan tidak menyertakan `tests`, ekspektasi dibuat otomatis
dengan menjalankan solusi contoh -- jadi data soal tidak perlu ditulis dua kali.
"""

import os
import re
import shutil
import subprocess

import runner
from utils import (
    C, paint, clear, press_enter, ask, ask_choice, confirm, header, rule, WIDTH,
)
from progress import (
    record_exercise_viewed, record_exercise_passed, load_progress, kunci,
)

WARNA_TINGKAT = {
    "Mudah": C.GREEN,
    "Sedang": C.YELLOW,
    "Menengah": C.MAGENTA,
    "Sulit": C.RED,
}

DIR_KERJA = os.environ.get(
    "BELAJAR_WORKSPACE",
    os.path.join(os.path.expanduser("~"), "belajar-ngoding", "kerjaanku"),
)


def _slug(teks):
    teks = re.sub(r"[^\w\s-]", "", teks).strip().lower()
    return re.sub(r"[\s_-]+", "-", teks) or "latihan"


def _path_kerja(kategori, ex, bahasa):
    tc = runner.TOOLCHAINS.get(bahasa)
    ext = tc.ekstensi if tc else ".txt"
    folder = os.path.join(DIR_KERJA, kategori)
    os.makedirs(folder, exist_ok=True)

    nama = _slug(ex["title"])
    if bahasa == "java":
        # javac menuntut nama file = nama public class.
        nama = "Latihan" + re.sub(r"\D", "", ex["title"]) or "Latihan"
    return os.path.join(folder, nama + ext)


def _kerangka(bahasa, ex):
    """Template awal supaya user tidak mulai dari halaman kosong."""
    judul = ex["title"]
    if bahasa == "java":
        kelas = os.path.basename(_path_kerja("x", ex, "java"))[:-5]
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
    return f"# {judul}\n# tulis kodemu di sini\n"


# ------------------------------------------------------------------ menulis kode

def _cari_editor():
    for kandidat in (os.environ.get("EDITOR"), os.environ.get("VISUAL"),
                     "nano", "vim", "vi", "micro", "notepad"):
        if kandidat and shutil.which(kandidat.split()[0]):
            return kandidat
    return None


def _tulis_inline(awal):
    """Masukan multi-baris tanpa editor eksternal. Diakhiri baris berisi '.'."""
    print(paint("\n  Ketik kodemu. Akhiri dengan baris berisi titik tunggal (.)", C.CYAN))
    print(paint("  Ketik '!batal' untuk membatalkan.", C.DIM))
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
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(_kerangka(bahasa, ex))

    editor = _cari_editor()
    if editor:
        print(paint(f"\n  Membuka {path}", C.DIM))
        print(paint(f"  dengan editor: {editor}", C.DIM))
        press_enter("Tekan ENTER untuk mulai mengetik...")
        try:
            subprocess.call(editor.split() + [path])
        except OSError as e:
            print(paint(f"  Editor gagal dibuka ({e}). Pakai mode ketik langsung.", C.RED))
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
        print(paint(f"  Gagal membaca file: {e}", C.RED))
        return None


# ------------------------------------------------------------------ pemeriksaan

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
    tests = []

    for i, stdin in enumerate(stdins, start=1):
        hasil = runner.jalankan(bahasa, gabung_setup(ex, ex["solution"]), stdin=stdin)
        if not hasil.sukses:
            return [], (f"Solusi contoh sendiri gagal dijalankan "
                        f"({hasil.fase}): {hasil.galat.strip()[:200]}")
        nama = "Bandingkan output dengan solusi contoh"
        if len(stdins) > 1:
            nama += f" (input #{i})"
        tests.append({"nama": nama, "stdin": stdin, "harapan": hasil.keluaran, "mode": mode})

    return tests, ""


def _tampilkan_hasil_uji(hasil_uji):
    lulus_semua = all(h.lulus for h in hasil_uji)
    print(paint("\n  " + "=" * (WIDTH - 4), C.CYAN))
    for h in hasil_uji:
        tanda = paint("LULUS", C.GREEN, C.BOLD) if h.lulus else paint("GAGAL", C.RED, C.BOLD)
        print(f"  [{tanda}] {h.nama}")
        if h.lulus:
            continue
        if h.galat.strip():
            print(paint("     Pesan error:", C.RED))
            for b in h.galat.strip().splitlines()[:12]:
                print(paint("       " + b, C.RED))
        if h.stdin:
            print(paint("     Input   : " + h.stdin.replace("\n", " \\n "), C.DIM))
        print(paint("     Harapan :", C.GREEN))
        for b in (runner.normalisasi(h.harapan) or "(kosong)").splitlines()[:12]:
            print(paint("       " + b, C.GREEN))
        print(paint("     Hasilmu :", C.YELLOW))
        for b in (runner.normalisasi(h.aktual) or "(kosong)").splitlines()[:12]:
            print(paint("       " + b, C.YELLOW))
    print(paint("  " + "=" * (WIDTH - 4), C.CYAN))
    return lulus_semua


def periksa_jawaban(ex, kategori, bahasa, kode):
    """Jalankan pemeriksaan dan catat kelulusan. Return True kalau lulus."""
    print(paint("\n  Menyiapkan kunci jawaban...", C.DIM))
    tests, galat = bangun_tests(ex, bahasa)

    if galat:
        print(paint("  " + galat, C.RED))
        print(paint("  Latihan ini hanya bisa dijalankan, belum bisa dinilai otomatis.", C.YELLOW))
        return False
    if not tests:
        print(paint("  Belum ada kunci jawaban untuk latihan ini.", C.YELLOW))
        return False

    print(paint("  Menjalankan kodemu...", C.DIM))
    semua, hasil_uji, _ = runner.periksa(bahasa, gabung_setup(ex, kode), tests)
    lulus = _tampilkan_hasil_uji(hasil_uji) and semua

    if lulus:
        print(paint("\n  BENAR! Outputmu sudah sesuai. Kerja bagus.", C.GREEN, C.BOLD))
        badge = record_exercise_passed(kategori, ex["title"])
        for _, nama, deskripsi in badge:
            print(paint(f"  [BADGE BARU] {nama} - {deskripsi}", C.YELLOW, C.BOLD))
    else:
        print(paint("\n  Belum sesuai. Perbaiki kodemu lalu coba lagi.", C.YELLOW, C.BOLD))
        print(paint("  Perhatikan tanda baca, huruf besar/kecil, dan spasi.", C.DIM))
    return lulus


# ------------------------------------------------------------------- tampilan

def _tampilkan_soal(ex, kategori, bahasa, hint_terbuka):
    clear()
    lulus = kunci(kategori, ex["title"]) in load_progress()["latihan_lulus"]
    header("LATIHAN: " + ex["title"], "SUDAH LULUS" if lulus else "")

    diff = ex.get("difficulty", "Sedang")
    print(paint(f"  Tingkat kesulitan: {diff}", WARNA_TINGKAT.get(diff, C.WHITE), C.BOLD))

    boleh, alasan = bisa_dinilai(ex, bahasa)
    if not boleh:
        print(paint(f"  Penilaian otomatis mati: {alasan}", C.RED))

    print(paint("\n  SOAL:", C.BLUE, C.BOLD))
    for line in ex["question"]:
        print(paint("  " + line, C.WHITE))

    if ex.get("setup", "").strip():
        print(paint("\n  KONDISI AWAL (sudah disiapkan, tak perlu kamu tulis):",
                    C.BLUE, C.BOLD))
        for line in ex["setup"].strip().splitlines():
            print(paint("  " + line, C.DIM))

    hints = ex.get("hints") or []
    if hint_terbuka > 0:
        print(paint(f"\n  HINT ({min(hint_terbuka, len(hints))}/{len(hints)}):", C.BLUE, C.BOLD))
        for h in hints[:hint_terbuka]:
            print(paint("  - " + h, C.DIM))
    elif hints:
        print(paint(f"\n  Tersedia {len(hints)} hint. Coba sendiri dulu ya.", C.DIM))


def _tampilkan_solusi(ex):
    clear()
    header("JAWABAN (Contoh Solusi)", ex["title"])
    for line in ex["solution"].splitlines():
        print(paint("  " + line, C.GREEN))
    print(paint("  " + "-" * (WIDTH - 4), C.DIM))
    print(paint("  Ini cuma SATU cara. Kode yang beda belum tentu salah,", C.MAGENTA))
    print(paint("  selama outputnya sama.", C.MAGENTA))
    press_enter()


def _jalankan_saja(ex, bahasa, kode):
    stdin = ex.get("stdin", "")
    print(paint("\n  Menjalankan...", C.DIM))
    hasil = runner.jalankan(bahasa, gabung_setup(ex, kode), stdin=stdin)

    print(paint("\n  " + "-" * (WIDTH - 4), C.DIM))
    if hasil.keluaran.strip():
        print(paint("  OUTPUT:", C.BLUE, C.BOLD))
        for b in hasil.keluaran.splitlines():
            print("  " + b)
    else:
        print(paint("  (Program tidak menghasilkan output)", C.DIM))

    if hasil.galat.strip():
        judul = "ERROR KOMPILASI:" if hasil.fase == "kompilasi" else "PESAN ERROR:"
        print(paint("\n  " + judul, C.RED, C.BOLD))
        for b in hasil.galat.splitlines()[:20]:
            print(paint("  " + b, C.RED))

    if hasil.catatan:
        print(paint("\n  Catatan: " + hasil.catatan, C.DIM))
    print(paint("  " + "-" * (WIDTH - 4), C.DIM))
    print(paint(f"  Kode keluar: {hasil.kode_keluar}", C.DIM))
    press_enter()


def show_exercise(ex, kategori="latihan", bahasa="python"):
    record_exercise_viewed(kategori, ex["title"])
    hint_terbuka = 0
    path = _path_kerja(kategori, ex, bahasa)
    bisa_jalan = runner.tersedia(bahasa)
    boleh_dinilai = bisa_dinilai(ex, bahasa)[0]

    while True:
        _tampilkan_soal(ex, kategori, bahasa, hint_terbuka)
        hints = ex.get("hints") or []

        print()
        if bisa_jalan:
            print(paint("  [1] Tulis / ubah kodeku", C.CYAN))
            print(paint("  [2] Jalankan kodeku", C.CYAN))
            if boleh_dinilai:
                print(paint("  [3] Periksa jawaban (otomatis)", C.GREEN, C.BOLD))
        else:
            print(paint("  [1] Tulis kodeku (runner nonaktif, hanya disimpan)", C.DIM))
        if hint_terbuka < len(hints):
            print(paint(f"  [h] Buka hint berikutnya ({hint_terbuka + 1}/{len(hints)})", C.YELLOW))
        print(paint("  [j] Tampilkan jawaban", C.MAGENTA))
        print(paint("  [0] Kembali ke daftar", C.DIM))

        pilih = ask("  Pilih > ", "0").lower()

        if pilih == "0":
            return
        if pilih == "h":
            hint_terbuka = min(hint_terbuka + 1, len(hints))
            continue
        if pilih == "j":
            if hint_terbuka < len(hints) and not confirm(
                "Masih ada hint yang belum dibuka. Yakin mau langsung lihat jawaban?"
            ):
                continue
            _tampilkan_solusi(ex)
            continue
        if pilih == "1":
            kode = tulis_kode(path, bahasa, ex)
            if kode is None:
                continue
            print(paint(f"\n  Tersimpan di: {path}", C.GREEN))
            if boleh_dinilai and confirm("Langsung periksa jawaban sekarang?", default=True):
                periksa_jawaban(ex, kategori, bahasa, kode)
                press_enter()
            elif bisa_jalan and confirm("Jalankan kodenya sekarang?", default=True):
                _jalankan_saja(ex, bahasa, kode)
            continue
        if pilih == "3" and not boleh_dinilai:
            print(paint("  Latihan ini tidak bisa dinilai otomatis.", C.RED))
            press_enter()
            continue
        if pilih in ("2", "3") and bisa_jalan:
            if not os.path.exists(path):
                print(paint("  Kamu belum menulis kode. Pilih [1] dulu.", C.RED))
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

        print(paint("  Pilihan tidak valid.", C.RED))
        press_enter()


def _label(ex, kategori, data):
    k = kunci(kategori, ex["title"])
    if k in data["latihan_lulus"]:
        tanda = paint("[LULUS]", C.GREEN, C.BOLD)
    elif k in data["latihan_dilihat"]:
        tanda = paint("[dibuka]", C.YELLOW)
    else:
        tanda = paint("[      ]", C.DIM)
    warna = WARNA_TINGKAT.get(ex.get("difficulty", ""), C.WHITE)
    return f"{tanda} {ex['title']}  {paint('(' + ex.get('difficulty', '-') + ')', warna)}"


def exercise_menu(title, exercises, kategori="latihan", bahasa="python"):
    while True:
        clear()
        header("LATIHAN: " + title)

        data = load_progress()
        lulus = sum(1 for e in exercises if kunci(kategori, e["title"]) in data["latihan_lulus"])
        print(paint(f"  Lulus {lulus}/{len(exercises)} latihan", C.WHITE))
        if runner.tersedia(bahasa):
            print(paint("  Kode kamu dijalankan & dinilai otomatis dari output-nya.", C.GREEN))
        else:
            hilang = ", ".join(runner.program_hilang(bahasa))
            print(paint(f"  Penilaian otomatis mati: {hilang} belum terpasang.", C.RED))
        print(paint(f"  Folder kerja: {os.path.join(DIR_KERJA, kategori)}", C.DIM))
        print(rule("-", C.DIM, bold=False))

        names = [_label(e, kategori, data) for e in exercises]
        pilih = ask_choice(paint("  Pilih latihan:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        show_exercise(exercises[pilih - 1], kategori, bahasa)
