"""Gambar konsep kurikulum TypeScript. Skema: inti/visual.py."""

VISUAL = {
    "Pengenalan TypeScript & Instalasi": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari berkas.ts sampai program jalan, tipenya hilang di tengah jalan",
            "ket": "tsc memeriksa tipe lalu menulis JavaScript tanpa satu pun anotasi. "
                   "Yang dijalankan node cuma berkas .js itu.",
            "langkah": [
                {"jenis": "masukan", "teks": "berkas.ts (kode + anotasi tipe)"},
                {"jenis": "proses", "teks": "tsc memeriksa tipe"},
                {"jenis": "keputusan", "teks": "tipenya cocok?", "tidak": 5},
                {"jenis": "proses", "teks": "tulis berkas.js, tipe dihapus"},
                {"jenis": "keluaran", "teks": "node berkas.js: Halo, Andi!", "ke": 6},
                {"jenis": "keluaran", "teks": "error tipe beserta nomor baris"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Tipe Dasar": [
        {
            "setelah": 1,
            "jenis": "variabel",
            "judul": "Variabel dari contoh tadi beserta tipe yang disimpulkan TypeScript",
            "ket": "Tipe di kanan nggak kamu tulis untuk nama, umur, dan nilai. "
                   "TypeScript menyimpulkannya dari nilai awalnya.",
            "isi": [
                ["nama", "\"Andi\"", "string"],
                ["umur", "20", "number"],
                ["nilai", "[78, 92, 65]", "number[]"],
                ["titik", "[3, 4]", "tuple"],
                ["m.catatan", "undefined", "string?"],
            ],
            "sorot": ["titik"],
        },
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "jelaskan(x: unknown) mempersempit tipe x satu pemeriksaan demi satu",
            "ket": "Disederhanakan: pemeriksaan boolean dan Array.isArray digabung di "
                   "cabang terakhir. Di tiap cabang ya, compiler tahu tipe x yang baru.",
            "langkah": [
                {"jenis": "mulai", "teks": "x: unknown"},
                {"jenis": "keputusan", "teks": "typeof x === \"string\"?", "tidak": 3},
                {"jenis": "keluaran", "teks": "teks 4 huruf (x: string)", "ke": 8},
                {"jenis": "keputusan", "teks": "typeof x === \"number\"?", "tidak": 5},
                {"jenis": "keluaran", "teks": "angka 42 (x: number)", "ke": 8},
                {"jenis": "keputusan", "teks": "x === null?", "tidak": 7},
                {"jenis": "keluaran", "teks": "\"null\"", "ke": 8},
                {"jenis": "keluaran", "teks": "boolean, array, atau lainnya"},
                {"jenis": "selesai", "teks": "return teksnya"},
            ],
        },
    ],
    "Union, Literal & Narrowing": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Union Bentuk: properti jenis menentukan properti lain yang tersedia",
            "ket": "Begitu b.jenis dicek, compiler cuma membuka properti milik cabang "
                   "itu. Di cabang \"lingkaran\", b.sisi ditolak.",
            "akar": {"teks": "Bentuk", "anak": [
                {"teks": "\"lingkaran\"", "anak": [{"teks": "jari: number"}]},
                {"teks": "\"persegi\"", "anak": [{"teks": "sisi: number"}]},
                {"teks": "\"persegiPanjang\"", "anak": [
                    {"teks": "panjang: number"},
                    {"teks": "lebar: number"},
                ]},
            ]},
        },
    ],
    "Interface & Type Alias": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Isi semua sesudah diurutkan, dan objek hitung sesudah perulangan",
            "ket": "Cuma Budi yang punya mapel, jadi cuma dia yang lolos adalahGuru "
                   "(\"mapel\" in o). "
                   "Kunci hitung bebas karena index signature [kata: string].",
            "tabel": [
                {
                    "nama": "semua: Orang[]",
                    "kolom": ["nama", "nilai", "mapel"],
                    "baris": [["Cici", "95", None], ["Andi", "88", None],
                              ["Budi", "72", "Matematika"]],
                    "sorot_kolom": ["mapel"],
                },
                {
                    "nama": "hitung: Frekuensi",
                    "kolom": ["kata", "jumlah"],
                    "baris": [["kucing", "3"], ["ikan", "2"], ["makan", "1"],
                              ["tidur", "1"]],
                },
            ],
        },
    ],
    "Fungsi & Tipe Fungsi": [
        {
            "setelah": 1,
            "jenis": "variabel",
            "judul": "garis(\" KECIL \", 20) mengisi parameternya begini",
            "ket": "pengisi nggak disebut, jadi nilai bawaannya yang dipakai. "
                   "Hasilnya baris selebar 20 yang diisi tanda minus.",
            "isi": [
                ["isi", "\" KECIL \"", "string"],
                ["lebar", "20", "number"],
                ["pengisi", "\"-\" (bawaan)", "string"],
            ],
            "sorot": ["pengisi"],
        },
    ],
    "Generic": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Satu fungsi ambil, dua tipe hasil yang berbeda",
            "ket": "T diisi Murid dari argumen pertama, K diisi teks yang kamu tulis, "
                   "dan T[K] adalah tipe properti itu.",
            "tabel": [
                {
                    "kolom": ["panggilan", "K", "T[K]"],
                    "baris": [["ambil(m,\"nama\")", "\"nama\"", "string"],
                              ["ambil(m,\"nilai\")", "\"nilai\"", "number"]],
                    "sorot_kolom": ["T[K]"],
                },
            ],
        },
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "mode": "antrean",
            "judul": "Kotak<number> bermuatan 3 sesudah empat kali masuk",
            "ket": "masuk(40) mengembalikan false karena kotaknya penuh. keluar() "
                   "memakai shift(), jadi yang keluar 10, yang paling depan.",
            "isi": ["10", "20", "30"],
            "label": "Kotak<number>, muat 3",
            "operasi": "keluar() -> 10",
        },
    ],
    "Class & Modifier Akses": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Interface, class abstrak, dan dua turunannya di contoh tadi",
            "ket": "Bangun cuma kontrak. BangunDasar abstrak, jadi nggak bisa di-new. "
                   "Persegi dan Lingkaran mengisi luas() masing-masing.",
            "akar": {"teks": "Bangun (interface)", "anak": [
                {"teks": "BangunDasar", "anak": [
                    {"teks": "Persegi"},
                    {"teks": "Lingkaran"},
                ]},
            ]},
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "a dan b menunjuk dua objek Rekening yang berbeda",
            "ket": "Saldo a: 500000 + 250000, tarik 900000 ditolak, tarik 300000 "
                   "diterima. #saldo cuma bisa disentuh method di dalam class.",
            "tumpukan": [["a", "@R1"], ["b", "@R2"]],
            "heap": [
                {"id": "R1", "isi": "AC0001 Andi #saldo 450000"},
                {"id": "R2", "isi": "AC0002 Budi #saldo 100000"},
            ],
            "label_tumpukan": "variabel",
            "label_heap": "objek",
        },
    ],
    "Modul: import & export": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Dengan tsconfig tadi, src berisi kode .ts dan dist berisi hasilnya",
            "ket": "rootDir menunjuk src, outDir menunjuk dist. declaration menambah "
                   "berkas .d.ts. Berkas .js.map dari sourceMap nggak digambar.",
            "akar": {"teks": "proyek/", "anak": [
                {"teks": "tsconfig.json"},
                {"teks": "src/", "anak": [
                    {"teks": "murid.ts"},
                    {"teks": "main.ts"},
                ]},
                {"teks": "dist/", "anak": [
                    {"teks": "murid.js"},
                    {"teks": "murid.d.ts"},
                    {"teks": "main.js"},
                    {"teks": "main.d.ts"},
                ]},
            ]},
        },
    ],
    "Async, Promise & await": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Berurutan: B baru diminta sesudah A selesai, total sekitar 400 ms",
            "pelaku": ["main", "ambil A", "ambil B"],
            "pesan": [
                [0, 1, "await ambil(\"A\", 200)"],
                [1, 0, "A selesai (200ms)"],
                [0, 2, "await ambil(\"B\", 200)"],
                [2, 0, "B selesai (200ms)"],
            ],
        },
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Bersamaan: C dan D diminta sekaligus, total sekitar 200 ms",
            "ket": "Promise.all menjalankan keduanya dulu, baru menunggu. Lamanya "
                   "ditentukan yang paling lambat, bukan jumlah semuanya.",
            "pelaku": ["main", "ambil C", "ambil D"],
            "pesan": [
                [0, 1, "ambil(\"C\", 200)"],
                [0, 2, "ambil(\"D\", 200)"],
                [1, 0, "C selesai (200ms)"],
                [2, 0, "D selesai (200ms)"],
            ],
        },
    ],
    "Tipe Lanjut": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Kupas<T> bercabang seperti a ? b : c, tapi untuk tipe",
            "ket": "infer U menangkap tipe isi array supaya bisa dipakai di cabang ya. "
                   "Kupas<number[]> jadi number, Kupas<string> tetap string.",
            "langkah": [
                {"jenis": "masukan", "teks": "Kupas<T>"},
                {"jenis": "keputusan", "teks": "T extends Array<infer U>?", "tidak": 3},
                {"jenis": "keluaran", "teks": "hasilnya U", "ke": 4},
                {"jenis": "keluaran", "teks": "hasilnya T apa adanya"},
                {"jenis": "selesai", "teks": "tipe hasil"},
            ],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Mapped type mengubah tiap properti Murid dengan aturan yang sama",
            "ket": "BisaDiubah membuang readonly (-readonly), WajibSemua membuang tanda "
                   "opsional (-?). Nama propertinya tetap.",
            "tabel": [
                {
                    "kolom": ["properti", "Murid", "BisaDiubah", "WajibSemua"],
                    "baris": [
                        ["id", "readonly number", "number", "readonly number"],
                        ["nama", "string", "string", "string"],
                        ["nilai", "number", "number", "number"],
                        ["catatan", "string, opsional", "string, opsional", "string"],
                    ],
                    "sorot_baris": [0, 3],
                },
            ],
        },
    ],
    "Enum, const & Readonly": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Enum Status dan objek Taraf as const, berdampingan",
            "ket": "Keduanya punya nilai waktu program jalan. Bedanya, tipe Taraf "
                   "diturunkan dari kolom nilai: \"info\" | \"peringatan\" | "
                   "\"galat\", jadi daftarnya cuma ditulis sekali.",
            "tabel": [
                {
                    "nama": "enum Status",
                    "kolom": ["anggota", "nilai"],
                    "baris": [["Draf", "\"draf\""], ["Ditinjau", "\"ditinjau\""],
                              ["Terbit", "\"terbit\""]],
                },
                {
                    "nama": "Taraf (as const)",
                    "kolom": ["kunci", "nilai"],
                    "baris": [["Info", "\"info\""], ["Peringatan", "\"peringatan\""],
                              ["Galat", "\"galat\""]],
                    "sorot_kolom": ["nilai"],
                },
            ],
        },
    ],
    "Data dari Luar: Tipe Bukan Jaminan": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "uraikanMurid memeriksa teks dari luar di dua pintu",
            "ket": "Data cuma lolos sebagai Murid sesudah melewati JSON.parse dan "
                   "adalahMurid. Sebelum itu tipenya unknown.",
            "langkah": [
                {"jenis": "masukan", "teks": "teks dari luar"},
                {"jenis": "keputusan", "teks": "JSON.parse berhasil?", "tidak": 5},
                {"jenis": "keputusan", "teks": "adalahMurid(mentah)?", "tidak": 4},
                {"jenis": "keluaran", "teks": "{ ok: true, nilai: Murid }", "ke": 6},
                {"jenis": "keluaran", "teks": "TOLAK bentuk data tidak sesuai", "ke": 6},
                {"jenis": "keluaran", "teks": "TOLAK JSON tidak bisa diurai"},
                {"jenis": "selesai", "teks": "kembalikan Hasil<Murid>"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Lima masukan tadi dan nasibnya masing-masing",
            "tabel": [
                {
                    "kolom": ["masukan", "hasil"],
                    "baris": [
                        ["Andi, nilai 88", "OK"],
                        ["Budi tanpa nilai", "TOLAK bentuk"],
                        ["Cici, nilai 150", "TOLAK bentuk"],
                        ["nama kosong", "TOLAK bentuk"],
                        ["{rusak}", "TOLAK JSON"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Pengujian": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Data it.each untuk grade: dua nilai di setiap batas",
            "ket": "Tiap pasangan mengapit satu batas (85, 75, 60). Kalau >= salah "
                   "ketik jadi >, salah satu baris di pasangan itu langsung gagal.",
            "tabel": [
                {
                    "kolom": ["nilai", "harapan"],
                    "baris": [["85", "A"], ["84", "B"], ["75", "B"], ["74", "C"],
                              ["60", "C"], ["59", "D"], ["0", "D"]],
                    "sorot_baris": [0, 2, 4],
                },
            ],
        },
    ],
    "Bekerja dengan Data & Koleksi": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Lima transaksi masuk, Map rekap keluar dengan dua kategori",
            "ket": "Perulangan menambahkan subtotal tiap transaksi ke entri kategorinya. "
                   "Map.get mengembalikan undefined untuk kategori yang belum ada.",
            "tabel": [
                {
                    "nama": "data",
                    "kolom": ["barang", "kategori", "jumlah", "harga"],
                    "baris": [
                        ["Kopi", "Minuman", "3", "25000"],
                        ["Teh", "Minuman", "5", "15000"],
                        ["Roti", "Makanan", "2", "20000"],
                        ["Nasi", "Makanan", "4", "30000"],
                        ["Jus", "Minuman", "1", "35000"],
                    ],
                },
                {
                    "nama": "rekap: Map",
                    "kolom": ["kategori", "total", "n"],
                    "baris": [["Makanan", "160000", "2"], ["Minuman", "185000", "3"]],
                },
            ],
            "panah": "rekap.set(kategori, total + sub(t))",
        },
    ],
    "TypeScript di Node & Browser": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "main() menulis CSV ke folder sementara, membacanya, lalu membersihkan",
            "pelaku": ["main()", "fs/promises", "folder tmp"],
            "pesan": [
                [0, 1, "mkdtemp(\"belajar-ts-\")"],
                [1, 2, "buat folder baru"],
                [0, 1, "writeFile(murid.csv)"],
                [1, 2, "tulis 4 baris CSV"],
                [0, 1, "readFile(murid.csv)"],
                [1, 0, "teks CSV untuk dariCsv"],
                [0, 1, "rm(folder, recursive)"],
                [1, 2, "hapus folder"],
            ],
        },
    ],
    "Proyek Utuh: Menggabungkan Semuanya": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Gudang.catat memeriksa tiga syarat sebelum stok diubah",
            "ket": "Tiap kegagalan dikembalikan sebagai galat bertanda, bukan dilempar. "
                   "Pemanggil wajib mengecek hasil.ok dulu.",
            "langkah": [
                {"jenis": "mulai", "teks": "catat(kode, gerak, jumlah)"},
                {"jenis": "keputusan", "teks": "kode ada di #isi?", "tidak": 6},
                {"jenis": "keputusan", "teks": "jumlah bulat dan > 0?", "tidak": 7},
                {"jenis": "keputusan", "teks": "stok baru >= 0?", "tidak": 8},
                {"jenis": "proses", "teks": "#isi.set(kode, {...b, stok})"},
                {"jenis": "keluaran", "teks": "{ ok: true, nilai: baru }", "ke": 9},
                {"jenis": "keluaran", "teks": "galat kodeTidakDikenal", "ke": 9},
                {"jenis": "keluaran", "teks": "galat jumlahTidakSah", "ke": 9},
                {"jenis": "keluaran", "teks": "galat stokTidakCukup"},
                {"jenis": "selesai", "teks": "kembalikan Hasil<number>"},
            ],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Isi gudang sesudah lima langkah, tiga di antaranya ditolak",
            "ket": "B02 tetap 4 karena keluar 10 ditolak. Nilai persediaannya "
                   "375000 + 340000 + 2400000 = 3115000.",
            "tabel": [
                {
                    "kolom": ["kode", "nama", "stok", "harga", "subtotal"],
                    "baris": [
                        ["B01", "Kabel", "25", "15000", "375000"],
                        ["B02", "Adaptor", "4", "85000", "340000"],
                        ["B03", "Mouse", "20", "120000", "2400000"],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
}
