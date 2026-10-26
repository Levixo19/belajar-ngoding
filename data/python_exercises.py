PYTHON_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Python.",
            "",
            "Tulis PERSIS seperti di atas, termasuk nama Andi -- penilaian",
            "membandingkan outputmu huruf demi huruf.",
            "",
            "Keluaran yang diharapkan:",
            "    Halo, namaku Andi!",
            "    Aku sedang belajar Python.",
        ],
        "hints": [
            "Baca ulang materi \"Pengenalan Python & Instalasi\". Satu baris teks di layar berarti satu kali memanggil fungsi untuk mencetak.",
            "Panggil print() dua kali, satu untuk tiap baris. Teksnya diapit tanda kutip ' atau \", dan Python nggak butuh titik koma di akhir baris.",
            "Salin teksnya persis, termasuk nama Andi, koma, tanda seru, dan titiknya. Penilaian membandingkan keluaranmu huruf demi huruf.",
        ],
        "solution": """print("Halo, namaku Andi!")
print("Aku sedang belajar Python.")""",
    },
    {
        "title": "Latihan 2: Kalkulator Sederhana",
        "difficulty": "Mudah",
        "question": [
            "Buat program dengan 2 variabel (misal 15 dan 4).",
            "Tampilkan hasil: penjumlahan, pengurangan, perkalian,",
            "pembagian biasa, pembagian bulat (//), dan sisa bagi (%).",
            "",
            "Keluaran yang diharapkan:",
            "    15 + 4 = 19",
            "    15 - 4 = 11",
            "    15 * 4 = 60",
            "    15 / 4 = 3.75",
            "    15 // 4 = 3",
            "    15 % 4 = 3",
        ],
        "hints": [
            "Keenam operator yang diminta dibahas di materi \"Operator\", termasuk beda / dan //.",
            "Simpan dua angkanya di variabel (misalnya a dan b), lalu cetak tiap hasil dengan f-string supaya angka dan hasilnya bisa ditulis dalam satu teks. Ingat, / selalu menghasilkan float, sedangkan // menghasilkan bilangan bulat.",
            "Contoh satu baris: print(f\"{a} // {b} = {a // b}\"). Lima baris lainnya polanya sama.",
        ],
        "solution": """a = 15
b = 4

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")""",
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Buat program: baca satu angka nilai dari input, jika nilai >= 75",
            "tampilkan 'Lulus', selain itu tampilkan 'Tidak Lulus'.",
            "",
            "Jangan cetak teks prompt apa pun. Program hanya boleh mengeluarkan",
            "satu baris berisi Lulus atau Tidak Lulus.",
            "",
            "Untuk input 80, keluarannya:",
            "    Lulus",
        ],
        "hints": [
            "Ini soal percabangan. Baca ulang \"Percabangan (if / elif / else)\" dan bagian input() di \"Masukan, Keluaran & Modul Bawaan\".",
            "input() selalu mengembalikan string, jadi ubah dulu ke int sebelum dibandingkan dengan 75. Panggil input() tanpa argumen: teks prompt di dalamnya ikut tercetak dan membuat keluaranmu dianggap salah.",
            "Kerangkanya: nilai = int(input()), lalu if nilai >= 75: cetak Lulus, else: cetak Tidak Lulus. Ternary satu baris juga boleh.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["80\n", "60\n"],
        "solution": """nilai = int(input())

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")

# Versi ternary:
# status = "Lulus" if nilai >= 75 else "Tidak Lulus"
# print(status)""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap",
        "difficulty": "Menengah",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20",
            "beserta total jumlahnya.",
            "Contoh output: 2 4 6 8 10 12 14 16 18 20, Total: 110",
            "",
            "Keluaran yang diharapkan:",
            "    2 4 6 8 10 12 14 16 18 20",
            "    Total: 110",
        ],
        "hints": [
            "Kamu butuh perulangan, cek genap dengan operator %, dan penjumlahan. Lihat \"Perulangan (for & while)\" dan \"Fungsi Bawaan untuk Koleksi\".",
            "Ulangi range(1, 21), kumpulkan angka yang n % 2 == 0 ke sebuah list, lalu cetak isinya dipisah spasi. Di baris kedua cetak Total: diikuti sum() dari list itu.",
            "print(*genap) mencetak isi list dipisah spasi, tanpa kurung siku dan koma.",
        ],
        "solution": """genap = [n for n in range(1, 21) if n % 2 == 0]

print(*genap)   # unpacking list jadi argumen print terpisah spasi
print(f"Total: {sum(genap)}")""",
    },
    {
        "title": "Latihan 5: Pola Bintang",
        "difficulty": "Menengah",
        "question": [
            "Buat pola segitiga siku-siku dari bintang:",
            "  *",
            "  **",
            "  ***",
            "  ****",
            "  *****",
            "",
            "Keluaran yang diharapkan:",
            "    *",
            "    **",
            "    ***",
            "    ****",
            "    *****",
        ],
        "hints": [
            "Baris ke-i berisi i bintang. Baca ulang \"Perulangan (for & while)\", lalu bagian operator * untuk string di \"String & Formatting\".",
            "Ulangi i dari 1 sampai 5 dengan range(1, 6). Di tiap putaran cetak bintang sebanyak i, bisa dengan loop di dalam loop atau tanpa loop dalam sama sekali.",
            "String bisa dikalikan dengan angka: \"*\" * 3 menghasilkan '***'.",
        ],
        "solution": """for i in range(1, 6):
    print("*" * i)

# Cara alternatif dengan nested loop:
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()""",
    },
    {
        "title": "Latihan 6: Statistik Nilai dengan List",
        "difficulty": "Menengah",
        "question": [
            "Diberikan list nilai = [80, 90, 75, 85, 60, 95, 70].",
            "Tampilkan: nilai terbesar, terkecil, rata-rata, dan",
            "list nilai yang sudah diurutkan dari terbesar ke terkecil.",
            "",
            "Keluaran yang diharapkan:",
            "    Terbesar: 95",
            "    Terkecil: 60",
            "    Rata-rata: 79.29",
            "    Urutan menurun: [95, 90, 85, 80, 75, 70, 60]",
        ],
        "hints": [
            "Semua yang diminta sudah tersedia sebagai fungsi bawaan. Lihat \"Fungsi Bawaan untuk Koleksi\" dan \"List & Tuple\".",
            "max() dan min() untuk terbesar dan terkecil, sum() dibagi len() untuk rata-rata, dan sorted() dengan reverse=True untuk urutan dari terbesar ke terkecil.",
            "Rata-rata dengan dua angka di belakang koma ditulis lewat f-string seperti f\"{rata:.2f}\".",
        ],
        "solution": """nilai = [80, 90, 75, 85, 60, 95, 70]

print(f"Terbesar: {max(nilai)}")
print(f"Terkecil: {min(nilai)}")
print(f"Rata-rata: {sum(nilai) / len(nilai):.2f}")
print(f"Urutan menurun: {sorted(nilai, reverse=True)}")""",
    },
    {
        "title": "Latihan 7: Fungsi Hitung Luas",
        "difficulty": "Menengah",
        "question": [
            "Buat 3 fungsi:",
            "  1. luas_persegi(sisi)          -> sisi * sisi",
            "  2. luas_persegi_panjang(p, l)  -> p * l",
            "  3. luas_lingkaran(r)           -> pi * r * r (pakai module math)",
            "Panggil ketiganya dan tampilkan hasilnya.",
            "",
            "Keluaran yang diharapkan:",
            "    Persegi (5): 25",
            "    Persegi Panjang (4x6): 24",
            "    Lingkaran (r=7): 153.94",
        ],
        "hints": [
            "Baca ulang \"Function (Fungsi)\" untuk def dan return, dan bagian module math di \"Masukan, Keluaran & Modul Bawaan\".",
            "Tulis tiga fungsi yang masing-masing mengembalikan hasil hitungannya dengan return, bukan mencetaknya. Untuk pi, tulis import math di atas berkas lalu pakai math.pi. Pencetakan dilakukan di luar fungsi.",
            "Kerangka satu fungsi: def luas_persegi(sisi): lalu di baris berikutnya return sisi * sisi. Luas lingkaran enak dicetak dengan format :.2f.",
        ],
        "solution": """import math

def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(p, l):
    return p * l

def luas_lingkaran(r):
    return math.pi * r * r

print(f"Persegi (5): {luas_persegi(5)}")
print(f"Persegi Panjang (4x6): {luas_persegi_panjang(4, 6)}")
print(f"Lingkaran (r=7): {luas_lingkaran(7):.2f}")""",
    },
    {
        "title": "Latihan 8: Manipulasi String",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat = '  Belajar Python itu Menyenangkan  '.",
            "Tampilkan:",
            "  1. Kalimat tanpa spasi di ujung.",
            "  2. Kalimat dalam huruf besar semua.",
            "  3. Jumlah kata dalam kalimat.",
            "  4. Kalimat dengan kata 'Python' diganti 'Coding'.",
            "",
            "Keluaran yang diharapkan:",
            "    1. 'Belajar Python itu Menyenangkan'",
            "    2. BELAJAR PYTHON ITU MENYENANGKAN",
            "    3. Jumlah kata: 4",
            "    4. Belajar Coding itu Menyenangkan",
        ],
        "hints": [
            "Semua langkah dikerjakan dengan method string. Baca ulang \"String & Formatting\".",
            "strip() membuang spasi di kedua ujung, upper() mengubah ke huruf besar, split() memecah kalimat jadi list kata (hitung dengan len()), dan replace(lama, baru) mengganti kata.",
            "Jalankan strip() sekali dan simpan hasilnya di variabel, lalu pakai variabel itu untuk tiga langkah sisanya.",
        ],
        "solution": """kalimat = "  Belajar Python itu Menyenangkan  "

bersih = kalimat.strip()
print(f"1. '{bersih}'")
print(f"2. {bersih.upper()}")
print(f"3. Jumlah kata: {len(bersih.split())}")
print(f"4. {bersih.replace('Python', 'Coding')}")""",
    },
    {
        "title": "Latihan 9: Dictionary Buku Kontak",
        "difficulty": "Menengah",
        "question": [
            "Buat dictionary kontak kosong. Tambahkan 3 kontak",
            "(nama sebagai key, nomor telepon sebagai value).",
            "Tampilkan semua kontak dengan format 'nama: nomor'.",
            "Lalu cari satu kontak yang mungkin tidak ada dengan aman",
            "(tanpa error) menggunakan .get().",
            "",
            "Keluaran yang diharapkan:",
            "    Andi: 0812-1111-1111",
            "    Budi: 0813-2222-2222",
            "    Citra: 0812-3333-3333",
            "    Kontak tidak ditemukan",
        ],
        "hints": [
            "Baca ulang \"Dictionary & Set\": cara menambah pasangan key-value, mengulang isinya, dan mengambil nilai tanpa KeyError.",
            "Mulai dari dict kosong {}, tambahkan tiga kontak dengan kontak[nama] = nomor, ulangi semuanya dengan for nama, nomor in kontak.items(), lalu cari nama yang nggak ada memakai .get().",
            "kontak.get(\"Zaki\", \"Kontak tidak ditemukan\") mengembalikan argumen keduanya kalau key itu nggak ada, tanpa melempar error.",
        ],
        "solution": """kontak = {}
kontak["Andi"] = "0812-1111-1111"
kontak["Budi"] = "0813-2222-2222"
kontak["Citra"] = "0812-3333-3333"

for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")

hasil = kontak.get("Zaki", "Kontak tidak ditemukan")
print(hasil)""",
    },
    {
        "title": "Latihan 10: Filter & Transform dengan Comprehension",
        "difficulty": "Lanjut",
        "question": [
            "Diberikan list angka = list(range(1, 21)).",
            "Menggunakan SATU list comprehension untuk masing-masing:",
            "  1. Ambil semua kelipatan 3.",
            "  2. Buat list berisi kuadrat dari bilangan ganjil saja.",
            "  3. Buat dictionary {angka: 'genap'/'ganjil'} untuk 1-10.",
            "",
            "Keluaran yang diharapkan:",
            "    [3, 6, 9, 12, 15, 18]",
            "    [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]",
            "    {1: 'ganjil', 2: 'genap', 3: 'ganjil', 4: 'genap', 5: 'ganjil', 6: 'genap', 7: 'ganjil', 8: 'genap', 9: 'ganjil', 10: 'genap'}",
        ],
        "hints": [
            "Baca ulang \"List Comprehension & Generator Expression\", termasuk bagian dict comprehension dan ekspresi if-else di dalamnya.",
            "Bentuk umumnya [ekspresi for x in angka if syarat]. Kelipatan 3 berarti x % 3 == 0, ganjil berarti x % 2 != 0. Untuk dict, pakai kurung kurawal dengan pasangan kunci: nilai.",
            "Nilai dict-nya berupa ternary, (\"genap\" if x % 2 == 0 else \"ganjil\"), dengan x diambil dari range(1, 11).",
        ],
        "solution": """angka = list(range(1, 21))

kelipatan_3 = [x for x in angka if x % 3 == 0]
print(kelipatan_3)

kuadrat_ganjil = [x**2 for x in angka if x % 2 != 0]
print(kuadrat_ganjil)

label_genap_ganjil = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(label_genap_ganjil)""",
    },
    {
        "title": "Latihan 11: Class Rekening Bank",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Rekening dengan:",
            "  - __init__ mengisi pemilik dan saldo (saldo pakai _saldo)",
            "  - @property saldo (getter)",
            "  - method setor(jumlah) dan tarik(jumlah)",
            "    (tarik hanya boleh jika saldo cukup, kembalikan True/False)",
            "  - method __str__ untuk menampilkan info rekening dengan rapi",
            "",
            "Keluaran yang diharapkan:",
            "    Rekening(Andi, saldo=100000)",
            "    Tarik 20000 berhasil? True",
            "    Tarik 999999 berhasil? False",
            "    Rekening(Andi, saldo=130000)",
        ],
        "hints": [
            "Baca ulang \"OOP: Class & Object\" dan \"OOP: Encapsulation & Dunder Methods\" untuk __init__, @property, dan __str__.",
            "Simpan saldo di self._saldo; garis bawah di depan artinya 'jangan disentuh dari luar' secara konvensi. Properti saldo cukup mengembalikannya. tarik() mengecek dulu apakah saldonya cukup, mengurangi saldo cuma kalau cukup, lalu mengembalikan True atau False.",
            "Getter-nya: @property di atas def saldo(self): return self._saldo. __str__ harus mengembalikan string dengan return f\"...\", bukan mencetaknya.",
        ],
        "solution": """class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            return True
        return False

    def tarik(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah
            return True
        return False

    def __str__(self):
        return f"Rekening({self.pemilik}, saldo={self._saldo})"


r = Rekening("Andi", 100000)
print(r)
r.setor(50000)
print(f"Tarik 20000 berhasil? {r.tarik(20000)}")
print(f"Tarik 999999 berhasil? {r.tarik(999999)}")
print(r)""",
    },
    {
        "title": "Latihan 12: Pewarisan Hewan",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Hewan (nama, method bersuara()).",
            "Buat subclass Kucing dan Anjing yang meng-override bersuara().",
            "Buat list berisi objek keduanya, lalu panggil bersuara()",
            "untuk semua (polymorphism).",
            "",
            "Keluaran yang diharapkan:",
            "    Tom: Meong!",
            "    Bobby: Guk!",
        ],
        "hints": [
            "Baca ulang \"OOP: Inheritance & Polymorphism\".",
            "Hewan menyimpan nama di __init__ dan punya method bersuara(). Kucing dan Anjing mewarisi Hewan, lalu menulis ulang bersuara() masing-masing. Taruh objek keduanya di satu list dan panggil bersuara() di dalam for.",
            "class Kucing(Hewan): sudah cukup untuk mewarisi. Kalau subclass butuh __init__ sendiri, panggil super().__init__(nama) di dalamnya.",
        ],
        "solution": """class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} bersuara.")


class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama}: Meong!")


