"""Tes eksekusi kode: keluaran, error, batas waktu, dan pencocokan jawaban."""

import unittest

import runner


def butuh(bahasa):
    return unittest.skipUnless(
        runner.tersedia(bahasa),
        f"toolchain {bahasa} belum terpasang: {', '.join(runner.program_hilang(bahasa))}",
    )


class TestDeteksiToolchain(unittest.TestCase):
    def test_bahasa_tak_dikenal_ditolak_dengan_rapi(self):
        hasil = runner.jalankan("brainfuck", "+++")
        self.assertFalse(hasil.sukses)
        self.assertEqual(hasil.fase, "setup")
        self.assertIn("belum didukung", hasil.galat)

    def test_daftar_tersedia_mencakup_semua_toolchain(self):
        daftar = runner.daftar_tersedia()
        self.assertEqual(set(daftar), set(runner.TOOLCHAINS))
        for nilai in daftar.values():
            self.assertIsInstance(nilai, bool)

    def test_toolchain_belum_terpasang_memberi_pesan_jelas(self):
        for bahasa in runner.TOOLCHAINS:
            if runner.tersedia(bahasa):
                continue
            with self.subTest(bahasa=bahasa):
                hasil = runner.jalankan(bahasa, "apa saja")
                self.assertFalse(hasil.sukses)
                self.assertEqual(hasil.fase, "setup")
                self.assertTrue(hasil.catatan, "harus memberi saran pemasangan")


class TestEksekusi(unittest.TestCase):
    @butuh("python")
    def test_python_mencetak_output(self):
        hasil = runner.jalankan("python", 'print("halo")')
        self.assertTrue(hasil.sukses)
        self.assertEqual(hasil.keluaran.strip(), "halo")

    @butuh("python")
    def test_python_membaca_stdin(self):
        kode = 'n = int(input())\nprint(n * 2)'
        hasil = runner.jalankan("python", kode, stdin="21\n")
        self.assertTrue(hasil.sukses)
        self.assertEqual(hasil.keluaran.strip(), "42")

    @butuh("python")
    def test_error_runtime_ditangkap_bukan_dilempar(self):
        hasil = runner.jalankan("python", "1 / 0")
        self.assertFalse(hasil.sukses)
        self.assertEqual(hasil.fase, "jalan")
        self.assertIn("ZeroDivisionError", hasil.galat)

    @butuh("python")
    def test_timeout_menghentikan_loop_tak_berujung(self):
        hasil = runner.jalankan("python", "while True: pass", timeout=2)
        self.assertFalse(hasil.sukses)
        self.assertTrue(hasil.timeout)
        self.assertIn("dihentikan", hasil.galat)

    @butuh("python")
    def test_output_sangat_panjang_dipotong(self):
        hasil = runner.jalankan("python", 'print("x" * 500000)', timeout=20)
        self.assertLessEqual(len(hasil.keluaran), runner.BATAS_OUTPUT_CHAR + 100)
        self.assertIn("dipotong", hasil.keluaran)

    @butuh("java")
    def test_java_memakai_nama_kelas_sebagai_nama_file(self):
        kode = ('public class Hitung { public static void main(String[] a) {'
                ' System.out.println(6 * 7); } }')
        hasil = runner.jalankan("java", kode, timeout=60)
        self.assertTrue(hasil.sukses, hasil.galat)
        self.assertEqual(hasil.keluaran.strip(), "42")

    @butuh("java")
    def test_kegagalan_kompilasi_ditandai_fase_kompilasi(self):
        kode = "public class Rusak { ini bukan java }"
        hasil = runner.jalankan("java", kode, timeout=60)
        self.assertFalse(hasil.sukses)
        self.assertEqual(hasil.fase, "kompilasi")

    @butuh("c")
    def test_c_terhubung_dengan_pustaka_matematika(self):
        kode = ('#include <stdio.h>\n#include <math.h>\n'
                'int main(void){ printf("%.0f\\n", sqrt(144.0)); return 0; }')
        hasil = runner.jalankan("c", kode, timeout=30)
        self.assertTrue(hasil.sukses, hasil.galat)
        self.assertEqual(hasil.keluaran.strip(), "12")

    @butuh("javascript")
    def test_javascript_mencetak_output(self):
        hasil = runner.jalankan("javascript", 'console.log(6 * 7)')
        self.assertTrue(hasil.sukses)
        self.assertEqual(hasil.keluaran.strip(), "42")

    @butuh("sql")
    def test_sql_dijalankan_dari_file(self):
        kode = "CREATE TABLE t(a INT); INSERT INTO t VALUES (10),(32); SELECT SUM(a) FROM t;"
        hasil = runner.jalankan("sql", kode)
        self.assertTrue(hasil.sukses, hasil.galat)
        self.assertEqual(hasil.keluaran.strip(), "42")

    @butuh("bash")
    def test_bash_mencetak_output(self):
        hasil = runner.jalankan("bash", 'echo $((6 * 7))')
        self.assertTrue(hasil.sukses)
        self.assertEqual(hasil.keluaran.strip(), "42")


