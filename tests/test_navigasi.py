"""Tes navigasi lintas bahasa: pencarian, bookmark, dan lanjut terakhir.

Sebelum berkas ini ada, seluruh isi navigasi.py nol baris tereksekusi. Mutasi
sesederhana `return None` di awal `_cari_objek` -- yang akan membuat menu
Bookmark selalu tampak kosong -- lolos tanpa satu tes pun gagal.
"""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest import mock

from layar import navigasi
from pelajar import konfigurasi
from pelajar import progress
from layar import utils
from main import LANGUAGES


class TestCariObjek(unittest.TestCase):
    def test_menemukan_materi(self):
        lang = LANGUAGES[0]
        judul = lang["materials"][0]["title"]
        hasil = navigasi._cari_objek(LANGUAGES, f"{lang['key']}_materi", judul)
        self.assertIsNotNone(hasil)
        self.assertEqual(hasil["tipe"], "materi")
        self.assertEqual(hasil["obj"]["title"], judul)
        self.assertIs(hasil["lang"], lang)

    def test_menemukan_kuis_dan_latihan(self):
        for lang in LANGUAGES:
            for tipe, koleksi in (("kuis", lang["quizzes"]),
                                  ("latihan", lang["exercises"])):
                judul = koleksi[0]["title"]
                with self.subTest(bahasa=lang["label"], tipe=tipe):
                    hasil = navigasi._cari_objek(LANGUAGES, f"{lang['key']}_{tipe}", judul)
                    self.assertIsNotNone(hasil)
                    self.assertEqual(hasil["obj"]["title"], judul)

    def test_judul_yang_sudah_tidak_ada(self):
        self.assertIsNone(
            navigasi._cari_objek(LANGUAGES, "java_materi", "Judul Yang Dihapus"))

    def test_kategori_tanpa_pemisah(self):
        self.assertIsNone(navigasi._cari_objek(LANGUAGES, "javamateri", "apa saja"))

    def test_prefix_bahasa_tidak_bocor(self):
        """'java' tidak boleh cocok dengan konten 'javascript'."""
        judul = next(l for l in LANGUAGES if l["key"] == "javascript")["materials"][0]["title"]
        self.assertIsNone(navigasi._cari_objek(LANGUAGES, "java_materi", judul))

    def test_tipe_tak_dikenal(self):
        self.assertIsNone(navigasi._cari_objek(LANGUAGES, "java_ngawur", "apa saja"))


class TestPencarian(unittest.TestCase):
    def test_menemukan_kata_umum_di_banyak_tipe(self):
        hasil = navigasi._kumpulkan(LANGUAGES, "perulangan")
        self.assertTrue(hasil)
        self.assertGreaterEqual(len({h["tipe"] for h in hasil}), 2)

    def test_diurutkan_dari_yang_paling_sering(self):
        hasil = navigasi._kumpulkan(LANGUAGES, "array")
        jumlah = [h["jumlah"] for h in hasil]
        self.assertEqual(jumlah, sorted(jumlah, reverse=True))

    def test_saringan_tipe_bekerja(self):
        for tipe in ("materi", "kuis", "latihan"):
            hasil = navigasi._kumpulkan(LANGUAGES, "fungsi", tipe)
            with self.subTest(tipe=tipe):
                self.assertTrue(all(h["tipe"] == tipe for h in hasil))

    def test_kata_tak_ada_memberi_daftar_kosong(self):
        self.assertEqual(navigasi._kumpulkan(LANGUAGES, "zzzqqqxxx"), [])

    def test_tidak_membedakan_huruf_besar_kecil(self):
        self.assertEqual(len(navigasi._kumpulkan(LANGUAGES, "JOIN")),
                         len(navigasi._kumpulkan(LANGUAGES, "join")))

    def test_setiap_hasil_punya_cuplikan(self):
        for h in navigasi._kumpulkan(LANGUAGES, "variabel")[:20]:
            self.assertTrue(h["cuplikan"].strip())
            self.assertGreater(h["jumlah"], 0)


class TestPotongan(unittest.TestCase):
    def test_mengambil_teks_di_sekitar_kata(self):
        teks = "a" * 200 + "PENTING" + "b" * 200
        cuplik = navigasi._potongan(teks, "PENTING")
        self.assertIn("PENTING", cuplik)
        self.assertLess(len(cuplik), 200)

    def test_kata_tak_ada_memberi_string_kosong(self):
        self.assertEqual(navigasi._potongan("halo dunia", "zzz"), "")

    def test_baris_baru_diratakan(self):
        self.assertNotIn("\n", navigasi._potongan("satu\nPENTING\ndua", "PENTING"))


