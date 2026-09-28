"""Tes penentu instruksi berkas: nama, perintah, dan klasifikasi blok kode.

Yang paling dijaga di sini adalah SATU invarian: kalau aplikasi bilang sebuah
blok itu program utuh yang bisa disimpan lalu dijalankan, blok itu memang harus
bisa dikompilasi. Salah menyuruh pelajar menjalankan potongan kode jauh lebih
membingungkan daripada tidak memberi instruksi sama sekali.
"""

import os
import unittest

from inti import berkas
from inti import runner
from main import LANGUAGES

LEWATI_LAMBAT = os.environ.get("BELAJAR_SKIP_LAMBAT") == "1"


class TestSlug(unittest.TestCase):
    def test_membuang_nomor_urut_di_depan(self):
        self.assertEqual(berkas.slug("2. Variabel & Tipe Data"), "variabel-tipe-data")

    def test_membuang_kata_penghubung(self):
        self.assertEqual(berkas.slug("Contoh operator in & is"), "operator-in-is")

    def test_menghormati_batas_panjang(self):
        hasil = berkas.slug("Perulangan bersarang dengan banyak sekali kata tambahan")
        self.assertLessEqual(len(hasil), berkas.MAKS_SLUG)

    def test_tidak_diakhiri_tanda_hubung(self):
        for judul in ("1. A bcdefghijklmnopqrstuvwxyz", "Contoh", "3. X y z"):
            self.assertFalse(berkas.slug(judul).endswith("-"), judul)

    def test_judul_kosong_tetap_memberi_nama(self):
        self.assertTrue(berkas.slug(""))
        self.assertTrue(berkas.slug("   "))
        self.assertTrue(berkas.slug("123"))

    def test_hanya_huruf_angka_dan_hubung(self):
        hasil = berkas.slug("DDL: Membuat Struktur (Tabel)!")
        self.assertRegex(hasil, r"^[a-z0-9-]+$")


class TestNamaBerkas(unittest.TestCase):
    def test_java_memakai_nama_kelas_public(self):
        kode = "public class Hello { public static void main(String[] a) {} }"
        self.assertEqual(berkas.nama_berkas("java", kode, "apa saja"), "Hello.java")

    def test_java_mengabaikan_kelas_pembantu(self):
        kode = "class Bantu {}\npublic class Utama { }"
        self.assertEqual(berkas.nama_berkas("java", kode, ""), "Utama.java")

    def test_java_tanpa_kelas_memakai_konteks(self):
        self.assertEqual(berkas.nama_berkas("java", "int x = 1;", "2. Tipe Data"),
                         "TipeData.java")

    def test_go_selalu_main(self):
        self.assertEqual(berkas.nama_berkas("go", "package main", "apa pun"), "main.go")

    def test_ekstensi_sesuai_bahasa(self):
        for bahasa, ext in (("python", ".py"), ("javascript", ".js"),
                            ("c", ".c"), ("cpp", ".cpp"), ("bash", ".sh"),
                            ("sql", ".sql")):
            with self.subTest(bahasa=bahasa):
                self.assertTrue(
                    berkas.nama_berkas(bahasa, "x", "Contoh Kode").endswith(ext))

    def test_nama_java_selalu_diawali_huruf(self):
        # Identifier Java tidak boleh dimulai angka.
        nama = berkas.nama_berkas("java", "// kosong", "123 Angka")
        self.assertTrue(nama[0].isalpha(), nama)


class TestPerintahJalan(unittest.TestCase):
    def test_java_dua_langkah_kompilasi_lalu_jalan(self):
        p = berkas.perintah_jalan("java", "Hello.java")
        self.assertEqual(p, ["javac Hello.java", "java Hello"])

    def test_c_mengompilasi_ke_nama_yang_sama(self):
        p = berkas.perintah_jalan("c", "kalkulator.c")
        self.assertEqual(p, ["gcc kalkulator.c -o kalkulator", "./kalkulator"])

    def test_python_satu_perintah(self):
        self.assertEqual(berkas.perintah_jalan("python", "a.py"), ["python3 a.py"])

    def test_bahasa_tak_dikenal_tidak_memberi_perintah(self):
        self.assertEqual(berkas.perintah_jalan("cobol", "a.cob"), [])

    def test_perintah_menyebut_nama_berkasnya(self):
        for bahasa in ("python", "javascript", "java", "c", "cpp", "go", "bash"):
            nama = berkas.nama_berkas(bahasa, "", "Contoh")
            with self.subTest(bahasa=bahasa):
                self.assertIn(nama, " ".join(berkas.perintah_jalan(bahasa, nama)))


