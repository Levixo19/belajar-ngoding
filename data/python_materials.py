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
        "title": "3. Operator",
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
        "title": "4. Percabangan (if / elif / else)",
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
        "title": "5. Perulangan (for & while)",
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
                ]
            },
        ],
    },
    {
        "title": "6. String & Formatting",
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
                    "  s[::-1]   -> 'nohtyP'  (trik membalik string)",
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
        ],
    },
    {
        "title": "7. List & Tuple",
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
        "title": "8. Dictionary & Set",
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
        "title": "9. Function (Fungsi)",
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
        "title": "10. Lambda & Higher-Order Function",
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
        "title": "11. List Comprehension & Generator Expression",
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
        "title": "12. OOP: Class & Object",
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
                    "  @staticmethod              -> tidak butuh self, seperti fungsi biasa",
                    "  def utilitas(): ...            di dalam namespace class.",
                    "  @classmethod                -> menerima cls (class-nya), bukan self.",
                    "  def dari_string(cls, s): ...",
                ]
            },
        ],
    },
    {
        "title": "13. OOP: Inheritance & Polymorphism",
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
        "title": "14. OOP: Encapsulation & Dunder Methods",
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
                ]
            },
        ],
    },
    {
        "title": "15. Exception Handling",
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
        "title": "16. Module & Package",
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
        "title": "17. File I/O",
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
                ]
            },
            {
                "heading": "Contoh menulis & membaca file teks",
                "code": """# Menulis file
with open("catatan.txt", "w") as f:
    f.write("Baris pertama\\n")
    f.write("Baris kedua\\n")
# file otomatis tertutup setelah keluar dari blok 'with'

# Membaca SELURUH isi file sekaligus
with open("catatan.txt", "r") as f:
    isi = f.read()
    print(isi)

# Membaca baris per baris (hemat memori untuk file besar)
with open("catatan.txt", "r") as f:
    for baris in f:
        print("Baca:", baris.strip())   # strip() buang newline

# Membaca semua baris jadi list
with open("catatan.txt", "r") as f:
    semua_baris = f.readlines()
    print(semua_baris)   # ['Baris pertama\\n', 'Baris kedua\\n']

# Menambah data tanpa menghapus isi lama
with open("catatan.txt", "a") as f:
    f.write("Baris tambahan\\n")"""
            },
            {
                "heading": "Bekerja dengan file JSON (format data paling umum)",
                "code": """import json

data = {"nama": "Andi", "umur": 20, "hobi": ["coding", "gaming"]}

# Menulis dict ke file JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Membaca file JSON jadi dict Python
with open("data.json", "r") as f:
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
                    "      with open(\"tidak_ada.txt\") as f:",
                    "          isi = f.read()",
                    "  except FileNotFoundError:",
                    "      print(\"File tidak ditemukan!\")",
                    "",
                    "Modul pathlib (cara modern kelola path file, lebih OOP):",
                    "  from pathlib import Path",
                    "  p = Path(\"data\") / \"catatan.txt\"",
                    "  print(p.exists())      # cek file ada atau tidak",
                    "  print(p.read_text())   # baca isi file langsung",
                ]
            },
        ],
    },
    {
        "title": "18. Iterator & Generator",
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
        "title": "19. Decorator & Context Manager",
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
        "title": "20. Virtual Environment, pip & Testing (pytest)",
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
        "title": "21. Roadmap Menjadi Python Developer Handal",
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
                    "  1. CLI tool sederhana (to-do list, expense tracker).",
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
                    "     flask, dsb) untuk belajar gaya kode yang baik.",
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
                    "     menunjuk PERSIS baris & jenis error yang terjadi.",
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
