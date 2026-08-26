SQL_MATERIALS = [
    {
        "title": "1. Pengenalan Database & SQL",
        "sections": [
            {
                "body": [
                    "Apa itu Database?",
                    "  - Tempat penyimpanan data secara terstruktur.",
                    "  - Data disimpan dalam bentuk Tabel (baris & kolom), seperti Excel.",
                    "",
                    "Apa itu SQL?",
                    "  - SQL = Structured Query Language.",
                    "  - Bahasa untuk mengelola data di database relasional.",
                    "  - Standar internasional, dipakai hampir semua database.",
                    "",
                    "Jenis-jenis perintah SQL:",
                    "  DDL - Data Definition Language (membuat struktur):",
                    "        CREATE, ALTER, DROP, TRUNCATE",
                    "  DML - Data Manipulation Language (mengelola data):",
                    "        INSERT, UPDATE, DELETE, SELECT",
                    "  DCL - Data Control Language (hak akses):",
                    "        GRANT, REVOKE",
                    "  TCL - Transaction Control Language:",
                    "        COMMIT, ROLLBACK, SAVEPOINT",
                    "",
                    "Database yang umum dipakai:",
                    "  - MySQL / MariaDB (paling populer untuk pemula)",
                    "  - PostgreSQL (fitur lengkap, gratis)",
                    "  - SQL Server (Microsoft)",
                    "  - Oracle (enterprise)",
                    "  - SQLite (file kecil, untuk aplikasi lokal)",
                    "",
                    "Struktur data:",
                    "  Database -> Tabel -> Kolom & Baris -> Sel",
                    "",
                    "Tabel contoh: MAHASISWA",
                    "  nim   | nama  | jurusan     | ipk",
                    "  ------+-------+-------------+-----",
                    "  101   | Andi  | Informatika | 3.5",
                    "  102   | Budi  | Sistem Info | 3.2",
                ]
            },
            {
                "body": [
                    "Membuat database baru di MySQL:",
                    "  CREATE DATABASE belajar_db;",
                    "  USE belajar_db;",
                    "",
                    "Menjalankan perintah di terminal (MySQL):",
                    "  mysql -u root -p",
                    "  lalu ketik perintah SQL dan akhiri dengan titik koma (;).",
                    "",
                    "Aturan penulisan SQL:",
                    "  1. Tidak case-sensitive: SELECT = select = Select.",
                    "     Namun konvensi: KATA KUNCI ditulis UPPERCASE.",
                    "  2. Setiap statement diakhiri titik koma (;).",
                    "  3. Komentar satu baris  : -- teks",
                    "  4. Komentar beberapa baris: /* teks */",
                    "  5. Nama tabel/kolom biasanya lowercase/snake_case.",
                    "",
                    "Contoh komentar:",
                    "  -- ini komentar",
                    "  SELECT * FROM mahasiswa;  -- ambil semua data",
                ]
            },
        ],
    },
    {
        "title": "2. DDL: Membuat Struktur Tabel",
        "sections": [
            {
                "body": [
                    "DDL (Data Definition Language) untuk membuat/mengubah struktur.",
                    "",
                    "CREATE TABLE:",
                    "  CREATE TABLE nama_tabel (",
                    "      kolom1 tipe_data [batasan],",
                    "      kolom2 tipe_data [batasan],",
                    "      ...",
                    "  );",
                    "",
                    "Tipe data umum di MySQL:",
                    "  INT             -> bilangan bulat",
                    "  VARCHAR(n)      -> teks maksimal n karakter",
                    "  TEXT            -> teks panjang",
                    "  DATE            -> tanggal (YYYY-MM-DD)",
                    "  DATETIME        -> tanggal + jam",
                    "  DECIMAL(p,s)    -> desimal presisi (misal 10,2)",
                    "  BOOLEAN         -> true/false (disimpan 1/0)",
                    "  FLOAT / DOUBLE  -> desimal",
                ]
            },
            {
                "heading": "Contoh CREATE TABLE",
                "code": """CREATE TABLE mahasiswa (
    nim      INT          PRIMARY KEY,
    nama     VARCHAR(100) NOT NULL,
    jurusan  VARCHAR(50),
    ipk      DECIMAL(3,2) DEFAULT 0.00,
    tanggal  DATE
);

CREATE TABLE mata_kuliah (
    kode  VARCHAR(10) PRIMARY KEY,
    nama  VARCHAR(100) NOT NULL,
    sks   INT          DEFAULT 3
);"""
            },
            {
                "body": [
                    "Batasan (constraint):",
                    "  PRIMARY KEY      -> kunci utama, unik & tidak boleh null.",
                    "  FOREIGN KEY      -> menghubungkan ke tabel lain.",
                    "  NOT NULL         -> wajib diisi.",
                    "  UNIQUE           -> tidak boleh duplikat.",
                    "  DEFAULT nilai    -> nilai awal jika tidak diisi.",
                    "  AUTO_INCREMENT   -> otomatis bertambah (untuk angka).",
                    "  CHECK            -> validasi (MySQL 8+).",
                    "",
                    "Contoh dengan FOREIGN KEY:",
                    "  CREATE TABLE nilai (",
                    "      id INT PRIMARY KEY AUTO_INCREMENT,",
                    "      nim INT,",
                    "      kode VARCHAR(10),",
                    "      skor INT CHECK (skor BETWEEN 0 AND 100),",
                    "      FOREIGN KEY (nim) REFERENCES mahasiswa(nim),",
                    "      FOREIGN KEY (kode) REFERENCES mata_kuliah(kode)",
                    "  );",
                ]
            },
            {
                "heading": "ALTER & DROP",
                "code": """-- Menambah kolom baru
ALTER TABLE mahasiswa ADD email VARCHAR(100);

-- Mengubah tipe kolom
ALTER TABLE mahasiswa MODIFY nama VARCHAR(150);

-- Menghapus kolom
ALTER TABLE mahasiswa DROP COLUMN email;

-- Menghapus seluruh tabel beserta strukturnya
DROP TABLE mahasiswa;

-- Menghapus semua DATA tapi struktur tetap
TRUNCATE TABLE mahasiswa;

-- Menghapus database
DROP DATABASE belajar_db;"""
            },
        ],
    },
    {
        "title": "3. DML: Insert, Update, Delete",
        "sections": [
            {
                "body": [
                    "DML (Data Manipulation Language) untuk mengelola DATA di tabel.",
                    "",
                    "INSERT - menambahkan data:",
                    "  INSERT INTO tabel (kolom1, kolom2, ...)",
                    "  VALUES (nilai1, nilai2, ...);",
                    "",
                    "  INSERT INTO mahasiswa (nim, nama, jurusan, ipk)",
                    "  VALUES (101, 'Andi', 'Informatika', 3.5);",
                    "",
                    "  INSERT beberapa baris sekaligus:",
                    "  INSERT INTO mahasiswa VALUES",
                    "      (102, 'Budi', 'Sistem Info', 3.2),",
                    "      (103, 'Citra', 'Informatika', 3.8);",
                    "",
                    "Catatan:",
                    "  - Nilai teks/tanggal pakai tanda kutip '...'.",
                    "  - Angka tidak perlu kutip.",
                ]
            },
            {
                "heading": "UPDATE & DELETE",
                "code": """-- UPDATE data
UPDATE mahasiswa
SET ipk = 3.7
WHERE nim = 101;

-- UPDATE beberapa kolom
UPDATE mahasiswa
SET jurusan = 'Data Science', ipk = 3.9
WHERE nim = 103;

-- DELETE data (PENTING: selalu pakai WHERE!)
DELETE FROM mahasiswa WHERE nim = 102;

-- Menghapus semua data
DELETE FROM mahasiswa;"""
            },
            {
                "body": [
                    "PERINGATAN PENTING:",
                    "  UPDATE dan DELETE tanpa WHERE akan memengaruhi",
                    "  SEMUA baris di tabel!",
                    "",
                    "  UPDATE mahasiswa SET ipk = 0;   -- ipk semua jadi 0!",
                    "  DELETE FROM mahasiswa;          -- data habis semua!",
                    "",
                    "Latihan kebiasaan baik:",
                    "  1. SELECT dulu dengan WHERE yang sama sebelum UPDATE/DELETE.",
                    "  2. Aktifkan transaction (BEGIN/COMMIT/ROLLBACK) saat data penting.",
                    "  3. Backup sebelum operasi massal.",
                    "",
                    "Transaction:",
                    "  START TRANSACTION;",
                    "  UPDATE ...;",
                    "  DELETE ...;",
                    "  ROLLBACK;   -- batalkan semua perubahan",
                    "  -- atau",
                    "  COMMIT;     -- simpan permanen",
                ]
            },
        ],
    },
    {
        "title": "4. SELECT & Filtering",
        "sections": [
            {
                "body": [
                    "SELECT adalah perintah paling sering dipakai.",
                    "Gunakan untuk membaca/menampilkan data.",
                    "",
                    "Sintaks dasar:",
                    "  SELECT kolom1, kolom2 FROM nama_tabel;",
                    "  SELECT * FROM nama_tabel;   -- semua kolom",
                    "",
                    "  SELECT nama, ipk FROM mahasiswa;",
                    "",
                    "Alias (nama sementara):",
                    "  SELECT nama AS 'Nama Lengkap', ipk AS IPK FROM mahasiswa;",
                    "  -- AS boleh dihilangkan:  SELECT nama 'Nama Lengkap' FROM mahasiswa;",
                    "",
                    "Menghilangkan duplikat:",
                    "  SELECT DISTINCT jurusan FROM mahasiswa;",
                ]
            },
            {
                "heading": "Contoh data untuk latihan",
                "code": """CREATE TABLE mahasiswa (
    nim INT PRIMARY KEY,
    nama VARCHAR(50),
    jurusan VARCHAR(30),
    ipk DECIMAL(3,2),
    angkatan YEAR
);

INSERT INTO mahasiswa VALUES
(101, 'Andi',   'Informatika', 3.5, 2023),
(102, 'Budi',   'Informatika', 3.2, 2023),
(103, 'Citra',  'Sistem Info', 3.8, 2022),
(104, 'Dewi',   'Sistem Info', 2.9, 2022),
(105, 'Eko',    'Teknik Komp', 3.6, 2021),
(106, 'Farah',  'Informatika', 4.0, 2021),
(107, 'Gilang', 'Teknik Komp', 2.7, 2023);"""
            },
            {
                "heading": "WHERE & operator perbandingan",
                "code": """-- Data Informatika saja
SELECT * FROM mahasiswa WHERE jurusan = 'Informatika';

-- IPK di atas 3.5
SELECT * FROM mahasiswa WHERE ipk > 3.5;

-- Bukan Informatika
SELECT * FROM mahasiswa WHERE jurusan != 'Informatika';

-- Angkatan 2022 atau 2023
SELECT * FROM mahasiswa WHERE angkatan IN (2022, 2023);

-- Nama diawali huruf C
SELECT * FROM mahasiswa WHERE nama LIKE 'C%';

-- IPK antara 3.0 dan 3.8
SELECT * FROM mahasiswa WHERE ipk BETWEEN 3.0 AND 3.8;

-- Kolom ipk tidak kosong
SELECT * FROM mahasiswa WHERE ipk IS NOT NULL;"""
            },
            {
                "body": [
                    "Operator logika AND, OR, NOT:",
                    "  SELECT * FROM mahasiswa",
                    "  WHERE jurusan = 'Informatika' AND ipk > 3.4;",
                    "",
                    "  SELECT * FROM mahasiswa",
                    "  WHERE jurusan = 'Informatika' OR jurusan = 'Teknik Komp';",
                    "",
                    "  SELECT * FROM mahasiswa",
                    "  WHERE NOT angkatan = 2021;",
                    "",
                    "LIKE (pencarian teks):",
                    "  %  -> nol atau lebih karakter",
                    "  _  -> tepat satu karakter",
                    "  LIKE 'A%'   -> diawali A  (Andi)",
                    "  LIKE '%a'   -> diakhiri a  (Citra, Dewi, Farah)",
                    "  LIKE '%di%' -> mengandung 'di' (Andi, Budi)",
                    "  LIKE 'B_d_' -> B diikuti 1 karakter, d, 1 karakter",
                    "",
                    "Pengurutan hasil (ORDER BY):",
                    "  SELECT * FROM mahasiswa ORDER BY ipk DESC;",
                    "  SELECT * FROM mahasiswa ORDER BY angkatan ASC, ipk DESC;",
                ]
            },
        ],
    },
    {
        "title": "5. Agregasi & Grouping",
        "sections": [
            {
                "body": [
                    "Fungsi agregat = meringkas banyak baris menjadi satu nilai.",
                    "",
                    "  COUNT(kolom)  -> jumlah baris",
                    "  SUM(kolom)    -> total penjumlahan",
                    "  AVG(kolom)    -> rata-rata",
                    "  MIN(kolom)    -> nilai terkecil",
                    "  MAX(kolom)    -> nilai terbesar",
                    "",
                    "Contoh:",
                    "  SELECT COUNT(*) FROM mahasiswa;         -- 7",
                    "  SELECT AVG(ipk) FROM mahasiswa;         -- rata-rata ipk",
                    "  SELECT MAX(ipk), MIN(ipk) FROM mahasiswa;",
                    "  SELECT SUM(sks) FROM mata_kuliah;",
                    "",
                    "COUNT(*) menghitung semua baris.",
                    "COUNT(kolom) mengabaikan nilai NULL.",
                    "COUNT(DISTINCT kolom) menghitung nilai unik.",
                ]
            },
            {
                "heading": "GROUP BY & HAVING",
                "code": """-- Rata-rata IPK per jurusan
SELECT jurusan, AVG(ipk) AS rata_ipk
FROM mahasiswa
GROUP BY jurusan;

-- Jumlah mahasiswa per angkatan
SELECT angkatan, COUNT(*) AS jumlah
FROM mahasiswa
GROUP BY angkatan;

-- Jurusan dengan rata-rata > 3.3 (filter hasil agregat)
SELECT jurusan, AVG(ipk) AS rata_ipk
FROM mahasiswa
GROUP BY jurusan
HAVING AVG(ipk) > 3.3;

-- Urutkan dari terbaik
SELECT jurusan, AVG(ipk) AS rata_ipk
FROM mahasiswa
GROUP BY jurusan
ORDER BY rata_ipk DESC;"""
            },
            {
                "body": [
                    "WHERE vs HAVING:",
                    "  WHERE  -> memfilter BARIS sebelum dikelompokkan.",
                    "  HAVING -> memfilter HASIL agregat setelah GROUP BY.",
                    "",
                    "  SELECT jurusan, AVG(ipk)",
                    "  FROM mahasiswa",
                    "  WHERE angkatan >= 2022     -- filter baris dulu",
                    "  GROUP BY jurusan",
                    "  HAVING AVG(ipk) > 3.0;     -- filter hasil grup",
                    "",
                    "Urutan penulisan klausa SELECT yang benar:",
                    "  SELECT  kolom, agregat",
                    "  FROM    tabel",
                    "  WHERE   filter baris",
                    "  GROUP BY kolom",
                    "  HAVING  filter agregat",
                    "  ORDER BY kolom",
                    "  LIMIT   jumlah;",
                    "",
                    "Urutan eksekusi di DB (logika):",
                    "  FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT",
                ]
            },
        ],
    },
    {
        "title": "6. JOIN: Menghubungkan Tabel",
        "sections": [
            {
                "body": [
                    "JOIN menggabungkan data dari 2 tabel atau lebih berdasarkan",
                    "kolom yang berhubungan (biasanya kunci).",
                    "",
                    "Jenis JOIN:",
                    "  INNER JOIN -> hanya baris yang cocok di kedua tabel.",
                    "  LEFT JOIN  -> semua baris tabel kiri + yang cocok di kanan.",
                    "  RIGHT JOIN -> semua baris tabel kanan + yang cocok di kiri.",
                    "  FULL OUTER JOIN -> semua baris kedua sisi (MySQL tidak punya).",
                    "  CROSS JOIN -> semua kombinasi baris.",
                    "",
                    "Visual INNER JOIN:",
                    "  [A]====[B]  hanya irisan yang muncul.",
                    "",
                    "Visual LEFT JOIN:",
                    "  [A]----->  semua A, irisan B. B yang tak cocok jadi NULL.",
                    "",
                    "Sintaks:",
                    "  SELECT kolom",
                    "  FROM tabel_a",
                    "  JOIN tabel_b ON tabel_a.kunci = tabel_b.kunci;",
                ]
            },
            {
                "heading": "Contoh data relasi",
                "code": """CREATE TABLE mahasiswa (
    nim INT PRIMARY KEY,
    nama VARCHAR(50),
    jurusan VARCHAR(30)
);

CREATE TABLE mata_kuliah (
    kode VARCHAR(10) PRIMARY KEY,
    nama VARCHAR(60),
    sks INT
);

CREATE TABLE nilai (
    nim INT,
    kode VARCHAR(10),
    skor INT,
    PRIMARY KEY (nim, kode),
    FOREIGN KEY (nim) REFERENCES mahasiswa(nim),
    FOREIGN KEY (kode) REFERENCES mata_kuliah(kode)
);"""
            },
            {
                "heading": "Contoh INNER JOIN",
                "code": """-- Nilai + nama mahasiswa + nama matkul
SELECT m.nama AS mahasiswa, mk.nama AS matkul, n.skor
FROM nilai n
INNER JOIN mahasiswa m ON n.nim = m.nim
INNER JOIN mata_kuliah mk ON n.kode = mk.kode
ORDER BY m.nama;

-- Rata-rata skor per mahasiswa
SELECT m.nama, AVG(n.skor) AS rata2
FROM nilai n
JOIN mahasiswa m ON n.nim = m.nim
GROUP BY m.nama;

-- Rata-rata skor per mata kuliah
SELECT mk.nama, AVG(n.skor) AS rata2
FROM nilai n
JOIN mata_kuliah mk ON n.kode = mk.kode
GROUP BY mk.nama;"""
            },
            {
                "heading": "Contoh LEFT JOIN",
                "code": """-- Semua mahasiswa + nilai (yang belum punya nilai tampil NULL)
SELECT m.nama, n.kode, n.skor
FROM mahasiswa m
LEFT JOIN nilai n ON m.nim = n.nim
ORDER BY m.nama;

-- Mahasiswa yang BELUM mengikuti ujian
SELECT m.nama
FROM mahasiswa m
LEFT JOIN nilai n ON m.nim = n.nim
WHERE n.nim IS NULL;"""
            },
            {
                "body": [
                    "Self Join: tabel digabung dengan dirinya sendiri.",
                    "  -- Contoh: relasi karyawan - atasan",
                    "  SELECT k.nama AS karyawan, a.nama AS atasan",
                    "  FROM karyawan k",
                    "  LEFT JOIN karyawan a ON k.atasan_id = a.id;",
                    "",
                    "Alias tabel:",
                    "  memakai singkatan (m, n, mk) agar query lebih pendek.",
                    "",
                    "Tips membaca JOIN:",
                    "  1. Tentukan kolom hasil yang diinginkan.",
                    "  2. Identifikasi tabel sumbernya.",
                    "  3. Temukan kolom penghubung antar tabel.",
                    "  4. Mulai dari tabel utama, gabung satu per satu.",
                ]
            },
        ],
    },
    {
        "title": "7. Subquery & Fungsi Lanjutan",
        "sections": [
            {
                "body": [
                    "Subquery = query di dalam query.",
                    "Hasilnya dipakai oleh query utama.",
                    "",
                    "Contoh penggunaan:",
                    "  - Mencari nilai terbesar dengan informasi lengkap.",
                    "  - Memfilter dengan hasil agregat.",
                    "  - Menggabungkan 2 hasil query.",
                    "",
                    "Subquery yang mengembalikan satu nilai (scalar):",
                    "  SELECT nama, ipk FROM mahasiswa",
                    "  WHERE ipk = (SELECT MAX(ipk) FROM mahasiswa);",
                    "",
                    "Subquery dengan IN:",
                    "  SELECT nama FROM mahasiswa",
                    "  WHERE nim IN (SELECT nim FROM nilai WHERE skor > 90);",
                ]
            },
            {
                "heading": "Contoh subquery",
                "code": """-- Mahasiswa dengan IPK di atas rata-rata
SELECT nama, ipk
FROM mahasiswa
WHERE ipk > (SELECT AVG(ipk) FROM mahasiswa);

-- Jurusan dengan jumlah terbanyak
SELECT jurusan, COUNT(*) AS jumlah
FROM mahasiswa
GROUP BY jurusan
ORDER BY jumlah DESC
LIMIT 1;

-- Nilai di atas rata-rata skor kelas
SELECT m.nama, mk.nama, n.skor
FROM nilai n
JOIN mahasiswa m ON n.nim = m.nim
JOIN mata_kuliah mk ON n.kode = mk.kode
WHERE n.skor > (SELECT AVG(skor) FROM nilai);"""
            },
            {
                "body": [
                    "Fungsi string:",
                    "  CONCAT(a, b)      -> gabung teks",
                    "  UPPER(teks)       -> huruf besar",
                    "  LOWER(teks)       -> huruf kecil",
                    "  LENGTH(teks)      -> panjang teks",
                    "  SUBSTRING(teks, mulai, panjang) -> potong teks",
                    "  REPLACE(teks, a, b) -> ganti 'a' jadi 'b'",
                    "  TRIM(teks)        -> buang spasi ujung",
                    "",
                    "Fungsi tanggal:",
                    "  NOW()             -> tanggal & jam sekarang",
                    "  CURDATE()         -> tanggal sekarang",
                    "  YEAR(tanggal), MONTH(tanggal), DAY(tanggal)",
                    "  DATEDIFF(a, b)    -> selisih hari",
                    "  DATE_FORMAT(t, '%d-%m-%Y') -> format tanggal",
                    "",
                    "  SELECT CONCAT(nama, ' - ', jurusan) AS info FROM mahasiswa;",
                ]
            },
            {
                "heading": "UNION & penggabungan",
                "code": """-- Gabungkan hasil 2 query (baris unik)
SELECT nama FROM dosen
UNION
SELECT nama FROM mahasiswa;

-- UNION ALL menyimpan duplikat
SELECT nama FROM dosen
UNION ALL
SELECT nama FROM mahasiswa;

-- Syarat UNION: jumlah & tipe kolom harus sama."""
            },
        ],
    },
    {
        "title": "8. Index, Normalisasi & Best Practice",
        "sections": [
            {
                "body": [
                    "INDEX:",
                    "  - Struktur khusus agar pencarian lebih cepat.",
                    "  - Seperti daftar isi di buku.",
                    "  - PRIMARY KEY otomatis ter-index.",
                    "",
                    "  CREATE INDEX idx_nama ON mahasiswa(nama);",
                    "  CREATE UNIQUE INDEX idx_nim ON mahasiswa(nim);",
                    "  DROP INDEX idx_nama ON mahasiswa;",
                    "",
                    "Kapan pakai index:",
                    "  - Kolom yang sering dipakai di WHERE / JOIN.",
                    "  - Data sudah banyak (ribuan+ baris).",
                    "  - Hati-hati: index mempercepat SELECT tapi memperlambat",
                    "    INSERT/UPDATE/DELETE dan memakai ruang.",
                ]
            },
            {
                "body": [
                    "NORMALISASI:",
                    "  Proses merapikan struktur tabel agar tidak boros dan",
                    "  terhindar dari data duplikat (redundansi).",
                    "",
                    "1NF - Kolom atomik (tidak boleh ada nilai ganda di satu sel).",
                    "  X  hobi: 'membaca, main game' -> pecah jadi baris.",
                    "",
                    "2NF - Tidak boleh ada kolom non-kunci yang hanya bergantung",
                    "      pada sebagian kunci (untuk tabel dengan kunci gabungan).",
                    "",
                    "3NF - Tidak boleh ada kolom yang bergantung ke kolom lain",
                    "      selain kunci utama (transitive dependency).",
                    "",
                    "Contoh buruk:",
                    "  nilai (nim, nama, jurusan, kode, skor)",
                    "  -> 'nama' & 'jurusan' hanya bergantung pada 'nim'.",
                    "  -> Pecah jadi tabel mahasiswa & tabel nilai.",
                    "",
                    "Hubungan antar tabel:",
                    "  1:1  -> satu-ke-satu",
                    "  1:N  -> satu-ke-banyak (paling umum)",
                    "  N:M  -> banyak-ke-banyak (butuh tabel penghubung)",
                ]
            },
            {
                "body": [
                    "Best practice SQL:",
                    "  1. Selalu pakai WHERE pada UPDATE & DELETE.",
                    "  2. Pilih kolom spesifik, hindari SELECT * saat data besar.",
                    "  3. Gunakan alias agar query jelas.",
                    "  4. Format query dengan rapi (per kata kunci satu baris).",
                    "  5. Pelajari EXPLAIN untuk analisa performa:",
                    "     EXPLAIN SELECT * FROM mahasiswa WHERE ipk > 3.0;",
                    "  6. Gunakan transaction untuk operasi penting.",
                    "  7. Back up database secara rutin.",
                    "  8. Kombinasikan dengan JDBC/Spring untuk aplikasi Java:",
                    "     - JDBC: API bawaan Java untuk akses database.",
                    "     - JPA/Hibernate: ORM yang memetakan tabel ke objek Java.",
                    "",
                    "Tips jadi handal:",
                    "  - Latih query di MySQL setiap hari.",
                    "  - Kerjakan soal JOIN & agregasi (yang paling sering ditanya).",
                    "  - Gabungkan dengan Java (JDBC) lalu Spring Boot.",
                ]
            },
        ],
    },
    {
        "title": "9. Window Function (Fungsi Jendela)",
        "sections": [
            {
                "body": [
                    "Window Function = fungsi agregat yang TIDAK meringkas baris",
                    "menjadi satu, tapi tetap menampilkan SEMUA baris asli",
                    "sambil menambahkan kolom hasil perhitungan per 'jendela' data.",
                    "",
                    "Beda dengan GROUP BY:",
                    "  GROUP BY      -> N baris jadi lebih sedikit baris (diringkas).",
                    "  Window Function -> tetap N baris, ditambah kolom baru.",
                    "",
                    "Sintaks umum:",
                    "  fungsi() OVER (",
                    "      PARTITION BY kolom   -- (opsional) kelompokkan seperti GROUP BY",
                    "      ORDER BY kolom        -- urutan dalam tiap partisi",
                    "  )",
                    "",
                    "Fungsi window yang sering dipakai:",
                    "  ROW_NUMBER()  -> nomor urut unik per baris (1,2,3,...)",
                    "  RANK()        -> peringkat, boleh sama, lompat jika ada seri",
                    "  DENSE_RANK()  -> peringkat, boleh sama, TIDAK lompat",
                    "  SUM()/AVG()/COUNT() OVER (...) -> agregat berjalan (running total)",
                ]
            },
            {
                "heading": "Contoh ROW_NUMBER, RANK, DENSE_RANK",
                "code": """-- Ranking mahasiswa berdasarkan IPK per jurusan
SELECT
    nama,
    jurusan,
    ipk,
    ROW_NUMBER() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS no_urut,
    RANK()       OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS peringkat,
    DENSE_RANK() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS peringkat_rapat
FROM mahasiswa;

-- Contoh hasil jika ada IPK yang sama (3.5, 3.5, 3.2):
-- RANK        -> 1, 1, 3   (lompat ke 3 karena 2 orang di posisi 1)
-- DENSE_RANK  -> 1, 1, 2   (tidak lompat)"""
            },
            {
                "heading": "Running total & perbandingan antar baris",
                "code": """-- Total penjualan berjalan (running total) per bulan
SELECT
    bulan,
    total_penjualan,
    SUM(total_penjualan) OVER (ORDER BY bulan) AS total_berjalan
FROM penjualan_bulanan;

-- Membandingkan dengan baris sebelumnya/berikutnya
SELECT
    bulan,
    total_penjualan,
    LAG(total_penjualan, 1) OVER (ORDER BY bulan) AS bulan_lalu,
    LEAD(total_penjualan, 1) OVER (ORDER BY bulan) AS bulan_depan
FROM penjualan_bulanan;

-- Mengambil TOP 3 mahasiswa per jurusan (kombinasi dengan subquery)
SELECT * FROM (
    SELECT nama, jurusan, ipk,
           RANK() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS rk
    FROM mahasiswa
) hasil
WHERE rk <= 3;"""
            },
            {
                "body": [
                    "Kapan window function sangat berguna:",
                    "  - Membuat leaderboard / ranking per kategori.",
                    "  - Laporan running total (kumulatif) penjualan/keuangan.",
                    "  - Membandingkan nilai bulan ini vs bulan lalu (LAG/LEAD).",
                    "  - Mengambil TOP-N per grup (misal: 3 produk terlaris tiap kategori).",
                    "",
                    "Window function dijalankan SETELAH WHERE/GROUP BY tapi SEBELUM",
                    "ORDER BY final, sehingga tidak bisa langsung dipakai di klausa",
                    "WHERE (karena itu perlu dibungkus subquery seperti contoh TOP 3 di atas).",
                ]
            },
        ],
    },
    {
        "title": "10. Common Table Expression (CTE) & Recursive Query",
        "sections": [
            {
                "body": [
                    "CTE (Common Table Expression) = 'tabel sementara' yang",
                    "didefinisikan dengan klausa WITH, hanya berlaku untuk satu query.",
                    "",
                    "Manfaat CTE dibanding subquery biasa:",
                    "  1. Lebih mudah dibaca (query kompleks dipecah jadi blok bernama).",
                    "  2. Bisa dipakai berkali-kali dalam query yang sama.",
                    "  3. Mendukung query REKURSIF (memanggil dirinya sendiri).",
                    "",
                    "Sintaks dasar:",
                    "  WITH nama_cte AS (",
                    "      SELECT ...",
                    "  )",
                    "  SELECT * FROM nama_cte WHERE ...;",
                ]
            },
            {
                "heading": "Contoh CTE sederhana & bertingkat",
                "code": """-- CTE sederhana: rata-rata ipk per jurusan, lalu dipakai lagi
WITH rata_jurusan AS (
    SELECT jurusan, AVG(ipk) AS rata_ipk
    FROM mahasiswa
    GROUP BY jurusan
)
SELECT m.nama, m.jurusan, m.ipk, r.rata_ipk
FROM mahasiswa m
JOIN rata_jurusan r ON m.jurusan = r.jurusan
WHERE m.ipk > r.rata_ipk;

-- Beberapa CTE sekaligus (dipisah koma)
WITH
total_per_kategori AS (
    SELECT kategori_id, SUM(harga * stok) AS total_nilai
    FROM produk
    GROUP BY kategori_id
),
kategori_teratas AS (
    SELECT * FROM total_per_kategori ORDER BY total_nilai DESC LIMIT 3
)
SELECT k.nama, t.total_nilai
FROM kategori_teratas t
JOIN kategori k ON t.kategori_id = k.id;"""
            },
            {
                "heading": "Recursive CTE: struktur hierarki (atasan-bawahan)",
                "code": """-- Tabel karyawan dengan relasi atasan (self-referencing)
CREATE TABLE karyawan (
    id INT PRIMARY KEY,
    nama VARCHAR(50),
    atasan_id INT
);

-- Recursive CTE: cari semua bawahan dari 'Direktur' (id=1) di semua level
WITH RECURSIVE hierarki AS (
    -- anchor: baris awal (Direktur sendiri)
    SELECT id, nama, atasan_id, 1 AS level
    FROM karyawan
    WHERE id = 1

    UNION ALL

    -- recursive: cari bawahan dari hasil sebelumnya, level bertambah
    SELECT k.id, k.nama, k.atasan_id, h.level + 1
    FROM karyawan k
    JOIN hierarki h ON k.atasan_id = h.id
)
SELECT * FROM hierarki ORDER BY level;"""
            },
            {
                "body": [
                    "Recursive CTE sangat berguna untuk data berbentuk POHON/HIERARKI:",
                    "  - Struktur organisasi (atasan - bawahan).",
                    "  - Kategori bertingkat (kategori > sub-kategori > sub-sub-kategori).",
                    "  - Komentar bersarang (comment - reply - reply dari reply).",
                    "",
                    "Struktur recursive CTE selalu ada 2 bagian dipisah UNION ALL:",
                    "  1. Anchor member  -> query awal (titik mulai).",
                    "  2. Recursive member -> query yang merujuk CTE itu sendiri,",
                    "     berhenti otomatis saat tidak ada baris baru yang cocok.",
                ]
            },
        ],
    },
    {
        "title": "11. View, Stored Procedure & Trigger",
        "sections": [
            {
                "body": [
                    "VIEW = 'tabel virtual' hasil dari sebuah query yang disimpan",
                    "dengan nama, tapi tidak menyimpan data sendiri (selalu live/update).",
                    "",
                    "Manfaat VIEW:",
                    "  1. Menyederhanakan query kompleks yang sering dipakai berulang.",
                    "  2. Menyembunyikan detail tabel asli (keamanan/abstraksi).",
                    "  3. Bisa diberi hak akses berbeda dari tabel aslinya.",
                ]
            },
            {
                "heading": "Contoh membuat & memakai VIEW",
                "code": """CREATE VIEW mahasiswa_unggulan AS
SELECT nim, nama, jurusan, ipk
FROM mahasiswa
WHERE ipk >= 3.5;

-- Pakai VIEW seperti tabel biasa
SELECT * FROM mahasiswa_unggulan WHERE jurusan = 'Informatika';

-- Menghapus view
DROP VIEW mahasiswa_unggulan;"""
            },
            {
                "body": [
                    "STORED PROCEDURE = kumpulan perintah SQL yang disimpan di",
                    "database dan bisa dipanggil sewaktu-waktu seperti memanggil fungsi.",
                    "",
                    "Manfaat:",
                    "  1. Logika bisnis bisa dijalankan di sisi database (lebih cepat,",
                    "     mengurangi bolak-balik data ke aplikasi).",
                    "  2. Dipakai ulang oleh banyak aplikasi yang mengakses DB yang sama.",
                    "  3. Bisa punya parameter, percabangan, dan perulangan.",
                ]
            },
            {
                "heading": "Contoh Stored Procedure (sintaks MySQL)",
                "code": """DELIMITER //

CREATE PROCEDURE TambahMahasiswa(
    IN p_nim INT,
    IN p_nama VARCHAR(100),
    IN p_jurusan VARCHAR(50)
)
BEGIN
    INSERT INTO mahasiswa (nim, nama, jurusan, ipk)
    VALUES (p_nim, p_nama, p_jurusan, 0.00);
END //

DELIMITER ;

-- Memanggil procedure
CALL TambahMahasiswa(201, 'Hesti', 'Informatika');"""
            },
            {
                "body": [
                    "TRIGGER = kode yang dijalankan OTOMATIS ketika sebuah event",
                    "terjadi pada tabel (INSERT, UPDATE, atau DELETE).",
                    "",
                    "Contoh kegunaan trigger:",
                    "  - Mencatat log setiap kali data diubah (audit trail).",
                    "  - Validasi tambahan sebelum data disimpan.",
                    "  - Update otomatis kolom lain (misal: stok berkurang saat ada penjualan).",
                ]
            },
            {
                "heading": "Contoh TRIGGER: catat log otomatis",
                "code": """CREATE TABLE log_mahasiswa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nim INT,
    aksi VARCHAR(20),
    waktu DATETIME
);

DELIMITER //

CREATE TRIGGER after_update_mahasiswa
AFTER UPDATE ON mahasiswa
FOR EACH ROW
BEGIN
    INSERT INTO log_mahasiswa (nim, aksi, waktu)
    VALUES (NEW.nim, 'UPDATE', NOW());
END //

DELIMITER ;

-- NEW merujuk data BARU (setelah diubah), OLD merujuk data SEBELUM diubah.
-- Trigger ini otomatis jalan setiap kali UPDATE mahasiswa dijalankan."""
            },
            {
                "body": [
                    "Catatan penting:",
                    "  - View, Procedure, dan Trigger memindahkan sebagian LOGIKA",
                    "    ke database, bukan hanya penyimpanan data.",
                    "  - Gunakan secukupnya - logika bisnis yang kompleks umumnya",
                    "    lebih baik ditulis di kode aplikasi (Java/Spring Boot) agar",
                    "    mudah di-test, di-debug, dan di-version control (Git).",
                    "  - Tetap penting dipahami karena banyak sistem lama (legacy)",
                    "    dan sistem enterprise memakainya secara ekstensif.",
                ]
            },
        ],
    },
    {
        "title": "12. Transaction & Isolation Level Lanjutan",
        "sections": [
            {
                "body": [
                    "Transaction = sekumpulan operasi SQL yang diperlakukan sebagai",
                    "SATU KESATUAN: semua berhasil (COMMIT) atau semua dibatalkan",
                    "(ROLLBACK). Tidak ada kondisi 'setengah berhasil'.",
                    "",
                    "Prinsip ACID pada transaction:",
                    "  Atomicity   -> semua-atau-tidak-sama-sekali.",
                    "  Consistency -> data selalu valid sesuai aturan/constraint.",
                    "  Isolation   -> transaction yang berjalan bersamaan tidak saling",
                    "                 mengganggu satu sama lain.",
                    "  Durability  -> setelah COMMIT, data PASTI tersimpan permanen",
                    "                 walau terjadi crash sesaat setelahnya.",
                    "",
                    "Contoh kasus wajib transaction: transfer uang antar rekening.",
                    "  Jika saldo A sudah dikurangi tapi saldo B gagal ditambah",
                    "  (misal listrik mati di tengah proses), data jadi TIDAK KONSISTEN",
                    "  tanpa transaction!",
                ]
            },
            {
                "heading": "Contoh transaction transfer saldo",
                "code": """START TRANSACTION;

UPDATE rekening SET saldo = saldo - 500000 WHERE id = 'A';
UPDATE rekening SET saldo = saldo + 500000 WHERE id = 'B';

-- Cek dulu tidak ada saldo negatif sebelum commit
-- Jika semua aman:
COMMIT;

-- Jika terjadi kesalahan/validasi gagal:
-- ROLLBACK;"""
            },
            {
                "body": [
                    "Masalah yang muncul saat banyak transaction berjalan bersamaan:",
                    "  Dirty Read      -> membaca data yang BELUM di-commit transaction lain",
                    "                     (bisa jadi nanti di-rollback, data 'palsu').",
                    "  Non-repeatable Read -> baca data yang sama 2x dalam 1 transaction,",
                    "                     hasilnya BEDA karena transaction lain sudah UPDATE.",
                    "  Phantom Read    -> query yang sama dijalankan 2x, jumlah BARIS berubah",
                    "                     karena ada INSERT/DELETE dari transaction lain.",
                    "",
                    "Isolation Level (dari paling longgar ke paling ketat):",
                    "  READ UNCOMMITTED -> bisa dirty read (paling cepat, paling berisiko).",
                    "  READ COMMITTED   -> mencegah dirty read (default di PostgreSQL).",
                    "  REPEATABLE READ  -> mencegah dirty + non-repeatable read",
                    "                      (default di MySQL/InnoDB).",
                    "  SERIALIZABLE     -> paling ketat, cegah semua masalah di atas,",
                    "                      tapi paling lambat (transaction seolah berurutan).",
                    "",
                    "  SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;",
                ]
            },
            {
                "body": [
                    "Deadlock: dua transaction saling menunggu lock yang dipegang",
                    "satu sama lain, sehingga keduanya macet selamanya.",
                    "  Transaction 1: lock baris A, mau lock baris B.",
                    "  Transaction 2: lock baris B, mau lock baris A.",
                    "  -> Database biasanya otomatis mendeteksi & membatalkan salah satu.",
                    "",
                    "Tips menghindari masalah transaction:",
                    "  1. Buat transaction sesingkat mungkin (jangan proses lama di dalamnya).",
                    "  2. Selalu kunci/akses tabel dengan URUTAN yang KONSISTEN.",
                    "  3. Tangani exception & pastikan ROLLBACK dipanggil saat error.",
                    "  4. Di aplikasi Java, gunakan @Transactional (Spring) agar otomatis",
                    "     commit/rollback berdasarkan sukses/gagalnya method.",
                ]
            },
        ],
    },
    {
        "title": "13. Roadmap Lanjutan: NoSQL, Scaling & Karir Database",
        "sections": [
            {
                "body": [
                    "Kamu sudah menguasai SQL relasional dari dasar sampai lanjutan.",
                    "Berikut gambaran topik lanjutan agar semakin handal:",
                    "",
                    "SQL vs NoSQL:",
                    "  SQL (relasional):",
                    "    - Data terstruktur ketat (skema tetap), pakai tabel.",
                    "    - Kuat di relasi data & transaction (ACID).",
                    "    - Contoh: MySQL, PostgreSQL, SQL Server, Oracle.",
                    "  NoSQL (non-relasional):",
                    "    - Skema fleksibel, cocok data semi/tidak terstruktur.",
                    "    - Jenis: Document (MongoDB), Key-Value (Redis),",
                    "      Column-family (Cassandra), Graph (Neo4j).",
                    "    - Kuat untuk skala sangat besar & data yang berubah-ubah bentuk.",
                    "",
                    "Kapan pilih SQL vs NoSQL:",
                    "  - Data punya relasi jelas & butuh transaction ketat -> SQL.",
                    "  - Data sangat besar, skema sering berubah, butuh skala",
                    "    horizontal masif -> NoSQL (atau kombinasi keduanya).",
                ]
            },
            {
                "body": [
                    "Konsep scaling database:",
                    "  Vertical scaling (scale-up)   -> tambah resource ke 1 server",
                    "                                    (CPU/RAM lebih besar).",
                    "  Horizontal scaling (scale-out) -> tambah lebih banyak server,",
                    "                                    data dipecah (sharding).",
                    "",
                    "  Replication -> menyalin data ke beberapa server (read replica)",
                    "                 untuk menyebar beban baca (read) dan sebagai backup.",
                    "  Sharding    -> memecah data besar ke beberapa database berbeda",
                    "                 berdasarkan kunci tertentu (misal per wilayah/user_id).",
                    "  Caching     -> menyimpan hasil query yang sering diakses di memori",
                    "                 (Redis/Memcached) agar tidak selalu query ke DB.",
                    "",
                    "Query Optimization checklist:",
                    "  1. Pakai EXPLAIN/EXPLAIN ANALYZE untuk lihat rencana eksekusi.",
                    "  2. Index kolom yang sering dipakai di WHERE/JOIN/ORDER BY.",
                    "  3. Hindari SELECT * pada tabel besar - ambil kolom yang perlu saja.",
                    "  4. Batasi hasil dengan LIMIT saat hanya butuh sebagian data.",
                    "  5. Hindari fungsi pada kolom di WHERE (merusak penggunaan index):",
                    "       X  WHERE YEAR(tanggal) = 2024",
                    "       V  WHERE tanggal BETWEEN '2024-01-01' AND '2024-12-31'",
                ]
            },
            {
                "body": [
                    "Peran yang berkaitan dengan database di industri:",
                    "  - Backend Developer  -> menulis query & ORM sehari-hari.",
                    "  - Database Administrator (DBA) -> kelola performa, backup, keamanan DB.",
                    "  - Data Engineer      -> membangun pipeline data skala besar (ETL).",
                    "  - Data Analyst       -> menulis query kompleks untuk analisis bisnis.",
                    "",
                    "Kebiasaan agar handal SQL:",
                    "  1. Latihan JOIN & window function tiap hari - itu yang paling",
                    "     sering dipakai & ditanyakan saat wawancara kerja.",
                    "  2. Selalu berpikir 'urutan eksekusi query' saat menulis SQL kompleks:",
                    "     FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT.",
                    "  3. Biasakan EXPLAIN setiap query yang lambat sebelum optimasi.",
                    "  4. Gabungkan dengan Java (JDBC -> Spring Data JPA) untuk jadi",
                    "     full-stack backend developer yang komplet.",
                    "  5. Pelajari studi kasus nyata: sistem e-commerce, perbankan,",
                    "     atau sistem akademik - semuanya butuh desain database yang baik.",
                ]
            },
        ],
    },
]
