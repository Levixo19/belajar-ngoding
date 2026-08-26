"""Tes penyorot sintaks.

Satu properti menentukan segalanya di sini: pemindai TIDAK BOLEH kehilangan
satu karakter pun. Kalau ia menelan karakter, contoh kode yang dilihat pelajar
berbeda dari kode yang sebenarnya -- kesalahan paling berbahaya untuk sebuah
aplikasi belajar.
"""

import unittest

import sorot
import tema
from main import LANGUAGES


def semua_potongan_kode():
    """(bahasa, judul, kode) untuk seluruh kode di kurikulum."""
    for lang in LANGUAGES:
        b = lang["runner"]
        for m in lang["materials"]:
            for s in m["sections"]:
                if s.get("code"):
                    yield b, m["title"], s["code"]
        for e in lang["exercises"]:
            yield b, e["title"], e["solution"]
            if e.get("setup"):
                yield b, e["title"] + " (setup)", e["setup"]
            if e.get("verifikasi"):
                yield b, e["title"] + " (verifikasi)", e["verifikasi"]


class TestKeutuhan(unittest.TestCase):
    def test_seluruh_kode_kurikulum_utuh_setelah_ditokenkan(self):
        jumlah = 0
        for bahasa, judul, kode in semua_potongan_kode():
            jumlah += 1
            with self.subTest(bahasa=bahasa, judul=judul):
                self.assertEqual(sorot.polos(kode, bahasa), kode)
        self.assertGreater(jumlah, 250, "kurikulum menyusut drastis?")

    def test_jumlah_baris_tidak_berubah(self):
        for bahasa, judul, kode in semua_potongan_kode():
            with self.subTest(bahasa=bahasa, judul=judul):
                self.assertEqual(len(sorot.sorot_baris(kode, bahasa)),
                                 len(kode.split("\n")))

    def test_kode_rusak_tetap_utuh(self):
        rusak = [
            'print("belum ditutup',
            "/* komentar tanpa penutup",
            "x = '''kutip tiga menggantung",
            "func main() { `raw string menggantung",
            "#include <stdio.h",
            "\\",
            "",
        ]
        for bahasa in sorot.bahasa_didukung():
            for kode in rusak:
                with self.subTest(bahasa=bahasa, kode=kode[:20]):
                    self.assertEqual(sorot.polos(kode, bahasa), kode)

    def test_bahasa_tak_dikenal_tidak_meledak(self):
        kode = "beberapa teks 123 // apa saja"
        self.assertEqual(sorot.polos(kode, "klingon"), kode)


class TestPenandaanToken(unittest.TestCase):
    def _jenis(self, kode, bahasa):
        return {teks: jenis for jenis, teks in sorot.token(kode, bahasa)}

    def test_komentar_python(self):
        jenis = dict((t, j) for j, t in sorot.token("x = 1  # catatan", "python"))
        self.assertEqual(jenis["# catatan"], "komentar")

    def test_string_kutip_tiga_python(self):
        kode = 'a = """dua\nbaris"""'
        potongan = [t for j, t in sorot.token(kode, "python") if j == "string"]
        self.assertEqual(potongan, ['"""dua\nbaris"""'])

    def test_kata_kunci_sql_tidak_bergantung_kapital(self):
        for kata in ("select", "SELECT", "SeLeCt"):
            jenis = [j for j, t in sorot.token(kata + " 1", "sql") if t == kata]
            self.assertEqual(jenis, ["kunci"], kata)

    def test_praprosesor_c_bukan_komentar(self):
        jenis = [j for j, t in sorot.token("#include <stdio.h>\nint x;", "c")
                 if t.startswith("#include")]
        self.assertEqual(jenis, ["khusus"])

    def test_shebang_bash_dianggap_komentar(self):
        jenis = [j for j, t in sorot.token("#!/usr/bin/env bash\necho hai", "bash")
                 if t.startswith("#!")]
        self.assertEqual(jenis, ["komentar"])

    def test_variabel_dolar_bash(self):
        for kode in ("echo $nama", "echo ${nama}", "echo $1", "echo $?"):
            khusus = [t for j, t in sorot.token(kode, "bash") if j == "khusus"]
            self.assertTrue(khusus, kode)

    def test_raw_string_go_boleh_lintas_baris(self):
        kode = "s := `satu\ndua`"
        potongan = [t for j, t in sorot.token(kode, "go") if j == "string"]
        self.assertEqual(potongan, ["`satu\ndua`"])

    def test_kutip_tunggal_menggantung_berhenti_di_akhir_baris(self):
        kode = "echo 'belum ditutup\necho lanjut"
        potongan = [t for j, t in sorot.token(kode, "bash") if j == "string"]
        self.assertNotIn("\n", potongan[0], "string menelan baris berikutnya")

    def test_nama_fungsi_dikenali(self):
        jenis = [j for j, t in sorot.token("hitungLuas(4)", "java") if t == "hitungLuas"]
        self.assertEqual(jenis, ["fungsi"])

    def test_angka_dalam_berbagai_bentuk(self):
        for kode in ("0xFF", "1_000", "3.14", "2e10", "10L", "1.5f"):
            angka = [t for j, t in sorot.token("x = " + kode, "java") if j == "angka"]
            self.assertEqual(angka, [kode], kode)


class TestKeluaran(unittest.TestCase):
    def test_tanpa_warna_hasilnya_sama_dengan_kode_asli(self):
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            kode = 'print("halo")  # komentar'
            self.assertEqual(sorot.sorot(kode, "python"), kode)
        finally:
            tema.pakai_kedalaman(asli)

    def test_setiap_baris_menutup_kode_warnanya_sendiri(self):
        """Kode warna yang menggantung antar baris akan bocor saat paginasi."""
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.WARNA_PENUH)
            kode = 'def f():\n    """dok\n    banyak baris"""\n    return 1'
            for baris in sorot.sorot_baris(kode, "python"):
                if "\033[" in baris:
                    self.assertTrue(baris.endswith(tema.RESET),
                                    f"warna menggantung: {baris!r}")
        finally:
            tema.pakai_kedalaman(asli)

    def test_awalan_ditempel_di_setiap_baris(self):
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            baris = sorot.sorot_baris("a\nb\nc", "python", awalan="  ")
            self.assertEqual(baris, ["  a", "  b", "  c"])
        finally:
            tema.pakai_kedalaman(asli)


if __name__ == "__main__":
    unittest.main(verbosity=2)
