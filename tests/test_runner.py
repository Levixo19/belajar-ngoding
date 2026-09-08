"""Tes eksekusi kode: keluaran, error, batas waktu, dan pencocokan jawaban."""

import os
import tempfile
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


class TestBatasSumberDaya(unittest.TestCase):
    """Docstring runner.py berjanji membatasi memori, ukuran berkas, dan output.

    Sebelum tes ini ada, mematikan SELURUH rlimit tetap membuat suite hijau --
    janji itu tidak dijaga apa pun.
    """

    @butuh("python")
    @unittest.skipIf(runner.resource is None, "modul resource hanya ada di POSIX")
    def test_alokasi_memori_kebablasan_ditolak(self):
        besar = runner.BATAS_MEMORI_MB * 4 * 1024 * 1024
        hasil = runner.jalankan("python", f"x = bytearray({besar})", timeout=20)
        self.assertFalse(hasil.sukses, "batas memori tidak ditegakkan")

    @butuh("python")
    @unittest.skipIf(runner.resource is None, "modul resource hanya ada di POSIX")
    def test_menulis_berkas_raksasa_dihentikan(self):
        kode = (f"blok = b'x' * (1024 * 1024)\n"
                f"with open('besar.bin', 'wb') as f:\n"
                f"    for _ in range({runner.BATAS_FILE_MB * 4}):\n"
                f"        f.write(blok)\n"
                f"print('selesai')")
        hasil = runner.jalankan("python", kode, timeout=30)
        self.assertFalse(hasil.sukses, "batas ukuran berkas tidak ditegakkan")

    @butuh("python")
    def test_output_tak_berujung_tidak_menyedot_memori_induk(self):
        """Regresi: dulu induk menampung 4,7 GB sebelum sempat memotong output."""
        if runner.resource is None:
            self.skipTest("butuh modul resource untuk mengukur RSS")
        sebelum = runner.resource.getrusage(runner.resource.RUSAGE_SELF).ru_maxrss
        runner.jalankan("python",
                        "import sys\nb='x'*65536\nwhile True: sys.stdout.write(b)",
                        timeout=5)
        sesudah = runner.resource.getrusage(runner.resource.RUSAGE_SELF).ru_maxrss
        naik_mb = (sesudah - sebelum) / 1024
        self.assertLess(naik_mb, 200, f"memori induk naik {naik_mb:.0f} MB")

    @butuh("python")
    def test_keluaran_selalu_dipotong(self):
        hasil = runner.jalankan("python", "print('x' * 5_000_000)", timeout=20)
        self.assertLessEqual(len(hasil.keluaran), runner.BATAS_OUTPUT_CHAR + 200)

    @butuh("bash")
    def test_proses_cucu_ikut_dibunuh_saat_timeout(self):
        """Regresi: subshell `&` dulu selamat dan terus membakar CPU."""
        import subprocess as sp
        import time

        def cucu_hidup():
            # -x: cocokkan NAMA proses, bukan seluruh baris perintah. `pgrep -f`
            # ikut mencocokkan shell yang menjalankan tes ini kalau kebetulan
            # teks "sleep 91" ada di baris perintahnya -- positif palsu.
            keluar = sp.run(["pgrep", "-a", "-x", "sleep"],
                            capture_output=True, text=True)
            return [b for b in keluar.stdout.splitlines() if b.rstrip().endswith(" 91")]

        self.assertEqual(cucu_hidup(), [], "sudah ada proses sisa sebelum tes")
        runner.jalankan("bash", "sleep 91 &\nsleep 30\n", timeout=2)
        time.sleep(1)
        self.assertEqual(cucu_hidup(), [], "proses cucu masih hidup setelah timeout")

    @butuh("python")
    def test_timeout_menyertakan_pesan_yang_sempat_tercetak(self):
        kode = ("import sys\n"
                "sys.stderr.write('sedang menunggu sesuatu')\n"
                "sys.stderr.flush()\n"
                "while True: pass")
        hasil = runner.jalankan("python", kode, timeout=3)
        self.assertTrue(hasil.timeout)
        self.assertIn("sedang menunggu sesuatu", hasil.galat)


class TestKeamananRunner(unittest.TestCase):
    @butuh("sql")
    def test_dot_command_sqlite_tidak_menembus_direktori_sementara(self):
        if not runner._SQLITE_AMAN:
            self.skipTest("sqlite3 di mesin ini belum mendukung -safe")
        tujuan = os.path.join(tempfile.gettempdir(), "belajar_uji_bocor.txt")
        if os.path.exists(tujuan):
            os.unlink(tujuan)
        runner.jalankan("sql", f".output {tujuan}\nselect 1;\n")
        self.assertFalse(os.path.exists(tujuan), "sqlite menulis di luar tempdir")

    @butuh("python")
    def test_home_diarahkan_ke_direktori_sementara(self):
        hasil = runner.jalankan("python", "import os; print(os.environ['HOME'])")
        self.assertIn("belajar-", hasil.keluaran)

    @butuh("java")
    def test_kompilasi_tetap_jalan_di_locale_non_utf8(self):
        """javac tanpa -encoding menolak huruf beraksen saat LC_ALL=C."""
        asli = os.environ.get("LC_ALL")
        os.environ["LC_ALL"] = "C"
        try:
            kode = ('public class Main { public static void main(String[] a) {'
                    ' System.out.println("harga: Rp5.000 \u00e9\u00fc"); } }')
            hasil = runner.jalankan("java", kode, timeout=60)
            self.assertTrue(hasil.sukses, hasil.galat)
        finally:
            if asli is None:
                os.environ.pop("LC_ALL", None)
            else:
                os.environ["LC_ALL"] = asli


