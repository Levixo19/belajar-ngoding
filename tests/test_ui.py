"""Tes helper tampilan dan smoke test alur aplikasi lewat stdin palsu."""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest import mock

from layar import utils


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
        from pelajar import progress
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")

    def tearDown(self):
        from pelajar import progress
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

    def test_kata_kunci_layar_sudah_muncul_sebelum_navigasi(self):
        """Penjaga untuk tes-tes di bawah.

        Menu utama sendiri sudah mencetak kata "MATERI", "BADGE", "BOOKMARK",
        dan seterusnya. Meng-assert kata itu -- yang dilakukan versi lama --
        membuktikan nol: semua tes navigasi tetap hijau walau submenunya tidak
        pernah terbuka. Tes ini merekam kenyataan itu supaya tidak terulang.
        """
        teks = self._jalankan_menu(["k"]).upper()
        for kata in ("MATERI", "BADGE", "BOOKMARK", "LANJUTKAN", "TENTANG"):
            self.assertIn(kata, teks)

    def test_masuk_bahasa_baca_materi_benar_benar_mencatat_progres(self):
        import main
        from pelajar import progress as p
        # Menu "1" memilih bahasa PERTAMA di daftar, jadi kunci progresnya
        # harus diturunkan dari bahasa itu juga — bukan dari nama yang
        # kebetulan benar hari ini. Versi sebelumnya menulis "java_materi"
        # sebagai literal, dan pecah begitu HTML masuk ke urutan pertama.
        #
        # Empat kali "1", bukan tiga: bahasa -> Materi -> BAB 1 -> materi 1.
        # Layar bab adalah tingkat tambahan yang sengaja ada, dan tes berikutnya
        # menjaga supaya ia tidak diam-diam hilang lagi — kalau tingkat itu
        # dihapus, tes ini akan membuka materi KEDUA dan tetap hijau, jadi ia
        # tidak bisa menjaga dirinya sendiri.
        bahasa = main.LANGUAGES[0]
        judul = bahasa["materials"][0]["title"]
        self._jalankan_menu(["1", "1", "1", "1"] + [""] * 40
                            + ["0", "0", "0", "0", "k"])
        dibaca = p.load_progress()["materi_dibaca"]
        self.assertIn(p.kunci(f"{bahasa['key']}_materi", judul), dibaca)

    def test_daftar_materi_lewat_layar_bab_dan_bab_terkunci_terlihat(self):
        """Bab bukan sekadar label: ia satu layar tersendiri sebelum materinya.

        Yang diuji sekaligus dua hal yang gampang hilang tanpa disadari:
        layar babnya sendiri, dan kenyataan bahwa bab yang MASIH TERKUNCI tetap
        ditampilkan. Menyembunyikan yang terkunci akan membuat layar ini tampak
        normal — dan menghapus satu-satunya alasan bab ini ada, yaitu memberi
        tahu apa yang sedang menanti di depan.
        """
        import main
        from pelajar import bab as modul_bab
        bahasa = main.LANGUAGES[0]
        daftar = modul_bab.status(bahasa, buka_semua=False)
        self.assertGreater(len(daftar), 1, "bahasa pertama harus punya >1 bab")

        teks = self._jalankan_menu(["1", "1"] + ["0", "0", "k"])
        self.assertIn(daftar[0]["judul"], teks)

        # Judul bab DIPOTONG kalau tidak muat selebar terminal, jadi yang
        # dicari cuma awalannya. Menuntut judul utuh membuat tes ini gagal
        # bukan karena babnya hilang, melainkan karena judulnya panjang —
        # persis kesalahan yang bikin orang berhenti percaya pada tesnya.
        terkunci = next(b for b in daftar if b["status"] == modul_bab.TERKUNCI)
        self.assertIn(terkunci["judul"][:18], teks)
        self.assertIn(f"Bab {terkunci['nomor']}", teks)
        self.assertIn("terkunci", teks.lower())

    def test_menu_badge_menampilkan_deskripsi_badge(self):
        # "Baca 25 materi" hanya muncul di layar daftar badge.
        teks = self._jalankan_menu(["s", "2", "", "0", "k"])
        self.assertIn("Baca 25 materi", teks)

    def test_menu_tentang_menampilkan_lokasi_berkas(self):
        from pelajar import konfigurasi
        teks = self._jalankan_menu(["t", "", "k"])
        self.assertIn(konfigurasi.BERKAS, teks)

    def test_bookmark_kosong_memberi_petunjuk(self):
        teks = self._jalankan_menu(["b", "", "k"])
        self.assertIn("tekan [b] untuk menyimpannya", teks)

    def test_lanjutkan_tanpa_riwayat_memberi_pesan_khusus(self):
        teks = self._jalankan_menu(["l", "", "k"])
        self.assertIn("Belum ada riwayat", teks)

    def test_pencarian_global_menampilkan_jumlah_hasil(self):
        teks = self._jalankan_menu(["c", "perulangan", "0", "k"])
        self.assertRegex(teks, r"\d+ dari \d+ hasil")

    def test_pencarian_tanpa_hasil(self):
        teks = self._jalankan_menu(["c", "zzzqqqxxx", "", "k"])
        self.assertIn("Tidak ada", teks)

    def test_pilihan_tidak_valid_tidak_bikin_crash(self):
        teks = self._jalankan_menu(["999", "abc", "-1", "k"])
        self.assertIn("tidak valid", teks.lower())

    def test_digit_unicode_tidak_menjatuhkan_menu(self):
        teks = self._jalankan_menu(["\u00b2", "k"])
        self.assertIn("Terima kasih", teks)

    def test_stdin_habis_langsung_keluar(self):
        """Regresi: dulu EOF membuat menu utama berputar & membanjiri terminal."""
        import main
        with mock.patch("builtins.input", side_effect=EOFError):
            with mock.patch.object(utils, "clear", lambda: None):
                with redirect_stdout(io.StringIO()) as keluar:
                    main.main_menu()
        teks = keluar.getvalue()
        self.assertIn("Terima kasih", teks)
        self.assertLess(len(teks), 200_000, "output membengkak seperti loop tak berujung")

    def test_menu_saran_menampilkan_alasan(self):
        teks = self._jalankan_menu(["n", "0", "k"])
        self.assertIn("LANGKAH BERIKUTNYA", teks.upper())

    def test_menu_pengaturan_menampilkan_lokasi_berkas(self):
        from pelajar import konfigurasi
        teks = self._jalankan_menu(["p", "0", "k"])
        self.assertIn(konfigurasi.BERKAS, teks)


