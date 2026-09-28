"""Helper tampilan terminal: warna, banner, paginasi, dan input pilihan.

Modul ini sengaja hanya mengurus URUSAN TAMPILAN. Semua yang berkaitan
dengan penyimpanan progres belajar ada di `progress.py`, palet warnanya di
`tema.py`, dan preferensi pengguna di `konfigurasi.py`.

Dua aturan yang dipegang seluruh modul ini:

1. **Tidak boleh ada loop tak berujung.** Setiap prompt harus punya jalan
   keluar walaupun stdin sudah habis (pipe tertutup, Ctrl+D, koneksi putus).
   Dulu `ask_choice` di menu utama berputar selamanya saat EOF dan membanjiri
   terminal dengan puluhan megabyte "Pilihan tidak valid".
2. **Lebar layar mengikuti terminal.** Angka 60 yang dulu dipatok membuat
   materi meluap di terminal sempit dan menyisakan setengah layar kosong di
   terminal lebar.
"""

import os
import re
import shutil
import sys
import textwrap

from inti import tema

try:                       # konfigurasi bergantung pada tema, bukan pada utils
    from pelajar import konfigurasi
except ImportError:        # tetap bisa dipakai walau modulnya belum ada
    konfigurasi = None


LEBAR_BAWAAN = 60
LEBAR_MIN = 52
LEBAR_MAKS = 100


class C:
    """Kode ANSI mentah.

    Dipertahankan supaya kode lama tetap jalan. Untuk kode baru pakai
    `tema.cat(teks, "peran")` yang mengikuti tema pilihan pengguna.
    """

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


def supports_color():
    """True kalau terminal kemungkinan besar bisa menampilkan warna ANSI."""
    return tema.deteksi_kedalaman() != tema.TANPA_WARNA


COLORS_ON = supports_color()


def sinkron_warna():
    """Samakan COLORS_ON dengan kedalaman warna tema yang sedang aktif.

    Dipanggil setelah konfigurasi diterapkan atau tema diganti dari menu.
    """
    global COLORS_ON
    COLORS_ON = tema.berwarna()
    return COLORS_ON


def paint(text, *colors):
    """Bungkus teks dengan kode warna ANSI (no-op kalau warna dimatikan)."""
    if not COLORS_ON or not colors:
        return text
    return f"{''.join(colors)}{text}{C.RESET}"


# CSI (termasuk yang bukan SGR), OSC berakhiran BEL atau ST, dan escape dua
# karakter. Versi lama hanya mencari huruf 'm' pertama, sehingga
# strip_ansi("\033[2Jhalo mantap") memakan teks sampai 'm' pada kata "mantap".
_POLA_ANSI = re.compile(
    r"\x1b\[[0-?]*[ -/]*[@-~]"             # CSI ... huruf akhir
    r"|\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)"  # OSC ... BEL / ST
    r"|\x1b\[[0-?]*[ -/]*\Z"               # CSI terpotong di ujung string
    r"|\x1b\][^\x07\x1b]*\Z"               # OSC terpotong di ujung string
    r"|\x1b[@-Z\\-_]"                      # escape dua karakter
    r"|\x1b"                               # ESC menggantung sendirian
)


def strip_ansi(text):
    """Buang kode escape dari string. Untuk menghitung lebar & mencari teks."""
    return _POLA_ANSI.sub("", text)


def visible_len(text):
    return len(strip_ansi(text))


# ------------------------------------------------------------------- ukuran

def _ukuran_terminal():
    try:
        return shutil.get_terminal_size((LEBAR_BAWAAN + 20, 24))
    except (OSError, ValueError):
        return os.terminal_size((LEBAR_BAWAAN + 20, 24))


def lebar():
    """Lebar garis & bingkai, mengikuti terminal kecuali dikunci pengguna."""
    if konfigurasi is not None:
        try:
            dipilih = int(konfigurasi.ambil("lebar", 0) or 0)
        except (TypeError, ValueError):
            dipilih = 0
        if dipilih:
            return max(LEBAR_MIN, min(LEBAR_MAKS, dipilih))
    kolom = _ukuran_terminal().columns
    return max(LEBAR_MIN, min(LEBAR_MAKS, kolom - 2))


def tinggi_halaman(sisa=8):
    """Berapa baris isi yang muat satu layar, menyisakan ruang untuk navigasi."""
    if konfigurasi is not None:
        try:
            dipilih = int(konfigurasi.ambil("tinggi_halaman", 0) or 0)
        except (TypeError, ValueError):
            dipilih = 0
        if dipilih:
            return max(5, dipilih)
    baris = _ukuran_terminal().lines
    return max(8, baris - sisa)


