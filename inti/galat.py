"""Menerjemahkan pesan error compiler/runtime jadi kalimat yang bisa dimengerti.

Aplikasi ini dipakai orang yang belajar dari nol. Menyodorkan

    /tmp/belajar-cp54ht3k/Halo.java:3: error: ';' expected

kepada orang seperti itu praktis sama dengan tidak memberi tahu apa-apa: path
yang tidak pernah dia buka, istilah Inggris, dan nomor baris yang tidak cocok
dengan berkas miliknya karena runner menempelkan kode prasyarat di depan.

Modul ini menangani ketiganya:

* `rapikan()` mengganti path sementara dengan nama berkas kerja pelajar dan
  menggeser nomor baris sebanyak baris `setup` yang ditempel.
* `terjemahkan()` mencocokkan pesan dengan tabel pola dan mengembalikan
  penjelasan berbahasa Indonesia beserta saran perbaikannya.
* `ringkas()` memotong pesan panjang dari ujung yang tepat -- traceback Python
  paling berguna di bagian akhir, keluaran kompiler di bagian awal.

Kalau tidak ada pola yang cocok, pesan aslinya tetap ditampilkan apa adanya.
Menebak-nebak lebih berbahaya daripada diam.

Importir: layar/exercises.py (tampilan hasil uji & mode "jalankan saja").
"""

import re

