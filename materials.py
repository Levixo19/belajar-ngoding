"""Tampilan materi: baca, tandai, bookmark, dan cari di dalam satu bahasa.

Dua perubahan perilaku yang disengaja:

* **Materi baru dihitung "dibaca" kalau benar-benar dibaca sampai habis.**
  Dulu XP dan tanda [v] diberikan sebelum halaman pertama muncul, jadi membuka
  lalu langsung menekan [q] tetap menaikkan progres. Sekarang berhenti di
  tengah dicatat sebagai [~] "dibaca sebagian", tanpa XP.
* **Paragraf dibungkus mengikuti lebar terminal** dan contoh kode disorot per
  token, bukan dicetak satu warna hijau datar.

Importir: main.py, navigasi.py, tests/test_data.py (memakai `teks_polos`).
"""

import sorot
import tema
from utils import (
    C, paint, clear, paginate, ask, ask_atau_eof, ask_choice, header, rule,
    lebar, bungkus_baris, sorot_kata, tinggi_halaman,
)
from progress import (
    record_material_read, load_progress, kunci, toggle_bookmark, is_bookmarked,
)

try:
    import konfigurasi
except ImportError:
    konfigurasi = None


def _bahasa_dari_kategori(kategori):
    """'java_materi' -> 'java'. Dipakai untuk memilih aturan penyorot."""
    return kategori.rsplit("_", 1)[0] if "_" in kategori else ""


def baris_materi(topic, bahasa="", kata_sorot=""):
    """Ubah satu topik jadi daftar baris siap tampil."""
    lbr = lebar()
    sorot_nyala = konfigurasi is None or konfigurasi.ambil("sorot_sintaks", True)
    lines = []

    for i, section in enumerate(topic["sections"]):
        if i > 0:
            lines.append("")
        if section.get("heading"):
            lines.append(tema.cat("  ### " + section["heading"], "subjudul", tema.TEBAL))

        for paragraph in section.get("body") or []:
            for baris in bungkus_baris(paragraph, lbr - 2, "  "):
                if kata_sorot:
                    baris = sorot_kata(baris, kata_sorot)
                lines.append(baris)

        if section.get("code"):
            lines.append(tema.cat("  " + "─" * (lbr - 6), "redup"))
            if sorot_nyala and bahasa:
                lines.extend(sorot.sorot_baris(section["code"], bahasa, awalan="  "))
            else:
                for cl in section["code"].splitlines():
                    lines.append(tema.cat("  " + cl, "kode_string"))
            lines.append(tema.cat("  " + "─" * (lbr - 6), "redup"))

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


def render_material(topic, kategori="materi", kata_sorot="", daftar=None):
    """Tampilkan satu materi. `daftar` (opsional) memungkinkan lompat ke berikutnya."""
    bahasa = _bahasa_dari_kategori(kategori)
    tuntas = paginate(topic["title"],
                      baris_materi(topic, bahasa, kata_sorot),
                      chunk_size=tinggi_halaman(sisa=9))
    # Dicatat SESUDAH dibaca: berhenti di tengah tidak boleh dihitung selesai.
    record_material_read(kategori, topic["title"], tuntas=tuntas)

    berikut = None
    if daftar:
        try:
            posisi = daftar.index(topic)
            if posisi + 1 < len(daftar):
                berikut = daftar[posisi + 1]
        except ValueError:
            berikut = None

    while True:
        clear()
        header(topic["title"], "selesai dibaca" if tuntas else "dihentikan di tengah")
        ditandai = is_bookmarked(kategori, topic["title"])
        print(tema.cat("  Status bookmark: "
                       + ("TERSIMPAN" if ditandai else "belum disimpan"),
                       "judul" if ditandai else "redup"))
        if not tuntas:
            print(tema.cat("  Materi ini ditandai [~] dibaca sebagian. "
                           "Baca sampai habis untuk mendapat XP.", "peringatan"))
        print()
        print(tema.cat("  [b] " + ("Hapus bookmark" if ditandai else "Simpan ke bookmark"),
                       "aksen"))
        print(tema.cat("  [u] Baca ulang materi ini", "aksen"))
        if berikut:
            print(tema.cat(f"  [n] Lanjut ke materi berikutnya: {berikut['title'][:38]}",
                           "sukses"))
        print(tema.cat("  [0] Kembali ke daftar", "redup"))

        pilih = ask_atau_eof("  Pilih > ")
        if pilih is None:
            return
        pilih = pilih.lower()
        if pilih == "b":
            toggle_bookmark(kategori, topic["title"])
        elif pilih == "u":
            tuntas = paginate(topic["title"], baris_materi(topic, bahasa, kata_sorot),
                              chunk_size=tinggi_halaman(sisa=9))
            record_material_read(kategori, topic["title"], tuntas=tuntas)
        elif pilih == "n" and berikut:
            render_material(berikut, kategori, kata_sorot, daftar)
            return
        else:
            return


def _label(topic, kategori, data):
    k = kunci(kategori, topic["title"])
    if k in data["materi_dibaca"]:
        tanda = tema.cat("[v]", "sukses", tema.TEBAL)
    elif k in data["materi_sebagian"]:
        tanda = tema.cat("[~]", "peringatan")
    else:
        tanda = tema.cat("[ ]", "redup")
    bintang = tema.cat(" *", "judul", tema.TEBAL) if k in data["bookmark"] else ""
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
        print(tema.cat(f"  Tidak ada materi yang memuat '{kata}'.", "galat"))
        ask("  Tekan ENTER untuk kembali...", "")
        return

    while True:
        clear()
        header("HASIL PENCARIAN", f"{title} - '{kata}' - {len(cocok)} materi")
        names = [f"{m['title']}  ({n}x)" for m, n in cocok]
        pilih = ask_choice(paint("  Pilih materi:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        render_material(cocok[pilih - 1][0], kategori, kata_sorot=kata, daftar=materials)


def materials_menu(title, materials, kategori="materi"):
    while True:
        clear()
        header("MATERI: " + title)

        data = load_progress()
        dibaca = sum(1 for m in materials
                     if kunci(kategori, m["title"]) in data["materi_dibaca"])
        sebagian = sum(1 for m in materials
                       if kunci(kategori, m["title"]) in data["materi_sebagian"])
        ringkasan = f"  Sudah dibaca {dibaca}/{len(materials)} materi"
        if sebagian:
            ringkasan += f"  ({sebagian} dibaca sebagian)"
        print(tema.cat(ringkasan, "teks"))
        print(tema.cat("  [v] selesai   [~] sebagian   * di-bookmark", "redup"))
        print(rule("-", C.DIM, bold=False))

        names = [_label(m, kategori, data) for m in materials]
        extra = {"c": "Cari kata kunci di materi ini"}
        # Loncat ke materi pertama yang belum tuntas: jalan pintas paling sering
        # dipakai orang yang belajar berurutan.
        belum = next((i for i, m in enumerate(materials, start=1)
                      if kunci(kategori, m["title"]) not in data["materi_dibaca"]), None)
        if belum:
            extra["l"] = f"Lanjutkan: {materials[belum - 1]['title'][:40]}"

        pilih = ask_choice(paint("  Pilih materi:", C.BLUE, C.BOLD), names, extra=extra)

        if pilih == 0:
            return
        if pilih == "c":
            _cari_lokal(title, materials, kategori)
            continue
        if pilih == "l" and belum:
            render_material(materials[belum - 1], kategori, daftar=materials)
            continue
        if isinstance(pilih, int):
            render_material(materials[pilih - 1], kategori, daftar=materials)
