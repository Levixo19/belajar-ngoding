#!/usr/bin/env python3
"""Aplikasi belajar pemrograman berbasis terminal.

Jalankan:  python3 main.py
Bantuan :  python3 main.py --bantuan

Berkas ini menyimpan dua hal: REGISTRY bahasa (satu-satunya tempat yang perlu
disentuh saat menambah bahasa baru) dan seluruh layar tingkat atas -- dashboard,
statistik, pengaturan, dan pengelolaan data.

Importir: tests/test_data.py dan tests/test_solutions.py memakai LANGUAGES.
Berkas yang disentuh: progres (progress.py) dan konfigurasi (konfigurasi.py).
"""

import argparse
import os
import sys
from datetime import date

import bab
import konfigurasi
import runner
import tema
import utils
from utils import (
    C, paint, clear, ask, ask_choice, confirm, press_enter, header, rule, bar,
    lebar, kotak,
)
from materials import materials_menu, render_material
from quiz import quiz_menu, menu_satu_kuis
from exercises import exercise_menu, show_exercise
from navigasi import cari_global, menu_bookmark, lanjut_terakhir
from saran import langkah_berikutnya, tantangan_harian
from progress import (
    load_progress, statistik_bahasa, info_level, gelar_dari_level, DAFTAR_BADGE,
    streak_aktif, xp_hari_ini, riwayat_harian, ekspor, impor, reset, cadangkan,
    judul_kunci, PROGRESS_FILE,
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
    APLIKASI_MATERIALS, APLIKASI_QUIZZES, APLIKASI_EXERCISES,
    HTML_MATERIALS, HTML_QUIZZES, HTML_EXERCISES,
    CSS_MATERIALS, CSS_QUIZZES, CSS_EXERCISES,
)

VERSI = "2.0"

# Registry semua bahasa. Menambah bahasa baru = tambah satu entri di sini
# plus tiga file di folder data/.
#   key     : prefix kategori progres, harus stabil (jangan diubah setelah rilis)
#   runner  : kunci toolchain di runner.TOOLCHAINS untuk eksekusi kode
LANGUAGES = [
    # HTML dan CSS berdiri paling depan, dan urutan itu disengaja. Keduanya
    # satu-satunya bahasa di daftar ini yang TIDAK membutuhkan satu program pun
    # untuk dipasang — cukup aplikasi ini dan sebuah browser. Buat orang yang
    # baru mulai dan belum sanggup memasang compiler apa pun, di sinilah pintu
    # masuk yang paling mungkin dilewati tanpa tersandung lebih dulu.
    {
        "key": "html", "label": "HTML", "runner": "html",
        "materials": HTML_MATERIALS, "quizzes": HTML_QUIZZES,
        "exercises": HTML_EXERCISES,
        "run_info": ["Buka berkasnya di browser: klik dua kali, atau Ctrl+O.",
                     "Di aplikasi ini strukturnya dibaca lalu ditampilkan",
                     "sebagai pohon elemen — itulah yang browser lihat dari",
                     "markup yang kamu tulis."],
    },
    {
        "key": "css", "label": "CSS", "runner": "css",
        "materials": CSS_MATERIALS, "quizzes": CSS_QUIZZES,
        "exercises": CSS_EXERCISES,
        "run_info": ['Tautkan dari HTML: <link rel="stylesheet" href="gaya.css">',
                     "lalu buka berkas HTML-nya di browser.",
                     "Di aplikasi ini aturannya dibaca lalu ditampilkan setelah",
                     "dirapikan: pemilih, lalu properti dan nilainya."],
    },
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
        "materials": PYTHON_MATERIALS, "quizzes": PYTHON_QUIZZES,
        "exercises": PYTHON_EXERCISES,
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
        "run_info": ["Jalankan : bash nama_file.sh",
                     "Atau: chmod +x nama_file.sh && ./nama_file.sh"],
    },
    {
        "key": "go", "label": "Go", "runner": "go",
        "materials": GO_MATERIALS, "quizzes": GO_QUIZZES, "exercises": GO_EXERCISES,
        "run_info": ["Jalankan : go run nama_file.go", "Build    : go build nama_file.go"],
    },
    {
        # Bukan bahasa pemrograman, melainkan kurikulum arsitektur aplikasi.
        # Latihannya Java murni, jadi memakai runner "java" yang sudah ada.
        "key": "aplikasi", "label": "Bikin Aplikasi", "runner": "java",
        "materials": APLIKASI_MATERIALS, "quizzes": APLIKASI_QUIZZES,
        "exercises": APLIKASI_EXERCISES,
        "run_info": ["Kompilasi : javac NamaFile.java", "Jalankan  : java NamaFile",
                     "Modul ini melatih cara berpikir membangun aplikasi,",
                     "bukan sintaks. Kerjakan setelah Java dasar terasa nyaman."],
    },
]