class TestKodeKeluarIkutDinilai(unittest.TestCase):
    @butuh("python")
    def test_output_benar_tapi_program_error_tidak_lulus(self):
        """Program yang mencetak jawaban benar lalu meledak bukan jawaban benar."""
        tests = [{"nama": "uji", "harapan": "Hasil: 7", "mode": "persis"}]
        semua, hasil, _ = runner.periksa(
            "python", 'print("Hasil: 7")\nraise SystemExit("boom")\n', tests)
        self.assertFalse(semua)
        self.assertTrue(hasil[0].output_cocok, "teksnya memang sudah cocok")
        self.assertNotEqual(hasil[0].kode_keluar, 0)

    @butuh("python")
    def test_program_normal_tetap_lulus(self):
        tests = [{"nama": "uji", "harapan": "7", "mode": "persis"}]
        semua, hasil, _ = runner.periksa("python", 'print(7)', tests)
        self.assertTrue(semua)
        self.assertEqual(hasil[0].kode_keluar, 0)

    @butuh("c")
    def test_segfault_dijelaskan_dalam_bahasa_manusia(self):
        kode = "int main(void){ int *p = 0; *p = 1; return 0; }"
        hasil = runner.jalankan("c", kode, timeout=20)
        self.assertFalse(hasil.sukses)
        self.assertIn("segmentation fault", hasil.galat.lower())


class TestNormalisasiSimetris(unittest.TestCase):
    def test_indentasi_baris_pertama_dipertahankan(self):
        """Regresi: .strip() global dulu membuang spasi baris pertama saja."""
        self.assertEqual(runner.normalisasi("  *\n **\n***"), "  *\n **\n***")

    def test_baris_kosong_di_awal_dibuang(self):
        self.assertEqual(runner.normalisasi("\n\nhalo"), "halo")

    def test_semua_baris_diperlakukan_sama(self):
        a = runner.normalisasi("   x\n   y")
        self.assertEqual(a, "   x\n   y")


class TestInstalasiToolchain(unittest.TestCase):
    """Setiap toolchain yang MEMBUTUHKAN pemasangan harus memberi tahu caranya.

    Syaratnya sengaja diikatkan pada `butuh`, bukan pada keberadaan entri di
    TOOLCHAINS. HTML dan CSS tidak memerlukan satu program pun — keduanya
    dibaca oleh struktur.py memakai penerjemah Python yang sama dengan yang
    menjalankan aplikasi ini — jadi menuntut petunjuk pemasangan untuk
    keduanya berarti menuntut jawaban atas pertanyaan yang tidak pernah
    ditanyakan. Yang penting justru kebalikannya, dan itu yang diuji di bawah:
    toolchain yang butuh sesuatu TIDAK BOLEH diam soal cara memasangnya.
    """

    def test_setiap_toolchain_yang_butuh_program_punya_petunjuk_pemasangan(self):
        for kunci, tc in runner.TOOLCHAINS.items():
            if not tc.butuh:
                continue
            with self.subTest(bahasa=kunci):
                self.assertTrue(tc.instalasi, "tidak ada petunjuk instalasi")
                for sistem in ("fedora", "debian", "mac", "windows"):
                    self.assertIn(sistem, tc.instalasi)
                    self.assertTrue(tc.instalasi[sistem].strip())

    def test_perintah_instalasi_cocok_untuk_mesin_ini(self):
        for kunci, tc in runner.TOOLCHAINS.items():
            if not tc.butuh:
                continue
            with self.subTest(bahasa=kunci):
                self.assertTrue(runner.perintah_instalasi(kunci).strip())

    def test_toolchain_tanpa_kebutuhan_selalu_tersedia(self):
        """Yang `butuh`-nya kosong harus benar-benar jalan di mana pun.

        Ini bukan sekadar konsekuensi logis: kalau suatu saat html/css diberi
        kebutuhan baru diam-diam, janji "bisa dikerjakan di komputer mana pun"
        ikut batal, dan yang menanggungnya adalah orang yang justru belum
        sanggup memasang apa-apa.
        """
        tanpa = [k for k, tc in runner.TOOLCHAINS.items() if not tc.butuh]
        self.assertEqual(sorted(tanpa), ["css", "html"])
        for kunci in tanpa:
            with self.subTest(bahasa=kunci):
                self.assertTrue(runner.tersedia(kunci))
                self.assertEqual(runner.program_hilang(kunci), [])
                self.assertEqual(runner.perintah_instalasi(kunci), "")

    def test_bahasa_tak_dikenal_memberi_string_kosong(self):
        self.assertEqual(runner.perintah_instalasi("klingon"), "")

    def test_batas_waktu_bahasa_terkompilasi_lebih_longgar(self):
        self.assertGreater(runner.batas_waktu("java"), runner.batas_waktu("python"))
        self.assertGreater(runner.batas_waktu("go"), runner.batas_waktu("python"))



if __name__ == "__main__":
    unittest.main(verbosity=2)
