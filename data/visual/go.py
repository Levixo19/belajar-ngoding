"""Gambar konsep kurikulum Go. Skema: inti/visual.py."""

VISUAL = {
    "Pengenalan Go & Instalasi": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari program.go sampai satu berkas binari",
            "ket": "Go memeriksa tipe dan import yang nggak dipakai waktu "
                   "kompilasi. Kalau ada yang salah, binarinya nggak dibuat.",
            "langkah": [
                {"jenis": "mulai", "teks": "tulis program.go"},
                {"jenis": "proses", "teks": "go build program.go"},
                {"jenis": "keputusan", "teks": "lolos kompilasi?", "tidak": 5},
                {"jenis": "proses", "teks": "binari program jadi"},
                {"jenis": "keluaran", "teks": "./program: Halo Dunia!", "ke": 6},
                {"jenis": "proses", "teks": "baca error, perbaiki kode", "ke": 1},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Variabel, Konstanta & Tipe Data": [
        {
            "setelah": 0,
            "jenis": "variabel",
            "judul": "Variabel yang belum diisi langsung dapat zero value",
            "ket": "Go nggak punya undefined. Begitu var ditulis, isinya "
                   "udah jelas sesuai tipenya.",
            "isi": [
                ["var n int", "0", "int"],
                ["var s string", "\"\"", "string"],
                ["var ok bool", "false", "bool"],
                ["var p *int", "nil", "*int"],
            ],
        },
        {
            "setelah": 1,
            "jenis": "variabel",
            "judul": "Enam variabel dari contoh, enam tipe",
            "ket": "rune menyimpan nomor Unicode, jadi 'A' tersimpan sebagai 65. "
                   "Itu sebabnya Println(huruf) mencetak 65.",
            "isi": [
                ["umur", "25", "int"],
                ["tinggi", "170.5", "float64"],
                ["nama", "\"Andi\"", "string"],
                ["aktif", "true", "bool"],
                ["huruf", "65 ('A')", "rune"],
                ["data", "255", "byte"],
            ],
            "sorot": ["huruf"],
        },
    ],
    "Operator": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "a = 15 dan b = 4: pembagian int membuang sisanya",
            "ket": "Dua-duanya int, jadi a / b memberi 3. Hasil 3.75 baru muncul "
                   "sesudah keduanya diubah ke float64.",
            "tabel": [
                {
                    "kolom": ["operasi", "hasil"],
                    "baris": [
                        ["a + b", "19"],
                        ["a - b", "11"],
                        ["a * b", "60"],
                        ["a / b (int)", "3"],
                        ["a % b", "3"],
                        ["a / b (float64)", "3.75"],
                    ],
                    "sorot_baris": [3, 5],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "bit",
            "judul": "Angka 8 di balik layar: satu bit di posisi keempat",
            "ket": "8 >> 1 menggeser bit itu satu langkah ke kanan jadi 4, "
                   "8 << 1 menggesernya ke kiri jadi 16.",
            "angka": 8,
            "lebar": 8,
            "label": "8 >> 1 = 4, 8 << 1 = 16",
        },
    ],
    "Angka & Waktu: math, time & strconv": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Empat cara membulatkan, dan bedanya di angka negatif",
            "ket": "Floor selalu ke bawah, jadi -3.9 jadi -4. Trunc cuma "
                   "membuang koma, jadi -3.9 jadi -3.",
            "tabel": [
                {
                    "kolom": ["fungsi", "12345.678", "-3.9"],
                    "baris": [
                        ["math.Floor", "12345", "-4"],
                        ["math.Ceil", "12346", "-3"],
                        ["math.Round", "12346", "-4"],
                        ["math.Trunc", "12345", "-3"],
                    ],
                    "sorot_kolom": ["-3.9"],
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Layout ditulis dengan tanggal acuan, bukan YYYY-MM-DD",
            "ket": "Waktunya merdeka dari contoh: 17 Agustus 1945 jam 10.00. "
                   "Layout YYYY-MM-DD nggak dikenal, jadi tercetak apa adanya.",
            "tabel": [
                {
                    "nama": "merdeka.Format(...)",
                    "kolom": ["layout", "hasil"],
                    "baris": [
                        ["2006-01-02 15:04", "1945-08-17 10:00"],
                        ["02/01/2006", "17/08/1945"],
                        ["Jan 2, 2006", "Aug 17, 1945"],
                        ["YYYY-MM-DD", "YYYY-MM-DD"],
                    ],
                    "sorot_baris": [3],
                },
            ],
        },
    ],
    "Input & Output dengan fmt": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Satu verb, satu bentuk cetakan",
            "ket": "Nilai yang sama bisa tercetak beda tergantung verb-nya, "
                   "misalnya 255 sebagai %d dan sebagai %x.",
            "tabel": [
                {
                    "kolom": ["verb", "nilai", "tercetak"],
                    "baris": [
                        ["%d", "255", "255"],
                        ["%x", "255", "ff"],
                        ["%b", "5", "101"],
                        ["%.2f", "3.14159", "3.14"],
                        ["%q", "\"Go\"", "\"Go\""],
                        ["%T", "3.5", "float64"],
                        ["%v", "true", "true"],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "Percabangan (if & switch)": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "if berantai diperiksa dari atas, berhenti di yang pertama benar",
            "ket": "Untuk nilai 85, kondisi pertama udah benar, jadi tercetak "
                   "Grade A dan sisa kondisi nggak diperiksa sama sekali.",
            "langkah": [
                {"jenis": "mulai", "teks": "nilai := 85"},
                {"jenis": "keputusan", "teks": "nilai >= 85?", "tidak": 3},
                {"jenis": "keluaran", "teks": "Grade A", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai >= 75?", "tidak": 5},
                {"jenis": "keluaran", "teks": "Grade B", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai >= 60?", "tidak": 7},
                {"jenis": "keluaran", "teks": "Grade C", "ke": 8},
                {"jenis": "keluaran", "teks": "Tidak Lulus"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Perulangan (for)": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "for bentuk lengkap: awal, cek kondisi, isi, lalu i++",
            "ket": "Kondisi dicek sebelum tiap putaran. Begitu i jadi 11, "
                   "loop berhenti dan total sudah 55.",
            "langkah": [
                {"jenis": "mulai", "teks": "total := 0"},
                {"jenis": "proses", "teks": "i := 1"},
                {"jenis": "keputusan", "teks": "i <= 10?", "tidak": 5},
                {"jenis": "proses", "teks": "total += i"},
                {"jenis": "proses", "teks": "i++", "ke": 2},
                {"jenis": "keluaran", "teks": "Jumlah 1..10 = 55"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Array & Slice": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "angka[1:4] mengambil indeks 1, 2, 3, dan indeks 4 nggak ikut",
            "ket": "Ini isi angka sesudah tiga kali append. Potongan [1:4] "
                   "memberi [2 9 1].",
            "nama": "angka",
            "isi": ["5", "2", "9", "1", "7", "4", "8", "3"],
            "rentang": [1, 4],
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "b := a[0:2] berbagi array yang sama dengan a",
            "ket": "Disederhanakan: tiap slice menyimpan penunjuk ke array, "
                   "panjang, dan kapasitas. Sesudah b[0] = 99, a ikut berubah.",
            "label_tumpukan": "slice",
            "label_heap": "array bersama",
            "tumpukan": [["a (len 3)", "@arr"], ["b (len 2)", "@arr"]],
            "heap": [{"id": "arr", "isi": "[99 2 3]"}],
        },
    ],
    "String, Rune & Package strings": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "\"café\" itu 5 byte, dan kata[:4] membelah é jadi separuh",
            "ket": "é makan dua byte, 195 dan 169. Potongan [:4] cuma mengambil "
                   "byte 195, yang sendirian bukan huruf apa pun.",
            "nama": "[]byte(kata)",
            "isi": ["99 c", "97 a", "102 f", "195", "169"],
            "sorot": [3, 4],
            "rentang": [0, 4],
        },
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "Lewat []rune, é kembali jadi satu elemen",
            "ket": "Empat rune untuk empat huruf. string(r[:2]) memberi \"ca\" "
                   "dengan aman.",
            "nama": "[]rune(kata)",
            "isi": ["c", "a", "f", "é"],
            "rentang": [0, 2],
        },
    ],
    "Map": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Isi map stok sesudah telur ditambah dan gula diubah",
            "ket": "Kunci kopi nggak ada di sini. stok[\"kopi\"] memberi 0, dan "
                   "comma ok memberi ada = false.",
            "tabel": [
                {
                    "nama": "stok",
                    "kolom": ["kunci", "nilai"],
                    "baris": [
                        ["beras", "25"],
                        ["gula", "12"],
                        ["minyak", "8"],
                        ["telur", "30"],
                    ],
                    "sorot_baris": [1, 3],
                },
            ],
        },
    ],
    "Fungsi": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "judul": "defer menumpuk, yang terakhir didaftarkan jalan duluan",
            "ket": "Tiga defer ditulis berurutan 1, 2, 3. Waktu fungsinya "
                   "selesai, cetakannya keluar 3, 2, 1.",
            "mode": "tumpukan",
            "isi": ["defer cetak(1)", "defer cetak(2)", "defer cetak(3)"],
            "label": "defer yang menunggu",
            "operasi": "jalan: 3, 2, 1",
        },
    ],
    "Pointer": [
        {
            "setelah": 0,
            "jenis": "memori",
            "judul": "p menyimpan alamat x, jadi *p = 20 mengubah x",
            "ket": "p := &x mengambil alamat x. Menulis lewat *p menulis ke "
                   "tempat yang sama, jadi x yang tadinya 10 ikut jadi 20.",
            "label_tumpukan": "pointer",
            "label_heap": "variabel x",
            "tumpukan": [["p", "@x"]],
            "heap": [{"id": "x", "isi": "20"}],
        },
    ],
    "Struct & Method": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Struct Kelas memuat slice Siswa, struct di dalam struct",
            "ket": "Ini nilai k dari contoh. RataRata() menjumlah Nilai kedua "
                   "murid lalu membaginya dua: 85.0.",
            "akar": {
                "teks": "k: Kelas",
                "anak": [
                    {"teks": "Nama \"12 IPA 1\""},
                    {
                        "teks": "Murid []Siswa",
                        "anak": [
                            {"teks": "Budi, 20, 80"},
                            {"teks": "Citra, 19, 90"},
                        ],
                    },
                ],
            },
        },
    ],
    "Interface": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Tiga tipe berbeda di satu []Bentuk",
            "ket": "Ketiganya punya Luas() dan Nama(), jadi sama-sama memenuhi "
                   "Bentuk. Total luasnya 54.27.",
            "tabel": [
                {
                    "nama": "daftar []Bentuk",
                    "kolom": ["tipe di dalam", "Nama()", "Luas()"],
                    "baris": [
                        ["Persegi{4}", "Persegi", "16.00"],
                        ["Lingkaran{3}", "Lingkaran", "28.27"],
                        ["Persegipanjang", "Persegi Panjang", "10.00"],
                    ],
                },
            ],
        },
    ],
    "Tipe Bentukan, Konstanta Berkelompok & iota": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Tiga blok const, tiga cara iota berhitung",
            "ket": "iota mulai dari 0 di tiap blok dan naik satu per baris. "
                   "Yang berubah cuma ekspresi yang diulang compiler.",
            "tabel": [
                {
                    "nama": "Status = iota",
                    "kolom": ["nama", "nilai"],
                    "baris": [["Draf", "0"], ["Menunggu", "1"],
                              ["Aktif", "2"], ["Ditolak", "3"]],
                },
                {
                    "nama": "Hari = iota + 1",
                    "kolom": ["nama", "nilai"],
                    "baris": [["Senin", "1"], ["Selasa", "2"], ["Rabu", "3"]],
                },
                {
                    "nama": "Izin = 1 << iota",
                    "kolom": ["nama", "nilai"],
                    "baris": [["Baca", "1"], ["Tulis", "2"], ["Hapus", "4"]],
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "bit",
            "judul": "punya := Baca | Tulis menyalakan dua bit sekaligus",
            "ket": "Baca bernilai 1, Tulis bernilai 2. Bit Hapus (4) masih mati, "
                   "jadi punya&Hapus != 0 bernilai false.",
            "angka": 3,
            "lebar": 4,
            "label": "Baca | Tulis = 3",
        },
    ],
    "Error Handling": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Cara contoh memilah tiga kemungkinan hasil Tarik",
            "ket": "50000 berhasil, 0 jadi INPUT SALAH lewat errors.As, dan "
                   "200000 jadi DITOLAK lewat errors.Is.",
            "langkah": [
                {"jenis": "mulai", "teks": "err := r.Tarik(jumlah)"},
                {"jenis": "keputusan", "teks": "err == nil?", "tidak": 3},
                {"jenis": "keluaran", "teks": "berhasil, cetak sisa", "ke": 8},
                {"jenis": "keputusan", "teks": "errors.Is(err, ErrSaldoKurang)?",
                 "tidak": 5},
                {"jenis": "keluaran", "teks": "DITOLAK, saldo kurang", "ke": 8},
                {"jenis": "keputusan", "teks": "errors.As(err, &ev)?", "tidak": 7},
                {"jenis": "keluaran", "teks": "INPUT SALAH pada ev.Field", "ke": 8},
                {"jenis": "keluaran", "teks": "Error lain"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Berkas: Membaca, Menulis & io.Reader/io.Writer": [
        {
            "setelah": 0,
            "jenis": "bit",
            "judul": "Izin 0644 dalam biner, cuma sembilan bit terakhir yang dipakai",
            "ket": "Sembilan bit paling kanan dibaca per tiga: 110 pemilik (baca, "
                   "tulis), 100 grup (baca), 100 orang lain (baca). Desimalnya 420.",
            "angka": 420,
            "lebar": 16,
            "label": "0644 = rw-r--r--",
        },
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Satu fungsi laporkan, tiga tujuan tulisan",
            "ket": "Isi laporkan nggak berubah sedikit pun. Yang berubah cuma "
                   "Writer yang dikirim ke parameternya.",
            "akar": {
                "teks": "w io.Writer",
                "anak": [
                    {"teks": "os.Stdout: layar"},
                    {"teks": "&buf bytes.Buffer"},
                    {
                        "teks": "bufio.Writer",
                        "anak": [{"teks": "*os.File stok.txt"}],
                    },
                ],
            },
        },
    ],
    "Program Baris Perintah: Argumen, flag & log": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "os.Args untuk ./sapa Levi --keras",
            "ket": "Indeks 0 itu nama programnya sendiri. Argumen yang diketik "
                   "pemakai mulai dari indeks 1, dan len(os.Args) bernilai 3.",
            "nama": "os.Args",
            "isi": ["./sapa", "Levi", "--keras"],
            "sorot": [0],
        },
    ],
    "JSON & Struct Tag": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Field mana yang sampai ke JSON, dan kenapa",
            "ket": "Hasil Marshal-nya {\"kode\":\"B001\",\"nama\":\"Beras 5kg\","
                   "\"harga\":65000}. Tiga field sisanya nggak ikut.",
            "tabel": [
                {
                    "nama": "Barang",
                    "kolom": ["field Go", "tag", "di JSON"],
                    "baris": [
                        ["Kode", "json:\"kode\"", "\"kode\":\"B001\""],
                        ["Nama", "json:\"nama\"", "\"nama\":..."],
                        ["Harga", "json:\"harga\"", "\"harga\":65000"],
                        ["Diskon", "diskon,omitempty", "(hilang, 0)"],
                        ["Catatan", "json:\"-\"", "(dibuang)"],
                        ["kategori", "(tanpa tag)", "(huruf kecil)"],
                    ],
                    "sorot_baris": [3, 4, 5],
                },
            ],
        },
    ],
    "Goroutine & Channel": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Pengirim mengisi channel angka, main membacanya dengan range",
            "ket": "for n := range angka menerima 10 sampai 50, lalu berhenti "
                   "sendiri begitu channel ditutup. Totalnya 150.",
            "pelaku": ["main", "goroutine"],
            "pesan": [
                [0, 1, "go func() { ... }()"],
                [1, 0, "angka <- 10"],
                [1, 0, "angka <- 20, 30, 40"],
                [1, 0, "angka <- 50"],
                [1, 0, "close(angka)"],
            ],
        },
        {
            "setelah": 3,
            "jenis": "tumpukan",
            "judul": "Channel berpenyangga bekerja seperti antrean",
            "ket": "make(chan int, 5) punya lima slot. Yang masuk duluan "
                   "keluar duluan, dan pengirim baru menunggu kalau slotnya penuh.",
            "mode": "antrean",
            "isi": ["10", "20", "30"],
            "label": "angka := make(chan int, 5)",
            "operasi": "<-angka memberi 10",
        },
    ],
    "Pola Goroutine: Channel Berarah, select & Worker Pool": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Worker pool: siapa mengirim, siapa menutup",
            "ket": "Pengirim menutup tugas sesudah enam tugas habis. Penutup "
                   "hasil menunggu wg.Wait() dulu, baru menutup hasil.",
            "pelaku": ["pengirim", "pekerja x3", "penutup hasil", "main"],
            "pesan": [
                [0, 1, "6 Tugas lewat chan tugas"],
                [0, 1, "close(tugas)"],
                [1, 3, "Hasil lewat chan hasil"],
                [1, 2, "wg.Done() x3"],
                [2, 3, "close(hasil)"],
            ],
        },
    ],
    "context: Membatalkan & Membatasi Waktu": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Context membentuk pohon, dan batal menurun ke anak",
            "ket": "batalInduk() menutup Done milik induk dan semua keturunannya, "
                   "jadi anak ikut batal. ctxT batal sendiri sesudah 30 ms.",
            "akar": {
                "teks": "Background()",
                "anak": [
                    {"teks": "ctx WithCancel"},
                    {"teks": "ctxT WithTimeout"},
                    {
                        "teks": "induk WithCancel",
                        "anak": [{"teks": "anak WithCancel"}],
                    },
                ],
            },
        },
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "cancel() cuma mengirim sinyal, main tetap menunggu selesai",
            "ket": "hitung berhenti waktu melihat ctx.Done() tertutup, mencetak "
                   "alasannya (context canceled), lalu menutup selesai.",
            "pelaku": ["main", "hitung()"],
            "pesan": [
                [0, 1, "go hitung(ctx, keluar)"],
                [1, 0, "keluar <- 1, 2, 3"],
                [0, 1, "cancel()"],
                [1, 0, "close(selesai)"],
            ],
        },
    ],
    "Generics: Type Parameter & Package slices/maps": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "judul": "Tumpukan[int] sesudah Dorong 1, 2, 3",
            "ket": "Ambil mengeluarkan yang terakhir masuk. Pada tumpukan "
                   "kosong, Ambil memberi zero value T dan false.",
            "mode": "tumpukan",
            "isi": ["1", "2", "3"],
            "label": "var angka Tumpukan[int]",
            "operasi": "Ambil() -> 3, true",
        },
    ],
    "Package, Module & Testing": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Table-driven test: satu baris, satu kasus",
            "ket": "Isi slice kasus dari TestTambah. Tiap baris jadi satu "
                   "subtest bernama lewat t.Run.",
            "tabel": [
                {
                    "nama": "kasus",
                    "kolom": ["nama", "a", "b", "harapan"],
                    "baris": [
                        ["positif", "2", "3", "5"],
                        ["negatif", "-2", "-3", "-5"],
                        ["campur", "-2", "5", "3"],
                        ["nol", "0", "0", "0"],
                    ],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Susunan folder project Go yang umum",
            "ket": "Package di dalam internal nggak bisa diimpor dari luar "
                   "module. Tiap folder di cmd berisi satu program.",
            "akar": {
                "teks": "proyekku/",
                "anak": [
                    {"teks": "go.mod"},
                    {"teks": "main.go"},
                    {"teks": "internal/", "anak": [{"teks": "layanan/"}]},
                    {"teks": "pkg/", "anak": [{"teks": "kalkulator/"}]},
                    {
                        "teks": "cmd/",
                        "anak": [
                            {"teks": "server/main.go"},
                            {"teks": "cli/main.go"},
                        ],
                    },
                ],
            },
        },
    ],
    "Module, Import & Direktif Compiler": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Jalur import = nama module + jalur folder",
            "ket": "Foldernya hitung, tapi package di dalamnya bernama harga. "
                   "Jadi main mengimpor .../internal/hitung lalu memanggil harga.Total.",
            "akar": {
                "teks": "contoh.dev/tokoku",
                "anak": [
                    {"teks": "go.mod"},
                    {"teks": "main.go"},
                    {
                        "teks": "internal/",
                        "anak": [
                            {"teks": "hitung/",
                             "anak": [{"teks": "harga.go"}]},
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Urutan yang dijamin Go sebelum main jalan",
            "ket": "Sama dengan nomor 1 sampai 4 yang dicetak contoh: pajak "
                   "diisi dulu, lalu dua init(), baru main.",
            "langkah": [
                {"jenis": "mulai", "teks": "program mulai"},
                {"jenis": "proses", "teks": "package impor diinisialisasi"},
                {"jenis": "proses", "teks": "var pajak = hitungPajak()"},
                {"jenis": "proses", "teks": "init() pertama"},
                {"jenis": "proses", "teks": "init() kedua"},
                {"jenis": "proses", "teks": "main()"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Server HTTP dengan net/http": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Satu permintaan lewat middleware, mux, lalu handler",
            "ket": "catat() membungkus seluruh mux. Dia mencatat lama "
                   "prosesnya sesudah handler selesai menulis jawaban.",
            "pelaku": ["klien", "catat()", "mux", "g.lihat"],
            "pesan": [
                [0, 1, "GET /barang/B001"],
                [1, 2, "next.ServeHTTP(w, r)"],
                [2, 3, "cocok GET /barang/{kode}"],
                [3, 0, "200, JSON Beras 5kg"],
                [3, 1, "kembali, log dicatat"],
            ],
        },
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Tiga panggilan klien di contoh kedua, tiga status",
            "ket": "Ketiganya punya err == nil, karena jawabannya sampai. "
                   "Berhasil atau nggaknya dibaca dari resp.StatusCode.",
            "pelaku": ["klien", "server"],
            "pesan": [
                [0, 1, "GET /halo/Levi"],
                [1, 0, "200 OK: Halo, Levi!"],
                [0, 1, "GET /rahasia"],
                [1, 0, "401: kamu belum login"],
                [0, 1, "GET /tidak-ada"],
                [1, 0, "404 page not found"],
            ],
        },
    ],
    "Testing Lanjutan: Benchmark, Example & httptest": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "TestHalo memanggil handler langsung, tanpa port",
            "ket": "NewRequest membuat permintaan palsu, NewRecorder menampung "
                   "jawabannya, lalu test membaca Code, Header, dan Body.",
            "pelaku": ["TestHalo", "web.Halo", "rek Recorder"],
            "pesan": [
                [0, 1, "Halo(rek, req ?nama=Levi)"],
                [1, 2, "Content-Type + JSON"],
                [0, 2, "cek Code, Header, Body"],
            ],
        },
    ],
    "Studi Kasus: Manajemen Inventaris": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Laporan kedua, sesudah tiga percobaan Ambil",
            "ket": "Cuma Ambil B001 x5 yang berhasil. Gula dan minyak di bawah "
                   "15, jadi keduanya muncul di StokMenipis(15).",
            "tabel": [
                {
                    "nama": "inventaris",
                    "kolom": ["kode", "nama", "harga", "stok", "nilai"],
                    "baris": [
                        ["B001", "Beras 5kg", "65000", "15", "975000"],
                        ["B002", "Gula 1kg", "15000", "13", "195000"],
                        ["B003", "Minyak 2L", "32000", "12", "384000"],
                    ],
                    "sorot_baris": [1, 2],
                },
            ],
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "map[string]*Barang: kuncinya menunjuk Barang yang sama",
            "ket": "Disederhanakan. Karena nilainya pointer, b.Stok -= jumlah "
                   "di Ambil mengubah Barang aslinya, bukan salinan.",
            "label_tumpukan": "i.barang",
            "label_heap": "Barang",
            "tumpukan": [["\"B001\"", "@b1"], ["\"B002\"", "@b2"],
                         ["\"B003\"", "@b3"]],
            "heap": [
                {"id": "b1", "isi": "Beras 5kg, stok 15"},
                {"id": "b2", "isi": "Gula 1kg, stok 13"},
                {"id": "b3", "isi": "Minyak 2L, stok 12"},
            ],
        },
    ],
}
