"""Tes mesin kuis.

Sebelum berkas ini ada, quiz.py praktis tidak diuji sama sekali (hanya baris
`def` yang tereksekusi saat modul dimuat). Dua bug termahal di seluruh proyek
justru bersembunyi di sana: pemetaan ulang index jawaban setelah opsi diacak,
dan sesi "ulangi soal yang salah" yang merusak skor terbaik.

Dijalankan lewat: python3 -m unittest discover -s tests -t .
"""

import io
import os
import random
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest import mock

import progress
import quiz
import utils


KUIS = {
    "title": "Kuis Uji",
    "questions": [
        {"q": f"Soal {i}?",
         "options": [f"pilihan {i}A", f"pilihan {i}B", f"pilihan {i}C", f"pilihan {i}D"],
         "answer": i % 4,
         "explanation": f"penjelasan {i}"}
        for i in range(10)
    ],
}


class TestSiapkanSoal(unittest.TestCase):
    """Properti yang harus berlaku untuk SEMUA seed pengacakan."""

    def test_teks_jawaban_benar_tidak_pernah_berubah(self):
        for seed in range(60):
            rng = random.Random(seed)
            paket = quiz._siapkan_soal(KUIS["questions"], list(range(10)),
                                       acak_soal=True, acak_opsi=True, rng=rng)
            for item in paket:
                asli = KUIS["questions"][item["asli"]]
                with self.subTest(seed=seed, soal=item["asli"]):
                    self.assertEqual(
                        item["options"][item["answer"]],
                        asli["options"][asli["answer"]],
                        "index jawaban tidak dipetakan ulang dengan benar",
                    )

    def test_opsi_tetap_lengkap_setelah_diacak(self):
        rng = random.Random(7)
        paket = quiz._siapkan_soal(KUIS["questions"], list(range(10)), True, True, rng)
        for item in paket:
            asli = KUIS["questions"][item["asli"]]
            self.assertCountEqual(item["options"], asli["options"])

    def test_field_asli_menunjuk_soal_yang_benar(self):
        rng = random.Random(3)
        paket = quiz._siapkan_soal(KUIS["questions"], list(range(10)), True, True, rng)
        for item in paket:
            self.assertEqual(item["q"], KUIS["questions"][item["asli"]]["q"])

    def test_semua_soal_muncul_tepat_sekali(self):
        rng = random.Random(11)
        paket = quiz._siapkan_soal(KUIS["questions"], list(range(10)), True, True, rng)
        self.assertCountEqual([i["asli"] for i in paket], list(range(10)))

    def test_subset_hanya_berisi_index_yang_diminta(self):
        rng = random.Random(5)
        paket = quiz._siapkan_soal(KUIS["questions"], [2, 5, 7], True, True, rng)
        self.assertCountEqual([i["asli"] for i in paket], [2, 5, 7])

    def test_tanpa_acak_urutannya_persis_data_asli(self):
        rng = random.Random(1)
        paket = quiz._siapkan_soal(KUIS["questions"], list(range(10)), False, False, rng)
        self.assertEqual([i["asli"] for i in paket], list(range(10)))
        for item in paket:
            self.assertEqual(item["answer"], KUIS["questions"][item["asli"]]["answer"])


class BasisKuis(unittest.TestCase):
    """Arahkan progres ke direktori sementara dan matikan pembersihan layar."""

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "p.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")
        self._patch = mock.patch.object(utils, "clear", lambda: None)
        self._patch.start()

    def tearDown(self):
        self._patch.stop()
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        self.dir.cleanup()

    def jalankan(self, masukan, **kwargs):
        with mock.patch("builtins.input", side_effect=list(masukan)):
            with redirect_stdout(io.StringIO()) as keluar:
                quiz.run_quiz(KUIS, "java_kuis", **kwargs)
        return keluar.getvalue()


class TestRunQuiz(BasisKuis):
    def test_jawaban_semua_benar_tercatat(self):
        soal = quiz._siapkan_soal(KUIS["questions"], list(range(10)), False, False,
                                  random.Random(0))
        jawaban = [str(s["answer"] + 1) for s in soal]
        teks = self.jalankan(jawaban + [""] * 3, acak_soal=False, acak_opsi=False)
        self.assertIn("10/10", teks)

        info = progress.load_progress()["kuis_skor"]["java_kuis::Kuis Uji"]
        self.assertEqual(info["terbaik"], 10)
        self.assertEqual(info["total_soal"], 10)

    def test_eof_menghentikan_kuis_bukan_mengulang_selamanya(self):
        """Dulu stdin habis membuat soal yang sama dicetak jutaan kali."""
        with mock.patch("builtins.input", side_effect=EOFError):
            with redirect_stdout(io.StringIO()) as keluar:
                quiz.run_quiz(KUIS, "java_kuis")
        teks = keluar.getvalue()
        self.assertIn("Masukan habis", teks)
        self.assertLess(teks.count("Soal 1/10"), 3, "soal tidak boleh diulang terus")

    def test_masukan_tidak_valid_berulang_akhirnya_berhenti(self):
        teks = self.jalankan(["zz"] * 40)
        self.assertIn("Terlalu banyak masukan tidak valid", teks)

    def test_digit_unicode_tidak_bikin_crash(self):
        # '²'.isdigit() bernilai True tapi int('²') melempar ValueError.
        teks = self.jalankan(["²", "q", ""])
        self.assertIn("tidak valid", teks.lower())

    def test_q_menghentikan_tanpa_mencatat_skor(self):
        self.jalankan(["q", ""])
        self.assertNotIn("java_kuis::Kuis Uji", progress.load_progress()["kuis_skor"])