class TestAskAtauEof(unittest.TestCase):
    def test_eof_mengembalikan_none(self):
        with mock.patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(io.StringIO()):
                self.assertIsNone(utils.ask_atau_eof("> "))

    def test_enter_kosong_bukan_eof(self):
        with mock.patch("builtins.input", return_value=""):
            self.assertEqual(utils.ask_atau_eof("> "), "")


class TestAngkaPilihan(unittest.TestCase):
    def test_angka_sah(self):
        self.assertEqual(utils.angka_pilihan("3", 5), 3)

    def test_di_luar_rentang(self):
        self.assertIsNone(utils.angka_pilihan("0", 5))
        self.assertIsNone(utils.angka_pilihan("6", 5))

    def test_bukan_angka(self):
        self.assertIsNone(utils.angka_pilihan("abc", 5))
        self.assertIsNone(utils.angka_pilihan("", 5))
        self.assertIsNone(utils.angka_pilihan("-1", 5))

    def test_digit_unicode_ditolak_bukan_meledak(self):
        """'\u00b2'.isdigit() True tapi int('\u00b2') melempar ValueError."""
        for aneh in ("\u00b2", "\u00b3", "\u00b9", "\uff11"):
            with self.subTest(masukan=aneh):
                self.assertIsNone(utils.angka_pilihan(aneh, 5))


