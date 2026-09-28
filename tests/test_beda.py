"""Tes mesin diff & diagnosis kegagalan latihan.

Modul ini yang menentukan apakah pelajar melihat "GAGAL" atau melihat PERSIS
di mana bedanya. Kalau diagnosisnya salah, ia justru menyesatkan -- lebih buruk
daripada diam.
"""

import unittest

from inti import beda
from inti import runner
from inti import tema


class TestKolomPertamaBeda(unittest.TestCase):
    def test_sama_persis(self):
        self.assertIsNone(beda.kolom_pertama_beda("halo", "halo"))

    def test_beda_di_awal(self):
        self.assertEqual(beda.kolom_pertama_beda("halo", "Halo"), 1)

    def test_beda_di_tengah(self):
        self.assertEqual(beda.kolom_pertama_beda("abcdef", "abcXef"), 4)

    def test_satu_lebih_panjang(self):
        self.assertEqual(beda.kolom_pertama_beda("abc", "abcdef"), 4)
        self.assertEqual(beda.kolom_pertama_beda("abcdef", "abc"), 4)

    def test_kedua_kosong(self):
        self.assertIsNone(beda.kolom_pertama_beda("", ""))


class TestNormalisasiSepadanDenganRunner(unittest.TestCase):
    """Diff dan auto-checker HARUS sepakat soal apa yang dianggap sama.

    Kalau tidak, pelajar bisa melihat "GAGAL" berdampingan dengan diff yang
    menyatakan outputnya sudah sama persis.
    """

    KASUS = [
        ("halo\ndunia", "halo   \ndunia  "),
        ("halo", "halo\n\n\n"),
        ("a\nb", "a\r\nb"),
        ("", "   \n  \n"),
        ("  *\n **", "  *\n **\n"),
    ]

    def test_kesepakatan_dengan_runner(self):
        for a, b in self.KASUS:
            with self.subTest(a=a, b=b):
                sama_runner = runner.normalisasi(a) == runner.normalisasi(b)
                sama_beda = beda.bandingkan(a, b).sama
                self.assertEqual(sama_runner, sama_beda)

    def test_indentasi_baris_pertama_dipertahankan(self):
        d = beda.bandingkan("  *\n **", "*\n **")
        self.assertFalse(d.sama, "spasi di depan baris pertama tidak boleh diabaikan")


class TestDiagnosa(unittest.TestCase):
    def _catatan(self, harapan, aktual):
        return " ".join(beda.bandingkan(harapan, aktual).catatan).lower()

    def test_output_kosong(self):
        self.assertIn("tidak mencetak apa pun", self._catatan("Halo", ""))

    def test_beda_kapital_saja(self):
        self.assertIn("huruf besar/kecil", self._catatan("Halo Dunia", "halo dunia"))

    def test_beda_spasi_saja(self):
        self.assertIn("spasi", self._catatan("a b c", "a  b   c"))

    def test_urutan_tertukar(self):
        self.assertIn("urutannya", self._catatan("1\n2\n3", "3\n2\n1"))

    def test_ikut_mencetak_prompt(self):
        catatan = self._catatan("Lulus", "Masukkan nilai: Lulus")
        self.assertIn("ajakan", catatan)

    def test_baris_hilang(self):
        self.assertIn("belum tercetak", self._catatan("a\nb\nc", "a\nc"))

    def test_baris_berlebih(self):
        self.assertIn("tambahan", self._catatan("a\nb", "a\nb\nc"))

    def test_angka_benar_teks_beda(self):
        catatan = self._catatan("Total: 42", "Jumlah: 42")
        self.assertIn("angkanya sudah benar", catatan)

    def test_beda_pemisah_desimal(self):
        self.assertIn("format", self._catatan("3.75", "3,75"))

    def test_output_sama_tidak_menghasilkan_catatan(self):
        self.assertEqual(beda.bandingkan("halo", "halo").catatan, [])

    def test_tidak_mengarang_saat_tidak_ada_pola(self):
        catatan = beda.bandingkan("alpha\nbeta", "zzz\nyyy\nxxx").catatan
        for c in catatan:
            self.assertNotIn("hanya beda", c.lower())


class TestRender(unittest.TestCase):
    def setUp(self):
        self._asli = tema.kedalaman_aktif()
        tema.pakai_kedalaman(tema.TANPA_WARNA)

    def tearDown(self):
        tema.pakai_kedalaman(self._asli)

    def test_output_sama_dilaporkan_singkat(self):
        baris = beda.render(beda.bandingkan("a", "a"))
        self.assertEqual(len(baris), 1)
        self.assertIn("sama persis", baris[0])

    def test_menampilkan_kedua_sisi(self):
        teks = "\n".join(beda.render(beda.bandingkan("benar", "salah")))
        self.assertIn("diharapkan", teks)
        self.assertIn("punyamu", teks)

    def test_menunjuk_kolom_yang_berbeda(self):
        teks = "\n".join(beda.render(beda.bandingkan("abcdef", "abcXef")))
        self.assertIn("beda mulai kolom 4", teks)

    def test_spasi_tersembunyi_dibuat_terlihat(self):
        teks = "\n".join(beda.render(beda.bandingkan("a b", "a  b")))
        self.assertIn(beda.SPASI_TAMPAK, teks)

    def test_diff_panjang_dipotong(self):
        panjang_h = "\n".join(f"baris {i}" for i in range(100))
        panjang_a = "\n".join(f"lain {i}" for i in range(100))
        baris = beda.render(beda.bandingkan(panjang_h, panjang_a), maks_baris=10)
        self.assertLess(len(baris), 25)
        self.assertTrue(any("tidak ditampilkan" in b for b in baris))

    def test_ringkas_selalu_satu_kalimat(self):
        for h, a in [("a", "a"), ("a", "b"), ("a\nb", ""), ("1", "2")]:
            r = beda.ringkas(beda.bandingkan(h, a))
            self.assertIsInstance(r, str)
            self.assertTrue(r.strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)