class TestKlasifikasi(unittest.TestCase):
    def test_python_program_utuh(self):
        self.assertEqual(berkas.jenis_kode("python", 'print("halo")'), berkas.PROGRAM)

    def test_python_sintaks_rusak_dianggap_potongan(self):
        self.assertEqual(berkas.jenis_kode("python", "def f(:\n  pass"), berkas.POTONGAN)

    def test_baris_pertama_menjorok_berarti_potongan(self):
        self.assertEqual(berkas.jenis_kode("python", "    x = 1\n    print(x)"),
                         berkas.POTONGAN)

    def test_elipsis_menandakan_kode_dipotong(self):
        kode = 'print("a")\n...\nprint("b")'
        self.assertEqual(berkas.jenis_kode("python", kode), berkas.POTONGAN)

    def test_java_tanpa_main_bukan_program(self):
        self.assertEqual(berkas.jenis_kode("java", "class A { int x; }"),
                         berkas.POTONGAN)

    def test_java_dengan_main_adalah_program(self):
        kode = "public class A { public static void main(String[] a) { } }"
        self.assertEqual(berkas.jenis_kode("java", kode), berkas.PROGRAM)

    def test_java_tanpa_import_yang_dipakai_bukan_program(self):
        kode = ("public class A { public static void main(String[] x) {"
                " List<String> d = null; } }")
        self.assertEqual(berkas.jenis_kode("java", kode), berkas.POTONGAN)

    def test_java_dengan_import_bintang_tetap_program(self):
        kode = ("import java.util.*;\npublic class A {"
                " public static void main(String[] x) { List<String> d = null; } }")
        self.assertEqual(berkas.jenis_kode("java", kode), berkas.PROGRAM)

    def test_go_butuh_package_main_dan_func_main(self):
        self.assertEqual(berkas.jenis_kode("go", "package kalkulator\nfunc F() {}"),
                         berkas.POTONGAN)
        self.assertEqual(berkas.jenis_kode("go", "package main\nfunc main() {}"),
                         berkas.PROGRAM)

    def test_c_butuh_fungsi_main(self):
        self.assertEqual(berkas.jenis_kode("c", "int tambah(int a){return a;}"),
                         berkas.POTONGAN)
        self.assertEqual(berkas.jenis_kode("c", "int main(void){return 0;}"),
                         berkas.PROGRAM)

    def test_sql_tanpa_create_table_diketik_di_sesi(self):
        self.assertEqual(berkas.jenis_kode("sql", "SELECT * FROM mahasiswa;"),
                         berkas.SESI)

    def test_sql_dengan_create_table_bisa_jadi_berkas(self):
        self.assertEqual(berkas.jenis_kode("sql", "CREATE TABLE t(a INT);"),
                         berkas.PROGRAM)

    def test_blok_kosong(self):
        self.assertEqual(berkas.jenis_kode("python", ""), berkas.POTONGAN)
        self.assertEqual(berkas.jenis_kode("python", "   \n  \n"), berkas.POTONGAN)


