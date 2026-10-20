"""Kurikulum Data & Analitik.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

DATA_EXERCISES = [
    {
        "title": "Latihan 1: Ringkasan Nilai Ujian",
        "difficulty": "Mudah",
        "question": [
            "Nilai ujian sepuluh siswa sudah ditulis di kode:",
            "",
            "  nilai = [78, 85, 62, 90, 85, 71, 88, 95, 85, 69]",
            "",
            "Hitung sendiri, tanpa modul statistics:",
            "  - mean (rata-rata)",
            "  - median (nilai tengah sesudah diurutkan)",
            "  - modus (nilai yang paling sering muncul)",
            "  - simpangan baku sampel (bagi dengan n - 1)",
            "",
            "Cetak mean, median, dan simpangan baku dengan dua angka di",
            "belakang koma. Sesudah itu, bandingkan keempat hasilmu dengan",
            "statistics.mean, median, mode, dan stdev. Kalau semuanya sama",
            "(dibandingkan dalam bentuk dua desimal), cetak baris",
            "\"cocok dengan modul statistics\".",
            "",
            "Keluaran yang diharapkan:",
            "mean   : 80.80",
            "median : 85.00",
            "modus  : 85",
            "stdev  : 10.48",
            "cocok dengan modul statistics",
        ],
        "hints": [
            "Mean itu jumlah dibagi banyaknya data, median itu nilai tengah dari data yang sudah diurutkan, dan modus itu nilai yang paling sering muncul.",
            "Banyaknya data genap, jadi median adalah rata-rata dua nilai di tengah; untuk simpangan baku sampel, jumlahkan kuadrat jarak tiap nilai ke mean, bagi dengan n - 1, lalu ambil akarnya.",
            "Hitung kemunculan tiap nilai dengan dict, ambil modus dengan max(hitung, key=hitung.get), lalu bandingkan f\"{x:.2f}\" milikmu dengan f\"{st.mean(nilai):.2f}\" dan kawan-kawannya.",
        ],
        "solution": """import statistics as st

nilai = [78, 85, 62, 90, 85, 71, 88, 95, 85, 69]

n = len(nilai)
mean = sum(nilai) / n

urut = sorted(nilai)
tengah = n // 2
if n % 2 == 1:
    median = urut[tengah]
else:
    median = (urut[tengah - 1] + urut[tengah]) / 2

hitung = {}
for x in nilai:
    hitung[x] = hitung.get(x, 0) + 1
modus = max(hitung, key=hitung.get)

jarak = sum((x - mean) ** 2 for x in nilai)
stdev = (jarak / (n - 1)) ** 0.5

print(f"mean   : {mean:.2f}")
print(f"median : {median:.2f}")
print(f"modus  : {modus}")
print(f"stdev  : {stdev:.2f}")

sama = (
    f"{mean:.2f}" == f"{st.mean(nilai):.2f}"
    and f"{median:.2f}" == f"{st.median(nilai):.2f}"
    and modus == st.mode(nilai)
    and f"{stdev:.2f}" == f"{st.stdev(nilai):.2f}"
)
print("cocok dengan modul statistics" if sama else "belum cocok")
""",
    },
    {
        "title": "Latihan 2: Garis Regresi Kuadrat Terkecil",
        "difficulty": "Mudah",
        "question": [
            "Data enam rumah: luas (meter persegi) dan harga (juta rupiah).",
            "",
            "  data = [(36, 310), (45, 365), (54, 430), (60, 470), (72, 560), (90, 690)]",
            "",
            "Hitung kemiringan dan intersep garis regresi dengan rumus",
            "kuadrat terkecil, tanpa statistics.linear_regression:",
            "",
            "  kemiringan = jumlah (x - rata_x)(y - rata_y)",
            "               / jumlah (x - rata_x) kuadrat",
            "  intersep   = rata_y - kemiringan x rata_x",
            "",
            "Cetak keduanya dengan dua desimal, lalu cetak perkiraan harga",
            "untuk luas 40, 65, dan 80 meter persegi dengan satu desimal.",
            "",
            "Keluaran yang diharapkan:",
            "kemiringan : 7.10",
            "intersep   : 48.60",
            "luas 40 m2 -> 332.5 juta",
            "luas 65 m2 -> 509.9 juta",
            "luas 80 m2 -> 616.3 juta",
        ],
        "hints": [
            "Hitung dulu rata-rata luas dan rata-rata harga, karena kedua rumus memakai jarak tiap titik ke rata-ratanya.",
            "Pembilang kemiringan menjumlahkan perkalian jarak x dan jarak y, sedangkan penyebutnya menjumlahkan kuadrat jarak x saja.",
            "Pakai sum((x - rata_x) * (y - rata_y) for x, y in data) untuk pembilang, lalu harga perkiraan = kemiringan * luas + intersep dicetak dengan f\"{harga:.1f}\".",
        ],
        "solution": """data = [(36, 310), (45, 365), (54, 430), (60, 470), (72, 560), (90, 690)]

n = len(data)
rata_x = sum(x for x, _ in data) / n
rata_y = sum(y for _, y in data) / n

atas = sum((x - rata_x) * (y - rata_y) for x, y in data)
bawah = sum((x - rata_x) ** 2 for x, _ in data)
kemiringan = atas / bawah
intersep = rata_y - kemiringan * rata_x

print(f"kemiringan : {kemiringan:.2f}")
print(f"intersep   : {intersep:.2f}")
for luas in (40, 65, 80):
    harga = kemiringan * luas + intersep
    print(f"luas {luas} m2 -> {harga:.1f} juta")
""",
    },
    {
        "title": "Latihan 3: Pivot Penjualan dengan Dict",
        "difficulty": "Mudah",
        "question": [
            "Data penjualan per wilayah per bulan sudah ditanam di kode",
            "sebagai CSV di dalam io.StringIO:",
            "",
            "  wilayah,bulan,jumlah",
            "  Jawa,2026-01,120",
            "  Bali,2026-01,40",
            "  Sumatra,2026-02,75",
            "  Jawa,2026-02,130",
            "  Bali,2026-02,55",
            "  Sumatra,2026-01,60",
            "  Jawa,2026-01,30",
            "  Bali,2026-03,70",
            "  Jawa,2026-03,90",
            "",
            "Buat tabel pivot: wilayah sebagai baris (urut alfabetis), bulan",
            "sebagai kolom (urut), isinya total jumlah, ditambah kolom total",
            "di ujung kanan. Wilayah yang nggak punya penjualan di suatu",
            "bulan diisi 0. Lebar kolom wilayah 8 karakter rata kiri, tiap",
            "kolom angka 8 karakter rata kanan.",
            "",
            "Keluaran yang diharapkan:",
            "wilayah  2026-01 2026-02 2026-03   total",
            "Bali          40      55      70     165",
            "Jawa         150     130      90     370",
            "Sumatra       60      75       0     135",
        ],
        "hints": [
            "Pivot table itu pengelompokan dua arah, jadi kumpulkan totalnya dalam satu dict yang kuncinya pasangan (wilayah, bulan).",
            "Sesudah semua baris dijumlahkan, ambil daftar bulan dan daftar wilayah yang unik dari kunci dict itu, lalu urutkan masing-masing.",
            "Untuk tiap wilayah, buat list angka dengan pivot.get((w, b), 0) untuk semua bulan, lalu cetak dengan f\"{w:<8}\" dan f\"{x:>8}\" ditambah sum(angka) di ujungnya.",
        ],
        "solution": "import csv\nimport io\nfrom collections import defaultdict\n\ndata = io.StringIO(\"\"\"wilayah,bulan,jumlah\nJawa,2026-01,120\nBali,2026-01,40\nSumatra,2026-02,75\nJawa,2026-02,130\nBali,2026-02,55\nSumatra,2026-01,60\nJawa,2026-01,30\nBali,2026-03,70\nJawa,2026-03,90\n\"\"\")\n\npivot = defaultdict(int)\nfor baris in csv.DictReader(data):\n    pivot[(baris[\"wilayah\"], baris[\"bulan\"])] += int(baris[\"jumlah\"])\n\nsemua_bulan = sorted({b for _, b in pivot})\nsemua_wilayah = sorted({w for w, _ in pivot})\n\nprint(f\"{'wilayah':<8}\" + \"\".join(f\"{b:>8}\" for b in semua_bulan) + f\"{'total':>8}\")\nfor w in semua_wilayah:\n    angka = [pivot.get((w, b), 0) for b in semua_bulan]\n    print(f\"{w:<8}\" + \"\".join(f\"{x:>8}\" for x in angka) + f\"{sum(angka):>8}\")\n",
    },
    {
        "title": "Latihan 4: Broadcasting Larik Mini",
        "difficulty": "Menengah",
        "question": [
            "Tulis fungsi tambah(a, b) yang meniru broadcasting NumPy untuk",
            "penjumlahan, tanpa NumPy. a selalu list 2D (list berisi list",
            "yang sama panjang). b bisa berupa:",
            "  - angka (skalar), ditambahkan ke semua sel",
            "  - list 1D sepanjang jumlah kolom, ditambahkan ke tiap baris",
            "  - list 2D yang tiap dimensinya sama dengan a atau bernilai 1",
            "",
            "Kalau bentuknya nggak cocok, lempar ValueError dengan pesan",
            "\"bentuk (baris, kolom) dan <bentuk b> tidak bisa di-broadcast\",",
            "dengan bentuk b ditulis sebagai tuple, misalnya (2,).",
            "",
            "Uji dengan a = [[1, 2, 3], [4, 5, 6]] dan empat nilai b:",
            "10, [10, 20, 30], [[100], [200]], dan [1, 2]. Cetak nama",
            "kasusnya rata kiri 11 karakter, lalu \" -> \" dan hasilnya,",
            "atau \"galat: \" disusul pesan error-nya.",
            "",
            "Keluaran yang diharapkan:",
            "skalar      -> [[11, 12, 13], [14, 15, 16]]",
            "baris       -> [[11, 22, 33], [14, 25, 36]]",
            "kolom       -> [[101, 102, 103], [204, 205, 206]]",
            "tidak cocok -> galat: bentuk (2, 3) dan (2,) tidak bisa di-broadcast",
        ],
        "hints": [
            "Aturan broadcasting membandingkan ukuran tiap dimensi: dua ukuran cocok kalau sama atau salah satunya 1.",
            "Ubah semua bentuk b jadi list 2D lebih dulu: skalar jadi [[b]] dan list 1D jadi [b], lalu cek apakah banyak baris dan kolomnya 1 atau sama dengan milik a.",
            "Saat mengisi sel hasil i, j, ambil b2[i if bb > 1 else 0][j if bk > 1 else 0] supaya dimensi berukuran 1 dipakai ulang.",
        ],
        "solution": """def bentuk(x):
    if isinstance(x, (int, float)):
        return ()
    if isinstance(x[0], list):
        return (len(x), len(x[0]))
    return (len(x),)


def tambah(a, b):
    baris, kolom = len(a), len(a[0])
    sb = bentuk(b)
    if sb == ():
        b2 = [[b]]
    elif len(sb) == 1:
        b2 = [b]
    else:
        b2 = b
    bb, bk = len(b2), len(b2[0])
    if bb not in (1, baris) or bk not in (1, kolom):
        raise ValueError(f"bentuk {(baris, kolom)} dan {sb} tidak bisa di-broadcast")
    hasil = []
    for i in range(baris):
        baru = []
        for j in range(kolom):
            nilai_b = b2[i if bb > 1 else 0][j if bk > 1 else 0]
            baru.append(a[i][j] + nilai_b)
        hasil.append(baru)
    return hasil


