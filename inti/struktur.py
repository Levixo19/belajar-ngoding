#!/usr/bin/env python3
"""Membaca struktur HTML dan CSS, lalu mencetaknya sebagai pohon.

HTML dan CSS tidak "dijalankan" seperti Python atau Java — tidak ada yang
dieksekusi, tidak ada yang dicetak. Padahal seluruh mesin penilaian di aplikasi
ini bekerja dengan membandingkan KELUARAN: `runner.periksa` menjalankan solusi
contoh, menyimpan outputnya sebagai kunci jawaban, lalu mengadu output pelajar
dengannya. Tanpa keluaran, kedua bahasa itu tidak bisa dinilai sama sekali dan
harus ditandai `auto_check: False` — dan latihan yang tidak dinilai adalah
latihan yang paling gampang dilewati begitu saja.

Modul ini menutup celah itu dengan menjadikan STRUKTUR sebagai keluarannya.
Berkas HTML dibaca jadi pohon elemen; berkas CSS jadi daftar aturan yang
dinormalisasi. Keduanya deterministik: masukan yang sama selalu menghasilkan
keluaran yang sama persis, sampai ke spasinya. Itu syarat mutlak — auto-checker
menurunkan kunci jawaban dengan menjalankan solusi contoh, dan apa pun yang
berubah antar-jalan membuat latihannya mustahil lulus (lihat AGENTS.md).

Ada alasan kedua yang sama pentingnya, dan ini soal belajar, bukan soal teknis.
Pemula yang salah menulis HTML tidak mendapat pesan error dari siapa pun:
browser diam-diam memperbaiki tag yang lupa ditutup, menebak maksudnya, dan
tetap menampilkan sesuatu. Halaman terlihat "hampir benar" dan tidak ada yang
memberi tahu di mana salahnya. Pohon di sini menunjukkan apa yang SEBENARNYA
terbaca dari markup itu — termasuk saat sebuah <p> ternyata tertelan masuk ke
dalam <div> karena tag penutupnya hilang.

Hanya stdlib: `html.parser` sudah ada di Python, dan CSS-nya dipindai tangan.
Tidak ada satu pun paket yang perlu dipasang, jadi HTML dan CSS adalah dua
bahasa yang latihannya bisa dinilai di komputer mana pun — bahkan yang tidak
punya satu compiler pun.

Dipakai `inti/runner.py` lewat subprocess. Untuk memeriksa dengan tangan,
dijalankan dari akar proyek:

    python3 inti/struktur.py html berkas.html
    python3 inti/struktur.py css  berkas.css

Kode keluarnya 2 kalau argumennya salah atau berkasnya tidak terbaca, dan 0
untuk segala hal lain -- TERMASUK markup yang tag penutupnya lupa. Itu bukan
kelalaian melainkan aturan: browser pun tidak menyatakan halaman gagal karena
sebuah tag tidak ditutup, dan pelajar justru perlu melihat pohonnya untuk
mengerti apa yang terjadi pada markup-nya. Keluhannya lewat stderr.
"""

import html.parser
import re
import sys

# Elemen yang memang tidak punya tag penutup. Menuntutnya ditutup adalah
# kesalahan yang sering dilakukan pemeriksa buatan sendiri, dan menyalahkan
# pelajar untuk sesuatu yang justru benar adalah cara tercepat membuat orang
# berhenti percaya pada umpan balik.
KOSONG = frozenset("""
    area base br col embed hr img input link meta param source track wbr
""".split())

# Tag yang boleh ditutup sendiri oleh HTML tanpa tag penutup eksplisit ketika
# saudara sejenis atau induknya berakhir. Daftar ini sengaja pendek: hanya yang
# benar-benar sering muncul di kurikulum pemula.
TUTUP_SENDIRI = {
    "li": {"li"},
    "p": {"p", "div", "section", "article", "ul", "ol", "h1", "h2", "h3",
          "h4", "h5", "h6", "table", "form", "footer", "header", "main",
          "nav", "aside", "blockquote", "pre", "hr"},
    "td": {"td", "th", "tr"},
    "th": {"td", "th", "tr"},
    "tr": {"tr"},
    "dt": {"dt", "dd"},
    "dd": {"dt", "dd"},
    "option": {"option"},
}

