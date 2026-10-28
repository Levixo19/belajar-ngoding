"""Tes penerjemah pesan error.

Dua sifat yang dijaga: terjemahannya benar-benar mengenali pesan yang dimaksud,
dan nomor baris yang digeser menunjuk ke berkas milik pelajar -- bukan ke berkas
sementara gabungan setup + kode yang tidak pernah dia lihat.
"""

import concurrent.futures
import hashlib
import json
import os
import re
import unittest

from inti import galat, runner


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


# ---------------------------------------------------------------------------
# Ruby, Rust, C#, Visual Basic, PHP, Kotlin, dan TypeScript (2026-10-28)
#
# Semua pesan di bawah ditangkap dari toolchain sungguhan lewat
# `runner.jalankan`, bukan ditulis dari ingatan; yang diganti cuma jalur
# direktori sementara (jadi /tmp/x). Dua sifat yang dijaga: tiap pesan
# diterjemahkan oleh pola yang menyebut kejadiannya, dan pesan bahasa LAIN
# tidak berubah hasilnya.


class TestBahasaBaruPesanNyata(unittest.TestCase):
    # (bahasa, pesan nyata, potongan penjelasan yang diharapkan, huruf kecil).
    # Potongannya sengaja memuat nilai yang diambil dari pesan (nama variabel,
    # tipe, angka), supaya rujukan grup \1, \2 ikut teruji, bukan cuma
    # kecocokan polanya.
    KASUS = [
        ("ruby", "/tmp/x/program.rb:1:in '<main>': undefined local variable or method 'x' for main (NameError)",
                "nama 'x' tidak dikenal"),
        ("ruby", "/tmp/x/program.rb:2:in '<main>': undefined method 'upcase' for nil (NoMethodError)",
                "method 'upcase' dipanggil pada nilai nil"),
        ("ruby", "/tmp/x/program.rb:1:in '<main>': undefined method 'foo' for an instance of Integer (NoMethodError)",
                "objek bertipe integer tidak punya method 'foo'"),
        ("ruby", "/tmp/x/program.rb:1:in 'Kernel#Integer': invalid value for Integer(): \"abc\" (ArgumentError)",
                "integer() menolak teks \"abc\""),
        ("ruby", "/tmp/x/program.rb:1:in 'Object#f': wrong number of arguments (given 1, expected 2) (ArgumentError)",
                "dipanggil dengan 1 argumen, padahal definisinya meminta 2"),
        ("ruby", "/tmp/x/program.rb:2:in 'Array#fetch': index 5 outside of array bounds: -2...2 (IndexError)",
                "indeks 5 di luar jangkauan array"),
        ("ruby", "/tmp/x/program.rb:1:in 'String#+': no implicit conversion of Integer into String (TypeError)",
                "tidak mengubah integer jadi string"),
        ("ruby", "/tmp/x/program.rb:1:in 'Kernel#require': cannot load such file -- x (LoadError)",
                "'x' tidak ditemukan oleh require"),
        ("ruby", "/tmp/x/program.rb:1:in '<main>': uninitialized constant Foo (NameError)",
                "'foo' diawali huruf besar"),
        ("ruby", "/tmp/x/program.rb:2:in '<main>': can't modify frozen String: \"abc\" (FrozenError)",
                "objek string ini sudah dibekukan"),
        ("ruby", "/tmp/x/program.rb: /tmp/x/program.rb:2: syntax errors found (SyntaxError)\n"
           "> 1 | def f\n"
           "    | ^~~ expected an `end` to close the `def` statement",
                "belum ditutup dengan end"),
        ("ruby", "/tmp/x/program.rb:1:in 'Integer#+': String can't be coerced into Integer (TypeError)",
                "string tidak bisa dihitung bersama integer"),
        ("ruby", "/tmp/x/program.rb:1:in 'Integer#+': nil can't be coerced into Integer (TypeError)",
                "nilai nil (kosong) yang ikut dihitung dengan integer"),
        ("ruby", "/tmp/x/program.rb:1:in 'IO.read': No such file or directory @ rb_sysopen - x.txt (Errno::ENOENT)",
                "berkas atau folder 'x.txt' tidak ada"),
        ("rust", "error[E0425]: cannot find value `x` in this scope",
                "nama 'x' tidak dikenal di sini"),
        ("rust", "error[E0308]: mismatched types\n"
           " --> /tmp/x/main.rs:2:18\n"
           "  |\n"
           "2 |     let x: i32 = \"a\";\n"
           "  |            ---   ^^^ expected `i32`, found `&str`",
                "menuntut `i32` tetapi menemukan `&str`"),
        ("rust", "error[E0382]: borrow of moved value: `s`",
                "'s' sudah dipindahkan"),
        ("rust", "error[E0384]: cannot assign twice to immutable variable `x`",
                "let mut x"),
        ("rust", "error[E0596]: cannot borrow `v` as mutable, as it is not declared as mutable",
                "variabel 'v' tidak dideklarasikan mut"),
        ("rust", "error[E0599]: no method named `foo` found for type `{integer}` in the current scope",
                "method bernama 'foo'"),
        ("rust", "error[E0433]: cannot find type `HashMap` in this scope",
                "tipe 'hashmap' belum dikenal"),
        ("rust", "error: expected `;`, found `println`",
                "tepat sebelum 'println'"),
        ("rust", "thread 'main' (294049) panicked at /tmp/x/main.rs:4:21:\n"
           "index out of bounds: the len is 3 but the index is 5",
                "indeks 5 padahal isinya cuma 3 elemen"),
        ("rust", "thread 'main' (294048) panicked at /tmp/x/main.rs:3:20:\n"
           "attempt to divide by zero",
                "pembagian dengan nol"),
        ("rust", "thread 'main' (294047) panicked at /tmp/x/main.rs:3:30:\n"
           "called `Option::unwrap()` on a `None` value",
                "option yang isinya none"),
        ("rust", "thread 'main' (294050) panicked at /tmp/x/main.rs:2:32:\n"
           "called `Result::unwrap()` on an `Err` value: ParseIntError { kind: InvalidDigit }",
                "parseinterror"),
        ("rust", "error[E0106]: missing lifetime specifier",
                "lifetime"),
        ("rust", "error[E0499]: cannot borrow `s` as mutable more than once at a time",
                "'s' dipinjam sebagai &mut dua kali"),
        ("csharp", "/tmp/x/Program.cs(1,19): error CS0103: The name 'y' does not exist in the current context [/tmp/x/latihan.csproj]",
                  "nama 'y' tidak dikenal"),
        ("csharp", "/tmp/x/Program.cs(1,9): error CS0029: Cannot implicitly convert type 'string' to 'int' [/tmp/x/latihan.csproj]",
                  "string dimasukkan ke tempat yang menuntut int"),
        ("csharp", "/tmp/x/Program.cs(2,9): error CS0266: Cannot implicitly convert type 'double' to 'int'. An explicit conversion exists (are you missing a cast?) [/tmp/x/latihan.csproj]",
                  "cast (int)nilai"),
        ("csharp", "/tmp/x/Program.cs(1,1): error CS0246: The type or namespace name 'Foo' could not be found (are you missing a using directive or an assembly reference?) [/tmp/x/latihan.csproj]",
                  "'foo' tidak dikenal"),
        ("csharp", "/tmp/x/Program.cs(2,21): error CS1061: 'string' does not contain a definition for 'Foo' and no accessible extension method 'Foo' accepting a first argument of type 'string' could be found (are you missing a using directive or an assembly reference?) [/tmp/x/latihan.csproj]",
                  "tipe string tidak punya method atau properti 'foo'"),
        ("csharp", "/tmp/x/Program.cs(2,19): error CS0165: Use of unassigned local variable 'x' [/tmp/x/latihan.csproj]",
                  "variabel 'x' dipakai sebelum diberi nilai"),
        ("csharp", "/tmp/x/Program.cs(2,19): error CS7036: There is no argument given that corresponds to the required parameter 'b' of 'F(int, int)' [/tmp/x/latihan.csproj]",
                  "parameter 'b'"),
        ("csharp", "/tmp/x/Program.cs(1,12): error CS0161: 'F(int)': not all code paths return a value [/tmp/x/latihan.csproj]",
                  "berakhir tanpa return"),
        ("csharp", "Unhandled exception. System.NullReferenceException: Object reference not set to an instance of an object.",
                  "isinya null"),
        ("csharp", "Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.",
                  "length - 1"),
        ("csharp", "Unhandled exception. System.DivideByZeroException: Attempted to divide by zero.",
                  "pembagian bilangan bulat dengan nol"),
        ("csharp", "Unhandled exception. System.FormatException: The input string 'abc' was not in a correct format.",
                  "teks 'abc' tidak bisa diubah jadi angka"),
        ("csharp", "Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'x' was not present in the dictionary.",
                  "kunci 'x' tidak ada di dictionary"),
        ("csharp", "/tmp/x/Program.cs(3,31): error CS1002: ; expected [/tmp/x/latihan.csproj]",
                  "titik koma"),
        ("vb", "/tmp/x/Program.vb(3,27): error BC30451: 'y' is not declared. It may be inaccessible due to its protection level. [/tmp/x/latihan.vbproj]",
              "nama 'y' tidak dikenal"),
        ("vb", "/tmp/x/Program.vb(3,28): error BC30512: Option Strict On disallows implicit conversions from 'String' to 'Integer'. [/tmp/x/latihan.vbproj]",
              "option strict on melarang"),
        ("vb", "/tmp/x/Program.vb(3,30): error BC30198: ')' expected. [/tmp/x/latihan.vbproj]",
              "mengharapkan ')'"),
        ("vb", "/tmp/x/Program.vb(3,9): error BC30081: 'If' must end with a matching 'End If'. [/tmp/x/latihan.vbproj]",
              "tambahkan end if"),
        ("vb", "/tmp/x/Program.vb(4,27): error BC30456: 'Foo' is not a member of 'String'. [/tmp/x/latihan.vbproj]",
              "tipe string tidak punya anggota bernama 'foo'"),
        ("vb", "/tmp/x/Program.vb(6,27): error BC30455: Argument not specified for parameter 'b' of 'Public Function F(a As Integer, b As Integer) As Integer'. [/tmp/x/latihan.vbproj]",
              "parameter 'b'"),
        ("vb", "/tmp/x/Program.vb(4,13): error BC30288: Local variable 'x' is already declared in the current block. [/tmp/x/latihan.vbproj]",
              "dideklarasikan dua kali"),
        ("vb", "Unhandled exception. System.NullReferenceException: Object reference not set to an instance of an object.",
              "isinya null"),
        ("vb", "Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.",
              "indeks array di luar jangkauan"),
        ("vb", "Unhandled exception. System.FormatException: The input string 'abc' was not in a correct format.",
              "tidak bisa diubah jadi angka"),
        ("vb", "Unhandled exception. System.InvalidCastException: Conversion from string \"abc\" to type 'Integer' is not valid.\n"
         " ---> System.FormatException: The input string 'abc' was not in a correct format.",
              "teks \"abc\" tidak bisa diubah jadi integer"),
        ("vb", "/tmp/x/Program.vb(3,27): error BC30800: Method arguments must be enclosed in parentheses. [/tmp/x/latihan.vbproj]",
              "harus memakai kurung"),
        ("php", "Parse error: syntax error, unexpected token \"echo\", expecting \",\" or \";\" in /tmp/x/program.php on line 3",
               "titik koma"),
        ("php", "Parse error: Unclosed '{' on line 2 in /tmp/x/program.php on line 4",
               "tanda '{' yang dibuka di baris 2"),
        ("php", "Warning: Undefined variable $x in /tmp/x/program.php on line 2",
               "variabel $x dipakai sebelum diberi nilai"),
        ("php", "Fatal error: Uncaught Error: Call to undefined function foo() in /tmp/x/program.php:2",
               "fungsi 'foo' tidak dikenal"),
        ("php", "Fatal error: Uncaught Error: Class \"Foo\" not found in /tmp/x/program.php:2",
               "kelas \"foo\" tidak ditemukan"),
        ("php", "Fatal error: Uncaught DivisionByZeroError: Division by zero in /tmp/x/program.php:2",
               "pembagian atau sisa bagi dengan nol"),
        ("php", "Warning: Undefined array key \"y\" in /tmp/x/program.php on line 3",
               "kunci \"y\""),
        ("php", "Fatal error: Uncaught TypeError: f(): Argument #1 ($n) must be of type int, string given, called in /tmp/x/program.php on line 3 and defined in /tmp/x/program.php:2",
               "argumen $n bertipe int"),
        ("php", "Fatal error: Uncaught ArgumentCountError: Too few arguments to function f(), 1 passed in /tmp/x/program.php on line 3 and exactly 2 expected in /tmp/x/program.php:2",
               "dipanggil dengan 1 argumen, padahal parameternya meminta 2"),
        ("php", "Warning: Attempt to read property \"nama\" on null in /tmp/x/program.php on line 3",
               "properti 'nama'"),
        ("php", "Fatal error: Uncaught Error: Call to a member function foo() on null in /tmp/x/program.php:3",
               "method foo() dipanggil dari nilai null"),
        ("php", "Warning: require(x.php): Failed to open stream: No such file or directory in /tmp/x/program.php on line 2",
               "berkas yang dibuka tidak ada"),
        ("php", "Parse error: syntax error, unexpected variable \"$y\" in /tmp/x/program.php on line 3",
               "tidak mengira ada \"$y\""),
        ("kotlin", "main.kt:2:13: error: unresolved reference 'x'.",
                  "nama 'x' tidak dikenal"),
        ("kotlin", "main.kt:2:16: error: initializer type mismatch: expected 'Int', actual 'String'.",
                  "string dimasukkan ke tempat yang menuntut int"),
        ("kotlin", "main.kt:3:5: error: 'val' cannot be reassigned.",
                  "dibuat dengan val"),
        ("kotlin", "main.kt:3:14: error: only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'String?'.",
                  "bisa null"),
        ("kotlin", "main.kt:3:13: error: no value passed for parameter 'b'.",
                  "parameter 'b' wajib diisi"),
        ("kotlin", "main.kt:3:15: error: unresolved reference 'foo' on receiver of type 'String'.",
                  "tipe string tidak punya method atau properti 'foo'"),
        ("kotlin", "main.kt:2:16: error: syntax error: Expecting ')'.",
                  "mengharapkan ')'"),
        ("kotlin", "Exception in thread \"main\" kotlin.UninitializedPropertyAccessException: lateinit property n has not been initialized",
                  "lateinit 'n'"),
        ("kotlin", "Exception in thread \"main\" java.lang.NullPointerException\n"
             "\tat MainKt.main(main.kt:3)",
                  "!!"),
        ("kotlin", "Exception in thread \"main\" java.lang.IndexOutOfBoundsException: Index 5 out of bounds for length 3\n"
             "\tat java.base/jdk.internal.util.Preconditions.outOfBounds(Preconditions.java:64)\n"
             "\tat java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Preconditions.java:70)\n"
             "\tat java.base/jdk.internal.util.Preconditions.checkIndex(Preconditions.java:266)\n"
             "\tat java.base/java.util.Objects.checkIndex(Objects.java:361)\n"
             "\tat java.base/java.util.ArrayList.get(ArrayList.java:427)\n"
             "\tat MainKt.main(main.kt:3)",
                  "indeks 5 padahal isinya cuma 3 elemen"),
        ("kotlin", "Exception in thread \"main\" java.util.NoSuchElementException: List is empty.\n"
             "\tat kotlin.collections.CollectionsKt___CollectionsKt.first(_Collections.kt:222)\n"
             "\tat MainKt.main(main.kt:3)",
                  "firstornull"),
        ("kotlin", "Exception in thread \"main\" java.lang.IllegalArgumentException: x harus positif\n"
             "\tat MainKt.main(main.kt:3)",
                  "illegalargumentexception"),
        ("typescript", "program.ts(1,5): error TS2322: Type 'string' is not assignable to type 'number'.",
                      "string dimasukkan ke tempat yang menuntut number"),
        ("typescript", "program.ts(1,13): error TS2304: Cannot find name 'y'.",
                      "nama 'y' tidak dikenal"),
        ("typescript", "program.ts(2,15): error TS2339: Property 'foo' does not exist on type '\"abc\"'.",
                      "tidak punya properti atau method 'foo'"),
        ("typescript", "program.ts(2,15): error TS2345: Argument of type 'string' is not assignable to parameter of type 'number'.",
                      "argumen bertipe string, padahal parameternya menuntut number"),
        ("typescript", "program.ts(2,13): error TS2554: Expected 2 arguments, but got 1.",
                      "1 argumen, padahal parameternya 2"),
        ("typescript", "program.ts(1,39): error TS18047: 's' is possibly 'null'.",
                      "'s' bisa berisi null"),
        ("typescript", "program.ts(1,11): error TS1005: ',' expected.",
                      "mengharapkan ','"),
        ("typescript", "program.ts(2,15): error TS2551: Property 'lenght' does not exist on type '\"abc\"'. Did you mean 'length'?",
                      "mungkin maksudmu 'length'"),
        ("typescript", "program.ts(1,19): error TS2307: Cannot find module './nope' or its corresponding type declarations.",
                      "modul './nope'"),
        ("typescript", "program.ts(2,1): error TS2588: Cannot assign to 'a' because it is a constant.",
                      "dibuat dengan const"),
        ("typescript", "program.ts(1,23): error TS1005: ';' expected.",
                      "mengharapkan ';'"),
        ("typescript", "program.ts(1,15): error TS2355: A function whose declared type is neither 'undefined', 'void', nor 'any' must return a value.",
                      "tidak mengembalikan nilai"),
    ]

    def test_pesan_nyata_diterjemahkan(self):
        for bahasa, pesan, frasa in self.KASUS:
            with self.subTest(bahasa=bahasa, pesan=pesan[:60]):
                hasil = galat.terjemahkan(pesan)
                self.assertTrue(hasil, "tidak ada terjemahan sama sekali")
                self.assertIn(frasa, " ".join(hasil).lower())

    def test_penjelasan_bersih_dan_satu_baris(self):
        # Sisa sintaks regex atau rujukan grup yang tidak terganti adalah
        # kerusakan yang diam: kalimatnya tetap tampil, cuma ada "\1" atau
        # "(?:" di tengahnya.
        sisa = re.compile(r"\\\d|\$\d|\(\?|\[\^")
        for bahasa, pesan, _ in self.KASUS:
            for teks in galat.terjemahkan(pesan):
                with self.subTest(bahasa=bahasa, pesan=pesan[:60]):
                    self.assertNotIn("\n", teks)
                    self.assertIsNone(sisa.search(teks), teks)

    def test_pola_bahasa_baru_berjangkar_pada_bahasanya(self):
        # Setiap pola yang cuma boleh mengenai satu bahasa tidak boleh
        # menjelaskan pesan bahasa lain: pesan Python, Java, dan JavaScript
        # yang mirip kata-katanya tetap jatuh ke pola mereka sendiri.
        for pesan in ("NameError: name 'x' is not defined",
                      "TypeError: 'int' object is not subscriptable",
                      "Main.java:5: error: cannot find symbol\n  symbol: variable x",
                      "ReferenceError: x is not defined",
                      "Uncaught TypeError: Cannot read properties of undefined"):
            with self.subTest(pesan=pesan[:40]):
                for teks in galat.terjemahkan(pesan):
                    for kata in ("Ruby", "Rust", "Kotlin", "TypeScript", "PHP",
                                 "VB", "C#"):
                        self.assertNotIn(kata, teks)