a = [[1, 2, 3],
     [4, 5, 6]]
kasus = [
    ("skalar", 10),
    ("baris", [10, 20, 30]),
    ("kolom", [[100], [200]]),
    ("tidak cocok", [1, 2]),
]
for nama, b in kasus:
    try:
        print(f"{nama:<11} -> {tambah(a, b)}")
    except ValueError as e:
        print(f"{nama:<11} -> galat: {e}")
""",
    },
    {
        "title": "Latihan 5: Mencari Minimum dengan Gradient Descent",
        "difficulty": "Menengah",
        "question": [
            "Fungsi f(x) = (x - 3) kuadrat + 1 punya titik terendah di x = 3.",
            "Temukan titik itu dengan gradient descent, seolah kamu belum",
            "tahu jawabannya.",
            "",
            "  - Turunan f adalah 2 x (x - 3).",
            "  - Mulai dari x = 0.0 dengan laju belajar 0.1.",
            "  - Jalankan 30 langkah: x = x - laju x turunan(x).",
            "  - Tiap kelipatan 5 langkah, cetak nomor langkah (lebar 2,",
            "    rata kanan), x, dan f(x), keduanya dengan 4 desimal.",
            "",
            "Keluaran yang diharapkan:",
            "langkah  5: x = 2.0170, f(x) = 1.9664",
            "langkah 10: x = 2.6779, f(x) = 1.1038",
            "langkah 15: x = 2.8944, f(x) = 1.0111",
            "langkah 20: x = 2.9654, f(x) = 1.0012",
            "langkah 25: x = 2.9887, f(x) = 1.0001",
            "langkah 30: x = 2.9963, f(x) = 1.0000",
        ],
        "hints": [
            "Gradient descent melangkah berlawanan arah dengan turunan, dan besar langkahnya diatur laju belajar.",
            "Tulis dua fungsi kecil, f(x) dan turunan(x), lalu perbarui x di dalam perulangan for langkah in range(1, 31).",
            "Cetak hanya kalau langkah % 5 == 0, dengan f\"langkah {langkah:2}: x = {x:.4f}, f(x) = {f(x):.4f}\".",
        ],
        "solution": """def f(x):
    return (x - 3) ** 2 + 1


def turunan(x):
    return 2 * (x - 3)


x = 0.0
laju = 0.1
for langkah in range(1, 31):
    x = x - laju * turunan(x)
    if langkah % 5 == 0:
        print(f"langkah {langkah:2}: x = {x:.4f}, f(x) = {f(x):.4f}")
""",
    },
    {
        "title": "Latihan 6: Group By Penjualan Tanpa pandas",
        "difficulty": "Menengah",
        "question": [
            "Daftar transaksi sudah ditanam di kode sebagai list of dict:",
            "",
            "  transaksi = [",
            "      {\"kategori\": \"minuman\", \"nominal\": 18000},",
            "      {\"kategori\": \"makanan\", \"nominal\": 22000},",
            "      {\"kategori\": \"minuman\", \"nominal\": 15000},",
            "      {\"kategori\": \"snack\", \"nominal\": 8000},",
            "      {\"kategori\": \"makanan\", \"nominal\": 35000},",
            "      {\"kategori\": \"minuman\", \"nominal\": 21000},",
            "      {\"kategori\": \"snack\", \"nominal\": 12000},",
            "      {\"kategori\": \"makanan\", \"nominal\": 27000},",
            "      {\"kategori\": \"minuman\", \"nominal\": 18000},",
            "  ]",
            "",
            "Tanpa pandas, hitung per kategori: total nominal, rata-rata",
            "(dua desimal), dan jumlah transaksi. Urutkan dari total",
            "terbesar. Lebar kolom: kategori 9 rata kiri, total 7, rata 10,",
            "dan n 3, ketiganya rata kanan. Cetak baris judul dulu.",
            "",
            "Keluaran yang diharapkan:",
            "kategori   total      rata  n",
            "makanan    84000  28000.00  3",
            "minuman    72000  18000.00  4",
            "snack      20000  10000.00  2",
        ],
        "hints": [
            "Group by itu tiga langkah: pecah per kategori, hitung di tiap kelompok, lalu gabungkan hasilnya.",
            "Simpan satu dict per kategori berisi total dan banyaknya transaksi, lalu urutkan item dict itu memakai total dengan tanda minus.",
            "Pakai kelompok.setdefault(t[\"kategori\"], {\"total\": 0, \"n\": 0}) di dalam perulangan, lalu cetak dengan f\"{nama:<9}{total:>7}{rata:>10.2f}{n:>3}\".",
        ],
        "solution": """transaksi = [
    {"kategori": "minuman", "nominal": 18000},
    {"kategori": "makanan", "nominal": 22000},
    {"kategori": "minuman", "nominal": 15000},
    {"kategori": "snack", "nominal": 8000},
    {"kategori": "makanan", "nominal": 35000},
    {"kategori": "minuman", "nominal": 21000},
    {"kategori": "snack", "nominal": 12000},
    {"kategori": "makanan", "nominal": 27000},
    {"kategori": "minuman", "nominal": 18000},
]

kelompok = {}
for t in transaksi:
    k = kelompok.setdefault(t["kategori"], {"total": 0, "n": 0})
    k["total"] += t["nominal"]
    k["n"] += 1

urut = sorted(kelompok.items(), key=lambda p: (-p[1]["total"], p[0]))
print(f"{'kategori':<9}{'total':>7}{'rata':>10}{'n':>3}")
for nama, k in urut:
    rata = k["total"] / k["n"]
    print(f"{nama:<9}{k['total']:>7}{rata:>10.2f}{k['n']:>3}")
""",
    },
    {
        "title": "Latihan 7: Membersihkan Data Pelanggan",
        "difficulty": "Menengah",
        "question": [
            "Data pelanggan berikut sudah ditanam di kode sebagai CSV di",
            "dalam io.StringIO (perhatikan spasi di awal baris kedua):",
            "",
            "  nama,email,kota",
            "    andi pratama ,ANDI@MAIL.COM,bandung",
            "  Siti Rahma,siti@mail.com , Jakarta",
            "  ANDI PRATAMA,andi@mail.com,Bandung",
            "  budi,,surabaya",
            "  Dewi Lestari,dewi@mail.com,YOGYAKARTA",
            "  siti rahma,SITI@mail.com,jakarta",
            "",
            "Bersihkan dengan aturan ini:",
            "  1. Buang spasi di ujung semua kolom.",
            "  2. Nama dan kota jadi huruf kapital di awal kata, email jadi",
            "     huruf kecil semua.",
            "  3. Baris tanpa email dibuang.",
            "  4. Baris dengan email yang sudah muncul sebelumnya dianggap",
            "     kembar dan dibuang (yang pertama disimpan).",
            "",
            "Cetak jumlah baris sebelum, alasan pembuangan, jumlah sesudah,",
            "lalu data bersih urut nama dengan pemisah \" | \".",
            "",
            "Keluaran yang diharapkan:",
            "sebelum : 6 baris",
            "dibuang : 1 tanpa email, 2 kembar",
            "sesudah : 3 baris",
            "Andi Pratama | andi@mail.com | Bandung",
            "Dewi Lestari | dewi@mail.com | Yogyakarta",
            "Siti Rahma | siti@mail.com | Jakarta",
        ],
        "hints": [
            "Rapikan teks lebih dulu sebelum mencari baris kembar, karena ANDI@MAIL.COM dan andi@mail.com baru terlihat sama sesudah disamakan hurufnya.",
            "Baca dengan csv.DictReader, lalu untuk tiap baris pakai strip(), title(), dan lower(), dan simpan email yang sudah terlihat di sebuah set.",
            "Hitung dua penghitung terpisah, tanpa_email dan kembar, simpan baris bersih sebagai tuple (nama, email, kota), lalu cetak sorted(bersih).",
        ],
        "solution": "import csv\nimport io\n\nmentah = io.StringIO(\"\"\"nama,email,kota\n  andi pratama ,ANDI@MAIL.COM,bandung\nSiti Rahma,siti@mail.com , Jakarta\nANDI PRATAMA,andi@mail.com,Bandung\nbudi,,surabaya\nDewi Lestari,dewi@mail.com,YOGYAKARTA\nsiti rahma,SITI@mail.com,jakarta\n\"\"\")\nbaris = list(csv.DictReader(mentah))\n\nbersih = []\nsudah = set()\ntanpa_email = 0\nkembar = 0\nfor b in baris:\n    nama = b[\"nama\"].strip().title()\n    email = b[\"email\"].strip().lower()\n    kota = b[\"kota\"].strip().title()\n    if not email:\n        tanpa_email += 1\n        continue\n    if email in sudah:\n        kembar += 1\n        continue\n    sudah.add(email)\n    bersih.append((nama, email, kota))\n\nprint(f\"sebelum : {len(baris)} baris\")\nprint(f\"dibuang : {tanpa_email} tanpa email, {kembar} kembar\")\nprint(f\"sesudah : {len(bersih)} baris\")\nfor nama, email, kota in sorted(bersih):\n    print(f\"{nama} | {email} | {kota}\")\n",
    },
    {
        "title": "Latihan 8: Histogram Teks",
        "difficulty": "Menengah",
        "question": [
            "Waktu antar pesanan (menit) dari 20 pesanan sudah ditanam di",
            "kode:",
            "",
            "  waktu = [12, 7, 25, 18, 9, 31, 14, 22, 5, 16,",
            "           11, 27, 19, 8, 13, 24, 17, 10, 29, 15]",
            "",
            "Buat histogram teks dengan kelas selebar 5 menit, mulai dari 5",
            "sampai 34: 5-9, 10-14, 15-19, 20-24, 25-29, 30-34. Untuk tiap",
            "kelas cetak batasnya, garis tegak, batang # sebanyak isinya",
            "(rata kiri selebar 6), lalu jumlahnya. Batas bawah ditulis rata",
            "kanan selebar 2, batas atas rata kiri selebar 2. Di akhir, cetak",
            "jumlah seluruh pesanan.",
            "",
            "Keluaran yang diharapkan:",
            " 5-9  | ####   4",
            "10-14 | #####  5",
            "15-19 | #####  5",
            "20-24 | ##     2",
            "25-29 | ###    3",
            "30-34 | #      1",
            "total 20 pesanan",
        ],
        "hints": [
            "Histogram membagi rentang angka jadi kelas-kelas yang lebarnya sama, lalu menghitung berapa nilai yang jatuh di tiap kelas.",
            "Ulangi batas bawah kelas dengan range(5, 35, 5); batas atasnya batas bawah ditambah 4, dan hitung nilai yang berada di antara keduanya.",
            "Pakai sum(1 for w in waktu if bawah <= w <= atas), lalu cetak f\"{bawah:>2}-{atas:<2} | {'#' * banyak:<6} {banyak}\".",
        ],
        "solution": """waktu = [12, 7, 25, 18, 9, 31, 14, 22, 5, 16,
         11, 27, 19, 8, 13, 24, 17, 10, 29, 15]

lebar = 5
for bawah in range(5, 35, lebar):
    atas = bawah + lebar - 1
    banyak = sum(1 for w in waktu if bawah <= w <= atas)
    print(f"{bawah:>2}-{atas:<2} | {'#' * banyak:<6} {banyak}")