# Elemen yang tag penutupnya memang boleh dihilangkan ketika induknya
# berakhir. `<li>` di dalam `<ul>` yang tidak ditutup BUKAN kesalahan — HTML
# menutupnya sendiri, dan melaporkannya sebagai masalah berarti menyalahkan
# pelajar untuk sesuatu yang justru benar.
BOLEH_TERBUKA = frozenset("""
    li p td th tr dt dd option thead tbody tfoot colgroup
    html head body
""".split())

INDENT = "  "
MAKS_TEKS = 60


def _rapikan(teks):
    """Padatkan spasi jadi satu, buang di ujung. Dua berkas HTML yang cuma
    berbeda indentasinya harus menghasilkan pohon yang sama persis."""
    return re.sub(r"\s+", " ", teks).strip()


def _potong(teks, maks=MAKS_TEKS):
    return teks if len(teks) <= maks else teks[:maks - 1] + "…"


class _Pembaca(html.parser.HTMLParser):
    """Membangun pohon elemen sambil mencatat apa yang janggal.

    convert_charrefs dibiarkan True (bawaan): pelajar menulis &amp; dan &nbsp;,
    dan yang ingin dilihatnya di pohon adalah karakter jadinya, bukan kode
    entitasnya.
    """

    def __init__(self):
        super().__init__()
        self.akar = []
        self.tumpukan = []
        self.masalah = []
        self.doctype = ""

    # ------------------------------------------------------------- bantu

    def _wadah(self):
        return self.tumpukan[-1]["anak"] if self.tumpukan else self.akar

    def _tutup_implisit(self, tag):
        """Tutup elemen yang menurut HTML memang berakhir sendiri di sini."""
        while self.tumpukan:
            atas = self.tumpukan[-1]["tag"]
            if tag in TUTUP_SENDIRI.get(atas, ()):
                self.tumpukan.pop()
            else:
                break

    # ---------------------------------------------------------- peristiwa

    def handle_decl(self, decl):
        self.doctype = "<!" + _rapikan(decl).lower() + ">"

    def handle_starttag(self, tag, attrs):
        self._tutup_implisit(tag)
        simpul = {
            "tag": tag,
            # Atribut DIURUTKAN. Urutan penulisan atribut tidak punya arti apa
            # pun di HTML, jadi membiarkannya memengaruhi hasil berarti
            # menggagalkan pelajar untuk sesuatu yang bukan kesalahan.
            "atribut": sorted((n, v if v is not None else "") for n, v in attrs),
            "anak": [],
            "teks": [],
            "baris": self.getpos()[0],
        }
        self._wadah().append(simpul)
        if tag not in KOSONG:
            self.tumpukan.append(simpul)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.tumpukan and self.tumpukan[-1]["tag"] == tag:
            self.tumpukan.pop()

    def handle_endtag(self, tag):
        if tag in KOSONG:
            self.masalah.append(
                f"baris {self.getpos()[0]}: </{tag}> tidak diperlukan: "
                f"<{tag}> memang tidak punya tag penutup")
            return
        for i in range(len(self.tumpukan) - 1, -1, -1):
            if self.tumpukan[i]["tag"] == tag:
                for hilang in self.tumpukan[i + 1:]:
                    if hilang["tag"] in BOLEH_TERBUKA:
                        continue
                    self.masalah.append(
                        f"baris {hilang['baris']}: <{hilang['tag']}> dibuka "
                        f"tapi tidak pernah ditutup")
                del self.tumpukan[i:]
                return
        self.masalah.append(
            f"baris {self.getpos()[0]}: </{tag}> menutup sesuatu yang "
            f"tidak pernah dibuka")

    def handle_data(self, data):
        teks = _rapikan(data)
        if not teks:
            return
        if self.tumpukan:
            self.tumpukan[-1]["teks"].append(teks)
        else:
            self.akar.append({"tag": "#teks", "atribut": [], "anak": [],
                              "teks": [teks], "baris": self.getpos()[0]})

    def handle_comment(self, data):
        pass                       # komentar tidak ikut jadi struktur

    def selesai(self):
        for sisa in self.tumpukan:
            if sisa["tag"] in BOLEH_TERBUKA:
                continue
            self.masalah.append(
                f"baris {sisa['baris']}: <{sisa['tag']}> dibuka tapi tidak "
                f"pernah ditutup")
        self.tumpukan = []


