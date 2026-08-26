#!/usr/bin/env python3
"""Aplikasi belajar pemrograman berbasis terminal.

Jalankan: python3 main.py
"""

import sys

import runner
from utils import C, paint, clear, ask_choice, ask, press_enter, header, rule, bar, WIDTH
from materials import materials_menu
from quiz import quiz_menu
from exercises import exercise_menu
from navigasi import cari_global, menu_bookmark, lanjut_terakhir
from progress import (
    load_progress, statistik_bahasa, info_level, gelar_dari_level, DAFTAR_BADGE,
)
from data import (
    JAVA_MATERIALS, JAVA_QUIZZES, JAVA_EXERCISES,
    SQL_MATERIALS, SQL_QUIZZES, SQL_EXERCISES,
    PYTHON_MATERIALS, PYTHON_QUIZZES, PYTHON_EXERCISES,
    JAVASCRIPT_MATERIALS, JAVASCRIPT_QUIZZES, JAVASCRIPT_EXERCISES,
    C_MATERIALS, C_QUIZZES, C_EXERCISES,
    CPP_MATERIALS, CPP_QUIZZES, CPP_EXERCISES,
    BASH_MATERIALS, BASH_QUIZZES, BASH_EXERCISES,
    GO_MATERIALS, GO_QUIZZES, GO_EXERCISES,
)

# Registry semua bahasa. Menambah bahasa baru = tambah satu entri di sini
# plus tiga file di folder data/.
#   key     : prefix kategori progres, harus stabil (jangan diubah setelah rilis)
#   runner  : kunci toolchain di runner.TOOLCHAINS untuk eksekusi kode
LANGUAGES = [
    {
        "key": "java", "label": "Java", "runner": "java",
        "materials": JAVA_MATERIALS, "quizzes": JAVA_QUIZZES, "exercises": JAVA_EXERCISES,
        "run_info": ["Kompilasi : javac NamaFile.java", "Jalankan  : java NamaFile"],
    },
    {
        "key": "sql", "label": "SQL", "runner": "sql",
        "materials": SQL_MATERIALS, "quizzes": SQL_QUIZZES, "exercises": SQL_EXERCISES,
        "run_info": ["Latihan dijalankan dengan SQLite: sqlite3 :memory: < file.sql",
                     "Di MySQL/MariaDB: mysql -u root -p"],
    },
    {
        "key": "python", "label": "Python", "runner": "python",
        "materials": PYTHON_MATERIALS, "quizzes": PYTHON_QUIZZES, "exercises": PYTHON_EXERCISES,
        "run_info": ["Jalankan : python3 nama_file.py"],
    },
    {
        "key": "javascript", "label": "JavaScript", "runner": "javascript",
        "materials": JAVASCRIPT_MATERIALS, "quizzes": JAVASCRIPT_QUIZZES,
        "exercises": JAVASCRIPT_EXERCISES,
        "run_info": ["Jalankan di Node.js : node nama_file.js",
                     "Atau tempel di console browser (F12 > Console)."],
    },
    {
        "key": "c", "label": "C", "runner": "c",
        "materials": C_MATERIALS, "quizzes": C_QUIZZES, "exercises": C_EXERCISES,
        "run_info": ["Kompilasi : gcc nama_file.c -o program", "Jalankan  : ./program"],
    },
    {
        "key": "cpp", "label": "C++", "runner": "cpp",
        "materials": CPP_MATERIALS, "quizzes": CPP_QUIZZES, "exercises": CPP_EXERCISES,
        "run_info": ["Kompilasi : g++ nama_file.cpp -o program", "Jalankan  : ./program"],
    },
    {
        "key": "bash", "label": "Bash", "runner": "bash",
        "materials": BASH_MATERIALS, "quizzes": BASH_QUIZZES, "exercises": BASH_EXERCISES,
        "run_info": ["Jalankan : bash nama_file.sh", "Atau: chmod +x nama_file.sh && ./nama_file.sh"],
    },
    {
        "key": "go", "label": "Go", "runner": "go",
        "materials": GO_MATERIALS, "quizzes": GO_QUIZZES, "exercises": GO_EXERCISES,
        "run_info": ["Jalankan : go run nama_file.go", "Build    : go build nama_file.go"],
    },
]


def _stat(lang, data):
    return statistik_bahasa(
        data, lang["key"], len(lang["materials"]), len(lang["quizzes"]), len(lang["exercises"])
    )


