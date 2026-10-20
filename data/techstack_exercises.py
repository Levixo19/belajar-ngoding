"""Kurikulum Tech Stack & Arsitektur.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

TECHSTACK_EXERCISES = [
    {
        "title": "Latihan 1: Membaca Akronim Stack",
        "difficulty": "Mudah",
        "question": [
            "Kamu menerima beberapa akronim stack dari stdin, satu per baris.",
            "Untuk akronim yang dikenal, cetak namanya, lalu satu baris per",
            "huruf berisi huruf, komponen, dan lapisannya. Akronim yang nggak",
            "dikenal dicetak sebagai satu baris: NAMA: tidak dikenal.",
            "",
            "Aturan tambahan:",
            "  - Baris kosong dilewati.",
            "  - Spasi di tepi dibuang, dan huruf kecil tetap dikenali.",
            "    Nama selalu dicetak dalam huruf besar.",
            "",
            "Tabel yang dikenali program (huruf, komponen, lapisan):",
            "  LAMP  L Linux       sistem operasi",
            "        A Apache      web server",
            "        M MySQL       database",
            "        P PHP         backend",
            "  LEMP  L Linux       sistem operasi",
            "        E Nginx       web server",
            "        M MySQL       database",
            "        P PHP         backend",
            "  MERN  M MongoDB     database",
            "        E Express     backend",
            "        R React       frontend",
            "        N Node.js     backend",
            "  MEAN  M MongoDB     database",
            "        E Express     backend",
            "        A Angular     frontend",
            "        N Node.js     backend",
            "  PERN  P PostgreSQL  database",
            "        E Express     backend",
            "        R React       frontend",
            "        N Node.js     backend",
            "",
            "Contoh input:",
            "  MERN",
            "  XYZ",
            "  LEMP",
            "",
            "Keluaran yang diharapkan:",
            "MERN",
            "  M = MongoDB (database)",
            "  E = Express (backend)",
            "  R = React (frontend)",
            "  N = Node.js (backend)",
            "XYZ: tidak dikenal",
            "LEMP",
            "  L = Linux (sistem operasi)",
            "  E = Nginx (web server)",
            "  M = MySQL (database)",
            "  P = PHP (backend)",
            "",
            "Untuk input lamp, keluarannya:",
            "LAMP",
            "  L = Linux (sistem operasi)",
            "  A = Apache (web server)",
            "  M = MySQL (database)",
            "  P = PHP (backend)",
            "PERN",
            "  P = PostgreSQL (database)",
            "  E = Express (backend)",
            "  R = React (frontend)",
            "  N = Node.js (backend)",
            "MEAN",
            "  M = MongoDB (database)",
            "  E = Express (backend)",
            "  A = Angular (frontend)",
            "  N = Node.js (backend)",
        ],
        "hints": [
            "Simpan tabelnya sebagai dict: kuncinya akronim, isinya daftar pasangan komponen dan lapisan, urut sesuai hurufnya.",
            "Baca semua baris lewat sys.stdin, buang spasi tepi dengan strip(), lewati yang kosong, lalu ubah ke huruf besar dengan upper() sebelum dicari di dict.",
            "Untuk akronim yang dikenal, pasangkan tiap huruf dengan komponennya memakai zip(nama, STACK[nama]), lalu cetak dengan f\"  {huruf} = {komponen} ({lapisan})\".",
        ],
        "solution": """import sys

STACK = {
    "LAMP": [("Linux", "sistem operasi"), ("Apache", "web server"),
             ("MySQL", "database"), ("PHP", "backend")],
    "LEMP": [("Linux", "sistem operasi"), ("Nginx", "web server"),
             ("MySQL", "database"), ("PHP", "backend")],
    "MERN": [("MongoDB", "database"), ("Express", "backend"),
             ("React", "frontend"), ("Node.js", "backend")],
    "MEAN": [("MongoDB", "database"), ("Express", "backend"),
             ("Angular", "frontend"), ("Node.js", "backend")],
    "PERN": [("PostgreSQL", "database"), ("Express", "backend"),
             ("React", "frontend"), ("Node.js", "backend")],
}

for baris in sys.stdin:
    nama = baris.strip().upper()
    if not nama:
        continue
    if nama not in STACK:
        print(f"{nama}: tidak dikenal")
        continue
    print(nama)
    for huruf, (komponen, lapisan) in zip(nama, STACK[nama]):
        print(f"  {huruf} = {komponen} ({lapisan})")
""",
        "stdin_list": [
            """MERN
XYZ
LEMP
""",
            """lamp

  pern  
MEAN
""",
        ],
    },
    {
        "title": "Latihan 2: Router dan Controller Mini ala MVC",
        "difficulty": "Mudah",
        "question": [
            "Tulis aplikasi MVC mini yang membaca request dari stdin, satu",
            "per baris, lalu mencetak satu baris response untuk tiap request.",
            "",
            "Model awal berisi dua produk:",
            "  1 Buku tulis",
            "  2 Pulpen",
            "",
            "Rute yang dikenali:",
            "  GET /produk          ->  200 produk: <semua nama, urut id>",
            "  GET /produk/<id>     ->  200 produk #<id>: <nama>",
            "  POST /produk <nama>  ->  201 dibuat #<id baru>: <nama>",
            "",
            "Aturan:",
            "  - Nama di daftar dipisah koma dan spasi.",
            "  - <id> berupa angka. Kalau id itu nggak ada di model, cetak",
            "    404 produk #<id> tidak ada.",
            "  - Nama produk boleh memuat spasi. Id baru = id terbesar + 1.",
            "  - Request lain dicetak 404 rute tidak ada: <metode> <path>.",
            "  - Baris kosong dilewati.",
            "",
            "Usahakan tiga peran terpisah: fungsi model yang mengurus data,",
            "fungsi view yang menyusun teks, dan controller yang memilih.",
            "",
            "Contoh input:",
            "  GET /produk",
            "  POST /produk Pensil 2B",
            "  GET /produk/3",
            "  GET /produk/9",
            "  DELETE /produk/1",
            "",
            "Keluaran yang diharapkan:",
            "200 produk: Buku tulis, Pulpen",
            "201 dibuat #3: Pensil 2B",
            "200 produk #3: Pensil 2B",
            "404 produk #9 tidak ada",
            "404 rute tidak ada: DELETE /produk/1",
            "",
            "Untuk input GET /produk/2, keluarannya:",
            "200 produk #2: Pulpen",
            "404 rute tidak ada: GET /keranjang",
            "201 dibuat #3: Penghapus karet",
            "200 produk: Buku tulis, Pulpen, Penghapus karet",
        ],
        "hints": [
            "Pisahkan tiga peran: model menyimpan produk dan mencarinya berdasarkan id, view mengubah hasil jadi teks, dan controller memutuskan view mana yang dipakai.",
            "Pecah tiap baris dengan split(maxsplit=2) supaya kamu dapat metode, path, dan sisa teks yang menjadi nama produk walau nama itu memuat spasi.",
            "Untuk GET /produk/<id>, cek path.startswith(\"/produk/\"), ambil potongan sesudahnya, pastikan isdigit(), lalu cari di dict produk dengan produk.get(int(id_teks)).",
        ],
        "solution": """import sys

# ---- model
produk = {1: "Buku tulis", 2: "Pulpen"}


def semua_produk():
    return [produk[i] for i in sorted(produk)]


def cari(id_produk):
    return produk.get(id_produk)


def tambah(nama):
    id_baru = max(produk) + 1
    produk[id_baru] = nama
    return id_baru


# ---- view
def view_daftar(daftar):
    return "200 produk: " + ", ".join(daftar)


def view_satu(id_produk, nama):
    return f"200 produk #{id_produk}: {nama}"


def view_dibuat(id_produk, nama):
    return f"201 dibuat #{id_produk}: {nama}"


def view_404(pesan):
    return "404 " + pesan


# ---- controller
def tangani(baris):
    bagian = baris.split(maxsplit=2)
    metode, path = bagian[0], bagian[1]
    sisa = bagian[2] if len(bagian) > 2 else ""
    if metode == "GET" and path == "/produk":
        return view_daftar(semua_produk())
    if metode == "GET" and path.startswith("/produk/"):
        id_teks = path[len("/produk/"):]
        if id_teks.isdigit():
            nama = cari(int(id_teks))
            if nama is None:
                return view_404(f"produk #{id_teks} tidak ada")
            return view_satu(int(id_teks), nama)
    if metode == "POST" and path == "/produk" and sisa:
        return view_dibuat(tambah(sisa), sisa)
    return view_404(f"rute tidak ada: {metode} {path}")


for baris in sys.stdin:
    baris = baris.strip()
    if baris:
        print(tangani(baris))
""",
        "stdin_list": [
            """GET /produk
POST /produk Pensil 2B
GET /produk/3
GET /produk/9
DELETE /produk/1
""",
            """GET /produk/2
GET /keranjang

POST /produk Penghapus karet
GET /produk
""",
        ],
    },
    {
        "title": "Latihan 3: Router Mini dengan Middleware ala Express",
        "difficulty": "Menengah",
        "question": [
            "Express menjalankan setiap request lewat rantai middleware:",
            "fungsi (req, lanjut) yang boleh mengerjakan sesuatu, lalu",
            "memanggil lanjut() untuk menyerahkan request ke fungsi",
            "berikutnya. Kalau lanjut() nggak dipanggil, rantainya berhenti.",
            "",
            "Tiap baris stdin berisi satu request: METODE PATH [TOKEN].",
            "Jalankan request itu lewat tiga middleware berurutan:",
            "  1. catat      mencetak [log] METODE PATH, lalu lanjut.",
            "  2. cek_token  kalau path diawali /admin dan token bukan",
            "                rahasia, cetak 401 butuh token lalu berhenti.",
            "  3. router     mencari rute pertama yang cocok, lalu mencetak",
            "                responsnya. Kalau nggak ada yang cocok, cetak",
            "                404 tidak ditemukan.",
            "",
            "Rute (potongan yang diawali titik dua adalah parameter dan",
            "cocok dengan teks apa pun di posisi itu):",
            "  GET /                       200 beranda",
            "  GET /user/:id               200 profil user <id>",
            "  GET /produk/:id/ulasan/:no  200 ulasan <no> untuk produk <id>",
            "  GET /admin/laporan          200 laporan admin",
            "",
            "Path cocok kalau jumlah potongannya sama dan setiap potongan",
            "yang bukan parameter sama persis. Baris kosong dilewati.",
            "",
            "Contoh input:",
            "  GET /user/7",
            "  GET /admin/laporan",
            "  GET /admin/laporan rahasia",
            "  GET /produk/3/ulasan/12",
            "  DELETE /user/7",
            "  GET /user",
            "",
            "Keluaran yang diharapkan:",
            "[log] GET /user/7",
            "200 profil user 7",
            "[log] GET /admin/laporan",
            "401 butuh token",
            "[log] GET /admin/laporan",
            "200 laporan admin",
            "[log] GET /produk/3/ulasan/12",
            "200 ulasan 12 untuk produk 3",
            "[log] DELETE /user/7",
            "404 tidak ditemukan",
            "[log] GET /user",
            "404 tidak ditemukan",
            "",
            "Untuk input GET /, keluarannya:",
            "[log] GET /",
            "200 beranda",
            "[log] GET /admin/laporan",
            "401 butuh token",
            "[log] GET /user/abc",
            "200 profil user abc",
        ],
        "hints": [
            "Anggap setiap middleware fungsi yang menerima request dan sebuah fungsi lanjut; middleware memutuskan sendiri apakah rantai diteruskan dengan memanggil lanjut().",
            "Untuk rute berparameter, pecah pola dan path dengan strip(\"/\").split(\"/\"), pastikan jumlah potongannya sama, lalu simpan potongan pola yang diawali titik dua ke dict param.",
            "Simpan middleware di list [catat, cek_token, router], lalu buat fungsi langkah(i) yang memanggil MIDDLEWARE[i](req, lambda: langkah(i + 1)) selama i masih di dalam list.",
        ],
        "solution": "import sys\n\n\ndef cocok(pola, path):\n    \"\"\"dict parameter kalau path cocok dengan pola, None kalau tidak.\"\"\"\n    a = pola.strip(\"/\").split(\"/\")\n    b = path.strip(\"/\").split(\"/\")\n    if len(a) != len(b):\n        return None\n    param = {}\n    for x, y in zip(a, b):\n        if x.startswith(\":\"):\n            param[x[1:]] = y\n        elif x != y:\n            return None\n    return param\n\n\nRUTE = [\n    (\"GET\", \"/\", lambda p: \"200 beranda\"),\n    (\"GET\", \"/user/:id\", lambda p: f\"200 profil user {p['id']}\"),\n    (\"GET\", \"/produk/:id/ulasan/:no\",\n     lambda p: f\"200 ulasan {p['no']} untuk produk {p['id']}\"),\n    (\"GET\", \"/admin/laporan\", lambda p: \"200 laporan admin\"),\n]\n\n\ndef catat(req, lanjut):\n    print(f\"[log] {req['metode']} {req['path']}\")\n    lanjut()\n\n\ndef cek_token(req, lanjut):\n    if req[\"path\"].startswith(\"/admin\") and req[\"token\"] != \"rahasia\":\n        print(\"401 butuh token\")\n        return\n    lanjut()\n\n\ndef router(req, lanjut):\n    for metode, pola, fungsi in RUTE:\n        if metode == req[\"metode\"]:\n            param = cocok(pola, req[\"path\"])\n            if param is not None:\n                print(fungsi(param))\n                return\n    print(\"404 tidak ditemukan\")\n\n\nMIDDLEWARE = [catat, cek_token, router]\n\n\ndef jalankan(req):\n    def langkah(i):\n        if i < len(MIDDLEWARE):\n            MIDDLEWARE[i](req, lambda: langkah(i + 1))\n    langkah(0)\n\n\nfor baris in sys.stdin:\n    bagian = baris.split()\n    if not bagian:\n        continue\n    jalankan({\"metode\": bagian[0], \"path\": bagian[1],\n              \"token\": bagian[2] if len(bagian) > 2 else \"\"})\n",
        "stdin_list": [
            """GET /user/7
