SQL_QUIZZES = [
    {
        "title": "Kuis 1: Dasar SQL & DDL",
        "questions": [
            {
                "q": "SQL adalah singkatan dari?",
                "options": [
                    "Structured Query Language",
                    "Simple Query Language",
                    "Standard Question Language",
                    "Sequential Query Language",
                ],
                "answer": 0,
                "explanation": "SQL kepanjangan dari Structured Query Language, bahasa standar buat ngobrol dengan database relasional.",
            },
            {
                "q": "Perintah untuk membuat tabel baru?",
                "options": ["CREATE TABLE", "CREATE VIEW", "ALTER TABLE", "INSERT INTO"],
                "answer": 0,
                "explanation": ("CREATE TABLE bikin struktur tabel baru. CREATE VIEW bikin view "
                                "dari query, ALTER TABLE mengubah tabel yang sudah ada, "
                                "dan INSERT INTO mengisi baris."),
            },
            {
                "q": "Constraint yang memastikan nilai unik dan tidak kosong?",
                "options": ["UNIQUE", "PRIMARY KEY", "CHECK", "NOT NULL"],
                "answer": 1,
                "explanation": ("PRIMARY KEY itu unik sekaligus nggak boleh kosong. UNIQUE cuma "
                                "menjamin unik, NOT NULL cuma menjamin terisi, dan CHECK "
                                "menguji syarat yang kamu tulis sendiri, misalnya harga > 0. "
                                "Catatan: SQLite, yang dipakai aplikasi ini untuk menjalankan "
                                "latihan, punya keanehan lama: PRIMARY KEY yang bukan INTEGER "
                                "masih menerima NULL. Tulis NOT NULL juga kalau mau aman."),
            },
            {
                "q": "Tipe data yang tepat untuk teks pendek (misal nama)?",
                "options": ["CHAR(1)", "VARCHAR(50)", "INT", "DECIMAL(5,2)"],
                "answer": 1,
                "explanation": ("VARCHAR(n) menyimpan teks sampai n karakter. CHAR(1) cuma muat satu "
                                "huruf, sedangkan INT dan DECIMAL untuk angka."),
            },
            {
                "q": "Perintah mana yang MENGHAPUS TABELNYA sekalian, bukan cuma isinya?",
                "options": ["DELETE FROM", "TRUNCATE TABLE", "DROP TABLE", "DROP COLUMN"],
                "answer": 2,
                "explanation": ("DROP TABLE membuang tabel beserta strukturnya. DELETE FROM "
                                "dan TRUNCATE TABLE sama-sama mengosongkan isi, tapi tabelnya "
                                "tetap ada (TRUNCATE lebih cepat karena nggak mencatat tiap "
                                "baris). DROP COLUMN, lewat ALTER TABLE, cuma membuang satu kolom."),
            },
            {
                "q": "Menambahkan kolom baru ke tabel menggunakan perintah?",
                "options": [
                    "INSERT INTO ... COLUMN ...",
                    "ALTER TABLE ... ADD ...",
                    "UPDATE ... SET ...",
                    "CREATE TABLE ... ADD ...",
                ],
                "answer": 1,
                "explanation": ("Bentuknya ALTER TABLE nama ADD kolom tipe;. INSERT dan UPDATE "
                                "mengurus isi baris, bukan struktur, dan CREATE TABLE cuma untuk "
                                "tabel yang belum ada."),
            },
            {
                "q": "Bagaimana mengganti nama tabel pelanggan jadi klien tanpa kehilangan isinya?",
                "options": ["UPDATE TABLE pelanggan SET nama = 'klien'",
                            "ALTER COLUMN pelanggan TO klien",
                            "ALTER TABLE pelanggan RENAME TO klien",
                            "CREATE TABLE klien AS pelanggan"],
                "answer": 2,
                "explanation": ("Mengganti nama tabel itu urusan struktur, jadi pintunya ALTER TABLE. "
                                "UPDATE cuma mengubah isi baris, dan CREATE TABLE ... AS butuh SELECT "
                                "serta membuat tabel kedua, bukan mengganti nama yang pertama."),
            },
            {
                "q": "Setiap statement SQL harus diakhiri dengan?",
                "options": ["titik koma (;)", "titik dua (:)", "koma (,)", "pagar (#)"],
                "answer": 0,
                "explanation": ("Titik koma menandai akhir statement. Koma dipakai untuk memisahkan "
                                "kolom, dan # di MySQL justru membuka komentar."),
            },
        ],
    },
    {
        "title": "Kuis 2: DML (INSERT, UPDATE, DELETE)",
        "questions": [
            {
                "q": "Perintah untuk menambahkan data baru ke tabel?",
                "options": ["UPDATE ... SET", "INSERT INTO", "ALTER TABLE", "ADD ROW"],
                "answer": 1,
                "explanation": ("Bentuknya INSERT INTO tabel (kolom) VALUES (nilai);. UPDATE mengubah "
                                "baris yang sudah ada, ALTER TABLE mengubah struktur."),
            },
            {
                "q": "INSERT INTO mahasiswa VALUES ('101', 'Andi'); Nilai teks harus diapit?",
                "options": ["backtick ``", "tanda kutip ''", "kurung siku []", "tanpa tanda apa pun"],
                "answer": 1,
                "explanation": ("Teks dan tanggal pakai tanda kutip tunggal. Backtick (MySQL) dan "
                                "kurung siku (SQL Server) dipakai untuk nama tabel atau kolom, "
                                "bukan untuk nilai."),
            },
            {
                "q": "Perintah yang benar untuk mengubah data?",
                "options": [
                    "UPDATE mahasiswa SET ipk = 3.5 WHERE nim = 101",
                    "UPDATE mahasiswa WHERE nim = 101 SET ipk = 3.5",
                    "MODIFY mahasiswa SET ipk = 3.5 WHERE nim = 101",
                    "UPDATE mahasiswa ipk = 3.5 WHERE nim = 101",
                ],
                "answer": 0,
                "explanation": ("Urutannya UPDATE tabel SET kolom = nilai WHERE kondisi;. SET wajib "
                                "ada dan datang sebelum WHERE. MODIFY bukan perintah untuk mengubah isi."),
            },
            {
                "q": "Apa yang terjadi jika UPDATE tanpa WHERE?",
                "options": [
                    "Muncul error karena WHERE wajib",
                    "Cuma baris pertama yang berubah",
                    "Semua baris di tabel berubah",
                    "Nggak ada baris yang berubah",
                ],
                "answer": 2,
                "explanation": ("Tanpa WHERE, semua baris kena dan database nggak protes sama sekali. "
                                "Kebiasaan yang aman: waktu mengetik, tulis UPDATE tabel WHERE kondisi "
                                "dulu, baru sisipkan SET di tengahnya. Ini cuma soal urutan mengetik; "
                                "perintah yang dijalankan tetap berurutan UPDATE, SET, lalu WHERE."),
            },
            {
                "q": "DELETE FROM mahasiswa WHERE nim = 101; Maksudnya?",
                "options": [
                    "Kosongkan nilai nim di baris 101",
                    "Hapus baris yang nim-nya 101",
                    "Hapus kolom nim dari tabel",
                    "Hapus semua baris kecuali nim 101",
                ],
                "answer": 1,
                "explanation": ("DELETE selalu membuang baris utuh, dan WHERE membatasi baris mana "
                                "yang kena. Mengosongkan satu nilai itu kerjanya UPDATE."),
            },
            {
                "q": "Perintah untuk membatalkan semua perubahan dalam transaction?",
                "options": ["COMMIT", "ROLLBACK", "REVOKE", "DELETE"],
                "answer": 1,
                "explanation": ("ROLLBACK mengembalikan data ke kondisi sebelum transaction dimulai. "
                                "COMMIT justru menyimpannya, REVOKE mencabut hak akses, dan "
                                "DELETE malah menambah perubahan baru."),
            },
            {
                "q": "Untuk menyimpan perubahan transaction secara permanen?",
                "options": ["SAVEPOINT", "COMMIT", "ROLLBACK", "BEGIN"],
                "answer": 1,
                "explanation": ("COMMIT menyimpan perubahan secara permanen. BEGIN membuka transaction, "
                                "SAVEPOINT menandai titik di dalamnya, ROLLBACK membatalkannya."),
            },
            {
                "q": "INSERT yang benar untuk beberapa baris sekaligus?",
                "options": [
                    "INSERT INTO t VALUES (1), (2), (3);",
                    "INSERT INTO t VALUES (1, 2, 3);",
                    "INSERT INTO t VALUES (1); (2); (3);",
                    "INSERT INTO t VALUES (1) AND (2) AND (3);",
                ],
                "answer": 0,
                "explanation": ("Tiap baris ditulis dalam kurungnya sendiri, dipisah koma. (1, 2, 3) "
                                "itu satu baris berisi tiga kolom, bukan tiga baris."),
            },
        ],
    },
    {
        "title": "Kuis 3: SELECT & Filtering",
        "questions": [
            {
                "q": "Perintah untuk menampilkan SEMUA kolom dari tabel?",
                "options": ["SELECT ALL FROM t;", "SELECT * FROM t;", "SHOW COLUMNS FROM t;", "DESCRIBE t;"],
                "answer": 1,
                "explanation": ("SELECT * FROM tabel menampilkan semua kolom beserta isinya. SHOW "
                                "COLUMNS dan DESCRIBE di MySQL cuma menampilkan struktur kolomnya, "
                                "bukan datanya."),
            },
            {
                "q": "Untuk menampilkan data unik dari kolom jurusan?",
                "options": [
                    "SELECT DISTINCT jurusan FROM mahasiswa;",
                    "SELECT jurusan FROM mahasiswa UNIQUE;",
                    "SELECT DIFFERENT jurusan FROM mahasiswa;",
                    "SELECT ALL jurusan FROM mahasiswa;",
                ],
                "answer": 0,
                "explanation": ("DISTINCT membuang nilai yang dobel. SELECT ALL justru kebalikannya: "
                                "semua baris tetap muncul, termasuk yang dobel."),
            },
            {
                "q": "SELECT nama AS 'Nama Lengkap' FROM mahasiswa; Fungsi AS adalah?",
                "options": ["menyaring", "memberi alias", "mengurutkan", "menghitung"],
                "answer": 1,
                "explanation": "AS memberi nama sementara (alias) pada kolom hasil. Isi kolomnya nggak berubah.",
            },
            {
                "q": "Filter yang benar untuk IPK lebih besar dari 3.5?",
                "options": [
                    "WHERE ipk > 3.5",
                    "WHERE ipk lebih dari 3.5",
                    "WHERE ipk >= 3.5",
                    "FILTER ipk > 3.5",
                ],
                "answer": 0,
                "explanation": "Operator > berarti lebih besar. >= ikut memasukkan 3.5 sendiri, jadi bukan \"lebih besar dari\".",
            },
            {
                "q": "LIKE 'A%' akan mencocokkan teks yang?",
                "options": [
                    "mengandung huruf A",
                    "diawali huruf A",
                    "diakhiri huruf A",
                    "tepat berhuruf A",
                ],
                "answer": 1,
                "explanation": "% artinya \"apa pun, berapa pun panjangnya\". Karena letaknya di belakang A, teksnya harus diawali A.",
            },
            {
                "q": "SELECT * FROM mahasiswa WHERE jurusan IN ('IF', 'SI'); artinya?",
                "options": [
                    "jurusan harus 'IF' dan 'SI' sekaligus",
                    "jurusan bernilai 'IF' atau 'SI'",
                    "jurusan selain 'IF' dan 'SI'",
                    "jurusan yang mengandung 'IF' atau 'SI'",
                ],
                "answer": 1,
                "explanation": ("IN sama dengan rangkaian OR: jurusan = 'IF' OR jurusan = 'SI'. "
                                "Cocoknya harus persis, bukan sekadar mengandung. Kebalikannya NOT IN."),
            },
            {
                "q": "Untuk mengurutkan hasil dari IPK tertinggi ke terendah?",
                "options": [
                    "ORDER BY ipk ASC",
                    "ORDER BY ipk DESC",
                    "SORT BY ipk DESC",
                    "ORDER ipk DOWN",
                ],
                "answer": 1,
                "explanation": "DESC artinya descending, dari besar ke kecil. ASC kebalikannya dan jadi bawaan kalau nggak ditulis.",
            },
            {
                "q": "IPK antara 3.0 dan 3.8 ditulis?",
                "options": [
                    "WHERE ipk BETWEEN 3.0 AND 3.8",
                    "WHERE ipk 3.0-3.8",
                    "WHERE ipk > 3.0 OR ipk < 3.8",
                    "WHERE ipk BETWEEN (3.0, 3.8)",
                ],
                "answer": 0,
                "explanation": ("BETWEEN ... AND ... mencakup kedua batas. Versi OR salah karena tiap "
                                "angka pasti lolos salah satu syaratnya, jadi semua baris ikut."),
            },
        ],
    },
    {
        "title": "Kuis 4: Agregasi & Grouping",
        "questions": [
            {
                "q": "Fungsi agregat untuk menghitung jumlah baris?",
                "options": ["TOTAL()", "SUM()", "COUNT()", "LENGTH()"],
                "answer": 2,
                "explanation": ("COUNT(*) menghitung banyaknya baris. SUM menjumlahkan nilai, dan "
                                "LENGTH mengukur panjang teks."),
            },
            {
                "q": "Fungsi untuk rata-rata nilai?",
                "options": ["MEAN()", "AVG()", "MEDIAN()", "SUM()"],
                "answer": 1,
                "explanation": "AVG() menghitung rata-rata. MEAN dan MEDIAN nggak ada di MySQL standar.",
            },
            {
                "q": "SELECT jurusan, COUNT(*) FROM mahasiswa GROUP BY jurusan; Tujuannya?",
                "options": [
                    "jumlah mahasiswa di tiap jurusan",
                    "jumlah jurusan di dalam tabel",
                    "mahasiswa diurutkan per jurusan",
                    "rata-rata nilai di tiap jurusan",
                ],
                "answer": 0,
                "explanation": ("GROUP BY jurusan bikin satu baris per jurusan, dan COUNT(*) menghitung "
                                "baris di dalam tiap kelompok itu. Mengurutkan itu kerjanya ORDER BY."),
            },
            {
                "q": "Filter hasil agregat menggunakan klausa?",
                "options": ["WHERE", "HAVING", "FILTER", "GROUP BY"],
                "answer": 1,
                "explanation": "HAVING menyaring hasil agregat, WHERE menyaring baris biasa sebelum dikelompokkan.",
            },
            {
                "q": "WHERE vs HAVING: yang benar adalah?",
                "options": [
                    "HAVING memfilter baris, WHERE memfilter agregat",
                    "WHERE memfilter baris, HAVING memfilter agregat",
                    "Keduanya sama, cuma beda nama",
                    "WHERE dipakai khusus untuk JOIN",
                ],
                "answer": 1,
                "explanation": "WHERE jalan sebelum pengelompokan, HAVING sesudahnya. Makanya COUNT(*) > 2 cuma bisa ditulis di HAVING.",
            },
            {
                "q": "Untuk menampilkan 5 data teratas, gunakan klausa?",
                "options": ["MAX 5", "LIMIT 5", "COUNT 5", "HAVING 5"],
                "answer": 1,
                "explanation": ("LIMIT 5 memotong hasil jadi lima baris (MySQL, PostgreSQL, SQLite). "
                                "Supaya yang diambil memang teratas, pasangkan dengan ORDER BY. MAX dan "
                                "COUNT itu fungsi agregat, bukan pembatas baris."),
            },
            {
                "q": "Urutan klausa SQL yang benar?",
                "options": [
                    "WHERE, GROUP BY, HAVING, ORDER BY",
                    "GROUP BY, WHERE, HAVING, ORDER BY",
                    "HAVING, WHERE, GROUP BY, ORDER BY",
                    "WHERE, HAVING, GROUP BY, ORDER BY",
                ],
                "answer": 0,
                "explanation": "Urutannya FROM, WHERE, GROUP BY, HAVING, lalu ORDER BY. HAVING butuh kelompok, jadi harus sesudah GROUP BY.",
            },
            {
                "q": "COUNT(kolom) vs COUNT(*): perbedaannya?",
                "options": [
                    "Sama saja",
                    "COUNT(kolom) mengabaikan NULL",
                    "COUNT(*) mengabaikan NULL",
                    "COUNT(kolom) lebih cepat",
                ],
                "answer": 1,
                "explanation": "COUNT(kolom) cuma menghitung nilai yang bukan NULL, sedangkan COUNT(*) menghitung semua baris.",
            },
        ],
    },
    {
        "title": "Kuis 5: JOIN & Lanjutan",
        "questions": [
            {
                "q": "JOIN yang hanya menampilkan data yang cocok di kedua tabel?",
                "options": ["LEFT JOIN", "INNER JOIN", "FULL JOIN", "SELF JOIN"],
                "answer": 1,
                "explanation": "INNER JOIN cuma mengambil baris yang memenuhi kondisi ON di kedua sisi.",
            },
            {
                "q": "JOIN yang menampilkan semua baris tabel kiri walau tidak cocok?",
                "options": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "CROSS JOIN"],
                "answer": 0,
                "explanation": "LEFT JOIN: semua baris tabel kiri tetap muncul, sisi kanan jadi NULL kalau nggak ada pasangannya.",
            },
            {
                "q": "Sintaks JOIN yang benar?",
                "options": [
                    "JOIN a, b ON a.id = b.id",
                    "FROM a JOIN b ON a.id = b.id",
                    "FROM a ON b JOIN a.id = b.id",
                    "FROM a JOIN b USING (a.id = b.id)",
                ],
                "answer": 1,
                "explanation": ("Polanya FROM tabelA JOIN tabelB ON kondisi_penghubung;. USING memang "
                                "ada, tapi isinya cuma nama kolom, misalnya USING (id)."),
            },
            {
                "q": "Kunci yang menghubungkan tabel di JOIN biasanya?",
                "options": [
                    "semua kolom yang ada di kedua tabel",
                    "foreign key yang menunjuk primary key",
                    "kolom pertama dari masing-masing tabel",
                    "kolom teks yang isinya mirip, misalnya nama",
                ],
                "answer": 1,
                "explanation": ("ON n.nim = m.nim membandingkan foreign key di satu tabel dengan "
                                "primary key di tabel lain. Nama bisa kembar, jadi nggak bisa diandalkan "
                                "sebagai penghubung."),
            },
            {
                "q": "Query untuk mencari mahasiswa yang BELUM pernah ikut ujian?",
                "options": [
                    "SELECT nama FROM m LEFT JOIN n ON m.nim=n.nim WHERE n.nim IS NULL;",
                    "SELECT nama FROM m JOIN n ON m.nim=n.nim WHERE n.nim IS NULL;",
                    "SELECT nama FROM m LEFT JOIN n ON m.nim=n.nim WHERE n.nim = NULL;",
                    "SELECT nama FROM m LEFT JOIN n ON m.nim=n.nim WHERE m.nim IS NULL;",
                ],
                "answer": 0,
                "explanation": ("LEFT JOIN mempertahankan semua mahasiswa, lalu n.nim IS NULL menyisakan "
                                "yang nggak punya pasangan. JOIN biasa (INNER) sudah membuang mereka duluan, "
                                "= NULL nggak pernah bernilai benar, dan m.nim nggak pernah kosong."),
            },
            {
                "q": "Subquery digunakan untuk?",
                "options": [
                    "menaruh query di dalam query lain",
                    "menyimpan query supaya bisa dipanggil lagi",
                    "menggabungkan dua tabel ke samping",
                    "menjalankan banyak query bergantian",
                ],
                "answer": 0,
                "explanation": ("Subquery itu SELECT di dalam query lain, ditulis dalam kurung, dan "
                                "hasilnya dipakai query luarnya. Yang disimpan untuk dipanggil lagi itu "
                                "VIEW, dan yang menggabungkan ke samping itu JOIN."),
            },
            {
                "q": "SELECT * FROM mahasiswa WHERE ipk > (SELECT AVG(ipk) FROM mahasiswa); Maksudnya?",
                "options": [
                    "ipk di atas rata-rata",
                    "ipk di bawah rata-rata",
                    "ipk terbesar",
                    "ipk terkecil",
                ],
                "answer": 0,
                "explanation": "Subquery menghitung rata-rata, lalu WHERE menyisakan ipk yang lebih besar dari angka itu.",
            },
            {
                "q": "Untuk menggabungkan hasil dua query dengan menghilangkan duplikat?",
                "options": ["JOIN", "UNION", "UNION ALL", "INTERSECT"],
                "answer": 1,
                "explanation": ("UNION menumpuk hasil dua query dan membuang yang dobel. UNION ALL "
                                "membiarkan yang dobel, dan INTERSECT cuma menyisakan baris yang ada "
                                "di kedua hasil."),
            },
            {
                "q": "CREATE INDEX berguna untuk?",
                "options": [
                    "mempercepat pencarian dan JOIN",
                    "mempercepat INSERT dan UPDATE",
                    "memperkecil ukuran tabel di disk",
                    "menolak data yang formatnya salah",
                ],
                "answer": 0,
                "explanation": ("Index mempercepat pencarian dan JOIN, tapi justru sedikit memperlambat "
                                "INSERT dan UPDATE karena index-nya ikut diperbarui, dan butuh ruang disk tambahan."),
            },
            {
                "q": "Redundansi data yang berlebihan biasanya diatasi dengan?",
                "options": ["index", "normalisasi", "transaksi", "backup"],
                "answer": 1,
                "explanation": "Normalisasi memecah tabel supaya satu fakta cuma disimpan di satu tempat.",
            },
        ],
    },
    {
        "title": "Kuis 6: Window Function & CTE",
        "questions": [
            {
                "q": "Perbedaan utama window function dengan GROUP BY?",
                "options": [
                    "Window function meringkas baris jadi lebih sedikit, sama seperti GROUP BY",
                    "Window function tetap menampilkan semua baris asli + kolom tambahan",
                    "Window function nggak bisa dipakai dengan ORDER BY",
                    "Nggak ada bedanya",
                ],
                "answer": 1,
                "explanation": "GROUP BY meringkas banyak baris jadi satu, window function membiarkan semua baris dan cuma menambah kolom hitungan.",
            },
            {
                "q": "ROW_NUMBER() OVER (PARTITION BY jurusan ORDER BY ipk DESC) menghasilkan?",
                "options": [
                    "nomor urut yang mulai dari 1 lagi di tiap jurusan",
                    "nomor urut berlanjut di seluruh tabel",
                    "peringkat ipk, nilai yang seri dapat nomor sama",
                    "jumlah mahasiswa di tiap jurusan, diurutkan",
                ],
                "answer": 0,
                "explanation": ("PARTITION BY memulai hitungan dari 1 lagi di tiap jurusan. ROW_NUMBER "
                                "selalu memberi nomor berbeda walau ipk-nya seri; yang memberi nomor "
                                "sama untuk nilai seri itu RANK."),
            },
            {
                "q": "Perbedaan RANK() dan DENSE_RANK() saat ada nilai seri (sama)?",
                "options": [
                    "Hasilnya selalu sama, cuma beda nama",
                    "RANK memberi 1, 1, 3; DENSE_RANK memberi 1, 1, 2",
                    "RANK memberi 1, 1, 2; DENSE_RANK memberi 1, 1, 3",
                    "RANK memberi 1, 2, 3; DENSE_RANK memberi 1, 1, 2",
                ],
                "answer": 1,
                "explanation": ("Dua nilai seri sama-sama dapat 1. RANK lalu melompat ke 3 karena dua "
                                "posisi sudah terpakai, DENSE_RANK lanjut ke 2 tanpa lompatan. Urutan "
                                "1, 2, 3 tanpa peduli seri itu ROW_NUMBER."),
            },
            {
                "q": "Klausa apa yang dipakai untuk mendefinisikan CTE?",
                "options": ["WITH", "AS CTE", "DEFINE", "TEMP TABLE"],
                "answer": 0,
                "explanation": "WITH nama_cte AS (SELECT ...) mendefinisikan sebuah CTE.",
            },
            {
                "q": "Keuntungan utama memakai CTE dibanding subquery bersarang biasa?",
                "options": [
                    "Query pasti jalan lebih cepat daripada subquery",
                    "Lebih gampang dibaca dan bisa dirujuk berulang",
                    "Hasilnya disimpan permanen seperti tabel biasa",
                    "Bisa menggantikan JOIN, jadi JOIN nggak perlu lagi",
                ],
                "answer": 1,
                "explanation": ("CTE memecah query rumit jadi blok bernama yang gampang dibaca dan bisa "
                                "dirujuk lebih dari sekali. Hasilnya cuma hidup selama query itu jalan, "
                                "dan nggak ada jaminan lebih cepat."),
            },
            {
                "q": "Recursive CTE paling cocok dipakai untuk data berbentuk?",
                "options": [
                    "tabel datar yang nggak merujuk dirinya sendiri",
                    "hierarki, misalnya atasan dan bawahan",
                    "ringkasan per kelompok hasil GROUP BY",
                    "data JSON yang disimpan dalam satu kolom",
                ],
                "answer": 1,
                "explanation": ("Recursive CTE menelusuri baris yang menunjuk baris lain di tabel yang "
                                "sama, seperti karyawan dan atasannya atau kategori bertingkat."),
            },
            {
                "q": "Bagian recursive CTE yang menjadi 'titik mulai' disebut?",
                "options": ["recursive member", "anchor member", "correlated subquery", "window frame"],
                "answer": 1,
                "explanation": ("Anchor member adalah query awal yang dijalankan sekali. Hasilnya lalu "
                                "disambung UNION ALL dengan recursive member, yang berulang sampai "
                                "nggak menghasilkan baris lagi."),
            },
        ],
    },
    {
        "title": "Kuis 7: View, Trigger & Transaction Lanjutan",
        "questions": [
            {
                "q": "VIEW pada dasarnya adalah?",
                "options": [
                    "tabel fisik yang menyimpan datanya",
                    "query bernama yang dibaca seperti tabel",
                    "cadangan otomatis dari tabel aslinya",
                    "index khusus supaya SELECT lebih cepat",
                ],
                "answer": 1,
                "explanation": ("VIEW cuma menyimpan query-nya, bukan datanya. Tiap kali dibaca, ia "
                                "mengambil data terbaru dari tabel asli."),
            },
            {
                "q": "TRIGGER dijalankan?",
                "options": [
                    "manual, dipanggil dengan perintah CALL",
                    "otomatis saat ada INSERT, UPDATE, atau DELETE",
                    "sekali saja, waktu database pertama dibuat",
                    "otomatis tiap selang waktu tertentu, seperti cron",
                ],
                "answer": 1,
                "explanation": ("Trigger aktif sendiri saat event yang didefinisikan terjadi pada "
                                "tabelnya. Yang dipanggil dengan CALL itu stored procedure, dan yang "
                                "jalan terjadwal itu EVENT di MySQL."),
            },
            {
                "q": "Di dalam trigger, NEW merujuk pada?",
                "options": ["data sebelum diubah", "data baru setelah diubah", "nama tabel", "nama trigger"],
                "answer": 1,
                "explanation": "NEW berisi data baru (setelah perubahan), OLD berisi data sebelum perubahan.",
            },
            {
                "q": "Prinsip ACID pada transaction, huruf 'A' berarti?",
                "options": ["Accuracy", "Atomicity", "Availability", "Authorization"],
                "answer": 1,
                "explanation": ("Atomicity: transaction berhasil semuanya atau dibatalkan semuanya, "
                                "nggak ada setengah jadi. Availability memang istilah database, tapi "
                                "dari teorema CAP, bukan ACID."),
            },
            {
                "q": "Dirty Read terjadi ketika?",
                "options": [
                    "membaca data yang sudah di-commit transaksi lain",
                    "membaca data yang belum di-commit transaksi lain",
                    "membaca baris yang sudah dihapus permanen",
                    "membaca dua kali dan dapat hasil berbeda",
                ],
                "answer": 1,
                "explanation": ("Dirty read artinya membaca perubahan yang belum di-commit, padahal "
                                "perubahan itu bisa saja di-rollback. Membaca dua kali dengan hasil "
                                "berbeda punya nama sendiri: non-repeatable read."),
            },
            {
                "q": "Isolation level PALING KETAT yang mencegah semua masalah baca serentak?",
                "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
                "answer": 3,
                "explanation": ("Serializable paling ketat: transaksi berjalan seolah antre satu per "
                                "satu. Harganya, performanya paling lambat."),
            },
            {
                "q": "Deadlock terjadi ketika?",
                "options": [
                    "satu transaksi berjalan terlalu lama sendirian",
                    "dua transaksi saling menunggu kunci milik lawannya",
                    "dua transaksi membaca baris yang sama pada saat bersamaan",
                    "transaksi gagal karena index-nya nggak dipakai",
                ],
                "answer": 1,
                "explanation": ("Deadlock itu kebuntuan: A menunggu kunci yang dipegang B, B menunggu "
                                "kunci yang dipegang A. Sekadar membaca baris yang sama nggak saling "
                                "mengunci."),
            },
            {
                "q": "Manakah yang merupakan karakteristik database NoSQL dibanding SQL?",
                "options": [
                    "Skema ketat yang wajib ditentukan sebelum isi data",
                    "Skemanya fleksibel, cocok untuk dokumen JSON",
                    "Selalu memakai tabel, relasi, dan JOIN",
                    "Nggak sanggup menyimpan data berukuran besar",
                ],
                "answer": 1,
                "explanation": ("NoSQL seperti MongoDB atau Redis menawarkan skema yang fleksibel. "
                                "Skema ketat dan JOIN justru ciri database SQL, dan banyak NoSQL "
                                "dibuat khusus untuk data sangat besar."),
            },
        ],
    },
]
