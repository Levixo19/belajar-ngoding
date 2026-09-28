"""Tes preferensi pengguna.

Berkas konfigurasi diedit tangan oleh sebagian orang, jadi setiap nilai harus
tahan terhadap isian ngawur: nilai bertipe salah, di luar rentang, atau kunci
yang tidak dikenal sama sekali.
"""

import json
import os
import tempfile
import unittest

from pelajar import konfigurasi
from inti import tema


class BasisKonfig(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = konfigurasi.BERKAS
        konfigurasi.BERKAS = os.path.join(self.dir.name, "konfig.json")
        konfigurasi.lupakan_cache()
        self._tema_asli = tema.tema_aktif()
        self._dalam_asli = tema.kedalaman_aktif()

    def tearDown(self):
        konfigurasi.BERKAS = self._asli
        konfigurasi.lupakan_cache()
        tema.pakai_tema(self._tema_asli)
        tema.pakai_kedalaman(self._dalam_asli)
        self.dir.cleanup()

    def tulis(self, isi):
        with open(konfigurasi.BERKAS, "w", encoding="utf-8") as f:
            if isinstance(isi, str):
                f.write(isi)
            else:
                json.dump(isi, f)
        konfigurasi.lupakan_cache()


class TestMuatSimpan(BasisKonfig):
    def test_berkas_belum_ada_memberi_bawaan(self):
        self.assertEqual(konfigurasi.ambil("tema"), "gelap")
        self.assertEqual(konfigurasi.ambil("lebar"), 0)

    def test_bolak_balik_simpan_muat(self):
        konfigurasi.pasang("nama", "Budi")
        konfigurasi.lupakan_cache()
        self.assertEqual(konfigurasi.ambil("nama"), "Budi")

    def test_berkas_rusak_tidak_bikin_crash(self):
        self.tulis("{ini bukan json")
        self.assertEqual(konfigurasi.ambil("tema"), "gelap")

    def test_berkas_berisi_list(self):
        self.tulis([1, 2, 3])
        self.assertEqual(konfigurasi.ambil("tema"), "gelap")

    def test_kunci_asing_diabaikan(self):
        self.tulis({"kunci_ngawur": 123, "nama": "Ani"})
        self.assertEqual(konfigurasi.ambil("nama"), "Ani")
        self.assertIsNone(konfigurasi.muat().get("kunci_ngawur"))

    def test_penulisan_atomik_tidak_meninggalkan_sampah(self):
        konfigurasi.pasang("nama", "X")
        sisa = [f for f in os.listdir(self.dir.name) if f.endswith(".tmp")]
        self.assertEqual(sisa, [])


class TestValidasiNilai(BasisKonfig):
    def test_tema_tak_dikenal_jatuh_ke_bawaan(self):
        self.tulis({"tema": "neon-ungu"})
        self.assertEqual(konfigurasi.ambil("tema"), "gelap")

    def test_angka_di_bawah_minimum_dijepit(self):
        self.tulis({"lebar": 10})
        self.assertEqual(konfigurasi.ambil("lebar"), 52)

    def test_angka_di_atas_maksimum_dijepit(self):
        self.tulis({"lebar": 9999})
        self.assertEqual(konfigurasi.ambil("lebar"), 140)

    def test_nol_tetap_berarti_otomatis(self):
        self.tulis({"lebar": 0})
        self.assertEqual(konfigurasi.ambil("lebar"), 0)

    def test_angka_bertipe_teks_ditolak_dengan_rapi(self):
        self.tulis({"detik_per_soal": "banyak"})
        self.assertEqual(konfigurasi.ambil("detik_per_soal"), 25)

    def test_sakelar_selalu_bool(self):
        self.tulis({"sorot_sintaks": "ya"})
        self.assertIs(konfigurasi.ambil("sorot_sintaks"), True)
        self.tulis({"sorot_sintaks": 0})
        self.assertIs(konfigurasi.ambil("sorot_sintaks"), False)

    def test_setiap_opsi_punya_keterangan_dan_bawaan_yang_sah(self):
        for o in konfigurasi.daftar_opsi():
            with self.subTest(opsi=o.kunci):
                self.assertTrue(o.label.strip())
                self.assertTrue(o.keterangan.strip())
                self.assertEqual(o.bersihkan(o.bawaan), o.bawaan)
                self.assertTrue(str(o.tampil(o.bawaan)).strip())

    def test_setiap_opsi_pilihan_punya_daftar_nilai(self):
        for o in konfigurasi.daftar_opsi():
            if o.jenis == "pilihan":
                with self.subTest(opsi=o.kunci):
                    self.assertTrue(o.pilihan)
                    self.assertIn(o.bawaan, [n for n, _ in o.pilihan])


class TestTerapkan(BasisKonfig):
    def test_tema_diterapkan_ke_modul_tema(self):
        konfigurasi.pasang("tema", "terang")
        self.assertEqual(tema.tema_aktif(), "terang")

    def test_warna_mati_mematikan_warna(self):
        konfigurasi.pasang("warna", "mati")
        self.assertFalse(tema.berwarna())

    def test_warna_penuh_dipaksa(self):
        konfigurasi.pasang("warna", "penuh")
        self.assertEqual(tema.kedalaman_aktif(), tema.WARNA_PENUH)

    def test_kembalikan_bawaan(self):
        konfigurasi.pasang("nama", "Budi")
        konfigurasi.pasang("tema", "terang")
        konfigurasi.kembalikan_bawaan()
        self.assertEqual(konfigurasi.ambil("nama"), "")
        self.assertEqual(tema.tema_aktif(), "gelap")

    def test_pasang_kunci_tak_dikenal_ditolak(self):
        self.assertFalse(konfigurasi.pasang("tidak_ada", 1))


class TestTema(unittest.TestCase):
    def test_semua_tema_mendefinisikan_semua_peran(self):
        for nama in tema.TEMA:
            with self.subTest(tema=nama):
                for peran in tema.PERAN:
                    self.assertIn(peran, tema.TEMA[nama]["warna"])

    def test_setiap_peran_menghasilkan_kode_ansi_yang_sah(self):
        asli = tema.kedalaman_aktif()
        try:
            for nama in tema.TEMA:
                tema.pakai_tema(nama)
                for kedalaman in (tema.WARNA_16, tema.WARNA_256, tema.WARNA_PENUH):
                    tema.pakai_kedalaman(kedalaman)
                    for peran in tema.PERAN:
                        kode = tema.w(peran)
                        if kode:
                            self.assertTrue(kode.startswith("\033["), (nama, peran))
                            self.assertTrue(kode.endswith("m"), (nama, peran))
        finally:
            tema.pakai_kedalaman(asli)
            tema.pakai_tema("gelap")

    def test_tanpa_warna_mengembalikan_teks_apa_adanya(self):
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            self.assertEqual(tema.cat("halo", "galat", tema.TEBAL), "halo")
        finally:
            tema.pakai_kedalaman(asli)

    def test_cat_selalu_menutup_dengan_reset(self):
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.WARNA_PENUH)
            self.assertTrue(tema.cat("x", "galat").endswith(tema.RESET))
        finally:
            tema.pakai_kedalaman(asli)

    def test_tema_tak_dikenal_ditolak(self):
        self.assertFalse(tema.pakai_tema("tidak-ada"))

    def test_no_color_dihormati(self):
        import os as _os
        from unittest import mock as _mock
        with _mock.patch.dict(_os.environ, {"NO_COLOR": "1"}):
            self.assertEqual(tema.deteksi_kedalaman(), tema.TANPA_WARNA)


if __name__ == "__main__":
    unittest.main(verbosity=2)