class TestSesiUlangTidakMerusakSkor(BasisKuis):
    """Regresi bug paling merusak: 'terbaik 8/2' dan badge sempurna palsu."""

    def _sesi_penuh_dengan_dua_salah(self):
        soal = quiz._siapkan_soal(KUIS["questions"], list(range(10)), False, False,
                                  random.Random(0))
        jawaban = []
        salah = []
        for i, s in enumerate(soal):
            if i < 2:                       # sengaja salah pada dua soal pertama
                jawaban.append(str((s["answer"] + 1) % 4 + 1))
                salah.append(s["asli"])
            else:
                jawaban.append(str(s["answer"] + 1))
        self.jalankan(jawaban + ["", ""], acak_soal=False, acak_opsi=False)
        return sorted(salah)

    def test_penyebut_tidak_menyusut_setelah_sesi_ulang(self):
        salah = self._sesi_penuh_dengan_dua_salah()
        info = progress.load_progress()["kuis_skor"]["java_kuis::Kuis Uji"]
        self.assertEqual((info["terbaik"], info["total_soal"]), (8, 10))

        soal = quiz._siapkan_soal(KUIS["questions"], salah, False, False, random.Random(0))
        jawaban = [str(s["answer"] + 1) for s in soal]
        self.jalankan(jawaban + ["", ""], indeks=salah, acak_soal=False, acak_opsi=False)

        info = progress.load_progress()["kuis_skor"]["java_kuis::Kuis Uji"]
        self.assertEqual(info["total_soal"], 10, "penyebut tertimpa jumlah subset")
        self.assertEqual(info["terbaik"], 8, "skor terbaik berubah karena sesi ulang")
        self.assertLessEqual(info["terbaik"], info["total_soal"])

    def test_sesi_ulang_tidak_memberi_xp_dan_badge_sempurna(self):
        salah = self._sesi_penuh_dengan_dua_salah()
        xp_sebelum = progress.load_progress()["xp"]

        for _ in range(3):
            soal = quiz._siapkan_soal(KUIS["questions"], salah, False, False,
                                      random.Random(0))
            jawaban = [str(s["answer"] + 1) for s in soal]
            self.jalankan(jawaban + ["", ""], indeks=salah, acak_soal=False,
                          acak_opsi=False)

        data = progress.load_progress()
        self.assertEqual(data["xp"], xp_sebelum, "XP bisa dipanen lewat sesi ulang")
        self.assertNotIn("nilai_sempurna", data["badge"])

    def test_sesi_ulang_mencoret_soal_yang_sudah_benar(self):
        salah = self._sesi_penuh_dengan_dua_salah()
        self.assertEqual(progress.soal_salah_terakhir("java_kuis", "Kuis Uji"), salah)

        soal = quiz._siapkan_soal(KUIS["questions"], salah, False, False, random.Random(0))
        jawaban = [str(s["answer"] + 1) for s in soal]
        self.jalankan(jawaban + ["", ""], indeks=salah, acak_soal=False, acak_opsi=False)
        self.assertEqual(progress.soal_salah_terakhir("java_kuis", "Kuis Uji"), [])

    def test_jadwal_ulang_tidak_melar_karena_sesi_ulang(self):
        salah = self._sesi_penuh_dengan_dua_salah()
        jadwal_awal = progress.load_progress()["jadwal_kuis"]["java_kuis::Kuis Uji"]

        for _ in range(4):
            soal = quiz._siapkan_soal(KUIS["questions"], salah, False, False,
                                      random.Random(0))
            self.jalankan([str(s["answer"] + 1) for s in soal] + ["", ""],
                          indeks=salah, acak_soal=False, acak_opsi=False)

        jadwal_akhir = progress.load_progress()["jadwal_kuis"]["java_kuis::Kuis Uji"]
        self.assertEqual(jadwal_awal, jadwal_akhir)


class TestStatusKuis(BasisKuis):
    def test_label_belum_dikerjakan(self):
        data = progress.load_progress()
        label = utils.strip_ansi(quiz._status_kuis(data, "java_kuis", KUIS))
        self.assertIn("belum dikerjakan", label)

    def test_label_tidak_pernah_melebihi_seratus_persen(self):
        """Data lama bisa punya terbaik > total_soal; tampilannya harus tetap waras."""
        progress.record_quiz_score("java_kuis", "Kuis Uji", 10, 10)
        data = progress.load_progress()
        data["kuis_skor"]["java_kuis::Kuis Uji"]["total_soal"] = 2
        label = utils.strip_ansi(quiz._status_kuis(data, "java_kuis", KUIS))
        self.assertIn("2/2", label)


if __name__ == "__main__":
    unittest.main(verbosity=2)
