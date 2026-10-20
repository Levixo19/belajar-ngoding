"""Kurikulum Database & Penyimpanan Data.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

DATABASE_EXERCISES = [
    {
        "title": "Latihan 1: Satu Toko, Empat Cara Menyimpan",
        "difficulty": "Mudah",
        "question": [
            "Data pembelian toko kecil ini (pelanggan, produk, harga):",
            "",
            "  PEMBELIAN = [",
            "      (\"ani\", \"kopi\", 25000),",
            "      (\"ani\", \"gula\", 14000),",
            "      (\"budi\", \"teh\", 9000),",
            "      (\"budi\", \"gula\", 14000),",
            "      (\"cici\", \"kopi\", 25000),",
            "      (\"cici\", \"susu\", 18000),",
            "      (\"dodi\", \"teh\", 9000),",
            "  ]",
            "",
            "Simpan data itu dengan empat cara:",
            "  1. tabel: tabel pembelian di sqlite3 \":memory:\"",
            "  2. dokumen: list berisi satu dict per pelanggan, misalnya",
            "     {\"nama\": \"ani\", \"belanja\": [{\"produk\": \"kopi\", \"harga\": 25000}]}",
            "  3. kunci: dict dengan kunci \"pelanggan:ani\" dan \"produk:kopi\"",
            "  4. graf: dict yang memetakan tiap simpul (pelanggan atau produk)",
            "     ke tetangganya",
            "",
            "Dari tiap cara, jawab tiga pertanyaan tentang pelanggan \"ani\":",
            "  - total: jumlah harga semua belanjaan ani",
            "  - produk: produk yang dibeli ani, terurut abjad, dipisah koma",
            "  - teman: pelanggan lain yang membeli salah satu produk yang sama",
            "    dengan ani, terurut abjad, dipisah koma",
            "",
            "Cetak satu baris per cara. Label rata kiri selebar 8 huruf, lalu",
            "\": \". Keempat jawaban harus sama.",
            "",
            "Keluaran yang diharapkan:",
            "tabel   : total=39000 produk=gula,kopi teman=budi,cici",
            "dokumen : total=39000 produk=gula,kopi teman=budi,cici",
            "kunci   : total=39000 produk=gula,kopi teman=budi,cici",
            "graf    : total=39000 produk=gula,kopi teman=budi,cici",
        ],
        "hints": [
            "Baca lagi contoh kunci-nilai di materi Memilih Jenis Database dari Pola Aksesnya: kunci-nilai cuma cepat kalau pertanyaannya memakai kuncinya, jadi simpan data dua arah.",
            "Untuk tabel, teman bisa dicari dengan JOIN tabel pembelian ke dirinya sendiri lewat kolom produk; untuk tiga cara lain, kumpulkan namanya ke set lalu buang \"ani\".",
            "Buat satu fungsi cetak(label, total, produk, teman) yang memakai f\"{label:<8}: total={total} produk={','.join(produk)} teman={','.join(teman)}\".",
        ],
        "solution": """import sqlite3

PEMBELIAN = [
    ("ani", "kopi", 25000),
    ("ani", "gula", 14000),
    ("budi", "teh", 9000),
    ("budi", "gula", 14000),
    ("cici", "kopi", 25000),
    ("cici", "susu", 18000),
    ("dodi", "teh", 9000),
]
TARGET = "ani"


def cetak(label, total, produk, teman):
    print(f"{label:<8}: total={total} produk={','.join(produk)} teman={','.join(teman)}")


# 1. Tabel relasional
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE pembelian (pelanggan TEXT, produk TEXT, harga INTEGER)")
db.executemany("INSERT INTO pembelian VALUES (?, ?, ?)", PEMBELIAN)
total = db.execute("SELECT SUM(harga) FROM pembelian WHERE pelanggan = ?",
                   (TARGET,)).fetchone()[0]
produk = [r[0] for r in db.execute(
    "SELECT DISTINCT produk FROM pembelian WHERE pelanggan = ? ORDER BY produk",
    (TARGET,))]
teman = [r[0] for r in db.execute(
    "SELECT DISTINCT b.pelanggan FROM pembelian a "
    "JOIN pembelian b ON a.produk = b.produk "
    "WHERE a.pelanggan = ? AND b.pelanggan <> ? ORDER BY b.pelanggan",
    (TARGET, TARGET))]
cetak("tabel", total, produk, teman)

# 2. Dokumen: satu dokumen per pelanggan
dokumen = []
for nama, barang, harga in PEMBELIAN:
    for d in dokumen:
        if d["nama"] == nama:
            break
    else:
        d = {"nama": nama, "belanja": []}
        dokumen.append(d)
    d["belanja"].append({"produk": barang, "harga": harga})
milik = next(d for d in dokumen if d["nama"] == TARGET)
total = sum(b["harga"] for b in milik["belanja"])
produk = sorted({b["produk"] for b in milik["belanja"]})
teman = sorted(d["nama"] for d in dokumen if d["nama"] != TARGET
               and any(b["produk"] in produk for b in d["belanja"]))
cetak("dokumen", total, produk, teman)

# 3. Kunci-nilai: disimpan dua arah, karena cuma bisa diambil per kunci
kv = {}
for nama, barang, harga in PEMBELIAN:
    kv.setdefault("pelanggan:" + nama, []).append((barang, harga))
    kv.setdefault("produk:" + barang, set()).add(nama)
belanja = kv["pelanggan:" + TARGET]
total = sum(h for _, h in belanja)
produk = sorted({b for b, _ in belanja})
teman = sorted({n for b in produk for n in kv["produk:" + b]} - {TARGET})
cetak("kunci", total, produk, teman)

# 4. Graf: simpul pelanggan dan produk, sisi "membeli" berbobot harga
graf = {}
for nama, barang, harga in PEMBELIAN:
    graf.setdefault(nama, []).append((barang, harga))
    graf.setdefault(barang, []).append((nama, harga))
total = sum(h for _, h in graf[TARGET])
produk = sorted({b for b, _ in graf[TARGET]})
teman = sorted({n for b in produk for n, _ in graf[b]} - {TARGET})
cetak("graf", total, produk, teman)
""",
    },
    {
        "title": "Latihan 2: Tabel STRICT dan Foreign Key yang Menjaga",
        "difficulty": "Mudah",
        "question": [
            "Buat dua tabel strict di sqlite3 \":memory:\" dengan foreign key",
            "yang dinyalakan:",
            "",
            "  kategori (id INTEGER PRIMARY KEY, nama TEXT NOT NULL)",
            "  produk   (id INTEGER PRIMARY KEY, nama TEXT NOT NULL,",
            "            harga INTEGER NOT NULL,",
            "            kategori_id INTEGER NOT NULL REFERENCES kategori(id))",
            "",
            "Isi kategori dengan (1, 'minuman') dan (2, 'makanan'). Lalu coba",
            "sisipkan lima produk ini, berurutan (nama, harga, kategori_id):",
            "",
            "  (\"kopi susu\", 18000, 1)",
            "  (\"roti bakar\", \"dua belas ribu\", 2)",
            "  (\"es teh\", 5000, 9)",
            "  (\"donat\", None, 2)",
            "  (\"teh tarik\", \"15000\", 1)",
            "",
            "Tangkap sqlite3.IntegrityError. Untuk tiap produk cetak",
            "\"diterima: <nama>\" atau \"ditolak : <nama> (<alasan>)\". Alasannya",
            "\"tipe salah\" kalau pesan error memuat cannot store, \"kategori",
            "tidak ada\" kalau memuat FOREIGN KEY, dan \"nilai kosong\" kalau",
            "memuat NOT NULL.",
            "",
            "Sesudah itu cetak \"---\", lalu tiap produk yang tersimpan dengan",
            "harga dan typeof(harga)-nya, urut menurut id.",
            "",
            "Keluaran yang diharapkan:",
            "diterima: kopi susu",
            "ditolak : roti bakar (tipe salah)",
            "ditolak : es teh (kategori tidak ada)",
            "ditolak : donat (nilai kosong)",
            "diterima: teh tarik",
            "---",
            "kopi susu = 18000 (integer)",
            "teh tarik = 15000 (integer)",
        ],
        "hints": [
            "Tabel strict cukup ditandai dengan kata STRICT sesudah kurung tutup CREATE TABLE, dan foreign key harus dinyalakan tepat sesudah connect.",
            "Bungkus tiap INSERT dengan try/except sqlite3.IntegrityError, lalu periksa str(e) untuk menentukan alasannya.",
            "Teh tarik diterima karena teks \"15000\" bisa diubah jadi angka tanpa kehilangan apa pun, jadi typeof-nya integer.",
        ],
        "solution": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"PRAGMA foreign_keys = ON\")\ndb.execute(\"\"\"\n    CREATE TABLE kategori (\n        id   INTEGER PRIMARY KEY,\n        nama TEXT NOT NULL\n    ) STRICT\n\"\"\")\ndb.execute(\"\"\"\n    CREATE TABLE produk (\n        id          INTEGER PRIMARY KEY,\n        nama        TEXT NOT NULL,\n        harga       INTEGER NOT NULL,\n        kategori_id INTEGER NOT NULL REFERENCES kategori(id)\n    ) STRICT\n\"\"\")\ndb.execute(\"INSERT INTO kategori VALUES (1, 'minuman'), (2, 'makanan')\")\n\nCALON = [\n    (\"kopi susu\", 18000, 1),\n    (\"roti bakar\", \"dua belas ribu\", 2),\n    (\"es teh\", 5000, 9),\n    (\"donat\", None, 2),\n    (\"teh tarik\", \"15000\", 1),\n]\n\n\ndef alasan(pesan):\n    if \"cannot store\" in pesan:\n        return \"tipe salah\"\n    if \"FOREIGN KEY\" in pesan:\n        return \"kategori tidak ada\"\n    if \"NOT NULL\" in pesan:\n        return \"nilai kosong\"\n    return pesan\n\n\nfor nama, harga, kategori in CALON:\n    try:\n        db.execute(\"INSERT INTO produk (nama, harga, kategori_id) VALUES (?, ?, ?)\",\n                   (nama, harga, kategori))\n        print(f\"diterima: {nama}\")\n    except sqlite3.IntegrityError as e:\n        print(f\"ditolak : {nama} ({alasan(str(e))})\")\n\nprint(\"---\")\nfor nama, harga, tipe in db.execute(\n        \"SELECT nama, harga, typeof(harga) FROM produk ORDER BY id\"):\n    print(f\"{nama} = {harga} ({tipe})\")\n",
    },
    {
        "title": "Latihan 3: Laporan dari Kolom JSON",
        "difficulty": "Mudah",
        "question": [
            "Lima pesanan disimpan sebagai JSON di kolom teks:",
            "",
            "  PESANAN = [",
            "      {\"kota\": \"Bandung\", \"item\": [{\"nama\": \"kopi\", \"harga\": 25000, \"jumlah\": 2},",
            "                                   {\"nama\": \"gula\", \"harga\": 14000, \"jumlah\": 1}]},",
            "      {\"kota\": \"Bogor\", \"item\": [{\"nama\": \"teh\", \"harga\": 9000, \"jumlah\": 3}]},",
            "      {\"kota\": \"Bandung\", \"item\": [{\"nama\": \"susu\", \"harga\": 18000, \"jumlah\": 1}]},",
            "      {\"kota\": \"Garut\", \"item\": [{\"nama\": \"dodol\", \"harga\": 30000, \"jumlah\": 2},",
            "                                 {\"nama\": \"teh\", \"harga\": 9000, \"jumlah\": 1}]},",
            "      {\"kota\": \"Bogor\", \"item\": [{\"nama\": \"kopi\", \"harga\": 25000, \"jumlah\": 1}]},",
            "  ]",
            "",
            "Buat tabel pesanan (id INTEGER PRIMARY KEY, data TEXT) di sqlite3",
            "\":memory:\", sisipkan tiap pesanan dengan json.dumps, lalu buat",
            "laporan per kota dengan SATU kueri SQL: banyaknya pesanan dan",
            "total belanja (harga dikali jumlah untuk tiap item).",
            "",
            "Urutkan dari total terbesar. Format tiap baris: nama kota rata",
            "kiri selebar 8 huruf, spasi, banyak pesanan, kata \"pesanan\",",
            "dua spasi, lalu \"Rp\" dan totalnya.",
            "",
            "Keluaran yang diharapkan:",
            "Bandung  2 pesanan  Rp82000",
            "Garut    1 pesanan  Rp69000",
            "Bogor    2 pesanan  Rp52000",
        ],
        "hints": [
            "Fungsi json_each memecah array item jadi baris, satu baris per item, dan isi tiap item bisa dibaca dari kolom value.",
            "Karena satu pesanan bisa punya beberapa item, hitung banyaknya pesanan dengan COUNT(DISTINCT p.id), bukan COUNT(*).",
            "Kerangka kuerinya: SELECT ... FROM pesanan AS p, json_each(p.data, '$.item') AS i GROUP BY kota ORDER BY total DESC.",
        ],
        "solution": "import json\nimport sqlite3\n\nPESANAN = [\n    {\"kota\": \"Bandung\", \"item\": [{\"nama\": \"kopi\", \"harga\": 25000, \"jumlah\": 2},\n                                 {\"nama\": \"gula\", \"harga\": 14000, \"jumlah\": 1}]},\n    {\"kota\": \"Bogor\", \"item\": [{\"nama\": \"teh\", \"harga\": 9000, \"jumlah\": 3}]},\n    {\"kota\": \"Bandung\", \"item\": [{\"nama\": \"susu\", \"harga\": 18000, \"jumlah\": 1}]},\n    {\"kota\": \"Garut\", \"item\": [{\"nama\": \"dodol\", \"harga\": 30000, \"jumlah\": 2},\n                               {\"nama\": \"teh\", \"harga\": 9000, \"jumlah\": 1}]},\n    {\"kota\": \"Bogor\", \"item\": [{\"nama\": \"kopi\", \"harga\": 25000, \"jumlah\": 1}]},\n]\n\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"CREATE TABLE pesanan (id INTEGER PRIMARY KEY, data TEXT NOT NULL)\")\ndb.executemany(\"INSERT INTO pesanan (data) VALUES (?)\",\n               [(json.dumps(p),) for p in PESANAN])\n\nLAPORAN = \"\"\"\n    SELECT json_extract(p.data, '$.kota') AS kota,\n           COUNT(DISTINCT p.id) AS pesanan,\n           SUM(json_extract(i.value, '$.harga') * json_extract(i.value, '$.jumlah')) AS total\n    FROM pesanan AS p, json_each(p.data, '$.item') AS i\n    GROUP BY kota\n    ORDER BY total DESC, kota\n\"\"\"\nfor kota, jumlah, total in db.execute(LAPORAN):\n    print(f\"{kota:<8} {jumlah} pesanan  Rp{total}\")\n",
    },
    {
        "title": "Latihan 4: Pecah Tabel Pesanan yang Berantakan",
        "difficulty": "Menengah",
        "question": [
            "Toko kue mencatat pesanan di satu tabel datar. Data pelanggan dan",
            "produk ditulis berulang di tiap baris:",
            "",
            "  DATAR = [",
            "      (101, \"2026-10-01\", \"Rina\", \"0812-1111\", \"Lapis legit\", 85000, 1),",
            "      (101, \"2026-10-01\", \"Rina\", \"0812-1111\", \"Nastar\", 60000, 2),",
            "      (102, \"2026-10-02\", \"Bayu\", \"0813-2222\", \"Nastar\", 60000, 1),",
            "      (103, \"2026-10-03\", \"Rina\", \"0812-1111\", \"Klepon\", 25000, 4),",
            "      (104, \"2026-10-03\", \"Citra\", \"0815-3333\", \"Lapis legit\", 85000, 2),",
            "      (104, \"2026-10-03\", \"Citra\", \"0815-3333\", \"Klepon\", 25000, 1),",
            "      (105, \"2026-10-04\", \"Bayu\", \"0813-2222\", \"Kastengel\", 70000, 1),",
            "  ]",
            "",
            "Kolomnya: no_pesanan, tanggal, nama_pelanggan, hp, produk, harga,",
            "jumlah. Di sqlite3 \":memory:\":",
            "  1. Buat tabel pesanan_datar dan isi dengan data itu.",
            "  2. Buat tabel pelanggan, produk, pesanan, dan detail_pesanan yang",
            "     ternormalisasi, lalu isi dari pesanan_datar dengan",
            "     INSERT ... SELECT. Nomor pesanan dipakai sebagai id pesanan.",
            "  3. Cetak jumlah baris tiap tabel, dengan urutan seperti di bawah.",
            "  4. Cetak total belanja per pelanggan (harga dikali jumlah), urut",
            "     nama, dihitung dari tabel datar lalu dari tabel-tabel baru.",
            "  5. Cetak \"sama: ya\" kalau keduanya identik.",
            "",
            "Keluaran yang diharapkan:",
            "pesanan_datar: 7 baris",
            "pelanggan: 3 baris",
            "produk: 4 baris",
            "pesanan: 5 baris",
            "detail_pesanan: 7 baris",
            "total sebelum: Bayu=130000 Citra=195000 Rina=305000",
            "total sesudah: Bayu=130000 Citra=195000 Rina=305000",
            "sama: ya",
        ],
        "hints": [
            "Tiap tabel baru menyimpan satu jenis benda: pelanggan dikenali dari nomor HP-nya, produk dari namanya, dan pesanan dari nomornya.",
            "Isi pelanggan dan produk dengan SELECT DISTINCT, lalu isi pesanan dan detail_pesanan dengan JOIN ke tabel yang baru diisi untuk mendapatkan id-nya.",
            "Contoh untuk pesanan: INSERT INTO pesanan (id, pelanggan_id, tanggal) SELECT DISTINCT d.no_pesanan, p.id, d.tanggal FROM pesanan_datar d JOIN pelanggan p ON p.hp = d.hp.",
        ],
        "solution": "import sqlite3\n\nDATAR = [\n    (101, \"2026-10-01\", \"Rina\", \"0812-1111\", \"Lapis legit\", 85000, 1),\n    (101, \"2026-10-01\", \"Rina\", \"0812-1111\", \"Nastar\", 60000, 2),\n    (102, \"2026-10-02\", \"Bayu\", \"0813-2222\", \"Nastar\", 60000, 1),\n    (103, \"2026-10-03\", \"Rina\", \"0812-1111\", \"Klepon\", 25000, 4),\n    (104, \"2026-10-03\", \"Citra\", \"0815-3333\", \"Lapis legit\", 85000, 2),\n    (104, \"2026-10-03\", \"Citra\", \"0815-3333\", \"Klepon\", 25000, 1),\n    (105, \"2026-10-04\", \"Bayu\", \"0813-2222\", \"Kastengel\", 70000, 1),\n]\n\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"PRAGMA foreign_keys = ON\")\ndb.execute(\"\"\"CREATE TABLE pesanan_datar (\n    no_pesanan INTEGER, tanggal TEXT, nama_pelanggan TEXT, hp TEXT,\n    produk TEXT, harga INTEGER, jumlah INTEGER)\"\"\")\ndb.executemany(\"INSERT INTO pesanan_datar VALUES (?, ?, ?, ?, ?, ?, ?)\", DATAR)\n\ndb.executescript(\"\"\"\nCREATE TABLE pelanggan (id INTEGER PRIMARY KEY, nama TEXT NOT NULL, hp TEXT NOT NULL UNIQUE);\nCREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT NOT NULL UNIQUE, harga INTEGER NOT NULL);\nCREATE TABLE pesanan (\n    id INTEGER PRIMARY KEY,\n    pelanggan_id INTEGER NOT NULL REFERENCES pelanggan(id),\n    tanggal TEXT NOT NULL);\nCREATE TABLE detail_pesanan (\n    pesanan_id INTEGER NOT NULL REFERENCES pesanan(id),\n    produk_id INTEGER NOT NULL REFERENCES produk(id),\n    jumlah INTEGER NOT NULL,\n    PRIMARY KEY (pesanan_id, produk_id));\n\nINSERT INTO pelanggan (nama, hp)\n    SELECT DISTINCT nama_pelanggan, hp FROM pesanan_datar ORDER BY nama_pelanggan;\nINSERT INTO produk (nama, harga)\n    SELECT DISTINCT produk, harga FROM pesanan_datar ORDER BY produk;\nINSERT INTO pesanan (id, pelanggan_id, tanggal)\n    SELECT DISTINCT d.no_pesanan, p.id, d.tanggal\n    FROM pesanan_datar d JOIN pelanggan p ON p.hp = d.hp;\nINSERT INTO detail_pesanan (pesanan_id, produk_id, jumlah)\n    SELECT d.no_pesanan, pr.id, d.jumlah\n    FROM pesanan_datar d JOIN produk pr ON pr.nama = d.produk;\n\"\"\")\n\nfor tabel in (\"pesanan_datar\", \"pelanggan\", \"produk\", \"pesanan\", \"detail_pesanan\"):\n    n = db.execute(f\"SELECT COUNT(*) FROM {tabel}\").fetchone()[0]\n    print(f\"{tabel}: {n} baris\")\n\nsebelum = db.execute(\"\"\"\n    SELECT nama_pelanggan, SUM(harga * jumlah) FROM pesanan_datar\n    GROUP BY nama_pelanggan ORDER BY nama_pelanggan\"\"\").fetchall()\nsesudah = db.execute(\"\"\"\n    SELECT pl.nama, SUM(pr.harga * d.jumlah)\n    FROM detail_pesanan d\n    JOIN pesanan ps ON ps.id = d.pesanan_id\n    JOIN pelanggan pl ON pl.id = ps.pelanggan_id\n    JOIN produk pr ON pr.id = d.produk_id\n    GROUP BY pl.nama ORDER BY pl.nama\"\"\").fetchall()\n\nprint(\"total sebelum:\", \" \".join(f\"{n}={t}\" for n, t in sebelum))\nprint(\"total sesudah:\", \" \".join(f\"{n}={t}\" for n, t in sesudah))\nprint(\"sama:\", \"ya\" if sebelum == sesudah else \"tidak\")\n",
    },
    {
        "title": "Latihan 5: Indeks Terurut dengan bisect",
        "difficulty": "Menengah",
        "question": [
            "Tabel produk punya 40 baris. Id-nya 1 sampai 40, dan harga produk",
            "ber-id i adalah ((i * 37) % 20 + 1) * 1000. Tiap harga dimiliki",
            "tepat dua produk.",
            "",
            "Bangun indeks sekunder sendiri: list berisi pasangan (harga, id)",
            "yang terurut. Lalu baca kueri rentang dari input, satu per baris,",
            "berbentuk \"bawah atas\" (keduanya termasuk). Untuk tiap kueri:",
            "  - Cari baris yang harganya di rentang itu memakai",
            "    bisect.bisect_left dan bisect.bisect_right pada indeks.",
            "  - Cetak \"harga bawah..atas: id ...\" dengan id dipisah koma",
            "    menurut urutan indeks (harga lalu id), atau \"-\" kalau kosong.",
            "  - Cetak biayanya. Tanpa indeks, semua 40 baris diperiksa. Dengan",
            "    indeks, biayanya dua pencarian biner (masing-masing",
            "    len(indeks).bit_length() langkah, yaitu 6 untuk 40 entri)",
            "    ditambah banyaknya entri yang dibaca.",
            "",
            "Untuk input 5000 7000, keluarannya:",
            "harga 5000..7000: id 12,32,5,25,18,38",
            "  tanpa indeks 40 langkah, dengan indeks 12 + 6 = 18 langkah",
            "harga 19500..25000: id 7,27",
            "  tanpa indeks 40 langkah, dengan indeks 12 + 2 = 14 langkah",
            "harga 15500..15900: id -",
            "  tanpa indeks 40 langkah, dengan indeks 12 + 0 = 12 langkah",
            "",
            "Coba juga rentang 1000 20000. Indeksnya justru lebih mahal dari",
            "scan, persis alasan planner memilih scan untuk kueri yang nggak",
            "selektif.",
        ],
        "stdin_list": [
            """5000 7000