GET /admin/laporan
GET /admin/laporan rahasia
GET /produk/3/ulasan/12
DELETE /user/7
GET /user
""",
            """GET /

GET /admin/laporan salah
GET /user/abc
""",
        ],
    },
    {
        "title": "Latihan 4: Kontainer Dependency Injection Mini",
        "difficulty": "Menengah",
        "question": [
            "Spring dan ASP.NET Core punya kontainer dependency injection:",
            "kamu cukup menyatakan apa yang dibutuhkan sebuah komponen, dan",
            "kontainer yang membuat semuanya dengan urutan yang benar.",
            "Tulis versi mininya.",
            "",
            "Tiap baris stdin berbentuk nama: dep1, dep2. Baris nama: tanpa",
            "isi berarti komponen itu nggak butuh apa-apa. Baris kosong",
            "dilewati.",
            "",
            "Aturan pembuatan:",
            "  1. Proses komponen menurut abjad namanya.",
            "  2. Sebelum membuat sebuah komponen, buat dulu semua yang",
            "     dibutuhkannya, juga menurut abjad, dengan aturan yang sama.",
            "  3. Komponen yang sudah dibuat nggak dibuat lagi.",
            "",
            "Kalau semua berhasil, cetak buat <nama> untuk tiap komponen",
            "sesuai urutan pembuatannya, lalu total: <n> komponen.",
            "",
            "Kalau ada masalah, jangan cetak urutan apa pun. Cetak satu baris",
            "galat untuk masalah pertama yang ditemui saat mengikuti aturan:",
            "  - Komponen yang dibutuhkan tapi nggak ada di input:",
            "    galat: <dep> dibutuhkan <nama> tapi tidak terdaftar",
            "  - Siklus, yaitu bertemu lagi komponen yang sedang dalam proses",
            "    dibuat: galat: siklus a -> b -> a, berisi jalur dari",
            "    komponen itu sampai kembali ke dirinya.",
            "",
            "Contoh input:",
            "  controller: service",
            "  service: repo, logger",
            "  repo: database",
            "  database: config",
            "  logger: config",
            "  config:",
            "",
            "Keluaran yang diharapkan:",
            "buat config",
            "buat logger",
            "buat database",
            "buat repo",
            "buat service",
            "buat controller",
            "total: 6 komponen",
            "",
            "Untuk input a: b, keluarannya:",
            "galat: siklus a -> b -> c -> a",
            "",
            "Untuk input web: cache, db, keluarannya:",
            "galat: cache dibutuhkan web tapi tidak terdaftar",
        ],
        "hints": [
            "Sebelum sebuah komponen dibuat, semua kebutuhannya harus sudah ada, dan itu pola fungsi rekursif yang membuat kebutuhannya dulu baru dirinya sendiri.",
            "Bawa daftar komponen yang sedang dalam proses dibuat (jalur); kalau kamu bertemu komponen yang sudah ada di jalur itu, potongan jalur dari komponen tersebut sampai akhir, ditambah komponen itu sekali lagi, adalah isi pesan siklus.",
            "Kumpulkan urutan di list selesai, lempar exception untuk kedua jenis galat, lalu panggil buat(nama, []) untuk setiap nama di sorted(butuh) di dalam satu blok try/except.",
        ],
        "solution": """import sys

butuh = {}
for baris in sys.stdin:
    baris = baris.strip()
    if not baris:
        continue
    nama, _, sisa = baris.partition(":")
    butuh[nama.strip()] = [d.strip() for d in sisa.split(",") if d.strip()]


class Galat(Exception):
    pass


selesai = []


def buat(nama, jalur):
    if nama in selesai:
        return
    if nama in jalur:
        siklus = jalur[jalur.index(nama):] + [nama]
        raise Galat("siklus " + " -> ".join(siklus))
    jalur.append(nama)
    for dep in sorted(butuh[nama]):
        if dep not in butuh:
            raise Galat(f"{dep} dibutuhkan {nama} tapi tidak terdaftar")
        buat(dep, jalur)
    jalur.pop()
    selesai.append(nama)


try:
    for nama in sorted(butuh):
        buat(nama, [])
except Galat as e:
    print(f"galat: {e}")
else:
    for nama in selesai:
        print(f"buat {nama}")
    print(f"total: {len(selesai)} komponen")
""",
        "stdin_list": [
            """controller: service
service: repo, logger
repo: database
database: config
logger: config
config:
""",
            """a: b
b: c

c: a
d:
""",
            """web: cache, db
db:
""",
        ],
    },
    {
        "title": "Latihan 5: Handler Serverless dan Cold Start",
        "difficulty": "Menengah",
        "question": [
            "Bikin simulator kecil yang menandai tiap panggilan fungsi serverless",
            "sebagai COLD atau WARM, lalu menghitung durasi yang ditagih. Anggap tiap",
            "fungsi punya paling banyak satu instans dan panggilan datang satu per",
            "satu.",
            "",
            "Baris pertama input berisi dua angka: batas menganggur dan biaya",
            "inisialisasi dalam ms. Tiap baris berikutnya satu panggilan: waktu",
            "(angka jam palsu yang selalu naik), nama fungsi, dan durasi handler",
            "dalam ms.",
            "",
            "Aturannya:",
            "  - Panggilan COLD kalau fungsinya belum pernah dipanggil, atau selisih",
            "    waktunya dengan panggilan terakhir fungsi itu lebih dari batas",
            "    menganggur. Selisih yang sama persis dengan batas masih WARM.",
            "  - Durasi yang ditagih = durasi handler, ditambah biaya inisialisasi",
            "    kalau COLD.",
            "  - Cetak satu baris per panggilan, lalu ringkasan per fungsi urut",
            "    abjad, lalu total ditagih.",
            "",
            "Contoh input:",
            "  5 300",
            "  0 harga 120",
            "  2 harga 100",
            "  3 stok 80",
            "  10 harga 110",
            "  12 stok 90",
            "  14 stok 70",
            "",
            "Keluaran yang diharapkan:",
            "t=0 harga COLD 420 ms",
            "t=2 harga WARM 100 ms",
            "t=3 stok COLD 380 ms",
            "t=10 harga COLD 410 ms",
            "t=12 stok COLD 390 ms",
            "t=14 stok WARM 70 ms",
            "harga: 3 panggilan, 2 cold, 930 ms",
            "stok: 3 panggilan, 2 cold, 840 ms",
            "total ditagih: 1770 ms",
        ],
        "hints": [
            "Ingat lagi materi cold start: instans baru butuh inisialisasi, instans yang masih hidup dipakai ulang, dan instans dibuang kalau terlalu lama menganggur.",
            "Simpan waktu panggilan terakhir tiap fungsi di dict; sebuah panggilan COLD kalau namanya belum ada di dict atau selisih waktunya lebih besar dari batas.",
            "Pakai dict kedua berisi [jumlah panggilan, jumlah cold, total ms] per fungsi, tambahkan biaya inisialisasi hanya untuk panggilan COLD, lalu cetak ringkasannya dengan for fungsi in sorted(dict).",
        ],
        "solution": """import sys

baris = [b.split() for b in sys.stdin.read().splitlines() if b.strip()]
batas_idle, biaya_init = int(baris[0][0]), int(baris[0][1])

terakhir = {}   # fungsi -> waktu panggilan terakhir
ringkas = {}    # fungsi -> [jumlah panggilan, jumlah cold, ms ditagih]

for t, fungsi, durasi in baris[1:]:
    t, durasi = int(t), int(durasi)
    dingin = fungsi not in terakhir or t - terakhir[fungsi] > batas_idle
    terakhir[fungsi] = t
    tagih = durasi + (biaya_init if dingin else 0)
    data = ringkas.setdefault(fungsi, [0, 0, 0])
    data[0] += 1
    data[1] += 1 if dingin else 0
    data[2] += tagih
    print(f"t={t} {fungsi} {'COLD' if dingin else 'WARM'} {tagih} ms")

for fungsi in sorted(ringkas):
    n, cold, ms = ringkas[fungsi]
    print(f"{fungsi}: {n} panggilan, {cold} cold, {ms} ms")
print("total ditagih:", sum(d[2] for d in ringkas.values()), "ms")""",
        "stdin_list": [
            """5 300
0 harga 120
2 harga 100
3 stok 80
10 harga 110
12 stok 90
14 stok 70
""",
            """10 250
