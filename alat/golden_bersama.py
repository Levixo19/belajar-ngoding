"""Rekam keluaran `sorot`, `galat`, dan `beda` atas SELURUH kode kurikulum.

Kenapa ada. Ketiga algoritma ini hari ini hidup DUA KALI: versi Python di
`inti/` dipakai server, versi JavaScript di `webapp/statik/js/` dipakai editor.
Yang menjaga keduanya tidak menyimpang adalah tes diferensial di
`tests/test_web.py` -- ia menjalankan keduanya atas korpus yang sama lalu
mengadu hasilnya.

Begitu keduanya digabung jadi satu implementasi TypeScript, tes diferensial itu
kehilangan lawan tandingnya dan ikut mati. Yang hilang bukan sekadar sebuah
tes: tidak ada lagi yang memberi tahu kalau penyorotan berubah. Perubahan
semacam itu tidak menimbulkan error di mana pun -- warna sebuah kata kunci
bergeser, dan tidak ada yang menyadarinya sampai berbulan-bulan kemudian.

Golden hash menggantikan perannya. Ia tidak membandingkan dua implementasi,
melainkan membandingkan keluaran HARI INI dengan keluaran yang sudah
disepakati. Rekamannya dibuat SEBELUM versi TypeScript ada, dan versi
TypeScript itu nanti wajib mereproduksi angka yang sama.

Yang direkam sidiknya, bukan keluarannya: korpusnya 1.300-an blok kode, dan
menyimpan tokennya utuh berarti berkas puluhan MB yang tidak pernah dibaca
siapa pun.

    python3 alat/golden_bersama.py            # hitung dan bandingkan
    python3 alat/golden_bersama.py --tulis    # tulis packages/bersama/golden/
"""

import argparse
import collections
import hashlib
import json
import os
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from inti import beda, galat, sorot  # noqa: E402
from inti.kurikulum import LANGUAGES  # noqa: E402
from webapp import isi  # noqa: E402

TUJUAN = os.path.join(AKAR, "packages", "bersama", "golden")