print(f"total {len(waktu)} pesanan")
""",
    },
    {
        "title": "Latihan 9: Uji Permutasi Dua Grup",
        "difficulty": "Menengah",
        "question": [
            "Sebuah aplikasi kasir mencoba fitur pencarian barang baru. Waktu",
            "melayani satu pembeli (detik) dicatat lima kali tanpa fitur dan",
            "lima kali dengan fitur:",
            "",
            "  tanpa = [31, 28, 35, 30, 33]",
            "  dengan = [26, 29, 24, 27, 30]",
            "",
            "Lakukan uji permutasi eksak dua sisi tanpa angka acak:",
            "",
            "  1. Hitung beda rata-rata teramati (tanpa dikurangi dengan).",
            "  2. Gabungkan sepuluh angka itu, lalu coba SEMUA cara memilih lima",
            "     angka untuk grup \"dengan\" (pakai itertools.combinations).",
            "  3. Hitung berapa pembagian yang beda rata-ratanya, dalam nilai",
            "     mutlak, sama atau lebih besar dari beda teramati.",
            "  4. p-value = jumlah itu dibagi jumlah semua pembagian.",
            "",
            "Angka pecahan dicetak dua desimal, p-value empat desimal.",
            "",
            "Keluaran yang diharapkan:",
            "Rata-rata tanpa fitur: 31.40",
            "Rata-rata dengan fitur: 27.20",
            "Beda teramati: 4.20",
            "Jumlah pembagian: 252",
            "Seekstrem atau lebih: 12",
            "p-value: 0.0476",
        ],
        "hints": [
            "Kalau fitur itu nggak berpengaruh, label tanpa dan dengan bisa ditukar sesukanya, jadi semua cara membagi sepuluh angka ke dua grup berukuran lima sama mungkinnya.",
            "combinations(range(10), 5) memberi 252 pilihan posisi untuk grup dengan; sisanya otomatis jadi grup tanpa.",
            "Karena dua grup sama besar, membandingkan selisih jumlah sudah setara dengan membandingkan selisih rata-rata, dan bilangan bulat terhindar dari masalah pembulatan float.",
            "Jumlah grup tanpa bisa dihitung dari total sepuluh angka dikurangi jumlah grup dengan, lalu bandingkan abs(selisih) dengan abs(selisih teramati).",
        ],
        "solution": """from itertools import combinations

tanpa = [31, 28, 35, 30, 33]
dengan = [26, 29, 24, 27, 30]

n = len(dengan)
gabung = tanpa + dengan
total_semua = sum(gabung)
selisih_teramati = sum(tanpa) - sum(dengan)

jumlah = 0
ekstrem = 0
for pilih in combinations(range(len(gabung)), n):
    jumlah_dengan = sum(gabung[i] for i in pilih)
    jumlah_tanpa = total_semua - jumlah_dengan
    jumlah += 1
    if abs(jumlah_tanpa - jumlah_dengan) >= abs(selisih_teramati):
        ekstrem += 1

print(f"Rata-rata tanpa fitur: {sum(tanpa) / n:.2f}")
print(f"Rata-rata dengan fitur: {sum(dengan) / n:.2f}")
print(f"Beda teramati: {selisih_teramati / n:.2f}")
print(f"Jumlah pembagian: {jumlah}")
print(f"Seekstrem atau lebih: {ekstrem}")
print(f"p-value: {ekstrem / jumlah:.4f}")
""",
    },
    {
        "title": "Latihan 10: Rata-rata Bergerak Tujuh Hari",
        "difficulty": "Menengah",
        "question": [
            "Penjualan nasi kotak sebuah warung selama 14 hari (hari ke-1 sampai",
            "ke-14) tercatat di list ini:",
            "",
            "  jual = [52, 61, 48, 70, 95, 120, 110, 58, 63, 55, 72, 99, 125, 118]",
            "",
            "Untuk hari ke-7 sampai ke-14, cetak penjualan hari itu dan rata-rata",
            "bergerak 7 hari, yaitu rata-rata hari itu dan enam hari sebelumnya.",
            "Nomor hari dicetak rata kanan selebar dua karakter, rata-rata dengan",
            "dua desimal.",
            "",
            "Keluaran yang diharapkan:",
            "Hari  7: terjual 110, rata-rata 7 hari 79.43",
            "Hari  8: terjual 58, rata-rata 7 hari 80.29",
            "Hari  9: terjual 63, rata-rata 7 hari 80.57",
            "Hari 10: terjual 55, rata-rata 7 hari 81.57",
            "Hari 11: terjual 72, rata-rata 7 hari 81.86",
            "Hari 12: terjual 99, rata-rata 7 hari 82.43",
            "Hari 13: terjual 125, rata-rata 7 hari 83.14",
            "Hari 14: terjual 118, rata-rata 7 hari 84.29",
        ],
        "hints": [
            "Hari ke-h ada di indeks h - 1, jadi jendela tujuh hari yang berakhir di hari ke-h mencakup indeks h - 7 sampai h - 1.",
            "Potongan list jual[h - 7:h] memberi tujuh angka itu, karena batas akhir potongan nggak ikut diambil.",
            "Ulangi untuk h dari 7 sampai 14 dengan range(7, 15), lalu cetak dengan format {h:2} dan {rata:.2f}.",
        ],
        "solution": """jual = [52, 61, 48, 70, 95, 120, 110, 58, 63, 55, 72, 99, 125, 118]

for h in range(7, len(jual) + 1):
    jendela = jual[h - 7:h]
    rata = sum(jendela) / 7
    print(f"Hari {h:2}: terjual {jual[h - 1]}, rata-rata 7 hari {rata:.2f}")
""",
    },
    {
        "title": "Latihan 11: Kolom Lebih Hemat dari Baris",
        "difficulty": "Menengah",
        "question": [
            "Data penjualan yang sama disimpan dengan dua tata letak:",
            "",
            "  - BARIS: list of dict, satu dict per transaksi (kolom id, tanggal,",
            "    kota, total).",
            "  - KOLOM: dict of list, satu list per kolom, dibuat dari BARIS.",
            "",
            "Tulis dua fungsi yang menjumlahkan kolom total sambil menghitung",
            "berapa nilai yang disentuh. Parameter kota opsional: kalau diisi,",
            "hanya transaksi di kota itu yang dijumlahkan.",
            "",
            "  - jumlah_baris(baris_baris, kota=None): membaca satu baris berarti",
            "    menyentuh SEMUA nilainya, jadi tiap baris menambah len(baris)",
            "    sentuhan, apa pun isinya.",
            "  - jumlah_kolom(kolom, kota=None): tiap elemen list yang diakses",
            "    dihitung satu sentuhan. Tanpa kota, cukup baca list total. Dengan",
            "    kota, baca seluruh list kota, lalu ambil total hanya untuk",
            "    posisi yang cocok.",
            "",
            "Jalankan dua query, lalu cetak hasilnya seperti di bawah:",
            "SUM(total), dan SUM(total) untuk kota Bandung.",
            "",
            "Datanya (salin ke programmu):",
            "",
            "  BARIS = [",
            "      {\"id\": 1, \"tanggal\": \"2026-09-01\", \"kota\": \"Bandung\", \"total\": 120000},",
            "      {\"id\": 2, \"tanggal\": \"2026-09-01\", \"kota\": \"Bogor\", \"total\": 80000},",
            "      {\"id\": 3, \"tanggal\": \"2026-09-02\", \"kota\": \"Bandung\", \"total\": 95000},",
            "      {\"id\": 4, \"tanggal\": \"2026-09-02\", \"kota\": \"Depok\", \"total\": 150000},",
            "      {\"id\": 5, \"tanggal\": \"2026-09-03\", \"kota\": \"Bogor\", \"total\": 110000},",
            "      {\"id\": 6, \"tanggal\": \"2026-09-03\", \"kota\": \"Bandung\", \"total\": 130000},",
            "  ]",
            "",
            "Keluaran yang diharapkan:",
            "SUM(total)",
            "  baris: total 685000, nilai disentuh 24",
            "  kolom: total 685000, nilai disentuh 6",
            "  hemat 18 dari 24 sentuhan",
            "SUM(total) WHERE kota = Bandung",
            "  baris: total 345000, nilai disentuh 24",
            "  kolom: total 345000, nilai disentuh 9",
            "  hemat 15 dari 24 sentuhan",
        ],
        "hints": [
            "Di tata letak baris, mencari kolom total tetap berarti melewati semua kolom lain di baris itu, makanya tiap baris dihitung penuh.",
            "Tata letak kolom bisa dibuat dengan dict comprehension: untuk tiap nama kolom di BARIS[0], kumpulkan nilai kolom itu dari semua baris.",
            "Di jumlah_kolom versi berkota, telusuri kolom kota dengan enumerate supaya posisi i bisa dipakai untuk mengambil kolom[\"total\"][i], dan tambah satu sentuhan lagi hanya saat kotanya cocok.",
        ],
        "solution": """BARIS = [
    {"id": 1, "tanggal": "2026-09-01", "kota": "Bandung", "total": 120000},
    {"id": 2, "tanggal": "2026-09-01", "kota": "Bogor", "total": 80000},
    {"id": 3, "tanggal": "2026-09-02", "kota": "Bandung", "total": 95000},
    {"id": 4, "tanggal": "2026-09-02", "kota": "Depok", "total": 150000},
    {"id": 5, "tanggal": "2026-09-03", "kota": "Bogor", "total": 110000},
    {"id": 6, "tanggal": "2026-09-03", "kota": "Bandung", "total": 130000},
]

KOLOM = {nama: [b[nama] for b in BARIS] for nama in BARIS[0]}


def jumlah_baris(baris_baris, kota=None):
    total, sentuh = 0, 0
    for b in baris_baris:
        sentuh += len(b)
        if kota is None or b["kota"] == kota:
            total += b["total"]
    return total, sentuh


def jumlah_kolom(kolom, kota=None):
    total, sentuh = 0, 0
    if kota is None:
        for nilai in kolom["total"]:
            sentuh += 1
            total += nilai
        return total, sentuh
    for i, k in enumerate(kolom["kota"]):
        sentuh += 1
        if k == kota:
            sentuh += 1
            total += kolom["total"][i]
    return total, sentuh


for judul, kota in [("SUM(total)", None),
                    ("SUM(total) WHERE kota = Bandung", "Bandung")]:
    tb, sb = jumlah_baris(BARIS, kota)
    tk, sk = jumlah_kolom(KOLOM, kota)
    print(judul)
    print(f"  baris: total {tb}, nilai disentuh {sb}")
    print(f"  kolom: total {tk}, nilai disentuh {sk}")
    print(f"  hemat {sb - sk} dari {sb} sentuhan")