class TestBahasaLainTidakBerubah(unittest.TestCase):
    def test_tiga_pesan_contoh_persis_sama(self):
        self.assertEqual(
            galat.terjemahkan("NameError: name 'x' is not defined"),
            ["Nama 'x' dipakai sebelum dibuat. Periksa ejaan dan huruf "
             "besar/kecil, atau apakah variabelnya memang sudah diisi "
             "sebelumnya."])
        self.assertEqual(
            galat.terjemahkan("Main.java:5: error: cannot find symbol\n"
                              "  symbol:   variable jumlah\n"
                              "  location: class Main"),
            ["Variabel 'jumlah' dipakai tapi belum pernah dideklarasikan. "
             "Periksa ejaan dan huruf besar/kecilnya -- Java membedakan Nama "
             "dan nama.",
             "Ada nama (variabel, method, atau kelas) yang dipakai tapi belum "
             "dideklarasikan, atau ejaannya berbeda."])
        self.assertEqual(
            galat.terjemahkan("ReferenceError: x is not defined"),
            ["Nama 'x' dipakai sebelum dibuat. Periksa ejaan dan huruf "
             "besar/kecilnya."])

    def test_titik_koma_java_dan_typescript_dipisah(self):
        # Pola Java dipersempit jadi "error: ';' expected" supaya pesan tsc
        # tidak dijelaskan dengan "Di Java ...". Keduanya harus tetap benar.
        java = galat.terjemahkan("Main.java:4: error: ';' expected")
        self.assertEqual(len(java), 1)
        self.assertIn("Di Java", java[0])
        ts = galat.terjemahkan("program.ts(1,23): error TS1005: ';' expected.")
        self.assertEqual(len(ts), 1)
        self.assertNotIn("Java", ts[0])
        self.assertIn("';'", ts[0])

    def test_exception_jvm_java_dan_kotlin_dipisah(self):
        # Pesan exception JVM sama persis di Java dan Kotlin; yang membedakan
        # cuma MainKt di jejak tumpukan. Java tidak boleh kehilangan
        # penjelasannya, dan Kotlin tidak boleh dijelaskan dengan 'new'.
        java_npe = ("Exception in thread \"main\" java.lang.NullPointerException\n"
                    "\tat Main.main(Main.java:5)")
        kotlin_npe = ("Exception in thread \"main\" java.lang.NullPointerException\n"
                      "\tat MainKt.main(main.kt:3)\n\tat MainKt.main(main.kt)")
        self.assertIn("'new'", " ".join(galat.terjemahkan(java_npe)))
        kt = galat.terjemahkan(kotlin_npe)
        self.assertEqual(len(kt), 1)
        self.assertIn("!!", kt[0])
        self.assertNotIn("'new'", kt[0])

        java_nse = ("Exception in thread \"main\" java.util.NoSuchElementException\n"
                    "\tat java.base/java.util.Scanner.throwFor(Scanner.java:937)\n"
                    "\tat Main.main(Main.java:6)")
        kotlin_nse = ("Exception in thread \"main\" java.util.NoSuchElementException: "
                      "List is empty.\n\tat MainKt.main(main.kt:3)")
        self.assertIn("Scanner", " ".join(galat.terjemahkan(java_nse)))
        kt = galat.terjemahkan(kotlin_nse)
        self.assertEqual(len(kt), 1)
        self.assertNotIn("Scanner", kt[0])
        self.assertIn("firstOrNull", kt[0])

    def test_rekaman_golden_bahasa_lama_tidak_bergeser(self):
        # Rekaman `packages/bersama/golden/galat.json` dibuat dari Python.
        # Pesan bahasa yang sudah ada sebelum tujuh bahasa ini ditambahkan
        # wajib masih menghasilkan sidik yang sama.
        jalur = os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), "packages", "bersama", "golden",
            "galat.json")
        with open(jalur, encoding="utf-8") as f:
            rekaman = json.load(f)
        lama = {"python", "java", "c", "javascript", "go", "bash", "sql",
                "html", "css"}
        diperiksa = 0
        for k in rekaman["kasus"]:
            if k["bahasa"] not in lama:
                continue
            diperiksa += 1
            teks = json.dumps(galat.terjemahkan(k["masukan"]),
                              ensure_ascii=False, sort_keys=True,
                              separators=(",", ":"))
            sidik = hashlib.sha256(teks.encode("utf-8")).hexdigest()
            with self.subTest(bahasa=k["bahasa"], pesan=k["masukan"][:50]):
                self.assertEqual(sidik, k["terjemahan_sha256"])
        self.assertGreater(diperiksa, 60)