def _soal_per_kuis(lang):
    # Berkunci judul_kunci, sama seperti kunci progres yang tersimpan. Judul
    # kuis memang tidak berbentuk "angka-titik" sehingga tidak berubah hari
    # ini — tapi peta yang kuncinya beda bentuk dari yang mencarinya adalah
    # bug yang menunggu giliran, dan yang hilang nanti cuma penyebut skor:
    # angka yang salah, bukan error yang kelihatan.
    return {judul_kunci(q["title"]): len(q["questions"])
            for q in lang["quizzes"]}


def _tak_dinilai(lang):
    """Berapa latihan bahasa ini yang memang tidak bisa dinilai otomatis."""
    if not runner.tersedia(lang["runner"]):
        return len(lang["exercises"])
    return sum(1 for e in lang["exercises"] if e.get("auto_check") is False)


def _stat(lang, data):
    return statistik_bahasa(
        data, lang["key"], len(lang["materials"]), len(lang["quizzes"]),
        len(lang["exercises"]),
        soal_per_kuis=_soal_per_kuis(lang),
        latihan_tak_dinilai=_tak_dinilai(lang),
    )


# ------------------------------------------------------------------ dashboard

def baris_dashboard(data):
    """Blok ringkasan XP, level, streak, dan target harian di atas menu utama."""
    xp = data.get("xp", 0)
    level, di_level, butuh = info_level(xp)
    streak = data.get("streak", {})
    beruntun = streak_aktif(data)
    badge = len(data.get("badge", []))
    target = konfigurasi.ambil("target_xp_harian", 60)
    hari_ini = xp_hari_ini(data)

    nama = konfigurasi.ambil("nama", "")
    sapaan = f"  Halo, {nama}! " if nama else "  "

    lines = [
        sapaan + tema.cat(f"Level {level} - {gelar_dari_level(level)}", "judul", tema.TEBAL)
        + tema.cat(f"   {xp} XP", "teks"),
        "  " + bar(di_level, butuh, 28)
        + tema.cat(f"  {di_level}/{butuh} ke level {level + 1}", "redup"),
    ]

    if beruntun:
        teks_streak = tema.cat(f"  Streak {beruntun} hari", "subjudul", tema.TEBAL)
    else:
        teks_streak = tema.cat("  Streak terputus", "redup")
    lines.append(
        teks_streak
        + tema.cat(f"   (rekor {streak.get('terpanjang', 0)}, "
                   f"total {streak.get('total_hari', 0)} hari)", "redup")
        + tema.cat(f"   Badge {badge}/{len(DAFTAR_BADGE)}", "aksen")
    )

    peran_target = "sukses" if hari_ini >= target else "peringatan"
    lines.append(
        tema.cat("  Hari ini ", "teks") + bar(hari_ini, target, 20)
        + tema.cat(f"  {hari_ini}/{target} XP", peran_target)
        + (tema.cat("  target tercapai!", "sukses", tema.TEBAL)
           if hari_ini >= target else "")
    )
    return lines


_BLOK_HEATMAP = " ·▪■"


def baris_heatmap(data, pekan=13):
    """Riwayat XP harian sebagai petak, mirip heatmap kontribusi."""
    riwayat = riwayat_harian(data, pekan * 7)
    target = max(1, konfigurasi.ambil("target_xp_harian", 60))

    # Susun jadi 7 baris (Senin..Minggu) x N kolom pekan. Jumlah kolom dihitung
    # dari offset hari pertama: kalau dipatok `pekan`, hari-hari terakhir --
    # termasuk HARI INI -- akan terpotong setiap kali pekan pertama tidak
    # kebetulan dimulai hari Senin.
    mulai = date.fromisoformat(riwayat[0][0]).weekday()
    kolom = (len(riwayat) + mulai + 6) // 7
    petak = [[" "] * kolom for _ in range(7)]
    for i, (_, xp) in enumerate(riwayat):
        posisi = i + mulai
        hari, minggu = posisi % 7, posisi // 7
        if xp <= 0:
            tingkat = 0
        elif xp < target * 0.5:
            tingkat = 1
        elif xp < target:
            tingkat = 2
        else:
            tingkat = 3
        petak[hari][minggu] = _BLOK_HEATMAP[tingkat]

    nama_hari = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
    lines = [tema.cat(f"  Aktivitas {pekan} pekan terakhir:", "judul", tema.TEBAL)]
    for i, baris in enumerate(petak):
        isi = "".join(b + " " for b in baris)
        peran = "sukses" if any(b == "■" for b in baris) else "aksen"
        lines.append(tema.cat(f"   {nama_hari[i]} ", "redup") + tema.cat(isi, peran))
    lines.append(tema.cat("   Makin pekat = makin banyak XP hari itu.", "redup"))
    return lines


