"""Membandingkan output harapan vs output pelajar, lalu MENJELASKAN bedanya.

Sebelum ini, latihan yang gagal cuma menampilkan dua blok teks berdampingan dan
menyerahkan pekerjaan mencarinya ke pelajar. Untuk beda satu spasi atau satu
huruf kapital, itu bisa memakan waktu berpuluh menit dan berakhir menyerah.

Modul ini melakukan tiga hal:

1. Menyejajarkan baris (difflib) supaya terlihat baris mana yang kurang,
   berlebih, atau berubah.
2. Menunjuk KOLOM pertama yang berbeda dengan penanda ^ di bawahnya.
3. Menebak PENYEBABNYA dalam bahasa manusia -- beda kapital saja, beda jumlah
   spasi saja, ikut mencetak teks prompt, urutan tertukar, angka sudah benar
   tapi tulisannya beda, dan seterusnya.

Semua murni tebakan heuristik; kalau tidak ada yang cocok, modul ini diam
alih-alih mengarang.
"""

import difflib
import re

from inti import tema

# Karakter pengganti untuk hal yang tak terlihat, dipakai saat sebuah baris
# terlihat identik padahal tidak.
SPASI_TAMPAK = "·"      # ·
TAB_TAMPAK = "→"        # →


class Beda:
    """Hasil perbandingan satu output harapan dengan satu output nyata."""

    __slots__ = ("sama", "harapan", "aktual", "baris", "nomor_beda",
                 "kolom_beda", "catatan")

    def __init__(self, sama, harapan, aktual, baris, nomor_beda, kolom_beda, catatan):
        self.sama = sama
        self.harapan = harapan
        self.aktual = aktual
        self.baris = baris              # [(tanda, teks_harapan, teks_aktual)]
        self.nomor_beda = nomor_beda    # nomor baris 1-basis, None kalau sama
        self.kolom_beda = kolom_beda    # kolom 1-basis pada baris itu
        self.catatan = catatan          # list[str] diagnosis berbahasa manusia


# ------------------------------------------------------------------ bantuan

def _baris(teks):
    """Pecah jadi baris, samakan akhiran, buang baris kosong di ujung.

    Harus sepadan dengan `runner.normalisasi`: kalau modul ini menganggap dua
    output berbeda padahal auto-checker menganggapnya sama, pelajar akan
    melihat "GAGAL" berdampingan dengan diff yang bilang "sudah sama".
    """
    teks = (teks or "").replace("\r\n", "\n").replace("\r", "\n")
    baris = [b.rstrip() for b in teks.split("\n")]
    while baris and not baris[-1]:
        baris.pop()
    while baris and not baris[0]:
        baris.pop(0)
    return baris


def _rapatkan(s):
    return re.sub(r"\s+", " ", s).strip()


def _angka(s):
    return re.findall(r"-?\d+(?:[.,]\d+)?", s)


def kolom_pertama_beda(a, b):
    """Kolom 1-basis pertama yang berbeda antara dua baris. None kalau sama."""
    batas = min(len(a), len(b))
    for i in range(batas):
        if a[i] != b[i]:
            return i + 1
    if len(a) != len(b):
        return batas + 1
    return None


def tampakkan(teks):
    """Ganti spasi & tab jadi karakter kasatmata.

    Hanya dipakai kalau dua baris terlihat sama tapi sebenarnya beda, supaya
    pelajar bisa melihat spasi ganda atau tab yang tersembunyi.
    """
    return teks.replace("\t", TAB_TAMPAK).replace(" ", SPASI_TAMPAK)


# ------------------------------------------------------------------ diagnosa

