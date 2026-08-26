"""Tampilan materi: baca, tandai, bookmark, dan cari di dalam satu bahasa."""

from utils import (
    C, paint, clear, paginate, ask, ask_choice, header, rule, WIDTH,
)
from progress import (
    record_material_read, load_progress, kunci, toggle_bookmark, is_bookmarked,
)


def baris_materi(topic):
    """Ubah satu topik jadi daftar baris siap tampil."""
    lines = []
    for i, section in enumerate(topic["sections"]):
        if i > 0:
            lines.append("")
        if section.get("heading"):
            lines.append(paint("  ### " + section["heading"], C.MAGENTA, C.BOLD))
        for paragraph in section.get("body") or []:
            lines.append("  " + paragraph)
        if section.get("code"):
            lines.append(paint("  " + "-" * (WIDTH - 6), C.DIM))
            for cl in section["code"].splitlines():
                lines.append(paint("  " + cl, C.GREEN))
            lines.append(paint("  " + "-" * (WIDTH - 6), C.DIM))
    return lines


def teks_polos(topic):
    """Seluruh isi materi sebagai teks biasa. Dipakai fitur pencarian."""
    bagian = [topic["title"]]
    for section in topic["sections"]:
        if section.get("heading"):
            bagian.append(section["heading"])
        bagian.extend(section.get("body") or [])
        if section.get("code"):
            bagian.append(section["code"])
    return "\n".join(bagian)


def render_material(topic, kategori="materi"):
    record_material_read(kategori, topic["title"])
    tuntas = paginate(topic["title"], baris_materi(topic), chunk_size=22)

    while True:
        clear()
        header(topic["title"], "selesai dibaca" if tuntas else "dihentikan di tengah")
        ditandai = is_bookmarked(kategori, topic["title"])
        print(paint(
            "  Status bookmark: " + ("TERSIMPAN" if ditandai else "belum disimpan"),
            C.YELLOW if ditandai else C.DIM,
        ))
        print()
        print(paint("  [b] " + ("Hapus bookmark" if ditandai else "Simpan ke bookmark"), C.CYAN))
        print(paint("  [u] Baca ulang materi ini", C.CYAN))
        print(paint("  [0] Kembali ke daftar", C.DIM))

        pilih = ask("  Pilih > ", "0").lower()
        if pilih == "b":
            toggle_bookmark(kategori, topic["title"])
        elif pilih == "u":
            tuntas = paginate(topic["title"], baris_materi(topic), chunk_size=22)
        else:
            return


def _label(topic, kategori, data):
    sudah = kunci(kategori, topic["title"]) in data["materi_dibaca"]
    ditandai = kunci(kategori, topic["title"]) in data["bookmark"]
    tanda = paint("[v]", C.GREEN, C.BOLD) if sudah else paint("[ ]", C.DIM)
    bintang = paint(" *", C.YELLOW, C.BOLD) if ditandai else ""
    return f"{tanda} {topic['title']}{bintang}"


def _cari_lokal(title, materials, kategori):
    """Cari kata kunci di dalam materi bahasa yang sedang dibuka."""
    kata = ask("  Kata kunci > ", "").strip()
    if not kata:
        return
    kunci_cari = kata.lower()

    cocok = []
    for m in materials:
        isi = teks_polos(m).lower()
        if kunci_cari in isi:
            cocok.append((m, isi.count(kunci_cari)))
    cocok.sort(key=lambda x: -x[1])

    if not cocok:
        print(paint(f"  Tidak ada materi yang memuat '{kata}'.", C.RED))
        ask("  Tekan ENTER untuk kembali...", "")
        return

    while True:
        clear()
        header("HASIL PENCARIAN", f"'{kata}' - {len(cocok)} materi")
        names = [f"{m['title']}  ({n}x)" for m, n in cocok]
        pilih = ask_choice(paint("  Pilih materi:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        render_material(cocok[pilih - 1][0], kategori)


def materials_menu(title, materials, kategori="materi"):
    while True:
        clear()
        header("MATERI: " + title)

        data = load_progress()
        dibaca = sum(1 for m in materials if kunci(kategori, m["title"]) in data["materi_dibaca"])
        print(paint(f"  Sudah dibaca {dibaca}/{len(materials)} materi", C.WHITE))
        print(paint("  [v] sudah dibaca   * di-bookmark", C.DIM))
        print(rule("-", C.DIM, bold=False))

        names = [_label(m, kategori, data) for m in materials]
        pilih = ask_choice(
            paint("  Pilih materi:", C.BLUE, C.BOLD),
            names,
            extra={"c": "Cari kata kunci di materi ini"},
        )

        if pilih == 0:
            return
        if pilih == "c":
            _cari_lokal(title, materials, kategori)
            continue
        render_material(materials[pilih - 1], kategori)