19500 25000
15500 15900
""",
            """1000 20000
12000 14000
""",
        ],
        "hints": [
            "Indeks yang terurut memungkinkan kamu melompat ke posisi awal rentang tanpa memeriksa semua baris, lalu berhenti begitu harga melewati batas atas.",
            "Karena isi indeks berupa pasangan, cari batas bawah dengan pasangan (bawah, 0) dan batas atas dengan pasangan (atas, float(\"inf\")).",
            "Hasilnya potongan indeks[awal:akhir]; biayanya 2 * len(indeks).bit_length() + len(potongan).",
        ],
        "solution": "import bisect\nimport sys\n\n# Tabel produk: id 1..40, harganya berulang supaya ada nilai kembar\nTABEL = {i: ((i * 37) % 20 + 1) * 1000 for i in range(1, 41)}\n\n# Indeks sekunder: daftar (harga, id) yang terurut\nindeks = sorted((harga, i) for i, harga in TABEL.items())\nlangkah_biner = len(indeks).bit_length()      # 40 entri -> 6 langkah\n\nfor baris in sys.stdin.read().split(\"\\n\"):\n    if not baris.strip():\n        continue\n    bawah, atas = map(int, baris.split())\n\n    # Tanpa indeks: periksa semua baris tabel\n    tanpa = sorted((h, i) for i, h in TABEL.items() if bawah <= h <= atas)\n\n    # Dengan indeks: lompat ke batas bawah, berhenti di batas atas\n    awal = bisect.bisect_left(indeks, (bawah, 0))\n    akhir = bisect.bisect_right(indeks, (atas, float(\"inf\")))\n    dengan = indeks[awal:akhir]\n\n    assert tanpa == dengan\n    ids = \",\".join(str(i) for _, i in dengan) or \"-\"\n    biaya = 2 * langkah_biner + len(dengan)\n    print(f\"harga {bawah}..{atas}: id {ids}\")\n    print(f\"  tanpa indeks {len(TABEL)} langkah, dengan indeks \"\n          f\"{2 * langkah_biner} + {len(dengan)} = {biaya} langkah\")\n",
    },
    {
        "title": "Latihan 6: Lost Update dan Kolom Versi",
        "difficulty": "Menengah",
        "question": [
            "Simulasikan dua kasir yang menyetor ke akun yang sama, memakai",
            "satu koneksi sqlite3 \":memory:\" dengan isolation_level=None.",
            "Langkah kedua kasir diatur berurutan dari satu skrip.",
            "",
            "Tabel: akun (id INTEGER PRIMARY KEY, saldo INTEGER, versi INTEGER),",
            "berisi satu baris (1, 100000, 1). Kasir A menyetor 50000, kasir B",
            "menyetor 20000.",
            "",
            "Bagian pertama, tanpa kolom versi: A membaca saldo, B membaca",
            "saldo, A menulis saldonya + 50000, B menulis saldonya + 20000.",
            "",
            "Bagian kedua: kembalikan baris jadi (1, 100000, 1). A dan B",
            "membaca saldo beserta versi. Tiap tulisan memakai",
            "UPDATE ... SET saldo = ?, versi = versi + 1 WHERE id = 1 AND",
            "versi = ?, lalu memeriksa rowcount. Kalau 0, kasir itu membaca",
            "ulang dan mencoba lagi. A menulis duluan.",
            "",
            "Keluaran yang diharapkan:",
            "--- tanpa kolom versi ---",
            "A baca saldo 100000",
            "B baca saldo 100000",
            "A tulis 150000",
            "B tulis 120000",
            "saldo akhir 120000 (setoran A hilang)",
            "--- dengan kolom versi ---",
            "A baca saldo 100000 versi 1",
            "B baca saldo 100000 versi 1",
            "A tulis 150000: berhasil (rowcount 1)",
            "B tulis 120000: gagal (rowcount 0), baca ulang",
            "B baca saldo 150000 versi 2",
            "B tulis 170000: berhasil (rowcount 1)",
            "saldo akhir 170000",
        ],
        "hints": [
            "Lost update terjadi karena B menghitung dari angka yang sudah basi saat A menulis lebih dulu.",
            "Kolom versi berfungsi sebagai syarat: UPDATE cuma mengenai baris kalau versinya masih sama dengan yang dibaca, dan kursor.rowcount memberi tahu berapa baris yang kena.",
            "Buat fungsi tulis_bersyarat(nama, saldo_baru, versi_lama) yang mengembalikan True kalau rowcount == 1, lalu ulangi baca dan tulis untuk B dalam while not tulis_bersyarat(...).",
        ],
        "solution": """import sqlite3

db = sqlite3.connect(":memory:", isolation_level=None)
db.execute("CREATE TABLE akun (id INTEGER PRIMARY KEY, saldo INTEGER, versi INTEGER)")
db.execute("INSERT INTO akun VALUES (1, 100000, 1)")


def baca():
    return db.execute("SELECT saldo, versi FROM akun WHERE id = 1").fetchone()


print("--- tanpa kolom versi ---")
saldo_a, _ = baca()
print("A baca saldo", saldo_a)
saldo_b, _ = baca()
print("B baca saldo", saldo_b)
db.execute("UPDATE akun SET saldo = ? WHERE id = 1", (saldo_a + 50000,))
print("A tulis", saldo_a + 50000)
db.execute("UPDATE akun SET saldo = ? WHERE id = 1", (saldo_b + 20000,))
print("B tulis", saldo_b + 20000)
print("saldo akhir", baca()[0], "(setoran A hilang)")

print("--- dengan kolom versi ---")
db.execute("UPDATE akun SET saldo = 100000, versi = 1 WHERE id = 1")


def tulis_bersyarat(nama, saldo_baru, versi_lama):
    kursor = db.execute(
        "UPDATE akun SET saldo = ?, versi = versi + 1 WHERE id = 1 AND versi = ?",
        (saldo_baru, versi_lama))
    if kursor.rowcount == 1:
        print(f"{nama} tulis {saldo_baru}: berhasil (rowcount 1)")
        return True
    print(f"{nama} tulis {saldo_baru}: gagal (rowcount 0), baca ulang")
    return False


saldo_a, versi_a = baca()
print("A baca saldo", saldo_a, "versi", versi_a)
saldo_b, versi_b = baca()
print("B baca saldo", saldo_b, "versi", versi_b)
tulis_bersyarat("A", saldo_a + 50000, versi_a)
while not tulis_bersyarat("B", saldo_b + 20000, versi_b):
    saldo_b, versi_b = baca()
    print("B baca saldo", saldo_b, "versi", versi_b)
