"""Tes penerjemah pesan error.

Dua sifat yang dijaga: terjemahannya benar-benar mengenali pesan yang dimaksud,
dan nomor baris yang digeser menunjuk ke berkas milik pelajar -- bukan ke berkas
sementara gabungan setup + kode yang tidak pernah dia lihat.
"""

import unittest

import galat


class TestTerjemahkan(unittest.TestCase):
    KASUS = [
        ("/tmp/belajar-x/Halo.java:3: error: ';' expected", "titik koma"),
        ("Halo.java:5: error: cannot find symbol\n  symbol: variable nilai", "nilai"),
        ("NameError: name 'nilai' is not defined", "nilai"),
        ("IndentationError: unexpected indent", "indentasi"),
        ("TypeError: unsupported operand type(s) for +: 'int' and 'str'", "teks"),
        ("ValueError: invalid literal for int() with base 10: 'abc'", "angka"),
        ("IndexError: list index out of range", "jangkauan"),
        ("ZeroDivisionError: division by zero", "nol"),
        ("prog.c:5: warning: implicit declaration of function 'printf'", "include"),
        ("undefined reference to `main'", "main()"),
        ("./main.go:7:2: \"os\" imported and not used", "import"),
        ("x declared and not used", "tidak pernah dipakai"),
        ("ReferenceError: total is not defined", "total"),
        ("line 3: syntax error near unexpected token `='", "spasi"),
        ("Parse error: near \"AUTO_INCREMENT\": syntax error", "MySQL"),
        ("Error: no such table: produk", "produk"),
        ("Exception in thread \"main\" java.lang.NullPointerException", "null"),
    ]

    def test_pesan_umum_diterjemahkan(self):
        for pesan, kata in self.KASUS:
            with self.subTest(pesan=pesan[:40]):
                hasil = galat.terjemahkan(pesan)
                self.assertTrue(hasil, "tidak ada terjemahan sama sekali")
                gabung = " ".join(hasil).lower()
                self.assertIn(kata.lower(), gabung)

    def test_pesan_tak_dikenal_tidak_dikarang(self):
        self.assertEqual(galat.terjemahkan("blorp zorp qux 12345"), [])

    def test_pesan_kosong(self):
        self.assertEqual(galat.terjemahkan(""), [])
        self.assertEqual(galat.terjemahkan(None), [])

    def test_jumlah_terjemahan_dibatasi(self):
        banyak = "\n".join(p for p, _ in self.KASUS)
        self.assertLessEqual(len(galat.terjemahkan(banyak, maks=3)), 3)

    def test_hasil_selalu_satu_baris(self):
        for pesan, _ in self.KASUS:
            for t in galat.terjemahkan(pesan):
                self.assertNotIn("\n", t)


class TestRapikan(unittest.TestCase):
    def test_path_sementara_diganti_nama_berkas_pelajar(self):
        hasil = galat.rapikan("/tmp/belajar-ab12/Halo.java:3: error: x", "Latihan3.java")
        self.assertNotIn("/tmp/", hasil)
        self.assertIn("Latihan3.java", hasil)

    def test_nomor_baris_digeser_sebanyak_baris_setup(self):
        hasil = galat.rapikan("Latihan.sql:17: error", "Latihan.sql", baris_setup=14)
        self.assertIn("Latihan.sql:3:", hasil)

    def test_baris_di_dalam_setup_ditandai_jelas(self):
        hasil = galat.rapikan("Latihan.sql:5: error", "Latihan.sql", baris_setup=14)
        self.assertIn("KONDISI AWAL", hasil)

    def test_kolom_tidak_ikut_digeser(self):
        hasil = galat.rapikan("prog.c:20:8: error", "prog.c", baris_setup=10)
        self.assertIn("prog.c:10:8", hasil)

    def test_kata_line_juga_digeser(self):
        hasil = galat.rapikan("Parse error near line 15:", "x.sql", baris_setup=14)
        self.assertIn("line 1:", hasil)

    def test_tanpa_setup_nomor_baris_tidak_berubah(self):
        asli = "Halo.java:3: error: x"
        self.assertEqual(galat.rapikan(asli, "Halo.java", 0), asli)

    def test_pesan_kosong_aman(self):
        self.assertEqual(galat.rapikan("", "x.py", 3), "")
        self.assertIsNone(galat.rapikan(None, "x.py", 3))


class TestRingkas(unittest.TestCase):
    def test_pesan_pendek_utuh(self):
        self.assertEqual(galat.ringkas("satu\ndua"), ["satu", "dua"])

    def test_traceback_diambil_dari_ujung(self):
        baris = ["Traceback (most recent call last):"] + [f"  frame {i}" for i in range(30)]
        baris.append("ValueError: pesan penting")
        hasil = galat.ringkas("\n".join(baris), maks_baris=5)
        self.assertIn("ValueError: pesan penting", hasil[-1])
        self.assertLessEqual(len(hasil), 5)

    def test_keluaran_kompiler_diambil_dari_awal(self):
        baris = [f"error {i}" for i in range(40)]
        hasil = galat.ringkas("\n".join(baris), maks_baris=5)
        self.assertIn("error 0", hasil[0])
        self.assertLessEqual(len(hasil), 5)

    def test_baris_kosong_dibuang(self):
        self.assertEqual(galat.ringkas("a\n\n\nb"), ["a", "b"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