class TestAskChoiceTahanBanting(unittest.TestCase):
    def test_eof_saat_allow_back_mati_tetap_kembali(self):
        """Regresi loop tak berujung di menu utama."""
        with mock.patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(io.StringIO()):
                hasil = utils.ask_choice("p", ["A", "B"], allow_back=False)
        self.assertEqual(hasil, 0)

    def test_masukan_ngawur_berulang_akhirnya_menyerah(self):
        with mock.patch("builtins.input", side_effect=["zz"] * 50):
            with redirect_stdout(io.StringIO()) as keluar:
                hasil = utils.ask_choice("p", ["A"], allow_back=False)
        self.assertEqual(hasil, 0)
        self.assertIn("Terlalu banyak", keluar.getvalue())

    def test_digit_unicode_tidak_bikin_crash(self):
        with mock.patch("builtins.input", side_effect=["\u00b2", "1"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(utils.ask_choice("p", ["A"]), 1)


class TestAskTimed(unittest.TestCase):
    def test_detik_nol_berperilaku_seperti_ask(self):
        with mock.patch("builtins.input", return_value="7"):
            self.assertEqual(utils.ask_timed("> ", 0), ("7", False))

    def test_eof_dilaporkan_sebagai_none(self):
        """Regresi: EOF dulu dikembalikan sebagai "" dan bikin kuis loop selamanya."""
        with mock.patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(io.StringIO()):
                jawab, habis = utils.ask_timed("> ", 0)
        self.assertIsNone(jawab)
        self.assertFalse(habis)

    def test_stdin_palsu_jatuh_ke_jalur_cadangan(self):
        # StringIO tidak punya fileno() yang sah -> harus memakai input() biasa.
        with mock.patch("sys.stdin", io.StringIO("5\n")):
            with mock.patch("builtins.input", return_value="5"):
                jawab, habis = utils.ask_timed("> ", 30)
        self.assertEqual(jawab, "5")
        self.assertFalse(habis)


class TestStripAnsiTahanBanting(unittest.TestCase):
    def test_escape_bukan_sgr_tidak_memakan_teks(self):
        """Regresi: versi lama memakan sampai huruf 'm' pertama di kata biasa."""
        self.assertEqual(utils.strip_ansi("\033[2Jhalo mantap"), "halo mantap")

    def test_osc_dibuang_utuh(self):
        self.assertEqual(utils.strip_ansi("\033]0;judul\007teks"), "teks")

    def test_escape_menggantung_tidak_membuang_sisa(self):
        self.assertEqual(utils.strip_ansi("halo\033["), "halo")

    def test_gerakan_kursor(self):
        self.assertEqual(utils.strip_ansi("a\033[10;20Hb"), "ab")

    def test_teks_polos_tidak_berubah(self):
        for teks in ("", "biasa saja", "100% aman", "m m m"):
            self.assertEqual(utils.strip_ansi(teks), teks)


class TestLebarDanPotong(unittest.TestCase):
    def test_lebar_selalu_dalam_batas(self):
        self.assertGreaterEqual(utils.lebar(), utils.LEBAR_MIN)
        self.assertLessEqual(utils.lebar(), utils.LEBAR_MAKS)

    def test_tinggi_halaman_masuk_akal(self):
        self.assertGreaterEqual(utils.tinggi_halaman(), 5)

    def test_potong_menghormati_batas(self):
        self.assertEqual(utils.potong("halo", 10), "halo")
        self.assertEqual(len(utils.potong("a" * 50, 10)), 10)

    def test_potong_mengabaikan_kode_warna_saat_menghitung(self):
        with mock.patch.object(utils, "COLORS_ON", True):
            berwarna = utils.paint("12345", utils.C.RED)
        self.assertEqual(utils.potong(berwarna, 10), berwarna)

    def test_pusatkan_menghasilkan_lebar_tepat(self):
        for teks in ("", "pendek", "x" * 200):
            self.assertEqual(utils.visible_len(utils.pusatkan(teks, 40)), 40)

    def test_header_judul_panjang_tidak_merusak_bingkai(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            with redirect_stdout(io.StringIO()) as keluar:
                utils.header("K" * 200, "S" * 200)
        for baris in keluar.getvalue().splitlines():
            self.assertLessEqual(len(baris), utils.lebar())


class TestBungkusBaris(unittest.TestCase):
    def test_baris_pendek_dibiarkan(self):
        self.assertEqual(utils.bungkus_baris("halo", 40, "  "), ["  halo"])

    def test_baris_panjang_dipecah(self):
        baris = utils.bungkus_baris("kata " * 40, 40, "  ")
        self.assertGreater(len(baris), 1)
        for b in baris:
            self.assertLessEqual(len(b), 40)

    def test_baris_kosong_dipertahankan(self):
        self.assertEqual(utils.bungkus_baris("", 40, "  "), [""])
        self.assertEqual(utils.bungkus_baris("   ", 40, "  "), [""])

    def test_tidak_ada_kata_yang_hilang(self):
        teks = "satu dua tiga empat lima enam tujuh delapan sembilan sepuluh " * 3
        gabung = " ".join(b.strip() for b in utils.bungkus_baris(teks, 30, "  "))
        self.assertEqual(gabung.split(), teks.split())


class TestSorotKata(unittest.TestCase):
    def test_tanpa_warna_teks_tidak_berubah(self):
        from inti import tema
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            self.assertEqual(utils.sorot_kata("halo dunia", "dunia"), "halo dunia")
        finally:
            tema.pakai_kedalaman(asli)

    def test_kata_kosong_aman(self):
        self.assertEqual(utils.sorot_kata("halo", ""), "halo")

    def test_semua_kemunculan_disorot(self):
        from inti import tema
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.WARNA_PENUH)
            hasil = utils.sorot_kata("aku aku aku", "aku")
            self.assertEqual(utils.strip_ansi(hasil), "aku aku aku")
            self.assertEqual(hasil.count(tema.RESET), 3)
        finally:
            tema.pakai_kedalaman(asli)

    def test_tidak_membedakan_huruf_besar_kecil(self):
        from inti import tema
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.WARNA_PENUH)
            hasil = utils.sorot_kata("Halo HALO halo", "halo")
            self.assertEqual(utils.strip_ansi(hasil), "Halo HALO halo")
            self.assertEqual(hasil.count(tema.RESET), 3)
        finally:
            tema.pakai_kedalaman(asli)


class TestKotak(unittest.TestCase):
    def test_lebar_setiap_baris_sama(self):
        with mock.patch.object(utils, "COLORS_ON", False):
            baris = utils.kotak(["satu", "dua panjang sekali " * 5], judul="UJI")
        lebar = {utils.visible_len(b) for b in baris}
        self.assertEqual(len(lebar), 1, f"lebar tidak seragam: {lebar}")

    def test_isi_kosong_tetap_membentuk_bingkai(self):
        baris = utils.kotak([])
        self.assertEqual(len(baris), 2)


class TestPaginateNavigasiBaru(unittest.TestCase):
    def _jalankan(self, baris, masukan, chunk=5):
        with mock.patch("builtins.input", side_effect=masukan):
            with mock.patch.object(utils, "clear", lambda: None):
                with redirect_stdout(io.StringIO()) as keluar:
                    hasil = utils.paginate("judul", baris, chunk_size=chunk)
        return hasil, keluar.getvalue()

    def test_a_kembali_ke_halaman_pertama(self):
        baris = [f"baris{i}" for i in range(20)]
        _, teks = self._jalankan(baris, ["", "", "a", "q"], chunk=5)
        self.assertGreaterEqual(teks.count("baris0"), 2)

    def test_eof_dianggap_berhenti_lebih_awal(self):
        baris = [f"b{i}" for i in range(20)]
        with mock.patch("builtins.input", side_effect=EOFError):
            with mock.patch.object(utils, "clear", lambda: None):
                with redirect_stdout(io.StringIO()):
                    hasil = utils.paginate("judul", baris, chunk_size=5)
        self.assertFalse(hasil)



if __name__ == "__main__":
    unittest.main(verbosity=2)


class TestHeatmap(unittest.TestCase):
    """Petak aktivitas harus SELALU memuat hari ini, apa pun hari pertamanya."""

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        from pelajar import progress
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")

    def tearDown(self):
        from pelajar import progress
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        self.dir.cleanup()

    def test_aktivitas_hari_ini_selalu_muncul(self):
        import main
        from pelajar import progress
        from inti import tema
        from datetime import date

        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            for _ in range(10):
                progress.record_material_read("java_materi", f"M{_}")
            data = progress.load_progress()
            self.assertGreater(progress.xp_hari_ini(data), 0)

            baris = main.baris_heatmap(data)
            hari_ini = date.today().weekday()
            # Baris 0 = Senin; petaknya ada di indeks weekday hari ini + 1
            # (baris pertama adalah judul).
            self.assertNotEqual(baris[hari_ini + 1].strip().split()[-1], "",
                                "baris hari ini kosong")
            gabung = "".join(baris)
            self.assertIn(main._BLOK_HEATMAP[3], gabung,
                          "aktivitas hari ini tidak terlihat di heatmap")
        finally:
            tema.pakai_kedalaman(asli)

    def test_jumlah_baris_selalu_sembilan(self):
        import main
        from pelajar import progress
        baris = main.baris_heatmap(progress.load_progress())
        self.assertEqual(len(baris), 9)   # judul + 7 hari + keterangan

    def test_lebar_setiap_baris_hari_sama(self):
        import main
        from pelajar import progress
        from inti import tema
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            baris = main.baris_heatmap(progress.load_progress())[1:8]
            self.assertEqual(len({len(b) for b in baris}), 1)
        finally:
            tema.pakai_kedalaman(asli)
