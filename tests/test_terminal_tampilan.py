"""Tes tampilan terminal: menu panah bermultibaris, kuis yang dibungkus, dan CLI.

Tiga cacat yang ditemukan audit terminal, masing-masing dengan pagarnya:

* Menu panah menumpuk saat opsinya bermultibaris. Penggambar ulang naik
  sebanyak jumlah OPSI padahal yang tercetak jumlah BARIS, jadi tiap tekanan
  panah meninggalkan sisa blok lama di atas blok baru ("Langkah berikutnya",
  hasil Cari, Pustaka). `potong()` juga mengukur seluruh string sekaligus,
  sehingga baris alasan terpangkas jadi "materi berik…".
* Penjelasan dan opsi kuis dicetak sebaris penuh: 846 dari 968 penjelasan
  lebih lebar dari 80 kolom, dan terminal melipatnya di tengah kata.
* Galat argparse berbahasa Inggris, tanpa tebakan untuk salah ketik, dan
  `--impor` lewat CLI menimpa progres tanpa bertanya.
"""

import io
import os
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

from inti import tema
from layar import navigasi, quiz, utils
from pelajar import konfigurasi, progress

import main


# --------------------------------------------------------------- emulator VT

_POLA_CSI = re.compile(r"\x1b\[([0-9;?]*)([A-Za-z])")


def _layar_vt(data, baris, kolom):
    """Emulator terminal sekecil mungkin: CR/LF, ESC[nA, ESC[2K, SGR diabaikan.

    Cukup untuk menjawab satu pertanyaan: sesudah semua gambar ulang, apa
    yang SUNGGUH tertinggal di layar. Baris yang melebihi `kolom` melipat,
    persis seperti terminal sungguhan.
    """
    layar = [[" "] * kolom for _ in range(baris)]
    r = c = 0

    def turun():
        nonlocal r
        if r == baris - 1:
            layar.pop(0)
            layar.append([" "] * kolom)
        else:
            r += 1

    i = 0
    while i < len(data):
        ch = data[i]
        if ch == "\x1b":
            m = _POLA_CSI.match(data, i)
            if m:
                arg, cmd = m.group(1), m.group(2)
                if cmd == "A":
                    r = max(0, r - int(arg or 1))
                elif cmd == "K" and arg == "2":
                    layar[r] = [" "] * kolom
                i = m.end()
                continue
            i += 1
            continue
        if ch == "\r":
            c = 0
        elif ch == "\n":
            turun()
            c = 0
        else:
            if c >= kolom:
                turun()
                c = 0
            layar[r][c] = ch
            c += 1
        i += 1
    return ["".join(b).rstrip() for b in layar]


def _opsi_saran(n=4):
    """Opsi berbentuk persis seperti `menu_saran` di main.py: dua baris."""
    return [
        f"{tema.cat('materi:', 'aksen')} Python - {k + 1}. Judul Materi Nomor {k + 1}\n"
        f"       {tema.cat('materi berikutnya di bahasa yang sedang kamu pelajari', 'redup')}"
        for k in range(n)
    ]


class BasisLayarTetap(unittest.TestCase):
    """Terminal 60x40 dengan warna menyala, terlepas dari setelan pemiliknya.

    `lebar()` membaca setelan "lebar" dari berkas konfigurasi pengguna, jadi
    tanpa ditambal hasil tes ini bergantung pada mesin siapa yang
    menjalankannya.
    """

    KOLOM = 60
    BARIS = 40

    def setUp(self):
        for target, nilai in (
            ("_ukuran_terminal", lambda: os.terminal_size((self.KOLOM, self.BARIS))),
            ("lebar", lambda: self.KOLOM - 2),
            ("COLORS_ON", True),
        ):
            p = mock.patch.object(utils, target, nilai)
            p.start()
            self.addCleanup(p.stop)


# ------------------------------------------------------------------ potong()

