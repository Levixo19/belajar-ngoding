"""Gambar konsep kurikulum Data & Analitik. Skema: inti/visual.py."""

VISUAL = {
    "Alur Kerja Analisis Data": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Lima langkah analisis, dan kapan harus balik ke awal",
            "ket": "Kalau hasil analisis belum cukup meyakinkan, perbaiki pertanyaan atau tambah data, lalu jalani lagi langkahnya.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Pertanyaan: hari paling ramai?",
                },
                {
                    "jenis": "masukan",
                    "teks": "Kumpulkan catatan kasir",
                },
                {
                    "jenis": "proses",
                    "teks": "Bersihkan: kosong dan kembar",
                },
                {
                    "jenis": "proses",
                    "teks": "Analisis: rata-rata per hari",
                },
                {
                    "jenis": "keputusan",
                    "teks": "Cukup meyakinkan?",
                    "tidak": 0,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Komunikasikan: tabel pendek",
                },
                {
                    "jenis": "selesai",
                    "teks": "Keputusan: jadwal barista",
                },
            ],
        },
    ],
    "Statistik Deskriptif: Pusat dan Sebaran": [
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "Median gaji: rata-rata dua nilai di tengah",
            "ket": "Delapan nilai terurut, jadi median = (5000 + 5300) / 2 = 5150. Gaji 38000 di ujung kanan menarik mean ke 9175, tapi median tetap di tengah.",
            "nama": "gaji",
            "isi": [
                "4200",
                "4500",
                "4500",
                "5000",
                "5300",
                "5800",
                "6100",
                "38000",
            ],
            "sorot": [3, 4],
            "penunjuk": {
                "pencilan": 7,
            },
        },
    ],
    "Peluang dan Distribusi Lewat Simulasi": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "6000 lemparan dadu dengan seed 42",
            "ket": "Teorinya tiap mata 1000 kali. Hasilnya meleset sedikit ke atas dan ke bawah, dan itu sifat acak yang wajar.",
            "tabel": [
                {
                    "kolom": [
                        "mata",
                        "kali",
                        "proporsi",
                    ],
                    "baris": [
                        [
                            "1",
                            "970",
                            "0.162",
                        ],
                        [
                            "2",
                            "974",
                            "0.162",
                        ],
                        [
                            "3",
                            "989",
                            "0.165",
                        ],
                        [
                            "4",
                            "1001",
                            "0.167",
                        ],
                        [
                            "5",
                            "999",
                            "0.167",
                        ],
                        [
                            "6",
                            "1067",
                            "0.178",
                        ],
                    ],
                    "sorot_baris": [5],
                },
            ],
        },
    ],
    "Korelasi, Regresi, dan Jebakan Sebab-Akibat": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Penjualan es teh asli dan tebakan garis regresi",
            "ket": "Tebakan = 3,14 x suhu - 29,60, dibulatkan. Selisih asli dan tebakan yang dikuadratkan lalu dijumlahkan itulah yang dibuat sekecil mungkin.",
            "tabel": [
                {
                    "kolom": [
                        "suhu",
                        "terjual",
                        "tebakan",
                    ],
                    "baris": [
                        [
                            "26",
                            "52",
                            "52",
                        ],
                        [
                            "27",
                            "58",
                            "55",
                        ],
                        [
                            "29",
                            "57",
                            "61",
                        ],
                        [
                            "30",
                            "66",
                            "65",
                        ],
                        [
                            "31",
                            "64",
                            "68",
                        ],
                        [
                            "32",
                            "73",
                            "71",
                        ],
                        [
                            "33",
                            "78",
                            "74",
                        ],
                        [
                            "34",
                            "75",
                            "77",
                        ],
                    ],
                },
            ],
        },
    ],
    "Jupyter, Colab, dan Kaggle": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Satu Shift+Enter melewati tiga pihak",
            "ket": "Browser cuma menampilkan. Server Jupyter meneruskan kode ke kernel, dan kernel yang menjalankan serta menyimpan variabelnya.",
            "pelaku": [
                "browser",
                "server Jupyter",
                "kernel",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "Shift+Enter: kode sel",
                ],
                [
                    1,
                    2,
                    "jalankan kode ini",
                ],
                [
                    2,
                    1,
                    "hasil, nomor [3]",
                ],
                [
                    1,
                    0,
                    "tampilkan di bawah sel",
                ],
            ],
        },
    ],
    "Environment Python: venv, conda, dan Miniforge": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Satu proyek, satu folder .venv di dalamnya",
            "ket": "requirements.txt masuk Git. Folder .venv dicatat di .gitignore dan dibuat ulang di tiap komputer.",
            "akar": {
                "teks": "proyek-kopi/",
                "anak": [
                    {
                        "teks": ".venv/",
                        "anak": [
                            {
                                "teks": "bin/python",
                            },
                            {
                                "teks": "lib/ (paket)",
                            },
                        ],
                    },
                    {
                        "teks": "data/",
                        "anak": [
                            {
                                "teks": "kasir.csv",
                            },
                        ],
                    },
                    {
                        "teks": "analisis.ipynb",
                    },
                    {
                        "teks": "requirements.txt",
                    },
                    {
                        "teks": ".gitignore",
                    },
                ],
            },
        },
    ],
    "Spreadsheet sebagai Alat Analisis Pertama": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Pivot omzet: produk sebagai baris, bulan sebagai kolom",
            "ket": "Angka sama dengan keluaran program. Sel 0 di Roti bakar berarti nggak ada penjualan di bulan itu.",
            "tabel": [
                {
                    "kolom": [
                        "produk",
                        "2026-09",
                        "2026-10",
                        "total",
                    ],
                    "baris": [
                        [
                            "Kopi susu",
                            "90000",
                            "108000",
                            "198000",
                        ],
                        [
                            "Roti bakar",
                            "0",
                            "88000",
                            "88000",
                        ],
                        [
                            "Teh tarik",
                            "75000",
                            "15000",
                            "90000",
                        ],
                    ],
                    "sorot_kolom": [
                        "total",
                    ],
                },
            ],
        },
    ],
    "NumPy: Larik N-Dimensi dan Broadcasting": [
        {
            "setelah": 4,
            "jenis": "larik",
            "judul": "Bobot (3,) diulang untuk tiap baris nilai",
            "ket": "Baris pertama: 80 x 0,3 + 75 x 0,3 + 90 x 0,4 = 82,5. Bobot nggak disalin di memori; NumPy cukup memakainya ulang untuk baris kedua.",
            "nama": "bobot",
            "isi": [
                "0.3",
                "0.3",
                "0.4",
            ],
            "sorot": [2],
        },
        {
            "setelah": 8,
            "jenis": "memori",
            "judul": "potong menunjuk data milik a, salin punya data sendiri",
            "ket": "Irisan NumPy adalah view, jadi potong[0] = 99 mengubah a. Hasil .copy() terpisah, jadi salin[0] = -1 nggak menyentuh a.",
            "tumpukan": [
                [
                    "a",
                    "@data",
                ],
                [
                    "potong",
                    "@data",
                ],
                [
                    "salin",
                    "@baru",
                ],
            ],
            "heap": [
                {
                    "id": "data",
                    "isi": "[1, 99, 3, 4, 5]",
                },
                {
                    "id": "baru",
                    "isi": "[-1, 3, 4] (salinan)",
                },
            ],
            "label_tumpukan": "nama",
            "label_heap": "data larik",
        },
    ],
    "Vektor, Matriks, dan Gradien": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "A x B: tiap sel adalah baris A dikali kolom B",
            "ket": "Sel kiri atas = 1 x 5 + 2 x 7 = 19. Sel kanan bawah = 3 x 6 + 4 x 8 = 50.",
            "tabel": [
                {
                    "nama": "A",
                    "kolom": [
                        "k1",
                        "k2",
                    ],
                    "baris": [
                        [
                            "1",
                            "2",
                        ],
                        [
                            "3",
                            "4",
                        ],
                    ],
                    "sorot_baris": [0],
                },
                {
                    "nama": "B",
                    "kolom": [
                        "k1",
                        "k2",
                    ],
                    "baris": [
                        [
                            "5",
                            "6",
                        ],
                        [
                            "7",
                            "8",
                        ],
                    ],
                    "sorot_kolom": [
                        "k1",
                    ],
                },
                {
                    "nama": "A x B",
                    "kolom": [
                        "k1",
                        "k2",
                    ],
                    "baris": [
                        [
                            "19",
                            "22",
                        ],
                        [
                            "43",
                            "50",
                        ],
                    ],
                },
            ],
            "panah": "baris A dikali kolom B",
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Gradient descent: melangkah berlawanan dengan gradien",
            "ket": "Untuk contoh y = w x x dengan laju 0,02, perulangan ini berhenti sesudah 25 langkah dengan w = 1,9897.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "w = 0",
                },
                {
                    "jenis": "proses",
                    "teks": "hitung gradien galat di w",
                },
                {
                    "jenis": "proses",
                    "teks": "w = w - laju x gradien",
                },
                {
                    "jenis": "keputusan",
                    "teks": "sudah 25 langkah?",
                    "tidak": 1,
                },
                {
                    "jenis": "selesai",
                    "teks": "w dekat titik terendah",
                },
            ],
        },
    ],
    "SciPy untuk Statistik dan Optimasi": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Submodul SciPy yang paling sering dipakai",
            "ket": "Impor yang dibutuhkan saja, misalnya from scipy import stats.",
            "tabel": [
                {
                    "kolom": [
                        "submodul",
                        "gunanya",
                        "contoh fungsi",
                    ],
                    "baris": [
                        [
                            "stats",
                            "uji statistik",
                            "ttest_ind",
                        ],
                        [
                            "optimize",
                            "cari minimum",
                            "minimize_scalar",
                        ],
                        [
                            "interpolate",
                            "isi titik antara",
                            "CubicSpline",
                        ],
                        [
                            "signal",
                            "olah sinyal",
                            "find_peaks",
                        ],
                        [
                            "integrate",
                            "integral",
                            "quad",
                        ],
                        [
                            "linalg",
                            "aljabar linear",
                            "solve",
                        ],
                        [
                            "sparse",
                            "matriks jarang",
                            "csr_matrix",
                        ],
                        [
                            "spatial",
                            "jarak, tetangga",
                            "KDTree",
                        ],
                    ],
                },
            ],
        },
    ],
    "pandas: Series, DataFrame, dan Membaca Data": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "DataFrame: index di kiri, tiap kolom satu Series",
            "ket": "Index bukan kolom data; ia label baris. df.loc memakai label ini, df.iloc memakai posisi.",
            "tabel": [
                {
                    "kolom": [
                        "index",
                        "cabang",
                        "produk",
                        "qty",
                    ],
                    "baris": [
                        [
                            "0",
                            "Depok",
                            "Kopi susu",
                            "3",
                        ],
                        [
                            "1",
                            "Bogor",
                            "Teh tarik",
                            "5",
                        ],
                        [
                            "2",
                            "Depok",
                            "Roti bakar",
                            "2",
                        ],
                    ],
                    "sorot_kolom": [
                        "index",
                    ],
                },
            ],
        },
    ],
    "pandas: Membersihkan Data Kotor": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Urutan membersihkan data yang aman",
            "ket": "Teks dirapikan sebelum mencari baris kembar, karena \" budi \" dan \"BUDI\" baru terlihat sama sesudah dirapikan.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Muat data mentah",
                },
                {
                    "jenis": "proses",
                    "teks": "Lihat: head, dtypes, isna",
                },
                {
                    "jenis": "proses",
                    "teks": "Rapikan teks: strip, title",
                },
                {
                    "jenis": "proses",
                    "teks": "Betulkan tipe: angka, tanggal",
                },
                {
                    "jenis": "proses",
                    "teks": "Buang baris kembar",
                },
                {
                    "jenis": "keputusan",
                    "teks": "Ada kosong atau pencilan?",
                    "tidak": 7,
                },
                {
                    "jenis": "proses",
                    "teks": "Buang, isi, atau tandai",
                    "ke": 7,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Catat jumlah baris dibuang",
                },
            ],
        },
    ],
    "pandas: Group By, Pivot, dan Menggabung Tabel": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Sebelum dan sesudah groupby(\"kategori\")",
            "ket": "Enam baris transaksi jadi dua baris ringkasan. Total minuman = 90000 + 75000 + 108000 = 273000.",
            "tabel": [
                {
                    "nama": "jual",
                    "kolom": [
                        "kategori",
                        "omzet",
                    ],
                    "baris": [
                        [
                            "minuman",
                            "90000",
                        ],
                        [
                            "makanan",
                            "44000",
                        ],
                        [
                            "minuman",
                            "75000",
                        ],
                        [
                            "minuman",
                            "108000",
                        ],
                        [
                            "makanan",
                            "88000",
                        ],
                        [
                            "makanan",
                            "22000",
                        ],
                    ],
                    "sorot_baris": [0, 2, 3],
                },
                {
                    "nama": "ringkas",
                    "kolom": [
                        "kategori",
                        "total",
                        "transaksi",
                    ],
                    "baris": [
                        [
                            "minuman",
                            "273000",
                            "3",
                        ],
                        [
                            "makanan",
                            "154000",
                            "3",
                        ],
                    ],
                    "sorot_baris": [0],
                },
            ],
            "panah": "groupby, lalu agg",
        },
    ],
    "Matplotlib: Grafik yang Jujur dan Jelas": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Pilih grafik dari pertanyaannya",
            "ket": "Pai cuma layak untuk dua atau tiga bagian. Lebih dari itu, batang yang diurutkan lebih mudah dibaca.",
            "tabel": [
                {
                    "kolom": [
                        "pertanyaan",
                        "grafik",
                        "Matplotlib",
                    ],
                    "baris": [
                        [
                            "tren waktu",
                            "garis",
                            "ax.plot",
                        ],
                        [
                            "banding kategori",
                            "batang",
                            "ax.bar",
                        ],
                        [
                            "hubungan 2 angka",
                            "sebar",
                            "ax.scatter",
                        ],
                        [
                            "sebaran 1 angka",
                            "histogram",
                            "ax.hist",
                        ],
                        [
                            "ringkas sebaran",
                            "boxplot",
                            "ax.boxplot",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Pustaka Grafik: Seaborn, Plotly, Altair, Bokeh": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Empat pustaka grafik dan kekuatannya",
            "ket": "Versi per Oktober 2026. Seaborn belum merilis versi baru sejak Januari 2024, tapi tetap banyak dipakai.",
            "tabel": [
                {
                    "kolom": [
                        "pustaka",
                        "versi",
                        "gaya",
                        "keluaran",
                    ],
                    "baris": [
                        [
                            "Seaborn",
                            "0.13.2",
                            "statistik",
                            "gambar statis",
                        ],
                        [
                            "Plotly",
                            "7.1.0",
                            "interaktif",
                            "HTML, notebook",
                        ],
                        [
                            "Altair",
                            "6.3.0",
                            "deklaratif",
                            "HTML Vega-Lite",
                        ],
                        [
                            "Bokeh",
                            "3.10.1",
                            "interaktif",
                            "HTML, server",
                        ],
                    ],
                },
            ],
        },
    ],
    "Aplikasi Data: Streamlit, Gradio, dan Dash": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Tiap interaksi menjalankan app.py dari atas",
            "ket": "Hasil fungsi bertanda @st.cache_data diambil dari simpanan, jadi CSV nggak dibaca ulang.",
            "pelaku": [
                "pengguna",
                "Streamlit",
                "app.py",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "pilih cabang Bogor",
                ],
                [
                    1,
                    2,
                    "jalankan ulang dari baris 1",
                ],
                [
                    2,
                    1,
                    "data dari cache",
                ],
                [
                    2,
                    1,
                    "grafik dan metric baru",
                ],
                [
                    1,
                    0,
                    "perbarui halaman",
                ],
            ],
        },
    ],
    "Sampel, Selang Kepercayaan, dan p-value": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Dari populasi ke kesimpulan lewat sampel",
            "ket": "Yang diukur cuma sampel. Selang kepercayaan membawa tebakan itu balik ke populasi, lengkap dengan ketidakpastiannya.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "populasi: semua pesanan",
                },
                {
                    "jenis": "proses",
                    "teks": "ambil 30 pesanan secara acak",
                },
                {
                    "jenis": "proses",
                    "teks": "hitung rata-rata dan SE",
                },
                {
                    "jenis": "proses",
                    "teks": "rata-rata +/- 1,96 x SE",
                },
                {
                    "jenis": "selesai",
                    "teks": "3,07 sampai 3,93 hari",
                },
            ],
        },
    ],
    "Uji Hipotesis dengan Uji Permutasi": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Uji permutasi: kocok label, hitung yang seekstrem",
            "ket": "Untuk 6 data lama dan 4 data baru ada 210 pembagian. Empat di antaranya seekstrem data asli, jadi p = 4/210 = 0,019.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "lama (6 data), baru (4 data)",
                },
                {
                    "jenis": "proses",
                    "teks": "beda teramati = 34,17 ms",
                },
                {
                    "jenis": "proses",
                    "teks": "gabungkan jadi 10 angka",
                },
                {
                    "jenis": "proses",
                    "teks": "coba semua 210 pembagian",
                },
                {
                    "jenis": "proses",
                    "teks": "hitung yang |beda| >= 34,17",
                },
                {
                    "jenis": "keluaran",
                    "teks": "p = 4 / 210 = 0,019",
                },
            ],
        },
    ],
    "A/B Testing untuk Keputusan Produk": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Satu pengguna, satu versi, sepanjang eksperimen",
            "ket": "Hash dari nama eksperimen dan user_id selalu memberi angka yang sama, jadi u101 selalu melihat versi B.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "pengguna datang (u101)",
                },
                {
                    "jenis": "proses",
                    "teks": "sha256(eksperimen:user) % 100",
                },
                {
                    "jenis": "keputusan",
                    "teks": "angka < 50?",
                    "ya": 3,
                    "tidak": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "tampilkan versi A",
                    "ke": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "tampilkan versi B",
                },
                {
                    "jenis": "proses",
                    "teks": "catat beli atau nggak",
                },
                {
                    "jenis": "selesai",
                    "teks": "uji sekali saat n tercapai",
                },
            ],
        },
    ],
    "Deret Waktu dan Peramalan Sederhana": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Rata-rata bergerak 3 hari meredam lonjakan",
            "ket": "Angkanya sama dengan keluaran program. Lonjakan 55 dan 60 turun jadi 45,33 dan 49,00, dan dua hari pertama belum punya jendela penuh.",
            "tabel": [
                {
                    "nama": "pengunjung per hari",
                    "kolom": [
                        "hari",
                        "pengunjung",
                        "rata 3 hari",
                    ],
                    "baris": [
                        [
                            "1",
                            "40",
                            "-",
                        ],
                        [
                            "2",
                            "42",
                            "-",
                        ],
                        [
                            "3",
                            "39",
                            "40.33",
                        ],
                        [
                            "4",
                            "55",
                            "45.33",
                        ],
                        [
                            "5",
                            "41",
                            "45.00",
                        ],
                        [
                            "6",
                            "43",
                            "46.33",
                        ],
                        [
                            "7",
                            "44",
                            "42.67",
                        ],
                        [
                            "8",
                            "60",
                            "49.00",
                        ],
                    ],
                    "sorot_baris": [3, 7],
                },
            ],
        },
    ],
    "Baris vs Kolom: Apache Arrow dan Parquet": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "Disimpan per baris: nilai total tersebar",
            "ket": "Untuk menjumlahkan kolom total, pembaca harus melompati id dan kota di setiap baris.",
            "nama": "memori (baris)",
            "isi": [
                "1",
                "Bandung",
                "52",
                "2",
                "Bogor",
                "30",
                "3",
                "Bandung",
                "41",
            ],
            "sorot": [2, 5, 8],
        },
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "Disimpan per kolom: nilai total berdempetan",
            "ket": "Tabel yang sama. Kolom total tinggal dibaca satu potong dari posisi 6 sampai 8.",
            "nama": "memori (kolom)",
            "isi": [
                "1",
                "2",
                "3",
                "Bandung",
                "Bogor",
                "Bandung",
                "52",
                "30",
                "41",
            ],
            "rentang": [6, 9],
        },
    ],
    "DuckDB: SQL Analitik di Laptop": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "DuckDB membaca footer dulu, lalu kolom yang perlu saja",
            "ket": "Query contoh cuma memakai kota dan total, jadi kolom tanggal nggak pernah dibaca dari disk.",
            "pelaku": [
                "Python",
                "DuckDB",
                "berkas Parquet",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "duckdb.sql('SELECT kota, ...')",
                ],
                [
                    1,
                    2,
                    "baca footer",
                ],
                [
                    2,
                    1,
                    "skema, letak kolom, min/max",
                ],
                [
                    1,
                    2,
                    "ambil kolom kota dan total",
                ],
                [
                    2,
                    1,
                    "potongan kolom terkompresi",
                ],
                [
                    1,
                    0,
                    "hasil: list, DataFrame, Polars",
                ],
            ],
        },
    ],
    "Polars dan Dask Saat pandas Mulai Berat": [
        {
            "setelah": 9,
            "jenis": "tabel",
            "judul": "Empat alat olah tabel dan tempatnya masing-masing",
            "ket": "Batas ukuran di sini cuma pegangan kasar. Ukur dengan datamu sendiri sebelum pindah alat.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "gaya",
                        "paralel",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            "pandas",
                            "DataFrame",
                            "tidak",
                            "muat di RAM",
                        ],
                        [
                            "Polars",
                            "ekspresi, lazy",
                            "semua inti",
                            "puluhan GB",
                        ],
                        [
                            "DuckDB",
                            "SQL",
                            "semua inti",
                            "puluhan GB",
                        ],
                        [
                            "Dask",
                            "mirip pandas",
                            "inti + mesin",
                            "lebih dari RAM",
                        ],
                    ],
                },
            ],
        },
    ],
    "R untuk Pengguna Python": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Hal yang sama di Python dan R",
            "ket": "Indeks pertama beda: 0 di Python, 1 di R. Tanda dolar di R mengambil satu kolom.",
            "tabel": [
                {
                    "kolom": [
                        "hal",
                        "Python",
                        "R",
                    ],
                    "baris": [
                        [
                            "vektor",
                            "[78, 85, 62]",
                            "c(78, 85, 62)",
                        ],
                        [
                            "elemen pertama",
                            "x[0]",
                            "x[1]",
                        ],
                        [
                            "satu kolom",
                            "df[\"nilai\"]",
                            "df$nilai",
                        ],
                        [
                            "nilai hilang",
                            "NaN / None",
                            "NA",
                        ],
                        [
                            "pakai paket",
                            "import x",
                            "library(x)",
                        ],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "Tidyverse: dplyr dan ggplot2": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Pipeline dplyr dibaca dari atas ke bawah",
            "ket": "Tujuh baris masuk, baris dengan jumlah 0 dibuang, lalu tiap kota diringkas jadi satu baris dan diurutkan.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "penjualan (7 baris)",
                },
                {
                    "jenis": "proses",
                    "teks": "filter(jumlah > 0): 6 baris",
                },
                {
                    "jenis": "proses",
                    "teks": "mutate(total = harga * jumlah)",
                },
                {
                    "jenis": "proses",
                    "teks": "group_by(kota): 3 kelompok",
                },
                {
                    "jenis": "proses",
                    "teks": "summarise(transaksi, omzet)",
                },
                {
                    "jenis": "proses",
                    "teks": "arrange(desc(omzet))",
                },
                {
                    "jenis": "keluaran",
                    "teks": "Bandung, Depok, Bogor",
                },
            ],
        },
    ],
    "Peta Ekosistem R: Shiny, Quarto, tidymodels": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Lima alat di ekosistem R dan padanannya di Python",
            "ket": "Padanan Python di sini cuma perkiraan fungsi, bukan terjemahan satu lawan satu.",
            "tabel": [
                {
                    "kolom": [
                        "alat R",
                        "untuk apa",
                        "padanan Python",
                    ],
                    "baris": [
                        [
                            "Shiny",
                            "aplikasi web",
                            "Streamlit, Dash",
                        ],
                        [
                            "R Markdown",
                            "laporan + kode",
                            "Jupyter",
                        ],
                        [
                            "Quarto",
                            "dokumen, situs",
                            "Quarto juga",
                        ],
                        [
                            "tidymodels",
                            "machine learning",
                            "scikit-learn",
                        ],
                        [
                            "data.table",
                            "tabel besar",
                            "Polars",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Alat Statistik Lain: Julia, MATLAB, SAS, SPSS": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Empat alat statistik di luar Python dan R",
            "ket": "Semua punya jalan gratis di Fedora: Julia memang gratis, sisanya punya pengganti.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "lisensi",
                        "kuat di",
                        "pengganti",
                    ],
                    "baris": [
                        [
                            "Julia",
                            "MIT",
                            "simulasi ilmiah",
                            "-",
                        ],
                        [
                            "MATLAB",
                            "berbayar",
                            "teknik, sinyal",
                            "GNU Octave",
                        ],
                        [
                            "SAS",
                            "berbayar",
                            "bank, farmasi",
                            "Python, R",
                        ],
                        [
                            "SPSS",
                            "berbayar",
                            "skripsi, survei",
                            "PSPP, JASP",
                        ],
                    ],
                },
            ],
        },
    ],
    "ETL, ELT, dan Pipeline yang Idempoten": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "ETL dan ELT: beda urutan transformasi",
            "ket": "ETL membersihkan dulu sebelum memuat. ELT memuat data mentah lalu mengolahnya di gudang data, jadi data mentahnya tetap ada.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "extract dari database aplikasi",
                },
                {
                    "jenis": "keputusan",
                    "teks": "transform sebelum dimuat?",
                    "ya": 2,
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "ETL: transform di server ETL",
                },
                {
                    "jenis": "proses",
                    "teks": "load data bersih ke gudang",
                    "ke": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "ELT: load mentah ke gudang",
                },
                {
                    "jenis": "proses",
                    "teks": "transform dengan SQL (dbt)",
                },
                {
                    "jenis": "selesai",
                    "teks": "tabel siap untuk laporan",
                },
            ],
        },
    ],
    "Warehouse, Data Lake, dan Lakehouse": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Warehouse, lake, dan lakehouse",
            "ket": "Lakehouse menyimpan berkas di object storage seperti lake, tapi memberi aturan tabel seperti warehouse.",
            "tabel": [
                {
                    "kolom": [
                        "aspek",
                        "warehouse",
                        "data lake",
                        "lakehouse",
                    ],
                    "baris": [
                        [
                            "isi",
                            "tabel rapi",
                            "berkas mentah",
                            "berkas+metadata",
                        ],
                        [
                            "skema",
                            "saat ditulis",
                            "saat dibaca",
                            "dijaga format",
                        ],
                        [
                            "biaya simpan",
                            "lebih mahal",
                            "murah",
                            "murah",
                        ],
                        [
                            "akses",
                            "SQL",
                            "macam-macam",
                            "SQL, Spark, dll.",
                        ],
                        [
                            "contoh",
                            "Snowflake",
                            "S3 + Parquet",
                            "Iceberg, Delta",
                        ],
                    ],
                },
            ],
        },
    ],
    "Pemodelan Dimensional: Star Schema dan SCD": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Satu tabel fakta, dua tabel dimensi",
            "ket": "Isinya sebagian data contoh. Kolom ber-key di fakta menunjuk ke baris dimensi; angka yang dijumlahkan ada di fakta.",
            "tabel": [
                {
                    "nama": "fakta_penjualan",
                    "kolom": [
                        "tanggal_key",
                        "produk_key",
                        "jumlah",
                        "omzet",
                    ],
                    "baris": [
                        [
                            "20260901",
                            "1",
                            "3",
                            "54000",
                        ],
                        [
                            "20260901",
                            "3",
                            "2",
                            "30000",
                        ],
                        [
                            "20260902",
                            "2",
                            "4",
                            "48000",
                        ],
                    ],
                    "sorot_kolom": [
                        "jumlah",
                        "omzet",
                    ],
                },
                {
                    "nama": "dim_produk",
                    "kolom": [
                        "produk_key",
                        "nama",
                        "kategori",
                    ],
                    "baris": [
                        [
                            "1",
                            "Kopi Susu",
                            "Minuman",
                        ],
                        [
                            "2",
                            "Teh Tarik",
                            "Minuman",
                        ],
                        [
                            "3",
                            "Roti Bakar",
                            "Makanan",
                        ],
                    ],
                },
                {
                    "nama": "dim_tanggal",
                    "kolom": [
                        "tanggal_key",
                        "bulan",
                        "hari",
                    ],
                    "baris": [
                        [
                            "20260901",
                            "2026-09",
                            "Selasa",
                        ],
                        [
                            "20260902",
                            "2026-09",
                            "Rabu",
                        ],
                    ],
                },
            ],
        },
    ],
    "Kualitas Data, Lineage, dan Data Pribadi": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Data masuk, divalidasi, lalu lulus atau dikarantina",
            "ket": "Di contoh, P001 dan P004 lulus. P002, P003, dan P005 masuk karantina beserta alasannya, bukan dibuang.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "baris baru dari sumber",
                },
                {
                    "jenis": "proses",
                    "teks": "cek semua aturan tingkat baris",
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada aturan yang gagal?",
                    "ya": 3,
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "karantina + catat alasannya",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "muat ke gudang data",
                },
                {
                    "jenis": "proses",
                    "teks": "cek tingkat tabel: jumlah baris",
                },
                {
                    "jenis": "selesai",
                    "teks": "laporan kualitas ke tim",
                },
            ],
        },
    ],
    "Apache Airflow: DAG, Jadwal, dan Retry": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Satu run laporan_harian, termasuk retry di task muat",
            "ket": "retries=2 dan retry_delay 5 menit dari default_args. Kalau muat tetap gagal sesudah tiga percobaan, lapor nggak dijalankan.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "jadwal 0 2 * * * terpicu",
                },
                {
                    "jenis": "proses",
                    "teks": "ekstrak",
                },
                {
                    "jenis": "proses",
                    "teks": "bersihkan",
                },
                {
                    "jenis": "proses",
                    "teks": "muat",
                },
                {
                    "jenis": "keputusan",
                    "teks": "muat berhasil?",
                    "ya": 6,
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "tunggu 5 menit, coba lagi",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "lapor",
                },
                {
                    "jenis": "selesai",
                    "teks": "run sukses",
                },
            ],
        },
    ],
    "Airflow dalam Praktik: Operator, XCom, Backfill": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Jalannya task unduh di Airflow 3",
            "ket": "Disederhanakan: antrean executor nggak digambar. Worker nggak menyentuh database langsung, semuanya lewat API server.",
            "pelaku": [
                "scheduler",
                "worker",
                "API server",
                "DB metadata",
            ],
            "pesan": [
                [
                    0,
                    3,
                    "buat run 2026-10-18",
                ],
                [
                    0,
                    1,
                    "jalankan task unduh",
                ],
                [
                    1,
                    2,
                    "status: running",
                ],
                [
                    2,
                    3,
                    "simpan status",
                ],
                [
                    1,
                    2,
                    "XCom: jalur berkas",
                ],
                [
                    2,
                    3,
                    "simpan XCom",
                ],
                [
                    0,
                    3,
                    "unduh sukses, hitung siap",
                ],
            ],
        },
    ],
    "dbt: Model SQL, ref, dan Uji Data": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Dari tabel mentah ke dasbor lewat dbt build",
            "ket": "Uji di stg_pesanan jalan sebelum omzet_per_kota dibangun. Kalau ujinya gagal, model di hilirnya dilewati.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "source: raw_pesanan",
                },
                {
                    "jenis": "proses",
                    "teks": "stg_pesanan (view)",
                },
                {
                    "jenis": "keputusan",
                    "teks": "uji not_null dan unique lulus?",
                    "ya": 4,
                    "tidak": 3,
                },
                {
                    "jenis": "selesai",
                    "teks": "omzet_per_kota dilewati",
                },
                {
                    "jenis": "proses",
                    "teks": "omzet_per_kota (table)",
                },
                {
                    "jenis": "keluaran",
                    "teks": "dasbor membaca mart",
                },
            ],
        },
    ],
    "Peta Orkestrasi dan Ingest Data": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Empat orkestrator dan unit kerjanya",
            "ket": "Status per Oktober 2026. Luigi masih dirawat tapi jarang dipilih untuk proyek baru.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "unit utama",
                        "status",
                    ],
                    "baris": [
                        [
                            "Airflow",
                            "task dalam DAG",
                            "paling dipakai",
                        ],
                        [
                            "Dagster",
                            "aset (tabel)",
                            "aktif",
                        ],
                        [
                            "Prefect",
                            "fungsi @flow",
                            "aktif",
                        ],
                        [
                            "Luigi",
                            "kelas Task",
                            "menurun",
                        ],
                        [
                            "NiFi",
                            "prosesor visual",
                            "aktif",
                        ],
                    ],
                },
            ],
        },
    ],
    "Apache Spark: Dari MapReduce ke DataFrame": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Omzet per kota lewat map, shuffle, dan reduce",
            "ket": "Nilai sama dengan program di atas. Shuffle satu-satunya langkah yang memindahkan data antarmesin.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "6 baris di 2 mesin",
                },
                {
                    "jenis": "proses",
                    "teks": "map: baris jadi (kota, jumlah)",
                },
                {
                    "jenis": "proses",
                    "teks": "shuffle: kunci sama, reducer sama",
                },
                {
                    "jenis": "proses",
                    "teks": "reduce: jumlahkan per kota",
                },
                {
                    "jenis": "keluaran",
                    "teks": "Bandung 115000, Medan 105000",
                },
            ],
        },
    ],
    "PySpark dalam Praktik": [
        {
            "setelah": 0,
            "jenis": "urutan",
            "judul": "Driver membagi pekerjaan ke dua executor",
            "ket": "Disederhanakan: satu executor bisa menjalankan banyak task sekaligus, dan shuffle bisa terjadi ke dua arah.",
            "pelaku": [
                "driver",
                "manajer",
                "executor 1",
                "executor 2",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "minta 2 executor",
                ],
                [
                    1,
                    2,
                    "nyalakan executor",
                ],
                [
                    1,
                    3,
                    "nyalakan executor",
                ],
                [
                    0,
                    2,
                    "task: partisi 0",
                ],
                [
                    0,
                    3,
                    "task: partisi 1",
                ],
                [
                    3,
                    2,
                    "shuffle: baris Medan",
                ],
                [
                    2,
                    0,
                    "hasil: Bandung, Medan",
                ],
                [
                    3,
                    0,
                    "hasil: Surabaya",
                ],
            ],
        },
    ],
    "Apache Kafka: Log, Topik, dan Offset": [
        {
            "setelah": 3,
            "jenis": "tumpukan",
            "mode": "antrean",
            "judul": "Partisi 1 berisi semua event ani, berurutan",
            "ket": "Event baru ditambah di ujung. Membaca nggak menghapus apa pun; tiap grup cuma menyimpan offset-nya sendiri.",
            "isi": [
                "0: dibuat",
                "1: dibayar",
                "2: dikirim",
            ],
            "label": "partisi 1 topik pesanan",
            "operasi": "gudang di offset 2",
        },
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Dua consumer group membaca partisi yang sama",
            "ket": "Offset yang di-commit adalah offset berikutnya yang akan dibaca. Grup analitik nggak terganggu grup gudang.",
            "pelaku": [
                "producer",
                "broker",
                "grup gudang",
                "grup analitik",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "kirim: ani dibayar",
                ],
                [
                    1,
                    2,
                    "baca offset 0-1",
                ],
                [
                    2,
                    1,
                    "commit offset 2",
                ],
                [
                    0,
                    1,
                    "kirim: ani dikirim",
                ],
                [
                    1,
                    3,
                    "baca offset 0-2",
                ],
                [
                    3,
                    1,
                    "commit offset 3",
                ],
                [
                    1,
                    2,
                    "baca offset 2",
                ],
                [
                    2,
                    1,
                    "commit offset 3",
                ],
            ],
        },
    ],
    "Peta Ekosistem Big Data dan Streaming": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Peran dan status alat big data",
            "ket": "Status per Oktober 2026. Hive sebagai mesin query menurun, tapi Hive Metastore masih banyak dipakai.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "peran",
                        "status",
                    ],
                    "baris": [
                        [
                            "Hadoop",
                            "HDFS dan YARN",
                            "sistem lama",
                        ],
                        [
                            "Hive",
                            "SQL di Hadoop",
                            "menurun",
                        ],
                        [
                            "Trino",
                            "SQL federasi",
                            "aktif",
                        ],
                        [
                            "Spark",
                            "batch besar",
                            "aktif, standar",
                        ],
                        [
                            "Flink",
                            "stream per event",
                            "aktif",
                        ],
                        [
                            "Beam",
                            "pipeline lintas",
                            "aktif",
                        ],
                        [
                            "Kafka",
                            "log event",
                            "aktif",
                        ],
                    ],
                },
            ],
        },
    ],
    "Format Tabel Terbuka: Iceberg, Delta Lake, Hudi": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Tabel Iceberg = berkas data + metadata bertingkat",
            "ket": "Berkas data nggak pernah diubah. Commit baru menulis metadata baru, dan catalog memindahkan penunjuknya.",
            "akar": {
                "teks": "pesanan/",
                "anak": [
                    {
                        "teks": "data/",
                        "anak": [
                            {
                                "teks": "00001.parquet",
                            },
                            {
                                "teks": "00002.parquet",
                            },
                        ],
                    },
                    {
                        "teks": "metadata/",
                        "anak": [
                            {
                                "teks": "v2.metadata.json",
                                "anak": [
                                    {
                                        "teks": "snap-7613-1.avro",
                                        "anak": [
                                            {
                                                "teks": "4f1c-m0.avro",
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Databricks dan Snowflake": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Databricks dan Snowflake dibandingkan",
            "ket": "Fitur keduanya makin tumpang tindih. Tabel ini menunjukkan titik berangkat masing-masing.",
            "tabel": [
                {
                    "kolom": [
                        "aspek",
                        "Databricks",
                        "Snowflake",
                    ],
                    "baris": [
                        [
                            "asal",
                            "Spark, data lake",
                            "gudang data SQL",
                        ],
                        [
                            "format tabel",
                            "Delta Lake",
                            "internal/Iceberg",
                        ],
                        [
                            "komputasi",
                            "cluster Spark",
                            "warehouse",
                        ],
                        [
                            "bahasa utama",
                            "Python, SQL",
                            "SQL, Python",
                        ],
                        [
                            "belajar gratis",
                            "Free Edition",
                            "coba 30 hari",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Platform Data Cloud": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Platform data cloud dan cara bayarnya",
            "ket": "Cara bayar menentukan kebiasaan yang perlu dijaga. Di BigQuery on-demand, kolom yang dipindai yang dihitung.",
            "tabel": [
                {
                    "kolom": [
                        "layanan",
                        "jenis",
                        "dibayar dari",
                    ],
                    "baris": [
                        [
                            "BigQuery",
                            "gudang data",
                            "data dipindai",
                        ],
                        [
                            "Redshift",
                            "gudang data AWS",
                            "jam cluster",
                        ],
                        [
                            "Snowflake",
                            "gudang data",
                            "kredit per detik",
                        ],
                        [
                            "Fabric",
                            "platform SaaS",
                            "kapasitas",
                        ],
                        [
                            "ClickHouse",
                            "OLAP open source",
                            "server sendiri",
                        ],
                        [
                            "AWS Glue",
                            "ETL Spark",
                            "pemakaian job",
                        ],
                    ],
                },
            ],
        },
    ],
    "Power BI: Model Data, DAX, dan Power Query": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Jalan data di sebuah laporan Power BI",
            "ket": "Pembersihan di Power Query, hubungan antartabel di model, angka di measure, dan tampilan di visual.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "sumber: Excel, CSV, database",
                },
                {
                    "jenis": "proses",
                    "teks": "Power Query: bersihkan (M)",
                },
                {
                    "jenis": "proses",
                    "teks": "model star: fakta + dimensi",
                },
                {
                    "jenis": "proses",
                    "teks": "measure: Total Omzet (DAX)",
                },
                {
                    "jenis": "keluaran",
                    "teks": "visual: matriks, kartu, slicer",
                },
            ],
        },
    ],
    "Merancang Dasbor yang Dibaca Orang": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "KPI, pembanding, dan visual yang cocok",
            "ket": "Tiap KPI ditemani pembanding. Angka di kartu sama dengan program contoh di materi ini.",
            "tabel": [
                {
                    "kolom": [
                        "KPI",
                        "pembanding",
                        "visual",
                    ],
                    "baris": [
                        [
                            "omzet",
                            "target, lalu",
                            "kartu + garis",
                        ],
                        [
                            "transaksi",
                            "minggu lalu",
                            "kartu angka",
                        ],
                        [
                            "rata keranjang",
                            "minggu lalu",
                            "kartu angka",
                        ],
                        [
                            "omzet per cabang",
                            "target cabang",
                            "batang urut",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Alat BI: Tableau, Looker, Metabase, Superset": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Alat BI: biaya dan dukungan Linux",
            "ket": "Untuk pengguna Fedora, pilihan yang langsung jalan adalah alat berbasis browser atau yang dipasang sendiri.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "biaya",
                        "di Linux",
                    ],
                    "baris": [
                        [
                            "Power BI",
                            "Desktop gratis",
                            "lewat browser",
                        ],
                        [
                            "Tableau",
                            "berbayar",
                            "Desktop nggak",
                        ],
                        [
                            "Looker Studio",
                            "gratis",
                            "browser",
                        ],
                        [
                            "Looker",
                            "berbayar",
                            "browser",
                        ],
                        [
                            "Metabase",
                            "AGPL + Pro",
                            "pasang sendiri",
                        ],
                        [
                            "Superset",
                            "Apache 2.0",
                            "pasang sendiri",
                        ],
                        [
                            "Qlik Sense",
                            "berbayar",
                            "browser",
                        ],
                    ],
                },
            ],
        },
    ],
}
