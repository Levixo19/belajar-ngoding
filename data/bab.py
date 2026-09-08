"""Pembagian materi tiap bahasa menjadi bab yang terbuka bertahap.

Kenapa ada: puluhan materi yang berbaris rata dari atas ke bawah adalah daftar,
bukan jalur. Buat orang yang belajar dari nol, daftar sepanjang itu tidak
memberi tahu apa pun tentang mana yang harus lebih dulu, mana yang boleh
ditunda, dan sudah sampai mana ia sekarang. Bab menjawab ketiganya sekaligus,
dan pintu yang baru terbuka memberi satu hal yang tidak bisa diberikan daftar:
tanda bahwa sesuatu sudah benar-benar selesai.

BENTUK DATANYA sengaja hanya menunjuk RENTANG INDEKS, bukan menyalin judul.
Judul materi adalah bagian dari kunci progres (lihat AGENTS.md — judul wajib
unik per bahasa, dan mengubahnya menghapus progres), jadi menuliskannya di dua
tempat berarti membuka peluang keduanya berbeda tanpa ada yang tahu. Rentang
indeks tidak punya masalah itu, dan tes memastikan rentangnya menutupi seluruh
materi tanpa celah maupun tumpang tindih.

TINGKAT ("dasar" / "menengah" / "mahir") ada supaya orang tahu apa yang sedang
ia hadapi sebelum membukanya. Tingkat tidak pernah MENURUN dari satu bab ke bab
berikutnya — kurikulum yang naik lalu turun lagi membuat orang mengira ia salah
membaca urutan.

Yang dikelompokkan HANYA materi. Kuis dan latihan sengaja dibiarkan sebagai
daftarnya sendiri: hubungan antara "Kuis 3" dan bab tertentu sering tidak
sejelas yang dikira, dan memaksakan pemetaan yang mengada-ada akan membuat
pelajar mengira ia melewatkan sesuatu padahal tidak.

BERKAS INI DIHASILKAN dari spesifikasi "judul, tingkat, berapa materi" — bukan
diketik tangan. Rentang indeks yang diketik tangan adalah undangan bagi
kesalahan yang tidak kelihatan: salah satu angka membuat seluruh bab sesudahnya
bergeser tanpa satu pun tanda di layar. Kalau materi bertambah, ubah jumlah di
spesifikasinya lalu hasilkan ulang.
"""