print("saldo akhir", baca()[0])
""",
    },
    {
        "title": "Latihan 7: Hitung Kueri dan Usir N+1",
        "difficulty": "Menengah",
        "question": [
            "Siapkan database sqlite3 \":memory:\" berisi dua tabel:",
            "",
            "  penulis: (1, 'Ayu'), (2, 'Bima'), (3, 'Citra'), (4, 'Dewi')",
            "  buku (judul, penulis_id):",
            "    ('Senja di Pelabuhan', 1), ('Hujan di Bulan Juli', 1),",
            "    ('Kode Pertama', 2),",
            "    ('Laut Tanpa Nama', 3), ('Arah Pulang', 3), ('Bintang Kecil', 3)",
            "",
            "Pasang db.set_trace_callback untuk mencatat tiap kueri. Lalu buat",
            "tiga fungsi yang menghasilkan daftar (nama_penulis, [judul terurut])",
            "untuk semua penulis, urut id:",
            "  - naif: satu kueri untuk penulis, lalu satu kueri per penulis",
            "  - JOIN: satu kueri LEFT JOIN",
            "  - IN: satu kueri penulis, lalu satu kueri buku WHERE penulis_id",
            "    IN (...)",
            "",
            "Kosongkan catatan kueri sebelum tiap fungsi dijalankan. Cetak",
            "jumlah kueri tiap fungsi (label rata kiri selebar 4), apakah",
            "hasil ketiganya sama, lalu isi hasilnya. Penulis tanpa buku ditulis",
            "\"(belum ada buku)\".",
            "",
            "Keluaran yang diharapkan:",
            "naif: 5 kueri",
            "JOIN: 1 kueri",
            "IN  : 2 kueri",
            "hasil sama: ya",
            "Ayu: Hujan di Bulan Juli, Senja di Pelabuhan",
            "Bima: Kode Pertama",
            "Citra: Arah Pulang, Bintang Kecil, Laut Tanpa Nama",
            "Dewi: (belum ada buku)",
        ],
        "hints": [
            "Jumlah kueri versi naif selalu satu ditambah banyaknya penulis, berapa pun jumlah bukunya.",
            "Di versi JOIN pakai LEFT JOIN supaya Dewi yang belum punya buku tetap muncul, dan lewati judul yang bernilai None.",
            "Di versi IN, buat tanda tanya sebanyak jumlah penulis dengan \",\".join(\"?\" * len(penulis)) lalu kelompokkan judul ke dict berkunci penulis_id.",
        ],
        "solution": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.executescript(\"\"\"\nCREATE TABLE penulis (id INTEGER PRIMARY KEY, nama TEXT NOT NULL);\nCREATE TABLE buku (\n    id INTEGER PRIMARY KEY,\n    judul TEXT NOT NULL,\n    penulis_id INTEGER NOT NULL REFERENCES penulis(id)\n);\nINSERT INTO penulis VALUES (1, 'Ayu'), (2, 'Bima'), (3, 'Citra'), (4, 'Dewi');\nINSERT INTO buku (judul, penulis_id) VALUES\n    ('Senja di Pelabuhan', 1), ('Hujan di Bulan Juli', 1),\n    ('Kode Pertama', 2),\n    ('Laut Tanpa Nama', 3), ('Arah Pulang', 3), ('Bintang Kecil', 3);\n\"\"\")\n\nkueri = []\ndb.set_trace_callback(kueri.append)\n\n\ndef naif():\n    hasil = []\n    for pid, nama in db.execute(\"SELECT id, nama FROM penulis ORDER BY id\").fetchall():\n        judul = [j for (j,) in db.execute(\n            \"SELECT judul FROM buku WHERE penulis_id = ? ORDER BY judul\", (pid,))]\n        hasil.append((nama, judul))\n    return hasil\n\n\ndef pakai_join():\n    hasil, posisi = [], {}\n    for pid, nama, judul in db.execute(\"\"\"\n            SELECT p.id, p.nama, b.judul FROM penulis p\n            LEFT JOIN buku b ON b.penulis_id = p.id\n            ORDER BY p.id, b.judul\"\"\"):\n        if pid not in posisi:\n            posisi[pid] = len(hasil)\n            hasil.append((nama, []))\n        if judul is not None:\n            hasil[posisi[pid]][1].append(judul)\n    return hasil\n\n\ndef pakai_in():\n    penulis = db.execute(\"SELECT id, nama FROM penulis ORDER BY id\").fetchall()\n    tanda = \",\".join(\"?\" * len(penulis))\n    per_penulis = {pid: [] for pid, _ in penulis}\n    for pid, judul in db.execute(\n            f\"SELECT penulis_id, judul FROM buku WHERE penulis_id IN ({tanda}) ORDER BY judul\",\n            [pid for pid, _ in penulis]):\n        per_penulis[pid].append(judul)\n    return [(nama, per_penulis[pid]) for pid, nama in penulis]\n\n\nhasil = {}\nfor nama, fungsi in ((\"naif\", naif), (\"JOIN\", pakai_join), (\"IN\", pakai_in)):\n    kueri.clear()\n    hasil[nama] = fungsi()\n    print(f\"{nama:<4}: {len(kueri)} kueri\")\n\nprint(\"hasil sama:\", \"ya\" if hasil[\"naif\"] == hasil[\"JOIN\"] == hasil[\"IN\"] else \"tidak\")\nfor nama, judul in hasil[\"JOIN\"]:\n    print(f\"{nama}: {', '.join(judul) or '(belum ada buku)'}\")\n",
    },
    {
        "title": "Latihan 8: Aturan Akses Per Baris ala RLS",
        "difficulty": "Menengah",
        "question": [
            "SQLite nggak punya Row Level Security, tapi gagasannya bisa ditiru",
            "di kode: semua akses data lewat fungsi yang selalu menambahkan",
            "syarat pemilik, persis seperti policy.",
            "",
            "Buat tabel catatan (id INTEGER PRIMARY KEY, pemilik TEXT, isi TEXT)",
            "di sqlite3 \":memory:\" berisi, berurutan:",
            "  ('ani', 'beli kuota'), ('budi', 'servis motor'),",
            "  ('ani', 'setor laporan PKL'), ('citra', 'bayar kos')",
            "",
            "Tulis fungsi syarat(pengguna) yang mengembalikan potongan WHERE",
            "beserta nilainya: \"1 = 1\" untuk admin, \"pemilik = ?\" untuk yang",
            "lain. Fungsi lihat(pengguna) dan ubah(pengguna, id, isi_baru) wajib",
            "memakainya, dan ubah() mengembalikan rowcount.",
            "",
            "Cetak apa yang dilihat ani, budi, dan admin, lalu buktikan ani",
            "nggak bisa mengubah catatan #2 milik budi, sedangkan budi bisa.",
            "",
            "Keluaran yang diharapkan:",
            "ani: 2 catatan -> #1 beli kuota, #3 setor laporan PKL",
            "budi: 1 catatan -> #2 servis motor",
            "admin: 4 catatan -> #1 beli kuota, #2 servis motor, #3 setor laporan PKL, #4 bayar kos",
            "ani ubah #2 milik budi: 0 baris berubah",
            "budi ubah #2 miliknya : 1 baris berubah",
            "isi #2 sekarang       : servis motor + ganti oli",
        ],
        "hints": [
            "Seperti policy RLS, syarat pemilik harus ditambahkan di satu tempat saja, sehingga fungsi baca dan ubah nggak mungkin lupa menulisnya.",
            "Potongan WHERE boleh disusun dengan f-string karena isinya tetap, tapi nama pengguna tetap dikirim lewat placeholder ?.",
            "UPDATE ubah() berbentuk \"UPDATE catatan SET isi = ? WHERE id = ? AND \" + where, dengan nilai (isi_baru, id_catatan) + nilai_syarat.",
        ],
        "solution": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\ndb.execute(\"CREATE TABLE catatan (id INTEGER PRIMARY KEY, pemilik TEXT NOT NULL, isi TEXT NOT NULL)\")\ndb.executemany(\"INSERT INTO catatan (pemilik, isi) VALUES (?, ?)\", [\n    (\"ani\", \"beli kuota\"),\n    (\"budi\", \"servis motor\"),\n    (\"ani\", \"setor laporan PKL\"),\n    (\"citra\", \"bayar kos\"),\n])\n\n\ndef syarat(pengguna):\n    \"\"\"Meniru policy RLS: admin melihat semua, selain itu cuma miliknya.\"\"\"\n    if pengguna == \"admin\":\n        return \"1 = 1\", ()\n    return \"pemilik = ?\", (pengguna,)\n\n\ndef lihat(pengguna):\n    where, nilai = syarat(pengguna)\n    return db.execute(f\"SELECT id, isi FROM catatan WHERE {where} ORDER BY id\", nilai).fetchall()\n\n\ndef ubah(pengguna, id_catatan, isi_baru):\n    where, nilai = syarat(pengguna)\n    kursor = db.execute(f\"UPDATE catatan SET isi = ? WHERE id = ? AND {where}\",\n                        (isi_baru, id_catatan) + nilai)\n    return kursor.rowcount\n\n\nfor pengguna in (\"ani\", \"budi\", \"admin\"):\n    baris = lihat(pengguna)\n    print(f\"{pengguna}: {len(baris)} catatan ->\", \", \".join(f\"#{i} {isi}\" for i, isi in baris))\n\nprint(\"ani ubah #2 milik budi:\", ubah(\"ani\", 2, \"dibajak\"), \"baris berubah\")\nprint(\"budi ubah #2 miliknya :\", ubah(\"budi\", 2, \"servis motor + ganti oli\"), \"baris berubah\")\nprint(\"isi #2 sekarang       :\", db.execute(\"SELECT isi FROM catatan WHERE id = 2\").fetchone()[0])\n",
    },
    {
        "title": "Latihan 9: Cari Pengemudi Terdekat dengan Haversine",
        "difficulty": "Menengah",
        "question": [
            "Baris pertama input berisi lintang, bujur, dan radius (km) titik",
            "penumpang. Baris-baris berikutnya berisi nama, lintang, dan bujur",
            "pengemudi, dipisah spasi.",
            "",
            "Tiru cara kerja indeks spasial dalam dua tahap:",
            "  1. Saring dulu dengan kotak pembatas. Lebar kotak ke utara dan",
            "     selatan radius / 111.32 derajat, ke barat dan timur",
            "     radius / (111.32 * cos(lintang penumpang)) derajat.",
            "  2. Untuk yang lolos kotak saja, hitung jarak haversine (jari-jari",
            "     bumi 6371 km) dan buang yang lebih jauh dari radius.",
            "",
            "Cetak \"lolos kotak dan radius: X dari Y pengemudi\", lalu paling",
            "banyak tiga pengemudi terdekat dengan jarak dibulatkan satu angka",
            "di belakang koma. Kalau nggak ada, cetak \"tidak ada pengemudi",
            "dalam radius\".",
            "",
            "Untuk input -6.9025 107.6191 3, keluarannya:",
            "lolos kotak dan radius: 4 dari 6 pengemudi",
            "Asep 0.1 km",
            "Yayan 1.5 km",
            "Dedi 1.7 km",
        ],
        "stdin_list": [
            """-6.9025 107.6191 3
Asep -6.9020 107.6186
Dedi -6.9147 107.6098
Euis -6.8915 107.6350
Ujang -6.8720 107.5420
Wawan -6.9300 107.6200
Yayan -6.9100 107.6300
""",
            """-6.2000 106.8166 2
Rudi -6.2100 106.8200
Sari -6.1750 106.8270
Tono -6.2050 106.8100
""",
            """-7.2575 112.7521 1
Bagus -7.2900 112.7300
""",
        ],
        "hints": [
            "Kotak pembatas murah dihitung karena cuma membandingkan selisih derajat, sedangkan haversine butuh sinus dan kosinus, jadi hitung haversine hanya untuk yang lolos kotak.",
            "Satu derajat bujur makin sempit menjauhi khatulistiwa, karena itu lebar kotak ke timur-barat dibagi math.cos(math.radians(lintang)).",
            "Kumpulkan pasangan (jarak, nama), urutkan, lalu cetak tiga pertama dengan f\"{nama} {jarak:.1f} km\".",
        ],
        "solution": "import math\nimport sys\n\n\ndef haversine_km(lat1, lon1, lat2, lon2):\n    r = 6371.0\n    p1, p2 = math.radians(lat1), math.radians(lat2)\n    dlat = math.radians(lat2 - lat1)\n    dlon = math.radians(lon2 - lon1)\n    a = math.sin(dlat / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlon / 2) ** 2\n    return 2 * r * math.asin(math.sqrt(a))\n\n\nbaris = [b.split() for b in sys.stdin.read().split(\"\\n\") if b.strip()]\nlat0, lon0, radius = float(baris[0][0]), float(baris[0][1]), float(baris[0][2])\n\n# Kotak pembatas: 1 derajat lintang kira-kira 111,32 km,\n# 1 derajat bujur menyusut mengikuti cos(lintang)\ndlat = radius / 111.32\ndlon = radius / (111.32 * math.cos(math.radians(lat0)))\n\ncalon, total = [], 0\nfor nama, lat, lon in baris[1:]:\n    total += 1\n    lat, lon = float(lat), float(lon)\n    if abs(lat - lat0) <= dlat and abs(lon - lon0) <= dlon:\n        jarak = haversine_km(lat0, lon0, lat, lon)\n        if jarak <= radius:\n            calon.append((jarak, nama))\n\nprint(f\"lolos kotak dan radius: {len(calon)} dari {total} pengemudi\")\ncalon.sort()\nfor jarak, nama in calon[:3]:\n    print(f\"{nama} {jarak:.1f} km\")\nif not calon:\n    print(\"tidak ada pengemudi dalam radius\")\n",
    },
    {
        "title": "Latihan 10: Penerjemah Logat MySQL ke SQLite",
        "difficulty": "Menengah",
        "question": [
            "Kamu diberi skrip MySQL kecil lewat stdin. Terjemahkan tiap",
            "perintahnya ke logat SQLite, jalankan di database sqlite3",
            "':memory:', lalu cetak hasilnya.",
            "",
            "Pecah skrip menjadi perintah-perintah dengan memotong di setiap",
            "titik koma (data di soal ini nggak memuat titik koma di dalam",
            "teks). Lewati potongan yang kosong. Aturan terjemahannya:",
            "  1. Backtick ` diganti tanda kutip ganda \".",
            "  2. INT AUTO_INCREMENT PRIMARY KEY (boleh ada NOT NULL di antara",
            "     INT dan AUTO_INCREMENT) diganti INTEGER PRIMARY KEY",
            "     AUTOINCREMENT.",
            "  3. Opsi tabel ENGINE=..., DEFAULT CHARSET=..., dan COLLATE=...",
            "     dibuang beserta spasi di depannya.",
            "  4. LIMIT a, b diganti LIMIT b OFFSET a.",
            "  5. Rapikan spasi: semua deretan spasi dan baris baru jadi satu",
            "     spasi, lalu buang spasi tepat sesudah ( dan tepat sebelum ).",
            "",
            "Aturan 2 penting. SQLite ternyata menerima INT AUTO_INCREMENT",
            "PRIMARY KEY tanpa error, tapi kolom id-nya tetap kosong (NULL)",
            "untuk setiap baris baru.",
            "",
            "Untuk tiap perintah, cetak \"> \" diikuti SQL hasil terjemahan.",
            "Kalau perintahnya SELECT, cetak juga setiap baris hasil dengan",
            "awalan dua spasi dan nilai dipisah \" | \".",
            "",
            "Contoh masukan:",
            "  CREATE TABLE `produk` (",
            "    `id` INT AUTO_INCREMENT PRIMARY KEY,",
            "    `nama` VARCHAR(50) NOT NULL,",
            "    `harga` INT NOT NULL",
            "  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;",
            "  INSERT INTO `produk` (`nama`, `harga`) VALUES ('Kopi Gayo', 85000);",
            "  ... (tiga INSERT lagi untuk Teh Tubruk, Gula Aren, Susu Sapi)",
            "  SELECT `id`, `nama`, `harga` FROM `produk`",
            "    ORDER BY `harga` DESC LIMIT 1, 2;",
            "",
            "Keluaran yang diharapkan:",
            "> CREATE TABLE \"produk\" (\"id\" INTEGER PRIMARY KEY AUTOINCREMENT, \"nama\" VARCHAR(50) NOT NULL, \"harga\" INT NOT NULL)",
            "> INSERT INTO \"produk\" (\"nama\", \"harga\") VALUES ('Kopi Gayo', 85000)",
            "> INSERT INTO \"produk\" (\"nama\", \"harga\") VALUES ('Teh Tubruk', 15000)",
            "> INSERT INTO \"produk\" (\"nama\", \"harga\") VALUES ('Gula Aren', 30000)",
            "> INSERT INTO \"produk\" (\"nama\", \"harga\") VALUES ('Susu Sapi', 22000)",
            "> SELECT \"id\", \"nama\", \"harga\" FROM \"produk\" ORDER BY \"harga\" DESC LIMIT 2 OFFSET 1",
            "  3 | Gula Aren | 30000",
            "  4 | Susu Sapi | 22000",
        ],
        "hints": [
            "Kerjakan satu aturan sekali jalan, dari yang paling sederhana (backtick) sampai yang paling rumit (LIMIT), lalu cetak hasil tiap aturan untuk memeriksanya.",
            "Modul re dengan flags=re.I memudahkan aturan 2 sampai 4, dan kelompok tangkapan seperti (\\d+) bisa dipakai ulang di pengganti sebagai \\1 dan \\2.",
            "Untuk merapikan spasi, \" \".join(sql.split()) mengubah semua deretan spasi dan baris baru jadi satu spasi, lalu replace(\"( \", \"(\") dan replace(\" )\", \")\") membereskan kurungnya.",
            "Cek awal perintah dengan sql.upper().startswith(\"SELECT\"), lalu cetak tiap baris dari kursor.fetchall() dengan \" | \".join(str(nilai) for nilai in baris).",
        ],
        "solution": "import re\nimport sqlite3\nimport sys\n\n\ndef terjemahkan(sql):\n    sql = sql.replace(\"`\", '\"')\n    sql = re.sub(r\"\\bINT(EGER)?\\s+(NOT\\s+NULL\\s+)?AUTO_INCREMENT\\s+PRIMARY\\s+KEY\\b\",\n                 \"INTEGER PRIMARY KEY AUTOINCREMENT\", sql, flags=re.I)\n    sql = re.sub(r\"\\s*\\b(DEFAULT\\s+)?(ENGINE|CHARSET|COLLATE)\\s*=\\s*\\w+\", \"\",\n                 sql, flags=re.I)\n    sql = re.sub(r\"\\bLIMIT\\s+(\\d+)\\s*,\\s*(\\d+)\", r\"LIMIT \\2 OFFSET \\1\",\n                 sql, flags=re.I)\n    sql = \" \".join(sql.split())\n    return sql.replace(\"( \", \"(\").replace(\" )\", \")\")\n\n\nkoneksi = sqlite3.connect(\":memory:\")\nfor mentah in sys.stdin.read().split(\";\"):\n    if not mentah.strip():\n        continue\n    sql = terjemahkan(mentah)\n    print(\"> \" + sql)\n    kursor = koneksi.execute(sql)\n    if sql.upper().startswith(\"SELECT\"):\n        for baris in kursor.fetchall():\n            print(\"  \" + \" | \".join(str(nilai) for nilai in baris))\n",
        "stdin_list": [
            """CREATE TABLE `produk` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `nama` VARCHAR(50) NOT NULL,
  `harga` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO `produk` (`nama`, `harga`) VALUES ('Kopi Gayo', 85000);
