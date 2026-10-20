"""Gambar konsep kurikulum Bahasa Pemrograman Lain. Skema: inti/visual.py."""

VISUAL = {
    "Peta Paradigma Pemrograman": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Paradigma, ciri, dan contoh bahasanya",
            "tabel": [
                {
                    "kolom": [
                        "Paradigma",
                        "Ciri",
                        "Contoh",
                    ],
                    "baris": [
                        [
                            "Imperatif",
                            "ubah variabel",
                            "C, Python",
                        ],
                        [
                            "OOP",
                            "kelas/prototipe",
                            "Java, JS",
                        ],
                        [
                            "Kirim pesan",
                            "semua objek",
                            "Smalltalk",
                        ],
                        [
                            "Fungsional",
                            "rangkai fungsi",
                            "Haskell, F#",
                        ],
                        [
                            "Logika",
                            "fakta + aturan",
                            "Prolog",
                        ],
                        [
                            "Array/stack",
                            "olah sekaligus",
                            "APL, Forth",
                        ],
                        [
                            "Deklaratif",
                            "sebut hasilnya",
                            "SQL, HTML",
                        ],
                        [
                            "Visual",
                            "susun blok",
                            "Scratch",
                        ],
                    ],
                },
            ],
            "ket": "Kebanyakan bahasa modern mencampur beberapa baris dari tabel ini.",
        },
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Silsilah tiga keluarga bahasa",
            "akar": {
                "teks": "tiga keluarga",
                "anak": [
                    {
                        "teks": "Algol",
                        "anak": [
                            {
                                "teks": "C",
                                "anak": [
                                    {
                                        "teks": "C++",
                                    },
                                    {
                                        "teks": "Java",
                                    },
                                    {
                                        "teks": "C#",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "ML",
                        "anak": [
                            {
                                "teks": "Caml",
                                "anak": [
                                    {
                                        "teks": "OCaml",
                                    },
                                    {
                                        "teks": "F#",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "Lisp",
                        "anak": [
                            {
                                "teks": "Scheme",
                            },
                            {
                                "teks": "Clojure",
                            },
                        ],
                    },
                ],
            },
            "ket": "Disederhanakan: Java dan C# juga meminjam banyak dari C++ dan bahasa lain.",
        },
    ],
    "Sistem Tipe: Statis, Dinamis, Kuat, dan Bertahap": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Dua sumbu sistem tipe",
            "tabel": [
                {
                    "kolom": [
                        "Diperiksa",
                        "Kuat",
                        "Lemah",
                    ],
                    "baris": [
                        [
                            "Statis",
                            "Haskell, Rust",
                            "C",
                        ],
                        [
                            "Dinamis",
                            "Python, Ruby",
                            "JavaScript, Perl",
                        ],
                    ],
                },
            ],
            "ket": "Kuat dan lemah itu rentang, bukan dua kotak tegas. C disebut lemah karena banyak konversi otomatis.",
        },
    ],
    "Model Memori dan Mesin yang Menjalankan Kode": [
        {
            "setelah": 1,
            "jenis": "memori",
            "judul": "Variabel di stack, daftar di heap",
            "tumpukan": [
                [
                    "nilai",
                    "@L1",
                ],
                [
                    "x",
                    "90",
                ],
            ],
            "heap": [
                {
                    "id": "L1",
                    "isi": "[70, 80, 90]",
                },
            ],
            "label_tumpukan": "stack (main)",
            "label_heap": "heap",
            "ket": "Disederhanakan: di Python angka 90 juga objek di heap; yang penting nilai cuma menyimpan alamat.",
        },
        {
            "setelah": 11,
            "jenis": "alur",
            "judul": "Perjalanan kode di bahasa bermesin virtual",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "kode sumber (.kt, .cs, .ex)",
                },
                {
                    "jenis": "proses",
                    "teks": "kompilator",
                },
                {
                    "jenis": "proses",
                    "teks": "bytecode (.class, IL, .beam)",
                },
                {
                    "jenis": "proses",
                    "teks": "mesin virtual + JIT",
                },
                {
                    "jenis": "selesai",
                    "teks": "instruksi mesin di CPU",
                },
            ],
        },
    ],
    "Belajar Bahasa ke-N dengan Cepat": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Rencana seminggu untuk bahasa baru",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "hari 1: pasang dan halo dunia",
                },
                {
                    "jenis": "proses",
                    "teks": "hari 2: tipe dan koleksi",
                },
                {
                    "jenis": "proses",
                    "teks": "hari 3: fungsi dan error",
                },
                {
                    "jenis": "proses",
                    "teks": "hari 4: modul dan paket",
                },
                {
                    "jenis": "proses",
                    "teks": "hari 5: terjemahkan program kecil",
                },
                {
                    "jenis": "proses",
                    "teks": "hari 6: baca kode orang lain",
                },
                {
                    "jenis": "selesai",
                    "teks": "hari 7: proyek mini sendiri",
                },
            ],
        },
        {
            "setelah": 11,
            "jenis": "tabel",
            "judul": "Nama berkas dan perintah menjalankannya",
            "tabel": [
                {
                    "kolom": [
                        "Bahasa",
                        "Berkas",
                        "Perintah",
                    ],
                    "baris": [
                        [
                            "Lua",
                            "halo.lua",
                            "lua halo.lua",
                        ],
                        [
                            "Perl",
                            "halo.pl",
                            "perl halo.pl",
                        ],
                        [
                            "Ruby",
                            "halo.rb",
                            "ruby halo.rb",
                        ],
                        [
                            "Tcl",
                            "halo.tcl",
                            "tclsh halo.tcl",
                        ],
                        [
                            "Swift",
                            "halo.swift",
                            "swift halo.swift",
                        ],
                        [
                            "Dart",
                            "halo.dart",
                            "dart halo.dart",
                        ],
                    ],
                },
            ],
            "ket": "Lua, Perl, Ruby, dan Tcl bisa dipasang dari dnf di Fedora; Swift lewat swift-lang; Dart diunduh dari dart.dev.",
        },
    ],
    "PowerShell dan Pipeline Objek": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Objek proses mengalir lewat empat cmdlet",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Get-Process: semua objek proses",
                },
                {
                    "jenis": "proses",
                    "teks": "Where-Object CPU -gt 10",
                },
                {
                    "jenis": "proses",
                    "teks": "Sort-Object CPU -Descending",
                },
                {
                    "jenis": "proses",
                    "teks": "Select-Object -First 3 Name, CPU",
                },
                {
                    "jenis": "keluaran",
                    "teks": "tabel teks di layar",
                },
            ],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Bash dan PowerShell untuk pekerjaan yang sama",
            "tabel": [
                {
                    "kolom": [
                        "Pekerjaan",
                        "Bash",
                        "PowerShell",
                    ],
                    "baris": [
                        [
                            "Isi pipeline",
                            "teks",
                            "objek .NET",
                        ],
                        [
                            "Saring",
                            "grep, awk",
                            "Where-Object",
                        ],
                        [
                            "Urutkan",
                            "sort",
                            "Sort-Object",
                        ],
                        [
                            "Pilih kolom",
                            "cut, awk",
                            "Select-Object",
                        ],
                        [
                            "Hitung baris",
                            "wc -l",
                            "Measure-Object",
                        ],
                        [
                            "Lebih dari",
                            "-gt (di test)",
                            "-gt",
                        ],
                    ],
                },
            ],
        },
    ],
    "PowerShell untuk Skrip Otomasi Sehari-hari": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Kata kerja cmdlet yang paling sering dipakai",
            "tabel": [
                {
                    "kolom": [
                        "Kata kerja",
                        "Artinya",
                        "Contoh",
                    ],
                    "baris": [
                        [
                            "Get",
                            "ambil, baca",
                            "Get-ChildItem",
                        ],
                        [
                            "Set",
                            "ubah nilai",
                            "Set-Content",
                        ],
                        [
                            "New",
                            "buat baru",
                            "New-Item",
                        ],
                        [
                            "Remove",
                            "hapus",
                            "Remove-Item",
                        ],
                        [
                            "Invoke",
                            "jalankan",
                            "Invoke-Command",
                        ],
                        [
                            "Start",
                            "mulai",
                            "Start-Process",
                        ],
                        [
                            "Stop",
                            "hentikan",
                            "Stop-Process",
                        ],
                    ],
                },
            ],
            "ket": "Daftar lengkap kata kerja resmi bisa dilihat dengan perintah Get-Verb.",
        },
    ],
    "Perl: Regex dan Olah Teks": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Sigil Perl dan artinya",
            "tabel": [
                {
                    "kolom": [
                        "Ditulis",
                        "Artinya",
                        "Contoh",
                    ],
                    "baris": [
                        [
                            "$nama",
                            "skalar",
                            "\"Ani\"",
                        ],
                        [
                            "@nilai",
                            "array",
                            "(70, 85, 90)",
                        ],
                        [
                            "%umur",
                            "hash",
                            "(ani => 17)",
                        ],
                        [
                            "$nilai[0]",
                            "elemen array",
                            "70",
                        ],
                        [
                            "$umur{budi}",
                            "nilai hash",
                            "18",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Bahasa Skrip: Awk, Tcl, Raku, Batch, VBScript": [
        {
            "setelah": 10,
            "jenis": "tabel",
            "judul": "Lima bahasa skrip: tempat hidup dan statusnya",
            "tabel": [
                {
                    "kolom": [
                        "Bahasa",
                        "Hidup di",
                        "Status",
                        "Pengganti",
                    ],
                    "baris": [
                        [
                            "Awk",
                            "terminal Unix",
                            "matang",
                            "tetap dipakai",
                        ],
                        [
                            "Tcl",
                            "alat chip, tes",
                            "matang",
                            "Python",
                        ],
                        [
                            "Raku",
                            "parsing teks",
                            "komunitas kecil",
                            "Python, Perl",
                        ],
                        [
                            "Batch",
                            "cmd Windows",
                            "menurun",
                            "PowerShell",
                        ],
                        [
                            "VBScript",
                            "Windows lama",
                            "usang",
                            "PowerShell",
                        ],
                    ],
                },
            ],
        },
    ],
    "Lua: Table, Fungsi, dan Indeks dari Satu": [
        {
            "setelah": 4,
            "jenis": "larik",
            "judul": "Table {70, 80, 90} dengan indeks Lua",
            "nama": "nilai",
            "isi": [
                "70",
                "80",
                "90",
            ],
            "penunjuk": {
                "[1]": 0,
                "[2]": 1,
                "[3]": 2,
            },
            "ket": "Indeks pertama 1, jadi nilai[1] = 70 dan #nilai = 3. nilai[0] menghasilkan nil.",
        },
    ],
    "Lua Lanjut: Metatable, Closure, dan Coroutine": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Pencarian k.kaki menelusuri rantai __index",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "baca k.kaki",
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada di table k?",
                    "ya": 5,
                    "tidak": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada di Kucing?",
                    "ya": 5,
                    "tidak": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada di Hewan?",
                    "ya": 5,
                    "tidak": 4,
                },
                {
                    "jenis": "selesai",
                    "teks": "hasilnya nil",
                },
                {
                    "jenis": "selesai",
                    "teks": "pakai nilai yang ketemu",
                },
            ],
            "ket": "Untuk k.kaki, jawabannya ketemu di Hewan: 4. Untuk k.sayap, semua jawaban tidak, jadi nil.",
        },
        {
            "setelah": 8,
            "jenis": "urutan",
            "judul": "main dan coroutine bergantian",
            "pelaku": [
                "main",
                "coroutine",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "resume()",
                ],
                [
                    1,
                    0,
                    "yield(1)",
                ],
                [
                    0,
                    1,
                    "resume()",
                ],
                [
                    1,
                    0,
                    "yield(2)",
                ],
                [
                    0,
                    1,
                    "resume()",
                ],
                [
                    1,
                    0,
                    "yield(3)",
                ],
                [
                    0,
                    1,
                    "resume()",
                ],
                [
                    1,
                    0,
                    "return \"habis\"",
                ],
            ],
        },
    ],
    "GDScript: Node, Signal, dan Game Loop di Godot": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Scene tree sebuah level sederhana",
            "akar": {
                "teks": "Main (Node2D)",
                "anak": [
                    {
                        "teks": "Pemain",
                        "anak": [
                            {
                                "teks": "Sprite2D",
                            },
                            {
                                "teks": "CollisionShape2D",
                            },
                        ],
                    },
                    {
                        "teks": "Koin (Area2D)",
                        "anak": [
                            {
                                "teks": "Sprite2D",
                            },
                        ],
                    },
                    {
                        "teks": "HUD",
                        "anak": [
                            {
                                "teks": "Label",
                            },
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Satu putaran game loop",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "baca input pemain",
                },
                {
                    "jenis": "proses",
                    "teks": "perbarui posisi (x delta)",
                },
                {
                    "jenis": "proses",
                    "teks": "cek tabrakan, pancarkan signal",
                },
                {
                    "jenis": "keluaran",
                    "teks": "gambar frame ke layar",
                    "ke": 0,
                },
            ],
        },
    ],
    "Peta Skrip Game: Luau, GML, dan Haxe": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Bahasa skrip game dan engine-nya",
            "tabel": [
                {
                    "kolom": [
                        "Bahasa",
                        "Engine",
                        "Lisensi engine",
                        "Cocok untuk",
                    ],
                    "baris": [
                        [
                            "Luau",
                            "Roblox Studio",
                            "proprietary",
                            "game di Roblox",
                        ],
                        [
                            "GDScript",
                            "Godot",
                            "MIT",
                            "indie 2D dan 3D",
                        ],
                        [
                            "GML",
                            "GameMaker",
                            "proprietary",
                            "game 2D",
                        ],
                        [
                            "Haxe",
                            "Heaps, OpenFL",
                            "MIT",
                            "lintas platform",
                        ],
                        [
                            "Lua",
                            "Love2D, Defold",
                            "zlib, Defold",
                            "2D ringan, mod",
                        ],
                    ],
                },
            ],
            "ket": "Lisensi Defold memakai lisensinya sendiri yang berbasis Apache 2.0.",
        },
    ],
    "Swift: Optional, Struct, dan Protokol": [
        {
            "setelah": 3,
            "jenis": "variabel",
            "judul": "Optional berisi nilai dan optional kosong",
            "isi": [
                [
                    "umur",
                    "17",
                    "Int",
                ],
                [
                    "angka",
                    "nil",
                    "Int?",
                ],
                [
                    "nama",
                    "\"Budi\"",
                    "String?",
                ],
            ],
            "sorot": [
                "angka",
            ],
            "ket": "Int? boleh nil, Int tidak. Untuk memakai isi angka, buka dulu dengan if let, guard let, atau ??.",
        },
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "struct dan class di Swift",
            "tabel": [
                {
                    "kolom": [
                        "Hal",
                        "struct",
                        "class",
                    ],
                    "baris": [
                        [
                            "Saat b = a",
                            "disalin",
                            "berbagi objek",
                        ],
                        [
                            "Pewarisan",
                            "tidak bisa",
                            "bisa",
                        ],
                        [
                            "deinit",
                            "tidak ada",
                            "ada",
                        ],
                        [
                            "Ubah di let",
                            "tidak boleh",
                            "properti boleh",
                        ],
                        [
                            "Contoh bawaan",
                            "String, Array",
                            "UIViewController",
                        ],
                    ],
                },
            ],
        },
    ],
    "Swift Lanjut: Konkurensi dan Warisan Objective-C": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Dua tugas mengakses actor bergiliran",
            "pelaku": [
                "tugas A",
                "actor Rekening",
                "tugas B",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "await setor(1)",
                ],
                [
                    2,
                    1,
                    "await setor(1), antre",
                ],
                [
                    1,
                    0,
                    "selesai, saldo 1",
                ],
                [
                    1,
                    2,
                    "giliranmu, saldo 2",
                ],
            ],
        },
        {
            "setelah": 8,
            "jenis": "tabel",
            "judul": "Hal yang sama di Swift dan Objective-C",
            "tabel": [
                {
                    "kolom": [
                        "Hal",
                        "Swift",
                        "Objective-C",
                    ],
                    "baris": [
                        [
                            "Panggil metode",
                            "p.tambah(10)",
                            "[p tambah:10]",
                        ],
                        [
                            "Buat objek",
                            "Pemain()",
                            "[Pemain new]",
                        ],
                        [
                            "Teks",
                            "\"Ani\"",
                            "@\"Ani\"",
                        ],
                        [
                            "Kosong",
                            "nil (Optional)",
                            "nil (bebas)",
                        ],
                        [
                            "Cetak",
                            "print()",
                            "NSLog()",
                        ],
                        [
                            "Berkas",
                            "satu .swift",
                            ".h dan .m",
                        ],
                    ],
                },
            ],
        },
    ],
    "Dart: Null Safety, Kelas, dan Async": [
        {
            "setelah": 3,
            "jenis": "variabel",
            "judul": "String dan String? di Dart",
            "isi": [
                [
                    "nama",
                    "\"Budi\"",
                    "String",
                ],
                [
                    "kota",
                    "null",
                    "String?",
                ],
            ],
            "sorot": [
                "kota",
            ],
            "ket": "kota boleh null karena tipenya String?. Memanggil kota.length langsung ditolak kompilator; pakai kota?.length.",
        },
    ],
    "Dart Lanjut: Event Loop, Stream, dan Isolate": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "mode": "antrean",
            "judul": "Urutan kerja sesudah main selesai",
            "isi": [
                "micro 3",
                "micro 4",
                "event 5",
                "event 6",
            ],
            "label": "microtask selalu duluan",
            "ket": "Dua antrean digambar sebagai satu urutan kerja: seluruh antrean microtask dikosongkan dulu, baru event pertama diambil.",
        },
        {
            "setelah": 9,
            "jenis": "pohon",
            "judul": "Pohon widget layar Toko Kopi",
            "akar": {
                "teks": "MaterialApp",
                "anak": [
                    {
                        "teks": "Scaffold",
                        "anak": [
                            {
                                "teks": "AppBar",
                                "anak": [
                                    {
                                        "teks": "Text",
                                    },
                                ],
                            },
                            {
                                "teks": "Center",
                                "anak": [
                                    {
                                        "teks": "Column",
                                        "anak": [
                                            {
                                                "teks": "Text",
                                            },
                                            {
                                                "teks": "ElevatedButton",
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
    "R: Vektor, Data Frame, dan Statistik Dasar": [
        {
            "setelah": 4,
            "jenis": "larik",
            "judul": "c(10, 20) didaur ulang jadi 10 20 10 20",
            "ket": "Dua elemen terakhir adalah salinan. Hasil c(1, 2, 3, 4) + c(10, 20) jadi 11 22 13 24, tanpa peringatan karena 4 habis dibagi 2.",
            "nama": "c(10, 20)",
            "isi": [
                "10",
                "20",
                "10",
                "20",
            ],
            "rentang": [2, 4],
        },
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Data frame siswa: tiap kolom satu vektor",
            "ket": "Kolom kelas bertipe factor dengan levels A dan B.",
            "tabel": [
                {
                    "nama": "siswa",
                    "kolom": [
                        "baris",
                        "nama",
                        "nilai",
                        "kelas",
                    ],
                    "baris": [
                        [
                            "1",
                            "Ani",
                            "85",
                            "A",
                        ],
                        [
                            "2",
                            "Budi",
                            "70",
                            "B",
                        ],
                        [
                            "3",
                            "Citra",
                            "92",
                            "A",
                        ],
                    ],
                    "sorot_baris": [0, 2],
                },
            ],
        },
    ],
    "R Lanjut: Pipe, Tidyverse, dan ggplot2": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Satu pipeline dplyr dibaca dari atas ke bawah",
            "ket": "Setiap langkah menerima tabel dari langkah sebelumnya dan menyerahkan tabel baru ke langkah berikutnya.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "nilai.csv",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "filter(hadir >= 10)",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "mutate(akhir = ...)",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "group_by(kelas)",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "summarise(rata, n)",
                    "ke": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "arrange(desc(rata))",
                },
            ],
        },
    ],
    "MATLAB dan GNU Octave: Berpikir dalam Matriks": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "A * B dan A .* B untuk A = [1 2; 3 4], B = [5 6; 7 8]",
            "ket": "Kiri: baris kali kolom lalu dijumlahkan (1*5 + 2*7 = 19). Kanan: elemen dengan posisi sama dikalikan (1*5 = 5).",
            "tabel": [
                {
                    "nama": "A * B",
                    "kolom": [
                        "baris",
                        "kolom 1",
                        "kolom 2",
                    ],
                    "baris": [
                        [
                            "1",
                            "19",
                            "22",
                        ],
                        [
                            "2",
                            "43",
                            "50",
                        ],
                    ],
                },
                {
                    "nama": "A .* B",
                    "kolom": [
                        "baris",
                        "kolom 1",
                        "kolom 2",
                    ],
                    "baris": [
                        [
                            "1",
                            "5",
                            "12",
                        ],
                        [
                            "2",
                            "21",
                            "32",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Bahasa Sains dan Bahasa Array": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Enam bahasa sains: bidang, lisensi, dan cara mencoba",
            "ket": "Status per Oktober 2026. Yang proprietary tetap punya jalur gratis untuk belajar.",
            "tabel": [
                {
                    "kolom": [
                        "bahasa",
                        "bidang",
                        "lisensi",
                        "coba gratis",
                    ],
                    "baris": [
                        [
                            "Julia",
                            "numerik, iklim",
                            "MIT",
                            "juliaup / dnf",
                        ],
                        [
                            "Fortran",
                            "cuaca, fisika",
                            "GPL (gfortran)",
                            "dnf",
                        ],
                        [
                            "SAS",
                            "farmasi, bank",
                            "proprietary",
                            "OnDemand",
                        ],
                        [
                            "Wolfram",
                            "simbolik",
                            "proprietary",
                            "Wolfram Engine",
                        ],
                        [
                            "APL",
                            "keuangan",
                            "Dyalog / GPL",
                            "TryAPL",
                        ],
                        [
                            "q",
                            "data pasar",
                            "proprietary",
                            "KDB-X Community",
                        ],
                    ],
                },
            ],
        },
    ],
    "Scala: Fungsional dan OOP di JVM": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "sealed trait Bentuk dan tiga case class turunannya",
            "ket": "Karena sealed, kompilator tahu cuma ada tiga turunan dan bisa memperingatkan match yang lupa satu cabang.",
            "akar": {
                "teks": "trait Bentuk",
                "anak": [
                    {
                        "teks": "Lingkaran(r)",
                    },
                    {
                        "teks": "Persegi(sisi)",
                    },
                    {
                        "teks": "Segitiga(a, b, c)",
                    },
                ],
            },
        },
    ],
    "Groovy: Bahasa di Balik Jenkinsfile dan Gradle": [
        {
            "setelah": 6,
            "jenis": "alur",
            "judul": "Tahap pipeline Jenkins dari Jenkinsfile di atas",
            "ket": "Tahap Deploy cuma jalan di cabang main. Kalau satu tahap gagal, tahap berikutnya nggak dijalankan dan blok post failure aktif.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "push ke repositori",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Checkout",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Build",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Test",
                    "ke": 4,
                },
                {
                    "jenis": "keputusan",
                    "teks": "cabang main?",
                    "ya": 5,
                    "tidak": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "Deploy",
                    "ke": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "selesai",
                },
            ],
        },
    ],
    "F#: Pemrograman Fungsional di .NET": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Teks mengalir lewat pipe |> sampai jadi daftar hitungan",
            "ket": "Setiap tahap menerima hasil tahap sebelumnya. Kata teh terbuang di tahap saring karena cuma tiga huruf.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "teks satu baris",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Split(' '): pisah kata",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "filter: lebih dari 3 huruf",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "countBy id: hitung",
                    "ke": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "sortByDescending snd",
                },
            ],
        },
    ],
    "Elixir: Pattern Matching dan Operator Pipe": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Pola di kiri, nilai di kanan: cocok atau MatchError",
            "ket": "Kalau cocok, variabel di pola diikat ke bagian nilai yang posisinya sama.",
            "tabel": [
                {
                    "kolom": [
                        "pola",
                        "nilai",
                        "hasil",
                    ],
                    "baris": [
                        [
                            "{:ok, x}",
                            "{:ok, 42}",
                            "cocok, x = 42",
                        ],
                        [
                            "{:ok, x}",
                            "{:error, :e}",
                            "MatchError",
                        ],
                        [
                            "[h | t]",
                            "[1, 2, 3]",
                            "h=1, t=[2, 3]",
                        ],
                        [
                            "%{nama: n}",
                            "%{nama: \"Ani\"}",
                            "n = \"Ani\"",
                        ],
                        [
                            "^y  (y = 5)",
                            "5",
                            "cocok",
                        ],
                        [
                            "^y  (y = 5)",
                            "6",
                            "MatchError",
                        ],
                    ],
                    "sorot_baris": [1, 5],
                },
            ],
        },
    ],
    "Elixir dan OTP: Proses, Pesan, dan Supervisor": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "call menunggu jawaban, cast nggak menunggu",
            "ket": "Pesan di kotak surat GenServer dilayani satu per satu, jadi keadaannya nggak pernah ditimpa dua pemanggil sekaligus.",
            "pelaku": [
                "klien",
                "Penghitung",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "cast {:tambah, 5}",
                ],
                [
                    0,
                    1,
                    "cast {:tambah, 10}",
                ],
                [
                    0,
                    1,
                    "call :nilai",
                ],
                [
                    1,
                    0,
                    "reply 15",
                ],
            ],
        },
        {
            "setelah": 6,
            "jenis": "pohon",
            "judul": "Supervision tree: supervisor mengawasi anak-anaknya",
            "ket": "Kalau satu pekerja mati, cuma dia yang dihidupkan ulang (one_for_one). Supervisor sendiri diawasi supervisor di atasnya.",
            "akar": {
                "teks": "Supervisor utama",
                "anak": [
                    {
                        "teks": "Penghitung",
                    },
                    {
                        "teks": "Supervisor room",
                        "anak": [
                            {
                                "teks": "room #1",
                            },
                            {
                                "teks": "room #2",
                            },
                        ],
                    },
                    {
                        "teks": "Pengambil kurs",
                    },
                ],
            },
        },
    ],
    "Peta BEAM: Erlang dan Gleam": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Tiga bahasa, satu mesin BEAM",
            "ket": "Semuanya memakai OTP dan bisa saling memanggil. Versi per Oktober 2026.",
            "tabel": [
                {
                    "kolom": [
                        "ciri",
                        "Erlang",
                        "Elixir",
                        "Gleam",
                    ],
                    "baris": [
                        [
                            "lahir",
                            "1986",
                            "2012",
                            "1.0 tahun 2024",
                        ],
                        [
                            "tipe",
                            "dinamis",
                            "dinamis",
                            "statis",
                        ],
                        [
                            "sintaks",
                            "mirip Prolog",
                            "mirip Ruby",
                            "mirip Rust",
                        ],
                        [
                            "target",
                            "BEAM",
                            "BEAM",
                            "BEAM dan JS",
                        ],
                        [
                            "kapan pilih",
                            "sistem lama",
                            "web, real-time",
                            "tipe ketat",
                        ],
                    ],
                },
            ],
        },
    ],
    "Haskell: Fungsi Murni, Tipe, dan Evaluasi Malas": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Evaluasi segera vs malas untuk take 3 (map kuadrat [1 ..])",
            "ket": "Bahasa yang menghitung segera mencoba membuat seluruh list dulu dan nggak pernah selesai. Haskell cuma menghitung tiga elemen.",
            "tabel": [
                {
                    "kolom": [
                        "langkah",
                        "segera",
                        "malas",
                    ],
                    "baris": [
                        [
                            "1",
                            "buat semua dulu",
                            "minta elemen 1",
                        ],
                        [
                            "2",
                            "nggak selesai",
                            "1 * 1 = 1",
                        ],
                        [
                            "3",
                            "-",
                            "minta 2 dan 3",
                        ],
                        [
                            "4",
                            "-",
                            "hasil [1,4,9]",
                        ],
                    ],
                },
            ],
        },
    ],
    "Haskell Lanjut: Maybe, Typeclass, dan Monad IO": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Rantai Maybe berhenti di Nothing pertama",
            "ket": "Untuk teks \"abc\", bacaUmur sudah memberi Nothing, jadi cekUmur dan perhitungan tahun lahir nggak pernah dijalankan.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "teks umur",
                    "ke": 1,
                },
                {
                    "jenis": "keputusan",
                    "teks": "bacaUmur: Just u?",
                    "ya": 2,
                    "tidak": 4,
                },
                {
                    "jenis": "keputusan",
                    "teks": "cekUmur: 0..150?",
                    "ya": 3,
                    "tidak": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Just (2026 - u)",
                },
                {
                    "jenis": "keluaran",
                    "teks": "Nothing",
                },
            ],
        },
    ],
    "Peta Fungsional dan Transpiler JavaScript": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Silsilah: keluarga ML dan keluarga Haskell",
            "ket": "Elm terinspirasi Haskell dan ML tanpa turunan langsung; CoffeeScript dan Roc berdiri di luar kedua pohon ini.",
            "akar": {
                "teks": "ML (1973)",
                "anak": [
                    {
                        "teks": "Caml (1985)",
                        "anak": [
                            {
                                "teks": "OCaml",
                                "anak": [
                                    {
                                        "teks": "ReScript",
                                    },
                                    {
                                        "teks": "F# (terinspirasi)",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "Haskell (1990)",
                        "anak": [
                            {
                                "teks": "PureScript",
                            },
                            {
                                "teks": "Elm (terinspirasi)",
                            },
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 11,
            "jenis": "tabel",
            "judul": "Tujuh bahasa: target dan status per Oktober 2026",
            "tabel": [
                {
                    "kolom": [
                        "bahasa",
                        "target",
                        "versi",
                        "status",
                    ],
                    "baris": [
                        [
                            "OCaml",
                            "kode mesin",
                            "5.5.1",
                            "aktif",
                        ],
                        [
                            "Caml Light",
                            "bytecode",
                            "0.75 (2002)",
                            "usang",
                        ],
                        [
                            "Elm",
                            "JavaScript",
                            "0.19.3",
                            "stabil, kecil",
                        ],
                        [
                            "PureScript",
                            "JavaScript",
                            "0.15.16",
                            "stabil, niche",
                        ],
                        [
                            "ReScript",
                            "JavaScript",
                            "12.3.1",
                            "aktif",
                        ],
                        [
                            "CoffeeScript",
                            "JavaScript",
                            "2.7.0 (2022)",
                            "usang",
                        ],
                        [
                            "Roc",
                            "kode mesin",
                            "belum 0.1",
                            "eksperimen",
                        ],
                    ],
                },
            ],
        },
    ],
    "Keluarga Lisp: Common Lisp, Scheme, Racket, Clojure": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Pohon sintaks dari (+ 1 (* 2 3))",
            "ket": "Setiap kurung jadi satu simpul. Lisp menghitung dari daun ke akar: (* 2 3) jadi 6, lalu (+ 1 6) jadi 7.",
            "akar": {
                "teks": "+",
                "anak": [
                    {
                        "teks": "1",
                    },
                    {
                        "teks": "*",
                        "anak": [
                            {
                                "teks": "2",
                            },
                            {
                                "teks": "3",
                            },
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Empat dialek Lisp per Oktober 2026",
            "ket": "Semuanya memakai S-expression dan macro; bedanya di ukuran bahasa, tempat jalan, dan komunitas.",
            "tabel": [
                {
                    "kolom": [
                        "dialek",
                        "berjalan di",
                        "versi",
                        "kegunaan",
                    ],
                    "baris": [
                        [
                            "Common Lisp",
                            "native (SBCL)",
                            "SBCL 2.6.9",
                            "umum, REPL",
                        ],
                        [
                            "Scheme",
                            "Guile, Chez",
                            "R7RS-small",
                            "pendidikan",
                        ],
                        [
                            "Racket",
                            "Racket CS",
                            "9.3",
                            "bahasa baru",
                        ],
                        [
                            "Clojure",
                            "JVM / JS",
                            "1.12.6",
                            "backend, data",
                        ],
                    ],
                },
            ],
        },
    ],
    "Prolog dan Lean: Logika yang Bisa Dijalankan": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Pohon pencarian untuk ?- kakek(budi, Cucu).",
            "ket": "Prolog menelusuri cabang dari kiri. Sesudah menemukan citra, ia mundur (backtracking) ke pilihan Y berikutnya.",
            "akar": {
                "teks": "kakek(budi, Cucu)",
                "anak": [
                    {
                        "teks": "Y = ani",
                        "anak": [
                            {
                                "teks": "Cucu = citra",
                            },
                        ],
                    },
                    {
                        "teks": "Y = dodi",
                        "anak": [
                            {
                                "teks": "Cucu = eka",
                            },
                            {
                                "teks": "Cucu = fajar",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Assembly: Register, Instruksi, dan Syscall": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Isi register tepat saat syscall write dipanggil",
            "ket": "rax memilih layanan, rdi berkas tujuan, rsi menunjuk ke teks di bagian data, rdx banyaknya byte yang ditulis.",
            "tumpukan": [
                [
                    "rax",
                    "1 (write)",
                ],
                [
                    "rdi",
                    "1 (stdout)",
                ],
                [
                    "rsi",
                    "@P",
                ],
                [
                    "rdx",
                    "13",
                ],
            ],
            "heap": [
                {
                    "id": "P",
                    "isi": "\"Halo, Dunia!\" + 10",
                },
            ],
            "label_tumpukan": "register",
            "label_heap": "section .data",
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Register untuk syscall di Linux x86-64",
            "tabel": [
                {
                    "kolom": [
                        "register",
                        "peran",
                        "write",
                        "exit",
                    ],
                    "baris": [
                        [
                            "rax",
                            "nomor syscall",
                            "1",
                            "60",
                        ],
                        [
                            "rdi",
                            "argumen 1",
                            "1 (stdout)",
                            "kode keluar",
                        ],
                        [
                            "rsi",
                            "argumen 2",
                            "alamat teks",
                            "-",
                        ],
                        [
                            "rdx",
                            "argumen 3",
                            "13 (panjang)",
                            "-",
                        ],
                    ],
                },
            ],
        },
    ],
    "Assembly Lanjut: Stack, Fungsi, dan Konvensi Panggilan": [
        {
            "setelah": 6,
            "jenis": "tumpukan",
            "judul": "Saat faktorial(1) berjalan, ada empat frame di stack",
            "ket": "Tiap frame menyimpan alamat balik, rbp pemanggil, n, dan hasil. Frame paling atas selesai duluan.",
            "mode": "tumpukan",
            "isi": [
                "main",
                "faktorial(3)",
                "faktorial(2)",
                "faktorial(1)",
            ],
            "label": "stack (rsp di puncak)",
            "operasi": "ret: frame dibuang",
        },
    ],
    "Zig: Alokator Eksplisit dan comptime": [
        {
            "setelah": 3,
            "jenis": "memori",
            "judul": "alloc meminta 5 x u32 di heap, defer membebaskannya",
            "ket": "angka di stack cuma berisi penunjuk dan panjang. Isi 0, 1, 4, 9, 16 tinggal di heap sampai defer menjalankan free.",
            "tumpukan": [
                [
                    "alokator",
                    "init.gpa",
                ],
                [
                    "angka",
                    "@B",
                ],
            ],
            "heap": [
                {
                    "id": "B",
                    "isi": "{ 0, 1, 4, 9, 16 }",
                },
            ],
            "label_tumpukan": "stack main",
            "label_heap": "heap",
        },
        {
            "setelah": 14,
            "jenis": "tabel",
            "judul": "C, Zig, dan Rust menangani memori dan error",
            "tabel": [
                {
                    "kolom": [
                        "hal",
                        "C",
                        "Zig",
                        "Rust",
                    ],
                    "baris": [
                        [
                            "memori heap",
                            "malloc/free",
                            "alokator+defer",
                            "kepemilikan",
                        ],
                        [
                            "error",
                            "kode -1/NULL",
                            "error union",
                            "Result, ?",
                        ],
                        [
                            "generik",
                            "makro",
                            "comptime",
                            "trait",
                        ],
                        [
                            "status",
                            "standar ISO",
                            "belum 1.0",
                            "stabil (2015)",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Bahasa Sistem Generasi Baru": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Sepuluh bahasa sistem generasi baru (Oktober 2026)",
            "ket": "Tabel atas: sudah 1.0 atau punya standar resmi. Kolom memori menyebut siapa yang membersihkan heap.",
            "tabel": [
                {
                    "nama": "sudah stabil",
                    "kolom": [
                        "bahasa",
                        "versi",
                        "memori",
                        "pemakaian",
                    ],
                    "baris": [
                        [
                            "Ada",
                            "Ada 2022",
                            "manual/lingkup",
                            "avionik, kereta",
                        ],
                        [
                            "D",
                            "DMD 2.113.0",
                            "GC opsional",
                            "alat, game",
                        ],
                        [
                            "Nim",
                            "2.2.12",
                            "ORC",
                            "CLI, Ethereum",
                        ],
                        [
                            "Crystal",
                            "1.22.0",
                            "GC",
                            "backend web",
                        ],
                        [
                            "Mojo",
                            "1.1.0",
                            "kepemilikan",
                            "kernel AI, GPU",
                        ],
                    ],
                },
                {
                    "nama": "belum 1.0",
                    "kolom": [
                        "bahasa",
                        "versi",
                        "memori",
                        "pemakaian",
                    ],
                    "baris": [
                        [
                            "Odin",
                            "dev-2026-10",
                            "manual",
                            "game, grafis",
                        ],
                        [
                            "V",
                            "0.5.2",
                            "GC (bawaan)",
                            "alat kecil",
                        ],
                        [
                            "MoonBit",
                            "0.9 beta",
                            "ikut target",
                            "WebAssembly",
                        ],
                        [
                            "Carbon",
                            "0.0.0 nightly",
                            "manual (C++)",
                            "eksperimen",
                        ],
                        [
                            "Forth",
                            "Gforth 0.7.3",
                            "manual",
                            "firmware lama",
                        ],
                    ],
                },
            ],
        },
    ],
    "COBOL: Bahasa Transaksi yang Masih Bekerja": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Empat DIVISION selalu muncul dengan urutan ini",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "IDENTIFICATION: nama program",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "ENVIRONMENT: berkas, perangkat",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "DATA: variabel dan record",
                    "ke": 3,
                },
                {
                    "jenis": "selesai",
                    "teks": "PROCEDURE: langkah program",
                },
            ],
        },
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "PIC menentukan lebar dan arti setiap field",
            "tabel": [
                {
                    "kolom": [
                        "PIC",
                        "lebar",
                        "contoh isi",
                        "artinya",
                    ],
                    "baris": [
                        [
                            "9(6)",
                            "6",
                            "000123",
                            "123",
                        ],
                        [
                            "X(10)",
                            "10",
                            "BUDI______",
                            "BUDI + 6 spasi",
                        ],
                        [
                            "9(7)V99",
                            "9",
                            "001234567",
                            "12345.67",
                        ],
                        [
                            "9(5)",
                            "5",
                            "34567",
                            "dari 1234567",
                        ],
                        [
                            "Z,ZZZ,ZZ9.99",
                            "12",
                            "___12,345.67",
                            "untuk dicetak",
                        ],
                    ],
                },
            ],
        },
    ],
    "VBA: Makro untuk Excel dan Office": [
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Model objek Excel: dari Application sampai sel",
            "ket": "Kumpulan Worksheets berisi lembar Data dan Grafik. Range dan Cells menunjuk sel di dalam satu lembar.",
            "akar": {
                "teks": "Application",
                "anak": [
                    {
                        "teks": "Workbooks",
                        "anak": [
                            {
                                "teks": "lap.xlsm",
                                "anak": [
                                    {
                                        "teks": "Worksheet Data",
                                        "anak": [
                                            {
                                                "teks": "Range(\"B2:B5\")",
                                            },
                                            {
                                                "teks": "Cells(2, 2)",
                                            },
                                        ],
                                    },
                                    {
                                        "teks": "Worksheet Grafik",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Peta Bahasa Enterprise: ABAP, Apex, X++, RPG, PL/I": [
        {
            "setelah": 12,
            "jenis": "tabel",
            "judul": "Lima bahasa enterprise dan cara mencobanya",
            "tabel": [
                {
                    "kolom": [
                        "bahasa",
                        "platform",
                        "coba gratis",
                        "status",
                    ],
                    "baris": [
                        [
                            "ABAP",
                            "SAP S/4HANA",
                            "trial SAP BTP",
                            "aktif",
                        ],
                        [
                            "Apex",
                            "Salesforce",
                            "Developer Ed.",
                            "aktif",
                        ],
                        [
                            "X++",
                            "Dynamics 365",
                            "lisensi/mitra",
                            "aktif",
                        ],
                        [
                            "RPG",
                            "IBM i",
                            "PUB400.com",
                            "menurun",
                        ],
                        [
                            "PL/I",
                            "z/OS mainframe",
                            "nggak umum",
                            "menurun",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Dialek SQL Prosedural: PL/SQL, T-SQL, PL/pgSQL": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Konsep yang sama di tiga dialek prosedural",
            "tabel": [
                {
                    "kolom": [
                        "hal",
                        "PL/SQL",
                        "T-SQL",
                        "PL/pgSQL",
                    ],
                    "baris": [
                        [
                            "mengisi",
                            ":=",
                            "SET @x =",
                            ":=",
                        ],
                        [
                            "baris kena",
                            "SQL%ROWCOUNT",
                            "@@ROWCOUNT",
                            "GET DIAGNOSTICS",
                        ],
                        [
                            "mencetak",
                            "DBMS_OUTPUT",
                            "PRINT",
                            "RAISE NOTICE",
                        ],
                        [
                            "gabung teks",
                            "||",
                            "+",
                            "||",
                        ],
                        [
                            "batasi baris",
                            "FETCH FIRST n",
                            "TOP n",
                            "LIMIT n",
                        ],
                        [
                            "pemisah blok",
                            "/",
                            "GO",
                            "$$ ... $$",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Kode Warisan: Delphi, VB6, FoxPro, CFML, ActionScript": [
        {
            "setelah": 13,
            "jenis": "tabel",
            "judul": "Enam bahasa warisan: status dan jalur migrasinya",
            "tabel": [
                {
                    "kolom": [
                        "bahasa",
                        "era",
                        "status",
                        "migrasi umum",
                    ],
                    "baris": [
                        [
                            "Delphi",
                            "1995-kini",
                            "aktif",
                            "tetap / C#",
                        ],
                        [
                            "VB6",
                            "1991-1998",
                            "usang",
                            "VB.NET / C#",
                        ],
                        [
                            "Visual FoxPro",
                            "1995-2007",
                            "usang (2015)",
                            "web+PostgreSQL",
                        ],
                        [
                            "CFML",
                            "1995-kini",
                            "menurun",
                            "PHP, Node, Java",
                        ],
                        [
                            "ActionScript 3",
                            "2006-2020",
                            "usang",
                            "JS, engine",
                        ],
                        [
                            "Hack",
                            "2014-2023",
                            "tanpa rilis",
                            "PHP bertipe",
                        ],
                    ],
                },
            ],
        },
    ],
    "Verilog dan VHDL: Menulis Rangkaian sebagai Kode": [
        {
            "setelah": 4,
            "jenis": "bit",
            "judul": "Kolom s di tabel kebenaran half adder dibaca dari atas: 0110",
            "ket": "Untuk ab = 00, 01, 10, 11, nilai s adalah 0, 1, 1, 0. Dibaca sebagai bilangan 4 bit, itu angka 6.",
            "angka": 6,
            "lebar": 4,
            "label": "s untuk ab = 00,01,10,11",
        },
        {
            "setelah": 8,
            "jenis": "alur",
            "judul": "Dari kode HDL sampai rangkaian di FPGA",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "tulis kode Verilog/VHDL",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "simulasi + testbench",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "keluaran sesuai?",
                    "ya": 3,
                    "tidak": 0,
                },
                {
                    "jenis": "proses",
                    "teks": "sintesis jadi gerbang",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "place and route",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "berkas konfigurasi ke FPGA",
                },
            ],
        },
    ],
    "MicroPython: Python di Mikrokontroler": [
        {
            "setelah": 6,
            "jenis": "urutan",
            "judul": "mpremote menyalin berkas, menjalankannya, dan membawa keluaran balik",
            "pelaku": [
                "laptop",
                "mpremote",
                "papan ESP32",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "mpremote fs cp main.py :",
                ],
                [
                    1,
                    2,
                    "kirim isi main.py lewat USB",
                ],
                [
                    2,
                    1,
                    "berkas tersimpan di flash",
                ],
                [
                    0,
                    1,
                    "mpremote run coba.py",
                ],
                [
                    1,
                    2,
                    "jalankan coba.py",
                ],
                [
                    2,
                    1,
                    "keluaran print",
                ],
                [
                    1,
                    0,
                    "tampil di terminal",
                ],
            ],
        },
    ],
    "Peta Otomasi Industri: Ladder Logic dan LabVIEW": [
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Siklus scan PLC berulang terus",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "baca semua input",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "evaluasi rung atas ke bawah",
                    "ke": 2,
                },
                {
                    "jenis": "keluaran",
                    "teks": "tulis semua output",
                    "ke": 0,
                },
            ],
        },
    ],
    "Solidity dan Bahasa Smart Contract Lain": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Satu transaksi transfer dari dompet sampai tercatat di blok",
            "pelaku": [
                "pengguna",
                "dompet",
                "kontrak",
                "blockchain",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "transfer(cici, 30)",
                ],
                [
                    1,
                    1,
                    "tanda tangani transaksi",
                ],
                [
                    1,
                    3,
                    "kirim transaksi + gas",
                ],
                [
                    3,
                    2,
                    "jalankan transfer di EVM",
                ],
                [
                    2,
                    2,
                    "require(saldo cukup)",
                ],
                [
                    2,
                    3,
                    "ubah saldo, emit Transfer",
                ],
                [
                    3,
                    1,
                    "transaksi masuk blok",
                ],
            ],
        },
        {
            "setelah": 14,
            "jenis": "tabel",
            "judul": "Empat bahasa smart contract",
            "tabel": [
                {
                    "kolom": [
                        "bahasa",
                        "jaringan",
                        "mirip",
                        "ciri",
                    ],
                    "baris": [
                        [
                            "Solidity",
                            "Ethereum/EVM",
                            "JS dan C++",
                            "paling banyak",
                        ],
                        [
                            "Vyper",
                            "Ethereum/EVM",
                            "Python",
                            "mudah diaudit",
                        ],
                        [
                            "Move",
                            "Sui, Aptos",
                            "Rust",
                            "aset = resource",
                        ],
                        [
                            "Cairo",
                            "Starknet",
                            "Rust",
                            "bisa dibuktikan",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Konfigurasi dan Integrasi: Nix, XSLT, Ballerina": [
        {
            "setelah": 6,
            "jenis": "alur",
            "judul": "Dari resep sampai folder di /nix/store",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "sumber, dependensi, langkah",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "derivation (resep lengkap)",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "hash semua masukan",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "hash sudah ada di store?",
                    "ya": 5,
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "build, simpan di store",
                    "ke": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "/nix/store/<hash>-paket",
                },
            ],
        },
        {
            "setelah": 9,
            "jenis": "pohon",
            "judul": "Dokumen menu.xml dan template yang mencocokkannya",
            "ket": "Template /menu cocok dengan akar. Item berkategori makanan diserahkan ke template item; Es Teh tidak terpilih.",
            "akar": {
                "teks": "menu  [/menu]",
                "anak": [
                    {
                        "teks": "item makanan",
                        "anak": [
                            {
                                "teks": "nama Nasi Goreng",
                            },
                            {
                                "teks": "harga 18000",
                            },
                        ],
                    },
                    {
                        "teks": "item minuman",
                        "anak": [
                            {
                                "teks": "nama Es Teh",
                            },
                            {
                                "teks": "harga 5000",
                            },
                        ],
                    },
                    {
                        "teks": "item makanan",
                        "anak": [
                            {
                                "teks": "nama Mie Ayam",
                            },
                            {
                                "teks": "harga 15000",
                            },
                        ],
                    },
                ],
            },
        },
    ],
}