""",
    },
    {
        "title": "Latihan 12: Rantai Kata Kerja ala dplyr",
        "difficulty": "Lanjut",
        "question": [
            "Tiru gaya pipeline dplyr di Python. Buat kelas Tabel yang",
            "membungkus list of dict, dengan metode yang bisa dirangkai:",
            "",
            "  - Tabel(baris, kelompok=None): simpan salinan list baris dan nama",
            "    kolom pengelompokan.",
            "  - filter(syarat): Tabel baru berisi baris yang syarat(baris)",
            "    bernilai True.",
            "  - mutate(**kolom_baru): Tabel baru; tiap baris disalin, lalu tiap",
            "    kolom baru diisi fungsi(baris). Data asli tidak boleh berubah.",
            "  - group_by(kolom): Tabel baru dengan baris yang sama, tapi",
            "    mengingat kolom pengelompokannya.",
            "  - summarise(**ringkasan): Tabel baru, satu baris per kelompok,",
            "    urut alfabetis menurut nilai kelompok (seperti dplyr). Tiap",
            "    baris dimulai kolom kelompok, lalu tiap ringkasan sesuai urutan",
            "    argumennya, diisi fungsi(list baris kelompok itu).",
            "  - cetak(): print tiap baris (dict) satu per baris.",
            "",
            "Pakai data dan pemakaian ini persis, lalu tambahkan satu baris yang",
            "mencetak nama kolom data asli untuk membuktikan data asli utuh:",
            "",
            "  PERJALANAN = [",
            "      {\"kota\": \"Jakarta\", \"jarak_km\": 12, \"tarif\": 3500, \"batal\": False},",
            "      {\"kota\": \"Bandung\", \"jarak_km\": 5, \"tarif\": 3000, \"batal\": False},",
            "      {\"kota\": \"Bandung\", \"jarak_km\": 8, \"tarif\": 3000, \"batal\": True},",
            "      {\"kota\": \"Surabaya\", \"jarak_km\": 7, \"tarif\": 2800, \"batal\": False},",
            "      {\"kota\": \"Jakarta\", \"jarak_km\": 4, \"tarif\": 3500, \"batal\": False},",
            "      {\"kota\": \"Bandung\", \"jarak_km\": 10, \"tarif\": 3000, \"batal\": False},",
            "      {\"kota\": \"Surabaya\", \"jarak_km\": 3, \"tarif\": 2800, \"batal\": True},",
            "  ]",
            "",
            "  hasil = (",
            "      Tabel(PERJALANAN)",
            "      .filter(lambda b: not b[\"batal\"])",
            "      .mutate(ongkos=lambda b: b[\"jarak_km\"] * b[\"tarif\"])",
            "      .group_by(\"kota\")",
            "      .summarise(",
            "          perjalanan=len,",
            "          total_ongkos=lambda g: sum(b[\"ongkos\"] for b in g),",
            "          jarak_terjauh=lambda g: max(b[\"jarak_km\"] for b in g),",
            "      )",
            "  )",
            "  hasil.cetak()",
            "  print(\"kolom data asli:\", list(PERJALANAN[0]))",
            "",
            "Keluaran yang diharapkan:",
            "{'kota': 'Bandung', 'perjalanan': 2, 'total_ongkos': 45000, 'jarak_terjauh': 10}",
            "{'kota': 'Jakarta', 'perjalanan': 2, 'total_ongkos': 56000, 'jarak_terjauh': 12}",
            "{'kota': 'Surabaya', 'perjalanan': 1, 'total_ongkos': 19600, 'jarak_terjauh': 7}",
            "kolom data asli: ['kota', 'jarak_km', 'tarif', 'batal']",
        ],
        "hints": [
            "Rangkaian bisa terjadi karena tiap metode mengembalikan objek Tabel baru, sehingga titik berikutnya memanggil metode pada hasil langkah sebelumnya.",
            "Supaya data asli utuh, mutate harus bekerja pada dict(b), salinan tiap baris, bukan pada b itu sendiri.",
            "Di summarise, kumpulkan baris per nilai kelompok dengan dict.setdefault(kunci, []).append(baris), lalu telusuri sorted() dari kunci-kuncinya.",
            "**ringkasan adalah dict yang menjaga urutan argumen, jadi ringkasan.items() memberi pasangan nama dan fungsi sesuai urutan ditulis.",
        ],
        "solution": """PERJALANAN = [
    {"kota": "Jakarta", "jarak_km": 12, "tarif": 3500, "batal": False},
    {"kota": "Bandung", "jarak_km": 5, "tarif": 3000, "batal": False},
    {"kota": "Bandung", "jarak_km": 8, "tarif": 3000, "batal": True},
    {"kota": "Surabaya", "jarak_km": 7, "tarif": 2800, "batal": False},
    {"kota": "Jakarta", "jarak_km": 4, "tarif": 3500, "batal": False},
    {"kota": "Bandung", "jarak_km": 10, "tarif": 3000, "batal": False},
    {"kota": "Surabaya", "jarak_km": 3, "tarif": 2800, "batal": True},
]


class Tabel:
    def __init__(self, baris, kelompok=None):
        self.baris = list(baris)
        self.kelompok = kelompok

    def filter(self, syarat):
        return Tabel([b for b in self.baris if syarat(b)], self.kelompok)

    def mutate(self, **kolom_baru):
        hasil = []
        for b in self.baris:
            baru = dict(b)
            for nama, fungsi in kolom_baru.items():
                baru[nama] = fungsi(baru)
            hasil.append(baru)
        return Tabel(hasil, self.kelompok)

    def group_by(self, kolom):
        return Tabel(self.baris, kolom)

    def summarise(self, **ringkasan):
        grup = {}
        for b in self.baris:
            grup.setdefault(b[self.kelompok], []).append(b)
        hasil = []
        for kunci in sorted(grup):
            satu = {self.kelompok: kunci}
            for nama, fungsi in ringkasan.items():
                satu[nama] = fungsi(grup[kunci])
            hasil.append(satu)
        return Tabel(hasil)

    def cetak(self):
        for b in self.baris:
            print(b)


