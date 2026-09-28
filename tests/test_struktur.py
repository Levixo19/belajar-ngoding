"""Tes pembaca struktur HTML dan CSS.

Modul `struktur.py` menentukan LULUS atau TIDAK untuk setiap latihan HTML dan
CSS: auto-checker menjalankan solusi contoh, menyimpan pohon yang dicetaknya
sebagai kunci jawaban, lalu mengadu pohon milik pelajar dengannya. Satu
perbedaan spasi saja membuat jawaban yang benar dinyatakan salah -- dan bagi
pemula, "kodeku sama tapi tetap salah" adalah titik orang berhenti belajar.

Dua sifat karena itu diuji paling keras:

1. **Determinisme.** Masukan yang sama wajib menghasilkan keluaran yang sama
   persis, berapa kali pun dijalankan, dan tidak boleh bergantung pada urutan
   iterasi dict atau apa pun yang bisa berubah antar-proses.
2. **Kesetaraan yang benar.** Dua berkas yang berbeda HANYA pada hal yang
   tidak berarti -- indentasi, urutan atribut, spasi di sekitar koma -- wajib
   menghasilkan pohon yang identik. Kalau tidak, pelajar dihukum untuk
   sesuatu yang bukan kesalahan.
"""

import os
import subprocess
import sys
import tempfile
import unittest