class TestMultiBerkas(unittest.TestCase):
    KODE = """/* ===== File: matematika.h ===== */
int tambah(int a, int b);

/* ===== File: matematika.c ===== */
#include "matematika.h"
int tambah(int a, int b) { return a + b; }

/* ===== File: main.c ===== */
#include <stdio.h>
int main(void) { printf("%d", tambah(1, 2)); return 0; }"""

    def test_terdeteksi_sebagai_multi(self):
        self.assertEqual(berkas.jenis_kode("c", self.KODE), berkas.MULTI)

    def test_semua_nama_berkas_terkumpul(self):
        self.assertEqual(berkas.berkas_ganda(self.KODE),
                         ["matematika.h", "matematika.c", "main.c"])

    def test_satu_penanda_saja_belum_dianggap_multi(self):
        self.assertEqual(berkas.berkas_ganda("// File: a.c\nint main(){}"), [])

    def test_instruksi_menyebut_semua_berkas(self):
        p = berkas.petunjuk_kode("c", self.KODE)
        for nama in ("matematika.h", "matematika.c", "main.c"):
            self.assertIn(nama, p.instruksi)

    def test_gaya_komentar_go_juga_dikenali(self):
        kode = ("// ==== file: kalkulator/kalkulator.go ====\npackage kalkulator\n"
                "// ==== file: kalkulator/kalkulator_test.go ====\npackage kalkulator")
        self.assertEqual(len(berkas.berkas_ganda(kode)), 2)


class TestIlustrasi(unittest.TestCase):
    def test_diagram_relasi(self):
        kode = ("Kategori ---punya banyak---> Item\n"
                "Item ---punya banyak---> Mutasi")
        self.assertEqual(berkas.jenis_kode("java", kode), berkas.ILUSTRASI)

    def test_peta_rute_dengan_placeholder_kurawal(self):
        kode = ("GET   /items                 daftar semua item\n"
                "POST  /items                 simpan item baru\n"
                "GET   /items/{id}            detail satu item\n"
                "GET   /items/{id}/edit       formulir ubah item")
        self.assertEqual(berkas.jenis_kode("java", kode), berkas.ILUSTRASI)

    def test_kode_sungguhan_tidak_salah_dikira_ilustrasi(self):
        kode = ('public class A {\n'
                '    public static void main(String[] x) {\n'
                '        System.out.println("halo");\n'
                '    }\n}')
        self.assertNotEqual(berkas.jenis_kode("java", kode), berkas.ILUSTRASI)

    def test_kode_berkolom_rapi_tetap_dianggap_kode(self):
        kode = ("a   = 1\n"
                "bb  = 22\n"
                "ccc = 333\n"
                "print(a, bb, ccc)")
        self.assertNotEqual(berkas.jenis_kode("python", kode), berkas.ILUSTRASI)


class TestPetunjuk(unittest.TestCase):
    def test_program_menyebut_nama_dan_perintah(self):
        p = berkas.petunjuk_kode("python", 'print("halo")', "Program pertama")
        self.assertEqual(p.jenis, berkas.PROGRAM)
        self.assertTrue(p.perlu_berkas)
        self.assertIn(".py", p.instruksi)
        self.assertTrue(p.perintah)

    def test_potongan_menyatakan_tidak_perlu_berkas(self):
        p = berkas.petunjuk_kode("python", "    x = 1")
        self.assertFalse(p.perlu_berkas)
        self.assertIn("tidak perlu", p.instruksi.lower())

    def test_sesi_sql_menyebut_database(self):
        p = berkas.petunjuk_kode("sql", "SELECT 1;")
        self.assertEqual(p.jenis, berkas.SESI)
        self.assertIn("database", p.instruksi.lower())

    def test_petunjuk_latihan_memakai_nama_yang_diberikan(self):
        p = berkas.petunjuk_latihan("java", "Latihan1.java")
        self.assertEqual(p.nama, "Latihan1.java")
        self.assertEqual(p.perintah, ["javac Latihan1.java", "java Latihan1"])

    def test_setiap_petunjuk_punya_instruksi_terisi(self):
        contoh = [("python", 'print(1)'), ("python", "    x=1"),
                  ("sql", "SELECT 1;"), ("java", "class A{}")]
        for bahasa, kode in contoh:
            with self.subTest(bahasa=bahasa, kode=kode[:20]):
                self.assertTrue(berkas.petunjuk_kode(bahasa, kode).instruksi.strip())


