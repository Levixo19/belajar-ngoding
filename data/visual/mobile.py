"""Gambar konsep kurikulum Mobile & Desktop. Skema: inti/visual.py."""

VISUAL = {
    "Native, Lintas Platform, Web, dan Desktop": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Empat cara membuat aplikasi, dibandingkan",
            "ket": "Ringkasan dari materi ini. Kolom kelemahan cuma menyebut harga yang paling sering dibayar, bukan satu-satunya.",
            "tabel": [
                {
                    "kolom": [
                        "cara",
                        "bahasa",
                        "jalan di",
                        "kelemahan",
                    ],
                    "baris": [
                        [
                            "native Android",
                            "Kotlin",
                            "Android",
                            "kode terpisah",
                        ],
                        [
                            "native iOS",
                            "Swift",
                            "iPhone",
                            "butuh Mac",
                        ],
                        [
                            "Flutter",
                            "Dart",
                            "banyak platform",
                            "fitur menyusul",
                        ],
                        [
                            "React Native",
                            "JavaScript/TS",
                            "Android, iOS",
                            "fitur menyusul",
                        ],
                        [
                            "PWA",
                            "HTML, CSS, JS",
                            "browser",
                            "akses terbatas",
                        ],
                        [
                            "Electron",
                            "HTML, CSS, JS",
                            "desktop",
                            "ukuran besar",
                        ],
                    ],
                },
            ],
        },
    ],
    "Jalur Belajar dari Fedora Tanpa Mac": [
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Dari mana build iOS-mu datang",
            "ket": "Bagian bawah tabel keputusan, digambar sebagai diagram. Jalur Android cukup Android Studio di Fedora.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "tentukan target aplikasi",
                },
                {
                    "jenis": "keputusan",
                    "teks": "perlu jalan di iPhone?",
                    "tidak": 7,
                },
                {
                    "jenis": "keputusan",
                    "teks": "punya Mac?",
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "build iOS di Xcode",
                    "ke": 8,
                },
                {
                    "jenis": "keputusan",
                    "teks": "jalurnya React Native + Expo?",
                    "tidak": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "build iOS di EAS Build",
                    "ke": 8,
                },
                {
                    "jenis": "proses",
                    "teks": "build iOS di Codemagic",
                    "ke": 8,
                },
                {
                    "jenis": "proses",
                    "teks": "Android Studio di Fedora cukup",
                },
                {
                    "jenis": "selesai",
                    "teks": "unggah ke toko aplikasi",
                },
            ],
        },
    ],
    "UI Thread, Event, dan Siklus Hidup Layar": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Satu ketukan dari jari sampai layar",
            "ket": "Semua lewat satu UI thread. Kalau handler-nya lama, event berikutnya menunggu di antrean.",
            "pelaku": [
                "pengguna",
                "antrean",
                "UI thread",
                "layar",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "ketuk tombol",
                ],
                [
                    1,
                    2,
                    "ambil event berikutnya",
                ],
                [
                    2,
                    3,
                    "gambar ulang (sekitar 16 ms)",
                ],
                [
                    3,
                    0,
                    "tombol berubah warna",
                ],
            ],
        },
    ],
    "Platform Android, API Level, dan Struktur Proyek": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Versi Android, API level, dan satu perubahan yang terasa",
            "ket": "Sebagian perubahan cuma berlaku kalau targetSdk aplikasimu setara atau lebih tinggi. Android 12L (API 32) tidak ditampilkan.",
            "tabel": [
                {
                    "kolom": [
                        "versi",
                        "API level",
                        "yang terasa",
                    ],
                    "baris": [
                        [
                            "Android 10",
                            "29",
                            "tanpa nama kue",
                        ],
                        [
                            "Android 11",
                            "30",
                            "izin sekali",
                        ],
                        [
                            "Android 12",
                            "31",
                            "exported wajib",
                        ],
                        [
                            "Android 13",
                            "33",
                            "izin notifikasi",
                        ],
                        [
                            "Android 14",
                            "34",
                            "jenis layanan",
                        ],
                        [
                            "Android 15",
                            "35",
                            "edge-to-edge",
                        ],
                        [
                            "Android 16",
                            "36",
                            "target Play 2026",
                        ],
                        [
                            "Android 17",
                            "37",
                            "terbaru",
                        ],
                    ],
                    "sorot_baris": [6],
                },
            ],
        },
    ],
    "Gradle dan Android Gradle Plugin": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Gambaran besar ./gradlew build",
            "ket": "Disederhanakan. Urutan sebenarnya ditentukan graf tugas, dan tugas yang masukannya nggak berubah dilewati.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "./gradlew build",
                },
                {
                    "jenis": "proses",
                    "teks": "susun graf tugas",
                },
                {
                    "jenis": "proses",
                    "teks": "compile: Kotlin jadi bytecode",
                },
                {
                    "jenis": "proses",
                    "teks": "test: jalankan uji unit",
                },
                {
                    "jenis": "keputusan",
                    "teks": "semua uji lulus?",
                    "tidak": 6,
                },
                {
                    "jenis": "keluaran",
                    "teks": "assemble: rakit APK",
                    "ke": 7,
                },
                {
                    "jenis": "keluaran",
                    "teks": "build gagal, baca laporannya",
                },
                {
                    "jenis": "selesai",
                    "teks": "selesai",
                },
            ],
        },
    ],
    "Siklus Hidup Activity dan Perubahan Konfigurasi": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Siklus hidup Activity",
            "ket": "Putar layar menempuh onPause, onStop, onDestroy, lalu mulai lagi dari onCreate dengan objek baru.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "onCreate",
                },
                {
                    "jenis": "proses",
                    "teks": "onStart: mulai terlihat",
                },
                {
                    "jenis": "proses",
                    "teks": "onResume: aktif di depan",
                },
                {
                    "jenis": "proses",
                    "teks": "onPause: kehilangan fokus",
                },
                {
                    "jenis": "keputusan",
                    "teks": "kembali ke depan?",
                    "ya": 2,
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "onStop: nggak terlihat",
                },
                {
                    "jenis": "keputusan",
                    "teks": "pengguna kembali?",
                    "tidak": 8,
                },
                {
                    "jenis": "proses",
                    "teks": "onRestart",
                    "ke": 1,
                },
                {
                    "jenis": "selesai",
                    "teks": "onDestroy",
                },
            ],
        },
    ],
    "Composable Pertama dan Cara Compose Menggambar": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Pohon UI dari setContent di MainActivity",
            "ket": "Hasil fase composition untuk KartuSapa(\"Rina\", \"XI RPL 2\"). Text pertama berisi sapaan, Text kedua berisi kelas.",
            "akar": {
                "teks": "MaterialTheme",
                "anak": [
                    {
                        "teks": "KartuSapa",
                        "anak": [
                            {
                                "teks": "Column",
                                "anak": [
                                    {
                                        "teks": "Text \"Halo, Rina!\"",
                                    },
                                    {
                                        "teks": "Text (kelas)",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "State, remember, dan Recomposition": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Satu ketukan sampai angkanya berubah",
            "ket": "Penghitung dengan remember dan mutableStateOf dari contoh di atas, waktu diketuk pertama kali.",
            "pelaku": [
                "pengguna",
                "Button",
                "state hitung",
                "Text",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "ketuk",
                ],
                [
                    1,
                    2,
                    "hitung++ (0 jadi 1)",
                ],
                [
                    2,
                    3,
                    "jadwalkan recomposition",
                ],
                [
                    3,
                    0,
                    "Diketuk 1 kali",
                ],
            ],
        },
    ],
    "Layout, Daftar, dan Material 3": [
        {
            "setelah": 2,
            "jenis": "tata",
            "judul": "BarisProduk: Row dengan SpaceBetween",
            "ket": "Sama dengan flex-direction: row, justify-content: space-between, dan align-items: center di CSS.",
            "mode": "flex",
            "arah": "row",
            "justify": "space-between",
            "align": "center",
            "item": [
                "Es teh manis",
                "Rp5000",
            ],
        },
    ],
    "Warisan View dan Layout XML": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Compose dibandingkan View system",
            "ket": "Keduanya masih didukung. Compose jadi pilihan untuk kode baru, View tetap ada di aplikasi lama.",
            "tabel": [
                {
                    "kolom": [
                        "hal",
                        "Compose",
                        "View dan XML",
                    ],
                    "baris": [
                        [
                            "tampilan ditulis",
                            "Kotlin",
                            "XML + Kotlin",
                        ],
                        [
                            "layar berubah",
                            "state berubah",
                            "panggil setText",
                        ],
                        [
                            "daftar panjang",
                            "LazyColumn",
                            "RecyclerView",
                        ],
                        [
                            "pratinjau",
                            "@Preview",
                            "Layout Editor",
                        ],
                        [
                            "status",
                            "utama",
                            "menurun",
                        ],
                    ],
                },
            ],
        },
    ],
    "ViewModel, UiState, dan Navigasi": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Jalan sebuah permintaan data di aplikasi berlapis",
            "ket": "Repository memutuskan sumber datanya. Layar nggak pernah tahu data datang dari database atau jaringan.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "pengguna mengetuk Muat ulang",
                },
                {
                    "jenis": "proses",
                    "teks": "UI memanggil vm.muat()",
                },
                {
                    "jenis": "proses",
                    "teks": "ViewModel bertanya ke repository",
                },
                {
                    "jenis": "keputusan",
                    "teks": "data lokal masih segar?",
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "ambil dari Room",
                    "ke": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "ambil dari API, simpan ke Room",
                },
                {
                    "jenis": "proses",
                    "teks": "ViewModel memperbarui StateFlow",
                },
                {
                    "jenis": "keluaran",
                    "teks": "composable digambar ulang",
                },
            ],
        },
    ],
    "Coroutines dan Flow untuk Kode Asinkron": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Satu coroutine memuat profil",
            "ket": "UI thread bebas selama jaringan bekerja. Hasilnya kembali ke layar lewat StateFlow.",
            "pelaku": [
                "UI",
                "coroutine",
                "jaringan",
                "StateFlow",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "launch di viewModelScope",
                ],
                [
                    1,
                    2,
                    "api.profil(7) di Dispatchers.IO",
                ],
                [
                    2,
                    1,
                    "data profil",
                ],
                [
                    1,
                    3,
                    "update { copy(nama = ...) }",
                ],
                [
                    3,
                    0,
                    "nilai baru, recomposition",
                ],
            ],
        },
    ],
    "Room: Database Lokal di Android": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Dari anotasi sampai berkas database",
            "ket": "KSP membangkitkan kode DAO saat build. Query yang salah ketahuan di langkah itu, sebelum aplikasi jalan.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "@Entity Catatan (data class)",
                },
                {
                    "jenis": "proses",
                    "teks": "@Dao berisi query dan suspend",
                },
                {
                    "jenis": "proses",
                    "teks": "@Database merangkai Entity + DAO",
                },
                {
                    "jenis": "keputusan",
                    "teks": "query cocok dengan tabel?",
                    "tidak": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "KSP membuat kode DAO",
                },
                {
                    "jenis": "keluaran",
                    "teks": "catatan.db di SQLite",
                    "ke": 7,
                },
                {
                    "jenis": "keluaran",
                    "teks": "build gagal, query diperbaiki",
                },
                {
                    "jenis": "selesai",
                    "teks": "siap dipakai repository",
                },
            ],
        },
    ],
    "Retrofit dan OkHttp: Bicara dengan API": [
        {
            "setelah": 6,
            "jenis": "urutan",
            "judul": "Permintaan melewati rantai [token, logging]",
            "ket": "Tiap interceptor dilewati dua kali: sekali saat permintaan berangkat, sekali saat respons kembali.",
            "pelaku": [
                "aplikasi",
                "token",
                "logging",
                "server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /produk",
                ],
                [
                    1,
                    2,
                    "+ Authorization",
                ],
                [
                    2,
                    3,
                    "GET /produk (dicatat)",
                ],
                [
                    3,
                    2,
                    "200",
                ],
                [
                    2,
                    1,
                    "200 (dicatat)",
                ],
                [
                    1,
                    0,
                    "respons",
                ],
            ],
        },
    ],
    "Hilt dan Dependency Injection": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Graf dependensi CatatanViewModel",
            "ket": "Hilt membuat dari bawah ke atas: Context dan OkHttpClient dulu, CatatanViewModel paling akhir.",
            "akar": {
                "teks": "CatatanViewModel",
                "anak": [
                    {
                        "teks": "CatatanRepository",
                        "anak": [
                            {
                                "teks": "CatatanDao",
                                "anak": [
                                    {
                                        "teks": "DatabaseAplikasi",
                                        "anak": [
                                            {
                                                "teks": "Context",
                                            },
                                        ],
                                    },
                                ],
                            },
                            {
                                "teks": "TokoApi",
                                "anak": [
                                    {
                                        "teks": "Retrofit",
                                        "anak": [
                                            {
                                                "teks": "OkHttpClient",
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
    "Swift Sekilas untuk Pelajar Kotlin": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Padanan Kotlin dan Swift yang paling sering ketemu",
            "ket": "Struct Swift nggak punya padanan langsung di Kotlin: data class tetap tipe referensi.",
            "tabel": [
                {
                    "kolom": [
                        "Kotlin",
                        "Swift",
                        "artinya",
                    ],
                    "baris": [
                        [
                            "val x = 1",
                            "let x = 1",
                            "tetap",
                        ],
                        [
                            "var y = 2",
                            "var y = 2",
                            "bisa diubah",
                        ],
                        [
                            "fun f()",
                            "func f()",
                            "fungsi",
                        ],
                        [
                            "String?",
                            "String?",
                            "boleh kosong",
                        ],
                        [
                            "a ?: b",
                            "a ?? b",
                            "nilai cadangan",
                        ],
                        [
                            "a!!",
                            "a!",
                            "paksa buka",
                        ],
                        [
                            "\"$nama\"",
                            "\"\\(nama)\"",
                            "interpolasi",
                        ],
                        [
                            "{ it * 2 }",
                            "{ $0 * 2 }",
                            "closure singkat",
                        ],
                    ],
                },
            ],
        },
    ],
    "SwiftUI dan UIKit: Dua Cara Membangun Layar iOS": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "SwiftUI dan UIKit untuk layar penghitung yang sama",
            "ket": "Padanan Android-nya: SwiftUI dengan Jetpack Compose, UIKit dengan View dan layout XML.",
            "tabel": [
                {
                    "kolom": [
                        "aspek",
                        "SwiftUI",
                        "UIKit",
                    ],
                    "baris": [
                        [
                            "gaya",
                            "deklaratif",
                            "imperatif",
                        ],
                        [
                            "sejak",
                            "2019 (iOS 13)",
                            "2008",
                        ],
                        [
                            "satu layar",
                            "struct View",
                            "view controller",
                        ],
                        [
                            "tata letak",
                            "VStack, HStack",
                            "Auto Layout",
                        ],
                        [
                            "state",
                            "@State",
                            "properti biasa",
                        ],
                        [
                            "ubah tampilan",
                            "otomatis",
                            "ditulis sendiri",
                        ],
                    ],
                },
            ],
        },
    ],
    "Xcode, Simulator, dan Pengelola Paket Swift": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Tiga pengelola paket iOS dan statusnya (Oktober 2026)",
            "ket": "Trunk CocoaPods read-only permanen mulai 2 Desember 2026. Proyek baru pakai SwiftPM.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "berkas",
                        "rilis terakhir",
                        "status",
                    ],
                    "baris": [
                        [
                            "SwiftPM",
                            "Package.swift",
                            "ikut Swift 6.4",
                            "aktif",
                        ],
                        [
                            "CocoaPods",
                            "Podfile",
                            "1.17.0",
                            "usang",
                        ],
                        [
                            "Carthage",
                            "Cartfile",
                            "0.40.0 (2024)",
                            "usang",
                        ],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Peta Framework Apple": [
        {
            "setelah": 8,
            "jenis": "tabel",
            "judul": "Nama framework Apple, gunanya, dan padanan Android",
            "ket": "Status per Oktober 2026. Stabil-matang berarti masih didukung tapi bukan pilihan pertama untuk kode baru.",
            "tabel": [
                {
                    "kolom": [
                        "nama",
                        "untuk",
                        "status",
                        "padanan",
                    ],
                    "baris": [
                        [
                            "Combine",
                            "aliran event",
                            "stabil-matang",
                            "Flow",
                        ],
                        [
                            "Core Data",
                            "data lokal",
                            "stabil-matang",
                            "Room",
                        ],
                        [
                            "SwiftData",
                            "data lokal",
                            "aktif",
                            "Room",
                        ],
                        [
                            "Alamofire",
                            "HTTP",
                            "stabil-matang",
                            "Retrofit",
                        ],
                        [
                            "Objective-C",
                            "bahasa lama",
                            "menurun",
                            "Java",
                        ],
                        [
                            "AppKit",
                            "layar Mac",
                            "stabil-matang",
                            "(desktop)",
                        ],
                    ],
                },
            ],
        },
    ],
    "Dart untuk Pemrogram JavaScript": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "JavaScript dan Dart berdampingan",
            "ket": "const di Dart lebih ketat dari const di JavaScript: nilainya harus sudah diketahui saat kompilasi.",
            "tabel": [
                {
                    "kolom": [
                        "JavaScript",
                        "Dart",
                        "artinya",
                    ],
                    "baris": [
                        [
                            "const x = 1",
                            "final x = 1",
                            "diisi sekali",
                        ],
                        [
                            "let y = 2",
                            "var y = 2",
                            "bisa diubah",
                        ],
                        [
                            "`Halo ${n}`",
                            "'Halo $n'",
                            "interpolasi",
                        ],
                        [
                            "Promise",
                            "Future",
                            "nilai nanti",
                        ],
                        [
                            "x ?? y",
                            "x ?? y",
                            "nilai cadangan",
                        ],
                        [
                            "(nggak ada)",
                            "String?",
                            "boleh null",
                        ],
                        [
                            "Web Worker",
                            "Isolate",
                            "kerja paralel",
                        ],
                        [
                            "npm",
                            "pub.dev",
                            "gudang paket",
                        ],
                    ],
                },
            ],
        },
    ],
    "Widget, Element, dan Cara Flutter Menggambar": [
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Pohon widget dari contoh Penghitung",
            "ket": "setState di _PenghitungState membangun ulang Scaffold ke bawah. MaterialApp tetap, dan widget const dilewati.",
            "akar": {
                "teks": "MaterialApp",
                "anak": [
                    {
                        "teks": "Penghitung",
                        "anak": [
                            {
                                "teks": "Scaffold",
                                "anak": [
                                    {
                                        "teks": "AppBar",
                                        "anak": [
                                            {
                                                "teks": "Text Penghitung",
                                            },
                                        ],
                                    },
                                    {
                                        "teks": "Center",
                                        "anak": [
                                            {
                                                "teks": "Text Diklik n",
                                            },
                                        ],
                                    },
                                    {
                                        "teks": "FAB (tombol +)",
                                        "anak": [
                                            {
                                                "teks": "Icon add",
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
    "State Management Flutter: setState, Riverpod, dan Bloc": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Perjalanan satu event di Bloc",
            "ket": "State yang sama dengan state sekarang diabaikan, jadi BlocBuilder nggak menggambar ulang.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "pengguna menekan Tambah",
                },
                {
                    "jenis": "masukan",
                    "teks": "add(Tambah(5000))",
                },
                {
                    "jenis": "proses",
                    "teks": "on<Tambah> hitung state baru",
                },
                {
                    "jenis": "keputusan",
                    "teks": "sama dengan state sekarang?",
                    "ya": 5,
                    "tidak": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "emit(state baru)",
                    "ke": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "diabaikan, nggak ada rebuild",
                },
                {
                    "jenis": "selesai",
                    "teks": "BlocBuilder build ulang",
                },
            ],
        },
    ],
    "React Native: Komponen Native dari JavaScript": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Satu ketukan tombol di New Architecture",
            "ket": "Disederhanakan. Fabric membuat shadow tree di C++, Yoga menghitung posisinya, lalu view native diubah.",
            "pelaku": [
                "kode React",
                "JSI",
                "Fabric + Yoga",
                "view native",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "render <Text>Diklik 1</Text>",
                ],
                [
                    1,
                    2,
                    "shadow tree di C++",
                ],
                [
                    2,
                    3,
                    "hitung posisi, ubah teks",
                ],
                [
                    3,
                    1,
                    "sentuhan: onPress",
                ],
                [
                    1,
                    0,
                    "panggil setJumlah(2)",
                ],
            ],
        },
    ],
    "Expo, EAS Build, dan Jalur iOS dari Linux": [
        {
            "setelah": 6,
            "jenis": "alur",
            "judul": "Jalur aplikasi iPhone dari laptop Fedora",
            "ket": "Langkah build dan tanda tangan terjadi di mesin macOS milik layanan build Expo. Akun Apple Developer tetap wajib.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "kode Expo di Fedora",
                },
                {
                    "jenis": "proses",
                    "teks": "eas build --platform ios",
                },
                {
                    "jenis": "proses",
                    "teks": "mesin macOS menjalankan Xcode",
                },
                {
                    "jenis": "keluaran",
                    "teks": "berkas .ipa bertanda tangan",
                },
                {
                    "jenis": "proses",
                    "teks": "eas submit --platform ios",
                },
                {
                    "jenis": "selesai",
                    "teks": "App Store Connect dan TestFlight",
                },
            ],
        },
    ],
    "Navigasi dengan React Navigation dan Expo Router": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "judul": "Stack sesudah Beranda, navigate Produk 7, lalu push Produk 9",
            "ket": "push selalu menumpuk, walau layar Produk sudah ada. goBack membuang Produk 9 dan kembali ke Produk 7.",
            "isi": [
                "Beranda",
                "Produk 7",
                "Produk 9",
            ],
            "operasi": "push Produk 9",
            "label": "stack navigator",
        },
    ],
    "Kotlin Multiplatform dan Compose Multiplatform": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Satu modul bersama, dua aplikasi",
            "ket": "commonMain dipakai kedua aplikasi. androidMain dan iosMain berisi actual untuk tiap platform.",
            "akar": {
                "teks": "kasir",
                "anak": [
                    {
                        "teks": "shared",
                        "anak": [
                            {
                                "teks": "commonMain",
                            },
                            {
                                "teks": "androidMain",
                            },
                            {
                                "teks": "iosMain",
                            },
                            {
                                "teks": "commonTest",
                            },
                        ],
                    },
                    {
                        "teks": "androidApp",
                        "anak": [
                            {
                                "teks": "UI Compose",
                            },
                        ],
                    },
                    {
                        "teks": "iosApp",
                        "anak": [
                            {
                                "teks": "UI SwiftUI",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Aplikasi Hybrid: Ionic, Capacitor, dan Cordova": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Camera.getPhoto dari kode web sampai kamera",
            "ket": "Nomor panggilan memasangkan balasan dengan Promise yang tepat. Disederhanakan dari cara kerja Capacitor.",
            "pelaku": [
                "kode web",
                "bridge",
                "plugin native",
                "kamera",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "Camera.getPhoto()",
                ],
                [
                    1,
                    2,
                    "pesan + nomor panggilan",
                ],
                [
                    2,
                    3,
                    "buka kamera",
                ],
                [
                    3,
                    2,
                    "foto",
                ],
                [
                    2,
                    1,
                    "balasan bernomor sama",
                ],
                [
                    1,
                    0,
                    "Promise selesai",
                ],
            ],
        },
    ],
    "Peta Lintas Platform Lain": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Kerangka lintas platform lain, Oktober 2026",
            "ket": "Pilih menurut bahasa yang sudah dikuasai tim. Xamarin cuma untuk dirawat sambil dipindah ke MAUI.",
            "tabel": [
                {
                    "kolom": [
                        "kerangka",
                        "bahasa",
                        "status",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            ".NET MAUI",
                            "C#, XAML",
                            "aktif",
                            "tim .NET",
                        ],
                        [
                            "Xamarin",
                            "C#",
                            "usang (2024)",
                            "migrasi ke MAUI",
                        ],
                        [
                            "Uno Platform",
                            "C#, XAML",
                            "aktif",
                            "aplikasi WinUI",
                        ],
                        [
                            "NativeScript",
                            "JS, TS",
                            "aktif, kecil",
                            "akses API native",
                        ],
                        [
                            "Lynx",
                            "JS, TS, CSS",
                            "aktif, muda",
                            "dicoba dulu",
                        ],
                        [
                            "Quasar",
                            "Vue",
                            "aktif",
                            "tim Vue",
                        ],
                    ],
                },
            ],
        },
    ],
    "Electron: Proses Main, Renderer, dan IPC": [
        {
            "setelah": 5,
            "jenis": "urutan",
            "judul": "Satu klik tombol Buka, dari renderer sampai berkas",
            "ket": "Renderer nggak pernah memegang fs. Ia cuma memanggil fungsi yang dibuka preload, lalu menunggu Promise yang diselesaikan main.",
            "pelaku": [
                "renderer",
                "preload",
                "main",
                "fs",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "catatan.baca('belanja')",
                ],
                [
                    1,
                    2,
                    "invoke catatan:baca",
                ],
                [
                    2,
                    3,
                    "readFile belanja.txt",
                ],
                [
                    3,
                    2,
                    "isi berkas",
                ],
                [
                    2,
                    1,
                    "Promise selesai",
                ],
                [
                    1,
                    0,
                    "teks catatan",
                ],
            ],
        },
    ],
    "Tauri dan Wails: Desktop Ringan dengan Webview Bawaan": [
        {
            "setelah": 9,
            "jenis": "tabel",
            "judul": "Electron, Tauri, dan Wails berdampingan (Oktober 2026)",
            "ket": "Angka ukuran Tauri dari dokumentasi resminya. Electron membawa Chromium, jadi tampilannya sama di semua sistem; dua lainnya ikut webview tiap sistem.",
            "tabel": [
                {
                    "nama": "tiga pilihan",
                    "kolom": [
                        "aspek",
                        "Electron",
                        "Tauri",
                        "Wails",
                    ],
                    "baris": [
                        [
                            "backend",
                            "Node.js",
                            "Rust",
                            "Go",
                        ],
                        [
                            "mesin tampilan",
                            "Chromium dibawa",
                            "webview OS",
                            "webview OS",
                        ],
                        [
                            "ukuran minimal",
                            "puluhan MB",
                            "< 600 KB",
                            "kecil",
                        ],
                        [
                            "tampilan per OS",
                            "sama persis",
                            "bisa beda",
                            "bisa beda",
                        ],
                        [
                            "mobile",
                            "tidak",
                            "Android, iOS",
                            "tidak (v2)",
                        ],
                        [
                            "versi stabil",
                            "44.9.0",
                            "2.12.4",
                            "2.17.0",
                        ],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "GUI Immediate Mode dengan Dear ImGui": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Satu frame di GUI immediate mode",
            "ket": "Kode UI dijalankan dari atas setiap frame. Tombol yang nggak dipanggil di frame itu nggak ada.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "frame baru dimulai",
                    "ke": 1,
                },
                {
                    "jenis": "masukan",
                    "teks": "baca posisi dan klik mouse",
                },
                {
                    "jenis": "proses",
                    "teks": "jalankan kode UI dari atas",
                },
                {
                    "jenis": "keputusan",
                    "teks": "Button() kena klik?",
                    "ya": 4,
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "ubah variabel state",
                },
                {
                    "jenis": "proses",
                    "teks": "kumpulkan perintah gambar",
                },
                {
                    "jenis": "keluaran",
                    "teks": "backend menggambar ke layar",
                    "ke": 0,
                },
            ],
        },
    ],
    "Peta Toolkit Desktop Native": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Toolkit desktop native yang paling sering kamu temui",
            "ket": "Versi per Oktober 2026. wxWidgets, NW.js, dan MFC dibahas di bagian Sisanya.",
            "tabel": [
                {
                    "nama": "toolkit desktop",
                    "kolom": [
                        "toolkit",
                        "bahasa",
                        "sistem",
                        "status",
                    ],
                    "baris": [
                        [
                            "Qt 6.12",
                            "C++, QML",
                            "Win/mac/Linux",
                            "aktif",
                        ],
                        [
                            "GTK 4.24",
                            "C, Python, Rust",
                            "Linux utama",
                            "aktif",
                        ],
                        [
                            "WinForms",
                            "C#, VB",
                            "Windows",
                            "stabil-matang",
                        ],
                        [
                            "WPF",
                            "C#, XAML",
                            "Windows",
                            "stabil-matang",
                        ],
                        [
                            "WinUI 3",
                            "C#, C++",
                            "Windows",
                            "aktif",
                        ],
                        [
                            "Avalonia 12.1",
                            "C#, XAML",
                            "Win/mac/Linux",
                            "aktif",
                        ],
                        [
                            "JavaFX 27",
                            "Java, Kotlin",
                            "Win/mac/Linux",
                            "stabil-matang",
                        ],
                        [
                            "Swing",
                            "Java",
                            "Win/mac/Linux",
                            "menurun",
                        ],
                    ],
                    "sorot_baris": [7],
                },
            ],
        },
    ],
    "Menguji Aplikasi Mobile: Unit, UI, dan Instrumentasi": [
        {
            "setelah": 0,
            "jenis": "tumpukan",
            "judul": "Piramida uji aplikasi mobile",
            "ket": "Dasarnya uji unit yang banyak dan cepat. Makin ke atas, uji makin lambat, makin mahal, dan makin sedikit jumlahnya.",
            "mode": "tumpukan",
            "isi": [
                "uji unit (banyak)",
                "uji instrumentasi",
                "uji UI (sedikit)",
            ],
            "label": "piramida uji",
            "operasi": "puncak paling lambat",
        },
    ],
    "Firebase untuk Aplikasi Mobile": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Koleksi, dokumen, dan subkoleksi di Firestore",
            "ket": "Koleksi berisi dokumen, dokumen berisi medan dan boleh punya subkoleksi. Alamat dokumen c1: pengguna/uid_budi/catatan/c1.",
            "akar": {
                "teks": "Firestore",
                "anak": [
                    {
                        "teks": "pengguna (koleksi)",
                        "anak": [
                            {
                                "teks": "uid_budi (dok)",
                                "anak": [
                                    {
                                        "teks": "nama: Budi",
                                    },
                                    {
                                        "teks": "kelas: XI-2",
                                    },
                                    {
                                        "teks": "catatan (koleksi)",
                                        "anak": [
                                            {
                                                "teks": "c1 (dok)",
                                            },
                                            {
                                                "teks": "c2 (dok)",
                                            },
                                        ],
                                    },
                                ],
                            },
                            {
                                "teks": "uid_sari (dok)",
                            },
                        ],
                    },
                    {
                        "teks": "guru (koleksi)",
                        "anak": [
                            {
                                "teks": "uid_bu_ani (dok)",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Fastlane dan CI/CD Rilis Mobile": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Satu lane rilis dari uji sampai unggah",
            "ket": "Langkah dijalankan berurutan. Begitu satu langkah gagal, sisanya dilewati, tapi notifikasi ke tim tetap dikirim.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "fastlane android internal",
                },
                {
                    "jenis": "proses",
                    "teks": "jalankan uji (gradle test)",
                },
                {
                    "jenis": "proses",
                    "teks": "build AAB rilis",
                },
                {
                    "jenis": "proses",
                    "teks": "tanda tangani dengan upload key",
                },
                {
                    "jenis": "keputusan",
                    "teks": "semua langkah berhasil?",
                    "ya": 5,
                    "tidak": 6,
                },
                {
                    "jenis": "keluaran",
                    "teks": "unggah ke jalur internal",
                    "ke": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "kirim notifikasi ke tim",
                },
            ],
        },
    ],
    "Google Play Console: Jalur Rilis dan Uji Tertutup": [
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Jalan sebuah aplikasi baru menuju jalur produksi",
            "ket": "Akun organisasi dan akun pribadi lama bisa langsung ke produksi. Akun pribadi yang dibuat sesudah 13 November 2023 harus lewat uji tertutup dulu.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "AAB baru diunggah",
                },
                {
                    "jenis": "proses",
                    "teks": "jalur internal (maks 100 orang)",
                },
                {
                    "jenis": "keputusan",
                    "teks": "akun pribadi sesudah 13-11-2023?",
                    "ya": 3,
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "uji tertutup: 12 orang, 14 hari",
                },
                {
                    "jenis": "proses",
                    "teks": "ajukan akses produksi",
                },
                {
                    "jenis": "keluaran",
                    "teks": "produksi, rollout bertahap",
                },
                {
                    "jenis": "selesai",
                    "teks": "pantau crash dan ulasan",
                },
            ],
        },
    ],
    "Verifikasi Developer Android Mulai 2026": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Pemasangan dari toko mitra sejak 30 September 2026",
            "ket": "Berlaku di Brasil, Indonesia, Singapura, dan Thailand untuk HP bersertifikat Android 7 ke atas. Pemasangan lewat ADB tetap boleh untuk uji.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "pasang dari toko mitra",
                },
                {
                    "jenis": "keputusan",
                    "teks": "HP bersertifikat, Android 7+?",
                    "ya": 2,
                    "tidak": 4,
                },
                {
                    "jenis": "keputusan",
                    "teks": "developer sudah terverifikasi?",
                    "ya": 4,
                    "tidak": 3,
                },
                {
                    "jenis": "keluaran",
                    "teks": "pemasangan ditolak",
                    "ke": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "aplikasi terpasang",
                },
                {
                    "jenis": "selesai",
                    "teks": "selesai",
                },
            ],
        },
    ],
    "App Store Connect dan TestFlight": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Satu build iOS dari laptop Fedora sampai penguji",
            "ket": "App Store di sini maksudnya App Store Connect. Tinjauan beta cuma untuk build pertama di grup eksternal; rilis ke toko tetap lewat App Review penuh.",
            "pelaku": [
                "EAS / Xcode",
                "App Store",
                "App Review",
                "penguji",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "unggah build (Xcode 26+)",
                ],
                [
                    1,
                    0,
                    "build selesai diproses",
                ],
                [
                    0,
                    1,
                    "tambah ke grup eksternal",
                ],
                [
                    1,
                    2,
                    "tinjauan beta build pertama",
                ],
                [
                    2,
                    1,
                    "disetujui",
                ],
                [
                    1,
                    3,
                    "undangan TestFlight",
                ],
                [
                    3,
                    0,
                    "masukan dan laporan crash",
                ],
                [
                    0,
                    2,
                    "kirim untuk App Review",
                ],
                [
                    2,
                    1,
                    "siap diterbitkan",
                ],
            ],
        },
    ],
    "Toko Lain: F-Droid dan Microsoft Store": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Membandingkan toko aplikasi (Oktober 2026)",
            "ket": "Biaya App Store per tahun, Play sekali bayar. Microsoft Store gratis untuk perorangan sejak September 2025.",
            "tabel": [
                {
                    "nama": "toko aplikasi",
                    "kolom": [
                        "toko",
                        "syarat utama",
                        "biaya daftar",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            "Google Play",
                            "AAB, uji 14 hr",
                            "25 dolar",
                            "Android umum",
                        ],
                        [
                            "App Store",
                            "Xcode 26",
                            "99 dolar/thn",
                            "iPhone, iPad",
                        ],
                        [
                            "F-Droid",
                            "kode terbuka",
                            "gratis",
                            "open source",
                        ],
                        [
                            "Microsoft Store",
                            "verifikasi ID",
                            "gratis (pribadi)",
                            "Windows",
                        ],
                        [
                            "Flathub",
                            "paket Flatpak",
                            "gratis",
                            "Linux",
                        ],
                    ],
                    "sorot_baris": [2],
                },
            ],
        },
    ],
    "Aturan Baru yang Bikin Tutorial Lama Menyesatkan": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Dulu dan sekarang: aturan yang paling sering bikin gagal",
            "ket": "Tanggal per Oktober 2026. Rinciannya ada di bagian-bagian materi ini.",
            "tabel": [
                {
                    "nama": "aturan berubah",
                    "kolom": [
                        "urusan",
                        "dulu",
                        "sekarang",
                        "sejak",
                    ],
                    "baris": [
                        [
                            "target API Play",
                            "35",
                            "36",
                            "31-08-2026",
                        ],
                        [
                            "rilis akun baru",
                            "langsung",
                            "12 orang 14 hari",
                            "akun >13-11-2023",
                        ],
                        [
                            "pasang di HP",
                            "bebas",
                            "dev diverifikasi",
                            "30-09-2026",
                        ],
                        [
                            "React Native",
                            "lama/baru",
                            "New Arch saja",
                            "0.82, Okt 2025",
                        ],
                        [
                            "CocoaPods trunk",
                            "terbuka",
                            "read-only",
                            "02-12-2026",
                        ],
                        [
                            "Xcode unggah",
                            "versi lama",
                            "26 ke atas",
                            "28-04-2026",
                        ],
                        [
                            "Xamarin",
                            "didukung",
                            "berakhir",
                            "01-05-2024",
                        ],
                        [
                            "FCM",
                            "server key",
                            "HTTP v1",
                            "22-07-2024",
                        ],
                    ],
                    "sorot_baris": [0, 1, 2],
                },
            ],
        },
    ],
}
