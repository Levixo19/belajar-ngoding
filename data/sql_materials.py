SQL_MATERIALS = [
    {
        "title": "1. Pengenalan Database & SQL",
        "sections": [
            {
                "body": [
                    "Database itu tempat menyimpan data secara terstruktur, artinya rapi dan",
                    "punya aturan. Datanya disimpan dalam tabel yang terdiri dari baris dan",
                    "kolom, mirip lembar Excel.",
                    "",
                    "SQL singkatan dari Structured Query Language. Ini bahasa untuk mengelola",
                    "data di database relasional, yaitu database yang menyimpan datanya dalam",
                    "tabel. SQL punya standar internasional, dan hampir semua database",
                    "memakainya.",
                    "",
                    "Standarnya memang satu, tapi tiap database menambah dan mengurangi",
                    "sendiri. Jadi SQL itu satu bahasa dengan banyak logat. Makanya query,",
                    "yaitu perintah yang kamu kirim ke database, yang disalin dari",
                    "StackOverflow kadang gagal tanpa sebab yang kelihatan. Biasanya orang",
                    "yang menulisnya pakai database lain. Cara mengenali logat sebuah berkas",
                    "dibahas di materi Membuka Database & Berkas SQL Orang Lain.",
                    "",
                    "Di kursus ini, contoh di materi ditulis dengan gaya MySQL. Latihannya",
                    "dijalankan aplikasi ini pakai sqlite3. Jadi kalau ejaan di bagian",
                    "\"KONDISI AWAL\" sebuah latihan kadang beda dari materi, itu bukan salah",
                    "ketik. Logatnya memang beda.",
                    "",
                    "Perintah SQL dikelompokkan jadi empat jenis menurut tugasnya:",
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
                    "  - MySQL / MariaDB, paling populer untuk pemula.",
                    "  - PostgreSQL, fiturnya lengkap dan gratis.",
                    "  - SQL Server, buatan Microsoft.",
                    "  - Oracle, banyak dipakai perusahaan besar (enterprise).",
                    "  - SQLite, cuma satu berkas kecil, cocok untuk aplikasi lokal.",
                    "",
                    "Isi database tersusun bertingkat begini:",
                    "  Database -> Tabel -> Kolom & Baris -> Sel",
                    "",
                    "Satu database berisi beberapa tabel. Tiap tabel punya kolom (jenis",
                    "datanya) dan baris (satu data utuh). Pertemuan satu baris dan satu kolom",
                    "disebut sel. Contohnya tabel mahasiswa:",
                    "  nim   | nama  | jurusan     | ipk",
                    "  ------+-------+-------------+-----",
                    "  101   | Andi  | Informatika | 3.5",
                    "  102   | Budi  | Sistem Info | 3.2",
                ]
            },
            {
                "body": [
                    "Di MySQL, database baru dibikin pakai CREATE DATABASE, lalu dipilih",
                    "pakai USE supaya perintah berikutnya bekerja di situ:",
                    "  CREATE DATABASE belajar_db;",
                    "  USE belajar_db;",
                    "",
                    "Untuk menjalankan perintah lewat terminal di MySQL, masuk dulu pakai",
                    "perintah ini, lalu ketik perintah SQL-mu dan akhiri dengan titik koma",
                    "(;):",
                    "  mysql -u root -p",
                    "",
                    "Cara menulis SQL yang perlu kamu tahu:",
                    "  1. Kata kunci SQL nggak peka huruf besar-kecil: SELECT, select, dan",
                    "     Select sama aja. Tapi kebiasaannya kata kunci ditulis huruf besar",
                    "     semua, supaya gampang dibedakan dari nama tabel dan kolom.",
                    "  2. Setiap perintah (statement) diakhiri titik koma (;).",
                    "  3. Komentar satu baris diawali dua tanda hubung (--).",
                    "  4. Komentar beberapa baris dibungkus /* dan */.",
                    "  5. Nama tabel dan kolom biasanya huruf kecil, dan kalau lebih dari",
                    "     satu kata disambung garis bawah (snake_case), misalnya",
                    "     tanggal_lahir.",
                    "",
                    "Contoh komentar:",
                    "  -- ini komentar",
                    "  SELECT * FROM mahasiswa;  -- ambil semua data",
                    "",
                    "Komentar dilewati database, jadi isinya bebas. Pakai untuk menjelaskan",
                    "maksud query-mu.",
                ]
            },
        ],
    },
    {
        "title": "2. DDL: Membuat Struktur Tabel",
        "sections": [
            {
                "body": [
                    "DDL (Data Definition Language) adalah kelompok perintah untuk membuat",
                    "dan mengubah struktur database: tabelnya, kolomnya, dan aturannya.",
                    "Datanya sendiri belum disentuh di sini.",
                    "",
                    "Tabel dibikin pakai CREATE TABLE. Bentuk umumnya begini (bagian dalam",
                    "kurung siku boleh ditulis, boleh nggak):",
                    "  CREATE TABLE nama_tabel (",
                    "      kolom1 tipe_data [batasan],",
                    "      kolom2 tipe_data [batasan],",
                    "      ...",
                    "  );",
                    "",
                    "Tiap kolom wajib punya tipe data, yaitu jenis nilai yang boleh disimpan",
                    "di kolom itu. Tipe data yang umum di MySQL:",
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
                    "Selain tipe data, kolom bisa dikasih batasan (constraint). Batasan itu",
                    "aturan yang dijaga database: data yang melanggar langsung ditolak.",
                    "  PRIMARY KEY      -> kunci utama, unik & tidak boleh null.",
                    "  FOREIGN KEY      -> menghubungkan ke tabel lain.",
                    "  NOT NULL         -> wajib diisi.",
                    "  UNIQUE           -> tidak boleh duplikat.",
                    "  DEFAULT nilai    -> nilai awal jika tidak diisi.",
                    "  AUTO_INCREMENT   -> otomatis bertambah (untuk angka).",
                    "  CHECK            -> validasi (MySQL 8.0.16+).",
                    "",
                    "NULL artinya \"nggak ada isinya\", beda dengan angka 0 atau teks kosong.",
                    "",
                    "Contoh tabel yang memakai FOREIGN KEY. Kolom nim dan kode di tabel nilai",
                    "harus menunjuk data yang memang ada di tabel mahasiswa dan mata_kuliah:",
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
        "title": "3. Tipe Data, Constraint & Kunci Gabungan",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya kamu bikin tabel pertama pakai 8 tipe data dan 7",
                    "constraint. Skema di proyek nyata pakai jauh lebih banyak. Tiap pilihan",
                    "punya akibat, dan akibatnya sering baru kerasa setahun kemudian.",
                    "",
                    "Tipe data itu janji ke database. Isinya tiga hal:",
                    "  - berapa byte yang disediakan untuk kolom itu di tiap baris,",
                    "  - nilai apa yang boleh masuk (yang lain langsung ditolak),",
                    "  - bagaimana nilainya dibandingkan dan diurutkan.",
                    "",
                    "Bilangan bulat",
                    "",
                    "Tipe bilangan bulat bedanya di ukuran, yaitu seberapa besar angka yang",
                    "muat:",
                    "  TINYINT    1 byte   -128 .. 127        (0 .. 255 kalau UNSIGNED)",
                    "  SMALLINT   2 byte   -32.768 .. 32.767",
                    "  MEDIUMINT  3 byte   -8,3 juta .. 8,3 juta      (MySQL saja)",
                    "  INT        4 byte   -2.147.483.648 .. 2.147.483.647",
                    "  BIGINT     8 byte   +/- 9.223.372.036.854.775.807",
                    "",
                    "Kolom id wajib pakai BIGINT kalau barisnya bisa lewat 2,1 miliar.",
                    "Contohnya tabel log, event, notifikasi, dan transaksi. Ada dua hal yang",
                    "bikin batas itu cepat kesampaian:",
                    "  1. Nomor yang udah kepakai nggak didaur ulang. Baris yang dihapus",
                    "     tetap menghabiskan nomornya. Jadi yang dihitung adalah jumlah baris",
                    "     yang pernah ada, termasuk yang udah dihapus.",
                    "  2. Begitu id INT habis, INSERT berikutnya gagal total, nggak sekadar",
                    "     melambat. Mengubah INT jadi BIGINT di tabel 500 juta baris artinya",
                    "     tabelnya ditulis ulang. Itu makan waktu berjam-jam, dan selama itu",
                    "     tabelnya terkunci.",
                    "",
                    "Patokannya gampang: id pakai BIGINT, sedangkan umur atau jumlah stok",
                    "cukup INT atau yang lebih kecil.",
                    "",
                    "UNSIGNED (cuma ada di MySQL) memindahkan jatah angka negatif ke sisi",
                    "positif. INT UNSIGNED isinya 0 sampai 4.294.967.295. PostgreSQL nggak",
                    "punya UNSIGNED.",
                    "",
                    "Teks",
                    "",
                    "Ada tiga bentuk yang sering dikira sama:",
                    "  CHAR(n)     panjang tetap n; isi yang lebih pendek dipadatkan spasi.",
                    "  VARCHAR(n)  panjangnya ikut isinya, maksimal n karakter.",
                    "  TEXT        teks panjang; di MySQL disimpan terpisah dari barisnya.",
                    "",
                    "Pakai CHAR cuma kalau panjangnya memang selalu sama, misalnya kode",
                    "negara 'ID' atau hash yang panjangnya pasti. Cara tiap database",
                    "memperlakukan spasi di ujung CHAR juga beda-beda. Itu aja udah cukup",
                    "jadi alasan untuk pilih VARCHAR.",
                    "",
                    "Angka n di VARCHAR(n) itu batas, bukan saran. Data yang lebih panjang",
                    "ditolak dengan pesan 'Data too long for column'. Di MySQL lama yang",
                    "masih pakai mode longgar, data itu malah dipotong tanpa pesan error apa",
                    "pun. Alamat pelanggan bisa hilang separuh dan nggak ada yang tahu.",
                    "",
                    "Di PostgreSQL, VARCHAR dan TEXT sama cepatnya. Di MySQL, kolom TEXT",
                    "nggak bisa di-index penuh. Index itu semacam daftar isi yang bikin",
                    "pencarian cepat, dan untuk TEXT yang bisa di-index cuma awalannya,",
                    "misalnya INDEX (isi(100)). Jadi jangan pakai TEXT untuk kolom yang",
                    "sering dicari.",
                    "",
                    "Uang",
                    "",
                    "Untuk uang, jangan pernah pakai FLOAT atau DOUBLE. Pakai DECIMAL(p,s).",
                    "Huruf p artinya jumlah seluruh digit, dan s artinya jumlah digit di",
                    "belakang koma. DECIMAL(10,2) menampung sampai 99.999.999,99 dan",
                    "menyimpannya persis.",
                    "",
                    "FLOAT dan DOUBLE nyimpen angka sebagai pendekatan dalam bentuk biner,",
                    "jadi angkanya hampir benar tapi nggak persis. Buktinya ada di contoh",
                    "berikut.",
                ],
            },
            {
                "heading": "Bukti: uang di kolom FLOAT bocor",
                "code": """-- Dua cara menyimpan harga: yang salah dan yang aman.
CREATE TABLE keranjang (
    id          INTEGER PRIMARY KEY,
    barang      TEXT    NOT NULL,
    harga_float REAL,      -- SALAH untuk uang: pendekatan biner
    harga_sen   INTEGER    -- aman: simpan dalam satuan terkecil (sen)
);

INSERT INTO keranjang (barang, harga_float, harga_sen) VALUES
    ('permen', 0.1, 10),
    ('korek',  0.2, 20);

SELECT 'total float   : ' || SUM(harga_float)         FROM keranjang;
SELECT 'sama dgn 0.3? : ' || (SUM(harga_float) = 0.3) FROM keranjang;
SELECT 'selisihnya    : ' || (SUM(harga_float) - 0.3) FROM keranjang;
SELECT 'total sen     : ' || SUM(harga_sen) || ' sen' FROM keranjang;

-- Kebocoran yang sama lewat pintu lain: mengubah rupiah ke sen dikali 100.
SELECT '19.99 * 100 lalu dibulatkan ke bawah: ' || CAST(19.99 * 100 AS INTEGER);

-- Yang tercetak:
--   total float   : 0.3          <- KELIHATAN benar
--   sama dgn 0.3? : 0            <- ternyata tidak sama (0 = false)
--   selisihnya    : 5.55111512312578e-17
--   total sen     : 30 sen
--   19.99 * 100 lalu dibulatkan ke bawah: 1998    <- satu sen menguap
--
-- Di MySQL/PostgreSQL, DECIMAL(10,2) menyimpan angkanya persis dan bebas dari
-- masalah ini. SQLite TIDAK punya DECIMAL sejati - kata DECIMAL diterima tapi
-- isinya tetap disimpan sebagai float, jadi di SQLite pilihannya memang
-- menyimpan sen sebagai INTEGER.""",
            },
            {
                "body": [
                    "Waktu",
                    "",
                    "Ada lima tipe untuk waktu. Bedanya ada di isi dan perilakunya, nggak",
                    "cuma di cara nulisnya:",
                    "  DATE       2026-09-06           tanggal saja, tanpa jam.",
                    "  TIME       14:30:00             jam saja; di MySQL boleh melebihi",
                    "                                  24 jam karena juga dipakai untuk",
                    "                                  durasi, bukan cuma jam dinding.",
                    "  DATETIME   2026-09-06 14:30:00  tanggal + jam, disimpan apa adanya.",
                    "  TIMESTAMP  terlihat sama persis, tapi sadar zona waktu.",
                    "  YEAR       2026                 tahun 4 digit, MySQL saja.",
                    "",
                    "YEAR adalah tipe kolom angkatan di tabel mahasiswa pada materi SELECT.",
                    "Di sana tipe ini dipakai tanpa pernah dijelaskan. PostgreSQL dan SQLite",
                    "nggak punya tipe ini, jadi pakai SMALLINT.",
                    "",
                    "Di MySQL, DATETIME dan TIMESTAMP kelihatan sama, tapi salah pilih bisa",
                    "bikin repot:",
                    "  - DATETIME disimpan persis seperti yang kamu tulis. Kalau zona waktu",
                    "    server berubah, nilainya tetap. Rentangnya sampai tahun 9999.",
                    "  - TIMESTAMP diubah ke UTC waktu disimpan, lalu dikembalikan ke zona",
                    "    waktu sesi waktu dibaca. Dua orang di zona waktu berbeda melihat jam",
                    "    yang berbeda dari baris yang sama. Itu memang fitur, bukan bug.",
                    "",
                    "Jebakan: rentang TIMESTAMP berhenti di 19 Januari 2038.",
                    "",
                    "Padanannya di PostgreSQL: TIMESTAMPTZ (sadar zona waktu) dan TIMESTAMP",
                    "(nggak sadar zona waktu). Aturan praktisnya: simpan dalam UTC, lalu ubah",
                    "ke waktu lokal waktu ditampilkan.",
                    "",
                    "Tipe yang sering ketemu di skema modern",
                    "  - BOOLEAN. Di MySQL ini cuma nama lain TINYINT(1): TRUE dan FALSE",
                    "    disimpan sebagai 1 dan 0, dan SELECT juga mengembalikan 1 atau 0.",
                    "    PostgreSQL punya boolean asli (t/f). SQLite nggak punya sama sekali,",
                    "    jadi simpan 0 atau 1.",
                    "  - BLOB, untuk data biner mentah seperti gambar atau PDF. Kebanyakan",
                    "    sistem cuma nyimpen path atau URL berkasnya. BLOB bikin backup",
                    "    membengkak dan tiap SELECT * jadi berat.",
                    "  - ENUM, daftar pilihan yang boleh diisi. Di MySQL: status",
                    "    ENUM('draft','terbit','arsip'). Nilai di luar daftar ditolak.",
                    "    Kekurangannya, menambah satu pilihan berarti ALTER TABLE di tabel",
                    "    produksi. Karena itu banyak tim memilih VARCHAR ditambah CHECK.",
                    "    PostgreSQL pakai CREATE TYPE ... AS ENUM.",
                    "  - JSON, satu kolom yang isinya dokumen utuh. PostgreSQL punya dua",
                    "    tipe: JSON (teks apa adanya) dan JSONB (biner, bisa di-index).",
                    "    Hampir selalu pilih JSONB. Ada dua operator yang wajib bisa kamu",
                    "    baca:",
                    "      data -> 'alamat'   hasilnya JSON, masih bisa ditelusuri",
                    "      data ->> 'kota'    hasilnya TEXT, baru bisa dibandingkan",
                    "      data -> 'alamat' ->> 'kota' = 'Bandung'",
                    "    Panah tunggal hasilnya tetap JSON, panah ganda hasilnya teks. Kalau",
                    "    salah pilih, perbandingannya nggak pernah cocok. MySQL pakai JSON",
                    "    path: data->'$.kota' dan data->>'$.kota'. Ingat juga, kolom biasa",
                    "    lebih cepat dan bisa dijaga constraint. Taruh di JSON cuma data yang",
                    "    bentuknya memang nggak tetap.",
                    "  - UUID, id acak sepanjang 128 bit, contohnya",
                    "    '550e8400-e29b-41d4-a716-446655440000'. PostgreSQL punya tipe uuid",
                    "    asli. MySQL pakai CHAR(36) atau BINARY(16). Untungnya, id bisa",
                    "    dibikin aplikasi tanpa nunggu database, dan aman digabung dari",
                    "    banyak server. Ruginya, ukurannya 16 byte (BIGINT cuma 8), dan",
                    "    urutannya acak, jadi index-nya lebih lambat ditulis.",
                    "",
                    "Kolom id yang terisi sendiri",
                    "",
                    "Idenya satu, tapi ejaannya beda di tiap database:",
                    "  MySQL       id BIGINT AUTO_INCREMENT PRIMARY KEY",
                    "  SQLite      id INTEGER PRIMARY KEY AUTOINCREMENT",
                    "  PostgreSQL  id BIGSERIAL PRIMARY KEY                    (gaya lama)",
                    "              id BIGINT GENERATED ALWAYS AS IDENTITY      (baku SQL)",
                    "              id UUID PRIMARY KEY DEFAULT gen_random_uuid()",
                    "",
                    "SERIAL bukan tipe data. Ia singkatan yang di belakang layar bikin",
                    "sequence, yaitu penghitung nomor urut, tersendiri. GENERATED ALWAYS AS",
                    "IDENTITY menggantikan SERIAL, supaya hak akses dan kepemilikan sequence",
                    "itu nggak perlu kamu urus lagi.",
                    "",
                    "Di SQLite ada satu jebakan kecil: tulis INTEGER, jangan INT. Kolom 'INT",
                    "PRIMARY KEY' bukan rowid (nomor baris bawaan SQLite), jadi id-nya terisi",
                    "NULL, bukan 1, 2, 3.",
                    "",
                    "Kolom waktu yang terisi sendiri",
                    "  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP",
                    "  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP",
                    "                                ON UPDATE CURRENT_TIMESTAMP  (MySQL)",
                    "  deleted_at TIMESTAMP NULL",
                    "",
                    "Kolom-kolom ini terisi walaupun nggak ada satu pun INSERT yang",
                    "menyebutnya. Isinya datang dari DEFAULT: database memakai nilai DEFAULT",
                    "kalau kolom itu nggak disebut di INSERT. Menyebut kolomnya lalu",
                    "mengisinya NULL itu beda cerita. Di kolom NOT NULL, cara itu malah bikin",
                    "error.",
                    "",
                    "ON UPDATE CURRENT_TIMESTAMP cuma ada di MySQL. Di PostgreSQL, updated_at",
                    "diisi trigger (dibahas di materi View & Trigger) atau oleh kode",
                    "aplikasi.",
                    "",
                    "Kolom deleted_at dipakai untuk soft delete. Barisnya nggak dihapus, cuma",
                    "ditandai. Akibatnya semua query wajib menambah WHERE deleted_at IS NULL.",
                    "Lupa di satu query aja, data yang \"udah dihapus\" muncul lagi. UNIQUE",
                    "juga tetap menghitung baris itu, jadi email yang \"udah dihapus\" nggak",
                    "bisa didaftarkan ulang.",
                ],
            },
            {
                "body": [
                    "Constraint adalah aturan yang dijaga oleh database, bukan oleh kode",
                    "aplikasimu. Bedanya besar. Aplikasi bisa punya banyak versi dan banyak",
                    "skrip, sedangkan constraint berlaku untuk siapa pun yang menulis data.",
                    "",
                    "Dua tempat menulis constraint",
                    "",
                    "Ini yang sering bikin bingung waktu membaca skema orang lain. Constraint",
                    "bisa ditulis di dua tempat:",
                    "  - Di tingkat kolom, menempel di belakang tipe kolomnya:",
                    "      email VARCHAR(255) NOT NULL UNIQUE",
                    "  - Di tingkat tabel, sebagai baris tersendiri sesudah semua kolom:",
                    "      PRIMARY KEY (siswa_id, kelas_kode),",
                    "      CONSTRAINT fk_siswa FOREIGN KEY (siswa_id) REFERENCES siswa (id)",
                    "",
                    "Alasannya sederhana. Constraint yang menyangkut lebih dari satu kolom",
                    "nggak punya satu kolom untuk ditempeli. NOT NULL satu-satunya yang cuma",
                    "bisa ditulis di tingkat kolom. Sisanya boleh di mana aja, dan yang",
                    "ditulis di tingkat tabel bisa dikasih nama.",
                    "",
                    "Constraint bernama",
                    "  CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (id)",
                    "",
                    "Kalau kata CONSTRAINT dan namanya nggak ditulis, database ngarang nama",
                    "sendiri, misalnya 'ambil_kelas_ibfk_1' (MySQL) atau",
                    "'ambil_kelas_siswa_id_fkey' (PostgreSQL). Nama itu penting karena dua",
                    "hal:",
                    "  1. Nama itulah yang muncul di pesan error waktu data ditolak, misalnya",
                    "     'violates foreign key constraint fk_kelas'. Kalau namanya karangan",
                    "     database, pesan error-nya jadi susah dimengerti.",
                    "  2. Nama itu juga yang harus kamu sebut untuk mencabut aturannya nanti:",
                    "       ALTER TABLE ambil_kelas DROP CONSTRAINT fk_kelas;  (PostgreSQL)",
                    "       ALTER TABLE ambil_kelas DROP FOREIGN KEY fk_kelas; (MySQL)",
                    "",
                    "Primary key gabungan (composite)",
                    "  PRIMARY KEY (siswa_id, kelas_kode)",
                    "",
                    "Yang harus unik di sini adalah pasangannya, bukan masing-masing kolom.",
                    "siswa_id 1 boleh muncul berkali-kali, kelas_kode 'IF101' juga boleh.",
                    "Yang dilarang cuma pasangan yang sama muncul dua kali. Ini bentuk baku",
                    "tabel penghubung untuk hubungan N:M (banyak-ke-banyak), dan persis",
                    "bentuk yang dipakai tabel nilai di materi JOIN: PRIMARY KEY (nim, kode).",
                    "",
                    "Akibatnya, tabel penghubung nggak perlu kolom id sendiri. Pasangan itu",
                    "udah jadi identitas barisnya. Urutan kolomnya juga ada artinya: index",
                    "gabungan bisa dipakai untuk mencari pakai kolom pertama saja, tapi nggak",
                    "bisa pakai kolom kedua saja.",
                    "",
                    "Unique gabungan",
                    "  CONSTRAINT uq_keranjang UNIQUE (user_id, produk_id)",
                    "",
                    "Satu user nggak bisa memasukkan produk yang sama dua kali, tapi user",
                    "lain tetap boleh. Bedanya dengan PRIMARY KEY: kolom UNIQUE masih boleh",
                    "NULL. Di hampir semua database, dua NULL dianggap berbeda, jadi banyak",
                    "baris NULL lolos begitu aja. Kalau nggak boleh kosong, tambahkan NOT",
                    "NULL.",
                    "",
                    "Check bernama",
                    "  CONSTRAINT harga_positif CHECK (harga >= 0)",
                    "  CONSTRAINT tanggal_urut  CHECK (selesai >= mulai)",
                    "",
                    "CHECK yang membandingkan dua kolom cuma bisa ditulis di tingkat tabel.",
                    "Ada dua jebakan:",
                    "  1. CHECK meloloskan NULL. Kondisinya jadi \"nggak diketahui\", dan itu",
                    "     nggak dianggap salah.",
                    "  2. Di MySQL sebelum 8.0.16, CHECK diterima tapi diabaikan. Jadi skema",
                    "     lama bisa punya CHECK yang nggak pernah bekerja.",
                    "",
                    "Aksi referensial",
                    "",
                    "Ini bagian FOREIGN KEY yang paling menentukan perilaku. Aksi referensial",
                    "menjawab pertanyaan: kalau baris induk dihapus atau diubah, baris",
                    "anaknya diapakan?",
                    "  ON DELETE RESTRICT     tolak hapus induk selama anaknya masih ada",
                    "  ON DELETE NO ACTION    sama, tapi bisa ditunda sampai akhir transaksi",
                    "  ON DELETE CASCADE      induk dihapus -> semua anaknya ikut terhapus",
                    "  ON DELETE SET NULL     kolom FK di anak diisi NULL (harus boleh NULL)",
                    "  ON DELETE SET DEFAULT  diisi nilai DEFAULT kolom itu",
                    "  ON UPDATE ...          pilihan sama, dipicu saat kunci induk berubah",
                    "",
                    "Bawaannya NO ACTION atau RESTRICT. Jadi kalau kamu nggak menulis klausa",
                    "apa pun, DELETE pada induk ditolak. Artinya foreign key aktif menolak",
                    "perintah yang melanggarnya. Kalau DELETE FROM users WHERE id = 1 gagal,",
                    "itu bukan bug. Ada baris pesanan yang menunjuk user itu, dan foreign key",
                    "sedang melindunginya.",
                    "",
                    "Pilih CASCADE cuma kalau anaknya nggak ada artinya tanpa induk, misalnya",
                    "isi keranjang, baris tabel penghubung, atau komentar. Jangan pakai untuk",
                    "pesanan: menghapus satu user nggak boleh ikut menghapus riwayat",
                    "belanjanya tanpa ada yang tahu.",
                    "",
                    "Khusus SQLite, foreign key baru ditegakkan sesudah perintah PRAGMA",
                    "foreign_keys = ON dijalankan di tiap koneksi. Bawaannya mati, jadi skema",
                    "yang benar pun bisa kelihatan \"nggak bekerja\".",
                    "",
                    "Penjaga idempoten",
                    "",
                    "Hampir tiap berkas skema dibuka dengan DROP TABLE IF EXISTS, CREATE",
                    "TABLE IF NOT EXISTS, atau DROP INDEX IF EXISTS. Tujuannya supaya berkas",
                    "itu idempoten, artinya hasilnya sama walaupun dijalankan berkali-kali.",
                    "",
                    "Berkas skema memang dijalankan berulang kali: waktu pasang ulang, waktu",
                    "tes, di CI, atau waktu teman baru clone repo. Tanpa IF EXISTS, jalan",
                    "kedua langsung berhenti di 'table already exists', dan sisa berkasnya",
                    "nggak pernah dijalankan.",
                    "",
                    "Urutan DROP wajib kebalikan dari urutan CREATE: anak dulu, induk",
                    "belakangan. Foreign key menolak induk dihapus lebih dulu.",
                    "",
                    "Ingat: IF EXISTS cuma bikin perintahnya nggak error. DROP tetap nggak",
                    "aman, datanya tetap habis.",
                ],
            },
            {
                "heading": "Skema utuh: semuanya sekaligus",
                "code": """-- Bentuk berkas schema.sql yang sebenarnya: penjaga idempoten, id & waktu
-- yang mengisi dirinya sendiri, kunci gabungan, dan constraint bernama.
PRAGMA foreign_keys = ON;   -- wajib di SQLite; MySQL & PostgreSQL selalu aktif

DROP TABLE IF EXISTS ambil_kelas;   -- anak dulu ...
DROP TABLE IF EXISTS kelas;
DROP TABLE IF EXISTS siswa;         -- ... induk belakangan

CREATE TABLE IF NOT EXISTS siswa (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,   -- MySQL: AUTO_INCREMENT
    email      TEXT    NOT NULL UNIQUE,
    nama       TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS kelas (
    kode TEXT PRIMARY KEY,
    nama TEXT NOT NULL
);

-- Tabel penghubung N:M. Identitasnya PASANGAN, bukan kolom id baru.
CREATE TABLE IF NOT EXISTS ambil_kelas (
    siswa_id   INTEGER NOT NULL,
    kelas_kode TEXT    NOT NULL,
    nilai      INTEGER,
    PRIMARY KEY (siswa_id, kelas_kode),
    CONSTRAINT fk_siswa FOREIGN KEY (siswa_id)
        REFERENCES siswa (id)   ON DELETE CASCADE,
    CONSTRAINT fk_kelas FOREIGN KEY (kelas_kode)
        REFERENCES kelas (kode) ON DELETE RESTRICT,
    CONSTRAINT nilai_wajar CHECK (nilai BETWEEN 0 AND 100)
);

-- id dan created_at sengaja TIDAK disebut, biar DEFAULT database yang mengisi.
INSERT INTO siswa (email, nama) VALUES
    ('andi@kampus.id', 'Andi'),
    ('budi@kampus.id', 'Budi');

INSERT INTO kelas VALUES ('IF101', 'Algoritma'), ('IF202', 'Basis Data');

-- siswa 1 muncul 2x dan IF101 muncul 2x: yang dijaga cuma PASANGANNYA.
INSERT INTO ambil_kelas VALUES
    (1, 'IF101', 90), (1, 'IF202', 85), (2, 'IF101', 78);

SELECT 'id & created_at terisi sendiri : ' || id
       || ' / ' || (created_at IS NOT NULL) FROM siswa;
SELECT 'baris ambil_kelas sekarang     : ' || COUNT(*) FROM ambil_kelas;

DELETE FROM siswa WHERE id = 1;   -- fk_siswa memakai ON DELETE CASCADE

SELECT 'setelah siswa 1 dihapus        : ' || COUNT(*) FROM ambil_kelas;

-- Tiga baris berikut DITOLAK kalau komentarnya kamu buka - coba satu per satu:
--   INSERT INTO ambil_kelas VALUES (2, 'IF101', 60);
--     -> UNIQUE constraint failed: ambil_kelas.siswa_id, ambil_kelas.kelas_kode
--        (pasangannya sudah ada; PRIMARY KEY gabungan yang menolak)
--   INSERT INTO ambil_kelas VALUES (2, 'IF202', 150);
--     -> CHECK constraint failed: nilai_wajar
--   DELETE FROM kelas WHERE kode = 'IF101';
--     -> FOREIGN KEY constraint failed  (fk_kelas memakai RESTRICT)""",
            },
        ],
    },
    {
        "title": "4. Membuka Database & Berkas SQL Orang Lain",
        "sections": [
            {
                "body": [
                    "Sampai sini kamu selalu bikin tabel sendiri, jadi kamu hafal isinya. Di",
                    "pekerjaan nyata hampir nggak pernah begitu. Kamu masuk ke database yang",
                    "udah berisi 40 tabel buatan orang lain. Atau kamu membuka repositori di",
                    "GitHub, ketemu berkas schema.sql, dan nggak tahu cara menjalankannya.",
                    "Materi ini menjawab dua masalah itu.",
                    "",
                    "Untuk melihat isi database di MySQL, pakai perintah-perintah ini:",
                    "  SHOW DATABASES;             -- daftar database di server ini",
                    "  USE toko;                   -- pilih database yang mau dipakai",
                    "  SHOW TABLES;                -- daftar tabel di database terpilih",
                    "  DESCRIBE pesanan;           -- kolom, tipe, boleh NULL?, default",
                    "  DESC pesanan;               -- singkatan DESCRIBE, artinya sama",
                    "  SHOW CREATE TABLE pesanan;  -- perintah CREATE aslinya, apa adanya",
                    "  SHOW INDEX FROM pesanan;    -- index di tabel itu, unik atau tidak",
                    "",
                    "Yang paling banyak ngasih info adalah SHOW CREATE TABLE. Di situ",
                    "kelihatan FOREIGN KEY, DEFAULT, engine, dan charset-nya sekaligus.",
                    "",
                    "Kata DESC punya dua arti, dan ini sering bikin bingung. Kalau berdiri",
                    "sendiri, DESC itu singkatan DESCRIBE. Kalau dipakai di ORDER BY, artinya",
                    "\"urut menurun\". Yang menentukan artinya adalah posisinya.",
                    "",
                    "Program klien lain punya perintah sendiri untuk pertanyaan yang sama.",
                    "Klien itu program yang kamu pakai untuk ngobrol dengan database,",
                    "misalnya psql untuk PostgreSQL dan sqlite3 untuk SQLite:",
                    "  Ada database apa saja?",
                    "    psql    : \\l",
                    "    sqlite3 : tidak ada -- satu berkas .db memang satu database",
                    "  Ada tabel apa saja?",
                    "    psql    : \\dt",
                    "    sqlite3 : .tables",
                    "  Kolom sebuah tabel?",
                    "    psql    : \\d pesanan",
                    "    sqlite3 : .schema pesanan",
                    "",
                    "Jebakan: perintah yang diawali titik (.tables) dan garis miring terbalik",
                    "(\\dt) itu bukan SQL. Perintah itu milik program kliennya sendiri. Kalau",
                    "kamu tempel ke dalam kode program atau ke aplikasi GUI database,",
                    "hasilnya langsung error.",
                    "",
                    "Satu lagi: sqlite3 mencetak hasil polos tanpa nama kolom, dipisah tanda",
                    "|. Supaya gampang dibaca, nyalakan dulu dua pengaturan ini:",
                    "  .headers on",
                    "  .mode column",
                    "",
                    "Aplikasi ini menjalankan latihan SQL-mu pakai sqlite3, jadi dua baris",
                    "itu langsung kepakai.",
                ],
            },
            {
                "heading": "Peta skema yang bisa kamu jalankan",
                "body": [
                    "Pertanyaan \"ada tabel apa saja\" juga bisa ditanyakan lewat SELECT biasa.",
                    "Cara ini berlaku di MySQL, PostgreSQL, dan SQL Server:",
                    "",
                    "  SELECT table_name",
                    "  FROM information_schema.tables",
                    "  WHERE table_schema = 'toko';",
                    "",
                    "  SELECT column_name, data_type, is_nullable, column_default",
                    "  FROM information_schema.columns",
                    "  WHERE table_schema = 'toko' AND table_name = 'pesanan'",
                    "  ORDER BY ordinal_position;",
                    "",
                    "information_schema adalah database bawaan yang isinya tabel-tabel",
                    "pencatat, yaitu tabel yang mencatat tabel lain. Hasilnya berupa baris",
                    "biasa, jadi bisa disaring pakai WHERE, digabung pakai JOIN, dan dipakai",
                    "dari dalam program. SHOW TABLES nggak bisa sefleksibel itu.",
                    "",
                    "Di PostgreSQL, isi table_schema biasanya 'public', bukan nama",
                    "databasenya. SQLite nggak punya information_schema. Padanannya adalah",
                    "tabel sqlite_master.",
                    "",
                    "Berkas di bawah ini bikin dua tabel, lalu membaca strukturnya lagi,",
                    "seolah kamu baru pertama kali membuka database itu.",
                ],
                "code": """-- Peta sebuah database, dibaca ulang dari nol.
.headers on
.mode column

CREATE TABLE penulis (
    id   INTEGER PRIMARY KEY,
    nama TEXT NOT NULL
);

CREATE TABLE buku (
    id         INTEGER PRIMARY KEY,
    judul      TEXT NOT NULL,
    penulis_id INTEGER REFERENCES penulis(id)
);

CREATE INDEX idx_buku_penulis ON buku(penulis_id);

-- Ada tabel apa saja? (di MySQL: SHOW TABLES;)
.tables

-- Tabel buku dibuat dengan perintah apa? (di MySQL: SHOW CREATE TABLE buku;)
.schema buku

-- Tanpa dot-command: skema pun bisa ditanya lewat SELECT biasa.
SELECT type, name FROM sqlite_master ORDER BY type, name;

-- Kolom apa saja di tabel buku? (di MySQL: DESCRIBE buku;)
-- "notnull" harus dikutip karena NOTNULL kata cadangan di SQLite.
SELECT name, type, "notnull", pk FROM pragma_table_info('buku');""",
            },
            {
                "heading": "SQL yang hidup sebagai berkas",
                "body": [
                    "Di repositori, SQL jarang berupa ketikan di prompt. Biasanya SQL",
                    "disimpan dalam berkas: schema.sql untuk struktur, seed.sql untuk data",
                    "awal, dan cadangan.sql untuk hasil backup. Cara menjalankannya:",
                    "  MySQL      : mysql -u root -p toko < schema.sql",
                    "  MySQL      : SOURCE schema.sql;   -- kalau sudah di dalam sesi",
                    "  PostgreSQL : psql -d toko -f schema.sql",
                    "  SQLite     : sqlite3 app.db < schema.sql",
                    "",
                    "Tanda < itu milik shell, bukan SQL. Gunanya menyuapkan isi berkas ke",
                    "program, seolah kamu mengetiknya sendiri. Karena itu tanda < diketik di",
                    "terminal, bukan di dalam sesi mysql. Di dalam sesi, padanannya SOURCE",
                    "(boleh juga ditulis \\. schema.sql).",
                    "",
                    "Urutannya penting: schema.sql dulu, baru seed.sql. Kalau dibalik, seed",
                    "mencoba mengisi tabel yang belum ada, dan langsung gagal di baris",
                    "pertama.",
                    "",
                    "Berkas .sql yang besar biasanya hasil perintah dump, yaitu perintah yang",
                    "menyalin isi database ke dalam berkas:",
                    "  mysqldump -u root -p toko > cadangan.sql          -- struktur+data",
                    "  mysqldump -u root -p --no-data toko > schema.sql  -- struktur saja",
                    "  pg_dump -U postgres toko > cadangan.sql",
                    "",
                    "Untuk mengembalikannya:",
                    "  mysql -u root -p toko < cadangan.sql",
                    "",
                    "Dump dari perintah di atas nggak membuat databasenya. Jadi kamu harus",
                    "menjalankan CREATE DATABASE toko; lebih dulu. Kalau nggak, proses",
                    "restore berhenti dengan pesan 'No database selected'.",
                    "",
                    "Isi berkas dump selalu kelihatan aneh buat pemula. Potongan khasnya",
                    "begini:",
                    "  SET NAMES utf8mb4;",
                    "  SET FOREIGN_KEY_CHECKS = 0;",
                    "  DROP TABLE IF EXISTS `pesanan`;",
                    "  CREATE TABLE `pesanan` (",
                    "    `id` int NOT NULL AUTO_INCREMENT,",
                    "    `kode` varchar(20) NOT NULL,",
                    "    `customer_id` int DEFAULT NULL,",
                    "    PRIMARY KEY (`id`),",
                    "    UNIQUE KEY `kode` (`kode`)",
                    "  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;",
                    "",
                    "Yang perlu kamu pahami dari potongan itu:",
                    "  - SET NAMES utf8mb4 artinya sesi ini pakai UTF-8 penuh, termasuk",
                    "    emoji.",
                    "  - FOREIGN_KEY_CHECKS = 0 mematikan pengecekan foreign key sementara.",
                    "    Dump menulis tabel menurut urutan abjad, jadi tabel anak bisa dibuat",
                    "    sebelum induknya. Kalau pengecekannya nggak dimatikan, restore gagal",
                    "    di tengah jalan. Di akhir berkas, nilainya dikembalikan ke 1.",
                    "  - ENGINE=InnoDB adalah mesin penyimpan MySQL. InnoDB yang bikin",
                    "    FOREIGN KEY dan transaction bekerja (dibahas di materi Transaction).",
                    "    Mesin lama, MyISAM, menerima FOREIGN KEY tapi nggak pernah",
                    "    menjalankannya, dan nggak ngasih tahu apa-apa.",
                    "  - Tanda backtick (`) di tiap nama muncul karena berkas ini ditulis",
                    "    program. Program itu mengutip semua nama supaya tetap aman walaupun",
                    "    ada kolom bernama order.",
                ],
            },
            {
                "heading": "Isi folder migrations/",
                "body": [
                    "Struktur database yang udah dipakai orang nggak diubah dengan mengedit",
                    "schema.sql. Perubahannya ditumpuk sebagai berkas-berkas kecil yang",
                    "bernomor urut di folder migrations/. Satu berkas seperti itu disebut",
                    "migrasi:",
                    "  001_buat_tabel_customer.up.sql",
                    "  001_buat_tabel_customer.down.sql",
                    "  002_tambah_kolom_email.up.sql",
                    "  002_tambah_kolom_email.down.sql",
                    "",
                    "Cara menomorinya tergantung alat yang dipakai, tapi polanya mirip:",
                    "  V1__buat_tabel.sql            -> gaya Flyway (dua garis bawah)",
                    "  001_init.up.sql               -> gaya golang-migrate, ada .down",
                    "  20240115120000_buat_user.sql  -> gaya Rails, cap waktu",
                    "",
                    "Laravel juga pakai cap waktu, cuma bagian tanggalnya dipisah garis",
                    "bawah, misalnya 2024_01_15_120000_buat_user.",
                    "",
                    "Berkas up berisi perubahan maju, misalnya ADD COLUMN. Berkas down berisi",
                    "pembatalnya, misalnya DROP COLUMN, dan dipakai kalau perubahannya harus",
                    "ditarik kembali. seed.sql urusannya lain. Isinya data awal yang memang",
                    "harus ada, seperti daftar kategori atau daftar role. seed.sql nggak",
                    "mengubah struktur.",
                    "",
                    "Ingat: migrasi yang udah pernah dijalankan nggak boleh diedit lagi.",
                    "Aturan ini jarang ditulis, tapi berlaku di semua tim. Alat migrasi",
                    "mencatat migrasi mana saja yang udah jalan di tabel khusus, misalnya",
                    "schema_migrations atau flyway_schema_history. Nomor yang tercatat di",
                    "sana dianggap selesai, jadi suntinganmu nggak pernah sampai ke database",
                    "teman satu timmu.",
                    "",
                    "Sebagian alat, seperti Flyway, juga nyimpen sidik jari (checksum) tiap",
                    "berkas. Kalau berkas lama diedit, sidik jarinya nggak cocok lagi, dan",
                    "alatnya menolak jalan. Jadi kalau ada yang salah, bikin migrasi baru",
                    "yang membetulkannya.",
                    "",
                    "Isi berkas migrasi hampir selalu ALTER TABLE. Perintah di bawah bisa",
                    "kamu coba di sesi database untuk melihat bentuknya. Di repositori, tiap",
                    "perubahan disimpan di berkasnya sendiri.",
                ],
                "code": """-- MySQL
ALTER TABLE pelanggan RENAME TO customer;
ALTER TABLE customer RENAME COLUMN nama TO nama_lengkap;
ALTER TABLE customer MODIFY email VARCHAR(200) NOT NULL;
ALTER TABLE pesanan ADD CONSTRAINT fk_pesanan_customer
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE;
ALTER TABLE pesanan DROP FOREIGN KEY fk_pesanan_customer;

-- PostgreSQL: maksud yang sama, kata kuncinya berbeda
ALTER TABLE customer ALTER COLUMN email TYPE VARCHAR(200);
ALTER TABLE customer ALTER COLUMN email SET NOT NULL;
ALTER TABLE pesanan DROP CONSTRAINT fk_pesanan_customer;""",
            },
            {
                "body": [
                    "Hal yang paling sering bikin bingung waktu membaca SQL orang lain adalah",
                    "tanda kutip. Ada empat macam, dan artinya beda-beda:",
                    "  'Andi'    -> kutip tunggal: nilai teks & tanggal. Sama di semua DB.",
                    "  `pesanan` -> backtick: NAMA tabel/kolom di MySQL & MariaDB.",
                    "  \"pesanan\" -> kutip ganda: NAMA di PostgreSQL, Oracle, SQLite.",
                    "  [pesanan] -> kurung siku: NAMA di SQL Server.",
                    "",
                    "Jebakan: WHERE nama = \"Andi\" jalan lancar di MySQL, tapi gagal di",
                    "PostgreSQL dengan pesan column \"Andi\" does not exist. Di PostgreSQL,",
                    "kutip ganda artinya nama kolom. Jadi biasakan pakai kutip tunggal untuk",
                    "teks, di database mana pun.",
                    "",
                    "Nama wajib dikutip kalau namanya kata cadangan, yaitu kata yang udah",
                    "dipakai SQL sendiri: order, user, group, from, table, key, desc. Kolom",
                    "bernama order ditulis `order` di MySQL dan \"order\" di PostgreSQL.",
                    "Makanya banyak tim memilih nama jamak seperti orders sejak awal, supaya",
                    "nggak perlu dikutip terus.",
                    "",
                    "Di PostgreSQL, nama tanpa kutip otomatis diubah jadi huruf kecil. Kalau",
                    "sebuah tabel telanjur dibuat dengan nama \"User\" (pakai kutip), perintah",
                    "SELECT * FROM User; akan selalu gagal, karena yang dicari adalah tabel",
                    "user.",
                    "",
                    "Cara mengenali logat (dialek) sebuah berkas dalam sepuluh detik:",
                    "  `backtick` + ENGINE=InnoDB + AUTO_INCREMENT -> MySQL / MariaDB",
                    "  \"kutip ganda\" + SERIAL + tanda :: + $$      -> PostgreSQL",
                    "  [kurung siku] + GO sendirian sebaris + TOP  -> SQL Server",
                    "  AUTOINCREMENT + PRAGMA                      -> SQLite",
                    "",
                    "Padanan untuk hal-hal yang paling sering beda:",
                    "  Hal             MySQL              PostgreSQL     SQLite",
                    "  --------------  -----------------  -------------  ---------------",
                    "  id otomatis     AUTO_INCREMENT     SERIAL         AUTOINCREMENT",
                    "  gabung teks     CONCAT(a, b)       a || b         a || b",
                    "  tidak sama      <> atau !=         <> atau !=     <> atau !=",
                    "  batas 10 baris  LIMIT 10           LIMIT 10       LIMIT 10",
                    "  waktu sekarang  NOW()              NOW()          datetime('now')",
                    "  mulai trans.    START TRANSACTION  BEGIN          BEGIN",
                    "",
                    "Tanda <> dan != sama-sama jalan di MySQL, PostgreSQL, SQLite, dan SQL",
                    "Server. Tapi <> yang standar dan pasti diterima di mana pun, jadi",
                    "biasakan pakai <>.",
                    "",
                    "Untuk membatasi jumlah baris, dua database besar justru punya cara",
                    "sendiri:",
                    "  SQL Server : SELECT TOP 10 * FROM pesanan;",
                    "  Oracle     : SELECT * FROM pesanan FETCH FIRST 10 ROWS ONLY;",
                ],
            },
        ],
    },
    {
        "title": "5. DML: Insert, Update, Delete",
        "sections": [
            {
                "body": [
                    "DML (Data Manipulation Language) adalah kelompok perintah untuk",
                    "mengelola data di dalam tabel: menambah, mengubah, dan menghapus.",
                    "Strukturnya sendiri nggak disentuh.",
                    "",
                    "Data baru ditambahkan pakai INSERT. Bentuk umumnya begini:",
                    "  INSERT INTO tabel (kolom1, kolom2, ...)",
                    "  VALUES (nilai1, nilai2, ...);",
                    "",
                    "Contohnya, menambah satu mahasiswa:",
                    "  INSERT INTO mahasiswa (nim, nama, jurusan, ipk)",
                    "  VALUES (101, 'Andi', 'Informatika', 3.5);",
                    "",
                    "Kamu juga bisa menambah beberapa baris sekaligus. Kalau daftar kolomnya",
                    "nggak ditulis, nilainya harus lengkap dan urut sesuai kolom di tabel:",
                    "  INSERT INTO mahasiswa VALUES",
                    "      (102, 'Budi', 'Sistem Info', 3.2),",
                    "      (103, 'Citra', 'Informatika', 3.8);",
                    "",
                    "Soal tanda kutip:",
                    "  - Nilai teks dan tanggal ditulis di dalam tanda kutip tunggal,",
                    "    misalnya 'Andi'.",
                    "  - Angka nggak perlu dikutip.",
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
                    "Hati-hati: UPDATE dan DELETE tanpa WHERE mengenai semua baris di tabel.",
                    "Database nggak nanya \"yakin?\", perintahnya langsung dijalankan:",
                    "  UPDATE mahasiswa SET ipk = 0;   -- ipk semua jadi 0!",
                    "  DELETE FROM mahasiswa;          -- data habis semua!",
                    "",
                    "Tiga kebiasaan yang melindungi datamu:",
                    "  1. Jalankan SELECT dulu dengan WHERE yang sama, sebelum UPDATE atau",
                    "     DELETE. Dari situ kamu tahu baris mana saja yang bakal kena.",
                    "  2. Kalau datanya penting, pakai transaction (BEGIN, COMMIT, ROLLBACK).",
                    "  3. Bikin backup sebelum mengubah data dalam jumlah besar.",
                    "",
                    "Transaction itu cara mengelompokkan beberapa perintah supaya bisa",
                    "dibatalkan bareng-bareng. Selama belum di-COMMIT, semua perubahan di",
                    "dalamnya masih bisa dibatalkan pakai ROLLBACK:",
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
        "title": "6. SELECT & Filtering",
        "sections": [
            {
                "body": [
                    "SELECT adalah perintah yang paling sering dipakai. Gunanya membaca dan",
                    "menampilkan data dari tabel.",
                    "",
                    "Bentuk dasarnya: sebutkan kolom yang mau diambil, lalu tabelnya. Tanda *",
                    "artinya semua kolom:",
                    "  SELECT kolom1, kolom2 FROM nama_tabel;",
                    "  SELECT * FROM nama_tabel;   -- semua kolom",
                    "",
                    "  SELECT nama, ipk FROM mahasiswa;",
                    "",
                    "Alias adalah nama sementara untuk kolom di hasil query. Nama aslinya di",
                    "tabel nggak berubah:",
                    "  SELECT nama AS 'Nama Lengkap', ipk AS IPK FROM mahasiswa;",
                    "  -- AS boleh dihilangkan:  SELECT nama 'Nama Lengkap' FROM mahasiswa;",
                    "",
                    "Alias pakai kutip tunggal seperti di atas diterima MySQL dan SQLite,",
                    "tapi nggak di PostgreSQL. Di PostgreSQL, kutip tunggal selalu berarti",
                    "teks. Jadi 'Nama Lengkap' dibaca sebagai nilai teks, lalu ditolak",
                    "sebagai nama kolom.",
                    "",
                    "Bentuk yang jalan di mana-mana pakai kutip ganda:",
                    "  SELECT nama AS \"Nama Lengkap\", ipk AS IPK FROM mahasiswa;",
                    "",
                    "Paling aman, pilih alias tanpa spasi, misalnya AS nama_lengkap. Alias",
                    "seperti itu nggak perlu dikutip di database mana pun.",
                    "",
                    "Untuk membuang baris yang isinya kembar, pakai DISTINCT. Contoh ini",
                    "menampilkan tiap jurusan sekali aja:",
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
                    "Beberapa syarat bisa digabung pakai operator logika AND, OR, dan NOT.",
                    "AND artinya semua syarat harus benar, OR artinya cukup salah satu, dan",
                    "NOT membalik syaratnya:",
                    "  SELECT * FROM mahasiswa",
                    "  WHERE jurusan = 'Informatika' AND ipk > 3.4;",
                    "",
                    "  SELECT * FROM mahasiswa",
                    "  WHERE jurusan = 'Informatika' OR jurusan = 'Teknik Komp';",
                    "",
                    "  SELECT * FROM mahasiswa",
                    "  WHERE NOT angkatan = 2021;",
                    "",
                    "LIKE dipakai untuk mencari teks yang cocok dengan pola. Ada dua tanda",
                    "khusus di polanya:",
                    "  %  -> nol atau lebih karakter",
                    "  _  -> tepat satu karakter",
                    "  LIKE 'A%'   -> diawali A  (Andi)",
                    "  LIKE '%a'   -> diakhiri a  (Citra)",
                    "  LIKE '%di%' -> mengandung 'di' (Andi, Budi)",
                    "  LIKE 'B_d_' -> B diikuti 1 karakter, d, 1 karakter",
                    "",
                    "Hasil query bisa diurutkan pakai ORDER BY. DESC artinya dari besar ke",
                    "kecil, ASC dari kecil ke besar. Kalau ada dua kolom, kolom kedua dipakai",
                    "untuk mengurutkan baris yang nilai kolom pertamanya sama:",
                    "  SELECT * FROM mahasiswa ORDER BY ipk DESC;",
                    "  SELECT * FROM mahasiswa ORDER BY angkatan ASC, ipk DESC;",
                    "",
                    "Mungkin kamu heran kenapa contoh di atas menulis WHERE ipk IS NOT NULL,",
                    "bukan != NULL. NULL artinya \"nggak diketahui\". Membandingkannya pakai =",
                    "atau != nggak pernah menghasilkan benar. Bahkan NULL = NULL pun hasilnya",
                    "nggak benar. Satu-satunya cara memeriksanya adalah IS NULL atau IS NOT",
                    "NULL. Aturan lengkapnya ada di materi berikutnya, Ekspresi, NULL & CASE.",
                ]
            },
        ],
    },
    {
        "title": "7. Ekspresi, NULL & CASE",
        "sections": [
            {
                "body": [
                    "SELECT nggak cuma bisa mengambil kolom yang udah ada. SELECT juga bisa",
                    "menghitung kolom baru dari kolom lain. Apa pun yang ditulis di antara",
                    "SELECT dan FROM disebut ekspresi. Hasilnya cuma ada selama query itu",
                    "jalan. Nggak disimpan ke tabel, dan nggak mengubah apa-apa.",
                    "",
                    "Operator aritmatika yang bisa kamu pakai:",
                    "  +   tambah      harga + ongkir",
                    "  -   kurang      stok - terjual",
                    "  *   kali        harga * stok",
                    "  /   bagi        total / jumlah",
                    "  %   sisa bagi   id % 2      -> 0 kalau genap, 1 kalau ganjil",
                    "",
                    "  SELECT nama, harga * stok AS nilai_stok FROM produk;",
                    "",
                    "Kalau nggak pakai AS, nama kolom hasilnya jadi tulisan 'harga * stok'",
                    "apa adanya. Itu sah, tapi susah dibaca, baik oleh orang maupun oleh",
                    "aplikasi. Alias udah dibahas di materi SELECT & Filtering. Mulai dari",
                    "sini, alias jadi keharusan.",
                    "",
                    "Ekspresi juga boleh dipakai di WHERE dan ORDER BY, nggak cuma di SELECT:",
                    "  SELECT * FROM produk WHERE harga * stok > 1000000;",
                    "  SELECT * FROM produk ORDER BY harga * stok DESC;",
                    "",
                    "Kolom yang dihitung dari dirinya sendiri",
                    "",
                    "Di UPDATE, sebuah kolom bisa diisi pakai nilai lamanya sendiri:",
                    "  UPDATE produk SET harga = harga * 1.10 WHERE kategori = 'Minuman';",
                    "",
                    "Tanda = di SET artinya \"isi dengan\", bukan perbandingan. Sisi kanan",
                    "dihitung lebih dulu pakai nilai lama baris itu, lalu hasilnya ditulis ke",
                    "kolom. Tiap baris dihitung sendiri-sendiri. Jadi satu perintah ini",
                    "menaikkan harga semua minuman sekaligus, dan kamu nggak perlu tahu harga",
                    "masing-masing.",
                    "",
                    "Bentuk yang persis sama dipakai untuk transfer saldo di materi",
                    "Transaction:",
                    "  UPDATE rekening SET saldo = saldo - 500000 WHERE id = 'A';",
                    "",
                    "Jebakan: pembagian bilangan bulat. Kalau kedua sisi tanda / berupa",
                    "bilangan bulat, banyak database memotong hasilnya jadi bulat juga. 5 / 2",
                    "hasilnya 2, bukan 2.5. Tiap database beda, jadi jangan menebak dari",
                    "ingatan:",
                    "  PostgreSQL, SQL Server, SQLite -> 2",
                    "  MySQL, Oracle                  -> 2.5",
                    "",
                    "Bahayanya, nggak ada error dan nggak ada peringatan. Yang keluar cuma",
                    "angka yang salah. Yang paling sering kena adalah persentase. Ekspresi",
                    "ini menghasilkan 0 untuk semua baris:",
                    "  stok / total * 100",
                    "",
                    "Alasannya, stok / total udah dibulatkan jadi 0 lebih dulu, baru",
                    "dikali 100. Ada tiga cara menghindarinya, pilih salah satu:",
                    "  stok * 100.0 / total         -- sentuh dulu dengan angka desimal",
                    "  stok * 1.0 / total           -- trik lama, sama saja maksudnya",
                    "  CAST(stok AS REAL) / total   -- ubah tipenya terang-terangan",
                    "",
                    "Mengubah tipe secara langsung",
                    "",
                    "Mengubah tipe data sebuah nilai disebut konversi tipe, atau cast.",
                    "Bentuknya beda-beda:",
                    "  CAST(nilai AS DECIMAL(10,2))   -- standar, dimengerti semua database",
                    "  CONVERT(nilai, DECIMAL(10,2))  -- MySQL (di SQL Server urutannya terbalik)",
                    "  harga::numeric                 -- bentuk pendek khas PostgreSQL",
                    "  '2024-01-01'::date             -- sama, untuk tanggal",
                    "",
                    "Titik dua ganda (::) adalah operator cast milik PostgreSQL. Artinya lain",
                    "dengan :: di C++ seperti std::cout. Kalau ketemu di query orang lain,",
                    "baca aja \"ubah jadi\".",
                    "",
                    "Fungsi angka yang sering muncul",
                    "  ROUND(nilai, digit) -> bulatkan     ROUND(3.14159, 2) = 3.14",
                    "  ABS(nilai)          -> nilai mutlak, tanda minus dibuang",
                    "  CEIL / CEILING      -> bulatkan ke ATAS    CEIL(2.1) = 3",
                    "  FLOOR               -> bulatkan ke BAWAH   FLOOR(2.9) = 2",
                    "  MOD(a, b)           -> sisa bagi, sama artinya dengan a % b",
                    "  POWER(a, b)         -> pangkat            POWER(2, 10) = 1024",
                    "  GREATEST(a, b, ...) -> terbesar di antara beberapa KOLOM, dalam satu baris",
                    "  LEAST(a, b, ...)    -> terkecil di antara beberapa kolom, dalam satu baris",
                    "",
                    "ROUND paling sering dipasangkan dengan AVG. Tanpa ROUND, rata-rata",
                    "keluar dengan belasan angka di belakang koma, dan laporannya jadi nggak",
                    "enak dibaca:",
                    "  SELECT jurusan, ROUND(AVG(ipk), 2) FROM mahasiswa GROUP BY jurusan;",
                    "",
                    "Soal beda database: SQLite nggak punya GREATEST dan LEAST. Di SQLite,",
                    "yang bekerja per baris adalah MAX(a, b) dan MIN(a, b). Namanya sama",
                    "dengan fungsi agregat MAX dan MIN, tapi kerjanya lain. SQL Server baru",
                    "punya GREATEST dan LEAST sejak versi 2022.",
                ],
            },
            {
                "heading": "Ekspresi & jebakan pembagian bulat",
                "code": """CREATE TABLE produk (
    id    INTEGER      PRIMARY KEY,
    nama  VARCHAR(50),
    harga DECIMAL(10,2),
    stok  INT
);

INSERT INTO produk VALUES
(1, 'Kopi Kapal Api',  3000, 100),
(2, 'Teh Botol',       5000,  40),
(3, 'Beras 5kg',      68000,  50);

-- 1. Kolom hasil hitungan. Ekspresi apa pun boleh berdiri di SELECT.
SELECT nama, harga, stok, harga * stok AS nilai_stok FROM produk;

-- 2. Dua bilangan bulat dibagi -> hasilnya ikut dipotong jadi bulat.
SELECT 5 / 2 AS bulat, 5.0 / 2 AS desimal, 5 * 1.0 / 2 AS dipaksa_desimal;
--        2      2.5              2.5

-- 3. Akibatnya pada persentase. Total stok = 190.
SELECT nama,
       stok / 190 * 100             AS persen_salah,   -- ketiganya 0
       stok * 100.0 / 190           AS persen_benar,
       ROUND(stok * 100.0 / 190, 2) AS persen_rapi
FROM produk;

-- 4. CAST memaksa tipe. Ini cara resmi keluar dari pembagian bulat.
SELECT stok, CAST(stok AS REAL) / 3 AS per_tiga_hari
FROM produk WHERE id = 1;

-- 5. Sisi kanan tanda '=' berisi nilai LAMA baris itu: harga naik 10%.
UPDATE produk SET harga = harga * 1.10 WHERE nama = 'Teh Botol';
SELECT nama, harga FROM produk WHERE id = 2;   -- 5000 -> 5500

-- 6. Fungsi numerik yang paling sering muncul.
SELECT ABS(-7) AS mutlak, ROUND(3.14159, 2) AS dua_desimal, 17 % 5 AS sisa;""",
            },
            {
                "body": [
                    "NULL bukan angka 0, dan bukan juga teks kosong ''. NULL artinya \"nggak",
                    "diketahui\".",
                    "",
                    "  ipk = 0     -> orang ini punya IPK, dan nilainya memang nol.",
                    "  nama = ''   -> datanya ada, isinya kebetulan kosong.",
                    "  ipk = NULL  -> tidak ada yang tahu berapa. Belum diisi, belum diukur.",
                    "",
                    "Bedanya kelihatan sepele, sampai kamu menghitung rata-rata. Nilai 0 ikut",
                    "menarik rata-rata ke bawah, sedangkan NULL nggak ikut dihitung sama",
                    "sekali.",
                    "",
                    "Logika tiga nilai",
                    "",
                    "Di kebanyakan bahasa pemrograman, perbandingan hasilnya benar atau",
                    "salah. Di SQL ada nilai ketiga, yaitu unknown (nggak diketahui). Kalau",
                    "kamu membandingkan sesuatu dengan yang nggak diketahui, hasilnya juga",
                    "nggak diketahui:",
                    "  ipk = NULL    -> unknown   (BUKAN benar, dan bukan salah)",
                    "  ipk <> NULL   -> unknown",
                    "  NULL = NULL   -> unknown   (dua hal tak diketahui belum tentu sama)",
                    "",
                    "WHERE cuma meloloskan baris yang kondisinya benar. Baris yang hasilnya",
                    "unknown ikut dibuang bareng yang salah. Makanya:",
                    "  SELECT * FROM mahasiswa WHERE ipk = NULL;     -- selalu 0 baris",
                    "  SELECT * FROM mahasiswa WHERE ipk IS NULL;    -- ini yang benar",
                    "  SELECT * FROM mahasiswa WHERE ipk IS NOT NULL;",
                    "",
                    "Query pertama nggak error. Dia jalan lancar dan mengembalikan hasil",
                    "kosong. Karena itu kesalahan ini bisa bertahan lama di kode nyata tanpa",
                    "ketahuan. Ini juga jawaban kenapa 'SELECT nama FROM n WHERE n.nim =",
                    "NULL' salah. Sintaksnya benar, tapi kondisinya nggak pernah bernilai",
                    "benar.",
                    "",
                    "NULL menular",
                    "",
                    "NULL ikut menular ke seluruh ekspresi yang menyentuhnya:",
                    "  NULL + 1               -> NULL",
                    "  harga * NULL           -> NULL",
                    "  'Hai ' || NULL         -> NULL   (penggabungan teks ikut hangus)",
                    "  CONCAT('Hai ', NULL)   -> NULL di MySQL; PostgreSQL malah mengabaikannya",
                    "",
                    "Satu kolom kosong aja udah cukup bikin seluruh kolom hasil jadi kosong.",
                    "Ini penyebab paling umum kolom \"alamat lengkap\" tiba-tiba kosong di",
                    "laporan. Padahal jalan, kota, dan provinsinya terisi, cuma RT-nya yang",
                    "kosong. Cara menambalnya: pakai CONCAT_WS di MySQL, atau COALESCE di",
                    "tiap potongannya.",
                    "",
                    "Agregat malah mengabaikan NULL",
                    "",
                    "Fungsi agregat, yaitu fungsi yang merangkum banyak baris jadi satu",
                    "angka, justru kebalikannya. AVG(ipk) menjumlahkan nilai yang terisi,",
                    "lalu membaginya dengan jumlah nilai yang terisi, bukan dengan jumlah",
                    "baris. Misalnya ada 4 baris, dan satu ipk-nya NULL:",
                    "  AVG(ipk)             -> dibagi 3",
                    "  SUM(ipk) / COUNT(*)  -> dibagi 4, hasilnya BEDA dan hampir selalu salah",
                    "",
                    "COUNT(*) menghitung baris, sedangkan COUNT(ipk) cuma menghitung yang",
                    "nggak NULL. Fungsi agregat dibahas lengkap di materi Agregasi &",
                    "Grouping.",
                    "",
                    "Jebakan: NOT IN yang daftarnya berisi NULL. Kesalahan ini nggak",
                    "kelihatan sama sekali:",
                    "  SELECT nama FROM mahasiswa",
                    "  WHERE nim NOT IN (SELECT wali_id FROM mahasiswa);",
                    "",
                    "Kalau ada satu aja wali_id yang NULL, query ini selalu mengembalikan nol",
                    "baris, apa pun isi tabelnya. Sebabnya, NOT IN (a, b, NULL) dijabarkan",
                    "jadi:",
                    "  nim <> a AND nim <> b AND nim <> NULL",
                    "",
                    "Bagian terakhir hasilnya unknown, jadi rangkaian AND-nya nggak pernah",
                    "bisa benar. IN biasa nggak kena masalah ini, cuma NOT IN. Cara",
                    "memperbaikinya: saring dulu pakai WHERE wali_id IS NOT NULL, atau pakai",
                    "NOT EXISTS yang memang kebal NULL.",
                    "",
                    "Menambal NULL",
                    "",
                    "Ada beberapa fungsi untuk mengganti NULL dengan nilai lain:",
                    "  COALESCE(a, b, c) -> ambil nilai pertama yang bukan NULL. Standar, ada",
                    "                       di semua database. Pakai ini kalau ragu.",
                    "  IFNULL(a, b)      -> versi dua argumen di MySQL & SQLite.",
                    "  ISNULL(a, b)      -> nama yang sama persis di SQL Server. Hati-hati:",
                    "                       ISNULL(x) di MySQL artinya lain (mengembalikan 1/0).",
                    "  NVL(a, b)         -> milik Oracle.",
                    "  NULLIF(a, b)      -> kebalikannya: hasilnya NULL kalau a sama dengan b.",
                    "",
                    "NULLIF paling berguna untuk menghindari pembagian dengan nol:",
                    "  SELECT total / NULLIF(jumlah, 0) FROM laporan;",
                    "",
                    "Hasilnya NULL (sel kosong), dan query-nya nggak gagal di tengah jalan.",
                    "",
                    "Pola yang muncul di hampir tiap laporan:",
                    "  COALESCE(SUM(nilai), 0)",
                    "",
                    "LEFT JOIN membiarkan sisi kanan kosong untuk baris yang nggak punya",
                    "pasangan. SUM dari nol baris hasilnya NULL, bukan 0. COALESCE menutup",
                    "lubang itu, jadi laporan menampilkan angka 0 dan nggak ada sel kosong",
                    "yang bikin orang bingung. LEFT JOIN dibahas di materi JOIN.",
                ],
            },
            {
                "body": [
                    "CASE adalah satu-satunya cara menulis logika if-else di dalam sebuah",
                    "query. Pakai CASE, kamu bisa mengubah kode angka jadi keterangan,",
                    "mengelompokkan nilai jadi kategori, dan memperlakukan tiap baris secara",
                    "berbeda. Semuanya tanpa query kedua.",
                    "",
                    "Bentuk pencarian (searched CASE)",
                    "",
                    "Bentuk ini yang paling sering dipakai:",
                    "  CASE",
                    "      WHEN ipk >= 3.5 THEN 'Cumlaude'",
                    "      WHEN ipk >= 3.0 THEN 'Baik'",
                    "      ELSE 'Biasa'",
                    "  END",
                    "",
                    "Tiap WHEN berisi kondisi utuh, sebebas isi WHERE. Kondisinya diperiksa",
                    "dari atas ke bawah, dan yang pertama cocok langsung dipakai. Sisanya",
                    "nggak dilihat lagi. Jadi urutannya menentukan hasil. Kalau WHEN ipk >=",
                    "3.0 ditulis lebih dulu, mahasiswa ber-IPK 3.8 ikut dapat label 'Baik',",
                    "dan label 'Cumlaude' nggak bakal muncul untuk siapa pun.",
                    "",
                    "Bentuk sederhana (simple CASE)",
                    "",
                    "Di bentuk ini, satu kolom dibandingkan dengan beberapa nilai:",
                    "  CASE status",
                    "      WHEN 1 THEN 'Aktif'",
                    "      WHEN 2 THEN 'Cuti'",
                    "      ELSE 'Tidak diketahui'",
                    "  END",
                    "",
                    "Bentuk ini cuma bisa mengecek kesamaan. Kalau butuh >, <, LIKE, atau",
                    "BETWEEN, pakai bentuk pencarian.",
                    "",
                    "Di balik layar, bentuk sederhana memakai tanda =. Akibatnya, baris yang",
                    "kolomnya NULL nggak pernah cocok dengan WHEN mana pun dan selalu jatuh",
                    "ke ELSE. Alasannya sama dengan logika tiga nilai tadi. Kalau NULL perlu",
                    "keterangan sendiri, pakai bentuk pencarian dan tulis WHEN kolom IS NULL.",
                    "",
                    "CASE itu ekspresi",
                    "",
                    "CASE adalah ekspresi, bukan perintah. Artinya CASE menghasilkan satu",
                    "nilai, jadi boleh dipakai di mana pun sebuah nilai boleh ditulis:",
                    "  SELECT   CASE ... END AS predikat",
                    "  WHERE    CASE ... END = 'Cumlaude'",
                    "  ORDER BY CASE WHEN ipk IS NULL THEN 1 ELSE 0 END, ipk DESC",
                    "  GROUP BY CASE ... END",
                    "  SUM(CASE WHEN ipk >= 3.5 THEN 1 ELSE 0 END)",
                    "  UPDATE produk SET kategori = CASE ... END",
                    "",
                    "Pola SUM(CASE ...) di atas sering kepakai. Dengan pola ini, kamu bisa",
                    "menghitung \"berapa yang memenuhi syarat\" bersebelahan dengan COUNT(*)",
                    "dalam satu query. Kalau pakai WHERE, kamu terpaksa menjalankan dua",
                    "query, lalu menggabungkan hasilnya sendiri di luar database.",
                    "",
                    "Karena CASE bukan perintah, CASE juga nggak bisa memilih perintah mana",
                    "yang dijalankan. Nggak ada bentuk 'CASE WHEN ... THEN DELETE'.",
                    "Percabangan seperti itu ditulis di stored procedure (IF ... THEN) atau",
                    "di kode aplikasi.",
                    "",
                    "Jebakan: ELSE yang lupa ditulis. Baris yang nggak cocok dengan WHEN mana",
                    "pun nggak error dan nggak dilewati. Hasilnya NULL. Kolom laporan",
                    "tiba-tiba kosong tanpa tanda apa-apa. Kalau NULL itu ikut dihitung lagi,",
                    "dia menular seperti yang udah dijelaskan tadi. Biasakan selalu menulis",
                    "ELSE, walaupun isinya cuma 'Lainnya'.",
                    "",
                    "Sisanya soal bentuk. END wajib ada, tiap WHEN wajib punya THEN, dan",
                    "semua THEN sebaiknya menghasilkan tipe yang sama. Kalau lupa END,",
                    "database biasanya mengeluh soal sintaks di baris yang jauh di bawahnya.",
                    "Jadi kalau pesan error-nya terasa nggak nyambung, cek dulu apakah ada",
                    "CASE yang belum ditutup.",
                ],
            },
            {
                "heading": "NULL & CASE dalam satu tabel",
                "code": """CREATE TABLE mahasiswa (
    nim     INTEGER PRIMARY KEY,
    nama    VARCHAR(50),
    ipk     DECIMAL(3,2),
    wali_id INT
);

INSERT INTO mahasiswa VALUES
(101, 'Andi',  3.50,  201),
(102, 'Budi',  2.90, NULL),
(103, 'Citra', NULL,  201),
(104, 'Dewi',  3.80,  202);

-- 1. Salah: perbandingan dengan NULL tak pernah benar -> 0 baris, tanpa error.
SELECT nama FROM mahasiswa WHERE ipk = NULL;

-- 2. Benar: hanya Citra yang keluar.
SELECT nama FROM mahasiswa WHERE ipk IS NULL;

-- 3. NULL menular ke seluruh ekspresi. Baris Citra kosong di semua kolom.
SELECT nama, ipk, ipk + 1 AS tambah, ipk * 2 AS kali FROM mahasiswa;

-- 4. Agregat MENGABAIKAN NULL: AVG membagi 3, hitungan manual membagi 4.
SELECT COUNT(*)                      AS baris,          -- 4
       COUNT(ipk)                    AS ipk_terisi,     -- 3
       ROUND(AVG(ipk), 2)            AS rata_avg,       -- 3.4
       ROUND(SUM(ipk) / COUNT(*), 2) AS rata_manual     -- 2.55 (salah)
FROM mahasiswa;

-- 5. NOT IN yang daftarnya memuat NULL: nol baris, selamanya.
SELECT nama FROM mahasiswa
WHERE nim NOT IN (SELECT wali_id FROM mahasiswa);

-- 6. Perbaikannya: buang NULL-nya lebih dulu -> keempat nama muncul.
SELECT nama FROM mahasiswa
WHERE nim NOT IN (SELECT wali_id FROM mahasiswa WHERE wali_id IS NOT NULL);

-- 7. COALESCE memberi nilai cadangan; NULLIF justru membuat NULL.
SELECT nama,
       COALESCE(ipk, 0)     AS ipk_aman,
       COALESCE(wali_id, 0) AS wali_aman,
       NULLIF(ipk, 3.50)    AS bukan_350
FROM mahasiswa;

-- 8. CASE bentuk pencarian: WHEN diperiksa berurutan, yang pertama cocok menang.
SELECT nama, ipk,
       CASE
           WHEN ipk IS NULL THEN 'Belum ada nilai'
           WHEN ipk >= 3.50 THEN 'Cumlaude'
           WHEN ipk >= 3.00 THEN 'Baik'
           ELSE                  'Biasa'
       END AS predikat
FROM mahasiswa;

-- 9. CASE bentuk sederhana. Budi (wali_id NULL) jatuh ke ELSE, bukan ke WHEN.
SELECT nama,
       CASE wali_id
           WHEN 201 THEN 'Bu Sari'
           WHEN 202 THEN 'Pak Joko'
           ELSE 'Belum punya wali'
       END AS dosen_wali
FROM mahasiswa;

-- 10. ELSE yang lupa ditulis -> baris tak cocok jadi NULL, bukan error.
SELECT nama, CASE WHEN ipk >= 3.50 THEN 'Cumlaude' END AS predikat
FROM mahasiswa;

-- 11. CASE di dalam agregat: hitung bersyarat tanpa query kedua.
SELECT COUNT(*) AS total,
       SUM(CASE WHEN ipk >= 3.50 THEN 1 ELSE 0 END) AS jumlah_cumlaude
FROM mahasiswa;

-- 12. CASE di ORDER BY: yang belum punya nilai didorong ke paling bawah.
SELECT nama, ipk FROM mahasiswa
ORDER BY CASE WHEN ipk IS NULL THEN 1 ELSE 0 END, ipk DESC;""",
            },
        ],
    },
    {
        "title": "8. Agregasi & Grouping",
        "sections": [
            {
                "body": [
                    "Fungsi agregat meringkas banyak baris jadi satu nilai. Misalnya \"ada",
                    "berapa mahasiswa?\" atau \"berapa rata-rata IPK-nya?\". Lima yang paling",
                    "sering dipakai:",
                    "",
                    "  COUNT(kolom)  -> jumlah baris",
                    "  SUM(kolom)    -> total penjumlahan",
                    "  AVG(kolom)    -> rata-rata",
                    "  MIN(kolom)    -> nilai terkecil",
                    "  MAX(kolom)    -> nilai terbesar",
                    "",
                    "Contohnya:",
                    "  SELECT COUNT(*) FROM mahasiswa;         -- 7",
                    "  SELECT AVG(ipk) FROM mahasiswa;         -- rata-rata ipk",
                    "  SELECT MAX(ipk), MIN(ipk) FROM mahasiswa;",
                    "  SELECT SUM(sks) FROM mata_kuliah;",
                    "",
                    "COUNT punya tiga bentuk, dan hasilnya bisa beda:",
                    "  - COUNT(*) menghitung semua baris.",
                    "  - COUNT(kolom) melewati baris yang kolomnya NULL.",
                    "  - COUNT(DISTINCT kolom) menghitung nilai yang berbeda saja, jadi nilai",
                    "    kembar dihitung sekali.",
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
                    "WHERE dan HAVING sama-sama menyaring, tapi waktunya beda:",
                    "  - WHERE menyaring baris sebelum dikelompokkan.",
                    "  - HAVING menyaring hasil agregat sesudah GROUP BY.",
                    "",
                    "Contoh yang memakai keduanya:",
                    "  SELECT jurusan, AVG(ipk)",
                    "  FROM mahasiswa",
                    "  WHERE angkatan >= 2022     -- filter baris dulu",
                    "  GROUP BY jurusan",
                    "  HAVING AVG(ipk) > 3.0;     -- filter hasil grup",
                    "",
                    "Urutan menulis klausa SELECT harus begini:",
                    "  SELECT  kolom, agregat",
                    "  FROM    tabel",
                    "  WHERE   filter baris",
                    "  GROUP BY kolom",
                    "  HAVING  filter agregat",
                    "  ORDER BY kolom",
                    "  LIMIT   jumlah;",
                    "",
                    "Tapi urutan database mengerjakannya (secara logika) lain lagi:",
                    "  FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT",
                ]
            },
            {
                "heading": "Aturan GROUP BY yang wajib dipatuhi",
                "body": [
                    "Aturannya cuma satu: setiap kolom di SELECT yang nggak dibungkus fungsi",
                    "agregat wajib ikut disebut di GROUP BY. Kalau nggak, database nggak",
                    "punya cara memilih nilai mana yang ditampilkan dari sekian baris di satu",
                    "grup.",
                    "",
                    "  X  SELECT jurusan, nama, AVG(ipk) FROM mahasiswa GROUP BY jurusan;",
                    "     -- nama siapa? satu grup berisi tiga nama.",
                    "",
                    "PostgreSQL menolak query itu dengan pesan:",
                    "  column \"mahasiswa.nama\" must appear in the GROUP BY clause or be",
                    "  used in an aggregate function",
                    "",
                    "MySQL 5.7 ke atas juga menolak, dengan pesan yang mirip:",
                    "  ... is not in GROUP BY clause and contains nonaggregated column ...",
                    "",
                    "SQLite dan MySQL versi lama malah nggak protes. Mereka memilih satu",
                    "nilai sembarang dari grup itu. Akibatnya query yang sama bisa lolos di",
                    "laptopmu, lalu ditolak di server. Yang benar adalah yang menolak.",
                    "",
                    "GROUP BY boleh pakai lebih dari satu kolom. Grupnya dibentuk dari",
                    "kombinasi nilai semua kolom yang disebut:",
                    "",
                    "  SELECT p.nama, k.nama, SUM(pn.jumlah) AS total",
                    "  FROM produk p",
                    "  JOIN penjualan pn ON p.id = pn.produk_id",
                    "  JOIN kategori k ON p.kategori_id = k.id",
                    "  GROUP BY p.id, p.nama, k.nama;",
                    "",
                    "Kolom p.id ikut disebut supaya dua produk yang kebetulan namanya sama",
                    "nggak dilebur jadi satu baris. Latihan 8 meminta bentuk seperti ini.",
                    "",
                    "Alias yang dibikin di SELECT boleh dipakai di ORDER BY, tapi nggak boleh",
                    "di WHERE. Alasannya ada di urutan kerja database tadi. WHERE dikerjakan",
                    "sebelum SELECT, jadi waktu WHERE dicek, aliasnya belum ada. ORDER BY",
                    "dikerjakan sesudah SELECT, jadi di sana aliasnya udah ada.",
                    "",
                    "  V  SELECT jurusan, AVG(ipk) AS rata FROM mahasiswa",
                    "     GROUP BY jurusan ORDER BY rata DESC;",
                    "  X  SELECT jurusan, AVG(ipk) AS rata FROM mahasiswa",
                    "     WHERE rata > 3 GROUP BY jurusan;",
                    "",
                    "Untuk menyaring hasil agregat, tempatnya di HAVING, jangan di WHERE.",
                ]
            },
            {
                "heading": "LIMIT & OFFSET: mengambil hasil per halaman",
                "body": [
                    "LIMIT udah muncul di urutan klausa tadi, tapi belum dijelaskan. LIMIT",
                    "membatasi jumlah baris hasil. OFFSET melewati sekian baris pertama",
                    "sebelum dibatasi. Keduanya dipakai untuk menampilkan data per halaman:",
                    "",
                    "  SELECT nama, ipk FROM mahasiswa ORDER BY ipk DESC LIMIT 10;",
                    "  -- sepuluh teratas: halaman 1",
                    "",
                    "  SELECT nama, ipk FROM mahasiswa ORDER BY ipk DESC LIMIT 10 OFFSET 10;",
                    "  -- lewati 10, ambil 10 berikutnya: baris ke-11 sampai ke-20",
                    "",
                    "Rumusnya: OFFSET = (nomor_halaman - 1) * isi_per_halaman.",
                    "",
                    "MySQL punya bentuk singkat yang urutan angkanya kebalikan dari dugaan",
                    "orang:",
                    "  LIMIT 40, 20   -- lewati 40, ambil 20",
                    "",
                    "Angka pertama itu OFFSET, angka kedua jumlah baris. Jadi bentuk itu sama",
                    "dengan LIMIT 20 OFFSET 40. Bentuk panjang LIMIT 20 OFFSET 40 jalan di",
                    "MySQL, PostgreSQL, dan SQLite sekaligus, jadi biasakan pakai yang",
                    "panjang.",
                    "",
                    "Jebakan: OFFSET tanpa ORDER BY hasilnya nggak stabil. Database nggak",
                    "wajib mengembalikan baris dengan urutan yang sama tiap kali. Akibatnya",
                    "satu baris bisa muncul di halaman 1 dan halaman 2 sekaligus, sementara",
                    "baris lain nggak pernah muncul. Jadi setiap query yang dibagi per",
                    "halaman wajib punya ORDER BY, dan urutannya harus pasti. Kalau kolom",
                    "pengurutnya bisa punya nilai kembar, tambahkan kolom unik seperti id",
                    "sebagai penentu urutan.",
                ]
            },
            {
                "heading": "Menghitung sub-kelompok & merujuk kolom lewat nomor",
                "body": [
                    "Di materi Ekspresi, NULL & CASE kamu udah kenal SUM(CASE WHEN ... THEN 1",
                    "ELSE 0 END). Pola itu paling sering dipakai di sini, bareng GROUP BY.",
                    "Ada dua bentuk lain yang perlu kamu kenali waktu membaca query laporan.",
                    "",
                    "Yang pertama, COUNT(CASE WHEN ... THEN 1 END), tanpa ELSE. ELSE-nya",
                    "memang sengaja nggak ditulis. CASE tanpa ELSE menghasilkan NULL, dan",
                    "COUNT melewati NULL. Hasilnya sama dengan SUM(CASE ... ELSE 0 END):",
                    "",
                    "  SELECT jurusan,",
                    "         COUNT(*) AS total,",
                    "         SUM(CASE WHEN ipk >= 3.5 THEN 1 ELSE 0 END) AS jml_unggul,",
                    "         COUNT(CASE WHEN ipk < 3.0 THEN 1 END)       AS jml_dibantu",
                    "  FROM mahasiswa",
                    "  GROUP BY jurusan;",
                    "",
                    "Yang kedua, FILTER. PostgreSQL dan SQLite 3.30 ke atas punya bentuk",
                    "modern yang lebih gampang dibaca:",
                    "  COUNT(*)   FILTER (WHERE ipk >= 3.5)        AS jml_unggul",
                    "  SUM(total) FILTER (WHERE status = 'lunas')  AS pendapatan_lunas",
                    "",
                    "MySQL belum punya FILTER, jadi di sana tetap pakai CASE.",
                    "",
                    "GROUP BY dan ORDER BY juga menerima nomor posisi kolom di SELECT:",
                    "",
                    "  SELECT jurusan, COUNT(*) FROM mahasiswa GROUP BY 1 ORDER BY 2 DESC;",
                    "",
                    "Angka 1 artinya kolom pertama di daftar SELECT (jurusan), dan 2 artinya",
                    "kolom kedua (COUNT(*)). Angka itu bukan nilai 1 dan 2. Bentuk ini",
                    "dipakai supaya ekspresi panjang nggak perlu ditulis dua kali.",
                    "Masalahnya, kalau urutan kolom di SELECT diubah, query-nya tetap jalan,",
                    "tapi hasilnya ikut berubah tanpa peringatan apa pun.",
                ]
            },
        ],
    },
    {
        "title": "9. JOIN: Menghubungkan Tabel",
        "sections": [
            {
                "body": [
                    "JOIN menggabungkan data dari dua tabel atau lebih. Penggabungannya",
                    "berdasarkan kolom yang berhubungan, biasanya kolom kunci. Misalnya tabel",
                    "nilai cuma nyimpen nim. Supaya nama mahasiswanya ikut tampil, tabel",
                    "nilai di-JOIN dengan tabel mahasiswa lewat kolom nim.",
                    "",
                    "Ada lima jenis JOIN:",
                    "  INNER JOIN -> hanya baris yang cocok di kedua tabel.",
                    "  LEFT JOIN  -> semua baris tabel kiri + yang cocok di kanan.",
                    "  RIGHT JOIN -> semua baris tabel kanan + yang cocok di kiri.",
                    "  FULL OUTER JOIN -> semua baris kedua sisi (MySQL tidak punya).",
                    "  CROSS JOIN -> semua kombinasi baris.",
                    "",
                    "Kalau digambar, INNER JOIN cuma mengambil bagian yang ada di kedua",
                    "tabel:",
                    "  [A]====[B]  hanya irisan yang muncul.",
                    "",
                    "LEFT JOIN mengambil semua baris A. Baris B yang nggak punya pasangan di",
                    "A nggak ikut, dan baris A yang nggak punya pasangan di B diisi NULL di",
                    "kolom-kolom B:",
                    "  [A]----->  semua A, irisan B. B yang tak cocok jadi NULL.",
                    "",
                    "Bentuk umumnya:",
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
                "heading": "ON, USING & nama panjang yang bukan jenis baru",
                "body": [
                    "Kalau kolom penghubungnya punya nama yang sama di kedua tabel, ON boleh",
                    "dipendekkan jadi USING:",
                    "",
                    "  FROM nilai n JOIN mahasiswa m ON n.nim = m.nim",
                    "  FROM nilai n JOIN mahasiswa m USING (nim)     -- maksud yang sama",
                    "",
                    "Bedanya nggak cuma soal panjang tulisan. Dengan USING, kolom penghubung",
                    "muncul sekali aja di hasil. Dengan ON, kolom itu muncul dua kali (n.nim",
                    "dan m.nim). Jadi SELECT * dari dua query itu menghasilkan jumlah kolom",
                    "yang beda. Sesudah USING, kolom itu juga ditulis polos: SELECT nim,",
                    "bukan n.nim. USING ada di MySQL, PostgreSQL, dan SQLite. SQL Server",
                    "nggak punya.",
                    "",
                    "NATURAL JOIN lebih jauh lagi. Dia menebak sendiri kolom penghubungnya,",
                    "yaitu semua kolom yang kebetulan namanya sama di kedua tabel:",
                    "",
                    "  SELECT * FROM nilai NATURAL JOIN mahasiswa;",
                    "",
                    "Hindari NATURAL JOIN di kode produksi. Misalnya kamu menambah kolom",
                    "created_at ke kedua tabel. Kolom itu otomatis ikut jadi syarat",
                    "penggabungan. Query yang kemarin benar, hari ini mengembalikan nol",
                    "baris, tanpa satu pun pesan error. Tulis ON atau USING supaya syaratnya",
                    "kelihatan jelas.",
                    "",
                    "Ada nama-nama panjang yang sering dikira jenis JOIN tersendiri. Padahal",
                    "artinya persis sama dengan versi pendeknya. Kode gaya lama biasanya",
                    "menulis yang panjang:",
                    "  JOIN       = INNER JOIN        (INNER boleh dihilangkan)",
                    "  LEFT JOIN  = LEFT OUTER JOIN   (OUTER boleh dihilangkan)",
                    "  RIGHT JOIN = RIGHT OUTER JOIN",
                    "  FULL JOIN  = FULL OUTER JOIN",
                ]
            },
            {
                "heading": "COALESCE pada LEFT JOIN & CROSS JOIN",
                "code": """-- LEFT JOIN membuat kolom sisi kanan jadi NULL untuk baris yang tidak
-- punya pasangan. Di laporan, NULL itu biasanya lebih enak dibaca sebagai 0.
SELECT m.nama,
       COALESCE(n.skor, 0)    AS skor,
       COALESCE(mk.nama, '-') AS matkul
FROM mahasiswa m
LEFT JOIN nilai n ON m.nim = n.nim
LEFT JOIN mata_kuliah mk ON n.kode = mk.kode
ORDER BY m.nama;

-- Hati-hati: yang dibungkus COALESCE adalah AGREGATNYA, bukan kolomnya.
-- SUM mengabaikan NULL lalu mengembalikan NULL kalau tak ada satu pun baris.
SELECT m.nama, COALESCE(SUM(n.skor), 0) AS total_skor
FROM mahasiswa m
LEFT JOIN nilai n ON m.nim = n.nim
GROUP BY m.nama;

-- CROSS JOIN: setiap baris kiri dipasangkan dengan SETIAP baris kanan.
-- Tidak ada ON sama sekali. 7 mahasiswa x 3 mata kuliah = 21 baris.
SELECT m.nama, mk.nama AS matkul
FROM mahasiswa m
CROSS JOIN mata_kuliah mk
ORDER BY m.nama, mk.nama;

-- Gunanya: membuat kerangka lengkap 'semua kombinasi yang SEHARUSNYA ada',
-- lalu di-LEFT JOIN ke data nyata untuk menemukan yang belum terisi.
-- Query ini menjawab: siapa belum mengambil mata kuliah apa?
SELECT m.nama, mk.nama AS matkul
FROM mahasiswa m
CROSS JOIN mata_kuliah mk
LEFT JOIN nilai n ON n.nim = m.nim AND n.kode = mk.kode
WHERE n.nim IS NULL
ORDER BY m.nama, mk.nama;

-- JEBAKAN: CROSS JOIN juga terjadi TANPA SENGAJA kalau ON-nya lupa ditulis
-- (gaya lama: FROM a, b tanpa WHERE). Seribu kali seribu = sejuta baris."""
            },
            {
                "body": [
                    "Self join artinya sebuah tabel digabung dengan dirinya sendiri.",
                    "Contohnya tabel karyawan yang punya kolom atasan_id. Atasan juga",
                    "karyawan, jadi datanya ada di tabel yang sama:",
                    "  -- Contoh: relasi karyawan - atasan",
                    "  SELECT k.nama AS karyawan, a.nama AS atasan",
                    "  FROM karyawan k",
                    "  LEFT JOIN karyawan a ON k.atasan_id = a.id;",
                    "",
                    "Huruf k dan a di situ adalah alias tabel. Alias tabel itu singkatan nama",
                    "tabel, seperti m, n, dan mk di contoh sebelumnya, supaya query lebih",
                    "pendek. Di self join, alias wajib dipakai supaya database tahu \"salinan\"",
                    "tabel mana yang kamu maksud.",
                    "",
                    "Cara membaca dan menyusun JOIN:",
                    "  1. Tentukan kolom apa saja yang mau ditampilkan.",
                    "  2. Cari tahu kolom-kolom itu ada di tabel mana.",
                    "  3. Temukan kolom penghubung antar tabel itu.",
                    "  4. Mulai dari tabel utama, lalu gabungkan tabel lain satu per satu.",
                ]
            },
        ],
    },
    {
        "title": "10. Subquery & Fungsi Lanjutan",
        "sections": [
            {
                "body": [
                    "Subquery adalah query di dalam query. Query yang di dalam dijalankan",
                    "untuk menghasilkan sesuatu, lalu hasilnya dipakai oleh query utama.",
                    "",
                    "Subquery biasanya dipakai untuk:",
                    "  - mencari baris dengan nilai terbesar, lengkap dengan data lainnya,",
                    "  - menyaring baris pakai hasil fungsi agregat,",
                    "  - memakai hasil sebuah query sebagai bahan query lain.",
                    "",
                    "Subquery yang mengembalikan satu nilai disebut scalar subquery. Contoh",
                    "ini mencari mahasiswa dengan IPK tertinggi:",
                    "  SELECT nama, ipk FROM mahasiswa",
                    "  WHERE ipk = (SELECT MAX(ipk) FROM mahasiswa);",
                    "",
                    "Subquery juga bisa mengembalikan daftar nilai, lalu dipakai bareng IN.",
                    "Contoh ini mencari mahasiswa yang pernah dapat skor di atas 90:",
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
                    "Fungsi untuk mengolah teks (string):",
                    "  CONCAT(a, b)      -> gabung teks",
                    "  UPPER(teks)       -> huruf besar",
                    "  LOWER(teks)       -> huruf kecil",
                    "  LENGTH(teks)      -> panjang teks",
                    "  SUBSTRING(teks, mulai, panjang) -> potong teks",
                    "  REPLACE(teks, a, b) -> ganti 'a' jadi 'b'",
                    "  TRIM(teks)        -> buang spasi ujung",
                    "",
                    "Fungsi untuk tanggal (ejaan MySQL):",
                    "  NOW()             -> tanggal & jam sekarang",
                    "  CURDATE()         -> tanggal sekarang",
                    "  YEAR(tanggal), MONTH(tanggal), DAY(tanggal)",
                    "  DATEDIFF(a, b)    -> selisih hari",
                    "  DATE_FORMAT(t, '%d-%m-%Y') -> format tanggal",
                    "",
                    "Contohnya, menggabungkan nama dan jurusan jadi satu kolom:",
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
        "title": "11. Fungsi Teks, Tanggal & Agregat Teks",
        "sections": [
            {
                "body": [
                    "Di materi Subquery & Fungsi Lanjutan kamu udah kenal CONCAT(), UPPER(),",
                    "SUBSTRING(), NOW(), dan DATEDIFF(). Yang belum dibahas: tiap database",
                    "punya cara sendiri untuk pekerjaan yang persis sama. Kode nyata yang",
                    "kamu baca bisa pakai bentuk mana pun, jadi kamu perlu bisa mengenali",
                    "semuanya.",
                    "",
                    "Menyambung teks",
                    "",
                    "Ada tiga cara, tergantung database-nya:",
                    "  ||        Standar SQL. Jalan di PostgreSQL, SQLite, Oracle, DB2.",
                    "  CONCAT()  MySQL, PostgreSQL 9.1+, SQL Server 2012+, SQLite 3.44+.",
                    "  +         SQL Server.",
                    "",
                    "  -- PostgreSQL/SQLite",
                    "  SELECT nama_depan || ' ' || nama_belakang FROM pelanggan;",
                    "  -- hampir di mana saja",
                    "  SELECT CONCAT(nama_depan, ' ', nama_belakang) FROM pelanggan;",
                    "",
                    "Jebakan: di SQL, || bukan OR. Kalau kamu datang dari Java atau",
                    "JavaScript, mata kamu bakal membaca a || b sebagai \"a atau b\". Di SQL",
                    "standar, artinya \"a disambung b\". Lebih bikin pusing lagi, di MySQL",
                    "bawaan || memang berarti OR, kecuali sql_mode PIPES_AS_CONCAT",
                    "dinyalakan. Jadi query yang sama menghasilkan angka 0 atau 1 di MySQL,",
                    "tapi menghasilkan kalimat di PostgreSQL. Nggak ada pesan error yang",
                    "ngasih tahu.",
                    "",
                    "Masalah kedua: satu NULL merusak seluruh hasil sambungan.",
                    "  'Andi' || NULL        -> NULL   (bukan 'Andi')",
                    "  CONCAT('Andi', NULL)  -> NULL   di MySQL (CONCAT PostgreSQL melewati NULL)",
                    "",
                    "Pengecualiannya Oracle, yang memperlakukan NULL sebagai teks kosong.",
                    "Akibatnya, satu kolom kosong bikin seluruh kolom hasil jadi kosong,",
                    "nggak cuma bagian kolom itu. Tambal pakai COALESCE(kolom, '') sebelum",
                    "disambung.",
                    "",
                    "CONCAT_WS('pemisah', a, b, c) adalah cara lain. WS artinya With",
                    "Separator, yaitu dengan pemisah. Pemisahnya ditulis sekali di depan,",
                    "lalu otomatis disisipkan di antara tiap bagian. Yang paling penting,",
                    "CONCAT_WS melewati argumen NULL, nggak ikut jadi NULL:",
                    "  CONCAT_WS(', ', 'Bandung', NULL, 'Jawa Barat')  -> 'Bandung, Jawa Barat'",
                    "",
                    "Tapi kalau pemisahnya sendiri NULL, hasilnya tetap NULL (di MySQL). Teks",
                    "kosong '' juga nggak dilewati, jadi hasilnya tetap punya pemisah dobel.",
                ],
            },
            {
                "heading": "Coba sendiri: fungsi teks yang jalan apa adanya di sqlite3",
                "code": """CREATE TABLE pelanggan (
    id            INTEGER PRIMARY KEY,
    nama_depan    TEXT,
    nama_belakang TEXT,
    kota          TEXT,
    email         TEXT
);

INSERT INTO pelanggan VALUES
(1, 'Andi',  'Saputra', 'Bandung',  'andi.s@contoh.id'),
(2, 'Budi',  NULL,      'Surabaya', 'BUDI@Contoh.ID'),
(3, 'Citra', 'Halim',   'Bandung',  'citra_h@contoh.id');

.mode column
.headers on

-- Sambung dengan || : baris 2 keluar KOSONG karena nama_belakang-nya NULL
SELECT id, nama_depan || ' ' || nama_belakang AS nama_lengkap FROM pelanggan;

-- COALESCE menambal lubang NULL itu, trim membuang sisa spasinya
SELECT id, trim(nama_depan || ' ' || COALESCE(nama_belakang, '')) AS nama_lengkap
FROM pelanggan;

-- Cari posisi sebuah karakter, lalu potong kiri & kanan dari posisi itu
SELECT email,
       instr(email, '@')                       AS posisi_at,
       substr(email, 1, instr(email, '@') - 1) AS bagian_user,
       substr(email, instr(email, '@') + 1)    AS domain
FROM pelanggan;

-- Nomor rata kanan berisi nol: LPAD di MySQL/PostgreSQL, printf di SQLite
SELECT printf('%04d', id) AS kode, upper(substr(kota, 1, 3)) AS singkatan
FROM pelanggan;

-- Perhatikan: di SQLite LIKE TIDAK peka huruf, jadi 'BUDI@Contoh.ID' ikut kena.
-- Di PostgreSQL baris ini tidak mengembalikan apa-apa.
SELECT nama_depan, email FROM pelanggan WHERE email LIKE '%budi%';

-- Bentuk yang berperilaku sama di semua database: turunkan dulu ke huruf kecil
SELECT nama_depan, email FROM pelanggan WHERE lower(email) LIKE '%budi%';

-- Agregat teks: banyak baris diringkas jadi satu kalimat
SELECT kota, COUNT(*) AS jumlah, group_concat(nama_depan, ', ') AS daftar
FROM pelanggan
GROUP BY kota;""",
            },
            {
                "body": [
                    "Banyak database pakai nama berbeda untuk pekerjaan yang sama. Yang perlu",
                    "kamu ingat adalah kebutuhannya. Nama fungsinya bisa dicari belakangan.",
                    "",
                    "Mencari posisi sebuah teks di dalam teks lain. Hasilnya angka, dan 0",
                    "artinya nggak ketemu:",
                    "  POSITION('@' IN email)  -> bentuk standar SQL (PostgreSQL, MySQL)",
                    "  STRPOS(email, '@')      -> PostgreSQL",
                    "  INSTR(email, '@')       -> MySQL, Oracle, SQLite",
                    "  CHARINDEX('@', email)   -> SQL Server",
                    "",
                    "Urutan argumen CHARINDEX kebalikan dari INSTR.",
                    "",
                    "Mengambil beberapa karakter dari ujung kiri atau kanan:",
                    "  LEFT(t, 3) dan RIGHT(t, 3)  -> PostgreSQL, MySQL, SQL Server",
                    "",
                    "SQLite dan Oracle nggak punya LEFT dan RIGHT. Di sana pakai substr(t,",
                    "1, 3) dan substr(t, -3).",
                    "",
                    "Menambah karakter sampai lebarnya pas, misalnya untuk nomor invoice,",
                    "kode barang, atau kolom laporan:",
                    "  LPAD('7', 4, '0') -> '0007'      RPAD('AB', 4, '.') -> 'AB..'",
                    "",
                    "LPAD dan RPAD ada di PostgreSQL, MySQL, dan Oracle. SQL Server dan",
                    "SQLite nggak punya. Padanannya FORMAT(7, '0000') di SQL Server dan",
                    "printf('%04d', 7) di SQLite.",
                    "",
                    "Memecah teks berdasarkan pemisah:",
                    "  SPLIT_PART('a,b,c', ',', 2)      -> 'b'     PostgreSQL",
                    "  SUBSTRING_INDEX('a,b,c', ',', 2) -> 'a,b'   MySQL",
                    "  STRING_SPLIT('a,b,c', ',')       -> tabel   SQL Server",
                    "",
                    "SUBSTRING_INDEX artinya beda dari dua yang lain. Fungsi ini mengambil n",
                    "bagian pertama, bukan bagian ke-n, dan sering salah dipakai karena itu.",
                    "",
                    "Mengubah huruf awal tiap kata jadi huruf besar:",
                    "  INITCAP('budi santoso') -> 'Budi Santoso'   (PostgreSQL, Oracle)",
                    "",
                    "MySQL, SQL Server, dan SQLite nggak punya fungsi ini. Biasanya teksnya",
                    "dirapikan di kode aplikasi.",
                    "",
                    "Pencarian yang nggak peduli huruf besar-kecil",
                    "",
                    "Bagian ini yang paling sering menipu. Tiap database punya kebiasaan",
                    "sendiri:",
                    "  PostgreSQL : LIKE PEKA huruf. Pakai ILIKE, atau LOWER(kolom) LIKE",
                    "  LOWER('%budi%').",
                    "  MySQL      : collation bawaannya _ci, jadi LIKE sudah TIDAK peka huruf.",
                    "  SQLite     : LIKE tidak peka huruf, tapi HANYA untuk A-Z",
                    "               (huruf beraksen tetap peka).",
                    "  SQL Server : tergantung collation databasenya.",
                    "",
                    "Collation adalah aturan database untuk membandingkan dan mengurutkan",
                    "teks. Akhiran _ci artinya case insensitive, yaitu nggak membedakan huruf",
                    "besar dan kecil.",
                    "",
                    "Akibatnya, query yang menemukan data di laptop bisa mengembalikan 0",
                    "baris di server, tanpa satu pun error. Kalau ragu, tulis LOWER(kolom).",
                    "Hasilnya jelas dan sama di semua database.",
                    "",
                    "Harganya, fungsi yang membungkus kolom bikin index nggak bisa dipakai",
                    "(dibahas di materi Roadmap). Solusinya index berbasis ekspresi:",
                    "  CREATE INDEX idx_email ON pelanggan (LOWER(email));",
                    "",
                    "Agregat teks",
                    "",
                    "Agregat teks mirip COUNT atau SUM, tapi hasilnya satu kalimat yang",
                    "disusun dari banyak baris:",
                    "  MySQL      : GROUP_CONCAT(nama ORDER BY nama SEPARATOR ', ')",
                    "  PostgreSQL : STRING_AGG(nama, ', ' ORDER BY nama)",
                    "  SQL Server : STRING_AGG(nama, ', ') WITHIN GROUP (ORDER BY nama)",
                    "  Oracle     : LISTAGG(nama, ', ') WITHIN GROUP (ORDER BY nama)",
                    "  SQLite     : group_concat(nama, ', ')",
                    "",
                    "Di SQLite, ORDER BY di dalam group_concat baru ada sejak versi 3.44.",
                    "",
                    "PostgreSQL juga punya ARRAY_AGG(nama). Hasilnya berupa array",
                    "{Andi,Citra}, bukan teks.",
                    "",
                    "Bentuknya memang nggak biasa. ORDER BY dan kata kunci SEPARATOR ditulis",
                    "di dalam kurung fungsi. Nggak ada fungsi lain yang begitu, dan SEPARATOR",
                    "di MySQL nggak didahului koma. Kalau baris itu kelihatan seperti salah",
                    "ketik, tenang aja, sintaksnya memang begitu.",
                    "",
                    "Jebakan: MySQL memotong hasil GROUP_CONCAT sampai batas",
                    "group_concat_max_len, yang bawaannya 1024 byte. Daftar yang panjang",
                    "terpotong, dan yang muncul cuma warning, bukan error. Laporannya",
                    "kelihatan wajar, padahal isinya kurang.",
                ],
            },
            {
                "heading": "Tanggal: nama yang sama sekali berbeda di tiap database",
                "body": [
                    "Waktu sekarang",
                    "",
                    "Ada beberapa nama untuk hal yang sama:",
                    "  CURRENT_TIMESTAMP  standar SQL, ada di hampir semua. Ditulis TANPA kurung.",
                    "  CURRENT_DATE       standar, tanggal saja tanpa jam.",
                    "  NOW()              MySQL & PostgreSQL.",
                    "  CURDATE()          MySQL saja.",
                    "  GETDATE()          SQL Server saja. Oracle memakai SYSDATE.",
                    "  datetime('now')    SQLite - dan ini UTC, bukan waktu lokal komputermu.",
                    "                     Waktu lokal: datetime('now', 'localtime').",
                    "",
                    "Kalau CURRENT_TIMESTAMP() ditulis pakai kurung, PostgreSQL menolaknya,",
                    "sedangkan MySQL menerimanya.",
                    "",
                    "Mengambil bagian dari tanggal",
                    "  EXTRACT(YEAR FROM tanggal)  bentuk standar. Hasilnya angka: 2024.",
                    "  YEAR(tanggal)               pintasan milik MySQL & SQL Server saja.",
                    "  DATE_TRUNC('month', t)      PostgreSQL: potong ke awal bulan.",
                    "  strftime('%Y-%m', t)        SQLite.  DATE_FORMAT(t, '%Y-%m') di MySQL.",
                    "",
                    "Kata FROM di EXTRACT ditulis di dalam kurung, dan nggak ada hubungannya",
                    "dengan klausa FROM tabel. DATE_TRUNC menghasilkan tanggal (2024-03-01),",
                    "bukan angka. Jadi hasilnya tetap urut dengan benar dan masih bisa",
                    "diformat. Cocok untuk laporan bulanan.",
                    "",
                    "Menggeser tanggal pakai INTERVAL",
                    "",
                    "INTERVAL itu literal, yaitu cara menulis nilai langsung, sama seperti",
                    "angka 30 atau teks 'abc'. Bedanya, nilai INTERVAL bertipe \"lama waktu\".",
                    "Karena bukan fungsi, INTERVAL nggak pernah pakai kurung:",
                    "  PostgreSQL : NOW() - INTERVAL '30 days'",
                    "  MySQL      : NOW() - INTERVAL 30 DAY",
                    "               DATE_SUB(NOW(), INTERVAL 7 DAY)",
                    "               DATE_ADD(t, INTERVAL 1 MONTH)",
                    "  SQL Server : DATEADD(DAY, -30, GETDATE())",
                    "  SQLite     : date(t, '-30 days')",
                    "",
                    "Di PostgreSQL, angka dan satuannya ditulis di dalam kutip. Di MySQL",
                    "nggak pakai kutip, dan satuannya berupa kata kunci berbentuk tunggal,",
                    "seperti DAY atau MONTH.",
                    "",
                    "Di MySQL, INTERVAL 30 DAYS (pakai bentuk jamak) bikin error sintaks.",
                    "PostgreSQL menerima dua-duanya.",
                    "",
                    "Selisih waktu",
                    "",
                    "Di sinilah tanda plus-minus paling gampang terbalik:",
                    "  MySQL      : DATEDIFF(a, b)       a dikurangi b, satuannya HARI.",
                    "  SQL Server : DATEDIFF(DAY, a, b)  b dikurangi a (tiga argumen).",
                    "  PostgreSQL : b - a langsung memberi interval.",
                    "               AGE(b, a) -> '1 year 2 mons 3 days'.",
                    "  SQLite     : julianday(b) - julianday(a).",
                    "",
                    "DATEDIFF di SQL Server pakai tiga argumen, dan arahnya terbalik dari",
                    "DATEDIFF di MySQL.",
                    "",
                    "Untuk umur atau lama langganan dalam tahun, jangan bagi jumlah hari",
                    "dengan 365. Tahun kabisat bikin hasilnya meleset sehari demi sehari.",
                    "Pakai fungsi yang sudah tersedia:",
                    "  MySQL      : TIMESTAMPDIFF(YEAR, tanggal_lahir, CURDATE())",
                    "  PostgreSQL : EXTRACT(YEAR FROM AGE(tanggal_lahir))",
                ],
                "code": """CREATE TABLE langganan (
    id             INTEGER PRIMARY KEY,
    nama           TEXT,
    tanggal_daftar TEXT,   -- SQLite tidak punya tipe DATE; wajib ISO 'YYYY-MM-DD'
    tanggal_akhir  TEXT
);

INSERT INTO langganan VALUES
(1, 'Andi',  '2023-11-05', '2024-11-05'),
(2, 'Budi',  '2024-01-20', '2024-07-20'),
(3, 'Citra', '2024-03-31', '2025-03-31');

.mode column
.headers on

-- Ambil bagian tanggal. Padanan di database lain:
--   EXTRACT(YEAR FROM t) standar  |  YEAR(t) MySQL  |  DATE_TRUNC('month', t) PostgreSQL
SELECT nama,
       strftime('%Y', tanggal_daftar)       AS tahun,
       strftime('%Y-%m', tanggal_daftar)    AS bulan,
       strftime('%d-%m-%Y', tanggal_daftar) AS tampilan_indonesia
FROM langganan;

-- Menggeser tanggal. Padanan INTERVAL: t + INTERVAL '1 month' (PostgreSQL),
-- DATE_ADD(t, INTERVAL 1 MONTH) (MySQL), DATEADD(MONTH, 1, t) (SQL Server).
SELECT nama,
       date(tanggal_daftar, '+30 days') AS tenggat_bayar,
       date(tanggal_daftar, '+1 month') AS perpanjangan,
       julianday(tanggal_akhir) - julianday(tanggal_daftar) AS lama_hari
FROM langganan;

-- Laporan bulanan: kelompokkan lewat hasil pemotongan, bukan lewat kolom mentahnya
SELECT strftime('%Y-%m', tanggal_daftar) AS bulan, COUNT(*) AS pendaftar
FROM langganan
GROUP BY bulan
ORDER BY bulan;

-- Rentang setengah terbuka: batas bawah ikut, batas atas tidak
SELECT nama FROM langganan
WHERE tanggal_daftar >= '2024-01-01' AND tanggal_daftar < '2025-01-01';

-- Jebakan: 31 Maret + 1 bulan. SQLite MELUBER ke 1 Mei karena 31 April tidak ada,
-- sedangkan MySQL & PostgreSQL MENJEPITnya ke 30 April. Jawabannya beda per database.
SELECT date('2024-03-31', '+1 month') AS sqlite_meluber;""",
            },
            {
                "body": [
                    "Ada tiga jebakan tanggal yang paling sering bikin pusing di kode nyata.",
                    "",
                    "Pertama: menyimpan tanggal sebagai teks bebas. Kolom VARCHAR berisi",
                    "'17/08/2024' kelihatan rapi, sampai kamu perlu melakukan hal-hal ini:",
                    "  - Mengurutkan. Sebagai teks, '05/09/2024' < '17/08/2024', jadi",
                    "    September muncul sebelum Agustus. Laporannya salah urut, dan nggak",
                    "    ada yang error.",
                    "  - Menghitung. DATEDIFF dan EXTRACT nggak mengerti teks itu.",
                    "  - Menjaga data tetap masuk akal. '2024-02-30' dan '17/8/24' sama-sama",
                    "    masuk tanpa protes.",
                    "",
                    "Pakai tipe DATE atau TIMESTAMP, lalu ubah formatnya cuma waktu",
                    "ditampilkan:",
                    "  MySQL       DATE_FORMAT(t, '%d-%m-%Y')",
                    "  PostgreSQL  TO_CHAR(t, 'DD-MM-YYYY')  huruf polanya beda, bukan salah ketik",
                    "  SQLite      strftime('%d-%m-%Y', t)",
                    "",
                    "SQLite pengecualiannya. SQLite memang nggak punya tipe DATE, semuanya",
                    "disimpan sebagai teks atau angka. Justru karena itu, format ISO",
                    "'YYYY-MM-DD' wajib dipakai di SQLite. Cuma format itu yang dimengerti",
                    "date() dan strftime(), dan cuma format itu yang urutannya benar kalau",
                    "dibandingkan sebagai teks.",
                    "",
                    "Kedua: menyaring rentang tanggal dengan cara yang bikin index nggak",
                    "terpakai.",
                    "  X  WHERE YEAR(tanggal) = 2024",
                    "     Fungsi membungkus kolom, index tidak terpakai, seluruh tabel",
                    "     dihitung ulang.",
                    "  X  WHERE tanggal BETWEEN '2024-01-01' AND '2024-12-31'",
                    "     Kalau kolomnya DATETIME, '2024-12-31' berarti jam 00:00:00.",
                    "     Transaksi tanggal 31 Desember jam 10 pagi HILANG dari laporan,",
                    "     tanpa error.",
                    "  V  WHERE tanggal >= '2024-01-01' AND tanggal < '2025-01-01'",
                    "",
                    "Bentuk terakhir disebut rentang setengah terbuka: batas bawah ikut,",
                    "batas atas nggak. Index tetap terpakai, jam berapa pun tercakup, dan",
                    "kamu nggak perlu tahu bulan itu isinya 28, 30, atau 31 hari. Pola yang",
                    "sama dipakai untuk sebulan, sehari, atau sejam. Ini lanjutan saran",
                    "\"hindari fungsi pada kolom di WHERE\" di materi Roadmap.",
                    "",
                    "Ketiga: zona waktu. Cukup dipahami secukupnya supaya nggak kaget.",
                    "",
                    "TIMESTAMP tanpa zona menyimpan angka jamnya apa adanya, misalnya",
                    "'2024-03-01 09:00'. Kolom itu nggak tahu jam 09:00 itu di Jakarta atau",
                    "di London, jadi dua server bisa beda pemahaman.",
                    "",
                    "TIMESTAMPTZ di PostgreSQL menyimpan titik waktu yang pasti. Namanya agak",
                    "menyesatkan, karena dia nggak menyimpan zona apa pun. Nilainya disimpan",
                    "sebagai UTC, lalu diubah ke zona waktu sesi waktu dibaca.",
                    "",
                    "Di MySQL, DATETIME disimpan apa adanya, sedangkan TIMESTAMP diubah ke",
                    "UTC waktu disimpan. Akibatnya, kalau zona waktu server diganti, arti",
                    "data lama di kolom TIMESTAMP ikut berubah, padahal nggak ada satu baris",
                    "pun yang di-UPDATE.",
                    "",
                    "Patokan yang menyelamatkan banyak orang: simpan dalam UTC, tampilkan",
                    "dalam waktu lokal pengguna. Mengubah ke waktu lokal adalah tugas bagian",
                    "tampilan aplikasi, bukan tugas tabel.",
                ],
            },
        ],
    },
    {
        "title": "12. EXISTS, Subquery Berkorelasi & Operator Himpunan",
        "sections": [
            {
                "body": [
                    "Subquery yang udah kamu kenal bisa berdiri sendiri. Isi kurungnya bisa",
                    "dipotong, ditempel ke jendela lain, dijalankan terpisah, dan hasilnya",
                    "tetap sama:",
                    "",
                    "  SELECT AVG(ipk) FROM mahasiswa      -- jalan sendirian, hasilnya satu angka",
                    "",
                    "Subquery berkorelasi nggak bisa begitu. Subquery ini menyebut kolom",
                    "milik query di luarnya:",
                    "",
                    "  SELECT m.nama FROM mahasiswa m",
                    "  WHERE m.ipk = (SELECT MAX(ipk) FROM mahasiswa WHERE jurusan = m.jurusan);",
                    "                                                            ^^^^^^^^^",
                    "                            m.jurusan tidak ada artinya di luar query ini",
                    "",
                    "Alias m boleh dipakai di dalam kurung karena alias yang ditulis di FROM",
                    "query luar berlaku untuk seluruh query, termasuk subquery di dalamnya.",
                    "Kebalikannya nggak berlaku. Alias yang dibikin di dalam subquery nggak",
                    "dikenal di luar. Anggap aja kurungnya seperti kaca satu arah: dari dalam",
                    "bisa melihat ke luar, dari luar nggak bisa melihat ke dalam.",
                    "",
                    "Di sini cara pikir \"subquery dijalankan lebih dulu, lalu hasilnya",
                    "dipakai query utama\" (kalimat yang dipakai di penjelasan Kuis 5) nggak",
                    "berlaku lagi. Untuk subquery berkorelasi, urutannya justru terbalik:",
                    "",
                    "  untuk SETIAP baris query luar:",
                    "      jalankan ulang subquery-nya dengan nilai baris itu",
                    "",
                    "Lima baris mahasiswa berarti MAX(ipk) dihitung lima kali. Query di atas",
                    "benar dan aman untuk tabel kecil. Tapi di tabel satu juta baris, artinya",
                    "satu juta kali subquery. Ini penyebab umum query yang hasilnya benar",
                    "tapi lambatnya keterlaluan.",
                    "",
                    "Query planner, yaitu bagian database yang menyusun cara menjalankan",
                    "query, sering bisa menulis ulang query seperti ini sendiri. Tapi jangan",
                    "bergantung pada itu. Kalau ada versi JOIN atau window function-nya,",
                    "pilih itu. Keduanya membaca tabel sekali aja, nggak sekali per baris.",
                    "",
                    "Cara mengenalinya cepat: lihat isi kurungnya. Kalau ada alias dari luar,",
                    "berarti subquery-nya berkorelasi, dan dia dijalankan berulang kali.",
                ],
            },
            {
                "heading": "Yang berkorelasi, dan dua cara menghindarinya",
                "body": [
                    "Contoh di bawah memakai subquery di tiga tempat yang berbeda. Dua di",
                    "antaranya baru buat kamu.",
                    "",
                    "Pertama, subquery di FROM, disebut derived table atau tabel turunan.",
                    "Hasil subquery diperlakukan sebagai tabel sementara, dan wajib dikasih",
                    "alias. MySQL menolaknya dengan pesan terkenal 'Every derived table must",
                    "have its own alias'. PostgreSQL menolak dengan pesan 'subquery in FROM",
                    "must have an alias'. SQLite kebetulan membolehkan, tapi tetap tulis",
                    "aliasnya. Tanpa nama, kolomnya nggak bisa dirujuk dari luar. Nanti di",
                    "materi Window Function ada contoh TOP 3 dengan kata 'hasil' sesudah",
                    "kurung tutup. Kata itu alias, dan nggak boleh dihapus.",
                    "",
                    "Kedua, subquery di daftar SELECT, disebut subquery skalar. Hasilnya jadi",
                    "kolom tambahan. Aturannya ketat: subquery ini harus mengembalikan tepat",
                    "satu baris dan satu kolom.",
                    "  - Kalau hasilnya dua kolom, semua database menolak, misalnya dengan",
                    "    pesan 'sub-select returns 2 columns - expected 1'.",
                    "  - Kalau hasilnya dua baris, MySQL dan PostgreSQL error waktu query",
                    "    dijalankan. SQLite malah pakai baris pertama tanpa bilang apa-apa.",
                    "    Jadi query yang lolos di laptopmu bisa gagal di server sungguhan.",
                    "  - Kalau nggak ada baris yang cocok, hasilnya NULL. Bukan nol, dan",
                    "    bukan error.",
                ],
                "code": """CREATE TABLE mahasiswa (
    nim     INTEGER PRIMARY KEY,
    nama    VARCHAR(50),
    jurusan VARCHAR(30),
    ipk     DECIMAL(3,2)
);

INSERT INTO mahasiswa VALUES
(101, 'Andi',  'Informatika',      3.75),
(102, 'Budi',  'Informatika',      3.20),
(103, 'Citra', 'Sistem Informasi', 3.90),
(104, 'Dedi',  'Sistem Informasi', 3.10),
(105, 'Eka',   'Informatika',      3.55);

-- 1) BERKORELASI: kurungnya menyebut m.jurusan milik query luar,
--    jadi ia dijalankan ulang untuk tiap baris (5 baris = 5 kali).
SELECT m.nama, m.jurusan, m.ipk
FROM mahasiswa m
WHERE m.ipk = (SELECT MAX(x.ipk) FROM mahasiswa x WHERE x.jurusan = m.jurusan)
ORDER BY m.jurusan;
-- Andi|Informatika|3.75
-- Citra|Sistem Informasi|3.9

-- 2) Versi JOIN: maksimum tiap jurusan dihitung SEKALI di derived table,
--    baru dipasangkan. Kata 'maks' sesudah kurung tutup itu aliasnya.
SELECT m.nama, m.jurusan, m.ipk
FROM mahasiswa m
JOIN (
    SELECT jurusan, MAX(ipk) AS ipk_tertinggi
    FROM mahasiswa
    GROUP BY jurusan
) maks ON maks.jurusan = m.jurusan AND maks.ipk_tertinggi = m.ipk
ORDER BY m.jurusan;

-- 3) Subquery skalar di daftar SELECT: satu baris satu kolom, per baris luar.
SELECT m.nama,
       (SELECT COUNT(*) FROM mahasiswa s WHERE s.jurusan = m.jurusan) AS sejurusan
FROM mahasiswa m
ORDER BY m.nim;
-- Andi|3   Budi|3   Citra|2   Dedi|2   Eka|3

-- 4) Versi window function: tabelnya dibaca sekali, tanpa subquery berulang.
SELECT nama, jurusan, ipk
FROM (
    SELECT nama, jurusan, ipk,
           RANK() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS rk
    FROM mahasiswa
) hasil
WHERE rk = 1
ORDER BY jurusan;""",
            },
            {
                "body": [
                    "EXISTS (subquery) bernilai benar kalau subquery-nya menghasilkan minimal",
                    "satu baris. Yang dicek adalah ada atau nggaknya baris, bukan isi",
                    "barisnya. Karena itu bentuk bakunya begini:",
                    "",
                    "  WHERE EXISTS (SELECT 1 FROM nilai n WHERE n.nim = m.nim)",
                    "",
                    "Angka 1 di situ bukan nomor kolom, dan bukan trik supaya cepat. Itu cuma",
                    "pengisi, karena SELECT tetap butuh sesuatu untuk ditulis. SELECT *,",
                    "SELECT n.skor, bahkan SELECT 'apa pun' hasilnya sama persis. Database",
                    "berhenti begitu ketemu baris pertama, dan nggak pernah membaca nilainya.",
                    "",
                    "EXISTS hampir selalu berkorelasi. Kalau subquery-nya nggak menyebut",
                    "kolom luar, jawabannya sama untuk semua baris, jadi nggak ada gunanya",
                    "ditulis.",
                    "",
                    "Ada dua istilah yang bakal sering kamu temui di pembahasan performa dan",
                    "di keluaran EXPLAIN:",
                    "  semi-join -> ambil baris kiri yang PUNYA pasangan, tanpa menampilkan kolom",
                    "               kanannya dan tanpa menggandakan baris kiri.",
                    "  anti-join -> kebalikannya: ambil baris kiri yang TIDAK punya pasangan.",
                    "",
                    "Anti-join bisa ditulis dengan tiga cara. Ketiganya sering dipakai orang,",
                    "jadi kamu perlu bisa membaca semuanya, walaupun yang kamu tulis sendiri",
                    "cuma satu:",
                    "  - LEFT JOIN + IS NULL. Ini cara paling tua dan jalan di database mana",
                    "    pun. Bentuk ini udah dipakai di materi JOIN. IS NULL wajib diarahkan",
                    "    ke kolom yang nggak pernah NULL di tabel kanan, biasanya kolom",
                    "    kuncinya. Kalau salah pilih kolom, hasilnya meleset tanpa tanda",
                    "    apa-apa.",
                    "  - NOT EXISTS. Maksudnya paling jelas, dan aman terhadap NULL. Jadikan",
                    "    ini pilihan utamamu.",
                    "  - NOT IN (subquery). Paling pendek, tapi punya jebakan.",
                    "",
                    "Jebakan: kalau hasil subquery di NOT IN berisi satu aja NULL, seluruh",
                    "query mengembalikan nol baris. Penyebabnya logika tiga nilai (lihat",
                    "materi Ekspresi, NULL & CASE). x NOT IN (101, NULL) sama dengan x <> 101",
                    "AND x <> NULL. Bagian x <> NULL selalu \"nggak diketahui\", nggak pernah",
                    "benar, jadi AND-nya juga nggak pernah benar. Nggak ada error, nggak ada",
                    "peringatan. Hasilnya cuma kosong, dan query-nya kelihatan baik-baik aja.",
                    "Ini alasan utama programmer berpengalaman memilih NOT EXISTS. Kalau",
                    "tetap mau pakai NOT IN, saring dulu NULL-nya: WHERE nim IS NOT NULL.",
                ],
            },
            {
                "heading": "Semi-join & anti-join: tiga tulisan, satu maksud",
                "code": """CREATE TABLE mahasiswa (
    nim  INTEGER PRIMARY KEY,
    nama VARCHAR(50)
);

CREATE TABLE nilai (
    nim  INTEGER,      -- sengaja boleh NULL: ada lembar jawaban tanpa nama
    kode VARCHAR(10),
    skor INT
);

INSERT INTO mahasiswa VALUES (101, 'Andi'), (102, 'Budi'), (103, 'Citra');
INSERT INTO nilai VALUES (101, 'IF101', 88), (103, 'IF101', 75), (NULL, 'IF101', 60);

-- SEMI-JOIN: yang PUNYA nilai. Kolom tabel nilai tidak ikut tampil.
SELECT m.nama FROM mahasiswa m
WHERE EXISTS (SELECT 1 FROM nilai n WHERE n.nim = m.nim);
-- Andi
-- Citra

-- Isi SELECT di dalam EXISTS tidak berpengaruh: hasilnya sama persis.
SELECT m.nama FROM mahasiswa m
WHERE EXISTS (SELECT n.skor * 1000 FROM nilai n WHERE n.nim = m.nim);

-- ANTI-JOIN cara 1: LEFT JOIN + IS NULL
SELECT m.nama FROM mahasiswa m
LEFT JOIN nilai n ON n.nim = m.nim
WHERE n.nim IS NULL;
-- Budi

-- ANTI-JOIN cara 2: NOT EXISTS (aman walau ada NULL)
SELECT m.nama FROM mahasiswa m
WHERE NOT EXISTS (SELECT 1 FROM nilai n WHERE n.nim = m.nim);
-- Budi

-- ANTI-JOIN cara 3: NOT IN -> KOSONG! daftar nim-nya memuat satu NULL
SELECT m.nama FROM mahasiswa m
WHERE m.nim NOT IN (SELECT nim FROM nilai);
-- (tidak ada baris sama sekali)

-- Tambalannya: buang NULL-nya lebih dulu
SELECT m.nama FROM mahasiswa m
WHERE m.nim NOT IN (SELECT nim FROM nilai WHERE nim IS NOT NULL);
-- Budi

-- Buktinya (1 = benar, kolom kosong = NULL alias 'tidak diketahui')
SELECT 102 NOT IN (101, 103)       AS tanpa_null,
       102 NOT IN (101, 103, NULL) AS dengan_null;
-- 1|""",
            },
            {
                "heading": "Operator himpunan: INTERSECT & EXCEPT",
                "body": [
                    "UNION dan UNION ALL udah kamu lihat di materi Subquery, dan nanti",
                    "dipakai lagi di recursive CTE. Keluarga lengkapnya ada empat operator",
                    "himpunan, dan dua sisanya sama pentingnya:",
                    "",
                    "  UNION      -> gabungan, duplikat DIBUANG (perlu menyortir, jadi lebih mahal)",
                    "  UNION ALL  -> gabungan apa adanya, duplikat DIPERTAHANKAN (paling murah)",
                    "  INTERSECT  -> irisan: baris yang muncul di KEDUA hasil",
                    "  EXCEPT     -> selisih: baris hasil pertama yang TIDAK ada di hasil kedua",
                    "",
                    "Aturannya sama untuk keempatnya:",
                    "  - Jumlah kolom di kedua sisi harus sama, dan tipenya harus sepadan.",
                    "    Kalau nggak, hasilnya error.",
                    "  - Nama kolom hasil diambil dari query pertama. Alias di query kedua",
                    "    diabaikan.",
                    "  - Yang dibandingkan adalah seluruh baris, semua kolomnya, nggak cuma",
                    "    kolom pertama.",
                    "  - ORDER BY cuma boleh ditulis sekali, di paling akhir, dan berlaku",
                    "    untuk seluruh gabungan.",
                    "  - INTERSECT dan EXCEPT juga membuang duplikat, sama seperti UNION.",
                    "",
                    "Namanya bisa beda antar database. Oracle menyebut EXCEPT sebagai MINUS,",
                    "artinya sama persis. MySQL baru punya INTERSECT dan EXCEPT sejak versi",
                    "8.0.31. Sebelum itu, orang menirunya pakai JOIN dan NOT EXISTS.",
                    "PostgreSQL dan SQLite udah lama punya keempatnya. PostgreSQL juga punya",
                    "varian INTERSECT ALL dan EXCEPT ALL yang ikut menghitung duplikat.",
                    "SQLite nggak punya varian ALL untuk keduanya.",
                    "",
                    "Operator ini alat utama untuk skrip rekonsiliasi dan audit, yaitu",
                    "membandingkan dua daftar yang seharusnya sama. Misalnya tabel lama",
                    "dengan hasil migrasi, atau catatan toko dengan rekening koran bank.",
                    "Pertanyaannya selalu dua: \"apa yang hilang?\" dan \"apa yang tiba-tiba",
                    "muncul?\". EXCEPT yang dijalankan dua arah menjawab keduanya. Kalau",
                    "dua-duanya kosong, berarti datanya cocok.",
                ],
                "code": """CREATE TABLE stok_lama (kode VARCHAR(10), nama VARCHAR(40));
CREATE TABLE stok_baru (kode VARCHAR(10), nama VARCHAR(40));

INSERT INTO stok_lama VALUES ('P01', 'Beras'), ('P02', 'Gula'), ('P03', 'Kopi');
INSERT INTO stok_baru VALUES ('P02', 'Gula'), ('P03', 'Kopi Bubuk'), ('P04', 'Teh');

-- IRISAN: kode yang ada di kedua daftar.
SELECT kode FROM stok_lama
INTERSECT
SELECT kode FROM stok_baru;
-- P02
-- P03

-- HILANG: ada di daftar lama, tidak ada di daftar baru.
SELECT kode FROM stok_lama
EXCEPT
SELECT kode FROM stok_baru;
-- P01

-- BARU MUNCUL: tinggal ditukar urutan kedua query-nya.
SELECT kode FROM stok_baru
EXCEPT
SELECT kode FROM stok_lama;
-- P04

-- BERUBAH: bandingkan SELURUH baris, bukan cuma kodenya.
-- P03 ikut muncul karena namanya berbeda; P02 tidak, karena identik.
SELECT kode, nama FROM stok_lama
EXCEPT
SELECT kode, nama FROM stok_baru;
-- P01|Beras
-- P03|Kopi

-- ORDER BY hanya sekali, di paling akhir, milik seluruh gabungan.
SELECT kode FROM stok_lama
UNION
SELECT kode FROM stok_baru
ORDER BY kode;""",
            },
        ],
    },
    {
        "title": "13. DML Lanjutan: INSERT dari Query, UPSERT & RETURNING",
        "sections": [
            {
                "body": [
                    "Di materi DML: Insert, Update, Delete, semua nilai INSERT kamu ketik",
                    "sendiri lewat VALUES. Di kode nyata, bentuk itu justru paling jarang.",
                    "Skrip migrasi, sinkronisasi, arsip, dan seed hampir selalu mengambil",
                    "datanya dari tabel lain. Bentuknya INSERT ... SELECT, dan kata VALUES",
                    "nggak muncul sama sekali:",
                    "",
                    "  INSERT INTO arsip (id, email, tanggal, total)",
                    "  SELECT id, email, tanggal, total",
                    "  FROM pesanan",
                    "  WHERE tanggal < '2024-01-01';",
                    "",
                    "Waktu pertama kali lihat, kamu mungkin mengira itu dua perintah yang",
                    "lupa dipisah titik koma. Ternyata itu satu perintah. INSERT selalu butuh",
                    "dua hal: datanya mau diisi ke mana, dan datanya dari mana. Bagian \"dari",
                    "mana\" itu boleh berupa VALUES, boleh juga berupa SELECT. Titik komanya",
                    "cuma satu, di paling akhir. Berapa pun baris yang dikembalikan",
                    "SELECT-nya, sebanyak itu juga baris yang masuk. Nol baris pun boleh, dan",
                    "itu bukan error.",
                    "",
                    "Yang dicocokkan adalah urutan dan jumlah kolom, bukan namanya:",
                    "  - Kolom ke-1 di daftar INSERT diisi kolom ke-1 hasil SELECT, dan",
                    "    seterusnya.",
                    "  - Namanya boleh beda total. Alias di SELECT sama sekali nggak dilihat.",
                    "  - Kalau jumlahnya beda, langsung error, jadi gampang ketahuan.",
                    "  - Kalau urutannya tertukar tapi tipenya kebetulan cocok, nggak ada",
                    "    error. Datanya masuk ke kolom yang salah tanpa ketahuan. Ini jebakan",
                    "    yang paling mahal di bagian ini.",
                    "",
                    "SELECT-nya query biasa. Boleh pakai JOIN, GROUP BY, subquery, ORDER BY,",
                    "apa aja.",
                    "",
                    "CTAS (CREATE TABLE AS SELECT) membuat tabel baru sekaligus mengisinya,",
                    "tanpa perlu mengetik daftar kolomnya dulu:",
                    "  CREATE TABLE ringkasan AS SELECT email, SUM(total) AS nilai FROM arsip",
                    "  GROUP BY email;",
                    "",
                    "Di SQL Server bentuknya beda sendiri, nama tabelnya ditulis di tengah:",
                    "  SELECT email, SUM(total) AS nilai INTO ringkasan FROM arsip GROUP BY email;",
                    "",
                    "Jebakan: CTAS cuma menyalin nama kolom, tipe, dan datanya. PRIMARY KEY,",
                    "index, NOT NULL, DEFAULT, dan FOREIGN KEY nggak ikut. Tabel hasil CTAS",
                    "yang lalu dipakai sebagai tabel sungguhan hampir selalu jadi tabel yang",
                    "lupa punya kunci.",
                ],
            },
            {
                "heading": "Skrip utuh: arsip, CTAS, UPSERT, dan RETURNING",
                "code": """-- Skrip ini membuat tabelnya sendiri, jadi bisa langsung dijalankan.
CREATE TABLE pesanan (
    id      INTEGER PRIMARY KEY,
    email   TEXT    NOT NULL,
    tanggal TEXT    NOT NULL,
    total   INTEGER NOT NULL
);

CREATE TABLE arsip (
    id      INTEGER PRIMARY KEY,
    email   TEXT    NOT NULL,
    tanggal TEXT    NOT NULL,
    total   INTEGER NOT NULL
);

CREATE TABLE pelanggan (
    email   TEXT PRIMARY KEY,
    nama    TEXT NOT NULL,
    belanja INTEGER NOT NULL DEFAULT 0
);

INSERT INTO pesanan (id, email, tanggal, total) VALUES
    (1, 'andi@mail.com', '2023-11-02', 150000),
    (2, 'budi@mail.com', '2023-12-20',  90000),
    (3, 'andi@mail.com', '2024-03-14', 250000);

-- 1. INSERT dari hasil query. Perhatikan: tidak ada kata VALUES sama sekali.
INSERT INTO arsip (id, email, tanggal, total)
SELECT id, email, tanggal, total
FROM pesanan
WHERE tanggal < '2024-01-01';

-- Baru boleh dihapus SESUDAH salinannya dipastikan masuk.
DELETE FROM pesanan WHERE tanggal < '2024-01-01';

SELECT 'sisa pesanan', COUNT(*) FROM pesanan;
SELECT 'baris terarsip', COUNT(*) FROM arsip;

-- 2. CTAS: tabel baru yang kolomnya diambil dari bentuk hasil SELECT.
CREATE TABLE ringkasan AS
SELECT email, COUNT(*) AS jumlah, SUM(total) AS nilai
FROM arsip
GROUP BY email;

SELECT 'ringkasan', email, jumlah, nilai FROM ringkasan;

-- 3. UPSERT: simpan kalau email-nya baru, tambahkan kalau sudah ada.
--    Dijalankan dua kali dengan email yang sama, dan barisnya tetap satu.
INSERT INTO pelanggan (email, nama, belanja)
VALUES ('andi@mail.com', 'Andi', 150000)
ON CONFLICT (email) DO UPDATE SET belanja = pelanggan.belanja + excluded.belanja;

INSERT INTO pelanggan (email, nama, belanja)
VALUES ('andi@mail.com', 'Andi', 250000)
ON CONFLICT (email) DO UPDATE SET belanja = pelanggan.belanja + excluded.belanja;

SELECT 'pelanggan', email, nama, belanja FROM pelanggan;

-- 4. RETURNING: id baris baru langsung dikembalikan, tanpa SELECT susulan.
INSERT INTO pesanan (email, tanggal, total)
VALUES ('citra@mail.com', '2024-04-01', 75000)
RETURNING id, email, total;""",
            },
            {
                "body": [
                    "UPDATE dan DELETE yang udah kamu pelajari selalu pakai nilai yang",
                    "diketik tangan. Di kode nyata, jauh lebih sering nilainya diambil dari",
                    "tabel lain. Sayangnya, di bagian ini tiap database paling banyak",
                    "bedanya. Ingat bentuk milik database yang kamu pakai, dan jangan kaget",
                    "kalau ada tiga bentuk untuk satu maksud.",
                    "",
                    "Contohnya, menyalin diskon milik pelanggan ke tiap pesanannya.",
                    "",
                    "MySQL / MariaDB, JOIN dulu, SET belakangan:",
                    "  UPDATE pesanan p",
                    "  JOIN pelanggan k ON p.email = k.email",
                    "  SET p.diskon = k.diskon;",
                    "",
                    "PostgreSQL / SQLite 3.33+, SET dulu, FROM belakangan:",
                    "  UPDATE pesanan AS p",
                    "  SET diskon = k.diskon",
                    "  FROM pelanggan AS k",
                    "  WHERE p.email = k.email;",
                    "",
                    "SQL Server, tabelnya disebut dua kali, di UPDATE dan di FROM:",
                    "  UPDATE p SET p.diskon = k.diskon",
                    "  FROM pesanan p JOIN pelanggan k ON p.email = k.email;",
                    "",
                    "Ada juga bentuk yang jalan di semua database. Bentuk ini pakai subquery",
                    "berkorelasi (dibahas di materi EXISTS, Subquery Berkorelasi & Operator",
                    "Himpunan):",
                    "  UPDATE pesanan",
                    "  SET diskon = (SELECT k.diskon FROM pelanggan k WHERE k.email =",
                    "  pesanan.email)",
                    "  WHERE EXISTS (SELECT 1 FROM pelanggan k WHERE k.email = pesanan.email);",
                    "",
                    "Jebakan: jangan buang baris WHERE EXISTS itu. Hampir semua orang",
                    "membuangnya karena kelihatan nggak perlu. Akibatnya, pesanan yang",
                    "email-nya nggak punya pasangan ikut ter-UPDATE. Subquery-nya",
                    "mengembalikan NULL untuk baris itu, jadi diskonnya ditimpa jadi NULL.",
                    "Nggak ada error, nggak ada peringatan, datanya hilang begitu aja. Bentuk",
                    "UPDATE ... FROM di atas nggak punya masalah ini, karena WHERE-nya",
                    "menyaring baris yang nggak berpasangan lebih dulu.",
                    "",
                    "DELETE juga punya bentuk lintas tabel:",
                    "  PostgreSQL : DELETE FROM pesanan p USING pelanggan k",
                    "               WHERE p.email = k.email AND k.status = 'blokir';",
                    "  MySQL      : DELETE p FROM pesanan p",
                    "               JOIN pelanggan k ON p.email = k.email WHERE k.status =",
                    "               'blokir';",
                    "  Portabel   : DELETE FROM pesanan",
                    "               WHERE email IN (SELECT email FROM pelanggan WHERE status",
                    "               = 'blokir');",
                    "",
                    "Bentuk 'DELETE p FROM ...' di MySQL bukan salah ketik. Kalau ada dua",
                    "tabel yang di-JOIN, alias sesudah DELETE menentukan tabel mana yang",
                    "barisnya dibuang. Kalau lupa menulis alias itu, hasilnya error sintaks.",
                    "Kalau salah menulisnya, tabel yang salah yang terhapus.",
                ],
            },
            {
                "body": [
                    "UPSERT artinya \"simpan kalau baru, perbarui kalau udah ada\". Sebelum",
                    "tahu UPSERT, biasanya orang menulisnya di aplikasi dengan tiga langkah:",
                    "",
                    "  langkah 1: SELECT ... WHERE email = 'andi@mail.com';   -- sudah ada belum?",
                    "  langkah 2: kalau ada   -> UPDATE",
                    "  langkah 3: kalau tidak -> INSERT",
                    "",
                    "Cara itu nggak cuma boros, tapi juga rusak. Di antara langkah 1 dan 3",
                    "ada jeda waktu. Bayangkan dua proses, misalnya dua permintaan web, dua",
                    "worker, atau dua tab browser, mengecek pada saat yang sama. Dua-duanya",
                    "melihat \"belum ada\", lalu dua-duanya menjalankan INSERT. Hasilnya baris",
                    "ganda, atau error UNIQUE yang cuma muncul sesekali dan susah sekali",
                    "ditiru ulang waktu kamu mencari penyebabnya.",
                    "",
                    "UPSERT menutup celah itu. Pengecekan dan penulisannya dikerjakan",
                    "database dalam satu perintah, jadi nggak ada jeda yang bisa diselipi",
                    "proses lain. Itu alasan utama UPSERT ada, jauh lebih penting daripada",
                    "soal hemat baris kode.",
                    "",
                    "Syaratnya mutlak: kolom yang menentukan \"udah ada\" harus punya PRIMARY",
                    "KEY atau UNIQUE. Tanpa itu, nggak ada yang namanya konflik. PostgreSQL",
                    "dan SQLite menolak ON CONFLICT (kolom) kalau kolomnya nggak unik. MySQL",
                    "menerima ON DUPLICATE KEY UPDATE, tapi klausanya nggak pernah jalan",
                    "sekali pun.",
                    "",
                    "Waktu INSERT berubah jadi UPDATE, kamu perlu cara menyebut nilai yang",
                    "tadi mau dimasukkan:",
                    "  - PostgreSQL dan SQLite memakai tabel semu bernama excluded (di",
                    "    dokumentasi sering ditulis EXCLUDED). excluded.nama adalah nilai",
                    "    yang barusan gagal masuk, sedangkan pelanggan.nama adalah nilai yang",
                    "    udah ada di tabel. Tanpa dua nama itu, kamu nggak bisa membedakan",
                    "    keduanya.",
                    "  - MySQL dan MariaDB memakai fungsi VALUES(nama). Sejak MySQL 8.0.20,",
                    "    bentuk itu deprecated (masih jalan tapi bakal dihapus) dan diganti",
                    "    alias baris:",
                    "      INSERT ... VALUES (...) AS baru",
                    "      ON DUPLICATE KEY UPDATE nama = baru.nama;",
                    "    Kamu bakal ketemu dua bentuk itu di kode yang beredar.",
                ],
                "code": """-- Kumpulan bentuk UPSERT per dialek. Ini BUKAN satu skrip yang dijalankan
-- berurutan: pilih SATU yang cocok dengan database yang kamu pakai.
-- Menjalankan semuanya sekaligus pasti error, karena tiap dialek hanya
-- mengerti bentuknya sendiri.

-- PostgreSQL & SQLite: perbarui kalau email-nya sudah terdaftar
INSERT INTO pelanggan (email, nama, belanja)
VALUES ('andi@mail.com', 'Andi', 150000)
ON CONFLICT (email) DO UPDATE
SET nama    = excluded.nama,
    belanja = pelanggan.belanja + excluded.belanja;

-- Diamkan saja kalau sudah ada; tidak dihitung sebagai error
INSERT INTO pelanggan (email, nama)
VALUES ('andi@mail.com', 'Andi')
ON CONFLICT (email) DO NOTHING;

-- MySQL / MariaDB, bentuk klasik
INSERT INTO pelanggan (email, nama, belanja)
VALUES ('andi@mail.com', 'Andi', 150000)
ON DUPLICATE KEY UPDATE
    nama    = VALUES(nama),
    belanja = belanja + VALUES(belanja);

-- Bentuk pendek. INSERT OR IGNORE aman: baris lama dibiarkan apa adanya.
INSERT OR IGNORE INTO pelanggan (email, nama) VALUES ('andi@mail.com', 'Andi');

-- INSERT OR REPLACE (dan REPLACE INTO di MySQL) BUKAN update. Baris lamanya
-- DIHAPUS lalu ditulis ulang dari nol, sehingga: kolom yang tidak kamu sebut
-- kembali ke DEFAULT/NULL (belanja hilang!), ON DELETE CASCADE ikut menyala
-- dan menyeret baris tabel lain, dan id/rowid-nya bisa berganti.
-- Hampir selalu bukan yang kamu mau -- pakai ON CONFLICT DO UPDATE.
INSERT OR REPLACE INTO pelanggan (email, nama) VALUES ('andi@mail.com', 'Andi');""",
            },
            {
                "body": [
                    "Sesudah INSERT, hampir selalu kamu butuh id baris yang baru dibikin,",
                    "misalnya untuk dipasang sebagai FOREIGN KEY di tabel berikutnya. Jangan",
                    "pernah menebaknya pakai SELECT MAX(id). Kalau dua proses menyisipkan",
                    "data bersamaan, keduanya bisa dapat angka yang sama, lalu salah satunya",
                    "menempelkan data ke baris milik orang lain.",
                    "",
                    "Cara yang benar di tiap database:",
                    "  PostgreSQL / SQLite 3.35+ / MariaDB : klausa RETURNING",
                    "      INSERT INTO pesanan (email, total) VALUES ('citra@mail.com', 75000)",
                    "      RETURNING id, total;",
                    "  MySQL      : SELECT LAST_INSERT_ID();   (MySQL belum punya RETURNING)",
                    "  SQL Server : SELECT SCOPE_IDENTITY();   atau klausa OUTPUT INSERTED.id",
                    "  SQLite     : SELECT last_insert_rowid();",
                    "",
                    "Nilai LAST_INSERT_ID() dan SCOPE_IDENTITY() dihitung per koneksi, jadi",
                    "aman dari proses lain. Tapi kalau kamu INSERT banyak baris sekaligus,",
                    "LAST_INSERT_ID() mengembalikan id baris pertama, bukan yang terakhir.",
                    "Banyak orang mengira sebaliknya.",
                    "",
                    "RETURNING juga jalan di UPDATE dan DELETE, nggak cuma di INSERT. Ini",
                    "cara paling rapi untuk tahu persis baris mana yang barusan kena:",
                    "  DELETE FROM sesi WHERE kedaluwarsa < '2024-01-01' RETURNING id;",
                    "",
                    "Menghapus banyak baris di tabel besar",
                    "",
                    "Sebaiknya jangan hapus sekaligus. Satu DELETE untuk jutaan baris",
                    "mengunci baris-barisnya lama sekali, bikin log transaksi membengkak, dan",
                    "bisa bikin aplikasi ikut macet. Hapus sedikit-sedikit, dan ulangi sampai",
                    "nggak ada lagi yang terhapus:",
                    "  MySQL      : DELETE FROM log WHERE tanggal < '2024-01-01' LIMIT 1000;",
                    "  PostgreSQL : DELETE FROM log WHERE id IN (",
                    "                   SELECT id FROM log WHERE tanggal < '2024-01-01' LIMIT",
                    "                   1000);",
                    "",
                    "PostgreSQL nggak menerima LIMIT langsung di DELETE, jadi batasnya",
                    "dipasang di subquery. Bentuk kedua ini juga jalan di SQLite. MySQL",
                    "menolaknya, karena MySQL nggak menerima LIMIT di dalam subquery IN.",
                    "",
                    "TRUNCATE dan DELETE",
                    "",
                    "Di materi DDL, TRUNCATE kelihatan seperti versi cepat dari DELETE.",
                    "Bedanya lebih dari itu:",
                    "  DELETE FROM t;     -> baris dibuang satu per satu, trigger MENYALA, bisa",
                    "                        di-ROLLBACK, dan nomor AUTO_INCREMENT lanjut dari",
                    "                        angka terakhir - baris berikutnya tidak mulai dari 1.",
                    "  TRUNCATE TABLE t;  -> isinya dibuang sekaligus, trigger TIDAK menyala, dan",
                    "                        AUTO_INCREMENT direset ke 1 (di PostgreSQL hanya kalau",
                    "                        kamu tulis TRUNCATE t RESTART IDENTITY).",
                    "",
                    "Kalau ada tabel lain yang menunjuk t lewat FOREIGN KEY, TRUNCATE",
                    "ditolak. MySQL dengan InnoDB langsung menolak. PostgreSQL minta kamu",
                    "menulis CASCADE, yang ikut mengosongkan tabel anaknya, jadi baca dua",
                    "kali sebelum mengetiknya. DELETE tetap jalan, dan mengikuti aturan ON",
                    "DELETE yang kamu pasang.",
                    "",
                    "Ingat: di MySQL, TRUNCATE langsung melakukan commit otomatis. Sekali",
                    "jalan, ROLLBACK nggak bisa menolong lagi. SQLite nggak punya TRUNCATE",
                    "sama sekali, jadi pakai DELETE FROM t;.",
                ],
            },
        ],
    },
    {
        "title": "14. Index, Normalisasi & Best Practice",
        "sections": [
            {
                "body": [
                    "Index adalah struktur khusus yang bikin pencarian lebih cepat. Mirip",
                    "daftar isi di buku: daripada membaca buku dari halaman pertama, kamu",
                    "lihat daftar isinya dulu, lalu langsung lompat ke halaman yang dicari.",
                    "PRIMARY KEY otomatis punya index.",
                    "",
                    "Cara membuat dan menghapus index (ejaan MySQL):",
                    "  CREATE INDEX idx_nama ON mahasiswa(nama);",
                    "  CREATE UNIQUE INDEX idx_nim ON mahasiswa(nim);",
                    "  DROP INDEX idx_nama ON mahasiswa;",
                    "",
                    "Index paling berguna kalau:",
                    "  - kolomnya sering dipakai di WHERE atau JOIN,",
                    "  - datanya udah banyak, ribuan baris atau lebih.",
                    "",
                    "Hati-hati: index mempercepat SELECT, tapi memperlambat INSERT, UPDATE,",
                    "dan DELETE, karena index-nya ikut diperbarui tiap kali data berubah.",
                    "Index juga makan ruang penyimpanan.",
                ]
            },
            {
                "body": [
                    "Normalisasi adalah cara merapikan struktur tabel supaya nggak boros dan",
                    "nggak ada data yang diulang-ulang (redundansi). Data yang diulang di",
                    "banyak tempat gampang jadi nggak sinkron: diubah di satu tempat, lupa",
                    "diubah di tempat lain.",
                    "",
                    "Ada tiga tingkat yang paling sering dibahas.",
                    "",
                    "1NF: tiap kolom harus atomik, artinya satu sel cuma berisi satu nilai.",
                    "  X  hobi: 'membaca, main game' -> pecah jadi baris.",
                    "",
                    "2NF: berlaku untuk tabel yang kuncinya gabungan. Kolom yang bukan kunci",
                    "nggak boleh bergantung cuma pada sebagian kunci.",
                    "",
                    "3NF: kolom nggak boleh bergantung pada kolom lain selain primary key.",
                    "Ketergantungan lewat perantara seperti ini disebut transitive",
                    "dependency.",
                    "",
                    "Contoh tabel yang kurang rapi:",
                    "  nilai (nim, nama, jurusan, kode, skor)",
                    "  -> 'nama' & 'jurusan' hanya bergantung pada 'nim'.",
                    "  -> Pecah jadi tabel mahasiswa & tabel nilai.",
                    "",
                    "Kalau nama dan jurusan ikut disimpan di tabel nilai, keduanya ditulis",
                    "ulang di setiap baris nilai milik mahasiswa itu. Dengan dipecah, nama",
                    "dan jurusan cukup disimpan sekali di tabel mahasiswa.",
                    "",
                    "Hubungan antar tabel ada tiga jenis:",
                    "  1:1  -> satu-ke-satu",
                    "  1:N  -> satu-ke-banyak (paling umum)",
                    "  N:M  -> banyak-ke-banyak (butuh tabel penghubung)",
                ]
            },
            {
                "body": [
                    "Kebiasaan baik waktu menulis SQL:",
                    "  1. Selalu pakai WHERE di UPDATE dan DELETE.",
                    "  2. Pilih kolom yang memang dibutuhkan. Hindari SELECT * kalau datanya",
                    "     besar.",
                    "  3. Pakai alias supaya query gampang dibaca.",
                    "  4. Tulis query dengan rapi, satu klausa (SELECT, FROM, WHERE, dan",
                    "     seterusnya) per baris.",
                    "  5. Pelajari EXPLAIN untuk menganalisis performa query:",
                    "       EXPLAIN SELECT * FROM mahasiswa WHERE ipk > 3.0;",
                    "  6. Pakai transaction untuk operasi yang penting.",
                    "  7. Backup database secara rutin.",
                    "  8. Kalau kamu bikin aplikasi Java, gabungkan SQL dengan JDBC atau",
                    "     Spring:",
                    "       - JDBC: API bawaan Java untuk akses database.",
                    "       - JPA/Hibernate: ORM yang memetakan tabel ke objek Java.",
                    "",
                    "Supaya makin lancar:",
                    "  - Latihan query di MySQL setiap hari.",
                    "  - Kerjakan soal JOIN dan agregasi, karena dua topik itu yang paling",
                    "    sering ditanyakan.",
                    "  - Gabungkan dengan Java lewat JDBC, lalu lanjut ke Spring Boot.",
                ]
            },
        ],
    },
    {
        "title": "15. Keamanan Query: Parameter, Injeksi & Hak Akses",
        "sections": [
            {
                "body": [
                    "Sampai sini kamu selalu mengetik SQL langsung ke prompt database. Di",
                    "kode nyata, itu justru jarang. Biasanya SQL ditulis sebagai string di",
                    "dalam program Java, Python, atau JavaScript, dan string itu hampir",
                    "selalu punya lubang:",
                    "",
                    "  // Java (JDBC)",
                    "  String sql = \"SELECT id, nama FROM pengguna WHERE email = ?\";",
                    "",
                    "  # Python (psycopg, mysql-connector)",
                    "  sql = \"SELECT id, nama FROM pengguna WHERE email = %s\"",
                    "",
                    "  // JavaScript (node-postgres)",
                    "  const sql = 'SELECT id, nama FROM pengguna WHERE email = $1'",
                    "",
                    "Tanda ?, %s, dan $1 itu bukan bagian dari bahasa SQL. Kamu nggak bakal",
                    "menemukannya di dokumentasi MySQL. Tanda itu adalah lubang, atau",
                    "placeholder: penanda bahwa nilainya menyusul dan nggak diketik di situ.",
                    "Yang mengisinya adalah pustaka penghubung database (driver), tepat",
                    "sebelum query dikirim.",
                    "",
                    "Bentuk lubangnya tergantung pustaka yang dipakai, bukan tergantung",
                    "database-nya:",
                    "  ?         -> JDBC (Java), SQLite, MySQL Connector, PHP PDO",
                    "  %s        -> Python DB-API: psycopg2, mysql-connector, MySQLdb",
                    "  :nama     -> named parameter: Spring JDBC, SQLAlchemy, Oracle, SQLite",
                    "  $1 $2 $3  -> PostgreSQL asli & node-postgres (bernomor, mulai dari 1)",
                    "",
                    "Nggak usah bingung kalau ketemu bentuk yang beda dari yang kamu hafal.",
                    "Artinya sama persis. Ada dua hal yang sering bikin salah:",
                    "  - %s di Python DB-API bukan format string Python. Tulisannya tetap %s",
                    "    walaupun nilainya angka. Nilainya dikirim sebagai argumen kedua",
                    "    execute(), bukan lewat % atau f-string.",
                    "  - Placeholder nggak diapit tanda kutip. Kalau kamu menulis email =",
                    "    '?', tanda tanya itu jadi teks satu karakter, bukan lubang lagi.",
                ],
            },
            {
                "heading": "Kenapa menyambung string itu berbahaya",
                "body": [
                    "Query di bawah ini disusun dengan menyambung string. Pemula paling",
                    "sering melihat cara ini, karena paling gampang ditulis:",
                    "",
                    "  sql = \"SELECT id, email FROM pengguna WHERE email = '\" + email",
                    "      + \"' AND sandi = '\" + sandi + \"'\"",
                    "",
                    "Jalankan blok berikut, lalu bandingkan tiga hasilnya. Di query ketiga,",
                    "yang diketik di kolom sandi bukan sandi siapa pun. Tapi seluruh isi",
                    "tabel tetap keluar, termasuk akun admin.",
                ],
                "code": """-- Tabel pengguna sebuah aplikasi, lengkap dengan satu akun admin.
CREATE TABLE pengguna (
    id     INTEGER PRIMARY KEY,
    email  TEXT NOT NULL,
    sandi  TEXT NOT NULL
);

INSERT INTO pengguna (id, email, sandi) VALUES
    (1, 'levi@contoh.id',  'kunci-levi'),
    (2, 'dina@contoh.id',  'kunci-dina'),
    (3, 'admin@contoh.id', 'kunci-admin');

-- 1. Login wajar: email dan sandi benar.
SELECT '=== sandi benar ===';
SELECT id, email FROM pengguna
WHERE email = 'levi@contoh.id' AND sandi = 'kunci-levi';

-- 2. Login gagal: sandi salah, tidak ada baris keluar. Ini yang diharapkan.
SELECT '=== sandi salah ===';
SELECT id, email FROM pengguna
WHERE email = 'levi@contoh.id' AND sandi = 'asal-tebak';

-- 3. Kolom sandi diisi persis teks ini:   ' OR '1'='1
--    Setelah disambung, kutip penutupnya jatuh di tempat yang salah dan
--    sisa ketikannya berhenti jadi NILAI lalu berubah jadi PERINTAH.
SELECT '=== sandi diisi tanda kutip lalu OR ===';
SELECT id, email FROM pengguna
WHERE email = 'levi@contoh.id' AND sandi = '' OR '1'='1';""",
            },
            {
                "body": [
                    "Database membaca query ketiga tadi sebagai: (email cocok dan sandi",
                    "kosong) atau ('1' sama dengan '1'). Bagian kanan selalu benar, jadi",
                    "semua baris lolos. Penyerang nggak menebak sandi siapa pun. Dia mengubah",
                    "bentuk query-nya. Itulah yang disebut SQL injection.",
                    "",
                    "Kalau pakai lubang ?, nilainya dikirim terpisah dari teks query.",
                    "Database menerima dua hal: kerangka query yang udah selesai dibaca, lalu",
                    "daftar nilainya. Nilai yang datang belakangan nggak pernah dibaca lagi",
                    "sebagai perintah. Isian seperti dua baris ini pun tetap dianggap satu",
                    "potong teks yang dicari di kolom sandi, dan hasilnya nol baris:",
                    "  ' OR '1'='1",
                    "  '; DROP TABLE pengguna; --",
                    "",
                    "Jadi placeholder itu beda dengan \"escape otomatis\". Bedanya besar:",
                    "  escape -> teksnya tetap disambung, cuma karakter bahaya dipagari.",
                    "  bind   -> teksnya TIDAK PERNAH disambung sama sekali.",
                    "",
                    "Mungkin kamu berpikir, \"Ya udah, buang aja tanda kutipnya.\" Itu nggak",
                    "pernah cukup:",
                    "  - Nilai angka nggak butuh kutip. WHERE id = 5 OR 1=1 tembus tanpa satu",
                    "    pun tanda kutip.",
                    "  - Tanda kutip bisa ditulis dengan banyak cara: digandakan, diawali",
                    "    backslash, atau lewat penyandian karakter. Filter buatan sendiri",
                    "    selalu ketinggalan satu kasus.",
                    "  - Yang menulis parser SQL, yaitu bagian yang membaca query, adalah",
                    "    pembuat database, bukan kamu. Jangan coba-coba menebak apa yang",
                    "    bakal dia anggap perintah.",
                    "",
                    "Di Java, lubang ? diisi lewat PreparedStatement, kelas bawaan JDBC.",
                    "Materi Index, Normalisasi & Best Practice menyarankan JDBC dan Spring",
                    "tapi belum menyebut kelas ini. Padahal ini bentuk yang benar:",
                    "",
                    "  String sql = \"SELECT id, nama FROM pengguna WHERE email = ? AND aktif = ?\";",
                    "  try (PreparedStatement ps = koneksi.prepareStatement(sql)) {",
                    "      ps.setString(1, emailDariForm);   // nomor mulai dari 1, bukan 0",
                    "      ps.setBoolean(2, true);",
                    "      ResultSet rs = ps.executeQuery();",
                    "  }",
                    "",
                    "Saudaranya, Statement (tanpa \"Prepared\"), menerima query jadi dalam",
                    "bentuk satu string utuh. Kalau kamu lihat Statement dipakai bersama",
                    "query yang disambung pakai +, anggap itu tanda bahaya. Bonusnya,",
                    "PreparedStatement yang dipakai berulang juga lebih cepat, karena rencana",
                    "query-nya nggak disusun ulang tiap kali dipanggil.",
                    "",
                    "Kalau nanti kamu pakai JPA/Hibernate atau Spring Data, kamu jarang",
                    "menulis ini sendiri. ORM bikin PreparedStatement di belakang layar untuk",
                    "setiap findByEmail(...). Tapi begitu kamu menulis query manual dengan",
                    "@Query atau createNativeQuery, tanggung jawabnya kembali ke kamu.",
                ],
            },
            {
                "heading": "Yang tidak bisa dijadikan parameter, dan hak akses (DCL)",
                "body": [
                    "Placeholder cuma bisa dipakai untuk nilai. Bagian-bagian ini nggak",
                    "pernah bisa diganti ?, dan kalau dicoba, hasilnya error sintaks:",
                    "  - nama tabel dan nama kolom,",
                    "  - kolom dan arah urutan di ORDER BY (ASC atau DESC),",
                    "  - kata kunci SQL apa pun.",
                    "",
                    "Alasannya sama dengan alasan placeholder aman. Kerangka query udah",
                    "dibaca dan direncanakan sebelum nilainya datang, dan database nggak bisa",
                    "merencanakan cara membaca tabel yang namanya belum diketahui.",
                    "",
                    "Cara yang benar adalah daftar putih (whitelist), bukan menyambung",
                    "string:",
                    "  kolom_boleh = {\"nama\": \"nama\", \"nilai\": \"ipk\", \"tanggal\": \"tanggal\"}",
                    "  kolom = kolom_boleh.get(pilihan_pengguna)",
                    "  if kolom is None:",
                    "      raise ValueError(\"kolom tidak dikenal\")",
                    "  sql = f\"SELECT nim, nama FROM mahasiswa ORDER BY {kolom} DESC\"",
                    "",
                    "Yang disambung ke query adalah salah satu nilai dari daftar yang kamu",
                    "tulis sendiri. Masukan pengguna cuma dipakai untuk memilih dari daftar",
                    "itu, dan nggak pernah masuk ke query. Bedanya tipis, tapi menentukan.",
                    "",
                    "Lapisan pertahanan kedua adalah DCL (Data Control Language). Kategori",
                    "ini disebut sekilas di materi pertama dan belum muncul lagi sejak itu.",
                    "Isinya cuma satu urusan: siapa boleh melakukan apa.",
                ],
                "code": """-- Sintaks MySQL. SQLite tidak punya sistem user sama sekali:
-- hak aksesnya adalah hak akses BERKAS database di sistem operasi.

-- 1. Buat user khusus untuk aplikasi (bukan memakai root!).
CREATE USER 'app_toko'@'localhost' IDENTIFIED BY 'sandi-panjang-acak';

-- 2. Beri hak SECUKUPNYA saja, di satu database saja.
GRANT SELECT, INSERT, UPDATE ON toko.* TO 'app_toko'@'localhost';

-- Cara membacanya:  GRANT <hak apa> ON <di mana> TO <siapa>
--   SELECT, INSERT, UPDATE -> hak apa saja yang diberikan
--   toko.*                 -> semua tabel di database 'toko'
--   'app_toko'@'localhost' -> nama user @ dari mana ia boleh menyambung
--                             ('%' berarti dari mesin mana pun)

-- Hak bisa dipersempit sampai satu tabel, bahkan satu kolom.
GRANT SELECT ON toko.produk TO 'app_toko'@'localhost';
GRANT SELECT (id, nama) ON toko.pelanggan TO 'app_toko'@'localhost';

-- User laporan: boleh baca, tidak boleh mengubah apa pun.
CREATE USER 'pelapor'@'%' IDENTIFIED BY 'sandi-laporan';
GRANT SELECT ON toko.* TO 'pelapor'@'%';

-- Mencabut hak yang terlanjur diberikan (perhatikan: FROM, bukan TO).
REVOKE UPDATE ON toko.* FROM 'app_toko'@'localhost';

-- Memeriksa hak seseorang, dan menghapus user.
SHOW GRANTS FOR 'app_toko'@'localhost';
DROP USER 'pelapor'@'%';

-- FLUSH PRIVILEGES cuma perlu kalau tabel hak akses disunting LANGSUNG
-- dengan UPDATE. GRANT dan REVOKE sudah berlaku seketika. Banyak tutorial
-- menempelkannya di mana-mana karena kebiasaan, bukan karena dibutuhkan.
FLUSH PRIVILEGES;""",
            },
            {
                "body": [
                    "Prinsip hak paling kecil (least privilege) artinya tiap user database",
                    "cuma dikasih hak secukupnya supaya pekerjaannya jalan. Nggak lebih.",
                    "",
                    "Aplikasi nggak boleh terhubung ke database sebagai root, karena root",
                    "boleh DROP DATABASE. Satu lubang injeksi di satu halaman pencarian udah",
                    "cukup untuk menghapus semuanya. Kalau user-nya cuma punya hak SELECT,",
                    "INSERT, dan UPDATE di satu database, perintah DROP TABLE yang disusupkan",
                    "bakal ditolak. Kerusakannya terbatas, walaupun kode aplikasinya nggak",
                    "sempurna.",
                    "",
                    "Karena itu satu aplikasi sering punya lebih dari satu koneksi database:",
                    "  - Koneksi harian, dengan hak SELECT, INSERT, dan UPDATE. Dipakai 99%",
                    "    waktu.",
                    "  - Koneksi migrasi, dengan hak CREATE, ALTER, dan DROP. Cuma dipakai",
                    "    waktu deploy, untuk menjalankan skrip yang mengubah struktur tabel.",
                    "  - Koneksi laporan, cuma SELECT. Sering diarahkan ke replika baca",
                    "    (salinan database khusus untuk dibaca), supaya query berat nggak",
                    "    mengganggu pengguna.",
                    "",
                    "Akibatnya, query yang udah benar pun bisa gagal. Kenali pesan error-nya:",
                    "  MySQL      : ERROR 1142 (42000): DELETE command denied to user",
                    "               'app_toko'@'localhost' for table 'produk'",
                    "  PostgreSQL : ERROR: permission denied for table produk",
                    "",
                    "Pesan itu bukan soal sintaks atau salah ketik, dan nggak bakal hilang",
                    "walaupun query-nya kamu tulis ulang seratus kali. Artinya user-nya",
                    "memang nggak dikasih hak itu. Orang sering menghabiskan sejam",
                    "memperbaiki SQL yang sebetulnya udah benar. Begitu kamu lihat kata",
                    "denied atau permission, berhenti mengedit query. Jalankan SHOW GRANTS",
                    "dulu.",
                    "",
                    "Kebiasaan lain yang perlu ikut:",
                    "  1. Jangan pernah menyimpan sandi pengguna sebagai teks biasa. Simpan",
                    "     hasil hash-nya, yaitu hasil olahan satu arah yang nggak bisa",
                    "     dibalik jadi sandi asli. Pakai bcrypt atau argon2, bukan MD5 atau",
                    "     SHA1 polos. Cocokkan sandinya di kode aplikasi, bukan dengan WHERE",
                    "     sandi = '...'. Kalau database bocor, yang bocor nggak boleh",
                    "     langsung berupa sandi semua orang.",
                    "  2. Sandi database sendiri (yang ditulis di IDENTIFIED BY) jangan ikut",
                    "     ke Git. Simpan di variabel lingkungan atau di berkas konfigurasi",
                    "     yang diabaikan Git. Repositori publik penuh dengan sandi yang lupa",
                    "     dihapus.",
                    "  3. Ambil kolom seperlunya. SELECT * bisa ikut membawa kolom hash sandi",
                    "     dan nomor identitas ke log aplikasi dan ke respons API tanpa",
                    "     sengaja.",
                    "  4. Catat perubahan penting: siapa mengubah apa, dan kapan. Bisa lewat",
                    "     log di aplikasi, atau tabel log yang diisi TRIGGER (lihat materi",
                    "     View, Stored Procedure & Trigger). Tanpa catatan itu, kalau ada",
                    "     data hilang, kamu nggak punya petunjuk apa pun untuk ditelusuri.",
                ],
            },
        ],
    },
    {
        "title": "16. Membaca EXPLAIN & Rencana Eksekusi",
        "sections": [
            {
                "body": [
                    "SQL itu bahasa deklaratif. Artinya kamu menulis apa yang kamu mau, bukan",
                    "cara mengambilnya. Misalnya \"ambil nama mahasiswa Informatika beserta",
                    "nilainya\", udah, itu aja. Kamu nggak pernah menyuruh database membaca",
                    "tabel A dulu atau memakai index B.",
                    "",
                    "Yang memilih caranya adalah query optimizer, bagian di dalam database",
                    "yang menyusun langkah kerja. Optimizer memutuskan tabel mana yang dibaca",
                    "duluan, index mana yang dipakai (atau malah diabaikan), bagaimana dua",
                    "tabel disatukan, dan perlu atau nggaknya bikin tabel sementara.",
                    "",
                    "Kumpulan keputusan itu disebut rencana eksekusi (execution plan).",
                    "EXPLAIN adalah cara menanyakan ke database: \"Query ini mau kamu kerjakan",
                    "bagaimana?\"",
                    "",
                    "Ini penting karena dua query yang hasilnya sama persis bisa beda",
                    "kecepatan sampai seribu kali, dan bedanya cuma di rencananya. Tanpa",
                    "membaca rencana, \"optimasi\" cuma tebak-tebakan. Orang menambah index",
                    "asal-asalan, lalu bingung kenapa query-nya tetap lambat, sementara",
                    "INSERT-nya malah ikut melambat.",
                    "",
                    "Ada tiga database dengan perintah yang mirip, jangan sampai tertukar:",
                    "  MySQL       EXPLAIN <query>            -> rencana saja, query TIDAK jalan.",
                    "              EXPLAIN ANALYZE <query>    -> query DIJALANKAN, lalu dilaporkan.",
                    "  PostgreSQL  EXPLAIN <query>            -> merencanakan saja.",
                    "              EXPLAIN ANALYZE <query>    -> query DIJALANKAN sungguhan.",
                    "  SQLite      EXPLAIN QUERY PLAN <query> -> ringkasan rencana, tidak jalan.",
                    "              EXPLAIN <query>            -> BUKAN yang kamu cari: itu bytecode",
                    "                                            mesin virtual SQLite,",
                    "                                            belasan baris",
                    "                                            opcode seperti OpenRead dan",
                    "                                            Rewind.",
                    "",
                    "Jebakan: EXPLAIN ANALYZE betul-betul menjalankan query-nya, jadi bisa",
                    "merusak data. 'EXPLAIN ANALYZE DELETE FROM pesanan WHERE ...'",
                    "betul-betul menghapus barisnya. Kalau yang mau kamu analisis adalah",
                    "perintah yang mengubah data, bungkus dengan transaction (lihat materi",
                    "Transaction), lalu batalkan:",
                    "",
                    "  BEGIN;",
                    "  EXPLAIN ANALYZE DELETE FROM pesanan WHERE status = 'batal';",
                    "  ROLLBACK;",
                ],
            },
            {
                "heading": "Sesi MySQL: satu baris rencana untuk tiap tabel",
                "code": """mysql> EXPLAIN SELECT m.nama, n.skor
    ->   FROM mahasiswa m
    ->   JOIN nilai n ON n.nim = m.nim
    ->  WHERE m.jurusan = 'Informatika'\\G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: m
   partitions: NULL
         type: ALL
possible_keys: NULL
          key: NULL
      key_len: NULL
          ref: NULL
         rows: 9821
     filtered: 10.00
        Extra: Using where
*************************** 2. row ***************************
           id: 1
  select_type: SIMPLE
        table: n
   partitions: NULL
         type: ref
possible_keys: idx_nim
          key: idx_nim
      key_len: 41
          ref: kampus.m.nim
         rows: 4
     filtered: 100.00
        Extra: NULL
2 rows in set, 1 warning (0.00 sec)""",
            },
            {
                "heading": "Membaca keluaran MySQL kolom demi kolom",
                "body": [
                    "Tanpa \\G di ujung query, MySQL mencetak rencananya sebagai tabel selebar",
                    "120-an karakter, dan tampilannya berantakan di layar sempit. \\G",
                    "memutarnya jadi satu kolom per baris. Isinya tetap sama persis.",
                    "",
                    "Satu \"row\" di keluaran ini artinya satu tabel yang dibaca, bukan satu",
                    "baris data. Query di atas menyentuh dua tabel, jadi rencananya punya dua",
                    "row.",
                    "",
                    "Tulisan \"1 warning\" di baris terakhir bukan tanda ada yang salah. MySQL",
                    "8 selalu menyimpan versi query yang udah dia tulis ulang di situ, dan",
                    "kamu bisa melihatnya dengan SHOW WARNINGS;.",
                    "",
                    "Arti tiap kolomnya:",
                    "  - id: nomor SELECT-nya. Angka yang sama berarti satu tingkat. Angka",
                    "    lebih besar berarti lebih dalam (subquery), dan yang paling besar",
                    "    dikerjakan duluan.",
                    "  - select_type: SIMPLE (tanpa subquery atau union), PRIMARY, SUBQUERY,",
                    "    DERIVED (subquery di FROM), UNION, dan DEPENDENT SUBQUERY. Yang",
                    "    terakhir artinya subquery-nya diulang untuk setiap baris, jadi",
                    "    mahal.",
                    "  - table: tabel, atau aliasnya, yang dibaca di langkah ini.",
                    "  - type: cara barisnya diambil. Ini kolom paling penting di seluruh",
                    "    keluaran.",
                    "  - possible_keys: index yang mungkin dipakai. NULL artinya nggak ada",
                    "    kandidat sama sekali.",
                    "  - key: index yang betul-betul dipakai. Kalau key NULL padahal",
                    "    possible_keys terisi, artinya optimizer udah menimbang lalu menolak",
                    "    semua kandidatnya.",
                    "  - key_len: berapa byte dari index itu yang terpakai. Di index",
                    "    gabungan, angka ini yang memberi tahu berapa kolom yang betul-betul",
                    "    kepakai. Untuk teks utf8mb4, hitungannya 4 byte per karakter,",
                    "    ditambah 2 byte kalau tipenya VARCHAR, ditambah 1 byte kalau",
                    "    kolomnya boleh NULL. Angka 41 di contoh tadi cocok dengan satu kolom",
                    "    nim CHAR(10) yang boleh NULL: 10 x 4 + 1 = 41. Jadi yang dipakai",
                    "    tepat satu kolom, yaitu nim.",
                    "  - ref: nilai apa yang dicocokkan ke index. Isinya 'const' kalau berupa",
                    "    konstanta, atau nama kolom tabel lain (di sini kampus.m.nim) kalau",
                    "    datang dari JOIN.",
                    "  - rows: perkiraan jumlah baris yang bakal disentuh. Ini tebakan, bukan",
                    "    hasil hitungan.",
                    "  - filtered: perkiraan persen baris yang lolos WHERE. rows x filtered /",
                    "    100 adalah perkiraan jumlah baris yang diteruskan ke langkah",
                    "    berikutnya.",
                    "  - Extra: catatan tambahan. Masalahnya justru sering kelihatan di sini.",
                    "",
                    "Isi kolom type, diurutkan dari yang terburuk ke yang terbaik:",
                    "  - ALL: seluruh tabel dipindai baris demi baris (full table scan).",
                    "  - index: seluruh index dipindai. Lebih ramping dari ALL, tapi tetap",
                    "    semuanya.",
                    "  - range: cuma sepotong rentang index yang dibaca (BETWEEN, >, <, IN,",
                    "    LIKE 'a%').",
                    "  - ref: lompat langsung ke baris yang cocok lewat index yang nilainya",
                    "    boleh berulang.",
                    "  - eq_ref: persis satu baris untuk tiap baris tabel sebelumnya (JOIN ke",
                    "    PRIMARY KEY).",
                    "  - const: satu baris, ditemukan sekali di awal (WHERE nim = 'M001' pada",
                    "    primary key).",
                    "",
                    "Nilai ALL nggak selalu masalah. Di tabel 200 baris, ALL justru wajar,",
                    "karena membaca semuanya lebih murah daripada bolak-balik ke index. Yang",
                    "gawat adalah ALL di tabel besar, apalagi di dalam JOIN. Di situ jumlah",
                    "baris tabel pertama dikalikan dengan pemindaian tabel kedua. Di contoh",
                    "tadi, tabel m masih ALL karena belum ada index untuk jurusan. Itu hal",
                    "yang jelas bisa diperbaiki, dan angka rows 9821 menunjukkan seberapa",
                    "mahal harganya.",
                    "",
                    "Isi kolom Extra yang perlu kamu kenali:",
                    "  - Using where: baris yang udah dibaca masih disaring lagi. Ini normal,",
                    "    bukan tanda bahaya.",
                    "  - Using index: namanya menjebak. Artinya bukan \"ada index yang",
                    "    dipakai\", karena itu urusan kolom key. Using index artinya covering",
                    "    index: semua kolom yang diminta udah ada di dalam index, jadi",
                    "    tabelnya nggak perlu dibuka sama sekali. Ini kabar paling baik yang",
                    "    bisa muncul di kolom Extra.",
                    "  - Using filesort: hasilnya harus diurutkan ulang, karena nggak ada",
                    "    index yang urutannya cocok dengan ORDER BY. Namanya menipu, karena",
                    "    prosesnya nggak selalu menyentuh disk. Solusinya index yang urutan",
                    "    kolomnya sama persis dengan ORDER BY-nya.",
                    "  - Using temporary: MySQL menampung hasil sementara di tabel sementara.",
                    "    Biasanya gara-gara GROUP BY, DISTINCT, atau ORDER BY yang beda dari",
                    "    GROUP BY. Kalau 'Using temporary; Using filesort' muncul bareng di",
                    "    tabel besar, itu kombinasi yang paling sering bikin query jalan",
                    "    merangkak.",
                ],
            },
            {
                "heading": "PostgreSQL: rencananya berbentuk pohon",
                "body": [
                    "PostgreSQL nggak menampilkan rencananya sebagai tabel, tapi sebagai",
                    "pohon. Cara membacanya cuma dua aturan:",
                    "  1. Baris yang menjorok paling dalam dikerjakan paling dulu. Baca dari",
                    "     dalam ke luar, dari bawah ke atas. Hasil tiap node (simpul di pohon",
                    "     itu) mengalir naik ke induknya.",
                    "  2. Tanda '->' menandai sebuah anak. Node tanpa '->' di baris paling",
                    "     atas adalah node terakhir, yang menghasilkan baris untukmu.",
                    "",
                    "Node yang membaca tabel:",
                    "  - Seq Scan: seluruh tabel dibaca. Kembarannya type ALL di MySQL.",
                    "  - Index Scan: index ditelusuri, lalu barisnya diambil satu per satu",
                    "    dari tabel.",
                    "  - Index Only Scan: semua kolom yang diminta ada di index, jadi tabel",
                    "    nggak dibuka. Kembarannya Using index di MySQL.",
                    "  - Bitmap Heap Scan dan Bitmap Index Scan: dipakai kalau jumlah baris",
                    "    yang cocok terlalu banyak untuk Index Scan, tapi terlalu sedikit",
                    "    untuk Seq Scan. Alamat baris dikumpulkan dulu jadi bitmap dan",
                    "    diurutkan, baru tabelnya dibaca sekali jalan menurut urutan",
                    "    fisiknya. Ini normal, bukan cacat.",
                    "",
                    "Node yang menyatukan dua tabel:",
                    "  - Nested Loop: untuk tiap baris di sisi luar, cari pasangannya di sisi",
                    "    dalam. Cepat kalau sisi luarnya sedikit dan sisi dalamnya punya",
                    "    index. Jadi bencana kalau sisi luarnya ternyata jutaan baris.",
                    "  - Hash Join: sisi yang lebih kecil dijadikan tabel hash di memori,",
                    "    lalu sisi yang besar dialirkan melewatinya. Ini andalan untuk data",
                    "    banyak yang nggak punya index cocok.",
                    "  - Merge Join: kedua sisi diurutkan dulu (atau memang udah urut), lalu",
                    "    ditelusuri bareng, seperti menyatukan dua daftar absen.",
                    "",
                    "Angka di tiap node:",
                    "  cost=48.60..312.44 -> 48.60 biaya sampai baris PERTAMA keluar, 312.44",
                    "  biaya sampai",
                    "                        baris terakhir. Satuannya bukan detik, bukan",
                    "                        milidetik -",
                    "                        cuma satuan buatan untuk membandingkan antar rencana.",
                    "  rows=392           -> PERKIRAAN jumlah baris keluaran node ini.",
                    "  width=29           -> perkiraan lebar satu baris hasil dalam byte.",
                    "  actual time=a..b   -> waktu nyata (milidetik) sampai baris pertama",
                    "                        dan sampai baris terakhir.",
                    "  rows= di blok actual -> jumlah baris NYATA. Inilah yang dibandingkan",
                    "  dengan tebakan.",
                    "  loops=N            -> node ini dijalankan N kali.",
                    "",
                    "Ingat: actual time dan rows di blok actual adalah rata-rata per loop.",
                    "Jadi 'rows=1 loops=50000' artinya 50.000 baris, dan waktunya juga dikali",
                    "50.000. Jumlahnya bukan 1 baris.",
                    "",
                    "Kebiasaan pertama yang perlu kamu punya: bandingkan rows tebakan dengan",
                    "rows nyata di node yang sama. Di dua rencana berikut, mahasiswa ditebak",
                    "98 baris, padahal nyatanya 2455. Melesetnya 25 kali. Tebakan itu",
                    "mengalir naik, jadi hasil join juga meleset, dari 392 jadi 9820.",
                    "",
                    "Selisih sebesar ini hampir selalu berarti statistik tabelnya udah basi,",
                    "dan optimizer memilih rencana berdasarkan angka yang salah. Solusinya",
                    "satu perintah: ANALYZE nama_tabel; (di MySQL: ANALYZE TABLE nama_tabel;,",
                    "di SQLite: ANALYZE;). Jalankan itu dulu sebelum menambah index. Sering",
                    "kali rencananya langsung berubah sendiri tanpa perlu index baru.",
                ],
                "code": """kampus=# EXPLAIN
kampus-# SELECT m.nama, n.skor
kampus-#   FROM mahasiswa m JOIN nilai n ON n.nim = m.nim
kampus-#  WHERE m.jurusan = 'Informatika';
                              QUERY PLAN
--------------------------------------------------------------------------
 Hash Join  (cost=198.23..1092.61 rows=392 width=29)
   Hash Cond: (n.nim = m.nim)
   ->  Seq Scan on nilai n  (cost=0.00..694.00 rows=40000 width=15)
   ->  Hash  (cost=197.00..197.00 rows=98 width=22)
         ->  Seq Scan on mahasiswa m  (cost=0.00..197.00 rows=98 width=22)
               Filter: (jurusan = 'Informatika'::text)
(6 rows)

kampus=# EXPLAIN (ANALYZE, COSTS OFF)
kampus-# SELECT m.nama, n.skor
kampus-#   FROM mahasiswa m JOIN nilai n ON n.nim = m.nim
kampus-#  WHERE m.jurusan = 'Informatika';
                              QUERY PLAN
--------------------------------------------------------------------------
 Hash Join (actual time=3.914..62.508 rows=9820 loops=1)
   Hash Cond: (n.nim = m.nim)
   ->  Seq Scan on nilai n (actual time=0.014..12.663 rows=40000 loops=1)
   ->  Hash (actual time=3.842..3.843 rows=2455 loops=1)
         Buckets: 4096  Batches: 1  Memory Usage: 165kB
         ->  Seq Scan on mahasiswa m (actual time=0.011..2.904 rows=2455 loops=1)
               Filter: (jurusan = 'Informatika'::text)
               Rows Removed by Filter: 7545
 Planning Time: 0.198 ms
 Execution Time: 64.117 ms
(10 rows)""",
            },
            {
                "heading": "Dari rencana ke perbaikan - dan coba sendiri di SQLite",
                "body": [
                    "Baris 'Rows Removed by Filter: 7545' di rencana tadi adalah petunjuk",
                    "yang paling jelas: 7545 baris dibaca, lalu langsung dibuang. Setiap",
                    "baris yang dibaca cuma untuk dibuang adalah tanda bahwa index mungkin",
                    "dibutuhkan. Begitulah cara mengubah rencana jadi tindakan.",
                    "",
                    "Ada empat perbaikan yang paling sering menjawab rencana yang jelek.",
                    "",
                    "Pertama, index gabungan, dan urutan kolomnya menentukan segalanya. Index",
                    "(angkatan, jurusan) itu seperti buku telepon yang diurutkan per kota,",
                    "lalu per nama. Mencari \"kota Bandung\" bisa. Mencari \"kota Bandung, nama",
                    "Budi\" juga bisa. Tapi mencari \"siapa pun bernama Budi di kota mana pun\"",
                    "nggak bisa, kamu tetap harus baca semuanya. Aturannya: kolom yang",
                    "dipakai dengan '=' ditaruh di depan, sedangkan kolom rentang (>, <,",
                    "BETWEEN) dan kolom ORDER BY ditaruh belakangan. Langkah 3 di program",
                    "bawah membuktikannya.",
                    "",
                    "Kedua, jangan pernah membungkus kolom di WHERE dengan fungsi:",
                    "  X  WHERE upper(jurusan) = 'ELEKTRO'     -- index jurusan mati total",
                    "  X  WHERE YEAR(tanggal) = 2024           -- index tanggal mati total",
                    "",
                    "Index menyimpan nilai kolom apa adanya, bukan hasil fungsinya. Jadi",
                    "database terpaksa menghitung fungsi itu untuk setiap baris dulu. Tulis",
                    "begini:",
                    "  V  WHERE jurusan = 'Elektro'",
                    "  V  WHERE tanggal >= '2024-01-01' AND tanggal < '2025-01-01'",
                    "",
                    "Kalau fungsinya memang nggak bisa dihindari, bikin index untuk",
                    "ekspresinya:",
                    "  CREATE INDEX idx_jurusan_besar ON mahasiswa(upper(jurusan));",
                    "",
                    "Ketiga, OFFSET yang besar makin lambat di tiap halaman, dan EXPLAIN",
                    "memperlihatkannya. LIMIT 20 OFFSET 100000 tetap harus membaca 100.020",
                    "baris, lalu membuang 100.000 yang pertama. Halaman 1 kilat, halaman 5000",
                    "merangkak, padahal query-nya sama. Gantinya keyset pagination, yaitu",
                    "mengingat nilai terakhir dari halaman sebelumnya:",
                    "  X  SELECT * FROM pesanan ORDER BY id LIMIT 20 OFFSET 100000;",
                    "  V  SELECT * FROM pesanan WHERE id > 100000 ORDER BY id LIMIT 20;",
                    "",
                    "Keempat, masalah N+1 query dari ORM. Ini satu-satunya masalah di daftar",
                    "ini yang nggak kelihatan di EXPLAIN. Kode seperti 'for m in mahasiswa:",
                    "print(m.nilai)' menjalankan 1 query untuk daftarnya, lalu 1 query lagi",
                    "untuk tiap baris. 500 mahasiswa berarti 501 query. Di mata EXPLAIN, tiap",
                    "query-nya sempurna (type const, 0.2 ms). Yang bikin lambat adalah",
                    "jumlahnya. Masalah ini ketahuan dari log query atau dari penghitung",
                    "jumlah query, bukan dari rencana. Solusinya satu JOIN, satu WHERE ... IN",
                    "(...), atau fitur eager loading di ORM-nya.",
                    "",
                    "Program di bawah menjalankan semuanya sungguhan di SQLite, dengan 5000",
                    "baris tanpa angka acak. Perhatikan bedanya SCAN (baca semua baris) dan",
                    "SEARCH (lompat langsung lewat index).",
                ],
                "code": """-- Rencana eksekusi bisa dicoba sungguhan di SQLite. Jalankan apa adanya.
CREATE TABLE mahasiswa (
    nim      TEXT PRIMARY KEY,
    nama     TEXT NOT NULL,
    jurusan  TEXT NOT NULL,
    angkatan INTEGER NOT NULL
);

-- Isi 5000 baris tanpa angka acak: semuanya diturunkan dari nomor urut.
WITH RECURSIVE angka(n) AS (
    SELECT 1 UNION ALL SELECT n + 1 FROM angka WHERE n < 5000
)
INSERT INTO mahasiswa
SELECT printf('NIM%04d', n),
       'Mahasiswa ' || n,
       CASE n % 4 WHEN 0 THEN 'Informatika'
                  WHEN 1 THEN 'Sistem Informasi'
                  WHEN 2 THEN 'Elektro'
                  ELSE 'Mesin' END,
       2020 + (n % 5)
FROM angka;

SELECT '1. belum ada index -> SCAN, semua 5000 baris dibaca';
EXPLAIN QUERY PLAN
SELECT nama FROM mahasiswa WHERE angkatan = 2021 AND jurusan = 'Elektro';

CREATE INDEX idx_angkatan_jurusan ON mahasiswa(angkatan, jurusan);

SELECT '2. index (angkatan, jurusan) -> SEARCH, dua kolom kepakai';
EXPLAIN QUERY PLAN
SELECT nama FROM mahasiswa WHERE angkatan = 2021 AND jurusan = 'Elektro';

SELECT '3. hanya jurusan yang difilter -> SCAN lagi (itu kolom KEDUA)';
EXPLAIN QUERY PLAN
SELECT nama FROM mahasiswa WHERE jurusan = 'Elektro';

CREATE INDEX idx_jurusan ON mahasiswa(jurusan);

SELECT '4. sesudah ada index khusus jurusan -> SEARCH';
EXPLAIN QUERY PLAN
SELECT nama FROM mahasiswa WHERE jurusan = 'Elektro';

SELECT '5. kolom dibungkus fungsi -> index diabaikan, SCAN';
EXPLAIN QUERY PLAN
SELECT nama FROM mahasiswa WHERE upper(jurusan) = 'ELEKTRO';

SELECT '6. kolom yang diminta semuanya ada di index -> COVERING INDEX';
EXPLAIN QUERY PLAN
SELECT jurusan, count(*) FROM mahasiswa GROUP BY jurusan;

SELECT '7. ORDER BY tanpa index -> TEMP B-TREE, sepupunya Using filesort';
EXPLAIN QUERY PLAN
SELECT nama FROM mahasiswa ORDER BY nama LIMIT 10;""",
            },
        ],
    },
    {
        "title": "17. Window Function (Fungsi Jendela)",
        "sections": [
            {
                "body": [
                    "Window function menghitung seperti fungsi agregat, tapi barisnya nggak",
                    "diringkas jadi satu. Semua baris asli tetap tampil, dan tiap baris dapat",
                    "kolom tambahan berisi hasil hitungan atas \"jendela\" datanya. Jendela itu",
                    "sekelompok baris yang terkait dengan baris tersebut.",
                    "",
                    "Bedanya dengan GROUP BY:",
                    "  GROUP BY      -> N baris jadi lebih sedikit baris (diringkas).",
                    "  Window Function -> tetap N baris, ditambah kolom baru.",
                    "",
                    "Bentuk umumnya:",
                    "  fungsi() OVER (",
                    "      PARTITION BY kolom   -- (opsional) kelompokkan seperti GROUP BY",
                    "      ORDER BY kolom        -- urutan dalam tiap partisi",
                    "  )",
                    "",
                    "PARTITION BY membagi baris jadi kelompok-kelompok, disebut partisi.",
                    "Hitungannya dimulai ulang di tiap partisi. ORDER BY di dalam OVER",
                    "menentukan urutan baris di dalam partisi.",
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
                "heading": "Frame: bagian OVER yang selama ini tidak terlihat",
                "body": [
                    "Coba lihat lagi SUM(total_penjualan) OVER (ORDER BY bulan). Hasilnya",
                    "kumulatif, padahal nggak ada satu kata pun soal kumulatif di query itu.",
                    "Penyebabnya frame. Setiap OVER punya frame, yaitu potongan baris dari",
                    "partisi yang ikut dihitung. Frame punya nilai bawaan yang nggak ditulis:",
                    "",
                    "  OVER (ORDER BY bulan)",
                    "  sama artinya dengan",
                    "  OVER (ORDER BY bulan",
                    "        RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)",
                    "",
                    "Bacanya: dari baris paling awal sampai baris ini. Jadi hasil kumulatif",
                    "tadi berasal dari frame bawaan, bukan dari sifat SUM.",
                    "",
                    "Kalau OVER sama sekali nggak punya ORDER BY, frame bawaannya seluruh",
                    "partisi. Hasilnya total keseluruhan yang sama di setiap baris:",
                    "  SUM(total_penjualan) OVER ()                   -- total semua bulan",
                    "  SUM(total_penjualan) OVER (PARTITION BY tahun) -- total per tahun",
                    "",
                    "Pasangan ini dipakai untuk menghitung porsi tanpa query kedua:",
                    "  total_penjualan * 100.0 / SUM(total_penjualan) OVER () AS persen",
                    "",
                    "Frame juga boleh kamu tulis sendiri. Bentuk-bentuk yang perlu dikenali:",
                    "  ROWS BETWEEN 6 PRECEDING AND CURRENT ROW",
                    "      -> baris ini dan enam sebelumnya = rata-rata bergerak 7 hari.",
                    "  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW",
                    "      -> kumulatif, ditulis terang-terangan.",
                    "  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING",
                    "      -> seluruh partisi, walaupun ada ORDER BY.",
                    "  ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING",
                    "      -> tiga baris berdampingan: jendela yang ikut bergeser.",
                    "",
                    "ROWS dan RANGE bedanya nyata:",
                    "  - ROWS menghitung baris. '3 PRECEDING' artinya tiga baris ke atas,",
                    "    titik.",
                    "  - RANGE menghitung nilai kolom di ORDER BY. Semua baris yang nilainya",
                    "    sama dianggap satu posisi, dan ikut dihitung sekaligus.",
                    "",
                    "Kalau ada nilai yang seri, RANGE memasukkan semuanya, sedangkan ROWS",
                    "berhenti di salah satunya. Untuk rata-rata bergerak yang jumlah barisnya",
                    "harus pasti, pakai ROWS.",
                ]
            },
            {
                "heading": "Fungsi window lain yang sering muncul",
                "body": [
                    "NTILE(n) membagi tiap partisi jadi n kelompok yang sama besar, lalu",
                    "memberi nomor kelompoknya. NTILE(4) artinya kuartil, NTILE(100) artinya",
                    "persentil.",
                    "  NTILE(4) OVER (ORDER BY ipk DESC) AS kuartil",
                    "  -> 1 untuk seperempat teratas, 4 untuk seperempat terbawah.",
                    "",
                    "FIRST_VALUE, LAST_VALUE, dan NTH_VALUE mengambil nilai dari baris",
                    "tertentu di dalam jendela, bukan nomor peringkatnya.",
                    "  FIRST_VALUE(nama) OVER (PARTITION BY jurusan ORDER BY ipk DESC)",
                    "  -> nama peraih IPK tertinggi jurusan itu, ditempelkan ke SEMUA",
                    "     baris jurusan tersebut, siap dibandingkan per baris.",
                    "",
                    "Jebakan: LAST_VALUE kena masalah frame dari bagian sebelumnya. Query ini",
                    "mengembalikan nama baris itu sendiri (atau baris terakhir yang nilainya",
                    "seri dengannya), bukan nama yang terakhir di jurusan:",
                    "  LAST_VALUE(nama) OVER (PARTITION BY jurusan ORDER BY ipk DESC)",
                    "",
                    "Penyebabnya, frame bawaan berhenti di CURRENT ROW. Jadi \"yang terakhir",
                    "di dalam jendela\" memang baris ini. Cara memperbaikinya, tulis frame",
                    "penuh:",
                    "  LAST_VALUE(nama) OVER (PARTITION BY jurusan ORDER BY ipk DESC",
                    "      ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)",
                    "",
                    "FIRST_VALUE aman, karena frame bawaannya memang dimulai dari awal.",
                    "",
                    "PERCENT_RANK() dan CUME_DIST() menjawab posisi relatif, bukan nomor",
                    "urut:",
                    "  - PERCENT_RANK() dihitung dari (peringkat - 1) / (jumlah baris - 1).",
                    "    Baris pertama selalu 0. Baris terakhir bernilai 1, asalkan nilainya",
                    "    nggak seri dengan baris di atasnya.",
                    "  - CUME_DIST() adalah porsi baris yang nilainya <= baris ini. Hasilnya",
                    "    selalu lebih dari 0, dan tepat 1 di baris terakhir.",
                    "",
                    "Keduanya bisa menjawab \"anak ini masuk 10% teratas atau nggak?\", nggak",
                    "peduli pesertanya 30 orang atau 30.000.",
                    "",
                    "Klausa WINDOW dipakai kalau OVER (...) yang sama ditulis berkali-kali di",
                    "satu SELECT. Kasih nama sekali, lalu pakai namanya. Letaknya sesudah",
                    "HAVING, sebelum ORDER BY.",
                ]
            },
            {
                "heading": "Klausa WINDOW & frame yang ditulis sendiri",
                "code": """-- Tanpa klausa WINDOW: definisi jendela yang sama ditulis tiga kali.
SELECT nama, jurusan, ipk,
       ROW_NUMBER() OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS no,
       RANK()       OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS rk,
       NTILE(4)     OVER (PARTITION BY jurusan ORDER BY ipk DESC) AS kuartil
FROM mahasiswa;

-- Dengan klausa WINDOW: ditulis sekali, namanya dipakai berulang.
SELECT nama, jurusan, ipk,
       ROW_NUMBER()      OVER w AS no,
       RANK()            OVER w AS rk,
       NTILE(4)          OVER w AS kuartil,
       FIRST_VALUE(nama) OVER w AS juara_jurusan
FROM mahasiswa
WINDOW w AS (PARTITION BY jurusan ORDER BY ipk DESC)
ORDER BY jurusan, ipk DESC;

-- Frame boleh ditambahkan di atas jendela bernama, saat dipakai.
SELECT bulan, total_penjualan,
       AVG(total_penjualan) OVER (w ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
           AS rata_3_bulan,
       SUM(total_penjualan) OVER (w ROWS BETWEEN UNBOUNDED PRECEDING
                                       AND CURRENT ROW) AS kumulatif
FROM penjualan_bulanan
WINDOW w AS (ORDER BY bulan);"""
            },
            {
                "body": [
                    "Window function paling berguna untuk:",
                    "  - bikin leaderboard atau peringkat per kategori,",
                    "  - laporan running total (kumulatif) penjualan atau keuangan,",
                    "  - membandingkan nilai bulan ini dengan bulan lalu (LAG/LEAD),",
                    "  - mengambil TOP-N per grup, misalnya 3 produk terlaris di tiap",
                    "    kategori.",
                    "",
                    "Window function dijalankan sesudah WHERE dan GROUP BY, tapi sebelum",
                    "ORDER BY terakhir. Karena itu window function nggak bisa langsung",
                    "dipakai di WHERE. Query-nya perlu dibungkus subquery dulu, seperti",
                    "contoh TOP 3 di atas.",
                ]
            },
        ],
    },
    {
        "title": "18. Common Table Expression (CTE) & Recursive Query",
        "sections": [
            {
                "body": [
                    "CTE (Common Table Expression) adalah semacam tabel sementara yang kamu",
                    "definisikan pakai klausa WITH. Tabel itu cuma berlaku untuk satu query.",
                    "",
                    "Kelebihan CTE dibanding subquery biasa:",
                    "  1. Lebih gampang dibaca, karena query yang rumit dipecah jadi",
                    "     blok-blok yang punya nama.",
                    "  2. Bisa dipakai berkali-kali dalam query yang sama.",
                    "  3. Bisa dipakai untuk query rekursif, yaitu query yang memanggil",
                    "     dirinya sendiri.",
                    "",
                    "Bentuk dasarnya:",
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
                    "Recursive CTE paling berguna untuk data yang bentuknya pohon atau",
                    "bertingkat (hierarki), misalnya:",
                    "  - struktur organisasi (atasan dan bawahan),",
                    "  - kategori bertingkat (kategori > sub-kategori > sub-sub-kategori),",
                    "  - komentar bersarang (komentar, balasan, balasan dari balasan).",
                    "",
                    "Recursive CTE selalu punya dua bagian yang dipisah UNION ALL:",
                    "  1. Anchor member: query awal, yaitu titik mulainya.",
                    "  2. Recursive member: query yang merujuk ke CTE itu sendiri. Query ini",
                    "     diulang terus, dan berhenti otomatis kalau udah nggak ada baris",
                    "     baru yang cocok.",
                ]
            },
        ],
    },
    {
        "title": "19. View, Stored Procedure & Trigger",
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
        "title": "20. Bahasa Prosedural di Database",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menjanjikan bahwa procedure 'bisa punya parameter,",
                    "percabangan, dan perulangan' - lalu tidak menunjukkan satu pun",
                    "sintaksnya. Materi ini yang menutupnya. Kunci jawaban Latihan 11 pun",
                    "sudah memakai IF ... THEN ... END IF yang belum pernah diajarkan.",
                    "",
                    "SQL yang kamu pakai sejauh ini DEKLARATIF: kamu menyebutkan hasil apa",
                    "yang diinginkan, database yang memilih caranya. Tidak ada 'kalau",
                    "begini, lakukan itu'. Tidak ada 'ulangi sampai habis'. Begitu logika",
                    "seperti itu dibutuhkan DI DALAM database - trigger yang harus",
                    "memutuskan menolak atau menerima, procedure yang harus mengulang -",
                    "SQL murni kehabisan kata. Karena itu setiap database menambahkan",
                    "bahasa prosedural sendiri di atas SQL:",
                    "  MySQL / MariaDB -> tanpa nama khusus, disebut 'stored program'",
                    "  PostgreSQL      -> PL/pgSQL",
                    "  Oracle          -> PL/SQL",
                    "  SQL Server      -> T-SQL",
                    "",
                    "Bagian SQL inilah yang PALING TIDAK portabel. Query SELECT-mu bisa",
                    "pindah database hampir tanpa diubah; procedure tidak. Fakta itu yang",
                    "menentukan bagian akhir materi ini, waktu membahas kapan sebaiknya",
                    "semua ini justru tidak dipakai.",
                    "",
                    "DELIMITER - dan kenapa ia tampak melanggar aturan titik koma",
                    "  Badan procedure berisi titik komanya SENDIRI. Klien mysql memotong",
                    "  kiriman ke server di setiap titik koma, jadi CREATE PROCEDURE",
                    "  terpotong di ';' PERTAMA di dalam badannya. Server menerima separuh",
                    "  perintah yang belum utuh dan menjawab ERROR 1064.",
                    "",
                    "  DELIMITER // menyuruh KLIEN: 'mulai sekarang yang mengakhiri",
                    "  kiriman adalah //, bukan ;'. Setelah procedure selesai ditulis,",
                    "  DELIMITER ; mengembalikan keadaannya seperti semula.",
                    "",
                    "  Jadi aturan di materi pertama - setiap statement diakhiri titik",
                    "  koma - tidak dilanggar sama sekali. Titik koma di dalam",
                    "  BEGIN ... END tetap wajib. Yang berubah cuma tanda yang dipakai",
                    "  KLIEN untuk memutuskan 'kiriman ini sudah utuh'.",
                    "",
                    "  DELIMITER bukan perintah SQL: ia tidak pernah sampai ke server,",
                    "  tidak ada di standar SQL, tidak dikenal psql, dan kalau kamu",
                    "  menuliskannya lewat JDBC di kode Java justru jadi error - di sana",
                    "  satu perintah memang dikirim utuh, tidak ada yang memotong.",
                    "",
                    "PostgreSQL menyelesaikan masalah yang sama dengan cara lain: badan",
                    "fungsi dikirim sebagai STRING, jadi tidak ada yang perlu dipotong.",
                    "",
                    "  CREATE OR REPLACE FUNCTION naikkan_ipk(p_nim INT)",
                    "  RETURNS void AS $$",
                    "  BEGIN",
                    "      UPDATE mahasiswa SET ipk = ipk + 0.1 WHERE nim = p_nim;",
                    "  END;",
                    "  $$ LANGUAGE plpgsql;",
                    "",
                    "  $$ ... $$ itu 'dollar quoting': tanda kutip yang isinya tidak perlu",
                    "  di-escape, supaya petik tunggal di dalam badan fungsi tidak perlu",
                    "  digandakan. Boleh diberi label kalau di dalamnya ada $$ lagi:",
                    "  $badan$ ... $badan$. LANGUAGE plpgsql wajib ditulis, karena",
                    "  PostgreSQL menerima badan fungsi dalam beberapa bahasa berbeda.",
                    "",
                    "BEGIN ... END adalah BLOK kode - bukan transaction",
                    "  Satu kata, dua makna, dan ini benar-benar menjebak. Di dalam stored",
                    "  program, BEGIN membuka blok yang ditutup END, persis seperti { }",
                    "  di Java. Di luar stored program, BEGIN memulai transaction (materi",
                    "  Transaction & Isolation Level).",
                    "",
                    "  Sekarang jelas kenapa materi transaction memakai START TRANSACTION,",
                    "  bukan BEGIN: bentuk panjangnya tidak pernah bisa disalahartikan.",
                    "  Pakai kebiasaan itu selamanya.",
                ],
            },
            {
                "heading": "Procedure MySQL: parameter, variabel lokal, percabangan",
                "body": [
                    "Tiga hal yang perlu diperhatikan saat membaca kode di bawah:",
                    "",
                    "1. Mode parameter - ARAH data, bukan operator IN yang kamu pakai di",
                    "   WHERE:",
                    "     IN    nilai masuk ke procedure; diubah di dalam pun tidak",
                    "           berpengaruh ke pemanggilnya",
                    "     OUT   tidak membawa nilai masuk (selalu NULL di awal); gunanya",
                    "           MENGEMBALIKAN hasil",
                    "     INOUT membawa nilai masuk DAN membawa hasilnya keluar",
                    "   'IN p_jurusan VARCHAR(50)' dan 'WHERE jurusan IN (...)' cuma",
                    "   kebetulan memakai kata yang sama.",
                    "",
                    "2. DECLARE hanya boleh di ATAS blok, sebelum statement lain. Menaruh",
                    "   satu DECLARE setelah sebuah SET itu error sintaks, bukan sekadar",
                    "   gaya penulisan yang jelek. Variabel lokal punya tipe, sama seperti",
                    "   kolom tabel.",
                    "",
                    "3. ELSEIF ditulis SATU KATA. 'ELSE IF' (dua kata) dibaca MySQL",
                    "   sebagai ELSE yang berisi IF baru - dan IF baru itu menuntut",
                    "   END IF-nya sendiri. Kurang satu END IF adalah error paling",
                    "   membingungkan buat pemula, karena pesannya menunjuk baris END di",
                    "   paling bawah, jauh dari sumber masalahnya. (PL/pgSQL menulisnya",
                    "   ELSIF; MySQL tidak menerima ejaan itu.)",
                ],
                "code": """DELIMITER //

CREATE PROCEDURE ringkas_jurusan(
    IN    p_jurusan VARCHAR(50),
    OUT   p_jumlah  INT,
    INOUT p_catatan VARCHAR(200)
)
BEGIN
    DECLARE v_rata DECIMAL(4,2) DEFAULT 0.00;

    -- SELECT ... INTO mengisi variabel, bukan menampilkan hasil.
    -- Aman di sini karena COUNT/AVG SELALU mengembalikan tepat satu baris.
    SELECT COUNT(*), IFNULL(AVG(ipk), 0.00)
      INTO p_jumlah, v_rata
      FROM mahasiswa
     WHERE jurusan = p_jurusan;

    IF p_jumlah = 0 THEN
        SET p_catatan = CONCAT(p_catatan, ' | jurusan kosong');
    ELSEIF v_rata >= 3.50 THEN
        SET p_catatan = CONCAT(p_catatan, ' | rata-rata unggul');
    ELSE
        SET p_catatan = CONCAT(p_catatan, ' | rata-rata biasa');
    END IF;
END //

DELIMITER ;

-- OUT dan INOUT butuh WADAH, tidak bisa diisi nilai mentah.
-- @catatan variabel sesi: tanpa DECLARE, hidup sampai koneksi ditutup.
SET @catatan = 'laporan';
CALL ringkas_jurusan('Informatika', @jumlah, @catatan);
SELECT @jumlah AS jumlah, @catatan AS catatan;""",
            },
            {
                "heading": "Perulangan, dan CASE yang berupa statement",
                "body": [
                    "Tiga bentuk perulangan. Yang membedakan: KAPAN syaratnya diperiksa?",
                    "",
                    "  WHILE ... DO ... END WHILE",
                    "      syarat diperiksa DULU -> badan bisa nol kali dijalankan",
                    "  REPEAT ... UNTIL ... END REPEAT",
                    "      syarat diperiksa di AKHIR -> badan jalan minimal SEKALI",
                    "  LOOP ... END LOOP",
                    "      tidak ada syarat sama sekali -> WAJIB dihentikan sendiri",
                    "      dengan LEAVE, kalau tidak ia berputar selamanya",
                    "",
                    "LEAVE keluar dari loop (seperti break). ITERATE lompat ke putaran",
                    "berikutnya (seperti continue). Keduanya menyebut LABEL, jadi LOOP yang",
                    "mau di-LEAVE harus diberi nama lebih dulu ('putaran:' di kode bawah).",
                    "",
                    "  Jebakan klasik: ITERATE ditulis SEBELUM baris yang menaikkan",
                    "  penghitung, sehingga penghitungnya tidak pernah naik. Procedure-nya",
                    "  lalu menggantung di server sampai koneksinya diputus paksa - tidak",
                    "  ada Ctrl+C di dalam database.",
                    "",
                    "  Perhatikan juga UNTIL: tidak diakhiri titik koma. Yang mengakhiri",
                    "  statement-nya adalah END REPEAT.",
                    "",
                    "CASE punya DUA wujud, dan orang sering menyangka keduanya sama:",
                    "",
                    "  CASE sebagai EKSPRESI - dipakai di dalam SELECT, hasilnya NILAI:",
                    "    SELECT nama, CASE WHEN ipk >= 3.5 THEN 'unggul'",
                    "                      ELSE 'biasa' END AS status",
                    "    FROM mahasiswa;",
                    "",
                    "  CASE sebagai STATEMENT - hanya di dalam stored program, tiap",
                    "  cabangnya berisi PERINTAH:",
                    "    CASE WHEN n = 0 THEN SET hasil = 'kosong'; ... END CASE;",
                    "",
                    "  Bedanya bukan cuma gaya penulisan. CASE ekspresi tanpa ELSE yang",
                    "  tidak cocok apa pun menghasilkan NULL dengan tenang. CASE STATEMENT",
                    "  tanpa ELSE yang tidak cocok apa pun MELEDAK: ERROR 1339, 'Case not",
                    "  found for CASE statement'. Tulis ELSE-nya, selalu.",
                ],
                "code": """DELIMITER //

CREATE PROCEDURE demo_perulangan(IN n INT)
BEGIN
    DECLARE i     INT DEFAULT 1;
    DECLARE sisa  INT DEFAULT 0;
    DECLARE hasil VARCHAR(255) DEFAULT '';

    -- 1. WHILE: kalau n = 0, badan ini tidak pernah jalan sekali pun.
    WHILE i <= n DO
        SET hasil = CONCAT(hasil, i, ' ');
        SET i = i + 1;
    END WHILE;

    -- 2. REPEAT: badan jalan dulu, syarat diperiksa belakangan.
    SET i = 1;
    REPEAT
        SET i = i + 1;
    UNTIL i > n
    END REPEAT;

    -- 3. LOOP: tanpa syarat. Berlabel supaya bisa di-LEAVE dan di-ITERATE.
    SET i = 0;
    putaran: LOOP
        SET i = i + 1;
        IF i > n THEN
            LEAVE putaran;          -- keluar dari loop (seperti break)
        END IF;
        SET sisa = i MOD 2;
        IF sisa = 0 THEN
            ITERATE putaran;        -- lanjut putaran berikutnya (continue)
        END IF;
        SET hasil = CONCAT(hasil, 'ganjil:', i, ' ');
    END LOOP putaran;

    -- 4. CASE sebagai STATEMENT: tiap cabang berisi perintah, bukan nilai.
    CASE
        WHEN n = 0 THEN SET hasil = 'kosong';
        WHEN n < 5 THEN SET hasil = CONCAT(hasil, '| sedikit');
        ELSE            SET hasil = CONCAT(hasil, '| banyak');
    END CASE;

    SELECT hasil;
END //

DELIMITER ;

CALL demo_perulangan(5);""",
            },
            {
                "heading": "FUNCTION, cursor, dan kenapa cursor sebaiknya dihindari",
                "body": [
                    "FUNCTION vs PROCEDURE - beda yang paling penting:",
                    "",
                    "  PROCEDURE  dipanggil dengan CALL, boleh punya OUT/INOUT, boleh",
                    "             mengubah banyak tabel, TIDAK bisa dipakai di dalam",
                    "             SELECT.",
                    "  FUNCTION   mengembalikan SATU nilai lewat RETURN, parameternya IN",
                    "             semua (kata IN tidak boleh ditulis), dan BISA dipanggil",
                    "             di tengah SELECT seperti UPPER() atau ROUND(). Itulah",
                    "             alasan utama membuat function alih-alih procedure.",
                    "",
                    "  Jebakan MySQL: function menolak dibuat tanpa 'karakteristik' -",
                    "  DETERMINISTIC, NO SQL, atau READS SQL DATA - selama binary logging",
                    "  menyala. Pesannya ERROR 1418 dan panjang sekali, padahal yang",
                    "  kurang cuma satu kata itu.",
                    "",
                    "CURSOR = alat untuk membaca hasil query BARIS DEMI BARIS, bukan",
                    "sekaligus sebagai himpunan. Urutannya: DECLARE, OPEN, FETCH berkali-",
                    "kali, lalu CLOSE.",
                    "",
                    "  Urutan DECLARE di dalam blok tidak boleh tertukar, dan inilah",
                    "  kesalahan nomor satu waktu pertama kali menulis cursor:",
                    "    1) variabel dan kondisi   2) cursor   3) handler",
                    "",
                    "  FETCH yang kehabisan baris memunculkan kondisi NOT FOUND. Tanpa",
                    "  handler, procedure berhenti dengan error 1329. Karena itu selalu",
                    "  ada pasangan 'DECLARE CONTINUE HANDLER FOR NOT FOUND SET habis = 1'",
                    "  dan pemeriksaan habis = 1 tepat SETELAH FETCH.",
                    "",
                    "  Jebakan halusnya: handler itu menangkap NOT FOUND dari statement",
                    "  APA PUN di dalam blok, bukan cuma dari FETCH. Satu SELECT ... INTO",
                    "  di tengah loop yang kebetulan tidak dapat baris ikut menyalakan",
                    "  habis = 1, dan loop berhenti diam-diam di tengah jalan tanpa satu",
                    "  pesan galat pun. Datanya separuh terproses dan tidak ada yang tahu.",
                    "",
                    "  Cursor hampir selalu KALAH CEPAT dari satu query himpunan. Seluruh",
                    "  procedure di bawah bisa diganti satu baris:",
                    "    UPDATE nilai SET huruf = nilai_huruf(skor);",
                    "  Untuk 100.000 baris, versi cursor menjalankan 100.000 UPDATE",
                    "  terpisah, masing-masing dengan biaya penguncian dan pencatatan log",
                    "  sendiri. Pakai cursor hanya kalau tiap baris benar-benar butuh",
                    "  keputusan yang tidak bisa dinyatakan sebagai satu query.",
                ],
                "code": """DELIMITER //

-- FUNCTION: satu nilai balik, dan boleh dipakai di dalam SELECT.
CREATE FUNCTION nilai_huruf(skor INT)
RETURNS CHAR(1)
DETERMINISTIC                       -- tanpa ini MySQL menolak (ERROR 1418)
BEGIN
    DECLARE h CHAR(1);
    IF skor IS NULL THEN
        SET h = '-';
    ELSEIF skor >= 85 THEN
        SET h = 'A';
    ELSEIF skor >= 70 THEN
        SET h = 'B';
    ELSE
        SET h = 'C';
    END IF;
    RETURN h;
END //

-- PROCEDURE dengan cursor: membaca hasil query satu baris demi satu baris.
-- Kolom penampungnya disiapkan dulu di luar sini:
--   ALTER TABLE nilai ADD huruf CHAR(1);
CREATE PROCEDURE beri_predikat()
BEGIN
    DECLARE habis  INT DEFAULT 0;                -- 1. variabel lebih dulu
    DECLARE v_nim  INT;
    DECLARE v_kode VARCHAR(10);
    DECLARE v_skor INT;
    DECLARE cur CURSOR FOR                       -- 2. baru cursor
        SELECT nim, kode, skor FROM nilai;
    DECLARE CONTINUE HANDLER FOR NOT FOUND       -- 3. handler paling belakang
        SET habis = 1;

    OPEN cur;
    baca: LOOP
        FETCH cur INTO v_nim, v_kode, v_skor;
        IF habis = 1 THEN
            LEAVE baca;
        END IF;
        UPDATE nilai SET huruf = nilai_huruf(v_skor)
         WHERE nim = v_nim AND kode = v_kode;    -- PK nilai = (nim, kode)
    END LOOP baca;
    CLOSE cur;
END //

DELIMITER ;

-- Function dipakai langsung di dalam SELECT; procedure tidak bisa begitu.
SELECT nim, kode, skor, nilai_huruf(skor) AS huruf FROM nilai;
CALL beri_predikat();""",
            },
            {
                "heading": "Menolak data tidak sah, dan kapan semua ini TIDAK dipakai",
                "body": [
                    "Sampai di sini semua kode hanya MENGHITUNG. Padahal tugas paling",
                    "berharga sebuah trigger justru MENOLAK: menggagalkan INSERT atau",
                    "UPDATE yang datanya tidak masuk akal, apa pun aplikasi yang",
                    "mengirimnya. Untuk itu procedure harus bisa melempar error sendiri.",
                    "",
                    "MySQL - SIGNAL:",
                    "  DELIMITER //",
                    "  CREATE TRIGGER cek_ipk BEFORE INSERT ON mahasiswa",
                    "  FOR EACH ROW",
                    "  BEGIN",
                    "      IF NEW.ipk < 0 OR NEW.ipk > 4 THEN",
                    "          SIGNAL SQLSTATE '45000'",
                    "              SET MESSAGE_TEXT = 'ipk harus di antara 0 dan 4';",
                    "      END IF;",
                    "  END //",
                    "  DELIMITER ;",
                    "",
                    "  '45000' kode SQLSTATE untuk 'error buatan pemakai yang tidak",
                    "  ditangani siapa pun'. Angkanya bukan pilihan bebas: kelas 45 memang",
                    "  disediakan untuk keperluan ini. INSERT yang kena SIGNAL GAGAL",
                    "  seluruhnya - barisnya tidak pernah masuk ke tabel.",
                    "",
                    "PostgreSQL - RAISE EXCEPTION:",
                    "      IF NEW.ipk < 0 OR NEW.ipk > 4 THEN",
                    "          RAISE EXCEPTION 'ipk % tidak masuk akal', NEW.ipk;",
                    "      END IF;",
                    "",
                    "  % adalah tempat nilai disisipkan, mirip %s di bahasa lain. Ada satu",
                    "  beda bentuk yang sering bikin kaget: di PostgreSQL trigger TIDAK",
                    "  berisi kode. Kamu membuat FUNCTION ... RETURNS trigger lebih dulu,",
                    "  lalu CREATE TRIGGER cuma menunjuk fungsi itu.",
                    "",
                    "",
                    "NEW DAN OLD: DUA POTRET BARIS YANG SAMA",
                    "",
                    "Di dalam trigger kamu tidak perlu SELECT untuk melihat datanya. Dua",
                    "nama sudah disediakan, dan keduanya menunjuk BARIS yang sedang",
                    "diproses:",
                    "",
                    "  NEW.kolom   nilainya SESUDAH perubahan",
                    "  OLD.kolom   nilainya SEBELUM perubahan",
                    "",
                    "Mana yang tersedia ditentukan perintah yang memicunya:",
                    "",
                    "  INSERT  ->  cuma NEW   (belum ada nilai lama)",
                    "  UPDATE  ->  NEW dan OLD, keduanya",
                    "  DELETE  ->  cuma OLD   (tidak ada nilai baru)",
                    "",
                    "Memakai OLD di trigger INSERT, atau NEW di trigger DELETE, ditolak",
                    "saat trigger-nya DIBUAT - bukan nanti saat dijalankan.",
                    "",
                    "Karena UPDATE memegang keduanya, ia bisa ditanyai 'apa yang berubah':",
                    "",
                    "  CREATE TRIGGER log_ipk AFTER UPDATE ON mahasiswa",
                    "  FOR EACH ROW",
                    "  WHEN OLD.ipk <> NEW.ipk",
                    "  BEGIN",
                    "      INSERT INTO log_perubahan_ipk(nim, ipk_lama, ipk_baru)",
                    "      VALUES (NEW.nim, OLD.ipk, NEW.ipk);",
                    "  END;",
                    "",
                    "Perhatikan baris WHEN-nya. Tanpa penyaring itu setiap UPDATE ikut",
                    "tercatat - termasuk yang cuma mengubah alamat dan tidak menyentuh ipk",
                    "sama sekali, bahkan UPDATE yang menulis nilai yang sama persis. Log",
                    "audit yang mencatat 'perubahan' yang tidak mengubah apa pun berhenti",
                    "bisa dipercaya.",
                    "",
                    "JEBAKAN: <> DIAM SAAT SALAH SATUNYA NULL",
                    "",
                    "Trigger di atas punya satu lubang yang tidak menimbulkan error apa pun.",
                    "Kalau ipk mahasiswa itu tadinya NULL lalu diisi 3.5, perbandingan",
                    "OLD.ipk <> NEW.ipk tidak menghasilkan TRUE melainkan NULL - dan WHEN",
                    "memperlakukan NULL persis seperti FALSE. Perubahannya TIDAK tercatat,",
                    "padahal justru itu perubahan yang paling pantas dicatat.",
                    "",
                    "Pembandingnya diganti dengan yang memang dibuat untuk itu:",
                    "",
                    "  SQLite      WHEN OLD.ipk IS NOT NEW.ipk",
                    "  PostgreSQL  WHEN OLD.ipk IS DISTINCT FROM NEW.ipk",
                    "  MySQL       IF NOT (OLD.ipk <=> NEW.ipk) THEN ...",
                    "",
                    "Ketiganya berarti sama: 'berbeda, dan NULL dihitung sebagai sebuah",
                    "nilai'. Aturan ini bukan khusus trigger - ia berlaku untuk SEMUA",
                    "perbandingan di SQL, termasuk di WHERE. Begitu sebuah kolom boleh",
                    "NULL, <> dan = berhenti bisa dipakai sendirian.",
                    "Kapan sebaiknya TIDAK dipakai - sekarang kamu punya pembandingnya:",
                    "  - Tidak bisa dites dengan wajar. Tidak ada unit test untuk",
                    "    procedure; mengujinya menuntut database hidup yang sudah berisi",
                    "    data yang pas.",
                    "  - Tidak ada debugger dan tidak ada print. Cara paling umum melacak",
                    "    bug di dalam procedure adalah menyisipkan INSERT ke tabel log,",
                    "    lalu menghapusnya lagi setelah selesai.",
                    "  - Tidak masuk Git dengan sendirinya. Kode ini hidup DI DALAM",
                    "    database. Kalau tidak ditulis ulang jadi berkas migrasi, tidak",
                    "    ada riwayat siapa mengubah apa dan kapan.",
                    "  - Tidak portabel. Semua kode MySQL di materi ini gagal di",
                    "    PostgreSQL, gagal di SQL Server, gagal di SQLite.",
                    "  - Tidak terlihat dari kode aplikasi. Orang membaca kode Java, tidak",
                    "    menemukan apa pun yang menulis ke tabel log, lalu menghabiskan",
                    "    sehari mencari hantu.",
                    "",
                    "Yang tetap pantas ditaruh di database:",
                    "  - Aturan yang WAJIB berlaku apa pun yang menulis - audit trail dan",
                    "    penolakan data tidak sah - karena aplikasi yang menyentuh satu",
                    "    database sering lebih dari satu.",
                    "  - Operasi massal atas data besar, karena menariknya keluar hanya",
                    "    untuk dihitung lalu dikirim balik justru jauh lebih lambat.",
                    "",
                    "Batas alat di mesinmu: sqlite3 - yang dipakai aplikasi ini - TIDAK",
                    "punya bahasa prosedural sama sekali. Tidak ada CREATE PROCEDURE,",
                    "tidak ada DECLARE, IF, atau WHILE. Yang ada cuma trigger dengan",
                    "syarat WHEN dan RAISE untuk membatalkan. Jadi tidak satu pun contoh",
                    "MySQL di atas bisa kamu jalankan di sini - tapi yang di bawah bisa.",
                    "",
                    "Baris INSERT kedua memang sengaja salah. Pesan galat yang muncul",
                    "itulah buktinya trigger bekerja, dan baris Budi tidak ikut tersimpan.",
                ],
                "code": """-- Versi paling sederhana yang benar-benar bisa dijalankan: SQLite.
-- DROP dulu supaya berkas ini aman dijalankan berulang kali. Tabelnya
-- diberi nama sendiri agar tabel mahasiswa dari materi lain tidak ikut hilang.
DROP TABLE IF EXISTS pendaftar;

CREATE TABLE pendaftar (
    nim  INTEGER PRIMARY KEY,
    nama TEXT    NOT NULL,
    ipk  REAL    NOT NULL
);

CREATE TRIGGER tolak_ipk_tak_masuk_akal
BEFORE INSERT ON pendaftar
FOR EACH ROW
WHEN NEW.ipk < 0.0 OR NEW.ipk > 4.0
BEGIN
    SELECT RAISE(ABORT, 'ipk harus di antara 0 dan 4');
END;

INSERT INTO pendaftar VALUES (101, 'Andi', 3.50);
INSERT INTO pendaftar VALUES (102, 'Budi', 7.00);   -- sengaja salah, ditolak

SELECT nim, nama, ipk FROM pendaftar;""",
            },
        ],
    },
    {
        "title": "21. Transaction & Isolation Level Lanjutan",
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
                "heading": "autocommit, dan tiga ejaan untuk kata 'mulai'",
                "body": [
                    "Kenapa satu UPDATE yang diketik tanpa BEGIN langsung permanen?",
                    "Karena database menyalakan AUTOCOMMIT: setiap perintah yang tidak",
                    "berada di dalam transaction dibungkus jadi transaction",
                    "satu-perintah, lalu di-commit sendiri begitu selesai. Jadi bukan",
                    "'tidak ada transaction', melainkan transaction yang dibuka dan",
                    "ditutup untukmu.",
                    "",
                    "Akibat yang paling mahal: DELETE FROM pesanan; yang lupa WHERE",
                    "tidak bisa di-ROLLBACK. Ia sudah ter-commit sebelum kamu sempat",
                    "membaca ulang perintahmu sendiri.",
                    "",
                    "Mematikannya di MySQL:",
                    "  SET autocommit = 0;   -- sejak sekarang WAJIB COMMIT sendiri",
                    "  SET autocommit = 1;   -- kembali seperti semula",
                    "PostgreSQL selalu autocommit di sisi server; yang mematikannya",
                    "adalah kliennya (di psql: \\set AUTOCOMMIT off) atau driver di kode",
                    "aplikasimu (JDBC: conn.setAutoCommit(false)).",
                    "",
                    "Membuka transaction punya tiga ejaan yang maksudnya sama:",
                    "  START TRANSACTION;   MySQL, dan bentuk baku SQL.",
                    "  BEGIN;               PostgreSQL & SQLite; MySQL menerimanya juga.",
                    "  BEGIN TRANSACTION;   SQL Server, dan sah pula di SQLite.",
                    "Perbedaan sepele inilah yang membuat Latihan 12 tidak dinilai",
                    "otomatis: kunci jawabannya memakai START TRANSACTION, sedangkan",
                    "latihanmu dijalankan dengan sqlite3 yang mengenal BEGIN.",
                ]
            },
            {
                "heading": "Mengunci baris: SELECT ... FOR UPDATE",
                "code": """-- Contoh transfer di atas masih berlubang: di antara MEMBACA saldo dan
-- menuliskannya kembali, transaction lain bisa ikut membaca saldo yang sama.
-- Keduanya lalu berhitung dari angka lama, dan satu pengurangan hilang.

START TRANSACTION;

-- FOR UPDATE mengunci baris yang terbaca sampai COMMIT atau ROLLBACK.
-- Transaction lain yang meminta baris ini MENUNGGU, bukan membaca yang basi.
SELECT saldo FROM rekening WHERE id = 'A' FOR UPDATE;

-- (di sini aplikasi memeriksa saldo >= 500000)

UPDATE rekening SET saldo = saldo - 500000 WHERE id = 'A';
UPDATE rekening SET saldo = saldo + 500000 WHERE id = 'B';

COMMIT;

-- FOR SHARE: boleh dibaca bersama-sama, tapi tidak boleh diubah siapa pun
-- selama transaction ini hidup. Dipakai saat kamu cuma perlu memastikan
-- baris rujukan tidak berubah di tengah jalan, misalnya kurs atau harga.
SELECT kurs FROM mata_uang WHERE kode = 'USD' FOR SHARE;

-- Ejaan lain untuk hal yang sama:
--   MySQL 8+ dan PostgreSQL : FOR UPDATE, FOR SHARE
--   MySQL 5.7 ke bawah      : LOCK IN SHARE MODE (pengganti FOR SHARE)
--   SQLite                  : tidak punya keduanya; hanya satu penulis pada
--                             satu waktu, jadi tidak diperlukan.

-- Dua varian yang menghindari antrean panjang:
--   FOR UPDATE NOWAIT       -> langsung error kalau baris sedang dikunci.
--   FOR UPDATE SKIP LOCKED  -> lewati yang terkunci, ambil sisanya. Inilah
--                              cara satu tabel antrean pekerjaan dibagi ke
--                              banyak worker tanpa saling rebut baris.

-- Ingat: UPDATE dan DELETE mengunci barisnya sendiri secara otomatis.
-- FOR UPDATE dipakai ketika kamu perlu mengunci sejak MEMBACA."""
            },
            {
                "heading": "SAVEPOINT: membatalkan sebagiannya saja",
                "body": [
                    "ROLLBACK membatalkan SELURUH transaction. SAVEPOINT memberi titik",
                    "simpan di tengah jalan, supaya yang dibatalkan cukup sebagian. Ini",
                    "anggota TCL ketiga yang disebut di materi pertama.",
                    "",
                    "  START TRANSACTION;",
                    "  INSERT INTO pesanan (id, pelanggan) VALUES (1, 'Andi');",
                    "",
                    "  SAVEPOINT pesanan_dibuat;",
                    "  INSERT INTO item (pesanan_id, produk, jumlah) VALUES (1, 'Mouse', 2);",
                    "  -- ternyata stok Mouse kosong:",
                    "  ROLLBACK TO pesanan_dibuat;   -- item batal, pesanan TETAP ada",
                    "",
                    "  INSERT INTO item (pesanan_id, produk, jumlah) VALUES (1, 'Buku', 1);",
                    "  RELEASE SAVEPOINT pesanan_dibuat;   -- penandanya sudah tak perlu",
                    "  COMMIT;",
                    "",
                    "Tiga hal yang sering disalahpahami:",
                    "  1. ROLLBACK TO nama TIDAK mengakhiri transaction. Ia mundur ke",
                    "     titik itu lalu jalan terus; COMMIT di akhir tetap perlu.",
                    "  2. Titik simpannya boleh banyak dan boleh bersarang. Mundur ke",
                    "     titik lama otomatis membuang semua titik sesudahnya.",
                    "  3. RELEASE membuang PENANDANYA, bukan datanya. Yang sudah ditulis",
                    "     tetap ada dan menunggu COMMIT seperti biasa.",
                    "",
                    "Kamu akan menemukannya di kode nyata meski tidak pernah",
                    "mengetiknya: transaction BERSARANG di ORM diterjemahkan menjadi",
                    "savepoint. @Transactional(propagation = NESTED) di Spring,",
                    "transaction.atomic() bertingkat di Django, dan DB::transaction()",
                    "bersarang di Laravel semuanya menerbitkan SAVEPOINT - karena",
                    "database memang tidak punya transaction di dalam transaction. Itu",
                    "sebabnya rollback di lapisan dalam tidak selalu membatalkan yang",
                    "di luar.",
                    "",
                    "Ejaannya sama persis di MySQL, PostgreSQL, dan SQLite. Oracle",
                    "punya SAVEPOINT dan ROLLBACK TO juga, tapi tidak punya RELEASE",
                    "SAVEPOINT. SQL Server yang paling jauh berbeda: di sana ditulis",
                    "SAVE TRANSACTION nama, mundurnya ROLLBACK TRANSACTION nama, dan",
                    "kata SAVEPOINT tidak dikenal sama sekali.",
                ]
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
        "title": "22. Roadmap Lanjutan: NoSQL, Scaling & Karir Database",
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