def _diagnosa(h, a):
    """Tebak kenapa output berbeda. Return daftar kalimat penjelas."""
    catatan = []

    if not a:
        catatan.append("Programmu tidak mencetak apa pun. Sudah pakai perintah cetak?")
        return catatan

    if h == a:
        return catatan

    gabung_h = "\n".join(h)
    gabung_a = "\n".join(a)

    if gabung_h.lower() == gabung_a.lower():
        catatan.append("Isinya sudah benar, hanya beda HURUF BESAR/KECIL.")
        return catatan

    if _rapatkan(gabung_h) == _rapatkan(gabung_a):
        catatan.append("Isinya sudah benar, hanya beda JUMLAH SPASI atau indentasi.")
        return catatan

    if _rapatkan(gabung_h).lower() == _rapatkan(gabung_a).lower():
        catatan.append("Isinya sudah benar, hanya beda spasi dan huruf besar/kecil.")
        return catatan

    if sorted(h) == sorted(a) and h != a:
        catatan.append("Semua barisnya benar, tapi URUTANNYA tertukar.")
        return catatan

    if len(a) > len(h) and all(b in a for b in h):
        catatan.append(f"Semua baris yang diminta sudah ada, tapi ada {len(a) - len(h)} "
                       "baris TAMBAHAN yang tidak diminta.")

    hilang = [b for b in h if b not in a]
    if hilang and len(hilang) < len(h):
        catatan.append(f"{len(hilang)} baris belum tercetak, mulai dari: {hilang[0][:48]!r}")

    # Pelajar mencetak teks ajakan sebelum jawabannya.
    for bh, ba in zip(h, a):
        if bh and ba.endswith(bh) and len(ba) > len(bh):
            awalan = ba[: len(ba) - len(bh)]
            if awalan.strip():
                catatan.append(
                    f"Sepertinya kamu ikut mencetak teks ajakan {awalan.strip()[:32]!r} "
                    "sebelum jawabannya. Latihan ini dinilai dari output, jadi jangan "
                    "cetak prompt apa pun."
                )
                break

    if _angka(gabung_h) and _angka(gabung_h) == _angka(gabung_a):
        catatan.append("Semua ANGKANYA sudah benar; yang beda cuma teks di sekitarnya.")
    else:
        rapi_h = [x.replace(",", ".").rstrip("0").rstrip(".") for x in _angka(gabung_h)]
        rapi_a = [x.replace(",", ".").rstrip("0").rstrip(".") for x in _angka(gabung_a)]
        if rapi_h and rapi_h == rapi_a:
            catatan.append("Nilainya sudah benar, yang beda FORMAT desimalnya "
                           "(misal 3 vs 3.0). Perhatikan tipe data pembagiannya.")

    if not catatan:
        tanpa_baca_h = [re.sub(r"[.!?,;:]+$", "", b) for b in h]
        tanpa_baca_a = [re.sub(r"[.!?,;:]+$", "", b) for b in a]
        if tanpa_baca_h == tanpa_baca_a:
            catatan.append("Hanya beda TANDA BACA di akhir baris.")
        elif [b.lower() for b in tanpa_baca_h] == [b.lower() for b in tanpa_baca_a]:
            catatan.append("Isinya sudah benar, yang beda cuma huruf besar/kecil "
                           "dan tanda baca di akhir baris.")

    if not catatan:
        if len(a) < len(h):
            catatan.append(f"Outputmu {len(h) - len(a)} baris lebih pendek dari yang diminta.")
        elif len(a) > len(h):
            catatan.append(f"Outputmu {len(a) - len(h)} baris lebih panjang dari yang diminta.")

    return catatan


# ---------------------------------------------------------------- pembanding

def bandingkan(harapan, aktual):
    """Sejajarkan dua output dan jelaskan bedanya. Selalu return objek Beda."""
    h = _baris(harapan)
    a = _baris(aktual)

    baris = []
    nomor_beda = None
    kolom_beda = None
    nomor = 0

    cocokan = difflib.SequenceMatcher(a=h, b=a, autojunk=False)
    for tag, h1, h2, a1, a2 in cocokan.get_opcodes():
        if tag == "equal":
            for offset in range(h2 - h1):
                nomor += 1
                baris.append(("=", h[h1 + offset], a[a1 + offset]))
        elif tag == "replace":
            # Sejajarkan berpasangan supaya kolom bedanya bisa ditunjuk.
            panjang = max(h2 - h1, a2 - a1)
            for offset in range(panjang):
                nomor += 1
                bh = h[h1 + offset] if h1 + offset < h2 else None
                ba = a[a1 + offset] if a1 + offset < a2 else None
                if bh is not None and ba is not None:
                    baris.append(("~", bh, ba))
                    if nomor_beda is None:
                        nomor_beda = nomor
                        kolom_beda = kolom_pertama_beda(bh, ba)
                elif bh is not None:
                    baris.append(("-", bh, None))
                    if nomor_beda is None:
                        nomor_beda, kolom_beda = nomor, None
                else:
                    baris.append(("+", None, ba))
                    if nomor_beda is None:
                        nomor_beda, kolom_beda = nomor, None
        elif tag == "delete":
            for offset in range(h2 - h1):
                nomor += 1
                baris.append(("-", h[h1 + offset], None))
                if nomor_beda is None:
                    nomor_beda, kolom_beda = nomor, None
        elif tag == "insert":
            for offset in range(a2 - a1):
                nomor += 1
                baris.append(("+", None, a[a1 + offset]))
                if nomor_beda is None:
                    nomor_beda, kolom_beda = nomor, None

    sama = h == a
    return Beda(sama, h, a, baris, nomor_beda, kolom_beda, _diagnosa(h, a))