class TestSeluruhKontenPunyaInstruksi(unittest.TestCase):
    def test_tiap_blok_kode_materi_dapat_petunjuk(self):
        for lang in LANGUAGES:
            for m in lang["materials"]:
                for s in m["sections"]:
                    if not s.get("code"):
                        continue
                    konteks = s.get("heading") or m["title"]
                    with self.subTest(bahasa=lang["label"], materi=m["title"]):
                        p = berkas.petunjuk_kode(lang["runner"], s["code"], konteks)
                        self.assertIn(p.jenis, (berkas.PROGRAM, berkas.POTONGAN,
                                                berkas.SESI, berkas.MULTI,
                                                berkas.ILUSTRASI))
                        self.assertTrue(p.instruksi.strip())

    def test_nama_berkas_latihan_cocok_dengan_yang_dipakai_runner(self):
        """Instruksi yang ditampilkan harus sama dengan berkas yang benar-benar ditulis."""
        from layar.exercises import nama_kerja
        for lang in LANGUAGES:
            for ex in lang["exercises"]:
                with self.subTest(bahasa=lang["label"], latihan=ex["title"]):
                    nama = nama_kerja(ex, lang["runner"])
                    p = berkas.petunjuk_latihan(lang["runner"], nama)
                    self.assertEqual(p.nama, nama)
                    self.assertIn(nama, p.instruksi)

    def test_nama_kelas_java_cocok_dengan_nama_berkas_latihan(self):
        """javac menolak kalau nama kelas public beda dari nama berkas."""
        from layar.exercises import nama_kerja, _kerangka
        lang = next(l for l in LANGUAGES if l["runner"] == "java")
        for ex in lang["exercises"]:
            with self.subTest(latihan=ex["title"]):
                nama = nama_kerja(ex, "java")
                kelas = berkas._kelas_java(_kerangka("java", ex))
                self.assertEqual(nama, kelas + ".java")


@unittest.skipIf(LEWATI_LAMBAT, "dilewati lewat BELAJAR_SKIP_LAMBAT=1")
class TestLabelProgramTerbukti(unittest.TestCase):
    """Invarian utama: yang disebut program utuh harus benar-benar bisa dikompilasi."""

    def test_blok_berlabel_program_bisa_dikompilasi(self):
        for lang in LANGUAGES:
            bahasa = lang["runner"]
            if not runner.tersedia(bahasa):
                continue
            for m in lang["materials"]:
                for s in m["sections"]:
                    kode = s.get("code")
                    if not kode or berkas.jenis_kode(bahasa, kode) != berkas.PROGRAM:
                        continue
                    with self.subTest(bahasa=lang["label"], materi=m["title"],
                                      bagian=s.get("heading", "")):
                        galat = self._galat_sintaks(bahasa, kode)
                        self.assertIsNone(galat, galat)

    @staticmethod
    def _galat_sintaks(bahasa, kode):
        """Pesan error kalau kode gagal DIKOMPILASI. Gagal saat runtime diabaikan."""
        hasil = runner.cek_sintaks(bahasa, kode)
        if hasil is not None:
            return hasil.galat.strip()[:300]
        if bahasa in ("java", "c", "cpp", "go"):
            # Bahasa terkompilasi: jalankan, tapi hanya fase kompilasi yang dinilai.
            r = runner.jalankan(bahasa, kode, stdin="5\n5\n5\n", timeout=90)
            if r.fase == "kompilasi":
                return r.galat.strip()[:300]
        return None