class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama}: Guk!")


daftar_hewan = [Kucing("Tom"), Anjing("Bobby")]
for h in daftar_hewan:
    h.bersuara()""",
    },
    {
        "title": "Latihan 13: Exception Handling Kalkulator",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi bagi(a, b) yang menangani:",
            "  1. ZeroDivisionError jika b == 0",
            "  2. TypeError jika a atau b bukan angka",
            "Gunakan try-except-else-finally, lalu uji dengan",
            "beberapa kasus termasuk yang error.",
            "",
            "Keluaran yang diharapkan:",
            "    Pembagian berhasil.",
            "    -- selesai mencoba --",
            "    5.0",
            "    Error: tidak bisa membagi dengan nol!",
            "    -- selesai mencoba --",
            "    None",
            "    Error: kedua argumen harus berupa angka!",
            "    -- selesai mencoba --",
            "    None",
        ],
        "hints": [
            "Baca ulang \"Exception Handling\": urutan try, except, else, dan finally, serta kapan masing-masing jalan.",
            "Lakukan pembagian di dalam try. Tulis satu except untuk ZeroDivisionError dan satu untuk TypeError, kembalikan hasilnya di else, dan cetak penanda selesai di finally. Uji dengan pembagi biasa, nol, dan sebuah string.",
            "else cuma jalan kalau try nggak melempar error. finally selalu jalan, bahkan sesudah return di except atau else.",
        ],
        "solution": """def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: tidak bisa membagi dengan nol!")
        return None
    except TypeError:
        print("Error: kedua argumen harus berupa angka!")
        return None
    else:
        print("Pembagian berhasil.")
        return hasil
    finally:
        print("-- selesai mencoba --")