# ------------------------------------------------------------------ tampilan

def _potong(teks, lebar):
    if lebar <= 4 or len(teks) <= lebar:
        return teks
    return teks[: lebar - 1] + "…"


def render(beda, lebar=76, maks_baris=14):
    """Ubah objek Beda jadi baris siap cetak (sudah berwarna).

    Format:
          1 | Halo, namaku Andi!             baris yang sudah benar
          2 - Aku sedang belajar Python.     yang diharapkan
          2 + aku sedang belajar python.     yang kamu cetak
              ^ beda mulai kolom 1
    """
    keluar = []
    if beda.sama:
        keluar.append(tema.cat("  Output sudah sama persis.", "sukses"))
        return keluar

    lebar_isi = max(20, lebar - 24)
    ditampilkan = 0

    for nomor, (tanda, bh, ba) in enumerate(beda.baris, start=1):
        if ditampilkan >= maks_baris:
            sisa = len(beda.baris) - nomor + 1
            keluar.append(tema.cat(f"      ... {sisa} baris lagi tidak ditampilkan", "redup"))
            break

        if tanda == "=":
            keluar.append(
                tema.cat(f"  {nomor:>3} │ ", "redup")
                + tema.cat(_potong(bh, lebar_isi), "beda_sama")
            )
            ditampilkan += 1
            continue

        # Kalau dua baris hanya berbeda pada spasi, mata tidak akan menemukan
        # bedanya. Buat spasinya kelihatan.
        tampil_h, tampil_a = bh, ba
        if (bh is not None and ba is not None
                and re.sub(r"\s+", "", bh) == re.sub(r"\s+", "", ba)):
            tampil_h, tampil_a = tampakkan(bh), tampakkan(ba)

        if tanda in ("-", "~"):
            keluar.append(
                tema.cat(f"  {nomor:>3} - ", "beda_kurang")
                + tema.cat(_potong(tampil_h, lebar_isi), "beda_kurang")
                + tema.cat("   (diharapkan)", "redup")
            )
            ditampilkan += 1
        if tanda in ("+", "~"):
            keluar.append(
                tema.cat(f"  {nomor:>3} + ", "beda_tambah")
                + tema.cat(_potong(tampil_a, lebar_isi), "beda_tambah")
                + tema.cat("   (punyamu)", "redup")
            )
            ditampilkan += 1

        # Penunjuk kolom, hanya untuk baris pertama yang berbeda.
        if tanda == "~" and nomor == beda.nomor_beda and beda.kolom_beda:
            kolom = beda.kolom_beda
            if kolom <= lebar_isi:
                keluar.append(
                    " " * (8 + kolom - 1)
                    + tema.cat("^", "peringatan", tema.TEBAL)
                    + tema.cat(f" beda mulai kolom {kolom}", "peringatan")
                )

    if beda.catatan:
        keluar.append("")
        for c in beda.catatan:
            keluar.append(tema.cat("  → " + c, "peringatan"))

    return keluar


def ringkas(beda):
    """Satu kalimat rangkuman, untuk daftar hasil uji."""
    if beda.sama:
        return "output sama persis"
    if beda.catatan:
        return beda.catatan[0]
    if beda.nomor_beda:
        kolom = f" kolom {beda.kolom_beda}" if beda.kolom_beda else ""
        return f"beda mulai baris {beda.nomor_beda}{kolom}"
    return "output berbeda"
