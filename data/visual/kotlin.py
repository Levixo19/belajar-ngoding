"""Gambar konsep kurikulum Kotlin. Skema: inti/visual.py."""

VISUAL = {
    "Pengenalan Kotlin & Instalasi": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari main.kt sampai teks muncul di layar",
            "ket": "kotlinc menerjemahkan kodemu jadi class MainKt di dalam jar, "
                   "lalu JVM yang menjalankannya.",
            "langkah": [
                {"jenis": "masukan", "teks": "main.kt (kode Kotlin)"},
                {"jenis": "proses", "teks": "kotlinc mengompilasi"},
                {"jenis": "proses", "teks": "main.jar berisi class MainKt"},
                {"jenis": "proses", "teks": "java -jar: JVM menjalankan"},
                {"jenis": "keluaran", "teks": "Halo Dunia!"},
            ],
        },
    ],
    "val, var & Tipe Data": [
        {
            "setelah": 1,
            "jenis": "variabel",
            "judul": "Enam val dari contoh tadi, tiap nilai dengan tipenya",
            "ket": "Tipenya disimpulkan compiler dari bentuk nilainya: akhiran L "
                   "jadi Long, akhiran f jadi Float, kutip tunggal jadi Char.",
            "isi": [
                ["umur", "20", "Int"],
                ["tinggi", "172.5", "Double"],
                ["huruf", "'K'", "Char"],
                ["aktif", "true", "Boolean"],
                ["panjang", "100L", "Long"],
                ["kecil", "3.14f", "Float"],
            ],
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "val daftar tetap menunjuk objek yang sama, isinya boleh bertambah",
            "ket": "val mengunci panah dari daftar ke objeknya. add(4) mengubah isi "
                   "objek itu, jadi compiler nggak keberatan.",
            "tumpukan": [["umur", "20"], ["daftar", "@L1"]],
            "heap": [{"id": "L1", "isi": "MutableList [1, 2, 3, 4]"}],
            "label_tumpukan": "variabel",
            "label_heap": "objek",
        },
    ],
    "Null Safety": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Rantai o.alamat?.kota ?: \"tidak diketahui\" untuk tiap orang",
            "ket": "Andi lolos dua pemeriksaan. Budi berhenti karena alamatnya null, "
                   "Cici karena kotanya null, dan keduanya jatuh ke sisi kanan Elvis.",
            "langkah": [
                {"jenis": "mulai", "teks": "o.alamat?.kota ?: ..."},
                {"jenis": "keputusan", "teks": "alamat bukan null?", "tidak": 4},
                {"jenis": "keputusan", "teks": "kota bukan null?", "tidak": 4},
                {"jenis": "keluaran", "teks": "pakai kota (Andi: Bandung)", "ke": 5},
                {"jenis": "keluaran", "teks": "\"tidak diketahui\" (Budi, Cici)"},
                {"jenis": "selesai", "teks": "cetak nama dan kota"},
            ],
        },
    ],
    "Fungsi": [
        {
            "setelah": 2,
            "jenis": "variabel",
            "judul": "garis(\" TEBAL \", pengisi = '=') mengisi parameter begini",
            "ket": "lebar nggak disebut, jadi nilai bawaannya yang dipakai. "
                   "pengisi diisi lewat namanya, melompati lebar.",
            "isi": [
                ["isi", "\" TEBAL \"", "String"],
                ["lebar", "30 (bawaan)", "Int"],
                ["pengisi", "'='", "Char"],
            ],
            "sorot": ["pengisi"],
        },
    ],
    "Kendali Alur": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "when memeriksa cabang dari atas, yang pertama benar dipakai",
            "ket": "Disederhanakan: cuma sebagian cabang jelaskan(x) yang digambar. "
                   "Karena in 1..9 ada di atas is Int, angka 5 jadi \"satuan 5\".",
            "langkah": [
                {"jenis": "masukan", "teks": "jelaskan(x)"},
                {"jenis": "keputusan", "teks": "x == null?", "tidak": 3},
                {"jenis": "keluaran", "teks": "\"kosong\"", "ke": 8},
                {"jenis": "keputusan", "teks": "x in 1..9?", "tidak": 5},
                {"jenis": "keluaran", "teks": "\"satuan $x\"", "ke": 8},
                {"jenis": "keputusan", "teks": "x is Int?", "tidak": 7},
                {"jenis": "keluaran", "teks": "negatif / bilangan besar", "ke": 8},
                {"jenis": "keluaran", "teks": "cabang berikutnya, lalu else"},
                {"jenis": "selesai", "teks": "kembalikan teksnya"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "1..10 step 3 mengambil 1, 4, 7, dan 10",
            "ket": "Rentang 1..10 ikut memuat 10, dan step 3 melompat tiga angka "
                   "tiap putaran.",
            "nama": "1..10",
            "isi": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            "sorot": [0, 3, 6, 9],
        },
    ],
    "Koleksi": [
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "filter { it > rata } menyisakan empat nilai di atas 78,88",
            "ket": "Yang disorot lolos filter. Urutannya tetap seperti data asli, "
                   "karena filter nggak mengurutkan.",
            "nama": "nilai",
            "isi": ["78", "92", "65", "88", "71", "95", "59", "83"],
            "sorot": [1, 3, 5, 7],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "groupBy { it.kelas } mengubah daftar murid jadi dua kelompok",
            "ket": "Kunci Map-nya kelas, nilainya daftar murid di kelas itu. "
                   "Rata-rata dihitung per kelompok sesudahnya.",
            "tabel": [
                {
                    "nama": "data",
                    "kolom": ["nama", "kelas", "nilai"],
                    "baris": [
                        ["Andi", "A", "88"], ["Budi", "B", "72"],
                        ["Cici", "A", "95"], ["Dedi", "B", "64"],
                        ["Euis", "A", "79"], ["Fajar", "B", "91"],
                    ],
                    "sorot_kolom": ["kelas"],
                },
                {
                    "nama": "hasil groupBy",
                    "kolom": ["kelas", "anggota", "rata-rata"],
                    "baris": [
                        ["A", "Andi,Cici,Euis", "87.3"],
                        ["B", "Budi,Dedi,Fajar", "75.7"],
                    ],
                },
            ],
            "panah": "groupBy { it.kelas }",
        },
    ],
    "Class, Properti & Constructor": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Dua objek Rekening, masing-masing menyimpan saldonya sendiri",
            "ket": "a dan b cuma memegang alamat objeknya. Saldo tinggal di dalam "
                   "objek, dan yang boleh mengubahnya cuma setor dan tarik.",
            "tumpukan": [["a", "@R1"], ["b", "@R2"]],
            "heap": [
                {"id": "R1", "isi": "Rekening AC0001 Andi 450000"},
                {"id": "R2", "isi": "Rekening AC0002 Budi 100000"},
            ],
            "label_tumpukan": "variabel",
            "label_heap": "objek",
        },
    ],
    "Data Class, Object & Sealed": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Sealed class Hasil dan tiga turunannya yang sudah pasti",
            "ket": "Turunannya nggak bisa ditambah dari modul lain, jadi when atas "
                   "Hasil cukup menangani tiga cabang ini tanpa else.",
            "akar": {
                "teks": "Hasil (sealed)",
                "anak": [
                    {"teks": "Sukses(data)"},
                    {"teks": "Gagal(pesan)"},
                    {"teks": "Memuat (object)"},
                ],
            },
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Isinya sama, objeknya beda: == true, === false",
            "ket": "Produk kedua di contoh dibuat langsung di baris perbandingan; "
                   "di sini ia diberi nama lain supaya kelihatan.",
            "tumpukan": [["kopi", "@P1"], ["lain", "@P2"]],
            "heap": [
                {"id": "P1", "isi": "Produk(Kopi, Minuman, 25000)"},
                {"id": "P2", "isi": "Produk(Kopi, Minuman, 25000)"},
            ],
            "label_tumpukan": "variabel",
            "label_heap": "objek",
        },
    ],
    "Pewarisan & Interface": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Bangun dan Berwarna dipenuhi BangunDasar, lalu diturunkan tiga class",
            "ket": "Simpul teratas adalah dua interface. BangunDasar yang abstract "
                   "memenuhi keduanya, dan tiga class di bawahnya tinggal mengisi luas().",
            "akar": {
                "teks": "Bangun, Berwarna",
                "anak": [
                    {
                        "teks": "BangunDasar",
                        "anak": [
                            {"teks": "Persegi"},
                            {"teks": "Lingkaran"},
                            {"teks": "PersegiPanjang"},
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Dengan by isi, galeri.size diteruskan ke list di dalamnya",
            "ket": "size nggak pernah ditulis di Galeri; delegasi meneruskannya ke isi. "
                   "totalLuas() ditulis sendiri di Galeri.",
            "pelaku": ["main", "Galeri", "isi (List)"],
            "pesan": [
                [0, 1, "galeri.size"],
                [1, 2, "size (diteruskan by)"],
                [2, 1, "3"],
                [1, 0, "3"],
                [0, 1, "galeri.totalLuas()"],
                [1, 0, "62.27"],
            ],
        },
    ],
    "Lambda & Higher-Order Function": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Lima scope function, dibedakan lewat dua kolom",
            "ket": "Kolom tengah: nama penerima di dalam blok. Kolom kanan: apa yang "
                   "dikembalikan sesudah bloknya selesai.",
            "tabel": [
                {
                    "kolom": ["fungsi", "penerima", "mengembalikan"],
                    "baris": [
                        ["let", "it", "hasil lambda"],
                        ["run", "this", "hasil lambda"],
                        ["with", "this", "hasil lambda"],
                        ["apply", "this", "objeknya sendiri"],
                        ["also", "it", "objeknya sendiri"],
                    ],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "kaliTiga menyimpan lambda yang ikut membawa faktor = 3",
            "ket": "Disederhanakan: closure menangkap faktor waktu pengali(3) jalan, "
                   "jadi nilainya tetap ada walau pengali sudah selesai.",
            "tumpukan": [["kaliTiga", "@F1"]],
            "heap": [{"id": "F1", "isi": "{ it * faktor }, faktor=3"}],
            "label_tumpukan": "variabel",
            "label_heap": "objek fungsi",
        },
    ],
    "Generic & Extension Lanjut": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "judul": "Kotak<Int>(3) bekerja seperti antrean: yang masuk duluan keluar duluan",
            "ket": "10, 20, 30 masuk dan 40 ditolak karena penuh. keluar() memakai "
                   "removeFirstOrNull, jadi yang keluar 10 dan sisanya 20, 30.",
            "mode": "antrean",
            "isi": ["20", "30"],
            "label": "Kotak<Int>, muat 3",
            "operasi": "keluar() -> 10",
        },
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "saringTipe<Int>(campur) mengambil isi bertipe Int: 1 dan 5",
            "ket": "Pemeriksaan tipe saat program jalan ini mungkin karena reified. "
                   "3.0 itu Double, jadi nggak ikut.",
            "nama": "campur",
            "isi": ["1", "\"dua\"", "3.0", "\"empat\"", "5", "true"],
            "sorot": [0, 4],
        },
    ],
    "Exception & Penanganan Galat": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Jalannya satu tagihan di perulangan Dompet",
            "ket": "require melempar IllegalArgumentException untuk -5, dan "
                   "SaldoKurangException dilempar untuk 100000. Dua-duanya ditangkap, "
                   "lalu perulangan lanjut.",
            "langkah": [
                {"jenis": "mulai", "teks": "d.bayar(tagihan)"},
                {"jenis": "keputusan", "teks": "jumlah > 0?", "tidak": 5},
                {"jenis": "keputusan", "teks": "jumlah <= saldo?", "tidak": 6},
                {"jenis": "proses", "teks": "saldo -= jumlah"},
                {"jenis": "keluaran", "teks": "cetak sisa saldo", "ke": 7},
                {"jenis": "keluaran", "teks": "catch: DITOLAK", "ke": 7},
                {"jenis": "keluaran", "teks": "catch: GAGAL, kurang sekian"},
                {"jenis": "selesai", "teks": "lanjut ke tagihan berikutnya"},
            ],
        },
    ],
    "Coroutine: Asinkron Tanpa Callback": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Berurutan: B baru mulai sesudah A selesai, total sekitar 400 ms",
            "pelaku": ["main", "A", "B"],
            "pesan": [
                [0, 1, "ambil(\"A\", 200)"],
                [1, 0, "A selesai (200ms)"],
                [0, 2, "ambil(\"B\", 200)"],
                [2, 0, "B selesai (200ms)"],
            ],
        },
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Bersamaan: C dan D dimulai dulu, baru ditunggu, total sekitar 200 ms",
            "ket": "Dua pekerjaan menunggu di waktu yang sama. Pola yang sama berlaku "
                   "untuk async lalu await di coroutine.",
            "pelaku": ["main", "C", "D"],
            "pesan": [
                [0, 1, "t1.start()"],
                [0, 2, "t2.start()"],
                [1, 0, "C selesai (200ms)"],
                [2, 0, "D selesai (200ms)"],
            ],
        },
    ],
    "Teks, Regex & Format": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Empat grup regex di baris log kedua, dipecah m.destructured",
            "ket": "Grup 1 ditampung _ karena tanggalnya nggak dipakai. Grup 4 "
                   "menangkap sisa baris: gagal user=budi ip=10.0.0.9.",
            "tabel": [
                {
                    "kolom": ["grup", "variabel", "isi"],
                    "baris": [
                        ["1", "_", "2026-09-22"],
                        ["2", "jam", "09:15:44"],
                        ["3", "taraf", "WARN"],
                        ["4", "pesan", "(sisa baris)"],
                    ],
                    "sorot_baris": [1, 2, 3],
                },
            ],
        },
    ],
    "Berkas & Baris Perintah": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "keMurid() mengubah isi berkas CSV jadi List<Murid>",
            "langkah": [
                {"jenis": "masukan", "teks": "readText(): seluruh isi berkas"},
                {"jenis": "proses", "teks": "lines(): pecah per baris"},
                {"jenis": "proses", "teks": "drop(1): buang judul kolom"},
                {"jenis": "proses", "teks": "filter: buang baris kosong"},
                {"jenis": "proses", "teks": "split(\",\") lalu Murid(...)"},
                {"jenis": "keluaran", "teks": "List<Murid> berisi 3 murid"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "val (nama, kelas, nilai) = baris.split(\",\")",
            "ket": "Destructuring mengambil isi list menurut urutannya. Kalau "
                   "kolomnya kurang dari tiga, baris ini melempar exception.",
            "nama": "\"Andi,A,88\"",
            "isi": ["Andi", "A", "88"],
            "penunjuk": {"nama": 0, "kelas": 1, "nilai": 2},
        },
    ],
    "Struktur Proyek & Gradle": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Susunan folder proyek Kotlin yang dibangun Gradle",
            "ket": "Disederhanakan: settings.gradle.kts dan gradle.properties nggak "
                   "digambar. Kode program di src/main/kotlin, tes di src/test/kotlin.",
            "akar": {
                "teks": "proyekku/",
                "anak": [
                    {"teks": "build.gradle.kts"},
                    {"teks": "gradlew"},
                    {"teks": "gradle/", "anak": [{"teks": "libs.versions.toml"}]},
                    {
                        "teks": "src/",
                        "anak": [
                            {
                                "teks": "main/kotlin/",
                                "anak": [
                                    {
                                        "teks": "toko/",
                                        "anak": [
                                            {"teks": "Main.kt"},
                                            {"teks": "domain/Produk.kt"},
                                            {"teks": "data/ProdukRepo.kt"},
                                            {"teks": "util/Format.kt"},
                                        ],
                                    },
                                ],
                            },
                            {
                                "teks": "test/kotlin/",
                                "anak": [
                                    {
                                        "teks": "toko/domain/",
                                        "anak": [{"teks": "ProdukTest.kt"}],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Pengujian": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Tiap fungsi @Test di RaporTest mulai dari Rapor yang baru",
            "ket": "@BeforeTest jalan sebelum setiap tes, jadi data dari tes "
                   "sebelumnya nggak pernah terbawa.",
            "langkah": [
                {"jenis": "mulai", "teks": "./gradlew test"},
                {"jenis": "proses", "teks": "@BeforeTest: rapor = Rapor()"},
                {"jenis": "proses", "teks": "jalankan satu fungsi @Test"},
                {"jenis": "keputusan", "teks": "semua assertion lolos?", "tidak": 5},
                {"jenis": "keluaran", "teks": "catat: lulus", "ke": 6},
                {"jenis": "keluaran", "teks": "catat: gagal beserta pesannya"},
                {"jenis": "keputusan", "teks": "masih ada tes?", "ya": 1, "tidak": 7},
                {"jenis": "selesai", "teks": "laporan tes"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Nilai uji grade dipilih berpasangan, tepat di tiap batas",
            "ket": "Baris yang disorot adalah batas bawah A, B, dan C. Salah ketik "
                   "> untuk >= langsung ketahuan di sana.",
            "tabel": [
                {
                    "kolom": ["nilai", "grade"],
                    "baris": [
                        ["85", "A"], ["84", "B"], ["75", "B"], ["74", "C"],
                        ["60", "C"], ["59", "D"], ["0", "D"],
                    ],
                    "sorot_baris": [0, 2, 4],
                },
            ],
        },
    ],
    "Proyek Utuh: Menggabungkan Semuanya": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Keluar B02 10: Gudang menolak lewat nilai kembalian",
            "ket": "Nggak ada exception yang dilempar. Kegagalannya pulang sebagai "
                   "Hasil.Salah, dan main yang memutuskan cara mencetaknya.",
            "pelaku": ["main", "Gudang", "isi (Map)"],
            "pesan": [
                [0, 1, "catat(B02, KELUAR, 10)"],
                [1, 2, "isi[\"B02\"]"],
                [2, 1, "Barang stok 4"],
                [1, 0, "Hasil.Salah(StokTidakCukup)"],
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Isi gudang di akhir program, B02 masuk daftar stok menipis",
            "ket": "Stok B01 naik jadi 25 dan B03 turun jadi 20. B02 tetap 4 karena "
                   "pengeluaran 10 ditolak, dan 4 kurang dari batas 10.",
            "tabel": [
                {
                    "nama": "gudang.semua()",
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