from inti import struktur

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestHtml(unittest.TestCase):

    def pohon(self, kode):
        teks, _ = struktur.baca_html(kode)
        return teks

    def masalah(self, kode):
        _, m = struktur.baca_html(kode)
        return m

    # ---------------------------------------------------------- bentuk dasar

    def test_pohon_berindentasi_mengikuti_kedalaman(self):
        self.assertEqual(
            self.pohon("<div><p>Halo</p></div>"),
            'div\n  p "Halo"')

    def test_teks_dipadatkan_spasinya(self):
        # Sumber yang cuma berbeda spasi dan baris barunya wajib sama hasilnya.
        rapat = self.pohon("<p>Halo dunia</p>")
        renggang = self.pohon("<p>\n   Halo\n   dunia\n</p>")
        self.assertEqual(rapat, renggang)
        self.assertEqual(rapat, 'p "Halo dunia"')

    def test_indentasi_sumber_tidak_mengubah_hasil(self):
        datar = "<ul><li>Satu</li><li>Dua</li></ul>"
        menjorok = """
            <ul>
                <li>Satu</li>
                <li>Dua</li>
            </ul>
        """
        self.assertEqual(self.pohon(datar), self.pohon(menjorok))

    def test_atribut_diurutkan_bukan_mengikuti_urutan_tulis(self):
        # Urutan atribut tidak punya arti apa pun di HTML. Membiarkannya
        # memengaruhi hasil berarti menggagalkan pelajar tanpa sebab.
        a = self.pohon('<img src="a.png" alt="Foto" class="besar">')
        b = self.pohon('<img class="besar" alt="Foto" src="a.png">')
        self.assertEqual(a, b)
        self.assertEqual(a, 'img alt="Foto" class="besar" src="a.png"')

    def test_atribut_tanpa_nilai_ditulis_tanpa_sama_dengan(self):
        self.assertEqual(self.pohon("<input required>"), "input required")

    def test_doctype_dinormalkan_jadi_huruf_kecil(self):
        self.assertEqual(self.pohon("<!DOCTYPE html><p>x</p>").splitlines()[0],
                         "<!doctype html>")

    def test_komentar_tidak_masuk_pohon(self):
        self.assertEqual(self.pohon("<p>a</p><!-- catatan --><p>b</p>"),
                         'p "a"\np "b"')

    def test_entitas_diubah_jadi_karakternya(self):
        self.assertEqual(self.pohon("<p>Roti &amp; Susu</p>"),
                         'p "Roti & Susu"')

    def test_teks_panjang_dipotong_supaya_pohon_tetap_terbaca(self):
        hasil = self.pohon("<p>" + "a" * 200 + "</p>")
        self.assertLess(len(hasil), 100)
        self.assertTrue(hasil.endswith('…"'), hasil)

    def test_halaman_kosong_tetap_menghasilkan_sesuatu(self):
        # Latihan yang keluarannya kosong akan meloloskan kode kosong juga.
        self.assertTrue(self.pohon("").strip())
        self.assertTrue(self.pohon("   \n  ").strip())

    # ------------------------------------------------------------- keluhan

    def test_tag_lupa_ditutup_dilaporkan_dengan_nomor_baris(self):
        m = self.masalah("<div>\n<section>\n<p>isi</p>\n</div>")
        self.assertTrue(any("section" in x and "baris 2" in x for x in m), m)

    def test_penutup_tanpa_pembuka_dilaporkan(self):
        m = self.masalah("<p>a</p></div>")
        self.assertTrue(any("</div>" in x for x in m), m)

    def test_elemen_kosong_tidak_dituntut_ditutup(self):
        # <br>, <img>, <meta> memang tidak punya tag penutup. Mengeluhkannya
        # berarti menyalahkan pelajar untuk sesuatu yang justru benar.
        self.assertEqual(self.masalah("<p>a<br>b</p><img src='x.png'>"), [])

    def test_li_tanpa_penutup_bukan_kesalahan(self):
        # HTML menutup <li> sendiri saat </ul> datang. Ini sah, dan sangat
        # sering ditulis begitu di kurikulum mana pun.
        self.assertEqual(self.masalah("<ul><li>Satu<li>Dua</ul>"), [])

    def test_li_tanpa_penutup_tetap_jadi_dua_elemen_bersaudara(self):
        # Yang penting bukan cuma diamnya, tapi pohonnya harus benar: dua <li>
        # bersaudara, bukan yang satu bersarang di dalam yang lain.
        self.assertEqual(self.pohon("<ul><li>Satu<li>Dua</ul>"),
                         'ul\n  li "Satu"\n  li "Dua"')

    def test_p_ditutup_sendiri_oleh_blok_berikutnya(self):
        self.assertEqual(self.pohon("<p>satu<p>dua"), 'p "satu"\np "dua"')

    def test_penutup_pada_elemen_kosong_dikeluhkan(self):
        m = self.masalah("<br></br>")
        self.assertTrue(any("tidak diperlukan" in x for x in m), m)

    def test_html_dan_body_boleh_tidak_ditutup(self):
        self.assertEqual(self.masalah("<html><body><p>a</p>"), [])


