"""Tes eksekusi kode: keluaran, error, batas waktu, dan pencocokan jawaban."""

import ast
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from inti import galat as modul_galat
from inti import runner


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


# Program yang PASTI gagal di tiap bahasa yang bisa mewarnai pesan galatnya.
# Kuncinya wajib ada di TOOLCHAINS; sel di bawah yang menegurnya kalau tidak.
_RAJAH_GAGAL = {
    "python": "x = 1 / 0\n",
    "javascript": "const x = 1;\nundefined.bukan\n",
}


def _setel_kenop(nama, isi):
    """Setel satu variabel lingkungan; `isi` None berarti dicabut."""
    if isi is None:
        os.environ.pop(nama, None)
    else:
        os.environ[nama] = isi


def _cacah_esc(hasil):
    """Berapa byte ESC yang sampai ke teks yang dilihat pelajar."""
    return (hasil.keluaran + hasil.galat).count("\x1b")


class TestLingkunganAnak(unittest.TestCase):
    """Saluran keluar anak selalu berkas, jadi warna paksaan induk cuma merusak.

    `_proses` membuka stdout/stderr anak sebagai berkas di dalam direktori
    sementara -- tidak pernah tty. Kalau `FORCE_COLOR` milik lingkungan induk
    diwarisi apa adanya, anak tetap menulis kode ANSI ke berkas itu, dan
    keluarannya ditampilkan apa adanya ke pelajar: pesan galat berisi sampah
    `ESC[35m`, DAN regex penunjuk nomor baris di `galat.py` berhenti cocok
    sehingga "loncat ke baris" hilang tanpa satu pun pesan galat.
    """

    def setUp(self):
        # Kenop dipulihkan lewat addCleanup, bukan finally: tes di bawah
        # menyetelnya berkali-kali di dalam satu loop, dan assert yang gagal
        # di tengah tidak boleh meninggalkan kenop itu menetes ke tes lain.
        self.addCleanup(_setel_kenop, "FORCE_COLOR", os.environ.get("FORCE_COLOR"))

    def test_force_color_induk_tidak_mewarnai_keluaran_anak(self):
        """Tiga keadaan kenop induk, dan ketiganya wajib bersih.

        `None` adalah kontrolnya: pagar tidak boleh cerewet, yang bersih tanpa
        kenop harus tetap bersih sesudah pagar dipasang. `"0"` ikut diuji
        karena di CPython nilai tak-kosong apa pun MEMAKSA warna nyala.
        """
        diuji = 0
        for bahasa, kode in _RAJAH_GAGAL.items():
            self.assertIn(bahasa, runner.TOOLCHAINS, "rajah untuk bahasa asing")
            if not runner.tersedia(bahasa):
                continue
            diuji += 1
            for kenop in (None, "1", "0"):
                with self.subTest(bahasa=bahasa, force_color=kenop):
                    _setel_kenop("FORCE_COLOR", kenop)
                    hasil = runner.jalankan(bahasa, kode, timeout=30)
                    self.assertFalse(hasil.sukses, "rajah ini harus gagal")
                    self.assertEqual(
                        _cacah_esc(hasil), 0,
                        f"kode ANSI bocor ke keluaran anak: {hasil.galat!r}")
        if not diuji:
            self.skipTest("tidak satu pun toolchain berajah terpasang di mesin ini")

    @butuh("python")
    def test_nomor_baris_tetap_ditemukan_dan_tetap_bisa_digeser(self):
        """Unit kontrak hilir: yang dijaga bukan warnanya, tapi nomor barisnya.

        Pergeseran `baris_setup` hari ini tidak bisa dicapai lewat kurikulum --
        nol dari 19 latihan Python dan nol dari 22 latihan JavaScript punya
        `setup`, dan yang punya cuma SQL, yang pesan galatnya tidak berwarna.
        Justru itu sebabnya ditulis sebagai unit: kontraknya harus berdiri
        sebelum latihan ber-`setup` pertama untuk kedua bahasa itu ditulis.
        """
        _setel_kenop("FORCE_COLOR", "1")
        hasil = runner.jalankan("python", _RAJAH_GAGAL["python"], timeout=30)
        self.assertFalse(hasil.sukses)

        nomor = [n for _, n in modul_galat._POLA_KATA_LINE.findall(hasil.galat)]
        self.assertIn("1", nomor, f"nomor baris tak terbaca lagi: {hasil.galat!r}")

        rapi = modul_galat.rapikan(hasil.galat, "program.py", 3)
        self.assertIn("line [bagian KONDISI AWAL]", rapi)
        self.assertNotIn("line 1", rapi, "nomor baris lolos tanpa digeser")

    def test_pagar_berlaku_untuk_setiap_toolchain(self):
        """Dipanggil langsung, supaya toolchain yang belum terpasang ikut diuji.

        `tc.lingkungan` di-`update()` paling akhir di `_lingkungan()`, jadi
        toolchain baru yang suatu hari menyisipkan `FORCE_COLOR` sendiri akan
        membatalkan pagar ini -- dan sel inilah yang menegurnya.
        """
        _setel_kenop("FORCE_COLOR", "1")
        cwd = tempfile.gettempdir()
        for bahasa, tc in runner.TOOLCHAINS.items():
            with self.subTest(bahasa=bahasa):
                lingkungan = runner._lingkungan(cwd, tc)
                self.assertNotIn("FORCE_COLOR", lingkungan)


