"""Gambar konsep kurikulum Bikin Aplikasi. Skema: inti/visual.py."""

VISUAL = {
    "Dari Skrip ke Aplikasi": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Empat pertanyaan tadi, dan bagian aplikasi yang menjawabnya",
            "ket": "Baris yang disorot sengaja disimpan paling lama. Jawabannya ada "
                   "di materi Dua Pengguna Bersamaan.",
            "tabel": [{
                "nama": "skrip HitungStok",
                "kolom": ["pertanyaan", "dijawab oleh"],
                "baris": [
                    ["angka 15 ke mana", "database"],
                    ["dua petugas", "penguncian"],
                    ["siapa, kapan", "log dan mutasi"],
                    ["minta 999 > 20", "aturan service"],
                ],
                "sorot_baris": [1],
            }],
        },
    ],
    "Lapisan-lapisan Aplikasi Web": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Satu klik Simpan mutasi, dari browser turun ke DAO lalu naik lagi",
            "ket": "Angkanya contoh: item 61, keluar 5, stok 20. Controller cuma "
                   "meneruskan; keputusan 'stok cukup' diambil di service.",
            "pelaku": ["Browser", "Controller", "Service", "DAO"],
            "pesan": [
                [0, 1, "POST /items/61/stock"],
                [1, 2, "catatMutasi(61, OUT, 5)"],
                [2, 3, "cariById(61)"],
                [3, 2, "Item, stok 20"],
                [2, 2, "cek: 20 >= 5? ya"],
                [2, 3, "simpan(item), stok 15"],
                [2, 1, "selesai tanpa exception"],
                [1, 0, "redirect:/items/61"],
            ],
        },
    ],
    "Model Data: dari Benda Nyata ke Tabel": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Tabel di sisi banyak yang menyimpan id si satu",
            "ket": "item.category_id menunjuk kategori. request_item jadi tabel "
                   "penghubung: permintaan 17 berisi dua item, item 61 muncul di "
                   "dua permintaan. Isinya contoh.",
            "tabel": [
                {
                    "nama": "category",
                    "kolom": ["id", "nama"],
                    "baris": [["1", "APAR"], ["2", "SCBA"]],
                },
                {
                    "nama": "item",
                    "kolom": ["id", "kode", "category_id"],
                    "baris": [
                        ["61", "APAR-003", "1"],
                        ["62", "APAR-004", "1"],
                        ["70", "SCBA-001", "2"],
                    ],
                    "sorot_kolom": ["category_id"],
                },
                {
                    "nama": "request_item",
                    "kolom": ["request_id", "item_id"],
                    "baris": [["17", "61"], ["17", "70"], ["18", "61"]],
                    "sorot_kolom": ["request_id", "item_id"],
                },
            ],
            "panah": "kolom *_id menyimpan id baris di tabel lain",
        },
    ],
    "Entitas: Benda Menjadi Kelas": [
        {
            "setelah": 1,
            "jenis": "variabel",
            "judul": "Isi field Item sesudah new Item(\"APR-003\", \"APAR 3kg\", \"buah\", 5)",
            "ket": "Constructor nggak menyentuh id, jadi masih null, dan stok "
                   "diisi 0. Karena 0 <= 5, isStokMenipis() menjawab true.",
            "isi": [
                ["id", "null", "Long"],
                ["kode", "\"APR-003\"", "String"],
                ["nama", "\"APAR 3kg\"", "String"],
                ["satuan", "\"buah\"", "String"],
                ["stok", "0", "int"],
                ["stokMinimum", "5", "int"],
            ],
            "sorot": ["stok", "stokMinimum"],
        },
    ],
    "Enum dan Exception Buatan Sendiri": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Angka ordinal di database berubah arti begitu REVIEW disisipkan",
            "ket": "Isi tabelnya nggak berubah sedikit pun. Yang berubah cuma "
                   "konstanta mana yang ada di posisi itu. Teks name() tetap aman.",
            "tabel": [{
                "nama": "kolom status (ORDINAL)",
                "kolom": ["angka", "dulu dibaca", "sesudah sisip"],
                "baris": [
                    ["0", "PENDING", "PENDING"],
                    ["1", "APPROVED", "REVIEW"],
                    ["2", "REJECTED", "APPROVED"],
                    ["3", "RETURNED", "REJECTED"],
                ],
                "sorot_baris": [1, 2, 3],
            }],
        },
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "coba(\"Selang\", 3, 10): service melempar, controller yang menangkap",
            "ket": "Nggak ada satu pun 'throws' di sepanjang jalan, karena "
                   "AturanDilanggar turunan RuntimeException.",
            "pelaku": ["Controller", "Service"],
            "pesan": [
                [0, 1, "catatKeluar(Selang, 3, 10)"],
                [1, 1, "stok 3 < jumlah 10"],
                [1, 0, "throw StokTidakCukupException"],
                [0, 0, "catch AturanDilanggar: DITOLAK"],
            ],
        },
    ],
    "DAO: Satu-satunya Pintu ke Database": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Service cuma kenal interface ItemDao, implementasinya bisa ditukar",
            "ket": "Ketiganya punya method yang sama. Ganti yang dipakai, dan "
                   "service nggak berubah sebaris pun.",
            "akar": {"teks": "ItemDao interface", "anak": [
                {"teks": "versi Hibernate"},
                {"teks": "versi PostgreSQL"},
                {"teks": "versi memori (uji)"},
            ]},
        },
    ],
    "Hubungan Antar Entitas dan Kapan Datanya Diambil": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Kolom hubungannya cuma ada di item, sisi pemilik",
            "ket": "Tabel category nggak menyimpan apa pun soal item. Makanya "
                   "kategori.getItems().add(item) aja nggak pernah tersimpan.",
            "tabel": [
                {
                    "nama": "category (sisi cermin)",
                    "kolom": ["id", "nama"],
                    "baris": [["1", "APAR"], ["2", "SCBA"]],
                },
                {
                    "nama": "item (sisi pemilik)",
                    "kolom": ["id", "kode", "category_id"],
                    "baris": [["61", "APAR-003", "1"], ["70", "SCBA-001", "2"]],
                    "sorot_kolom": ["category_id"],
                },
            ],
            "panah": "@JoinColumn(name = \"category_id\")",
        },
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Cara LAZY polos di program tadi: 1 query kategori + 3 query item",
            "ket": "Program DemoNPlusSatu meniru Hibernate tanpa database. Tiap "
                   "getItems() pertama menembak SELECT sendiri, jadi totalnya 4. "
                   "Dengan JOIN FETCH cukup 1.",
            "pelaku": ["program", "Hibernate", "Database"],
            "pesan": [
                [0, 1, "ambil semua kategori"],
                [1, 2, "SELECT * FROM category"],
                [0, 1, "APAR.getItems()"],
                [1, 2, "SELECT item WHERE kategori=?"],
                [0, 1, "SCBA.getItems()"],
                [1, 2, "SELECT item WHERE kategori=?"],
                [0, 1, "APD.getItems()"],
                [1, 2, "SELECT item WHERE kategori=?"],
            ],
        },
    ],
    "Wadah Objek Spring: Bean dan Injeksi Dependensi": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Yang dikerjakan main() di WadahMini, persis tugas wadah Spring",
            "ket": "DAO dibuat lebih dulu, lalu diserahkan lewat constructor. "
                   "Panggilan stok() untuk mencetak sisa nggak digambar.",
            "pelaku": ["main()", "ItemDaoMemori", "StokService"],
            "pesan": [
                [0, 1, "new ItemDaoMemori()"],
                [0, 2, "new StokService(dao)"],
                [0, 2, "kurangi(\"APAR-6KG\", 3)"],
                [2, 1, "stok(): 20"],
                [2, 1, "simpan(\"APAR-6KG\", 17)"],
                [0, 2, "kurangi(\"APAR-6KG\", 30)"],
                [2, 1, "stok(): 17"],
                [2, 2, "17 < 30: Ditolak"],
            ],
        },
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Dua wadah di Spring MVC gaya lama: wadah web anak dari wadah root",
            "ket": "Anak boleh melihat isi induknya, kebalikannya nggak. "
                   "Penghidup @PreAuthorize cuma membungkus bean di wadahnya sendiri.",
            "akar": {"teks": "wadah root", "anak": [
                {"teks": "RequestService"},
                {"teks": "ItemDaoImpl"},
                {"teks": "DataSource"},
                {"teks": "PasswordEncoder"},
                {"teks": "wadah web (anak)", "anak": [
                    {"teks": "ItemController"},
                    {"teks": "view resolver"},
                ]},
            ]},
        },
    ],
    "Service: Tempat Aturan Bisnis Hidup": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "setujui(): semua pemeriksaan dulu, perubahan belakangan",
            "ket": "Di kode di atas, junk dan stok diperiksa bergantian per baris di "
                   "perulangan pertama. Kalau satu aja gagal, belum ada stok yang "
                   "berkurang.",
            "langkah": [
                {"jenis": "mulai", "teks": "setujui(requestId, namaPetugas)"},
                {"jenis": "keputusan", "teks": "status == PENDING?", "tidak": 6},
                {"jenis": "keputusan", "teks": "tiap baris: item bukan junk?", "tidak": 6},
                {"jenis": "keputusan", "teks": "tiap baris: stok cukup?", "tidak": 6},
                {"jenis": "proses", "teks": "kurangi stok, catat mutasi OUT"},
                {"jenis": "selesai", "teks": "status APPROVED, simpan"},
                {"jenis": "selesai", "teks": "throw AturanDilanggar"},
            ],
        },
    ],
    "Controller: Menerjemahkan HTTP": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Post-Redirect-Get: yang diulang waktu refresh cuma GET",
            "ket": "Halaman terakhir di browser hasil GET, jadi refresh nggak "
                   "mencatat mutasi untuk kedua kalinya.",
            "pelaku": ["Browser", "Controller"],
            "pesan": [
                [0, 1, "POST /items/61/stock"],
                [1, 0, "302, Location: /items/61"],
                [0, 1, "GET /items/61"],
                [1, 0, "200, halaman detail"],
                [0, 1, "refresh: GET /items/61 lagi"],
                [1, 0, "200, stok nggak berubah"],
            ],
        },
    ],
    "Anotasi Controller dan Jalan Data ke Tampilan": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Teks dari HTTP diubah Spring jadi tipe Java, dan bisa gagal",
            "ket": "Dua baris terakhir ditolak 400 oleh Spring sendiri, sebelum "
                   "method controller-mu sempat jalan.",
            "tabel": [{
                "kolom": ["dari HTTP", "diisi ke", "hasil"],
                "baris": [
                    ["/items/61", "id (path)", "Long 61"],
                    ["?qty=5", "qty (param)", "int 5"],
                    ["?type=OUT", "type (param)", "MovementType.OUT"],
                    ["?qty=dua", "qty (param)", "400 Bad Request"],
                    ["/items/abc", "id (path)", "400 Bad Request"],
                ],
                "sorot_baris": [3, 4],
            }],
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "${...} mencari nama di kotak model, dan nama yang salah diam saja",
            "ket": "Persis keluaran program JembatanTampilan: ${histori} kosong "
                   "tanpa satu pun pesan error.",
            "tabel": [{
                "nama": "model",
                "kolom": ["di JSP", "isi model", "tercetak"],
                "baris": [
                    ["${item}", "APAR 3kg", "[APAR 3kg]"],
                    ["${history}", "3 baris mutasi", "[3 baris mutasi]"],
                    ["${histori}", "(nggak ada)", "[]"],
                ],
                "sorot_baris": [2],
            }],
        },
    ],
    "DTO dan Validasi Masukan": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Field yang nggak ada di ItemForm nggak punya jalan masuk",
            "ket": "Baris yang disorot cuma ada di entitas. Pengguna yang "
                   "mengirim stok=9999 nggak menemukan setter untuknya.",
            "tabel": [{
                "kolom": ["field", "Item", "ItemForm"],
                "baris": [
                    ["id", "ada", "nggak ada"],
                    ["kode", "ada", "ada"],
                    ["nama", "ada", "ada"],
                    ["satuan", "ada", "ada"],
                    ["stokMinimum", "int", "Integer"],
                    ["stok", "ada", "nggak ada"],
                    ["dibuatOleh", "ada", "nggak ada"],
                    ["kategori", "objek Kategori", "kategoriId saja"],
                ],
                "sorot_baris": [0, 5, 6],
            }],
        },
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Satu perjalanan utuh formulir tambah item",
            "ket": "Dua jalan kembali ke formulir: gagal bentuk (anotasi) dan "
                   "gagal aturan bisnis (service). Cuma yang berhasil yang redirect.",
            "langkah": [
                {"jenis": "masukan", "teks": "POST /items (isian teks)"},
                {"jenis": "proses", "teks": "@ModelAttribute isi ItemForm"},
                {"jenis": "proses", "teks": "@Valid tulis ke BindingResult"},
                {"jenis": "keputusan", "teks": "result.hasErrors()?", "tidak": 5},
                {"jenis": "selesai", "teks": "return items/form + pesan"},
                {"jenis": "proses", "teks": "itemService.buat(form)"},
                {"jenis": "keputusan", "teks": "aturan bisnis lolos?", "tidak": 4},
                {"jenis": "selesai", "teks": "redirect + flash sukses"},
            ],
        },
    ],
    "Kode Status HTTP dan Penanganan Error Terpusat": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Angka pertama kode status menjawab: siapa yang harus membetulkan",
            "tabel": [{
                "kolom": ["keluarga", "artinya", "yang membetulkan"],
                "baris": [
                    ["2xx", "berhasil", "nggak ada"],
                    ["3xx", "pindah alamat", "nggak ada"],
                    ["4xx", "permintaan salah", "pengirim"],
                    ["5xx", "server gagal", "kamu"],
                ],
                "sorot_baris": [2, 3],
            }],
        },
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Dua permintaan dari program PenanganGalat: 400 dan 500",
            "ket": "Stok item 61 tinggal 15 sesudah permintaan qty=5. Controller cuma "
                   "melempar, Advice yang memilih angkanya, dan isi log kasus 500 "
                   "beda dengan yang dilihat pengguna.",
            "pelaku": ["Browser", "Spring", "Controller", "Advice"],
            "pesan": [
                [0, 1, "POST /items/61/stock qty=99"],
                [1, 2, "catatKeluar(61, 99)"],
                [2, 1, "throw AturanDilanggar"],
                [1, 3, "tangani(e)"],
                [1, 0, "400 Stok kurang: tersedia 15"],
                [0, 1, "POST /items/62/stock qty=1"],
                [1, 2, "catatKeluar(62, 1)"],
                [2, 1, "NullPointerException"],
                [1, 3, "tangani(e): tulis ke log"],
                [1, 0, "500 Terjadi kesalahan di server"],
            ],
        },
    ],
    "Log: Melihat Apa yang Terjadi Saat Kamu Tidak Menonton": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Dengan level INFO di produksi, TRACE dan DEBUG nggak ditulis",
            "ket": "Contohnya diambil dari daftar lima tingkat di atas.",
            "tabel": [{
                "kolom": ["tingkat", "contoh", "ditulis?"],
                "baris": [
                    ["TRACE", "isi tiap putaran", "nggak"],
                    ["DEBUG", "parameter masuk", "nggak"],
                    ["INFO", "8813 disetujui", "ya"],
                    ["WARN", "stok kurang", "ya"],
                    ["ERROR", "database mati", "ya"],
                ],
                "sorot_baris": [2, 3, 4],
            }],
        },
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "Tumpukan panggilan saat 'connection is closed' dilempar",
            "ket": "Puncaknya tempat kejadian, dasarnya titik masuk. Urutan ini "
                   "yang dicetak di bawah Caused by, dari atas ke bawah.",
            "mode": "tumpukan",
            "isi": ["main", "simpanItem", "simpanKeDatabase"],
            "label": "call stack ContohStackTrace",
        },
    ],
    "Tampilan: JSP, Tiles, dan Kenapa Dipisah": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Tulisan di dalam ${...} memanggil getter, field-nya nggak dibaca langsung",
            "ket": "Baris terakhir salah nama objek: lubangnya kosong tanpa error. "
                   "Salah nama getter malah berakhir PropertyNotFoundException.",
            "tabel": [{
                "kolom": ["di dalam ${...}", "yang dipanggil"],
                "baris": [
                    ["item.nama", "getNama()"],
                    ["item.satuan", "getSatuan()"],
                    ["item.stokMenipis", "isStokMenipis()"],
                    ["itm.nama", "(kosong, diam)"],
                ],
                "sorot_baris": [3],
            }],
        },
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Tiles: satu rangka layout.jsp, isinya ditukar per halaman",
            "ket": "Ganti menu sekali di layout.jsp, dan lima belas halaman ikut "
                   "berubah.",
            "akar": {"teks": "layout.jsp", "anak": [
                {"teks": "header"},
                {"teks": "menu samping"},
                {"teks": "lubang isi", "anak": [{"teks": "detail.jsp"}]},
                {"teks": "footer"},
            ]},
        },
    ],
    "REST yang Membalas JSON": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "ResponseEntity menentukan angkanya: 200 dengan badan, 404 tanpa badan",
            "pelaku": ["curl", "Controller", "ItemService"],
            "pesan": [
                [0, 1, "GET /api/items/61"],
                [1, 2, "cariById(61)"],
                [2, 1, "Item 61"],
                [1, 0, "200 + JSON item"],
                [0, 1, "GET /api/items/999"],
                [1, 2, "cariById(999)"],
                [2, 1, "null"],
                [1, 0, "404, badan kosong"],
            ],
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Jackson membaca getter: hasil program JsonDariGetter",
            "ket": "catatanInternal punya field tapi nggak punya getter, jadi "
                   "hilang. stokMenipis cuma punya getter, tapi tetap terbit.",
            "tabel": [{
                "kolom": ["di kelas Item", "di JSON"],
                "baris": [
                    ["getId()", "id: 61"],
                    ["getKode()", "kode: APAR-004"],
                    ["getNama()", "nama: APAR 6kg"],
                    ["getStok()", "stok: 3"],
                    ["isStokMenipis()", "stokMenipis:true"],
                    ["catatanInternal", "(nggak muncul)"],
                ],
                "sorot_baris": [4, 5],
            }],
        },
    ],
    "Maven dan Struktur Proyek": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Struktur folder yang ditetapkan Maven, dengan lapisan jadi folder",
            "ket": "Isi target/ hasil rakitan, jadi nggak disimpan di Git.",
            "akar": {"teks": "proyek/", "anak": [
                {"teks": "pom.xml"},
                {"teks": "src/main/java", "anak": [
                    {"teks": "com/badak/ifams", "anak": [
                        {"teks": "controller"},
                        {"teks": "service"},
                        {"teks": "dao"},
                        {"teks": "model"},
                    ]},
                ]},
                {"teks": "src/main/resources", "anak": [
                    {"teks": "jdbc.properties"},
                ]},
                {"teks": "src/main/webapp", "anak": [
                    {"teks": "WEB-INF/views"},
                    {"teks": "WEB-INF/web.xml"},
                ]},
                {"teks": "src/test/java"},
                {"teks": "target"},
            ]},
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Satu kata di <scope> menentukan isi berkas .war",
            "tabel": [{
                "kolom": ["scope", "kompilasi", "berjalan", "masuk .war"],
                "baris": [
                    ["compile", "ya", "ya", "ya"],
                    ["provided", "ya", "dari server", "nggak"],
                    ["runtime", "nggak", "ya", "ya"],
                    ["test", "cuma uji", "cuma uji", "nggak"],
                ],
                "sorot_kolom": ["masuk .war"],
            }],
        },
    ],
    "Server Aplikasi: Tomcat, Servlet, dan DispatcherServlet": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Perjalanan GET /items/61 sampai jadi halaman",
            "ket": "Filter bisa menolak lebih dulu, dan kalau itu terjadi "
                   "controller nggak pernah dipanggil.",
            "pelaku": ["Browser", "Tomcat+filter", "Dispatcher", "Controller"],
            "pesan": [
                [0, 1, "GET /items/61"],
                [1, 1, "filter encoding, lalu security"],
                [1, 2, "chain.doFilter: teruskan"],
                [2, 3, "handler mapping: detail(61)"],
                [3, 2, "return \"item/detail\""],
                [2, 2, "view resolver: .../detail.jsp"],
                [2, 1, "HTML hasil JSP"],
                [1, 0, "200 + halaman"],
            ],
        },
    ],
    "Spring Boot dan Spring Data JPA": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "findByNamaContainingIgnoreCase dipotong di kata sambungnya",
            "ket": "Hasil program NamaJadiQuery untuk nama ini: SELECT * FROM item "
                   "WHERE LOWER(nama) LIKE LOWER(?).",
            "tabel": [{
                "kolom": ["potongan", "artinya"],
                "baris": [
                    ["findBy", "mulai syarat"],
                    ["Nama", "kolom nama"],
                    ["Containing", "LIKE %...%"],
                    ["IgnoreCase", "abaikan kapital"],
                ],
            }],
        },
    ],
    "Login: Sesi, Sandi, dan CSRF": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "'Sudah login' cuma nomor sesi yang bolak-balik lewat cookie",
            "ket": "Nilai-nilainya dari program SimulasiSesi. Catatan 'S1 = budi' "
                   "nggak pernah meninggalkan server.",
            "pelaku": ["Browser", "Server", "Gudang sesi"],
            "pesan": [
                [0, 1, "GET /items (tanpa cookie)"],
                [1, 0, "302 ke /login"],
                [0, 1, "POST /login budi, cocok"],
                [1, 2, "simpan S1 = budi"],
                [1, 0, "Set-Cookie: JSESSIONID=S1"],
                [0, 1, "GET /items, JSESSIONID=S1"],
                [1, 2, "S1 siapa?"],
                [2, 1, "budi"],
                [1, 0, "200 halaman untuk budi"],
            ],
        },
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Formulir asli membawa _csrf, formulir jebakan nggak bisa",
            "ket": "Cookie sesi ikut terkirim di kedua POST. Yang membedakan cuma "
                   "token yang nggak bisa dibaca halaman lain.",
            "pelaku": ["Situs jebakan", "Browser Budi", "B-iFAMS"],
            "pesan": [
                [1, 2, "buka /requests/17"],
                [2, 1, "formulir + token _csrf acak"],
                [1, 2, "POST approve, cookie + _csrf"],
                [2, 1, "302, disetujui"],
                [0, 1, "formulir jebakan, kirim sendiri"],
                [1, 2, "POST approve, cookie saja"],
                [2, 1, "403, token nggak ada"],
            ],
        },
    ],
    "Keamanan: Autentikasi vs Otorisasi": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Dua lapis pemeriksaan sesudah login, supaya satu yang mati tertahan",
            "ket": "Di bug B-iFAMS lapis method mati tanpa tanda. Lapis URL yang "
                   "ditambahkan sesudahnya jadi penahan kedua.",
            "langkah": [
                {"jenis": "masukan", "teks": "permintaan dari akun yang login"},
                {"jenis": "keputusan", "teks": "lapis URL: perannya boleh?",
                 "tidak": 4},
                {"jenis": "keputusan", "teks": "@PreAuthorize lolos?", "tidak": 4},
                {"jenis": "selesai", "teks": "method controller jalan"},
                {"jenis": "selesai", "teks": "403 Forbidden"},
            ],
        },
    ],
    "Database di Produksi": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Yang terjadi saat aplikasi start dengan Flyway dan validate",
            "ket": "Skrip lama yang disunting ketahuan lewat checksum. Skrip baru "
                   "dijalankan berurutan, baru Hibernate memeriksa kecocokannya.",
            "langkah": [
                {"jenis": "mulai", "teks": "aplikasi start"},
                {"jenis": "keputusan", "teks": "checksum skrip lama cocok?",
                 "tidak": 7},
                {"jenis": "keputusan", "teks": "ada skrip bernomor baru?",
                 "tidak": 5},
                {"jenis": "proses", "teks": "jalankan skrip berikutnya"},
                {"jenis": "proses", "teks": "catat di flyway_schema_history",
                 "ke": 2},
                {"jenis": "keputusan", "teks": "validate: entitas cocok?",
                 "tidak": 7},
                {"jenis": "selesai", "teks": "aplikasi siap melayani"},
                {"jenis": "selesai", "teks": "gagal start, baca log"},
            ],
        },
    ],
    "Satu Kode, Banyak Lingkungan: Konfigurasi dan Rahasia": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Kode yang sama, nilai yang dipakai tergantung profil aktif",
            "ket": "Disingkat dari berkas dev dan prod di atas. Sandi prod cuma "
                   "berupa placeholder yang diisi saat aplikasi dijalankan.",
            "tabel": [{
                "kolom": ["kunci", "profil dev", "profil prod"],
                "baris": [
                    ["app.nama", "B-iFAMS", "B-iFAMS"],
                    ["jdbc.url", "H2 di memori", "Oracle (server)"],
                    ["jdbc.username", "sa", "BIFAMS_FS"],
                    ["jdbc.password", "(kosong)", "${DB_PASSWORD}"],
                    ["log.level", "DEBUG", "WARN"],
                ],
                "sorot_baris": [3],
            }],
        },
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "Kalau satu kunci diisi di beberapa tempat, yang paling atas menang",
            "mode": "tumpukan",
            "isi": ["berkas properties", "variabel env", "baris perintah"],
            "label": "makin dekat saat dijalankan",
        },
    ],
    "Dua Pengguna Bersamaan: Race Condition dan Penguncian": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "@Version: dua permintaan membaca versi 7, cuma satu yang lolos",
            "ket": "UPDATE kedua masih menuntut version = 7, padahal di tabel "
                   "sudah 8. Nol baris berubah, dan Hibernate melempar "
                   "OptimisticLockException.",
            "pelaku": ["Permintaan A", "Database", "Permintaan B"],
            "pesan": [
                [0, 1, "baca stok 20, version 7"],
                [2, 1, "baca stok 20, version 7"],
                [0, 1, "UPDATE ... WHERE version = 7"],
                [1, 0, "1 baris, version jadi 8"],
                [2, 1, "UPDATE ... WHERE version = 7"],
                [1, 2, "0 baris: exception"],
            ],
        },
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Ringkasan: kapan pakai cara yang mana",
            "langkah": [
                {"jenis": "mulai", "teks": "dua penulis bisa bentrok"},
                {"jenis": "keputusan", "teks": "aturannya muat di satu WHERE?",
                 "tidak": 3},
                {"jenis": "selesai", "teks": "UPDATE yang menghitung sendiri"},
                {"jenis": "keputusan", "teks": "bentrok jarang, ulang murah?",
                 "tidak": 5},
                {"jenis": "selesai", "teks": "optimistic: @Version"},
                {"jenis": "selesai", "teks": "pessimistic: FOR UPDATE"},
            ],
        },
    ],
    "Kontainer: Docker dan docker-compose": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Yang tersisa sesudah sebuah kontainer dihapus",
            "ket": "Data database yang nggak ditaruh di volume ikut hilang "
                   "bersama lapisan tulis kontainernya.",
            "tabel": [{
                "kolom": ["benda", "kalau dihapus"],
                "baris": [
                    ["image", "tetap ada"],
                    ["kontainer", "hilang"],
                    ["lapisan tulis", "ikut hilang"],
                    ["volume", "tetap ada"],
                ],
                "sorot_baris": [2, 3],
            }],
        },
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "docker compose up: db sehat dulu, baru app nyala",
            "ket": "app menyambung ke nama layanan db. Kata localhost di dalam "
                   "kontainer app artinya kontainer app sendiri.",
            "pelaku": ["compose", "db", "app"],
            "pesan": [
                [0, 1, "nyalakan postgres:16"],
                [0, 1, "tunggu healthcheck pg_isready"],
                [1, 0, "sehat (service_healthy)"],
                [0, 2, "nyalakan app"],
                [2, 1, "jdbc:postgresql://db:5432"],
                [1, 2, "koneksi diterima"],
            ],
        },
    ],
    "Deploy, Cadangan, dan Cara Mundur": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Enam langkah deploy, dan jalan mundurnya",
            "ket": "Jalan mundur cuma ada karena langkah 2 dikerjakan.",
            "langkah": [
                {"jenis": "mulai", "teks": "1. rakit: mvn clean package"},
                {"jenis": "proses", "teks": "2. cadangkan .war lama"},
                {"jenis": "proses", "teks": "3. hentikan: shutdown.sh"},
                {"jenis": "proses", "teks": "4. tukar .war"},
                {"jenis": "proses", "teks": "5. nyalakan: startup.sh"},
                {"jenis": "keputusan", "teks": "6. log bersih, halaman normal?",
                 "tidak": 7},
                {"jenis": "selesai", "teks": "deploy selesai"},
                {"jenis": "selesai", "teks": "mundur pakai cadangan langkah 2"},
            ],
        },
    ],
    "Menguji Seperti Pengguna Sungguhan": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "Daftar uji 'stok 20, keluar berapa?': yang disorot ada di batas",
            "ket": "20 berhasil, 21 ditolak, 0 ditolak. Kesalahan paling sering "
                   "bersembunyi di angka-angka itu.",
            "nama": "jumlah keluar",
            "isi": ["-5", "0", "5", "20", "21"],
            "sorot": [1, 3, 4],
            "penunjuk": {"stok": 3},
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Layar bilang item terhapus, tabelnya masih menyimpan rujukannya",
            "ket": "Angkanya contoh. Dua baris permintaan menunjuk item 61 yang "
                   "udah nggak ada, dan cuma SQL yang menunjukkannya.",
            "tabel": [
                {
                    "nama": "item",
                    "kolom": ["id", "kode"],
                    "baris": [],
                },
                {
                    "nama": "request_item",
                    "kolom": ["request_id", "item_id", "jumlah"],
                    "baris": [["17", "61", "2"], ["18", "61", "1"]],
                    "sorot_kolom": ["item_id"],
                },
            ],
            "panah": "item_id 61 menunjuk baris yang udah dihapus",
        },
    ],
    "Menulis Uji Otomatis: Mock, MockMvc, dan Uji Integrasi": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Uji permintaanBerlebihDitolak, langkah demi langkah",
            "ket": "Boneka cuma menjawab yang diajarkan, lalu verify memastikan "
                   "simpan() nggak pernah terpanggil.",
            "pelaku": ["Uji", "ItemService", "mock ItemDao"],
            "pesan": [
                [0, 2, "when cariById(1L) -> item"],
                [0, 1, "keluarkan(1L, 21)"],
                [1, 2, "cariById(1L)"],
                [2, 1, "item, stok 20"],
                [1, 0, "throw AturanDilanggar"],
                [0, 2, "verify: simpan() never?"],
                [2, 0, "0 panggilan: lulus"],
            ],
        },
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Seberapa banyak yang dinyalakan tiap jenis uji",
            "ket": "Makin ke bawah makin ringan, tapi makin sedikit yang terbukti "
                   "soal database.",
            "tabel": [{
                "kolom": ["jenis uji", "yang menyala", "database"],
                "baris": [
                    ["@SpringBootTest", "semua bean", "sungguhan"],
                    ["@DataJpaTest", "entitas, repo", "sementara"],
                    ["@WebMvcTest", "lapisan web", "nggak ada"],
                    ["unit + mock", "tanpa Spring", "nggak ada"],
                ],
            }],
        },
    ],
}
