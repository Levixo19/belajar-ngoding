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
                "explanation": "Service adalah tempat aturan bisnis. Ditaruh di sana, "
                               "aturan itu berlaku untuk SEMUA jalur yang mengurangi stok "
                               "tanpa perlu ditulis ulang.",
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
                    "Tebal, berisi semua keputusan",
                    "Tipis, cuma menghubungkan HTTP dengan service",
                    "Berisi query database langsung",
                    "Menyimpan data di variabel static",
                ],
                "answer": 1,
                "explanation": "Controller cuma menerjemahkan HTTP ke Java dan sebaliknya. "
                               "Kalau ada 'if' rumit di sana, biasanya salah tempat.",
            },
            {
                "q": "Kenapa DAO dibuat sebagai interface lebih dulu?",
                "options": [
                    "Supaya lebih cepat dijalankan",
                    "Karena Java mewajibkannya",
                    "Supaya service tidak terikat pada satu cara penyimpanan",
                    "Supaya file-nya lebih sedikit",
                ],
                "answer": 2,
                "explanation": "Service cukup tahu APA yang bisa dilakukan, bukan CARANYA. "
                               "Implementasinya bisa diganti dari Oracle ke daftar di memori "
                               "untuk pengujian tanpa mengubah service.",
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
                    "Aplikasi jadi lebih cepat",
                    "Suatu hari satu di antaranya lupa diperbarui dan jadi celah",
                    "Tidak ada bedanya",
                    "Java akan menolak mengompilasi",
                ],
                "answer": 1,
                "explanation": "Duplikasi aturan selalu berakhir dengan salinan yang "
                               "tertinggal saat aturannya berubah - dan celah itu masuk "
                               "lewat jalur yang terlupakan.",
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
                               "tengah - di B-iFAMS namanya request_item.",
            },
            {
                "q": "Nama item ikut disimpan di tabel mutasi. Apa masalahnya?",
                "options": [
                    "Tidak ada masalah",
                    "Mengganti nama item harus memperbarui ratusan baris mutasi",
                    "Databasenya jadi lebih cepat",
                    "Mutasi tidak bisa diurutkan",
                ],
                "answer": 1,
                "explanation": "Data yang sama disimpan di dua tempat selalu berakhir "
                               "berbeda. Mutasi cukup menyimpan item_id.",
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
                    "Karena tidak bisa diubah sama sekali",
                    "Karena mengubahnya setelah ada data asli itu berat dan berisiko",
                    "Karena Hibernate melarangnya",
                    "Karena tidak berpengaruh pada kode",
                ],
                "answer": 1,
                "explanation": "Seperti mengganti pondasi rumah yang sudah ditinggali. "
                               "Bisa, tapi mahal dan rawan merusak.",
            },
        ],
    },
    {
        "title": "Kuis 3: HTTP, Controller, dan Tampilan",
        "questions": [
            {
                "q": "Kenapa aksi menghapus data tidak boleh dibuat sebagai GET?",
                "options": [
                    "Karena GET lebih lambat",
                    "Karena browser bebas memanggil GET kapan saja, termasuk saat refresh",
                    "Karena GET tidak bisa mengirim id",
                    "Karena GET tidak didukung Spring",
                ],
                "answer": 1,
                "explanation": "GET harus aman: dipanggil berkali-kali tidak mengubah apa "
                               "pun. Menghapus lewat GET berarti satu refresh bisa "
                               "menghapus dua kali.",
            },
            {
                "q": "Apa gunanya pola POST-Redirect-GET?",
                "options": [
                    "Mempercepat halaman",
                    "Mencegah formulir terkirim dua kali saat pengguna me-refresh",
                    "Menghemat memori server",
                    "Menyembunyikan URL",
                ],
                "answer": 1,
                "explanation": "Tanpa redirect, refresh setelah menyimpan mengirim ulang "
                               "formulir yang sama - dan stok berkurang dua kali dari satu "
                               "pencatatan.",
            },
            {
                "q": "Mana penulisan yang BENAR di dalam JSP?",
                "options": [
                    "<c:if test=\"${item.stok <= item.stokMin}\">",
                    "<c:if test=\"${item.stokMenipis}\">",
                    "Keduanya sama saja",
                    "Keduanya terlarang",
                ],
                "answer": 1,
                "explanation": "Yang pertama MEMUTUSKAN di tampilan, dan keputusan itu akan "
                               "berbeda dengan yang di service begitu aturannya berubah. "
                               "Yang kedua cuma bertanya pada objek.",
            },
            {
                "q": "Apa masalah utama yang diselesaikan Apache Tiles?",
                "options": [
                    "Mempercepat query database",
                    "Menghindari menyalin header dan menu ke lima belas halaman",
                    "Mengamankan formulir",
                    "Mengompilasi Java lebih cepat",
                ],
                "answer": 1,
                "explanation": "Tiles memisahkan rangka dari isi. Ganti menu sekali di "
                               "layout, semua halaman ikut berubah.",
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
                    "Pengamanan yang cukup",
                    "Kenyamanan tampilan, BUKAN pengamanan",
                    "Bentuk autentikasi",
                    "Cara mempercepat halaman",
                ],
                "answer": 1,
                "explanation": "Tombol yang disembunyikan tetap bisa dicapai dengan "
                               "mengetik alamatnya langsung. Pengamanan harus di server.",
            },
            {
                "q": "Di B-iFAMS, semua @PreAuthorize sudah ditulis benar tapi tidak pernah "
                     "aktif. Apa penyebabnya?",
                "options": [
                    "Salah ketik nama peran",
                    "Konfigurasi penghidupnya ditaruh di wadah Spring yang berbeda dari controller",
                    "Versi Java terlalu lama",
                    "Databasenya tidak mendukung",
                ],
                "answer": 1,
                "explanation": "Mekanisme penghidupnya hanya bekerja pada penghuni wadah "
                               "yang sama. Controller ada di wadah web, konfigurasinya di "
                               "wadah utama - jadi anotasinya diam saja.",
            },
            {
                "q": "Kenapa menguji hak akses sebagai admin tidak membuktikan apa pun?",
                "options": [
                    "Karena admin lebih lambat",
                    "Karena admin memang boleh segalanya, jadi semua uji akan lolos",
                    "Karena admin tidak punya sesi",
                    "Karena admin tidak tercatat di log",
                ],
                "answer": 1,
                "explanation": "Bug hak akses hanya terlihat kalau diuji dari akun berperan "
                               "rendah yang mencoba menembus endpoint admin.",
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
                    "Melihat nama kontainer atau nama servernya",
                    "Membaca konfigurasi aplikasi yang sedang berjalan, lalu mencari satu "
                    "baris yang kamu tahu pasti ada",
                    "Mempercayai dokumentasi",
                    "Menebak dari nama tabel",
                ],
                "answer": 1,
                "explanation": "Di B-iFAMS ada database sisa dengan nama tabel yang sama "
                               "persis tapi kosong. Nama menipu; isi tidak.",
            },
            {
                "q": "Langkah mana yang paling sering dilewatkan padahal paling menyelamatkan "
                     "saat deploy?",
                "options": [
                    "Menulis catatan rilis",
                    "Mencadangkan versi yang sedang berjalan sebelum ditimpa",
                    "Mengganti nomor versi",
                    "Menghapus log lama",
                ],
                "answer": 1,
                "explanation": "Dengan cadangan, kamu bisa mundur dalam hitungan detik "
                               "alih-alih memperbaiki dalam panik sementara pengguna menunggu.",
            },
        ],
    },
]