# (pola, penjelasan) -- diurutkan dari yang paling spesifik.
# Penjelasan boleh memakai \1, \2 untuk grup tangkapan pola.
POLA = [
    # ----------------------------------------------------------------- Java
    # Berjangkar pada "error: " supaya `error TS1005: ';' expected` dari tsc
    # tidak ikut dijelaskan dengan kalimat "Di Java ...". javac selalu menulis
    # awalan itu.
    (r"error: ';' expected",
     "Ada baris yang lupa diakhiri titik koma (;). Di Java setiap pernyataan "
     "wajib ditutup titik koma."),
    (r"cannot find symbol.*?symbol:\s*variable (\w+)",
     "Variabel '\\1' dipakai tapi belum pernah dideklarasikan. Periksa ejaan "
     "dan huruf besar/kecilnya -- Java membedakan Nama dan nama."),
    (r"cannot find symbol.*?symbol:\s*method (\w+)",
     "Method '\\1' tidak dikenal. Periksa ejaannya, atau kelas/objek yang kamu "
     "panggil memang tidak punya method itu."),
    (r"cannot find symbol",
     "Ada nama (variabel, method, atau kelas) yang dipakai tapi belum "
     "dideklarasikan, atau ejaannya berbeda."),
    (r"incompatible types: (\S+) cannot be converted to (\S+)",
     "Tipe data tidak cocok: nilai bertipe \\1 dimasukkan ke tempat yang "
     "menuntut \\2. Konversi dulu, misalnya dengan Integer.parseInt()."),
    (r"class \w+ is public, should be declared in a file named",
     "Nama kelas public harus sama persis dengan nama berkasnya. Aplikasi ini "
     "biasanya mengurusnya otomatis; pastikan hanya ada satu kelas public."),
    (r"missing return statement",
     "Ada method dengan tipe kembalian (bukan void) yang tidak selalu "
     "melakukan return. Pastikan semua cabang if/else mengembalikan nilai."),
    (r"unreachable statement",
     "Ada kode setelah return/break yang tidak akan pernah dijalankan."),
    (r"reached end of file while parsing",
     "Ada kurung kurawal { yang belum ditutup. Hitung kembali pasangan { dan }."),
    # `(?!.*MainKt)`: jejak tumpukan Kotlin memuat MainKt, dan Kotlin punya
    # penjelasannya sendiri di bagian bawah (tidak ada 'new' di sana).
    (r"NullPointerException(?!.*MainKt)",
     "Program memakai objek yang isinya null (belum diisi). Pastikan objeknya "
     "sudah dibuat dengan 'new' sebelum dipakai."),
    (r"ArrayIndexOutOfBoundsException",
     "Indeks array di luar jangkauan. Ingat indeks pertama adalah 0 dan yang "
     "terakhir adalah panjang - 1."),
    (r"NumberFormatException",
     "Gagal mengubah teks jadi angka. Teks yang dibaca bukan angka yang sah "
     "(mungkin ada spasi atau baris kosong)."),
    (r"ArithmeticException: / by zero",
     "Pembagian dengan nol. Periksa dulu apakah pembaginya nol."),
    (r"NoSuchElementException(?!.*MainKt)",
     "Scanner membaca input yang sudah habis. Latihan ini mungkin tidak "
     "mengirim input sebanyak yang kamu baca."),

    # --------------------------------------------------------------- Python
    (r"IndentationError: (?:unexpected indent|expected an indented block)",
     "Indentasi (jumlah spasi di awal baris) tidak konsisten. Di Python "
     "indentasi menentukan blok kode -- pakai 4 spasi dan jangan campur "
     "spasi dengan tab."),
    (r"TabError",
     "Tab dan spasi tercampur dalam satu blok. Pilih salah satu, disarankan "
     "4 spasi."),
    # Python 3.10+ mengganti "invalid syntax" yang serba-guna dengan pesan yang
    # jauh lebih spesifik. Tanpa pola-pola berikut semuanya jatuh ke jawaban
    # umum di bawah -- yang justru menyembunyikan petunjuk terbaik yang sudah
    # susah payah diberikan Python.
    (r"SyntaxError: '(.)' was never closed",
     "Tanda '\\1' dibuka tapi tidak pernah ditutup. Hitung lagi pasangan "
     "buka-tutupnya. Python menunjuk baris tempat tanda itu DIBUKA, bukan "
     "tempat kesalahannya baru terasa."),
    (r"SyntaxError: unmatched '(.)'",
     "Ada '\\1' penutup yang tidak punya pasangan pembuka."),
    (r"SyntaxError: expected ':'",
     "Kurang titik dua (:) di akhir baris. Baris if, elif, else, for, while, "
     "def, dan class selalu ditutup titik dua."),
    (r"Perhaps you forgot a comma",
     "Sepertinya ada koma yang kurang di antara dua nilai."),
    (r"SyntaxError: cannot assign to (?:literal|expression)",
     "Sisi kiri tanda = harus berupa nama variabel. Kalau maksudmu "
     "MEMBANDINGKAN dua nilai, pakai == (dua tanda sama dengan)."),
    (r"SyntaxError: invalid syntax",
     "Ada kesalahan penulisan. Tersering: lupa titik dua (:) di akhir baris "
     "if/for/while/def, atau kurung yang belum ditutup."),
    (r"object is not subscriptable",
     "Nilai ini tidak bisa diakses dengan kurung siku [ ]. Kurung siku hanya "
     "berlaku untuk list, tuple, string, dan dictionary."),
    (r"object is not callable",
     "Nilai ini dipanggil seperti fungsi padahal bukan fungsi. Periksa apakah "
     "ada nama variabel yang tanpa sengaja menimpa nama fungsi."),
    (r"takes \d+ positional arguments? but \d+ (?:was|were) given",
     "Jumlah argumen saat memanggil fungsi tidak cocok dengan jumlah parameter "
     "di definisinya."),
    (r"SyntaxError: unterminated string literal",
     "Ada teks yang tanda kutipnya belum ditutup."),
    (r"NameError: name '(\w+)' is not defined",
     "Nama '\\1' dipakai sebelum dibuat. Periksa ejaan dan huruf besar/kecil, "
     "atau apakah variabelnya memang sudah diisi sebelumnya."),
    (r"TypeError: unsupported operand type\(s\) for \+: 'int' and 'str'",
     "Angka dan teks tidak bisa dijumlahkan langsung. Ubah dulu dengan "
     "int(teks) atau str(angka)."),
    (r"TypeError: can only concatenate str",
     "Teks hanya bisa disambung dengan teks. Bungkus angkanya dengan str(), "
     "atau pakai f-string."),
    (r"ValueError: invalid literal for int\(\)",
     "int() menerima teks yang bukan angka. Kalau membaca input, pastikan "
     "isinya memang angka dan tidak ada spasi berlebih."),
    (r"IndexError: list index out of range",
     "Indeks list di luar jangkauan. Ingat indeks pertama 0 dan terakhir "
     "len(daftar) - 1."),
    (r"ZeroDivisionError",
     "Pembagian dengan nol. Periksa dulu apakah pembaginya nol."),
    (r"EOFError",
     "Program membaca input lebih banyak daripada yang tersedia. Periksa "
     "berapa kali input() dipanggil."),
    (r"AttributeError: '(\w+)' object has no attribute '(\w+)'",
     "Objek bertipe \\1 tidak punya '\\2'. Periksa ejaannya, atau tipe "
     "variabelnya memang bukan yang kamu kira."),
    (r"ModuleNotFoundError: No module named '(\w+)'",
     "Pustaka '\\1' tidak terpasang. Latihan di aplikasi ini hanya boleh "
     "memakai pustaka bawaan bahasa."),
    (r"KeyError",
     "Kunci yang dicari tidak ada di dictionary. Periksa ejaannya, atau pakai "
     ".get(kunci) yang aman kalau kuncinya boleh tidak ada."),

    # -------------------------------------------------------------- C / C++
    (r"expected ';' before",
     "Ada pernyataan yang lupa diakhiri titik koma (;)."),
    (r"undefined reference to `main'",
     "Program tidak punya fungsi main(). Setiap program C/C++ wajib punya "
     "int main(void) { ... }."),
    (r"undefined reference to `(\w+)'",
     "Fungsi '\\1' dipanggil tapi tidak pernah didefinisikan (atau pustakanya "
     "belum di-#include)."),
    (r"implicit declaration of function '(\w+)'",
     "Fungsi '\\1' dipakai sebelum dikenalkan. Biasanya kurang #include, "
     "misalnya <stdio.h> untuk printf atau <string.h> untuk strlen."),
    (r"'(\w+)' undeclared",
     "Nama '\\1' belum dideklarasikan. Deklarasikan tipenya dulu, "
     "misalnya: int \\1 = 0;"),
    (r"format '%\w+' expects argument of type",
     "Kode format printf tidak cocok dengan tipe datanya. %d untuk int, "
     "%f untuk float/double, %s untuk teks, %c untuk satu karakter."),
    (r"expected '\}' at end of input",
     "Ada kurung kurawal { yang belum ditutup."),
    (r"segmentation fault",
     "Program mengakses memori yang bukan miliknya. Tersering: indeks array "
     "kelewat batas, atau pointer yang belum diisi."),

    # ----------------------------------------------------------- JavaScript
    (r"ReferenceError: (\w+) is not defined",
     "Nama '\\1' dipakai sebelum dibuat. Periksa ejaan dan huruf "
     "besar/kecilnya."),
    (r"TypeError: (\S+) is not a function",
     "\\1 dipanggil seperti fungsi padahal bukan fungsi. Periksa ejaan nama "
     "method-nya."),
    (r"TypeError: Cannot read propert(?:y|ies) of undefined",
     "Program membaca properti dari nilai undefined. Pastikan objek/array-nya "
     "sudah terisi sebelum dipakai."),
    (r"SyntaxError: Unexpected token",
     "Ada karakter yang tidak pada tempatnya. Tersering: kurung atau kurung "
     "kurawal yang tidak berpasangan."),
    (r"Assignment to constant variable",
     "Variabel yang dibuat dengan const tidak bisa diisi ulang. Pakai let "
     "kalau nilainya memang perlu berubah."),

    # ------------------------------------------------------------------- Go
    (r'"([\w/]+)" imported and not used',
     "Paket \"\\1\" di-import tapi tidak dipakai. Go melarang import yang "
     "menganggur -- hapus barisnya."),
    (r"(\w+) declared and not used",
     "Variabel '\\1' dibuat tapi tidak pernah dipakai. Go melarang itu -- "
     "hapus, atau pakai _ sebagai namanya."),
    (r"undefined: (\w+)",
     "Nama '\\1' belum didefinisikan. Periksa ejaannya; di Go huruf besar di "
     "awal nama juga bermakna."),
    (r"expected declaration",
     "Ada kode di luar fungsi. Di Go semua pernyataan harus berada di dalam "
     "func."),
    (r"invalid operation: .+ \(mismatched types (\S+) and (\S+)\)",
     "Tipe \\1 dan \\2 tidak bisa dioperasikan langsung. Go tidak mengonversi "
     "tipe secara otomatis."),
    (r"index out of range",
     "Indeks slice/array di luar jangkauan."),

    # ----------------------------------------------------------------- Bash
    (r"unexpected EOF while looking for matching",
     "Ada tanda kutip atau kurung yang belum ditutup."),
    (r"syntax error near unexpected token",
     "Ada kesalahan penulisan. Di Bash, spasi di sekitar = saat memberi nilai "
     "TIDAK boleh ada: tulis nama=\"Budi\", bukan nama = \"Budi\"."),
    # Harus lebih spesifik daripada "command not found" di bawahnya. Menulis
    # `nama = "Budi"` dengan spasi di sekitar = adalah kesalahan Bash paling
    # sering di kalangan pemula, dan pesan aslinya sama sekali tidak
    # menyinggungnya: bash cuma bilang "nama: command not found".
    (r"line \d+: (\w+): command not found",
     "Bash mengira '\\1' adalah nama perintah. Kalau maksudmu mengisi variabel, "
     "hilangkan spasi di sekitar tanda sama dengan: tulis \\1=\"nilai\", bukan "
     "\\1 = \"nilai\"."),
    (r"command not found",
     "Perintah tidak dikenal. Periksa ejaannya, atau program itu memang belum "
     "terpasang di komputer ini."),
    (r"integer expression expected",
     "Perbandingan angka memakai operator teks. Pakai -eq/-lt/-gt untuk angka "
     "dan =/!= untuk teks."),

    # --------------------------------------------------------------- SQLite
    (r'near "(\w+)": syntax error',
     "SQLite tidak mengenali \"\\1\" di posisi itu. Kalau ini sintaks khas "
     "MySQL (AUTO_INCREMENT, ENGINE=InnoDB, SHOW TABLES), memang tidak "
     "didukung -- pakai padanan SQLite-nya."),
    (r"no such table: (\w+)",
     "Tabel '\\1' belum ada. Tiap latihan SQL dijalankan di database kosong; "
     "buat tabelnya dulu, atau pakai tabel dari bagian KONDISI AWAL."),
    (r"no such column: (\w+)",
     "Kolom '\\1' tidak ada di tabel itu. Periksa ejaan nama kolomnya."),
    (r"UNIQUE constraint failed: (\S+)",
     "Nilai yang dimasukkan ke \\1 sudah ada, padahal kolom itu wajib unik."),

    # --------------------------------------------------------- HTML & CSS
    #
    # Pesan dari struktur.py sudah berbahasa Indonesia dan sudah menyebut
    # nomor barisnya. Yang ditambahkan di sini bukan terjemahan melainkan
    # AKIBATNYA — bagian yang paling sering tidak diduga pemula, karena
    # browser tidak pernah mengeluh dan halamannya tetap tampil.
    (r"<(\w+)> dibuka tapi tidak pernah ditutup",
     "Tag <\\1> tidak punya penutup </\\1>. Browser tidak akan menampilkan "
     "pesan error untuk ini -- ia menebak sendiri di mana elemennya berakhir, "
     "dan tebakannya sering menelan elemen-elemen di bawahnya. Itu sebabnya "
     "satu tag yang lupa ditutup bisa membuat separuh halaman ikut bergeser."),
    (r"</(\w+)> menutup sesuatu yang tidak pernah dibuka",
     "Ada </\\1> tanpa <\\1> pasangannya di atasnya. Biasanya ini sisa dari "
     "menghapus satu baris tapi lupa menghapus penutupnya."),
    (r"</(\w+)> tidak diperlukan",
     "<\\1> termasuk elemen kosong -- ia tidak membungkus apa pun, jadi tidak "
     "punya tag penutup. Cukup tulis <\\1> saja."),
    (r"tidak diikuti '\{'",
     "Setiap aturan CSS berbentuk `pemilih { properti: nilai; }`. Ada teks "
     "yang berdiri sendiri tanpa blok kurung kurawal di belakangnya."),
    (r"dibuka dengan '\{' tapi tidak pernah ditutup",
     "Ada blok CSS yang kurung kurawalnya tidak ditutup. Semua aturan "
     "sesudahnya ikut tertelan ke dalam blok itu dan berhenti berlaku -- "
     "gejalanya: satu perubahan kecil membuat banyak gaya lain hilang."),
    (r"bukan deklarasi yang sah",
     "Deklarasi CSS selalu berbentuk `properti: nilai;` -- pakai titik dua "
     "antara nama properti dan nilainya, dan titik koma di akhirnya."),
    (r"blok '\{ … \}' tanpa pemilih",
     "Ada kurung kurawal yang tidak didahului pemilih. CSS perlu tahu "
     "elemen mana yang diatur: `p { ... }`, `.kartu { ... }`, `#judul { ... }`."),

    # =====================================================================
    # Ruby, Rust, C#, Visual Basic, PHP, Kotlin, TypeScript (2026-10-28)
    #
    # Semua pola di bawah DITURUNKAN dari pesan yang keluar dari toolchain
    # sungguhan lewat `runner.jalankan` (Ruby 4.0 dengan parser Prism, rustc,
    # .NET SDK, PHP 8, kotlinc K2, tsc 5), bukan dari ingatan. Tiga aturan
    # yang membuatnya aman dicampur dengan bahasa di atas:
    #
    # * Tiap pola berjangkar pada frasa yang cuma dimiliki bahasanya: kode
    #   galat (`error TS2304`, `error CS0103`, `error BC30451`), nama kelas
    #   exception (`System.NullReferenceException`), atau kalimat khas
    #   (`Call to undefined function`). Pola yang cuma berbunyi "cannot find
    #   name" akan ikut menelan pesan bahasa lain.
    # * Pola umum dan pola khusus untuk pesan yang sama dibuat SALING
    #   MENGECUALIKAN lewat lookahead negatif di dalam kecocokan, supaya satu
    #   pesan menghasilkan satu penjelasan, bukan dua kalimat yang mengulang.
    #   Lookahead itu tidak boleh melihat melewati teks yang cocok: kalimat
    #   penjelasan disusun dengan mencocokkan ulang pola pada `group(0)`.
    # * Penjelasan Kotlin untuk exception JVM berjangkar pada `MainKt` (nama
    #   kelas yang runner pasang untuk main.kt), karena pesannya sama persis
    #   dengan Java dan pola Java di atas sudah menjelaskannya dengan bahasa
    #   Java ("dengan 'new'"). Tiga pola Java itu dipersempit dengan jangkar
    #   yang sama; pesan Java tidak berubah.
    #
    # Perlu diketahui sebelum mengandalkannya di aplikasi (per 2026-10-28):
    # `terjemahkan()` cuma diberi `hasil.galat` (stderr). Pesan kompilasi
    # .NET (C#, VB) dan tsc keluar lewat STDOUT, dan semua pesan PHP juga
    # (display_errors menyala), jadi untuk kasus itu `galat` berisi
    # "Kompilasi gagal." atau kosong dan penjelasan di bawah belum sampai ke
    # layar. Pola-polanya benar untuk teks yang dikeluarkan compiler; yang
    # perlu disambungkan adalah jalur runner, di luar modul ini. Pesan
    # runtime C# dan VB, serta kompilasi Rust dan Kotlin, lewat stderr dan
    # sampai. Galat sintaks PHP sampai lewat `cek_sintaks` (`php -l`).

    # ----------------------------------------------------------------- Ruby
    # Nama method dan konstanta diapit kutip tunggal di Ruby 4.0; versi lama
    # menulis `nama' dengan backtick di depan, jadi kelas [`'] menerima keduanya.
    (r"undefined local variable or method [`']([^'`\s]+)[`']",
     "Nama '\\1' tidak dikenal: bukan variabel yang sudah diisi, dan bukan "
     "nama method. Periksa ejaan dan huruf besar/kecilnya, atau pastikan "
     "variabelnya sudah diberi nilai sebelum baris ini."),
    (r"uninitialized constant (\S+)",
     "'\\1' diawali huruf besar, jadi Ruby mengiranya nama kelas atau "
     "konstanta, dan ia belum ada. Periksa ejaannya, atau pastikan kelasnya "
     "sudah didefinisikan di atas baris ini."),
    (r"undefined method [`']([^'`\s]+)[`'] for nil",
     "Method '\\1' dipanggil pada nilai nil (kosong), bukan pada objek. "
     "Paling sering karena variabelnya belum diisi, hash atau array yang "
     "kunci atau indeksnya tidak ada, atau gets yang tidak mendapat input. "
     "Periksa dari mana nilainya datang, atau pakai &. supaya nil dilewati."),
    (r"undefined method [`']([^'`\s]+)[`'] for an instance of (\S+)",
     "Objek bertipe \\2 tidak punya method '\\1'. Periksa ejaannya, atau "
     "tipe nilainya memang bukan yang kamu kira."),
    (r"undefined method [`']([^'`\s]+)[`'] for (?:class|module) (\S+)",
     "'\\2' tidak punya method kelas '\\1'. Periksa ejaannya, atau method itu "
     "ditulis tanpa self. sehingga cuma bisa dipanggil lewat objek, bukan "
     "lewat nama kelasnya."),
    (r"(private|protected) method [`']([^'`\s]+)[`'] called for",
     "Method '\\2' berstatus \\1, jadi tidak bisa dipanggil dari luar "
     "kelasnya. Pindahkan ke bagian public, atau panggil lewat method public "
     "lain di kelas itu."),
    (r"invalid value for (Integer|Float)\(\): \"([^\"\n]*)\"",
     "\\1() menolak teks \"\\2\" karena bukan angka yang sah. Periksa isinya, "
     "mungkin ada huruf atau spasi nyasar. to_i dan to_f tidak melempar "
     "error, tapi diam-diam menghasilkan 0 untuk teks seperti itu."),
    (r"can't convert nil into (\w+)",
     "nil (kosong) tidak bisa diubah jadi \\1. Periksa dari mana nilainya "
     "datang: mungkin variabelnya belum diisi, atau gets tidak mendapat input."),
    (r"wrong number of arguments \(given (\d+), expected ([^)]+)\)",
     "Method dipanggil dengan \\1 argumen, padahal definisinya meminta \\2. "
     "Samakan jumlah argumen saat memanggil dengan parameter di def-nya."),
    (r"missing keywords?: :(\w+)",
     "Parameter bernama (keyword) '\\1' wajib diisi tapi tidak diberikan saat "
     "memanggil. Tulis \\1: nilai di pemanggilnya."),
    (r"no block given \(yield\)",
     "Method ini memakai yield, tapi dipanggil tanpa blok. Panggil dengan "
     "blok (do ... end atau { ... }), atau cek dulu dengan block_given?."),
    (r"index (-?\d+) outside of array bounds",
     "Indeks \\1 di luar jangkauan array, dan fetch menolak indeks yang tidak "
     "ada (berbeda dengan [] yang diam-diam memberi nil). Ingat indeks "
     "pertama 0 dan yang terakhir panjang - 1."),
    (r"no implicit conversion of (\w+) into (\w+)",
     "Ruby tidak mengubah \\1 jadi \\2 secara otomatis. Ubah sendiri, "
     "misalnya angka.to_s sebelum disambung ke teks, atau teks.to_i untuk "
     "dihitung."),
    (r"\bnil can't be coerced into (\w+)",
     "Ada nilai nil (kosong) yang ikut dihitung dengan \\1. Periksa variabel "
     "atau hasil method yang dipakai di perhitungan itu: mungkin belum diisi, "
     "atau hash atau array-nya tidak punya kunci atau indeks tersebut."),
    (r"\b(?!nil\b)(\w+) can't be coerced into (\w+)",
     "\\1 tidak bisa dihitung bersama \\2. Samakan tipenya dulu, misalnya "
     "teks.to_i atau angka.to_s."),
    (r"comparison of (\w+) with (\S+) failed",
     "Ruby tidak bisa membandingkan \\1 dengan \\2, jadi tidak tahu mana yang "
     "lebih besar. Isi array atau nilai yang dibandingkan harus sejenis: "
     "semuanya angka, atau semuanya teks."),
    (r"can't modify frozen (\w+)",
     "Objek \\1 ini sudah dibekukan (frozen), jadi isinya tidak boleh diubah "
     "di tempat. Buat salinannya dengan dup lalu ubah salinan itu."),
    (r"cannot load such file -- (\S+)",
     "Berkas atau pustaka '\\1' tidak ditemukan oleh require. Periksa "
     "ejaannya. Di aplikasi ini hanya pustaka bawaan Ruby yang bisa dipakai, "
     "dan berkas lain harus dipanggil dengan require_relative."),
    (r"No such file or directory @ \w+ - (\S+)",
     "Berkas atau folder '\\1' tidak ada. Periksa ejaan nama dan letaknya; "
     "program ini berjalan di folder sementara yang hanya berisi berkasnya "
     "sendiri."),
    (r"stack level too deep",
     "Method memanggil dirinya sendiri terus-menerus sampai tumpukan panggilan "
     "penuh. Rekursi wajib punya kondisi berhenti, dan tiap panggilan harus "
     "mendekatinya."),
    (r"expected (?:an [`']end[`'] to close|a block beginning with [`']do[`'] "
     r"to end with [`']end[`'])",
     "Ada blok (def, if, class, do, atau while) yang belum ditutup dengan "
     "end. Hitung pasangan pembuka dan end-nya; Ruby menunjuk tempat blok itu "
     "dibuka."),
    (r"expected a(?: matching)? [`']([)\]}])[`']",
     "Ada kurung yang belum ditutup: Ruby mengharapkan \\1 untuk menutupnya. "
     "Hitung lagi pasangan kurungnya."),
    (r"unexpected [`']([a-z]+)[`'], ignoring it",
     "Kata kunci \\1 muncul di tempat yang tidak membukanya. Biasanya ada end "
     "yang kelebihan, atau else dan elsif yang dobel. Hitung lagi pasangan "
     "if, def, dan do dengan end-nya."),
    (r"unterminated string meets end of file",
     "Ada teks yang tanda kutipnya belum ditutup."),

    # ----------------------------------------------------------------- Rust
    # Pesan rustc di sini ditulis dengan backtick, bukan kutip tunggal, jadi
    # tidak bertabrakan dengan pola C ("expected ';' before") di atas.
    (r"cannot find (?:value|function) `(\w+)` in this scope",
     "Nama '\\1' tidak dikenal di sini. Periksa ejaan dan huruf besar/"
     "kecilnya, dan pastikan variabelnya dibuat dengan let sebelum dipakai "
     "serta masih berada di dalam blok yang sama."),
    (r"(?:cannot find type|use of undeclared type) `(\w+)`",
     "Tipe '\\1' belum dikenal di sini. Tipe dari pustaka standar, misalnya "
     "HashMap, harus diimpor dulu dengan use (use std::collections::HashMap;), "
     "dan ejaannya harus tepat."),
    (r"cannot find macro `(\w+)` in this scope",
     "Makro '\\1!' tidak dikenal. Periksa ejaan namanya (println!, format!, "
     "vec!), dan ingat makro selalu diakhiri tanda seru."),
    (r"unresolved import `([^`]+)`",
     "Impor '\\1' tidak ditemukan. Periksa ejaan jalurnya dan huruf besar/"
     "kecilnya. Di aplikasi ini hanya pustaka standar (std) yang tersedia."),
    (r"error\[E0308\]: mismatched types.*?expected ([^\n]+?), found ([^\n]+)",
     "Tipe tidak cocok: di sini Rust menuntut \\1 tetapi menemukan \\2. Ubah "
     "nilainya supaya tipenya sama, atau ubah tipe yang ditulis. Rust tidak "
     "mengonversi tipe secara otomatis."),
    (r"implicitly returns `\(\)` as its body has no tail or `return` expression",
     "Badan fungsi tidak mengembalikan nilai apa pun, padahal tipe "
     "kembaliannya sudah ditulis. Hapus titik koma di baris terakhir supaya "
     "nilainya dikembalikan, atau tambahkan return."),
    (r"(?:borrow of|use of) moved value: `(\w+)`",
     "Nilai '\\1' sudah dipindahkan (move) ke tempat lain, jadi tidak bisa "
     "dipakai lagi di sini. Di Rust nilai seperti String punya satu pemilik: "
     "pinjamkan dengan &\\1, atau salin dengan \\1.clone() kalau memang perlu "
     "dua."),
    (r"cannot assign twice to immutable variable `(\w+)`",
     "Variabel '\\1' dibuat tanpa mut, jadi nilainya tidak bisa diubah lagi. "
     "Tulis let mut \\1 = ... kalau nilainya memang harus berubah."),
    (r"cannot borrow `([^`]+)` as mutable, as it is not declared as mutable",
     "Variabel '\\1' tidak dideklarasikan mut, padahal operasi ini mengubah "
     "isinya. Tulis let mut \\1 = ... di deklarasinya."),
    (r"cannot borrow `([^`]+)` as mutable, as it is behind a `&` reference",
     "Nilai ini hanya dipinjam untuk dibaca (&), jadi isinya tidak boleh "
     "diubah. Ubah parameternya jadi &mut dan kirim dengan &mut saat memanggil."),
    (r"cannot borrow `(\w+)` as mutable more than once at a time",
     "Variabel '\\1' dipinjam sebagai &mut dua kali dalam waktu yang sama. "
     "Rust hanya mengizinkan satu peminjam yang bisa mengubah pada satu "
     "waktu: selesaikan pemakaian yang pertama dulu sebelum meminjam lagi."),
    (r"`(\w+)` does not live long enough",
     "Nilai '\\1' sudah dibuang (keluar dari blok tempat ia dibuat) padahal "
     "masih ada referensi yang menunjuk ke sana. Buat nilainya di blok yang "
     "lebih luas, atau kembalikan nilainya, bukan referensinya."),
    (r"no method named `(\w+)` found",
     "Tidak ada method bernama '\\1' untuk tipe itu. Periksa ejaannya, atau "
     "tipe nilainya memang bukan yang kamu kira."),
    (r"this (?:function|method) takes (\d+) arguments? but (\d+) arguments? "
     r"(?:was|were) supplied",
     "Fungsi menuntut \\1 argumen, tetapi dipanggil dengan \\2. Samakan "
     "jumlah argumen saat memanggil dengan parameter di definisinya."),
    (r"missing lifetime specifier",
     "Fungsi mengembalikan referensi (&), tapi Rust tidak tahu referensi itu "
     "dipinjam dari parameter yang mana. Tambahkan lifetime seperti <'a> pada "
     "nama fungsi dan 'a pada referensi yang saling terkait."),
    (r"error\[E0277\]: cannot add `([^`]+)` to `([^`]+)`",
     "Rust tidak bisa menjumlahkan \\1 dengan \\2 karena tipenya berbeda. "
     "Samakan tipenya dulu, misalnya ubah teks jadi angka dengan parse(), "
     "atau angka jadi teks dengan to_string()."),
    (r"`([^`]+)` doesn't implement `std::fmt::Display`",
     "Tipe \\1 belum punya cara menampilkan dirinya, jadi tidak bisa dicetak "
     "dengan {}. Cetak dengan {:?} setelah menambah #[derive(Debug)], atau "
     "implementasikan Display sendiri."),
    (r"can't compare `([^`]+)` with `([^`]+)`",
     "Rust tidak bisa membandingkan \\1 dengan \\2 karena tipenya berbeda. "
     "Bandingkan dua nilai yang sejenis."),
    (r"the type `(?:str|String)` cannot be indexed by",
     "Teks tidak bisa diambil hurufnya dengan s[0]. Pakai s.chars().nth(0) "
     "untuk huruf ke-n, atau potong dengan s[0..1] kalau yang dimaksud byte."),
    (r"error\[E0369\]",
     "Operator (+, ==, dan sejenisnya) dipakai pada tipe yang belum tahu "
     "caranya. Untuk == tambahkan #[derive(PartialEq)] di atas struct-nya; "
     "untuk + implementasikan trait std::ops::Add."),
    (r"non-exhaustive patterns: ([^\n]+?) not covered",
     "match belum mencakup semua kemungkinan: \\1 belum ditangani. Tambahkan "
     "cabangnya, atau cabang penampung _ => ... di akhir."),
    (r"no field `(\w+)` on type `([^`]+)`",
     "Tipe \\2 tidak punya field bernama '\\1'. Periksa ejaannya di definisi "
     "struct-nya."),
    (r"missing field `(\w+)` in initializer of `([^`]+)`",
     "Saat membuat \\2, field '\\1' belum diisi. Setiap field struct wajib "
     "diberi nilai."),
    (r"used binding `(\w+)` isn't initialized",
     "Variabel '\\1' dipakai sebelum diberi nilai. Beri nilai awal saat "
     "dibuat, misalnya let \\1 = 0;"),
    (r"`main` function not found",
     "Program Rust wajib punya fungsi fn main() { ... } sebagai titik mulai, "
     "dan fungsi itu tidak ditemukan."),
    (r"expected `;`, found `([^`]+)`",
     "Ada pernyataan yang lupa diakhiri titik koma (;), tepat sebelum '\\1'."),
    (r"this file contains an unclosed delimiter",
     "Ada kurung kurawal, kurung, atau kurung siku yang dibuka tapi tidak "
     "pernah ditutup. Hitung lagi pasangannya; Rust menandai pembuka yang "
     "belum punya penutup."),
    (r"unexpected closing delimiter: `(.)`",
     "Ada '\\1' penutup yang tidak punya pasangan pembuka."),
    (r"index out of bounds: the len is (\d+) but the index is (\d+)",
     "Program mengakses indeks \\2 padahal isinya cuma \\1 elemen. Indeks "
     "pertama 0 dan yang terakhir panjang - 1."),
    (r"attempt to (?:divide by zero|calculate the remainder with a divisor "
     r"of zero)",
     "Pembagian dengan nol. Periksa dulu apakah pembaginya nol."),
    (r"called `Option::unwrap\(\)` on a `None` value",
     "unwrap() dipanggil pada Option yang isinya None (kosong), jadi program "
     "panik. Tangani kasus kosongnya dengan match atau if let, atau pakai "
     "unwrap_or(nilai_cadangan)."),
    (r"called `Result::unwrap\(\)` on an `Err` value: ([^\n]+)",
     "unwrap() dipanggil pada Result yang berisi Err (\\1), jadi program "
     "panik. Tangani errornya dengan match atau if let. Untuk parse angka, "
     "Err berarti teksnya bukan angka yang sah."),

    # ----------------------------------------------------------------- PHP
    # PHP mencetak "Parse error:" dengan satu atau dua spasi sesudah titik dua
    # (log memakai dua), jadi jangkar yang memuat awalan itu memakai \s+.
    (r"Parse error:\s+Unclosed '(.)' on line (\d+)",
     "Tanda '\\1' yang dibuka di baris \\2 tidak pernah ditutup. Hitung lagi "
     "pasangan buka-tutupnya."),
    (r"Parse error:\s+Unmatched '(.)'",
     "Ada '\\1' penutup yang tidak punya pasangan pembuka."),
    (r"syntax error, unexpected [^\n]*?, expecting \",\" or \";\"",
     "Sepertinya ada baris sebelumnya yang lupa diakhiri titik koma (;), atau "
     "ada koma yang kurang di antara dua nilai. PHP menunjuk tempat ia baru "
     "sadar ada yang salah, biasanya satu baris sesudah kesalahannya."),
    (r"syntax error, unexpected token \"[^\"]*\", expecting end of file",
     "Ada kata atau tanda yang muncul di tempat yang tidak boleh. Biasanya "
     "ada kurung kurawal } yang kelebihan dan menutup blok terlalu awal, atau "
     "else tanpa if pasangannya. Hitung lagi pasangan { dan }."),
    (r"syntax error, unexpected token \"[^\"]*\", expecting \"([)\]}])\"",
     "PHP mengharapkan tanda \\1 di sini, jadi ada kurung buka yang belum "
     "ditutup. Hitung lagi pasangan kurungnya."),
    (r"syntax error, unexpected token \"([^\"]*)\"(?!,)",
     "PHP tidak mengira ada \"\\1\" di sini. Periksa baris itu dan baris "
     "sebelumnya: biasanya ada titik koma, kurung, atau nilai yang kurang, "
     "atau ekspresinya belum lengkap."),
    (r"syntax error, unexpected (?:variable|identifier|integer|float|"
     r"double-quoted string|single-quoted string) \"([^\"]*)\"",
     "PHP tidak mengira ada \"\\1\" di sini. Biasanya baris sebelumnya lupa "
     "diakhiri titik koma (;), atau ada koma, operator, atau tanda kutip yang "
     "kurang di antara dua nilai."),
    (r"syntax error, unexpected end of file(?!, expecting \",\" or \";\")",
     "File berakhir padahal masih ada yang belum ditutup: tanda kutip, "
     "kurung, atau kurung kurawal. Hitung lagi pasangan buka-tutupnya."),
    (r"Undefined variable \$(\w+)",
     "Variabel $\\1 dipakai sebelum diberi nilai. Di PHP variabel baru ada "
     "setelah diisi, dan huruf besar/kecil dibedakan ($nama dan $Nama itu "
     "berbeda). Periksa ejaannya."),
    (r"Call to undefined function ([^\s(]+)\(\)",
     "Fungsi '\\1' tidak dikenal. Periksa ejaan namanya, atau fungsi itu "
     "memang belum dibuat atau berasal dari ekstensi yang tidak terpasang."),
    (r"Call to undefined method (\w+)::(\w+)\(\)",
     "Kelas \\1 tidak punya method \\2(). Periksa ejaannya, atau method itu "
     "belum ditulis di kelasnya."),
    (r"Call to (private|protected) method (\w+)::(\w+)\(\)",
     "Method \\3() di kelas \\2 bersifat \\1, jadi tidak bisa dipanggil dari "
     "luar kelasnya. Ubah jadi public, atau panggil lewat method public lain."),
    (r"Call to a member function (\w+)\(\) on (\w+)",
     "Method \\1() dipanggil dari nilai \\2, padahal harus dari objek. "
     "Pastikan variabelnya sudah berisi objek (bukan null) sebelum dipanggil."),
    (r"Class \"([^\"]+)\" not found",
     "Kelas \"\\1\" tidak ditemukan. Periksa ejaan namanya, atau kelasnya "
     "belum didefinisikan di atas baris ini."),
    (r"Non-static method ([\w:]+)\(\) cannot be called statically",
     "Method \\1() bukan method static, jadi harus dipanggil lewat objek "
     "($objek->method()), bukan lewat nama kelas dengan ::."),
    (r"Cannot instantiate abstract class (\w+)",
     "Kelas \\1 abstract: ia cuma kerangka dan tidak bisa dibuat objeknya "
     "langsung. Buat kelas turunan yang melengkapinya, lalu buat objek dari "
     "turunan itu."),
    (r"Value of type (\w+) is not callable",
     "Nilai bertipe \\1 dipanggil seperti fungsi (dengan tanda kurung) "
     "padahal bukan fungsi. Periksa apakah variabelnya tertimpa nilai lain."),
    (r"Unsupported operand types: (\w+) (\S+) (\w+)",
     "Operator \\2 tidak bisa dipakai antara \\1 dan \\3. Hitungan butuh "
     "angka: ubah dulu isinya (misalnya dengan (int) atau intval()), dan "
     "periksa apakah salah satu sisinya array atau teks yang bukan angka."),
    (r"DivisionByZeroError: (?:Division|Modulo) by zero",
     "Pembagian atau sisa bagi dengan nol. Periksa dulu apakah pembaginya "
     "nol, misalnya dengan if ($pembagi != 0)."),
    (r"Too few arguments to function ([^\s(]+)\(\), (\d+) passed[^\n]*? and "
     r"(?:exactly|at least) (\d+) expected",
     "Fungsi \\1() dipanggil dengan \\2 argumen, padahal parameternya "
     "meminta \\3. Lengkapi argumen saat memanggil, atau beri nilai bawaan "
     "pada parameter di definisinya."),
    (r"(\w+)\(\): Argument #(\d+) \(\$(\w+)\) must be of type ([^,\n]+), "
     r"(\w+) given",
     "Fungsi \\1() meminta argumen $\\3 bertipe \\4, tapi yang dikirim bertipe "
     "\\5. Kirim nilai dengan tipe yang benar, atau ubah dulu dengan (int), "
     "(string), dan semacamnya."),
    (r"(\w+)\(\): Return value must be of type ([^,\n]+), (\w+) returned",
     "Fungsi \\1() dijanjikan mengembalikan \\2, tapi malah mengembalikan "
     "\\3. Samakan nilai di return dengan tipe yang ditulis."),
    (r"ValueError: (\w+)\(\): Argument #(\d+) \(\$(\w+)\)",
     "Fungsi \\1() menolak nilai yang dikirim untuk argumen $\\3 karena di "
     "luar batas yang diizinkan. Baca keterangan di pesan aslinya, lalu "
     "periksa nilai yang kamu kirim."),
    (r"Uncaught (\w*Exception)",
     "Ada exception (\\1) yang dilempar dengan throw tapi tidak ada catch "
     "yang menangkapnya, jadi program berhenti. Baca pesannya, lalu tangani "
     "dengan try/catch kalau kasusnya memang bisa diduga."),
    (r"Undefined array key (-?\d+|\"[^\"]*\")",
     "Array ini tidak punya kunci \\1, jadi PHP memberi null disertai "
     "peringatan. Periksa ejaan kuncinya, atau cek lebih dulu dengan isset() "
     "atau operator ??."),
    (r"Attempt to read property \"(\w+)\" on (\w+)",
     "Program membaca properti '\\1' dari nilai \\2, bukan dari objek. "
     "Pastikan variabelnya sudah berisi objek sebelum dipakai."),
    (r"Trying to access array offset on (?:value of type )?(\w+)",
     "Program membaca isi nilai bertipe \\1 dengan kurung siku [ ], padahal "
     "itu bukan array. Pastikan variabelnya sudah berisi array sebelum diakses."),
    (r"Uninitialized string offset (-?\d+)",
     "Indeks \\1 melewati panjang teks. Huruf pertama berindeks 0 dan yang "
     "terakhir panjang - 1."),
    (r"Undefined property: (\w+)::\$(\w+)",
     "Objek bertipe \\1 tidak punya properti '\\2'. Periksa ejaannya, atau "
     "properti itu belum dideklarasikan di kelasnya."),
    (r"Cannot access (private|protected) property (\w+)::\$(\w+)",
     "Properti \\3 di kelas \\2 bersifat \\1, jadi tidak bisa dibaca dari "
     "luar kelasnya. Tambahkan method getter yang public, atau ubah "
     "visibilitasnya kalau memang boleh."),
    (r"Cannot modify readonly property (\w+)::\$(\w+)",
     "Properti \\2 di kelas \\1 bertanda readonly: setelah diisi di "
     "constructor, nilainya tidak boleh diubah lagi. Buat objek baru kalau "
     "memang butuh nilai berbeda."),
    (r"Cannot redeclare (?:function )?(\w+)\(\)",
     "Fungsi '\\1' dibuat dua kali. Nama fungsi harus unik: hapus salah satu "
     "atau ganti namanya."),
    (r"Undefined constant \"(\w+)\"",
     "Konstanta '\\1' tidak dikenal. Kalau maksudmu teks, tulis dengan tanda "
     "kutip (\"\\1\"). Kalau konstanta, periksa ejaan dan define()-nya."),
    (r"Unhandled match case (\S+)",
     "Ekspresi match tidak punya cabang untuk nilai \\1. Tambahkan cabang "
     "untuk nilai itu, atau cabang penampung default => ... di akhir."),
    (r"Array to string conversion",
     "Array dicetak sebagai teks, hasilnya cuma kata 'Array'. Cetak isinya "
     "dengan print_r() atau var_dump(), atau loop dengan foreach."),
    (r"foreach\(\) argument must be of type array\|object, (\w+) given",
     "foreach butuh array atau objek, tapi yang diberikan bertipe \\1. "
     "Pastikan variabelnya benar-benar array sebelum di-loop."),
    (r"Failed to open stream: No such file or directory",
     "Berkas yang dibuka tidak ada di tempat yang disebut. Periksa nama dan "
     "letaknya; di aplikasi ini hanya berkas programmu sendiri yang tersedia."),

    # --------------------------------------------------------------- Kotlin
    # kotlinc K2 menulis pesannya dengan huruf kecil sesudah "error: " dan
    # kutip tunggal di sekitar nama.
    (r"unresolved reference '(\w+)' on receiver of type '([^']+)'",
     "Tipe \\2 tidak punya method atau properti '\\1'. Periksa ejaannya, atau "
     "tipe nilainya memang bukan yang kamu kira."),
    (r"unresolved reference '(\w+)'(?! on receiver)",
     "Nama '\\1' tidak dikenal. Periksa ejaan dan huruf besar/kecilnya, "
     "pastikan sudah dideklarasikan (val, var, atau fun), dan kalau berasal "
     "dari pustaka, pastikan sudah di-import."),
    (r"(?:initializer|return) type mismatch: expected '([^']+)', actual "
     r"'([^']+)'",
     "Nilai bertipe \\2 dimasukkan ke tempat yang menuntut \\1. Samakan "
     "tipenya, misalnya dengan toInt() atau toString(), atau ubah tipe yang "
     "ditulis."),
    (r"assignment type mismatch: actual type is '([^']+)', but '([^']+)' was "
     r"expected",
     "Variabel bertipe \\2 diisi dengan nilai bertipe \\1. Tipe variabel di "
     "Kotlin tetap setelah dibuat: samakan nilainya, atau deklarasikan "
     "variabelnya dengan tipe yang sesuai."),
    (r"argument type mismatch: actual type is '([^']+)', but '([^']+)' was "
     r"expected",
     "Argumen bertipe \\1 dikirim ke tempat yang menuntut \\2. Kirim nilai "
     "dengan tipe yang benar, atau ubah dulu tipenya (toInt(), toString(), "
     "dan sebagainya)."),
    (r"condition type mismatch: inferred type is '([^']+)' but 'Boolean' was "
     r"expected",
     "Kondisi if atau while harus bertipe Boolean, tapi yang ditulis bertipe "
     "\\1. Kotlin tidak menganggap angka sebagai benar atau salah: tulis "
     "perbandingannya, misalnya x != 0."),
    (r"'val' cannot be reassigned",
     "Variabel ini dibuat dengan val, jadi nilainya tidak bisa diisi ulang. "
     "Pakai var kalau nilainya memang harus berubah."),
    (r"only safe \(\?\.\) or non-null asserted \(!!\.\) calls are allowed on "
     r"a nullable receiver of type '([^']+)'",
     "Nilai bertipe \\1 bisa null, dan Kotlin menolak memanggil method atau "
     "propertinya langsung. Pakai ?. (panggilan aman), ?: (nilai cadangan), "
     "atau periksa dulu dengan if (x != null)."),
    (r"null cannot be a value of a non-null type '([^']+)'",
     "null tidak boleh dimasukkan ke tipe \\1. Tambahkan tanda tanya pada "
     "tipenya (\\1?) kalau nilainya memang boleh kosong."),
    (r"no value passed for parameter '(\w+)'",
     "Parameter '\\1' wajib diisi tapi tidak diberi nilai saat fungsi "
     "dipanggil. Lengkapi argumennya, atau beri nilai bawaan di definisi "
     "fungsi (\\1: Tipe = nilai)."),
    (r"too many arguments for '([^']+)'",
     "Fungsi dipanggil dengan argumen lebih banyak daripada parameternya "
     "(\\1). Kurangi argumennya, atau tambahkan parameter di definisinya."),
    (r"no parameter with name '(\w+)' found",
     "Fungsi tidak punya parameter bernama '\\1'. Periksa ejaan nama "
     "parameter di pemanggilnya."),
    (r"variable '(\w+)' must be initialized",
     "Variabel '\\1' dipakai sebelum diberi nilai. Beri nilai awal saat "
     "dideklarasikan, misalnya val \\1 = 0."),
    (r"this variable must either have an explicit type or be initialized",
     "Variabel tanpa nilai awal harus ditulis tipenya (val x: Int), karena "
     "Kotlin tidak bisa menebak tipenya."),
    (r"error: conflicting declarations",
     "Ada dua variabel atau fungsi dengan nama yang sama di lingkup yang "
     "sama. Hapus salah satunya, atau pakai nama lain."),
    (r"cannot create an instance of an abstract class",
     "Kelas ini abstract: ia cuma kerangka dan tidak bisa dibuat objeknya "
     "langsung. Buat kelas turunan yang melengkapinya, lalu buat objek dari "
     "turunan itu."),
    (r"cannot access '([^']+)': it is (private|protected) in '([^']+)'",
     "'\\1' bersifat \\2 di kelas \\3, jadi tidak bisa diakses dari luar. "
     "Ubah visibilitasnya, atau sediakan fungsi publik untuk mengaksesnya."),
    (r"syntax error: Expecting '([^']+)'",
     "Kotlin mengharapkan '\\1' di sini tapi tidak menemukannya. Hitung lagi "
     "pasangan kurung, kurung kurawal, dan tanda kutipnya."),
    (r"syntax error: Expecting an expression",
     "Ada tempat yang butuh nilai atau ekspresi tapi kosong, misalnya sesudah "
     "tanda = atau operator."),
    (r"UninitializedPropertyAccessException: lateinit property (\w+) has not "
     r"been initialized",
     "Properti lateinit '\\1' dibaca sebelum diisi. Isi dulu (misalnya di "
     "init atau constructor), atau pakai tipe nullable dengan nilai awal null."),
    (r"NullPointerException.*?\bat MainKt",
     "Program memakai nilai null lewat !! (atau dari kode Java). Hindari !!: "
     "pakai ?. (panggilan aman) atau ?: (nilai cadangan), atau periksa dulu "
     "dengan if (x != null)."),
    (r"\bIndexOutOfBoundsException: Index (\d+) out of bounds for length "
     r"(\d+).*?\bat MainKt",
     "Program mengakses indeks \\1 padahal isinya cuma \\2 elemen. Indeks "
     "pertama 0 dan yang terakhir size - 1. getOrNull(indeks) mengembalikan "
     "null alih-alih melempar error."),
    (r"NoSuchElementException.*?\bat MainKt",
     "first(), last(), atau single() dipanggil pada koleksi yang kosong atau "
     "tidak punya elemen yang cocok. Periksa isinya dulu, atau pakai "
     "firstOrNull() yang mengembalikan null."),
    (r"ClassCastException: class (\S+) cannot be cast to class (\S+).*?"
     r"\bat MainKt",
     "Objek bertipe \\1 dipaksa jadi \\2 dengan as, padahal tidak bisa. "
     "Periksa tipenya dulu dengan is, atau pakai as? yang mengembalikan null "
     "alih-alih melempar error."),
    (r"Illegal(Argument|State)Exception.*?\bat MainKt",
     "require(), check(), atau checkNotNull() melempar Illegal\\1Exception "
     "karena syarat yang dipasang di kode tidak terpenuhi. Baca pesan "
     "sesudah titik dua untuk tahu syarat mana yang dilanggar."),
    (r"StackOverflowError.*?\bat MainKt",
     "Fungsi memanggil dirinya sendiri terus-menerus sampai tumpukan panggilan "
     "penuh. Rekursi wajib punya kondisi berhenti, dan tiap panggilan harus "
     "mendekatinya."),

    # ----------------------------------------------------------- TypeScript
    # tsc menaruh kode di tiap pesan ("error TS2304"), dan semua pola di sini
    # berjangkar padanya: "Cannot find module" polos juga muncul di Node saat
    # runtime, dan itu bukan urusan bagian ini.
    (r"error TS1005: '([^']+)' expected",
     "TypeScript mengharapkan '\\1' di sini, tapi tidak ada. Periksa baris "
     "itu dan baris sebelumnya: biasanya ada koma, kurung, kurung kurawal, "
     "atau titik koma yang kurang."),
    (r"error TS1109: Expression expected",
     "Ada tempat yang butuh nilai atau ekspresi tapi kosong, misalnya "
     "sesudah tanda = atau operator."),
    (r"error TS1128: Declaration or statement expected",
     "Ada kode atau tanda yang tidak pada tempatnya, sering kurung kurawal } "
     "yang kelebihan atau pernyataan yang jatuh di luar fungsi."),
    (r"error TS1002: Unterminated string literal",
     "Ada teks yang tanda kutipnya belum ditutup."),
    (r"error TS1308: 'await' expressions are only allowed within async",
     "await hanya boleh dipakai di dalam fungsi async. Tambahkan kata async "
     "di depan fungsinya."),
    (r"error TS2304: Cannot find name '([^']+)'",
     "Nama '\\1' tidak dikenal. Periksa ejaan dan huruf besar/kecilnya, atau "
     "pastikan variabel, fungsi, atau tipenya sudah dideklarasikan sebelum "
     "dipakai."),
    (r"error TS2307: Cannot find module '([^']+)'",
     "Modul '\\1' tidak ditemukan. Periksa ejaan jalurnya; di aplikasi ini "
     "hanya satu berkas yang berjalan dan paket dari luar tidak terpasang."),
    (r"error TS2322: Type '([^']+)' is not assignable to type '([^']+)'",
     "Nilai bertipe \\1 dimasukkan ke tempat yang menuntut \\2. Samakan "
     "tipenya: ubah nilainya (misalnya Number(teks) atau String(angka)), "
     "atau ubah tipe yang ditulis di deklarasinya."),
    (r"error TS2345: Argument of type '([^']+)' is not assignable to "
     r"parameter of type '([^']+)'",
     "Fungsi dipanggil dengan argumen bertipe \\1, padahal parameternya "
     "menuntut \\2. Kirim nilai dengan tipe yang benar, atau ubah dulu "
     "tipenya."),
    (r"error TS2554: Expected (\d+(?:-\d+)?) arguments?, but got (\d+)",
     "Fungsi dipanggil dengan \\2 argumen, padahal parameternya \\1. Samakan "
     "jumlah argumen saat memanggil dengan definisinya."),
    (r"error TS2551: Property '([^']+)' does not exist on type '[^']+'\. "
     r"Did you mean '([^']+)'\?",
     "Properti '\\1' tidak ada. Mungkin maksudmu '\\2'; periksa ejaannya, "
     "termasuk huruf besar/kecilnya."),
    (r"error TS2339: Property '([^']+)' does not exist on type '([^']+)'",
     "Tipe \\2 tidak punya properti atau method '\\1'. Periksa ejaannya, atau "
     "tipe nilainya memang bukan yang kamu kira."),
    (r"error TS2353: Object literal may only specify known properties, and "
     r"'([^']+)' does not exist in type '([^']+)'",
     "Properti '\\1' tidak ada di tipe \\2, jadi tidak boleh ditulis di objek "
     "ini. Periksa ejaannya, atau tambahkan propertinya ke tipe."),
    (r"error TS2741: Property '([^']+)' is missing in type '[^']+' but "
     r"required in type '([^']+)'",
     "Objek ini belum punya properti '\\1' yang wajib ada menurut tipe \\2. "
     "Tambahkan propertinya, atau jadikan opsional di tipenya dengan tanda ?."),
    (r"error TS7006: Parameter '([^']+)' implicitly has an 'any' type",
     "Parameter '\\1' belum diberi tipe, dan mode ketat (strict) melarang "
     "tipe any yang diam-diam. Tulis tipenya, misalnya (\\1: number)."),
    (r"error TS7053: Element implicitly has an 'any' type because expression "
     r"of type '([^']+)' can't be used to index",
     "Kunci \\1 tidak dikenal oleh tipe objek ini, jadi TypeScript tidak tahu "
     "tipe hasilnya. Pakai kunci yang memang ada di tipenya, atau beri tipe "
     "objek yang mengizinkan kunci lain, misalnya Record<string, number>."),
    (r"error TS\d+: '([^']+)' is possibly '(null|undefined)'",
     "'\\1' bisa berisi \\2, dan TypeScript menolak memakainya langsung. "
     "Periksa dulu dengan if (\\1), atau pakai ?. (misalnya \\1?.length)."),
    (r"error TS2588: Cannot assign to '([^']+)' because it is a constant",
     "'\\1' dibuat dengan const, jadi tidak bisa diisi ulang. Pakai let "
     "kalau nilainya memang harus berubah."),
    (r"error TS2540: Cannot assign to '([^']+)' because it is a read-only "
     r"property",
     "Properti '\\1' bertanda readonly, jadi tidak bisa diisi ulang setelah "
     "objeknya dibuat. Hapus readonly dari tipenya kalau nilainya memang "
     "harus berubah."),
    (r"error TS2448: Block-scoped variable '([^']+)' used before its "
     r"declaration",
     "Variabel '\\1' dipakai sebelum dideklarasikan. Pindahkan deklarasi "
     "let atau const-nya ke atas baris yang memakainya."),
    (r"error TS2454: Variable '([^']+)' is used before being assigned",
     "Variabel '\\1' dipakai sebelum diberi nilai. Beri nilai awal saat "
     "dideklarasikan."),
    (r"error TS2451: Cannot redeclare block-scoped variable '([^']+)'",
     "Variabel '\\1' dideklarasikan dua kali di lingkup yang sama. Hapus "
     "salah satu let atau const-nya, atau pakai nama lain."),
    (r"error TS2355: A function whose declared type is neither 'undefined', "
     r"'void', nor 'any' must return a value",
     "Fungsi punya tipe kembalian, tapi badannya tidak mengembalikan nilai "
     "apa pun. Tambahkan return, atau ubah tipe kembaliannya jadi void."),
    (r"error TS2366: Function lacks ending return statement",
     "Ada jalur di dalam fungsi yang berakhir tanpa return, padahal tipe "
     "kembaliannya sudah dijanjikan. Pastikan semua cabang if dan else "
     "mengembalikan nilai."),
    (r"error TS2349: This expression is not callable",
     "Nilai ini dipanggil seperti fungsi (dengan tanda kurung) padahal bukan "
     "fungsi. Periksa apakah variabelnya tertimpa angka atau teks, atau "
     "ejaan nama fungsinya."),
    (r"error TS236[23]: The (?:left|right)-hand side of an arithmetic "
     r"operation must be of type",
     "Salah satu sisi operator aritmatika bukan angka, misalnya teks. Ubah "
     "dulu nilainya jadi angka dengan Number(...)."),
    (r"error TS2367: This comparison appears to be unintentional because the "
     r"types '([^']+)' and '([^']+)' have no overlap",
     "Perbandingan ini tidak mungkin pernah benar: tipe \\1 dan \\2 tidak "
     "punya nilai yang sama. Samakan tipe yang dibandingkan, atau periksa "
     "apakah salah satu sisinya keliru."),
    (r"error TS2564: Property '([^']+)' has no initializer and is not "
     r"definitely assigned in the constructor",
     "Properti '\\1' di kelas belum diberi nilai awal dan tidak diisi di "
     "constructor. Beri nilai awal, isi di constructor, atau tandai opsional "
     "(\\1?) kalau boleh kosong."),
    (r"error TS2420: Class '([^']+)' incorrectly implements interface "
     r"'([^']+)'",
     "Kelas \\1 belum memenuhi isi interface \\2. Baca baris di bawahnya "
     "untuk tahu properti atau method mana yang kurang."),
    (r"error TS2769: No overload matches this call",
     "Fungsi ini punya beberapa bentuk pemanggilan, dan argumenmu tidak cocok "
     "dengan satu pun. Baca baris di bawahnya: TypeScript menyebut bentuk "
     "terakhir yang dicoba beserta tipe yang diharapkan."),

    # ------------------------------------------------------------------- C#
    # Pesan kompilasi diawali "error CSxxxx:"; pesan runtime di bagian
    # ".NET" di bawahnya dipakai bersama Visual Basic.
    (r"The name '([^']+)' does not exist in the current context",
     "Nama '\\1' tidak dikenal di sini. Periksa ejaan dan huruf besar/"
     "kecilnya (C# membedakannya), dan pastikan variabelnya sudah "
     "dideklarasikan sebelum dipakai serta masih berada di dalam bloknya."),
    (r"error CS1002: ; expected",
     "Ada pernyataan yang lupa diakhiri titik koma (;)."),
    (r"error CS1026: \) expected",
     "Ada kurung buka ( yang belum ditutup. Hitung lagi pasangan ( dan )."),
    (r"error CS1513: \} expected",
     "Ada kurung kurawal { yang belum ditutup. Hitung lagi pasangan { dan }."),
    (r"error CS1003: Syntax error, '([^']+)' expected",
     "C# mengharapkan '\\1' di sini tapi tidak menemukannya. Periksa baris "
     "itu dan baris sebelumnya: sering ada titik koma, koma, atau kurung "
     "yang kurang."),
    (r"error CS1001: Identifier expected",
     "C# menunggu sebuah nama di sini. Nama variabel tidak boleh diawali "
     "angka dan tidak boleh memakai kata kunci seperti if atau class."),
    (r"error CS1022: Type or namespace definition, or end-of-file expected",
     "Ada kode atau tanda yang tidak pada tempatnya di luar kelas, sering "
     "kurung kurawal } yang kelebihan. Hitung lagi pasangan { dan }."),
    (r"Cannot implicitly convert type '([^']+)' to '([^']+)'\. An explicit "
     r"conversion exists",
     "Nilai bertipe \\1 tidak otomatis menjadi \\2 karena sebagian datanya "
     "bisa hilang. Tulis konversinya sendiri, misalnya cast (\\2)nilai atau "
     "Convert.To...()."),
    (r"Cannot implicitly convert type '([^']+)' to '([^']+)'(?!\. An explicit)",
     "Nilai bertipe \\1 dimasukkan ke tempat yang menuntut \\2, dan C# tidak "
     "mengubahnya otomatis. Samakan tipenya, atau konversi dulu, misalnya "
     "int.Parse(teks) untuk teks ke angka dan angka.ToString() untuk "
     "sebaliknya."),
    (r"The type or namespace name '([^']+)' could not be found",
     "Tipe atau namespace '\\1' tidak dikenal. Periksa ejaannya, atau "
     "tambahkan using untuk namespace yang memuatnya di baris paling atas."),
    (r"'([^']+)' does not contain a definition for '([^']+)'",
     "Tipe \\1 tidak punya method atau properti '\\2'. Periksa ejaannya "
     "(huruf besar/kecil berpengaruh), atau tipe nilainya memang bukan yang "
     "kamu kira."),
    (r"Use of unassigned local variable '([^']+)'",
     "Variabel '\\1' dipakai sebelum diberi nilai. Beri nilai awal saat "
     "dideklarasikan, misalnya \\1 = 0."),
    (r"There is no argument given that corresponds to the required parameter "
     r"'([^']+)' of '([^']+)'",
     "Pemanggilan \\2 belum memberi nilai untuk parameter '\\1'. Lengkapi "
     "argumennya, atau beri nilai bawaan pada parameter di definisinya."),
    (r"Argument (\d+): cannot convert from '([^']+)' to '([^']+)'",
     "Argumen ke-\\1 bertipe \\2, padahal parameternya menuntut \\3. Kirim "
     "nilai dengan tipe yang benar, atau konversi dulu."),
    (r"'([^']+)': not all code paths return a value",
     "Method \\1 punya tipe kembalian, tapi ada jalur yang berakhir tanpa "
     "return. Pastikan semua cabang if dan else mengembalikan nilai."),
    (r"A local variable or function named '([^']+)' is already defined in "
     r"this scope",
     "Variabel '\\1' dideklarasikan dua kali di lingkup yang sama. Hapus "
     "salah satu deklarasinya, atau pakai nama lain. Untuk mengubah nilai "
     "cukup tulis \\1 = nilai tanpa tipe di depannya."),
    (r"A local or parameter named '([^']+)' cannot be declared in this scope",
     "Nama '\\1' sudah dipakai oleh variabel di blok yang membungkus blok "
     "ini, dan C# tidak mengizinkan nama yang sama di blok bersarang. Pakai "
     "nama lain, atau hapus tipe di depannya kalau maksudmu mengubah nilai."),
    (r"An object reference is required for the non-static field, method, or "
     r"property '([^']+)'",
     "'\\1' milik objek, tapi dipakai dari method static tanpa objek. Buat "
     "objeknya dulu dengan new, atau jadikan anggotanya static."),
    (r"Operator '([^']+)' cannot be applied to operands of type '([^']+)' "
     r"and '([^']+)'",
     "Operator \\1 tidak bisa dipakai antara tipe \\2 dan \\3. Samakan "
     "tipenya dulu, dan periksa operator yang kamu maksud (= untuk mengisi, "
     "== untuk membandingkan)."),
    (r"'([^']+)' is inaccessible due to its protection level",
     "'\\1' bersifat private atau protected, jadi tidak bisa diakses dari "
     "luar kelasnya. Ubah jadi public, atau sediakan method atau properti "
     "public untuk mengaksesnya."),
    (r"Program does not contain a static 'Main' method",
     "Program tidak punya titik mulai. Tulis method static void Main() di "
     "dalam sebuah kelas, atau tulis kodenya langsung di berkas tanpa kelas."),
    (r"A readonly field cannot be assigned to",
     "Field readonly hanya boleh diisi saat dideklarasikan atau di "
     "constructor. Hapus readonly kalau nilainya memang harus berubah."),
    (r"Cannot create an instance of the abstract type or interface '([^']+)'",
     "'\\1' abstract atau interface: ia cuma kerangka dan tidak bisa dibuat "
     "objeknya langsung. Buat kelas turunan yang melengkapinya, lalu buat "
     "objek dari kelas itu."),
    (r"The left-hand side of an assignment must be a variable, property or "
     r"indexer",
     "Sisi kiri tanda = harus berupa variabel. Nilai const dan hasil "
     "perhitungan tidak bisa diisi; ubah const jadi variabel biasa kalau "
     "nilainya memang harus berubah."),
    (r"Since '([^']+)' returns void, a return keyword must not be followed by",
     "Method '\\1' bertipe void, jadi tidak boleh mengembalikan nilai. Ganti "
     "void dengan tipe kembaliannya (misalnya int), atau hapus nilai di "
     "sebelah return."),

    # ---------------------------------------------------------- Visual Basic
    # Kode galat VB berawalan BC. Pola umum berjangkar pada kodenya supaya
    # tidak menelan pesan bahasa lain yang kebetulan memuat "is not declared".
    (r"error BC30451: '([^']+)' is not declared",
     "Nama '\\1' tidak dikenal di sini. Periksa ejaannya, dan pastikan "
     "variabelnya sudah dideklarasikan dengan Dim sebelum dipakai serta "
     "masih berada di Sub atau Function yang sama."),
    (r"Option Strict On disallows implicit conversions from '([^']+)' to "
     r"'([^']+)'",
     "Nilai bertipe \\1 dimasukkan ke tempat yang menuntut \\2, dan Option "
     "Strict On melarang konversi otomatis. Tulis konversinya sendiri, "
     "misalnya CInt(...), CDbl(...), atau .ToString()."),
    (r"error BC\d+: '([^']+)' expected",
     "VB mengharapkan '\\1' di sini tapi tidak menemukannya. Hitung lagi "
     "pasangan pembuka dan penutupnya (Sub dan End Sub, If dan End If, "
     "kurung)."),
    (r"error BC\d+: '(\w+)' must end with a matching '([^']+)'",
     "Blok \\1 belum ditutup: tambahkan \\2 di akhir blok itu."),
    (r"error BC\d+: '([^']+)' must be preceded by a matching '([^']+)'",
     "\\1 muncul tanpa pasangannya: ia harus didahului \\2 di atasnya. "
     "Biasanya ada baris pembuka yang terhapus, atau penutupnya kelebihan."),
    (r"error BC30491: Expression does not produce a value",
     "Ada pemanggilan Sub (yang tidak mengembalikan nilai) dipakai seolah "
     "menghasilkan nilai, atau ekspresi yang belum lengkap di baris itu. "
     "Ubah Sub jadi Function kalau memang perlu mengembalikan nilai."),
    (r"error BC30456: '([^']+)' is not a member of '([^']+)'",
     "Tipe \\2 tidak punya anggota bernama '\\1'. Periksa ejaannya, atau "
     "tipe nilainya memang bukan yang kamu kira."),
    (r"error BC30002: Type '([^']+)' is not defined",
     "Tipe '\\1' tidak dikenal. Periksa ejaannya, atau tambahkan Imports "
     "untuk namespace yang memuatnya."),
    (r"error BC30455: Argument not specified for parameter '([^']+)'",
     "Pemanggilan belum memberi nilai untuk parameter '\\1'. Lengkapi "
     "argumennya, atau jadikan parameternya Optional dengan nilai bawaan."),
    (r"error BC30057: Too many arguments to '([^']+)'",
     "Pemanggilan memberi argumen lebih banyak daripada parameter yang ada di "
     "'\\1'. Kurangi argumennya, atau tambahkan parameter di definisinya."),
    (r"error BC30288: Local variable '([^']+)' is already declared in the "
     r"current block",
     "Variabel '\\1' dideklarasikan dua kali di blok yang sama. Hapus salah "
     "satu Dim-nya, atau pakai nama lain. Untuk mengubah nilai cukup tulis "
     "\\1 = nilai tanpa Dim."),
    (r"error BC30389: '([^']+)' is not accessible in this context because it "
     r"is '(\w+)'",
     "'\\1' bersifat \\2, jadi tidak bisa diakses dari luar kelasnya. Ubah "
     "jadi Public, atau sediakan Property atau fungsi Public untuk "
     "mengaksesnya."),
    (r"error BC30800: Method arguments must be enclosed in parentheses",
     "Pemanggilan Sub atau Function di VB.NET harus memakai kurung: tulis "
     "Console.WriteLine(\"a\"), bukan Console.WriteLine \"a\"."),
    (r"error BC30182: Type expected",
     "VB menunggu nama tipe sesudah As. Tulis misalnya Dim x As Integer."),
    (r"error BC30074: Constant cannot be the target of an assignment",
     "Nilai Const tidak bisa diisi ulang. Pakai Dim kalau nilainya memang "
     "harus berubah."),
    (r"error BC30203: Identifier expected",
     "VB menunggu sebuah nama di sini. Nama variabel tidak boleh diawali "
     "angka dan tidak boleh memakai kata kunci seperti If atau Class."),
    (r"error BC30205: End of statement expected",
     "Ada sisa teks di akhir baris. Di VB satu pernyataan ditulis satu "
     "baris; periksa apakah ada operator atau koma yang kurang."),
    (r"error BC30188: Declaration expected",
     "Di dalam Module atau Class hanya boleh ada deklarasi (Sub, Function, "
     "Dim). Pernyataan seperti Console.WriteLine harus berada di dalam Sub "
     "atau Function."),

    # ------------------------------------------- .NET (C# dan Visual Basic)
    (r"Conversion from string \"([^\"]*)\" to type '([^']+)' is not valid",
     "Teks \"\\1\" tidak bisa diubah jadi \\2 karena bukan nilai yang sah. "
     "Periksa isinya, atau pakai \\2.TryParse yang tidak melempar error."),
    (r"NullReferenceException",
     "Program memakai objek yang isinya null (belum diisi). Periksa dulu "
     "dengan If x IsNot Nothing atau if (x != null), atau pakai ?. supaya "
     "null dilewati."),
    (r"IndexOutOfRangeException",
     "Indeks array di luar jangkauan. Ingat indeks pertama adalah 0 dan yang "
     "terakhir adalah Length - 1."),
    (r"DivideByZeroException",
     "Pembagian bilangan bulat dengan nol. Periksa dulu apakah pembaginya "
     "nol."),
    (r"FormatException: The input string '([^']*)' was not in a correct "
     r"format",
     "Teks '\\1' tidak bisa diubah jadi angka karena bukan angka yang sah. "
     "Periksa isinya (spasi atau huruf nyasar), atau pakai TryParse yang "
     "tidak melempar error."),
    (r"InvalidCastException: Unable to cast object of type '([^']+)' to type "
     r"'([^']+)'",
     "Objek bertipe \\1 dipaksa jadi \\2, padahal tidak bisa. Periksa tipe "
     "nilai aslinya sebelum konversi."),
    (r"KeyNotFoundException: The given key '([^']*)' was not present in the "
     r"dictionary",
     "Kunci '\\1' tidak ada di Dictionary. Periksa ejaannya, atau cek dulu "
     "dengan ContainsKey() atau TryGetValue()."),
    (r"ArgumentOutOfRangeException: Index was out of range",
     "Indeks di luar jangkauan koleksi (List atau sejenisnya). Ingat indeks "
     "pertama 0 dan yang terakhir Count - 1."),
    (r"InvalidOperationException: Sequence contains no elements",
     "First(), Last(), atau Max() dipanggil pada koleksi yang kosong. "
     "Periksa dulu isinya dengan Any(), atau pakai FirstOrDefault()."),
    (r"ArgumentNullException: Value cannot be null\. \(Parameter '([^']*)'\)",
     "Nilai null dikirim ke parameter '\\1' padahal tidak boleh. Periksa asal "
     "nilainya sebelum dikirim."),
    (r"OverflowException: Arithmetic operation resulted in an overflow",
     "Hasil hitungan melebihi batas tipe datanya (Byte maksimum 255, Integer "
     "sekitar 2 miliar). Pakai tipe yang lebih besar, misalnya Long."),
]