# ------------------------------------------------- jalur anak di luar pagar
#
# Pagar di atas duduk di `_lingkungan()`, dan HANYA `_proses()` memakainya.
# `_tfm_dotnet()` memanggil `subprocess.run` sendiri lalu MENGURAI
# keluarannya -- kelas cacat yang lebih mahal daripada warna yang bocor,
# sebab yang rusak bukan tampilan melainkan keputusan: `int("9\x1b[0m")`
# melempar ValueError, fallback menang, dan tidak ada satu pun pesan yang
# menyebut warna, lingkungan, maupun TFM.

_STUB_DOTNET = """#!/bin/sh
# Stub `dotnet` ronde t11b. SDK palsunya 9.0.100, dan ia mewarnai
# keluarannya begitu FORCE_COLOR diwarisi -- itu persis keadaan yang
# membuat penguraian di `_tfm_dotnet` jatuh ke fallback tanpa suara.
if [ -n "${FORCE_COLOR-}" ]; then
    printf '\\033[32m9.0.100\\033[0m\\n'
else
    printf '9.0.100\\n'
fi
"""

# Yang menentukan TFM seluruh latihan C#/VB satu sesi bukan hasil panggilan
# per latihan, melainkan konstanta modul yang dihitung SEKALI saat impor.
_PENGEMUDI_TFM = "from inti import runner; print('TFM=' + runner._TFM_DOTNET)"

_PANGGILAN_ANAK = frozenset({
    "run", "Popen", "call", "check_output", "check_call",
    "getoutput", "getstatusoutput",
})

_PAKET_PRODUKSI = ("inti", "pelajar", "layar", "webapp")
_AKAR_PRODUKSI = ("main.py", "belajar-web.py")

# Situs di tingkat modul tidak punya fungsi pembungkus; ia tetap butuh nama
# supaya kunci whitelist-nya bisa ditulis orang.
_MODUL = "<modul>"

# Kunci = (berkas, nama fungsi), BUKAN nomor baris: nomor baris bergerak tiap
# ronde, dan ampunan yang alamatnya basi berhenti menjaga apa pun. Tiap entri
# membawa sebabnya, dan entri yang tidak menutupi satu pun situs ikut memerah.
DIIZINKAN_MEWARISI = {
    ("inti/runner.py", "_sqlite_aman"):
        "hanya membaca returncode; keluarannya tidak pernah diurai",
    ("layar/exercises.py", "tulis_kode"):
        "$EDITOR di tty pelajar; tidak ada teks yang diparsing",
}