class PagarPerintahSistem(unittest.TestCase):
    """Aplikasi TIDAK BOLEH menjalankan perintah sistem atas nama pelajar.

    Kurikulum CLI Fedora berisi perintah sungguhan: `sudo dnf5 install`,
    `systemctl enable`, `mkfs.ext4`, `rm`. Semuanya hanya bermakna kalau
    pelajar sendiri yang mengetiknya di terminalnya sendiri.

    Ini pernah bocor, dan bocornya lewat jalur yang tidak terlihat dari
    `jenis_kode`: klasifikasinya sudah benar (SESI), tapi webapp menghitung
    `bisa_dijalankan` sebagai `jenis in (PROGRAM, SESI)` -- aturan yang ditulis
    untuk SQL, di mana "sesi" berarti sqlite3 yang dinyalakan aplikasi sendiri
    dan memang aman. Akibatnya halaman materi Fedora memasang tombol Jalankan
    di empat blok perintah sekaligus, salah satunya rm.

    Karena itu yang diuji di sini BUKAN klasifikasinya, melainkan keputusan
    akhirnya: boleh atau tidak aplikasi mengeksekusi blok ini.
    """

    # Yang dilarang adalah kata kerja yang MENGUBAH, bukan nama perintahnya.
    # `systemctl is-system-running` dan `systemctl --failed` cuma bertanya, dan
    # skrip laporan kesehatan memang perlu bertanya. Melarang "systemctl "
    # begitu saja membuat tes ini menolak satu-satunya contoh yang justru
    # aman -- persis jenis pagar yang lama-lama dimatikan orang karena rewel.
    BERBAHAYA = ("sudo ", "mkfs", "rm -rf", "rm -f", "dd if=", "dd of=",
                 "setenforce", "cryptsetup", "chattr ", "semanage ",
                 "systemctl start", "systemctl stop", "systemctl restart",
                 "systemctl enable", "systemctl disable", "systemctl mask",
                 "systemctl isolate", "systemctl kill", "systemctl set-",
                 "firewall-cmd --add", "firewall-cmd --remove",
                 "firewall-cmd --set", "firewall-cmd --panic",
                 "dnf5 install", "dnf5 remove", "dnf5 upgrade",
                 "flatpak install", "flatpak uninstall",
                 "podman run", "podman rm", "podman system reset",
                 "btrfs subvolume delete", "lvremove", "lvreduce", "userdel")

    def test_blok_perintah_fedora_tidak_pernah_bisa_dijalankan_aplikasi(self):
        lang = next((l for l in LANGUAGES if l["key"] == "fedora"), None)
        if lang is None:
            self.skipTest("kurikulum fedora tidak terpasang")
        diperiksa = 0
        for m in lang["materials"]:
            for s in m["sections"]:
                kode = s.get("code")
                if not kode:
                    continue
                jenis = berkas.jenis_kode("fedora", kode)
                boleh = berkas.boleh_dijalankan_aplikasi("fedora", jenis)
                if not boleh:
                    diperiksa += 1
                    continue
                # Yang lolos HARUS skrip berpenanda shebang, dan skrip contoh
                # pun tidak boleh membawa perintah yang mengubah sistem.
                with self.subTest(materi=m["title"]):
                    self.assertTrue(
                        kode.lstrip().startswith("#!"),
                        f"blok tanpa shebang boleh dijalankan aplikasi:\n"
                        f"{kode[:200]}")
                    for kata in self.BERBAHAYA:
                        self.assertNotIn(
                            kata, kode,
                            f"skrip contoh yang bisa dijalankan aplikasi memuat "
                            f"{kata.strip()!r} -- ia akan mengubah sistem pelajar")
                diperiksa += 1
        self.assertGreater(diperiksa, 100, "blok materi Fedora tidak terbaca")

    def test_sesi_sql_tetap_boleh_dijalankan(self):
        """Pagar di atas tidak boleh ikut mematikan SQL.

        SESI milik SQL adalah sqlite3 yang dinyalakan aplikasi sendiri, dan
        menjalankannya memang gunanya. Tanpa tes ini, "amankan Fedora" gampang
        berubah jadi "matikan SESI di mana-mana".
        """
        self.assertTrue(berkas.boleh_dijalankan_aplikasi("sql", berkas.SESI))
        self.assertFalse(berkas.boleh_dijalankan_aplikasi("fedora", berkas.SESI))
        self.assertTrue(berkas.boleh_dijalankan_aplikasi("fedora", berkas.PROGRAM))
        self.assertFalse(berkas.boleh_dijalankan_aplikasi("python", berkas.POTONGAN))


if __name__ == "__main__":
    unittest.main(verbosity=2)