def baris_dashboard(data):
    """Blok ringkasan XP, level, dan streak di atas menu utama."""
    xp = data.get("xp", 0)
    level, di_level, butuh = info_level(xp)
    streak = data.get("streak", {})
    beruntun = streak.get("beruntun", 0)
    badge = len(data.get("badge", []))

    lines = [
        paint(f"  Level {level} - {gelar_dari_level(level)}", C.YELLOW, C.BOLD)
        + paint(f"   {xp} XP", C.WHITE),
        "  " + bar(di_level, butuh, 28) + paint(f"  {di_level}/{butuh} ke level {level + 1}", C.DIM),
        paint(f"  Streak {beruntun} hari", C.MAGENTA, C.BOLD)
        + paint(f"   (terpanjang {streak.get('terpanjang', 0)}, total {streak.get('total_hari', 0)} hari)", C.DIM)
        + paint(f"   Badge {badge}/{len(DAFTAR_BADGE)}", C.CYAN),
    ]
    return lines


def baris_progres(languages, data):
    lines = [paint("  Progres per bahasa:", C.YELLOW, C.BOLD)]
    total_skor = total_maks = 0
    for lang in languages:
        s = _stat(lang, data)
        total_skor += s["skor"]
        total_maks += s["skor_maks"]
        lines.append(
            paint(f"   {lang['label']:<11}", C.WHITE)
            + bar(s["persen"], 100, 12)
            + paint(f" {s['persen']:>3.0f}%", C.WHITE)
            + paint(f"  materi {s['materi']}/{s['total_materi']}", C.DIM)
            + paint(f"  kuis {s['kuis']}/{s['total_kuis']}", C.DIM)
            + paint(f"  latihan {s['latihan_lulus']}/{s['total_latihan']}", C.DIM)
        )
    if total_maks:
        pct = total_skor / total_maks * 100
        lines.append(paint(
            f"   Skor kuis terbaik keseluruhan: {total_skor}/{total_maks} ({pct:.0f}%)",
            C.GREEN, C.BOLD,
        ))
    return lines


def language_menu(lang):
    while True:
        clear()
        data = load_progress()
        s = _stat(lang, data)
        header("BAHASA: " + lang["label"], f"{s['persen']:.0f}% selesai")

        print("  " + bar(s["persen"], 100, 30) + paint(f"  {s['persen']:.0f}%", C.WHITE, C.BOLD))
        if not runner.tersedia(lang["runner"]):
            hilang = ", ".join(runner.program_hilang(lang["runner"]))
            print(paint(f"  Runner nonaktif: {hilang} belum terpasang.", C.RED))
        print(rule("-", C.DIM, bold=False))

        pilih = ask_choice(
            paint("  Pilih menu:", C.BLUE, C.BOLD),
            [
                f"Materi        ({s['materi']}/{s['total_materi']} dibaca)",
                f"Kuis          ({s['kuis']}/{s['total_kuis']} dikerjakan)",
                f"Latihan Kode  ({s['latihan_lulus']}/{s['total_latihan']} lulus)",
                "Cara menjalankan kode " + lang["label"],
            ],
        )
        if pilih == 0:
            return
        if pilih == 1:
            materials_menu(lang["label"], lang["materials"], f"{lang['key']}_materi")
        elif pilih == 2:
            quiz_menu(lang["label"], lang["quizzes"], f"{lang['key']}_kuis")
        elif pilih == 3:
            exercise_menu(lang["label"], lang["exercises"], f"{lang['key']}_latihan",
                          lang["runner"])
        elif pilih == 4:
            _cara_jalan(lang)


def _cara_jalan(lang):
    clear()
    header("CARA MENJALANKAN KODE " + lang["label"].upper())
    for info in lang["run_info"]:
        print(paint("   " + info, C.WHITE))
    print()
    tc = runner.TOOLCHAINS.get(lang["runner"])
    if runner.tersedia(lang["runner"]):
        print(paint("  Status: toolchain terpasang, kode bisa dijalankan dari aplikasi ini.",
                    C.GREEN))
    else:
        hilang = ", ".join(runner.program_hilang(lang["runner"]))
        print(paint(f"  Status: {hilang} belum terpasang.", C.RED))
        print(paint("  Materi & kuis tetap bisa dipakai, hanya penilaian otomatis yang mati.",
                    C.DIM))
    if tc and tc.catatan:
        print(paint("\n  Catatan: " + tc.catatan, C.YELLOW))
    press_enter()


