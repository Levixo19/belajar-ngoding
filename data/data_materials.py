"""Kurikulum Data & Analitik.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

DATA_BAB = [
    {
        "judul": "Berpikir dengan Data",
        "ket": "Alur analisis dan statistik deskriptif untuk yang baru selesai Python dan SQL.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Lingkungan Kerja Data",
        "ket": "Notebook, environment Python, dan spreadsheet sebagai tempat kerja analis.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "NumPy dan Matematika Numerik",
        "ket": "Larik, broadcasting, vektor, gradien, dan SciPy.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "pandas: Mengolah Tabel",
        "ket": "Membaca, membersihkan, meringkas, dan menggabung data tabel dengan pandas.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Visualisasi dan Aplikasi Data",
        "ket": "Grafik yang jujur dan aplikasi data interaktif.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Statistik Inferensial dan Eksperimen",
        "ket": "Menarik kesimpulan dari sampel, A/B testing, dan deret waktu.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Data Kolumnar di Satu Mesin",
        "ket": "Arrow, Parquet, DuckDB, Polars, dan Dask untuk data yang mulai besar.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "R dan Alat Statistik Lain",
        "ket": "R dan tidyverse untuk pengguna Python, plus peta alat statistik lain.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Dasar Rekayasa Data",
        "ket": "ETL/ELT, gudang data, pemodelan dimensional, dan kualitas data.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Orkestrasi dan Transformasi Data",
        "ket": "Menjadwalkan pipeline dengan Airflow dan mentransformasi data dengan dbt.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Big Data dan Streaming",
        "ket": "Spark untuk data terdistribusi dan Kafka untuk aliran event.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Lakehouse dan Platform Data Cloud",
        "ket": "Format tabel terbuka dan platform data terkelola di cloud.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "BI dan Komunikasi Data",
        "ket": "Power BI, desain dasbor, dan peta alat BI; ditutup proyek akhir.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
]

DATA_MATERIALS = [
    {
        "title": "1. Alur Kerja Analisis Data",
        "sections": [
            {
                "body": [
                    "Analisis data itu kerja menjawab pertanyaan pakai angka.",
                    "Pertanyaannya bisa sesederhana \"hari apa kedai kita paling",
                    "ramai?\" atau seberat \"kenapa banyak pelanggan berhenti",
                    "langganan bulan ini?\". Datanya bisa catatan kasir, isi",
                    "spreadsheet, tabel di database, atau log aplikasi.",
                    "",
                    "Kurikulum Python dan SQL sudah ngajarin kamu membaca berkas,",
                    "memakai dict, dan menulis SELECT. Di sini alat yang sama dipakai",
                    "untuk satu tujuan: bikin keputusan yang lebih baik. Dasar Python",
                    "dan SQL nggak diulang. Kalau ada yang lupa, buka lagi kurikulum",
                    "itu, misalnya soal GROUP BY atau modul csv.",
                ],
            },
            {
                "heading": "Lima langkah yang hampir selalu sama",
                "body": [
                    "Dari tugas kuliah sampai laporan untuk direksi, analisis",
                    "biasanya lewat lima langkah ini:",
                    "",
                    "  1. Pertanyaan. Tulis dulu apa yang mau dijawab, dan keputusan",
                    "     apa yang bergantung pada jawabannya. \"Lihat-lihat data",
                    "     penjualan\" itu bukan pertanyaan. \"Perlu nambah barista di",
                    "     hari apa?\" itu pertanyaan.",
                    "  2. Kumpulkan. Cari data yang bisa menjawabnya: ekspor dari",
                    "     aplikasi kasir, query ke database, atau formulir survei.",
                    "  3. Bersihkan. Buang baris kosong dan baris kembar, samakan",
                    "     penulisan, betulkan tipe data. Langkah ini sering makan",
                    "     waktu paling lama.",
                    "  4. Analisis. Hitung ringkasan, bandingkan kelompok, cari pola.",
                    "  5. Komunikasikan. Sampaikan jawabannya dalam bentuk yang",
                    "     dimengerti orang yang mengambil keputusan: satu tabel",
                    "     pendek, satu grafik, atau satu kalimat.",
                    "",
                    "Langkahnya sering berputar. Waktu membersihkan, kamu bisa sadar",
                    "datanya nggak cukup untuk menjawab pertanyaan, lalu balik ke",
                    "langkah pertama dan mempertajam pertanyaannya.",
                    "",
                    "Kurikulum ini mengikuti urutan itu. Bab 01 membekali kamu",
                    "dengan statistik untuk langkah analisis. Bab 02 menyiapkan",
                    "tempat kerjanya. Bab 04 membahas pembersihan dengan pandas, bab",
                    "05 soal grafik, dan bab 06 soal menarik kesimpulan dari",
                    "sampel. Bab 09 sampai 11 membahas pengumpulan data dalam skala",
                    "besar, dan bab 13 soal dasbor untuk menyampaikan hasil.",
                ],
            },
            {
                "heading": "Lima langkah dalam satu program kecil",
                "code": "import csv\nimport io\nfrom collections import defaultdict\n\n# 1. Pertanyaan: hari apa kedai paling ramai?\n# 2. Kumpulkan: catatan kasir (biasanya dari berkas ekspor)\ncatatan = io.StringIO(\"\"\"tanggal,hari,cup\n2026-10-04,Minggu,140\n2026-10-05,Senin,82\n2026-10-06,Selasa,\n2026-10-07,Rabu,95\n2026-10-10,Sabtu,151\n2026-10-11,Minggu,136\n2026-10-12,Senin,78\n2026-10-12,Senin,78\n\"\"\")\nmentah = list(csv.DictReader(catatan))\n\n# 3. Bersihkan: buang baris tanpa angka dan baris kembar\nbersih, sudah = [], set()\nfor b in mentah:\n    kunci = (b[\"tanggal\"], b[\"hari\"], b[\"cup\"])\n    if b[\"cup\"] == \"\" or kunci in sudah:\n        continue\n    sudah.add(kunci)\n    bersih.append(b)\n\n# 4. Analisis: rata-rata cup per hari\ntotal = defaultdict(int)\nbanyak = defaultdict(int)\nfor b in bersih:\n    total[b[\"hari\"]] += int(b[\"cup\"])\n    banyak[b[\"hari\"]] += 1\n\n# 5. Komunikasikan: urutkan dari yang paling ramai\nprint(f\"{len(mentah)} baris mentah, {len(bersih)} baris bersih\")\nfor hari in sorted(total, key=lambda h: total[h] / banyak[h], reverse=True):\n    rata = total[hari] / banyak[hari]\n    print(f\"{hari:<7} {rata:6.1f} cup  (dari {banyak[hari]} hari)\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  8 baris mentah, 6 baris bersih",
                    "  Sabtu    151.0 cup  (dari 1 hari)",
                    "  Minggu   138.0 cup  (dari 2 hari)",
                    "  Rabu      95.0 cup  (dari 1 hari)",
                    "  Senin     80.0 cup  (dari 2 hari)",
                    "",
                    "io.StringIO membungkus teks supaya bisa dibaca seperti berkas.",
                    "Di pekerjaan nyata baris itu diganti open(\"kasir.csv\").",
                    "Selasa hilang karena angkanya kosong, dan satu baris Senin",
                    "dibuang karena kembar. Kalau baris kembar itu ikut dihitung,",
                    "Senin kelihatan lebih ramai dari kenyataannya.",
                    "",
                    "Lihat juga keterangan \"dari 1 hari\". Sabtu paling atas, tapi",
                    "angkanya cuma dari satu Sabtu. Bisa jadi hari itu ada acara",
                    "di dekat kedai. Dua minggu data terlalu sedikit untuk",
                    "memutuskan jadwal karyawan, dan jawaban jujurnya: \"Sabtu dan",
                    "Minggu kelihatannya paling ramai, kumpulkan dua bulan data",
                    "dulu untuk memastikan.\"",
                ],
            },
            {
                "heading": "Siapa mengerjakan apa",
                "body": [
                    "Lowongan di ranah data memakai beberapa nama jabatan. Situs",
                    "roadmap.sh punya peta belajar untuk masing-masing, dan",
                    "pembagiannya kira-kira begini:",
                    "",
                    "  Data Analyst     menjawab pertanyaan bisnis dari data yang",
                    "                   sudah ada: SQL, spreadsheet, pandas, grafik",
                    "  BI Analyst       membangun dasbor dan laporan rutin yang",
                    "                   dipakai banyak orang, misalnya di Power BI",
                    "  Data Engineer    membangun pipeline yang mengumpulkan data",
                    "                   dari banyak sistem ke satu gudang data",
                    "  Data Scientist   statistik lanjut dan machine learning untuk",
                    "                   memprediksi atau menjelaskan sesuatu",
                    "",
                    "Di perusahaan kecil, satu orang sering merangkap semuanya. Bab",
                    "01 sampai 08 paling dekat dengan pekerjaan Data Analyst. Bab 09",
                    "sampai 12 condong ke Data Engineer, dan bab 13 ke BI Analyst.",
                    "Machine learning dibahas di kurikulum AI & Machine Learning.",
                ],
            },
            {
                "heading": "Kesalahan yang sering terjadi",
                "body": [
                    "Jebakan: mulai dari data, bukan dari pertanyaan. Hasilnya dua",
                    "puluh grafik yang rapi, dan nggak satu pun menjawab apa-apa.",
                    "Kalau kamu nggak bisa menulis pertanyaannya dalam satu",
                    "kalimat, jangan buka datanya dulu.",
                    "",
                    "Kesalahan kedua: menganggap data mentah sudah benar. Kasir bisa",
                    "salah ketik, aplikasi bisa mencatat transaksi dua kali, dan",
                    "kolom yang mestinya angka bisa berisi \"-\" atau \"belum\".",
                    "Selalu hitung berapa baris yang masuk dan berapa yang kamu",
                    "buang, lalu tulis angkanya di laporan.",
                    "",
                    "Kesalahan ketiga: menyimpulkan dari data yang terlalu sedikit,",
                    "seperti Sabtu di contoh tadi. Bab 06 membahas cara mengukur",
                    "seberapa yakin kamu boleh terhadap sebuah kesimpulan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir yang dipakai kedai, warung, dan toko kecil",
                    "hampir selalu punya menu ekspor laporan penjualan ke CSV atau",
                    "Excel. Berkas itulah bahan analisis pertama di banyak usaha",
                    "kecil, jauh sebelum mereka punya database atau dasbor.",
                    "",
                    "Kasus kecil: pemilik kedai kopi bertanya, \"Aku perlu nambah",
                    "satu barista. Hari apa aja dia harus masuk?\" Ia mengirim",
                    "ekspor kasir tiga bulan terakhir.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis pertanyaannya jadi bisa dihitung: rata-rata cup per",
                    "     hari dalam seminggu, dan jam berapa antrean terpanjang.",
                    "  2. Hitung baris mentah, lalu buang baris kosong dan kembar.",
                    "     Catat berapa yang dibuang.",
                    "  3. Kelompokkan per hari dan hitung rata-ratanya, seperti",
                    "     program di atas. Tampilkan juga dari berapa hari tiap",
                    "     angka dihitung:",
                    "       Sabtu  151.0 cup  (dari 13 hari)",
                    "  4. Sampaikan satu kalimat jawaban plus tabel pendek, misalnya",
                    "     \"Sabtu dan Minggu rata-rata 40 persen lebih ramai, jadi",
                    "     barista baru masuk akhir pekan.\"",
                ],
            },
        ],
    },
    {
        "title": "2. Statistik Deskriptif: Pusat dan Sebaran",
        "sections": [
            {
                "body": [
                    "Statistik deskriptif itu cara meringkas sekumpulan angka jadi",
                    "beberapa angka saja. Ringkasannya menjawab dua pertanyaan:",
                    "",
                    "  - Di mana pusatnya? Angka berapa yang paling mewakili data?",
                    "  - Seberapa menyebar? Apakah angkanya mirip-mirip semua, atau",
                    "    ada yang jauh di bawah dan jauh di atas?",
                    "",
                    "Ada tiga ukuran pusat yang umum. Mean atau rata-rata adalah",
                    "jumlah semua nilai dibagi banyaknya. Median adalah nilai tengah",
                    "sesudah data diurutkan; kalau banyaknya genap, median adalah",
                    "rata-rata dua nilai tengah. Modus adalah nilai yang paling",
                    "sering muncul.",
                    "",
                    "Python sudah punya modul statistics untuk semua ini, jadi kamu",
                    "nggak perlu memasang apa pun.",
                ],
            },
            {
                "heading": "Gaji delapan karyawan",
                "code": """import statistics as st

gaji = [4200, 4500, 4500, 5000, 5300, 5800, 6100, 38000]  # ribu rupiah

print("mean    :", st.mean(gaji))
print("median  :", st.median(gaji))
print("modus   :", st.mode(gaji))
print("rentang :", max(gaji) - min(gaji))
print("stdev   :", round(st.stdev(gaji), 1))
print("kuartil :", st.quantiles(gaji, n=4))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  mean    : 9175",
                    "  median  : 5150.0",
                    "  modus   : 4500",
                    "  rentang : 33800",
                    "  stdev   : 11665.8",
                    "  kuartil : [4500.0, 5150.0, 6025.0]",
                    "",
                    "Rata-ratanya 9,175 juta, padahal tujuh dari delapan orang",
                    "gajinya di bawah 6,2 juta. Satu gaji 38 juta, mungkin milik",
                    "pemiliknya, menarik rata-rata jauh ke atas. Nilai yang jauh",
                    "berbeda dari kelompoknya seperti itu disebut pencilan",
                    "(outlier).",
                    "",
                    "Median nggak peduli seberapa besar nilai paling atas. Ia cuma",
                    "melihat posisi tengah, jadi 5,15 juta lebih jujur menggambarkan",
                    "gaji orang biasa di kantor itu. Makanya berita soal gaji,",
                    "harga rumah, dan pendapatan biasanya memakai median.",
                    "",
                    "Kalau mean jauh lebih besar daripada median, datanya menceng ke",
                    "kanan (skewed): ada ekor panjang berisi beberapa nilai besar.",
                    "Itu tanda untuk melihat datanya lebih teliti sebelum melaporkan",
                    "rata-rata.",
                ],
            },
            {
                "heading": "Varians dan simpangan baku",
                "body": [
                    "Rentang (nilai terbesar dikurangi terkecil) gampang dihitung,",
                    "tapi cuma memakai dua angka. Satu pencilan langsung membuatnya",
                    "melonjak, seperti 33.800 tadi.",
                    "",
                    "Varians memakai semua angka. Caranya: hitung jarak tiap nilai",
                    "ke rata-rata, kuadratkan supaya jarak negatif nggak saling",
                    "menghapus dengan yang positif, lalu rata-ratakan. Simpangan",
                    "baku (standard deviation) adalah akar kuadrat varians. Akar itu",
                    "mengembalikan satuannya: kalau datanya rupiah, simpangan",
                    "bakunya juga rupiah, bukan rupiah kuadrat.",
                    "",
                    "Gampangnya, simpangan baku menjawab \"rata-rata, seberapa jauh",
                    "sebuah nilai dari pusatnya?\". Program di bawah menghitungnya",
                    "dengan tangan supaya tiap langkah kelihatan.",
                ],
            },
            {
                "heading": "Menghitung varians langkah demi langkah",
                "code": """import statistics as st

data = [2, 4, 4, 4, 5, 5, 7, 9]
rata = sum(data) / len(data)
kuadrat = [(x - rata) ** 2 for x in data]

var_populasi = sum(kuadrat) / len(data)
var_sampel = sum(kuadrat) / (len(data) - 1)

print("rata-rata      :", rata)
print("jarak kuadrat  :", kuadrat)
print("varians (n)    :", var_populasi, "->", var_populasi ** 0.5)
print("varians (n - 1):", round(var_sampel, 3), "->", round(var_sampel ** 0.5, 3))
print("pstdev / stdev :", st.pstdev(data), round(st.stdev(data), 3))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  rata-rata      : 5.0",
                    "  jarak kuadrat  : [9.0, 1.0, 1.0, 1.0, 0.0, 0.0, 4.0, 16.0]",
                    "  varians (n)    : 4.0 -> 2.0",
                    "  varians (n - 1): 4.571 -> 2.138",
                    "  pstdev / stdev : 2.0 2.138",
                    "",
                    "Ada dua versi pembagi, dan bedanya penting. Kalau data yang kamu",
                    "punya adalah seluruh kelompok yang ingin kamu gambarkan,",
                    "misalnya nilai semua siswa di satu kelas, itu populasi. Bagi",
                    "dengan n, dan fungsinya statistics.pstdev.",
                    "",
                    "Kalau datamu cuma sebagian dari kelompok yang lebih besar,",
                    "misalnya 50 responden survei yang mewakili semua pelanggan, itu",
                    "sampel. Bagi dengan n - 1, dan fungsinya statistics.stdev.",
                    "Sampel cenderung lebih rapat daripada populasinya, dan pembagi",
                    "yang lebih kecil itu mengoreksinya sedikit ke atas.",
                    "",
                    "Jebakan: alat yang berbeda memakai pembagi bawaan yang",
                    "berbeda. Angka yang beda tipis di dua alat biasanya berasal",
                    "dari sini:",
                    "",
                    "  bagi n - 1   statistics.stdev, Excel STDEV.S, pandas .std()",
                    "  bagi n       statistics.pstdev, Excel STDEV.P, NumPy np.std()",
                ],
            },
            {
                "heading": "Kuartil dan pencilan",
                "body": [
                    "Kuartil membagi data terurut jadi empat bagian sama banyak. Q1",
                    "adalah batas seperempat terbawah, Q2 sama dengan median, dan Q3",
                    "batas seperempat teratas. Jarak Q3 - Q1 disebut jangkauan",
                    "antarkuartil (interquartile range), yaitu lebar separuh data",
                    "yang ada di tengah.",
                    "",
                    "Aturan praktis untuk menandai pencilan:",
                    "",
                    "  batas bawah = Q1 - 1,5 x (Q3 - Q1)",
                    "  batas atas  = Q3 + 1,5 x (Q3 - Q1)",
                    "",
                    "Untuk gaji tadi, Q1 = 4500 dan Q3 = 6025. Jangkauan",
                    "antarkuartilnya 1525, jadi batas atasnya 8312,5. Gaji 38000",
                    "jelas lewat. Grafik boxplot yang nanti kamu temui di bab 05",
                    "menggambar persis aturan ini.",
                    "",
                    "Ingat: kuartil untuk data sedikit punya beberapa cara hitung.",
                    "statistics.quantiles memakai cara \"exclusive\" sebagai bawaan",
                    "dan memberi Q3 = 6025. Dengan method=\"inclusive\", cara yang",
                    "juga dipakai pandas dan Excel, hasilnya 5875:",
                    "",
                    "  st.quantiles(gaji, n=4, method=\"inclusive\")",
                    "  [4500.0, 5150.0, 5875.0]",
                    "",
                    "Dua-duanya benar. Sebutkan cara yang kamu pakai kalau angkanya",
                    "akan dibandingkan dengan hitungan orang lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan gaji dari situs lowongan kerja dan laporan harga rumah",
                    "biasanya mencantumkan median, sering ditemani rentang persentil",
                    "seperti \"25 persen terbawah\" dan \"25 persen teratas\". Itu",
                    "statistik deskriptif yang sama dengan materi ini: pusat dan",
                    "sebaran, dengan median supaya beberapa angka ekstrem nggak",
                    "menyesatkan pembaca.",
                    "",
                    "Kasus kecil: HRD minta \"gaji rata-rata\" staf gudang untuk",
                    "pengumuman lowongan. Datanya 12 orang, dan dua di antaranya",
                    "kepala gudang yang gajinya tiga kali lipat staf biasa.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung mean dan median. Kalau mean jauh di atas median,",
                    "     ada pencilan yang menarik rata-rata.",
                    "  2. Cari pencilannya dengan aturan batas atas tadi:",
                    "       q1, _, q3 = st.quantiles(gaji, n=4)",
                    "       batas = q3 + 1.5 * (q3 - q1)",
                    "  3. Tanyakan: apakah kepala gudang termasuk yang dilamar? Kalau",
                    "     nggak, keluarkan dari hitungan dan tulis alasannya.",
                    "  4. Laporkan median plus rentangnya, misalnya \"median 5,2 juta,",
                    "     separuh staf di antara 4,8 dan 5,6 juta\".",
                ],
            },
        ],
    },
    {
        "title": "3. Peluang dan Distribusi Lewat Simulasi",
        "sections": [
            {
                "body": [
                    "Peluang itu angka dari 0 sampai 1 yang menyatakan seberapa",
                    "mungkin sesuatu terjadi. Nol artinya mustahil, satu artinya",
                    "pasti. Dadu yang seimbang punya enam sisi, jadi peluang keluar",
                    "angka 6 adalah 1/6, kira-kira 0,167.",
                    "",
                    "Rumus peluang bisa terasa abstrak. Untungnya komputer bisa",
                    "melempar dadu ribuan kali dalam sekejap, jadi kita bisa melihat",
                    "peluang bekerja. Cara belajar lewat percobaan acak berulang",
                    "seperti ini disebut simulasi.",
                    "",
                    "Modul random menghasilkan angka acak semu (pseudo-random):",
                    "kelihatan acak, padahal dihitung dari satu angka awal yang",
                    "disebut seed. Seed yang sama selalu menghasilkan urutan angka",
                    "yang sama. Karena itu semua contoh di bawah memanggil",
                    "random.seed() dulu, supaya hasilnya di komputermu sama persis",
                    "dengan yang tertulis di sini.",
                ],
            },
            {
                "heading": "Melempar dadu 6000 kali",
                "code": """import random
from collections import Counter

random.seed(42)
lemparan = [random.randint(1, 6) for _ in range(6000)]
hitung = Counter(lemparan)
for mata in range(1, 7):
    print(f"mata {mata}: {hitung[mata]:4} kali  ({hitung[mata] / 6000:.3f})")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  mata 1:  970 kali  (0.162)",
                    "  mata 2:  974 kali  (0.162)",
                    "  mata 3:  989 kali  (0.165)",
                    "  mata 4: 1001 kali  (0.167)",
                    "  mata 5:  999 kali  (0.167)",
                    "  mata 6: 1067 kali  (0.178)",
                    "",
                    "Teorinya tiap mata muncul 1000 kali. Hasilnya dekat, tapi",
                    "nggak ada yang persis 1000, dan mata 6 malah kelebihan 67 kali.",
                    "Itu wajar. Acak memang begitu: rata-ratanya terarah, tiap",
                    "percobaannya meleset sedikit.",
                    "",
                    "Daftar semua hasil yang mungkin beserta seberapa sering",
                    "masing-masing muncul disebut distribusi. Dadu seimbang punya",
                    "distribusi seragam (uniform), karena keenam hasilnya punya",
                    "peluang yang sama.",
                ],
            },
            {
                "heading": "Makin banyak lemparan, makin dekat ke 1/6",
                "code": """import random

random.seed(7)
for n in (10, 100, 1000, 10000, 100000):
    enam = sum(1 for _ in range(n) if random.randint(1, 6) == 6)
    print(f"{n:>6} lemparan: proporsi angka 6 = {enam / n:.4f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "      10 lemparan: proporsi angka 6 = 0.1000",
                    "     100 lemparan: proporsi angka 6 = 0.1000",
                    "    1000 lemparan: proporsi angka 6 = 0.1620",
                    "   10000 lemparan: proporsi angka 6 = 0.1705",
                    "  100000 lemparan: proporsi angka 6 = 0.1653",
                    "",
                    "Dengan 10 atau 100 lemparan, proporsinya bisa meleset jauh dari",
                    "0,1667. Dengan 100.000 lemparan, melesetnya tinggal sepersekian",
                    "persen. Ini yang disebut hukum bilangan besar: makin banyak",
                    "percobaan, makin dekat proporsi hasilnya ke peluang menurut",
                    "teori.",
                    "",
                    "Jebakan: hukum ini sering dibaca terbalik. Kalau koin keluar",
                    "gambar lima kali berturut-turut, lemparan keenam tetap 50:50.",
                    "Koin nggak punya ingatan dan nggak \"berutang\" angka.",
                    "Proporsinya mendekati 0,5 karena lemparan yang banyak sekali",
                    "membuat lima gambar itu nggak berarti lagi, bukan karena koin",
                    "menyeimbangkan diri. Salah kaprah ini punya nama: gambler's",
                    "fallacy.",
                ],
            },
            {
                "heading": "Rata-rata empat dadu membentuk lonceng",
                "code": """import random
from collections import Counter

random.seed(1)
rata_rata = []
for _ in range(2000):
    empat_dadu = [random.randint(1, 6) for _ in range(4)]
    rata_rata.append(sum(empat_dadu) / 4)

kelompok = Counter(int(r * 2) / 2 for r in rata_rata)
for nilai in sorted(kelompok):
    batang = "#" * (kelompok[nilai] // 10)
    print(f"{nilai:.1f}  {kelompok[nilai]:4}  {batang}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  1.0     9  ",
                    "  1.5    44  ####",
                    "  2.0   148  ##############",
                    "  2.5   267  ##########################",
                    "  3.0   395  #######################################",
                    "  3.5   460  ##############################################",
                    "  4.0   376  #####################################",
                    "  4.5   203  ####################",
                    "  5.0    79  #######",
                    "  5.5    19  #",
                    "",
                    "Satu dadu distribusinya rata. Tapi rata-rata empat dadu",
                    "menumpuk di tengah, sekitar 3,5, dan menipis ke dua ujung.",
                    "Rata-rata 1 atau 6 butuh empat dadu yang kompak keluar angka",
                    "sama, dan itu jarang. Bentuk lonceng ini muncul juga kalau kamu",
                    "merata-ratakan hal lain yang acak. Teorema limit pusat (central",
                    "limit theorem) menjelaskannya: rata-rata dari banyak nilai acak",
                    "cenderung berdistribusi normal, apa pun distribusi asalnya.",
                    "",
                    "Distribusi normal adalah lonceng simetris yang ditentukan dua",
                    "angka: rata-rata (letak puncak) dan simpangan baku (lebar",
                    "lonceng). Aturan praktisnya 68-95-99,7: sekitar 68 persen data",
                    "ada dalam satu simpangan baku dari rata-rata, 95 persen dalam",
                    "dua, dan 99,7 persen dalam tiga. Teorema ini juga alasan bab 06",
                    "bisa menghitung seberapa yakin kita terhadap rata-rata sampel.",
                ],
            },
            {
                "heading": "Menghitung peluang tanpa simulasi",
                "code": """from math import comb
from statistics import NormalDist

# Binomial: 20 pengunjung, tiap orang membeli dengan peluang 0,1
n, p = 20, 0.1
for k in range(5):
    peluang = comb(n, k) * p**k * (1 - p) ** (n - k)
    print(f"tepat {k} pembeli: {peluang:.3f}")

# Normal: tinggi rata-rata 165 cm, simpangan baku 7 cm
tinggi = NormalDist(mu=165, sigma=7)
print(f"lebih pendek dari 172 cm: {tinggi.cdf(172):.3f}")
print(f"antara 158 dan 172 cm   : {tinggi.cdf(172) - tinggi.cdf(158):.3f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tepat 0 pembeli: 0.122",
                    "  tepat 1 pembeli: 0.270",
                    "  tepat 2 pembeli: 0.285",
                    "  tepat 3 pembeli: 0.190",
                    "  tepat 4 pembeli: 0.090",
                    "  lebih pendek dari 172 cm: 0.841",
                    "  antara 158 dan 172 cm   : 0.683",
                    "",
                    "Distribusi binomial dipakai untuk percobaan ya-atau-tidak yang",
                    "diulang n kali dengan peluang p yang sama. comb(n, k) menghitung",
                    "berapa cara memilih k orang dari n. Hasilnya: walaupun peluang",
                    "membeli 10 persen, dari 20 pengunjung ada 12 persen kemungkinan",
                    "nggak ada satu pun yang membeli.",
                    "",
                    "NormalDist dari modul statistics menghitung peluang di",
                    "distribusi normal. cdf(x) memberi peluang sebuah nilai lebih",
                    "kecil dari x. Antara 158 dan 172 cm artinya satu simpangan baku",
                    "ke kiri dan ke kanan, dan hasilnya 0,683, cocok dengan aturan",
                    "68 persen tadi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online, aplikasi ojek, dan bank memakai cara pikir ini",
                    "setiap hari. Rasio konversi (berapa persen pengunjung yang",
                    "membeli) diperlakukan sebagai peluang, dan simulasi dipakai",
                    "untuk memperkirakan stok, antrean, atau risiko yang sulit",
                    "dihitung dengan rumus. Teknik simulasi acak berulang ini",
                    "disebut metode Monte Carlo.",
                    "",
                    "Kasus kecil: pemilik toko online kecil heran. Biasanya 10",
                    "persen pengunjung membeli, tapi kemarin dari 20 pengunjung",
                    "nggak ada satu pun yang membeli. Ia curiga tombol bayarnya",
                    "rusak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Anggap tiap pengunjung percobaan ya-atau-tidak dengan",
                    "     p = 0,1. Itu distribusi binomial dengan n = 20.",
                    "  2. Hitung peluang nol pembeli:",
                    "       comb(20, 0) * 0.1**0 * 0.9**20",
                    "     Hasilnya sekitar 0,122. Kejadian seperti itu muncul kira-",
                    "     kira satu dari delapan hari.",
                    "  3. Simpulkan bahwa satu hari sepi belum bukti tombolnya rusak.",
                    "     Cek tombolnya sekali, lalu pantau beberapa hari lagi.",
                    "  4. Kalau tiga hari berturut-turut nol pembeli, peluangnya",
                    "     0,122 pangkat 3, sekitar 0,002. Itu sudah layak dicurigai.",
                ],
            },
        ],
    },
    {
        "title": "4. Korelasi, Regresi, dan Jebakan Sebab-Akibat",
        "sections": [
            {
                "body": [
                    "Sering kita ingin tahu apakah dua hal bergerak bareng. Kalau",
                    "cuaca makin panas, apakah es teh makin laku? Kalau jam belajar",
                    "naik, apakah nilai ikut naik?",
                    "",
                    "Korelasi mengukur seberapa rapat dua variabel membentuk garis",
                    "lurus. Ukurannya disebut koefisien korelasi Pearson, ditulis r,",
                    "nilainya dari -1 sampai 1:",
                    "",
                    "  r mendekati  1   naik bareng, titiknya hampir segaris",
                    "  r mendekati  0   nggak ada pola garis lurus",
                    "  r mendekati -1   yang satu naik, yang lain turun",
                    "",
                    "Regresi linear melangkah lebih jauh. Ia mencari satu garis",
                    "y = kemiringan x x + intersep yang paling dekat dengan semua",
                    "titik, supaya kita bisa menebak y dari x.",
                ],
            },
            {
                "heading": "Suhu dan es teh di kantin",
                "code": """import statistics as st

suhu = [26, 27, 29, 30, 31, 32, 33, 34]      # derajat Celsius
es_teh = [52, 58, 57, 66, 64, 73, 78, 75]    # gelas terjual

r = st.correlation(suhu, es_teh)
garis = st.linear_regression(suhu, es_teh)
print(f"korelasi r = {r:.3f}")
print(f"kemiringan = {garis.slope:.2f}")
print(f"intersep   = {garis.intercept:.2f}")

for t, y in zip(suhu, es_teh):
    tebak = garis.slope * t + garis.intercept
    print(f"{t} derajat: terjual {y}, garis menebak {tebak:.0f}")
print(f"40 derajat: garis menebak {garis.slope * 40 + garis.intercept:.0f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  korelasi r = 0.942",
                    "  kemiringan = 3.14",
                    "  intersep   = -29.60",
                    "  26 derajat: terjual 52, garis menebak 52",
                    "  27 derajat: terjual 58, garis menebak 55",
                    "  29 derajat: terjual 57, garis menebak 61",
                    "  30 derajat: terjual 66, garis menebak 65",
                    "  31 derajat: terjual 64, garis menebak 68",
                    "  32 derajat: terjual 73, garis menebak 71",
                    "  33 derajat: terjual 78, garis menebak 74",
                    "  34 derajat: terjual 75, garis menebak 77",
                    "  40 derajat: garis menebak 96",
                    "",
                    "r = 0,942 artinya hubungannya kuat dan searah. Kemiringan 3,14",
                    "artinya tiap suhu naik satu derajat, garis menebak kantin",
                    "menjual sekitar tiga gelas lebih banyak. Kuadrat r, yaitu",
                    "0,888, sering ditulis R kuadrat: kira-kira 89 persen naik",
                    "turunnya penjualan bisa dijelaskan oleh garis suhu ini.",
                    "",
                    "Intersep -29,60 adalah tebakan garis untuk suhu 0 derajat.",
                    "Menjual minus 30 gelas jelas mustahil. Garis cuma bisa",
                    "dipercaya di sekitar data yang membentuknya, di sini 26 sampai",
                    "34 derajat. Tebakan 96 gelas untuk 40 derajat juga meragukan,",
                    "karena nggak ada data sepanas itu. Menebak di luar rentang data",
                    "disebut ekstrapolasi, dan hasilnya sering meleset.",
                ],
            },
            {
                "heading": "Dari mana garis itu datang",
                "body": [
                    "Garis regresi dipilih dengan cara kuadrat terkecil (least",
                    "squares). Untuk tiap titik, hitung selisih antara nilai asli",
                    "dan tebakan garis, kuadratkan, lalu jumlahkan. Garis terbaik",
                    "adalah garis yang jumlah kuadratnya paling kecil. Hasilnya bisa",
                    "dihitung langsung dengan dua rumus:",
                    "",
                    "  kemiringan = jumlah (x - rata_x)(y - rata_y)",
                    "               / jumlah (x - rata_x) kuadrat",
                    "  intersep   = rata_y - kemiringan x rata_x",
                    "",
                    "Kamu akan menulis dua rumus ini sendiri di latihan, lalu",
                    "mencocokkannya dengan statistics.linear_regression. Fungsi itu",
                    "dan statistics.correlation ada sejak Python 3.10.",
                ],
            },
            {
                "heading": "Lihat datanya, jangan cuma r",
                "body": [
                    "Pearson cuma mengukur pola garis lurus. Hubungan yang",
                    "melengkung, misalnya penjualan yang naik lalu turun lagi saat",
                    "terlalu panas, bisa punya r mendekati nol walaupun hubungannya",
                    "kuat. Untuk hubungan yang selalu searah tapi nggak lurus, pakai",
                    "korelasi Spearman yang memakai peringkat:",
                    "",
                    "  st.correlation(suhu, es_teh, method=\"ranked\")",
                    "",
                    "Pilihan method=\"ranked\" ada sejak Python 3.12. Untuk data",
                    "kantin tadi hasilnya 0,929.",
                    "",
                    "Ahli statistik Francis Anscombe pernah membuat empat kumpulan",
                    "data kecil yang mean, varians, korelasi, dan garis regresinya",
                    "hampir sama persis. Begitu digambar, bentuknya beda total: satu",
                    "garis wajar, satu melengkung, dua lagi rusak oleh satu",
                    "pencilan. Kumpulan ini dikenal sebagai kuartet Anscombe.",
                    "Pelajarannya: selalu gambar grafik sebarnya dulu. Caranya ada",
                    "di bab 05.",
                ],
            },
            {
                "heading": "Korelasi belum tentu sebab",
                "body": [
                    "Di banyak kota, penjualan es krim dan jumlah kasus tenggelam",
                    "naik dan turun bareng. Korelasinya kuat, tapi es krim jelas",
                    "nggak bikin orang tenggelam. Keduanya naik karena hal ketiga:",
                    "cuaca panas membuat orang beli es krim dan juga pergi",
                    "berenang. Hal ketiga seperti itu disebut variabel perancu",
                    "(confounder).",
                    "",
                    "Selain perancu, korelasi bisa muncul karena dua hal lain:",
                    "",
                    "  - Arahnya terbalik. Toko yang ramai memasang lebih banyak",
                    "    iklan, dan orang menyimpulkan iklan yang bikin ramai.",
                    "  - Kebetulan. Kalau kamu membandingkan ratusan pasang",
                    "    variabel, beberapa pasang pasti berkorelasi tanpa alasan.",
                    "",
                    "Cara paling meyakinkan untuk membuktikan sebab-akibat adalah",
                    "eksperimen: acak siapa yang dapat perlakuan dan siapa yang",
                    "nggak, lalu bandingkan. Bab 06 membahasnya lewat A/B testing.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs jual beli properti menampilkan perkiraan harga rumah",
                    "berdasarkan luas, lokasi, dan jumlah kamar. Versi paling",
                    "sederhana dari perkiraan seperti itu adalah regresi linear",
                    "satu variabel di materi ini. Tim pemasaran juga sering melihat",
                    "korelasi antara biaya iklan dan penjualan, dan di situlah",
                    "jebakan sebab-akibat paling sering terjadi.",
                    "",
                    "Kasus kecil: manajer kantin melihat grafik suhu dan penjualan",
                    "es teh, lalu bilang, \"Bulan depan diramalkan 40 derajat, siapkan",
                    "100 gelas per hari.\"",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung r dan garis regresinya dari data yang ada:",
                    "       garis = st.linear_regression(suhu, es_teh)",
                    "  2. Cek rentang data. Suhu tertinggi yang pernah tercatat 34",
                    "     derajat, jadi 40 derajat itu ekstrapolasi.",
                    "  3. Tanya hal lain yang mungkin berubah. Kalau sepanas itu,",
                    "     siswa bisa memilih tetap di kelas, atau stok es batu habis.",
                    "  4. Sarankan angka yang lebih aman, misalnya stok untuk 80",
                    "     gelas plus cadangan, lalu catat penjualan aslinya supaya",
                    "     garisnya bisa diperbarui.",
                ],
            },
        ],
    },
    {
        "title": "5. Jupyter, Colab, dan Kaggle",
        "sections": [
            {
                "body": [
                    "Analisis data jarang lurus dari atas ke bawah. Kamu memuat",
                    "data, melihat lima baris pertama, sadar ada kolom yang aneh,",
                    "membetulkannya, lalu menggambar grafik dan sadar lagi ada yang",
                    "kurang. Kalau tiap perubahan kecil berarti menjalankan ulang",
                    "seluruh skrip, termasuk memuat berkas CSV 500 MB, kamu bakal",
                    "lebih banyak menunggu daripada berpikir.",
                    "",
                    "Notebook dibuat untuk cara kerja bolak-balik itu. Notebook",
                    "adalah dokumen di browser yang terdiri dari sel. Tiap sel bisa",
                    "dijalankan sendiri, dan hasilnya (angka, tabel, grafik) muncul",
                    "tepat di bawahnya. Kode, hasil, dan catatan penjelasan tersimpan",
                    "bareng dalam satu berkas berakhiran .ipynb.",
                    "",
                    "Alat notebook yang paling banyak dipakai adalah Jupyter. Namanya",
                    "dari tiga bahasa yang pertama didukungnya: Julia, Python, dan R.",
                    "Di Survei Stack Overflow 2025, Jupyter Notebook dan JupyterLab",
                    "dipakai 14,1 persen responden sebagai alat kerja.",
                ],
            },
            {
                "heading": "Sel dan kernel",
                "body": [
                    "Ada dua jenis sel. Sel kode berisi Python. Sel Markdown berisi",
                    "teks berformat: judul, daftar, tautan, untuk menjelaskan apa",
                    "yang sedang kamu kerjakan.",
                    "",
                    "Di belakang notebook ada kernel, yaitu program Python yang",
                    "terus hidup dan menjalankan kode tiap sel. Semua sel memakai",
                    "kernel yang sama, jadi variabel yang dibuat di sel 2 bisa",
                    "dipakai di sel 5. Data yang sudah dimuat tetap ada di memori",
                    "kernel sampai kernelnya dimatikan atau di-restart.",
                    "",
                    "Tekan Shift+Enter untuk menjalankan sel yang sedang aktif.",
                    "Angka di kiri sel, misalnya [3], adalah nomor urut eksekusi:",
                    "sel itu yang ketiga dijalankan sejak kernel dinyalakan. Nomor",
                    "ini penting, nanti kelihatan kenapa.",
                ],
            },
            {
                "heading": "Memasang dan membuka JupyterLab",
                "bahasa": "terminal",
                "code": """cd ~/proyek-kopi
python3 -m venv .venv
source .venv/bin/activate
pip install jupyterlab pandas
jupyter lab""",
            },
            {
                "body": [
                    "Perintah terakhir menyalakan server Jupyter di komputermu dan",
                    "membuka browser ke alamat http://localhost:8888. Semua tetap",
                    "jalan di laptopmu sendiri, tanpa internet. Tiga baris di",
                    "tengah membuat environment terpisah untuk proyek ini; caranya",
                    "dibahas di materi berikutnya.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), versi terbarunya",
                    "JupyterLab 4.6.4 dan Jupyter Notebook 7.6.3. JupyterLab",
                    "tampil seperti IDE kecil: daftar berkas, banyak tab, terminal.",
                    "Jupyter Notebook tampil lebih sederhana, satu notebook per tab.",
                    "Sejak versi 7, Notebook dibangun di atas komponen JupyterLab,",
                    "jadi berkas .ipynb-nya sama persis dan bisa dibuka di",
                    "keduanya. VS Code juga bisa membuka .ipynb lewat ekstensi",
                    "Jupyter.",
                ],
            },
            {
                "heading": "Jebakan urutan sel, ditiru dengan Python biasa",
                "code": """sel = {
    1: "harga = 10000",
    2: "harga = harga * 2",
    3: "print('  total:', harga * 3)",
}
kernel = {}  # memori bersama, seperti kernel Jupyter


def jalankan(nomor):
    exec(sel[nomor], kernel)


print("Urutan 1, 2, 3:")
for n in (1, 2, 3):
    jalankan(n)

print("Sel 2 tanpa sengaja dijalankan lagi, lalu sel 3:")
jalankan(2)
jalankan(3)

print("Restart & Run All:")
kernel.clear()
for n in (1, 2, 3):
    jalankan(n)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Urutan 1, 2, 3:",
                    "    total: 60000",
                    "  Sel 2 tanpa sengaja dijalankan lagi, lalu sel 3:",
                    "    total: 120000",
                    "  Restart & Run All:",
                    "    total: 60000",
                    "",
                    "Program kecil ini meniru kernel: tiga potong kode yang berbagi",
                    "satu dict sebagai memori. Begitu sel 2 dijalankan dua kali,",
                    "harga jadi 40000, dan totalnya berubah walaupun nggak ada satu",
                    "huruf pun kode yang diubah. Di notebook sungguhan hal ini",
                    "gampang terjadi: kamu menyunting sel di tengah, menjalankannya",
                    "lagi, lalu lupa. Notebook-nya kelihatan benar di layarmu, tapi",
                    "hasilnya nggak bisa diulang orang lain.",
                    "",
                    "Jebakan: sel yang sudah dihapus tetap meninggalkan variabelnya",
                    "di kernel. Notebook bisa jalan di laptopmu dan langsung",
                    "NameError di laptop temanmu, karena variabelnya ternyata dibuat",
                    "di sel yang sudah nggak ada.",
                    "",
                    "Obatnya satu kebiasaan: sebelum menyimpan atau mengirim",
                    "notebook, pilih menu Kernel lalu Restart Kernel and Run All",
                    "Cells. Kernel dikosongkan, semua sel dijalankan dari atas. Kalau",
                    "lolos tanpa error dan angka-angkanya sama, notebook-mu aman",
                    "dibagikan. Nomor sel yang berurutan 1, 2, 3 dari atas juga",
                    "jadi tanda bagi pembaca bahwa urutannya beres.",
                    "",
                    "Satu tip lagi: kalau perlu memasang paket dari dalam notebook,",
                    "tulis %pip install nama-paket di sebuah sel. Perintah %pip",
                    "memasang ke environment milik kernel yang sedang dipakai,",
                    "jadi paketnya pasti bisa diimpor sesudahnya.",
                ],
            },
            {
                "heading": "Colab dan Kaggle: notebook di cloud",
                "body": [
                    "Google Colab adalah layanan notebook gratis milik Google yang",
                    "jalan di browser. Tampilannya mirip Jupyter dan berkasnya juga",
                    ".ipynb. Kelebihannya: nggak perlu memasang apa pun, banyak",
                    "pustaka data sudah terpasang, dan ada akses GPU terbatas untuk",
                    "deep learning. Kekurangannya: butuh akun Google dan internet,",
                    "sesi gratis bisa terputus kalau lama nggak dipakai, dan berkas",
                    "yang diunggah ke sesi hilang saat sesi berakhir. Simpan",
                    "berkasmu di Google Drive. Ada paket berbayar untuk kuota yang",
                    "lebih besar.",
                    "",
                    "Kaggle juga milik Google, tapi pusatnya komunitas: ribuan",
                    "dataset gratis, kompetisi data science, notebook di cloud",
                    "dengan kuota GPU, dan kursus singkat bernama Kaggle Learn.",
                    "Kaggle cocok untuk mencari data latihan dan membangun",
                    "portofolio. Tiap dataset punya lisensi sendiri, dan nggak",
                    "semuanya boleh disebarkan ulang, jadi cek dulu sebelum dipakai",
                    "untuk tulisan atau aplikasi.",
                    "",
                    "Kapan memilih yang mana:",
                    "  - Jupyter di laptop: data kantor, data pribadi, atau kerja",
                    "    tanpa internet.",
                    "  - Colab: laptop terlalu lemah, butuh GPU sesekali, atau ingin",
                    "    berbagi notebook lewat tautan.",
                    "  - Kaggle: mencari dataset, ikut kompetisi, belajar dari",
                    "    notebook orang lain.",
                    "",
                    "Ingat: jangan unggah data pelanggan atau data perusahaan ke",
                    "akun Google pribadimu. Data seperti itu biasanya punya aturan",
                    "tempat penyimpanan sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Notebook dipakai di kampus untuk tugas analisis, di Kaggle",
                    "untuk kompetisi, dan di perusahaan untuk eksplorasi data",
                    "sebelum hasilnya dijadikan laporan rutin. Berkas .ipynb juga",
                    "ditampilkan apa adanya oleh GitHub, lengkap dengan grafiknya,",
                    "jadi banyak orang memakainya sebagai portofolio.",
                    "",
                    "Kasus kecil: kamu mengirim notebook analisis penjualan ke",
                    "atasan. Ia membalas, \"Di laptopku muncul NameError: name",
                    "'bersih' is not defined di sel 9.\"",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka notebook-mu dan lihat nomor di kiri tiap sel. Kalau",
                    "     urutannya lompat, misalnya [12], [3], [27], ada sel yang",
                    "     dijalankan nggak berurutan.",
                    "  2. Pilih Kernel lalu Restart Kernel and Run All Cells. Error",
                    "     yang sama bakal muncul di laptopmu juga.",
                    "  3. Cari sel yang membuat variabel bersih. Kalau sudah",
                    "     terhapus, tulis ulang, dan taruh di atas sel 9:",
                    "       bersih = mentah.dropna()",
                    "  4. Ulangi Restart and Run All sampai lolos, simpan, lalu",
                    "     kirim ulang dengan catatan versi Python dan pustakanya.",
                ],
            },
        ],
    },
    {
        "title": "6. Environment Python: venv, conda, dan Miniforge",
        "sections": [
            {
                "body": [
                    "Bayangkan dua proyek di satu laptop. Proyek lama ditulis",
                    "untuk pandas 2.2, proyek baru memakai pandas 3.0 yang",
                    "perilakunya sudah berubah. Kalau semua paket dipasang di satu",
                    "tempat untuk seluruh komputer, memperbarui pandas demi proyek",
                    "baru bisa merusak proyek lama.",
                    "",
                    "Environment menyelesaikan masalah itu. Environment adalah folder",
                    "terpisah berisi satu salinan Python beserta paket-paketnya",
                    "sendiri. Tiap proyek punya environment-nya, jadi versi paket di",
                    "satu proyek nggak mengganggu proyek lain.",
                    "",
                    "Python sudah membawa alat untuk ini, namanya venv. Di Fedora,",
                    "python3 -m venv langsung bisa dipakai.",
                ],
            },
            {
                "heading": "Membuat dan memakai venv",
                "bahasa": "terminal",
                "code": """cd ~/proyek-kopi
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas matplotlib
python -m pip freeze > requirements.txt
deactivate

# di laptop lain, sesudah menyalin folder proyek tanpa .venv:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt""",
            },
            {
                "body": [
                    "Baris demi baris:",
                    "",
                    "  python3 -m venv .venv",
                    "    Membuat folder .venv berisi Python dan pip milik proyek",
                    "    ini. Nama .venv cuma kebiasaan, tapi hampir semua editor",
                    "    mengenalinya otomatis.",
                    "",
                    "  source .venv/bin/activate",
                    "    Mengaktifkan environment. Prompt terminal berubah jadi",
                    "    diawali (.venv), dan perintah python serta pip sekarang",
                    "    menunjuk ke dalam folder itu.",
                    "",
                    "  python -m pip install ...",
                    "    Memasang paket ke environment yang aktif. Memanggil pip",
                    "    lewat python -m menjamin pip-nya milik Python yang sama.",
                    "",
                    "  python -m pip freeze > requirements.txt",
                    "    Mencatat semua paket beserta versi persisnya ke sebuah",
                    "    berkas teks. Berkas inilah yang disimpan di Git, supaya",
                    "    orang lain bisa membuat environment yang sama.",
                    "",
                    "Folder .venv sendiri jangan dimasukkan ke Git. Ukurannya bisa",
                    "ratusan MB dan isinya terikat ke komputer yang membuatnya.",
                    "Tambahkan baris .venv/ ke berkas .gitignore. Jangan pernah",
                    "memakai sudo pip install, karena itu mencampur paketmu dengan",
                    "paket milik sistem Fedora.",
                ],
            },
            {
                "heading": "Python mana yang sedang jalan?",
                "code": """import sys

print("Python       :", sys.executable)
print("di dalam venv:", sys.prefix != sys.base_prefix)""",
            },
            {
                "body": [
                    "Jalankan program ini di terminal yang environment-nya aktif,",
                    "lalu di terminal biasa. Jalurnya berbeda di tiap komputer, jadi",
                    "nggak ada keluaran pasti yang bisa ditulis di sini. Yang",
                    "penting baris kedua: True artinya kamu di dalam environment.",
                    "",
                    "Jebakan: \"Aku sudah pip install pandas, kok masih",
                    "ModuleNotFoundError?\" Hampir selalu jawabannya: pandas",
                    "terpasang di environment A, sedangkan kode dijalankan dengan",
                    "Python dari environment B. Ini sering terjadi di VS Code dan",
                    "Jupyter, yang punya pilihan interpreter atau kernel sendiri.",
                    "Cetak sys.executable untuk memastikan Python mana yang sedang",
                    "dipakai.",
                ],
            },
            {
                "heading": "conda, Anaconda, dan Miniforge",
                "body": [
                    "conda adalah pengelola paket dan environment yang populer di",
                    "dunia data. Bedanya dengan pip: pip memasang paket Python dari",
                    "PyPI, sedangkan conda bisa memasang paket apa saja, termasuk",
                    "pustaka C, compiler, R, dan CUDA untuk GPU. Paket yang susah",
                    "dipasang lewat pip karena butuh pustaka sistem, misalnya",
                    "pustaka pengolah data peta, biasanya mulus lewat conda. Versi",
                    "terbaru saat materi ini ditulis adalah conda 26.9.3 (14",
                    "Oktober 2026).",
                    "",
                    "Nama-nama di sekitarnya sering tertukar:",
                    "",
                    "  Anaconda      installer besar berisi conda plus ratusan paket",
                    "                data science, mengambil dari repositori Anaconda",
                    "  Miniconda     installer kecil, cuma conda dan Python, juga",
                    "                mengambil dari repositori Anaconda",
                    "  Miniforge     installer kecil yang memakai channel",
                    "                conda-forge, gratis untuk siapa pun",
                    "  conda-forge   kumpulan paket conda yang dirawat komunitas",
                    "",
                    "Jebakan: repositori Anaconda nggak gratis untuk semua orang.",
                    "Menurut syarat layanannya, pemakaian gratis berlaku untuk",
                    "perorangan yang memakainya untuk keperluan pribadi nonkomersial,",
                    "perusahaan dengan paling banyak 200 karyawan, serta lembaga",
                    "pendidikan dan nirlaba yang memenuhi syarat. Perusahaan yang",
                    "lebih besar wajib berlangganan. Aturan ini juga berlaku kalau",
                    "kamu memakai Miniconda. Miniforge dengan conda-forge nggak",
                    "terkena aturan itu, jadi Miniforge pilihan aman untuk kerja",
                    "kantoran. Syarat layanan bisa berubah, jadi baca versi",
                    "terbarunya kalau ragu.",
                ],
            },
            {
                "heading": "Environment conda dari berkas (environment.yml)",
                "bahasa": "yaml",
                "code": """name: analisis
channels:
  - conda-forge
dependencies:
  - python=3.13
  - pandas
  - matplotlib
  - jupyterlab""",
            },
            {
                "heading": "Perintah conda yang paling sering dipakai",
                "bahasa": "terminal",
                "code": """bash Miniforge3-Linux-x86_64.sh   # installer dari GitHub conda-forge/miniforge
conda env create -f environment.yml
conda activate analisis
conda install scipy
conda env export --from-history > environment.yml
conda deactivate""",
            },
            {
                "body": [
                    "Jadi pakai yang mana? Untuk kurikulum ini, venv plus pip sudah",
                    "cukup: semua paket yang dipakai (pandas, NumPy, Matplotlib,",
                    "SciPy) tersedia lengkap di PyPI. Pilih conda lewat Miniforge",
                    "kalau proyekmu butuh paket dengan pustaka non-Python, atau",
                    "timmu sudah memakai conda. Ada juga uv, pengelola paket buatan",
                    "Astral yang ditulis dengan Rust dan makin sering dipakai karena",
                    "jauh lebih cepat dari pip; perintahnya mirip, misalnya",
                    "uv venv dan uv pip install.",
                    "",
                    "Ingat: kalau terpaksa mencampur conda dan pip di satu",
                    "environment, pasang paket conda dulu, baru pip. Kebalikannya",
                    "sering membuat conda menimpa paket yang dipasang pip. Hindari",
                    "juga memasang semuanya di environment base bawaan conda; buat",
                    "environment baru per proyek.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Repositori analisis data di GitHub hampir selalu menyertakan",
                    "requirements.txt, environment.yml, atau pyproject.toml. Berkas",
                    "itu yang memungkinkan orang lain menjalankan analisis yang sama",
                    "bertahun-tahun kemudian. Banyak perusahaan juga mengganti",
                    "Anaconda dengan Miniforge sesudah aturan lisensinya berubah.",
                    "",
                    "Kasus kecil: kamu mewarisi notebook analisis dari kakak",
                    "tingkat. Isinya import pandas dan matplotlib, tanpa catatan",
                    "versi. Begitu dijalankan dengan pandas 3.0, beberapa sel",
                    "error atau memberi angka berbeda.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat environment baru khusus proyek ini supaya proyekmu",
                    "     yang lain nggak ikut terganggu:",
                    "       python3 -m venv .venv",
                    "       source .venv/bin/activate",
                    "  2. Lihat tanggal berkasnya, lalu pasang versi pandas yang",
                    "     berlaku saat itu, misalnya pandas versi 2.2:",
                    "       python -m pip install \"pandas<3\" matplotlib",
                    "  3. Jalankan Restart and Run All. Kalau sudah lolos, catat",
                    "     versinya dengan pip freeze > requirements.txt.",
                    "  4. Sesudah itu baru perbarui kodenya ke pandas 3.0 sedikit",
                    "     demi sedikit, sambil membandingkan angkanya.",
                ],
            },
        ],
    },
    {
        "title": "7. Spreadsheet sebagai Alat Analisis Pertama",
        "sections": [
            {
                "body": [
                    "Sebelum Python, sebelum SQL, analisis data di kebanyakan kantor",
                    "dimulai di spreadsheet: Microsoft Excel atau Google Sheets.",
                    "Data sering datang sebagai berkas .xlsx, dan atasanmu mungkin",
                    "minta hasilnya dalam bentuk yang sama. Peta belajar Data",
                    "Analyst di roadmap.sh pun memasukkan Excel: rumus IF, rumus",
                    "pencarian, pivot table, dan grafik.",
                    "",
                    "Excel versi desktop nggak tersedia untuk Linux. Di Fedora kamu",
                    "bisa memakai LibreOffice Calc, Google Sheets di browser, atau",
                    "Excel versi web yang gratis dengan akun Microsoft walaupun",
                    "fiturnya lebih sedikit. Rumus dan pivot table di materi ini",
                    "ada di ketiganya.",
                ],
            },
            {
                "heading": "Rumus yang paling sering dipakai",
                "bahasa": "teks",
                "code": """=IF(D2>=5; "grosir"; "eceran")
=VLOOKUP(B2; Produk!A:C; 3; FALSE)
=XLOOKUP(B2; Produk!A:A; Produk!C:C)
=SUMIF(B:B; "K01"; E:E)
=COUNTIF(F:F; "grosir")""",
            },
            {
                "body": [
                    "Artinya, berurutan dari atas:",
                    "",
                    "  1. Kalau jumlah beli di D2 lima atau lebih, tulis grosir,",
                    "     kalau nggak, eceran.",
                    "  2. Cari kode produk dari B2 di kolom pertama sheet Produk,",
                    "     lalu ambil isi kolom ketiganya, yaitu harga.",
                    "  3. Sama dengan nomor 2, tapi dengan fungsi yang lebih baru.",
                    "     Kolom yang dicari dan kolom yang diambil disebut terpisah,",
                    "     jadi nggak terikat urutan kolom.",
                    "  4. Jumlahkan kolom E di semua baris yang kodenya K01.",
                    "  5. Hitung berapa baris yang kolom F-nya bertuliskan grosir.",
                    "",
                    "Jebakan: argumen terakhir rumus nomor 2 harus FALSE supaya",
                    "kodenya dicari persis. Tanpa itu, rumusnya memakai pencocokan",
                    "kira-kira yang mengandaikan kolomnya urut, dan kalau nggak",
                    "urut, ia mengembalikan harga produk lain tanpa pesan error apa",
                    "pun.",
                    "",
                    "Pemisah argumen tergantung pengaturan bahasa. Excel dan Google",
                    "Sheets dengan format Indonesia memakai titik koma, karena koma",
                    "dipakai sebagai tanda desimal. Tutorial berbahasa Inggris",
                    "menulis koma: =IF(D2>=5, \"grosir\", \"eceran\"). Kalau rumus",
                    "salinan dari internet ditolak, ganti dulu pemisahnya.",
                    "",
                    "Saat rumus disalin ke bawah, alamat sel ikut bergeser: D2",
                    "jadi D3, D4, dan seterusnya. Tanda dolar mengunci alamatnya,",
                    "misalnya $H$1 untuk sel tarif pajak yang dipakai semua baris.",
                ],
            },
            {
                "heading": "Pivot table",
                "body": [
                    "Pivot table adalah fitur untuk meringkas tabel panjang tanpa",
                    "menulis rumus. Kamu memilih kolom mana yang jadi baris, mana",
                    "yang jadi kolom, dan angka apa yang dijumlahkan. Misalnya",
                    "baris = produk, kolom = bulan, nilai = jumlah omzet.",
                    "Spreadsheet mengelompokkan dan menjumlahkan sendiri.",
                    "",
                    "Kalau kamu sudah belajar SQL, pivot table itu GROUP BY dengan",
                    "tampilan dua arah. Program di bawah membuat pivot yang sama",
                    "dengan Python biasa: dict sebagai pengganti rumus pencarian,",
                    "dan dict berkunci pasangan (produk, bulan) sebagai pengganti",
                    "pivot.",
                ],
            },
            {
                "heading": "Pivot table dengan Python",
                "code": "import csv\nimport io\nfrom collections import defaultdict\n\npenjualan = io.StringIO(\"\"\"tanggal,kode,qty\n2026-09-02,K01,3\n2026-09-02,T02,5\n2026-09-15,K01,2\n2026-10-01,R03,4\n2026-10-03,T02,1\n2026-10-09,K01,6\n\"\"\")\nproduk = {\n    \"K01\": (\"Kopi susu\", 18000),\n    \"T02\": (\"Teh tarik\", 15000),\n    \"R03\": (\"Roti bakar\", 22000),\n}\n\npivot = defaultdict(int)  # (nama produk, bulan) -> omzet\nfor b in csv.DictReader(penjualan):\n    nama, harga = produk[b[\"kode\"]]      # padanan VLOOKUP\n    bulan = b[\"tanggal\"][:7]             # \"2026-09\"\n    pivot[(nama, bulan)] += harga * int(b[\"qty\"])\n\nsemua_bulan = sorted({bln for _, bln in pivot})\nsemua_nama = sorted({nama for nama, _ in pivot})\nprint(f\"{'produk':<11}\" + \"\".join(f\"{bln:>9}\" for bln in semua_bulan) + f\"{'total':>9}\")\nfor nama in semua_nama:\n    angka = [pivot.get((nama, bln), 0) for bln in semua_bulan]\n    print(f\"{nama:<11}\" + \"\".join(f\"{x:>9}\" for x in angka) + f\"{sum(angka):>9}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  produk       2026-09  2026-10    total",
                    "  Kopi susu      90000   108000   198000",
                    "  Roti bakar         0    88000    88000",
                    "  Teh tarik      75000    15000    90000",
                    "",
                    "Roti bakar di bulan September berisi 0 karena memang nggak ada",
                    "penjualannya. pivot.get(kunci, 0) menangani sel kosong itu,",
                    "sama seperti pivot table yang membiarkan selnya kosong. Dalam",
                    "SQL, hasil yang sama datang dari GROUP BY produk, bulan.",
                    "",
                    "Hasilnya memang sama dengan pivot table, tapi bedanya penting:",
                    "program ini bisa dijalankan ulang minggu depan dengan data",
                    "baru, dan hasilnya pasti dihitung dengan cara yang sama.",
                ],
            },
            {
                "heading": "Jebakan: Excel mengubah datamu sendiri",
                "body": [
                    "Excel mencoba menebak jenis isi sel saat kamu mengetik atau",
                    "membuka berkas CSV, dan tebakannya sering merusak data:",
                    "",
                    "  - Nomor HP 081234567890 kehilangan angka nol di depan dan",
                    "    jadi 81234567890.",
                    "  - NIK 16 digit berubah jadi 3,27409E+15, dan digit",
                    "    terakhirnya diganti 0. Excel cuma menyimpan 15 digit angka",
                    "    yang berarti, jadi digit ke-16 hilang untuk selamanya.",
                    "  - Teks seperti 1-2 atau MARCH1 berubah jadi tanggal. Kasus",
                    "    ini sampai membuat lembaga penamaan gen manusia (HGNC)",
                    "    mengganti nama beberapa gen pada 2020, misalnya MARCH1",
                    "    jadi MARCHF1, supaya nggak terus dirusak spreadsheet.",
                    "",
                    "Cara mencegahnya: jangan buka CSV dengan klik dua kali. Pakai",
                    "menu impor (Data lalu From Text/CSV) dan atur kolom nomor HP,",
                    "NIK, dan kode jadi Text sebelum dimuat. Excel untuk Microsoft",
                    "365 versi baru juga punya pengaturan untuk mematikan sebagian",
                    "konversi otomatis ini di File, Options, Data. Di Python,",
                    "baca kolom seperti itu sebagai teks (str), jangan int.",
                ],
            },
            {
                "heading": "Kapan pindah ke Python",
                "body": [
                    "Spreadsheet tetap alat yang bagus untuk melihat data sekilas",
                    "dan berbagi hasil dengan orang yang nggak menulis kode. Tapi",
                    "ada tanda-tanda kamu sudah butuh alat lain:",
                    "",
                    "  - Datanya besar. Satu sheet Excel paling banyak memuat",
                    "    1.048.576 baris, dan Google Sheets paling banyak 10 juta",
                    "    sel per berkas. Jauh sebelum batas itu, berkasnya sudah",
                    "    terasa berat.",
                    "  - Pekerjaannya berulang. Laporan yang tiap minggu dibuat",
                    "    dengan klik yang sama lebih cepat dan lebih jarang salah",
                    "    kalau ditulis jadi skrip.",
                    "  - Hasilnya harus bisa diperiksa. Klik dan seret di",
                    "    spreadsheet nggak tercatat, sedangkan kode bisa dibaca",
                    "    ulang, disimpan di Git, dan dijalankan orang lain.",
                    "  - Datanya dari banyak berkas atau banyak sumber yang harus",
                    "    digabung.",
                    "",
                    "Bab 04 membahas pandas, pustaka Python yang memang dibuat untuk",
                    "pekerjaan spreadsheet dalam skala yang lebih besar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bagian keuangan, gudang, dan penjualan di banyak perusahaan",
                    "masih bertukar laporan dalam bentuk berkas Excel. Analis data",
                    "pemula sering mendapat tugas pertama berupa merapikan atau",
                    "menggabungkan berkas-berkas seperti itu, lalu menjadikannya",
                    "skrip supaya nggak dikerjakan manual tiap minggu.",
                    "",
                    "Kasus kecil: bagian HRD mengirim CSV data karyawan untuk",
                    "dicocokkan dengan data BPJS. Begitu dibuka di Excel, kolom NIK",
                    "tampil sebagai 3,27409E+15 dan nomor HP kehilangan angka nol.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jangan simpan berkas yang sudah rusak itu. Minta ulang",
                    "     berkas aslinya kalau sempat tersimpan.",
                    "  2. Di Excel, impor lewat Data lalu From Text/CSV, dan atur",
                    "     kolom NIK dan nomor HP sebagai Text.",
                    "  3. Di Python, baca semua kolom sebagai teks lewat modul csv,",
                    "     lalu cek panjang NIK-nya:",
                    "       salah = [b for b in baris if len(b[\"nik\"]) != 16]",
                    "  4. Laporkan berapa baris yang NIK-nya nggak 16 digit sebelum",
                    "     data dicocokkan.",
                ],
            },
        ],
    },
    {
        "title": "8. NumPy: Larik N-Dimensi dan Broadcasting",
        "sections": [
            {
                "body": [
                    "List Python nggak dibuat untuk berhitung. Coba kalikan list",
                    "harga dengan 2: yang kamu dapat list yang diulang dua kali,",
                    "harganya sendiri nggak berubah. Untuk mengalikan tiap",
                    "angka, kamu butuh perulangan, dan perulangan Python terasa",
                    "lambat begitu angkanya jutaan.",
                    "",
                    "NumPy menyelesaikan dua masalah itu. Isinya satu jenis objek",
                    "utama, ndarray (N-dimensional array), yaitu larik: kisi angka",
                    "yang semuanya bertipe sama dan tersimpan berdampingan di",
                    "memori. Operasi seperti kali, tambah, atau rata-rata",
                    "dikerjakan sekaligus oleh kode C di dalam NumPy, tanpa",
                    "perulangan Python.",
                    "",
                    "Hampir semua pustaka data di Python berdiri di atas NumPy:",
                    "pandas, SciPy, Matplotlib, scikit-learn. Di Survei Stack",
                    "Overflow 2024, NumPy dipakai 21,2 persen responden, dan di",
                    "Python Developers Survey 2024 (PSF dan JetBrains) 75 persen",
                    "orang yang mengolah data memakainya. Versi terbaru saat materi",
                    "ini ditulis adalah NumPy 2.5.4 (10 Oktober 2026). Pasang dengan",
                    "pip install numpy di environment proyekmu.",
                ],
            },
            {
                "heading": "List dan larik, berdampingan",
                "code": """import numpy as np

harga = [10000, 25000, 8000]
print(harga * 2)

h = np.array(harga)
print(h * 2)
print(h.dtype, h.shape, h.ndim)

nilai = np.array([[80, 75, 90],
                  [60, 85, 70]])
print(nilai.shape)
print(nilai.mean(axis=0))
print(nilai.mean(axis=1))""",
            },
            {
                "body": [
                    "Keluarannya (dijalankan dengan NumPy 2.5.4):",
                    "  [10000, 25000, 8000, 10000, 25000, 8000]",
                    "  [20000 50000 16000]",
                    "  int64 (3,) 1",
                    "  (2, 3)",
                    "  [70. 80. 80.]",
                    "  [81.66666667 71.66666667]",
                    "",
                    "Larik dicetak tanpa koma, jadi kamu bisa langsung membedakannya",
                    "dari list. Tiga atribut yang paling sering dicek:",
                    "",
                    "  - dtype: tipe semua isinya. int64 artinya bilangan bulat 64",
                    "    bit; float64 untuk pecahan.",
                    "  - shape: ukuran tiap dimensi. (3,) artinya satu dimensi",
                    "    berisi 3 angka, (2, 3) artinya 2 baris dan 3 kolom.",
                    "  - ndim: banyaknya dimensi.",
                    "",
                    "Larik nilai berisi nilai dua siswa untuk tiga mata pelajaran.",
                    "axis=0 artinya hitung menyusuri baris, jadi hasilnya rata-rata",
                    "per kolom (per mata pelajaran). axis=1 menyusuri kolom, jadi",
                    "hasilnya rata-rata per baris (per siswa). Kalau bingung,",
                    "ingat bahwa axis yang disebut adalah dimensi yang hilang dari",
                    "hasilnya.",
                ],
            },
            {
                "heading": "Broadcasting: larik beda ukuran bisa dihitung bareng",
                "code": """import numpy as np

nilai = np.array([[80, 75, 90],
                  [60, 85, 70]])
print(nilai + 5)                   # bonus 5 untuk semua sel

bobot = np.array([0.3, 0.3, 0.4])  # bentuk (3,)
print((nilai * bobot).sum(axis=1)) # nilai akhir per siswa

koreksi = np.array([[2], [-3]])    # bentuk (2, 1)
print(nilai + koreksi)

nilai + np.array([1, 2])           # bentuk (2,): galat""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  [[85 80 95]",
                    "   [65 90 75]]",
                    "  [82.5 71.5]",
                    "  [[82 77 92]",
                    "   [57 82 67]]",
                    "  ValueError: operands could not be broadcast together with",
                    "  shapes (2,3) (2,)",
                    "",
                    "Broadcasting adalah aturan NumPy untuk menghitung dua larik",
                    "yang ukurannya beda. Larik yang lebih kecil seolah diulang",
                    "sampai ukurannya sama, tanpa ikut disalin di memori.",
                    "Angka 5 diulang ke enam sel. Bobot (3,) diulang untuk tiap",
                    "baris. Koreksi (2, 1) diulang ke tiap kolom, jadi siswa",
                    "pertama dapat +2 dan siswa kedua -3 di semua pelajaran.",
                    "",
                    "Aturannya: jajarkan shape dari kanan. Tiap pasangan dimensi",
                    "harus sama, atau salah satunya 1. Dimensi yang nggak ada",
                    "dianggap 1. Shape (2, 3) dengan (2,) gagal karena yang",
                    "dijajarkan di kanan adalah 3 dan 2. Program Python biasa di",
                    "bawah memeriksa aturan itu, jadi kamu bisa mencobanya tanpa",
                    "NumPy.",
                ],
            },
            {
                "heading": "Aturan broadcasting dalam Python biasa",
                "code": """def bisa_broadcast(bentuk_a, bentuk_b):
    a, b = list(bentuk_a), list(bentuk_b)
    while len(a) < len(b):
        a.insert(0, 1)
    while len(b) < len(a):
        b.insert(0, 1)
    hasil = []
    for x, y in zip(a, b):
        if x == y or x == 1 or y == 1:
            hasil.append(max(x, y))
        else:
            return None
    return tuple(hasil)


pasangan = [
    ((2, 3), ()),
    ((2, 3), (3,)),
    ((2, 3), (2, 1)),
    ((2, 3), (2,)),
    ((4, 1), (1, 5)),
]
for a, b in pasangan:
    hasil = bisa_broadcast(a, b)
    print(f"{str(a):<7} dengan {str(b):<7} -> {hasil if hasil else 'galat'}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  (2, 3)  dengan ()      -> (2, 3)",
                    "  (2, 3)  dengan (3,)    -> (2, 3)",
                    "  (2, 3)  dengan (2, 1)  -> (2, 3)",
                    "  (2, 3)  dengan (2,)    -> galat",
                    "  (4, 1)  dengan (1, 5)  -> (4, 5)",
                    "",
                    "Baris terakhir menarik: kolom (4, 1) dan baris (1, 5)",
                    "menghasilkan kisi 4 x 5. Cara ini sering dipakai untuk membuat",
                    "tabel semua pasangan, misalnya jarak antara 4 toko dan 5",
                    "gudang, dalam satu operasi.",
                ],
            },
            {
                "heading": "View dan copy",
                "code": """import numpy as np

a = np.array([1, 2, 3, 4, 5])
potong = a[1:4]
potong[0] = 99
print(a)

salin = a[1:4].copy()
salin[0] = -1
print(a, salin)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  [ 1 99  3  4  5]",
                    "  [ 1 99  3  4  5] [-1  3  4]",
                    "",
                    "Di list Python, a[1:4] selalu membuat salinan. Di NumPy, irisan",
                    "seperti a[1:4] adalah view: jendela ke data milik a, tanpa",
                    "salinan. Mengubah potong berarti mengubah a. Ini disengaja",
                    "supaya mengiris larik berukuran gigabyte nggak menghabiskan",
                    "memori, tapi bagi pemula efeknya mengejutkan. Pakai .copy()",
                    "kalau kamu ingin data yang berdiri sendiri. Pengindeksan",
                    "dengan daftar indeks atau syarat, misalnya a[a > 2], selalu",
                    "menghasilkan salinan.",
                    "",
                    "Jebakan: dtype bilangan bulat bisa meluap tanpa error. Larik",
                    "int8 cuma muat -128 sampai 127, jadi 100 + 100 jadi -56. Foto",
                    "biasanya disimpan sebagai uint8 (0 sampai 255), jadi piksel",
                    "250 ditambah 10 jadi 4, bukan 260. NumPy cuma memberi",
                    "peringatan untuk sebagian kasus, dan kadang nggak sama sekali.",
                ],
            },
            {
                "heading": "NumPy 2 dan tutorial lama",
                "body": [
                    "NumPy 2.0 dirilis pertengahan 2024 dan sengaja memutus sebagian",
                    "kebiasaan NumPy 1.x. Kode dari tutorial atau jawaban forum",
                    "sebelum 2024 bisa gagal dengan cara-cara ini:",
                    "",
                    "  - Nama lama dihapus. np.float_ diganti np.float64, np.NaN",
                    "    diganti np.nan, dan np.Inf diganti np.inf. Pesan error-nya",
                    "    biasanya langsung menyebut penggantinya.",
                    "  - Tampilan angka berubah. np.float64(3.0) sekarang dicetak",
                    "    apa adanya sebagai np.float64(3.0) di dalam list atau",
                    "    repr, jadi keluaran di tutorial lama yang cuma menulis 3.0",
                    "    kelihatan beda.",
                    "  - Aturan tipe berubah. np.uint8(200) + 100 dulu memberi 300",
                    "    bertipe int64. Sekarang hasilnya tetap uint8, yaitu 44,",
                    "    disertai peringatan overflow.",
                    "  - Paket yang dikompilasi untuk NumPy 1.x berhenti dengan pesan",
                    "    \"A module that was compiled using NumPy 1.x cannot be run",
                    "    in NumPy 2.x\". Obatnya memperbarui paket itu, atau",
                    "    sementara memasang numpy<2 di environment terpisah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Foto di komputer adalah larik NumPy berbentuk (tinggi, lebar,",
                    "3): tiap piksel tiga angka uint8 untuk merah, hijau, dan biru.",
                    "Pustaka gambar seperti Pillow dan OpenCV bisa menyerahkan foto",
                    "sebagai larik, dan aplikasi pengolah foto mencerahkan gambar",
                    "dengan broadcasting, satu angka ditambahkan ke jutaan piksel.",
                    "",
                    "Kasus kecil: kamu menulis skrip untuk mencerahkan foto produk",
                    "dengan foto + 60. Hasilnya aneh: bagian yang tadinya paling",
                    "terang malah jadi gelap.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek dtype larik foto. Hasilnya uint8, jadi piksel 200 + 60",
                    "     meluap jadi 4.",
                    "  2. Ubah dulu ke tipe yang lebih lebar sebelum dijumlah:",
                    "       lebar = foto.astype(np.int16) + 60",
                    "  3. Potong nilainya supaya tetap di rentang 0 sampai 255, lalu",
                    "     kembalikan ke uint8:",
                    "       terang = np.clip(lebar, 0, 255).astype(np.uint8)",
                    "  4. Coba di larik kecil dulu, misalnya [[200, 250], [30, 90]].",
                    "     Hasil yang benar [[255, 255], [90, 150]], bukan",
                    "     [[4, 54], [90, 150]].",
                ],
            },
        ],
    },
    {
        "title": "9. Vektor, Matriks, dan Gradien",
        "sections": [
            {
                "body": [
                    "Materi ini membekali dua hal yang nanti dipakai terus di",
                    "kurikulum AI & Machine Learning: perkalian matriks dan",
                    "gradient descent. Matematikanya diambil seperlunya saja, dan",
                    "tiap konsep langsung ditulis jadi kode.",
                    "",
                    "Vektor adalah deretan angka yang menggambarkan satu hal.",
                    "Seorang pelanggan bisa digambarkan sebagai [umur, belanja",
                    "per bulan, jumlah kunjungan]. Matriks adalah tabel angka:",
                    "kumpulan vektor yang ditumpuk jadi baris-baris.",
                    "",
                    "Operasi paling dasar antara dua vektor adalah dot product:",
                    "kalikan pasangan angka di posisi yang sama, lalu jumlahkan.",
                    "Contohnya pesanan [2, 1, 0] dan harga [18000, 15000, 22000].",
                    "Dot product-nya 2 x 18000 + 1 x 15000 + 0 x 22000 = 51000,",
                    "yaitu total tagihan.",
                ],
            },
            {
                "heading": "Dot product dan perkalian matriks",
                "code": """def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def matmul(A, B):
    kolom_B = list(zip(*B))
    return [[dot(baris, kol) for kol in kolom_B] for baris in A]


harga = [18000, 15000, 22000]   # kopi, teh, roti
pesanan = [[2, 1, 0],           # meja 1
           [0, 3, 2]]           # meja 2
print("tagihan:", [dot(p, harga) for p in pesanan])

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
print("A x B =", matmul(A, B))
print("B x A =", matmul(B, A))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tagihan: [51000, 89000]",
                    "  A x B = [[19, 22], [43, 50]]",
                    "  B x A = [[23, 34], [31, 46]]",
                    "",
                    "Perkalian matriks adalah dot product berulang: sel baris i",
                    "kolom j di hasil = dot product baris i dari A dengan kolom j",
                    "dari B. Sel kiri atas 1 x 5 + 2 x 7 = 19. zip(*B) membalik B",
                    "supaya kolom-kolomnya bisa diambil satu per satu.",
                    "",
                    "Dua hal yang sering bikin bingung:",
                    "",
                    "  - Urutan berpengaruh. A x B dan B x A hasilnya beda.",
                    "  - Ukurannya harus nyambung. Matriks m x n cuma bisa dikali",
                    "    dengan matriks n x p, dan hasilnya m x p. Banyak kolom",
                    "    di kiri harus sama dengan banyak baris di kanan.",
                    "",
                    "Di NumPy, perkalian matriks ditulis dengan operator @, dan",
                    "hasilnya sama dengan fungsi buatan kita:",
                    "",
                    "  np.array(pesanan) @ np.array(harga)   ->  [51000 89000]",
                    "  np.array(A) @ np.array(B)             ->  [[19 22] [43 50]]",
                    "",
                    "Jebakan: A * B di NumPy mengalikan sel per sel, hasilnya",
                    "[[5 12] [21 32]]. Itu bukan perkalian matriks. Kalau yang kamu",
                    "maksud perkalian matriks, pakai @.",
                ],
            },
            {
                "heading": "Turunan dan gradien",
                "body": [
                    "Turunan sebuah fungsi di satu titik adalah kemiringannya di",
                    "titik itu: kalau x digeser sedikit, f(x) berubah seberapa",
                    "banyak dan ke arah mana. Untuk f(x) = x kuadrat, turunannya",
                    "2x, jadi di x = 3 kemiringannya 6. Turunan bisa juga",
                    "diperkirakan tanpa rumus, cukup dengan menggeser x sedikit:",
                    "",
                    "  turunan kira-kira = (f(x + h) - f(x - h)) / (2 x h)",
                    "  dengan h angka kecil, misalnya 0,000001",
                    "",
                    "Kalau fungsinya punya banyak masukan, turunan terhadap tiap",
                    "masukan dikumpulkan jadi satu vektor yang disebut gradien.",
                    "Gradien menunjuk arah naik paling curam. Jadi kalau kamu",
                    "ingin turun ke titik terendah, melangkahlah ke arah",
                    "kebalikannya. Itulah gradient descent:",
                    "",
                    "  w_baru = w_lama - laju_belajar x gradien",
                    "",
                    "Laju belajar (learning rate) menentukan seberapa besar",
                    "langkahnya. Di machine learning, w adalah parameter model,",
                    "dan yang diturunkan adalah fungsi galat: seberapa jauh",
                    "tebakan model dari jawaban yang benar.",
                ],
            },
            {
                "heading": "Model terkecil di dunia: y = w x x",
                "code": """x = [1, 2, 3, 4]
y = [2.1, 3.9, 6.2, 7.8]


def galat(w):
    return sum((w * xi - yi) ** 2 for xi, yi in zip(x, y)) / len(x)


def gradien(w):
    return sum(2 * (w * xi - yi) * xi for xi, yi in zip(x, y)) / len(x)


h = 1e-6
print(f"turunan numerik di w=1: {(galat(1 + h) - galat(1 - h)) / (2 * h):.3f}")
print(f"turunan rumus di w=1  : {gradien(1):.3f}")

for laju in (0.001, 0.02, 0.15):
    w = 0.0
    for _ in range(25):
        w = w - laju * gradien(w)
    print(f"laju {laju:<5}: w = {w:.4f}, galat = {galat(w):.4f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  turunan numerik di w=1: -14.850",
                    "  turunan rumus di w=1  : -14.850",
                    "  laju 0.001: w = 0.6262, galat = 13.9744",
                    "  laju 0.02 : w = 1.9897, galat = 0.0243",
                    "  laju 0.15 : w = 528.7386, galat = 2080980.7925",
                    "",
                    "Model ini cuma punya satu parameter, w, dan tugasnya menebak y",
                    "dari x. Galatnya adalah rata-rata kuadrat selisih tebakan dan",
                    "jawaban (mean squared error), mirip kuadrat terkecil di",
                    "materi regresi bab 01. Dua baris pertama menunjukkan rumus",
                    "gradien dan perkiraan numerik memberi angka yang sama, cara",
                    "ampuh untuk mengecek rumus turunan buatanmu sendiri.",
                    "",
                    "Lalu tiga laju belajar, masing-masing 25 langkah dari w = 0:",
                    "",
                    "  - 0,001 terlalu kecil. Sesudah 25 langkah w baru 0,63,",
                    "    masih jauh dari jawabannya.",
                    "  - 0,02 pas. w sampai di 1,99, hampir tepat di titik",
                    "    terendah, dan galatnya turun dari belasan ke 0,02.",
                    "  - 0,15 terlalu besar. Tiap langkah melompati titik terendah",
                    "    makin jauh, sampai w jadi 528 dan galatnya meledak.",
                    "",
                    "Memilih laju belajar memang bagian dari pekerjaan melatih",
                    "model. Pustaka seperti PyTorch menghitung gradien secara",
                    "otomatis untuk jutaan parameter, tapi langkah yang dilakukan",
                    "persis sama dengan perulangan kecil di atas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem rekomendasi di toko online dan layanan musik",
                    "menggambarkan pengguna dan produk sebagai vektor, lalu memakai",
                    "dot product untuk menilai seberapa cocok keduanya. Model",
                    "machine learning, dari regresi sampai model bahasa besar,",
                    "dilatih dengan varian gradient descent yang menghitung",
                    "perkalian matriks raksasa di GPU.",
                    "",
                    "Kasus kecil: toko kue punya tiga cabang. Kamu punya tabel",
                    "jumlah terjual per cabang untuk tiga produk dan daftar harga",
                    "per produk. Pemilik minta omzet tiap cabang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Susun jumlah terjual jadi matriks 3 x 3: baris = cabang,",
                    "     kolom = produk. Susun harga jadi vektor dengan urutan",
                    "     produk yang sama.",
                    "  2. Cek ukurannya: matriks 3 x 3 dikali vektor 3 hasilnya",
                    "     vektor 3, satu angka per cabang.",
                    "  3. Hitung dengan dot product per baris, atau dengan NumPy:",
                    "       omzet = terjual @ harga",
                    "  4. Cocokkan satu cabang dengan hitungan tangan sebelum",
                    "     angkanya dilaporkan. Urutan kolom produk yang tertukar",
                    "     adalah sumber salah yang paling sering.",
                ],
            },
        ],
    },
    {
        "title": "10. SciPy untuk Statistik dan Optimasi",
        "sections": [
            {
                "body": [
                    "NumPy memberi larik dan operasi dasarnya. SciPy memberi",
                    "algoritma ilmiah yang memakai larik itu: uji statistik,",
                    "pencarian nilai terbaik, interpolasi, pengolahan sinyal, dan",
                    "banyak lagi. Algoritmanya sudah diuji puluhan tahun, sebagian",
                    "ditulis dalam C, C++, dan Fortran, jadi kamu nggak perlu",
                    "menulis ulang rumus yang rawan salah.",
                    "",
                    "Versi terbaru saat materi ini ditulis adalah SciPy 1.18.1",
                    "(21 Agustus 2026), berlisensi BSD. Di Python Developers Survey",
                    "2024, 42 persen orang yang melatih model machine learning",
                    "memakainya. Pasang dengan pip install scipy.",
                    "",
                    "SciPy dibagi jadi submodul. Kamu mengimpor yang dibutuhkan",
                    "saja:",
                    "",
                    "  scipy.stats        distribusi peluang dan uji statistik",
                    "  scipy.optimize     mencari minimum, akar, dan kurva terbaik",
                    "  scipy.interpolate  memperkirakan nilai di antara titik data",
                    "  scipy.signal       menghaluskan dan menganalisis sinyal",
                    "  scipy.integrate    integral dan persamaan diferensial",
                    "  scipy.linalg       aljabar linear lanjutan",
                    "  scipy.sparse       matriks yang hampir semua isinya nol",
                    "  scipy.spatial      jarak, tetangga terdekat, bentuk ruang",
                ],
            },
            {
                "heading": "scipy.stats: uji statistik dalam satu baris",
                "code": """from scipy import stats

kelas_a = [78, 85, 69, 90, 74, 88, 81, 79]
kelas_b = [72, 70, 80, 65, 75, 68, 77, 71]

hasil = stats.ttest_ind(kelas_a, kelas_b, equal_var=False)
print(f"t = {hasil.statistic:.3f}, p = {hasil.pvalue:.4f}")
print(f"P(Z < 1.96) = {stats.norm.cdf(1.96):.4f}")""",
            },
            {
                "body": [
                    "Keluarannya (SciPy 1.18.1):",
                    "  t = 2.714, p = 0.0183",
                    "  P(Z < 1.96) = 0.9750",
                    "",
                    "ttest_ind membandingkan rata-rata dua kelompok yang saling",
                    "lepas, di sini dua kelas yang diajar dengan cara berbeda. p",
                    "yang kecil artinya beda rata-rata sebesar itu jarang muncul",
                    "kalau dua cara mengajar itu sama baiknya. Arti p-value",
                    "yang tepat dan jebakannya dibahas di bab 06; sekarang cukup",
                    "tahu letak alatnya.",
                    "",
                    "Jebakan: bawaan ttest_ind adalah equal_var=True, yang",
                    "mengandaikan sebaran kedua kelompok sama. Kalau nggak yakin,",
                    "pakai equal_var=False (uji Welch). Untuk data ini, bawaannya",
                    "memberi p = 0,0168, sedikit berbeda.",
                    "",
                    "Baris kedua sama dengan NormalDist().cdf(1.96) dari modul",
                    "statistics di bab 01. Untuk distribusi sederhana, pustaka",
                    "standar sudah cukup. SciPy berguna saat kamu butuh puluhan",
                    "distribusi lain dan uji statistik yang siap pakai.",
                ],
            },
            {
                "heading": "Optimasi versi mini: mencari harga terbaik",
                "code": """def pendapatan(harga):
    terjual = 1000 - 20 * harga     # makin mahal, makin sedikit
    return harga * terjual


kiri, kanan = 0.0, 50.0
for _ in range(60):
    m1 = kiri + (kanan - kiri) / 3
    m2 = kanan - (kanan - kiri) / 3
    if pendapatan(m1) < pendapatan(m2):
        kiri = m1
    else:
        kanan = m2
terbaik = (kiri + kanan) / 2
print(f"harga terbaik : {terbaik:.2f} ribu")
print(f"pendapatan    : {pendapatan(terbaik):.0f} ribu")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  harga terbaik : 25.00 ribu",
                    "  pendapatan    : 12500 ribu",
                    "",
                    "Optimasi artinya mencari masukan yang membuat sebuah fungsi",
                    "paling besar atau paling kecil. Program di atas memakai",
                    "pencarian ternary: bagi rentang harga jadi tiga, buang",
                    "sepertiga yang pasti bukan tempat puncaknya, ulangi. Cara ini",
                    "cuma bekerja untuk fungsi yang punya satu puncak.",
                    "",
                    "Dengan SciPy, pekerjaan yang sama satu baris. minimize_scalar",
                    "mencari minimum, jadi pendapatan diberi tanda minus supaya",
                    "puncaknya jadi lembah:",
                    "",
                    "  from scipy.optimize import minimize_scalar",
                    "  hasil = minimize_scalar(lambda h: -pendapatan(h),",
                    "                          bounds=(0, 50), method=\"bounded\")",
                    "  print(f\"{hasil.x:.2f}\")   # 25.00",
                    "",
                    "scipy.optimize juga punya minimize untuk fungsi dengan banyak",
                    "masukan, root_scalar untuk mencari akar, dan curve_fit untuk",
                    "mencocokkan rumus ke data.",
                ],
            },
            {
                "heading": "Interpolasi dan sinyal",
                "code": """import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import find_peaks

jam = [6, 9, 12, 18]
suhu = [24.0, 28.5, 32.0, 27.0]
spline = CubicSpline(jam, suhu)
print(f"jam 15, kurva halus : {spline(15):.1f}")
print(f"jam 15, garis lurus : {np.interp(15, jam, suhu):.1f}")

pengunjung = [12, 30, 25, 41, 38, 22, 55, 40]
puncak, _ = find_peaks(pengunjung)
print("puncak di indeks:", puncak)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  jam 15, kurva halus : 32.2",
                    "  jam 15, garis lurus : 29.5",
                    "  puncak di indeks: [1 3 6]",
                    "",
                    "Sensor suhu yang mati jam 15 meninggalkan lubang di data.",
                    "Interpolasi memperkirakan nilainya dari titik-titik di",
                    "sekitarnya. np.interp menarik garis lurus antara jam 12 dan 18,",
                    "jadi tebakannya 29,5. CubicSpline membuat kurva halus, tapi",
                    "tebakannya 32,2, lebih panas dari jam 12 yang tercatat paling",
                    "panas. Kurva halus bisa melampaui data aslinya, jadi selalu",
                    "cek apakah hasilnya masuk akal.",
                    "",
                    "find_peaks dari scipy.signal mencari titik yang lebih tinggi",
                    "dari tetangga kiri dan kanannya: indeks 1, 3, dan 6. Fungsi",
                    "ini punya pilihan seperti height dan distance untuk",
                    "mengabaikan puncak kecil yang cuma derau.",
                    "",
                    "Kapan memakai SciPy dan kapan pustaka lain? Untuk satu uji",
                    "statistik atau satu optimasi, SciPy. Untuk tabel regresi",
                    "lengkap dan model deret waktu, statsmodels (dibahas di bab",
                    "06). Untuk machine learning, scikit-learn di kurikulum AI &",
                    "Machine Learning.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim produk di aplikasi belanja memakai scipy.stats untuk",
                    "membandingkan dua versi halaman, peneliti memakai",
                    "scipy.optimize untuk mencocokkan model ke data percobaan, dan",
                    "insinyur memakai scipy.signal untuk membersihkan data sensor",
                    "getaran mesin atau rekaman suara. Banyak pustaka lain, termasuk",
                    "scikit-learn dan statsmodels, memakai SciPy di dalamnya.",
                    "",
                    "Kasus kecil: kedai ingin tahu harga paket hemat yang memberi",
                    "pendapatan terbesar. Dari uji coba, setiap kenaikan seribu",
                    "rupiah mengurangi penjualan sekitar 20 paket dari 1000 paket.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis hubungan itu jadi fungsi pendapatan(harga), seperti",
                    "     contoh di atas.",
                    "  2. Tentukan rentang yang masuk akal, misalnya 0 sampai 50",
                    "     ribu, karena di atas 50 ribu penjualannya nol.",
                    "  3. Cari puncaknya dengan pencarian ternary atau dengan",
                    "       minimize_scalar(lambda h: -pendapatan(h), bounds=(0, 50),",
                    "                       method=\"bounded\")",
                    "  4. Sampaikan hasilnya sebagai titik awal, bukan kepastian:",
                    "     rumus permintaan itu tebakan dari data uji coba, jadi",
                    "     pantau penjualan sesudah harga baru dipasang.",
                ],
            },
        ],
    },
    {
        "title": "11. pandas: Series, DataFrame, dan Membaca Data",
        "sections": [
            {
                "body": [
                    "pandas adalah pustaka Python untuk mengolah data berbentuk",
                    "tabel. Kalau NumPy itu kisi angka, pandas itu spreadsheet di",
                    "dalam Python: kolom punya nama, baris punya label, dan tiap",
                    "kolom boleh bertipe beda (teks, angka, tanggal).",
                    "",
                    "pandas paling banyak dipakai di ranah ini. Di Python",
                    "Developers Survey 2024 (PSF dan JetBrains), 80 persen orang",
                    "yang mengolah data memakainya, dan di Survei Stack Overflow",
                    "2024 angkanya 20,7 persen dari semua responden. Versi terbaru",
                    "saat materi ini ditulis adalah pandas 3.0.6 (17 September",
                    "2026). Pasang dengan pip install pandas, ditambah openpyxl",
                    "kalau kamu perlu membaca berkas Excel.",
                    "",
                    "Ada dua objek utama:",
                    "",
                    "  - Series: satu kolom data beserta labelnya. Mirip list,",
                    "    tapi tiap nilai punya label.",
                    "  - DataFrame: tabel yang terdiri dari beberapa Series dengan",
                    "    label baris yang sama.",
                    "",
                    "Label baris itu disebut index. Kalau nggak ditentukan, index",
                    "berisi 0, 1, 2, dan seterusnya.",
                ],
            },
            {
                "heading": "DataFrame mini dengan Python biasa",
                "code": "import csv\nimport io\n\ncsv_teks = \"\"\"tanggal,cabang,produk,qty,harga\n2026-10-01,Depok,Kopi susu,3,18000\n2026-10-01,Bogor,Teh tarik,5,15000\n2026-10-02,Depok,Roti bakar,2,22000\n2026-10-02,Depok,Kopi susu,4,18000\n2026-10-03,Bogor,Kopi susu,1,18000\n\"\"\"\nbaris = list(csv.DictReader(io.StringIO(csv_teks)))\n\n# \"DataFrame\" mini: satu list per kolom, semua sepanjang jumlah baris\nkolom = {nama: [b[nama] for b in baris] for nama in baris[0]}\nkolom[\"qty\"] = [int(x) for x in kolom[\"qty\"]]\n\nprint(\"shape:\", (len(baris), len(kolom)))\nprint(\"kolom:\", list(kolom))\nprint(\"rata-rata qty:\", sum(kolom[\"qty\"]) / len(kolom[\"qty\"]))\nprint(\"baris 1, produk:\", kolom[\"produk\"][1])\ndepok = [q for c, q in zip(kolom[\"cabang\"], kolom[\"qty\"]) if c == \"Depok\"]\nprint(\"qty Depok:\", sum(depok))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  shape: (5, 5)",
                    "  kolom: ['tanggal', 'cabang', 'produk', 'qty', 'harga']",
                    "  rata-rata qty: 3.0",
                    "  baris 1, produk: Teh tarik",
                    "  qty Depok: 9",
                    "",
                    "Program ini menyimpan tabel per kolom, bukan per baris, persis",
                    "cara pandas menyimpannya. Tiap kolom satu jenis data, jadi",
                    "menghitung rata-rata qty cukup membaca satu list. Perhatikan",
                    "juga baris yang mengubah qty jadi int: csv selalu membaca teks,",
                    "jadi tipe kolom harus diurus sendiri. pandas melakukan semua",
                    "itu, ditambah ratusan fungsi lain, dalam satu baris.",
                ],
            },
            {
                "heading": "Data yang sama dengan pandas",
                "code": "import io\n\nimport pandas as pd\n\ncsv_teks = \"\"\"tanggal,cabang,produk,qty,harga\n2026-10-01,Depok,Kopi susu,3,18000\n2026-10-01,Bogor,Teh tarik,5,15000\n2026-10-02,Depok,Roti bakar,2,22000\n2026-10-02,Depok,Kopi susu,4,18000\n2026-10-03,Bogor,Kopi susu,1,18000\n\"\"\"\ndf = pd.read_csv(io.StringIO(csv_teks), parse_dates=[\"tanggal\"])\nprint(df.head(3))\nprint(df.shape)\nprint(df.dtypes)\nprint(df[\"qty\"].describe())",
            },
            {
                "body": [
                    "Keluarannya (pandas 3.0.6):",
                    "       tanggal cabang      produk  qty  harga",
                    "  0 2026-10-01  Depok   Kopi susu    3  18000",
                    "  1 2026-10-01  Bogor   Teh tarik    5  15000",
                    "  2 2026-10-02  Depok  Roti bakar    2  22000",
                    "  (5, 5)",
                    "  tanggal    datetime64[us]",
                    "  cabang                str",
                    "  produk                str",
                    "  qty                 int64",
                    "  harga               int64",
                    "  dtype: object",
                    "  count    5.000000",
                    "  mean     3.000000",
                    "  std      1.581139",
                    "  min      1.000000",
                    "  25%      2.000000",
                    "  50%      3.000000",
                    "  75%      4.000000",
                    "  max      5.000000",
                    "  Name: qty, dtype: float64",
                    "",
                    "Kolom paling kiri (0, 1, 2) adalah index. read_csv menebak tipe",
                    "tiap kolom sendiri: qty dan harga jadi int64, cabang dan produk",
                    "jadi str, dan tanggal jadi datetime karena diminta lewat",
                    "parse_dates. Kebiasaan pertama tiap kali memuat data: lihat",
                    "head(), shape, dan dtypes. Kolom angka yang ternyata bertipe",
                    "str adalah tanda ada isi aneh di dalamnya.",
                    "",
                    "describe() memberi ringkasan statistik dari bab 01 dalam satu",
                    "panggilan: jumlah data, rata-rata, simpangan baku (pembagi",
                    "n - 1), minimum, kuartil, dan maksimum.",
                ],
            },
            {
                "heading": "Memilih kolom dan baris: loc dan iloc",
                "code": """# lanjutan contoh sebelumnya: df sudah dibuat dengan read_csv
...
print(df.loc[1, "produk"])                  # label baris 1, kolom produk
print(df.iloc[0, 2])                         # posisi baris 0, kolom ke-2
print(df.loc[0:2, ["cabang", "qty"]])       # label 0 sampai 2, termasuk 2
print(df.iloc[0:2, [1, 3]])                  # posisi 0 dan 1, tanpa 2
print(df[df["cabang"] == "Depok"]["qty"].sum())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Teh tarik",
                    "  Kopi susu",
                    "    cabang  qty",
                    "  0  Depok    3",
                    "  1  Bogor    5",
                    "  2  Depok    2",
                    "    cabang  qty",
                    "  0  Depok    3",
                    "  1  Bogor    5",
                    "  9",
                    "",
                    "df[\"qty\"] mengambil satu kolom sebagai Series, sedangkan",
                    "df[[\"cabang\", \"qty\"]] dengan kurung ganda mengambil beberapa",
                    "kolom sebagai DataFrame. Untuk memilih baris ada dua cara:",
                    "",
                    "  - loc memakai label. loc[0:2] mengambil label 0 sampai 2,",
                    "    termasuk 2.",
                    "  - iloc memakai posisi, seperti indeks list. iloc[0:2]",
                    "    mengambil posisi 0 dan 1, tanpa 2.",
                    "",
                    "Di contoh ini label dan posisi kebetulan sama. Sesudah data",
                    "diurutkan atau disaring, labelnya ikut berpindah, dan di",
                    "situlah loc dan iloc mulai memberi hasil berbeda.",
                    "",
                    "Baris terakhir menyaring dengan syarat. df[\"cabang\"] ==",
                    "\"Depok\" menghasilkan Series berisi True dan False, lalu",
                    "df[...] cuma menyisakan baris yang True. Padanannya di SQL:",
                    "SELECT SUM(qty) FROM df WHERE cabang = 'Depok'.",
                ],
            },
            {
                "heading": "Membaca format lain",
                "body": [
                    "read_csv punya banyak parameter, dan beberapa di antaranya",
                    "penting untuk data dari Indonesia:",
                    "",
                    "  pd.read_csv(\"jual.csv\", sep=\";\", decimal=\",\")",
                    "      CSV hasil ekspor Excel berformat Indonesia biasanya",
                    "      memakai titik koma sebagai pemisah dan koma sebagai",
                    "      tanda desimal.",
                    "  pd.read_csv(\"warga.csv\", dtype={\"nik\": str, \"hp\": str})",
                    "      Kolom NIK dan nomor HP dibaca sebagai teks supaya angka",
                    "      nol di depan dan digit ke-16 nggak hilang.",
                    "  pd.read_excel(\"laporan.xlsx\", sheet_name=\"Oktober\")",
                    "      Membaca satu sheet dari berkas Excel (butuh openpyxl).",
                    "  pd.read_sql(\"SELECT * FROM jual\", koneksi)",
                    "      Menjalankan query ke database, misalnya koneksi",
                    "      sqlite3, dan menerima hasilnya sebagai DataFrame.",
                    "",
                    "Ada juga read_json dan read_parquet. Parquet, format kolom",
                    "yang jauh lebih cepat dari CSV untuk data besar, dibahas di",
                    "bab 07. Untuk menyimpan, pakai pasangannya: to_csv, to_excel,",
                    "to_parquet.",
                ],
            },
            {
                "heading": "pandas 3.0 dan tutorial lama",
                "body": [
                    "pandas 3.0 dirilis 21 Januari 2026 dan membawa perubahan yang",
                    "membuat sebagian tutorial lama menyesatkan:",
                    "",
                    "  - Copy-on-Write jadi perilaku bawaan. Hasil penyaringan atau",
                    "    pemilihan selalu berperilaku seperti salinan, dan pola",
                    "    lama df[\"kolom\"][0] = nilai nggak lagi mengubah df sama",
                    "    sekali. Detailnya di materi berikutnya.",
                    "  - Kolom teks memakai tipe str yang baru, bukan object. Kalau",
                    "    tutorial lama menunjukkan dtypes object untuk kolom nama,",
                    "    di pandas 3 kamu akan melihat str.",
                    "  - Tanggal yang dibaca dari teks kini disimpan dengan",
                    "    ketelitian mikrodetik, makanya muncul datetime64[us].",
                    "  - pandas 3 butuh Python 3.11 atau lebih baru.",
                    "",
                    "Ingat: kalau contoh dari internet memberi hasil berbeda,",
                    "cek dulu pd.__version__ dan tahun tulisannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Analis data di toko online, bank, dan perusahaan logistik",
                    "memakai pandas setiap hari untuk membaca ekspor dari sistem",
                    "lain, mengecek isinya, lalu menyiapkannya untuk laporan atau",
                    "model. Notebook analisis di Kaggle hampir semuanya diawali",
                    "import pandas as pd dan pd.read_csv.",
                    "",
                    "Kasus kecil: bagian keuangan mengirim keuangan_okt.csv hasil",
                    "ekspor Excel. Begitu dibaca dengan pd.read_csv, DataFrame-nya",
                    "cuma punya satu kolom raksasa berisi tulisan seperti",
                    "\"2026-10-01;Depok;1250000,50\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat isi mentahnya. Pemisahnya titik koma dan desimalnya",
                    "     koma, ciri ekspor Excel berformat Indonesia.",
                    "  2. Baca ulang dengan parameter yang cocok:",
                    "       df = pd.read_csv(\"keuangan_okt.csv\", sep=\";\", decimal=\",\")",
                    "  3. Cek df.shape dan df.dtypes. Kolom nominal harus float64,",
                    "     bukan str.",
                    "  4. Bandingkan df[\"nominal\"].sum() dengan total di berkas",
                    "     Excel aslinya sebelum lanjut ke analisis.",
                ],
            },
        ],
    },
    {
        "title": "12. pandas: Membersihkan Data Kotor",
        "sections": [
            {
                "body": [
                    "Data dari dunia nyata hampir nggak pernah rapi. Nama ditulis",
                    "dengan spasi berlebih dan huruf besar kecil acak, satu kota",
                    "punya tiga ejaan, harga ditulis \"Rp15.000\" sebagai teks, ada",
                    "sel kosong, dan ada baris yang tercatat dua kali. Kalau",
                    "langsung dihitung, hasilnya salah tanpa pesan error apa pun.",
                    "",
                    "Urutan yang aman untuk membersihkan data:",
                    "",
                    "  1. Lihat dulu: head(), dtypes, dan isna().sum().",
                    "  2. Rapikan teks: spasi, huruf besar kecil, ejaan.",
                    "  3. Betulkan tipe: teks angka jadi angka, teks tanggal jadi",
                    "     tanggal.",
                    "  4. Buang baris kembar.",
                    "  5. Tangani nilai kosong dan pencilan.",
                    "  6. Hitung ulang jumlah baris, catat berapa yang dibuang.",
                    "",
                    "Urutannya penting. Baris kembar baru kelihatan kembar sesudah",
                    "teksnya dirapikan. Nama \" budi santoso \" dengan spasi di",
                    "ujung dan nama yang sama dalam huruf besar semua dianggap",
                    "beda sebelum di-strip dan disamakan hurufnya.",
                ],
            },
            {
                "heading": "Membersihkan dengan pandas",
                "code": "import io\n\nimport pandas as pd\n\nkotor = \"\"\"nama,kota,harga,tanggal\n budi santoso ,jakarta,Rp15.000,17/08/2026\nSiti Aminah,Jakarta ,Rp22.500,18/08/2026\nBUDI SANTOSO,JKT,Rp15.000,17/08/2026\nRina,Bandung,,19/08/2026\nAgus,bandung,Rp9.000.000,20/08/2026\n\"\"\"\ndf = pd.read_csv(io.StringIO(kotor))\nprint(df.isna().sum())\n\ndf[\"nama\"] = df[\"nama\"].str.strip().str.title()\ndf[\"kota\"] = df[\"kota\"].str.strip().str.title().replace({\"Jkt\": \"Jakarta\"})\ndf[\"harga\"] = pd.to_numeric(\n    df[\"harga\"].str.replace(\"Rp\", \"\").str.replace(\".\", \"\"), errors=\"coerce\")\ndf[\"tanggal\"] = pd.to_datetime(df[\"tanggal\"], format=\"%d/%m/%Y\")\ndf = df.drop_duplicates()\nprint(df)\nprint(df.dtypes)",
            },
            {
                "body": [
                    "Keluarannya (pandas 3.0.6):",
                    "  nama       0",
                    "  kota       0",
                    "  harga      1",
                    "  tanggal    0",
                    "  dtype: int64",
                    "             nama     kota      harga    tanggal",
                    "  0  Budi Santoso  Jakarta    15000.0 2026-08-17",
                    "  1   Siti Aminah  Jakarta    22500.0 2026-08-18",
                    "  3          Rina  Bandung        NaN 2026-08-19",
                    "  4          Agus  Bandung  9000000.0 2026-08-20",
                    "  nama                  str",
                    "  kota                  str",
                    "  harga             float64",
                    "  tanggal    datetime64[us]",
                    "  dtype: object",
                    "",
                    "Yang terjadi baris demi baris:",
                    "",
                    "  - .str memberi akses ke fungsi teks untuk seluruh kolom",
                    "    sekaligus: strip() membuang spasi di ujung, title()",
                    "    membuat huruf pertama tiap kata kapital.",
                    "  - replace({\"Jkt\": \"Jakarta\"}) menyamakan singkatan.",
                    "  - to_numeric mengubah teks jadi angka. errors=\"coerce\"",
                    "    membuat isi yang gagal diubah jadi NaN, bukan menghentikan",
                    "    program.",
                    "  - to_datetime dengan format=\"%d/%m/%Y\" membaca tanggal gaya",
                    "    Indonesia: hari dulu, lalu bulan.",
                    "  - drop_duplicates membuang baris ketiga, yang sesudah",
                    "    dirapikan isinya sama persis dengan baris pertama.",
                    "",
                    "NaN (not a number) adalah tanda nilai kosong di pandas. Kolom",
                    "harga jadi float64 karena NaN cuma bisa disimpan di kolom",
                    "pecahan. Dan perhatikan Agus: 9.000.000 untuk satu transaksi",
                    "kedai jelas pencilan, mungkin salah ketik 9.000. Pembersihan",
                    "belum selesai.",
                ],
            },
            {
                "heading": "Nilai kosong dan pencilan",
                "body": [
                    "Ada tiga pilihan untuk nilai kosong, dan nggak ada yang selalu",
                    "benar:",
                    "",
                    "  df.dropna(subset=[\"harga\"])",
                    "      Buang barisnya. Aman kalau barisnya sedikit dan",
                    "      kosongnya acak.",
                    "  df[\"harga\"].fillna(df[\"harga\"].median())",
                    "      Isi dengan median. Rata-rata tetap masuk akal, tapi",
                    "      sebaran datanya jadi terlihat lebih rapat.",
                    "  df[\"harga_kosong\"] = df[\"harga\"].isna()",
                    "      Tandai dulu, putuskan nanti. Kadang kosongnya sendiri",
                    "      berarti sesuatu, misalnya pelanggan yang menolak mengisi.",
                    "",
                    "Jebakan: mengisi nilai kosong dengan 0 hampir selalu salah.",
                    "Harga kosong artinya nggak diketahui, bukan gratis. Rata-rata",
                    "yang dihitung sesudah fillna(0) jadi lebih rendah dari",
                    "kenyataan.",
                    "",
                    "Untuk pencilan, pakai aturan batas kuartil dari bab 01:",
                    "",
                    "  q1, q3 = df[\"harga\"].quantile([0.25, 0.75])",
                    "  batas = q3 + 1.5 * (q3 - q1)",
                    "  df[df[\"harga\"] > batas]",
                    "",
                    "Lihat baris-baris itu dulu sebelum dibuang. Pencilan bisa salah",
                    "ketik, bisa juga pelanggan grosir yang memang belanja banyak.",
                    "Yang memutuskan adalah pengetahuan tentang datanya, bukan",
                    "rumusnya.",
                ],
            },
            {
                "heading": "Copy-on-Write di pandas 3",
                "code": """import pandas as pd

stok = pd.DataFrame({"produk": ["kopi", "teh"], "jumlah": [5, 0]})

stok["jumlah"][1] = 10          # pola lama: nggak mengubah apa-apa
print(stok)

stok.loc[1, "jumlah"] = 10      # cara yang benar
print(stok)

menipis = stok[stok["jumlah"] < 6]
menipis.loc[:, "jumlah"] = 99   # mengubah salinan, stok aman
print(stok)""",
            },
            {
                "body": [
                    "Keluarannya (dengan peringatan ChainedAssignmentError di baris",
                    "pertama):",
                    "    produk  jumlah",
                    "  0   kopi       5",
                    "  1    teh       0",
                    "    produk  jumlah",
                    "  0   kopi       5",
                    "  1    teh      10",
                    "    produk  jumlah",
                    "  0   kopi       5",
                    "  1    teh      10",
                    "",
                    "stok[\"jumlah\"][1] = 10 disebut chained assignment: dua kurung",
                    "berurutan, yang pertama mengambil kolom, yang kedua mengubah",
                    "isinya. Di pandas 3 dengan Copy-on-Write, langkah pertama",
                    "selalu berperilaku seperti salinan, jadi perubahannya hilang.",
                    "pandas memberi peringatan ChainedAssignmentError yang bilang",
                    "cara ini nggak pernah berhasil. Pakai satu langkah saja:",
                    "stok.loc[baris, kolom] = nilai.",
                    "",
                    "Kabar baiknya, perilakunya sekarang bisa ditebak. Hasil",
                    "penyaringan seperti menipis bisa diubah sesukamu tanpa",
                    "menyentuh stok. Peringatan SettingWithCopyWarning yang dulu",
                    "membingungkan banyak orang sudah dihapus di pandas 3.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem pendaftaran, formulir online, dan aplikasi kasir",
                    "menerima ketikan manusia, jadi datanya selalu perlu",
                    "dibersihkan sebelum dianalisis. Banyak tim data menyimpan",
                    "langkah pembersihan sebagai fungsi atau skrip sendiri supaya",
                    "bisa dijalankan ulang setiap ada data baru.",
                    "",
                    "Kasus kecil: laporan omzet per kota menunjukkan \"Jakarta\",",
                    "\"jakarta\", \"JKT\", dan \"Jakarta \" sebagai empat kota berbeda,",
                    "dan rata-rata transaksi Bandung tiba-tiba 4,5 juta.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat ejaan yang ada dengan df[\"kota\"].value_counts().",
                    "  2. Rapikan dan samakan ejaannya:",
                    "       df[\"kota\"] = df[\"kota\"].str.strip().str.title()",
                    "       df[\"kota\"] = df[\"kota\"].replace({\"Jkt\": \"Jakarta\"})",
                    "  3. Cari pencilan di Bandung dengan batas kuartil, lalu",
                    "     tanyakan ke kasir apakah 9.000.000 itu salah ketik.",
                    "  4. Hitung ulang laporan, dan tulis di bawahnya berapa baris",
                    "     yang dibetulkan atau dibuang beserta alasannya.",
                ],
            },
        ],
    },
    {
        "title": "13. pandas: Group By, Pivot, dan Menggabung Tabel",
        "sections": [
            {
                "body": [
                    "Pertanyaan analisis paling sering berbentuk \"per\": omzet per",
                    "kategori, rata-rata nilai per kelas, jumlah pesanan per",
                    "pelanggan. pandas menjawabnya dengan groupby, yang bekerja",
                    "dalam tiga langkah:",
                    "",
                    "  1. Pecah (split) baris jadi kelompok menurut satu kolom.",
                    "  2. Hitung (apply) sesuatu di tiap kelompok: jumlah,",
                    "     rata-rata, banyaknya.",
                    "  3. Gabungkan (combine) hasilnya jadi satu tabel baru.",
                    "",
                    "Kalau kamu sudah belajar SQL, ini sama dengan GROUP BY.",
                    "Program pertama di bawah memakai sqlite3 bawaan Python, supaya",
                    "kamu bisa melihat hasil yang nanti kita hasilkan lagi dengan",
                    "pandas.",
                ],
            },
            {
                "heading": "GROUP BY di SQLite",
                "code": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"CREATE TABLE jual (bulan TEXT, kategori TEXT, omzet INTEGER)\")\ndb.executemany(\"INSERT INTO jual VALUES (?, ?, ?)\", [\n    (\"2026-09\", \"minuman\", 90000), (\"2026-09\", \"makanan\", 44000),\n    (\"2026-09\", \"minuman\", 75000), (\"2026-10\", \"minuman\", 108000),\n    (\"2026-10\", \"makanan\", 88000), (\"2026-10\", \"makanan\", 22000),\n])\nquery = \"\"\"\nSELECT kategori, SUM(omzet) AS total, ROUND(AVG(omzet)) AS rata,\n       COUNT(*) AS transaksi\nFROM jual\nGROUP BY kategori\nORDER BY total DESC\n\"\"\"\nfor baris in db.execute(query):\n    print(baris)",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ('minuman', 273000, 91000.0, 3)",
                    "  ('makanan', 154000, 51333.0, 3)",
                ],
            },
            {
                "heading": "groupby dan agg di pandas",
                "code": """import pandas as pd

jual = pd.DataFrame({
    "bulan":    ["2026-09", "2026-09", "2026-09", "2026-10", "2026-10", "2026-10"],
    "kategori": ["minuman", "makanan", "minuman", "minuman", "makanan", "makanan"],
    "omzet":    [90000, 44000, 75000, 108000, 88000, 22000],
})

ringkas = (
    jual.groupby("kategori")
        .agg(total=("omzet", "sum"), rata=("omzet", "mean"),
             transaksi=("omzet", "count"))
        .round()
        .sort_values("total", ascending=False)
)
print(ringkas)

tabel = jual.pivot_table(index="kategori", columns="bulan", values="omzet",
                         aggfunc="sum", margins=True, margins_name="Total")
print(tabel)""",
            },
            {
                "body": [
                    "Keluarannya (pandas 3.0.6):",
                    "             total     rata  transaksi",
                    "  kategori",
                    "  minuman   273000  91000.0          3",
                    "  makanan   154000  51333.0          3",
                    "  bulan     2026-09  2026-10   Total",
                    "  kategori",
                    "  makanan     44000   110000  154000",
                    "  minuman    165000   108000  273000",
                    "  Total      209000   218000  427000",
                    "",
                    "agg dengan pasangan nama=(kolom, fungsi) disebut named",
                    "aggregation: kamu menentukan nama kolom hasilnya sendiri,",
                    "mirip AS di SQL. Kolom kategori pindah jadi index tabel hasil.",
                    "Kalau ingin dia kembali jadi kolom biasa, tambahkan",
                    ".reset_index().",
                    "",
                    "pivot_table adalah pivot table spreadsheet dari bab 02:",
                    "index jadi baris, columns jadi kolom, values yang dihitung,",
                    "dan margins=True menambah baris dan kolom total.",
                    "",
                    "Jebakan: kolom bulan diurutkan menurut teksnya. Kalau bulan",
                    "ditulis \"Sep\" dan \"Okt\", urutannya jadi Okt dulu baru Sep,",
                    "karena O lebih dulu dari S di abjad. Simpan bulan sebagai",
                    "\"2026-09\" atau sebagai tanggal supaya urutannya benar.",
                ],
            },
            {
                "heading": "Menggabung dua tabel: merge",
                "code": """import pandas as pd

pelanggan = pd.DataFrame({"id": [1, 2, 3, 4],
                          "nama": ["Ani", "Budi", "Citra", "Dodi"]})
pesanan = pd.DataFrame({"id_pelanggan": [1, 1, 3, 5],
                        "total": [50000, 20000, 75000, 30000]})

dalam = pelanggan.merge(pesanan, left_on="id", right_on="id_pelanggan", how="inner")
kiri = pelanggan.merge(pesanan, left_on="id", right_on="id_pelanggan", how="left")
print(dalam)
print(kiri)
print(len(pelanggan), len(dalam), len(kiri))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "     id   nama  id_pelanggan  total",
                    "  0   1    Ani             1  50000",
                    "  1   1    Ani             1  20000",
                    "  2   3  Citra             3  75000",
                    "     id   nama  id_pelanggan    total",
                    "  0   1    Ani           1.0  50000.0",
                    "  1   1    Ani           1.0  20000.0",
                    "  2   2   Budi           NaN      NaN",
                    "  3   3  Citra           3.0  75000.0",
                    "  4   4   Dodi           NaN      NaN",
                    "  4 3 5",
                    "",
                    "merge adalah JOIN di SQL. how=\"inner\" cuma menyimpan baris",
                    "yang punya pasangan di kedua tabel, jadi Budi, Dodi, dan",
                    "pesanan dari pelanggan 5 hilang. how=\"left\" menyimpan semua",
                    "pelanggan, dan yang nggak punya pesanan diisi NaN. Ada juga",
                    "\"right\" dan \"outer\" dengan arti yang sama seperti di SQL.",
                    "",
                    "Jebakan: lihat angka di baris terakhir. Tabel pelanggan punya",
                    "4 baris, tapi hasil left merge punya 5, karena Ani punya dua",
                    "pesanan. Kalau kunci di tabel kanan nggak unik, baris di kiri",
                    "ikut berlipat. Menjumlahkan kolom milik tabel kiri sesudah",
                    "merge seperti itu menghitung Ani dua kali. Pakai",
                    "validate=\"one_to_one\" atau \"many_to_one\" supaya pandas",
                    "menolak merge yang kuncinya nggak sesuai dugaanmu, dan",
                    "indicator=True untuk melihat baris mana yang nggak punya",
                    "pasangan.",
                ],
            },
            {
                "heading": "Padanan pandas dan SQL",
                "body": [
                    "Kalau kamu lebih lancar SQL, tabel ini membantu menerjemahkan:",
                    "",
                    "  SQL                          pandas",
                    "  WHERE kota = 'Depok'         df[df[\"kota\"] == \"Depok\"]",
                    "  SELECT nama, kota            df[[\"nama\", \"kota\"]]",
                    "  ORDER BY total DESC          df.sort_values(\"total\", ascending=False)",
                    "  GROUP BY kategori + SUM      df.groupby(\"kategori\")[\"omzet\"].sum()",
                    "  INNER JOIN ... ON            a.merge(b, on=\"id\")",
                    "  LEFT JOIN ... ON             a.merge(b, on=\"id\", how=\"left\")",
                    "  COUNT(DISTINCT kota)         df[\"kota\"].nunique()",
                    "  LIMIT 5                      df.head(5)",
                    "",
                    "Mana yang dipilih? Kalau datanya sudah di database dan",
                    "besar, biarkan database yang menghitung, lalu ambil hasilnya",
                    "dengan pd.read_sql. Kalau datanya berkas CSV atau Excel, atau",
                    "kamu butuh langkah yang susah ditulis di SQL seperti",
                    "membersihkan teks, pandas lebih nyaman.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan bulanan di banyak perusahaan dibuat dengan pola yang",
                    "sama: gabungkan tabel transaksi dengan tabel produk atau",
                    "pelanggan, kelompokkan, lalu ringkas jadi tabel pivot. Bagian",
                    "pemasaran memakai hasil yang sama untuk mencari pelanggan yang",
                    "lama nggak belanja, yaitu baris yang tetap kosong sesudah left",
                    "merge.",
                    "",
                    "Kasus kecil: manajer minta total belanja per kota. Kamu",
                    "menggabungkan tabel pesanan dengan tabel pelanggan, dan total",
                    "Depok tiba-tiba dua kali lipat dari laporan kasir.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bandingkan jumlah baris sebelum dan sesudah merge. Kalau",
                    "     bertambah, ada kunci yang kembar.",
                    "  2. Cari kuncinya: pelanggan[\"id\"].duplicated().sum(). Bisa",
                    "     jadi satu pelanggan tercatat dua kali di tabel pelanggan.",
                    "  3. Bersihkan duplikatnya, lalu ulangi merge dengan pagar:",
                    "       pesanan.merge(pelanggan, left_on=\"id_pelanggan\",",
                    "                     right_on=\"id\", validate=\"many_to_one\")",
                    "  4. Baru kelompokkan per kota, dan cocokkan totalnya dengan",
                    "     laporan kasir.",
                ],
            },
        ],
    },
    {
        "title": "14. Matplotlib: Grafik yang Jujur dan Jelas",
        "sections": [
            {
                "body": [
                    "Tabel angka bagus untuk mencari satu nilai. Grafik bagus untuk",
                    "melihat pola: tren yang naik, kelompok yang menonjol, titik",
                    "yang menyimpang. Ingat kuartet Anscombe di bab 01: empat",
                    "kumpulan data dengan rata-rata dan korelasi yang sama, tapi",
                    "bentuknya beda total begitu digambar.",
                    "",
                    "Matplotlib adalah pustaka grafik dasar di Python. Seaborn dan",
                    "fungsi plot() milik pandas dibangun di atasnya, jadi apa yang",
                    "kamu pelajari di sini terpakai juga di sana. Versi terbaru saat",
                    "materi ini ditulis adalah Matplotlib 3.11.2 (11 September",
                    "2026). Pasang dengan pip install matplotlib.",
                    "",
                    "Pilih jenis grafik dari pertanyaannya, bukan dari mana yang",
                    "kelihatan keren:",
                    "",
                    "  Pertanyaan                        Grafik",
                    "  Bagaimana tren dari waktu ke waktu  garis (plot)",
                    "  Kategori mana yang lebih besar    batang (bar)",
                    "  Apakah dua angka berhubungan      sebar (scatter)",
                    "  Bagaimana sebaran satu angka      histogram atau boxplot",
                    "  Berapa bagian dari keseluruhan    batang bertumpuk; pai",
                    "                                    cuma kalau 2-3 bagian",
                ],
            },
            {
                "heading": "Empat grafik dengan gaya fig, ax",
                "code": """from matplotlib import pyplot as plt

bulan = ["Jul", "Agu", "Sep", "Okt"]
omzet = [41.2, 43.5, 42.8, 47.1]          # juta rupiah
suhu = [26, 27, 29, 30, 31, 32, 33, 34]
es_teh = [52, 58, 57, 66, 64, 73, 78, 75]
tunggu = [3, 5, 4, 8, 12, 6, 5, 7, 4, 15, 6, 5, 9, 4, 6]   # menit

fig, ax = plt.subplots(2, 2, figsize=(9, 6))
ax[0, 0].plot(bulan, omzet, marker="o")
ax[0, 0].set_title("Tren: omzet per bulan")
ax[0, 0].set_ylabel("juta rupiah")
ax[0, 0].set_ylim(0, 50)

ax[0, 1].bar(bulan, omzet)
ax[0, 1].set_title("Perbandingan: batang mulai dari 0")

ax[1, 0].scatter(suhu, es_teh)
ax[1, 0].set_xlabel("suhu (derajat C)")
ax[1, 0].set_ylabel("gelas terjual")

ax[1, 1].hist(tunggu, bins=[0, 3, 6, 9, 12, 15, 18])
ax[1, 1].set_xlabel("waktu tunggu (menit)")

fig.tight_layout()
fig.savefig("ringkasan.png", dpi=150)""",
            },
            {
                "body": [
                    "Program ini menyimpan satu gambar ringkasan.png berisi empat",
                    "grafik. Contoh ini sudah dicoba dengan Matplotlib 3.11.2.",
                    "",
                    "fig adalah seluruh gambar, sedangkan ax adalah kotak-kotak",
                    "grafik di dalamnya (axes). plt.subplots(2, 2) membuat kisi",
                    "2 x 2, jadi ax[0, 0] adalah kotak kiri atas. Semua pengaturan",
                    "ditulis ke kotak tertentu: ax.set_title, ax.set_ylabel,",
                    "ax.set_ylim.",
                    "",
                    "Matplotlib punya gaya lain yang sering muncul di tutorial:",
                    "plt.plot(...), plt.title(...), langsung lewat plt. Gaya itu",
                    "menggambar ke kotak yang sedang aktif, dan begitu grafiknya",
                    "lebih dari satu, gampang tertukar mana yang sedang diatur.",
                    "Biasakan gaya fig, ax dari awal. Kalau menemukan kode plt.xxx,",
                    "padanannya hampir selalu ax.xxx atau ax.set_xxx.",
                    "",
                    "Di Jupyter, grafik langsung muncul di bawah sel. Di skrip",
                    "biasa, panggil plt.show() untuk membuka jendela, atau",
                    "fig.savefig() untuk menyimpan berkas PNG, SVG, atau PDF.",
                ],
            },
            {
                "heading": "Grafik yang menipu: sumbu terpotong",
                "code": """omzet = {"Jul": 41.2, "Agu": 43.5, "Sep": 42.8, "Okt": 47.1}


def batang(data, mulai, lebar=36):
    puncak = max(data.values())
    for bulan, nilai in data.items():
        panjang = round((nilai - mulai) / (puncak - mulai) * lebar)
        print(f"  {bulan} {'#' * panjang} {nilai}")


print("Sumbu mulai dari 0:")
batang(omzet, 0)
print("Sumbu mulai dari 40:")
batang(omzet, 40)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Sumbu mulai dari 0:",
                    "    Jul ############################### 41.2",
                    "    Agu ################################# 43.5",
                    "    Sep ################################# 42.8",
                    "    Okt #################################### 47.1",
                    "  Sumbu mulai dari 40:",
                    "    Jul ###### 41.2",
                    "    Agu ################## 43.5",
                    "    Sep ############## 42.8",
                    "    Okt #################################### 47.1",
                    "",
                    "Datanya sama persis. Omzet Oktober cuma sekitar 14 persen di",
                    "atas Juli. Tapi kalau sumbu batang dimulai dari 40, batang",
                    "Oktober terlihat enam kali lebih panjang. Pembaca melihat",
                    "panjang batang, bukan angka di sumbu, jadi yang ia tangkap",
                    "adalah \"naik berlipat-lipat\".",
                    "",
                    "Aturannya: grafik batang selalu mulai dari nol, karena",
                    "panjang batang itulah yang dibandingkan mata. Grafik garis",
                    "boleh nggak mulai dari nol kalau yang mau ditunjukkan adalah",
                    "perubahan kecil, asal sumbunya diberi angka yang jelas.",
                    "",
                    "Tipuan lain yang sering ditemui:",
                    "",
                    "  - Pai dengan banyak irisan. Mata susah membandingkan sudut,",
                    "    jadi tujuh irisan yang ukurannya mirip nggak bisa dibaca.",
                    "    Pakai batang yang diurutkan.",
                    "  - Grafik tiga dimensi. Kemiringan membuat irisan atau batang",
                    "    di depan terlihat lebih besar dari aslinya.",
                    "  - Dua sumbu y dengan skala berbeda. Dua garis bisa dibuat",
                    "    seolah bergerak bareng cuma dengan mengatur skalanya.",
                    "  - Grafik tanpa satuan dan sumber. \"Naik 40\" bisa berarti",
                    "    40 rupiah atau 40 persen.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Grafik di laporan perusahaan, berita ekonomi, dan dasbor",
                    "aplikasi dibaca orang dalam beberapa detik. Media data",
                    "seperti bagian grafik di koran besar punya pedoman yang mirip",
                    "materi ini: batang mulai dari nol, satuan selalu ditulis,",
                    "sumber data dicantumkan di bawah grafik.",
                    "",
                    "Kasus kecil: tim pemasaran mengirim grafik batang \"Penjualan",
                    "melonjak sejak kampanye!\" untuk ditaruh di slide direksi.",
                    "Sumbu y grafiknya dimulai dari 40 juta.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca angka aslinya, bukan panjang batangnya: dari 41,2",
                    "     ke 47,1 juta, naik sekitar 14 persen.",
                    "  2. Gambar ulang dengan sumbu dari nol:",
                    "       ax.bar(bulan, omzet)",
                    "       ax.set_ylim(0, 50)",
                    "  3. Kalau kenaikannya memang yang penting, tulis angkanya",
                    "     langsung di judul: \"Omzet Oktober naik 14 persen\".",
                    "  4. Tambahkan satuan di sumbu dan sumber data di bawah",
                    "     grafik.",
                ],
            },
        ],
    },
    {
        "title": "15. Peta Pustaka Grafik: Seaborn, Plotly, Altair, Bokeh",
        "sections": [
            {
                "body": [
                    "Matplotlib bisa menggambar hampir apa saja, tapi kadang",
                    "butuh banyak baris. Beberapa pustaka lain dibuat untuk",
                    "kebutuhan yang lebih khusus. Ada yang membuat grafik statistik",
                    "rapi dengan sedikit kode, ada yang membuat grafik interaktif",
                    "yang bisa di-zoom di browser, dan ada yang menulis grafik",
                    "sebagai deskripsi, bukan langkah-langkah.",
                    "",
                    "  Pustaka   Versi (Okt 2026)  Kekuatan",
                    "  Seaborn   0.13.2            grafik statistik di atas Matplotlib",
                    "  Plotly    7.1.0             interaktif, tampil di browser",
                    "  Altair    6.3.0             deklaratif, grammar of graphics",
                    "  Bokeh     3.10.1            interaktif, data besar, streaming",
                    "",
                    "Keempatnya gratis dan sumber terbuka (Plotly berlisensi MIT,",
                    "tiga lainnya BSD-3-Clause), dan semuanya menerima DataFrame",
                    "pandas secara langsung.",
                ],
            },
            {
                "heading": "Seaborn: grafik statistik",
                "code": """import pandas as pd
import seaborn as sns

df = pd.DataFrame({"suhu": [26, 27, 29, 30, 31, 32, 33, 34],
                   "es_teh": [52, 58, 57, 66, 64, 73, 78, 75]})
ax = sns.regplot(data=df, x="suhu", y="es_teh")
ax.figure.savefig("es_teh.png")""",
            },
            {
                "body": [
                    "Satu baris regplot menggambar titik sebar, garis regresi, dan",
                    "pita keyakinan di sekitar garis. Dengan Matplotlib murni,",
                    "kamu harus menghitung garisnya sendiri seperti di bab 01.",
                    "Seaborn juga punya boxplot, heatmap korelasi, dan pairplot",
                    "(grafik sebar untuk semua pasangan kolom), yang paling sering",
                    "dipakai saat eksplorasi data.",
                    "",
                    "Ingat: rilis Seaborn terakhir adalah 0.13.2 pada Januari 2024,",
                    "dan sampai Oktober 2026 belum ada rilis baru. Pustakanya tetap",
                    "jalan dan banyak dipakai, cuma perkembangannya lambat. Seaborn",
                    "juga punya antarmuka baru bernama seaborn.objects yang",
                    "gayanya mirip Altair.",
                ],
            },
            {
                "heading": "Plotly: interaktif di browser",
                "code": """import plotly.express as px

bulan = ["Jul", "Agu", "Sep", "Okt"]
omzet = [41.2, 43.5, 42.8, 47.1]
fig = px.line(x=bulan, y=omzet, markers=True, title="Omzet per bulan")
fig.write_html("omzet.html")""",
            },
            {
                "body": [
                    "Berkas omzet.html bisa dibuka di browser mana pun: arahkan",
                    "kursor ke titik untuk melihat angkanya, seret untuk zoom, dan",
                    "klik dua kali untuk kembali. plotly.express adalah lapisan",
                    "ringkas untuk grafik umum. Plotly juga dipakai sebagai mesin",
                    "grafik Dash (materi berikutnya) dan punya versi JavaScript",
                    "(plotly.js) dan R.",
                    "",
                    "Plotly 7.0 dirilis Agustus 2026. Untuk menyimpan grafik",
                    "sebagai PNG statis, Plotly butuh paket tambahan Kaleido.",
                    "",
                    "Altair memakai pendekatan berbeda. Kamu cukup menyebut",
                    "datanya, jenis tandanya (titik, garis, batang), dan kolom",
                    "mana yang dipetakan ke sumbu atau warna:",
                    "",
                    "  alt.Chart(df).mark_point().encode(x=\"suhu\", y=\"es_teh\")",
                    "",
                    "Cara ini disebut grammar of graphics, sama dengan ggplot2 di",
                    "R yang dibahas di bab 08. Hasilnya spesifikasi JSON",
                    "Vega-Lite yang digambar browser. Jebakan: Altair menolak data",
                    "lebih dari 5000 baris dengan MaxRowsError, supaya berkas",
                    "HTML-nya nggak membengkak. Agregasikan datanya dulu, atau",
                    "matikan batasnya dengan alt.data_transformers.disable_max_rows()",
                    "kalau kamu yakin.",
                    "",
                    "Bokeh juga menggambar grafik interaktif untuk browser, dan",
                    "unggul untuk data yang besar atau terus bertambah, misalnya",
                    "data sensor yang mengalir. Bokeh punya server sendiri untuk",
                    "dasbor dan jadi dasar pustaka dasbor Panel. Versi 4.0 sedang",
                    "dikembangkan.",
                ],
            },
            {
                "heading": "Memilih pustaka",
                "body": [
                    "  - Laporan statis, makalah, atau gambar untuk slide:",
                    "    Matplotlib, atau Seaborn kalau grafiknya statistik.",
                    "  - Eksplorasi cepat di notebook: Seaborn atau Altair.",
                    "  - Grafik yang dibagikan sebagai halaman web dan perlu",
                    "    disorot atau di-zoom: Plotly.",
                    "  - Data besar atau streaming di dasbor: Bokeh.",
                    "",
                    "Pustaka mana pun yang kamu pilih, aturan dari materi",
                    "Matplotlib tetap berlaku: batang mulai dari nol, satuan",
                    "ditulis, dan jenis grafik dipilih dari pertanyaannya.",
                    "Interaktif juga nggak selalu lebih baik. Grafik di slide atau",
                    "PDF nggak bisa disorot, jadi angka pentingnya harus terbaca",
                    "tanpa kursor.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Notebook analisis di Kaggle banyak memakai Seaborn untuk",
                    "eksplorasi, sedangkan grafik interaktif di halaman berita atau",
                    "laporan web sering dibuat dengan Plotly atau pustaka sejenis",
                    "yang menghasilkan HTML. Bokeh dan Panel banyak dipakai untuk",
                    "dasbor ilmiah yang datanya terus bertambah.",
                    "",
                    "Kasus kecil: dosen minta grafik hubungan jam belajar dan nilai",
                    "untuk 300 mahasiswa. Satu versi dimasukkan ke laporan PDF, satu",
                    "versi lagi dibagikan ke mahasiswa sebagai halaman web yang",
                    "bisa disorot per titik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Untuk PDF, pakai Seaborn regplot, lalu simpan sebagai PDF",
                    "     atau PNG resolusi tinggi:",
                    "       ax.figure.savefig(\"nilai.pdf\")",
                    "  2. Untuk halaman web, pakai Plotly dengan nama mahasiswa",
                    "     sebagai info saat titik disorot:",
                    "       px.scatter(df, x=\"jam\", y=\"nilai\", hover_name=\"nama\")",
                    "  3. Periksa apakah nama boleh ditampilkan. Kalau nggak, ganti",
                    "     dengan nomor acak.",
                    "  4. Pastikan kedua versi memakai data dan judul yang sama,",
                    "     supaya angkanya nggak membingungkan.",
                ],
            },
        ],
    },
    {
        "title": "16. Aplikasi Data: Streamlit, Gradio, dan Dash",
        "sections": [
            {
                "body": [
                    "Notebook bagus untuk analis, tapi atasan atau pengguna lain",
                    "biasanya nggak mau membuka Jupyter. Mereka ingin halaman web",
                    "dengan beberapa pilihan, misalnya pilih cabang dan bulan, lalu",
                    "grafiknya berubah. Tiga pustaka membuat halaman seperti itu",
                    "dengan Python saja, tanpa menulis HTML atau JavaScript:",
                    "",
                    "  Pustaka    Versi (Okt 2026)  Paling cocok untuk",
                    "  Streamlit  1.66.0            dasbor dan alat internal cepat",
                    "  Gradio     6.30.0            demo model machine learning",
                    "  Dash       4.4.1             dasbor dengan kendali penuh",
                    "",
                    "Ketiganya gratis dan sumber terbuka. Streamlit milik",
                    "Snowflake sejak 2022 dan Gradio milik Hugging Face, keduanya",
                    "berlisensi Apache-2.0. Dash dibuat oleh Plotly dan berlisensi",
                    "MIT. Streamlit dan Gradio merilis versi baru dengan cepat,",
                    "jadi contoh di tutorial yang umurnya setahun bisa sudah nggak",
                    "jalan. Selalu cocokkan dengan dokumentasi versi yang kamu",
                    "pasang.",
                ],
            },
            {
                "heading": "Streamlit: skrip yang dijalankan ulang",
                "code": """import pandas as pd
import streamlit as st


@st.cache_data
def muat_data():
    return pd.read_csv("penjualan.csv")


df = muat_data()
st.title("Omzet per cabang")
cabang = st.selectbox("Pilih cabang", sorted(df["cabang"].unique()))
pilihan = df[df["cabang"] == cabang]
st.line_chart(pilihan, x="tanggal", y="omzet")
st.metric("Total omzet", f"{pilihan['omzet'].sum():,}")""",
            },
            {
                "body": [
                    "Simpan sebagai app.py, lalu jalankan di terminal dengan",
                    "streamlit run app.py. Browser terbuka ke localhost:8501.",
                    "",
                    "Model kerja Streamlit perlu dipahami dari awal: setiap kali",
                    "pengguna mengubah sesuatu, misalnya memilih cabang lain,",
                    "seluruh app.py dijalankan ulang dari baris pertama. Itu",
                    "membuat kodenya sederhana, karena kamu menulis skrip biasa",
                    "dari atas ke bawah. Akibatnya dua hal:",
                    "",
                    "  - Pekerjaan berat ikut diulang. Membaca CSV 200 MB di setiap",
                    "    klik membuat aplikasinya lambat. @st.cache_data menyimpan",
                    "    hasil fungsi, jadi berkasnya dibaca sekali saja.",
                    "  - Variabel biasa selalu mulai dari awal. Penghitung klik",
                    "    yang ditulis sebagai variabel biasa nggak pernah lewat",
                    "    dari 1. Simpan keadaan seperti itu di st.session_state.",
                    "",
                    "Program Python biasa di bawah meniru model itu, supaya kamu",
                    "bisa melihat bedanya tanpa memasang Streamlit.",
                ],
            },
            {
                "heading": "Model jalankan ulang, ditiru dengan Python biasa",
                "code": "from functools import lru_cache\n\nmuat_dipanggil = 0\n\n\n@lru_cache\ndef muat_data():                  # peran @st.cache_data\n    global muat_dipanggil\n    muat_dipanggil += 1\n    return [41.2, 43.5, 42.8, 47.1]\n\n\ndef aplikasi(slider, session_state):\n    \"\"\"Seperti app.py Streamlit: dijalankan ulang dari atas tiap interaksi.\"\"\"\n    data = muat_data()\n    klik_biasa = 0\n    klik_biasa += 1\n    session_state[\"klik\"] = session_state.get(\"klik\", 0) + 1\n    rata = sum(data) / len(data)\n    print(f\"slider={slider:>2}  variabel biasa={klik_biasa}  \"\n          f\"session_state={session_state['klik']}  rata={rata:.2f}\")\n\n\nstate = {}\nfor nilai in (10, 25, 40):   # pengguna menggeser slider tiga kali\n    aplikasi(nilai, state)\nprint(\"muat_data dijalankan:\", muat_dipanggil, \"kali\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  slider=10  variabel biasa=1  session_state=1  rata=43.65",
                    "  slider=25  variabel biasa=1  session_state=2  rata=43.65",
                    "  slider=40  variabel biasa=1  session_state=3  rata=43.65",
                    "  muat_data dijalankan: 1 kali",
                    "",
                    "Fungsi aplikasi dipanggil tiga kali, seperti tiga interaksi.",
                    "klik_biasa selalu 1 karena dibuat ulang tiap pemanggilan,",
                    "sedangkan session_state, dict yang tetap hidup di luar",
                    "fungsi, terus bertambah. lru_cache membuat muat_data cuma",
                    "benar dijalankan sekali; pemanggilan berikutnya mengambil",
                    "hasil yang tersimpan.",
                ],
            },
            {
                "heading": "Gradio dan Dash",
                "code": """import gradio as gr


def kategori_ulasan(teks):
    kata_buruk = {"lambat", "kecewa", "rusak"}
    buruk = any(k in teks.lower() for k in kata_buruk)
    return "negatif" if buruk else "positif"


demo = gr.Interface(fn=kategori_ulasan, inputs="text", outputs="text")
demo.launch()""",
            },
            {
                "body": [
                    "Gradio dibuat untuk satu pola: ada fungsi (biasanya model",
                    "machine learning), ada masukan, ada keluaran. gr.Interface",
                    "membuatkan halaman berisi kotak teks, tombol kirim, dan kotak",
                    "hasil. Masukannya bisa juga gambar, suara, atau percakapan",
                    "chat. Gradio paling banyak dipakai untuk demo model di Hugging",
                    "Face Spaces, dan untuk tata letak yang lebih bebas ada",
                    "gr.Blocks. Contoh di atas cuma aturan kata sederhana; di",
                    "kurikulum AI & Machine Learning fungsinya diganti model",
                    "sungguhan.",
                    "",
                    "Dash memakai pola berbeda. Kamu menyusun tata letak halaman",
                    "dari komponen, lalu menulis callback: fungsi yang dipanggil",
                    "Dash setiap kali komponen masukan berubah, dan hasilnya",
                    "dikirim ke komponen keluaran:",
                    "",
                    "  @callback(Output(\"grafik\", \"figure\"), Input(\"cabang\", \"value\"))",
                    "  def perbarui(cabang):",
                    "      return px.line(df[df[\"cabang\"] == cabang], x=\"tanggal\", y=\"omzet\")",
                    "",
                    "Hanya fungsi itu yang dijalankan, bukan seluruh skrip. Pola",
                    "ini lebih banyak ditulis di awal, tapi lebih terkendali untuk",
                    "dasbor besar dengan banyak grafik yang saling terhubung. Dash",
                    "berjalan di atas Flask, jadi bisa dipasang di server seperti",
                    "aplikasi web Python lain.",
                    "",
                    "Jebakan: ketiganya menyalakan server web. demo.launch(",
                    "share=True) di Gradio membuat tautan publik sementara yang bisa",
                    "dibuka siapa pun. Jangan pakai untuk data pribadi atau data",
                    "kantor.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim data di banyak perusahaan memakai Streamlit untuk alat",
                    "internal, misalnya halaman cek stok atau pantauan penjualan",
                    "harian. Hugging Face Spaces memuat ribuan demo model yang",
                    "dibangun dengan Gradio dan Streamlit, dan Dash banyak dipakai",
                    "untuk dasbor analitik yang lebih rumit.",
                    "",
                    "Kasus kecil: kamu membuat dasbor Streamlit omzet per cabang.",
                    "Tiap kali cabang dipilih, halaman membeku lima detik, dan",
                    "penghitung \"berapa kali kamu memilih\" selalu menunjukkan 1.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ingat model jalankan ulang: tiap pilihan menjalankan",
                    "     app.py dari atas, termasuk membaca CSV.",
                    "  2. Bungkus pembacaan data dengan cache:",
                    "       @st.cache_data",
                    "       def muat_data():",
                    "           return pd.read_csv(\"penjualan.csv\")",
                    "  3. Pindahkan penghitung ke session_state:",
                    "       st.session_state.pilih = st.session_state.get(\"pilih\", 0) + 1",
                    "  4. Cek ulang dengan memilih beberapa cabang: halaman cepat",
                    "     dan penghitung bertambah.",
                ],
            },
        ],
    },
    {
        "title": "17. Sampel, Selang Kepercayaan, dan p-value",
        "sections": [
            {
                "body": [
                    "Bayangkan kamu kerja di toko online, lalu bos nanya: \"Rata-rata",
                    "paket kita sampai ke pembeli dalam berapa hari?\" Toko itu mengirim",
                    "puluhan ribu paket sebulan. Ngecek semuanya jelas nggak mungkin, jadi",
                    "kamu ambil sebagian aja, misalnya 30 pesanan, lalu menebak",
                    "keseluruhannya dari situ.",
                    "",
                    "Menarik kesimpulan tentang kelompok besar dari sebagian kecilnya",
                    "disebut statistik inferensial. Dua istilah ini bakal muncul terus:",
                    "",
                    "  - Populasi: semua hal yang mau kamu ketahui. Di contoh ini, semua",
                    "    pesanan bulan ini.",
                    "  - Sampel: bagian populasi yang memang kamu ukur. Di contoh ini, 30",
                    "    pesanan tadi.",
                    "",
                    "Angka yang menggambarkan populasi disebut parameter, misalnya",
                    "rata-rata lama kirim semua pesanan. Angka itu hampir nggak pernah",
                    "kamu ketahui persis. Angka yang kamu hitung dari sampel disebut",
                    "statistik, misalnya rata-rata 30 pesanan tadi. Statistik dipakai",
                    "untuk menebak parameter, dan tebakan itu selalu meleset sedikit.",
                    "Materi ini soal cara mengukur seberapa jauh melesetnya.",
                ],
            },
            {
                "heading": "Sampel yang mewakili",
                "body": [
                    "Tebakan dari sampel cuma masuk akal kalau sampelnya dipilih acak:",
                    "tiap anggota populasi punya peluang yang sama untuk terpilih. Kalau",
                    "nggak, sampelnya bias, dan menambah jumlahnya nggak menolong.",
                    "",
                    "Contoh bias yang sering kejadian:",
                    "",
                    "  - Survei kepuasan yang dikirim lewat notifikasi aplikasi cuma",
                    "    sampai ke pengguna yang masih aktif. Yang sudah kecewa dan",
                    "    menghapus aplikasinya nggak pernah ikut dihitung.",
                    "  - Ulasan bintang di marketplace kebanyakan ditulis orang yang puas",
                    "    sekali atau kesal sekali. Pembeli yang biasa aja jarang menulis.",
                    "",
                    "Kalau sampelnya acak, rata-rata sampel tetap meleset dari rata-rata",
                    "populasi, tapi melesetnya bisa diukur. Ukurannya disebut standard",
                    "error (SE): kira-kira seberapa jauh rata-rata sampel biasanya",
                    "meleset. Rumusnya simpangan baku sampel dibagi akar jumlah data.",
                    "",
                    "Karena ada akarnya, menambah data nggak langsung sebanding",
                    "hasilnya. Supaya SE jadi setengahnya, kamu butuh sampel empat kali",
                    "lebih banyak.",
                ],
            },
            {
                "heading": "Menghitung selang kepercayaan 95%",
                "code": """import math
from statistics import NormalDist, mean, stdev

# lama kirim (hari) dari 30 pesanan yang dipilih acak
lama = [2, 3, 3, 4, 2, 5, 3, 3, 4, 6, 2, 3, 4, 3, 5,
        3, 2, 4, 3, 3, 7, 3, 4, 2, 3, 4, 3, 5, 3, 4]

n = len(lama)
rata = mean(lama)
se = stdev(lama) / math.sqrt(n)        # standard error
z = NormalDist().inv_cdf(0.975)        # sekitar 1,96 untuk 95%
print(f"n = {n}, rata-rata = {rata:.2f} hari")
print(f"standard error = {se:.3f}")
print(f"selang 95%: {rata - z * se:.2f} sampai {rata + z * se:.2f} hari")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  n = 30, rata-rata = 3.50 hari",
                    "  standard error = 0.218",
                    "  selang 95%: 3.07 sampai 3.93 hari",
                    "",
                    "Selang kepercayaan (confidence interval) adalah rentang tebakan",
                    "untuk parameter: rata-rata sampel ditambah dan dikurangi beberapa",
                    "kali SE. Angka 1,96 datang dari distribusi normal. Sebanyak 95%",
                    "luas kurva normal ada di antara -1,96 dan +1,96 simpangan baku, dan",
                    "NormalDist().inv_cdf(0.975) mengembalikan batas atasnya.",
                    "",
                    "Untuk sampel kecil, statistikawan memakai distribusi t, yang",
                    "ekornya lebih tebal. Untuk 30 data angkanya 2,045, bukan 1,96, jadi",
                    "selangnya sedikit lebih lebar: 3,05 sampai 3,95 hari. Modul",
                    "statistics bawaan Python belum punya distribusi t, jadi di",
                    "lapangan angka itu biasanya diambil dari SciPy (contohnya di bawah).",
                ],
            },
            {
                "heading": "Apa arti 95%? Kita coba berkali-kali",
                "code": """import math
import random
from statistics import NormalDist

random.seed(7)
z = NormalDist().inv_cdf(0.975)
kena = 0
for _ in range(100):
    # populasi buatan: angka acak 0 sampai 10, rata-ratanya 5
    sampel = [random.random() * 10 for _ in range(30)]
    m = sum(sampel) / 30
    s = math.sqrt(sum((x - m) ** 2 for x in sampel) / 29)
    se = s / math.sqrt(30)
    if m - z * se <= 5.0 <= m + z * se:
        kena += 1
print(f"{kena} dari 100 selang memuat rata-rata populasi 5.0")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  95 dari 100 selang memuat rata-rata populasi 5.0",
                    "",
                    "Program ini mengambil 100 sampel berbeda dari populasi yang",
                    "rata-ratanya sudah kita tahu, yaitu 5. Tiap sampel menghasilkan",
                    "selangnya sendiri, dan 95 di antaranya memuat angka 5. Kalau seed",
                    "diganti, hasilnya bergeser sedikit, biasanya antara 92 dan 97.",
                    "",
                    "Jadi 95% itu sifat caranya: kalau langkah yang sama diulang terus,",
                    "sekitar 95 dari 100 selang bakal memuat nilai aslinya. Satu selang",
                    "yang sudah jadi, misalnya 3,07 sampai 3,93 hari tadi, memuat nilai",
                    "aslinya atau nggak. Kita cuma nggak tahu yang mana.",
                    "",
                    "Jebakan: kalimat \"ada peluang 95% rata-rata asli ada di selang",
                    "ini\" kedengarannya wajar, tapi itu tafsir yang keliru. Yang aman:",
                    "\"dengan cara yang 95% tepat, rata-ratanya kami perkirakan antara",
                    "3,07 dan 3,93 hari\".",
                ],
            },
            {
                "heading": "p-value: seberapa mengejutkan datamu",
                "code": """import math

# koin dilempar 20 kali, keluar gambar 16 kali
n, k = 20, 16
peluang = [math.comb(n, i) / 2 ** n for i in range(n + 1)]
p_atas = sum(peluang[k:])      # 16 atau lebih
p_dua_sisi = 2 * p_atas        # ditambah 4 atau kurang
print(f"P(16 atau lebih) = {p_atas:.4f}")
print(f"p-value dua sisi = {p_dua_sisi:.4f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  P(16 atau lebih) = 0.0059",
                    "  p-value dua sisi = 0.0118",
                    "",
                    "Uji hipotesis selalu dimulai dari hipotesis nol (H0), yaitu dugaan",
                    "\"nggak ada apa-apa\": koinnya adil, obatnya nggak berefek, desain",
                    "barunya sama aja. p-value menjawab satu pertanyaan sempit: kalau H0",
                    "benar, seberapa besar peluang dapat hasil seekstrem ini atau lebih?",
                    "",
                    "Koin adil yang dilempar 20 kali cuma punya peluang 1,18% untuk",
                    "keluar gambar 16 kali atau lebih, atau sebaliknya 4 kali atau",
                    "kurang. Hasil seperti itu mengejutkan kalau koinnya adil, jadi kita",
                    "menolak H0. Batas yang paling sering dipakai 0,05, disebut alfa.",
                    "Angka itu cuma kebiasaan sejak zaman Ronald Fisher, nggak ada yang",
                    "istimewa di situ.",
                    "",
                    "Yang bukan arti p-value:",
                    "",
                    "  - Peluang H0 benar. p = 0,0118 nggak berarti peluang koinnya adil",
                    "    1,18%.",
                    "  - Ukuran besar efek. Efek kecil sekali pun bisa memberi p-value",
                    "    mungil kalau datanya jutaan.",
                    "  - Bukti bahwa H0 benar. p = 0,30 cuma berarti datanya belum cukup",
                    "    untuk menolak H0.",
                    "",
                    "American Statistical Association sampai menerbitkan pernyataan",
                    "resmi soal salah kaprah ini pada 2016. Salah satu isinya: keputusan",
                    "jangan diambil cuma karena p-value melewati 0,05.",
                    "",
                    "Jebakan: mencoba banyak cara analisis sampai ada yang p < 0,05,",
                    "lalu cuma melaporkan yang itu. Praktik ini disebut p-hacking, dan",
                    "hasilnya hampir selalu nggak bisa diulang orang lain.",
                ],
            },
            {
                "heading": "Di lapangan: SciPy",
                "body": [
                    "Rumus di atas sengaja ditulis manual supaya kelihatan isinya. Di",
                    "pekerjaan, orang memakai SciPy, pustaka algoritma ilmiah di atas",
                    "NumPy. Versi stabil terbaru saat materi ini ditulis (Oktober 2026)",
                    "adalah 1.18.1. Modul scipy.stats punya hampir semua uji yang kamu",
                    "butuhkan. Untuk model statistik klasik ada statsmodels (versi",
                    "0.15.0), yang dipakai lagi di materi deret waktu.",
                ],
                "code": """import math
from statistics import mean, stdev
from scipy import stats

print(stats.binomtest(16, n=20, p=0.5).pvalue)   # 0.0118...

lama = [2, 3, 3, 4, 2, 5, 3, 3, 4, 6, 2, 3, 4, 3, 5,
        3, 2, 4, 3, 3, 7, 3, 4, 2, 3, 4, 3, 5, 3, 4]
se = stdev(lama) / math.sqrt(len(lama))
print(stats.t.ppf(0.975, df=29))                # 2.045...
print(stats.t.interval(0.95, df=29, loc=mean(lama), scale=se))
# (3.053..., 3.946...)""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hasil hitung cepat (quick count) pemilu di Indonesia diumumkan",
                    "lembaga survei beberapa jam sesudah TPS tutup. Mereka nggak",
                    "menghitung semua TPS, cuma sampel TPS yang dipilih acak, lalu",
                    "menulis margin of error di sampingnya, misalnya plus minus 1%.",
                    "Margin itu setengah lebar selang kepercayaan.",
                    "",
                    "Kasus kecil: survei kepuasan disebar acak ke 400 pelanggan, dan 300",
                    "menjawab puas. Bos minta angka yang bisa dipertanggungjawabkan,",
                    "lengkap dengan ketidakpastiannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung proporsinya: p = 300 / 400 = 0,75.",
                    "  2. Hitung standard error untuk proporsi: akar dari p(1 - p) / n,",
                    "     yaitu akar 0,75 x 0,25 / 400 = 0,0217.",
                    "  3. Kalikan dengan 1,96: margin = 0,0424. Selangnya 70,8% sampai",
                    "     79,2%.",
                    "      import math",
                    "      p, n = 300 / 400, 400",
                    "      margin = 1.96 * math.sqrt(p * (1 - p) / n)",
                    "      print(f\"{p - margin:.1%} sampai {p + margin:.1%}\")",
                    "  4. Tulis laporannya: \"75% pelanggan puas (selang 95%: 70,8% sampai",
                    "     79,2%, n = 400)\".",
                    "  5. Kalau bos mau margin cuma 2%, balik rumusnya: n = 1,96^2 x 0,75",
                    "     x 0,25 / 0,02^2 = 1.800,75. Bulatkan ke atas jadi 1.801",
                    "     responden.",
                ],
            },
        ],
    },
    {
        "title": "18. Uji Hipotesis dengan Uji Permutasi",
        "sections": [
            {
                "body": [
                    "Tim web toko online bikin desain halaman baru. Mereka mengukur",
                    "waktu muat halaman: enam kali dengan desain lama, empat kali dengan",
                    "desain baru. Rata-rata desain baru 34 milidetik lebih cepat.",
                    "Pertanyaannya: itu memang lebih cepat, atau cuma kebetulan angka",
                    "yang keluar hari itu?",
                    "",
                    "Uji hipotesis menjawabnya dengan dua dugaan:",
                    "",
                    "  - Hipotesis nol (H0): desainnya nggak berpengaruh. Bedanya cuma",
                    "    kebetulan.",
                    "  - Hipotesis alternatif (H1): desainnya berpengaruh.",
                    "",
                    "Lalu kita hitung p-value: kalau H0 benar, seberapa sering beda",
                    "sebesar 34 milidetik muncul cuma karena kebetulan? Materi",
                    "sebelumnya memakai rumus peluang koin. Untuk dua grup, ada cara",
                    "yang lebih gampang dipahami dan nyaris tanpa asumsi: uji",
                    "permutasi.",
                ],
            },
            {
                "heading": "Ide uji permutasi",
                "body": [
                    "Bayangkan tiap angka ditulis di kartu, dan di belakangnya ada label",
                    "\"lama\" atau \"baru\". Kalau H0 benar, label itu nggak ada artinya.",
                    "Angka 300 bisa aja muncul di desain lama, angka 345 bisa aja muncul",
                    "di desain baru. Jadi kita boleh mengocok labelnya.",
                    "",
                    "Langkahnya:",
                    "",
                    "  1. Hitung beda rata-rata yang teramati dari data asli.",
                    "  2. Gabungkan semua angka jadi satu tumpukan.",
                    "  3. Bagi ulang tumpukan itu ke dua grup berukuran sama seperti",
                    "     aslinya, dengan semua cara yang mungkin.",
                    "  4. Untuk tiap pembagian, hitung beda rata-ratanya.",
                    "  5. p-value adalah proporsi pembagian yang bedanya seekstrem beda",
                    "     teramati atau lebih.",
                    "",
                    "Kalau beda asli kita termasuk yang jarang muncul di antara semua",
                    "pembagian, label grupnya kemungkinan memang berarti.",
                ],
            },
            {
                "heading": "Uji permutasi eksak dengan Python murni",
                "code": """from itertools import combinations
from statistics import fmean

# waktu muat halaman (milidetik) dari dua desain
lama = [320, 345, 310, 360, 335, 350]
baru = [300, 290, 315, 305]

teramati = fmean(lama) - fmean(baru)
gabung = lama + baru
semua = range(len(gabung))

total = 0
ekstrem = 0
for pilih in combinations(semua, len(baru)):
    grup_baru = [gabung[i] for i in pilih]
    grup_lama = [gabung[i] for i in semua if i not in pilih]
    beda = fmean(grup_lama) - fmean(grup_baru)
    total += 1
    if abs(beda) >= abs(teramati) - 1e-9:
        ekstrem += 1

print(f"beda teramati: {teramati:.2f} ms")
print(f"semua pembagian: {total}")
print(f"seekstrem itu atau lebih: {ekstrem}")
print(f"p-value: {ekstrem / total:.4f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  beda teramati: 34.17 ms",
                    "  semua pembagian: 210",
                    "  seekstrem itu atau lebih: 4",
                    "  p-value: 0.0190",
                    "",
                    "combinations(semua, 4) memilih 4 posisi dari 10 untuk grup baru.",
                    "Banyaknya 210 cara, sama dengan C(10, 4). Karena semua cara dicoba,",
                    "uji ini disebut eksak. Cuma 4 pembagian yang bedanya sejauh 34,17",
                    "milidetik atau lebih, ke arah mana pun. Salah satunya tentu",
                    "pembagian asli.",
                    "",
                    "abs() dipakai karena kita menguji dua sisi: desain baru bisa lebih",
                    "cepat, bisa juga lebih lambat. p-value 0,019 lebih kecil dari 0,05,",
                    "jadi H0 ditolak. Beda waktu muatnya kecil kemungkinan kebetulan.",
                    "",
                    "Jebakan: membandingkan float dengan >= bisa meleset karena",
                    "pembulatan. Beda yang di atas kertas sama persis bisa tersimpan",
                    "sebagai 34,1666...67 di satu tempat dan 34,1666...64 di tempat lain.",
                    "Pengurangan 1e-9 menjaga supaya pembagian yang bedanya sama tetap",
                    "terhitung.",
                ],
            },
            {
                "heading": "Kalau datanya banyak: SciPy dan uji t",
                "body": [
                    "Dua grup berisi 20 data punya C(40, 20) pembagian, kira-kira 138",
                    "miliar. Mencoba semuanya nggak praktis, jadi orang mengocok label",
                    "secara acak beberapa ribu kali dan memakai proporsinya sebagai",
                    "perkiraan p-value. SciPy melakukan keduanya lewat",
                    "stats.permutation_test: eksak kalau jumlah pembagiannya cukup",
                    "kecil, acak kalau terlalu banyak.",
                    "",
                    "Pembanding yang paling sering kamu lihat di laporan adalah uji t.",
                    "Uji ini menghitung beda rata-rata dibagi standard error-nya, lalu",
                    "membaca p-value dari distribusi t. Cepat dan standar, tapi",
                    "berasumsi data tiap grup kira-kira normal, atau sampelnya cukup",
                    "besar.",
                ],
                "code": """import numpy as np
from scipy import stats

lama = [320, 345, 310, 360, 335, 350]
baru = [300, 290, 315, 305]

def beda_rata(x, y, axis):
    return np.mean(x, axis=axis) - np.mean(y, axis=axis)

hasil = stats.permutation_test((lama, baru), beda_rata,
                               permutation_type="independent")
print(f"permutasi: p = {hasil.pvalue:.4f}")      # 0.0190

t = stats.ttest_ind(lama, baru, equal_var=False)
print(f"uji t Welch: t = {t.statistic:.2f}, p = {t.pvalue:.4f}")
# uji t Welch: t = 3.67, p = 0.0065""",
            },
            {
                "heading": "Membaca dua hasil yang beda",
                "body": [
                    "Uji permutasi memberi 0,0190, uji t memberi 0,0065. Dua-duanya di",
                    "bawah 0,05, jadi kesimpulannya sama, tapi angkanya beda karena",
                    "asumsinya beda. Dengan cuma 10 data, uji permutasi lebih jujur:",
                    "ia nggak menganggap data ikut kurva normal.",
                    "",
                    "Perhatikan equal_var=False. Itu uji t Welch, yang nggak menganggap",
                    "sebaran dua grup sama. Bawaan ttest_ind justru equal_var=True (uji t",
                    "Student), padahal Welch lebih aman untuk hampir semua kasus.",
                    "",
                    "Setiap uji punya dua kemungkinan salah:",
                    "",
                    "                      H0 benar           H0 salah",
                    "    tolak H0          galat tipe I (a)   benar (power)",
                    "    gagal tolak H0    benar              galat tipe II (b)",
                    "",
                    "Galat tipe I itu alarm kebakaran yang bunyi padahal nggak ada api.",
                    "Peluangnya sama dengan alfa yang kamu pilih, misalnya 5%. Galat",
                    "tipe II itu ada api tapi alarm diam: efeknya ada, ujimu nggak",
                    "menangkapnya. Power, yaitu 1 dikurangi peluang galat tipe II, naik",
                    "kalau sampelnya lebih banyak atau efeknya lebih besar. Menurunkan",
                    "alfa mengurangi alarm palsu, tapi menambah api yang lolos.",
                ],
            },
            {
                "heading": "Memilih uji, dan bahaya terlalu banyak uji",
                "body": [
                    "Pegangan kasarnya:",
                    "",
                    "  - Dua grup, data angka, sampel kecil atau bentuknya aneh: uji",
                    "    permutasi, atau Mann-Whitney (stats.mannwhitneyu). Untuk data",
                    "    di atas, Mann-Whitney juga memberi p = 0,0190.",
                    "  - Dua grup, data angka, sampel cukup besar: uji t Welch.",
                    "  - Data hitungan per kategori, misalnya jumlah yang beli dan nggak",
                    "    beli per kota: uji chi-kuadrat (stats.chi2_contingency).",
                    "  - Lebih dari dua grup: ANOVA atau Kruskal-Wallis, yang juga ada di",
                    "    scipy.stats.",
                    "",
                    "Jebakan: menjalankan 20 uji sekaligus dengan alfa 0,05 berarti",
                    "rata-rata satu uji bakal \"signifikan\" walau nggak ada efek apa",
                    "pun. Koreksi paling sederhana namanya Bonferroni: bagi alfa dengan",
                    "jumlah uji. Untuk 20 uji, batasnya jadi 0,0025.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Uji klinis obat, riset pendidikan, dan analisis performa aplikasi",
                    "sama-sama butuh jawaban \"beda ini nyata atau kebetulan\". Uji",
                    "permutasi sering dipakai di riset dengan sampel kecil, misalnya",
                    "percobaan di beberapa kelas atau beberapa server.",
                    "",
                    "Kasus kecil: seorang guru mencoba kuis harian di kelas A (8 siswa),",
                    "sementara kelas B (8 siswa) belajar seperti biasa. Rata-rata nilai",
                    "ujian kelas A 6 poin lebih tinggi. Kepala sekolah bertanya apakah",
                    "kuis harian layak diterapkan di semua kelas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis H0: kuis harian nggak berpengaruh pada nilai ujian.",
                    "  2. Hitung banyaknya pembagian: C(16, 8) = 12.870. Masih kecil, jadi",
                    "     uji permutasi eksak dengan combinations bisa dipakai.",
                    "  3. Hitung proporsi pembagian yang bedanya 6 poin atau lebih, ke",
                    "     dua arah. Proporsi itu p-value-nya.",
                    "  4. Kalau p < 0,05, laporkan bedanya beserta p-value. Kalau nggak,",
                    "     laporkan bahwa data belum cukup untuk menyimpulkan.",
                    "  5. Sampaikan batasnya dengan jujur: kelasnya nggak diacak, jadi",
                    "     mungkin kelas A memang lebih rajin sejak awal. Untuk bukti sebab",
                    "     akibat, siswa perlu dibagi acak, seperti di A/B testing.",
                ],
            },
        ],
    },
    {
        "title": "19. A/B Testing untuk Keputusan Produk",
        "sections": [
            {
                "body": [
                    "Tim toko online mengganti tulisan tombol dari \"Beli sekarang\" jadi",
                    "\"Masukkan keranjang\". Minggu berikutnya penjualan naik 8%. Apakah",
                    "tombolnya yang berjasa? Belum tentu. Minggu itu mungkin ada tanggal",
                    "gajian, promo ongkir, atau iklan baru. Membandingkan sebelum dan",
                    "sesudah selalu tercampur hal lain yang ikut berubah.",
                    "",
                    "A/B testing memecahkannya dengan menjalankan dua versi bersamaan.",
                    "Pengunjung dibagi acak: sebagian melihat versi A (kontrol, yang",
                    "lama), sebagian melihat versi B (yang baru). Karena pembagiannya",
                    "acak dan waktunya sama, gajian dan promo mengenai dua grup dengan",
                    "porsi yang sama. Beda yang tersisa bisa dipercaya sebagai efek",
                    "tombolnya.",
                    "",
                    "Hal yang perlu diputuskan sebelum eksperimen jalan:",
                    "",
                    "  - Hipotesis: \"tulisan baru menaikkan konversi\".",
                    "  - Metrik utama: satu angka penentu, misalnya konversi, yaitu",
                    "    persen pengunjung yang akhirnya membeli.",
                    "  - Metrik pagar (guardrail): angka yang nggak boleh memburuk,",
                    "    misalnya jumlah pembatalan atau waktu muat halaman.",
                    "  - Unit acak: biasanya pengguna, bukan kunjungan halaman, supaya",
                    "    satu orang nggak melihat dua versi bergantian.",
                    "  - Alfa, power, efek minimum yang mau dideteksi, lalu ukuran",
                    "    sampel dan lama eksperimen. Lamanya sebaiknya minggu penuh,",
                    "    karena perilaku belanja hari Senin dan Sabtu beda.",
                ],
            },
            {
                "heading": "Membagi pengunjung dengan hash",
                "code": """import hashlib

def varian(user_id, eksperimen="tombol-beli"):
    kunci = f"{eksperimen}:{user_id}".encode()
    angka = int(hashlib.sha256(kunci).hexdigest(), 16) % 100
    return "A" if angka < 50 else "B"

for uid in ["u101", "u102", "u103", "u101"]:
    print(uid, "->", varian(uid))

hitung = {"A": 0, "B": 0}
for i in range(10_000):
    hitung[varian(f"u{i}")] += 1
print(hitung)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  u101 -> B",
                    "  u102 -> A",
                    "  u103 -> B",
                    "  u101 -> B",
                    "  {'A': 5002, 'B': 4998}",
                    "",
                    "Kenapa hash dan bukan random? Hash selalu memberi hasil yang sama",
                    "untuk masukan yang sama. Pengguna u101 dapat versi B hari ini,",
                    "besok, dan di HP-nya yang lain, tanpa perlu disimpan di mana pun.",
                    "Tapi untuk banyak pengguna, hasilnya tersebar seperti acak: 5002",
                    "lawan 4998.",
                    "",
                    "Nama eksperimen ikut masuk ke kunci. Tanpa itu, orang yang sama",
                    "selalu masuk grup B di semua eksperimen, dan dua eksperimen yang",
                    "jalan bersamaan jadi saling mengganggu.",
                ],
            },
            {
                "heading": "Berapa pengunjung yang dibutuhkan",
                "code": """from statistics import NormalDist

def ukuran_per_grup(p1, p2, alfa=0.05, power=0.80):
    z_a = NormalDist().inv_cdf(1 - alfa / 2)
    z_b = NormalDist().inv_cdf(power)
    ragam = p1 * (1 - p1) + p2 * (1 - p2)
    return (z_a + z_b) ** 2 * ragam / (p1 - p2) ** 2

print(f"5% -> 6%  : {ukuran_per_grup(0.05, 0.06):,.0f} per grup")
print(f"5% -> 5.5%: {ukuran_per_grup(0.05, 0.055):,.0f} per grup")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  5% -> 6%  : 8,155 per grup",
                    "  5% -> 5.5%: 31,231 per grup",
                    "",
                    "Konversi sekarang 5%. Kalau kamu cuma peduli pada kenaikan minimal",
                    "satu poin jadi 6%, butuh sekitar 8.155 pengunjung per grup. Kenaikan",
                    "sekecil itu disebut efek minimum yang bisa dideteksi (minimum",
                    "detectable effect).",
                    "",
                    "Mengecilkan efek jadi setengahnya membuat kebutuhan sampel hampir",
                    "empat kali lipat, karena selisihnya dikuadratkan di penyebut. Kalau",
                    "toko itu cuma kedatangan 1.000 pengunjung per grup per hari,",
                    "eksperimen pertama butuh sembilan hari, jadi dibulatkan ke dua",
                    "minggu penuh. Eksperimen kedua butuh lebih dari sebulan, dan itu",
                    "bahan diskusi dengan tim produk sebelum mulai.",
                ],
            },
            {
                "heading": "Membaca hasil dengan uji dua proporsi",
                "code": """import math
from statistics import NormalDist

n_a, beli_a = 8200, 410     # versi A: "Beli sekarang"
n_b, beli_b = 8200, 492     # versi B: "Masukkan keranjang"

p_a, p_b = beli_a / n_a, beli_b / n_b
p_gabung = (beli_a + beli_b) / (n_a + n_b)
se = math.sqrt(p_gabung * (1 - p_gabung) * (1 / n_a + 1 / n_b))
z = (p_b - p_a) / se
p_value = 2 * (1 - NormalDist().cdf(abs(z)))

se_beda = math.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
bawah = (p_b - p_a) - 1.96 * se_beda
atas = (p_b - p_a) + 1.96 * se_beda

print(f"konversi A = {p_a:.2%}, B = {p_b:.2%}")
print(f"z = {z:.2f}, p-value = {p_value:.4f}")
print(f"selisih 95%: {bawah:+.2%} sampai {atas:+.2%}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  konversi A = 5.00%, B = 6.00%",
                    "  z = 2.81, p-value = 0.0050",
                    "  selisih 95%: +0.30% sampai +1.70%",
                    "",
                    "p-value 0,005 berarti beda sebesar ini jarang muncul kalau dua",
                    "tombol memang sama. Selang kepercayaannya lebih berguna lagi",
                    "untuk bisnis: kenaikan konversinya kira-kira antara 0,3 dan 1,7",
                    "poin. Kalau kenaikan 0,3 poin pun sudah menguntungkan, keputusannya",
                    "gampang. Kalau baru untung di atas 1 poin, hasil ini belum cukup",
                    "meyakinkan.",
                    "",
                    "Signifikan secara statistik belum tentu penting secara bisnis.",
                    "Dengan sejuta pengunjung, kenaikan 0,05 poin pun bisa signifikan,",
                    "padahal mungkin nggak sebanding dengan biaya mengganti desain.",
                    "",
                    "Di Python, fungsi proportions_ztest dari statsmodels menghitung hal",
                    "yang sama dan memberi z = 2,81, p = 0,0050.",
                ],
            },
            {
                "heading": "Peeking: mengintip lalu berhenti",
                "code": """import math
import random
from statistics import NormalDist

def p_value(beli_a, beli_b, n):
    p = (beli_a + beli_b) / (2 * n)
    if p in (0, 1):
        return 1.0
    se = math.sqrt(p * (1 - p) * 2 / n)
    z = (beli_b - beli_a) / n / se
    return 2 * (1 - NormalDist().cdf(abs(z)))

random.seed(42)
ngintip, sabar = 0, 0
for _ in range(200):               # 200 eksperimen A/A
    beli_a = beli_b = 0
    pernah_signifikan = False
    for n in range(1, 5001):       # 5000 pengunjung per grup
        beli_a += random.random() < 0.05
        beli_b += random.random() < 0.05
        if n % 250 == 0 and p_value(beli_a, beli_b, n) < 0.05:
            pernah_signifikan = True
    ngintip += pernah_signifikan
    sabar += p_value(beli_a, beli_b, 5000) < 0.05

print(f"dicek tiap 250 pengunjung : {ngintip} dari 200 'menang'")
print(f"dicek sekali di akhir     : {sabar} dari 200 'menang'")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  dicek tiap 250 pengunjung : 37 dari 200 'menang'",
                    "  dicek sekali di akhir     : 10 dari 200 'menang'",
                    "",
                    "Ini eksperimen A/A: dua grup dengan konversi persis sama, 5%. Semua",
                    "\"kemenangan\" di sini palsu. Kalau dicek sekali di akhir, alarm",
                    "palsunya 10 dari 200, persis 5% sesuai alfa. Kalau dashboard dicek",
                    "tiap 250 pengunjung dan eksperimen dihentikan begitu p < 0,05, alarm",
                    "palsunya jadi 37 dari 200, hampir 19%.",
                    "",
                    "Kebiasaan itu disebut peeking. Obatnya: tentukan ukuran sampel di",
                    "awal dan baca hasil sekali di akhir. Kalau memang harus memantau",
                    "terus, pakai metode sequential testing yang dirancang untuk itu,",
                    "yang biasanya sudah tersedia di platform eksperimen.",
                    "",
                    "Jebakan lain yang sering ditemui:",
                    "",
                    "  - Sample ratio mismatch: pembagian yang seharusnya 50:50 ternyata",
                    "    53:47. Biasanya tanda ada bug di pembagian atau pencatatan, dan",
                    "    hasil eksperimennya nggak bisa dipercaya.",
                    "  - Efek kebaruan: tombol baru diklik karena baru, lalu efeknya",
                    "    memudar sesudah seminggu.",
                    "  - Memotong data per segmen sesudah melihat hasil sampai ketemu",
                    "    segmen yang \"menang\". Itu p-hacking dengan nama lain.",
                    "",
                    "Perusahaan besar biasanya punya platform eksperimen sendiri atau",
                    "memakai produk jadi, ada yang open source seperti GrowthBook, ada",
                    "yang berbayar. Teknik pengurang ragam seperti CUPED juga sering",
                    "dipakai supaya eksperimen selesai lebih cepat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Marketplace, aplikasi transportasi online, dan layanan streaming",
                    "rutin menguji perubahan kecil dengan A/B testing: urutan menu,",
                    "teks notifikasi, sampai besar diskon. Keputusan meluncurkan fitur",
                    "sering menunggu hasil eksperimen, bukan pendapat orang di rapat.",
                    "",
                    "Kasus kecil: tim pemasaran mau menguji banner \"gratis ongkir\" di",
                    "halaman produk. Konversi sekarang 4%, dan banner dianggap layak",
                    "kalau menaikkannya minimal jadi 4,5%. Situsnya didatangi sekitar",
                    "6.000 pengguna per hari.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tetapkan metrik utama (konversi) dan metrik pagar (jumlah",
                    "     pembatalan pesanan).",
                    "  2. Hitung ukuran sampel dengan fungsi ukuran_per_grup(0.04,",
                    "     0.045). Hasilnya sekitar 25.500 pengguna per grup, jadi 51.000",
                    "     total.",
                    "  3. Dengan 6.000 pengguna per hari, butuh sekitar 9 hari. Bulatkan",
                    "     ke 14 hari supaya mencakup dua minggu penuh.",
                    "  4. Bagi pengguna dengan hash dari user_id dan nama eksperimen.",
                    "     Cek di hari pertama bahwa pembagiannya mendekati 50:50.",
                    "  5. Jangan berhenti di tengah walau grafiknya kelihatan menang.",
                    "     Di hari ke-14, hitung uji dua proporsi dan selang selisihnya,",
                    "     lalu putuskan berdasarkan batas 4,5% yang ditetapkan di awal.",
                ],
            },
        ],
    },
    {
        "title": "20. Deret Waktu dan Peramalan Sederhana",
        "sections": [
            {
                "body": [
                    "Deret waktu (time series) adalah data yang dicatat berurutan",
                    "menurut waktu: penjualan harian, jumlah pengunjung per jam, harga",
                    "cabai per minggu. Urutannya bagian dari isinya. Mengacak baris",
                    "tabel penjualan nggak mengubah totalnya, tapi menghapus semua yang",
                    "bisa dipelajari dari polanya.",
                    "",
                    "Biasanya deret waktu dipecah jadi beberapa komponen:",
                    "",
                    "  - Tren: arah jangka panjang, misalnya penjualan pelan-pelan naik",
                    "    karena tokonya makin dikenal.",
                    "  - Musiman (seasonality): pola yang berulang dengan periode tetap.",
                    "    Kedai kopi ramai tiap Sabtu, listrik kantor turun tiap Minggu.",
                    "  - Noise: naik turun kecil yang nggak bisa dijelaskan.",
                    "",
                    "Di Indonesia ada musiman yang unik: penjualan banyak toko naik",
                    "menjelang Lebaran. Tanggal Lebaran ikut kalender Hijriah, yang",
                    "setahunnya sekitar 11 hari lebih pendek dari tahun Masehi. Jadi",
                    "puncaknya bergeser maju tiap tahun, dan model yang cuma mengenal",
                    "\"bulan April\" bakal salah tebak.",
                ],
            },
            {
                "heading": "Rata-rata bergerak",
                "code": """pengunjung = [40, 42, 39, 55, 41, 43, 44, 60, 46, 47]

def rata_bergerak(data, jendela):
    hasil = []
    for i in range(jendela - 1, len(data)):
        potong = data[i - jendela + 1 : i + 1]
        hasil.append(sum(potong) / jendela)
    return hasil

for hari, nilai in enumerate(rata_bergerak(pengunjung, 3), start=3):
    print(f"hari {hari:2}: {nilai:.2f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  hari  3: 40.33",
                    "  hari  4: 45.33",
                    "  hari  5: 45.00",
                    "  hari  6: 46.33",
                    "  hari  7: 42.67",
                    "  hari  8: 49.00",
                    "  hari  9: 50.00",
                    "  hari 10: 51.00",
                    "",
                    "Rata-rata bergerak (moving average) menghitung rata-rata beberapa",
                    "titik terakhir, lalu jendelanya digeser satu langkah. Hasilnya",
                    "garis yang lebih halus: lonjakan 55 di hari ke-4 dan 60 di hari",
                    "ke-8 diredam jadi 45,33 dan 49,00, dan arah naiknya jadi lebih",
                    "kelihatan.",
                    "",
                    "Hasilnya mulai di hari ke-3 karena jendela 3 hari butuh tiga data.",
                    "Makin lebar jendelanya, makin halus garisnya, tapi makin telat",
                    "juga ia bereaksi saat tren berubah. Untuk data harian yang punya",
                    "pola mingguan, jendela 7 hari paling sering dipakai, karena tiap",
                    "jendela memuat tepat satu Senin sampai Minggu dan pola mingguannya",
                    "saling menetralkan.",
                ],
            },
            {
                "heading": "Rata-rata bergerak dengan window function SQL",
                "bahasa": "sql",
                "code": """CREATE TABLE kunjungan (hari INTEGER, pengunjung INTEGER);
INSERT INTO kunjungan VALUES
  (1, 40), (2, 42), (3, 39), (4, 55), (5, 41),
  (6, 43), (7, 44), (8, 60), (9, 46), (10, 47);

SELECT hari, pengunjung,
       ROUND(AVG(pengunjung) OVER (
         ORDER BY hari ROWS BETWEEN 2 PRECEDING AND CURRENT ROW),
         2) AS ma3
FROM kunjungan;""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  1|40|40.0",
                    "  2|42|41.0",
                    "  3|39|40.33",
                    "  4|55|45.33",
                    "  5|41|45.0",
                    "  6|43|46.33",
                    "  7|44|42.67",
                    "  8|60|49.0",
                    "  9|46|50.0",
                    "  10|47|51.0",
                    "",
                    "Data deret waktu sering tinggal di database, jadi rata-rata",
                    "bergerak juga sering dihitung di SQL. Bentuk OVER (ORDER BY ...",
                    "ROWS BETWEEN ...) sudah kamu kenal dari kurikulum SQL bagian window",
                    "function. Mulai hari ke-3, angkanya sama dengan versi Python.",
                    "",
                    "Bedanya di dua baris pertama. SQL tetap menghitung rata-rata dari",
                    "data yang ada (satu atau dua hari), sedangkan fungsi Python tadi",
                    "menunggu jendelanya penuh. pandas lewat",
                    "df[\"pengunjung\"].rolling(3).mean() mengikuti cara kedua dan",
                    "mengisi dua baris pertama dengan NaN. Pilih salah satu dengan",
                    "sadar, karena rata-rata dari satu hari bisa menyesatkan di grafik.",
                ],
            },
            {
                "heading": "Meramal, lalu menguji ramalannya",
                "code": """# cup kopi terjual per hari, 4 minggu, mulai hari Senin
cup = [123, 114, 120, 132, 151, 196, 180,
       129, 119, 130, 135, 159, 207, 187,
       135, 127, 136, 142, 167, 213, 193,
       141, 140, 140, 145, 177, 217, 202]

latih, uji = cup[:21], cup[21:]      # 3 minggu awal vs minggu terakhir

naif = [latih[-1]] * 7               # besok sama dengan hari terakhir
musiman = latih[-7:]                 # Senin depan = Senin lalu
rata7 = [sum(latih[-7:]) / 7] * 7    # rata-rata minggu terakhir

def mae(tebakan, asli):
    return sum(abs(t - a) for t, a in zip(tebakan, asli)) / len(asli)

for nama, tebakan in [("naif", naif), ("rata-rata 7 hari", rata7),
                      ("naif musiman", musiman)]:
    print(f"{nama:17} MAE = {mae(tebakan, uji):6.2f} cup")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  naif              MAE =  36.43 cup",
                    "  rata-rata 7 hari  MAE =  27.00 cup",
                    "  naif musiman      MAE =   7.00 cup",
                    "",
                    "Tiga cara meramal paling sederhana dibandingkan di sini. MAE (mean",
                    "absolute error) adalah rata-rata selisih ramalan dengan kenyataan,",
                    "jadi makin kecil makin bagus. Ramalan naif musiman, yang cuma",
                    "menyalin minggu lalu, menang jauh karena pola mingguan kedai ini",
                    "kuat. Cara-cara sederhana ini disebut baseline. Model rumit apa pun",
                    "harus mengalahkan baseline dulu sebelum layak dipakai.",
                    "",
                    "Perhatikan cara datanya dibagi. Tiga minggu awal untuk menyusun",
                    "ramalan, minggu terakhir untuk menguji. Data deret waktu nggak",
                    "boleh dibagi acak. Kalau hari Rabu minggu keempat masuk data latih",
                    "sementara hari Selasanya masuk data uji, modelnya sudah \"melihat",
                    "masa depan\". Nilainya bagus di atas kertas, lalu gagal saat dipakai",
                    "sungguhan. Kesalahan ini disebut kebocoran data (data leakage).",
                    "",
                    "Cara yang lebih teliti namanya walk-forward validation: latih",
                    "sampai minggu 1 lalu uji minggu 2, latih sampai minggu 2 lalu uji",
                    "minggu 3, dan seterusnya. scikit-learn menyediakan TimeSeriesSplit",
                    "untuk membagi dengan pola ini.",
                ],
            },
            {
                "heading": "ARIMA dan alat di Python",
                "body": [
                    "Kalau baseline sudah terkalahkan dan kamu butuh lebih, model klasik",
                    "yang paling sering muncul adalah ARIMA. Namanya gabungan tiga",
                    "bagian:",
                    "",
                    "  - AR (autoregressive): nilai hari ini dijelaskan nilai hari-hari",
                    "    sebelumnya.",
                    "  - I (integrated): data diubah jadi selisih antarhari supaya",
                    "    trennya hilang dan datanya stasioner, artinya rata-rata dan",
                    "    sebarannya nggak berubah-ubah sepanjang waktu.",
                    "  - MA (moving average): nilai hari ini dijelaskan kesalahan",
                    "    ramalan hari-hari sebelumnya.",
                    "",
                    "Jebakan: huruf MA di nama model itu beda dengan rata-rata bergerak",
                    "di awal materi ini, walau namanya sama. Yang di model itu",
                    "merata-ratakan kesalahan ramalan, bukan datanya.",
                    "",
                    "Di Python, pustaka acuannya statsmodels (versi stabil terbaru saat",
                    "materi ini ditulis, Oktober 2026, adalah 0.15.0). Isinya model tadi",
                    "beserta versi musimannya, ExponentialSmoothing (metode Holt-Winters),",
                    "dan seasonal_decompose untuk memecah tren dan musiman. Prophet dari",
                    "Meta juga sering muncul di tutorial. Untuk data yang sudah ada di",
                    "pandas, rolling() dan resample() menangani rata-rata bergerak dan",
                    "perubahan periode, misalnya harian jadi mingguan.",
                ],
                "code": """import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose

cup = [123, 114, 120, 132, 151, 196, 180,
       129, 119, 130, 135, 159, 207, 187,
       135, 127, 136, 142, 167, 213, 193,
       141, 140, 140, 145, 177, 217, 202]
seri = pd.Series(cup, index=pd.date_range("2026-09-07", periods=28))

print(seri.rolling(7).mean().tail(3))
print(seasonal_decompose(seri, period=7).seasonal.head(7))

# ARIMA(1,1,1) plus selisih musiman 7 hari, dilatih 3 minggu awal
model = ARIMA(seri[:21], order=(1, 1, 1),
              seasonal_order=(0, 1, 0, 7)).fit()
print(model.forecast(7))""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Gudang ritel dan minimarket meramal penjualan untuk menentukan",
                    "berapa barang yang dipesan ke pemasok. Ramalan yang terlalu tinggi",
                    "berarti barang menumpuk dan kedaluwarsa, ramalan yang terlalu rendah",
                    "berarti rak kosong. Perusahaan listrik dan aplikasi transportasi",
                    "juga meramal beban per jam supaya kapasitasnya cukup.",
                    "",
                    "Kasus kecil: pemilik kedai kopi di contoh tadi mau tahu berapa",
                    "kilogram biji kopi yang perlu dibeli untuk minggu depan. Satu",
                    "kilogram cukup untuk sekitar 60 cup.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kumpulkan data harian minimal beberapa minggu, urut menurut",
                    "     tanggal, dan pastikan nggak ada hari yang bolong.",
                    "  2. Uji beberapa baseline dengan memisahkan minggu terakhir sebagai",
                    "     data uji. Di contoh tadi, naif musiman paling akurat, dengan",
                    "     kesalahan rata-rata 7 cup per hari.",
                    "  3. Ramal minggu depan dengan cara pemenangnya, yaitu menyalin",
                    "     minggu terakhir: totalnya 1.162 cup.",
                    "      minggu_lalu = [141, 140, 140, 145, 177, 217, 202]",
                    "      total = sum(minggu_lalu)        # 1162",
                    "      print(total / 60)              # sekitar 19,4 kg",
                    "  4. Tambah cadangan sesuai kesalahan ramalan. Meleset 7 cup per hari",
                    "     berarti sekitar 49 cup seminggu, kurang lebih 1 kg lagi. Jadi",
                    "     belanjanya 21 kg.",
                    "  5. Minggu depannya, bandingkan ramalan dengan penjualan asli dan",
                    "     catat kesalahannya. Kalau ada libur nasional, sesuaikan dengan",
                    "     tangan, karena pola mingguan biasa nggak tahu soal libur.",
                ],
            },
        ],
    },
    {
        "title": "21. Baris vs Kolom: Apache Arrow dan Parquet",
        "sections": [
            {
                "body": [
                    "Misalnya kamu dapat berkas CSV transaksi setahun, ukurannya 5 GB",
                    "dengan 40 kolom. Pertanyaannya sederhana: berapa rata-rata nilai",
                    "belanja? Yang dibutuhkan cuma satu kolom, tapi program tetap harus",
                    "membaca seluruh 5 GB itu. Di CSV, satu baris berisi semua kolom",
                    "yang berdempetan, jadi kolom total nggak bisa diambil tanpa ikut",
                    "melewati 39 kolom lainnya.",
                    "",
                    "Bayangkan dua cara menyimpan formulir pendaftaran. Cara pertama:",
                    "satu map per orang, isinya nama, alamat, dan umur orang itu. Cara",
                    "kedua: satu map berisi semua nama, satu map berisi semua alamat,",
                    "satu map berisi semua umur. Kalau mau tahu rata-rata umur, cara",
                    "kedua cukup membuka satu map. Kalau mau melihat data lengkap satu",
                    "orang, cara pertama yang lebih cepat.",
                    "",
                    "Cara pertama disebut penyimpanan berbasis baris (row-oriented),",
                    "cara kedua berbasis kolom (columnar). Materi ini membahas kenapa",
                    "dunia analisis data pindah ke cara kedua, dan dua standar yang",
                    "lahir dari situ: Parquet untuk berkas di disk dan Apache Arrow",
                    "untuk data di memori.",
                ],
            },
            {
                "heading": "Disimpan per baris atau per kolom",
                "body": [
                    "Komputer menyimpan data sebagai deretan byte yang berurutan. Ambil",
                    "tabel kecil ini:",
                    "",
                    "  id   kota      total",
                    "  1    Bandung   52",
                    "  2    Bogor     30",
                    "  3    Bandung   41",
                    "",
                    "Penyimpanan baris menaruhnya sebagai 1, Bandung, 52, 2, Bogor, 30,",
                    "dan seterusnya. Penyimpanan kolom menaruh semua id dulu, lalu semua",
                    "kota, lalu semua total. Gambar di bawah memperlihatkan dua urutan",
                    "itu.",
                    "",
                    "Penyimpanan baris cocok untuk aplikasi yang tiap kali menyentuh",
                    "satu catatan utuh: menyimpan satu pesanan, menampilkan profil satu",
                    "pengguna. Pekerjaan seperti itu disebut OLTP (online transaction",
                    "processing), dan database aplikasi seperti PostgreSQL, MySQL, dan",
                    "SQLite memang menyimpan per baris.",
                    "",
                    "Penyimpanan kolom cocok untuk pertanyaan analisis yang menyapu",
                    "jutaan baris tapi cuma beberapa kolom: total per bulan, rata-rata",
                    "per kota. Pekerjaan seperti itu disebut OLAP (online analytical",
                    "processing). Selain membaca lebih sedikit, nilai satu kolom",
                    "bertipe sama dan berurutan, jadi CPU bisa memprosesnya beberapa",
                    "sekaligus dengan instruksi khusus yang disebut SIMD.",
                ],
            },
            {
                "heading": "Kolom lebih gampang dipadatkan",
                "code": """kota = ["Bandung", "Bandung", "Bandung", "Bogor", "Bogor", "Bandung",
        "Depok", "Depok", "Depok", "Depok", "Bogor", "Bogor"]

# 1. dictionary encoding: simpan tiap nama sekali, sisanya cuma nomor
kamus = sorted(set(kota))
kode = [kamus.index(k) for k in kota]
print("kamus:", kamus)
print("kode :", kode)

# 2. run-length encoding: nilai berulang ditulis (nilai, berapa kali)
rle = []
for k in kode:
    if rle and rle[-1][0] == k:
        rle[-1][1] += 1
    else:
        rle.append([k, 1])
print("rle  :", rle)

asli = sum(len(k) for k in kota)
print(f"huruf asli: {asli}, sesudah dipadatkan: {len(rle) * 2} angka "
      f"+ kamus {sum(len(k) for k in kamus)} huruf")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  kamus: ['Bandung', 'Bogor', 'Depok']",
                    "  kode : [0, 0, 0, 1, 1, 0, 2, 2, 2, 2, 1, 1]",
                    "  rle  : [[0, 3], [1, 2], [0, 1], [2, 4], [1, 2]]",
                    "  huruf asli: 68, sesudah dipadatkan: 10 angka + kamus 17 huruf",
                    "",
                    "Dua trik ini dipakai format kolumnar sungguhan. Dictionary encoding",
                    "menyimpan tiap nilai unik sekali, lalu kolomnya cukup berisi nomor",
                    "kecil. Run-length encoding (RLE) meringkas nilai yang berulang",
                    "berturut-turut jadi pasangan nilai dan jumlahnya.",
                    "",
                    "Dua trik itu cuma ampuh kalau nilai yang mirip berdekatan, dan",
                    "itulah yang terjadi di penyimpanan kolom: satu kolom kota isinya",
                    "nama kota semua. Di penyimpanan baris, nama kota diselingi tanggal",
                    "dan angka, jadi pengulangannya terputus-putus. Data yang diurutkan",
                    "dulu, misalnya menurut kota, bisa dipadatkan jauh lebih kecil lagi.",
                ],
            },
            {
                "heading": "Parquet: berkas kolumnar di disk",
                "body": [
                    "Apache Parquet adalah format berkas kolumnar yang dimulai Twitter",
                    "dan Cloudera pada 2013, lalu jadi proyek Apache. Sekarang ia format",
                    "standar untuk data analitik: Spark, DuckDB, Polars, pandas,",
                    "BigQuery, dan Snowflake semuanya bisa membaca dan menulisnya.",
                    "",
                    "Isi satu berkas Parquet kira-kira begini:",
                ],
                "bahasa": "teks",
                "code": """penjualan.parquet
├── row group 0          (misalnya 1 juta baris pertama)
│   ├── kolom tanggal    -> beberapa page, terkompresi
│   ├── kolom kota       -> beberapa page, terkompresi
│   └── kolom total      -> beberapa page, terkompresi
├── row group 1          (1 juta baris berikutnya)
│   └── ...
└── footer: skema, tipe tiap kolom, letak tiap kolom,
            nilai min/max kolom per row group""",
            },
            {
                "body": [
                    "Baris dibagi jadi kelompok (row group). Di dalam tiap kelompok, tiap",
                    "kolom disimpan terpisah. Bagian paling penting ada di ujung berkas,",
                    "yaitu footer. Pembaca Parquet membaca footer dulu, lalu bisa",
                    "melakukan dua penghematan:",
                    "",
                    "  - Projection pushdown: cuma kolom yang diminta yang dibaca dari",
                    "    disk.",
                    "  - Predicate pushdown: kalau kamu minta total > 1.000.000 dan",
                    "    footer bilang nilai maksimal di row group 3 cuma 400.000, row",
                    "    group itu dilewati tanpa dibaca.",
                    "",
                    "Parquet juga menyimpan tipe data tiap kolom. Di CSV, \"00123\" bisa",
                    "ditebak jadi angka 123 dan nol di depannya hilang. Di Parquet,",
                    "kolom teks tetap teks.",
                    "",
                    "Jebakan: Parquet berkas biner. Membukanya di editor teks cuma",
                    "menampilkan karakter acak. Untuk mengintip isinya, pakai pandas,",
                    "DuckDB, atau perintah duckdb -c \"FROM 'berkas.parquet' LIMIT 5\".",
                ],
            },
            {
                "heading": "Apache Arrow: format kolumnar di memori",
                "body": [
                    "Parquet mengurus data di disk. Begitu data dibaca ke memori, tiap",
                    "pustaka dulu punya bentuk sendiri. Memindahkan tabel dari pandas ke",
                    "Spark atau dari database ke pandas berarti mengubah bentuknya,",
                    "kadang lewat teks, dan untuk data besar itu bisa lebih lama dari",
                    "analisisnya sendiri.",
                    "",
                    "Apache Arrow adalah standar tata letak tabel kolumnar di memori.",
                    "Kalau dua program sama-sama memakai bentuk Arrow, tabelnya bisa",
                    "dioper tanpa disalin dan tanpa diubah (zero-copy). Arrow sekarang",
                    "jadi bahasa bersama di ekosistem data:",
                    "",
                    "  - Polars dibangun di atas model memori Arrow.",
                    "  - DuckDB bisa membaca dan mengembalikan tabel Arrow langsung.",
                    "  - pandas memakai pyarrow untuk membaca Parquet, dan di pandas 3.0",
                    "    tipe teks bawaannya (str) memakai Arrow kalau pyarrow terpasang.",
                    "  - Spark memakai Arrow saat mengirim data ke pandas.",
                    "",
                    "Untuk mengirim data Arrow lewat jaringan ada Arrow Flight, dan",
                    "untuk koneksi database ada ADBC. Pustaka Python-nya bernama",
                    "pyarrow. Versi stabil terbaru saat materi ini ditulis (Oktober",
                    "2026) adalah 26.0.0, berlisensi Apache 2.0.",
                ],
            },
            {
                "heading": "Mencoba dengan pyarrow dan pandas",
                "code": """import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

tabel = pa.table({
    "tanggal": ["2026-09-01", "2026-09-01", "2026-09-02"],
    "kota": ["Bandung", "Bogor", "Bandung"],
    "total": [120000, 80000, 95000],
})
pq.write_table(tabel, "penjualan.parquet")   # kompresi bawaan: snappy

# baca dua kolom saja
sebagian = pq.read_table("penjualan.parquet", columns=["kota", "total"])
print(sebagian.num_rows, sebagian.column_names)  # 3 ['kota', 'total']

# intip footer: nilai maksimal kolom total di row group pertama
meta = pq.ParquetFile("penjualan.parquet").metadata
print(meta.row_group(0).column(2).statistics.max)  # 120000

df = pd.read_parquet("penjualan.parquet")
print(df.dtypes)          # tanggal str, kota str, total int64
df.to_parquet("salinan.parquet")""",
            },
            {
                "heading": "Kapan tetap pakai CSV atau JSON",
                "body": [
                    "Parquet bukan jawaban untuk semua hal. Format lain masih punya",
                    "tempat:",
                    "",
                    "  format     bentuk           cocok untuk",
                    "  CSV        teks, baris      tukar data kecil, dibuka di Excel",
                    "  JSON       teks, bersarang  respons API, konfigurasi",
                    "  Parquet    biner, kolom     simpan data analitik, data lake",
                    "  ORC        biner, kolom     ekosistem Hive dan Hadoop lama",
                    "  Avro       biner, baris     pesan Kafka, skema yang berubah",
                    "  Arrow IPC  biner, kolom     oper data antarproses (Feather)",
                    "",
                    "Pegangannya: kalau datanya kecil atau harus dibaca manusia, CSV",
                    "masih paling praktis. Kalau datanya mulai puluhan megabyte dan",
                    "dibaca berkali-kali untuk analisis, ubah sekali jadi Parquet. Avro",
                    "berbasis baris, jadi ia cocok untuk aliran pesan yang ditulis satu",
                    "per satu, dan bakal muncul lagi di materi Kafka.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak data terbuka sekarang dirilis dalam Parquet. Data perjalanan",
                    "taksi kota New York (NYC TLC), salah satu data latihan paling",
                    "populer, diterbitkan dalam Parquet sejak 2022. Hugging Face juga",
                    "mengonversi dataset di Hub-nya ke Parquet supaya bisa langsung",
                    "di-query.",
                    "",
                    "Kasus kecil: tiap bulan kamu membuat laporan omzet per kota dari",
                    "berkas CSV setahun berukuran 2 GB dengan 40 kolom. Membacanya",
                    "dengan pandas butuh beberapa menit dan memorinya hampir habis.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ubah CSV itu sekali jadi Parquet. DuckDB bisa melakukannya",
                    "     tanpa memuat semuanya ke memori:",
                    "      COPY (FROM 'transaksi.csv') TO 'transaksi.parquet'",
                    "           (FORMAT parquet);",
                    "  2. Cek ukurannya. Berkas Parquet biasanya jauh lebih kecil dari",
                    "     CSV-nya karena terkompresi per kolom.",
                    "  3. Untuk laporan, baca cuma kolom yang dipakai:",
                    "      pd.read_parquet(\"transaksi.parquet\",",
                    "                      columns=[\"tanggal\", \"kota\", \"total\"])",
                    "  4. Data bulan berikutnya ditulis sebagai berkas Parquet baru di",
                    "     folder yang sama, bukan ditempel ke CSV raksasa.",
                    "  5. Simpan CSV aslinya sebagai arsip, tapi semua analisis jalan",
                    "     dari Parquet.",
                ],
            },
        ],
    },
    {
        "title": "22. DuckDB: SQL Analitik di Laptop",
        "sections": [
            {
                "body": [
                    "Kamu sudah kenal SQL dari kurikulum SQL, dan sudah kenal SQLite:",
                    "database yang tinggal di satu berkas dan berjalan di dalam",
                    "programmu, tanpa server. DuckDB punya bentuk yang sama, tapi",
                    "dirancang untuk analisis. Orang sering menyebutnya \"SQLite untuk",
                    "analitik\".",
                    "",
                    "DuckDB lahir di CWI, lembaga riset matematika dan informatika di",
                    "Amsterdam, dibuat oleh Mark Raasveldt dan Hannes Mühleisen. Versi",
                    "1.0 rilis Juni 2024. Versi stabil terbaru saat materi ini ditulis",
                    "(Oktober 2026) adalah 1.5.6, sementara cabang 2.0 masih dalam",
                    "pengembangan. Lisensinya MIT. Di Survei Stack Overflow 2025, 3,3%",
                    "responden memakai DuckDB, naik dari 1,4% setahun sebelumnya.",
                    "",
                    "Tiga hal yang membuatnya cepat untuk analisis:",
                    "",
                    "  - Penyimpanan kolumnar, seperti dibahas di materi sebelumnya.",
                    "  - Eksekusi tervektorisasi: data diproses per potongan ribuan",
                    "    nilai sekaligus, bukan satu baris demi satu baris.",
                    "  - Paralel: satu query memakai semua inti CPU laptopmu.",
                    "",
                    "Ditambah satu kemampuan yang paling sering bikin orang jatuh hati:",
                    "DuckDB bisa meng-query berkas CSV, Parquet, dan JSON langsung dari",
                    "jalurnya, tanpa perlu diimpor dulu.",
                ],
            },
            {
                "heading": "Database di dalam programmu",
                "body": [
                    "Database seperti PostgreSQL dan MySQL berbentuk client-server:",
                    "ada proses server yang jalan terus, dan programmu terhubung",
                    "lewat jaringan. DuckDB dan SQLite berbentuk in-process: database-nya",
                    "cuma pustaka yang dimuat ke dalam programmu sendiri.",
                    "",
                    "                 PostgreSQL       SQLite           DuckDB",
                    "  bentuk         client-server    in-process       in-process",
                    "  penyimpanan    baris            baris            kolom",
                    "  cocok untuk    backend aplikasi data aplikasi    analisis",
                    "  penulis        banyak sekaligus satu per waktu   satu proses",
                    "",
                    "Akibatnya, memasang DuckDB cukup pip install duckdb. Nggak ada",
                    "server yang harus dinyalakan, nggak ada pengguna dan kata sandi.",
                    "Database-nya bisa berupa satu berkas .duckdb, atau cuma di memori",
                    "selama program jalan.",
                ],
            },
            {
                "heading": "Bentuk query analitik, dicoba dengan sqlite3",
                "code": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.executescript(\"\"\"\nCREATE TABLE penjualan (tanggal TEXT, kota TEXT, total INTEGER);\nINSERT INTO penjualan VALUES\n  ('2026-09-01', 'Bandung', 120000), ('2026-09-01', 'Bogor', 80000),\n  ('2026-09-02', 'Bandung', 95000),  ('2026-09-02', 'Depok', 150000),\n  ('2026-09-03', 'Bogor', 110000),   ('2026-09-03', 'Depok', 70000),\n  ('2026-09-03', 'Bandung', 130000);\n\"\"\")\n\nsql = \"\"\"\nSELECT kota,\n       COUNT(*)   AS transaksi,\n       SUM(total) AS omzet,\n       RANK() OVER (ORDER BY SUM(total) DESC) AS peringkat\nFROM penjualan\nGROUP BY kota\nORDER BY peringkat\n\"\"\"\nfor baris in db.execute(sql):\n    print(baris)",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ('Bandung', 3, 345000, 1)",
                    "  ('Depok', 2, 220000, 2)",
                    "  ('Bogor', 2, 190000, 3)",
                    "",
                    "Contoh ini memakai sqlite3 bawaan Python supaya bisa dijalankan",
                    "tanpa memasang apa pun. Query yang sama persis jalan di DuckDB:",
                    "GROUP BY, fungsi agregat, dan window function seperti RANK() sudah",
                    "kamu kenal dari kurikulum SQL.",
                    "",
                    "Untuk tujuh baris, SQLite dan DuckDB sama-sama selesai seketika.",
                    "Bedanya terasa di puluhan juta baris. SQLite membaca baris demi",
                    "baris dengan satu inti CPU, DuckDB membaca kolom yang dipakai saja",
                    "dengan semua inti. Seberapa jauh lebih cepatnya tergantung data dan",
                    "mesinnya, jadi ukur sendiri dengan datamu.",
                ],
            },
            {
                "heading": "DuckDB di Python",
                "code": "import duckdb\nimport pandas as pd\n\n# query berkas Parquet langsung dari jalurnya\nprint(duckdb.sql(\"\"\"\n    SELECT kota, sum(total) AS omzet\n    FROM 'penjualan.parquet'\n    GROUP BY ALL\n    ORDER BY omzet DESC\n\"\"\").fetchall())                  # [('Bandung', 215000), ('Bogor', 80000)]\n\n# DataFrame pandas bisa dipanggil langsung dengan nama variabelnya\ndf = pd.read_parquet(\"penjualan.parquet\")\nhasil = duckdb.sql(\"SELECT kota, count(*) AS n FROM df GROUP BY kota\").df()\n\n# database dalam berkas, lalu ekspor hasil ke Parquet\ncon = duckdb.connect(\"toko.duckdb\")\ncon.sql(\"CREATE TABLE penjualan AS FROM 'penjualan.parquet'\")\ncon.sql(\"COPY (SELECT * FROM penjualan WHERE kota = 'Bandung') \"\n        \"TO 'bandung.parquet' (FORMAT parquet)\")\ncon.close()",
            },
            {
                "heading": "SQL khas DuckDB",
                "body": [
                    "Hasil query bisa diambil dalam beberapa bentuk: .fetchall() untuk",
                    "list of tuple, .df() untuk DataFrame pandas, .pl() untuk DataFrame",
                    "Polars. Nama berkas boleh memakai pola, misalnya",
                    "'penjualan/*.parquet' untuk membaca semua berkas di folder itu",
                    "sekaligus. Untuk CSV, read_csv menebak sendiri pemisah dan tipe",
                    "kolomnya.",
                    "",
                    "DuckDB juga menambah beberapa singkatan yang nggak ada di SQLite.",
                    "Blok di bawah cuma untuk dibaca, karena aplikasi ini menjalankan",
                    "SQL dengan SQLite:",
                ],
                "bahasa": "teks",
                "code": """-- kelompokkan menurut semua kolom yang bukan agregat
SELECT kota, tanggal, sum(total) FROM penjualan GROUP BY ALL;

-- semua kolom kecuali satu
SELECT * EXCLUDE (tanggal) FROM penjualan;

-- FROM duluan; SELECT boleh dihilangkan
FROM penjualan WHERE kota = 'Bogor';

-- saring hasil window function tanpa subquery
SELECT * FROM penjualan
QUALIFY row_number() OVER (PARTITION BY kota ORDER BY total DESC) = 1;

-- ringkasan statistik tiap kolom: min, max, rata-rata, null
SUMMARIZE penjualan;""",
            },
            {
                "heading": "Memasang dan memakai dari terminal",
                "bahasa": "terminal",
                "code": """pip install duckdb                 # pustaka Python
duckdb toko.duckdb                 # CLI, unduh dari duckdb.org/install
duckdb -c "FROM 'penjualan.parquet' LIMIT 5"
duckdb -ui                         # antarmuka web lokal di browser""",
            },
            {
                "heading": "DuckDB, SQLite, atau PostgreSQL?",
                "body": [
                    "Pilih DuckDB untuk analisis di satu mesin: notebook, skrip laporan,",
                    "membersihkan berkas besar, atau mesin di balik dasbor kecil. Pilih",
                    "SQLite untuk menyimpan data aplikasi lokal, misalnya data aplikasi",
                    "HP atau desktop. Pilih PostgreSQL untuk backend aplikasi yang",
                    "dipakai banyak orang sekaligus.",
                    "",
                    "Jebakan: berkas .duckdb cuma boleh ditulis satu proses dalam satu",
                    "waktu. Kalau dua skrip mencoba menulis ke berkas yang sama, yang",
                    "kedua ditolak. DuckDB nggak cocok jadi database backend web yang",
                    "menerima ribuan transaksi kecil dari banyak pengguna.",
                    "",
                    "Kalau datanya tumbuh melewati satu laptop, ada MotherDuck, layanan",
                    "cloud berbayar yang menjalankan DuckDB di server. DuckDB juga",
                    "muncul lagi di bab berikutnya sebagai mesin lokal untuk dbt.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Analis data memakai DuckDB di notebook untuk meng-query berkas",
                    "Parquet ratusan juta baris tanpa cluster. Alat BI berbasis kode",
                    "Evidence memakai DuckDB sebagai mesin query-nya, dan banyak tim",
                    "memakai adapter dbt-duckdb untuk mencoba model data di laptop",
                    "sebelum dijalankan di gudang data cloud.",
                    "",
                    "Kasus kecil: bagian keuangan mengirim 12 berkas CSV transaksi,",
                    "satu per bulan (transaksi_01.csv sampai transaksi_12.csv), dengan",
                    "kolom tanggal, kategori, dan total. Kamu diminta tabel omzet per",
                    "bulan per kategori.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Taruh semua berkas di satu folder dan pasang DuckDB dengan pip",
                    "     install duckdb.",
                    "  2. Baca semuanya sekaligus dengan pola nama berkas, dan biarkan",
                    "     DuckDB menebak tipe kolomnya:",
                    "      SELECT strftime(tanggal, '%Y-%m') AS bulan, kategori,",
                    "             sum(total) AS omzet",
                    "      FROM read_csv('transaksi_*.csv')",
                    "      GROUP BY ALL",
                    "      ORDER BY bulan, omzet DESC;",
                    "  3. Kalau tanggal terbaca sebagai teks, ubah dulu dengan",
                    "     CAST(tanggal AS DATE).",
                    "  4. Cek jumlah barisnya dengan SELECT count(*) dan bandingkan",
                    "     dengan jumlah baris tiap berkas, supaya nggak ada bulan yang",
                    "     terlewat.",
                    "  5. Simpan hasilnya dengan COPY ... TO 'omzet.csv' kalau mau",
                    "     dibuka di spreadsheet, atau TO 'omzet.parquet' untuk dipakai",
                    "     ulang.",
                ],
            },
        ],
    },
    {
        "title": "23. Polars dan Dask Saat pandas Mulai Berat",
        "sections": [
            {
                "body": [
                    "pandas tetap alat olah tabel yang paling banyak dipakai. Di Python",
                    "Developers Survey 2024 (PSF dan JetBrains), 80% orang yang mengolah",
                    "data memakainya. Tapi ada tanda-tanda ia mulai kewalahan:",
                    "",
                    "  - MemoryError saat membaca berkas, karena pandas memuat semuanya",
                    "    ke RAM, dan biasanya butuh beberapa kali ukuran datanya.",
                    "  - Satu inti CPU sibuk 100% sementara tujuh inti lainnya diam.",
                    "  - Satu baris kode butuh beberapa menit, padahal datanya \"cuma\"",
                    "    beberapa gigabyte.",
                    "",
                    "Ada dua arah keluar. Pertama, alat yang lebih cepat di satu mesin:",
                    "Polars, atau DuckDB dari materi sebelumnya. Kedua, alat yang",
                    "membagi pekerjaan ke banyak inti atau banyak mesin: Dask, atau",
                    "Spark yang dibahas di bab Big Data.",
                ],
            },
            {
                "heading": "Polars: ekspresi, bukan index",
                "body": [
                    "Polars adalah pustaka DataFrame yang ditulis dengan Rust, memakai",
                    "model memori Arrow, dan otomatis memakai semua inti CPU. Versi",
                    "2.0.0 rilis 6 Oktober 2026, berlisensi MIT. Di survei yang sama,",
                    "15% pengolah data sudah memakainya.",
                    "",
                    "Ada dua beda besar dengan pandas. Polars nggak punya index baris,",
                    "jadi nggak ada loc, iloc, atau reset_index. Lalu operasi ditulis",
                    "sebagai ekspresi: pl.col(\"total\").sum() menggambarkan apa yang mau",
                    "dihitung, dan Polars yang memutuskan cara menghitungnya.",
                ],
                "code": """import polars as pl

df = pl.read_parquet("penjualan.parquet")

omzet = (df.group_by("kota")
           .agg(pl.col("total").sum().alias("omzet"))
           .sort("omzet", descending=True))
print(omzet)

bandung = (df.with_columns((pl.col("total") * 1.11).alias("total_ppn"))
             .filter(pl.col("kota") == "Bandung"))
print(bandung)""",
            },
            {
                "heading": "Mode lazy: rencana dulu, kerja belakangan",
                "body": [
                    "Kekuatan utama Polars ada di mode lazy. scan_parquet atau scan_csv",
                    "nggak membaca apa pun. Ia cuma mencatat rencana. Saat kamu memanggil",
                    ".collect(), pengoptimal query melihat seluruh rencana sekaligus,",
                    "lalu misalnya mendorong filter ke tahap baca berkas supaya baris",
                    "yang nggak perlu nggak pernah dimuat. .explain() menampilkan",
                    "rencana yang sudah dioptimalkan.",
                ],
                "code": """import polars as pl

rencana = (
    pl.scan_parquet("penjualan.parquet")
    .filter(pl.col("kota") == "Bandung")
    .group_by("tanggal")
    .agg(pl.col("total").sum())
    .sort("tanggal")
)
print(rencana.explain())   # ada SELECTION: col("kota") == "Bandung"
                           # di dalam langkah Parquet SCAN
print(rencana.collect())""",
            },
            {
                "heading": "Yang berubah di Polars 2.0",
                "body": [
                    "Polars 2.0 baru rilis, jadi banyak tutorial dan jawaban forum masih",
                    "memakai Polars 1.x. Yang paling sering bikin bingung:",
                    "",
                    "  - collect() pada query lazy sekarang memakai mesin streaming",
                    "    secara bawaan, yang memproses data per potongan sehingga muat",
                    "    walau datanya lebih besar dari RAM. Mesin lama bisa dipilih",
                    "    dengan collect(engine=\"in-memory\").",
                    "  - Urutan baris hasil join dan beberapa operasi lain nggak",
                    "    dijamin lagi kecuali kamu memberi maintain_order=True. Kalau",
                    "    urutan penting, tambahkan .sort() di akhir, seperti contoh di",
                    "    atas.",
                    "  - melt() sudah dihapus, gantinya unpivot(). with_row_count()",
                    "    diganti with_row_index().",
                    "",
                    "Jebakan: kode dari tutorial lama yang lolos tanpa error bisa tetap",
                    "memberi urutan baris yang beda dari sebelumnya. Kalau hasilnya",
                    "dibandingkan baris per baris dengan laporan lama, urutkan dulu.",
                ],
            },
            {
                "heading": "Meniru lazy evaluation dengan generator",
                "code": """from itertools import islice

DATA = [
    {"id": 1, "kota": "Bandung", "total": 120},
    {"id": 2, "kota": "Bogor", "total": 80},
    {"id": 3, "kota": "Bandung", "total": 95},
    {"id": 4, "kota": "Depok", "total": 150},
    {"id": 5, "kota": "Bandung", "total": 130},
    {"id": 6, "kota": "Bogor", "total": 110},
]

def baca(sumber):
    for baris in sumber:
        print(f"  membaca baris {baris['id']}")
        yield baris

def saring(baris_baris, syarat):
    return (b for b in baris_baris if syarat(b))

def pilih(baris_baris, kolom):
    return ({k: b[k] for k in kolom} for b in baris_baris)

rencana = pilih(saring(baca(DATA), lambda b: b["kota"] == "Bandung"),
                ["id", "total"])
print("rencana sudah dibuat, belum ada baris yang dibaca")

print("ambil 2 hasil pertama:")
print(list(islice(rencana, 2)))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  rencana sudah dibuat, belum ada baris yang dibaca",
                    "  ambil 2 hasil pertama:",
                    "    membaca baris 1",
                    "    membaca baris 2",
                    "    membaca baris 3",
                    "  [{'id': 1, 'total': 120}, {'id': 3, 'total': 95}]",
                    "",
                    "Generator Python juga malas: fungsi yang memakai yield baru",
                    "bekerja saat hasilnya diminta. Membuat rencana nggak membaca satu",
                    "baris pun. Waktu islice minta dua hasil, baris dibaca satu per satu",
                    "sampai dua baris Bandung ketemu, lalu berhenti. Baris 4 sampai 6",
                    "nggak pernah disentuh.",
                    "",
                    "Polars bekerja dengan ide yang sama, plus kemampuan yang nggak",
                    "dimiliki rantai generator: sebelum mulai, ia membaca seluruh",
                    "rencana dan menyusun ulang langkahnya supaya paling hemat.",
                ],
            },
            {
                "heading": "Dask: pandas yang dipecah jadi banyak potongan",
                "body": [
                    "Dask mengambil pendekatan lain. DataFrame Dask adalah kumpulan",
                    "banyak DataFrame pandas kecil yang disebut partisi. Tiap operasi",
                    "dicatat sebagai graf tugas (task graph), lalu .compute() menyuruh",
                    "penjadwal Dask menjalankan tugas-tugas itu paralel, di semua inti",
                    "laptop atau di banyak mesin lewat dask.distributed.",
                    "",
                    "Karena tiap partisi adalah pandas, API-nya mirip sekali dengan",
                    "pandas, dan kode lama bisa dipindah dengan sedikit perubahan. Versi stabil",
                    "terbaru saat materi ini ditulis adalah 2026.8.0. Dask memakai",
                    "nomor versi berbentuk tanggal (tahun.bulan.perbaikan), lisensinya",
                    "BSD-3-Clause. Di survei PSF dan JetBrains 2024, 7% pengolah data",
                    "memakainya. Ia masih aktif dikembangkan, tapi untuk satu mesin kini",
                    "sering kalah pamor dari Polars dan DuckDB, dan untuk cluster besar",
                    "dari Spark.",
                ],
                "code": """import dask.dataframe as dd

ddf = dd.read_parquet("penjualan/*.parquet")   # belum dibaca
omzet = ddf.groupby("kota")["total"].sum()      # baru rencana
print(omzet.compute())                          # dijalankan di sini""",
            },
            {
                "heading": "Pecah, kerjakan, gabung",
                "code": """from concurrent.futures import ThreadPoolExecutor

angka = list(range(1, 1_000_001))      # sejuta baris "data"
potongan = [angka[i:i + 250_000] for i in range(0, len(angka), 250_000)]

def jumlah_potongan(p):
    return sum(p)

with ThreadPoolExecutor(max_workers=4) as pekerja:
    hasil_sebagian = list(pekerja.map(jumlah_potongan, potongan))

print("jumlah per potongan:", hasil_sebagian)
print("total:", sum(hasil_sebagian))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  jumlah per potongan: [31250125000, 93750125000, 156250125000, 218750125000]",
                    "  total: 500000500000",
                    "",
                    "Ini bentuk paling sederhana dari yang dikerjakan Dask: data dipecah",
                    "jadi empat partisi, tiap partisi dijumlahkan sendiri, lalu hasil",
                    "sebagiannya digabung. Graf tugasnya cuma dua lapis: empat tugas",
                    "jumlah_potongan, lalu satu tugas sum di akhir.",
                    "",
                    "Ingat: di Python biasa, thread nggak mempercepat hitungan murni",
                    "karena GIL, kunci yang membuat cuma satu thread menjalankan kode",
                    "Python pada satu waktu. Contoh ini cuma menunjukkan bentuknya. Dask",
                    "jadi cepat karena kerja beratnya dilakukan pandas dan NumPy, yang",
                    "melepas GIL saat menghitung, atau karena memakai banyak proses dan",
                    "banyak mesin.",
                ],
            },
            {
                "heading": "Memilih alat",
                "body": [
                    "Pegangan kasar menurut ukuran data dan bentuk pekerjaan:",
                    "",
                    "  - Muat di RAM dengan lega (sampai beberapa GB): pandas sudah",
                    "    cukup, dan paling banyak contoh serta bantuannya.",
                    "  - Lebih besar dari nyaman, tapi masih satu mesin (puluhan GB):",
                    "    Polars mode lazy kalau kamu suka gaya DataFrame, DuckDB kalau",
                    "    kamu lebih nyaman dengan SQL. Simpan datanya sebagai Parquet.",
                    "  - Lebih besar dari satu mesin, atau perusahaan sudah punya",
                    "    cluster: Dask kalau tim terbiasa pandas dan NumPy, Spark kalau",
                    "    datanya terabyte atau platformnya sudah Spark.",
                    "",
                    "Ketiganya bisa saling oper data lewat Arrow:",
                    "pl.from_pandas(df), df_polars.to_pandas(), duckdb.sql(...).pl().",
                    "Jadi kamu nggak harus memilih satu untuk seluruh proyek.",
                    "",
                    "Jebakan: untuk data kecil, Dask justru lebih lambat dari pandas,",
                    "karena menyusun dan menjadwalkan graf tugas butuh waktu sendiri.",
                    "Pakai alat terdistribusi hanya kalau datanya memang nggak muat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim analitik di perusahaan rintisan sering menganalisis log",
                    "aplikasi atau data transaksi puluhan gigabyte langsung di laptop",
                    "kerja dengan Polars atau DuckDB, tanpa menunggu tim infrastruktur",
                    "menyiapkan cluster.",
                    "",
                    "Kasus kecil: kamu punya log akses web setahun, 20 GB dalam 365",
                    "berkas CSV harian. Laptopmu punya RAM 16 GB. Kamu diminta jumlah",
                    "kunjungan per halaman per bulan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jangan pd.read_csv semua berkas sekaligus. 20 GB teks bisa",
                    "     butuh RAM beberapa kali lipat setelah jadi DataFrame.",
                    "  2. Ubah berkas harian jadi Parquet, cukup sekali. Ukurannya akan",
                    "     jauh lebih kecil dan kolomnya bertipe.",
                    "  3. Tulis query lazy dengan Polars: scan_parquet(\"log/*.parquet\"),",
                    "     pilih kolom halaman dan waktu, buat kolom bulan, lalu group_by",
                    "     dan agg dengan pl.len().",
                    "  4. Panggil .collect(). Di Polars 2.0, mesin streaming dipakai",
                    "     secara bawaan, jadi data diproses per potongan dan nggak perlu",
                    "     muat seluruhnya di RAM.",
                    "  5. Hasilnya cuma ribuan baris. Ubah ke pandas dengan .to_pandas()",
                    "     kalau mau digambar dengan Matplotlib.",
                ],
            },
        ],
    },
    {
        "title": "24. R untuk Pengguna Python",
        "sections": [
            {
                "body": [
                    "R adalah bahasa pemrograman yang dibuat khusus untuk statistik",
                    "dan analisis data. Ia lahir di University of Auckland, Selandia",
                    "Baru, dibuat Ross Ihaka dan Robert Gentleman pada awal 1990-an",
                    "sebagai versi terbuka dari bahasa S buatan Bell Labs. R 1.0 rilis",
                    "tahun 2000. Versi stabil terbaru saat materi ini ditulis (Oktober",
                    "2026) adalah 4.6.1, rilis 24 Juni 2026, berlisensi GPL.",
                    "",
                    "Kekuatan utamanya ada di paket. Gudang paket resminya bernama",
                    "CRAN, isinya lebih dari 20.000 paket, dari uji statistik yang",
                    "jarang dipakai sampai model survei dan analisis genetika. Untuk",
                    "bioinformatika ada gudang terpisah bernama Bioconductor.",
                    "",
                    "Di industri, R kalah populer dari Python. Survei Stack Overflow",
                    "2025 mencatat 4,9% responden memakai R, sementara Python di atas",
                    "50%. Tapi di kampus, rumah sakit, lembaga riset, dan farmasi, R",
                    "masih sering jadi bahasa utama. Kamu nggak harus pindah ke R.",
                    "Yang sering terjadi: kamu dapat skrip R dari dosen, peneliti, atau",
                    "rekan kerja, dan harus bisa membacanya. Materi ini untuk itu.",
                ],
            },
            {
                "heading": "Memasang R dan IDE-nya",
                "body": [
                    "Di Fedora, R ada di repositori resmi, jadi cukup satu perintah.",
                    "Skrip R berakhiran .R dan dijalankan dengan Rscript, mirip",
                    "python3 nama.py. Perintah R tanpa argumen membuka konsol",
                    "interaktif, mirip REPL Python.",
                    "",
                    "Untuk IDE ada dua pilihan dari Posit, perusahaan di balik",
                    "tidyverse dan Shiny. RStudio adalah IDE R yang paling lama dipakai",
                    "(versi terbaru 2026.10.0, edisi open source-nya gratis).",
                    "Positron adalah IDE data science yang lebih baru untuk R dan Python",
                    "sekaligus, dibangun di atas basis terbuka VS Code.",
                    "Positron gratis, tapi lisensinya Elastic License 2.0, artinya",
                    "kodenya bisa dibaca tapi bukan open source dalam arti ketat.",
                ],
                "bahasa": "terminal",
                "code": """sudo dnf install R          # R 4.6.1 di repositori Fedora 44
Rscript halo.R              # jalankan skrip
R                           # konsol interaktif, keluar dengan q()""",
            },
            {
                "heading": "Sintaks dasar",
                "bahasa": "r",
                "code": """# vektor: kumpulan nilai bertipe sama, dibuat dengan c()
nilai <- c(78, 85, 62, 90, 71)

nilai[1]            # 78, indeks dimulai dari 1
nilai[2:3]          # 85 62
nilai[-1]           # semua kecuali elemen pertama: 85 62 90 71
nilai * 2           # tiap elemen dikali 2, tanpa loop
mean(nilai)         # 77.2
nilai[nilai > 75]   # 78 85 90

nilai_kosong <- c(78, NA, 90)
mean(nilai_kosong)                 # NA
mean(nilai_kosong, na.rm = TRUE)   # 84

lulus <- function(x, batas = 75) {
  x >= batas        # nilai terakhir otomatis dikembalikan
}
lulus(nilai)        # TRUE TRUE FALSE TRUE FALSE

for (n in nilai) {
  if (n >= 85) print(paste("istimewa:", n))
}""",
            },
            {
                "heading": "Yang bikin orang Python tersandung",
                "body": [
                    "Kebanyakan sintaks R bisa ditebak, tapi beberapa hal kebalikan",
                    "dari kebiasaan Python:",
                    "",
                    "  - Indeks mulai dari 1. nilai[1] adalah elemen pertama, dan",
                    "    nilai[0] menghasilkan vektor kosong tanpa error.",
                    "  - Indeks negatif berarti buang. Di Python, nilai[-1] adalah",
                    "    elemen terakhir. Di R, artinya semua elemen kecuali yang",
                    "    pertama. Elemen terakhir di R ditulis nilai[length(nilai)].",
                    "  - Penugasan memakai <-. Tanda = juga jalan di kebanyakan tempat,",
                    "    tapi gaya yang lazim adalah <-, dan = dipakai untuk argumen",
                    "    fungsi seperti na.rm = TRUE.",
                    "  - Hampir semua operasi tervektorisasi. nilai * 2 langsung bekerja",
                    "    untuk seluruh vektor, mirip NumPy, jadi loop for jarang perlu.",
                    "  - NA berarti nilai hilang, mirip NaN di pandas. NULL berarti",
                    "    nggak ada objeknya sama sekali. Fungsi seperti mean() memberi NA",
                    "    kalau ada satu NA, kecuali diberi na.rm = TRUE.",
                    "  - Titik di nama cuma huruf biasa. data.frame dan na.rm bukan",
                    "    akses atribut seperti di Python.",
                    "",
                    "Jebakan: vektor yang panjangnya beda didaur ulang diam saja.",
                    "c(1, 2, 3, 4) + c(10, 20) menghasilkan 11 22 13 24, karena vektor",
                    "pendek diulang sampai panjangnya sama. R baru memperingatkan kalau",
                    "panjang yang satu bukan kelipatan yang lain.",
                ],
            },
            {
                "heading": "data.frame dan factor",
                "body": [
                    "Tabel di R disebut data.frame, dan sudah ada sejak awal, jauh",
                    "sebelum pandas meniru konsepnya. Tiap kolom adalah vektor. Kolom",
                    "diambil dengan tanda dolar: siswa$nilai.",
                    "",
                    "Data kategori, misalnya kelas A dan B, biasanya disimpan sebagai",
                    "factor: vektor yang mengingat daftar kategori yang sah. Model",
                    "statistik di R memakai factor untuk tahu kolom mana yang",
                    "kategori.",
                ],
                "bahasa": "r",
                "code": """siswa <- data.frame(
  nama  = c("Ani", "Budi", "Citra", "Dodi"),
  kelas = factor(c("A", "B", "A", "B")),
  nilai = c(78, 85, 62, 90)
)

str(siswa)                            # tipe tiap kolom
siswa$nilai                           # 78 85 62 90
siswa[siswa$nilai > 75, ]             # baris yang lolos, semua kolom
siswa[order(-siswa$nilai), "nama"]    # Dodi Budi Ani Citra
tapply(siswa$nilai, siswa$kelas, mean)  # A: 70, B: 87.5
summary(siswa$nilai)                  # min, kuartil, rata-rata, max""",
            },
            {
                "heading": "Python dan R berdampingan",
                "body": [
                    "Kalau kamu sudah bisa pandas, kebanyakan kode R tinggal",
                    "diterjemahkan kepala. Bentuk [baris, kolom] di R, misalnya",
                    "siswa[siswa$nilai > 75, ], mirip df.loc[df[\"nilai\"] > 75] di",
                    "pandas. Bedanya, koma di R wajib ada walau bagian kolomnya kosong.",
                    "",
                    "  hal                  Python (pandas)          R",
                    "  buat list/vektor     [78, 85, 62]             c(78, 85, 62)",
                    "  elemen pertama       x[0]                     x[1]",
                    "  rata-rata            statistics.mean(x)       mean(x)",
                    "  baca CSV             pd.read_csv(\"a.csv\")     read.csv(\"a.csv\")",
                    "  satu kolom           df[\"nilai\"]              df$nilai",
                    "  nilai hilang         NaN / None               NA",
                    "  pasang paket         pip install x            install.packages(\"x\")",
                    "  pakai paket          import x                 library(x)",
                ],
            },
            {
                "heading": "Kapan memilih R",
                "body": [
                    "R unggul kalau pekerjaannya statistik murni dan hasilnya ditulis",
                    "untuk dibaca orang. Contohnya uji statistik yang jarang, model",
                    "campuran (paket lme4), analisis kelangsungan hidup (paket",
                    "survival), grafik publikasi dengan ggplot2, dan laporan riset yang",
                    "bisa diulang.",
                    "Banyak metode statistik baru terbit pertama kali sebagai paket R.",
                    "",
                    "Python unggul kalau hasil analisisnya harus jadi bagian dari",
                    "aplikasi: model machine learning yang dipasang di server, pipeline",
                    "data, atau API. Ekosistem deep learning dan LLM juga hampir",
                    "seluruhnya di Python.",
                    "",
                    "Banyak tim memakai keduanya. Paket R reticulate bisa memanggil kode",
                    "Python dari R, dan pustaka Python rpy2 melakukan kebalikannya.",
                    "Positron juga sengaja dibuat supaya dua bahasa itu nyaman di satu",
                    "jendela.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Ahli epidemiologi dan biostatistik banyak memakai R. Selama",
                    "pandemi Covid-19, misalnya, paket R seperti EpiEstim dipakai untuk",
                    "memperkirakan angka reproduksi penyakit dari data kasus harian.",
                    "Di farmasi, analisis uji klinis juga makin sering ditulis dengan R",
                    "di samping SAS.",
                    "",
                    "Kasus kecil: dosen pembimbingmu mengirim skrip analisis.R untuk",
                    "data kuesioner skripsi. Kamu terbiasa Python, dan diminta",
                    "menjalankan ulang skripnya dengan data terbaru.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang R dengan sudo dnf install R, lalu buka skripnya di",
                    "     Positron atau RStudio supaya bisa dijalankan baris per baris.",
                    "  2. Cari semua baris library(...). Paket yang belum ada dipasang",
                    "     dulu dari konsol R:",
                    "      install.packages(c(\"dplyr\", \"ggplot2\"))",
                    "  3. Cari baris yang membaca data, misalnya read.csv(\"data.csv\"),",
                    "     dan arahkan ke berkas terbaru.",
                    "  4. Waspadai jebakan Python: indeks mulai 1, [-1] berarti buang",
                    "     elemen pertama, dan NA yang membuat mean() ikut NA.",
                    "  5. Jalankan dengan Rscript analisis.R, lalu bandingkan angka",
                    "     ringkasannya dengan hasil lama dosenmu sebelum memakai",
                    "     hasil baru.",
                ],
            },
        ],
    },
    {
        "title": "25. Tidyverse: dplyr dan ggplot2",
        "sections": [
            {
                "body": [
                    "Tidyverse adalah kumpulan paket R yang dirancang dengan gaya yang",
                    "sama, dipimpin Hadley Wickham di Posit. Isinya antara lain dplyr",
                    "(mengolah tabel), ggplot2 (grafik), tidyr (merapikan bentuk",
                    "tabel), readr (membaca CSV), purrr (bekerja dengan list), tibble",
                    "(data.frame versi modern), stringr (teks), forcats (factor), dan",
                    "lubridate (tanggal). Memanggil library(tidyverse) memuat semuanya",
                    "sekaligus.",
                    "",
                    "Paket gabungan tidyverse sendiri jarang dirilis (versi 2.0.0 sejak",
                    "2023), tapi anggotanya rutin diperbarui. Saat materi ini ditulis",
                    "(Oktober 2026), dplyr ada di versi 1.2.1 dan ggplot2 di 4.0.3.",
                    "Semuanya berlisensi MIT. Survei Stack Overflow 2024 mencatat 1,7%",
                    "responden memakai tidyverse.",
                    "",
                    "Gaya bersamanya bertumpu pada data rapi (tidy data): tiap variabel",
                    "satu kolom, tiap pengamatan satu baris, tiap nilai satu sel. Tabel",
                    "nilai yang punya kolom uts_matematika, uts_fisika, uas_matematika",
                    "belum rapi, karena jenis ujian dan mata pelajaran tersembunyi di",
                    "nama kolom.",
                ],
            },
            {
                "heading": "Pipe: membaca dari kiri ke kanan",
                "body": [
                    "Tanpa pipe, langkah berurutan ditulis bersarang:",
                    "arrange(summarise(group_by(filter(data, ...), kota), ...)). Kamu",
                    "harus membaca dari dalam ke luar.",
                    "",
                    "Pipe |> mengoper hasil di kirinya jadi argumen pertama fungsi di",
                    "kanannya. data |> filter(...) sama dengan filter(data, ...). Pipe",
                    "bawaan ini ada sejak R 4.1 (2021). Di kode yang lebih tua kamu",
                    "bakal ketemu %>% dari paket magrittr, yang kerjanya hampir sama.",
                    "Kalau dibaca keras, pipe enak diucapkan \"lalu\".",
                ],
            },
            {
                "heading": "Lima kata kerja dplyr",
                "bahasa": "r",
                "code": """library(dplyr)

penjualan <- tibble(
  kota   = c("Bandung", "Bandung", "Bogor", "Bandung", "Depok", "Bogor", "Depok"),
  produk = c("kopi", "teh", "kopi", "roti", "teh", "roti", "kopi"),
  harga  = c(25000, 15000, 25000, 12000, 15000, 12000, 25000),
  jumlah = c(2, 0, 1, 3, 4, 2, 1)
)

penjualan |>
  filter(jumlah > 0) |>
  mutate(total = harga * jumlah) |>
  group_by(kota) |>
  summarise(transaksi = n(), omzet = sum(total)) |>
  arrange(desc(omzet))""",
            },
            {
                "body": [
                    "Hasilnya di konsol R:",
                    "",
                    "  # A tibble: 3 × 3",
                    "    kota    transaksi omzet",
                    "    <chr>       <int> <dbl>",
                    "  1 Bandung         2 86000",
                    "  2 Depok           2 85000",
                    "  3 Bogor           2 49000",
                    "",
                    "Tiap kata kerja melakukan satu hal:",
                    "",
                    "  - filter() memilih baris. Baris teh di Bandung dengan jumlah 0",
                    "    dibuang.",
                    "  - mutate() menambah atau mengubah kolom, di sini total.",
                    "  - group_by() menandai kelompok. Tabelnya belum berubah, tapi",
                    "    langkah sesudahnya dikerjakan per kota.",
                    "  - summarise() meringkas tiap kelompok jadi satu baris. n()",
                    "    menghitung barisnya.",
                    "  - arrange() mengurutkan, dan desc() membaliknya jadi menurun.",
                    "",
                    "Ada juga select() untuk memilih kolom dan keluarga join, misalnya",
                    "left_join(), untuk menggabung tabel. Nama-namanya sengaja dibuat",
                    "seperti kalimat, jadi pipeline dplyr bisa dibaca orang yang belum",
                    "pernah belajar R.",
                ],
            },
            {
                "heading": "Padanannya di SQL",
                "bahasa": "sql",
                "code": """CREATE TABLE penjualan (kota TEXT, produk TEXT, harga INTEGER, jumlah INTEGER);
INSERT INTO penjualan VALUES
  ('Bandung', 'kopi', 25000, 2), ('Bandung', 'teh', 15000, 0),
  ('Bogor', 'kopi', 25000, 1),   ('Bandung', 'roti', 12000, 3),
  ('Depok', 'teh', 15000, 4),    ('Bogor', 'roti', 12000, 2),
  ('Depok', 'kopi', 25000, 1);

SELECT kota,
       COUNT(*) AS transaksi,
       SUM(harga * jumlah) AS omzet
FROM penjualan
WHERE jumlah > 0
GROUP BY kota
ORDER BY omzet DESC;""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Bandung|2|86000",
                    "  Depok|2|85000",
                    "  Bogor|2|49000",
                    "",
                    "Angkanya sama dengan versi dplyr, karena kata kerja dplyr memang",
                    "sejajar dengan klausa SQL:",
                    "",
                    "  dplyr                    SQL                pandas",
                    "  filter()                 WHERE              df[syarat]",
                    "  select()                 SELECT kolom       df[[\"a\", \"b\"]]",
                    "  mutate()                 kolom hitungan     df.assign()",
                    "  group_by() + summarise() GROUP BY + agregat groupby().agg()",
                    "  arrange()                ORDER BY           sort_values()",
                    "  left_join()              LEFT JOIN          merge(how=\"left\")",
                    "",
                    "Paket dbplyr bahkan bisa menerjemahkan pipeline dplyr jadi SQL",
                    "dan menjalankannya langsung di database.",
                ],
            },
            {
                "heading": "ggplot2: grammar of graphics",
                "body": [
                    "ggplot2 membangun grafik dari lapisan, mengikuti ide grammar of",
                    "graphics. Lapisan pertama adalah data. Lalu pemetaan estetika",
                    "(aes): kolom mana jadi sumbu x, sumbu y, dan warna. Lalu geom,",
                    "yaitu bentuk yang digambar: batang, titik, atau garis. Lapisan",
                    "ditambah dengan tanda +. Ide yang sama",
                    "dipakai Altair di Python, yang dibahas di bab visualisasi.",
                    "",
                    "ggplot2 4.0 rilis September 2025. Bagian dalamnya dipindah ke",
                    "sistem objek baru bernama S7. Kode grafik biasa tetap jalan, tapi",
                    "paket ekstensi lama yang mengutak-atik bagian dalam ggplot2 bisa",
                    "perlu diperbarui.",
                ],
                "bahasa": "r",
                "code": """library(ggplot2)

grafik <- ggplot(penjualan, aes(x = kota, y = harga * jumlah, fill = produk)) +
  geom_col() +
  labs(title = "Omzet per kota", x = NULL, y = "Rupiah") +
  theme_minimal()

ggsave("omzet.png", grafik, width = 6, height = 4)""",
            },
            {
                "heading": "tidyr dan jebakan yang sering muncul",
                "body": [
                    "tidyr merapikan bentuk tabel. pivot_longer() mengubah tabel lebar",
                    "(satu kolom per produk) jadi panjang (satu baris per kota dan",
                    "produk), dan pivot_wider() kebalikannya. Di tutorial lama kamu",
                    "bakal ketemu gather() dan spread(). Keduanya sudah digantikan dua",
                    "fungsi pivot tadi dan nggak disarankan lagi untuk kode baru.",
                    "",
                    "Jebakan: group_by() menempel pada tabel sampai dilepas. Kalau",
                    "hasil group_by() disimpan ke variabel lalu dipakai lagi, mutate()",
                    "berikutnya ikut dihitung per kelompok. Lepaskan dengan ungroup(),",
                    "atau pakai argumen .by yang berlaku untuk satu langkah saja:",
                    "summarise(omzet = sum(total), .by = kota).",
                    "",
                    "Jebakan: sum(), mean(), dan teman-temannya memberi NA kalau ada",
                    "satu nilai NA di kelompok itu. Tambahkan na.rm = TRUE kalau memang",
                    "nilai hilang boleh diabaikan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Buku R for Data Science edisi kedua, ditulis Hadley Wickham dan",
                    "rekan, bisa dibaca gratis di r4ds.hadley.nz dan seluruhnya memakai",
                    "tidyverse. Komunitasnya juga menjalankan TidyTuesday: tiap minggu",
                    "satu dataset baru dibagikan, dan orang dari seluruh dunia",
                    "memamerkan grafik ggplot2 buatannya.",
                    "",
                    "Kasus kecil: wali kelas punya tabel nilai (nama, kelas, mapel,",
                    "nilai) untuk tiga kelas. Ia minta rata-rata tiap kelas per mapel",
                    "dan grafik batangnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca datanya dengan readr: nilai <- read_csv(\"nilai.csv\").",
                    "  2. Pastikan bentuknya rapi: satu baris per siswa per mapel. Kalau",
                    "     tiap mapel jadi kolom sendiri, ubah dulu dengan",
                    "     pivot_longer().",
                    "  3. Ringkas dengan dplyr:",
                    "      ringkas <- nilai |>",
                    "        summarise(rata = mean(nilai, na.rm = TRUE),",
                    "                  .by = c(kelas, mapel))",
                    "  4. Gambar dengan ggplot2, satu panel per mapel:",
                    "      ggplot(ringkas, aes(kelas, rata)) + geom_col() +",
                    "        facet_wrap(~ mapel)",
                    "  5. Simpan dengan ggsave() dan periksa satu angka dengan tangan,",
                    "     misalnya rata-rata matematika kelas A, sebelum dikirim.",
                ],
            },
        ],
    },
    {
        "title": "26. Peta Ekosistem R: Shiny, Quarto, tidymodels",
        "sections": [
            {
                "body": [
                    "Di luar dplyr dan ggplot2, ada beberapa paket dan alat R yang",
                    "sering muncul di lowongan kerja dan di proyek kampus. Versinya di",
                    "bawah adalah versi stabil terbaru saat materi ini ditulis",
                    "(Oktober 2026):",
                    "",
                    "  nama        untuk apa                         versi    status",
                    "  Shiny       aplikasi web interaktif           1.14.0   aktif",
                    "  R Markdown  laporan teks + kode R             2.32     dirawat",
                    "  Quarto      dokumen, slide, situs, buku       1.10.19  aktif",
                    "  tidymodels  machine learning gaya tidyverse   1.5.0    aktif",
                    "  data.table  olah tabel besar dengan cepat     1.18.6.1 matang",
                    "",
                    "Tiap bagian di bawah membahas satu alat: masalah yang dipecahkan,",
                    "bentuk kodenya, dan padanannya di Python.",
                ],
            },
            {
                "heading": "Shiny: aplikasi web tanpa JavaScript",
                "body": [
                    "Shiny dari Posit membuat aplikasi web interaktif cukup dengan R.",
                    "Aplikasinya punya dua bagian: ui (apa yang tampil) dan server (apa",
                    "yang dihitung). Kuncinya reaktivitas: output yang memakai",
                    "input$n otomatis dihitung ulang setiap kali slider n digeser, dan",
                    "cuma output itu yang dihitung ulang.",
                    "",
                    "Bandingkan dengan Streamlit yang menjalankan ulang seluruh skrip",
                    "tiap ada interaksi, seperti dibahas di materi Aplikasi Data:",
                    "Streamlit, Gradio, dan Dash. Shiny juga punya versi Python",
                    "bernama Shiny for Python. Aplikasinya bisa dipasang di",
                    "shinyapps.io, di Posit Connect, atau dijalankan sepenuhnya di",
                    "browser lewat Shinylive.",
                ],
                "bahasa": "r",
                "code": """library(shiny)

ui <- fluidPage(
  sliderInput("n", "Jumlah angka acak", min = 10, max = 500, value = 100),
  plotOutput("histogram")
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    hist(rnorm(input$n), main = paste(input$n, "angka acak"))
  })
}

shinyApp(ui, server)""",
            },
            {
                "heading": "R Markdown dan Quarto: laporan yang bisa diulang",
                "body": [
                    "Laporan analisis biasanya dibuat dengan menyalin angka dan grafik",
                    "ke dokumen Word. Begitu datanya diperbarui, semua harus disalin",
                    "ulang. R Markdown memecahkan ini: teks Markdown dan potongan kode",
                    "R ditulis di satu berkas .Rmd, lalu dirender jadi HTML, PDF, atau",
                    "Word. Angka di laporan selalu hasil kode terbaru.",
                    "",
                    "Quarto adalah penerusnya dari Posit. Bedanya, Quarto nggak terikat",
                    "R: berkas .qmd bisa berisi kode R, Python, Julia, atau Observable",
                    "JS, dan bisa dirender jadi dokumen, slide, situs web, sampai buku.",
                    "R Markdown masih dirawat, tapi untuk proyek baru Posit menyarankan",
                    "Quarto. Quarto adalah program terminal tersendiri, jadi dipasang",
                    "terpisah dari R. RStudio sudah membawanya, dan untuk Fedora ada",
                    "berkas unduhan di quarto.org.",
                ],
                "bahasa": "markdown",
                "code": """---
title: "Laporan Penjualan September"
format: html
---

Omzet bulan ini dihitung langsung dari data kasir.

```{r}
penjualan <- read.csv("penjualan.csv")
sum(penjualan$total)
```""",
            },
            {
                "heading": "Merender laporan",
                "bahasa": "terminal",
                "code": """quarto render laporan.qmd                  # jadi laporan.html
quarto render laporan.qmd --to pdf         # butuh LaTeX
quarto install tinytex                     # LaTeX kecil untuk PDF""",
            },
            {
                "heading": "tidymodels: machine learning gaya tidyverse",
                "body": [
                    "tidymodels adalah kumpulan paket untuk machine learning di R,",
                    "penerus modern paket caret. Kedudukannya mirip scikit-learn di",
                    "Python. Paketnya dibagi menurut tugas:",
                    "",
                    "  - rsample membagi data latih dan uji.",
                    "  - recipes menyiapkan fitur.",
                    "  - parsnip menyediakan model dengan satu antarmuka untuk banyak",
                    "    mesin.",
                    "  - workflows merangkai langkahnya, dan tune mencari hyperparameter.",
                    "  - yardstick menghitung metrik.",
                ],
                "bahasa": "r",
                "code": """library(tidymodels)

set.seed(42)
bagi  <- initial_split(mtcars, prop = 0.75)
latih <- training(bagi)
uji   <- testing(bagi)

model <- linear_reg() |> set_engine("lm")
hasil <- model |> fit(mpg ~ wt + hp, data = latih)

predict(hasil, uji) |>
  bind_cols(uji) |>
  rmse(truth = mpg, estimate = .pred)""",
            },
            {
                "heading": "data.table: cepat dan ringkas",
                "body": [
                    "data.table adalah alternatif dplyr untuk data besar. Ia terkenal",
                    "cepat dan hemat memori karena banyak operasinya mengubah tabel",
                    "tanpa menyalin. Sintaksnya padat: DT[i, j, by], artinya baris mana",
                    "(i), hitung apa (j), dikelompokkan menurut apa (by). Lisensinya",
                    "MPL 2.0.",
                    "",
                    "Kalau kamu suka gaya dplyr tapi butuh kecepatan data.table, paket",
                    "dtplyr menerjemahkan yang satu ke yang lain. Untuk data yang lebih",
                    "besar dari RAM, paket arrow dan duckdb versi R bekerja dengan",
                    "Parquet persis seperti di bab sebelumnya.",
                ],
                "bahasa": "r",
                "code": """library(data.table)

dt <- data.table(
  kota  = c("Bandung", "Bogor", "Bandung", "Depok"),
  total = c(50000, 25000, 36000, 60000)
)

dt[total > 30000, .(omzet = sum(total), n = .N), by = kota]
# Bandung 86000 2, Depok 60000 1

dt[, pajak := total * 0.11]     # tambah kolom tanpa menyalin tabel""",
            },
            {
                "heading": "Mana yang dipakai untuk proyek baru",
                "body": [
                    "  - Laporan dan dokumen: Quarto. R Markdown cukup dipelajari untuk",
                    "    membaca dan merawat berkas .Rmd lama.",
                    "  - Aplikasi interaktif untuk tim non-teknis: Shiny, kalau timnya",
                    "    berbasis R. Kalau berbasis Python, Shiny for Python atau",
                    "    Streamlit.",
                    "  - Machine learning di R: tidymodels. caret masih ada di banyak",
                    "    tutorial, tapi pengembangnya sendiri kini memusatkan tenaga ke",
                    "    tidymodels.",
                    "  - Olah data: dplyr untuk kebanyakan orang, data.table kalau",
                    "    datanya puluhan juta baris dan kecepatan jadi masalah.",
                    "",
                    "Jebakan: quarto render ke PDF butuh LaTeX. Kalau muncul error soal",
                    "LaTeX yang nggak ketemu, pasang TinyTeX dengan quarto install",
                    "tinytex, atau render ke HTML dulu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lembaga riset dan tim analitik memakai Quarto untuk laporan rutin,",
                    "buku teknis, dan situs dokumentasi. Buku R for Data Science edisi",
                    "kedua, misalnya, dibangun dengan Quarto. Dasbor Shiny sering",
                    "dipakai di rumah sakit dan universitas untuk alat analisis yang",
                    "dioperasikan orang tanpa latar pemrograman.",
                    "",
                    "Kasus kecil: tiap awal bulan kamu membuat laporan penjualan yang",
                    "isinya sama, cuma datanya beda. Selama ini kamu menyalin angka ke",
                    "Word secara manual, dan dua kali ketahuan salah ketik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan isi laporan ke laporan.qmd: teks penjelasan, lalu",
                    "     potongan kode R yang membaca data dan menghitung angkanya.",
                    "  2. Jadikan bulan sebagai parameter di bagian YAML:",
                    "      params:",
                    "        bulan: \"2026-09\"",
                    "  3. Di dalam kode, saring data dengan params$bulan, bukan dengan",
                    "     bulan yang diketik langsung.",
                    "  4. Tiap bulan cukup jalankan satu perintah:",
                    "      quarto render laporan.qmd -P bulan:2026-10",
                    "  5. Simpan laporan.qmd di Git. Kalau ada angka yang dipertanyakan,",
                    "     kamu bisa menunjukkan kode yang menghasilkannya.",
                ],
            },
        ],
    },
    {
        "title": "27. Peta Alat Statistik Lain: Julia, MATLAB, SAS, SPSS",
        "sections": [
            {
                "body": [
                    "Selain Python dan R, ada empat nama yang sering kamu temui di",
                    "lowongan kerja, mata kuliah, atau laporan riset. Dua di antaranya",
                    "berbayar mahal, tapi semuanya punya pengganti gratis yang jalan di",
                    "Fedora.",
                    "",
                    "  alat     jenis              lisensi       pengganti gratis",
                    "  Julia    bahasa ilmiah      MIT           (sudah gratis)",
                    "  MATLAB   komputasi numerik  berbayar      GNU Octave",
                    "  SAS      analitik korporat  berbayar      Python, R",
                    "  SPSS     statistik menu     berbayar      PSPP, JASP, jamovi",
                    "",
                    "Materi ini nggak mengajar keempatnya. Tujuannya supaya kamu tahu",
                    "posisi tiap alat, bisa membaca contoh kodenya, dan tahu harus",
                    "pakai apa kalau nggak punya lisensinya.",
                ],
            },
            {
                "heading": "Julia: secepat C, semudah Python",
                "body": [
                    "Julia adalah bahasa untuk komputasi ilmiah yang rilis publik tahun",
                    "2012, dengan versi 1.0 pada 2018. Tujuannya memecahkan masalah dua",
                    "bahasa: ilmuwan menulis prototipe di bahasa yang gampang, lalu",
                    "harus menulis ulang bagian lambatnya di C. Julia dikompilasi",
                    "saat dijalankan (JIT) lewat LLVM, jadi loop biasa pun bisa cepat.",
                    "",
                    "Ciri khasnya multiple dispatch: satu nama fungsi bisa punya",
                    "beberapa versi, dan versi yang dipilih tergantung tipe semua",
                    "argumennya. Indeksnya mulai dari 1, sama dengan R.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "1.13.2, dengan 1.10.12 sebagai versi dukungan jangka panjang (LTS).",
                    "Repositori Fedora 44 membawa versi yang lebih tua (1.12), jadi",
                    "situs resminya menyarankan pemasang juliaup. Survei Stack Overflow",
                    "2024 mencatat 1,1% responden memakai Julia. Ia aktif tapi ceruk:",
                    "kuat di simulasi iklim, optimasi, dan farmakologi.",
                ],
                "bahasa": "julia",
                "code": """nilai = [78, 85, 62, 90, 71]
println(nilai[1])                     # 78, indeks mulai dari 1
println(sum(nilai) / length(nilai))   # 77.2

# multiple dispatch: satu nama, isi beda menurut tipe argumen
luas(r::Real) = pi * r^2
luas(p::Real, l::Real) = p * l
println(luas(2.0))                    # 12.566370614359172
println(luas(3, 4))                   # 12""",
            },
            {
                "heading": "MATLAB dan GNU Octave",
                "body": [
                    "MATLAB dari MathWorks adalah lingkungan komputasi numerik",
                    "berbayar yang kuat di teknik: pengolahan sinyal, sistem kontrol,",
                    "pengolahan citra, dan simulasi dengan Simulink. Banyak kampus",
                    "teknik punya lisensinya, jadi tugas kuliah sering memakainya.",
                    "Versi terbarunya R2026b. Di data science, posisinya terus bergeser",
                    "ke Python dengan NumPy dan SciPy dari bab 03.",
                    "",
                    "Semua di sana adalah matriks, dan operasinya mirip NumPy. GNU",
                    "Octave adalah pengganti gratis yang sintaksnya hampir sama, jadi",
                    "contoh di bawah jalan di keduanya. Di Fedora: sudo dnf install",
                    "octave (versi 10.3 di Fedora 44).",
                ],
                "bahasa": "matlab",
                "code": """% matriks 3x2: tiap baris satu siswa, kolom = nilai UTS dan UAS
nilai = [78 85; 62 70; 90 88];

rata_kolom = mean(nilai)        % 76.667   81.000
akhir = nilai * [0.4; 0.6]      % perkalian matriks: 82.2, 66.8, 88.8
lulus = akhir >= 75             % 1, 0, 1
nilai(2, :)                     % baris kedua, semua kolom: 62 70""",
            },
            {
                "heading": "SAS: analitik di industri teregulasi",
                "body": [
                    "SAS adalah perangkat analitik komersial yang dipakai puluhan",
                    "tahun oleh bank, asuransi, perusahaan farmasi, dan instansi",
                    "pemerintah. Kodenya terdiri dari langkah data (menyiapkan data)",
                    "dan langkah proc (prosedur analisis siap pakai). Platform",
                    "modernnya bernama Viya, dan edisi belajarnya, SAS Viya for",
                    "Learners, gratis bagi pelajar dan pengajar.",
                    "",
                    "Statusnya menurun: banyak tim beralih ke Python dan R karena",
                    "lisensinya mahal. Tapi di industri yang diawasi ketat, misalnya",
                    "skor risiko kredit bank dan laporan uji klinis, perangkat ini",
                    "masih sering diminta di lowongan kerja, jadi ada baiknya bisa",
                    "membaca kodenya.",
                ],
                "bahasa": "sas",
                "code": """data siswa;
  input nama $ kelas $ nilai;
  datalines;
Ani A 78
Budi B 85
Citra A 62
Dodi B 90
;
run;

proc means data=siswa mean std maxdec=2;
  class kelas;
  var nilai;
run;""",
            },
            {
                "heading": "IBM SPSS Statistics",
                "body": [
                    "SPSS adalah perangkat statistik dari IBM yang dipakai lewat menu",
                    "dan kotak dialog, jadi orang bisa menjalankan uji t atau regresi",
                    "tanpa menulis kode. Di Indonesia, SPSS banyak dipakai di skripsi dan",
                    "riset sosial, terutama untuk uji validitas dan reliabilitas",
                    "kuesioner. Lisensinya berbayar, biasanya datang dari kampus atau",
                    "kantor.",
                    "",
                    "Di balik menunya ada bahasa perintah yang disebut sintaks SPSS.",
                    "Menyimpan sintaks membuat analisis bisa diulang persis, tapi",
                    "banyak pengguna nggak pernah membukanya.",
                    "",
                    "Di Fedora, pengganti gratisnya mudah didapat. PSPP adalah",
                    "pengganti dari proyek GNU yang bisa membaca berkas .sav dan",
                    "sintaks SPSS dasar (sudo dnf install pspp). JASP dan jamovi",
                    "punya tampilan menu yang lebih modern, dibangun di atas R, dan",
                    "tersedia lewat Flathub.",
                ],
                "bahasa": "teks",
                "code": """DATA LIST FREE / kelas nilai.
BEGIN DATA
1 78
2 85
1 62
2 90
END DATA.
T-TEST GROUPS=kelas(1 2)
  /VARIABLES=nilai.""",
            },
            {
                "heading": "Pindah ke Python atau R",
                "body": [
                    "Kalau kamu mewarisi pekerjaan dari salah satu alat tadi, padanan",
                    "ini membantu menerjemahkannya:",
                    "",
                    "  dari                         Python                  R",
                    "  T-TEST di SPSS               scipy.stats.ttest_ind   t.test()",
                    "  proc means di SAS            df.groupby().describe() summary()",
                    "  matriks di MATLAB            NumPy                   matrix()",
                    "  regresi di SPSS atau SAS     statsmodels             lm()",
                    "",
                    "Yang perlu dicek saat pindah alat adalah pilihan bawaan tiap",
                    "alat, yang bisa beda. Uji t di SPSS menampilkan dua baris: dengan",
                    "dan tanpa anggapan ragam sama. scipy memakai ragam sama sebagai",
                    "bawaan, sedangkan t.test() di R memakai Welch. Angka yang beda",
                    "sedikit biasanya berasal dari situ, bukan dari salah hitung.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mahasiswa yang menyebar kuesioner skala Likert (pilihan 1 sampai",
                    "5) hampir selalu diminta menguji reliabilitas, biasanya dengan",
                    "Cronbach's alpha. Angka 0,7 ke atas lazim dianggap cukup. Di",
                    "banyak kampus, uji ini dikerjakan dengan SPSS.",
                    "",
                    "Kasus kecil: temanmu minta tolong menghitung Cronbach's alpha",
                    "untuk empat butir pertanyaan dari lima responden, tapi laptopmu",
                    "Fedora dan kamu nggak punya lisensi SPSS.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang pengganti bermenu: sudo dnf install pspp, atau JASP",
                    "     dari Flathub yang punya modul Reliability.",
                    "  2. Untuk mengecek angkanya, hitung juga dengan rumusnya: alpha =",
                    "     k / (k - 1) x (1 - jumlah ragam tiap butir / ragam skor",
                    "     total), dengan k jumlah butir.",
                    "  3. Tulis versi Python murninya:",
                    "      from statistics import variance",
                    "      data = [[4, 5, 4, 4], [3, 3, 4, 3], [5, 5, 5, 4],",
                    "              [2, 3, 2, 3], [4, 4, 5, 4]]",
                    "      k = len(data[0])",
                    "      ragam_butir = [variance([r[i] for r in data]) for i in range(k)]",
                    "      ragam_total = variance([sum(r) for r in data])",
                    "      alpha = k / (k - 1) * (1 - sum(ragam_butir) / ragam_total)",
                    "      print(round(alpha, 3))     # 0.919",
                    "  4. Bandingkan dengan hasil alat bermenu tadi. Kalau sama, angkanya",
                    "     bisa dipakai di skripsi dengan menyebut alat yang dipakai.",
                    "  5. Ingatkan temanmu: lima responden terlalu sedikit untuk",
                    "     kesimpulan yang kuat. Contoh ini cuma untuk mengecek cara",
                    "     hitungnya.",
                ],
            },
        ],
    },
    {
        "title": "28. ETL, ELT, dan Pipeline yang Idempoten",
        "sections": [
            {
                "body": [
                    "Data sebuah toko online lahir di database aplikasinya: tiap",
                    "pesanan, tiap pembayaran, tiap klik. Database itu dirancang untuk",
                    "melayani pembeli dengan cepat. Kalau analis menjalankan query",
                    "berat di sana, misalnya omzet per kota setahun terakhir, aplikasi",
                    "bisa ikut melambat tepat saat pembeli mau bayar.",
                    "",
                    "Jalan keluarnya: data disalin secara rutin ke tempat lain yang",
                    "khusus untuk analisis, lalu dirapikan di sana. Rangkaian langkah",
                    "otomatis yang memindahkan dan mengolah data itu disebut pipeline",
                    "data. Orang yang membangun dan merawatnya disebut data engineer.",
                    "Di roadmap.sh, peran ini punya jalur belajar sendiri yang dimulai",
                    "dari SQL, Python, dan konsep di bab ini.",
                ],
            },
            {
                "heading": "ETL dan ELT",
                "body": [
                    "Hampir semua pipeline punya tiga tahap:",
                    "",
                    "  - Extract: ambil data dari sumbernya, misalnya database",
                    "    aplikasi, API, atau berkas CSV kiriman mitra.",
                    "  - Transform: bersihkan dan ubah bentuknya. Buang duplikat,",
                    "    samakan format tanggal, gabungkan tabel, hitung kolom baru.",
                    "  - Load: muat hasilnya ke tempat tujuan.",
                    "",
                    "Urutan klasiknya ETL: data ditransformasi di server tersendiri,",
                    "baru hasil bersihnya dimuat ke gudang data. Dulu penyimpanan dan",
                    "komputasi gudang data mahal, jadi yang masuk harus sudah rapi.",
                    "",
                    "Sekarang yang lebih umum ELT: data mentah dimuat dulu apa adanya",
                    "ke gudang data cloud, lalu ditransformasi di dalamnya dengan SQL.",
                    "Penyimpanan cloud murah dan mesin query-nya kuat, jadi menyimpan",
                    "data mentah jadi masuk akal. Bonusnya, kalau ada aturan",
                    "transformasi yang salah, data mentahnya masih ada dan bisa diolah",
                    "ulang. Alat transformasi ELT yang paling banyak dipakai, dbt,",
                    "dibahas di bab berikutnya.",
                    "",
                    "ETL belum hilang. Ia tetap dipakai kalau data harus diubah",
                    "sebelum mendarat, misalnya kolom data pribadi yang wajib",
                    "disamarkan sebelum boleh disimpan di gudang data.",
                ],
            },
            {
                "heading": "Batch dan streaming",
                "body": [
                    "Pipeline batch jalan per jadwal dan memproses sekumpulan data",
                    "sekaligus, misalnya tiap jam 1 malam untuk semua pesanan kemarin.",
                    "Pipeline streaming memproses tiap kejadian begitu ia muncul, dalam",
                    "hitungan detik. Di antaranya ada micro-batch: kumpulan kecil tiap",
                    "beberapa detik atau menit.",
                    "",
                    "Streaming terdengar lebih canggih, tapi lebih rumit dibangun dan",
                    "dirawat. Laporan omzet harian cukup batch. Deteksi transaksi",
                    "kartu yang mencurigakan butuh streaming, karena keputusannya harus",
                    "keluar sebelum transaksi selesai. Kebanyakan perusahaan mulai",
                    "dari batch, lalu menambah streaming cuma untuk kebutuhan yang",
                    "memang menuntut detik. Alat streaming seperti Kafka dibahas di bab",
                    "Big Data dan Streaming.",
                    "",
                    "Ada juga teknik change data capture (CDC): pipeline membaca catatan",
                    "perubahan database (log transaksinya) dan cuma menyalin baris yang",
                    "berubah, bukan seluruh tabel tiap kali. Debezium adalah alat open",
                    "source yang populer untuk ini.",
                ],
            },
            {
                "heading": "Kenapa pipeline harus idempoten",
                "code": """import sqlite3

# pesanan dari aplikasi untuk tanggal 2026-10-18 (hasil extract)
PESANAN = [
    ("P001", "2026-10-18", 125000),
    ("P002", "2026-10-18", 80000),
    ("P003", "2026-10-18", 47500),
]

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE fakta_pesanan (id TEXT, tanggal TEXT, total INTEGER)")


def muat_naif(tanggal):
    db.executemany("INSERT INTO fakta_pesanan VALUES (?, ?, ?)",
                   [p for p in PESANAN if p[1] == tanggal])


def muat_idempoten(tanggal):
    with db:  # satu transaksi: dua langkah sukses bersama atau batal bersama
        db.execute("DELETE FROM fakta_pesanan WHERE tanggal = ?", (tanggal,))
        db.executemany("INSERT INTO fakta_pesanan VALUES (?, ?, ?)",
                       [p for p in PESANAN if p[1] == tanggal])


def omzet():
    return db.execute("SELECT COUNT(*), SUM(total) FROM fakta_pesanan").fetchone()


muat_naif("2026-10-18")
muat_naif("2026-10-18")          # job dijalankan ulang sesudah gagal
print("naif, dua kali      :", omzet())

db.execute("DELETE FROM fakta_pesanan")
muat_idempoten("2026-10-18")
muat_idempoten("2026-10-18")
print("idempoten, dua kali :", omzet())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  naif, dua kali      : (6, 505000)",
                    "  idempoten, dua kali : (3, 252500)",
                    "",
                    "Pipeline yang idempoten memberi hasil yang sama walau dijalankan",
                    "sekali, dua kali, atau sepuluh kali dengan masukan yang sama. Ini",
                    "bukan kemewahan. Pipeline pasti pernah gagal di tengah jalan:",
                    "server mati, koneksi putus, disk penuh. Reaksi pertama siapa pun",
                    "adalah menjalankannya ulang.",
                    "",
                    "Versi naif cuma menambah baris. Dijalankan ulang, pesanan kemarin",
                    "masuk dua kali dan omzetnya dobel, dari 252.500 jadi 505.000.",
                    "Nggak ada error, laporannya tetap keluar, cuma angkanya salah.",
                    "Versi idempoten menghapus dulu data untuk tanggal itu, lalu",
                    "mengisinya lagi. Karena dua langkah itu dibungkus satu transaksi",
                    "(with db), nggak ada keadaan setengah jadi: kalau INSERT gagal,",
                    "DELETE-nya ikut dibatalkan.",
                ],
            },
            {
                "heading": "Tiga cara membuat muatan idempoten",
                "body": [
                    "  1. Hapus lalu isi ulang per partisi, seperti contoh di atas.",
                    "     Partisi biasanya per tanggal: menjalankan ulang job tanggal",
                    "     18 cuma mengganti data tanggal 18.",
                    "  2. Upsert, yaitu insert yang berubah jadi update kalau kuncinya",
                    "     sudah ada. Di SQLite dan PostgreSQL bentuknya INSERT ... ON",
                    "     CONFLICT DO UPDATE, di banyak gudang data bentuknya MERGE.",
                    "     Cocok untuk tabel yang barisnya punya id tetap, misalnya",
                    "     daftar produk.",
                    "  3. Tulis ke tabel sementara (staging), periksa, lalu tukar dengan",
                    "     tabel aslinya sekaligus. Pembaca laporan nggak pernah melihat",
                    "     tabel yang setengah terisi.",
                    "",
                    "Satu syarat lagi: transformasinya sendiri harus deterministik.",
                    "Kalau job menulis \"data kemarin\" dengan menghitung tanggal dari",
                    "jam komputer, menjalankan ulang job hari Senin pada hari Rabu",
                    "akan memproses tanggal yang salah. Tanggal yang diproses harus",
                    "jadi parameter job. Orkestrator seperti Airflow menyebutnya",
                    "logical date, dan ini muncul lagi di bab berikutnya.",
                    "",
                    "Jebakan: memanggil datetime.now() di dalam transformasi. Hasilnya",
                    "berubah tiap kali job jalan, jadi menjalankan ulang job lama nggak",
                    "pernah memberi hasil yang sama.",
                ],
            },
            {
                "heading": "Pipeline yang bisa dipercaya",
                "body": [
                    "Selain idempoten, pipeline produksi biasanya punya:",
                    "",
                    "  - Log yang mencatat berapa baris dibaca, dibuang, dan dimuat.",
                    "  - Rekonsiliasi: jumlah baris atau total di tujuan dibandingkan",
                    "    dengan sumbernya. Selisih berarti ada yang hilang di jalan.",
                    "  - Retry otomatis dengan jeda yang makin panjang, karena banyak",
                    "    kegagalan cuma gangguan sesaat.",
                    "  - Peringatan ke tim kalau job gagal atau datanya aneh.",
                    "  - Cara menangani data terlambat: pesanan tanggal 18 yang baru",
                    "    tercatat tanggal 19 harus tetap masuk ke partisi tanggal 18.",
                    "  - Backfill, yaitu kemampuan memproses ulang rentang tanggal lama,",
                    "    misalnya sesudah aturan transformasi diperbaiki.",
                    "",
                    "Semua itu jauh lebih gampang kalau pipeline-nya idempoten:",
                    "backfill cuma berarti menjalankan job yang sama untuk tanggal",
                    "lama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online, aplikasi fintech, dan layanan logistik hampir selalu",
                    "punya job malam yang menyalin data transaksi hari sebelumnya ke",
                    "gudang data seperti BigQuery atau Snowflake. Dasbor manajemen",
                    "pagi harinya dibangun dari tabel hasil job itu.",
                    "",
                    "Kasus kecil: job jam 01.00 gagal di tengah karena koneksi putus.",
                    "Pagi harinya seorang engineer menjalankannya ulang, dan dasbor",
                    "menunjukkan omzet kemarin dua kali lipat dari biasanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek jumlah baris per tanggal di tabel tujuan. Kalau tanggal",
                    "     kemarin punya baris dua kali lipat, job-nya cuma menambah.",
                    "      SELECT tanggal, COUNT(*) FROM fakta_pesanan",
                    "      GROUP BY tanggal ORDER BY tanggal DESC LIMIT 3;",
                    "  2. Ubah langkah muat jadi hapus lalu isi ulang untuk tanggal",
                    "     yang diproses, dibungkus satu transaksi.",
                    "  3. Jadikan tanggal sebagai parameter job, jangan dihitung dari",
                    "     jam komputer di dalam kode.",
                    "  4. Jalankan ulang job untuk tanggal kemarin. Sekarang aman,",
                    "     karena job idempoten selalu menghasilkan jumlah baris yang",
                    "     sama.",
                    "  5. Tambahkan rekonsiliasi: bandingkan jumlah pesanan di database",
                    "     aplikasi dengan di gudang data, dan kirim peringatan kalau",
                    "     selisihnya lebih dari nol.",
                ],
            },
        ],
    },
    {
        "title": "29. Warehouse, Data Lake, dan Lakehouse",
        "sections": [
            {
                "body": [
                    "Sesudah data disalin, pertanyaan berikutnya adalah tempat",
                    "menyimpannya, dan itu tergantung jenis pekerjaannya. Database aplikasi dan",
                    "database analisis dirancang untuk dua pekerjaan yang berlawanan:",
                    "",
                    "                 OLTP (aplikasi)           OLAP (analisis)",
                    "  pekerjaan      banyak transaksi kecil    sedikit query besar",
                    "  contoh         simpan satu pesanan       omzet per kota setahun",
                    "  baris disentuh beberapa per query        jutaan per query",
                    "  penyimpanan    biasanya per baris        biasanya per kolom",
                    "  contoh produk  PostgreSQL, MySQL         BigQuery, Snowflake",
                    "",
                    "OLTP (online transaction processing) melayani aplikasi, OLAP",
                    "(online analytical processing) melayani analisis. Kenapa",
                    "penyimpanan per kolom cocok untuk OLAP sudah dibahas di bab Data",
                    "Kolumnar di Satu Mesin. Materi ini membahas tiga bentuk tempat",
                    "penyimpanan untuk OLAP.",
                ],
            },
            {
                "heading": "Data warehouse",
                "body": [
                    "Data warehouse, atau gudang data, menyimpan data dalam tabel yang",
                    "rapi dan bisa di-query dengan SQL. Skemanya ditentukan sebelum",
                    "data ditulis (schema-on-write): kolom, tipe, dan aturannya sudah",
                    "pasti, jadi data yang melanggar ditolak di pintu. Gudang data",
                    "modern menyimpan per kolom dan membagi query ke banyak mesin",
                    "sekaligus.",
                    "",
                    "Contohnya Snowflake, Google BigQuery, Amazon Redshift, dan",
                    "warehouse di Microsoft Fabric. Perusahaan lama sering masih",
                    "memakai sistem di server sendiri seperti Teradata atau Oracle.",
                    "",
                    "Dua nama sering muncul dalam sejarahnya. Bill Inmon merancang",
                    "gudang data sebagai satu sumber kebenaran terpusat yang dibangun",
                    "dari atas. Ralph Kimball membangunnya dari bawah lewat pemodelan",
                    "dimensional, yang dibahas di materi berikutnya. Bagian kecil",
                    "gudang data untuk satu departemen, misalnya khusus keuangan,",
                    "disebut data mart.",
                ],
            },
            {
                "heading": "Data lake",
                "body": [
                    "Data lake menyimpan berkas mentah apa adanya di object storage",
                    "yang murah: Amazon S3, Google Cloud Storage, atau Azure Data Lake",
                    "Storage. Isinya boleh apa saja: CSV, JSON, Parquet, log, gambar,",
                    "rekaman suara. Skemanya baru ditentukan saat data dibaca",
                    "(schema-on-read).",
                    "",
                    "Kelebihannya fleksibel dan murah, dan cocok untuk data yang",
                    "belum jelas mau dipakai untuk apa, termasuk bahan machine",
                    "learning. Kekurangannya: tanpa aturan dan catatan isi, lama-lama",
                    "nggak ada yang tahu berkas mana yang benar, mana yang usang, dan",
                    "kolom mana artinya apa. Keadaan ini dijuluki data swamp, rawa",
                    "data.",
                ],
            },
            {
                "heading": "Mencoba dua pendekatan",
                "code": "import csv\nimport io\nimport json\nimport sqlite3\n\n# \"data lake\": berkas mentah apa adanya, skema ditentukan saat dibaca\nLAKE = {\n    \"klik/2026-10-18.json\": '[{\"user\": \"u1\", \"halaman\": \"/promo\"}, '\n                            '{\"user\": \"u2\", \"halaman\": \"/keranjang\", \"durasi\": 31}]',\n    \"pesanan/2026-10-18.csv\": \"id,total\\nP001,125000\\nP002,delapan puluh ribu\\nP003,-5000\\n\",\n}\n\nklik = json.loads(LAKE[\"klik/2026-10-18.json\"])\nprint(\"klik:\", len(klik), \"baris, kolom:\", sorted({k for b in klik for k in b}))\n\n# \"warehouse\": skema ditentukan saat ditulis, yang melanggar ditolak\ngudang = sqlite3.connect(\":memory:\")\ngudang.execute(\"\"\"\n    CREATE TABLE pesanan (\n        id    TEXT PRIMARY KEY,\n        total INTEGER NOT NULL CHECK (total >= 0)\n    ) STRICT\"\"\")\n\nfor baris in csv.DictReader(io.StringIO(LAKE[\"pesanan/2026-10-18.csv\"])):\n    try:\n        with gudang:\n            gudang.execute(\"INSERT INTO pesanan VALUES (?, ?)\",\n                           (baris[\"id\"], baris[\"total\"]))\n        print(\"masuk  :\", baris[\"id\"])\n    except sqlite3.IntegrityError as e:\n        print(\"ditolak:\", baris[\"id\"], \"->\", e)\n\nprint(\"isi gudang:\", gudang.execute(\"SELECT * FROM pesanan\").fetchall())",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  klik: 2 baris, kolom: ['durasi', 'halaman', 'user']",
                    "  masuk  : P001",
                    "  ditolak: P002 -> cannot store TEXT value in INTEGER column pesanan.total",
                    "  ditolak: P003 -> CHECK constraint failed: total >= 0",
                    "  isi gudang: [('P001', 125000)]",
                    "",
                    "Berkas JSON di \"lake\" diterima apa adanya, termasuk baris kedua",
                    "yang punya kolom durasi sementara baris pertama nggak. Siapa pun",
                    "yang membacanya nanti yang harus memutuskan arti kolom yang",
                    "kadang ada kadang nggak.",
                    "",
                    "Tabel di \"gudang\" punya skema ketat. STRICT membuat SQLite",
                    "menolak teks di kolom INTEGER, dan CHECK menolak total negatif.",
                    "Teks \"125000\" tetap masuk karena bisa diubah ke angka tanpa",
                    "kehilangan apa pun. Data kotor ketahuan saat ditulis, bukan",
                    "berbulan-bulan kemudian di laporan.",
                ],
            },
            {
                "heading": "Lakehouse",
                "body": [
                    "Lakehouse mencoba menggabungkan dua dunia: berkas tetap disimpan",
                    "murah di object storage dalam format terbuka (biasanya Parquet),",
                    "tapi di atasnya ada lapisan metadata yang memberi fitur gudang",
                    "data. Fiturnya antara lain transaksi ACID, skema yang dijaga, dan",
                    "kemampuan melihat isi tabel di masa lalu. Lapisan itu disediakan",
                    "format tabel terbuka seperti Apache Iceberg, Delta Lake, dan",
                    "Apache Hudi, yang dibahas di bab Lakehouse dan Platform Data",
                    "Cloud. Istilah lakehouse dipopulerkan Databricks sekitar 2020.",
                    "",
                    "Keuntungan terbesarnya: satu salinan data bisa dibaca banyak",
                    "mesin. Spark, Trino, DuckDB, dan Snowflake bisa membaca tabel",
                    "Iceberg yang sama, jadi perusahaan nggak terkunci di satu vendor.",
                    "",
                    "Data di lakehouse sering ditata berlapis, yang dijuluki arsitektur",
                    "medallion:",
                    "",
                    "  - bronze: data mentah persis seperti dari sumber;",
                    "  - silver: sudah dibersihkan, diberi tipe, duplikat dibuang;",
                    "  - gold: tabel siap pakai untuk laporan dan dasbor.",
                ],
            },
            {
                "heading": "Data mesh dan data fabric",
                "body": [
                    "Dua istilah ini sering muncul di presentasi dan lowongan kerja.",
                    "Data mesh, diperkenalkan Zhamak Dehghani pada 2019, adalah cara",
                    "mengatur organisasi, bukan produk yang bisa dibeli. Tiap domain",
                    "bisnis (penjualan, logistik, pemasaran) memiliki dan merawat",
                    "datanya sendiri sebagai produk untuk tim lain, dengan platform",
                    "bersama dan aturan tata kelola yang disepakati. Tujuannya",
                    "mengurangi antrean di satu tim data pusat yang kewalahan.",
                    "",
                    "Data fabric lebih condong ke teknologi: lapisan integrasi yang",
                    "menghubungkan banyak sumber data lewat metadata, sehingga data",
                    "bisa ditemukan dan dipakai tanpa harus dipindah semua ke satu",
                    "tempat. Istilah ini banyak dipakai vendor, jadi artinya agak",
                    "beragam tergantung siapa yang bicara.",
                ],
            },
            {
                "heading": "Memilih tempat penyimpanan",
                "body": [
                    "  - Perusahaan kecil dengan data beberapa GB: replika baca dari",
                    "    database aplikasi, atau DuckDB atas berkas Parquet, sering",
                    "    sudah cukup.",
                    "  - Data mulai besar dan banyak tim butuh laporan SQL: gudang data",
                    "    cloud seperti BigQuery atau Snowflake.",
                    "  - Banyak data setengah terstruktur, kebutuhan machine learning,",
                    "    dan keinginan nggak terkunci vendor: lakehouse dengan format",
                    "    tabel terbuka.",
                    "",
                    "Pilihan ini jarang mutlak. Banyak perusahaan menyimpan data mentah",
                    "di lake, lalu memuat hasil olahannya ke gudang data untuk analis.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Startup yang tumbuh hampir selalu melewati urutan yang mirip.",
                    "Laporan awalnya di-query langsung dari database aplikasi, lalu",
                    "pindah ke replika baca, lalu ke gudang data cloud. Kadang",
                    "akhirnya ke lakehouse saat data dan timnya makin besar.",
                    "",
                    "Kasus kecil: startup dengan satu database PostgreSQL mengeluh",
                    "aplikasinya lambat tiap Senin pagi. Ternyata tim keuangan",
                    "menjalankan query laporan mingguan yang berat di database yang",
                    "sama.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan penyebabnya dengan melihat query yang sedang jalan",
                    "     di jam lambat, misalnya lewat pg_stat_activity di PostgreSQL.",
                    "  2. Langkah tercepat: arahkan query laporan ke replika baca, yaitu",
                    "     salinan database yang selalu ikut diperbarui. Aplikasi utama",
                    "     nggak lagi terbebani.",
                    "  3. Kalau laporan makin banyak dan makin berat, siapkan pipeline",
                    "     ELT harian ke gudang data cloud.",
                    "  4. Simpan juga salinan mentahnya sebagai Parquet di object",
                    "     storage, supaya bisa diolah ulang kalau aturan laporan",
                    "     berubah.",
                    "  5. Tulis aturan sederhana: dasbor dan analis membaca dari gudang",
                    "     data, bukan dari database aplikasi.",
                ],
            },
        ],
    },
    {
        "title": "30. Pemodelan Dimensional: Star Schema dan SCD",
        "sections": [
            {
                "body": [
                    "Database aplikasi biasanya dinormalisasi: data dipecah ke banyak",
                    "tabel kecil supaya nggak ada yang ditulis dua kali. Bagus untuk",
                    "menyimpan, tapi query laporan jadi butuh JOIN ke delapan tabel,",
                    "dan analis gampang salah.",
                    "",
                    "Pemodelan dimensional, yang dipopulerkan Ralph Kimball lewat buku",
                    "The Data Warehouse Toolkit, menata ulang data analitik jadi dua",
                    "jenis tabel:",
                    "",
                    "  - Tabel fakta: satu baris untuk satu kejadian bisnis, berisi",
                    "    angka yang mau dijumlahkan (jumlah, omzet) dan kunci ke tabel",
                    "    dimensi.",
                    "  - Tabel dimensi: konteks kejadian itu, yaitu siapa, apa, di",
                    "    mana, dan kapan. Isinya kolom deskriptif seperti nama produk,",
                    "    kategori, kota, atau nama hari.",
                    "",
                    "Tabel fakta di tengah, dimensi mengelilinginya. Kalau digambar,",
                    "bentuknya seperti bintang, makanya disebut star schema.",
                ],
            },
            {
                "heading": "Fakta, dimensi, dan grain",
                "body": [
                    "Langkah merancangnya menurut Kimball ada empat: pilih proses",
                    "bisnisnya (misalnya penjualan), tentukan grain, tentukan",
                    "dimensinya, lalu tentukan faktanya.",
                    "",
                    "Grain adalah arti satu baris di tabel fakta, dan ini keputusan",
                    "paling penting. \"Satu baris = satu produk dalam satu struk\"",
                    "beda jauh dengan \"satu baris = total satu struk\". Yang pertama",
                    "bisa menjawab produk apa yang laku, yang kedua nggak. Pilih grain",
                    "serinci mungkin, karena ringkasan selalu bisa dibuat dari data",
                    "rinci, tapi nggak sebaliknya.",
                    "",
                    "Angka di tabel fakta punya tiga sifat:",
                    "",
                    "  - Aditif: boleh dijumlahkan ke arah mana pun, misalnya omzet.",
                    "  - Semi-aditif: boleh dijumlahkan antarproduk, tapi nggak",
                    "    antarwaktu, misalnya saldo rekening atau stok gudang.",
                    "  - Non-aditif: nggak boleh dijumlahkan, misalnya persen diskon.",
                    "    Hitung ulang dari komponennya.",
                    "",
                    "Tabel dimensi biasanya memakai surrogate key, yaitu nomor buatan",
                    "gudang data sendiri, bukan id dari aplikasi. Alasannya kelihatan",
                    "nanti di bagian SCD. Hampir semua model juga punya dimensi",
                    "tanggal: satu baris per hari, lengkap dengan bulan, nama hari, dan",
                    "penanda hari libur, supaya laporan nggak perlu menghitung ulang",
                    "dari teks tanggal.",
                ],
            },
            {
                "heading": "Star schema di SQLite",
                "bahasa": "sql",
                "code": """CREATE TABLE dim_produk (
  produk_key INTEGER PRIMARY KEY,
  nama TEXT, kategori TEXT
);
CREATE TABLE dim_tanggal (
  tanggal_key INTEGER PRIMARY KEY,   -- 20260901 = 1 September 2026
  tanggal TEXT, bulan TEXT, hari TEXT
);
CREATE TABLE fakta_penjualan (
  tanggal_key INTEGER REFERENCES dim_tanggal,
  produk_key INTEGER REFERENCES dim_produk,
  jumlah INTEGER, omzet INTEGER
);

INSERT INTO dim_produk VALUES
  (1, 'Kopi Susu', 'Minuman'), (2, 'Teh Tarik', 'Minuman'),
  (3, 'Roti Bakar', 'Makanan');
INSERT INTO dim_tanggal VALUES
  (20260901, '2026-09-01', '2026-09', 'Selasa'),
  (20260902, '2026-09-02', '2026-09', 'Rabu'),
  (20261001, '2026-10-01', '2026-10', 'Kamis');
INSERT INTO fakta_penjualan VALUES
  (20260901, 1, 3, 54000), (20260901, 3, 2, 30000),
  (20260902, 2, 4, 48000), (20260902, 1, 1, 18000),
  (20261001, 1, 5, 90000), (20261001, 3, 1, 15000);

SELECT t.bulan, p.kategori, SUM(f.jumlah) AS jumlah, SUM(f.omzet) AS omzet
FROM fakta_penjualan f
JOIN dim_tanggal t ON t.tanggal_key = f.tanggal_key
JOIN dim_produk  p ON p.produk_key  = f.produk_key
GROUP BY t.bulan, p.kategori
ORDER BY t.bulan, omzet DESC;""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  2026-09|Minuman|8|120000",
                    "  2026-09|Makanan|2|30000",
                    "  2026-10|Minuman|5|90000",
                    "  2026-10|Makanan|1|15000",
                    "",
                    "Grain tabel fakta ini satu produk per hari. Query laporannya",
                    "selalu berpola sama: tabel fakta di FROM, JOIN ke dimensi yang",
                    "dibutuhkan, saring dan kelompokkan menurut kolom dimensi, lalu",
                    "jumlahkan kolom fakta. Pola yang seragam ini yang membuat star",
                    "schema disukai analis dan alat BI. Power BI, misalnya, dalam",
                    "dokumentasinya menyarankan model berbentuk star schema.",
                ],
            },
            {
                "heading": "Star atau snowflake",
                "body": [
                    "Kalau tabel dimensi dinormalisasi lagi, misalnya kategori",
                    "dipindah ke tabel dim_kategori tersendiri, bentuknya bercabang",
                    "seperti kepingan salju dan disebut snowflake schema. Hemat sedikit",
                    "ruang, tapi tiap query butuh JOIN tambahan. Di gudang data modern",
                    "yang penyimpanannya murah, star schema biasanya lebih dipilih.",
                    "",
                    "Jebakan: snowflake schema adalah pola tabel, sedangkan Snowflake",
                    "adalah nama produk gudang data cloud. Keduanya nggak berhubungan.",
                    "Model di Snowflake justru biasanya berbentuk star schema.",
                ],
            },
            {
                "heading": "Dimensi yang berubah pelan (SCD)",
                "body": [
                    "Pelanggan pindah kota, produk ganti kategori, salesman pindah",
                    "wilayah. Dimensi seperti ini berubah pelan dan jarang, jadi",
                    "disebut slowly changing dimension (SCD). Pertanyaannya: penjualan",
                    "lama dihitung untuk kota lama atau kota baru? Ada beberapa tipe",
                    "jawaban:",
                    "",
                    "  - Tipe 0: nilai awal nggak pernah diubah, misalnya tanggal",
                    "    daftar.",
                    "  - Tipe 1: timpa nilai lama. Sederhana, tapi sejarahnya hilang:",
                    "    semua penjualan lama ikut pindah ke kota baru.",
                    "  - Tipe 2: tambah baris baru untuk versi baru, dan tutup baris",
                    "    lama dengan tanggal berlaku. Sejarahnya utuh.",
                    "  - Tipe 3: simpan nilai sebelumnya di kolom tersendiri, misalnya",
                    "    kota_sebelumnya. Cuma ingat satu perubahan.",
                    "",
                    "Tipe 2 yang paling sering dipakai untuk atribut yang penting di",
                    "laporan. Di sinilah surrogate key berguna: satu pelanggan bisa",
                    "punya beberapa baris versi, masing-masing dengan key sendiri.",
                ],
            },
            {
                "heading": "SCD tipe 2 di SQLite",
                "bahasa": "sql",
                "code": """CREATE TABLE dim_pelanggan (
  pelanggan_key  INTEGER PRIMARY KEY,   -- surrogate key, unik per versi
  pelanggan_id   TEXT,                  -- id asli dari aplikasi
  nama TEXT, kota TEXT,
  berlaku_dari   TEXT,
  berlaku_sampai TEXT,                  -- '9999-12-31' = masih berlaku
  aktif INTEGER
);
CREATE TABLE fakta_order (tanggal TEXT, pelanggan_key INTEGER, omzet INTEGER);

INSERT INTO dim_pelanggan VALUES
  (1, 'C07', 'Rina', 'Bandung', '2025-01-10', '9999-12-31', 1);
INSERT INTO fakta_order VALUES ('2026-05-03', 1, 200000), ('2026-06-20', 1, 150000);

-- 1 Juli 2026 Rina pindah ke Surabaya: tutup versi lama, tambah versi baru
UPDATE dim_pelanggan
   SET berlaku_sampai = '2026-06-30', aktif = 0
 WHERE pelanggan_id = 'C07' AND aktif = 1;
INSERT INTO dim_pelanggan VALUES
  (2, 'C07', 'Rina', 'Surabaya', '2026-07-01', '9999-12-31', 1);
INSERT INTO fakta_order VALUES ('2026-08-11', 2, 300000);

SELECT d.kota, SUM(f.omzet) AS omzet
FROM fakta_order f
JOIN dim_pelanggan d ON d.pelanggan_key = f.pelanggan_key
GROUP BY d.kota
ORDER BY d.kota;""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Bandung|350000",
                    "  Surabaya|300000",
                    "",
                    "Dua order Rina sebelum pindah tetap tercatat untuk Bandung, dan",
                    "order sesudahnya untuk Surabaya. Kuncinya ada di tabel fakta: tiap",
                    "order menyimpan pelanggan_key versi yang berlaku saat order itu",
                    "terjadi. Pipeline yang memuat fakta harus mencari versi itu, yaitu",
                    "baris dengan pelanggan_id yang cocok dan tanggal order di antara",
                    "berlaku_dari dan berlaku_sampai.",
                    "",
                    "Kalau yang dibutuhkan cuma keadaan sekarang, misalnya daftar kota",
                    "pelanggan hari ini, saring dengan aktif = 1. Kalau dimensi ini",
                    "memakai tipe 1, omzet Bandung bakal hilang semua dan Surabaya",
                    "tampak punya 650.000, padahal Rina baru di sana sejak Juli.",
                    "",
                    "Ingat: tabel dimensi sengaja nggak dinormalisasi. Kolom kategori",
                    "yang ditulis berulang di tiap produk itu disengaja, demi query",
                    "yang sederhana. Sebagian tim modern bahkan menggabungkan fakta dan",
                    "dimensi jadi satu tabel lebar (one big table), karena gudang data",
                    "kolumnar membuat kolom berulang murah. Tapi untuk model di alat BI,",
                    "star schema tetap jadi bentuk standar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan penjualan ritel, model semantik di Power BI, dan tabel",
                    "mart di gudang data perusahaan hampir selalu berbentuk fakta dan",
                    "dimensi. Masalah SCD muncul di mana pun ada orang atau barang yang",
                    "berpindah kelompok: salesman pindah cabang, toko pindah wilayah,",
                    "produk pindah kategori.",
                    "",
                    "Kasus kecil: manajer penjualan minta omzet per wilayah per bulan",
                    "selama setahun. Masalahnya, tiga salesman pindah wilayah di",
                    "tengah tahun, dan ia mau omzet mereka tetap tercatat di wilayah",
                    "tempat mereka bekerja saat itu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan grain tabel fakta: satu baris per transaksi.",
                    "  2. Rancang dim_salesman sebagai SCD tipe 2 dengan kolom",
                    "     salesman_key, salesman_id, wilayah, berlaku_dari,",
                    "     berlaku_sampai, dan aktif.",
                    "  3. Tiap ada perpindahan, tutup baris lama (isi berlaku_sampai,",
                    "     aktif = 0), lalu tambah baris baru dengan wilayah baru.",
                    "  4. Saat memuat fakta, cari salesman_key yang berlaku pada tanggal",
                    "     transaksi:",
                    "      SELECT salesman_key FROM dim_salesman",
                    "      WHERE salesman_id = ? AND ? BETWEEN berlaku_dari",
                    "                                    AND berlaku_sampai;",
                    "  5. Laporannya tinggal JOIN fakta ke dim_salesman dan dim_tanggal,",
                    "     lalu GROUP BY wilayah dan bulan.",
                ],
            },
        ],
    },
    {
        "title": "31. Kualitas Data, Lineage, dan Data Pribadi",
        "sections": [
            {
                "body": [
                    "Pipeline yang jalan mulus belum tentu menghasilkan angka yang",
                    "benar. Baris duplikat membuat omzet dobel. Kolom email yang",
                    "kosong membuat kampanye pemasaran nggak sampai. Jumlah barang",
                    "negatif karena salah input membuat stok aneh. Zona waktu yang",
                    "keliru menggeser transaksi tengah malam ke hari yang salah.",
                    "",
                    "Kualitas data biasanya dinilai dari beberapa sisi:",
                    "",
                    "  - Kelengkapan: kolom wajib nggak boleh kosong.",
                    "  - Keunikan: satu pesanan cuma muncul sekali.",
                    "  - Validitas: nilainya masuk akal, misalnya umur 0 sampai 120",
                    "    dan email punya format yang benar.",
                    "  - Konsistensi: kode kota di tabel pesanan ada di tabel kota.",
                    "  - Ketepatan waktu: data kemarin sudah masuk pagi ini.",
                    "",
                    "Uji kualitas data adalah pemeriksaan otomatis untuk sisi-sisi itu,",
                    "mirip tes untuk kode, tapi yang diuji isi datanya.",
                ],
            },
            {
                "heading": "Memvalidasi lalu mengarantina",
                "code": """MASUK = [
    {"id": "P001", "tanggal": "2026-10-18", "jumlah": 2, "harga": 25000},
    {"id": "P002", "tanggal": "2026-10-18", "jumlah": -1, "harga": 25000},
    {"id": "P003", "tanggal": "", "jumlah": 1, "harga": 15000},
    {"id": "P004", "tanggal": "2026-10-18", "jumlah": 3, "harga": 12000},
    {"id": "P005", "tanggal": "2026-10-18", "jumlah": 1, "harga": None},
]

ATURAN = {
    "tanggal wajib ada": lambda b: bool(b["tanggal"]),
    "jumlah harus positif": lambda b: b["jumlah"] > 0,
    "harga wajib ada": lambda b: b["harga"] is not None,
}

lulus, karantina = [], []
for baris in MASUK:
    gagal = [nama for nama, cek in ATURAN.items() if not cek(baris)]
    if gagal:
        karantina.append((baris["id"], gagal))
    else:
        lulus.append(baris)

print("lulus    :", [b["id"] for b in lulus])
for id_, alasan in karantina:
    print("karantina:", id_, alasan)

# cek tingkat tabel: jumlah baris hari ini dibanding biasanya
rata_minggu_lalu = 5
if len(lulus) < 0.5 * rata_minggu_lalu:
    print(f"peringatan: cuma {len(lulus)} baris lulus, biasanya sekitar {rata_minggu_lalu}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  lulus    : ['P001', 'P004']",
                    "  karantina: P002 ['jumlah harus positif']",
                    "  karantina: P003 ['tanggal wajib ada']",
                    "  karantina: P005 ['harga wajib ada']",
                    "  peringatan: cuma 2 baris lulus, biasanya sekitar 5",
                    "",
                    "Ada dua jenis pemeriksaan di sini. Pemeriksaan tingkat baris",
                    "menilai tiap baris sendiri-sendiri. Baris yang gagal nggak",
                    "dibuang, tapi dipindah ke karantina beserta alasannya, supaya bisa",
                    "diperiksa, diperbaiki di sumbernya, lalu dimuat ulang.",
                    "",
                    "Pemeriksaan tingkat tabel menilai datanya sebagai satu kesatuan:",
                    "jumlah baris yang tiba-tiba anjlok, total yang melonjak sepuluh",
                    "kali, atau data yang belum diperbarui sejak kemarin. Masalah",
                    "seperti ini nggak kelihatan kalau baris diperiksa satu per satu.",
                    "",
                    "Pasang uji di dua tempat: saat data masuk, supaya data rusak",
                    "tertahan sebelum menyebar, dan sesudah transformasi, supaya",
                    "kesalahan logika ketahuan sebelum sampai ke laporan.",
                ],
            },
            {
                "heading": "Great Expectations dan kawan-kawan",
                "body": [
                    "Great Expectations (GX) adalah pustaka Python untuk uji kualitas",
                    "data. Kamu menulis ekspektasi, misalnya kolom ini nggak boleh",
                    "kosong atau nilainya harus di antara 1 dan 100, lalu GX",
                    "memvalidasi data dan membuat laporannya. Versi stabil terbaru saat",
                    "materi ini ditulis (Oktober 2026) adalah 1.24.0, berlisensi Apache",
                    "2.0.",
                    "",
                    "Jebakan: GX 1.x (sejak 2024) berubah besar dari 0.x. Tutorial yang",
                    "memakai ge.from_pandas() atau konfigurasi DataContext lama nggak",
                    "berlaku lagi. Contoh di bawah memakai API 1.x.",
                    "",
                    "Alat lain yang sering kamu temui: uji bawaan dbt (not_null,",
                    "unique) yang dibahas di bab berikutnya, Soda Core, pandera untuk",
                    "memvalidasi skema DataFrame, dan Deequ atau PyDeequ untuk Spark.",
                    "Di Python Developers Survey 2024, 7% orang yang bekerja dengan big",
                    "data memakai Great Expectations dan 4% memakai PyDeequ.",
                ],
                "code": """import great_expectations as gx
import pandas as pd

df = pd.DataFrame({
    "id": ["P001", "P002", "P003"],
    "email": ["a@contoh.id", None, "c@contoh.id"],
    "jumlah": [2, -1, 3],
})

context = gx.get_context()
sumber = context.data_sources.add_pandas("pandas")
aset = sumber.add_dataframe_asset(name="pesanan")
batch_def = aset.add_batch_definition_whole_dataframe("semua")
batch = batch_def.get_batch(batch_parameters={"dataframe": df})

suite = gx.ExpectationSuite(name="pesanan_harian")
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="email"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="id"))
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(column="jumlah", min_value=1))

hasil = batch.validate(suite)
print(hasil.success)                    # False
for r in hasil.results:
    print(r.expectation_config.type, r.success)""",
            },
            {
                "heading": "Lineage, metadata, dan data catalog",
                "body": [
                    "Bayangkan angka omzet di dasbor tiba-tiba aneh. Pertanyaan",
                    "pertama: angka ini datang dari tabel mana, dan tabel itu dari",
                    "mana? Peta asal-usul data seperti itu disebut lineage. Dari arah",
                    "sebaliknya, lineage juga menjawab pertanyaan sebelum mengubah",
                    "sesuatu: kalau kolom ini diganti namanya, laporan apa saja yang",
                    "rusak?",
                    "",
                    "Lineage adalah bagian dari metadata, yaitu data tentang data:",
                    "siapa pemilik tabel, arti tiap kolom, seberapa sering diperbarui,",
                    "kolom mana yang berisi data pribadi. Metadata dikumpulkan di data",
                    "catalog supaya orang bisa mencari tabel yang mereka butuhkan.",
                    "",
                    "Untuk lineage ada OpenLineage, standar terbuka untuk mencatat",
                    "lineage dari Airflow, Spark, dan dbt. Untuk data catalog ada",
                    "DataHub dan OpenMetadata (open source), Unity Catalog di",
                    "Databricks, AWS Glue Data Catalog, dan Hive Metastore yang masih",
                    "dipakai banyak sistem lama.",
                ],
            },
            {
                "heading": "Data pribadi: UU PDP dan GDPR",
                "body": [
                    "Di Indonesia, pemrosesan data pribadi diatur Undang-Undang Nomor",
                    "27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), yang",
                    "disahkan Oktober 2022 dengan masa penyesuaian dua tahun. Beberapa",
                    "hal yang langsung menyentuh pekerjaan data:",
                    "",
                    "  - Ada data pribadi yang bersifat spesifik dan butuh perlindungan",
                    "    lebih: data kesehatan, biometrik, genetika, catatan kejahatan,",
                    "    data anak, dan data keuangan pribadi.",
                    "  - Pemrosesan harus punya dasar yang sah, misalnya persetujuan,",
                    "    dan dibatasi untuk tujuan yang disampaikan.",
                    "  - Kalau terjadi kegagalan pelindungan data, misalnya kebocoran,",
                    "    pengendali data wajib memberi tahu subjek data dan lembaga",
                    "    pengawas secara tertulis paling lambat 3 x 24 jam (Pasal 46).",
                    "  - Sanksi administratifnya bisa sampai denda 2% dari pendapatan",
                    "    tahunan, di samping ancaman pidana untuk pelanggaran tertentu.",
                    "",
                    "Kalau perusahaanmu melayani orang di Uni Eropa, berlaku juga GDPR",
                    "(sejak 25 Mei 2018). Kebocoran harus dilaporkan ke otoritas dalam",
                    "72 jam, dan dendanya bisa sampai 20 juta euro atau 4% omzet global",
                    "tahunan, mana yang lebih besar. Ini ringkasan untuk orang teknis.",
                    "Untuk keputusan hukum, tanyakan ke bagian legal.",
                ],
            },
            {
                "heading": "Pseudonim dan penyamaran",
                "code": """import hashlib
import hmac

KUNCI = b"rahasia-dari-brankas"   # di produksi: ambil dari secret manager

def pseudonim(nilai):
    return hmac.new(KUNCI, nilai.encode(), hashlib.sha256).hexdigest()[:16]

def samarkan_hp(nomor):
    return nomor[:4] + "*" * (len(nomor) - 7) + nomor[-3:]

pelanggan = {"nik": "1234567890123456", "email": "rina@contoh.id",
             "hp": "081234567890", "kota": "Bandung"}

untuk_analis = {
    "id_pelanggan": pseudonim(pelanggan["nik"]),
    "hp": samarkan_hp(pelanggan["hp"]),
    "kota": pelanggan["kota"],
}
print(untuk_analis["id_pelanggan"], untuk_analis["hp"], untuk_analis["kota"])
print(pseudonim("1234567890123456") == untuk_analis["id_pelanggan"])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ecba89a1c2b5bfb5 0812*****890 Bandung",
                    "  True",
                    "",
                    "Analis churn nggak butuh NIK atau email. Mereka butuh cara",
                    "mengenali pelanggan yang sama di beberapa tabel. Pseudonim",
                    "memberinya: nilai yang sama selalu jadi kode yang sama, tapi",
                    "kodenya nggak bisa dibalik jadi NIK tanpa kunci rahasia. Email",
                    "nggak dikirim sama sekali, karena nggak dibutuhkan. Itu prinsip",
                    "minimisasi data: kirim kolom yang perlu saja.",
                    "",
                    "Jebakan: hash biasa tanpa kunci, misalnya sha256(email), bisa",
                    "dibalik dengan menebak. Penyerang cukup menghitung hash dari",
                    "daftar email atau semua kemungkinan NIK, lalu mencocokkannya.",
                    "Makanya contoh ini memakai HMAC dengan kunci yang disimpan",
                    "terpisah. Data yang dipseudonimkan juga tetap dianggap data",
                    "pribadi oleh GDPR, karena masih bisa dihubungkan kembali oleh",
                    "pemegang kunci.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kebocoran data pribadi beberapa kali jadi berita besar di",
                    "Indonesia. Sejak UU PDP berlaku, perusahaan yang mengolah",
                    "data pelanggan, dari fintech sampai e-commerce, menyusun ulang",
                    "siapa boleh melihat kolom apa. Pekerjaan itu banyak jatuh ke tim",
                    "data, karena merekalah yang membangun pipeline dan gudang datanya.",
                    "",
                    "Kasus kecil: tim analis minta salinan tabel pelanggan untuk",
                    "analisis pelanggan yang berhenti belanja (churn). Tabelnya berisi",
                    "NIK, nama, email, nomor HP, alamat lengkap, kota, dan riwayat",
                    "belanja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tanyakan kolom apa yang benar dibutuhkan. Untuk churn",
                    "     biasanya cukup id pelanggan, kota, tanggal daftar, dan",
                    "     riwayat belanja.",
                    "  2. Ganti NIK dengan pseudonim HMAC dan jangan kirim nama, email,",
                    "     nomor HP, atau alamat lengkap.",
                    "  3. Kalau nomor HP tetap perlu, misalnya untuk mengecek operator,",
                    "     kirim versi yang disamarkan seperti 0812*****890.",
                    "  4. Buat tabel atau view khusus analis di gudang data dan beri",
                    "     akses ke situ saja, bukan ke tabel aslinya.",
                    "  5. Catat di data catalog bahwa tabel asli memuat data pribadi,",
                    "     siapa pemiliknya, dan berapa lama data boleh disimpan.",
                ],
            },
        ],
    },
    {
        "title": "32. Apache Airflow: DAG, Jadwal, dan Retry",
        "sections": [
            {
                "body": [
                    "Bayangkan tiap malam ada empat skrip yang harus jalan berurutan:",
                    "ambil data pesanan dari database toko, bersihkan, muat ke gudang",
                    "data, lalu kirim laporan ke tim. Cara paling gampang adalah cron,",
                    "penjadwal bawaan Linux yang menjalankan perintah pada jam tertentu.",
                    "Skrip pertama jalan pukul 01.00, skrip kedua pukul 01.30, dan",
                    "seterusnya.",
                    "",
                    "Masalahnya muncul waktu ada yang meleset. Kalau pengambilan data",
                    "telat selesai karena server toko lambat, skrip pembersih tetap jalan",
                    "pukul 01.30 dan membaca berkas yang belum lengkap. Kalau satu skrip",
                    "gagal karena koneksi putus sebentar, nggak ada yang mencoba ulang.",
                    "Kamu baru tahu besok paginya, waktu laporannya kosong.",
                    "",
                    "Apache Airflow dibuat untuk masalah seperti ini. Airflow adalah",
                    "orkestrator, yaitu program yang mengatur kapan dan dalam urutan apa",
                    "pekerjaan dijalankan. Ia juga mencoba ulang pekerjaan yang gagal dan",
                    "mencatat semuanya di satu halaman web. Airflow dimulai di Airbnb pada",
                    "2014, lalu jadi proyek Apache. Pipeline-nya ditulis sebagai kode",
                    "Python biasa.",
                ],
            },
            {
                "heading": "DAG: graf tugas tanpa putaran",
                "body": [
                    "Satu pipeline di Airflow disebut DAG, singkatan dari Directed",
                    "Acyclic Graph. Namanya kedengaran rumit, tapi bisa dipecah jadi tiga",
                    "kata:",
                    "  - Graph (graf): kumpulan titik yang disambung garis. Di sini",
                    "    titiknya adalah task, yaitu satu pekerjaan kecil seperti \"ambil",
                    "    data\".",
                    "  - Directed (berarah): garisnya punya panah. Panah dari ekstrak ke",
                    "    bersihkan artinya bersihkan baru boleh jalan sesudah ekstrak",
                    "    selesai.",
                    "  - Acyclic (tanpa putaran): kalau kamu mengikuti panahnya, kamu",
                    "    nggak pernah balik ke titik awal. Kalau A menunggu B dan B",
                    "    menunggu A, dua-duanya menunggu selamanya, jadi DAG seperti itu",
                    "    ditolak.",
                    "",
                    "Python punya modul bawaan graphlib yang bisa mengurutkan graf",
                    "seperti ini. Kita pakai dulu untuk melihat apa yang dikerjakan",
                    "Airflow waktu menentukan urutan, tanpa memasang apa pun.",
                ],
            },
            {
                "heading": "Urutan task dengan graphlib",
                "code": """from graphlib import TopologicalSorter, CycleError

# task -> daftar task yang harus selesai lebih dulu
dag = {
    "ekstrak": [],
    "bersihkan": ["ekstrak"],
    "muat": ["bersihkan"],
    "lapor": ["muat"],
}
urutan = list(TopologicalSorter(dag).static_order())
print(" -> ".join(urutan))

dag["ekstrak"] = ["lapor"]  # sengaja bikin putaran
try:
    list(TopologicalSorter(dag).static_order())
except CycleError as e:
    print("ditolak:", e.args[0])
    print("putarannya:", " -> ".join(e.args[1]))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ekstrak -> bersihkan -> muat -> lapor",
                    "  ditolak: nodes are in a cycle",
                    "  putarannya: ekstrak -> bersihkan -> muat -> lapor -> ekstrak",
                    "",
                    "Dict dag menulis ketergantungan. Kuncinya nama task, isinya daftar",
                    "task yang harus selesai lebih dulu. TopologicalSorter menyusun",
                    "urutan yang memenuhi semua panah itu, dan urutan seperti ini disebut",
                    "urutan topologis. Begitu ekstrak dibuat menunggu lapor, terbentuk",
                    "putaran, dan graphlib menolak dengan CycleError sambil menyebut",
                    "putarannya.",
                    "",
                    "Airflow melakukan pemeriksaan yang sama waktu membaca berkas DAG-mu.",
                    "Bedanya, Airflow juga tahu kapan DAG harus jalan, status tiap task,",
                    "dan apa yang harus dilakukan kalau sebuah task gagal.",
                ],
            },
            {
                "heading": "DAG Airflow sungguhan (dags/laporan_harian.py)",
                "code": """from datetime import datetime, timedelta

from airflow.sdk import dag, task


@dag(
    schedule="0 2 * * *",
    start_date=datetime(2026, 10, 1),
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=5)},
    tags=["toko"],
)
def laporan_harian():
    @task
    def ekstrak():
        return [{"id": 1, "jumlah": 50000}, {"id": 2, "jumlah": None}]

    @task
    def bersihkan(baris):
        return [b for b in baris if b["jumlah"] is not None]

    @task
    def muat(baris):
        print(f"memuat {len(baris)} baris ke gudang data")
        return len(baris)

    @task
    def lapor(jumlah):
        print(f"laporan siap: {jumlah} pesanan")

    lapor(muat(bersihkan(ekstrak())))


laporan_harian()""",
            },
            {
                "body": [
                    "Bagian-bagiannya:",
                    "  - @dag(...) mengubah fungsi laporan_harian jadi DAG. Nama",
                    "    fungsinya jadi dag_id, nama yang tampil di halaman web Airflow.",
                    "  - @task mengubah fungsi biasa jadi task. Gaya menulis seperti ini",
                    "    disebut TaskFlow API.",
                    "  - lapor(muat(bersihkan(ekstrak()))) menentukan urutan sekaligus",
                    "    mengoper hasil satu task ke task berikutnya. Dari baris itu",
                    "    Airflow tahu ekstrak harus jalan paling dulu.",
                    "  - laporan_harian() di baris paling bawah mendaftarkan DAG-nya.",
                    "    Kalau lupa, berkasnya tetap dibaca tapi DAG-nya nggak muncul.",
                    "",
                    "Berkas ini disimpan di folder dags milik Airflow. Bagian Airflow yang",
                    "namanya DAG processor membaca ulang tiap berkas di folder itu secara",
                    "berkala, bawaannya tiap 30 detik. Artinya kode di luar fungsi task",
                    "ikut jalan tiap kali berkasnya dibaca. Query ke database yang ditaruh",
                    "di tingkat atas berkas bakal jalan dua kali semenit sepanjang hari,",
                    "walaupun DAG-nya cuma terjadwal sekali sehari.",
                ],
            },
            {
                "heading": "Jadwal dan logical date",
                "body": [
                    "Parameter schedule menerima ekspresi cron atau singkatan seperti",
                    "@daily (tiap tengah malam) dan @hourly (tiap awal jam). Ekspresi cron",
                    "punya lima kolom:",
                    "",
                    "  menit  jam  tanggal  bulan  hari",
                    "    0     2      *       *     *      tiap hari pukul 02.00",
                    "    30    6      *       *     1      tiap Senin pukul 06.30",
                    "",
                    "Tanda bintang artinya semua nilai. Kalau zona waktunya nggak diatur,",
                    "Airflow memakai UTC. Pukul 02.00 UTC sama dengan pukul 09.00 WIB,",
                    "jadi tim di Jakarta sering heran kenapa laporan jam dua pagi baru",
                    "datang siang. Zona waktu bisa ditempel di start_date, misalnya",
                    "pendulum.datetime(2026, 10, 1, tz=\"Asia/Jakarta\").",
                    "",
                    "start_date adalah tanggal paling awal DAG boleh dijadwalkan. catchup",
                    "menentukan apa yang terjadi kalau start_date sudah lewat waktu DAG",
                    "baru dinyalakan. Dengan catchup=False, Airflow cuma menjadwalkan run",
                    "berikutnya dan nggak mengejar hari-hari yang terlewat. Sejak Airflow",
                    "3, catchup memang mati secara bawaan, tapi menuliskannya bikin niatmu",
                    "jelas buat pembaca berikutnya.",
                    "",
                    "Tiap run punya logical date, yaitu tanggal yang diwakili run itu. Di",
                    "Airflow 3, untuk jadwal cron seperti contoh di atas, logical date",
                    "sama dengan waktu run itu dijadwalkan. Tutorial Airflow 2 memakai",
                    "aturan lama: run untuk tanggal 18 baru jalan sesudah tanggal 18",
                    "berakhir, jadi logical date-nya selalu satu periode di belakang.",
                    "Aturan lama itu masih bisa dinyalakan lewat setelan",
                    "create_cron_data_intervals, tapi bawaannya sekarang mati.",
                ],
            },
            {
                "heading": "Retry",
                "body": [
                    "Banyak kegagalan di pipeline cuma sesaat: koneksi putus, API sedang",
                    "sibuk, atau tabel sedang dikunci proses lain. Untuk itu ada retry,",
                    "yaitu mencoba ulang task yang gagal sebelum menyatakannya gagal.",
                    "",
                    "Di contoh tadi, default_args berlaku untuk semua task di DAG itu.",
                    "retries=2 dan retry_delay=timedelta(minutes=5) artinya kalau muat",
                    "gagal, Airflow menunggu lima menit lalu mencoba lagi, paling banyak",
                    "dua kali. Totalnya tiga percobaan. Kalau percobaan ketiga juga gagal,",
                    "status muat jadi failed dan lapor nggak dijalankan. Status lapor",
                    "jadi upstream_failed, artinya ada task di hulunya yang gagal.",
                    "",
                    "Bawaan Airflow adalah 0 retry. Kalau kamu nggak mengaturnya, satu",
                    "gangguan kecil langsung menggagalkan seluruh run. Ada juga",
                    "retry_exponential_backoff=True yang membuat jeda antarpercobaan",
                    "makin panjang. Ini berguna untuk API yang membatasi jumlah",
                    "permintaan.",
                    "",
                    "Ingat: retry menjalankan task yang sama lebih dari sekali. Itu cuma",
                    "aman kalau hasil task-nya tetap sama walaupun diulang. Materi",
                    "berikutnya membahas cara menulis task seperti itu.",
                ],
            },
            {
                "heading": "Versi dan cara memasang",
                "body": [
                    "Airflow 3.0 rilis April 2025 dan mengubah banyak hal. Versi stabil",
                    "terbaru saat materi ini ditulis (Oktober 2026) adalah 3.3.2, dan 3.4",
                    "sedang diuji sebagai beta. Perubahan yang paling sering bikin",
                    "tutorial lama gagal:",
                    "  - Impor untuk menulis DAG pindah ke airflow.sdk. Impor lama seperti",
                    "    airflow.decorators masih jalan, tapi memunculkan peringatan",
                    "    usang.",
                    "  - Parameter schedule_interval dihapus. Contoh yang memakainya",
                    "    langsung error, gantinya schedule.",
                    "  - BashOperator, PythonOperator, dan operator dasar lain pindah ke",
                    "    paket provider standard.",
                    "  - Halaman webnya dibangun ulang, dan proses webserver diganti",
                    "    api-server.",
                    "  - DAG punya versi. Kalau kodenya berubah, run lama tetap tercatat",
                    "    dengan versi DAG yang dipakainya waktu itu.",
                    "",
                    "Airflow jalan di Linux dan macOS. Windows nggak didukung langsung,",
                    "jadi pengguna Windows memakai WSL2 atau Docker. Di Fedora kamu bisa",
                    "langsung memasangnya di venv. Pakai berkas constraint resmi supaya",
                    "versi semua paket pendukungnya cocok satu sama lain:",
                ],
            },
            {
                "heading": "Memasang Airflow 3.3.2",
                "bahasa": "terminal",
                "code": "python3 -m venv .venv\nsource .venv/bin/activate\nAIRFLOW_VERSION=3.3.2\nPYTHON_VERSION=\"$(python -c 'import sys; print(f\"{sys.version_info.major}.{sys.version_info.minor}\")')\"\npip install \"apache-airflow==${AIRFLOW_VERSION}\" \\\n  --constraint \"https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt\"\nairflow standalone",
            },
            {
                "heading": "Mencoba di laptop",
                "body": [
                    "airflow standalone menyalakan semua bagian Airflow sekaligus untuk",
                    "dicoba di laptop. Halaman webnya bisa dibuka di",
                    "http://localhost:8080. Taruh berkas laporan_harian.py di folder",
                    "dags di dalam AIRFLOW_HOME (bawaannya ~/airflow), dan DAG-nya muncul",
                    "sesudah dibaca DAG processor. Untuk server sungguhan, tiap bagian",
                    "dijalankan terpisah dan databasenya PostgreSQL atau MySQL.",
                    "",
                    "Jebakan: start_date=datetime.now(). Nilainya berubah tiap kali",
                    "berkas dibaca ulang, jadi jadwalnya ikut bergeser dan run bisa nggak",
                    "pernah terpicu. Pakai tanggal tetap.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Airflow dipakai tim yang punya banyak pipeline data harian. Contohnya",
                    "toko online yang menghitung ulang laporan penjualan tiap malam,",
                    "fintech yang menarik data transaksi dari mitra, atau tim data yang",
                    "melatih ulang model rekomendasi tiap minggu. Cloud besar juga menjual",
                    "Airflow terkelola, misalnya Amazon Managed Workflows for Apache",
                    "Airflow dan Google Cloud Composer, jadi timnya nggak perlu merawat",
                    "servernya sendiri.",
                    "",
                    "Kasus kecil: tiap pagi tim keuangan menerima laporan omzet kemarin",
                    "dari tiga skrip cron. Dua kali bulan ini laporannya kosong, karena",
                    "skrip pertama gagal mengambil data sementara dua skrip lain tetap",
                    "jalan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jadikan tiga skrip itu tiga task dalam satu DAG dengan urutan",
                    "     ekstrak, hitung, kirim. Task sesudahnya otomatis nggak jalan",
                    "     kalau task sebelumnya gagal.",
                    "  2. Pasang retries=3 dan retry_delay=timedelta(minutes=10) di",
                    "     default_args, karena penyebab gagalnya koneksi yang putus",
                    "     sesaat.",
                    "  3. Atur jadwalnya ke pukul 06.00 WIB. Kalau DAG memakai UTC, itu",
                    "     berarti schedule=\"0 23 * * *\" (pukul 23.00 UTC hari",
                    "     sebelumnya).",
                    "  4. Pasang on_failure_callback yang mengirim pesan ke grup tim,",
                    "     supaya kegagalan yang tersisa sesudah semua retry langsung",
                    "     ketahuan pagi itu juga.",
                ],
            },
        ],
    },
    {
        "title": "33. Airflow dalam Praktik: Operator, XCom, Backfill",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya memakai @task untuk semua pekerjaan. Di proyek",
                    "sungguhan kamu juga bakal ketemu operator, cara Airflow yang lebih",
                    "tua untuk mendefinisikan task dan masih dipakai di mana-mana.",
                    "",
                    "Operator adalah cetakan task yang sudah jadi. Kamu tinggal mengisi",
                    "parameternya. Beberapa yang paling sering muncul:",
                    "  - BashOperator menjalankan perintah shell.",
                    "  - PythonOperator menjalankan fungsi Python. @task adalah cara",
                    "    singkat untuk menulis operator ini.",
                    "  - SQLExecuteQueryOperator menjalankan query ke database lewat",
                    "    sebuah connection, yaitu alamat dan kata sandi database yang",
                    "    disimpan di Airflow, bukan di kode.",
                    "  - Sensor menunggu sesuatu terjadi, misalnya berkas muncul di",
                    "    folder atau task di DAG lain selesai.",
                    "",
                    "Operator untuk layanan luar dibagi ke paket terpisah yang disebut",
                    "provider, misalnya apache-airflow-providers-postgres atau",
                    "apache-airflow-providers-amazon. Kamu cuma memasang provider yang",
                    "dipakai.",
                ],
            },
            {
                "heading": "Operator dan TaskFlow dalam satu DAG",
                "code": """from datetime import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import dag, task


@dag(schedule="@daily", start_date=datetime(2026, 10, 1), catchup=False)
def ekspor_pesanan():
    unduh = BashOperator(
        task_id="unduh",
        bash_command="echo /data/pesanan/{{ ds }}.csv",
    )

    @task
    def hitung(jalur):
        print(f"membaca {jalur}")
        return {"jalur": jalur, "baris": 120}

    @task
    def umumkan(info):
        print(f"{info['jalur']}: {info['baris']} baris")

    umumkan(hitung(unduh.output))


ekspor_pesanan()""",
            },
            {
                "body": [
                    "{{ ds }} di dalam bash_command adalah templat Jinja. Waktu task",
                    "dijalankan, Airflow menggantinya dengan logical date run itu dalam",
                    "bentuk 2026-10-18. Jadi run untuk tanggal 18 mencetak",
                    "/data/pesanan/2026-10-18.csv, dan run untuk tanggal 3 mencetak",
                    "berkas tanggal 3.",
                    "",
                    "BashOperator menyimpan baris terakhir keluarannya sebagai XCom.",
                    "XCom, singkatan dari cross-communication, adalah cara task mengoper",
                    "nilai kecil ke task lain. Nilainya disimpan di database metadata",
                    "Airflow. unduh.output menunjuk nilai itu, jadi hitung menerima jalur",
                    "berkas sebagai argumen. Dict yang dikembalikan hitung juga otomatis",
                    "jadi XCom, lalu dibaca umumkan.",
                    "",
                    "Jebakan: memakai XCom untuk mengoper isi tabel. XCom cocok untuk",
                    "jalur berkas, jumlah baris, atau nomor batch. Data jutaan baris",
                    "harus diubah dulu jadi bentuk yang bisa disimpan, ditulis ke",
                    "database metadata, lalu dibaca ulang, dan database itu nggak",
                    "dirancang untuk data bisnis. Polanya: task pertama menulis datanya",
                    "ke penyimpanan (berkas Parquet di object storage atau tabel di",
                    "gudang data), lalu cuma mengoper alamatnya lewat XCom.",
                ],
            },
            {
                "heading": "Siapa mengerjakan apa",
                "body": [
                    "Airflow terdiri dari beberapa proses yang bekerja bareng:",
                    "  - Scheduler memutuskan run mana yang sudah waktunya dan task mana",
                    "    yang siap jalan, lalu mengantrekannya.",
                    "  - DAG processor membaca berkas di folder dags dan menyimpan",
                    "    strukturnya ke database. Di Airflow 3 ini proses tersendiri.",
                    "  - Executor menentukan di mana task dijalankan. LocalExecutor",
                    "    menjalankan task sebagai proses di mesin yang sama.",
                    "    CeleryExecutor membaginya ke beberapa mesin worker.",
                    "    KubernetesExecutor membuat satu pod untuk tiap task.",
                    "  - Worker adalah proses yang menjalankan kode task-mu.",
                    "  - API server melayani halaman web dan API. Di Airflow 3, worker",
                    "    melapor status dan XCom ke sini, nggak lagi langsung ke",
                    "    database.",
                    "  - Database metadata menyimpan status semua run, task, XCom, dan",
                    "    riwayatnya. Untuk server sungguhan dipakai PostgreSQL atau",
                    "    MySQL. SQLite cuma untuk coba-coba.",
                    "",
                    "Kalau halaman web mati, run tetap jalan karena yang menjadwalkan",
                    "adalah scheduler. Sebaliknya, kalau scheduler mati, halaman webnya",
                    "masih bisa dibuka tapi nggak ada run baru yang dimulai.",
                ],
            },
            {
                "heading": "Backfill: menjalankan untuk tanggal yang lewat",
                "body": [
                    "Backfill adalah menjalankan DAG untuk rentang tanggal di masa lalu.",
                    "Kebutuhannya muncul terus. DAG baru dibuat dan kamu butuh data tiga",
                    "bulan ke belakang. Atau ada bug di rumus omzet yang baru ketahuan,",
                    "dan semua laporan minggu lalu harus dihitung ulang.",
                    "",
                    "Di Airflow 3, backfill dikelola scheduler dan bisa dibuat lewat",
                    "halaman web atau perintah. Sebelum itu, ada dua perintah untuk",
                    "mencoba DAG tanpa menunggu jadwal:",
                    "  - airflow dags test menjalankan satu run penuh untuk satu tanggal,",
                    "    langsung di terminal.",
                    "  - airflow tasks test menjalankan satu task saja, tanpa",
                    "    memperhatikan task lain.",
                ],
            },
            {
                "heading": "Mencoba dan membuat backfill",
                "bahasa": "terminal",
                "code": "airflow dags test laporan_harian 2026-10-18\nairflow tasks test laporan_harian muat 2026-10-18\nairflow backfill create --dag-id laporan_harian \\\n  --from-date 2026-10-01 --to-date 2026-10-07",
            },
            {
                "heading": "Task yang aman diulang",
                "body": [
                    "Perintah terakhir membuat tujuh run, satu untuk tiap tanggal 1",
                    "sampai 7 Oktober. Kalau tanggal itu sudah punya run, opsi",
                    "--reprocess-behavior menentukan apakah run-nya diulang.",
                    "",
                    "Retry dan backfill sama-sama menjalankan task yang sama lebih dari",
                    "sekali. Itu cuma aman kalau task-nya idempoten: dijalankan sekali",
                    "atau lima kali, hasil akhirnya sama. Konsepnya sudah dibahas di",
                    "materi ETL di bab 9. Di Airflow, wujudnya begini.",
                    "",
                    "Task yang menambah baris dengan INSERT polos nggak idempoten. Kalau",
                    "task itu gagal di tengah lalu di-retry, baris yang sudah sempat",
                    "masuk jadi dobel. Polanya: hapus dulu data tanggal yang sedang",
                    "diproses, baru masukkan. Tanggalnya diambil dari logical date run,",
                    "bukan dari jam sekarang, supaya backfill untuk 3 Oktober mengisi",
                    "data 3 Oktober.",
                ],
            },
            {
                "heading": "Hapus dulu, baru isi",
                "code": """import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE omzet (tanggal TEXT, kota TEXT, total INTEGER)")

sumber = {
    "2026-10-03": [("Bandung", 70000), ("Medan", 75000)],
    "2026-10-04": [("Bandung", 20000)],
}


def muat_polos(tanggal):
    db.executemany(
        "INSERT INTO omzet VALUES (?, ?, ?)",
        [(tanggal, kota, total) for kota, total in sumber[tanggal]],
    )


def muat_idempoten(tanggal):
    with db:  # satu transaksi: hapus lalu isi ulang
        db.execute("DELETE FROM omzet WHERE tanggal = ?", (tanggal,))
        muat_polos(tanggal)


def jumlah_baris():
    return db.execute("SELECT COUNT(*) FROM omzet").fetchone()[0]


muat_polos("2026-10-03")
muat_polos("2026-10-03")  # retry pada versi polos
print("polos, dijalankan 2x:", jumlah_baris(), "baris")

db.execute("DELETE FROM omzet")
for _ in range(3):  # run pertama, lalu dua retry
    muat_idempoten("2026-10-03")
muat_idempoten("2026-10-04")
print("idempoten, dijalankan 4x:", jumlah_baris(), "baris")
for baris in db.execute("SELECT * FROM omzet ORDER BY tanggal, kota"):
    print(baris)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  polos, dijalankan 2x: 4 baris",
                    "  idempoten, dijalankan 4x: 3 baris",
                    "  ('2026-10-03', 'Bandung', 70000)",
                    "  ('2026-10-03', 'Medan', 75000)",
                    "  ('2026-10-04', 'Bandung', 20000)",
                    "",
                    "Versi polos dijalankan dua kali dan isinya jadi dobel. Versi",
                    "idempoten dijalankan tiga kali untuk tanggal 3 dan sekali untuk",
                    "tanggal 4, dan tabelnya tetap berisi tiga baris yang benar.",
                    "",
                    "with db membungkus DELETE dan INSERT dalam satu transaksi. Kalau",
                    "INSERT gagal di tengah, DELETE ikut dibatalkan, jadi tabelnya nggak",
                    "pernah kosong setengah jalan. Di gudang data, pola yang sama ditulis",
                    "dengan MERGE atau dengan menimpa satu partisi tanggal sekaligus.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di tim data yang memakai Airflow, backfill adalah pekerjaan rutin:",
                    "rumus metrik dibetulkan, sumber data baru ditambahkan, atau server",
                    "mati semalaman sehingga run-nya terlewat. Tim yang task-nya",
                    "idempoten cukup membuat backfill untuk rentang tanggalnya. Tim yang",
                    "task-nya nggak idempoten harus membersihkan data dobel dengan tangan",
                    "dulu.",
                    "",
                    "Kasus kecil: rumus diskon di task hitung_omzet ternyata salah sejak",
                    "1 Oktober. Rumusnya sudah dibetulkan hari ini, 19 Oktober, dan",
                    "laporan 1 sampai 18 Oktober harus dihitung ulang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan task muat menghapus data per tanggal sebelum mengisi",
                    "     ulang, dan tanggalnya diambil dari logical date (misalnya",
                    "     templat {{ ds }}), bukan dari jam sekarang.",
                    "  2. Coba satu tanggal dulu dengan airflow dags test laporan_harian",
                    "     2026-10-01, lalu cocokkan hasilnya dengan hitungan manual.",
                    "  3. Buat backfill-nya, termasuk tanggal yang run-nya sudah pernah",
                    "     selesai:",
                    "       airflow backfill create --dag-id laporan_harian \\",
                    "         --from-date 2026-10-01 --to-date 2026-10-18 \\",
                    "         --reprocess-behavior completed",
                    "  4. Sesudah selesai, hitung baris per tanggal. Tanggal yang barisnya",
                    "     dua kali lipat dari biasanya tanda task muatnya belum",
                    "     idempoten.",
                ],
            },
        ],
    },
    {
        "title": "34. dbt: Model SQL, ref, dan Uji Data",
        "sections": [
            {
                "body": [
                    "Sesudah data mentah masuk gudang data, pekerjaan berikutnya adalah",
                    "mengubahnya jadi tabel yang siap dipakai laporan: membuang pesanan",
                    "batal, menggabung pesanan dengan pelanggan, menghitung omzet per",
                    "kota. Di banyak tim, pekerjaan ini dulu berupa puluhan berkas SQL",
                    "yang dijalankan berurutan dengan tangan. Kalau satu tabel di tengah",
                    "berubah, nggak ada yang tahu tabel mana saja yang ikut rusak.",
                    "",
                    "dbt (data build tool, selalu ditulis huruf kecil) membereskan bagian",
                    "ini. Di pola ELT, data dimuat dulu ke gudang data, lalu",
                    "ditransformasi di sana, dan dbt mengerjakan bagian transformasi itu.",
                    "dbt sendiri nggak memindahkan dan nggak menyimpan data. Ia mengirim",
                    "SQL ke gudang datamu (Snowflake, BigQuery, Databricks, PostgreSQL,",
                    "DuckDB, dan lain-lain), dan gudang data itulah yang bekerja.",
                ],
            },
            {
                "heading": "Model: satu berkas, satu SELECT",
                "body": [
                    "Di dbt, satu model adalah satu berkas .sql yang isinya satu perintah",
                    "SELECT. Nama berkasnya jadi nama tabel atau view hasilnya. Kamu",
                    "nggak menulis CREATE TABLE, karena dbt yang membungkus SELECT-mu",
                    "dengan perintah pembuatnya. Tiga model di bawah ditaruh di dua",
                    "folder: staging untuk merapikan data mentah, marts untuk tabel yang",
                    "dibaca laporan.",
                ],
            },
            {
                "heading": "Tiga model dalam satu proyek",
                "bahasa": "jinja",
                "code": """-- models/staging/stg_pesanan.sql
select
    id as id_pesanan,
    id_pelanggan,
    jumlah
from {{ source('toko', 'raw_pesanan') }}
where status = 'selesai'

-- models/staging/stg_pelanggan.sql
select
    id as id_pelanggan,
    nama,
    kota
from {{ source('toko', 'raw_pelanggan') }}

-- models/marts/omzet_per_kota.sql
{{ config(materialized='table') }}

select
    c.kota,
    count(*) as jumlah_pesanan,
    sum(p.jumlah) as omzet
from {{ ref('stg_pesanan') }} as p
join {{ ref('stg_pelanggan') }} as c
    on c.id_pelanggan = p.id_pelanggan
group by c.kota""",
            },
            {
                "body": [
                    "Kurung kurawal ganda itu sintaks Jinja, bahasa templat yang juga",
                    "dipakai Airflow untuk {{ ds }}. Ada dua fungsi yang paling penting:",
                    "  - source('toko', 'raw_pesanan') menunjuk tabel mentah yang dimuat",
                    "    alat lain. Sumber didaftarkan sekali di berkas YAML.",
                    "  - ref('stg_pesanan') menunjuk model lain di proyek yang sama.",
                    "",
                    "Sebelum dikirim ke gudang data, dbt mengganti ref dengan nama",
                    "lengkap tabelnya, misalnya \"toko\".\"main\".\"stg_pesanan\" di",
                    "DuckDB. Gunanya dua. Nama skema bisa beda antara laptopmu dan server",
                    "produksi, dan ref yang mengurusnya. Lalu dari semua ref, dbt",
                    "menyusun DAG antarmodel. dbt tahu omzet_per_kota butuh stg_pesanan",
                    "dan stg_pelanggan, jadi keduanya dibangun lebih dulu tanpa kamu",
                    "tulis urutannya.",
                    "",
                    "config(materialized='table') menentukan bentuk hasilnya, yang di",
                    "dbt disebut materialization:",
                    "  - view: cuma menyimpan query-nya. Murah, tapi dihitung ulang tiap",
                    "    kali dibaca.",
                    "  - table: hasilnya disimpan sebagai tabel. Cepat dibaca, dibangun",
                    "    ulang penuh tiap dbt run.",
                    "  - incremental: cuma memproses baris baru sejak run terakhir.",
                    "    Dipakai untuk tabel besar seperti log klik.",
                    "  - ephemeral: nggak dibuat di gudang data sama sekali, disisipkan",
                    "    sebagai CTE ke model yang memakainya.",
                ],
            },
            {
                "heading": "Uji data (models/staging/schema.yml)",
                "bahasa": "yaml",
                "code": """version: 2

models:
  - name: stg_pesanan
    columns:
      - name: id_pesanan
        data_tests:
          - not_null
          - unique
      - name: id_pelanggan
        data_tests:
          - not_null
          - relationships:
              arguments:
                to: ref('stg_pelanggan')
                field: id_pelanggan""",
            },
            {
                "body": [
                    "Empat uji bawaan dbt sudah cukup untuk kebanyakan kebutuhan:",
                    "  - not_null: kolomnya nggak boleh kosong.",
                    "  - unique: nggak boleh ada nilai ganda.",
                    "  - relationships: tiap nilai harus ada di tabel lain.",
                    "  - accepted_values: nilainya cuma boleh dari daftar tertentu.",
                    "",
                    "Di dbt-core versi sekarang, argumen uji seperti to dan field",
                    "ditaruh di bawah arguments. Tutorial yang lebih tua menulisnya",
                    "langsung di bawah nama uji, dan bentuk itu sekarang memunculkan",
                    "peringatan usang. Kunci data_tests juga dulunya bernama tests, dan",
                    "nama lama itu masih diterima.",
                    "",
                    "Yang sering bikin kaget: uji dbt nggak punya mesin khusus. Tiap uji",
                    "diterjemahkan jadi satu query yang mencari baris pelanggar aturan.",
                    "Program di bawah meniru tiga uji tadi dengan sqlite3.",
                ],
            },
            {
                "heading": "Isi sebuah uji dbt",
                "code": """import sqlite3

db = sqlite3.connect(":memory:")
db.executescript('''
CREATE TABLE stg_pelanggan (id_pelanggan INTEGER, kota TEXT);
INSERT INTO stg_pelanggan VALUES (10, 'Bandung'), (12, 'Surabaya');
CREATE TABLE stg_pesanan (id_pesanan INTEGER, id_pelanggan INTEGER);
INSERT INTO stg_pesanan VALUES (1, 10), (3, 10), (4, NULL), (5, 99);
''')

# tiap uji = query yang mencari baris pelanggar aturan
uji = {
    "not_null id_pelanggan":
        "SELECT * FROM stg_pesanan WHERE id_pelanggan IS NULL",
    "unique id_pesanan":
        "SELECT id_pesanan FROM stg_pesanan"
        " GROUP BY id_pesanan HAVING COUNT(*) > 1",
    "relationships id_pelanggan":
        "SELECT p.* FROM stg_pesanan AS p"
        " LEFT JOIN stg_pelanggan AS c ON c.id_pelanggan = p.id_pelanggan"
        " WHERE p.id_pelanggan IS NOT NULL AND c.id_pelanggan IS NULL",
}
for nama, sql in uji.items():
    pelanggar = db.execute(sql).fetchall()
    hasil = "lulus" if not pelanggar else f"gagal, {len(pelanggar)} baris"
    print(f"{nama:28}{hasil}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  not_null id_pelanggan       gagal, 1 baris",
                    "  unique id_pesanan           lulus",
                    "  relationships id_pelanggan  gagal, 1 baris",
                    "",
                    "Pesanan 4 nggak punya pelanggan, dan pesanan 5 menunjuk pelanggan 99",
                    "yang nggak ada. Kalau query sebuah uji mengembalikan nol baris, uji",
                    "itu lulus.",
                    "",
                    "dbt build menjalankan model dan ujinya bergantian sesuai DAG. Kalau",
                    "uji di stg_pesanan gagal, omzet_per_kota nggak dibangun dari data",
                    "yang salah, dan dbt melaporkannya sebagai dilewati (skip).",
                ],
            },
            {
                "heading": "Menjalankan dbt",
                "bahasa": "terminal",
                "code": """pip install dbt-core dbt-duckdb
dbt init toko
dbt build
dbt run --select +omzet_per_kota
dbt test --select stg_pesanan
dbt docs generate && dbt docs serve""",
            },
            {
                "body": [
                    "dbt init membuat kerangka proyek. dbt run membangun model, dbt test",
                    "menjalankan uji, dan dbt build mengerjakan keduanya sesuai urutan",
                    "DAG. --select +omzet_per_kota artinya model itu beserta semua model",
                    "di hulunya. dbt docs generate membuat halaman dokumentasi lengkap",
                    "dengan gambar lineage, yaitu peta tabel mana dibuat dari tabel mana.",
                    "Ada juga dbt snapshot, yang menyimpan riwayat perubahan baris dengan",
                    "pola SCD tipe 2 dari bab 9.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), dbt punya dua mesin:",
                    "  - dbt-core: CLI open source berlisensi Apache 2.0, ditulis dengan",
                    "    Python. Versi stabil terbarunya 1.12.6, dan 2.0 sedang diuji",
                    "    sebagai release candidate.",
                    "  - dbt Fusion: mesin baru yang ditulis ulang dengan Rust. Ia lebih",
                    "    cepat dan bisa memeriksa SQL-mu sebelum dikirim ke gudang data,",
                    "    misalnya menemukan kolom yang salah ketik. Lisensinya beda dari",
                    "    dbt-core, jadi baca syaratnya sebelum dipakai di kantor.",
                    "",
                    "dbt Labs, perusahaan di balik dbt, juga menjual versi cloud",
                    "berbayar dengan editor di browser dan penjadwal. Pada Oktober 2025",
                    "dbt Labs mengumumkan merger dengan Fivetran, perusahaan alat ingest",
                    "yang dibahas di materi berikutnya. Untuk belajar, dbt-core plus",
                    "adaptor dbt-duckdb sudah cukup, dan semuanya jalan di laptop Fedora",
                    "tanpa akun cloud apa pun.",
                    "",
                    "Jebakan: menulis nama tabel langsung, misalnya FROM",
                    "main.stg_pesanan, alih-alih ref('stg_pesanan'). Query-nya tetap",
                    "jalan, tapi dbt nggak tahu ada ketergantungan. Urutan pembangunannya",
                    "bisa salah, dan lineage-nya bolong.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Istilah analytics engineer, yaitu orang yang merawat lapisan",
                    "transformasi di gudang data, dipopulerkan oleh dbt Labs. Lowongan",
                    "untuk posisi itu, dan banyak lowongan data analyst, sekarang",
                    "mencantumkan dbt di samping SQL. Pola folder staging, intermediate,",
                    "dan marts yang kamu lihat di sini juga yang dianjurkan panduan",
                    "resmi dbt.",
                    "",
                    "Kasus kecil: dasbor omzet per kota menunjukkan angka Bandung dua",
                    "kali lipat sejak kemarin. Ternyata tabel pelanggan mentah sekarang",
                    "memuat baris ganda untuk pelanggan yang pindah alamat, jadi join-nya",
                    "menggandakan pesanan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambah uji unique pada kolom id_pelanggan di stg_pelanggan, lalu",
                    "     jalankan dbt test --select stg_pelanggan. Ujinya gagal dan",
                    "     menyebut berapa baris yang ganda.",
                    "  2. Betulkan model staging-nya supaya cuma mengambil baris terbaru",
                    "     per pelanggan, misalnya dengan window function:",
                    "       row_number() over (partition by id order by diperbarui desc)",
                    "     lalu menyaring yang nomornya 1.",
                    "  3. Jalankan dbt build --select stg_pelanggan+ supaya model itu, uji",
                    "     ujinya, dan semua model di hilirnya dibangun ulang.",
                    "  4. Biarkan uji unique itu tetap di schema.yml. Kalau sumbernya",
                    "     mengirim baris ganda lagi, dbt build berhenti sebelum angka yang",
                    "     salah sampai ke dasbor.",
                ],
            },
        ],
    },
    {
        "title": "35. Peta Orkestrasi dan Ingest Data",
        "sections": [
            {
                "body": [
                    "Airflow dan dbt punya banyak tetangga. Supaya nggak tersesat, pisahkan",
                    "dulu tiga pekerjaan yang berbeda:",
                    "  - Orkestrasi: menentukan kapan dan dalam urutan apa pekerjaan",
                    "    jalan. Airflow, Dagster, Prefect, dan Luigi ada di sini.",
                    "  - Ingest: menyalin data dari aplikasi dan database sumber ke gudang",
                    "    data, yaitu huruf E dan L di ETL. Airbyte, Fivetran, dan Apache",
                    "    NiFi ada di sini.",
                    "  - Reverse ETL: kebalikannya, mengirim hasil olahan dari gudang data",
                    "    kembali ke aplikasi bisnis. Contohnya Hightouch, Census, dan",
                    "    Segment.",
                    "",
                    "Satu alat bisa menyentuh lebih dari satu pekerjaan. NiFi misalnya",
                    "sering dipakai untuk ingest sekaligus mengatur aliran datanya.",
                ],
            },
            {
                "heading": "Peta singkat (Oktober 2026)",
                "bahasa": "teks",
                "code": """alat         pekerjaan      cara menulis        lisensi        status
Airflow      orkestrasi     DAG di Python       Apache 2.0     paling banyak dipakai
Dagster      orkestrasi     aset di Python      Apache 2.0     aktif, 1.13.x
Prefect      orkestrasi     @flow dan @task     Apache 2.0     aktif, 3.8.x
Luigi        orkestrasi     kelas Task          Apache 2.0     menurun, 3.8.x
Apache NiFi  aliran data    kanvas visual       Apache 2.0     aktif, 2.12.x
Airbyte      ingest         UI dan konektor     ELv2 dan MIT   aktif
Fivetran     ingest         layanan terkelola   berbayar       aktif
Hightouch,   reverse ETL    layanan terkelola   berbayar       pasar kecil
Census""",
            },
            {
                "heading": "Dagster: yang dijadwalkan adalah hasilnya",
                "body": [
                    "Dagster memakai sudut pandang yang beda dari Airflow. Di Airflow",
                    "kamu mendefinisikan pekerjaan: ekstrak, bersihkan, muat. Di Dagster",
                    "kamu mendefinisikan aset, yaitu benda yang dihasilkan pipeline,",
                    "misalnya tabel stg_pesanan atau berkas laporan, beserta aset lain",
                    "yang dibutuhkannya. Urutan pekerjaan diturunkan dari situ, mirip ref",
                    "di dbt. Karena itu Dagster sering dipasangkan dengan dbt: tiap model",
                    "dbt bisa tampil sebagai aset. Versi stabil terbarunya saat materi",
                    "ini ditulis 1.13.26, berlisensi Apache 2.0.",
                ],
            },
            {
                "heading": "Dua aset di Dagster",
                "code": """import dagster as dg


@dg.asset
def pesanan_mentah():
    return [{"id": 1, "jumlah": 50000}, {"id": 2, "jumlah": 75000}]


@dg.asset
def omzet_harian(pesanan_mentah):
    return sum(p["jumlah"] for p in pesanan_mentah)


defs = dg.Definitions(assets=[pesanan_mentah, omzet_harian])""",
            },
            {
                "body": [
                    "Parameter pesanan_mentah di fungsi omzet_harian bukan variabel",
                    "biasa. Nama itu memberi tahu Dagster bahwa omzet_harian dibangun",
                    "dari aset pesanan_mentah. Pertanyaan yang gampang dijawab dengan",
                    "cara berpikir ini: kalau satu sumber berubah, aset mana saja yang",
                    "sekarang basi? Program di bawah meniru jawabannya dengan Python",
                    "murni.",
                ],
            },
            {
                "heading": "Mencari aset yang basi",
                "code": "# aset -> aset lain yang dibutuhkannya\naset = {\n    \"pesanan_mentah\": [],\n    \"pelanggan_mentah\": [],\n    \"stg_pesanan\": [\"pesanan_mentah\"],\n    \"stg_pelanggan\": [\"pelanggan_mentah\"],\n    \"omzet_per_kota\": [\"stg_pesanan\", \"stg_pelanggan\"],\n    \"laporan_mingguan\": [\"omzet_per_kota\"],\n    \"daftar_vip\": [\"stg_pelanggan\"],\n}\n\n\ndef hilir(nama):\n    \"\"\"Semua aset yang langsung atau lewat perantara memakai `nama`.\"\"\"\n    hasil = set()\n    for anak, induk in aset.items():\n        if nama in induk:\n            hasil |= {anak} | hilir(anak)\n    return hasil\n\n\nfor sumber in (\"pesanan_mentah\", \"pelanggan_mentah\"):\n    print(f\"{sumber} berubah, bangun ulang:\")\n    for nama in sorted(hilir(sumber)):\n        print(\"   \", nama)",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  pesanan_mentah berubah, bangun ulang:",
                    "      laporan_mingguan",
                    "      omzet_per_kota",
                    "      stg_pesanan",
                    "  pelanggan_mentah berubah, bangun ulang:",
                    "      daftar_vip",
                    "      laporan_mingguan",
                    "      omzet_per_kota",
                    "      stg_pelanggan",
                    "",
                    "hilir() menelusuri panah ke arah sebaliknya: dari sebuah aset, cari",
                    "siapa saja yang memakainya, lalu siapa yang memakai mereka. Dagster",
                    "menampilkan hasil penelusuran seperti ini di halaman webnya, jadi",
                    "kamu bisa membangun ulang cuma aset yang terdampak.",
                ],
            },
            {
                "heading": "Prefect, Luigi, dan NiFi",
                "body": [
                    "Prefect memilih jalan yang paling dekat ke Python biasa. Fungsi yang",
                    "sudah ada tinggal diberi dekorator @flow untuk alurnya dan @task",
                    "untuk langkah-langkahnya, seperti contoh di bawah. Retry dan",
                    "riwayat run ikut dari situ. Versi stabil terbarunya 3.8.8. Prefect",
                    "cocok untuk tim kecil yang ingin skrip Python-nya punya retry dan",
                    "jadwal tanpa merawat Airflow.",
                    "",
                    "Luigi dibuat Spotify dan dirilis sebagai open source sekitar 2012.",
                    "Ia memodelkan pipeline sebagai kelas Task dengan method requires,",
                    "output, dan run, dan menganggap task selesai kalau berkas output-nya",
                    "sudah ada. Luigi masih dirawat (versi 3.8.1 rilis Mei 2026), tapi",
                    "jarang dipilih untuk proyek baru. Kamu lebih mungkin ketemu Luigi di",
                    "sistem lama.",
                    "",
                    "Apache NiFi berasal dari badan keamanan nasional Amerika Serikat,",
                    "yang menyumbangkannya ke Apache pada 2014. Di NiFi kamu nggak",
                    "menulis kode. Kamu menyusun prosesor di kanvas browser, misalnya",
                    "ambil berkas dari folder, ubah CSV ke JSON, lalu kirim ke Kafka, dan",
                    "menyambungkannya dengan panah. Tiap data yang lewat dicatat",
                    "asal-usulnya (data provenance), jadi satu record bisa dilacak dari",
                    "mana dan diubah apa saja. NiFi banyak dipakai di instansi besar dan",
                    "untuk mengumpulkan data perangkat IoT. Versi terbarunya 2.12.0.",
                ],
            },
            {
                "heading": "Flow Prefect",
                "code": """from prefect import flow, task


@task(retries=2, retry_delay_seconds=30)
def ambil_pesanan():
    return [50000, 75000, 20000]


@flow(log_prints=True)
def laporan_harian():
    total = sum(ambil_pesanan())
    print(f"omzet: {total}")


if __name__ == "__main__":
    laporan_harian()""",
            },
            {
                "heading": "Ingest dan reverse ETL",
                "body": [
                    "Menulis kode untuk menarik data dari Google Ads, Salesforce, atau",
                    "database PostgreSQL aplikasi kelihatannya gampang. Lalu kamu harus",
                    "mengurus paginasi, batas permintaan per menit, kolom yang tiba-tiba",
                    "ditambah, dan token yang kedaluwarsa. Alat ingest sudah menyediakan",
                    "konektor untuk ratusan sumber seperti itu.",
                    "  - Airbyte: open source dengan ratusan konektor. Platformnya",
                    "    berlisensi Elastic License 2.0, yang boleh dipakai gratis tapi",
                    "    nggak boleh dijual ulang sebagai layanan, dan sebagian",
                    "    konektornya berlisensi MIT. Bisa dipasang sendiri atau dipakai",
                    "    versi cloud-nya.",
                    "  - Fivetran: layanan terkelola berbayar. Kamu memilih sumber dan",
                    "    tujuan, Fivetran mengurus sisanya, termasuk kolom baru di sumber.",
                    "",
                    "Keduanya memakai sinkronisasi inkremental: yang disalin cuma baris",
                    "yang berubah sejak sinkronisasi terakhir. Perubahan dilacak lewat",
                    "kolom seperti updated_at, yang disebut cursor, atau lewat CDC",
                    "(change data capture), yaitu membaca log perubahan database.",
                    "",
                    "Reverse ETL berjalan ke arah sebaliknya. Gudang data sudah punya",
                    "skor pelanggan atau daftar pelanggan yang hampir berhenti",
                    "berlangganan, tapi tim penjualan bekerja di Salesforce dan tim iklan",
                    "di Google Ads. Hightouch dan Census menyinkronkan hasil query gudang",
                    "data ke aplikasi-aplikasi itu secara terjadwal. Segment, yang",
                    "awalnya alat pengumpul event pelanggan, juga menawarkan fitur",
                    "serupa. Semuanya layanan berbayar, jadi cukup kenali bentuknya dulu.",
                    "",
                    "Cara memilih secara kasar:",
                    "  - Baru mulai dan ingin yang paling banyak dipakai: Airflow. Di",
                    "    Python Developers Survey 2024, Airflow dipakai 15% responden",
                    "    yang mengolah data.",
                    "  - Pipeline berpusat pada tabel, sudah memakai dbt, dan ingin",
                    "    lineage terlihat: Dagster.",
                    "  - Tim kecil dengan skrip Python yang tinggal ditambahi retry:",
                    "    Prefect.",
                    "  - Menyalin data dari aplikasi SaaS ke gudang data: Airbyte kalau",
                    "    mau pasang sendiri, Fivetran kalau mau bayar supaya nggak repot.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Susunan yang umum di startup sekarang: Airbyte atau Fivetran",
                    "menyalin data aplikasi ke gudang data tiap jam, dbt mengubahnya jadi",
                    "tabel laporan, dan Airflow atau Dagster mengatur urutan keduanya.",
                    "Hasilnya dibaca alat BI, dan sebagian dikirim balik ke CRM lewat",
                    "reverse ETL.",
                    "",
                    "Kasus kecil: startup katering ingin data pesanan dari database",
                    "PostgreSQL aplikasinya dan data iklan dari Google Ads masuk ke satu",
                    "gudang data tiap pagi, lalu dihitung biaya iklan per pesanan. Tim",
                    "datanya cuma dua orang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pakai konektor siap pakai untuk dua sumber itu, Airbyte yang",
                    "     dipasang sendiri atau Fivetran kalau anggarannya ada, dengan",
                    "     sinkronisasi inkremental berbasis kolom updated_at.",
                    "  2. Tulis transformasinya sebagai model dbt: stg_pesanan dan",
                    "     stg_iklan, lalu mart biaya_per_pesanan dengan uji not_null di",
                    "     kolom tanggal.",
                    "  3. Atur urutannya di orkestrator: sinkronisasi selesai dulu, baru",
                    "     dbt build. Untuk tim dua orang, versi terkelola Prefect atau",
                    "     Dagster mengurangi server yang harus dirawat.",
                    "  4. Pasang peringatan kalau sinkronisasi pagi gagal, supaya tim",
                    "     tahu laporan hari itu masih memakai data kemarin.",
                ],
            },
        ],
    },
    {
        "title": "36. Apache Spark: Dari MapReduce ke DataFrame",
        "sections": [
            {
                "body": [
                    "Laptop biasa punya RAM 8 sampai 16 GB dan SSD beberapa ratus",
                    "gigabyte. Log klik toko online besar atau catatan transaksi bank bisa",
                    "berukuran terabyte, dan bertambah tiap hari. Data seperti itu nggak",
                    "muat di satu mesin. Kalaupun muat, membacanya dari awal sampai akhir",
                    "makan waktu berjam-jam.",
                    "",
                    "Ada dua jalan keluar. Pertama, beli mesin yang lebih besar. Cara ini",
                    "disebut scale up, dan cepat mentok di harga. Kedua, pecah datanya ke",
                    "banyak mesin biasa dan suruh semuanya bekerja bareng. Cara ini",
                    "disebut scale out, dan sekumpulan mesin yang bekerja bareng itu",
                    "disebut cluster. Hampir semua alat big data memilih jalan kedua.",
                    "",
                    "Masalah barunya: gimana menulis program yang jalan di seratus mesin",
                    "sekaligus, tanpa harus mengurus sendiri jaringan, mesin yang mati di",
                    "tengah jalan, dan pembagian datanya?",
                ],
            },
            {
                "heading": "MapReduce: pola tiga langkah",
                "body": [
                    "Pada 2004 Google menerbitkan makalah tentang MapReduce, pola yang",
                    "menjawab pertanyaan tadi. Proyek open source Apache Hadoop lalu",
                    "menirunya. Idenya, hampir semua pengolahan data besar bisa dipecah",
                    "jadi tiga langkah:",
                    "  1. Map: tiap mesin mengolah potongan datanya sendiri dan",
                    "     menghasilkan pasangan (kunci, nilai). Langkah ini nggak perlu",
                    "     ngobrol dengan mesin lain.",
                    "  2. Shuffle: pasangan dengan kunci yang sama dikirim lewat jaringan",
                    "     ke mesin yang sama. Ini satu-satunya langkah yang memindahkan",
                    "     data antarmesin.",
                    "  3. Reduce: tiap mesin meringkas semua nilai untuk tiap kunci yang",
                    "     diterimanya, misalnya menjumlahkannya.",
                    "",
                    "Program di bawah meniru ketiganya untuk menghitung omzet per kota",
                    "dari data yang tersebar di dua mesin.",
                ],
            },
            {
                "heading": "MapReduce versi mini",
                "code": """from collections import defaultdict

# data transaksi yang dipecah ke dua mesin
mesin = [
    ["Bandung,50000", "Medan,75000", "Bandung,20000"],
    ["Surabaya,120000", "Medan,30000", "Bandung,45000"],
]


def petakan(baris):
    kota, jumlah = baris.split(",")
    return (kota, int(jumlah))


def reducer_untuk(kunci, jumlah_reducer=2):
    # Hadoop memakai hash kunci; di sini jumlah kode huruf supaya tetap sama
    return sum(map(ord, kunci)) % jumlah_reducer


# 1. map: tiap mesin mengolah potongannya sendiri
hasil_map = [[petakan(b) for b in potongan] for potongan in mesin]
for i, pasangan in enumerate(hasil_map):
    print(f"map mesin {i}: {pasangan}")

# 2. shuffle: pasangan berkunci sama dikirim ke reducer yang sama
reducer = [defaultdict(list), defaultdict(list)]
for pasangan in hasil_map:
    for kota, jumlah in pasangan:
        reducer[reducer_untuk(kota)][kota].append(jumlah)
for i, kelompok in enumerate(reducer):
    for kota in sorted(kelompok):
        print(f"shuffle: {kota} -> reducer {i} {kelompok[kota]}")

# 3. reduce: tiap kunci diringkas jadi satu nilai
for i, kelompok in enumerate(reducer):
    for kota in sorted(kelompok):
        print(f"reduce {i}: {kota} = {sum(kelompok[kota])}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  map mesin 0: [('Bandung', 50000), ('Medan', 75000), ('Bandung', 20000)]",
                    "  map mesin 1: [('Surabaya', 120000), ('Medan', 30000), ('Bandung', 45000)]",
                    "  shuffle: Surabaya -> reducer 0 [120000]",
                    "  shuffle: Bandung -> reducer 1 [50000, 20000, 45000]",
                    "  shuffle: Medan -> reducer 1 [75000, 30000]",
                    "  reduce 0: Surabaya = 120000",
                    "  reduce 1: Bandung = 115000",
                    "  reduce 1: Medan = 105000",
                    "",
                    "Map jalan di tiap mesin tanpa menunggu mesin lain, jadi pekerjaannya",
                    "bisa dibagi rata ke seratus mesin kalau datanya dipecah seratus.",
                    "Shuffle memastikan semua angka Bandung sampai di reducer yang sama,",
                    "karena reducer cuma bisa menjumlahkan angka yang ada di tangannya.",
                    "Tujuannya dihitung dari kunci, jadi Bandung dari mesin mana pun",
                    "selalu mendarat di reducer 1.",
                    "",
                    "Ingat: shuffle adalah langkah yang paling mahal. Datanya dikirim",
                    "lewat jaringan dan biasanya ditulis ke disk dulu. Banyak trik",
                    "mempercepat pipeline big data intinya sama: kurangi data yang perlu",
                    "di-shuffle.",
                ],
            },
            {
                "heading": "Dari Hadoop ke Spark",
                "body": [
                    "Hadoop terdiri dari tiga bagian. HDFS menyimpan berkas besar yang",
                    "dipotong jadi blok (bawaannya 128 MB), dan tiap blok disalin ke tiga",
                    "mesin supaya data tetap aman kalau satu mesin rusak. MapReduce",
                    "menjalankan pola tadi. YARN membagi CPU dan memori cluster ke",
                    "program-program yang antre.",
                    "",
                    "Kelemahan MapReduce di Hadoop: hasil tiap langkah ditulis ke disk.",
                    "Pipeline yang butuh lima tahap MapReduce berarti lima kali menulis",
                    "dan membaca disk, padahal disk jauh lebih lambat dari RAM.",
                    "",
                    "Apache Spark lahir di laboratorium AMPLab, UC Berkeley, pada 2009 dan",
                    "jadi proyek utama Apache pada 2014. Spark menyimpan data antara di",
                    "memori sebisa mungkin. Spark juga melihat seluruh rangkaian langkahmu",
                    "sebelum mulai, lalu menyusun rencana eksekusi yang paling hemat.",
                    "Polanya masih map, shuffle, reduce, tapi kamu menulisnya sebagai",
                    "operasi tabel yang jauh lebih gampang dibaca.",
                ],
            },
            {
                "heading": "Hitungan yang sama di PySpark",
                "code": """from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[*]").appName("omzet").getOrCreate()

data = [("Bandung", 50000), ("Medan", 75000), ("Bandung", 20000),
        ("Surabaya", 120000), ("Medan", 30000), ("Bandung", 45000)]

# gaya lama: RDD dengan reduceByKey, mirip MapReduce
rdd = spark.sparkContext.parallelize(data)
print(sorted(rdd.reduceByKey(lambda a, b: a + b).collect()))

# gaya sekarang: DataFrame
df = spark.createDataFrame(data, ["kota", "jumlah"])
df.groupBy("kota").agg(F.sum("jumlah").alias("omzet")).orderBy("kota").show()

spark.stop()""",
            },
            {
                "body": [
                    "Hasilnya:",
                    "  [('Bandung', 115000), ('Medan', 105000), ('Surabaya', 120000)]",
                    "  +--------+------+",
                    "  |    kota| omzet|",
                    "  +--------+------+",
                    "  | Bandung|115000|",
                    "  |   Medan|105000|",
                    "  |Surabaya|120000|",
                    "  +--------+------+",
                    "",
                    "Ada dua gaya menulis untuk hitungan yang sama:",
                    "  - RDD (Resilient Distributed Dataset) adalah API lama Spark. Kamu",
                    "    menulis map dan reduceByKey sendiri, mirip MapReduce.",
                    "  - DataFrame adalah tabel dengan kolom bernama. Kamu bilang apa yang",
                    "    mau dihitung (groupBy lalu sum), dan pengoptimal Spark yang",
                    "    bernama Catalyst menentukan caranya. Untuk kode baru, pakai",
                    "    DataFrame atau Spark SQL.",
                    "",
                    "pip install pyspark sudah membawa Spark-nya sekalian, jadi kamu bisa",
                    "mencobanya di laptop tanpa cluster. local[*] artinya pakai semua inti",
                    "CPU laptop sebagai pengganti mesin-mesin cluster. Spark 4 butuh Java",
                    "17 atau 21.",
                ],
            },
            {
                "heading": "Status dan versi",
                "body": [
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Spark 4.2.0, rilis 14 Juli 2026. Cabang 4.1.x, 4.0.x, dan 3.5.x masih",
                    "menerima perbaikan. Spark 4 menyalakan mode ANSI SQL secara bawaan.",
                    "Akibatnya, CAST('abc' AS INT) sekarang menghasilkan error, padahal di",
                    "Spark 3 hasilnya NULL tanpa peringatan. Kalau memang ingin NULL,",
                    "pakai try_cast.",
                    "",
                    "Di Survei Stack Overflow 2024, Spark dipakai 4,4% responden. Angkanya",
                    "kecil karena survei itu mencakup semua jenis programmer. Di kalangan",
                    "Python, Python Developers Survey 2024 mencatat 40% responden yang",
                    "bekerja dengan big data memakai PySpark.",
                    "",
                    "Hadoop masih dirilis (versi 3.5.0, April 2026) dan masih jalan di",
                    "banyak bank dan perusahaan telekomunikasi. Untuk proyek baru, peran",
                    "HDFS sudah banyak digantikan object storage seperti Amazon S3, dan",
                    "peran MapReduce digantikan Spark.",
                    "",
                    "Jebakan: PySpark menjalankan Python di dua tempat, di driver dan di",
                    "worker. Kalau versinya beda, misalnya venv-mu Python 3.12 sementara",
                    "python3 bawaan Fedora versi 3.14, job gagal dengan",
                    "PYTHON_VERSION_MISMATCH. Atur variabel lingkungan PYSPARK_PYTHON ke",
                    "Python milik venv-mu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Spark jadi mesin di balik banyak layanan data. Databricks dibangun di",
                    "atasnya, AWS Glue menjalankan job ETL dengan Spark, dan Amazon EMR",
                    "serta Google Dataproc menyewakan cluster Spark siap pakai. Pemakaian",
                    "yang paling umum adalah pekerjaan batch malam hari, misalnya",
                    "merangkum miliaran baris log jadi tabel harian.",
                    "",
                    "Kasus kecil: skrip pandas yang merangkum log klik harian makin",
                    "lambat. Lognya sekarang 40 GB per hari dalam ratusan berkas Parquet,",
                    "dan laptop 16 GB kehabisan memori.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek dulu apakah perlu cluster. Untuk 40 GB, DuckDB atau Polars di",
                    "     satu mesin sering sudah cukup (lihat bab 7). Spark masuk akal",
                    "     kalau datanya terus tumbuh atau tim sudah punya cluster.",
                    "  2. Tulis ulang dengan DataFrame PySpark, mulai dari",
                    "     spark.read.parquet(\"log/tanggal=2026-10-18/\") supaya cuma satu",
                    "     hari yang dibaca.",
                    "  3. Ganti perulangan Python per baris dengan operasi kolom seperti",
                    "     groupBy dan agg, supaya pekerjaannya dibagi ke executor.",
                    "  4. Jalankan dulu dengan master local[*] di laptop untuk satu hari",
                    "     data, cocokkan hasilnya dengan skrip lama, baru kirim ke cluster",
                    "     lewat spark-submit.",
                ],
            },
        ],
    },
    {
        "title": "37. PySpark dalam Praktik",
        "sections": [
            {
                "body": [
                    "Sebagian besar masalah performa PySpark datang dari salah paham soal",
                    "cara Spark bekerja. Jadi sebelum menulis job yang lebih besar, kenali",
                    "dulu siapa mengerjakan apa.",
                    "",
                    "Program PySpark-mu jalan di driver. Driver membaca kodemu, menyusun",
                    "rencana, lalu memecah pekerjaannya jadi task-task kecil. Task dikirim",
                    "ke executor, yaitu proses di mesin-mesin worker yang mengolah data.",
                    "Mesinnya disediakan manajer cluster: pembagi sumber daya Hadoop di",
                    "cluster lama, Kubernetes di cluster modern, atau mode standalone",
                    "bawaan Spark.",
                    "",
                    "Data di Spark dibagi jadi partisi, yaitu potongan baris yang diolah",
                    "satu task. Kalau DataFrame punya 200 partisi dan cluster punya 50",
                    "inti CPU, task-nya dikerjakan dalam empat gelombang.",
                ],
            },
            {
                "heading": "Transformasi, aksi, dan rencana eksekusi",
                "code": "from pyspark.sql import SparkSession, functions as F\n\nspark = SparkSession.builder.master(\"local[*]\").appName(\"praktik\").getOrCreate()\n\npesanan = spark.createDataFrame(\n    [\n        (1, \"Bandung\", \"2026-10-01\", 50000),\n        (2, \"Medan\", \"2026-10-01\", 75000),\n        (3, \"Bandung\", \"2026-10-02\", 20000),\n        (4, \"Surabaya\", \"2026-10-02\", 120000),\n        (5, \"Medan\", \"2026-10-02\", 30000),\n    ],\n    [\"id\", \"kota\", \"tanggal\", \"jumlah\"],\n)\n\n# transformasi: cuma dicatat, belum ada yang dihitung\nbesar = pesanan.filter(F.col(\"jumlah\") >= 30000)\nper_kota = besar.groupBy(\"kota\").agg(F.sum(\"jumlah\").alias(\"omzet\"))\n\nper_kota.explain()               # lihat rencananya\nper_kota.orderBy(\"kota\").show()  # aksi: baru di sini Spark bekerja\n\n# hitungan yang sama dengan Spark SQL\npesanan.createOrReplaceTempView(\"pesanan\")\nspark.sql(\"\"\"\n    SELECT kota, SUM(jumlah) AS omzet\n    FROM pesanan WHERE jumlah >= 30000\n    GROUP BY kota ORDER BY kota\n\"\"\").show()",
            },
            {
                "body": [
                    "Hasil show() yang pertama:",
                    "  +--------+------+",
                    "  |    kota| omzet|",
                    "  +--------+------+",
                    "  | Bandung| 50000|",
                    "  |   Medan|105000|",
                    "  |Surabaya|120000|",
                    "  +--------+------+",
                    "",
                    "Pesanan 3 (20000) dibuang filter, jadi Bandung tinggal 50000. Query",
                    "Spark SQL di bawahnya menghasilkan tabel yang persis sama, karena",
                    "dua cara itu diterjemahkan ke rencana yang sama.",
                    "",
                    "Potongan rencana dari explain(), nomor kolom seperti kota#16 sudah",
                    "dibuang. Bacanya dari bawah ke atas:",
                    "  HashAggregate(keys=[kota], functions=[sum(jumlah)])",
                    "  +- Exchange hashpartitioning(kota, 200)",
                    "     +- HashAggregate(keys=[kota], functions=[partial_sum(jumlah)])",
                    "        +- Filter (jumlah >= 30000)",
                    "",
                    "Filter jalan duluan, lalu tiap partisi menjumlahkan sebagian",
                    "(partial_sum) sebelum data dikirim. Exchange adalah shuffle: baris",
                    "dipindah supaya kota yang sama berkumpul di partisi yang sama. Angka",
                    "200 datang dari setelan spark.sql.shuffle.partitions. Fitur Adaptive",
                    "Query Execution, yang menyala secara bawaan, bisa menggabungkan",
                    "partisi kecil sesudah shuffle supaya nggak ada 200 task untuk lima",
                    "baris data.",
                ],
            },
            {
                "heading": "Transformasi dan aksi",
                "body": [
                    "Operasi di Spark terbagi dua:",
                    "  - Transformasi menghasilkan DataFrame baru dan cuma dicatat:",
                    "    select, filter, withColumn, groupBy, join, orderBy.",
                    "  - Aksi meminta hasil, dan baru di sini Spark bekerja: show, count,",
                    "    collect, take, dan menulis berkas dengan write.",
                    "",
                    "Cara ini disebut evaluasi malas (lazy evaluation). Mirip menyusun",
                    "daftar belanja dulu, baru berangkat ke pasar sekali jalan. Karena",
                    "seluruh daftar sudah terlihat sebelum berangkat, Spark bisa mengatur",
                    "ulang urutannya. Misalnya filter dipindah sedekat mungkin ke",
                    "pembacaan berkas, supaya baris yang nggak perlu nggak pernah dibaca.",
                    "Program di bawah meniru idenya dengan Python biasa.",
                ],
            },
            {
                "heading": "Evaluasi malas versi mini",
                "code": "class DataMalas:\n    \"\"\"Mencatat langkah dulu, baru menghitung waktu collect() dipanggil.\"\"\"\n\n    def __init__(self, data, langkah=()):\n        self.data = data\n        self.langkah = list(langkah)\n\n    def filter(self, syarat):\n        print(\"  catat: filter\")\n        return DataMalas(self.data, self.langkah + [(\"filter\", syarat)])\n\n    def map(self, fungsi):\n        print(\"  catat: map\")\n        return DataMalas(self.data, self.langkah + [(\"map\", fungsi)])\n\n    def collect(self):\n        print(f\"  jalankan {len(self.langkah)} langkah sekaligus\")\n        hasil = []\n        for x in self.data:\n            for jenis, f in self.langkah:\n                if jenis == \"filter\" and not f(x):\n                    break\n                if jenis == \"map\":\n                    x = f(x)\n            else:\n                hasil.append(x)\n        return hasil\n\n\nprint(\"menyusun rencana:\")\nrencana = DataMalas([50000, 75000, 20000, 120000, 30000])\nrencana = rencana.filter(lambda j: j >= 30000).map(lambda j: j // 1000)\nprint(\"belum ada yang dihitung\")\nprint(\"aksi collect():\")\nprint(rencana.collect())",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  menyusun rencana:",
                    "    catat: filter",
                    "    catat: map",
                    "  belum ada yang dihitung",
                    "  aksi collect():",
                    "    jalankan 2 langkah sekaligus",
                    "  [50, 75, 120, 30]",
                    "",
                    "filter dan map cuma menambah catatan. Pekerjaannya baru dikerjakan",
                    "waktu collect() dipanggil, dan kedua langkah dijalankan dalam satu",
                    "putaran atas data. Spark melakukan hal yang sama dalam skala besar.",
                    "",
                    "Jebakan: collect() dan toPandas() menarik seluruh hasil ke driver.",
                    "Pada DataFrame besar, driver kehabisan memori dan job-nya mati. Pakai",
                    "show(), take(10), atau tulis hasilnya ke berkas.",
                ],
            },
            {
                "heading": "Membaca dan menulis berkas (laporan_harian.py)",
                "code": """from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("laporan-harian").getOrCreate()

pesanan = spark.read.option("header", True).csv("data/pesanan/*.csv")
harian = (
    pesanan.withColumn("jumlah", F.col("jumlah").cast("long"))
    .groupBy("tanggal", "kota")
    .agg(F.sum("jumlah").alias("omzet"), F.count("*").alias("transaksi"))
)
harian.write.mode("overwrite").partitionBy("tanggal").parquet("hasil/omzet_harian")

spark.stop()""",
            },
            {
                "body": [
                    "partitionBy(\"tanggal\") menulis satu folder per tanggal, misalnya",
                    "hasil/omzet_harian/tanggal=2026-10-01/. Query berikutnya yang",
                    "menyaring tanggal cuma membuka folder yang cocok. Ini disebut",
                    "partition pruning. Ini alasan data besar hampir selalu",
                    "dipartisi per tanggal.",
                    "",
                    "cast(\"long\") di mode ANSI langsung error kalau ada nilai seperti",
                    "\"Rp50.000\" di kolom jumlah. Itu bagus: data kotor ketahuan di sini,",
                    "nggak diam jadi NULL lalu menurunkan omzet tanpa ada yang sadar.",
                    "",
                    "Program PySpark dijalankan dengan spark-submit. Dengan master",
                    "local[4] ia jalan di laptop memakai empat inti. Dengan master yarn",
                    "atau k8s:// ia dikirim ke cluster, dan kodenya nggak perlu diubah.",
                ],
            },
            {
                "heading": "Menjalankan job",
                "bahasa": "terminal",
                "code": """pip install pyspark==4.2.0
export PYSPARK_PYTHON="$(which python)"
spark-submit --master "local[4]" laporan_harian.py
spark-submit --master yarn --deploy-mode cluster laporan_harian.py""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman Spark UI (bawaannya di port 4040 selama job jalan) dipakai",
                    "data engineer untuk mencari tahap yang lambat. Yang paling sering",
                    "ketemu adalah shuffle yang terlalu besar dan data skew. Data skew",
                    "artinya satu kunci punya jauh lebih banyak baris dari kunci lain.",
                    "Akibatnya satu task bekerja lama sementara yang lain menunggu.",
                    "",
                    "Kasus kecil: job omzet harian per kota selesai dalam 40 menit, dan",
                    "di Spark UI terlihat 199 task selesai dalam hitungan detik sementara",
                    "satu task jalan 38 menit. Ternyata kota \"Jakarta\" punya 70% dari",
                    "seluruh baris.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan dugaannya dengan menghitung baris per kunci:",
                    "       df.groupBy(\"kota\").count().orderBy(F.desc(\"count\")).show(5)",
                    "  2. Cek apakah Adaptive Query Execution menyala",
                    "     (spark.sql.adaptive.enabled). Di Spark 4 bawaannya menyala dan",
                    "     bisa memecah partisi yang miring waktu join.",
                    "  3. Kalau masih miring di groupBy, lakukan agregasi dua tahap: tambah",
                    "     kolom acak 0 sampai 9 ke kunci, jumlahkan per (kota, acak), lalu",
                    "     jumlahkan lagi per kota.",
                    "  4. Bandingkan durasi tahapnya di Spark UI sebelum dan sesudah, dan",
                    "     cocokkan total omzetnya supaya hasilnya tetap sama.",
                ],
            },
        ],
    },
    {
        "title": "38. Apache Kafka: Log, Topik, dan Offset",
        "sections": [
            {
                "body": [
                    "Waktu pembeli membayar pesanan, beberapa sistem perlu tahu: gudang",
                    "untuk menyiapkan barang, layanan email untuk mengirim struk, dan tim",
                    "data untuk dasbor penjualan. Kalau layanan pesanan memanggil",
                    "ketiganya satu per satu, setiap ada sistem baru yang ingin ikut tahu,",
                    "kode layanan pesanan harus diubah. Kalau satu sistem sedang mati,",
                    "pesannya hilang.",
                    "",
                    "Apache Kafka memecahkannya dengan cara lain. Layanan pesanan cukup",
                    "menulis satu event, yaitu catatan bahwa sesuatu terjadi (\"pesanan",
                    "#1 dibayar\"), ke Kafka. Sistem lain membaca event itu sendiri,",
                    "dengan kecepatannya masing-masing, kapan pun mereka siap. Kafka",
                    "dibuat di LinkedIn, dirilis sebagai open source pada 2011, lalu jadi",
                    "proyek Apache.",
                ],
            },
            {
                "heading": "Log, topik, partisi, dan offset",
                "body": [
                    "Inti Kafka adalah log: daftar yang cuma bisa ditambah di ujungnya.",
                    "Event lama nggak diubah dan nggak dihapus waktu dibaca. Istilah",
                    "lainnya:",
                    "  - Topik: log yang diberi nama, misalnya pesanan atau klik.",
                    "  - Partisi: satu topik dipecah jadi beberapa log supaya bisa ditulis",
                    "    dan dibaca paralel oleh banyak mesin.",
                    "  - Offset: nomor urut event di dalam satu partisi, mulai dari 0.",
                    "  - Broker: server Kafka. Partisi disebar ke beberapa broker dan",
                    "    disalin ke broker lain supaya tetap aman kalau satu broker mati.",
                    "  - Retensi: berapa lama event disimpan. Bawaannya tujuh hari. Sesudah",
                    "    itu event lama dihapus, sudah dibaca atau belum.",
                    "",
                    "Producer, yaitu program yang menulis event, boleh memberi kunci pada",
                    "tiap event. Event berkunci sama selalu masuk partisi yang sama. Di",
                    "program berikut, kuncinya nama pelanggan.",
                ],
            },
            {
                "heading": "Partisi berdasarkan kunci",
                "code": "import zlib\n\nJUMLAH_PARTISI = 3\ntopik = [[] for _ in range(JUMLAH_PARTISI)]  # satu log per partisi\n\n\ndef kirim(kunci, nilai):\n    \"\"\"Producer: pesan berkunci sama selalu masuk partisi yang sama.\"\"\"\n    # Kafka asli memakai hash murmur2; crc32 dipakai karena ada di stdlib\n    p = zlib.crc32(kunci.encode()) % JUMLAH_PARTISI\n    topik[p].append(nilai)\n    print(f\"{kunci:6}{nilai:14}-> partisi {p}, offset {len(topik[p]) - 1}\")\n\n\nkirim(\"ani\", \"dibuat\")\nkirim(\"dedi\", \"dibuat\")\nkirim(\"ani\", \"dibayar\")\nkirim(\"fajar\", \"dibuat\")\nkirim(\"ani\", \"dikirim\")\nkirim(\"dedi\", \"dibatalkan\")\n\nfor p, log in enumerate(topik):\n    print(f\"partisi {p}: {log}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ani   dibuat        -> partisi 1, offset 0",
                    "  dedi  dibuat        -> partisi 2, offset 0",
                    "  ani   dibayar       -> partisi 1, offset 1",
                    "  fajar dibuat        -> partisi 0, offset 0",
                    "  ani   dikirim       -> partisi 1, offset 2",
                    "  dedi  dibatalkan    -> partisi 2, offset 1",
                    "  partisi 0: ['dibuat']",
                    "  partisi 1: ['dibuat', 'dibayar', 'dikirim']",
                    "  partisi 2: ['dibuat', 'dibatalkan']",
                    "",
                    "Semua event ani ada di partisi 1 dengan urutan yang benar: dibuat,",
                    "dibayar, dikirim. Kafka cuma menjamin urutan di dalam satu partisi.",
                    "Event ani dan dedi bisa terbaca dalam urutan yang beda dari urutan",
                    "kirimnya, karena mereka ada di partisi berbeda. Jadi kalau urutan",
                    "penting untuk satu pesanan atau satu pelanggan, pakai ID-nya sebagai",
                    "kunci. Offset juga dihitung per partisi, makanya ani, dedi, dan",
                    "fajar sama-sama punya offset 0.",
                ],
            },
            {
                "heading": "Consumer dan consumer group",
                "body": [
                    "Consumer adalah program yang membaca event. Ia membaca mulai dari",
                    "sebuah offset, lalu menyimpan posisi bacanya. Menyimpan posisi ini",
                    "disebut commit. Kalau consumer mati lalu hidup lagi, ia melanjutkan",
                    "dari offset yang terakhir di-commit, nggak mengulang dari awal.",
                    "",
                    "Beberapa consumer bisa bergabung dalam satu consumer group. Partisi",
                    "topik dibagi di antara anggota grup, dan satu partisi cuma dibaca",
                    "satu anggota. Topik tiga partisi yang dibaca grup berisi tiga",
                    "consumer berarti tiap consumer mengurus satu partisi. Consumer",
                    "keempat cuma menganggur.",
                    "",
                    "Grup yang berbeda membaca secara terpisah, masing-masing dengan",
                    "offset sendiri. Grup gudang dan grup analitik sama-sama menerima",
                    "semua event pesanan, dan grup yang lambat nggak menahan grup yang",
                    "cepat.",
                ],
            },
            {
                "heading": "Producer dengan confluent-kafka",
                "code": """from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})


def laporan(err, msg):
    if err:
        print("gagal:", err)
    else:
        print(f"masuk partisi {msg.partition()}, offset {msg.offset()}")


producer.produce("pesanan", key="ani", value="dibayar", callback=laporan)
producer.flush()  # tunggu sampai broker mengonfirmasi""",
            },
            {
                "heading": "Consumer dalam grup gudang",
                "code": """from confluent_kafka import Consumer

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "gudang",
    "auto.offset.reset": "earliest",
})
consumer.subscribe(["pesanan"])
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("galat:", msg.error())
            continue
        print(msg.key().decode(), msg.value().decode(), msg.offset())
finally:
    consumer.close()""",
            },
            {
                "body": [
                    "Dua contoh ini butuh paket confluent-kafka dan broker Kafka yang",
                    "menyala. Yang perlu kamu perhatikan:",
                    "  - group.id menentukan grup. Jalankan program consumer yang sama dua",
                    "    kali, dan Kafka membagi partisi ke keduanya.",
                    "  - auto.offset.reset=earliest artinya grup baru mulai dari event",
                    "    paling lama yang masih disimpan. Tanpa itu, grup baru cuma",
                    "    membaca event yang datang sesudah ia bergabung.",
                    "  - Offset di-commit otomatis secara berkala. Kalau consumer mati",
                    "    sesudah memproses event tapi sebelum commit, event itu dibaca",
                    "    lagi sesudah ia hidup. Jadi pemrosesannya harus aman diulang,",
                    "    sama seperti task Airflow di bab sebelumnya.",
                ],
            },
            {
                "heading": "Kafka 4 tanpa ZooKeeper",
                "body": [
                    "Dulu Kafka butuh sistem terpisah bernama ZooKeeper untuk menyimpan",
                    "data cluster, misalnya broker mana yang hidup dan siapa pemimpin",
                    "tiap partisi. Tutorial lama selalu dimulai dengan menyalakan",
                    "ZooKeeper. Kafka 4.0, rilis Maret 2025, menghapus ZooKeeper",
                    "sepenuhnya dan cuma memakai mode KRaft, yaitu Kafka mengurus data",
                    "cluster-nya sendiri. Perintah yang memakai --zookeeper nggak jalan",
                    "lagi.",
                    "",
                    "Rilis terbaru di halaman unduhan resmi saat materi ini ditulis",
                    "(Oktober 2026) adalah 4.3.1, dan cabang 4.2.x serta 4.1.x masih",
                    "menerima perbaikan. Kafka butuh Java 17 ke atas. Di Survei Stack",
                    "Overflow 2024, Kafka dipakai 9,4% responden.",
                    "",
                    "Kalau nggak mau merawat broker sendiri, ada layanan terkelola seperti",
                    "Confluent Cloud dan Amazon MSK. Ada juga layanan serupa yang nggak",
                    "memakai protokol Kafka, seperti Amazon Kinesis dan Google Pub/Sub.",
                    "Redpanda adalah implementasi lain yang bisa dipakai klien Kafka.",
                    "",
                    "Untuk mencoba di laptop Fedora, unduh kafka_2.13-4.3.1.tgz dari situs",
                    "resmi, ekstrak, lalu jalankan perintah di bawah.",
                ],
            },
            {
                "heading": "Kafka di laptop",
                "bahasa": "terminal",
                "code": """# di folder hasil ekstrak kafka_2.13-4.3.1.tgz (butuh Java 17+)
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
bin/kafka-server-start.sh config/server.properties

# di terminal lain
bin/kafka-topics.sh --create --topic pesanan --partitions 3 --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic pesanan --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --topic pesanan --group gudang --from-beginning --bootstrap-server localhost:9092
bin/kafka-consumer-groups.sh --describe --group gudang --bootstrap-server localhost:9092""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kafka dipakai untuk aliran event yang terus mengalir. Contohnya klik",
                    "dan pencarian di aplikasi belanja, posisi pengemudi ojek online, dan",
                    "perubahan baris database yang disalin ke gudang data lewat change",
                    "data capture. Debezium adalah alat open source yang sering dipakai",
                    "untuk bagian terakhir itu.",
                    "",
                    "Kasus kecil: tim data ingin dasbor jumlah pesanan per menit, tanpa",
                    "mengubah layanan pesanan yang sudah mengirim event ke topik pesanan",
                    "untuk tim gudang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat consumer baru dengan group.id sendiri, misalnya dasbor,",
                    "     supaya offsetnya terpisah dari grup gudang dan nggak",
                    "     mengganggunya.",
                    "  2. Atur auto.offset.reset=latest kalau dasbor cuma butuh data mulai",
                    "     sekarang, atau earliest kalau ingin mengisi data beberapa hari",
                    "     ke belakang yang masih ada di retensi.",
                    "  3. Kelompokkan event per menit berdasarkan waktu kejadian yang",
                    "     tertulis di dalam event, karena event bisa telat tiba.",
                    "  4. Pantau lag grup dasbor, yaitu selisih offset terakhir di topik",
                    "     dengan offset yang sudah dibaca:",
                    "       kafka-consumer-groups.sh --describe --group dasbor \\",
                    "         --bootstrap-server localhost:9092",
                    "     Lag yang terus naik artinya consumer-nya kalah cepat dari",
                    "     producer.",
                ],
            },
        ],
    },
    {
        "title": "39. Peta Ekosistem Big Data dan Streaming",
        "sections": [
            {
                "body": [
                    "Ekosistem big data punya banyak nama yang muncul di lowongan kerja",
                    "dan di sistem lama. Kamu nggak perlu menguasai semuanya. Yang perlu:",
                    "tahu tiap alat itu untuk apa, dan apakah masih layak dipilih untuk",
                    "proyek baru.",
                ],
            },
            {
                "heading": "Peta singkat (Oktober 2026)",
                "bahasa": "teks",
                "code": """alat           peran                          versi terbaru      status
Hadoop HDFS    penyimpanan berkas cluster     3.5.0 (Apr 2026)   menurun, sistem lama
Hadoop YARN    pembagi sumber daya cluster    3.5.0              menurun, sistem lama
MapReduce      mesin batch generasi pertama   3.5.0              digantikan Spark
Apache Hive    SQL di atas Hadoop             4.2.1 (Agu 2026)   query menurun
Trino          mesin query SQL terdistribusi  484 (Okt 2026)     aktif
Apache Spark   batch dan streaming mikro      4.2.0 (Jul 2026)   aktif, standar
Apache Flink   streaming per event            2.3.0 (Jun 2026)   aktif
Apache Beam    model pipeline lintas mesin    2.77.0 (Okt 2026)  aktif
Apache Kafka   log event                      4.3.1 (Jun 2026)   aktif""",
            },
            {
                "heading": "Hadoop dan Hive",
                "body": [
                    "Hadoop masih jalan di cluster lama milik",
                    "bank dan operator telekomunikasi. Kalau kamu bekerja di tempat",
                    "seperti itu, kamu bakal ketemu HDFS dan pembagi sumber dayanya.",
                    "Untuk proyek baru,",
                    "jangan pilih Hadoop. Penyimpanannya sudah pindah ke object storage",
                    "seperti S3, dan pemrosesannya ke Spark atau mesin SQL.",
                    "",
                    "Apache Hive memberi SQL (namanya HiveQL) untuk berkas di HDFS.",
                    "Query-nya diterjemahkan jadi job MapReduce, belakangan jadi job Tez.",
                    "Sebagai mesin query, Hive menurun. Bagian yang tetap hidup adalah",
                    "Hive Metastore, tempat mencatat tabel apa saja yang ada, kolomnya",
                    "apa, dan berkasnya di mana. Spark, Trino, dan Iceberg masih bisa",
                    "memakai Hive Metastore sebagai pencatat tabel. Versi terbaru Hive",
                    "4.2.1 (Agustus 2026).",
                ],
            },
            {
                "heading": "Trino: satu SQL untuk banyak sumber",
                "body": [
                    "Trino adalah mesin query SQL terdistribusi. Trino nggak menyimpan",
                    "data sendiri. Ia membaca langsung dari tempat data berada, misalnya",
                    "data lake, PostgreSQL, MySQL, atau Kafka, dan bisa menggabungkan",
                    "semuanya dalam satu query. Tiap sumber dipasang sebagai catalog,",
                    "jadi nama tabel ditulis catalog.skema.tabel.",
                    "",
                    "Trino dulu bernama PrestoSQL, cabang dari Presto buatan Facebook.",
                    "Presto (PrestoDB) masih ada sebagai proyek terpisah. Rilis terbaru",
                    "Trino saat materi ini ditulis adalah 484 (15 Oktober 2026). Amazon",
                    "Athena dan Starburst dibangun di atas Trino.",
                ],
            },
            {
                "heading": "Query federasi di Trino",
                "bahasa": "teks",
                "code": """-- satu query, dua sumber: data lake (catalog hive) dan PostgreSQL aplikasi
SELECT p.nama, COUNT(*) AS klik
FROM hive.log.klik AS k
JOIN postgresql.public.pelanggan AS p ON p.id = k.id_pelanggan
WHERE k.tanggal = DATE '2026-10-18'
GROUP BY p.nama""",
            },
            {
                "heading": "Flink dan jendela waktu",
                "body": [
                    "Spark Structured Streaming secara bawaan mengolah aliran data dalam",
                    "potongan kecil berselang beberapa detik (micro-batch). Apache Flink",
                    "mengolah tiap event begitu datang, sambil menyimpan state, yaitu",
                    "ingatan seperti \"kartu ini sudah gagal bayar tiga kali dalam lima",
                    "menit\". Flink dipilih saat hasil harus keluar dalam hitungan",
                    "milidetik, misalnya deteksi penipuan kartu. Versi terbarunya 2.3.0",
                    "(Juni 2026), cabang LTS 1.20.x masih dirawat, dan ada API Python",
                    "bernama PyFlink.",
                    "",
                    "Konsep terpenting di streaming adalah beda waktu kejadian (event",
                    "time) dan waktu tiba (processing time). Event bisa telat tiba karena",
                    "jaringan putus. Program di bawah mengelompokkan transaksi ke jendela",
                    "satu menit berdasarkan waktu kejadiannya. Jendela yang nggak saling",
                    "tumpang tindih seperti ini disebut tumbling window.",
                ],
            },
            {
                "heading": "Jendela satu menit menurut waktu kejadian",
                "code": """# (waktu kejadian, jumlah) dalam urutan TIBA di server
aliran = [
    ("10:00:12", 50000),
    ("10:00:47", 20000),
    ("10:01:05", 75000),
    ("10:00:58", 30000),  # telat tiba: sinyal HP pembeli sempat putus
    ("10:01:40", 45000),
    ("10:02:03", 120000),
]

jendela = {}  # awal jendela satu menit -> (banyak transaksi, total)
for waktu, jumlah in aliran:
    awal = waktu[:5]  # "10:00:58" masuk jendela "10:00"
    n, total = jendela.get(awal, (0, 0))
    jendela[awal] = (n + 1, total + jumlah)

for awal in sorted(jendela):
    n, total = jendela[awal]
    print(f"jendela {awal}: {n} transaksi, total {total}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  jendela 10:00: 3 transaksi, total 100000",
                    "  jendela 10:01: 2 transaksi, total 120000",
                    "  jendela 10:02: 1 transaksi, total 120000",
                    "",
                    "Transaksi 10:00:58 tiba sesudah transaksi 10:01:05, tapi tetap masuk",
                    "jendela 10:00 karena yang dipakai waktu kejadiannya. Di sistem",
                    "sungguhan aliran nggak pernah selesai, jadi Flink harus memutuskan",
                    "kapan jendela 10:00 ditutup dan hasilnya dikirim. Keputusan itu",
                    "diatur watermark, yaitu batas waktu yang artinya \"event yang lebih",
                    "tua dari ini anggap sudah datang semua\".",
                ],
            },
            {
                "heading": "Beam, layanan terkelola, dan cara memilih",
                "body": [
                    "Apache Beam adalah model pemrograman. Kamu menulis pipeline sekali",
                    "dengan Java, Python, atau Go, lalu memilih mesin yang menjalankannya",
                    "(disebut runner), misalnya Google Cloud Dataflow, Flink, atau Spark.",
                    "Pipeline yang sama bisa dipakai untuk batch maupun streaming. Beam",
                    "paling sering dipakai bareng Dataflow di Google Cloud. Versi",
                    "terbarunya 2.77.0 (Oktober 2026).",
                    "",
                    "Untuk aliran event, cloud punya layanan sendiri yang nggak perlu",
                    "dirawat: Amazon Kinesis di AWS dan Google Pub/Sub di Google Cloud.",
                    "Konsepnya mirip Kafka (producer, consumer, retensi), tapi API-nya",
                    "beda.",
                    "",
                    "Cara memilih secara kasar:",
                    "  - Data batch harian berukuran besar: Spark.",
                    "  - Query SQL interaktif atas data lake tanpa memindahkan data:",
                    "    Trino.",
                    "  - Aliran event yang harus diolah dalam milidetik dengan state:",
                    "    Flink.",
                    "  - Pipeline di Google Cloud: Beam dengan Dataflow.",
                    "  - Menyalurkan event antarsistem: Kafka, atau Kinesis dan Pub/Sub",
                    "    kalau mau terkelola.",
                    "  - Hadoop, MapReduce, dan Hive sebagai mesin query: cuma kalau",
                    "    sistem lama sudah memakainya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi ojek dan pesan-antar memakai streaming untuk hal yang harus",
                    "cepat, seperti harga dinamis dan deteksi order palsu. Laporan",
                    "hariannya tetap dibuat dengan batch. Banyak bank yang punya cluster",
                    "Hadoop sejak 2010-an memindahkan pekerjaannya bertahap ke Spark dan",
                    "object storage, sambil tetap memakai Hive Metastore sebagai pencatat",
                    "tabel.",
                    "",
                    "Kasus kecil: tim analis ingin menggabungkan log klik di data lake",
                    "(berkas Parquet yang terdaftar di Hive Metastore) dengan tabel",
                    "pelanggan di PostgreSQL aplikasi untuk laporan mingguan. Mereka",
                    "nggak mau membangun pipeline penyalinan dulu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang Trino dengan dua catalog: hive untuk data lake dan",
                    "     postgresql untuk database aplikasi.",
                    "  2. Tulis satu query yang menggabungkan keduanya:",
                    "       SELECT p.kota, COUNT(*) AS klik",
                    "       FROM hive.log.klik AS k",
                    "       JOIN postgresql.public.pelanggan AS p",
                    "         ON p.id = k.id_pelanggan",
                    "       WHERE k.tanggal >= DATE '2026-10-12'",
                    "       GROUP BY p.kota",
                    "  3. Pastikan data lake dipartisi per tanggal, supaya filter tanggal",
                    "     cuma membaca berkas seminggu terakhir.",
                    "  4. Kalau query ini dipakai tiap hari dan makin berat, baru",
                    "     pertimbangkan menyalin tabel pelanggan ke data lake lewat",
                    "     pipeline.",
                ],
            },
        ],
    },
    {
        "title": "40. Format Tabel Terbuka: Iceberg, Delta Lake, Hudi",
        "sections": [
            {
                "body": [
                    "Data lake di bab 9 isinya folder raksasa berisi berkas",
                    "Parquet di object storage seperti Amazon S3. Murah dan bisa dibaca",
                    "banyak mesin, tapi ada empat masalah yang nggak dimiliki database:",
                    "  - Nggak ada transaksi. Pembaca yang membuka folder saat penulis",
                    "    sedang menulis bisa melihat setengah data baru.",
                    "  - Mengubah atau menghapus satu baris berarti menulis ulang berkas",
                    "    Parquet-nya sendiri, dan nggak ada yang mencatatnya.",
                    "  - Skema gampang kacau. Berkas lama punya lima kolom, berkas baru",
                    "    enam, dan pembaca harus menebak.",
                    "  - Nggak ada riwayat. Kalau job semalam merusak data, isi kemarin",
                    "    sudah hilang.",
                    "",
                    "Format tabel terbuka (open table format) menambah satu lapisan",
                    "metadata di atas berkas Parquet itu. Dengan metadata itu, folder",
                    "berkas bisa diperlakukan seperti tabel database: punya transaksi",
                    "ACID, skema yang bisa diubah dengan aman, dan time travel, yaitu",
                    "membaca isi tabel di masa lalu. Gabungan data lake dan kemampuan",
                    "seperti ini yang disebut lakehouse.",
                ],
            },
            {
                "heading": "Ide dasarnya: daftar berkas yang diberi nomor",
                "body": [
                    "Kuncinya satu: berkas data nggak pernah diubah. Menambah data",
                    "berarti menulis berkas baru. Menghapus baris berarti menulis ulang",
                    "berkas yang memuat baris itu jadi berkas baru tanpa baris tersebut.",
                    "",
                    "Yang berubah cuma daftar berkas mana yang membentuk tabel saat ini.",
                    "Satu versi daftar itu disebut snapshot. Tiap commit membuat snapshot",
                    "baru. Snapshot lama tetap ada, dan berkas yang dipakainya belum",
                    "dihapus, jadi kamu bisa membaca tabel persis seperti kemarin. Begitu",
                    "cara kerja time travel.",
                    "",
                    "Pembaca nggak pernah melihat setengah commit, karena pindah ke",
                    "snapshot baru cuma satu langkah: mengganti satu penunjuk.",
                ],
            },
            {
                "heading": "Isi folder dua tabel",
                "bahasa": "teks",
                "code": """s3://gudang/pesanan/                    (tabel Iceberg)
├── data/
│   ├── tanggal=2026-10-17/00001.parquet
│   └── tanggal=2026-10-18/00002.parquet
└── metadata/
    ├── v1.metadata.json               skema, partisi, daftar snapshot
    ├── v2.metadata.json               versi metadata sesudah commit kedua
    ├── snap-7613-1.avro               manifest list satu snapshot
    └── 4f1c-m0.avro                   manifest: daftar berkas data

s3://gudang/pelanggan/                  (tabel Delta Lake)
├── part-00000.parquet
├── part-00001.parquet
└── _delta_log/
    ├── 00000000000000000000.json      commit 0: tambah part-00000
    └── 00000000000000000001.json      commit 1: tambah part-00001""",
            },
            {
                "body": [
                    "Iceberg menyusun metadatanya bertingkat. Berkas metadata.json",
                    "mencatat skema, partisi, dan daftar snapshot. Tiap snapshot menunjuk",
                    "satu manifest list. Manifest list menunjuk beberapa manifest, dan",
                    "manifest berisi daftar berkas data beserta statistiknya, misalnya",
                    "nilai terkecil dan terbesar tiap kolom. Statistik itu membuat mesin",
                    "query bisa melewati berkas yang pasti nggak berisi data yang dicari.",
                    "",
                    "Delta Lake lebih sederhana. Tiap commit adalah satu berkas JSON",
                    "bernomor di folder _delta_log, berisi aksi seperti tambah berkas",
                    "ini dan buang berkas itu. Isi tabel didapat dengan memutar ulang",
                    "log dari awal, dan sesekali log itu diringkas jadi berkas",
                    "checkpoint supaya pembaca nggak perlu membaca ribuan JSON.",
                    "",
                    "Lalu siapa yang mencegah dua penulis menimpa commit satu sama lain?",
                    "Program di bawah meniru caranya.",
                ],
            },
            {
                "heading": "Commit dengan tukar penunjuk",
                "code": "class Katalog:\n    \"\"\"Menyimpan penunjuk ke snapshot terbaru tiap tabel.\"\"\"\n\n    def __init__(self):\n        self.penunjuk = {\"pesanan\": 1}\n\n    def tukar(self, tabel, harap, baru):\n        \"\"\"Ganti penunjuk hanya kalau isinya masih sama dengan `harap`.\"\"\"\n        if self.penunjuk[tabel] != harap:\n            return False\n        self.penunjuk[tabel] = baru\n        return True\n\n\nkatalog = Katalog()\nsnapshot = {1: [\"data-1.parquet\"]}\n\n# dua penulis membaca snapshot terbaru pada saat yang sama\ndasar_a = dasar_b = katalog.penunjuk[\"pesanan\"]\n\nsnapshot[2] = snapshot[dasar_a] + [\"data-2a.parquet\"]\nprint(\"A commit snapshot 2:\", katalog.tukar(\"pesanan\", dasar_a, 2))\n\nsnapshot[3] = snapshot[dasar_b] + [\"data-2b.parquet\"]\nprint(\"B commit snapshot 3:\", katalog.tukar(\"pesanan\", dasar_b, 3))\n\n# B ditolak, jadi ia mengulang dari snapshot terbaru\ndasar_b = katalog.penunjuk[\"pesanan\"]\nsnapshot[4] = snapshot[dasar_b] + [\"data-2b.parquet\"]\nprint(\"B ulang snapshot 4:\", katalog.tukar(\"pesanan\", dasar_b, 4))\n\nprint(\"isi tabel sekarang:\", \", \".join(snapshot[katalog.penunjuk[\"pesanan\"]]))\nprint(\"time travel ke snapshot 1:\", \", \".join(snapshot[1]))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  A commit snapshot 2: True",
                    "  B commit snapshot 3: False",
                    "  B ulang snapshot 4: True",
                    "  isi tabel sekarang: data-1.parquet, data-2a.parquet, data-2b.parquet",
                    "  time travel ke snapshot 1: data-1.parquet",
                    "",
                    "A dan B sama-sama berangkat dari snapshot 1. A menang duluan. Waktu",
                    "B mencoba commit, penunjuknya sudah bukan 1 lagi, jadi tukar()",
                    "menolak. B mengulang dari snapshot terbaru, dan hasil akhirnya",
                    "memuat berkas keduanya. Cara ini disebut optimistic concurrency:",
                    "semua boleh menulis, dan bentrokan baru diperiksa waktu commit.",
                    "",
                    "Di Iceberg, penunjuk itu dipegang catalog, misalnya Hive Metastore,",
                    "AWS Glue Data Catalog, atau catalog berbasis REST. Snapshot 3 yang",
                    "gagal tadi jadi berkas yatim yang nanti dibersihkan oleh perintah",
                    "pembersih.",
                ],
            },
            {
                "heading": "Tiga format, satu ide",
                "body": [
                    "  - Apache Iceberg lahir di Netflix lalu jadi proyek Apache. Ia",
                    "    format yang paling luas didukung: Spark, Trino, Flink,",
                    "    Snowflake, dan BigQuery bisa membaca tabel yang sama. Versi",
                    "    terbarunya 1.12.0 (30 September 2026). Spesifikasi tabel versi",
                    "    3 menambah tipe variant untuk data semi-terstruktur, tipe",
                    "    geometri, nilai bawaan kolom, deletion vector, dan pelacakan",
                    "    asal baris. Dukungan v3 mulai muncul di platform besar,",
                    "    misalnya AWS Glue 6.0.",
                    "  - Delta Lake dibuat Databricks dan sekarang dikelola Linux",
                    "    Foundation. Ia format bawaan di Databricks dan di OneLake milik",
                    "    Microsoft Fabric. Versi terbarunya 4.4.1 (5 Oktober 2026).",
                    "  - Apache Hudi lahir di Uber. Kekuatannya upsert dan penyerapan",
                    "    inkremental yang sering, misalnya menyalin perubahan database",
                    "    tiap beberapa menit. Ia punya dua jenis tabel: Copy-on-Write",
                    "    (tulis ulang berkas saat update) dan Merge-on-Read (catat",
                    "    perubahan dulu, gabung waktu dibaca). Versi terbarunya 1.2.1,",
                    "    dan pangsanya lebih kecil dari dua format lain.",
                    "",
                    "Karena idenya sama, ada juga alat penerjemah. Delta Lake punya",
                    "fitur UniForm yang ikut menulis metadata Iceberg, dan Apache XTable",
                    "menerjemahkan metadata antar ketiga format.",
                ],
            },
            {
                "heading": "Time travel dan perawatan di Spark SQL",
                "bahasa": "teks",
                "code": """-- Spark SQL dengan tabel Delta Lake
DESCRIBE HISTORY pelanggan;
SELECT * FROM pelanggan VERSION AS OF 3;
SELECT * FROM pelanggan TIMESTAMP AS OF '2026-10-18 00:00:00';

-- Spark SQL dengan tabel Iceberg (catalog bernama gudang)
SELECT * FROM gudang.toko.pesanan.snapshots;
SELECT * FROM gudang.toko.pesanan VERSION AS OF 7613;
SELECT * FROM gudang.toko.pesanan TIMESTAMP AS OF '2026-10-18 00:00:00';

-- merapikan berkas kecil dan membuang snapshot lama
OPTIMIZE pelanggan;
VACUUM pelanggan RETAIN 168 HOURS;
CALL gudang.system.expire_snapshots('toko.pesanan', TIMESTAMP '2026-10-11 00:00:00');""",
            },
            {
                "body": [
                    "Jebakan: time travel ada batasnya. Perintah pembersih seperti VACUUM",
                    "di Delta atau expire_snapshots di Iceberg menghapus berkas yang",
                    "cuma dipakai snapshot lama. Sesudah itu snapshot tersebut nggak bisa",
                    "dibaca lagi. Atur masa simpannya sesuai kebutuhan audit.",
                    "",
                    "Jebakan: banyak berkas kecil. Streaming yang commit tiap menit",
                    "menghasilkan ribuan berkas Parquet mungil, dan membaca ribuan",
                    "berkas kecil jauh lebih lambat dari membaca puluhan berkas besar.",
                    "Jalankan pemadatan secara berkala: perintah optimize di Delta, atau",
                    "prosedur rewrite_data_files di Iceberg.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lakehouse dengan Iceberg atau Delta dipakai perusahaan yang ingin",
                    "satu salinan data dibaca banyak mesin: Spark untuk ETL, Trino untuk",
                    "analis, dan Snowflake atau Databricks untuk dasbor. Layanan cloud",
                    "seperti AWS Glue, Databricks, Snowflake, dan BigQuery sudah bisa",
                    "membaca atau menulis format-format ini.",
                    "",
                    "Kasus kecil: job ETL semalam salah memfilter dan menghapus semua",
                    "pesanan Medan dari tabel Delta pesanan. Dasbor pagi menunjukkan",
                    "omzet Medan nol.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat riwayat tabelnya dan cari versi terakhir sebelum job",
                    "     semalam, misalnya versi 41:",
                    "       DESCRIBE HISTORY pesanan",
                    "  2. Cocokkan dulu isinya:",
                    "       SELECT COUNT(*) FROM pesanan VERSION AS OF 41",
                    "       WHERE kota = 'Medan'",
                    "  3. Kembalikan tabel ke versi itu. Pemulihan ini dicatat sebagai",
                    "     commit baru, jadi riwayatnya tetap utuh:",
                    "       RESTORE TABLE pesanan TO VERSION AS OF 41",
                    "  4. Betulkan filter di job ETL, lalu jalankan ulang untuk tanggal",
                    "     semalam. Jangan jalankan VACUUM dengan masa simpan pendek",
                    "     sebelum masalahnya beres.",
                ],
            },
        ],
    },
    {
        "title": "41. Databricks dan Snowflake",
        "sections": [
            {
                "body": [
                    "Kalau kamu membuka lowongan data engineer, dua nama ini muncul",
                    "terus. Keduanya platform data di cloud, keduanya bisa menjalankan",
                    "SQL atas data berukuran terabyte, tapi asal-usulnya beda.",
                    "Databricks berangkat dari data lake dan Spark. Snowflake berangkat",
                    "dari gudang data SQL. Bertahun-tahun keduanya saling mendekat, jadi",
                    "sekarang fiturnya banyak yang tumpang tindih.",
                ],
            },
            {
                "heading": "Databricks: lakehouse di atas Spark",
                "body": [
                    "Databricks didirikan pada 2013 oleh pembuat Spark. Isinya:",
                    "  - Notebook di browser untuk Python, SQL, Scala, dan R.",
                    "  - Spark terkelola, baik cluster yang kamu atur ukurannya maupun",
                    "    komputasi serverless.",
                    "  - Delta Lake sebagai format tabel bawaan.",
                    "  - Unity Catalog untuk mencatat tabel, hak akses, dan lineage di",
                    "    satu tempat.",
                    "  - Databricks SQL untuk analis yang cuma butuh SQL dan dasbor, plus",
                    "    MLflow dan layanan AI untuk tim machine learning.",
                    "",
                    "Saat materi ini ditulis, Databricks Runtime 19 memakai Spark 4.2.0,",
                    "dan versi LTS terbarunya Runtime 18. Biayanya dihitung dari",
                    "pemakaian komputasi, ditambah biaya mesin di akun cloud-mu kalau",
                    "tidak memakai serverless.",
                    "",
                    "Untuk belajar ada Databricks Free Edition, yang menggantikan",
                    "Community Edition lama yang dipensiunkan pada 2025. Free Edition",
                    "gratis, cuma serverless, dan kuotanya dibatasi. Semuanya jalan di",
                    "browser, jadi aman dipakai dari Fedora.",
                ],
            },
            {
                "heading": "Kode di notebook Databricks",
                "code": """from pyspark.sql import functions as F

# di notebook Databricks, variabel spark sudah tersedia
pesanan = spark.table("main.toko.pesanan")          # tabel Delta di Unity Catalog
harian = pesanan.groupBy("tanggal").agg(F.sum("jumlah").alias("omzet"))
harian.write.mode("overwrite").saveAsTable("main.toko.omzet_harian")""",
            },
            {
                "heading": "Snowflake: penyimpanan dan komputasi dipisah",
                "body": [
                    "Snowflake menyimpan datamu sekali, dalam bentuk kolumnar di",
                    "penyimpanan cloud yang dikelolanya. Komputasinya terpisah, berupa",
                    "virtual warehouse: sekelompok mesin yang bisa dinyalakan, dimatikan,",
                    "dan diubah ukurannya kapan saja. Ukurannya bertingkat dari X-Small,",
                    "Small, Medium, dan seterusnya. Tiap naik satu tingkat, jumlah mesin",
                    "dan biaya per jamnya dua kali lipat.",
                    "",
                    "Akibat pemisahan ini, tim keuangan dan tim pemasaran bisa memakai",
                    "warehouse masing-masing atas data yang sama tanpa saling",
                    "memperlambat. Biaya dihitung dalam kredit per detik selama",
                    "warehouse menyala, dengan minimal 60 detik tiap kali dinyalakan.",
                    "Warehouse X-Small memakai 1 kredit per jam.",
                    "",
                    "Fitur yang sering dipakai:",
                    "  - Time Travel untuk membaca isi tabel di masa lalu. Bawaannya 1",
                    "    hari.",
                    "  - Zero-copy clone untuk menyalin tabel tanpa menggandakan data.",
                    "  - Snowpark untuk menulis transformasi dengan Python.",
                    "  - Streamlit yang bisa dijalankan di dalam Snowflake.",
                    "",
                    "Snowflake dirilis bergulir tiap minggu. Saat materi ini ditulis,",
                    "rilis yang sedang digulirkan adalah 10.37.",
                ],
            },
            {
                "heading": "SQL Snowflake",
                "bahasa": "teks",
                "code": """-- komputasi: warehouse kecil yang tidur sendiri sesudah 60 detik menganggur
CREATE WAREHOUSE analis_wh
  WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE WAREHOUSE analis_wh;
SELECT kota, SUM(jumlah) AS omzet FROM toko.publik.pesanan GROUP BY kota;

-- Time Travel: isi tabel satu jam yang lalu
SELECT * FROM toko.publik.pesanan AT(OFFSET => -3600);

-- zero-copy clone: salinan untuk uji coba tanpa menggandakan data
CREATE TABLE toko.publik.pesanan_uji CLONE toko.publik.pesanan;""",
            },
            {
                "body": [
                    "AUTO_SUSPEND menentukan berapa detik warehouse boleh menganggur",
                    "sebelum tidur sendiri. Angka ini pengaruhnya besar ke tagihan.",
                    "Program di bawah menghitung kredit untuk empat query yang sama",
                    "dengan dua setelan.",
                ],
            },
            {
                "heading": "Menghitung kredit warehouse",
                "code": "# kapan query datang (detik sejak pagi) dan berapa detik jalannya\nquery = [(0, 40), (100, 30), (2000, 50), (2100, 20)]\nKREDIT_PER_JAM = 1  # ukuran X-Small\n\n\ndef detik_menyala(auto_suspend):\n    \"\"\"Total detik warehouse menyala, minimal 60 detik tiap kali bangun.\"\"\"\n    total = 0\n    awal = akhir = None\n    for mulai, lama in query:\n        if akhir is None or mulai > akhir:  # warehouse sedang tidur\n            if akhir is not None:\n                total += max(akhir - awal, 60)\n            awal = mulai\n        akhir = max(akhir or 0, mulai + lama + auto_suspend)\n    return total + max(akhir - awal, 60)\n\n\nfor jeda in (60, 600):\n    detik = detik_menyala(jeda)\n    kredit = detik / 3600 * KREDIT_PER_JAM\n    print(f\"auto_suspend {jeda:>3} detik: menyala {detik:>4} detik, \"\n          f\"{kredit:.3f} kredit\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  auto_suspend  60 detik: menyala  370 detik, 0.103 kredit",
                    "  auto_suspend 600 detik: menyala 1450 detik, 0.403 kredit",
                    "",
                    "Query-nya sama persis, dan total waktu jalannya cuma 140 detik.",
                    "Dengan jeda 10 menit, warehouse terus menyala menunggu query yang",
                    "nggak datang, dan biayanya hampir empat kali lipat.",
                    "",
                    "Ringkasnya, pilih Databricks kalau pekerjaanmu banyak Spark, Python,",
                    "dan machine learning di atas data lake. Pilih Snowflake kalau timmu",
                    "kebanyakan analis SQL yang ingin gudang data tanpa mengurus mesin.",
                    "Banyak perusahaan memakai keduanya. Snowflake punya masa coba",
                    "gratis 30 hari tanpa kartu kredit, cukup alamat email.",
                    "",
                    "Di Survei Stack Overflow 2025 kategori database, Snowflake dipakai",
                    "4,1% responden dan Databricks SQL 3,4%.",
                    "",
                    "Jebakan: warehouse atau cluster yang lupa dimatikan. Pasang",
                    "AUTO_SUSPEND di Snowflake dan auto-termination di cluster",
                    "Databricks sejak hari pertama, dan pasang batas anggaran di akun.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Startup yang datanya sudah di cloud sering memulai dengan Snowflake",
                    "atau BigQuery karena tinggal menulis SQL. Perusahaan yang banyak",
                    "melatih model atau mengolah data mentah berukuran besar cenderung",
                    "memakai Databricks. Keduanya sering jadi tujuan Fivetran atau",
                    "Airbyte, lalu ditransformasi dengan dbt.",
                    "",
                    "Kasus kecil: tagihan Snowflake tim analis bulan ini dua kali lipat,",
                    "padahal jumlah query hampir sama. Satu warehouse Medium ternyata",
                    "dipakai dasbor yang di-refresh tiap 5 menit, dengan AUTO_SUSPEND",
                    "600 detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek riwayat pemakaian kredit per warehouse di tampilan",
                    "     WAREHOUSE_METERING_HISTORY, dan temukan warehouse yang hampir",
                    "     nggak pernah tidur.",
                    "  2. Turunkan AUTO_SUSPEND jadi 60 detik:",
                    "       ALTER WAREHOUSE dasbor_wh SET AUTO_SUSPEND = 60;",
                    "  3. Coba ukuran lebih kecil. Query dasbor biasanya ringan, jadi",
                    "     X-Small atau Small sering cukup.",
                    "  4. Kurangi frekuensi refresh dasbor ke tiap jam kalau datanya",
                    "     memang cuma berubah tiap jam, lalu pasang resource monitor",
                    "     supaya warehouse berhenti kalau kuota kredit habis.",
                ],
            },
        ],
    },
    {
        "title": "42. Peta Platform Data Cloud",
        "sections": [
            {
                "body": [
                    "Selain Databricks dan Snowflake, tiap penyedia cloud punya layanan",
                    "data sendiri. Supaya nggak bingung, kelompokkan dulu:",
                    "  - Gudang data terkelola: Google BigQuery dan Amazon Redshift.",
                    "  - Platform terpadu dari ingest sampai laporan: Microsoft Fabric.",
                    "  - Database OLAP open source yang bisa dipasang sendiri:",
                    "    ClickHouse.",
                    "  - Layanan ETL: AWS Glue dan Azure Data Factory.",
                    "",
                    "Layanan terkelola seperti ini nggak punya nomor versi yang perlu",
                    "kamu ikuti. Yang perlu diikuti justru cara bayarnya, karena di",
                    "situlah kejutan biasanya muncul.",
                ],
            },
            {
                "heading": "Peta singkat (Oktober 2026)",
                "bahasa": "teks",
                "code": """layanan              jenis                     cara bayar             catatan
Google BigQuery      gudang data serverless    per data dipindai      sandbox gratis
                                               atau kapasitas
Amazon Redshift      gudang data AWS           per jam cluster atau   SQL turunan PostgreSQL
                                               Serverless
Snowflake            gudang data multi-cloud   kredit per detik       rilis mingguan
Databricks           lakehouse berbasis Spark  per pemakaian          ada Free Edition
Microsoft Fabric     platform analitik SaaS    kapasitas              Power BI di dalamnya
ClickHouse           database OLAP kolumnar    gratis (open source)   26.9, LTS 26.3
                                               atau Cloud
AWS Glue             ETL serverless (Spark)    per pemakaian          Glue 6.0 = Spark 4.1.1
Azure Data Factory   ETL dan orkestrasi visual per pemakaian          juga ada di Fabric""",
            },
            {
                "heading": "Google BigQuery",
                "body": [
                    "BigQuery adalah gudang data serverless: nggak ada server atau",
                    "warehouse yang perlu dinyalakan. Kamu tinggal menulis SQL. Dengan",
                    "harga on-demand, yang dibayar adalah banyaknya data yang dipindai",
                    "query, bukan lamanya query jalan. Di Survei Stack Overflow 2025",
                    "kategori database, BigQuery dipakai 6,5% responden, tertinggi di",
                    "antara gudang data cloud.",
                    "",
                    "Untuk belajar ada BigQuery sandbox. Tanpa kartu kredit, kamu dapat",
                    "10 GiB penyimpanan dan 1 TiB pemrosesan query per bulan, dengan",
                    "syarat semua tabel otomatis terhapus sesudah 60 hari. Data ekspor",
                    "Google Analytics 4 juga sering dianalisis di BigQuery.",
                    "",
                    "Karena BigQuery menyimpan data per kolom, yang dihitung cuma kolom",
                    "yang kamu sebut. Program di bawah menghitung data yang dipindai tiga",
                    "query atas tabel yang sama.",
                ],
            },
            {
                "heading": "Berapa data yang dipindai",
                "code": "# ukuran tiap kolom tabel pesanan untuk SATU hari data, dalam MB\nkolom = {\"id\": 8, \"tanggal\": 8, \"id_pelanggan\": 8, \"jumlah\": 8,\n         \"alamat\": 120, \"catatan\": 300}\nHARI_TERSIMPAN = 365\n\n\ndef dipindai_gb(pilih, hari=HARI_TERSIMPAN):\n    \"\"\"Data yang dibaca mesin kolumnar: cuma kolom terpilih x hari dibaca.\"\"\"\n    return sum(kolom[k] for k in pilih) * hari / 1024\n\n\nsemua = list(kolom)\nprint(f\"SELECT * ... LIMIT 10            : {dipindai_gb(semua):7.2f} GB\")\nprint(f\"SELECT tanggal, jumlah           : {dipindai_gb(['tanggal', 'jumlah']):7.2f} GB\")\nprint(f\"+ WHERE 7 hari terakhir (partisi): \"\n      f\"{dipindai_gb(['tanggal', 'jumlah'], hari=7):7.2f} GB\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  SELECT * ... LIMIT 10            :  161.11 GB",
                    "  SELECT tanggal, jumlah           :    5.70 GB",
                    "  + WHERE 7 hari terakhir (partisi):    0.11 GB",
                    "",
                    "Jebakan: LIMIT nggak mengurangi biaya. Dokumentasi BigQuery menulis",
                    "bahwa untuk tabel yang nggak di-cluster, LIMIT nggak mengubah",
                    "banyaknya data yang dibaca. SELECT * LIMIT 10 tetap memindai semua",
                    "kolom di semua hari. Yang menurunkan biaya adalah memilih kolom",
                    "seperlunya, memartisi tabel per tanggal, dan menyaring partisinya.",
                    "Sebelum menjalankan query besar, lakukan dry run untuk melihat",
                    "perkiraan datanya, atau pasang maximum bytes billed supaya query",
                    "yang kelewat besar gagal tanpa ditagih.",
                ],
            },
            {
                "heading": "Redshift dan Microsoft Fabric",
                "body": [
                    "Amazon Redshift adalah gudang data kolumnar milik AWS yang membagi",
                    "query ke banyak node. Dialek SQL-nya turunan PostgreSQL, jadi",
                    "banyak sintaksnya terasa akrab. Ada dua cara pakai: cluster yang",
                    "kamu pilih ukurannya, atau Redshift Serverless yang menyesuaikan",
                    "kapasitas sendiri. Redshift juga bisa membaca berkas di S3 langsung.",
                    "Pilihan wajar kalau perusahaannya sudah banyak memakai AWS.",
                    "",
                    "Microsoft Fabric adalah platform analitik SaaS yang menyatukan",
                    "banyak layanan Microsoft. Pusatnya OneLake, satu data lake untuk",
                    "seluruh organisasi yang menyimpan tabel dalam format Delta Lake. Di",
                    "atasnya ada Data Factory untuk ingest, Spark untuk data engineering,",
                    "gudang data SQL, analitik real-time, dan Power BI. Fabric dibayar",
                    "per kapasitas, yaitu paket daya komputasi yang dipakai bersama semua",
                    "layanan itu. Karena Power BI sekarang bagian dari Fabric, perusahaan",
                    "yang sudah memakai Power BI sering bertemu Fabric lebih dulu.",
                ],
            },
            {
                "heading": "ClickHouse, Glue, dan Data Factory",
                "body": [
                    "ClickHouse adalah database kolumnar open source (lisensi Apache 2.0)",
                    "yang ditulis dengan C++. Ia terkenal cepat untuk agregasi atas",
                    "miliaran baris, jadi sering dipakai untuk analitik log, event, dan",
                    "dasbor real-time. Versi stabil terbarunya 26.9, dengan cabang LTS",
                    "26.3. ClickHouse bisa dipasang sendiri di Linux atau dipakai versi",
                    "cloud-nya. Di Survei Stack Overflow 2025, ClickHouse dipakai 2,4%",
                    "responden.",
                    "",
                    "AWS Glue menjalankan job ETL berbasis Spark tanpa kamu mengurus",
                    "cluster, dan punya Glue Data Catalog untuk mencatat tabel di data",
                    "lake. Glue 6.0 memakai Spark 4.1.1 dan Python 3.13. Glue versi 0.9",
                    "sampai 2.0 sudah habis masa dukungannya sejak 1 April 2026, jadi",
                    "job lama yang masih memakainya harus dipindah.",
                    "",
                    "Azure Data Factory adalah layanan ETL dan orkestrasi milik Azure",
                    "dengan antarmuka visual dan ratusan konektor. Fiturnya juga hadir",
                    "di Microsoft Fabric dengan nama Data Factory. Padanannya di Google",
                    "Cloud adalah Dataflow, yang menjalankan pipeline Apache Beam.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pilihan platform di perusahaan jarang ditentukan fitur saja. Yang",
                    "lebih sering menentukan: cloud apa yang sudah dipakai. Perusahaan",
                    "di Google Cloud condong ke BigQuery, di AWS ke Redshift dan Glue,",
                    "dan di ekosistem Microsoft ke Fabric.",
                    "",
                    "Kasus kecil: analis magang menjalankan SELECT * FROM",
                    "events LIMIT 100 di BigQuery untuk melihat contoh data. Tabelnya 4",
                    "TiB, dan satu query itu menghabiskan jatah gratis bulanan tim.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Untuk melihat contoh baris, pakai tab Preview di konsol",
                    "     BigQuery, yang nggak menjalankan query.",
                    "  2. Biasakan menyebut kolom yang dibutuhkan saja dan selalu",
                    "     menyaring kolom partisi, misalnya:",
                    "       SELECT event_name, user_id FROM events",
                    "       WHERE tanggal = '2026-10-18'",
                    "  3. Lihat perkiraan data yang dipindai sebelum menekan Run. Konsol",
                    "     menampilkannya dari dry run.",
                    "  4. Pasang maximum bytes billed di level proyek atau query, supaya",
                    "     query yang kelewat besar gagal tanpa ditagih.",
                ],
            },
        ],
    },
    {
        "title": "43. Power BI: Model Data, DAX, dan Power Query",
        "sections": [
            {
                "body": [
                    "Power BI adalah alat BI (business intelligence) buatan Microsoft",
                    "untuk menyambungkan data, menyusun model, lalu membuat laporan dan",
                    "dasbor interaktif. Ia punya tiga bagian:",
                    "  - Power BI Desktop: aplikasi gratis untuk membuat laporan. Cuma",
                    "    ada untuk Windows.",
                    "  - Power BI service: situs web tempat laporan diterbitkan, dibagikan,",
                    "    dan di-refresh terjadwal. Berbagi laporan ke orang lain butuh",
                    "    lisensi Pro atau kapasitas Microsoft Fabric.",
                    "  - Aplikasi ponsel untuk membaca laporan.",
                    "",
                    "Power BI sekarang bagian dari Microsoft Fabric, dan dirilis tiap",
                    "bulan. Saat materi ini ditulis (Oktober 2026), pembaruan terbaru di",
                    "halaman resmi Microsoft adalah rilis Agustus 2026. Di versi baru,",
                    "yang dulu disebut dataset sekarang bernama semantic model, jadi",
                    "jangan bingung kalau tutorial lama memakai nama lama.",
                    "",
                    "Catatan untuk pengguna Fedora: Power BI Desktop nggak jalan di",
                    "Linux. Pilihan pertama, pakai Windows di mesin virtual. Pilihan",
                    "kedua, buat dan sunting laporan langsung di Power BI service lewat",
                    "browser. Pilihan ketiga, latih konsep yang sama dengan Metabase,",
                    "Superset, atau Looker Studio yang dibahas dua materi lagi.",
                ],
            },
            {
                "heading": "Alurnya: Power Query, model, measure, visual",
                "body": [
                    "Hampir semua laporan Power BI dibangun dengan urutan yang sama:",
                    "  1. Power Query mengambil data dari sumber (Excel, CSV, database,",
                    "     layanan web) dan membersihkannya.",
                    "  2. Hasilnya dimuat ke model: tabel-tabel yang dihubungkan dengan",
                    "     relationship, sebaiknya berbentuk star schema.",
                    "  3. Measure ditulis dengan DAX (Data Analysis Expressions) untuk",
                    "     menghitung angka seperti omzet dan margin.",
                    "  4. Visual seperti grafik, tabel matriks, kartu angka, dan slicer",
                    "     ditaruh di halaman laporan dan memakai measure itu.",
                ],
            },
            {
                "heading": "Power Query: membersihkan sebelum masuk model",
                "body": [
                    "Power Query adalah editor pembersihan data. Kamu mengeklik menu,",
                    "misalnya jadikan baris pertama header, ubah tipe kolom, buang baris",
                    "kosong, dan tiap klik dicatat sebagai satu langkah (Applied Steps).",
                    "Di balik layar, langkah-langkah itu ditulis dalam bahasa M. Kamu",
                    "jarang perlu menulis M dari nol, tapi bisa membacanya menolong saat",
                    "ada langkah yang error.",
                    "",
                    "Kalau sumbernya database, Power Query berusaha menerjemahkan",
                    "langkahmu jadi SQL dan menjalankannya di database. Fitur ini",
                    "disebut query folding, dan membuat pembersihan tabel besar jauh",
                    "lebih cepat.",
                ],
            },
            {
                "heading": "Langkah Power Query dalam bahasa M",
                "bahasa": "teks",
                "code": "let\n    Sumber = Csv.Document(File.Contents(\"C:\\data\\penjualan.csv\"),\n        [Delimiter = \",\", Encoding = 65001]),\n    Header = Table.PromoteHeaders(Sumber, [PromoteAllScalars = true]),\n    Tipe = Table.TransformColumnTypes(Header,\n        {{\"tanggal\", type date}, {\"jumlah\", Int64.Type}}),\n    Bersih = Table.SelectRows(Tipe, each [jumlah] <> null),\n    Rapi = Table.TransformColumns(Bersih, {{\"produk\", Text.Proper}})\nin\n    Rapi",
            },
            {
                "heading": "Model, measure, dan kolom terhitung",
                "body": [
                    "Model Power BI yang sehat berbentuk star schema seperti di bab 9:",
                    "tabel fakta Penjualan di tengah, dikelilingi tabel dimensi Produk,",
                    "Toko, dan Tanggal. Relationship-nya satu-ke-banyak, dan filter",
                    "mengalir dari dimensi ke fakta. Memilih kota Bandung di slicer Toko",
                    "berarti menyaring baris Penjualan milik toko Bandung. Tabel Tanggal",
                    "sebaiknya ditandai sebagai tabel tanggal, supaya fungsi waktu",
                    "seperti year-to-date bekerja benar.",
                    "",
                    "Ada dua cara menambah perhitungan:",
                    "  - Kolom terhitung (calculated column) dihitung sekali per baris",
                    "    waktu data di-refresh, lalu disimpan di model. Cocok untuk nilai",
                    "    yang melekat pada satu baris, misalnya jumlah dikali harga.",
                    "  - Measure dihitung saat visual memintanya, atas baris-baris yang",
                    "    lolos filter saat itu. Total, rata-rata, rasio, dan persen",
                    "    hampir selalu harus berupa measure.",
                ],
            },
            {
                "heading": "Contoh rumus DAX",
                "bahasa": "teks",
                "code": """-- kolom terhitung di tabel Penjualan: dihitung per baris, lalu disimpan
Nilai = Penjualan[Jumlah] * RELATED(Produk[Harga])

-- measure: dihitung saat sebuah visual memintanya, mengikuti filter
Total Omzet = SUM(Penjualan[Nilai])
Omzet Bandung = CALCULATE([Total Omzet], Toko[Kota] = "Bandung")
Persen dari Total = DIVIDE([Total Omzet], CALCULATE([Total Omzet], ALL(Toko)))
Margin = DIVIDE(SUM(Penjualan[Laba]), SUM(Penjualan[Nilai]))""",
            },
            {
                "body": [
                    "Kunci memahami measure adalah konteks filter, yaitu kumpulan filter",
                    "yang berlaku saat sebuah measure dihitung. Di tabel matriks dengan",
                    "baris kota dan kolom bulan, sel Bandung-Oktober menghitung [Total",
                    "Omzet] dengan filter kota Bandung dan bulan Oktober. Slicer dan",
                    "filter halaman ikut menambah filter. Fungsi calculate mengubah",
                    "konteks itu: menambah filter seperti di Omzet Bandung, atau",
                    "membuangnya dengan fungsi all seperti di Persen dari Total. Nama",
                    "fungsi DAX nggak peka huruf besar-kecil, tapi biasanya ditulis",
                    "kapital seperti di contoh.",
                    "",
                    "Kenapa rasio harus measure? Program di bawah membandingkan margin",
                    "yang dihitung sebagai kolom per baris lalu dirata-rata, dengan",
                    "margin sebagai measure.",
                ],
            },
            {
                "heading": "Kolom terhitung lawan measure",
                "code": """penjualan = [
    {"produk": "Kopi", "omzet": 100000, "laba": 40000},
    {"produk": "Teh", "omzet": 20000, "laba": 2000},
    {"produk": "Roti", "omzet": 80000, "laba": 20000},
]

# cara kolom terhitung: margin dihitung per baris, lalu dirata-rata
for b in penjualan:
    b["margin"] = b["laba"] / b["omzet"]
rata_kolom = sum(b["margin"] for b in penjualan) / len(penjualan)


# cara measure: saring dulu sesuai filter, jumlahkan, baru dibagi
def margin(produk=None):
    baris = [b for b in penjualan if produk in (None, b["produk"])]
    return sum(b["laba"] for b in baris) / sum(b["omzet"] for b in baris)


print(f"rata-rata kolom margin : {rata_kolom:.1%}")
print(f"measure margin, total  : {margin():.1%}")
print(f"measure margin, Kopi   : {margin('Kopi'):.1%}")
print(f"measure margin, Teh    : {margin('Teh'):.1%}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  rata-rata kolom margin : 25.0%",
                    "  measure margin, total  : 31.0%",
                    "  measure margin, Kopi   : 40.0%",
                    "  measure margin, Teh    : 10.0%",
                    "",
                    "Rata-rata margin per baris memberi 25%, karena Teh yang omzetnya",
                    "kecil diberi bobot sama dengan Kopi. Margin sungguhan toko ini 31%:",
                    "laba 62.000 dibagi omzet 200.000. Measure selalu menjumlahkan dulu",
                    "di bawah filter yang berlaku, baru membagi, jadi angkanya benar",
                    "untuk total maupun untuk tiap produk.",
                    "",
                    "Jebakan: terlalu banyak kolom terhitung. Tiap kolom disimpan untuk",
                    "semua baris, jadi model membengkak dan refresh melambat. Jebakan",
                    "lain: relationship dua arah yang dinyalakan di mana-mana. Filternya",
                    "jadi berputar ke tabel yang nggak terduga, dan angkanya sulit",
                    "dijelaskan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Power BI dipakai untuk dasbor penjualan, laporan keuangan bulanan,",
                    "dan laporan operasional yang datanya masih dari Excel. Lowongan data",
                    "analyst dan BI analyst di Indonesia sering menyebut Power BI atau",
                    "Tableau, dan roadmap peran Data Analyst di roadmap.sh mencantumkan",
                    "keduanya.",
                    "",
                    "Kasus kecil: manajer minta persen kontribusi omzet tiap cabang",
                    "terhadap total nasional. Kartu persen di laporan selalu menunjukkan",
                    "100% untuk cabang yang dipilih di slicer.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali penyebabnya. Pembilang dan penyebut sama-sama dihitung di",
                    "     bawah filter cabang dari slicer, jadi hasilnya pasti 100%.",
                    "  2. Buat penyebut yang membuang filter cabang:",
                    "       Omzet Nasional = CALCULATE([Total Omzet], ALL(Toko[Cabang]))",
                    "  3. Tulis measure persennya dengan fungsi pembagi yang nggak error",
                    "     kalau penyebutnya nol:",
                    "       Kontribusi = DIVIDE([Total Omzet], [Omzet Nasional])",
                    "  4. Uji di tabel matriks berisi semua cabang. Jumlah kolom",
                    "     Kontribusi harus 100%, dan memilih satu cabang di slicer nggak",
                    "     boleh mengubah persennya.",
                ],
            },
        ],
    },
    {
        "title": "44. Merancang Dasbor yang Dibaca Orang",
        "sections": [
            {
                "body": [
                    "Banyak dasbor dibuat dengan semangat lalu nggak pernah dibuka lagi",
                    "sesudah minggu kedua. Penyebabnya hampir selalu sama: dasbor itu",
                    "menampilkan semua data yang ada, tanpa menjawab pertanyaan siapa",
                    "pun. Pembacanya harus menebak sendiri angka mana yang penting.",
                    "",
                    "Pegangan paling berguna: satu dasbor, satu pertanyaan utama, untuk",
                    "satu kelompok pembaca. Dasbor direksi dan dasbor kepala gudang",
                    "boleh memakai data yang sama, tapi pertanyaannya beda, jadi",
                    "isinya juga beda.",
                ],
            },
            {
                "heading": "Mulai dari pertanyaan",
                "body": [
                    "Sebelum membuka Power BI, tulis dulu tiga hal:",
                    "  - Siapa pembacanya, dan seberapa sering ia membuka dasbor ini.",
                    "  - Keputusan apa yang ingin dibantu. Contohnya cabang mana yang",
                    "    perlu dikunjungi minggu ini.",
                    "  - Pertanyaan utamanya dalam satu kalimat. Contohnya: cabang mana",
                    "    yang omzetnya turun minggu ini, dan dari produk apa.",
                    "",
                    "Kalau sebuah grafik nggak membantu menjawab pertanyaan itu, ia",
                    "nggak masuk halaman utama. Taruh di halaman detail, atau buang.",
                ],
            },
            {
                "heading": "Memilih KPI",
                "body": [
                    "KPI (key performance indicator) adalah angka yang mengukur kemajuan",
                    "menuju tujuan. Angka yang layak jadi KPI punya empat ciri:",
                    "  - Terhubung ke keputusan. Jumlah pengunjung situs nggak berguna",
                    "    untuk kepala gudang.",
                    "  - Definisinya jelas dan tertulis. Omzet kotor atau bersih?",
                    "    Pesanan yang dibatalkan dihitung atau nggak?",
                    "  - Punya pembanding: target, periode lalu, atau rata-rata. Angka",
                    "    182 juta tanpa pembanding nggak bisa dibilang baik atau buruk.",
                    "  - Jumlahnya sedikit. Tiga sampai lima KPI di bagian atas lebih",
                    "    gampang diingat daripada dua puluh.",
                    "",
                    "Bedakan juga KPI yang menunjukkan hasil (omzet bulan lalu) dengan",
                    "KPI yang memberi tanda lebih awal (jumlah keranjang yang",
                    "ditinggalkan minggu ini). Yang kedua memberi waktu untuk bertindak.",
                ],
            },
            {
                "heading": "Kartu KPI dengan pembanding",
                "code": """minggu_ini = {"omzet": 182_500_000, "transaksi": 1460, "pelanggan baru": 210}
minggu_lalu = {"omzet": 175_000_000, "transaksi": 1520, "pelanggan baru": 180}
target = {"omzet": 190_000_000, "transaksi": 1500, "pelanggan baru": 200}


def rupiah(n):
    return f"{n:,}".replace(",", ".")


for nama, kini in minggu_ini.items():
    ubah = (kini - minggu_lalu[nama]) / minggu_lalu[nama]
    arah = "naik " if ubah >= 0 else "turun"
    capai = kini / target[nama]
    print(f"{nama:15}{rupiah(kini):>12}  {arah} {abs(ubah):5.1%}  "
          f"target {capai:6.1%}")

keranjang = minggu_ini["omzet"] // minggu_ini["transaksi"]
print(f"{'rata keranjang':15}{rupiah(keranjang):>12}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  omzet           182.500.000  naik   4.3%  target  96.1%",
                    "  transaksi             1.460  turun  3.9%  target  97.3%",
                    "  pelanggan baru          210  naik  16.7%  target 105.0%",
                    "  rata keranjang      125.000",
                    "",
                    "Tiap angka langsung ditemani arah perubahan dan capaian target.",
                    "Pembaca bisa menyimpulkan dalam beberapa detik: omzet naik walaupun",
                    "transaksi turun, karena tiap transaksi makin besar. Kesimpulan",
                    "seperti ini cocok jadi judul halaman, misalnya \"Omzet naik 4,3%,",
                    "didorong keranjang yang lebih besar\". Judul seperti itu jauh lebih",
                    "berguna daripada \"Penjualan\".",
                ],
            },
            {
                "heading": "Visual yang cocok untuk tiap pertanyaan",
                "bahasa": "teks",
                "code": """pertanyaan                          visual yang cocok
naik atau turun dari waktu ke waktu   grafik garis
mana yang paling besar               batang horizontal, diurutkan
satu angka penting                   kartu angka + pembanding
bagian dari keseluruhan              batang bertumpuk; pai cuma kalau <= 3 bagian
sebaran nilai                        histogram
hubungan dua angka                   diagram sebar
beda antarlokasi                     peta, kalau lokasinya memang penting""",
            },
            {
                "heading": "Tata letak dan grafik yang jujur",
                "body": [
                    "Orang membaca layar dari kiri atas. Taruh kartu KPI di baris paling",
                    "atas, tren di bawahnya, lalu rincian per cabang atau per produk.",
                    "Pakai satu warna netral untuk semua data dan satu warna sorotan",
                    "untuk hal yang perlu dilihat. Merah dan hijau sebaiknya punya",
                    "arti yang sama di seluruh dasbor.",
                    "",
                    "Grafik yang menyesatkan sudah dibahas di bab 5. Yang paling sering",
                    "muncul di dasbor:",
                    "  - Sumbu batang yang nggak mulai dari nol, sehingga selisih 2%",
                    "    terlihat seperti dua kali lipat.",
                    "  - Dua sumbu Y di satu grafik yang skalanya dipilih sesukanya.",
                    "  - Pai tiga dimensi atau pai dengan belasan irisan.",
                    "  - Rentang waktu yang beda antarvisual di halaman yang sama.",
                    "",
                    "Di Power BI ada beberapa alat yang membantu:",
                    "  - Drill-through untuk pindah ke halaman detail dari satu titik",
                    "    data.",
                    "  - Tooltip halaman untuk rincian saat kursor diarahkan.",
                    "  - Row-level security supaya kepala cabang cuma melihat data",
                    "    cabangnya.",
                    "  - Performance Analyzer untuk menemukan visual yang membuat halaman",
                    "    lambat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dasbor yang tetap dibuka orang biasanya sederhana: beberapa kartu",
                    "angka dengan pembanding, satu atau dua grafik tren, dan tabel",
                    "rincian. Peran BI analyst di roadmap.sh menaruh storytelling dan",
                    "desain dasbor sejajar dengan SQL dan pemodelan data, karena angka",
                    "yang benar tetap sia-sia kalau nggak terbaca.",
                    "",
                    "Kasus kecil: kepala area mengeluh dasbor penjualan berisi 14 grafik",
                    "di satu halaman, dan ia tetap harus menelepon tiap cabang untuk",
                    "tahu cabang mana yang bermasalah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Wawancarai kepala area lima menit. Pertanyaannya ternyata",
                    "     cuma satu: cabang mana yang di bawah target minggu ini, dan",
                    "     kenapa.",
                    "  2. Pilih tiga KPI: omzet terhadap target, jumlah transaksi, dan",
                    "     rata-rata keranjang, masing-masing dengan pembanding minggu",
                    "     lalu.",
                    "  3. Susun ulang halaman utama: kartu KPI di atas, batang horizontal",
                    "     capaian target per cabang yang diurutkan dari terendah, dan",
                    "     garis tren mingguan. Sebelas grafik lain pindah ke halaman",
                    "     detail yang bisa dicapai lewat drill-through.",
                    "  4. Beri judul halaman berupa kesimpulan yang diperbarui tiap",
                    "     minggu, lalu cek dua minggu kemudian apakah dasbornya masih",
                    "     dibuka.",
                ],
            },
        ],
    },
    {
        "title": "45. Peta Alat BI: Tableau, Looker, Metabase, Superset",
        "sections": [
            {
                "body": [
                    "Power BI bukan satu-satunya alat BI. Di tiap kantor kamu bisa",
                    "bertemu alat yang berbeda, dan konsepnya sama: sambungkan data,",
                    "definisikan metrik, buat visual, bagikan. Yang membedakan adalah",
                    "biaya, lisensi, apakah jalan di Linux, dan seberapa kuat lapisan",
                    "semantiknya.",
                    "",
                    "Alat BI nggak disurvei Stack Overflow maupun JetBrains, jadi nggak",
                    "ada angka popularitas yang bisa dipercaya untuk membandingkannya.",
                    "Petunjuk yang lebih jujur: roadmap.sh untuk peran Data Analyst dan",
                    "BI Analyst menyebut Power BI dan Tableau, ditambah Looker dan Qlik",
                    "untuk BI Analyst.",
                ],
            },
            {
                "heading": "Peta singkat (Oktober 2026)",
                "bahasa": "teks",
                "code": """alat              lisensi / biaya                 jalan di Linux?           kekuatan
Power BI          Desktop gratis, berbagi bayar   Desktop nggak; web ya     DAX, ekosistem Microsoft
Tableau           berbayar; Tableau Public gratis Desktop nggak             eksplorasi visual
Looker Studio     gratis (ada versi Pro)          ya, di browser            Google Sheets, GA4, BigQuery
Looker            berbayar (Google Cloud)         ya, di browser            lapisan semantik LookML
Metabase          AGPL-3.0 + edisi berbayar       ya, pasang sendiri        mudah untuk non-SQL
Apache Superset   Apache 2.0                      ya, pasang sendiri        SQL Lab, banyak jenis grafik
Qlik Sense        berbayar                        ya, di browser            mesin asosiatif
Grafana           AGPL-3.0                        ya                        metrik dan deret waktu
Redash            BSD-2-Clause                    ya                        dasbor SQL ringan, menurun
Evidence          MIT                             ya                        laporan sebagai kode""",
            },
            {
                "heading": "Tableau",
                "body": [
                    "Tableau dimiliki Salesforce sejak 2019. Kekuatannya eksplorasi",
                    "visual: kamu menyeret kolom ke baris dan kolom, dan Tableau memilih",
                    "grafik yang masuk akal. Tableau Desktop ada untuk Windows dan macOS,",
                    "nggak untuk Linux. Laporan dibagikan lewat Tableau Cloud atau",
                    "Tableau Server. Rilisnya dinamai tahun dan nomor urut, misalnya",
                    "2026.2.",
                    "",
                    "Tableau Public gratis dan sering dipakai untuk portofolio. Ingat:",
                    "semua yang disimpan di Tableau Public bisa dilihat siapa saja,",
                    "jadi jangan pernah memakai data kantor di sana.",
                ],
            },
            {
                "heading": "Looker Studio, Looker, dan lapisan semantik",
                "body": [
                    "Dua produk Google ini namanya mirip tapi beda jauh. Looker Studio,",
                    "dulu bernama Google Data Studio, adalah pembuat dasbor gratis di",
                    "browser yang gampang disambungkan ke Google Sheets, Google Analytics",
                    "4, dan BigQuery. Ia pilihan paling ramah untuk pengguna Fedora,",
                    "karena cukup browser.",
                    "",
                    "Looker adalah platform BI perusahaan di Google Cloud. Cirinya adalah",
                    "lapisan semantik bernama LookML: definisi dimensi dan metrik ditulis",
                    "sekali sebagai kode, lalu semua laporan memakainya. Kalau definisi",
                    "omzet berubah, cukup diubah di satu tempat. Rilis Looker terbaru",
                    "saat materi ini ditulis adalah 26.20, yang penggelarannya selesai",
                    "paling lambat 25 Oktober 2026.",
                ],
            },
            {
                "heading": "Satu view LookML",
                "bahasa": "teks",
                "code": """view: pesanan {
  sql_table_name: analitik.fakta_pesanan ;;

  dimension: kota {
    type: string
    sql: ${TABLE}.kota ;;
  }

  measure: omzet {
    type: sum
    sql: ${TABLE}.jumlah ;;
    value_format_name: decimal_0
  }

  measure: transaksi {
    type: count
  }
}""",
            },
            {
                "body": [
                    "Lapisan semantik menyelesaikan masalah klasik: tim keuangan dan tim",
                    "pemasaran menghitung omzet dengan rumus berbeda, lalu rapat habis",
                    "untuk memperdebatkan angka mana yang benar. Program di bawah meniru",
                    "idenya. Tiap metrik didefinisikan sekali di satu dict, dan query",
                    "untuk dimensi apa pun dirakit dari definisi itu.",
                ],
            },
            {
                "heading": "Lapisan semantik versi mini",
                "code": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.executescript(\"\"\"\nCREATE TABLE fakta_pesanan (kota TEXT, kanal TEXT, jumlah INTEGER);\nINSERT INTO fakta_pesanan VALUES\n  ('Bandung', 'web', 50000), ('Bandung', 'aplikasi', 20000),\n  ('Medan', 'aplikasi', 75000), ('Medan', 'web', 30000),\n  ('Surabaya', 'aplikasi', 120000);\n\"\"\")\n\n# lapisan semantik: tiap metrik didefinisikan SEKALI\nMETRIK = {\n    \"omzet\": \"SUM(jumlah)\",\n    \"transaksi\": \"COUNT(*)\",\n    \"keranjang\": \"SUM(jumlah) / COUNT(*)\",\n}\n\n\ndef tanya(metrik, dimensi):\n    kolom = \", \".join(f\"{METRIK[m]} AS {m}\" for m in metrik)\n    sql = (f\"SELECT {dimensi}, {kolom} FROM fakta_pesanan \"\n           f\"GROUP BY {dimensi} ORDER BY {dimensi}\")\n    print(f\"SELECT {dimensi}, {kolom}\")\n    print(f\"  ... GROUP BY {dimensi}\")\n    for baris in db.execute(sql):\n        print(\"  \", baris)\n\n\ntanya([\"omzet\", \"transaksi\"], \"kota\")\ntanya([\"omzet\", \"keranjang\"], \"kanal\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  SELECT kota, SUM(jumlah) AS omzet, COUNT(*) AS transaksi",
                    "    ... GROUP BY kota",
                    "     ('Bandung', 70000, 2)",
                    "     ('Medan', 105000, 2)",
                    "     ('Surabaya', 120000, 1)",
                    "  SELECT kanal, SUM(jumlah) AS omzet, SUM(jumlah) / COUNT(*) AS keranjang",
                    "    ... GROUP BY kanal",
                    "     ('aplikasi', 215000, 71666)",
                    "     ('web', 80000, 40000)",
                    "",
                    "Laporan per kota dan per kanal memakai rumus omzet yang sama persis.",
                    "LookML, metrik di dbt, dan measure di Power BI semuanya memakai ide",
                    "ini.",
                ],
            },
            {
                "heading": "Metabase, Superset, Qlik, dan yang lain",
                "body": [
                    "Metabase dan Apache Superset adalah dua alat BI open source yang",
                    "bisa kamu pasang sendiri di Linux:",
                    "  - Metabase paling gampang dipakai. Orang yang nggak bisa SQL tetap",
                    "    bisa bertanya lewat pembuat pertanyaan visual. Edisi open",
                    "    source-nya berlisensi AGPL-3.0, dan ada edisi Pro serta",
                    "    Enterprise yang berbayar. Versi terbarunya v0.64.1 (Oktober",
                    "    2026).",
                    "  - Superset berasal dari Airbnb, dibuat oleh orang yang juga",
                    "    membuat Airflow, lalu jadi proyek Apache berlisensi Apache 2.0.",
                    "    Ia kuat untuk pengguna SQL (ada SQL Lab) dan punya banyak jenis",
                    "    grafik, tapi lebih berat dipasang. Versi stabilnya 6.1.0, dan",
                    "    7.0 masih release candidate.",
                    "",
                    "Beda lisensinya penting kalau kamu ingin mengubah kodenya. Kalau",
                    "Metabase versi AGPL kamu ubah lalu kamu tawarkan ke orang lain",
                    "lewat jaringan, kode perubahannya wajib dibuka. Lisensi Apache 2.0",
                    "milik Superset nggak mewajibkan itu.",
                    "",
                    "Qlik Sense memakai mesin asosiatif: memilih satu nilai menyaring",
                    "semua visual, dan nilai yang nggak terkait ikut ditampilkan dengan",
                    "warna abu-abu, jadi kamu juga melihat apa yang nggak ada. Qlik",
                    "banyak dipakai di manufaktur dan ritel, terutama di Eropa.",
                    "",
                    "Tiga alat lain sering disebut berdampingan dengan BI. Grafana",
                    "(AGPL-3.0) untuk dasbor metrik server dan deret waktu, dan ia lebih",
                    "dekat ke ranah DevOps. Redash (BSD-2-Clause) untuk dasbor SQL",
                    "ringan, sekarang dirawat komunitas dan menurun. Evidence (MIT)",
                    "untuk laporan sebagai kode: Markdown plus SQL yang dibangun jadi",
                    "situs.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Startup sering memulai dengan Metabase karena gratis dan dalam",
                    "sejam bisa tersambung ke database PostgreSQL aplikasinya. UMKM dan",
                    "tim pemasaran banyak memakai Looker Studio karena datanya sudah di",
                    "Google Sheets dan Google Analytics. Perusahaan besar di ekosistem",
                    "Microsoft memakai Power BI.",
                    "",
                    "Kasus kecil: kamu magang di startup kecil yang semua komputernya",
                    "memakai Linux. Tim operasional minta dasbor pesanan harian dari",
                    "database PostgreSQL, tanpa anggaran lisensi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Coret dulu alat yang Desktop-nya cuma untuk Windows atau macOS,",
                    "     yaitu Power BI Desktop dan Tableau Desktop.",
                    "  2. Pilih Metabase edisi open source, karena tim operasional nggak",
                    "     bisa SQL dan butuh pembuat pertanyaan visual. Jalankan berkas",
                    "     metabase.jar atau pakai image Docker resmi:",
                    "       java --add-opens java.base/java.nio=ALL-UNNAMED \\",
                    "         -jar metabase.jar",
                    "  3. Sambungkan ke replika baca database, bukan database utama,",
                    "     supaya query dasbor nggak memperlambat aplikasi.",
                    "  4. Buat pertanyaan pesanan per hari dan per kota, susun jadi satu",
                    "     dasbor, lalu atur langganan email harian untuk tim.",
                ],
            },
        ],
    },
]