# `WIDTH` dipertahankan sebagai konstanta agar kode & tes lama tetap jalan,
# tapi kode baru sebaiknya memanggil `lebar()` supaya ikut berubah saat jendela
# terminal diubah ukurannya di tengah sesi.
WIDTH = lebar()


# ------------------------------------------------------------------ bingkai

def potong(teks, maks):
    """Potong teks (sadar ANSI) supaya tidak merusak bingkai."""
    if maks <= 1:
        return ""
    if visible_len(teks) <= maks:
        return teks
    polos = strip_ansi(teks)
    return polos[: maks - 1] + "…"


def pusatkan(teks, kolom=None):
    """str.center yang menghitung lebar tanpa kode warna, dan memotong dulu."""
    kolom = kolom or lebar()
    teks = potong(teks, kolom)
    sisa = kolom - visible_len(teks)
    kiri = sisa // 2
    return " " * kiri + teks + " " * (sisa - kiri)


def rule(char="=", color=C.CYAN, bold=True):
    styles = [color, C.BOLD] if bold else [color]
    return paint(char * lebar(), *styles)


def garis(char="─", peran="garis"):
    """Garis pemisah bergaya tema. Versi modern dari `rule`."""
    return tema.cat(char * lebar(), peran)


def banner(title, subtitle=""):
    print("\n" + rule())
    print(paint(pusatkan(title), C.YELLOW, C.BOLD))
    if subtitle:
        print(paint(pusatkan(subtitle), C.DIM))
    print(rule() + "\n")


def header(title, subtitle=""):
    """Banner tanpa baris kosong pembuka. Dipakai tepat setelah clear()."""
    print(rule())
    print(paint(pusatkan(title), C.YELLOW, C.BOLD))
    if subtitle:
        print(paint(pusatkan(subtitle), C.DIM))
    print(rule())


def kotak(baris, judul="", peran="garis"):
    """Bingkai kotak di sekeliling beberapa baris teks. Return list baris."""
    lbr = lebar()
    dalam = lbr - 4
    atas = ("┌─ " + judul + " ") if judul else "┌"
    atas = atas + "─" * max(0, lbr - visible_len(atas) - 1) + "┐"
    keluar = [tema.cat(atas, peran)]
    for b in baris:
        isi = potong(b, dalam)
        pad = " " * max(0, dalam - visible_len(isi))
        keluar.append(tema.cat("│ ", peran) + isi + pad + tema.cat(" │", peran))
    keluar.append(tema.cat("└" + "─" * (lbr - 2) + "┘", peran))
    return keluar


def press_enter(msg="Tekan ENTER untuk lanjut..."):
    try:
        input(paint("\n  " + msg, C.DIM))
    except EOFError:
        print()


def clear():
    """Bersihkan layar tanpa memanggil shell.

    `os.system("clear")` dulu dipakai di sini, tapi kalau TERM tidak diset
    perintah itu mencetak "TERM environment variable not set." ke layar dan
    tidak menghapus apa pun -- persis kebalikan dari yang diinginkan.
    """
    if not COLORS_ON:
        print("\n" * 2)
        return
    try:
        sys.stdout.write("\033[H\033[2J\033[3J")
        sys.stdout.flush()
    except (OSError, ValueError):
        print("\n" * 2)


# -------------------------------------------------------------------- input

def ask(prompt, default=""):
    """input() yang tidak meledak saat stdin habis (mis. dijalankan via pipe)."""
    hasil = ask_atau_eof(prompt)
    return default if hasil is None else hasil


def ask_atau_eof(prompt):
    """Seperti `ask`, tapi mengembalikan None saat stdin sudah habis.

    Membedakan "pengguna menekan ENTER" dari "tidak akan ada masukan lagi"
    adalah satu-satunya cara menghentikan menu tanpa berputar selamanya.
    """
    try:
        return input(paint(prompt, C.CYAN)).strip()
    except EOFError:
        print()
        return None