hasil = (
    Tabel(PERJALANAN)
    .filter(lambda b: not b["batal"])
    .mutate(ongkos=lambda b: b["jarak_km"] * b["tarif"])
    .group_by("kota")
    .summarise(
        perjalanan=len,
        total_ongkos=lambda g: sum(b["ongkos"] for b in g),
        jarak_terjauh=lambda g: max(b["jarak_km"] for b in g),
    )
)
hasil.cetak()
print("kolom data asli:", list(PERJALANAN[0]))
""",
    },
    {
        "title": "Latihan 13: Pipeline CSV ke SQLite yang Idempoten",
        "difficulty": "Lanjut",
        "question": [
            "Daftar produk dikirim mitra sebagai CSV yang agak kotor. Tulis",
            "fungsi pipeline() yang membaca CSV itu dengan csv.DictReader dari",
            "io.StringIO, membersihkannya, lalu memuatnya ke tabel produk di",
            "database sqlite3 \":memory:\" yang dibuat SEKALI di awal program:",
            "",
            "  CREATE TABLE produk (kode TEXT PRIMARY KEY, nama TEXT, harga INTEGER)",
            "",
            "Aturan pembersihan:",
            "  - kode: buang spasi di tepi, jadikan huruf besar.",
            "  - nama: buang spasi di tepi, jadikan Huruf Awal Kapital",
            "    (str.title()). Baris dengan nama kosong dilewati dan dihitung.",
            "  - harga: buang spasi, jadikan int.",
            "  - Kode yang muncul dua kali: baris yang belakangan menang.",
            "",
            "Muat dengan upsert (INSERT ... ON CONFLICT(kode) DO UPDATE) di",
            "dalam satu transaksi, dan kembalikan jumlah baris yang dilewati.",
            "Jalankan pipeline DUA KALI dengan CSV yang sama. Sesudah tiap",
            "jalan, cetak jumlah baris di tabel. Terakhir, cetak isi tabel urut",
            "menurut kode.",
            "",
            "Datanya:",
            "",
            "  CSV_PRODUK = \"\"\"kode,nama,harga",
            "   K01 , kopi susu ,18000",
            "  K02,TEH TARIK,12000",
            "  k03,Roti Bakar , 15000",
            "  K02,Teh Tarik,13000",
            "  K04,,9000",
            "  \"\"\"",
            "",
            "Keluaran yang diharapkan:",
            "Jalan ke-1: 3 baris di tabel, 1 baris dilewati",
            "Jalan ke-2: 3 baris di tabel, 1 baris dilewati",
            "K01 | Kopi Susu | 18000",
            "K02 | Teh Tarik | 13000",
            "K03 | Roti Bakar | 15000",
        ],
        "hints": [
            "Pipeline idempoten memberi isi tabel yang sama berapa kali pun dijalankan, jadi kuncinya ada di cara memuat, bukan di cara membaca.",
            "Upsert menyelesaikan dua hal sekaligus: kode K02 yang muncul dua kali di CSV berakhir jadi satu baris, dan jalan kedua cuma memperbarui baris yang sudah ada.",
            "Di bagian DO UPDATE, nilai baru diakses lewat excluded, misalnya SET nama = excluded.nama, harga = excluded.harga.",
            "Bungkus semua INSERT dengan with db: supaya satu jalan pipeline jadi satu transaksi, dan buat io.StringIO baru di tiap pemanggilan karena StringIO yang sudah dibaca habis nggak bisa dibaca lagi.",
        ],
        "solution": "import csv\nimport io\nimport sqlite3\n\nCSV_PRODUK = \"\"\"kode,nama,harga\n K01 , kopi susu ,18000\nK02,TEH TARIK,12000\nk03,Roti Bakar , 15000\nK02,Teh Tarik,13000\nK04,,9000\n\"\"\"\n\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"CREATE TABLE produk (kode TEXT PRIMARY KEY, nama TEXT, harga INTEGER)\")\n\n\ndef pipeline():\n    dilewati = 0\n    with db:\n        for baris in csv.DictReader(io.StringIO(CSV_PRODUK)):\n            kode = baris[\"kode\"].strip().upper()\n            nama = baris[\"nama\"].strip().title()\n            if not nama:\n                dilewati += 1\n                continue\n            harga = int(baris[\"harga\"].strip())\n            db.execute(\n                \"INSERT INTO produk (kode, nama, harga) VALUES (?, ?, ?) \"\n                \"ON CONFLICT(kode) DO UPDATE SET nama = excluded.nama, \"\n                \"harga = excluded.harga\",\n                (kode, nama, harga),\n            )\n    return dilewati\n\n\nfor ke in (1, 2):\n    dilewati = pipeline()\n    jumlah = db.execute(\"SELECT COUNT(*) FROM produk\").fetchone()[0]\n    print(f\"Jalan ke-{ke}: {jumlah} baris di tabel, {dilewati} baris dilewati\")\n\nfor kode, nama, harga in db.execute(\"SELECT * FROM produk ORDER BY kode\"):\n    print(f\"{kode} | {nama} | {harga}\")\n",
    },
    {
        "title": "Latihan 14: Validator Kualitas Data",
        "difficulty": "Lanjut",
        "question": [
            "Tulis validator kualitas data untuk tabel pelanggan di bawah. Ada",
            "lima aturan, diperiksa dan dicetak dengan urutan ini:",
            "",
            "  1. not_null(nama): kolom nama tidak boleh None atau string kosong.",
            "  2. not_null(email): sama, untuk kolom email.",
            "  3. unique(id): sebutkan nilai id yang muncul lebih dari sekali",
            "     (sekali saja per nilai, urut).",
            "  4. rentang(umur,17,100): umur harus 17 sampai 100, ujung ikut.",
            "  5. format_email(email): email yang tidak None harus cocok dengan",
            "     pola ^[^@\\s]+@[^@\\s]+\\.[A-Za-z]{2,}$ (pakai modul re).",
            "",
            "Untuk aturan yang gagal, sebutkan id baris yang melanggar sesuai",
            "urutan data, dipisah koma dan spasi. Nama aturan dicetak rata kiri",
            "selebar 22 karakter. Akhiri dengan baris ringkasan.",
            "",
            "Datanya:",
            "",
            "  PELANGGAN = [",
            "      {\"id\": \"C01\", \"nama\": \"Ani\", \"email\": \"ani@contoh.id\", \"umur\": 25},",
            "      {\"id\": \"C02\", \"nama\": \"Budi\", \"email\": None, \"umur\": 31},",
            "      {\"id\": \"C03\", \"nama\": \"Citra\", \"email\": \"citra@contoh\", \"umur\": 19},",
            "      {\"id\": \"C04\", \"nama\": \"Dodi\", \"email\": \"dodi@contoh.id\", \"umur\": 15},",
            "      {\"id\": \"C05\", \"nama\": \"Eka\", \"email\": \"eka@contoh.id\", \"umur\": 40},",
            "      {\"id\": \"C05\", \"nama\": \"Eko\", \"email\": \"eko@contoh.id\", \"umur\": 38},",
            "      {\"id\": \"C06\", \"nama\": \"Fajar\", \"email\": \"fajar@contoh.co.id\", \"umur\": 52},",
            "  ]",
            "",
            "Keluaran yang diharapkan:",
            "not_null(nama)        LULUS",
            "not_null(email)       GAGAL -> C02",
            "unique(id)            GAGAL -> C05",
            "rentang(umur,17,100)  GAGAL -> C04",
            "format_email(email)   GAGAL -> C03",
            "Ringkasan: 1 lulus, 4 gagal",
        ],
        "hints": [
            "Tiap aturan bisa dibuat sebagai fungsi yang mengembalikan daftar pelanggaran; daftar kosong berarti lulus.",
            "Untuk unique, telusuri data sambil menyimpan id yang sudah pernah dilihat di sebuah set, dan masukkan id ke set kembar kalau ia sudah ada di set pertama.",
            "Email None dilewati oleh format_email karena sudah ditangkap not_null, jadi satu masalah nggak dilaporkan dua kali.",
            "Format barisnya f\"{nama:<22}LULUS\" atau f\"{nama:<22}GAGAL -> \" diikuti \", \".join(daftar_id).",
        ],
        "solution": "import re\n\nPELANGGAN = [\n    {\"id\": \"C01\", \"nama\": \"Ani\", \"email\": \"ani@contoh.id\", \"umur\": 25},\n    {\"id\": \"C02\", \"nama\": \"Budi\", \"email\": None, \"umur\": 31},\n    {\"id\": \"C03\", \"nama\": \"Citra\", \"email\": \"citra@contoh\", \"umur\": 19},\n    {\"id\": \"C04\", \"nama\": \"Dodi\", \"email\": \"dodi@contoh.id\", \"umur\": 15},\n    {\"id\": \"C05\", \"nama\": \"Eka\", \"email\": \"eka@contoh.id\", \"umur\": 40},\n    {\"id\": \"C05\", \"nama\": \"Eko\", \"email\": \"eko@contoh.id\", \"umur\": 38},\n    {\"id\": \"C06\", \"nama\": \"Fajar\", \"email\": \"fajar@contoh.co.id\", \"umur\": 52},\n]\n\nPOLA_EMAIL = re.compile(r\"^[^@\\s]+@[^@\\s]+\\.[A-Za-z]{2,}$\")\n\n\ndef not_null(kolom):\n    return [b[\"id\"] for b in PELANGGAN if b[kolom] in (None, \"\")]\n\n\ndef unique(kolom):\n    lihat, kembar = set(), set()\n    for b in PELANGGAN:\n        if b[kolom] in lihat:\n            kembar.add(b[kolom])\n        lihat.add(b[kolom])\n    return sorted(kembar)\n\n\ndef rentang(kolom, bawah, atas):\n    return [b[\"id\"] for b in PELANGGAN if not bawah <= b[kolom] <= atas]\n\n\ndef format_email(kolom):\n    return [b[\"id\"] for b in PELANGGAN\n            if b[kolom] is not None and not POLA_EMAIL.match(b[kolom])]\n\n\nATURAN = [\n    (\"not_null(nama)\", not_null(\"nama\")),\n    (\"not_null(email)\", not_null(\"email\")),\n    (\"unique(id)\", unique(\"id\")),\n    (\"rentang(umur,17,100)\", rentang(\"umur\", 17, 100)),\n    (\"format_email(email)\", format_email(\"email\")),\n]\n\nlulus = 0\nfor nama, gagal in ATURAN:\n    if gagal:\n        print(f\"{nama:<22}GAGAL -> {', '.join(gagal)}\")\n    else:\n        lulus += 1\n        print(f\"{nama:<22}LULUS\")\nprint(f\"Ringkasan: {lulus} lulus, {len(ATURAN) - lulus} gagal\")\n",
    },
    {
        "title": "Latihan 15: Penjadwal DAG dengan graphlib",
        "difficulty": "Lanjut",
        "question": [
            "Tulis penjadwal mini yang menjalankan task sesuai urutan DAG dan",
            "mencoba ulang task yang gagal, seperti scheduler Airflow.",
            "",
            "Bagian setup sudah menyiapkan:",
            "  - dag: dict nama task -> daftar task yang harus selesai dulu.",
            "  - MAKS_COBA = 3, batas percobaan per task.",
            "  - jalankan(nama): mengembalikan True kalau task berhasil.",
            "    bersihkan_pesanan sengaja gagal di percobaan pertama.",
            "",
            "Aturannya:",
            "  1. Pakai graphlib.TopologicalSorter dengan prepare(), get_ready(),",
            "     dan done(). Tiap putaran get_ready() adalah satu gelombang.",
            "  2. Di dalam satu gelombang, jalankan task urut alfabet.",
            "  3. Panggil jalankan() sampai berhasil, paling banyak MAKS_COBA",
            "     kali, dan cetak tiap percobaan.",
            "  4. Di akhir, cetak jumlah task dan jumlah seluruh percobaan.",
            "",
            "Keluaran yang diharapkan:",
            "gelombang 1: ekstrak_pelanggan, ekstrak_pesanan",
            "  ekstrak_pelanggan percobaan 1: sukses",
            "  ekstrak_pesanan percobaan 1: sukses",
            "gelombang 2: bersihkan_pesanan",
            "  bersihkan_pesanan percobaan 1: gagal, coba lagi",
            "  bersihkan_pesanan percobaan 2: sukses",
            "gelombang 3: gabung",
            "  gabung percobaan 1: sukses",
            "gelombang 4: muat_gudang",
            "  muat_gudang percobaan 1: sukses",
            "gelombang 5: kirim_laporan",
            "  kirim_laporan percobaan 1: sukses",
            "selesai: 6 task, 7 percobaan",
        ],
        "hints": [
            "Sebuah task baru boleh jalan kalau semua task yang ditunggunya sudah ditandai selesai, dan TopologicalSorter menyimpan catatan itu untukmu.",
            "Ulangi selama ts.is_active() bernilai True, ambil task yang siap, urutkan, coba tiap task dengan for coba in range(1, MAKS_COBA + 1), lalu panggil ts.done(nama).",
            "Di dalam loop percobaan, naikkan penghitung percobaan, lalu pakai if jalankan(nama): cetak sukses dan break; kalau nggak, cetak gagal, coba lagi.",
        ],
        "setup": "# Disiapkan: DAG, batas percobaan, dan fungsi yang \"menjalankan\" task.\ndag = {\n    \"ekstrak_pesanan\": [],\n    \"ekstrak_pelanggan\": [],\n    \"bersihkan_pesanan\": [\"ekstrak_pesanan\"],\n    \"gabung\": [\"bersihkan_pesanan\", \"ekstrak_pelanggan\"],\n    \"muat_gudang\": [\"gabung\"],\n    \"kirim_laporan\": [\"muat_gudang\"],\n}\nMAKS_COBA = 3\n_sudah_gagal = set()\n\n\ndef jalankan(task):\n    \"\"\"True kalau task berhasil. bersihkan_pesanan gagal di percobaan pertama.\"\"\"\n    if task == \"bersihkan_pesanan\" and task not in _sudah_gagal:\n        _sudah_gagal.add(task)\n        return False\n    return True",
        "solution": """from graphlib import TopologicalSorter

ts = TopologicalSorter(dag)
ts.prepare()
gelombang = 0
percobaan = 0
selesai = 0
while ts.is_active():
    siap = sorted(ts.get_ready())
    gelombang += 1
    print(f"gelombang {gelombang}: {', '.join(siap)}")
    for nama in siap:
        for coba in range(1, MAKS_COBA + 1):
            percobaan += 1
            if jalankan(nama):
                print(f"  {nama} percobaan {coba}: sukses")
                break
            print(f"  {nama} percobaan {coba}: gagal, coba lagi")
        ts.done(nama)
        selesai += 1