class TestPotongPerBaris(unittest.TestCase):
    def test_teks_bermultibaris_dipotong_per_baris(self):
        hasil = utils.potong("pendek\n" + "x" * 40, 10)
        baris = hasil.split("\n")
        self.assertEqual(len(baris), 2, "jumlah baris tidak boleh berubah")
        self.assertEqual(baris[0], "pendek", "baris pendek tidak ikut dipotong")
        self.assertEqual(utils.visible_len(baris[1]), 10)

    def test_baris_kedua_tidak_memakan_baris_pertama(self):
        """Gejala aslinya: alasan saran tinggal "materi berik…"."""
        teks = "materi: HTML - 1. Apa Itu HTML\n       materi berikutnya di bahasa ini"
        hasil = utils.potong(teks, 60)
        self.assertEqual(hasil, teks)

    def test_kode_warna_dipertahankan_dan_ditutup(self):
        with mock.patch.object(utils, "COLORS_ON", True):
            berwarna = "awal " + utils.paint("x" * 40, utils.C.RED) + " akhir"
        hasil = utils.potong(berwarna, 12)
        self.assertEqual(utils.visible_len(hasil), 12)
        self.assertIn(utils.C.RED, hasil, "warna di dalam baris tidak boleh dibuang")
        self.assertTrue(hasil.endswith("\033[0m"), "warna harus ditutup di ujung")
        self.assertEqual(utils.strip_ansi(hasil), "awal " + "x" * 6 + "…")

    def test_teks_polos_tidak_diberi_kode_penutup(self):
        self.assertEqual(utils.potong("a" * 50, 10), "a" * 9 + "…")


# ------------------------------------------------------------- menu panah

class TestBarisMenu(BasisLayarTetap):
    def test_satu_elemen_satu_baris_layar(self):
        opsi = _opsi_saran(3)
        baris = utils._baris_menu(opsi, {"x": "Aksi tambahan"}, True, "Kembali", 0, "")
        for b in baris:
            self.assertNotIn("\n", b)
            self.assertLessEqual(utils.visible_len(b), utils.lebar_menu())
        # 3 opsi x 2 baris + 1 extra + "Kembali" + petunjuk
        self.assertEqual(len(baris), 3 * 2 + 1 + 1 + 1)

    def test_baris_lanjutan_tetap_utuh_kalau_muat(self):
        opsi = "judul\n       " + tema.cat("alasan yang muat di enam puluh kolom", "redup")
        baris = utils._baris_menu([opsi], {}, False, "", 0, "")
        self.assertEqual(utils.strip_ansi(baris[1]),
                         "       alasan yang muat di enam puluh kolom")

    def test_lebar_terkunci_lebih_lebar_dari_terminal_tidak_melipat(self):
        """Setelan `--lebar 100` di jendela 60 kolom tidak boleh membuat baris melipat."""
        with mock.patch.object(utils, "lebar", lambda: 100):
            baris = utils._baris_menu(["y" * 150], {}, True, "Kembali", 0, "")
        for b in baris:
            self.assertLess(utils.visible_len(b), self.KOLOM)

    def test_tinggi_blok_dihitung_dari_baris_sungguhan(self):
        dicatat = []

        def bisa_panah(tinggi):
            dicatat.append(tinggi)
            return False

        with mock.patch.object(utils, "_bisa_panah", bisa_panah), \
                mock.patch.object(utils, "_ask_choice_angka", return_value=0):
            utils.ask_choice("pilih", _opsi_saran(5))
        self.assertEqual(dicatat, [5 * 2 + 1 + 1])


