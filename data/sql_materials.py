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
                    "Satu standar, banyak logat:",
                    "  Standarnya memang satu, tapi tiap database menambah dan mengurangi",
                    "  sendiri. Itu sebabnya query yang disalin dari StackOverflow kadang",
                    "  gagal tanpa sebab yang kelihatan - yang menulisnya memakai database",
                    "  lain. Cara mengenali logat sebuah berkas ada di materi Membuka",
                    "  Database & Berkas SQL Orang Lain.",
                    "",
                    "  Untuk kursus ini: contoh ditulis dengan gaya MySQL, sedangkan",
                    "  LATIHAN dijalankan aplikasi ini memakai sqlite3. Karena itu blok",
                    "  KONDISI AWAL di latihan ejaannya kadang berbeda dari materi -",
                    "  bukan salah ketik, memang beda logat.",
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
        "title": "3. Tipe Data, Constraint & Kunci Gabungan",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya membuat tabel pertamamu dengan 8 tipe data dan 7",
                    "constraint. Skema di kode nyata memakai jauh lebih banyak, dan tiap",
                    "pilihan punya akibat yang baru terasa setahun kemudian.",
                    "",
                    "Tipe data bukan label. Ia JANJI ke database soal:",
                    "  - berapa byte yang disediakan untuk kolom itu di tiap baris,",
                    "  - nilai apa yang boleh masuk (yang lain ditolak di pintu),",
                    "  - bagaimana nilainya dibandingkan dan diurutkan.",
                    "",
                    "BILANGAN BULAT - yang beda ukurannya, bukan 'rasanya':",
                    "  TINYINT    1 byte   -128 .. 127        (0 .. 255 kalau UNSIGNED)",
                    "  SMALLINT   2 byte   -32.768 .. 32.767",
                    "  MEDIUMINT  3 byte   -8,3 juta .. 8,3 juta      (MySQL saja)",
                    "  INT        4 byte   -2.147.483.648 .. 2.147.483.647",
                    "  BIGINT     8 byte   +/- 9.223.372.036.854.775.807",
                    "",
                    "Kapan BIGINT WAJIB: kolom id tabel yang barisnya bisa lewat 2,1 miliar",
                    "yaitu log, event, notifikasi, transaksi. Dua hal membuat batas itu",
                    "cepat sampai:",
                    "  1. Nomor yang sudah terpakai TIDAK didaur ulang. Baris yang dihapus",
                    "     tetap memakan nomornya. Jadi batasnya bukan 'jumlah baris",
                    "     sekarang', tapi 'jumlah baris yang pernah ada'.",
                    "  2. Saat id INT habis, INSERT berikutnya GAGAL - bukan melambat, mati.",
                    "     Mengubah INT jadi BIGINT di tabel 500 juta baris berarti tabelnya",
                    "     ditulis ulang, berjam-jam, sambil terkunci.",
                    "  Aturan praktis: id pakai BIGINT, umur/jumlah stok pakai INT ke bawah.",
                    "  UNSIGNED (MySQL) memindahkan jatah negatif ke sisi positif:",
                    "  INT UNSIGNED = 0 .. 4.294.967.295. PostgreSQL tidak punya UNSIGNED.",
                    "",
                    "TEKS - tiga bentuk yang sering dikira sama:",
                    "  CHAR(n)     panjang TETAP n; isi yang lebih pendek dipadatkan spasi.",
                    "  VARCHAR(n)  panjangnya ikut isinya, maksimal n karakter.",
                    "  TEXT        teks panjang; di MySQL disimpan terpisah dari barisnya.",
                    "",
                    "  Pakai CHAR hanya kalau panjangnya benar-benar tetap: kode negara",
                    "  'ID', hash dengan panjang pasti. Perlakuan spasi di ekor CHAR BEDA",
                    "  antar database, dan itu saja alasan cukup untuk memilih VARCHAR.",
                    "  n pada VARCHAR(n) itu pagar, bukan saran: data yang lebih panjang",
                    "  ditolak ('Data too long for column'). Di MySQL mode longgar yang",
                    "  lama, data itu justru DIPOTONG diam-diam - alamat pelanggan hilang",
                    "  separuh tanpa satu pun pesan error.",
                    "  Di PostgreSQL, VARCHAR dan TEXT sama cepat. Di MySQL kolom TEXT tidak",
                    "  bisa di-index penuh (harus awalannya saja: INDEX (isi(100))), jadi",
                    "  jangan pakai TEXT untuk kolom yang sering dicari.",
                    "",
                    "UANG - jangan pernah FLOAT atau DOUBLE. Pakai DECIMAL(p,s):",
                    "  p = total digit, s = digit di belakang koma.",
                    "  DECIMAL(10,2) menampung sampai 99.999.999,99 dan menyimpannya PERSIS.",
                    "  FLOAT/DOUBLE menyimpan PENDEKATAN biner. Buktinya di bawah ini.",
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
                    "WAKTU - lima tipe, dan bedanya bukan gaya penulisan:",
                    "  DATE       2026-09-06           tanggal saja, tanpa jam.",
                    "  TIME       14:30:00             jam saja; di MySQL boleh melebihi",
                    "                                  24 jam karena juga dipakai untuk",
                    "                                  DURASI, bukan cuma jam dinding.",
                    "  DATETIME   2026-09-06 14:30:00  tanggal + jam, disimpan APA ADANYA.",
                    "  TIMESTAMP  terlihat sama persis, tapi SADAR ZONA WAKTU.",
                    "  YEAR       2026                 tahun 4 digit, MySQL saja.",
                    "",
                    "  YEAR itulah tipe kolom 'angkatan' pada tabel mahasiswa di materi",
                    "  SELECT - dipakai di sana tanpa pernah didaftar. Di PostgreSQL dan",
                    "  SQLite tipe ini tidak ada; pakai SMALLINT.",
                    "",
                    "  DATETIME vs TIMESTAMP di MySQL - beda yang menyakitkan kalau salah:",
                    "    DATETIME  disimpan persis seperti yang kamu tulis. Zona waktu",
                    "              server berubah? Nilainya tetap. Sampai tahun 9999.",
                    "    TIMESTAMP diubah ke UTC saat disimpan, dikembalikan ke zona waktu",
                    "              sesi saat dibaca. Dua orang di zona berbeda melihat jam",
                    "              berbeda dari BARIS YANG SAMA - itu fitur, bukan bug.",
                    "              Jebakannya: rentangnya berhenti di 19 Januari 2038.",
                    "    Padanan PostgreSQL: TIMESTAMPTZ (sadar zona) vs TIMESTAMP (tidak).",
                    "    Aturan praktis: simpan UTC, ubah ke waktu lokal saat menampilkan.",
                    "",
                    "TIPE YANG LAZIM DI SKEMA MODERN:",
                    "  BOOLEAN  Di MySQL cuma nama lain TINYINT(1): TRUE/FALSE disimpan 1/0",
                    "           dan SELECT mengembalikan 1/0. PostgreSQL punya boolean asli",
                    "           (t/f). SQLite tidak punya sama sekali - simpan 0/1.",
                    "  BLOB     Data biner mentah (gambar, PDF). Kebanyakan sistem justru",
                    "           menyimpan PATH atau URL berkasnya saja: BLOB membuat backup",
                    "           membengkak dan tiap SELECT * jadi berat.",
                    "  ENUM     MySQL: status ENUM('draft','terbit','arsip'); nilai di luar",
                    "           daftar ditolak. Harganya: menambah satu pilihan = ALTER",
                    "           TABLE di tabel produksi, jadi banyak tim memilih VARCHAR +",
                    "           CHECK. PostgreSQL memakai CREATE TYPE ... AS ENUM.",
                    "  JSON     Satu kolom berisi dokumen utuh. PostgreSQL punya dua: JSON",
                    "  JSONB    (teks apa adanya) dan JSONB (biner, bisa di-index); hampir",
                    "           selalu pilih JSONB. Dua operator yang wajib bisa dibaca:",
                    "             data -> 'alamat'   hasilnya JSON, masih bisa ditelusuri",
                    "             data ->> 'kota'    hasilnya TEXT, baru bisa dibandingkan",
                    "             data -> 'alamat' ->> 'kota' = 'Bandung'",
                    "           Panah tunggal tetap JSON, panah ganda keluar jadi teks;",
                    "           salah pilih = perbandingan yang tidak pernah cocok.",
                    "           MySQL memakai JSON path: data->'$.kota', data->>'$.kota'.",
                    "           Jebakan: kolom biasa lebih cepat dan bisa dijaga constraint",
                    "           - taruh di JSON hanya yang benar-benar tak berbentuk tetap.",
                    "  UUID     Id acak 128-bit: '550e8400-e29b-41d4-a716-446655440000'.",
                    "           PostgreSQL punya tipe uuid asli; MySQL memakai CHAR(36)",
                    "           atau BINARY(16). Untungnya id bisa dibuat aplikasi tanpa",
                    "           menunggu database dan aman digabung dari banyak server.",
                    "           Ruginya 16 byte lawan 8, dan urutannya acak sehingga",
                    "           index-nya lebih lambat ditulis.",
                    "",
                    "KOLOM ID YANG MENGISI DIRINYA SENDIRI - satu ide, lima ejaan:",
                    "  MySQL       id BIGINT AUTO_INCREMENT PRIMARY KEY",
                    "  SQLite      id INTEGER PRIMARY KEY AUTOINCREMENT",
                    "  PostgreSQL  id BIGSERIAL PRIMARY KEY                    (gaya lama)",
                    "              id BIGINT GENERATED ALWAYS AS IDENTITY      (baku SQL)",
                    "              id UUID PRIMARY KEY DEFAULT gen_random_uuid()",
                    "  SERIAL bukan tipe data; ia singkatan yang diam-diam membuat sequence",
                    "  tersendiri. GENERATED ALWAYS AS IDENTITY menggantikannya supaya hak",
                    "  akses dan kepemilikan sequence itu bukan lagi urusanmu.",
                    "  Jebakan SQLite: harus INTEGER, bukan INT. 'INT PRIMARY KEY' bukan",
                    "  rowid, dan id-nya terisi NULL, bukan 1, 2, 3.",
                    "",
                    "KOLOM WAKTU YANG MENGISI DIRINYA SENDIRI:",
                    "  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP",
                    "  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP",
                    "                                ON UPDATE CURRENT_TIMESTAMP  (MySQL)",
                    "  deleted_at TIMESTAMP NULL",
                    "  Inilah jawaban 'dari mana isinya datang' padahal tak ada satu pun",
                    "  INSERT yang mengisinya: DEFAULT dipakai database saat kolom itu TIDAK",
                    "  DISEBUT di INSERT. Menyebut kolomnya lalu mengisi NULL bukan hal yang",
                    "  sama - di kolom NOT NULL itu malah error.",
                    "  ON UPDATE CURRENT_TIMESTAMP hanya ada di MySQL; di PostgreSQL",
                    "  updated_at diisi trigger (lihat materi View & Trigger) atau kode.",
                    "  deleted_at = soft delete: barisnya tidak dihapus, cuma ditandai, dan",
                    "  SEMUA query wajib menambah WHERE deleted_at IS NULL. Lupa satu query,",
                    "  data yang 'sudah dihapus' muncul lagi. UNIQUE pun tetap menghitung",
                    "  baris itu, jadi email yang 'sudah dihapus' tak bisa didaftar ulang.",
                ],
            },
            {
                "body": [
                    "Constraint adalah aturan yang DIJAGA DATABASE, bukan oleh kode",
                    "aplikasimu. Bedanya besar: aplikasi punya banyak versi dan banyak",
                    "skrip, sedangkan constraint berlaku untuk semua penulis data.",
                    "",
                    "DUA TEMPAT MENULISNYA - ini yang membingungkan saat membaca skema:",
                    "  Tingkat KOLOM, menempel di belakang tipe kolomnya:",
                    "      email VARCHAR(255) NOT NULL UNIQUE",
                    "  Tingkat TABEL, sebagai baris tersendiri setelah semua kolom:",
                    "      PRIMARY KEY (siswa_id, kelas_kode),",
                    "      CONSTRAINT fk_siswa FOREIGN KEY (siswa_id) REFERENCES siswa (id)",
                    "  Alasannya sederhana: constraint yang menyangkut LEBIH DARI SATU kolom",
                    "  tidak punya kolom untuk ditempeli. NOT NULL satu-satunya yang hanya",
                    "  bisa di tingkat kolom; sisanya boleh dua-duanya - dan yang di tingkat",
                    "  tabel bisa DIBERI NAMA.",
                    "",
                    "CONSTRAINT BERNAMA:",
                    "  CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (id)",
                    "  Tanpa kata CONSTRAINT, database mengarang namanya sendiri:",
                    "  'ambil_kelas_ibfk_1' (MySQL), 'ambil_kelas_siswa_id_fkey'",
                    "  (PostgreSQL). Nama itu penting karena dua hal:",
                    "    1. Dialah yang muncul di pesan error saat data ditolak, misalnya",
                    "       'violates foreign key constraint fk_kelas'. Nama karangan",
                    "       database membuat pesan error jadi teka-teki.",
                    "    2. Dialah yang harus disebut untuk mencabut aturannya nanti:",
                    "       ALTER TABLE ambil_kelas DROP CONSTRAINT fk_kelas;  (PostgreSQL)",
                    "       ALTER TABLE ambil_kelas DROP FOREIGN KEY fk_kelas; (MySQL)",
                    "",
                    "PRIMARY KEY GABUNGAN (composite):  PRIMARY KEY (siswa_id, kelas_kode)",
                    "  Yang unik adalah PASANGANNYA, bukan masing-masing kolom. siswa_id 1",
                    "  boleh muncul berkali-kali, kelas_kode 'IF101' juga - yang dilarang",
                    "  cuma pasangan yang sama muncul dua kali. Inilah bentuk baku tabel",
                    "  penghubung N:M, dan persis bentuk yang sudah dipakai tabel 'nilai'",
                    "  di materi JOIN: PRIMARY KEY (nim, kode).",
                    "  Akibatnya tabel penghubung tidak perlu kolom id sendiri - pasangan",
                    "  itu sudah menjadi identitas barisnya. Urutan kolomnya pun berarti:",
                    "  index gabungan bisa dipakai mencari dengan kolom PERTAMA saja, tidak",
                    "  dengan kolom keduanya saja.",
                    "",
                    "UNIQUE GABUNGAN:  CONSTRAINT uq_keranjang UNIQUE (user_id, produk_id)",
                    "  Satu user tidak bisa memasukkan produk yang sama dua kali, user lain",
                    "  tetap boleh. Beda dengan PRIMARY KEY: UNIQUE masih boleh NULL, dan di",
                    "  hampir semua database dua NULL dianggap BERBEDA - jadi banyak baris",
                    "  NULL lolos begitu saja. Kalau tak boleh kosong, tambah NOT NULL.",
                    "",
                    "CHECK BERNAMA:",
                    "  CONSTRAINT harga_positif CHECK (harga >= 0)",
                    "  CONSTRAINT tanggal_urut  CHECK (selesai >= mulai)",
                    "  CHECK yang membandingkan DUA kolom hanya bisa di tingkat tabel.",
                    "  Dua jebakan: (1) CHECK MELOLOSKAN NULL, karena kondisinya jadi 'tidak",
                    "  diketahui', bukan salah; (2) di MySQL sebelum 8.0.16 CHECK diterima",
                    "  tapi DIABAIKAN - skema lama bisa punya CHECK yang tak pernah bekerja.",
                    "",
                    "AKSI REFERENSIAL - bagian FOREIGN KEY yang paling menentukan perilaku:",
                    "  ON DELETE RESTRICT     tolak hapus induk selama anaknya masih ada",
                    "  ON DELETE NO ACTION    sama, tapi bisa ditunda sampai akhir transaksi",
                    "  ON DELETE CASCADE      induk dihapus -> semua anaknya ikut terhapus",
                    "  ON DELETE SET NULL     kolom FK di anak diisi NULL (harus boleh NULL)",
                    "  ON DELETE SET DEFAULT  diisi nilai DEFAULT kolom itu",
                    "  ON UPDATE ...          pilihan sama, dipicu saat kunci induk BERUBAH",
                    "  BAWAANNYA NO ACTION/RESTRICT. Jadi tanpa menulis klausa apa pun,",
                    "  DELETE pada induk DITOLAK - foreign key bukan pengecek yang pasif.",
                    "  Kalau DELETE FROM users WHERE id = 1 gagal, itu bukan bug: ada baris",
                    "  pesanan yang menunjuk user itu dan FK sedang melindunginya.",
                    "  Pilih CASCADE hanya kalau si anak tak punya makna tanpa induknya: isi",
                    "  keranjang, baris tabel penghubung, komentar. JANGAN untuk pesanan -",
                    "  menghapus satu user tak boleh diam-diam menghapus riwayatnya.",
                    "  Khusus SQLite: foreign key baru ditegakkan setelah perintah",
                    "  PRAGMA foreign_keys = ON di TIAP koneksi. Bawaannya mati, jadi skema",
                    "  yang benar pun bisa terlihat 'tidak bekerja'.",
                    "",
                    "PENJAGA IDEMPOTEN - kenapa hampir tiap berkas skema dibuka dengan",
                    "DROP TABLE IF EXISTS, CREATE TABLE IF NOT EXISTS, DROP INDEX IF EXISTS:",
                    "  Berkas skema dijalankan berulang kali - pasang ulang, tes, CI, teman",
                    "  baru yang clone repo. Tanpa IF EXISTS, jalan kedua langsung mati di",
                    "  'table already exists' dan sisa berkasnya tak pernah dieksekusi.",
                    "  Urutan DROP wajib KEBALIKAN urutan CREATE: anak dulu, induk",
                    "  belakangan, karena foreign key menolak induk dihapus lebih dulu.",
                    "  Ingat: IF EXISTS hanya membuat perintahnya tidak error. Ia tidak",
                    "  membuat DROP jadi aman - datanya tetap habis.",
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
                    "Sampai sini kamu selalu membuat tabelmu sendiri, jadi kamu hafal isinya.",
                    "Di pekerjaan nyata hampir tidak pernah begitu. Kamu masuk ke database",
                    "yang sudah berisi 40 tabel buatan orang lain, atau membuka repositori",
                    "di GitHub dan menemukan berkas schema.sql yang entah dijalankan",
                    "bagaimana. Dua pertanyaan itulah yang ditutup materi ini.",
                    "",
                    "Melihat isi database di MySQL:",
                    "  SHOW DATABASES;             -- daftar database di server ini",
                    "  USE toko;                   -- pilih database yang mau dipakai",
                    "  SHOW TABLES;                -- daftar tabel di database terpilih",
                    "  DESCRIBE pesanan;           -- kolom, tipe, boleh NULL?, default",
                    "  DESC pesanan;               -- singkatan DESCRIBE, artinya sama",
                    "  SHOW CREATE TABLE pesanan;  -- perintah CREATE aslinya, apa adanya",
                    "  SHOW INDEX FROM pesanan;    -- index di tabel itu, unik atau tidak",
                    "",
                    "SHOW CREATE TABLE yang paling banyak bercerita: di situ terlihat",
                    "FOREIGN KEY, DEFAULT, engine, dan charset-nya sekaligus.",
                    "",
                    "DESC punya DUA arti dan itu sering bikin bingung: singkatan DESCRIBE",
                    "kalau berdiri sendiri, dan 'urut menurun' kalau dipakai di ORDER BY.",
                    "Posisinya yang menentukan, bukan katanya.",
                    "",
                    "Pertanyaan yang sama di klien lain:",
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
                    "JEBAKAN: perintah berawalan titik (.tables) dan garis miring terbalik",
                    "(\\dt) BUKAN SQL. Itu milik program kliennya sendiri. Menempelkannya",
                    "ke dalam kode program atau ke GUI database langsung error.",
                    "",
                    "JEBAKAN kedua: sqlite3 mencetak hasil polos tanpa nama kolom dan",
                    "dipisah tanda | . Nyalakan dulu supaya terbaca manusia:",
                    "  .headers on",
                    "  .mode column",
                    "Aplikasi ini menjalankan latihan SQL-mu dengan sqlite3, jadi dua",
                    "baris itu langsung berguna, bukan cuma teori.",
                ],
            },
            {
                "heading": "Peta skema yang bisa kamu jalankan",
                "body": [
                    "'Ada tabel apa saja' juga bisa ditanya lewat SELECT biasa, dan cara",
                    "ini berlaku di MySQL, PostgreSQL, maupun SQL Server:",
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
                    "information_schema adalah database bawaan berisi katalog: tabel yang",
                    "mencatat tabel. Karena hasilnya baris biasa, ia bisa disaring dengan",
                    "WHERE, di-JOIN, dan dipakai dari dalam program -- SHOW TABLES tidak",
                    "sefleksibel itu. Di PostgreSQL isi table_schema biasanya 'public',",
                    "bukan nama databasenya. SQLite tidak punya information_schema;",
                    "padanannya tabel sqlite_master.",
                    "",
                    "Berkas di bawah ini membuat dua tabel, lalu membacanya ulang seolah",
                    "kamu baru pertama kali membuka database itu.",
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
                    "Di repositori, SQL jarang berbentuk ketikan di prompt. Ia berupa",
                    "berkas: schema.sql (struktur), seed.sql (data awal), cadangan.sql",
                    "(hasil backup). Cara menjalankannya:",
                    "  MySQL      : mysql -u root -p toko < schema.sql",
                    "  MySQL      : SOURCE schema.sql;   -- kalau sudah di dalam sesi",
                    "  PostgreSQL : psql -d toko -f schema.sql",
                    "  SQLite     : sqlite3 app.db < schema.sql",
                    "",
                    "Tanda < itu milik shell, bukan SQL: ia menyuapkan isi berkas ke",
                    "program seolah kamu mengetiknya sendiri. Karena itu ia diketik di",
                    "terminal, bukan di dalam sesi mysql. Di dalam sesi, padanannya",
                    "SOURCE (boleh juga ditulis \\. schema.sql).",
                    "",
                    "Urutannya penting: schema.sql dulu, seed.sql sesudahnya. Dibalik,",
                    "seed mengisi tabel yang belum ada dan gagal di baris pertama.",
                    "",
                    "Dari mana berkas .sql raksasa itu berasal? Dari perintah dump:",
                    "  mysqldump -u root -p toko > cadangan.sql          -- struktur+data",
                    "  mysqldump -u root -p --no-data toko > schema.sql  -- struktur saja",
                    "  pg_dump -U postgres toko > cadangan.sql",
                    "Mengembalikannya: mysql -u root -p toko < cadangan.sql",
                    "",
                    "JEBAKAN: mysqldump tidak membuat databasenya. CREATE DATABASE toko;",
                    "harus dijalankan lebih dulu, kalau tidak restore berhenti dengan",
                    "'No database selected'.",
                    "",
                    "Isi dump selalu terlihat aneh buat pemula. Potongan khasnya:",
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
                    "Yang perlu dimengerti dari situ:",
                    "  SET NAMES utf8mb4    -> sesi ini bicara UTF-8 penuh (termasuk emoji).",
                    "  FOREIGN_KEY_CHECKS=0 -> cek FK dimatikan sementara. Dump menulis",
                    "     tabel berurutan abjad, jadi tabel anak bisa lahir sebelum",
                    "     induknya; tanpa dimatikan, restore gagal di tengah jalan.",
                    "     Di akhir berkas nilainya dikembalikan ke 1.",
                    "  ENGINE=InnoDB        -> mesin penyimpan MySQL. InnoDB-lah yang",
                    "     membuat FOREIGN KEY dan transaction benar-benar bekerja (lihat",
                    "     materi Transaction). MyISAM yang lama menerima FOREIGN KEY lalu",
                    "     diam-diam mengabaikannya.",
                    "  backtick di tiap nama -> yang menulis berkas ini mesin, jadi ia",
                    "     mengutip SEMUA nama supaya aman walau ada kolom bernama order.",
                ],
            },
            {
                "heading": "Isi folder migrations/",
                "body": [
                    "Struktur database yang sudah dipakai orang tidak diubah dengan",
                    "mengedit schema.sql. Perubahannya ditumpuk sebagai berkas kecil",
                    "berurutan di folder migrations/:",
                    "  001_buat_tabel_customer.up.sql",
                    "  001_buat_tabel_customer.down.sql",
                    "  002_tambah_kolom_email.up.sql",
                    "  002_tambah_kolom_email.down.sql",
                    "",
                    "Penomorannya tergantung alatnya, tapi polanya sama:",
                    "  V1__buat_tabel.sql            -> gaya Flyway (dua garis bawah)",
                    "  001_init.up.sql               -> gaya golang-migrate, ada .down",
                    "  20240115120000_buat_user.sql  -> gaya Rails/Laravel, cap waktu",
                    "",
                    "up = perubahan maju (ADD COLUMN). down = pembatalnya (DROP COLUMN),",
                    "dipakai kalau perubahannya harus ditarik kembali. seed.sql beda",
                    "urusan: ia mengisi DATA awal yang memang harus ada (daftar kategori,",
                    "daftar role), bukan mengubah struktur.",
                    "",
                    "ATURAN yang jarang ditulis tapi berlaku di semua tim: migrasi yang",
                    "SUDAH pernah dijalankan tidak pernah diedit lagi. Alatnya mencatat",
                    "migrasi mana saja yang sudah jalan di sebuah tabel khusus",
                    "(schema_migrations, flyway_schema_history) lengkap dengan sidik",
                    "jarinya. Mengedit berkas lama membuat sidik jari itu tidak cocok dan",
                    "alatnya menolak jalan -- dan database teman satu timmu tetap tidak",
                    "menerima suntinganmu, karena nomor itu tercatat sudah selesai.",
                    "Ada yang salah? Buat migrasi BARU yang membetulkannya.",
                    "",
                    "Isi sebuah berkas migrasi hampir selalu ALTER TABLE. Perintah di",
                    "bawah bisa kamu coba di sesi database untuk melihat bentuknya; di",
                    "repositori, tiap satu perubahan tinggal di berkasnya sendiri.",
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
                    "Sumber kebingungan terbesar saat membaca SQL orang lain: ada empat",
                    "macam tanda kutip dan artinya tidak sama.",
                    "  'Andi'    -> kutip TUNGGAL: nilai teks & tanggal. Sama di semua DB.",
                    "  `pesanan` -> backtick: NAMA tabel/kolom di MySQL & MariaDB.",
                    "  \"pesanan\" -> kutip ganda: NAMA di PostgreSQL, Oracle, SQLite.",
                    "  [pesanan] -> kurung siku: NAMA di SQL Server.",
                    "",
                    "JEBAKAN: WHERE nama = \"Andi\" jalan mulus di MySQL lalu meledak di",
                    "PostgreSQL dengan pesan column \"Andi\" does not exist -- karena di",
                    "sana kutip ganda berarti nama kolom. Biasakan kutip tunggal untuk",
                    "teks, selalu, di database mana pun.",
                    "",
                    "Nama WAJIB dikutip kalau namanya kata cadangan: order, user, group,",
                    "from, table, key, desc. Kolom bernama order ditulis `order` di MySQL",
                    "dan \"order\" di PostgreSQL. Ini alasan banyak tim memilih nama jamak",
                    "seperti orders sejak awal -- supaya tidak perlu dikutip seumur hidup.",
                    "",
                    "JEBAKAN PostgreSQL: nama tanpa kutip otomatis dijadikan huruf kecil.",
                    "Kalau sebuah tabel telanjur dibuat sebagai \"User\" (pakai kutip),",
                    "maka SELECT * FROM User; gagal selamanya -- yang dicari tabel user.",
                    "",
                    "Mengenali dialek sebuah berkas dalam sepuluh detik:",
                    "  `backtick` + ENGINE=InnoDB + AUTO_INCREMENT -> MySQL / MariaDB",
                    "  \"kutip ganda\" + SERIAL + tanda :: + $$      -> PostgreSQL",
                    "  [kurung siku] + GO sendirian sebaris + TOP  -> SQL Server",
                    "  AUTOINCREMENT + PRAGMA                      -> SQLite",
                    "",
                    "Peta padanan untuk hal yang paling sering berbeda:",
                    "  Hal             MySQL              PostgreSQL     SQLite",
                    "  --------------  -----------------  -------------  ---------------",
                    "  id otomatis     AUTO_INCREMENT     SERIAL         AUTOINCREMENT",
                    "  gabung teks     CONCAT(a, b)       a || b         a || b",
                    "  tidak sama      <> atau !=         <> atau !=     <> atau !=",
                    "  batas 10 baris  LIMIT 10           LIMIT 10       LIMIT 10",
                    "  waktu sekarang  NOW()              NOW()          datetime('now')",
                    "  mulai trans.    START TRANSACTION  BEGIN          BEGIN",
                    "",
                    "  <> dan != sama-sama jalan di MySQL, PostgreSQL, SQLite, dan SQL",
                    "  Server, tapi <> yang standar dan tidak pernah salah di mana pun.",
                    "  Biasakan <>.",
                    "  Batas baris justru beda sendiri di dua database besar:",
                    "    SQL Server : SELECT TOP 10 * FROM pesanan;",
                    "    Oracle     : SELECT * FROM pesanan FETCH FIRST 10 ROWS ONLY;",
                ],
            },
        ],
    },
    {
        "title": "5. DML: Insert, Update, Delete",
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
        "title": "6. SELECT & Filtering",
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
                    "  Alias berkutip TUNGGAL seperti di atas cuma diterima MySQL dan",
                    "  SQLite. Di PostgreSQL kutip tunggal SELALU berarti teks, jadi",
                    "  'Nama Lengkap' di situ dibaca sebagai nilai lalu ditolak sebagai",
                    "  nama kolom.",
                    "  Bentuk portabelnya memakai kutip ganda:",
                    "    SELECT nama AS \"Nama Lengkap\", ipk AS IPK FROM mahasiswa;",
                    "  Paling aman: pilih alias tanpa spasi (AS nama_lengkap) supaya",
                    "  tidak perlu dikutip di database mana pun.",
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
                    "",
                    "Kenapa contoh WHERE ipk IS NOT NULL di atas tidak ditulis != NULL:",
                    "  NULL bukan sebuah nilai, melainkan 'tidak diketahui'.",
                    "  Membandingkannya dengan = atau != tidak pernah menghasilkan benar -",
                    "  bahkan NULL = NULL pun bukan benar. Satu-satunya cara memeriksanya",
                    "  IS NULL / IS NOT NULL. Aturan lengkapnya di materi berikutnya,",
                    "  Ekspresi, NULL & CASE.",
                ]
            },
        ],
    },
    {
        "title": "7. Ekspresi, NULL & CASE",
        "sections": [
            {
                "body": [
                    "SELECT tidak cuma MENGAMBIL kolom yang sudah ada. Ia juga bisa MENGHITUNG",
                    "kolom baru dari kolom lain. Apa pun yang ditulis di antara SELECT dan FROM",
                    "disebut ekspresi, dan hasilnya cuma hidup selama query itu jalan - tidak",
                    "disimpan ke tabel, tidak mengubah apa-apa.",
                    "",
                    "Operator aritmatika:",
                    "  +   tambah      harga + ongkir",
                    "  -   kurang      stok - terjual",
                    "  *   kali        harga * stok",
                    "  /   bagi        total / jumlah",
                    "  %   sisa bagi   id % 2      -> 0 kalau genap, 1 kalau ganjil",
                    "",
                    "  SELECT nama, harga * stok AS nilai_stok FROM produk;",
                    "",
                    "Tanpa AS, nama kolom hasilnya jadi tulisan 'harga * stok' apa adanya - sah,",
                    "tapi menyusahkan dibaca orang maupun aplikasi. Alias sudah dibahas di materi",
                    "SELECT & Filtering; mulai di sini ia berhenti jadi hiasan dan jadi keharusan.",
                    "",
                    "Ekspresi juga boleh berdiri di WHERE dan ORDER BY, bukan cuma di SELECT:",
                    "  SELECT * FROM produk WHERE harga * stok > 1000000;",
                    "  SELECT * FROM produk ORDER BY harga * stok DESC;",
                    "",
                    "KOLOM YANG DIHITUNG DARI DIRINYA SENDIRI (di UPDATE):",
                    "  UPDATE produk SET harga = harga * 1.10 WHERE kategori = 'Minuman';",
                    "",
                    "  Tanda = di SET bukan perbandingan, tapi penugasan. Sisi KANAN dibaca lebih",
                    "  dulu dan berisi nilai LAMA baris itu; hasilnya baru ditulis balik ke kolom.",
                    "  Tiap baris dihitung sendiri-sendiri, jadi satu perintah menaikkan harga",
                    "  seluruh minuman sekaligus tanpa kamu perlu tahu harga masing-masing.",
                    "",
                    "  Bentuk yang persis sama dipakai transfer saldo di materi Transaction:",
                    "    UPDATE rekening SET saldo = saldo - 500000 WHERE id = 'A';",
                    "",
                    "JEBAKAN: PEMBAGIAN BILANGAN BULAT.",
                    "  Kalau kedua sisi tanda / berupa bilangan bulat, banyak database memotong",
                    "  hasilnya jadi bulat juga: 5 / 2 menghasilkan 2, bukan 2.5.",
                    "    PostgreSQL, SQL Server, SQLite -> 2",
                    "    MySQL, Oracle                  -> 2.5",
                    "  Jangan menebak dari ingatan; kelakuannya beda tergantung database.",
                    "",
                    "  Yang bikin berbahaya: tidak ada error, tidak ada peringatan. Yang keluar",
                    "  cuma angka yang salah. Korban paling sering adalah persentase -",
                    "    stok / total * 100",
                    "  memberi 0 untuk SEMUA baris, karena stok / total sudah dibulatkan jadi 0",
                    "  lebih dulu, baru dikali 100.",
                    "",
                    "  Tiga cara keluar (pilih satu):",
                    "    stok * 100.0 / total         -- sentuh dulu dengan angka desimal",
                    "    stok * 1.0 / total           -- trik lama, sama saja maksudnya",
                    "    CAST(stok AS REAL) / total   -- ubah tipenya terang-terangan",
                    "",
                    "KONVERSI TIPE EKSPLISIT:",
                    "  CAST(nilai AS DECIMAL(10,2))   -- standar, dimengerti semua database",
                    "  CONVERT(nilai, DECIMAL(10,2))  -- MySQL (di SQL Server urutannya terbalik)",
                    "  harga::numeric                 -- bentuk pendek khas PostgreSQL",
                    "  '2024-01-01'::date             -- sama, untuk tanggal",
                    "",
                    "  Titik dua ganda (::) itu operator CAST milik PostgreSQL, BUKAN operator",
                    "  lingkup seperti std::cout di C++. Kalau menemuinya di query orang lain,",
                    "  bacanya cukup 'ubah jadi'.",
                    "",
                    "FUNGSI NUMERIK yang sering muncul:",
                    "  ROUND(nilai, digit) -> bulatkan     ROUND(3.14159, 2) = 3.14",
                    "  ABS(nilai)          -> nilai mutlak, tanda minus dibuang",
                    "  CEIL / CEILING      -> bulatkan ke ATAS    CEIL(2.1) = 3",
                    "  FLOOR               -> bulatkan ke BAWAH   FLOOR(2.9) = 2",
                    "  MOD(a, b)           -> sisa bagi, sama artinya dengan a % b",
                    "  POWER(a, b)         -> pangkat            POWER(2, 10) = 1024",
                    "  GREATEST(a, b, ...) -> terbesar di antara beberapa KOLOM, dalam satu baris",
                    "  LEAST(a, b, ...)    -> terkecil di antara beberapa kolom, dalam satu baris",
                    "",
                    "  ROUND paling sering dipasangkan ke AVG. Tanpa ROUND, rata-rata keluar",
                    "  dengan belasan angka di belakang koma dan laporan jadi tak enak dibaca:",
                    "    SELECT jurusan, ROUND(AVG(ipk), 2) FROM mahasiswa GROUP BY jurusan;",
                    "",
                    "  Catatan dialek: SQLite tidak punya GREATEST/LEAST - di sana MAX(a, b) dan",
                    "  MIN(a, b) yang bekerja per baris (bernama sama dengan fungsi agregat, tapi",
                    "  beda pekerjaan). SQL Server baru punya GREATEST/LEAST sejak versi 2022.",
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
                    "NULL bukan angka 0. Bukan juga teks kosong ''. NULL artinya TIDAK DIKETAHUI.",
                    "",
                    "  ipk = 0     -> orang ini punya IPK, dan nilainya memang nol.",
                    "  nama = ''   -> datanya ada, isinya kebetulan kosong.",
                    "  ipk = NULL  -> tidak ada yang tahu berapa. Belum diisi, belum diukur.",
                    "",
                    "Bedanya terasa sepele sampai kamu menghitung rata-rata: nilai 0 ikut menarik",
                    "rata-rata ke bawah, sedangkan NULL tidak ikut dihitung sama sekali.",
                    "",
                    "LOGIKA TIGA NILAI",
                    "  Di kebanyakan bahasa, perbandingan bernilai benar atau salah. Di SQL ada",
                    "  nilai KETIGA: unknown. Membandingkan sesuatu dengan yang tidak diketahui",
                    "  hasilnya juga tidak diketahui.",
                    "",
                    "    ipk = NULL    -> unknown   (BUKAN benar, dan bukan salah)",
                    "    ipk <> NULL   -> unknown",
                    "    NULL = NULL   -> unknown   (dua hal tak diketahui belum tentu sama)",
                    "",
                    "  WHERE hanya meloloskan baris yang kondisinya BENAR. Unknown ikut terbuang",
                    "  bersama yang salah. Karena itu:",
                    "",
                    "    SELECT * FROM mahasiswa WHERE ipk = NULL;     -- selalu 0 baris",
                    "    SELECT * FROM mahasiswa WHERE ipk IS NULL;    -- ini yang benar",
                    "    SELECT * FROM mahasiswa WHERE ipk IS NOT NULL;",
                    "",
                    "  Perhatikan: query pertama TIDAK error. Ia jalan mulus dan mengembalikan",
                    "  kosong - itulah sebabnya kesalahan ini sanggup bertahan lama di kode nyata.",
                    "  Ini juga jawaban kenapa 'SELECT nama FROM n WHERE n.nim = NULL' salah:",
                    "  bukan karena sintaksnya keliru, tapi karena kondisinya tak pernah benar.",
                    "",
                    "NULL MENULAR ke seluruh ekspresi yang menyentuhnya:",
                    "  NULL + 1               -> NULL",
                    "  harga * NULL           -> NULL",
                    "  'Hai ' || NULL         -> NULL   (penggabungan teks ikut hangus)",
                    "  CONCAT('Hai ', NULL)   -> NULL di MySQL; PostgreSQL malah mengabaikannya",
                    "",
                    "  Satu kolom kosong sudah cukup membuat seluruh kolom hasil jadi kosong.",
                    "  Inilah sebab paling umum kolom 'alamat lengkap' mendadak blank di laporan,",
                    "  padahal jalan, kota, dan provinsinya jelas terisi - yang kosong cuma RT-nya.",
                    "  Tambalannya: CONCAT_WS di MySQL, atau COALESCE di tiap potongannya.",
                    "",
                    "AGREGAT JUSTRU MENGABAIKAN NULL - kebalikannya.",
                    "  AVG(ipk) menjumlahkan yang terisi lalu membagi dengan JUMLAH YANG TERISI,",
                    "  bukan dengan jumlah baris. Dari 4 baris yang satu ipk-nya NULL:",
                    "    AVG(ipk)             -> dibagi 3",
                    "    SUM(ipk) / COUNT(*)  -> dibagi 4, hasilnya BEDA dan hampir selalu salah",
                    "  COUNT(*) menghitung baris; COUNT(ipk) hanya menghitung yang tidak NULL.",
                    "  (Fungsi agregat dibahas tuntas di materi Agregasi & Grouping.)",
                    "",
                    "JEBAKAN PALING SENYAP: NOT IN yang daftarnya memuat NULL.",
                    "    SELECT nama FROM mahasiswa",
                    "    WHERE nim NOT IN (SELECT wali_id FROM mahasiswa);",
                    "",
                    "  Kalau ada SATU saja wali_id bernilai NULL, query ini mengembalikan NOL",
                    "  BARIS - selamanya, apa pun isi tabelnya. Sebabnya: NOT IN (a, b, NULL)",
                    "  dijabarkan jadi  nim <> a AND nim <> b AND nim <> NULL, dan bagian",
                    "  terakhir itu unknown, sehingga rangkaian AND-nya tak pernah bisa benar.",
                    "  IN biasa tidak kena masalah ini; hanya NOT IN.",
                    "  Perbaikannya: saring dulu (WHERE wali_id IS NOT NULL), atau pakai",
                    "  NOT EXISTS yang memang kebal NULL.",
                    "",
                    "MENAMBAL NULL",
                    "  COALESCE(a, b, c) -> ambil nilai pertama yang bukan NULL. Standar, ada",
                    "                       di semua database. Pakai ini kalau ragu.",
                    "  IFNULL(a, b)      -> versi dua argumen di MySQL & SQLite.",
                    "  ISNULL(a, b)      -> nama yang sama persis di SQL Server. Hati-hati:",
                    "                       ISNULL(x) di MySQL artinya lain (mengembalikan 1/0).",
                    "  NVL(a, b)         -> milik Oracle.",
                    "  NULLIF(a, b)      -> kebalikannya: hasilnya NULL kalau a sama dengan b.",
                    "",
                    "  NULLIF paling berguna menghindari pembagian dengan nol:",
                    "    SELECT total / NULLIF(jumlah, 0) FROM laporan;",
                    "  Hasilnya NULL (sel kosong) alih-alih query gagal di tengah jalan.",
                    "",
                    "  Pola yang muncul di hampir tiap laporan:",
                    "    COALESCE(SUM(nilai), 0)",
                    "  LEFT JOIN membiarkan sisi kanan kosong untuk baris tanpa pasangan, dan",
                    "  SUM dari NOL baris bukan 0 melainkan NULL. COALESCE menutup lubang itu",
                    "  supaya laporan menampilkan angka 0, bukan sel kosong yang bikin panik.",
                    "  (LEFT JOIN dibahas di materi JOIN.)",
                ],
            },
            {
                "body": [
                    "CASE adalah satu-satunya cara menulis logika if-else DI DALAM sebuah query.",
                    "Ia menerjemahkan kode angka jadi keterangan, mengelompokkan nilai jadi",
                    "kategori, dan memberi perlakuan berbeda per baris - tanpa query kedua.",
                    "",
                    "BENTUK PENCARIAN (searched CASE) - yang paling sering dipakai:",
                    "  CASE",
                    "      WHEN ipk >= 3.5 THEN 'Cumlaude'",
                    "      WHEN ipk >= 3.0 THEN 'Baik'",
                    "      ELSE 'Biasa'",
                    "  END",
                    "",
                    "  Tiap WHEN berisi kondisi utuh, sebebas isi WHERE. Diperiksa dari ATAS ke",
                    "  BAWAH, dan yang PERTAMA cocok langsung menang - sisanya tak dilihat lagi.",
                    "  Urutan karena itu menentukan hasil: seandainya WHEN ipk >= 3.0 ditulis",
                    "  lebih dulu, mahasiswa ber-IPK 3.8 ikut dilabeli 'Baik' dan label",
                    "  'Cumlaude' tidak akan pernah muncul untuk siapa pun.",
                    "",
                    "BENTUK SEDERHANA (simple CASE) - satu kolom diadu ke beberapa nilai:",
                    "  CASE status",
                    "      WHEN 1 THEN 'Aktif'",
                    "      WHEN 2 THEN 'Cuti'",
                    "      ELSE 'Tidak diketahui'",
                    "  END",
                    "",
                    "  Bentuk ini hanya sanggup membandingkan KESAMAAN. Begitu butuh >, <, LIKE,",
                    "  atau BETWEEN, pindah ke bentuk pencarian.",
                    "  Dan karena diam-diam ia memakai '=', baris yang kolomnya NULL TIDAK PERNAH",
                    "  cocok dengan WHEN mana pun - ia selalu jatuh ke ELSE (alasannya persis",
                    "  seperti logika tiga nilai di bagian sebelumnya). Kalau NULL perlu",
                    "  keterangan sendiri, tulis WHEN kolom IS NULL memakai bentuk pencarian.",
                    "",
                    "CASE ITU EKSPRESI, BUKAN STATEMENT.",
                    "  Artinya ia menghasilkan SATU NILAI, jadi boleh berdiri di mana pun sebuah",
                    "  nilai boleh berdiri:",
                    "    SELECT   CASE ... END AS predikat",
                    "    WHERE    CASE ... END = 'Cumlaude'",
                    "    ORDER BY CASE WHEN ipk IS NULL THEN 1 ELSE 0 END, ipk DESC",
                    "    GROUP BY CASE ... END",
                    "    SUM(CASE WHEN ipk >= 3.5 THEN 1 ELSE 0 END)",
                    "    UPDATE produk SET kategori = CASE ... END",
                    "",
                    "  Yang di dalam SUM itu pola penting: SUM(CASE ...) menghitung 'berapa yang",
                    "  memenuhi syarat' berdampingan dengan COUNT(*) dalam SATU query. Kalau",
                    "  memakai WHERE, kamu terpaksa menjalankan dua query lalu menggabungkannya",
                    "  sendiri di luar database.",
                    "",
                    "  Karena CASE bukan perintah, ia juga TIDAK bisa memilih menjalankan",
                    "  perintah - tidak ada 'CASE WHEN ... THEN DELETE'. Percabangan semacam itu",
                    "  ditulis di stored procedure (IF ... THEN) atau di kode aplikasi.",
                    "",
                    "JEBAKAN: ELSE YANG LUPA DITULIS.",
                    "  Baris yang tidak cocok WHEN mana pun tidak error dan tidak dilewati -",
                    "  hasilnya NULL. Kolom laporan mendadak kosong tanpa satu pun tanda bahaya,",
                    "  dan kalau NULL itu ikut masuk hitungan berikutnya, ia menular seperti yang",
                    "  sudah dijelaskan di atas. Biasakan selalu menulis ELSE, walau isinya cuma",
                    "  'Lainnya'.",
                    "",
                    "  Sisanya soal bentuk: END wajib ada, tiap WHEN wajib punya THEN, dan semua",
                    "  THEN sebaiknya menghasilkan tipe yang sama. Lupa END biasanya bikin",
                    "  database mengeluh soal sintaks di baris yang jauh di bawahnya, jadi kalau",
                    "  pesan errornya terasa tak nyambung, cek dulu CASE yang belum ditutup.",
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
            {
                "heading": "Aturan GROUP BY yang wajib dipatuhi",
                "body": [
                    "Aturannya satu: setiap kolom di SELECT yang TIDAK dibungkus fungsi",
                    "agregat wajib ikut disebut di GROUP BY. Kalau tidak, database tidak",
                    "punya cara memilih nilai mana dari sekian baris dalam satu grup.",
                    "",
                    "  X  SELECT jurusan, nama, AVG(ipk) FROM mahasiswa GROUP BY jurusan;",
                    "     -- nama siapa? satu grup berisi tiga nama.",
                    "",
                    "PostgreSQL menolaknya:",
                    "  column \"mahasiswa.nama\" must appear in the GROUP BY clause or be",
                    "  used in an aggregate function",
                    "MySQL 5.7+ menolak dengan bunyi yang mirip:",
                    "  ... is not in GROUP BY clause and contains nonaggregated column ...",
                    "SQLite dan MySQL lama justru DIAM: mereka memilih satu nilai asal",
                    "dari grup itu. Query yang sama karena itu bisa lolos di laptopmu lalu",
                    "ditolak di server - dan yang benar adalah yang menolak.",
                    "",
                    "GROUP BY boleh lebih dari satu kolom. Grupnya dibentuk dari",
                    "KOMBINASI nilai semua kolom yang disebut:",
                    "",
                    "  SELECT p.nama, k.nama, SUM(pn.jumlah) AS total",
                    "  FROM produk p",
                    "  JOIN penjualan pn ON p.id = pn.produk_id",
                    "  JOIN kategori k ON p.kategori_id = k.id",
                    "  GROUP BY p.id, p.nama, k.nama;",
                    "",
                    "  p.id ikut disebut supaya dua produk yang kebetulan bernama sama",
                    "  tidak terlebur jadi satu baris. Inilah bentuk yang dituntut",
                    "  Latihan 8.",
                    "",
                    "Alias yang lahir di SELECT boleh dipakai di ORDER BY, TAPI TIDAK di",
                    "WHERE. Alasannya persis urutan eksekusi di atas: WHERE dijalankan",
                    "SEBELUM SELECT, jadi saat WHERE diperiksa aliasnya belum ada.",
                    "ORDER BY dijalankan SESUDAH SELECT, jadi di sana sudah ada.",
                    "",
                    "  V  SELECT jurusan, AVG(ipk) AS rata FROM mahasiswa",
                    "     GROUP BY jurusan ORDER BY rata DESC;",
                    "  X  SELECT jurusan, AVG(ipk) AS rata FROM mahasiswa",
                    "     WHERE rata > 3 GROUP BY jurusan;",
                    "  Untuk menyaring hasil agregat, tempatnya HAVING - bukan WHERE.",
                ]
            },
            {
                "heading": "LIMIT & OFFSET: mengambil hasil per halaman",
                "body": [
                    "LIMIT sudah muncul di daftar urutan klausa di atas tanpa pernah",
                    "dijelaskan. LIMIT memotong jumlah baris hasil; OFFSET melewati",
                    "sekian baris pertama sebelum pemotongan itu.",
                    "",
                    "  SELECT nama, ipk FROM mahasiswa ORDER BY ipk DESC LIMIT 10;",
                    "  -- sepuluh teratas: halaman 1",
                    "",
                    "  SELECT nama, ipk FROM mahasiswa ORDER BY ipk DESC LIMIT 10 OFFSET 10;",
                    "  -- lewati 10, ambil 10 berikutnya: baris ke-11 sampai ke-20",
                    "",
                    "Rumus halamannya: OFFSET = (nomor_halaman - 1) * isi_per_halaman.",
                    "",
                    "MySQL punya bentuk singkat yang urutan angkanya TERBALIK dari dugaan:",
                    "  LIMIT 40, 20   -- lewati 40, ambil 20",
                    "Angka pertama itu OFFSET, angka kedua jumlah baris; jadi ia sama",
                    "dengan LIMIT 20 OFFSET 40, bukan sebaliknya. Bentuk panjang",
                    "LIMIT 20 OFFSET 40 jalan di MySQL, PostgreSQL, dan SQLite sekaligus,",
                    "jadi biasakan yang panjang saja.",
                    "",
                    "JEBAKAN: OFFSET TANPA ORDER BY memberi hasil yang tidak stabil.",
                    "Database tidak wajib mengembalikan baris dalam urutan yang sama dua",
                    "kali, jadi satu baris bisa muncul di halaman 1 dan halaman 2",
                    "sekaligus sementara baris lain tidak pernah muncul sama sekali.",
                    "Setiap query berhalaman WAJIB punya ORDER BY, dan urutannya harus",
                    "pasti: tambahkan kolom unik seperti id sebagai pemutus kalau kolom",
                    "pengurutnya bisa bernilai seri.",
                ]
            },
            {
                "heading": "Menghitung sub-kelompok & merujuk kolom lewat nomor",
                "body": [
                    "Materi Ekspresi, NULL & CASE sudah memperkenalkan",
                    "SUM(CASE WHEN ... THEN 1 ELSE 0 END). Tempat pemakaiannya memang di",
                    "sini, berdampingan dengan GROUP BY, dan ada dua bentuk lain yang",
                    "perlu dikenali saat membaca query laporan.",
                    "",
                    "COUNT(CASE WHEN ... THEN 1 END) - tanpa ELSE. Itu bukan kelalaian:",
                    "CASE tanpa ELSE menghasilkan NULL, dan COUNT memang mengabaikan",
                    "NULL. Hasilnya sama dengan SUM(CASE ... ELSE 0 END).",
                    "",
                    "  SELECT jurusan,",
                    "         COUNT(*) AS total,",
                    "         SUM(CASE WHEN ipk >= 3.5 THEN 1 ELSE 0 END) AS jml_unggul,",
                    "         COUNT(CASE WHEN ipk < 3.0 THEN 1 END)       AS jml_dibantu",
                    "  FROM mahasiswa",
                    "  GROUP BY jurusan;",
                    "",
                    "PostgreSQL dan SQLite 3.30+ punya bentuk modern yang lebih terbaca:",
                    "  COUNT(*)   FILTER (WHERE ipk >= 3.5)        AS jml_unggul",
                    "  SUM(total) FILTER (WHERE status = 'lunas')  AS pendapatan_lunas",
                    "MySQL belum punya FILTER; di sana tetap pakai CASE.",
                    "",
                    "GROUP BY dan ORDER BY juga menerima NOMOR POSISI kolom di SELECT:",
                    "",
                    "  SELECT jurusan, COUNT(*) FROM mahasiswa GROUP BY 1 ORDER BY 2 DESC;",
                    "",
                    "  1 berarti kolom PERTAMA di daftar SELECT (jurusan), 2 kolom kedua",
                    "  (COUNT(*)). Itu bukan konstanta angka 1 dan 2. Bentuk ini dipakai",
                    "  supaya ekspresi panjang tidak perlu ditulis dua kali, tapi jadi",
                    "  jebakan begitu urutan kolom di SELECT diubah: query tetap jalan,",
                    "  hasilnya diam-diam berubah.",
                ]
            },
        ],
    },
    {
        "title": "9. JOIN: Menghubungkan Tabel",
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
                "heading": "ON, USING & nama panjang yang bukan jenis baru",
                "body": [
                    "Kalau kolom penghubungnya BERNAMA SAMA di kedua tabel, ON boleh",
                    "dipendekkan jadi USING:",
                    "",
                    "  FROM nilai n JOIN mahasiswa m ON n.nim = m.nim",
                    "  FROM nilai n JOIN mahasiswa m USING (nim)     -- maksud yang sama",
                    "",
                    "Bedanya bukan cuma panjang tulisan. Dengan USING, kolom penghubung",
                    "muncul SEKALI saja di hasil; dengan ON ia muncul dua kali (n.nim dan",
                    "m.nim). Jadi SELECT * pada keduanya memberi jumlah kolom yang",
                    "berbeda. Kolom itu juga ditulis polos sesudah USING: SELECT nim,",
                    "bukan n.nim. USING ada di MySQL, PostgreSQL, dan SQLite; SQL Server",
                    "tidak punya.",
                    "",
                    "NATURAL JOIN melangkah lebih jauh: ia menebak sendiri penghubungnya",
                    "dari SEMUA nama kolom yang kebetulan sama di kedua tabel.",
                    "",
                    "  SELECT * FROM nilai NATURAL JOIN mahasiswa;",
                    "",
                    "Hindari di kode produksi. Menambah kolom created_at ke kedua tabel",
                    "diam-diam menjadikannya syarat penggabungan juga, dan query yang",
                    "kemarin benar hari ini mengembalikan nol baris tanpa satu pun pesan",
                    "error. Tulis ON atau USING supaya syaratnya terlihat mata.",
                    "",
                    "Nama panjang yang sering disangka jenis JOIN tersendiri:",
                    "  JOIN       = INNER JOIN        (INNER boleh dihilangkan)",
                    "  LEFT JOIN  = LEFT OUTER JOIN   (OUTER boleh dihilangkan)",
                    "  RIGHT JOIN = RIGHT OUTER JOIN",
                    "  FULL JOIN  = FULL OUTER JOIN",
                    "Kode gaya lama menulis yang panjang; artinya persis sama.",
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
        "title": "10. Subquery & Fungsi Lanjutan",
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
        "title": "11. Fungsi Teks, Tanggal & Agregat Teks",
        "sections": [
            {
                "body": [
                    "Materi 7 sudah memperkenalkan CONCAT(), UPPER(), SUBSTRING(), NOW(), dan DATEDIFF().",
                    "Yang belum disebut: tiap database punya CARA SENDIRI untuk pekerjaan yang persis sama.",
                    "Kode nyata yang kamu baca bisa memakai bentuk mana pun, jadi semuanya harus dikenali.",
                    "",
                    "Menyambung teks:",
                    "  ||        Standar SQL. Jalan di PostgreSQL, SQLite, Oracle, DB2.",
                    "  CONCAT()  MySQL, PostgreSQL 9.1+, SQL Server 2012+, SQLite 3.44+.",
                    "  +         SQL Server.",
                    "",
                    "  SELECT nama_depan || ' ' || nama_belakang FROM pelanggan;      -- PostgreSQL/SQLite",
                    "  SELECT CONCAT(nama_depan, ' ', nama_belakang) FROM pelanggan;  -- hampir di mana saja",
                    "",
                    "JEBAKAN 1 - || di SQL bukan OR.",
                    "  Datang dari Java atau JavaScript, mata kamu membaca a || b sebagai 'a ATAU b'.",
                    "  Di SQL standar artinya 'a disambung b'. Dua arti yang sama sekali berbeda.",
                    "  Lebih parah: di MySQL bawaan, || MEMANG berarti OR (kecuali sql_mode",
                    "  PIPES_AS_CONCAT dinyalakan). Query yang sama diam-diam menghasilkan angka 0 atau 1",
                    "  di MySQL, dan sebuah kalimat di PostgreSQL. Tidak ada pesan error yang menolong.",
                    "",
                    "JEBAKAN 2 - satu NULL merusak seluruh hasil sambungan.",
                    "  'Andi' || NULL        -> NULL   (bukan 'Andi')",
                    "  CONCAT('Andi', NULL)  -> NULL   di MySQL & PostgreSQL",
                    "  Pengecualiannya Oracle, yang memperlakukan NULL sebagai teks kosong.",
                    "  Akibatnya: satu kolom kosong mengosongkan SELURUH kolom hasil, bukan bagiannya saja.",
                    "  Tambal dengan COALESCE(kolom, '') sebelum disambung.",
                    "",
                    "CONCAT_WS('pemisah', a, b, c)  -- WS = With Separator.",
                    "  Pemisahnya ditulis SEKALI di depan, lalu disisipkan sendiri di antara tiap bagian.",
                    "  Bedanya yang penting: CONCAT_WS MELEWATI argumen NULL, bukan menularkannya.",
                    "    CONCAT_WS(', ', 'Bandung', NULL, 'Jawa Barat')  -> 'Bandung, Jawa Barat'",
                    "  Tapi kalau PEMISAHNYA sendiri NULL, hasilnya tetap NULL (MySQL).",
                    "  Dan teks kosong '' TIDAK dilewati - ia tetap menghasilkan pemisah dobel.",
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
                    "Nama berbeda untuk pekerjaan yang sama. Hafalkan KEBUTUHANNYA; namanya dicari belakangan.",
                    "",
                    "Cari posisi sebuah teks di dalam teks lain (hasilnya angka, 0 berarti tidak ketemu):",
                    "  POSITION('@' IN email)  -> bentuk standar SQL (PostgreSQL, MySQL)",
                    "  STRPOS(email, '@')      -> PostgreSQL",
                    "  INSTR(email, '@')       -> MySQL, Oracle, SQLite",
                    "  CHARINDEX('@', email)   -> SQL Server, dan urutan argumennya TERBALIK dari INSTR",
                    "",
                    "Ambil beberapa karakter dari ujung:",
                    "  LEFT(t, 3) dan RIGHT(t, 3)  -> PostgreSQL, MySQL, SQL Server",
                    "  SQLite dan Oracle tidak punya keduanya: pakai substr(t, 1, 3) dan substr(t, -3).",
                    "",
                    "Menambal sampai lebar tertentu (nomor invoice, kode barang, kolom laporan):",
                    "  LPAD('7', 4, '0') -> '0007'      RPAD('AB', 4, '.') -> 'AB..'",
                    "  Ada di PostgreSQL, MySQL, Oracle. SQL Server & SQLite tidak punya; padanannya",
                    "  FORMAT(7, '0000') dan printf('%04d', 7).",
                    "",
                    "Memecah teks per pemisah:",
                    "  SPLIT_PART('a,b,c', ',', 2)      -> 'b'     PostgreSQL",
                    "  SUBSTRING_INDEX('a,b,c', ',', 2) -> 'a,b'   MySQL - BEDA ARTI: n bagian PERTAMA,",
                    "                                              bukan bagian ke-n. Sering salah dipakai.",
                    "  STRING_SPLIT('a,b,c', ',')       -> tabel   SQL Server",
                    "",
                    "Huruf awal tiap kata jadi kapital:",
                    "  INITCAP('budi santoso') -> 'Budi Santoso'   (PostgreSQL, Oracle)",
                    "  MySQL, SQL Server, dan SQLite tidak punya. Biasanya dirapikan di kode aplikasi.",
                    "",
                    "Pencarian tidak peka huruf besar-kecil - ini yang paling sering menipu:",
                    "  PostgreSQL : LIKE PEKA huruf. Pakai ILIKE, atau LOWER(kolom) LIKE LOWER('%budi%').",
                    "  MySQL      : collation bawaannya _ci, jadi LIKE sudah TIDAK peka huruf.",
                    "  SQLite     : LIKE tidak peka huruf, tapi HANYA untuk A-Z (huruf beraksen tetap peka).",
                    "  SQL Server : tergantung collation databasenya.",
                    "  Artinya query yang menemukan data di laptop bisa mengembalikan 0 baris di server,",
                    "  tanpa satu pun error. Kalau ragu, tulis LOWER(kolom) - jelas dan sama di mana-mana.",
                    "  Harganya: fungsi yang membungkus kolom mematikan index (lihat materi Roadmap).",
                    "  Obatnya index berbasis ekspresi: CREATE INDEX idx_email ON pelanggan (LOWER(email));",
                    "",
                    "Agregat teks: seperti COUNT/SUM, tapi hasilnya SATU KALIMAT dari banyak baris.",
                    "  MySQL      : GROUP_CONCAT(nama ORDER BY nama SEPARATOR ', ')",
                    "  PostgreSQL : STRING_AGG(nama, ', ' ORDER BY nama)",
                    "  SQL Server : STRING_AGG(nama, ', ') WITHIN GROUP (ORDER BY nama)",
                    "  Oracle     : LISTAGG(nama, ', ') WITHIN GROUP (ORDER BY nama)",
                    "  SQLite     : group_concat(nama, ', ')   -- ORDER BY di dalamnya baru ada di 3.44",
                    "  PostgreSQL juga punya ARRAY_AGG(nama): hasilnya array {Andi,Citra}, bukan teks.",
                    "",
                    "Bentuknya memang tidak biasa: ORDER BY dan kata kunci SEPARATOR duduk DI DALAM kurung",
                    "fungsi. Tidak ada fungsi lain yang begitu, dan SEPARATOR di MySQL tidak didahului koma.",
                    "Kalau baris itu terbaca seperti salah ketik - ia memang sah, begitulah sintaksnya.",
                    "",
                    "JEBAKAN produksi: MySQL memotong hasil GROUP_CONCAT di group_concat_max_len (bawaan",
                    "1024 byte). Daftar yang panjang terpangkas DIAM-DIAM: cuma muncul warning, bukan error,",
                    "jadi laporannya terlihat wajar padahal isinya kurang.",
                ],
            },
            {
                "heading": "Tanggal: nama yang sama sekali berbeda di tiap database",
                "body": [
                    "Waktu sekarang - beberapa nama untuk satu hal yang sama:",
                    "  CURRENT_TIMESTAMP  standar SQL, ada di hampir semua. Ditulis TANPA kurung.",
                    "  CURRENT_DATE       standar, tanggal saja tanpa jam.",
                    "  NOW()              MySQL & PostgreSQL.",
                    "  CURDATE()          MySQL saja.",
                    "  GETDATE()          SQL Server saja. Oracle memakai SYSDATE.",
                    "  datetime('now')    SQLite - dan ini UTC, bukan waktu lokal komputermu.",
                    "                     Waktu lokal: datetime('now', 'localtime').",
                    "  Menulis CURRENT_TIMESTAMP() pakai kurung ditolak PostgreSQL, diterima MySQL.",
                    "",
                    "Mengambil bagian dari sebuah tanggal:",
                    "  EXTRACT(YEAR FROM tanggal)  bentuk STANDAR. Kata FROM itu ADA DI DALAM kurung,",
                    "                              bukan klausa FROM tabel. Hasilnya angka: 2024.",
                    "  YEAR(tanggal)               pintasan milik MySQL & SQL Server saja.",
                    "  DATE_TRUNC('month', t)      PostgreSQL: potong ke awal bulan. Hasilnya TANGGAL",
                    "                              (2024-03-01), bukan angka - jadi tetap urut benar dan",
                    "                              masih bisa diformat. Ideal untuk laporan bulanan.",
                    "  strftime('%Y-%m', t)        SQLite.  DATE_FORMAT(t, '%Y-%m') di MySQL.",
                    "",
                    "INTERVAL bukan fungsi, melainkan LITERAL - cara menulis nilai bertipe 'lama waktu',",
                    "sejajar dengan angka 30 atau teks 'abc'. Itu sebabnya ia tidak pernah pakai kurung.",
                    "  PostgreSQL : NOW() - INTERVAL '30 days'   angka dan satuannya di dalam kutip",
                    "  MySQL      : NOW() - INTERVAL 30 DAY      tanpa kutip, satuan TUNGGAL, kata kunci",
                    "               DATE_SUB(NOW(), INTERVAL 7 DAY)  dan  DATE_ADD(t, INTERVAL 1 MONTH)",
                    "  SQL Server : DATEADD(DAY, -30, GETDATE())",
                    "  SQLite     : date(t, '-30 days')",
                    "  Menulis INTERVAL 30 DAYS (jamak) adalah error sintaks di MySQL; PostgreSQL santai.",
                    "",
                    "Selisih waktu - di sinilah tanda plus-minusnya paling gampang terbalik:",
                    "  MySQL      : DATEDIFF(a, b)       a dikurangi b, satuannya HARI.",
                    "  SQL Server : DATEDIFF(DAY, a, b)  b dikurangi a. Tiga argumen, arahnya TERBALIK.",
                    "  PostgreSQL : b - a langsung memberi interval. AGE(b, a) -> '1 year 2 mons 3 days'.",
                    "  SQLite     : julianday(b) - julianday(a).",
                    "",
                    "Umur atau lama langganan dalam TAHUN - jangan dihitung dengan membagi 365,",
                    "tahun kabisat membuatnya meleset sehari demi sehari:",
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
                    "Tiga jebakan tanggal yang paling banyak memakan waktu di kode nyata.",
                    "",
                    "1. Menyimpan tanggal sebagai TEKS bebas.",
                    "   Kolom VARCHAR berisi '17/08/2024' terlihat rapi sampai kamu perlu:",
                    "     - Mengurutkan: sebagai teks '05/09/2024' < '17/08/2024', jadi September",
                    "       muncul SEBELUM Agustus. Laporannya salah urut dan tidak ada yang error.",
                    "     - Menghitung: DATEDIFF dan EXTRACT tidak mengerti teks itu.",
                    "     - Menjaga kewarasan data: '2024-02-30' dan '17/8/24' sama-sama masuk tanpa protes.",
                    "   Pakai tipe DATE / TIMESTAMP, lalu format hanya saat MENAMPILKAN:",
                    "     MySQL       DATE_FORMAT(t, '%d-%m-%Y')",
                    "     PostgreSQL  TO_CHAR(t, 'DD-MM-YYYY')    huruf polanya beda, bukan salah ketik",
                    "     SQLite      strftime('%d-%m-%Y', t)",
                    "   SQLite adalah pengecualiannya: ia memang TIDAK punya tipe DATE, semuanya teks atau",
                    "   angka. Justru karena itu disiplin format ISO 'YYYY-MM-DD' jadi wajib di SQLite -",
                    "   cuma format itu yang dimengerti date()/strftime(), dan cuma format itu yang urut",
                    "   benar ketika dibandingkan sebagai teks.",
                    "",
                    "2. Memfilter rentang tanggal dengan cara yang mematikan index.",
                    "   X  WHERE YEAR(tanggal) = 2024",
                    "      Fungsi membungkus kolom, index tidak terpakai, seluruh tabel dihitung ulang.",
                    "   X  WHERE tanggal BETWEEN '2024-01-01' AND '2024-12-31'",
                    "      Kalau kolomnya DATETIME, '2024-12-31' berarti jam 00:00:00. Transaksi tanggal",
                    "      31 Desember jam 10 pagi HILANG dari laporan - diam-diam, tanpa error.",
                    "   V  WHERE tanggal >= '2024-01-01' AND tanggal < '2025-01-01'",
                    "      Rentang setengah terbuka: batas bawah ikut, batas atas tidak. Index tetap",
                    "      terpakai, jam berapa pun tercakup, dan kamu tidak perlu tahu bulan itu isinya",
                    "      28, 30, atau 31 hari. Pola yang sama dipakai untuk sebulan, sehari, atau sejam.",
                    "   Ini lanjutan nasihat 'hindari fungsi pada kolom di WHERE' di materi Roadmap.",
                    "",
                    "3. Zona waktu, secukupnya supaya tidak kaget.",
                    "   TIMESTAMP tanpa zona menyimpan angka jamnya apa adanya: '2024-03-01 09:00'. Kolom",
                    "   itu tidak tahu 09:00 di Jakarta atau di London, jadi dua server bisa berbeda paham.",
                    "   TIMESTAMPTZ di PostgreSQL menyimpan TITIK WAKTU absolut. Namanya menyesatkan: ia",
                    "   tidak menyimpan zona apa pun - nilainya disimpan sebagai UTC, lalu dikonversi ke",
                    "   zona sesi saat dibaca.",
                    "   Di MySQL, DATETIME disimpan apa adanya sedangkan TIMESTAMP dikonversi ke UTC saat",
                    "   disimpan. Konsekuensinya: mengubah zona server MENGUBAH ARTI data lama di kolom",
                    "   TIMESTAMP, padahal tidak ada satu baris pun yang di-UPDATE.",
                    "   Aturan praktis yang menyelamatkan banyak orang:",
                    "     SIMPAN dalam UTC, TAMPILKAN dalam waktu lokal pengguna.",
                    "   Konversi ke waktu lokal adalah urusan lapisan tampilan, bukan urusan tabel.",
                ],
            },
        ],
    },
    {
        "title": "12. EXISTS, Subquery Berkorelasi & Operator Himpunan",
        "sections": [
            {
                "body": [
                    "Subquery yang sudah dikenal berdiri SENDIRI: isi kurungnya bisa dipotong,",
                    "ditempel ke jendela lain, dijalankan terpisah, dan hasilnya sama saja.",
                    "",
                    "  SELECT AVG(ipk) FROM mahasiswa      -- jalan sendirian, hasilnya satu angka",
                    "",
                    "Subquery BERKORELASI tidak bisa. Ia menyebut kolom milik query di LUARnya:",
                    "",
                    "  SELECT m.nama FROM mahasiswa m",
                    "  WHERE m.ipk = (SELECT MAX(ipk) FROM mahasiswa WHERE jurusan = m.jurusan);",
                    "                                                            ^^^^^^^^^",
                    "                            m.jurusan tidak ada artinya di luar query ini",
                    "",
                    "Kenapa alias m boleh dipakai di dalam kurung? Karena alias yang dideklarasikan di",
                    "FROM query luar berlaku untuk SELURUH query, termasuk subquery yang bersarang di",
                    "dalamnya. Kebalikannya tidak berlaku: alias yang lahir di dalam subquery tidak",
                    "dikenal di luar — kurungnya seperti dinding kaca, bisa dilihat dari dalam saja.",
                    "",
                    "Di sinilah model mental 'subquery dijalankan lebih dulu, hasilnya dipakai query",
                    "utama' (kalimat yang dipakai di penjelasan Kuis 5) patah. Untuk bentuk yang",
                    "berkorelasi, urutannya justru terbalik:",
                    "",
                    "  untuk SETIAP baris query luar:",
                    "      jalankan ulang subquery-nya dengan nilai baris itu",
                    "",
                    "Lima baris mahasiswa berarti MAX(ipk) dihitung lima kali. Query di atas benar dan",
                    "aman untuk tabel kecil, tapi di tabel satu juta baris ia berarti satu juta",
                    "subquery — inilah biang query yang 'hasilnya betul tapi lambatnya keterlaluan'.",
                    "",
                    "Query planner modern sering pandai menulis ulangnya sendiri, tapi jangan pernah",
                    "bergantung pada itu. Kalau versi JOIN atau window function-nya ada, pilih itu:",
                    "keduanya membaca tabelnya sekali, bukan sekali per baris.",
                    "",
                    "Cara mengenalinya dalam sekejap: lihat ke dalam kurung. Ada alias dari luar?",
                    "Berarti berkorelasi, dan ia jalan berulang kali.",
                ],
            },
            {
                "heading": "Yang berkorelasi, dan dua cara menghindarinya",
                "body": [
                    "Contoh di bawah memakai subquery di TIGA tempat berbeda. Dua di antaranya baru:",
                    "",
                    "  Di FROM (derived table / tabel turunan) -> hasil subquery diperlakukan sebagai",
                    "  tabel sementara. Ia WAJIB diberi alias. MySQL menolak dengan pesan terkenal",
                    "  'Every derived table must have its own alias', PostgreSQL dengan 'subquery in",
                    "  FROM must have an alias'. SQLite kebetulan membolehkannya, tapi tetap tulis:",
                    "  tanpa nama, kolomnya tidak bisa dirujuk dari luar. Kata 'hasil' yang menempel",
                    "  di kurung tutup pada contoh TOP 3 di materi Window Function itu alias, bukan",
                    "  hiasan yang bisa dihapus.",
                    "",
                    "  Di daftar SELECT (subquery skalar) -> jadi kolom tambahan. Batasnya keras: harus",
                    "  mengembalikan TEPAT satu baris dan satu kolom. Dua kolom ditolak semua database",
                    "  ('sub-select returns 2 columns - expected 1'). Dua baris lebih licik: MySQL dan",
                    "  PostgreSQL melempar error saat query DIJALANKAN, sedangkan SQLite diam-diam",
                    "  memakai baris pertama — yang lolos di laptopmu bisa meledak di server sungguhan.",
                    "  Kalau tidak ada baris yang cocok, hasilnya NULL: bukan nol, dan bukan error.",
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
                    "EXISTS (subquery) bernilai benar kalau subquery-nya menghasilkan MINIMAL SATU",
                    "baris. Yang diperiksa keberadaan BARISnya, bukan isi barisnya. Karena itu idiom",
                    "bakunya begini:",
                    "",
                    "  WHERE EXISTS (SELECT 1 FROM nilai n WHERE n.nim = m.nim)",
                    "",
                    "Angka 1 di situ bukan nomor kolom dan bukan trik performa. Ia cuma pengisi tempat",
                    "karena SELECT tetap butuh sesuatu untuk ditulis. SELECT *, SELECT n.skor, bahkan",
                    "SELECT 'apa pun' memberi hasil yang sama persis — database berhenti begitu ketemu",
                    "baris pertama dan tidak pernah repot membaca nilainya.",
                    "",
                    "EXISTS hampir selalu berkorelasi. Kalau subquery-nya tidak menyebut kolom luar,",
                    "jawabannya sama untuk semua baris dan tidak ada gunanya menulisnya sama sekali.",
                    "",
                    "Dua istilah yang akan sering kamu temui di pembahasan performa dan di keluaran",
                    "EXPLAIN:",
                    "  semi-join -> ambil baris kiri yang PUNYA pasangan, tanpa menampilkan kolom",
                    "               kanannya dan tanpa menggandakan baris kiri.",
                    "  anti-join -> kebalikannya: ambil baris kiri yang TIDAK punya pasangan.",
                    "",
                    "Anti-join bisa ditulis tiga cara. Ketiganya lazim, jadi kamu harus bisa membaca",
                    "semuanya walau yang kamu tulis sendiri cuma satu:",
                    "",
                    "  LEFT JOIN + IS NULL -> cara paling tua, jalan di database mana pun. Ini bentuk",
                    "                         yang sudah dipakai materi JOIN. IS NULL wajib diarahkan",
                    "                         ke kolom yang TIDAK PERNAH NULL di tabel kanan (biasanya",
                    "                         kuncinya); salah kolom, hasilnya diam-diam meleset.",
                    "  NOT EXISTS          -> paling jelas maksudnya dan aman terhadap NULL.",
                    "                         Jadikan ini pilihan bawaanmu.",
                    "  NOT IN (subquery)   -> paling pendek, dan punya jebakan di bawah ini.",
                    "",
                    "JEBAKAN NOT IN: kalau hasil subquery-nya memuat satu saja NULL, seluruh query",
                    "mengembalikan NOL baris. Sebabnya logika tiga nilai (lihat materi Ekspresi, NULL",
                    "& CASE): x NOT IN (101, NULL) sama dengan x <> 101 AND x <> NULL, sedangkan",
                    "x <> NULL selalu 'tidak diketahui' — tidak pernah benar, jadi AND-nya tidak",
                    "pernah benar. Tidak ada error, tidak ada peringatan; hasilnya cuma kosong dan",
                    "query-nya kelihatan sehat-sehat saja. Ini alasan utama orang berpengalaman",
                    "menulis NOT EXISTS. Kalau tetap mau NOT IN, saring dulu: WHERE nim IS NOT NULL.",
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
                    "UNION dan UNION ALL sudah dipakai di materi Subquery dan di recursive CTE.",
                    "Keluarga lengkapnya ada empat, dan dua sisanya sama pentingnya:",
                    "",
                    "  UNION      -> gabungan, duplikat DIBUANG (perlu menyortir, jadi lebih mahal)",
                    "  UNION ALL  -> gabungan apa adanya, duplikat DIPERTAHANKAN (paling murah)",
                    "  INTERSECT  -> irisan: baris yang muncul di KEDUA hasil",
                    "  EXCEPT     -> selisih: baris hasil pertama yang TIDAK ada di hasil kedua",
                    "",
                    "Aturannya identik untuk keempatnya:",
                    "  - Jumlah kolom kedua sisi harus sama dan tipenya sepadan; kalau tidak, error.",
                    "  - Nama kolom hasil diambil dari query PERTAMA, alias di query kedua diabaikan.",
                    "  - Yang dibandingkan SELURUH baris, bukan cuma kolom pertamanya.",
                    "  - ORDER BY cuma boleh sekali, di paling akhir, dan miliknya gabungan itu.",
                    "  - INTERSECT dan EXCEPT juga membuang duplikat, sama seperti UNION.",
                    "",
                    "Nama yang berbeda antar database: Oracle menyebut EXCEPT sebagai MINUS — artinya",
                    "sama persis. MySQL baru punya INTERSECT dan EXCEPT sejak 8.0.31; sebelum itu",
                    "orang menirunya dengan JOIN dan NOT EXISTS. PostgreSQL dan SQLite sudah lama",
                    "punya keempatnya, plus varian INTERSECT ALL / EXCEPT ALL yang menghitung duplikat.",
                    "",
                    "Inilah alat utama skrip rekonsiliasi dan audit: membandingkan dua daftar yang",
                    "seharusnya sama — tabel lama vs hasil migrasi, catatan kita vs rekening koran",
                    "bank — lalu bertanya 'apa yang hilang?' dan 'apa yang tiba-tiba muncul?'.",
                    "EXCEPT dua arah menjawab keduanya, dan hasil kosong di dua-duanya berarti cocok.",
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
                    "Di materi 'DML: Insert, Update, Delete' semua nilai INSERT selalu kamu ketik",
                    "sendiri lewat VALUES. Di kode nyata bentuk itu justru yang paling jarang: skrip",
                    "migrasi, sinkronisasi, arsip, dan seed hampir selalu mengambil datanya dari tabel",
                    "lain. Bentuknya INSERT ... SELECT, dan kata VALUES hilang sama sekali.",
                    "",
                    "  INSERT INTO arsip (id, email, tanggal, total)",
                    "  SELECT id, email, tanggal, total",
                    "  FROM pesanan",
                    "  WHERE tanggal < '2024-01-01';",
                    "",
                    "Pertama kali melihatnya, otak gampang membacanya sebagai DUA perintah yang lupa",
                    "dipisah titik koma. Bukan. Itu SATU statement. INSERT selalu butuh dua hal: mau",
                    "diisi ke mana, dan datanya dari mana. 'Dari mana' itulah yang boleh berupa VALUES",
                    "ATAU berupa SELECT. Titik komanya cuma satu, di paling akhir. Berapa pun baris",
                    "yang dikembalikan SELECT-nya, sebanyak itu pula baris yang masuk - nol pun boleh,",
                    "dan itu bukan error.",
                    "",
                    "Yang dicocokkan adalah URUTAN dan JUMLAH kolom, BUKAN namanya:",
                    "  - Kolom ke-1 di daftar INSERT diisi kolom ke-1 hasil SELECT, dan seterusnya.",
                    "  - Nama boleh beda total; alias di SELECT tidak dilihat sama sekali.",
                    "  - Jumlahnya beda -> error, ketahuan langsung.",
                    "  - Urutannya tertukar tapi tipenya kebetulan cocok -> TIDAK error. Datanya diam-",
                    "    diam masuk ke kolom yang salah. Ini jebakan yang paling mahal di sini.",
                    "",
                    "SELECT-nya query biasa: boleh JOIN, GROUP BY, subquery, ORDER BY, apa saja.",
                    "",
                    "CTAS (CREATE TABLE AS SELECT) - bikin tabel BARU sekaligus mengisinya, tanpa",
                    "harus mengetik daftar kolomnya lebih dulu:",
                    "  CREATE TABLE ringkasan AS SELECT email, SUM(total) AS nilai FROM arsip",
                    "  GROUP BY email;",
                    "  Di SQL Server bentuknya lain sendiri, tabelnya disebut di tengah:",
                    "  SELECT email, SUM(total) AS nilai INTO ringkasan FROM arsip GROUP BY email;",
                    "",
                    "Jebakan CTAS: yang ikut cuma nama kolom, tipe, dan datanya. PRIMARY KEY, index,",
                    "NOT NULL, DEFAULT, dan FOREIGN KEY TIDAK ikut. Tabel hasil CTAS yang lalu dipakai",
                    "sebagai tabel sungguhan hampir selalu jadi tabel yang lupa punya kunci.",
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
                    "UPDATE dan DELETE yang sudah kamu pelajari selalu memakai nilai yang diketik",
                    "tangan. Yang jauh lebih sering di kode nyata: nilainya diambil dari tabel LAIN.",
                    "Sayangnya di sinilah tiap database paling banyak berbeda - hafalkan bentuk milik",
                    "database yang kamu pakai, dan jangan kaget melihat tiga bentuk untuk satu maksud.",
                    "",
                    "Menyalin diskon milik pelanggan ke tiap pesanannya:",
                    "",
                    "  MySQL / MariaDB (JOIN dulu, SET belakangan):",
                    "      UPDATE pesanan p",
                    "      JOIN pelanggan k ON p.email = k.email",
                    "      SET p.diskon = k.diskon;",
                    "",
                    "  PostgreSQL / SQLite 3.33+ (SET dulu, FROM belakangan):",
                    "      UPDATE pesanan AS p",
                    "      SET diskon = k.diskon",
                    "      FROM pelanggan AS k",
                    "      WHERE p.email = k.email;",
                    "",
                    "  SQL Server (tabelnya disebut dua kali, di UPDATE dan di FROM):",
                    "      UPDATE p SET p.diskon = k.diskon",
                    "      FROM pesanan p JOIN pelanggan k ON p.email = k.email;",
                    "",
                    "Bentuk yang jalan di SEMUA database, memakai subquery berkorelasi (materi",
                    "'Subquery & Fungsi Lanjutan'):",
                    "      UPDATE pesanan",
                    "      SET diskon = (SELECT k.diskon FROM pelanggan k WHERE k.email = pesanan.email)",
                    "      WHERE EXISTS (SELECT 1 FROM pelanggan k WHERE k.email = pesanan.email);",
                    "",
                    "JEBAKAN TERBESAR ada di baris WHERE EXISTS itu. Kalau kamu buang - dan hampir",
                    "semua orang membuangnya karena kelihatan mubazir - baris pesanan yang emailnya",
                    "TIDAK punya pasangan tetap ikut ter-UPDATE. Subquery-nya mengembalikan NULL untuk",
                    "baris itu, jadi diskon-nya ditimpa jadi NULL. Bukan error, bukan peringatan;",
                    "datanya cuma hilang diam-diam. Bandingkan: bentuk UPDATE ... FROM di atas",
                    "melewatkan baris tak berpasangan begitu saja karena WHERE-nya menyaring dulu.",
                    "",
                    "DELETE juga punya bentuk lintas tabel:",
                    "  PostgreSQL : DELETE FROM pesanan p USING pelanggan k",
                    "               WHERE p.email = k.email AND k.status = 'blokir';",
                    "  MySQL      : DELETE p FROM pesanan p",
                    "               JOIN pelanggan k ON p.email = k.email WHERE k.status = 'blokir';",
                    "  Portabel   : DELETE FROM pesanan",
                    "               WHERE email IN (SELECT email FROM pelanggan WHERE status = 'blokir');",
                    "",
                    "'DELETE p FROM ...' di MySQL bukan salah ketik. Saat ada dua tabel yang di-JOIN,",
                    "alias sesudah DELETE menentukan tabel MANA yang barisnya dibuang. Lupa menulis",
                    "alias itu = sintaks error; salah menulisnya = tabel yang salah yang terhapus.",
                ],
            },
            {
                "body": [
                    "UPSERT = 'simpan kalau baru, perbarui kalau sudah ada'. Sebelum tahu ini ada,",
                    "semua orang menuliskannya begini di aplikasi:",
                    "",
                    "  1. SELECT ... WHERE email = 'andi@mail.com';   -- sudah ada belum?",
                    "  2. kalau ada  -> UPDATE",
                    "  3. kalau tidak -> INSERT",
                    "",
                    "Itu bukan sekadar boros tiga langkah. Itu RUSAK. Di antara langkah 1 dan 3 ada",
                    "celah waktu. Kalau dua proses - dua permintaan web, dua worker, dua tab browser -",
                    "memeriksa pada saat yang sama, keduanya sama-sama melihat 'belum ada' dan keduanya",
                    "melakukan INSERT. Hasilnya baris ganda, atau error UNIQUE yang muncul cuma",
                    "sesekali dan mustahil ditiru ulang saat kamu mencoba mencarinya. UPSERT menutup",
                    "celah itu karena pemeriksaan dan penulisannya dikerjakan database dalam SATU",
                    "perintah: tidak ada jeda untuk disusupi. Ini alasan utamanya ada, jauh lebih",
                    "penting daripada urusan hemat baris kode.",
                    "",
                    "Syarat mutlak: kolom penentu 'sudah ada' HARUS punya PRIMARY KEY atau UNIQUE.",
                    "Tanpa itu tidak ada yang namanya konflik - PostgreSQL menolak perintahnya, dan",
                    "yang lain menerima tapi klausanya tidak pernah menyala sekali pun.",
                    "",
                    "Dari mana nilai 'yang tadi mau dimasukkan' diambil ketika berubah jadi UPDATE?",
                    "  PostgreSQL & SQLite : dari pseudo-tabel excluded (di dokumentasi sering ditulis",
                    "                        EXCLUDED). excluded.nama = nilai yang barusan GAGAL masuk.",
                    "                        pelanggan.nama = nilai yang SUDAH ada di tabel.",
                    "                        Tanpa dua nama itu kamu tidak bisa membedakan keduanya.",
                    "  MySQL & MariaDB     : dari fungsi VALUES(nama). Sejak MySQL 8.0.20 bentuk itu",
                    "                        deprecated dan diganti alias baris - INSERT ... VALUES",
                    "                        (...) AS baru ON DUPLICATE KEY UPDATE nama = baru.nama;",
                    "                        Kamu akan menemui kedua bentuk di kode yang beredar.",
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
                    "Sesudah INSERT, hampir selalu kamu butuh id baris yang baru dibuat - untuk",
                    "dipasang sebagai FOREIGN KEY di tabel berikutnya. Jangan pernah menebaknya dengan",
                    "SELECT MAX(id): dua proses yang menyisip bersamaan akan sama-sama mendapat angka",
                    "yang sama, lalu salah satunya menempelkan datanya ke baris milik orang lain.",
                    "",
                    "Cara yang benar, per database:",
                    "  PostgreSQL / SQLite 3.35+ / MariaDB : klausa RETURNING",
                    "      INSERT INTO pesanan (email, total) VALUES ('citra@mail.com', 75000)",
                    "      RETURNING id, total;",
                    "  MySQL      : SELECT LAST_INSERT_ID();   (MySQL belum punya RETURNING)",
                    "  SQL Server : SELECT SCOPE_IDENTITY();   atau klausa OUTPUT INSERTED.id",
                    "  SQLite     : SELECT last_insert_rowid();",
                    "",
                    "LAST_INSERT_ID() dan SCOPE_IDENTITY() nilainya per KONEKSI, jadi aman dari proses",
                    "lain. Tapi pada INSERT banyak baris sekaligus, LAST_INSERT_ID() mengembalikan id",
                    "baris PERTAMA, bukan yang terakhir - banyak orang menyangka sebaliknya.",
                    "",
                    "RETURNING tidak cuma untuk INSERT. Ia jalan juga di UPDATE dan DELETE, dan itulah",
                    "cara paling rapi mengetahui persis baris mana yang barusan kena:",
                    "      DELETE FROM sesi WHERE kedaluwarsa < '2024-01-01' RETURNING id;",
                    "",
                    "Menghapus banyak baris di tabel besar: jangan sekali tembak. Satu DELETE atas",
                    "jutaan baris mengunci baris-barisnya lama sekali, menggemukkan log transaksi, dan",
                    "bisa membuat aplikasi ikut macet. Hapus bertahap, ulangi sampai tidak ada lagi",
                    "yang terhapus:",
                    "      MySQL      : DELETE FROM log WHERE tanggal < '2024-01-01' LIMIT 1000;",
                    "      PostgreSQL : DELETE FROM log WHERE id IN (",
                    "                       SELECT id FROM log WHERE tanggal < '2024-01-01' LIMIT 1000);",
                    "  PostgreSQL tidak menerima LIMIT langsung pada DELETE, jadi batasnya dipasang",
                    "  di subquery. Bentuk kedua ini jalan di MySQL dan SQLite juga.",
                    "",
                    "TRUNCATE vs DELETE - bukan sekadar 'versi cepatnya' seperti yang disinggung di",
                    "materi DDL:",
                    "  DELETE FROM t;     -> baris dibuang satu per satu, trigger MENYALA, bisa",
                    "                        di-ROLLBACK, dan nomor AUTO_INCREMENT lanjut dari",
                    "                        angka terakhir - baris berikutnya tidak mulai dari 1.",
                    "  TRUNCATE TABLE t;  -> isinya dibuang sekaligus, trigger TIDAK menyala, dan",
                    "                        AUTO_INCREMENT direset ke 1 (di PostgreSQL hanya kalau",
                    "                        kamu tulis TRUNCATE t RESTART IDENTITY).",
                    "",
                    "  Kalau ada tabel lain yang menunjuk t lewat FOREIGN KEY, TRUNCATE DITOLAK:",
                    "  MySQL/InnoDB menolak mentah-mentah, PostgreSQL minta kamu menulis CASCADE",
                    "  (yang ikut mengosongkan tabel anaknya - baca dua kali sebelum mengetiknya).",
                    "  DELETE tetap jalan dan menghormati aturan ON DELETE yang kamu pasang.",
                    "  Di MySQL, TRUNCATE melakukan commit otomatis: sekali jalan, ROLLBACK tidak",
                    "  bisa menolongmu lagi. SQLite tidak punya TRUNCATE sama sekali - pakai",
                    "  DELETE FROM t;.",
                ],
            },
        ],
    },
    {
        "title": "14. Index, Normalisasi & Best Practice",
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
        "title": "15. Keamanan Query: Parameter, Injeksi & Hak Akses",
        "sections": [
            {
                "body": [
                    "Sampai sini kamu selalu mengetik SQL langsung ke prompt database. Di kode",
                    "nyata itu justru pengecualian. SQL biasanya berupa STRING di dalam program",
                    "Java, Python, atau JavaScript - dan string itu hampir selalu BERLUBANG:",
                    "",
                    "  // Java (JDBC)",
                    "  String sql = \"SELECT id, nama FROM pengguna WHERE email = ?\";",
                    "",
                    "  # Python (sqlite3, psycopg, mysql-connector)",
                    "  sql = \"SELECT id, nama FROM pengguna WHERE email = %s\"",
                    "",
                    "  // JavaScript (node-postgres)",
                    "  const sql = 'SELECT id, nama FROM pengguna WHERE email = $1'",
                    "",
                    "Tanda ? , %s , dan $1 itu BUKAN bagian dari bahasa SQL. Kamu tidak akan",
                    "menemukannya di dokumentasi MySQL. Ia lubang: penanda 'nilainya menyusul,",
                    "jangan diketik di sini'. Yang mengisinya adalah pustaka penghubung",
                    "database (driver), tepat sebelum query dikirim.",
                    "",
                    "Bentuk lubangnya beda-beda tergantung pustaka, bukan tergantung database:",
                    "  ?         -> JDBC (Java), SQLite, MySQL Connector, PHP PDO",
                    "  %s        -> Python DB-API: psycopg2, mysql-connector, MySQLdb",
                    "  :nama     -> named parameter: Spring JDBC, SQLAlchemy, Oracle, SQLite",
                    "  $1 $2 $3  -> PostgreSQL asli & node-postgres (bernomor, mulai dari 1)",
                    "",
                    "Jangan hafal satu bentuk lalu bingung melihat bentuk lain. Artinya sama",
                    "persis. Dua hal yang sering bikin salah:",
                    "  - %s di Python DB-API BUKAN format string Python. Ia tetap ditulis %s",
                    "    walau nilainya angka, dan nilainya dikirim sebagai argumen kedua",
                    "    execute(), bukan lewat % atau f-string.",
                    "  - Placeholder TIDAK diapit tanda kutip. Menulis email = '?' membuatnya",
                    "    jadi teks satu karakter, bukan lubang.",
                ],
            },
            {
                "heading": "Kenapa menyambung string itu berbahaya",
                "body": [
                    "Query di bawah dirangkai dengan penyambungan string, cara yang paling",
                    "sering dilihat pemula karena paling gampang ditulis:",
                    "",
                    "  sql = \"SELECT id, email FROM pengguna WHERE email = '\" + email",
                    "      + \"' AND sandi = '\" + sandi + \"'\"",
                    "",
                    "Jalankan blok ini lalu bandingkan tiga hasilnya. Di query ketiga, yang",
                    "diketik di kolom sandi bukan sandi siapa pun - tapi seluruh isi tabel",
                    "tetap keluar, termasuk akun admin.",
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
                    "Query ketiga tadi dibaca database sebagai: (email cocok DAN sandi",
                    "kosong) ATAU ('1' sama dengan '1'). Bagian kanan selalu benar, jadi",
                    "SEMUA baris lolos. Penyerang tidak menebak sandi siapa pun; ia mengubah",
                    "bentuk query-nya. Itulah SQL injection.",
                    "",
                    "Dengan lubang ? nilainya dikirim TERPISAH dari teks query. Database",
                    "menerima dua hal: kerangka query yang sudah selesai dibaca, lalu daftar",
                    "nilai. Nilai yang datang belakangan tidak pernah dibaca ulang sebagai",
                    "perintah - mau isinya ' OR '1'='1 atau '; DROP TABLE pengguna; -- ia",
                    "tetap satu potong teks yang dicari di kolom sandi, dan hasilnya nol baris.",
                    "",
                    "Jadi placeholder bukan 'escape otomatis'. Bedanya besar:",
                    "  escape -> teksnya tetap disambung, cuma karakter bahaya dipagari.",
                    "  bind   -> teksnya TIDAK PERNAH disambung sama sekali.",
                    "",
                    "Kenapa 'ya sudah, buang saja tanda kutipnya' tidak pernah cukup:",
                    "  - Nilai angka tidak butuh kutip. WHERE id = 5 OR 1=1 tembus tanpa satu",
                    "    pun tanda kutip.",
                    "  - Tanda kutip bisa ditulis lebih dari satu cara: digandakan, dilarikan",
                    "    dengan backslash, atau lewat penyandian karakter. Filter buatan",
                    "    sendiri selalu ketinggalan satu kasus.",
                    "  - Yang menulis parser SQL adalah pembuat database, bukan kamu. Jangan",
                    "    bertanding menebak apa yang akan ia anggap perintah.",
                    "",
                    "Di Java, lubang ? diisi lewat PreparedStatement (bawaan JDBC). Materi",
                    "Index, Normalisasi & Best Practice menyarankan JDBC dan Spring tanpa",
                    "sempat menyebut kelas ini - padahal inilah bentuk yang benar:",
                    "",
                    "  String sql = \"SELECT id, nama FROM pengguna WHERE email = ? AND aktif = ?\";",
                    "  try (PreparedStatement ps = koneksi.prepareStatement(sql)) {",
                    "      ps.setString(1, emailDariForm);   // nomor mulai dari 1, bukan 0",
                    "      ps.setBoolean(2, true);",
                    "      ResultSet rs = ps.executeQuery();",
                    "  }",
                    "",
                    "Saudaranya, Statement (tanpa 'Prepared'), menerima query jadi berupa satu",
                    "string utuh. Begitu kamu melihat Statement dipakai bersama query yang",
                    "disambung pakai +, itu lampu kuning. Bonus: PreparedStatement yang sama",
                    "dipakai berulang juga lebih cepat, karena rencana query-nya tidak disusun",
                    "ulang setiap kali dipanggil.",
                    "",
                    "Kalau nanti kamu memakai JPA/Hibernate atau Spring Data, kamu jarang",
                    "menulis ini sendiri - ORM membuat PreparedStatement di balik layar untuk",
                    "setiap findByEmail(...). Tapi begitu kamu menulis query manual dengan",
                    "@Query atau createNativeQuery, tanggung jawabnya kembali ke tanganmu.",
                ],
            },
            {
                "heading": "Yang tidak bisa dijadikan parameter, dan hak akses (DCL)",
                "body": [
                    "Placeholder hanya berlaku untuk NILAI. Yang berikut ini tidak akan pernah",
                    "bisa diganti ?, dan mencobanya menghasilkan error sintaks:",
                    "  - Nama tabel dan nama kolom.",
                    "  - Kolom serta arah urutan di ORDER BY (ASC / DESC).",
                    "  - Kata kunci SQL apa pun.",
                    "",
                    "Sebabnya sama dengan alasan ia aman: kerangka query sudah dibaca dan",
                    "direncanakan sebelum nilai datang, dan database tidak bisa merencanakan",
                    "pembacaan tabel yang namanya belum diketahui.",
                    "",
                    "Cara benarnya DAFTAR PUTIH (whitelist), bukan sambung string:",
                    "  kolom_boleh = {\"nama\": \"nama\", \"nilai\": \"ipk\", \"tanggal\": \"tanggal\"}",
                    "  kolom = kolom_boleh.get(pilihan_pengguna)",
                    "  if kolom is None:",
                    "      raise ValueError(\"kolom tidak dikenal\")",
                    "  sql = f\"SELECT nim, nama FROM mahasiswa ORDER BY {kolom} DESC\"",
                    "",
                    "Yang disambung bukan masukan pengguna, melainkan salah satu nilai dari",
                    "daftar yang KAMU tulis sendiri. Masukan pengguna cuma dipakai untuk",
                    "MEMILIH dari daftar itu. Ini bedanya tipis tapi menentukan.",
                    "",
                    "Lapis pertahanan kedua: DCL (Data Control Language) - kategori yang",
                    "disebut sekilas di materi pertama lalu tidak pernah muncul lagi. Isinya",
                    "cuma soal siapa boleh melakukan apa.",
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
                    "Prinsip hak paling kecil (least privilege): tiap user database dikasih",
                    "hak seminimal yang membuat pekerjaannya jalan, tidak lebih.",
                    "",
                    "Kenapa aplikasi tidak boleh menyambung sebagai root: root boleh DROP",
                    "DATABASE. Satu lubang injeksi di satu halaman pencarian sudah cukup untuk",
                    "menghapus segalanya. Dengan user yang cuma punya SELECT/INSERT/UPDATE di",
                    "satu database, perintah DROP TABLE yang disuntikkan berhenti dengan",
                    "penolakan - kerusakannya dibatasi tanpa perlu kode aplikasi ikut sempurna.",
                    "",
                    "Karena itu satu aplikasi sering punya lebih dari satu koneksi database:",
                    "  - koneksi harian  -> SELECT, INSERT, UPDATE. Dipakai 99% waktu.",
                    "  - koneksi migrasi -> CREATE, ALTER, DROP. Hanya hidup saat deploy,",
                    "                       saat menjalankan skrip perubahan struktur tabel.",
                    "  - koneksi laporan -> SELECT saja, sering diarahkan ke replika baca",
                    "                       agar query berat tidak mengganggu pengguna.",
                    "",
                    "Akibat yang wajib kamu kenali: query yang SUDAH BENAR bisa gagal.",
                    "  MySQL      : ERROR 1142 (42000): DELETE command denied to user",
                    "               'app_toko'@'localhost' for table 'produk'",
                    "  PostgreSQL : ERROR: permission denied for table produk",
                    "",
                    "Pesan itu bukan soal sintaks, bukan soal typo, dan tidak akan hilang",
                    "walau query-nya kamu tulis ulang seratus kali. Artinya user-nya memang",
                    "tidak diberi hak itu. Jebakannya: orang menghabiskan sejam memperbaiki",
                    "SQL yang sebetulnya sempurna. Begitu melihat kata denied atau permission,",
                    "berhenti mengedit query - jalankan SHOW GRANTS dulu.",
                    "",
                    "Kebiasaan lain yang menyertainya:",
                    "  1. Sandi pengguna JANGAN pernah disimpan sebagai teks polos. Simpan",
                    "     hasil hash (bcrypt/argon2, bukan MD5 atau SHA1 polos), dan cocokkan",
                    "     di kode aplikasi - bukan dengan WHERE sandi = '...'. Kalau database",
                    "     bocor, yang bocor tidak boleh langsung berupa sandi semua orang.",
                    "  2. Sandi database sendiri (yang di IDENTIFIED BY) jangan ikut ke Git.",
                    "     Simpan di variabel lingkungan atau berkas konfigurasi yang diabaikan",
                    "     Git. Repositori publik penuh sandi yang lupa dihapus.",
                    "  3. Ambil kolom seperlunya. SELECT * ikut menyeret kolom hash sandi dan",
                    "     nomor identitas ke log aplikasi dan ke respons API tanpa sengaja.",
                    "  4. Catat perubahan penting: siapa mengubah apa, kapan. Bisa lewat log",
                    "     di aplikasi, atau tabel log yang diisi TRIGGER (lihat materi View,",
                    "     Stored Procedure & Trigger). Tanpa itu, saat ada data hilang kamu",
                    "     tidak punya satu pun petunjuk untuk ditelusuri.",
                ],
            },
        ],
    },
    {
        "title": "16. Membaca EXPLAIN & Rencana Eksekusi",
        "sections": [
            {
                "body": [
                    "SQL itu bahasa DEKLARATIF: kamu menulis APA yang kamu mau, bukan CARA mengambilnya.",
                    "'Ambil nama mahasiswa Informatika beserta nilainya' - titik. Kamu tidak pernah",
                    "menyuruh database membaca tabel A dulu atau memakai index B.",
                    "",
                    "Yang memilih CARANYA adalah query optimizer di dalam database: tabel mana dibaca",
                    "lebih dulu, index mana dipakai (atau justru diabaikan), bagaimana dua tabel",
                    "disatukan, perlu-tidaknya membuat tabel sementara.",
                    "",
                    "Rencana eksekusi (execution plan) = kumpulan keputusan itu.",
                    "EXPLAIN adalah cara bertanya: 'query ini rencananya kamu kerjakan bagaimana?'",
                    "",
                    "Kenapa ini yang menentukan: dua query dengan hasil SAMA PERSIS bisa berbeda",
                    "seribu kali kecepatannya, dan bedanya cuma di rencana. Tanpa membaca rencananya,",
                    "'optimasi' tinggal tebak-tebakan - menambah index asal-asalan, lalu bingung kenapa",
                    "query-nya tetap lambat sementara INSERT-nya ikut melambat.",
                    "",
                    "Tiga perintah, tiga database, jangan tertukar:",
                    "  MySQL       EXPLAIN <query>            -> merencanakan saja, query TIDAK jalan.",
                    "              EXPLAIN ANALYZE <query>    -> query DIJALANKAN, lalu dilaporkan.",
                    "  PostgreSQL  EXPLAIN <query>            -> merencanakan saja.",
                    "              EXPLAIN ANALYZE <query>    -> query DIJALANKAN sungguhan.",
                    "  SQLite      EXPLAIN QUERY PLAN <query> -> ringkasan rencana, tidak dijalankan.",
                    "              EXPLAIN <query>            -> BUKAN yang kamu cari: itu bytecode",
                    "                                            mesin virtual SQLite, belasan baris",
                    "                                            opcode seperti OpenRead dan Rewind.",
                    "",
                    "Jebakan yang bisa merusak data: EXPLAIN ANALYZE benar-benar MENJALANKAN",
                    "query-nya. 'EXPLAIN ANALYZE DELETE FROM pesanan WHERE ...' sungguh menghapus",
                    "barisnya. Kalau yang dianalisa perintah yang mengubah data, bungkus dengan",
                    "transaction (lihat materi Transaction) lalu batalkan:",
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
                    "Tanpa \\G di ujung, MySQL mencetaknya sebagai tabel selebar 120-an karakter yang",
                    "hancur berantakan di layar sempit. \\G memutarnya jadi satu kolom per baris. Isinya",
                    "sama persis - dan satu 'row' di sini artinya satu TABEL yang dibaca, bukan satu",
                    "baris data. Query di atas menyentuh dua tabel, jadi rencananya dua row.",
                    "",
                    "'1 warning' di baris terakhir bukan tanda ada yang salah: MySQL 8 selalu menyimpan",
                    "query hasil tulis-ulangnya sendiri di situ, dan bisa dilihat dengan SHOW WARNINGS;",
                    "",
                    "  id            -> nomor SELECT-nya. Angka sama = satu tingkat. Angka lebih besar",
                    "                   = lebih dalam (subquery), dan yang paling besar dikerjakan duluan.",
                    "  select_type   -> SIMPLE (tanpa subquery/union), PRIMARY, SUBQUERY, DERIVED",
                    "                   (subquery di FROM), UNION, dan DEPENDENT SUBQUERY - yang terakhir",
                    "                   ini artinya subquery-nya diulang untuk SETIAP baris. Mahal.",
                    "  table         -> tabel atau aliasnya yang dibaca di langkah ini.",
                    "  type          -> CARA barisnya diambil. Kolom paling penting di seluruh keluaran.",
                    "  possible_keys -> index yang MUNGKIN dipakai. NULL = tidak ada kandidat sama sekali.",
                    "  key           -> index yang BENAR-BENAR dipakai. key NULL padahal possible_keys",
                    "                   terisi = optimizer menimbang lalu menolak semua kandidatnya.",
                    "  key_len       -> berapa BYTE dari index itu yang terpakai. Pada index gabungan,",
                    "                   angka inilah yang membuka rahasia berapa KOLOM yang sungguh",
                    "                   kepakai: nim VARCHAR(10) utf8mb4 NOT NULL = 10 x 4 + 1 = 41 byte,",
                    "                   jadi key_len 41 berarti tepat satu kolom nim yang dipakai.",
                    "  ref           -> nilai apa yang dicocokkan ke index: 'const' kalau konstanta, atau",
                    "                   nama kolom tabel lain (di sini kampus.m.nim) kalau dari JOIN.",
                    "  rows          -> PERKIRAAN jumlah baris yang akan disentuh. Tebakan, bukan hitungan.",
                    "  filtered      -> perkiraan persen baris yang lolos WHERE. rows x filtered / 100 =",
                    "                   perkiraan baris yang diteruskan ke langkah berikutnya.",
                    "  Extra         -> catatan tambahan. Sering justru di sinilah letak masalahnya.",
                    "",
                    "Tangga kolom type, dari TERBURUK ke TERBAIK:",
                    "  ALL     -> seluruh tabel dipindai baris demi baris (full table scan).",
                    "  index   -> seluruh INDEX dipindai. Lebih ramping dari ALL, tapi tetap semuanya.",
                    "  range   -> hanya sepotong rentang index yang dibaca (BETWEEN, >, <, IN, LIKE 'a%').",
                    "  ref     -> lompat langsung ke baris yang cocok lewat index yang boleh berulang.",
                    "  eq_ref  -> persis SATU baris untuk tiap baris tabel sebelumnya (JOIN ke PRIMARY KEY).",
                    "  const   -> satu baris, ditemukan sekali di awal (WHERE nim = 'M001' pada kunci utama).",
                    "",
                    "Kenapa ALL bikin waswas: pada tabel 200 baris itu justru wajar - membaca semuanya",
                    "lebih murah daripada bolak-balik ke index. Yang gawat adalah ALL pada tabel besar,",
                    "apalagi di dalam JOIN: baris tabel pertama DIKALIKAN dengan pemindaian tabel kedua.",
                    "Di contoh di atas tabel m masih ALL (belum ada index untuk jurusan) - itulah satu",
                    "hal yang jelas bisa diperbaiki, dan rows 9821 memberi tahu seberapa mahal harganya.",
                    "",
                    "Isi Extra yang wajib dikenali:",
                    "  Using where     -> baris yang sudah dibaca masih disaring lagi. Normal, bukan alarm.",
                    "  Using index     -> JEBAKAN NAMA. Ini BUKAN 'ada index yang dipakai' - itu urusan",
                    "                     kolom key. Ini artinya covering index: semua kolom yang diminta",
                    "                     sudah ada di dalam index, tabelnya tidak perlu dibuka sama",
                    "                     sekali. Ini kabar paling BAIK yang bisa muncul di sini.",
                    "  Using filesort  -> hasilnya harus diurutkan ulang karena tidak ada index yang",
                    "                     urutannya cocok dengan ORDER BY. Namanya menipu: tidak selalu",
                    "                     menyentuh disk. Obatnya index yang urutan kolomnya sama persis",
                    "                     dengan ORDER BY-nya.",
                    "  Using temporary -> MySQL menampung hasil antara di tabel sementara, biasanya gara-",
                    "                     gara GROUP BY / DISTINCT / ORDER BY yang berbeda dari GROUP BY.",
                    "                     'Using temporary; Using filesort' berbarengan pada tabel besar",
                    "                     adalah kombinasi yang paling sering bikin query merangkak.",
                ],
            },
            {
                "heading": "PostgreSQL: rencananya berbentuk pohon",
                "body": [
                    "PostgreSQL tidak menampilkan tabel, tapi POHON. Aturan bacanya cuma dua:",
                    "  1. Yang menjorok paling dalam dikerjakan paling DULU. Baca dari dalam ke luar,",
                    "     dari bawah ke atas - hasil tiap node mengalir naik ke induknya.",
                    "  2. Tanda '->' menandai sebuah anak. Node tanpa '->' di baris teratas adalah",
                    "     node terakhir yang menghasilkan baris untukmu.",
                    "",
                    "Node pembaca tabel:",
                    "  Seq Scan        -> seluruh tabel dibaca (kembarannya type ALL di MySQL).",
                    "  Index Scan      -> telusuri index, lalu ambil barisnya satu per satu dari tabel.",
                    "  Index Only Scan -> semua kolom yang diminta ada di index; tabel tidak dibuka",
                    "                     (kembarannya Using index di MySQL).",
                    "  Bitmap Heap Scan + Bitmap Index Scan -> untuk jumlah kecocokan yang kebanyakan",
                    "                     buat Index Scan tapi kesedikitan buat Seq Scan. Alamat baris",
                    "                     dikumpulkan dulu jadi bitmap, diurutkan, baru tabelnya dibaca",
                    "                     sekali jalan menurut urutan fisiknya. Ini normal, bukan cacat.",
                    "",
                    "Node penyatu dua tabel:",
                    "  Nested Loop -> untuk TIAP baris sisi luar, cari pasangannya di sisi dalam. Cepat",
                    "                 kalau sisi luar sedikit DAN sisi dalam punya index. Bencana kalau",
                    "                 sisi luarnya ternyata jutaan baris.",
                    "  Hash Join   -> sisi yang lebih kecil dijadikan tabel hash di memori, sisi besar",
                    "                 dialirkan melewatinya. Andalan untuk data banyak tanpa index cocok.",
                    "  Merge Join  -> kedua sisi diurutkan dulu (atau memang sudah urut), lalu ditelusuri",
                    "                 berbarengan seperti menyatukan dua daftar absensi.",
                    "",
                    "Angka di tiap node:",
                    "  cost=48.60..312.44 -> 48.60 biaya sampai baris PERTAMA keluar, 312.44 biaya sampai",
                    "                        baris terakhir. Satuannya bukan detik, bukan milidetik -",
                    "                        cuma satuan buatan untuk membandingkan antar rencana.",
                    "  rows=392           -> PERKIRAAN jumlah baris keluaran node ini.",
                    "  width=29           -> perkiraan lebar satu baris hasil dalam byte.",
                    "  actual time=a..b   -> waktu nyata (milidetik) sampai baris pertama dan terakhir.",
                    "  rows= di blok actual -> jumlah baris NYATA. Inilah yang dibandingkan dengan tebakan.",
                    "  loops=N            -> node ini dijalankan N kali. PENTING: actual time dan rows",
                    "                        adalah RATA-RATA PER LOOP. 'rows=1 loops=50000' berarti",
                    "                        50.000 baris dan waktunya dikali 50.000, bukan 1 baris.",
                    "",
                    "Perkiraan vs kenyataan - kebiasaan pertama yang harus kamu punya: bandingkan rows",
                    "tebakan dengan rows nyata di node yang SAMA. Di dua rencana berikut, mahasiswa",
                    "ditebak 98 baris padahal nyatanya 2455 (meleset 25 kali), dan karena tebakan itu",
                    "mengalir naik, hasil join pun meleset dari 392 ke 9820. Selisih sebesar ini hampir",
                    "selalu berarti statistik tabelnya basi, dan optimizer memilih rencana berdasarkan",
                    "angka yang salah. Obatnya satu perintah: ANALYZE nama_tabel; (di MySQL: ANALYZE",
                    "TABLE nama_tabel;, di SQLite: ANALYZE;). Jalankan itu dulu SEBELUM menambah index -",
                    "sering kali rencananya langsung berubah sendiri tanpa perlu index baru.",
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
                    "'Rows Removed by Filter: 7545' di rencana tadi adalah petunjuk paling gamblang:",
                    "7545 baris dibaca lalu langsung dibuang. Setiap baris yang dibaca untuk dibuang",
                    "adalah kandidat index. Itulah cara membaca rencana menjadi tindakan.",
                    "",
                    "Empat perbaikan yang paling sering menjawab rencana yang jelek:",
                    "",
                    "1. Index gabungan, dan URUTAN kolomnya menentukan segalanya.",
                    "   Index (angkatan, jurusan) itu seperti buku telepon yang diurutkan per kota lalu",
                    "   per nama. Mencari 'kota Bandung' bisa; 'kota Bandung, nama Budi' bisa; tapi",
                    "   'siapa pun bernama Budi di kota mana pun' TIDAK - kamu tetap harus baca semua.",
                    "   Aturannya: kolom yang dipakai dengan '=' ditaruh di depan, kolom rentang",
                    "   (>, <, BETWEEN) dan kolom ORDER BY belakangan. Bagian 3 di bawah membuktikannya.",
                    "",
                    "2. Jangan pernah membungkus kolom WHERE dengan fungsi.",
                    "   X  WHERE upper(jurusan) = 'ELEKTRO'     -- index jurusan mati total",
                    "   X  WHERE YEAR(tanggal) = 2024           -- index tanggal mati total",
                    "   Index menyimpan nilai kolom apa adanya, bukan hasil fungsinya, jadi database",
                    "   terpaksa menghitung fungsi itu untuk SETIAP baris dulu.",
                    "   V  WHERE jurusan = 'Elektro'",
                    "   V  WHERE tanggal >= '2024-01-01' AND tanggal < '2025-01-01'",
                    "   Kalau fungsinya memang tak terhindarkan, buat index atas ekspresinya:",
                    "   CREATE INDEX idx_jurusan_besar ON mahasiswa(upper(jurusan));",
                    "",
                    "3. OFFSET besar makin lambat tiap halaman - dan EXPLAIN memperlihatkannya.",
                    "   LIMIT 20 OFFSET 100000 tetap harus MEMBACA 100.020 baris lalu membuang 100.000",
                    "   yang pertama. Halaman 1 kilat, halaman 5000 merangkak, padahal query-nya sama.",
                    "   Gantinya keyset pagination: ingat nilai terakhir halaman sebelumnya.",
                    "   X  SELECT * FROM pesanan ORDER BY id LIMIT 20 OFFSET 100000;",
                    "   V  SELECT * FROM pesanan WHERE id > 100000 ORDER BY id LIMIT 20;",
                    "",
                    "4. N+1 query dari ORM - satu-satunya masalah di daftar ini yang TIDAK kelihatan",
                    "   di EXPLAIN. Kode seperti 'for m in mahasiswa: print(m.nilai)' menembakkan 1",
                    "   query untuk daftarnya, lalu 1 query lagi untuk tiap baris: 500 mahasiswa = 501",
                    "   query. Tiap query-nya sendiri sempurna di mata EXPLAIN (type const, 0.2 ms),",
                    "   yang membunuh adalah jumlahnya. Ketahuannya dari LOG query atau penghitung",
                    "   jumlah query, bukan dari rencana. Obatnya satu JOIN, satu WHERE ... IN (...),",
                    "   atau fitur eager loading di ORM-nya.",
                    "",
                    "Program di bawah menjalankan semuanya sungguhan di SQLite - 5000 baris, tanpa",
                    "angka acak. Perhatikan SCAN (baca semua) versus SEARCH (lompat lewat index).",
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
                "heading": "Frame: bagian OVER yang selama ini tidak terlihat",
                "body": [
                    "Kenapa SUM(total_penjualan) OVER (ORDER BY bulan) jadi KUMULATIF,",
                    "padahal tidak ada satu kata pun soal kumulatif di query itu? Karena",
                    "setiap OVER punya FRAME - potongan baris mana dari partisi yang ikut",
                    "dihitung - dan frame itu punya nilai bawaan yang tidak ditulis:",
                    "",
                    "  OVER (ORDER BY bulan)",
                    "  sama artinya dengan",
                    "  OVER (ORDER BY bulan",
                    "        RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)",
                    "",
                    "Bunyinya: dari baris paling awal sampai baris ini. Itulah",
                    "kumulatifnya - bukan sifat SUM, melainkan sifat frame bawaan.",
                    "",
                    "OVER TANPA ORDER BY sama sekali frame bawaannya SELURUH partisi,",
                    "jadi hasilnya total keseluruhan yang sama di setiap baris:",
                    "  SUM(total_penjualan) OVER ()                   -- total semua bulan",
                    "  SUM(total_penjualan) OVER (PARTITION BY tahun) -- total per tahun",
                    "Pasangan inilah yang dipakai menghitung porsi tanpa query kedua:",
                    "  total_penjualan * 100.0 / SUM(total_penjualan) OVER () AS persen",
                    "",
                    "Frame boleh ditulis sendiri. Bentuk yang perlu dikenali:",
                    "  ROWS BETWEEN 6 PRECEDING AND CURRENT ROW",
                    "      -> baris ini dan enam sebelumnya = rata-rata bergerak 7 hari.",
                    "  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW",
                    "      -> kumulatif, ditulis terang-terangan.",
                    "  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING",
                    "      -> seluruh partisi, walaupun ada ORDER BY.",
                    "  ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING",
                    "      -> tiga baris berdampingan: jendela yang ikut bergeser.",
                    "",
                    "ROWS lawan RANGE, dan ini beda yang sungguhan:",
                    "  ROWS  menghitung BARIS. '3 PRECEDING' = tiga baris ke atas, titik.",
                    "  RANGE menghitung NILAI kolom di ORDER BY. Semua baris yang",
                    "        nilainya SAMA dianggap satu posisi dan ikut sekaligus.",
                    "  Kalau ada nilai yang seri, RANGE memasukkan semuanya sementara",
                    "  ROWS berhenti di salah satunya. Untuk rata-rata bergerak yang",
                    "  jumlah barisnya harus pasti, pakai ROWS.",
                ]
            },
            {
                "heading": "Fungsi window lain yang sering muncul",
                "body": [
                    "NTILE(n) membelah tiap partisi jadi n kelompok sama besar lalu",
                    "memberi nomor kelompoknya. NTILE(4) = kuartil, NTILE(100) =",
                    "persentil.",
                    "  NTILE(4) OVER (ORDER BY ipk DESC) AS kuartil",
                    "  -> 1 untuk seperempat teratas, 4 untuk seperempat terbawah.",
                    "",
                    "FIRST_VALUE / LAST_VALUE / NTH_VALUE mengambil NILAI baris tertentu",
                    "di dalam jendela, bukan nomor peringkatnya.",
                    "  FIRST_VALUE(nama) OVER (PARTITION BY jurusan ORDER BY ipk DESC)",
                    "  -> nama peraih IPK tertinggi jurusan itu, ditempelkan ke SEMUA",
                    "     baris jurusan tersebut, siap dibandingkan per baris.",
                    "",
                    "JEBAKAN LAST_VALUE - dan ini jebakan frame dari bagian sebelumnya:",
                    "  LAST_VALUE(nama) OVER (PARTITION BY jurusan ORDER BY ipk DESC)",
                    "  mengembalikan nama BARIS ITU SENDIRI, bukan yang terakhir.",
                    "  Sebabnya frame bawaan berhenti di CURRENT ROW, jadi 'terakhir di",
                    "  dalam jendela' memang baris ini. Perbaikannya menulis frame penuh:",
                    "    LAST_VALUE(nama) OVER (PARTITION BY jurusan ORDER BY ipk DESC",
                    "        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)",
                    "  FIRST_VALUE aman karena frame bawaan memang dimulai dari awal.",
                    "",
                    "PERCENT_RANK() dan CUME_DIST() menjawab 'posisi relatif', bukan",
                    "nomor urut:",
                    "  PERCENT_RANK() -> (peringkat - 1) / (jumlah baris - 1). Baris",
                    "                    pertama selalu 0, baris terakhir selalu 1.",
                    "  CUME_DIST()    -> porsi baris yang nilainya <= baris ini. Selalu",
                    "                    lebih dari 0, dan tepat 1 di baris terakhir.",
                    "  Keduanya menjawab 'anak ini di 10% teratas' tanpa peduli",
                    "  pesertanya 30 orang atau 30.000.",
                    "",
                    "Klausa WINDOW: kalau OVER (...) yang sama diulang berkali-kali di",
                    "satu SELECT, beri nama sekali lalu rujuk namanya. Letaknya sesudah",
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
        "title": "18. Common Table Expression (CTE) & Recursive Query",
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