class TestCss(unittest.TestCase):

    def aturan(self, kode):
        teks, _ = struktur.baca_css(kode)
        return teks

    def masalah(self, kode):
        _, m = struktur.baca_css(kode)
        return m

    def test_bentuk_dasar(self):
        self.assertEqual(self.aturan("body { color: red; }"),
                         "body\n  color: red")

    def test_spasi_dan_baris_tidak_mengubah_hasil(self):
        a = self.aturan("body{color:red;margin:0}")
        b = self.aturan("body {\n  color : red ;\n  margin : 0 ;\n}")
        self.assertEqual(a, b)

    def test_urutan_properti_dipertahankan(self):
        # Berbeda dengan atribut HTML, urutan properti CSS BERARTI: yang
        # belakangan menimpa yang duluan. Menyortirnya akan menyembunyikan
        # justru hal yang paling perlu dimengerti pemula soal cascade.
        self.assertEqual(self.aturan("p { margin: 0; color: red; }"),
                         "p\n  margin: 0\n  color: red")
        self.assertNotEqual(self.aturan("p { margin: 0; color: red; }"),
                            self.aturan("p { color: red; margin: 0; }"))

    def test_komentar_dibuang(self):
        self.assertEqual(self.aturan("/* tema */ body { color: red; }"),
                         "body\n  color: red")

    def test_komentar_di_dalam_blok_dibuang(self):
        self.assertEqual(
            self.aturan("body { color: red; /* catatan */ margin: 0; }"),
            "body\n  color: red\n  margin: 0")

    def test_pemilih_banyak_dirapikan_spasinya(self):
        self.assertEqual(self.aturan("h1,h2 { color: red; }").splitlines()[0],
                         "h1, h2")
        self.assertEqual(self.aturan("h1 ,  h2 { color: red; }").splitlines()[0],
                         "h1, h2")

    def test_kombinator_dirapikan(self):
        self.assertEqual(self.aturan(".a>.b { color: red; }").splitlines()[0],
                         ".a > .b")

    def test_titik_koma_di_dalam_kurung_bukan_pemisah(self):
        # url(data:image/svg+xml;base64,...) pernah memecah parser naif.
        hasil = self.aturan('a { background: url("x;y.png"); color: red; }')
        self.assertIn('background: url("x;y.png")', hasil)
        self.assertIn("color: red", hasil)

    def test_media_query_bersarang(self):
        hasil = self.aturan("@media (max-width: 600px) { h1 { color: red; } }")
        self.assertEqual(hasil, "@media (max-width: 600px)\n  h1\n    color: red")

    def test_deklarasi_terakhir_tanpa_titik_koma_tetap_terbaca(self):
        self.assertEqual(self.aturan("body { color: red }"),
                         "body\n  color: red")

    def test_berkas_kosong_tetap_menghasilkan_sesuatu(self):
        self.assertTrue(self.aturan("").strip())

    def test_kurung_tak_ditutup_dilaporkan(self):
        m = self.masalah("body { color: red;")
        self.assertTrue(any("tidak pernah ditutup" in x for x in m), m)

    def test_deklarasi_tanpa_titik_dua_dilaporkan(self):
        m = self.masalah("body { font-size 16px; }")
        self.assertTrue(any("bukan deklarasi yang sah" in x for x in m), m)

    def test_blok_tanpa_pemilih_dilaporkan(self):
        m = self.masalah("{ color: red; }")
        self.assertTrue(any("tanpa pemilih" in x for x in m), m)