def _akar_repo():
    """Akar diturunkan dari `runner.__file__`, bukan dari cwd atau `__file__`.

    Baterai mutasi berjalan di salinan rata, dan sapuan yang melacak cwd akan
    membaca pohon ASLI sambil mengira sedang membaca salinan -- merah palsu di
    satu arah, hijau palsu di arah lain.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(runner.__file__)))


def _berkas_produksi(akar):
    """Sumber yang dijalankan aplikasi: empat paket + dua titik masuk akar.

    `tests/` jelas di luar (ia memang menjalankan anak untuk menguji), dan
    `data/` juga: yang ada di sana teks materi, bukan jalur yang dieksekusi.
    """
    ditemukan = []
    for paket in _PAKET_PRODUKSI:
        for induk, anak, berkas in os.walk(os.path.join(akar, paket)):
            anak[:] = [d for d in anak if d != "__pycache__"]
            for nama in berkas:
                if nama.endswith(".py"):
                    ditemukan.append(os.path.join(induk, nama))
    for nama in _AKAR_PRODUKSI:
        jalur = os.path.join(akar, nama)
        if os.path.exists(jalur):
            ditemukan.append(jalur)
    return sorted(ditemukan)


class _SapuAnak(ast.NodeVisitor):
    """Memetakan tiap `subprocess.<X>(...)` ke nama fungsi pembungkusnya.

    AST, bukan `grep`: nama fungsi pembungkus tidak bisa dibaca dari sebuah
    baris, dan justru fungsi itulah kunci whitelist-nya.
    """

    def __init__(self, berkas):
        self.berkas = berkas
        self.tumpukan = []
        self.situs = []

    def _masuk_fungsi(self, node):
        self.tumpukan.append(node.name)
        self.generic_visit(node)
        self.tumpukan.pop()

    visit_FunctionDef = _masuk_fungsi
    visit_AsyncFunctionDef = _masuk_fungsi

    def visit_Call(self, node):
        fungsi = node.func
        if (isinstance(fungsi, ast.Attribute)
                and fungsi.attr in _PANGGILAN_ANAK
                and isinstance(fungsi.value, ast.Name)
                and fungsi.value.id == "subprocess"):
            self.situs.append((
                self.berkas,
                self.tumpukan[-1] if self.tumpukan else _MODUL,
                fungsi.attr,
                node.lineno,
                any(kata.arg == "env" for kata in node.keywords),
            ))
        self.generic_visit(node)


def _situs_anak(akar):
    """Seluruh situs panggilan anak di produksi, berikut ada-tidaknya `env=`."""
    situs = []
    for jalur in _berkas_produksi(akar):
        with open(jalur, encoding="utf-8") as f:
            sumber = f.read()
        sapu = _SapuAnak(os.path.relpath(jalur, akar).replace(os.sep, "/"))
        sapu.visit(ast.parse(sumber, filename=jalur))
        situs.extend(sapu.situs)
    return situs


class TestJalurAnakTanpaPagar(unittest.TestCase):
    """`_tfm_dotnet()` mengambil keputusan dari teks yang bisa disusupi.

    Seluruh pembuktian di sini lewat STUB, karena `dotnet` tidak terpasang di
    mesin ini -- dan stub yang diam membuat tes berikutnya lolos palsu, jadi
    metode pertama tidak boleh bisa lulus karena tidak melakukan apa pun.
    """

    def setUp(self):
        self.addCleanup(_setel_kenop, "FORCE_COLOR", os.environ.get("FORCE_COLOR"))
        self.addCleanup(_setel_kenop, "PATH", os.environ.get("PATH"))
        self.sarang = os.path.join(_akar_repo(), "__pycache__", "t11bh1", "stub")
        os.makedirs(self.sarang, exist_ok=True)
        self.addCleanup(shutil.rmtree, self.sarang, ignore_errors=True)
        self.stub = os.path.join(self.sarang, "dotnet")
        with open(self.stub, "w", encoding="utf-8") as f:
            f.write(_STUB_DOTNET)
        os.chmod(self.stub, 0o755)
        os.environ["PATH"] = self.sarang + os.pathsep + os.environ.get("PATH", "")

    def _probe(self):
        return subprocess.run(["dotnet", "--version"],
                              capture_output=True, text=True, timeout=20)

    def test_stub_membayangi_dotnet_dan_mewarnai_hanya_saat_dipaksa(self):
        """Fondasinya: stub yang tidak membayangi membuat tiga metode di bawah
        lolos tanpa menguji apa pun, jadi kegagalannya `fail`, bukan `skipTest`.
        """
        terpilih = shutil.which("dotnet")
        if terpilih != self.stub:
            self.fail(f"stub tidak membayangi: which('dotnet')={terpilih!r} "
                      f"bukan {self.stub!r}; PATH={os.environ['PATH']!r}")

        _setel_kenop("FORCE_COLOR", "1")
        berwarna = self._probe()
        esc = berwarna.stdout.count("\x1b")
        if esc < 1:
            self.fail(f"stub tidak mewarnai saat FORCE_COLOR=1 -- tanpa ANSI "
                      f"tidak ada yang dibuktikan: stdout={berwarna.stdout!r}")

        _setel_kenop("FORCE_COLOR", None)
        bersih = self._probe()
        if bersih.stdout.count("\x1b") != 0:
            self.fail(f"stub mewarnai tanpa diminta, jadi sisi kontrol di bawah "
                      f"tidak berarti: stdout={bersih.stdout!r}")
        self.assertIn("9.0.100", bersih.stdout, "SDK palsunya harus 9.0.100")

    def test_tfm_tidak_tertipu_warna_paksaan_induk(self):
        """Kontraknya: SDK 9.0.100 berarti `net9.0`, berapa pun kenop induknya."""
        _setel_kenop("FORCE_COLOR", "1")
        tfm = runner._tfm_dotnet()
        self.assertEqual(
            tfm, "net9.0",
            f"TFM={tfm!r}. Dua bentuk salah yang sudah terukur dan DITOLAK "
            f"keduanya: 'net8.0' berarti ANSI membuat int() melempar dan "
            f"fallback menang diam-diam; 'net32.0' berarti penguraiannya "
            f"toleran tanpa menyeka kenop, dan angka 32 itu diambil dari "
            f"ESC[32m -- nomor warna dibaca sebagai nomor versi.")

    def test_tfm_tetap_benar_tanpa_kenop_di_induk(self):
        """Kontrol: pagar tidak boleh cerewet, dan tidak boleh mengubah jalur
        yang hari ini sudah benar."""
        _setel_kenop("FORCE_COLOR", None)
        tfm = runner._tfm_dotnet()
        self.assertEqual(tfm, "net9.0",
                         f"TFM={tfm!r} pada jalur yang tanpa pagar pun benar")

    def test_konstanta_modul_ikut_terjaga_saat_impor(self):
        """Yang menentukan TFM pelajar adalah `_TFM_DOTNET` di `:144`.

        Pagar di dalam fungsi belum terbukti sampai ke sana, karena konstanta
        itu dihitung SEKALI saat `inti/runner.py` diimpor. Sisi tanpa kenop
        ikut diadu dan ikut dicetak: pada pohon yang sama-sama sakit, sisi itu
        memberi `net9.0` dan HIJAU -- jadi tes yang lupa menyetel kenop tidak
        membuktikan apa pun, dan harus bisa terlihat tidak membuktikan apa pun.
        """
        akar = _akar_repo()
        for kenop in ("1", None):
            with self.subTest(force_color=kenop):
                lingkungan = os.environ.copy()
                if kenop is None:
                    lingkungan.pop("FORCE_COLOR", None)
                else:
                    lingkungan["FORCE_COLOR"] = kenop
                anak = subprocess.run(
                    [sys.executable, "-B", "-c", _PENGEMUDI_TFM],
                    cwd=akar, env=lingkungan,
                    capture_output=True, text=True, timeout=120)
                self.assertIn(
                    "TFM=net9.0", anak.stdout,
                    f"impor dengan FORCE_COLOR={kenop!r} di {akar!r} memberi "
                    f"stdout={anak.stdout!r} galat={anak.stderr!r}")

    def test_tiap_jalur_anak_punya_env_atau_punya_sebab(self):
        """Pagar struktur, supaya jalur anak ketiga tidak lahir diam-diam.

        Dua arah, dan arah baliknya yang penting: ampunan yang tidak menutupi
        satu pun situs ikut memerah, karena exemption yang tidak dibeli adalah
        exemption yang akan diwarisi bahasa berikutnya tanpa ada yang
        membacanya.
        """
        akar = _akar_repo()
        situs = _situs_anak(akar)

        alamat = {(b, f) for b, f, _, _, _ in situs}
        self.assertIn(("inti/runner.py", "_proses"), alamat,
                      f"sapuan tidak menemukan jalur anak yang sudah pasti ada "
                      f"-- bentuk penguraiannya yang salah, bukan pohonnya. "
                      f"akar={akar!r} situs={situs!r}")
        self.assertGreaterEqual(len(situs), 4, f"situs terbaca: {situs!r}")

        melanggar = [s for s in situs
                     if not s[4] and (s[0], s[1]) not in DIIZINKAN_MEWARISI]
        self.assertEqual(
            melanggar, [],
            f"jalur anak tanpa `env=` dan tanpa sebab tertulis: "
            f"{[(b, f, a, n) for b, f, a, n, _ in melanggar]}. Kirim lingkungan "
            f"yang sudah diseka lewat `env=`, atau belilah ampunannya dengan "
            f"satu baris sebab di DIIZINKAN_MEWARISI.")

        dipakai = {(b, f) for b, f, _, _, ada in situs if not ada}
        mati = sorted(set(DIIZINKAN_MEWARISI) - dipakai)
        self.assertEqual(
            mati, [],
            f"ampunan yang tidak menutupi satu pun situs tanpa `env=`: {mati}. "
            f"Hapus entrinya -- ampunan yang tidak dibeli akan diwarisi tanpa "
            f"dibaca. Situs tanpa `env=` hari ini: {sorted(dipakai)}")


@unittest.skipIf(os.name == "nt", "grup proses POSIX")
class TestTidakAdaProsesYatim(unittest.TestCase):
    """Anak latar yang ditinggal program yang SELESAI NORMAL ikut dibunuh.

    Audit 2026-10-17: `os.system("sleep 300 &")` lewat /api/coba selesai dengan
    rc=0 dan `sleep 300` masih hidup sesudahnya. Pelajar yang mencoba server
    kecil atau `&` di latihan Bash akan menumpuk proses sampai reboot.
    """

    def test_anak_latar_mati_sesudah_program_selesai(self):
        if not runner.tersedia("python"):
            self.skipTest("python tidak tersedia")
        kode = ("import subprocess, sys\n"
                "p = subprocess.Popen(['sleep', '300'])\n"
                "print(p.pid)\n")
        hasil = runner.jalankan("python", kode, timeout=10)
        self.assertEqual(hasil.kode_keluar, 0, hasil.galat)
        pid = int(hasil.keluaran.strip())
        for _ in range(50):
            try:
                os.kill(pid, 0)
            except ProcessLookupError:
                return
            time.sleep(0.05)
        try:
            os.kill(pid, 9)
        finally:
            self.fail(f"proses anak {pid} masih hidup sesudah program selesai")


if __name__ == "__main__":
    unittest.main(verbosity=2)