def ask_timed(prompt, detik):
    """input() dengan batas waktu. Return (jawaban, kehabisan_waktu).

    `jawaban` bernilai None kalau stdin habis (EOF). Di POSIX memakai select()
    supaya benar-benar berhenti saat waktu habis; di platform lain waktu
    dihitung setelah user menekan ENTER.
    """
    import time

    if detik <= 0:
        return ask_atau_eof(prompt), False

    try:
        import select

        if os.name == "nt" or not hasattr(sys.stdin, "fileno"):
            raise ImportError
        sys.stdin.fileno()          # melempar kalau stdin diganti StringIO

        print(paint(prompt, C.CYAN), end="", flush=True)
        siap, _, _ = select.select([sys.stdin], [], [], detik)
        if not siap:
            print(paint("\n  Waktu habis!", C.RED, C.BOLD))
            return "", True

        baris = sys.stdin.readline()
        if baris == "":
            # select() melaporkan "siap" juga saat pipe sudah ditutup; tanpa
            # pemeriksaan ini pemanggil menerima "" berulang selamanya.
            print()
            return None, False
        return baris.strip(), False
    except (ImportError, OSError, ValueError, AttributeError):
        mulai = time.monotonic()
        jawab = ask_atau_eof(prompt)
        habis = jawab is not None and (time.monotonic() - mulai) > detik
        return jawab, habis


def angka_pilihan(raw, maksimum):
    """Ubah masukan jadi nomor menu yang sah, atau None.

    `str.isdigit()` bernilai True untuk '²' padahal `int('²')` melempar
    ValueError -- satu karakter tempelan itu dulu cukup untuk menjatuhkan
    seluruh aplikasi dengan traceback.
    """
    if not (raw.isascii() and raw.isdigit()):
        return None
    try:
        nilai = int(raw)
    except ValueError:
        return None
    return nilai if 1 <= nilai <= maksimum else None


MAKS_SALAH_BERTURUT = 8

# ---------------------------------------------------------------------------
# Navigasi panah
#
# Menu tetap bernomor seperti sebelumnya, tapi kalau aplikasi dijalankan di
# terminal sungguhan, kursor bisa digeser dengan panah dan dipilih dengan
# ENTER. Mengetik angka lalu ENTER tetap berfungsi persis seperti dulu, jadi
# kebiasaan lama tidak perlu diubah.
#
# Mode ini SENGAJA dimatikan saat stdin bukan terminal - misalnya saat tes
# menyuapkan masukan lewat pipa. Tanpa penjagaan itu, seluruh tes UI yang
# mengandalkan input bernomor akan rusak.
# ---------------------------------------------------------------------------

try:
    import termios
    import tty
    import select as _select
except ImportError:                     # Windows atau terminal tanpa POSIX tty
    termios = None
    tty = None
    _select = None


def _bisa_panah(jumlah_baris):
    """Panah hanya dipakai bila aman: terminal asli, POSIX, dan layar cukup."""
    if os.environ.get("BELAJAR_MENU", "").strip().lower() in ("angka", "nomor"):
        return False
    if termios is None or tty is None or _select is None:
        return False
    try:
        if not (sys.stdin.isatty() and sys.stdout.isatty()):
            return False
    except (AttributeError, ValueError):
        return False
    try:
        tinggi = shutil.get_terminal_size((80, 24)).lines
    except OSError:
        return False
    # +3 untuk prompt, baris petunjuk, dan sisa napas
    return jumlah_baris + 3 <= tinggi


def _baca_tombol():
    """Baca satu tombol dalam mode mentah. Mengembalikan nama tombol/karakter."""
    fd = sys.stdin.fileno()
    lama = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        # os.read, BUKAN sys.stdin.read: sys.stdin memakai buffer sendiri,
        # sehingga byte lanjutan urutan panah bisa sudah tersedot ke buffer
        # dan select() salah melaporkan "tidak ada lanjutan". Akibatnya setiap
        # panah terbaca sebagai ESC polos dan menu langsung tertutup.
        c = os.read(fd, 1)
        if not c:
            return "eof"

        if c == b"\x1b":
            # Bisa ESC polos, bisa awalan urutan panah. Tunggu sebentar saja;
            # kalau tidak ada lanjutannya berarti memang ESC.
            siap, _, _ = _select.select([fd], [], [], 0.05)
            if not siap:
                return "esc"
            sisa = os.read(fd, 2)
            if sisa == b"[A":
                return "atas"
            if sisa == b"[B":
                return "bawah"
            return "abai"

        if c in (b"\r", b"\n"):
            return "pilih"
        if c == b"\x03":
            raise KeyboardInterrupt
        if c == b"\x04":
            return "eof"
        return c.decode("utf-8", "ignore")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, lama)


