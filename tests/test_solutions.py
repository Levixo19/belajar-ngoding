"""Verifikasi setiap solusi contoh benar-benar lolos pemeriksaan otomatisnya.

Auto-checker menurunkan kunci jawaban dengan menjalankan solusi contoh. Kalau
solusi itu sendiri gagal jalan atau outputnya berubah-ubah, latihan tersebut
mustahil diselesaikan siswa. Tes ini memastikan hal itu tidak terjadi.

Latihan yang sengaja ditandai `auto_check: False` dilewati, tapi tetap diperiksa
alasannya masuk akal lewat TestLatihanTanpaPenilaian.

**Bahasa yang toolchain-nya tidak terpasang dilewati SECARA TERLIHAT.** Versi
lama menyaringnya di dalam generator, sehingga suite melaporkan "OK" tanpa satu
pun penanda skip -- di mesin tanpa g++ dan go, 32 dari 127 latihan tidak pernah
dijalankan dan tidak ada yang tahu. Sekarang tiap bahasa punya kelas tes sendiri
yang muncul sebagai `skipped` di laporan.

Tes ini LAMBAT karena mengompilasi ratusan program. Untuk melewatinya:
    BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .

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


def _stdin_pertama(ex):
    """Input pertama sebuah latihan, apa pun bentuk fieldnya."""
    daftar = ex.get("stdin_list")
    if daftar:
        return daftar[0]
    return ex.get("stdin", "")


def latihan_bahasa(lang):
    """Latihan bahasa ini yang layak dijalankan otomatis."""
    return [e for e in lang["exercises"] if bisa_dinilai(e, lang["runner"])[0]]


def _jalankan(bahasa, ex):
    return runner.jalankan(bahasa, gabung_setup(ex, ex["solution"]),
                           stdin=_stdin_pertama(ex), timeout=TIMEOUT)


def _bahasa_dipilih():
    for lang in LANGUAGES:
        if HANYA_BAHASA and lang["key"] != HANYA_BAHASA:
            continue
        yield lang


class BasisSolusi:
    """Kerangka untuk kelas per-bahasa yang dibuat otomatis di bawah.

    Sengaja BUKAN turunan TestCase: kalau ia turunan, unittest akan ikut
    menjalankannya sendiri dengan `lang = None` dan meledak.
    """

    lang = None

    def setUp(self):
        if LEWATI_LAMBAT:
            self.skipTest("dilewati lewat BELAJAR_SKIP_LAMBAT=1")
        if not runner.tersedia(self.lang["runner"]):
            hilang = ", ".join(runner.program_hilang(self.lang["runner"]))
            self.skipTest(f"toolchain {self.lang['label']} belum terpasang: {hilang}")

    def test_solusi_berjalan_tanpa_error(self):
        for ex in latihan_bahasa(self.lang):
            with self.subTest(latihan=ex["title"]):
                hasil = _jalankan(self.lang["runner"], ex)
                self.assertTrue(
                    hasil.sukses,
                    f"gagal di fase {hasil.fase}: {hasil.galat.strip()[:400]}",
                )

    def test_solusi_menghasilkan_output(self):
        """Tanpa output, auto-check tak bermakna: kode kosong pun akan lolos."""
        for ex in latihan_bahasa(self.lang):
            with self.subTest(latihan=ex["title"]):
                hasil = _jalankan(self.lang["runner"], ex)
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
        for ex in latihan_bahasa(self.lang):
            with self.subTest(latihan=ex["title"]):
                a = _jalankan(self.lang["runner"], ex)
                if not a.sukses:
                    self.skipTest("sudah dilaporkan tes lain")
                b = _jalankan(self.lang["runner"], ex)
                self.assertEqual(
                    runner.normalisasi(a.keluaran),
                    runner.normalisasi(b.keluaran),
                    "output berbeda antar eksekusi",
                )

    def test_solusi_lolos_auto_checker(self):
        """Uji ujung ke ujung: kunci jawaban dibuat, lalu solusi diperiksa."""
        for ex in latihan_bahasa(self.lang):
            with self.subTest(latihan=ex["title"]):
                tests, galat = bangun_tests(ex, self.lang["runner"])
                self.assertFalse(galat, galat)
                self.assertTrue(tests, "tidak ada test case yang terbentuk")

                semua, hasil_uji, _ = runner.periksa(
                    self.lang["runner"], gabung_setup(ex, ex["solution"]), tests,
                    timeout=TIMEOUT)

                if not semua:
                    rincian = "; ".join(
                        f"{h.nama}: harap={runner.normalisasi(h.harapan)[:80]!r} "
                        f"dapat={runner.normalisasi(h.aktual)[:80]!r} {h.galat[:120]}"
                        for h in hasil_uji if not h.lulus
                    )
                    self.fail(rincian)

    def test_input_berbeda_menghasilkan_output_berbeda(self):
        """Latihan bercabang wajib diuji dengan input yang menempuh cabang beda.

        Kalau semua input menghasilkan output yang sama, jawaban yang
        di-hardcode ikut dinyatakan benar dan latihan tidak mengukur apa pun.
        """
        for ex in latihan_bahasa(self.lang):
            if not ex.get("stdin_list"):
                continue
            with self.subTest(latihan=ex["title"]):
                tests, galat = bangun_tests(ex, self.lang["runner"])
                self.assertFalse(galat, galat)
                self.assertEqual(len(tests), len(ex["stdin_list"]))
                harapan = {runner.normalisasi(t["harapan"]) for t in tests}
                self.assertGreater(
                    len(harapan), 1,
                    "semua input menghasilkan output yang sama; pilih input yang "
                    "benar-benar menempuh cabang berbeda",
                )


# Satu kelas tes per bahasa supaya bahasa yang toolchain-nya hilang muncul
# sebagai `skipped` di laporan, bukan lenyap tanpa jejak.
for _lang in _bahasa_dipilih():
    _nama = "TestSolusi" + _lang["label"].replace("+", "p").replace(" ", "")
    globals()[_nama] = type(_nama, (BasisSolusi, unittest.TestCase), {"lang": _lang})
try:
    del _lang, _nama
except NameError:
    pass


class TestCakupanPengujian(unittest.TestCase):
    """Jaring pengaman: buat celah cakupan terlihat, jangan disembunyikan."""

    def test_melaporkan_bahasa_yang_tidak_teruji(self):
        tak_teruji = [l["label"] for l in LANGUAGES if not runner.tersedia(l["runner"])]
        jumlah = sum(len(l["exercises"]) for l in LANGUAGES
                     if not runner.tersedia(l["runner"]))
        total = sum(len(l["exercises"]) for l in LANGUAGES)
        if tak_teruji:
            print(f"\n  CATATAN: {jumlah}/{total} latihan tidak diverifikasi di mesin "
                  f"ini (toolchain hilang: {', '.join(tak_teruji)})")
        self.assertLessEqual(jumlah, total)


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