1 kirim_email 40
5 kirim_email 35
20 kirim_email 50
21 laporan 900
30 kirim_email 45
33 laporan 870
""",
        ],
    },
    {
        "title": "Latihan 6: Pemeriksa SemVer",
        "difficulty": "Menengah",
        "question": [
            "Input berisi daftar string versi, satu per baris. Periksa tiap string",
            "dengan aturan SemVer 2.0.0, cetak yang nggak sah, lalu urutkan yang sah",
            "dari yang paling rendah.",
            "",
            "Aturan sah:",
            "  - Bagian inti berupa tiga angka dipisah titik. Tiap angka nggak boleh",
            "    diawali nol, kecuali angka 0 itu sendiri.",
            "  - Pra-rilis opsional, ditulis sesudah tanda hubung, berupa potongan",
            "    dipisah titik. Tiap potongan berisi huruf, angka, atau tanda hubung,",
            "    nggak boleh kosong, dan potongan yang isinya angka saja nggak boleh",
            "    diawali nol.",
            "  - Metadata build opsional, ditulis sesudah tanda plus, dengan aturan",
            "    potongan yang sama tapi boleh diawali nol.",
            "",
            "Aturan urut:",
            "  - Bandingkan tiga angka inti sebagai angka.",
            "  - Kalau angkanya sama, versi pra-rilis lebih rendah daripada versi",
            "    tanpa pra-rilis.",
            "  - Pra-rilis dibandingkan per potongan: angka sebagai angka, huruf",
            "    menurut urutan ASCII, potongan angka lebih rendah daripada potongan",
            "    huruf, dan kalau semua potongan di depannya sama, yang lebih banyak",
            "    potongannya lebih tinggi.",
            "  - Metadata build diabaikan. Versi yang setara tetap dalam urutan",
            "    masuknya.",
            "",
            "Cetak dulu setiap versi yang nggak sah dengan awalan \"tidak sah: \"",
            "sesuai urutan input, lalu baris \"urutan (N versi sah):\", lalu versi yang",
            "sah satu per baris.",
            "",
            "Contoh input:",
            "  1.0.0",
            "  1.0.0-beta.11",
            "  1.0.0-alpha",
            "  01.2.3",
            "  1.0.0-rc.1",
            "  1.0.0-alpha.beta",
            "  1.2",
            "  1.0.0-beta",
            "  1.0.0-alpha.1",
            "  2.0.0+build.7",
            "  1.0.0-beta.2",
            "  1.0.0-alpha..1",
            "  1.10.0",
            "  1.9.0",
            "  1.0.0-01",
            "",
            "Keluaran yang diharapkan:",
            "tidak sah: 01.2.3",
            "tidak sah: 1.2",
            "tidak sah: 1.0.0-alpha..1",
            "tidak sah: 1.0.0-01",
            "urutan (11 versi sah):",
            "1.0.0-alpha",
            "1.0.0-alpha.1",
            "1.0.0-alpha.beta",
            "1.0.0-beta",
            "1.0.0-beta.2",
            "1.0.0-beta.11",
            "1.0.0-rc.1",
            "1.0.0",
            "1.9.0",
            "1.10.0",
            "2.0.0+build.7",
        ],
        "hints": [
            "Baca lagi bagian SemVer: tiga angka tanpa nol di depan, pra-rilis sesudah tanda hubung, dan metadata build sesudah tanda plus yang diabaikan saat membandingkan.",
            "Pisahkan build dengan partition(\"+\") lebih dulu, lalu pra-rilis dengan partition(\"-\"), periksa tiap potongan dengan regex, lalu buat fungsi kunci berbentuk tuple supaya sort() bisa membandingkan langsung.",
            "Kunci yang bekerja: (angka, 1, ()) untuk versi tanpa pra-rilis dan (angka, 0, potongan) untuk pra-rilis, dengan tiap potongan diubah jadi (0, int(p), \"\") kalau angka atau (1, 0, p) kalau huruf; sort() di Python stabil, jadi versi yang setara tetap berurutan seperti input.",
        ],
        "solution": "import re\nimport sys\n\nANGKA = re.compile(r\"0|[1-9][0-9]*\")\nPOTONGAN = re.compile(r\"[0-9A-Za-z-]+\")\n\n\ndef urai(teks):\n    \"\"\"(angka, pra-rilis) kalau sah menurut SemVer 2.0.0, None kalau tidak.\"\"\"\n    inti, plus, build = teks.partition(\"+\")\n    if plus and not all(POTONGAN.fullmatch(b) for b in build.split(\".\")):\n        return None\n    inti, minus, pra = inti.partition(\"-\")\n    bagian = inti.split(\".\")\n    if len(bagian) != 3 or not all(ANGKA.fullmatch(b) for b in bagian):\n        return None\n    daftar_pra = pra.split(\".\") if minus else []\n    for p in daftar_pra:\n        if not POTONGAN.fullmatch(p):\n            return None\n        if p.isdigit() and not ANGKA.fullmatch(p):\n            return None\n    return tuple(int(b) for b in bagian), daftar_pra\n\n\ndef kunci(hasil):\n    angka, pra = hasil\n    if not pra:\n        return (angka, 1, ())\n    return (angka, 0, tuple((0, int(p), \"\") if p.isdigit() else (1, 0, p)\n                           for p in pra))\n\n\nsah = []\nfor teks in sys.stdin.read().split():\n    hasil = urai(teks)\n    if hasil is None:\n        print(\"tidak sah:\", teks)\n    else:\n        sah.append((kunci(hasil), teks))\n\nsah.sort(key=lambda x: x[0])\nprint(f\"urutan ({len(sah)} versi sah):\")\nfor _, teks in sah:\n    print(teks)",
        "stdin_list": [
            """1.0.0
1.0.0-beta.11
1.0.0-alpha
01.2.3
1.0.0-rc.1
1.0.0-alpha.beta
1.2
1.0.0-beta
1.0.0-alpha.1
2.0.0+build.7
1.0.0-beta.2
1.0.0-alpha..1
1.10.0
1.9.0
1.0.0-01
""",
            """0.10.0
v1.2.3
0.9.12
1.0.0+20261019
1.0.0
1.0.0-rc.1
1.2.3-
1.0.0-RC.1
1.0.0-rc.1+build.5
00.1.0
""",
        ],
    },
    {
        "title": "Latihan 7: Versi Berikutnya dari Conventional Commits",
        "difficulty": "Menengah",
        "question": [
            "Baris pertama input berisi versi sekarang. Sesudahnya ada beberapa pesan",
            "commit, dipisah baris yang isinya --- saja. Satu pesan commit boleh",
            "terdiri dari beberapa baris: baris pertama judul, baris berikutnya badan",
            "dan footer.",
            "",
            "Tentukan kenaikan versi dengan aturan Conventional Commits:",
            "  - Judul berbentuk tipe(scope opsional): deskripsi, dengan tanda !",
            "    opsional tepat sebelum titik dua.",
            "  - Perubahan merusak kalau ada tanda !, atau ada baris berawalan",
            "    BREAKING CHANGE: atau BREAKING-CHANGE: di bawah judul. Kenaikannya",
            "    mayor, kecuali versi sekarang 0.x: cukup minor. Beberapa alat rilis",
            "    menyediakan pilihan seperti ini.",
            "  - Kalau nggak ada yang merusak: ada feat berarti minor, kalau cuma fix",
            "    berarti patch, selain itu nggak ada rilis.",
            "  - Angka di kanan angka yang naik kembali ke nol.",
            "",
            "Sesudah tiga baris ringkasan, cetak kelompok merusak, fitur, dan",
            "perbaikan, masing-masing hanya kalau isinya ada. Tiap entri ditulis",
            "\"scope: deskripsi\", atau deskripsi saja kalau tanpa scope. Commit feat",
            "yang merusak muncul di dua kelompok. Commit yang judulnya nggak sesuai",
            "format, atau tipenya selain feat dan fix tanpa tanda merusak, dihitung",
            "sebagai lainnya.",
            "",
            "Contoh input:",
            "  1.4.2",
            "  ---",
            "  feat(kurir): dukung kurir instan",
            "  ---",
            "  fix: ongkir negatif untuk jarak 0",
            "  ---",
            "  docs: perbaiki contoh di README",
            "  ---",
            "  refactor(api)!: hapus endpoint /v1/harga",
            "  ---",
            "  feat: ekspor laporan ke CSV",
            "",
            "  BREAKING CHANGE: kolom total sekarang dalam rupiah penuh",
            "",
            "Keluaran yang diharapkan:",
            "versi sekarang: 1.4.2",
            "kenaikan: mayor",
            "versi berikutnya: 2.0.0",
            "merusak:",
            "- api: hapus endpoint /v1/harga",
            "- ekspor laporan ke CSV",
            "fitur:",
            "- kurir: dukung kurir instan",
            "- ekspor laporan ke CSV",
            "perbaikan:",
            "- ongkir negatif untuk jarak 0",
            "lainnya: 1 commit",
            "",
            "Contoh input kedua:",
            "  0.3.1",
            "  ---",
            "  feat!: ganti nama fungsi hitung() jadi hitung_ongkir()",
            "  ---",
            "  fix(kurir): tarif kurir instan dibulatkan ke ratusan",
            "  ---",
            "  chore: perbarui dependensi",
            "",
            "Untuk input 0.3.1, keluarannya:",
            "versi sekarang: 0.3.1",
            "kenaikan: minor (perubahan merusak di versi 0.x)",
            "versi berikutnya: 0.4.0",
            "merusak:",
            "- ganti nama fungsi hitung() jadi hitung_ongkir()",
            "fitur:",
            "- ganti nama fungsi hitung() jadi hitung_ongkir()",
            "perbaikan:",
            "- kurir: tarif kurir instan dibulatkan ke ratusan",
            "lainnya: 1 commit",
        ],
        "hints": [
            "Ingat tabel di materi Conventional Commits: feat menaikkan minor, fix menaikkan patch, dan tanda ! atau footer BREAKING CHANGE menaikkan mayor; kalau ada beberapa commit, kenaikan terbesar yang menang.",
            "Pecah input dengan re.split di baris ---, cocokkan baris pertama tiap commit dengan regex yang menangkap tipe, scope, tanda !, dan deskripsi, lalu periksa baris sisanya untuk footer.",
            "Pola r\"^(\\w+)(?:\\(([\\w-]+)\\))?(!)?: (.+)$\" sudah cukup; simpan tiga daftar dan satu penghitung, lalu tentukan kenaikannya dengan if/elif dari yang paling besar, termasuk cabang khusus untuk versi 0.x.",
        ],
        "solution": "import re\nimport sys\n\nPOLA = re.compile(r\"^(\\w+)(?:\\(([\\w-]+)\\))?(!)?: (.+)$\")\n\nbagian = re.split(r\"^---$\", sys.stdin.read(), flags=re.MULTILINE)\nversi = [int(x) for x in bagian[0].strip().split(\".\")]\n\nmerusak, fitur, perbaikan = [], [], []\nlainnya = 0\nfor teks in bagian[1:]:\n    baris = teks.strip().splitlines()\n    cocok = POLA.match(baris[0]) if baris else None\n    if not cocok:\n        lainnya += 1\n        continue\n    tipe, scope, seru, deskripsi = cocok.groups()\n    entri = f\"{scope}: {deskripsi}\" if scope else deskripsi\n    rusak = seru == \"!\" or any(\n        b.startswith((\"BREAKING CHANGE:\", \"BREAKING-CHANGE:\")) for b in baris[1:])\n    if rusak:\n        merusak.append(entri)\n    if tipe == \"feat\":\n        fitur.append(entri)\n    elif tipe == \"fix\":\n        perbaikan.append(entri)\n    elif not rusak:\n        lainnya += 1\n\nmayor, minor, patch = versi\nif merusak and mayor > 0:\n    kenaikan, baru = \"mayor\", (mayor + 1, 0, 0)\nelif merusak:\n    kenaikan, baru = \"minor (perubahan merusak di versi 0.x)\", (0, minor + 1, 0)\nelif fitur:\n    kenaikan, baru = \"minor\", (mayor, minor + 1, 0)\nelif perbaikan:\n    kenaikan, baru = \"patch\", (mayor, minor, patch + 1)\nelse:\n    kenaikan, baru = \"tidak ada\", None\n\nlama = \".\".join(map(str, versi))\nprint(\"versi sekarang:\", lama)\nprint(\"kenaikan:\", kenaikan)\nif baru:\n    print(\"versi berikutnya:\", \".\".join(map(str, baru)))\nelse:\n    print(\"versi berikutnya:\", lama, \"(tidak ada rilis)\")\nfor judul, isi in ((\"merusak\", merusak), (\"fitur\", fitur),\n                   (\"perbaikan\", perbaikan)):\n    if isi:\n        print(f\"{judul}:\")\n        for entri in isi:\n            print(\"-\", entri)\nprint(f\"lainnya: {lainnya} commit\")",
        "stdin_list": [
            """1.4.2
---
feat(kurir): dukung kurir instan
---
fix: ongkir negatif untuk jarak 0
---
docs: perbaiki contoh di README
---
refactor(api)!: hapus endpoint /v1/harga
---
feat: ekspor laporan ke CSV