class TestDeterministik(unittest.TestCase):
    """Hasil yang sama, berapa kali pun dan di proses mana pun.

    Auto-checker menurunkan kunci jawaban dengan MENJALANKAN solusi contoh.
    Kalau keluarannya bisa berbeda antar-jalan, latihannya mustahil lulus dan
    tidak ada satu pun pesan error yang menjelaskan kenapa. `test_solutions`
    menjaga hal yang sama untuk seluruh bahasa lain; ini menjaganya di
    tingkat modul.
    """

    CONTOH_HTML = """<!DOCTYPE html>
<html lang="id">
<head><meta charset="utf-8"><title>Uji</title></head>
<body>
  <h1 id="judul" class="besar">Halo</h1>
  <ul><li>Satu<li>Dua</ul>
  <img src="a.png" alt="A">
</body>
</html>"""

    CONTOH_CSS = """/* tema */
body { background-color: #fff; font-family: sans-serif; margin: 0 }
h1, h2 { color: #333; text-align: center; }
@media (max-width: 600px) { h1 { font-size: 1.5rem; } }"""

    def test_dua_panggilan_di_proses_yang_sama_identik(self):
        for baca, kode in ((struktur.baca_html, self.CONTOH_HTML),
                           (struktur.baca_css, self.CONTOH_CSS)):
            self.assertEqual(baca(kode), baca(kode))

    def test_dua_proses_terpisah_identik(self):
        # Proses baru berarti hash seed baru. Kalau ada dict yang urutannya
        # ikut menentukan keluaran, di sinilah ia ketahuan.
        for jenis, kode in (("html", self.CONTOH_HTML), ("css", self.CONTOH_CSS)):
            keluaran = set()
            for _ in range(3):
                with tempfile.TemporaryDirectory() as d:
                    berkas = os.path.join(d, "uji." + jenis)
                    with open(berkas, "w", encoding="utf-8") as f:
                        f.write(kode)
                    hasil = subprocess.run(
                        [sys.executable, os.path.join(AKAR, "inti", "struktur.py"),
                         jenis, berkas],
                        capture_output=True, text=True, timeout=30,
                        env={**os.environ, "PYTHONHASHSEED": "random"})
                self.assertEqual(hasil.returncode, 0, hasil.stderr)
                keluaran.add(hasil.stdout)
            self.assertEqual(len(keluaran), 1,
                             f"{jenis} menghasilkan keluaran berbeda antar-proses")

    def test_markup_rusak_tidak_menjatuhkan_pembaca(self):
        # Yang ditulis pemula bisa rusak dengan cara apa pun. Pembacanya boleh
        # mengeluh, tapi tidak boleh melempar exception -- exception berarti
        # layar error, bukan umpan balik yang bisa dipelajari.
        rusak = [
            "<div><p>tak ditutup",
            "</div>",
            "<a href=>x</a>",
            "<<>>",
            "<p>" * 200,
            "<!-- komentar tak ditutup",
            "<img src='belum ditutup",
            "",
            "   ",
            "teks polos tanpa satu pun tag",
        ]
        for kode in rusak:
            with self.subTest(kode=kode[:30]):
                teks, masalah = struktur.baca_html(kode)
                self.assertIsInstance(teks, str)
                self.assertIsInstance(masalah, list)

        rusak_css = [
            "body {",
            "}",
            "body { color }",
            "{ }",
            "/* tak ditutup",
            "@media {",
            "body { background: url(",
            "",
            "bukan css sama sekali",
        ]
        for kode in rusak_css:
            with self.subTest(kode=kode[:30]):
                teks, masalah = struktur.baca_css(kode)
                self.assertIsInstance(teks, str)
                self.assertIsInstance(masalah, list)


class TestLewatRunner(unittest.TestCase):
    """HTML dan CSS harus masuk mesin eksekusi yang sama dengan bahasa lain."""

    def test_keduanya_selalu_tersedia(self):
        # Tidak butuh satu program pun untuk dipasang -- itu justru alasan
        # keduanya ditaruh paling depan di daftar bahasa.
        from inti import runner
        for b in ("html", "css"):
            self.assertTrue(runner.tersedia(b), b)
            self.assertEqual(runner.program_hilang(b), [])

    def test_jalankan_html_lewat_runner(self):
        from inti import runner
        h = runner.jalankan("html", "<h1>Halo</h1>")
        self.assertTrue(h.sukses, h.galat)
        self.assertIn('h1 "Halo"', h.keluaran)

    def test_jalankan_css_lewat_runner(self):
        from inti import runner
        h = runner.jalankan("css", "body { color: red; }")
        self.assertTrue(h.sukses, h.galat)
        self.assertIn("color: red", h.keluaran)

    def test_markup_rusak_tetap_sukses_tapi_mengeluh(self):
        # Tag yang lupa ditutup bukan alasan menyatakan seluruh berkas gagal:
        # browser pun tidak melakukannya, dan pelajar tetap perlu melihat
        # pohonnya untuk mengerti apa yang terjadi.
        from inti import runner
        h = runner.jalankan("html", "<div><p>lupa ditutup")
        self.assertTrue(h.sukses)
        self.assertIn("div", h.keluaran)
        self.assertIn("tidak pernah ditutup", h.galat)