def _baris_menu(options, extra, allow_back, back_label, kursor, ketikan):
    """Susun seluruh baris menu. Dipotong selebar layar supaya tidak melipat -
    baris yang melipat merusak hitungan kursor saat digambar ulang."""
    maks = lebar()
    baris = []

    for i, opt in enumerate(options):
        nomor = f"{i + 1:>2}"
        if i == kursor:
            teks = potong(f" > {nomor}. {opt}", maks)
            baris.append(paint(teks, C.BOLD, C.CYAN))
        else:
            baris.append(paint(potong(f"   {nomor}. {opt}", maks), C.WHITE))

    for key, label in extra.items():
        baris.append(paint(potong(f"    {key}. {label}", maks), C.CYAN))

    if allow_back:
        baris.append(paint(potong(f"    0. {back_label}", maks), C.DIM))

    petunjuk = "   panah pindah  ENTER pilih  angka lompat"
    if allow_back:
        petunjuk += "  0/ESC kembali"
    if ketikan:
        petunjuk += f"   [{ketikan}]"
    baris.append(paint(potong(petunjuk, maks), C.DIM))

    return baris


def _ask_choice_panah(prompt, options, allow_back, back_label, extra):
    kursor = 0
    ketikan = ""

    print(prompt)
    baris = _baris_menu(options, extra, allow_back, back_label, kursor, ketikan)
    for b in baris:
        print(b)

    while True:
        try:
            tombol = _baca_tombol()
        except KeyboardInterrupt:
            print()
            return 0

        if tombol in ("eof", "esc"):
            return 0

        if tombol == "atas":
            kursor = (kursor - 1) % len(options)
            ketikan = ""
        elif tombol == "bawah":
            kursor = (kursor + 1) % len(options)
            ketikan = ""
        elif tombol == "pilih":
            print()
            return kursor + 1
        elif tombol == "0" and allow_back:
            print()
            return 0
        elif tombol.isascii() and tombol.isdigit():
            # Angka menggeser kursor, ENTER yang memilih - jadi urutan tombol
            # "5" lalu ENTER berperilaku sama persis seperti menu lama.
            calon = ketikan + tombol
            if angka_pilihan(calon, len(options)) is not None:
                ketikan = calon
            elif angka_pilihan(tombol, len(options)) is not None:
                ketikan = tombol
            else:
                ketikan = ""
            if ketikan:
                kursor = int(ketikan) - 1
        elif tombol.lower() in extra:
            print()
            return tombol.lower()
        else:
            ketikan = ""

        # Gambar ulang di tempat: naik setinggi blok, hapus tiap baris, cetak lagi.
        sys.stdout.write(f"\033[{len(baris)}A")
        baris = _baris_menu(options, extra, allow_back, back_label, kursor, ketikan)
        for b in baris:
            sys.stdout.write("\033[2K" + b + "\n")
        sys.stdout.flush()


def _ask_choice_angka(prompt, options, allow_back, back_label, extra):
    """Menu bernomor klasik. Dipakai saat panah tidak tersedia."""
    first_pass = True
    salah_berturut = 0

    while True:
        if first_pass:
            print(prompt)
            for i, opt in enumerate(options, start=1):
                print(paint(f"   {i:>2}. {opt}", C.WHITE))
            for key, label in extra.items():
                print(paint(f"    {key}. {label}", C.CYAN))
            if allow_back:
                print(paint(f"    0. {back_label}", C.DIM))
            first_pass = False

        raw = ask_atau_eof("  Pilih > ")
        if raw is None:
            return 0

        low = raw.lower()
        if allow_back and raw == "0":
            return 0
        if low in extra:
            return low

        nomor = angka_pilihan(raw, len(options))
        if nomor is not None:
            return nomor

        salah_berturut += 1
        if salah_berturut >= MAKS_SALAH_BERTURUT:
            print(paint("  Terlalu banyak masukan tidak valid, kembali.", C.YELLOW))
            return 0

        print(paint("  Pilihan tidak valid, coba lagi.", C.RED))
        first_pass = True


def ask_choice(prompt, options, allow_back=True, back_label="Kembali", extra=None):
    """Menu pilihan.

    Return: 0 kalau pilih "Kembali" / stdin habis, 1..n untuk opsi, atau string
    kunci dari `extra` (dict {huruf: label}) untuk aksi tambahan.

    Pemanggil dengan `allow_back=False` tetap bisa menerima 0: artinya "tidak
    ada masukan lagi, tutup layar ini". Menu utama memperlakukannya sebagai
    keluar.

    Di terminal sungguhan dipakai navigasi panah; selain itu jatuh ke menu
    bernomor. Kontrak nilai kembaliannya sama persis pada kedua mode.
    """
    extra = extra or {}
    if not options:
        return 0

    tinggi_blok = len(options) + len(extra) + (1 if allow_back else 0) + 1
    if _bisa_panah(tinggi_blok):
        try:
            return _ask_choice_panah(prompt, options, allow_back, back_label, extra)
        except (OSError, termios.error):
            # Terminal menolak mode mentah - lanjutkan dengan menu bernomor
            # daripada menjatuhkan aplikasi.
            pass

    return _ask_choice_angka(prompt, options, allow_back, back_label, extra)


