"""Tes mesin rekomendasi langkah berikutnya & tantangan harian."""

import os
import tempfile
import unittest
from datetime import date, timedelta

import konfigurasi
import progress
import saran
from main import LANGUAGES


class BasisSaran(unittest.TestCase):
    """Progres DAN konfigurasi diarahkan ke direktori sementara.

    Konfigurasinya ikut karena `saran` sekarang lewat `bab`, dan `bab` membaca
    setelan "Buka semua bab tanpa syarat". Tanpa pengalihan ini, tes membaca
    berkas konfigurasi milik orang yang menjalankannya: siapa pun yang pernah
    menyalakan saklar itu akan menguji jalur yang berbeda dari CI, dan setiap
    tes penguncian yang ditambahkan nanti lolos palsu di mesinnya sendiri.
    Berkasnya cuma dibaca, tidak ditulis — tapi tes yang hasilnya bergantung
    pada preferensi pribadi bukan tes.
    """

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        self._asli_konfig = konfigurasi.BERKAS
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")
        konfigurasi.BERKAS = os.path.join(self.dir.name, "konfig.json")
        konfigurasi.lupakan_cache()

    def tearDown(self):
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        konfigurasi.BERKAS = self._asli_konfig
        konfigurasi.lupakan_cache()
        self.dir.cleanup()

    def data(self):
        return progress.load_progress()


class TestLangkahBerikutnya(BasisSaran):
    def test_pengguna_baru_diarahkan_ke_materi_pertama(self):
        langkah = saran.langkah_berikutnya(LANGUAGES, self.data())
        self.assertTrue(langkah)
        self.assertEqual(langkah[0].tipe, "materi")
        self.assertEqual(langkah[0].judul, LANGUAGES[0]["materials"][0]["title"])

    def test_kuis_jatuh_tempo_jadi_prioritas_utama(self):
        lang = LANGUAGES[0]
        kuis = lang["quizzes"][0]
        progress.record_quiz_score(f"{lang['key']}_kuis", kuis["title"], 5, 10)
        d = progress.load_progress()
        d["jadwal_kuis"][f"{lang['key']}_kuis::{kuis['title']}"]["jatuh_tempo"] = (
            date.today() - timedelta(days=3)).isoformat()
        progress.save_progress(d)

        langkah = saran.langkah_berikutnya(LANGUAGES, progress.load_progress())
        self.assertEqual(langkah[0].tipe, "kuis")
        self.assertEqual(langkah[0].judul, kuis["title"])
        self.assertIn("diulang", langkah[0].alasan)

    def test_materi_yang_berhenti_di_tengah_diingatkan(self):
        lang = LANGUAGES[2]
        materi = lang["materials"][3]
        progress.record_material_read(f"{lang['key']}_materi", materi["title"],
                                      tuntas=False)
        langkah = saran.langkah_berikutnya(LANGUAGES, progress.load_progress())
        judul = [s.judul for s in langkah]
        self.assertIn(materi["title"], judul)

    def test_melanjutkan_bahasa_yang_sedang_dikerjakan(self):
        lang = LANGUAGES[3]
        progress.record_material_read(f"{lang['key']}_materi",
                                      lang["materials"][0]["title"])
        langkah = saran.langkah_berikutnya(LANGUAGES, progress.load_progress())
        bahasa_disarankan = [s.lang["key"] for s in langkah]
        self.assertIn(lang["key"], bahasa_disarankan)
        # Materi kedua bahasa itu harus muncul, bukan materi pertama yang sudah dibaca.
        judul = [s.judul for s in langkah if s.lang["key"] == lang["key"]]
        self.assertNotIn(lang["materials"][0]["title"], judul)

    def test_tidak_pernah_menyarankan_hal_yang_sama_dua_kali(self):
        lang = LANGUAGES[0]
        progress.record_material_read(f"{lang['key']}_materi",
                                      lang["materials"][0]["title"], tuntas=False)
        langkah = saran.langkah_berikutnya(LANGUAGES, progress.load_progress(), maks=8)
        tanda = [(s.lang["key"], s.tipe, s.judul) for s in langkah]
        self.assertEqual(len(tanda), len(set(tanda)))

    def test_menghormati_batas_jumlah(self):
        langkah = saran.langkah_berikutnya(LANGUAGES, self.data(), maks=2)
        self.assertLessEqual(len(langkah), 2)

    def test_daftar_bahasa_kosong_aman(self):
        self.assertEqual(saran.langkah_berikutnya([], self.data()), [])

    def test_setiap_langkah_punya_alasan_dan_objek(self):
        for s in saran.langkah_berikutnya(LANGUAGES, self.data(), maks=8):
            self.assertTrue(s.alasan.strip())
            self.assertIn("title", s.obj)
            self.assertTrue(s.label().strip())


class TestTantanganHarian(BasisSaran):
    def test_stabil_dalam_satu_hari(self):
        d = self.data()
        a = saran.tantangan_harian(LANGUAGES, d)
        b = saran.tantangan_harian(LANGUAGES, d)
        self.assertEqual((a.lang["key"], a.judul), (b.lang["key"], b.judul))

    def test_berubah_antar_hari(self):
        d = self.data()
        hari = date(2026, 1, 1)
        pilihan = {(saran.tantangan_harian(LANGUAGES, d, hari + timedelta(days=i)).judul)
                   for i in range(20)}
        self.assertGreater(len(pilihan), 1, "tantangan tidak pernah berganti")

    def test_tidak_menawarkan_latihan_yang_sudah_lulus(self):
        d = self.data()
        t = saran.tantangan_harian(LANGUAGES, d)
        progress.record_exercise_passed(f"{t.lang['key']}_latihan", t.judul)
        d2 = progress.load_progress()
        t2 = saran.tantangan_harian(LANGUAGES, d2)
        self.assertNotEqual((t.lang["key"], t.judul), (t2.lang["key"], t2.judul))

    def test_none_kalau_semua_sudah_selesai(self):
        d = self.data()
        for lang in LANGUAGES:
            for e in lang["exercises"]:
                d["latihan_lulus"].append(
                    progress.kunci(f"{lang['key']}_latihan", e["title"]))
        self.assertIsNone(saran.tantangan_harian(LANGUAGES, d))

    def test_selalu_berupa_latihan(self):
        t = saran.tantangan_harian(LANGUAGES, self.data())
        self.assertEqual(t.tipe, "latihan")


class TestRingkasanHariIni(BasisSaran):
    def test_belum_ada_aktivitas(self):
        xp, target, tercapai = saran.ringkasan_hari_ini(self.data(), 60)
        self.assertEqual((xp, target, tercapai), (0, 60, False))

    def test_target_tercapai(self):
        for i in range(8):
            progress.record_material_read("java_materi", f"Materi {i}")
        xp, target, tercapai = saran.ringkasan_hari_ini(progress.load_progress(), 60)
        self.assertGreaterEqual(xp, 60)
        self.assertTrue(tercapai)


if __name__ == "__main__":
    unittest.main(verbosity=2)
