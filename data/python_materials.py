PYTHON_MATERIALS = [
    {
        "title": "1. Pengenalan Python & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu Python?",
                    "  - Bahasa pemrograman tingkat tinggi, mudah dibaca, serbaguna.",
                    "  - Dibuat oleh Guido van Rossum, dirilis pertama 1991.",
                    "  - Bersifat interpreted (dijalankan langsung, tanpa kompilasi manual).",
                    "  - Dipakai untuk: web (Django/Flask), data science, AI/ML,",
                    "    automation/scripting, DevOps, hingga game sederhana.",
                    "",
                    "Kenapa Python cocok untuk pemula:",
                    "  - Sintaks mirip bahasa Inggris, minim tanda kurung kurawal.",
                    "  - Komunitas besar, banyak library siap pakai (PyPI).",
                    "  - 'Batteries included' - banyak fitur sudah tersedia bawaan.",
                    "",
                    "Instalasi:",
                    "  - Download dari https://python.org (pilih versi 3.x, BUKAN 2.x).",
                    "  - Cek instalasi: python3 --version  (atau python --version di Windows)",
                    "  - Package manager bawaan: pip",
                    "",
                    "Menjalankan program Python:",
                    "  1. Buat file bernama program.py",
                    "  2. Tulis kodenya (lihat contoh di bawah)",
                    "  3. Jalankan:  python3 program.py",
                    "",
                    "Python juga punya mode interaktif (REPL):",
                    "  Ketik 'python3' di terminal, langsung bisa coba kode baris per baris.",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """print("Halo Dunia!")
print("Aku sedang belajar Python.")"""
            },
            {
                "body": [
                    "Penjelasan:",
                    "  print(...)  -> fungsi bawaan untuk menampilkan teks ke layar.",
                    "  TIDAK butuh class atau method main seperti Java/C - Python",
                    "  bisa langsung eksekusi baris demi baris dari atas ke bawah.",
                    "",
                    "Aturan penting sintaks Python:",
                    "  1. TIDAK pakai titik koma (;) di akhir baris (opsional, jarang dipakai).",
                    "  2. TIDAK pakai { } untuk blok kode - pakai INDENTASI (spasi/tab).",
                    "  3. Indentasi harus KONSISTEN (disarankan 4 spasi), karena",
                    "     menentukan blok mana yang termasuk suatu kondisi/fungsi.",
                    "  4. Komentar satu baris pakai tanda pagar (#).",
                    "  5. Case-sensitive: Nama beda dengan nama.",
                    "",
                    "  # ini komentar satu baris",
                    "  \"\"\"ini komentar/docstring banyak baris\"\"\"",
                    "",
                    "Satu pengecualian untuk aturan nomor 4. Kalau baris PERTAMA sebuah",
                    "berkas berbunyi:",
                    "",
                    "  #!/usr/bin/env python3",
                    "",
                    "baris itu BUKAN komentar biasa meski diawali #. Namanya shebang, dan",
                    "yang membacanya bukan Python melainkan sistem operasi - isinya memberi",
                    "tahu program mana yang harus menjalankan berkas ini, supaya berkasnya",
                    "bisa dipanggil langsung sebagai ./skrip.py tanpa mengetik python3 di",
                    "depannya. Jadi jangan ikut menghapusnya waktu merapikan komentar.",
                    "Cara memakainya dibahas tuntas di materi Program Baris Perintah:",
                    "sys, os & argparse.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "Python bersifat dynamically typed: tipe data variabel",
                    "ditentukan OTOMATIS dari nilainya, tidak perlu dideklarasikan.",
                    "",
                    "Tipe data dasar (built-in):",
                    "  int      -> bilangan bulat            umur = 20",
                    "  float    -> bilangan desimal           harga = 15000.5",
                    "  str      -> teks/string                nama = \"Budi\"",
                    "  bool     -> True atau False             lulus = True",
                    "  complex  -> bilangan kompleks (jarang)  z = 2 + 3j",
                    "  NoneType -> representasi 'tidak ada nilai'  kosong = None",
                    "",
                    "Mengecek tipe data:",
                    "  type(umur)     -> <class 'int'>",
                    "  isinstance(umur, int)  -> True",
                ]
            },
            {
                "heading": "Contoh deklarasi variabel",
                "code": """umur = 20
harga = 15000.50
nama = "Budi"
lulus = True
data_kosong = None

print(type(umur))     # <class 'int'>
print(type(harga))    # <class 'float'>
print(type(nama))     # <class 'str'>

# Multiple assignment sekaligus
x, y, z = 1, 2, 3
print(x, y, z)        # 1 2 3

# Semua variabel bernilai sama
a = b = c = 0
print(a, b, c)        # 0 0 0"""
            },
            {
                "body": [
                    "Aturan penamaan variabel:",
                    "  1. Boleh huruf, angka, underscore (_). Tidak boleh diawali angka.",
                    "  2. Konvensi Python: snake_case untuk variabel/fungsi.",
                    "     jumlah_mahasiswa, bukan JumlahMahasiswa (itu gaya class).",
                    "  3. Konstanta biasanya ditulis UPPERCASE (hanya konvensi,",
                    "     Python TIDAK punya keyword 'final' seperti Java):",
                    "     PI = 3.14159",
                    "",
                    "Konversi tipe data (type casting):",
                    "  int(\"10\")     -> 10        (str ke int)",
                    "  float(\"3.5\")  -> 3.5       (str ke float)",
                    "  str(100)      -> \"100\"     (int ke str)",
                    "  int(3.99)     -> 3         (float ke int, dibulatkan ke bawah)",
                    "",
                    "f-string (cara modern gabung teks & variabel, Python 3.6+):",
                    "  nama = \"Andi\"; umur = 20",
                    "  print(f\"Nama saya {nama}, umur {umur} tahun\")",
                    "  print(f\"Tahun depan jadi {umur + 1} tahun\")  # bisa ekspresi",
                ]
            },
        ],
    },
    {
        "title": "3. Masukan, Keluaran & Modul Bawaan",
        "sections": [
            {
                "body": [
                    "Sampai sini semua contoh hanya MENCETAK nilai yang sudah ditulis di kodenya.",
                    "Program sungguhan punya dua sisi: MASUKAN (data dari luar) dan KELUARAN",
                    "(hasil yang ditampilkan). Materi ini membahas keduanya sampai tuntas, plus",
                    "dua hal yang muncul di hampir setiap berkas Python: escape sequence dan import.",
                    "",
                    "ESCAPE SEQUENCE: KARAKTER YANG TIDAK BISA DIKETIK LANGSUNG",
                    "",
                    "Bagaimana cara menaruh karakter 'pindah baris' di dalam sebuah string? Menekan",
                    "Enter di tengah tanda kutip tidak bisa - string biasa harus selesai di baris",
                    "yang sama. Jalan keluarnya: backslash (\\) sebagai penanda yang berarti",
                    "'huruf sesudahku punya arti khusus'.",
                    "",
                    "  \\n    pindah baris (newline)",
                    "  \\t    tab",
                    "  \\\\    satu backslash sungguhan",
                    "  \\\"    kutip ganda di dalam string yang dibatasi kutip ganda",
                    "  \\'    kutip tunggal di dalam string yang dibatasi kutip tunggal",
                    "",
                    "YANG PALING SERING DISALAHPAHAMI: \\n itu SATU karakter, bukan dua.",
                    "  len(\"a\\nb\")   ->  3, bukan 4",
                    "Backslash-nya tidak ikut tersimpan; ia hanya cara MENULIS karakter itu di kode.",
                    "",
                    "Kaitannya nanti di materi File I/O: readlines() menampilkan",
                    "['Baris pertama\\n', 'Baris kedua\\n']. Itu bukan tulisan aneh - itu karakter",
                    "pindah baris yang memang tersimpan di berkasnya. Karena itulah strip() dipakai",
                    "untuk membuangnya sebelum teksnya dipakai.",
                    "",
                    "RAW STRING: HURUF r DI DEPAN TANDA KUTIP",
                    "",
                    "  print(\"C:\\Users\\Andi\")     # RUSAK: \\U dikira awal escape unicode",
                    "  print(\"C:\\\\Users\\\\Andi\")   # benar, tapi berisik dibaca",
                    "  print(r\"C:\\Users\\Andi\")    # raw string: backslash apa adanya",
                    "",
                    "Huruf r sebelum tanda kutip BUKAN salah ketik. Artinya: di string ini backslash",
                    "tidak punya arti khusus. Dua tempat r\"...\" paling sering terlihat: pola regex",
                    "(r\"\\d+\") dan path Windows. Panjang r\"a\\nb\" adalah 4, karena di situ \\ dan n",
                    "memang benar-benar dua karakter terpisah.",
                ],
            },
            {
                "body": [
                    "print() JAUH LEBIH LENTUR DARIPADA YANG TERLIHAT DI MATERI PERTAMA",
                    "",
                    "1. Beberapa nilai sekaligus, dipisah koma:",
                    "     print(\"Nama:\", nama, \"Umur:\", umur)",
                    "   Antar nilai OTOMATIS disisipi satu spasi, dan tipe apa pun boleh dicampur.",
                    "   Bandingkan dengan menggabung memakai + :",
                    "     print(\"Umur: \" + umur)   # TypeError kalau umur bertipe int",
                    "     print(\"Umur:\", umur)     # aman, print() yang mengurus konversinya",
                    "",
                    "2. sep - pemisah antar nilai (default satu spasi):",
                    "     print(\"a\", \"b\", \"c\")           # a b c",
                    "     print(\"a\", \"b\", \"c\", sep=\"-\")  # a-b-c",
                    "     print(\"a\", \"b\", \"c\", sep=\"\")   # abc",
                    "",
                    "3. end - yang dicetak SETELAH semua nilai. Default-nya \"\\n\", si karakter",
                    "   pindah baris. Itu sebabnya tiap print() otomatis pindah ke baris baru.",
                    "     print(\"Memuat\", end=\"\")   # kursor ditahan di baris yang sama",
                    "     print(\"...selesai\")       # tersambung jadi: Memuat...selesai",
                    "",
                    "   print() KOSONG berarti: tidak mencetak nilai apa pun, tapi end tetap",
                    "   dijalankan - hasilnya pindah baris saja, alias satu baris kosong.",
                    "   Inilah yang dipakai di materi Perulangan: print(i, end=\" \") menjejerkan",
                    "   angka di satu baris, lalu print() kosong sesudah loop menutup baris itu.",
                    "   Tanpa print() penutupnya, keluaran berikutnya akan menempel di ujungnya.",
                    "",
                    "sep= dan end= ditulis dengan bentuk nama=nilai saat MEMANGGIL fungsi. Bentuk",
                    "itu namanya keyword argument: urutannya bebas, dan boleh dipakai salah satu",
                    "saja. Cara membuat fungsi sendiri yang menerimanya dibahas di materi Function.",
                ],
            },
            {
                "heading": "Contoh: escape sequence, sep, dan end",
                "code": """# --- escape sequence: backslash + satu huruf = SATU karakter ---
print("Baris satu\\nBaris dua")
print("Nama:\\tAndi")
print("Dia bilang \\"halo\\" lalu pergi")
print(len("a\\nb"))              # 3, bukan 4

# --- raw string: backslash dibiarkan apa adanya ---
print(r"C:\\Users\\Andi\\nota.txt")
print(len(r"a\\nb"))             # 4

# --- print() dengan beberapa nilai, sep, dan end ---
nama = "Andi"
umur = 20
print("Nama:", nama, "Umur:", umur)   # spasi disisipkan otomatis
print(nama, umur, sep=" | ")
print("a", "b", "c", sep="")

print("Memuat", end="")          # tanpa pindah baris
print("...", end="")
print(" selesai")

print()                          # end tetap jalan -> satu baris kosong
print("Setelah baris kosong")""",
            },
            {
                "body": [
                    "MASUKAN: input()",
                    "",
                    "input() menghentikan program, menunggu pengguna mengetik lalu menekan Enter,",
                    "dan melanjutkan program dengan teks yang tadi diketik. Teks di dalam kurungnya",
                    "adalah PROMPT - dicetak lebih dulu tanpa pindah baris, supaya pengguna tahu",
                    "apa yang diminta:",
                    "",
                    "  nama = input(\"Siapa namamu? \")",
                    "",
                    "ATURAN TERPENTINGNYA, DAN SUMBER BUG PERTAMA HAMPIR SEMUA PEMULA:",
                    "input() SELALU mengembalikan str. Selalu. Walaupun yang diketik jelas angka.",
                    "",
                    "  umur = input(\"Umur: \")    # pengguna mengetik 20",
                    "  print(umur + 1)   # TypeError: can only concatenate str (not \"int\") to str",
                    "  print(umur * 2)   # \"2020\", bukan 40 - str dikali angka berarti diulang",
                    "  print(umur == 20) # False selamanya, karena \"20\" bukan 20",
                    "",
                    "Jadi konversikan dulu (casting sudah dibahas di materi Variabel & Tipe Data):",
                    "  umur = int(input(\"Umur: \"))            # str -> int",
                    "  tinggi = float(input(\"Tinggi (m): \"))  # str -> float",
                    "",
                    "Jebakan turunannya:",
                    "  - int(\"20.5\") -> ValueError. int() hanya mau bilangan BULAT; pakai float().",
                    "  - int(\"\") atau int(\"abc\") -> ValueError, program berhenti. Cara menanganinya",
                    "    dengan rapi ada di materi Exception Handling.",
                    "  - int(\" 20 \") -> 20. Spasi di ujung dimaafkan, huruf tidak.",
                    "  - Enter yang ditekan pengguna TIDAK ikut terbawa; input() sudah membuangnya.",
                    "",
                    "Menjalankan program ber-input() di aplikasi ini: tekan \"Coba jalankan\" pada",
                    "blok kodenya, lalu isi kotak \"Masukan program (stdin)\" - satu jawaban per",
                    "baris, berurutan sesuai urutan input() dipanggil. Kalau kotaknya dikosongkan,",
                    "program berhenti dengan EOFError karena tidak ada yang bisa dibaca. Karena",
                    "jawabannya datang dari kotak dan bukan dari ketikan langsung, semua prompt",
                    "akan terlihat berderet di awal keluaran - itu normal, bukan bug.",
                    "",
                    "MODUL BAWAAN: FUNGSI YANG TIDAK OTOMATIS TERSEDIA",
                    "",
                    "print(), input(), int(), len(), type() selalu ada tanpa diminta. Sisanya -",
                    "akar kuadrat, angka acak, tanggal - tinggal di dalam MODUL yang harus",
                    "di-import dulu. Modul bawaan sudah ikut terpasang bersama Python; tidak perlu",
                    "mengunduh apa pun.",
                    "",
                    "  import math                 # dipakai: math.sqrt(16), math.pi",
                    "  from math import sqrt, pi   # dipakai: sqrt(16), pi   (tanpa \"math.\")",
                    "  import math as m            # alias; bentuk yang paling sering dilihat di",
                    "                              # kode nyata: import numpy as np",
                    "",
                    "Dua jebakannya:",
                    "  - import math lalu menulis sqrt(16) -> NameError. Nama yang dibuat baris",
                    "    itu adalah math, bukan sqrt.",
                    "  - JANGAN menamai berkasmu sendiri math.py atau random.py. Python akan",
                    "    menemukan berkasmu lebih dulu, dan modul aslinya jadi tidak terjangkau.",
                    "",
                    "Modul bawaan lain, package, dan cara membuat modul sendiri dibahas tuntas",
                    "di materi Module & Package.",
                ],
            },
            {
                "heading": "Contoh: input(), konversi tipe, dan modul math",
                "code": """import math
from math import sqrt        # dengan bentuk ini cukup tulis sqrt(...)

nama = input("Nama          : ")
jumlah_teks = input("Jumlah barang : ")
harga = float(input("Harga satuan  : "))   # langsung dikonversi

print(type(jumlah_teks))     # <class 'str'> -- input() SELALU str
jumlah = int(jumlah_teks)    # baru boleh dipakai berhitung

total = jumlah * harga
print("Halo,", nama)
print("Total bayar :", total)
print("Akar total  :", round(sqrt(total), 2))
print("Dibulatkan  :", math.floor(total))""",
            },
        ],
    },
    {
        "title": "4. Operator",
        "sections": [
            {
                "body": [
                    "Operator aritmatika:",
                    "  +  penjumlahan     -  pengurangan",
                    "  *  perkalian       /  pembagian (SELALU hasil float)",
                    "  // pembagian bulat (floor division, dibulatkan ke bawah)",
                    "  %  modulus (sisa bagi)",
                    "  ** pangkat",
                    "",
                    "Contoh:",
                    "  7 / 2   = 3.5   (pembagian biasa, hasil float)",
                    "  7 // 2  = 3     (floor division, hasil int jika kedua int)",
                    "  7 % 2   = 1     (sisa bagi)",
                    "  2 ** 3  = 8     (2 pangkat 3)",
                    "",
                    "Operator penugasan (assignment):",
                    "  =   x = 5     +=  x += 3     -=  x -= 3",
                    "  *=  x *= 3    /=  x /= 3     //= x //= 3",
                    "  **= x **= 2",
                    "",
                    "PENTING: Python TIDAK punya operator ++ atau -- seperti Java/C!",
                    "  Gunakan  x += 1   bukan  x++",
                ]
            },
            {
                "body": [
                    "Operator perbandingan (hasilnya bool):",
                    "  ==  sama dengan      !=  tidak sama",
                    "  >   lebih besar      <   lebih kecil",
                    "  >=  lebih besar sama <=  lebih kecil sama",
                    "",
                    "Operator logika (pakai KATA, bukan simbol seperti Java):",
                    "  and  -> DAN (keduanya True baru True)",
                    "  or   -> ATAU (salah satu True jadi True)",
                    "  not  -> NEGASI",
                    "",
                    "  (5 > 3) and (2 > 1)   -> True",
                    "  (5 > 3) and (2 > 5)   -> False",
                    "  not (5 > 3)           -> False",
                    "",
                    "Operator keanggotaan & identitas (KHAS Python):",
                    "  in      -> cek apakah ada di dalam koleksi",
                    "  not in  -> kebalikannya",
                    "  is      -> cek apakah referensi objek SAMA PERSIS",
                    "  is not  -> kebalikannya",
                ]
            },
            {
                "heading": "Contoh operator in & is",
                "code": """buah = ["apel", "jeruk", "mangga"]
print("apel" in buah)        # True
print("durian" not in buah)  # True

a = None
print(a is None)             # True (cara yang benar cek None, bukan a == None)

# Perbedaan == vs is untuk objek
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)    # True  (isi sama)
print(x is y)    # False (objek/alamat berbeda)"""
            },
        ],
    },
    {
        "title": "5. Percabangan (if / elif / else)",
        "sections": [
            {
                "body": [
                    "Percabangan membuat program mengambil keputusan.",
                    "Python TIDAK pakai kurung kurawal { } - blok kode ditentukan",
                    "oleh INDENTASI (harus konsisten, biasanya 4 spasi).",
                    "",
                    "Sintaks:",
                    "  if kondisi:",
                    "      # jalankan jika kondisi True",
                    "  elif kondisi2:",
                    "      # jalankan jika kondisi2 True",
                    "  else:",
                    "      # jalankan jika semua False",
                    "",
                    "PENTING: setiap if/elif/else diakhiri titik dua (:)",
                    "diikuti baris baru dengan indentasi.",
                    "",
                    "Akibat langsung dari aturan indentasi itu: blok yang benar-benar",
                    "KOSONG bukan program yang sah, melainkan IndentationError. Padahal",
                    "kadang memang belum ada yang mau ditulis di situ. Untuk itulah",
                    "keyword pass ada - ia tidak mengerjakan apa pun, tugasnya cuma",
                    "mengisi tempat supaya bloknya tidak kosong:",
                    "",
                    "  if saldo < 0:",
                    "      pass              # sengaja kosong, nanti baru diisi",
                    "  else:",
                    "      print(\"aman\")",
                    "",
                    "Tanda ... (tiga titik, namanya Ellipsis) dipakai untuk maksud yang",
                    "sama dan sama sahnya. pass bukan milik if saja - ia berlaku di mana",
                    "pun sebuah blok berindentasi dibutuhkan: for, while, def, class,",
                    "except. Jadi kalau nanti kamu bertemu class C(A, B): pass atau",
                    "class SaldoTidakCukup(Exception): pass, artinya tetap satu ini juga:",
                    "badan bloknya memang sengaja dibiarkan kosong. pass TIDAK punya arti",
                    "khusus untuk class maupun untuk exception.",
                ]
            },
            {
                "heading": "Contoh if-elif-else",
                "code": """nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")
# Output: B

# Ternary (conditional expression) - satu baris
status = "Lulus" if nilai >= 75 else "Tidak Lulus"
print(status)   # Lulus"""
            },
            {
                "body": [
                    "Python TIDAK punya switch-case (sebelum versi 3.10).",
                    "Sejak Python 3.10, ada match-case yang mirip switch:",
                    "",
                    "  match hari:",
                    "      case 1:",
                    "          print(\"Senin\")",
                    "      case 2:",
                    "          print(\"Selasa\")",
                    "      case _:",
                    "          print(\"Hari tidak valid\")",
                    "",
                    "  '_' adalah wildcard, mirip 'default' di switch bahasa lain.",
                    "",
                    "'Truthy' dan 'Falsy' (nilai yang dianggap True/False di if):",
                    "  Falsy: 0, 0.0, \"\", [], {}, (), None, False",
                    "  Truthy: semua nilai selain di atas.",
                    "  if daftar:      # sama dengan: if len(daftar) > 0:",
                    "      print(\"Ada isinya\")",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan (for & while)",
        "sections": [
            {
                "body": [
                    "1. for - mengulang untuk setiap elemen dalam sebuah",
                    "   'iterable' (list, string, range, dsb). BEDA dari Java/C,",
                    "   for Python TIDAK memakai (awal; kondisi; update).",
                    "",
                    "   for item in iterable:",
                    "       # kode diulang",
                    "",
                    "2. while - mengulang SELAMA kondisi bernilai True.",
                    "   while kondisi:",
                    "       # kode",
                    "",
                    "range(): menghasilkan urutan angka, dipakai luas dengan for.",
                    "  range(5)        -> 0, 1, 2, 3, 4",
                    "  range(1, 6)     -> 1, 2, 3, 4, 5",
                    "  range(0, 10, 2) -> 0, 2, 4, 6, 8  (loncat 2)",
                ]
            },
            {
                "heading": "Contoh for & while",
                "code": """# for dengan range
for i in range(1, 6):
    print(i, end=" ")
print()                     # 1 2 3 4 5

# for langsung ke elemen list
buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(b)

# for dengan index memakai enumerate
for i, b in enumerate(buah):
    print(f"{i}: {b}")      # 0: apel, 1: jeruk, 2: mangga

# while
j = 1
while j <= 5:
    print(j, end=" ")
    j += 1
print()                     # 1 2 3 4 5"""
            },
            {
                "heading": "break, continue, dan else pada loop",
                "code": """for i in range(1, 11):
    if i == 5:
        continue     # lewati 5
    if i == 8:
        break        # berhenti di 8
    print(i, end=" ")
# Output: 1 2 3 4 6 7

# KHAS PYTHON: for...else / while...else
# blok else dijalankan HANYA jika loop selesai TANPA break
for i in range(3):
    print("cek", i)
else:
    print("loop selesai normal, tanpa break")"""
            },
            {
                "body": [
                    "List comprehension (KHAS Python, cara ringkas membuat list",
                    "dari sebuah loop) - dibahas lebih detail di materi tersendiri:",
                    "  kuadrat = [x**2 for x in range(1, 6)]",
                    "  print(kuadrat)   # [1, 4, 9, 16, 25]",
                    "",
                    "Nested loop (loop di dalam loop) - untuk pola/tabel:",
                    "  for i in range(1, 5):",
                    "      for j in range(i):",
                    "          print(\"*\", end=\"\")",
                    "      print()",
                    "  Output:",
                    "  *",
                    "  **",
                    "  ***",
                    "  ****",
                    "",
                    "Nama _ untuk nilai yang memang tidak dipakai:",
                    "  for _ in range(3):",
                    "      print(\"halo\")         # nomor putarannya tidak terpakai",
                    "  _, nilai = (\"Andi\", 85)   # namanya diabaikan, ambil nilainya saja",
                    "",
                    "_ adalah variabel biasa - Python sama sekali tidak memperlakukannya",
                    "khusus. Yang khusus cuma KESEPAKATAN antar pembaca kode: 'isi variabel",
                    "ini memang tidak akan dipakai, jangan cari-cari di mana dipakainya'.",
                    "Menulis for i in range(3) pun tetap jalan; _ hanya membuat niatmu",
                    "langsung terbaca.",
                    "",
                    "Ada tiga hal mirip yang gampang tertukar, padahal artinya beda-beda:",
                    "  for _ in ...  -> nilai buangan, yang barusan dibahas",
                    "  case _:       -> wildcard di match-case (materi Percabangan),",
                    "                   artinya 'cocok dengan apa saja'",
                    "  _nama         -> konvensi 'protected' untuk atribut, dibahas di",
                    "                   materi OOP: Encapsulation & Dunder Methods",
                ]
            },
        ],
    },
    {
        "title": "7. Angka, Perbandingan & Operator yang Belum Dibahas",
        "sections": [
            {
                "body": [
                    "Materi 3 sudah mendaftar operator aritmatika, perbandingan, dan",
                    "logika lalu berhenti. Materi ini menutup sisanya: hal-hal yang lazim",
                    "ada di kode nyata tapi belum pernah disebut sekali pun. Kita mulai",
                    "dari angkanya sendiri.",
                    "",
                    "int (bilangan bulat) di Python TIDAK punya batas. 2 ** 100 dihitung",
                    "utuh sampai digit terakhir, tidak meluap (overflow) seperti int",
                    "32-bit di Java/C.",
                    "",
                    "float (bilangan desimal) punya batas, DAN tidak eksak:",
                    "",
                    "    0.1 + 0.2    menghasilkan    0.30000000000000004",
                    "",
                    "Ini bukan bug Python; hampir semua bahasa berperilaku sama. Komputer",
                    "menyimpan pecahan dalam basis DUA, dan 0,1 dalam basis dua adalah",
                    "pecahan berulang yang tak pernah selesai - persis seperti 1/3 yang",
                    "jadi 0,3333... dan tak pernah habis ditulis dalam basis sepuluh.",
                    "Yang benar-benar tersimpan adalah angka TERDEKAT yang muat, bukan",
                    "0,1 itu sendiri. Selisih sekecil itu ikut menumpuk tiap kali",
                    "dijumlahkan.",
                    "",
                    "Dari situ lahir satu aturan keras: JANGAN membandingkan dua float",
                    "dengan ==. Ekspresi 0.1 + 0.2 == 0.3 bernilai False. Kode semacam",
                    "itu tidak error dan tidak berhenti; ia diam-diam mengambil cabang",
                    "yang keliru, dan bug yang tidak berteriak adalah bug yang paling",
                    "lama dicari. Ini penting justru sekarang, karena banyak latihan",
                    "menghitung RATA-RATA, dan hasil pembagian / selalu float.",
                    "",
                    "Alat yang benar:",
                    "",
                    "  math.isclose(a, b)   True kalau selisihnya bisa diabaikan; ini",
                    "                       cara yang dipakai orang",
                    "  abs(a - b) < 1e-9    versi manualnya; abs() = nilai mutlak,",
                    "                       yaitu membuang tanda minus",
                    "  round(x, 2)          bulatkan ke 2 desimal (hasilnya tetap float)",
                    "  divmod(a, b)         (a // b, a % b) sekaligus, satu panggilan",
                    "",
                    "Tiga jebakan yang benar-benar menjebak:",
                    "",
                    "  - round(0.5) = 0 dan round(2.5) = 2. Kalau nilainya tepat di",
                    "    tengah, Python membulatkan ke GENAP terdekat supaya pembulatan",
                    "    berulang tidak selalu bias naik. Beda dari pelajaran sekolah,",
                    "    dan beda dari Java.",
                    "  - round() untuk MENAMPILKAN itu keliru. Pakai f\"{x:.2f}\"",
                    "    (materi 6), karena round(85.0, 2) tetap tercetak 85.0, bukan",
                    "    85.00 seperti yang kamu mau.",
                    "  - math.isclose(x, 0) hampir selalu False: toleransinya RELATIF",
                    "    terhadap besar angkanya, dan nol tidak punya besar. Lawan nol",
                    "    wajib pakai abs_tol: math.isclose(x, 0, abs_tol=1e-9).",
                    "",
                    "Kalau meleset sedikit pun tidak boleh - uang, pajak, tagihan -",
                    "jangan pakai float sama sekali:",
                    "",
                    "  decimal.Decimal      berhitung dalam basis SEPULUH, persis",
                    "                       seperti hitungan tangan di atas kertas",
                    "  fractions.Fraction   menyimpan pembilang & penyebut, jadi 1/3",
                    "                       tetap tepat 1/3",
                    "",
                    "Aturan mati untuk Decimal: SELALU dibuat dari STRING. Decimal(\"0.1\")",
                    "tepat 0,1, sedangkan Decimal(0.1) menampung float yang sudah meleset",
                    "sebelum sempat masuk. quantize() memaksa berapa desimal hasilnya,",
                    "dan ROUND_HALF_UP adalah pembulatan ala sekolah (tepat setengah",
                    "dibulatkan naik) - sengaja beda dari round() bawaan tadi.",
                    "",
                    "Jadi kalau nanti kamu ketemu Decimal(\"10.50\") di kode orang, itu",
                    "bukan gaya-gayaan: penulisnya menolak kehilangan satu sen gara-gara",
                    "pembulatan yang tak terlihat.",
                ],
            },
            {
                "heading": "Angka desimal: membandingkan, membulatkan, menghitung uang",
                "code": """import math
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

a = 0.1 + 0.2
print(a)                       # 0.30000000000000004
print(a == 0.3)                # False, inilah jebakannya
print(math.isclose(a, 0.3))    # True, cara yang benar
print(abs(a - 0.3) < 1e-9)     # True, versi manualnya

# math.isclose memakai toleransi RELATIF, jadi lawan nol ia gagal
print(math.isclose(1e-12, 0.0))                # False
print(math.isclose(1e-12, 0.0, abs_tol=1e-9))  # True

rata = sum([80, 90, 85]) / 3
print(rata)                    # 85.0
print(f"{rata:.2f}")           # 85.00, untuk DITAMPILKAN pakai f-string

# round() membulatkan ke GENAP terdekat kalau nilainya tepat di tengah
print(round(0.5), round(1.5), round(2.5))   # 0 2 2, bukan 1 2 3
print(round(2.675, 2))                      # 2.67, bukan 2.68

menit, detik = divmod(125, 60)        # hasil bagi dan sisa sekaligus
print(menit, detik, abs(-7))          # 2 5 7
print(float("nan") == float("nan"))   # False, nan tidak sama dengan apa pun

# Uang: pakai Decimal, dan SELALU dibuat dari string
total = Decimal("19.99") + Decimal("5.01")
print(total)                          # 25.00, dua desimalnya terjaga
pajak = total * Decimal("0.11")
print(pajak)                          # 2.7500
print(pajak.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # 2.75
print(Decimal(0.1))     # 0.1000000000000000055511151231257827... (JEBAKAN)
print(Decimal("0.1"))   # 0.1

# Fraction: pecahan yang benar-benar tepat
print(Fraction(1, 3) + Fraction(1, 6))    # 1/2
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))   # True""",
            },
            {
                "body": [
                    "Tiga kelompok operator berikut belum pernah muncul, padahal",
                    "ketiganya lazim ditemui.",
                    "",
                    "OPERATOR BITWISE bekerja pada BIT penyusun sebuah bilangan bulat:",
                    "",
                    "  a & b    AND   bit yang 1 di KEDUANYA          6 & 3   = 2",
                    "  a | b    OR    bit yang 1 di salah satunya     6 | 3   = 7",
                    "  a ^ b    XOR   bit yang BERBEDA                6 ^ 3   = 5",
                    "  ~a       NOT   balik semua bitnya              ~5      = -6",
                    "  a << n   geser kiri n bit  = a * 2**n          1 << 3  = 8",
                    "  a >> n   geser kanan n bit = a // 2**n         40 >> 2 = 10",
                    "",
                    "Ada versi penugasannya juga - |= &= ^= <<= >>= - sama polanya",
                    "dengan += di materi 3.",
                    "",
                    "Pemakaian yang paling sering ditemui adalah BIT FLAG: menyimpan",
                    "banyak saklar ya/tidak di dalam SATU angka. Tiap izin diberi satu",
                    "bit sendiri (1, 2, 4, 8, 16), lalu | menyalakan, & memeriksa, dan",
                    "&= ~ mematikan. Inilah yang sebenarnya terjadi di balik chmod 755,",
                    "dan di balik penulisan seperti re.IGNORECASE | re.MULTILINE yang",
                    "akan kamu temui di banyak library.",
                    "",
                    "PERINGATAN, dan ini bagian terpenting materi ini: | & ^ SUDAH kamu",
                    "lihat di materi 8 sebagai union/irisan set dan penggabung dict.",
                    "Simbolnya sama, ARTINYA BEDA. Yang menentukan bukan simbolnya,",
                    "melainkan TIPE operandnya:",
                    "",
                    "  3 | 4                 ->  7            int  : gabungkan bit",
                    "  {3} | {4}             ->  {3, 4}       set  : union himpunan",
                    "  {\"a\": 1} | {\"b\": 2}   ->  dict gabungan (Python 3.9+)",
                    "",
                    "Membaca izin | TULIS pada dua int sebagai 'union himpunan' adalah",
                    "salah paham yang membuat seluruh baris itu terasa tidak masuk akal.",
                    "",
                    "PERBANDINGAN BERANTAI. Di Java dan C, 0 < nilai <= 100 tidak",
                    "berarti seperti yang kamu kira: 0 < nilai dihitung lebih dulu jadi",
                    "True/1, lalu 1 itulah yang dibandingkan dengan 100. Di Python",
                    "bentuk ini SAH dan berarti dua perbandingan sekaligus, digabung and:",
                    "",
                    "  0 < nilai <= 100     sama dengan    (0 < nilai) and (nilai <= 100)",
                    "",
                    "Bagian tengahnya dievaluasi SATU KALI saja, jadi f(x) < g(y) < h(z)",
                    "tidak memanggil g() dua kali. Bentuk inilah yang dipakai solusi",
                    "Latihan 11, dan akan sering kamu temui di kode orang.",
                    "",
                    "OPERATOR WALRUS := (Python 3.8+) menugaskan nilai SAMBIL",
                    "menghasilkan nilai itu. Bedakan bertiga:",
                    "",
                    "  =    penugasan, sebuah pernyataan; tidak boleh masuk ke if/while",
                    "  ==   perbandingan, menghasilkan bool",
                    "  :=   penugasan yang JUGA menghasilkan nilainya, boleh di ekspresi",
                    "",
                    "Gunanya menghapus pengulangan: tanpa :=, len(daftar) harus dipanggil",
                    "dua kali, atau ditulis sebaris di atas if-nya walaupun cuma dipakai",
                    "di dalam if itu. Bentuk yang paling sering ditemui adalah membaca",
                    "berulang sampai habis:",
                    "",
                    "  while (baris := f.readline()):     (berkas dibahas di materi 17)",
                    "",
                    "Jebakannya:",
                    "",
                    "  - Presedensi. if n := len(x) > 5  dibaca  n := (len(x) > 5),",
                    "    jadi n berisi True - bukan panjangnya. Kurungnya wajib:",
                    "    if (n := len(x)) > 5:",
                    "  - := tidak bisa berdiri sendiri sebagai satu baris pernyataan;",
                    "    untuk itu pakai = biasa.",
                    "  - Pola sentinel di contoh memakai 'is not None', bukan sekadar",
                    "    nilai kebenarannya. Kalau cuma mengandalkan truthy/falsy",
                    "    (materi 4), angka 0 akan menghentikan loop padahal 0 itu data",
                    "    yang sah.",
                    "  - Jangan memakainya cuma karena bisa. Kalau nilainya dipakai",
                    "    sekali saja, = biasa sebaris di atasnya lebih enak dibaca.",
                ],
            },
            {
                "heading": "Bit flag: banyak saklar dalam satu angka",
                "code": """BACA     = 1   # 0b001
TULIS    = 2   # 0b010
EKSEKUSI = 4   # 0b100

izin = BACA | TULIS          # gabungkan dua flag
print(izin, bin(izin))       # 3 0b11

izin |= EKSEKUSI             # nyalakan satu flag lagi
print(izin, bin(izin))       # 7 0b111

print(bool(izin & TULIS))    # True  : apakah punya izin tulis?
izin &= ~TULIS               # cabut izin tulis
print(izin, bin(izin))       # 5 0b101
print(bool(izin & TULIS))    # False

print(5 ^ 3)     # 6   XOR: bit yang BERBEDA jadi 1
print(~5)        # -6  NOT: membalik semua bit
print(1 << 3)    # 8   geser kiri 3 bit, sama dengan 1 * 2**3
print(40 >> 2)   # 10  geser kanan 2 bit, sama dengan 40 // 4

# Simbol yang SAMA, arti ditentukan TIPE operandnya:
print(6 | 1)                  # 7 : int, gabungkan bit
print({1, 2} | {2, 3})        # {1, 2, 3} : set, union
print({"a": 1} | {"b": 2})    # {'a': 1, 'b': 2} : dict, gabungan
print(True | False)           # True : bool""",
            },
            {
                "heading": "Perbandingan berantai & operator walrus",
                "code": """nilai = 85
print(0 < nilai <= 100)              # True
print(0 < nilai and nilai <= 100)    # True, arti yang sama persis

def ambil():
    print("dipanggil")
    return 5

print(1 < ambil() < 10)   # "dipanggil" cuma sekali, lalu True

daftar = [3, 1, 4, 1, 5, 9, 2, 6]
if (n := len(daftar)) > 5:
    print(f"daftar panjang: {n} elemen")   # n masih bisa dipakai di sini

# JEBAKAN presedensi: tanpa kurung, := menangkap hasil PERBANDINGANNYA
if n := len(daftar) > 5:
    print(n)                         # True, bukan 8

# Pola sentinel, kembaran dari  while (baris := f.readline()):
sisa = iter([3, 0, 7])
while (x := next(sisa, None)) is not None:
    print("dapat", x)                # 3, lalu 0, lalu 7

# Di dalam comprehension: hitung sekali, pakai dua kali
harga = [1000, 5000, 20000]
mahal = [p for h in harga if (p := h // 10) > 400]
print(mahal)                         # [500, 2000]""",
            },
        ],
    },
    {
        "title": "8. String & Formatting",
        "sections": [
            {
                "body": [
                    "String di Python bersifat IMMUTABLE (tidak bisa diubah setelah",
                    "dibuat) dan bisa memakai kutip tunggal '...' atau ganda \"...\".",
                    "",
                    "String multi-baris pakai kutip tiga:",
                    "  teks = \"\"\"Baris pertama",
                    "  Baris kedua\"\"\"",
                    "",
                    "Indexing & slicing (mirip list, karena string = urutan karakter):",
                    "  s = \"Python\"",
                    "  s[0]      -> 'P'   (indeks dari 0)",
                    "  s[-1]     -> 'n'   (indeks negatif = dari belakang)",
                    "  s[0:3]    -> 'Pyt' (slicing: mulai:akhir, akhir TIDAK termasuk)",
                    "  s[2:]     -> 'thon'",
                    "",
                    "Slicing sebenarnya punya TIGA bagian: [mulai:akhir:langkah].",
                    "Langkah = berapa karakter dilompati tiap kali, bawaannya 1.",
                    "  s[::2]    -> 'Pto'    (dari awal ke akhir, ambil satu lewati satu)",
                    "  s[1::2]   -> 'yhn'    (sama, tapi mulai dari indeks 1)",
                    "  s[::-1]   -> 'nohtyP' (langkah -1 = berjalan MUNDUR, sehingga",
                    "                         hasilnya string terbalik)",
                    "  s[::-2]   -> 'nhy'    (mundur sambil melompat dua)",
                    "",
                    "Jadi s[::-1] bukan mantra yang harus dihafal, melainkan turunan",
                    "langsung dari aturan langkah. Ketiga bagiannya boleh dikosongkan; yang",
                    "kosong berarti 'dari paling awal', 'sampai paling akhir', dan 'langkah",
                    "1'. Itu sebabnya s[:] berarti seluruh isinya.",
                ]
            },
            {
                "heading": "Method string yang sering dipakai",
                "code": """s = "  Belajar Python  "

print(s.strip())          # "Belajar Python" (buang spasi ujung)
print(s.upper())          # "  BELAJAR PYTHON  "
print(s.lower())          # "  belajar python  "
print(s.strip().replace("Python", "Java"))  # "Belajar Java"
print(len(s))             # panjang string (termasuk spasi)
print("Python" in s)      # True
print(s.strip().split(" "))  # ['Belajar', 'Python']  -> jadi list

# Bergabung list jadi string
kata = ["Aku", "suka", "Python"]
print(" ".join(kata))     # "Aku suka Python"

print("python".capitalize())  # "Python"
print("PYTHON".isupper())     # True
print("123".isdigit())        # True"""
            },
            {
                "heading": "Method string lain yang selalu muncul di kode nyata",
                "code": """baris = "# ini komentar"
berkas = "laporan.py"

# startswith / endswith: penyaring paling umum di kode nyata, hasilnya bool
print(baris.startswith("#"))              # True
print(berkas.endswith(".py"))             # True
print(berkas.endswith((".py", ".txt")))   # True - boleh diberi tuple pilihan

teks = "pisang goreng pisang bakar"

# find() memberi -1 kalau tidak ketemu; index() MELEMPAR ValueError
print(teks.find("pisang"))    # 0
print(teks.find("apel"))      # -1  <- aman dipakai di dalam if
print(teks.index("goreng"))   # 7
print(teks.count("pisang"))   # 2

print("budi santoso".title())              # Budi Santoso  (tiap kata dikapitalkan)
print("catatan\\nbaris dua".splitlines())   # ['catatan', 'baris dua']

# strip() membuang kedua ujung; rstrip()/lstrip() hanya satu ujung
print(repr("  data  ".rstrip()))   # '  data'
print(repr("  data  ".lstrip()))   # 'data  '
print("7".zfill(3))                # 007  (diisi nol di depan sampai lebar 3)

# removeprefix / removesuffix (Python 3.9+): buang kalau ada, diamkan kalau tidak.
# Ditulis di dalam if supaya berkas ini tetap jalan di Python 3.8 -- di sana
# kedua method itu belum ada, dan memanggilnya berujung AttributeError.
if hasattr(str, "removesuffix"):
    print(berkas.removesuffix(".py"))   # laporan
    print(baris.removeprefix("# "))     # ini komentar
else:
    # Cara lama, dan alasan kedua method itu akhirnya dibuat: yang ini
    # gampang salah -- lupa memeriksa endswith() lebih dulu membuat
    # [:-3] memotong tiga huruf terakhir dari nama yang tidak berakhiran .py.
    print(berkas[:-3] if berkas.endswith(".py") else berkas)
    print(baris[2:] if baris.startswith("# ") else baris)"""
            },
            {
                "body": [
                    "find() dan index() menjawab pertanyaan yang sama dengan sikap yang",
                    "berbeda. Pakai find() kalau 'tidak ketemu' adalah kemungkinan wajar",
                    "yang mau kamu periksa sendiri; pakai index() kalau 'tidak ketemu'",
                    "berarti ada yang salah dan program memang sebaiknya berhenti.",
                    "Dua jebakan menyertai find(). Pertama, hasilnya harus dibandingkan",
                    "dengan -1 secara eksplisit: if teks.find(x) != -1 benar, sedangkan",
                    "if teks.find(x) SALAH - posisi 0 (ketemu di awal) bernilai Falsy dan",
                    "akan terbaca 'tidak ada'. Kedua, -1 sendiri adalah indeks yang SAH di",
                    "Python, jadi teks[teks.find(x)] yang tidak diperiksa dulu akan diam-diam",
                    "memberi karakter TERAKHIR alih-alih mengeluh.",
                    "",
                    "Daftar di dua contoh ini pun masih jauh dari lengkap, dan memang tidak",
                    "perlu dihafal. Yang penting: bentuknya selalu sama - teks.sesuatu(...)",
                    "- dan semuanya mengembalikan string BARU, tidak pernah mengubah string",
                    "aslinya. String itu immutable, seperti disebut di awal materi ini.",
                ]
            },
            {
                "body": [
                    "Dua operator aritmatika juga bekerja pada string, bukan cuma pada",
                    "angka:",
                    "  \"-\" * 40      -> garis pemisah sepanjang 40 karakter",
                    "  \"*\" * 3       -> '***'",
                    "  \"Ha\" + \"lo\"   -> 'Halo'   (+ MENYAMBUNG, bukan menjumlahkan)",
                    "",
                    "Materi Masukan, Keluaran & Modul Bawaan sudah menyinggung yang pertama",
                    "sebagai JEBAKAN (\"20\" * 2 memberi \"2020\", bukan 40). Di sini",
                    "kebalikannya: dipakai dengan sengaja. Garis pemisah di layar dan pola",
                    "segitiga bintang hampir selalu dibuat begini -",
                    "  for i in range(1, 5):",
                    "      print(\"*\" * i)",
                    "menggantikan loop bersarang yang ada di materi Perulangan.",
                    "",
                    "Keduanya menuntut tipe yang cocok di kedua sisi: \"umur: \" + 20 langsung",
                    "TypeError. Harus \"umur: \" + str(20), atau - lebih enak dibaca -",
                    "f\"umur: {20}\".",
                ]
            },
            {
                "heading": "f-string: cara modern format string (Python 3.6+)",
                "code": """nama = "Andi"
umur = 20
ipk = 3.756789

print(f"Nama: {nama}, Umur: {umur}")
print(f"IPK dibulatkan 2 desimal: {ipk:.2f}")     # IPK dibulatkan 2 desimal: 3.76
print(f"Umur tahun depan: {umur + 1}")            # bisa ekspresi langsung
print(f"{nama:>10}")   # rata kanan lebar 10 karakter
print(f"{nama:<10}|")  # rata kiri lebar 10 karakter

# Cara lama (masih sering ditemui di kode legacy):
print("Nama: {}, Umur: {}".format(nama, umur))
print("Nama: %s, Umur: %d" % (nama, umur))"""
            },
            {
                "heading": "Spesifier f-string yang menghemat banyak baris",
                "code": """nama = "Andi"
n = 1234567
p = 0.4567
ipk = 3.75

print(f"{nama=}")        # nama='Andi'  <- nama variabelnya ikut tercetak
print(f"{ipk=}")         # ipk=3.75     <- cara tercepat mengintip isi variabel
print(f"{n:,}")          # 1,234,567    <- pemisah ribuan otomatis
print(f"{p:.1%}")        # 45.7%        <- dikali 100 lalu diberi tanda persen
print(f"{ipk:08.2f}")    # 00003.75     <- lebar 8, 2 desimal, sisanya diisi nol
print(f"[{nama:^20}]")   # [        Andi        ]   <- rata TENGAH selebar 20
print(f"[{nama:*^20}]")  # [********Andi********]   <- karakter pengisi bebas"""
            },
            {
                "body": [
                    "Bentuk {nilai=} itu khusus untuk mengintip isi variabel saat mencari",
                    "bug: ia mencetak nama variabelnya sekalian, jadi kamu tidak perlu",
                    "menulis print(\"ipk:\", ipk) lagi. Sisanya - :, untuk ribuan, :.1% untuk",
                    "persen, :^ untuk rata tengah - dipakai saat merapikan tabel dan",
                    "laporan, melanjutkan :.2f, :>10, dan :<10 di contoh sebelumnya.",
                    "",
                    "Dua baris berlabel 'cara lama' di contoh f-string yang pertama",
                    "juga perlu bisa DIBACA, karena kode lama penuh keduanya:",
                    "",
                    "  \"Nama: {}, Umur: {}\".format(nama, umur)",
                    "    Tiap {} yang kosong diisi argumen .format() secara BERURUTAN: {}",
                    "    pertama menerima argumen pertama, dan seterusnya. Boleh juga diberi",
                    "    nomor {0} {1} atau nama {n}, lalu .format(n=nama).",
                    "",
                    "  \"Nama: %s, Umur: %d\" % (nama, umur)",
                    "    Di sini % adalah OPERATOR, bukan modulus dari materi Operator.",
                    "    Sisi kirinya string berpola, sisi kanannya tuple berisi nilai yang",
                    "    mengisi pola itu berurutan: %s untuk apa saja (diubah jadi string),",
                    "    %d untuk bilangan bulat, %f untuk desimal, %.2f untuk dua desimal.",
                    "    Kalau nilainya cuma satu, tuple-nya boleh dilepas: \"Halo %s\" % nama.",
                    "",
                    "Untuk kode BARU pakai f-string. Dua bentuk di atas cukup dikenali - tapi",
                    "harus benar-benar dikenali, karena keduanya masih hidup di mana-mana.",
                ]
            },
        ],
    },
    {
        "title": "9. List & Tuple",
        "sections": [
            {
                "body": [
                    "List = koleksi data berurutan yang BISA DIUBAH (mutable),",
                    "boleh berisi tipe data campuran, dan ukurannya dinamis.",
                    "",
                    "  angka = [10, 20, 30, 40]",
                    "  campur = [1, \"dua\", 3.0, True]",
                    "",
                    "Operasi umum pada list:",
                    "  angka.append(50)      -> tambah di akhir",
                    "  angka.insert(0, 5)    -> sisipkan di indeks tertentu",
                    "  angka.remove(20)      -> hapus berdasarkan NILAI",
                    "  angka.pop()           -> hapus & kembalikan elemen terakhir",
                    "  angka.pop(0)          -> hapus berdasarkan INDEKS",
                    "  len(angka)            -> jumlah elemen",
                    "  angka.sort()          -> urutkan (mengubah list asli)",
                    "  sorted(angka)         -> urutkan (list BARU, asli tak berubah)",
                    "  angka.reverse()       -> balik urutan",
                ]
            },
            {
                "heading": "Contoh manipulasi list & slicing",
                "code": """nilai = [80, 90, 75, 85, 60]

print(nilai[0])       # 80  (indeks pertama)
print(nilai[-1])      # 60  (indeks terakhir)
print(nilai[1:3])     # [90, 75]  (slicing)
print(nilai[:2])      # [80, 90]  (dari awal sampai indeks 2, exclusive)
print(nilai[2:])      # [75, 85, 60]

nilai.append(95)
print(nilai)          # [80, 90, 75, 85, 60, 95]

total = sum(nilai)
rata = total / len(nilai)
print(f"Total: {total}, Rata-rata: {rata:.2f}")

print(max(nilai), min(nilai))    # 95 60

# List di dalam list (mirip array 2 dimensi)
matriks = [[1, 2, 3], [4, 5, 6]]
print(matriks[0][1])   # 2 (baris 0, kolom 1)"""
            },
            {
                "body": [
                    "Tuple = seperti list tapi TIDAK BISA DIUBAH (immutable).",
                    "Dipakai untuk data yang tidak boleh berubah (koordinat, dsb).",
                    "",
                    "  titik = (10, 20)",
                    "  titik[0] = 99    # ERROR! tuple tidak bisa diubah",
                    "",
                    "  x, y = titik     # unpacking: x=10, y=20",
                    "",
                    "Kenapa pakai tuple padahal ada list?",
                    "  1. Performa sedikit lebih cepat & hemat memori dari list.",
                    "  2. Bisa dipakai sebagai key di dictionary (list TIDAK BISA).",
                    "  3. 'Kontrak' bahwa data ini tidak boleh berubah - lebih aman.",
                    "",
                    "Fungsi bawaan berguna untuk list/tuple:",
                    "  len(x), sum(x), max(x), min(x), sorted(x)",
                    "  list(range(5))  -> [0, 1, 2, 3, 4]",
                ]
            },
        ],
    },
    {
        "title": "10. Fungsi Bawaan untuk Koleksi",
        "sections": [
            {
                "body": [
                    "Materi List & Tuple ditutup dengan daftar 'fungsi bawaan berguna':",
                    "len, sum, max, min, sorted. Daftar itu benar, tapi BELUM selesai -",
                    "dan justru karena tampak rapi, banyak orang berhenti di situ. Fungsi",
                    "di materi ini muncul di hampir setiap kode Python nyata; tidak",
                    "mengenalnya berarti tersandung tiap kali membaca kode orang lain.",
                    "",
                    "Semuanya bekerja pada ITERABLE apa pun - list, tuple, string, set,",
                    "dict, range - bukan cuma list. Itu sebabnya jumlahnya sedikit tapi",
                    "jangkauannya luas: satu fungsi melayani semua jenis koleksi.",
                    "",
                    "Tiga kelompok, dan perbedaannya penting sekali:",
                    "",
                    "  Menghasilkan SATU nilai, langsung bisa dicetak:",
                    "    len  sum  max  min  any  all  isinstance  id  repr",
                    "",
                    "  Menghasilkan LIST baru:",
                    "    sorted  list",
                    "",
                    "  Menghasilkan ITERATOR - dan ini bukan list:",
                    "    zip  enumerate  reversed  map  filter",
                    "",
                    "Kelompok ketiga adalah sumber kebingungan pertama pemula:",
                    "",
                    "  print(zip(a, b))        -> <zip object at 0x7f3c9a1b2d40>",
                    "  print(list(zip(a, b)))  -> [('Andi', 85), ('Budi', 70)]",
                    "",
                    "Iterator itu antrean yang dibaca sekali jalan, bukan wadah berisi;",
                    "ia belum menghitung apa pun sampai diminta. Untuk MELIHAT isinya,",
                    "bungkus list(). Untuk sekadar di-for-loop, tidak perlu dibungkus.",
                    "Seluk-beluknya dibahas tuntas di materi Iterator & Generator.",
                ],
            },
            {
                "heading": "zip() dan enumerate(): berjalan bersama tanpa indeks",
                "code": """nama = ["Andi", "Budi", "Citra", "Dewi"]
nilai = [85, 70, 95]

# Dua koleksi berjalan sejajar - tanpa satu pun indeks
for n, v in zip(nama, nilai):
    print(f"{n}: {v}")
# Dewi TIDAK muncul: zip berhenti di koleksi terpendek, tanpa error apa pun

print(list(zip(nama, nilai)))
# [('Andi', 85), ('Budi', 70), ('Citra', 95)]

# Pola yang sangat sering dipakai: dua list jadi satu dictionary
kunci = ["nama", "umur", "kota"]
isi = ["Andi", 20, "Bandung"]
print(dict(zip(kunci, isi)))
# {'nama': 'Andi', 'umur': 20, 'kota': 'Bandung'}

# zip(*matriks): baris berubah jadi kolom (transpose)
matriks = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matriks)))
# [(1, 4), (2, 5), (3, 6)]

# enumerate: nomor dan isinya sekaligus. start= mengubah NOMOR-nya saja
for i, n in enumerate(nama, start=1):
    print(f"{i}. {n}")
# 1. Andi / 2. Budi / 3. Citra / 4. Dewi   <- Andi tetap ikut

# Keduanya boleh digabung: nomor + dua koleksi sejajar
for i, (n, v) in enumerate(zip(nama, nilai), start=1):
    print(i, n, v)""",
            },
            {
                "body": [
                    "zip berhenti di koleksi TERPENDEK, dan itu terjadi DIAM-DIAM: tidak",
                    "ada error, tidak ada peringatan, sisanya hilang begitu saja. Kalau",
                    "kedua koleksi seharusnya sama panjang, ini bug tanpa jejak sama sekali.",
                    "  - Python 3.10+ punya zip(a, b, strict=True) yang melempar ValueError",
                    "    kalau panjangnya beda. Di Python lebih lama, argumen itu justru error.",
                    "  - Aman di versi mana pun: periksa len(a) == len(b) lebih dulu.",
                    "",
                    "zip() dan enumerate() mengembalikan iterator, dan isinya HABIS sekali",
                    "pakai. Jebakan ini rutin menghabiskan waktu orang:",
                    "",
                    "  z = zip(nama, nilai)",
                    "  print(list(z))   -> [('Andi', 85), ('Budi', 70), ('Citra', 95)]",
                    "  print(list(z))   -> []      <- kosong, dan TIDAK ada error",
                    "",
                    "  Dua for-loop atas objek zip yang sama: yang kedua tidak jalan sama",
                    "  sekali. Kalau perlu dipakai ulang, simpan: pasangan = list(zip(...))",
                    "",
                    "Tanda * pada zip(*matriks) MEMBONGKAR list-of-list jadi argumen",
                    "terpisah, jadi zip(*[[1, 2, 3], [4, 5, 6]]) sama persis dengan",
                    "zip([1, 2, 3], [4, 5, 6]). Hasilnya barisan TUPLE, bukan list - pakai",
                    "[list(k) for k in zip(*matriks)] kalau memang butuh list. (Tanda *",
                    "dibahas tuntas di materi Membongkar Argumen & Parameter Khusus.)",
                    "",
                    "Pada enumerate(daftar, start=1), 'start' cuma menggeser NOMOR yang",
                    "dicetak. Elemen pertama TETAP ikut - ini bukan cara melewati elemen.",
                    "Pakai enumerate, jangan for i in range(len(daftar)): yang kedua memaksa",
                    "menulis daftar[i] di setiap baris dan gampang meleset satu langkah.",
                ],
            },
            {
                "heading": "any, all, sorted, max, min, reversed, dan pengenal objek",
                "code": """angka = [12, -5, 8, 30, -1]

# any: cukup SATU yang benar. all: harus SEMUA benar.
print(any(x < 0 for x in angka))     # True  - ada yang minus
print(all(x < 100 for x in angka))   # True  - semuanya di bawah 100
print(any([]), all([]))              # False True  <- jebakan koleksi kosong

# any/all memakai aturan truthy: "", 0, [], None dihitung salah
form = {"nama": "Andi", "email": "", "kota": "Bandung"}
print(all(form.values()))            # False - masih ada isian kosong

nama = ["dewi", "Andi", "budi", "Citra"]

# key= diberi NAMA fungsi, tanpa tanda kurung: len, bukan len()
print(sorted(nama))                  # ['Andi', 'Citra', 'budi', 'dewi']
print(sorted(nama, key=str.lower))   # ['Andi', 'budi', 'Citra', 'dewi']
print(sorted(nama, key=len, reverse=True))  # ['Citra', 'dewi', 'Andi', 'budi']
print(max(nama, key=len))            # Citra
print(max([], default=0))            # 0  - tanpa default: ValueError
print(list(reversed(angka)))         # [-1, 30, 8, -5, 12]
print(sum([15000, 25000], start=10000))     # 50000  (10000 = ongkos kirim)

# Mengenali objek - muncul di mana-mana saat membaca kode orang lain
nilai = True
print(type(nilai), type(nilai).__name__)    # <class 'bool'> bool
print(isinstance(nilai, int))               # True! bool adalah turunan int
print(isinstance(3.5, (int, float)))        # True - boleh beberapa tipe

teks = "Halo\\nDunia"
print(str(teks))                     # tercetak jadi DUA baris
print(repr(teks))                    # 'Halo\\nDunia' - ditampilkan apa adanya
print(["Halo", "Dunia"])             # isi list selalu dicetak pakai repr

a = [1, 2]
b = a
c = [1, 2]
print(id(a) == id(b), id(a) == id(c))       # True False""",
            },
            {
                "body": [
                    "any() dan all() berhenti begitu jawabannya pasti (short-circuit).",
                    "Karena itu tulis generator - kurung biasa - bukan list comprehension:",
                    "  any(x < 0 for x in data)     -> berhenti di elemen minus PERTAMA",
                    "  any([x < 0 for x in data])   -> seluruh list dibangun dulu",
                    "Keduanya cuma mengembalikan True/False, bukan elemennya.",
                    "",
                    "all() atas koleksi KOSONG bernilai True: 'tidak ada satu pun yang",
                    "melanggar'. Akibat nyatanya, validasi berbentuk all(...) atas daftar",
                    "yang ternyata kosong akan LOLOS tanpa memeriksa apa pun. Kalau kosong",
                    "itu tidak boleh, periksa daftarnya sendiri lebih dulu.",
                    "",
                    "daftar.sort() mengubah list ASLINYA dan mengembalikan None:",
                    "  daftar = daftar.sort()   -> daftar kini None, dan errornya baru",
                    "                              muncul beberapa baris kemudian.",
                    "sorted(daftar) yang memberi list baru. sorted() juga STABIL - elemen",
                    "ber-key sama tetap pada urutan aslinya, dan itulah yang membuat",
                    "pengurutan dua tingkat bisa dikerjakan dengan dua kali sorted().",
                    "",
                    "reversed() butuh koleksi ber-URUTAN: list, tuple, str, range.",
                    "reversed({1, 2, 3}) -> TypeError, karena set memang tidak berurutan.",
                    "Tiga hal yang beda: daftar[::-1] memberi list baru, reversed(daftar)",
                    "memberi iterator, daftar.reverse() mengubah list aslinya.",
                    "",
                    "Pakai isinstance(x, T), bukan type(x) == T. isinstance mengakui kelas",
                    "TURUNAN, type() menolaknya; bedanya baru terasa setelah materi",
                    "Inheritance, tapi kebiasaannya dibentuk sekarang.",
                    "",
                    "repr() otomatis dipakai di dalam list, tuple, dict, dan saat debugging",
                    "- itu sebabnya print(['a']) menampilkan tanda kutip padahal print('a')",
                    "tidak. Di f-string, {teks!r} memaksa bentuk repr. Cara menentukan",
                    "sendiri bentuk str dan repr sebuah objek ada di materi Dunder Methods.",
                    "",
                    "id() adalah nomor identitas objek selama ia hidup, dan itulah yang",
                    "sebenarnya dibandingkan operator 'is' (materi Operator). Nilainya",
                    "berganti tiap program dijalankan, jadi jangan pernah disimpan - gunanya",
                    "hanya menjawab 'ini objek yang sama, atau kembarannya?'.",
                ],
            },
        ],
    },
    {
        "title": "11. Dictionary & Set",
        "sections": [
            {
                "body": [
                    "Dictionary (dict) = koleksi pasangan KEY: VALUE, mirip",
                    "HashMap di Java. Key harus unik & immutable (str/int/tuple).",
                    "Sejak Python 3.7+, urutan insert dict TERJAGA.",
                    "",
                    "  mahasiswa = {",
                    "      \"nama\": \"Andi\",",
                    "      \"umur\": 20,",
                    "      \"jurusan\": \"Informatika\"",
                    "  }",
                    "",
                    "  mahasiswa[\"nama\"]         -> \"Andi\"  (akses by key)",
                    "  mahasiswa[\"ipk\"] = 3.5     -> tambah key baru",
                    "  mahasiswa.get(\"kota\", \"-\") -> \"-\" (default jika key tak ada,",
                    "                                    aman dari KeyError)",
                    "  del mahasiswa[\"umur\"]      -> hapus key",
                    "  \"nama\" in mahasiswa         -> True (cek key ada/tidak)",
                ]
            },
            {
                "heading": "Contoh operasi dictionary",
                "code": """mahasiswa = {"nama": "Andi", "umur": 20, "jurusan": "Informatika"}

for key in mahasiswa:
    print(key, ":", mahasiswa[key])

for key, value in mahasiswa.items():
    print(f"{key} -> {value}")

print(mahasiswa.keys())     # dict_keys(['nama', 'umur', 'jurusan'])
print(mahasiswa.values())   # dict_values(['Andi', 20, 'Informatika'])

# Dictionary comprehension
kuadrat = {x: x**2 for x in range(1, 6)}
print(kuadrat)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Menggabung 2 dictionary (Python 3.9+)
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
gabungan = a | b
print(gabungan)   # {'x': 1, 'y': 99, 'z': 3}  (b menimpa a jika key sama)"""
            },
            {
                "body": [
                    "Set = koleksi data UNIK (tidak boleh duplikat), TIDAK berurutan.",
                    "Mirip HashSet di Java. Cocok untuk menghilangkan duplikat &",
                    "operasi himpunan (union, intersection, dll).",
                    "",
                    "  angka = {1, 2, 2, 3, 3, 3}",
                    "  print(angka)   # {1, 2, 3}  (duplikat otomatis hilang)",
                    "",
                    "  angka.add(4)          -> tambah elemen",
                    "  angka.remove(1)       -> hapus elemen (error jika tak ada)",
                    "  angka.discard(99)     -> hapus jika ada, aman jika tak ada",
                ]
            },
            {
                "heading": "Operasi himpunan pada set",
                "code": """a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union: {1, 2, 3, 4, 5, 6}
print(a & b)    # intersection: {3, 4}
print(a - b)    # difference: {1, 2}  (ada di a, tidak di b)
print(a ^ b)    # symmetric difference: {1, 2, 5, 6}

# Menghilangkan duplikat dari list dengan cepat
nama = ["Andi", "Budi", "Andi", "Citra", "Budi"]
unik = list(set(nama))
print(unik)     # urutan tidak dijamin sama seperti aslinya"""
            },
        ],
    },
    {
        "title": "12. Wadah Data Siap Pakai (module collections)",
        "sections": [
            {
                "body": [
                    "Module collections berisi wadah data siap pakai: dict dan list yang sudah disetel",
                    "untuk pola yang paling sering ditulis orang. Ia bagian dari Python sendiri",
                    "(stdlib) - tidak perlu pip install apa pun, cukup satu baris import.",
                    "",
                    "  from collections import defaultdict, Counter, namedtuple, deque",
                    "",
                    "  defaultdict  dict yang membuatkan nilai awal saat key-nya belum ada",
                    "  Counter      dict khusus menghitung: berapa kali tiap nilai muncul",
                    "  namedtuple   tuple yang tiap posisinya punya NAMA",
                    "  deque        list yang cepat ditambah/dikurangi di KEDUA ujungnya",
                    "",
                    "Kenapa ini perlu kamu kenali walau belum kamu pakai sendiri: keempatnya muncul",
                    "di kode orang lain justru untuk MENGGANTIKAN pola dict/list dari materi",
                    "Dictionary & Set. Baris seperti",
                    "",
                    "      per_orang[nama].append(barang)",
                    "",
                    "tanpa satu pun pengecekan key terlihat seperti bug yang pasti KeyError -",
                    "padahal benar, karena per_orang bukan dict biasa. Kalau kamu tidak tahu wadah",
                    "ini ada, kamu akan menghabiskan sore 'membetulkan' kode yang tidak rusak.",
                ],
            },
            {
                "heading": "defaultdict: nilai awal yang dibuatkan sendiri",
                "code": """from collections import defaultdict

pesanan = [("Andi", "kopi"), ("Budi", "teh"), ("Andi", "roti"), ("Citra", "teh")]

# CARA dict biasa: key wajib disiapkan dulu, kalau tidak -> KeyError
per_orang = {}
for nama, barang in pesanan:
    if nama not in per_orang:
        per_orang[nama] = []
    per_orang[nama].append(barang)
print(per_orang)

# CARA defaultdict: dua baris pengecekannya HILANG, hasilnya sama persis
per_orang = defaultdict(list)
for nama, barang in pesanan:
    per_orang[nama].append(barang)   # key belum ada -> dibuatkan [] lebih dulu
print(per_orang)                     # cetakannya BUKAN dict polos
print(dict(per_orang))               # dict() mengembalikannya jadi dict biasa

# defaultdict(int): nilai awalnya 0, jadi += 1 boleh langsung
jumlah = defaultdict(int)
for nama, barang in pesanan:
    jumlah[barang] += 1
print(dict(jumlah))                  # {'kopi': 1, 'teh': 2, 'roti': 1}

# JEBAKAN: MEMBACA saja sudah membuat key baru
print(len(per_orang))          # 3
per_orang["Dedi"]              # cuma dibaca, tidak diisi apa pun
print(len(per_orang))          # 4 -- "Dedi" terlanjur ada, isinya []
print("Dedi" in per_orang)     # True
print(per_orang.get("Eka"))    # None, dan "Eka" TIDAK ikut dibuat""",
            },
            {
                "heading": "Counter: menghitung tanpa loop penghitung",
                "code": """from collections import Counter

kalimat = "kucing makan ikan ikan kecil kucing tidur"

kata = Counter(kalimat.split())      # hitung KATA -> beri ia hasil split()
print(kata)                          # Counter({'kucing': 2, 'ikan': 2, ...})
print(kata["ikan"])                  # 2
print(kata["gajah"])                 # 0  -- BUKAN KeyError
print("gajah" in kata)               # False -- membaca TIDAK menambah key
print(kata.most_common(2))           # [('kucing', 2), ('ikan', 2)]
print(sum(kata.values()))            # 7 -- total seluruh cacahan

# JEBAKAN: Counter atas STRING menghitung HURUF, bukan kata
huruf = Counter("kabar kabur")
print(huruf.most_common(3))          # [('a', 3), ('k', 2), ('b', 2)]

# Counter menerima list apa pun, bukan cuma teks
nilai = Counter(["A", "B", "A", "C", "A", "B"])
print(nilai.most_common())           # semua, terurut dari yang terbanyak
nilai.update(["C", "C"])             # MENAMBAH cacahan, bukan menimpa
print(nilai["C"])                    # 3""",
            },
            {
                "heading": "namedtuple & deque",
                "code": """from collections import namedtuple, deque

# --- namedtuple: tuple yang tiap posisinya punya NAMA ---
Suhu = namedtuple("Suhu", ["kota", "derajat"])

bacaan = [Suhu("Bandung", 22), Suhu("Surabaya", 33), Suhu("Medan", 30)]
for b in bacaan:
    print(f"{b.kota}: {b.derajat}")     # dibaca lewat nama, bukan b[1]

print(bacaan[0])                        # Suhu(kota='Bandung', derajat=22)
kota, derajat = bacaan[0]               # tetap bisa di-unpack seperti tuple
print(kota, derajat)                    # Bandung 22
print(bacaan[0] == ("Bandung", 22))     # True -- ia MEMANG sebuah tuple

dingin = bacaan[0]._replace(derajat=18) # immutable: hasilnya SALINAN baru
print(dingin, "|", bacaan[0])           # data lama tidak ikut berubah

# --- deque: antrean yang cepat di KEDUA ujung ---
antrean = deque(["Andi", "Budi"])
antrean.append("Citra")                 # masuk dari belakang
antrean.appendleft("Zaki")              # masuk dari DEPAN
print(antrean)                          # deque(['Zaki', 'Andi', 'Budi', 'Citra'])
print(antrean.popleft())                # Zaki  -- keluar dari depan
print(antrean.pop())                    # Citra -- keluar dari belakang
print(list(antrean))                    # ['Andi', 'Budi']

# maxlen: riwayat berukuran tetap, yang paling tua otomatis terbuang
riwayat = deque(maxlen=3)
for perintah in ["buka", "tulis", "simpan", "tutup"]:
    riwayat.append(perintah)
print(riwayat)                          # "buka" hilang tanpa error apa pun""",
            },
            {
                "body": [
                    "Jebakan yang benar-benar menjebak:",
                    "",
                    "  1. defaultdict TUMBUH saat dibaca. Salah ketik key sekali - d[\"nma\"] - dan dict",
                    "     biasa langsung KeyError, jadi kamu tahu persis di baris mana; defaultdict",
                    "     malah mengembalikan [] lalu diam, dan salahnya baru terasa jauh di belakang.",
                    "     Untuk sekadar mengintip, pakai .get(key) seperti pada dict biasa.",
                    "  2. Yang dioper ke defaultdict adalah NAMA fungsinya, bukan hasil panggilannya:",
                    "     defaultdict(list)  benar,  defaultdict(list())  -> TypeError.",
                    "  3. Counter(\"halo dunia\") menghitung HURUF. Untuk kata, beri ia list:",
                    "     Counter(kalimat.split()). Keduanya sama-sama jalan tanpa error, jadi salah",
                    "     pilih di sini tidak pernah diberi tahu siapa pun.",
                    "  4. Counter[key] yang tidak ada bernilai 0 dan TIDAK menambah key - persis",
                    "     kebalikan defaultdict. Dua wadah yang mirip, perilakunya berlawanan.",
                    "  5. namedtuple tetap immutable: p.derajat = 9 -> AttributeError. _replace()",
                    "     memberi SALINAN baru; kalau hasilnya lupa ditampung, kamu akan bingung",
                    "     kenapa datanya tidak berubah padahal 'sudah diganti'.",
                    "  6. deque tidak bisa di-slice: d[1:3] -> TypeError. Mengakses tengahnya (d[500])",
                    "     juga lambat. Cepatnya HANYA di dua ujung.",
                    "  7. maxlen membuang yang tertua DIAM-DIAM. Itu memang gunanya, tapi jangan",
                    "     dipakai untuk data yang tidak boleh hilang.",
                    "",
                    "Kapan dict/list biasa sudah cukup:",
                    "  - Isinya sedikit dan key-nya sudah pasti (konfigurasi, satu baris data).",
                    "  - Kamu JUSTRU ingin KeyError saat key salah - itu penjaga yang berguna.",
                    "  - Cuma sekali dua kali menyisipkan di depan; list.insert(0, x) baru terasa",
                    "    lambat kalau datanya ribuan.",
                    "",
                    "Kapan namedtuple cukup, kapan sudah waktunya class:",
                    "  - Cukup: objeknya hanya menyimpan data, tidak punya perilaku, dan wajar",
                    "    diperlakukan sebagai tuple - satu baris hasil query, satu titik koordinat.",
                    "  - Sudah waktunya class: butuh method sendiri, butuh field yang bisa diubah,",
                    "    atau butuh pemeriksaan nilai saat objeknya dibuat. Class dibahas di materi",
                    "    OOP nanti, dan dataclass mengisi ruang tengah antara keduanya.",
                ],
            },
        ],
    },
    {
        "title": "13. Function (Fungsi)",
        "sections": [
            {
                "body": [
                    "Function = blok kode yang bisa dipanggil berulang, dideklarasikan",
                    "dengan keyword def. Python TIDAK butuh deklarasi tipe kembali.",
                    "",
                    "  def nama_fungsi(parameter):",
                    "      # isi fungsi",
                    "      return nilai   # opsional, jika tak ada return -> None",
                    "",
                    "  def sapa(nama):",
                    "      print(f\"Halo, {nama}\")",
                    "",
                    "  def tambah(a, b):",
                    "      return a + b",
                    "",
                    "Memanggil fungsi:",
                    "  sapa(\"Andi\")            # Halo, Andi",
                    "  hasil = tambah(3, 4)    # hasil = 7",
                ]
            },
            {
                "heading": "Default parameter, keyword argument, *args, **kwargs",
                "code": """def sapa(nama, sapaan="Halo"):
    print(f"{sapaan}, {nama}!")

sapa("Andi")                  # Halo, Andi!
sapa("Budi", sapaan="Hai")    # Hai, Budi!  (keyword argument)
sapa(nama="Citra", sapaan="Selamat pagi")

# *args: menerima BANYAK argumen posisi jadi tuple
def total(*angka):
    return sum(angka)

print(total(1, 2, 3))        # 6
print(total(1, 2, 3, 4, 5))  # 15

# **kwargs: menerima BANYAK argumen keyword jadi dict
def profil(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

profil(nama="Andi", umur=20, jurusan="Informatika")"""
            },
            {
                "body": [
                    "Scope variabel:",
                    "  - Variabel di dalam fungsi bersifat LOKAL (hanya dikenal",
                    "    di dalam fungsi itu).",
                    "  - Untuk mengubah variabel GLOBAL dari dalam fungsi,",
                    "    gunakan keyword 'global' (JARANG dipakai, hindari jika bisa):",
                    "      total = 0",
                    "      def tambah_total(n):",
                    "          global total",
                    "          total += n",
                    "",
                    "Docstring: dokumentasi fungsi, ditulis di baris pertama fungsi:",
                    "  def tambah(a, b):",
                    "      \"\"\"Mengembalikan hasil penjumlahan a dan b.\"\"\"",
                    "      return a + b",
                    "  help(tambah)   # menampilkan docstring",
                    "",
                    "Type hint (opsional, untuk kejelasan & bantuan IDE, Python 3.5+):",
                    "  def tambah(a: int, b: int) -> int:",
                    "      return a + b",
                    "  (Python TETAP dynamically typed - ini hanya PETUNJUK, tidak",
                    "  dipaksakan saat runtime seperti di Java/C++.)",
                ]
            },
        ],
    },
    {
        "title": "14. Referensi Objek, Salinan & Jebakan Mutable",
        "sections": [
            {
                "body": [
                    "Di Python, variabel BUKAN kotak yang menyimpan nilai - ia LABEL yang",
                    "ditempelkan ke sebuah objek di memori. Objeknya yang punya isi; namanya",
                    "cuma penunjuk ke sana. Satu objek boleh punya banyak nama sekaligus.",
                    "",
                    "Akibatnya, baris yang kelihatan paling polos ternyata tidak menyalin apa pun:",
                    "",
                    "  a = [1, 2, 3]",
                    "  b = a          # BUKAN salinan - b cuma label KEDUA untuk objek yang sama",
                    "  b.append(4)",
                    "  print(a)       # [1, 2, 3, 4]   <- a ikut berubah",
                    "",
                    "Ini bukan kelakuan aneh yang khusus untuk list; ini cara kerja SEMUA tipe di",
                    "Python. Yang menentukan kelihatan atau tidaknya cuma satu hal: objek itu bisa",
                    "diubah di tempat atau tidak.",
                    "",
                    "  Mutable   (bisa diubah di tempat) : list, dict, set, objek class buatanmu",
                    "  Immutable (tidak bisa diubah)     : int, float, str, bool, tuple, None",
                    "",
                    "Pada yang immutable, 'mengubah' selalu berarti membuat objek BARU lalu",
                    "memindahkan labelnya (lihat materi String soal str yang immutable, dan materi",
                    "List & Tuple soal tuple). Karena objek lamanya tidak pernah tersentuh, nama",
                    "lain yang menunjuk ke sana tetap aman - itu sebabnya jebakan ini seolah cuma",
                    "menyerang list dan dict, padahal aturannya sama untuk semuanya.",
                    "",
                    "Alat untuk mengintip identitas objek (sudah dikenalkan di materi Operator):",
                    "  a is b     -> True kalau keduanya objek yang SAMA PERSIS, bukan sekadar",
                    "                isinya mirip",
                    "  a == b     -> cuma menanyakan ISInya sama",
                    "  id(a)      -> nomor identitas objek. Angkanya berbeda tiap kali program",
                    "                dijalankan, jadi yang berguna adalah MEMBANDINGKANnya",
                    "                (id(a) == id(b)), bukan membaca angkanya satu per satu.",
                    "",
                    "Catatan: jangan pakai 'is' untuk membandingkan angka atau string. Python",
                    "kadang mendaur ulang objek kecil, jadi hasilnya bisa kebetulan True lalu",
                    "diam-diam False di data yang lebih besar. Untuk isi, pakai '=='.",
                ],
            },
            {
                "heading": "Bukti: dua nama untuk satu objek",
                "code": """a = [1, 2, 3]
b = a                  # b BUKAN salinan: nama KEDUA untuk objek yang sama

print(a is b)          # True  -> memang satu objek
print(id(a) == id(b))  # True  -> nomor identitasnya sama persis

b.append(4)
print(a)               # [1, 2, 3, 4]  <- a ikut berubah, padahal yang disentuh b

# Bandingkan dengan int: angka TIDAK bisa diubah di tempat
x = 10
y = x
y += 1                 # membuat objek 11 yang BARU, lalu y menunjuk ke sana
print(x, y)            # 10 11  -> x tidak tersentuh

# Tanda '=' memindahkan LABEL, bukan mengubah objeknya
a = [9, 9]             # a sekarang menunjuk objek lain
print(b)               # [1, 2, 3, 4]  <- b masih memegang objek yang lama
print(a is b)          # False""",
            },
            {
                "body": [
                    "Kalau kamu memang mau objek BARU, mintalah secara eksplisit. Empat bentuk yang",
                    "paling sering muncul di kode orang - semuanya mengerjakan hal yang sama:",
                    "",
                    "  baru = lama[:]        # slicing penuh; gaya lama, masih sangat umum",
                    "  baru = list(lama)     # membangun list baru dari isinya",
                    "  baru = lama.copy()    # sejak Python 3.3; paling gampang dibaca",
                    "  baru = dict(cfg)      # untuk dict (ada juga cfg.copy())",
                    "  baru = set(s)         # untuk set",
                    "",
                    "Kalau suatu saat kamu membaca baris seperti itu dan merasa mubazir - jangan",
                    "dihapus. Baris itulah satu-satunya yang menahan kode dari mengubah data milik",
                    "orang lain.",
                    "",
                    "TAPI semua cara di atas cuma salinan DANGKAL (shallow copy): yang dibuat baru",
                    "hanya wadah paling luar. Isinya tetap objek yang itu-itu juga.",
                    "",
                    "  asli  = [[1, 2], [3, 4]]",
                    "  salin = asli[:]",
                    "  salin[0].append(99)",
                    "  print(asli)      # [[1, 2, 99], [3, 4]]   <- tembus sampai ke asli",
                    "",
                    "Untuk list satu lapis berisi angka atau string, salinan dangkal SUDAH cukup:",
                    "isinya immutable, tidak ada yang bisa diubah dari dalam.",
                    "",
                    "Untuk struktur bersarang, pakai salinan DALAM (deep copy) yang menyalin sampai",
                    "ke dasar:",
                    "",
                    "  import copy",
                    "  aman = copy.deepcopy(konfigurasi)",
                    "",
                    "Kapan deepcopy benar-benar dibutuhkan: kalau strukturnya BERSARANG (dict berisi",
                    "list, list berisi dict, state aplikasi) DAN kamu memang akan mengubah isi",
                    "dalamnya. Untuk data satu lapis ia cuma memperlambat tanpa menambah keamanan,",
                    "dan pada struktur besar biayanya terasa - ia menelusuri seluruh isi.",
                    "",
                    "Yang TAMPAK menyalin padahal tidak:",
                    "  b = a            -> label kedua untuk objek yang sama",
                    "  fungsi(a)        -> parameter di dalam fungsi juga cuma label kedua",
                    "  [[0] * 3] * 3    -> tiga nama untuk SATU baris yang sama",
                    "",
                    "([0] * 3 sendiri aman, karena 0 tidak bisa diubah. Yang berbahaya adalah",
                    "mengulang list - '*' menggandakan REFERENSInya, bukan isinya.)",
                    "",
                    "Aturan yang sama melahirkan dua jebakan di fungsi (contoh terakhir):",
                    "  1. Mengoper list/dict ke fungsi berarti fungsi itu BISA mengubah data milik",
                    "     pemanggilnya. Kalau yang dioper int, str, atau tuple, fungsi tidak punya",
                    "     cara mengubahnya - paling jauh ia memindahkan labelnya sendiri di dalam.",
                    "     Karena itu putuskan sejak awal: fungsimu mengubah di tempat (biasanya",
                    "     return None, seperti list.sort()) atau mengembalikan yang BARU (seperti",
                    "     sorted()). Yang membingungkan adalah fungsi yang diam-diam melakukan",
                    "     keduanya.",
                    "  2. Nilai default sebuah parameter dibuat SEKALI, saat baris 'def' dijalankan",
                    "     - bukan tiap kali fungsinya dipanggil. Jadi def f(x=[]) memakai SATU list",
                    "     yang sama untuk semua panggilan, dan isinya menumpuk. Polanya yang benar",
                    "     memakai None sebagai penanda 'tidak diisi':",
                    "       def f(x=None):",
                    "           if x is None:",
                    "               x = []",
                    "     Untuk default yang immutable (0, \"\", None, True) tidak ada masalah -",
                    "     tidak ada yang bisa menumpuk di sana.",
                ],
            },
            {
                "heading": "Salinan dangkal, salinan dalam, dan jebakan [[0] * 3] * 3",
                "code": """import copy

# Salinan DANGKAL: wadah luarnya baru, isi di dalamnya masih dibagi bersama
asli = [[1, 2], [3, 4]]
dangkal = asli[:]               # sama saja: list(asli) atau asli.copy()

print(dangkal is asli)          # False -> list luarnya memang objek baru
print(dangkal[0] is asli[0])    # True  -> list di dalamnya MASIH yang itu juga

dangkal[0].append(99)
print(asli)                     # [[1, 2, 99], [3, 4]]  <- asli ikut kena

# Salinan DALAM: isinya ikut disalin sampai ke dasar
dalam = copy.deepcopy(asli)
dalam[0].append(7)
print(asli)                     # [[1, 2, 99], [3, 4]]     <- kali ini aman
print(dalam)                    # [[1, 2, 99, 7], [3, 4]]

# Jebakan klasik: '*' pada list mengulang REFERENSI, bukan menyalin isinya
papan = [[0] * 3] * 3           # tiga nama untuk SATU baris yang sama
papan[0][0] = 1
print(papan)                    # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# Cara benar: bikin baris BARU untuk tiap iterasi
papan = [[0] * 3 for _ in range(3)]
papan[0][0] = 1
print(papan)                    # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]""",
            },
            {
                "heading": "Dua jebakan di fungsi: mengubah milik pemanggil & def f(x=[])",
                "code": """def tambah_bonus(nilai):
    nilai.append(100)        # mengubah list MILIK PEMANGGIL, bukan salinan
    return nilai

data = [80, 90]
tambah_bonus(data)
print(data)                  # [80, 90, 100]  <- data ikut berubah

def tambah_bonus_aman(nilai):
    baru = list(nilai)       # kerjakan di salinan sendiri
    baru.append(100)
    return baru

data = [80, 90]
hasil = tambah_bonus_aman(data)
print(data, hasil)           # [80, 90] [80, 90, 100]

# JEBAKAN: nilai default dibuat SEKALI, saat baris 'def' dijalankan
def catat_salah(item, keranjang=[]):
    keranjang.append(item)
    return keranjang

print(catat_salah("apel"))   # ['apel']
print(catat_salah("jeruk"))  # ['apel', 'jeruk']  <- bocor dari panggilan sebelumnya!

# Pola yang benar: None sebagai penanda "tidak diisi"
def catat(item, keranjang=None):
    if keranjang is None:
        keranjang = []
    keranjang.append(item)
    return keranjang

print(catat("apel"))         # ['apel']
print(catat("jeruk"))        # ['jeruk']""",
            },
        ],
    },
    {
        "title": "15. Rekursi",
        "sections": [
            {
                "body": [
                    "Rekursi = fungsi yang memanggil DIRINYA SENDIRI. Ini bukan trik:",
                    "begitu sebuah nama didaftarkan oleh def, isi fungsinya boleh menyebut",
                    "nama apa pun yang dikenal saat dipanggil - termasuk namanya sendiri.",
                    "",
                    "Kenapa ini ada. Sebagian data bentuknya bersarang tanpa kedalaman",
                    "tetap: folder di dalam folder, JSON di dalam JSON, balasan komentar",
                    "di dalam balasan komentar. Untuk itu for bertingkat tidak cukup,",
                    "karena kamu harus tahu lebih dulu perlu berapa tingkat - dan kamu",
                    "TIDAK tahu. Rekursi memakai bentuk datanya sendiri sebagai aturan.",
                    "",
                    "Setiap fungsi rekursif WAJIB punya dua bagian:",
                    "  - base case      -> kondisi berhenti; menjawab langsung TANPA",
                    "                      memanggil dirinya lagi",
                    "  - recursive case -> memanggil dirinya untuk masalah LEBIH KECIL",
                    "",
                    "Yang membuatnya benar bukan sekadar adanya base case, tapi bahwa",
                    "tiap panggilan benar-benar BERGERAK ke arahnya. faktorial(n - 1)",
                    "mendekati 1; faktorial(n) tidak pindah ke mana-mana.",
                    "",
                    "Kalau base case lupa ditulis, atau ada tapi tak pernah tercapai:",
                    "  def hitung_mundur(n):",
                    "      print(n)",
                    "      hitung_mundur(n - 1)   # tak berhenti: 3, 2, 1, 0, -1, -2, ...",
                    "",
                    "  hitung_mundur(3)",
                    "  # RecursionError: maximum recursion depth exceeded",
                    "",
                    "Perhatikan bedanya dari 'while True': yang terjadi BUKAN program",
                    "menggantung, melainkan sebuah error. Alasannya di bagian batas",
                    "rekursi di bawah.",
                    "",
                    "Istilah yang akan sering kamu temui: tumpukan panggilan (call",
                    "stack). Panggilan yang belum selesai tidak hilang - ia menunggu,",
                    "lengkap dengan variabel lokalnya, sampai panggilan di dalamnya",
                    "mengembalikan nilai. Contoh berikut membuat tumpukan itu kelihatan.",
                ],
            },
            {
                "heading": "Faktorial: melihat tumpukan panggilannya sendiri",
                "code": """def faktorial(n, kedalaman=0):
    spasi = "  " * kedalaman     # cuma untuk tampilan, bukan bagian rekursinya
    print(f"{spasi}-> masuk faktorial({n})")
    if n <= 1:
        # BASE CASE: menjawab langsung, tidak memanggil dirinya lagi
        print(f"{spasi}   base case, kembalikan 1")
        return 1
    # RECURSIVE CASE: masalah yang sama, ukurannya lebih kecil
    lebih_kecil = faktorial(n - 1, kedalaman + 1)
    hasil = n * lebih_kecil
    print(f"{spasi}<- keluar faktorial({n}) = {n} * {lebih_kecil} = {hasil}")
    return hasil

print("Jawaban:", faktorial(4))

# -> masuk faktorial(4)
#   -> masuk faktorial(3)
#     -> masuk faktorial(2)
#       -> masuk faktorial(1)
#          base case, kembalikan 1
#     <- keluar faktorial(2) = 2 * 1 = 2
#   <- keluar faktorial(3) = 3 * 2 = 6
# <- keluar faktorial(4) = 4 * 6 = 24
# Jawaban: 24

# Baca dari atas: SEMUA panggilan turun dulu sampai base case, baru hasilnya
# dirakit balik ke atas. Baris "masuk faktorial(4)" sudah tercetak jauh
# sebelum fungsi itu selesai - selama itu ia menunggu di tumpukan panggilan.""",
            },
            {
                "heading": "Kasus nyata: dict/JSON bersarang dan isi folder bertingkat",
                "code": """# Dua bentuk data yang paling sering memaksa orang menulis rekursi untuk
# pertama kalinya. Polanya sama persis: kalau isinya wadah lagi -> panggil
# diri sendiri; kalau bukan wadah -> itu base case, kerjakan lalu berhenti.

from pathlib import Path
from tempfile import TemporaryDirectory

# --- 1. Menelusuri dict bersarang (bentuknya persis hasil json.load) ---
data = {
    "nama": "toko",
    "cabang": [
        {"nama": "utara", "stok": {"beras": 10, "gula": 4}},
        {"nama": "selatan", "stok": {"beras": 7}},
    ],
}

def cari_angka(simpul, jalur="data"):
    if isinstance(simpul, dict):
        for kunci, nilai in simpul.items():
            cari_angka(nilai, f"{jalur}[{kunci!r}]")
    elif isinstance(simpul, list):
        for i, nilai in enumerate(simpul):
            cari_angka(nilai, f"{jalur}[{i}]")
    elif isinstance(simpul, (int, float)):
        # base case: angka tidak punya isi untuk ditelusuri lagi
        print(f"{jalur} = {simpul}")

cari_angka(data)
# data['cabang'][0]['stok']['beras'] = 10
# data['cabang'][0]['stok']['gula'] = 4
# data['cabang'][1]['stok']['beras'] = 7

# --- 2. Menelusuri folder bertingkat ---
def pohon(folder, tingkat=0):
    for anak in sorted(folder.iterdir()):   # sorted: urutan iterdir tak dijamin
        print("  " * tingkat + anak.name + ("/" if anak.is_dir() else ""))
        if anak.is_dir():
            pohon(anak, tingkat + 1)        # recursive case
        # berkas biasa = base case: tidak ada isi untuk ditelusuri

with TemporaryDirectory() as tmp:           # folder contoh, dihapus otomatis
    akar = Path(tmp)
    (akar / "src" / "utils").mkdir(parents=True)
    (akar / "src" / "main.py").write_text("print('halo')")
    (akar / "src" / "utils" / "teks.py").write_text("")
    (akar / "README.md").write_text("catatan")
    pohon(akar)
# README.md
# src/
#   main.py
#   utils/
#     teks.py

# Jebakan halus di cari_angka: isinstance(True, int) bernilai True di Python,
# jadi True/False ikut tercetak sebagai angka. Kalau itu tidak diinginkan,
# saring lebih dulu dengan cabang isinstance(simpul, bool) SEBELUM cabang int.
# Untuk folder, versi loop-nya sudah disediakan Python: os.walk().""",
            },
            {
                "body": [
                    "Python membatasi seberapa dalam rekursi boleh menumpuk:",
                    "  import sys",
                    "  print(sys.getrecursionlimit())   # 1000 di hampir semua Python",
                    "",
                    "Lewat dari itu, program berhenti dengan:",
                    "  RecursionError: maximum recursion depth exceeded",
                    "",
                    "Tracebacknya sangat panjang dan memuat baris seperti",
                    "'[Previous line repeated 996 more times]'. Baris itu justru",
                    "petunjuk terbaiknya: fungsi yang namanya diulang-ulang di situ",
                    "adalah fungsi yang tak pernah sampai ke base case-nya.",
                    "",
                    "Batas itu PELINDUNG, bukan gangguan. Tiap panggilan yang belum",
                    "selesai memakai tempat di tumpukan milik proses. Tanpa batas,",
                    "tumpukannya habis dan prosesnya mati tanpa pesan apa pun",
                    "(segmentation fault) - jauh lebih sulit didiagnosis daripada",
                    "exception yang menyebut nama fungsi dan nomor barisnya.",
                    "",
                    "Batasnya memang bisa dinaikkan, tapi ini JARANG jawaban yang benar:",
                    "  import sys",
                    "  sys.setrecursionlimit(20000)",
                    "Yang naik cuma penghitung milik Python; ukuran stack asli dari",
                    "sistem operasi TIDAK ikut naik. Jadi RecursionError yang sopan bisa",
                    "berubah jadi crash tanpa pesan sama sekali. Kalau kamu tergoda",
                    "memakainya, penyebabnya hampir selalu salah satu dari dua ini:",
                    "  - base case-nya tidak pernah tercapai. Itu bug; menaikkan batas",
                    "    cuma menyembunyikannya lebih lama.",
                    "  - datanya memang panjang, dan yang keliru justru memilih rekursi",
                    "    untuk data seperti itu.",
                    "",
                    "Kapan loop lebih baik daripada rekursi:",
                    "  - Kalau kedalamannya sebanding dengan JUMLAH DATA - menjumlahkan",
                    "    sejuta baris, faktorial 5000. Loop tidak punya batas kedalaman",
                    "    dan lebih cepat.",
                    "  - Kalau bentuknya lurus: satu panggilan melahirkan tepat satu",
                    "    panggilan lagi. Itu perulangan yang menyamar, dan lebih jelas",
                    "    ditulis sebagai for.",
                    "  - Python TIDAK punya tail-call optimization seperti sebagian",
                    "    bahasa lain, jadi 'return f(x)' di baris terakhir pun tetap",
                    "    menumpuk. Tidak ada keringanan di sini.",
                    "",
                    "Rekursi menang saat DATANYA sendiri bercabang dan kedalamannya",
                    "tidak diketahui: pohon, JSON bersarang, folder, penguraian",
                    "ekspresi. Di sana kedalamannya belasan sampai puluhan tingkat -",
                    "jauh di bawah 1000, dan kodenya jauh lebih pendek daripada versi",
                    "loop yang harus mengurus tumpukannya sendiri.",
                ],
            },
            {
                "heading": "Kenapa fibonacci rekursif lambat, dan apa yang ditolong @lru_cache",
                "code": """# Materi Decorator nanti memakai fibonacci ber-@lru_cache sambil menyebut
# "tanpa cache SANGAT lambat". Ini alasannya, dalam angka - jalankan sendiri
# dan perhatikan penghitung panggilannya.

from functools import lru_cache

panggilan = 0

def fib(n):
    global panggilan
    panggilan += 1
    if n < 2:                          # base case: fib(0) = 0, fib(1) = 1
        return n
    return fib(n - 1) + fib(n - 2)     # DUA cabang -> pekerjaannya berlipat

print("fib(20) =", fib(20), "dengan", panggilan, "panggilan")
panggilan = 0
print("fib(25) =", fib(25), "dengan", panggilan, "panggilan")
# fib(20) = 6765 dengan 21891 panggilan
# fib(25) = 75025 dengan 242785 panggilan
# n naik 5, pekerjaannya naik 11 kali lipat. fib(50) tak selesai hari ini.

# Sebabnya: fib(23) dihitung ulang dari nol setiap kali dibutuhkan, dan itu
# terjadi ratusan kali. @lru_cache menyimpan hasil per argumen, sehingga
# tiap n dihitung TEPAT sekali.
@lru_cache(maxsize=None)
def fib_cepat(n):
    if n < 2:
        return n
    return fib_cepat(n - 1) + fib_cepat(n - 2)

print("fib_cepat(25) =", fib_cepat(25), fib_cepat.cache_info())
# fib_cepat(25) = 75025 CacheInfo(hits=23, misses=26, maxsize=None, currsize=26)
# 26 perhitungan sungguhan; sisanya diambil dari cache.

# Versi loop: tanpa cache, tanpa batas kedalaman, satu lintasan saja.
def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("fib_loop(25) =", fib_loop(25))
print("fib_loop(500) punya", len(str(fib_loop(500))), "digit")
# fib_loop(25) = 75025
# fib_loop(500) punya 105 digit

# Pelajarannya: rekursi yang lambat biasanya bukan salah rekursinya, tapi
# salah karena pekerjaan yang sama dikerjakan berkali-kali. Cara kerja tanda @
# dan cara membuat decorator sendiri dibahas di materi Decorator.""",
            },
        ],
    },
    {
        "title": "16. Membongkar Argumen & Parameter Khusus",
        "sections": [
            {
                "body": [
                    "Di materi Function kamu memakai bintang di sisi DEFINISI: def total(*angka)",
                    "MENGUMPULKAN banyak argumen jadi satu tuple. Materi ini tentang arah sebaliknya -",
                    "bintang di sisi PEMANGGILAN, yang MEMBONGKAR satu koleksi jadi argumen terpisah.",
                    "",
                    "Tandanya sama persis, artinya berlawanan. Yang menentukan cuma letaknya:",
                    "  di dalam def(...)     -> mengumpulkan  (satu nama menampung banyak nilai)",
                    "  di dalam pemanggilan  -> membongkar    (satu koleksi jadi banyak argumen)",
                    "",
                    "  *   membongkar list/tuple/range jadi argumen POSISI",
                    "  **  membongkar dict jadi argumen KEYWORD (key-nya jadi nama parameter)",
                    "",
                    "Bedanya paling gampang dilihat di print:",
                    "  genap = [2, 4, 6, 8]",
                    "  print(genap)    -> [2, 4, 6, 8]   satu argumen: list-nya dicetak lengkap dengan",
                    "                                    kurung siku dan komanya",
                    "  print(*genap)   -> 2 4 6 8        empat argumen: print memisahkannya sendiri",
                    "",
                    "Kalau bintangnya lupa, fungsi menerima SATU list di parameter pertama dan sisanya",
                    "kosong:",
                    "  def f(a, b, c): ...",
                    "  f([1, 2, 3])",
                    "  TypeError: f() missing 2 required positional arguments: 'b' and 'c'",
                    "",
                    "Pesan itu menyesatkan kalau tidak tahu sebabnya: kamu merasa sudah mengirim tiga",
                    "angka, tapi Python melihat satu list.",
                ],
            },
            {
                "heading": "Membongkar koleksi jadi argumen",
                "code": """def buat_akun(nama, umur, kota):
    return f"{nama} ({umur} th) dari {kota}"

baris = ["Andi", 20, "Bandung"]
data = {"nama": "Budi", "umur": 22, "kota": "Medan"}

# buat_akun(baris) -> TypeError: list-nya dianggap SATU argumen
print(buat_akun(*baris))    # * membongkar list jadi 3 argumen posisi
print(buat_akun(**data))    # ** membongkar dict jadi argumen keyword

genap = [2, 4, 6, 8]
print(genap)                # [2, 4, 6, 8]  -> 1 argumen, dicetak apa adanya
print(*genap)               # 2 4 6 8       -> 4 argumen, dipisah spasi
print(*genap, sep=" | ")    # 2 | 4 | 6 | 8

# Inilah kenapa wrapper decorator SELALU ditulis seperti ini:
def catat(fungsi):
    def wrapper(*args, **kwargs):        # KUMPULKAN apa pun yang dikirim
        print(f"-> memanggil {fungsi.__name__}")
        return fungsi(*args, **kwargs)   # BONGKAR lagi, persis seperti semula
    return wrapper

@catat
def luas(panjang, lebar=2):
    return panjang * lebar

print(luas(5))
print(luas(5, lebar=3))""",
            },
            {
                "body": [
                    "Di materi Decorator kamu sudah melihat pasangan itu tanpa penjelasan: wrapper MENAMPUNG",
                    "argumen apa pun ke args/kwargs, lalu MEMBONGKARNYA lagi saat meneruskan ke fungsi",
                    "asli. Tanpa bintang di baris kedua, fungsi aslinya akan menerima satu tuple dan satu",
                    "dict, bukan argumen yang tadi dikirim pemanggil.",
                    "",
                    "Bintang juga bekerja di dalam kurung pembuat koleksi. Di sana ia menuang isi koleksi",
                    "lain ke dalam koleksi baru:",
                    "  [*a, *b]      -> list baru: isi a lalu isi b",
                    "  (*a, *b)      -> tuple baru",
                    "  {*a, *b}      -> set baru (duplikatnya hilang sendiri)",
                    "  {**a, **b}    -> dict baru; kalau key-nya bentrok, yang KANAN menang",
                    "",
                    "{**bawaan, **pilihan} adalah bentuk penggabungan dict yang paling sering ditemui di",
                    "kode orang, dan polanya hampir selalu sama: satu dict setelan bawaan, ditimpa dict",
                    "pilihan pemakai. Materi Dictionary & Set sudah mengajarkan a | b untuk hasil yang sama.",
                    "Bedanya:",
                    "  a | b         khusus dict, dan baru ada sejak Python 3.9",
                    "  {**a, **b}    jalan sejak Python 3.5, dan pola bintangnya sama untuk list/set/tuple",
                    "  a.update(b)   MENGUBAH a di tempat. Dua bentuk di atas membuat dict BARU; a dan b",
                    "                tetap utuh. Salah pilih di sini berarti diam-diam merusak data asal.",
                    "",
                    "Arah bongkar berlaku juga di KIRI tanda sama dengan. Materi List & Tuple memakai unpacking",
                    "biasa (x, y = titik) yang menuntut jumlahnya pas persis. Dengan bintang, satu nama boleh",
                    "menampung sisanya - namanya extended unpacking:",
                    "  pertama, *sisa = [10, 20, 30]      pertama=10  sisa=[20, 30]",
                    "  nama, *nilai, status = baris       yang di ujung diambil, sisanya ke tengah",
                    "",
                    "Tiga hal yang perlu diingat:",
                    "  1. Yang ditampung bintang SELALU list, walau sumbernya tuple atau string.",
                    "  2. Sisanya boleh kosong; hasilnya list kosong, bukan error.",
                    "  3. Bintang cuma boleh SATU di satu sisi kiri. a, *b, *c = ... adalah SyntaxError,",
                    "     karena tidak ada cara menebak di mana b berhenti dan c mulai.",
                ],
            },
            {
                "heading": "Menggabung koleksi & extended unpacking",
                "code": """bawaan = {"warna": "biru", "ukuran": 12, "tebal": False}
pilihan = {"ukuran": 16}

setelan = {**bawaan, **pilihan}     # yang KANAN menimpa yang kiri
print(setelan)
print(bawaan)                       # bawaan tetap utuh, tidak ikut berubah

depan = [1, 2]
belakang = [3, 4]
print([*depan, *belakang, 5])       # [1, 2, 3, 4, 5]
print([*depan, *range(7, 10)])      # sumbernya boleh iterable apa saja
print({*depan, *belakang, 1})       # set: duplikatnya hilang sendiri

# Extended unpacking: bintang menampung SISANYA, hasilnya selalu list
baris = ["andi", "80", "90", "70", "lulus"]
nama, *nilai, status = baris
print(nama, nilai, status)          # andi ['80', '90', '70'] lulus

pertama, *sisa = [10, 20, 30]
print(pertama, sisa)                # 10 [20, 30]

satu, *habis = [9]
print(satu, habis)                  # 9 []  sisanya boleh kosong, bukan error""",
            },
            {
                "body": [
                    "Sampai sini bintang selalu diikuti nama. Kalau ia BERDIRI SENDIRI di daftar parameter,",
                    "artinya lain lagi: semua parameter SESUDAHNYA wajib dipanggil dengan namanya.",
                    "",
                    "  def buat_koneksi(host, *, timeout=30, ulang=3):",
                    "      ...",
                    "",
                    "  buat_koneksi(\"localhost\")              OK",
                    "  buat_koneksi(\"localhost\", timeout=5)   OK",
                    "  buat_koneksi(\"localhost\", 5)",
                    "  TypeError: buat_koneksi() takes 1 positional argument but 2 were given",
                    "",
                    "Kenapa dipaksa begitu? Karena buat_koneksi(\"localhost\", 5, 3) tidak terbaca oleh siapa",
                    "pun - 5 itu timeout atau jumlah ulang? Bintang telanjang memaksa pemanggilnya jadi",
                    "dokumentasi dirinya sendiri. Fungsi bawaan pun begitu: sorted(data, reverse=True)",
                    "memang tidak punya cara ditulis sebagai sorted(data, True).",
                    "",
                    "Bintang telanjang wajib punya parameter sesudahnya; def f(a, *): langsung",
                    "SyntaxError: named arguments must follow bare *.",
                    "",
                    "Kebalikannya adalah tanda / (Python 3.8+): semua parameter SEBELUMNYA cuma boleh",
                    "dikirim lewat posisi, namanya tidak boleh disebut.",
                    "",
                    "  def bagi(a, b, /, bulat=False):",
                    "      ...",
                    "  bagi(7, 2)               OK",
                    "  bagi(7, 2, bulat=True)   OK   (bulat ada SESUDAH /, jadi bebas)",
                    "  bagi(a=7, b=2)",
                    "  TypeError: bagi() got some positional-only arguments passed as keyword",
                    "  arguments: 'a, b'",
                    "",
                    "Gunanya: nama a dan b jadi bukan bagian dari janji fungsimu, jadi boleh diganti kapan",
                    "saja tanpa merusak kode orang yang memanggilnya.",
                    "",
                    "Ini juga yang menjelaskan keluaran help() yang tadinya terlihat aneh:",
                    "  help(len)     -> len(obj, /)",
                    "  help(sorted)  -> sorted(iterable, /, *, key=None, reverse=False)",
                    "  help(round)   -> round(number, ndigits=None)   (tanpa / dan *: bebas dua-duanya)",
                    "",
                    "Baca baris sorted tadi begini: iterable wajib posisi, key dan reverse wajib pakai nama.",
                    "Itu pula sebabnya len(obj=[1, 2]) gagal dengan TypeError: len() takes no keyword",
                    "arguments, padahal help()-nya jelas-jelas menyebut nama 'obj'.",
                    "",
                    "Aturan ini tetap berlaku untuk argumen hasil pembongkaran. Key dict yang tidak cocok",
                    "dengan nama parameter mana pun langsung ditolak:",
                    "  buat_koneksi(**{\"host\": \"x\", \"port\": 80})",
                    "  TypeError: buat_koneksi() got an unexpected keyword argument 'port'",
                ],
            },
        ],
    },
    {
        "title": "17. Anotasi Tipe (Type Hint)",
        "sections": [
            {
                "body": [
                    "Anotasi tipe = catatan di dalam kode yang menyebutkan TIPE sebuah nilai.",
                    "Python tetap dynamically typed (lihat materi Variabel & Tipe Data): anotasi",
                    "TIDAK mengubah cara program berjalan sedikit pun. Ia ada untuk MANUSIA yang",
                    "membaca kode dan untuk alat pemeriksa. Materi Function sudah menyinggungnya",
                    "sekilas; di sini kita bedah sampai bisa dibaca lancar.",
                    "",
                    "Kenapa perlu dikuasai: baris tanda tangan fungsi adalah hal PERTAMA yang",
                    "kamu baca saat membuka kode orang lain, dan di project Python modern baris",
                    "itu hampir selalu beranotasi. Kalau bentuknya asing, kamu berhenti di baris",
                    "pertama padahal isinya justru penjelasan paling padat soal fungsi itu.",
                    "",
                    "Bacalah baris ini pelan-pelan:",
                    "",
                    "  def cari(nama: str, umur: int | None = None) -> list[Pengguna]:",
                    "",
                    "  nama: str          -> parameter nama diharapkan berupa str",
                    "  umur: int | None   -> boleh int, boleh None (tanda | dibaca 'atau')",
                    "  = None             -> nilai default; INI yang membuat argumennya opsional",
                    "  -> list[Pengguna]  -> yang dikembalikan: list berisi objek Pengguna",
                    "",
                    "Jadi polanya cuma dua: titik dua untuk tipe sebuah nama, dan panah -> untuk",
                    "tipe nilai yang dikembalikan.",
                    "",
                    "Anotasi juga boleh dipasang pada variabel biasa dan atribut objek:",
                    "  jumlah: int = 0",
                    "  nama: str = \"Andi\"",
                    "  self.saldo: float = 0.0",
                    "",
                    "-> None dipakai untuk fungsi yang kerjanya hanya MELAKUKAN sesuatu (mencetak,",
                    "menyimpan, mengirim) tanpa memberi nilai balik. Fungsi tanpa return di Python",
                    "tetap mengembalikan None, jadi None memang tipe hasilnya - bukan 'kosong'.",
                ],
            },
            {
                "heading": "Anotasi dasar, dan bukti bahwa Python tidak memaksakannya",
                "code": """# Anotasi tipe: titik dua untuk variabel/parameter, panah untuk nilai kembali
jumlah: int = 0
nama: str = "Andi"
harga: float = 15000.5

def tambah(a: int, b: int) -> int:
    return a + b

def sapa(orang: str) -> None:      # -> None: fungsi ini tidak mengembalikan apa-apa
    print(f"Halo, {orang}!")

sapa(nama)
jumlah = tambah(3, 4)
print(jumlah, harga)               # 7 15000.5

# Anotasi cuma DICATAT sebagai data biasa, tidak pernah jadi aturan:
print(tambah.__annotations__)
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

# Buktinya: kirim str ke parameter yang ditulis int -- Python diam saja
print(tambah("3", "4"))            # 34, bukan 7 dan bukan error""",
            },
            {
                "body": [
                    "Tipe koleksi ditulis dengan kurung siku yang menyebut ISINYA:",
                    "",
                    "  list[int]             list berisi bilangan bulat",
                    "  list[str]             list berisi teks",
                    "  dict[str, int]        dict dengan kunci str dan nilai int",
                    "  set[str]              set berisi teks",
                    "  tuple[str, int]       tuple 2 elemen: teks lalu int (POSISI menentukan)",
                    "  tuple[int, ...]       tuple berisi int, jumlah elemennya bebas",
                    "  list[dict[str, int]]  boleh bersarang sedalam yang perlu",
                    "",
                    "Dua bentuk tuple itu sengaja berbeda: tuple[str, int] adalah pasangan tetap",
                    "(nama, umur), sedangkan tuple[int, ...] adalah 'sekumpulan int, berapa pun",
                    "banyaknya'. Tanda ... di situ bagian dari tipenya, bukan kode yang belum ditulis.",
                    "",
                    "BENTUK LAMA yang masih sangat sering kamu temui:",
                    "Sebelum Python 3.9, list dan dict bawaan belum boleh diberi kurung siku, jadi",
                    "tipe koleksi diambil dari modul typing dan ditulis berhuruf besar:",
                    "",
                    "  from typing import List, Dict, Any",
                    "",
                    "  def proses(data: List[int]) -> Dict[str, Any]:    # gaya lama",
                    "  def proses(data: list[int]) -> dict[str, Any]:    # gaya sekarang",
                    "",
                    "Artinya sama persis. Any tetap diambil dari typing karena tidak punya padanan",
                    "bawaan. Jangan bingung melihat dua gaya ini bercampur di satu project.",
                    "",
                    "Beda versi yang perlu diingat saat menyalin kode dari internet:",
                    "",
                    "  list[int], dict[str, int]    butuh Python 3.9+",
                    "  int | None, int | str        butuh Python 3.10+",
                    "  List[int], Optional[int]     jalan di semua versi (dari typing)",
                    "",
                    "Kalau kode harus jalan di Python lama, tulis baris ini di paling atas berkas:",
                    "  from __future__ import annotations",
                    "Anotasi jadi disimpan sebagai teks dan tidak dievaluasi, sehingga sintaks baru",
                    "boleh dipakai DI DALAM anotasi - tapi tidak di tempat lain.",
                ],
            },
            {
                "heading": "Optional, Union, Callable, dan forward reference",
                "code": """from typing import Any, Callable, Optional, Sequence, Union

def cari_nama(user_id: int) -> Optional[str]:
    # Optional[str] = str ATAU None. Sejak 3.10 boleh ditulis str | None.
    daftar = {1: "Andi", 2: "Budi"}
    return daftar.get(user_id)          # .get() memang bisa mengembalikan None

def rata_rata(angka: Sequence[float]) -> float:
    # Sequence = bisa di-index dan di-len: list, tuple, str (set tidak)
    return sum(angka) / len(angka)

def terapkan(data: Sequence[int], fungsi: Callable[[int], int]) -> list[int]:
    # Callable[[int], int] = fungsi yang menerima satu int, mengembalikan int
    return [fungsi(x) for x in data]

def tampilkan(nilai: Union[int, str]) -> None:   # sama artinya dengan int | str
    print("nilai:", nilai)

def ringkas(data: dict[str, Any]) -> str:
    # Any = "isinya apa saja, jangan diperiksa" -- pintu darurat, jangan diobral
    return ", ".join(f"{k}={v}" for k, v in data.items())

class Node:
    def __init__(self, nilai: int) -> None:
        self.nilai = nilai
        self.berikut: Optional["Node"] = None   # "Node" belum jadi -> pakai kutip

    def sambung(self, nilai: int) -> "Node":    # forward reference, alasan sama
        self.berikut = Node(nilai)
        return self.berikut

print(cari_nama(1))                  # Andi
print(cari_nama(99))                 # None  <- inilah yang diwakili Optional
print(rata_rata([80, 90, 100]))      # 90.0
print(terapkan([1, 2, 3], lambda x: x * 10))   # [10, 20, 30]
tampilkan(7)
tampilkan("tujuh")
print(ringkas({"nama": "Andi", "umur": 20, "aktif": True}))

kepala = Node(1)
kepala.sambung(2).sambung(3)
print(kepala.nilai, kepala.berikut.nilai, kepala.berikut.berikut.nilai)  # 1 2 3""",
            },
            {
                "body": [
                    "Isi baris 'from typing import ...' yang paling sering nongol di puncak berkas:",
                    "",
                    "  Any        tipe apa pun; mematikan pemeriksaan untuk nilai itu",
                    "  Optional   Optional[X] sama dengan X | None",
                    "  Union      Union[A, B] sama dengan A | B",
                    "  Callable   Callable[[int, str], bool] = fungsi(int, str) yang hasilnya bool",
                    "  Iterable   apa saja yang bisa di-for: list, tuple, set, generator",
                    "  Sequence   yang bisa di-index dan di-len: list, tuple, str (set TIDAK)",
                    "  TypeAlias  penanda bahwa sebuah nama adalah nama lain untuk sebuah tipe",
                    "",
                    "Kenapa parameter sering ditulis Iterable/Sequence dan bukan list? Karena",
                    "fungsinya cuma butuh 'sesuatu yang bisa di-for'; menulis list[int] berarti",
                    "menolak tuple dan generator tanpa alasan. Untuk nilai KEMBALI sebaliknya:",
                    "sebutkan yang paling konkret (list[int]) supaya pemanggil tahu apa yang dipegang.",
                    "",
                    "Nama pendek untuk tipe yang panjang (type alias):",
                    "  from typing import TypeAlias",
                    "  Matriks: TypeAlias = list[list[float]]",
                    "  def transpose(m: Matriks) -> Matriks:      # jauh lebih enak dibaca",
                    "  (Python 3.12+ punya bentuk lebih ringkas: type Matriks = list[list[float]])",
                    "",
                    "SIAPA yang memeriksa anotasi? Bukan Python. Alatnya terpisah - mypy, yang",
                    "sudah disebut di materi Virtual Environment, pip & Testing. Ia membaca kode",
                    "TANPA menjalankannya, lalu mengadukan anotasi yang tidak cocok:",
                    "",
                    "  pip install mypy",
                    "  mypy program.py",
                    "",
                    "  program.py:19: error: Argument 1 to \"tambah\" has incompatible type \"str\";",
                    "  expected \"int\"",
                    "  Found 1 error in 1 file (checked 1 source file)",
                    "",
                    "Editor seperti VS Code memakai anotasi yang sama untuk autocomplete dan",
                    "garis merah, jadi anotasi terbayar bahkan sebelum kamu memasang mypy.",
                    "",
                    "JEBAKAN yang sungguh menjebak:",
                    "",
                    "  1. Anotasi tanpa nilai TIDAK membuat variabel.",
                    "       umur: int",
                    "       print(umur)    # NameError: name 'umur' is not defined",
                    "     Baris itu cuma mencatat 'kalau nanti ada umur, tipenya int'.",
                    "",
                    "  2. Optional BUKAN berarti 'argumennya boleh tidak diisi'.",
                    "       def simpan(nama: Optional[str]) -> None:",
                    "     Argumen nama tetap WAJIB diisi; yang boleh None adalah NILAInya.",
                    "     Yang membuat sebuah argumen boleh dilewati hanyalah nilai default.",
                    "",
                    "  3. def kirim(pesan: str = None) adalah salah tulis yang sangat umum:",
                    "     defaultnya None padahal tipenya ditulis str. Yang benar:",
                    "       def kirim(pesan: str | None = None) -> None:",
                    "",
                    "  4. Anotasi yang BOHONG lebih berbahaya daripada tanpa anotasi. Fungsi",
                    "     ditulis -> int tapi diam-diam kadang mengembalikan None: pembaca percaya,",
                    "     mypy percaya, dan yang meledak justru kode pemanggilnya.",
                    "",
                    "  5. Tipe berkurung siku tidak bisa dipakai di isinstance:",
                    "       isinstance(data, list[int])",
                    "       # TypeError: isinstance() argument 2 cannot be a parameterized generic",
                    "       isinstance(data, list)      # ini yang benar",
                    "",
                    "  6. Nama class yang belum selesai dibuat ditulis dalam tanda kutip (\"Node\"),",
                    "     karena saat baris def itu dibaca, class-nya memang belum ada. Sejak",
                    "     Python 3.14 kutipnya tidak lagi wajib, tapi kode yang beredar hari ini",
                    "     penuh bentuk berkutip itu - kamu tetap perlu mengenalinya.",
                ],
            },
        ],
    },
    {
        "title": "18. Lambda & Higher-Order Function",
        "sections": [
            {
                "body": [
                    "Lambda = fungsi anonim (tanpa nama) yang ringkas, untuk logika",
                    "SEDERHANA satu baris. Mirip arrow function di JS / lambda di Java.",
                    "",
                    "Sintaks:",
                    "  lambda parameter: ekspresi",
                    "",
                    "  tambah = lambda a, b: a + b",
                    "  print(tambah(3, 4))     # 7",
                    "",
                    "  kuadrat = lambda x: x ** 2",
                    "  print(kuadrat(5))       # 25",
                    "",
                    "Lambda paling sering dipakai sebagai ARGUMEN untuk fungsi lain",
                    "(higher-order function), bukan disimpan ke variabel seperti di atas.",
                ]
            },
            {
                "heading": "map, filter, reduce, sorted dengan lambda",
                "code": """angka = [5, 3, 8, 1, 9, 2]

# map: transformasi tiap elemen
dikali2 = list(map(lambda x: x * 2, angka))
print(dikali2)    # [10, 6, 16, 2, 18, 4]

# filter: menyaring elemen sesuai kondisi
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)      # [8, 2]

# reduce: gabungkan semua elemen jadi satu nilai (perlu import)
from functools import reduce
total = reduce(lambda a, b: a + b, angka)
print(total)      # 28

# sorted dengan key (lambda menentukan dasar pengurutan)
mahasiswa = [("Andi", 85), ("Budi", 70), ("Citra", 95)]
urut = sorted(mahasiswa, key=lambda m: m[1], reverse=True)
print(urut)       # [('Citra', 95), ('Andi', 85), ('Budi', 70)]"""
            },
            {
                "body": [
                    "Kenapa tiap map() dan filter() di atas dibungkus list()? Karena",
                    "keduanya TIDAK mengembalikan list. Yang keluar adalah ITERATOR - objek",
                    "yang menyiapkan hasilnya satu per satu saat diminta, bukan sekaligus",
                    "di depan:",
                    "",
                    "  print(map(lambda x: x * 2, angka))",
                    "  -> <map object at 0x7f3a1c0d5e40>",
                    "",
                    "Itu bukan error dan bukan list yang gagal tercetak; memang begitulah",
                    "wujud objeknya. list() yang meminta seluruh isinya keluar sekarang juga.",
                    "Kalau hasilnya cuma mau di-for-loop sekali, list() malah tidak perlu.",
                    "Dan konsekuensi yang sama dengan zip() di materi Fungsi Bawaan untuk",
                    "Koleksi berlaku persis di sini: isinya HABIS sekali pakai.",
                    "",
                    "Alasan serupa membuat mahasiswa.keys() di materi Dictionary & Set",
                    "tercetak sebagai dict_keys([...]), bukan list biasa. Bedanya .keys(),",
                    ".values(), dan .items() memberi VIEW - jendela yang selalu menampilkan",
                    "isi dict saat itu juga, dan boleh dilihat berkali-kali. Sama-sama bukan",
                    "list, sama-sama tinggal dibungkus list() kalau memang butuh list.",
                    "Mesin di balik keduanya dibahas di materi Iterator & Generator.",
                ]
            },
            {
                "body": [
                    "Kapan pakai lambda vs def biasa:",
                    "  - Lambda: logika singkat, sekali pakai, sebagai argumen.",
                    "  - def: logika lebih dari satu baris, dipakai berkali-kali,",
                    "    atau butuh nama yang jelas untuk keterbacaan.",
                    "",
                    "PEP 8 (panduan gaya kode Python resmi) menyarankan TIDAK",
                    "menyimpan lambda ke variabel (pakai def saja untuk itu):",
                    "  X  kuadrat = lambda x: x ** 2",
                    "  V  def kuadrat(x): return x ** 2",
                ]
            },
        ],
    },
    {
        "title": "19. Scope, Closure & nonlocal",
        "sections": [
            {
                "body": [
                    "Materi Function sudah menyebut dua tingkat: variabel LOKAL milik fungsi dan",
                    "variabel GLOBAL milik modul. Kenyataannya Python punya EMPAT tingkat, dan yang",
                    "ketiga - tingkat 'enclosing' - hampir tidak pernah dibicarakan padahal justru ia",
                    "yang membuat decorator, callback, dan factory function bisa bekerja.",
                    "",
                    "Kenapa scope ada sama sekali. Sebuah program berisi ribuan nama. Kalau semuanya",
                    "tinggal di satu tempat, variabel i yang kamu tulis hari ini menimpa i yang",
                    "ditulis orang lain bulan lalu, tanpa satu pun tanda di layar. Scope adalah",
                    "aturan yang membuat nama sama di dua tempat tetap dua barang yang berbeda.",
                    "",
                    "Aturan pencarian nama di Python bernama LEGB. Saat sebuah nama DIBACA, Python",
                    "menengok empat tempat BERURUTAN dan berhenti di yang pertama ketemu:",
                    "",
                    "  L  Local      nama di dalam fungsi yang sedang berjalan",
                    "  E  Enclosing  nama milik fungsi PEMBUNGKUS, kalau fungsi ini bersarang",
                    "  G  Global     nama di tingkat modul, yaitu berkas .py yang sedang jalan",
                    "  B  Built-in   nama bawaan Python: print, len, sum, str, list, range, ...",
                    "",
                    "Kalau sampai B pun tidak ketemu, barulah NameError.",
                    "",
                    "Dua akibat yang langsung terasa waktu kamu membaca kode orang:",
                    "  - Nama di tingkat lebih dalam MENUTUPI (shadow) nama di tingkat luar. Menamai",
                    "    variabel list, id, atau sum mematikan fungsi bawaannya - tapi hanya di dalam",
                    "    scope itu, sehingga errornya sering muncul jauh dari penyebabnya.",
                    "  - MEMBACA nama dari scope luar tidak butuh izin apa pun. MENUGASKAN ulang",
                    "    butuh izin eksplisit: global atau nonlocal. Tanpa izin itu, penugasan selalu",
                    "    membuat variabel BARU yang lokal - dan itu asal-usul UnboundLocalError.",
                ],
            },
            {
                "heading": "LEGB dalam satu program, dan error scope yang paling sering muncul",
                "code": """# Python mencari sebuah NAMA di empat tempat, berurutan, dan berhenti begitu
# ketemu: Local -> Enclosing -> Global -> Built-in. Itulah aturan LEGB.

pesan = "aku Global"              # G: nama tingkat modul

def luar():
    pesan = "aku Enclosing"       # E: lokal milik luar(), enclosing bagi dalam()

    def dalam():
        pesan = "aku Local"       # L: lokal milik dalam()
        print("dari dalam():", pesan)

    dalam()
    print("dari luar() :", pesan)  # tidak ikut berubah: dalam() punya kotaknya sendiri

luar()
print("dari modul  :", pesan)
# dari dalam(): aku Local
# dari luar() : aku Enclosing
# dari modul  : aku Global

# Hilangkan satu tingkat, pencariannya lanjut ke tingkat berikutnya.
def luar2():
    pesan = "aku Enclosing"

    def dalam2():
        print("dalam2 melihat :", pesan)   # tak ada L -> naik ke E

    dalam2()

luar2()

def sendirian():
    print("sendirian melihat:", pesan)     # tak ada L, tak ada E -> G

sendirian()
# dalam2 melihat : aku Enclosing
# sendirian melihat: aku Global

# B = Built-in: print, len, sum, str, list ... tinggal di tingkat paling luar.
# Karena L menang atas B, memakai ulang nama bawaan mematikan fungsi bawaannya
# DI DALAM fungsi itu:
def hitung(daftar):
    len = 99                 # mulai baris ini, len adalah int lokal
    # return len(daftar)     # TypeError: 'int' object is not callable
    return len

print("hitung([1,2,3]) =", hitung([1, 2, 3]))         # 99, bukan 3
print("di luar, len masih fungsi:", len([1, 2, 3]))   # 3

# Jebakan nomor satu soal scope. MENUGASKAN sebuah nama di mana pun di dalam
# fungsi membuat nama itu lokal untuk SELURUH badan fungsi - termasuk di
# baris-baris sebelum penugasannya.
skor = 10

def naikkan():
    print(skor)        # baris ini yang meledak
    skor = skor + 1    # gara-gara baris INI

try:
    naikkan()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
# UnboundLocalError: cannot access local variable 'skor' where it is not associated
# with a value
# (Python 3.10 ke bawah menulisnya "local variable 'skor' referenced before
#  assignment" - maksudnya sama persis.)

# Bacalah pesan itu sebagai: "kamu menugaskan skor di fungsi ini, jadi skor lokal,
# dan kamu membacanya sebelum sempat diisi." Perbaikannya bukan menghapus print,
# tapi memutuskan siapa pemilik skor - lihat bagian global vs nonlocal di bawah.""",
            },
            {
                "heading": "Closure: fungsi yang mencetak fungsi, dan pencacah dengan nonlocal",
                "code": """# Closure = fungsi dalam yang TETAP MENGINGAT variabel fungsi luarnya, bahkan
# setelah fungsi luar itu selesai dan variabel lokalnya "seharusnya" lenyap.

def pembuat_pengali(faktor):
    def kali(x):
        return x * faktor      # faktor bukan milik kali(); ia datang dari E
    return kali                # fungsinya DIKEMBALIKAN, bukan dipanggil

kali3 = pembuat_pengali(3)     # pembuat_pengali sudah SELESAI di baris ini
kali10 = pembuat_pengali(10)

print(kali3(5), kali10(5))     # 15 50

# Kenapa faktor masih ada? Karena masih ada fungsi yang menyebutnya, jadi Python
# menyimpannya di sebuah "cell" yang menempel pada fungsi itu. Bisa dilihat:
print(kali3.__code__.co_freevars)             # ('faktor',)
print(kali3.__closure__[0].cell_contents)     # 3
print(kali10.__closure__[0].cell_contents)    # 10
# Dua fungsi, dua kotak terpisah - kali3 dan kali10 tidak saling mengganggu.
# Fungsi yang tidak mengambil apa pun dari luar punya __closure__ bernilai None:
print((lambda x: x + 1).__closure__)          # None

# ---------------------------------------------------------------------------
# Pencacah tanpa satu pun variabel global.

def buat_pencacah(mulai=0):
    hitung = mulai

    def tambah(langkah=1):
        nonlocal hitung        # "hitung milik fungsi PEMBUNGKUS, bukan punyaku"
        hitung += langkah      # tanpa baris nonlocal di atas -> UnboundLocalError
        return hitung

    def lihat():
        return hitung          # cuma MEMBACA -> nonlocal tidak diperlukan

    return tambah, lihat

tambah_a, lihat_a = buat_pencacah()
tambah_b, lihat_b = buat_pencacah(100)

print(tambah_a(), tambah_a(), tambah_a())   # 1 2 3
print(tambah_b(5))                          # 105
print(lihat_a(), lihat_b())                 # 3 105

# Bandingkan dengan versi 'global' di materi Function: di sana hitung tinggal di
# tingkat modul - terlihat dan bisa diubah SIAPA SAJA di berkas itu, dan dua
# pencacah mustahil hidup berdampingan. Di sini hitung tak bisa disentuh dari
# luar kecuali lewat tambah() dan lihat(); namanya bahkan tidak ada di modul.
print("hitung" in dir())                    # False""",
            },
            {
                "body": [
                    "global vs nonlocal. Keduanya berkata 'jangan bikin variabel baru, pakai yang",
                    "sudah ada', tapi menunjuk tempat yang berbeda:",
                    "",
                    "                  menunjuk ke                dipakai di",
                    "  global x        tingkat MODUL              fungsi mana pun",
                    "  nonlocal x      fungsi PEMBUNGKUS terdekat hanya di fungsi bersarang",
                    "",
                    "Aturan mainnya, sekaligus jebakannya:",
                    "  - nonlocal MENUNTUT namanya sudah ada di salah satu fungsi pembungkus. Kalau",
                    "    tidak ada, Python menolak berkasnya sebelum sebaris pun dijalankan:",
                    "      SyntaxError: no binding for nonlocal 'x' found",
                    "    Perhatikan itu SyntaxError, bukan error saat jalan - jadi yang gagal dimuat",
                    "    seluruh berkas, bukan cuma fungsi itu.",
                    "  - nonlocal tidak pernah sampai ke tingkat modul. Untuk itu memang global.",
                    "  - global di dalam fungsi bersarang MELOMPATI tingkat enclosing, langsung ke",
                    "    modul. Jadi keduanya bukan versi kuat-lemah, melainkan tujuan berbeda.",
                    "",
                    "Kapan nonlocal TIDAK diperlukan - ini sumber kebingungan yang lazim:",
                    "  - Kalau kamu cuma MEMBACA. 'return hitung' tidak butuh izin apa pun.",
                    "  - Kalau kamu MEMUTASI objeknya, bukan menugaskan ulang namanya:",
                    "      data.append(x)   isi['k'] = 1   daftar[0] = 9    -> tidak butuh nonlocal",
                    "      hitung += 1      data = []                       -> butuh nonlocal",
                    "    Bedanya: baris atas mengubah ISI objek yang sudah ditunjuk namanya; baris",
                    "    bawah membuat nama itu menunjuk barang lain. Lihat materi Referensi Objek,",
                    "    Salinan & Jebakan Mutable. Karena itu banyak closure memakai list atau dict",
                    "    sebagai wadah keadaan dan tak pernah menyentuh nonlocal sama sekali.",
                    "",
                    "Dua scope yang sering mengagetkan pembaca kode:",
                    "  - Comprehension punya scope SENDIRI. [n * 2 for n in range(3)] tidak",
                    "    meninggalkan n di luar, sedangkan for biasa meninggalkannya.",
                    "  - Badan class BUKAN scope pembungkus bagi method di dalamnya. Method yang",
                    "    menulis 'faktor' polos kena NameError walau ada faktor = 3 di badan class;",
                    "    yang benar self.faktor atau NamaKelas.faktor.",
                    "",
                    "Di mana closure benar-benar muncul di kode nyata:",
                    "  - Decorator: wrapper mengingat fungsi yang dibungkusnya (materi Decorator).",
                    "  - Callback dan event handler: fungsi dititipkan sekarang, dipanggil nanti,",
                    "    dan tetap perlu tahu konteks saat ia dibuat.",
                    "  - Factory: satu fungsi mencetak banyak fungsi dengan setelan berbeda.",
                    "  - key= untuk sorted() yang dasar pengurutannya baru diketahui saat jalan.",
                    "",
                    "Kapan JANGAN pakai closure: begitu keadaannya lebih dari satu-dua nilai, atau",
                    "butuh lebih dari dua fungsi untuk mengurusnya, class lebih enak dibaca (materi",
                    "OOP: Class & Object). Closure berisi satu fungsi pada dasarnya class dengan satu",
                    "method - bedanya class memberi nama pada tiap bagiannya.",
                ],
            },
            {
                "heading": "Jebakan late binding, dan closure di balik decorator",
                "code": """# Closure menyimpan VARIABELnya, bukan nilai variabel itu saat closure dibuat.
# Nilainya baru dibaca ketika fungsinya DIPANGGIL. Itu namanya late binding,
# dan inilah akibatnya:

fungsi = [lambda: i for i in range(3)]
print([f() for f in fungsi])        # [2, 2, 2]  -- bukan [0, 1, 2]

# Ketiga lambda menunjuk ke SATU i yang sama. Waktu f() akhirnya dipanggil,
# loopnya sudah lama berhenti dan i bernilai 2.

# Bentuknya lebih sering muncul begini, dan lebih sulit dikenali:
salam = []
for nama in ["Andi", "Budi", "Citra"]:
    salam.append(lambda: f"Halo, {nama}!")
print([s() for s in salam])         # ['Halo, Citra!', 'Halo, Citra!', 'Halo, Citra!']

# Perbaikan 1: default argument. Nilainya dihitung SEKALI, saat lambda dibuat.
fungsi = [lambda i=i: i for i in range(3)]
print([f() for f in fungsi])        # [0, 1, 2]

# Perbaikan 2: factory. Tiap panggilan bikin() membuat scope BARU, dan tiap
# lambda menutup atas i milik panggilannya sendiri.
def bikin(i):
    return lambda: i

fungsi = [bikin(i) for i in range(3)]
print([f() for f in fungsi])        # [0, 1, 2]

# Perbaikan 1 paling ringkas, tapi ingat: default argument dievaluasi sekali saja
# - untuk nilai MUTABLE justru itu sumber jebakan yang lain (lihat materi
# Referensi Objek, Salinan & Jebakan Mutable).

# ---------------------------------------------------------------------------
# Dan inilah mesin di balik decorator: wrapper adalah closure yang mengingat
# 'fungsi' dan 'jumlah' dari scope pembungkusnya.

def hitung_panggilan(fungsi):
    jumlah = 0

    def wrapper(*args, **kwargs):
        nonlocal jumlah                 # satu penghitung, dipakai lintas panggilan
        jumlah += 1
        print(f"[{fungsi.__name__} dipanggil ke-{jumlah}]")
        return fungsi(*args, **kwargs)

    return wrapper

@hitung_panggilan
def sapa(nama):
    return f"Halo, {nama}"

print(sapa("Andi"))
print(sapa("Budi"))
# [sapa dipanggil ke-1]
# Halo, Andi
# [sapa dipanggil ke-2]
# Halo, Budi

# Nama sapa sekarang menunjuk ke wrapper, dan wrapper membawa dua tumpangan:
print(sapa.__code__.co_freevars)        # ('fungsi', 'jumlah')
# Tanpa closure, decorator mustahil: wrapper harus bisa menyebut fungsi aslinya
# padahal hitung_panggilan sudah lama selesai. Sintaks @ dan pemakaiannya
# dibahas tuntas di materi Decorator & Context Manager.""",
            },
        ],
    },
    {
        "title": "20. List Comprehension & Generator Expression",
        "sections": [
            {
                "body": [
                    "List comprehension = cara ringkas & 'Pythonic' membuat list",
                    "dari sebuah iterable, menggantikan for-loop yang lebih panjang.",
                    "",
                    "Sintaks dasar:",
                    "  [ekspresi for item in iterable]",
                    "  [ekspresi for item in iterable if kondisi]",
                    "",
                    "Cara biasa (for-loop):        Cara comprehension:",
                    "  hasil = []                    hasil = [x**2 for x in range(5)]",
                    "  for x in range(5):",
                    "      hasil.append(x**2)",
                ]
            },
            {
                "heading": "Contoh list & dict comprehension",
                "code": """# List comprehension sederhana
kuadrat = [x**2 for x in range(1, 6)]
print(kuadrat)    # [1, 4, 9, 16, 25]

# Dengan kondisi (filter)
genap = [x for x in range(1, 11) if x % 2 == 0]
print(genap)      # [2, 4, 6, 8, 10]

# Dengan transformasi + kondisi sekaligus
label = ["genap" if x % 2 == 0 else "ganjil" for x in range(1, 6)]
print(label)      # ['ganjil', 'genap', 'ganjil', 'genap', 'ganjil']

# Nested (matriks jadi list datar)
matriks = [[1, 2], [3, 4], [5, 6]]
datar = [nilai for baris in matriks for nilai in baris]
print(datar)      # [1, 2, 3, 4, 5, 6]

# Dict comprehension
nama = ["andi", "budi", "citra"]
panjang = {n: len(n) for n in nama}
print(panjang)    # {'andi': 4, 'budi': 4, 'citra': 6}"""
            },
            {
                "body": [
                    "Generator expression: sintaks MIRIP list comprehension tapi",
                    "pakai kurung () bukan [], dan TIDAK langsung membuat semua",
                    "elemen di memori - dihasilkan 'malas' (lazy) satu per satu.",
                    "",
                    "  kuadrat_list = [x**2 for x in range(1000000)]   # buat semua di RAM",
                    "  kuadrat_gen  = (x**2 for x in range(1000000))   # hemat memori!",
                    "",
                    "Kapan pakai generator expression:",
                    "  - Data SANGAT besar, tidak perlu semuanya sekaligus di memori.",
                    "  - Hanya perlu diproses SEKALI secara berurutan (misal dengan sum()).",
                    "    total = sum(x**2 for x in range(1000000))  # hemat RAM",
                    "",
                    "Generator dibahas lebih dalam di materi Iterator & Generator.",
                ]
            },
        ],
    },
    {
        "title": "21. OOP: Class & Object",
        "sections": [
            {
                "body": [
                    "Class = blueprint/cetakan. Object = hasil dari class (instance).",
                    "",
                    "Sintaks dasar class di Python:",
                    "  class NamaClass:",
                    "      def __init__(self, param):    # constructor",
                    "          self.atribut = param",
                    "",
                    "      def method(self):             # method biasa",
                    "          print(self.atribut)",
                    "",
                    "  self  -> merujuk ke objek itu sendiri (WAJIB jadi parameter",
                    "           pertama tiap method, tapi TIDAK ditulis saat memanggil).",
                    "  __init__ -> constructor, otomatis dipanggil saat objek dibuat.",
                ]
            },
            {
                "heading": "Contoh class & object",
                "code": """class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama      # atribut/attribute
        self.umur = umur

    def perkenalan(self):     # method
        print(f"Halo, saya {self.nama}, {self.umur} tahun.")

# Membuat object (instance)
m1 = Mahasiswa("Andi", 20)
m2 = Mahasiswa("Budi", 22)

m1.perkenalan()   # Halo, saya Andi, 20 tahun.
m2.perkenalan()   # Halo, saya Budi, 22 tahun.

print(m1.nama)    # Andi (akses atribut langsung)"""
            },
            {
                "body": [
                    "Class attribute vs instance attribute:",
                    "  class Mahasiswa:",
                    "      kampus = \"Universitas ABC\"   # class attribute (dibagi SEMUA objek)",
                    "      def __init__(self, nama):",
                    "          self.nama = nama            # instance attribute (per objek)",
                    "",
                    "  m1 = Mahasiswa(\"Andi\")",
                    "  print(m1.kampus)    # Universitas ABC (diwarisi dari class)",
                    "  print(Mahasiswa.kampus)  # bisa diakses lewat class langsung",
                    "",
                    "Method static & class method:",
                    "  @staticmethod  -> tidak butuh self maupun cls. Fungsi biasa yang",
                    "                    kebetulan tinggal di dalam namespace class.",
                    "  @classmethod   -> menerima cls (CLASS-nya), bukan self. Paling sering",
                    "                    dipakai untuk membuat objek lewat jalan lain.",
                    "",
                    "Tanda @ di atas def itu namanya DECORATOR: sebuah penanda yang mengubah",
                    "cara Python memperlakukan def di bawahnya. Di sini cukup tahu efeknya;",
                    "cara kerjanya dan cara membuat decorator sendiri dibahas tuntas di",
                    "materi Decorator & Context Manager.",
                ]
            },
            {
                "heading": "self, cls, dan tanpa keduanya - dalam satu class yang utuh",
                "code": """class Suhu:
    satuan = "Celsius"                 # class attribute, dibagi semua objek

    def __init__(self, derajat):
        self.derajat = derajat         # instance attribute, milik tiap objek

    def ringkas(self):                 # METHOD BIASA - butuh objeknya (self)
        return f"{self.derajat} {Suhu.satuan}"

    @classmethod
    def dari_string(cls, teks):        # menerima CLASS-nya (cls), bukan objek
        return cls(float(teks.replace(",", ".")))

    @staticmethod
    def beku(derajat):                 # tidak butuh objek maupun class
        return derajat <= 0


s = Suhu(27.5)
print(s.ringkas())            # 27.5 Celsius

# classmethod dipanggil lewat CLASS, dan mengembalikan objek Suhu yang baru.
lain = Suhu.dari_string("31,2")
print(type(lain).__name__, lain.ringkas())   # Suhu 31.2 Celsius

# staticmethod boleh lewat class maupun lewat objek; hasilnya sama saja.
print(Suhu.beku(-3), s.beku(-3))             # True True

# Bedanya baru terasa kalau method biasa dipanggil tanpa objek:
try:
    Suhu.ringkas()
except TypeError as e:
    print("TypeError:", e)
# TypeError: Suhu.ringkas() missing 1 required positional argument: 'self'
# (di Python lama namanya tercetak 'ringkas()' saja - isinya sama)"""
            },
        ],
    },
    {
        "title": "22. OOP: Inheritance & Polymorphism",
        "sections": [
            {
                "body": [
                    "Inheritance = class anak mewarisi atribut & method dari class induk.",
                    "  class Anak(Induk):",
                    "      ...",
                    "",
                    "super() dipakai untuk memanggil constructor/method class induk.",
                ]
            },
            {
                "heading": "Contoh inheritance & override (polymorphism)",
                "code": """class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} bersuara.")

class Kucing(Hewan):
    def bersuara(self):          # override method induk
        print(f"{self.nama}: Meong!")

class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)   # panggil constructor induk
        self.ras = ras

    def bersuara(self):
        print(f"{self.nama} ({self.ras}): Guk!")

hewan_hewan = [Kucing("Tom"), Anjing("Bobby", "Herder")]
for h in hewan_hewan:
    h.bersuara()     # method yang dipanggil sesuai class ASLI objek (polymorphism)
# Tom: Meong!
# Bobby (Herder): Guk!"""
            },
            {
                "body": [
                    "Multiple inheritance: Python (BEDA dari Java) MENGIZINKAN",
                    "satu class mewarisi dari BANYAK class sekaligus:",
                    "  class C(A, B):",
                    "      pass",
                    "  Method Resolution Order (MRO) menentukan urutan pencarian",
                    "  method jika ada nama yang sama di beberapa induk.",
                    "  Cek dengan: C.__mro__ atau C.mro()",
                    "",
                    "isinstance() & issubclass():",
                    "  isinstance(kucing, Hewan)     -> True (Kucing adalah Hewan)",
                    "  issubclass(Kucing, Hewan)     -> True",
                    "",
                    "Duck typing (filosofi Python): 'jika berjalan seperti bebek",
                    "dan bersuara seperti bebek, maka anggap itu bebek' - Python",
                    "tidak terlalu ketat soal tipe, yang penting objek punya",
                    "method/perilaku yang dibutuhkan (tidak WAJIB inheritance formal).",
                ]
            },
        ],
    },
    {
        "title": "23. Abstract Base Class & Kontrak Antar-Class",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menutup dengan duck typing: Python tidak menuntut pewarisan, yang",
                    "penting objeknya punya method yang dibutuhkan. Itu enak sampai program membesar dan",
                    "ada class lain - punyamu bulan depan, atau punya orang lain - yang harus bisa dipakai",
                    "di tempat yang sama. Muncul pertanyaan yang tidak dijawab duck typing: bagaimana cara",
                    "MEMASTIKAN sebuah class punya method wajibnya, sebelum kodenya terlanjur jalan?",
                    "",
                    "Abstract base class (ABC) adalah jawaban bakunya. ABC adalah class yang sengaja dibuat",
                    "TIDAK LENGKAP: isinya sebagian besar cuma daftar nama method yang HARUS ditulis oleh",
                    "turunannya. Ini padanan Python untuk interface di Java, yang berkali-kali dipakai",
                    "sebagai pembanding di materi OOP sebelumnya.",
                    "",
                    "Bentuknya, dan kamu akan sering menemuinya saat membaca kode orang:",
                    "",
                    "  from abc import ABC, abstractmethod",
                    "",
                    "  class Penyimpan(ABC):              # ABC datang dari modul bawaan abc",
                    "      @abstractmethod                # penanda: WAJIB ditulis ulang turunannya",
                    "      def simpan(self, kunci, nilai):",
                    "          pass                       # badan kosong; boleh juga ditulis  ...",
                    "",
                    "Bagian yang paling sering salah dibaca pemula ada di baris terakhir itu. Badan pass",
                    "atau ... di situ BUKAN tanda kodenya belum selesai ditulis atau ditinggalkan setengah",
                    "jalan. Justru sebaliknya: badannya memang tidak boleh berisi apa-apa, karena yang",
                    "bertugas menulis isinya adalah class turunan, bukan class ini. Konsekuensinya class",
                    "ini juga tidak boleh dibuat objeknya sama sekali - Penyimpan() akan gagal, dan itu",
                    "kegagalan yang disengaja.",
                ],
            },
            {
                "heading": "Satu kontrak, dua implementasi, dan dua penolakan",
                "code": "from abc import ABC, abstractmethod\n\n\nclass Penyimpan(ABC):\n    \"\"\"Kontrak: apa pun yang menyimpan catatan wajib bisa simpan & ambil.\"\"\"\n\n    @abstractmethod\n    def simpan(self, kunci, nilai):\n        pass\n\n    @abstractmethod\n    def ambil(self, kunci):\n        pass\n\n    def simpan_banyak(self, pasangan):    # method BIASA, isinya sudah lengkap\n        for kunci, nilai in pasangan:\n            self.simpan(kunci, nilai)     # memakai method yang belum ditulis\n\n\nclass PenyimpanMemori(Penyimpan):         # implementasi konkret pertama\n    def __init__(self):\n        self.data = {}\n\n    def simpan(self, kunci, nilai):\n        self.data[kunci] = nilai\n\n    def ambil(self, kunci):\n        return self.data.get(kunci)\n\n\nclass PenyimpanBaris(Penyimpan):          # implementasi konkret kedua\n    def __init__(self):\n        self.baris = []\n\n    def simpan(self, kunci, nilai):\n        self.baris.append(f\"{kunci}={nilai}\")\n\n    def ambil(self, kunci):\n        for b in self.baris:\n            k, _, v = b.partition(\"=\")\n            if k == kunci:\n                return v\n        return None\n\n\nclass PenyimpanSetengahJadi(Penyimpan):\n    def simpan(self, kunci, nilai):       # method 'ambil' LUPA ditulis\n        print(\"disimpan:\", kunci)\n\n\n# Kode di bawah ini tidak peduli gudangnya jenis apa: kontraknya menjamin\n# simpan(), ambil(), dan simpan_banyak() PASTI ada di dua-duanya.\nfor gudang in (PenyimpanMemori(), PenyimpanBaris()):\n    gudang.simpan_banyak([(\"nama\", \"Levi\"), (\"kota\", \"Bontang\")])\n    print(type(gudang).__name__, \"->\", gudang.ambil(\"kota\"))\n\ntry:\n    Penyimpan()                 # class kontrak memang TIDAK boleh jadi objek\nexcept TypeError as e:\n    print(\"TypeError:\", e)\n\ntry:\n    PenyimpanSetengahJadi()      # turunan yang belum lengkap ikut ditolak\nexcept TypeError as e:\n    print(\"TypeError:\", e)\n\n# PenyimpanMemori -> Bontang\n# PenyimpanBaris -> Bontang\n# TypeError: Can't instantiate abstract class Penyimpan without an\n#            implementation for abstract methods 'ambil', 'simpan'\n# TypeError: Can't instantiate abstract class PenyimpanSetengahJadi without\n#            an implementation for abstract method 'ambil' (kalimat persisnya\n#            berbeda antar versi Python; yang penting nama method yang kurang)",
            },
            {
                "body": [
                    "Tiga hal yang perlu kamu tangkap dari program di atas:",
                    "",
                    "  1. Penyimpan() melempar TypeError. Bukan karena kodenya rusak, tapi karena itulah",
                    "     gunanya ABC: menutup pintu supaya kontrak tidak dipakai sebagai barang jadi.",
                    "  2. Pengecekannya terjadi saat MEMBUAT OBJEK, bukan saat class-nya dibaca Python.",
                    "     PenyimpanSetengahJadi yang kurang satu method tetap lolos didefinisikan; error",
                    "     baru meledak di baris yang mencoba membuat objeknya. Jadi kalau kode kamu tidak",
                    "     pernah membuat objek dari class itu, tidak akan pernah ada yang mengeluh.",
                    "  3. ABC boleh berisi method biasa yang sudah lengkap, seperti simpan_banyak. Pola",
                    "     ini sangat umum: induk menulis ALURNYA, turunan mengisi LANGKAH-langkahnya.",
                    "",
                    "Kalimat TypeError-nya berbeda antar versi Python (versi lama berbunyi 'with abstract",
                    "methods ambil, simpan'). Yang perlu kamu kenali kata kuncinya saja: abstract class,",
                    "lalu nama method yang belum diisi.",
                    "",
                    "Tiga jebakan yang sungguh sering kejadian:",
                    "",
                    "  - LUPA menulis (ABC). Kalau class-nya cuma  class Penyimpan:  maka @abstractmethod",
                    "    tidak melakukan APA-APA. Objeknya terbuat, method-nya boleh dipanggil, hasilnya",
                    "    None, tanpa satu pun pesan error. Jebakan paling mahal justru karena ia diam.",
                    "  - Urutan decorator kalau digabung dengan property: @property di ATAS,",
                    "    @abstractmethod tepat di bawahnya. Terbalik, kontraknya tidak terdaftar.",
                    "  - ABC hanya mengecek NAMA method-nya ada, bukan parameternya. Turunan yang menulis",
                    "    def simpan(self) padahal induknya def simpan(self, kunci, nilai) tetap lolos, dan",
                    "    errornya baru muncul nanti saat method itu dipanggil dengan dua argumen.",
                    "",
                    "Ada bentuk manual dari kontrak yang sama, tanpa modul abc, dan masih banyak ditemui",
                    "di kode lama - kamu wajib bisa mengenalinya:",
                    "",
                    "  class Penyimpan:",
                    "      def simpan(self, kunci, nilai):",
                    "          raise NotImplementedError(\"turunan wajib menulis simpan()\")",
                    "",
                    "                        ABC + @abstractmethod      raise NotImplementedError",
                    "    ketahuannya         saat objek dibuat          saat method-nya dipanggil",
                    "    Penyimpan() polos   ditolak TypeError          berhasil, objek setengah jadi",
                    "    kelewat kalau       -                          method itu tak pernah dipanggil",
                    "",
                    "Makin cepat sebuah kesalahan ketahuan, makin murah memperbaikinya. Untuk kode baru",
                    "pakai ABC; NotImplementedError tetap berguna untuk satu-dua method di class yang",
                    "bukan kontrak penuh.",
                    "",
                    "Jangan tertukar dua nama mirip ini: NotImplementedError adalah class exception,",
                    "dipakai dengan raise. NotImplemented (tanpa 'Error') adalah NILAI khusus yang",
                    "dikembalikan dunder pembanding seperti __eq__ saat tipenya tidak cocok. Menulis",
                    "raise NotImplemented memberi pesan yang bikin bingung karena tidak menyebut namanya:",
                    "  TypeError: exceptions must derive from BaseException",
                    "",
                    "Ada cara ketiga yang makin sering muncul di kode modern, dan bentuknya beda sekali:",
                    "typing.Protocol - kontrak yang bahkan tidak menuntut pewarisan.",
                ],
            },
            {
                "heading": "typing.Protocol: kontrak tanpa pewarisan",
                "code": "from typing import Protocol, runtime_checkable\n\n\n@runtime_checkable\nclass Pencetak(Protocol):\n    \"\"\"Kontrak: apa pun yang punya cetak(teks) sudah dianggap cocok.\"\"\"\n\n    def cetak(self, teks: str) -> None: ...\n\n\nclass Layar:                  # tidak mewarisi Pencetak, dan memang tidak perlu\n    def cetak(self, teks):\n        print(\"[layar]\", teks)\n\n\nclass Penampung:              # juga tidak menyebut Pencetak sama sekali\n    def __init__(self):\n        self.isi = []\n\n    def cetak(self, teks):\n        self.isi.append(teks)\n\n\ndef laporkan(keluaran: Pencetak, baris):\n    for b in baris:\n        keluaran.cetak(b)\n\n\nlaporkan(Layar(), [\"gaji: 100\", \"bonus: 20\"])\n\np = Penampung()\nlaporkan(p, [\"gaji: 100\", \"bonus: 20\"])\nprint(p.isi)\n\n# isinstance() hanya bekerja karena Protocol-nya diberi @runtime_checkable,\n# dan yang dicek cuma NAMA method-nya ada, bukan bentuk parameternya.\nprint(isinstance(Layar(), Pencetak))     # True\nprint(isinstance(3, Pencetak))           # False: int tidak punya cetak()\n\n# [layar] gaji: 100\n# [layar] bonus: 20\n# ['gaji: 100', 'bonus: 20']\n# True\n# False",
            },
            {
                "body": [
                    "Protocol (modul typing, ada sejak Python 3.8) membalik arah kontraknya. Pada ABC,",
                    "turunan harus MENYEBUT nama induknya. Pada Protocol tidak: sebuah class dianggap",
                    "memenuhi kontrak kalau kebetulan punya method dengan nama dan bentuk yang cocok.",
                    "Layar dan Penampung di atas tidak pernah menyebut Pencetak, tapi keduanya sah",
                    "dikirim ke laporkan(). Inilah duck typing yang akhirnya bisa DITULIS, bukan cuma",
                    "dijanjikan di kepala orang yang menulis kodenya.",
                    "",
                    "Kapan Protocol yang kamu butuhkan: saat class yang harus memenuhi kontrak BUKAN",
                    "milikmu - datang dari library orang lain, atau sudah terlanjur ditulis sebelum",
                    "kontraknya ada. Kamu tidak bisa menyuruhnya mewarisi apa pun, tapi tetap ingin",
                    "kewajibannya tertulis hitam di atas putih.",
                    "",
                    "Yang wajib diwaspadai: Protocol dicek oleh pemeriksa tipe seperti mypy SAAT KAMU",
                    "MENULIS, bukan oleh Python saat program berjalan. Tanpa mypy, anotasi Pencetak itu",
                    "hanya catatan untuk manusia; class yang tidak punya cetak() tetap diterima sampai",
                    "meledak jadi AttributeError. ABC kebalikannya: Python sendiri yang memaksanya.",
                    "",
                    "  duck typing polos   tidak tertulis di mana pun; ketahuan saat error terjadi",
                    "  ABC                 tertulis, DIPAKSA Python, turunan wajib menyebut induknya",
                    "  Protocol            tertulis, dicek mypy, class-nya tidak perlu tahu apa-apa",
                    "",
                    "Cara membaca kode orang yang memakai ABC - ini yang paling sering kamu perlukan:",
                    "",
                    "  - Begitu melihat class ber-(ABC), daftar @abstractmethod-nya adalah daftar method",
                    "    yang PASTI ada di setiap objek bertipe itu. Itu peta terpendek sebuah modul.",
                    "  - Class ber-ABC biasanya tidak melakukan pekerjaan sesungguhnya. Cari yang konkret",
                    "    dengan menyebut nama induknya di dalam kurung:",
                    "      grep -rn \"(Penyimpan)\" .",
                    "    Kalau ada tiga hasil, berarti ada tiga cara berbeda yang bisa dipilih program.",
                    "  - Saat sebuah fungsi menerima parameter bertipe Penyimpan, kamu langsung tahu apa",
                    "    yang boleh dilakukan padanya tanpa membuka satu pun implementasinya. Itu alasan",
                    "    kontrak ini ditulis sejak awal.",
                ],
            },
        ],
    },
    {
        "title": "24. OOP: Encapsulation & Dunder Methods",
        "sections": [
            {
                "body": [
                    "Python TIDAK punya keyword private/public/protected sungguhan",
                    "seperti Java. Konvensinya berbasis PENAMAAN:",
                    "  nama_biasa    -> public (default, bebas diakses)",
                    "  _nama_protect -> 'protected' (konvensi: jangan diakses dari luar,",
                    "                    tapi TIDAK dipaksakan Python, cuma etika kode)",
                    "  __nama_privat -> 'private' (name mangling: Python mengubah nama",
                    "                    jadi _NamaClass__nama_privat agar sulit diakses",
                    "                    tidak sengaja dari luar)",
                    "",
                    "property: cara Pythonic membuat getter/setter tanpa mengubah",
                    "cara pemakaian (tetap terlihat seperti akses atribut biasa).",
                ]
            },
            {
                "heading": "Contoh encapsulation dengan property",
                "code": """class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self._saldo = saldo         # konvensi: 'protected'

    @property
    def saldo(self):                # getter
        return self._saldo

    @saldo.setter
    def saldo(self, nilai):         # setter dengan validasi
        if nilai < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self._saldo = nilai

    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah

r = Rekening("Andi", 100000)
print(r.saldo)      # 100000 (dipanggil TANPA tanda kurung, seperti atribut biasa)
r.setor(50000)
print(r.saldo)      # 150000
r.saldo = -100      # ValueError: Saldo tidak boleh negatif!"""
            },
            {
                "body": [
                    "Dua baris di contoh itu pantas dibongkar, karena keduanya muncul",
                    "begitu saja tanpa pernah diperkenalkan.",
                    "",
                    "PERTAMA, dari mana nama @saldo.setter datang? @property tidak sekadar",
                    "menandai fungsinya; ia MENGGANTI fungsi saldo dengan sebuah objek",
                    "property, dan objek itu punya .setter dan .deleter. Jadi @saldo.setter",
                    "dibaca 'pakai .setter milik property bernama saldo'. Akibatnya:",
                    "  - Nama decorator-nya SELALU mengikuti nama fungsi di atasnya. Untuk",
                    "    @property def harga, pasangannya @harga.setter.",
                    "  - @property harus ditulis LEBIH DULU. @saldo.setter tidak punya apa",
                    "    pun untuk disambung kalau getter-nya belum ada.",
                    "  - Getter dan setter WAJIB sama namanya. Kalau setter-nya diberi",
                    "    nama set_saldo, yang lahir adalah property KEDUA bernama set_saldo,",
                    "    sedangkan saldo tetap cuma bisa dibaca - r.saldo = 0 lalu ditolak",
                    "    dengan  AttributeError: property 'saldo' of 'Rekening' object has",
                    "    no setter, dan pesannya tidak menyinggung salah nama sama sekali.",
                    "  - Ada juga @saldo.deleter untuk del r.saldo, jauh lebih jarang perlu.",
                    "",
                    "KEDUA, raise ValueError(...) di dalam setter itu artinya: lemparkan",
                    "error dan HENTIKAN penugasan di situ juga. Baris self._saldo = nilai di",
                    "bawahnya tidak pernah dijalankan, dan r.saldo tetap berisi nilai lama.",
                    "Itulah yang membuat validasi ini benar-benar mengikat, bukan sekadar",
                    "peringatan. raise, jenis-jenis error, dan cara menangkapnya dibahas",
                    "tuntas di materi Exception Handling.",
                ]
            },
            {
                "heading": "Dunder (magic) methods yang sering dipakai",
                "code": """class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):              # dipanggil oleh print()/str()
        return f"({self.x}, {self.y})"

    def __repr__(self):             # representasi untuk debugging
        return f"Titik({self.x}, {self.y})"

    def __eq__(self, other):        # dipanggil oleh operator ==
        return self.x == other.x and self.y == other.y

    def __add__(self, other):       # dipanggil oleh operator +
        return Titik(self.x + other.x, self.y + other.y)

p1 = Titik(1, 2)
p2 = Titik(3, 4)
print(p1)          # (1, 2)  -- lewat __str__
print(p1 == Titik(1, 2))   # True -- lewat __eq__
print(p1 + p2)     # (4, 6) -- lewat __add__"""
            },
            {
                "body": [
                    "Dunder method umum lainnya:",
                    "  __len__(self)       -> dipanggil oleh len(objek)",
                    "  __getitem__(self,i) -> dipanggil oleh objek[i]",
                    "  __iter__(self)      -> membuat objek bisa di-for-loop",
                    "  __lt__, __gt__      -> dipanggil oleh operator < dan >",
                    "  __call__(self)      -> membuat objek bisa 'dipanggil' seperti fungsi",
                    "",
                    "__slots__: satu baris di PUNCAK badan class yang mengunci daftar",
                    "atribut yang boleh dimiliki objeknya.",
                    "",
                    "  class Titik:",
                    "      __slots__ = (\"x\", \"y\")",
                    "",
                    "      def __init__(self, x, y):",
                    "          self.x = x",
                    "          self.y = y",
                    "",
                    "  p = Titik(1, 2)",
                    "  p.z = 3   -> AttributeError: 'Titik' object has no attribute 'z'",
                    "               and no __dict__ for setting new attributes",
                    "",
                    "Bentuknya persis seperti class attribute biasa di materi Class & Object,",
                    "padahal kerjanya lain sama sekali. Python jadi tidak perlu menyiapkan",
                    "kamus atribut untuk tiap objek, sehingga objeknya jauh lebih hemat",
                    "memori - itu sebabnya __slots__ muncul di kode yang membuat jutaan",
                    "objek kecil. Efek sampingnya sering justru yang paling berguna: salah",
                    "ketik nama atribut langsung ketahuan, bukan diam-diam membuat atribut",
                    "baru yang tidak pernah dibaca siapa pun.",
                    "",
                    "Harganya, atribut di luar daftar itu tidak bisa ditambahkan lagi",
                    "belakangan. Jadi pakai hanya kalau memang butuh; class biasa tetap",
                    "pilihan bawaan.",
                ]
            },
        ],
    },
    {
        "title": "25. dataclass & Enum",
        "sections": [
            {
                "body": [
                    "Sebagian besar class di kode nyata bukan class yang pintar - ia cuma PEMBAWA DATA.",
                    "Titik, Produk, Konfigurasi, satu baris hasil query dari database: isinya beberapa",
                    "atribut dan nyaris tidak ada perilaku. Ditulis dengan cara materi Encapsulation &",
                    "Dunder Methods, class semacam itu jadi panjang oleh __init__, __repr__, dan __eq__",
                    "yang isinya selalu bisa ditebak: sebutkan nama field, lalu ulangi lagi, lalu ulangi",
                    "lagi. Tiga kali menulis daftar yang sama, dan satu field yang lupa disalin ke salah",
                    "satunya adalah bug yang sangat sulit dilihat.",
                    "",
                    "@dataclass (modul bawaan dataclasses, sejak Python 3.7) menuliskan method-method itu",
                    "untukmu. Kamu cukup menyebut ATRIBUT apa saja yang dipunya class ini - sekali.",
                    "",
                    "Bentuknya sangat berbeda dari class biasa, dan inilah yang wajib kamu kenali:",
                    "",
                    "  from dataclasses import dataclass",
                    "",
                    "  @dataclass",
                    "  class Produk:",
                    "      nama: str",
                    "      harga: int",
                    "      stok: int = 0",
                    "",
                    "Tidak ada def __init__ satu baris pun. Saat pertama kali membaca kode seperti ini,",
                    "kesimpulan yang paling mudah diambil - dan salah - adalah 'class ini tidak punya",
                    "constructor'. Justru sebaliknya: constructornya DIBUATKAN, persis dari tiga baris",
                    "itu, dan Produk(\"Kopi\", 25000) langsung bisa dipanggil.",
                    "",
                    "Tiga baris nama: str / harga: int / stok: int = 0 itu anotasi tipe (lihat materi",
                    "Anotasi Tipe (Type Hint)). Bedanya, di sini anotasinya BUKAN sekadar catatan untuk",
                    "manusia: @dataclass membaca daftar anotasi di badan class untuk tahu ada field apa",
                    "saja.",
                    "Konsekuensi yang mengejutkan - atribut yang ditulis TANPA anotasi tidak dianggap",
                    "field sama sekali, tidak muncul di __init__, dan cuma jadi class attribute biasa",
                    "(lihat materi Class & Object):",
                    "",
                    "  @dataclass",
                    "  class Produk:",
                    "      nama: str        # field: masuk __init__",
                    "      pajak = 0.11     # BUKAN field, cuma class attribute - gampang salah kira",
                    "",
                    "Tipe yang ditulis tetap tidak dipaksakan Python; Produk(123, \"mahal\") tetap jalan.",
                    "Yang dipakai @dataclass hanya KEBERADAAN anotasinya, bukan isinya.",
                    "",
                    "Yang dibuatkan untukmu:",
                    "  __init__   parameternya berurutan persis seperti urutan field di badan class",
                    "  __repr__   sehingga print(objek) menampilkan isinya, bukan alamat memori",
                    "  __eq__     sehingga == membandingkan ISI field, bukan 'objek yang sama persis'",
                    "",
                    "__eq__ itu yang paling sering menyelamatkan. Tanpanya, dua objek berisi data",
                    "identik selalu dianggap tidak sama - termasuk saat kamu membandingkan hasil di",
                    "dalam tes, dan itu kegagalan yang membingungkan karena keduanya terlihat sama.",
                ],
            },
            {
                "heading": "Class yang sama: ditulis tangan, lalu dengan @dataclass",
                "code": """from dataclasses import dataclass, field, asdict, replace

# Ditulis tangan: tiga method di bawah harus diketik sendiri, satu per satu
class TitikManual:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"TitikManual(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Hal yang sama persis - ketiganya dibuatkan otomatis
@dataclass
class Titik:
    x: int          # field diumumkan lewat ANOTASI TIPE, bukan lewat self.x = x
    y: int

p = Titik(3, 4)              # __init__ ada, urutan parameternya seperti di atas
print(p.x, p.y)              # 3 4
print(p)                     # Titik(x=3, y=4)         <- __repr__ bawaan
print(p == Titik(3, 4))      # True                    <- __eq__ bawaan
print(TitikManual(3, 4))     # TitikManual(x=3, y=4)

p.y = 99                     # dataclass biasa TETAP bisa diubah seperti class lain
print(p)                     # Titik(x=3, y=99)

# Tanpa __repr__, print() sebuah objek cuma menampilkan alamat memorinya
class Polos:
    def __init__(self, x):
        self.x = x

print(str(Polos(3)).startswith("<__main__.Polos object at 0x"))   # True

# ---- field berdefault, dan default yang mutable ----
@dataclass
class Keranjang:
    pemilik: str
    diskon: float = 0.0                     # yang berdefault WAJIB di belakang
    isi: list = field(default_factory=list)  # BUKAN  isi: list = []

k1 = Keranjang("Andi")
k2 = Keranjang("Budi")
k1.isi.append("apel")
print(k1.isi, k2.isi)     # ['apel'] []   <- tiap objek dapat list SENDIRI
print(asdict(k1))         # {'pemilik': 'Andi', 'diskon': 0.0, 'isi': ['apel']}

# ---- frozen & order ----
@dataclass(frozen=True, order=True)
class Uang:
    jumlah: int
    mata: str = "IDR"

a = Uang(5000)
b = replace(a, jumlah=7000)     # objek BARU, satu field diganti; a tidak tersentuh
print(a)                        # Uang(jumlah=5000, mata='IDR')  <- a tidak berubah
print(b)                        # Uang(jumlah=7000, mata='IDR')
print(a < b)                    # True  <- order=True menghidupkan < > <= >=
print(len({a, Uang(5000)}))     # 1     <- frozen=True membuatnya bisa masuk set/dict

try:
    a.jumlah = 9000             # frozen: menulis ke field ditolak
except Exception as e:
    # FrozenInstanceError - cannot assign to field 'jumlah'
    print(type(e).__name__, "-", e)""",
            },
            {
                "body": [
                    "Aturan main dan jebakan @dataclass yang perlu kamu tahu sebelum memakainya:",
                    "",
                    "1. Field berdefault harus di BELAKANG yang tidak berdefault - alasannya sama",
                    "   persis dengan parameter fungsi, karena __init__ yang dibuatkan memang fungsi",
                    "   biasa. Kalau terbalik, class-nya gagal SAAT BERKASNYA DIIMPOR, bukan nanti",
                    "   saat objek dibuat:",
                    "     @dataclass",
                    "     class Keranjang:",
                    "         diskon: float = 0.0",
                    "         pemilik: str",
                    "     TypeError: non-default argument 'pemilik' follows default argument 'diskon'",
                    "",
                    "2. Default MUTABLE dilarang - dan dilarangnya keras, bukan cuma disarankan:",
                    "     @dataclass",
                    "     class Keranjang:",
                    "         pemilik: str",
                    "         isi: list = []",
                    "     ValueError: mutable default <class 'list'> for field isi is not allowed:",
                    "     use default_factory",
                    "   Ini jebakan yang sama dengan def f(x=[]) di materi Referensi Objek, Salinan &",
                    "   Jebakan Mutable: badan class dijalankan SEKALI, jadi satu list itu akan dipakai",
                    "   bersama oleh semua objek dan isinya menumpuk. Bedanya, di fungsi Python diam",
                    "   saja dan kamu baru sadar setelah datanya bocor; di dataclass Python menolak",
                    "   sejak awal. Perbaikannya:",
                    "     isi: list = field(default_factory=list)      # dict, set, atau lambda juga boleh",
                    "   default_factory adalah FUNGSI yang dipanggil ulang tiap objek dibuat - tulis",
                    "   namanya saja (list), tanpa tanda kurung, karena yang diminta fungsinya sendiri.",
                    "   Untuk default yang immutable (0, \"\", None, True) cukup tulis biasa: stok: int = 0.",
                    "",
                    "3. frozen=True membuat objeknya tidak bisa diubah setelah dibuat. Menulis ke",
                    "   fieldnya melempar FrozenInstanceError. Hadiah sampingannya besar: objeknya jadi",
                    "   hashable, sehingga bisa dipakai sebagai key dict atau anggota set. dataclass",
                    "   BIASA justru tidak bisa - begitu __eq__ dibuatkan, Python mematikan __hash__",
                    "   bawaannya, dan {Titik(1, 2)} berujung TypeError: unhashable type.",
                    "   JEBAKAN: frozen cuma mengunci LAPISAN LUAR. Kalau salah satu field berisi list,",
                    "   isi list itu tetap bisa di-append - persis seperti salinan dangkal di materi",
                    "   Referensi Objek. 'Frozen' berarti labelnya tidak bisa dipindah, bukan isinya",
                    "   dibekukan.",
                    "",
                    "4. order=True menghidupkan < > <= >= dengan membandingkan field BERURUTAN, seperti",
                    "   tuple. Karena itu urutan penulisan field mendadak menentukan cara sorting:",
                    "   kalau field pertamamu 'nama' padahal yang ingin diurutkan 'harga', sorted()",
                    "   akan mengurutkan berdasarkan nama tanpa mengeluh sedikit pun. field(compare=False)",
                    "   mengeluarkan satu field dari __eq__ dan dari pengurutan.",
                    "",
                    "5. Alat pendukung yang sering muncul:",
                    "     asdict(objek)          -> dict, menembus sampai ke dataclass di dalamnya",
                    "     astuple(objek)         -> tuple",
                    "     replace(objek, x=9)    -> objek BARU dengan sebagian field diganti; ini satu-",
                    "                               satunya cara 'mengubah' objek frozen",
                    "     field(init=False)      -> field yang TIDAK jadi parameter __init__",
                    "     __post_init__(self)    -> dipanggil otomatis setelah __init__ selesai; tempat",
                    "                               memvalidasi atau menghitung field turunan",
                    "",
                    "     @dataclass",
                    "     class Lingkaran:",
                    "         jari: float",
                    "         luas: float = field(init=False)",
                    "         def __post_init__(self):",
                    "             if self.jari <= 0:",
                    "                 raise ValueError(\"jari harus positif\")",
                    "             self.luas = 3.14159 * self.jari ** 2",
                    "",
                    "Sekarang lubang yang kedua, dan ini tetangga dekatnya.",
                    "",
                    "Materi Variabel & Tipe Data mengajarkan konstanta sebagai konvensi UPPERCASE",
                    "(PI = 3.14159). Itu cukup untuk SATU nilai tetap. Yang tidak tertutup: HIMPUNAN",
                    "nilai tetap yang saling terkait - status pesanan, peran pengguna, level log, jenis",
                    "pembayaran. Cara naifnya adalah menyebarkan string mentah ke seluruh kode:",
                    "",
                    "  if status == \"dikirim\": ...",
                    "  pesanan[\"status\"] = \"selesai\"",
                    "",
                    "Masalahnya bukan gaya, tapi diamnya: kalau kamu mengetik \"dikirin\", Python tidak",
                    "protes apa-apa. Perbandingannya cuma menghasilkan False, cabang if itu tidak pernah",
                    "jalan, dan programnya tetap berjalan mulus sambil salah. Tidak ada satu pun yang",
                    "menahanmu - bukan Python, bukan editor, bukan mypy.",
                    "",
                    "Enum (modul bawaan enum) menutup itu: sebuah class yang anggotanya TETAP dan",
                    "TERBATAS, masing-masing punya nama dan nilai.",
                ],
            },
            {
                "heading": "Enum: himpunan nilai yang tetap dan terbatas",
                "code": """from enum import Enum, auto

class Status(Enum):
    MENUNGGU = "menunggu"      # kiri = NAMA anggota, kanan = NILAInya
    DIKIRIM = "dikirim"
    SELESAI = "selesai"

class Prioritas(Enum):
    RENDAH = auto()            # auto() mengisi 1, 2, 3 - dipakai kalau nilainya
    SEDANG = auto()            # memang tidak penting, yang penting namanya
    TINGGI = auto()

s = Status.DIKIRIM
print(s)                       # Status.DIKIRIM
print(s.name)                  # DIKIRIM   <- namanya, bertipe str
print(s.value)                 # dikirim   <- nilai yang kamu tulis
print(s is Status.DIKIRIM)     # True      <- tiap anggota cuma ada SATU objeknya
print(s is Status.SELESAI)     # False
print(Prioritas.TINGGI.value)  # 3

for st in Status:              # urutan iterasi = urutan penulisan
    print(st.name, "->", st.value)

print(Status("selesai"))       # Status.SELESAI  <- cari lewat NILAI (kurung biasa)
print(Status["SELESAI"])       # Status.SELESAI  <- cari lewat NAMA (kurung siku)
print(len(Status))             # 3

# Nilai yang tidak terdaftar langsung ditolak - inilah gunanya Enum
try:
    Status("dikirin")          # salah ketik, ketahuan DI SINI
except ValueError as e:
    print("ValueError:", e)    # 'dikirin' is not a valid Status

def pesan(st):
    if st is Status.MENUNGGU:
        return "Pesanan sedang diproses."
    if st is Status.DIKIRIM:
        return "Pesanan sedang di jalan."
    return "Pesanan selesai."

print(pesan(Status.MENUNGGU))  # Pesanan sedang diproses.""",
            },
            {
                "body": [
                    "Yang perlu dipegang soal Enum:",
                    "",
                    "  Status.DIKIRIM        anggotanya sendiri - inilah yang dioper ke mana-mana",
                    "  .name                 \"DIKIRIM\", teks nama anggotanya",
                    "  .value                \"dikirim\", nilai yang kamu tulis di sebelah kanan",
                    "  is                    cara membandingkan anggota Enum; == juga benar, tapi 'is'",
                    "                        lebih tegas dan tidak bisa tertipu oleh nilai yang mirip",
                    "  auto()                minta Python mengisi nilainya sendiri: 1, 2, 3, ...",
                    "  @unique               dekorator dari modul enum; melarang dua anggota bernilai sama",
                    "",
                    "JEBAKAN NOMOR SATU: anggota Enum BUKAN string-nya.",
                    "  Status.DIKIRIM == \"dikirim\"     -> False, dan Python tidak protes",
                    "Kode yang setengah dipindah ke Enum - sebagian sudah memakai Status.DIKIRIM,",
                    "sebagian masih membandingkan dengan string mentah - akan berjalan tanpa error",
                    "sambil salah terus. Kalau butuh string aslinya, minta secara eksplisit: .value.",
                    "Karena alasan yang sama, json.dumps({\"status\": Status.DIKIRIM}) gagal dengan",
                    "TypeError: Object of type Status is not JSON serializable. Kirim .value-nya.",
                    "",
                    "Jebakan kedua: dua anggota yang nilainya SAMA tidak jadi dua anggota. Yang kedua",
                    "otomatis jadi ALIAS - nama lain untuk anggota pertama - sehingga ia tidak muncul",
                    "saat diiterasi dan .name-nya berubah jadi nama yang pertama. Pasang @unique di",
                    "atas class kalau kamu ingin itu ditolak sebagai kesalahan.",
                    "",
                    "Jebakan ketiga: jangan menyimpan nilai auto() ke database. auto() memberi 1, 2, 3",
                    "menurut URUTAN PENULISAN, jadi menyisipkan satu anggota baru di tengah menggeser",
                    "nomor semua anggota sesudahnya - dan seluruh baris lama di database mendadak",
                    "menunjuk status yang berbeda. Untuk nilai yang ikut tersimpan, tulis eksplisit",
                    "(\"dikirim\", 3), dan anggap nilai itu tidak boleh diubah lagi selamanya.",
                    "",
                    "Dua varian yang sering kamu temui:",
                    "  IntEnum   anggotanya SUNGGUH int: Level.TINGGI > 2 dan Level.RENDAH + 1 jalan.",
                    "            Dipakai untuk hal yang memang punya tingkatan - level log, kode HTTP.",
                    "  StrEnum   anggotanya SUNGGUH str (Python 3.11+): Warna.MERAH == \"merah\" jadi",
                    "            True, .upper() jalan, dan json.dumps langsung menghasilkan \"merah\".",
                    "            Sebelum 3.11 orang menulis  class Warna(str, Enum):  untuk efek yang",
                    "            hampir sama - bentuk itu masih bertebaran di kode yang beredar. Satu",
                    "            bedanya: pada StrEnum, f\"{Warna.MERAH}\" menghasilkan merah, sedangkan",
                    "            pada (str, Enum) menghasilkan Warna.MERAH.",
                    "Keduanya menukar keamanan dengan kenyamanan: karena anggotanya bisa disamakan",
                    "dengan int/str biasa, salah ketik jadi mungkin lolos lagi. Pilih Enum polos dulu,",
                    "naik ke IntEnum/StrEnum hanya kalau nilainya memang harus keluar-masuk sistem lain.",
                    "",
                    "Sekilas ke depan, supaya tidak asing. Di project FastAPI (disebut di materi",
                    "Roadmap) berkas pertama yang kamu buka biasanya berisi ini:",
                    "",
                    "  from pydantic import BaseModel",
                    "",
                    "  class Produk(BaseModel):",
                    "      nama: str",
                    "      harga: int = 0",
                    "",
                    "Bentuknya nyaris sama dengan @dataclass, dan alasannya memang sama: field",
                    "diumumkan lewat anotasi tipe di badan class. Bedanya satu dan besar - pydantic",
                    "BENAR-BENAR memeriksa tipenya saat objek dibuat, lalu menolak data yang tidak",
                    "cocok, karena datanya datang dari internet dan tidak boleh dipercaya. @dataclass",
                    "tidak memeriksa apa pun. Enum juga dipakai langsung di situ sebagai tipe field,",
                    "dan FastAPI mengubahnya jadi daftar nilai yang sah di dokumentasi API otomatisnya.",
                ],
            },
        ],
    },
    {
        "title": "26. Exception Handling",
        "sections": [
            {
                "body": [
                    "Exception = error yang terjadi saat program berjalan.",
                    "Tanpa penanganan, program langsung berhenti (crash).",
                    "",
                    "Exception umum bawaan Python:",
                    "  ZeroDivisionError    -> 10 / 0",
                    "  IndexError           -> list[99] padahal list kecil",
                    "  KeyError             -> dict[\"tidak_ada\"]",
                    "  TypeError            -> \"5\" + 5 (tipe tak cocok)",
                    "  ValueError           -> int(\"abc\") (gagal konversi)",
                    "  FileNotFoundError    -> buka file yang tidak ada",
                    "  AttributeError       -> objek.method_tidak_ada()",
                    "",
                    "Sintaks try-except:",
                    "  try:",
                    "      # kode yang mungkin error",
                    "  except TipeError as e:",
                    "      # penanganan error",
                    "  else:",
                    "      # jalan HANYA jika TIDAK ada error",
                    "  finally:",
                    "      # SELALU jalan, error atau tidak",
                ]
            },
            {
                "heading": "Contoh try-except-else-finally",
                "code": """def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol!")
        return None
    except TypeError:
        print("Tipe data harus angka!")
        return None
    else:
        print("Pembagian berhasil.")
        return hasil
    finally:
        print("Selesai mencoba pembagian.")

print(bagi(10, 2))    # Pembagian berhasil. / Selesai mencoba... / 5.0
print(bagi(10, 0))    # Tidak bisa membagi dengan nol! / Selesai... / None
print(bagi(10, "a"))  # Tipe data harus angka! / Selesai... / None"""
            },
            {
                "body": [
                    "Menangkap beberapa exception sekaligus:",
                    "  except (ZeroDivisionError, TypeError) as e:",
                    "      print(f\"Error: {e}\")",
                    "",
                    "raise: melempar exception secara sengaja.",
                    "  if umur < 0:",
                    "      raise ValueError(\"Umur tidak boleh negatif\")",
                    "",
                    "Membuat exception custom (turunan dari Exception):",
                    "  class SaldoTidakCukup(Exception):",
                    "      pass",
                    "",
                    "  raise SaldoTidakCukup(\"Saldo kurang untuk transaksi ini\")",
                    "",
                    "EAFP vs LBYL (filosofi Python untuk error handling):",
                    "  EAFP (Easier to Ask Forgiveness than Permission) - GAYA PYTHON:",
                    "      try:",
                    "          nilai = data[\"key\"]",
                    "      except KeyError:",
                    "          nilai = default",
                    "  LBYL (Look Before You Leap) - gaya lebih defensif:",
                    "      if \"key\" in data:",
                    "          nilai = data[\"key\"]",
                    "      else:",
                    "          nilai = default",
                ]
            },
        ],
    },
    {
        "title": "27. Membaca Traceback & Menangkap Error Secara Luas",
        "sections": [
            {
                "body": [
                    "Traceback adalah teks yang Python cetak ketika programmu berhenti karena error yang",
                    "tidak ditangani. Ini teks yang PALING SERING dibaca seorang programmer - jauh lebih",
                    "sering daripada kode orang lain. Pemula biasanya memandangnya sebagai tembok merah lalu",
                    "menebak-nebak sendiri, padahal isinya laporan berformat tetap yang hampir selalu sudah",
                    "memuat jawabannya.",
                    "",
                    "Bentuknya selalu seperti ini:",
                    "",
                    "  Traceback (most recent call last):",
                    "    File \"program.py\", line 24, in <module>          <- frame paling LUAR",
                    "      print(\"Rata-rata umur:\", rata_rata_umur(data))",
                    "    File \"program.py\", line 12, in rata_rata_umur    <- dipanggil oleh yang di atas",
                    "      orang = baca_baris(baris)",
                    "    File \"program.py\", line 6, in baca_baris         <- frame paling DALAM",
                    "      return {\"nama\": nama, \"umur\": int(umur)}",
                    "  ValueError: invalid literal for int() with base 10: 'tiga puluh'",
                    "",
                    "Bagian-bagiannya:",
                    "  - 'most recent call last' bukan basa-basi, itu petunjuk cara baca: panggilan TERBARU",
                    "    ada di BAWAH. Karena itu traceback dibaca dari bawah ke atas.",
                    "  - Tiap pasang baris adalah satu FRAME: satu fungsi yang sedang berjalan saat error",
                    "    terjadi. Baris pertama menyebut berkas, nomor baris, dan nama fungsinya; baris",
                    "    kedua menampilkan isi baris kode itu.",
                    "  - <module> berarti kode itu ada di tingkat atas berkas, bukan di dalam fungsi mana pun.",
                    "  - Baris TERAKHIR adalah intinya, berbentuk 'JenisError: pesan'. Baca ini lebih dulu.",
                    "  - Python 3.11 ke atas menambahkan penanda ~~~^^^ di bawah baris kode untuk menunjuk",
                    "    PERSIS bagian ekspresi yang gagal. Di Python lama penanda ini tidak ada.",
                    "",
                    "Urutan membacanya - ini yang menghemat berjam-jam:",
                    "  1. Baris paling bawah: errornya apa, pesannya apa.",
                    "  2. Frame paling bawah: baris mana yang sedang jalan saat itu.",
                    "  3. Naik ke atas: siapa memanggil siapa. Kalau tumpukannya penuh berkas library",
                    "     (site-packages), errornya hampir selalu berasal dari data yang KAMU kirim ke",
                    "     library itu - jadi cari frame TERAKHIR yang berkasnya milikmu.",
                    "  4. Baru sesudah itu buka baris yang ditunjuk.",
                    "",
                    "Jebakan besarnya: baris yang ditunjuk adalah baris yang sedang BERJALAN, belum tentu",
                    "baris yang salah. Traceback menunjuk tempat kejadian, bukan tempat kesalahan. Pesan",
                    "errornya - potongan nilai yang bikin gagal - yang menuntunmu ke sumber sebenarnya.",
                ],
            },
            {
                "heading": "Traceback asli dari program yang gagal",
                "code": """# Program ini SENGAJA gagal. Jalankan, lalu baca teks error yang muncul --
# itulah traceback. Bedah barisnya ada di komentar paling bawah berkas ini.

def baca_baris(baris):
    nama, umur = baris.split(",")
    return {"nama": nama, "umur": int(umur)}


def rata_rata_umur(daftar):
    total = 0
    for baris in daftar:
        orang = baca_baris(baris)
        total += orang["umur"]
    return total / len(daftar)


data = [
    "Andi,30",
    "Budi,25",
    "Citra,tiga puluh",       # <- baris inilah biang keroknya
]

print("Mulai menghitung...")
print("Rata-rata umur:", rata_rata_umur(data))
print("Baris ini tidak pernah tercetak.")

# Yang muncul di layar:
#
# Mulai menghitung...
# Traceback (most recent call last):
#   File "/home/kamu/traceback-asli.py", line 24, in <module>
#     print("Rata-rata umur:", rata_rata_umur(data))
#                              ~~~~~~~~~~~~~~^^^^^^
#   File "/home/kamu/traceback-asli.py", line 12, in rata_rata_umur
#     orang = baca_baris(baris)
#   File "/home/kamu/traceback-asli.py", line 6, in baca_baris
#     return {"nama": nama, "umur": int(umur)}
#                                   ~~~^^^^^^
# ValueError: invalid literal for int() with base 10: 'tiga puluh'
#
# (Jalur berkasnya ditulis Python selengkap-lengkapnya, jadi di layarmu nanti
#  yang tampil adalah tempat kamu menyimpan berkas ini.)
#
# Membacanya dari BAWAH:
#   1. ValueError -- int() diberi teks yang bukan angka, isinya 'tiga puluh'.
#   2. Frame terbawah: baris 6, di dalam baca_baris; di situ int(umur) jalan.
#   3. Naik: baris 12 di rata_rata_umur, yang memanggil baca_baris.
#   4. Naik lagi: baris 24 di <module>, yaitu tingkat atas berkas.
#   Jalurnya: baris 24 -> baris 12 -> baris 6, lalu meledak.
#
# Dan yang perlu DIPERBAIKI bukan baris 6. int(umur) sudah benar; yang salah
# datanya di baris 20. Pesan errornya yang menunjukkan itu: begitu kamu tahu
# nilai yang bikin gagal berbunyi 'tiga puluh', kamu tahu harus mencari ke mana.
#
# "Mulai menghitung..." tetap tercetak karena baris 23 sudah lewat. Baris 25
# tidak, karena program berhenti seketika saat sebuah error tidak ditangani.""",
            },
            {
                "body": [
                    "Sekarang sisi penangkapannya. Materi Exception Handling mengajarkan menangkap SATU tipe",
                    "yang sudah kamu duga. Kode nyata butuh dua hal lagi: menangkap satu KELUARGA error",
                    "sekaligus, dan menaruh satu jaring pengaman di batas program.",
                    "",
                    "Semua exception di Python adalah class, dan class-class itu punya silsilah:",
                    "",
                    "  BaseException                 akar segalanya -- JANGAN ditangkap",
                    "   +-- SystemExit               dilempar oleh sys.exit()",
                    "   +-- KeyboardInterrupt        kamu menekan Ctrl+C",
                    "   +-- GeneratorExit",
                    "   +-- Exception                akar semua error 'biasa' -- INI yang ditangkap",
                    "        +-- ArithmeticError",
                    "        |    +-- ZeroDivisionError",
                    "        +-- LookupError",
                    "        |    +-- IndexError",
                    "        |    +-- KeyError",
                    "        +-- OSError",
                    "        |    +-- FileNotFoundError, PermissionError, IsADirectoryError, ...",
                    "        +-- ValueError",
                    "        +-- TypeError",
                    "        +-- AttributeError",
                    "        +-- NameError",
                    "        +-- ImportError  ->  ModuleNotFoundError",
                    "        +-- RuntimeError ->  RecursionError",
                    "        +-- StopIteration",
                    "",
                    "Aturan yang mengalir dari silsilah itu: 'except X' menangkap X BESERTA seluruh",
                    "keturunannya. 'except LookupError' ikut menangkap KeyError dan IndexError; 'except",
                    "Exception' menangkap hampir segalanya. Exception custom buatanmu turunan Exception,",
                    "jadi ia pun ikut tertangkap - itu memang maunya.",
                    "",
                    "Akibat langsungnya: URUTAN blok except menentukan segalanya. Python mencoba blok dari",
                    "atas ke bawah dan memakai yang PERTAMA cocok. Menaruh 'except Exception' di atas",
                    "membuat semua blok di bawahnya jadi kode mati - dan Python tidak memperingatkan apa pun.",
                    "Aturannya: yang paling SPESIFIK di atas, jaring terluas paling bawah.",
                    "",
                    "  ditulis                 menangkap                        dipakai kapan",
                    "  except ValueError:      ValueError saja                  kasus yang kamu antisipasi",
                    "  except LookupError:     KeyError, IndexError, ...        satu keluarga sekaligus",
                    "  except Exception as e:  semua error 'biasa'              batas program, retry, log",
                    "  except BaseException:   ikut Ctrl+C dan sys.exit()       hampir tidak pernah",
                    "  except:                 sama saja dengan BaseException   jangan",
                    "",
                    "Kenapa 'except:' telanjang berbahaya. Ia sama dengan 'except BaseException', jadi ikut",
                    "menelan KeyboardInterrupt (Ctrl+C-mu tidak lagi menghentikan program) dan SystemExit",
                    "(sys.exit() di dalam blok itu tidak jadi keluar). Dua hal itu bukan error - itu",
                    "perintah berhenti. 'except Exception' tidak menyentuh keduanya, dan itulah sebabnya",
                    "ia bentuk yang benar untuk menangkap secara luas.",
                    "",
                    "Kapan menangkap luas itu SAH: hanya di tempat yang bisa benar-benar berbuat sesuatu -",
                    "batas program (fungsi main), satu putaran pekerjaan yang boleh gagal sendirian, atau",
                    "sebelum mencoba ulang. Dan syaratnya dua: pesannya dicatat lengkap dengan tracebacknya,",
                    "lalu error itu ditangani atau dilempar ulang. 'except Exception: pass' adalah cara",
                    "tercepat membuat bug tak terlacak - programmu diam, salah, dan tak meninggalkan jejak.",
                ],
            },
            {
                "heading": "Hierarki exception, urutan except, dan except telanjang",
                "code": """import sys

# -------------------------------------------------------------------------
# 1. Menangkap sebuah INDUK berarti ikut menangkap seluruh keturunannya.

print(issubclass(KeyError, LookupError))           # True
print(issubclass(ZeroDivisionError, Exception))    # True
print(issubclass(KeyboardInterrupt, Exception))    # False -- ia ADIK Exception
print(issubclass(Exception, BaseException))        # True

data = {"a": 1}
try:
    print(data["z"])
except LookupError as e:            # KeyError masih satu keluarga LookupError
    # type(e).__name__ -> nama jenisnya   str(e) -> pesannya saja
    # repr(e)          -> dua-duanya sekaligus, bentuk terbaik untuk dicatat
    print("tertangkap:", type(e).__name__, "->", e, "|", repr(e))
    simpan = e                      # masih perlu di luar? SALIN dulu di sini

# Jebakan kecil: nama sesudah 'as' DIHAPUS Python begitu blok except selesai.
print("e masih ada di luar blok?", "e" in dir())    # False
print("untung sudah disalin:", repr(simpan))

# -------------------------------------------------------------------------
# 2. Urutan except menentukan segalanya: Python memakai blok PERTAMA yang cocok.

def urutan_benar(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "pembagi nol"
    except Exception as e:              # jaring terakhir -> taruh paling BAWAH
        return "error lain: " + type(e).__name__

def urutan_salah(a, b):
    try:
        return a / b
    except Exception as e:              # menyapu semuanya lebih dulu ...
        return "error lain: " + type(e).__name__
    except ZeroDivisionError:           # ... jadi baris ini KODE MATI
        return "pembagi nol"

print(urutan_benar(10, 0), "|", urutan_benar(10, "x"))
print(urutan_salah(10, 0), "|", urutan_salah(10, "x"))
# Python tidak memberi peringatan apa pun soal blok yang tak terjangkau itu.

# -------------------------------------------------------------------------
# 3. except telanjang menelan hal-hal yang tidak boleh ditelan.

def pakai_except_telanjang():
    try:
        sys.exit("berhenti: input tidak sah")
    except:                     # TELANJANG, sama dengan except BaseException
        print("  sys.exit() barusan DITELAN; program jalan terus")

def pakai_except_exception():
    try:
        sys.exit("berhenti: input tidak sah")
    except Exception:           # SystemExit bukan turunan Exception -> lolos
        print("  baris ini tidak pernah tercetak")

print("percobaan 1 - except telanjang:")
pakai_except_telanjang()
print("percobaan 2 - except Exception:")
try:
    pakai_except_exception()
except SystemExit as e:
    print("  SystemExit lolos seperti seharusnya:", e)

# Nasib yang sama menimpa KeyboardInterrupt: dengan except telanjang, Ctrl+C
# ikut tertelan dan programmu jadi tidak bisa dihentikan dari keyboard.
# (sys.exit dibahas tuntas di materi Program Baris Perintah: sys, os & argparse.)

# -------------------------------------------------------------------------
# 4. raise telanjang: menangkap sebentar, lalu melempar ulang error yang SAMA.

def ambil(data, kunci):
    try:
        return data[kunci]
    except KeyError:
        print("  [catat] kunci", repr(kunci), "tidak ada -- dilempar ulang")
        raise           # tanpa argumen: error yang sama, traceback asli utuh

try:
    ambil({"a": 1}, "z")
except KeyError as e:
    print("  sampai ke pemanggil:", repr(e))

# Keluarannya:
# True
# True
# False
# True
# tertangkap: KeyError -> 'z' | KeyError('z')
# e masih ada di luar blok? False
# untung sudah disalin: KeyError('z')
# pembagi nol | error lain: TypeError
# error lain: ZeroDivisionError | error lain: TypeError
# percobaan 1 - except telanjang:
#   sys.exit() barusan DITELAN; program jalan terus
# percobaan 2 - except Exception:
#   SystemExit lolos seperti seharusnya: berhenti: input tidak sah
#   [catat] kunci 'z' tidak ada -- dilempar ulang
#   sampai ke pemanggil: KeyError('z')""",
            },
            {
                "heading": "Rantai sebab: raise from, dan modul traceback",
                "code": "import traceback\n\n\nclass GagalKirim(Exception):\n    \"\"\"Error tingkat aplikasi: pesannya untuk manusia, bukan untuk mesin.\"\"\"\n\n\nSERVER = {\"andi@contoh.id\": \"smtp-1\"}\n\n\ndef cari_server(alamat):\n    return SERVER[alamat]            # KeyError kalau alamatnya tak terdaftar\n\n\ndef kirim(alamat, gaya):\n    try:\n        return cari_server(alamat)\n    except KeyError as err:\n        pesan = \"notifikasi ke \" + alamat + \" tidak terkirim\"\n        if gaya == \"from err\":\n            raise GagalKirim(pesan) from err      # sebab EKSPLISIT\n        if gaya == \"tanpa from\":\n            raise GagalKirim(pesan)               # sebab tetap ikut tercatat\n        raise GagalKirim(pesan) from None         # sebab SENGAJA disembunyikan\n\n\nfor gaya in (\"from err\", \"tanpa from\", \"from None\"):\n    print(\"=\" * 66)\n    print(\"raise GagalKirim(pesan) \" + gaya)\n    try:\n        kirim(\"budi@contoh.id\", gaya)\n    except GagalKirim as e:\n        print(\"__cause__           :\", repr(e.__cause__))\n        print(\"__context__         :\", repr(e.__context__))\n        print(\"__suppress_context__:\", e.__suppress_context__)\n        print(\"-\" * 66)\n        print(traceback.format_exc(), end=\"\")\n\n# Keluaran untuk gaya PERTAMA (hanya jalur berkasnya yang dipendekkan):\n#\n# __cause__           : KeyError('budi@contoh.id')\n# __context__         : KeyError('budi@contoh.id')\n# __suppress_context__: True\n# ------------------------------------------------------------------\n# Traceback (most recent call last):\n#   File \"rantai-sebab-raise.py\", line 17, in kirim\n#     return cari_server(alamat)\n#   File \"rantai-sebab-raise.py\", line 12, in cari_server\n#     return SERVER[alamat]            # KeyError kalau alamatnya tak terdaftar\n#            ~~~~~~^^^^^^^^\n# KeyError: 'budi@contoh.id'\n#\n# The above exception was the direct cause of the following exception:\n#\n# Traceback (most recent call last):\n#   File \"rantai-sebab-raise.py\", line 31, in <module>\n#     kirim(\"budi@contoh.id\", gaya)\n#     ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n#   File \"rantai-sebab-raise.py\", line 21, in kirim\n#     raise GagalKirim(pesan) from err      # sebab EKSPLISIT\n#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n# GagalKirim: notifikasi ke budi@contoh.id tidak terkirim\n#\n# DUA traceback tercetak berurutan, disambung satu kalimat. Itulah rantai sebab.\n# Bacanya tetap sama: yang paling ATAS sebab paling awal, yang paling BAWAH error\n# yang akhirnya menghentikan program.\n#\n# Kalimat penyambungnya cuma ada dua, dan masing-masing punya arti pasti:\n#   \"The above exception was the direct cause of ...\"  <- kamu menulis 'from err'\n#   \"During handling of the above exception, ...\"      <- muncul OTOMATIS tanpa\n#                                                         'from', karena error baru\n#                                                         lahir di dalam blok except\n#\n# Python memilihnya dari tiga atribut yang tercetak di atas:\n#   __cause__ terisi                                   -> \"direct cause\"\n#   __cause__ None, __context__ terisi, suppress False -> \"During handling\"\n#   selain itu                                         -> tidak dicetak sama sekali\n#\n# Jadi beda ketiga gaya:\n#   from err     -> __cause__ terisi (dan suppress ikut True, karena sebabnya\n#                   sudah diwakili __cause__). Sengaja kamu nyatakan: ini sebabnya.\n#   tanpa from   -> __cause__ None, tapi __context__ tetap terisi sendiri. Jejaknya\n#                   tidak hilang, cuma tidak kamu AKUI sebagai sebab. Untuk error\n#                   yang kamu bungkus sendiri, 'from err' lebih jujur.\n#   from None    -> __cause__ None dan suppress True: KeyError-nya tidak dicetak\n#                   sama sekali. Pakai HANYA kalau sebab teknisnya benar-benar tak\n#                   berguna bagi pembaca -- ia menyembunyikan bukti.\n#\n# Kenapa membungkus error sama sekali? Supaya pemanggil tidak perlu tahu isi perut\n# fungsimu. Yang bocor keluar sebaiknya GagalKirim, bukan KeyError dari sebuah\n# dict yang kebetulan dipakai di dalam.\n\n# -------------------------------------------------------------------------\n# Di BATAS program: satu kalimat untuk pemakai, jejak lengkap untuk kamu.\n\ndef main():\n    kirim(\"budi@contoh.id\", \"from err\")\n\n\nprint(\"=\" * 66)\ntry:\n    main()\nexcept GagalKirim as e:                  # BUKAN except telanjang, bukan pass\n    print(\"Maaf,\", e)                    # yang dibaca pemakai\n    jejak = traceback.format_exc()       # STRING -> bisa ditulis ke berkas log\n    print(\"[baris terakhir jejak]\", jejak.strip().splitlines()[-1])\n    # with open(\"error.log\", \"a\") as f:\n    #     f.write(jejak)\n    # traceback.print_exc()  -> mencetak jejak yang sama langsung ke stderr\n\n# Maaf, notifikasi ke budi@contoh.id tidak terkirim\n# [baris terakhir jejak] GagalKirim: notifikasi ke budi@contoh.id tidak terkirim\n#\n# traceback.format_exc()  -> seluruh traceback sebagai satu string\n# traceback.print_exc()   -> mencetaknya ke stderr, persis seperti Python sendiri\n# Keduanya hanya bermakna DI DALAM blok except; di luar itu tidak ada error yang\n# sedang ditangani. Di program sungguhan, jejak ini masuk ke berkas log lewat\n# logging.exception() -- lihat materi Logging.",
            },
        ],
    },
    {
        "title": "28. Module & Package",
        "sections": [
            {
                "body": [
                    "Module = satu file .py yang berisi fungsi/class/variabel,",
                    "bisa di-import dan dipakai ulang di file lain.",
                    "Package = folder berisi banyak module (ditandai file __init__.py).",
                    "",
                    "Cara import:",
                    "  import math                    # import seluruh module",
                    "  from math import sqrt, pi      # import bagian tertentu saja",
                    "  import numpy as np             # import dengan alias",
                    "  from mypackage import mymodule # import dari package sendiri",
                ]
            },
            {
                "heading": "Contoh memakai module bawaan Python",
                "code": """import math
import random
import datetime

print(math.sqrt(16))        # 4.0
print(math.pi)               # 3.141592653589793
print(math.ceil(4.2))        # 5
print(math.floor(4.8))       # 4

print(random.randint(1, 10)) # angka acak 1-10
print(random.choice(["A", "B", "C"]))  # pilih acak dari list

sekarang = datetime.datetime.now()
print(sekarang.year, sekarang.month, sekarang.day)"""
            },
            {
                "body": [
                    "Membuat module sendiri:",
                    "  # file kalkulator.py",
                    "  def tambah(a, b):",
                    "      return a + b",
                    "",
                    "  # file main.py (folder yang sama)",
                    "  import kalkulator",
                    "  print(kalkulator.tambah(3, 4))   # 7",
                    "",
                    "if __name__ == \"__main__\": (idiom PENTING di Python)",
                    "  Kode di dalam blok ini HANYA jalan saat file dieksekusi",
                    "  LANGSUNG (python3 file.py), TIDAK jalan saat file di-import",
                    "  module lain. Berguna untuk kode testing/demo di file module.",
                    "",
                    "  def tambah(a, b):",
                    "      return a + b",
                    "",
                    "  if __name__ == \"__main__\":",
                    "      print(tambah(2, 3))   # hanya jalan jika file ini dieksekusi langsung",
                    "",
                    "PyPI (Python Package Index) & pip:",
                    "  pip install nama_package     -> install library eksternal",
                    "  pip freeze > requirements.txt -> catat semua dependency project",
                    "  pip install -r requirements.txt -> install semua dari catatan itu",
                ]
            },
        ],
    },
    {
        "title": "29. Struktur Project Python",
        "sections": [
            {
                "body": [
                    "Sampai sini setiap contoh masih berupa satu berkas .py. Project Python sungguhan",
                    "tidak pernah berbentuk begitu: ia sekumpulan folder dengan susunan yang nyaris sama",
                    "di semua repo. Materi Module & Package sudah menyebut bahwa paket itu folder",
                    "ber-__init__.py; sekarang kita lihat folder itu di tempat kerjanya.",
                    "",
                    "Kenapa perlu sekarang: saat kamu membuka repo Python orang lain, yang PERTAMA",
                    "terlihat bukan kodenya melainkan daftar berkas ini. Dan baris paling atas hampir",
                    "tiap berkas di dalamnya berbentuk 'from .sesuatu import X' - titik di depan nama,",
                    "yang belum pernah muncul sekali pun sebelum ini dan mustahil ditebak artinya.",
                    "",
                    "ISI SEBUAH REPO PYTHON, satu per satu:",
                    "",
                    "  <nama_paket>/   Kode yang sesungguhnya. Nama folder INI yang nanti diketik orang",
                    "                  di baris import, jadi pilih nama yang sah sebagai nama Python:",
                    "                  huruf kecil, tanpa spasi, tanpa tanda hubung.",
                    "  tests/          Berkas test (test_*.py). Sengaja DI LUAR paket: test tidak ikut",
                    "                  terpasang di komputer pemakai, dan memisahkannya membuktikan",
                    "                  paketmu bisa di-import dari luar, bukan cuma dari dalam dirinya.",
                    "  pyproject.toml  Identitas project. Dibahas di bawah.",
                    "  README.md       Penjelasan untuk manusia: project ini apa, cara pasang, cara pakai.",
                    "  .gitignore      Daftar berkas yang TIDAK ikut masuk ke Git.",
                    "  main.py         Titik masuk program, kalau memang berupa aplikasi. Boleh juga",
                    "                  bernama app.py atau cli.py; yang penting ia di luar paket.",
                    "",
                    "PYPROJECT.TOML - satu berkas yang menggantikan setup.py, setup.cfg, dan berkas",
                    "setelan berserakan milik tiap alat bantu. TOML adalah format setelan: [tabel] di",
                    "dalam kurung siku, lalu baris kunci = nilai, teks memakai tanda kutip.",
                    "",
                    "  [project]",
                    "  name = \"toko-online\"              # nama saat dipasang, boleh pakai tanda hubung",
                    "  version = \"0.1.0\"",
                    "  requires-python = \">=3.9\"         # versi Python paling tua yang didukung",
                    "  dependencies = [\"requests>=2.31\"] # library yang WAJIB ikut terpasang",
                    "",
                    "  [build-system]                    # alat untuk mengemas project jadi paket",
                    "  requires = [\"setuptools>=68\"]",
                    "  build-backend = \"setuptools.build_meta\"",
                    "",
                    "  [tool.ruff]                       # setelan alat lain menumpang di sini",
                    "  line-length = 100",
                    "",
                    "  [tool.pytest.ini_options]",
                    "  testpaths = [\"tests\"]",
                    "",
                    "Tiga jenis tabel itu punya pemilik berbeda: [project] dibaca pip, [build-system]",
                    "dibaca alat pengemas, dan [tool.apa_saja] dibaca alat yang namanya disebut. Kalau",
                    "kamu tidak memakai ruff, [tool.ruff] cuma teks yang diabaikan semua orang.",
                    "",
                    "Hubungannya dengan yang sudah kamu kenal:",
                    "  - requirements.txt (materi Virtual Environment) mencatat versi PERSIS hasil",
                    "    pip freeze, untuk menyusun ulang environment yang identik. dependencies di",
                    "    pyproject.toml menyebut BATAS yang project ini butuhkan. Banyak repo memakai",
                    "    keduanya: pyproject untuk niat, requirements untuk hasil yang terkunci.",
                    "  - setup.py adalah cara lama dengan tugas yang sama. Bentuknya skrip Python yang",
                    "    DIJALANKAN saat pemasangan - itu justru alasan ia ditinggalkan: berkas setelan",
                    "    tidak seharusnya bisa mengeksekusi apa pun. Repo lama masih banyak memakainya.",
                    "",
                    "__PYCACHE__/ dan berkas .pyc di dalamnya muncul sendiri, tanpa kamu ketik. Isinya",
                    "hasil terjemahan modul ke bytecode, dibuat saat sebuah modul DI-IMPORT (bukan saat",
                    "dijalankan langsung), supaya import berikutnya tidak perlu membaca ulang teksnya.",
                    "Isinya tidak terbaca manusia, terikat versi Python, dan bisa dibuat ulang kapan",
                    "saja - tiga alasan kenapa __pycache__/ selalu ada di .gitignore. Menghapusnya aman.",
                ],
            },
            {
                "heading": "Pohon folder sebuah project Python",
                "code": """toko-online/                 # folder akar project (nama bebas)
|-- pyproject.toml
|-- README.md
|-- .gitignore
|-- main.py                  # titik masuk, sengaja di luar paket
|-- toko/                    # PAKET -- inilah yang di-import orang
|   |-- __init__.py
|   |-- uang.py
|   |-- laporan.py
|   `-- model/               # subpaket: folder di dalam paket, ber-__init__.py juga
|       |-- __init__.py
|       `-- produk.py
`-- tests/
    |-- test_uang.py
    `-- test_produk.py""",
            },
            {
                "body": [
                    "__init__.py bukan berkas kosong yang cuma jadi penanda. Ia DIJALANKAN Python saat",
                    "paketnya pertama kali di-import, dan biasanya memikul tiga peran sekaligus:",
                    "  1. Penanda  - folder ini paket, bukan sekadar folder berisi berkas .py.",
                    "  2. Etalase  - mengangkat nama dari kedalaman ke permukaan, supaya pemakai cukup",
                    "                menulis 'from toko import Produk', bukan 'from toko.model.produk",
                    "                import Produk'. Struktur dalammu jadi bebas dirombak nanti tanpa",
                    "                merusak kode siapa pun.",
                    "  3. Tempat __all__.",
                    "",
                    "Sejak Python 3.3, folder tanpa __init__.py masih bisa di-import (namanya namespace",
                    "package). Jangan mengandalkan itu: tanpa __init__.py kamu kehilangan etalase, dan",
                    "salah ketik nama folder berubah jadi paket kosong yang diam-diam berhasil di-import",
                    "lalu gagal jauh di kemudian - error yang jauh lebih sulit dilacak.",
                    "",
                    "IMPORT RELATIF - arti titik di depan nama. Titik dihitung dari POSISI BERKAS yang",
                    "sedang ditulis, bukan dari folder tempat kamu mengetik perintah:",
                    "",
                    "  from . import uang                 . = paket tempat berkas ini berada",
                    "  from .uang import rupiah           ambil nama rupiah dari modul tetangga uang.py",
                    "  from .model.produk import Produk   turun ke subpaket model, lalu ke produk.py",
                    "  from ..uang import rupiah          .. = NAIK satu tingkat, ke paket induk",
                    "  from ...alat import bantu          ... = naik dua tingkat (jarang; kalau perlu",
                    "                                     sebanyak ini, biasanya strukturnya yang salah)",
                    "",
                    "Keunggulannya justru di situ: seluruh paket bisa diganti nama atau dipindah ke",
                    "project lain tanpa menyunting satu pun baris import di dalamnya. Import absolut",
                    "('from toko.uang import rupiah') menyebut nama paket, jadi ikut harus diubah.",
                    "Aturan praktis: relatif untuk saling memanggil DI DALAM paketmu, absolut untuk",
                    "memanggil paket luar.",
                    "",
                    "Dua jebakannya:",
                    "  - Import relatif hanya sah di dalam paket. Di berkas skrip biasa ia langsung",
                    "    gagal: ImportError: attempted relative import with no known parent package.",
                    "  - Bentuknya WAJIB 'from .modul import nama'. Tidak ada bentuk 'import .modul'.",
                    "",
                    "__all__ = [\"Produk\", \"rupiah\"] adalah daftar nama yang ikut terbawa saat orang",
                    "menulis 'from toko import *'. Tanpa __all__, bintang membawa semua nama yang tidak",
                    "diawali garis bawah - TERMASUK modul yang kebetulan kamu import di berkas itu",
                    "(os, json, sys) yang lalu menimpa nama bernama sama di kode pemakainya.",
                    "",
                    "__all__ tidak menyembunyikan apa pun: 'from toko.uang import rupiah' tetap jalan",
                    "walau rupiah tidak disebut di sana. Ia cuma mengatur bintang, dan dibaca alat",
                    "dokumentasi sebagai 'inilah antarmuka resmi paket ini'. Adapun import * sendiri",
                    "sebaiknya dihindari di kode biasa, justru karena kamu tidak bisa melihat nama apa",
                    "yang masuk hanya dengan membaca barisnya.",
                ],
            },
            {
                "heading": "Satu paket utuh: enam berkas yang saling memanggil",
                "body": [
                    "Buat foldernya persis seperti pohon di atas, lalu jalankan dari folder akar:",
                    "  python3 main.py         -> memakai paket lewat etalase __init__.py",
                    "  python3 -m toko.laporan -> menjalankan satu modul DARI DALAM paket",
                ],
                "code": "# File: toko/__init__.py\n\"\"\"Paket toko. Berkas INI yang dijalankan Python saat ada yang menulis `import toko`.\"\"\"\n\nfrom .uang import rupiah              # satu titik = modul tetangga, di paket yang sama\nfrom .model.produk import Produk      # titik lalu nama = turun ke subpaket model\n\n__all__ = [\"Produk\", \"rupiah\"]        # nama yang ikut terbawa `from toko import *`\n\n\n# File: toko/uang.py\ndef rupiah(jumlah):\n    \"\"\"12500 -> 'Rp12.500'\"\"\"\n    return \"Rp\" + format(jumlah, \",d\").replace(\",\", \".\")\n\n\n# File: toko/model/__init__.py\n# Boleh kosong. Yang penting keberadaannya: folder ini jadi subpaket, bukan folder biasa.\n\n\n# File: toko/model/produk.py\nfrom ..uang import rupiah             # DUA titik = naik satu tingkat, ke paket toko\n\n\nclass Produk:\n    def __init__(self, nama, harga):\n        self.nama = nama\n        self.harga = harga\n\n    def label(self):\n        return f\"{self.nama} - {rupiah(self.harga)}\"\n\n\n# File: toko/laporan.py\nfrom .model.produk import Produk      # satu titik: mulai dari paket toko\n\n\ndef ringkas(barang):\n    return \"\\n\".join(b.label() for b in barang)\n\n\nif __name__ == \"__main__\":            # jalankan: python3 -m toko.laporan\n    print(ringkas([Produk(\"Kopi\", 25000), Produk(\"Gula\", 12500)]))\n\n\n# File: main.py\nfrom toko import Produk, rupiah       # cukup 'toko' -- itu gunanya __init__.py\n\nbarang = [Produk(\"Kopi\", 25000), Produk(\"Gula\", 12500)]\nfor b in barang:\n    print(b.label())\nprint(\"Total:\", rupiah(sum(b.harga for b in barang)))\n\n# Keluaran python3 main.py:\n# Kopi - Rp25.000\n# Gula - Rp12.500\n# Total: Rp37.500",
            },
            {
                "heading": "Kenapa import-nya gagal, dan obatnya",
                "body": [
                    "Dua pesan error ini menunggu setiap orang yang baru memakai paketnya sendiri.",
                    "",
                    "1. ImportError: attempted relative import with no known parent package",
                    "   Muncul saat kamu menjalankan berkas yang ada DI DALAM paket secara langsung:",
                    "     python3 toko/laporan.py",
                    "   Berkas yang dijalankan langsung diberi __name__ == \"__main__\" dan tidak punya",
                    "   paket induk sama sekali. Titik di 'from .model.produk import Produk' jadi tidak",
                    "   menunjuk apa-apa. Berkas yang sama baik-baik saja begitu ia DI-IMPORT.",
                    "",
                    "2. ModuleNotFoundError: No module named 'toko'",
                    "   Python mencari modul menyusuri daftar folder di sys.path, dan entri pertamanya",
                    "   adalah folder BERKAS YANG DIJALANKAN - bukan folder tempat kamu berdiri. Jadi",
                    "   'python3 skrip/coba.py' yang dijalankan dari akar project memasukkan skrip/ ke",
                    "   sys.path, dan toko/ di sebelahnya tidak pernah terlihat.",
                    "",
                    "Obatnya satu bentuk perintah: jalankan sebagai MODUL, dari folder akar project.",
                    "  python3 -m toko.laporan     titik, bukan garis miring, dan tanpa akhiran .py",
                    "  python3 -m pytest           pytest melihat folder sekarang, bukan folder pytest",
                    "-m menaruh folder sekarang di sys.path lalu mengimpor modul yang kamu sebut SEBAGAI",
                    "bagian dari paketnya - sehingga paket induknya dikenal dan titiknya punya arti.",
                    "",
                    "Jangan menambalnya dengan sys.path.append(\"..\") di dalam kode. Itu memindahkan",
                    "kesalahan ke tempat yang lebih sulit dilihat dan patah begitu berkasnya dipanggil",
                    "dari folder lain. Untuk project yang sudah punya pyproject.toml, cara paling bersih",
                    "adalah 'pip install -e .' di dalam venv: nama paketmu terdaftar sekali, lalu bisa",
                    "di-import dari folder mana pun tanpa satu baris kode tambahan.",
                    "",
                    "Program di bawah ini memperlihatkan mesinnya - jalankan apa adanya:",
                ],
                "code": """# Melihat langsung cara Python menemukan -- dan gagal menemukan -- sebuah modul
import sys
import json
import json.decoder

# 1. Hasil import cuma objek biasa, bukan sihir
print(type(json).__name__)              # module
print(json.__name__)                    # json

# 2. Modul yang sudah di-import dicatat di sys.modules dan tidak dibaca ulang
print("json" in sys.modules)            # True
print(sys.modules["json"] is json)      # True

# 3. Tiap modul tahu siapa PAKET INDUKNYA. Inilah yang dihitung oleh titik.
print(json.__spec__.parent)             # json  (paket: induknya dirinya sendiri)
print(json.decoder.__spec__.parent)     # json  (modul di dalam paket json)

# 4. Berkas yang dijalankan langsung tidak punya paket induk sama sekali
print(__name__)                         # __main__
print(repr(__spec__))                   # None

# 5. Karena itu titik di depan nama tidak menunjuk apa pun di berkas ini
try:
    exec("from .uang import rupiah")
except ImportError as e:
    # relatif gagal: attempted relative import with no known parent package
    print("relatif gagal:", e)

# 6. Sedangkan nama absolut yang tidak ada di satu pun folder sys.path
try:
    import paket_yang_tidak_ada
except ModuleNotFoundError as e:
    print("absolut gagal:", e)          # No module named 'paket_yang_tidak_ada'""",
            },
        ],
    },
    {
        "title": "30. Program Baris Perintah: sys, os & argparse",
        "sections": [
            {
                "body": [
                    "Sampai sini, satu-satunya cara program menerima data dari luar adalah input(): program",
                    "berhenti, menunggu orang mengetik, baru lanjut. Program sungguhan hampir tidak pernah",
                    "begitu - datanya disebut di baris perintahnya, jadi bisa dijalankan penjadwal atau skrip",
                    "lain tanpa ada orang yang menungguinya.",
                    "",
                    "  python3 ringkas.py laporan.txt -n 3 --huruf-besar",
                    "",
                    "  ringkas.py     -> berkas program yang dijalankan",
                    "  laporan.txt    -> argumen POSISI: artinya ditentukan URUTANNYA",
                    "  -n 3           -> OPSI bernilai (bentuk panjangnya --baris 3), letaknya bebas",
                    "  --huruf-besar  -> OPSI saklar/flag: ditulis berarti hidup, tidak ditulis berarti mati",
                    "",
                    "sys.argv - daftar mentah semua itu, sudah disiapkan Python sebelum barismu jalan:",
                    "",
                    "  import sys",
                    "  sys.argv       -> ['ringkas.py', 'laporan.txt', '-n', '3']",
                    "  sys.argv[0]    -> nama/jalur berkas PROGRAMNYA SENDIRI, bukan argumen pertama",
                    "  sys.argv[1:]   -> bagian yang benar-benar diberikan pemakai",
                    "  len(sys.argv)  -> 1 kalau program dijalankan tanpa argumen sama sekali",
                    "",
                    "  Dua hal yang paling sering menjebak:",
                    "  1. Isi sys.argv SELALU str. '3' bukan 3; lupa int() bikin '3' * 2 jadi '33', bukan 6.",
                    "  2. Kata python3 TIDAK ikut tercatat. Daftarnya mulai dari nama berkasnya.",
                    "",
                    "sys.exit(kode) - berhenti sekarang juga, sekaligus melapor berhasil atau gagal:",
                    "",
                    "  sys.exit(0)        -> selesai baik-baik (0 juga otomatis kalau program habis normal)",
                    "  sys.exit(1)        -> ada yang salah; angka apa pun selain 0 berarti GAGAL",
                    "  sys.exit(\"pesan\")  -> cetak pesan itu ke stderr, lalu keluar dengan kode 1",
                    "",
                    "  Error yang tidak ditangkap juga membuat program keluar dengan kode 1 sendirinya.",
                    "  sys.exit() bekerja dengan melempar SystemExit, jadi 'except:' polos bisa menelannya",
                    "  dan program malah menolak berhenti saat disuruh berhenti.",
                    "",
                    "Angka itu namanya exit code - satu-satunya cara terminal tahu program tadi sukses:",
                    "",
                    "  echo $?              # Linux/Mac: lihat kode keluar perintah terakhir",
                    "  echo %ERRORLEVEL%    # Windows (cmd)",
                    "  ./a.py && ./b.py     # b.py HANYA jalan kalau a.py keluar dengan kode 0",
                    "",
                    "Karena itu pesan error dicetak ke stderr: 'python3 alat.py > hasil.txt' mengalihkan",
                    "stdout ke berkas, sementara errornya tetap terlihat dan tidak ikut mengotori hasil.",
                    "Program yang mencetak 'gagal!' tapi keluar dengan kode 0 tetap akan dikira berhasil",
                    "oleh alat mana pun yang memanggilnya.",
                ],
            },
            {
                "heading": "Membaca argumen sendiri lewat sys.argv",
                "code": """import sys

# sys.argv SELALU list of str. Indeks 0 adalah berkas programnya sendiri,
# jadi argumen dari pemakai mulai dari indeks 1.
print("Dijalankan sebagai :", sys.argv[0])
print("Argumen dari luar  :", sys.argv[1:])
print("Banyaknya bagian   :", len(sys.argv))

angka = sys.argv[1:]
if not angka:
    # Dijalankan tanpa argumen: pakai contoh bawaan supaya tetap ada hasilnya.
    angka = ["10", "20", "12"]
    print("(tanpa argumen, dipakai contoh:", " ".join(angka) + ")")

total = 0
for teks in angka:
    try:
        total += int(teks)      # int() WAJIB: isi argv itu str, "3" bukan 3
    except ValueError:
        # Pesan error ke stderr, bukan stdout, supaya tidak mengotori hasil.
        print(f"Bukan angka: {teks}", file=sys.stderr)
        sys.exit(1)             # berhenti SEKARANG dan lapor gagal ke terminal

print("Total:", total)

# Simpan sebagai jumlah.py, lalu coba ketiganya di terminal dan perhatikan
# kode keluarnya:
#   python3 jumlah.py           -> Total: 42    (lalu ketik: echo $?  ->  0)
#   python3 jumlah.py 5 7 100   -> Total: 112   (echo $?  ->  0)
#   python3 jumlah.py 5 tujuh   -> Bukan angka: tujuh   (echo $?  ->  1)""",
            },
            {
                "heading": "Alat baris perintah yang layak dipakai: argparse",
                "code": "#!/usr/bin/env python3\n# Baris pertama di atas dijelaskan di bagian terakhir materi ini.\n\"\"\"ringkas - menampilkan beberapa baris pertama sebuah berkas teks.\"\"\"\nimport argparse\n\n\ndef buat_parser():\n    p = argparse.ArgumentParser(\n        prog=\"ringkas\",\n        description=\"Menampilkan beberapa baris pertama sebuah berkas teks.\")\n    # Argumen POSISI: wajib ada, artinya ditentukan urutannya.\n    p.add_argument(\"berkas\", help=\"berkas yang akan dibaca\")\n    # OPSI: boleh ada boleh tidak, ditandai - atau --, urutannya bebas.\n    # type=int mengubah \"3\" jadi 3 sekaligus menolak isian yang bukan angka.\n    p.add_argument(\"-n\", \"--baris\", type=int, default=5,\n                   help=\"berapa baris ditampilkan (default: 5)\")\n    # store_true = saklar tanpa nilai: ditulis -> True, tidak ditulis -> False.\n    p.add_argument(\"--huruf-besar\", action=\"store_true\",\n                   help=\"ubah hasilnya jadi HURUF BESAR\")\n    return p\n\n\ndef main():\n    parser = buat_parser()\n    # Bentuk sebenarnya cuma:  args = parser.parse_args()\n    # yang membaca sys.argv[1:] sendiri. Daftarnya ditulis di sini supaya\n    # contoh ini bisa langsung dicoba tanpa mengetik argumen apa pun.\n    args = parser.parse_args([\"laporan.txt\", \"-n\", \"3\", \"--huruf-besar\"])\n\n    print(args)                          # sebuah Namespace berisi hasil parsing\n    print(\"args.berkas      :\", args.berkas)\n    print(\"args.baris       :\", args.baris, \"->\", type(args.baris))\n    print(\"args.huruf_besar :\", args.huruf_besar)   # --huruf-besar, tanda - jadi _\n\n    print()\n    print(\"Ini yang keluar kalau orang mengetik:  ringkas --help\")\n    print(\"-\" * 52)\n    parser.print_help()\n\n\nif __name__ == \"__main__\":\n    main()",
            },
            {
                "body": [
                    "Yang barusan terjadi, dan kenapa hampir tidak ada yang menulis parsernya sendiri:",
                    "",
                    "  - parse_args() mengembalikan Namespace: dibaca args.nama, bukan args[\"nama\"].",
                    "  - Nama atributnya dirapikan - awalan -- dibuang dan tanda - jadi _ - sehingga",
                    "    --huruf-besar dibaca args.huruf_besar. Ini bikin bingung kalau tidak diberi tahu.",
                    "  - --help dan -h muncul GRATIS, dirakit dari description dan tiap help=. Itu sebabnya",
                    "    help= layak ditulis serius: itulah dokumentasi programmu yang sesungguhnya.",
                    "  - Argumen wajib yang tidak diberikan: argparse mencetak cara pemakaian ke stderr lalu",
                    "    keluar dengan kode 2. Itu perilaku yang benar, bukan program yang rusak.",
                    "  - Di Python lawas judul di --help tertulis 'optional arguments:', bukan 'options:'.",
                    "  - Kalau nanti perlu: nargs=\"+\" (banyak nilai jadi satu list), choices=[...] (batasi",
                    "    pilihan), required=True, dan add_subparsers() untuk perintah bertingkat seperti",
                    "    'git commit' dan 'git push'.",
                    "",
                    "SHEBANG - baris pertama yang BUKAN komentar biasa:",
                    "",
                    "  #!/usr/bin/env python3",
                    "",
                    "  Diawali #, jadi Python memang mengabaikannya. Tapi dua karakter pertamanya (#!)",
                    "  dibaca SISTEM OPERASI, bukan Python, dan artinya: 'kalau berkas ini dijalankan",
                    "  langsung, serahkan isinya ke program berikut'.",
                    "",
                    "    chmod +x ringkas.py        # tandai berkasnya boleh dieksekusi, cukup sekali",
                    "    ./ringkas.py laporan.txt   # jalan tanpa mengetik python3 lagi",
                    "",
                    "  - Harus baris PERTAMA. Di baris kedua ia benar-benar cuma komentar biasa.",
                    "  - Tulis /usr/bin/env python3, bukan /usr/bin/python3: env mencari python3 lewat",
                    "    PATH, jadi skripnya ikut memakai python3 milik venv yang sedang aktif.",
                    "  - Lupa chmod +x -> ./ringkas.py ditolak dengan 'Permission denied'.",
                    "  - Windows tidak memakai shebang; di sana tetap python ringkas.py.",
                    "",
                    "python3 -m PAKET - menjalankan modul, bukan berkas:",
                    "",
                    "    python3 -m venv venv        # -m yang sama sudah kamu pakai di materi venv & pip",
                    "    python3 -m pytest           # pytest milik python3 ini, bukan yang lain di PATH",
                    "    python3 -m http.server 8000",
                    "    python3 -m alatku           # menjalankan sebuah PAKET buatan sendiri",
                    "",
                    "  Sebuah paket bisa dijalankan begitu kalau di dalamnya ada berkas __main__.py",
                    "  (bertetangga dengan __init__.py); isinya biasanya cuma memanggil main() di balik",
                    "  if __name__ == \"__main__\" - idiom dari materi Module & Package. Kenapa -m juga",
                    "  menyembuhkan ImportError dibahas di materi Struktur Project Python.",
                ],
            },
            {
                "heading": "os: environment, jalur berkas & memanggil program lain",
                "code": """import os
import subprocess
import sys

# --- 1. Konfigurasi dibaca dari environment, bukan ditulis di dalam kode ---
# Ini cara baku menaruh alamat database, kunci API, dan mode jalan: kalau
# ditulis di dalam kode, rahasianya ikut terbawa saat kodenya dibagikan.
# getenv(nama, default): nilai cadangan dipakai kalau variabelnya belum diset,
# jadi program tetap jalan di komputer mana pun tanpa disunting.
db = os.getenv("DATABASE_URL", "sqlite:///lokal.db")
mode = os.getenv("MODE", "development")
print("DATABASE_URL :", db)
print("MODE         :", mode)

# os.environ berkelakuan seperti dict berisi SEMUA variabel lingkungan.
print("PATH terdaftar?      ", "PATH" in os.environ)
print("Variabel yang tak ada:", os.environ.get("BELUM_DISET", "(tidak ada)"))
# os.environ["BELUM_DISET"] melempar KeyError -- .get()/getenv() yang aman.

# --- 2. Merangkai jalur berkas tanpa mengetik pemisahnya sendiri ---
jalur = os.path.join("data", "laporan", "januari.csv")
print("join     :", jalur)
print("basename :", os.path.basename(jalur))   # nama berkasnya saja
print("dirname  :", os.path.dirname(jalur))    # foldernya saja
print("splitext :", os.path.splitext(jalur))   # pisah nama dan ekstensi
print("exists   :", os.path.exists(jalur))     # False, foldernya memang belum ada
# Padanan modernnya pathlib (materi File I/O):
#   p = Path("data") / "laporan" / "januari.csv"
#   p.name, p.parent, p.suffix, p.exists()

# --- 3. Menjalankan program lain dari dalam Python ---
# sys.executable = python3 yang sedang menjalankan berkas ini.
hasil = subprocess.run([sys.executable, "--version"],
                       capture_output=True, text=True, check=True)
print("keluaran :", hasil.stdout.strip())   # str, karena text=True
print("exit code:", hasil.returncode)       # 0; check=True melempar kalau bukan 0

# Perintahnya diberikan sebagai LIST, satu kata satu elemen -- BUKAN satu
# string panjang. shell=True terlihat lebih gampang, dan di situ jebakannya:
#   nama = "catatan.txt; rm -rf ~"          <- misalnya nama ini kiriman pemakai
#   subprocess.run(f"wc -l {nama}", shell=True)   # JANGAN: DUA perintah ikut jalan
#   subprocess.run(["wc", "-l", nama])            # aman: tetap satu nama berkas""",
            },
        ],
    },
    {
        "title": "31. Logging: Pengganti print di Program Sungguhan",
        "sections": [
            {
                "body": [
                    "Sampai sejauh ini, satu-satunya cara program kita bercerita tentang dirinya",
                    "sendiri adalah print(). Untuk belajar itu memang pas. Tapi di kode yang benar-benar",
                    "dipakai orang, print() untuk MELAPORKAN KEADAAN program hampir tidak pernah ada.",
                    "Yang dipakai adalah modul logging - bawaan Python, tidak perlu pip install.",
                    "",
                    "Bedakan dulu dua pekerjaan yang gampang tertukar:",
                    "  - print() = MENYAJIKAN HASIL kepada pemakai. Tabel, jawaban, laporan akhir.",
                    "    Ini tetap print(), selamanya, dan tidak ada yang salah dengannya.",
                    "  - logging  = MENCERITAKAN JALANNYA program kepada yang merawatnya. \"mulai\",",
                    "    \"50 baris diproses\", \"gagal menyimpan\", \"koneksi putus\".",
                    "Yang digantikan logging cuma pekerjaan kedua.",
                    "",
                    "Kenapa print() tidak cukup untuk pekerjaan kedua - tiga hal yang tidak bisa ia lakukan:",
                    "",
                    "  1. Tidak punya TINGKAT KEPENTINGAN.",
                    "     Bagi print(), \"sedang mengecek isi variabel\" dan \"database mati\" sama saja.",
                    "     Padahal yang pertama cuma perlu terlihat saat kamu berburu bug, dan yang",
                    "     kedua harus terlihat selamanya. Tanpa tingkat, keduanya menumpuk jadi satu",
                    "     dinding teks - dan yang penting tenggelam di antara yang tidak penting.",
                    "",
                    "  2. TUJUANNYA tidak bisa dipindahkan.",
                    "     print() selalu ke layar. Program yang jalan sebagai layanan di server tidak",
                    "     punya layar yang ditonton siapa pun; ketika ia rusak jam dua pagi, satu-satunya",
                    "     petunjuk yang tersisa adalah apa yang sempat tertulis ke BERKAS. print()",
                    "     tidak bisa dialihkan ke berkas tanpa menyunting kodenya satu per satu.",
                    "",
                    "  3. Tidak bisa DIMATIKAN tanpa menyentuh kode.",
                    "     Ini yang melahirkan kebiasaan buruk paling umum: menaburkan print() saat",
                    "     melacak bug, lalu menghapusinya sebelum kode dikirim. Bug yang sama muncul",
                    "     lagi bulan depan, dan semua jejak yang dulu susah payah dipasang sudah",
                    "     dihapus. Dengan logging, baris itu TIDAK dihapus - ia cuma didiamkan,",
                    "     dan dinyalakan lagi lewat satu angka saat dibutuhkan.",
                    "",
                    "Itu sebabnya baris logging.getLogger(__name__) ada di puncak ribuan berkas Python",
                    "di luar sana. Setelah materi ini, baris itu tidak asing lagi saat kamu membacanya.",
                ],
            },
            {
                "heading": "Menyalakan logging: basicConfig dan lima levelnya",
                "code": """import logging

# Satu baris ini menyalakan logging sekaligus menentukan BATAS bawahnya:
# pesan yang levelnya DI BAWAH INFO tidak ditampilkan sama sekali.
logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s | %(name)s | %(message)s")

logging.debug("nilai sementara x = 42")   # hilang tanpa suara: DEBUG di bawah INFO
logging.info("program mulai")
logging.warning("berkas konfigurasi tidak ada, memakai nilai bawaan")
logging.error("gagal menyimpan data ke berkas")
logging.critical("koneksi database putus, program berhenti")

print("ini print biasa, tidak ada urusannya dengan logging")

# Yang tercetak:
# INFO | root | program mulai
# WARNING | root | berkas konfigurasi tidak ada, memakai nilai bawaan
# ERROR | root | gagal menyimpan data ke berkas
# CRITICAL | root | koneksi database putus, program berhenti
# ini print biasa, tidak ada urusannya dengan logging
#
# Dua hal untuk diperhatikan:
#   1. Baris debug TIDAK muncul, dan program juga tidak protes. Ia disaring.
#   2. Nama logger-nya "root" karena kita memanggil logging.info() langsung.
#      Cara yang lebih baik ada di bagian berikutnya.
#
# Coba ganti INFO jadi logging.WARNING di basicConfig lalu jalankan lagi:
# dua baris teratas ikut lenyap, tanpa satu pun baris log disunting.""",
            },
            {
                "body": [
                    "Lima level, dari yang paling remeh ke yang paling gawat. Angka di tengah itu",
                    "nilai sesungguhnya - level bekerja sebagai PERBANDINGAN ANGKA, bukan kategori:",
                    "",
                    "  DEBUG     10   detail untuk dirimu sendiri saat melacak bug: isi variabel,",
                    "                 fungsi apa dipanggil dengan argumen apa.",
                    "  INFO      20   kejadian normal yang wajar dicatat: \"server jalan di port 8000\",",
                    "                 \"120 baris diproses\", \"berkas ditulis\".",
                    "  WARNING   30   ada yang aneh, program MASIH jalan: konfigurasi tidak ketemu,",
                    "                 memakai nilai cadangan. Ini level BAWAAN kalau kamu diam saja.",
                    "  ERROR     40   satu pekerjaan GAGAL, tapi program belum mati.",
                    "  CRITICAL  50   program tidak bisa lanjut sama sekali.",
                    "",
                    "level=logging.INFO berarti \"tampilkan yang nilainya >= 20\". Tidak ada sihir lain",
                    "di balik itu. Karena itu menaikkan level = mendiamkan yang di bawahnya.",
                    "",
                    "Isi format: potongan %(...)s yang boleh kamu susun sesukamu.",
                    "",
                    "  %(asctime)s     waktu pesan dibuat     2026-01-05 09:41:12,317",
                    "  %(levelname)s   nama levelnya          WARNING",
                    "  %(name)s        nama logger-nya        toko.pembayaran",
                    "  %(message)s     pesannya sendiri       saldo tidak cukup",
                    "  %(filename)s    berkas pemanggilnya    pembayaran.py",
                    "  %(lineno)d      nomor barisnya         57",
                    "  %(funcName)s    nama fungsinya         potong_saldo",
                    "",
                    "Susunan yang paling sering kamu temui di kode nyata:",
                    "  format=\"%(asctime)s %(levelname)-8s [%(name)s] %(message)s\"",
                    "  2026-01-05 09:41:12,317 WARNING  [toko.pembayaran] saldo tidak cukup",
                    "(angka -8 pada %(levelname)-8s cuma meratakan lebar kolomnya biar sejajar.)",
                    "",
                    "logger = logging.getLogger(__name__)  -- baris yang ada di mana-mana itu",
                    "",
                    "Di sini __name__ dipakai dengan cara yang BERBEDA dari yang kamu kenal di materi",
                    "Module & Package. Dua-duanya sering dilihat orang tanpa sadar itu hal yang sama:",
                    "  - if __name__ == \"__main__\":   __name__ dipakai sebagai BAHAN PERBANDINGAN;",
                    "    yang dipakai hasilnya, True atau False.",
                    "  - getLogger(__name__)          __name__ dipakai sebagai NILAI; yang dipakai",
                    "    isinya, yaitu sebuah string.",
                    "",
                    "Isi string itu apa persis:",
                    "  berkas dijalankan langsung (python3 app.py)  ->  __name__ berisi \"__main__\"",
                    "  berkas di-import sebagai module              ->  __name__ berisi nama module,",
                    "                                                   misalnya \"toko.pembayaran\"",
                    "",
                    "Jadi getLogger(__name__) memberi setiap berkas sebuah logger bernama sesuai",
                    "posisinya sendiri, tanpa kamu pernah mengetik nama itu. Pindahkan berkasnya ke",
                    "folder lain, namanya ikut berubah sendiri. Itulah kenapa bentuk ini menang atas",
                    "getLogger(\"pembayaran\") yang namanya diketik tangan lalu basi diam-diam.",
                    "",
                    "Titik di dalam nama membentuk keluarga: \"toko.pembayaran\" adalah anak dari",
                    "\"toko\". Dan itu bukan sekadar rapi - anak mewarisi pengaturan induknya:",
                    "",
                    "  logging.getLogger(\"toko\").setLevel(logging.DEBUG)",
                    "  # seluruh logger di bawah \"toko\" ikut jadi DEBUG, tanpa satu berkas pun disunting",
                    "",
                    "Di situlah janji \"bisa dinyalakan tanpa menyentuh kode\" ditepati: kamu bisa",
                    "membuka keran DEBUG untuk satu bagian program yang dicurigai saja, dan membiarkan",
                    "sisanya tetap tenang. Di program baris perintah (materi sebelumnya), keran itu",
                    "biasanya disambungkan ke sebuah flag:",
                    "",
                    "  p.add_argument(\"-v\", \"--verbose\", action=\"store_true\")",
                    "  args = p.parse_args()",
                    "  logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)",
                    "",
                    "Sejak itu, \"aku mau lihat detailnya\" cukup jadi urusan mengetik -v saat menjalankan",
                    "program - bukan lagi urusan menyunting lalu mengembalikan kode.",
                ],
            },
            {
                "heading": "Log ke berkas, dan logger.exception di dalam except",
                "code": """import logging

# filename= mengalihkan SELURUH log ke berkas. Setelah baris ini tidak ada satu
# pun baris log yang muncul di layar -- semuanya masuk ke app.log.
logging.basicConfig(
    filename="app.log",
    filemode="w",     # "w" = tulis ulang dari kosong; "a" (bawaan) = menyambung
    level=logging.DEBUG,
    format="%(levelname)-8s [%(name)s] %(message)s",
)

logger = logging.getLogger(__name__)


def bagi(a, b):
    # Nilainya dikirim sebagai ARGUMEN (%s), bukan dirangkai dengan f-string.
    logger.debug("bagi dipanggil: a=%s b=%s", a, b)
    try:
        hasil = a / b
    except ZeroDivisionError:
        # exception() = error() + traceback lengkapnya, dalam satu panggilan.
        # Hanya bermakna DI DALAM blok except.
        logger.exception("pembagian gagal")
        return None
    logger.info("hasilnya %s", hasil)
    return hasil


print("__name__ di berkas ini :", __name__)
print("nama logger            :", logger.name)
print("bagi(10, 2) ->", bagi(10, 2))
print("bagi(10, 0) ->", bagi(10, 0))

logging.shutdown()    # pastikan yang masih tertahan benar-benar tertulis

print("--- isi app.log ---")
with open("app.log") as f:
    print(f.read(), end="")

# Yang tercetak di layar:
# __name__ di berkas ini : __main__
# nama logger            : __main__
# bagi(10, 2) -> 5.0
# bagi(10, 0) -> None
# --- isi app.log ---
# DEBUG    [__main__] bagi dipanggil: a=10 b=2
# INFO     [__main__] hasilnya 5.0
# DEBUG    [__main__] bagi dipanggil: a=10 b=0
# ERROR    [__main__] pembagian gagal
# Traceback (most recent call last):
#   File "app.py", line 18, in bagi
#     hasil = a / b
# ZeroDivisionError: division by zero
#
# Perhatikan: nama logger-nya "__main__" karena berkas ini DIJALANKAN langsung.
# Kalau berkas yang sama di-import module lain, namanya berubah sendiri.
# Traceback di dalam log itu bukan hasil print terpisah -- satu panggilan
# logger.exception() yang membawanya, lengkap sampai baris penyebabnya.
# (jalur berkas & nomor barisnya menyesuaikan berkasmu sendiri.)""",
            },
            {
                "body": [
                    "Jebakan yang benar-benar menjebak:",
                    "",
                    "  1. \"Programku tidak mencetak apa-apa\" - hampir selalu soal LEVEL.",
                    "     Kalau basicConfig tidak pernah dipanggil, level bawaannya WARNING, jadi",
                    "     semua logger.info() dan logger.debug() lenyap. Tidak ada error, tidak ada",
                    "     peringatan, cuma sunyi - dan itu yang membuatnya lama dicari. Sebelum",
                    "     curiga kodenya rusak, turunkan dulu levelnya ke logging.DEBUG.",
                    "",
                    "  2. basicConfig hanya berlaku SEKALI, panggilan berikutnya diabaikan diam-diam.",
                    "     Begitu root logger sudah punya handler, basicConfig tidak berbuat apa-apa",
                    "     lagi - termasuk kalau yang memasang handler itu logging.warning() yang",
                    "     kebetulan kamu panggil lebih dulu (fungsi jalan pintas itu memanggil",
                    "     basicConfig sendiri). Akibatnya format dan level barumu tidak pernah",
                    "     berlaku, tanpa satu keluhan pun. Panggil basicConfig SEKALI di paling atas",
                    "     program utamamu. Kalau memang harus menimpa: basicConfig(..., force=True).",
                    "",
                    "  3. logger.exception() di luar blok except menghasilkan \"NoneType: None\".",
                    "     Ia mengambil traceback dari exception yang SEDANG ditangani; di luar except",
                    "     tidak ada apa-apa untuk diambil. Kalau perlu traceback pada level lain:",
                    "     logger.error(\"...\", exc_info=True) atau logger.debug(\"...\", exc_info=True).",
                    "     exception() sendiri selalu berlevel ERROR.",
                    "",
                    "  4. Jangan rakit pesannya dengan f-string.",
                    "       logger.debug(f\"data = {data}\")     # dirakit SELALU, walau nanti dibuang",
                    "       logger.debug(\"data = %s\", data)     # dirakit HANYA kalau jadi ditampilkan",
                    "     Bentuk kedua menyerahkan perakitan ke logging, yang tidak akan repot kalau",
                    "     pesannya toh disaring level. Pada debug di dalam loop panas, bedanya nyata.",
                    "",
                    "  5. Log keluar lewat stderr, bukan stdout.",
                    "     Jadi  python3 app.py > catatan.txt  tidak menangkap satu baris log pun -",
                    "     yang perlu  2> catatan.txt. Di aplikasi ini pun, \"Coba jalankan\" menampilkan",
                    "     baris log di bagian pesan error, bukan di bagian keluaran. Itu normal, bukan",
                    "     tanda programnya gagal.",
                    "",
                    "  6. Jangan panggil basicConfig di dalam module yang di-import.",
                    "     Yang berhak memutuskan ke mana log pergi adalah program utama, bukan",
                    "     potongan yang dipakainya. Module cukup punya logger = getLogger(__name__)",
                    "     lalu memakainya; kalau tidak ada yang mengonfigurasi, pesannya memang tidak",
                    "     ke mana-mana, dan itu justru perilaku yang benar.",
                    "",
                    "  7. Berkas log tumbuh selamanya kalau dibiarkan. Project sungguhan memakai",
                    "     logging.handlers.RotatingFileHandler supaya berkasnya dipotong dan didaur",
                    "     ulang setelah ukuran tertentu. Cukup tahu namanya untuk sekarang.",
                    "",
                    "  8. Jangan pernah mencatat password, token, atau nomor kartu ke log. Berkas log",
                    "     adalah benda yang paling sering dikirim ke orang lain saat berburu bug.",
                    "",
                    "Satu catatan kecil: logging.warn() (tanpa -ing) sudah usang dan bakal hilang;",
                    "yang benar logging.warning(). Kamu masih akan melihatnya di kode lama.",
                ],
            },
        ],
    },
    {
        "title": "32. Tanggal & Waktu (datetime)",
        "sections": [
            {
                "body": [
                    "Hampir semua program sungguhan menyentuh waktu: kapan pesanan dibuat, berapa lama",
                    "sebuah proses berjalan, apakah sesi login sudah kedaluwarsa. Di materi Module &",
                    "Package datetime baru lewat sekilas lewat .now(); di sini kita bongkar isinya.",
                    "",
                    "Modul datetime berisi EMPAT class utama:",
                    "  date       -> tanggal saja                  date(2005, 8, 17)",
                    "  time       -> jam saja, tanpa tanggal       time(14, 30, 0)",
                    "  datetime   -> tanggal + jam sekaligus       datetime(2024, 3, 1, 14, 30)",
                    "  timedelta  -> DURASI, bukan titik waktu     timedelta(days=7, hours=3)",
                    "",
                    "Bedakan baik-baik dua yang terakhir. datetime menjawab \"kapan\", timedelta",
                    "menjawab \"berapa lama\". Tanggal dikurangi tanggal menghasilkan durasi, dan",
                    "tanggal ditambah durasi menghasilkan tanggal lagi - seperti aljabar biasa.",
                    "",
                    "Jebakan pertama, dan ini kena ke semua orang: MODUL-nya bernama datetime, dan",
                    "ada CLASS bernama datetime di dalamnya. Itu sebabnya kode orang lain kelihatan",
                    "berbeda-beda padahal maksudnya sama:",
                    "  import datetime                  -> tulisnya  datetime.datetime.now()",
                    "  from datetime import datetime    -> tulisnya  datetime.now()",
                    "Pilih satu gaya lalu konsisten. Gaya kedua yang paling sering dipakai di kode",
                    "nyata, dan itu yang dipakai di materi ini.",
                    "",
                    "Mengambil waktu SEKARANG dari jam komputer:",
                    "  datetime.now()   -> tanggal + jam saat ini",
                    "  date.today()     -> tanggal hari ini saja",
                    "Keduanya bukan konstanta: dipanggil dua kali, hasilnya berbeda. Karena itu",
                    "contoh di bawah memakai tanggal TETAP - supaya keluarannya bisa dipastikan,",
                    "dan supaya kamu bisa membandingkan hasil di layarmu dengan komentarnya.",
                ],
            },
            {
                "heading": "Membuat tanggal, membacanya, dan berhitung dengan timedelta",
                "code": """from datetime import date, datetime, timedelta

# Dibuat manual, bukan dari jam komputer: tahun, bulan, tanggal
lahir = date(2005, 8, 17)
print(lahir)                        # 2005-08-17
print(lahir.year, lahir.month, lahir.day)   # 2005 8 17

# datetime = tanggal + jam dalam satu objek
jadwal = datetime(2024, 3, 1, 14, 30, 0)
print(jadwal)                       # 2024-03-01 14:30:00
print(jadwal.hour, jadwal.minute)   # 14 30
print(jadwal.date())                # 2024-03-01  (ambil bagian date-nya saja)
print(jadwal.weekday())             # 4  -> Senin=0, jadi 4 berarti Jumat

# Menambah waktu WAJIB lewat timedelta.
# "jadwal + 7" langsung = TypeError, karena 7 itu apa? hari? detik?
minggu_depan = jadwal + timedelta(days=7)
print(minggu_depan)                 # 2024-03-08 14:30:00
print(jadwal - timedelta(hours=3))  # 2024-03-01 11:30:00

# Selisih dua datetime menghasilkan timedelta, bukan angka biasa
selisih = minggu_depan - jadwal
print(selisih)                      # 7 days, 0:00:00
print(selisih.days)                 # 7
print(selisih.total_seconds())      # 604800.0

# Umur dalam hari = selisih dua date
umur = date(2024, 3, 1) - lahir
print(umur.days, "hari")            # 6771 hari""",
            },
            {
                "body": [
                    "Yang dilakukan kode nyata pada tanggal hampir selalu salah satu dari dua hal:",
                    "mengubahnya jadi TEKS untuk disimpan/ditampilkan, atau membaca TEKS jadi",
                    "tanggal lagi. Dua method itulah yang harus kamu hafal:",
                    "",
                    "  strftime  = string format time  ->  objek datetime  jadi  teks",
                    "  strptime  = string parse time   ->  teks            jadi  objek datetime",
                    "",
                    "PENTING: \"%Y-%m-%d\" BUKAN %-formatting string yang dibahas di materi String &",
                    "Formatting (\"Umur: %d\" % umur). Bentuknya kebetulan mirip, artinya lain sama",
                    "sekali. Ini bahasa mini milik datetime, dan %d di sini berarti TANGGAL, bukan",
                    "bilangan bulat. Jangan pernah menebak artinya dari kemiripan itu.",
                    "",
                    "Kode format yang paling sering ditemui:",
                    "  %Y  tahun 4 digit      2024      %y  tahun 2 digit        24",
                    "  %m  bulan 2 digit      03        %B  nama bulan           March",
                    "  %d  tanggal 2 digit    01        %b  nama bulan singkat   Mar",
                    "  %H  jam 24-an (00-23)  14        %A  nama hari            Friday",
                    "  %I  jam 12-an (01-12)  02        %a  nama hari singkat    Fri",
                    "  %M  menit              30        %p  AM atau PM           PM",
                    "  %S  detik              00        %%  tanda persen sendiri %",
                    "",
                    "Jebakan yang paling mahal: %m itu BULAN, %M itu MENIT. Besar-kecil huruf",
                    "menentukan, dan salah ketik TIDAK menghasilkan error - hanya tanggal keliru",
                    "yang diam-diam tersimpan, dan baru ketahuan berbulan-bulan kemudian.",
                    "",
                    "%A dan %B mengikuti locale sistem; pada setelan bawaan hasilnya Inggris",
                    "(\"Friday\"), bukan \"Jumat\". Pakai keduanya untuk TAMPILAN saja, jangan untuk",
                    "data yang disimpan - kalau tidak, berkasmu berubah arti pindah mesin.",
                    "",
                    "strptime menuntut polanya cocok PERSIS, termasuk garis miring dan strip-nya.",
                    "Kalau tidak cocok, ia melempar ValueError, bukan mengembalikan None. Jadi",
                    "bungkus try/except (materi Exception Handling) setiap kali teksnya datang dari",
                    "pengguna atau dari berkas yang tidak kamu tulis sendiri.",
                ],
            },
            {
                "heading": "strftime, strptime, dan ISO 8601",
                "code": """from datetime import datetime

jadwal = datetime(2024, 3, 1, 14, 30, 0)

# datetime -> teks
print(jadwal.strftime("%Y-%m-%d"))         # 2024-03-01
print(jadwal.strftime("%d/%m/%Y %H:%M"))   # 01/03/2024 14:30
print(jadwal.strftime("%d %B %Y"))         # 01 March 2024  (nama bulan ikut locale)

# teks -> datetime
lahir = datetime.strptime("17/08/2005", "%d/%m/%Y")
print(lahir)                               # 2005-08-17 00:00:00
print(type(lahir))                         # <class 'datetime.datetime'>
print(lahir.year)                          # 2005

# Pola yang tidak cocok melempar ValueError, bukan mengembalikan None
try:
    datetime.strptime("2005-08-17", "%d/%m/%Y")
except ValueError as e:
    print("gagal:", e)
# gagal: time data '2005-08-17' does not match format '%d/%m/%Y'

# ISO 8601: bentuk baku untuk MENYIMPAN dan menukar waktu
teks_iso = jadwal.isoformat()
print(teks_iso)                            # 2024-03-01T14:30:00
kembali = datetime.fromisoformat(teks_iso)
print(kembali == jadwal)                   # True""",
            },
            {
                "body": [
                    "Kenapa ISO 8601 (\"2024-03-01T14:30:00\") jadi format baku di mana-mana:",
                    "  - Urutannya tahun-bulan-tanggal, jadi diurutkan sebagai TEKS biasa pun",
                    "    urutan waktunya tetap benar. Itu alasan praktis yang besar sekali.",
                    "  - Tidak ambigu. \"03/01/2024\" itu 3 Januari atau 1 Maret? Tergantung negara,",
                    "    dan tidak ada di dalam teksnya sendiri yang bisa menjawab.",
                    "  - .isoformat() menulisnya, datetime.fromisoformat() membacanya kembali,",
                    "    tanpa kamu perlu mengarang pola strftime sendiri.",
                    "Aturan praktisnya: SIMPAN dalam ISO, TAMPILKAN dengan strftime.",
                    "Catatan versi: sebelum Python 3.11, fromisoformat() hanya sanggup membaca",
                    "bentuk yang persis dikeluarkan isoformat(), dan menolak akhiran \"Z\".",
                    "",
                    "Naive vs aware - istilah yang akan kamu temui di pesan error:",
                    "  naive  -> tidak tahu zona waktunya. Ini bawaan datetime(2024, 3, 1, 14, 30).",
                    "  aware  -> membawa zona waktu di dalam dirinya.",
                    "",
                    "  from datetime import datetime, timezone, timedelta",
                    "  utc = datetime(2024, 3, 1, 14, 30, tzinfo=timezone.utc)",
                    "  print(utc.isoformat())                # 2024-03-01T14:30:00+00:00",
                    "  wib = utc.astimezone(timezone(timedelta(hours=7)))",
                    "  print(wib.isoformat())                # 2024-03-01T21:30:00+07:00",
                    "",
                    "Mencampur keduanya berakhir di:",
                    "  TypeError: can't subtract offset-naive and offset-aware datetimes",
                    "Error ini khas muncul di produksi, bukan saat ngoding: satu sisi datang dari",
                    "database (aware) dan satu lagi dibuat di kode (naive). Yang dilakukan server",
                    "sungguhan: simpan SEMUA waktu dalam UTC, ubah ke zona lokal hanya sesaat",
                    "sebelum ditampilkan ke orang.",
                    "",
                    "Terakhir, modul time - BEDA dari class datetime.time, dan gampang tertukar",
                    "kalau kamu menulis 'from datetime import time' di berkas yang sama:",
                    "  time.time()          -> detik sejak 1 Januari 1970 (epoch), sebuah float",
                    "  time.sleep(2)        -> menjeda program 2 detik",
                    "  time.perf_counter()  -> khusus MENGUKUR durasi, lebih teliti dari time.time()",
                    "  datetime.fromtimestamp(detik)  -> epoch kembali jadi datetime (zona lokal);",
                    "                                    beri timezone.utc kalau mau hasil pasti",
                    "Decorator pengukur waktu di materi Decorator & Context Manager memakai",
                    "time.time(); untuk pengukuran serius, perf_counter() pilihan yang lebih tepat.",
                ],
            },
        ],
    },
    {
        "title": "33. File I/O",
        "sections": [
            {
                "body": [
                    "File I/O = membaca dan menulis data ke file.",
                    "",
                    "Fungsi bawaan open() dengan MODE:",
                    "  'r'  -> read (baca), error jika file tak ada (default)",
                    "  'w'  -> write (tulis), MENGHAPUS isi lama jika file sudah ada",
                    "  'a'  -> append (tambah di akhir, tidak menghapus isi lama)",
                    "  'x'  -> exclusive create, error jika file SUDAH ada",
                    "  'r+' -> baca & tulis sekaligus",
                    "",
                    "SELALU gunakan 'with' statement (context manager) agar file",
                    "otomatis tertutup walau terjadi error - INI CARA STANDAR PYTHON.",
                    "",
                    "Dan untuk berkas TEKS, selalu tulis encoding=\"utf-8\" juga:",
                    "  with open(\"catatan.txt\", \"w\", encoding=\"utf-8\") as f:",
                    "",
                    "Tanpa argumen itu Python memakai encoding bawaan SISTEM, dan bawaan",
                    "tiap sistem berbeda-beda (Linux/Mac umumnya UTF-8, Windows lama sering",
                    "cp1252). Akibatnya berkas berisi 'e' beraksen, huruf Arab, atau emoji",
                    "yang tertulis mulus di komputermu bisa gagal dibaca di komputer orang",
                    "lain dengan UnicodeDecodeError - padahal kodenya terlihat benar, dan kamu",
                    "tidak bisa mereproduksi errornya. Menuliskannya membuat hasilnya sama",
                    "di mana pun. Semua contoh di bawah memakainya.",
                    "",
                    "Semua mode di atas adalah mode TEKS: yang masuk dan keluar bertipe str.",
                    "Menambahkan huruf b (\"rb\", \"wb\") membuka berkas sebagai BINER, yang",
                    "bekerja dengan bytes dan tidak memakai encoding sama sekali - untuk",
                    "gambar, PDF, dan sejenisnya. Itu, berikut apa sebenarnya encoding,",
                    "dibahas di materi Encoding, bytes & Berkas Biner tepat sesudah ini.",
                ]
            },
            {
                "heading": "Contoh menulis & membaca file teks",
                "code": """# Menulis file
with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Baris pertama\\n")
    f.write("Baris kedua\\n")
# file otomatis tertutup setelah keluar dari blok 'with'

# Membaca SELURUH isi file sekaligus
with open("catatan.txt", "r", encoding="utf-8") as f:
    isi = f.read()
    print(isi)

# Membaca baris per baris (hemat memori untuk file besar)
with open("catatan.txt", "r", encoding="utf-8") as f:
    for baris in f:
        print("Baca:", baris.strip())   # strip() buang newline

# Membaca semua baris jadi list
with open("catatan.txt", "r", encoding="utf-8") as f:
    semua_baris = f.readlines()
    print(semua_baris)   # ['Baris pertama\\n', 'Baris kedua\\n']

# Menambah data tanpa menghapus isi lama
with open("catatan.txt", "a", encoding="utf-8") as f:
    f.write("Baris tambahan\\n")"""
            },
            {
                "heading": "Bekerja dengan file JSON (format data paling umum)",
                "code": """import json

data = {"nama": "Andi", "umur": 20, "hobi": ["coding", "gaming"]}

# Menulis dict ke file JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Membaca file JSON jadi dict Python
with open("data.json", "r", encoding="utf-8") as f:
    hasil = json.load(f)
    print(hasil["nama"])   # Andi

# Konversi string <-> JSON tanpa file
teks_json = json.dumps(data)     # dict -> string JSON
data_lagi = json.loads(teks_json)  # string JSON -> dict"""
            },
            {
                "body": [
                    "Menangani error file (file tidak ada, dsb):",
                    "  try:",
                    "      with open(\"tidak_ada.txt\", encoding=\"utf-8\") as f:",
                    "          isi = f.read()",
                    "  except FileNotFoundError:",
                    "      print(\"File tidak ditemukan!\")",
                    "",
                    "Modul pathlib (cara modern kelola path file, lebih OOP):",
                    "  from pathlib import Path",
                    "  p = Path(\"data\") / \"catatan.txt\"",
                    "  print(p.exists())      # cek file ada atau tidak",
                    "  print(p.read_text(encoding=\"utf-8\"))   # baca isi file langsung",
                ]
            },
        ],
    },
    {
        "title": "34. Encoding, bytes & Berkas Biner",
        "sections": [
            {
                "body": [
                    "Di memori, teks Python adalah str: deretan KARAKTER (huruf, emoji, aksara Arab).",
                    "Di dalam berkas dan di kabel jaringan tidak ada karakter - yang ada cuma BYTE,",
                    "yaitu angka 0-255. Sesuatu harus menerjemahkan antara keduanya.",
                    "",
                    "Penerjemah itu namanya ENCODING, dan yang menang di dunia nyata adalah UTF-8:",
                    "  - huruf ASCII (a-z, 0-9, tanda baca) tetap 1 byte, jadi berkas lama tetap terbaca,",
                    "  - huruf beraksen (é, ü) 2 byte, aksara Asia 3 byte, emoji 4 byte.",
                    "",
                    "Materi 17 mendaftar mode open() dengan lengkap. Yang belum disebut di sana justru",
                    "parameter kedua yang paling sering ditulis orang di kode nyata:",
                    "",
                    "  with open(\"data.txt\", encoding=\"utf-8\") as f:",
                    "      isi = f.read()",
                    "",
                    "Tanpa encoding=, Python memakai default SISTEM, dan defaultnya tidak seragam:",
                    "  Linux & macOS  ->  hampir selalu UTF-8",
                    "  Windows        ->  sering cp1252 atau cp1250, tergantung setelan negara",
                    "",
                    "Akibatnya kode yang mulus di laptopmu bisa gagal di komputer orang lain padahal",
                    "berkasnya sama persis. Itu jenis bug paling menyebalkan: tidak bisa ditiru sendiri.",
                    "",
                    "Aturan praktisnya satu kalimat: SETIAP open() untuk teks, tulis encoding=\"utf-8\".",
                    "Versi Python baru pelan-pelan bergerak ke UTF-8 sebagai default, tapi jangan menunggu.",
                    "Yang eksplisit benar di semua versi dan di semua sistem.",
                ],
            },
            {
                "heading": "str vs bytes: dua tipe yang mirip di layar, beda total di dalam",
                "code": """teks = "Cafe berhasil"          # str  -> deretan karakter
data = teks.encode("utf-8")     # bytes -> deretan angka 0-255

print(type(teks), len(teks))    # <class 'str'> 13
print(type(data), len(data))    # <class 'bytes'> 13  (semua ASCII, 1 byte/karakter)

aksen = "Café"                       # 4 karakter di layar
print(len(aksen))                       # 4
print(len(aksen.encode("utf-8")))       # 5    <- é sendirian memakan 2 byte
print(aksen.encode("utf-8"))            # b'Caf\\xc3\\xa9'

# Literal bytes ditandai awalan b. Isinya HANYA boleh ASCII;
# byte lain WAJIB ditulis sebagai \\xNN.
sapaan = b"Halo"
print(sapaan[0])      # 72     <- indexing bytes menghasilkan INT, bukan "H"
print(sapaan[0:1])    # b'H'   <- slicing tetap bytes

# str + bytes = TypeError. Python 3 sengaja MENOLAK menebak encoding-nya,
# karena tebakan yang salah merusak data tanpa memberi tahu siapa pun.
try:
    print("Halo " + b"dunia")
except TypeError as e:
    print("TypeError:", e)

# Bolak-balik dengan tabel yang sama selalu aman:
print(data.decode("utf-8") == teks)     # True

# Bolak-balik dengan tabel yang SALAH sering TIDAK error - ia cuma diam:
print(aksen.encode("utf-8").decode("cp1252"))   # CafÃ©  <- mojibake, tanpa satu pun error

# Kalau karakternya tidak ada di tabel tujuan, barulah menulis pun gagal:
try:
    "π".encode("ascii")            # pi
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)
""",
            },
            {
                "body": [
                    "Kalau tabelnya salah saat MEMBACA, Python berhenti dengan pesan seperti ini:",
                    "",
                    "  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:",
                    "  invalid continuation byte",
                    "",
                    "Bacalah potong per potong, jangan sebagai satu kalimat asing:",
                    "  'utf-8' codec         -> tabel yang KAMU minta (lewat encoding=, atau default sistem)",
                    "  byte 0xe9             -> byte yang tidak masuk akal menurut tabel itu",
                    "  in position 5         -> byte ke-5 pada potongan yang sedang dibaca",
                    "  invalid continuation  -> alasannya: UTF-8 menunggu byte lanjutan, yang datang bukan",
                    "",
                    "0xe9 kebetulan adalah huruf e beraksen di tabel Latin-1/cp1252. Jadi pesan ini hampir",
                    "selalu berarti salah satu dari dua hal:",
                    "  1. Berkasnya memang bukan UTF-8 - biasanya lahir dari Excel atau Notepad di Windows.",
                    "  2. Berkasnya bukan teks sama sekali (gambar, PDF, zip) tapi dibuka dengan mode teks.",
                    "",
                    "Urutan penanganan, dari yang paling benar ke jalan darurat:",
                    "  1. Cari tahu encoding aslinya lalu sebutkan:  open(p, encoding=\"cp1252\")",
                    "  2. Kalau isinya biner, yang diganti MODE-nya jadi \"rb\" - bukan encoding-nya.",
                    "  3. Baru sesudah itu:",
                    "       open(p, encoding=\"utf-8\", errors=\"replace\")  -> byte rusak jadi karakter �",
                    "       open(p, encoding=\"utf-8\", errors=\"ignore\")   -> byte rusak DIHAPUS diam-diam",
                    "",
                    "errors= tidak memperbaiki apa pun; ia menukar error dengan data rusak. Pakai untuk log",
                    "yang cuma dibaca manusia, JANGAN untuk data yang akan disimpan lagi - kerusakannya",
                    "ikut tersimpan dan tidak ada yang memberi tahu.",
                    "",
                    "Jebakan terbesar di bagian ini: encoding=\"latin-1\" TIDAK PERNAH gagal membaca, karena",
                    "ke-256 byte punya arti di tabel itu. Ia bukan menyelamatkanmu, cuma mengganti error",
                    "dengan teks kacau (mojibake) yang baru ketahuan berbulan-bulan kemudian.",
                    "",
                    "Kembarannya saat MENULIS bernama UnicodeEncodeError - lihat contoh terakhir di atas.",
                ],
            },
            {
                "heading": "Mode biner: \"rb\" dan \"wb\" untuk gambar, PDF, dan berkas apa pun",
                "code": """import base64
import hashlib

# Tambahkan huruf "b" pada mode -> TIDAK ada penerjemahan apa pun.
# Yang keluar-masuk adalah bytes mentah, persis seperti di disk.

data = b"\\x89PNG\\r\\n\\x1a\\n" + bytes([0, 1, 2, 250])
with open("contoh.bin", "wb") as f:     # perhatikan: TIDAK ada encoding=
    f.write(data)                       # f.write() di sini menuntut bytes

with open("contoh.bin", "rb") as f:
    isi = f.read()                      # hasilnya bytes, bukan str

print(type(isi), len(isi))              # <class 'bytes'> 12
print(isi[:4])                          # b'\\x89PNG'
print(isi[:8] == b"\\x89PNG\\r\\n\\x1a\\n")  # True -> 8 byte pertama = tanda pengenal PNG

# Menyalin berkas apa pun (gambar, PDF, zip) selalu lewat mode biner.
# Menyalinnya lewat mode teks akan merusaknya: Python mencoba men-decode isinya.
with open("contoh.bin", "rb") as sumber, open("salinan.bin", "wb") as tujuan:
    tujuan.write(sumber.read())
print(open("salinan.bin", "rb").read() == data)   # True

# hashlib dan base64 HANYA menerima bytes. Inilah sebabnya .encode("utf-8")
# begitu sering terlihat menempel tepat sebelum keduanya di kode orang.
sidik = hashlib.sha256("rahasia".encode("utf-8")).hexdigest()
print(sidik[:16])                       # 16 karakter pertama sidik jari isi

sandi = base64.b64encode(b"pengguna:12345")
print(sandi)                            # b'cGVuZ2d1bmE6MTIzNDU='
print(base64.b64decode(sandi).decode("utf-8"))   # pengguna:12345

# base64 bukan enkripsi, cuma cara menitipkan bytes lewat jalur yang
# hanya sanggup membawa teks (URL, JSON, header HTTP, email).
""",
            },
            {
                "body": [
                    "Satu sisa jebakan yang menempel pada berkas teks: akhir baris tidak sama di tiap sistem.",
                    "  Linux & macOS  ->  satu byte LF     \\n",
                    "  Windows        ->  dua byte CR LF   \\r\\n",
                    "",
                    "Mode teks menyembunyikan beda itu (universal newlines). Saat MEMBACA, \\r\\n diubah jadi",
                    "\\n; saat MENULIS, \\n diubah balik ke akhir baris khas sistem yang menjalankannya.",
                    "Mode biner tidak menerjemahkan apa pun - di sanalah kamu melihat byte yang sebenarnya.",
                    "",
                    "Terjemahan otomatis itu berguna, sampai ada modul yang mengurus akhir barisnya sendiri.",
                    "Modul csv menulis \\r\\n sendiri. Kalau berkasnya dibuka tanpa newline=\"\", di Windows",
                    "\\n miliknya diterjemahkan sekali lagi jadi \\r\\r\\n, dan tiap baris data dipisahkan",
                    "satu baris kosong. Karena itu resep bakunya selalu ditulis begini:",
                    "",
                    "  with open(\"data.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as f:",
                    "",
                    "newline=\"\" berarti: jangan sentuh akhir baris, aku yang urus. Bukan berarti tanpa baris.",
                    "",
                    "BOM: Notepad dan Excel di Windows menyimpan tiga byte penanda (EF BB BF) di awal berkas.",
                    "Dibuka dengan encoding=\"utf-8\", byte itu menjadi satu karakter tak terlihat \\ufeff yang",
                    "menempel di kolom pertama - lalu perbandingan sepolos baris[0] == \"nama\" gagal tanpa",
                    "sebab yang kelihatan. Obatnya encoding=\"utf-8-sig\" saat MEMBACA: ia memakan BOM itu",
                    "kalau ada, dan diam saja kalau tidak ada.",
                    "",
                    "Catatan penutup: encoding= dan newline= hanya sah di mode teks. Menuliskannya bersama",
                    "\"rb\" atau \"wb\" langsung ValueError - dan itu wajar, karena di mode biner memang tidak",
                    "ada yang perlu diterjemahkan.",
                ],
            },
        ],
    },
    {
        "title": "35. Regular Expression (modul re)",
        "sections": [
            {
                "body": [
                    "Ada pekerjaan teks yang bentuknya selalu itu-itu saja: \"ambil semua angka di baris log",
                    "ini\", \"periksa apakah teks ini berbentuk email\", \"rapikan spasi yang bertumpuk jadi satu\".",
                    "Semuanya bisa dikerjakan dengan .find(), .split(), dan perulangan - tapi kodenya panjang,",
                    "dan tiap variasi kecil berarti menulis ulang logikanya dari nol.",
                    "",
                    "Regular expression (sering disingkat regex atau regexp) adalah BAHASA MINI untuk",
                    "mendeskripsikan POLA teks. Satu baris pola menggantikan belasan baris pencarian manual.",
                    "Bahasa ini bukan milik Python - ia juga ada di JavaScript, Java, grep, dan editor kode -",
                    "jadi yang kamu pelajari di sini terpakai di banyak tempat lain.",
                    "Di Python mesinnya ada di modul BAWAAN bernama re, tidak perlu pip install apa pun:",
                    "",
                    "  import re",
                    "",
                    "Yang bikin bingung saat pertama membaca kode orang: polanya hampir selalu didahului r.",
                    "",
                    "  re.sub(r\"\\s+\", \" \", teks)",
                    "",
                    "Huruf r itu BUKAN salah ketik dan bukan singkatan \"regex\". Itu raw string, yang sudah",
                    "dibahas di materi Masukan, Keluaran & Modul Bawaan: backslash di dalamnya dibiarkan apa",
                    "adanya, tidak diterjemahkan Python.",
                    "",
                    "Kenapa raw string WAJIB di sini, bukan sekadar kebiasaan?",
                    "Karena backslash punya arti di DUA tempat sekaligus, dan Python selalu jalan duluan.",
                    "Python menerjemahkan isi string dulu; SISANYA baru diserahkan ke mesin regex.",
                    "",
                    "  \"\\b\"   Python mengubahnya jadi SATU karakter backspace (kode 8). Mesin regex tidak",
                    "         pernah melihat backslash-b, jadi polanya tidak akan pernah cocok - dan tidak",
                    "         ada pesan error apa pun, hasilnya cuma daftar kosong.",
                    "  r\"\\b\"  DUA karakter: backslash dan b. Mesin regex membacanya sebagai \"batas kata\",",
                    "         yang memang kita maksud.",
                    "",
                    "Beberapa kombinasi seperti \"\\d\" dan \"\\s\" kebetulan selamat karena Python tidak mengenalnya",
                    "sebagai escape sequence, sehingga backslash-nya dibiarkan. Jangan bersandar pada kebetulan",
                    "itu: Python 3.12+ sudah memperingatkannya (SyntaxWarning: invalid escape sequence \"\\d\"),",
                    "dan versi mendatang akan menjadikannya error.",
                    "",
                    "Aturan praktis yang tidak perlu dipikir lagi: setiap pola regex ditulis r\"...\". Selalu.",
                ],
            },
            {
                "heading": "Bahan dasar pola",
                "body": [
                    "Mencocokkan SATU karakter:",
                    "  .          satu karakter apa saja KECUALI newline",
                    "  \\d  \\D     satu digit 0-9   /   satu karakter yang BUKAN digit",
                    "  \\w  \\W     huruf, angka, atau underscore   /   kebalikannya",
                    "  \\s  \\S     whitespace (spasi, tab, newline)   /   kebalikannya",
                    "  [abc]      salah satu dari a, b, atau c",
                    "  [a-z0-9]   rentang: satu huruf kecil atau satu digit",
                    "  [^abc]     apa saja KECUALI a, b, c  (tanda ^ di DALAM kurung siku berarti negasi)",
                    "",
                    "Berapa kali diulang (kuantifier - berlaku untuk hal tepat SEBELUMNYA):",
                    "  a+         satu atau lebih          a*      nol atau lebih",
                    "  a?         nol atau satu (opsional) a{3}    tepat tiga kali",
                    "  a{2,5}     dua sampai lima kali     a{2,}   dua kali atau lebih",
                    "  a+?        versi MALAS: ambil sesedikit mungkin (lihat bagian jebakan)",
                    "",
                    "Jangkar dan pengelompokan:",
                    "  ^          awal teks (atau awal tiap baris kalau flag re.MULTILINE menyala)",
                    "  $          akhir teks (atau akhir tiap baris)",
                    "  \\b         batas kata: r\"\\bkota\\b\" cocok dengan \"kota\", tapi tidak dengan \"kotak\"",
                    "  |          alternasi alias \"atau\": kucing|anjing",
                    "  (...)      grup: mengelompokkan DAN menangkap isinya supaya bisa diambil belakangan",
                    "  (?:...)    grup yang hanya mengelompokkan, TIDAK menangkap",
                    "",
                    "Karakter dengan arti khusus:  . ^ $ * + ? { } [ ] \\ | ( )",
                    "Untuk mencocokkan karakter itu sendiri, dahului backslash:",
                    "  r\"3.14\"    juga cocok dengan \"3x14\", karena titik berarti \"apa saja\"",
                    "  r\"3\\.14\"   hanya cocok dengan \"3.14\"",
                    "Kalau teks yang dicari datang dari variabel (misalnya ketikan pengguna), jangan menebak",
                    "mana yang perlu di-escape - pakai re.escape(teks), ia melucuti semuanya sekaligus.",
                ],
            },
            {
                "heading": "Fungsi-fungsi modul re",
                "code": """import re

teks = "Order A-19 dikirim, order B-204 tertunda, order C-7 batal."

# search  -> cari kecocokan PERTAMA di mana pun; hasilnya objek Match atau None
m = re.search(r"[A-Z]-\\d+", teks)
print(m.group(0))            # A-19
print(m.start(), m.end())    # 6 10

# match   -> hanya mencoba dari AWAL string (bukan berarti "seluruhnya cocok")
print(re.match(r"[A-Z]-\\d+", teks))       # None, teks diawali "Order"
print(re.match(r"Order", teks).group(0))  # Order

# fullmatch -> seluruh string harus habis dipakai polanya
print(bool(re.fullmatch(r"\\d{4}", "2024")))    # True
print(bool(re.fullmatch(r"\\d{4}", "2024x")))   # False

# findall -> semua kecocokan sekaligus, langsung berupa list of str
print(re.findall(r"[A-Z]-\\d+", teks))     # ['A-19', 'B-204', 'C-7']

# finditer -> sama, tapi tiap hasilnya objek Match (jadi tahu posisinya)
for cocok in re.finditer(r"[A-Z]-(\\d+)", teks):
    print(cocok.group(0), "nomornya", cocok.group(1), "di indeks", cocok.start())

# sub -> ganti semua kecocokan; split -> pecah string memakai pola sebagai pemisah
print(re.sub(r"\\d+", "#", teks))
print(re.split(r",\\s*", teks))""",
            },
            {
                "heading": "Objek Match, grup bernama, re.compile & flag",
                "body": [
                    "Tiga fungsi (search, match, fullmatch) mengembalikan objek Match, bukan string.",
                    "  .group(0)      seluruh bagian teks yang cocok",
                    "  .group(1)      isi grup tangkap pertama, .group(2) yang kedua, dan seterusnya",
                    "  .group(\"jam\")  isi grup BERNAMA yang ditulis (?P<jam>...) di polanya",
                    "  .groupdict()   semua grup bernama sekaligus, langsung berbentuk dict",
                    "  .start() .end() posisi kecocokan di dalam teks aslinya",
                    "",
                    "re.compile(pola) mengubah pola jadi objek yang bisa dipakai berulang. Untuk pola yang",
                    "dipanggil di dalam perulangan atau di beberapa tempat, ini lebih cepat sekaligus lebih",
                    "rapi: polanya jadi satu konstanta bernama, bukan string yang disalin ke mana-mana.",
                    "",
                    "Flag mengubah CARA mencocokkan (boleh digabung dengan tanda |):",
                    "  re.IGNORECASE  huruf besar/kecil dianggap sama",
                    "  re.MULTILINE   ^ dan $ berlaku per BARIS, bukan per seluruh teks",
                    "  re.DOTALL      titik ikut cocok dengan newline",
                    "  re.VERBOSE     spasi & komentar di dalam pola diabaikan, untuk pola panjang",
                ],
                "code": "import re\n\nLOG = \"\"\"08:15:02 INFO  server siap di port 8080\n08:15:44 ERROR koneksi gagal setelah 3 percobaan\n08:16:10 warn  memori terpakai 87 persen\"\"\"\n\n# Pola dikompilasi SEKALI, lalu dipakai berkali-kali.\n# (?P<nama>...) = grup tangkap BERNAMA, jauh lebih terbaca daripada group(2).\nPOLA = re.compile(\n    r\"^(?P<jam>\\d{2}:\\d{2}:\\d{2})\\s+(?P<level>INFO|WARN|ERROR)\\s+(?P<pesan>.+)$\",\n    re.MULTILINE | re.IGNORECASE,\n)\n# MULTILINE : tanpa ini ^ dan $ hanya cocok di ujung SELURUH teks, bukan tiap baris\n# IGNORECASE: baris \"warn\" ikut cocok. Flag mengubah cara mencocokkan, bukan hasilnya.\n\nfor cocok in POLA.finditer(LOG):\n    print(cocok.group(0))                     # seluruh bagian yang cocok\n    print(\"  jam   :\", cocok.group(\"jam\"))\n    print(\"  level :\", cocok.group(2))        # grup ke-2 = grup bernama \"level\"\n    print(\"  angka :\", re.findall(r\"\\d+\", cocok.group(\"pesan\")))\n\nsatu = POLA.search(\"09:00:00 ERROR disk penuh\")\nprint(satu.groupdict())   # {'jam': '09:00:00', 'level': 'ERROR', 'pesan': 'disk penuh'}\n\n# Memeriksa format email SEDERHANA. fullmatch dipakai supaya tidak ada sisa\n# karakter di kiri/kanan. Titik ditulis \\. karena titik polos = \"apa saja\".\nPOLA_EMAIL = re.compile(r\"[\\w.+-]+@[\\w-]+\\.[\\w.]+\")\nfor alamat in [\"budi@contoh.co.id\", \"budi@@contoh\", \"budi contoh.id\"]:\n    print(alamat, \"->\", bool(POLA_EMAIL.fullmatch(alamat)))\n\n# search mengembalikan None kalau tidak ketemu -> cek dulu sebelum .group()\nhasil = re.search(r\"\\d+\", \"tidak ada angka di sini\")\nprint(hasil.group(0) if hasil else \"tidak ada angka\")\n\n# Merapikan spasi berlebih: satu atau lebih whitespace jadi satu spasi biasa\nkotor = \"  Belajar   Python\\tsampai\\n\\nbisa  \"\nprint(repr(re.sub(r\"\\s+\", \" \", kotor).strip()))   # 'Belajar Python sampai bisa'\n\n# Di string PENGGANTI, \\1 (atau \\g<jam>) menunjuk isi grup tangkap\nprint(re.sub(r\"(\\d{2}):(\\d{2}):(\\d{2})\", r\"\\1.\\2\", \"08:15:02 INFO server siap\"))",
            },
            {
                "heading": "Jebakan, dan kapan JANGAN memakai regex",
                "body": [
                    "1. Lupa r\"...\". Penyebab nomor satu keluhan \"polaku sudah benar tapi tidak pernah cocok\".",
                    "2. re.match BUKAN \"cocok seluruhnya\", ia cuma menambatkan ke AWAL string. Kalau maksudmu",
                    "   \"seluruh teks harus berbentuk begini\", yang benar re.fullmatch.",
                    "3. Memanggil .group() pada None. Kalau tidak ketemu, hasilnya None, dan Python menjawab",
                    "   AttributeError: 'NoneType' object has no attribute 'group'. Simpan ke variabel dulu,",
                    "   cek, baru pakai.",
                    "4. findall BERUBAH PERILAKU begitu polanya punya grup tangkap: tanpa grup ia memberi",
                    "   seluruh kecocokan, dengan satu grup ia memberi isi grup itu saja, dengan dua grup",
                    "   atau lebih ia memberi tuple. Kalau kurungnya cuma untuk mengelompokkan, tulis (?:...).",
                    "5. Kuantifier itu SERAKAH: .+ mengambil sepanjang mungkin lalu mundur secukupnya.",
                    "   Tambahkan ? di belakangnya untuk versi malas.",
                    "6. Titik tidak pernah cocok dengan newline, kecuali flag re.DOTALL dinyalakan.",
                    "",
                    "Kapan regex adalah alat yang SALAH:",
                    "  HTML / XML  ->  pakai parser sungguhan (html.parser di stdlib). Tag boleh bersarang",
                    "                  tanpa batas, dan regex secara matematis tidak sanggup menghitung sarang;",
                    "                  pola yang \"hampir jalan\" gagal di halaman pertama yang sedikit berbeda.",
                    "  JSON        ->  json.loads. Sudah ada, sudah benar, dan mengerti escape di dalamnya.",
                    "  CSV         ->  modul csv. Koma di dalam tanda kutip (\"Jakarta, Pusat\") merusak setiap",
                    "                  pemisahan naif.",
                    "  Path berkas ->  pathlib / os.path, seperti di materi File I/O.",
                    "",
                    "Regex bersinar untuk teks DATAR yang berpola tetap: baris log, nomor invoice, kode pos,",
                    "timestamp, validasi format. Begitu datanya bersarang atau berstruktur, ia bahasa yang salah.",
                ],
                "code": """import re

# Jebakan 1: backslash diproses Python DULU. Tanpa huruf r, "\\b" sudah berubah
# jadi satu karakter backspace sebelum mesin regex sempat melihatnya.
print(len("\\b"), ascii("\\b"))     # 1 '\\x08'  -> bukan lagi pola "batas kata"
print(len(r"\\b"), ascii(r"\\b"))   # 2 '\\\\b'   -> inilah yang dibaca mesin regex
print(re.findall(r"\\b\\w+\\b", "kata dua tiga"))   # ['kata', 'dua', 'tiga']

# Jebakan 2: findall berubah perilaku begitu polanya punya grup tangkap
print(re.findall(r"\\d+-\\d+", "10-20 dan 30-40"))          # ['10-20', '30-40']
print(re.findall(r"(\\d+)-(\\d+)", "10-20 dan 30-40"))      # [('10', '20'), ('30', '40')]
print(re.findall(r"(?:\\d+)-(?:\\d+)", "10-20 dan 30-40"))  # ['10-20', '30-40']

# Jebakan 3: kuantifier itu SERAKAH; tambahkan ? untuk versi malas
print(re.search(r"<.+>", "<b>tebal</b>").group(0))    # <b>tebal</b>
print(re.search(r"<.+?>", "<b>tebal</b>").group(0))   # <b>

# Jebakan 4: match hanya menambatkan ke AWAL, bukan berarti "seluruhnya cocok"
print(bool(re.match(r"\\d+", "123abc")))       # True
print(bool(re.fullmatch(r"\\d+", "123abc")))   # False

# Jebakan 5: hasilnya bisa None. Jangan langsung memanggil .group() di situ.
cocok = re.search(r"\\d+", "tanpa angka")
print(cocok.group(0) if cocok else "(tidak ketemu)")""",
            },
        ],
    },
    {
        "title": "36. Iterator & Generator",
        "sections": [
            {
                "body": [
                    "Iterable = objek yang bisa di-for-loop (list, str, dict, dsb).",
                    "Iterator = objek yang 'mengingat' posisinya, punya method",
                    "__next__() untuk mengambil elemen SATU per SATU.",
                    "",
                    "  angka = [1, 2, 3]",
                    "  it = iter(angka)       # ubah iterable jadi iterator",
                    "  print(next(it))        # 1",
                    "  print(next(it))        # 2",
                    "  print(next(it))        # 3",
                    "  print(next(it))        # StopIteration error (habis)",
                    "",
                    "for-loop di Python SEBENARNYA memakai iter() dan next()",
                    "di baliknya secara otomatis sampai StopIteration muncul.",
                ]
            },
            {
                "heading": "Generator function: cara mudah membuat iterator",
                "code": """def hitung_mundur(n):
    while n > 0:
        yield n      # 'yield' membekukan fungsi, mengembalikan nilai
        n -= 1
    print("Selesai!")

for angka in hitung_mundur(5):
    print(angka, end=" ")
# 5 4 3 2 1 Selesai!

# Generator HANYA hasilkan nilai saat DIMINTA (lazy evaluation),
# hemat memori dibanding membuat seluruh list sekaligus.
def genap_tak_terbatas():
    n = 0
    while True:              # bisa 'tak terbatas' karena lazy!
        yield n
        n += 2

gen = genap_tak_terbatas()
print(next(gen))   # 0
print(next(gen))   # 2
print(next(gen))   # 4"""
            },
            {
                "body": [
                    "Kapan generator sangat berguna:",
                    "  1. Memproses file/data SANGAT BESAR baris per baris",
                    "     tanpa memuat semuanya ke memori sekaligus.",
                    "  2. Membuat 'stream' data tak terbatas (seperti contoh di atas).",
                    "  3. Pipeline pemrosesan data bertahap (mirip konsep Stream di Java).",
                    "",
                    "Generator expression (versi ringkas, mirip list comprehension):",
                    "  kuadrat_gen = (x**2 for x in range(10))",
                    "  print(sum(kuadrat_gen))    # dihitung tanpa buat list utuh dulu",
                    "",
                    "Perbedaan return vs yield:",
                    "  return  -> mengembalikan nilai SEKALI, fungsi selesai total.",
                    "  yield   -> mengembalikan nilai, fungsi 'dibekukan', bisa",
                    "             dilanjutkan lagi dari titik yield terakhir.",
                ]
            },
        ],
    },
    {
        "title": "37. itertools & yield from",
        "sections": [
            {
                "body": [
                    "itertools = kotak perkakas iterator yang sudah ikut terpasang",
                    "bersama Python. Isinya fungsi untuk MENYAMBUNG, MEMOTONG,",
                    "MENGULANG, dan MEMASANGKAN iterable tanpa membuat list perantara.",
                    "Tidak perlu pip install apa pun; cukup di-import.",
                    "",
                    "Satu hal membingungkan hampir semua orang di percobaan pertama:",
                    "",
                    "  from itertools import chain",
                    "  print(chain([1, 2], [3]))",
                    "  # <itertools.chain object at 0x7f3a...>",
                    "",
                    "Itu BUKAN error, dan datanya tidak hilang. Hampir semua fungsi",
                    "itertools mengembalikan ITERATOR - sifat lazy yang sudah dibahas",
                    "di materi Iterator & Generator. Isinya belum dihitung sampai ada",
                    "yang meminta. Untuk MELIHAT isinya, bungkus list() (atau tuple(),",
                    "atau langsung pakai di for-loop):",
                    "",
                    "  print(list(chain([1, 2], [3])))   # [1, 2, 3]",
                    "",
                    "Akibat lanjutannya lebih menjebak: iterator itu SEKALI PAKAI.",
                    "Setelah dibaca sampai habis, pembacaan kedua mengembalikan yang",
                    "kosong - tanpa error sama sekali. Gejalanya baru muncul jauh",
                    "kemudian, sebagai 'datanya tiba-tiba kosong' di baris yang lain.",
                    "Kalau memang perlu dipakai dua kali, simpan hasilnya ke list.",
                ],
            },
            {
                "heading": "Menyambung & memotong: chain, islice, count, cycle, repeat",
                "body": [
                    "  chain(a, b, c)          sambung beberapa iterable jadi satu",
                    "  chain.from_iterable(x)  sama, tapi iterable-nya dalam 1 wadah",
                    "  islice(it, ...)         'slice' untuk iterator - TANPA indeks",
                    "                          negatif, karena iterator tidak tahu",
                    "                          di mana ujungnya",
                    "  count(mulai, langkah)   angka menaik TANPA HENTI",
                    "  cycle(iterable)         isinya diputar berulang TANPA HENTI",
                    "  repeat(nilai, n)        nilai sama n kali (tanpa n: tak henti)",
                    "",
                    "Tiga yang terakhir tidak pernah berhenti sendiri. list(count(1))",
                    "akan menggantung dan memakan seluruh RAM - batasi dengan islice()",
                    "atau dengan break.",
                ],
                "code": """from itertools import chain, islice, count, cycle, repeat

a = [1, 2, 3]
b = (4, 5)
c = "xy"

gabung = chain(a, b, c)
print(gabung)                 # <itertools.chain object at 0x...>
print(list(gabung))           # [1, 2, 3, 4, 5, 'x', 'y']
print(list(gabung))           # [] -> sekali pakai, sudah habis

# chain.from_iterable: SATU argumen yang isinya banyak iterable
matriks = [[1, 2], [3, 4], [5]]
print(list(chain.from_iterable(matriks)))   # [1, 2, 3, 4, 5]

# islice: potong iterator seperti slice (tanpa indeks negatif)
print(list(islice(range(10), 3)))           # [0, 1, 2]
print(list(islice(range(10), 2, 7, 2)))     # [2, 4, 6]

# count, cycle, repeat: TAK TERBATAS kalau tidak dibatasi
print(list(islice(count(10, 5), 4)))        # [10, 15, 20, 25]
print(list(islice(cycle("AB"), 5)))         # ['A', 'B', 'A', 'B', 'A']
print(list(repeat("hai", 3)))               # ['hai', 'hai', 'hai']""",
            },
            {
                "heading": "product, combinations, permutations",
                "body": [
                    "product() adalah loop bersarang yang ditulis mendatar. Dua loop",
                    "bersarang jadi satu baris; sepuluh loop bersarang pun tetap satu",
                    "baris. Itu sebabnya ia sering muncul di kode nyata - bukan karena",
                    "lebih cepat, tapi karena menjoroknya tidak ikut bertambah dalam.",
                    "",
                    "  product(a, b)         semua pasangan a x b (yang paling kanan",
                    "                        berputar paling cepat)",
                    "  product(a, repeat=n)  a dipasangkan dengan DIRINYA SENDIRI",
                    "  combinations(x, n)    pilih n, urutan TIDAK dihitung: AB = BA",
                    "  permutations(x, n)    susun n, urutan DIHITUNG: AB != BA",
                    "",
                    "Jebakan hitungannya: product([0, 1], repeat=20) berisi lebih dari",
                    "sejuta tuple. Selama masih berupa iterator itu aman; begitu",
                    "di-list(), semuanya jadi nyata di RAM sekaligus.",
                ],
                "code": """from itertools import product, combinations, permutations

ukuran = ["S", "M"]
warna = ["merah", "biru"]

for u in ukuran:            # cara lama: dua loop bersarang
    for w in warna:
        print(u, w, end="  ")
print()

for u, w in product(ukuran, warna):   # hasilnya PERSIS sama
    print(u, w, end="  ")
print()

# repeat=n = "iterable ini dipakai n kali", bukan "diulang n kali"
print(list(product([0, 1], repeat=2)))
# [(0, 0), (0, 1), (1, 0), (1, 1)]

# combinations: urutan TIDAK penting, satu anggota tak dipakai 2x
print(list(combinations("ABC", 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# permutations: urutan PENTING, ('A','B') dan ('B','A') dua-duanya masuk
print(list(permutations("ABC", 2)))
print(len(list(permutations("ABC"))))    # 6 = 3!""",
            },
            {
                "heading": "groupby: datanya WAJIB diurutkan lebih dulu",
                "body": [
                    "groupby() mengelompokkan elemen BERURUTAN yang key-nya sama.",
                    "Kata kuncinya berurutan: ia tidak mengurutkan apa pun, ia cuma",
                    "memotong setiap kali nilai key BERUBAH dari elemen sebelumnya.",
                    "",
                    "Akibatnya data yang belum diurutkan menghasilkan grup PECAH -",
                    "kategori yang sama muncul dua-tiga kali. Tidak ada error, tidak",
                    "ada peringatan, cuma hasil yang salah. Aturannya: sort() dulu",
                    "dengan key yang PERSIS SAMA dengan key groupby.",
                    "",
                    "Jebakan kedua: iterator anggota tiap grup hangus begitu kita maju",
                    "ke grup berikutnya. Jadi list(groupby(...)) memberi daftar grup",
                    "yang isinya kosong semua. Olah anggotanya di dalam loop, atau",
                    "salin dengan list() saat itu juga.",
                ],
                "code": """from itertools import groupby

data = [
    ("buah", "apel"),
    ("sayur", "bayam"),
    ("buah", "jeruk"),
    ("sayur", "kangkung"),
]

def kategori(pasangan):
    return pasangan[0]

print("Tanpa diurutkan lebih dulu:")
for kunci, anggota in groupby(data, key=kategori):
    print("  ", kunci, [nama for _, nama in anggota])
# "buah" muncul DUA KALI: grupnya pecah karena datanya berselang

data.sort(key=kategori)          # WAJIB: key sortir = key groupby
print("Setelah diurutkan:")
for kunci, anggota in groupby(data, key=kategori):
    print("  ", kunci, [nama for _, nama in anggota])

# Anggota grup hangus kalau baru dibaca setelah loopnya jalan terus:
grup = list(groupby(data, key=kategori))
print([(kunci, list(anggota)) for kunci, anggota in grup])
# [('buah', []), ('sayur', [])]  <- bukan bug; memang begitu""",
            },
            {
                "heading": "yield from: menyerahkan giliran ke generator lain",
                "body": [
                    "yield from artinya 'sambungkan generator itu langsung ke",
                    "pemanggilku'. Salah baca yang paling sering: mengira",
                    "'yield generator_lain()' sama saja. Tidak - tanpa kata from,",
                    "yang keluar OBJEK generatornya, dan hasilnya",
                    "[<generator object ... at 0x...>] alih-alih isinya. Bedanya satu",
                    "kata, tapi kesimpulan soal apa yang keluar jadi terbalik.",
                    "",
                    "Dua hal yang dibawanya selain memendekkan for-loop:",
                    "  - generator REKURSIF jadi enak ditulis. Lihat ratakan() di",
                    "    bawah: pola baku menelusuri list/pohon bersarang tanpa",
                    "    pernah membangun list besar di memori.",
                    "  - nilai return generator anak ikut TERTANGKAP.",
                    "",
                    "return di dalam generator TIDAK mengirim nilai ke for-loop.",
                    "Artinya cuma 'generator ini selesai', dan nilainya diselipkan ke",
                    "StopIteration.value. Karena itu 'jumlah = yield from hitung(...)'",
                    "adalah cara wajar membacanya; for-loop biasa tidak akan pernah",
                    "melihat angka itu.",
                    "",
                    "Sekilas .send(): yield juga bisa berdiri sebagai EKSPRESI yang",
                    "MENERIMA data, bukan mengirim.",
                    "",
                    "  def penampung():",
                    "      while True:",
                    "          pesan = yield        # nilai MASUK dari luar",
                    "          print(\"dapat:\", pesan)",
                    "",
                    "  p = penampung()",
                    "  next(p)                      # wajib: maju ke yield pertama",
                    "  p.send(\"halo\")               # dapat: halo",
                    "",
                    "Inilah pintu masuk pertama Python ke coroutine, jauh sebelum",
                    "async/await ada. Sekarang jarang ditulis orang; cukup kenali",
                    "bentuknya kalau bertemu di kode lama.",
                ],
                "code": """def angka():
    yield 1
    yield 2

def semua():
    yield from angka()        # serahkan penuh ke generator lain
    yield "selesai"

print(list(semua()))          # [1, 2, 'selesai']

def keliru():
    yield angka()             # tanpa 'from': yang keluar OBJEK-nya
print(list(keliru()))         # [<generator object angka at 0x...>]

def ratakan(data):            # generator rekursif, list bersarang
    for item in data:
        if isinstance(item, list):
            yield from ratakan(item)
        else:
            yield item

print(list(ratakan([1, [2, [3, 4], 5], [[6]], 7])))
# [1, 2, 3, 4, 5, 6, 7]

def hitung(data):
    total = 0
    for n in data:
        total += n
        yield n
    return total              # BUKAN di-yield; ini nilai balik

def pemakai():
    jumlah = yield from hitung([1, 2, 3])   # menangkap return-nya
    print("total:", jumlah)

print(list(pemakai()))        # total: 6  lalu  [1, 2, 3]""",
            },
        ],
    },
    {
        "title": "38. Decorator & Context Manager",
        "sections": [
            {
                "body": [
                    "Decorator = fungsi yang 'membungkus' fungsi lain untuk",
                    "menambah perilaku TANPA mengubah kode fungsi aslinya.",
                    "Ditandai dengan simbol @ di atas definisi fungsi.",
                    "",
                    "Konsep dasar: fungsi di Python adalah 'first-class object'",
                    "(bisa disimpan ke variabel, dikirim sebagai argumen, dsb).",
                ]
            },
            {
                "heading": "Membuat decorator sendiri",
                "code": """import time

def ukur_waktu(fungsi):
    def wrapper(*args, **kwargs):
        mulai = time.time()
        hasil = fungsi(*args, **kwargs)
        selesai = time.time()
        print(f"{fungsi.__name__} selesai dalam {selesai - mulai:.4f} detik")
        return hasil
    return wrapper

@ukur_waktu
def proses_data(n):
    total = sum(range(n))
    return total

hasil = proses_data(1000000)
print(hasil)
# proses_data selesai dalam 0.0123 detik
# 499999500000

# @ukur_waktu setara dengan:
# proses_data = ukur_waktu(proses_data)"""
            },
            {
                "body": [
                    "Decorator bawaan Python yang sering dipakai:",
                    "  @staticmethod / @classmethod  -> di dalam class (materi OOP)",
                    "  @property                      -> getter/setter (materi encapsulation)",
                    "  @functools.lru_cache            -> cache hasil fungsi otomatis",
                    "",
                    "  from functools import lru_cache",
                    "  @lru_cache(maxsize=None)",
                    "  def fibonacci(n):",
                    "      if n < 2: return n",
                    "      return fibonacci(n-1) + fibonacci(n-2)",
                    "  # tanpa cache, ini SANGAT lambat untuk n besar;",
                    "  # dengan cache, hasil yang sudah dihitung disimpan otomatis.",
                ]
            },
            {
                "heading": "Context manager: membuat 'with' sendiri",
                "code": """class BukaFile:
    def __init__(self, nama_file, mode):
        self.nama_file = nama_file
        self.mode = mode

    def __enter__(self):               # dijalankan saat masuk blok 'with'
        self.file = open(self.nama_file, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # saat keluar blok
        self.file.close()
        print("File otomatis ditutup.")

with BukaFile("test.txt", "w") as f:
    f.write("Halo!")
# File otomatis ditutup.

# Cara lebih ringkas dengan @contextmanager
from contextlib import contextmanager

@contextmanager
def bukafile(nama, mode):
    f = open(nama, mode)
    try:
        yield f
    finally:
        f.close()
        print("Ditutup lewat contextmanager.")"""
            },
        ],
    },
    {
        "title": "39. Introspeksi Objek & Decorator Lanjutan",
        "sections": [
            {
                "body": [
                    "Materi Decorator baru saja memakai fungsi.__name__, dan Latihan 16 mewajibkannya,",
                    "tanpa sekali pun menjelaskan dari mana nilai itu datang. Padahal satu-satunya",
                    "__name__ yang pernah kamu lihat sebelumnya ada di if __name__ == \"__main__\", dan",
                    "di sana isinya \"__main__\". Keduanya benar, dan keduanya BARANG YANG BERBEDA:",
                    "",
                    "  __name__ polos di tingkat modul  -> nama MODUL yang sedang berjalan",
                    "  fungsi.__name__                  -> nama FUNGSI itu, mis. \"proses_data\"",
                    "",
                    "Yang menyatukan keduanya: di Python semua hal adalah OBJEK, dan objek punya",
                    "atribut. Angka, string, list, class, modul, bahkan fungsi. Sebuah fungsi bukan",
                    "'kode yang ditempel ke sebuah nama' - ia benda yang bisa disimpan ke variabel,",
                    "dioper sebagai argumen (itu sudah kamu pakai di materi Lambda), dan yang belum",
                    "pernah disebut: DIINTIP isinya.",
                    "",
                    "Atribut yang dimiliki setiap fungsi, tanpa kamu menuliskannya:",
                    "  fungsi.__name__      nama saat ia didefinisikan, berupa str",
                    "  fungsi.__doc__       docstring-nya, atau None kalau tidak ditulis",
                    "  fungsi.__module__    nama modul tempat ia ditulis",
                    "  fungsi.__qualname__  nama lengkap termasuk class pembungkusnya",
                    "  fungsi.__dict__      kotak kosong, tempat siapa pun boleh menempel atribut baru",
                    "",
                    "Membaca isi sebuah objek saat program BERJALAN namanya introspeksi. Ini bukan",
                    "trik pinggiran: Django membaca field model-mu begini, Flask mendaftar rute dari",
                    "__name__ fungsimu, pytest menemukan test dari nama yang berawalan test_, dan ORM",
                    "mengubah objek jadi baris tabel dengan membaca atributnya satu per satu. Tanpa",
                    "bab ini, semua pustaka itu akan terus terasa seperti sihir yang tidak bisa kamu",
                    "tiru sendiri.",
                ],
            },
            {
                "heading": "Mengintip objek yang isinya belum kamu ketahui",
                "code": "def sapa(nama):\n    \"\"\"Menyapa seseorang dengan ramah.\"\"\"\n    return f\"Halo, {nama}!\"\n\n# Fungsi itu OBJEK. Buktinya: ia punya atribut yang bisa dibaca seperti objek lain.\nprint(sapa.__name__)       # sapa\nprint(sapa.__doc__)        # Menyapa seseorang dengan ramah.\nprint(sapa.__module__)     # __main__   <- nama MODUL, beda barang dengan __name__ di atas\nprint(sapa.__dict__)       # {}         <- kotak atribut tambahan, awalnya kosong\n\n# Kotak itu boleh diisi siapa saja. Begitulah framework menempel catatan ke fungsimu.\nsapa.rute = \"/sapa\"\nprint(sapa.__dict__)       # {'rute': '/sapa'}\nprint(sapa.rute)           # /sapa\n\n\nclass Kucing:\n    def __init__(self, nama, umur):\n        self.nama = nama\n        self.umur = umur\n\n    def bersuara(self):\n        return \"Meong\"\n\n\nprint(Kucing.bersuara.__qualname__)   # Kucing.bersuara  -- __name__ cuma 'bersuara'\n\nc = Kucing(\"Oyen\", 3)\nprint(type(c))                # <class '__main__.Kucing'>\nprint(c.__class__.__name__)   # Kucing  -- nama class-nya SAJA, tanpa bungkus <class ...>\n\n# vars(obj) = isi __dict__ objek itu: hanya atribut yang benar-benar dipasang padanya.\nprint(vars(c))                # {'nama': 'Oyen', 'umur': 3}\nprint(c.__dict__)             # sama persis; vars() memang membaca __dict__\n\n# dir(obj) = SEMUA nama yang bisa diakses dari objek, termasuk warisan dan dunder.\nprint(len(dir(c)) > 20)                                # True, daftarnya panjang sekali\nprint([n for n in dir(c) if not n.startswith(\"__\")])   # ['bersuara', 'nama', 'umur']\n\n# Pakai yang mana: vars() untuk \"apa isi objek ini\", dir() untuk \"apa yang bisa\n# kulakukan padanya\". Keduanya alat pertama saat kamu memegang objek asing di REPL.",
            },
            {
                "heading": "getattr, setattr, hasattr: atribut lewat nama berupa string",
                "body": [
                    "Sampai sekarang setiap atribut yang kamu baca namanya DITULIS di kode: p.harga.",
                    "Itu cukup selama kamu sendiri yang tahu isinya waktu mengetik. Sebuah framework",
                    "tidak pernah tahu - Django ditulis bertahun-tahun sebelum class-mu ada. Yang ia",
                    "punya cuma nama berupa STRING, dan trio inilah jembatannya:",
                    "",
                    "  getattr(obj, \"harga\")        sama dengan obj.harga",
                    "  getattr(obj, \"harga\", 0)     ... tapi kembalikan 0 kalau atributnya tidak ada",
                    "  setattr(obj, \"harga\", 500)   sama dengan obj.harga = 500",
                    "  hasattr(obj, \"harga\")        True/False, tanpa melempar error",
                    "  delattr(obj, \"harga\")        sama dengan del obj.harga",
                    "",
                    "Bedanya cuma satu, dan itu segalanya: nama atributnya kini DATA. Ia boleh datang",
                    "dari daftar kolom, dari berkas konfigurasi, atau dari input pengguna.",
                ],
                "code": """class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def total_nilai(self):
        return self.harga * self.stok


p = Produk("Kopi", 25000, 4)

print(p.harga)                   # 25000  -- nama atribut ditulis langsung di kode
kolom = "harga"
print(getattr(p, kolom))         # 25000  -- nama atribut berupa string, boleh dari mana saja

# Argumen ketiga = nilai cadangan. TANPA itu, atribut yang tidak ada -> AttributeError.
print(getattr(p, "diskon", 0))   # 0
print(hasattr(p, "diskon"))      # False

# Beginilah sebuah "framework" mencetak objek apa pun tanpa pernah tahu isinya:
def ke_baris(objek, kolom):
    return " | ".join(str(getattr(objek, k, "-")) for k in kolom)

print(ke_baris(p, ["nama", "harga", "stok", "diskon"]))
# Kopi | 25000 | 4 | -

# setattr menulis balik. Beginilah data mentah dari form web dituang ke objek.
for kunci, nilai in {"harga": 30000, "stok": 10}.items():
    setattr(p, kunci, nilai)
print(vars(p))                   # {'nama': 'Kopi', 'harga': 30000, 'stok': 10}

# JEBAKAN 1: setattr menerima nama APA PUN. Salah ketik tidak menimbulkan error,
# ia diam-diam membuat atribut BARU yang tidak pernah dibaca siapa pun.
setattr(p, "stokk", 99)
print(p.stok, p.stokk)           # 10 99  -- dua atribut berbeda, tanpa satu pun peringatan

# Method juga atribut. getattr MENGAMBIL methodnya; tanda kurung () yang memanggilnya.
perintah = "total_nilai"         # bayangkan ini datang dari input pengguna
aksi = getattr(p, perintah)      # sudah diambil, BELUM dipanggil
print(callable(aksi))            # True
print(aksi())                    # 300000

# JEBAKAN 2: lupa () membuatmu mencetak <bound method ...> alih-alih hasilnya.
# Periksa dulu daripada meledak di tengah jalan:
for perintah in ["total_nilai", "diskon_akhir"]:
    if hasattr(p, perintah):
        print(perintah, "->", getattr(p, perintah)())
    else:
        print(perintah, "-> tidak dikenal")""",
            },
            {
                "heading": "functools.wraps: kenapa wrapper polos merusak fungsi yang dibungkusnya",
                "code": "def catat(fungsi):\n    def wrapper(*args, **kwargs):\n        print(f\"-> memanggil {fungsi.__name__}\")\n        return fungsi(*args, **kwargs)\n    return wrapper\n\n\n@catat\ndef tambah(a, b):\n    \"\"\"Menjumlahkan dua angka.\"\"\"\n    return a + b\n\n\nprint(tambah(2, 3))\n# -> memanggil tambah\n# 5\n\n# Sejauh ini terlihat baik-baik saja. Sekarang tanya IDENTITAS fungsinya:\nprint(tambah.__name__)      # wrapper   <- BUKAN 'tambah'\nprint(tambah.__doc__)       # None      <- docstring aslinya lenyap\n\n# Sebabnya: @catat menugaskan ulang nama 'tambah' ke objek wrapper. Fungsi aslinya\n# masih hidup di dalam closure, tapi yang dilihat dunia luar adalah wrapper -\n# dan wrapper memang bernama 'wrapper'.\n\nimport functools\n\n\ndef catat_rapi(fungsi):\n    @functools.wraps(fungsi)         # salin __name__, __doc__, __module__, __dict__\n    def wrapper(*args, **kwargs):\n        print(f\"-> memanggil {fungsi.__name__}\")\n        return fungsi(*args, **kwargs)\n    return wrapper\n\n\n@catat_rapi\ndef kurang(a, b):\n    \"\"\"Mengurangi dua angka.\"\"\"\n    return a - b\n\n\nprint(kurang(9, 4))         # -> memanggil kurang   lalu   5\nprint(kurang.__name__)      # kurang\nprint(kurang.__doc__)       # Mengurangi dua angka.\n\nasli = kurang.__wrapped__   # wraps menyimpan fungsi aslinya di sini\nprint(asli(9, 4))           # 5  -- dipanggil langsung, jadi tidak mencetak '->'\n\n# Kenapa ini bukan sekadar kerapian:\n#   - help(tambah) dan dokumentasi otomatis menampilkan wrapper, bukan fungsi aslimu.\n#   - Flask mendaftar rute memakai __name__. Dua fungsi yang sama-sama jadi 'wrapper'\n#     dianggap bertabrakan, dan aplikasinya menolak jalan.\n#   - Laporan pytest dan pesan log jadi berisi 'wrapper' berulang-ulang, tak terbaca.\n# Aturannya: SETIAP decorator yang kamu tulis diawali @functools.wraps(fungsi).\n# Termasuk ukur_waktu di materi sebelumnya dan log_panggilan di Latihan 16 -\n# keduanya memang kurang baris ini.",
            },
            {
                "heading": "Decorator berargumen dan urutan saat ditumpuk",
                "body": [
                    "Kenapa @lru_cache(maxsize=None) memakai kurung sedangkan @ukur_waktu tidak?",
                    "Karena apa pun yang ditulis di belakang @ DIEVALUASI lebih dulu, dan hasilnya",
                    "harus berupa sesuatu yang siap menerima fungsimu:",
                    "",
                    "  @ukur_waktu               ukur_waktu sudah berupa decorator -> ukur_waktu(fungsi)",
                    "  @lru_cache(maxsize=None)  lru_cache(maxsize=None) DIPANGGIL dulu; nilai",
                    "                            kembaliannya yang jadi decorator, baru menerima fungsi",
                    "",
                    "Yang kedua butuh TIGA lapis fungsi bersarang - pabrik, decorator, wrapper. Lapis",
                    "terluar hanya ada untuk menyimpan argumennya, dan yang menyimpannya adalah closure",
                    "(materi Scope, Closure & nonlocal). Bentuk tiga lapis inilah yang kamu temui di",
                    "hampir semua decorator dunia nyata: @app.route(\"/produk\") di Flask,",
                    "@pytest.mark.parametrize(...) di pytest, @retry(kali=3) di pustaka ketahanan.",
                    "",
                    "JEBAKAN: lupa kurungnya. @ulangi tanpa (kali=3) membuat fungsimu dikirim sebagai",
                    "argumen kali, dan yang terpasang ke namamu adalah objek 'decorator' - errornya",
                    "baru meledak jauh kemudian, dengan pesan yang tidak menyebut decorator sama sekali.",
                    "",
                    "Menumpuk decorator: yang paling DEKAT dengan def diterapkan lebih dulu (dari bawah",
                    "ke atas), tapi saat fungsinya dipanggil, pembungkus paling ATAS yang jalan duluan.",
                ],
                "code": """import functools


def ulangi(kali):                      # LAPIS 1 - pabrik: menerima ARGUMEN decorator
    def decorator(fungsi):             # LAPIS 2 - decorator asli: menerima FUNGSI
        @functools.wraps(fungsi)
        def wrapper(*args, **kwargs):  # LAPIS 3 - pengganti: menerima argumen pemanggilan
            hasil = None
            for _ in range(kali):
                hasil = fungsi(*args, **kwargs)
            return hasil
        return wrapper
    return decorator


@ulangi(kali=3)
def sapa(nama):
    print(f"Halo, {nama}!")


sapa("Levi")
# Halo, Levi!
# Halo, Levi!
# Halo, Levi!

# @ulangi(kali=3)  setara dengan:  sapa = ulangi(kali=3)(sapa)
# Kurungnya dievaluasi DULU -> menghasilkan decorator -> barulah ia menerima sapa.

# ---- Menumpuk decorator: urutan penerapan vs urutan eksekusi ----

def luar(fungsi):
    @functools.wraps(fungsi)
    def wrapper(*a, **kw):
        print("luar : masuk")
        hasil = fungsi(*a, **kw)
        print("luar : keluar")
        return hasil
    return wrapper


def dalam(fungsi):
    @functools.wraps(fungsi)
    def wrapper(*a, **kw):
        print("dalam: masuk")
        hasil = fungsi(*a, **kw)
        print("dalam: keluar")
        return hasil
    return wrapper


@luar
@dalam
def kerja():
    print("kerja: jalan")


kerja()
# luar : masuk      DITERAPKAN dari bawah ke atas:  kerja = luar(dalam(kerja))
# dalam: masuk      DIJALANKAN dari atas ke bawah:  pembungkus terluar duluan
# kerja: jalan
# dalam: keluar
# luar : keluar
print(kerja.__name__)   # kerja  -- tetap utuh karena kedua wrapper memakai @wraps""",
            },
        ],
    },
    {
        "title": "40. Konkurensi: Thread, Proses & GIL",
        "sections": [
            {
                "body": [
                    "Sampai sini semua program kita mengerjakan satu hal pada satu waktu: baris demi",
                    "baris, dari atas ke bawah. KONKURENSI adalah cara menyusun program supaya banyak",
                    "pekerjaan bisa maju bergantian tanpa saling menunggu sampai tuntas.",
                    "",
                    "Dua kata yang sering tertukar:",
                    "  concurrency (kebersamaan)  -> banyak tugas SEDANG berjalan, bergantian memakai",
                    "                                satu inti CPU. Satu koki menggoreng sambil",
                    "                                menunggu air di panci lain mendidih.",
                    "  parallelism (kesejajaran)  -> banyak tugas berjalan BENAR-BENAR serentak di",
                    "                                beberapa inti CPU. Empat koki, empat kompor.",
                    "",
                    "Yang menentukan mana yang kamu butuhkan bukan selera, tapi JENIS PEKERJAANNYA:",
                    "  I/O-bound  -> waktunya habis MENUNGGU. Unduh halaman, baca berkas besar, query",
                    "                database, panggil API. Selama menunggu, CPU-nya menganggur.",
                    "  CPU-bound  -> waktunya habis MENGHITUNG. Kompresi gambar, enkripsi, olah angka,",
                    "                parsing berkas raksasa. CPU-nya penuh dari awal sampai akhir.",
                    "",
                    "GIL (Global Interpreter Lock)",
                    "CPython - interpreter yang dipasang orang dari python.org - memakai satu kunci",
                    "besar: hanya SATU thread yang boleh menjalankan bytecode Python pada satu waktu.",
                    "Ini bukan kelalaian, tapi pilihan desain; manajemen memorinya jadi jauh lebih",
                    "sederhana dan kode satu-thread jadi cepat. Konsekuensinya mengikat:",
                    "",
                    "  - Menambah thread TIDAK mempercepat pekerjaan CPU-bound. Empat thread yang",
                    "    sama-sama menghitung tetap bergantian di satu inti; totalnya segitu juga.",
                    "  - Menambah thread SANGAT mempercepat pekerjaan I/O-bound, karena GIL DILEPAS",
                    "    selama sebuah thread menunggu jaringan, disk, atau time.sleep().",
                    "  - GIL tidak menyelamatkanmu dari race condition. Yang dilindunginya adalah",
                    "    interpreter, bukan data milikmu.",
                    "",
                    "Kalau yang kamu butuhkan CPU berjalan sejajar sungguhan, jalankan beberapa PROSES.",
                    "Tiap proses punya interpreter, memori, dan GIL sendiri-sendiri.",
                ],
            },
            {
                "heading": "Thread mentah: threading.Thread, join, dan Lock",
                "code": """import threading
import time

def unduh(nama, detik):
    print(f"[{nama}] mulai")
    time.sleep(detik)          # pura-pura menunggu jaringan; GIL dilepas di sini
    print(f"[{nama}] selesai")

mulai = time.perf_counter()

t1 = threading.Thread(target=unduh, args=("A", 1))
t2 = threading.Thread(target=unduh, args=("B", 1))
t1.start()                     # start() menjalankan, TIDAK menunggu
t2.start()
t1.join()                      # join() barulah menunggu sampai thread itu habis
t2.join()

print(f"Dua tugas 1 detik selesai dalam {time.perf_counter() - mulai:.1f} detik")

# ---- Data bersama tanpa penjagaan = RACE CONDITION
stok = {"beras": 0}

def tambah_tanpa_lock(kali):
    for _ in range(kali):
        stok["beras"] = stok.get("beras", 0) + 1   # baca -> tambah -> tulis

utas = [threading.Thread(target=tambah_tanpa_lock, args=(200000,)) for _ in range(4)]
for u in utas:
    u.start()
for u in utas:
    u.join()
print("tanpa Lock :", stok["beras"], "<- seharusnya 800000")

# Baris "baca -> tambah -> tulis" itu TIGA langkah. Thread lain bisa menyelip di
# tengahnya, membaca angka yang sama, lalu menimpa hasil temannya. Angka di atas
# berubah-ubah tiap kali program dijalankan - dan justru itu buktinya.

# ---- Dengan Lock: hanya satu thread yang boleh masuk
stok["beras"] = 0
kunci = threading.Lock()

def tambah_dengan_lock(kali):
    for _ in range(kali):
        with kunci:                                # kunci dilepas otomatis
            stok["beras"] = stok.get("beras", 0) + 1

utas = [threading.Thread(target=tambah_dengan_lock, args=(200000,)) for _ in range(4)]
for u in utas:
    u.start()
for u in utas:
    u.join()
print("dengan Lock:", stok["beras"], "<- selalu 800000")""",
            },
            {
                "heading": "Kolam thread siap pakai: ThreadPoolExecutor",
                "code": """import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def ambil_halaman(nama, detik):
    time.sleep(detik)          # menunggu jaringan
    return f"{nama} siap"

halaman = [("beranda", 0.4), ("produk", 0.3), ("kontak", 0.2), ("promo", 0.1)]

mulai = time.perf_counter()
for nama, detik in halaman:
    ambil_halaman(nama, detik)
print(f"berurutan : {time.perf_counter() - mulai:.1f} detik")

# Blok 'with' menunggu SEMUA pekerjaan selesai sebelum keluar - sama seperti
# 'with' pada berkas, ia yang membereskan (materi Decorator & Context Manager).
mulai = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as ex:
    # map() -> hasil datang SESUAI URUTAN masukan, walau selesainya tidak urut
    hasil = list(ex.map(lambda h: ambil_halaman(*h), halaman))
print(f"4 thread  : {time.perf_counter() - mulai:.1f} detik")
print("map  ->", hasil)

# submit() + as_completed() -> tangani begitu ada yang selesai, tidak menunggu urutan
with ThreadPoolExecutor(max_workers=4) as ex:
    tugas = {ex.submit(ambil_halaman, nama, detik): nama for nama, detik in halaman}
    for masa_depan in as_completed(tugas):
        print("selesai ->", masa_depan.result(), "| dari:", tugas[masa_depan])

# submit() mengembalikan Future: sebuah "janji hasil" yang belum tentu sudah jadi.
# Error di dalam worker DIAM saja sampai .result() dipanggil.
def pasti_gagal():
    return 1 / 0

with ThreadPoolExecutor() as ex:
    f = ex.submit(pasti_gagal)
    print("sudah submit, program masih tenang")
    try:
        f.result()             # error baru meledak persis di baris ini
    except ZeroDivisionError as e:
        print("tertangkap di result():", e)""",
            },
            {
                "heading": "Untuk pekerjaan menghitung: ProcessPoolExecutor",
                "body": [
                    "ProcessPoolExecutor punya API yang sama persis dengan ThreadPoolExecutor -",
                    "submit, map, as_completed - tapi pekerjanya PROSES sistem operasi, bukan thread.",
                    "Tiap proses punya GIL sendiri, jadi hitungan benar-benar berjalan sejajar.",
                    "",
                    "Harganya dua hal yang tidak ada pada thread:",
                    "  1. Menyalakan proses baru butuh waktu (puluhan sampai ratusan milidetik).",
                    "  2. Argumen dan hasilnya DISALIN lewat pickle, bukan dibagi. Kalau datanya",
                    "     besar, ongkos salin-menyalin bisa mengalahkan hasil percepatannya.",
                ],
                "code": """import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cacah_prima(batas):
    # CPU-bound murni: tidak ada yang ditunggu, semuanya dihitung.
    jumlah = 0
    for n in range(2, batas):
        pembagi = 2
        while pembagi * pembagi <= n:
            if n % pembagi == 0:
                break
            pembagi += 1
        else:
            jumlah += 1
    return jumlah

def ukur(nama, kerjakan):
    mulai = time.perf_counter()
    hasil = kerjakan()
    print(f"{nama:<22}: {time.perf_counter() - mulai:.2f} detik -> {hasil}")

TUGAS = [100000, 100000, 100000, 100000]

if __name__ == "__main__":          # WAJIB kalau memakai proses. Lihat catatan di bawah.
    print("inti CPU tersedia:", multiprocessing.cpu_count())

    ukur("berurutan", lambda: [cacah_prima(b) for b in TUGAS])

    with ThreadPoolExecutor(max_workers=4) as ex:
        ukur("4 thread (kena GIL)", lambda: list(ex.map(cacah_prima, TUGAS)))

    with ProcessPoolExecutor(max_workers=4) as ex:
        ex.submit(abs, 0).result()  # nyalakan dulu prosesnya, supaya yang diukur kerjanya
        ukur("4 proses (sejajar)", lambda: list(ex.map(cacah_prima, TUGAS)))

    # Semua yang dikirim ke proses lain harus bisa di-pickle. lambda tidak bisa.
    try:
        with ProcessPoolExecutor(max_workers=2) as ex:
            list(ex.map(lambda x: x * 2, [1, 2, 3]))
    except Exception as e:
        print("lambda ditolak:", type(e).__name__)

# Contoh keluaran (angkanya beda di tiap mesin, yang penting POLANYA):
#   inti CPU tersedia: 8
#   berurutan             : 1.05 detik -> [9592, 9592, 9592, 9592]
#   4 thread (kena GIL)   : 1.07 detik -> [9592, 9592, 9592, 9592]   <- tidak menolong
#   4 proses (sejajar)    : 0.30 detik -> [9592, 9592, 9592, 9592]   <- inilah bedanya
#   lambda ditolak: PicklingError""",
            },
            {
                "body": [
                    "Cara memilih, dari yang paling murah:",
                    "  1. TIDAK PAKAI APA-APA. Konkurensi menambahkan bug yang cuma muncul sesekali",
                    "     dan sulit diulang. Kalau versi berurutannya sudah cukup cepat, berhenti",
                    "     di situ. Ukur dulu dengan time.perf_counter(), jangan menebak.",
                    "  2. Pekerjaan MENUNGGU (jaringan, berkas, database) -> thread. ThreadPoolExecutor",
                    "     hampir selalu jawabannya; jarang ada alasan membuat Thread satu per satu.",
                    "  3. Pekerjaan MENGHITUNG -> proses. ProcessPoolExecutor dengan jumlah pekerja",
                    "     kira-kira sebanyak inti CPU (multiprocessing.cpu_count()).",
                    "  4. Ribuan koneksi menunggu sekaligus -> async/await di materi berikutnya,",
                    "     karena seribu thread berarti seribu tumpukan memori.",
                    "",
                    "Jebakan yang benar-benar menjebak:",
                    "  - Kode yang benar SEKALI dijalankan bukan bukti kode itu aman. Race condition",
                    "    bisa bersembunyi berbulan-bulan lalu muncul saat servernya sedang sibuk.",
                    "  - Future yang hasilnya tidak pernah diambil = error yang tidak pernah terlihat.",
                    "    ex.map() juga mengembalikan iterator: errornya baru muncul saat diiterasi.",
                    "  - Lupa join() atau tidak memakai blok 'with' pada executor: program induk bisa",
                    "    selesai lebih dulu dan pekerjaannya terpotong di tengah jalan.",
                    "  - Tanpa 'if __name__ == \"__main__\":', proses anak mengimpor ulang berkasmu,",
                    "    membuat pool baru lagi, yang membuat proses lagi - beranak-pinak tanpa henti.",
                    "  - Antar-proses data DISALIN, bukan dibagi. Mengubah variabel global di proses",
                    "    anak sama sekali tidak terlihat di induknya.",
                    "  - lambda, fungsi di dalam fungsi, koneksi, dan objek file tidak bisa di-pickle.",
                    "    Fungsi untuk ProcessPoolExecutor harus fungsi biasa di level atas modul.",
                    "  - Kebanyakan pekerja proses justru memperlambat: tiap proses makan memori",
                    "    sendiri dan mereka berebut inti yang jumlahnya tetap segitu.",
                    "",
                    "Nama-nama lain yang akan kamu temui saat membaca kode orang:",
                    "  threading.Lock / RLock   penjaga data bersama (RLock boleh dikunci berkali-kali",
                    "                           oleh thread yang sama, Lock tidak - itu deadlock)",
                    "  threading.Event          isyarat \"sudah boleh jalan\" antar-thread",
                    "  queue.Queue              antrean yang SUDAH aman dipakai banyak thread",
                    "  multiprocessing.Process  proses tunggal, saudara dari threading.Thread",
                    "  daemon=True              thread yang ikut mati begitu program utama selesai",
                    "",
                    "Catatan versi: Python 3.13 ke atas menyediakan build eksperimental",
                    "\"free-threaded\" yang GIL-nya bisa dimatikan; sys._is_gil_enabled() memberitahu",
                    "statusnya. Python yang biasa dipasang orang masih memakai GIL, jadi seluruh",
                    "aturan di atas tetap berlaku - dan kode yang bebas race condition tetap aman",
                    "di kedua-duanya.",
                ],
            },
        ],
    },
    {
        "title": "41. Asinkron: async, await & asyncio",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menutup dua cara mengerjakan banyak hal sekaligus: thread dan proses.",
                    "asyncio adalah cara KETIGA, dan bentuknya paling asing karena ia menambah KATA KUNCI baru",
                    "ke bahasanya - async dan await - bukan sekadar modul yang di-import.",
                    "",
                    "Masalah yang dipecahkannya sempit tapi sangat umum: program yang kebanyakan MENUNGGU.",
                    "Menunggu jawaban server, menunggu query database, menunggu berkas dibaca dari disk.",
                    "Selama menunggu, CPU tidak mengerjakan apa pun; ia berdiri diam di satu baris kode.",
                    "",
                    "Bayangkan satu pelayan warung yang cekatan. Ia tidak berdiri diam menunggu masakan meja 1",
                    "matang; sambil menunggu, ia mencatat pesanan meja 2 lalu meja 3. Satu orang, tapi nyaris",
                    "tidak ada waktu terbuang. Itu persis model asyncio: SATU thread yang tidak pernah",
                    "menganggur, bukan banyak thread yang berlarian bersama-sama.",
                    "",
                    "Tiga kata yang harus jelas dulu:",
                    "  coroutine   -> fungsi yang ditulis dengan 'async def'. Ia bisa DIBEKUKAN di tengah jalan",
                    "                 lalu dilanjutkan lagi, persis seperti generator di materi Iterator &",
                    "                 Generator. Bedanya, yang membangunkannya bukan next() tapi event loop.",
                    "  await       -> 'aku menunggu hasil ini; sementara itu pakai giliranku untuk yang lain'.",
                    "                 Hanya boleh ditulis DI DALAM async def. Di luar itu: SyntaxError.",
                    "  event loop  -> penjadwal yang memegang antrean coroutine dan membagi giliran.",
                    "                 Kamu tidak membuatnya sendiri; asyncio.run() yang menyalakan lalu",
                    "                 mematikannya. Itu satu-satunya pintu masuk dari kode biasa ke dunia async.",
                    "",
                    "Satu konsekuensi yang paling sering disalahpahami: giliran HANYA berpindah di titik await.",
                    "Di antara dua await, kodemu jalan sendirian dan tidak bisa diserobot. Itu kabar baik, sebab",
                    "race condition yang menghantui thread di materi sebelumnya nyaris tidak ada di sini. Tapi",
                    "itu juga kabar buruk: satu baris lambat yang tidak ber-await membekukan SELURUH program.",
                ],
            },
            {
                "heading": "async def menghasilkan coroutine, bukan hasil",
                "body": [
                    "Ini jebakan nomor satu, dan ia menipu karena tidak ada error mencolok yang muncul:",
                    "",
                    "  hasil = ambil_data()      # hasil BUKAN data. hasil adalah objek coroutine.",
                    "",
                    "Python tidak menjalankan satu baris pun di dalam ambil_data(). Yang kamu pegang cuma kupon",
                    "yang masih harus ditukar. Kalau kupon itu dibuang tanpa pernah ditukar, Python mengeluh",
                    "saat objeknya dibersihkan:",
                    "",
                    "  RuntimeWarning: coroutine 'ambil_data' was never awaited",
                    "",
                    "Perhatikan: Warning, bukan Error. Program tetap keluar dengan status sukses sambil",
                    "diam-diam tidak mengerjakan apa-apa - jenis bug yang paling lama tidak ketahuan.",
                    "Menukar kuponnya ada dua cara: 'await' dari dalam async def, atau 'asyncio.run()' dari",
                    "kode biasa di luar.",
                ],
                "code": """import asyncio

async def ambil(nama, detik):
    print("mulai   ", nama)
    await asyncio.sleep(detik)      # menunggu, tapi TIDAK membekukan program
    print("selesai ", nama)
    return nama.upper()

async def main():                   # await hanya boleh di dalam async def
    hasil = await ambil("data-a", 0.2)
    print("hasil:", hasil)

# Memanggil coroutine seperti fungsi biasa TIDAK menjalankan isinya:
c = ambil("data-x", 0.2)
print(type(c))
print("tidak ada satu baris pun di dalam ambil() yang jalan")
c.close()        # tanpa ini: RuntimeWarning: coroutine 'ambil' was never awaited

asyncio.run(main())   # inilah yang menyalakan event loop dan menjalankan main()

# <class 'coroutine'>
# tidak ada satu baris pun di dalam ambil() yang jalan
# mulai    data-a
# selesai  data-a
# hasil: DATA-A""",
            },
            {
                "heading": "Menunggu banyak sekaligus: gather, create_task & TaskGroup",
                "body": [
                    "Menulis 'await' tiga kali berturut-turut TIDAK membuat ketiganya berjalan bersamaan.",
                    "await artinya 'berhenti di sini sampai yang ini selesai'. Yang membuatnya bersamaan:",
                    "",
                    "  asyncio.gather(a(), b())        -> jalankan semua, tunggu semua. Hasilnya daftar,",
                    "                                     urut sesuai ARGUMEN, bukan sesuai siapa duluan selesai.",
                    "  asyncio.create_task(a())        -> jadwalkan SEKARANG lalu lanjut ke baris berikutnya;",
                    "                                     hasilnya diambil dengan 'await task' kapan pun perlu.",
                    "  async with asyncio.TaskGroup()  -> Python 3.11+. Blok with-nya baru selesai setelah semua",
                    "                                     task di dalamnya selesai, dan kalau SATU melempar",
                    "                                     exception, sisanya otomatis dibatalkan.",
                    "",
                    "Jebakan create_task: simpan hasilnya ke variabel. Event loop hanya memegang task dengan",
                    "referensi lemah, jadi task yang tidak disimpan bisa dibuang garbage collector di tengah",
                    "jalan. Bug ini kadang muncul kadang tidak, tergantung waktu - jenis yang paling melelahkan.",
                    "",
                    "Untuk kode baru, TaskGroup pilihan paling aman. gather biasa membiarkan task lain TERUS",
                    "jalan saat satu di antaranya gagal, dan itu sumber 'task yang masih hidup padahal",
                    "programnya sudah menyerah'.",
                    "",
                    "Contoh di bawah mengunduh dua hal yang masing-masing makan 0,3 detik. Berurutan butuh",
                    "0,6 detik; tiga bentuk lainnya cukup 0,3 detik - waktu yang sama seperti mengunduh satu.",
                ],
                "code": """import asyncio
import time

async def unduh(nama, detik):
    await asyncio.sleep(detik)
    return nama.upper()

async def berurutan():
    a = await unduh("a", 0.3)        # tunggu sampai selesai...
    b = await unduh("b", 0.3)        # ...baru yang ini mulai
    return [a, b]

async def dengan_gather():
    return await asyncio.gather(unduh("a", 0.3), unduh("b", 0.3))

async def dengan_create_task():
    t1 = asyncio.create_task(unduh("a", 0.3))   # langsung dijadwalkan jalan
    t2 = asyncio.create_task(unduh("b", 0.3))
    return [await t1, await t2]

async def dengan_taskgroup():        # butuh Python 3.11+
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(unduh("a", 0.3))
        t2 = tg.create_task(unduh("b", 0.3))
    return [t1.result(), t2.result()]

async def main():
    for nama, cara in [("berurutan", berurutan), ("gather", dengan_gather),
                       ("create_task", dengan_create_task),
                       ("TaskGroup", dengan_taskgroup)]:
        mulai = time.perf_counter()
        hasil = await cara()
        lipat = (time.perf_counter() - mulai) / 0.3     # 0,3 = lama satu unduhan
        print(f"{nama:12} {hasil} -> {lipat:.0f}x waktu satu unduhan")

asyncio.run(main())

# berurutan    ['A', 'B'] -> 2x waktu satu unduhan
# gather       ['A', 'B'] -> 1x waktu satu unduhan
# create_task  ['A', 'B'] -> 1x waktu satu unduhan
# TaskGroup    ['A', 'B'] -> 1x waktu satu unduhan""",
            },
            {
                "heading": "Satu panggilan blocking membekukan seluruh loop",
                "body": [
                    "time.sleep(1) menahan THREAD. Di dalam async def, thread itu satu-satunya thread yang",
                    "memutar event loop, jadi selama satu detik itu tidak ada coroutine lain yang dapat giliran.",
                    "asyncio.sleep(1) sebaliknya: ia menitip pesan 'bangunkan aku satu detik lagi' lalu MELEPAS",
                    "gilirannya. Perbedaannya bukan soal gaya penulisan - yang satu jalan, yang satu tidak.",
                    "",
                    "Aturan yang sama berlaku untuk semua panggilan blocking, bukan hanya sleep:",
                    "  requests.get(...)   f.read() atas berkas besar   input()   driver database sinkron",
                    "",
                    "Kalau sebuah library sinkron memang harus dipakai di dalam kode async, buang ia ke thread",
                    "lain supaya event loop tetap bernapas:",
                    "  hasil = await asyncio.to_thread(fungsi_lambat, argumen)   # Python 3.9+",
                    "",
                    "Contoh di bawah menyerahkan tiga tugas ke gather. Yang blocking tidak menghemat sedetik",
                    "pun - tiga tugas 0,5 detik tetap makan 3x waktu satu tugas, persis seperti tanpa async.",
                ],
                "code": """import asyncio
import time

async def tidur_blocking():
    time.sleep(0.5)               # SALAH: menahan thread yang sedang memutar loop

async def tidur_async():
    await asyncio.sleep(0.5)      # BENAR: giliran diserahkan ke event loop

async def tiga_sekaligus(kerja):
    mulai = time.perf_counter()
    await asyncio.gather(kerja(), kerja(), kerja())
    return time.perf_counter() - mulai

def baca_sinkron():               # bayangkan ini library lama yang tidak punya versi async
    time.sleep(0.5)
    return "isi berkas"

async def main():
    for nama, kerja in [("time.sleep", tidur_blocking),
                        ("asyncio.sleep", tidur_async)]:
        detik = await tiga_sekaligus(kerja)
        print(f"{nama:14} 3 tugas @0,5 detik -> {detik / 0.5:.0f}x waktu satu tugas")

    # Fungsi sinkron yang terpaksa dipakai: buang ke thread lain, jangan panggil langsung.
    hasil = await asyncio.to_thread(baca_sinkron)
    print("asyncio.to_thread ->", hasil)

asyncio.run(main())

# time.sleep     3 tugas @0,5 detik -> 3x waktu satu tugas
# asyncio.sleep  3 tugas @0,5 detik -> 1x waktu satu tugas
# asyncio.to_thread -> isi berkas""",
            },
            {
                "heading": "async with, async for, dan kapan async TIDAK perlu",
                "body": [
                    "with dan for punya kembaran async, dan inilah bentuk yang akan kamu temui di kode nyata:",
                    "",
                    "  async with httpx.AsyncClient() as klien:            # __aenter__ / __aexit__",
                    "      jawaban = await klien.get(alamat)",
                    "      async for potongan in jawaban.aiter_bytes():    # __anext__, boleh menunggu",
                    "          print(len(potongan))",
                    "",
                    "Alasannya sama seperti async def: membuka koneksi dan menutupnya juga MENUNGGU jaringan,",
                    "jadi langkah itu pun harus bisa melepas giliran. Aturan main with dan for dari materi",
                    "Context Manager dan Perulangan tidak berubah sedikit pun; cuma ada kata 'async' di depan.",
                    "Kalau salah pakai - 'with' biasa untuk objek async - error-nya menyebut __enter__ hilang.",
                    "",
                    "Di FastAPI, framework yang disebut di materi Roadmap, endpoint-nya ditulis begini:",
                    "",
                    "  @app.get('/produk')",
                    "  async def daftar_produk():",
                    "      return await db.ambil_semua()",
                    "",
                    "Sekarang kamu tahu kenapa hampir seluruh dokumentasinya berbentuk async def: supaya satu",
                    "proses sanggup melayani ratusan permintaan yang kebetulan sedang sama-sama menunggu",
                    "database, tanpa satu thread pun per permintaan.",
                    "",
                    "KAPAN JUSTRU TIDAK PERLU async:",
                    "  - Skrip yang mengerjakan satu hal lalu selesai. Tidak ada yang bisa disambi.",
                    "  - Kerja berat di CPU (mengolah gambar, menghitung angka). async tidak menambah satu inti",
                    "    pun; untuk itu pakai multiprocessing dari materi sebelumnya.",
                    "  - Kode yang semua library-nya sinkron. Membungkusnya dengan async def tidak mempercepat",
                    "    apa pun, dan kamu hanya menambah sintaks yang harus dijaga.",
                    "",
                    "Hubungannya dengan GIL: asyncio tidak melawan GIL, ia MENGHINDARI kebutuhan akan thread.",
                    "Satu thread, satu GIL, nol lock. Ringkasnya - banyak menunggu I/O: asyncio (atau thread);",
                    "banyak menghitung: proses.",
                ],
            },
        ],
    },
    {
        "title": "42. Virtual Environment, pip & Testing (pytest)",
        "sections": [
            {
                "body": [
                    "Virtual environment (venv) = lingkungan Python TERISOLASI per",
                    "project, agar library satu project tidak bentrok dengan project lain.",
                    "",
                    "Membuat & memakai venv:",
                    "  python3 -m venv venv          # buat folder venv/",
                    "  source venv/bin/activate      # aktifkan (Linux/Mac)",
                    "  venv\\\\Scripts\\\\activate         # aktifkan (Windows)",
                    "  pip install nama_library       # install HANYA di venv ini",
                    "  deactivate                     # keluar dari venv",
                    "",
                    "requirements.txt: mencatat semua dependency agar project",
                    "mudah di-setup ulang di komputer lain:",
                    "  pip freeze > requirements.txt",
                    "  pip install -r requirements.txt",
                ]
            },
            {
                "heading": "Unit testing dengan pytest",
                "code": """# file kalkulator.py
def tambah(a, b):
    return a + b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b


# file test_kalkulator.py
from kalkulator import tambah, bagi
import pytest

def test_tambah():
    assert tambah(2, 3) == 5
    assert tambah(-1, 1) == 0

def test_bagi():
    assert bagi(10, 2) == 5

def test_bagi_nol_melempar_error():
    with pytest.raises(ValueError):
        bagi(10, 0)

# Jalankan semua test dengan perintah terminal:
#   pytest
#   pytest -v          (lebih detail)
#   pytest test_kalkulator.py::test_tambah   (satu test spesifik)"""
            },
            {
                "body": [
                    "Konsep AAA dalam menulis test (sama seperti bahasa lain):",
                    "  1. Arrange -> siapkan data yang dibutuhkan.",
                    "  2. Act     -> panggil fungsi yang diuji.",
                    "  3. Assert  -> pastikan hasilnya sesuai harapan.",
                    "",
                    "assert dasar Python (dipakai juga di luar pytest):",
                    "  assert kondisi, \"pesan jika gagal\"",
                    "  assert 1 + 1 == 2, \"Matematika rusak!\"",
                    "",
                    "Tools penting ekosistem Python untuk kerja profesional:",
                    "  pip / venv    -> manajemen dependency & isolasi environment",
                    "  pytest        -> testing (alternatif: unittest bawaan Python)",
                    "  black / ruff  -> formatter & linter otomatis (kerapian kode)",
                    "  mypy          -> pengecekan type hint secara statis",
                ]
            },
        ],
    },
    {
        "title": "43. Testing Lebih Dalam: fixture, parametrize & unittest",
        "sections": [
            {
                "body": [
                    "Materi 20 menunjukkan bentuk paling dasar sebuah test: satu fungsi,",
                    "satu assert. Kode nyata tidak berhenti di situ. Buka berkas test",
                    "proyek mana pun, dan hal pertama yang membingungkan hampir selalu",
                    "sama - fungsi test-nya PUNYA PARAMETER, padahal tidak ada satu baris",
                    "pun yang memanggil fungsi itu dan mengoper argumennya.",
                    "",
                    "  def test_pakai_mengurangi_saldo(dompet):  # 'dompet' dari mana?",
                    "      dompet.pakai(30)",
                    "",
                    "Jawabannya: pytest yang mengisinya. Sebelum menjalankan sebuah fungsi",
                    "test, pytest membaca NAMA tiap parameternya, lalu mencari fungsi lain",
                    "bertanda @pytest.fixture dengan nama yang sama persis. Nilai kembalian",
                    "fungsi itulah yang dioper masuk. Yang menyambungkan keduanya adalah",
                    "NAMA - bukan urutan, bukan import.",
                    "",
                    "Karena itu salah ketik nama parameter tidak memunculkan NameError,",
                    "melainkan:",
                    "",
                    "  E    fixture 'dompett' not found",
                    "  >    available fixtures: capsys, monkeypatch, tmp_path, dompet, ...",
                    "",
                    "dan test-nya dihitung ERROR, bukan FAILED - test-nya bahkan belum",
                    "sempat jalan. Begitu melihat kalimat itu, yang salah hampir selalu",
                    "ejaan nama parameternya.",
                    "",
                    "Kenapa repot bikin fixture, bukan langsung menulis d = Dompet(100) di",
                    "setiap test? Supaya tiap test berangkat dari keadaan BERSIH yang sama.",
                    "Secara bawaan fixture dipanggil ULANG untuk setiap fungsi test, jadi",
                    "test kedua tidak mewarisi sisa-sisa test pertama. Itulah yang membuat",
                    "test boleh dijalankan dalam urutan apa pun.",
                    "",
                    "scope: seberapa sering sebuah fixture dipanggil ulang.",
                    "",
                    "  scope=\"function\"   (bawaan) dipanggil lagi untuk SETIAP fungsi test",
                    "  scope=\"class\"      sekali untuk satu class test",
                    "  scope=\"module\"     sekali untuk satu berkas test",
                    "  scope=\"session\"    sekali untuk seluruh jalannya pytest",
                    "",
                    "JEBAKAN scope. Menaikkannya ke \"module\" atau \"session\" supaya 'lebih",
                    "hemat' berarti satu objek yang sama dipakai bersama-sama. Kalau objek",
                    "itu mutable, test pertama yang mengubahnya diam-diam mewariskan",
                    "perubahan itu ke test sesudahnya:",
                    "",
                    "  @pytest.fixture(scope=\"module\")",
                    "  def keranjang():",
                    "      return []",
                    "  # test_satu menambah 1 item, assert len == 1  -> lulus",
                    "  # test_dua  menambah 1 item, assert len == 1  -> GAGAL, isinya 2",
                    "",
                    "Gejalanya yang paling jahat: test lulus kalau dijalankan sendirian,",
                    "tapi gagal kalau dijalankan bersama yang lain. Pakai scope besar hanya",
                    "untuk yang mahal DAN tidak diubah - koneksi database, server uji,",
                    "berkas contoh yang cuma dibaca.",
                    "",
                    "yield: pembersihan sesudah test. Fixture yang memakai yield (bukan",
                    "return) menyerahkan nilainya di baris yield, lalu MELANJUTKAN sisa",
                    "barisnya setelah test selesai - baik test-nya lulus maupun gagal.",
                    "Polanya persis generator di materi 18 dan @contextmanager di materi",
                    "19: yang di atas yield itu persiapan, yang di bawah pembersihan.",
                ],
            },
            {
                "heading": "Fixture & conftest.py: satu objek baru untuk tiap test",
                "code": """# file: dompet.py
class Dompet:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def isi(self, jumlah):
        self.saldo += jumlah

    def pakai(self, jumlah):
        if jumlah > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= jumlah


# file: conftest.py
# Nama berkasnya WAJIB conftest.py, dan tidak boleh di-import siapa pun.
# pytest membacanya sendiri; semua berkas test di folder ini dan di
# subfoldernya otomatis melihat fixture yang ditulis di sini.
import pytest
from dompet import Dompet


@pytest.fixture
def dompet():
    d = Dompet(100)      # persiapan
    yield d              # nilai ini yang masuk ke parameter fungsi test
    d.saldo = 0          # pembersihan: jalan SESUDAH test, lulus atau gagal


# file: test_dompet.py
import pytest
# Perhatikan: TIDAK ada 'from conftest import dompet'. Memang tidak perlu.


def test_isi_menambah_saldo(dompet):      # parameter 'dompet' = nama fixture
    dompet.isi(50)
    assert dompet.saldo == 150


def test_pakai_mengurangi_saldo(dompet):  # Dompet BARU, bukan sisa test atas
    dompet.pakai(30)
    assert dompet.saldo == 70


def test_pakai_kebanyakan_melempar_error(dompet):
    with pytest.raises(ValueError):
        dompet.pakai(999)
    assert dompet.saldo == 100            # gagal pakai tak boleh ubah saldo


# Jalankan dari folder yang sama:  pytest -v
#   test_dompet.py::test_isi_menambah_saldo PASSED
#   test_dompet.py::test_pakai_mengurangi_saldo PASSED
#   test_dompet.py::test_pakai_kebanyakan_melempar_error PASSED
#   3 passed""",
            },
            {
                "heading": "parametrize, fixture bawaan, skip & xfail",
                "body": [
                    "@pytest.mark.parametrize menjalankan SATU fungsi test berkali-kali",
                    "dengan data berbeda. Tanpa itu orang menulis lima test yang isinya",
                    "sama persis kecuali angkanya - dan ketika rumusnya berubah, kelimanya",
                    "harus disunting satu per satu.",
                    "",
                    "Jumlah nama di string parameter WAJIB sama dengan panjang tiap tuple",
                    "di daftarnya; kalau meleset, pytest menolak mengumpulkan test itu",
                    "sebelum satu pun dijalankan. Untuk satu parameter saja, daftarnya",
                    "cukup list biasa tanpa tuple: [0, 5, 10].",
                    "",
                    "Hasilnya bukan satu test, melainkan EMPAT test terpisah yang punya",
                    "nama sendiri-sendiri, seperti test_hitung_pajak[6000000-50000]. Satu",
                    "kasus gagal tidak menghentikan sisanya, dan laporannya menyebut kasus",
                    "mana yang gagal. Itu keunggulannya dibanding menumpuk empat assert di",
                    "dalam satu fungsi test, yang berhenti di assert pertama yang gagal.",
                    "",
                    "Fixture bawaan pytest - tidak perlu ditulis, tinggal diminta lewat",
                    "nama parameter:",
                    "",
                    "  tmp_path      objek Path ke folder kosong khusus test itu, dihapus",
                    "                sendiri. Pengganti menulis ke \"data.txt\" di folder",
                    "                proyek, yang akan saling menimpa antar test dan",
                    "                mengotori repo.",
                    "  monkeypatch   mengubah environment variable, atribut objek, atau",
                    "                isi dict SEMENTARA; semuanya dikembalikan otomatis",
                    "                begitu test selesai.",
                    "  capsys        menangkap apa yang dicetak print(). readouterr()",
                    "                memberi .out dan .err - inilah cara menguji fungsi",
                    "                yang kerjanya mencetak.",
                    "",
                    "Menandai test yang belum siap:",
                    "",
                    "  @pytest.mark.skip(reason=\"...\")         selalu dilewati",
                    "  @pytest.mark.skipif(kondisi, reason=)   dilewati kalau kondisi True",
                    "  @pytest.mark.xfail(reason=\"...\")        diharapkan gagal (bug lama)",
                    "",
                    "JEBAKAN xfail: kalau test-nya ternyata LULUS, statusnya XPASS - dan",
                    "itu tidak dihitung kegagalan. Bug yang sudah terlanjur diperbaiki bisa",
                    "menumpuk sebagai xfail selamanya tanpa ada yang menyadarinya. Pakai",
                    "xfail(strict=True) supaya XPASS dinyatakan FAILED, sehingga tandanya",
                    "wajib dibersihkan.",
                    "",
                    "Dan jangan pernah menghapus reason=. Test yang dimatikan tanpa alasan",
                    "tertulis tidak akan pernah dinyalakan lagi oleh siapa pun, karena tak",
                    "seorang pun tahu kenapa ia mati.",
                ],
                "code": """# file: pajak.py
def hitung_pajak(gaji):
    if gaji <= 5000000:
        return 0
    return int((gaji - 5000000) * 0.05)


# file: test_pajak.py
import os
import pytest
from pajak import hitung_pajak


@pytest.mark.parametrize("gaji, pajak", [
    (0, 0),
    (5000000, 0),
    (6000000, 50000),
    (10000000, 250000),
])
def test_hitung_pajak(gaji, pajak):     # satu fungsi -> empat test terpisah
    assert hitung_pajak(gaji) == pajak


def test_menulis_laporan(tmp_path):     # folder kosong khusus test ini
    berkas = tmp_path / "laporan.txt"
    berkas.write_text("gaji 6000000\\n", encoding="utf-8")
    assert berkas.read_text(encoding="utf-8").startswith("gaji")


def test_membaca_env(monkeypatch):      # ubahannya dibatalkan otomatis
    monkeypatch.setenv("MODE_APP", "uji")
    assert os.environ["MODE_APP"] == "uji"


def test_cetakan_ditangkap_capsys(capsys):
    print("halo")
    keluar = capsys.readouterr()
    assert keluar.out == "halo\\n"


@pytest.mark.skip(reason="potongan BPJS belum ditulis")
def test_potongan_bpjs():
    assert hitung_pajak(6000000) == 999


@pytest.mark.xfail(reason="pembulatan ke bawah, sudah dilaporkan")
def test_pembulatan_seribu_rupiah():
    assert hitung_pajak(5000001) == 1


# pytest -v  ->  7 passed, 1 skipped, 1 xfailed""",
            },
            {
                "heading": "unittest: bentuk yang dipakai pustaka standar",
                "body": [
                    "unittest adalah framework testing BAWAAN Python - tidak perlu pip",
                    "install apa pun. pytest bukan bawaan (materi 20: pasang di dalam venv",
                    "dengan pip install pytest). Bentuk keduanya berbeda jauh, dan kamu",
                    "perlu bisa MEMBACA dua-duanya:",
                    "",
                    "                  pytest                 unittest",
                    "  wadah test      fungsi biasa           method di class TestCase",
                    "  nama wajib      berkas test_*.py       method berawalan test_",
                    "                  fungsi test_*",
                    "  persiapan       @pytest.fixture        setUp() / setUpClass()",
                    "  pembersihan     baris setelah yield    tearDown() / tearDownClass()",
                    "  memeriksa       assert biasa           self.assertEqual(...) dst",
                    "  menjalankan     pytest                 python3 -m unittest discover",
                    "",
                    "Di unittest, assert bukan keyword melainkan METHOD milik TestCase.",
                    "Yang paling sering dipakai (semuanya diawali self.):",
                    "",
                    "  assertEqual(a, b)         assertNotEqual(a, b)",
                    "  assertTrue(x)             assertFalse(x)",
                    "  assertIn(a, wadah)        assertNotIn(a, wadah)",
                    "  assertIsNone(x)           assertIsInstance(x, tipe)",
                    "  assertAlmostEqual(a, b)   untuk float: 0.1 + 0.2 bukan persis 0.3",
                    "  assertRaises(Error)       dipakai sebagai 'with', lihat di bawah",
                    "",
                    "Kenapa tidak assert biasa saja? assertEqual mencetak KEDUA nilainya",
                    "saat gagal ('150000 != 140000'), sedangkan assert a == b polos cuma",
                    "bilang AssertionError tanpa angka apa pun. Selain itu assert dimatikan",
                    "TOTAL kalau Python dijalankan dengan flag -O, sedangkan assertEqual",
                    "tetap bekerja. (pytest menambal kekurangan itu dengan menulis ulang",
                    "bytecode berkas test-nya, jadi di pytest assert polos tetap memamerkan",
                    "nilai kedua sisinya. Di luar berkas test, sihir itu tidak berlaku.)",
                ],
                "code": "import unittest\n\n\ndef normalkan(nama):\n    \"\"\"'  budi   santoso ' -> 'Budi Santoso'.\"\"\"\n    return \" \".join(nama.split()).title()\n\n\nclass TestNormalkan(unittest.TestCase):\n\n    def setUp(self):\n        # Dijalankan ULANG sebelum SETIAP method test_ di bawah.\n        self.kotor = \"  budi   santoso \"\n\n    def tearDown(self):\n        # Setelah tiap test, lulus maupun gagal (mirip baris setelah yield).\n        self.kotor = None\n\n    def test_spasi_berlebih_dirapikan(self):\n        self.assertEqual(normalkan(self.kotor), \"Budi Santoso\")\n\n    def test_kapital_dirapikan(self):\n        self.assertEqual(normalkan(\"SITI aminah\"), \"Siti Aminah\")\n\n    def test_nama_kosong_tetap_kosong(self):\n        self.assertEqual(normalkan(\"   \"), \"\")\n\n    def test_nama_depan_ada_di_hasil(self):\n        self.assertIn(\"Budi\", normalkan(self.kotor))\n\n    def test_angka_bukan_string_melempar_error(self):\n        with self.assertRaises(AttributeError):\n            normalkan(123)\n\n    def cek_ini_tidak_pernah_jalan(self):\n        # Tidak berawalan test_, jadi unittest TIDAK PERNAH memanggilnya.\n        # Buktinya: laporannya berbunyi \"Ran 5 tests\", bukan 6.\n        self.assertEqual(1, 2)\n\n\nif __name__ == \"__main__\":\n    unittest.main(verbosity=2)",
            },
            {
                "body": [
                    "Contoh di atas program utuh: simpan, lalu jalankan seperti skrip",
                    "biasa. Satu hal yang bikin panik pertama kali - laporan unittest",
                    "dicetak ke stderr, bukan stdout. Jadi kalau tombol \"Coba jalankan\" di",
                    "aplikasi ini menaruh laporannya di kotak pesan error padahal semua",
                    "lulus, itu bukan kegagalan. Lihat dua baris terakhirnya: 'OK', dan",
                    "'Kode keluar: 0'. Kalau ada test yang gagal, barisnya berbunyi",
                    "'FAILED (failures=1)' dan kode keluarnya bukan 0 - angka itulah yang",
                    "dibaca server CI untuk memutuskan sebuah commit boleh masuk atau tidak.",
                    "",
                    "Menjalankan seluruh folder test, tanpa if __name__ di tiap berkas:",
                    "",
                    "  python3 -m unittest discover -s tests -t .",
                    "      # -s: folder berisi test, -t: folder akar proyek",
                    "  python3 -m unittest tests.test_nama          # satu berkas saja",
                    "  python3 -m unittest tests.test_nama.TestNormalkan.test_kapital_dirapikan",
                    "",
                    "Persis perintah pertama itulah yang dipakai aplikasi yang sedang kamu",
                    "baca ini untuk menjalankan ratusan test-nya sendiri.",
                    "",
                    "Tiga jebakan unittest yang benar-benar sering memakan waktu:",
                    "",
                    "  1. Method yang tidak berawalan test_ TIDAK PERNAH dijalankan, tanpa",
                    "     peringatan apa pun. Salah ketik 'tes_saldo' saja sudah cukup",
                    "     untuk membuat sebuah test hilang diam-diam, dan laporannya tetap",
                    "     hijau. Biasakan membaca angka 'Ran N tests': kalau N mengecil",
                    "     padahal kamu menambah test, di situlah masalahnya.",
                    "  2. discover hanya mengambil berkas yang cocok pola test*.py (ubah",
                    "     dengan -p), dan dengan -t . folder tests/ WAJIB punya berkas",
                    "     __init__.py. Tanpa itu muncul 'ImportError: Start directory is",
                    "     not importable' - bukan nol test, melainkan gagal total sebelum",
                    "     satu pun test sempat dimuat.",
                    "  3. assertRaises harus menerima FUNGSINYA, bukan hasil pemanggilan:",
                    "       self.assertRaises(ValueError, bagi(1, 0))   # SALAH",
                    "       # bagi(1,0) dijalankan duluan, error-nya meledak sebelum",
                    "       # assertRaises sempat memasang jaringnya",
                    "       self.assertRaises(ValueError, bagi, 1, 0)   # benar",
                    "       with self.assertRaises(ValueError):         # paling terbaca",
                    "           bagi(1, 0)",
                    "",
                    "Satu lagi yang sering disangka bug: setiap method test dijalankan pada",
                    "INSTANCE BARU dari class-nya. self.kotor yang dipasang di satu test",
                    "tidak akan ada di test berikutnya. Itu disengaja - test tidak boleh",
                    "saling bergantung. Yang dipakai untuk berbagi persiapan adalah setUp(),",
                    "yang memang dijalankan ulang sebelum tiap test.",
                    "",
                    "Kenapa harus kuasai dua-duanya. Pustaka standar Python, banyak proyek",
                    "lama, dan aplikasi yang sedang kamu pakai ini semuanya memakai",
                    "unittest; kalau cuma kenal pytest, folder tests/ mereka tidak akan",
                    "terbaca. Kabar baiknya, satu arah gratis: pytest bisa menjalankan class",
                    "TestCase apa adanya, jadi sebuah proyek boleh pindah pelan-pelan.",
                    "Sebaliknya tidak - unittest tidak mengerti fixture maupun parametrize,",
                    "dan method TestCase yang diberi parameter tambahan langsung error.",
                ],
            },
        ],
    },
    {
        "title": "44. Roadmap Menjadi Python Developer Handal",
        "sections": [
            {
                "body": [
                    "Kamu sudah menguasai fondasi Python yang solid: sintaks,",
                    "OOP, exception, file I/O, decorator, hingga testing.",
                    "Berikut roadmap realistis untuk melangkah lebih jauh.",
                    "",
                    "TAHAP 1 - Kuatkan Fondasi (kamu di sini):",
                    "  - Bisa membaca & menulis semua konsep di atas dengan lancar.",
                    "  - Latihan: kerjakan soal di HackerRank/LeetCode kategori Python.",
                    "",
                    "TAHAP 2 - Pilih Jalur Spesialisasi:",
                    "  Web Development:",
                    "    - Flask (ringan, fleksibel) atau Django (lengkap, 'batteries",
                    "      included') untuk backend web & REST API.",
                    "    - FastAPI - populer untuk API modern, cepat, otomatis dokumentasi.",
                    "      Dibangun di atas async/await, jadi bekalnya ada di materi",
                    "      Asinkron: async, await & asyncio.",
                    "  Data Science / AI:",
                    "    - NumPy & Pandas -> manipulasi data numerik/tabel.",
                    "    - Matplotlib/Seaborn -> visualisasi data.",
                    "    - scikit-learn -> machine learning klasik.",
                    "    - PyTorch/TensorFlow -> deep learning.",
                    "  Automation/DevOps:",
                    "    - Script otomasi (file, email, web scraping dengan requests/",
                    "      BeautifulSoup/Selenium).",
                    "    - Ansible (berbasis Python) untuk automasi infrastruktur.",
                ]
            },
            {
                "body": [
                    "TAHAP 3 - Bangun Project Nyata (paling penting!):",
                    "  1. CLI tool sederhana (to-do list, expense tracker) - argparse dan",
                    "     sys.argv-nya ada di materi Program Baris Perintah: sys, os & argparse.",
                    "  2. REST API dengan FastAPI/Flask + database (SQLite/PostgreSQL).",
                    "  3. Web scraper yang mengambil & mengolah data nyata.",
                    "  4. Project data analysis dari dataset publik (Kaggle, dsb).",
                    "  5. Semua project di atas WAJIB disertai unit test (pytest).",
                    "",
                    "TAHAP 4 - Kebiasaan Profesional:",
                    "  1. Ikuti PEP 8 (panduan gaya kode resmi Python) secara konsisten.",
                    "  2. Pakai type hint untuk project yang lebih besar dari skrip kecil.",
                    "  3. Gunakan Git untuk semua project, biasakan commit rapi.",
                    "  4. Baca kode open source Python populer di GitHub (requests,",
                    "     flask, dsb) untuk belajar gaya kode yang baik. Modal membacanya",
                    "     sudah kamu punya: materi Struktur Project Python untuk memahami",
                    "     tata letak berkas & paketnya, dan materi Anotasi Tipe untuk",
                    "     signature bertanda -> yang bertaburan di dalamnya.",
                    "  5. Pahami perbedaan Python 2 vs 3 secukupnya (Python 2 sudah EOL,",
                    "     tapi kadang masih ditemui di kode lama/legacy system).",
                ]
            },
            {
                "body": [
                    "Kebiasaan harian agar handal:",
                    "  1. Ketik ulang semua contoh di aplikasi ini, jangan copy-paste.",
                    "  2. Coba pecahkan masalah dengan LEBIH dari satu cara (misal:",
                    "     for-loop vs list comprehension) untuk memahami trade-off-nya.",
                    "  3. Gunakan Python REPL/Jupyter Notebook untuk eksperimen cepat.",
                    "  4. Baca error message Python dengan teliti - traceback biasanya",
                    "     menunjuk PERSIS baris & jenis error yang terjadi. Cara membacanya",
                    "     baris per baris ada di materi Membaca Traceback & Menangkap Error",
                    "     Secara Luas; balik ke sana tiap kali sebuah error terasa buntu.",
                    "  5. Kuasai SQL (lihat menu SQL di aplikasi ini) untuk melengkapi",
                    "     kemampuan sebagai backend/data developer yang komplet.",
                    "",
                    "Python terkenal karena filosofi 'The Zen of Python' - ketik",
                    "'import this' di Python untuk membacanya. Prinsip favorit:",
                    "  'Simple is better than complex.'",
                    "  'Readability counts.'",
                    "  'There should be one obvious way to do it.'",
                ]
            },
        ],
    },
]
