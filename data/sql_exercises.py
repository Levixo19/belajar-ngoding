SQL_EXERCISES = [
    {
        "title": "Latihan 1: Buat Tabel Produk",
        "difficulty": "Mudah",
        "question": [
            "Buat tabel 'produk' dengan kolom:",
            "  id         INT primary key auto_increment",
            "  nama       VARCHAR(100) not null",
            "  kategori   VARCHAR(50)",
            "  harga      DECIMAL(10,2)",
            "  stok       INT default 0",
        ],
        "hints": [
            "CREATE TABLE produk ( ... );",
            "AUTO_INCREMENT untuk id otomatis bertambah.",
            "DECIMAL(10,2) = 10 digit dengan 2 desimal.",
        ],
        "auto_check": False,
        "alasan_tidak_dicek": "AUTO_INCREMENT khas MySQL, tidak dikenali SQLite",
        "solution": """CREATE TABLE produk (
    id        INT PRIMARY KEY AUTO_INCREMENT,
    nama      VARCHAR(100) NOT NULL,
    kategori  VARCHAR(50),
    harga     DECIMAL(10,2),
    stok      INT DEFAULT 0
);""",
    },
    {
        "title": "Latihan 2: Insert Data Produk",
        "difficulty": "Mudah",
        "question": [
            "Isi tabel produk dari latihan 1 dengan data:",
            "  (Beras 5kg, Sembako, 68000, 50)",
            "  (Minyak Goreng 1L, Sembako, 17500, 30)",
            "  (Kopi Kapal Api, Minuman, 3000, 100)",
            "  (Teh Botol, Minuman, 5000, 0)",
            "  (Sabun Cuci, Kebersihan, 12000, 20)",
        ],
        "hints": [
            "INSERT INTO produk (nama, kategori, harga, stok) VALUES ...;",
            "Boleh masukkan beberapa baris sekaligus dipisah koma.",
            "Kolom id dibiarkan otomatis terisi.",
        ],
        "setup": """CREATE TABLE produk (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nama      VARCHAR(100) NOT NULL,
    kategori  VARCHAR(50),
    harga     DECIMAL(10,2),
    stok      INT DEFAULT 0
);""",
        "verifikasi": """-- Dijalankan otomatis untuk memeriksa hasilnya
SELECT nama, kategori, harga, stok FROM produk ORDER BY id;""",
        "solution": """INSERT INTO produk (nama, kategori, harga, stok) VALUES
('Beras 5kg',      'Sembako',    68000, 50),
('Minyak Goreng 1L','Sembako',   17500, 30),
('Kopi Kapal Api',  'Minuman',    3000, 100),
('Teh Botol',       'Minuman',    5000, 0),
('Sabun Cuci',      'Kebersihan', 12000, 20);""",
    },
    {
        "title": "Latihan 3: Query Dasar",
        "difficulty": "Mudah",
        "question": [
            "Dengan tabel produk di atas, tulis query untuk:",
            "  1. Tampilkan semua produk.",
            "  2. Tampilkan nama & harga produk kategori 'Sembako'.",
            "  3. Tampilkan produk yang stok-nya 0.",
            "  4. Tampilkan produk dengan harga di atas 10000, urut dari termahal.",
        ],
        # Hint harus MENUNTUN, bukan menyalinkan jawaban. Versi lama berisi
        # empat baris query utuh, jadi yang membuka semua hint praktis sudah
        # selesai tanpa pernah menyusun satu klausa pun sendiri.
        "hints": [
            "Nomor 1 cukup menampilkan semua kolom -- ingat tanda bintang.",
            "Nomor 2 butuh dua kolom saja, plus satu penyaring kategori.",
            "Nomor 3: bandingkan kolom stok dengan angka nol memakai WHERE.",
            "Nomor 4: saring dulu harganya, baru urutkan menurun (DESC).",
        ],
        "setup": """CREATE TABLE produk (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nama      VARCHAR(100) NOT NULL,
    kategori  VARCHAR(50),
    harga     DECIMAL(10,2),
    stok      INT DEFAULT 0
);

INSERT INTO produk (nama, kategori, harga, stok) VALUES
('Beras 5kg',        'Sembako',    68000,  50),
('Minyak Goreng 1L', 'Sembako',    17500,  30),
('Kopi Kapal Api',   'Minuman',     3000, 100),
('Teh Botol',        'Minuman',     5000,   0),
('Sabun Cuci',       'Kebersihan', 12000,  20);""",
        "solution": """-- 1. Semua produk
SELECT * FROM produk;

-- 2. Sembako
SELECT nama, harga FROM produk WHERE kategori = 'Sembako';

-- 3. Stok habis
SELECT * FROM produk WHERE stok = 0;

-- 4. Harga di atas 10000 termahal dulu
SELECT * FROM produk
WHERE harga > 10000
ORDER BY harga DESC;""",
    },
    {
        "title": "Latihan 4: Update & Delete",
        "difficulty": "Mudah",
        "question": [
            "Lakukan operasi berikut:",
            "  1. Harga semua 'Minuman' naik 10%.",
            "  2. Stok 'Teh Botol' diisi 40.",
            "  3. Hapus produk 'Sabun Cuci'.",
            "  4. Tampilkan hasil akhir.",
        ],
        "hints": [
            "UPDATE produk SET harga = harga * 1.10 WHERE kategori = 'Minuman';",
            "UPDATE produk SET stok = 40 WHERE nama = 'Teh Botol';",
            "DELETE FROM produk WHERE nama = 'Sabun Cuci';",
            "Selalu pakai WHERE yang spesifik!",
        ],
        "setup": """CREATE TABLE produk (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nama      VARCHAR(100) NOT NULL,
    kategori  VARCHAR(50),
    harga     DECIMAL(10,2),
    stok      INT DEFAULT 0
);

INSERT INTO produk (nama, kategori, harga, stok) VALUES
('Beras 5kg',        'Sembako',    68000,  50),
('Minyak Goreng 1L', 'Sembako',    17500,  30),
('Kopi Kapal Api',   'Minuman',     3000, 100),
('Teh Botol',        'Minuman',     5000,   0),
('Sabun Cuci',       'Kebersihan', 12000,  20);""",
        "solution": """UPDATE produk SET harga = harga * 1.10 WHERE kategori = 'Minuman';
UPDATE produk SET stok = 40 WHERE nama = 'Teh Botol';
DELETE FROM produk WHERE nama = 'Sabun Cuci';
SELECT * FROM produk;""",
    },
    {
        "title": "Latihan 5: Agregasi & Grouping",
        "difficulty": "Menengah",
        "question": [
            "Dengan tabel produk, tulis query untuk:",
            "  1. Jumlah total produk.",
            "  2. Rata-rata harga semua produk.",
            "  3. Harga produk paling mahal.",
            "  4. Jumlah produk dan total nilai stok per kategori.",
            "     (nilai stok = harga * stok)",
            "  5. Kategori dengan total nilai stok di atas 1.000.000.",
        ],
        "hints": [
            "COUNT(*), AVG(harga), MAX(harga).",
            "GROUP BY kategori, lalu SUM(harga * stok).",
            "HAVING untuk filter agregat.",
        ],
        "setup": """CREATE TABLE produk (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nama      VARCHAR(100) NOT NULL,
    kategori  VARCHAR(50),
    harga     DECIMAL(10,2),
    stok      INT DEFAULT 0
);

INSERT INTO produk (nama, kategori, harga, stok) VALUES
('Beras 5kg',        'Sembako',    68000,  50),
('Minyak Goreng 1L', 'Sembako',    17500,  30),
('Kopi Kapal Api',   'Minuman',     3000, 100),
('Teh Botol',        'Minuman',     5000,   0),
('Sabun Cuci',       'Kebersihan', 12000,  20);""",
        "solution": """-- 1. Total produk
SELECT COUNT(*) AS total_produk FROM produk;

-- 2. Rata-rata harga
SELECT AVG(harga) AS rata_rata FROM produk;

-- 3. Harga termahal
SELECT MAX(harga) AS termahal FROM produk;

-- 4. Per kategori
SELECT kategori,
       COUNT(*) AS jumlah_produk,
       SUM(harga * stok) AS total_nilai_stok
FROM produk
GROUP BY kategori;

-- 5. Kategori dengan nilai stok > 1.000.000
SELECT kategori, SUM(harga * stok) AS total_nilai_stok
FROM produk
GROUP BY kategori
HAVING SUM(harga * stok) > 1000000;""",
    },
    {
        "title": "Latihan 6: JOIN Tiga Tabel",
        "difficulty": "Menengah",
        "question": [
            "Buat tabel berikut lalu tulis query JOIN:",
            "  kategori(id, nama)",
            "  produk(id, nama, kategori_id, harga)",
            "  penjualan(id, produk_id, jumlah)",
            "Query yang diminta:",
            "  1. Nama produk + nama kategorinya.",
            "  2. Total pendapatan per produk (jumlah * harga).",
            "  3. Produk yang tidak pernah terjual (LEFT JOIN + IS NULL).",
        ],
        "hints": [
            "produk.kategori_id REFERENCES kategori.id",
            "penjualan.produk_id REFERENCES produk.id",
            "JOIN kategori k ON p.kategori_id = k.id",
            "SUM(penjualan.jumlah * produk.harga) dengan GROUP BY.",
        ],
        "solution": """CREATE TABLE kategori (
    id INT PRIMARY KEY,
    nama VARCHAR(50)
);

CREATE TABLE produk (
    id INT PRIMARY KEY,
    nama VARCHAR(50),
    kategori_id INT,
    harga DECIMAL(10,2),
    FOREIGN KEY (kategori_id) REFERENCES kategori(id)
);

CREATE TABLE penjualan (
    id INT PRIMARY KEY,
    produk_id INT,
    jumlah INT,
    FOREIGN KEY (produk_id) REFERENCES produk(id)
);

INSERT INTO kategori VALUES (1, 'Elektronik'), (2, 'Alat Tulis');
INSERT INTO produk VALUES
(1, 'Laptop', 1, 7500000),
(2, 'Mouse', 1, 150000),
(3, 'Buku', 2, 25000);
INSERT INTO penjualan VALUES
(1, 1, 3),
(2, 2, 10),
(3, 2, 5);

-- 1. Produk + kategori
SELECT p.nama AS produk, k.nama AS kategori
FROM produk p
JOIN kategori k ON p.kategori_id = k.id;

-- 2. Pendapatan per produk
SELECT p.nama, SUM(pn.jumlah * p.harga) AS pendapatan
FROM produk p
JOIN penjualan pn ON p.id = pn.produk_id
GROUP BY p.nama;

-- 3. Produk tidak pernah terjual
SELECT p.nama
FROM produk p
LEFT JOIN penjualan pn ON p.id = pn.produk_id
WHERE pn.id IS NULL;""",
    },
    {
        "title": "Latihan 7: Subquery",
        "difficulty": "Menengah",
        "question": [
            "Dengan tabel mahasiswa(nim, nama, jurusan, ipk), tulis query:",
            "  1. Mahasiswa dengan IPK di atas rata-rata.",
            "  2. Jurusan yang punya mahasiswa dengan IPK di atas 3.5.",
            "  3. Mahasiswa dengan IPK tertinggi di setiap jurusan.",
        ],
        "hints": [
            "WHERE ipk > (SELECT AVG(ipk) FROM mahasiswa)",
            "WHERE jurusan IN (SELECT jurusan FROM mahasiswa WHERE ipk > 3.5)",
            "Untuk nomor 3: bandingkan ipk dengan MAX(ipk) per jurusan, atau gunakan subquery berkorelasi.",
        ],
        "setup": """CREATE TABLE mahasiswa (
    nim     INT PRIMARY KEY,
    nama    VARCHAR(50),
    jurusan VARCHAR(50),
    ipk     DECIMAL(3,2)
);

INSERT INTO mahasiswa VALUES
(101, 'Andi',  'Informatika',      3.75),
(102, 'Budi',  'Informatika',      3.20),
(103, 'Citra', 'Sistem Informasi', 3.90),
(104, 'Dedi',  'Sistem Informasi', 3.10),
(105, 'Eka',   'Informatika',      3.55);""",
        "solution": """-- 1. IPK di atas rata-rata
SELECT * FROM mahasiswa
WHERE ipk > (SELECT AVG(ipk) FROM mahasiswa);

-- 2. Jurusan dengan mahasiswa ber-IPK > 3.5
SELECT DISTINCT jurusan
FROM mahasiswa
WHERE jurusan IN (SELECT jurusan FROM mahasiswa WHERE ipk > 3.5);

-- 3. IPK tertinggi tiap jurusan (subquery berkorelasi)
SELECT m.nama, m.jurusan, m.ipk
FROM mahasiswa m
WHERE m.ipk = (
    SELECT MAX(ipk) FROM mahasiswa
    WHERE jurusan = m.jurusan
)
ORDER BY m.jurusan;""",
    },
    {
        "title": "Latihan 8: Query Gabungan (Challenging)",
        "difficulty": "Lanjut",
        "question": [
            "Database toko. Buat query yang menampilkan:",
            "  10 produk terlaris berdasarkan jumlah terjual,",
            "  lengkap dengan nama produk, kategori, total terjual,",
            "  dan total pendapatan, hanya untuk produk yang",
            "  pendapatannya di atas 500.000.",
            "Urutkan dari pendapatan tertinggi.",
        ],
        "hints": [
            "Gabungan: JOIN penjualan & kategori, GROUP BY produk, SUM.",
            "Filter agregat dengan HAVING.",
            "LIMIT 10 di akhir.",
        ],
        "setup": """CREATE TABLE kategori (
    id   INT PRIMARY KEY,
    nama VARCHAR(50)
);

CREATE TABLE produk (
    id          INT PRIMARY KEY,
    nama        VARCHAR(50),
    kategori_id INT,
    harga       DECIMAL(10,2)
);

CREATE TABLE penjualan (
    id        INT PRIMARY KEY,
    produk_id INT,
    jumlah    INT
);

INSERT INTO kategori VALUES (1, 'Elektronik'), (2, 'Alat Tulis');
INSERT INTO produk VALUES
(1, 'Laptop', 1, 7500000),
(2, 'Mouse',  1,  150000),
(3, 'Buku',   2,   25000);
INSERT INTO penjualan VALUES (1, 1, 3), (2, 2, 10);""",
        "solution": """SELECT p.nama AS produk,
       k.nama AS kategori,
       SUM(pn.jumlah) AS total_terjual,
       SUM(pn.jumlah * p.harga) AS total_pendapatan
FROM produk p
JOIN penjualan pn ON p.id = pn.produk_id
JOIN kategori k ON p.kategori_id = k.id
GROUP BY p.id, p.nama, k.nama
HAVING SUM(pn.jumlah * p.harga) > 500000
ORDER BY total_pendapatan DESC
LIMIT 10;""",
    },
    {
        "title": "Latihan 9: Ranking dengan Window Function",
        "difficulty": "Sulit",
        "question": [
            "Dengan tabel mahasiswa(nim, nama, jurusan, ipk), tulis query:",
            "  1. Tampilkan peringkat (RANK) IPK tiap mahasiswa DI DALAM",
            "     jurusannya masing-masing (peringkat 1 = IPK tertinggi).",
            "  2. Ambil HANYA mahasiswa dengan peringkat 1-2 di tiap jurusan.",
            "  3. Tampilkan juga selisih IPK dengan mahasiswa peringkat",
            "     tepat di atasnya (gunakan LAG).",
        ],
        "hints": [
            "RANK() OVER (PARTITION BY jurusan ORDER BY ipk DESC)",
            "Window function tidak bisa langsung di WHERE, bungkus dengan subquery.",
            "LAG(ipk) OVER (PARTITION BY jurusan ORDER BY ipk DESC) untuk baris sebelumnya.",
        ],
        "setup": """CREATE TABLE mahasiswa (
    nim     INT PRIMARY KEY,
    nama    VARCHAR(50),
    jurusan VARCHAR(50),
    ipk     DECIMAL(3,2)
);

INSERT INTO mahasiswa VALUES
(101, 'Andi',  'Informatika',      3.75),
(102, 'Budi',  'Informatika',      3.20),
(103, 'Citra', 'Sistem Informasi', 3.90),
(104, 'Dedi',  'Sistem Informasi', 3.10),
(105, 'Eka',   'Informatika',      3.55);""",
        "solution": """-- 1 & 3: peringkat + selisih dengan peringkat di atasnya
SELECT
    nama, jurusan, ipk,
    RANK() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS peringkat,
    ipk - LAG(ipk) OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS selisih_ke_atas
FROM mahasiswa;

-- 2: hanya peringkat 1-2 per jurusan (bungkus dengan subquery)
SELECT * FROM (
    SELECT
        nama, jurusan, ipk,
        RANK() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS peringkat
    FROM mahasiswa
) hasil
WHERE peringkat <= 2
ORDER BY jurusan, peringkat;""",
    },
    {
        "title": "Latihan 10: Hierarki Kategori dengan Recursive CTE",
        "difficulty": "Sulit",
        "question": [
            "Buat tabel kategori(id, nama, parent_id) untuk struktur",
            "kategori bertingkat (kategori > sub-kategori > sub-sub-kategori).",
            "Isi beberapa data contoh (Elektronik > Komputer > Laptop, dst).",
            "Tulis recursive CTE untuk menampilkan SEMUA sub-kategori dari",
            "kategori 'Elektronik' beserta level kedalamannya.",
        ],
        "hints": [
            "parent_id merujuk ke id kategori induknya sendiri (self-reference).",
            "Anchor: SELECT kategori dengan nama = 'Elektronik', level = 1.",
            "Recursive: JOIN kategori dengan hasil CTE dimana parent_id = id CTE, level+1.",
        ],
        "solution": """CREATE TABLE kategori (
    id INT PRIMARY KEY,
    nama VARCHAR(50),
    parent_id INT
);

INSERT INTO kategori VALUES
(1, 'Elektronik', NULL),
(2, 'Komputer', 1),
(3, 'Laptop', 2),
(4, 'PC Desktop', 2),
(5, 'Handphone', 1),
(6, 'Aksesoris', 5);

WITH RECURSIVE sub_kategori AS (
    SELECT id, nama, parent_id, 1 AS level
    FROM kategori
    WHERE nama = 'Elektronik'

    UNION ALL

    SELECT k.id, k.nama, k.parent_id, s.level + 1
    FROM kategori k
    JOIN sub_kategori s ON k.parent_id = s.id
)
SELECT * FROM sub_kategori ORDER BY level, nama;""",
    },
    {
        "title": "Latihan 11: View & Trigger untuk Sistem Nilai",
        "difficulty": "Sulit",
        "question": [
            "Dengan tabel mahasiswa(nim, nama, ipk):",
            "  1. Buat VIEW 'mahasiswa_cumlaude' yang menampilkan mahasiswa",
            "     dengan ipk >= 3.7.",
            "  2. Buat tabel log_perubahan_ipk(nim, ipk_lama, ipk_baru, waktu).",
            "  3. Buat TRIGGER yang otomatis mencatat ke tabel log setiap",
            "     kali kolom ipk di tabel mahasiswa di-UPDATE.",
        ],
        "hints": [
            "CREATE VIEW nama AS SELECT ... WHERE ipk >= 3.7;",
            "TRIGGER AFTER UPDATE ON mahasiswa FOR EACH ROW ...",
            "Gunakan OLD.ipk untuk nilai sebelum, NEW.ipk untuk nilai sesudah.",
        ],
        "auto_check": False,
        "alasan_tidak_dicek": "DELIMITER dan sintaks TRIGGER MySQL tidak ada di SQLite",
        "solution": """-- 1. View mahasiswa cumlaude
CREATE VIEW mahasiswa_cumlaude AS
SELECT nim, nama, ipk FROM mahasiswa WHERE ipk >= 3.7;

-- 2. Tabel log
CREATE TABLE log_perubahan_ipk (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nim INT,
    ipk_lama DECIMAL(3,2),
    ipk_baru DECIMAL(3,2),
    waktu DATETIME
);

-- 3. Trigger pencatat perubahan ipk
DELIMITER //

CREATE TRIGGER log_update_ipk
AFTER UPDATE ON mahasiswa
FOR EACH ROW
BEGIN
    IF OLD.ipk <> NEW.ipk THEN
        INSERT INTO log_perubahan_ipk (nim, ipk_lama, ipk_baru, waktu)
        VALUES (NEW.nim, OLD.ipk, NEW.ipk, NOW());
    END IF;
END //

DELIMITER ;""",
    },
    {
        "title": "Latihan 12: Transaction Transfer Saldo yang Aman",
        "difficulty": "Sulit",
        "question": [
            "Dengan tabel rekening(id, nama, saldo), buat transaction untuk",
            "mentransfer 500000 dari rekening 'A' ke rekening 'B' dengan aturan:",
            "  1. Gunakan START TRANSACTION.",
            "  2. Kurangi saldo A, tambah saldo B.",
            "  3. Jika setelah dikurangi saldo A menjadi NEGATIF, batalkan",
            "     seluruh transaction dengan ROLLBACK.",
            "  4. Jika aman, COMMIT.",
            "  (Tulis sebagai pseudo-SQL step-by-step, karena pengecekan",
            "  kondisional murni butuh stored procedure di kebanyakan DB).",
        ],
        "hints": [
            "START TRANSACTION; lalu 2 UPDATE.",
            "SELECT saldo dari A setelah UPDATE untuk verifikasi >= 0.",
            "Jika saldo < 0 -> ROLLBACK; jika tidak -> COMMIT;",
        ],
        "auto_check": False,
        "alasan_tidak_dicek": "START TRANSACTION khas MySQL; SQLite memakai BEGIN",
        "solution": """START TRANSACTION;

UPDATE rekening SET saldo = saldo - 500000 WHERE id = 'A';
UPDATE rekening SET saldo = saldo + 500000 WHERE id = 'B';

-- Verifikasi saldo A tidak negatif
SELECT saldo FROM rekening WHERE id = 'A';

-- Jika hasil SELECT di atas menunjukkan saldo < 0:
ROLLBACK;
-- Jika saldo aman (>= 0):
-- COMMIT;

-- Catatan: di aplikasi nyata (Java/Spring), pengecekan ini dilakukan
-- di kode aplikasi sebelum memanggil commit(), atau memakai
-- stored procedure dengan IF/THEN untuk keputusan otomatis di DB."""
    },
    {
        'title': 'Proyek Akhir: Analisis Penjualan Toko Bahan Kue',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Analisis Penjualan Toko Bahan Kue',
        '',
        'Toko bahan kue punya tiga tabel dan nol laporan. Pemiliknya menebak-',
        'nebak siapa pelanggan terbaiknya dan barang mana yang mati.',
        '',
        'Satu berkas SQL harus membangun skemanya, mengisinya, lalu menjawab',
        'empat pertanyaan. Yang diuji bukan menulis SELECT sederhana melainkan',
        'menyusun jawaban dari beberapa tabel sekaligus.',
        '',
        'Skema: pelanggan(id, nama, kota), produk(id, nama, kategori, harga),',
        'pesanan(id, pelanggan_id, produk_id, jumlah, tanggal).',
        'Data: 4 pelanggan, 7 produk, 9 pesanan (dua produk tak pernah dipesan).',
        '',
        'Yang harus ada di programmu:',
        '  1. CREATE TABLE dengan PRIMARY KEY, NOT NULL, CHECK, dan REFERENCES.',
        '  2. Pertanyaan 1: total belanja per pelanggan (JOIN tiga tabel +',
        '     GROUP BY), urut dari terbesar.',
        '  3. Pertanyaan 2: produk terlaris PER KATEGORI. Pakai CTE + window',
        '     function RANK() OVER (PARTITION BY ... ORDER BY ...).',
        '  4. Pertanyaan 3: kota yang totalnya di atas rata-rata seluruh kota.',
        '     Rata-ratanya dihitung dari hasil agregat, jadi butuh CTE juga.',
        '  5. Pertanyaan 4: produk yang TIDAK pernah dipesan -- LEFT JOIN lalu',
        '     WHERE ... IS NULL, bukan NOT IN.',
        '  6. Tiap pengurutan wajib punya pemutus seri, supaya hasilnya tidak',
        '     berubah-ubah. Judul bagian dicetak dengan .print.',
        '  7. Awali keluaran dengan .headers on dan .mode column.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  ',
        '  == 1. Belanja per pelanggan (terbesar dulu) ==',
        '  pelanggan      kota     transaksi  total ',
        '  -------------  -------  ---------  ------',
        '  Toko Melati    Bandung  3          358000',
        '  Roti Anggrek   Bandung  2          356000',
        '  Warung Bu Sri  Bandung  2          312000',
        '  Kue Pak Dedi   Cimahi   2          144000',
        '  ',
        '  == 2. Produk terlaris per kategori ==',
        '  kategori      nama           unit',
        '  ------------  -------------  ----',
        '  Bahan Basah   Telur          8   ',
        '  Bahan Kering  Tepung Terigu  21  ',
        '  ',
        '  == 3. Kota yang belanjanya di atas rata-rata ==',
        '  kota     total  ',
        '  -------  -------',
        '  Bandung  1026000',
        '  ',
        '  == 4. Produk yang tidak pernah dipesan ==',
        '  nama          kategori    ',
        '  ------------  ------------',
        '  Susu Cair     Bahan Basah ',
        '  Vanili Bubuk  Bahan Kering',
    ],
        'hints': [
        'Window function butuh CTE kalau kamu mau MENYARING hasilnya: RANK() tidak bisa dipakai di WHERE pada kueri yang sama.',
        'Anti-join: SELECT ... FROM produk pr LEFT JOIN pesanan ps ON ps.produk_id = pr.id WHERE ps.id IS NULL.',
        'Rata-rata dari agregat: WITH per_kota AS (SELECT ... GROUP BY kota) SELECT * FROM per_kota WHERE total > (SELECT AVG(total) FROM per_kota)',
    ],
        'solution': """-- Analisis Penjualan Toko Bahan Kue -- dari tabel mentah jadi tiga keputusan.

CREATE TABLE pelanggan (
  id     INTEGER PRIMARY KEY,
  nama   TEXT NOT NULL,
  kota   TEXT NOT NULL
);

CREATE TABLE produk (
  id       INTEGER PRIMARY KEY,
  nama     TEXT NOT NULL,
  kategori TEXT NOT NULL,
  harga    INTEGER NOT NULL CHECK (harga > 0)
);

CREATE TABLE pesanan (
  id          INTEGER PRIMARY KEY,
  pelanggan_id INTEGER NOT NULL REFERENCES pelanggan(id),
  produk_id    INTEGER NOT NULL REFERENCES produk(id),
  jumlah       INTEGER NOT NULL CHECK (jumlah > 0),
  tanggal      TEXT NOT NULL
);

INSERT INTO pelanggan (id, nama, kota) VALUES
  (1, 'Toko Melati',  'Bandung'),
  (2, 'Warung Bu Sri','Bandung'),
  (3, 'Kue Pak Dedi', 'Cimahi'),
  (4, 'Roti Anggrek', 'Bandung');

INSERT INTO produk (id, nama, kategori, harga) VALUES
  (1, 'Tepung Terigu', 'Bahan Kering', 12000),
  (2, 'Gula Pasir',    'Bahan Kering',  15000),
  (3, 'Mentega',       'Bahan Basah',   28000),
  (4, 'Cokelat Bubuk', 'Bahan Kering',  42000),
  (5, 'Telur',         'Bahan Basah',   30000),
  (6, 'Vanili Bubuk',  'Bahan Kering',   9000),
  (7, 'Susu Cair',     'Bahan Basah',   18000);

INSERT INTO pesanan (id, pelanggan_id, produk_id, jumlah, tanggal) VALUES
  (1, 1, 1, 10, '2026-01-05'),
  (2, 1, 3,  4, '2026-01-05'),
  (3, 2, 1,  6, '2026-01-06'),
  (4, 3, 4,  2, '2026-01-06'),
  (5, 1, 4,  3, '2026-01-08'),
  (6, 2, 5,  8, '2026-01-09'),
  (7, 4, 2, 20, '2026-01-09'),
  (8, 3, 1,  5, '2026-01-10'),
  (9, 4, 3,  2, '2026-01-11');

.headers on
.mode column

.print ''
.print '== 1. Belanja per pelanggan (terbesar dulu) =='
SELECT
  pl.nama                          AS pelanggan,
  pl.kota,
  COUNT(*)                         AS transaksi,
  SUM(ps.jumlah * pr.harga)        AS total
FROM pesanan ps
JOIN pelanggan pl ON pl.id = ps.pelanggan_id
JOIN produk    pr ON pr.id = ps.produk_id
GROUP BY pl.id
ORDER BY total DESC, pelanggan;

.print ''
.print '== 2. Produk terlaris per kategori =='
WITH laku AS (
  SELECT pr.kategori,
         pr.nama,
         SUM(ps.jumlah) AS unit,
         RANK() OVER (PARTITION BY pr.kategori
                      ORDER BY SUM(ps.jumlah) DESC, pr.nama) AS peringkat
  FROM pesanan ps
  JOIN produk pr ON pr.id = ps.produk_id
  GROUP BY pr.id
)
SELECT kategori, nama, unit FROM laku WHERE peringkat = 1 ORDER BY kategori;

.print ''
.print '== 3. Kota yang belanjanya di atas rata-rata =='
WITH per_kota AS (
  SELECT pl.kota, SUM(ps.jumlah * pr.harga) AS total
  FROM pesanan ps
  JOIN pelanggan pl ON pl.id = ps.pelanggan_id
  JOIN produk    pr ON pr.id = ps.produk_id
  GROUP BY pl.kota
)
SELECT kota, total FROM per_kota
WHERE total > (SELECT AVG(total) FROM per_kota)
ORDER BY total DESC;

.print ''
.print '== 4. Produk yang tidak pernah dipesan =='
SELECT pr.nama, pr.kategori
FROM produk pr
LEFT JOIN pesanan ps ON ps.produk_id = pr.id
WHERE ps.id IS NULL
ORDER BY pr.nama;
""",
    },
]