print(bagi(10, 2))
print(bagi(10, 0))
print(bagi(10, "a"))""",
    },
    {
        "title": "Latihan 14: Lambda & Higher-Order Function",
        "difficulty": "Lanjut",
        "question": [
            "Diberikan list mahasiswa berisi tuple (nama, nilai):",
            "  [('Andi', 80), ('Budi', 65), ('Citra', 92), ('Dedi', 70)]",
            "Menggunakan lambda + fungsi bawaan (map/filter/sorted):",
            "  1. Ambil hanya mahasiswa dengan nilai >= 75.",
            "  2. Urutkan berdasarkan nilai tertinggi ke terendah.",
            "  3. Buat list nama SAJA (tanpa nilai) dari hasil nomor 2.",
            "",
            "Keluaran yang diharapkan:",
            "    [('Andi', 80), ('Citra', 92)]",
            "    [('Citra', 92), ('Andi', 80)]",
            "    ['Citra', 'Andi']",
        ],
        "hints": [
            "Baca ulang \"Lambda & Higher-Order Function\": filter, sorted dengan key, dan map.",
            "Kerjakan berantai: filter dengan syarat nilai >= 75, urutkan hasilnya dengan sorted() memakai key nilai dan reverse=True, lalu map untuk mengambil namanya saja. Bungkus hasil filter dan map dengan list() supaya bisa dicetak.",
            "Di tiap tuple, m[0] adalah nama dan m[1] nilainya, jadi key untuk sorted() adalah lambda m: m[1].",
        ],
        "solution": """mahasiswa = [("Andi", 80), ("Budi", 65), ("Citra", 92), ("Dedi", 70)]

