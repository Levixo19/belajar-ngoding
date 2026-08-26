"""Verifikasi setiap solusi contoh benar-benar lolos pemeriksaan otomatisnya.

Auto-checker menurunkan kunci jawaban dengan menjalankan solusi contoh. Kalau
solusi itu sendiri gagal jalan atau outputnya berubah-ubah, latihan tersebut
mustahil diselesaikan siswa. Tes ini memastikan hal itu tidak terjadi.

Latihan yang sengaja ditandai `auto_check: False` dilewati, tapi tetap diperiksa
alasannya masuk akal lewat TestLatihanTanpaPenilaian.

Tes ini LAMBAT karena mengompilasi ratusan program. Untuk melewatinya:
    BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover tests

Untuk menguji satu bahasa saja:
    BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions
"""

import os
import unittest

import runner
from exercises import bangun_tests, bisa_dinilai, gabung_setup
from main import LANGUAGES

LEWATI_LAMBAT = os.environ.get("BELAJAR_SKIP_LAMBAT") == "1"
HANYA_BAHASA = os.environ.get("BELAJAR_BAHASA", "").lower()
TIMEOUT = 90


def latihan_yang_diuji():
    """Hasilkan (bahasa_label, runner_key, latihan) yang layak dijalankan."""
    for lang in LANGUAGES:
        if HANYA_BAHASA and lang["key"] != HANYA_BAHASA:
            continue
        bahasa = lang["runner"]
        if not runner.tersedia(bahasa):
            continue
        for ex in lang["exercises"]:
            if not bisa_dinilai(ex, bahasa)[0]:
                continue
            yield lang["label"], bahasa, ex


def _jalankan(bahasa, ex):
    return runner.jalankan(bahasa, gabung_setup(ex, ex["solution"]),
                           stdin=ex.get("stdin", ""), timeout=TIMEOUT)


@unittest.skipIf(LEWATI_LAMBAT, "dilewati lewat BELAJAR_SKIP_LAMBAT=1")
class TestSolusiContoh(unittest.TestCase):

    def test_solusi_berjalan_tanpa_error(self):
        for label, bahasa, ex in latihan_yang_diuji():
            with self.subTest(bahasa=label, latihan=ex["title"]):
                hasil = _jalankan(bahasa, ex)
                self.assertTrue(
                    hasil.sukses,
                    f"gagal di fase {hasil.fase}: {hasil.galat.strip()[:400]}",
                )

    def test_solusi_menghasilkan_output(self):
        """Tanpa output, auto-check tak bermakna: kode kosong pun akan lolos."""
        for label, bahasa, ex in latihan_yang_diuji():
            with self.subTest(bahasa=label, latihan=ex["title"]):
                hasil = _jalankan(bahasa, ex)
                if not hasil.sukses:
                    self.skipTest("sudah dilaporkan tes lain")
                self.assertTrue(
                    runner.normalisasi(hasil.keluaran),
                    "solusi tidak mencetak apa pun; tambahkan field 'verifikasi'",
                )

    def test_output_deterministik(self):
        """Output yang berubah tiap dijalankan membuat auto-check mustahil lulus.

        Penyebab tersering: bilangan acak, tanggal saat ini, dan iterasi map
        di Go yang urutannya sengaja diacak runtime.
        """
        for label, bahasa, ex in latihan_yang_diuji():
            with self.subTest(bahasa=label, latihan=ex["title"]):
                a = _jalankan(bahasa, ex)
                if not a.sukses:
                    self.skipTest("sudah dilaporkan tes lain")
                b = _jalankan(bahasa, ex)
                self.assertEqual(
                    runner.normalisasi(a.keluaran),
                    runner.normalisasi(b.keluaran),
                    "output berbeda antar eksekusi",
                )

    def test_solusi_lolos_auto_checker(self):
        """Uji ujung ke ujung: kunci jawaban dibuat, lalu solusi diperiksa."""
        for label, bahasa, ex in latihan_yang_diuji():
            with self.subTest(bahasa=label, latihan=ex["title"]):
                tests, galat = bangun_tests(ex, bahasa)
                self.assertFalse(galat, galat)
                self.assertTrue(tests, "tidak ada test case yang terbentuk")

                semua, hasil_uji, _ = runner.periksa(
                    bahasa, gabung_setup(ex, ex["solution"]), tests, timeout=TIMEOUT)

                if not semua:
                    rincian = "; ".join(
                        f"{h.nama}: harap={runner.normalisasi(h.harapan)[:80]!r} "
                        f"dapat={runner.normalisasi(h.aktual)[:80]!r} {h.galat[:120]}"
                        for h in hasil_uji if not h.lulus
                    )
                    self.fail(rincian)


class TestLatihanTanpaPenilaian(unittest.TestCase):
    """Latihan yang tidak dinilai otomatis harus tetap utuh dan jelas alasannya."""

    def _tak_dinilai(self):
        for lang in LANGUAGES:
            for ex in lang["exercises"]:
                if ex.get("auto_check") is False:
                    yield lang["label"], ex

    def test_punya_alasan_yang_dijelaskan(self):
        for label, ex in self._tak_dinilai():
            with self.subTest(bahasa=label, latihan=ex["title"]):
                alasan = ex.get("alasan_tidak_dicek", "")
                self.assertTrue(alasan.strip(),
                                "wajib menjelaskan kenapa tidak bisa dinilai")
                self.assertGreater(len(alasan), 15, "alasan terlalu singkat")

    def test_tetap_punya_solusi_contoh(self):
        for label, ex in self._tak_dinilai():
            with self.subTest(bahasa=label, latihan=ex["title"]):
                self.assertTrue(ex["solution"].strip())

    def test_jumlahnya_tetap_sedikit(self):
        """Kalau angkanya melonjak, ada yang salah dengan runner-nya."""
        total = sum(len(l["exercises"]) for l in LANGUAGES)
        tak_dinilai = sum(1 for _ in self._tak_dinilai())
        self.assertLess(tak_dinilai / total, 0.10,
                        f"{tak_dinilai}/{total} latihan tidak bisa dinilai otomatis")


class TestLatihanTanpaToolchain(unittest.TestCase):
    def test_bahasa_tanpa_toolchain_tetap_punya_solusi(self):
        for lang in LANGUAGES:
            if runner.tersedia(lang["runner"]):
                continue
            for ex in lang["exercises"]:
                with self.subTest(bahasa=lang["label"], latihan=ex["title"]):
                    self.assertTrue(ex["solution"].strip())

    def test_bangun_tests_melapor_rapi_saat_toolchain_hilang(self):
        for lang in LANGUAGES:
            if runner.tersedia(lang["runner"]):
                continue
            ex = lang["exercises"][0]
            with self.subTest(bahasa=lang["label"]):
                tests, galat = bangun_tests(ex, lang["runner"])
                self.assertEqual(tests, [])
                self.assertIn("Toolchain", galat)


if __name__ == "__main__":
    unittest.main(verbosity=2)