INSERT INTO `produk` (`nama`, `harga`) VALUES ('Teh Tubruk', 15000);
INSERT INTO `produk` (`nama`, `harga`) VALUES ('Gula Aren', 30000);
INSERT INTO `produk` (`nama`, `harga`) VALUES ('Susu Sapi', 22000);
SELECT `id`, `nama`, `harga` FROM `produk` ORDER BY `harga` DESC LIMIT 1, 2;
""",
            """CREATE TABLE `siswa` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nama` VARCHAR(40) NOT NULL,
  `kelas` VARCHAR(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `siswa` (`nama`, `kelas`) VALUES ('Andi', 'X-1'), ('Budi', 'X-2');
INSERT INTO `siswa` (`nama`, `kelas`) VALUES ('Citra', 'X-1'), ('Dewi', 'X-1');
SELECT `kelas`, COUNT(*) FROM `siswa` GROUP BY `kelas` ORDER BY `kelas`;
SELECT `id`, `nama` FROM `siswa` WHERE `kelas` = 'X-1' ORDER BY `id` LIMIT 0, 2;
""",
        ],
    },
    {
        "title": "Latihan 11: Cache LRU dengan TTL dan Jam Buatan",
        "difficulty": "Menengah",
        "question": [
            "Buat cache mini yang membaca perintah dari stdin, satu perintah",
            "per baris:",
            "",
            "  KAPASITAS n       jumlah kunci maksimum (bawaan 2)",
            "  WAKTU t           setel jam buatan ke detik t (bawaan 0)",
            "  SET k v [ttl]     simpan v di kunci k, ttl opsional dalam detik",
            "  GET k             cetak nilai k, atau (kosong)",
            "",
            "Aturannya:",
            "  - Kunci dengan ttl kedaluwarsa saat jam >= waktu SET + ttl.",
            "    Tanpa ttl, kunci nggak pernah kedaluwarsa.",
            "  - GET pada kunci yang kedaluwarsa menghapus kunci itu, mencetak",
            "    (kosong), dan dihitung miss. Kunci kedaluwarsa tetap memakan",
            "    tempat sampai di-GET atau diusir.",
            "  - GET yang berhasil dihitung hit dan menjadikan kunci itu paling",
            "    baru dipakai.",
            "  - SET ke kunci yang sudah ada memperbarui nilai dan ttl-nya, dan",
            "    menjadikannya paling baru dipakai, tanpa mengusir apa pun.",
            "  - SET kunci baru saat cache sudah penuh mengusir kunci yang",
            "    paling lama nggak dipakai, lalu mencetak usir <kunci>.",
            "  - Di akhir, cetak hit=<jumlah> miss=<jumlah>.",
            "",
            "Contoh masukan:",
            "  KAPASITAS 2",
            "  WAKTU 0",
            "  SET kota Bandung",
            "  SET nama Sari 30",
            "  GET kota",
            "  SET poin 120",
            "  GET nama",
            "  GET kota",
            "  WAKTU 40",
            "  GET poin",
            "",
            "Keluaran yang diharapkan:",
            "Bandung",
            "usir nama",
            "(kosong)",
            "Bandung",
            "120",
            "hit=3 miss=1",
        ],
        "hints": [
            "Cache LRU butuh dua hal sekaligus: mencari kunci dengan cepat dan tahu kunci mana yang paling lama nggak dipakai.",
            "collections.OrderedDict memberi keduanya: move_to_end(k) menandai k paling baru dipakai, dan popitem(last=False) mengeluarkan yang paling lama.",
            "Simpan nilai sebagai pasangan (nilai, detik_kedaluwarsa), dengan None untuk kunci tanpa ttl, lalu saat GET periksa jam >= detik_kedaluwarsa sebelum memakai nilainya.",
        ],
        "solution": """import sys
from collections import OrderedDict

cache = OrderedDict()   # kunci -> (nilai, detik kedaluwarsa atau None)
kapasitas = 2
jam = 0
hit = miss = 0

for baris in sys.stdin:
    bagian = baris.split()
    if not bagian:
        continue
    perintah = bagian[0].upper()
    if perintah == "KAPASITAS":
        kapasitas = int(bagian[1])
    elif perintah == "WAKTU":
        jam = int(bagian[1])
    elif perintah == "SET":
        kunci, nilai = bagian[1], bagian[2]
        habis = jam + int(bagian[3]) if len(bagian) > 3 else None
        if kunci in cache:
            cache.move_to_end(kunci)
        elif len(cache) >= kapasitas:
            lama, _ = cache.popitem(last=False)
            print("usir", lama)
        cache[kunci] = (nilai, habis)
    elif perintah == "GET":
        kunci = bagian[1]
        data = cache.get(kunci)
        if data is not None and data[1] is not None and jam >= data[1]:
            del cache[kunci]
            data = None
        if data is None:
            miss += 1
            print("(kosong)")
        else:
            hit += 1
            cache.move_to_end(kunci)
            print(data[0])
print(f"hit={hit} miss={miss}")
""",
        "stdin_list": [
            """KAPASITAS 2
WAKTU 0
SET kota Bandung
SET nama Sari 30
GET kota
SET poin 120
GET nama
GET kota
WAKTU 40
GET poin
""",
            """KAPASITAS 3
WAKTU 100
SET token abc 60
SET tema gelap
WAKTU 159
GET token
WAKTU 160
GET token
GET tema
SET token xyz 10
WAKTU 165
GET token
WAKTU 170
GET token
""",
            """KAPASITAS 2
SET a 1
SET b 2
SET a 10
SET c 3
GET b
GET a
GET c
WAKTU 5
SET d 4 2
WAKTU 7
GET d
GET a
""",
        ],
    },
    {
        "title": "Latihan 12: Pembatas Laju Jendela Geser",
        "difficulty": "Lanjut",
        "question": [
            "Buat pembatas laju dengan sliding window log. Baris pertama stdin",
            "berisi dua angka, N dan W: tiap pengguna boleh paling banyak N",
            "permintaan dalam W detik terakhir.",
            "",
            "Baris berikutnya berisi permintaan berbentuk \"waktu pengguna\",",
            "dengan waktu berupa detik bulat yang nggak pernah mundur.",
            "",
            "Untuk tiap permintaan pada detik t:",
            "  - Abaikan catatan pengguna itu yang waktunya <= t - W.",
            "  - Kalau sisa catatannya kurang dari N, izinkan dan catat t.",
            "  - Kalau sudah N, tolak. Permintaan yang ditolak nggak dicatat.",
            "",
            "Cetak \"waktu pengguna IZIN\" atau \"waktu pengguna TOLAK\" untuk",
            "tiap permintaan, sesuai urutan masukan. Tiap pengguna dihitung",
            "terpisah.",
            "",
            "Untuk input 3 10, keluarannya:",
            "1 sari IZIN",
            "2 sari IZIN",
            "3 budi IZIN",
            "4 sari IZIN",
            "5 sari TOLAK",
            "11 sari IZIN",
            "12 sari IZIN",
            "14 sari IZIN",
            "15 budi IZIN",
            "",
            "(Masukan lengkap untuk contoh itu: baris \"3 10\", lalu 1 sari,",
            "2 sari, 3 budi, 4 sari, 5 sari, 11 sari, 12 sari, 14 sari, dan",
            "15 budi, masing-masing satu baris.)",
        ],
        "hints": [
            "Fixed window menghitung dari nol di awal tiap menit, sedangkan jendela geser selalu melihat W detik ke belakang dari permintaan yang sedang diperiksa.",
            "Simpan waktu permintaan yang diizinkan per pengguna di collections.deque, karena catatan paling tua selalu ada di depan dan bisa dibuang dengan popleft().",
            "Sebelum memutuskan, jalankan while antre and antre[0] <= waktu - jendela: antre.popleft(), lalu bandingkan len(antre) dengan batas.",
        ],
        "solution": "import sys\nfrom collections import defaultdict, deque\n\nbaris = sys.stdin.read().split(\"\\n\")\nbatas, jendela = map(int, baris[0].split())\nriwayat = defaultdict(deque)\nfor teks in baris[1:]:\n    if not teks.strip():\n        continue\n    waktu, pengguna = teks.split()\n    waktu = int(waktu)\n    antre = riwayat[pengguna]\n    while antre and antre[0] <= waktu - jendela:\n        antre.popleft()\n    if len(antre) < batas:\n        antre.append(waktu)\n        print(waktu, pengguna, \"IZIN\")\n    else:\n        print(waktu, pengguna, \"TOLAK\")\n",
        "stdin_list": [
            """3 10
1 sari
2 sari
3 budi
4 sari
5 sari
11 sari
12 sari
14 sari
15 budi
""",
            """3 10
8 sari
9 sari
9 sari
10 sari
11 sari
18 sari
19 sari
19 budi
""",
            """2 5
0 andi
1 andi
2 andi
5 andi
6 andi
6 budi
7 budi
8 budi
""",
        ],
    },
    {
        "title": "Latihan 13: Document Store Mini dengan Operator Kueri",
        "difficulty": "Lanjut",
        "question": [
            "Buat document store mini. Koleksinya list of dict yang ditulis di",
            "program (salin persis):",
            "",
            "  _id  nama   umur  alamat.kota  hobi",
            "  1    Sari   24    Bandung      lari",
            "  2    Budi   31    Medan        catur",
            "  3    Dewi   19    Bandung      baca",
            "  4    Eko    45    Solo         lari",
            "  5    Fitri  28    Medan        baca",
            "",
            "Field alamat berupa dict bersarang, misalnya",
            "{\"_id\": 1, \"nama\": \"Sari\", \"umur\": 24,",
            "\"alamat\": {\"kota\": \"Bandung\"}, \"hobi\": \"lari\"}.",
            "",
            "Stdin berisi perintah, satu per baris:",
            "  FIND <filter JSON>",
            "  UPDATE <filter JSON> <perubahan JSON>",
            "",
            "Filter mendukung:",
            "  - kesamaan: {\"hobi\": \"lari\"}",
            "  - kunci bertitik ke dict bersarang: {\"alamat.kota\": \"Medan\"}",
            "  - operator $gt, $lt, $in, boleh digabung dalam satu syarat:",
            "    {\"umur\": {\"$gt\": 25, \"$lt\": 40}}",
            "  - $and berisi daftar filter: {\"$and\": [{...}, {...}]}",
            "  - beberapa kunci dalam satu filter berarti semuanya harus cocok",
            "Field yang nggak ada di dokumen nggak pernah cocok.",
            "",
            "Perubahan selalu berbentuk {\"$set\": {...}}. Kunci bertitik di",
            "$set membuat dict bersarang kalau belum ada.",
            "",
            "Untuk FIND, cetak FIND -> lalu nama dokumen yang cocok dipisah",
            "koma, urut menurut _id, atau (kosong). Untuk UPDATE, ubah semua",
            "dokumen yang cocok lalu cetak UPDATE -> <jumlah> dokumen.",
            "",
            "Contoh masukan:",
            "  FIND {\"alamat.kota\": \"Bandung\"}",
            "  FIND {\"umur\": {\"$gt\": 25, \"$lt\": 40}}",
            "  FIND {\"hobi\": {\"$in\": [\"lari\", \"catur\"]}}",
            "  FIND {\"$and\": [{\"alamat.kota\": \"Medan\"}, {\"umur\": {\"$lt\": 30}}]}",
            "  UPDATE {\"alamat.kota\": \"Bandung\"} {\"$set\": {\"alamat.kota\": \"Cimahi\", \"aktif\": true}}",
            "  FIND {\"aktif\": true}",
            "  FIND {\"alamat.kota\": \"Bandung\"}",
            "",
            "Keluaran yang diharapkan:",
            "FIND -> Sari, Dewi",
            "FIND -> Budi, Fitri",
            "FIND -> Sari, Budi, Eko",
            "FIND -> Fitri",
            "UPDATE -> 2 dokumen",
            "FIND -> Sari, Dewi",
            "FIND -> (kosong)",
        ],
        "hints": [
            "Pecah masalahnya jadi tiga fungsi kecil: mengambil nilai lewat jalur bertitik, memeriksa satu syarat, dan memeriksa seluruh filter.",
            "Fungsi pengambil sebaiknya mengembalikan dua hal, nilainya dan apakah field itu ada, supaya field yang hilang bisa dibedakan dari field yang isinya null.",
            "Baris UPDATE memuat dua JSON berurutan. json.JSONDecoder().raw_decode(teks) mengurai JSON pertama dan mengembalikan posisi akhirnya, lalu sisanya bisa diurai dengan json.loads.",
            "Untuk $set bertitik, telusuri bagian jalur kecuali yang terakhir dengan dok = dok.setdefault(nama, {}), lalu isi dok[bagian_terakhir].",
        ],
        "solution": """import json
import sys

KOLEKSI = [
    {"_id": 1, "nama": "Sari", "umur": 24, "alamat": {"kota": "Bandung"},
     "hobi": "lari"},
    {"_id": 2, "nama": "Budi", "umur": 31, "alamat": {"kota": "Medan"},
     "hobi": "catur"},
    {"_id": 3, "nama": "Dewi", "umur": 19, "alamat": {"kota": "Bandung"},
     "hobi": "baca"},
    {"_id": 4, "nama": "Eko", "umur": 45, "alamat": {"kota": "Solo"},
     "hobi": "lari"},
    {"_id": 5, "nama": "Fitri", "umur": 28, "alamat": {"kota": "Medan"},
     "hobi": "baca"},
]


def ambil(dok, jalur):
    nilai = dok
    for bagian in jalur.split("."):
        if not isinstance(nilai, dict) or bagian not in nilai:
            return None, False
        nilai = nilai[bagian]
    return nilai, True


def cocok_syarat(nilai, ada, syarat):
    if not isinstance(syarat, dict):
        return ada and nilai == syarat
    if not ada:
        return False
    for op, pembanding in syarat.items():
        if op == "$gt" and not nilai > pembanding:
            return False
        if op == "$lt" and not nilai < pembanding:
            return False
        if op == "$in" and nilai not in pembanding:
            return False
    return True


def cocok(dok, saringan):
    for kunci, syarat in saringan.items():
        if kunci == "$and":
            if not all(cocok(dok, bagian) for bagian in syarat):
                return False
        else:
            nilai, ada = ambil(dok, kunci)
            if not cocok_syarat(nilai, ada, syarat):
                return False
    return True


def pasang(dok, jalur, nilai):
    bagian = jalur.split(".")
    for nama in bagian[:-1]:
        dok = dok.setdefault(nama, {})
    dok[bagian[-1]] = nilai


pengurai = json.JSONDecoder()
for baris in sys.stdin:
    baris = baris.strip()
    if not baris:
        continue
    perintah, _, sisa = baris.partition(" ")
    if perintah == "FIND":
        saringan = json.loads(sisa)
        nama = [d["nama"] for d in KOLEKSI if cocok(d, saringan)]
        print("FIND ->", ", ".join(nama) if nama else "(kosong)")
    elif perintah == "UPDATE":
        saringan, akhir = pengurai.raw_decode(sisa)
        perubahan = json.loads(sisa[akhir:])
        jumlah = 0
        for d in KOLEKSI:
            if cocok(d, saringan):
                for jalur, nilai in perubahan["$set"].items():
                    pasang(d, jalur, nilai)
                jumlah += 1
        print(f"UPDATE -> {jumlah} dokumen")
""",
        "stdin_list": [
            """FIND {"alamat.kota": "Bandung"}
FIND {"umur": {"$gt": 25, "$lt": 40}}
FIND {"hobi": {"$in": ["lari", "catur"]}}
FIND {"$and": [{"alamat.kota": "Medan"}, {"umur": {"$lt": 30}}]}
UPDATE {"alamat.kota": "Bandung"} {"$set": {"alamat.kota": "Cimahi", "aktif": true}}
FIND {"aktif": true}
FIND {"alamat.kota": "Bandung"}
""",
            """FIND {"umur": {"$lt": 20}}
FIND {"nama": "Eko"}
UPDATE {"nama": {"$in": ["Eko", "Budi"]}} {"$set": {"umur": 50}}
FIND {"umur": {"$gt": 46}}
FIND {"kantor.kota": "Solo"}
UPDATE {"_id": 4} {"$set": {"kantor.kota": "Solo"}}
FIND {"kantor.kota": "Solo"}
""",
        ],
    },
    {
        "title": "Latihan 14: Aggregation Pipeline Buatan Sendiri",
        "difficulty": "Lanjut",
        "question": [
            "Jalankan aggregation pipeline buatan sendiri atas data pesanan yang",
            "ditulis di program (salin persis):",
            "",
            "  _id  kota     status   total",
            "  1    Bandung  lunas    120000",
            "  2    Medan    lunas    85000",
            "  3    Bandung  batal    60000",
            "  4    Solo     lunas    45000",
            "  5    Medan    lunas    150000",
            "  6    Bandung  lunas    30000",
            "  7    Solo     dikirim  99000",
            "",
            "Stdin berisi satu array JSON berisi tahap-tahap pipeline. Tiap",
            "tahap adalah dict dengan tepat satu kunci:",
            "  - $match: filter dengan kesamaan atau operator $gt, $gte, $lt,",
            "    $lte, $in pada field tingkat atas.",
            "  - $group: {\"_id\": \"$kolom\" atau null, \"nama\": {\"$sum\": ...}}.",
            "    Isi $sum berupa \"$kolom\" (jumlahkan kolom itu) atau angka",
            "    (tambahkan angka itu per dokumen, jadi {\"$sum\": 1} menghitung).",
            "    Urutan kelompok mengikuti kemunculan pertamanya, dan urutan",
            "    field mengikuti _id lalu urutan di aturan.",
            "  - $sort: {\"kolom\": 1 atau -1, ...}. Kolom pertama paling",
            "    menentukan, kolom berikutnya dipakai kalau nilainya seri.",
            "  - $limit: angka.",
            "",
            "Sesudah tiap tahap, cetak tahap <nomor> <nama>: <n> dokumen.",
            "Sesudah semua tahap, cetak tiap dokumen hasil dengan",
            "json.dumps(dok, ensure_ascii=False).",
            "",
            "Contoh masukan:",
            "  [{\"$match\": {\"status\": \"lunas\"}},",
            "   {\"$group\": {\"_id\": \"$kota\", \"omzet\": {\"$sum\": \"$total\"},",
            "               \"jumlah\": {\"$sum\": 1}}},",
            "   {\"$sort\": {\"omzet\": -1}}]",
            "",
            "Keluaran yang diharapkan:",
            "tahap 1 $match: 5 dokumen",
            "tahap 2 $group: 3 dokumen",
            "tahap 3 $sort: 3 dokumen",
            "{\"_id\": \"Medan\", \"omzet\": 235000, \"jumlah\": 2}",
            "{\"_id\": \"Bandung\", \"omzet\": 150000, \"jumlah\": 2}",
            "{\"_id\": \"Solo\", \"omzet\": 45000, \"jumlah\": 1}",
        ],
        "hints": [
            "Anggap tiap tahap sebagai fungsi yang menerima daftar dokumen dan mengembalikan daftar dokumen baru, lalu jalankan semuanya berurutan.",
            "Untuk $group, pakai dict biasa berkunci nilai _id, karena dict Python menjaga urutan kunci sesuai kemunculan pertamanya.",
            "Untuk $sort berkolom banyak, urutkan berkali-kali dari kolom terakhir ke kolom pertama, karena sort Python stabil dan reverse=True membalik arah per kolom.",
            "Satu tahap bisa dibongkar dengan (nama, aturan), = tahap.items(), dan ungkapan \"$kota\" diubah jadi dok[ungkapan[1:]].",
        ],
        "solution": """import json
import sys

PESANAN = [
    {"_id": 1, "kota": "Bandung", "status": "lunas", "total": 120000},
    {"_id": 2, "kota": "Medan", "status": "lunas", "total": 85000},
    {"_id": 3, "kota": "Bandung", "status": "batal", "total": 60000},
    {"_id": 4, "kota": "Solo", "status": "lunas", "total": 45000},
    {"_id": 5, "kota": "Medan", "status": "lunas", "total": 150000},
    {"_id": 6, "kota": "Bandung", "status": "lunas", "total": 30000},
    {"_id": 7, "kota": "Solo", "status": "dikirim", "total": 99000},
]

UJI = {
    "$gt": lambda a, b: a > b,
    "$gte": lambda a, b: a >= b,
    "$lt": lambda a, b: a < b,
    "$lte": lambda a, b: a <= b,
    "$in": lambda a, b: a in b,
}


def cocok(dok, saringan):
    for kolom, syarat in saringan.items():
        if kolom not in dok:
            return False
        if isinstance(syarat, dict):
            if not all(UJI[op](dok[kolom], b) for op, b in syarat.items()):
                return False
        elif dok[kolom] != syarat:
            return False
    return True


def nilai_dari(dok, ungkapan):
    if isinstance(ungkapan, str) and ungkapan.startswith("$"):
        return dok[ungkapan[1:]]
    return ungkapan


def kelompokkan(dokumen, aturan):
    hasil = {}
    for dok in dokumen:
        kunci = nilai_dari(dok, aturan["_id"])
        if kunci not in hasil:
            hasil[kunci] = {"_id": kunci}
            for nama in aturan:
                if nama != "_id":
                    hasil[kunci][nama] = 0
        for nama, akumulator in aturan.items():
            if nama != "_id":
                hasil[kunci][nama] += nilai_dari(dok, akumulator["$sum"])
    return list(hasil.values())


def urutkan(dokumen, aturan):
    dokumen = list(dokumen)
    for kolom, arah in reversed(list(aturan.items())):
        dokumen.sort(key=lambda d: d[kolom], reverse=(arah == -1))
    return dokumen


pipeline = json.loads(sys.stdin.read())
dokumen = PESANAN
for nomor, tahap in enumerate(pipeline, start=1):
    (nama, aturan), = tahap.items()
    if nama == "$match":
        dokumen = [d for d in dokumen if cocok(d, aturan)]
    elif nama == "$group":
        dokumen = kelompokkan(dokumen, aturan)
    elif nama == "$sort":
        dokumen = urutkan(dokumen, aturan)
    elif nama == "$limit":
        dokumen = dokumen[:aturan]
    print(f"tahap {nomor} {nama}: {len(dokumen)} dokumen")
for dok in dokumen:
    print(json.dumps(dok, ensure_ascii=False))
""",
        "stdin_list": [
            """[{"$match": {"status": "lunas"}}, {"$group": {"_id": "$kota", "omzet": {"$sum": "$total"}, "jumlah": {"$sum": 1}}}, {"$sort": {"omzet": -1}}]
""",
            """[{"$match": {"total": {"$gte": 60000}}}, {"$group": {"_id": "$status", "jumlah": {"$sum": 1}}}, {"$sort": {"jumlah": -1, "_id": 1}}]
""",
            """[{"$group": {"_id": null, "omzet": {"$sum": "$total"}, "jumlah": {"$sum": 1}}}]
""",
            """[{"$match": {"kota": {"$in": ["Bandung", "Solo"]}}}, {"$sort": {"total": -1}}, {"$limit": 2}]
""",
        ],
    },
    {
        "title": "Latihan 15: Aturan Keamanan ala Firestore",
        "difficulty": "Lanjut",
        "question": [
            "Buat evaluator aturan keamanan mini ala Firestore. Aturannya",
            "ditulis di program (salin persis):",
            "",
            "  jalur                         read            write",
            "  pengguna/{uid}                auth != null    auth.uid == uid",
            "  pengguna/{uid}/catatan/{id}   auth.uid == uid auth.uid == uid",
            "  pengumuman/{id}               true            auth.uid == 'admin'",
            "",
            "Tiap baris stdin berisi satu permintaan: pengguna, operasi (read",
            "atau write), dan jalur dokumen, dipisah spasi. Pengguna - artinya",
            "belum login.",
            "",
            "Cara mencocokkan:",
            "  - Pola dan jalur dipecah di tanda /. Jumlah bagiannya harus",
            "    sama persis, jadi aturan pengguna/{uid} nggak berlaku untuk",
            "    pengguna/sari/catatan/c1.",
            "  - Bagian berbentuk {nama} cocok dengan apa saja dan mengikat",
            "    nilainya ke nama itu. Bagian lain harus sama persis.",
            "  - Syarat yang dikenal: true, false, auth != null (sudah login),",
            "    auth.uid == <nama ikatan>, dan auth.uid == '<teks>'. Pengguna",
            "    yang belum login nggak pernah lolos syarat auth.uid.",
            "  - Kalau ada aturan cocok yang syaratnya terpenuhi, hasilnya",
            "    IZIN. Selain itu, termasuk jalur yang nggak cocok dengan aturan",
            "    mana pun, hasilnya TOLAK.",
            "",
            "Cetak IZIN atau TOLAK diikuti pengguna, operasi, dan jalurnya.",
            "",
            "Untuk input sari read pengguna/sari/catatan/c1, keluarannya:",
            "IZIN sari read pengguna/sari/catatan/c1",
            "TOLAK budi read pengguna/sari/catatan/c1",
            "IZIN - read pengumuman/p1",
            "TOLAK - write pengumuman/p1",
            "IZIN admin write pengumuman/p1",
            "IZIN budi read pengguna/sari",
            "TOLAK - read pengguna/sari",
            "IZIN sari write pengguna/sari",
            "TOLAK sari read rahasia/x",
            "",
            "(Masukan contoh itu berisi sembilan baris yang sama dengan",
            "keluarannya, tanpa kata IZIN/TOLAK di depan.)",
        ],
        "hints": [
            "Pisahkan dua pekerjaan: mencocokkan pola jalur sambil mengumpulkan ikatan, lalu menilai syarat memakai ikatan itu.",
            "Fungsi pencocok bisa mengembalikan dict ikatan seperti {\"uid\": \"sari\"} kalau cocok dan None kalau nggak, supaya dict kosong untuk pola tanpa variabel tetap dianggap cocok.",
            "Untuk syarat auth.uid == ..., pecah dengan split(\" == \"): kalau sisi kanan diawali tanda kutip, bandingkan dengan teksnya, kalau nggak, ambil nilainya dari ikatan.",
        ],
        "solution": """import sys

ATURAN = [
    ("pengguna/{uid}", {"read": "auth != null", "write": "auth.uid == uid"}),
    ("pengguna/{uid}/catatan/{id}", {"read": "auth.uid == uid",
                                     "write": "auth.uid == uid"}),
    ("pengumuman/{id}", {"read": "true", "write": "auth.uid == 'admin'"}),
]


def cocokkan(pola, jalur):
    bagian_pola, bagian_jalur = pola.split("/"), jalur.split("/")
    if len(bagian_pola) != len(bagian_jalur):
        return None
    ikatan = {}
    for p, j in zip(bagian_pola, bagian_jalur):
        if p.startswith("{") and p.endswith("}"):
            ikatan[p[1:-1]] = j
        elif p != j:
            return None
    return ikatan


def syarat_terpenuhi(syarat, uid, ikatan):
    if syarat == "true":
        return True
    if syarat == "false":
        return False
    if syarat == "auth != null":
        return uid is not None
    _, kanan = syarat.split(" == ")
    if uid is None:
        return False
    if kanan.startswith("'"):
        return uid == kanan.strip("'")
    return uid == ikatan.get(kanan)


for baris in sys.stdin:
    if not baris.strip():
        continue
    pengguna, operasi, jalur = baris.split()
    uid = None if pengguna == "-" else pengguna
    keputusan = "TOLAK"
    for pola, izin in ATURAN:
        ikatan = cocokkan(pola, jalur)
        if (ikatan is not None and operasi in izin
                and syarat_terpenuhi(izin[operasi], uid, ikatan)):
            keputusan = "IZIN"
            break
    print(keputusan, pengguna, operasi, jalur)
""",
        "stdin_list": [
            """sari read pengguna/sari/catatan/c1
budi read pengguna/sari/catatan/c1
- read pengumuman/p1
- write pengumuman/p1
admin write pengumuman/p1
budi read pengguna/sari
- read pengguna/sari
sari write pengguna/sari
sari read rahasia/x
""",
            """sari write pengguna/sari/catatan/c9
sari write pengguna/budi/catatan/c9
budi write pengguna/budi
- read pengguna/budi/catatan/c1
admin read pengguna/sari/catatan/c1
sari read pengguna/sari/catatan
""",
        ],
    },
    {
        "title": "Latihan 16: Desain Tabel Tunggal ala DynamoDB",
        "difficulty": "Lanjut",
        "question": [
            "Tiru desain tabel tunggal DynamoDB dengan satu dict berkunci",
            "pasangan (pk, sk). Tiap baris stdin berisi satu perintah:",
            "",
            "  PUT <pk> <sk> [atribut=nilai ...]   simpan item (menimpa utuh)",
            "  GET <pk> <sk>                       ambil satu item",
            "  QUERY <pk> [awalan]                 item ber-pk itu yang sk-nya",
            "                                      diawali awalan (boleh kosong)",
            "",
            "Aturan keluaran:",
            "  - PUT nggak mencetak apa pun.",
            "  - GET mencetak sk lalu atribut=nilai dipisah spasi, sesuai urutan",
            "    saat PUT, atau (tidak ada).",
            "  - QUERY mencetak QUERY <pk> <awalan> -> <n> item (tanpa awalan",
            "    kalau kosong), lalu tiap item dengan awalan dua spasi,",
            "    diurutkan menurut sk dari kecil ke besar seperti DynamoDB.",
            "",
            "Contoh masukan:",
            "  PUT PELANGGAN#42 PROFIL nama=Sari kota=Bandung",
            "  PUT PELANGGAN#42 PESANAN#2026-10-03#1007 total=85000 status=lunas",
            "  PUT PELANGGAN#42 PESANAN#2026-09-28#0998 total=30000 status=lunas",
            "  PUT PELANGGAN#42 ALAMAT#rumah jalan=Jl.Riau-12",
            "  PUT PELANGGAN#7 PROFIL nama=Budi kota=Medan",
            "  PUT PELANGGAN#42 PESANAN#2026-10-15#1032 total=120000 status=dikirim",
            "  GET PELANGGAN#42 PROFIL",
            "  QUERY PELANGGAN#42 PESANAN#",
            "  QUERY PELANGGAN#42 PESANAN#2026-10",
            "  QUERY PELANGGAN#7",
            "  GET PELANGGAN#7 ALAMAT#rumah",
            "",
            "Keluaran yang diharapkan:",
            "PROFIL nama=Sari kota=Bandung",
            "QUERY PELANGGAN#42 PESANAN# -> 3 item",
            "  PESANAN#2026-09-28#0998 total=30000 status=lunas",
            "  PESANAN#2026-10-03#1007 total=85000 status=lunas",
            "  PESANAN#2026-10-15#1032 total=120000 status=dikirim",
            "QUERY PELANGGAN#42 PESANAN#2026-10 -> 2 item",
            "  PESANAN#2026-10-03#1007 total=85000 status=lunas",
            "  PESANAN#2026-10-15#1032 total=120000 status=dikirim",
            "QUERY PELANGGAN#7 -> 1 item",
            "  PROFIL nama=Budi kota=Medan",
            "(tidak ada)",
        ],
        "hints": [
            "Kunci tabelnya pasangan (pk, sk), dan nilai tiap kunci adalah dict atribut, jadi PUT ke pasangan yang sama otomatis menimpa item lama.",
            "Query cukup menyaring item yang pk-nya sama dan sk-nya diawali awalan dengan str.startswith, lalu mengurutkan hasilnya menurut sk.",
            "Atribut bisa dibangun dengan dict(a.split(\"=\", 1) for a in bagian[3:]), dan dicetak kembali dengan \" \".join(f\"{k}={v}\" ...).",
        ],
        "solution": """import sys

tabel = {}


def query(pk, awalan=""):
    hasil = [(sk, item) for (p, sk), item in tabel.items()
             if p == pk and sk.startswith(awalan)]
    return sorted(hasil, key=lambda pasangan: pasangan[0])


def tampil(item):
    return " ".join(f"{k}={v}" for k, v in item.items())


for baris in sys.stdin:
    bagian = baris.split()
    if not bagian:
        continue
    perintah = bagian[0]
    if perintah == "PUT":
        pk, sk = bagian[1], bagian[2]
        tabel[(pk, sk)] = dict(a.split("=", 1) for a in bagian[3:])
    elif perintah == "GET":
        item = tabel.get((bagian[1], bagian[2]))
        print("(tidak ada)" if item is None else f"{bagian[2]} {tampil(item)}")
    elif perintah == "QUERY":
        pk = bagian[1]
        awalan = bagian[2] if len(bagian) > 2 else ""
        hasil = query(pk, awalan)
        judul = f"QUERY {pk} {awalan}".rstrip()
        print(f"{judul} -> {len(hasil)} item")
        for sk, item in hasil:
            print(f"  {sk} {tampil(item)}".rstrip())
""",
        "stdin_list": [
            """PUT PELANGGAN#42 PROFIL nama=Sari kota=Bandung
PUT PELANGGAN#42 PESANAN#2026-10-03#1007 total=85000 status=lunas
PUT PELANGGAN#42 PESANAN#2026-09-28#0998 total=30000 status=lunas
PUT PELANGGAN#42 ALAMAT#rumah jalan=Jl.Riau-12
PUT PELANGGAN#7 PROFIL nama=Budi kota=Medan
PUT PELANGGAN#42 PESANAN#2026-10-15#1032 total=120000 status=dikirim
GET PELANGGAN#42 PROFIL
QUERY PELANGGAN#42 PESANAN#
QUERY PELANGGAN#42 PESANAN#2026-10
QUERY PELANGGAN#7
GET PELANGGAN#7 ALAMAT#rumah
""",
            """PUT PRODUK#7 INFO nama=Kopi-Gayo harga=85000
PUT PRODUK#7 ULASAN#2026-10-01#sari bintang=5
PUT PRODUK#7 ULASAN#2026-10-09#budi bintang=3
PUT PRODUK#7 INFO nama=Kopi-Gayo harga=82000
QUERY PRODUK#7 ULASAN#
GET PRODUK#7 INFO
QUERY PRODUK#9
""",
        ],
    },
    {
        "title": "Latihan 17: Log Tulis-Depan dan Pemulihan Sesudah Crash",
        "difficulty": "Lanjut",
        "question": [
            "Bikin penyimpanan kunci-nilai yang selamat dari crash berkat log",
            "tulis-depan. Ada dua tempat menyimpan:",
            "",
            "  - log: daftar baris teks yang dianggap ada di disk, jadi",
            "    bertahan saat crash;",
            "  - data: dict di memori yang hilang saat crash.",
            "",
            "Perintah dibaca dari stdin, satu per baris:",
            "",
            "  SET k v    tambahkan 'SET k v;' ke log dulu, baru ubah data",
            "  DEL k      tambahkan 'DEL k;' ke log dulu, baru hapus dari data",
            "  GET k      cetak 'k = nilai' atau 'k = (kosong)'",
            "  ISI        cetak 'isi: k1=v1 k2=v2' urut kunci,",
            "             atau 'isi: (kosong)'",
            "  CRASH      kosongkan data, lalu bangun ulang dari log",
            "  PUTUS k v  listrik putus saat 'SET k v;' baru setengah",
            "             tertulis: tambahkan potongan awal baris itu",
            "             sepanjang len(baris) // 2 karakter ke log,",
            "             lalu lakukan CRASH",
            "",
            "Saat CRASH, cetak 'CRASH: memutar ulang N baris log' (N = isi",
            "log saat itu), putar ulang setiap baris yang diakhiri ';', buang",
            "baris yang nggak utuh dari log, lalu cetak",
            "'pulih: X perubahan, Y baris rusak dibuang'.",
            "",
            "Contoh masukan:",
            "",
            "  SET kota Bandung",
            "  SET nama Ani",
            "  GET kota",
            "  DEL kota",
            "  SET umur 20",
            "  ISI",
            "  CRASH",
            "  ISI",
            "  PUTUS nama Budi",
            "  GET nama",
            "  SET kota Medan",
            "  CRASH",
            "  ISI",
            "",
            "Keluaran yang diharapkan:",
            "kota = Bandung",
            "isi: nama=Ani umur=20",
            "CRASH: memutar ulang 4 baris log",
            "pulih: 4 perubahan, 0 baris rusak dibuang",
            "isi: nama=Ani umur=20",
            "CRASH: memutar ulang 5 baris log",
            "pulih: 4 perubahan, 1 baris rusak dibuang",
            "nama = Ani",
            "CRASH: memutar ulang 5 baris log",
            "pulih: 5 perubahan, 0 baris rusak dibuang",
            "isi: kota=Medan nama=Ani umur=20",
        ],
        "hints": [
            "Baca lagi contoh log tulis-depan versi mini di materi WAL, B-Tree, dan LSM-Tree: Jalan Data Menuju Disk.",
            "Pisahkan dua pekerjaan jadi fungsi: satu menerapkan satu baris log ke dict, satu lagi menulis ke log lalu menerapkannya.",
            "Saat CRASH, saring baris yang endswith(';'), terapkan semuanya ke dict kosong, lalu ganti isi log dengan hasil saringan itu.",
        ],
        "solution": """import sys

log = []     # bertahan melewati crash
data = {}    # hilang saat crash


def terapkan(rekaman):
    bagian = rekaman.split()
    if bagian[0] == "SET":
        data[bagian[1]] = bagian[2]
    else:
        data.pop(bagian[1], None)


def tulis(rekaman):
    log.append(rekaman + ";")   # catat dulu
    terapkan(rekaman)           # baru ubah memori


def crash():
    global data, log
    data = {}
    print(f"CRASH: memutar ulang {len(log)} baris log")
    utuh = [b for b in log if b.endswith(";")]
    for b in utuh:
        terapkan(b[:-1])
    print(f"pulih: {len(utuh)} perubahan, {len(log) - len(utuh)} baris rusak dibuang")
    log = utuh


for baris in sys.stdin:
    p = baris.split()
    if not p:
        continue
    if p[0] == "SET":
        tulis(f"SET {p[1]} {p[2]}")
    elif p[0] == "DEL":
        tulis(f"DEL {p[1]}")
    elif p[0] == "GET":
        print(f"{p[1]} = {data.get(p[1], '(kosong)')}")
    elif p[0] == "ISI":
        isi = " ".join(f"{k}={data[k]}" for k in sorted(data))
        print("isi:", isi or "(kosong)")
    elif p[0] == "CRASH":
        crash()
    elif p[0] == "PUTUS":
        rekaman = f"SET {p[1]} {p[2]};"
        log.append(rekaman[:len(rekaman) // 2])
        crash()""",
        "stdin_list": [
            """SET kota Bandung
SET nama Ani
GET kota
DEL kota
SET umur 20
ISI
CRASH
ISI
PUTUS nama Budi
GET nama
SET kota Medan
CRASH
ISI
""",
            """GET x
SET x 1
SET y 2
SET x 3
DEL y
CRASH
GET x
GET y
PUTUS y 99
ISI
""",
            """PUTUS a 1
ISI
SET a 1
SET b 2
DEL a
DEL b
CRASH
ISI
""",
        ],
    },
    {
        "title": "Latihan 18: Replika Tertinggal dan Pemilihan Primary",
        "difficulty": "Sulit",
        "question": [
            "Simulasikan satu primary bernama utama dan beberapa replika yang",
            "tertinggal. Jam-nya buatan: waktu cuma berubah lewat perintah",
            "WAKTU, jadi jangan memakai jam komputer.",
            "",
            "Log primary berisi tulisan (waktu_tulis, kunci, nilai). Replika",
            "berjeda L detik sudah menerapkan tulisan yang",
            "waktu_tulis + L <= waktu sekarang. Primary nggak punya jeda.",
            "",
            "Perintah dari stdin:",
            "",
            "  REPLIKA nama L  daftarkan replika berjeda L detik",
            "  WAKTU t         setel jam ke detik t",
            "  TULIS k v       tambahkan tulisan ke log primary, cetak",
            "                  't=T TULIS k=v di P (log: N)'",
            "  BACA node k     node = nama replika, nama primary, atau kata",
            "                  primary; cetak 't=T BACA node k -> nilai',",
            "                  nilai '(kosong)' kalau belum ada; kalau",
            "                  beda dengan primary, tambahkan",
            "                  ' (basi, primary: nilai_primary)'",
            "  MATI            primary mati: cetak",
            "                  't=T P mati, panjang log: r1=A r2=B'",
            "                  (urut nama), pilih replika dengan log",
            "                  terpanjang (seri: nama terkecil), potong",
            "                  log primary sepanjang log replika itu, lalu",
            "                  cetak 't=T R jadi primary, H tulisan hilang'",
            "",
            "Di baris BACA, nama node yang dicetak adalah nama aslinya",
            "(kata primary diganti nama primary yang sedang aktif). Sesudah",
            "failover, replika yang tersisa tetap memakai jedanya sendiri.",
            "",
            "Contoh masukan:",
            "",
            "  REPLIKA r1 1",
            "  REPLIKA r2 4",
            "  WAKTU 0",
            "  TULIS saldo 100",
            "  WAKTU 2",
            "  TULIS saldo 80",
            "  BACA primary saldo",
            "  BACA r1 saldo",
            "  BACA r2 saldo",
            "  WAKTU 3",
            "  TULIS bonus 5",
            "  MATI",
            "  BACA primary bonus",
            "  WAKTU 6",
            "  BACA r2 saldo",
            "",
            "Keluaran yang diharapkan:",
            "t=0 TULIS saldo=100 di utama (log: 1)",
            "t=2 TULIS saldo=80 di utama (log: 2)",
            "t=2 BACA utama saldo -> 80",
            "t=2 BACA r1 saldo -> 100 (basi, primary: 80)",
            "t=2 BACA r2 saldo -> (kosong) (basi, primary: 80)",
            "t=3 TULIS bonus=5 di utama (log: 3)",
            "t=3 utama mati, panjang log: r1=2 r2=0",
            "t=3 r1 jadi primary, 1 tulisan hilang",
            "t=3 BACA r1 bonus -> (kosong)",
            "t=6 BACA r2 saldo -> 80",
        ],
        "hints": [
            "Simpan log primary sebagai satu daftar saja; keadaan tiap replika bisa dihitung ulang dari daftar itu setiap kali dibaca.",
            "Buat fungsi keadaan(node) yang memutar log dan cuma memakai tulisan yang sudah tiba di node itu, lalu fungsi panjang(node) yang menghitung banyaknya tulisan yang sudah tiba.",
            "Saat MATI, pilih replika berlog terpanjang (kalau seri, nama terkecil), potong log dengan log[:panjang], ganti nama primary, lalu hapus replika itu dari daftar jeda.",
        ],
        "solution": """import sys

lag = {}          # replika -> jeda detik
log = []          # log primary: (waktu, kunci, nilai)
primary = "utama"
sekarang = 0


def keadaan(node):
    jeda = 0 if node == primary else lag[node]
    hasil = {}
    for t, k, v in log:
        if t + jeda <= sekarang:
            hasil[k] = v
    return hasil


def panjang(node):
    return sum(1 for t, _, _ in log if t + lag[node] <= sekarang)


for baris in sys.stdin:
    p = baris.split()
    if not p:
        continue
    if p[0] == "REPLIKA":
        lag[p[1]] = int(p[2])
    elif p[0] == "WAKTU":
        sekarang = int(p[1])
    elif p[0] == "TULIS":
        log.append((sekarang, p[1], p[2]))
        print(f"t={sekarang} TULIS {p[1]}={p[2]} di {primary} (log: {len(log)})")
    elif p[0] == "BACA":
        node = primary if p[1] == "primary" else p[1]
        nilai = keadaan(node).get(p[2], "(kosong)")
        benar = keadaan(primary).get(p[2], "(kosong)")
        catatan = "" if nilai == benar else f" (basi, primary: {benar})"
        print(f"t={sekarang} BACA {node} {p[2]} -> {nilai}{catatan}")
    elif p[0] == "MATI":
        calon = sorted(lag)
        isi = " ".join(f"{r}={panjang(r)}" for r in calon)
        print(f"t={sekarang} {primary} mati, panjang log: {isi}")
        baru = max(calon, key=lambda r: (panjang(r), -calon.index(r)))
        hilang = len(log) - panjang(baru)
        log = log[:panjang(baru)]
        primary = baru
        del lag[baru]
        print(f"t={sekarang} {baru} jadi primary, {hilang} tulisan hilang")""",
        "stdin_list": [
            """REPLIKA r1 1
REPLIKA r2 4
WAKTU 0
TULIS saldo 100
WAKTU 2
TULIS saldo 80
BACA primary saldo
BACA r1 saldo
BACA r2 saldo
WAKTU 3
TULIS bonus 5
MATI
BACA primary bonus
WAKTU 6
BACA r2 saldo
""",
            """REPLIKA a 2
REPLIKA b 2
WAKTU 1
TULIS x 1
WAKTU 4
TULIS x 2
BACA b x
MATI
TULIS y 7
BACA primary y
WAKTU 6
BACA b y
BACA b x
""",
            """REPLIKA lambat 9
REPLIKA cepat 1
WAKTU 0
TULIS menu nasi
WAKTU 1
TULIS menu soto
WAKTU 2
BACA lambat menu
BACA cepat menu
MATI
BACA lambat menu
WAKTU 10
BACA lambat menu
""",
        ],
    },
    {
        "title": "Latihan 19: Consistent Hashing dan Shard Kelima",
        "difficulty": "Lanjut",
        "question": [
            "Bandingkan dua cara membagi kunci ke shard saat empat shard",
            "bertambah jadi lima: modulo dan cincin consistent hashing.",
            "",
            "Masukan satu baris berisi dua angka: banyaknya kunci dan",
            "banyaknya virtual node per shard, misalnya '1000 50'. Kuncinya",
            "user0, user1, ..., sampai sebanyak angka pertama.",
            "",
            "Aturan yang harus dipakai persis supaya hasilnya cocok:",
            "",
            "  h(teks) = int(hashlib.md5(teks.encode()).hexdigest(), 16)",
            "            % 2**32",
            "  shard   = s0 s1 s2 s3 (empat), lalu s0 s1 s2 s3 s4 (lima)",
            "  modulo  : kunci milik shard ke-(h(kunci) % banyak_shard)",
            "  cincin  : shard s punya titik di posisi h(f'{s}#{v}') untuk",
            "            v = 0 sampai virtual - 1; kunci milik titik pertama",
            "            yang posisinya >= h(kunci); kalau nggak ada,",
            "            kembali ke titik dengan posisi terkecil",
            "",
            "Cetak tujuh baris: sebaran tiap cara untuk 4 dan 5 shard, berapa",
            "kunci yang pindah shard, dan berapa yang pindah ke s4 di cincin.",
            "",
            "Untuk input 1000 50, keluarannya:",
            "modulo 4: s0=216 s1=248 s2=279 s3=257",
            "modulo 5: s0=200 s1=191 s2=204 s3=206 s4=199",
            "modulo: 812 dari 1000 kunci pindah",
            "cincin 4: s0=253 s1=238 s2=278 s3=231",
            "cincin 5: s0=188 s1=183 s2=211 s3=207 s4=211",
            "cincin: 211 dari 1000 kunci pindah",
            "yang pindah ke s4: 211",
            "",
            "Coba juga '1000 1'. Dengan satu titik per shard, cincinnya",
            "timpang dan shard baru cuma mengambil kunci dari satu tetangga.",
        ],
        "hints": [
            "Simpan titik cincin sebagai daftar posisi yang terurut, lalu cari pemilik kunci dengan pencarian biner.",
            "Modul bisect sudah menyediakan pencarian biner: bisect_left memberi indeks titik pertama yang posisinya >= posisi kunci.",
            "Indeks yang sama dengan panjang daftar berarti kunci melewati titik terakhir, jadi pakai indeks % len(daftar) supaya kembali ke titik pertama.",
        ],
        "solution": """import bisect
import hashlib
import sys


def h(teks):
    return int(hashlib.md5(teks.encode()).hexdigest(), 16) % 2**32


def cincin(shard, virtual):
    titik = sorted((h(f"{s}#{v}"), s) for s in shard for v in range(virtual))
    return [t for t, _ in titik], [s for _, s in titik]


def pemilik(posisi, nama, kunci):
    i = bisect.bisect_left(posisi, h(kunci))
    return nama[i % len(nama)]          # lewat ujung: kembali ke awal


def sebaran(milik, shard):
    return " ".join(f"{s}={sum(1 for m in milik.values() if m == s)}"
                    for s in shard)


jumlah, virtual = map(int, sys.stdin.read().split())
kunci = [f"user{i}" for i in range(jumlah)]
empat = ["s0", "s1", "s2", "s3"]
lima = empat + ["s4"]

mod4 = {k: empat[h(k) % 4] for k in kunci}
mod5 = {k: lima[h(k) % 5] for k in kunci}
print("modulo 4:", sebaran(mod4, empat))
print("modulo 5:", sebaran(mod5, lima))
pindah = sum(1 for k in kunci if mod4[k] != mod5[k])
print(f"modulo: {pindah} dari {jumlah} kunci pindah")

p4, n4 = cincin(empat, virtual)
p5, n5 = cincin(lima, virtual)
c4 = {k: pemilik(p4, n4, k) for k in kunci}
c5 = {k: pemilik(p5, n5, k) for k in kunci}
print("cincin 4:", sebaran(c4, empat))
print("cincin 5:", sebaran(c5, lima))
pindah = sum(1 for k in kunci if c4[k] != c5[k])
print(f"cincin: {pindah} dari {jumlah} kunci pindah")
ke_baru = sum(1 for k in kunci if c4[k] != c5[k] and c5[k] == "s4")
print(f"yang pindah ke s4: {ke_baru}")""",
        "stdin_list": [
            """1000 50
""",
            """1000 1
""",
            """200 10
""",
        ],
    },
    {
        "title": "Latihan 20: Kuorum Baca-Tulis ala Cassandra",
        "difficulty": "Sulit",
        "question": [
            "Simulasikan N replika bernama r1 sampai rN yang menyimpan",
            "pasangan kunci-nilai bercap waktu. Jam-nya buatan: waktu cuma",
            "berubah lewat perintah WAKTU.",
            "",
            "Tingkat konsistensi menentukan berapa replika yang dibutuhkan:",
            "ONE = 1, QUORUM = N // 2 + 1, ALL = N.",
            "",
            "Supaya hasilnya bisa diperiksa, pemilihan replika dibuat tetap",
            "dan sengaja dibuat kasus terburuk:",
            "",
            "  - tulisan dikirim ke replika hidup bernomor terkecil sebanyak",
            "    yang dibutuhkan;",
            "  - bacaan bertanya ke replika hidup bernomor terbesar sebanyak",
            "    yang dibutuhkan, lalu mengambil nilai dengan waktu terbesar.",
            "",
            "Kalau replika hidup kurang dari yang dibutuhkan, operasi gagal",
            "dan nggak mengubah apa pun. Replika yang menerima tulisan",
            "menyimpannya kalau waktunya >= waktu nilai yang ia punya.",
            "",
            "Perintah dari stdin:",
            "",
            "  N n              jumlah replika (baris pertama)",
            "  WAKTU t          setel jam",
            "  MATI rX          cetak 't=T rX mati'",
            "  HIDUP rX         cetak 't=T rX hidup lagi' (datanya yang lama)",
            "  TULIS LVL k v    cetak 't=T TULIS LVL k=v: berhasil di r1 r2'",
            "  BACA LVL k       cetak 't=T BACA LVL k: nilai dari r2 r3'",
            "",
            "Nilai yang belum pernah ada dicetak '(kosong)'. Kalau bacaan",
            "nggak sama dengan tulisan terakhir yang berhasil untuk kunci itu,",
            "tambahkan ' (basi, terbaru NILAI)'. Kalau gagal, ganti bagian",
            "sesudah titik dua dengan 'GAGAL, butuh X replika, hidup Y'.",
            "",
            "Contoh masukan:",
            "",
            "  N 3",
            "  WAKTU 1",
            "  TULIS ALL kota Jakarta",
            "  WAKTU 2",
            "  TULIS ONE kota Bandung",
            "  BACA ONE kota",
            "  BACA QUORUM kota",
            "  WAKTU 3",
            "  TULIS QUORUM kota Medan",
            "  BACA QUORUM kota",
            "  BACA ONE kota",
            "",
            "Keluaran yang diharapkan:",
            "t=1 TULIS ALL kota=Jakarta: berhasil di r1 r2 r3",
            "t=2 TULIS ONE kota=Bandung: berhasil di r1",
            "t=2 BACA ONE kota: Jakarta dari r3 (basi, terbaru Bandung)",
            "t=2 BACA QUORUM kota: Jakarta dari r2 r3 (basi, terbaru Bandung)",
            "t=3 TULIS QUORUM kota=Medan: berhasil di r1 r2",
            "t=3 BACA QUORUM kota: Medan dari r2 r3",
            "t=3 BACA ONE kota: Jakarta dari r3 (basi, terbaru Medan)",
            "",
            "Perhatikan baris kedua dari bawah: QUORUM + QUORUM = 4 > 3, jadi",
            "kelompok baca dan tulis pasti bertemu di r2.",
        ],
        "hints": [
            "Simpan data per replika sebagai dict berisi pasangan (waktu, nilai), dan simpan juga tulisan terakhir yang berhasil untuk setiap kunci.",
            "Hitung dulu daftar replika hidup yang terurut; tulisan memakai potongan dari depan, bacaan memakai potongan dari belakang.",
            "Pasangan (waktu, nilai) bisa dibandingkan langsung dengan max(), karena tuple Python dibandingkan mulai dari elemen pertamanya.",
        ],
        "solution": """import sys

replika = []
hidup = set()
simpan = {}       # replika -> {kunci: (waktu, nilai)}
terbaru = {}      # kunci -> (waktu, nilai) tulisan terakhir yang berhasil
butuh = {}
sekarang = 0

for baris in sys.stdin:
    p = baris.split()
    if not p:
        continue
    if p[0] == "N":
        n = int(p[1])
        replika = [f"r{i}" for i in range(1, n + 1)]
        hidup = set(replika)
        simpan = {r: {} for r in replika}
        butuh = {"ONE": 1, "QUORUM": n // 2 + 1, "ALL": n}
    elif p[0] == "WAKTU":
        sekarang = int(p[1])
    elif p[0] in ("MATI", "HIDUP"):
        if p[0] == "MATI":
            hidup.discard(p[1])
            print(f"t={sekarang} {p[1]} mati")
        else:
            hidup.add(p[1])
            print(f"t={sekarang} {p[1]} hidup lagi")
    elif p[0] in ("TULIS", "BACA"):
        level, kunci = p[1], p[2]
        aktif = [r for r in replika if r in hidup]
        perlu = butuh[level]
        if p[0] == "TULIS":
            awal = f"t={sekarang} TULIS {level} {kunci}={p[3]}:"
        else:
            awal = f"t={sekarang} BACA {level} {kunci}:"
        if len(aktif) < perlu:
            print(f"{awal} GAGAL, butuh {perlu} replika, hidup {len(aktif)}")
        elif p[0] == "TULIS":
            sasaran = aktif[:perlu]                 # nomor terkecil
            for r in sasaran:
                lama = simpan[r].get(kunci)
                if lama is None or sekarang >= lama[0]:
                    simpan[r][kunci] = (sekarang, p[3])
            terbaru[kunci] = (sekarang, p[3])
            print(f"{awal} berhasil di {' '.join(sasaran)}")
        else:
            sasaran = aktif[-perlu:]                # nomor terbesar
            jawaban = [simpan[r][kunci] for r in sasaran if kunci in simpan[r]]
            dapat = max(jawaban) if jawaban else None
            teks = dapat[1] if dapat else "(kosong)"
            catatan = ""
            if kunci in terbaru and dapat != terbaru[kunci]:
                catatan = f" (basi, terbaru {terbaru[kunci][1]})"
            print(f"{awal} {teks} dari {' '.join(sasaran)}{catatan}")""",
        "stdin_list": [
            """N 3
WAKTU 1
TULIS ALL kota Jakarta
WAKTU 2
TULIS ONE kota Bandung
BACA ONE kota
BACA QUORUM kota
WAKTU 3
TULIS QUORUM kota Medan
BACA QUORUM kota
BACA ONE kota
""",
            """N 3
WAKTU 1
TULIS QUORUM stok 10
MATI r3
WAKTU 2
TULIS QUORUM stok 9
TULIS ALL stok 8
BACA QUORUM stok
MATI r2
TULIS QUORUM stok 7
BACA ONE stok
WAKTU 3
HIDUP r2
HIDUP r3
BACA ONE stok
BACA QUORUM stok
""",
            """N 5
WAKTU 1
TULIS QUORUM skor 50
BACA QUORUM skor
BACA ONE skor
WAKTU 2
TULIS ONE skor 70
BACA QUORUM skor
BACA ALL skor
""",
        ],
    },
    {
        "title": "Latihan 21: Mesin Pencari Mini dengan BM25",
        "difficulty": "Sulit",
        "question": [
            "Bangun mesin pencari kecil: indeks terbalik plus skor BM25.",
            "",
            "Masukan dari stdin. Bagian pertama berisi dokumen, satu per baris,",
            "dalam bentuk 'id teks'. Lalu satu baris '---'. Sesudahnya, setiap",
            "baris adalah satu kueri.",
            "",
            "Aturannya:",
            "",
            "  token     : re.findall(r'[a-z0-9]+', teks.lower()), tanpa",
            "              stop word dan tanpa stemming",
            "  kata kueri: kata yang sama di satu kueri dihitung sekali",
            "  skor      : jumlah untuk tiap kata q di kueri dari",
            "              IDF(q) * f * (k1 + 1) /",
            "              (f + k1 * (1 - b + b * |D| / rata))",
            "  IDF(q)    : ln(1 + (N - n + 0.5) / (n + 0.5))",
            "  k1 = 1.2, b = 0.75",
            "",
            "f = kemunculan q di dokumen D, |D| = banyaknya token D, rata =",
            "rata-rata banyaknya token semua dokumen, N = jumlah dokumen,",
            "n = jumlah dokumen yang memuat q.",
            "",
            "Untuk setiap kueri, cetak 'kueri: <teks kueri>' lalu paling",
            "banyak tiga dokumen berskor tertinggi, masing-masing '  id skor'",
            "dengan skor tiga angka di belakang titik. Skor sama diurutkan",
            "menurut id. Kalau nggak ada dokumen yang cocok, cetak",
            "'  (tidak ada)'.",
            "",
            "Contoh masukan:",
            "",
            "  d1 Kucing makan ikan goreng",
            "  d2 Kucing oren tidur di sofa, kucing itu malas",
            "  d3 Resep ikan bakar bumbu kecap",
            "  d4 Cara merawat kucing persia",
            "  d5 Ikan cupang dan ikan koi di akuarium",
            "  ---",
            "  kucing",
            "  ikan bakar",
            "  kucing tidur",
            "  mobil listrik",
            "",
            "Keluaran yang diharapkan:",
            "kueri: kucing",
            "  d2 0.661",
            "  d1 0.610",
            "  d4 0.610",
            "kueri: ikan bakar",
            "  d3 2.014",
            "  d5 0.692",
            "  d1 0.610",
            "kueri: kucing tidur",
            "  d2 1.841",
            "  d1 0.610",
            "  d4 0.610",
            "kueri: mobil listrik",
            "  (tidak ada)",
            "",
            "Perhatikan d2: kata kucing muncul dua kali, tapi skornya cuma",
            "sedikit di atas d1 karena d2 lebih panjang.",
        ],
        "hints": [
            "Pisahkan pekerjaannya jadi dua tahap: bangun indeks sekali dari semua dokumen, lalu hitung skor setiap kueri memakai indeks itu.",
            "Simpan indeks sebagai dict kata ke dict lain berisi id dokumen dan frekuensinya, jadi n adalah panjang dict dalam itu.",
            "Urutkan dengan sorted(skor.items(), key=lambda x: (-x[1], x[0])) lalu ambil tiga yang pertama, dan cetak skornya dengan f'{s:.3f}'.",
        ],
        "solution": """import math
import re
import sys

K1 = 1.2
B = 0.75


def token(teks):
    return re.findall(r"[a-z0-9]+", teks.lower())


baris = sys.stdin.read().splitlines()
pisah = baris.index("---")
dokumen = {}
for b in baris[:pisah]:
    if b.strip():
        nomor, teks = b.split(" ", 1)
        dokumen[nomor] = token(teks)
kueri = [b for b in baris[pisah + 1:] if b.strip()]

N = len(dokumen)
rata = sum(len(t) for t in dokumen.values()) / N
indeks = {}                      # kata -> {dokumen: frekuensi}
for nomor, kata_kata in dokumen.items():
    for kata in kata_kata:
        indeks.setdefault(kata, {})
        indeks[kata][nomor] = indeks[kata].get(nomor, 0) + 1


def idf(kata):
    n = len(indeks.get(kata, {}))
    return math.log(1 + (N - n + 0.5) / (n + 0.5))


for q in kueri:
    skor = {}
    for kata in sorted(set(token(q))):
        for nomor, f in indeks.get(kata, {}).items():
            panjang = len(dokumen[nomor])
            atas = f * (K1 + 1)
            bawah = f + K1 * (1 - B + B * panjang / rata)
            skor[nomor] = skor.get(nomor, 0) + idf(kata) * atas / bawah
    print(f"kueri: {q}")
    urut = sorted(skor.items(), key=lambda x: (-x[1], x[0]))[:3]
    if not urut:
        print("  (tidak ada)")
    for nomor, s in urut:
        print(f"  {nomor} {s:.3f}")""",
        "stdin_list": [
            """d1 Kucing makan ikan goreng
d2 Kucing oren tidur di sofa, kucing itu malas
d3 Resep ikan bakar bumbu kecap
d4 Cara merawat kucing persia
d5 Ikan cupang dan ikan koi di akuarium
---
kucing
ikan bakar
kucing tidur
mobil listrik
""",
            """a Sepatu lari ringan untuk pemula
b Sepatu kulit untuk kantor
c Kaos lari bahan dingin
d Tas lari dan botol minum
---
sepatu lari
kantor
SEPATU
""",
        ],
    },
    {
        "title": "Latihan 22: Baris Lawan Kolom: Agregasi Kolumnar",
        "difficulty": "Lanjut",
        "question": [
            "Simpan data penjualan yang sama dengan dua cara, lalu bandingkan",
            "berapa banyak nilai yang harus dibaca untuk menjawab satu kueri",
            "analitik: total jumlah per kategori.",
            "",
            "Masukan dari stdin, satu penjualan per baris, tanpa spasi:",
            "'tanggal,kategori,produk,jumlah'.",
            "",
            "  - Cara baris: list berisi dict, satu dict per penjualan. Setiap",
            "    dict dibaca utuh, jadi semua nilainya (4 per baris) dihitung",
            "    tersentuh.",
            "  - Cara kolom: dict berisi list, satu list per kolom. Kueri cuma",
            "    membaca list kategori dan jumlah (2 nilai per baris).",
            "",
            "Cetak total per kategori (urut nama, menjorok dua spasi),",
            "apakah hasil kedua cara sama, banyaknya nilai yang disentuh",
            "tiap cara, lalu kompresi run-length kolom kategori yang sudah",
            "diurutkan.",
            "",
            "Contoh masukan:",
            "",
            "  2026-10-01,minuman,kopi,12",
            "  2026-10-01,makanan,roti,6",
            "  2026-10-01,minuman,teh,8",
            "  2026-10-02,makanan,nasi,10",
            "  2026-10-02,minuman,kopi,15",
            "  2026-10-02,alat,sedotan,40",
            "",
            "Keluaran yang diharapkan:",
            "total per kategori:",
            "  alat 40",
            "  makanan 16",
            "  minuman 35",
            "hasil sama: ya",
            "cara baris: 24 nilai disentuh",
            "cara kolom: 12 nilai disentuh",
            "RLE kategori: alat x1, makanan x2, minuman x3",
            "RLE menyimpan 3 pasangan untuk 6 nilai",
        ],
        "hints": [
            "Bangun dua struktur sekaligus saat membaca masukan, supaya isi keduanya pasti sama.",
            "Untuk cara baris tambahkan len(dict) ke penghitung setiap baris; untuk cara kolom tambahkan 2 setiap pasangan kategori dan jumlah yang dibaca dengan zip.",
            "Untuk run-length, urutkan list kategori lalu berjalan satu per satu: kalau sama dengan pasangan terakhir naikkan hitungannya, kalau beda tambahkan pasangan baru [kategori, 1].",
        ],
        "solution": """import sys

KOLOM = ["tanggal", "kategori", "produk", "jumlah"]

baris = []                       # penyimpanan baris: list of dict
kolom = {k: [] for k in KOLOM}   # penyimpanan kolom: dict of list
for teks in sys.stdin.read().split():
    nilai = teks.split(",")
    nilai[3] = int(nilai[3])
    baris.append(dict(zip(KOLOM, nilai)))
    for k, v in zip(KOLOM, nilai):
        kolom[k].append(v)

total_b, sentuh_b = {}, 0
for b in baris:                  # baris dibaca utuh
    sentuh_b += len(b)
    total_b[b["kategori"]] = total_b.get(b["kategori"], 0) + b["jumlah"]

total_k, sentuh_k = {}, 0
for kat, jml in zip(kolom["kategori"], kolom["jumlah"]):
    sentuh_k += 2                # cuma dua kolom yang dibaca
    total_k[kat] = total_k.get(kat, 0) + jml

print("total per kategori:")
for kat in sorted(total_k):
    print(f"  {kat} {total_k[kat]}")
print("hasil sama:", "ya" if total_b == total_k else "tidak")
print(f"cara baris: {sentuh_b} nilai disentuh")
print(f"cara kolom: {sentuh_k} nilai disentuh")

urut = sorted(kolom["kategori"])
rle = []
for kat in urut:
    if rle and rle[-1][0] == kat:
        rle[-1][1] += 1
    else:
        rle.append([kat, 1])
print("RLE kategori:", ", ".join(f"{k} x{n}" for k, n in rle))
print(f"RLE menyimpan {len(rle)} pasangan untuk {len(urut)} nilai")""",
        "stdin_list": [
            """2026-10-01,minuman,kopi,12
2026-10-01,makanan,roti,6
2026-10-01,minuman,teh,8
2026-10-02,makanan,nasi,10
2026-10-02,minuman,kopi,15
2026-10-02,alat,sedotan,40
""",
            """2026-11-01,buku,novel,2
2026-11-01,buku,komik,3
2026-11-02,buku,kamus,1
2026-11-02,alat,pensil,10
""",
            """2026-12-01,minuman,kopi,7
""",
        ],
    },
    {
        "title": "Latihan 23: Tetangga Terdekat dengan Kemiripan Kosinus",
        "difficulty": "Lanjut",
        "question": [
            "Cari dua tetangga terdekat sebuah kata dengan kemiripan kosinus,",
            "lalu bandingkan dengan pencarian ala IVF yang cuma memeriksa satu",
            "kelompok. Vektornya buatan tangan, tanpa model AI. Salin data ini",
            "ke programmu:",
            "",
            "  kucing 0.9 0.1 0.1     apel   0.1 0.9 0.1     mobil 0.1 0.1 0.9",
            "  anjing 0.8 0.3 0.1     jeruk  0.2 0.8 0.3     motor 0.1 0.3 0.8",
            "  singa  0.7 0.0 0.4     pisang 0.4 0.7 0.0     kuda  0.6 0.1 0.7",
            "",
            "  pusat kelompok: hewan (1, 0, 0), buah (0, 1, 0),",
            "                  kendaraan (0, 0, 1)",
            "",
            "Langkahnya:",
            "",
            "  1. Masukkan setiap kata ke kelompok yang pusatnya paling mirip",
            "     (kosinus terbesar), lalu cetak isi tiap kelompok dengan",
            "     urutan hewan, buah, kendaraan, kata di dalamnya urut abjad.",
            "  2. Untuk setiap kata kueri dari stdin, cari dua kata lain yang",
            "     paling mirip dari semua kata (brute force).",
            "  3. Ulangi, tapi calonnya cuma kata lain di kelompok kata kueri",
            "     (IVF dengan satu kelompok yang diperiksa).",
            "  4. Cetak 'sama' kalau dua hasil itu identik, 'beda' kalau nggak.",
            "",
            "Bulatkan kemiripan ke tiga angka di belakang titik dengan round()",
            "sebelum mengurutkan, urutkan dari yang terbesar, dan kalau",
            "nilainya sama urutkan menurut abjad.",
            "",
            "Contoh masukan:",
            "",
            "  kucing",
            "  kuda",
            "  singa",
            "",
            "Keluaran yang diharapkan:",
            "kelompok hewan: anjing kucing singa",
            "kelompok buah: apel jeruk pisang",
            "kelompok kendaraan: kuda mobil motor",
            "kucing:",
            "  semua : anjing 0.970, singa 0.912",
            "  ivf   : anjing 0.970, singa 0.912 [kelompok hewan]",
            "  sama",
            "kuda:",
            "  semua : singa 0.936, mobil 0.829",
            "  ivf   : mobil 0.829, motor 0.815 [kelompok kendaraan]",
            "  beda",
            "singa:",
            "  semua : kuda 0.936, kucing 0.912",
            "  ivf   : kucing 0.912, anjing 0.865 [kelompok hewan]",
            "  beda",
            "",
            "Kuda jatuh di kelompok kendaraan, padahal tetangga terdekatnya",
            "singa. Begitulah harga kecepatan IVF: kata di dekat batas kelompok",
            "bisa terlewat.",
        ],
        "hints": [
            "Pisahkan tiga fungsi kecil: kosinus dua vektor, kelompok sebuah vektor, dan daftar calon terdekat dari sekumpulan kata.",
            "Hitung isi kelompok sekali di awal, lalu untuk IVF cukup ambil kata-kata di kelompok yang sama dengan kata kueri, tanpa kata kueri itu sendiri.",
            "Buat daftar pasangan (round(skor, 3), kata), urutkan dengan key=lambda x: (-x[0], x[1]), lalu ambil dua yang pertama dan bandingkan dua daftar itu dengan ==.",
        ],
        "solution": """import math
import sys

KATA = {
    "kucing": (0.9, 0.1, 0.1),
    "anjing": (0.8, 0.3, 0.1),
    "singa": (0.7, 0.0, 0.4),
    "apel": (0.1, 0.9, 0.1),
    "jeruk": (0.2, 0.8, 0.3),
    "pisang": (0.4, 0.7, 0.0),
    "mobil": (0.1, 0.1, 0.9),
    "motor": (0.1, 0.3, 0.8),
    "kuda": (0.6, 0.1, 0.7),
}
PUSAT = {
    "hewan": (1.0, 0.0, 0.0),
    "buah": (0.0, 1.0, 0.0),
    "kendaraan": (0.0, 0.0, 1.0),
}


def kosinus(a, b):
    titik = sum(x * y for x, y in zip(a, b))
    pa = math.sqrt(sum(x * x for x in a))
    pb = math.sqrt(sum(y * y for y in b))
    return titik / (pa * pb)


def terdekat(vektor, calon, jumlah):
    skor = [(round(kosinus(vektor, KATA[k]), 3), k) for k in calon]
    skor.sort(key=lambda x: (-x[0], x[1]))
    return skor[:jumlah]


def kelompok(vektor):
    return max(PUSAT, key=lambda p: kosinus(vektor, PUSAT[p]))


def tulis(hasil):
    return ", ".join(f"{k} {s:.3f}" for s, k in hasil) or "(tidak ada)"


anggota = {p: [] for p in PUSAT}
for k in sorted(KATA):
    anggota[kelompok(KATA[k])].append(k)
for p in PUSAT:
    print(f"kelompok {p}: {' '.join(anggota[p])}")

for baris in sys.stdin:
    q = baris.strip()
    if not q:
        continue
    v = KATA[q]
    semua = terdekat(v, [k for k in KATA if k != q], 2)
    g = kelompok(v)
    ivf = terdekat(v, [k for k in anggota[g] if k != q], 2)
    print(f"{q}:")
    print(f"  semua : {tulis(semua)}")
    print(f"  ivf   : {tulis(ivf)} [kelompok {g}]")
    print("  sama" if semua == ivf else "  beda")""",
        "stdin_list": [
            """kucing
kuda
singa
""",
            """apel
motor
""",
            """pisang
anjing
kuda
""",
        ],
    },
    {
        "title": "Latihan 24: Database Kunci-Nilai Mini dengan WAL, Indeks, dan TTL",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: bangun database kunci-nilai kecil yang memakai",
            "hampir semua ide di kurikulum ini sekaligus: log tulis-depan,",
            "pemulihan sesudah crash, indeks sekunder, transaksi, TTL dengan",
            "jam buatan, dan compaction.",
            "",
            "Program membaca perintah dari stdin, satu per baris, tanpa",
            "mencetak prompt. Kunci dan nilai nggak mengandung spasi.",
            "",
            "  WAKTU t          setel jam buatan ke detik t (awalnya 0)",
            "  SET k v [ttl]    simpan; kalau ada ttl, kunci kedaluwarsa",
            "                   saat jam >= waktu SET + ttl",
            "  GET k            cetak nilainya, atau (kosong) kalau nggak",
            "                   ada atau sudah kedaluwarsa",
            "  DEL k            hapus kunci",
            "  CARI v           cetak semua kunci hidup bernilai v, urut",
            "                   abjad dipisah spasi, atau (kosong)",
            "  BEGIN            mulai transaksi",
            "  COMMIT           tulis semua perubahan transaksi ke WAL dan",
            "                   terapkan; cetak 'COMMIT n perubahan'",
            "  ROLLBACK         buang perubahan transaksi; cetak",
            "                   'ROLLBACK n perubahan dibuang'",
            "  CRASH            buang semua keadaan di memori, termasuk",
            "                   transaksi yang terbuka, lalu bangun ulang",
            "                   dari WAL; cetak 'CRASH: pulih dari M baris WAL'",
            "  COMPACT          tulis ulang WAL jadi satu baris SET per kunci",
            "                   yang masih hidup; cetak 'COMPACT: wal M -> K'",
            "  STAT             cetak 'kunci=N wal=M' (N = kunci yang hidup)",
            "",
            "Aturan yang diuji:",
            "",
            "  - Di luar transaksi, setiap SET dan DEL menambah tepat satu",
            "    baris ke WAL lebih dulu, baru mengubah data di memori.",
            "  - Di dalam transaksi, SET dan DEL ditampung dulu. COMMIT",
            "    menambahkan satu baris WAL per perubahan. Waktu kedaluwarsa",
            "    dihitung saat perintah SET dibaca, bukan saat COMMIT.",
            "  - GET dan CARI selalu membaca data yang sudah di-COMMIT, juga",
            "    saat transaksi masih terbuka.",
            "  - WAL dan jam buatan bertahan melewati CRASH; data, indeks,",
            "    dan transaksi yang terbuka hilang.",
            "  - Indeks sekunder harus tetap benar sesudah SET ulang, DEL,",
            "    TTL habis, dan CRASH.",
            "  - Jangan memakai jam komputer, berkas, atau jaringan. WAL",
            "    cukup berupa list di memori yang nggak ikut dibuang saat",
            "    CRASH.",
            "",
            "Contoh masukan:",
            "",
            "  SET ani Bandung",
            "  SET budi Jakarta",
            "  SET cici Bandung",
            "  CARI Bandung",
            "  SET ani Medan",
            "  CARI Bandung",
            "  BEGIN",
            "  SET dodi Bandung",
            "  DEL budi",
            "  GET budi",
            "  CRASH",
            "  GET budi",
            "  CARI Bandung",
            "  STAT",
            "",
            "Keluaran yang diharapkan:",
            "ani cici",
            "cici",
            "Jakarta",
            "CRASH: pulih dari 4 baris WAL",
            "Jakarta",
            "cici",
            "kunci=3 wal=4",
            "",
            "Transaksi berisi dodi dan DEL budi belum di-COMMIT saat CRASH,",
            "jadi keduanya hilang. Kasus uji lain memakai TTL, COMPACT, dan",
            "ROLLBACK.",
        ],
        "hints": [
            "Pegang empat keadaan terpisah: daftar WAL, dict data berisi pasangan (nilai, waktu habis), dict indeks dari nilai ke set kunci, dan daftar transaksi yang bernilai None saat nggak ada transaksi.",
            "Buat satu fungsi terapkan(rekaman) yang dipakai baik saat menulis biasa maupun saat membangun ulang dari WAL; fungsi itu wajib melepas kunci dari indeks nilai lamanya sebelum memasang nilai baru.",
            "Simpan waktu habis sebagai angka mutlak di rekaman WAL (misalnya SET sesi aktif 40, atau tanda - kalau tanpa TTL), lalu cek sekarang < habis setiap kali GET, CARI, STAT, dan COMPACT memeriksa apakah sebuah kunci masih hidup.",
        ],
        "solution": """import sys

wal = []          # "disk": daftar rekaman, bertahan melewati CRASH
data = {}         # kunci -> (nilai, waktu_habis atau None)
indeks = {}       # nilai -> set kunci (indeks sekunder)
transaksi = None  # None, atau daftar rekaman yang menunggu COMMIT
sekarang = 0      # jam buatan


def hidup(kunci):
    if kunci not in data:
        return False
    habis = data[kunci][1]
    return habis is None or sekarang < habis


def terapkan(rekaman):
    bagian = rekaman.split()
    kunci = bagian[1]
    if kunci in data:                          # lepas dari indeks lama
        lama = data.pop(kunci)[0]
        indeks[lama].discard(kunci)
    if bagian[0] == "SET":
        habis = None if bagian[3] == "-" else int(bagian[3])
        data[kunci] = (bagian[2], habis)
        indeks.setdefault(bagian[2], set()).add(kunci)


def tulis(rekaman):
    wal.append(rekaman)                        # WAL dulu
    terapkan(rekaman)                          # baru keadaan di memori


def bangun_ulang():
    global data, indeks, transaksi
    data, indeks, transaksi = {}, {}, None
    for rekaman in wal:
        terapkan(rekaman)


for baris in sys.stdin:
    p = baris.split()
    if not p:
        continue
    perintah = p[0]
    if perintah == "WAKTU":
        sekarang = int(p[1])
    elif perintah in ("SET", "DEL"):
        if perintah == "SET":
            habis = str(sekarang + int(p[3])) if len(p) > 3 else "-"
            rekaman = f"SET {p[1]} {p[2]} {habis}"
        else:
            rekaman = f"DEL {p[1]}"
        if transaksi is None:
            tulis(rekaman)
        else:
            transaksi.append(rekaman)
    elif perintah == "GET":
        print(data[p[1]][0] if hidup(p[1]) else "(kosong)")
    elif perintah == "CARI":
        kunci = sorted(k for k in indeks.get(p[1], ()) if hidup(k))
        print(" ".join(kunci) if kunci else "(kosong)")
    elif perintah == "BEGIN":
        transaksi = []
    elif perintah == "COMMIT":
        for rekaman in transaksi:
            tulis(rekaman)
        print(f"COMMIT {len(transaksi)} perubahan")
        transaksi = None
    elif perintah == "ROLLBACK":
        print(f"ROLLBACK {len(transaksi)} perubahan dibuang")
        transaksi = None
    elif perintah == "CRASH":
        bangun_ulang()
        print(f"CRASH: pulih dari {len(wal)} baris WAL")
    elif perintah == "COMPACT":
        lama = len(wal)
        wal[:] = [f"SET {k} {data[k][0]} {'-' if data[k][1] is None else data[k][1]}"
                  for k in sorted(data) if hidup(k)]
        print(f"COMPACT: wal {lama} -> {len(wal)}")
    elif perintah == "STAT":
        print(f"kunci={sum(1 for k in data if hidup(k))} wal={len(wal)}")""",
        "stdin_list": [
            """SET ani Bandung
SET budi Jakarta
SET cici Bandung
CARI Bandung
SET ani Medan
CARI Bandung
BEGIN
SET dodi Bandung
DEL budi
GET budi
CRASH
GET budi
CARI Bandung
STAT
""",
            """WAKTU 10
SET sesi1 aktif 30
SET sesi2 aktif 5
SET kota Surabaya
CARI aktif
WAKTU 15
CARI aktif
GET sesi2
STAT
SET kota Malang
SET kota Surabaya
DEL sesi2
STAT
COMPACT
STAT
WAKTU 40
GET sesi1
CRASH
GET kota
CARI aktif
STAT
""",
            """SET a 1
BEGIN
SET b 2
SET c 1
ROLLBACK
CARI 1
BEGIN
SET b 2
DEL a
COMMIT
CARI 1
GET b
COMPACT
CRASH
GET a
GET b
STAT
""",
        ],
    },
]