class TestGambarUlangMenuPanah(BasisLayarTetap):
    TOMBOL = ["bawah", "bawah", "atas", "bawah", "bawah", "pilih"]

    def _jalankan(self, opsi, extra=None):
        keluar = io.StringIO()
        with mock.patch.object(utils, "_baca_tombol", side_effect=list(self.TOMBOL)), \
                redirect_stdout(keluar):
            pilih = utils._ask_choice_panah("PROMPT", opsi, True, "Kembali", extra or {})
        return pilih, keluar.getvalue()

    def test_naik_sebanyak_baris_yang_tercetak(self):
        """Tiap ESC[nA wajib sama dengan jumlah baris gambar sebelumnya."""
        _, teks = self._jalankan(_opsi_saran(4))
        badan = teks.split("PROMPT", 1)[1]
        badan = badan[badan.index("\n") + 1:]          # buang sisa baris prompt
        potongan = re.split(r"\x1b\[(\d+)A", badan)
        bingkai, naik = potongan[0::2], [int(n) for n in potongan[1::2]]
        self.assertEqual(len(naik), len(self.TOMBOL) - 1)
        for k, n in enumerate(naik):
            with self.subTest(gambar_ulang=k + 1):
                self.assertEqual(n, bingkai[k].count("\n"))

    def test_layar_akhir_tidak_menumpuk(self):
        opsi = _opsi_saran(4)
        pilih, teks = self._jalankan(opsi)
        self.assertEqual(pilih, 4)       # 0 -> 1 -> 2 -> 1 -> 2 -> 3, lalu ENTER
        layar = [b for b in _layar_vt(teks, self.BARIS, self.KOLOM) if b]
        for k in range(1, 5):
            with self.subTest(opsi=k):
                cocok = [b for b in layar if f"Judul Materi Nomor {k}" in b]
                self.assertEqual(len(cocok), 1, "\n".join(layar))
        self.assertEqual(sum("materi berikutnya" in b for b in layar), 4)
        self.assertEqual(sum(b.lstrip().startswith(">") for b in layar), 1)
        blok = utils._baris_menu(opsi, {}, True, "Kembali", 3, "")
        self.assertEqual(len(layar), 1 + len(blok), "\n".join(layar))

    def test_judul_panjang_dan_lanjutan_panjang(self):
        """Hasil Cari: baris pertama dan cuplikan sama-sama melebihi terminal."""
        opsi = [f"materi   Go          Judul ke-{k} " + "panjang " * 12 + "\n       "
                + tema.cat("...cuplikan " * 10, "redup") for k in range(3)]
        _, teks = self._jalankan(opsi)
        layar = [b for b in _layar_vt(teks, self.BARIS, self.KOLOM) if b]
        for k in range(3):
            self.assertEqual(sum(f"Judul ke-{k}" in b for b in layar), 1,
                             "\n".join(layar))


class TestPenandaKunciTidakTerpotong(BasisLayarTetap):
    """Penanda "[terkunci]" di hasil Cari tidak boleh termakan pemotongan menu."""

    def setUp(self):
        super().setUp()
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)
        for modul, nama, nilai in (
            (progress, "PROGRESS_FILE", os.path.join(self.dir.name, "p.json")),
            (progress, "PROGRESS_FILE_LAMA", os.path.join(self.dir.name, "x.json")),
            (konfigurasi, "BERKAS", os.path.join(self.dir.name, "k.json")),
        ):
            p = mock.patch.object(modul, nama, nilai)
            p.start()
            self.addCleanup(p.stop)
        konfigurasi.lupakan_cache()
        self.addCleanup(konfigurasi.lupakan_cache)

    def test_hasil_terkunci_menandai_dirinya_di_layar(self):
        dilihat = []

        def tangkap(prompt, options, **_):
            dilihat.extend(options)
            return 0

        with mock.patch.object(navigasi, "ask", return_value="goroutine"), \
                mock.patch.object(navigasi, "ask_choice", tangkap), \
                redirect_stdout(io.StringIO()):
            navigasi.cari_global(main.LANGUAGES)
        terkunci = [o for o in dilihat if "[terkunci]" in o]
        self.assertTrue(terkunci, "profil baru semestinya punya hasil terkunci")
        for o in terkunci:
            baris = utils._baris_opsi("   1. ", o, utils.lebar_menu(), ())
            self.assertIn("[terkunci]", utils.strip_ansi(baris[0]), o)


