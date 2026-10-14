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
            "Menulis berkas HTML pertama, menutup tag dengan benar, membaca "
            "pohonnya, dan menandai teks.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Isi Halaman dan Cara Menyajikannya",
        "ket":
            "Menandai kutipan dan waktu, menyusun daftar, menautkan halaman "
            "dan gambar, lalu menjalankannya lewat server lokal.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 8,
        },
        {
        "judul": "Atribut, Gaya, dan Makna",
        "ket":
            "Memberi keterangan pada elemen, menempelkan CSS dan "
            "JavaScript, dan memilih elemen yang menyebut perannya sendiri.",
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
            "Metadata, merakit semuanya jadi satu halaman, canvas, dan "
            "membaca berkas .html buatan orang lain.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 23,
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
            "Menentukan warna, memilih satuan yang benar, menghitung ukuran "
            "di dalam CSS, dan menata teks.",
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
            "Bayangan, filter, transform, dan cara memotong teks yang lebih "
            "panjang dari kotaknya.",
        "tingkat": "menengah",
        "awal": 9, "akhir": 12,
        },
        {
        "judul": "Tata Letak",
        "ket":
            "Menyusun halaman dengan flexbox dan grid, sampai float yang "
            "masih memenuhi kode lama.",
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
            "Menata tabel dan formulir, menyesuaikan diri ke lebar layar "
            "apa pun, dan menyatukan semuanya lewat variabel.",
        "tingkat": "menengah",
        "awal": 19, "akhir": 23,
        },
        {
        "judul": "CSS Zaman Sekarang",
        "ket":
            "Pemilih dan at-rule baru, properti logis, container query, "
            "nesting, dan cara membaca CSS di repo orang lain.",
        "tingkat": "mahir",
        "awal": 23, "akhir": 27,
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
            "Membuat class beserta constructor, anggota static, enum, dan "
            "data yang terlindungi.",
        "tingkat": "dasar",
        "awal": 10, "akhir": 14,
        },
        {
        "judul": "Pewarisan, Interface, dan Java Modern",
        "ket":
            "Menurunkan class, menyeragamkan perilaku lewat interface, dan "
            "membaca sintaks Java terbaru.",
        "tingkat": "menengah",
        "awal": 14, "akhir": 20,
        },
        {
        "judul": "Menangani Error dan Mengolah Koleksi",
        "ket":
            "Menangkap error, membaca stack trace, memakai List/Map/Set, "
            "string, dan tanggal.",
        "tingkat": "menengah",
        "awal": 20, "akhir": 27,
        },
        {
        "judul": "Mengolah Data dengan Lambda & Stream",
        "ket":
            "Lambda, pengurutan objek, class bersarang, stream, generics, "
            "dan menghindari null.",
        "tingkat": "menengah",
        "awal": 27, "akhir": 33,
        },
        {
        "judul": "Berjalan Bersamaan dan Menyimpan Data",
        "ket":
            "Thread, tugas asinkron, berkas, dan database.",
        "tingkat": "mahir",
        "awal": 33, "akhir": 37,
        },
        {
        "judul": "Bekerja Seperti Developer Profesional",
        "ket":
            "Unit test, design pattern, Git dan build tool, serta arah "
            "belajar sesudah ini.",
        "tingkat": "mahir",
        "awal": 37, "akhir": 41,
        },
    ],
    "sql": [
        {
        "judul": "Tabel Pertama",
        "ket":
            "Membuat tabel, memilih tipe kolom yang tepat, dan melihat isi "
            "database yang sudah ada sebelum menyentuh apa pun.",
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
            "Index, normalisasi, query berparameter, hak akses, dan membaca "
            "rencana eksekusi.",
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
            "Menulis blok prosedural di database, menjaga konsistensi data, "
            "dan arah belajar sesudahnya.",
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
            "Teks, list, tuple, dictionary, set, dan wadah siap pakai dari "
            "pustaka standar.",
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
            "Unpacking, anotasi tipe, lambda, closure, dan comprehension.",
        "tingkat": "menengah",
        "awal": 15, "akhir": 20,
        },
        {
        "judul": "Pemrograman Berorientasi Objek",
        "ket":
            "Class, pewarisan, kontrak abstrak, dunder method, dataclass, "
            "dan Enum.",
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
            "Encoding, bytes, regular expression, iterator, generator, dan "
            "itertools.",
        "tingkat": "menengah",
        "awal": 33, "akhir": 37,
        },
        {
        "judul": "Membentuk Perilaku dan Menjalankan Serentak",
        "ket":
            "Decorator, context manager, introspeksi objek, konkurensi, dan "
            "asinkron.",
        "tingkat": "mahir",
        "awal": 37, "akhir": 41,
        },
        {
        "judul": "Siap Bekerja dengan Python",
        "ket":
            "Lingkungan terisolasi, pengujian menyeluruh, dan arah sesudah "
            "ini.",
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
        "judul": "Keluar dari Browser dan Bekerja dengan Node.js",
        "ket":
            "Module lengkap, dan Node.js untuk berkas dan terminal.",
        "tingkat": "mahir",
        "awal": 27, "akhir": 30,
        },
        {
        "judul": "Web API Browser Lanjutan",
        "ket":
            "Observer (Intersection/Mutation/Resize), animasi lewat "
            "requestAnimationFrame, Geolocation, Clipboard, dan menggambar "
            "dengan Canvas API.",
        "tingkat": "mahir",
        "awal": 30, "akhir": 33,
        },
        {
        "judul": "Membaca Kode Orang Lain dan Roadmap",
        "ket":
            "Isi repo JavaScript sungguhan, dan arah belajar setelah ini.",
        "tingkat": "mahir",
        "awal": 33, "akhir": 35,
        },
    ],
    "c": [
        {
        "judul": "Program C Pertama",
        "ket":
            "Memasang compiler, menjalankan program pertama, dan mengerti "
            "bagaimana angka benar-benar disimpan komputer.",
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
            "Array, string, pustaka standar yang sering dipakai, memecah "
            "program jadi fungsi, dan rekursi.",
        "tingkat": "dasar",
        "awal": 8, "akhir": 13,
        },
        {
        "judul": "Memori dan Pointer",
        "ket":
            "Lingkup variabel, pointer, teks sebagai pointer, dan memesan "
            "memori sendiri saat program berjalan.",
        "tingkat": "menengah",
        "awal": 13, "akhir": 18,
        },
        {
        "judul": "Tipe Data Buatan Sendiri",
        "ket":
            "Struct, cara struct ditata di memori, union, dan enum.",
        "tingkat": "menengah",
        "awal": 18, "akhir": 21,
        },
        {
        "judul": "Berkas dan Dunia Luar",
        "ket":
            "Membaca dan menulis berkas teks maupun biner, menerima argumen "
            "baris perintah, dan melaporkan kegagalan seperti kode C "
            "sungguhan.",
        "tingkat": "menengah",
        "awal": 21, "akhir": 25,
        },
        {
        "judul": "Makro dan Fungsi Tingkat Lanjut",
        "ket":
            "Preprocessor yang sesungguhnya, function pointer, dan cara C "
            "menulis kode yang bekerja untuk tipe apa saja.",
        "tingkat": "mahir",
        "awal": 25, "akhir": 29,
        },
        {
        "judul": "Proyek C Sungguhan",
        "ket":
            "Linked list, proyek multi-berkas, build system, debugging, dan "
            "arah sesudah kurikulum ini.",
        "tingkat": "mahir",
        "awal": 29, "akhir": 34,
        },
    ],
    "cpp": [
        {
        "judul": "Dari C ke C++",
        "ket":
            "Bedanya C++ dari C, tipe data, membuat namespace sendiri, dan "
            "memberi nama pada nilai.",
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
            "Generic programming, container standar, iterator, dan pustaka "
            "algorithm.",
        "tingkat": "menengah",
        "awal": 19, "akhir": 25,
        },
        {
        "judul": "C++ Modern",
        "ket":
            "Smart pointer, exception, berkas, lambda, dan memperlakukan "
            "fungsi sebagai nilai.",
        "tingkat": "mahir",
        "awal": 25, "akhir": 30,
        },
        {
        "judul": "C++ Sungguhan",
        "ket":
            "RAII, move semantics, thread, dan kebiasaan yang dipakai di "
            "proyek beneran.",
        "tingkat": "mahir",
        "awal": 30, "akhir": 33,
        },
    ],
    "bash": [
        {
        "judul": "Langkah Pertama di Terminal",
        "ket":
            "Menjalankan script pertama, membaca izin berkas, dan menyimpan "
            "nilai ke variabel.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Aliran Data dan Lingkungan Shell",
        "ket":
            "Mengarahkan keluaran, memahami proses dan source, lalu menata "
            "shell yang dipakai sehari-hari.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 7,
        },
        {
        "judul": "Logika dan Struktur Program",
        "ket":
            "Berhitung, bercabang, mengulang, menyimpan banyak nilai, dan "
            "memecah script jadi fungsi.",
        "tingkat": "dasar",
        "awal": 7, "akhir": 12,
        },
        {
        "judul": "Dari Script Jadi Alat",
        "ket":
            "Menerima argumen dan opsi, mencocokkan pola, mengolah teks, "
            "dan menyentuh berkas.",
        "tingkat": "menengah",
        "awal": 12, "akhir": 17,
        },
        {
        "judul": "Mengolah Berkas dan Proses",
        "ket":
            "Memproses banyak berkas sekaligus, mengendalikan proses yang "
            "berjalan, dan merekatkan alat luar.",
        "tingkat": "menengah",
        "awal": 17, "akhir": 21,
        },
        {
        "judul": "Script Layak Produksi",
        "ket":
            "Men-debug, menulis yang portabel antar shell, memakai fitur "
            "lanjutan, dan merakit satu alat utuh.",
        "tingkat": "mahir",
        "awal": 21, "akhir": 25,
        },
    ],
    "go": [
        {
        "judul": "Langkah Pertama di Go",
        "ket":
            "Memasang Go, menjalankan program pertama, menyimpan nilai, dan "
            "menghitung.",
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
            "Tiga wadah yang dipakai setiap hari di Go: slice, teks, dan "
            "map.",
        "tingkat": "dasar",
        "awal": 7, "akhir": 10,
        },
        {
        "judul": "Fungsi, Pointer & Tipe Buatan Sendiri",
        "ket":
            "Memecah program jadi fungsi, mengubah data lewat pointer, lalu "
            "merancang tipe dan perilaku sendiri dengan struct, interface, "
            "dan iota.",
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
            "Generics, isi go.mod dan blok import, server HTTP, pengujian "
            "lanjutan, dan satu studi kasus utuh.",
        "tingkat": "mahir",
        "awal": 22, "akhir": 28,
        },
    ],
    "csharp": [
        {
        "judul": "Langkah Pertama di C#",
        "ket":
            "Memasang .NET, menjalankan program pertama, menyimpan nilai, "
            "menghitung, lalu menyusun dan membaca teks.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Mengatur Alur Program",
        "ket":
            "Percabangan dengan if dan switch expression, pattern matching, "
            "lalu empat bentuk perulangan dan kapan memakai yang mana.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 6,
        },
        {
        "judul": "Kumpulan Data dan Method",
        "ket":
            "Array beserta indeks dari belakang, koleksi generik yang "
            "tumbuh, dan memecah program jadi method.",
        "tingkat": "dasar",
        "awal": 6, "akhir": 9,
        },
        {
        "judul": "Berpikir dengan Objek",
        "ket":
            "Null-safety, class dan property yang menjaga dirinya sendiri, "
            "pewarisan, interface, serta bedanya struct, class, dan record.",
        "tingkat": "menengah",
        "awal": 9, "akhir": 15,
        },
        {
        "judul": "Tipe Bernama, Kegagalan, dan Perilaku",
        "ket":
            "Enum dan flag, exception beserta cara menanganinya dengan "
            "jujur, generic, lalu delegate dan lambda.",
        "tingkat": "menengah",
        "awal": 15, "akhir": 19,
        },
        {
        "judul": "Bertanya pada Data dan Menyentuh Dunia Luar",
        "ket":
            "LINQ, berkas dan path, pelepasan sumber daya lewat using, dan "
            "async/await yang benar-benar berjalan bersamaan.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 23,
        },
        {
        "judul": "C# Seperti di Proyek Sungguhan",
        "ket":
            "Namespace dan struktur proyek, unit test dan debugging, "
            "konvensi serta analyzer, dan satu aplikasi konsol utuh.",
        "tingkat": "mahir",
        "awal": 23, "akhir": 27,
        },
    ],
    "rust": [
        {
        "judul": "Langkah Pertama di Rust",
        "ket":
            "Memasang Rust, menjalankan program pertama, menyimpan nilai, "
            "menulis fungsi, lalu mengatur alur program.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Aturan Inti: Ownership & Borrowing",
        "ket":
            "Tiga aturan yang membuat Rust berbeda dari semua bahasa lain, "
            "cara meminjam tanpa mengambil, dan dua tipe teks yang wajib "
            "dibedakan.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 7,
        },
        {
        "judul": "Merancang Tipe Sendiri",
        "ket":
            "Struct, enum berdata beserta Option, pencocokan pola yang "
            "diperiksa kelengkapannya, dan dua wadah yang dipakai setiap "
            "hari.",
        "tingkat": "menengah",
        "awal": 7, "akhir": 11,
        },
        {
        "judul": "Kegagalan yang Jujur dan Kode yang Dipakai Ulang",
        "ket":
            "Result dan operator tanya, generic tanpa ongkos, trait sebagai "
            "kontrak, dan lifetime yang biasanya tidak perlu ditulis.",
        "tingkat": "menengah",
        "awal": 11, "akhir": 15,
        },
        {
        "judul": "Closure, Iterator & Struktur Proyek",
        "ket":
            "Rantai iterator yang secepat perulangan tangan, pembagian kode "
            "jadi modul dan crate, serta smart pointer.",
        "tingkat": "mahir",
        "awal": 15, "akhir": 18,
        },
        {
        "judul": "Konkurensi, Pengujian, dan Dunia Luar",
        "ket":
            "Fearless concurrency, tes yang menyatu dengan bahasanya, trait "
            "standar, membaca masukan dan berkas, lalu satu proyek utuh.",
        "tingkat": "mahir",
        "awal": 18, "akhir": 23,
        },
    ],
    "php": [
        {
        "judul": "Langkah Pertama di PHP",
        "ket":
            "Memasang PHP 8, menjalankan skrip pertama, menyimpan nilai, "
            "menyusun teks, lalu membandingkan dengan benar.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Alur Program dan Kumpulan Data",
        "ket":
            "Percabangan dengan match, perulangan, array yang merangkap "
            "daftar dan kamus, serta fungsi bertipe ketat.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 7,
        },
        {
        "judul": "Berorientasi Objek",
        "ket":
            "Class dan property yang menjaga dirinya, pewarisan beserta "
            "interface dan trait, enum sungguhan, dan exception.",
        "tingkat": "menengah",
        "awal": 7, "akhir": 11,
        },
        {
        "judul": "Menyentuh Dunia Luar",
        "ket":
            "Berkas dan JSON, permintaan web beserta formulir dan sesi, "
            "lalu database lewat PDO dan prepared statement.",
        "tingkat": "menengah",
        "awal": 11, "akhir": 14,
        },
        {
        "judul": "PHP Seperti di Proyek Sungguhan",
        "ket":
            "Composer dan autoload, praktik baik beserta keamanan, tanggal "
            "dan waktu, serta ekspresi reguler.",
        "tingkat": "mahir",
        "awal": 14, "akhir": 18,
        },
        {
        "judul": "Yang Membedakan PHP Modern",
        "ket":
            "Generator untuk data besar, anggota statis dan method ajaib, "
            "dan pengujian dengan PHPUnit.",
        "tingkat": "mahir",
        "awal": 18, "akhir": 21,
        },
    ],
    "ruby": [
        {
        "judul": "Langkah Pertama di Ruby",
        "ket":
            "Memasang Ruby, menjalankan program pertama, memahami bahwa "
            "semuanya objek, lalu mengolah teks dan dua wadah utamanya.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Alur Program dan Blok",
        "ket":
            "Percabangan yang jauh lebih kaya daripada switch, dan blok "
            "sebagai gagasan paling khas Ruby.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 6,
        },
        {
        "judul": "Enumerable dan Method",
        "ket":
            "Puluhan method yang didapat dari satu each, serta empat jenis "
            "argumen dan operator yang bisa kamu tulis sendiri.",
        "tingkat": "dasar",
        "awal": 6, "akhir": 8,
        },
        {
        "judul": "Objek, Mixin, dan Kegagalan",
        "ket":
            "Class beserta attr, module sebagai mixin, penanganan galat "
            "yang jujur, lalu berkas dan JSON.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 12,
        },
        {
        "judul": "Ruby Seperti di Proyek Sungguhan",
        "ket":
            "Gem dan Bundler, pengujian dengan Minitest dan RSpec, "
            "metaprogramming secukupnya, dan ekspresi reguler.",
        "tingkat": "menengah",
        "awal": 12, "akhir": 16,
        },
        {
        "judul": "Bahan yang Melengkapi",
        "ket":
            "Tanggal dan waktu, Set beserta Struct dan Data, Ruby sebagai "
            "pengganti skrip shell, jebakan yang paling sering, lalu satu "
            "proyek utuh.",
        "tingkat": "mahir",
        "awal": 16, "akhir": 21,
        },
    ],
    "kotlin": [
        {
        "judul": "Langkah Pertama di Kotlin",
        "ket":
            "Memasang Kotlin, menjalankan program pertama, memilih antara "
            "val dan var, memahami null safety, lalu menulis fungsi.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Alur Program dan Koleksi",
        "ket":
            "when yang jauh lebih kuat daripada switch, dan koleksi yang "
            "membedakan hanya-baca dari yang bisa diubah.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 6,
        },
        {
        "judul": "Merancang Tipe Sendiri",
        "ket":
            "Class beserta properti yang menjaga dirinya, data class dan "
            "sealed class, lalu pewarisan dan delegasi.",
        "tingkat": "menengah",
        "awal": 6, "akhir": 9,
        },
        {
        "judul": "Fungsi sebagai Nilai",
        "ket":
            "Lambda dan scope function, generic beserta variansi, serta "
            "penanganan galat tanpa checked exception.",
        "tingkat": "menengah",
        "awal": 9, "akhir": 12,
        },
        {
        "judul": "Konkurensi dan Dunia Luar",
        "ket":
            "Coroutine dan structured concurrency, pengolahan teks dengan "
            "regex, lalu berkas dan baris perintah.",
        "tingkat": "mahir",
        "awal": 12, "akhir": 15,
        },
        {
        "judul": "Kotlin Seperti di Proyek Sungguhan",
        "ket":
            "Struktur proyek dan Gradle, pengujian, dan satu aplikasi utuh "
            "yang memisahkan model, layanan, dan antarmuka.",
        "tingkat": "mahir",
        "awal": 15, "akhir": 18,
        },
    ],
    "typescript": [
        {
        "judul": "Langkah Pertama di TypeScript",
        "ket":
            "Memasang compiler, memahami bahwa tipe hilang saat program "
            "jalan, mengenal tipe dasar, lalu union dan penyempitan.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Menamai Bentuk dan Menulis Fungsi",
        "ket":
            "Interface dan type alias beserta jebakannya, lalu semua bentuk "
            "fungsi termasuk tipe fungsi itu sendiri.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 5,
        },
        {
        "judul": "Generic, Class, dan Modul",
        "ket":
            "Generic beserta keyof dan utility type, class dengan modifier "
            "akses, serta sistem modul dan tsconfig.",
        "tingkat": "menengah",
        "awal": 5, "akhir": 8,
        },
        {
        "judul": "Asinkron dan Tipe yang Lebih Dalam",
        "ket":
            "Promise dan async/await, tipe kondisional dan mapped type, "
            "lalu enum beserta as const dan readonly.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 11,
        },
        {
        "judul": "Menghadapi Data dari Luar",
        "ket":
            "Validasi di batas sistem, pengujian, dan pengolahan koleksi "
            "dengan method yang tidak merusak data aslinya.",
        "tingkat": "mahir",
        "awal": 11, "akhir": 14,
        },
        {
        "judul": "TypeScript Seperti di Proyek Sungguhan",
        "ket":
            "Node dan browser beserta paket tipenya, lalu satu aplikasi "
            "utuh yang memisahkan model, layanan, dan antarmuka.",
        "tingkat": "mahir",
        "awal": 14, "akhir": 16,
        },
    ],
    "vb": [
        {
        "judul": "Langkah Pertama di Visual Basic",
        "ket":
            "Membedakan VB.NET dari VB6 dan VBA, menyalakan Option Strict, "
            "mengenal tipe data, lalu operator yang khas VB.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 3,
        },
        {
        "judul": "Mengatur Alur Program",
        "ket":
            "Percabangan dengan If dan Select Case yang menerima rentang, "
            "serta empat bentuk perulangan dengan batas yang inklusif.",
        "tingkat": "dasar",
        "awal": 3, "akhir": 5,
        },
        {
        "judul": "Data dan Prosedur",
        "ket":
            "Array beserta jebakan batas atasnya, koleksi generik, prosedur "
            "dengan ByVal dan ByRef, lalu pengolahan teks.",
        "tingkat": "dasar",
        "awal": 5, "akhir": 8,
        },
        {
        "judul": "Berpikir dengan Objek",
        "ket":
            "Class beserta property yang menjaga dirinya, pewarisan dan "
            "interface, serta Structure, Enum, dan Module.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 11,
        },
        {
        "judul": "Kegagalan dan Data",
        "ket":
            "Exception beserta klausa When, LINQ dengan sintaks query, lalu "
            "berkas dan blok Using.",
        "tingkat": "menengah",
        "awal": 11, "akhir": 14,
        },
        {
        "judul": "Visual Basic Seperti di Proyek Sungguhan",
        "ket":
            "Praktik baik beserta jebakan yang paling sering, dan satu "
            "aplikasi utuh yang memisahkan model, layanan, dan antarmuka.",
        "tingkat": "mahir",
        "awal": 14, "akhir": 16,
        },
    ],
    "aplikasi": [
        {
        "judul": "Membaca Bentuk Aplikasi",
        "ket":
            "Mengenali bedanya skrip dan aplikasi, lapisan- lapisannya, dan "
            "cara menurunkan model data dari kalimat kebutuhan.",
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
            "Memetakan hubungan antar entitas, memahami siapa yang membuat "
            "dan mengisi objek, dan menaruh aturan bisnis di service.",
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
            "proyeknya dirakit, dijalankan, dan berubah bentuk di Spring "
            "Boot.",
        "tingkat": "menengah",
        "awal": 14, "akhir": 19,
        },
        {
        "judul": "Menjaga Pengguna dan Data Sungguhan",
        "ket":
            "Mengenali siapa yang sedang login, memisahkan hak akses, dan "
            "memperlakukan database serta rahasia produksi dengan "
            "hati-hati.",
        "tingkat": "mahir",
        "awal": 19, "akhir": 23,
        },
        {
        "judul": "Melepas Aplikasi ke Dunia Nyata",
        "ket":
            "Menangani pengguna yang datang bersamaan, mengemas aplikasi, "
            "deploy dengan jalan mundur yang siap, dan membuktikan semuanya "
            "lewat pengujian.",
        "tingkat": "mahir",
        "awal": 23, "akhir": 28,
        },
    ],
    "fedora": [
        {
        "judul": "Menjejak di Terminal Fedora",
        "ket":
            "Mengenali sistem sendiri, membaca prompt, menjelajah pohon "
            "direktori, lalu membuat dan memindahkan berkas tanpa menyesal.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Membaca Berkas dan Menemukannya Kembali",
        "ket":
            "Memilih alat sesuai ukuran berkas, lalu mencari berdasarkan "
            "sifat berkas maupun isinya dengan find dan grep.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 6,
        },
        {
        "judul": "Izin, Pengguna, dan Hak Akses",
        "ket":
            "Model rwx dan artinya yang berbeda pada direktori, ACL untuk "
            "kasus yang rwx tidak sanggup, serta sudo dan polkit.",
        "tingkat": "dasar",
        "awal": 6, "akhir": 9,
        },
        {
        "judul": "Mengolah Teks seperti Administrator",
        "ket":
            "Menyambung perintah dengan pipa, memotong kolom, menghitung "
            "frekuensi, lalu menyunting aliran teks dengan sed dan awk.",
        "tingkat": "menengah",
        "awal": 9, "akhir": 12,
        },
        {
        "judul": "Perangkat Lunak: DNF5, RPM, dan Flatpak",
        "ket":
            "Memasang, menyelidiki, dan membatalkan transaksi paket, "
            "memahami repositori pihak ketiga, serta aplikasi terkurung "
            "Flatpak.",
        "tingkat": "menengah",
        "awal": 12, "akhir": 15,
        },
        {
        "judul": "systemd: Layanan, Log, dan Jadwal",
        "ket":
            "Menulis unit sendiri, membaca jurnal secara presisi, "
            "menjadwalkan dengan timer, dan mengendalikan proses serta "
            "sumber dayanya.",
        "tingkat": "menengah",
        "awal": 15, "akhir": 19,
        },
        {
        "judul": "Jaringan dan Pertahanan Fedora",
        "ket":
            "Mengatur koneksi dengan nmcli, mendiagnosis berlapis dari "
            "kabel sampai DNS, lalu firewalld berbasis zona dan SELinux.",
        "tingkat": "menengah",
        "awal": 19, "akhir": 23,
        },
        {
        "judul": "Penyimpanan, Btrfs, dan Cadangan",
        "ket":
            "Memahami mount dan fstab, memanfaatkan snapshot Btrfs, "
            "mengelola LVM dan enkripsi, serta menyalin dengan rsync.",
        "tingkat": "mahir",
        "awal": 23, "akhir": 27,
        },
        {
        "judul": "Jarak Jauh, Container, dan Atomic",
        "ket":
            "Bekerja aman lewat SSH, menjalankan container rootless dengan "
            "Podman, dan mengenal sistem yang diperbarui sebagai citra "
            "utuh.",
        "tingkat": "mahir",
        "awal": 27, "akhir": 30,
        },
        {
        "judul": "Pemulihan, Keamanan, dan Otomasi",
        "ket":
            "Menyelamatkan sistem yang gagal boot, merawat dan mengaudit "
            "keamanannya, lalu menyatukan semuanya jadi skrip yang tahan "
            "banting.",
        "tingkat": "mahir",
        "awal": 30, "akhir": 33,
        },
    ],
    "git": [
        {
        "judul": "Mulai Melacak: Commit Pertama",
        "ket":
            "Masalah yang diselesaikan Git, memasangnya, tiga area kerja, "
            "lalu membaca status, diff, dan riwayat tanpa takut.",
        "tingkat": "dasar",
        "awal": 0, "akhir": 4,
        },
        {
        "judul": "Mengendalikan Apa yang Masuk Riwayat",
        "ket":
            ".gitignore, memindah dan menghapus berkas terlacak, pesan commit "
            "yang terbaca setahun kemudian, dan membatalkan dengan aman.",
        "tingkat": "dasar",
        "awal": 4, "akhir": 8,
        },
        {
        "judul": "Bercabang dan Menyatu",
        "ket":
            "Branch sebagai penunjuk murah, berpindah di antaranya, merge "
            "fast-forward dan merge commit, lalu konflik sebagai hal biasa.",
        "tingkat": "menengah",
        "awal": 8, "akhir": 12,
        },
        {
        "judul": "Jarak Jauh dan GitHub",
        "ket":
            "Remote, clone, fetch, pull, kunci SSH, repo pertama di GitHub, "
            "alur push harian, dan pull request sebagai cara kerja tim.",
        "tingkat": "menengah",
        "awal": 12, "akhir": 16,
        },
        {
        "judul": "Menulis Ulang dan Menyelamatkan Riwayat",
        "ket":
            "reset tiga tingkat, rebase dan rebase -i, stash, cherry-pick, "
            "tag, lalu reflog dan bisect sebagai jaring pengaman dan detektif.",
        "tingkat": "mahir",
        "awal": 16, "akhir": 20,
        },
        {
        "judul": "Bekerja sebagai Tim",
        "ket":
            "Model cabang, perlindungan main, .gitattributes, hooks, CI, dan "
            "cara membaca repositori sungguhan sebelum berkontribusi.",
        "tingkat": "mahir",
        "awal": 20, "akhir": 22,
        },
    ],
}
