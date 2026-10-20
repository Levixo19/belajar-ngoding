"""Peta soal kuis -> materi (data/kuis_materi.py) dan logika kesiapannya."""

import os
import tempfile
import unittest

from data.kuis_materi import KUIS_MATERI
from inti.kurikulum import LANGUAGES
from pelajar import konfigurasi, kuis_materi, progress
from pelajar.progress import judul_kunci


class TestPetaUtuh(unittest.TestCase):
    def test_tiap_kuis_punya_entri_per_soal(self):
        for lang in LANGUAGES:
            peta = KUIS_MATERI.get(lang["key"], {})
            self.assertEqual(sorted(peta), sorted(q["title"] for q in lang["quizzes"]),
                             lang["key"])
            for q in lang["quizzes"]:
                with self.subTest(bahasa=lang["key"], kuis=q["title"]):
                    self.assertEqual(len(peta[q["title"]]), len(q["questions"]))

    def test_tiap_judul_materi_memang_ada(self):
        for lang in LANGUAGES:
            ada = {judul_kunci(m["title"]) for m in lang["materials"]}
            for judul_kuis, daftar in KUIS_MATERI[lang["key"]].items():
                for i, t in enumerate(daftar):
                    with self.subTest(bahasa=lang["key"], kuis=judul_kuis, soal=i):
                        self.assertIn(t, ada, "judul materi tak dikenal (ganti nama?)")


class TestKesiapan(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = (progress.PROGRESS_FILE, progress.PROGRESS_FILE_LAMA, konfigurasi.BERKAS)
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "x.json")
        konfigurasi.BERKAS = os.path.join(self.dir.name, "k.json")
        konfigurasi.lupakan_cache()
        self.lang = next(l for l in LANGUAGES if l["key"] == "python")
        self.kuis = self.lang["quizzes"][0]

    def tearDown(self):
        progress.PROGRESS_FILE, progress.PROGRESS_FILE_LAMA, konfigurasi.BERKAS = self._asli
        konfigurasi.lupakan_cache()
        self.dir.cleanup()

    def test_profil_baru_belum_siap(self):
        self.assertFalse(kuis_materi.kuis_siap(self.lang, self.kuis, progress.load_progress()))

    def test_siap_tepat_saat_materi_terakhir_yang_diuji_dibaca(self):
        indeks = kuis_materi.materi_kuis(self.lang, self.kuis)
        self.assertTrue(indeks)
        for i in indeks[:-1]:
            progress.record_material_read("python_materi", self.lang["materials"][i]["title"])
        sebelum = progress.load_progress()
        self.assertFalse(kuis_materi.kuis_siap(self.lang, self.kuis, sebelum))
        self.assertEqual(kuis_materi.sisa_materi(self.lang, self.kuis, sebelum), indeks[-1:])
        progress.record_material_read("python_materi",
                                      self.lang["materials"][indeks[-1]]["title"])
        sesudah = progress.load_progress()
        self.assertTrue(kuis_materi.kuis_siap(self.lang, self.kuis, sesudah))
        baru = kuis_materi.kuis_baru_siap(self.lang, sebelum, sesudah)
        self.assertIn(self.kuis["title"], [q["title"] for _, q in baru])

    def test_kuis_yang_sudah_dikerjakan_tidak_ditawarkan_lagi(self):
        indeks = kuis_materi.materi_kuis(self.lang, self.kuis)
        for i in indeks[:-1]:
            progress.record_material_read("python_materi", self.lang["materials"][i]["title"])
        progress.record_quiz_score("python_kuis", self.kuis["title"], 5, 8)
        sebelum = progress.load_progress()
        progress.record_material_read("python_materi",
                                      self.lang["materials"][indeks[-1]]["title"])
        self.assertEqual(kuis_materi.kuis_baru_siap(self.lang, sebelum,
                                                    progress.load_progress()), [])

    def test_materi_soal_menunjuk_materi_yang_ada(self):
        i, judul = kuis_materi.materi_soal(self.lang, self.kuis["title"], 0)
        self.assertEqual(self.lang["materials"][i]["title"], judul)
        self.assertIsNone(kuis_materi.materi_soal(self.lang, self.kuis["title"], 999))


if __name__ == "__main__":
    unittest.main()