# ------------------------------------------------------------------- kuis

class TestKuisDibungkus(unittest.TestCase):
    LEBAR = 60

    def setUp(self):
        p = mock.patch.object(quiz, "lebar", lambda: self.LEBAR)
        p.start()
        self.addCleanup(p.stop)

    def _cek_baris(self, baris, awalan, asli):
        for i, b in enumerate(baris):
            # Satu-satunya yang boleh melebihi lebar: satu kata yang memang
            # lebih panjang dari barisnya (potongan kode, alamat).
            if len(b) > self.LEBAR:
                isi = b[len(awalan):] if i == 0 else b
                self.assertEqual(len(isi.split()), 1, b)
        self.assertTrue(baris[0].startswith(awalan))
        for b in baris[1:]:
            self.assertTrue(b.startswith(" " * len(awalan)), "lanjutan wajib menjorok")
        # Isinya sama dengan yang dikirim ke web: tidak ada kata yang hilang
        # atau berubah, cuma tempat patahnya.
        self.assertEqual(" ".join(b for b in baris).split()[len(awalan.split()):],
                         asli.split())

    def test_seluruh_penjelasan_dan_opsi_kurikulum(self):
        jumlah = 0
        for lang in main.LANGUAGES:
            for k in lang["quizzes"]:
                for s in k["questions"]:
                    teks = s.get("explanation", "")
                    if teks:
                        self._cek_baris(quiz._bungkus(teks, "  Penjelasan: "),
                                        "  Penjelasan: ", teks)
                        jumlah += 1
                    for i, o in enumerate(s["options"]):
                        self._cek_baris(quiz._bungkus(o, f"    {i + 1}. "),
                                        f"    {i + 1}. ", o)
        self.assertGreater(jumlah, 900)

    def test_run_quiz_tidak_mencetak_baris_melebihi_layar(self):
        panjang = ("Penjelasan ini sengaja panjang sekali supaya pasti melebihi "
                   "lebar terminal yang sempit dan harus dibungkus. ") * 3
        kuis = {"title": "Kuis Uji", "questions": [{
            "q": "Soal yang juga cukup panjang untuk dibungkus di layar sempit "
                 "enam puluh kolom?",
            "options": ["Opsi pertama yang panjang sekali sampai melewati "
                        "batas lebar layar", "Kedua"],
            "answer": 0, "explanation": panjang}]}
        keluar = io.StringIO()
        with mock.patch.object(quiz, "_baca_jawaban", return_value=("2", False, False)), \
                mock.patch.object(quiz, "record_quiz_score", return_value=[]), \
                mock.patch.object(quiz, "ask", return_value=""), \
                mock.patch.object(quiz, "press_enter"), \
                mock.patch.object(quiz, "clear"), \
                mock.patch.object(quiz, "header"), \
                redirect_stdout(keluar):
            quiz.run_quiz(kuis, "uji_kuis", acak_soal=False, acak_opsi=False)
        baris = [utils.strip_ansi(b) for b in keluar.getvalue().splitlines()]
        for b in baris:
            self.assertLessEqual(len(b), self.LEBAR, b)
        teks = " ".join(baris)
        self.assertIn(" ".join(panjang.split()), " ".join(teks.split()))
        self.assertTrue(any(b.startswith("              ") for b in baris),
                        "lanjutan penjelasan wajib menjorok di bawah isinya")


# -------------------------------------------------------------------- CLI