lulus = list(filter(lambda m: m[1] >= 75, mahasiswa))
print(lulus)          # [('Andi', 80), ('Citra', 92)]

urut = sorted(lulus, key=lambda m: m[1], reverse=True)
print(urut)           # [('Citra', 92), ('Andi', 80)]

nama_saja = list(map(lambda m: m[0], urut))
print(nama_saja)      # ['Citra', 'Andi']""",
    },
    {
        "title": "Latihan 15: Generator Fibonacci",
        "difficulty": "Sulit",
        "question": [
            "Buat generator function fibonacci(n) yang menghasilkan",
            "n bilangan pertama dari deret Fibonacci (0, 1, 1, 2, 3, 5, ...)",
            "menggunakan yield, TANPA menyimpan semua nilai ke list dulu.",
            "Tampilkan 10 bilangan pertama.",
            "",
            "Keluaran yang diharapkan:",
            "    0 1 1 2 3 5 8 13 21 34",
        ],
        "hints": [
            "Baca ulang \"Iterator & Generator\": fungsi yang memakai yield menghasilkan nilai satu per satu, tanpa list.",
            "Simpan dua nilai terakhir di a dan b, mulai dari 0 dan 1. Dalam perulangan sebanyak n kali, yield a lalu geser kedua nilainya. Cetak hasilnya dalam satu baris, dipisah spasi.",
            "Penggeserannya cukup satu baris: a, b = b, a + b. Untuk mencetak satu baris, pakai print(angka, end=\" \") di dalam for, lalu satu print() kosong sesudahnya.",
        ],
        "solution": """def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


for angka in fibonacci(10):
    print(angka, end=" ")
print()
# 0 1 1 2 3 5 8 13 21 34""",
    },
    {
        "title": "Latihan 16: Decorator Logging & Validasi",
        "difficulty": "Sulit",
        "question": [
            "Buat decorator log_panggilan yang mencetak nama fungsi",
            "dan argumennya SETIAP KALI fungsi dipanggil, lalu mencetak",
            "juga nilai yang dikembalikan. Terapkan ke fungsi tambah(a, b).",
            "",
            "Keluaran yang diharapkan:",
            "    Memanggil tambah dengan args=(3, 4), kwargs={}",
            "    tambah mengembalikan: 7",
        ],
        "hints": [
            "Baca ulang \"Decorator & Context Manager\": decorator adalah fungsi yang menerima fungsi lain dan mengembalikan fungsi pembungkus.",
            "Di dalam log_panggilan, buat fungsi wrapper(*args, **kwargs). Wrapper mencetak nama fungsi dan argumennya, memanggil fungsi asli, menyimpan hasilnya, mencetak hasil itu, lalu me-return-nya. log_panggilan sendiri mengembalikan wrapper.",
            "Nama fungsi asli ada di fungsi.__name__. Keluaran untuk tambah(3, 4) berbentuk: Memanggil tambah dengan args=(3, 4), kwargs={} lalu tambah mengembalikan: 7.",
        ],
        "solution": """def log_panggilan(fungsi):
    def wrapper(*args, **kwargs):
        print(f"Memanggil {fungsi.__name__} dengan args={args}, kwargs={kwargs}")
        hasil = fungsi(*args, **kwargs)
        print(f"{fungsi.__name__} mengembalikan: {hasil}")
        return hasil
    return wrapper


@log_panggilan
def tambah(a, b):
    return a + b


tambah(3, 4)
# Memanggil tambah dengan args=(3, 4), kwargs={}
# tambah mengembalikan: 7""",
    },
    {
        "title": "Latihan 17: File I/O + JSON Manajemen Kontak",
        "difficulty": "Sulit",
        "question": [
            "Buat program yang:",
            "  1. Menyimpan dictionary kontak (nama -> nomor) ke file",
            "     'kontak.json' menggunakan module json.",
            "  2. Membaca kembali file tersebut ke dalam dictionary baru.",
            "  3. Menambah satu kontak baru ke dictionary hasil baca,",
            "     lalu menyimpannya kembali ke file yang sama.",
            "Gunakan 'with' statement untuk semua operasi file.",
            "",
            "Keluaran yang diharapkan:",
            "    {'Andi': '0812-1111', 'Budi': '0813-2222'}",
            "    Kontak berhasil diperbarui: {'Andi': '0812-1111', 'Budi': '0813-2222', 'Citra': '0812-3333'}",
        ],
        "hints": [
            "Baca ulang \"File I/O\": blok with untuk membuka berkas, dan module json (dump untuk menulis, load untuk membaca).",
            "Pakai tiga blok with berurutan: tulis dict ke kontak.json dengan mode 'w', baca lagi dengan mode 'r' ke dict baru, tambahkan satu kontak, lalu tulis ulang dengan mode 'w'.",
            "json.dump(data, f, indent=2) menulis dengan rapi, dan json.load(f) mengembalikan dict.",
        ],
        "solution": """import json

kontak = {"Andi": "0812-1111", "Budi": "0813-2222"}

# 1. Simpan ke file
with open("kontak.json", "w") as f:
    json.dump(kontak, f, indent=2)

# 2. Baca kembali
with open("kontak.json", "r") as f:
    data_dibaca = json.load(f)
print(data_dibaca)

# 3. Tambah kontak baru & simpan ulang
data_dibaca["Citra"] = "0812-3333"
with open("kontak.json", "w") as f:
    json.dump(data_dibaca, f, indent=2)

print("Kontak berhasil diperbarui:", data_dibaca)""",
    },
    {
        "title": "Latihan 18: Unit Test dengan pytest untuk Rekening",
        "difficulty": "Sulit",
        "question": [
            "Menggunakan class Rekening dari Latihan 11, tulis unit test",
            "dengan pytest yang mencakup:",
            "  1. setor() menambah saldo dengan benar.",
            "  2. tarik() mengurangi saldo jika cukup.",
            "  3. tarik() mengembalikan False jika saldo tidak cukup",
            "     (dan saldo TIDAK berubah).",
            "Gunakan fixture pytest untuk membuat objek Rekening baru",
            "sebelum setiap test (menggantikan setUp di JUnit).",
        ],
        "hints": [
            "Baca ulang \"Virtual Environment, pip & Testing (pytest)\" dan \"Testing Lebih Dalam: fixture, parametrize & unittest\".",
            "Buat fungsi bertanda @pytest.fixture yang mengembalikan Rekening baru. Tiap fungsi test_... menerima fixture itu lewat nama parameternya, memanggil setor() atau tarik(), lalu memeriksa hasil dan saldonya dengan assert.",
            "Untuk kasus saldo nggak cukup, periksa dua hal: hasilnya False, dan saldonya masih sama dengan saldo awal.",
        ],
        "auto_check": False,
        "alasan_tidak_dicek": "butuh pytest terpasang dan file rekening.py terpisah",
        "solution": """import pytest
from rekening import Rekening   # asumsikan class Rekening di file rekening.py


@pytest.fixture
def rekening():
    return Rekening("Andi", 100000)


def test_setor_menambah_saldo(rekening):
    rekening.setor(50000)
    assert rekening.saldo == 150000


def test_tarik_berhasil_jika_saldo_cukup(rekening):
    hasil = rekening.tarik(30000)
    assert hasil is True
    assert rekening.saldo == 70000


def test_tarik_gagal_jika_saldo_tidak_cukup(rekening):
    hasil = rekening.tarik(999999)
    assert hasil is False
    assert rekening.saldo == 100000   # saldo tidak berubah

# Jalankan dengan: pytest -v""",
    },
    {
        'title': 'Proyek Akhir: Koperasi Sekolah',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Koperasi Sekolah',
        '',
        'Koperasi sekolahmu mencatat penjualan di buku tulis, dan tiap sore',
        'bendaharanya menghabiskan satu jam menghitung ulang. Kamu diminta',
        'menggantinya dengan satu program.',
        '',
        'Barang di koperasi (kode, nama, harga, stok awal):',
        '  BK01  Buku Tulis   4000   50',
        '  PN02  Pulpen       2500   40',
        '  PS03  Penghapus    1500   12',
        '  SP04  Spidol       8000    6',
        '',
        'Permintaan yang masuk hari ini, berurutan:',
        '  BK01 x12,  PN02 x20,  SP04 x10,  PS03 x5,  XX99 x1,  BK01 x8',
        '',
        'Dua di antaranya TIDAK BOLEH jadi penjualan: satu meminta lebih',
        'banyak daripada stok, satu lagi kodenya tidak ada. Keduanya wajib',
        'ditangani dengan exception -- bukan dengan if yang menyelinap --',
        'dan program tidak boleh berhenti karenanya.',
        '',
        'Yang harus ada di programmu:',
        '  1. class Barang dengan method nilai_stok() = harga x stok.',
        '  2. class turunan Exception sendiri untuk kasus stok kurang.',
        '  3. class Koperasi yang menyimpan barang dalam dict berkunci kode,',
        '     mencatat tiap penjualan yang BERHASIL, dan bisa menghitung',
        '     pemasukan serta jumlah laku per barang.',
        '  4. Barang diurutkan berdasarkan KODE saat dicetak.',
        "  5. 'Perlu dipesan lagi' berisi nama barang bersisa kurang dari 10,",
        '     diurutkan alfabetis.',
        '  6. Uang ditulis dengan pemisah titik: 137500 -> Rp137.500',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  LAPORAN KOPERASI SEKOLAH',
        '  ==============================================',
        '  Kode  Nama            Laku  Sisa    Nilai sisa',
        '  BK01  Buku Tulis        20    30     Rp120.000',
        '  PN02  Pulpen            20    20      Rp50.000',
        '  PS03  Penghapus          5     7      Rp10.500',
        '  SP04  Spidol             0     6      Rp48.000',
        '  ----------------------------------------------',
        '  Pemasukan hari ini : Rp137.500',
        '  Nilai stok tersisa : Rp228.500',
        '  Perlu dipesan lagi : Penghapus, Spidol',
        '  Transaksi gagal    : 2',
        '    - stok kurang - Spidol: diminta 10, tersisa 6',
        '    - kode tidak dikenal - XX99',
    ],
        "hints": [
            "Ulang materi \"OOP: Class & Object\", \"Exception Handling\", dan \"String & Formatting\". Rancang dulu tiga class-nya: Barang, exception untuk stok kurang, dan Koperasi yang menyimpan dict berkunci kode.",
            "Method jual() melempar KeyError kalau kodenya nggak ada dan exception buatanmu kalau stoknya kurang. Pemanggilnya menangkap keduanya dengan dua except terpisah, mencatat pesan gagalnya, lalu lanjut ke permintaan berikutnya. Penjualan yang berhasil dicatat sebagai pasangan (kode, jumlah), supaya pemasukan dan jumlah laku per barang bisa dihitung belakangan.",
            "Exception sendiri cukup class StokKurang(Exception): pass, dan urutan except menentukan siapa yang kena. Lebar kolom pakai f-string seperti f\"{b.kode:<6}{b.nama:<14}{laku:>6}\". Pemisah ribuan: f\"{n:,}\".replace(\",\", \".\").",
        ],
        'solution': """\"\"\"Koperasi Sekolah -- laporan penjualan satu hari.\"\"\"


class Barang:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def nilai_stok(self):
        return self.harga * self.stok


class StokKurang(Exception):
    \"\"\"Dipakai saat penjualan meminta lebih banyak daripada yang ada.\"\"\"


class Koperasi:
    def __init__(self):
        self.barang = {}
        self.terjual = []

    def tambah(self, barang):
        self.barang[barang.kode] = barang

    def jual(self, kode, jumlah):
        if kode not in self.barang:
            raise KeyError(kode)
        b = self.barang[kode]
        if jumlah > b.stok:
            raise StokKurang(f"{b.nama}: diminta {jumlah}, tersisa {b.stok}")
        b.stok -= jumlah
        self.terjual.append((kode, jumlah))
        return b.harga * jumlah

    def pemasukan(self):
        return sum(self.barang[k].harga * j for k, j in self.terjual)

    def laku_per_barang(self):
        hitung = {}
        for kode, jumlah in self.terjual:
            hitung[kode] = hitung.get(kode, 0) + jumlah
        return hitung


def rupiah(n):
    return "Rp" + f"{n:,}".replace(",", ".")


def main():
    kop = Koperasi()
    for kode, nama, harga, stok in [
        ("BK01", "Buku Tulis", 4000, 50),
        ("PN02", "Pulpen", 2500, 40),
        ("PS03", "Penghapus", 1500, 12),
        ("SP04", "Spidol", 8000, 6),
    ]:
        kop.tambah(Barang(kode, nama, harga, stok))

    permintaan = [("BK01", 12), ("PN02", 20), ("SP04", 10),
                  ("PS03", 5), ("XX99", 1), ("BK01", 8)]

    gagal = []
    for kode, jumlah in permintaan:
        try:
            kop.jual(kode, jumlah)
        except StokKurang as e:
            gagal.append(f"stok kurang - {e}")
        except KeyError as e:
            gagal.append(f"kode tidak dikenal - {e.args[0]}")

    print("LAPORAN KOPERASI SEKOLAH")
    print("=" * 46)

    laku = kop.laku_per_barang()
    print(f"{'Kode':<6}{'Nama':<14}{'Laku':>6}{'Sisa':>6}{'Nilai sisa':>14}")
    for kode in sorted(kop.barang):
        b = kop.barang[kode]
        print(f"{b.kode:<6}{b.nama:<14}{laku.get(kode, 0):>6}"
              f"{b.stok:>6}{rupiah(b.nilai_stok()):>14}")

    print("-" * 46)
    print(f"Pemasukan hari ini : {rupiah(kop.pemasukan())}")
    print(f"Nilai stok tersisa : "
          f"{rupiah(sum(b.nilai_stok() for b in kop.barang.values()))}")

    habis = [b.nama for b in kop.barang.values() if b.stok < 10]
    print(f"Perlu dipesan lagi : {', '.join(sorted(habis)) if habis else '-'}")

    print(f"Transaksi gagal    : {len(gagal)}")
    for g in gagal:
        print("  - " + g)


main()
""",
    },
]
