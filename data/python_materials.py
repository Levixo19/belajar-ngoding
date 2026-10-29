PYTHON_MATERIALS = [
    {
        "title": "1. Pengenalan Python & Instalasi",
        "sections": [
            {
                "body": [
                    "Python itu bahasa pemrograman tingkat tinggi. Artinya, kamu nulis",
                    "perintah dengan kata-kata yang mirip bahasa manusia, dan urusan mesinnya",
                    "diurus Python. Kodenya gampang dibaca dan bisa dipakai untuk banyak hal.",
                    "",
                    "Sedikit sejarahnya:",
                    "  - Python dibuat oleh Guido van Rossum dan pertama dirilis tahun 1991.",
                    "  - Python itu bahasa interpreted. Kodemu langsung dijalankan, tanpa",
                    "    langkah kompilasi yang harus kamu lakukan sendiri.",
                    "  - Python dipakai untuk web (Django dan Flask), data science, AI dan",
                    "    machine learning (ML), otomatisasi dan scripting, DevOps, sampai",
                    "    game sederhana.",
                    "",
                    "Kenapa Python cocok untuk pemula? Ada tiga alasan:",
                    "  - Sintaksnya, yaitu aturan cara menulis kodenya, mirip bahasa Inggris",
                    "    dan jarang pakai kurung kurawal.",
                    "  - Komunitasnya besar. Ada banyak library siap pakai, yaitu kumpulan",
                    "    kode buatan orang lain yang tinggal kamu pakai. Tempat",
                    "    kumpulannya namanya PyPI.",
                    "  - Python terkenal dengan semboyan 'Batteries included': banyak fitur",
                    "    udah tersedia bawaan, nggak perlu dipasang lagi.",
                    "",
                    "Cara memasang Python:",
                    "  - Unduh dari https://python.org. Pilih versi 3.x, jangan 2.x.",
                    "  - Cek apakah udah terpasang dengan perintah ini di terminal:",
                    "      python3 --version",
                    "    Di Windows perintahnya python --version.",
                    "  - Python udah membawa pip, yaitu package manager bawaan. Gunanya",
                    "    untuk memasang library tambahan.",
                    "",
                    "Cara menjalankan program Python:",
                    "  1. Bikin berkas bernama program.py.",
                    "  2. Tulis kodenya (lihat contoh di bawah).",
                    "  3. Jalankan dengan perintah:  python3 program.py",
                    "",
                    "Python juga punya mode interaktif yang namanya REPL, singkatan dari",
                    "Read-Eval-Print Loop: baca, jalankan, cetak hasilnya, ulangi. Ketik",
                    "'python3' di terminal, lalu kamu bisa langsung nyoba kode baris per",
                    "baris.",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """print("Halo Dunia!")
print("Aku sedang belajar Python.")"""
            },
            {
                "heading": "Aturan dasar sintaks Python dan shebang",
                "body": [
                    "print(...) itu fungsi bawaan untuk menampilkan teks ke layar.",
                    "",
                    "Kalau kamu pernah lihat Java atau C, di sana program harus dibungkus",
                    "class atau fungsi main dulu. Python nggak butuh itu. Python langsung",
                    "menjalankan kodemu baris demi baris, dari atas ke bawah.",
                    "",
                    "Aturan dasar menulis kode Python:",
                    "  1. Nggak pakai titik koma (;) di akhir baris. Titik koma di situ",
                    "     boleh, tapi jarang ada yang nulis.",
                    "  2. Nggak pakai { } untuk menandai blok kode. Python pakai indentasi,",
                    "     yaitu spasi atau tab di awal baris.",
                    "  3. Indentasinya harus konsisten. Yang disarankan 4 spasi. Indentasi",
                    "     itu yang menentukan baris mana yang termasuk sebuah kondisi",
                    "     atau fungsi.",
                    "  4. Komentar satu baris ditulis pakai tanda pagar (#).",
                    "  5. Huruf besar dan kecil dianggap beda (case-sensitive). Nama dan",
                    "     nama itu dua hal yang berbeda.",
                    "",
                    "  # ini komentar satu baris",
                    "  \"\"\"ini komentar/docstring banyak baris\"\"\"",
                    "",
                    "Ada satu pengecualian untuk aturan nomor 4. Kalau baris pertama sebuah",
                    "berkas bunyinya begini:",
                    "",
                    "  #!/usr/bin/env python3",
                    "",
                    "baris itu bukan komentar biasa, walaupun diawali #. Namanya shebang.",
                    "Yang membacanya sistem operasi, bukan Python. Isinya ngasih tahu",
                    "program mana yang harus menjalankan berkas ini. Dengan shebang, berkas",
                    "bisa dipanggil langsung sebagai ./skrip.py tanpa ngetik python3 di",
                    "depannya.",
                    "",
                    "Jadi jangan ikut menghapus baris itu waktu merapikan komentar. Cara",
                    "memakainya dibahas lengkap di materi Program Baris Perintah: sys, os &",
                    "argparse.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di kantor, Python sering muncul sebagai skrip kecil yang dijalankan dari",
                    "terminal, misalnya python3 rekap_absen.py yang tiap pagi merapikan data",
                    "absensi karyawan. Programmer juga sering membuka REPL dengan mengetik",
                    "python3, lalu memakainya sebagai kalkulator cepat waktu ngecek hitungan.",
                    "",
                    "Kasus kecil: pemilik warung minta program yang mencetak kepala struk",
                    "tiga baris, yaitu nama warung \"Warung Bu Sri\", alamat \"Jl. Melati No.",
                    "5\", dan satu garis pemisah dari tanda sama dengan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya dulu: tiga baris teks, urutannya tetap, dan",
                    "     nggak ada hitungan apa pun.",
                    "  2. Satu baris keluaran berarti satu print(). Tulis di berkas struk.py:",
                    "      print(\"Warung Bu Sri\")",
                    "      print(\"Jl. Melati No. 5\")",
                    "      print(\"====================\")",
                    "  3. Jalankan dengan python3 struk.py dari folder tempat berkas itu",
                    "     disimpan. Hasilnya tiga baris, persis seperti yang diminta.",
                    "  4. Cek kasus pinggir. Kalau salah satu baris diawali spasi, Python",
                    "     menolak dengan IndentationError. Kalau print ditulis Print, yang",
                    "     muncul NameError, karena huruf besar dan kecil dianggap beda.",
                    "",
                    "Jebakan: menjalankan python3 struk.py dari folder lain berakhir dengan",
                    "pesan \"No such file or directory\". Python cuma mencari berkas itu di",
                    "folder tempat kamu sedang berada.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "Variabel itu nama yang kamu tempelkan ke sebuah nilai, supaya nilainya",
                    "bisa dipakai lagi nanti. Di Python kamu nggak perlu menyebut tipe",
                    "datanya waktu bikin variabel. Python melihat nilainya, lalu menentukan",
                    "tipenya sendiri. Sifat ini namanya dynamically typed.",
                    "",
                    "Tipe data dasar yang sudah ada di Python (built-in):",
                    "  int      -> bilangan bulat            umur = 20",
                    "  float    -> bilangan desimal           harga = 15000.5",
                    "  str      -> teks/string                nama = \"Budi\"",
                    "  bool     -> True atau False             lulus = True",
                    "  complex  -> bilangan kompleks (jarang)  z = 2 + 3j",
                    "  NoneType -> representasi 'tidak ada nilai'  kosong = None",
                    "",
                    "Untuk mengecek tipe sebuah nilai, ada dua cara:",
                    "  type(umur)     -> <class 'int'>",
                    "  isinstance(umur, int)  -> True",
                    "",
                    "type() ngasih tahu tipenya apa. isinstance() menjawab ya atau nggak:",
                    "apakah nilai ini bertipe int?",
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
                "heading": "Penamaan, konversi tipe, dan f-string",
                "body": [
                    "Aturan memberi nama variabel:",
                    "  1. Boleh pakai huruf, angka, dan underscore (_). Nama nggak boleh",
                    "     diawali angka.",
                    "  2. Kebiasaan yang disepakati programmer Python (konvensi) adalah",
                    "     snake_case untuk variabel dan fungsi: huruf kecil semua, antarkata",
                    "     dipisah underscore. Jadi jumlah_mahasiswa, bukan JumlahMahasiswa.",
                    "     Bentuk JumlahMahasiswa itu gaya penulisan nama class.",
                    "  3. Konstanta, yaitu nilai yang nggak dimaksudkan untuk diubah,",
                    "     biasanya ditulis huruf besar semua:",
                    "     PI = 3.14159",
                    "     Ini cuma kesepakatan. Python nggak punya keyword 'final' seperti",
                    "     Java, jadi PI tetap bisa diubah kalau kamu memaksa.",
                    "",
                    "Kamu juga bisa mengubah nilai dari satu tipe ke tipe lain. Namanya",
                    "konversi tipe data (type casting):",
                    "  int(\"10\")     -> 10        (str ke int)",
                    "  float(\"3.5\")  -> 3.5       (str ke float)",
                    "  str(100)      -> \"100\"     (int ke str)",
                    "  int(3.99)     -> 3         (float ke int, desimalnya dibuang)",
                    "",
                    "Perhatikan: int() bukan pembulatan ke bawah. Ia cuma membuang angka di",
                    "belakang koma. Untuk bilangan positif hasilnya sama, tapi int(-3.99)",
                    "hasilnya -3, bukan -4.",
                    "",
                    "Untuk menggabungkan teks dengan isi variabel, cara modernnya f-string",
                    "(ada sejak Python 3.6). Tulis huruf f sebelum tanda kutip, lalu taruh",
                    "nama variabel di dalam kurung kurawal:",
                    "  nama = \"Andi\"; umur = 20",
                    "  print(f\"Nama saya {nama}, umur {umur} tahun\")",
                    "  print(f\"Tahun depan jadi {umur + 1} tahun\")  # bisa ekspresi",
                    "",
                    "Di dalam kurung kurawal itu boleh juga ditulis hitungan, seperti umur + 1.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir menyimpan tiap data dengan tipe yang cocok: nama barang",
                    "sebagai str, jumlah sebagai int, berat timbangan sebagai float, dan",
                    "status lunas sebagai bool. Masalahnya, data yang datang dari formulir",
                    "atau berkas hampir selalu berupa teks. Jadi programmer terus-terusan",
                    "mengubah tipe sebelum bisa berhitung.",
                    "",
                    "Kasus kecil: timbangan di toko beras mengirim berat \"2.5\" (kg), dan",
                    "daftar harga mengirim \"13500\" (rupiah per kg). Dua-duanya teks. Kamu",
                    "perlu mencetak total harganya sebagai rupiah bulat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali tipe masukannya. \"2.5\" dan \"13500\" itu str, jadi belum bisa",
                    "     dikalikan sebagai angka.",
                    "  2. Pilih alat konversinya. Berat punya angka di belakang titik, jadi",
                    "     pakai float(). Harga bilangan bulat, jadi pakai int().",
                    "  3. Kalikan, lalu ubah hasilnya ke int supaya tampil tanpa \".0\":",
                    "      harga = int(\"13500\")",
                    "      berat = float(\"2.5\")",
                    "      total = harga * berat",
                    "      print(f\"Total: Rp {int(total)}\")",
                    "     Hasilnya Total: Rp 33750.",
                    "  4. Cek kasus pinggir. int() cuma membuang desimal, nggak membulatkan.",
                    "     Kalau totalnya 33749.9, yang tercetak 33749.",
                    "",
                    "Ingat: float dikali int hasilnya tetap float. Makanya total di atas",
                    "berisi 33750.0 sebelum dibungkus int().",
                ]
            },
        ],
    },
    {
        "title": "3. Masukan, Keluaran & Modul Bawaan",
        "sections": [
            {
                "body": [
                    "Sampai sini, semua contoh cuma mencetak nilai yang udah ditulis di",
                    "kodenya. Program sungguhan punya dua sisi: masukan, yaitu data yang",
                    "datang dari luar, dan keluaran, yaitu hasil yang ditampilkan. Materi",
                    "ini membahas keduanya sampai tuntas. Ditambah dua hal yang muncul di",
                    "hampir setiap berkas Python: escape sequence dan import.",
                    "",
                    "Escape sequence: karakter yang nggak bisa diketik langsung",
                    "",
                    "Gimana caranya naruh karakter \"pindah baris\" di dalam string? Menekan",
                    "Enter di tengah tanda kutip nggak bisa, karena string biasa harus",
                    "selesai di baris yang sama. Jalan keluarnya pakai backslash (\\). Tanda",
                    "ini artinya \"huruf sesudahku punya arti khusus\". Gabungan backslash dan",
                    "satu huruf itu namanya escape sequence:",
                    "",
                    "  \\n    pindah baris (newline)",
                    "  \\t    tab",
                    "  \\\\    satu backslash sungguhan",
                    "  \\\"    kutip ganda di dalam string yang dibatasi kutip ganda",
                    "  \\'    kutip tunggal di dalam string yang dibatasi kutip tunggal",
                    "",
                    "Yang paling sering disalahpahami: \\n itu satu karakter, bukan dua.",
                    "",
                    "  len(\"a\\nb\")   ->  3, bukan 4",
                    "",
                    "Backslash-nya nggak ikut tersimpan. Dia cuma cara menulis karakter itu",
                    "di kode.",
                    "",
                    "Nanti di materi File I/O kamu bakal lihat readlines() menampilkan",
                    "['Baris pertama\\n', 'Baris kedua\\n']. Itu bukan tulisan aneh. Itu",
                    "karakter pindah baris yang memang tersimpan di berkasnya. Makanya",
                    "strip() dipakai untuk membuangnya sebelum teksnya dipakai.",
                    "",
                    "Raw string: huruf r di depan tanda kutip",
                    "",
                    "  print(\"C:\\Users\\Andi\")     # RUSAK: \\U dikira awal escape unicode",
                    "  print(\"C:\\\\Users\\\\Andi\")   # benar, tapi berisik dibaca",
                    "  print(r\"C:\\Users\\Andi\")    # raw string: backslash apa adanya",
                    "",
                    "Huruf r sebelum tanda kutip itu disengaja, bukan salah ketik. Artinya:",
                    "di string ini backslash nggak punya arti khusus. Raw string r\"...\"",
                    "paling sering kamu temui di dua tempat: pola regex seperti r\"\\d+\", dan",
                    "path Windows. Panjang r\"a\\nb\" adalah 4, karena di situ \\ dan n memang",
                    "dua karakter terpisah.",
                ],
            },
            {
                "heading": "Fungsi print dengan banyak nilai, sep, dan end",
                "body": [
                    "print() bisa lebih banyak dari yang kamu lihat di materi pertama.",
                    "",
                    "Pertama, print() bisa menerima beberapa nilai sekaligus, dipisah koma:",
                    "",
                    "  print(\"Nama:\", nama, \"Umur:\", umur)",
                    "",
                    "Di antara tiap nilai otomatis disisipkan satu spasi, dan nilainya boleh",
                    "campur tipe apa aja. Bandingkan dengan menggabung pakai tanda +:",
                    "",
                    "  print(\"Umur: \" + umur)   # TypeError kalau umur bertipe int",
                    "  print(\"Umur:\", umur)     # aman, print() yang mengurus konversinya",
                    "",
                    "Kedua, sep. Ini pemisah antarnilai, dan bawaannya satu spasi:",
                    "",
                    "  print(\"a\", \"b\", \"c\")           # a b c",
                    "  print(\"a\", \"b\", \"c\", sep=\"-\")  # a-b-c",
                    "  print(\"a\", \"b\", \"c\", sep=\"\")   # abc",
                    "",
                    "Ketiga, end. Ini yang dicetak sesudah semua nilai. Bawaannya \"\\n\",",
                    "karakter pindah baris tadi. Makanya tiap print() otomatis pindah ke",
                    "baris baru.",
                    "",
                    "  print(\"Memuat\", end=\"\")   # kursor ditahan di baris yang sama",
                    "  print(\"...selesai\")       # tersambung jadi: Memuat...selesai",
                    "",
                    "print() yang kosong artinya nggak mencetak nilai apa pun, tapi end",
                    "tetap dijalankan. Hasilnya cuma pindah baris, alias satu baris kosong.",
                    "Trik ini dipakai di materi Perulangan: print(i, end=\" \") menjejerkan",
                    "angka di satu baris, lalu print() kosong sesudah loop menutup baris",
                    "itu. Kalau print() penutupnya lupa, keluaran berikutnya bakal nempel",
                    "di ujung baris tadi.",
                    "",
                    "sep= dan end= ditulis dalam bentuk nama=nilai waktu memanggil fungsi.",
                    "Bentuk ini namanya keyword argument. Urutannya bebas, dan kamu boleh",
                    "pakai salah satunya aja. Cara bikin fungsi sendiri yang bisa menerima",
                    "keyword argument dibahas di materi Function.",
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
                "heading": "Masukan input() dan cara import modul",
                "body": [
                    "Masukan: input()",
                    "",
                    "input() menghentikan program sebentar. Dia nunggu pengguna mengetik",
                    "lalu menekan Enter, kemudian program jalan lagi dengan teks yang tadi",
                    "diketik. Teks di dalam kurungnya disebut prompt. Prompt dicetak lebih",
                    "dulu tanpa pindah baris, supaya pengguna tahu apa yang diminta:",
                    "",
                    "  nama = input(\"Siapa namamu? \")",
                    "",
                    "Aturan terpenting di sini, dan sumber bug pertama hampir semua pemula:",
                    "input() selalu mengembalikan str, yaitu teks. Selalu, walaupun yang",
                    "diketik jelas-jelas angka.",
                    "",
                    "  umur = input(\"Umur: \")    # pengguna mengetik 20",
                    "  print(umur + 1)   # TypeError: can only concatenate str (not \"int\") to str",
                    "  print(umur * 2)   # \"2020\", bukan 40 - str dikali angka berarti diulang",
                    "  print(umur == 20) # False selamanya, karena \"20\" bukan 20",
                    "",
                    "Jadi ubah dulu ke angka. Caranya (casting) udah dibahas di materi",
                    "Variabel & Tipe Data:",
                    "",
                    "  umur = int(input(\"Umur: \"))            # str -> int",
                    "  tinggi = float(input(\"Tinggi (m): \"))  # str -> float",
                    "",
                    "Beberapa jebakan yang ikut muncul:",
                    "  - int(\"20.5\") menghasilkan ValueError. int() cuma mau bilangan bulat.",
                    "    Untuk angka berkoma, pakai float().",
                    "  - int(\"\") atau int(\"abc\") juga ValueError, dan programnya berhenti.",
                    "    Cara menanganinya dengan rapi ada di materi Exception Handling.",
                    "  - int(\" 20 \") hasilnya 20. Spasi di ujung dimaafkan, huruf nggak.",
                    "  - Enter yang ditekan pengguna nggak ikut terbawa. input() udah",
                    "    membuangnya.",
                    "",
                    "Cara menjalankan program yang pakai input() di aplikasi ini: tombol",
                    "Jalankan di blok kode nggak punya kotak masukan, jadi input() di sana",
                    "langsung berhenti dengan EOFError. Tekan tombol Ruang Coba di blok",
                    "kodenya, lalu isi kotak \"Masukan program (stdin)\". Tulis satu jawaban",
                    "per baris, urut sesuai urutan input() dipanggil. Kalau kotaknya",
                    "dikosongkan, program juga berhenti dengan EOFError karena nggak ada",
                    "yang bisa dibaca.",
                    "",
                    "Karena jawabannya datang dari kotak, bukan dari ketikan langsung, semua",
                    "prompt bakal kelihatan berderet di awal keluaran. Itu normal, bukan",
                    "bug.",
                    "",
                    "Modul bawaan: fungsi yang nggak otomatis tersedia",
                    "",
                    "print(), input(), int(), len(), dan type() selalu ada tanpa diminta.",
                    "Sisanya, misalnya akar kuadrat, angka acak, atau tanggal, tinggal di",
                    "dalam modul. Modul itu berkas berisi kumpulan fungsi, dan harus",
                    "di-import dulu sebelum dipakai. Modul bawaan udah ikut terpasang",
                    "bersama Python, jadi kamu nggak perlu mengunduh apa pun.",
                    "",
                    "  import math                 # dipakai: math.sqrt(16), math.pi",
                    "  from math import sqrt, pi   # dipakai: sqrt(16), pi   (tanpa \"math.\")",
                    "  import math as m            # alias; bentuk yang paling sering dilihat di",
                    "                              # kode nyata: import numpy as np",
                    "",
                    "Dua jebakannya:",
                    "  - Kalau kamu menulis import math lalu memanggil sqrt(16), hasilnya",
                    "    NameError. Nama yang dibuat baris itu cuma math, nggak ada sqrt.",
                    "  - Jangan menamai berkasmu sendiri math.py atau random.py. Python bakal",
                    "    nemu berkasmu lebih dulu, dan modul aslinya jadi nggak terjangkau.",
                    "",
                    "Modul bawaan lain, package, dan cara bikin modul sendiri dibahas lengkap",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program di loket pembayaran sekolah atau koperasi biasanya bekerja",
                    "begini: petugas mengetik angka, program menghitung, lalu mencetak",
                    "hasilnya. Bagian mengetik itu input(), bagian mencetak itu print().",
                    "Hitungan yang lebih rumit, seperti akar atau pembulatan ke bawah,",
                    "diambil dari modul bawaan math.",
                    "",
                    "Kasus kecil: petugas koperasi sekolah butuh program yang menanyakan",
                    "harga belanja dan uang yang dibayar, lalu mencetak kembaliannya.",
                    "Belanja 12500 yang dibayar 20000 harus menghasilkan Kembalian: 7500.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua angka yang diketik petugas, keluarannya satu baris.",
                    "  2. Ingat aturan nomor satu: input() selalu memberi str. Bungkus",
                    "     langsung dengan int() supaya bisa dikurangi:",
                    "      harga = int(input(\"Harga belanja: \"))",
                    "      bayar = int(input(\"Uang dibayar : \"))",
                    "      print(\"Kembalian:\", bayar - harga)",
                    "  3. Coba di Ruang Coba dengan kotak masukan berisi dua baris, 12500",
                    "     lalu 20000. Di ujung keluarannya muncul Kembalian: 7500.",
                    "  4. Cek kasus pinggir. Petugas yang terbiasa menulis 12.500 pakai",
                    "     titik ribuan bakal bikin int() berhenti dengan ValueError. Tulis",
                    "     di prompt bahwa angkanya diketik tanpa titik.",
                    "",
                    "Jebakan: tanpa int(), bayar - harga langsung kena TypeError, karena dua",
                    "str nggak bisa dikurangi.",
                ]
            },
        ],
    },
    {
        "title": "4. Operator",
        "sections": [
            {
                "body": [
                    "Operator itu tanda untuk mengolah nilai, misalnya menjumlah atau",
                    "membandingkan. Kita mulai dari operator aritmatika, yaitu yang dipakai",
                    "untuk berhitung:",
                    "",
                    "  +  penjumlahan     -  pengurangan",
                    "  *  perkalian       /  pembagian (selalu hasil float)",
                    "  // pembagian bulat (floor division, dibulatkan ke bawah)",
                    "  %  modulus (sisa bagi)",
                    "  ** pangkat",
                    "",
                    "Contohnya:",
                    "",
                    "  7 / 2   = 3.5   (pembagian biasa, hasil float)",
                    "  7 // 2  = 3     (floor division, hasil int jika kedua int)",
                    "  7 % 2   = 1     (sisa bagi)",
                    "  2 ** 3  = 8     (2 pangkat 3)",
                    "",
                    "Perhatikan bedanya / dan //. Tanda / selalu menghasilkan float,",
                    "walaupun hasilnya bulat. Tanda // membuang bagian desimalnya dengan",
                    "membulatkan ke bawah.",
                    "",
                    "Lalu ada operator penugasan (assignment). Bentuk x += 3 itu singkatan",
                    "dari x = x + 3, dan pola yang sama berlaku untuk operator lain:",
                    "",
                    "  =   x = 5     +=  x += 3     -=  x -= 3",
                    "  *=  x *= 3    /=  x /= 3     //= x //= 3",
                    "  **= x **= 2",
                    "",
                    "Ingat: Python nggak punya operator ++ dan --, yang di Java dan C",
                    "dipakai untuk menambah atau mengurangi satu. Untuk menambah satu, tulis",
                    "x += 1. Bentuk x++ nggak bisa dipakai.",
                ]
            },
            {
                "heading": "Operator perbandingan, logika, in, dan is",
                "body": [
                    "Operator perbandingan membandingkan dua nilai. Hasilnya selalu bool,",
                    "yaitu True atau False:",
                    "",
                    "  ==  sama dengan      !=  tidak sama",
                    "  >   lebih besar      <   lebih kecil",
                    "  >=  lebih besar sama <=  lebih kecil sama",
                    "",
                    "Operator logika dipakai untuk menggabungkan beberapa kondisi. Di Java",
                    "operator ini ditulis pakai simbol. Python pakai kata:",
                    "",
                    "  and  -> DAN (keduanya True baru True)",
                    "  or   -> ATAU (salah satu True jadi True)",
                    "  not  -> NEGASI",
                    "",
                    "  (5 > 3) and (2 > 1)   -> True",
                    "  (5 > 3) and (2 > 5)   -> False",
                    "  not (5 > 3)           -> False",
                    "",
                    "Terakhir, ada operator keanggotaan dan identitas. Operator ini khas",
                    "Python:",
                    "",
                    "  in      -> cek apakah ada di dalam koleksi",
                    "  not in  -> kebalikannya",
                    "  is      -> cek apakah referensi objek SAMA PERSIS",
                    "  is not  -> kebalikannya",
                    "",
                    "in mengecek apakah sebuah nilai ada di dalam kumpulan, misalnya list.",
                    "is mengecek apakah dua nama menunjuk ke objek yang persis sama di",
                    "memori. Dua list yang isinya sama tetap bisa jadi dua objek berbeda.",
                    "Contoh di bawah menunjukkan bedanya.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mesin kasir perlu memecah uang kembalian jadi beberapa lembar. Alatnya",
                    "cuma dua operator: // untuk jumlah lembar, dan % untuk sisa yang dibawa",
                    "ke pecahan berikutnya. Pola yang sama dipakai aplikasi absensi untuk",
                    "mengubah 135 menit lembur jadi 2 jam 15 menit.",
                    "",
                    "Kasus kecil: kasir harus menyerahkan kembalian Rp 37.000 dengan lembar",
                    "sesedikit mungkin, memakai pecahan 20.000, 10.000, 5.000, dan 2.000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu angka, 37000. Keluarannya jumlah lembar untuk tiap",
                    "     pecahan, mulai dari yang terbesar.",
                    "  2. Untuk satu pecahan, // memberi jumlah lembarnya, dan % memberi sisa",
                    "     uang yang belum diserahkan:",
                    "      sisa = 37000",
                    "      lembar_20rb = sisa // 20000",
                    "      sisa = sisa % 20000",
                    "      lembar_10rb = sisa // 10000",
                    "      sisa %= 10000",
                    "  3. Ulangi pasangan baris itu untuk 5.000 dan 2.000. Hasilnya satu",
                    "     lembar untuk tiap pecahan, dan sisa akhirnya 0.",
                    "  4. Cek kasus pinggir. Kembalian Rp 37.500 menyisakan 500 yang nggak",
                    "     bisa jadi lembar. Cetak sisa akhirnya, supaya kasir tahu masih",
                    "     harus menyiapkan koin.",
                    "",
                    "Jebakan: pakai //, jangan /. Hasil 17000 / 10000 adalah 1.7, dan itu",
                    "nggak bisa dipakai sebagai jumlah lembar.",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan (if / elif / else)",
        "sections": [
            {
                "body": [
                    "Percabangan bikin program bisa mengambil keputusan: kalau begini,",
                    "kerjakan itu. Python nggak pakai kurung kurawal { } untuk menandai",
                    "blok kode. Yang menentukan blok adalah indentasi, dan indentasinya",
                    "harus konsisten. Biasanya 4 spasi.",
                    "",
                    "Bentuk umumnya:",
                    "",
                    "  if kondisi:",
                    "      # jalankan jika kondisi True",
                    "  elif kondisi2:",
                    "      # jalankan jika kondisi2 True",
                    "  else:",
                    "      # jalankan jika semua False",
                    "",
                    "elif itu singkatan dari \"else if\". Python ngecek kondisinya dari atas",
                    "ke bawah, lalu menjalankan blok pertama yang kondisinya True.",
                    "",
                    "Ingat: setiap baris if, elif, dan else diakhiri titik dua (:). Sesudah",
                    "itu pindah baris, lalu isi bloknya ditulis menjorok.",
                    "",
                    "Aturan indentasi ini punya akibat langsung. Blok yang kosong sama",
                    "sekali dianggap salah, dan Python berhenti dengan IndentationError.",
                    "Padahal kadang kamu memang belum tahu mau nulis apa di situ. Untuk",
                    "itulah ada keyword pass. pass nggak mengerjakan apa pun. Tugasnya cuma",
                    "mengisi tempat supaya bloknya nggak kosong:",
                    "",
                    "  if saldo < 0:",
                    "      pass              # sengaja kosong, nanti baru diisi",
                    "  else:",
                    "      print(\"aman\")",
                    "",
                    "Tanda ... (tiga titik, namanya Ellipsis) juga bisa dipakai untuk",
                    "maksud yang sama, dan sama sahnya.",
                    "",
                    "pass juga nggak terbatas di if. pass berlaku di mana pun Python butuh blok",
                    "yang menjorok: for, while, def, class, dan except. Jadi kalau nanti",
                    "kamu ketemu class C(A, B): pass atau class SaldoTidakCukup(Exception):",
                    "pass, artinya tetap sama: badan bloknya sengaja dibiarkan kosong. pass",
                    "nggak punya arti khusus untuk class maupun exception.",
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
                "heading": "Fitur match-case dan nilai truthy falsy",
                "body": [
                    "Sebelum versi 3.10, Python nggak punya switch-case seperti bahasa lain.",
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
                    "Tanda '_' di case _ itu wildcard, artinya \"cocok dengan apa aja\". Ia",
                    "mirip 'default' di switch bahasa lain: dipakai kalau nggak ada case",
                    "lain yang cocok.",
                    "",
                    "Truthy dan falsy",
                    "",
                    "Di if, kamu nggak harus menulis perbandingan. Nilai apa pun bisa",
                    "dipakai sebagai kondisi. Nilai yang dianggap False disebut 'Falsy',",
                    "dan nilai yang dianggap True disebut 'Truthy'.",
                    "",
                    "  Falsy: 0, 0.0, \"\", [], {}, (), None, False",
                    "  Truthy: semua nilai selain di atas.",
                    "",
                    "Daftar falsy di atas itu yang paling sering kamu temui. Wadah kosong",
                    "lain, misalnya set() yang kosong, juga falsy. Gampangnya: angka nol,",
                    "wadah kosong, None, dan False dianggap False. Sisanya dianggap True.",
                    "",
                    "Karena itu, dua baris ini artinya sama:",
                    "",
                    "  if daftar:      # sama dengan: if len(daftar) > 0:",
                    "      print(\"Ada isinya\")",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir setiap aturan bisnis ditulis sebagai percabangan: gratis ongkir",
                    "kalau belanja sudah cukup, predikat rapor dari rentang nilai, atau",
                    "tarif parkir yang beda untuk motor dan mobil. Begitu aturannya punya",
                    "beberapa tingkat, urutan if dan elif ikut menentukan hasilnya.",
                    "",
                    "Kasus kecil: toko online memasang aturan ongkir. Belanja minimal",
                    "200.000 gratis ongkir, minimal 100.000 kena 10.000, dan di bawah itu",
                    "kena 20.000. Kamu diminta menghitung ongkir untuk belanja berapa pun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya total belanja, keluarannya satu angka ongkir.",
                    "  2. Python berhenti di cabang pertama yang True. Jadi tulis batas yang",
                    "     paling besar lebih dulu:",
                    "      if belanja >= 200000:",
                    "          ongkir = 0",
                    "      elif belanja >= 100000:",
                    "          ongkir = 10000",
                    "      else:",
                    "          ongkir = 20000",
                    "  3. Uji satu angka untuk tiap cabang: 250000 memberi 0, 150000 memberi",
                    "     10000, dan 50000 memberi 20000.",
                    "  4. Cek kasus pinggir tepat di batas. Belanja 100000 harus kena 10000,",
                    "     makanya tandanya >=. Kalau ditulis >, angka itu jatuh ke else.",
                    "",
                    "Jebakan: kalau urutannya dibalik dan belanja >= 100000 ditulis paling",
                    "atas, belanja 250000 ikut kena ongkir 10000.",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan (for & while)",
        "sections": [
            {
                "body": [
                    "Perulangan (loop) dipakai untuk menjalankan kode yang sama berkali-kali.",
                    "Python punya dua jenis.",
                    "",
                    "Yang pertama for. for mengulang kode untuk setiap elemen di dalam",
                    "sebuah iterable. Iterable itu apa pun yang isinya bisa diambil satu per",
                    "satu, misalnya list, string, atau range.",
                    "",
                    "  for item in iterable:",
                    "      # kode diulang",
                    "",
                    "Kalau kamu pernah lihat Java atau C, for di sana ditulis dengan tiga",
                    "bagian: (awal; kondisi; update). for di Python nggak pakai bentuk itu.",
                    "Dia langsung mengambil elemen satu per satu.",
                    "",
                    "Yang kedua while. while mengulang kode selama kondisinya masih True:",
                    "",
                    "  while kondisi:",
                    "      # kode",
                    "",
                    "for sering dipakai bareng range(). range() menghasilkan deretan angka:",
                    "",
                    "  range(5)        -> 0, 1, 2, 3, 4",
                    "  range(1, 6)     -> 1, 2, 3, 4, 5",
                    "  range(0, 10, 2) -> 0, 2, 4, 6, 8  (loncat 2)",
                    "",
                    "Perhatikan: angka terakhir nggak ikut. range(5) berhenti di 4, dan",
                    "range(1, 6) berhenti di 5.",
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
                "heading": "Comprehension, nested loop, dan nama _",
                "body": [
                    "List comprehension adalah cara ringkas bikin list dari sebuah loop.",
                    "Bentuk ini khas Python, dan dibahas lebih detail di materi tersendiri:",
                    "",
                    "  kuadrat = [x**2 for x in range(1, 6)]",
                    "  print(kuadrat)   # [1, 4, 9, 16, 25]",
                    "",
                    "Nested loop artinya loop di dalam loop. Biasanya dipakai untuk bikin",
                    "pola atau tabel:",
                    "",
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
                    "Nama _ untuk nilai yang nggak dipakai",
                    "",
                    "  for _ in range(3):",
                    "      print(\"halo\")         # nomor putarannya tidak terpakai",
                    "  _, nilai = (\"Andi\", 85)   # namanya diabaikan, ambil nilainya saja",
                    "",
                    "_ itu variabel biasa. Python nggak memperlakukannya secara khusus. Yang",
                    "khusus cuma kesepakatan antarpembaca kode. Artinya: \"isi variabel ini",
                    "memang nggak bakal dipakai, nggak usah dicari di mana dipakainya\".",
                    "Menulis for i in range(3) juga tetap jalan. _ cuma bikin niatmu",
                    "langsung kebaca.",
                    "",
                    "Ada tiga hal mirip yang gampang ketukar, padahal artinya beda:",
                    "",
                    "  for _ in ...  -> nilai buangan, yang barusan dibahas",
                    "  case _:       -> wildcard di match-case (materi Percabangan),",
                    "                   artinya 'cocok dengan apa saja'",
                    "  _nama         -> konvensi 'protected' untuk atribut, dibahas di",
                    "                   materi OOP: Encapsulation & Dunder Methods",
                    "",
                    "Konvensi itu kebiasaan yang disepakati programmer, bukan aturan yang",
                    "dipaksa Python.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi tabungan dan cicilan sering menjawab pertanyaan \"berapa kali",
                    "lagi sampai target?\". Jumlah putarannya belum diketahui di awal, jadi",
                    "yang dipakai while. Kalau jumlahnya sudah pasti, misalnya mencetak",
                    "jadwal cicilan 12 bulan, for dengan range() lebih cocok.",
                    "",
                    "Kasus kecil: Sinta menabung Rp 75.000 tiap minggu, dan butuh Rp 600.000",
                    "untuk biaya karyawisata. Berapa minggu yang dia perlukan?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya setoran per minggu dan target. Keluarannya jumlah",
                    "     minggu.",
                    "  2. Jumlah putaran justru yang dicari, jadi pakai while dengan dua",
                    "     variabel penghitung:",
                    "      tabungan, minggu = 0, 0",
                    "      while tabungan < 600000:",
                    "          tabungan += 75000",
                    "          minggu += 1",
                    "      print(minggu, tabungan)",
                    "  3. Jalankan. Hasilnya 8 minggu, dengan tabungan tepat 600000.",
                    "  4. Cek kasus pinggir: target tercapai persis. Dengan <=, loop jalan",
                    "     sekali lagi dan menjawab 9 minggu. Tandanya harus <.",
                    "",
                    "Jebakan: kalau baris tabungan += 75000 lupa ditulis, kondisinya selalu",
                    "True dan loop nggak pernah berhenti.",
                ]
            },
        ],
    },
    {
        "title": "7. Angka, Perbandingan & Operator yang Belum Dibahas",
        "sections": [
            {
                "body": [
                    "Materi Operator tadi mendaftar operator aritmatika, perbandingan, dan",
                    "logika, lalu berhenti. Materi ini melengkapi sisanya: hal-hal yang",
                    "sering muncul di kode nyata tapi belum pernah disebut. Kita mulai dari",
                    "angkanya dulu.",
                    "",
                    "int, si bilangan bulat, di Python nggak punya batas. 2 ** 100 dihitung",
                    "utuh sampai digit terakhir. Nggak ada overflow, yaitu angka yang",
                    "\"meluap\" karena kebesaran, seperti int 32-bit di Java dan C.",
                    "",
                    "float, si bilangan desimal, beda cerita. float punya batas, dan",
                    "hasilnya nggak selalu tepat:",
                    "",
                    "    0.1 + 0.2    menghasilkan    0.30000000000000004",
                    "",
                    "Ini bukan bug Python. Hampir semua bahasa pemrograman begini juga.",
                    "Komputer menyimpan pecahan dalam basis dua. Masalahnya, 0,1 dalam basis",
                    "dua adalah pecahan berulang yang nggak pernah selesai. Mirip 1/3 yang",
                    "jadi 0,3333... dan nggak pernah habis ditulis dalam basis sepuluh.",
                    "",
                    "Jadi yang tersimpan di memori adalah angka terdekat yang muat, bukan",
                    "0,1 persis. Selisihnya kecil sekali, tapi ikut menumpuk tiap kali",
                    "angkanya dijumlahkan.",
                    "",
                    "Dari situ ada satu aturan tegas: jangan membandingkan dua float pakai",
                    "==. Ekspresi 0.1 + 0.2 == 0.3 hasilnya False. Kode seperti itu nggak",
                    "error dan nggak berhenti. Dia cuma masuk ke cabang if yang salah, dan",
                    "kamu nggak dikasih tahu apa-apa. Ini perlu kamu tahu dari sekarang,",
                    "karena banyak latihan menghitung rata-rata, dan hasil pembagian /",
                    "selalu float.",
                    "",
                    "Alat yang benar untuk urusan ini:",
                    "",
                    "  math.isclose(a, b)   True kalau selisihnya bisa diabaikan; ini",
                    "                       cara yang dipakai orang",
                    "  abs(a - b) < 1e-9    versi manualnya; abs() = nilai mutlak,",
                    "                       yaitu membuang tanda minus",
                    "  round(x, 2)          bulatkan ke 2 desimal (hasilnya tetap float)",
                    "  divmod(a, b)         (a // b, a % b) sekaligus, satu panggilan",
                    "",
                    "Tiga jebakan yang sering kena:",
                    "",
                    "  - round(0.5) = 0 dan round(2.5) = 2. Kalau nilainya tepat di tengah,",
                    "    Python membulatkan ke angka genap terdekat. Tujuannya supaya",
                    "    pembulatan yang diulang-ulang nggak selalu condong naik. Ini beda",
                    "    dari pelajaran sekolah, dan beda juga dari Java.",
                    "  - Jangan pakai round() untuk menampilkan angka. Pakai f\"{x:.2f}\",",
                    "    yang dibahas di materi String & Formatting. Soalnya round(85.0, 2)",
                    "    tetap tercetak 85.0, bukan 85.00 seperti yang kamu mau.",
                    "  - math.isclose(x, 0) hampir selalu False. Toleransinya relatif,",
                    "    artinya diukur dari besar angkanya, dan nol nggak punya besar.",
                    "    Kalau dibandingkan dengan nol, wajib pakai abs_tol:",
                    "      math.isclose(x, 0, abs_tol=1e-9)",
                    "",
                    "Untuk hitungan yang nggak boleh meleset sedikit pun, seperti uang,",
                    "pajak, atau tagihan, jangan pakai float sama sekali. Pakai salah satu",
                    "dari dua ini:",
                    "",
                    "  decimal.Decimal      berhitung dalam basis SEPULUH, persis",
                    "                       seperti hitungan tangan di atas kertas",
                    "  fractions.Fraction   menyimpan pembilang & penyebut, jadi 1/3",
                    "                       tetap tepat 1/3",
                    "",
                    "Aturan wajib untuk Decimal: selalu bikin dari string. Decimal(\"0.1\")",
                    "nilainya tepat 0,1. Sebaliknya, Decimal(0.1) menerima float yang udah",
                    "meleset sebelum sempat masuk.",
                    "",
                    "quantize() dipakai untuk menentukan berapa angka di belakang koma.",
                    "ROUND_HALF_UP adalah pembulatan ala sekolah: yang tepat setengah",
                    "dibulatkan naik. Ini sengaja beda dari round() bawaan tadi.",
                    "",
                    "Jadi kalau nanti kamu lihat Decimal(\"10.50\") di kode orang, itu bukan",
                    "gaya-gayaan. Penulisnya nggak mau kehilangan satu sen gara-gara",
                    "pembulatan yang nggak kelihatan.",
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
                "heading": "Operator bitwise, rantai perbandingan, dan walrus",
                "body": [
                    "Ada tiga kelompok operator lagi yang belum dibahas, padahal ketiganya",
                    "sering kamu temui.",
                    "",
                    "Operator bitwise",
                    "",
                    "Operator bitwise bekerja pada bit, yaitu angka 0 dan 1 yang menyusun",
                    "sebuah bilangan bulat di dalam komputer:",
                    "",
                    "  a & b    AND   bit yang 1 di KEDUANYA          6 & 3   = 2",
                    "  a | b    OR    bit yang 1 di salah satunya     6 | 3   = 7",
                    "  a ^ b    XOR   bit yang BERBEDA                6 ^ 3   = 5",
                    "  ~a       NOT   balik semua bitnya              ~5      = -6",
                    "  a << n   geser kiri n bit  = a * 2**n          1 << 3  = 8",
                    "  a >> n   geser kanan n bit = a // 2**n         40 >> 2 = 10",
                    "",
                    "Operator ini juga punya versi penugasan: |= &= ^= <<= >>=. Polanya",
                    "sama dengan += di materi Operator.",
                    "",
                    "Pemakaian yang paling sering adalah bit flag. Idenya: menyimpan banyak",
                    "saklar ya/nggak di dalam satu angka. Tiap izin dikasih satu bit",
                    "sendiri (1, 2, 4, 8, 16). Lalu | dipakai untuk menyalakan, & untuk",
                    "memeriksa, dan &= ~ untuk mematikan. Cara ini yang dipakai di balik",
                    "chmod 755, dan di balik tulisan seperti re.IGNORECASE | re.MULTILINE",
                    "yang bakal kamu temui di banyak library.",
                    "",
                    "Simbol | & ^ nanti muncul lagi di materi Dictionary & Set dengan arti",
                    "lain, yaitu untuk menggabungkan set dan dict. Itu belum perlu dipahami",
                    "sekarang. Cukup ingat bahwa simbolnya sama, tapi artinya bisa beda. Yang",
                    "menentukan artinya adalah tipe nilai di kiri dan kanannya (operand):",
                    "",
                    "  3 | 4           ->  7       int  : gabungkan bit",
                    "  True | False    ->  True    bool : hasilnya tetap bool",
                    "",
                    "Jadi waktu kamu membaca izin | TULIS di kode, ingat bahwa yang digabung",
                    "di situ bitnya.",
                    "",
                    "Perbandingan berantai",
                    "",
                    "Di Python, 0 < nilai <= 100 itu sah. Artinya dua perbandingan",
                    "sekaligus, digabung pakai and:",
                    "",
                    "  0 < nilai <= 100     sama dengan    (0 < nilai) and (nilai <= 100)",
                    "",
                    "Di bahasa lain belum tentu begitu. Di C, 0 < nilai dihitung lebih dulu",
                    "jadi 1 (artinya benar), lalu angka 1 itu yang dibandingkan dengan 100.",
                    "Hasilnya hampir selalu benar, apa pun isi nilai. Di Java, bentuk ini",
                    "malah ditolak compiler.",
                    "",
                    "Di Python, bagian tengahnya cuma dihitung satu kali. Jadi",
                    "f(x) < g(y) < h(z) nggak memanggil g() dua kali. Bentuk ini dipakai di",
                    "solusi Latihan 11, dan bakal sering kamu lihat di kode orang.",
                    "",
                    "Operator walrus :=",
                    "",
                    "Operator walrus := ada sejak Python 3.8. Dia menyimpan nilai ke",
                    "variabel, sekaligus menghasilkan nilai itu. Namanya diambil dari",
                    "bentuknya yang mirip mata dan gading walrus. Jangan sampai ketukar",
                    "dengan dua tanda yang mirip:",
                    "",
                    "  =    penugasan, sebuah pernyataan; tidak boleh masuk ke if/while",
                    "  ==   perbandingan, menghasilkan bool",
                    "  :=   penugasan yang JUGA menghasilkan nilainya, boleh di ekspresi",
                    "",
                    "Gunanya untuk menghilangkan pengulangan. Tanpa :=, len(daftar) harus",
                    "dipanggil dua kali, atau ditulis di baris sendiri di atas if, walaupun",
                    "hasilnya cuma dipakai di dalam if itu. Bentuk yang paling sering kamu",
                    "temui adalah membaca berulang sampai habis:",
                    "",
                    "  while (baris := f.readline()):     (berkas dibahas di materi File I/O)",
                    "",
                    "Jebakannya:",
                    "",
                    "  - Urutan pengerjaan (presedensi). if n := len(x) > 5 dibaca sebagai",
                    "    n := (len(x) > 5). Jadi n berisi True, bukan panjangnya. Kurungnya",
                    "    wajib ditulis:",
                    "      if (n := len(x)) > 5:",
                    "  - := nggak bisa berdiri sendiri sebagai satu baris pernyataan. Untuk",
                    "    itu pakai = biasa.",
                    "  - Pola sentinel di contoh pakai 'is not None', nggak cuma mengandalkan",
                    "    nilainya dianggap benar atau salah. Sentinel itu nilai penanda",
                    "    \"datanya udah habis\", di sini None. Kalau kamu cuma mengandalkan",
                    "    truthy/falsy (materi Percabangan), angka 0 bakal menghentikan loop,",
                    "    padahal 0 itu data yang sah.",
                    "  - Jangan pakai := cuma karena bisa. Kalau nilainya cuma dipakai",
                    "    sekali, = biasa di baris atasnya lebih enak dibaca.",
                    "",
                    ":= juga boleh dipakai di dalam list comprehension. Contohnya ada nanti",
                    "di materi List Comprehension & Generator Expression.",
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
print(True | False)           # True : bool, hasilnya tetap bool
# Untuk set dan dict, | punya arti lain lagi (nanti di materi Dictionary & Set)""",
            },
            {
                "heading": "Perbandingan berantai & operator walrus",
                "code": """nilai = 85
print(0 < nilai <= 100)              # True
print(0 < nilai and nilai <= 100)    # True, arti yang sama persis

daftar = [3, 1, 4, 1, 5, 9, 2, 6]
print(0 < len(daftar) < 10)          # True, dan len() cuma dipanggil sekali

if (n := len(daftar)) > 5:
    print(f"daftar panjang: {n} elemen")   # n masih bisa dipakai di sini

# JEBAKAN presedensi: tanpa kurung, := menangkap hasil PERBANDINGANNYA
if n := len(daftar) > 5:
    print(n)                         # True, bukan 8

# Pola sentinel, kembaran dari  while (baris := f.readline()):
# iter() dan next() baru dibahas di materi Iterator & Generator. Untuk
# sekarang cukup tahu: next(sisa, None) mengambil isi berikutnya, atau None
# kalau isinya sudah habis.
sisa = iter([3, 0, 7])
while (x := next(sisa, None)) is not None:
    print("dapat", x)                # 3, lalu 0, lalu 7""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir, bank, dan pembukuan UMKM nggak menyimpan uang sebagai",
                    "float. Yang dipakai Decimal atau bilangan bulat, karena selisih kecil",
                    "dari float ikut menumpuk di laporan bulanan. Aturan pembulatannya juga",
                    "ditulis jelas, karena round() bawaan membulatkan nilai tengah ke angka",
                    "genap.",
                    "",
                    "Kasus kecil: struk kafe menulis subtotal Rp 12.950 dan pajak 11%.",
                    "Pajaknya Rp 1.424,50, dan pemilik kafe mau dibulatkan ala sekolah:",
                    "setengah ke atas, jadi Rp 1.425.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya subtotal dan tarif, keluarannya pajak dalam rupiah",
                    "     bulat.",
                    "  2. Ini uang, jadi pakai Decimal yang dibuat dari string, termasuk",
                    "     tarifnya:",
                    "      from decimal import Decimal, ROUND_HALF_UP",
                    "      pajak = Decimal(\"12950\") * Decimal(\"0.11\")",
                    "      print(pajak)",
                    "      print(pajak.quantize(Decimal(\"1\"), rounding=ROUND_HALF_UP))",
                    "  3. Jalankan. Baris pertama 1424.50, baris kedua 1425.",
                    "  4. Cek kasus pinggir yang jadi alasan soal ini, yaitu nilai yang tepat",
                    "     di tengah. round(Decimal(\"1424.50\")) memberi 1424, karena round()",
                    "     membulatkan ke angka genap terdekat.",
                    "",
                    "Jebakan: Decimal(0.11) tanpa tanda kutip membawa ekor float yang",
                    "meleset, dan pajaknya ikut meleset.",
                ]
            },
        ],
    },
    {
        "title": "8. String & Formatting",
        "sections": [
            {
                "body": [
                    "String itu teks. Di Python, string bisa ditulis pakai kutip tunggal",
                    "'...' atau kutip ganda \"...\". Hasilnya sama aja.",
                    "",
                    "String bersifat immutable, artinya nggak bisa diubah sesudah dibuat.",
                    "Kalau kamu \"mengubah\" string, yang terjadi adalah Python bikin string",
                    "baru.",
                    "",
                    "Untuk string yang panjangnya beberapa baris, pakai kutip tiga:",
                    "",
                    "  teks = \"\"\"Baris pertama",
                    "  Baris kedua\"\"\"",
                    "",
                    "String itu deretan karakter, jadi kamu bisa mengambil karakter",
                    "tertentu lewat posisinya. Mengambil satu karakter disebut indexing,",
                    "dan mengambil potongan disebut slicing. Caranya mirip list:",
                    "",
                    "  s = \"Python\"",
                    "  s[0]      -> 'P'   (indeks dari 0)",
                    "  s[-1]     -> 'n'   (indeks negatif = dari belakang)",
                    "  s[0:3]    -> 'Pyt' (slicing: mulai:akhir, akhir TIDAK termasuk)",
                    "  s[2:]     -> 'thon'",
                    "",
                    "Perhatikan: posisi pertama itu 0, bukan 1. Dan di slicing, posisi",
                    "akhirnya nggak ikut diambil.",
                    "",
                    "Slicing punya tiga bagian: [mulai:akhir:langkah]. Langkah artinya",
                    "berapa karakter dilompati tiap kali. Bawaannya 1.",
                    "",
                    "  s[::2]    -> 'Pto'    (dari awal ke akhir, ambil satu lewati satu)",
                    "  s[1::2]   -> 'yhn'    (sama, tapi mulai dari indeks 1)",
                    "  s[::-1]   -> 'nohtyP' (langkah -1 = berjalan MUNDUR, sehingga",
                    "                         hasilnya string terbalik)",
                    "  s[::-2]   -> 'nhy'    (mundur sambil melompat dua)",
                    "",
                    "Jadi s[::-1] nggak perlu dihafal sebagai rumus khusus. Itu cuma",
                    "akibat aturan langkah tadi: langkah -1 artinya jalan mundur.",
                    "",
                    "Ketiga bagiannya boleh dikosongkan. Bagian yang kosong artinya \"dari",
                    "paling awal\", \"sampai paling akhir\", dan \"langkah 1\". Makanya s[:]",
                    "artinya seluruh isi string.",
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
                "heading": "Beda find() dan index() saat teks tak ketemu",
                "body": [
                    "find() dan index() sama-sama mencari posisi sebuah teks. Bedanya ada",
                    "di sikapnya kalau teksnya nggak ketemu. find() memberi -1, sedangkan",
                    "index() melempar ValueError dan programnya berhenti.",
                    "",
                    "Pakai find() kalau \"nggak ketemu\" itu hal wajar yang mau kamu periksa",
                    "sendiri. Pakai index() kalau \"nggak ketemu\" berarti ada yang salah, dan",
                    "program memang sebaiknya berhenti.",
                    "",
                    "Jebakan: find() punya dua jebakan. Pertama, hasilnya harus",
                    "dibandingkan dengan -1 secara jelas. Tulis if teks.find(x) != -1.",
                    "Kalau cuma if teks.find(x), hasilnya salah: posisi 0 (ketemu di awal)",
                    "dianggap falsy dan terbaca \"nggak ada\", sedangkan -1 dianggap truthy",
                    "dan terbaca \"ada\". Kedua, -1 itu indeks yang sah di Python. Jadi",
                    "teks[teks.find(x)] yang nggak diperiksa dulu bakal memberi karakter",
                    "terakhir, tanpa error apa pun.",
                    "",
                    "Method di dua contoh tadi belum semuanya, dan nggak perlu dihafal.",
                    "Yang perlu kamu ingat: bentuknya selalu sama, yaitu teks.sesuatu(...).",
                    "Semuanya mengembalikan string baru dan nggak pernah mengubah string",
                    "aslinya, karena string itu immutable.",
                ]
            },
            {
                "body": [
                    "Dua operator aritmatika juga bisa dipakai untuk string:",
                    "",
                    "  \"-\" * 40      -> garis pemisah sepanjang 40 karakter",
                    "  \"*\" * 3       -> '***'",
                    "  \"Ha\" + \"lo\"   -> 'Halo'   (+ MENYAMBUNG, bukan menjumlahkan)",
                    "",
                    "Tanda * mengulang string, dan tanda + menyambung string.",
                    "",
                    "Di materi Masukan, Keluaran & Modul Bawaan, perkalian string muncul",
                    "sebagai jebakan: \"20\" * 2 memberi \"2020\", bukan 40. Di sini kita",
                    "pakai dengan sengaja. Garis pemisah di layar dan pola segitiga bintang",
                    "hampir selalu dibikin begini:",
                    "",
                    "  for i in range(1, 5):",
                    "      print(\"*\" * i)",
                    "",
                    "Dua baris itu menggantikan loop bersarang di materi Perulangan.",
                    "",
                    "Ingat: kedua sisinya harus bertipe cocok. \"umur: \" + 20 langsung",
                    "TypeError. Tulis \"umur: \" + str(20), atau yang lebih enak dibaca,",
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
                "heading": "Format {nilai=}, .format(), dan operator %",
                "body": [
                    "Bentuk {nilai=} dipakai untuk mengintip isi variabel waktu kamu nyari",
                    "bug. Dia mencetak nama variabelnya sekalian, jadi kamu nggak perlu",
                    "nulis print(\"ipk:\", ipk) lagi.",
                    "",
                    "Sisanya dipakai untuk merapikan tabel dan laporan: :, untuk pemisah",
                    "ribuan, :.1% untuk persen, dan :^ untuk rata tengah. Semuanya",
                    "melanjutkan :.2f, :>10, dan :<10 di contoh sebelumnya.",
                    "",
                    "Dua baris berlabel \"cara lama\" di contoh f-string pertama juga perlu",
                    "bisa kamu baca, karena kode lama penuh dengan keduanya:",
                    "",
                    "  \"Nama: {}, Umur: {}\".format(nama, umur)",
                    "",
                    "Tiap {} yang kosong diisi argumen .format() secara berurutan. {}",
                    "pertama menerima argumen pertama, dan seterusnya. Kamu juga boleh",
                    "pakai nomor seperti {0} {1}, atau nama seperti {n} lalu",
                    ".format(n=nama).",
                    "",
                    "  \"Nama: %s, Umur: %d\" % (nama, umur)",
                    "",
                    "Di sini % itu operator untuk mengisi pola, bukan modulus dari materi",
                    "Operator. Sisi kirinya string berpola. Sisi kanannya tuple berisi",
                    "nilai yang mengisi pola itu berurutan:",
                    "  - %s untuk apa aja (diubah jadi string)",
                    "  - %d untuk bilangan bulat",
                    "  - %f untuk desimal",
                    "  - %.2f untuk dua desimal",
                    "",
                    "Kalau nilainya cuma satu, tuple-nya boleh dilepas: \"Halo %s\" % nama.",
                    "",
                    "Untuk kode baru, pakai f-string. Dua bentuk lama tadi cukup kamu kenali",
                    "waktu membaca kode orang, karena keduanya masih banyak dipakai.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Struk belanja, laporan rekap, dan label harga di rak semuanya teks yang",
                    "dirapikan: kolom nama rata kiri, kolom harga rata kanan, dan angka",
                    "ribuan diberi pemisah. Semua itu dikerjakan f-string. Nama dari",
                    "formulir pendaftaran juga hampir selalu lewat strip() dan title() dulu",
                    "sebelum disimpan.",
                    "",
                    "Kasus kecil: kamu diminta mencetak baris struk \"Kopi susu\" seharga",
                    "18000. Kolom nama selebar 12 karakter rata kiri, kolom harga selebar 10",
                    "karakter rata kanan, dan harganya memakai titik ribuan: 18.000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Keluarannya satu baris selebar 22 karakter. Nama di kiri, harga",
                    "     menempel di tepi kanan.",
                    "  2. f\"{harga:,}\" memberi 18,000 dengan koma, gaya Inggris. Ganti",
                    "     komanya jadi titik dulu, baru ratakan:",
                    "      nama, harga = \"Kopi susu\", 18000",
                    "      teks_harga = f\"{harga:,}\".replace(\",\", \".\")",
                    "      print(f\"{nama:<12}{teks_harga:>10}\")",
                    "  3. Jalankan. Nama diisi spasi sampai 12 karakter, lalu 18.000 rata",
                    "     kanan di 10 karakter berikutnya.",
                    "  4. Cek kasus pinggir: nama yang lebih dari 12 huruf, misalnya \"Teh",
                    "     tarik gula aren\". f-string nggak memotongnya, jadi kolom harga ikut",
                    "     bergeser. Potong dulu dengan nama[:12].",
                    "",
                    "Jebakan: replace() dijalankan pada teks harga saja. Kalau dijalankan",
                    "pada seluruh baris, koma di nama barang ikut berubah jadi titik.",
                ]
            },
        ],
    },
    {
        "title": "9. List & Tuple",
        "sections": [
            {
                "body": [
                    "List itu kumpulan data yang berurutan. Isinya bisa diubah (mutable),",
                    "boleh campur tipe data, dan ukurannya bisa bertambah atau berkurang",
                    "sesuka kamu.",
                    "",
                    "  angka = [10, 20, 30, 40]",
                    "  campur = [1, \"dua\", 3.0, True]",
                    "",
                    "Operasi yang paling sering dipakai pada list:",
                    "",
                    "  angka.append(50)      -> tambah di akhir",
                    "  angka.insert(0, 5)    -> sisipkan di indeks tertentu",
                    "  angka.remove(20)      -> hapus berdasarkan NILAI",
                    "  angka.pop()           -> hapus & kembalikan elemen terakhir",
                    "  angka.pop(0)          -> hapus berdasarkan INDEKS",
                    "  len(angka)            -> jumlah elemen",
                    "  angka.sort()          -> urutkan (mengubah list asli)",
                    "  sorted(angka)         -> urutkan (list BARU, asli tak berubah)",
                    "  angka.reverse()       -> balik urutan",
                    "",
                    "Perhatikan dua pasangan yang mirip. remove() menghapus berdasarkan",
                    "nilainya, sedangkan pop() berdasarkan posisinya. angka.sort() mengubah",
                    "list aslinya, sedangkan sorted(angka) bikin list baru dan list aslinya",
                    "dibiarkan.",
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
                    "Tuple itu mirip list, tapi isinya nggak bisa diubah (immutable).",
                    "Tuple dipakai untuk data yang memang nggak boleh berubah, misalnya",
                    "koordinat.",
                    "",
                    "  titik = (10, 20)",
                    "  titik[0] = 99    # ERROR! tuple tidak bisa diubah",
                    "",
                    "  x, y = titik     # unpacking: x=10, y=20",
                    "",
                    "Baris terakhir itu namanya unpacking: isi tuple dibongkar dan dibagi ke",
                    "beberapa variabel sekaligus.",
                    "",
                    "Kenapa pakai tuple, padahal udah ada list?",
                    "  1. Sedikit lebih cepat dan lebih hemat memori daripada list.",
                    "  2. Tuple bisa dipakai sebagai key di dictionary. List nggak bisa.",
                    "  3. Tuple jadi semacam janji bahwa data ini nggak boleh berubah. Kalau",
                    "     ada kode yang mencoba mengubahnya, Python langsung menolak.",
                    "",
                    "Beberapa fungsi bawaan yang berguna untuk list dan tuple:",
                    "",
                    "  len(x), sum(x), max(x), min(x), sorted(x)",
                    "  list(range(5))  -> [0, 1, 2, 3, 4]",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Daftar nilai satu kelas, isi keranjang belanja, dan antrean pesanan di",
                    "dapur restoran semuanya list: urutannya penting dan isinya bisa",
                    "bertambah. Data yang nggak boleh berubah, seperti koordinat lokasi toko",
                    "(lintang, bujur), biasanya disimpan sebagai tuple.",
                    "",
                    "Kasus kecil: guru memakai aturan remedial. Nilai ulangan terendah",
                    "dibuang, lalu sisanya dirata-rata. Nilai Andi [78, 92, 65, 88, 70].",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya list nilai, keluarannya satu angka rata-rata dengan dua",
                    "     desimal.",
                    "  2. List aslinya masih dipakai untuk rapor, jadi jangan diubah. Pakai",
                    "     sorted(), yang membuat list baru, lalu buang elemen pertamanya:",
                    "      nilai = [78, 92, 65, 88, 70]",
                    "      tanpa_terendah = sorted(nilai)[1:]",
                    "      rata = sum(tanpa_terendah) / len(tanpa_terendah)",
                    "      print(f\"{rata:.2f}\")",
                    "  3. Jalankan. Yang tersisa [70, 78, 88, 92], dan hasilnya 82.00.",
                    "  4. Cek kasus pinggir: siswa yang cuma punya satu nilai. Sesudah",
                    "     dibuang, list-nya kosong, dan pembagian dengan len() yang 0 berakhir",
                    "     ZeroDivisionError. Periksa dulu dengan if len(nilai) > 1.",
                    "",
                    "Jebakan: nilai.sort() mengubah list aslinya. Urutan ulangan pertama,",
                    "kedua, dan seterusnya hilang, padahal rapor masih membutuhkannya.",
                ]
            },
        ],
    },
    {
        "title": "10. Fungsi Bawaan untuk Koleksi",
        "sections": [
            {
                "body": [
                    "Materi List & Tuple ditutup dengan daftar \"fungsi bawaan yang",
                    "berguna\": len, sum, max, min, sorted. Daftar itu benar, tapi belum",
                    "lengkap. Fungsi di materi ini muncul di hampir setiap kode Python",
                    "nyata. Kalau belum kenal, kamu bakal tersandung tiap kali membaca kode",
                    "orang lain.",
                    "",
                    "Semua fungsi ini bekerja pada iterable apa pun. Iterable itu apa pun",
                    "yang isinya bisa diambil satu per satu: list, tuple, string, set,",
                    "dict, range. Jadi nggak cuma list. Makanya jumlah fungsinya sedikit",
                    "tapi jangkauannya luas: satu fungsi bisa dipakai untuk semua jenis",
                    "koleksi.",
                    "",
                    "Fungsinya terbagi tiga kelompok, dan bedanya perlu kamu perhatikan:",
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
                    "Kelompok ketiga paling sering bikin pemula bingung:",
                    "",
                    "  print(zip(a, b))        -> <zip object at 0x7f3c9a1b2d40>",
                    "  print(list(zip(a, b)))  -> [('Andi', 85), ('Budi', 70)]",
                    "",
                    "Iterator itu seperti antrean yang cuma bisa dibaca sekali jalan. Dia",
                    "bukan wadah yang menyimpan isinya. Dia juga belum menghitung apa pun",
                    "sampai isinya diminta. Untuk melihat isinya, bungkus pakai list().",
                    "Kalau cuma mau dipakai di for-loop, nggak perlu dibungkus. Detailnya",
                    "dibahas lengkap di materi Iterator & Generator.",
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
                "heading": "Hasil zip terpotong dan iterator sekali pakai",
                "body": [
                    "zip berhenti di koleksi yang paling pendek, dan nggak ngasih tahu.",
                    "Nggak ada error, nggak ada peringatan, sisanya hilang begitu aja.",
                    "Kalau kedua koleksi seharusnya sama panjang, bug seperti ini susah",
                    "dilacak karena nggak meninggalkan jejak.",
                    "  - Python 3.10 ke atas punya zip(a, b, strict=True). Bentuk ini",
                    "    melempar ValueError kalau panjangnya beda. Di Python yang lebih",
                    "    lama, argumen strict itu malah bikin error.",
                    "  - Cara yang aman di versi mana pun: periksa len(a) == len(b) dulu.",
                    "",
                    "zip() dan enumerate() mengembalikan iterator, dan isinya habis",
                    "sesudah sekali dipakai. Jebakan ini sering banget bikin orang bingung:",
                    "",
                    "  z = zip(nama, nilai)",
                    "  print(list(z))   -> [('Andi', 85), ('Budi', 70), ('Citra', 95)]",
                    "  print(list(z))   -> []      <- kosong, dan TIDAK ada error",
                    "",
                    "Kalau ada dua for-loop atas objek zip yang sama, loop kedua nggak",
                    "jalan sama sekali. Kalau isinya perlu dipakai ulang, simpan dulu jadi",
                    "list: pasangan = list(zip(...))",
                    "",
                    "Tanda * pada zip(*matriks) membongkar list berisi list jadi beberapa",
                    "argumen terpisah. Jadi zip(*[[1, 2, 3], [4, 5, 6]]) sama persis dengan",
                    "zip([1, 2, 3], [4, 5, 6]). Hasilnya deretan tuple, bukan list. Kalau",
                    "kamu butuh list, pakai [list(k) for k in zip(*matriks)]. Tanda * ini",
                    "dibahas lengkap di materi Membongkar Argumen & Parameter Khusus.",
                    "",
                    "Pada enumerate(daftar, start=1), start cuma menggeser nomor yang",
                    "dicetak. Elemen pertama tetap ikut. Jadi start bukan cara untuk",
                    "melewati elemen.",
                    "",
                    "Pakai enumerate, jangan for i in range(len(daftar)). Cara kedua itu",
                    "memaksa kamu menulis daftar[i] di setiap baris, dan gampang meleset",
                    "satu langkah.",
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
                "heading": "Jebakan any, all, sort, dan reversed",
                "body": [
                    "any() dan all() langsung berhenti begitu jawabannya udah pasti. Sifat",
                    "ini namanya short-circuit. Karena itu, isi kurungnya lebih baik",
                    "generator (kurung biasa), bukan list comprehension (kurung siku):",
                    "",
                    "  any(x < 0 for x in data)     -> berhenti di elemen minus PERTAMA",
                    "  any([x < 0 for x in data])   -> seluruh list dibangun dulu",
                    "",
                    "Keduanya cuma mengembalikan True atau False, bukan elemennya.",
                    "",
                    "Jebakan: all() atas koleksi kosong hasilnya True. Logikanya, \"nggak",
                    "ada satu pun yang melanggar\". Akibatnya, validasi pakai all(...) atas",
                    "daftar yang ternyata kosong bakal lolos tanpa memeriksa apa pun. Kalau",
                    "daftar kosong itu nggak boleh, periksa daftarnya sendiri dulu.",
                    "",
                    "daftar.sort() mengubah list aslinya dan mengembalikan None:",
                    "",
                    "  daftar = daftar.sort()   -> daftar kini None, dan errornya baru",
                    "                              muncul beberapa baris kemudian.",
                    "",
                    "Yang memberi list baru itu sorted(daftar). sorted() juga stabil:",
                    "elemen dengan key yang sama tetap di urutan aslinya. Sifat ini yang",
                    "bikin pengurutan dua tingkat bisa dikerjakan dengan dua kali sorted().",
                    "",
                    "reversed() butuh koleksi yang berurutan: list, tuple, str, atau range.",
                    "reversed({1, 2, 3}) hasilnya TypeError, karena set memang nggak",
                    "berurutan. Ada tiga cara membalik yang hasilnya beda:",
                    "  - daftar[::-1] memberi list baru.",
                    "  - reversed(daftar) memberi iterator.",
                    "  - daftar.reverse() mengubah list aslinya.",
                    "",
                    "Pakai isinstance(x, T), jangan type(x) == T. isinstance mengakui class",
                    "turunan, sedangkan type() menolaknya. Bedanya baru kerasa sesudah",
                    "materi OOP: Inheritance & Polymorphism, tapi kebiasaannya lebih baik",
                    "dibentuk dari sekarang.",
                    "",
                    "repr() otomatis dipakai di dalam list, tuple, dict, dan waktu",
                    "debugging. Makanya print(['a']) menampilkan tanda kutip, padahal",
                    "print('a') nggak. Di f-string, {teks!r} memaksa bentuk repr. Cara",
                    "menentukan sendiri bentuk str dan repr sebuah objek ada di materi OOP:",
                    "Encapsulation & Dunder Methods.",
                    "",
                    "id() itu nomor identitas sebuah objek selama objek itu masih ada. Nomor",
                    "ini yang dibandingkan operator is (materi Operator). Nilainya ganti",
                    "tiap program dijalankan, jadi jangan disimpan. Gunanya cuma untuk",
                    "menjawab: \"ini objek yang sama, atau cuma kembarannya?\"",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data dari spreadsheet sering datang sebagai kolom terpisah: satu list",
                    "nama, satu list nilai. zip() menyandingkan keduanya, sorted() membuat",
                    "peringkat, dan enumerate() memberi nomor urut. Validasi formulir juga",
                    "sering ditulis dengan all(), misalnya untuk memastikan semua isian",
                    "wajib terisi.",
                    "",
                    "Kasus kecil: wali kelas punya dua kolom, nama [\"Andi\", \"Budi\", \"Citra\",",
                    "\"Dewi\"] dan nilai [85, 70, 95, 88]. Dia minta tiga besar beserta nomor",
                    "peringkatnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua list sejajar. Keluarannya tiga baris, misalnya",
                    "     \"1. Citra 95\".",
                    "  2. Pasangkan dengan zip(), taruh nilai di depan supaya tuple-nya",
                    "     diurutkan menurut nilai, lalu urutkan dari yang terbesar:",
                    "      nama = [\"Andi\", \"Budi\", \"Citra\", \"Dewi\"]",
                    "      nilai = [85, 70, 95, 88]",
                    "      urut = sorted(zip(nilai, nama), reverse=True)",
                    "      for i, (v, n) in enumerate(urut[:3], start=1):",
                    "          print(f\"{i}. {n} {v}\")",
                    "  3. Jalankan. Hasilnya Citra 95, Dewi 88, lalu Andi 85.",
                    "  4. Cek kasus pinggir: kolom yang panjangnya beda. zip() berhenti di",
                    "     list terpendek tanpa memberi tahu, jadi siswa terakhir bisa hilang",
                    "     dari peringkat. Bandingkan len(nama) dan len(nilai) dulu.",
                    "",
                    "Ingat: kalau dua nilai sama, tuple dibandingkan lewat elemen keduanya,",
                    "yaitu nama. Dengan reverse=True, nama yang abjadnya belakangan muncul",
                    "lebih dulu.",
                ]
            },
        ],
    },
    {
        "title": "11. Dictionary & Set",
        "sections": [
            {
                "body": [
                    "Dictionary (dict) itu kumpulan pasangan key dan value. Key itu kunci",
                    "untuk mencari, value itu isinya. Mirip kamus: kamu cari kata (key),",
                    "lalu dapat artinya (value). Kalau kamu kenal Java, dict mirip HashMap.",
                    "",
                    "Key harus unik dan immutable, misalnya str, int, atau tuple. Sejak",
                    "Python 3.7, urutan pasangan di dict selalu sama dengan urutan waktu",
                    "dimasukkan.",
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
                    "",
                    "Bedanya mahasiswa[\"kota\"] dan mahasiswa.get(\"kota\", \"-\"): yang pertama",
                    "berhenti dengan KeyError kalau key-nya nggak ada. Yang kedua memberi",
                    "nilai cadangan \"-\" dan programnya jalan terus.",
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
                    "Set itu kumpulan data yang unik, artinya nggak boleh ada yang dobel.",
                    "Isinya juga nggak berurutan. Mirip HashSet di Java. Set cocok untuk",
                    "membuang data dobel, dan untuk operasi himpunan seperti union",
                    "(gabungan) dan intersection (irisan).",
                    "",
                    "  angka = {1, 2, 2, 3, 3, 3}",
                    "  print(angka)   # {1, 2, 3}  (duplikat otomatis hilang)",
                    "",
                    "  angka.add(4)          -> tambah elemen",
                    "  angka.remove(1)       -> hapus elemen (error jika tak ada)",
                    "  angka.discard(99)     -> hapus jika ada, aman jika tak ada",
                    "",
                    "remove() dan discard() sama-sama menghapus. Bedanya, remove() bikin",
                    "error kalau elemennya nggak ada, sedangkan discard() diam aja.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mesin kasir menyimpan daftar harga sebagai dict: kode atau nama barang",
                    "jadi key, harganya jadi value. Mencari harga satu barang di antara",
                    "ribuan barang tetap cepat. Set dipakai untuk pertanyaan seperti \"siapa",
                    "saja yang hadir di dua hari pelatihan?\" atau \"barang mana yang nggak",
                    "terdaftar?\".",
                    "",
                    "Kasus kecil: daftar harga warung {\"beras\": 13500, \"gula\": 17000,",
                    "\"minyak\": 18000}. Keranjang pelanggan berisi [\"beras\", \"gula\", \"beras\",",
                    "\"kopi\"]. Hitung totalnya, dan laporkan barang yang belum punya harga.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dict harga dan list belanja. Keluarannya total dan",
                    "     himpunan barang yang nggak dikenal.",
                    "  2. Ambil harga dengan get() supaya barang asing nggak bikin KeyError,",
                    "     lalu cari barang asing dengan selisih set:",
                    "      total = 0",
                    "      for barang in keranjang:",
                    "          total += daftar_harga.get(barang, 0)",
                    "      tak_dikenal = set(keranjang) - set(daftar_harga)",
                    "      print(total, tak_dikenal)",
                    "  3. Jalankan. Totalnya 44000, dan barang yang nggak dikenal {'kopi'}.",
                    "     set(daftar_harga) berisi key-nya saja.",
                    "  4. Cek kasus pinggir: beras dibeli dua kali. Loop menjumlahkan setiap",
                    "     kemunculan, sedangkan set cuma dipakai untuk mencari yang asing.",
                    "",
                    "Jebakan: get(barang, 0) membuat kopi seolah gratis. Makanya daftar",
                    "barang asing wajib ditampilkan ke kasir sebelum struk dicetak.",
                ]
            },
        ],
    },
    {
        "title": "12. Wadah Data Siap Pakai (module collections)",
        "sections": [
            {
                "body": [
                    "Module collections isinya wadah data siap pakai. Gampangnya, ini dict dan",
                    "list yang udah disetel untuk pola yang paling sering ditulis orang. Module",
                    "ini bagian dari Python sendiri, alias stdlib (pustaka standar yang ikut",
                    "terpasang bareng Python). Jadi nggak perlu pip install apa pun, cukup satu",
                    "baris import:",
                    "",
                    "  from collections import defaultdict, Counter, namedtuple, deque",
                    "",
                    "Isinya ada empat:",
                    "",
                    "  defaultdict  dict yang membuatkan nilai awal saat key-nya belum ada",
                    "  Counter      dict khusus menghitung: berapa kali tiap nilai muncul",
                    "  namedtuple   tuple yang tiap posisinya punya NAMA",
                    "  deque        list yang cepat ditambah/dikurangi di KEDUA ujungnya",
                    "",
                    "Mungkin kamu belum bakal memakainya sendiri dalam waktu dekat. Tapi",
                    "keempatnya sering muncul di kode orang lain, dan biasanya justru untuk",
                    "menggantikan pola dict dan list dari materi Dictionary & Set. Contohnya",
                    "baris ini:",
                    "",
                    "      per_orang[nama].append(barang)",
                    "",
                    "Nggak ada pengecekan key sama sekali, jadi kelihatannya pasti kena",
                    "KeyError. Ternyata kodenya benar, soalnya per_orang bukan dict biasa. Kalau",
                    "kamu nggak tahu wadah ini ada, kamu bisa buang waktu sesorean",
                    "\"membetulkan\" kode yang nggak rusak.",
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
                "heading": "Jebakan defaultdict, Counter, dan deque",
                "body": [
                    "Ada beberapa jebakan yang perlu kamu tahu:",
                    "",
                    "  1. defaultdict bertambah isinya walaupun cuma dibaca. Misalnya kamu salah",
                    "     ketik key sekali, d[\"nma\"]. Dict biasa langsung kena KeyError, jadi",
                    "     kamu tahu persis barisnya. defaultdict malah mengembalikan [] tanpa",
                    "     protes, dan salahnya baru kerasa jauh di belakang. Kalau cuma mau",
                    "     ngintip isinya, pakai .get(key) seperti di dict biasa.",
                    "  2. Yang dikasih ke defaultdict adalah nama fungsinya, bukan hasil",
                    "     memanggil fungsi itu:",
                    "     defaultdict(list)  benar,  defaultdict(list())  -> TypeError.",
                    "  3. Counter(\"halo dunia\") menghitung huruf. Kalau mau menghitung kata,",
                    "     kasih dia list: Counter(kalimat.split()). Dua-duanya jalan tanpa",
                    "     error, jadi kalau salah pilih, nggak ada yang ngasih tahu.",
                    "  4. Counter[key] untuk key yang nggak ada nilainya 0, dan key-nya nggak",
                    "     ikut ditambahkan. Ini kebalikan defaultdict. Dua wadahnya mirip, tapi",
                    "     perilakunya berlawanan.",
                    "  5. namedtuple tetap immutable, artinya isinya nggak bisa diubah:",
                    "     p.derajat = 9 -> AttributeError. _replace() memberi salinan baru.",
                    "     Kalau hasilnya lupa disimpan ke variabel, kamu bakal bingung kenapa",
                    "     datanya nggak berubah padahal rasanya \"udah diganti\".",
                    "  6. deque nggak bisa di-slice: d[1:3] -> TypeError. Mengakses bagian",
                    "     tengahnya (d[500]) juga lambat. Cepatnya cuma di dua ujung.",
                    "  7. maxlen membuang data yang paling tua tanpa pemberitahuan apa pun.",
                    "     Gunanya memang itu, tapi jangan dipakai untuk data yang nggak boleh",
                    "     hilang.",
                    "",
                    "Kapan dict atau list biasa udah cukup:",
                    "  - Isinya sedikit dan key-nya udah pasti, misalnya konfigurasi atau satu",
                    "    baris data.",
                    "  - Kamu justru pengin dapat KeyError kalau key-nya salah. Error itu",
                    "    berguna sebagai penjaga.",
                    "  - Kamu cuma sesekali menyisipkan di depan. list.insert(0, x) baru kerasa",
                    "    lambat kalau datanya ribuan.",
                    "",
                    "Kapan namedtuple cukup, dan kapan udah waktunya pakai class:",
                    "  - Cukup: objeknya cuma menyimpan data, nggak punya perilaku, dan wajar",
                    "    diperlakukan sebagai tuple. Contohnya satu baris hasil query atau satu",
                    "    titik koordinat.",
                    "  - Udah waktunya class: kamu butuh method sendiri, butuh field yang bisa",
                    "    diubah, atau butuh pemeriksaan nilai waktu objeknya dibuat. Class",
                    "    dibahas di materi OOP nanti. Di antara keduanya ada dataclass, yang",
                    "    juga dibahas nanti.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir kafe memakai Counter untuk mencari menu terlaris hari",
                    "ini, defaultdict(list) untuk mengelompokkan pesanan per meja, dan deque",
                    "untuk antrean pesanan yang diambil dari depan. Ketiganya menggantikan",
                    "pola dict dan list yang biasanya ditulis tangan berulang kali.",
                    "",
                    "Kasus kecil: catatan penjualan kafe hari ini berbentuk list [\"kopi\",",
                    "\"teh\", \"kopi\", \"roti\", \"kopi\", \"teh\"]. Pemilik ingin tahu dua menu yang",
                    "paling laku beserta jumlahnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya list nama menu, satu elemen per porsi. Keluarannya dua",
                    "     baris, menu dan jumlahnya.",
                    "  2. Menghitung kemunculan adalah pekerjaan Counter, dan most_common(n)",
                    "     langsung mengurutkannya:",
                    "      from collections import Counter",
                    "      terjual = [\"kopi\", \"teh\", \"kopi\", \"roti\", \"kopi\", \"teh\"]",
                    "      hitung = Counter(terjual)",
                    "      for menu, jumlah in hitung.most_common(2):",
                    "          print(menu, jumlah)",
                    "  3. Jalankan. Hasilnya kopi 3, lalu teh 2.",
                    "  4. Cek kasus pinggir: catatan yang datang sebagai satu teks panjang,",
                    "     \"kopi teh kopi\". Counter atas string menghitung huruf, jadi pecah",
                    "     dulu dengan split().",
                    "",
                    "Ingat: menu yang nggak pernah dipesan memberi hitung[\"es jeruk\"] = 0,",
                    "tanpa KeyError.",
                ]
            },
        ],
    },
    {
        "title": "13. Function (Fungsi)",
        "sections": [
            {
                "body": [
                    "Function, atau fungsi, adalah blok kode yang dikasih nama supaya bisa",
                    "dipanggil berulang kali. Fungsi dibuat pakai keyword def. Keyword itu kata",
                    "yang punya arti khusus buat Python, jadi nggak boleh dipakai sebagai nama",
                    "variabel.",
                    "",
                    "Kamu juga nggak perlu menulis tipe nilai yang dikembalikan fungsi. Di Java",
                    "atau C, tipe itu wajib ditulis. Di Python nggak.",
                    "",
                    "Bentuk umumnya begini:",
                    "",
                    "  def nama_fungsi(parameter):",
                    "      # isi fungsi",
                    "      return nilai   # opsional, jika tak ada return -> None",
                    "",
                    "return itu opsional. Fungsi yang nggak punya return tetap mengembalikan",
                    "sesuatu, yaitu None. Dua contoh fungsi:",
                    "",
                    "  def sapa(nama):",
                    "      print(f\"Halo, {nama}\")",
                    "",
                    "  def tambah(a, b):",
                    "      return a + b",
                    "",
                    "Cara memanggilnya:",
                    "",
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
                "heading": "Scope, docstring, dan type hint",
                "body": [
                    "Scope variabel",
                    "",
                    "Scope artinya wilayah tempat sebuah variabel dikenal. Variabel yang dibuat",
                    "di dalam fungsi sifatnya lokal: cuma dikenal di dalam fungsi itu.",
                    "",
                    "Kalau kamu mau mengubah variabel global (yang dibuat di luar semua fungsi)",
                    "dari dalam fungsi, pakai keyword global. Cara ini jarang dipakai, dan",
                    "sebaiknya dihindari kalau bisa:",
                    "",
                    "  total = 0",
                    "  def tambah_total(n):",
                    "      global total",
                    "      total += n",
                    "",
                    "Docstring",
                    "",
                    "Docstring adalah teks dokumentasi fungsi. Tulis di baris pertama isi",
                    "fungsi, diapit tiga tanda kutip. help() bakal menampilkannya:",
                    "",
                    "  def tambah(a, b):",
                    "      \"\"\"Mengembalikan hasil penjumlahan a dan b.\"\"\"",
                    "      return a + b",
                    "  help(tambah)   # menampilkan docstring",
                    "",
                    "Type hint",
                    "",
                    "Type hint adalah keterangan tipe yang kamu tulis sendiri di parameter dan",
                    "nilai kembalian. Sifatnya opsional, ada sejak Python 3.5, dan gunanya",
                    "supaya kode lebih jelas dan IDE (aplikasi untuk menulis kode) bisa",
                    "membantu lebih banyak:",
                    "",
                    "  def tambah(a: int, b: int) -> int:",
                    "      return a + b",
                    "",
                    "Python tetap dynamically typed, artinya tipe variabel baru ditentukan",
                    "waktu program jalan. Type hint cuma petunjuk. Python nggak memaksanya",
                    "waktu program dijalankan, beda dengan Java atau C++.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rumus yang dipakai di banyak tempat, seperti harga sesudah diskon atau",
                    "ongkir per kilo, dibungkus jadi fungsi. Toko online memakai rumus yang",
                    "sama di halaman produk, keranjang, dan struk. Kalau aturannya berubah,",
                    "cukup satu fungsi yang disunting, bukan tiga salinan rumus.",
                    "",
                    "Kasus kecil: harga Rp 50.000 kena diskon 20%, dan harga Rp 30.000",
                    "nggak kena diskon. Kamu butuh total keduanya, dan rumus diskonnya akan",
                    "dipakai lagi di halaman lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya harga dan persen diskon, keluarannya harga akhir. Diskon",
                    "     sering kosong, jadi beri nilai default 0.",
                    "  2. Tulis rumusnya sekali di dalam def, dan kembalikan hasilnya dengan",
                    "     return supaya bisa dijumlahkan:",
                    "      def harga_akhir(harga, diskon=0):",
                    "          \"\"\"Harga sesudah dipotong diskon persen.\"\"\"",
                    "          return harga - harga * diskon // 100",
                    "      total = harga_akhir(50000, 20) + harga_akhir(30000)",
                    "      print(total)",
                    "  3. Jalankan. 40000 ditambah 30000, hasilnya 70000.",
                    "  4. Cek kasus pinggir: diskon 100 harus memberi 0, dan tanpa diskon",
                    "     harus memberi harga utuh. Panggil harga_akhir(50000, 100) dan",
                    "     harga_akhir(50000) untuk memastikannya.",
                    "",
                    "Jebakan: kalau fungsinya cuma print() tanpa return, nilainya None, dan",
                    "penjumlahan di atas berhenti dengan TypeError.",
                ]
            },
        ],
    },
    {
        "title": "14. Referensi Objek, Salinan & Jebakan Mutable",
        "sections": [
            {
                "body": [
                    "Di Python, variabel itu lebih mirip label daripada kotak. Label itu",
                    "ditempel ke sebuah objek di memori. Yang punya isi adalah objeknya,",
                    "sedangkan namanya cuma penunjuk ke sana. Satu objek boleh punya banyak",
                    "nama sekaligus.",
                    "",
                    "Akibatnya, baris yang kelihatan paling polos ternyata nggak menyalin apa",
                    "pun:",
                    "",
                    "  a = [1, 2, 3]",
                    "  b = a          # BUKAN salinan - b cuma label KEDUA untuk objek yang sama",
                    "  b.append(4)",
                    "  print(a)       # [1, 2, 3, 4]   <- a ikut berubah",
                    "",
                    "Ini bukan kelakuan aneh khusus list. Semua tipe di Python bekerja begini.",
                    "Kelihatan atau nggaknya cuma ditentukan satu hal: objek itu bisa diubah di",
                    "tempat atau nggak.",
                    "",
                    "  Mutable   (bisa diubah di tempat) : list, dict, set, objek class buatanmu",
                    "  Immutable (tidak bisa diubah)     : int, float, str, bool, tuple, None",
                    "",
                    "Mutable artinya isinya bisa diubah langsung. Immutable artinya nggak bisa.",
                    "Pada objek immutable, \"mengubah\" selalu berarti bikin objek baru, lalu",
                    "labelnya dipindah ke objek baru itu. Kamu udah lihat ini di materi String",
                    "(str itu immutable) dan materi List & Tuple (soal tuple).",
                    "",
                    "Objek lamanya nggak pernah tersentuh, jadi nama lain yang masih menunjuk",
                    "ke sana tetap aman. Makanya jebakan ini seolah cuma kena list dan dict.",
                    "Padahal aturannya sama untuk semua tipe.",
                    "",
                    "Ada tiga alat untuk mengintip identitas objek. Kamu udah kenal dari materi",
                    "Operator:",
                    "  a is b     -> True kalau keduanya objek yang SAMA PERSIS, bukan sekadar",
                    "                isinya mirip",
                    "  a == b     -> cuma menanyakan ISInya sama",
                    "  id(a)      -> nomor identitas objek. Angkanya berbeda tiap kali program",
                    "                dijalankan, jadi yang berguna adalah MEMBANDINGKANnya",
                    "                (id(a) == id(b)), bukan membaca angkanya satu per satu.",
                    "",
                    "Catatan: jangan pakai is untuk membandingkan angka atau string. Python",
                    "kadang memakai ulang objek kecil yang sama. Jadi hasilnya bisa kebetulan",
                    "True, lalu jadi False waktu datanya lebih besar, tanpa peringatan apa pun.",
                    "Untuk membandingkan isi, pakai ==.",
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
                "heading": "Membuat salinan: [:], copy, dan deepcopy",
                "body": [
                    "Kalau kamu memang mau objek baru, mintalah terang-terangan. Ada beberapa",
                    "bentuk yang sering muncul di kode orang, dan semuanya mengerjakan hal yang",
                    "sama:",
                    "",
                    "  baru = lama[:]        # slicing penuh; gaya lama, masih sangat umum",
                    "  baru = list(lama)     # membangun list baru dari isinya",
                    "  baru = lama.copy()    # sejak Python 3.3; paling gampang dibaca",
                    "  baru = dict(cfg)      # untuk dict (ada juga cfg.copy())",
                    "  baru = set(s)         # untuk set",
                    "",
                    "Kalau suatu saat kamu ketemu baris seperti itu dan rasanya mubazir, jangan",
                    "dihapus. Baris itulah yang menjaga supaya kode nggak mengubah data milik",
                    "orang lain.",
                    "",
                    "Tapi semua cara di atas cuma bikin salinan dangkal (shallow copy). Yang",
                    "dibuat baru cuma wadah paling luarnya. Isinya tetap objek yang itu-itu",
                    "juga:",
                    "",
                    "  asli  = [[1, 2], [3, 4]]",
                    "  salin = asli[:]",
                    "  salin[0].append(99)",
                    "  print(asli)      # [[1, 2, 99], [3, 4]]   <- tembus sampai ke asli",
                    "",
                    "Untuk list satu lapis yang isinya angka atau string, salinan dangkal udah",
                    "cukup. Isinya immutable, jadi nggak ada yang bisa diubah dari dalam.",
                    "",
                    "Untuk struktur bersarang, pakai salinan dalam (deep copy). Salinan ini",
                    "menyalin sampai ke lapisan paling dasar:",
                    "",
                    "  import copy",
                    "  aman = copy.deepcopy(konfigurasi)",
                    "",
                    "Kapan deepcopy dibutuhkan? Kalau strukturnya bersarang (dict berisi list,",
                    "list berisi dict, atau state aplikasi), dan kamu memang bakal mengubah isi",
                    "dalamnya. Untuk data satu lapis, deepcopy cuma bikin lambat tanpa menambah",
                    "keamanan. Di struktur besar, biayanya kerasa, soalnya dia menelusuri",
                    "seluruh isi.",
                    "",
                    "Ada juga yang kelihatannya menyalin padahal nggak:",
                    "  b = a            -> label kedua untuk objek yang sama",
                    "  fungsi(a)        -> parameter di dalam fungsi juga cuma label kedua",
                    "  [[0] * 3] * 3    -> tiga nama untuk SATU baris yang sama",
                    "",
                    "[0] * 3 sendiri aman, karena 0 nggak bisa diubah. Yang bahaya adalah",
                    "mengulang list. Tanda * menggandakan referensinya (penunjuknya), bukan",
                    "isinya.",
                    "",
                    "Aturan yang sama bikin dua jebakan di fungsi. Contohnya ada di blok kode",
                    "terakhir:",
                    "",
                    "  1. Kalau kamu mengoper list atau dict ke fungsi, fungsi itu bisa mengubah",
                    "     data milik pemanggilnya. Kalau yang dioper int, str, atau tuple,",
                    "     fungsi nggak punya cara mengubahnya. Paling jauh dia cuma memindah",
                    "     labelnya sendiri di dalam fungsi.",
                    "",
                    "     Jadi putuskan dari awal. Fungsimu mengubah data di tempat (biasanya",
                    "     mengembalikan None, seperti list.sort()), atau mengembalikan objek",
                    "     baru (seperti sorted()). Yang bikin bingung adalah fungsi yang",
                    "     mengerjakan dua-duanya tanpa bilang.",
                    "  2. Nilai default sebuah parameter dibuat sekali aja, waktu baris def",
                    "     dijalankan, bukan tiap kali fungsinya dipanggil. Jadi def f(x=[])",
                    "     memakai satu list yang sama untuk semua panggilan, dan isinya",
                    "     menumpuk. Pola yang benar memakai None sebagai tanda \"nggak diisi\":",
                    "       def f(x=None):",
                    "           if x is None:",
                    "               x = []",
                    "     Untuk default yang immutable (0, \"\", None, True), nggak ada masalah.",
                    "     Nggak ada yang bisa menumpuk di sana.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi sekolah sering menyimpan template, misalnya jadwal piket",
                    "bawaan, lalu membuat jadwal tiap kelas dari template itu. Kalau",
                    "template cuma diberi nama kedua, perubahan di satu kelas ikut muncul di",
                    "template dan di kelas lain. Bug seperti ini baru ketahuan waktu ada",
                    "guru yang protes namanya muncul di kelas yang salah.",
                    "",
                    "Kasus kecil: template {\"Senin\": [\"Andi\"], \"Selasa\": [\"Budi\"]} dipakai",
                    "untuk kelas B, lalu Citra ditambahkan ke piket Senin kelas B. Template",
                    "aslinya harus tetap berisi Andi saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali bentuk datanya: dict yang berisi list. Ada dua lapis wadah",
                    "     yang bisa diubah.",
                    "  2. dict(template) atau template.copy() cuma salinan dangkal. List di",
                    "     dalamnya masih dipakai bersama, jadi append tetap tembus.",
                    "  3. Pakai salinan dalam supaya list-nya ikut disalin:",
                    "      import copy",
                    "      template = {\"Senin\": [\"Andi\"], \"Selasa\": [\"Budi\"]}",
                    "      kelas_b = copy.deepcopy(template)",
                    "      kelas_b[\"Senin\"].append(\"Citra\")",
                    "      print(template[\"Senin\"], kelas_b[\"Senin\"])",
                    "  4. Periksa hasilnya. Yang tercetak ['Andi'] dan ['Andi', 'Citra'],",
                    "     jadi template aman. Bisa juga dicek dengan kelas_b[\"Senin\"] is",
                    "     template[\"Senin\"], yang harus False.",
                    "",
                    "Jebakan: kelas_b = template sama sekali nggak menyalin. Itu cuma label",
                    "kedua untuk dict yang sama.",
                ]
            },
        ],
    },
    {
        "title": "15. Rekursi",
        "sections": [
            {
                "body": [
                    "Rekursi artinya fungsi yang memanggil dirinya sendiri. Kedengarannya",
                    "seperti trik, padahal aturannya biasa aja. Begitu sebuah nama didaftarkan",
                    "lewat def, isi fungsinya boleh menyebut nama apa pun yang dikenal waktu",
                    "fungsi itu dipanggil. Termasuk namanya sendiri.",
                    "",
                    "Rekursi ada karena sebagian data bentuknya bersarang dan kedalamannya",
                    "nggak tetap. Misalnya folder di dalam folder, JSON di dalam JSON, atau",
                    "balasan komentar di dalam balasan komentar. For bertingkat nggak cukup",
                    "untuk data seperti ini. Kamu harus tahu dulu butuh berapa tingkat, dan",
                    "justru itu yang nggak kamu tahu. Rekursi memakai bentuk datanya sendiri",
                    "sebagai aturan.",
                    "",
                    "Setiap fungsi rekursif wajib punya dua bagian:",
                    "  - Base case: kondisi berhenti. Di sini fungsinya langsung menjawab,",
                    "    tanpa memanggil dirinya lagi.",
                    "  - Recursive case: fungsinya memanggil dirinya sendiri untuk masalah",
                    "    yang lebih kecil.",
                    "",
                    "Punya base case aja belum cukup. Tiap panggilan juga harus bergerak",
                    "mendekati base case itu. faktorial(n - 1) makin dekat ke 1, sedangkan",
                    "faktorial(n) nggak pindah ke mana-mana.",
                    "",
                    "Kalau base case lupa ditulis, atau ada tapi nggak pernah tercapai,",
                    "hasilnya begini:",
                    "",
                    "  def hitung_mundur(n):",
                    "      print(n)",
                    "      hitung_mundur(n - 1)   # tak berhenti: 3, 2, 1, 0, -1, -2, ...",
                    "",
                    "  hitung_mundur(3)",
                    "  # RecursionError: maximum recursion depth exceeded",
                    "",
                    "Bedanya dengan while True: programnya nggak menggantung selamanya. Yang",
                    "muncul adalah error. Alasannya dijelaskan di bagian batas rekursi di",
                    "bawah.",
                    "",
                    "Ada satu istilah yang bakal sering kamu temui: tumpukan panggilan (call",
                    "stack). Panggilan yang belum selesai nggak hilang. Dia menunggu, lengkap",
                    "dengan variabel lokalnya, sampai panggilan di dalamnya mengembalikan",
                    "nilai. Contoh berikut bikin tumpukan itu kelihatan.",
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
                "heading": "RecursionError dan kapan loop lebih baik",
                "body": [
                    "Python membatasi seberapa dalam rekursi boleh menumpuk:",
                    "",
                    "  import sys",
                    "  print(sys.getrecursionlimit())   # 1000 di hampir semua Python",
                    "",
                    "Kalau lewat dari itu, program berhenti dengan:",
                    "",
                    "  RecursionError: maximum recursion depth exceeded",
                    "",
                    "Traceback-nya (laporan error dari Python) panjang banget, dan memuat",
                    "baris seperti '[Previous line repeated 996 more times]'. Justru baris itu",
                    "petunjuk paling berguna. Fungsi yang namanya diulang-ulang di situ adalah",
                    "fungsi yang nggak pernah sampai ke base case-nya.",
                    "",
                    "Batas itu ada untuk melindungi programmu. Tiap panggilan yang belum",
                    "selesai memakai tempat di tumpukan milik proses. Tanpa batas, tumpukannya",
                    "habis dan prosesnya mati tanpa pesan apa pun (segmentation fault).",
                    "Penyebabnya jauh lebih susah dicari daripada exception yang menyebut nama",
                    "fungsi dan nomor barisnya.",
                    "",
                    "Batasnya memang bisa dinaikkan, tapi itu jarang jadi jawaban yang benar:",
                    "",
                    "  import sys",
                    "  sys.setrecursionlimit(20000)",
                    "",
                    "Yang naik cuma penghitung milik Python. Ukuran stack asli dari sistem",
                    "operasi nggak ikut naik. Jadi RecursionError yang masih ngasih tahu",
                    "penyebabnya bisa berubah jadi crash tanpa pesan sama sekali. Kalau kamu",
                    "tergoda memakainya, penyebabnya hampir selalu salah satu dari dua ini:",
                    "  - Base case-nya nggak pernah tercapai. Itu bug, dan menaikkan batas",
                    "    cuma bikin bug-nya ketahuan lebih lambat.",
                    "  - Datanya memang panjang, dan yang keliru adalah memilih rekursi untuk",
                    "    data seperti itu.",
                    "",
                    "Kapan loop lebih baik daripada rekursi:",
                    "  - Kalau kedalamannya sebanding dengan jumlah data. Misalnya",
                    "    menjumlahkan sejuta baris, atau faktorial 5000. Loop nggak punya",
                    "    batas kedalaman dan lebih cepat.",
                    "  - Kalau bentuknya lurus: satu panggilan cuma melahirkan tepat satu",
                    "    panggilan lagi. Itu cuma perulangan biasa, dan lebih jelas ditulis",
                    "    sebagai for.",
                    "  - Python nggak punya tail-call optimization seperti sebagian bahasa",
                    "    lain. Itu fitur yang membuat panggilan di baris terakhir nggak",
                    "    menambah tumpukan. Jadi di Python, return f(x) di baris terakhir pun",
                    "    tetap menumpuk.",
                    "",
                    "Rekursi unggul kalau datanya sendiri bercabang dan kedalamannya nggak",
                    "diketahui: pohon, JSON bersarang, folder, atau penguraian ekspresi. Di",
                    "data seperti itu kedalamannya biasanya cuma belasan sampai puluhan",
                    "tingkat, jauh di bawah 1000. Kodenya juga jauh lebih pendek daripada",
                    "versi loop yang harus mengurus tumpukannya sendiri.",
                ],
            },
            {
                "heading": "Kenapa fibonacci rekursif lambat, dan apa yang ditolong cache",
                "code": """# Materi Decorator nanti memakai fibonacci ber-@lru_cache sambil menyebut
# "tanpa cache SANGAT lambat". Ini alasannya, dalam angka - jalankan sendiri
# dan perhatikan penghitung panggilannya.

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
# terjadi ratusan kali. Obatnya cache: dict yang menyimpan hasil per argumen,
# sehingga tiap n dihitung TEPAT sekali.
cache = {}

def fib_cepat(n):
    if n in cache:                     # sudah pernah dihitung? ambil saja
        return cache[n]
    hasil = n if n < 2 else fib_cepat(n - 1) + fib_cepat(n - 2)
    cache[n] = hasil                   # simpan untuk panggilan berikutnya
    return hasil

print("fib_cepat(25) =", fib_cepat(25), "dengan", len(cache), "hasil di cache")
# fib_cepat(25) = 75025 dengan 26 hasil di cache
# 26 perhitungan sungguhan; sisanya diambil dari cache.
# Python punya alat siap pakai untuk ini, @lru_cache dari functools. Tanda @
# itu baru dibahas nanti di materi Decorator & Context Manager.

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
# salah karena pekerjaan yang sama dikerjakan berkali-kali.""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Menu kategori di toko online sering bersarang: Elektronik berisi HP dan",
                    "Laptop, Laptop berisi Aksesoris, dan seterusnya. Kedalamannya nggak",
                    "tetap, jadi for bertingkat nggak cukup. Pola yang sama muncul di folder",
                    "dalam folder dan balasan komentar yang membalas komentar lain.",
                    "",
                    "Kasus kecil: kategori Elektronik punya 3 produk langsung, subkategori",
                    "HP (5 produk), dan subkategori Laptop (2 produk). Laptop masih punya",
                    "subkategori Aksesoris (4 produk). Berapa total produk di Elektronik?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis bentuk datanya: tiap kategori adalah dict berisi \"produk\"",
                    "     (jumlah langsung) dan \"anak\" (list kategori di bawahnya).",
                    "  2. Total satu kategori sama dengan produknya sendiri ditambah total",
                    "     tiap anaknya. Masalah yang sama, ukurannya lebih kecil:",
                    "      def total_produk(kategori):",
                    "          jumlah = kategori[\"produk\"]",
                    "          for anak in kategori[\"anak\"]:",
                    "              jumlah += total_produk(anak)",
                    "          return jumlah",
                    "  3. Base case-nya kategori tanpa anak. Loop-nya nggak jalan, dan fungsi",
                    "     langsung mengembalikan produknya sendiri. Untuk Elektronik,",
                    "     hasilnya 14.",
                    "  4. Cek kasus pinggir: kategori yang kosong sama sekali, {\"produk\": 0,",
                    "     \"anak\": []}, harus memberi 0 tanpa error.",
                    "",
                    "Ingat: kategori toko biasanya cuma beberapa tingkat, jauh di bawah",
                    "batas rekursi Python yang sekitar 1000.",
                ]
            },
        ],
    },
    {
        "title": "16. Membongkar Argumen & Parameter Khusus",
        "sections": [
            {
                "body": [
                    "Di materi Function kamu udah pakai bintang di sisi definisi fungsi. Di",
                    "def total(*angka), bintang mengumpulkan banyak argumen jadi satu tuple.",
                    "Materi ini membahas arah sebaliknya: bintang di sisi pemanggilan. Di",
                    "situ bintang membongkar satu koleksi jadi beberapa argumen terpisah.",
                    "",
                    "Tandanya sama persis, tapi artinya berlawanan. Yang menentukan cuma",
                    "letaknya:",
                    "  di dalam def(...)     -> mengumpulkan  (satu nama menampung banyak nilai)",
                    "  di dalam pemanggilan  -> membongkar    (satu koleksi jadi banyak argumen)",
                    "",
                    "Ada dua macam bintang:",
                    "  *   membongkar list/tuple/range jadi argumen POSISI",
                    "  **  membongkar dict jadi argumen KEYWORD (key-nya jadi nama parameter)",
                    "",
                    "Argumen posisi dikirim menurut urutannya. Argumen keyword dikirim dengan",
                    "menyebut namanya, seperti sep=\" \".",
                    "",
                    "Bedanya paling gampang dilihat di print:",
                    "  genap = [2, 4, 6, 8]",
                    "  print(genap)    -> [2, 4, 6, 8]   satu argumen: list-nya dicetak",
                    "                                    lengkap dengan kurung siku dan komanya",
                    "  print(*genap)   -> 2 4 6 8        empat argumen: print memisahkannya",
                    "                                    sendiri",
                    "",
                    "Kalau bintangnya lupa, fungsi menerima satu list di parameter pertama,",
                    "dan parameter sisanya kosong:",
                    "  def f(a, b, c): ...",
                    "  f([1, 2, 3])",
                    "  TypeError: f() missing 2 required positional arguments: 'b' and 'c'",
                    "",
                    "Pesan itu membingungkan kalau kamu nggak tahu sebabnya. Rasanya kamu udah",
                    "mengirim tiga angka, tapi yang dilihat Python cuma satu list.",
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

# Pasangan * di def dan * di pemanggilan sering muncul bersama:
def luas(panjang, lebar=2):
    return panjang * lebar

def luas_dicatat(*args, **kwargs):   # KUMPULKAN apa pun yang dikirim
    print(f"-> luas dipanggil dengan {args} {kwargs}")
    return luas(*args, **kwargs)     # BONGKAR lagi, persis seperti semula

print(luas_dicatat(5))
print(luas_dicatat(5, lebar=3))""",
            },
            {
                "heading": "Menuang dan menampung koleksi dengan bintang",
                "body": [
                    "luas_dicatat menampung argumen apa pun ke args dan kwargs, lalu",
                    "membongkarnya lagi waktu meneruskan ke luas. Kalau bintang di baris",
                    "terakhirnya nggak ada, luas menerima satu tuple dan satu dict, bukan",
                    "argumen yang tadi dikirim pemanggil.",
                    "",
                    "Pasangan kumpulkan-lalu-bongkar ini bakal kamu temui lagi nanti di",
                    "materi Decorator & Context Manager. Di sana bentuknya persis seperti",
                    "ini.",
                    "",
                    "Bintang juga bisa dipakai di dalam kurung pembuat koleksi. Di sana",
                    "bintang menuang isi koleksi lain ke dalam koleksi baru:",
                    "  [*a, *b]      -> list baru: isi a lalu isi b",
                    "  (*a, *b)      -> tuple baru",
                    "  {*a, *b}      -> set baru (duplikatnya hilang sendiri)",
                    "  {**a, **b}    -> dict baru; kalau key-nya bentrok, yang KANAN menang",
                    "",
                    "{**bawaan, **pilihan} adalah cara menggabung dict yang paling sering",
                    "ketemu di kode orang. Polanya hampir selalu sama: satu dict berisi",
                    "setelan bawaan, lalu ditimpa dict berisi pilihan pemakai.",
                    "",
                    "Materi Dictionary & Set udah ngajarin a | b untuk hasil yang sama.",
                    "Bedanya:",
                    "  a | b         khusus dict, dan baru ada sejak Python 3.9",
                    "  {**a, **b}    jalan sejak Python 3.5, dan pola bintangnya sama untuk",
                    "                list/set/tuple",
                    "  a.update(b)   MENGUBAH a di tempat.",
                    "",
                    "Dua bentuk pertama bikin dict baru, jadi a dan b tetap utuh. update()",
                    "lain sendiri. Kalau salah pilih, data asalnya ikut rusak tanpa ada yang",
                    "ngasih tahu.",
                    "",
                    "Bongkar juga bisa terjadi di sebelah kiri tanda sama dengan. Materi List",
                    "& Tuple memakai unpacking biasa (x, y = titik), dan jumlahnya harus pas",
                    "persis. Dengan bintang, satu nama boleh menampung sisanya. Namanya",
                    "extended unpacking:",
                    "  pertama, *sisa = [10, 20, 30]      pertama=10  sisa=[20, 30]",
                    "  nama, *nilai, status = baris       yang di ujung diambil, sisanya ke tengah",
                    "",
                    "Ada tiga hal yang perlu kamu ingat:",
                    "  1. Yang ditampung bintang selalu berupa list, walaupun sumbernya tuple",
                    "     atau string.",
                    "  2. Sisanya boleh kosong. Hasilnya list kosong, bukan error.",
                    "  3. Di satu sisi kiri cuma boleh ada satu bintang. a, *b, *c = ... itu",
                    "     SyntaxError, soalnya Python nggak bisa menebak b berhenti di mana",
                    "     dan c mulai di mana.",
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
                "heading": "Parameter keyword-only dan positional-only",
                "body": [
                    "Sampai sini bintang selalu diikuti nama. Kalau bintang berdiri sendiri di",
                    "daftar parameter, artinya lain lagi: semua parameter sesudahnya wajib",
                    "dipanggil dengan menyebut namanya.",
                    "",
                    "  def buat_koneksi(host, *, timeout=30, ulang=3):",
                    "      ...",
                    "",
                    "  buat_koneksi(\"localhost\")              OK",
                    "  buat_koneksi(\"localhost\", timeout=5)   OK",
                    "  buat_koneksi(\"localhost\", 5)",
                    "  TypeError: buat_koneksi() takes 1 positional argument but 2 were given",
                    "",
                    "Gunanya apa? Coba baca buat_koneksi(\"localhost\", 5, 3). Nggak ada yang",
                    "bisa langsung tahu 5 itu timeout atau jumlah ulang. Dengan bintang yang",
                    "berdiri sendiri, pemanggilnya terpaksa menulis nama parameternya, jadi",
                    "kodenya menjelaskan dirinya sendiri. Fungsi bawaan juga begitu.",
                    "sorted(data, reverse=True) memang nggak bisa ditulis sorted(data, True).",
                    "",
                    "Bintang yang berdiri sendiri wajib punya parameter sesudahnya. Kalau",
                    "kamu menulis def f(a, *): tanpa apa-apa lagi, Python langsung menolak",
                    "dengan SyntaxError: named arguments must follow bare *.",
                    "",
                    "Kebalikannya adalah tanda / (Python 3.8+). Semua parameter sebelum tanda",
                    "itu cuma boleh dikirim lewat posisi, dan namanya nggak boleh disebut.",
                    "",
                    "  def bagi(a, b, /, bulat=False):",
                    "      ...",
                    "  bagi(7, 2)               OK",
                    "  bagi(7, 2, bulat=True)   OK   (bulat ada SESUDAH /, jadi bebas)",
                    "  bagi(a=7, b=2)",
                    "  TypeError: bagi() got some positional-only arguments passed as keyword",
                    "  arguments: 'a, b'",
                    "",
                    "Gunanya: nama a dan b jadi bukan bagian dari janji fungsimu. Kamu boleh",
                    "menggantinya kapan aja tanpa merusak kode orang yang memanggilnya.",
                    "",
                    "Ini juga menjelaskan keluaran help() yang tadinya kelihatan aneh:",
                    "  help(len)     -> len(obj, /)",
                    "  help(sorted)  -> sorted(iterable, /, *, key=None, reverse=False)",
                    "  help(round)   -> round(number, ndigits=None)   (tanpa / dan *: bebas",
                    "                                                  dua-duanya)",
                    "",
                    "Baris sorted tadi dibaca begini: iterable wajib lewat posisi, sedangkan",
                    "key dan reverse wajib pakai nama. Itu juga sebabnya len(obj=[1, 2])",
                    "gagal dengan TypeError: len() takes no keyword arguments, padahal",
                    "help()-nya jelas menyebut nama obj.",
                    "",
                    "Aturan ini tetap berlaku untuk argumen hasil bongkaran. Key dict yang",
                    "nggak cocok dengan nama parameter mana pun langsung ditolak:",
                    "  buat_koneksi(**{\"host\": \"x\", \"port\": 80})",
                    "  TypeError: buat_koneksi() got an unexpected keyword argument 'port'",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Berkas absensi atau ekspor spreadsheet sering punya kolom yang",
                    "jumlahnya nggak tetap: dua kolom identitas di depan, lalu sederet",
                    "status per sesi. Extended unpacking memisahkan keduanya dalam satu",
                    "baris. Pola {**bawaan, **pilihan} juga muncul di hampir setiap aplikasi",
                    "yang punya halaman pengaturan.",
                    "",
                    "Kasus kecil: satu baris absensi pelatihan berbunyi",
                    "\"2024-03-01,Andi,hadir,hadir,izin,hadir\". Kolom pertama tanggal, kedua",
                    "nama, sisanya status tiap sesi. Jumlah sesi bisa beda tiap hari.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu baris teks. Keluarannya nama dan berapa sesi yang",
                    "     dihadiri.",
                    "  2. Pecah dengan split(\",\"), lalu biarkan bintang menampung semua",
                    "     kolom sesudah nama:",
                    "      baris = \"2024-03-01,Andi,hadir,hadir,izin,hadir\"",
                    "      tanggal, nama, *sesi = baris.split(\",\")",
                    "      print(nama, sesi.count(\"hadir\"), \"dari\", len(sesi))",
                    "  3. Jalankan. Hasilnya Andi 3 dari 4. count() pada list bekerja sama",
                    "     seperti count() pada string.",
                    "  4. Cek kasus pinggir. Baris tanpa sesi sama sekali tetap jalan, dan",
                    "     sesi berisi list kosong. Baris yang cuma punya satu kolom berakhir",
                    "     ValueError, karena tanggal dan nama wajib ada.",
                    "",
                    "Ingat: yang ditampung bintang selalu list, walaupun sumbernya tuple.",
                ]
            },
        ],
    },
    {
        "title": "17. Anotasi Tipe (Type Hint)",
        "sections": [
            {
                "body": [
                    "Anotasi tipe adalah catatan di dalam kode yang menyebutkan tipe sebuah",
                    "nilai. Python tetap dynamically typed (lihat materi Variabel & Tipe",
                    "Data), dan anotasi nggak mengubah cara program berjalan sedikit pun.",
                    "Anotasi ditulis untuk manusia yang membaca kode, dan untuk alat",
                    "pemeriksa. Materi Function udah nyinggung sekilas. Di sini kita bedah",
                    "sampai kamu lancar membacanya.",
                    "",
                    "Kenapa perlu? Baris tanda tangan fungsi, yaitu baris def beserta",
                    "parameternya, adalah hal pertama yang kamu baca waktu membuka kode orang",
                    "lain. Di project Python modern, baris itu hampir selalu pakai anotasi.",
                    "Kalau bentuknya asing, kamu bakal mentok di baris pertama. Padahal baris",
                    "itu penjelasan paling padat soal fungsinya.",
                    "",
                    "Coba baca baris ini pelan-pelan:",
                    "",
                    "  def cari(nama: str, umur: int | None = None) -> list[Pengguna]:",
                    "",
                    "  nama: str          -> parameter nama diharapkan berupa str",
                    "  umur: int | None   -> boleh int, boleh None (tanda | dibaca 'atau')",
                    "  = None             -> nilai default; INI yang membuat argumennya opsional",
                    "  -> list[Pengguna]  -> yang dikembalikan: list berisi objek Pengguna",
                    "",
                    "Polanya cuma dua. Titik dua untuk tipe sebuah nama, dan panah -> untuk",
                    "tipe nilai yang dikembalikan.",
                    "",
                    "Anotasi juga boleh dipasang di variabel biasa dan atribut objek:",
                    "  jumlah: int = 0",
                    "  nama: str = \"Andi\"",
                    "  self.saldo: float = 0.0",
                    "",
                    "-> None dipakai untuk fungsi yang kerjanya cuma melakukan sesuatu",
                    "(mencetak, menyimpan, mengirim) tanpa memberi nilai balik. Fungsi tanpa",
                    "return di Python tetap mengembalikan None. Jadi None memang tipe hasilnya,",
                    "dan artinya bukan \"kosong\".",
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
                "heading": "Tipe koleksi dan gaya lama dari typing",
                "body": [
                    "Tipe koleksi ditulis pakai kurung siku yang menyebut isinya:",
                    "",
                    "  list[int]             list berisi bilangan bulat",
                    "  list[str]             list berisi teks",
                    "  dict[str, int]        dict dengan kunci str dan nilai int",
                    "  set[str]              set berisi teks",
                    "  tuple[str, int]       tuple 2 elemen: teks lalu int (POSISI menentukan)",
                    "  tuple[int, ...]       tuple berisi int, jumlah elemennya bebas",
                    "  list[dict[str, int]]  boleh bersarang sedalam yang perlu",
                    "",
                    "Dua bentuk tuple itu sengaja beda. tuple[str, int] adalah pasangan tetap,",
                    "misalnya (nama, umur). tuple[int, ...] artinya \"sekumpulan int, berapa",
                    "pun banyaknya\". Tanda ... di situ bagian dari tipenya, bukan tanda kode",
                    "yang belum selesai ditulis.",
                    "",
                    "Bentuk lama yang masih sering kamu temui",
                    "",
                    "Sebelum Python 3.9, list dan dict bawaan belum boleh dikasih kurung",
                    "siku. Jadi tipe koleksi diambil dari modul typing dan ditulis dengan",
                    "huruf besar di depan:",
                    "",
                    "  from typing import List, Dict, Any",
                    "",
                    "  def proses(data: List[int]) -> Dict[str, Any]:    # gaya lama",
                    "  def proses(data: list[int]) -> dict[str, Any]:    # gaya sekarang",
                    "",
                    "Artinya sama persis. Any tetap diambil dari typing, karena nggak punya",
                    "padanan bawaan. Jadi jangan bingung kalau dua gaya ini campur di satu",
                    "project.",
                    "",
                    "Perhatikan versinya waktu menyalin kode dari internet:",
                    "",
                    "  list[int], dict[str, int]    butuh Python 3.9+",
                    "  int | None, int | str        butuh Python 3.10+",
                    "  List[int], Optional[int]     jalan di semua versi (dari typing)",
                    "",
                    "Kalau kodenya harus jalan di Python lama, tulis baris ini di paling atas",
                    "berkas:",
                    "  from __future__ import annotations",
                    "",
                    "Dengan baris itu, anotasi disimpan sebagai teks dan nggak dievaluasi",
                    "(nggak dijalankan sebagai kode). Jadi sintaks baru boleh dipakai di dalam",
                    "anotasi. Di tempat lain tetap nggak boleh.",
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
                "heading": "Isi typing, mypy, dan jebakan anotasi",
                "body": [
                    "Ini isi baris from typing import ... yang paling sering muncul di atas",
                    "berkas:",
                    "",
                    "  Any        tipe apa pun; mematikan pemeriksaan untuk nilai itu",
                    "  Optional   Optional[X] sama dengan X | None",
                    "  Union      Union[A, B] sama dengan A | B",
                    "  Callable   Callable[[int, str], bool] = fungsi(int, str) yang hasilnya bool",
                    "  Iterable   apa saja yang bisa di-for: list, tuple, set, generator",
                    "  Sequence   yang bisa di-index dan di-len: list, tuple, str (set TIDAK)",
                    "  TypeAlias  penanda bahwa sebuah nama adalah nama lain untuk sebuah tipe",
                    "",
                    "Kenapa parameter sering ditulis Iterable atau Sequence, bukan list?",
                    "Fungsinya cuma butuh \"sesuatu yang bisa di-for\". Kalau kamu menulis",
                    "list[int], tuple dan generator ikut ditolak tanpa alasan. Untuk nilai",
                    "kembalian, aturannya kebalikannya. Sebutkan tipe yang paling konkret",
                    "(list[int]) supaya pemanggil tahu apa yang dia pegang.",
                    "",
                    "Tipe yang panjang bisa dikasih nama pendek. Namanya type alias:",
                    "  from typing import TypeAlias",
                    "  Matriks: TypeAlias = list[list[float]]",
                    "  def transpose(m: Matriks) -> Matriks:      # jauh lebih enak dibaca",
                    "",
                    "Python 3.12+ punya bentuk yang lebih ringkas:",
                    "  type Matriks = list[list[float]]",
                    "",
                    "Terus siapa yang memeriksa anotasi? Python sendiri nggak. Alatnya",
                    "terpisah, namanya mypy, dan udah disebut di materi Virtual Environment,",
                    "pip & Testing. mypy membaca kodemu tanpa menjalankannya, lalu melaporkan",
                    "anotasi yang nggak cocok:",
                    "",
                    "  pip install mypy",
                    "  mypy program.py",
                    "",
                    "  program.py:19: error: Argument 1 to \"tambah\" has incompatible type \"str\";",
                    "  expected \"int\"",
                    "  Found 1 error in 1 file (checked 1 source file)",
                    "",
                    "Editor seperti VS Code memakai anotasi yang sama untuk autocomplete dan",
                    "garis merah di bawah kode yang salah. Jadi anotasi udah ada gunanya",
                    "bahkan sebelum kamu memasang mypy.",
                    "",
                    "Beberapa jebakan yang sering kejadian:",
                    "",
                    "  1. Anotasi tanpa nilai nggak membuat variabel.",
                    "       umur: int",
                    "       print(umur)    # NameError: name 'umur' is not defined",
                    "     Baris itu cuma mencatat \"kalau nanti ada umur, tipenya int\".",
                    "",
                    "  2. Optional artinya nilainya boleh None. Artinya bukan \"argumennya",
                    "     boleh nggak diisi\".",
                    "       def simpan(nama: Optional[str]) -> None:",
                    "     Argumen nama tetap wajib diisi. Yang boleh None adalah nilainya.",
                    "     Satu-satunya yang bikin argumen boleh dilewati adalah nilai default.",
                    "",
                    "  3. def kirim(pesan: str = None) adalah salah tulis yang umum banget.",
                    "     Default-nya None, padahal tipenya ditulis str. Yang benar:",
                    "       def kirim(pesan: str | None = None) -> None:",
                    "",
                    "  4. Anotasi yang bohong lebih bahaya daripada nggak pakai anotasi.",
                    "     Misalnya fungsi ditulis -> int, tapi kadang mengembalikan None.",
                    "     Pembaca percaya, mypy juga percaya, dan yang error justru kode",
                    "     pemanggilnya.",
                    "",
                    "  5. Tipe yang pakai kurung siku nggak bisa dipakai di isinstance:",
                    "       isinstance(data, list[int])",
                    "       # TypeError: isinstance() argument 2 cannot be a parameterized generic",
                    "       isinstance(data, list)      # ini yang benar",
                    "",
                    "  6. Nama class yang belum selesai dibuat ditulis dalam tanda kutip",
                    "     (\"Node\"). Alasannya, waktu baris def itu dibaca, class-nya memang",
                    "     belum ada. Sejak Python 3.14 kutipnya nggak wajib lagi. Tapi kode",
                    "     yang beredar sekarang masih penuh bentuk berkutip itu, jadi kamu",
                    "     tetap perlu mengenalinya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di proyek yang dikerjakan banyak orang, baris def beranotasi adalah",
                    "dokumentasi pertama yang dibaca. Editor memakai anotasi itu untuk",
                    "autocomplete, dan mypy memakainya untuk menandai kesalahan sebelum",
                    "program dijalankan. Yang paling sering diselamatkan anotasi adalah",
                    "fungsi yang kadang mengembalikan None.",
                    "",
                    "Kasus kecil: fungsi cari_harga(kode) di aplikasi kasir mengembalikan",
                    "None untuk kode yang belum terdaftar. Rekan satu timmu memakainya",
                    "langsung untuk berhitung, dan programnya jatuh dengan TypeError waktu",
                    "ada kode asing.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tanyakan apa saja yang bisa dikembalikan fungsinya: int kalau kode",
                    "     ketemu, None kalau nggak.",
                    "  2. Tulis anotasi yang jujur, supaya pembaca dan mypy tahu None",
                    "     mungkin datang:",
                    "      from typing import Optional",
                    "      HARGA = {\"A01\": 12500, \"A02\": 8000}",
                    "      def cari_harga(kode: str) -> Optional[int]:",
                    "          return HARGA.get(kode)",
                    "      harga = cari_harga(\"B99\")",
                    "      print(0 if harga is None else harga)",
                    "  3. Di pemanggil, periksa is None sebelum berhitung. Kode B99 di atas",
                    "     memberi 0, dan program tetap jalan.",
                    "  4. Jalankan mypy program.py. Kalau ada pemanggil yang menjumlahkan",
                    "     hasil cari_harga() tanpa memeriksanya, mypy menandai baris itu.",
                    "",
                    "Jebakan: menulis -> int padahal fungsinya kadang mengembalikan None.",
                    "mypy ikut percaya, dan pemeriksaan di pemanggil nggak pernah diminta.",
                ]
            },
        ],
    },
    {
        "title": "18. Lambda & Higher-Order Function",
        "sections": [
            {
                "body": [
                    "Lambda adalah fungsi anonim, artinya fungsi tanpa nama. Bentuknya",
                    "ringkas, dan cocok untuk logika sederhana yang muat satu baris. Kalau kamu",
                    "pernah lihat arrow function di JS atau lambda di Java, idenya mirip.",
                    "",
                    "Bentuk penulisannya:",
                    "  lambda parameter: ekspresi",
                    "",
                    "Contohnya:",
                    "  tambah = lambda a, b: a + b",
                    "  print(tambah(3, 4))     # 7",
                    "",
                    "  kuadrat = lambda x: x ** 2",
                    "  print(kuadrat(5))       # 25",
                    "",
                    "Dalam praktik, lambda jarang disimpan ke variabel seperti di atas.",
                    "Biasanya lambda dikirim sebagai argumen untuk fungsi lain. Fungsi yang",
                    "menerima fungsi lain sebagai argumen disebut higher-order function.",
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
                "heading": "Kenapa map dan filter dibungkus list",
                "body": [
                    "Kenapa tiap map() dan filter() di atas dibungkus list()? Soalnya dua-duanya",
                    "nggak mengembalikan list. Yang keluar adalah iterator, yaitu objek yang",
                    "menyiapkan hasilnya satu per satu waktu diminta, bukan sekaligus di",
                    "depan:",
                    "",
                    "  print(map(lambda x: x * 2, angka))",
                    "  -> <map object at 0x7f3a1c0d5e40>",
                    "",
                    "Itu bukan error, dan bukan list yang gagal dicetak. Wujud objeknya memang",
                    "begitu. list() yang meminta seluruh isinya dikeluarkan saat itu juga.",
                    "Kalau hasilnya cuma mau dipakai di for satu kali, list() malah nggak",
                    "perlu.",
                    "",
                    "Sama seperti zip() di materi Fungsi Bawaan untuk Koleksi, isi iterator",
                    "ini habis sekali pakai. Begitu udah dibaca sampai akhir, membacanya lagi",
                    "nggak menghasilkan apa-apa.",
                    "",
                    "Alasan yang mirip bikin mahasiswa.keys() di materi Dictionary & Set",
                    "tercetak sebagai dict_keys([...]), bukan list biasa. Bedanya, .keys(),",
                    ".values(), dan .items() memberi view. View itu seperti jendela yang selalu",
                    "menampilkan isi dict saat itu juga, dan boleh dilihat berkali-kali.",
                    "Dua-duanya bukan list, dan dua-duanya tinggal dibungkus list() kalau kamu",
                    "memang butuh list. Cara kerja di balik keduanya dibahas di materi",
                    "Iterator & Generator.",
                ]
            },
            {
                "body": [
                    "Kapan pakai lambda, kapan pakai def biasa:",
                    "  - Lambda: logikanya singkat, cuma dipakai sekali, dan dikirim sebagai",
                    "    argumen.",
                    "  - def: logikanya lebih dari satu baris, dipakai berkali-kali, atau",
                    "    butuh nama yang jelas supaya gampang dibaca.",
                    "",
                    "PEP 8, panduan gaya kode Python yang resmi, menyarankan supaya lambda",
                    "nggak disimpan ke variabel. Kalau butuh nama, pakai def aja:",
                    "  X  kuadrat = lambda x: x ** 2",
                    "  V  def kuadrat(x): return x ** 2",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online selalu punya tombol \"urutkan berdasarkan harga\" dan filter",
                    "\"di bawah 50 ribu\". Di balik tombol itu ada sorted() dengan key dan",
                    "penyaring seperti filter(). Aturannya pendek dan cuma dipakai di satu",
                    "tempat, jadi lambda pas untuk ditulis langsung di argumennya.",
                    "",
                    "Kasus kecil: daftar produk berupa tuple (nama, harga): Kaos 75000, Topi",
                    "45000, Kaus kaki 15000, dan Tas 45000. Tampilkan produk di bawah 50.000",
                    "dari yang termurah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya list tuple. Keluarannya nama dan harga produk murah,",
                    "     diurutkan menurut harga.",
                    "  2. Saring dengan filter(), lalu urutkan dengan key yang mengambil",
                    "     elemen harga, yaitu indeks 1:",
                    "      produk = [(\"Kaos\", 75000), (\"Topi\", 45000),",
                    "                (\"Kaus kaki\", 15000), (\"Tas\", 45000)]",
                    "      murah = filter(lambda p: p[1] < 50000, produk)",
                    "      for nama, harga in sorted(murah, key=lambda p: p[1]):",
                    "          print(nama, harga)",
                    "  3. Jalankan. Hasilnya Kaus kaki 15000, Topi 45000, lalu Tas 45000.",
                    "  4. Cek kasus pinggir: Topi dan Tas harganya sama. sorted() itu stabil,",
                    "     jadi keduanya tetap di urutan aslinya. Topi muncul lebih dulu.",
                    "",
                    "Jebakan: hasil filter() habis sekali pakai. Kalau murah dipakai di",
                    "loop kedua, loop itu nggak mencetak apa pun.",
                ]
            },
        ],
    },
    {
        "title": "19. Scope, Closure & nonlocal",
        "sections": [
            {
                "body": [
                    "Materi Function udah menyebut dua tingkat scope. Ada variabel lokal milik",
                    "fungsi, dan variabel global milik modul. Ternyata Python punya empat",
                    "tingkat. Tingkat ketiga, namanya enclosing, hampir nggak pernah dibahas.",
                    "Padahal tingkat itulah yang bikin decorator, callback, dan factory",
                    "function bisa bekerja.",
                    "",
                    "Kenapa harus ada scope? Sebuah program bisa berisi ribuan nama. Kalau",
                    "semuanya tinggal di satu tempat, variabel i yang kamu tulis hari ini bisa",
                    "menimpa i yang ditulis orang lain bulan lalu, tanpa tanda apa pun di",
                    "layar. Scope adalah aturan yang bikin nama yang sama di dua tempat tetap",
                    "jadi dua barang yang berbeda.",
                    "",
                    "Aturan mencari nama di Python namanya LEGB. Waktu sebuah nama dibaca,",
                    "Python ngecek empat tempat secara berurutan, lalu berhenti di tempat",
                    "pertama yang punya nama itu:",
                    "",
                    "  L  Local      nama di dalam fungsi yang sedang berjalan",
                    "  E  Enclosing  nama milik fungsi PEMBUNGKUS, kalau fungsi ini bersarang",
                    "  G  Global     nama di tingkat modul, yaitu berkas .py yang sedang jalan",
                    "  B  Built-in   nama bawaan Python: print, len, sum, str, list, range, ...",
                    "",
                    "Kalau sampai B pun nggak ketemu, baru muncul NameError.",
                    "",
                    "Ada dua akibat yang langsung kerasa waktu kamu membaca kode orang:",
                    "  - Nama di tingkat yang lebih dalam menutupi (shadow) nama yang sama di",
                    "    tingkat luar. Kalau kamu menamai variabel list, id, atau sum, fungsi",
                    "    bawaannya jadi nggak bisa dipakai. Tapi cuma di dalam scope itu, jadi",
                    "    error-nya sering muncul jauh dari penyebabnya.",
                    "  - Membaca nama dari scope luar nggak butuh izin apa pun. Menugaskan",
                    "    ulang, artinya mengisi nama itu dengan nilai baru pakai =, butuh izin",
                    "    yang ditulis jelas: global atau nonlocal. Tanpa izin itu, penugasan",
                    "    selalu bikin variabel lokal yang baru. Dari situlah UnboundLocalError",
                    "    berasal.",
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
                "heading": "Beda global dan nonlocal, serta pemakaian closure",
                "body": [
                    "global vs nonlocal",
                    "",
                    "Dua-duanya bilang \"jangan bikin variabel baru, pakai yang udah ada\".",
                    "Bedanya, tempat yang ditunjuk nggak sama:",
                    "",
                    "                  menunjuk ke                dipakai di",
                    "  global x        tingkat MODUL              fungsi mana pun",
                    "  nonlocal x      fungsi PEMBUNGKUS terdekat hanya di fungsi bersarang",
                    "",
                    "Aturan mainnya, sekaligus jebakannya:",
                    "  - nonlocal menuntut namanya udah ada di salah satu fungsi pembungkus.",
                    "    Kalau nggak ada, Python menolak berkasnya sebelum satu baris pun",
                    "    dijalankan:",
                    "      SyntaxError: no binding for nonlocal 'x' found",
                    "    Perhatikan, ini SyntaxError, bukan error waktu program jalan. Jadi",
                    "    seluruh berkasnya gagal dimuat, termasuk fungsi lain yang nggak",
                    "    salah apa-apa.",
                    "  - nonlocal nggak pernah sampai ke tingkat modul. Untuk itu memang",
                    "    pakai global.",
                    "  - global di dalam fungsi bersarang melompati tingkat enclosing dan",
                    "    langsung ke modul. Jadi dua kata ini menunjuk tujuan yang berbeda.",
                    "    Yang satu bukan versi lebih kuat dari yang lain.",
                    "",
                    "Banyak orang bingung kapan nonlocal nggak diperlukan. Jawabannya ada dua:",
                    "  - Kalau kamu cuma membaca. return hitung nggak butuh izin apa pun.",
                    "  - Kalau kamu memutasi objeknya, artinya mengubah isinya, bukan",
                    "    menugaskan ulang namanya:",
                    "      data.append(x)   isi['k'] = 1   daftar[0] = 9    -> tidak butuh nonlocal",
                    "      hitung += 1      data = []                       -> butuh nonlocal",
                    "    Baris atas mengubah isi objek yang udah ditunjuk namanya. Baris bawah",
                    "    bikin nama itu menunjuk barang lain. Lihat materi Referensi Objek,",
                    "    Salinan & Jebakan Mutable. Makanya banyak closure memakai list atau",
                    "    dict sebagai wadah keadaan, dan nggak pernah menyentuh nonlocal sama",
                    "    sekali.",
                    "",
                    "Ada dua scope yang sering bikin kaget waktu membaca kode:",
                    "  - Comprehension punya scope sendiri. [n * 2 for n in range(3)] nggak",
                    "    meninggalkan n di luar, sedangkan for biasa meninggalkannya.",
                    "  - Badan class nggak dianggap pembungkus bagi method di dalamnya. Method",
                    "    yang menulis faktor begitu aja kena NameError, walaupun ada",
                    "    faktor = 3 di badan class. Yang benar self.faktor atau",
                    "    NamaKelas.faktor.",
                    "",
                    "Closure ini muncul di kode nyata dalam beberapa bentuk:",
                    "  - Fungsi pembungkus: wrapper mengingat fungsi yang dibungkusnya.",
                    "    Contohnya ada di bawah. Pola ini namanya decorator, dan dibahas",
                    "    nanti di materi Decorator & Context Manager.",
                    "  - Callback dan event handler: fungsinya dititipkan sekarang, dipanggil",
                    "    nanti, dan tetap perlu tahu konteks waktu dia dibuat.",
                    "  - Factory: satu fungsi mencetak banyak fungsi dengan setelan berbeda.",
                    "  - key= untuk sorted(), kalau dasar pengurutannya baru diketahui waktu",
                    "    program jalan.",
                    "",
                    "Kapan jangan pakai closure? Begitu keadaan yang disimpan lebih dari",
                    "satu-dua nilai, atau butuh lebih dari dua fungsi untuk mengurusnya, class",
                    "lebih enak dibaca (materi OOP: Class & Object). Closure yang berisi satu",
                    "fungsi itu mirip class dengan satu method. Bedanya, class memberi nama",
                    "untuk tiap bagiannya.",
                ],
            },
            {
                "heading": "Jebakan late binding, dan closure yang membungkus fungsi",
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
# Closure juga bisa membungkus fungsi lain. wrapper di bawah adalah closure
# yang mengingat 'fungsi' dan 'jumlah' dari scope pembungkusnya.

def hitung_panggilan(fungsi):
    jumlah = 0

    def wrapper(*args, **kwargs):
        nonlocal jumlah                 # satu penghitung, dipakai lintas panggilan
        jumlah += 1
        print(f"[{fungsi.__name__} dipanggil ke-{jumlah}]")
        return fungsi(*args, **kwargs)

    return wrapper

def sapa(nama):
    return f"Halo, {nama}"

sapa = hitung_panggilan(sapa)           # nama sapa sekarang menunjuk ke wrapper

print(sapa("Andi"))
print(sapa("Budi"))
# [sapa dipanggil ke-1]
# Halo, Andi
# [sapa dipanggil ke-2]
# Halo, Budi

# wrapper membawa dua tumpangan dari scope pembungkusnya:
print(sapa.__code__.co_freevars)        # ('fungsi', 'jumlah')
# hitung_panggilan sudah lama selesai, tapi wrapper masih bisa menyebut fungsi
# aslinya. Itu cuma mungkin karena closure. Pola "bungkus fungsi lalu timpa
# namanya" ini disebut decorator, dan Python punya tanda @ untuk menulisnya
# lebih singkat. Itu dibahas nanti di materi Decorator & Context Manager.""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Closure dipakai untuk membuat fungsi yang membawa setelannya sendiri:",
                    "pemformat harga per mata uang, callback tombol yang ingat tombol mana",
                    "yang diklik, atau pencacah yang nggak boleh disentuh kode lain. Satu",
                    "fungsi pembuat bisa mencetak banyak fungsi, dan keadaan masing-masing",
                    "tetap terpisah.",
                    "",
                    "Kasus kecil: puskesmas punya loket A untuk pasien umum dan loket B",
                    "untuk pasien BPJS. Tiap loket memberi nomor antrean sendiri yang naik",
                    "terus: A-001, A-002, lalu B-001 di loket sebelah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tiap loket butuh keadaan sendiri, yaitu nomor terakhir. Variabel",
                    "     global cuma ada satu, jadi nomor dua loket bakal tercampur.",
                    "  2. Simpan nomornya sebagai variabel milik fungsi pembuat. Fungsi di",
                    "     dalamnya menaikkan nomor itu, jadi butuh nonlocal:",
                    "      def buat_loket(huruf, hitung=0):",
                    "          def ambil():",
                    "              nonlocal hitung",
                    "              hitung += 1",
                    "              return f\"{huruf}-{hitung:03}\"",
                    "          return ambil",
                    "  3. Buat dua loket: loket_a = buat_loket(\"A\") dan loket_b =",
                    "     buat_loket(\"B\"). Memanggil loket_a() dua kali lalu loket_b() sekali",
                    "     memberi A-001, A-002, dan B-001.",
                    "  4. Cek kasus pinggir: hapus baris nonlocal. Python menganggap hitung",
                    "     variabel lokal baru, dan panggilan pertama gagal dengan",
                    "     UnboundLocalError.",
                    "",
                    "Ingat: :03 di f-string artinya lebar 3, sisanya diisi nol di depan.",
                ]
            },
        ],
    },
    {
        "title": "20. List Comprehension & Generator Expression",
        "sections": [
            {
                "body": [
                    "List comprehension adalah cara ringkas bikin list dari sebuah iterable.",
                    "Iterable artinya sesuatu yang isinya bisa diambil satu per satu, seperti",
                    "list, string, atau range. Cara ini menggantikan for-loop yang lebih",
                    "panjang, dan sering disebut \"Pythonic\", artinya sesuai gaya yang lazim",
                    "dipakai programmer Python.",
                    "",
                    "Bentuk dasarnya:",
                    "  [ekspresi for item in iterable]",
                    "  [ekspresi for item in iterable if kondisi]",
                    "",
                    "Bandingkan dua cara bikin list yang sama. Pakai for-loop biasa:",
                    "  hasil = []",
                    "  for x in range(5):",
                    "      hasil.append(x**2)",
                    "",
                    "Pakai comprehension, cukup satu baris:",
                    "  hasil = [x**2 for x in range(5)]",
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
print(panjang)    # {'andi': 4, 'budi': 4, 'citra': 5}

# Operator walrus := (materi Angka, Perbandingan & Operator yang Belum
# Dibahas) di kondisi: hitung sekali, pakai dua kali
harga = [1000, 5000, 20000]
mahal = [p for h in harga if (p := h // 10) > 400]
print(mahal)      # [500, 2000]"""
            },
            {
                "body": [
                    "Generator expression bentuknya mirip list comprehension, tapi pakai",
                    "kurung () dan bukan []. Bedanya, dia nggak langsung bikin semua elemen",
                    "di memori. Elemennya dihasilkan satu per satu, baru waktu diminta. Cara",
                    "kerja begini disebut lazy (malas).",
                    "",
                    "  kuadrat_list = [x**2 for x in range(1000000)]   # buat semua di RAM",
                    "  kuadrat_gen  = (x**2 for x in range(1000000))   # hemat memori!",
                    "",
                    "Kapan pakai generator expression:",
                    "  - Datanya besar sekali, dan kamu nggak butuh semuanya ada di memori",
                    "    sekaligus.",
                    "  - Datanya cuma perlu diproses sekali secara berurutan, misalnya",
                    "    dengan sum():",
                    "    total = sum(x**2 for x in range(1000000))  # hemat RAM",
                    "",
                    "Generator dibahas lebih dalam di materi Iterator & Generator.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data dari formulir online jarang rapi: ada spasi di ujung, huruf besar",
                    "campur kecil, dan baris kosong. Sebelum disimpan atau dihitung,",
                    "programmer biasanya merapikannya dengan satu list comprehension. Untuk",
                    "data jutaan baris, generator expression dipakai supaya hasil",
                    "antaranya nggak memenuhi memori.",
                    "",
                    "Kasus kecil: daftar email pendaftar lomba berisi \" Andi@Gmail.com\",",
                    "\"budi@yahoo.co.id \" yang ada spasi di ujungnya, satu isian yang cuma",
                    "berisi spasi, dan \"andi@gmail.com\". Panitia butuh list yang rapi, dan",
                    "jumlah pendaftar yang berbeda.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya list teks kotor. Keluarannya list email huruf kecil",
                    "     tanpa spasi, tanpa isian kosong.",
                    "  2. Rapikan dan saring sekaligus. strip() dulu, baru lower():",
                    "      data = [\" Andi@Gmail.com\", \"budi@yahoo.co.id \", \"  \",",
                    "              \"andi@gmail.com\"]",
                    "      rapi = [e.strip().lower() for e in data if e.strip()]",
                    "      print(rapi, len(set(rapi)))",
                    "  3. Jalankan. List-nya berisi tiga email, dan jumlah yang berbeda 2,",
                    "     karena dua email Andi ternyata sama sesudah dirapikan.",
                    "  4. Cek kasus pinggir: isian yang cuma berisi spasi. e.strip() memberi",
                    "     string kosong, yang falsy, jadi isian itu tersaring.",
                    "",
                    "Jebakan: if e saja nggak cukup. \"  \" bukan string kosong, jadi isian",
                    "spasi ikut lolos kalau syaratnya nggak memakai strip().",
                ]
            },
        ],
    },
    {
        "title": "21. OOP: Class & Object",
        "sections": [
            {
                "body": [
                    "Class itu cetakan, atau blueprint. Object adalah benda yang dibuat dari",
                    "cetakan itu, dan sering juga disebut instance. Gampangnya, class itu",
                    "cetakan kue, object itu kuenya. Satu cetakan bisa menghasilkan banyak",
                    "kue.",
                    "",
                    "Bentuk dasar class di Python:",
                    "  class NamaClass:",
                    "      def __init__(self, param):    # constructor",
                    "          self.atribut = param",
                    "",
                    "      def method(self):             # method biasa",
                    "          print(self.atribut)",
                    "",
                    "Dua nama di situ perlu kamu kenal:",
                    "  - self merujuk ke objek itu sendiri. self wajib jadi parameter pertama",
                    "    di tiap method, tapi nggak ditulis waktu kamu memanggil method-nya.",
                    "    Python yang mengisinya.",
                    "  - __init__ adalah constructor, yaitu method yang otomatis dipanggil",
                    "    waktu objek dibuat.",
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
                "heading": "Class attribute, static method, dan class method",
                "body": [
                    "Class attribute vs instance attribute",
                    "",
                    "Class attribute ditulis langsung di badan class, dan dipakai bersama oleh",
                    "semua objek. Instance attribute ditulis lewat self, dan tiap objek punya",
                    "miliknya sendiri:",
                    "",
                    "  class Mahasiswa:",
                    "      kampus = \"Universitas ABC\"   # class attribute (dibagi SEMUA objek)",
                    "      def __init__(self, nama):",
                    "          self.nama = nama            # instance attribute (per objek)",
                    "",
                    "  m1 = Mahasiswa(\"Andi\")",
                    "  print(m1.kampus)    # Universitas ABC (diwarisi dari class)",
                    "  print(Mahasiswa.kampus)  # bisa diakses lewat class langsung",
                    "",
                    "Static method dan class method",
                    "",
                    "Selain method biasa, ada dua jenis method lain:",
                    "  - @staticmethod nggak butuh self maupun cls. Isinya fungsi biasa yang",
                    "    kebetulan tinggal di dalam namespace class. Namespace artinya wadah",
                    "    nama, jadi fungsinya dipanggil lewat nama class-nya.",
                    "  - @classmethod menerima cls, yaitu class-nya, bukan self. Paling sering",
                    "    dipakai untuk bikin objek lewat jalan lain.",
                    "",
                    "Tanda @ di atas def itu namanya decorator. Decorator adalah penanda yang",
                    "mengubah cara Python memperlakukan def di bawahnya. Untuk sekarang cukup",
                    "tahu efeknya. Cara kerjanya, dan cara bikin decorator sendiri, dibahas",
                    "di materi Decorator & Context Manager.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di aplikasi sungguhan, tiap benda yang diurus program biasanya jadi",
                    "class: Produk, Pelanggan, Rekening, Keranjang. Objeknya membawa data",
                    "sekaligus aturan yang boleh dikerjakan pada data itu. Kasir nggak perlu",
                    "tahu isi keranjang disimpan di mana, cukup memanggil tambah() dan",
                    "total().",
                    "",
                    "Kasus kecil: dua pelanggan, Andi dan Budi, belanja bersamaan di kasir",
                    "online. Andi membeli 2 kopi seharga 18000, Budi membeli 1 roti seharga",
                    "12000. Keranjang mereka nggak boleh tercampur.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan data dan perilakunya. Datanya daftar harga item, dan",
                    "     perilakunya menambah item serta menghitung total.",
                    "  2. Siapkan list kosong di __init__, supaya tiap objek punya list-nya",
                    "     sendiri:",
                    "      class Keranjang:",
                    "          def __init__(self):",
                    "              self.isi = []",
                    "          def tambah(self, harga, jumlah=1):",
                    "              self.isi.append(harga * jumlah)",
                    "  3. Tambahkan method total() yang mengembalikan sum(self.isi). Buat",
                    "     dua objek, isi masing-masing, lalu panggil total(). Hasilnya 36000",
                    "     untuk Andi dan 12000 untuk Budi.",
                    "  4. Cek kasus pinggir: keranjang yang belum diisi. total() memberi 0,",
                    "     karena sum() atas list kosong memang 0.",
                    "",
                    "Jebakan: kalau isi = [] ditulis di badan class sebagai class attribute,",
                    "semua keranjang berbagi satu list. Total Budi ikut memuat kopi Andi.",
                ]
            },
        ],
    },
    {
        "title": "22. OOP: Inheritance & Polymorphism",
        "sections": [
            {
                "body": [
                    "Inheritance, atau pewarisan, artinya class anak mewarisi atribut dan",
                    "method dari class induk. Class induknya ditulis di dalam kurung:",
                    "  class Anak(Induk):",
                    "      ...",
                    "",
                    "super() dipakai untuk memanggil constructor atau method milik class",
                    "induk.",
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
                    "Multiple inheritance",
                    "",
                    "Python mengizinkan satu class mewarisi dari banyak class sekaligus. Ini",
                    "beda dengan Java, yang nggak mengizinkannya:",
                    "  class C(A, B):",
                    "      pass",
                    "",
                    "Kalau ada method dengan nama yang sama di beberapa induk, urutan",
                    "pencariannya ditentukan Method Resolution Order (MRO). Kamu bisa ngecek",
                    "urutannya dengan C.__mro__ atau C.mro().",
                    "",
                    "isinstance() dan issubclass()",
                    "",
                    "isinstance() mengecek apakah sebuah objek termasuk class tertentu.",
                    "issubclass() mengecek apakah sebuah class turunan class lain:",
                    "  isinstance(kucing, Hewan)     -> True (Kucing adalah Hewan)",
                    "  issubclass(Kucing, Hewan)     -> True",
                    "",
                    "Duck typing",
                    "",
                    "Python memegang filosofi yang namanya duck typing: \"kalau jalannya",
                    "seperti bebek dan suaranya seperti bebek, anggap aja itu bebek\". Python",
                    "nggak terlalu ketat soal tipe. Yang penting objeknya punya method atau",
                    "perilaku yang dibutuhkan. Objek itu nggak wajib turunan class tertentu",
                    "lewat inheritance.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kasir modern menerima beberapa cara bayar: tunai, transfer bank, dan",
                    "dompet digital. Biaya adminnya beda-beda, tapi kode kasir cukup",
                    "memanggil satu method yang sama untuk semuanya. Begitu ada cara bayar",
                    "baru, yang ditambah cuma satu class, dan kode kasirnya nggak disentuh.",
                    "",
                    "Kasus kecil: belanja Rp 100.000. Tunai tanpa biaya admin, transfer",
                    "bank kena Rp 2.500, dan dompet digital kena 1% dari belanja. Kasir",
                    "harus mencetak total bayar untuk cara apa pun yang dipilih pelanggan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang beda: cuma cara menghitung biaya. Bagian itu yang",
                    "     jadi method di class induk.",
                    "  2. Tulis induknya dengan biaya bawaan 0, lalu biarkan tiap anak",
                    "     menimpa method itu:",
                    "      class Pembayaran:",
                    "          def biaya(self, total):",
                    "              return 0",
                    "      class Transfer(Pembayaran):",
                    "          def biaya(self, total):",
                    "              return 2500",
                    "  3. Tambahkan class DompetDigital(Pembayaran) yang biaya()-nya",
                    "     mengembalikan total // 100. Kasir cukup menulis total +",
                    "     p.biaya(total). Hasilnya 100000, 102500, dan 101000.",
                    "  4. Cek kasus pinggir: class anak yang lupa menulis biaya(). Python",
                    "     nggak protes, dan objeknya memakai biaya 0 milik induk tanpa",
                    "     peringatan apa pun.",
                    "",
                    "Ingat: kasir nggak pernah bertanya \"ini transfer atau tunai?\". Python",
                    "memilih method sesuai class asli objeknya, dan itulah polymorphism.",
                ]
            },
        ],
    },
    {
        "title": "23. Abstract Base Class & Kontrak Antar-Class",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya ditutup dengan duck typing: Python nggak menuntut",
                    "pewarisan, yang penting objeknya punya method yang dibutuhkan. Cara itu",
                    "enak selama programnya kecil. Begitu program membesar, muncul class lain",
                    "yang harus bisa dipakai di tempat yang sama. Bisa class bikinanmu bulan",
                    "depan, bisa juga bikinan orang lain.",
                    "",
                    "Di situ muncul pertanyaan yang nggak dijawab duck typing: gimana caranya",
                    "memastikan sebuah class punya semua method wajibnya, sebelum kodenya",
                    "terlanjur jalan?",
                    "",
                    "Jawaban bakunya abstract base class, disingkat ABC. ABC adalah class",
                    "yang sengaja dibikin nggak lengkap. Isinya kebanyakan cuma daftar nama",
                    "method yang harus ditulis oleh class turunannya. Kalau kamu pernah",
                    "belajar Java, ABC ini padanan interface di Java, yang sering dipakai",
                    "sebagai pembanding di materi OOP sebelumnya.",
                    "",
                    "Bentuknya seperti ini, dan kamu bakal sering ketemu bentuk ini waktu",
                    "membaca kode orang:",
                    "",
                    "  from abc import ABC, abstractmethod",
                    "",
                    "  class Penyimpan(ABC):              # ABC datang dari modul bawaan abc",
                    "      @abstractmethod                # penanda: WAJIB ditulis ulang turunannya",
                    "      def simpan(self, kunci, nilai):",
                    "          pass                       # badan kosong; boleh juga ditulis  ...",
                    "",
                    "Baris terakhir itu yang paling sering salah dibaca pemula. Badan pass",
                    "atau ... di situ nggak berarti kodenya belum selesai atau ditinggal",
                    "setengah jalan. Badannya memang harus kosong, soalnya yang bertugas",
                    "mengisinya adalah class turunan.",
                    "",
                    "Akibatnya, class Penyimpan sendiri nggak boleh dibikin objeknya.",
                    "Menulis Penyimpan() bakal gagal, dan kegagalan itu memang disengaja.",
                ],
            },
            {
                "heading": "Satu kontrak, dua implementasi, dan dua penolakan",
                "code": "from abc import ABC, abstractmethod\n\n\nclass Penyimpan(ABC):\n    \"\"\"Kontrak: apa pun yang menyimpan catatan wajib bisa simpan & ambil.\"\"\"\n\n    @abstractmethod\n    def simpan(self, kunci, nilai):\n        pass\n\n    @abstractmethod\n    def ambil(self, kunci):\n        pass\n\n    def simpan_banyak(self, pasangan):    # method BIASA, isinya sudah lengkap\n        for kunci, nilai in pasangan:\n            self.simpan(kunci, nilai)     # memakai method yang belum ditulis\n\n\nclass PenyimpanMemori(Penyimpan):         # implementasi konkret pertama\n    def __init__(self):\n        self.data = {}\n\n    def simpan(self, kunci, nilai):\n        self.data[kunci] = nilai\n\n    def ambil(self, kunci):\n        return self.data.get(kunci)\n\n\nclass PenyimpanBaris(Penyimpan):          # implementasi konkret kedua\n    def __init__(self):\n        self.baris = []\n\n    def simpan(self, kunci, nilai):\n        self.baris.append(f\"{kunci}={nilai}\")\n\n    def ambil(self, kunci):\n        for b in self.baris:\n            k, _, v = b.partition(\"=\")\n            if k == kunci:\n                return v\n        return None\n\n\nclass PenyimpanSetengahJadi(Penyimpan):\n    def simpan(self, kunci, nilai):       # method 'ambil' LUPA ditulis\n        print(\"disimpan:\", kunci)\n\n\n# Kode di bawah ini tidak peduli gudangnya jenis apa: kontraknya menjamin\n# simpan(), ambil(), dan simpan_banyak() PASTI ada di dua-duanya.\nfor gudang in (PenyimpanMemori(), PenyimpanBaris()):\n    gudang.simpan_banyak([(\"nama\", \"Levi\"), (\"kota\", \"Bontang\")])\n    print(type(gudang).__name__, \"->\", gudang.ambil(\"kota\"))\n\ntry:\n    Penyimpan()                 # class kontrak memang TIDAK boleh jadi objek\nexcept TypeError as e:\n    print(\"TypeError:\", e)\n\ntry:\n    PenyimpanSetengahJadi()      # turunan yang belum lengkap ikut ditolak\nexcept TypeError as e:\n    print(\"TypeError:\", e)\n\n# PenyimpanMemori -> Bontang\n# PenyimpanBaris -> Bontang\n# TypeError: Can't instantiate abstract class Penyimpan without an\n#            implementation for abstract methods 'ambil', 'simpan'\n# TypeError: Can't instantiate abstract class PenyimpanSetengahJadi without\n#            an implementation for abstract method 'ambil' (kalimat persisnya\n#            berbeda antar versi Python; yang penting nama method yang kurang)",
            },
            {
                "heading": "Jebakan ABC dan raise NotImplementedError",
                "body": [
                    "Ada tiga hal yang perlu kamu tangkap dari program di atas:",
                    "",
                    "  1. Penyimpan() melempar TypeError. Kodenya nggak rusak. Memang itu",
                    "     gunanya ABC: kontrak nggak boleh dipakai sebagai barang jadi.",
                    "  2. Pengecekannya terjadi waktu objek dibikin, bukan waktu Python",
                    "     membaca class-nya. PenyimpanSetengahJadi yang kurang satu method",
                    "     tetap lolos didefinisikan. Error-nya baru muncul di baris yang",
                    "     mencoba bikin objeknya. Jadi kalau kodemu nggak pernah bikin",
                    "     objek dari class itu, nggak bakal ada yang protes.",
                    "  3. ABC boleh berisi method biasa yang isinya sudah lengkap, seperti",
                    "     simpan_banyak. Pola ini umum banget: class induk menulis alurnya,",
                    "     class turunan mengisi langkah-langkahnya.",
                    "",
                    "Kalimat TypeError-nya beda-beda antar versi Python. Versi lama berbunyi",
                    "'with abstract methods ambil, simpan'. Kamu cukup kenali kata kuncinya:",
                    "abstract class, lalu nama method yang belum diisi.",
                    "",
                    "Ada tiga jebakan yang sering kejadian:",
                    "",
                    "  - Lupa menulis (ABC). Kalau class-nya cuma ditulis  class Penyimpan:",
                    "    maka @abstractmethod nggak ngapa-ngapain. Objeknya tetap bisa",
                    "    dibikin, method-nya bisa dipanggil, hasilnya None, dan nggak ada",
                    "    satu pun pesan error. Justru karena nggak ada pesannya, jebakan ini",
                    "    yang paling mahal.",
                    "  - Urutan decorator kalau digabung dengan property: @property di atas,",
                    "    @abstractmethod tepat di bawahnya. Kalau urutannya dibalik, Python",
                    "    langsung menolak waktu class-nya dibaca, dengan AttributeError yang",
                    "    bilang atribut __isabstractmethod__ milik property nggak bisa",
                    "    ditulis.",
                    "  - ABC cuma ngecek nama method-nya ada, nggak ngecek parameternya.",
                    "    Turunan yang menulis def simpan(self) padahal induknya",
                    "    def simpan(self, kunci, nilai) tetap lolos. Error-nya baru muncul",
                    "    nanti, waktu method itu dipanggil dengan dua argumen.",
                    "",
                    "Ada juga bentuk manual untuk kontrak yang sama, tanpa modul abc. Bentuk",
                    "ini masih banyak di kode lama, jadi kamu perlu bisa mengenalinya:",
                    "",
                    "  class Penyimpan:",
                    "      def simpan(self, kunci, nilai):",
                    "          raise NotImplementedError(\"turunan wajib menulis simpan()\")",
                    "",
                    "Bedanya dengan ABC:",
                    "",
                    "                      ABC + @abstractmethod   raise NotImplementedError",
                    "  ketahuannya         saat objek dibuat       saat method-nya dipanggil",
                    "  Penyimpan() polos   ditolak TypeError       berhasil, objek setengah jadi",
                    "  kelewat kalau       -                       method itu tak pernah dipanggil",
                    "",
                    "Makin cepat kesalahan ketahuan, makin murah memperbaikinya. Untuk kode",
                    "baru, pakai ABC. NotImplementedError tetap berguna untuk satu-dua method",
                    "di class yang bukan kontrak penuh.",
                    "",
                    "Jangan ketuker dua nama yang mirip ini. NotImplementedError adalah class",
                    "exception, dipakai bareng raise. NotImplemented (tanpa 'Error') adalah",
                    "nilai khusus yang dikembalikan dunder pembanding seperti __eq__ kalau",
                    "tipenya nggak cocok. Kalau kamu salah menulis raise NotImplemented,",
                    "pesan error-nya bikin bingung karena nggak menyebut nama itu sama",
                    "sekali:",
                    "  TypeError: exceptions must derive from BaseException",
                    "",
                    "Ada cara ketiga yang makin sering muncul di kode modern, dan bentuknya",
                    "beda jauh: typing.Protocol. Ini kontrak yang bahkan nggak menuntut",
                    "pewarisan.",
                ],
            },
            {
                "heading": "typing.Protocol: kontrak tanpa pewarisan",
                "code": "from typing import Protocol, runtime_checkable\n\n\n@runtime_checkable\nclass Pencetak(Protocol):\n    \"\"\"Kontrak: apa pun yang punya cetak(teks) sudah dianggap cocok.\"\"\"\n\n    def cetak(self, teks: str) -> None: ...\n\n\nclass Layar:                  # tidak mewarisi Pencetak, dan memang tidak perlu\n    def cetak(self, teks):\n        print(\"[layar]\", teks)\n\n\nclass Penampung:              # juga tidak menyebut Pencetak sama sekali\n    def __init__(self):\n        self.isi = []\n\n    def cetak(self, teks):\n        self.isi.append(teks)\n\n\ndef laporkan(keluaran: Pencetak, baris):\n    for b in baris:\n        keluaran.cetak(b)\n\n\nlaporkan(Layar(), [\"gaji: 100\", \"bonus: 20\"])\n\np = Penampung()\nlaporkan(p, [\"gaji: 100\", \"bonus: 20\"])\nprint(p.isi)\n\n# isinstance() hanya bekerja karena Protocol-nya diberi @runtime_checkable,\n# dan yang dicek cuma NAMA method-nya ada, bukan bentuk parameternya.\nprint(isinstance(Layar(), Pencetak))     # True\nprint(isinstance(3, Pencetak))           # False: int tidak punya cetak()\n\n# [layar] gaji: 100\n# [layar] bonus: 20\n# ['gaji: 100', 'bonus: 20']\n# True\n# False",
            },
            {
                "heading": "Protocol dibanding ABC, dan cara membaca ABC",
                "body": [
                    "Protocol ada di modul typing sejak Python 3.8, dan arah kontraknya",
                    "kebalikan dari ABC. Di ABC, class turunan harus menyebut nama induknya.",
                    "Di Protocol nggak perlu. Sebuah class dianggap memenuhi kontrak kalau",
                    "kebetulan punya method dengan nama dan bentuk yang cocok.",
                    "",
                    "Layar dan Penampung di atas nggak pernah menyebut Pencetak, tapi",
                    "dua-duanya sah dikirim ke laporkan(). Jadi Protocol itu duck typing yang",
                    "akhirnya bisa ditulis, nggak cuma dijanjikan di kepala orang yang",
                    "menulis kodenya.",
                    "",
                    "Kapan kamu butuh Protocol? Waktu class yang harus memenuhi kontrak itu",
                    "bukan milikmu. Misalnya class dari library orang lain, atau class yang",
                    "sudah terlanjur ditulis sebelum kontraknya ada. Kamu nggak bisa",
                    "menyuruhnya mewarisi apa pun, tapi kamu tetap mau kewajibannya tertulis",
                    "hitam di atas putih.",
                    "",
                    "Jebakan: Protocol dicek oleh pemeriksa tipe seperti mypy waktu kamu",
                    "menulis kode, bukan oleh Python waktu programnya jalan. Tanpa mypy,",
                    "anotasi Pencetak itu cuma catatan untuk manusia. Class yang nggak punya",
                    "cetak() tetap diterima, sampai akhirnya gagal dengan AttributeError.",
                    "ABC kebalikannya: Python sendiri yang memaksa aturannya.",
                    "",
                    "Ringkasnya:",
                    "",
                    "  duck typing polos tidak tertulis di mana pun; ketahuan saat error terjadi",
                    "  ABC               tertulis, DIPAKSA Python, turunan wajib menyebut induknya",
                    "  Protocol          tertulis, dicek mypy, class-nya tidak perlu tahu apa-apa",
                    "",
                    "Yang paling sering kamu perlukan justru cara membaca kode orang yang",
                    "memakai ABC:",
                    "",
                    "  - Begitu lihat class yang ditulis dengan (ABC), daftar",
                    "    @abstractmethod-nya adalah daftar method yang pasti ada di setiap",
                    "    objek bertipe itu. Itu peta tercepat untuk memahami sebuah modul.",
                    "  - Class ABC biasanya nggak mengerjakan pekerjaan aslinya. Untuk",
                    "    mencari class konkret yang mengerjakannya, cari nama induknya di",
                    "    dalam kurung:",
                    "      grep -rn \"(Penyimpan)\" .",
                    "    Kalau hasilnya tiga, berarti ada tiga cara berbeda yang bisa dipilih",
                    "    program.",
                    "  - Kalau sebuah fungsi menerima parameter bertipe Penyimpan, kamu",
                    "    langsung tahu apa saja yang boleh dilakukan padanya tanpa membuka",
                    "    satu pun implementasinya. Itu alasan kontrak ini ditulis dari awal.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi sekolah bisa mengirim pengumuman lewat email, SMS, atau",
                    "aplikasi pesan. Tiap saluran ditulis sebagai class sendiri, sering oleh",
                    "orang yang berbeda. ABC menuliskan kontraknya: setiap pengirim wajib",
                    "punya method kirim(), dan class yang lupa langsung ditolak.",
                    "",
                    "Kasus kecil: pengirim email dan SMS sudah jalan. Seorang anggota tim",
                    "baru menambah PengirimPesan, tapi lupa menulis kirim(). Kesalahan itu",
                    "harus ketahuan waktu objeknya dibuat, jangan di tengah pengumuman ke",
                    "ratusan wali murid.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan apa yang wajib dimiliki semua pengirim, yaitu",
                    "     kirim(tujuan, pesan).",
                    "  2. Tulis kontraknya sebagai ABC dengan @abstractmethod:",
                    "      from abc import ABC, abstractmethod",
                    "      class Pengirim(ABC):",
                    "          @abstractmethod",
                    "          def kirim(self, tujuan, pesan):",
                    "              ...",
                    "  3. Tiap saluran mewarisinya, misalnya class Email(Pengirim), lalu",
                    "     mengisi kirim(). Kode pengumuman cukup memanggil kirim() pada",
                    "     pengirim apa pun.",
                    "  4. Cek kasus pinggir: class PengirimPesan(Pengirim) tanpa kirim().",
                    "     Baris PengirimPesan() langsung gagal dengan TypeError yang menyebut",
                    "     method kirim, sebelum satu pesan pun terkirim.",
                    "",
                    "Jebakan: lupa menulis (ABC) di class Pengirim. @abstractmethod jadi",
                    "nggak berbuat apa-apa, dan class yang belum lengkap lolos tanpa error.",
                ]
            },
        ],
    },
    {
        "title": "24. OOP: Encapsulation & Dunder Methods",
        "sections": [
            {
                "body": [
                    "Encapsulation artinya menyembunyikan isi sebuah objek supaya nggak",
                    "diutak-atik sembarangan dari luar. Java punya keyword private, public,",
                    "dan protected untuk itu. Python nggak punya keyword semacam itu yang",
                    "dipaksakan. Yang dipakai adalah kesepakatan lewat nama",
                    "atribut:",
                    "",
                    "  - nama_biasa artinya public. Ini bawaannya, bebas diakses dari mana",
                    "    aja.",
                    "  - _nama_protect, diawali satu garis bawah, artinya 'protected'.",
                    "    Maksudnya: tolong jangan diakses dari luar class. Tapi Python nggak",
                    "    memaksanya. Ini cuma etika kode antar programmer.",
                    "  - __nama_privat, diawali dua garis bawah, artinya 'private'. Python",
                    "    melakukan name mangling, yaitu mengganti namanya jadi",
                    "    _NamaClass__nama_privat. Tujuannya supaya atribut itu susah diakses",
                    "    dari luar secara nggak sengaja.",
                    "",
                    "Lalu ada property. Ini cara gaya Python untuk bikin getter dan setter,",
                    "yaitu fungsi untuk membaca dan mengubah atribut. Kelebihannya, cara",
                    "pakainya nggak berubah: dari luar tetap kelihatan seperti akses atribut",
                    "biasa.",
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
                "heading": "Asal @saldo.setter dan raise di dalam setter",
                "body": [
                    "Ada dua baris di contoh itu yang perlu dibongkar, karena dua-duanya",
                    "muncul tanpa pernah diperkenalkan.",
                    "",
                    "Yang pertama: dari mana nama @saldo.setter datang? @property nggak cuma",
                    "menandai fungsinya. Dia mengganti fungsi saldo dengan sebuah objek",
                    "property, dan objek itu punya .setter dan .deleter. Jadi @saldo.setter",
                    "dibaca 'pakai .setter milik property bernama saldo'. Akibatnya:",
                    "",
                    "  - Nama decorator-nya selalu mengikuti nama fungsi di atasnya. Untuk",
                    "    @property def harga, pasangannya @harga.setter.",
                    "  - @property harus ditulis lebih dulu. Kalau getter-nya belum ada,",
                    "    @saldo.setter nggak punya apa pun untuk disambung.",
                    "  - Getter dan setter wajib sama namanya. Kalau setter-nya dikasih nama",
                    "    set_saldo, yang lahir malah property kedua bernama set_saldo.",
                    "    Sementara itu saldo tetap cuma bisa dibaca. Begitu kamu menulis",
                    "    r.saldo = 0, Python menolak dengan",
                    "    AttributeError: property 'saldo' of 'Rekening' object has no setter",
                    "    dan pesannya nggak menyinggung soal salah nama sama sekali.",
                    "  - Ada juga @saldo.deleter untuk del r.saldo, tapi ini jauh lebih",
                    "    jarang dipakai.",
                    "",
                    "Yang kedua: raise ValueError(...) di dalam setter itu artinya lempar",
                    "error dan hentikan penugasan saat itu juga. Baris self._saldo = nilai di",
                    "bawahnya nggak pernah dijalankan, jadi r.saldo tetap berisi nilai lama.",
                    "Karena itulah validasinya mengikat. Ini bukan peringatan yang boleh",
                    "dilewati. Soal raise, jenis-jenis error, dan cara menangkapnya dibahas",
                    "lengkap di materi Exception Handling.",
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
                "heading": "Dunder method lain dan __slots__",
                "body": [
                    "Dunder method lain yang umum dipakai:",
                    "  __len__(self)       -> dipanggil oleh len(objek)",
                    "  __getitem__(self,i) -> dipanggil oleh objek[i]",
                    "  __iter__(self)      -> membuat objek bisa di-for-loop",
                    "  __lt__, __gt__      -> dipanggil oleh operator < dan >",
                    "  __call__(self)      -> membuat objek bisa 'dipanggil' seperti fungsi",
                    "",
                    "Berikutnya __slots__. Ini satu baris di bagian paling atas badan class",
                    "yang mengunci daftar atribut yang boleh dimiliki objeknya.",
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
                    "padahal kerjanya beda. Dengan __slots__, Python nggak perlu menyiapkan",
                    "kamus atribut untuk tiap objek, jadi objeknya jauh lebih hemat memori.",
                    "Makanya __slots__ sering muncul di kode yang bikin jutaan objek kecil.",
                    "",
                    "Efek sampingnya malah sering paling berguna: salah ketik nama atribut",
                    "langsung ketahuan. Tanpa __slots__, salah ketik cuma bikin atribut baru",
                    "yang nggak pernah dibaca siapa pun, tanpa pesan apa-apa.",
                    "",
                    "Harganya, atribut di luar daftar itu nggak bisa ditambahkan belakangan.",
                    "Jadi pakai __slots__ cuma kalau memang butuh. Untuk keperluan biasa,",
                    "class biasa tetap pilihan utama.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi gudang dan rekening bank punya aturan yang nggak boleh",
                    "dilanggar: stok dan saldo nggak boleh negatif. Daripada berharap tiap",
                    "programmer ingat memeriksanya, aturan itu dipasang di objeknya sendiri",
                    "lewat property. Siapa pun yang mengubah nilainya otomatis lewat",
                    "pemeriksaan yang sama.",
                    "",
                    "Kasus kecil: stok sabun di gudang tinggal 10. Petugas salah ketik dan",
                    "mencatat pengambilan 15, sehingga stok jadi -5. Program harus menolak",
                    "perubahan itu dan membiarkan stok tetap 10.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Rumuskan aturannya: stok harus >= 0 setiap saat, termasuk waktu",
                    "     objeknya pertama dibuat.",
                    "  2. Simpan angkanya di self._stok, lalu buka lewat @property stok yang",
                    "     cuma mengembalikan self._stok.",
                    "  3. Pasang pemeriksaannya di setter:",
                    "          @stok.setter",
                    "          def stok(self, nilai):",
                    "              if nilai < 0:",
                    "                  raise ValueError(\"stok tidak boleh negatif\")",
                    "              self._stok = nilai",
                    "  4. Cek kasus pinggir. Stok tepat 0 harus boleh, makanya syaratnya",
                    "     < 0. Lalu coba sabun.stok -= 15. ValueError muncul, dan",
                    "     sabun.stok tetap 10.",
                    "",
                    "Jebakan: kalau __init__ menulis self._stok = stok, Barang(-5) lolos",
                    "karena setter-nya dilewati. Tulis self.stok = stok di __init__.",
                ]
            },
        ],
    },
    {
        "title": "25. dataclass & Enum",
        "sections": [
            {
                "body": [
                    "Kebanyakan class di kode nyata nggak pintar. Tugasnya cuma membawa",
                    "data. Contohnya Titik, Produk, Konfigurasi, atau satu baris hasil query",
                    "dari database. Isinya beberapa atribut, dan hampir nggak ada",
                    "perilakunya.",
                    "",
                    "Kalau ditulis dengan cara materi Encapsulation & Dunder Methods, class",
                    "seperti itu jadi panjang karena __init__, __repr__, dan __eq__. Isinya",
                    "selalu bisa ditebak: sebut nama field, ulangi lagi, lalu ulangi lagi.",
                    "Daftar yang sama ditulis tiga kali. Kalau satu field lupa disalin ke",
                    "salah satunya, bug-nya susah banget kelihatan.",
                    "",
                    "@dataclass menuliskan method-method itu untukmu. Dia ada di modul bawaan",
                    "dataclasses sejak Python 3.7. Kamu cukup menyebut atribut apa aja yang",
                    "dimiliki class ini, sekali aja.",
                    "",
                    "Bentuknya beda jauh dari class biasa, jadi kenali baik-baik:",
                    "",
                    "  from dataclasses import dataclass",
                    "",
                    "  @dataclass",
                    "  class Produk:",
                    "      nama: str",
                    "      harga: int",
                    "      stok: int = 0",
                    "",
                    "Nggak ada def __init__ sama sekali. Waktu pertama kali membaca kode",
                    "seperti ini, gampang banget menyimpulkan 'class ini nggak punya",
                    "constructor'. Kesimpulan itu salah. Constructor-nya dibikinkan, persis",
                    "dari tiga baris itu, jadi Produk(\"Kopi\", 25000) langsung bisa dipanggil.",
                    "",
                    "Tiga baris nama: str, harga: int, dan stok: int = 0 itu anotasi tipe",
                    "(lihat materi Anotasi Tipe (Type Hint)). Bedanya, di sini anotasinya",
                    "punya tugas. @dataclass membaca daftar anotasi di badan class untuk tahu",
                    "ada field apa aja.",
                    "",
                    "Akibatnya bisa bikin kaget. Atribut yang ditulis tanpa anotasi nggak",
                    "dianggap field. Dia nggak muncul di __init__, dan cuma jadi class",
                    "attribute biasa (lihat materi Class & Object):",
                    "",
                    "  @dataclass",
                    "  class Produk:",
                    "      nama: str       # field: masuk __init__",
                    "      pajak = 0.11    # BUKAN field, cuma class attribute - gampang salah kira",
                    "",
                    "Tipe yang ditulis tetap nggak dipaksakan Python. Produk(123, \"mahal\")",
                    "tetap jalan. Yang dipakai @dataclass cuma ada atau nggaknya anotasi,",
                    "bukan isinya.",
                    "",
                    "Yang dibikinkan untukmu ada tiga:",
                    "",
                    "  - __init__, yang parameternya berurutan persis seperti urutan field di",
                    "    badan class.",
                    "  - __repr__, supaya print(objek) menampilkan isinya, bukan alamat",
                    "    memori.",
                    "  - __eq__, supaya == membandingkan isi field, bukan 'objek yang sama",
                    "    persis'.",
                    "",
                    "Dari ketiganya, __eq__ yang paling sering menolong. Tanpa __eq__, dua",
                    "objek yang datanya sama persis tetap dianggap nggak sama. Ini juga",
                    "kejadian waktu kamu membandingkan hasil di dalam tes, dan bikin bingung",
                    "karena dua objek itu kelihatan sama.",
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
                "heading": "Lima aturan dan jebakan @dataclass",
                "body": [
                    "Ada beberapa aturan main dan jebakan @dataclass yang perlu kamu tahu",
                    "sebelum memakainya.",
                    "",
                    "Aturan 1: field yang punya nilai default harus ditulis di belakang field",
                    "yang nggak punya default. Alasannya sama dengan parameter fungsi, karena",
                    "__init__ yang dibikinkan memang fungsi biasa. Kalau urutannya terbalik,",
                    "class-nya gagal waktu berkasnya diimpor, belum nunggu objeknya dibikin:",
                    "",
                    "  @dataclass",
                    "  class Keranjang:",
                    "      diskon: float = 0.0",
                    "      pemilik: str",
                    "  TypeError: non-default argument 'pemilik' follows default argument 'diskon'",
                    "",
                    "Aturan 2: default yang mutable dilarang, dan larangannya tegas. Mutable",
                    "artinya isinya bisa diubah, seperti list, dict, dan set.",
                    "",
                    "  @dataclass",
                    "  class Keranjang:",
                    "      pemilik: str",
                    "      isi: list = []",
                    "  ValueError: mutable default <class 'list'> for field isi is not allowed:",
                    "  use default_factory",
                    "",
                    "Ini jebakan yang sama dengan def f(x=[]) di materi Referensi Objek,",
                    "Salinan & Jebakan Mutable. Badan class dijalankan sekali aja, jadi satu",
                    "list itu bakal dipakai bareng oleh semua objek dan isinya menumpuk.",
                    "Bedanya, di fungsi Python nggak protes, dan kamu baru sadar setelah",
                    "datanya bocor. Di dataclass, Python menolak dari awal. Perbaikannya:",
                    "",
                    "  isi: list = field(default_factory=list)  # dict, set, atau lambda juga boleh",
                    "",
                    "default_factory adalah fungsi yang dipanggil ulang setiap kali objek",
                    "dibikin. Tulis namanya aja (list), tanpa tanda kurung, karena yang",
                    "diminta fungsinya. Untuk default yang immutable, artinya nggak bisa",
                    "diubah, seperti 0, \"\", None, atau True, cukup tulis biasa: stok: int = 0.",
                    "",
                    "Aturan 3: frozen=True bikin objeknya nggak bisa diubah setelah dibikin.",
                    "Menulis ke field-nya melempar FrozenInstanceError. Bonusnya, objeknya",
                    "jadi hashable, jadi bisa dipakai sebagai key dict atau anggota set.",
                    "Dataclass biasa malah nggak bisa. Begitu __eq__ dibikinkan, Python",
                    "mematikan __hash__ bawaannya, dan {Titik(1, 2)} berakhir dengan",
                    "TypeError yang menyebut unhashable type.",
                    "",
                    "Jebakan: frozen cuma mengunci lapisan luarnya. Kalau salah satu field",
                    "berisi list, isi list itu tetap bisa di-append, persis seperti salinan",
                    "dangkal di materi Referensi Objek. Frozen artinya labelnya nggak bisa",
                    "dipindah. Isinya sendiri nggak ikut dibekukan.",
                    "",
                    "Aturan 4: order=True menghidupkan < > <= >= dengan membandingkan field",
                    "satu per satu sesuai urutannya, seperti tuple. Jadi urutan penulisan",
                    "field ikut menentukan cara mengurutkan. Misalnya field pertamamu 'nama',",
                    "padahal yang mau kamu urutkan 'harga'. sorted() bakal mengurutkan",
                    "berdasarkan nama tanpa protes. field(compare=False) mengeluarkan satu",
                    "field dari __eq__ dan dari pengurutan.",
                    "",
                    "Aturan 5: ada beberapa alat pendukung yang sering muncul:",
                    "",
                    "  asdict(objek)        -> dict, menembus sampai ke dataclass di dalamnya",
                    "  astuple(objek)       -> tuple",
                    "  replace(objek, x=9)  -> objek BARU dengan sebagian field diganti; ini satu-",
                    "                          satunya cara 'mengubah' objek frozen",
                    "  field(init=False)    -> field yang TIDAK jadi parameter __init__",
                    "  __post_init__(self)  -> dipanggil otomatis setelah __init__ selesai; tempat",
                    "                          memvalidasi atau menghitung field turunan",
                    "",
                    "  @dataclass",
                    "  class Lingkaran:",
                    "      jari: float",
                    "      luas: float = field(init=False)",
                    "      def __post_init__(self):",
                    "          if self.jari <= 0:",
                    "              raise ValueError(\"jari harus positif\")",
                    "          self.luas = 3.14159 * self.jari ** 2",
                    "",
                    "Sekarang masalah kedua, yang masih tetangga dekat dataclass.",
                    "",
                    "Materi Variabel & Tipe Data mengajarkan konstanta sebagai kebiasaan",
                    "menulis nama dengan huruf besar semua, seperti PI = 3.14159. Cara itu",
                    "cukup untuk satu nilai tetap. Yang belum tertangani adalah sekumpulan",
                    "nilai tetap yang saling berkaitan. Misalnya status pesanan, peran",
                    "pengguna, level log, atau jenis pembayaran. Cara paling polosnya adalah",
                    "menyebar string mentah ke seluruh kode:",
                    "",
                    "  if status == \"dikirim\": ...",
                    "  pesanan[\"status\"] = \"selesai\"",
                    "",
                    "Masalahnya, salah ketik nggak ketahuan. Kalau kamu mengetik \"dikirin\",",
                    "Python nggak protes. Perbandingannya cuma menghasilkan False, cabang if",
                    "itu nggak pernah jalan, dan programnya tetap jalan dengan hasil yang",
                    "salah. Nggak ada yang menahanmu: Python nggak, editor nggak, mypy juga",
                    "nggak.",
                    "",
                    "Enum dari modul bawaan enum menutup celah itu. Enum adalah class yang",
                    "anggotanya tetap dan terbatas, dan tiap anggota punya nama dan nilai.",
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
                "heading": "Anggota Enum, jebakan, IntEnum, dan StrEnum",
                "body": [
                    "Yang perlu kamu pegang soal Enum:",
                    "",
                    "  - Status.DIKIRIM adalah anggotanya sendiri. Anggota ini yang",
                    "    dioper ke mana-mana.",
                    "  - .name berisi \"DIKIRIM\", yaitu teks nama anggotanya.",
                    "  - .value berisi \"dikirim\", yaitu nilai yang kamu tulis di sebelah",
                    "    kanan.",
                    "  - is dipakai untuk membandingkan anggota Enum. == juga benar, tapi is",
                    "    lebih tegas dan nggak bisa ketipu oleh nilai yang mirip.",
                    "  - auto() minta Python mengisi nilainya sendiri: 1, 2, 3, dan",
                    "    seterusnya.",
                    "  - @unique adalah decorator dari modul enum. Dia melarang dua anggota",
                    "    punya nilai yang sama.",
                    "",
                    "Jebakan: anggota Enum itu beda dengan string-nya.",
                    "",
                    "  Status.DIKIRIM == \"dikirim\"     -> False, dan Python tidak protes",
                    "",
                    "Bayangkan kode yang baru setengah dipindah ke Enum. Sebagian sudah",
                    "memakai Status.DIKIRIM, sebagian lagi masih membandingkan dengan string",
                    "mentah. Kode itu bakal jalan tanpa error, tapi hasilnya salah terus.",
                    "Kalau kamu butuh string aslinya, minta secara jelas lewat .value.",
                    "",
                    "Alasan yang sama bikin json.dumps({\"status\": Status.DIKIRIM}) gagal",
                    "dengan TypeError: Object of type Status is not JSON serializable. Yang",
                    "dikirim seharusnya .value-nya.",
                    "",
                    "Jebakan kedua: dua anggota yang nilainya sama nggak jadi dua anggota.",
                    "Anggota kedua otomatis jadi alias, yaitu nama lain untuk anggota",
                    "pertama. Akibatnya dia nggak muncul waktu Enum-nya diiterasi, dan",
                    ".name-nya berubah jadi nama anggota pertama. Kalau kamu mau hal ini",
                    "ditolak sebagai kesalahan, pasang @unique di atas class-nya.",
                    "",
                    "Jebakan ketiga: jangan simpan nilai auto() ke database. auto() memberi",
                    "1, 2, 3 sesuai urutan penulisan. Kalau kamu menyisipkan satu anggota",
                    "baru di tengah, nomor semua anggota sesudahnya ikut bergeser. Akibatnya",
                    "semua baris lama di database tiba-tiba menunjuk status yang berbeda.",
                    "Untuk nilai yang ikut disimpan, tulis nilainya sendiri, misalnya",
                    "\"dikirim\" atau 3, dan anggap nilai itu nggak boleh diubah lagi.",
                    "",
                    "Ada dua varian yang sering kamu temui:",
                    "",
                    "  - IntEnum: anggotanya betul-betul int, jadi Level.TINGGI > 2 dan",
                    "    Level.RENDAH + 1 bisa jalan. Dipakai untuk hal yang memang punya",
                    "    tingkatan, seperti level log atau kode HTTP.",
                    "  - StrEnum (Python 3.11 ke atas): anggotanya betul-betul str, jadi",
                    "    Warna.MERAH == \"merah\" hasilnya True, .upper() bisa jalan, dan",
                    "    json.dumps langsung menghasilkan \"merah\".",
                    "",
                    "Sebelum 3.11, orang menulis  class Warna(str, Enum):  untuk efek yang",
                    "hampir sama, dan bentuk ini masih banyak di kode yang beredar. Bedanya",
                    "satu: pada StrEnum, f\"{Warna.MERAH}\" menghasilkan merah, sedangkan pada",
                    "(str, Enum) hasilnya Warna.MERAH.",
                    "",
                    "IntEnum dan StrEnum menukar keamanan dengan kenyamanan. Karena anggotanya",
                    "bisa disamakan dengan int atau str biasa, salah ketik jadi bisa lolos",
                    "lagi. Mulailah dengan Enum polos. Pindah ke IntEnum atau StrEnum cuma",
                    "kalau nilainya memang harus keluar-masuk sistem lain.",
                    "",
                    "Satu intipan ke depan, supaya nanti nggak asing. Di project FastAPI",
                    "(disebut di materi Roadmap), berkas pertama yang kamu buka biasanya",
                    "berisi ini:",
                    "",
                    "  from pydantic import BaseModel",
                    "",
                    "  class Produk(BaseModel):",
                    "      nama: str",
                    "      harga: int = 0",
                    "",
                    "Bentuknya hampir sama dengan @dataclass, dan alasannya juga sama: field",
                    "ditentukan lewat anotasi tipe di badan class. Bedanya satu, dan besar:",
                    "pydantic memeriksa tipenya waktu objek dibikin, lalu menolak data yang",
                    "nggak cocok. Alasannya, datanya datang dari internet dan nggak boleh",
                    "langsung dipercaya. @dataclass nggak memeriksa apa pun.",
                    "",
                    "Enum juga dipakai langsung di sana sebagai tipe field. FastAPI mengubahnya",
                    "jadi daftar nilai yang sah di dokumentasi API yang dia bikin otomatis.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kurir dan toko online menyimpan tiap pesanan sebagai objek data",
                    "sederhana, yang cocok ditulis dengan @dataclass. Statusnya cuma boleh",
                    "salah satu dari beberapa nilai tetap, seperti dikemas, dikirim, dan",
                    "selesai, dan di situlah Enum dipakai. Salah ketik nama status langsung",
                    "ketahuan, jadi pesanan nggak nyangkut di status yang nggak ada.",
                    "",
                    "Kasus kecil: database mengirim status pesanan hari ini sebagai teks:",
                    "[\"dikirim\", \"selesai\", \"dikirim\"]. Admin gudang ingin tahu berapa",
                    "pesanan yang masih di jalan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya list teks status. Keluarannya satu angka, jumlah",
                    "     pesanan berstatus dikirim.",
                    "  2. Daftarkan semua status yang sah sebagai Enum, lalu ubah tiap teks",
                    "     jadi anggotanya dengan Status(teks):",
                    "      from enum import Enum",
                    "      class Status(Enum):",
                    "          DIKIRIM = \"dikirim\"",
                    "          SELESAI = \"selesai\"",
                    "      data = [\"dikirim\", \"selesai\", \"dikirim\"]",
                    "      print(len([t for t in data if Status(t) is Status.DIKIRIM]))",
                    "  3. Jalankan. Hasilnya 2.",
                    "  4. Cek kasus pinggir: teks yang salah ketik, misalnya \"dikirin\".",
                    "     Status(\"dikirin\") langsung melempar ValueError, jadi data rusak",
                    "     ketahuan di baris pengubahnya.",
                    "",
                    "Jebakan: anggota Enum nggak sama dengan teksnya. Status(\"dikirim\") ==",
                    "\"dikirim\" hasilnya False. Kalau butuh teksnya, ambil lewat .value.",
                ]
            },
        ],
    },
    {
        "title": "26. Exception Handling",
        "sections": [
            {
                "body": [
                    "Exception adalah error yang terjadi waktu program sedang jalan. Kalau",
                    "nggak ditangani, program langsung berhenti. Istilahnya crash.",
                    "",
                    "Ini beberapa exception bawaan Python yang paling sering kamu temui,",
                    "beserta contoh penyebabnya:",
                    "  ZeroDivisionError    -> 10 / 0",
                    "  IndexError           -> list[99] padahal list kecil",
                    "  KeyError             -> dict[\"tidak_ada\"]",
                    "  TypeError            -> \"5\" + 5 (tipe tak cocok)",
                    "  ValueError           -> int(\"abc\") (gagal konversi)",
                    "  FileNotFoundError    -> buka file yang tidak ada",
                    "  AttributeError       -> objek.method_tidak_ada()",
                    "",
                    "Untuk menangani exception, Python memakai try-except. Bentuk lengkapnya",
                    "seperti ini:",
                    "  try:",
                    "      # kode yang mungkin error",
                    "  except TipeError as e:",
                    "      # penanganan error",
                    "  else:",
                    "      # jalan HANYA jika TIDAK ada error",
                    "  finally:",
                    "      # SELALU jalan, error atau tidak",
                    "",
                    "Kode yang mungkin gagal ditaruh di blok try. Kalau error-nya terjadi,",
                    "Python lompat ke blok except yang jenisnya cocok. Blok else cuma jalan",
                    "kalau nggak ada error sama sekali. Blok finally selalu jalan, mau ada",
                    "error atau nggak.",
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
                "heading": "Menangkap banyak jenis, raise, dan EAFP",
                "body": [
                    "Kamu bisa menangkap beberapa jenis exception sekaligus. Caranya, tulis",
                    "jenis-jenisnya di dalam kurung:",
                    "  except (ZeroDivisionError, TypeError) as e:",
                    "      print(f\"Error: {e}\")",
                    "",
                    "Kamu juga bisa melempar exception dengan sengaja pakai raise. Biasanya",
                    "dipakai waktu datanya nggak masuk akal:",
                    "  if umur < 0:",
                    "      raise ValueError(\"Umur tidak boleh negatif\")",
                    "",
                    "Kalau jenis bawaan kurang pas, bikin exception sendiri. Caranya, bikin",
                    "class turunan dari Exception:",
                    "  class SaldoTidakCukup(Exception):",
                    "      pass",
                    "",
                    "  raise SaldoTidakCukup(\"Saldo kurang untuk transaksi ini\")",
                    "",
                    "Terakhir, ada dua gaya menangani error yang sering disebut di dunia",
                    "Python: EAFP dan LBYL.",
                    "",
                    "EAFP singkatan dari Easier to Ask Forgiveness than Permission, artinya",
                    "lebih gampang minta maaf daripada minta izin. Langsung coba aja, lalu",
                    "tangani kalau gagal. Ini gaya yang lazim di Python:",
                    "      try:",
                    "          nilai = data[\"key\"]",
                    "      except KeyError:",
                    "          nilai = default",
                    "",
                    "LBYL singkatan dari Look Before You Leap, artinya lihat dulu sebelum",
                    "melompat. Cek dulu kondisinya, baru jalankan. Gaya ini lebih defensif:",
                    "      if \"key\" in data:",
                    "          nilai = data[\"key\"]",
                    "      else:",
                    "          nilai = default",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program yang membaca data dari orang atau dari berkas pasti ketemu",
                    "isian yang salah: huruf di kolom angka, sel yang kosong, atau tanda",
                    "titik yang nyasar. Program rekap keuangan UMKM nggak boleh berhenti",
                    "cuma karena satu baris rusak. Baris itu dilewati, dicatat, lalu",
                    "pekerjaannya jalan terus.",
                    "",
                    "Kasus kecil: setoran harian kasir tercatat sebagai teks [\"15000\",",
                    "\"20000\", \"abc\", \"\", \"7500\"]. Pemilik toko butuh total setoran yang sah,",
                    "dan berapa baris yang ditolak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya list teks. Keluarannya total dan jumlah baris yang",
                    "     ditolak.",
                    "  2. Kerjakan int() satu per satu, dan tangkap ValueError di dalam loop,",
                    "     supaya satu baris rusak nggak menghentikan baris lain:",
                    "      total, ditolak = 0, 0",
                    "      for teks in setoran:",
                    "          try:",
                    "              total += int(teks)",
                    "          except ValueError:",
                    "              ditolak += 1",
                    "  3. Jalankan. Totalnya 42500, dan baris yang ditolak 2.",
                    "  4. Cek kasus pinggir: string kosong. int(\"\") juga ValueError, jadi",
                    "     sudah ikut tertangkap tanpa cabang tambahan.",
                    "",
                    "Jebakan: menangkap dengan except kosong ikut menelan error lain yang",
                    "bukan urusannya. Sebut jenisnya, ValueError, supaya kesalahan lain",
                    "tetap kelihatan.",
                ]
            },
        ],
    },
    {
        "title": "27. Membaca Traceback & Menangkap Error Secara Luas",
        "sections": [
            {
                "body": [
                    "Traceback adalah teks yang dicetak Python waktu programmu berhenti",
                    "karena error yang nggak ditangani. Teks ini yang paling sering dibaca",
                    "programmer, jauh lebih sering daripada kode orang lain.",
                    "",
                    "Pemula biasanya melihatnya sebagai tembok tulisan merah, lalu",
                    "menebak-nebak sendiri. Padahal traceback itu laporan dengan format",
                    "tetap, dan isinya hampir selalu sudah memuat jawabannya.",
                    "",
                    "Bentuknya selalu seperti ini:",
                    "",
                    "  Traceback (most recent call last):",
                    "    File \"program.py\", line 24, in <module>        <- frame paling LUAR",
                    "      print(\"Rata-rata umur:\", rata_rata_umur(data))",
                    "    File \"program.py\", line 12, in rata_rata_umur  <- dipanggil yang di atas",
                    "      orang = baca_baris(baris)",
                    "    File \"program.py\", line 6, in baca_baris       <- frame paling DALAM",
                    "      return {\"nama\": nama, \"umur\": int(umur)}",
                    "  ValueError: invalid literal for int() with base 10: 'tiga puluh'",
                    "",
                    "Bagian-bagiannya:",
                    "",
                    "  - 'most recent call last' artinya panggilan terbaru ada di paling",
                    "    bawah. Ini petunjuk cara bacanya: traceback dibaca dari bawah ke",
                    "    atas.",
                    "  - Tiap pasang baris adalah satu frame, yaitu satu fungsi yang sedang",
                    "    jalan waktu error terjadi. Baris pertama menyebut berkas, nomor",
                    "    baris, dan nama fungsinya. Baris kedua menampilkan isi baris kode",
                    "    itu.",
                    "  - <module> artinya kode itu ada di tingkat paling atas berkas, nggak",
                    "    di dalam fungsi mana pun.",
                    "  - Baris terakhir adalah intinya, bentuknya 'JenisError: pesan'. Baca",
                    "    baris ini lebih dulu.",
                    "  - Python 3.11 ke atas menambahkan penanda ~~~^^^ di bawah baris kode.",
                    "    Penanda itu menunjuk bagian ekspresi yang gagal dengan persis. Di",
                    "    Python versi lama, penanda ini nggak ada.",
                    "",
                    "Urutan membacanya:",
                    "",
                    "  1. Baris paling bawah: error-nya apa, pesannya apa.",
                    "  2. Frame paling bawah: baris mana yang sedang jalan waktu itu.",
                    "  3. Naik ke atas: siapa memanggil siapa. Kalau tumpukannya penuh",
                    "     berkas library (site-packages), error-nya hampir selalu berasal",
                    "     dari data yang kamu kirim ke library itu. Jadi cari frame terakhir",
                    "     yang berkasnya milikmu.",
                    "  4. Baru sesudah itu buka baris yang ditunjuk.",
                    "",
                    "Jebakan: baris yang ditunjuk adalah baris yang sedang jalan, belum",
                    "tentu baris yang salah. Traceback menunjuk tempat kejadiannya, belum",
                    "tentu tempat kesalahannya. Untuk menemukan sumber aslinya, lihat pesan",
                    "error-nya, terutama potongan nilai yang bikin gagal.",
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
                "heading": "Silsilah exception dan menangkap secara luas",
                "body": [
                    "Sekarang sisi menangkap error. Materi Exception Handling mengajarkan",
                    "cara menangkap satu jenis error yang sudah kamu duga. Di kode nyata,",
                    "kamu butuh dua hal lagi: menangkap satu keluarga error sekaligus, dan",
                    "memasang satu jaring pengaman di batas program.",
                    "",
                    "Semua exception di Python adalah class, dan class-class itu punya",
                    "silsilah:",
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
                    "Dari silsilah itu muncul satu aturan: 'except X' menangkap X beserta",
                    "semua turunannya. 'except LookupError' ikut menangkap KeyError dan",
                    "IndexError. 'except Exception' menangkap hampir semuanya. Exception",
                    "bikinanmu sendiri juga turunan Exception, jadi ikut tertangkap. Itu",
                    "memang yang diharapkan.",
                    "",
                    "Akibatnya, urutan blok except jadi penting. Python mencoba blok dari",
                    "atas ke bawah, lalu memakai blok pertama yang cocok. Kalau",
                    "'except Exception' ditaruh paling atas, semua blok di bawahnya jadi kode",
                    "mati, yaitu kode yang nggak pernah bisa dijalankan. Python nggak",
                    "memperingatkan apa pun soal ini. Jadi taruh yang paling spesifik di",
                    "atas, dan jaring yang paling luas di paling bawah.",
                    "",
                    "Ringkasnya, dari yang paling sempit sampai yang paling luas:",
                    "",
                    "  - except ValueError: menangkap ValueError saja. Dipakai untuk kasus",
                    "    yang kamu antisipasi.",
                    "  - except LookupError: menangkap KeyError, IndexError, dan saudaranya.",
                    "    Dipakai untuk satu keluarga sekaligus.",
                    "  - except Exception as e: menangkap semua error 'biasa'. Dipakai di",
                    "    batas program, sebelum retry (mencoba ulang), atau untuk log.",
                    "  - except BaseException: ikut menangkap Ctrl+C dan sys.exit(). Hampir",
                    "    nggak pernah dipakai.",
                    "  - except: sama aja dengan BaseException. Jangan dipakai.",
                    "",
                    "'except:' tanpa nama jenis error (sering disebut except telanjang) itu",
                    "berbahaya. Dia sama dengan 'except BaseException', jadi ikut menelan",
                    "KeyboardInterrupt dan SystemExit. Akibatnya Ctrl+C nggak lagi",
                    "menghentikan program, dan sys.exit() di dalam blok itu nggak jadi",
                    "keluar. Dua hal itu bukan error. Dua-duanya perintah untuk berhenti.",
                    "'except Exception' nggak menyentuh keduanya, makanya itu bentuk yang",
                    "benar kalau kamu mau menangkap secara luas.",
                    "",
                    "Menangkap secara luas cuma pantas di tempat yang bisa berbuat sesuatu",
                    "dengan error-nya. Misalnya di batas program (fungsi main), di satu",
                    "putaran pekerjaan yang boleh gagal sendirian, atau sebelum mencoba",
                    "ulang. Syaratnya dua: pesannya dicatat lengkap dengan traceback-nya,",
                    "lalu error itu ditangani atau dilempar ulang.",
                    "",
                    "'except Exception: pass' adalah cara tercepat bikin bug yang nggak bisa",
                    "dilacak. Programmu nggak protes, hasilnya salah, dan nggak ada jejak",
                    "apa pun yang tertinggal.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Skrip yang jalan tiap malam untuk memproses ratusan pesanan nggak boleh",
                    "berhenti gara-gara satu pesanan aneh. Pola yang dipakai di kode nyata:",
                    "setiap putaran dibungkus except Exception, error-nya dicatat lengkap,",
                    "lalu loop lanjut ke pesanan berikutnya. Paginya, programmer membaca",
                    "catatan itu dari baris paling bawah.",
                    "",
                    "Kasus kecil: tiga pesanan masuk. Pesanan P1 berisi jumlah \"2\", P2",
                    "berisi jumlah \"x\", dan P3 lupa mencantumkan jumlah sama sekali. Fungsi",
                    "proses(p) mengubah p[\"jumlah\"] jadi int. Pesanan yang sehat harus tetap",
                    "diproses.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan sekali tanpa penangkap, lalu baca traceback-nya dari",
                    "     bawah. Baris terakhir menyebut jenis error dan nilai yang bikin",
                    "     gagal.",
                    "  2. Tentukan batasnya: satu pesanan boleh gagal sendirian. Jadi",
                    "     try diletakkan di dalam loop, bukan di luar loop:",
                    "      gagal = []",
                    "      for p in pesanan:",
                    "          try:",
                    "              proses(p)",
                    "          except Exception as e:",
                    "              gagal.append((p.get(\"kode\"), repr(e)))",
                    "  3. Jalankan. P1 lolos, sedangkan gagal berisi P2 dengan ValueError dan",
                    "     P3 dengan KeyError('jumlah'). Dua jenis error berbeda tertangkap",
                    "     oleh satu except Exception.",
                    "  4. Cek kasus pinggir: tekan Ctrl+C waktu loop berjalan. Programnya",
                    "     tetap berhenti, karena KeyboardInterrupt bukan turunan Exception.",
                    "",
                    "Jebakan: except Exception: pass membuang semua jejak. Selalu simpan",
                    "repr(e), atau catat traceback-nya dengan traceback.format_exc().",
                ]
            },
        ],
    },
    {
        "title": "28. Module & Package",
        "sections": [
            {
                "body": [
                    "Module adalah satu berkas .py yang berisi fungsi, class, atau variabel.",
                    "Isinya bisa di-import, lalu dipakai ulang di berkas lain.",
                    "",
                    "Package adalah folder yang berisi banyak module. Folder itu ditandai",
                    "dengan berkas __init__.py di dalamnya.",
                    "",
                    "Ada beberapa cara import:",
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
                "heading": "Module sendiri, idiom __main__, dan pip",
                "body": [
                    "Bikin module sendiri itu gampang. Setiap berkas .py yang kamu tulis",
                    "sudah otomatis jadi module:",
                    "  # file kalkulator.py",
                    "  def tambah(a, b):",
                    "      return a + b",
                    "",
                    "  # file main.py (folder yang sama)",
                    "  import kalkulator",
                    "  print(kalkulator.tambah(3, 4))   # 7",
                    "",
                    "Satu idiom yang bakal kamu lihat di hampir semua berkas Python adalah",
                    "if __name__ == \"__main__\":. Kode di dalam blok ini cuma jalan kalau",
                    "berkasnya dijalankan langsung, misalnya dengan python3 file.py. Kalau",
                    "berkas itu di-import oleh module lain, blok ini nggak jalan. Gunanya",
                    "untuk menaruh kode tes atau demo di dalam berkas module.",
                    "",
                    "  def tambah(a, b):",
                    "      return a + b",
                    "",
                    "  if __name__ == \"__main__\":",
                    "      print(tambah(2, 3))   # hanya jalan jika file ini dieksekusi langsung",
                    "",
                    "Library buatan orang lain dikumpulkan di PyPI (Python Package Index),",
                    "dan dipasang pakai pip:",
                    "  pip install nama_package     -> install library eksternal",
                    "  pip freeze > requirements.txt -> catat semua dependency project",
                    "  pip install -r requirements.txt -> install semua dari catatan itu",
                    "",
                    "Dependency artinya library lain yang dibutuhkan project-mu supaya bisa",
                    "jalan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kode toko yang mulai besar dipecah jadi beberapa berkas: uang.py untuk",
                    "format rupiah, struk.py untuk mencetak struk, laporan.py untuk rekap",
                    "bulanan. Fungsi yang dipakai di banyak tempat tinggal di satu modul,",
                    "lalu di-import. Daftar library-nya dicatat di requirements.txt supaya",
                    "komputer kasir lain bisa memasang hal yang sama.",
                    "",
                    "Kasus kecil: fungsi pemformat rupiah tersalin di tiga skrip. Suatu hari",
                    "satu salinan dibetulkan, dua lainnya lupa, dan struk mencetak format",
                    "yang beda dengan laporan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali kode yang tersalin. Salinan seperti ini selalu jadi tempat",
                    "     bug yang dibetulkan di satu tempat saja.",
                    "  2. Pindahkan fungsinya ke berkas uang.py. Contoh pemakaiannya ditaruh",
                    "     di bawah if __name__ == \"__main__\", supaya nggak ikut jalan waktu",
                    "     di-import:",
                    "      def rupiah(n):",
                    "          return \"Rp\" + f\"{n:,}\".replace(\",\", \".\")",
                    "      if __name__ == \"__main__\":",
                    "          print(rupiah(12500))",
                    "  3. Di struk.py dan laporan.py, tulis import uang lalu panggil",
                    "     uang.rupiah(37500). Hasilnya Rp37.500 di semua skrip.",
                    "  4. Cek kasus pinggir: jalankan python3 struk.py. Baris contoh milik",
                    "     uang.py nggak ikut tercetak, karena waktu di-import, __name__ di",
                    "     sana berisi \"uang\", bukan \"__main__\".",
                    "",
                    "Jebakan: jangan menamai berkasmu math.py atau random.py. Python",
                    "menemukan berkasmu lebih dulu, dan modul bawaannya jadi nggak bisa",
                    "di-import.",
                ]
            },
        ],
    },
    {
        "title": "29. Struktur Project Python",
        "sections": [
            {
                "body": [
                    "Sampai sini, setiap contoh masih berupa satu berkas .py. Project Python",
                    "sungguhan nggak pernah sesederhana itu. Isinya sekumpulan folder, dan",
                    "susunannya hampir sama di semua repo. Materi Module & Package sudah",
                    "bilang bahwa paket itu folder yang punya __init__.py. Sekarang kita",
                    "lihat folder itu di tempat kerjanya.",
                    "",
                    "Kenapa perlu dibahas sekarang? Waktu kamu membuka repo Python orang",
                    "lain, yang pertama kelihatan adalah daftar berkas ini, belum kodenya.",
                    "Lalu di baris paling atas hampir tiap berkas ada bentuk seperti",
                    "'from .sesuatu import X'. Titik di depan nama itu belum pernah muncul",
                    "sebelumnya, dan artinya mustahil ditebak tanpa dijelaskan.",
                    "",
                    "Isi sebuah repo Python, satu per satu:",
                    "",
                    "  - <nama_paket>/ berisi kode utamanya. Nama folder ini yang",
                    "    nanti diketik orang di baris import. Jadi pilih nama yang sah",
                    "    sebagai nama Python: huruf kecil, tanpa spasi, tanpa tanda hubung.",
                    "  - tests/ berisi berkas test (test_*.py). Folder ini sengaja ditaruh",
                    "    di luar paket. Alasannya, test nggak ikut terpasang di komputer",
                    "    pemakai. Selain itu, memisahkannya membuktikan paketmu bisa",
                    "    di-import dari luar, nggak cuma dari dalam dirinya sendiri.",
                    "  - pyproject.toml berisi identitas project. Dibahas di bawah.",
                    "  - README.md berisi penjelasan untuk manusia: project ini apa, cara",
                    "    pasangnya, dan cara pakainya.",
                    "  - .gitignore berisi daftar berkas yang nggak ikut masuk ke Git.",
                    "  - main.py adalah titik masuk program, kalau project-nya memang berupa",
                    "    aplikasi. Namanya boleh juga app.py atau cli.py. Yang penting dia",
                    "    ada di luar paket.",
                    "",
                    "Sekarang pyproject.toml. Satu berkas ini menggantikan setup.py,",
                    "setup.cfg, dan berkas setelan milik tiap alat bantu yang dulu",
                    "berserakan. TOML adalah format berkas setelan. Aturannya: nama [tabel]",
                    "ditulis di dalam kurung siku, lalu di bawahnya baris kunci = nilai, dan",
                    "teks ditulis pakai tanda kutip.",
                    "",
                    "  [project]",
                    "  name = \"toko-online\"              # nama saat dipasang; tanda hubung boleh",
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
                    "Tiga jenis tabel itu dibaca oleh pihak yang berbeda. [project] dibaca",
                    "pip. [build-system] dibaca alat pengemas. [tool.apa_saja] dibaca alat",
                    "yang namanya disebut. Jadi kalau kamu nggak pakai ruff, [tool.ruff]",
                    "cuma teks yang diabaikan semua orang.",
                    "",
                    "Hubungannya dengan yang sudah kamu kenal:",
                    "",
                    "  - requirements.txt (materi Virtual Environment) mencatat versi persis",
                    "    hasil pip freeze. Gunanya untuk menyusun ulang environment yang",
                    "    sama persis. Sementara itu, dependencies di pyproject.toml menyebut",
                    "    batas versi yang dibutuhkan project ini. Banyak repo memakai",
                    "    dua-duanya: pyproject untuk niatnya, requirements untuk hasil yang",
                    "    dikunci.",
                    "  - setup.py adalah cara lama dengan tugas yang sama. Bentuknya skrip",
                    "    Python yang dijalankan waktu pemasangan. Justru itu alasan setup.py",
                    "    ditinggalkan: berkas setelan seharusnya nggak bisa menjalankan apa",
                    "    pun. Tapi repo lama masih banyak yang memakainya.",
                    "",
                    "Folder __pycache__/ dan berkas .pyc di dalamnya muncul sendiri, tanpa",
                    "kamu ketik. Isinya hasil terjemahan modul ke bytecode, yaitu bentuk",
                    "kode yang lebih cepat dibaca Python. Berkas ini dibikin waktu sebuah",
                    "modul di-import, bukan waktu dijalankan langsung. Tujuannya supaya",
                    "import berikutnya nggak perlu membaca ulang teks kodenya.",
                    "",
                    "Isinya nggak bisa dibaca manusia, terikat ke versi Python tertentu, dan",
                    "bisa dibikin ulang kapan aja. Makanya __pycache__/ selalu dimasukkan ke",
                    ".gitignore. Menghapusnya juga aman.",
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
                "heading": "Peran __init__.py, import relatif, dan __all__",
                "body": [
                    "__init__.py itu lebih dari berkas kosong penanda. Python menjalankan",
                    "berkas ini waktu paketnya pertama kali di-import. Biasanya dia punya",
                    "tiga peran sekaligus:",
                    "",
                    "  1. Penanda. Folder ini paket, bukan folder biasa yang kebetulan",
                    "     berisi berkas .py.",
                    "  2. Etalase. __init__.py mengangkat nama dari dalam ke permukaan,",
                    "     supaya pemakai cukup menulis 'from toko import Produk', bukan",
                    "     'from toko.model.produk import Produk'. Hasilnya, susunan di dalam",
                    "     paketmu bebas dirombak nanti tanpa merusak kode siapa pun.",
                    "  3. Tempat __all__.",
                    "",
                    "Sejak Python 3.3, folder tanpa __init__.py masih bisa di-import.",
                    "Namanya namespace package. Jangan mengandalkan itu. Tanpa __init__.py",
                    "kamu kehilangan etalase. Lebih parah lagi, salah ketik nama folder bisa",
                    "jadi paket kosong yang berhasil di-import tanpa protes, lalu baru gagal",
                    "jauh belakangan. Error seperti itu jauh lebih susah dilacak.",
                    "",
                    "Sekarang import relatif, alias arti titik di depan nama. Titik itu",
                    "dihitung dari posisi berkas yang sedang ditulis, bukan dari folder",
                    "tempat kamu mengetik perintah:",
                    "",
                    "  from . import uang                . = paket tempat berkas ini berada",
                    "  from .uang import rupiah          ambil rupiah dari modul tetangga uang.py",
                    "  from .model.produk import Produk  turun ke subpaket model, lalu ke produk.py",
                    "  from ..uang import rupiah         .. = NAIK satu tingkat, ke paket induk",
                    "  from ...alat import bantu         ... = naik dua tingkat (jarang)",
                    "",
                    "Tiga titik jarang dipakai. Kalau kamu sampai butuh naik sebanyak itu,",
                    "biasanya susunan paketnya yang salah.",
                    "",
                    "Kelebihannya: seluruh paket bisa diganti nama atau dipindah ke project",
                    "lain tanpa menyunting satu pun baris import di dalamnya. Import absolut",
                    "seperti 'from toko.uang import rupiah' menyebut nama paketnya, jadi",
                    "harus ikut diubah. Aturan praktisnya: pakai import relatif untuk saling",
                    "memanggil di dalam paketmu sendiri, dan import absolut untuk memanggil",
                    "paket dari luar.",
                    "",
                    "Ada dua jebakan:",
                    "",
                    "  - Import relatif cuma sah di dalam paket. Di berkas skrip biasa dia",
                    "    langsung gagal dengan",
                    "    ImportError: attempted relative import with no known parent package.",
                    "  - Bentuknya harus 'from .modul import nama'. Bentuk 'import .modul'",
                    "    nggak ada.",
                    "",
                    "__all__ = [\"Produk\", \"rupiah\"] adalah daftar nama yang ikut terbawa",
                    "waktu orang menulis 'from toko import *'. Tanpa __all__, tanda bintang",
                    "membawa semua nama yang nggak diawali garis bawah. Termasuk modul yang",
                    "kebetulan kamu import di berkas itu, seperti os, json, atau sys. Nama",
                    "itu lalu menimpa nama yang sama di kode pemakainya.",
                    "",
                    "__all__ nggak menyembunyikan apa pun. 'from toko.uang import rupiah'",
                    "tetap jalan walaupun rupiah nggak disebut di __all__. Dia cuma mengatur",
                    "tanda bintang, dan dibaca alat dokumentasi sebagai daftar antarmuka",
                    "resmi paket ini. Import * sendiri sebaiknya dihindari di kode biasa,",
                    "karena kamu nggak bisa tahu nama apa aja yang masuk cuma dengan membaca",
                    "barisnya.",
                ],
            },
            {
                "heading": "Satu paket utuh: enam berkas yang saling memanggil",
                "body": [
                    "Bikin foldernya persis seperti pohon di atas, lalu jalankan dari folder",
                    "akar:",
                    "  python3 main.py         -> memakai paket lewat etalase __init__.py",
                    "  python3 -m toko.laporan -> menjalankan satu modul DARI DALAM paket",
                ],
                "code": "# File: toko/__init__.py\n\"\"\"Paket toko. Berkas INI yang dijalankan Python saat ada yang menulis `import toko`.\"\"\"\n\nfrom .uang import rupiah              # satu titik = modul tetangga, di paket yang sama\nfrom .model.produk import Produk      # titik lalu nama = turun ke subpaket model\n\n__all__ = [\"Produk\", \"rupiah\"]        # nama yang ikut terbawa `from toko import *`\n\n\n# File: toko/uang.py\ndef rupiah(jumlah):\n    \"\"\"12500 -> 'Rp12.500'\"\"\"\n    return \"Rp\" + format(jumlah, \",d\").replace(\",\", \".\")\n\n\n# File: toko/model/__init__.py\n# Boleh kosong. Yang penting keberadaannya: folder ini jadi subpaket, bukan folder biasa.\n\n\n# File: toko/model/produk.py\nfrom ..uang import rupiah             # DUA titik = naik satu tingkat, ke paket toko\n\n\nclass Produk:\n    def __init__(self, nama, harga):\n        self.nama = nama\n        self.harga = harga\n\n    def label(self):\n        return f\"{self.nama} - {rupiah(self.harga)}\"\n\n\n# File: toko/laporan.py\nfrom .model.produk import Produk      # satu titik: mulai dari paket toko\n\n\ndef ringkas(barang):\n    return \"\\n\".join(b.label() for b in barang)\n\n\nif __name__ == \"__main__\":            # jalankan: python3 -m toko.laporan\n    print(ringkas([Produk(\"Kopi\", 25000), Produk(\"Gula\", 12500)]))\n\n\n# File: main.py\nfrom toko import Produk, rupiah       # cukup 'toko' -- itu gunanya __init__.py\n\nbarang = [Produk(\"Kopi\", 25000), Produk(\"Gula\", 12500)]\nfor b in barang:\n    print(b.label())\nprint(\"Total:\", rupiah(sum(b.harga for b in barang)))\n\n# Keluaran python3 main.py:\n# Kopi - Rp25.000\n# Gula - Rp12.500\n# Total: Rp37.500",
            },
            {
                "heading": "Kenapa import-nya gagal, dan obatnya",
                "body": [
                    "Dua pesan error ini hampir pasti kamu temui waktu pertama kali memakai",
                    "paket buatan sendiri.",
                    "",
                    "  1. Pesan pertama:",
                    "       ImportError: attempted relative import with no known parent package",
                    "     Ini muncul kalau kamu menjalankan langsung berkas yang ada di dalam",
                    "     paket:",
                    "       python3 toko/laporan.py",
                    "     Berkas yang dijalankan langsung dikasih __name__ == \"__main__\", dan",
                    "     dia nggak punya paket induk sama sekali. Akibatnya titik di",
                    "     'from .model.produk import Produk' nggak menunjuk apa-apa. Berkas",
                    "     yang sama jalan normal kalau dia di-import.",
                    "",
                    "  2. Pesan kedua:",
                    "       ModuleNotFoundError: No module named 'toko'",
                    "     Python mencari modul dengan menyusuri daftar folder di sys.path.",
                    "     Entri pertamanya adalah folder tempat berkas yang dijalankan",
                    "     berada, bukan folder tempat kamu sedang berdiri di terminal. Jadi",
                    "     'python3 skrip/coba.py' yang dijalankan dari akar project",
                    "     memasukkan skrip/ ke sys.path. Folder toko/ di sebelahnya nggak",
                    "     pernah kelihatan.",
                    "",
                    "Obat untuk keduanya sama: jalankan sebagai modul, dari folder akar",
                    "project.",
                    "  python3 -m toko.laporan   titik, bukan garis miring, dan tanpa akhiran .py",
                    "  python3 -m pytest         pytest melihat folder sekarang",
                    "",
                    "Untuk pytest, bentuk -m ini bikin dia melihat folder sekarang, bukan",
                    "folder tempat pytest sendiri terpasang.",
                    "",
                    "Opsi -m menaruh folder sekarang di sys.path, lalu mengimpor modul yang",
                    "kamu sebut sebagai bagian dari paketnya. Dengan begitu paket induknya",
                    "dikenal, dan titiknya punya arti.",
                    "",
                    "Jangan menambalnya dengan sys.path.append(\"..\") di dalam kode. Cara itu",
                    "cuma memindahkan kesalahannya ke tempat yang lebih susah dilihat, dan",
                    "langsung rusak begitu berkasnya dipanggil dari folder lain. Untuk",
                    "project yang sudah punya pyproject.toml, cara paling bersih adalah",
                    "'pip install -e .' di dalam venv. Nama paketmu didaftarkan sekali, lalu",
                    "bisa di-import dari folder mana pun tanpa satu baris kode tambahan.",
                    "",
                    "Program di bawah ini memperlihatkan cara kerjanya. Jalankan apa adanya:",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Repo aplikasi di kantor hampir selalu bersusun sama: satu folder paket",
                    "berisi kode, folder tests/ di sebelahnya, pyproject.toml di akar, dan",
                    "main.py sebagai titik masuk. Orang baru yang meng-clone repo itu",
                    "langsung tahu harus membuka apa, dan menjalankan semuanya dari folder",
                    "akar.",
                    "",
                    "Kasus kecil: proyek kasir sudah punya paket kasir/ berisi __init__.py,",
                    "uang.py, dan laporan.py. Di laporan.py ada baris from .uang import",
                    "rupiah. Temanmu menjalankan python3 kasir/laporan.py dan mendapat",
                    "ImportError: attempted relative import with no known parent package.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesannya. \"no known parent package\" artinya berkas itu",
                    "     dijalankan langsung, sehingga titik di depan .uang nggak menunjuk",
                    "     paket apa pun.",
                    "  2. Pastikan susunannya benar: kasir/ punya __init__.py, dan import di",
                    "     dalam paket memakai bentuk relatif from .uang import rupiah.",
                    "  3. Jalankan sebagai modul dari folder akar, memakai titik dan tanpa",
                    "     .py:",
                    "      python3 kasir/laporan.py     # ImportError",
                    "      python3 -m kasir.laporan     # jalan",
                    "  4. Cek kasus pinggir: perintah yang sama dari dalam folder kasir/",
                    "     gagal, dan pesannya menyebut No module named 'kasir'. Folder",
                    "     tempat kamu mengetik perintah harus folder akar.",
                    "",
                    "Jebakan: menambal dengan sys.path.append(\"..\") cuma memindahkan",
                    "masalahnya. Begitu skripnya dipanggil dari folder lain, ia rusak lagi.",
                ]
            },
        ],
    },
    {
        "title": "30. Program Baris Perintah: sys, os & argparse",
        "sections": [
            {
                "body": [
                    "Sampai sini, satu-satunya cara program menerima data dari luar adalah",
                    "input(). Program berhenti, nunggu orang mengetik, baru lanjut. Program",
                    "sungguhan hampir nggak pernah begitu. Datanya disebut langsung di baris",
                    "perintah, jadi program bisa dijalankan oleh penjadwal atau skrip lain",
                    "tanpa ada orang yang menunggui.",
                    "",
                    "  python3 ringkas.py laporan.txt -n 3 --huruf-besar",
                    "",
                    "Bagian-bagian baris perintah itu:",
                    "",
                    "  - ringkas.py adalah berkas program yang dijalankan.",
                    "  - laporan.txt adalah argumen posisi. Artinya ditentukan oleh",
                    "    urutannya.",
                    "  - -n 3 adalah opsi yang punya nilai. Bentuk panjangnya --baris 3, dan",
                    "    letaknya bebas.",
                    "  - --huruf-besar adalah opsi saklar, sering disebut flag. Kalau",
                    "    ditulis berarti hidup, kalau nggak ditulis berarti mati.",
                    "",
                    "Python sudah menyiapkan semua bagian itu dalam bentuk mentah di",
                    "sys.argv, sebelum baris pertamamu jalan:",
                    "",
                    "  import sys",
                    "  sys.argv      -> ['ringkas.py', 'laporan.txt', '-n', '3']",
                    "  sys.argv[0]   -> nama/jalur berkas PROGRAMNYA SENDIRI, bukan argumen pertama",
                    "  sys.argv[1:]  -> bagian yang benar-benar diberikan pemakai",
                    "  len(sys.argv) -> 1 kalau program dijalankan tanpa argumen sama sekali",
                    "",
                    "Ada dua hal yang paling sering menjebak:",
                    "",
                    "  1. Isi sys.argv selalu str. '3' itu beda dengan 3. Kalau lupa int(),",
                    "     '3' * 2 hasilnya '33', bukan 6.",
                    "  2. Kata python3 nggak ikut tercatat. Daftarnya mulai dari nama",
                    "     berkasnya.",
                    "",
                    "Lalu sys.exit(kode). Fungsi ini menghentikan program saat itu juga,",
                    "sekaligus melapor apakah program berhasil atau gagal:",
                    "",
                    "  sys.exit(0)        -> selesai baik-baik",
                    "  sys.exit(1)        -> ada yang salah; angka apa pun selain 0 berarti GAGAL",
                    "  sys.exit(\"pesan\")  -> cetak pesan itu ke stderr, lalu keluar dengan kode 1",
                    "",
                    "Kode 0 juga dipakai otomatis kalau programnya habis dengan normal.",
                    "",
                    "Error yang nggak ditangkap juga bikin program keluar dengan kode 1 dengan",
                    "sendirinya. sys.exit() bekerja dengan melempar SystemExit. Akibatnya,",
                    "'except:' polos bisa menelannya, dan program malah nggak mau berhenti",
                    "waktu disuruh berhenti.",
                    "",
                    "Angka itu namanya exit code, atau kode keluar. Cuma lewat angka ini",
                    "terminal tahu program tadi sukses atau nggak:",
                    "",
                    "  echo $?              # Linux/Mac: lihat kode keluar perintah terakhir",
                    "  echo %ERRORLEVEL%    # Windows (cmd)",
                    "  ./a.py && ./b.py     # b.py HANYA jalan kalau a.py keluar dengan kode 0",
                    "",
                    "Itu juga alasan pesan error dicetak ke stderr. Perintah",
                    "'python3 alat.py > hasil.txt' mengalihkan stdout ke berkas. Error-nya",
                    "tetap kelihatan di layar dan nggak ikut mengotori hasil.",
                    "",
                    "Program yang mencetak 'gagal!' tapi keluar dengan kode 0 tetap bakal",
                    "dianggap berhasil oleh alat apa pun yang memanggilnya.",
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
                "heading": "Hasil argparse, shebang, dan python3 -m",
                "body": [
                    "Yang barusan terjadi, dan alasan hampir nggak ada yang menulis parser",
                    "sendiri:",
                    "",
                    "  - parse_args() mengembalikan Namespace. Isinya dibaca dengan",
                    "    args.nama, bukan args[\"nama\"].",
                    "  - Nama atributnya dirapikan. Awalan dua tanda hubung (--) dibuang,",
                    "    dan tanda - diganti jadi _. Jadi --huruf-besar dibaca",
                    "    args.huruf_besar. Ini bikin bingung kalau nggak dikasih tahu.",
                    "  - --help dan -h langsung tersedia tanpa kamu tulis. Isinya dirakit",
                    "    dari description dan tiap help=. Makanya help= layak ditulis dengan",
                    "    serius: itu dokumentasi programmu yang dibaca orang.",
                    "  - Kalau argumen wajib nggak diberikan, argparse mencetak cara",
                    "    pemakaian ke stderr lalu keluar dengan kode 2. Itu perilaku yang",
                    "    benar. Programnya nggak rusak.",
                    "  - Di Python lawas, judul di --help tertulis 'optional arguments:',",
                    "    bukan 'options:'.",
                    "  - Kalau nanti perlu: nargs=\"+\" (banyak nilai jadi satu list),",
                    "    choices=[...] (membatasi pilihan), required=True, dan",
                    "    add_subparsers() untuk perintah bertingkat seperti 'git commit' dan",
                    "    'git push'.",
                    "",
                    "Sekarang shebang, baris pertama yang beda dari komentar biasa:",
                    "",
                    "  #!/usr/bin/env python3",
                    "",
                    "Baris ini diawali #, jadi Python memang mengabaikannya. Tapi dua",
                    "karakter pertamanya (#!) dibaca oleh sistem operasi. Artinya: 'kalau",
                    "berkas ini dijalankan langsung, serahkan isinya ke program berikut'.",
                    "",
                    "  chmod +x ringkas.py        # tandai berkasnya boleh dieksekusi, cukup sekali",
                    "  ./ringkas.py laporan.txt   # jalan tanpa mengetik python3 lagi",
                    "",
                    "Yang perlu kamu tahu soal shebang:",
                    "",
                    "  - Harus di baris pertama. Di baris kedua, dia cuma komentar biasa.",
                    "  - Tulis /usr/bin/env python3, bukan /usr/bin/python3. env mencari",
                    "    python3 lewat PATH, jadi skripnya ikut memakai python3 milik venv",
                    "    yang sedang aktif.",
                    "  - Kalau lupa chmod +x, ./ringkas.py ditolak dengan pesan",
                    "    'Permission denied'.",
                    "  - Windows nggak memakai shebang. Di sana tetap pakai python",
                    "    ringkas.py.",
                    "",
                    "Terakhir, python3 -m nama_paket. Bentuk ini menjalankan modul, bukan berkas:",
                    "",
                    "  python3 -m venv venv  # -m yang sama sudah kamu pakai di materi venv & pip",
                    "  python3 -m pytest     # pytest milik python3 ini, bukan yang lain di PATH",
                    "  python3 -m http.server 8000",
                    "  python3 -m alatku     # menjalankan sebuah PAKET buatan sendiri",
                    "",
                    "Sebuah paket bisa dijalankan dengan cara itu kalau di dalamnya ada",
                    "berkas __main__.py, yang letaknya bersebelahan dengan __init__.py.",
                    "Isinya biasanya cuma memanggil main() di balik",
                    "if __name__ == \"__main__\", idiom dari materi Module & Package. Alasan",
                    "-m juga bisa membereskan ImportError dibahas di materi Struktur Project",
                    "Python.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Skrip di server jarang ditunggui orang. Penjadwal menjalankannya tiap",
                    "malam dengan argumen, misalnya python3 rekap.py --tanggal 2024-03-01,",
                    "lalu membaca kode keluarnya untuk tahu berhasil atau gagal. Kata sandi",
                    "database dibaca dari environment lewat os.getenv(), jadi nggak pernah",
                    "tertulis di kode.",
                    "",
                    "Kasus kecil: staf toko butuh alat kecil. Perintah python3 diskon.py",
                    "150000 --persen 10 harus mencetak harga sesudah diskon, dan isian yang",
                    "bukan angka harus ditolak dengan kode keluar selain 0.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu argumen posisi, yaitu harga, dan satu opsi --persen",
                    "     yang boleh nggak ditulis. Keluarannya satu angka.",
                    "  2. Pakai argparse dengan type=int, supaya konversi dan penolakan",
                    "     dikerjakan otomatis:",
                    "      import argparse",
                    "      p = argparse.ArgumentParser(prog=\"diskon\")",
                    "      p.add_argument(\"harga\", type=int)",
                    "      p.add_argument(\"--persen\", type=int, default=0)",
                    "      args = p.parse_args()",
                    "      print(args.harga - args.harga * args.persen // 100)",
                    "  3. Coba python3 diskon.py 150000 --persen 10. Hasilnya 135000. Tanpa",
                    "     --persen, hasilnya 150000.",
                    "  4. Cek kasus pinggir: python3 diskon.py seratus. argparse mencetak",
                    "     pesan error ke stderr dan keluar dengan kode 2. Periksa dengan",
                    "     echo $? sesudahnya.",
                    "",
                    "Ingat: --help sudah tersedia tanpa ditulis. Isi help= di tiap",
                    "add_argument supaya staf tahu cara memakainya.",
                ]
            },
        ],
    },
    {
        "title": "31. Logging: Pengganti print di Program Sungguhan",
        "sections": [
            {
                "body": [
                    "Sejauh ini, satu-satunya cara program kita bercerita tentang dirinya",
                    "sendiri adalah print(). Untuk belajar, itu sudah pas. Tapi di kode yang",
                    "dipakai orang beneran, print() hampir nggak pernah dipakai untuk",
                    "melaporkan keadaan program. Yang dipakai adalah modul logging. Modul",
                    "ini bawaan Python, jadi nggak perlu pip install.",
                    "",
                    "Bedakan dulu dua pekerjaan yang gampang ketuker:",
                    "",
                    "  - print() untuk menyajikan hasil ke pemakai, misalnya tabel, jawaban,",
                    "    atau laporan akhir. Pekerjaan ini tetap pakai print(), dan nggak",
                    "    ada yang salah dengan itu.",
                    "  - logging untuk menceritakan jalannya program ke orang yang",
                    "    merawatnya, misalnya \"mulai\", \"50 baris diproses\", \"gagal",
                    "    menyimpan\", atau \"koneksi putus\".",
                    "",
                    "Yang digantikan logging cuma pekerjaan kedua.",
                    "",
                    "Untuk pekerjaan kedua itu, print() punya tiga kekurangan:",
                    "",
                    "  1. print() nggak punya tingkat kepentingan. Buat print(), \"sedang",
                    "     ngecek isi variabel\" dan \"database mati\" sama aja. Padahal yang",
                    "     pertama cuma perlu kelihatan waktu kamu nyari bug, sedangkan yang",
                    "     kedua harus selalu kelihatan. Tanpa tingkat, dua-duanya numpuk jadi",
                    "     satu tembok teks, dan pesan yang penting tenggelam di antara yang",
                    "     nggak penting.",
                    "  2. Tujuan print() nggak bisa dipindah. print() selalu ke layar.",
                    "     Program yang jalan sebagai layanan di server nggak punya layar yang",
                    "     ditonton siapa pun. Kalau program itu rusak jam dua pagi, satu-",
                    "     satunya petunjuk adalah apa yang sempat tertulis ke berkas.",
                    "     print() nggak bisa dialihkan ke berkas tanpa menyunting kodenya",
                    "     satu per satu.",
                    "  3. print() nggak bisa dimatikan tanpa menyentuh kode. Dari sini lahir",
                    "     kebiasaan buruk yang paling umum: menaburkan print() waktu melacak",
                    "     bug, lalu menghapusnya satu per satu sebelum kodenya dikirim. Bulan",
                    "     depan bug yang sama muncul lagi, dan semua jejak yang dulu susah",
                    "     payah dipasang sudah hilang. Dengan logging, baris itu nggak",
                    "     dihapus. Dia cuma didiamkan, lalu bisa dinyalakan lagi lewat satu",
                    "     angka waktu dibutuhkan.",
                    "",
                    "Makanya baris logging.getLogger(__name__) ada di bagian atas ribuan",
                    "berkas Python di luar sana. Setelah materi ini, baris itu nggak bakal",
                    "asing lagi waktu kamu membacanya.",
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
                "heading": "Level log, format, dan getLogger(__name__)",
                "body": [
                    "Ada lima level, dari yang paling remeh sampai yang paling gawat. Angka",
                    "di tengah itu nilai aslinya. Level itu angka yang dibandingkan, bukan",
                    "kategori:",
                    "",
                    "  DEBUG     10  detail untuk dirimu sendiri saat melacak bug: isi variabel,",
                    "                fungsi apa dipanggil dengan argumen apa.",
                    "  INFO      20  kejadian normal yang wajar dicatat:",
                    "                \"server jalan di port 8000\", \"120 baris diproses\",",
                    "                \"berkas ditulis\".",
                    "  WARNING   30  ada yang aneh, program MASIH jalan: konfigurasi tidak ketemu,",
                    "                memakai nilai cadangan. Ini level BAWAAN kalau kamu diam saja.",
                    "  ERROR     40  satu pekerjaan GAGAL, tapi program belum mati.",
                    "  CRITICAL  50  program tidak bisa lanjut sama sekali.",
                    "",
                    "level=logging.INFO artinya \"tampilkan yang nilainya >= 20\". Cuma itu.",
                    "Jadi menaikkan level sama dengan mendiamkan semua level di bawahnya.",
                    "",
                    "Isi format berupa potongan %(...)s yang boleh kamu susun sesukamu:",
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
                    "",
                    "  format=\"%(asctime)s %(levelname)-8s [%(name)s] %(message)s\"",
                    "  2026-01-05 09:41:12,317 WARNING  [toko.pembayaran] saldo tidak cukup",
                    "",
                    "Angka -8 pada %(levelname)-8s cuma meratakan lebar kolomnya supaya",
                    "sejajar.",
                    "",
                    "Sekarang baris yang ada di mana-mana itu:",
                    "",
                    "  logger = logging.getLogger(__name__)",
                    "",
                    "Di sini __name__ dipakai dengan cara yang beda dari yang kamu kenal di",
                    "materi Module & Package. Banyak orang melihat dua-duanya tanpa sadar",
                    "itu hal yang sama:",
                    "",
                    "  - Di if __name__ == \"__main__\":, __name__ dipakai sebagai bahan",
                    "    perbandingan. Yang dipakai hasilnya, True atau False.",
                    "  - Di getLogger(__name__), __name__ dipakai sebagai nilai. Yang dipakai",
                    "    isinya, yaitu sebuah string.",
                    "",
                    "Isi string itu persisnya:",
                    "",
                    "  berkas dijalankan langsung (python3 app.py) -> __name__ berisi \"__main__\"",
                    "  berkas di-import sebagai module             -> __name__ berisi nama module,",
                    "                                                 misalnya \"toko.pembayaran\"",
                    "",
                    "Jadi getLogger(__name__) memberi setiap berkas sebuah logger yang",
                    "namanya sesuai posisi berkas itu, tanpa kamu pernah mengetik nama itu.",
                    "Kalau berkasnya dipindah ke folder lain, namanya ikut berubah sendiri.",
                    "Itu kelebihannya dibanding getLogger(\"pembayaran\"), yang namanya diketik",
                    "tangan lalu bisa basi tanpa ada yang sadar.",
                    "",
                    "Titik di dalam nama logger membentuk keluarga. \"toko.pembayaran\" adalah",
                    "anak dari \"toko\". Gunanya lebih dari kerapian: anak mewarisi pengaturan",
                    "induknya.",
                    "",
                    "  logging.getLogger(\"toko\").setLevel(logging.DEBUG)",
                    "  # seluruh logger di bawah \"toko\" ikut jadi DEBUG,",
                    "  # tanpa satu berkas pun disunting",
                    "",
                    "Dengan cara ini, logging bisa dinyalakan tanpa menyentuh kode. Kamu bisa",
                    "membuka keran DEBUG cuma untuk satu bagian program yang dicurigai, dan",
                    "membiarkan bagian lain tetap tenang. Di program baris perintah (materi",
                    "sebelumnya), keran itu biasanya disambungkan ke sebuah flag:",
                    "",
                    "  p.add_argument(\"-v\", \"--verbose\", action=\"store_true\")",
                    "  args = p.parse_args()",
                    "  logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)",
                    "",
                    "Sejak itu, kalau kamu mau lihat detailnya, cukup ketik -v waktu",
                    "menjalankan program. Nggak perlu lagi menyunting kode lalu",
                    "mengembalikannya.",
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
                "heading": "Jebakan basicConfig, level, dan f-string di log",
                "body": [
                    "Ada beberapa jebakan yang sering kejadian:",
                    "",
                    "  1. \"Programku nggak mencetak apa-apa.\" Penyebabnya hampir selalu",
                    "     level. Kalau basicConfig nggak pernah dipanggil, level bawaannya",
                    "     WARNING, jadi semua logger.info() dan logger.debug() hilang. Nggak",
                    "     ada error, nggak ada peringatan, cuma sepi. Itu yang bikin masalah",
                    "     ini lama ketemu. Sebelum curiga kodenya rusak, turunkan dulu",
                    "     levelnya ke logging.DEBUG.",
                    "  2. basicConfig cuma berlaku sekali. Panggilan berikutnya diabaikan",
                    "     tanpa pesan. Begitu root logger, yaitu logger induk paling atas,",
                    "     sudah punya handler (bagian yang menentukan ke mana log ditulis),",
                    "     basicConfig nggak berbuat apa-apa lagi. Ini termasuk kalau handler",
                    "     itu dipasang oleh logging.warning() yang kebetulan kamu panggil",
                    "     lebih dulu, karena fungsi jalan pintas itu memanggil basicConfig",
                    "     sendiri. Akibatnya format dan level barumu nggak pernah berlaku,",
                    "     tanpa satu keluhan pun. Panggil basicConfig sekali di paling atas",
                    "     program utamamu. Kalau memang harus menimpa, pakai",
                    "     basicConfig(..., force=True).",
                    "  3. logger.exception() di luar blok except menghasilkan",
                    "     \"NoneType: None\". Dia mengambil traceback dari exception yang sedang",
                    "     ditangani. Di luar except, nggak ada yang bisa diambil. Kalau kamu",
                    "     perlu traceback di level lain, pakai",
                    "     logger.error(\"...\", exc_info=True) atau",
                    "     logger.debug(\"...\", exc_info=True). exception() sendiri selalu",
                    "     berlevel ERROR.",
                    "  4. Jangan rakit pesannya dengan f-string.",
                    "       logger.debug(f\"data = {data}\")   # dirakit SELALU, walau nanti dibuang",
                    "       logger.debug(\"data = %s\", data)  # dirakit HANYA kalau ditampilkan",
                    "     Bentuk kedua menyerahkan perakitan pesan ke logging. Kalau pesannya",
                    "     toh disaring level, logging nggak bakal repot merakitnya. Untuk",
                    "     debug di dalam loop yang jalan jutaan kali, bedanya terasa.",
                    "  5. Log keluar lewat stderr, bukan stdout. Jadi",
                    "     python3 app.py > catatan.txt nggak menangkap satu baris log pun.",
                    "     Yang kamu perlukan 2> catatan.txt. Di aplikasi ini juga begitu:",
                    "     tombol Jalankan menampilkan baris log di bagian pesan error, bukan",
                    "     di bagian keluaran. Itu normal. Programnya nggak gagal.",
                    "  6. Jangan panggil basicConfig di dalam module yang di-import. Yang",
                    "     berhak menentukan ke mana log pergi adalah program utama, bukan",
                    "     potongan yang dipakainya. Module cukup punya",
                    "     logger = getLogger(__name__) lalu memakainya. Kalau nggak ada yang",
                    "     mengonfigurasi, pesannya memang nggak ke mana-mana, dan itu",
                    "     perilaku yang benar.",
                    "  7. Berkas log tumbuh terus kalau dibiarkan. Project sungguhan memakai",
                    "     logging.handlers.RotatingFileHandler, supaya berkasnya dipotong dan",
                    "     diganti baru setelah mencapai ukuran tertentu. Untuk sekarang,",
                    "     cukup tahu namanya.",
                    "  8. Jangan pernah mencatat password, token, atau nomor kartu ke log.",
                    "     Berkas log adalah benda yang paling sering dikirim ke orang lain",
                    "     waktu sedang nyari bug.",
                    "",
                    "Catatan: logging.warn() (tanpa -ing) sudah usang dan bakal dihapus.",
                    "Yang benar logging.warning(). Kamu masih bakal melihat bentuk lama itu",
                    "di kode lama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi yang jalan di server nggak punya layar yang ditonton orang.",
                    "Waktu ada laporan \"pembayaran gagal jam dua pagi\", satu-satunya",
                    "petunjuk adalah berkas log. Level membuat log harian tetap tenang di",
                    "INFO, lalu bisa dibuka sampai DEBUG cuma waktu sedang melacak masalah.",
                    "",
                    "Kasus kecil: skrip impor data pelanggan membaca baris \"nama;nomor HP\".",
                    "Baris yang nomornya kosong harus dilewati. Admin ingin tahu baris mana",
                    "yang dilewati, tanpa mengotori ringkasan hasil yang dicetak di akhir.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua pekerjaan. Ringkasan untuk admin tetap print().",
                    "     Cerita jalannya program, termasuk baris yang dilewati, masuk log.",
                    "  2. Nyalakan logging sekali di paling atas program, lalu buat logger",
                    "     untuk berkas ini:",
                    "      import logging",
                    "      logging.basicConfig(level=logging.INFO,",
                    "                          format=\"%(levelname)s %(message)s\")",
                    "      logger = logging.getLogger(__name__)",
                    "      logger.warning(\"baris %s dilewati: nomor HP kosong\", 2)",
                    "  3. Di dalam loop, panggil logger.warning() setiap kali ada baris yang",
                    "     dilewati, dengan nomor barisnya sebagai argumen. Contoh di atas",
                    "     mencetak WARNING baris 2 dilewati: nomor HP kosong.",
                    "  4. Cek kasus pinggir: tanpa basicConfig, logger.info() nggak muncul",
                    "     sama sekali, karena level bawaannya WARNING. Kalau log terasa",
                    "     sepi, periksa level dulu.",
                    "",
                    "Ingat: log keluar lewat stderr. python3 impor.py > hasil.txt cuma",
                    "menangkap print(), sedangkan log tetap muncul di layar.",
                ]
            },
        ],
    },
    {
        "title": "32. Tanggal & Waktu (datetime)",
        "sections": [
            {
                "body": [
                    "Hampir semua program sungguhan berurusan dengan waktu. Kapan pesanan",
                    "dibuat, berapa lama sebuah proses jalan, apakah sesi login sudah",
                    "kedaluwarsa. Di materi Module & Package, datetime cuma lewat sekilas",
                    "lewat .now(). Di sini kita bongkar isinya.",
                    "",
                    "Modul datetime punya empat class utama:",
                    "  date       -> tanggal saja                  date(2005, 8, 17)",
                    "  time       -> jam saja, tanpa tanggal       time(14, 30, 0)",
                    "  datetime   -> tanggal + jam sekaligus       datetime(2024, 3, 1, 14, 30)",
                    "  timedelta  -> DURASI, bukan titik waktu     timedelta(days=7, hours=3)",
                    "",
                    "Bedakan baik-baik dua yang terakhir. datetime menjawab \"kapan\",",
                    "timedelta menjawab \"berapa lama\". Tanggal dikurangi tanggal hasilnya",
                    "durasi. Tanggal ditambah durasi hasilnya tanggal lagi. Persis seperti",
                    "aljabar biasa.",
                    "",
                    "Jebakan: modulnya bernama datetime, dan di dalamnya ada class yang juga",
                    "bernama datetime. Gara-gara ini, kode orang lain kelihatan beda-beda",
                    "padahal maksudnya sama:",
                    "  import datetime                  -> tulisnya  datetime.datetime.now()",
                    "  from datetime import datetime    -> tulisnya  datetime.now()",
                    "",
                    "Pilih satu gaya, lalu pakai terus. Gaya kedua paling sering dipakai di",
                    "kode nyata, dan gaya itu juga yang dipakai di materi ini.",
                    "",
                    "Untuk mengambil waktu sekarang dari jam komputer:",
                    "  datetime.now()   -> tanggal + jam saat ini",
                    "  date.today()     -> tanggal hari ini saja",
                    "",
                    "Dua-duanya bukan konstanta. Kalau dipanggil dua kali, hasilnya beda.",
                    "Makanya contoh di bawah memakai tanggal tetap, supaya keluarannya pasti",
                    "dan kamu bisa mencocokkan hasil di layarmu dengan komentarnya.",
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
                "heading": "Method strftime, strptime, dan kode formatnya",
                "body": [
                    "Di kode nyata, tanggal hampir selalu dipakai untuk salah satu dari dua",
                    "hal. Pertama, diubah jadi teks untuk disimpan atau ditampilkan. Kedua,",
                    "teks dibaca lagi jadi tanggal. Ada dua method untuk itu, dan dua-duanya",
                    "perlu kamu hafal:",
                    "",
                    "  strftime  = string format time  ->  objek datetime  jadi  teks",
                    "  strptime  = string parse time   ->  teks            jadi  objek datetime",
                    "",
                    "Perhatikan: \"%Y-%m-%d\" itu beda dengan %-formatting string di materi",
                    "String & Formatting (\"Umur: %d\" % umur). Bentuknya kebetulan mirip,",
                    "tapi artinya lain sama sekali. Ini bahasa mini milik datetime, dan %d",
                    "di sini artinya tanggal, bukan bilangan bulat. Jangan menebak artinya",
                    "dari kemiripan itu.",
                    "",
                    "Kode format yang paling sering kamu temui:",
                    "  %Y  tahun 4 digit      2024      %y  tahun 2 digit        24",
                    "  %m  bulan 2 digit      03        %B  nama bulan           March",
                    "  %d  tanggal 2 digit    01        %b  nama bulan singkat   Mar",
                    "  %H  jam 24-an (00-23)  14        %A  nama hari            Friday",
                    "  %I  jam 12-an (01-12)  02        %a  nama hari singkat    Fri",
                    "  %M  menit              30        %p  AM atau PM           PM",
                    "  %S  detik              00        %%  tanda persen sendiri %",
                    "",
                    "Jebakan: %m itu bulan, %M itu menit. Huruf besar-kecilnya menentukan.",
                    "Salah ketik di sini nggak menghasilkan error. Yang terjadi, tanggal",
                    "yang keliru tersimpan tanpa ada yang sadar, dan baru ketahuan",
                    "berbulan-bulan kemudian.",
                    "",
                    "%A dan %B mengikuti locale sistem, yaitu setelan bahasa dan wilayah di",
                    "komputernya. Dengan setelan bawaan, hasilnya bahasa Inggris (\"Friday\"),",
                    "bukan \"Jumat\". Pakai keduanya cuma untuk tampilan. Jangan pakai untuk",
                    "data yang disimpan, karena arti berkasmu bisa berubah begitu pindah",
                    "mesin.",
                    "",
                    "strptime menuntut polanya cocok persis, termasuk garis miring dan",
                    "tanda strip-nya. Kalau nggak cocok, dia melempar ValueError, bukan",
                    "mengembalikan None. Jadi bungkus dengan try/except (materi Exception",
                    "Handling) setiap kali teksnya datang dari pengguna, atau dari berkas",
                    "yang bukan kamu tulis sendiri.",
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
                "heading": "ISO 8601, zona waktu, dan modul time",
                "body": [
                    "Ada tiga alasan ISO 8601 (\"2024-03-01T14:30:00\") jadi format baku di",
                    "mana-mana:",
                    "",
                    "  - Urutannya tahun-bulan-tanggal. Jadi kalau diurutkan sebagai teks",
                    "    biasa pun, urutan waktunya tetap benar. Ini alasan praktis yang",
                    "    besar.",
                    "  - Nggak ambigu. \"03/01/2024\" itu 3 Januari atau 1 Maret? Tergantung",
                    "    negaranya, dan nggak ada apa pun di dalam teks itu yang bisa",
                    "    menjawab.",
                    "  - .isoformat() menulisnya, datetime.fromisoformat() membacanya",
                    "    kembali. Kamu nggak perlu mengarang pola strftime sendiri.",
                    "",
                    "Aturan praktisnya: simpan dalam ISO, tampilkan dengan strftime.",
                    "",
                    "Catatan: sebelum Python 3.11, fromisoformat() cuma bisa membaca bentuk",
                    "yang persis dikeluarkan isoformat(), dan menolak akhiran \"Z\".",
                    "",
                    "Lalu ada istilah naive dan aware, yang bakal kamu temui di pesan error:",
                    "  naive  -> tidak tahu zona waktunya. Ini bawaan datetime(2024, 3, 1, 14, 30).",
                    "  aware  -> membawa zona waktu di dalam dirinya.",
                    "",
                    "  from datetime import datetime, timezone, timedelta",
                    "  utc = datetime(2024, 3, 1, 14, 30, tzinfo=timezone.utc)",
                    "  print(utc.isoformat())                # 2024-03-01T14:30:00+00:00",
                    "  wib = utc.astimezone(timezone(timedelta(hours=7)))",
                    "  print(wib.isoformat())                # 2024-03-01T21:30:00+07:00",
                    "",
                    "Kalau keduanya dicampur, hasilnya:",
                    "  TypeError: can't subtract offset-naive and offset-aware datetimes",
                    "",
                    "Error ini biasanya muncul di produksi, yaitu waktu program sudah dipakai",
                    "beneran, bukan waktu kamu lagi ngoding. Satu sisi datang dari database",
                    "(aware), sisi lainnya dibikin di kode (naive). Server sungguhan biasanya",
                    "begini: simpan semua waktu dalam UTC, lalu ubah ke zona lokal sesaat",
                    "sebelum ditampilkan ke orang.",
                    "",
                    "Terakhir, modul time. Modul ini beda dengan class datetime.time, dan",
                    "gampang ketuker kalau kamu menulis 'from datetime import time' di",
                    "berkas yang sama:",
                    "  time.time()          -> detik sejak 1 Januari 1970 (epoch), sebuah float",
                    "  time.sleep(2)        -> menjeda program 2 detik",
                    "  time.perf_counter()  -> khusus MENGUKUR durasi,",
                    "                          lebih teliti dari time.time()",
                    "  datetime.fromtimestamp(detik)  -> epoch kembali jadi datetime (zona lokal);",
                    "                                    beri timezone.utc kalau mau hasil pasti",
                    "",
                    "Decorator pengukur waktu di materi Decorator & Context Manager memakai",
                    "time.time(). Untuk pengukuran yang serius, perf_counter() lebih tepat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem perpustakaan, tagihan, dan absensi selalu berhitung dengan",
                    "tanggal: kapan jatuh tempo, berapa hari terlambat, jam berapa karyawan",
                    "masuk. Tanggal dari formulir datang sebagai teks, jadi harus dibaca",
                    "dengan strptime() dulu. Di database, tanggal biasanya disimpan dalam",
                    "format ISO seperti 2024-03-15.",
                    "",
                    "Kasus kecil: perpustakaan sekolah meminjamkan buku selama 7 hari, dan",
                    "dendanya Rp 1.000 per hari terlambat. Buku dipinjam 05/03/2024 dan",
                    "dikembalikan 15/03/2024. Berapa dendanya?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua tanggal berformat hari/bulan/tahun. Keluarannya",
                    "     denda dalam rupiah.",
                    "  2. Ubah teks jadi datetime, hitung jatuh tempo dengan timedelta, lalu",
                    "     ambil selisih harinya:",
                    "      from datetime import datetime, timedelta",
                    "      pinjam = datetime.strptime(\"05/03/2024\", \"%d/%m/%Y\")",
                    "      kembali = datetime.strptime(\"15/03/2024\", \"%d/%m/%Y\")",
                    "      telat = (kembali - (pinjam + timedelta(days=7))).days",
                    "      print(max(0, telat) * 1000)",
                    "  3. Jalankan. Jatuh temponya 12 Maret, terlambat 3 hari, dendanya",
                    "     3000.",
                    "  4. Cek kasus pinggir: buku yang dikembalikan lebih cepat. telat jadi",
                    "     negatif, dan max(0, telat) menjaga dendanya tetap 0.",
                    "",
                    "Jebakan: %m itu bulan, %M itu menit. Salah huruf di pola strptime",
                    "nggak selalu error, tapi tanggalnya terbaca keliru.",
                ]
            },
        ],
    },
    {
        "title": "33. File I/O",
        "sections": [
            {
                "body": [
                    "File I/O artinya membaca dan menulis data ke file. I itu input (data",
                    "masuk ke program), O itu output (data keluar dari program).",
                    "",
                    "Pintu masuknya satu fungsi bawaan: open(). Selain nama file, open()",
                    "menerima mode, yaitu huruf yang bilang kamu mau ngapain dengan file itu:",
                    "  'r'  -> read (baca), error jika file tak ada (default)",
                    "  'w'  -> write (tulis), MENGHAPUS isi lama jika file sudah ada",
                    "  'a'  -> append (tambah di akhir, tidak menghapus isi lama)",
                    "  'x'  -> exclusive create, error jika file SUDAH ada",
                    "  'r+' -> baca & tulis sekaligus",
                    "",
                    "Kalau mode nggak ditulis, Python pakai 'r'. Hati-hati dengan 'w': begitu",
                    "file dibuka dengan mode itu, isi lamanya langsung kosong, walaupun kamu",
                    "belum menulis apa-apa.",
                    "",
                    "Buka file selalu lewat with. Bentuk ini namanya context manager: file",
                    "otomatis ditutup begitu blok with selesai, termasuk kalau di tengahnya",
                    "terjadi error. Begitulah cara standar membuka file di Python.",
                    "",
                    "Untuk berkas teks, biasakan juga menulis encoding=\"utf-8\":",
                    "  with open(\"catatan.txt\", \"w\", encoding=\"utf-8\") as f:",
                    "",
                    "Encoding adalah aturan untuk mengubah huruf jadi byte yang disimpan di",
                    "disk. Kalau argumen itu nggak ditulis, Python pakai encoding bawaan",
                    "sistem, dan bawaan tiap sistem beda-beda. Linux dan Mac umumnya UTF-8,",
                    "Windows lama sering cp1252.",
                    "",
                    "Akibatnya bisa begini. Berkas berisi 'e' beraksen, huruf Arab, atau",
                    "emoji yang tertulis mulus di komputermu bisa gagal dibaca di komputer",
                    "orang lain dengan UnicodeDecodeError. Kodenya kelihatan benar, dan kamu",
                    "nggak bisa memunculkan error itu di komputermu sendiri. Dengan",
                    "encoding=\"utf-8\", hasilnya sama di mana pun. Semua contoh di bawah",
                    "memakainya.",
                    "",
                    "Semua mode di atas adalah mode teks: yang masuk dan keluar bertipe str.",
                    "Kalau kamu tambahkan huruf b (\"rb\", \"wb\"), berkas dibuka sebagai biner.",
                    "Mode biner bekerja dengan bytes dan nggak memakai encoding sama sekali.",
                    "Mode ini dipakai untuk gambar, PDF, dan sejenisnya. Soal mode biner dan",
                    "apa itu encoding dibahas lengkap di materi berikutnya, Encoding, bytes &",
                    "Berkas Biner.",
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
                    "Kalau file yang mau dibaca nggak ada, open() melempar FileNotFoundError.",
                    "Kamu bisa menangkapnya pakai try/except:",
                    "  try:",
                    "      with open(\"tidak_ada.txt\", encoding=\"utf-8\") as f:",
                    "          isi = f.read()",
                    "  except FileNotFoundError:",
                    "      print(\"File tidak ditemukan!\")",
                    "",
                    "Selain open(), ada modul pathlib. Ini cara yang lebih modern untuk",
                    "mengelola path, yaitu alamat file seperti data/catatan.txt. Path di",
                    "pathlib berupa objek yang punya method sendiri, jadi gayanya lebih OOP:",
                    "  from pathlib import Path",
                    "  p = Path(\"data\") / \"catatan.txt\"",
                    "  print(p.exists())      # cek file ada atau tidak",
                    "  print(p.read_text(encoding=\"utf-8\"))   # baca isi file langsung",
                    "",
                    "Tanda / di situ bukan pembagian. Untuk objek Path, / artinya menyambung",
                    "nama folder dan nama file jadi satu path.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kasir, mesin absensi, dan sensor gudang sering mencatat datanya ke",
                    "berkas teks, satu baris per kejadian. Di akhir hari, sebuah skrip",
                    "membaca berkas itu dan merekapnya. Mode \"a\" dipakai untuk menambah",
                    "catatan baru, karena mode \"w\" menghapus isi lama.",
                    "",
                    "Kasus kecil: berkas setoran.txt berisi setoran per baris: 15000, 20000,",
                    "satu baris kosong, lalu 7500. Pemilik toko butuh totalnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya berkas teks. Keluarannya satu angka total.",
                    "  2. Buka dengan with dan encoding=\"utf-8\", baca baris per baris, dan",
                    "     lewati baris yang kosong:",
                    "      total = 0",
                    "      with open(\"setoran.txt\", encoding=\"utf-8\") as f:",
                    "          for baris in f:",
                    "              if baris.strip():",
                    "                  total += int(baris)",
                    "      print(total)",
                    "  3. Jalankan. Hasilnya 42500. int() memaafkan karakter pindah baris di",
                    "     ujung, sama seperti spasi.",
                    "  4. Cek kasus pinggir: berkasnya belum ada, misalnya di hari pertama.",
                    "     open() melempar FileNotFoundError, jadi tangkap itu dan anggap",
                    "     totalnya 0.",
                    "",
                    "Jebakan: menulis transaksi baru dengan open(\"setoran.txt\", \"w\")",
                    "menghapus semua setoran sebelumnya. Untuk menambah, pakai \"a\".",
                ]
            },
        ],
    },
    {
        "title": "34. Encoding, bytes & Berkas Biner",
        "sections": [
            {
                "body": [
                    "Di memori, teks Python berbentuk str, yaitu deretan karakter: huruf,",
                    "emoji, aksara Arab. Di dalam berkas dan di kabel jaringan nggak ada",
                    "karakter. Yang ada cuma byte, yaitu angka 0-255. Jadi harus ada yang",
                    "menerjemahkan karakter jadi byte dan sebaliknya.",
                    "",
                    "Penerjemah itu namanya encoding. Gampangnya, encoding itu tabel yang",
                    "bilang \"huruf ini disimpan sebagai byte-byte ini\". Encoding yang paling",
                    "banyak dipakai sekarang adalah UTF-8:",
                    "  - Huruf ASCII (a-z, 0-9, tanda baca) tetap 1 byte, jadi berkas lama",
                    "    tetap terbaca.",
                    "  - Huruf beraksen (é, ü) makan 2 byte, aksara Asia 3 byte, emoji 4",
                    "    byte.",
                    "",
                    "Materi File I/O sudah mendaftar mode open() dengan lengkap. Yang belum",
                    "dibahas di sana adalah parameter yang paling sering ditulis orang di",
                    "kode nyata sesudah nama file dan mode:",
                    "",
                    "  with open(\"data.txt\", encoding=\"utf-8\") as f:",
                    "      isi = f.read()",
                    "",
                    "Kalau encoding= nggak ditulis, Python pakai default sistem, dan default",
                    "itu nggak seragam:",
                    "  Linux & macOS  ->  hampir selalu UTF-8",
                    "  Windows        ->  sering cp1252 atau cp1250, tergantung setelan negara",
                    "",
                    "Akibatnya, kode yang mulus di laptopmu bisa gagal di komputer orang lain,",
                    "padahal berkasnya sama persis. Bug seperti ini paling menyebalkan, karena",
                    "nggak bisa kamu munculkan di komputermu sendiri.",
                    "",
                    "Aturan praktisnya cuma satu: setiap open() untuk teks, tulis",
                    "encoding=\"utf-8\". Versi Python baru pelan-pelan bergerak ke UTF-8",
                    "sebagai default, tapi jangan menunggu. Yang ditulis jelas begitu benar",
                    "di semua versi dan di semua sistem.",
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
                "heading": "Membaca UnicodeDecodeError dan menanganinya",
                "body": [
                    "Kalau tabelnya salah waktu membaca, Python berhenti dengan pesan seperti",
                    "ini:",
                    "",
                    "  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:",
                    "  invalid continuation byte",
                    "",
                    "Baca pesannya potong per potong:",
                    "  'utf-8' codec         -> tabel yang kamu minta",
                    "                           (lewat encoding=, atau default sistem)",
                    "  byte 0xe9             -> byte yang nggak masuk akal menurut tabel itu",
                    "  in position 5         -> byte ke-5 pada potongan yang sedang dibaca",
                    "  invalid continuation  -> alasannya: UTF-8 menunggu byte lanjutan,",
                    "                           yang datang bukan byte lanjutan",
                    "",
                    "0xe9 kebetulan adalah huruf e beraksen di tabel Latin-1/cp1252. Jadi",
                    "pesan ini hampir selalu berarti salah satu dari dua hal:",
                    "  1. Berkasnya memang bukan UTF-8. Biasanya berkas itu dibuat Excel",
                    "     atau Notepad di Windows.",
                    "  2. Isi berkasnya gambar, PDF, atau zip, jadi sama sekali bukan teks,",
                    "     padahal dibuka dengan mode teks.",
                    "",
                    "Ini urutan penanganannya, dari yang paling benar sampai jalan darurat:",
                    "  1. Cari tahu encoding aslinya, lalu tulis:  open(p, encoding=\"cp1252\")",
                    "  2. Kalau isinya biner, yang diganti mode-nya jadi \"rb\", bukan",
                    "     encoding-nya.",
                    "  3. Baru sesudah itu:",
                    "       open(p, encoding=\"utf-8\", errors=\"replace\")  -> byte rusak jadi �",
                    "       open(p, encoding=\"utf-8\", errors=\"ignore\")   -> byte rusak dibuang",
                    "",
                    "errors= nggak memperbaiki apa pun. Dia cuma menukar error dengan data",
                    "rusak, dan dengan \"ignore\" byte yang rusak dibuang tanpa pemberitahuan.",
                    "Pakai untuk log yang cuma dibaca manusia. Jangan pakai untuk data yang",
                    "bakal disimpan lagi, karena kerusakannya ikut tersimpan dan nggak ada",
                    "yang ngasih tahu.",
                    "",
                    "Jebakan: encoding=\"latin-1\" nggak pernah gagal membaca, karena ke-256",
                    "byte punya arti di tabel itu. Kelihatannya menyelamatkan, padahal dia",
                    "cuma mengganti error dengan teks kacau (mojibake) yang baru ketahuan",
                    "berbulan-bulan kemudian.",
                    "",
                    "Pasangannya waktu menulis bernama UnicodeEncodeError. Lihat contoh",
                    "terakhir di kode atas.",
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
                "heading": "Akhir baris, newline kosong, dan BOM",
                "body": [
                    "Ada satu jebakan lagi di berkas teks: akhir baris nggak sama di tiap",
                    "sistem.",
                    "  Linux & macOS  ->  satu byte LF     \\n",
                    "  Windows        ->  dua byte CR LF   \\r\\n",
                    "",
                    "Mode teks menyembunyikan beda itu. Fitur ini namanya universal newlines.",
                    "Waktu membaca, \\r\\n diubah jadi \\n. Waktu menulis, \\n diubah balik jadi",
                    "akhir baris khas sistem yang menjalankan programnya. Mode biner nggak",
                    "menerjemahkan apa pun, jadi di sana kamu melihat byte aslinya.",
                    "",
                    "Terjemahan otomatis itu berguna, sampai ada modul yang mengurus akhir",
                    "barisnya sendiri. Modul csv menulis \\r\\n sendiri. Kalau berkasnya dibuka",
                    "tanpa newline=\"\", di Windows \\n milik csv diterjemahkan sekali lagi jadi",
                    "\\r\\r\\n, dan tiap baris data dipisahkan satu baris kosong. Makanya resep",
                    "bakunya selalu ditulis begini:",
                    "",
                    "  with open(\"data.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as f:",
                    "",
                    "newline=\"\" artinya \"jangan sentuh akhir baris, aku yang urus\". Artinya",
                    "bukan \"tanpa baris\".",
                    "",
                    "Masih ada satu lagi, namanya BOM (byte order mark). Notepad dan Excel",
                    "di Windows suka menyimpan tiga byte penanda (EF BB BF) di awal berkas.",
                    "Kalau dibuka dengan encoding=\"utf-8\", tiga byte itu jadi satu karakter",
                    "tak terlihat, \\ufeff, yang nempel di kolom pertama.",
                    "Akibatnya perbandingan sesederhana baris[0] == \"nama\" gagal, dan",
                    "penyebabnya nggak kelihatan di layar.",
                    "Obatnya encoding=\"utf-8-sig\" waktu membaca. Encoding ini membuang",
                    "penanda itu kalau ada, dan nggak ngapa-ngapain kalau nggak ada.",
                    "",
                    "Catatan: encoding= dan newline= cuma sah di mode teks. Kalau ditulis",
                    "bareng \"rb\" atau \"wb\", hasilnya langsung ValueError. Wajar, karena di",
                    "mode biner memang nggak ada yang perlu diterjemahkan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Berkas CSV dari kantor sering dibuat di Excel atau Notepad di Windows,",
                    "lalu diolah di server Linux. Di situ muncul dua masalah klasik: berkas",
                    "yang bukan UTF-8, dan tiga byte BOM di awal berkas. Programmer data",
                    "hampir pasti pernah ketemu keduanya waktu mengimpor data siswa atau",
                    "pelanggan.",
                    "",
                    "Kasus kecil: berkas siswa.csv hasil ekspor Excel diawali baris",
                    "nama;kelas. Kodemu memeriksa kepala[0] == \"nama\", dan hasilnya selalu",
                    "False, padahal di layar tulisannya sama persis.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat isinya apa adanya dengan repr(). Ternyata kolom pertamanya",
                    "     '﻿nama', bukan 'nama'. Karakter tak terlihat itu BOM.",
                    "  2. Baca dengan encoding=\"utf-8-sig\", yang membuang BOM kalau ada:",
                    "      with open(\"siswa.csv\", encoding=\"utf-8-sig\") as f:",
                    "          kepala = f.readline().strip().split(\";\")",
                    "      print(kepala[0] == \"nama\")",
                    "  3. Jalankan. Hasilnya True.",
                    "  4. Cek kasus pinggir: berkas yang dibuat tanpa BOM. utf-8-sig tetap",
                    "     membacanya dengan benar, jadi kode yang sama aman untuk dua-duanya.",
                    "",
                    "Jebakan: kalau yang muncul UnicodeDecodeError, berkasnya mungkin bukan",
                    "UTF-8 sama sekali. errors=\"ignore\" cuma menyembunyikan masalahnya.",
                    "Cari tahu encoding aslinya, misalnya cp1252.",
                ]
            },
        ],
    },
    {
        "title": "35. Regular Expression (modul re)",
        "sections": [
            {
                "body": [
                    "Ada pekerjaan teks yang bentuknya itu-itu aja. Misalnya \"ambil semua",
                    "angka di baris log ini\", \"periksa apakah teks ini berbentuk email\",",
                    "atau \"rapikan spasi yang bertumpuk jadi satu\". Semuanya bisa dikerjakan",
                    "pakai .find(), .split(), dan perulangan. Masalahnya, kodenya panjang,",
                    "dan tiap variasi kecil berarti menulis ulang logikanya dari nol.",
                    "",
                    "Regular expression, sering disingkat regex atau regexp, adalah bahasa",
                    "mini untuk menggambarkan pola teks. Satu baris pola bisa menggantikan",
                    "belasan baris pencarian manual. Bahasa ini juga ada di luar Python:",
                    "di JavaScript, Java, grep, dan editor kode. Jadi yang kamu pelajari di",
                    "sini kepakai di banyak tempat lain.",
                    "",
                    "Di Python, mesin regex ada di modul bawaan bernama re. Kamu nggak perlu",
                    "pip install apa pun:",
                    "",
                    "  import re",
                    "",
                    "Waktu pertama baca kode orang, biasanya yang bikin bingung adalah huruf",
                    "r di depan polanya:",
                    "",
                    "  re.sub(r\"\\s+\", \" \", teks)",
                    "",
                    "Huruf r itu bukan salah ketik dan bukan singkatan \"regex\". Itu raw",
                    "string, yang udah dibahas di materi Masukan, Keluaran & Modul Bawaan.",
                    "Di raw string, backslash dibiarkan apa adanya dan nggak diterjemahkan",
                    "Python.",
                    "",
                    "Kenapa di regex raw string itu wajib? Soalnya backslash punya arti di",
                    "dua tempat sekaligus, dan Python selalu jalan duluan. Python",
                    "menerjemahkan isi string dulu, baru sisanya diserahkan ke mesin regex.",
                    "Bandingkan dua tulisan ini:",
                    "  - \"\\b\" diubah Python jadi satu karakter backspace (kode 8). Mesin",
                    "    regex nggak pernah melihat backslash-b, jadi polanya nggak bakal",
                    "    pernah cocok. Nggak ada pesan error apa pun, hasilnya cuma daftar",
                    "    kosong.",
                    "  - r\"\\b\" berisi dua karakter: backslash dan b. Mesin regex membacanya",
                    "    sebagai \"batas kata\", dan itulah yang kita maksud.",
                    "",
                    "Beberapa kombinasi seperti \"\\d\" dan \"\\s\" kebetulan selamat. Python",
                    "nggak mengenalnya sebagai escape sequence, jadi backslash-nya dibiarkan.",
                    "Jangan mengandalkan kebetulan itu. Python 3.12+ udah ngasih peringatan",
                    "SyntaxWarning yang menyebut \"\\d\" sebagai invalid escape sequence, dan",
                    "versi mendatang bakal menjadikannya error.",
                    "",
                    "Aturan praktisnya gampang: setiap pola regex ditulis r\"...\", tanpa",
                    "kecuali.",
                ],
            },
            {
                "heading": "Bahan dasar pola",
                "body": [
                    "Mencocokkan satu karakter:",
                    "  .          satu karakter apa saja kecuali newline",
                    "  \\d  \\D     satu digit 0-9   /   satu karakter yang bukan digit",
                    "  \\w  \\W     huruf, angka, atau underscore   /   kebalikannya",
                    "  \\s  \\S     whitespace (spasi, tab, newline)   /   kebalikannya",
                    "  [abc]      salah satu dari a, b, atau c",
                    "  [a-z0-9]   rentang: satu huruf kecil atau satu digit",
                    "  [^abc]     apa saja kecuali a, b, c",
                    "",
                    "Perhatikan: tanda ^ di dalam kurung siku artinya negasi, yaitu \"selain",
                    "yang ini\".",
                    "",
                    "Untuk menentukan berapa kali sesuatu diulang, ada kuantifier.",
                    "Kuantifier berlaku untuk hal yang tepat ada di depannya:",
                    "  a+         satu atau lebih          a*      nol atau lebih",
                    "  a?         nol atau satu (opsional) a{3}    tepat tiga kali",
                    "  a{2,5}     dua sampai lima kali     a{2,}   dua kali atau lebih",
                    "  a+?        versi malas: ambil sesedikit mungkin (lihat bagian jebakan)",
                    "",
                    "Jangkar dan pengelompokan:",
                    "  ^          awal teks (atau awal tiap baris kalau flag re.MULTILINE",
                    "             menyala)",
                    "  $          akhir teks (atau akhir tiap baris)",
                    "  \\b         batas kata: r\"\\bkota\\b\" cocok dengan \"kota\", tapi tidak",
                    "             dengan \"kotak\"",
                    "  |          alternasi alias \"atau\": kucing|anjing",
                    "  (...)      grup: mengelompokkan dan menangkap isinya supaya bisa",
                    "             diambil belakangan",
                    "  (?:...)    grup yang cuma mengelompokkan, tidak menangkap",
                    "",
                    "Karakter yang punya arti khusus:  . ^ $ * + ? { } [ ] \\ | ( )",
                    "Kalau mau mencocokkan karakter itu sendiri, kasih backslash di depannya:",
                    "  r\"3.14\"    juga cocok dengan \"3x14\", karena titik berarti \"apa saja\"",
                    "  r\"3\\.14\"   hanya cocok dengan \"3.14\"",
                    "",
                    "Kalau teks yang dicari datang dari variabel, misalnya ketikan pengguna,",
                    "jangan menebak karakter mana yang perlu di-escape. Pakai re.escape(teks).",
                    "Fungsi itu memberi backslash ke semua karakter khusus sekaligus.",
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
                    "Tiga fungsi, yaitu search, match, dan fullmatch, mengembalikan objek",
                    "Match, bukan string. Dari objek itu kamu ambil isinya:",
                    "  .group(0)       seluruh bagian teks yang cocok",
                    "  .group(1)       isi grup tangkap pertama, .group(2) yang kedua, dst.",
                    "  .group(\"jam\")   isi grup bernama yang ditulis (?P<jam>...) di polanya",
                    "  .groupdict()    semua grup bernama sekaligus, langsung berbentuk dict",
                    "  .start() .end() posisi kecocokan di dalam teks aslinya",
                    "",
                    "re.compile(pola) mengubah pola jadi objek yang bisa dipakai berulang.",
                    "Untuk pola yang dipanggil di dalam perulangan atau di beberapa tempat,",
                    "cara ini lebih cepat dan lebih rapi. Polanya jadi satu konstanta",
                    "bernama, nggak lagi berupa string yang disalin ke mana-mana.",
                    "",
                    "Flag mengubah cara mencocokkan. Beberapa flag boleh digabung pakai",
                    "tanda |:",
                    "  re.IGNORECASE  huruf besar/kecil dianggap sama",
                    "  re.MULTILINE   ^ dan $ berlaku per baris, bukan per seluruh teks",
                    "  re.DOTALL      titik ikut cocok dengan newline",
                    "  re.VERBOSE     spasi & komentar di dalam pola diabaikan, untuk pola",
                    "                 panjang",
                ],
                "code": "import re\n\nLOG = \"\"\"08:15:02 INFO  server siap di port 8080\n08:15:44 ERROR koneksi gagal setelah 3 percobaan\n08:16:10 warn  memori terpakai 87 persen\"\"\"\n\n# Pola dikompilasi SEKALI, lalu dipakai berkali-kali.\n# (?P<nama>...) = grup tangkap BERNAMA, jauh lebih terbaca daripada group(2).\nPOLA = re.compile(\n    r\"^(?P<jam>\\d{2}:\\d{2}:\\d{2})\\s+(?P<level>INFO|WARN|ERROR)\\s+(?P<pesan>.+)$\",\n    re.MULTILINE | re.IGNORECASE,\n)\n# MULTILINE : tanpa ini ^ dan $ hanya cocok di ujung SELURUH teks, bukan tiap baris\n# IGNORECASE: baris \"warn\" ikut cocok. Flag mengubah cara mencocokkan, bukan hasilnya.\n\nfor cocok in POLA.finditer(LOG):\n    print(cocok.group(0))                     # seluruh bagian yang cocok\n    print(\"  jam   :\", cocok.group(\"jam\"))\n    print(\"  level :\", cocok.group(2))        # grup ke-2 = grup bernama \"level\"\n    print(\"  angka :\", re.findall(r\"\\d+\", cocok.group(\"pesan\")))\n\nsatu = POLA.search(\"09:00:00 ERROR disk penuh\")\nprint(satu.groupdict())   # {'jam': '09:00:00', 'level': 'ERROR', 'pesan': 'disk penuh'}\n\n# Memeriksa format email SEDERHANA. fullmatch dipakai supaya tidak ada sisa\n# karakter di kiri/kanan. Titik ditulis \\. karena titik polos = \"apa saja\".\nPOLA_EMAIL = re.compile(r\"[\\w.+-]+@[\\w-]+\\.[\\w.]+\")\nfor alamat in [\"budi@contoh.co.id\", \"budi@@contoh\", \"budi contoh.id\"]:\n    print(alamat, \"->\", bool(POLA_EMAIL.fullmatch(alamat)))\n\n# search mengembalikan None kalau tidak ketemu -> cek dulu sebelum .group()\nhasil = re.search(r\"\\d+\", \"tidak ada angka di sini\")\nprint(hasil.group(0) if hasil else \"tidak ada angka\")\n\n# Merapikan spasi berlebih: satu atau lebih whitespace jadi satu spasi biasa\nkotor = \"  Belajar   Python\\tsampai\\n\\nbisa  \"\nprint(repr(re.sub(r\"\\s+\", \" \", kotor).strip()))   # 'Belajar Python sampai bisa'\n\n# Di string PENGGANTI, \\1 (atau \\g<jam>) menunjuk isi grup tangkap\nprint(re.sub(r\"(\\d{2}):(\\d{2}):(\\d{2})\", r\"\\1.\\2\", \"08:15:02 INFO server siap\"))",
            },
            {
                "heading": "Jebakan, dan kapan jangan memakai regex",
                "body": [
                    "Ini jebakan yang paling sering kena:",
                    "  1. Lupa r\"...\". Ini penyebab nomor satu keluhan \"polaku udah benar",
                    "     tapi nggak pernah cocok\".",
                    "  2. re.match artinya bukan \"cocok seluruhnya\". Dia cuma mengikat pola",
                    "     ke awal string. Kalau maksudmu \"seluruh teks harus berbentuk",
                    "     begini\", yang benar re.fullmatch.",
                    "  3. Memanggil .group() pada None. Kalau polanya nggak ketemu, hasilnya",
                    "     None, dan Python menjawab AttributeError: 'NoneType' object has",
                    "     no attribute 'group'. Simpan hasilnya ke variabel dulu, cek, baru",
                    "     pakai.",
                    "  4. findall berubah perilaku begitu polanya punya grup tangkap. Tanpa",
                    "     grup, dia memberi seluruh kecocokan. Dengan satu grup, dia cuma",
                    "     memberi isi grup itu. Dengan dua grup atau lebih, dia memberi",
                    "     tuple. Kalau kurungnya cuma untuk mengelompokkan, tulis (?:...).",
                    "  5. Kuantifier itu serakah: .+ mengambil sepanjang mungkin, lalu",
                    "     mundur secukupnya. Tambahkan ? di belakangnya untuk versi malas.",
                    "  6. Titik nggak pernah cocok dengan newline, kecuali flag re.DOTALL",
                    "     dinyalakan.",
                    "",
                    "Regex juga punya batas. Untuk data berikut, pakai alat lain:",
                    "  HTML / XML  ->  pakai parser sungguhan (html.parser di stdlib)",
                    "  JSON        ->  json.loads",
                    "  CSV         ->  modul csv",
                    "  Path berkas ->  pathlib / os.path, seperti di materi File I/O",
                    "",
                    "Alasannya beda-beda. Tag HTML boleh bersarang tanpa batas, dan secara",
                    "matematis regex nggak sanggup menghitung sarang. Pola yang \"hampir",
                    "jalan\" bakal gagal di halaman pertama yang sedikit berbeda. Untuk JSON,",
                    "json.loads udah ada, udah benar, dan ngerti escape di dalamnya. Untuk",
                    "CSV, koma di dalam tanda kutip (\"Jakarta, Pusat\") merusak setiap",
                    "pemisahan yang naif.",
                    "",
                    "Regex paling cocok untuk teks datar yang polanya tetap: baris log,",
                    "nomor invoice, kode pos, timestamp, atau validasi format. Begitu datanya",
                    "bersarang atau berstruktur, regex alat yang salah.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Formulir pendaftaran memeriksa format nomor HP, email, dan kode pos",
                    "dengan regex. Tim operasional memakainya untuk mengambil nomor resi",
                    "atau nomor pesanan dari teks chat pelanggan, dan untuk menyaring baris",
                    "log. Satu pola pendek menggantikan belasan baris find() dan split().",
                    "",
                    "Kasus kecil: formulir lomba menetapkan aturan nomor HP: diawali 08,",
                    "cuma berisi angka, dan panjangnya 10 sampai 13 digit. Kamu diminta",
                    "menolak isian yang nggak memenuhi aturan itu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Terjemahkan aturannya jadi pola. Dua digit pertama 08, sisanya 8",
                    "     sampai 11 digit, jadi totalnya 10 sampai 13.",
                    "  2. Seluruh isian harus cocok, jadi pakai fullmatch:",
                    "      import re",
                    "      POLA_HP = re.compile(r\"08\\d{8,11}\")",
                    "      for hp in [\"081234567890\", \"0812-3456\", \"08123456789012345\"]:",
                    "          print(hp, bool(POLA_HP.fullmatch(hp.strip())))",
                    "  3. Jalankan. Hanya nomor pertama yang True. Yang kedua mengandung",
                    "     tanda hubung, yang ketiga kepanjangan.",
                    "  4. Cek kasus pinggir: isian dengan spasi di ujung karena pengguna",
                    "     menyalin dari chat. Makanya isiannya di-strip() dulu.",
                    "",
                    "Jebakan: re.match di sini meloloskan nomor yang kepanjangan, karena ia",
                    "cuma memeriksa bagian awal teks. Untuk validasi format, pakai",
                    "fullmatch.",
                ]
            },
        ],
    },
    {
        "title": "36. Iterator & Generator",
        "sections": [
            {
                "body": [
                    "Ada dua istilah yang sering ketuker di sini: iterable dan iterator.",
                    "",
                    "Iterable adalah objek yang bisa kamu pakai di for-loop, misalnya list,",
                    "str, atau dict. Iterator adalah objek yang ingat sudah sampai mana. Dia",
                    "punya method __next__() untuk mengambil elemen satu per satu.",
                    "",
                    "Kamu bisa bikin iterator dari iterable pakai iter(), lalu mengambil",
                    "isinya pakai next():",
                    "",
                    "  angka = [1, 2, 3]",
                    "  it = iter(angka)       # ubah iterable jadi iterator",
                    "  print(next(it))        # 1",
                    "  print(next(it))        # 2",
                    "  print(next(it))        # 3",
                    "  print(next(it))        # StopIteration error (habis)",
                    "",
                    "Waktu isinya habis, next() melempar StopIteration. For-loop di Python",
                    "ternyata kerjanya persis begitu. Di belakang layar dia memanggil iter()",
                    "dan next() secara otomatis, sampai StopIteration muncul, lalu berhenti",
                    "dengan rapi.",
                    "",
                    "Cara paling gampang bikin iterator sendiri adalah generator, yaitu",
                    "fungsi yang memakai yield sebagai ganti return. Contohnya di bawah.",
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
                    "Generator paling berguna untuk tiga hal:",
                    "  1. Memproses file atau data yang besar sekali, baris per baris, tanpa",
                    "     memuat semuanya ke memori sekaligus.",
                    "  2. Bikin stream (aliran data) yang nggak ada habisnya, seperti contoh",
                    "     genap_tak_terbatas() di atas.",
                    "  3. Pipeline, yaitu pemrosesan data bertahap yang hasil satu tahap",
                    "     langsung dioper ke tahap berikutnya. Mirip konsep Stream di Java.",
                    "",
                    "Ada juga generator expression, versi ringkas generator. Bentuknya mirip",
                    "list comprehension, tapi pakai kurung biasa:",
                    "  kuadrat_gen = (x**2 for x in range(10))",
                    "  print(sum(kuadrat_gen))    # dihitung tanpa buat list utuh dulu",
                    "",
                    "Terakhir, bedanya return dan yield. return mengembalikan nilai sekali,",
                    "lalu fungsinya selesai total. yield juga mengembalikan nilai, tapi",
                    "fungsinya cuma dibekukan. Nanti fungsi itu bisa dilanjutkan lagi dari",
                    "titik yield terakhir.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Berkas log server bisa berukuran gigabyte, dan data penjualan setahun",
                    "bisa berisi jutaan baris. Memuat semuanya ke list menghabiskan memori.",
                    "Generator membaca dan menyaring satu baris setiap kali diminta, jadi",
                    "memori yang dipakai tetap kecil sebesar apa pun berkasnya.",
                    "",
                    "Kasus kecil: berkas server.log berisi baris seperti \"08:15 INFO server",
                    "siap\" dan \"08:16 ERROR disk penuh\". Tim ingin tahu berapa baris ERROR,",
                    "tanpa memuat seluruh berkas ke memori.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya berkas yang ukurannya bisa gigabyte. Keluarannya satu",
                    "     angka.",
                    "  2. Tulis generator yang menyerahkan baris ERROR satu per satu:",
                    "      def baris_error(baris_baris):",
                    "          for baris in baris_baris:",
                    "              if \" ERROR \" in baris:",
                    "                  yield baris.strip()",
                    "  3. Objek berkas sendiri sudah memberi baris satu per satu, jadi",
                    "     sambungkan saja: sum(1 for _ in baris_error(f)) di dalam blok with",
                    "     open(). Untuk dua contoh baris tadi, hasilnya 1.",
                    "  4. Cek kasus pinggir: generator habis sekali pakai. Kalau perlu",
                    "     menghitung lagi, buat generator baru dari berkas yang dibuka ulang.",
                    "",
                    "Jebakan: f.readlines() memuat seluruh berkas ke list. Itu persis yang",
                    "mau dihindari.",
                ]
            },
        ],
    },
    {
        "title": "37. itertools & yield from",
        "sections": [
            {
                "body": [
                    "itertools adalah kotak perkakas iterator yang udah ikut terpasang",
                    "bersama Python. Isinya fungsi untuk menyambung, memotong, mengulang,",
                    "dan memasangkan iterable tanpa bikin list perantara. Kamu nggak perlu",
                    "pip install apa pun, cukup di-import.",
                    "",
                    "Percobaan pertama dengan itertools biasanya bikin bingung:",
                    "",
                    "  from itertools import chain",
                    "  print(chain([1, 2], [3]))",
                    "  # <itertools.chain object at 0x7f3a...>",
                    "",
                    "Itu bukan error, dan datanya nggak hilang. Hampir semua fungsi",
                    "itertools mengembalikan iterator, yang sifatnya lazy seperti yang udah",
                    "dibahas di materi Iterator & Generator. Lazy artinya isinya belum",
                    "dihitung sampai ada yang meminta. Untuk melihat isinya, bungkus pakai",
                    "list() atau tuple(), atau langsung pakai di for-loop:",
                    "",
                    "  print(list(chain([1, 2], [3])))   # [1, 2, 3]",
                    "",
                    "Akibat berikutnya lebih menjebak: iterator itu sekali pakai. Sesudah",
                    "dibaca sampai habis, pembacaan kedua cuma memberi hasil kosong, tanpa",
                    "error sama sekali. Gejalanya baru muncul jauh kemudian, dalam bentuk",
                    "\"datanya tiba-tiba kosong\" di baris lain. Kalau memang perlu dipakai",
                    "dua kali, simpan hasilnya ke list.",
                ],
            },
            {
                "heading": "Menyambung & memotong: chain, islice, count, cycle, repeat",
                "body": [
                    "Fungsi-fungsi untuk menyambung dan memotong:",
                    "  chain(a, b, c)          sambung beberapa iterable jadi satu",
                    "  chain.from_iterable(x)  sama, tapi iterable-nya dalam 1 wadah",
                    "  islice(it, ...)         'slice' untuk iterator - TANPA indeks",
                    "                          negatif, karena iterator tidak tahu",
                    "                          di mana ujungnya",
                    "  count(mulai, langkah)   angka menaik TANPA HENTI",
                    "  cycle(iterable)         isinya diputar berulang TANPA HENTI",
                    "  repeat(nilai, n)        nilai sama n kali (tanpa n: tak henti)",
                    "",
                    "Jebakan: count, cycle, dan repeat tanpa n nggak pernah berhenti",
                    "sendiri. list(count(1)) bakal menggantung dan menghabiskan seluruh RAM.",
                    "Batasi pakai islice() atau pakai break.",
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
                    "product() itu loop bersarang yang ditulis mendatar. Dua loop bersarang",
                    "jadi satu baris. Sepuluh loop bersarang pun tetap satu baris. Makanya",
                    "product() sering muncul di kode nyata. Alasannya bukan kecepatan.",
                    "Alasannya kodenya nggak makin menjorok ke kanan tiap kali loop",
                    "ditambah.",
                    "",
                    "  product(a, b)         semua pasangan a x b (yang paling kanan",
                    "                        berputar paling cepat)",
                    "  product(a, repeat=n)  a dipasangkan dengan DIRINYA SENDIRI",
                    "  combinations(x, n)    pilih n, urutan TIDAK dihitung: AB = BA",
                    "  permutations(x, n)    susun n, urutan DIHITUNG: AB != BA",
                    "",
                    "Hati-hati dengan jumlahnya. product([0, 1], repeat=20) berisi lebih",
                    "dari sejuta tuple. Selama masih berupa iterator, itu aman. Begitu kamu",
                    "bungkus pakai list(), semuanya dibuat di RAM sekaligus.",
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
                "heading": "groupby: datanya wajib diurutkan lebih dulu",
                "body": [
                    "groupby() mengelompokkan elemen berurutan yang key-nya sama. Kata",
                    "pentingnya \"berurutan\". groupby() nggak mengurutkan apa pun. Dia cuma",
                    "memotong setiap kali nilai key berubah dari elemen sebelumnya.",
                    "",
                    "Akibatnya, data yang belum diurutkan menghasilkan grup yang pecah.",
                    "Kategori yang sama bisa muncul dua-tiga kali. Nggak ada error, nggak",
                    "ada peringatan, hasilnya cuma salah. Aturannya: sort() dulu dengan key",
                    "yang persis sama dengan key groupby.",
                    "",
                    "Jebakan kedua: iterator anggota tiap grup hangus begitu kita maju ke",
                    "grup berikutnya. Jadi list(groupby(...)) memberi daftar grup yang",
                    "isinya kosong semua. Olah anggotanya di dalam loop, atau salin pakai",
                    "list() saat itu juga.",
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
                    "yield from artinya \"sambungkan generator itu langsung ke pemanggilku\".",
                    "Salah baca yang paling sering: mengira 'yield generator_lain()' sama",
                    "aja. Ternyata beda. Tanpa kata from, yang keluar adalah objek",
                    "generatornya, jadi hasilnya [<generator object ... at 0x...>], bukan",
                    "isinya. Bedanya cuma satu kata, tapi yang keluar jadi beda total.",
                    "",
                    "Selain memendekkan for-loop, yield from membawa dua hal lagi:",
                    "  - Generator rekursif, yaitu generator yang memanggil dirinya sendiri,",
                    "    jadi enak ditulis. Lihat ratakan() di bawah. Itu pola baku untuk",
                    "    menelusuri list atau pohon bersarang tanpa pernah bikin list besar",
                    "    di memori.",
                    "  - Nilai return dari generator anak ikut tertangkap.",
                    "",
                    "Perhatikan: return di dalam generator nggak mengirim nilai ke for-loop.",
                    "Artinya cuma \"generator ini selesai\", dan nilainya diselipkan ke",
                    "StopIteration.value. Makanya 'jumlah = yield from hitung(...)' adalah",
                    "cara wajar membacanya. For-loop biasa nggak bakal pernah melihat angka",
                    "itu.",
                    "",
                    "Sekilas soal .send(). yield juga bisa dipakai sebagai ekspresi yang",
                    "menerima data dari luar, kebalikan dari mengirim.",
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
                    "Ini cara pertama Python untuk bikin coroutine, jauh sebelum async/await",
                    "ada. Sekarang bentuk ini jarang ditulis orang. Cukup kenali bentuknya",
                    "kalau ketemu di kode lama.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online memakai product() untuk membuat semua varian barang, misalnya",
                    "setiap ukuran dikali setiap warna. Jadwal piket atau giliran shift yang",
                    "berputar ditulis dengan cycle(). Rekap per kategori memakai groupby()",
                    "sesudah datanya diurutkan.",
                    "",
                    "Kasus kecil: kantor punya lima hari kerja dan tiga petugas piket, Andi,",
                    "Budi, dan Citra. Piketnya bergiliran, jadi sesudah Citra kembali ke",
                    "Andi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya daftar hari dan daftar petugas. Keluarannya pasangan",
                    "     hari dan petugas.",
                    "  2. cycle() memutar petugas tanpa henti, dan zip() berhenti begitu",
                    "     daftar hari habis:",
                    "      from itertools import cycle",
                    "      hari = [\"Senin\", \"Selasa\", \"Rabu\", \"Kamis\", \"Jumat\"]",
                    "      petugas = [\"Andi\", \"Budi\", \"Citra\"]",
                    "      for h, p in zip(hari, cycle(petugas)):",
                    "          print(h, p)",
                    "  3. Jalankan. Kamis kembali ke Andi, dan Jumat dapat Budi.",
                    "  4. Cek kasus pinggir: petugas lebih banyak daripada hari, misalnya",
                    "     tujuh orang. zip() tetap berhenti di Jumat, jadi dua petugas",
                    "     terakhir belum kebagian minggu ini.",
                    "",
                    "Jebakan: list(cycle(petugas)) nggak pernah selesai dan menghabiskan",
                    "memori. cycle() selalu dipasangkan dengan sesuatu yang berhenti.",
                ]
            },
        ],
    },
    {
        "title": "38. Decorator & Context Manager",
        "sections": [
            {
                "body": [
                    "Decorator adalah fungsi yang membungkus fungsi lain untuk menambah",
                    "perilaku baru, tanpa mengubah kode fungsi aslinya. Cara pakainya: tulis",
                    "simbol @ dan nama decorator-nya tepat di atas definisi fungsi.",
                    "",
                    "Ini bisa jalan karena di Python fungsi adalah first-class object.",
                    "Artinya fungsi diperlakukan seperti nilai biasa: bisa disimpan ke",
                    "variabel, dikirim sebagai argumen ke fungsi lain, dan seterusnya.",
                    "Contoh di bawah mengukur berapa lama sebuah fungsi berjalan.",
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
                    "Beberapa decorator bawaan Python yang sering dipakai:",
                    "  @staticmethod / @classmethod  -> di dalam class (materi OOP)",
                    "  @property                      -> getter/setter (materi encapsulation)",
                    "  @functools.lru_cache            -> cache hasil fungsi otomatis",
                    "",
                    "Cache artinya simpanan hasil. Dengan lru_cache, hasil fungsi untuk",
                    "argumen yang sama cukup dihitung sekali. Panggilan berikutnya langsung",
                    "mengambil hasil yang udah disimpan. Contohnya fibonacci:",
                    "",
                    "  from functools import lru_cache",
                    "  @lru_cache(maxsize=None)",
                    "  def fibonacci(n):",
                    "      if n < 2: return n",
                    "      return fibonacci(n-1) + fibonacci(n-2)",
                    "  # tanpa cache, ini SANGAT lambat untuk n besar;",
                    "  # dengan cache, hasil yang sudah dihitung disimpan otomatis.",
                    "",
                    "Sesudah decorator, contoh di bawah membahas context manager, yaitu",
                    "benda yang bisa dipakai di blok with. Kamu bisa bikin sendiri dengan",
                    "class yang punya method __enter__ dan __exit__, atau dengan decorator",
                    "@contextmanager.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Framework web memakai decorator untuk pekerjaan yang sama di banyak",
                    "fungsi: memeriksa login, mencatat log, atau menyimpan hasil di cache.",
                    "Pengecekannya ditulis sekali, lalu dipasang dengan satu baris @ di atas",
                    "tiap fungsi. Context manager dipakai untuk hal yang wajib dibereskan,",
                    "seperti menutup berkas atau koneksi database.",
                    "",
                    "Kasus kecil: aplikasi nilai sekolah punya fungsi hapus_nilai() dan",
                    "ubah_jadwal() yang cuma boleh dijalankan admin. Pengecekan peran di",
                    "awal tiap fungsi sudah tersalin di mana-mana.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pengecekan yang sama di awal banyak fungsi adalah tanda untuk",
                    "     memakai decorator.",
                    "  2. Tulis decorator yang memeriksa peran dulu, baru memanggil fungsi",
                    "     aslinya:",
                    "      def wajib_admin(fungsi):",
                    "          def wrapper(peran, *args, **kwargs):",
                    "              if peran != \"admin\":",
                    "                  return \"ditolak: khusus admin\"",
                    "              return fungsi(peran, *args, **kwargs)",
                    "          return wrapper",
                    "  3. Pasang @wajib_admin di atas def hapus_nilai(peran, nama). Panggilan",
                    "     dengan peran \"guru\" mendapat pesan ditolak, dan fungsi aslinya",
                    "     nggak pernah jalan.",
                    "  4. Cek kasus pinggir: panggilan dengan peran \"admin\" harus tetap",
                    "     mengembalikan hasil fungsi aslinya, bukan None.",
                    "",
                    "Jebakan: lupa menulis return di depan fungsi(peran, *args, **kwargs).",
                    "Fungsinya tetap jalan, tapi hasilnya hilang dan pemanggil menerima",
                    "None.",
                ]
            },
        ],
    },
    {
        "title": "39. Introspeksi Objek & Decorator Lanjutan",
        "sections": [
            {
                "body": [
                    "Materi Decorator barusan memakai fungsi.__name__, dan Latihan 16 juga",
                    "mewajibkannya, tapi belum dijelaskan nilai itu datang dari mana.",
                    "Padahal __name__ yang pernah kamu lihat sebelumnya cuma yang ada di",
                    "if __name__ == \"__main__\", dan di sana isinya \"__main__\". Dua-duanya",
                    "benar, tapi dua-duanya barang yang beda:",
                    "",
                    "  __name__ polos di tingkat modul  -> nama MODUL yang sedang berjalan",
                    "  fungsi.__name__                  -> nama FUNGSI itu, mis. \"proses_data\"",
                    "",
                    "Yang menyatukan keduanya: di Python semua hal adalah objek, dan objek",
                    "punya atribut. Angka, string, list, class, modul, bahkan fungsi.",
                    "Fungsi itu benda. Dia bisa disimpan ke variabel, dioper sebagai argumen",
                    "(itu udah kamu pakai di materi Lambda), dan satu lagi yang belum pernah",
                    "disebut: isinya bisa diintip.",
                    "",
                    "Setiap fungsi otomatis punya atribut ini, tanpa kamu tulis:",
                    "  fungsi.__name__      nama saat ia didefinisikan, berupa str",
                    "  fungsi.__doc__       docstring-nya, atau None kalau tidak ditulis",
                    "  fungsi.__module__    nama modul tempat ia ditulis",
                    "  fungsi.__qualname__  nama lengkap termasuk class pembungkusnya",
                    "  fungsi.__dict__      kotak kosong, tempat siapa pun boleh",
                    "                       menempel atribut baru",
                    "",
                    "Membaca isi sebuah objek waktu program sedang berjalan namanya",
                    "introspeksi. Ini dipakai di mana-mana. Django membaca field model-mu",
                    "dengan cara ini. Flask mendaftar rute dari __name__ fungsimu. pytest",
                    "menemukan test dari nama yang berawalan test_. ORM mengubah objek jadi",
                    "baris tabel dengan membaca atributnya satu per satu. Kalau kamu belum",
                    "paham bab ini, semua pustaka itu bakal terus terasa seperti sulap yang",
                    "nggak bisa kamu tiru sendiri.",
                ],
            },
            {
                "heading": "Mengintip objek yang isinya belum kamu ketahui",
                "code": "def sapa(nama):\n    \"\"\"Menyapa seseorang dengan ramah.\"\"\"\n    return f\"Halo, {nama}!\"\n\n# Fungsi itu OBJEK. Buktinya: ia punya atribut yang bisa dibaca seperti objek lain.\nprint(sapa.__name__)       # sapa\nprint(sapa.__doc__)        # Menyapa seseorang dengan ramah.\nprint(sapa.__module__)     # __main__   <- nama MODUL, beda barang dengan __name__ di atas\nprint(sapa.__dict__)       # {}         <- kotak atribut tambahan, awalnya kosong\n\n# Kotak itu boleh diisi siapa saja. Begitulah framework menempel catatan ke fungsimu.\nsapa.rute = \"/sapa\"\nprint(sapa.__dict__)       # {'rute': '/sapa'}\nprint(sapa.rute)           # /sapa\n\n\nclass Kucing:\n    def __init__(self, nama, umur):\n        self.nama = nama\n        self.umur = umur\n\n    def bersuara(self):\n        return \"Meong\"\n\n\nprint(Kucing.bersuara.__qualname__)   # Kucing.bersuara  -- __name__ cuma 'bersuara'\n\nc = Kucing(\"Oyen\", 3)\nprint(type(c))                # <class '__main__.Kucing'>\nprint(c.__class__.__name__)   # Kucing  -- nama class-nya SAJA, tanpa bungkus <class ...>\n\n# vars(obj) = isi __dict__ objek itu: hanya atribut yang benar-benar dipasang padanya.\nprint(vars(c))                # {'nama': 'Oyen', 'umur': 3}\nprint(c.__dict__)             # sama persis; vars() memang membaca __dict__\n\n# dir(obj) = SEMUA nama yang bisa diakses dari objek, termasuk warisan dan dunder.\nprint(len(dir(c)) > 20)                                # True, daftarnya panjang sekali\nprint([n for n in dir(c) if not n.startswith(\"__\")])   # ['bersuara', 'nama', 'umur']\n\n# Pakai yang mana: vars() untuk \"apa isi objek ini\", dir() untuk \"apa yang bisa\n# kulakukan padanya\". Keduanya alat pertama saat kamu memegang objek asing di REPL.",
            },
            {
                "heading": "getattr, setattr, hasattr: atribut lewat nama berupa string",
                "body": [
                    "Sampai sekarang, setiap atribut yang kamu baca namanya ditulis langsung",
                    "di kode, misalnya p.harga. Itu cukup selama kamu sendiri tahu isinya",
                    "waktu mengetik. Framework nggak pernah tahu. Django ditulis",
                    "bertahun-tahun sebelum class-mu ada. Yang dia punya cuma nama atribut",
                    "berupa string, dan fungsi-fungsi ini jembatannya:",
                    "",
                    "  getattr(obj, \"harga\")        sama dengan obj.harga",
                    "  getattr(obj, \"harga\", 0)     ... tapi kembalikan 0 kalau atributnya",
                    "                               tidak ada",
                    "  setattr(obj, \"harga\", 500)   sama dengan obj.harga = 500",
                    "  hasattr(obj, \"harga\")        True/False, tanpa melempar error",
                    "  delattr(obj, \"harga\")        sama dengan del obj.harga",
                    "",
                    "Bedanya cuma satu, tapi efeknya besar: nama atributnya sekarang jadi",
                    "data. Nama itu boleh datang dari daftar kolom, dari berkas konfigurasi,",
                    "atau dari input pengguna.",
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
                    "Kenapa @lru_cache(maxsize=None) pakai kurung, sedangkan @ukur_waktu",
                    "nggak? Aturannya begini: apa pun yang ditulis sesudah @ dijalankan",
                    "dulu, dan hasilnya harus sesuatu yang siap menerima fungsimu.",
                    "",
                    "  @ukur_waktu",
                    "      ukur_waktu sudah berupa decorator -> ukur_waktu(fungsi)",
                    "  @lru_cache(maxsize=None)",
                    "      lru_cache(maxsize=None) DIPANGGIL dulu; nilai kembaliannya",
                    "      yang jadi decorator, baru menerima fungsi",
                    "",
                    "Bentuk kedua butuh tiga lapis fungsi bersarang: pabrik, decorator, dan",
                    "wrapper. Lapis terluar cuma ada untuk menyimpan argumennya, dan yang",
                    "menyimpannya adalah closure (materi Scope, Closure & nonlocal). Bentuk",
                    "tiga lapis ini yang bakal kamu temui di hampir semua decorator di dunia",
                    "nyata: @app.route(\"/produk\") di Flask, @pytest.mark.parametrize(...) di",
                    "pytest, dan @retry(kali=3) di pustaka ketahanan.",
                    "",
                    "Jebakan: lupa kurungnya. Kalau kamu nulis @ulangi tanpa (kali=3),",
                    "fungsimu malah dikirim sebagai argumen kali, dan yang terpasang ke nama",
                    "fungsimu adalah objek decorator. Errornya baru muncul jauh kemudian,",
                    "dengan pesan yang nggak menyebut decorator sama sekali.",
                    "",
                    "Kalau decorator ditumpuk, yang paling dekat dengan def dipasang lebih",
                    "dulu, jadi urutannya dari bawah ke atas. Tapi waktu fungsinya dipanggil,",
                    "pembungkus paling atas yang jalan duluan.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fitur \"ekspor ke Excel\" di aplikasi admin biasanya membiarkan pengguna",
                    "memilih kolom. Kode di baliknya nggak menulis satu if per kolom. Ia",
                    "membaca atribut lewat namanya dengan getattr(), mirip cara framework",
                    "seperti Django membaca field model.",
                    "",
                    "Kasus kecil: objek Produk punya atribut nama, harga, dan stok. Admin A",
                    "mengekspor kolom \"nama,harga\", admin B mengekspor \"nama,stok\". Satu",
                    "fungsi harus melayani dua-duanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya objek dan daftar nama kolom berupa teks. Keluarannya",
                    "     satu baris teks dipisah titik koma.",
                    "  2. Ambil tiap atribut lewat namanya, dengan nilai cadangan \"-\":",
                    "      def ke_baris(objek, kolom):",
                    "          return \";\".join(str(getattr(objek, k, \"-\")) for k in kolom)",
                    "      kolom = \"nama,harga\".split(\",\")",
                    "      print(ke_baris(Produk(\"Kopi\", 25000, 4), kolom))",
                    "  3. Jalankan. Hasilnya Kopi;25000. Dengan \"nama,stok\", hasilnya",
                    "     Kopi;4.",
                    "  4. Cek kasus pinggir: kolom salah ketik, misalnya \"hrga\". Tanpa nilai",
                    "     cadangan, getattr() melempar AttributeError. Dengan \"-\", kolomnya",
                    "     terisi tanda strip.",
                    "",
                    "Ingat: tanda strip menyembunyikan salah ketik. Periksa dulu dengan",
                    "hasattr(), lalu beri tahu admin kolom mana yang nggak dikenal.",
                ]
            },
        ],
    },
    {
        "title": "40. Konkurensi: Thread, Proses & GIL",
        "sections": [
            {
                "body": [
                    "Sampai sini semua program kita mengerjakan satu hal pada satu waktu:",
                    "baris demi baris, dari atas ke bawah. Konkurensi adalah cara menyusun",
                    "program supaya banyak pekerjaan bisa maju bergantian, tanpa harus",
                    "saling menunggu sampai yang lain tuntas.",
                    "",
                    "Ada dua kata yang sering ketuker:",
                    "  concurrency (kebersamaan)",
                    "      banyak tugas SEDANG berjalan, bergantian memakai satu inti CPU.",
                    "      Satu koki menggoreng sambil menunggu air di panci lain mendidih.",
                    "  parallelism (kesejajaran)",
                    "      banyak tugas berjalan BENAR-BENAR serentak di beberapa inti CPU.",
                    "      Empat koki, empat kompor.",
                    "",
                    "Mana yang kamu butuhkan ditentukan oleh jenis pekerjaannya:",
                    "  I/O-bound  -> waktunya habis MENUNGGU. Unduh halaman, baca berkas",
                    "                besar, query database, panggil API. Selama menunggu,",
                    "                CPU-nya menganggur.",
                    "  CPU-bound  -> waktunya habis MENGHITUNG. Kompresi gambar, enkripsi,",
                    "                olah angka, parsing berkas raksasa. CPU-nya penuh dari",
                    "                awal sampai akhir.",
                    "",
                    "GIL (Global Interpreter Lock)",
                    "",
                    "CPython, yaitu interpreter yang dipasang orang dari python.org, memakai",
                    "satu kunci besar bernama GIL. Aturannya: cuma satu thread yang boleh",
                    "menjalankan bytecode Python pada satu waktu. Thread itu jalur kerja di",
                    "dalam satu program, dan bytecode itu bentuk kode Python yang sudah",
                    "diterjemahkan supaya bisa dijalankan interpreter.",
                    "",
                    "Kunci itu sengaja dibuat begitu. Dengan satu kunci, manajemen memorinya",
                    "jadi jauh lebih sederhana, dan kode yang cuma pakai satu thread jadi",
                    "cepat. Akibatnya:",
                    "  - Menambah thread nggak mempercepat pekerjaan CPU-bound. Empat thread",
                    "    yang sama-sama menghitung tetap bergantian di satu inti, jadi",
                    "    totalnya segitu juga.",
                    "  - Menambah thread bikin pekerjaan I/O-bound jauh lebih cepat. Kunci",
                    "    itu dilepas selama sebuah thread menunggu jaringan, disk, atau",
                    "    time.sleep().",
                    "  - Kunci itu nggak melindungimu dari race condition, yaitu dua thread",
                    "    yang mengubah data yang sama berbarengan sampai hasilnya kacau. Yang",
                    "    dilindungi kunci itu adalah interpreter, bukan data milikmu.",
                    "",
                    "Kalau kamu butuh CPU yang jalan sejajar sungguhan, jalankan beberapa",
                    "proses. Tiap proses punya interpreter, memori, dan GIL sendiri-sendiri.",
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
                    "ProcessPoolExecutor punya API yang sama persis dengan",
                    "ThreadPoolExecutor: submit, map, as_completed. Bedanya, pekerjanya",
                    "adalah proses sistem operasi, bukan thread. Tiap proses punya GIL",
                    "sendiri, jadi hitungannya betul-betul jalan sejajar.",
                    "",
                    "Ada dua harga yang harus dibayar, yang nggak ada pada thread:",
                    "  1. Menyalakan proses baru butuh waktu, puluhan sampai ratusan",
                    "     milidetik.",
                    "  2. Argumen dan hasilnya disalin lewat pickle, nggak dibagi bersama.",
                    "     pickle adalah cara Python mengubah objek jadi bytes supaya bisa",
                    "     dikirim ke proses lain. Kalau datanya besar, ongkos menyalinnya",
                    "     bisa lebih mahal daripada waktu yang dihemat.",
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
                "heading": "Memilih model konkurensi dan jebakannya",
                "body": [
                    "Cara memilih, dari yang paling murah:",
                    "  1. Nggak pakai apa-apa. Konkurensi menambah bug yang cuma muncul",
                    "     sesekali dan susah diulang. Kalau versi berurutannya udah cukup",
                    "     cepat, berhenti di situ. Ukur dulu pakai time.perf_counter(),",
                    "     jangan menebak.",
                    "  2. Pekerjaan yang menunggu (jaringan, berkas, database) -> thread.",
                    "     ThreadPoolExecutor hampir selalu jawabannya. Jarang ada alasan",
                    "     bikin Thread satu per satu.",
                    "  3. Pekerjaan yang menghitung -> proses. Pakai ProcessPoolExecutor",
                    "     dengan jumlah pekerja kira-kira sebanyak inti CPU",
                    "     (multiprocessing.cpu_count()).",
                    "  4. Ribuan koneksi yang menunggu sekaligus -> async/await di materi",
                    "     berikutnya, karena seribu thread berarti seribu tumpukan memori.",
                    "",
                    "Jebakan yang paling sering kena:",
                    "  - Kode yang benar waktu sekali dijalankan belum tentu aman. Race",
                    "    condition bisa sembunyi berbulan-bulan, lalu muncul waktu servernya",
                    "    lagi sibuk.",
                    "  - Future yang hasilnya nggak pernah diambil berarti error yang nggak",
                    "    pernah kelihatan. ex.map() juga mengembalikan iterator, jadi",
                    "    errornya baru muncul waktu hasilnya dibaca satu per satu.",
                    "  - Lupa join() atau nggak pakai blok 'with' pada executor bikin",
                    "    program induk bisa selesai duluan, dan pekerjaannya terpotong di",
                    "    tengah jalan.",
                    "  - Tanpa 'if __name__ == \"__main__\":', proses anak mengimpor ulang",
                    "    berkasmu, bikin pool baru lagi, yang bikin proses lagi, dan begitu",
                    "    terus tanpa henti.",
                    "  - Antar-proses, data disalin, nggak dibagi. Mengubah variabel global",
                    "    di proses anak sama sekali nggak kelihatan di induknya.",
                    "  - lambda, fungsi di dalam fungsi, koneksi, dan objek file nggak bisa",
                    "    di-pickle. Fungsi untuk ProcessPoolExecutor harus fungsi biasa di",
                    "    level atas modul.",
                    "  - Kebanyakan pekerja proses malah memperlambat. Tiap proses makan",
                    "    memori sendiri, dan mereka rebutan inti yang jumlahnya tetap",
                    "    segitu.",
                    "",
                    "Nama-nama lain yang bakal kamu temui waktu membaca kode orang:",
                    "  threading.Lock / RLock   penjaga data bersama (RLock boleh dikunci",
                    "                           berkali-kali oleh thread yang sama, Lock",
                    "                           tidak - itu deadlock)",
                    "  threading.Event          isyarat \"sudah boleh jalan\" antar-thread",
                    "  queue.Queue              antrean yang SUDAH aman dipakai banyak thread",
                    "  multiprocessing.Process  proses tunggal, saudara dari threading.Thread",
                    "  daemon=True              thread yang ikut mati begitu program utama",
                    "                           selesai",
                    "",
                    "Catatan: mulai Python 3.13 ada build eksperimental bernama",
                    "\"free-threaded\" yang GIL-nya bisa dimatikan. sys._is_gil_enabled()",
                    "memberi tahu statusnya. Python yang biasa dipasang orang masih memakai",
                    "GIL, jadi semua aturan di atas tetap berlaku. Kode yang bebas race",
                    "condition tetap aman di dua-duanya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang mengecek status puluhan resi ke server kurir",
                    "menghabiskan hampir seluruh waktunya untuk menunggu jawaban. Pekerjaan",
                    "seperti itu dipercepat dengan thread. Pekerjaan yang menghitung,",
                    "seperti mengecilkan ribuan foto produk, butuh proses, karena GIL",
                    "membuat thread menghitung bergantian.",
                    "",
                    "Kasus kecil: ada 20 nomor resi yang harus dicek. Fungsi cek_resi(nomor)",
                    "menunggu sekitar satu detik untuk tiap jawaban. Kalau berurutan, totalnya",
                    "20 detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali jenis pekerjaannya. Waktunya habis untuk menunggu jaringan,",
                    "     jadi ini I/O-bound, dan thread cocok.",
                    "  2. Serahkan daftar resi ke kolam thread. map() mengembalikan hasil",
                    "     sesuai urutan masukan:",
                    "      from concurrent.futures import ThreadPoolExecutor",
                    "      with ThreadPoolExecutor(max_workers=5) as ex:",
                    "          hasil = list(ex.map(cek_resi, daftar_resi))",
                    "  3. Dengan 5 pekerja, 20 panggilan berjalan dalam 4 gelombang. Totalnya",
                    "     sekitar 4 detik, bukan 20.",
                    "  4. Cek kasus pinggir: satu resi yang membuat cek_resi() error. Error-nya",
                    "     baru muncul waktu hasilnya dibaca oleh list(), jadi tangkap di",
                    "     sana atau di dalam cek_resi().",
                    "",
                    "Jebakan: jumlah pekerja jangan asal besar. Server kurir bisa membatasi",
                    "jumlah permintaan, dan seratus thread cuma membuat permintaanmu ditolak.",
                ]
            },
        ],
    },
    {
        "title": "41. Asinkron: async, await & asyncio",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya membahas dua cara mengerjakan banyak hal sekaligus:",
                    "thread dan proses. asyncio adalah cara ketiga, dan bentuknya paling",
                    "asing. Soalnya asyncio menambah kata kunci baru ke bahasanya, yaitu",
                    "async dan await. Jadi isinya lebih dari sekadar modul yang di-import.",
                    "",
                    "Masalah yang dipecahkan asyncio sempit tapi umum sekali: program yang",
                    "kebanyakan menunggu. Menunggu jawaban server, menunggu query database,",
                    "menunggu berkas dibaca dari disk. Selama menunggu, CPU nggak",
                    "mengerjakan apa pun. Programnya berhenti di satu baris kode.",
                    "",
                    "Bayangkan satu pelayan warung yang cekatan. Dia nggak berdiri nunggu",
                    "masakan meja 1 matang. Sambil menunggu, dia mencatat pesanan meja 2,",
                    "lalu meja 3. Pelayannya cuma satu, tapi hampir nggak ada waktu yang",
                    "terbuang. Begitulah cara kerja asyncio: satu thread yang nggak pernah",
                    "menganggur. Yang dipakai bukan banyak thread yang jalan bareng.",
                    "",
                    "Ada tiga istilah yang perlu jelas dulu:",
                    "  - coroutine: fungsi yang ditulis dengan 'async def'. Fungsi ini bisa",
                    "    dibekukan di tengah jalan lalu dilanjutkan lagi, persis seperti",
                    "    generator di materi Iterator & Generator. Bedanya, yang",
                    "    membangunkannya event loop, dan next() nggak dipakai.",
                    "  - await: artinya \"aku menunggu hasil ini, sementara itu pakai",
                    "    giliranku untuk yang lain\". await cuma boleh ditulis di dalam async",
                    "    def. Di luar itu hasilnya SyntaxError.",
                    "  - event loop: penjadwal yang memegang antrean coroutine dan membagi",
                    "    giliran. Kamu nggak bikin sendiri. asyncio.run() yang menyalakan",
                    "    lalu mematikannya, dan itu satu-satunya pintu masuk dari kode biasa",
                    "    ke dunia async.",
                    "",
                    "Satu akibat yang paling sering disalahpahami: giliran cuma pindah di",
                    "titik await. Di antara dua await, kodemu jalan sendirian dan nggak bisa",
                    "diserobot. Kabar baiknya, race condition yang jadi masalah di thread",
                    "pada materi sebelumnya hampir nggak ada di sini. Kabar buruknya, satu",
                    "baris lambat yang nggak pakai await bikin seluruh program berhenti.",
                ],
            },
            {
                "heading": "async def menghasilkan coroutine, bukan hasil",
                "body": [
                    "Ini jebakan nomor satu, dan jebakan ini menipu karena nggak ada error",
                    "yang mencolok:",
                    "",
                    "  hasil = ambil_data()      # hasil BUKAN data. hasil adalah objek coroutine.",
                    "",
                    "Python belum menjalankan satu baris pun di dalam ambil_data(). Yang kamu",
                    "pegang cuma kupon yang masih harus ditukar. Kalau kupon itu dibuang",
                    "tanpa pernah ditukar, Python mengeluh waktu objeknya dibersihkan:",
                    "",
                    "  RuntimeWarning: coroutine 'ambil_data' was never awaited",
                    "",
                    "Perhatikan: yang muncul Warning, bukan Error. Program tetap selesai",
                    "dengan status sukses, padahal nggak mengerjakan apa-apa. Bug seperti ini",
                    "yang paling lama ketahuannya.",
                    "",
                    "Ada dua cara menukar kuponnya: 'await' dari dalam async def, atau",
                    "'asyncio.run()' dari kode biasa di luar.",
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
                    "Menulis 'await' tiga kali berturut-turut nggak bikin ketiganya jalan",
                    "bersamaan. await artinya \"berhenti di sini sampai yang ini selesai\".",
                    "Supaya bersamaan, pakai salah satu dari ini:",
                    "  - asyncio.gather(a(), b()): jalankan semua, tunggu semua. Hasilnya",
                    "    berupa daftar yang urutannya sesuai urutan argumen, nggak peduli",
                    "    siapa yang duluan selesai.",
                    "  - asyncio.create_task(a()): jadwalkan sekarang, lalu langsung lanjut",
                    "    ke baris berikutnya. Hasilnya diambil pakai 'await task' kapan pun",
                    "    kamu perlu.",
                    "  - async with asyncio.TaskGroup(): butuh Python 3.11+. Blok with-nya",
                    "    baru selesai sesudah semua task di dalamnya selesai. Kalau satu task",
                    "    melempar exception, sisanya otomatis dibatalkan.",
                    "",
                    "Jebakan: hasil create_task harus disimpan ke variabel. Event loop cuma",
                    "memegang task dengan referensi lemah, artinya pegangan yang nggak",
                    "mencegah objeknya dibuang. Jadi task yang nggak disimpan bisa dibuang",
                    "garbage collector di tengah jalan. Bug ini kadang muncul kadang nggak,",
                    "tergantung waktu, jadi susah dilacak.",
                    "",
                    "Untuk kode baru, TaskGroup pilihan paling aman. gather biasa membiarkan",
                    "task lain terus jalan waktu salah satunya gagal. Dari situ muncul task",
                    "yang masih hidup padahal programnya udah menyerah.",
                    "",
                    "Contoh di bawah mengunduh dua hal yang masing-masing makan 0,3 detik.",
                    "Kalau berurutan butuh 0,6 detik. Tiga cara lainnya cukup 0,3 detik,",
                    "sama dengan waktu mengunduh satu.",
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
                    "time.sleep(1) menahan thread. Di dalam async def, thread itu",
                    "satu-satunya thread yang memutar event loop. Jadi selama satu detik itu,",
                    "nggak ada coroutine lain yang kebagian giliran.",
                    "",
                    "asyncio.sleep(1) kerjanya beda. Dia menitip pesan \"bangunkan aku satu",
                    "detik lagi\", lalu melepas gilirannya. Jadi ini soal jalan atau nggak,",
                    "bukan soal gaya penulisan.",
                    "",
                    "Aturan yang sama berlaku untuk semua panggilan blocking, yaitu",
                    "panggilan yang menahan thread sampai selesai. Selain sleep, contohnya:",
                    "  - requests.get(...)",
                    "  - f.read() atas berkas besar",
                    "  - input()",
                    "  - driver database sinkron",
                    "",
                    "Kalau sebuah library sinkron memang harus dipakai di dalam kode async,",
                    "lempar ke thread lain supaya event loop tetap bisa jalan:",
                    "  hasil = await asyncio.to_thread(fungsi_lambat, argumen)   # Python 3.9+",
                    "",
                    "Contoh di bawah menyerahkan tiga tugas ke gather. Versi yang blocking",
                    "nggak menghemat waktu sedikit pun. Tiga tugas 0,5 detik tetap makan 3x",
                    "waktu satu tugas, persis seperti tanpa async.",
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
                "heading": "async with, async for, dan kapan async tidak perlu",
                "body": [
                    "with dan for punya kembaran async. Bentuk ini yang bakal kamu temui di",
                    "kode nyata:",
                    "",
                    "  async with httpx.AsyncClient() as klien:         # __aenter__ / __aexit__",
                    "      jawaban = await klien.get(alamat)",
                    "      async for potongan in jawaban.aiter_bytes(): # __anext__, boleh menunggu",
                    "          print(len(potongan))",
                    "",
                    "Alasannya sama seperti async def. Membuka dan menutup koneksi juga",
                    "menunggu jaringan, jadi langkah itu pun harus bisa melepas giliran.",
                    "Aturan with dan for dari materi Context Manager dan Perulangan nggak",
                    "berubah sama sekali. Bedanya cuma ada kata 'async' di depannya.",
                    "",
                    "Kalau salah pakai, yaitu 'with' biasa untuk objek async, kamu dapat",
                    "error. Di Python 3.10 ke bawah errornya AttributeError yang menyebut",
                    "__enter__. Mulai Python 3.11 errornya TypeError yang bilang objeknya",
                    "nggak mendukung context manager protocol.",
                    "",
                    "FastAPI adalah framework web yang nanti disebut di materi Roadmap. Di",
                    "sana endpoint-nya ditulis begini:",
                    "",
                    "  @app.get('/produk')",
                    "  async def daftar_produk():",
                    "      return await db.ambil_semua()",
                    "",
                    "Sekarang kamu tahu kenapa hampir seluruh dokumentasinya berbentuk async",
                    "def. Dengan cara itu satu proses sanggup melayani ratusan permintaan",
                    "yang kebetulan lagi sama-sama menunggu database, tanpa satu thread pun",
                    "per permintaan.",
                    "",
                    "Async juga ada saatnya nggak perlu:",
                    "  - Skrip yang mengerjakan satu hal lalu selesai. Nggak ada yang bisa",
                    "    dikerjakan sambil menunggu.",
                    "  - Kerja berat di CPU, misalnya mengolah gambar atau menghitung angka.",
                    "    async nggak menambah satu inti pun. Untuk itu pakai multiprocessing",
                    "    dari materi sebelumnya.",
                    "  - Kode yang semua library-nya sinkron. Membungkusnya pakai async def",
                    "    nggak mempercepat apa pun. Kamu cuma menambah sintaks yang harus",
                    "    dijaga.",
                    "",
                    "Hubungannya dengan GIL: asyncio nggak melawan kunci itu. asyncio",
                    "menghindari kebutuhan akan banyak thread. Satu thread, satu GIL, nol lock.",
                    "Ringkasnya: kalau banyak menunggu I/O, pakai asyncio (atau thread).",
                    "Kalau banyak menghitung, pakai proses.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman dasbor toko sering mengambil beberapa data dari layanan yang",
                    "berbeda: saldo, pesanan baru, dan stok menipis. Framework seperti",
                    "FastAPI menulis endpoint sebagai async def, supaya satu proses bisa",
                    "melayani banyak permintaan yang sama-sama sedang menunggu database atau",
                    "layanan lain.",
                    "",
                    "Kasus kecil: dasbor butuh tiga data, dan tiap pengambilan menunggu",
                    "sekitar 0,5 detik. Kalau diambil berurutan, halaman baru tampil sesudah",
                    "1,5 detik. Pemilik toko ingin halamannya lebih cepat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ketiga pengambilan saling bebas dan isinya cuma menunggu. Itu",
                    "     tanda cocok untuk asyncio.",
                    "  2. Tulis tiap pengambilan sebagai async def ambil(nama) yang memakai",
                    "     await, lalu jalankan ketiganya bersamaan dengan gather():",
                    "      import asyncio",
                    "      async def dasbor():",
                    "          return await asyncio.gather(",
                    "              ambil(\"saldo\"), ambil(\"pesanan\"), ambil(\"stok\"))",
                    "      print(asyncio.run(dasbor()))",
                    "  3. Jalankan. Ketiga hasil datang sesuai urutan argumen, dan totalnya",
                    "     sekitar 0,5 detik.",
                    "  4. Cek kasus pinggir: di dalam ambil(), pakai await asyncio.sleep()",
                    "     atau library async. time.sleep() membekukan event loop, dan",
                    "     totalnya kembali jadi 1,5 detik.",
                    "",
                    "Jebakan: menulis ambil(\"saldo\") tanpa await cuma membuat objek",
                    "coroutine. Isinya nggak pernah dijalankan.",
                ]
            },
        ],
    },
    {
        "title": "42. Virtual Environment, pip & Testing (pytest)",
        "sections": [
            {
                "body": [
                    "Virtual environment, disingkat venv, adalah lingkungan Python yang",
                    "terpisah untuk tiap project. Gunanya supaya library satu project nggak",
                    "bentrok dengan library project lain. Misalnya project A butuh versi",
                    "lama sebuah library, sedangkan project B butuh versi baru. Dengan venv,",
                    "masing-masing punya salinannya sendiri.",
                    "",
                    "Cara bikin dan memakai venv:",
                    "  python3 -m venv venv          # buat folder venv/",
                    "  source venv/bin/activate      # aktifkan (Linux/Mac)",
                    "  venv\\Scripts\\activate         # aktifkan (Windows)",
                    "  pip install nama_library       # install HANYA di venv ini",
                    "  deactivate                     # keluar dari venv",
                    "",
                    "Daftar library yang dipakai sebuah project disebut dependency. Daftar",
                    "itu biasanya dicatat di berkas requirements.txt, supaya project gampang",
                    "disiapkan ulang di komputer lain:",
                    "  pip freeze > requirements.txt",
                    "  pip install -r requirements.txt",
                    "",
                    "Perintah pertama menulis semua library yang terpasang ke berkas itu.",
                    "Perintah kedua memasang semuanya lagi dari berkas itu.",
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
                    "Test yang rapi biasanya mengikuti pola AAA, singkatan dari tiga langkah",
                    "di bawah. Pola ini sama di bahasa lain:",
                    "  1. Arrange -> siapkan data yang dibutuhkan.",
                    "  2. Act     -> panggil fungsi yang diuji.",
                    "  3. Assert  -> pastikan hasilnya sesuai harapan.",
                    "",
                    "assert sendiri adalah perintah dasar Python, jadi bisa dipakai juga di",
                    "luar pytest. Kalau kondisinya False, program berhenti dengan",
                    "AssertionError dan pesannya ditampilkan:",
                    "  assert kondisi, \"pesan jika gagal\"",
                    "  assert 1 + 1 == 2, \"Matematika rusak!\"",
                    "",
                    "Alat-alat yang biasa dipakai programmer Python di tempat kerja:",
                    "  pip / venv    -> manajemen dependency & isolasi environment",
                    "  pytest        -> testing (alternatif: unittest bawaan Python)",
                    "  black / ruff  -> formatter & linter otomatis (kerapian kode)",
                    "  mypy          -> pengecekan type hint secara statis",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di tempat kerja, tiap proyek Python punya venv sendiri dan daftar",
                    "library di requirements.txt, supaya laptop semua anggota tim memasang",
                    "versi yang sama. Tes otomatis dijalankan sebelum perubahan digabung,",
                    "jadi rumus yang rusak ketahuan sebelum sampai ke pelanggan.",
                    "",
                    "Kasus kecil: fungsi hitung_ongkir(berat_kg) di toko online memakai",
                    "aturan Rp 9.000 per kg dengan berat minimal 1 kg. Rekanmu mau mengubah",
                    "tarifnya, dan kamu ingin aturan minimal 1 kg tetap terjaga.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis dulu hasil yang diharapkan: berat 0,5 kg tetap dihitung 9000,",
                    "     dan 3 kg jadi 27000.",
                    "  2. Siapkan venv, lalu pasang pytest di dalamnya: python3 -m venv venv,",
                    "     source venv/bin/activate, pip install pytest.",
                    "  3. Tulis tesnya di berkas test_ongkir.py:",
                    "      from ongkir import hitung_ongkir",
                    "      def test_minimal_satu_kg():",
                    "          assert hitung_ongkir(0.5) == 9000",
                    "      def test_tiga_kg():",
                    "          assert hitung_ongkir(3) == 27000",
                    "     Jalankan pytest. Kalau rumusnya rusak, tes yang gagal menyebut",
                    "     namanya sendiri.",
                    "  4. Cek kasus pinggir: berat negatif. Tambahkan tes dengan with",
                    "     pytest.raises(ValueError), supaya fungsi wajib menolaknya.",
                    "",
                    "Ingat: catat pytest di requirements.txt lewat pip freeze, supaya",
                    "anggota tim lain memasang versi yang sama.",
                ]
            },
        ],
    },
    {
        "title": "43. Testing Lebih Dalam: fixture, parametrize & unittest",
        "sections": [
            {
                "body": [
                    "Materi Virtual Environment, pip & Testing menunjukkan bentuk test yang",
                    "paling dasar: satu fungsi, satu assert. Kode nyata nggak berhenti di",
                    "situ. Coba buka berkas test di project mana pun. Hal pertama yang bikin",
                    "bingung hampir selalu sama: fungsi test-nya punya parameter, padahal",
                    "nggak ada satu baris pun yang memanggil fungsi itu dan mengoper",
                    "argumennya.",
                    "",
                    "  def test_pakai_mengurangi_saldo(dompet):  # 'dompet' dari mana?",
                    "      dompet.pakai(30)",
                    "",
                    "Yang mengisinya pytest. Sebelum menjalankan sebuah fungsi test, pytest",
                    "membaca nama tiap parameternya. Lalu pytest mencari fungsi lain yang",
                    "bertanda @pytest.fixture dengan nama yang sama persis. Nilai kembalian",
                    "fungsi itu yang dioper masuk. Fungsi seperti itu disebut fixture. Yang",
                    "menyambungkan test dan fixture cuma namanya. Urutan dan import nggak",
                    "berpengaruh.",
                    "",
                    "Makanya salah ketik nama parameter nggak memunculkan NameError. Yang",
                    "muncul pesan ini:",
                    "",
                    "  E    fixture 'dompett' not found",
                    "  >    available fixtures: capsys, monkeypatch, tmp_path, dompet, ...",
                    "",
                    "Test-nya juga dihitung sebagai ERROR, bukan FAILED, karena test-nya",
                    "bahkan belum sempat jalan. Begitu kamu lihat kalimat itu, yang salah",
                    "hampir selalu ejaan nama parameternya.",
                    "",
                    "Kenapa repot bikin fixture? Kenapa nggak langsung nulis d = Dompet(100)",
                    "di setiap test? Gunanya supaya tiap test mulai dari keadaan bersih yang",
                    "sama. Secara bawaan, fixture dipanggil ulang untuk setiap fungsi test.",
                    "Jadi test kedua nggak kebagian sisa-sisa test pertama, dan test boleh",
                    "dijalankan dalam urutan apa pun.",
                    "",
                    "scope menentukan seberapa sering sebuah fixture dipanggil ulang:",
                    "",
                    "  scope=\"function\"   (bawaan) dipanggil lagi untuk SETIAP fungsi test",
                    "  scope=\"class\"      sekali untuk satu class test",
                    "  scope=\"module\"     sekali untuk satu berkas test",
                    "  scope=\"session\"    sekali untuk seluruh jalannya pytest",
                    "",
                    "Jebakan: kalau scope dinaikkan ke \"module\" atau \"session\" supaya lebih",
                    "hemat, satu objek yang sama dipakai bareng-bareng. Kalau objek itu",
                    "mutable, artinya isinya bisa diubah, test pertama yang mengubahnya",
                    "bakal mewariskan perubahan itu ke test sesudahnya tanpa ketahuan:",
                    "",
                    "  @pytest.fixture(scope=\"module\")",
                    "  def keranjang():",
                    "      return []",
                    "  # test_satu menambah 1 item, assert len == 1  -> lulus",
                    "  # test_dua  menambah 1 item, assert len == 1  -> GAGAL, isinya 2",
                    "",
                    "Gejala yang paling membingungkan: test lulus kalau dijalankan sendirian,",
                    "tapi gagal kalau dijalankan bareng yang lain. Pakai scope besar cuma",
                    "untuk yang mahal dan nggak diubah, misalnya koneksi database, server",
                    "uji, atau berkas contoh yang cuma dibaca.",
                    "",
                    "Fixture juga bisa membereskan sesudah test lewat yield. Fixture yang",
                    "pakai yield sebagai ganti return menyerahkan nilainya di baris yield.",
                    "Sesudah test selesai, sisa barisnya dilanjutkan, entah test-nya lulus",
                    "atau gagal. Polanya persis generator di materi Iterator & Generator dan",
                    "@contextmanager di materi Decorator & Context Manager. Yang di atas",
                    "yield itu persiapan, yang di bawahnya pembersihan.",
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
                    "@pytest.mark.parametrize menjalankan satu fungsi test berkali-kali",
                    "dengan data yang beda-beda. Tanpa itu, orang nulis lima test yang",
                    "isinya sama persis kecuali angkanya. Begitu rumusnya berubah, kelimanya",
                    "harus diubah satu per satu.",
                    "",
                    "Jumlah nama di string parameter wajib sama dengan panjang tiap tuple di",
                    "daftarnya. Kalau meleset, pytest menolak mengumpulkan test itu sebelum",
                    "satu pun dijalankan. Kalau parameternya cuma satu, daftarnya cukup list",
                    "biasa tanpa tuple: [0, 5, 10].",
                    "",
                    "Hasilnya empat test terpisah yang punya nama sendiri-sendiri, misalnya",
                    "test_hitung_pajak[6000000-50000]. Satu kasus gagal nggak menghentikan",
                    "yang lain, dan laporannya menyebut kasus mana yang gagal. Ini lebih",
                    "enak daripada menumpuk empat assert di dalam satu fungsi test, yang",
                    "langsung berhenti di assert pertama yang gagal.",
                    "",
                    "pytest juga punya fixture bawaan. Kamu nggak perlu menulisnya, tinggal",
                    "minta lewat nama parameter:",
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
                    "Untuk menandai test yang belum siap:",
                    "",
                    "  @pytest.mark.skip(reason=\"...\")         selalu dilewati",
                    "  @pytest.mark.skipif(kondisi, reason=)   dilewati kalau kondisi True",
                    "  @pytest.mark.xfail(reason=\"...\")        diharapkan gagal (bug lama)",
                    "",
                    "Jebakan: kalau test bertanda xfail ternyata lulus, statusnya XPASS, dan",
                    "itu nggak dihitung sebagai kegagalan. Akibatnya bug yang udah lama",
                    "diperbaiki bisa terus tercatat sebagai xfail tanpa ada yang sadar.",
                    "Pakai xfail(strict=True) supaya XPASS dinyatakan FAILED. Dengan begitu",
                    "tandanya wajib dibersihkan.",
                    "",
                    "Satu lagi: jangan pernah menghapus reason=. Test yang dimatikan tanpa",
                    "alasan tertulis nggak bakal dinyalakan lagi oleh siapa pun, karena",
                    "nggak ada yang tahu kenapa test itu dimatikan.",
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
                    "unittest adalah framework testing bawaan Python, jadi nggak perlu pip",
                    "install apa pun. pytest bukan bawaan. Seperti di materi Virtual",
                    "Environment, pip & Testing, pytest dipasang di dalam venv pakai pip",
                    "install pytest. Bentuk keduanya beda jauh, dan kamu perlu bisa membaca",
                    "dua-duanya:",
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
                    "Di unittest, pemeriksaan dilakukan lewat method milik TestCase, dan",
                    "keyword assert nggak dipakai. Ini yang paling sering dipakai (semuanya",
                    "diawali self.):",
                    "",
                    "  assertEqual(a, b)         assertNotEqual(a, b)",
                    "  assertTrue(x)             assertFalse(x)",
                    "  assertIn(a, wadah)        assertNotIn(a, wadah)",
                    "  assertIsNone(x)           assertIsInstance(x, tipe)",
                    "  assertAlmostEqual(a, b)   untuk float: 0.1 + 0.2 bukan persis 0.3",
                    "  assertRaises(Error)       dipakai sebagai 'with', lihat di bawah",
                    "",
                    "Kenapa nggak assert biasa aja? Ada dua alasan. Pertama, assertEqual",
                    "mencetak kedua nilainya waktu gagal ('150000 != 140000'), sedangkan",
                    "assert a == b polos cuma bilang AssertionError tanpa angka apa pun.",
                    "Kedua, assert dimatikan total kalau Python dijalankan dengan flag -O,",
                    "sedangkan assertEqual tetap bekerja.",
                    "",
                    "pytest menambal kekurangan pertama dengan menulis ulang bytecode berkas",
                    "test-nya, jadi di pytest assert polos tetap menampilkan nilai kedua",
                    "sisinya. Di luar berkas test, trik itu nggak berlaku.",
                ],
                "code": "import unittest\n\n\ndef normalkan(nama):\n    \"\"\"'  budi   santoso ' -> 'Budi Santoso'.\"\"\"\n    return \" \".join(nama.split()).title()\n\n\nclass TestNormalkan(unittest.TestCase):\n\n    def setUp(self):\n        # Dijalankan ULANG sebelum SETIAP method test_ di bawah.\n        self.kotor = \"  budi   santoso \"\n\n    def tearDown(self):\n        # Setelah tiap test, lulus maupun gagal (mirip baris setelah yield).\n        self.kotor = None\n\n    def test_spasi_berlebih_dirapikan(self):\n        self.assertEqual(normalkan(self.kotor), \"Budi Santoso\")\n\n    def test_kapital_dirapikan(self):\n        self.assertEqual(normalkan(\"SITI aminah\"), \"Siti Aminah\")\n\n    def test_nama_kosong_tetap_kosong(self):\n        self.assertEqual(normalkan(\"   \"), \"\")\n\n    def test_nama_depan_ada_di_hasil(self):\n        self.assertIn(\"Budi\", normalkan(self.kotor))\n\n    def test_angka_bukan_string_melempar_error(self):\n        with self.assertRaises(AttributeError):\n            normalkan(123)\n\n    def cek_ini_tidak_pernah_jalan(self):\n        # Tidak berawalan test_, jadi unittest TIDAK PERNAH memanggilnya.\n        # Buktinya: laporannya berbunyi \"Ran 5 tests\", bukan 6.\n        self.assertEqual(1, 2)\n\n\nif __name__ == \"__main__\":\n    unittest.main(verbosity=2)",
            },
            {
                "heading": "Menjalankan unittest dan tiga jebakannya",
                "body": [
                    "Contoh di atas program utuh. Simpan, lalu jalankan seperti skrip biasa.",
                    "",
                    "Yang sering bikin panik pertama kali: laporan unittest dicetak ke",
                    "stderr, bukan stdout. Jadi kalau tombol Jalankan di aplikasi ini",
                    "menaruh laporannya di kotak pesan error padahal semua lulus, itu bukan",
                    "kegagalan. Lihat baris terakhirnya, 'OK', dan tanda kode keluar 0.",
                    "Kalau ada test yang gagal, barisnya berbunyi 'FAILED (failures=1)' dan",
                    "kode keluarnya bukan 0. Angka itu yang dibaca server CI, yaitu server",
                    "yang otomatis menjalankan test tiap ada perubahan, untuk memutuskan",
                    "sebuah commit boleh masuk atau nggak.",
                    "",
                    "Untuk menjalankan seluruh folder test tanpa if __name__ di tiap berkas:",
                    "",
                    "  python3 -m unittest discover -s tests -t .",
                    "      # -s: folder berisi test, -t: folder akar proyek",
                    "  python3 -m unittest tests.test_nama          # satu berkas saja",
                    "  python3 -m unittest tests.test_nama.TestNormalkan.test_kapital_dirapikan",
                    "",
                    "Perintah pertama itu persis yang dipakai aplikasi yang lagi kamu baca",
                    "ini untuk menjalankan ratusan test-nya sendiri.",
                    "",
                    "Tiga jebakan unittest yang paling sering makan waktu:",
                    "",
                    "  1. Method yang nggak berawalan test_ nggak pernah dijalankan, tanpa",
                    "     peringatan apa pun. Salah ketik 'tes_saldo' aja udah cukup bikin",
                    "     sebuah test hilang, sementara laporannya tetap hijau. Biasakan",
                    "     membaca angka 'Ran N tests'. Kalau N mengecil padahal kamu",
                    "     menambah test, di situ masalahnya.",
                    "  2. discover cuma mengambil berkas yang cocok dengan pola test*.py",
                    "     (bisa diubah pakai -p). Kalau pakai -t . folder tests/ wajib punya",
                    "     berkas __init__.py. Tanpa berkas itu muncul 'ImportError: Start",
                    "     directory is not importable'. Yang kamu dapat error yang bikin",
                    "     gagal total sebelum satu test pun sempat dimuat. Ini lebih parah",
                    "     daripada laporan \"nol test\".",
                    "  3. assertRaises harus menerima fungsinya, bukan hasil pemanggilannya:",
                    "       self.assertRaises(ValueError, bagi(1, 0))   # SALAH",
                    "       # bagi(1,0) dijalankan duluan, error-nya meledak sebelum",
                    "       # assertRaises sempat memasang jaringnya",
                    "       self.assertRaises(ValueError, bagi, 1, 0)   # benar",
                    "       with self.assertRaises(ValueError):         # paling terbaca",
                    "           bagi(1, 0)",
                    "",
                    "Ada satu lagi yang sering disangka bug. Setiap method test dijalankan",
                    "pada instance baru dari class-nya. Jadi self.kotor yang dipasang di",
                    "satu test nggak bakal ada di test berikutnya. Ini memang disengaja,",
                    "karena test nggak boleh saling bergantung. Kalau mau berbagi",
                    "persiapan, pakai setUp(), yang memang dijalankan ulang sebelum tiap",
                    "test.",
                    "",
                    "Kenapa harus kuasai dua-duanya? Pustaka standar Python, banyak project",
                    "lama, dan aplikasi yang lagi kamu pakai ini semuanya pakai unittest.",
                    "Kalau kamu cuma kenal pytest, folder tests/ mereka nggak bakal kebaca.",
                    "Kabar baiknya, satu arah gratis: pytest bisa menjalankan class TestCase",
                    "apa adanya, jadi sebuah project boleh pindah pelan-pelan. Arah",
                    "sebaliknya nggak bisa. unittest nggak ngerti fixture maupun",
                    "parametrize, dan method TestCase yang dikasih parameter tambahan",
                    "langsung error.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aturan bisnis yang punya tingkatan, seperti pajak, diskon bertingkat,",
                    "atau ongkir per zona, paling sering salah di angka batasnya. Tim yang",
                    "merawat aturan seperti itu menguji tiap batas dengan parametrize, satu",
                    "fungsi tes untuk banyak kasus. Fixture menyiapkan data bersih untuk",
                    "tiap tes.",
                    "",
                    "Kasus kecil: toko memberi diskon 0% untuk belanja di bawah 100.000, 5%",
                    "untuk 100.000 sampai 499.999, dan 10% mulai 500.000. Fungsi",
                    "hitung_diskon(belanja) mengembalikan potongan dalam rupiah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar kasus pinggirnya: tepat di batas, dan satu rupiah di",
                    "     bawahnya. Untuk dua batas, itu empat angka.",
                    "  2. Tulis keempatnya sebagai satu tes berparameter:",
                    "      import pytest",
                    "      @pytest.mark.parametrize(\"belanja, diskon\", [",
                    "          (99999, 0), (100000, 5000), (499999, 24999), (500000, 50000),",
                    "      ])",
                    "      def test_diskon(belanja, diskon):",
                    "          assert hitung_diskon(belanja) == diskon",
                    "  3. Jalankan pytest -v. Hasilnya empat tes terpisah. Kalau satu batas",
                    "     salah, laporannya menyebut angka yang gagal, misalnya",
                    "     test_diskon[500000-50000].",
                    "  4. Cek kasus pinggir milik tesnya sendiri: jumlah nama di string",
                    "     \"belanja, diskon\" harus sama dengan isi tiap tuple. Kalau beda,",
                    "     pytest menolak mengumpulkan tes itu.",
                    "",
                    "Jebakan: 499999 dikali 5% hasilnya 24999,95. Tentukan dulu aturan",
                    "pembulatannya, lalu tulis angka harapannya sesuai aturan itu.",
                ]
            },
        ],
    },
    {
        "title": "44. Roadmap Menjadi Python Developer Handal",
        "sections": [
            {
                "body": [
                    "Sampai sini kamu udah punya fondasi Python yang kuat: sintaks, OOP,",
                    "exception, file I/O, decorator, sampai testing. Di bawah ini roadmap,",
                    "yaitu peta langkah, yang realistis untuk melangkah lebih jauh.",
                    "",
                    "Tahap 1: kuatkan fondasi (kamu di sini)",
                    "  - Bisa membaca dan menulis semua konsep di atas dengan lancar.",
                    "  - Latihan: kerjakan soal di HackerRank/LeetCode kategori Python.",
                    "",
                    "Tahap 2: pilih jalur spesialisasi",
                    "",
                    "Web Development:",
                    "  - Flask (ringan, fleksibel) atau Django (lengkap, 'batteries",
                    "    included', artinya hampir semua yang dibutuhkan udah ikut) untuk",
                    "    backend web dan REST API.",
                    "  - FastAPI, yang populer untuk API modern: cepat, dan dokumentasinya",
                    "    dibuat otomatis. FastAPI dibangun di atas async/await, jadi",
                    "    bekalnya ada di materi Asinkron: async, await & asyncio.",
                    "",
                    "Data Science / AI:",
                    "  - NumPy & Pandas untuk mengolah data angka dan tabel.",
                    "  - Matplotlib/Seaborn untuk visualisasi data.",
                    "  - scikit-learn untuk machine learning klasik.",
                    "  - PyTorch/TensorFlow untuk deep learning.",
                    "",
                    "Automation/DevOps:",
                    "  - Script otomasi untuk file, email, dan web scraping (mengambil data",
                    "    dari halaman web) pakai requests/BeautifulSoup/Selenium.",
                    "  - Ansible (berbasis Python) untuk otomasi infrastruktur, yaitu",
                    "    server dan jaringan.",
                ]
            },
            {
                "heading": "Proyek nyata dan kebiasaan profesional",
                "body": [
                    "Tahap 3: bangun project nyata",
                    "",
                    "Ini tahap yang paling penting. Yang kamu baca baru nempel kalau kamu",
                    "pakai untuk bikin sesuatu sendiri:",
                    "  1. CLI tool sederhana, misalnya to-do list atau expense tracker",
                    "     (pencatat pengeluaran). argparse dan sys.argv-nya ada di materi",
                    "     Program Baris Perintah: sys, os & argparse.",
                    "  2. REST API dengan FastAPI/Flask plus database (SQLite/PostgreSQL).",
                    "  3. Web scraper yang mengambil dan mengolah data nyata.",
                    "  4. Project analisis data dari dataset publik (Kaggle, dsb).",
                    "  5. Semua project di atas wajib disertai unit test (pytest).",
                    "",
                    "Tahap 4: kebiasaan profesional",
                    "  1. Ikuti PEP 8 (panduan gaya kode resmi Python) secara konsisten.",
                    "  2. Pakai type hint untuk project yang lebih besar dari skrip kecil.",
                    "  3. Pakai Git untuk semua project, dan biasakan commit yang rapi.",
                    "  4. Baca kode open source Python yang populer di GitHub (requests,",
                    "     flask, dsb) untuk belajar gaya kode yang baik. Bekal membacanya",
                    "     udah kamu punya: materi Struktur Project Python untuk memahami",
                    "     tata letak berkas dan paketnya, dan materi Anotasi Tipe untuk",
                    "     signature bertanda -> yang banyak muncul di dalamnya.",
                    "  5. Pahami beda Python 2 dan 3 secukupnya. Python 2 sudah EOL (end of",
                    "     life), artinya nggak dirawat lagi, tapi kadang masih ketemu di",
                    "     kode lama atau legacy system.",
                ]
            },
            {
                "heading": "Kebiasaan harian dan Zen of Python",
                "body": [
                    "Kebiasaan harian supaya makin jago:",
                    "  1. Ketik ulang semua contoh di aplikasi ini. Jangan copy-paste.",
                    "  2. Coba pecahkan satu masalah dengan lebih dari satu cara, misalnya",
                    "     for-loop dan list comprehension, supaya kamu paham trade-off-nya,",
                    "     yaitu untung-rugi tiap cara.",
                    "  3. Pakai Python REPL (mode interaktif yang muncul kalau kamu ketik",
                    "     python3 di terminal) atau Jupyter Notebook untuk eksperimen",
                    "     cepat.",
                    "  4. Baca pesan error Python dengan teliti. Traceback biasanya menunjuk",
                    "     persis baris dan jenis error yang terjadi. Cara membacanya baris",
                    "     per baris ada di materi Membaca Traceback & Menangkap Error Secara",
                    "     Luas. Balik ke sana tiap kali sebuah error terasa buntu.",
                    "  5. Kuasai SQL (lihat menu SQL di aplikasi ini) untuk melengkapi",
                    "     kemampuanmu sebagai backend atau data developer.",
                    "",
                    "Python terkenal dengan filosofi 'The Zen of Python'. Ketik",
                    "'import this' di Python untuk membacanya. Beberapa prinsip yang paling",
                    "sering dikutip:",
                    "  'Simple is better than complex.'",
                    "  'Readability counts.'",
                    "  'There should be one-- and preferably only one --obvious way to do it.'",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Waktu melamar magang atau kerja sebagai programmer Python pemula, repo",
                    "berisi proyek kecil yang jalan, punya tes, dan punya README adalah",
                    "bukti yang bisa langsung dibuka pewawancara. Proyek seperti itu juga",
                    "bahan yang bagus untuk laporan PKL, karena bisa didemokan di depan",
                    "pembimbing.",
                    "",
                    "Kasus kecil: kamu ingin satu proyek portofolio pertama, yaitu pencatat",
                    "pengeluaran harian di terminal. Bingungnya, harus mulai dari mana.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah jadi fitur sekecil mungkin: tambah catatan, lihat total hari",
                    "     ini, dan simpan ke berkas supaya data nggak hilang.",
                    "  2. Petakan tiap fitur ke materi yang sudah kamu baca: argparse untuk",
                    "     perintah, json untuk menyimpan, datetime untuk tanggal, dan pytest",
                    "     untuk tes.",
                    "  3. Tentukan bentuk datanya sebelum menulis kode:",
                    "      catatan = [{\"tanggal\": \"2024-03-01\", \"jumlah\": 15000,",
                    "                  \"keterangan\": \"makan siang\"}]",
                    "     Tanggal disimpan dalam format ISO, dan uang sebagai int rupiah.",
                    "  4. Cek kasus pinggir sejak awal: berkas data yang belum ada di hari",
                    "     pertama, dan jumlah yang diketik dengan huruf. Tulis tes untuk",
                    "     keduanya.",
                    "",
                    "Ingat: versi pertama cukup bisa menambah dan menjumlah. Fitur lain",
                    "ditambahkan sesudah versi itu jalan dan punya tes.",
                ]
            },
        ],
    },
]