class TestArgumenCli(unittest.TestCase):
    def _gagal(self, argv):
        galat = io.StringIO()
        with redirect_stderr(galat), self.assertRaises(SystemExit) as ctx:
            main._argumen(argv)
        return ctx.exception.code, galat.getvalue()

    def test_salah_ketik_bahasa_diberi_tebakan(self):
        kode, teks = self._gagal(["--bahasa", "pyhton"])
        self.assertEqual(kode, 2)
        self.assertIn("Maksudmu python?", teks)
        self.assertIn("cara pakai:", teks)
        self.assertNotIn("usage", teks)
        self.assertNotIn("error:", teks)

    def test_opsi_tak_dikenal_berbahasa_indonesia_dan_ditebak(self):
        kode, teks = self._gagal(["--bahsa", "go"])
        self.assertEqual(kode, 2)
        self.assertIn("argumen tidak dikenal", teks)
        self.assertIn("Maksudmu --bahasa?", teks)
        self.assertIn("--bantuan", teks, "galat wajib menunjuk jalan keluarnya")
        self.assertNotIn("unrecognized", teks)

    def test_nilai_bukan_angka(self):
        kode, teks = self._gagal(["--lebar", "lebar"])
        self.assertEqual(kode, 2)
        self.assertIn("bilangan bulat", teks)

    def test_bahasa_diterima_lewat_key_atau_label(self):
        for masukan, key in (("python", "python"), ("PYTHON", "python"),
                             ("C++", "cpp"), ("visual basic", "vb")):
            with self.subTest(masukan=masukan):
                _, arg = main._argumen(["--bahasa", masukan])
                self.assertEqual(arg.bahasa, key)

    def test_bantuan_berbahasa_indonesia(self):
        p, _ = main._argumen([])
        teks = p.format_help()
        self.assertIn("cara pakai:", teks)
        self.assertIn("pilihan:", teks)
        self.assertNotIn("usage:", teks)
        self.assertNotIn("options:", teks)


class TestKonfirmasiImpor(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)
        self.berkas = os.path.join(self.dir.name, "impor.json")
        with open(self.berkas, "w", encoding="utf-8") as f:
            f.write("{}")
        p = mock.patch.object(progress, "PROGRESS_FILE",
                              os.path.join(self.dir.name, "p.json"))
        p.start()
        self.addCleanup(p.stop)

    def _jalankan(self, argv, tty, jawaban):
        konfirmasi = mock.Mock(return_value=jawaban)
        with mock.patch.object(sys.stdin, "isatty", return_value=tty, create=True), \
                mock.patch.object(main, "confirm", konfirmasi), \
                redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            try:
                main._argumen(argv)
                kode = None
            except SystemExit as e:
                kode = e.code
        return kode, konfirmasi.call_count

    def test_di_terminal_ditanya_dan_bisa_dibatalkan(self):
        kode, ditanya = self._jalankan(["--impor", self.berkas], True, False)
        self.assertEqual(ditanya, 1)
        self.assertEqual(kode, 1, "pembatalan keluar dengan kode bukan nol")

    def test_di_terminal_dijawab_ya_lanjut(self):
        kode, ditanya = self._jalankan(["--impor", self.berkas], True, True)
        self.assertEqual((kode, ditanya), (None, 1))

    def test_skrip_tanpa_tty_tidak_ditanya(self):
        """Otomasi lama tidak boleh tiba-tiba menggantung menunggu jawaban."""
        kode, ditanya = self._jalankan(["--impor", self.berkas], False, False)
        self.assertEqual((kode, ditanya), (None, 0))

    def test_ya_melewati_pertanyaan(self):
        kode, ditanya = self._jalankan(["--impor", self.berkas, "--ya"], True, False)
        self.assertEqual((kode, ditanya), (None, 0))

    def test_berkas_tidak_ada_tidak_ditanya(self):
        """`impor()` sendiri yang melaporkan berkas hilang; bertanya dulu cuma membuang waktu."""
        hilang = os.path.join(self.dir.name, "tidak-ada.json")
        kode, ditanya = self._jalankan(["--impor", hilang], True, False)
        self.assertEqual((kode, ditanya), (None, 0))


if __name__ == "__main__":
    unittest.main()