LEWATI_LAMBAT = os.environ.get("BELAJAR_SKIP_LAMBAT") == "1"

# Program pendek yang memicu kesalahan khas pemula, satu per kejadian.
PROGRAM_PEMICU = {
    "ruby": [
        ("r01_nameerror",
         "puts x\n"),
        ("r02_nil_upcase",
         "x = nil\n"
         "puts x.upcase\n"),
        ("r04_integer_abc",
         "puts Integer(\"abc\")\n"),
        ("r05_arity",
         "def f(a, b)\n"
         "  a + b\n"
         "end\n"
         "puts f(1)\n"),
        ("r11_syntax_def",
         "def f\n"
         "  puts 1\n"),
        ("r16_int_plus_str",
         "puts 1 + \"2\"\n"),
    ],
    "rust": [
        ("u01_notfound",
         "fn main() {\n"
         "    println!(\"{}\", x);\n"
         "}\n"),
        ("u02_mismatch",
         "fn main() {\n"
         "    let x: i32 = \"a\";\n"
         "    println!(\"{}\", x);\n"
         "}\n"),
        ("u03_moved",
         "fn main() {\n"
         "    let s = String::from(\"a\");\n"
         "    let t = s;\n"
         "    println!(\"{} {}\", s, t);\n"
         "}\n"),
        ("u05_borrow_mut",
         "fn main() {\n"
         "    let v = vec![1];\n"
         "    v.push(2);\n"
         "    println!(\"{:?}\", v);\n"
         "}\n"),
        ("u10_index_oob",
         "fn main() {\n"
         "    let v = vec![1, 2, 3];\n"
         "    let i = v.len() + 2;\n"
         "    println!(\"{}\", v[i]);\n"
         "}\n"),
        ("u13_unwrap_err",
         "fn main() {\n"
         "    let n: i32 = \"abc\".parse().unwrap();\n"
         "    println!(\"{}\", n);\n"
         "}\n"),
    ],
    "csharp": [
        ("c01_name",
         "Console.WriteLine(y);\n"),
        ("c03_convert",
         "int x = \"a\";\n"
         "Console.WriteLine(x);\n"),
        ("c07_missing_arg",
         "static int F(int a, int b) => a + b;\n"
         "Console.WriteLine(F(1));\n"),
        ("c13_index",
         "var a = new int[3];\n"
         "Console.WriteLine(a[5]);\n"),
        ("c15_format",
         "int n = int.Parse(\"abc\");\n"
         "Console.WriteLine(n);\n"),
    ],
    "vb": [
        ("v01_not_declared",
         "Module Program\n"
         "    Sub Main()\n"
         "        Console.WriteLine(y)\n"
         "    End Sub\n"
         "End Module\n"),
        ("v02_str_to_int",
         "Module Program\n"
         "    Sub Main()\n"
         "        Dim n As Integer = \"abc\"\n"
         "        Console.WriteLine(n)\n"
         "    End Sub\n"
         "End Module\n"),
        ("v05_paren",
         "Module Program\n"
         "    Sub Main()\n"
         "        Console.WriteLine(\"a\"\n"
         "    End Sub\n"
         "End Module\n"),
        ("v14_index",
         "Module Program\n"
         "    Sub Main()\n"
         "        Dim a(2) As Integer\n"
         "        Console.WriteLine(a(5))\n"
         "    End Sub\n"
         "End Module\n"),
        ("v16_format",
         "Module Program\n"
         "    Sub Main()\n"
         "        Dim n As Integer = Integer.Parse(\"abc\")\n"
         "        Console.WriteLine(n)\n"
         "    End Sub\n"
         "End Module\n"),
    ],
    "php": [
        ("p01_parse_semicolon",
         "<?php\n"
         "echo \"a\"\n"
         "echo \"b\";\n"),
        ("p03_undefined_var",
         "<?php\n"
         "echo $x;\n"),
        ("p04_undefined_func",
         "<?php\n"
         "foo();\n"),
        ("p10_type_arg",
         "<?php\n"
         "function f(int $n) { return $n; }\n"
         "echo f(\"abc\");\n"),
        ("p13_member_null",
         "<?php\n"
         "$o = null;\n"
         "$o->foo();\n"),
        ("p23_unexpected_var",
         "<?php\n"
         "$x = 1\n"
         "$y = 2;\n"),
    ],
    "kotlin": [
        ("k01_unresolved",
         "fun main() {\n"
         "    println(x)\n"
         "}\n"),
        ("k02_mismatch",
         "fun main() {\n"
         "    val n: Int = \"a\"\n"
         "    println(n)\n"
         "}\n"),
        ("k04_nullable_call",
         "fun main() {\n"
         "    val s: String? = null\n"
         "    println(s.length)\n"
         "}\n"),
        ("k22_npe",
         "fun main() {\n"
         "    val s: String? = null\n"
         "    println(s!!.length)\n"
         "}\n"),
        ("k23_index_list",
         "fun main() {\n"
         "    val a = mutableListOf(1, 2, 3)\n"
         "    println(a[5])\n"
         "}\n"),
    ],
    "typescript": [
        ("t01_not_assignable",
         "let x: number = \"a\";\n"
         "console.log(x);\n"),
        ("t02_cannot_find",
         "console.log(y);\n"),
        ("t05_arg_count",
         "function f(a: number, b: number) { return a + b; }\n"
         "console.log(f(1));\n"),
        ("t07_possibly_null",
         "function f(s: string | null) { return s.length; }\n"
         "console.log(f('a'));\n"),
        ("t41_for_semicolon",
         "for (let i = 0; i < 3 i++) {\n"
         "  console.log(i);\n"
         "}\n"),
    ],
}