BREAKING CHANGE: kolom total sekarang dalam rupiah penuh
""",
            """0.3.1
---
feat!: ganti nama fungsi hitung() jadi hitung_ongkir()
---
fix(kurir): tarif kurir instan dibulatkan ke ratusan
---
chore: perbarui dependensi
""",
            """2.1.0
---
docs: tambah contoh pemakaian
---
ci: jalankan tes di Python 3.14
---
perbaikan typo di README
""",
        ],
    },
    {
        "title": "Latihan 8: Pipeline Pipes and Filters",
        "difficulty": "Menengah",
        "question": [
            "Bangun pipeline pengolah log yang urutan filternya dibaca dari input.",
            "Baris pertama input berisi nama filter, dipisah spasi, dengan urai",
            "selalu di depan. Baris sisanya adalah log berbentuk \"waktu LEVEL layanan",
            "pesan...\".",
            "",
            "Empat filter yang harus ada, semuanya berupa generator:",
            "  - urai: mengubah tiap baris jadi catatan berisi waktu, level, layanan,",
            "    dan pesan. Baris yang kurang dari empat bagian dibuang.",
            "  - saring_level: meneruskan catatan berlevel WARN atau ERROR saja.",
            "  - sensor_email: mengganti setiap kata di pesan yang memuat @ dengan",
            "    [email].",
            "  - hitung_layanan: menghabiskan semua catatan yang masuk, lalu",
            "    mengeluarkan satu catatan per layanan, urut abjad, dengan waktu \"-\",",
            "    level RINGKAS, dan pesan \"N baris\".",
            "",
            "Cetak setiap catatan yang keluar dari ujung pipeline dengan format",
            "\"waktu LEVEL layanan: pesan\", lalu baris terakhir \"jumlah keluaran: N\".",
            "",
            "Contoh input:",
            "  urai saring_level sensor_email hitung_layanan",
            "  08:00 INFO pesanan dibuat oleh sari@contoh.id",
            "  08:01 ERROR pembayaran gagal untuk budi@contoh.id",
            "  08:02 WARN stok sisa 2 untuk buku",
            "  08:03 INFO stok diperbarui",
            "  08:04 ERROR pembayaran timeout dari bank",
            "  08:05 ERROR kurir tidak merespons",
            "  rusak",
            "  08:06 WARN pesanan alamat kurang lengkap",
            "",
            "Keluaran yang diharapkan:",
            "- RINGKAS kurir: 1 baris",
            "- RINGKAS pembayaran: 2 baris",
            "- RINGKAS pesanan: 1 baris",
            "- RINGKAS stok: 1 baris",
            "jumlah keluaran: 4",
            "",
            "Untuk input urai sensor_email saring_level, keluarannya:",
            "08:01 ERROR pembayaran: gagal untuk [email]",
            "08:02 WARN stok: sisa 2 untuk buku",
            "08:04 ERROR pembayaran: timeout dari bank",
            "08:05 ERROR kurir: tidak merespons",
            "08:06 WARN pesanan: alamat kurang lengkap",
            "jumlah keluaran: 5",
            "",
            "Urutan menentukan hasil. Dengan baris log yang sama, input \"urai",
            "hitung_layanan saring_level\" menghasilkan nol catatan, karena catatan",
            "RINGKAS dibuang saring_level.",
            "",
            "Untuk input urai hitung_layanan saring_level, keluarannya:",
            "jumlah keluaran: 0",
        ],
        "hints": [
            "Ingat contoh pipes and filters di materi: tiap filter adalah generator yang menerima aliran dari filter sebelumnya dan mengirim hasilnya ke filter berikutnya, jadi urutan menentukan hasil.",
            "Simpan keempat filter di dict yang memetakan nama ke fungsi, lalu bangun alirannya dengan memulai dari baris log dan membungkusnya berulang sesuai urutan nama di baris pertama.",
            "Polanya aliran = iter(baris_log), lalu for nama in urutan: aliran = FILTER[nama](aliran); hitung_layanan cukup mengumpulkan jumlah per layanan di dict, lalu yield satu catatan RINGKAS per layanan menurut sorted().",
        ],
        "solution": """import sys


def urai(baris):
    for b in baris:
        bagian = b.split(maxsplit=3)
        if len(bagian) < 4:
            continue                      # baris rusak dibuang
        waktu, level, layanan, pesan = bagian
        yield {"waktu": waktu, "level": level, "layanan": layanan,
               "pesan": pesan}


def saring_level(catatan):
    for c in catatan:
        if c["level"] in ("WARN", "ERROR"):
            yield c


def sensor_email(catatan):
    for c in catatan:
        kata = ["[email]" if "@" in k else k for k in c["pesan"].split()]
        yield {**c, "pesan": " ".join(kata)}


def hitung_layanan(catatan):
    jumlah = {}
    for c in catatan:
        jumlah[c["layanan"]] = jumlah.get(c["layanan"], 0) + 1
    for layanan in sorted(jumlah):
        yield {"waktu": "-", "level": "RINGKAS", "layanan": layanan,
               "pesan": f"{jumlah[layanan]} baris"}


FILTER = {"urai": urai, "saring_level": saring_level,
          "sensor_email": sensor_email, "hitung_layanan": hitung_layanan}

baris = sys.stdin.read().splitlines()
aliran = iter(baris[1:])
for nama in baris[0].split():
    aliran = FILTER[nama](aliran)

n = 0
for c in aliran:
    print(f"{c['waktu']} {c['level']} {c['layanan']}: {c['pesan']}")
    n += 1
print("jumlah keluaran:", n)""",
        "stdin_list": [
            """urai saring_level sensor_email hitung_layanan
08:00 INFO pesanan dibuat oleh sari@contoh.id
08:01 ERROR pembayaran gagal untuk budi@contoh.id
08:02 WARN stok sisa 2 untuk buku
08:03 INFO stok diperbarui
08:04 ERROR pembayaran timeout dari bank
08:05 ERROR kurir tidak merespons
rusak
08:06 WARN pesanan alamat kurang lengkap
""",
            """urai sensor_email saring_level
08:00 INFO pesanan dibuat oleh sari@contoh.id
08:01 ERROR pembayaran gagal untuk budi@contoh.id
08:02 WARN stok sisa 2 untuk buku
08:03 INFO stok diperbarui
08:04 ERROR pembayaran timeout dari bank
08:05 ERROR kurir tidak merespons
rusak
08:06 WARN pesanan alamat kurang lengkap
""",
            """urai hitung_layanan
08:00 INFO pesanan dibuat oleh sari@contoh.id
08:01 ERROR pembayaran gagal untuk budi@contoh.id
08:02 WARN stok sisa 2 untuk buku
08:03 INFO stok diperbarui
08:04 ERROR pembayaran timeout dari bank
08:05 ERROR kurir tidak merespons
rusak
08:06 WARN pesanan alamat kurang lengkap
""",
            """urai hitung_layanan saring_level
08:00 INFO pesanan dibuat oleh sari@contoh.id
08:01 ERROR pembayaran gagal untuk budi@contoh.id
08:02 WARN stok sisa 2 untuk buku
08:03 INFO stok diperbarui
08:04 ERROR pembayaran timeout dari bank
08:05 ERROR kurir tidak merespons
rusak
08:06 WARN pesanan alamat kurang lengkap
""",
        ],
    },
    {
        "title": "Latihan 9: Simulasi Load Balancer",
        "difficulty": "Lanjut",
        "question": [
            "Tiru keputusan sebuah load balancer. Baris pertama input berisi nama",
            "algoritma: round_robin, weighted, atau least_conn. Baris kedua berisi",
            "jumlah server N. N baris berikutnya berisi nama, bobot, dan status",
            "(sehat atau mati) tiap server. Sisanya satu request per baris: waktu",
            "tiba t dan durasi, keduanya bilangan bulat.",
            "",
            "Aturan tiap algoritma, hanya untuk server yang sehat:",
            "  - round_robin: server sehat dipakai bergiliran sesuai urutan daftar,",
            "    mulai dari yang pertama.",
            "  - weighted: smooth weighted round-robin seperti di Nginx. Setiap",
            "    server punya bobot_kini yang mulai dari 0. Untuk setiap request,",
            "    tambahkan bobot ke bobot_kini semua server sehat, pilih bobot_kini",
            "    terbesar, lalu kurangi bobot_kini server terpilih dengan total bobot",
            "    server sehat.",
            "  - least_conn: pilih server dengan koneksi aktif paling sedikit.",
            "    Koneksi aktif pada waktu t adalah request di server itu yang waktu",
            "    selesainya (waktu tiba + durasi) lebih besar dari t.",
            "  - Kalau ada yang seri, menangkan server yang lebih dulu di daftar.",
            "    Kalau semua server mati, request dijawab 503.",
            "",
            "Cetak satu baris per request, lalu jumlah request tiap server sesuai",
            "urutan daftar. Server yang mati diberi tanda (mati).",
            "",
            "Contoh input:",
            "  weighted",
            "  4",
            "  A 3 sehat",
            "  B 1 sehat",
            "  C 1 sehat",
            "  D 2 mati",
            "  0 5",
            "  1 5",
            "  2 5",
            "  3 5",
            "  4 5",
            "  5 5",
            "  6 5",
            "",
            "Keluaran yang diharapkan:",
            "t=0 -> A",
            "t=1 -> B",
            "t=2 -> A",
            "t=3 -> C",
            "t=4 -> A",
            "t=5 -> A",
            "t=6 -> B",
            "A: 4 request",
            "B: 2 request",
            "C: 1 request",
            "D: 0 request (mati)",
            "",
            "Contoh input kedua:",
            "  least_conn",
            "  3",
            "  A 1 sehat",
            "  B 1 sehat",
            "  C 1 sehat",
            "  0 10",
            "  1 2",
            "  2 5",
            "  4 1",
            "  5 3",
            "  8 2",
            "",
            "Untuk input least_conn, keluarannya:",
            "t=0 -> A",
            "t=1 -> B",
            "t=2 -> C",
            "t=4 -> B",
            "t=5 -> B",
            "t=8 -> B",
            "A: 1 request",
            "B: 4 request",
            "C: 1 request",
        ],
        "hints": [
            "Baca lagi daftar algoritma di materi Load Balancer dan Reverse Proxy: round-robin bergiliran, weighted memberi jatah sesuai bobot, dan least connections memilih server yang paling sepi.",
            "Simpan tiap server sebagai dict berisi nama, bobot, status, bobot_kini, dan daftar waktu selesai request-nya, lalu tulis satu fungsi pilih(t) yang bercabang menurut algoritma dan cuma melihat server yang sehat.",
            "Untuk weighted, tambahkan bobot ke bobot_kini semua server sehat, ambil max() (yang pertama menang kalau seri), lalu kurangi bobot_kini pemenangnya dengan total bobot; untuk least_conn, buang waktu selesai yang <= t lalu ambil min() menurut panjang daftarnya.",
        ],
        "solution": """import sys

baris = [b.split() for b in sys.stdin.read().splitlines() if b.strip()]
algoritma = baris[0][0]
n = int(baris[1][0])
server = []
for nama, bobot, status in baris[2:2 + n]:
    server.append({"nama": nama, "bobot": int(bobot),
                   "sehat": status == "sehat", "bobot_kini": 0,
                   "selesai": [], "jumlah": 0})
sehat = [s for s in server if s["sehat"]]
giliran = 0


def pilih(t):
    global giliran
    if not sehat:
        return None
    if algoritma == "round_robin":
        s = sehat[giliran % len(sehat)]
        giliran += 1
        return s
    if algoritma == "weighted":
        total = sum(s["bobot"] for s in sehat)
        for s in sehat:
            s["bobot_kini"] += s["bobot"]
        terpilih = max(sehat, key=lambda s: s["bobot_kini"])
        terpilih["bobot_kini"] -= total
        return terpilih
    # least_conn: koneksi aktif = request yang belum selesai pada waktu t
    for s in sehat:
        s["selesai"] = [akhir for akhir in s["selesai"] if akhir > t]
    return min(sehat, key=lambda s: len(s["selesai"]))