def menu_badge():
    clear()
    data = load_progress()
    dimiliki = set(data.get("badge", []))
    header("BADGE", f"{len(dimiliki)} dari {len(DAFTAR_BADGE)} terbuka")

    for bid, nama, deskripsi, _ in DAFTAR_BADGE:
        if bid in dimiliki:
            print(paint(f"  [v] {nama:<22}", C.GREEN, C.BOLD) + paint(deskripsi, C.WHITE))
        else:
            print(paint(f"  [ ] {nama:<22}", C.DIM) + paint(deskripsi, C.DIM))
    press_enter()


def menu_statistik():
    clear()
    data = load_progress()
    header("STATISTIK BELAJAR")
    for line in baris_dashboard(data):
        print(line)
    print(rule("-", C.DIM, bold=False))
    for line in baris_progres(LANGUAGES, data):
        print(line)
    print(rule("-", C.DIM, bold=False))

    print(paint("  Ketersediaan runner:", C.YELLOW, C.BOLD))
    for lang in LANGUAGES:
        ada = runner.tersedia(lang["runner"])
        status = paint("terpasang", C.GREEN) if ada else paint(
            "belum ada: " + ", ".join(runner.program_hilang(lang["runner"])), C.RED)
        print(paint(f"   {lang['label']:<11}", C.WHITE) + status)
    press_enter()


def about():
    clear()
    header("TENTANG APLIKASI INI")
    print(paint("  Aplikasi belajar pemrograman dari nol lewat terminal.", C.WHITE))
    print(paint(f"  {len(LANGUAGES)} bahasa: " + ", ".join(l["label"] for l in LANGUAGES), C.WHITE))
    print()
    print(paint("  Fitur:", C.YELLOW, C.BOLD))
    for f in [
        "Materi bertahap dengan contoh kode",
        "Kuis dengan soal & opsi diacak, mode timer, dan review jawaban salah",
        "Latihan coding yang DIJALANKAN dan dinilai otomatis dari output-nya",
        "Kuis dijadwalkan ulang otomatis supaya tidak cepat lupa",
        "Pencarian lintas bahasa, bookmark, dan lanjut dari terakhir",
        "XP, level, streak harian, dan badge",
    ]:
        print(paint("   - " + f, C.WHITE))
    print()
    print(paint("  Alur belajar yang disarankan:", C.GREEN, C.BOLD))
    for i, langkah in enumerate([
        "Baca materi berurutan",
        "Ketik ulang contoh kodenya, jangan copy-paste",
        "Kerjakan latihan sampai statusnya LULUS",
        "Uji pemahaman lewat kuis",
        "Ulangi kuis saat ditandai 'saatnya diulang'",
    ], start=1):
        print(paint(f"   {i}. {langkah}", C.WHITE))
    press_enter()


def main_menu():
    while True:
        clear()
        data = load_progress()
        header("APLIKASI BELAJAR PEMROGRAMAN",
               " | ".join(l["label"] for l in LANGUAGES))
        for line in baris_dashboard(data):
            print(line)
        print(rule("-", C.DIM, bold=False))
        for line in baris_progres(LANGUAGES, data):
            print(line)
        print(rule())

        options = [lang["label"] for lang in LANGUAGES]
        pilih = ask_choice(
            paint("  Pilih bahasa yang mau dipelajari:", C.BLUE, C.BOLD),
            options,
            allow_back=False,
            extra={
                "l": "Lanjutkan dari terakhir",
                "c": "Cari di semua bahasa",
                "b": "Bookmark",
                "s": "Statistik & badge",
                "t": "Tentang aplikasi",
                "k": "Keluar",
            },
        )

        if pilih == "k":
            print(paint("\n  Terima kasih sudah belajar. Semangat terus!\n", C.GREEN, C.BOLD))
            return
        if pilih == "l":
            lanjut_terakhir(LANGUAGES)
        elif pilih == "c":
            cari_global(LANGUAGES)
        elif pilih == "b":
            menu_bookmark(LANGUAGES)
        elif pilih == "s":
            _menu_statistik()
        elif pilih == "t":
            about()
        elif isinstance(pilih, int) and 1 <= pilih <= len(LANGUAGES):
            language_menu(LANGUAGES[pilih - 1])


def _menu_statistik():
    while True:
        clear()
        header("STATISTIK & PENCAPAIAN")
        pilih = ask_choice(paint("  Pilih:", C.BLUE, C.BOLD),
                           ["Statistik lengkap", "Daftar badge"])
        if pilih == 0:
            return
        if pilih == 1:
            menu_statistik()
        else:
            menu_badge()


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(paint("\n\n  Sampai jumpa! Tetap semangat belajar ya.\n", C.GREEN, C.BOLD))
        sys.exit(0)