def baris_progres(languages, data):
    lines = [tema.cat("  Progres per bahasa:", "judul", tema.TEBAL)]
    total_skor = total_maks = 0
    for lang in languages:
        s = _stat(lang, data)
        total_skor += s["skor"]
        total_maks += s["skor_maks"]
        tanda_runner = "" if runner.tersedia(lang["runner"]) else tema.cat(" !", "galat")
        lines.append(
            tema.cat(f"   {lang['label']:<11}", "teks")
            + bar(s["persen"], 100, 12)
            + tema.cat(f" {s['persen']:>3.0f}%", "teks")
            + tema.cat(f"  materi {s['materi']}/{s['total_materi']}", "redup")
            + tema.cat(f"  kuis {s['kuis']}/{s['total_kuis']}", "redup")
            + tema.cat(f"  latihan {s['latihan_lulus'] + s['latihan_manual']}"
                       f"/{s['total_latihan']}", "redup")
            + tanda_runner
        )
    if total_maks:
        pct = total_skor / total_maks * 100
        lines.append(tema.cat(
            f"   Skor kuis terbaik keseluruhan: {total_skor}/{total_maks} ({pct:.0f}%)",
            "sukses", tema.TEBAL))
    if any(not runner.tersedia(l["runner"]) for l in languages):
        lines.append(tema.cat("   ! = toolchain belum terpasang (lihat Statistik)",
                              "redup"))
    return lines


def baris_saran(data):
    """Blok 'langkah berikutnya' -- penunjuk arah utama di menu."""
    langkah = langkah_berikutnya(LANGUAGES, data, maks=3)
    if not langkah:
        return []
    lines = [tema.cat("  Langkah berikutnya:", "judul", tema.TEBAL)]
    for s in langkah:
        lines.append(
            tema.cat(f"   {s.tipe:<8}", "aksen")
            + tema.cat(f"{s.lang['label']} - {s.judul}", "teks")
        )
        lines.append(tema.cat(f"            {s.alasan}", "redup"))
    return lines


# ---------------------------------------------------------------------- layar

def _buka_langkah(s):
    if s.tipe == "materi":
        render_material(s.obj, f"{s.lang['key']}_materi",
                        daftar=s.lang["materials"], lang=s.lang)
    elif s.tipe == "kuis":
        menu_satu_kuis(s.obj, f"{s.lang['key']}_kuis")
    else:
        show_exercise(s.obj, f"{s.lang['key']}_latihan", s.lang["runner"])