for t, durasi in baris[2 + n:]:
    t, durasi = int(t), int(durasi)
    s = pilih(t)
    if s is None:
        print(f"t={t} -> 503, semua server mati")
        continue
    s["selesai"].append(t + durasi)
    s["jumlah"] += 1
    print(f"t={t} -> {s['nama']}")

for s in server:
    catatan = "" if s["sehat"] else " (mati)"
    print(f"{s['nama']}: {s['jumlah']} request{catatan}")""",
        "stdin_list": [
            """weighted
4
A 3 sehat
B 1 sehat
C 1 sehat
D 2 mati
0 5
1 5
2 5
3 5
4 5
5 5
6 5
""",
            """least_conn
3
A 1 sehat
B 1 sehat
C 1 sehat
0 10
1 2
2 5
4 1
5 3
8 2
""",
            """round_robin
3
A 1 sehat
B 1 mati
C 1 sehat
0 1
1 1
2 1
3 1
4 1
""",
            """round_robin
2
A 1 mati
B 1 mati
0 1
""",
        ],
    },
    {
        "title": "Latihan 10: LRU Cache dengan Kapasitas Tetap",
        "difficulty": "Lanjut",
        "question": [
            "Bangun cache LRU. Baris pertama input berisi kapasitas. Baris berikutnya",
            "berisi operasi GET kunci atau PUT kunci nilai.",
            "",
            "Aturannya:",
            "  - GET kunci yang ada mencetak HIT beserta nilainya dan menjadikan",
            "    kunci itu paling baru. Kalau nggak ada, cetak MISS.",
            "  - PUT kunci baru menambahkannya sebagai yang paling baru. Kalau isi",
            "    cache jadi melebihi kapasitas, keluarkan kunci yang paling lama",
            "    nggak dipakai dan sebutkan namanya.",
            "  - PUT kunci yang sudah ada mengganti nilainya, menjadikannya paling",
            "    baru, dan ditandai (diperbarui).",
            "  - Di akhir, cetak isi cache dari yang paling lama ke yang paling baru,",
            "    lalu jumlah hit dan miss.",
            "",
            "Contoh input:",
            "  3",
            "  PUT pena 5000",
            "  PUT buku 12000",
            "  PUT map 3000",
            "  GET pena",
            "  PUT tas 85000",
            "  GET buku",
            "  GET map",
            "  PUT pena 5500",
            "  GET pena",
            "  PUT spidol 9000",
            "  GET tas",
            "",
            "Keluaran yang diharapkan:",
            "PUT pena",
            "PUT buku",
            "PUT map",
            "GET pena -> HIT 5000",
            "PUT tas (keluar: buku)",
            "GET buku -> MISS",
            "GET map -> HIT 3000",
            "PUT pena (diperbarui)",
            "GET pena -> HIT 5500",
            "PUT spidol (keluar: tas)",
            "GET tas -> MISS",
            "isi (lama -> baru): map, pena, spidol",
            "hit: 3, miss: 2",
        ],
        "hints": [
            "Ingat urutan LRU di materi Caching dan CDN: setiap kunci yang dibaca atau ditulis pindah ke posisi paling baru, dan yang dikeluarkan selalu yang paling lama nggak disentuh.",
            "collections.OrderedDict mengingat urutan kunci, punya move_to_end() untuk memindahkan kunci ke ujung, dan popitem(last=False) untuk membuang kunci yang paling lama.",
            "Kalau ingin tanpa OrderedDict, gabungkan dict biasa untuk mencari kunci dengan daftar tertaut ganda untuk menyimpan urutan; dengan OrderedDict, cukup cek kunci, panggil move_to_end(), dan panggil popitem(last=False) saat len(cache) > kapasitas.",
        ],
        "solution": """import sys
from collections import OrderedDict

baris = sys.stdin.read().splitlines()
kapasitas = int(baris[0])
cache = OrderedDict()
hit = miss = 0

for b in baris[1:]:
    bagian = b.split()
    if not bagian:
        continue
    if bagian[0] == "GET":
        kunci = bagian[1]
        if kunci in cache:
            cache.move_to_end(kunci)
            hit += 1
            print(f"GET {kunci} -> HIT {cache[kunci]}")
        else:
            miss += 1
            print(f"GET {kunci} -> MISS")
    elif bagian[0] == "PUT":
        kunci, nilai = bagian[1], bagian[2]
        if kunci in cache:
            cache[kunci] = nilai
            cache.move_to_end(kunci)
            print(f"PUT {kunci} (diperbarui)")
            continue
        cache[kunci] = nilai
        if len(cache) > kapasitas:
            keluar, _ = cache.popitem(last=False)
            print(f"PUT {kunci} (keluar: {keluar})")
        else:
            print(f"PUT {kunci}")

print("isi (lama -> baru):", ", ".join(cache) if cache else "(kosong)")
print(f"hit: {hit}, miss: {miss}")""",
        "stdin_list": [
            """3
PUT pena 5000
PUT buku 12000
PUT map 3000
GET pena
PUT tas 85000
GET buku
GET map
PUT pena 5500
GET pena
PUT spidol 9000
GET tas
""",
            """1
GET x
PUT x 1
PUT y 2
GET x
GET y
""",
        ],
    },
    {
        "title": "Latihan 11: Consistent Hashing untuk Pembagian Shard",
        "difficulty": "Lanjut",
        "question": [
            "Bangun ring consistent hashing kecil, lalu bandingkan berapa kunci",
            "yang pindah saat satu node ditambah, dibandingkan cara mod N.",
            "",
            "Input (stdin), empat baris:",
            "  baris 1: nama node awal, dipisah spasi",
            "  baris 2: nama node baru",
            "  baris 3: banyak node virtual per node",
            "  baris 4: banyak kunci n; kuncinya user-1, user-2, ..., user-n",
            "",
            "Aturan:",
            "  - Hash sebuah teks = int(hashlib.md5(teks.encode()).hexdigest(), 16).",
            "  - Node virtual ke-i milik node X ditaruh di posisi hash(\"X#i\"),",
            "    dengan i mulai dari 0.",
            "  - Pemilik kunci adalah node virtual pertama yang posisinya >= hash",
            "    kunci. Kalau tidak ada, putar ke posisi terkecil.",
            "  - Cara mod N: kunci masuk node ke-(hash % banyak node) menurut",
            "    urutan daftar node. Node baru selalu di urutan terakhir.",
            "",
            "Cetak sebaran ring sebelum dan sesudah node baru masuk (urutan node",
            "sesuai input), lalu berapa kunci yang pindah dengan ring dan dengan",
            "mod N.",
            "",
            "Untuk input db-a db-b db-c, keluarannya:",
            "Ring dengan 3 node:",
            "  db-a: 13",
            "  db-b: 12",
            "  db-c: 15",
            "Ring sesudah db-d masuk:",
            "  db-a: 11",
            "  db-b: 10",
            "  db-c: 12",
            "  db-d: 7",
            "Pindah dengan ring: 7 dari 40",
            "Pindah dengan mod N: 34 dari 40",
            "",
            "(Input lengkapnya: db-a db-b db-c, lalu db-d, lalu 40, lalu 40.)",
        ],
        "hints": [
            "Ring itu daftar pasangan (posisi, nama node) yang diurutkan menurut posisi, dan mencari pemilik kunci berarti mencari posisi pertama yang tidak lebih kecil dari hash kunci.",
            "Buat dua ring (sebelum dan sesudah), tentukan pemilik tiap kunci di keduanya, lalu hitung kunci yang pemiliknya berbeda; lakukan hal yang sama untuk mod 3 dan mod 4.",
            "Modul bisect membantu mencari posisinya: i = bisect.bisect_left(daftar_posisi, hash_kunci), dan kalau i sama dengan panjang ring, pakai i = 0.",
        ],
        "solution": "import bisect\nimport hashlib\nimport sys\n\n\ndef angka_hash(teks):\n    return int(hashlib.md5(teks.encode()).hexdigest(), 16)\n\n\ndef buat_ring(node, virtual):\n    ring = []\n    for n in node:\n        for i in range(virtual):\n            ring.append((angka_hash(f\"{n}#{i}\"), n))\n    ring.sort()\n    return ring\n\n\ndef cari_node(ring, kunci):\n    posisi = [p for p, _ in ring]\n    i = bisect.bisect_left(posisi, angka_hash(kunci))\n    if i == len(ring):\n        i = 0\n    return ring[i][1]\n\n\ndef cetak_sebaran(judul, node, peta):\n    print(judul)\n    for n in node:\n        jumlah = sum(1 for v in peta.values() if v == n)\n        print(f\"  {n}: {jumlah}\")\n\n\nbaris = sys.stdin.read().split(\"\\n\")\nnode_awal = baris[0].split()\nnode_baru = baris[1].strip()\nvirtual = int(baris[2])\nbanyak = int(baris[3])\nkunci = [f\"user-{i}\" for i in range(1, banyak + 1)]\nnode_akhir = node_awal + [node_baru]\n\nring_awal = buat_ring(node_awal, virtual)\nring_akhir = buat_ring(node_akhir, virtual)\nsebelum = {k: cari_node(ring_awal, k) for k in kunci}\nsesudah = {k: cari_node(ring_akhir, k) for k in kunci}\n\ncetak_sebaran(f\"Ring dengan {len(node_awal)} node:\", node_awal, sebelum)\ncetak_sebaran(f\"Ring sesudah {node_baru} masuk:\", node_akhir, sesudah)\n\npindah_ring = sum(1 for k in kunci if sebelum[k] != sesudah[k])\npindah_mod = sum(1 for k in kunci\n                 if angka_hash(k) % len(node_awal) != angka_hash(k) % len(node_akhir))\nprint(f\"Pindah dengan ring: {pindah_ring} dari {banyak}\")\nprint(f\"Pindah dengan mod N: {pindah_mod} dari {banyak}\")\n",
        "stdin_list": [
            """db-a db-b db-c
db-d
40
40
""",
            """shard-1 shard-2