_TERKOMPILASI = [(re.compile(p, re.IGNORECASE | re.DOTALL), pesan) for p, pesan in POLA]


def terjemahkan(galat, maks=3):
    """Return daftar penjelasan berbahasa Indonesia untuk sebuah pesan error.

    Kosong kalau tidak ada pola yang cocok -- pemanggil tetap wajib
    menampilkan pesan aslinya.
    """
    if not galat or not galat.strip():
        return []

    keluar = []
    for pola, pesan in _TERKOMPILASI:
        cocok = pola.search(galat)
        if not cocok:
            continue
        try:
            teks = pola.sub(pesan, cocok.group(0), count=1)
        except (re.error, IndexError):
            teks = pesan
        teks = " ".join(teks.split())
        if teks not in keluar:
            keluar.append(teks)
        if len(keluar) >= maks:
            break
    return keluar


_POLA_PATH = re.compile(r"(?:[^\s:,\"']*[/\\])?belajar-[A-Za-z0-9_]+[/\\]([^\s:,\"']+)")

# Nomor BARIS saja yang boleh digeser. `prog.c:5:5` berisi baris 5 kolom 5 --
# menggeser keduanya akan mengubah kolom jadi angka yang tidak ada artinya.
_POLA_BARIS_BERKAS = re.compile(r"([\w./\\-]+\.\w+:)(\d+)")
_POLA_KATA_LINE = re.compile(r"(\bline )(\d+)")