class BasisNavigasi(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        self._asli_konfig = konfigurasi.BERKAS
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")
        # Konfigurasi ikut dialihkan: `navigasi` sekarang lewat `bab`, yang
        # membaca setelan "Buka semua bab tanpa syarat". Membiarkannya menunjuk
        # berkas asli membuat hasil tes bergantung pada preferensi pribadi
        # orang yang menjalankannya.
        konfigurasi.BERKAS = os.path.join(self.dir.name, "konfig.json")
        konfigurasi.lupakan_cache()
        self._patch = mock.patch.object(utils, "clear", lambda: None)
        self._patch.start()

    def tearDown(self):
        self._patch.stop()
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        konfigurasi.BERKAS = self._asli_konfig
        konfigurasi.lupakan_cache()
        self.dir.cleanup()

    def jalankan(self, fungsi, masukan):
        with mock.patch("builtins.input", side_effect=list(masukan) + ["0"] * 20):
            with redirect_stdout(io.StringIO()) as keluar:
                fungsi(LANGUAGES)
        return keluar.getvalue()


class TestBookmark(BasisNavigasi):
    def test_bookmark_nyata_ditampilkan(self):
        lang = LANGUAGES[0]
        judul = lang["materials"][0]["title"]
        progress.toggle_bookmark(f"{lang['key']}_materi", judul)
        teks = self.jalankan(navigasi.menu_bookmark, ["0"])
        self.assertIn(judul[:20], teks)

    def test_bookmark_basi_dilaporkan_bukan_disembunyikan(self):
        d = progress.load_progress()
        d["bookmark"].append("java_materi::Judul Yang Sudah Dihapus")
        progress.save_progress(d)
        teks = self.jalankan(navigasi.menu_bookmark, ["", ""])
        self.assertIn("sudah tidak ada", teks)

    def test_bersihkan_bookmark_basi(self):
        lang = LANGUAGES[0]
        judul = lang["materials"][0]["title"]
        progress.toggle_bookmark(f"{lang['key']}_materi", judul)
        d = progress.load_progress()
        d["bookmark"].append("java_materi::Hantu")
        progress.save_progress(d)

        self.jalankan(navigasi.menu_bookmark, ["x", "", "0"])
        sisa = progress.load_progress()["bookmark"]
        self.assertNotIn("java_materi::Hantu", sisa)
        self.assertIn(progress.kunci(f"{lang['key']}_materi", judul), sisa)

    def test_kunci_valid_mencakup_semua_tipe(self):
        sah = navigasi._kunci_bookmark_valid(LANGUAGES)
        lang = LANGUAGES[0]
        for tipe, koleksi in (("materi", lang["materials"]), ("kuis", lang["quizzes"]),
                              ("latihan", lang["exercises"])):
            self.assertIn(progress.kunci(f"{lang['key']}_{tipe}", koleksi[0]["title"]), sah)


class TestLanjutTerakhir(BasisNavigasi):
    def test_tanpa_riwayat(self):
        teks = self.jalankan(navigasi.lanjut_terakhir, [""])
        self.assertIn("Belum ada riwayat", teks)

    def test_menampilkan_item_terakhir(self):
        lang = LANGUAGES[1]
        judul = lang["materials"][0]["title"]
        progress.record_material_read(f"{lang['key']}_materi", judul)
        teks = self.jalankan(navigasi.lanjut_terakhir, ["0"])
        self.assertIn(judul[:20], teks)
        self.assertIn(lang["label"], teks)

    def test_menawarkan_materi_berikutnya(self):
        lang = LANGUAGES[1]
        progress.record_material_read(f"{lang['key']}_materi",
                                      lang["materials"][0]["title"])
        teks = self.jalankan(navigasi.lanjut_terakhir, ["0"])
        self.assertIn(lang["materials"][1]["title"][:20], teks)

    def test_riwayat_menunjuk_konten_terhapus(self):
        d = progress.load_progress()
        d["terakhir"] = {"tipe": "materi", "kategori": "java_materi",
                         "judul": "Sudah Dihapus", "waktu": "2026-01-01T00:00:00"}
        progress.save_progress(d)
        teks = self.jalankan(navigasi.lanjut_terakhir, [""])
        self.assertIn("tidak ditemukan", teks)


if __name__ == "__main__":
    unittest.main(verbosity=2)