def confirm(prompt, default=False):
    suffix = " [Y/n] " if default else " [y/N] "
    raw = ask_atau_eof("  " + prompt + suffix)
    if raw is None or not raw:
        return default
    return raw.lower().startswith("y")


# ---------------------------------------------------------------- paginasi

def paginate(title, lines, chunk_size=None):
    """Tampilkan `lines` per halaman.

    Return True kalau user membaca sampai habis, False kalau keluar lebih awal.
    Navigasi: ENTER/n = maju, p = mundur, a = ke awal, q = keluar.
    """
    total = len(lines)
    if total == 0:
        return True

    if chunk_size is None:
        chunk_size = tinggi_halaman(sisa=9)
    chunk_size = max(1, chunk_size)

    pages = [lines[i:i + chunk_size] for i in range(0, total, chunk_size)]
    idx = 0

    while True:
        clear()
        print(paint("  " + potong(title, lebar() - 4), C.BLUE, C.BOLD))
        print(paint("  " + "-" * (lebar() - 4), C.DIM))
        for line in pages[idx]:
            print(line)

        first = idx * chunk_size + 1
        last = min((idx + 1) * chunk_size, total)
        is_last = idx == len(pages) - 1

        if len(pages) > 1:
            print(paint(
                f"\n  Halaman {idx + 1}/{len(pages)}  (baris {first}-{last} dari {total})",
                C.DIM,
            ))
            print("  " + bar(idx + 1, len(pages), min(30, max(10, lebar() - 30))))

        if len(pages) == 1:
            nav = "[ENTER] selesai"
        elif idx == 0:
            nav = "[ENTER] lanjut | [q] keluar"
        elif is_last:
            nav = "[ENTER] selesai | [p] sebelumnya | [a] ke awal | [q] keluar"
        else:
            nav = "[ENTER] lanjut | [p] sebelumnya | [a] ke awal | [q] keluar"

        raw = ask_atau_eof(f"\n  {nav}  > ")
        if raw is None:
            return False
        choice = raw.lower()

        if choice == "q":
            return False
        if choice == "p":
            idx = max(0, idx - 1)
            continue
        if choice == "a":
            idx = 0
            continue
        if is_last:
            return True
        idx += 1


# --------------------------------------------------------------------- teks

def wrap(text, width=None, indent="  "):
    width = width if width is not None else lebar() - 2
    return textwrap.fill(text, width=width, initial_indent=indent,
                         subsequent_indent=indent)


def bungkus_baris(teks, width=None, indent="  "):
    """Seperti `wrap` tapi mengembalikan daftar baris dan menjaga baris kosong.

    Materi ditulis sebagai daftar baris siap tampil dengan indentasi manual
    yang bermakna (daftar bernomor, tabel ASCII). Membungkus paksa akan
    merusaknya, jadi baris yang sudah muat dibiarkan apa adanya.
    """
    width = width if width is not None else lebar() - 2
    if not teks.strip():
        return [""]
    if len(teks) + len(indent) <= width:
        return [indent + teks]

    # Pertahankan indentasi asli baris supaya sambungannya tetap sejajar.
    spasi_asli = len(teks) - len(teks.lstrip(" "))
    lanjutan = indent + " " * min(spasi_asli + 2, max(0, width - 20))
    return textwrap.wrap(
        teks, width=width, initial_indent=indent, subsequent_indent=lanjutan,
        break_long_words=False, break_on_hyphens=False,
    ) or [indent + teks]


def sorot_kata(teks, kata, peran="sorot"):
    """Tebalkan kemunculan `kata` di dalam teks (tanpa membedakan kapital)."""
    if not kata:
        return teks
    hasil = []
    sisa = teks
    rendah = kata.lower()
    while True:
        posisi = sisa.lower().find(rendah)
        if posisi < 0:
            hasil.append(sisa)
            break
        hasil.append(sisa[:posisi])
        hasil.append(tema.cat(sisa[posisi:posisi + len(kata)], peran, tema.TEBAL))
        sisa = sisa[posisi + len(kata):]
    return "".join(hasil)


def fmt_code(code):
    return paint(code, C.GREEN)


def fmt_comment(comment):
    return paint(comment, C.DIM)


def bar(done, total, width=20, fill_color=C.GREEN):
    """Progress bar teks: [##########----------] 50%"""
    if total <= 0:
        pct = 0.0
    else:
        pct = max(0.0, min(1.0, done / total))
    filled = int(round(pct * width))
    return paint("#" * filled, fill_color, C.BOLD) + paint("-" * (width - filled), C.DIM)