print(f"selesai: {selesai} task, {percobaan} percobaan")""",
    },
    {
        "title": "Latihan 16: Model dbt Mini di SQLite",
        "difficulty": "Lanjut",
        "question": [
            "Tiru cara dbt membangun model: cari ref() di tiap model, susun",
            "urutannya, ganti ref() dengan nama tabel, lalu jalankan ke SQLite.",
            "",
            "Bagian setup sudah menyiapkan db (sqlite3 di memori berisi tabel",
            "raw_pesanan dan raw_pelanggan) dan models, dict nama model ->",
            "isi berkas .sql. Rujukan antarmodel ditulis {{ ref('nama') }}.",
            "",
            "Aturannya:",
            "  1. Temukan semua ref di tiap model dengan regex.",
            "  2. Susun urutan dengan graphlib.TopologicalSorter. Kalau ada",
            "     beberapa model yang sama-sama siap, dahulukan urut alfabet.",
            "  3. Untuk tiap model sesuai urutan, ganti {{ ref('x') }} jadi x,",
            "     lalu jalankan CREATE TABLE nama AS <sql>.",
            "  4. Cetak SQL kota_teratas yang sudah dikompilasi dalam satu baris",
            "     (spasi berlebih dirapikan), isi omzet_per_kota urut nama kota,",
            "     dan isi kota_teratas.",
            "",
            "Keluaran yang diharapkan:",
            "urutan: stg_pelanggan, stg_pesanan, omzet_per_kota, kota_teratas",
            "kota_teratas dikompilasi:",
            "  SELECT kota, omzet FROM omzet_per_kota ORDER BY omzet DESC LIMIT 1",
            "omzet_per_kota:",
            "  Bandung     2    70000",
            "  Medan       1    30000",
            "  Surabaya    2   165000",
            "kota_teratas: Surabaya 165000",
        ],
        "hints": [
            "Model yang di-ref harus sudah jadi tabel sebelum model yang memakainya dijalankan, jadi ref adalah daftar ketergantungan sebuah model.",
            "Buat dict nama -> daftar ref dengan re.findall, susun urutannya lewat prepare(), get_ready() yang di-sorted, dan done(), lalu ganti ref dengan re.sub sebelum CREATE TABLE.",
            "Pola regex yang cocok untuk ref adalah r\"\\{\\{\\s*ref\\('(\\w+)'\\)\\s*\\}\\}\", dan \" \".join(sql.split()) merapikan spasinya.",
        ],
        "setup": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.executescript(\"\"\"\nCREATE TABLE raw_pesanan (id INTEGER, id_pelanggan INTEGER,\n                          jumlah INTEGER, status TEXT);\nINSERT INTO raw_pesanan VALUES\n  (1, 10, 50000, 'selesai'), (2, 11, 75000, 'batal'),\n  (3, 10, 20000, 'selesai'), (4, 12, 120000, 'selesai'),\n  (5, 11, 30000, 'selesai'), (6, 12, 45000, 'selesai');\nCREATE TABLE raw_pelanggan (id INTEGER, nama TEXT, kota TEXT);\nINSERT INTO raw_pelanggan VALUES\n  (10, 'Ani', 'Bandung'), (11, 'Budi', 'Medan'), (12, 'Citra', 'Surabaya');\n\"\"\")\n\n# nama model -> isi berkas .sql; urutannya sengaja acak\nmodels = {\n    \"kota_teratas\": \"\"\"\n        SELECT kota, omzet FROM {{ ref('omzet_per_kota') }}\n        ORDER BY omzet DESC LIMIT 1\n    \"\"\",\n    \"omzet_per_kota\": \"\"\"\n        SELECT c.kota, COUNT(*) AS pesanan, SUM(p.jumlah) AS omzet\n        FROM {{ ref('stg_pesanan') }} AS p\n        JOIN {{ ref('stg_pelanggan') }} AS c\n          ON c.id_pelanggan = p.id_pelanggan\n        GROUP BY c.kota\n    \"\"\",\n    \"stg_pesanan\": \"\"\"\n        SELECT id AS id_pesanan, id_pelanggan, jumlah\n        FROM raw_pesanan WHERE status = 'selesai'\n    \"\"\",\n    \"stg_pelanggan\": \"\"\"\n        SELECT id AS id_pelanggan, nama, kota FROM raw_pelanggan\n    \"\"\",\n}",
        "solution": "import re\nfrom graphlib import TopologicalSorter\n\nPOLA_REF = re.compile(r\"\\{\\{\\s*ref\\('(\\w+)'\\)\\s*\\}\\}\")\n\nbutuh = {nama: POLA_REF.findall(sql) for nama, sql in models.items()}\n\nts = TopologicalSorter(butuh)\nts.prepare()\nurutan = []\nwhile ts.is_active():\n    for nama in sorted(ts.get_ready()):\n        urutan.append(nama)\n        ts.done(nama)\nprint(\"urutan:\", \", \".join(urutan))\n\nfor nama in urutan:\n    sql = POLA_REF.sub(lambda m: m.group(1), models[nama])\n    db.execute(f\"CREATE TABLE {nama} AS {sql}\")\n    if nama == \"kota_teratas\":\n        print(nama, \"dikompilasi:\")\n        print(\"  \" + \" \".join(sql.split()))\n\nprint(\"omzet_per_kota:\")\nfor kota, pesanan, omzet in db.execute(\n        \"SELECT kota, pesanan, omzet FROM omzet_per_kota ORDER BY kota\"):\n    print(f\"  {kota:<10}{pesanan:>3}{omzet:>9}\")\nkota, omzet = db.execute(\"SELECT kota, omzet FROM kota_teratas\").fetchone()\nprint(f\"kota_teratas: {kota} {omzet}\")",
    },
    {
        "title": "Latihan 17: MapReduce Hitung Kata",
        "difficulty": "Lanjut",
        "question": [
            "Hitung kata dengan pola MapReduce: map, shuffle, lalu reduce.",
            "",
            "Bagian setup sudah menyiapkan dokumen, list berisi tiga kalimat yang",
            "anggap saja tersebar di tiga mesin.",
            "",
            "Aturannya:",
            "  1. Map: dari tiap dokumen, ambil kata dengan",
            "     re.findall(r\"[a-z]+\", teks.lower()) dan hasilkan pasangan",
            "     (kata, 1). Cetak banyaknya pasangan per dokumen.",
            "  2. Shuffle: kumpulkan pasangan dari semua dokumen per kata. Cetak",
            "     banyaknya kata unik.",
            "  3. Reduce: jumlahkan nilai tiap kata.",
            "  4. Cetak 5 kata terbanyak. Kalau jumlahnya sama, urutkan menurut",
            "     abjad. Kata ditulis rata kiri selebar 12 karakter.",
            "",
            "Keluaran yang diharapkan:",
            "map dokumen 0: 8 pasangan",
            "map dokumen 1: 11 pasangan",
            "map dokumen 2: 7 pasangan",
            "shuffle: 16 kata unik",
            "5 kata terbanyak:",
            "  data        5",
            "  kotor       3",
            "  waktu       3",
            "  itu         2",
            "  yang        2",
        ],
        "hints": [
            "Tiga tahap ini sengaja dipisah supaya map bisa jalan di tiap mesin, sedangkan shuffle adalah satu-satunya tahap yang menggabungkan data dari semua mesin.",
            "Tulis tiga fungsi: tahap_map mengembalikan list pasangan, tahap_shuffle mengisi defaultdict(list) per kata, dan tahap_reduce menjumlahkan list tiap kata.",
            "Urutan jumlah turun lalu abjad didapat dengan sorted(jumlah.items(), key=lambda p: (-p[1], p[0]))[:5].",
        ],
        "setup": """# Disiapkan: tiga "dokumen" yang tersebar di tiga mesin.
dokumen = [
    "Data bersih itu murah. Data kotor itu mahal.",
    "Pipeline data yang rapi menghemat waktu, data yang kotor menghabiskan waktu.",
    "Waktu analis habis untuk membersihkan data kotor.",
]""",
        "solution": """import re
from collections import defaultdict


def tahap_map(teks):
    return [(kata, 1) for kata in re.findall(r"[a-z]+", teks.lower())]


def tahap_shuffle(semua_pasangan):
    kelompok = defaultdict(list)
    for pasangan in semua_pasangan:
        for kata, satu in pasangan:
            kelompok[kata].append(satu)
    return kelompok


def tahap_reduce(kelompok):
    return {kata: sum(nilai) for kata, nilai in kelompok.items()}


hasil_map = [tahap_map(d) for d in dokumen]
for i, pasangan in enumerate(hasil_map):
    print(f"map dokumen {i}: {len(pasangan)} pasangan")