def _gambar_html(simpul, dalam, keluar):
    spasi = INDENT * dalam
    if simpul["tag"] == "#teks":
        keluar.append(f'{spasi}"{_potong(" ".join(simpul["teks"]))}"')
        return

    bagian = [spasi + simpul["tag"]]
    for nama, nilai in simpul["atribut"]:
        bagian.append(f'{nama}="{nilai}"' if nilai else nama)
    teks = _rapikan(" ".join(simpul["teks"]))
    if teks:
        bagian.append(f'"{_potong(teks)}"')
    keluar.append(" ".join(bagian))

    for anak in simpul["anak"]:
        _gambar_html(anak, dalam + 1, keluar)


def baca_html(kode):
    """(pohon, masalah) — pohon sebagai teks, masalah sebagai daftar kalimat."""
    p = _Pembaca()
    p.feed(kode)
    p.close()
    p.selesai()

    baris = []
    if p.doctype:
        baris.append(p.doctype)
    for simpul in p.akar:
        _gambar_html(simpul, 0, baris)
    if not baris:
        baris.append("(tidak ada satu pun elemen)")
    return "\n".join(baris), p.masalah


# ---------------------------------------------------------------------- CSS

def _buang_komentar_css(kode):
    """Buang /* ... */ tanpa menyentuh yang ada di dalam string."""
    keluar = []
    i = 0
    n = len(kode)
    while i < n:
        c = kode[i]
        if c in "\"'":
            j = i + 1
            while j < n and kode[j] != c:
                j += 2 if kode[j] == "\\" else 1
            keluar.append(kode[i:min(j + 1, n)])
            i = j + 1
        elif kode.startswith("/*", i):
            tutup = kode.find("*/", i + 2)
            # Komentar tak ditutup: sisa berkas memang komentar. Diganti spasi
            # supaya nomor baris tidak bergeser buat pesan kesalahan.
            i = n if tutup < 0 else tutup + 2
            keluar.append(" ")
        else:
            keluar.append(c)
            i += 1
    return "".join(keluar)


def _pisah_deklarasi(badan):
    """Pecah isi blok jadi (properti, nilai). Titik koma di dalam kutip dan
    kurung — url(...), rgba(...) — bukan pemisah."""
    hasil = []
    buffer = []
    dalam_kurung = 0
    kutip = ""
    for c in badan:
        if kutip:
            buffer.append(c)
            if c == kutip:
                kutip = ""
            continue
        if c in "\"'":
            kutip = c
            buffer.append(c)
        elif c == "(":
            dalam_kurung += 1
            buffer.append(c)
        elif c == ")":
            dalam_kurung = max(0, dalam_kurung - 1)
            buffer.append(c)
        elif c == ";" and not dalam_kurung:
            hasil.append("".join(buffer))
            buffer = []
        else:
            buffer.append(c)
    hasil.append("".join(buffer))

    keluar = []
    for potong in hasil:
        potong = _rapikan(potong)
        if not potong:
            continue
        if ":" not in potong:
            keluar.append((potong, None))       # ditandai sebagai masalah
            continue
        prop, _, nilai = potong.partition(":")
        keluar.append((_rapikan(prop), _rapikan(nilai)))
    return keluar