class TestLatihanHtmlCss(unittest.TestCase):
    """Contoh keluaran yang dijanjikan soal HARUS sama dengan keluaran nyata.

    Latihan HTML dan CSS dinilai dengan membandingkan pohon struktur, jadi
    soalnya menuliskan pohon yang diharapkan apa adanya supaya pelajar tahu
    persis apa yang dituju. Janji itu ditulis tangan, dan begitu solusi
    contohnya disunting sedikit saja -- satu atribut ditambah, satu properti
    dipindah -- janjinya jadi berbohong tanpa ada yang tahu. Yang terjadi pada
    pelajar: ia menyalin bentuk yang dijanjikan soal, hasilnya dinyatakan
    salah, dan tidak ada satu pun keterangan yang menjelaskan kenapa.

    Tes ini mengadu keduanya untuk SETIAP latihan HTML dan CSS.
    """

    @classmethod
    def setUpClass(cls):
        import main
        cls.bahasa = [l for l in main.LANGUAGES if l["key"] in ("html", "css")]
        cls.assertTrue_ = len(cls.bahasa) == 2

    @staticmethod
    def _rata(baris):
        """Buang indentasi bersama supaya perbandingannya soal bentuk, bukan
        soal berapa spasi penulis soal memakai untuk menjorokkan contohnya."""
        isi = [b.rstrip() for b in baris if b.strip()]
        if not isi:
            return []
        pad = min(len(b) - len(b.lstrip()) for b in isi)
        return [b[pad:] for b in isi]

    def test_setiap_solusi_menghasilkan_keluaran_yang_deterministik(self):
        for lang in self.bahasa:
            jenis = lang["key"]
            for e in lang["exercises"]:
                with self.subTest(latihan=f"{jenis}/{e['title']}"):
                    a = self._jalankan(jenis, e["solution"])
                    b = self._jalankan(jenis, e["solution"])
                    self.assertEqual(a.returncode, 0, a.stderr)
                    self.assertEqual(a.stdout, b.stdout,
                                     "keluaran berubah antar-jalan")
                    self.assertTrue(a.stdout.strip(),
                                    "keluaran kosong: kode kosong pun akan lulus")

    def test_solusi_contoh_sendiri_tidak_boleh_mengeluh(self):
        # Kalau solusi contoh saja markup-nya bermasalah, pelajar yang
        # menirunya akan melihat keluhan yang sama dan mengira dirinya salah.
        for lang in self.bahasa:
            for e in lang["exercises"]:
                with self.subTest(latihan=f"{lang['key']}/{e['title']}"):
                    hasil = self._jalankan(lang["key"], e["solution"])
                    self.assertEqual(hasil.stderr.strip(), "")

    def test_contoh_keluaran_di_soal_sama_dengan_keluaran_nyata(self):
        import re
        diperiksa = 0
        for lang in self.bahasa:
            jenis = lang["key"]
            for e in lang["exercises"]:
                soal = "\n".join(e["question"])
                m = re.search(r"Keluaran yang diharapkan[^\n]*:?\s*\n(.*)$",
                              soal, re.S)
                with self.subTest(latihan=f"{jenis}/{e['title']}"):
                    self.assertIsNotNone(
                        m, "soal tidak menuliskan contoh keluaran — tanpa itu "
                           "latihan yang dinilai per-karakter mustahil "
                           "dikerjakan")
                    nyata = self._jalankan(jenis, e["solution"]).stdout
                    self.assertEqual(self._rata(m.group(1).splitlines()),
                                     self._rata(nyata.splitlines()))
                    diperiksa += 1
        self.assertGreaterEqual(diperiksa, 20,
                                "terlalu sedikit latihan yang benar-benar diadu")

    @staticmethod
    def _jalankan(jenis, kode):
        with tempfile.TemporaryDirectory() as d:
            berkas = os.path.join(d, "uji." + jenis)
            with open(berkas, "w", encoding="utf-8") as f:
                f.write(kode)
            return subprocess.run(
                [sys.executable, os.path.join(AKAR, "inti", "struktur.py"), jenis,
                 berkas],
                capture_output=True, text=True, timeout=30)


if __name__ == "__main__":
    unittest.main()
