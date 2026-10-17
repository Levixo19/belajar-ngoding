"""Kuis modul "Bikin Aplikasi".

Soal-soal di sini menguji PERTIMBANGAN, bukan hafalan sintaks. Sebagian
besar berbentuk "di mana kode ini seharusnya ditaruh" atau "kenapa cara ini
berbahaya" - jenis pertanyaan yang benar-benar muncul saat membangun aplikasi.

Beberapa soal diangkat dari bug nyata di B-iFAMS.
"""

APLIKASI_QUIZZES = [
    {
        "title": "Kuis 1: Lapisan Aplikasi",
        "questions": [
            {
                "q": "Aturan 'stok tidak boleh negatif' paling tepat ditaruh di lapisan mana?",
                "options": ["Controller", "Service", "JSP", "DAO"],
                "answer": 1,
                "explanation": "Service adalah tempat aturan bisnis. Ditaruh di sana, aturan itu "
                               "berlaku untuk semua jalur yang mengurangi stok tanpa perlu "
                               "ditulis ulang.",
            },
            {
                "q": "Lapisan mana yang boleh berisi perintah SQL?",
                "options": ["Service", "Controller", "DAO", "Semua boleh"],
                "answer": 2,
                "explanation": "Seluruh SQL dikurung di DAO. Kalau SQL bocor ke lapisan "
                               "lain, kamu kehilangan kemampuan menjawab 'siapa saja yang "
                               "menyentuh tabel ini?'.",
            },
            {
                "q": "Ciri controller yang sehat adalah?",
                "options": [
                    "Tebal, karena semua keputusan bisnis ditulis di sana",
                    "Tipis, cuma menerjemahkan HTTP lalu panggil service",
                    "Langsung memanggil DAO supaya alurnya lebih ringkas",
                    "Menyimpan data pengguna di field static supaya cepat",
                ],
                "answer": 1,
                "explanation": "Controller cuma menerjemahkan HTTP ke Java dan sebaliknya, lalu "
                               "menyerahkan keputusannya ke service. Kalau ada 'if' rumit atau "
                               "panggilan DAO langsung di sana, biasanya itu salah tempat.",
            },
            {
                "q": "Kenapa DAO dibuat sebagai interface lebih dulu?",
                "options": [
                    "Supaya query-nya dijalankan lebih cepat oleh database",
                    "Karena Spring cuma bisa menyuntikkan sebuah interface",
                    "Supaya service tak terikat pada satu cara menyimpan",
                    "Supaya satu DAO bisa melayani semua tabel sekaligus",
                ],
                "answer": 2,
                "explanation": "Service cukup tahu apa yang bisa dilakukan DAO, nggak perlu tahu "
                               "caranya. Implementasinya bisa diganti dari Oracle ke daftar di memori "
                               "untuk pengujian tanpa mengubah service. Spring sendiri bisa "
                               "menyuntikkan class biasa; interface di sini dipilih demi desain.",
            },
            {
                "q": "Method isStokMenipis() yang cuma membandingkan field milik "
                     "sendiri paling tepat ditaruh di?",
                "options": ["Entitas", "Controller", "DAO", "JSP"],
                "answer": 0,
                "explanation": "Pertanyaan yang bisa dijawab dari field sendiri tanpa data "
                               "lain dan tanpa menyentuh database pantas ada di entitas.",
            },
            {
                "q": "Apa akibatnya kalau aturan bisnis ditulis di tiga controller berbeda?",
                "options": [
                    "Aman, asalkan ketiga salinannya ditulis persis sama",
                    "Saat aturan berubah, satu salinan bisa terlupa diubah",
                    "Aplikasi melambat karena aturan diperiksa tiga kali",
                    "Spring menolak start karena ada bean yang kembar",
                ],
                "answer": 1,
                "explanation": "Duplikasi aturan hampir selalu berakhir dengan salinan yang "
                               "tertinggal waktu aturannya berubah, dan celahnya masuk lewat jalur "
                               "yang terlupa. Hari ini ketiganya mungkin sama persis; masalahnya "
                               "muncul belakangan.",
            },
        ],
    },
    {
        "title": "Kuis 2: Model Data",
        "questions": [
            {
                "q": "Satu kategori punya banyak item. Di mana id penghubungnya disimpan?",
                "options": [
                    "Di tabel kategori",
                    "Di tabel item",
                    "Di tabel penghubung terpisah",
                    "Tidak perlu disimpan",
                ],
                "answer": 1,
                "explanation": "Pada hubungan satu-ke-banyak, tabel di sisi 'banyak' yang "
                               "menyimpan id sisi 'satu'. Tabel item punya kolom category_id.",
            },
            {
                "q": "Satu permintaan berisi banyak item, dan satu item muncul di banyak "
                     "permintaan. Ini hubungan apa?",
                "options": ["Satu ke satu", "Satu ke banyak", "Banyak ke banyak", "Tidak berhubungan"],
                "answer": 2,
                "explanation": "Banyak ke banyak, dan penyelesaiannya tabel penghubung di "
                               "tengah. Di B-iFAMS namanya request_item.",
            },
            {
                "q": "Nama item ikut disimpan di tabel mutasi. Apa masalahnya?",
                "options": [
                    "Tidak masalah, karena nama item jarang sekali diganti",
                    "Ganti nama item berarti mengubah ratusan baris mutasi",
                    "Mutasi lama ikut terhapus saat nama item diganti",
                    "Mutasi jadi tidak bisa diurutkan menurut tanggalnya",
                ],
                "answer": 1,
                "explanation": "Data yang sama disimpan di dua tempat lama-lama pasti berbeda: begitu "
                               "nama item diganti, ratusan baris mutasi harus ikut diperbarui, dan "
                               "yang terlewat jadi salah. Mutasi cukup menyimpan item_id.",
            },
            {
                "q": "Cara paling praktis menemukan tabel apa saja yang dibutuhkan?",
                "options": [
                    "Menyalin dari aplikasi lain",
                    "Melingkari kata benda di dokumen kebutuhan",
                    "Membuat satu tabel besar berisi semuanya",
                    "Menunggu sampai kode selesai ditulis",
                ],
                "answer": 1,
                "explanation": "Kata benda dalam deskripsi masalah hampir selalu jadi "
                               "kandidat tabel. Sisanya disaring: mana yang sama, mana "
                               "yang sebenarnya cuma sifat.",
            },
            {
                "q": "Kenapa model data sebaiknya benar sejak awal?",
                "options": [
                    "Karena skema tabel tidak bisa diubah sama sekali",
                    "Karena mengubahnya setelah ada data asli itu berisiko",
                    "Karena Hibernate melarang tabel diubah setelah dibuat",
                    "Karena tabel baru tidak bisa ditambah belakangan",
                ],
                "answer": 1,
                "explanation": "Mirip mengganti pondasi rumah yang sudah ditinggali: bisa, tapi mahal "
                               "dan rawan merusak, karena data lama harus dipindah dan kode yang "
                               "membacanya ikut berubah. Skemanya tetap bisa diubah, cuma ongkosnya "
                               "naik begitu ada data asli.",
            },
        ],
    },
    {
        "title": "Kuis 3: HTTP, Controller, dan Tampilan",
        "questions": [
            {
                "q": "Kenapa aksi menghapus data tidak boleh dibuat sebagai GET?",
                "options": [
                    "Karena GET lebih lambat daripada POST di Spring",
                    "Browser bebas mengulang GET, misalnya saat refresh",
                    "Karena alamat GET tidak bisa membawa id datanya",
                    "Karena Spring tidak mengizinkan GET mengubah data",
                ],
                "answer": 1,
                "explanation": "GET harus aman: dipanggil berkali-kali nggak boleh mengubah apa pun. "
                               "Browser bebas mengulang GET, misalnya saat refresh, jadi menghapus "
                               "lewat GET bisa menghapus dua kali. Spring sendiri nggak melarangnya; "
                               "kamu yang harus memilih POST.",
            },
            {
                "q": "Apa gunanya pola POST-Redirect-GET?",
                "options": [
                    "Mempercepat halaman karena hasilnya disimpan di cache",
                    "Mencegah formulir terkirim ulang saat halaman di-refresh",
                    "Menyembunyikan isi formulir dari alamat di browser",
                    "Menghemat memori server karena sesinya langsung dihapus",
                ],
                "answer": 1,
                "explanation": "Tanpa redirect, refresh sesudah menyimpan mengirim ulang formulir yang "
                               "sama, dan stok berkurang dua kali dari satu pencatatan. Redirect "
                               "membuat halaman terakhir jadi GET biasa yang aman di-refresh.",
            },
            {
                "q": "Mana penulisan yang paling tepat di dalam JSP?",
                "options": [
                    "<c:if test=\"${item.stok <= item.stokMin}\">",
                    "<c:if test=\"${item.stokMenipis}\">",
                    "Keduanya sama saja",
                    "Keduanya terlarang",
                ],
                "answer": 1,
                "explanation": "Yang pertama memutuskan di tampilan, dan keputusan itu bakal "
                               "berbeda dengan yang di service begitu aturannya berubah. Yang "
                               "kedua cuma bertanya pada objek.",
            },
            {
                "q": "Apa masalah utama yang diselesaikan Apache Tiles?",
                "options": [
                    "Mempercepat query database yang dipanggil halaman",
                    "Menghindari menyalin header dan menu ke tiap halaman",
                    "Mengamankan formulir dari serangan CSRF otomatis",
                    "Mengubah JSP jadi JSON supaya bisa dipakai REST",
                ],
                "answer": 1,
                "explanation": "Tiles memisahkan rangka halaman dari isinya. Header dan menu ditulis "
                               "sekali di layout, jadi mengganti menu cukup di satu tempat dan semua "
                               "halaman ikut berubah.",
            },
            {
                "q": "Dalam pola REST, alamat mana yang paling tepat untuk melihat detail "
                     "item ber-id 61?",
                "options": ["/lihatItem?nomor=61", "/items/61", "/item/detail/get/61", "/getItem61"],
                "answer": 1,
                "explanation": "Kata benda jamak untuk kumpulan, id untuk satu benda. "
                               "Keteraturan ini membuat alamat bisa ditebak.",
            },
        ],
    },
    {
        "title": "Kuis 4: Keamanan dan Produksi",
        "questions": [
            {
                "q": "Apa beda autentikasi dan otorisasi?",
                "options": [
                    "Sama saja, cuma beda istilah",
                    "Autentikasi = siapa kamu; otorisasi = kamu boleh apa",
                    "Autentikasi = kamu boleh apa; otorisasi = siapa kamu",
                    "Autentikasi untuk admin, otorisasi untuk pengguna biasa",
                ],
                "answer": 1,
                "explanation": "Login yang benar tidak berguna kalau setelah masuk semua "
                               "orang bisa melakukan segalanya.",
            },
            {
                "q": "Menyembunyikan tombol 'Hapus' dari pengguna non-admin termasuk?",
                "options": [
                    "Pengamanan yang cukup karena tombolnya tak terlihat",
                    "Kenyamanan tampilan, belum termasuk pengamanan",
                    "Bentuk autentikasi karena memeriksa siapa yang login",
                    "Otorisasi di sisi server yang sudah lengkap",
                ],
                "answer": 1,
                "explanation": "Tombol yang disembunyikan tetap bisa dicapai dengan mengetik "
                               "alamatnya langsung. Menyembunyikan tombol cuma bikin tampilan rapi; "
                               "pengamanannya harus di server.",
            },
            {
                "q": "Di B-iFAMS, semua @PreAuthorize sudah ditulis benar tapi tidak pernah "
                     "aktif. Apa penyebabnya?",
                "options": [
                    "Pengguna di database belum diberi peran apa pun",
                    "Penghidupnya ada di wadah Spring lain dari controller",
                    "Versi Java terlalu lama untuk membaca anotasi itu",
                    "Anotasinya harus ditaruh di JSP, bukan di controller",
                ],
                "answer": 1,
                "explanation": "Mekanisme penghidupnya cuma bekerja pada penghuni wadah yang sama. "
                               "Controller ada di wadah web, konfigurasinya di wadah utama, jadi "
                               "anotasinya diam saja tanpa error. Kalau masalahnya peran yang kosong, "
                               "yang terjadi justru semua orang ditolak.",
            },
            {
                "q": "Kenapa menguji hak akses sebagai admin tidak membuktikan apa pun?",
                "options": [
                    "Karena admin memang boleh segalanya, jadi uji pasti lolos",
                    "Karena sesi admin tidak diperiksa oleh Spring Security",
                    "Karena akun admin tidak tercatat di log akses",
                    "Karena peran admin dibuat ulang setiap kali login",
                ],
                "answer": 0,
                "explanation": "Admin memang boleh segalanya, jadi uji dari akun admin selalu lolos "
                               "dan nggak menemukan apa pun. Bug hak akses cuma terlihat kalau kamu "
                               "mencoba menembus endpoint admin dari akun berperan rendah.",
            },
            {
                "q": "hibernate.hbm2ddl.auto bernilai apa yang aman untuk produksi?",
                "options": ["update", "create", "validate", "create-drop"],
                "answer": 2,
                "explanation": "validate memeriksa kecocokan skema dan menolak jalan kalau "
                               "tidak cocok, tapi tidak pernah mengubah tabel. 'update' "
                               "mengubah struktur produksi diam-diam.",
            },
            {
                "q": "Sebelum menyentuh data, cara memastikan kamu terhubung ke database "
                     "yang benar adalah?",
                "options": [
                    "Melihat nama kontainer atau server tempat database itu jalan",
                    "Baca konfigurasi aplikasi yang jalan, lalu cari baris yang pasti ada",
                    "Mencocokkan nama tabelnya dengan yang tertulis di dokumentasi",
                    "Memastikan jumlah tabelnya sama dengan database di laptopmu",
                ],
                "answer": 1,
                "explanation": "Di B-iFAMS ada database sisa dengan nama tabel yang sama persis tapi "
                               "kosong. Nama kontainer, nama tabel, dan dokumentasi bisa menipu; satu "
                               "baris data yang kamu tahu pasti ada nggak bisa.",
            },
            {
                "q": "Langkah mana yang paling sering dilewatkan padahal paling menyelamatkan "
                     "saat deploy?",
                "options": [
                    "Menulis catatan rilis untuk tim dan pengguna",
                    "Mencadangkan versi yang jalan sebelum ditimpa",
                    "Menaikkan nomor versi di berkas konfigurasi build",
                    "Menghapus log lama supaya disk server tetap lega",
                ],
                "answer": 1,
                "explanation": "Dengan cadangan, kamu bisa mundur dalam hitungan detik, bukan "
                               "memperbaiki sambil panik sementara pengguna menunggu.",
            },
        ],
    },
    {
        "title": "Kuis 5: Bean, Validasi, dan Balasan HTTP",
        "questions": [
            {
                "q": "Sebuah @Service punya field 'private final ItemDao itemDao;' dan tidak ada satu baris pun yang mengisinya. Kenapa ia tidak null saat aplikasi jalan?",
                "options": [
                    "Java mengisi field final dengan objek kosong otomatis",
                    "Spring menyerahkannya lewat argumen constructor bean itu",
                    "Field bertipe interface selalu diisi implementasi pertama",
                    "@Service membuat seluruh field kelasnya terisi sendiri",
                ],
                "answer": 1,
                "explanation": "Spring membuat bean-nya dan mencocokkan tipe: ia mencari bean "
                               "bertipe ItemDao di wadah, menemukan ItemDaoImpl, lalu "
                               "menyerahkannya lewat constructor. Karena itu memanggil 'new "
                               "RequestService()' sendiri di luar Spring memang menghasilkan "
                               "NullPointerException, sebab nggak ada yang mengisinya di situ. "
                               "Refleksi dipakai pada bentuk lama @Autowired di field, bukan "
                               "pada injeksi lewat constructor.",
            },
            {
                "q": "Apa bedanya @Service dan @Component di mata Spring?",
                "options": [
                    "@Service menyalakan transaksi database pada methodnya",
                    "Nyaris tidak ada; bedanya untuk manusia yang membacanya",
                    "@Service membuat bean-nya dibuat lebih dulu dari yang lain",
                    "@Service cuma boleh dipakai pada kelas yang punya interface",
                ],
                "answer": 1,
                "explanation": "@Service, @Repository, dan @Controller sebenarnya @Component "
                               "juga, cuma diberi nama sesuai lapisannya. Buat Spring keduanya "
                               "nyaris identik; bedanya buat pembaca: sekali lihat baris pertama "
                               "sebuah kelas, kamu tahu ia duduk di lapisan mana. Yang sering "
                               "dikira: @Service menyalakan transaksi. Itu pekerjaan "
                               "@Transactional.",
            },
            {
                "q": "Kenapa injeksi lewat constructor lebih disukai daripada @Autowired di field?",
                "options": [
                    "Karena constructor dijalankan lebih cepat oleh Spring",
                    "Karena @Autowired sudah dihapus sejak Spring versi 4.3",
                    "Karena field-nya bisa final, jadi mustahil null oleh struktur",
                    "Karena injeksi constructor tidak membutuhkan wadah Spring",
                ],
                "answer": 2,
                "explanation": "Dengan constructor, compiler memaksa field terisi sebelum "
                               "objeknya selesai dibuat, jadi ia boleh final dan secara struktur "
                               "mustahil null. @Autowired di field mengisinya sesudah objeknya "
                               "ada, sehingga final nggak mungkin dipakai. Sejak Spring 4.3 "
                               "constructor tunggal memang nggak perlu ditandai apa pun, tapi "
                               "@Autowired sendiri nggak dihapus.",
            },
            {
                "q": "Di Spring MVC gaya lama ada dua wadah: web (anak) dan root (induk). Mana yang TIDAK bisa terjadi?",
                "options": [
                    "Service di wadah root meminta bean dari wadah web",
                    "Controller di wadah web meminta service dari wadah root",
                    "Kedua wadah memakai berkas konfigurasi yang berbeda",
                    "Wadah root berisi DataSource dan PasswordEncoder",
                ],
                "answer": 0,
                "explanation": "Panahnya searah: anak boleh melihat isi induknya, induk nggak "
                               "bisa melihat isi anaknya. Penghuni wadah root (@Service, "
                               "@Repository, DataSource) nggak tahu-menahu soal isi wadah web. "
                               "Tiga pilihan lain justru hal yang memang terjadi. Ini juga "
                               "sebabnya konfigurasi keamanan yang ditaruh di wadah yang salah "
                               "membuat anotasi hak akses diam saja tanpa error.",
            },
            {
                "q": "'Stok tidak boleh negatif' termasuk validasi bentuk atau aturan bisnis?",
                "options": [
                    "Validasi bentuk, karena cukup memeriksa angkanya saja",
                    "Validasi bentuk, karena bisa ditulis sebagai anotasi @Min",
                    "Aturan bisnis, karena butuh melihat stok yang ada sekarang",
                    "Aturan bisnis, karena selalu melibatkan lebih dari satu tabel",
                ],
                "answer": 2,
                "explanation": "Patokannya satu kalimat: kalau untuk memutuskan kamu perlu membuka database, itu aturan bisnis; kalau cukup melihat isi formulirnya, itu validasi bentuk. Menghitung stok sesudah pengurangan menuntut stok saat ini, jadi ia aturan bisnis dan tempatnya di service. Jumlah tabel tidak menentukan apa pun, dan tidak setiap aturan bisa dijadikan anotasi.",
            },
            {
                "q": "Apa yang sebenarnya dibedakan garis antara kode 4xx dan 5xx?",
                "options": [
                    "Seberapa parah akibatnya bagi pengguna yang meminta",
                    "Siapa yang harus memperbaiki supaya permintaannya berhasil",
                    "Apakah balasan itu membawa badan atau dikirim kosong",
                    "Apakah kesalahannya terjadi sebelum atau sesudah login",
                ],
                "answer": 1,
                "explanation": "4xx berarti kesalahannya di sisi pengirim: mengulang permintaan "
                               "yang sama persis akan gagal lagi, datanya dulu yang harus "
                               "dibetulkan. 5xx berarti permintaannya wajar tapi server yang "
                               "gagal memenuhinya. Pembagian ini punya akibat nyata: alat "
                               "pemantau menghitung 5xx dan membangunkan orang tengah malam, "
                               "sedangkan 4xx nggak membangunkan siapa-siapa.",
            },
            {
                "q": "Controller menangkap exception lalu 'return \"error\";' untuk menampilkan halaman kesalahan. Apa masalahnya?",
                "options": [
                    "Halaman error tidak bisa menampilkan pesan exception-nya",
                    "Exception-nya tertelan sehingga tidak pernah masuk ke log",
                    "Statusnya tetap 200, jadi kegagalannya tak terlihat mesin",
                    "Spring akan mencari controller lain bernama 'error' dulu",
                ],
                "answer": 2,
                "explanation": "Halamannya memang memberi tahu manusia, tapi angka statusnya "
                               "tetap 200 OK, dan yang dibaca program adalah angkanya. Alat "
                               "pemantau, aplikasi lain yang memanggilmu, dan access log "
                               "semuanya menyimpulkan permintaan itu berhasil. Kerusakan yang "
                               "dibalas 200 nggak pernah muncul di grafik mana pun. Log-nya "
                               "sendiri masih bisa terisi; yang hilang statusnya.",
            },
            {
                "q": "Pengguna sudah login, tapi perannya tidak berhak membuka halaman itu. Kode status yang tepat?",
                "options": [
                    "401 Unauthorized",
                    "403 Forbidden",
                    "404 Not Found",
                    "405 Method Not Allowed",
                ],
                "answer": 1,
                "explanation": "401 berarti kamu belum dikenali: belum login, atau sesimu "
                               "kedaluwarsa. 403 berarti kamu sudah dikenali tapi perannya nggak "
                               "berhak. Namanya memang menyesatkan: 'Unauthorized' terdengar "
                               "seperti soal hak akses, padahal ia soal identitas. 404 dipakai "
                               "kalau datanya memang nggak ada, 405 kalau alamatnya benar tapi "
                               "methodnya salah.",
            },
        ],
    },
]