kelompok = tahap_shuffle(hasil_map)
print(f"shuffle: {len(kelompok)} kata unik")
jumlah = tahap_reduce(kelompok)
teratas = sorted(jumlah.items(), key=lambda p: (-p[1], p[0]))[:5]
print("5 kata terbanyak:")
for kata, n in teratas:
    print(f"  {kata:<12}{n}")""",
    },
    {
        "title": "Latihan 18: Log Kafka Mini dengan Offset",
        "difficulty": "Lanjut",
        "question": [
            "Buat kelas Topik yang meniru satu partisi Kafka: log append-only dan",
            "offset yang disimpan terpisah untuk tiap consumer group.",
            "",
            "Method yang dibutuhkan:",
            "  - kirim(pesan): tambah pesan di ujung log.",
            "  - baca(grup, maks): cetak paling banyak maks pesan mulai dari",
            "    offset grup itu (grup baru mulai dari 0), dengan format",
            "    [grup] offset N: pesan. Sesudah membaca, simpan offset",
            "    berikutnya sebagai offset grup.",
            "  - seek(grup, offset): cetak [grup] mundur ke offset N, lalu ubah",
            "    offset grup itu.",
            "",
            "Lalu jalankan skenario ini berurutan:",
            "  1. Buat topik pesanan dan kirim: #1 dibuat, #1 dibayar, #2 dibuat,",
            "     #1 dikirim, #2 dibayar.",
            "  2. Grup gudang membaca maks 3, grup analitik membaca maks 10.",
            "  3. Kirim #3 dibuat dan #2 dikirim, lalu gudang membaca maks 10.",
            "  4. Analitik mundur ke offset 1 dan membaca maks 2.",
            "  5. Cetak dict offset dan banyaknya pesan di log.",
            "",
            "Keluaran yang diharapkan:",
            "[gudang] offset 0: #1 dibuat",
            "[gudang] offset 1: #1 dibayar",
            "[gudang] offset 2: #2 dibuat",
            "[analitik] offset 0: #1 dibuat",
            "[analitik] offset 1: #1 dibayar",
            "[analitik] offset 2: #2 dibuat",
            "[analitik] offset 3: #1 dikirim",
            "[analitik] offset 4: #2 dibayar",
            "[gudang] offset 3: #1 dikirim",
            "[gudang] offset 4: #2 dibayar",
            "[gudang] offset 5: #3 dibuat",
            "[gudang] offset 6: #2 dikirim",
            "[analitik] mundur ke offset 1",
            "[analitik] offset 1: #1 dibayar",
            "[analitik] offset 2: #2 dibuat",
            "offset tersimpan: {'gudang': 7, 'analitik': 3}",
            "isi log: 7 pesan",
        ],
        "hints": [
            "Membaca nggak menghapus pesan dari log, jadi yang membedakan dua grup cuma angka offset yang disimpan masing-masing.",
            "Simpan log sebagai list dan offset sebagai dict grup -> angka, lalu di baca() hitung mulai dengan self.offset.get(grup, 0) dan akhir dengan min(mulai + maks, len(self.log)).",
            "Sesudah loop di baca(), tulis self.offset[grup] = akhir, dan seek() cukup mencetak pesannya lalu menimpa self.offset[grup].",
        ],
        "solution": "class Topik:\n    \"\"\"Log append-only dengan offset terpisah untuk tiap consumer group.\"\"\"\n\n    def __init__(self, nama):\n        self.nama = nama\n        self.log = []\n        self.offset = {}\n\n    def kirim(self, pesan):\n        self.log.append(pesan)\n        return len(self.log) - 1\n\n    def baca(self, grup, maks):\n        mulai = self.offset.get(grup, 0)\n        akhir = min(mulai + maks, len(self.log))\n        for i in range(mulai, akhir):\n            print(f\"[{grup}] offset {i}: {self.log[i]}\")\n        self.offset[grup] = akhir  # commit sesudah membaca\n        return akhir - mulai\n\n    def seek(self, grup, offset):\n        print(f\"[{grup}] mundur ke offset {offset}\")\n        self.offset[grup] = offset\n\n\npesanan = Topik(\"pesanan\")\nfor p in [\"#1 dibuat\", \"#1 dibayar\", \"#2 dibuat\", \"#1 dikirim\", \"#2 dibayar\"]:\n    pesanan.kirim(p)\n\npesanan.baca(\"gudang\", 3)\npesanan.baca(\"analitik\", 10)\npesanan.kirim(\"#3 dibuat\")\npesanan.kirim(\"#2 dikirim\")\npesanan.baca(\"gudang\", 10)\npesanan.seek(\"analitik\", 1)\npesanan.baca(\"analitik\", 2)\nprint(\"offset tersimpan:\", pesanan.offset)\nprint(\"isi log:\", len(pesanan.log), \"pesan\")",
    },
    {
        "title": "Latihan 19: Tabel Lakehouse Mini dengan Time Travel",
        "difficulty": "Sulit",
        "question": [
            "Buat kelas TabelLakehouse yang meniru cara kerja Iceberg dan Delta",
            "Lake: berkas data nggak pernah diubah, dan tiap operasi membuat",
            "snapshot baru berisi daftar berkas yang membentuk tabel.",
            "",
            "Isi kelasnya:",
            "  - berkas: dict nama berkas -> list baris. Nama berkas baru",
            "    data-001, data-002, dan seterusnya, mengikuti banyaknya berkas",
            "    yang pernah ditulis.",
            "  - snapshot: dict id -> (operasi, daftar nama berkas). Id mulai 1.",
            "    Tiap commit mencetak snapshot N: operasi -> daftar berkas, dengan",
            "    operasi rata kiri selebar 6.",
            "  - tambah(baris): tulis satu berkas baru, lalu commit daftar lama",
            "    ditambah berkas itu.",
            "  - hapus(syarat): untuk tiap berkas di snapshot terbaru, buang baris",
            "    yang memenuhi syarat. Berkas yang nggak berubah tetap dipakai di",
            "    posisinya. Berkas yang berubah ditulis ulang jadi berkas baru di",
            "    posisi yang sama, dan berkas yang jadi kosong dibuang.",
            "  - baca(id_snapshot=None): semua baris snapshot itu (bawaannya yang",
            "    terbaru), diurutkan. Snapshot yang nggak ada memicu KeyError.",
            "  - kedaluwarsakan(sebelum): hapus snapshot dengan id lebih kecil",
            "    dari sebelum, lalu hapus berkas yang nggak dipakai snapshot mana",
            "    pun, dan cetak namanya.",
            "",
            "Jalankan skenario ini: tambah Ani dan Budi, tambah Citra, hapus",
            "baris berid 2, tambah Dedi. Cetak isi terbaru, snapshot 2, snapshot",
            "1, dan banyaknya berkas. Lalu kedaluwarsakan sebelum snapshot 3,",
            "coba baca snapshot 1, dan cetak banyaknya baris terbaru.",
            "",
            "Data barisnya: (1, \"Ani\", 50000), (2, \"Budi\", 75000),",
            "(3, \"Citra\", 120000), dan (4, \"Dedi\", 30000).",
            "",
            "Keluaran yang diharapkan:",
            "snapshot 1: tambah -> data-001",
            "snapshot 2: tambah -> data-001, data-002",
            "snapshot 3: hapus  -> data-003, data-002",
            "snapshot 4: tambah -> data-003, data-002, data-004",
            "terbaru: [(1, 'Ani', 50000), (3, 'Citra', 120000), (4, 'Dedi', 30000)]",
            "snapshot 2: [(1, 'Ani', 50000), (2, 'Budi', 75000), (3, 'Citra', 120000)]",
            "snapshot 1: [(1, 'Ani', 50000), (2, 'Budi', 75000)]",
            "berkas tersimpan: 4",
            "berkas dihapus: data-001",
            "snapshot 1 sudah kedaluwarsa",
            "terbaru masih utuh: 3 baris",
        ],
        "hints": [
            "Time travel berhasil karena berkas lama nggak pernah ditimpa: snapshot lama tetap menunjuk berkas yang sama, dan cuma snapshot baru yang menunjuk berkas hasil tulis ulang.",
            "Simpan snapshot sebagai (operasi, list nama berkas), ambil daftar terbaru dari self.snapshot[self.terakhir], dan di hapus() bandingkan panjang isi berkas sebelum dan sesudah disaring untuk tahu berkas mana yang perlu ditulis ulang.",
            "Untuk kedaluwarsa, kumpulkan dulu himpunan berkas yang masih dipakai dengan {n for _, daftar in self.snapshot.values() for n in daftar}, lalu hapus berkas di luar himpunan itu.",
        ],
        "solution": "class TabelLakehouse:\n    \"\"\"Tabel = daftar berkas per snapshot. Berkas data nggak pernah diubah.\"\"\"\n\n    def __init__(self):\n        self.berkas = {}      # nama berkas -> list baris\n        self.snapshot = {}    # id snapshot -> (operasi, list nama berkas)\n        self.terakhir = 0\n\n    def _tulis_berkas(self, baris):\n        nama = f\"data-{len(self.berkas) + 1:03d}\"\n        self.berkas[nama] = list(baris)\n        return nama\n\n    def _commit(self, operasi, daftar):\n        self.terakhir += 1\n        self.snapshot[self.terakhir] = (operasi, daftar)\n        print(f\"snapshot {self.terakhir}: {operasi:<6} -> {', '.join(daftar)}\")\n\n    def _daftar_kini(self):\n        return list(self.snapshot[self.terakhir][1]) if self.terakhir else []\n\n    def tambah(self, baris):\n        self._commit(\"tambah\", self._daftar_kini() + [self._tulis_berkas(baris)])\n\n    def hapus(self, syarat):\n        baru = []\n        for nama in self._daftar_kini():\n            isi = self.berkas[nama]\n            sisa = [b for b in isi if not syarat(b)]\n            if len(sisa) == len(isi):\n                baru.append(nama)                     # berkas nggak tersentuh\n            elif sisa:\n                baru.append(self._tulis_berkas(sisa))  # tulis ulang tanpa baris itu\n        self._commit(\"hapus\", baru)\n\n    def baca(self, id_snapshot=None):\n        id_snapshot = id_snapshot or self.terakhir\n        if id_snapshot not in self.snapshot:\n            raise KeyError(id_snapshot)\n        daftar = self.snapshot[id_snapshot][1]\n        return sorted(b for nama in daftar for b in self.berkas[nama])\n\n    def kedaluwarsakan(self, sebelum):\n        for i in [i for i in self.snapshot if i < sebelum]:\n            del self.snapshot[i]\n        dipakai = {n for _, daftar in self.snapshot.values() for n in daftar}\n        dibuang = sorted(n for n in self.berkas if n not in dipakai)\n        for n in dibuang:\n            del self.berkas[n]\n        print(\"berkas dihapus:\", \", \".join(dibuang))\n\n\nt = TabelLakehouse()\nt.tambah([(1, \"Ani\", 50000), (2, \"Budi\", 75000)])\nt.tambah([(3, \"Citra\", 120000)])\nt.hapus(lambda b: b[0] == 2)\nt.tambah([(4, \"Dedi\", 30000)])\n\nprint(\"terbaru:\", t.baca())\nprint(\"snapshot 2:\", t.baca(2))\nprint(\"snapshot 1:\", t.baca(1))\nprint(\"berkas tersimpan:\", len(t.berkas))\n\nt.kedaluwarsakan(sebelum=3)\ntry:\n    t.baca(1)\nexcept KeyError:\n    print(\"snapshot 1 sudah kedaluwarsa\")\nprint(\"terbaru masih utuh:\", len(t.baca()), \"baris\")",
    },
    {
        "title": "Latihan 20: Measure dengan Konteks Filter",
        "difficulty": "Sulit",
        "question": [
            "Tiru cara Power BI menghitung measure di tabel matriks: satu fungsi",
            "yang sama dihitung ulang untuk tiap sel dengan filter sel itu.",
            "",
            "Bagian setup sudah menyiapkan penjualan (list dict berkunci wilayah,",
            "bulan, jumlah), WILAYAH, dan BULAN.",
            "",
            "Aturannya:",
            "  1. Tulis measure(filter_). filter_ adalah dict kolom -> nilai,",
            "     misalnya {\"wilayah\": \"Barat\", \"bulan\": \"Sep\"}. Hasilnya",
            "     jumlah kolom jumlah untuk baris yang cocok dengan semua filter.",
            "     Dict kosong artinya tanpa filter, seperti ALL di DAX.",
            "  2. Tulis persen(filter_) = measure(filter_) / measure({}).",
            "  3. Cetak matriks total: baris tiap wilayah lalu Semua, kolom tiap",
            "     bulan lalu Semua. Label baris rata kiri selebar 8, tiap angka",
            "     rata kanan selebar 7. Sel tanpa transaksi bernilai 0.",
            "  4. Cetak matriks persen dengan bentuk yang sama, format :>7.1%.",
            "",
            "Keluaran yang diharapkan:",
            "total       Agu    Sep    Okt  Semua",
            "Barat       120    150    130    400",
            "Tengah       80      0    110    190",
            "Timur        50    110     50    210",
            "Semua       250    260    290    800",
            "persen      Agu    Sep    Okt  Semua",
            "Barat     15.0%  18.8%  16.2%  50.0%",
            "Tengah    10.0%   0.0%  13.8%  23.8%",
            "Timur      6.2%  13.8%   6.2%  26.2%",
            "Semua     31.2%  32.5%  36.2% 100.0%",
        ],
        "hints": [
            "Sel matriks, total baris, total kolom, dan total keseluruhan semuanya hasil fungsi yang sama, yang membedakan cuma isi filternya.",
            "Bentuk filter tiap sel dengan menggabung dict, misalnya {**konteks, \"bulan\": b}, dengan konteks berisi {\"wilayah\": w} atau dict kosong untuk baris Semua.",
            "Di dalam measure, saring dengan all(b[k] == v for k, v in filter_.items()), lalu jumlahkan b[\"jumlah\"] dari baris yang lolos.",
        ],
        "setup": """# Disiapkan: tabel penjualan (satu dict per transaksi).
