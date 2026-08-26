"""Tes helper tampilan dan smoke test alur aplikasi lewat stdin palsu."""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest import mock

import utils


class TestPewarnaan(unittest.TestCase):
    def test_paint_menambahkan_reset(self):
        with mock.patch.object(utils, "COLORS_ON", True):
            hasil = utils.paint("halo", utils.C.RED)
            self.assertTrue(hasil.startswith(utils.C.RED))
            self.assertTrue(hasil.endswith(utils.C.RESET))

    def test_paint_tanpa_warna_mengembalikan_apa_adanya(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            self.assertEqual(utils.paint("halo", utils.C.RED), "halo")

    def test_paint_tanpa_argumen_warna(self):
        with mock.patch.object(utils, "COLORS_ON", True):
            self.assertEqual(utils.paint("halo"), "halo")

    def test_strip_ansi_membuang_kode_warna(self):
        with mock.patch.object(utils, "COLORS_ON", True):
            berwarna = utils.paint("halo", utils.C.RED, utils.C.BOLD)
        self.assertEqual(utils.strip_ansi(berwarna), "halo")

    def test_visible_len_mengabaikan_warna(self):
        with mock.patch.object(utils, "COLORS_ON", True):
            berwarna = utils.paint("12345", utils.C.GREEN)
        self.assertEqual(utils.visible_len(berwarna), 5)

    def test_strip_ansi_pada_teks_polos(self):
        self.assertEqual(utils.strip_ansi("tanpa warna"), "tanpa warna")

    def test_no_color_dihormati(self):
        with mock.patch.dict(os.environ, {"NO_COLOR": "1"}):
            self.assertFalse(utils.supports_color())


class TestProgressBar(unittest.TestCase):
    def test_kosong_dan_penuh(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            self.assertEqual(utils.bar(0, 10, 10), "-" * 10)
            self.assertEqual(utils.bar(10, 10, 10), "#" * 10)

    def test_setengah(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            self.assertEqual(utils.bar(5, 10, 10), "#" * 5 + "-" * 5)

    def test_total_nol_tidak_membagi_nol(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            self.assertEqual(utils.bar(0, 0, 8), "-" * 8)

    def test_nilai_di_luar_batas_dijepit(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            self.assertEqual(utils.bar(99, 10, 6), "#" * 6)
            self.assertEqual(utils.bar(-5, 10, 6), "-" * 6)

    def test_lebar_selalu_tetap(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            for done in range(0, 21):
                self.assertEqual(len(utils.bar(done, 20, 15)), 15)


class TestAsk(unittest.TestCase):
    def test_membaca_dan_memangkas_spasi(self):
        with mock.patch("builtins.input", return_value="  jawab  "):
            self.assertEqual(utils.ask("> "), "jawab")

    def test_eof_mengembalikan_default(self):
        with mock.patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(utils.ask("> ", "bawaan"), "bawaan")


class TestAskChoice(unittest.TestCase):
    def _pilih(self, masukan, **kwargs):
        with mock.patch("builtins.input", side_effect=masukan):
            with redirect_stdout(io.StringIO()):
                return utils.ask_choice("prompt", ["A", "B", "C"], **kwargs)

    def test_memilih_nomor_valid(self):
        self.assertEqual(self._pilih(["2"]), 2)

    def test_nol_berarti_kembali(self):
        self.assertEqual(self._pilih(["0"]), 0)

    def test_mengulang_saat_input_tidak_valid(self):
        self.assertEqual(self._pilih(["abc", "99", "-1", "3"]), 3)

    def test_opsi_tambahan_berupa_huruf(self):
        self.assertEqual(self._pilih(["c"], extra={"c": "Cari"}), "c")

    def test_huruf_besar_pada_opsi_tambahan_tetap_dikenali(self):
        self.assertEqual(self._pilih(["C"], extra={"c": "Cari"}), "c")

    def test_nol_ditolak_saat_allow_back_mati(self):
        self.assertEqual(self._pilih(["0", "1"], allow_back=False), 1)

    def test_eof_dianggap_kembali(self):
        with mock.patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(utils.ask_choice("p", ["A"]), 0)


class TestConfirm(unittest.TestCase):
    def test_ya(self):
        with mock.patch("builtins.input", return_value="y"):
            self.assertTrue(utils.confirm("yakin?"))

    def test_tidak(self):
        with mock.patch("builtins.input", return_value="n"):
            self.assertFalse(utils.confirm("yakin?", default=True))

    def test_kosong_memakai_default(self):
        with mock.patch("builtins.input", return_value=""):
            self.assertTrue(utils.confirm("yakin?", default=True))
            self.assertFalse(utils.confirm("yakin?", default=False))


class TestPaginate(unittest.TestCase):
    def _jalankan(self, baris, masukan, chunk=5):
        with mock.patch("builtins.input", side_effect=masukan):
            with mock.patch.object(utils, "clear", lambda: None):
                with redirect_stdout(io.StringIO()) as keluar:
                    hasil = utils.paginate("judul", baris, chunk_size=chunk)
        return hasil, keluar.getvalue()

    def test_daftar_kosong_langsung_selesai(self):
        hasil, _ = self._jalankan([], [])
        self.assertTrue(hasil)

    def test_satu_halaman_selesai_dengan_enter(self):
        hasil, teks = self._jalankan(["a", "b"], [""])
        self.assertTrue(hasil)
        self.assertIn("a", teks)

    def test_maju_sampai_halaman_terakhir(self):
        baris = [str(i) for i in range(12)]
        hasil, teks = self._jalankan(baris, ["", "", ""], chunk=5)
        self.assertTrue(hasil)
        self.assertIn("11", teks, "halaman terakhir harus tampil")

    def test_q_menghentikan_lebih_awal(self):
        baris = [str(i) for i in range(20)]
        hasil, teks = self._jalankan(baris, ["q"], chunk=5)
        self.assertFalse(hasil)
        self.assertNotIn("19", teks)

    def test_p_kembali_ke_halaman_sebelumnya(self):
        baris = [f"baris{i}" for i in range(15)]
        # maju, maju, mundur, lalu keluar
        _, teks = self._jalankan(baris, ["", "", "p", "q"], chunk=5)
        self.assertGreaterEqual(teks.count("baris5"), 2,
                                "halaman kedua harus tampil dua kali")

    def test_p_di_halaman_pertama_tidak_error(self):
        baris = [str(i) for i in range(10)]
        hasil, _ = self._jalankan(baris, ["p", "", ""], chunk=5)
        self.assertTrue(hasil)

    def test_semua_baris_tampil_kalau_dibaca_sampai_habis(self):
        baris = [f"x{i}" for i in range(23)]
        _, teks = self._jalankan(baris, [""] * 5, chunk=5)
        for b in baris:
            self.assertIn(b, teks)


class TestWrap(unittest.TestCase):
    def test_memotong_pada_lebar_tertentu(self):
        teks = "kata " * 40
        hasil = utils.wrap(teks, width=30)
        for baris in hasil.split("\n"):
            self.assertLessEqual(len(baris), 30)

    def test_menjaga_indentasi(self):
        hasil = utils.wrap("halo dunia", width=40, indent="    ")
        self.assertTrue(hasil.startswith("    "))


class TestSmokeAplikasi(unittest.TestCase):
    """Menjalankan menu utama dengan input palsu; tidak boleh ada exception."""

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        import progress
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")

    def tearDown(self):
        import progress
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        self.dir.cleanup()

    def _jalankan_menu(self, masukan):
        import main
        with mock.patch("builtins.input", side_effect=list(masukan) + ["k"] * 40):
            with mock.patch.object(utils, "clear", lambda: None):
                with redirect_stdout(io.StringIO()) as keluar:
                    main.main_menu()
        return keluar.getvalue()

    def test_menu_utama_lalu_keluar(self):
        teks = self._jalankan_menu(["k"])
        self.assertIn("Terima kasih", teks)

    def test_masuk_bahasa_baca_materi_lalu_keluar(self):
        # Bahasa 1 > Materi > materi 1 > baca sampai habis > kembali x3 > keluar
        teks = self._jalankan_menu(
            ["1", "1", "1"] + [""] * 30 + ["0", "0", "0", "k"]
        )
        self.assertIn("MATERI", teks.upper())

    def test_menu_statistik_dan_badge(self):
        teks = self._jalankan_menu(["s", "1", "", "2", "", "0", "k"])
        self.assertIn("BADGE", teks.upper())

    def test_menu_tentang(self):
        teks = self._jalankan_menu(["t", "", "k"])
        self.assertIn("TENTANG", teks.upper())

    def test_bookmark_kosong(self):
        teks = self._jalankan_menu(["b", "", "k"])
        self.assertIn("BOOKMARK", teks.upper())

    def test_lanjutkan_tanpa_riwayat(self):
        teks = self._jalankan_menu(["l", "", "k"])
        self.assertIn("LANJUTKAN", teks.upper())

    def test_pencarian_global(self):
        teks = self._jalankan_menu(["c", "perulangan", "0", "k"])
        self.assertIn("HASIL PENCARIAN", teks.upper())

    def test_pencarian_tanpa_hasil(self):
        teks = self._jalankan_menu(["c", "zzzqqqxxx", "", "k"])
        self.assertIn("Tidak ada", teks)

    def test_pilihan_tidak_valid_tidak_bikin_crash(self):
        teks = self._jalankan_menu(["999", "abc", "-1", "k"])
        self.assertIn("tidak valid", teks.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
