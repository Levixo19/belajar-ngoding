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

Importir: exercises.py (tampilan hasil uji & mode "jalankan saja").
"""

import re

# (pola, penjelasan) -- diurutkan dari yang paling spesifik.
# Penjelasan boleh memakai \1, \2 untuk grup tangkapan pola.
POLA = [
    # ----------------------------------------------------------------- Java
    (r"';' expected",
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
    (r"NullPointerException",
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
    (r"NoSuchElementException",
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
    (r"SyntaxError: invalid syntax",
     "Ada kesalahan penulisan. Tersering: lupa titik dua (:) di akhir baris "
     "if/for/while/def, atau kurung yang belum ditutup."),
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