penjualan = [
    {"wilayah": "Barat", "bulan": "Agu", "jumlah": 120},
    {"wilayah": "Barat", "bulan": "Sep", "jumlah": 90},
    {"wilayah": "Barat", "bulan": "Sep", "jumlah": 60},
    {"wilayah": "Barat", "bulan": "Okt", "jumlah": 130},
    {"wilayah": "Tengah", "bulan": "Agu", "jumlah": 80},
    {"wilayah": "Tengah", "bulan": "Okt", "jumlah": 70},
    {"wilayah": "Tengah", "bulan": "Okt", "jumlah": 40},
    {"wilayah": "Timur", "bulan": "Agu", "jumlah": 50},
    {"wilayah": "Timur", "bulan": "Sep", "jumlah": 110},
    {"wilayah": "Timur", "bulan": "Okt", "jumlah": 50},
]
WILAYAH = ["Barat", "Tengah", "Timur"]
BULAN = ["Agu", "Sep", "Okt"]""",
        "solution": "def measure(filter_):\n    \"\"\"SUM(jumlah) di bawah konteks filter: dict kolom -> nilai.\"\"\"\n    return sum(b[\"jumlah\"] for b in penjualan\n               if all(b[k] == v for k, v in filter_.items()))\n\n\ndef persen(filter_):\n    \"\"\"DIVIDE(total di filter ini, total tanpa filter apa pun).\"\"\"\n    return measure(filter_) / measure({})\n\n\nprint(f\"{'total':8}\" + \"\".join(f\"{b:>7}\" for b in BULAN) + f\"{'Semua':>7}\")\nfor w in WILAYAH + [None]:\n    konteks = {\"wilayah\": w} if w else {}\n    sel = [measure({**konteks, \"bulan\": b}) for b in BULAN] + [measure(konteks)]\n    print(f\"{w or 'Semua':8}\" + \"\".join(f\"{x:>7}\" for x in sel))\n\nprint(f\"{'persen':8}\" + \"\".join(f\"{b:>7}\" for b in BULAN) + f\"{'Semua':>7}\")\nfor w in WILAYAH + [None]:\n    konteks = {\"wilayah\": w} if w else {}\n    sel = [persen({**konteks, \"bulan\": b}) for b in BULAN] + [persen(konteks)]\n    print(f\"{w or 'Semua':8}\" + \"\".join(f\"{x:>7.1%}\" for x in sel))",
    },
    {
        "title": "Latihan 21: Proyek Akhir: Laporan KPI Toko dari Data Mentah",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek ini menyatukan pembersihan data, star schema, SQL analitik,",
            "dan laporan KPI. Kamu menerima ekspor kasir yang masih kotor, lalu",
            "harus menghasilkan laporan bulanan yang bisa dipercaya.",
            "",
            "Bagian setup sudah menyiapkan CSV_MENTAH (io.StringIO berisi CSV",
            "berkolom id_transaksi, tanggal, produk, qty, harga) dan KATEGORI",
            "(dict nama produk -> kategori).",
            "",
            "Tahap 1, bersihkan. Baca dengan csv.DictReader dan strip semua",
            "nilai. Periksa tiap baris berurutan, alasan pertama yang cocok",
            "menang:",
            "  - id_transaksi yang sudah pernah muncul: karantina \"duplikat\".",
            "  - produk kosong: karantina \"produk kosong\".",
            "  - qty <= 0: karantina \"qty <= 0\".",
            "Baris yang lolos: tanggal DD/MM/YYYY diubah jadi YYYY-MM-DD, nama",
            "produk ditulis kapital tiap kata (\"kopi susu\" jadi \"Kopi Susu\"),",
            "harga dibuang \"Rp\", titik, dan spasinya lalu jadi int.",
            "",
            "Tahap 2, muat star schema ke sqlite3 di memori:",
            "  - dim_produk(id_produk, nama, kategori), id 1, 2, ... menurut",
            "    urutan abjad nama.",
            "  - dim_tanggal(id_tanggal, tanggal, bulan), id berbentuk 20260803,",
            "    bulan berbentuk 2026-08.",
            "  - fakta_penjualan(id_transaksi, id_produk, id_tanggal, qty, harga,",
            "    total), dengan total = qty x harga.",
            "",
            "Tahap 3, hitung KPI dengan SQL: per bulan omzet, transaksi,",
            "keranjang (omzet dibagi transaksi, pembagian bulat), dan",
            "pertumbuhan omzet terhadap bulan sebelumnya memakai window function",
            "LAG, dibulatkan satu desimal (bulan pertama ditulis -). Lalu produk",
            "terlaris menurut jumlah qty dan omzet per kategori.",
            "",
            "Tahap 4, validasi dengan query yang menghitung baris pelanggar:",
            "fk_lengkap (semua id_produk dan id_tanggal di fakta ada di",
            "dimensinya), id_unik, total_cocok, dan tanggal_rentang (semua",
            "tanggal di antara 2026-08-01 dan 2026-10-31). Nol pelanggar berarti",
            "lulus.",
            "",
            "Keluaran yang diharapkan:",
            "LAPORAN KPI TOKO",
            "pembersihan: 18 baris mentah, 14 bersih, 4 dikarantina",
            "  duplikat      2",
            "  produk kosong 1",
            "  qty <= 0      1",
            "bulan       omzet  transaksi  keranjang  tumbuh",
            "2026-08    100000          4      25000       -",
            "2026-09    166000          4      41500   66.0%",
            "2026-10    236000          6      39333   42.2%",
            "produk terlaris: Kopi Susu (10 porsi)",
            "omzet per kategori:",
            "  makanan   250000",
            "  minuman   252000",
            "validasi:",
            "  fk_lengkap        lulus",
            "  id_unik           lulus",
            "  total_cocok       lulus",
            "  tanggal_rentang   lulus",
        ],
        "hints": [
            "Kerjakan per tahap dan cetak hasil sementara tiap tahap, karena angka laporan cuma bisa benar kalau jumlah baris bersih dan isi dimensinya sudah benar lebih dulu.",
            "Simpan id_transaksi yang sudah terlihat di sebuah set sebelum memeriksa alasan lain, dan bangun dict nama produk -> id_produk dari sorted(set nama) supaya fakta bisa menunjuk dimensinya.",
            "Pertumbuhan bisa dihitung di SQL dengan ROUND((omzet - LAG(omzet) OVER (ORDER BY bulan)) * 100.0 / LAG(omzet) OVER (ORDER BY bulan), 1) di atas CTE yang menjumlahkan omzet per bulan.",
        ],
        "setup": "import io\n\n# Disiapkan: ekspor kasir mentah (masih kotor) dan kategori tiap produk.\nCSV_MENTAH = io.StringIO(\"\"\"id_transaksi,tanggal,produk,qty,harga\nT001,2026-08-03,kopi susu,2,Rp18.000\nT002,03/08/2026, Roti Bakar ,1,Rp15.000\nT003,2026-08-10,NASI GORENG,1,Rp 25.000\nT004,2026-08-17,teh manis,3,Rp8.000\nT004,2026-08-17,teh manis,3,Rp8.000\nT005,2026-08-24,kopi susu,0,Rp18.000\nT006,2026-09-02,Kopi Susu,3,Rp18.000\nT007,07/09/2026,roti bakar,2,Rp15.000\nT008,2026-09-14,nasi goreng,2,Rp25.000\nT009,2026-09-21,,1,Rp10.000\nT010,2026-09-28,teh manis ,4,Rp8.000\nT011,2026-10-01,kopi susu,4,Rp18.000\nT012,05/10/2026,nasi goreng,1,Rp25.000\nT013,2026-10-08,Roti Bakar,2,Rp15.000\nT014,2026-10-12,teh manis,2,Rp8.000\nT013,2026-10-08,Roti Bakar,2,Rp15.000\nT015,2026-10-15,kopi susu,1,Rp18.000\nT016,2026-10-18,nasi goreng,3,Rp25.000\n\"\"\")\nKATEGORI = {\"Kopi Susu\": \"minuman\", \"Teh Manis\": \"minuman\",\n            \"Roti Bakar\": \"makanan\", \"Nasi Goreng\": \"makanan\"}",
        "solution": "import csv\nimport sqlite3\n\n\ndef rapikan_tanggal(teks):\n    if \"/\" in teks:                      # 03/08/2026 -> 2026-08-03\n        hari, bulan, tahun = teks.split(\"/\")\n        return f\"{tahun}-{bulan}-{hari}\"\n    return teks\n\n\ndef bersihkan(sumber):\n    bersih, karantina, terlihat = [], {}, set()\n    mentah = list(csv.DictReader(sumber))\n    for r in mentah:\n        r = {k: v.strip() for k, v in r.items()}\n        if r[\"id_transaksi\"] in terlihat:\n            alasan = \"duplikat\"\n        elif not r[\"produk\"]:\n            alasan = \"produk kosong\"\n        elif int(r[\"qty\"]) <= 0:\n            alasan = \"qty <= 0\"\n        else:\n            alasan = None\n        terlihat.add(r[\"id_transaksi\"])\n        if alasan:\n            karantina[alasan] = karantina.get(alasan, 0) + 1\n            continue\n        bersih.append({\n            \"id\": r[\"id_transaksi\"],\n            \"tanggal\": rapikan_tanggal(r[\"tanggal\"]),\n            \"produk\": r[\"produk\"].lower().title(),\n            \"qty\": int(r[\"qty\"]),\n            \"harga\": int(r[\"harga\"].replace(\"Rp\", \"\").replace(\".\", \"\").strip()),\n        })\n    return len(mentah), bersih, karantina\n\n\ndef muat(db, baris):\n    db.executescript(\"\"\"\n    CREATE TABLE dim_produk (id_produk INTEGER PRIMARY KEY, nama TEXT,\n        kategori TEXT);\n    CREATE TABLE dim_tanggal (id_tanggal INTEGER PRIMARY KEY, tanggal TEXT,\n        bulan TEXT);\n    CREATE TABLE fakta_penjualan (id_transaksi TEXT PRIMARY KEY,\n        id_produk INTEGER, id_tanggal INTEGER, qty INTEGER, harga INTEGER,\n        total INTEGER);\n    \"\"\")\n    produk = sorted({b[\"produk\"] for b in baris})\n    db.executemany(\"INSERT INTO dim_produk VALUES (?, ?, ?)\",\n                   [(i, p, KATEGORI[p]) for i, p in enumerate(produk, 1)])\n    id_produk = {p: i for i, p in enumerate(produk, 1)}\n    tanggal = sorted({b[\"tanggal\"] for b in baris})\n    db.executemany(\"INSERT INTO dim_tanggal VALUES (?, ?, ?)\",\n                   [(int(t.replace(\"-\", \"\")), t, t[:7]) for t in tanggal])\n    db.executemany(\"INSERT INTO fakta_penjualan VALUES (?, ?, ?, ?, ?, ?)\", [\n        (b[\"id\"], id_produk[b[\"produk\"]], int(b[\"tanggal\"].replace(\"-\", \"\")),\n         b[\"qty\"], b[\"harga\"], b[\"qty\"] * b[\"harga\"]) for b in baris])\n\n\nKPI_BULANAN = \"\"\"\nWITH per_bulan AS (\n    SELECT t.bulan, SUM(f.total) AS omzet, COUNT(*) AS transaksi\n    FROM fakta_penjualan f JOIN dim_tanggal t ON t.id_tanggal = f.id_tanggal\n    GROUP BY t.bulan\n)\nSELECT bulan, omzet, transaksi, omzet / transaksi AS keranjang,\n       ROUND((omzet - LAG(omzet) OVER (ORDER BY bulan)) * 100.0\n             / LAG(omzet) OVER (ORDER BY bulan), 1) AS tumbuh\nFROM per_bulan ORDER BY bulan\n\"\"\"\n\nTERLARIS = \"\"\"\nSELECT p.nama, SUM(f.qty) AS porsi\nFROM fakta_penjualan f JOIN dim_produk p ON p.id_produk = f.id_produk\nGROUP BY p.nama ORDER BY porsi DESC, p.nama LIMIT 1\n\"\"\"\n\nPER_KATEGORI = \"\"\"\nSELECT p.kategori, SUM(f.total)\nFROM fakta_penjualan f JOIN dim_produk p ON p.id_produk = f.id_produk\nGROUP BY p.kategori ORDER BY p.kategori\n\"\"\"\n\nVALIDASI = {\n    \"fk_lengkap\": \"\"\"SELECT COUNT(*) FROM fakta_penjualan f\n        LEFT JOIN dim_produk p ON p.id_produk = f.id_produk\n        LEFT JOIN dim_tanggal t ON t.id_tanggal = f.id_tanggal\n        WHERE p.id_produk IS NULL OR t.id_tanggal IS NULL\"\"\",\n    \"id_unik\": \"\"\"SELECT COUNT(*) FROM (SELECT id_transaksi\n        FROM fakta_penjualan GROUP BY id_transaksi HAVING COUNT(*) > 1)\"\"\",\n    \"total_cocok\": \"\"\"SELECT COUNT(*) FROM fakta_penjualan\n        WHERE total != qty * harga\"\"\",\n    \"tanggal_rentang\": \"\"\"SELECT COUNT(*) FROM dim_tanggal\n        WHERE tanggal NOT BETWEEN '2026-08-01' AND '2026-10-31'\"\"\",\n}\n\nn_mentah, bersih, karantina = bersihkan(CSV_MENTAH)\ndb = sqlite3.connect(\":memory:\")\nmuat(db, bersih)\n\nprint(\"LAPORAN KPI TOKO\")\nprint(f\"pembersihan: {n_mentah} baris mentah, {len(bersih)} bersih, \"\n      f\"{sum(karantina.values())} dikarantina\")\nfor alasan in sorted(karantina):\n    print(f\"  {alasan:<14}{karantina[alasan]}\")\nprint(f\"{'bulan':<9}{'omzet':>8}{'transaksi':>11}{'keranjang':>11}{'tumbuh':>8}\")\nfor bulan, omzet, transaksi, keranjang, tumbuh in db.execute(KPI_BULANAN):\n    teks = \"-\" if tumbuh is None else f\"{tumbuh:.1f}%\"\n    print(f\"{bulan:<9}{omzet:>8}{transaksi:>11}{keranjang:>11}{teks:>8}\")\nnama, porsi = db.execute(TERLARIS).fetchone()\nprint(f\"produk terlaris: {nama} ({porsi} porsi)\")\nprint(\"omzet per kategori:\")\nfor kategori, omzet in db.execute(PER_KATEGORI):\n    print(f\"  {kategori:<10}{omzet}\")\nprint(\"validasi:\")\nfor nama, sql in VALIDASI.items():\n    gagal = db.execute(sql).fetchone()[0]\n    print(f\"  {nama:<18}{'lulus' if gagal == 0 else f'gagal ({gagal})'}\")",
    },
]
