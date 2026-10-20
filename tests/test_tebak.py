"""Tebak keluarannya (pelajar/tebak.py, /api/tebak)."""

import os
import tempfile
import unittest

from inti import runner
from inti.kurikulum import LANGUAGES
from pelajar import konfigurasi, progress, tebak

L = {l["key"]: l for l in LANGUAGES}


class TestBlokLayak(unittest.TestCase):
    def test_sesi_fedora_git_dan_html_css_tidak_pernah_ikut(self):
        for key in ("fedora", "git", "html", "css"):
            self.assertEqual(tebak.blok_layak(L[key]), [], key)

    def test_tidak_ada_contoh_yang_membaca_masukan(self):
        for lang in LANGUAGES:
            for _i, _j, kode in tebak.blok_layak(lang):
                self.assertNotIn("input(", kode)
                self.assertNotIn("Scanner", kode)


class BasisTebak(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = (progress.PROGRESS_FILE, progress.PROGRESS_FILE_LAMA, konfigurasi.BERKAS)
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "x.json")
        konfigurasi.BERKAS = os.path.join(self.dir.name, "k.json")
        konfigurasi.lupakan_cache()

    def tearDown(self):
        progress.PROGRESS_FILE, progress.PROGRESS_FILE_LAMA, konfigurasi.BERKAS = self._asli
        konfigurasi.lupakan_cache()
        self.dir.cleanup()


class TestKartuDanCatatan(BasisTebak):
    def test_kartu_hanya_dari_materi_yang_sudah_dibaca(self):
        if not runner.tersedia("python"):
            self.skipTest("python")
        py = L["python"]
        self.assertEqual(tebak.pilih_kartu(py, progress.load_progress()), [])
        progress.record_material_read("python_materi", py["materials"][0]["title"])
        kartu = tebak.pilih_kartu(py, progress.load_progress())
        self.assertTrue(kartu)
        self.assertTrue(all(i == 0 for i, _j, _k in kartu))

    def test_xp_hanya_untuk_benar_pertama_dan_salah_didahulukan(self):
        py = L["python"]
        for m in py["materials"][:6]:
            progress.record_material_read("python_materi", m["title"])
        a, b = tebak.pilih_kartu(py, progress.load_progress())[:2]
        kb = tebak.kunci_blok(py, b[0], b[1])
        xp0 = progress.load_progress()["xp"]
        progress.record_tebakan(kb, True)
        progress.record_tebakan(kb, True)
        self.assertEqual(progress.load_progress()["xp"] - xp0, progress.XP_TEBAK_BENAR)
        progress.record_tebakan(kb, False)
        pertama = tebak.pilih_kartu(py, progress.load_progress())[0]
        self.assertEqual(pertama[:2], b[:2], "yang terakhir salah ditebak muncul paling dulu")


class TestApiTebak(BasisTebak):
    def test_menolak_kode_yang_bukan_contoh_materi(self):
        from webapp import api
        with self.assertRaises(api.Galat) as konteks:
            api.tebak({"key": "python", "indeks": 0, "kode": "print('bebas')", "tebakan": ""})
        self.assertEqual(konteks.exception.kode, 409)

    def test_tebakan_dinilai_dari_keluaran_nyata(self):
        if not runner.tersedia("python"):
            self.skipTest("python")
        from webapp import api
        py = L["python"]
        progress.record_material_read("python_materi", py["materials"][0]["title"])
        i, _j, kode = tebak.pilih_kartu(py, progress.load_progress())[0]
        salah = api.tebak({"key": "python", "indeks": i, "kode": kode, "tebakan": "bukan ini"})
        self.assertFalse(salah["benar"])
        tepat = api.tebak({"key": "python", "indeks": i, "kode": kode, "tebakan": salah["keluaran"]})
        self.assertTrue(tepat["benar"])


if __name__ == "__main__":
    unittest.main()
