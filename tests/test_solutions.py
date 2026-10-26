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
import re
import textwrap
import unittest

from inti import runner
from inti.berkas import PROGRAM, jenis_kode
from inti.latihan import (bangun_tests, bisa_dinilai, blok_janji,
                          gabung_setup, input_untuk)
from inti.kurikulum import LANGUAGES

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


_KEPALA_MATERI = re.compile(r"^keluaran(?:nya)?(?:\s*\([^)]*\))?\s*:?$", re.I)


def _blok_keluaran(body):
    """Semua blok keluaran yang dijanjikan sebuah prosa materi."""
    hasil = []
    for j, baris in enumerate(body):
        if not _KEPALA_MATERI.match(baris.strip()):
            continue
        keluar, mulai = [], False
        for x in body[j + 1:]:
            if not x.strip():
                if mulai:
                    break
                continue
            mulai = True
            keluar.append(x.rstrip())
        if keluar:
            hasil.append("\n".join(keluar))
    return hasil


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

    def test_janji_keluaran_di_soal_sesuai_kenyataan(self):
        """Blok "Keluaran yang diharapkan" di soal harus benar-benar keluar.

        Hampir semua latihan menjanjikan bentuk keluarannya di dalam soal,
        lengkap sampai lebar kolomnya. Janji itu ditulis tangan, dan lebar
        kolom yang dihitung di kepala ternyata sangat sering meleset satu
        spasi -- kesalahan yang tidak menggagalkan satu pun tes lain, tapi
        membuat pelajar mengejar keluaran yang MUSTAHIL dihasilkan solusi
        mana pun. Lima kasus seperti itu ditemukan saat tes ini pertama
        ditulis, tersebar di tiga bahasa.

        Soal boleh menampilkan CUPLIKAN, bukan seluruh keluaran; karena itu
        janji yang lebih pendek diterima asal muncul utuh di dalam hasilnya.
        Indentasi seluruh blok juga diabaikan (dedent) -- yang dijaga adalah
        indentasi RELATIF antar barisnya, karena itulah yang jadi isi pada
        keluaran berbentuk pohon atau tabel.
        """
        for ex in latihan_bahasa(self.lang):
            for petunjuk, harap in blok_janji(ex):
                masukan = input_untuk(ex, petunjuk)
                if masukan is None:
                    continue
                with self.subTest(latihan=ex["title"], input=petunjuk):
                    hasil = runner.jalankan(
                        self.lang["runner"], gabung_setup(ex, ex["solution"]),
                        stdin=masukan, timeout=TIMEOUT)
                    if not hasil.sukses:
                        self.skipTest("sudah dilaporkan tes lain")

                    nyata = textwrap.dedent(runner.normalisasi(hasil.keluaran))
                    janji = textwrap.dedent(runner.normalisasi(harap))
                    self.assertTrue(
                        janji == nyata or janji in nyata,
                        "keluaran yang dijanjikan soal tidak pernah terjadi.\n"
                        f"  janji: {janji[:300]!r}\n"
                        f"  nyata: {nyata[:300]!r}",
                    )

    def test_janji_keluaran_di_materi_sesuai_kenyataan(self):
        """Blok "Keluaran:" di prosa materi harus benar-benar keluar.

        Contoh kode di materi hampir selalu diikuti prosa yang menuliskan
        keluarannya. Itu janji yang persis sama rawannya dengan janji di
        soal latihan -- angka, lebar kolom, dan pemisah desimal yang
        ditulis dari ingatan sering meleset. Dua puluh satu kasus seperti
        itu ditemukan saat tes ini pertama ditulis, tersebar di lima
        bahasa; salah satunya menjanjikan pemisah ribuan titik untuk
        keluaran yang sebenarnya memakai koma.

        Prosa boleh menampilkan CUPLIKAN; karena itu janji yang lebih
        pendek diterima asal muncul UTUH dan BERURUTAN di dalam hasilnya.
        """
        for m in self.lang["materials"]:
            bagian = m["sections"]
            for i, s in enumerate(bagian):
                kode = s.get("code")
                if not kode or i + 1 >= len(bagian):
                    continue
                bhs = s.get("bahasa") or self.lang["runner"]
                if jenis_kode(bhs, kode) != PROGRAM:
                    continue
                if bhs != self.lang["runner"] and not runner.tersedia(bhs):
                    continue
                for janji in _blok_keluaran(bagian[i + 1].get("body") or []):
                    with self.subTest(materi=m["title"]):
                        hasil = runner.jalankan(bhs, kode,
                                                timeout=TIMEOUT)
                        if not hasil.sukses:
                            self.fail(f"contoh kode tidak bisa dijalankan: "
                                      f"{hasil.galat.strip()[:300]}")
                        nyata = textwrap.dedent(runner.normalisasi(hasil.keluaran))
                        harap = textwrap.dedent(runner.normalisasi(janji))
                        self.assertTrue(
                            harap == nyata or harap in nyata,
                            "keluaran yang dijanjikan materi tidak pernah "
                            f"terjadi.\n  janji: {harap[:300]!r}\n"
                            f"  nyata: {nyata[:300]!r}",
                        )

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


class TestKerangkaTidakMenggagalkan(unittest.TestCase):
    """Kerangka editor + jawaban yang benar harus tetap lulus.

    Pelajar menulis jawabannya DI BAWAH baris "tulis kodemu di sini", jadi
    kerangka itu ikut dinilai. Kerangka HTML dan CSS dulu memakai `#`: di
    HTML baris itu jadi teks halaman, di CSS ia menelan pemilih pertama, dan
    latihan pertama pintu masuk pemula gagal padahal kodenya benar.

    Hanya bahasa yang kerangkanya komentar belaka. Untuk Java, C, Go, dst.
    jawabannya ditulis DI DALAM main, bukan ditempel sesudahnya. HTML dan CSS
    selalu diperiksa (cepat, tanpa compiler); sisanya ikut mode lambat.
    """

    SELALU = ("html", "css")
    LAMBAT = ("python", "javascript", "sql", "ruby", "bash")

    def test_kerangka_ditambah_solusi_tetap_lulus(self):
        from inti.latihan import _kerangka
        bahasa = self.SELALU + (() if LEWATI_LAMBAT else self.LAMBAT)
        for lang in LANGUAGES:
            if lang["key"] not in bahasa or not runner.tersedia(lang["runner"]):
                continue
            daftar = latihan_bahasa(lang)
            if lang["key"] not in self.SELALU:
                daftar = daftar[:3]
            for ex in daftar:
                with self.subTest(bahasa=lang["key"], latihan=ex["title"]):
                    tests, galat = bangun_tests(ex, lang["runner"])
                    self.assertFalse(galat, galat)
                    kode = _kerangka(lang["runner"], ex) + ex["solution"]
                    semua, hasil, _ = runner.periksa(
                        lang["runner"], gabung_setup(ex, kode), tests,
                        timeout=TIMEOUT)
                    self.assertTrue(semua, "; ".join(
                        f"dapat={runner.normalisasi(h.aktual)[:120]!r}"
                        for h in hasil if not h.lulus))


if __name__ == "__main__":
    unittest.main(verbosity=2)