class TestNormalisasi(unittest.TestCase):
    def test_spasi_di_akhir_baris_diabaikan(self):
        self.assertEqual(runner.normalisasi("halo   \ndunia  "), "halo\ndunia")

    def test_baris_kosong_di_akhir_dibuang(self):
        self.assertEqual(runner.normalisasi("halo\n\n\n"), "halo")

    def test_akhiran_baris_windows_disamakan(self):
        self.assertEqual(runner.normalisasi("a\r\nb"), runner.normalisasi("a\nb"))

    def test_teks_kosong(self):
        self.assertEqual(runner.normalisasi("   \n  \n"), "")


class TestPencocokan(unittest.TestCase):
    def test_mode_persis(self):
        self.assertTrue(runner._cocok("halo", "halo", "persis"))
        self.assertFalse(runner._cocok("Halo", "halo", "persis"))

    def test_mode_abaikan_kapital(self):
        self.assertTrue(runner._cocok("HALO", "halo", "abaikan_kapital"))

    def test_mode_mengandung(self):
        self.assertTrue(runner._cocok("nilai akhir: 42 poin", "42", "mengandung"))
        self.assertFalse(runner._cocok("nilai akhir: 41", "42", "mengandung"))

    def test_mode_angka_mengabaikan_teks_di_sekitarnya(self):
        self.assertTrue(runner._cocok("Total: 42 item", "42", "angka"))
        self.assertTrue(runner._cocok("a=1 b=2", "1 dan 2", "angka"))
        self.assertFalse(runner._cocok("Total: 43", "42", "angka"))

    def test_mode_regex(self):
        self.assertTrue(runner._cocok("versi 1.2.3", r"versi \d+\.\d+\.\d+", "regex"))
        self.assertFalse(runner._cocok("versi x", r"versi \d+", "regex"))

    def test_regex_rusak_dianggap_tidak_cocok(self):
        self.assertFalse(runner._cocok("apa saja", "[kurung tidak ditutup", "regex"))


class TestPeriksa(unittest.TestCase):
    @butuh("python")
    def test_semua_uji_lulus(self):
        tests = [
            {"nama": "genap", "stdin": "4\n", "harapan": "genap"},
            {"nama": "ganjil", "stdin": "7\n", "harapan": "ganjil"},
        ]
        kode = 'n = int(input())\nprint("genap" if n % 2 == 0 else "ganjil")'
        semua, hasil, _ = runner.periksa("python", kode, tests)
        self.assertTrue(semua)
        self.assertEqual(len(hasil), 2)
        self.assertTrue(all(h.lulus for h in hasil))

    @butuh("python")
    def test_satu_uji_gagal_membuat_keseluruhan_gagal(self):
        tests = [
            {"nama": "benar", "stdin": "4\n", "harapan": "genap"},
            {"nama": "sengaja salah", "stdin": "7\n", "harapan": "genap"},
        ]
        kode = 'n = int(input())\nprint("genap" if n % 2 == 0 else "ganjil")'
        semua, hasil, _ = runner.periksa("python", kode, tests)
        self.assertFalse(semua)
        self.assertTrue(hasil[0].lulus)
        self.assertFalse(hasil[1].lulus)

    @butuh("python")
    def test_error_sintaks_menghentikan_sisa_uji(self):
        tests = [{"harapan": "a"}, {"harapan": "b"}, {"harapan": "c"}]
        semua, hasil, _ = runner.periksa("python", "ini bukan python(((", tests)
        self.assertFalse(semua)
        self.assertEqual(len(hasil), 1, "harus berhenti setelah uji pertama gagal")

    @butuh("python")
    def test_timeout_dihitung_gagal(self):
        tests = [{"harapan": "apa pun"}]
        semua, hasil, _ = runner.periksa("python", "while True: pass", tests, timeout=2)
        self.assertFalse(semua)
        self.assertFalse(hasil[0].lulus)


class TestNamaKelasJava(unittest.TestCase):
    def test_mengambil_public_class(self):
        self.assertEqual(runner._nama_kelas_java("public class Halo {}"), "Halo")

    def test_mengambil_class_biasa(self):
        self.assertEqual(runner._nama_kelas_java("class Diam {}"), "Diam")

    def test_public_final_class(self):
        self.assertEqual(runner._nama_kelas_java("public final class Kunci {}"), "Kunci")

    def test_mengabaikan_class_setelah_public_class(self):
        kode = "public class Utama {}\nclass Bantu {}"
        self.assertEqual(runner._nama_kelas_java(kode), "Utama")

    def test_tanpa_class_memakai_nama_bawaan(self):
        self.assertEqual(runner._nama_kelas_java("int x = 1;"), "Main")


if __name__ == "__main__":
    unittest.main(verbosity=2)