def baca_css(kode):
    """(aturan sebagai teks, masalah)."""
    bersih = _buang_komentar_css(kode)
    baris = []
    masalah = []

    i = 0
    n = len(bersih)
    tumpukan = []                  # untuk @media dan sejenisnya
    while i < n:
        buka = bersih.find("{", i)
        if buka < 0:
            sisa = _rapikan(bersih[i:])
            if sisa and sisa != "}":
                masalah.append(f"'{_potong(sisa, 40)}' tidak diikuti '{{'; "
                               "aturan CSS selalu berbentuk pemilih { … }")
            break

        pemilih = _rapikan(bersih[i:buka])
        # '}' yang menutup blok bersarang ikut terbawa ke depan pemilih.
        while pemilih.startswith("}"):
            if tumpukan:
                tumpukan.pop()
            pemilih = _rapikan(pemilih[1:])

        tutup = _cari_tutup(bersih, buka)
        if tutup < 0:
            masalah.append(f"blok untuk '{_potong(pemilih, 40)}' dibuka "
                           "dengan '{' tapi tidak pernah ditutup dengan '}'")
            tutup = n

        badan = bersih[buka + 1:tutup]
        if pemilih.startswith("@") and "{" in badan:
            baris.append(INDENT * len(tumpukan) + _pemilih_rapi(pemilih))
            tumpukan.append(pemilih)
            i = buka + 1
            continue

        if not pemilih:
            masalah.append("ada blok '{ … }' tanpa pemilih di depannya")
            pemilih = "(tanpa pemilih)"

        dalam = len(tumpukan)
        baris.append(INDENT * dalam + _pemilih_rapi(pemilih))
        isi = _pisah_deklarasi(badan)
        if not isi:
            baris.append(INDENT * (dalam + 1) + "(kosong)")
        for prop, nilai in isi:
            if nilai is None:
                masalah.append(f"'{_potong(prop, 40)}' bukan deklarasi yang "
                               "sah; bentuknya selalu properti: nilai;")
                continue
            baris.append(f"{INDENT * (dalam + 1)}{prop}: {nilai}")
        i = tutup + 1

    if not baris:
        baris.append("(tidak ada satu pun aturan)")
    return "\n".join(baris), masalah


def _cari_tutup(teks, buka):
    dalam = 0
    for i in range(buka, len(teks)):
        if teks[i] == "{":
            dalam += 1
        elif teks[i] == "}":
            dalam -= 1
            if dalam == 0:
                return i
    return -1


def _pemilih_rapi(pemilih):
    """Normalkan spasi di sekitar koma dan kombinator supaya `h1,h2` dan
    `h1 , h2` menghasilkan baris yang sama."""
    p = re.sub(r"\s*,\s*", ", ", pemilih)
    p = re.sub(r"\s*([>+~])\s*", r" \1 ", p)
    return _rapikan(p)


# --------------------------------------------------------------------- main

def main(argv):
    if len(argv) != 3 or argv[1] not in ("html", "css"):
        # Jalurnya ditulis dari akar proyek, sama seperti docstring di atas:
        # pesan pemulihan yang menyuruh perintah yang gagal lebih buruk
        # daripada tidak ada pesan sama sekali.
        print("pemakaian: python3 inti/struktur.py html|css BERKAS",
              file=sys.stderr)
        return 2
    try:
        with open(argv[2], "r", encoding="utf-8", errors="replace") as f:
            kode = f.read()
    except OSError as e:
        print(f"tidak bisa membaca berkas: {e}", file=sys.stderr)
        return 2

    if argv[1] == "html":
        pohon, masalah = baca_html(kode)
    else:
        pohon, masalah = baca_css(kode)

    print(pohon)
    for m in masalah:
        print(m, file=sys.stderr)
    # Masalah dilaporkan lewat stderr TAPI kode keluarnya tetap 0 kalau
    # strukturnya masih terbaca. Tag yang lupa ditutup bukan alasan untuk
    # menyatakan seluruh berkas gagal — browser pun tidak melakukannya, dan
    # pelajar tetap perlu melihat pohonnya untuk mengerti apa yang terjadi.
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
