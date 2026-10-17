"""Perkiraan menit (pelajar/waktu.py) dan profesi tujuan (konfigurasi tujuan_karier)."""

import os
import tempfile
import unittest

from main import LANGUAGES
from pelajar import konfigurasi, waktu


class TestPerkiraanWaktu(unittest.TestCase):
    def test_semua_materi_masuk_akal(self):
        for lang in LANGUAGES:
            for m in lang["materials"]:
                with self.subTest(bahasa=lang["key"], materi=m["title"]):
                    self.assertTrue(2 <= waktu.menit_materi(m) <= 90)

    def test_dibulatkan_ke_lima_di_atas_sepuluh(self):
        self.assertEqual(waktu._bulat(23), 25)
        self.assertEqual(waktu._bulat(7.4), 7)
        self.assertEqual(waktu._bulat(0.2), 2)

    def test_proyek_akhir_satu_jam(self):
        proyek = [e for l in LANGUAGES for e in l["exercises"] if e.get("proyek")]
        self.assertTrue(proyek)
        self.assertTrue(all(waktu.menit_latihan(e) == 60 for e in proyek))

    def test_kuis_menurut_jumlah_soal(self):
        q = LANGUAGES[0]["quizzes"][0]
        self.assertEqual(waktu.menit("kuis", q), waktu._bulat(len(q["questions"]) * 0.75))


class TestTujuanKarier(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = konfigurasi.BERKAS
        konfigurasi.BERKAS = os.path.join(self.dir.name, "k.json")
        konfigurasi.lupakan_cache()

    def tearDown(self):
        konfigurasi.BERKAS = self._asli
        konfigurasi.lupakan_cache()
        self.dir.cleanup()

    def test_bawaan_kosong_dan_hanya_menerima_profesi_yang_ada(self):
        self.assertEqual(konfigurasi.ambil("tujuan_karier"), "")
        konfigurasi.pasang("tujuan_karier", "backend-developer")
        self.assertEqual(konfigurasi.ambil("tujuan_karier"), "backend-developer")
        konfigurasi.pasang("tujuan_karier", "astronot")
        self.assertIn(konfigurasi.ambil("tujuan_karier"),
                      {o for o, _ in next(x for x in konfigurasi.SKEMA
                                          if x.kunci == "tujuan_karier").pilihan})


if __name__ == "__main__":
    unittest.main()
