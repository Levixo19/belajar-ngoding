PYTHON_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Python.",
            "(Nama boleh diganti dengan nama sendiri)",
        ],
        "hints": [
            "Gunakan print() untuk tiap baris.",
            "Teks diapit tanda kutip ' atau \".",
            "Python tidak butuh titik koma di akhir baris.",
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
        ],
        "hints": [
            "a = 15; b = 4",
            "Ingat / selalu hasil float, // hasil bulat.",
            "Gunakan f-string untuk menampilkan hasil dengan rapi.",
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
        ],
        "hints": [
            "Gunakan input() untuk membaca dari keyboard (hasilnya string).",
            "Ubah ke int dengan int(input()), tanpa argumen di dalam input().",
            "Gunakan if-else atau ternary satu baris.",
        ],
        "stdin": "80\n",
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
        "difficulty": "Sedang",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20",
            "beserta total jumlahnya.",
            "Contoh output: 2 4 6 8 10 12 14 16 18 20, Total: 110",
        ],
        "hints": [
            "Gunakan for dengan range(1, 21) dan cek n % 2 == 0.",
            "Kumpulkan angka genap ke list, lalu pakai sum().",
        ],
        "solution": """genap = [n for n in range(1, 21) if n % 2 == 0]

print(*genap)   # unpacking list jadi argumen print terpisah spasi
print(f"Total: {sum(genap)}")""",
    },
    {
        "title": "Latihan 5: Pola Bintang",
        "difficulty": "Sedang",
        "question": [
            "Buat pola segitiga siku-siku dari bintang:",
            "  *",
            "  **",
            "  ***",
            "  ****",
            "  *****",
        ],
        "hints": [
            "Gunakan nested loop (for di dalam for).",
            "print('*' * i) bisa dipakai untuk mengulang karakter tanpa loop dalam.",
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
        "difficulty": "Sedang",
        "question": [
            "Diberikan list nilai = [80, 90, 75, 85, 60, 95, 70].",
            "Tampilkan: nilai terbesar, terkecil, rata-rata, dan",
            "list nilai yang sudah diurutkan dari terbesar ke terkecil.",
        ],
        "hints": [
            "Gunakan fungsi bawaan max(), min(), sum(), len().",
            "sorted(list, reverse=True) untuk urutan menurun.",
        ],
        "solution": """nilai = [80, 90, 75, 85, 60, 95, 70]

print(f"Terbesar: {max(nilai)}")
print(f"Terkecil: {min(nilai)}")
print(f"Rata-rata: {sum(nilai) / len(nilai):.2f}")
print(f"Urutan menurun: {sorted(nilai, reverse=True)}")""",
    },
    {
        "title": "Latihan 7: Fungsi Hitung Luas",
        "difficulty": "Sedang",
        "question": [
            "Buat 3 fungsi:",
            "  1. luas_persegi(sisi)          -> sisi * sisi",
            "  2. luas_persegi_panjang(p, l)  -> p * l",
            "  3. luas_lingkaran(r)           -> pi * r * r (pakai module math)",
            "Panggil ketiganya dan tampilkan hasilnya.",
        ],
        "hints": [
            "import math lalu pakai math.pi.",
            "def nama_fungsi(parameter): ... return hasil",
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
        "difficulty": "Sedang",
        "question": [
            "Diberikan kalimat = '  Belajar Python itu Menyenangkan  '.",
            "Tampilkan:",
            "  1. Kalimat tanpa spasi di ujung.",
            "  2. Kalimat dalam huruf besar semua.",
            "  3. Jumlah kata dalam kalimat.",
            "  4. Kalimat dengan kata 'Python' diganti 'Coding'.",
        ],
        "hints": [
            "strip() untuk buang spasi ujung.",
            "split() memecah kalimat jadi list kata, len() untuk menghitung.",
            "replace(lama, baru) untuk mengganti kata.",
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
        "difficulty": "Sedang",
        "question": [
            "Buat dictionary kontak kosong. Tambahkan 3 kontak",
            "(nama sebagai key, nomor telepon sebagai value).",
            "Tampilkan semua kontak dengan format 'nama: nomor'.",
            "Lalu cari satu kontak yang mungkin tidak ada dengan aman",
            "(tanpa error) menggunakan .get().",
        ],
        "hints": [
            "kontak = {}",
            "kontak['Andi'] = '0812xxxx'",
            "for nama, no in kontak.items(): ...",
            "kontak.get('Zaki', 'Tidak ditemukan')",
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
        "difficulty": "Menengah",
        "question": [
            "Diberikan list angka = list(range(1, 21)).",
            "Menggunakan SATU list comprehension untuk masing-masing:",
            "  1. Ambil semua kelipatan 3.",
            "  2. Buat list berisi kuadrat dari bilangan ganjil saja.",
            "  3. Buat dictionary {angka: 'genap'/'ganjil'} untuk 1-10.",
        ],
        "hints": [
            "[x for x in angka if x % 3 == 0]",
            "[x**2 for x in angka if x % 2 != 0]",
            "{x: ('genap' if x % 2 == 0 else 'ganjil') for x in range(1, 11)}",
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
        "difficulty": "Menengah",
        "question": [
            "Buat class Rekening dengan:",
            "  - __init__ mengisi pemilik dan saldo (saldo pakai _saldo)",
            "  - @property saldo (getter)",
            "  - method setor(jumlah) dan tarik(jumlah)",
            "    (tarik hanya boleh jika saldo cukup, kembalikan True/False)",
            "  - method __str__ untuk menampilkan info rekening dengan rapi",
        ],
        "hints": [
            "self._saldo untuk atribut 'protected' secara konvensi.",
            "@property def saldo(self): return self._saldo",
            "def __str__(self): return f'...'",
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
        "difficulty": "Menengah",
        "question": [
            "Buat class Hewan (nama, method bersuara()).",
            "Buat subclass Kucing dan Anjing yang meng-override bersuara().",
            "Buat list berisi objek keduanya, lalu panggil bersuara()",
            "untuk semua (polymorphism).",
        ],
        "hints": [
            "class Kucing(Hewan): def bersuara(self): ...",
            "super().__init__(nama) untuk memanggil constructor induk.",
            "for h in daftar_hewan: h.bersuara()",
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
        "difficulty": "Menengah",
        "question": [
            "Buat fungsi bagi(a, b) yang menangani:",
            "  1. ZeroDivisionError jika b == 0",
            "  2. TypeError jika a atau b bukan angka",
            "Gunakan try-except-else-finally, lalu uji dengan",
            "beberapa kasus termasuk yang error.",
        ],
        "hints": [
            "except ZeroDivisionError: ...",
            "except TypeError: ...",
            "else dijalankan jika tidak ada error, finally selalu jalan.",
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
        "difficulty": "Menengah",
        "question": [
            "Diberikan list mahasiswa berisi tuple (nama, nilai):",
            "  [('Andi', 80), ('Budi', 65), ('Citra', 92), ('Dedi', 70)]",
            "Menggunakan lambda + fungsi bawaan (map/filter/sorted):",
            "  1. Ambil hanya mahasiswa dengan nilai >= 75.",
            "  2. Urutkan berdasarkan nilai tertinggi ke terendah.",
            "  3. Buat list nama SAJA (tanpa nilai) dari hasil nomor 2.",
        ],
        "hints": [
            "filter(lambda m: m[1] >= 75, mahasiswa)",
            "sorted(hasil, key=lambda m: m[1], reverse=True)",
            "map(lambda m: m[0], hasil_urut)",
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
        ],
        "hints": [
            "Gunakan dua variabel a, b untuk melacak dua nilai terakhir.",
            "yield a, lalu a, b = b, a + b di dalam loop.",
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
        ],
        "hints": [
            "def log_panggilan(fungsi): def wrapper(*args, **kwargs): ...",
            "Panggil fungsi asli di dalam wrapper, simpan hasilnya, lalu return.",
            "Gunakan fungsi.__name__ untuk mendapat nama fungsi asli.",
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
        ],
        "hints": [
            "json.dump(data, f, indent=2) untuk menulis.",
            "json.load(f) untuk membaca.",
            "Gabungkan langkah baca -> update dict -> tulis ulang.",
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
            "import pytest, gunakan @pytest.fixture untuk membuat objek.",
            "Fungsi test menerima fixture sebagai parameter.",
            "assert hasil == nilai_yang_diharapkan",
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
]