BAB = {
    "html": [
        {
        "judul": "Halaman Pertama dan Kerangkanya",
        "ket":
            "Menulis berkas HTML pertama, menutup tag dengan benar, "
            "membaca pohonnya, dan menandai teks.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Isi Halaman dan Cara Menyajikannya",
        "ket":
            "Menandai kutipan dan waktu, menyusun daftar, menautkan "
            "halaman dan gambar, lalu menjalankannya lewat server "
            "lokal.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 8,
        },
        {
        "judul": "Atribut, Gaya, dan Makna",
        "ket":
            "Memberi keterangan pada elemen, menempelkan CSS dan "
            "JavaScript, dan memilih elemen yang menyebut perannya "
            "sendiri.",
        "tingkat": "dasar",
        "awal": 8, "akhir": 11,
        },
        {
        "judul": "Gambar, Media, dan Tabel",
        "ket":
            "Gambar responsif, SVG sebaris, video, konten tersemat, dan "
            "data yang berbaris-kolom.",
        "tingkat": "menengah",
        "awal": 11, "akhir": 14,
        },
        {
        "judul": "Formulir, Widget, dan Akses untuk Semua",
        "ket":
            "Menerima masukan, memvalidasi, mengunggah berkas, memakai "
            "widget bawaan browser, dan menamai semuanya untuk pembaca "
            "layar.",
        "tingkat": "menengah",
        "awal": 14, "akhir": 19,
        },
        {
        "judul": "Halaman Utuh dan Kode Sungguhan",
        "ket":
            "Metadata, merakit semuanya jadi satu halaman, dan membaca "
            "berkas .html buatan orang lain.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 22,
        },
    ],
    "css": [
        {
        "judul": "Aturan Pertama dan Cara Memeriksanya",
        "ket":
            "Menulis aturan CSS, memilih elemen yang tepat, dan melihat "
            "sendiri di browser aturan mana yang menang.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Warna, Ukuran, dan Huruf",
        "ket":
            "Menentukan warna, memilih satuan yang benar, menghitung "
            "ukuran di dalam CSS, dan menata teks.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 6,
        },
        {
        "judul": "Kotak, Alur, dan Latarnya",
        "ket":
            "Mengatur ruang di dalam dan di luar kotak, mengubah alur "
            "dokumen, lalu memberinya latar dan gambar.",
        "tingkat": "dasar",
        "awal": 6, "akhir": 9,
        },
        {
        "judul": "Rupa dan Teks yang Tidak Muat",
        "ket":
            "Bayangan, filter, transform, dan cara memotong teks yang "
            "lebih panjang dari kotaknya.",
        "tingkat": "menengah",
        "awal": 9, "akhir": 12,
        },
        {
        "judul": "Tata Letak",
        "ket":
            "Menyusun halaman dengan flexbox dan grid, sampai float "
            "yang masih memenuhi kode lama.",
        "tingkat": "menengah",
        "awal": 12, "akhir": 16,
        },
        {
        "judul": "Keadaan, Kedalaman, dan Gerak",
        "ket":
            "Menumpuk elemen, menanggapi kursor dan fokus, lalu membuat "
            "perubahannya bergerak halus.",
        "tingkat": "menengah",
        "awal": 16, "akhir": 19,
        },
        {
        "judul": "Komponen dan Halaman Utuh",
        "ket":
            "Menata tabel dan formulir, menyesuaikan diri ke lebar "
            "layar apa pun, dan menyatukan semuanya lewat variabel.",
        "tingkat": "menengah",
        "awal": 19, "akhir": 23,
        },
        {
        "judul": "CSS Zaman Sekarang",
        "ket":
            "Pemilih dan at-rule baru, properti logis, dan cara membaca "
            "CSS di repo orang lain.",
        "tingkat": "mahir",
        "awal": 23, "akhir": 26,
        },
    ],
    "java": [
        {
        "judul": "Menjalankan Program Java Pertama",
        "ket":
            "Memasang Java, memahami baris-baris pembuka sebuah berkas, "
            "menyimpan nilai, dan menghitung.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 5,
        },
        {
        "judul": "Mengatur Alur dan Memecah Kode",
        "ket":
            "Percabangan, perulangan, array, method, dan method yang "
            "memanggil dirinya sendiri.",
        "tingkat": "dasar",
        "awal": 5, "akhir": 10,
        },
        {
        "judul": "Merancang Class Sendiri",
        "ket":
            "Membuat class beserta constructor, anggota static, enum, "
            "dan data yang terlindungi.",
        "tingkat": "dasar",
        "awal": 10, "akhir": 14,
        },
        {
        "judul": "Pewarisan, Interface, dan Java Modern",
        "ket":
            "Menurunkan class, menyeragamkan perilaku lewat interface, "
            "dan membaca sintaks Java terbaru.",
        "tingkat": "menengah",
        "awal": 14, "akhir": 20,
        },
        {
        "judul": "Menangani Error dan Mengolah Koleksi",
        "ket":
            "Menangkap error, membaca stack trace, memakai "
            "List/Map/Set, string, dan tanggal.",
        "tingkat": "menengah",
        "awal": 20, "akhir": 26,
        },
        {
        "judul": "Mengolah Data dengan Lambda & Stream",
        "ket":
            "Lambda, pengurutan objek, class bersarang, stream, "
            "generics, dan menghindari null.",
        "tingkat": "menengah",
        "awal": 26, "akhir": 32,
        },
        {
        "judul": "Berjalan Bersamaan dan Menyimpan Data",
        "ket": "Thread, tugas asinkron, berkas, dan database.",
        "tingkat": "mahir",
        "awal": 32, "akhir": 36,
        },
        {
        "judul": "Bekerja Seperti Developer Profesional",
        "ket":
            "Unit test, design pattern, Git dan build tool, serta arah "
            "belajar sesudah ini.",
        "tingkat": "mahir",
        "awal": 36, "akhir": 40,
        },
    ],
    "sql": [
        {
        "judul": "Tabel Pertama",
        "ket":
            "Membuat tabel, memilih tipe kolom yang tepat, dan melihat "
            "isi database yang sudah ada sebelum menyentuh apa pun.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Mengisi & Menanyai Data",
        "ket":
            "Memasukkan data lalu mengambil, menghitung, menyaring, dan "
            "meringkasnya.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 8,
        },
        {
        "judul": "Banyak Tabel Sekaligus",
        "ket":
            "JOIN, subquery, fungsi bawaan, dan perintah yang datanya "
            "diambil dari query lain.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 13,
        },
        {
        "judul": "Query yang Cepat & Aman",
        "ket":
            "Index, normalisasi, query berparameter, hak akses, dan "
            "membaca rencana eksekusi.",
        "tingkat": "menengah",
        "awal": 13, "akhir": 16,
        },
        {
        "judul": "Analitik & Objek Database",
        "ket":
            "Window function, CTE rekursif, view, stored procedure, dan "
            "trigger.",
        "tingkat": "mahir",
        "awal": 16, "akhir": 19,
        },
        {
        "judul": "Logika Prosedural, Transaksi & Langkah Berikutnya",
        "ket":
            "Menulis blok prosedural di database, menjaga konsistensi "
            "data, dan arah belajar sesudahnya.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 22,
        },
    ],
    "python": [
        {
        "judul": "Menjalankan Program Pertama",
        "ket":
            "Memasang Python, menyimpan nilai, dan bertukar data dengan "
            "pengguna lewat input dan print.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Mengatur Alur Program",
        "ket":
            "Berhitung dengan benar, mengambil keputusan, dan mengulang "
            "pekerjaan.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 7,
        },
        {
        "judul": "Menyimpan Banyak Data",
        "ket":
            "Teks, list, tuple, dictionary, set, dan wadah siap pakai "
            "dari pustaka standar.",
        "tingkat": "dasar",
        "awal": 7, "akhir": 12,
        },
        {
        "judul": "Memecah Program Jadi Fungsi",
        "ket":
            "Menulis fungsi, memahami apa yang sebenarnya dioper ke "
            "dalamnya, dan rekursi.",
        "tingkat": "dasar",
        "awal": 12, "akhir": 15,
        },
        {
        "judul": "Menulis Fungsi seperti Kode Nyata",
        "ket":
            "Unpacking, anotasi tipe, lambda, closure, dan "
            "comprehension.",
        "tingkat": "menengah",
        "awal": 15, "akhir": 20,
        },
        {
        "judul": "Pemrograman Berorientasi Objek",
        "ket":
            "Class, pewarisan, kontrak abstrak, dunder method, "
            "dataclass, dan Enum.",
        "tingkat": "menengah",
        "awal": 20, "akhir": 25,
        },
        {
        "judul": "Kesalahan dan Struktur Project",
        "ket":
            "Menangkap error, membaca traceback, serta menata modul dan "
            "berkas project.",
        "tingkat": "menengah",
        "awal": 25, "akhir": 29,
        },
        {
        "judul": "Program yang Bicara dengan Sistem",
        "ket":
            "Argumen baris perintah, environment, logging, waktu, dan "
            "berkas.",
        "tingkat": "menengah",
        "awal": 29, "akhir": 33,
        },
        {
        "judul": "Mengolah Teks dan Aliran Data",
        "ket":
            "Encoding, bytes, regular expression, iterator, generator, "
            "dan itertools.",
        "tingkat": "menengah",
        "awal": 33, "akhir": 37,
        },
        {
        "judul": "Membentuk Perilaku dan Menjalankan Serentak",
        "ket":
            "Decorator, context manager, introspeksi objek, konkurensi, "
            "dan asinkron.",
        "tingkat": "mahir",
        "awal": 37, "akhir": 41,
        },
        {
        "judul": "Siap Bekerja dengan Python",
        "ket":
            "Lingkungan terisolasi, pengujian menyeluruh, dan arah "
            "sesudah ini.",
        "tingkat": "mahir",
        "awal": 41, "akhir": 44,
        },
    ],
    "javascript": [
        {
        "judul": "Menjalankan Kode Pertama",
        "ket":
            "Menjalankan berkas JavaScript pertama, menyimpan nilai ke "
            "variabel, dan menghitung dengan operator.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Angka, Keputusan, dan Teks",
        "ket":
            "Mengubah tipe data dengan sengaja, memakai Math, mengambil "
            "keputusan, mengulang, lalu mengolah teks dan tanggal.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 8,
        },
        {
        "judul": "Menyimpan dan Mengolah Kumpulan Data",
        "ket":
            "Pola teks dengan regex, array, object, cara JavaScript "
            "menyimpan rujukan alih-alih salinan, serta Map dan Set.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 13,
        },
        {
        "judul": "Menguasai Fungsi dan Konteks",
        "ket":
            "Semua bentuk fungsi, closure, IIFE, rekursi, currying, "
            "generator, dan aturan nilai 'this'.",
        "tingkat": "menengah",
        "awal": 13, "akhir": 18,
        },
        {
        "judul": "Objek Buatan Sendiri dan Penanganan Kesalahan",
        "ket":
            "Class beserta mekanisme prototype di baliknya, dan cara "
            "menangani error tanpa program berhenti.",
        "tingkat": "menengah",
        "awal": 18, "akhir": 21,
        },
        {
        "judul": "Asinkron dan Halaman Web yang Hidup",
        "ket":
            "Callback, promise, async/await, lalu membaca dan mengubah "
            "halaman: form, atribut, event, dan fetch.",
        "tingkat": "menengah",
        "awal": 21, "akhir": 27,
        },
        {
        "judul": "Keluar dari Browser dan Membaca Kode Orang Lain",
        "ket":
            "Module lengkap, Node.js untuk berkas dan terminal, isi "
            "repo sungguhan, dan arah setelah ini.",
        "tingkat": "mahir",
        "awal": 27, "akhir": 32,
        },
    ],
    "c": [
        {
        "judul": "Program C Pertama",
        "ket":
            "Memasang compiler, menjalankan program pertama, dan "
            "mengerti bagaimana angka benar-benar disimpan komputer.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Menghitung dan Mengatur Alur",
        "ket":
            "Operator, cara membaca ekspresi, masukan/keluaran, "
            "percabangan, dan perulangan.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 8,
        },
        {
        "judul": "Data Berkelompok dan Fungsi",
        "ket":
            "Array, string, pustaka standar yang sering dipakai, "
            "memecah program jadi fungsi, dan rekursi.",
        "tingkat": "dasar",
        "awal": 8, "akhir": 13,
        },
        {
        "judul": "Memori dan Pointer",
        "ket":
            "Lingkup variabel, pointer, teks sebagai pointer, dan "
            "memesan memori sendiri saat program berjalan.",
        "tingkat": "menengah",
        "awal": 13, "akhir": 18,
        },
        {
        "judul": "Tipe Data Buatan Sendiri",
        "ket": "Struct, cara struct ditata di memori, union, dan enum.",
        "tingkat": "menengah",
        "awal": 18, "akhir": 21,
        },
        {
        "judul": "Berkas dan Dunia Luar",
        "ket":
            "Membaca dan menulis berkas teks maupun biner, menerima "
            "argumen baris perintah, dan melaporkan kegagalan seperti "
            "kode C sungguhan.",
        "tingkat": "menengah",
        "awal": 21, "akhir": 25,
        },
        {
        "judul": "Makro dan Fungsi Tingkat Lanjut",
        "ket":
            "Preprocessor yang sesungguhnya, function pointer, dan cara "
            "C menulis kode yang bekerja untuk tipe apa saja.",
        "tingkat": "mahir",
        "awal": 25, "akhir": 29,
        },
        {
        "judul": "Proyek C Sungguhan",
        "ket":
            "Linked list, proyek multi-berkas, build system, debugging, "
            "dan arah sesudah kurikulum ini.",
        "tingkat": "mahir",
        "awal": 29, "akhir": 34,
        },
    ],
    "cpp": [
        {
        "judul": "Dari C ke C++",
        "ket":
            "Bedanya C++ dari C, tipe data, membuat namespace sendiri, "
            "dan memberi nama pada nilai.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Masukan, Teks, dan Fungsi",
        "ket":
            "Membaca masukan, mengolah string, memakai referensi, dan "
            "meng-overload fungsi.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 8,
        },
        {
        "judul": "Membangun Class",
        "ket":
            "Class, constructor, hak akses, memecahnya ke .h/.cpp, dan "
            "anatomi class di kode nyata.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 13,
        },
        {
        "judul": "Hierarki dan Perilaku Objek",
        "ket":
            "Pewarisan, virtual function, cast yang aman, operator, dan "
            "aturan menyalin objek.",
        "tingkat": "menengah",
        "awal": 13, "akhir": 19,
        },
        {
        "judul": "Template dan STL",
        "ket":
            "Generic programming, container standar, iterator, dan "
            "pustaka algorithm.",
        "tingkat": "menengah",
        "awal": 19, "akhir": 25,
        },
        {
        "judul": "C++ Modern",
        "ket":
            "Smart pointer, exception, berkas, lambda, dan "
            "memperlakukan fungsi sebagai nilai.",
        "tingkat": "mahir",
        "awal": 25, "akhir": 30,
        },
        {
        "judul": "C++ Sungguhan",
        "ket":
            "RAII, move semantics, thread, dan kebiasaan yang dipakai "
            "di proyek beneran.",
        "tingkat": "mahir",
        "awal": 30, "akhir": 33,
        },
    ],
    "bash": [
        {
        "judul": "Langkah Pertama di Terminal",
        "ket":
            "Menjalankan script pertama, membaca izin berkas, dan "
            "menyimpan nilai ke variabel.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Aliran Data dan Lingkungan Shell",
        "ket":
            "Mengarahkan keluaran, memahami proses dan source, lalu "
            "menata shell yang dipakai sehari-hari.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 7,
        },
        {
        "judul": "Logika dan Struktur Program",
        "ket":
            "Berhitung, bercabang, mengulang, menyimpan banyak nilai, "
            "dan memecah script jadi fungsi.",
        "tingkat": "dasar",
        "awal": 7, "akhir": 12,
        },
        {
        "judul": "Dari Script Jadi Alat",
        "ket":
            "Menerima argumen dan opsi, mencocokkan pola, mengolah "
            "teks, dan menyentuh berkas.",
        "tingkat": "menengah",
        "awal": 12, "akhir": 17,
        },
        {
        "judul": "Mengolah Berkas dan Proses",
        "ket":
            "Memproses banyak berkas sekaligus, mengendalikan proses "
            "yang berjalan, dan merekatkan alat luar.",
        "tingkat": "menengah",
        "awal": 17, "akhir": 21,
        },
        {
        "judul": "Script Layak Produksi",
        "ket":
            "Men-debug, menulis yang portabel antar shell, memakai "
            "fitur lanjutan, dan merakit satu alat utuh.",
        "tingkat": "mahir",
        "awal": 21, "akhir": 25,
        },
    ],
    "go": [
        {
        "judul": "Langkah Pertama di Go",
        "ket":
            "Memasang Go, menjalankan program pertama, menyimpan nilai, "
            "dan menghitung.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Menghitung, Bertanya, dan Mengulang",
        "ket":
            "Memakai package angka dan waktu, menerima masukan, lalu "
            "mengatur alur program dengan percabangan dan perulangan.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 7,
        },
        {
        "judul": "Mengolah Kumpulan Data",
        "ket":
            "Tiga wadah yang dipakai setiap hari di Go: slice, teks, "
            "dan map.",
        "tingkat": "dasar",
        "awal": 7, "akhir": 10,
        },
        {
        "judul": "Fungsi, Pointer & Tipe Buatan Sendiri",
        "ket":
            "Memecah program jadi fungsi, mengubah data lewat pointer, "
            "lalu merancang tipe dan perilaku sendiri dengan struct, "
            "interface, dan iota.",
        "tingkat": "menengah",
        "awal": 10, "akhir": 15,
        },
        {
        "judul": "Program yang Menyentuh Dunia Luar",
        "ket":
            "Menangani kegagalan, membaca dan menulis berkas, menerima "
            "argumen dari terminal, dan bertukar data lewat JSON.",
        "tingkat": "menengah",
        "awal": 15, "akhir": 19,
        },
        {
        "judul": "Menjalankan Banyak Hal Sekaligus",
        "ket":
            "Goroutine, channel, pola worker, dan cara membatalkan "
            "pekerjaan yang sudah tidak diperlukan.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 22,
        },
        {
        "judul": "Go Seperti di Repo Sungguhan",
        "ket":
            "Generics, isi go.mod dan blok import, server HTTP, "
            "pengujian lanjutan, dan satu studi kasus utuh.",
        "tingkat": "mahir",
        "awal": 22, "akhir": 28,
        },
    ],
    "aplikasi": [
        {
        "judul": "Membaca Bentuk Aplikasi",
        "ket":
            "Mengenali bedanya skrip dan aplikasi, lapisan- lapisannya, "
            "dan cara menurunkan model data dari kalimat kebutuhan.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Dari Benda ke Kelas dan Tabel",
        "ket":
            "Menulis entitas beserta tipe pendukungnya, lalu menutup "
            "seluruh akses database di balik satu pintu.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 6,
        },
        {
        "judul": "Menyambung Lapisan Jadi Aplikasi",
        "ket":
            "Memetakan hubungan antar entitas, memahami siapa yang "
            "membuat dan mengisi objek, dan menaruh aturan bisnis di "
            "service.",
        "tingkat": "menengah",
        "awal": 6, "akhir": 9,
        },
        {
        "judul": "Menangani Permintaan dan Kesalahan",
        "ket":
            "Mengikat permintaan HTTP jadi objek Java, memvalidasi "
            "masukannya, membalas dengan kode status yang benar, dan "
            "meninggalkan jejak yang bisa dibaca.",
        "tingkat": "menengah",
        "awal": 9, "akhir": 14,
        },
        {
        "judul": "Menyajikan Jawaban dan Merakit Proyek",
        "ket":
            "Membuat halaman dan balasan JSON, lalu memahami bagaimana "
            "proyeknya dirakit, dijalankan, dan berubah bentuk di "
            "Spring Boot.",
        "tingkat": "menengah",
        "awal": 14, "akhir": 19,
        },
        {
        "judul": "Menjaga Pengguna dan Data Sungguhan",
        "ket":
            "Mengenali siapa yang sedang login, memisahkan hak akses, "
            "dan memperlakukan database serta rahasia produksi dengan "
            "hati-hati.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 23,
        },
        {
        "judul": "Melepas Aplikasi ke Dunia Nyata",
        "ket":
            "Menangani pengguna yang datang bersamaan, mengemas "
            "aplikasi, deploy dengan jalan mundur yang siap, dan "
            "membuktikan semuanya lewat pengujian.",
        "tingkat": "mahir",
        "awal": 23, "akhir": 28,
        },
    ],
}
