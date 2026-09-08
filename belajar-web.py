#!/usr/bin/env python3
"""Jalankan antarmuka web aplikasi belajar.

    python3 belajar-web.py            nyalakan lalu buka browser
    python3 belajar-web.py --bantuan  daftar opsi

Aplikasi terminalnya tetap ada dan tidak berubah: `python3 main.py`. Keduanya
membaca dan menulis berkas progres yang sama, jadi materi yang dibaca di
browser langsung terhitung di terminal, dan sebaliknya.

Tanpa dependensi luar. Yang dibutuhkan cuma Python 3.8+ dan sebuah browser.
"""

import argparse
import os
import sys
import threading
import webbrowser

# Jalankan dari mana pun: modul aplikasi ada di folder berkas ini, bukan di
# folder kerja pengguna.
AKAR = os.path.dirname(os.path.abspath(__file__))
if AKAR not in sys.path:
    sys.path.insert(0, AKAR)

PORT_BAWAAN = 7777


def _argumen(argv=None):
    p = argparse.ArgumentParser(
        prog="belajar-web", add_help=False,
        description="Antarmuka web aplikasi belajar pemrograman.")
    p.add_argument("--bantuan", "-h", action="store_true",
                   help="tampilkan bantuan ini")
    p.add_argument("--port", type=int, default=PORT_BAWAAN, metavar="N",
                   help=f"port yang dipakai (bawaan {PORT_BAWAAN}; kalau sudah "
                        "terpakai, port berikutnya dicoba otomatis)")
    p.add_argument("--tanpa-browser", action="store_true",
                   help="jangan buka browser, cukup cetak alamatnya")
    p.add_argument("--berisik", action="store_true",
                   help="cetak setiap permintaan HTTP (untuk mencari masalah)")
    return p, p.parse_args(argv)


def _cetak_sambutan(url, langsung_buka):
    import runner
    from main import LANGUAGES

    materi = sum(len(l["materials"]) for l in LANGUAGES)
    soal = sum(len(q["questions"]) for l in LANGUAGES for q in l["quizzes"])
    latihan = sum(len(l["exercises"]) for l in LANGUAGES)
    siap = [l["label"] for l in LANGUAGES if runner.tersedia(l["runner"])]
    belum = [l for l in LANGUAGES if not runner.tersedia(l["runner"])]

    lebar = 60
    judul = (f"{len(LANGUAGES)} bahasa · {materi} materi · {soal} soal kuis "
             f"· {latihan} latihan")
    print()
    print("  ┌" + "─" * lebar + "┐")
    print("  │" + "  BELAJAR NGODING".ljust(lebar) + "│")
    print("  │" + f"  {judul}".ljust(lebar) + "│")
    print("  └" + "─" * lebar + "┘")
    print()
    print(f"    Buka di browser :  {url}")
    print("    Hentikan        :  Ctrl+C di jendela ini")
    print()
    print(f"    Kode bisa dijalankan untuk: {', '.join(siap) or '(belum ada)'}")
    for l in belum:
        pasang = runner.perintah_instalasi(l["runner"])
        kurang = ", ".join(runner.program_hilang(l["runner"]))
        print(f"    {l['label']:<14} butuh {kurang}"
              + (f"  →  {pasang}" if pasang else ""))
    if belum:
        print("    (materi & kuis tetap jalan penuh tanpa itu semua)")
    print()
    if langsung_buka:
        print("    Membuka browser...")
        print()
    # Setelah ini proses masuk ke serve_forever dan tidak mencetak apa-apa lagi
    # untuk waktu yang lama. Kalau keluarannya dialihkan ke berkas, Python
    # menyanggahnya di buffer -- dan pengguna menatap berkas kosong sambil
    # mengira servernya gagal menyala.
    sys.stdout.flush()


def utama(argv=None):
    parser, arg = _argumen(argv)
    if arg.bantuan:
        parser.print_help()
        return 0

    from webapp import server as modul_server

    def ketika_siap(url):
        _cetak_sambutan(url, not arg.tanpa_browser)
        if arg.tanpa_browser:
            return
        # Dijadwalkan sedikit tertunda: `serve_forever` baru mulai menerima
        # koneksi SETELAH callback ini selesai, jadi membuka browser langsung
        # di sini bisa mendarat di port yang belum mendengarkan.
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()

    try:
        return modul_server.jalankan(port=arg.port, berisik=arg.berisik,
                                     siap=ketika_siap)
    except OSError as e:
        print(f"\n  Gagal menyalakan server: {e}\n")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(utama())
    except KeyboardInterrupt:
        print("\n\n  Server dihentikan. Sampai jumpa!\n")
        sys.exit(0)