def menu_saran():
    while True:
        clear()
        data = load_progress()
        header("LANGKAH BERIKUTNYA", "disusun dari progresmu sendiri")
        langkah = langkah_berikutnya(LANGUAGES, data, maks=8)
        if not langkah:
            print(tema.cat("\n  Semuanya sudah beres. Luar biasa!", "sukses", tema.TEBAL))
            press_enter()
            return

        names = [f"{tema.cat(s.tipe + ':', 'aksen')} {s.label()}\n"
                 f"       {tema.cat(s.alasan, 'redup')}" for s in langkah]
        pilih = ask_choice(paint("  Mau mulai dari mana?", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        _buka_langkah(langkah[pilih - 1])


def menu_tantangan():
    clear()
    data = load_progress()
    header("TANTANGAN HARI INI", date.today().isoformat())
    t = tantangan_harian(LANGUAGES, data)
    if not t:
        print(tema.cat("\n  Semua latihan sudah kamu selesaikan. Tidak ada tantangan "
                       "tersisa!", "sukses", tema.TEBAL))
        press_enter()
        return

    for baris in kotak([
        tema.cat(f"{t.lang['label']} - {t.judul}", "teks", tema.TEBAL),
        tema.cat(f"Tingkat: {t.obj.get('difficulty', '-')}", "redup"),
        "",
        tema.cat("Tantangan berganti tiap hari dan selalu sama untuk hari yang sama.",
                 "redup"),
    ], judul="TANTANGAN"):
        print(baris)

    print()
    if confirm("Kerjakan sekarang?", default=True):
        _buka_langkah(t)


def language_menu(lang):
    while True:
        clear()
        data = load_progress()
        s = _stat(lang, data)
        header("BAHASA: " + lang["label"], f"{s['persen']:.0f}% selesai")

        print("  " + bar(s["persen"], 100, 30)
              + tema.cat(f"  {s['persen']:.0f}%", "teks", tema.TEBAL))

        # Ringkasan bab pakai bar KEDUA yang sengaja lebih pendek. Dua ukuran
        # yang sama panjang akan terbaca sebagai dua hal yang sederajat,
        # padahal yang di atas adalah kemajuan seluruh bahasa ini.
        tuntas_bab, jumlah_bab, _ = bab.ringkas(lang, data)
        kalimat_bab = bab.kalimat_ringkas(lang, data)
        if jumlah_bab > 1:
            print("  " + bar(tuntas_bab, jumlah_bab, 12)
                  + tema.cat(f"  {tuntas_bab}/{jumlah_bab} bab tuntas", "teks"))
            if kalimat_bab:
                # Kalimatnya berdiri sendiri DI SINI, bukan ditempel ke baris
                # menu "Materi". Baris menu digambar ulang tiap tombol panah
                # dan karena itu dipotong selebar layar; di terminal 80 kolom
                # -- ukuran bawaan -- ekornya berubah jadi "…" persis pada
                # bagian yang paling perlu dibaca: nama bab dan sisa materinya.
                print(tema.cat("  " + utils.potong(kalimat_bab, lebar() - 2),
                               "redup"))

        if not runner.tersedia(lang["runner"]):
            hilang = ", ".join(runner.program_hilang(lang["runner"]))
            print(tema.cat(f"  Runner nonaktif: {hilang} belum terpasang.", "galat"))
            saran_pasang = runner.perintah_instalasi(lang["runner"])
            if saran_pasang:
                print(tema.cat(f"  Pasang dengan: {saran_pasang}", "info"))
        print(rule("-", C.DIM, bold=False))

        selesai_latihan = s["latihan_lulus"] + s["latihan_manual"]
        pilih = ask_choice(
            paint("  Pilih menu:", C.BLUE, C.BOLD),
            [
                f"Materi        ({s['materi']}/{s['total_materi']} dibaca)",
                f"Kuis          ({s['kuis']}/{s['total_kuis']} dikerjakan)",
                f"Latihan Kode  ({selesai_latihan}/{s['total_latihan']} selesai)",
                "Cara menjalankan kode " + lang["label"],
            ],
        )
        if pilih == 0:
            return
        if pilih == 1:
            materials_menu(lang["label"], lang["materials"], f"{lang['key']}_materi",
                           lang=lang)
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
        print(tema.cat("   " + info, "teks"))
    print()
    tc = runner.TOOLCHAINS.get(lang["runner"])
    if runner.tersedia(lang["runner"]):
        print(tema.cat("  Status: toolchain terpasang, kode bisa dijalankan dari "
                       "aplikasi ini.", "sukses"))
    else:
        hilang = ", ".join(runner.program_hilang(lang["runner"]))
        print(tema.cat(f"  Status: {hilang} belum terpasang.", "galat"))
        saran_pasang = runner.perintah_instalasi(lang["runner"])
        if saran_pasang:
            print(tema.cat("\n  Cara memasangnya di komputer ini:", "info", tema.TEBAL))
            print(tema.cat(f"    {saran_pasang}", "sukses", tema.TEBAL))
        if tc and tc.instalasi:
            print(tema.cat("\n  Sistem lain:", "redup"))
            for sistem, perintah in tc.instalasi.items():
                print(tema.cat(f"    {sistem:<9} {perintah}", "redup"))
        print(tema.cat("\n  Materi & kuis tetap bisa dipakai; latihan bisa ditandai "
                       "selesai manual.", "redup"))
    if tc and tc.catatan:
        print(tema.cat("\n  Catatan: " + tc.catatan, "peringatan"))
    press_enter()


def menu_badge():
    clear()
    data = load_progress()
    dimiliki = set(data.get("badge", []))
    header("BADGE", f"{len(dimiliki)} dari {len(DAFTAR_BADGE)} terbuka")

    for bid, nama, deskripsi, _ in DAFTAR_BADGE:
        if bid in dimiliki:
            print(tema.cat(f"  [v] {nama:<22}", "sukses", tema.TEBAL)
                  + tema.cat(deskripsi, "teks"))
        else:
            print(tema.cat(f"  [ ] {nama:<22}", "redup") + tema.cat(deskripsi, "redup"))
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
    for line in baris_heatmap(data):
        print(line)
    print(rule("-", C.DIM, bold=False))

    print(tema.cat("  Ketersediaan runner:", "judul", tema.TEBAL))
    for lang in LANGUAGES:
        if runner.tersedia(lang["runner"]):
            status = tema.cat("terpasang", "sukses")
        else:
            hilang = ", ".join(runner.program_hilang(lang["runner"]))
            status = tema.cat(f"belum ada: {hilang}", "galat")
            saran_pasang = runner.perintah_instalasi(lang["runner"])
            if saran_pasang:
                status += tema.cat(f"  ->  {saran_pasang}", "redup")
        print(tema.cat(f"   {lang['label']:<11}", "teks") + status)
    press_enter()


# ----------------------------------------------------------------- pengaturan

def _ubah_opsi(opsi):
    nilai_kini = konfigurasi.ambil(opsi.kunci)
    clear()
    header("PENGATURAN: " + opsi.label)
    print(tema.cat("  " + opsi.keterangan, "redup"))
    print(tema.cat(f"  Sekarang: {opsi.tampil(nilai_kini)}", "teks", tema.TEBAL))
    print(rule("-", C.DIM, bold=False))

    if opsi.jenis == "sakelar":
        konfigurasi.pasang(opsi.kunci, not nilai_kini)
        return
    if opsi.jenis == "pilihan":
        label = [l for _, l in opsi.pilihan]
        pilih = ask_choice(paint("  Pilih nilai:", C.BLUE, C.BOLD), label)
        if pilih == 0:
            return
        konfigurasi.pasang(opsi.kunci, opsi.pilihan[pilih - 1][0])
        return
    if opsi.jenis == "angka":
        batas = f" ({opsi.minimum}-{opsi.maksimum}, 0 = otomatis)"
        raw = ask(f"  Nilai baru{batas} > ", "")
        if raw.strip():
            konfigurasi.pasang(opsi.kunci, raw.strip())
        return

    raw = ask("  Nilai baru (kosongkan untuk mengosongkan) > ", "")
    konfigurasi.pasang(opsi.kunci, raw)


def menu_pengaturan():
    while True:
        clear()
        header("PENGATURAN", f"tersimpan di {konfigurasi.BERKAS}")
        print(tema.cat(
            f"  Terminal terdeteksi: {tema.nama_kedalaman(tema.kedalaman_aktif())}"
            f", lebar {lebar()} kolom", "redup"))
        print(rule("-", C.DIM, bold=False))

        daftar = konfigurasi.daftar_opsi()
        names = [f"{o.label:<34} " + tema.cat(o.tampil(konfigurasi.ambil(o.kunci)), "aksen")
                 for o in daftar]
        pilih = ask_choice(paint("  Ubah pengaturan:", C.BLUE, C.BOLD), names,
                           extra={"r": "Kembalikan semua ke bawaan"})
        if pilih == 0:
            return
        if pilih == "r":
            if confirm("Kembalikan SEMUA pengaturan ke bawaan?"):
                konfigurasi.kembalikan_bawaan()
                utils.sinkron_warna()
            continue
        _ubah_opsi(daftar[pilih - 1])
        utils.sinkron_warna()


# --------------------------------------------------------------- kelola data

def _teks_laporan(data):
    """Laporan kemajuan dalam Markdown, siap disimpan atau ditempel di mana pun."""
    xp = data.get("xp", 0)
    level, _, _ = info_level(xp)
    streak = data.get("streak", {})
    baris = [
        "# Laporan Kemajuan Belajar Ngoding",
        "",
        f"Tanggal : {date.today().isoformat()}",
        f"Level   : {level} - {gelar_dari_level(level)}  ({xp} XP)",
        f"Streak  : {streak_aktif(data)} hari berjalan, "
        f"rekor {streak.get('terpanjang', 0)}, "
        f"total {streak.get('total_hari', 0)} hari belajar",
        f"Badge   : {len(data.get('badge', []))} dari {len(DAFTAR_BADGE)}",
        "",
        "## Progres per bahasa",
        "",
        "| Bahasa | Materi | Kuis | Latihan | Skor kuis | Selesai |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for lang in LANGUAGES:
        s = _stat(lang, data)
        skor = f"{s['skor']}/{s['skor_maks']}" if s["skor_maks"] else "-"
        baris.append(
            f"| {lang['label']} | {s['materi']}/{s['total_materi']} "
            f"| {s['kuis']}/{s['total_kuis']} "
            f"| {s['latihan_lulus'] + s['latihan_manual']}/{s['total_latihan']} "
            f"| {skor} | {s['persen']:.0f}% |"
        )

    dimiliki = set(data.get("badge", []))
    baris += ["", "## Badge yang terbuka", ""]
    terbuka = [f"- {nama} - {desk}" for bid, nama, desk, _ in DAFTAR_BADGE
               if bid in dimiliki]
    baris += terbuka or ["- (belum ada)"]
    return "\n".join(baris) + "\n"


def menu_data():
    while True:
        clear()
        header("KELOLA DATA BELAJAR", PROGRESS_FILE)
        data = load_progress()
        print(tema.cat(f"  XP {data.get('xp', 0)} | "
                       f"{len(data['materi_dibaca'])} materi | "
                       f"{len(data['kuis_skor'])} kuis | "
                       f"{len(data['latihan_lulus'])} latihan lulus", "teks"))
        print(rule("-", C.DIM, bold=False))

        pilih = ask_choice(paint("  Pilih tindakan:", C.BLUE, C.BOLD), [
            "Simpan laporan kemajuan (Markdown)",
            "Ekspor progres ke berkas JSON",
            "Impor progres dari berkas JSON",
            "Buat cadangan sekarang",
            "Reset progres satu bahasa",
            "Reset SELURUH progres",
        ])
        if pilih == 0:
            return

        if pilih == 1:
            tujuan = ask("  Simpan ke [laporan-belajar.md] > ", "") or "laporan-belajar.md"
            try:
                with open(os.path.expanduser(tujuan), "w", encoding="utf-8") as f:
                    f.write(_teks_laporan(data))
                print(tema.cat(f"  Tersimpan di {tujuan}", "sukses"))
            except OSError as e:
                print(tema.cat(f"  Gagal menyimpan: {e}", "galat"))
        elif pilih == 2:
            tujuan = ask("  Ekspor ke [progres-belajar.json] > ", "") or "progres-belajar.json"
            ok, pesan = ekspor(tujuan)
            print(tema.cat(("  Tersimpan di " if ok else "  Gagal: ") + pesan,
                           "sukses" if ok else "galat"))
        elif pilih == 3:
            asal = ask("  Impor dari berkas > ", "")
            if not asal.strip():
                continue
            if not confirm("Progres saat ini akan DIGANTI (dicadangkan dulu). Lanjut?"):
                continue
            ok, pesan = impor(asal.strip())
            print(tema.cat(("  Berhasil. Cadangan lama: " if ok else "  Gagal: ") + pesan,
                           "sukses" if ok else "galat"))
        elif pilih == 4:
            hasil = cadangkan()
            print(tema.cat(f"  Cadangan: {hasil}" if hasil
                           else "  Belum ada progres untuk dicadangkan.",
                           "sukses" if hasil else "redup"))
        elif pilih == 5:
            nama = [l["label"] for l in LANGUAGES]
            b = ask_choice(paint("  Reset bahasa mana?", C.BLUE, C.BOLD), nama)
            if b == 0:
                continue
            lang = LANGUAGES[b - 1]
            if confirm(f"Hapus SEMUA progres {lang['label']}? Tidak bisa dibatalkan."):
                cadangan = reset(lang["key"])
                print(tema.cat(f"  Progres {lang['label']} dihapus. "
                               f"Cadangan: {cadangan or '-'}", "sukses"))
        elif pilih == 6:
            if confirm("Hapus SELURUH progres semua bahasa? Tidak bisa dibatalkan."):
                if confirm("Yakin betul? Jawab y sekali lagi."):
                    cadangan = reset("semua")
                    print(tema.cat(f"  Semua progres dihapus. "
                                   f"Cadangan: {cadangan or '-'}", "sukses"))
        press_enter()


def about():
    clear()
    header("TENTANG APLIKASI INI", f"versi {VERSI}")
    print(tema.cat("  Aplikasi belajar pemrograman dari nol lewat terminal.", "teks"))
    print(tema.cat(f"  {len(LANGUAGES)} bahasa: "
                   + ", ".join(l["label"] for l in LANGUAGES), "teks"))
    print()
    print(tema.cat("  Fitur:", "judul", tema.TEBAL))
    for f in [
        "Materi bertahap dengan contoh kode bersorot sintaks",
        "Kuis dengan soal & opsi diacak, mode timer, dan review jawaban salah",
        "Latihan coding yang DIJALANKAN dan dinilai otomatis dari output-nya",
        "Umpan balik berupa diff: baris & kolom mana yang beda, plus tebakan sebabnya",
        "Pesan error compiler diterjemahkan ke bahasa Indonesia",
        "Kuis dijadwalkan ulang otomatis supaya tidak cepat lupa",
        "Saran langkah berikutnya & tantangan harian",
        "Pencarian lintas bahasa, bookmark, dan lanjut dari terakhir",
        "XP, level, streak harian, target harian, dan badge",
    ]:
        print(tema.cat("   - " + f, "teks"))
    print()
    print(tema.cat("  Alur belajar yang disarankan:", "sukses", tema.TEBAL))
    for i, langkah in enumerate([
        "Baca materi berurutan sampai habis",
        "Ketik ulang contoh kodenya, jangan copy-paste",
        "Kerjakan latihan sampai statusnya LULUS",
        "Uji pemahaman lewat kuis",
        "Ulangi kuis saat ditandai 'saatnya diulang'",
    ], start=1):
        print(tema.cat(f"   {i}. {langkah}", "teks"))
    print()
    print(tema.cat(f"  Progres    : {PROGRESS_FILE}", "redup"))
    print(tema.cat(f"  Pengaturan : {konfigurasi.BERKAS}", "redup"))
    press_enter()


def _menu_statistik():
    while True:
        clear()
        header("STATISTIK & PENCAPAIAN")
        pilih = ask_choice(paint("  Pilih:", C.BLUE, C.BOLD),
                           ["Statistik lengkap", "Daftar badge", "Kelola data belajar"])
        if pilih == 0:
            return
        if pilih == 1:
            menu_statistik()
        elif pilih == 2:
            menu_badge()
        else:
            menu_data()


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
        blok_saran = baris_saran(data)
        if blok_saran:
            print(rule("-", C.DIM, bold=False))
            for line in blok_saran:
                print(line)
        print(rule())

        options = [lang["label"] for lang in LANGUAGES]
        pilih = ask_choice(
            paint("  Pilih bahasa yang mau dipelajari:", C.BLUE, C.BOLD),
            options,
            allow_back=False,
            extra={
                "n": "Langkah berikutnya (rekomendasi)",
                "h": "Tantangan hari ini",
                "l": "Lanjutkan dari terakhir",
                "c": "Cari di semua bahasa",
                "b": "Bookmark",
                "s": "Statistik, badge & data",
                "p": "Pengaturan",
                "t": "Tentang aplikasi",
                "k": "Keluar",
            },
        )

        # 0 muncul saat stdin habis (pipe/Ctrl+D). Tanpa penanganan ini menu
        # utama dulu berputar selamanya dan membanjiri terminal puluhan MB.
        if pilih == "k" or pilih == 0:
            print(tema.cat("\n  Terima kasih sudah belajar. Semangat terus!\n",
                           "sukses", tema.TEBAL))
            return
        if pilih == "n":
            menu_saran()
        elif pilih == "h":
            menu_tantangan()
        elif pilih == "l":
            lanjut_terakhir(LANGUAGES)
        elif pilih == "c":
            cari_global(LANGUAGES)
        elif pilih == "b":
            menu_bookmark(LANGUAGES)
        elif pilih == "s":
            _menu_statistik()
        elif pilih == "p":
            menu_pengaturan()
        elif pilih == "t":
            about()
        elif isinstance(pilih, int) and 1 <= pilih <= len(LANGUAGES):
            language_menu(LANGUAGES[pilih - 1])


# ----------------------------------------------------------------------- CLI

def _argumen(argv=None):
    p = argparse.ArgumentParser(
        prog="belajar", add_help=False,
        description="Aplikasi belajar pemrograman berbahasa Indonesia di terminal.")
    p.add_argument("--bantuan", "-h", action="store_true", help="tampilkan bantuan ini")
    p.add_argument("--versi", "-v", action="store_true", help="tampilkan versi")
    p.add_argument("--tanpa-warna", action="store_true", help="matikan semua warna")
    p.add_argument("--tema", metavar="NAMA",
                   help="paksa tema: " + ", ".join(tema.TEMA))
    p.add_argument("--lebar", type=int, metavar="N", help="kunci lebar layar")
    p.add_argument("--bahasa", metavar="KEY",
                   help="langsung buka satu bahasa: "
                        + ", ".join(l["key"] for l in LANGUAGES))
    p.add_argument("--statistik", action="store_true",
                   help="cetak ringkasan progres lalu keluar")
    p.add_argument("--laporan", nargs="?", const="-", metavar="BERKAS",
                   help="tulis laporan Markdown (tanpa nama berkas = ke layar)")
    p.add_argument("--cek-toolchain", action="store_true",
                   help="periksa compiler/interpreter yang terpasang")
    p.add_argument("--ekspor", metavar="BERKAS", help="ekspor progres ke JSON")
    p.add_argument("--impor", metavar="BERKAS", help="impor progres dari JSON")
    return p, p.parse_args(argv)


def _cetak_cek_toolchain():
    print("Ketersediaan toolchain:\n")
    kurang = 0
    for lang in LANGUAGES:
        if runner.tersedia(lang["runner"]):
            print(f"  [v] {lang['label']:<12} siap")
        else:
            kurang += 1
            hilang = ", ".join(runner.program_hilang(lang["runner"]))
            print(f"  [ ] {lang['label']:<12} butuh {hilang}")
            saran_pasang = runner.perintah_instalasi(lang["runner"])
            if saran_pasang:
                print(f"      pasang: {saran_pasang}")
    print(f"\n{len(LANGUAGES) - kurang}/{len(LANGUAGES)} bahasa bisa dinilai otomatis.")
    print("Materi dan kuis tetap jalan penuh tanpa toolchain apa pun.")
    return 0


def _cetak_statistik():
    data = load_progress()
    for line in baris_dashboard(data):
        print(line)
    print()
    for line in baris_progres(LANGUAGES, data):
        print(line)
    return 0


def cli(argv=None):
    parser, arg = _argumen(argv)

    konfigurasi.terapkan()
    if arg.tanpa_warna:
        tema.pakai_kedalaman(tema.TANPA_WARNA)
    if arg.tema and not tema.pakai_tema(arg.tema):
        print(f"Tema '{arg.tema}' tidak dikenal. Pilihan: {', '.join(tema.TEMA)}")
        return 2
    if arg.lebar:
        konfigurasi.pasang("lebar", arg.lebar, langsung_simpan=False)
    utils.sinkron_warna()

    if arg.bantuan:
        parser.print_help()
        return 0
    if arg.versi:
        print(f"Belajar Ngoding versi {VERSI} (Python {sys.version.split()[0]})")
        return 0
    if arg.cek_toolchain:
        return _cetak_cek_toolchain()
    if arg.statistik:
        return _cetak_statistik()
    if arg.laporan:
        teks = _teks_laporan(load_progress())
        if arg.laporan == "-":
            print(teks)
            return 0
        try:
            with open(os.path.expanduser(arg.laporan), "w", encoding="utf-8") as f:
                f.write(teks)
            print(f"Laporan tersimpan di {arg.laporan}")
            return 0
        except OSError as e:
            print(f"Gagal menulis laporan: {e}")
            return 1
    if arg.ekspor:
        ok, pesan = ekspor(arg.ekspor)
        print(("Tersimpan di " if ok else "Gagal: ") + pesan)
        return 0 if ok else 1
    if arg.impor:
        ok, pesan = impor(arg.impor)
        print(("Berhasil. Cadangan lama: " if ok else "Gagal: ") + pesan)
        return 0 if ok else 1

    if arg.bahasa:
        lang = next((l for l in LANGUAGES if l["key"] == arg.bahasa.lower()), None)
        if not lang:
            print(f"Bahasa '{arg.bahasa}' tidak dikenal. "
                  f"Pilihan: {', '.join(l['key'] for l in LANGUAGES)}")
            return 2
        language_menu(lang)
        return 0

    main_menu()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except KeyboardInterrupt:
        print(tema.cat("\n\n  Sampai jumpa! Tetap semangat belajar ya.\n",
                       "sukses", tema.TEBAL))
        sys.exit(0)