shard-3
50
12
""",
        ],
    },
    {
        "title": "Latihan 12: Rate Limiter Token Bucket dengan Jam Palsu",
        "difficulty": "Lanjut",
        "question": [
            "Buat rate limiter token bucket dengan satu ember per klien. Waktu",
            "berupa jam palsu dalam milidetik yang dibaca dari input.",
            "",
            "Input (stdin):",
            "  baris 1: kapasitas ember dan laju isi ulang (token per detik)",
            "  baris berikutnya: waktu_ms nama_klien, urut menurut waktu",
            "",
            "Aturan:",
            "  - Ember klien baru dibuat penuh saat permintaan pertamanya datang.",
            "  - Sebelum memutuskan, ember diisi ulang sesuai waktu yang lewat",
            "    sejak permintaan terakhir klien itu, tapi tidak melebihi",
            "    kapasitas.",
            "  - Satu permintaan butuh satu token. Kalau cukup, IZINKAN dan",
            "    kurangi satu token. Kalau kurang, TOLAK dan cetak tunggu, yaitu",
            "    milidetik sampai satu token terkumpul, dibulatkan ke atas.",
            "  - Supaya tidak ada pecahan float, simpan token dalam satuan mili:",
            "    1 token = 1000. Laju L token per detik = L mili-token per ms.",
            "  - Cetak sisa dengan tiga angka di belakang titik.",
            "",
            "Sesudah semua kejadian, cetak ringkasan per klien urut abjad.",
            "",
            "Untuk input 3 2, keluarannya:",
            "t=0 ani IZINKAN sisa=2.000",
            "t=0 ani IZINKAN sisa=1.000",
            "t=100 ani IZINKAN sisa=0.200",
            "t=200 ani TOLAK sisa=0.400 tunggu=300ms",
            "t=200 budi IZINKAN sisa=2.000",
            "t=400 ani TOLAK sisa=0.800 tunggu=100ms",
            "t=900 ani IZINKAN sisa=0.800",
            "t=2000 ani IZINKAN sisa=2.000",
            "Ringkasan:",
            "  ani: 5 izinkan, 2 tolak",
            "  budi: 1 izinkan, 0 tolak",
            "",
            "(Baris input sesudah \"3 2\": 0 ani, 0 ani, 100 ani, 200 ani,",
            "200 budi, 400 ani, 900 ani, 2000 ani.)",
        ],
        "hints": [
            "Tiap klien cukup diingat dengan dua angka, yaitu isi ember dan waktu permintaan terakhirnya, dan isi ulang dihitung dari selisih waktu dikali laju.",
            "Urutannya selalu sama untuk tiap baris: isi ulang dulu (dibatasi kapasitas), baru periksa apakah isi ember minimal 1000 mili-token.",
            "Untuk waktu tunggu, kekurangan token adalah 1000 - sisa, dan pembulatan ke atas bisa ditulis (kurang + laju - 1) // laju.",
        ],
        "solution": "import sys\n\nbaris = [b for b in sys.stdin.read().split(\"\\n\") if b.strip()]\nkapasitas, laju = map(int, baris[0].split())\npenuh = kapasitas * 1000          # token disimpan dalam satuan mili\nember = {}                        # klien -> [sisa_mili, waktu_terakhir]\nhitung = {}                       # klien -> [izinkan, tolak]\n\nfor b in baris[1:]:\n    t, klien = b.split()\n    t = int(t)\n    if klien not in ember:\n        ember[klien] = [penuh, t]\n        hitung[klien] = [0, 0]\n    sisa, terakhir = ember[klien]\n    sisa = min(penuh, sisa + (t - terakhir) * laju)\n    if sisa >= 1000:\n        sisa -= 1000\n        hitung[klien][0] += 1\n        hasil = \"IZINKAN\"\n        tambahan = \"\"\n    else:\n        hitung[klien][1] += 1\n        kurang = 1000 - sisa\n        tunggu = (kurang + laju - 1) // laju\n        hasil = \"TOLAK\"\n        tambahan = f\" tunggu={tunggu}ms\"\n    ember[klien] = [sisa, t]\n    print(f\"t={t} {klien} {hasil} sisa={sisa // 1000}.{sisa % 1000:03d}{tambahan}\")\n\nprint(\"Ringkasan:\")\nfor klien in sorted(hitung):\n    izin, tolak = hitung[klien]\n    print(f\"  {klien}: {izin} izinkan, {tolak} tolak\")\n",
        "stdin_list": [
            """3 2
0 ani
0 ani
100 ani
200 ani
200 budi
400 ani
900 ani
2000 ani
""",
            """1 1
0 api-key-1
300 api-key-1
1000 api-key-1
1000 api-key-2
1500 api-key-1
""",
        ],
    },
    {
        "title": "Latihan 13: Antrean Pesan dengan Retry",
        "difficulty": "Lanjut",
        "question": [
            "Buat simulasi konsumen antrean pesan dengan percobaan ulang,",
            "dead-letter queue (DLQ), dan pembuangan pesan ganda.",
            "",
            "Input (stdin): satu pesan per baris, berbentuk",
            "  waktu id pola",
            "Pola berisi huruf S (sukses) atau G (gagal). Huruf ke-i adalah hasil",
            "percobaan ke-i. Kalau polanya habis, pakai huruf terakhir.",
            "",
            "Aturan:",
            "  - Semua pesan input masuk antrean lebih dulu, sesuai urutan baris.",
            "  - Kejadian diproses urut waktu. Kalau waktunya sama, yang lebih",
            "    dulu masuk antrean diproses lebih dulu.",
            "  - Percobaan gagal dijadwalkan ulang dengan jeda 1, 2, lalu 4",
            "    satuan waktu. Percobaan ulang masuk antrean saat dijadwalkan.",
            "  - Kalau percobaan ke-4 juga gagal, pesan masuk DLQ.",
            "  - Pesan dengan id yang sudah pernah diterima dilewati",
            "    (idempotensi), walaupun pesan pertamanya belum selesai.",
            "",
            "Format tiap baris keluaran:",
            "  t=W ID percobaan K: sukses",
            "  t=W ID percobaan K: gagal, ulang di t=W2",
            "  t=W ID percobaan K: gagal, masuk DLQ",
            "  t=W ID duplikat, dilewati",
            "Lalu ringkasan Selesai, DLQ (pakai - kalau kosong), dan jumlah",
            "duplikat. Urutan id di ringkasan mengikuti urutan kejadiannya.",
            "",
            "Untuk input 0 m1 S, keluarannya:",
            "t=0 m1 percobaan 1: sukses",
            "t=0 m2 percobaan 1: gagal, ulang di t=1",
            "t=1 m3 percobaan 1: gagal, ulang di t=2",
            "t=1 m2 percobaan 2: gagal, ulang di t=3",
            "t=2 m2 duplikat, dilewati",
            "t=2 m3 percobaan 2: gagal, ulang di t=4",
            "t=3 m4 percobaan 1: gagal, ulang di t=4",
            "t=3 m2 percobaan 3: sukses",
            "t=4 m3 percobaan 3: gagal, ulang di t=8",
            "t=4 m4 percobaan 2: sukses",
            "t=8 m3 percobaan 4: gagal, masuk DLQ",
            "Selesai: m1 m2 m4",
            "DLQ: m3",
            "Duplikat dilewati: 1",
            "",
            "(Input lengkapnya lima baris: 0 m1 S, 0 m2 GGS, 1 m3 GGGG,",
            "2 m2 S, 3 m4 GS.)",
        ],
        "hints": [
            "Antrean yang diurutkan menurut waktu lalu urutan masuk adalah antrean prioritas, dan pasangan (waktu, nomor_masuk) cocok jadi kunci urutannya.",
            "Simpan himpunan id yang sudah pernah diterima, dan periksa id hanya pada percobaan pertama, karena percobaan ulang memang id yang sama.",
            "Modul heapq menyimpan tuple (waktu, nomor, id, pola, percobaan); naikkan nomor setiap kali sesuatu dimasukkan ke heap.",
        ],
        "solution": "import heapq\nimport sys\n\nJEDA = [1, 2, 4]          # jeda sebelum percobaan ulang ke-1, ke-2, ke-3\n\nantrean = []              # isi: (waktu, nomor_masuk, id, pola, percobaan)\nnomor = 0\nfor b in sys.stdin.read().split(\"\\n\"):\n    if not b.strip():\n        continue\n    t, pid, pola = b.split()\n    heapq.heappush(antrean, (int(t), nomor, pid, pola, 1))\n    nomor += 1\n\npernah = set()\nselesai, dlq = [], []\ndilewati = 0\nwhile antrean:\n    t, _, pid, pola, ke = heapq.heappop(antrean)\n    if ke == 1:\n        if pid in pernah:\n            print(f\"t={t} {pid} duplikat, dilewati\")\n            dilewati += 1\n            continue\n        pernah.add(pid)\n    hasil = pola[ke - 1] if ke <= len(pola) else pola[-1]\n    if hasil == \"S\":\n        print(f\"t={t} {pid} percobaan {ke}: sukses\")\n        selesai.append(pid)\n    elif ke <= len(JEDA):\n        ulang = t + JEDA[ke - 1]\n        print(f\"t={t} {pid} percobaan {ke}: gagal, ulang di t={ulang}\")\n        heapq.heappush(antrean, (ulang, nomor, pid, pola, ke + 1))\n        nomor += 1\n    else:\n        print(f\"t={t} {pid} percobaan {ke}: gagal, masuk DLQ\")\n        dlq.append(pid)\n\nprint(\"Selesai:\", \" \".join(selesai) if selesai else \"-\")\nprint(\"DLQ:\", \" \".join(dlq) if dlq else \"-\")\nprint(f\"Duplikat dilewati: {dilewati}\")\n",
        "stdin_list": [
            """0 m1 S
0 m2 GGS
1 m3 GGGG
2 m2 S
3 m4 GS
""",
            """0 email-1 GS
0 email-2 S
0 email-1 S
5 email-3 G
""",
        ],
    },
    {
        "title": "Latihan 14: Circuit Breaker Tiga Keadaan",
        "difficulty": "Lanjut",
        "question": [
            "Buat circuit breaker dengan tiga keadaan: CLOSED, OPEN, HALF_OPEN.",
            "",
            "Input (stdin):",
            "  baris 1: ambang (gagal beruntun) dan masa tunggu",
            "  baris berikutnya: waktu hasil, dengan hasil SUKSES atau GAGAL,",
            "  yaitu jawaban layanan tujuan kalau panggilan itu diteruskan",
            "",
            "Aturan:",
            "  - CLOSED: panggilan diteruskan. GAGAL menambah hitungan gagal",
            "    beruntun, SUKSES mengembalikannya ke 0. Kalau hitungan mencapai",
            "    ambang, breaker jadi OPEN sejak waktu itu.",
            "  - OPEN: kalau waktu sekarang dikurangi waktu dibuka masih kurang",
            "    dari masa tunggu, panggilan ditolak tanpa diteruskan. Kalau",
            "    sudah tidak kurang, breaker jadi HALF_OPEN dan panggilan itu",
            "    diteruskan sebagai uji.",
            "  - HALF_OPEN: SUKSES membuat breaker CLOSED dengan hitungan 0.",
            "    GAGAL membuatnya OPEN lagi sejak waktu itu.",
            "",
            "Format keluaran (keadaan yang dicetak adalah keadaan saat",
            "keputusan diambil):",
            "  t=W OPEN ditolak",
            "  t=W CLOSED diteruskan HASIL gagal=N",
            "  t=W CLOSED diteruskan HASIL gagal=N -> OPEN",
            "  t=W HALF_OPEN diteruskan HASIL -> KEADAAN_BARU",
            "Terakhir: Ringkasan: diteruskan X, ditolak Y",
            "",
            "Untuk input 3 5, keluarannya:",
            "t=0 CLOSED diteruskan GAGAL gagal=1",
            "t=1 CLOSED diteruskan SUKSES gagal=0",
            "t=2 CLOSED diteruskan GAGAL gagal=1",
            "t=3 CLOSED diteruskan GAGAL gagal=2",
            "t=4 CLOSED diteruskan GAGAL gagal=3 -> OPEN",
            "t=6 OPEN ditolak",
            "t=8 OPEN ditolak",
            "t=9 HALF_OPEN diteruskan GAGAL -> OPEN",
            "t=11 OPEN ditolak",
            "t=14 HALF_OPEN diteruskan SUKSES -> CLOSED",
            "t=15 CLOSED diteruskan GAGAL gagal=1",
            "Ringkasan: diteruskan 8, ditolak 3",
            "",
            "(Baris input sesudah \"3 5\": 0 GAGAL, 1 SUKSES, 2 GAGAL, 3 GAGAL,",
            "4 GAGAL, 6 SUKSES, 8 GAGAL, 9 GAGAL, 11 SUKSES, 14 SUKSES,",
            "15 GAGAL.)",
        ],
        "hints": [
            "Keadaan breaker cukup diwakili tiga variabel: nama keadaan, jumlah gagal beruntun, dan waktu terakhir breaker dibuka.",
            "Untuk tiap baris, tangani OPEN lebih dulu: tolak kalau masa tunggu belum habis, atau ubah jadi HALF_OPEN lalu lanjutkan seperti panggilan yang diteruskan.",
            "Pisahkan cabang HALF_OPEN dari cabang CLOSED, karena HALF_OPEN langsung pindah keadaan berdasarkan satu hasil, sedangkan CLOSED menghitung gagal beruntun dulu.",
        ],
        "solution": "import sys\n\nbaris = [b for b in sys.stdin.read().split(\"\\n\") if b.strip()]\nambang, tunggu = map(int, baris[0].split())\n\nkeadaan = \"CLOSED\"\ngagal = 0\ndibuka = 0\nditeruskan = ditolak = 0\n\nfor b in baris[1:]:\n    t, hasil = b.split()\n    t = int(t)\n    if keadaan == \"OPEN\":\n        if t - dibuka < tunggu:\n            print(f\"t={t} OPEN ditolak\")\n            ditolak += 1\n            continue\n        keadaan = \"HALF_OPEN\"\n\n    diteruskan += 1\n    awal = keadaan\n    if keadaan == \"HALF_OPEN\":\n        if hasil == \"SUKSES\":\n            keadaan, gagal = \"CLOSED\", 0\n        else:\n            keadaan, dibuka = \"OPEN\", t\n        print(f\"t={t} {awal} diteruskan {hasil} -> {keadaan}\")\n        continue\n\n    if hasil == \"SUKSES\":\n        gagal = 0\n    else:\n        gagal += 1\n    pesan = f\"t={t} CLOSED diteruskan {hasil} gagal={gagal}\"\n    if gagal >= ambang:\n        keadaan, dibuka = \"OPEN\", t\n        pesan += \" -> OPEN\"\n    print(pesan)\n\nprint(f\"Ringkasan: diteruskan {diteruskan}, ditolak {ditolak}\")\n",
        "stdin_list": [
            """3 5
