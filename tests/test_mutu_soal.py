"""Kuis yang tidak bisa ditebak dari bentuknya, petunjuk yang tidak membocorkan.

Audit 2026-10-17 (alat/periksa_kuis.py) menemukan 67% jawaban benar adalah
opsi terpanjang, 195 soal yang jawabannya ditandai huruf kapital penekanan,
dan 92 latihan yang petunjuk pertamanya sudah memuat baris solusi. Skor kuis
dipakai penjadwal ulang dan kesiapan Peta Karier, jadi skor yang bisa
ditebak menyesatkan dua fitur sekaligus.

Ambang "terpanjang" sengaja longgar: dengan empat opsi peluang acaknya 25%,
dan kurikulum berisi 40-60 soal, jadi simpangan bakunya sekitar tujuh poin.
40% berarti "tidak lagi sistematis", bukan "harus persis acak".
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "alat"))

from main import LANGUAGES  # noqa: E402
from periksa_kuis import masalah_soal, petunjuk_bocor  # noqa: E402

AMBANG_TERPANJANG = 0.40
AMBANG_JAUH = 3


class TestKuisTidakBisaDitebak(unittest.TestCase):
    def test_jawaban_benar_tidak_selalu_terpanjang(self):
        for lang in LANGUAGES:
            soal = [s for k in lang["quizzes"] for s in k["questions"]]
            n = sum("terpanjang" in masalah_soal(s) for s in soal)
            with self.subTest(bahasa=lang["key"]):
                self.assertLessEqual(n / len(soal), AMBANG_TERPANJANG,
                                     f"{n}/{len(soal)} jawaban benar = opsi terpanjang")

    def test_jawaban_benar_tidak_jauh_lebih_panjang(self):
        for lang in LANGUAGES:
            n = sum("jauh" in masalah_soal(s)
                    for k in lang["quizzes"] for s in k["questions"])
            with self.subTest(bahasa=lang["key"]):
                self.assertLessEqual(n, AMBANG_JAUH)

    def test_kapital_penekanan_tidak_menandai_jawaban(self):
        for lang in LANGUAGES:
            for k in lang["quizzes"]:
                for i, s in enumerate(k["questions"]):
                    with self.subTest(bahasa=lang["key"], kuis=k["title"], soal=i):
                        self.assertNotIn("kapital", masalah_soal(s))


class TestPetunjukBertangga(unittest.TestCase):
    def test_minimal_dua_petunjuk(self):
        for lang in LANGUAGES:
            for ex in lang["exercises"]:
                with self.subTest(bahasa=lang["key"], latihan=ex["title"]):
                    self.assertGreaterEqual(len(ex.get("hints") or []), 2)

    def test_petunjuk_pertama_tidak_memuat_baris_solusi(self):
        for lang in LANGUAGES:
            for ex in lang["exercises"]:
                with self.subTest(bahasa=lang["key"], latihan=ex["title"]):
                    self.assertEqual(petunjuk_bocor(ex), [])


if __name__ == "__main__":
    unittest.main()