def rapikan(galat, nama_berkas="", baris_setup=0):
    """Bersihkan pesan error mentah supaya cocok dengan berkas milik pelajar.

    - Path direktori sementara diganti nama berkas kerja pelajar.
    - Nomor baris digeser mundur sebanyak baris `setup` yang ditempel runner,
      sehingga "baris 15" menunjuk baris 1 di berkas pelajar yang isinya
      memang cuma satu baris.
    """
    if not galat:
        return galat

    teks = _POLA_PATH.sub(lambda m: nama_berkas or m.group(1), galat)
    if baris_setup <= 0:
        return teks

    def geser(m):
        baru = int(m.group(2)) - baris_setup
        if baru < 1:
            return f"{m.group(1)}[bagian KONDISI AWAL]"
        return f"{m.group(1)}{baru}"

    teks = _POLA_BARIS_BERKAS.sub(geser, teks)
    return _POLA_KATA_LINE.sub(geser, teks)


def ringkas(galat, maks_baris=12):
    """Ambil bagian paling berguna dari pesan error yang panjang."""
    baris = [b for b in (galat or "").splitlines() if b.strip()]
    if len(baris) <= maks_baris:
        return baris
    # Traceback Python paling berguna di bagian akhir; keluaran kompiler di awal.
    if any("Traceback" in b for b in baris[:3]):
        return ["...(bagian awal disingkat)"] + baris[-(maks_baris - 1):]
    return baris[:maks_baris - 1] + [f"...({len(baris) - maks_baris + 1} baris lagi)"]