0 GAGAL
1 SUKSES
2 GAGAL
3 GAGAL
4 GAGAL
6 SUKSES
8 GAGAL
9 GAGAL
11 SUKSES
14 SUKSES
15 GAGAL
""",
            """2 10
0 GAGAL
5 GAGAL
6 SUKSES
15 SUKSES
16 GAGAL
""",
        ],
    },
    {
        "title": "Latihan 15: Penghitung SLO dan Error Budget",
        "difficulty": "Lanjut",
        "question": [
            "Hitung SLI, error budget, dan burn rate dari log permintaan, lalu",
            "cetak tabel waktu henti per bulan.",
            "",
            "Input (stdin):",
            "  baris 1: target SLO dalam persen, misalnya 99.5",
            "  baris berikutnya: menit kode_http jumlah",
            "",
            "Aturan:",
            "  - Permintaan gagal adalah yang kode HTTP-nya 500 ke atas. Kode",
            "    4xx dihitung sukses, karena itu kesalahan klien.",
            "  - SLI = (total - gagal) / total, dalam persen.",
            "  - Gagal yang diizinkan = total x (100 - target) / 100, dibulatkan",
            "    ke bawah.",
            "  - Sisa budget = diizinkan - gagal. Kalau negatif, cetak",
            "    \"habis, lewat N\".",
            "  - Burn rate = (gagal / total) dibagi ((100 - target) / 100).",
            "  - SLI dan burn rate dicetak dua angka di belakang titik,",
            "    dibulatkan setengah ke atas. Pakai fractions.Fraction supaya",
            "    tidak ada selisih float.",
            "  - Tabel waktu henti memakai bulan 30 hari, untuk 99, 99.9,",
            "    99.99, ditambah target input kalau belum ada, urut dari yang",
            "    terkecil. Detik dibulatkan ke bawah.",
            "",
            "Untuk input 99.5, keluarannya:",
            "Total request: 1192",
            "Gagal (5xx): 7",
            "SLI: 99.41%",
            "Target SLO: 99.5%",
            "Gagal yang diizinkan: 5",
            "Terpakai: 7",
            "Sisa budget: habis, lewat 2",
            "Burn rate: 1.17",
            "Waktu henti per bulan (30 hari):",
            "  99%: 7 jam 12 menit 0 detik",
            "  99.5%: 3 jam 36 menit 0 detik",
            "  99.9%: 0 jam 43 menit 12 detik",
            "  99.99%: 0 jam 4 menit 19 detik",
            "",
            "(Baris input sesudah 99.5: 1 200 300, 1 500 1, 2 200 280,",
            "2 503 2, 3 200 310, 3 404 5, 4 200 290, 4 500 4.)",
        ],
        "hints": [
            "Error budget adalah porsi kegagalan yang boleh terjadi, yaitu seratus persen dikurangi target SLO, dikalikan jumlah permintaan.",
            "Ubah teks target jadi Fraction (Fraction(\"99.5\") menghasilkan 199/2), hitung semuanya sebagai pecahan, dan baru ubah jadi teks saat dicetak.",
            "Pembulatan dua desimal setengah ke atas bisa ditulis x = (nilai * 100 + Fraction(1, 2)) // 1, lalu dicetak sebagai x // 100 dan x % 100 dengan dua digit.",
        ],
        "solution": "import sys\nfrom decimal import Decimal\nfrom fractions import Fraction\n\n\ndef dua_desimal(nilai):\n    \"\"\"Fraction tak negatif -> teks dua angka di belakang titik, dibulatkan.\"\"\"\n    x = (nilai * 100 + Fraction(1, 2)) // 1\n    return f\"{x // 100}.{x % 100:02d}\"\n\n\ndef lama(detik):\n    jam, sisa = divmod(detik, 3600)\n    menit, detik = divmod(sisa, 60)\n    return f\"{jam} jam {menit} menit {detik} detik\"\n\n\nbaris = [b for b in sys.stdin.read().split(\"\\n\") if b.strip()]\ntarget_teks = baris[0].strip()\ntarget = Fraction(target_teks)\njatah = (100 - target) / 100            # porsi request yang boleh gagal\n\ntotal = gagal = 0\nfor b in baris[1:]:\n    _menit, kode, jumlah = b.split()\n    total += int(jumlah)\n    if int(kode) >= 500:\n        gagal += int(jumlah)\n\nizin = int(total * jatah)               # dibulatkan ke bawah\nprint(f\"Total request: {total}\")\nprint(f\"Gagal (5xx): {gagal}\")\nprint(f\"SLI: {dua_desimal(Fraction(total - gagal, total) * 100)}%\")\nprint(f\"Target SLO: {target_teks}%\")\nprint(f\"Gagal yang diizinkan: {izin}\")\nprint(f\"Terpakai: {gagal}\")\nif gagal <= izin:\n    print(f\"Sisa budget: {izin - gagal}\")\nelse:\n    print(f\"Sisa budget: habis, lewat {gagal - izin}\")\nprint(f\"Burn rate: {dua_desimal(Fraction(gagal, total) / jatah)}\")\n\ndaftar = {\"99\": Decimal(\"99\"), \"99.9\": Decimal(\"99.9\"), \"99.99\": Decimal(\"99.99\")}\nif Decimal(target_teks) not in daftar.values():\n    daftar[target_teks] = Decimal(target_teks)\nprint(\"Waktu henti per bulan (30 hari):\")\nsebulan = 30 * 24 * 3600\nfor teks, nilai in sorted(daftar.items(), key=lambda p: p[1]):\n    boleh = int(sebulan * (100 - Fraction(teks)) / 100)\n    print(f\"  {teks}%: {lama(boleh)}\")\n",
        "stdin_list": [
            """99.5
1 200 300
1 500 1
2 200 280
2 503 2
3 200 310
3 404 5
4 200 290
4 500 4
""",
            """99.9
1 200 4000
1 502 1
2 200 3995
2 429 3
2 500 2
""",
        ],
    },
    {
        "title": "Latihan 16: Matriks Keputusan Pemilihan Stack",
        "difficulty": "Lanjut",
        "question": [
            "Buat program matriks keputusan yang menyingkirkan stack yang",
            "melanggar syarat wajib, lalu memberi peringkat sisanya.",
            "",
            "Input (stdin), tiap baris diawali jenisnya:",
            "  kriteria: nama=bobot nama=bobot ...",
            "  wajib: syarat syarat ...",
            "  stack: Nama syarat ... kriteria=skor kriteria=skor ...",
            "Di baris stack, kata pertama adalah nama. Kata tanpa tanda = adalah",
            "syarat yang dipenuhi stack itu. Skor 1 sampai 5; kriteria yang",
            "tidak diberi skor dianggap 0.",
            "",
            "Yang dicetak:",
            "  - Bobot total dan skor maksimal (bobot total x 5).",
            "  - Daftar Gugur, urut nama, beserta syarat wajib yang tidak",
            "    dipenuhi (dipisah koma, urut seperti di baris wajib). Kalau",
            "    tidak ada yang gugur, cetak \"  -\".",
            "  - Peringkat stack yang lolos menurut skor tertimbang, yaitu",
            "    jumlah bobot x skor. Skor sama diurut nama secara abjad.",
            "",
            "Untuk input kriteria: biaya=3 tim=5 ekosistem=4 skala=2, keluarannya:",
            "Bobot total: 14 (skor maksimal 70)",
            "Gugur:",
            "  Next.js+Firebase: tidak memenuhi hosting_sendiri",
            "Peringkat:",
            "  1. Django+PostgreSQL 57",
            "  2. Laravel+MySQL 57",
            "  3. Next.js+Supabase 55",
            "  4. Rails+PostgreSQL 49",
            "",
            "(Baris berikutnya di input itu: wajib: hosting_sendiri, lalu lima",
            "baris stack untuk Laravel+MySQL, Next.js+Firebase,",
            "Django+PostgreSQL, Rails+PostgreSQL, dan Next.js+Supabase.)",
        ],
        "hints": [
            "Pisahkan tiap baris di tanda titik dua pertama untuk tahu jenisnya, lalu kumpulkan bobot, daftar syarat wajib, dan data tiap stack.",
            "Untuk tiap stack, cari dulu syarat wajib yang tidak dimilikinya; kalau ada, stack itu gugur dan tidak perlu dihitung skornya.",
            "Urutan peringkat bisa didapat dengan sort memakai kunci (-skor, nama), jadi skor tertinggi di depan dan seri diurut abjad.",
        ],
        "solution": "import sys\n\nbobot = {}\nwajib = []\nstack = []                       # (nama, set syarat, dict skor)\n\nfor b in sys.stdin.read().split(\"\\n\"):\n    if not b.strip():\n        continue\n    jenis, isi = b.split(\":\", 1)\n    kata = isi.split()\n    if jenis == \"kriteria\":\n        for k in kata:\n            nama, nilai = k.split(\"=\")\n            bobot[nama] = int(nilai)\n    elif jenis == \"wajib\":\n        wajib = kata\n    elif jenis == \"stack\":\n        syarat, skor = set(), {}\n        for k in kata[1:]:\n            if \"=\" in k:\n                nama, nilai = k.split(\"=\")\n                skor[nama] = int(nilai)\n            else:\n                syarat.add(k)\n        stack.append((kata[0], syarat, skor))\n\ntotal_bobot = sum(bobot.values())\nprint(f\"Bobot total: {total_bobot} (skor maksimal {total_bobot * 5})\")\n\ngugur, lolos = [], []\nfor nama, syarat, skor in stack:\n    kurang = [w for w in wajib if w not in syarat]\n    if kurang:\n        gugur.append((nama, kurang))\n    else:\n        nilai = sum(bobot[k] * skor.get(k, 0) for k in bobot)\n        lolos.append((nama, nilai))\n\nprint(\"Gugur:\")\nif not gugur:\n    print(\"  -\")\nfor nama, kurang in sorted(gugur):\n    print(f\"  {nama}: tidak memenuhi {', '.join(kurang)}\")\n\nprint(\"Peringkat:\")\nlolos.sort(key=lambda p: (-p[1], p[0]))\nfor i, (nama, nilai) in enumerate(lolos, 1):\n    print(f\"  {i}. {nama} {nilai}\")\n",
        "stdin_list": [
            """kriteria: biaya=3 tim=5 ekosistem=4 skala=2