def _teks_toolchain(hasil):
    """Teks yang dikeluarkan toolchain untuk sebuah kegagalan.

    stderr dulu. Untuk runner yang menulis diagnosanya ke STDOUT (kompilasi
    .NET dan tsc, serta semua pesan PHP) `hasil.galat` kosong atau cuma
    "Kompilasi gagal.", jadi teks compilernya diambil dari `keluaran`.
    """
    teks = hasil.galat or ""
    if not teks.strip() or teks.strip() == "Kompilasi gagal.":
        teks = hasil.keluaran or ""
    return teks


class TestToolchainNyata(unittest.TestCase):
    """Pola harus setia pada kata-kata compiler versi yang terpasang.

    Pesan di `TestBahasaBaruPesanNyata` adalah foto; tes ini yang memotret
    ulang. Kalau sebuah versi Ruby, rustc, .NET, PHP, kotlinc, atau tsc
    mengubah kalimat pesannya, tes inilah yang merah, bukan pelajar yang
    mendadak melihat pesan mentah lagi.

    Yang diuji hanya `galat.terjemahkan`: apakah teks itu SAMPAI ke
    penerjemah (hanya `hasil.galat` yang dikirim aplikasi) urusan runner.
    """

    @unittest.skipIf(LEWATI_LAMBAT, "menjalankan toolchain; BELAJAR_SKIP_LAMBAT=1")
    def test_setiap_pesan_toolchain_punya_penjelasan(self):
        tugas = []
        for bahasa, daftar in PROGRAM_PEMICU.items():
            if not runner.tersedia(bahasa):
                with self.subTest(bahasa=bahasa):
                    self.skipTest(
                        f"{bahasa} tidak terpasang ({', '.join(runner.program_hilang(bahasa))}); "
                        "untuk Kotlin tambahkan ~/.sdkman/candidates/kotlin/current/bin ke PATH")
                continue
            tugas += [(bahasa, nama, kode) for nama, kode in daftar]
        if not tugas:
            self.skipTest("tidak satu pun toolchain terpasang")

        def jalan(t):
            bahasa, _nama, kode = t
            return runner.jalankan(bahasa, kode)

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            hasil_semua = list(pool.map(jalan, tugas))

        for (bahasa, nama, _kode), hasil in zip(tugas, hasil_semua):
            with self.subTest(bahasa=bahasa, program=nama):
                self.assertFalse(
                    hasil.sukses and not (hasil.galat or hasil.keluaran).strip(),
                    "program pemicu tidak menghasilkan kesalahan sama sekali")
                teks = galat.rapikan(_teks_toolchain(hasil), "program")
                self.assertTrue(teks.strip(), "toolchain tidak mengeluarkan pesan")
                self.assertTrue(
                    galat.terjemahkan(teks),
                    "pesan toolchain tanpa penjelasan:\n" + teks[:400])


if __name__ == "__main__":
    unittest.main(verbosity=2)
