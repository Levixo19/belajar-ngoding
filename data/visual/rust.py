"""Gambar konsep kurikulum Rust. Skema: inti/visual.py."""

VISUAL = {
    "Pengenalan Rust & Instalasi": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari main.rs sampai program jalan",
            "ket": "Compiler memeriksa kodemu sebelum binari dibuat. Kalau ada "
                   "yang salah, kamu memperbaikinya dulu, lalu kompilasi lagi.",
            "langkah": [
                {"jenis": "mulai", "teks": "tulis main.rs"},
                {"jenis": "proses", "teks": "rustc main.rs"},
                {"jenis": "keputusan", "teks": "lolos pemeriksaan?", "tidak": 5},
                {"jenis": "proses", "teks": "binari main jadi"},
                {"jenis": "keluaran", "teks": "./main: Halo Dunia!", "ke": 6},
                {"jenis": "proses", "teks": "baca error, perbaiki kode", "ke": 1},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Variabel, Mutabilitas & Tipe Data": [
        {
            "setelah": 0,
            "jenis": "variabel",
            "judul": "Shadowing bikin tiga x berbeda, x yang lama nggak diubah",
            "ket": "Tiap let membuat variabel baru dengan nama yang sama. "
                   "Karena baru, tipenya boleh ganti dari i32 ke &str.",
            "isi": [
                ["x pertama", "5", "i32"],
                ["x kedua", "6", "i32"],
                ["x ketiga", "\"enam\"", "&str"],
            ],
            "sorot": ["x ketiga"],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "250 + 10 di u8: empat cara, empat hasil",
            "ket": "u8 cuma muat sampai 255. Kamu yang memilih apa yang terjadi "
                   "saat hasilnya kelewatan.",
            "tabel": [
                {
                    "nama": "besar: u8 = 250",
                    "kolom": ["cara", "hasil"],
                    "baris": [
                        ["checked_add(10)", "None"],
                        ["saturating_add", "255"],
                        ["wrapping_add(10)", "4"],
                        ["besar + 10", "panic (debug)"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Fungsi, Ekspresi & Pernyataan": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Rantai if-else di grade() langsung jadi nilai kembalian",
            "ket": "Tiap cabang berakhir di sebuah char tanpa titik koma. "
                   "Cabang pertama yang syaratnya benar yang menang.",
            "langkah": [
                {"jenis": "mulai", "teks": "grade(nilai)"},
                {"jenis": "keputusan", "teks": "nilai >= 85?", "tidak": 3},
                {"jenis": "keluaran", "teks": "'A'", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai >= 75?", "tidak": 5},
                {"jenis": "keluaran", "teks": "'B'", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai >= 60?", "tidak": 7},
                {"jenis": "keluaran", "teks": "'C'", "ke": 8},
                {"jenis": "keluaran", "teks": "'D'"},
                {"jenis": "selesai", "teks": "kembali ke pemanggil"},
            ],
        },
    ],
    "Percabangan & Perulangan": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "0..5 berhenti sebelum 5, 0..=5 ikut memuat 5",
            "ket": "Yang disorot adalah isi rentang 0..5. Angka 5 di ujung "
                   "cuma ikut kalau kamu menulis 0..=5.",
            "isi": ["0", "1", "2", "3", "4", "5"],
            "rentang": [0, 5],
        },
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "loop yang mengembalikan nilai lewat break n",
            "ket": "n naik satu per satu sampai n * n lewat dari 100. "
                   "Itu terjadi di n = 11, jadi pertama bernilai 11.",
            "langkah": [
                {"jenis": "mulai", "teks": "n = 0"},
                {"jenis": "proses", "teks": "n += 1"},
                {"jenis": "keputusan", "teks": "n * n > 100?", "tidak": 1},
                {"jenis": "keluaran", "teks": "break n, pertama = 11"},
                {"jenis": "selesai", "teks": "lanjut ke println!"},
            ],
        },
    ],
    "Ownership: Aturan Inti Rust": [
        {
            "setelah": 0,
            "jenis": "memori",
            "judul": "Sesudah let b = a, cuma b yang memegang teksnya",
            "ket": "a dan b sempat menunjuk ke teks yang sama. Rust menganggap "
                   "a nggak berlaku lagi, jadi teks itu cuma dilepas sekali, "
                   "waktu b keluar dari scope.",
            "tumpukan": [
                ["a", "dipindah, mati"],
                ["b", "@teks"],
            ],
            "heap": [
                {"id": "teks", "isi": "\"halo\" (4 byte)"},
            ],
            "label_tumpukan": "stack",
            "label_heap": "heap",
        },
        {
            "setelah": 1,
            "jenis": "memori",
            "judul": "Angka disalin di stack, clone() menyalin teksnya ke heap",
            "ket": "a dan b masing-masing punya angka 5 sendiri. s1 dan s2 "
                   "masing-masing punya teks \"halo\" sendiri di heap, karena "
                   "clone membuat salinan penuh.",
            "tumpukan": [
                ["a", "5"],
                ["b", "5"],
                ["s1", "@h1"],
                ["s2", "@h2"],
            ],
            "heap": [
                {"id": "h1", "isi": "\"halo\" milik s1"},
                {"id": "h2", "isi": "\"halo\" milik s2"},
            ],
            "label_tumpukan": "stack",
            "label_heap": "heap",
        },
    ],
    "Reference & Borrowing": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Banyak peminjam baca, atau satu peminjam ubah",
            "ket": "Yang dihitung cuma pinjaman yang masih dipakai sesudah "
                   "titik itu (NLL). Campuran & dan &mut ditolak compiler.",
            "tabel": [
                {
                    "nama": "hidup bersamaan",
                    "kolom": ["pinjaman", "boleh?"],
                    "baris": [
                        ["&v", "boleh"],
                        ["&v, &v, &v", "boleh"],
                        ["&mut v", "boleh"],
                        ["&mut v, &mut v", "ditolak"],
                        ["&v, &mut v", "ditolak"],
                    ],
                    "sorot_baris": [3, 4],
                },
            ],
        },
    ],
    "Slice & String": [
        {
            "setelah": 0,
            "jenis": "larik",
            "nama": "v",
            "judul": "&v[1..4] meminjam elemen ke-1 sampai ke-3",
            "ket": "Akhir rentang nggak ikut, jadi isinya [2, 3, 4]. Slice "
                   "nggak menyalin apa pun; ia menunjuk ke bagian v.",
            "isi": ["1", "2", "3", "4", "5"],
            "rentang": [1, 4],
        },
        {
            "setelah": 0,
            "jenis": "memori",
            "judul": "String memiliki teks di heap, &str cuma menunjuk ke situ",
            "ket": "b yang melepas teksnya waktu keluar dari scope. d cuma "
                   "pinjaman, jadi d nggak boleh dipakai lebih lama dari b.",
            "tumpukan": [
                ["b: String", "@teks"],
                ["d: &str", "@teks"],
            ],
            "heap": [
                {"id": "teks", "isi": "\"halo\""},
            ],
            "label_tumpukan": "stack",
            "label_heap": "heap",
        },
    ],
    "Struct": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Field struct tinggal bersebelahan, isi String-nya di heap",
            "ket": "Keadaan a dan b di akhir main. saldo (i64) disimpan "
                   "langsung di struct, sedangkan pemilik menunjuk ke teks di heap.",
            "tumpukan": [
                ["a.pemilik", "@andi"],
                ["a.saldo", "450000"],
                ["b.pemilik", "@budi"],
                ["b.saldo", "100000"],
            ],
            "heap": [
                {"id": "andi", "isi": "\"Andi\""},
                {"id": "budi", "isi": "\"Budi\""},
            ],
            "label_tumpukan": "stack",
            "label_heap": "heap",
        },
    ],
    "Enum & Option": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Satu enum Bentuk, tiap varian membawa data sendiri",
            "ket": "Nilai yang sama dengan isi vec semua di contoh kode. "
                   "match di luas() membongkar datanya per varian.",
            "tabel": [
                {
                    "nama": "isi vec semua",
                    "kolom": ["varian", "datanya", "luas"],
                    "baris": [
                        ["Lingkaran", "2.0", "12.57"],
                        ["Persegi", "4.0", "16.00"],
                        ["PersegiPanjang", "p: 6.0, l: 3.0", "18.00"],
                    ],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "cari() mengembalikan Some(i) kalau ketemu, None kalau nggak",
            "ket": "Disederhanakan dari for dengan enumerate. Pemanggil wajib "
                   "membuka Option-nya, misalnya dengan unwrap_or(0).",
            "langkah": [
                {"jenis": "mulai", "teks": "i = 0"},
                {"jenis": "keputusan", "teks": "masih ada elemen?", "tidak": 5},
                {"jenis": "keputusan", "teks": "data[i] == target?", "tidak": 4},
                {"jenis": "keluaran", "teks": "return Some(i)", "ke": 6},
                {"jenis": "proses", "teks": "i += 1", "ke": 1},
                {"jenis": "keluaran", "teks": "None"},
                {"jenis": "selesai", "teks": "kembali ke pemanggil"},
            ],
        },
    ],
    "Pattern Matching: match & if let": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "match mencoba pola dari atas dan berhenti di yang pertama cocok",
            "ket": "Untuk titik (3, -7), empat pola pertama gagal. Pola kelima "
                   "cocok, jadi pola _ di bawahnya nggak pernah dicoba.",
            "tabel": [
                {
                    "nama": "titik = (3, -7)",
                    "kolom": ["pola", "hasil", "(3, -7)?"],
                    "baris": [
                        ["(0, 0)", "pusat", "nggak"],
                        ["(_, 0)", "sumbu x", "nggak"],
                        ["(0, _)", "sumbu y", "nggak"],
                        ["x>0 && y>0", "kuadran I", "nggak"],
                        ["x>0 && y<0", "kuadran IV", "cocok"],
                        ["_", "kiri", "dilewati"],
                    ],
                    "sorot_baris": [4],
                },
            ],
        },
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "mode": "tumpukan",
            "judul": "while let Some(atas) = tumpuk.pop() mengambil dari atas",
            "ket": "pop() memberi 3, lalu 2, lalu 1, lalu None. Begitu None, "
                   "polanya nggak cocok lagi dan perulangan berhenti.",
            "isi": ["1", "2", "3"],
            "label": "tumpuk = vec![1, 2, 3]",
            "operasi": "pop() -> Some(3)",
        },
    ],
    "Vec & HashMap": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Isi HashMap hitung sesudah kalimatnya dibaca",
            "ket": "Baris di sini sudah diurutkan seperti keluaran program. "
                   "Di HashMap aslinya, urutan isinya nggak dijamin.",
            "tabel": [
                {
                    "nama": "hitung (HashMap)",
                    "kolom": ["kunci", "nilai"],
                    "baris": [
                        ["kucing", "3"],
                        ["ikan", "2"],
                        ["makan", "1"],
                        ["tidur", "1"],
                    ],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "larik",
            "nama": "angka (sort)",
            "judul": "Sesudah sort, dua angka 3 bersebelahan, jadi dedup bisa membuangnya",
            "ket": "dedup() cuma membuang duplikat yang letaknya berurutan. "
                   "Hasil akhirnya [1, 3, 5, 7, 9].",
            "isi": ["1", "3", "3", "5", "7", "9"],
            "sorot": [1, 2],
        },
    ],
    "Penanganan Galat: panic! & Result": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Apa yang dikerjakan ? di total += parse_nilai(t)?",
            "ket": "Kalau hasilnya Err, rata_rata langsung berhenti dan "
                   "mengembalikan galat itu ke pemanggilnya.",
            "langkah": [
                {"jenis": "mulai", "teks": "panggil parse_nilai(t)"},
                {"jenis": "keputusan", "teks": "hasilnya Ok(n)?", "tidak": 4},
                {"jenis": "proses", "teks": "buka bungkusnya: n"},
                {"jenis": "proses", "teks": "total += n, lanjut", "ke": 5},
                {"jenis": "keluaran", "teks": "return Err(..) dari rata_rata"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Lima masukan, lima hasil parse_nilai",
            "ket": "Sama dengan keluaran contoh kode. Spasi di \" 92 \" "
                   "dibuang trim() sebelum diurai.",
            "tabel": [
                {
                    "nama": "parse_nilai(t)",
                    "kolom": ["t", "Ok/Err", "isinya"],
                    "baris": [
                        ["\"88\"", "Ok", "88"],
                        ["\" 92 \"", "Ok", "92"],
                        ["\"abc\"", "Err", "BukanAngka"],
                        ["\"150\"", "Err", "DiLuarRentang"],
                        ["\"-3\"", "Err", "DiLuarRentang"],
                    ],
                    "sorot_baris": [2, 3, 4],
                },
            ],
        },
    ],
    "Generic": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Satu fungsi terbesar, tiga salinan di binari",
            "ket": "Monomorphization: compiler menulis satu versi untuk tiap "
                   "tipe yang betul-betul dipakai di main.",
            "tabel": [
                {
                    "nama": "terbesar(&...) di main",
                    "kolom": ["data", "salinan fungsi", "hasil"],
                    "baris": [
                        ["angka", "terbesar::<i32>", "9"],
                        ["pecahan", "terbesar::<f64>", "8.1"],
                        ["huruf", "terbesar::<char>", "u"],
                    ],
                },
            ],
        },
    ],
    "Trait": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Dua tipe menerapkan trait Bangun yang sama",
            "ket": "Persegi memakai ringkas() bawaan dari trait, Lingkaran "
                   "menulis versinya sendiri.",
            "akar": {
                "teks": "trait Bangun",
                "anak": [
                    {"teks": "Persegi", "anak": [
                        {"teks": "luas, nama"},
                        {"teks": "ringkas: bawaan"},
                    ]},
                    {"teks": "Lingkaran", "anak": [
                        {"teks": "luas, nama"},
                        {"teks": "ringkas: ditimpa"},
                    ]},
                ],
            },
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Vec<Box<dyn Bangun>> menyimpan penunjuk, datanya di heap",
            "ket": "Tiap elemen Vec berukuran sama: penunjuk ke data plus "
                   "penunjuk ke tabel virtual. Data Persegi dan Lingkaran "
                   "sendiri boleh beda ukuran.",
            "tumpukan": [
                ["semua[0]", "@p2"],
                ["semua[1]", "@l1"],
                ["semua[2]", "@p5"],
            ],
            "heap": [
                {"id": "p2", "isi": "Persegi { sisi: 2.0 }"},
                {"id": "l1", "isi": "Lingkaran { jari: 1.0 }"},
                {"id": "p5", "isi": "Persegi { sisi: 5.0 }"},
            ],
            "label_tumpukan": "elemen Vec",
            "label_heap": "isi Box di heap",
        },
    ],
    "Lifetime": [
        {
            "setelah": 1,
            "jenis": "memori",
            "judul": "Pengutip nggak menyalin teks, ia menunjuk ke teks milik kalimat",
            "ket": "Literal tertanam di binari, makanya bertipe &'static str. "
                   "p.sumber dan hasil p.awal(10) meminjam teks yang sama, jadi "
                   "keduanya terikat pada umur teks itu.",
            "tumpukan": [
                ["kalimat", "@lit"],
                ["p.sumber", "@lit"],
                ["p.awal(10)", "@lit"],
            ],
            "heap": [
                {"id": "lit", "isi": "\"Rust menjamin keamanan...\""},
            ],
            "label_tumpukan": "stack",
            "label_heap": "teks di binari",
        },
    ],
    "Closure & Iterator": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "filter menyaring, sort_by mengurutkan yang tersisa",
            "ket": "Data yang sama dengan contoh kode. Tiga murid dengan nilai "
                   "75 ke atas lolos, lalu diurutkan dari nilai tertinggi.",
            "tabel": [
                {
                    "nama": "data",
                    "kolom": ["nama", "kelas", "nilai"],
                    "baris": [
                        ["Andi", "A", "88"],
                        ["Budi", "B", "72"],
                        ["Cici", "A", "95"],
                        ["Dedi", "B", "64"],
                        ["Euis", "A", "79"],
                    ],
                    "sorot_baris": [0, 2, 4],
                },
                {
                    "nama": "lulus (terurut)",
                    "kolom": ["nama", "kelas", "nilai"],
                    "baris": [
                        ["Cici", "A", "95"],
                        ["Andi", "A", "88"],
                        ["Euis", "A", "79"],
                    ],
                },
            ],
            "panah": "filter(nilai >= 75), lalu sort_by",
        },
    ],
    "Modul, Crate & Cargo": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Modul matematika dan siapa yang kelihatan dari luar",
            "ket": "Item tanpa pub cuma bisa dipakai dari dalam modulnya. "
                   "pangkat butuh pub di dirinya dan di modul lanjut.",
            "akar": {
                "teks": "crate",
                "anak": [
                    {"teks": "mod matematika", "anak": [
                        {"teks": "pub fn tambah"},
                        {"teks": "fn rahasia"},
                        {"teks": "pub mod lanjut", "anak": [
                            {"teks": "pub fn pangkat"},
                        ]},
                    ]},
                ],
            },
        },
    ],
    "Smart Pointer: Box, Rc & RefCell": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Tiga Rc menunjuk ke satu RefCell yang sama",
            "ket": "Rc::clone cuma menaikkan hitungan, datanya nggak disalin. "
                   "borrow_mut() dari penunjuk mana pun mengubah Vec yang sama.",
            "tumpukan": [
                ["catatan", "@c"],
                ["penulis_a", "@c"],
                ["penulis_b", "@c"],
            ],
            "heap": [
                {"id": "c", "isi": "hitungan 3, Vec isi 3 teks"},
            ],
            "label_tumpukan": "stack",
            "label_heap": "heap (Rc)",
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Hitungan Rc naik di dalam blok, turun lagi sesudahnya",
            "ket": "_a dan _b dilepas di akhir blok, jadi hitungannya kembali "
                   "jadi 1. Datanya baru dilepas saat hitungan sampai nol.",
            "tabel": [
                {
                    "nama": "strong_count(&bersama)",
                    "kolom": ["saat", "hitungan"],
                    "baris": [
                        ["sesudah Rc::new", "1"],
                        ["di dalam blok", "3"],
                        ["sesudah blok", "1"],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "Concurrency: Thread & Channel": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Tiga thread mengirim pesan ke main lewat satu channel",
            "ket": "Urutan pesan yang tiba bisa beda tiap kali dijalankan, "
                   "makanya main mengurutkannya sebelum mencetak.",
            "pelaku": ["main", "thread A", "thread B", "thread C"],
            "pesan": [
                [0, 1, "spawn, bawa salinan kirim"],
                [0, 2, "spawn, bawa salinan kirim"],
                [0, 3, "spawn, bawa salinan kirim"],
                [2, 0, "pesan dari B"],
                [1, 0, "pesan dari A"],
                [3, 0, "pesan dari C"],
            ],
        },
    ],
    "Testing & Dokumentasi": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Tes memilih nilai tepat di kedua sisi tiap batas",
            "ket": "Sama dengan grade_di_batas_bawah_tiap_huruf. Di batas "
                   "inilah salah ketik >= dan > atau ..= dan .. ketahuan.",
            "tabel": [
                {
                    "nama": "tes grade(n)",
                    "kolom": ["n", "harus"],
                    "baris": [
                        ["85", "'A'"],
                        ["84", "'B'"],
                        ["75", "'B'"],
                        ["74", "'C'"],
                        ["60", "'C'"],
                        ["59", "'D'"],
                        ["0", "'D'"],
                    ],
                },
            ],
        },
    ],
    "Trait Standar & Konversi": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Versi yang diurutkan sebagai teks salah tempat",
            "ket": "Sebagai teks, \"v1.10.0\" ada sebelum \"v1.4.2\" karena "
                   "'1' lebih kecil dari '4'. derive(Ord) membandingkan mayor, "
                   "minor, lalu tambal sebagai angka.",
            "tabel": [
                {
                    "nama": "diurutkan sebagai teks",
                    "kolom": ["versi"],
                    "baris": [["v0.0.0"], ["v1.10.0"], ["v1.4.2"], ["v2.0.0"]],
                    "sorot_baris": [1],
                },
                {
                    "nama": "derive(Ord)",
                    "kolom": ["versi"],
                    "baris": [["v0.0.0"], ["v1.4.2"], ["v1.10.0"], ["v2.0.0"]],
                    "sorot_baris": [2],
                },
            ],
        },
    ],
    "Membaca Masukan & Berkas": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "filter_map(|t| t.parse().ok()) untuk tiap token masukan",
            "ket": "Dengan masukan \"12 7 abc 30 5\", cuma \"abc\" yang gagal "
                   "diurai dan dibuang.",
            "langkah": [
                {"jenis": "masukan", "teks": "ambil token berikutnya"},
                {"jenis": "keputusan", "teks": "parse() berhasil?", "tidak": 3},
                {"jenis": "proses", "teks": "masukkan ke angka", "ke": 4},
                {"jenis": "proses", "teks": "buang token itu"},
                {"jenis": "keputusan", "teks": "masih ada token?", "ya": 0, "tidak": 5},
                {"jenis": "keluaran", "teks": "angka = [12, 7, 30, 5]"},
            ],
        },
    ],
    "Proyek Utuh: Menggabungkan Semuanya": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "main bertanya, Gudang menjawab dengan Result",
            "ket": "Dua langkah dari daftar langkah di main. Gudang nggak "
                   "mencetak apa pun; main yang mengubah jawabannya jadi teks.",
            "pelaku": ["main", "Gudang"],
            "pesan": [
                [0, 1, "catat(\"B01\", Masuk, 15)"],
                [1, 0, "Ok(25)"],
                [0, 1, "catat(\"B02\", Keluar, 10)"],
                [1, 0, "Err(StokTidakCukup)"],
            ],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Isi gudang di akhir program",
            "ket": "Nilai persediaannya 3115000. B02 satu-satunya yang stoknya "
                   "di bawah 10, jadi cuma ia yang muncul di stok menipis.",
            "tabel": [
                {
                    "nama": "g.semua()",
                    "kolom": ["kode", "nama", "stok", "harga", "nilai"],
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