def _sha(nilai):
    """SHA-256 atas bentuk JSON yang bisa DIREPRODUKSI di luar Python.

    `separators=(",", ":")` bukan penghematan tempat. Bawaan `json.dumps`
    memakai `", "` dan `": "` dengan spasi, sedangkan `JSON.stringify` di
    JavaScript tidak pernah memakai spasi -- jadi sidik yang sama-sama benar
    akan selalu berbeda di kedua sisi. Gejalanya bukan "ada yang salah di
    algoritmanya" melainkan tiga ribu sidik yang tidak satu pun cocok, yang
    terbaca seperti port yang gagal total dan menghabiskan sehari untuk
    ditelusuri.

    `sort_keys` tetap dipasang untuk kasus `golden_beda`, yang menyidik sebuah
    dict. `JSON.stringify` TIDAK mengurutkan kunci, jadi sisi TS yang nanti
    mereproduksi sidik itu wajib mengurutkannya sendiri; untuk `sorot` dan
    `galat` yang disidik cuma daftar dan string, jadi di sana `JSON.stringify`
    polos sudah cukup.
    """
    teks = json.dumps(nilai, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()


def korpus():
    """Setiap blok kode di kurikulum, beserta bahasa penyorotnya.

    Bahasanya WAJIB datang dari `isi.bahasa_blok` dan `isi.bahasa_sorot`, bukan
    dari `lang["runner"]` mentah. Versi pertama alat ini memakai yang mentah,
    dan akibatnya 408 dari 3.315 kasus direkam untuk bahasa yang aplikasinya
    tidak pernah pakai: `"terminal"` disorot sebagai bash, `"jsx"` sebagai
    javascript, `"postgresql"` sebagai sql (seluruh tabelnya di
    `berkas.sorot_untuk`). Tiga ratus empat puluh empat di antaranya
    menghasilkan token yang BERBEDA, jadi sidiknya membekukan jalur mati --
    pagar yang tidak pernah bisa memerah untuk perubahan yang nyata, dan
    memerah untuk perubahan yang tidak pernah terlihat pelajar.
    """
    keluar = []
    for lang in LANGUAGES:
        for m in lang["materials"]:
            for i, s in enumerate(m["sections"]):
                if s.get("code"):
                    _runner, bhs = isi.bahasa_blok(s, lang)
                    keluar.append((f"{lang['key']}/materi/{m['title']}/{i}",
                                   bhs, s["code"]))
        bhs_latihan = isi.bahasa_sorot(lang)
        for x in lang["exercises"]:
            if x.get("solution"):
                keluar.append((f"{lang['key']}/latihan/{x['title']}",
                               bhs_latihan, x["solution"]))
    return keluar


def golden_sorot(blok):
    """Sidik token per blok. Gabungan teks token WAJIB sama dengan sumbernya."""
    kasus, cacat = [], []
    for nama, bhs, kode in blok:
        token = [[j, t] for j, t in sorot.token(kode, bhs)]
        if "".join(t for _, t in token) != kode:
            cacat.append(nama)
        kasus.append({"nama": nama, "bahasa": bhs, "sha256": _sha(token)})
    return kasus, cacat


# Pesan compiler yang diterjemahkan `galat.terjemahkan`. Sengaja ditulis
# tangan: yang diuji adalah penerjemahnya, dan korpus pesan error sungguhan
# tidak ada di repo. Tiap entri berbentuk seperti yang keluar di mesin ini.
PESAN = [
    ("python", 'File "/tmp/x/program.py", line 3\n    print("a"\n         ^\nSyntaxError: \'(\' was never closed'),
    ("python", 'Traceback (most recent call last):\n  File "/tmp/x/program.py", line 2, in <module>\n    print(x)\nNameError: name \'x\' is not defined'),
    ("python", 'Traceback (most recent call last):\n  File "/tmp/x/program.py", line 1, in <module>\n    1/0\nZeroDivisionError: division by zero'),
    ("java", "/tmp/x/Main.java:4: error: ';' expected\n        int a = 1\n                 ^\n1 error"),
    ("java", "Exception in thread \"main\" java.lang.NullPointerException\n\tat Main.main(Main.java:5)"),
    ("c", "/tmp/x/program.c:3:5: error: 'y' undeclared (first use in this function)\n    3 |     y = 1;\n      |     ^"),
    ("javascript", "/tmp/x/program.js:2\nconsole.log(x)\n            ^\n\nReferenceError: x is not defined\n    at Object.<anonymous> (/tmp/x/program.js:2:13)"),
    ("go", "./program.go:5:2: declared and not used: x"),
    ("rust", "error[E0425]: cannot find value `x` in this scope\n --> program.rs:2:20"),
]


# Satu pesan per pola yang TIDAK tersentuh `PESAN` di atas. Diukur, bukan
# dikira: dari 274 pola, sembilan pesan sungguhan cuma menjalani 8. Dua ratus
# enam puluh enam sisanya tidak pernah dieksekusi sama sekali -- dan justru di
# situ beda regex Python-JavaScript bisa bersembunyi, karena satu pola yang
# tidak pernah cocok di sisi TS tidak menimbulkan error: pesan errornya cuma
# kembali tampil mentah kepada orang yang paling tidak bisa membacanya.
#
# Bentuknya ditulis mendekati keluaran aslinya, bukan cuma potongan yang
# kebetulan cocok, supaya pola yang terlalu longgar ikut ketahuan.
PROBE = [
    ("java", "Main.java:4: error: cannot find symbol\n  symbol:   variable jumlah\n  location: class Main"),
    ("java", "Main.java:4: error: cannot find symbol\n  symbol:   method hitung(int)\n  location: class Main"),
    ("java", "error: cannot find symbol"),
    ("java", "Main.java:5: error: incompatible types: String cannot be converted to int"),
    ("java", "Main.java:1: error: class Halo is public, should be declared in a file named Halo.java"),
    ("java", "Main.java:8: error: missing return statement"),
    ("java", "Main.java:9: error: unreachable statement"),
    ("java", "Main.java:12: error: reached end of file while parsing"),
    ("java", 'Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 3'),
    ("java", 'Exception in thread "main" java.lang.NumberFormatException: For input string: "abc"'),
    ("java", 'Exception in thread "main" java.lang.ArithmeticException: / by zero'),
    ("java", 'Exception in thread "main" java.util.NoSuchElementException'),
    ("python", '  File "program.py", line 3\n    print(x)\nIndentationError: unexpected indent'),
    ("python", '  File "program.py", line 4\nTabError: inconsistent use of tabs and spaces in indentation'),
    ("python", '  File "program.py", line 2\nSyntaxError: unmatched \')\''),
    ("python", '  File "program.py", line 1\nSyntaxError: expected \':\''),
    ("python", "SyntaxError: invalid syntax. Perhaps you forgot a comma?"),
    ("python", "SyntaxError: cannot assign to literal here."),
    ("python", '  File "program.py", line 1\nSyntaxError: invalid syntax'),
    ("python", "TypeError: 'int' object is not subscriptable"),
    ("python", "TypeError: 'str' object is not callable"),
    ("python", "TypeError: f() takes 2 positional arguments but 3 were given"),
    ("python", "SyntaxError: unterminated string literal (detected at line 1)"),
    ("python", "TypeError: unsupported operand type(s) for +: 'int' and 'str'"),
    ("python", 'TypeError: can only concatenate str (not "int") to str'),
    ("python", "ValueError: invalid literal for int() with base 10: 'abc'"),
    ("python", "IndexError: list index out of range"),
    ("python", "EOFError: EOF when reading a line"),
    ("python", "AttributeError: 'list' object has no attribute 'push'"),
    ("python", "ModuleNotFoundError: No module named 'requests'"),
    ("python", "KeyError: 'nama'"),
    ("c", "program.c:4:5: error: expected ';' before '}' token"),
    ("c", "/usr/bin/ld: undefined reference to `main'"),
    ("c", "/usr/bin/ld: program.c:5: undefined reference to `hitung'"),
    ("c", "program.c:3:5: warning: implicit declaration of function 'printf'"),
    ("c", "program.c:5:12: warning: format '%d' expects argument of type 'int', but argument 2 has type 'double'"),
    ("c", "program.c:10:1: error: expected '}' at end of input"),
    ("c", "Segmentation fault (core dumped)"),
    ("javascript", "TypeError: daftar.push is not a function"),
    ("javascript", "TypeError: Cannot read properties of undefined (reading 'nama')"),
    ("javascript", "SyntaxError: Unexpected token ')'"),
    ("javascript", "TypeError: Assignment to constant variable."),
    ("go", './program.go:4:2: "fmt" imported and not used'),
    ("go", "./program.go:6:2: x declared and not used"),
    ("go", "./program.go:7:9: undefined: hitung"),
    ("go", "./program.go:3:1: expected declaration"),
    ("go", "./program.go:8:10: invalid operation: a + b (mismatched types int and string)"),
    ("go", "panic: runtime error: index out of range [5] with length 3"),
    ("bash", "program.sh: line 10: unexpected EOF while looking for matching `\"'"),
    ("bash", "program.sh: line 4: syntax error near unexpected token `('"),
    ("bash", "program.sh: line 3: nama: command not found"),
    ("bash", "bash: kompilasi: command not found"),
    ("bash", "program.sh: line 7: [: abc: integer expression expected"),
    ("sql", 'Error: near "AUTO_INCREMENT": syntax error'),
    ("sql", "Error: no such table: siswa"),
    ("sql", "Error: no such column: nilai"),
    ("sql", "Error: UNIQUE constraint failed: siswa.id"),
    ("html", "halaman.html:3: <div> dibuka tapi tidak pernah ditutup"),
    ("html", "halaman.html:7: </span> menutup sesuatu yang tidak pernah dibuka"),
    ("html", "halaman.html:2: </br> tidak diperlukan"),
    ("css", "gaya.css:4: pemilih 'p' tidak diikuti '{'"),
    ("css", "gaya.css:9: blok dibuka dengan '{' tapi tidak pernah ditutup"),
    ("css", "gaya.css:5: 'warna merah' bukan deklarasi yang sah"),
    ("css", "gaya.css:1: blok '{ … }' tanpa pemilih"),
    # Dua di bawah bukan untuk polanya, melainkan untuk `rapikan` dan
    # `ringkas`. Baterai mutasi di `packages/bersama/uji/gigi-golden.py`
    # menemukan keduanya tidak terjaga sama sekali: melepas bendera `g` dari
    # pola jalur dan menggeser deteksi Traceback tidak memerahkan apa pun,
    # karena tidak satu pun pesan di atas menyebut jalur sementara DUA KALI
    # atau memuat kata Traceback di luar tiga baris pertama.
    ("c", "/tmp/belajar-ab12cd/program.c:3:5: error: 'y' undeclared\n"
          "/tmp/belajar-ab12cd/program.c:4:9: note: each undeclared "
          "identifier is reported only once"),
    ("python", "============ test session starts ============\n"
               "collected 1 item\n\n"
               "tes_hitung.py F                        [100%]\n\n"
               "================= FAILURES =================\n"
               "_______________ test_jumlah ________________\n"
               "Traceback (most recent call last):\n"
               '  File "tes_hitung.py", line 4, in test_jumlah\n'
               "    assert jumlah(2, 2) == 5\n"
               "AssertionError: assert 4 == 5\n"
               "========== short test summary info =========\n"
               "FAILED tes_hitung.py::test_jumlah\n"
               "FAILED tes_hitung.py::test_kurang\n"
               "FAILED tes_hitung.py::test_kali\n"
               "============= 3 failed in 0.03s ============"),
    # Ruby, Rust, C#, Visual Basic, PHP, Kotlin, dan TypeScript (2026-10-28).
    # Bukan karangan: tiap entri ditangkap dari toolchain sungguhan lewat
    # `runner.jalankan` (jalur direktori sementara diganti /tmp/x), lalu dipilih
    # satu per satu sampai SEMUA pola baru tersentuh dan dipotong sependek yang
    # masih menyentuh pola yang sama. Pesan kompilasi .NET dipotong sebelum
    # "Build FAILED.", karena bagian itu mengulang pesan yang sama.
    ("ruby", "/tmp/x/program.rb:1:in '<main>': undefined local variable or method 'x' for main (NameError)"),
    ("ruby", "/tmp/x/program.rb:1:in 'Object#f': wrong number of arguments (given 1, expected 2) (ArgumentError)\n"
          "\tfrom /tmp/x/program.rb:4:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:2:in 'Array#fetch': index 5 outside of array bounds: -2...2 (IndexError)\n"
          "\tfrom /tmp/x/program.rb:2:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in 'String#+': no implicit conversion of Integer into String (TypeError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in 'Kernel#require': cannot load such file -- x (LoadError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in '<main>': uninitialized constant Foo (NameError)"),
    ("ruby", "/tmp/x/program.rb:2:in '<main>': can't modify frozen String: \"abc\" (FrozenError)"),
    ("ruby", "/tmp/x/program.rb: /tmp/x/program.rb:2: syntax errors found (SyntaxError)\n"
          "> 1 | def f\n"
          "    | ^~~ expected an `end` to close the `def` statement\n"
          "> 2 |   puts 1"),
    ("ruby", "/tmp/x/program.rb:1:in 'Kernel#Float': invalid value for Float(): \"x\" (ArgumentError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in 'Integer#+': String can't be coerced into Integer (TypeError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:2:in '<main>': undefined method '+' for nil (NoMethodError)"),
    ("ruby", "/tmp/x/program.rb:7:in '<main>': private method 'sekret' called for an instance of A (NoMethodError)"),
    ("ruby", "/tmp/x/program.rb:2:in 'Object#f': stack level too deep (SystemStackError)\n"
          "\tfrom /tmp/x/program.rb:2:in 'Object#f'\n"
          "\tfrom /tmp/x/program.rb:2:in 'Object#f'\n"
          "\tfrom /tmp/x/program.rb:2:in 'Object#f'"),
    ("ruby", "/tmp/x/program.rb: /tmp/x/program.rb:2: syntax error found (SyntaxError)\n"
          "  1 | puts 1\n"
          "> 2 | end\n"
          "    | ^~~ unexpected 'end', ignoring it"),
    ("ruby", "/tmp/x/program.rb:3:in '<main>': undefined method 'bar' for class Foo (NoMethodError)"),
    ("ruby", "/tmp/x/program.rb: /tmp/x/program.rb:1: syntax error found (SyntaxError)\n"
          "> 1 | puts \"abc\n"
          "    |          ^ unterminated string meets end of file"),
    ("ruby", "/tmp/x/program.rb:1:in 'Integer#+': nil can't be coerced into Integer (TypeError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in '<main>': undefined method 'foo' for an instance of Symbol (NoMethodError)"),
    ("ruby", "/tmp/x/program.rb:1:in 'Object#f': missing keyword: :a (ArgumentError)\n"
          "\tfrom /tmp/x/program.rb:4:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in 'Comparable#<': comparison of String with 1 failed (ArgumentError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:1:in 'IO.read': No such file or directory @ rb_sysopen - x.txt (Errno::ENOENT)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("ruby", "/tmp/x/program.rb:2:in 'Object#f': no block given (yield) (LocalJumpError)\n"
          "\tfrom /tmp/x/program.rb:4:in '<main>'"),
    ("ruby", "/tmp/x/program.rb: /tmp/x/program.rb:1: syntax error found (SyntaxError)\n"
          "> 1 | puts(\"a\"\n"
          "    |         ^ unexpected end-of-input; expected a `)` to close the arguments"),
    ("ruby", "/tmp/x/program.rb:1:in 'Kernel#Integer': can't convert nil into Integer (TypeError)\n"
          "\tfrom /tmp/x/program.rb:1:in '<main>'"),
    ("rust", "error[E0382]: borrow of moved value: `s`\n"
          " --> /tmp/x/main.rs:4:23\n"
          "  |\n"
          "2 |     let s = String::from(\"a\");"),
    ("rust", "error[E0384]: cannot assign twice to immutable variable `x`\n"
          " --> /tmp/x/main.rs:3:5\n"
          "  |\n"
          "2 |     let x = 5;"),
    ("rust", "error[E0596]: cannot borrow `v` as mutable, as it is not declared as mutable\n"
          " --> /tmp/x/main.rs:3:5\n"
          "  |\n"
          "3 |     v.push(2);"),
    ("rust", "error[E0599]: no method named `foo` found for type `{integer}` in the current scope\n"
          " --> /tmp/x/main.rs:3:7\n"
          "  |\n"
          "3 |     n.foo();"),
    ("rust", "error[E0433]: cannot find type `HashMap` in this scope\n"
          " --> /tmp/x/main.rs:2:13\n"
          "  |\n"
          "2 |     let m = HashMap::new();"),
    ("rust", "error: expected `;`, found `println`\n"
          " --> /tmp/x/main.rs:2:14\n"
          "  |\n"
          "2 |     let x = 5"),
    ("rust", "error[E0061]: this function takes 2 arguments but 1 argument was supplied\n"
          " --> /tmp/x/main.rs:5:20\n"
          "  |\n"
          "5 |     println!(\"{}\", f(1));"),
    ("rust", "\n"
          "thread 'main' (294049) panicked at /tmp/x/main.rs:4:21:\n"
          "index out of bounds: the len is 3 but the index is 5\n"
          "note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace"),
    ("rust", "\n"
          "thread 'main' (294048) panicked at /tmp/x/main.rs:3:20:\n"
          "attempt to divide by zero\n"
          "note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace"),
    ("rust", "\n"
          "thread 'main' (294047) panicked at /tmp/x/main.rs:3:30:\n"
          "called `Option::unwrap()` on a `None` value\n"
          "note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace"),
    ("rust", "\n"
          "thread 'main' (294050) panicked at /tmp/x/main.rs:2:32:\n"
          "called `Result::unwrap()` on an `Err` value: ParseIntError { kind: InvalidDigit }\n"
          "note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace"),
    ("rust", "error[E0106]: missing lifetime specifier\n"
          " --> /tmp/x/main.rs:1:33\n"
          "  |\n"
          "1 | fn longest(a: &str, b: &str) -> &str {"),
    ("rust", "error[E0277]: cannot add `&str` to `{integer}`\n"
          " --> /tmp/x/main.rs:2:15\n"
          "  |\n"
          "2 |     let x = 5 + \"a\";"),
    ("rust", "error[E0277]: `P` doesn't implement `std::fmt::Display`\n"
          " --> /tmp/x/main.rs:3:20\n"
          "  |\n"
          "3 |     println!(\"{}\", P);"),
    ("rust", "error: this file contains an unclosed delimiter\n"
          " --> /tmp/x/main.rs:2:20\n"
          "  |\n"
          "1 | fn main() {"),
    ("rust", "error[E0499]: cannot borrow `s` as mutable more than once at a time\n"
          " --> /tmp/x/main.rs:4:13\n"
          "  |\n"
          "3 |     let a = &mut s;"),
    ("rust", "error[E0597]: `x` does not live long enough\n"
          " --> /tmp/x/main.rs:5:13\n"
          "  |\n"
          "4 |         let x = 5;"),
    ("rust", "error[E0004]: non-exhaustive patterns: `E::B` not covered\n"
          " --> /tmp/x/main.rs:7:11\n"
          "  |\n"
          "7 |     match e {"),
    ("rust", "error[E0308]: mismatched types\n"
          " --> /tmp/x/main.rs:1:11\n"
          "  |\n"
          "1 | fn f() -> i32 {\n"
          "  |    -      ^^^ expected `i32`, found `()`\n"
          "  |    |\n"
          "  |    implicitly returns `()` as its body has no tail or `return` expression\n"
          "2 |     5;"),
    ("rust", "error[E0601]: `main` function not found in crate `latihan`\n"
          " --> /tmp/x/main.rs:3:2\n"
          "  |\n"
          "3 | }"),
    ("rust", "error: cannot find macro `printn` in this scope\n"
          " --> /tmp/x/main.rs:2:5\n"
          "  |\n"
          "2 |     printn!(\"x\");"),
    ("rust", "error[E0432]: unresolved import `std::collections::Hashmap`\n"
          " --> /tmp/x/main.rs:1:5\n"
          "  |\n"
          "1 | use std::collections::Hashmap;"),
    ("rust", "error[E0425]: cannot find function `foo` in this scope\n"
          " --> /tmp/x/main.rs:2:5\n"
          "  |\n"
          "2 |     foo();"),
    ("rust", "error[E0369]: cannot add `P` to `P`\n"
          " --> /tmp/x/main.rs:5:16\n"
          "  |\n"
          "5 |     let _c = a + b;"),
    ("rust", "error: unexpected closing delimiter: `}`\n"
          " --> /tmp/x/main.rs:3:1\n"
          "  |\n"
          "1 | fn main() {"),
    ("rust", "error[E0609]: no field `b` on type `P`\n"
          " --> /tmp/x/main.rs:6:22\n"
          "  |\n"
          "6 |     println!(\"{}\", p.b);"),
    ("rust", "error[E0063]: missing field `a` in initializer of `P`\n"
          " --> /tmp/x/main.rs:5:14\n"
          "  |\n"
          "5 |     let _p = P { };"),
    ("rust", "error[E0381]: used binding `x` isn't initialized\n"
          " --> /tmp/x/main.rs:3:20\n"
          "  |\n"
          "2 |     let x: i32;"),
    ("rust", "error[E0277]: the type `str` cannot be indexed by `{integer}`\n"
          " --> /tmp/x/main.rs:3:15\n"
          "  |\n"
          "3 |     let c = s[0];"),
    ("rust", "error[E0596]: cannot borrow `*v` as mutable, as it is behind a `&` reference\n"
          " --> /tmp/x/main.rs:2:5\n"
          "  |\n"
          "2 |     v.push(1);"),
    ("rust", "error[E0277]: can't compare `Vec<{integer}>` with `{integer}`\n"
          " --> /tmp/x/main.rs:4:22\n"
          "  |\n"
          "4 |     println!(\"{}\", a == 5);"),
    ("csharp", "/tmp/x/Program.cs(1,19): error CS0103: The name 'y' does not exist in the current context [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,21): error CS1061: 'string' does not contain a definition for 'Foo' and no accessible extension method 'Foo' accepting a first argument of type 'string' could be found (are you missing a using directive or an assembly reference?) [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,19): error CS0165: Use of unassigned local variable 'x' [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,19): error CS7036: There is no argument given that corresponds to the required parameter 'b' of 'F(int, int)' [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,21): error CS1503: Argument 1: cannot convert from 'string' to 'int' [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,12): error CS0161: 'F(int)': not all code paths return a value [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(4,6): error CS1513: } expected [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,5): error CS0128: A local variable or function named 'a' is already defined in this scope [/tmp/x/latihan.csproj]\n"
            "/tmp/x/Program.cs(2,5): warning CS0219: The variable 'a' is assigned but its value is never used [/tmp/x/latihan.csproj]"),
    ("csharp", "Unhandled exception. System.InvalidCastException: Unable to cast object of type 'System.String' to type 'System.Int32'.\n"
            "   at Program.<Main>$(String[] args) in /tmp/x/Program.cs:line 2\n"
            "\n"
            "Program membatalkan dirinya sendiri (abort)."),
    ("csharp", "Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'x' was not present in the dictionary.\n"
            "   at System.Collections.Generic.Dictionary`2.get_Item(TKey key)\n"
            "   at Program.<Main>$(String[] args) in /tmp/x/Program.cs:line 2\n"
            ""),
    ("csharp", "Unhandled exception. System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index')\n"
            "   at System.Collections.Generic.List`1.get_Item(Int32 index)\n"
            "   at Program.<Main>$(String[] args) in /tmp/x/Program.cs:line 2\n"
            ""),
    ("csharp", "/tmp/x/Program.cs(4,32): error CS0120: An object reference is required for the non-static field, method, or property 'P.n' [/tmp/x/latihan.csproj]\n"
            "/tmp/x/Program.cs(3,9): warning CS0414: The field 'P.n' is assigned but its value is never used [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,9): error CS0019: Operator '+' cannot be applied to operands of type 'int' and 'bool' [/tmp/x/latihan.csproj]"),
    ("csharp", "Unhandled exception. System.InvalidOperationException: Sequence contains no elements\n"
            "   at System.Linq.ThrowHelper.ThrowNoElementsException()\n"
            "   at System.Linq.Enumerable.First[TSource](IEnumerable`1 source)\n"
            "   at Program.<Main>$(String[] args) in /tmp/x/Program.cs:line 2"),
    ("csharp", "/tmp/x/Program.cs(2,3): error CS0122: 'A.x' is inaccessible due to its protection level [/tmp/x/latihan.csproj]\n"
            "/tmp/x/Program.cs(3,23): warning CS0169: The field 'A.x' is never used [/tmp/x/latihan.csproj]"),
    ("csharp", "CSC : error CS5001: Program does not contain a static 'Main' method suitable for an entry point [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,1): error CS1022: Type or namespace definition, or end-of-file expected [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(4,23): error CS0191: A readonly field cannot be assigned to (except in a constructor or init-only setter of the type in which the field is defined or a variable initializer) [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,22): error CS1026: ) expected [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,9): error CS0266: Cannot implicitly convert type 'double' to 'int'. An explicit conversion exists (are you missing a cast?) [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,5): error CS1001: Identifier expected [/tmp/x/latihan.csproj]\n"
            "/tmp/x/Program.cs(1,5): error CS1003: Syntax error, ',' expected [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,9): error CS0144: Cannot create an instance of the abstract type or interface 'A' [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,13): error CS0246: The type or namespace name 'Stopwatch' could not be found (are you missing a using directive or an assembly reference?) [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,5): error CS0029: Cannot implicitly convert type 'int' to 'bool' [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,1): error CS0131: The left-hand side of an assignment must be a variable, property or indexer [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(1,19): error CS0127: Since 'F()' returns void, a return keyword must not be followed by an object expression [/tmp/x/latihan.csproj]"),
    ("csharp", "Unhandled exception. System.ArgumentNullException: Value cannot be null. (Parameter 's')\n"
            "   at System.Int32.Parse(String s)\n"
            "   at Program.<Main>$(String[] args) in /tmp/x/Program.cs:line 2\n"
            ""),
    ("csharp", "/tmp/x/Program.cs(3,31): error CS1002: ; expected [/tmp/x/latihan.csproj]"),
    ("csharp", "/tmp/x/Program.cs(2,18): error CS0136: A local or parameter named 'x' cannot be declared in this scope because that name is used in an enclosing local scope to define a local or parameter [/tmp/x/latihan.csproj]"),
    ("vb", "/tmp/x/Program.vb(3,27): error BC30451: 'y' is not declared. It may be inaccessible due to its protection level. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(3,30): error BC30198: ')' expected. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(4,9): error BC30491: Expression does not produce a value. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(4,27): error BC30456: 'Foo' is not a member of 'String'. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(3,18): error BC30002: Type 'Foo' is not defined. [/tmp/x/latihan.vbproj]\n"
        "/tmp/x/Program.vb(4,27): warning BC42104: Variable 'f' is used before it has been assigned a value. A null reference exception could result at runtime. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(6,27): error BC30455: Argument not specified for parameter 'b' of 'Public Function F(a As Integer, b As Integer) As Integer'. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(6,32): error BC30057: Too many arguments to 'Public Function F(a As Integer) As Integer'. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(4,13): error BC30288: Local variable 'x' is already declared in the current block. [/tmp/x/latihan.vbproj]"),
    ("vb", "Unhandled exception. System.NullReferenceException: Object reference not set to an instance of an object.\n"
        "   at Latihan.Program.Main() in /tmp/x/Program.vb:line 4\n"
        "\n"
        "Program membatalkan dirinya sendiri (abort)."),
    ("vb", "Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.\n"
        "   at Latihan.Program.Main() in /tmp/x/Program.vb:line 4\n"
        "\n"
        "Program membatalkan dirinya sendiri (abort)."),
    ("vb", "Unhandled exception. System.DivideByZeroException: Attempted to divide by zero.\n"
        "   at Latihan.Program.Main() in /tmp/x/Program.vb:line 4\n"
        "\n"
        "Program membatalkan dirinya sendiri (abort)."),
    ("vb", "Unhandled exception. System.InvalidCastException: Conversion from string \"abc\" to type 'Integer' is not valid.\n"
        " ---> System.FormatException: The input string 'abc' was not in a correct format.\n"
        "   at Microsoft.VisualBasic.CompilerServices.Conversions.ParseDouble(String Value, NumberFormatInfo NumberFormat)\n"
        "   at Microsoft.VisualBasic.CompilerServices.Conversions.ToInteger(String Value)"),
    ("vb", "/tmp/x/Program.vb(4,9): error BC30092: 'Next' must be preceded by a matching 'For'. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(4,31): error BC30512: Option Strict On disallows implicit conversions from 'String' to 'Double'. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(7,27): error BC30389: 'Latihan.Program.A.x' is not accessible in this context because it is 'Private'. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(3,27): error BC30800: Method arguments must be enclosed in parentheses. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(3,18): error BC30182: Type expected. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(4,9): error BC30074: Constant cannot be the target of an assignment. [/tmp/x/latihan.vbproj]"),
    ("vb", "Unhandled exception. System.OverflowException: Arithmetic operation resulted in an overflow.\n"
        "   at Latihan.Program.Main() in /tmp/x/Program.vb:line 4\n"
        "\n"
        "Program membatalkan dirinya sendiri (abort)."),
    ("vb", "/tmp/x/Program.vb(3,13): error BC30203: Identifier expected. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(2,5): error BC30188: Declaration expected. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(3,30): error BC30205: End of statement expected. [/tmp/x/latihan.vbproj]"),
    ("vb", "/tmp/x/Program.vb(3,9): error BC30084: 'For' must end with a matching 'Next'. [/tmp/x/latihan.vbproj]"),
    ("php", "\n"
         "Parse error: Unclosed '{' on line 2 in /tmp/x/program.php on line 4"),
    ("php", "\n"
         "Warning: Undefined variable $x in /tmp/x/program.php on line 2"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Call to undefined function foo() in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Call to undefined method A::bar() in /tmp/x/program.php:4\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Class \"Foo\" not found in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught TypeError: Unsupported operand types: string * int in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught ArgumentCountError: Too few arguments to function f(), 1 passed in /tmp/x/program.php on line 3 and exactly 2 expected in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 /tmp/x/program.php(3): f(1)"),
    ("php", "\n"
         "Warning: Attempt to read property \"nama\" on null in /tmp/x/program.php on line 3"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Call to a member function foo() on null in /tmp/x/program.php:3\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Cannot redeclare function f() (previously declared in /tmp/x/program.php:2) in /tmp/x/program.php on line 3\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Undefined constant \"FOO\" in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Warning: Array to string conversion in /tmp/x/program.php on line 2\n"
         "Array"),
    ("php", "\n"
         "Warning: require(x.php): Failed to open stream: No such file or directory in /tmp/x/program.php on line 2\n"
         "\n"
         "Fatal error: Uncaught Error: Failed opening required 'x.php' (include_path='.:/usr/share/pear:/usr/share/php') in /tmp/x/program.php:2"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Cannot modify readonly property A::$x in /tmp/x/program.php:6\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught UnhandledMatchError: Unhandled match case 5 in /tmp/x/program.php:3\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Cannot access private property A::$x in /tmp/x/program.php:6\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught ValueError: str_repeat(): Argument #2 ($times) must be greater than or equal to 0 in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 /tmp/x/program.php(2): str_repeat('a', -1)"),
    ("php", "\n"
         "Fatal error: Uncaught DivisionByZeroError: Modulo by zero in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Parse error: syntax error, unexpected variable \"$y\" in /tmp/x/program.php on line 3"),
    ("php", "\n"
         "Parse error: syntax error, unexpected token \";\" in /tmp/x/program.php on line 2"),
    ("php", "\n"
         "Warning: Trying to access array offset on null in /tmp/x/program.php on line 3"),
    ("php", "\n"
         "Fatal error: Uncaught TypeError: f(): Return value must be of type int, string returned in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 /tmp/x/program.php(3): f()"),
    ("php", "\n"
         "Warning: Undefined array key 5 in /tmp/x/program.php on line 3"),
    ("php", "\n"
         "Warning: Uninitialized string offset 10 in /tmp/x/program.php on line 3"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Cannot instantiate abstract class A in /tmp/x/program.php:3\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Parse error: syntax error, unexpected token \";\", expecting \")\" in /tmp/x/program.php on line 2"),
    ("php", "\n"
         "Parse error: syntax error, unexpected end of file, expecting variable or \"${\" or \"{$\" in /tmp/x/program.php on line 3"),
    ("php", "\n"
         "Fatal error: Uncaught Exception: boom in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Parse error: Unmatched '}' in /tmp/x/program.php on line 4"),
    ("php", "\n"
         "Warning: Undefined property: A::$x in /tmp/x/program.php on line 4"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Value of type int is not callable in /tmp/x/program.php:3\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Non-static method A::hi() cannot be called statically in /tmp/x/program.php:5\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Parse error: syntax error, unexpected token \"else\", expecting end of file in /tmp/x/program.php on line 2"),
    ("php", "\n"
         "Fatal error: Uncaught Error: Call to private method A::f() from global scope in /tmp/x/program.php:6\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("php", "\n"
         "Warning: foreach() argument must be of type array|object, int given in /tmp/x/program.php on line 2"),
    ("php", "\n"
         "Parse error: syntax error, unexpected end of file, expecting \",\" or \";\" in /tmp/x/program.php on line 2"),
    ("php", "\n"
         "Fatal error: Uncaught TypeError: count(): Argument #1 ($value) must be of type Countable|array, int given in /tmp/x/program.php:2\n"
         "Stack trace:\n"
         "#0 {main}"),
    ("kotlin", "main.kt:3:5: error: 'val' cannot be reassigned.\n"
            "    x = 2\n"
            "    ^"),
    ("kotlin", "main.kt:3:14: error: only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'String?'.\n"
            "    println(s.length)\n"
            "             ^"),
    ("kotlin", "main.kt:2:18: error: null cannot be a value of a non-null type 'Int'.\n"
            "    val n: Int = null\n"
            "                 ^^^^"),
    ("kotlin", "main.kt:3:18: error: too many arguments for 'fun f(a: Int): Int'.\n"
            "    println(f(1, 2))\n"
            "                 ^"),
    ("kotlin", "main.kt:2:16: error: syntax error: Expecting ')'.\n"
            "    println(\"a\"\n"
            "               ^"),
    ("kotlin", "main.kt:3:13: error: variable 'x' must be initialized.\n"
            "    println(x)\n"
            "            ^"),
    ("kotlin", "main.kt:2:9: error: conflicting declarations:\n"
            "local val a: Int\n"
            "local val a: Int\n"
            "    val a = 1"),
    ("kotlin", "main.kt:3:9: error: condition type mismatch: inferred type is 'Int' but 'Boolean' was expected.\n"
            "    if (x) {\n"
            "        ^"),
    ("kotlin", "main.kt:3:13: error: cannot create an instance of an abstract class.\n"
            "    val a = A()\n"
            "            ^^^"),
    ("kotlin", "main.kt:5:17: error: cannot access 'val x: Int': it is private in 'A'.\n"
            "    println(A().x)\n"
            "                ^"),
    ("kotlin", "main.kt:1:8: error: unresolved reference 'foo'.\n"
            "import foo.Bar\n"
            "       ^^^"),
    ("kotlin", "main.kt:2:9: error: this variable must either have an explicit type or be initialized.\n"
            "    val x =\n"
            "        ^\n"
            "main.kt:2:12: error: syntax error: Expecting an expression."),
    ("kotlin", "Exception in thread \"main\" kotlin.UninitializedPropertyAccessException: lateinit property n has not been initialized\n"
            "\tat A.getN(main.kt:2)\n"
            "\tat MainKt.main(main.kt:5)\n"
            "\tat MainKt.main(main.kt)"),
    ("kotlin", "Exception in thread \"main\" java.lang.NullPointerException\n"
            "\tat MainKt.main(main.kt:3)\n"
            "\tat MainKt.main(main.kt)"),
    ("kotlin", "Exception in thread \"main\" java.lang.IndexOutOfBoundsException: Index 5 out of bounds for length 3\n"
            "\tat java.base/jdk.internal.util.Preconditions.outOfBounds(Preconditions.java:64)\n"
            "\tat java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Preconditions.java:70)\n"
            "\tat java.base/jdk.internal.util.Preconditions.checkIndex(Preconditions.java:266)\n"
            "\tat java.base/java.util.Objects.checkIndex(Objects.java:361)\n"
            "\tat java.base/java.util.ArrayList.get(ArrayList.java:427)\n"
            "\tat MainKt.main(main.kt:3)\n"
            "\tat MainKt.main(main.kt)"),
    ("kotlin", "Exception in thread \"main\" java.util.NoSuchElementException: List is empty.\n"
            "\tat kotlin.collections.CollectionsKt___CollectionsKt.first(_Collections.kt:222)\n"
            "\tat MainKt.main(main.kt:3)\n"
            "\tat MainKt.main(main.kt)"),
    ("kotlin", "Exception in thread \"main\" java.lang.ClassCastException: class java.lang.String cannot be cast to class java.lang.Integer (java.lang.String and java.lang.Integer are in module java.base of loader 'bootstrap')\n"
            "\tat MainKt.main(main.kt:3)\n"
            "\tat MainKt.main(main.kt)"),
    ("kotlin", "main.kt:3:7: error: assignment type mismatch: actual type is 'String', but 'Int' was expected.\n"
            "    x = \"a\"\n"
            "      ^"),
    ("kotlin", "main.kt:2:12: error: return type mismatch: expected 'Int', actual 'String'.\n"
            "    return \"a\"\n"
            "           ^^^"),
    ("kotlin", "main.kt:3:13: error: no value passed for parameter 'b'.\n"
            "    println(f(a = 1, c = 2))\n"
            "            ^\n"
            "main.kt:3:22: error: no parameter with name 'c' found."),
    ("kotlin", "main.kt:3:7: error: unresolved reference 'add' on receiver of type 'List<Int>'.\n"
            "    l.add(3)\n"
            "      ^^^"),
    ("kotlin", "main.kt:4:15: error: argument type mismatch: actual type is 'String?', but 'String' was expected.\n"
            "    println(f(x))\n"
            "              ^"),
    ("kotlin", "Exception in thread \"main\" java.lang.StackOverflowError\n"
            "\tat MainKt.f(main.kt:1)\n"
            "\tat MainKt.f(main.kt:1)\n"
            "\tat MainKt.f(main.kt:1)"),
    ("kotlin", "Exception in thread \"main\" java.lang.IllegalStateException: x kosong\n"
            "\tat MainKt.main(main.kt:3)\n"
            "\tat MainKt.main(main.kt)"),
    ("typescript", "program.ts(1,5): error TS2322: Type 'string' is not assignable to type 'number'."),
    ("typescript", "program.ts(1,13): error TS2304: Cannot find name 'y'."),
    ("typescript", "program.ts(2,15): error TS2339: Property 'foo' does not exist on type '\"abc\"'."),
    ("typescript", "program.ts(1,12): error TS7006: Parameter 'x' implicitly has an 'any' type."),
    ("typescript", "program.ts(1,39): error TS18047: 's' is possibly 'null'."),
    ("typescript", "program.ts(2,15): error TS2551: Property 'lenght' does not exist on type '\"abc\"'. Did you mean 'length'?"),
    ("typescript", "program.ts(1,19): error TS2307: Cannot find module './nope' or its corresponding type declarations."),
    ("typescript", "program.ts(2,1): error TS2588: Cannot assign to 'a' because it is a constant."),
    ("typescript", "program.ts(2,7): error TS2741: Property 'b' is missing in type '{ a: number; }' but required in type 'P'."),
    ("typescript", "program.ts(1,13): error TS2448: Block-scoped variable 'a' used before its declaration.\n"
                "program.ts(1,13): error TS2454: Variable 'a' is used before being assigned."),
    ("typescript", "program.ts(1,15): error TS2355: A function whose declared type is neither 'undefined', 'void', nor 'any' must return a value."),
    ("typescript", "program.ts(1,24): error TS2366: Function lacks ending return statement and return type does not include 'undefined'."),
    ("typescript", "program.ts(1,5): error TS2451: Cannot redeclare block-scoped variable 'a'.\n"
                "program.ts(2,5): error TS2451: Cannot redeclare block-scoped variable 'a'."),
    ("typescript", "program.ts(1,9): error TS1109: Expression expected."),
    ("typescript", "program.ts(2,1): error TS2349: This expression is not callable.\n"
                "  Type 'Number' has no call signatures."),
    ("typescript", "program.ts(1,9): error TS2362: The left-hand side of an arithmetic operation must be of type 'any', 'number', 'bigint' or an enum type."),
    ("typescript", "program.ts(2,5): error TS2367: This comparison appears to be unintentional because the types 'number' and 'string' have no overlap."),
    ("typescript", "program.ts(1,11): error TS2564: Property 'x' has no initializer and is not definitely assigned in the constructor."),
    ("typescript", "program.ts(3,3): error TS2540: Cannot assign to 'a' because it is a read-only property."),
    ("typescript", "program.ts(2,8): error TS2345: Argument of type 'string' is not assignable to parameter of type 'number'."),
    ("typescript", "program.ts(1,1): error TS1128: Declaration or statement expected."),
    ("typescript", "program.ts(2,13): error TS7053: Element implicitly has an 'any' type because expression of type '\"b\"' can't be used to index type '{ a: number; }'.\n"
                "  Property 'b' does not exist on type '{ a: number; }'."),
    ("typescript", "program.ts(2,7): error TS2420: Class 'C' incorrectly implements interface 'I'.\n"
                "  Property 'f' is missing in type 'C' but required in type 'I'."),
    ("typescript", "program.ts(1,14): error TS1002: Unterminated string literal."),
    ("typescript", "program.ts(1,34): error TS2353: Object literal may only specify known properties, and 'b' does not exist in type '{ a: number; }'."),
    ("typescript", "program.ts(1,16): error TS1308: 'await' expressions are only allowed within async functions and at the top levels of modules."),
    ("typescript", "program.ts(2,6): error TS2554: Expected 1 arguments, but got 2."),
    ("typescript", "program.ts(1,20): error TS2769: No overload matches this call.\n"
                "  The last overload gave the following error.\n"
                "    Argument of type '{}' is not assignable to parameter of type 'string | number'."),
    ("typescript", "program.ts(3,1): error TS1005: '}' expected."),
]


def cakupan_galat(pesan):
    """Indeks pola yang benar-benar dijalani korpus ini.

    Dicatat ke rekaman supaya celahnya KELIHATAN. Pola yang tidak pernah
    tersentuh bukan pola yang aman -- ia pola yang belum diuji, dan rekaman
    yang tidak menyebutkan jumlahnya membuat orang mengira sebaliknya.
    """
    kena = set()
    for _bhs, teks in pesan:
        for i, (pola, _p) in enumerate(galat._TERKOMPILASI):
            if pola.search(teks):
                kena.add(i)
    return {
        "pola": len(galat.POLA),
        "tersentuh": len(kena),
        "tidak_tersentuh": sorted(set(range(len(galat.POLA))) - kena),
    }


def golden_galat():
    # Masukannya ditulis APA ADANYA, bukan cuma sidiknya. Versi pertama cuma
    # menyimpan sidik, dan akibatnya rekaman ini tidak bisa dipakai siapa pun
    # di luar Python: sisi TS tidak punya cara menurunkan pesan compiler dari
    # SHA-256-nya, jadi ia harus menyalin daftarnya -- dan salinan kedua yang
    # menyimpang membuat kedua sisi menguji dua korpus berbeda sambil
    # sama-sama hijau. Sidiknya tetap ditulis sebagai pagar atas masukannya
    # sendiri.
    kasus = []
    for bhs, pesan in list(PESAN) + PROBE:
        kasus.append({
            "bahasa": bhs,
            "masukan": pesan,
            "masukan_sha256": _sha(pesan),
            "terjemahan_sha256": _sha(galat.terjemahkan(pesan)),
            "ringkas_sha256": _sha(galat.ringkas(pesan)),
            "rapikan_sha256": _sha(galat.rapikan(pesan, "program")),
        })
    return kasus


# Pasangan (harapan, aktual) yang mewakili bentuk kegagalan nyata: beda satu
# huruf, beda spasi di ujung, baris hilang, baris tertukar, beda angka.
PASANGAN = [
    ("Halo, Dunia!", "Halo, dunia!"),
    ("12\n7\n", "12\n8\n"),
    ("a\nb\nc\n", "a\nc\n"),
    ("a\nb\nc\n", "a\nc\nb\n"),
    ("total: 1.500", "total: 1500"),
    ("baris  berkolom   rapi", "baris berkolom rapi"),
    ("selesai", "selesai "),
    ("", "ada isinya"),
    ("ada isinya", ""),
    # Tiga di bawah menutup cabang diagnosis yang tidak pernah terpicu korpus
    # hasilan. Bentuknya tidak realistis, dan memang bukan itu gunanya:
    # `uji/gigi-golden.py` menemukan bahwa mencabut sebuah awalan dari
    # `_AWALAN_NYARIS` tidak memerahkan apa pun, karena tidak satu pun dari
    # 309 pasangan menghasilkan kalimat itu. Cabang yang tidak pernah dijalani
    # adalah cabang yang bebas menyimpang saat diport.
    ("Halo.", "Halo"),                 # -> "Hanya beda TANDA BACA"
    ("Selesai.", "selesai"),           # -> beda kapital + tanda baca
    ("nilai  akhir", "Nilai Akhir"),   # -> beda spasi + kapital
]


def pasangan_hasilan(jumlah=300):
    """Pasangan keluaran yang DIHASILKAN, untuk menguji penyejajar barisnya.

    Sembilan pasangan di `PASANGAN` ditulis tangan untuk heuristik
    DIAGNOSISNYA, dan tidak satu pun darinya memicu rekursi
    `SequenceMatcher`: semuanya satu blok beda di satu tempat. Padahal justru
    penyejajar itu bagian yang paling mungkin menyimpang saat diport, karena
    ia bukan Myers diff dan pemenang-seri-blok-terpanjangnya halus.

    Jadi di sini keluaran berbilah banyak dirusak dengan cara-cara yang
    memaksa rekursinya: baris disisipkan, dibuang, ditukar tempat, dan
    diduplikasi. Duplikasi yang paling tajam -- baris yang sama muncul
    beberapa kali membuat beberapa blok cocok berukuran sama, dan di situlah
    dua implementasi bisa memilih yang berbeda tanpa salah satunya salah.

    SEED-nya bagian dari rekaman. Mengubahnya berarti mengganti seluruh
    korpus, dan rekaman yang korpusnya berubah tidak membuktikan apa pun soal
    perubahan yang sedang diperiksa. Kalau korpusnya perlu diperluas, TAMBAH
    kasus di ujung; jangan sentuh seed-nya.
    """
    import random
    rng = random.Random(20261020)
    kata = ["total", "nama", "skor", "Budi", "Ani", "lulus", "gagal",
            "0", "1", "10", "3.0", "3", "-5", "OK", "selesai", ""]

    def baris_acak():
        n = rng.randint(1, 4)
        return " ".join(rng.choice(kata) for _ in range(n)).strip()

    keluar = []
    for _ in range(jumlah):
        n = rng.randint(1, 9)
        asal = [baris_acak() for _ in range(n)]
        # Baris duplikat disuntikkan dengan sengaja: tanpa itu hampir setiap
        # baris unik, dan blok cocok terpanjangnya selalu tunggal.
        if n >= 2 and rng.random() < 0.5:
            asal[rng.randrange(n)] = asal[rng.randrange(n)]
        rusak = list(asal)
        for _ in range(rng.randint(1, 3)):
            aksi = rng.choice(("sisip", "buang", "ubah", "tukar"))
            if aksi == "sisip":
                rusak.insert(rng.randint(0, len(rusak)), baris_acak())
            elif aksi == "buang" and rusak:
                rusak.pop(rng.randrange(len(rusak)))
            elif aksi == "ubah" and rusak:
                rusak[rng.randrange(len(rusak))] = baris_acak()
            elif aksi == "tukar" and len(rusak) >= 2:
                i, j = rng.randrange(len(rusak)), rng.randrange(len(rusak))
                rusak[i], rusak[j] = rusak[j], rusak[i]
        keluar.append(("\n".join(asal), "\n".join(rusak)))
    return keluar


def golden_beda():
    kasus = []
    for harap, aktual in list(PASANGAN) + pasangan_hasilan():
        hasil = beda.bandingkan(harap, aktual)
        # `Beda` objek biasa tanpa __dict__, jadi medannya diambil eksplisit.
        # Menyebutnya satu per satu juga membuat medan BARU yang ditambahkan
        # nanti tidak diam-diam lolos dari rekaman ini.
        bentuk = {m: getattr(hasil, m) for m in
                  ("sama", "nomor_beda", "kolom_beda", "catatan",
                   "harapan", "aktual")}
        bentuk["baris"] = [list(b) if isinstance(b, tuple) else b
                           for b in (hasil.baris or [])]
        kasus.append({
            # Apa adanya, dengan alasan yang sama seperti di `golden_galat`.
            "harap": harap,
            "aktual": aktual,
            "harap_sha256": _sha(harap),
            "aktual_sha256": _sha(aktual),
            "bandingkan_sha256": _sha(bentuk),
            "nyaris": beda.nyaris(hasil),
            "kolom_pertama_beda": beda.kolom_pertama_beda(harap, aktual),
        })
    return kasus


def cakupan(blok):
    """Berapa blok yang benar-benar tersorot, dan bahasa apa yang tidak.

    Ini yang membuat rekaman di bawah bisa menyebut PENYEBAB, bukan cuma
    melaporkan sidik yang bergeser. Sebuah pemetaan yang hilang di
    `berkas.sorot_untuk` menggeser ratusan sidik sekaligus, dan daftar sidik
    tidak memberi tahu apa pun soal mana yang hilang -- sedangkan satu nama
    bahasa yang pindah dari "tersorot" ke "polos" langsung menunjuknya.
    """
    # `sorot.ATURAN`, bukan `sorot.bahasa_didukung()`. Yang kedua membuang
    # duplikat berdasarkan `id()`, jadi ia menjawab "ada berapa SET aturan
    # yang berbeda" -- bukan "nama apa saja yang dikenali". Memakainya di sini
    # menggolongkan setiap alias sebagai tidak tersorot, dan `aplikasi` (68
    # blok, alias Java) langsung muncul di puncak daftar sebagai bukti.
    punya = set(sorot.ATURAN)
    polos = collections.Counter(b[1] for b in blok if b[1] not in punya)
    return {
        "tersorot": sum(1 for b in blok if b[1] in punya),
        "polos": sum(polos.values()),
        # Bahasa tanpa aturan penyorotan. Angkanya ikut dicatat supaya
        # menambah aturan baru untuk salah satunya terlihat sebagai
        # perbaikan yang terukur, bukan sebagai "golden bergeser".
        "bahasa_polos": dict(sorted(polos.items())),
    }


def susun():
    blok = korpus()
    kasus_sorot, cacat = golden_sorot(blok)
    if cacat:
        raise ValueError("token tidak merekonstruksi sumbernya: "
                         + ", ".join(cacat[:3]))
    return {
        "sorot.json": {
            "fungsi": "sorot.token(kode, bahasa) -> [[jenis, teks]]",
            "catatan": "Gabungan teks token WAJIB sama persis dengan kodenya.",
            "bahasa_didukung": sorot.bahasa_didukung(),
            "cakupan": cakupan(blok),
            "kasus": kasus_sorot,
        },
        "galat.json": {
            "fungsi": "galat.terjemahkan(pesan), ringkas(pesan), rapikan(pesan, nama)",
            "cakupan": cakupan_galat(list(PESAN) + PROBE),
            "kasus": golden_galat(),
        },
        "beda.json": {
            "fungsi": "beda.bandingkan(harap, aktual), nyaris, kolom_pertama_beda",
            "kasus": golden_beda(),
        },
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tulis", action="store_true")
    a = ap.parse_args()

    berkas = susun()
    n = len(berkas["sorot.json"]["kasus"])
    print(f"sorot: {n} blok kode di {len(LANGUAGES)} kurikulum")
    print(f"galat: {len(berkas['galat.json']['kasus'])} pesan compiler")
    print(f"beda : {len(berkas['beda.json']['kasus'])} pasangan keluaran")

    lama = {}
    for nama in berkas:
        jalur = os.path.join(TUJUAN, nama)
        if os.path.exists(jalur):
            with open(jalur, encoding="utf-8") as f:
                lama[nama] = json.load(f)
    # `isi` sengaja TIDAK dipakai sebagai nama di sini: modul `webapp.isi`
    # sudah memakai nama itu di berkas ini, dan loop yang menimpanya pernah
    # jadi bug yang cuma muncul kalau cabangnya diambil.
    if lama:
        geser = [n for n, rekaman in lama.items() if rekaman != berkas[n]]
        if geser:
            print("BERGESER dari rekaman sebelumnya:", ", ".join(geser))
            if not a.tulis:
                # Menolak di sini TANPA --tulis saja. Versi sebelumnya menolak
                # keduanya sekaligus sambil mencetak "kalau ini disengaja,
                # tulis ulang" -- saran yang mustahil diikuti, karena jalurnya
                # sendiri yang ditutup. Pagar yang tidak bisa dilewati dengan
                # sengaja bukan pagar; ia cuma alat yang rusak.
                print("  Kalau ini disengaja, jalankan ulang dengan --tulis. "
                      "Kalau tidak, cari perubahan yang menyebabkannya "
                      "SEBELUM menerimanya.")
                return 1
            print("  --tulis diberikan: rekaman DIGANTI dengan yang sekarang.")
        else:
            print("cocok dengan rekaman sebelumnya")

    if a.tulis:
        os.makedirs(TUJUAN, exist_ok=True)
        for nama, isi in berkas.items():
            with open(os.path.join(TUJUAN, nama), "w", encoding="utf-8") as f:
                json.dump(isi, f, ensure_ascii=False, indent=1)
                f.write("\n")
        print(f"  ditulis {len(berkas)} berkas ke packages/bersama/golden/")
    else:
        print("  (belum ditulis; tambahkan --tulis)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