wajib: hosting_sendiri
stack: Laravel+MySQL hosting_sendiri biaya=5 tim=4 ekosistem=4 skala=3
stack: Next.js+Firebase biaya=4 tim=3 ekosistem=5 skala=5
stack: Django+PostgreSQL hosting_sendiri biaya=5 tim=4 ekosistem=4 skala=3
stack: Rails+PostgreSQL hosting_sendiri biaya=5 tim=2 ekosistem=4 skala=4
stack: Next.js+Supabase hosting_sendiri biaya=4 tim=3 ekosistem=5 skala=4
""",
            """kriteria: kinerja=5 biaya=2
wajib: lisensi_osi tim_bisa
stack: Go+PostgreSQL lisensi_osi kinerja=5 biaya=4
stack: Java+Oracle tim_bisa kinerja=4 biaya=1
stack: Node+MongoDB tim_bisa kinerja=3 biaya=4
stack: Python+PostgreSQL lisensi_osi tim_bisa kinerja=3 biaya=5
""",
        ],
    },
    {
        "title": "Latihan 17: Simulator Gerbang Layanan",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: buat simulator API gateway yang menggabungkan rate",
            "limiter, cache LRU, load balancer round-robin, circuit breaker, dan",
            "satu kali percobaan ulang. Semua waktu adalah jam palsu (detik,",
            "bilangan bulat).",
            "",
            "Input (stdin), baris konfigurasi lalu kejadian:",
            "  cache N                kapasitas cache LRU",
            "  token K L              ember token per klien: kapasitas K,",
            "                         isi ulang L token per detik",
            "  backend A B C ...      daftar backend, urutan round-robin",
            "  breaker M W            ambang gagal beruntun M, masa tunggu W",
            "  rusak NAMA T1 T2       backend NAMA gagal untuk T1 <= t < T2",
            "                         (boleh ada beberapa baris rusak)",
            "  t klien METODE path    satu permintaan (METODE GET atau POST)",
            "",
            "Urutan pemrosesan tiap permintaan:",
            "  1. Rate limiter. Ember klien baru dibuat penuh. Isi ulang sesuai",
            "     waktu yang lewat (tidak melebihi K). Kalau isi kurang dari 1,",
            "     jawab \"429 limiter\". Kalau cukup, ambil 1 token, lalu lanjut.",
            "  2. Cache. GET yang path-nya ada di cache dijawab \"200 cache\" dan",
            "     path itu jadi yang paling baru dipakai. POST menghapus path",
            "     yang sama dari cache lalu tetap diteruskan ke backend.",
            "  3. Load balancer. Mulai dari giliran sekarang, pilih backend",
            "     pertama yang breaker-nya mengizinkan, lalu giliran pindah ke",
            "     backend sesudahnya. Kalau tidak ada, jawab",
            "     \"503 semua backend open\".",
            "  4. Panggil backend. Kalau gagal, ulangi sekali ke backend",
            "     berikutnya yang diizinkan selain backend yang tadi gagal",
            "     (memakai dan memajukan giliran yang sama). Kalau tidak ada",
            "     backend lain atau ulangannya juga gagal, jawab 502.",
            "  5. Kalau sukses, jawab \"200 NAMA\". GET yang sukses disimpan di",
            "     cache; kalau cache melebihi N, buang yang paling lama tidak",
            "     dipakai.",
            "",
            "Circuit breaker per backend: CLOSED menghitung gagal beruntun",
            "(sukses mengembalikannya ke 0) dan jadi OPEN saat mencapai M.",
            "OPEN mengizinkan panggilan lagi kalau t - waktu_dibuka >= W.",
            "Panggilan itu adalah uji: sukses membuat CLOSED, gagal membuat",
            "OPEN lagi sejak t.",
            "",
            "Catatan di dalam kurung, urut sesuai kejadiannya: \"NAMA gagal\",",
            "\"NAMA OPEN\" saat breaker jadi OPEN, \"NAMA CLOSED\" saat uji",
            "berhasil, dan \"buang cache PATH\". Kegagalan backend pertama",
            "selalu ditulis paling depan. Format satu baris:",
            "  t=T klien METODE path: JAWABAN (catatan, catatan)",
            "Sesudah semua kejadian, cetak ringkasan seperti contoh.",
            "",
            "Untuk input cache 2, keluarannya:",
            "t=0 ani GET /produk: 200 api-1",
            "t=0 ani GET /produk: 200 cache",
            "t=0 ani GET /produk: 429 limiter",
            "t=1 budi GET /promo: 200 api-3 (api-2 gagal)",
            "t=1 budi GET /kategori: 200 api-1 (buang cache /produk)",
            "t=2 citra GET /stok: 200 api-3 (api-2 gagal, api-2 OPEN, buang cache /promo)",
            "t=3 ani GET /produk: 200 api-1 (buang cache /kategori)",
            "t=4 budi POST /produk: 200 api-3",
            "t=5 citra GET /produk: 200 api-1",
            "t=6 ani GET /promo: 200 api-3 (buang cache /stok)",
            "t=7 budi GET /promo: 200 cache",
            "t=20 budi GET /stok: 200 api-1 (buang cache /produk)",
            "t=21 citra GET /kategori: 200 api-2 (api-2 CLOSED, buang cache /promo)",
            "Ringkasan:",
            "  200: 12",
            "  429: 1",
            "  502: 0",
            "  503: 0",
            "  cache hit: 2",
            "  api-1: 5 panggilan, CLOSED",
            "  api-2: 3 panggilan, CLOSED",
            "  api-3: 4 panggilan, CLOSED",
            "",
            "(Input lengkapnya: cache 2, token 2 1, backend api-1 api-2 api-3,",
            "breaker 2 10, rusak api-2 0 15, lalu tiga belas permintaan seperti",
            "yang terlihat di keluaran.)",
        ],
        "hints": [
            "Pecah program jadi bagian-bagian dari latihan sebelumnya (token bucket, LRU, round-robin, dan circuit breaker), lalu susun urutan pemrosesannya persis seperti di soal.",
            "Breaker cukup menyimpan keadaan, jumlah gagal beruntun, dan waktu dibuka; panggilan ke backend yang OPEN dengan masa tunggu habis diperlakukan sebagai panggilan uji.",
            "collections.OrderedDict memudahkan LRU: move_to_end(path) saat dipakai, dan popitem(last=False) untuk membuang yang paling lama.",
        ],
        "solution": "import sys\nfrom collections import OrderedDict\n\n\nclass Breaker:\n    def __init__(self, ambang, tunggu):\n        self.ambang, self.tunggu = ambang, tunggu\n        self.keadaan, self.gagal, self.dibuka = \"CLOSED\", 0, 0\n\n    def boleh(self, t):\n        return self.keadaan != \"OPEN\" or t - self.dibuka >= self.tunggu\n\n    def catat(self, t, sukses):\n        \"\"\"Catat hasil panggilan; kembalikan \"OPEN\"/\"CLOSED\" kalau keadaan berubah.\"\"\"\n        uji = self.keadaan == \"OPEN\"     # boleh() sudah mengizinkan: panggilan uji\n        if sukses:\n            self.gagal = 0\n            if uji:\n                self.keadaan = \"CLOSED\"\n                return \"CLOSED\"\n            return \"\"\n        self.gagal += 1\n        if uji or self.gagal >= self.ambang:\n            self.keadaan, self.dibuka = \"OPEN\", t\n            return \"OPEN\"\n        return \"\"\n\n\nbaris = [b for b in sys.stdin.read().split(\"\\n\") if b.strip()]\nkonfig, kejadian = {}, []\nrusak = []\nfor b in baris:\n    kata = b.split()\n    if kata[0] == \"rusak\":\n        rusak.append((kata[1], int(kata[2]), int(kata[3])))\n    elif kata[0].isdigit():\n        kejadian.append((int(kata[0]), kata[1], kata[2], kata[3]))\n    else:\n        konfig[kata[0]] = kata[1:]\n\nkapasitas_cache = int(konfig[\"cache\"][0])\nisi_ember, laju = map(int, konfig[\"token\"])\nbackend = konfig[\"backend\"]\nambang, tunggu = map(int, konfig[\"breaker\"])\n\ncache = OrderedDict()\nember = {}\nbreaker = {n: Breaker(ambang, tunggu) for n in backend}\npanggilan = {n: 0 for n in backend}\ngiliran = 0\nhitung = {\"200\": 0, \"429\": 0, \"502\": 0, \"503\": 0, \"cache\": 0}\n\n\ndef pilih(t, kecuali):\n    \"\"\"Round-robin: backend berikutnya yang breaker-nya mengizinkan.\"\"\"\n    global giliran\n    for k in range(len(backend)):\n        i = (giliran + k) % len(backend)\n        nama = backend[i]\n        if nama != kecuali and breaker[nama].boleh(t):\n            giliran = (i + 1) % len(backend)\n            return nama\n    return None\n\n\ndef panggil(t, nama):\n    panggilan[nama] += 1\n    sukses = not any(n == nama and a <= t < z for n, a, z in rusak)\n    ubah = breaker[nama].catat(t, sukses)\n    return sukses, ubah\n\n\nfor t, klien, metode, path in kejadian:\n    awal = f\"t={t} {klien} {metode} {path}:\"\n    sisa, terakhir = ember.get(klien, (isi_ember, t))\n    sisa = min(isi_ember, sisa + (t - terakhir) * laju)\n    if sisa < 1:\n        ember[klien] = (sisa, t)\n        hitung[\"429\"] += 1\n        print(awal, \"429 limiter\")\n        continue\n    ember[klien] = (sisa - 1, t)\n\n    if metode == \"GET\" and path in cache:\n        cache.move_to_end(path)\n        hitung[\"cache\"] += 1\n        hitung[\"200\"] += 1\n        print(awal, \"200 cache\")\n        continue\n    if metode == \"POST\":\n        cache.pop(path, None)\n\n    catatan = []\n    pertama = pilih(t, None)\n    if pertama is None:\n        hitung[\"503\"] += 1\n        print(awal, \"503 semua backend open\")\n        continue\n    sukses, ubah = panggil(t, pertama)\n    dipakai = pertama\n    if ubah:\n        catatan.append(f\"{pertama} {ubah}\")\n    if not sukses:\n        catatan.insert(0, f\"{pertama} gagal\")\n        kedua = pilih(t, pertama)\n        if kedua is not None:\n            sukses, ubah = panggil(t, kedua)\n            dipakai = kedua\n            if not sukses:\n                catatan.append(f\"{kedua} gagal\")\n            if ubah:\n                catatan.append(f\"{kedua} {ubah}\")\n    if sukses:\n        hitung[\"200\"] += 1\n        hasil = f\"200 {dipakai}\"\n        if metode == \"GET\":\n            cache[path] = dipakai\n            if len(cache) > kapasitas_cache:\n                buang, _ = cache.popitem(last=False)\n                catatan.append(f\"buang cache {buang}\")\n    else:\n        hitung[\"502\"] += 1\n        hasil = \"502\"\n    if catatan:\n        hasil += \" (\" + \", \".join(catatan) + \")\"\n    print(awal, hasil)\n\nprint(\"Ringkasan:\")\nfor kode in (\"200\", \"429\", \"502\", \"503\"):\n    print(f\"  {kode}: {hitung[kode]}\")\nprint(f\"  cache hit: {hitung['cache']}\")\nfor nama in backend:\n    print(f\"  {nama}: {panggilan[nama]} panggilan, {breaker[nama].keadaan}\")\n",
        "stdin_list": [
            """cache 2
token 2 1
backend api-1 api-2 api-3
breaker 2 10
rusak api-2 0 15
0 ani GET /produk
0 ani GET /produk
0 ani GET /produk
1 budi GET /promo
1 budi GET /kategori
2 citra GET /stok
3 ani GET /produk
4 budi POST /produk
5 citra GET /produk
6 ani GET /promo
7 budi GET /promo
20 budi GET /stok
21 citra GET /kategori
""",
            """cache 1
token 1 1
backend b1 b2
breaker 1 5
rusak b1 0 100
rusak b2 0 3
0 x GET /a
1 x GET /a
1 y GET /a
6 x GET /a
6 x GET /a
7 y GET /a
""",
        ],
    },
]
