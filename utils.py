"""Helper tampilan terminal: warna, banner, paginasi, dan input pilihan.

Modul ini sengaja hanya mengurus URUSAN TAMPILAN. Semua yang berkaitan
dengan penyimpanan progres belajar ada di `progress.py`.
"""

import os
import sys
import textwrap

WIDTH = 60


class C:
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
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    if not (hasattr(sys.stdout, "isatty") and sys.stdout.isatty()):
        return False
    if os.name == "nt":
        # Windows Terminal / ConEmu / ANSICON mendukung ANSI.
        return bool(
            os.environ.get("WT_SESSION")
            or os.environ.get("ANSICON")
            or os.environ.get("ConEmuANSI") == "ON"
            or sys.getwindowsversion().major >= 10  # type: ignore[attr-defined]
        )
    return os.environ.get("TERM", "") != "dumb"


COLORS_ON = supports_color()


def paint(text, *colors):
    """Bungkus teks dengan kode warna ANSI (no-op kalau warna dimatikan)."""
    if not COLORS_ON or not colors:
        return text
    return f"{''.join(colors)}{text}{C.RESET}"


def strip_ansi(text):
    """Buang kode warna dari string. Berguna untuk menghitung lebar & mencari teks."""
    out = []
    i = 0
    while i < len(text):
        if text[i] == "\033":
            j = text.find("m", i)
            if j == -1:
                break
            i = j + 1
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def visible_len(text):
    return len(strip_ansi(text))


def rule(char="=", color=C.CYAN, bold=True):
    styles = [color, C.BOLD] if bold else [color]
    return paint(char * WIDTH, *styles)


def banner(title, subtitle=""):
    print("\n" + rule())
    print(paint(title.center(WIDTH), C.YELLOW, C.BOLD))
    if subtitle:
        print(paint(subtitle.center(WIDTH), C.DIM))
    print(rule() + "\n")


def header(title, subtitle=""):
    """Banner tanpa baris kosong pembuka. Dipakai tepat setelah clear()."""
    print(rule())
    print(paint(title.center(WIDTH), C.YELLOW, C.BOLD))
    if subtitle:
        print(paint(subtitle.center(WIDTH), C.DIM))
    print(rule())


def press_enter(msg="Tekan ENTER untuk lanjut..."):
    try:
        input(paint("\n  " + msg, C.DIM))
    except EOFError:
        print()


def clear():
    """Bersihkan layar. Aman dipanggil walau output bukan terminal."""
    if not COLORS_ON:
        print("\n" * 2)
        return
    os.system("cls" if os.name == "nt" else "clear")


def ask(prompt, default=""):
    """input() yang tidak meledak saat stdin habis (mis. dijalankan via pipe)."""
    try:
        return input(paint(prompt, C.CYAN)).strip()
    except EOFError:
        print()
        return default


def ask_timed(prompt, detik):
    """input() dengan batas waktu. Return (jawaban, kehabisan_waktu).

    Di POSIX pakai select() supaya benar-benar berhenti saat waktu habis.
    Di platform lain waktu dihitung setelah user menekan ENTER.
    """
    import time

    if detik <= 0:
        return ask(prompt), False

    try:
        import select
        import sys as _sys

        if not (hasattr(_sys.stdin, "fileno") and os.name != "nt"):
            raise ImportError

        print(paint(prompt, C.CYAN), end="", flush=True)
        siap, _, _ = select.select([_sys.stdin], [], [], detik)
        if not siap:
            print(paint("\n  Waktu habis!", C.RED, C.BOLD))
            return "", True
        return _sys.stdin.readline().strip(), False
    except (ImportError, OSError, ValueError):
        mulai = time.monotonic()
        jawab = ask(prompt)
        return jawab, (time.monotonic() - mulai) > detik


def paginate(title, lines, chunk_size=22):
    """Tampilkan `lines` per halaman.

    Return True kalau user membaca sampai habis, False kalau keluar lebih awal.
    Navigasi: ENTER/n = maju, p = mundur, q = keluar.
    """
    total = len(lines)
    if total == 0:
        return True

    pages = [lines[i:i + chunk_size] for i in range(0, total, chunk_size)]
    idx = 0

    while True:
        clear()
        print(paint(f"  {title}", C.BLUE, C.BOLD))
        print(paint("  " + "-" * (WIDTH - 4), C.DIM))
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

        if len(pages) == 1:
            nav = "[ENTER] selesai"
        elif idx == 0:
            nav = "[ENTER] lanjut | [q] keluar"
        elif is_last:
            nav = "[ENTER] selesai | [p] sebelumnya | [q] keluar"
        else:
            nav = "[ENTER] lanjut | [p] sebelumnya | [q] keluar"

        choice = ask(f"\n  {nav}  > ", "q").lower()

        if choice == "q":
            return False
        if choice == "p":
            idx = max(0, idx - 1)
            continue
        if is_last:
            return True
        idx += 1


def ask_choice(prompt, options, allow_back=True, back_label="Kembali", extra=None):
    """Menu bernomor.

    Return: 0 kalau pilih "Kembali", 1..n untuk opsi, atau string kunci dari
    `extra` (dict {huruf: label}) untuk aksi tambahan seperti 'c' = cari.
    """
    extra = extra or {}
    first_pass = True
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

        raw = ask("  Pilih > ", "0")
        low = raw.lower()

        if allow_back and raw == "0":
            return 0
        if low in extra:
            return low
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw)

        print(paint("  Pilihan tidak valid, coba lagi.", C.RED))
        first_pass = True


def confirm(prompt, default=False):
    suffix = " [Y/n] " if default else " [y/N] "
    raw = ask("  " + prompt + suffix, "").lower()
    if not raw:
        return default
    return raw.startswith("y")


def wrap(text, width=WIDTH - 2, indent="  "):
    return textwrap.fill(text, width=width, initial_indent=indent, subsequent_indent=indent)


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
