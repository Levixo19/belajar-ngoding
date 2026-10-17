"""Gambar konsep kurikulum Python. Skema: inti/visual.py.

Materi Python sudah punya tombol "Lihat jalannya" yang melacak contoh kode
langkah demi langkah. Gambar di sini sengaja menjelaskan KONSEP-nya (slicing,
nama yang menunjuk objek, alur cabang, tumpukan panggilan, hierarki), bukan
mengulang jejak eksekusi baris per baris.
"""

VISUAL = {
    "Variabel & Tipe Data": [
        {
            "setelah": 1,
            "jenis": "variabel",
            "judul": "Lima nama, lima nilai, dan Python sendiri yang menentukan tipenya",
            "ket": "Nilainya sama dengan contoh kode di atas. Kamu nggak menulis "
                   "tipe di mana pun; type() yang memberi tahu.",
            "isi": [
                ["umur", "20", "int"],
                ["harga", "15000.5", "float"],
                ["nama", "\"Budi\"", "str"],
                ["lulus", "True", "bool"],
                ["data_kosong", "None", "NoneType"],
            ],
        },
    ],
    "Masukan, Keluaran & Modul Bawaan": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "\"a\\nb\" cuma tiga karakter, karena \\n itu satu karakter",
            "ket": "Backslash-nya nggak ikut tersimpan. Makanya len(\"a\\nb\") "
                   "memberi 3, bukan 4.",
            "nama": "\"a\\nb\"",
            "isi": ["a", "\\n", "b"],
            "sorot": [1],
        },
    ],
    "Operator": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Empat operator untuk 7 dan 2, empat hasil yang beda",
            "ket": "/ selalu memberi float. // membuang desimal dengan membulatkan "
                   "ke bawah, dan % memberi sisanya.",
            "tabel": [
                {
                    "kolom": ["ekspresi", "hasil", "tipe"],
                    "baris": [
                        ["7 / 2", "3.5", "float"],
                        ["7 // 2", "3", "int"],
                        ["7 % 2", "1", "int"],
                        ["2 ** 3", "8", "int"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "x == y True, x is y False: isinya sama, objeknya dua",
            "ket": "== membandingkan isi. is menanyakan apakah dua nama menunjuk "
                   "objek yang sama persis di memori.",
            "tumpukan": [["x", "@l1"], ["y", "@l2"]],
            "heap": [
                {"id": "l1", "isi": "list [1, 2, 3]"},
                {"id": "l2", "isi": "list [1, 2, 3]"},
            ],
            "label_tumpukan": "nama",
            "label_heap": "objek",
        },
    ],
    "Percabangan (if / elif / else)": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Python berhenti di cabang pertama yang True",
            "ket": "Untuk nilai 85, nilai >= 90 salah, lalu nilai >= 80 benar. "
                   "Yang tercetak B, dan cabang sisanya nggak diperiksa lagi.",
            "langkah": [
                {"jenis": "mulai", "teks": "nilai = 85"},
                {"jenis": "keputusan", "teks": "nilai >= 90?", "tidak": 3},
                {"jenis": "keluaran", "teks": "print(\"A\")", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai >= 80?", "tidak": 5},
                {"jenis": "keluaran", "teks": "print(\"B\")", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai >= 70?", "tidak": 7},
                {"jenis": "keluaran", "teks": "print(\"C\")", "ke": 8},
                {"jenis": "keluaran", "teks": "print(\"D\")"},
                {"jenis": "selesai", "teks": "lanjut ke baris sesudah if"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Nilai apa pun bisa jadi kondisi: nol dan wadah kosong itu falsy",
            "ket": "Sisanya truthy. Makanya if daftar: sama artinya dengan "
                   "if len(daftar) > 0:.",
            "tabel": [
                {
                    "nama": "nilai di dalam if",
                    "kolom": ["nilai", "dianggap"],
                    "baris": [
                        ["0, 0.0", "False"],
                        ["\"\"", "False"],
                        ["[], {}, ()", "False"],
                        ["None", "False"],
                        ["5, -1", "True"],
                        ["\"0\"", "True"],
                        ["[0]", "True"],
                    ],
                    "sorot_baris": [5, 6],
                },
            ],
        },
    ],
    "Perulangan (for & while)": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "while memeriksa kondisinya dulu, baru menjalankan isinya",
            "ket": "Ini while di contoh atas. Kalau j += 1 hilang, panah balik "
                   "itu berputar selamanya.",
            "langkah": [
                {"jenis": "mulai", "teks": "j = 1"},
                {"jenis": "keputusan", "teks": "j <= 5?", "tidak": 4},
                {"jenis": "keluaran", "teks": "print(j, end=\" \")"},
                {"jenis": "proses", "teks": "j += 1", "ke": 1},
                {"jenis": "selesai", "teks": "print() menutup baris"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "continue balik ke atas, break langsung keluar dari loop",
            "ket": "for i in range(1, 11) dari contoh di atas. Hasilnya "
                   "1 2 3 4 6 7: angka 5 dilewati, dan loop berhenti di 8.",
            "langkah": [
                {"jenis": "mulai", "teks": "for i in range(1, 11)"},
                {"jenis": "keputusan", "teks": "masih ada i berikutnya?", "tidak": 5},
                {"jenis": "keputusan", "teks": "i == 5? (continue)", "ya": 1, "tidak": 3},
                {"jenis": "keputusan", "teks": "i == 8? (break)", "ya": 5, "tidak": 4},
                {"jenis": "keluaran", "teks": "print(i, end=\" \")", "ke": 1},
                {"jenis": "selesai", "teks": "keluar dari loop"},
            ],
        },
    ],
    "Angka, Perbandingan & Operator yang Belum Dibahas": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "round() membulatkan nilai tengah ke angka genap terdekat",
            "ket": "Ini beda dari pelajaran sekolah. Untuk uang, pakai Decimal "
                   "dengan ROUND_HALF_UP seperti di contoh.",
            "tabel": [
                {
                    "kolom": ["ekspresi", "hasil", "ala sekolah"],
                    "baris": [
                        ["round(0.5)", "0", "1"],
                        ["round(1.5)", "2", "2"],
                        ["round(2.5)", "2", "3"],
                    ],
                    "sorot_baris": [0, 2],
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "bit",
            "judul": "izin = 5 sesudah izin tulis dicabut: bit BACA dan EKSEKUSI menyala",
            "ket": "Bit paling kanan BACA (1), tengah TULIS (2), kiri EKSEKUSI "
                   "(4). izin & TULIS memeriksa satu bit itu saja.",
            "angka": 5,
            "lebar": 4,
            "label": "izin = 0b101",
        },
    ],
    "String & Formatting": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "s[0:3] mengambil indeks 0, 1, dan 2, jadi hasilnya 'Pyt'",
            "ket": "Posisi akhir nggak ikut diambil. Indeks negatif dihitung dari "
                   "belakang, jadi s[-1] adalah 'n'.",
            "nama": "s = \"Python\"",
            "isi": ["P", "y", "t", "h", "o", "n"],
            "rentang": [0, 3],
            "penunjuk": {"s[0]": 0, "s[-1]": 5},
        },
    ],
    "List & Tuple": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "nilai[1:3] memberi [90, 75]: indeks 1 sampai sebelum 3",
            "ket": "List yang sama dengan contoh kode. nilai[-1] menunjuk elemen "
                   "terakhir, 60.",
            "nama": "nilai",
            "isi": ["80", "90", "75", "85", "60"],
            "rentang": [1, 3],
            "penunjuk": {"[0]": 0, "[-1]": 4},
        },
    ],
    "Fungsi Bawaan untuk Koleksi": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "zip() berhenti di koleksi terpendek, dan Dewi hilang tanpa error",
            "ket": "nama punya empat isi, nilai cuma tiga. Pasangan keempat nggak "
                   "pernah dibuat, dan zip() nggak memberi tahu.",
            "tabel": [
                {
                    "nama": "zip(nama, nilai)",
                    "kolom": ["nama", "nilai", "hasil zip"],
                    "baris": [
                        ["Andi", "85", "('Andi', 85)"],
                        ["Budi", "70", "('Budi', 70)"],
                        ["Citra", "95", "('Citra', 95)"],
                        ["Dewi", None, "nggak ada"],
                    ],
                    "sorot_baris": [3],
                },
            ],
        },
    ],
    "Dictionary & Set": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Dict itu pasangan key dan value; key yang dipakai untuk mencari",
            "ket": "mahasiswa[\"nama\"] memberi \"Andi\". Key yang nggak ada "
                   "berakhir KeyError, kecuali lewat get().",
            "tabel": [
                {
                    "nama": "mahasiswa",
                    "kolom": ["key", "value"],
                    "baris": [
                        ["\"nama\"", "\"Andi\""],
                        ["\"umur\"", "20"],
                        ["\"jurusan\"", "\"Informatika\""],
                    ],
                    "sorot_kolom": ["key"],
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Empat operasi himpunan untuk a = {1, 2, 3, 4} dan b = {3, 4, 5, 6}",
            "ket": "Isi hasilnya sama dengan contoh kode. Urutan isi set nggak "
                   "dijamin waktu dicetak.",
            "tabel": [
                {
                    "kolom": ["operasi", "artinya", "hasil"],
                    "baris": [
                        ["a | b", "gabungan", "{1,2,3,4,5,6}"],
                        ["a & b", "irisan", "{3,4}"],
                        ["a - b", "ada di a saja", "{1,2}"],
                        ["a ^ b", "di salah satu", "{1,2,5,6}"],
                    ],
                },
            ],
        },
    ],
    "Wadah Data Siap Pakai (module collections)": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Counter menghitung kata kalau diberi list hasil split()",
            "ket": "Kalimatnya sama dengan contoh. most_common(2) mengambil dua "
                   "baris teratas; kata yang nggak ada dihitung 0.",
            "tabel": [
                {
                    "nama": "Counter(kalimat.split())",
                    "kolom": ["kata", "jumlah"],
                    "baris": [
                        ["kucing", "2"],
                        ["ikan", "2"],
                        ["makan", "1"],
                        ["kecil", "1"],
                        ["tidur", "1"],
                    ],
                    "sorot_baris": [0, 1],
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "tumpukan",
            "mode": "antrean",
            "judul": "deque bisa ditambah dan diambil di dua ujungnya",
            "ket": "Keadaan antrean sesudah append(\"Citra\") dan "
                   "appendleft(\"Zaki\"). popleft() mengambil dari depan.",
            "isi": ["Zaki", "Andi", "Budi", "Citra"],
            "label": "deque antrean",
            "operasi": "popleft() -> Zaki",
        },
    ],
    "Function (Fungsi)": [
        {
            "setelah": 0,
            "jenis": "tumpukan",
            "judul": "Memanggil fungsi membuka ruang kerja baru di atas pemanggilnya",
            "ket": "a dan b cuma hidup selama tambah(3, 4) berjalan. Sesudah "
                   "return 7, ruangnya dibuang dan 7 diterima pemanggil.",
            "isi": ["tingkat modul", "tambah(a=3, b=4)"],
            "label": "tumpukan panggilan",
            "operasi": "return 7",
        },
    ],
    "Referensi Objek, Salinan & Jebakan Mutable": [
        {
            "setelah": 0,
            "jenis": "memori",
            "judul": "b = a nggak menyalin apa pun: dua label untuk satu list",
            "ket": "Makanya b.append(4) ikut terlihat dari a. Yang punya isi "
                   "adalah objeknya, namanya cuma penunjuk.",
            "tumpukan": [["a", "@l1"], ["b", "@l1"]],
            "heap": [{"id": "l1", "isi": "list [1, 2, 3, 4]"}],
            "label_tumpukan": "nama",
            "label_heap": "objek",
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Salinan dangkal: list luarnya baru, list di dalamnya masih bersama",
            "ket": "dangkal = asli[:]. asli[0] dan dangkal[0] menunjuk list yang "
                   "sama, jadi append(99) tembus ke asli.",
            "tumpukan": [
                ["asli", "@luar1"],
                ["dangkal", "@luar2"],
                ["asli[0]", "@d1"],
                ["dangkal[0]", "@d1"],
            ],
            "heap": [
                {"id": "luar1", "isi": "list luar: [d1, d2]"},
                {"id": "luar2", "isi": "list luar baru: [d1, d2]"},
                {"id": "d1", "isi": "list [1, 2, 99]"},
                {"id": "d2", "isi": "list [3, 4]"},
            ],
            "label_tumpukan": "nama",
            "label_heap": "objek",
        },
    ],
    "Rekursi": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "faktorial(4) menumpuk sampai base case, baru hasilnya dirakit balik",
            "ket": "Tiap panggilan menunggu di tumpukan sampai panggilan di "
                   "atasnya selesai. Yang paling atas yang pertama menjawab.",
            "isi": ["tingkat modul", "faktorial(4)", "faktorial(3)",
                    "faktorial(2)", "faktorial(1)"],
            "label": "tumpukan panggilan",
            "operasi": "base case: return 1",
        },
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "fib(4) menghitung fib(2) dua kali, dan makin besar makin boros",
            "ket": "Pekerjaan yang sama diulang dari nol. Cache menyimpan hasil "
                   "fib(2) sekali, lalu sisanya tinggal diambil.",
            "akar": {"teks": "fib(4)", "anak": [
                {"teks": "fib(3)", "anak": [
                    {"teks": "fib(2)", "anak": [
                        {"teks": "fib(1)"}, {"teks": "fib(0)"}]},
                    {"teks": "fib(1)"},
                ]},
                {"teks": "fib(2)", "anak": [
                    {"teks": "fib(1)"}, {"teks": "fib(0)"}]},
            ]},
        },
        {
            "setelah": 4,
            "jenis": "kurva",
            "judul": "Tanpa cache, kerja fib rekursif tumbuh eksponensial; versi loop linear",
            "ket": "Disederhanakan: kerja fib rekursif tanpa cache dibatasi 2^n. "
                   "Dengan cache atau versi loop, tiap n dihitung sekali.",
            "kurva": ["n", "2^n"],
            "sorot": "2^n",
        },
    ],
    "Membongkar Argumen & Parameter Khusus": [
        {
            "setelah": 3,
            "jenis": "larik",
            "judul": "nama, *nilai, status = baris: ujungnya diambil, tengahnya ke bintang",
            "ket": "nilai berisi ['80', '90', '70'], selalu berupa list, walaupun "
                   "sisanya kosong.",
            "nama": "baris",
            "isi": ["andi", "80", "90", "70", "lulus"],
            "rentang": [1, 4],
            "penunjuk": {"nama": 0, "status": 4},
        },
    ],
    "Anotasi Tipe (Type Hint)": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Cara membaca tipe koleksi yang pakai kurung siku",
            "ket": "Python nggak memeriksa satu pun dari ini. Yang memakainya "
                   "editor dan mypy.",
            "tabel": [
                {
                    "kolom": ["anotasi", "artinya"],
                    "baris": [
                        ["list[int]", "list isi int"],
                        ["dict[str, int]", "key str -> int"],
                        ["tuple[str, int]", "str lalu int"],
                        ["tuple[int, ...]", "int sebanyaknya"],
                        ["int | None", "int atau None"],
                    ],
                },
            ],
        },
    ],
    "Lambda & Higher-Order Function": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "map mengubah tiap elemen, filter cuma menyisakan yang lolos",
            "ket": "angka = [5, 3, 8, 1, 9, 2] dari contoh. map memberi enam "
                   "hasil, filter genap cuma menyisakan 8 dan 2.",
            "tabel": [
                {
                    "kolom": ["angka", "map x * 2", "filter genap"],
                    "baris": [
                        ["5", "10", None],
                        ["3", "6", None],
                        ["8", "16", "8"],
                        ["1", "2", None],
                        ["9", "18", None],
                        ["2", "4", "2"],
                    ],
                    "sorot_baris": [2, 5],
                },
            ],
        },
    ],
    "Scope, Closure & nonlocal": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "LEGB: Python mencari nama dari scope terdalam ke luar",
            "ket": "Pencarian berhenti di tempat pertama yang punya nama itu. "
                   "Kalau sampai Built-in pun nggak ketemu, muncul NameError.",
            "isi": ["B: print, len, sum", "G: pesan Global", "E: pesan Enclosing",
                    "L: pesan Local"],
            "label": "dicari dari atas",
            "operasi": "ketemu di L",
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Tiap fungsi hasil pembuat_pengali membawa faktornya sendiri",
            "ket": "pembuat_pengali sudah selesai, tapi faktor tetap hidup di sel "
                   "yang menempel pada fungsi kali. Dua fungsi, dua sel.",
            "tumpukan": [["kali3", "@f3"], ["kali10", "@f10"]],
            "heap": [
                {"id": "f3", "isi": "fungsi kali, faktor = 3"},
                {"id": "f10", "isi": "fungsi kali, faktor = 10"},
            ],
            "label_tumpukan": "nama",
            "label_heap": "fungsi + sel",
        },
    ],
    "List Comprehension & Generator Expression": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "[x for x in range(1, 11) if x % 2 == 0] adalah loop ini",
            "ket": "Kondisi if di ujung comprehension menyaring sebelum x "
                   "dimasukkan. Hasilnya [2, 4, 6, 8, 10].",
            "langkah": [
                {"jenis": "mulai", "teks": "hasil = []"},
                {"jenis": "keputusan", "teks": "ada x berikutnya?", "tidak": 4},
                {"jenis": "keputusan", "teks": "x % 2 == 0?", "tidak": 1},
                {"jenis": "proses", "teks": "hasil.append(x)", "ke": 1},
                {"jenis": "selesai", "teks": "hasil jadi list baru"},
            ],
        },
    ],
    "OOP: Class & Object": [
        {
            "setelah": 1,
            "jenis": "memori",
            "judul": "Satu class Mahasiswa, dua objek dengan atributnya sendiri",
            "ket": "self di dalam method menunjuk objek yang sedang dipakai. "
                   "m1.nama dan m2.nama dua atribut yang terpisah.",
            "tumpukan": [["m1", "@o1"], ["m2", "@o2"]],
            "heap": [
                {"id": "o1", "isi": "Mahasiswa nama=Andi umur=20"},
                {"id": "o2", "isi": "Mahasiswa nama=Budi umur=22"},
            ],
            "label_tumpukan": "nama",
            "label_heap": "objek",
        },
    ],
    "OOP: Inheritance & Polymorphism": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Kucing dan Anjing mewarisi Hewan, lalu menimpa bersuara()",
            "ket": "Anjing menambah atribut ras lewat super().__init__(nama). "
                   "h.bersuara() memilih method sesuai class asli objeknya.",
            "akar": {"teks": "Hewan: bersuara()", "anak": [
                {"teks": "Kucing: Meong!"},
                {"teks": "Anjing: Guk! + ras"},
            ]},
        },
    ],
    "Abstract Base Class & Kontrak Antar-Class": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Satu kontrak, dua turunan yang lengkap, satu yang ditolak",
            "ket": "PenyimpanSetengahJadi lupa menulis ambil(), jadi objeknya "
                   "gagal dibuat dengan TypeError.",
            "akar": {"teks": "Penyimpan (ABC)", "anak": [
                {"teks": "PenyimpanMemori"},
                {"teks": "PenyimpanBaris"},
                {"teks": "SetengahJadi: X"},
            ]},
        },
    ],
    "OOP: Encapsulation & Dunder Methods": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Di balik operator dan fungsi bawaan ada dunder method yang dipanggil",
            "ket": "Class Titik di atas menulis empat yang pertama. Tanpa "
                   "__str__, print() cuma menampilkan alamat objek.",
            "tabel": [
                {
                    "kolom": ["yang kamu tulis", "yang dipanggil"],
                    "baris": [
                        ["print(p1)", "p1.__str__()"],
                        ["repr(p1)", "p1.__repr__()"],
                        ["p1 == p2", "p1.__eq__(p2)"],
                        ["p1 + p2", "p1.__add__(p2)"],
                        ["len(x)", "x.__len__()"],
                        ["x[i]", "x.__getitem__(i)"],
                    ],
                },
            ],
        },
    ],
    "dataclass & Enum": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Tiap anggota Enum punya nama dan nilai",
            "ket": "Status(\"selesai\") mencari lewat nilai, Status[\"SELESAI\"] "
                   "lewat nama. Nilai yang nggak terdaftar ditolak ValueError.",
            "tabel": [
                {
                    "nama": "class Status(Enum)",
                    "kolom": [".name", ".value"],
                    "baris": [
                        ["MENUNGGU", "\"menunggu\""],
                        ["DIKIRIM", "\"dikirim\""],
                        ["SELESAI", "\"selesai\""],
                    ],
                },
            ],
        },
    ],
    "Exception Handling": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "except cuma jalan kalau ada error, else kalau nggak ada, finally selalu",
            "ket": "Disederhanakan untuk satu blok except. Kalau jenis error-nya "
                   "nggak cocok dengan except mana pun, error itu lanjut ke luar.",
            "langkah": [
                {"jenis": "mulai", "teks": "try: hasil = a / b"},
                {"jenis": "keputusan", "teks": "terjadi error?", "tidak": 3},
                {"jenis": "proses", "teks": "jalankan except yang cocok", "ke": 4},
                {"jenis": "proses", "teks": "jalankan else"},
                {"jenis": "proses", "teks": "jalankan finally"},
                {"jenis": "selesai", "teks": "lanjut ke baris berikutnya"},
            ],
        },
    ],
    "Membaca Traceback & Menangkap Error Secara Luas": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "Tiga frame yang sedang jalan waktu int('tiga puluh') gagal",
            "ket": "Di layar, traceback mencetaknya terbalik: frame paling atas "
                   "di sini muncul paling bawah, tepat di atas baris ValueError.",
            "isi": ["<module> line 24", "rata_rata_umur l12", "baca_baris line 6"],
            "label": "frame, terbaru di atas",
            "operasi": "ValueError",
        },
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "except X ikut menangkap semua turunan X",
            "ket": "Silsilahnya diringkas. except Exception menangkap seluruh "
                   "cabang di bawah Exception, tapi nggak menyentuh SystemExit "
                   "dan KeyboardInterrupt.",
            "akar": {"teks": "BaseException", "anak": [
                {"teks": "SystemExit"},
                {"teks": "KeyboardInterrupt"},
                {"teks": "Exception", "anak": [
                    {"teks": "ArithmeticError", "anak": [
                        {"teks": "ZeroDivisionError"}]},
                    {"teks": "LookupError", "anak": [
                        {"teks": "IndexError"}, {"teks": "KeyError"}]},
                    {"teks": "ValueError"},
                    {"teks": "TypeError"},
                ]},
            ]},
        },
    ],
    "Module & Package": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Blok if __name__ == \"__main__\" cuma jalan kalau berkasnya dijalankan langsung",
            "ket": "Lewat python3 file.py, __name__ berisi \"__main__\". Lewat "
                   "import, isinya nama modul, jadi bloknya dilewati.",
            "langkah": [
                {"jenis": "mulai", "teks": "Python membaca berkas"},
                {"jenis": "proses", "teks": "def tambah(a, b) didaftarkan"},
                {"jenis": "keputusan", "teks": "__name__ == \"__main__\"?", "tidak": 4},
                {"jenis": "keluaran", "teks": "print(tambah(2, 3))"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Struktur Project Python": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Paket toko/ di tengah, tests/ dan main.py sengaja di luarnya",
            "ket": "Folder yang punya __init__.py adalah paket. Import relatif "
                   "seperti from ..uang dihitung dari posisi berkasnya di pohon ini.",
            "akar": {"teks": "toko-online/", "anak": [
                {"teks": "pyproject.toml"},
                {"teks": "README.md"},
                {"teks": "main.py"},
                {"teks": "toko/", "anak": [
                    {"teks": "__init__.py"},
                    {"teks": "uang.py"},
                    {"teks": "laporan.py"},
                    {"teks": "model/", "anak": [
                        {"teks": "__init__.py"},
                        {"teks": "produk.py"},
                    ]},
                ]},
                {"teks": "tests/", "anak": [
                    {"teks": "test_uang.py"},
                    {"teks": "test_produk.py"},
                ]},
            ]},
        },
    ],
    "Program Baris Perintah: sys, os & argparse": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "sys.argv untuk python3 ringkas.py laporan.txt -n 3",
            "ket": "Indeks 0 nama programnya sendiri, dan kata python3 nggak "
                   "ikut. Semua isinya str, termasuk '3'.",
            "tabel": [
                {
                    "nama": "sys.argv",
                    "kolom": ["indeks", "isi"],
                    "baris": [
                        ["0", "'ringkas.py'"],
                        ["1", "'laporan.txt'"],
                        ["2", "'-n'"],
                        ["3", "'3'"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Logging: Pengganti print di Program Sungguhan": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "level=logging.INFO artinya: tampilkan yang nilainya 20 ke atas",
            "ket": "Level itu angka yang dibandingkan. Tanpa basicConfig, batasnya "
                   "WARNING, jadi info dan debug ikut hilang.",
            "tabel": [
                {
                    "nama": "basicConfig(level=INFO)",
                    "kolom": ["level", "nilai", "tampil?"],
                    "baris": [
                        ["DEBUG", "10", "disaring"],
                        ["INFO", "20", "ya"],
                        ["WARNING", "30", "ya"],
                        ["ERROR", "40", "ya"],
                        ["CRITICAL", "50", "ya"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Tanggal & Waktu (datetime)": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Tanggal dan durasi berhitung seperti aljabar",
            "ket": "tgl di sini objek datetime, durasi objek timedelta. "
                   "Menambah angka polos ke tanggal langsung TypeError.",
            "tabel": [
                {
                    "kolom": ["ekspresi", "hasilnya"],
                    "baris": [
                        ["tgl - tgl", "timedelta"],
                        ["tgl + durasi", "datetime"],
                        ["durasi + durasi", "timedelta"],
                        ["tgl + 7", "TypeError"],
                    ],
                    "sorot_baris": [3],
                },
            ],
        },
    ],
    "File I/O": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Mode open() menentukan nasib isi lama berkasnya",
            "ket": "Error untuk 'r' adalah FileNotFoundError, untuk 'x' "
                   "FileExistsError. Mode 'w' mengosongkan berkas begitu dibuka.",
            "tabel": [
                {
                    "kolom": ["mode", "berkas sudah ada", "belum ada"],
                    "baris": [
                        ["'r'", "dibaca", "error"],
                        ["'w'", "dikosongkan", "dibuat"],
                        ["'a'", "tambah di akhir", "dibuat"],
                        ["'x'", "error", "dibuat"],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "Encoding, bytes & Berkas Biner": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "\"Café\" empat karakter, tapi lima byte dalam UTF-8",
            "ket": "Isi \"Café\".encode(\"utf-8\"). Huruf ASCII tetap satu "
                   "byte, é jadi dua byte, c3 dan a9 (heksadesimal).",
            "nama": "UTF-8 \"Café\"",
            "isi": ["43 C", "61 a", "66 f", "c3", "a9"],
            "sorot": [3, 4],
        },
    ],
    "Regular Expression (modul re)": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Pola yang sama, empat fungsi, empat jawaban berbeda",
            "ket": "Pola r\"[A-Z]-\\d+\" atas teks \"Order A-19 ... C-7 batal.\" "
                   "dari contoh. match cuma melihat awal teks.",
            "tabel": [
                {
                    "kolom": ["fungsi", "melihat", "hasil"],
                    "baris": [
                        ["re.search", "di mana pun", "Match A-19"],
                        ["re.match", "awal teks saja", "None"],
                        ["re.fullmatch", "seluruh teks", "None"],
                        ["re.findall", "semua tempat", "3 teks"],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "Iterator & Generator": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Generator membeku di yield dan lanjut waktu nilai berikutnya diminta",
            "ket": "Disederhanakan untuk hitung_mundur(2). For-loop memanggil "
                   "next() sendiri sampai StopIteration muncul.",
            "pelaku": ["for-loop", "hitung_mundur"],
            "pesan": [
                [0, 1, "next()"],
                [1, 0, "yield 2, lalu membeku"],
                [0, 1, "next()"],
                [1, 0, "yield 1, lalu membeku"],
                [0, 1, "next()"],
                [1, 0, "print Selesai, StopIteration"],
            ],
        },
    ],
    "itertools & yield from": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "groupby cuma memotong saat key berubah, jadi urutkan dulu",
            "ket": "Data yang sama dengan contoh. Tanpa sort, buah muncul dua "
                   "kali karena datanya berselang.",
            "tabel": [
                {
                    "nama": "tanpa sort: 4 grup",
                    "kolom": ["kunci", "anggota"],
                    "baris": [
                        ["buah", "apel"],
                        ["sayur", "bayam"],
                        ["buah", "jeruk"],
                        ["sayur", "kangkung"],
                    ],
                },
                {
                    "nama": "sesudah sort: 2 grup",
                    "kolom": ["kunci", "anggota"],
                    "baris": [
                        ["buah", "apel, jeruk"],
                        ["sayur", "bayam, kangkung"],
                    ],
                },
            ],
            "panah": "data.sort(key=kategori)",
        },
    ],
    "Decorator & Context Manager": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Sesudah @ukur_waktu, nama proses_data menunjuk wrapper",
            "ket": "Pemanggil nggak tahu ada wrapper. wrapper yang memanggil "
                   "fungsi aslinya, mengukur waktunya, lalu meneruskan hasilnya.",
            "pelaku": ["pemanggil", "wrapper", "fungsi asli"],
            "pesan": [
                [0, 1, "proses_data(1000000)"],
                [1, 2, "fungsi(*args, **kwargs)"],
                [2, 1, "return 499999500000"],
                [1, 0, "cetak waktu, return hasil"],
            ],
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "with menjamin __exit__ jalan sesudah bloknya selesai",
            "ket": "__exit__ juga jalan kalau isi blok with melempar error. Di "
                   "situ berkasnya ditutup.",
            "langkah": [
                {"jenis": "mulai", "teks": "with BukaFile(...) as f"},
                {"jenis": "proses", "teks": "__enter__: buka berkas"},
                {"jenis": "proses", "teks": "isi blok: f.write(\"Halo!\")"},
                {"jenis": "proses", "teks": "__exit__: tutup berkas"},
                {"jenis": "selesai", "teks": "lanjut sesudah with"},
            ],
        },
    ],
    "Introspeksi Objek & Decorator Lanjutan": [
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "@luar di atas @dalam: dipasang dari bawah, dijalankan dari atas",
            "ket": "kerja = luar(dalam(kerja)). Waktu kerja() dipanggil, wrapper "
                   "luar masuk duluan dan keluar paling akhir.",
            "isi": ["kerja asli", "wrapper dalam", "wrapper luar"],
            "label": "lapisan pembungkus",
            "operasi": "kerja() masuk luar",
        },
    ],
    "Konkurensi: Thread, Proses & GIL": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Jenis pekerjaannya yang menentukan alatnya",
            "ket": "GIL membuat thread menghitung bergantian, tapi dilepas "
                   "selama thread menunggu. Ukur dulu sebelum memilih.",
            "tabel": [
                {
                    "kolom": ["pekerjaan", "waktunya habis", "pakai"],
                    "baris": [
                        ["unduh, query", "menunggu", "thread"],
                        ["hitung, kompres", "menghitung", "proses"],
                        ["ribuan koneksi", "menunggu", "asyncio"],
                    ],
                },
            ],
        },
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Race condition: dua kali tambah, stok cuma naik satu",
            "ket": "Disederhanakan dari contoh stok[\"beras\"]. Thread B membaca "
                   "sebelum A menulis, lalu menimpanya. Lock mencegah selipan ini.",
            "pelaku": ["thread A", "stok", "thread B"],
            "pesan": [
                [0, 1, "baca beras = 5"],
                [2, 1, "baca beras = 5"],
                [0, 1, "tulis 5 + 1 = 6"],
                [2, 1, "tulis 5 + 1 = 6"],
            ],
        },
    ],
    "Asinkron: async, await & asyncio": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Di setiap await, event loop memberi giliran ke coroutine lain",
            "ket": "Disederhanakan dari dengan_gather(). Dua unduhan 0,3 detik "
                   "menunggu bersamaan, jadi totalnya sekitar 0,3 detik.",
            "pelaku": ["main", "event loop", "unduh a", "unduh b"],
            "pesan": [
                [0, 1, "gather(unduh a, unduh b)"],
                [1, 2, "mulai"],
                [2, 1, "await sleep: lepas giliran"],
                [1, 3, "mulai"],
                [3, 1, "await sleep: lepas giliran"],
                [2, 1, "bangun, return 'A'"],
                [3, 1, "bangun, return 'B'"],
                [1, 0, "['A', 'B']"],
            ],
        },
    ],
    "Virtual Environment, pip & Testing (pytest)": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Satu fungsi test: siapkan, panggil, lalu periksa",
            "ket": "Pola AAA. Kalau satu assert salah, test itu dilaporkan "
                   "FAILED dan test lain tetap dijalankan.",
            "langkah": [
                {"jenis": "mulai", "teks": "pytest menemukan test_*"},
                {"jenis": "proses", "teks": "Arrange: siapkan data"},
                {"jenis": "proses", "teks": "Act: panggil fungsi"},
                {"jenis": "keputusan", "teks": "Assert: hasilnya benar?", "tidak": 5},
                {"jenis": "keluaran", "teks": "PASSED", "ke": 6},
                {"jenis": "keluaran", "teks": "FAILED + nilai dua sisi"},
                {"jenis": "selesai", "teks": "test berikutnya"},
            ],
        },
    ],
    "Testing Lebih Dalam: fixture, parametrize & unittest": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Fixture ber-yield: persiapan sebelum test, pembersihan sesudahnya",
            "ket": "pytest mencocokkan nama parameter dompet dengan nama fixture. "
                   "Baris sesudah yield jalan, test-nya lulus atau gagal.",
            "pelaku": ["pytest", "fixture dompet", "test"],
            "pesan": [
                [0, 1, "panggil dompet()"],
                [1, 0, "yield Dompet(100)"],
                [0, 2, "test_...(dompet)"],
                [2, 0, "selesai, lulus atau gagal"],
                [0, 1, "lanjut sesudah yield"],
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Satu fungsi berparameter jadi empat test bernama sendiri",
            "ket": "Data dari test_hitung_pajak di atas. Di laporan namanya jadi "
                   "test_hitung_pajak[0-0] dan seterusnya.",
            "tabel": [
                {
                    "nama": "\"gaji, pajak\"",
                    "kolom": ["gaji", "pajak", "id test"],
                    "baris": [
                        ["0", "0", "0-0"],
                        ["5000000", "0", "5000000-0"],
                        ["6000000", "50000", "6000000-50000"],
                        ["10000000", "250000", "10000000-250000"],
                    ],
                },
            ],
        },
    ],
    "Roadmap Menjadi Python Developer Handal": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Satu fondasi, tiga jalur spesialisasi",
            "ket": "Nama alat di tiap jalur diambil dari roadmap di atas. Fondasi "
                   "yang sama dipakai di ketiganya.",
            "akar": {"teks": "Fondasi Python", "anak": [
                {"teks": "Web", "anak": [
                    {"teks": "Flask / Django"}, {"teks": "FastAPI"}]},
                {"teks": "Data / AI", "anak": [
                    {"teks": "NumPy, Pandas"}, {"teks": "scikit-learn"}]},
                {"teks": "Otomasi", "anak": [
                    {"teks": "requests"}, {"teks": "Ansible"}]},
            ]},
        },
    ],
}
