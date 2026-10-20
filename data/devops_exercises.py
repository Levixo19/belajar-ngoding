"""Kurikulum DevOps & Cloud.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

DEVOPS_EXERCISES = [
    {
        "title": "Latihan 1: Metrik DORA dari Log Deploy",
        "difficulty": "Mudah",
        "question": [
            "Tim kasir mencatat setiap deploy dalam satu baris berformat:",
            "",
            "  tanggal,hasil,menit_lead,menit_pulih",
            "",
            "hasil berisi sukses atau gagal. menit_lead adalah menit dari commit",
            "sampai jalan di produksi. menit_pulih adalah menit sampai deploy yang",
            "gagal berhasil dipulihkan (selalu 0 untuk deploy yang sukses).",
            "",
            "Baca semua baris dari input, lalu cetak empat baris:",
            "  - jumlah deploy, jumlah minggu berbeda (pakai nomor minggu ISO dari",
            "    tanggalnya), dan rata-rata deploy per minggu dengan satu angka",
            "    di belakang titik;",
            "  - median lead time, ditulis tanpa .0 kalau hasilnya bulat;",
            "  - change failure rate dalam persen, dibulatkan tanpa desimal;",
            "  - rata-rata waktu pulih deploy yang gagal dengan satu angka di",
            "    belakang titik, atau tanda - kalau tidak ada deploy yang gagal.",
            "",
            "Contoh input:",
            "  2026-10-05,sukses,95,0",
            "  2026-10-06,sukses,140,0",
            "  2026-10-08,gagal,210,50",
            "  2026-10-09,sukses,80,0",
            "  2026-10-12,sukses,120,0",
            "  2026-10-13,sukses,60,0",
            "  2026-10-15,gagal,180,25",
            "  2026-10-16,sukses,100,0",
            "",
            "Keluaran yang diharapkan:",
            "Deploy: 8 dalam 2 minggu (4.0 per minggu)",
            "Median lead time: 110 menit",
            "Change failure rate: 25%",
            "Rata-rata waktu pulih: 37.5 menit",
        ],
        "hints": [
            "Waktu pulih cuma dirata-rata dari deploy yang gagal, karena deploy yang sukses nggak perlu dipulihkan.",
            "Simpan nomor minggu di sebuah set supaya minggu yang sama nggak terhitung dua kali, dan kumpulkan lead time serta waktu pulih di dua list terpisah.",
            "Pakai date.fromisoformat(tanggal).isocalendar()[1] untuk nomor minggu, statistics.median untuk median, dan format {x:g} supaya 110.0 tercetak 110.",
        ],
        "solution": "import sys\nfrom datetime import date\nfrom statistics import median\n\nminggu = set()\nlead = []\npulih = []\njumlah = 0\nfor baris in sys.stdin.read().split(\"\\n\"):\n    baris = baris.strip()\n    if not baris:\n        continue\n    tanggal, hasil, menit_lead, menit_pulih = baris.split(\",\")\n    jumlah += 1\n    minggu.add(date.fromisoformat(tanggal).isocalendar()[1])\n    lead.append(int(menit_lead))\n    if hasil == \"gagal\":\n        pulih.append(int(menit_pulih))\n\nper_minggu = jumlah / len(minggu)\nprint(f\"Deploy: {jumlah} dalam {len(minggu)} minggu ({per_minggu:.1f} per minggu)\")\nprint(f\"Median lead time: {median(lead):g} menit\")\nprint(f\"Change failure rate: {100 * len(pulih) / jumlah:.0f}%\")\nif pulih:\n    print(f\"Rata-rata waktu pulih: {sum(pulih) / len(pulih):.1f} menit\")\nelse:\n    print(\"Rata-rata waktu pulih: -\")\n",
        "stdin_list": [
            """2026-10-05,sukses,95,0
2026-10-06,sukses,140,0
2026-10-08,gagal,210,50
2026-10-09,sukses,80,0
2026-10-12,sukses,120,0
2026-10-13,sukses,60,0
2026-10-15,gagal,180,25
2026-10-16,sukses,100,0
""",
            """2026-09-01,sukses,45,0
2026-09-03,sukses,30,0
2026-09-09,sukses,61,0
""",
        ],
    },
    {
        "title": "Latihan 2: Pengurai YAML Mini",
        "difficulty": "Mudah",
        "question": [
            "Python nggak punya pengurai YAML bawaan, jadi kita tulis versi mini.",
            "Program membaca berkas YAML dari input dengan aturan subset berikut:",
            "",
            "  - Baris kosong dan baris yang diawali # dilewati.",
            "  - kunci: nilai adalah pasangan biasa.",
            "  - kunci: tanpa nilai membuka mapping atau daftar di bawahnya. Isinya",
            "    menjorok lebih dalam, selalu dua spasi per tingkat.",
            "  - - butir adalah butir daftar milik kunci di atasnya.",
            "  - Tanda kutip di sekitar nilai dibuang.",
            "",
            "Cetak setiap nilai sebagai jalur = nilai, satu per baris, diurutkan",
            "abjad menurut jalurnya. Jalur kunci bertingkat disambung titik",
            "(server.port), dan butir daftar diberi nomor mulai 0 (fitur[0]).",
            "",
            "Kalau ada baris yang indentasinya memakai tab, cetak",
            "galat baris N: tab tidak boleh dipakai untuk indentasi",
            "dengan N nomor baris di input (mulai 1), lalu berhenti tanpa mencetak",
            "apa pun lagi.",
            "",
            "Contoh input:",
            "  aplikasi: toko",
            "  # server utama",
            "  server:",
            "    host: 0.0.0.0",
            "    port: 8080",
            "    tls:",
            "      aktif: \"ya\"",
            "  fitur:",
            "    - keranjang",
            "    - pembayaran",
            "  admin: budi",
            "",
            "Keluaran yang diharapkan:",
            "admin = budi",
            "aplikasi = toko",
            "fitur[0] = keranjang",
            "fitur[1] = pembayaran",
            "server.host = 0.0.0.0",
            "server.port = 8080",
            "server.tls.aktif = ya",
        ],
        "hints": [
            "Yang menentukan sebuah kunci milik siapa cuma jumlah spasi di awal barisnya.",
            "Simpan tumpukan berisi pasangan indentasi dan jalur untuk kunci yang belum punya nilai, lalu buang isi tumpukan yang indentasinya lebih besar atau sama dengan baris sekarang.",
            "Hitung indentasi dengan len(baris) - len(baris.lstrip(' ')), pisahkan kunci dan nilai dengan partition(':'), dan pakai dict penghitung per jalur untuk nomor butir daftar.",
        ],
        "solution": "import sys\n\nhasil = {}\nhitung = {}\ntumpukan = []          # (indentasi, jalur) untuk kunci yang belum punya nilai\nfor nomor, baris in enumerate(sys.stdin.read().split(\"\\n\"), 1):\n    if not baris.strip() or baris.strip().startswith(\"#\"):\n        continue\n    isi = baris.lstrip(\" \")\n    if isi.startswith(\"\\t\"):\n        print(f\"galat baris {nomor}: tab tidak boleh dipakai untuk indentasi\")\n        sys.exit(0)\n    indentasi = len(baris) - len(isi)\n    while tumpukan and tumpukan[-1][0] >= indentasi:\n        tumpukan.pop()\n    induk = tumpukan[-1][1] if tumpukan else \"\"\n    if isi.startswith(\"- \"):\n        nomor_butir = hitung.get(induk, 0)\n        hitung[induk] = nomor_butir + 1\n        hasil[f\"{induk}[{nomor_butir}]\"] = isi[2:].strip()\n        continue\n    kunci, _, nilai = isi.partition(\":\")\n    jalur = f\"{induk}.{kunci.strip()}\" if induk else kunci.strip()\n    nilai = nilai.strip()\n    if nilai:\n        hasil[jalur] = nilai.strip(\"\\\"'\")\n    else:\n        tumpukan.append((indentasi, jalur))\n\nfor jalur in sorted(hasil):\n    print(f\"{jalur} = {hasil[jalur]}\")\n",
        "stdin_list": [
            """aplikasi: toko
# server utama
server:
  host: 0.0.0.0
  port: 8080
  tls:
    aktif: "ya"
fitur:
  - keranjang
  - pembayaran
admin: budi
""",
            """server:
  host: 0.0.0.0
	port: 8080
""",
        ],
    },
    {
        "title": "Latihan 3: Resolver DNS Mini dengan Cache TTL",
        "difficulty": "Menengah",
        "question": [
            "Tulis resolver DNS mini yang punya cache. Input terdiri dari dua",
            "bagian. Bagian zona diawali baris zona, isinya record berformat",
            "nama jenis nilai ttl. Jenisnya cuma A (alamat) atau CNAME (alias).",
            "Bagian kueri diawali baris kueri, isinya waktu nama, dengan waktu dalam",
            "detik dari jam tiruan (selalu naik).",
            "",
            "Untuk setiap kueri, cetak [t=waktu] nama, lalu ikuti rantainya. Untuk",
            "setiap nama di rantai:",
            "  - Kalau ada di cache dan waktu < saat kedaluwarsanya, cetak",
            "    HIT  nama jenis nilai (sisa detik)  (dua spasi sesudah HIT).",
            "  - Kalau tidak, ambil dari zona, simpan di cache sampai waktu + ttl,",
            "    lalu cetak MISS nama jenis nilai (ttl ttl).",
            "  - Kalau nama tidak ada di zona, cetak   galat: NXDOMAIN lalu berhenti.",
            "  - Kalau nama sudah pernah dilewati di kueri yang sama, cetak",
            "      galat: loop CNAME lalu berhenti.",
            "Kalau sampai di record A, cetak   jawaban: alamatnya.",
            "Semua baris sesudah [t=...] menjorok dua spasi.",
            "",
            "Contoh input:",
            "  zona",
            "  www.toko.id CNAME toko.id 300",
            "  toko.id A 203.0.113.10 60",
            "  api.toko.id CNAME gw.toko.id 120",
            "  gw.toko.id CNAME api.toko.id 120",
            "  kueri",
            "  0 www.toko.id",
            "  30 www.toko.id",
            "  70 www.toko.id",
            "  75 api.toko.id",
            "  90 kosong.toko.id",
            "",
            "Keluaran yang diharapkan:",
            "[t=0] www.toko.id",
            "  MISS www.toko.id CNAME toko.id (ttl 300)",
            "  MISS toko.id A 203.0.113.10 (ttl 60)",
            "  jawaban: 203.0.113.10",
            "[t=30] www.toko.id",
            "  HIT  www.toko.id CNAME toko.id (sisa 270)",
            "  HIT  toko.id A 203.0.113.10 (sisa 30)",
            "  jawaban: 203.0.113.10",
            "[t=70] www.toko.id",
            "  HIT  www.toko.id CNAME toko.id (sisa 230)",
            "  MISS toko.id A 203.0.113.10 (ttl 60)",
            "  jawaban: 203.0.113.10",
            "[t=75] api.toko.id",
            "  MISS api.toko.id CNAME gw.toko.id (ttl 120)",
            "  MISS gw.toko.id CNAME api.toko.id (ttl 120)",
            "  galat: loop CNAME",
            "[t=90] kosong.toko.id",
            "  galat: NXDOMAIN",
        ],
        "hints": [
            "Cache cukup menyimpan jenis, nilai, dan detik kedaluwarsa untuk tiap nama, dan entri yang waktunya sudah lewat diperlakukan seperti tidak ada.",
            "Untuk tiap kueri, pakai perulangan while yang terus mengikuti nilai alias, dan sebuah set nama yang sudah dilewati untuk mendeteksi loop.",
            "Simpan cache sebagai dict nama ke tuple (jenis, nilai, waktu + ttl), lalu anggap HIT hanya kalau waktu < tuple[2].",
        ],
        "solution": "import sys\n\nzona = {}\nkueri = []\nbagian = None\nfor baris in sys.stdin.read().split(\"\\n\"):\n    baris = baris.strip()\n    if not baris:\n        continue\n    if baris in (\"zona\", \"kueri\"):\n        bagian = baris\n        continue\n    if bagian == \"zona\":\n        nama, tipe, nilai, ttl = baris.split()\n        zona[nama] = (tipe, nilai, int(ttl))\n    else:\n        waktu, nama = baris.split()\n        kueri.append((int(waktu), nama))\n\ncache = {}   # nama -> (tipe, nilai, kedaluwarsa)\nfor waktu, nama in kueri:\n    print(f\"[t={waktu}] {nama}\")\n    dilihat = set()\n    while True:\n        if nama in dilihat:\n            print(\"  galat: loop CNAME\")\n            break\n        dilihat.add(nama)\n        simpanan = cache.get(nama)\n        if simpanan and waktu < simpanan[2]:\n            tipe, nilai, habis = simpanan\n            print(f\"  HIT  {nama} {tipe} {nilai} (sisa {habis - waktu})\")\n        elif nama in zona:\n            tipe, nilai, ttl = zona[nama]\n            cache[nama] = (tipe, nilai, waktu + ttl)\n            print(f\"  MISS {nama} {tipe} {nilai} (ttl {ttl})\")\n        else:\n            print(\"  galat: NXDOMAIN\")\n            break\n        if tipe == \"A\":\n            print(f\"  jawaban: {nilai}\")\n            break\n        nama = nilai\n",
        "stdin_list": [
            """zona
www.toko.id CNAME toko.id 300
toko.id A 203.0.113.10 60
api.toko.id CNAME gw.toko.id 120
gw.toko.id CNAME api.toko.id 120
kueri
0 www.toko.id
30 www.toko.id
70 www.toko.id
75 api.toko.id
90 kosong.toko.id
""",
            """zona
toko.id A 203.0.113.10 30
kueri
0 toko.id
29 toko.id
30 toko.id
""",
        ],
    },
    {
        "title": "Latihan 4: Pencocok location ala Nginx",
        "difficulty": "Menengah",
        "question": [
            "Tulis program yang memilih blok location seperti Nginx. Input berisi",
            "daftar location, satu per baris, lalu baris ---, lalu daftar jalur",
            "yang diminta. Bentuk location yang mungkin:",
            "",
            "  location = /jalur        persis",
            "  location ^~ /awalan/     awalan, hentikan pencarian regex",
            "  location ~ pola          regex peka huruf besar-kecil",
            "  location ~* pola         regex tidak peka huruf besar-kecil",
            "  location /awalan/        awalan biasa",
            "",
            "Ikuti urutan Nginx: persis dulu; lalu cari awalan terpanjang di antara",
            "awalan biasa dan ^~; kalau yang terpanjang bertanda ^~, pakai itu;",
            "kalau tidak, periksa regex sesuai urutan tulis dan pakai yang pertama",
            "cocok (cocok di bagian mana pun jalur, seperti re.search); kalau tidak",
            "ada regex yang cocok, pakai awalan terpanjang.",
            "",
            "Untuk setiap jalur cetak jalur -> tanda pola (atau jalur -> pola untuk",
            "awalan biasa). Kalau tidak ada yang cocok sama sekali, cetak",
            "jalur -> 404 (tidak ada location).",
            "",
            "Contoh input:",
            "  location = /",
            "  location /",
            "  location /static/",
            "  location ^~ /static/img/",
            "  location ~ \\.php$",
            "  location ~* \\.(png|jpg)$",
            "  ---",
            "  /",
            "  /index.html",
            "  /static/app.css",
            "  /static/img/logo.png",
            "  /foto/kucing.JPG",
            "  /admin/index.php",
            "",
            "Keluaran yang diharapkan:",
            "/ -> = /",
            "/index.html -> /",
            "/static/app.css -> /static/",
            "/static/img/logo.png -> ^~ /static/img/",
            "/foto/kucing.JPG -> ~* \\.(png|jpg)$",
            "/admin/index.php -> ~ \\.php$",
        ],
        "hints": [
            "Awalan biasa nggak langsung dipakai: ia cuma diingat sebagai cadangan sementara regex diperiksa lebih dulu.",
            "Simpan tiap location sebagai pasangan (tanda, pola) dengan tanda kosong untuk awalan biasa, lalu tulis fungsi pilih(jalur) yang menjalankan lima langkah berurutan.",
            "Pakai jalur.startswith(pola) untuk awalan, re.search(pola, jalur) untuk ~, dan tambahkan re.IGNORECASE untuk ~*.",
        ],
        "solution": "import re\nimport sys\n\nteks = sys.stdin.read()\nbagian_lokasi, _, bagian_jalur = teks.partition(\"---\")\n\naturan = []\nfor baris in bagian_lokasi.split(\"\\n\"):\n    baris = baris.strip()\n    if not baris:\n        continue\n    kata = baris.split()\n    if len(kata) == 3:\n        aturan.append((kata[1], kata[2]))\n    else:\n        aturan.append((\"\", kata[1]))\n\n\ndef pilih(jalur):\n    for tanda, pola in aturan:\n        if tanda == \"=\" and jalur == pola:\n            return tanda, pola\n    terpanjang = None\n    for tanda, pola in aturan:\n        if tanda in (\"\", \"^~\") and jalur.startswith(pola):\n            if terpanjang is None or len(pola) > len(terpanjang[1]):\n                terpanjang = (tanda, pola)\n    if terpanjang and terpanjang[0] == \"^~\":\n        return terpanjang\n    for tanda, pola in aturan:\n        if tanda == \"~\" and re.search(pola, jalur):\n            return tanda, pola\n        if tanda == \"~*\" and re.search(pola, jalur, re.IGNORECASE):\n            return tanda, pola\n    return terpanjang\n\n\nfor jalur in bagian_jalur.split(\"\\n\"):\n    jalur = jalur.strip()\n    if not jalur:\n        continue\n    hasil = pilih(jalur)\n    if hasil is None:\n        print(f\"{jalur} -> 404 (tidak ada location)\")\n    else:\n        tanda, pola = hasil\n        print(f\"{jalur} -> {(tanda + ' ' + pola).strip()}\")\n",
        "stdin_list": [
            "location = /\nlocation /\nlocation /static/\nlocation ^~ /static/img/\nlocation ~ \\.php$\nlocation ~* \\.(png|jpg)$\n---\n/\n/index.html\n/static/app.css\n/static/img/logo.png\n/foto/kucing.JPG\n/admin/index.php\n",
            """location /api/
location ~ ^/api/v[0-9]+/
location = /api/status
---
/api/status
/api/v2/produk
/api/lama
/beranda
""",
        ],
    },
    {
        "title": "Latihan 5: Simulasi Cache Layer Dockerfile",
        "difficulty": "Menengah",
        "question": [
            "Docker memutuskan sebuah layer boleh diambil dari cache dengan kunci",
            "berantai. Kunci instruksi ke-n dihitung dari kunci instruksi",
            "sebelumnya, teks instruksinya, dan isi berkas yang disalin (khusus",
            "COPY). Begitu satu kunci berubah, semua kunci sesudahnya ikut berubah.",
            "",
            "Input punya tiga bagian:",
            "  [lama]        isi folder proyek waktu build pertama, nama=isi",
            "  [baru]        isi folder proyek waktu build kedua, nama=isi",
            "  [dockerfile]  instruksi Dockerfile, satu per baris",
            "",
            "Hitung kunci tiap instruksi dengan",
            "  sha256(kunci_sebelumnya + instruksi + masukan)",
            "dengan kunci awal string kosong. masukan kosong untuk instruksi selain",
            "COPY. Untuk COPY nama_berkas ..., masukan adalah isi berkas itu. Untuk",
            "COPY . ., masukan adalah gabungan nama=isi; untuk semua berkas, urut",
            "abjad nama berkasnya.",
            "",
            "Jalankan build pertama dengan isi [lama], lalu build kedua dengan isi",
            "[baru], memakai satu cache bersama (himpunan kunci yang sudah pernah",
            "dibangun). Untuk tiap instruksi cetak #nomor CACHED instruksi kalau",
            "kuncinya sudah ada di cache, atau #nomor BUILD  instruksi (dua spasi",
            "sesudah BUILD) kalau belum. Tutup tiap build dengan ringkasan.",
            "",
            "Contoh input:",
            "  [lama]",
            "  requirements.txt=flask==3.1.2",
            "  app.py=print(\"v1\")",
            "  [baru]",
            "  requirements.txt=flask==3.1.2",
            "  app.py=print(\"v2\")",
            "  [dockerfile]",
            "  FROM python:3.14-slim",
            "  WORKDIR /app",
            "  COPY requirements.txt .",
            "  RUN pip install -r requirements.txt",
            "  COPY . .",
            "  CMD [\"python\", \"app.py\"]",
            "",
            "Keluaran yang diharapkan:",
            "Build pertama:",
            "  #1 BUILD  FROM python:3.14-slim",
            "  #2 BUILD  WORKDIR /app",
            "  #3 BUILD  COPY requirements.txt .",
            "  #4 BUILD  RUN pip install -r requirements.txt",
            "  #5 BUILD  COPY . .",
            "  #6 BUILD  CMD [\"python\", \"app.py\"]",
            "  0 dari cache, 6 dibangun ulang",
            "Build kedua:",
            "  #1 CACHED FROM python:3.14-slim",
            "  #2 CACHED WORKDIR /app",
            "  #3 CACHED COPY requirements.txt .",
            "  #4 CACHED RUN pip install -r requirements.txt",
            "  #5 BUILD  COPY . .",
            "  #6 BUILD  CMD [\"python\", \"app.py\"]",
            "  4 dari cache, 2 dibangun ulang",
        ],
        "hints": [
            "Kunci berantai membuat satu perubahan di tengah merambat ke semua instruksi di bawahnya, karena kunci sebelumnya ikut di-hash.",
            "Baca input jadi dict per bagian, lalu tulis satu fungsi bangun yang menerima Dockerfile, isi folder, dan himpunan cache yang sama untuk kedua build.",
            "Pakai hashlib.sha256((kunci + instruksi + masukan).encode()).hexdigest(), dan untuk COPY . . susun masukan dengan perulangan atas sorted(konteks).",
        ],
        "solution": "import hashlib\nimport sys\n\n\ndef baca(teks):\n    bagian, berkas, dockerfile = None, {}, []\n    for baris in teks.split(\"\\n\"):\n        if not baris.strip():\n            continue\n        if baris.startswith(\"[\") and baris.endswith(\"]\"):\n            bagian = baris[1:-1]\n            berkas.setdefault(bagian, {})\n            continue\n        if bagian == \"dockerfile\":\n            dockerfile.append(baris.strip())\n        else:\n            nama, _, isi = baris.partition(\"=\")\n            berkas[bagian][nama] = isi\n    return berkas, dockerfile\n\n\ndef bangun(judul, dockerfile, konteks, cache):\n    print(judul)\n    kunci = \"\"\n    jumlah_cache = 0\n    for nomor, instruksi in enumerate(dockerfile, 1):\n        masukan = \"\"\n        if instruksi.startswith(\"COPY \"):\n            sumber = instruksi.split()[1]\n            if sumber == \".\":\n                masukan = \"\".join(f\"{n}={konteks[n]};\" for n in sorted(konteks))\n            else:\n                masukan = konteks[sumber]\n        kunci = hashlib.sha256((kunci + instruksi + masukan).encode()).hexdigest()\n        if kunci in cache:\n            status = \"CACHED\"\n            jumlah_cache += 1\n        else:\n            status = \"BUILD \"\n            cache.add(kunci)\n        print(f\"  #{nomor} {status} {instruksi}\")\n    print(f\"  {jumlah_cache} dari cache, {len(dockerfile) - jumlah_cache} dibangun ulang\")\n\n\nberkas, dockerfile = baca(sys.stdin.read())\ncache = set()\nbangun(\"Build pertama:\", dockerfile, berkas[\"lama\"], cache)\nbangun(\"Build kedua:\", dockerfile, berkas[\"baru\"], cache)\n",
        "stdin_list": [
            """[lama]
requirements.txt=flask==3.1.2
app.py=print("v1")
[baru]
requirements.txt=flask==3.1.2
app.py=print("v2")
[dockerfile]
FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
""",
            """[lama]
requirements.txt=flask==3.1.2
app.py=print("v1")
[baru]
requirements.txt=flask==3.1.2
app.py=print("v2")
[dockerfile]
FROM python:3.14-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
""",
        ],
    },
    {
        "title": "Latihan 6: Urutan Start Layanan Compose",
        "difficulty": "Menengah",
        "question": [
            "Compose menyalakan layanan sesuai depends_on: sebuah layanan baru",
            "dinyalakan sesudah semua layanan yang ia butuhkan menyala. Tulis",
            "program yang menentukan urutan itu.",
            "",
            "Setiap baris input berformat nama: dep1, dep2. Layanan tanpa",
            "dependensi ditulis nama: saja. Semua layanan yang disebut sebagai",
            "dependensi juga punya barisnya sendiri.",
            "",
            "Cetak urutan menyala dengan nomor, satu layanan per baris. Kalau ada",
            "beberapa layanan yang sama-sama sudah siap dinyalakan, dahulukan yang",
            "namanya lebih awal menurut abjad.",
            "",
            "Kalau ada siklus, sebagian layanan tidak akan pernah bisa menyala.",
            "Dalam kasus itu jangan cetak urutan apa pun; cetak satu baris",
            "tertahan siklus: diikuti semua layanan yang tidak bisa menyala, urut",
            "abjad, dipisah koma dan spasi.",
            "",
            "Contoh input:",
            "  web: db, cache, migrasi",
            "  migrasi: db",
            "  db:",
            "  cache:",
            "  worker: cache, db",
            "  proxy: web",
            "",
            "Keluaran yang diharapkan:",
            "1. cache",
            "2. db",
            "3. migrasi",
            "4. web",
            "5. proxy",
            "6. worker",
        ],
        "hints": [
            "Layanan boleh dinyalakan begitu hitungan dependensinya yang belum menyala jadi nol, dan menyalakannya mengurangi hitungan semua layanan yang menunggunya.",
            "Pakai algoritma Kahn: simpan jumlah dependensi tiap layanan, daftar siapa memakai siapa, dan antrean layanan yang siap.",
            "Supaya yang siap selalu diambil urut abjad, simpan antreannya dengan heapq, lalu bandingkan panjang urutan akhir dengan jumlah layanan untuk mendeteksi siklus.",
        ],
        "solution": "import heapq\nimport sys\n\nbutuh = {}\nfor baris in sys.stdin.read().split(\"\\n\"):\n    if not baris.strip():\n        continue\n    nama, _, sisa = baris.partition(\":\")\n    deps = [d.strip() for d in sisa.split(\",\") if d.strip()]\n    butuh[nama.strip()] = deps\n\nsisa_dep = {nama: len(deps) for nama, deps in butuh.items()}\npemakai = {nama: [] for nama in butuh}\nfor nama, deps in butuh.items():\n    for d in deps:\n        pemakai[d].append(nama)\n\nsiap = [nama for nama, n in sisa_dep.items() if n == 0]\nheapq.heapify(siap)\nurutan = []\nwhile siap:\n    nama = heapq.heappop(siap)\n    urutan.append(nama)\n    for p in pemakai[nama]:\n        sisa_dep[p] -= 1\n        if sisa_dep[p] == 0:\n            heapq.heappush(siap, p)\n\nif len(urutan) < len(butuh):\n    macet = sorted(n for n in butuh if n not in urutan)\n    print(\"tertahan siklus: \" + \", \".join(macet))\nelse:\n    for i, nama in enumerate(urutan, 1):\n        print(f\"{i}. {nama}\")\n",
        "stdin_list": [
            """web: db, cache, migrasi
migrasi: db
db:
cache:
worker: cache, db
proxy: web
""",
            """web: api
api: auth
auth: api
db:
""",
        ],
    },
    {
        "title": "Latihan 7: Pengurai Referensi Image Container",
        "difficulty": "Menengah",
        "question": [
            "Tulis pengurai nama image dengan aturan bawaan Docker. Input berisi",
            "beberapa referensi image, satu per baris. Untuk setiap referensi,",
            "tentukan lima bagian:",
            "",
            "  - digest: bagian sesudah @, atau - kalau tidak ada.",
            "  - tag: bagian sesudah titik dua terakhir yang letaknya sesudah garis",
            "    miring terakhir. Kalau tidak ada tag, isinya latest, kecuali kalau",
            "    ada digest: dalam hal itu tag diisi -.",
            "  - registry: bagian pertama sebelum garis miring, hanya kalau ada",
            "    garis miring dan bagian itu memuat titik atau titik dua, atau sama",
            "    dengan localhost. Selain itu registry-nya docker.io.",
            "  - namespace: semua bagian di antara registry dan nama terakhir,",
            "    disambung garis miring. Untuk docker.io tanpa namespace, isinya",
            "    library. Untuk registry lain tanpa namespace, isinya -.",
            "  - nama: bagian terakhir sesudah garis miring.",
            "",
            "Cetak referensinya, lalu lima baris menjorok dua spasi persis seperti",
            "contoh, dengan label yang diratakan.",
            "",
            "Contoh input:",
            "  nginx",
            "  postgres:17",
            "  bitnami/redis:7.4",
            "  ghcr.io/contoh/tim/toko:1.4.0",
            "  localhost:5000/coba",
            "  registry.contoh.id/app@sha256:9f86d081",
            "",
            "Keluaran yang diharapkan:",
            "nginx",
            "  registry : docker.io",
            "  namespace: library",
            "  nama     : nginx",
            "  tag      : latest",
            "  digest   : -",
            "postgres:17",
            "  registry : docker.io",
            "  namespace: library",
            "  nama     : postgres",
            "  tag      : 17",
            "  digest   : -",
            "bitnami/redis:7.4",
            "  registry : docker.io",
            "  namespace: bitnami",
            "  nama     : redis",
            "  tag      : 7.4",
            "  digest   : -",
            "ghcr.io/contoh/tim/toko:1.4.0",
            "  registry : ghcr.io",
            "  namespace: contoh/tim",
            "  nama     : toko",
            "  tag      : 1.4.0",
            "  digest   : -",
            "localhost:5000/coba",
            "  registry : localhost:5000",
            "  namespace: -",
            "  nama     : coba",
            "  tag      : latest",
            "  digest   : -",
            "registry.contoh.id/app@sha256:9f86d081",
            "  registry : registry.contoh.id",
            "  namespace: -",
            "  nama     : app",
            "  tag      : -",
            "  digest   : sha256:9f86d081",
        ],
        "hints": [
            "Titik dua di localhost:5000 adalah nomor port, bukan tag, jadi tag cuma dicari sesudah garis miring terakhir.",
            "Kupas dari belakang: pisahkan digest dengan @ dulu, lalu tag dengan membandingkan posisi titik dua terakhir dan garis miring terakhir, baru pecah sisanya dengan garis miring.",
            "Pakai nama.rfind('/') dan nama.rfind(':') untuk posisi, lalu cek '.' in bagian[0] or ':' in bagian[0] or bagian[0] == 'localhost' untuk menentukan registry.",
        ],
        "solution": """import sys


def urai(ref):
    nama, digest = ref, "-"
    if "@" in nama:
        nama, digest = nama.split("@", 1)
    tag = "-" if digest != "-" else "latest"
    garis = nama.rfind("/")
    titik_dua = nama.rfind(":")
    if titik_dua > garis:
        nama, tag = nama[:titik_dua], nama[titik_dua + 1:]
    bagian = nama.split("/")
    if len(bagian) > 1 and ("." in bagian[0] or ":" in bagian[0] or bagian[0] == "localhost"):
        registry, bagian = bagian[0], bagian[1:]
    else:
        registry = "docker.io"
    if registry == "docker.io" and len(bagian) == 1:
        bagian = ["library"] + bagian
    namespace = "/".join(bagian[:-1]) or "-"
    return registry, namespace, bagian[-1], tag, digest


for ref in sys.stdin.read().split():
    registry, namespace, nama, tag, digest = urai(ref)
    print(ref)
    print(f"  registry : {registry}")
    print(f"  namespace: {namespace}")
    print(f"  nama     : {nama}")
    print(f"  tag      : {tag}")
    print(f"  digest   : {digest}")
""",
        "stdin_list": [
            """nginx
postgres:17
bitnami/redis:7.4
ghcr.io/contoh/tim/toko:1.4.0
localhost:5000/coba
registry.contoh.id/app@sha256:9f86d081
""",
            """python:3.14-slim
quay.io/podman/stable:v5
""",
        ],
    },
    {
        "title": "Latihan 8: Runner Pipeline Mini dengan DAG",
        "difficulty": "Menengah",
        "question": [
            "Tulis runner pipeline mini yang meniru cara GitHub Actions menjalankan",
            "job berdasarkan needs.",
            "",
            "Tiap baris stdin berisi satu job: nama|needs|hasil. needs berupa daftar",
            "nama dipisah koma, atau tanda - kalau job itu nggak menunggu siapa pun.",
            "hasil adalah lulus atau gagal: hasil tiruan kalau job itu sempat jalan.",
            "",
            "Aturannya:",
            "  1. Tiap gelombang menjalankan semua job yang semua needs-nya sudah",
            "     punya status, dalam urutan baris masukan.",
            "  2. Job yang salah satu needs-nya tidak lulus (gagal atau dilewati)",
            "     tidak jalan dan berstatus dilewati.",
            "  3. Kalau ada job tersisa tapi tidak ada yang siap, cetak",
            "     galat: needs melingkar di <job tersisa dipisah koma> lalu berhenti.",
            "",
            "Untuk input",
            "  lint|-|lulus",
            "  tes-unit|-|gagal",
            "  tes-integrasi|tes-unit|lulus",
            "  build|lint,tes-unit|lulus",
            "  dokumen|lint|lulus",
            "  deploy|build,tes-integrasi|lulus",
            "keluarannya:",
            "gelombang 1:",
            "  [lulus] lint",
            "  [gagal] tes-unit",
            "gelombang 2:",
            "  [lewat] tes-integrasi (menunggu tes-unit)",
            "  [lewat] build (menunggu tes-unit)",
            "  [lulus] dokumen",
            "gelombang 3:",
            "  [lewat] deploy (menunggu build, tes-integrasi)",
            "ringkasan: 2 lulus, 1 gagal, 3 dilewati",
            "workflow: gagal",
            "",
            "Workflow berstatus lulus hanya kalau semua job lulus.",
        ],
        "hints": [
            "Simpan needs tiap job di dict, lalu ulangi pencarian job yang siap sampai semua job punya status.",
            "Sebuah job siap kalau semua nama di needs-nya sudah ada di dict status, terlepas dari apa statusnya.",
            "Untuk job yang siap, kumpulkan needs yang statusnya bukan lulus; kalau daftar itu tidak kosong, job dilewati dengan daftar itu di dalam kurung.",
        ],
        "solution": """import sys

jobs = []
butuh = {}
hasil_tiruan = {}
for baris in sys.stdin.read().splitlines():
    baris = baris.strip()
    if not baris or baris.startswith("#"):
        continue
    nama, needs, hasil = [b.strip() for b in baris.split("|")]
    jobs.append(nama)
    butuh[nama] = [] if needs == "-" else [n.strip() for n in needs.split(",")]
    hasil_tiruan[nama] = hasil

status = {}
gelombang = 0
while len(status) < len(jobs):
    siap = [j for j in jobs if j not in status
            and all(n in status for n in butuh[j])]
    if not siap:
        sisa = ", ".join(j for j in jobs if j not in status)
        print("galat: needs melingkar di", sisa)
        sys.exit(0)
    gelombang += 1
    print(f"gelombang {gelombang}:")
    for j in siap:
        gagal = [n for n in butuh[j] if status[n] != "lulus"]
        if gagal:
            status[j] = "dilewati"
            print(f"  [lewat] {j} (menunggu {', '.join(gagal)})")
        else:
            status[j] = hasil_tiruan[j]
            print(f"  [{status[j]}] {j}")

hitung = {s: sum(1 for v in status.values() if v == s)
          for s in ("lulus", "gagal", "dilewati")}
print(f"ringkasan: {hitung['lulus']} lulus, {hitung['gagal']} gagal, "
      f"{hitung['dilewati']} dilewati")
print("workflow:", "lulus" if hitung["lulus"] == len(jobs) else "gagal")""",
        "stdin_list": [
            """lint|-|lulus
tes-unit|-|gagal
tes-integrasi|tes-unit|lulus
build|lint,tes-unit|lulus
dokumen|lint|lulus
deploy|build,tes-integrasi|lulus
""",
            """lint|-|lulus
tes-unit|-|lulus
tes-integrasi|tes-unit|lulus
build|lint,tes-unit|lulus
deploy|build,tes-integrasi|lulus
""",
            """a|c|lulus
b|a|lulus
c|b|lulus
""",
        ],
    },
    {
        "title": "Latihan 9: Pengembang Matriks Build",
        "difficulty": "Menengah",
        "question": [
            "GitHub Actions mengembangkan strategy.matrix menjadi daftar job. Tulis",
            "program yang melakukan hal yang sama. stdin berisi satu objek JSON",
            "dengan kunci matrix (wajib), exclude, dan include (opsional).",
            "",
            "Aturannya, sesuai dokumentasi GitHub:",
            "  1. Buat semua kombinasi nilai matrix. Kunci pertama jadi perulangan",
            "     terluar, mengikuti urutan kunci di JSON.",
            "  2. Buang kombinasi yang cocok dengan salah satu entri exclude (semua",
            "     pasangan kunci-nilai entri itu sama).",
            "  3. Untuk tiap entri include, tambahkan isinya ke setiap kombinasi",
            "     hasil langkah 2 yang tidak bentrok dengan nilai matrix asli",
            "     (kunci matrix asli di entri itu harus bernilai sama). Kunci",
            "     tambahan dari include sebelumnya boleh ditimpa.",
            "  4. Kalau entri include tidak bisa ditambahkan ke kombinasi mana pun,",
            "     entri itu menjadi kombinasi baru di akhir daftar.",
            "",
            "Cetak tiap job sebagai job N: kunci=nilai, dipisah koma, dengan urutan",
            "kunci sesuai urutan masuknya. Nilai string dicetak apa adanya, nilai",
            "lain dicetak dalam bentuk JSON (true, 3, dan seterusnya). Baris",
            "terakhir: total: N job.",
            "",
            "Untuk input",
            "  {\"matrix\": {\"os\": [\"ubuntu-latest\", \"windows-latest\"],",
            "   \"python\": [\"3.13\", \"3.14\"]}}",
            "keluarannya:",
            "job 1: os=ubuntu-latest, python=3.13",
            "job 2: os=ubuntu-latest, python=3.14",
            "job 3: os=windows-latest, python=3.13",
            "job 4: os=windows-latest, python=3.14",
            "total: 4 job",
        ],
        "hints": [
            "Kombinasi semua nilai bisa dibuat dengan itertools.product, lalu di-zip dengan daftar kunci matrix menjadi dict.",
            "Simpan daftar kunci asli matrix, karena include hanya boleh menempel kalau nilai untuk kunci-kunci itu sama.",
            "Cocokkan include hanya dengan kombinasi asli hasil exclude, bukan dengan kombinasi baru yang dibuat include sebelumnya.",
        ],
        "solution": """import itertools
import json
import sys

data = json.loads(sys.stdin.read())
matriks = data["matrix"]
kunci_asli = list(matriks)

kombinasi = [dict(zip(kunci_asli, nilai))
             for nilai in itertools.product(*matriks.values())]


def cocok(kombo, pola):
    return all(kombo.get(k) == v for k, v in pola.items())


kombinasi = [k for k in kombinasi
             if not any(cocok(k, pola) for pola in data.get("exclude", []))]

asli = list(kombinasi)
tambahan = []
for isi in data.get("include", []):
    dipakai = False
    for kombo in asli:
        if all(kombo[k] == v for k, v in isi.items() if k in kunci_asli):
            kombo.update(isi)
            dipakai = True
    if not dipakai:
        tambahan.append(dict(isi))


def tampil(v):
    return v if isinstance(v, str) else json.dumps(v)


semua = asli + tambahan
for i, kombo in enumerate(semua, 1):
    isi = ", ".join(f"{k}={tampil(v)}" for k, v in kombo.items())
    print(f"job {i}: {isi}")
print("total:", len(semua), "job")""",
        "stdin_list": [
            """{"matrix": {"os": ["ubuntu-latest", "windows-latest"], "python": ["3.13", "3.14"]}}
""",
            """{"matrix": {"os": ["ubuntu-latest", "windows-latest", "macos-latest"], "python": ["3.12", "3.13", "3.14"]}, "exclude": [{"os": "windows-latest", "python": "3.12"}, {"os": "macos-latest", "python": "3.12"}], "include": [{"python": "3.14", "coverage": true}, {"os": "ubuntu-latest", "python": "3.15-dev", "experimental": true}]}
""",
            """{"matrix": {"fruit": ["apple", "pear"], "animal": ["cat", "dog"]}, "include": [{"color": "green"}, {"color": "pink", "animal": "cat"}, {"fruit": "apple", "shape": "circle"}, {"fruit": "banana"}, {"fruit": "banana", "animal": "cat"}]}
""",
        ],
    },
    {
        "title": "Latihan 10: Kalkulator Subnet VPC",
        "difficulty": "Menengah",
        "question": [
            "Tulis kalkulator subnet untuk VPC AWS memakai modul ipaddress.",
            "Tiap baris stdin berisi satu perintah:",
            "",
            "  vpc <CIDR>            blok VPC (selalu baris pertama)",
            "  subnet <nama> /<n>    pesan subnet berukuran /n",
            "  cek <alamat IP>       alamat itu masuk subnet mana",
            "",
            "Aturannya:",
            "  1. vpc mencetak VPC <CIDR> (<jumlah> alamat).",
            "  2. subnet memakai blok /n pertama di dalam VPC (dari alamat",
            "     terkecil) yang tidak tumpang tindih dengan subnet yang sudah",
            "     dipesan. Cetak nama (lebar 10, rata kiri), CIDR (lebar 15, rata",
            "     kiri), rentang alamat yang bisa dipakai, dan jumlahnya. AWS",
            "     mencadangkan empat alamat pertama dan satu alamat terakhir.",
            "  3. Kalau tidak ada blok yang muat, cetak",
            "     galat: ruang VPC habis untuk <nama>.",
            "  4. cek mencetak nama subnet, atau keterangan dicadangkan AWS, di",
            "     VPC tapi belum masuk subnet, atau di luar VPC.",
            "",
            "Untuk input",
            "  vpc 10.0.0.0/16",
            "  subnet publik-a /24",
            "  subnet publik-b /24",
            "  subnet privat-a /20",
            "  subnet privat-b /20",
            "  cek 10.0.1.25",
            "  cek 10.0.16.9",
            "  cek 10.0.0.2",
            "  cek 10.0.2.7",
            "  cek 10.1.0.1",
            "keluarannya:",
            "VPC 10.0.0.0/16 (65536 alamat)",
            "publik-a   10.0.0.0/24     pakai 10.0.0.4 - 10.0.0.254 (251 alamat)",
            "publik-b   10.0.1.0/24     pakai 10.0.1.4 - 10.0.1.254 (251 alamat)",
            "privat-a   10.0.16.0/20    pakai 10.0.16.4 - 10.0.31.254 (4091 alamat)",
            "privat-b   10.0.32.0/20    pakai 10.0.32.4 - 10.0.47.254 (4091 alamat)",
            "cek 10.0.1.25: publik-b",
            "cek 10.0.16.9: privat-a",
            "cek 10.0.0.2: publik-a, tapi dicadangkan AWS",
            "cek 10.0.2.7: di VPC, belum masuk subnet mana pun",
            "cek 10.1.0.1: di luar VPC",
            "",
            "Perhatikan privat-a mulai di 10.0.16.0, bukan 10.0.2.0: blok /20",
            "harus mulai di kelipatan 16 pada oktet ketiga.",
        ],
        "hints": [
            "Blok /n yang sah di dalam VPC bisa didaftar berurutan dengan metode subnets(new_prefix=n) milik objek jaringan.",
            "Pilih calon pertama yang tidak overlaps dengan subnet mana pun yang sudah dipesan.",
            "Untuk cek, bandingkan selisih int(ip) dengan int(network_address); selisih di bawah 4 atau sama dengan broadcast_address berarti dicadangkan.",
        ],
        "solution": """import ipaddress
import sys

vpc = None
subnet = []
for baris in sys.stdin.read().splitlines():
    bagian = baris.split()
    if not bagian:
        continue
    if bagian[0] == "vpc":
        vpc = ipaddress.ip_network(bagian[1])
        print(f"VPC {vpc} ({vpc.num_addresses} alamat)")
    elif bagian[0] == "subnet":
        nama, prefiks = bagian[1], int(bagian[2].lstrip("/"))
        dipilih = None
        for calon in vpc.subnets(new_prefix=prefiks):
            if not any(calon.overlaps(s) for _, s in subnet):
                dipilih = calon
                break
        if dipilih is None:
            print(f"galat: ruang VPC habis untuk {nama}")
            continue
        subnet.append((nama, dipilih))
        alamat = list(dipilih)
        print(f"{nama:<10} {str(dipilih):<15} pakai {alamat[4]} - {alamat[-2]}"
              f" ({dipilih.num_addresses - 5} alamat)")
    elif bagian[0] == "cek":
        ip = ipaddress.ip_address(bagian[1])
        if ip not in vpc:
            print(f"cek {ip}: di luar VPC")
            continue
        for nama, s in subnet:
            if ip in s:
                urutan = int(ip) - int(s.network_address)
                if urutan < 4 or ip == s.broadcast_address:
                    print(f"cek {ip}: {nama}, tapi dicadangkan AWS")
                else:
                    print(f"cek {ip}: {nama}")
                break
        else:
            print(f"cek {ip}: di VPC, belum masuk subnet mana pun")""",
        "stdin_list": [
            """vpc 10.0.0.0/16
subnet publik-a /24
subnet publik-b /24
subnet privat-a /20
subnet privat-b /20
cek 10.0.1.25
cek 10.0.16.9
cek 10.0.0.2
cek 10.0.2.7
cek 10.1.0.1
""",
            """vpc 172.16.0.0/22
subnet web /24
subnet app /23
subnet db /24
subnet cadangan /24
cek 172.16.2.255
cek 172.16.3.10
""",
        ],
    },
    {
        "title": "Latihan 11: Evaluator Kebijakan IAM Mini",
        "difficulty": "Lanjut",
        "question": [
            "Tulis evaluator kebijakan IAM versi mini. stdin berisi satu objek",
            "JSON dengan dua kunci:",
            "",
            "  kebijakan   daftar pernyataan: Sid, Effect (Allow atau Deny),",
            "              Action dan Resource (teks atau daftar teks, boleh",
            "              memakai wildcard * dan ?)",
            "  permintaan  daftar objek dengan kunci action dan resource",
            "",
            "Sebuah pernyataan cocok kalau salah satu pola Action cocok dengan",
            "action (tanpa membedakan huruf besar kecil) dan salah satu pola",
            "Resource cocok dengan resource (huruf besar kecil dibedakan). Untuk",
            "tiap permintaan:",
            "  1. Ada Deny yang cocok: DENY, ditolak eksplisit oleh <Sid, ...>.",
            "  2. Selain itu, ada Allow yang cocok: ALLOW, diizinkan oleh <Sid>.",
            "  3. Selain itu: DENY, tolak bawaan, tidak ada Allow yang cocok.",
            "",
            "Cetak dua baris per permintaan: hasil (ALLOW atau DENY ditambah",
            "satu spasi supaya lebarnya lima), action, dan resource; lalu enam",
            "spasi dan alasannya. Sid dicetak sesuai urutan di kebijakan.",
            "",
            "Kebijakan pada kasus uji pertama:",
            "  BacaLaporan    Allow  s3:GetObject, s3:ListBucket",
            "                        laporan-tim dan laporan-tim/*",
            "  TulisDraf      Allow  s3:PutObject  laporan-tim/draf/*",
            "  LindungiArsip  Deny   s3:*          laporan-tim/arsip/*",
            "  LihatEC2       Allow  ec2:Describe* *",
            "(ARN bucket ditulis lengkap, misalnya arn:aws:s3:::laporan-tim/*.)",
            "",
            "Keluaran yang diharapkan:",
            "ALLOW s3:GetObject arn:aws:s3:::laporan-tim/2026/okt.csv",
            "      diizinkan oleh BacaLaporan",
            "ALLOW s3:PutObject arn:aws:s3:::laporan-tim/draf/nov.csv",
            "      diizinkan oleh TulisDraf",
            "DENY  s3:PutObject arn:aws:s3:::laporan-tim/2026/okt.csv",
            "      tolak bawaan, tidak ada Allow yang cocok",
            "DENY  s3:GetObject arn:aws:s3:::laporan-tim/arsip/2020.csv",
            "      ditolak eksplisit oleh LindungiArsip",
            "ALLOW ec2:DescribeInstances *",
            "      diizinkan oleh LihatEC2",
            "DENY  ec2:TerminateInstances *",
            "      tolak bawaan, tidak ada Allow yang cocok",
        ],
        "hints": [
            "Modul fnmatch sudah memahami wildcard * dan ?; pakai fnmatchcase supaya huruf besar kecil diatur sendiri.",
            "Ubah Action dan Resource yang berupa teks tunggal jadi daftar satu elemen supaya bisa diperlakukan sama.",
            "Kumpulkan dulu semua pernyataan yang cocok, lalu periksa Deny sebelum Allow, persis urutan IAM.",
        ],
        "solution": """import fnmatch
import json
import sys

data = json.loads(sys.stdin.read())


def daftar(nilai):
    return nilai if isinstance(nilai, list) else [nilai]


def cocok(pernyataan, permintaan):
    aksi = any(fnmatch.fnmatchcase(permintaan["action"].lower(), pola.lower())
               for pola in daftar(pernyataan["Action"]))
    sumber = any(fnmatch.fnmatchcase(permintaan["resource"], pola)
                 for pola in daftar(pernyataan["Resource"]))
    return aksi and sumber


for p in data["permintaan"]:
    kena = [s for s in data["kebijakan"] if cocok(s, p)]
    tolak = [s["Sid"] for s in kena if s["Effect"] == "Deny"]
    izin = [s["Sid"] for s in kena if s["Effect"] == "Allow"]
    if tolak:
        hasil, alasan = "DENY ", "ditolak eksplisit oleh " + ", ".join(tolak)
    elif izin:
        hasil, alasan = "ALLOW", "diizinkan oleh " + ", ".join(izin)
    else:
        hasil, alasan = "DENY ", "tolak bawaan, tidak ada Allow yang cocok"
    print(f"{hasil} {p['action']} {p['resource']}")
    print(f"      {alasan}")""",
        "stdin_list": [
            """{"kebijakan": [{"Sid": "BacaLaporan", "Effect": "Allow", "Action": ["s3:GetObject", "s3:ListBucket"], "Resource": ["arn:aws:s3:::laporan-tim", "arn:aws:s3:::laporan-tim/*"]}, {"Sid": "TulisDraf", "Effect": "Allow", "Action": "s3:PutObject", "Resource": "arn:aws:s3:::laporan-tim/draf/*"}, {"Sid": "LindungiArsip", "Effect": "Deny", "Action": "s3:*", "Resource": "arn:aws:s3:::laporan-tim/arsip/*"}, {"Sid": "LihatEC2", "Effect": "Allow", "Action": "ec2:Describe*", "Resource": "*"}], "permintaan": [{"action": "s3:GetObject", "resource": "arn:aws:s3:::laporan-tim/2026/okt.csv"}, {"action": "s3:PutObject", "resource": "arn:aws:s3:::laporan-tim/draf/nov.csv"}, {"action": "s3:PutObject", "resource": "arn:aws:s3:::laporan-tim/2026/okt.csv"}, {"action": "s3:GetObject", "resource": "arn:aws:s3:::laporan-tim/arsip/2020.csv"}, {"action": "ec2:DescribeInstances", "resource": "*"}, {"action": "ec2:TerminateInstances", "resource": "*"}]}
""",
            """{"kebijakan": [{"Sid": "SemuaS3", "Effect": "Allow", "Action": "s3:*", "Resource": "*"}, {"Sid": "JanganHapus", "Effect": "Deny", "Action": ["s3:DeleteObject", "s3:DeleteBucket"], "Resource": "*"}], "permintaan": [{"action": "s3:deleteobject", "resource": "arn:aws:s3:::foto/a.jpg"}, {"action": "s3:GetObject", "resource": "arn:aws:s3:::foto/a.jpg"}, {"action": "dynamodb:GetItem", "resource": "arn:aws:dynamodb:ap-southeast-3:123456789012:table/Pesanan"}]}
""",
        ],
    },
    {
        "title": "Latihan 12: Handler Event Lambda Tiruan",
        "difficulty": "Menengah",
        "question": [
            "Tiru cara Lambda memanggil handler dan memakai ulang lingkungan.",
            "Tiap baris stdin berisi satu objek JSON {\"detik\": n, \"event\": {...}}",
            "dengan detik yang selalu naik.",
            "",
            "Aturannya:",
            "  1. Kalau belum ada lingkungan, atau jeda sejak pemanggilan",
            "     terakhir lebih dari 300 detik, buat lingkungan baru (COLD).",
            "     Selain itu pakai lingkungan lama (WARM). Angka 300 cuma",
            "     tiruan; AWS tidak menjanjikan angka pasti.",
            "  2. Lingkungan menyimpan berapa kali handler dipanggil di",
            "     dalamnya, mulai dari 1 untuk lingkungan baru.",
            "  3. Event S3 (punya kunci Records) menghasilkan status ok dan pesan",
            "     proses <key> (<size> bita) dari record pertama.",
            "  4. Event HTTP GET (requestContext.http.method bernilai GET)",
            "     menghasilkan statusCode 200 dan body JSON {\"pesan\": \"Halo,",
            "     <nama>!\"}; nama dari queryStringParameters, bawaannya dunia.",
            "  5. Event lain menghasilkan statusCode 400 dan body",
            "     {\"galat\": \"event tidak dikenal\"}.",
            "",
            "Cetak satu baris per event: detik (lebar 4, rata kanan), [COLD] atau",
            "[WARM], ke-<n>, kode (statusCode atau status), lalu body atau pesan.",
            "Baris terakhir menghitung cold start dan warm start.",
            "",
            "Kasus uji pertama berisi GET nama Sari di detik 0, GET tanpa nama di",
            "detik 2, S3 produk/sepatu.jpg 20480 bita di detik 40, GET nama Budi",
            "di detik 500, dan event jadwal di detik 520.",
            "",
            "Keluaran yang diharapkan:",
            "detik    0 [COLD] ke-1 200 {\"pesan\": \"Halo, Sari!\"}",
            "detik    2 [WARM] ke-2 200 {\"pesan\": \"Halo, dunia!\"}",
            "detik   40 [WARM] ke-3 ok proses produk/sepatu.jpg (20480 bita)",
            "detik  500 [COLD] ke-1 200 {\"pesan\": \"Halo, Budi!\"}",
            "detik  520 [WARM] ke-2 400 {\"galat\": \"event tidak dikenal\"}",
            "cold start: 2, warm start: 3",
        ],
        "hints": [
            "Simpan lingkungan sebagai variabel di luar handler, isinya dict penghitung, dan simpan juga detik pemanggilan terakhir.",
            "Bandingkan detik sekarang dikurangi detik terakhir dengan 300 sebelum memanggil handler, lalu perbarui detik terakhir.",
            "Body HTTP dibuat dengan json.dumps supaya tanda kutipnya sama persis dengan keluaran yang diminta.",
        ],
        "solution": """import json
import sys

BATAS_MENGANGGUR = 300      # detik, angka tiruan

lingkungan = None           # None berarti belum ada instans hangat
terakhir = None
hitung = {"cold": 0, "warm": 0}


def inisialisasi():
    # Kode di luar handler: jalan sekali per instans baru
    return {"dipanggil": 0}


def handler(event, context):
    context["dipanggil"] += 1
    if "Records" in event:
        objek = event["Records"][0]["s3"]["object"]
        return {"status": "ok",
                "pesan": f"proses {objek['key']} ({objek['size']} bita)"}
    if event.get("requestContext", {}).get("http", {}).get("method") == "GET":
        nama = (event.get("queryStringParameters") or {}).get("nama", "dunia")
        return {"statusCode": 200,
                "body": json.dumps({"pesan": f"Halo, {nama}!"})}
    return {"statusCode": 400, "body": json.dumps({"galat": "event tidak dikenal"})}


for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    data = json.loads(baris)
    detik, event = data["detik"], data["event"]
    if lingkungan is None or detik - terakhir > BATAS_MENGANGGUR:
        lingkungan = inisialisasi()
        jenis = "COLD"
    else:
        jenis = "WARM"
    hitung[jenis.lower()] += 1
    terakhir = detik
    hasil = handler(event, lingkungan)
    kode = hasil.get("statusCode", hasil.get("status"))
    isi = hasil.get("body", hasil.get("pesan"))
    print(f"detik {detik:>4} [{jenis}] ke-{lingkungan['dipanggil']} {kode} {isi}")

print(f"cold start: {hitung['cold']}, warm start: {hitung['warm']}")""",
        "stdin_list": [
            """{"detik": 0, "event": {"version": "2.0", "rawPath": "/halo", "requestContext": {"http": {"method": "GET"}}, "queryStringParameters": {"nama": "Sari"}}}
{"detik": 2, "event": {"version": "2.0", "rawPath": "/halo", "requestContext": {"http": {"method": "GET"}}}}
{"detik": 40, "event": {"Records": [{"eventSource": "aws:s3", "s3": {"bucket": {"name": "foto-toko"}, "object": {"key": "produk/sepatu.jpg", "size": 20480}}}]}}
{"detik": 500, "event": {"version": "2.0", "rawPath": "/halo", "requestContext": {"http": {"method": "GET"}}, "queryStringParameters": {"nama": "Budi"}}}
{"detik": 520, "event": {"jenis": "jadwal"}}
""",
            """{"detik": 0, "event": {"Records": [{"eventSource": "aws:s3", "s3": {"bucket": {"name": "foto-toko"}, "object": {"key": "a.png", "size": 10}}}]}}
{"detik": 100, "event": {"Records": [{"eventSource": "aws:s3", "s3": {"bucket": {"name": "foto-toko"}, "object": {"key": "b.png", "size": 20}}}]}}
{"detik": 399, "event": {"Records": [{"eventSource": "aws:s3", "s3": {"bucket": {"name": "foto-toko"}, "object": {"key": "c.png", "size": 30}}}]}}
{"detik": 700, "event": {"Records": [{"eventSource": "aws:s3", "s3": {"bucket": {"name": "foto-toko"}, "object": {"key": "d.png", "size": 40}}}]}}
""",
        ],
    },
    {
        "title": "Latihan 13: Antrean dengan Visibility Timeout dan DLQ",
        "difficulty": "Lanjut",
        "question": [
            "Simulasikan antrean SQS dengan jam tiruan. Baris stdin:",
            "",
            "  visibility <detik>   lama pesan disembunyikan setelah diterima",
            "  maks <n>             maxReceiveCount sebelum pindah ke DLQ",
            "  interval <detik>     konsumen memeriksa antrean tiap sekian detik",
            "  pesan <id> gagal <k> pesan dikirim di detik 0; k penerimaan",
            "                       pertamanya gagal, sesudahnya berhasil",
            "",
            "Konsumen memeriksa di detik 0, interval, 2 x interval, dan",
            "seterusnya, sampai semua pesan selesai. Di tiap pemeriksaan, untuk",
            "setiap pesan yang belum selesai dan sudah terlihat (detik sekarang",
            "tidak kurang dari detik terlihatnya), sesuai urutan kirim:",
            "  1. Kalau pesan sudah diterima sebanyak maks kali, pindahkan ke",
            "     DLQ.",
            "  2. Selain itu tambah hitungan terima. Kalau hitungan lebih dari k,",
            "     pesan berhasil dan dihapus. Kalau tidak, pesan gagal dan",
            "     terlihat lagi di detik sekarang + visibility.",
            "",
            "Cetak tiap kejadian dengan detik selebar 3 (rata kanan), lalu daftar",
            "id yang berhasil dan yang masuk DLQ (pakai - kalau kosong).",
            "",
            "Untuk input",
            "  visibility 30",
            "  maks 3",
            "  interval 10",
            "  pesan A gagal 0",
            "  pesan B gagal 2",
            "  pesan C gagal 99",
            "keluarannya:",
            "detik   0: A diterima ke-1, berhasil, dihapus",
            "detik   0: B diterima ke-1, gagal, muncul lagi di detik 30",
            "detik   0: C diterima ke-1, gagal, muncul lagi di detik 30",
            "detik  30: B diterima ke-2, gagal, muncul lagi di detik 60",
            "detik  30: C diterima ke-2, gagal, muncul lagi di detik 60",
            "detik  60: B diterima ke-3, berhasil, dihapus",
            "detik  60: C diterima ke-3, gagal, muncul lagi di detik 90",
            "detik  90: C pindah ke DLQ sesudah 3 kali diterima",
            "berhasil: A, B",
            "DLQ: C",
        ],
        "hints": [
            "Simpan tiap pesan sebagai dict berisi hitungan terima, detik terlihat, ambang gagal, dan tanda selesai.",
            "Jalankan perulangan while selama masih ada pesan yang belum selesai, dan naikkan detik sebesar interval di akhir tiap putaran.",
            "Periksa syarat pindah ke DLQ sebelum menambah hitungan terima, supaya pesan dipindah tepat saat akan diterima untuk kali ke maks + 1.",
        ],
        "solution": """import sys

konfigurasi = {}
antrean = []        # pesan sesuai urutan kirim
for baris in sys.stdin.read().splitlines():
    b = baris.split()
    if not b:
        continue
    if b[0] == "pesan":
        antrean.append({"id": b[1], "gagal": int(b[3]), "terima": 0,
                        "terlihat": 0, "selesai": False})
    else:
        konfigurasi[b[0]] = int(b[1])

visibility = konfigurasi["visibility"]
maks = konfigurasi["maks"]
interval = konfigurasi["interval"]
dlq = []
detik = 0
while any(not p["selesai"] for p in antrean):
    for p in antrean:
        if p["selesai"] or p["terlihat"] > detik:
            continue
        if p["terima"] == maks:
            p["selesai"] = True
            dlq.append(p["id"])
            print(f"detik {detik:>3}: {p['id']} pindah ke DLQ "
                  f"sesudah {maks} kali diterima")
            continue
        p["terima"] += 1
        if p["terima"] > p["gagal"]:
            p["selesai"] = True
            print(f"detik {detik:>3}: {p['id']} diterima ke-{p['terima']}, "
                  "berhasil, dihapus")
        else:
            p["terlihat"] = detik + visibility
            print(f"detik {detik:>3}: {p['id']} diterima ke-{p['terima']}, "
                  f"gagal, muncul lagi di detik {p['terlihat']}")
    detik += interval

berhasil = [p["id"] for p in antrean if p["id"] not in dlq]
print("berhasil:", ", ".join(berhasil) if berhasil else "-")
print("DLQ:", ", ".join(dlq) if dlq else "-")""",
        "stdin_list": [
            """visibility 30
maks 3
interval 10
pesan A gagal 0
pesan B gagal 2
pesan C gagal 99
""",
            """visibility 15
maks 2
interval 10
pesan struk-1 gagal 1
pesan struk-2 gagal 2
""",
        ],
    },
    {
        "title": "Latihan 14: Simulasi Terraform Plan",
        "difficulty": "Lanjut",
        "question": [
            "Tulis versi mini terraform plan. stdin berisi satu objek JSON:",
            "",
            "  state      alamat -> {attrs, depends_on (opsional)}",
            "  config     alamat -> {attrs, depends_on (opsional)}",
            "  force_new  jenis resource -> daftar atribut yang memaksa ganti",
            "             (opsional)",
            "",
            "Jenis resource adalah bagian alamat sebelum titik pertama.",
            "",
            "Aturannya:",
            "  1. Telusuri config dalam urutan topologis menurut depends_on.",
            "     Kalau ada beberapa yang siap, ambil yang abjadnya paling kecil",
            "     dulu, satu per satu.",
            "  2. Alamat yang tidak ada di state: + <alamat> (create), lalu tiap",
            "     atribut urut abjad sebagai '      kunci = nilai'.",
            "  3. Alamat yang ada di keduanya dan atributnya sama: tidak dicetak.",
            "  4. Ada atribut berbeda yang terdaftar di force_new:",
            "     -/+ <alamat> (replace). Kalau tidak: ~ <alamat> (update",
            "     in-place). Lalu tiap atribut yang berbeda urut abjad sebagai",
            "     '      kunci: lama -> baru', ditambah '  # memaksa ganti' untuk",
            "     atribut pemaksa.",
            "  5. Alamat yang ada di state tapi tidak di config dihapus:",
            "     - <alamat> (destroy), dalam kebalikan urutan topologis state.",
            "  6. Nilai dicetak dengan json.dumps (atribut yang hilang jadi null).",
            "  7. Sesudah baris kosong, cetak",
            "     Plan: X to add, Y to change, Z to destroy. Replace dihitung satu",
            "     add dan satu destroy. Kalau tidak ada perubahan sama sekali,",
            "     cetak No changes. Your infrastructure matches the configuration.",
            "",
            "Kasus uji pertama: instance web berganti instance_type, instance",
            "batch berganti ami (pemaksa), bucket foto dan distribusi CloudFront",
            "baru, serta bucket lama beserta policy-nya dibuang.",
            "",
            "Keluaran yang diharapkan:",
            "+ aws_s3_bucket.foto (create)",
            "      bucket = \"foto-toko-2026\"",
            "      versioning = true",
            "+ aws_cloudfront_distribution.cdn (create)",
            "      origin = \"foto-toko-2026\"",
            "-/+ aws_instance.batch (replace)",
            "      ami: \"ami-0a1\" -> \"ami-0b2\"  # memaksa ganti",
            "~ aws_instance.web (update in-place)",
            "      instance_type: \"t3.micro\" -> \"t3.small\"",
            "- aws_s3_bucket_policy.lama (destroy)",
            "- aws_s3_bucket.lama (destroy)",
            "",
            "Plan: 3 to add, 1 to change, 3 to destroy.",
        ],
        "hints": [
            "Urutan topologis bisa dibuat dengan perulangan: di tiap langkah cari alamat yang semua depends_on-nya sudah tidak tersisa, urutkan, ambil yang pertama.",
            "Untuk alamat yang ada di keduanya, kumpulkan kunci gabungan dari dua dict attrs lalu ambil yang nilainya berbeda.",
            "Jalankan fungsi urutan topologis yang sama untuk resource yang dibuang, lalu balik hasilnya dengan reversed.",
        ],
        "solution": "import json\nimport sys\n\ndata = json.loads(sys.stdin.read())\nstate = data[\"state\"]\nconfig = data[\"config\"]\npaksa = data.get(\"force_new\", {})\n\n\ndef urut_topologis(sumber):\n    sisa = dict(sumber)\n    hasil = []\n    while sisa:\n        siap = sorted(a for a, isi in sisa.items()\n                      if all(d not in sisa for d in isi.get(\"depends_on\", [])))\n        if not siap:\n            raise SystemExit(\"galat: dependensi melingkar\")\n        hasil.append(siap[0])\n        del sisa[siap[0]]\n    return hasil\n\n\ndef tampil(v):\n    return json.dumps(v)\n\n\ntambah = ubah = hapus = 0\nbaris = []\nfor alamat in urut_topologis(config):\n    baru = config[alamat][\"attrs\"]\n    if alamat not in state:\n        tambah += 1\n        baris.append(f\"+ {alamat} (create)\")\n        for k in sorted(baru):\n            baris.append(f\"      {k} = {tampil(baru[k])}\")\n        continue\n    lama = state[alamat][\"attrs\"]\n    beda = sorted(k for k in set(lama) | set(baru) if lama.get(k) != baru.get(k))\n    if not beda:\n        continue\n    jenis = alamat.split(\".\")[0]\n    pemaksa = [k for k in beda if k in paksa.get(jenis, [])]\n    if pemaksa:\n        tambah += 1\n        hapus += 1\n        baris.append(f\"-/+ {alamat} (replace)\")\n    else:\n        ubah += 1\n        baris.append(f\"~ {alamat} (update in-place)\")\n    for k in beda:\n        catatan = \"  # memaksa ganti\" if k in pemaksa else \"\"\n        baris.append(f\"      {k}: {tampil(lama.get(k))} -> {tampil(baru.get(k))}{catatan}\")\n\ndibuang = {a: isi for a, isi in state.items() if a not in config}\nfor alamat in reversed(urut_topologis(dibuang)):\n    hapus += 1\n    baris.append(f\"- {alamat} (destroy)\")\n\nif not baris:\n    print(\"No changes. Your infrastructure matches the configuration.\")\nelse:\n    print(\"\\n\".join(baris))\n    print()\n    print(f\"Plan: {tambah} to add, {ubah} to change, {hapus} to destroy.\")",
        "stdin_list": [
            """{"force_new": {"aws_instance": ["ami"], "aws_s3_bucket": ["bucket"]}, "state": {"aws_vpc.utama": {"attrs": {"cidr_block": "10.0.0.0/16"}}, "aws_instance.web": {"attrs": {"ami": "ami-0a1", "instance_type": "t3.micro"}, "depends_on": ["aws_vpc.utama"]}, "aws_instance.batch": {"attrs": {"ami": "ami-0a1", "instance_type": "t3.small"}, "depends_on": ["aws_vpc.utama"]}, "aws_s3_bucket.lama": {"attrs": {"bucket": "log-lama-2024"}}, "aws_s3_bucket_policy.lama": {"attrs": {"public": false}, "depends_on": ["aws_s3_bucket.lama"]}}, "config": {"aws_vpc.utama": {"attrs": {"cidr_block": "10.0.0.0/16"}}, "aws_instance.web": {"attrs": {"ami": "ami-0a1", "instance_type": "t3.small"}, "depends_on": ["aws_vpc.utama"]}, "aws_instance.batch": {"attrs": {"ami": "ami-0b2", "instance_type": "t3.small"}, "depends_on": ["aws_vpc.utama"]}, "aws_s3_bucket.foto": {"attrs": {"bucket": "foto-toko-2026", "versioning": true}}, "aws_cloudfront_distribution.cdn": {"attrs": {"origin": "foto-toko-2026"}, "depends_on": ["aws_s3_bucket.foto"]}}}
""",
            """{"state": {"aws_vpc.utama": {"attrs": {"cidr_block": "10.0.0.0/16"}}}, "config": {"aws_vpc.utama": {"attrs": {"cidr_block": "10.0.0.0/16"}}}}
""",
            """{"force_new": {"aws_vpc": ["cidr_block"]}, "state": {"aws_vpc.utama": {"attrs": {"cidr_block": "10.0.0.0/16", "tags": {"env": "dev"}}}}, "config": {"aws_vpc.utama": {"attrs": {"cidr_block": "10.1.0.0/16", "tags": {"env": "dev"}}}, "aws_subnet.a": {"attrs": {"cidr_block": "10.1.1.0/24"}, "depends_on": ["aws_vpc.utama"]}}}
""",
        ],
    },
    {
        "title": "Latihan 15: Playbook Idempoten Mini",
        "difficulty": "Lanjut",
        "question": [
            "Tiru cara Ansible menilai ok dan changed. stdin berisi isi berkas",
            "konfigurasi, lalu baris ---, lalu daftar tugas, satu per baris:",
            "",
            "  baris_ada <teks>        pastikan baris persis itu ada (tambah di",
            "                          akhir kalau belum ada)",
            "  baris_tidak_ada <teks>  pastikan baris persis itu tidak ada",
            "  nilai <kunci> <nilai>   baris pertama yang kata pertamanya kunci",
            "                          diganti jadi '<kunci> <nilai>'; kalau tidak",
            "                          ada, tambahkan di akhir",
            "  tulis_ujung <teks>      selalu tambah di akhir, seperti shell",
            "                          echo >> (sengaja tidak idempoten)",
            "",
            "Jalankan semua tugas dua putaran atas berkas yang sama. Tiap tugas",
            "dicetak sebagai '  changed: [jenis] isi' atau '  ok: [jenis] isi'.",
            "Tiap putaran diakhiri '  rekap: ok=<jumlah tugas> changed=<n>',",
            "lalu cetak isi akhir berkas dengan dua spasi di depan tiap baris.",
            "",
            "Untuk input",
            "  Port 22",
            "  PermitRootLogin yes",
            "  PasswordAuthentication yes",
            "  ---",
            "  nilai PermitRootLogin no",
            "  baris_tidak_ada PasswordAuthentication yes",
            "  baris_ada PubkeyAuthentication yes",
            "  nilai Port 22",
            "keluarannya:",
            "putaran 1",
            "  changed: [nilai] PermitRootLogin no",
            "  changed: [baris_tidak_ada] PasswordAuthentication yes",
            "  changed: [baris_ada] PubkeyAuthentication yes",
            "  ok: [nilai] Port 22",
            "  rekap: ok=4 changed=3",
            "putaran 2",
            "  ok: [nilai] PermitRootLogin no",
            "  ok: [baris_tidak_ada] PasswordAuthentication yes",
            "  ok: [baris_ada] PubkeyAuthentication yes",
            "  ok: [nilai] Port 22",
            "  rekap: ok=4 changed=0",
            "isi akhir:",
            "  Port 22",
            "  PermitRootLogin no",
            "  PubkeyAuthentication yes",
            "",
            "Putaran kedua yang melapor changed=0 adalah tanda tugasnya",
            "idempoten. Kasus uji lain memakai tulis_ujung, yang tetap changed",
            "di putaran kedua.",
        ],
        "hints": [
            "Pisahkan masukan dengan str.partition pada baris --- , lalu simpan isi berkas sebagai list baris yang diubah langsung oleh tiap tugas.",
            "Buat satu fungsi yang menjalankan satu tugas dan mengembalikan True hanya kalau list barisnya benar-benar berubah.",
            "Untuk tugas nilai, bandingkan kata pertama tiap baris dengan kunci; kalau barisnya sudah persis sama, kembalikan False tanpa mengubah apa pun.",
        ],
        "solution": "import sys\n\nteks, _, tugas_teks = sys.stdin.read().partition(\"---\\n\")\nberkas = teks.splitlines()\ntugas = [t.split(\" \", 1) for t in tugas_teks.splitlines() if t.strip()]\n\n\ndef jalankan(jenis, isi):\n    \"\"\"Kembalikan True kalau berkas berubah.\"\"\"\n    if jenis == \"baris_ada\":\n        if isi in berkas:\n            return False\n        berkas.append(isi)\n        return True\n    if jenis == \"baris_tidak_ada\":\n        if isi not in berkas:\n            return False\n        berkas[:] = [b for b in berkas if b != isi]\n        return True\n    if jenis == \"nilai\":\n        kunci = isi.split()[0]\n        for i, b in enumerate(berkas):\n            if b.split() and b.split()[0] == kunci:\n                if b == isi:\n                    return False\n                berkas[i] = isi\n                return True\n        berkas.append(isi)\n        return True\n    if jenis == \"tulis_ujung\":\n        berkas.append(isi)\n        return True\n    raise SystemExit(f\"galat: jenis tugas {jenis} tidak dikenal\")\n\n\nfor putaran in (1, 2):\n    print(f\"putaran {putaran}\")\n    berubah = 0\n    for jenis, isi in tugas:\n        if jalankan(jenis, isi):\n            berubah += 1\n            print(f\"  changed: [{jenis}] {isi}\")\n        else:\n            print(f\"  ok: [{jenis}] {isi}\")\n    print(f\"  rekap: ok={len(tugas)} changed={berubah}\")\n\nprint(\"isi akhir:\")\nfor b in berkas:\n    print(\"  \" + b)",
        "stdin_list": [
            """Port 22
PermitRootLogin yes
PasswordAuthentication yes
---
nilai PermitRootLogin no
baris_tidak_ada PasswordAuthentication yes
baris_ada PubkeyAuthentication yes
nilai Port 22
""",
            """Port 22
---
nilai Port 2222
tulis_ujung MaxAuthTries 3
baris_ada UseDNS no
""",
        ],
    },
    {
        "title": "Latihan 16: Reconciler Replika Mini",
        "difficulty": "Lanjut",
        "question": [
            "Tulis reconciliation loop yang menjaga jumlah pod sesuai jumlah",
            "replika yang diinginkan, memakai jam tiruan (tick 1, 2, 3, ...).",
            "",
            "Masukan dari stdin:",
            "  desired N          jumlah replika awal yang diinginkan",
            "  pods a b ...       pod yang sudah hidup, bernama web-<nomor>",
            "  ticks T            jumlah tick yang disimulasikan",
            "  <t> mati p q ...   pada tick t, pod p dan q mati",
            "  <t> skala N        pada tick t, replika diubah jadi N",
            "",
            "Tiap tick: jalankan kejadian tick itu lebih dulu (cetak",
            "'t=<t> kejadian: mati ...' atau 't=<t> kejadian: skala ke N'),",
            "lalu rekonsiliasi dan cetak satu baris:",
            "  t=<t> desired=<N> actual=<jumlah sebelum bertindak> -> <aksi>",
            "",
            "Aksinya 'buat ...' (nomor baru melanjutkan nomor terbesar yang",
            "pernah ada), 'hapus ...' (pod bernomor terbesar lebih dulu, ditulis",
            "urut nomor kecil ke besar), atau 'sesuai'. Di akhir cetak",
            "'akhir:' diikuti pod yang tersisa, urut nomor.",
            "",
            "Contoh masukan:",
            "  desired 3",
            "  pods web-1 web-2",
            "  ticks 6",
            "  2 mati web-1",
            "  3 skala 5",
            "  5 mati web-3 web-4",
            "  6 skala 2",
            "",
            "Keluaran yang diharapkan:",
            "t=1 desired=3 actual=2 -> buat web-3",
            "t=2 kejadian: mati web-1",
            "t=2 desired=3 actual=2 -> buat web-4",
            "t=3 kejadian: skala ke 5",
            "t=3 desired=5 actual=3 -> buat web-5 web-6",
            "t=4 desired=5 actual=5 -> sesuai",
            "t=5 kejadian: mati web-3 web-4",
            "t=5 desired=5 actual=3 -> buat web-7 web-8",
            "t=6 kejadian: skala ke 2",
            "t=6 desired=2 actual=5 -> hapus web-6 web-7 web-8",
            "akhir: web-2 web-5",
        ],
        "hints": [
            "Controller nggak menyimpan riwayat perintah; tiap tick ia cuma membandingkan jumlah pod yang ada dengan jumlah yang diinginkan.",
            "Simpan kejadian dalam dict berkunci nomor tick, dan simpan nomor pod terbesar yang pernah dipakai supaya nama pod baru nggak pernah mengulang nama lama.",
            "Untuk menghapus, urutkan pod menurut angka sesudah tanda hubung, lalu ambil potongan mulai indeks desired sampai akhir.",
        ],
        "stdin": """desired 3
pods web-1 web-2
ticks 6
2 mati web-1
3 skala 5
5 mati web-3 web-4
6 skala 2
""",
        "solution": """import sys

desired = 0
pods = []
ticks = 0
kejadian = {}
nomor = 0

for baris in sys.stdin.read().splitlines():
    bagian = baris.split()
    if not bagian:
        continue
    if bagian[0] == "desired":
        desired = int(bagian[1])
    elif bagian[0] == "pods":
        pods = bagian[1:]
    elif bagian[0] == "ticks":
        ticks = int(bagian[1])
    else:
        kejadian.setdefault(int(bagian[0]), []).append(bagian[1:])

for nama in pods:
    nomor = max(nomor, int(nama.split("-")[1]))

for t in range(1, ticks + 1):
    for k in kejadian.get(t, []):
        if k[0] == "mati":
            for nama in k[1:]:
                if nama in pods:
                    pods.remove(nama)
            print(f"t={t} kejadian: mati {' '.join(k[1:])}")
        elif k[0] == "skala":
            desired = int(k[1])
            print(f"t={t} kejadian: skala ke {desired}")
    aktual = len(pods)
    if aktual < desired:
        baru = []
        for _ in range(desired - aktual):
            nomor += 1
            baru.append(f"web-{nomor}")
        pods += baru
        aksi = "buat " + " ".join(baru)
    elif aktual > desired:
        urut = sorted(pods, key=lambda n: int(n.split("-")[1]))
        hapus = urut[desired:]
        for nama in hapus:
            pods.remove(nama)
        aksi = "hapus " + " ".join(hapus)
    else:
        aksi = "sesuai"
    print(f"t={t} desired={desired} actual={aktual} -> {aksi}")

print("akhir:", " ".join(sorted(pods, key=lambda n: int(n.split("-")[1]))))
""",
    },
    {
        "title": "Latihan 17: Scheduler Pod ke Node",
        "difficulty": "Lanjut",
        "question": [
            "Tiru keputusan kube-scheduler versi sederhana. Tiap pod punya",
            "request CPU (milicore) dan memori (Mi); tiap node punya sisa",
            "kapasitas. Pod diproses sesuai urutan masukan.",
            "",
            "Aturan: node yang muat adalah node yang sisa CPU dan sisa",
            "memorinya sama-sama cukup. Dari yang muat, pilih node dengan sisa",
            "CPU terbanyak; kalau seri, pilih nama yang lebih dulu menurut",
            "abjad. Kurangi sisa node itu. Kalau nggak ada yang muat, pod",
            "berstatus Pending.",
            "",
            "Masukan dari stdin: baris 'node <nama> <cpu> <mem>' lalu baris",
            "'pod <nama> <cpu> <mem>'.",
            "",
            "Contoh masukan:",
            "  node node-a 2000 4096",
            "  node node-b 2000 2048",
            "  node node-c 1000 8192",
            "  pod api-1 500 512",
            "  pod api-2 500 512",
            "  pod db-1 1000 3072",
            "  pod worker-1 1500 1024",
            "  pod cache-1 250 256",
            "  pod batch-1 1200 512",
            "",
            "Keluaran yang diharapkan:",
            "api-1 (500m, 512Mi) -> node-a",
            "api-2 (500m, 512Mi) -> node-b",
            "db-1 (1000m, 3072Mi) -> node-a",
            "worker-1 (1500m, 1024Mi) -> node-b",
            "cache-1 (250m, 256Mi) -> node-c",
            "batch-1 (1200m, 512Mi) -> Pending: tidak ada node yang muat",
            "sisa:",
            "  node-a: 500m CPU, 512Mi memori",
            "  node-b: 0m CPU, 512Mi memori",
            "  node-c: 750m CPU, 7936Mi memori",
            "pending: batch-1",
            "",
            "Perhatikan batch-1: total sisa CPU semua node 1250m, tapi nggak",
            "ada satu node pun yang punya 1200m sendirian. Itu fragmentasi,",
            "alasan pod bisa Pending walau klaster kelihatan masih longgar.",
        ],
        "hints": [
            "Scheduler bekerja dua tahap: menyaring node yang muat, lalu memberi skor dan memilih yang terbaik.",
            "Simpan node sebagai dict nama ke sisa cpu dan mem, lalu untuk tiap pod buat daftar node yang muat dengan list comprehension.",
            "Kunci pengurutan (-sisa_cpu, nama) memberi node dengan CPU terbanyak lebih dulu dan memutus seri menurut abjad.",
        ],
        "stdin": """node node-a 2000 4096
node node-b 2000 2048
node node-c 1000 8192
pod api-1 500 512
pod api-2 500 512
pod db-1 1000 3072
pod worker-1 1500 1024
pod cache-1 250 256
pod batch-1 1200 512
""",
        "solution": """import sys

node = {}
pod = []

for baris in sys.stdin.read().splitlines():
    b = baris.split()
    if not b:
        continue
    if b[0] == "node":
        node[b[1]] = {"cpu": int(b[2]), "mem": int(b[3])}
    elif b[0] == "pod":
        pod.append((b[1], int(b[2]), int(b[3])))

pending = []
for nama, cpu, mem in pod:
    muat = [n for n in node if node[n]["cpu"] >= cpu and node[n]["mem"] >= mem]
    if not muat:
        pending.append(nama)
        print(f"{nama} ({cpu}m, {mem}Mi) -> Pending: tidak ada node yang muat")
        continue
    pilih = sorted(muat, key=lambda n: (-node[n]["cpu"], n))[0]
    node[pilih]["cpu"] -= cpu
    node[pilih]["mem"] -= mem
    print(f"{nama} ({cpu}m, {mem}Mi) -> {pilih}")

print("sisa:")
for n in sorted(node):
    print(f"  {n}: {node[n]['cpu']}m CPU, {node[n]['mem']}Mi memori")
print("pending:", ", ".join(pending) if pending else "tidak ada")
""",
    },
    {
        "title": "Latihan 18: Mesin Templat Helm Mini",
        "difficulty": "Lanjut",
        "question": [
            "Tulis mesin templat kecil yang meniru helm template untuk pola",
            "{{ .Values.jalur.kunci }} saja.",
            "",
            "Masukan dari stdin terdiri dari empat bagian berurutan:",
            "  [bawaan]   values.yaml bawaan chart, baris jalur=nilai",
            "  [berkas]   isi berkas -f, baris jalur=nilai",
            "  [set]      isi --set, baris jalur=nilai",
            "  [templat]  baris templat apa adanya (sampai akhir masukan)",
            "",
            "Jalur bertitik seperti image.tag berarti values bertingkat.",
            "Prioritasnya seperti Helm: bawaan < berkas < set. Ganti setiap",
            "{{ .Values.x }} (spasi di dalam kurung kurawal boleh ada atau",
            "nggak) dengan nilainya. Kunci yang nggak ada diganti teks",
            "kosong, seperti perilaku Helm, lalu dicatat.",
            "",
            "Sesudah templat, cetak '---' lalu 'kunci hilang:' diikuti jalur",
            "yang hilang (bentuk .Values.x, urut kemunculan, dipisah koma dan",
            "spasi), atau 'tidak ada'.",
            "",
            "Contoh masukan:",
            "  [bawaan]",
            "  replicaCount=1",
            "  image.repository=toko-api",
            "  image.tag=2.4.0",
            "  service.port=80",
            "  [berkas]",
            "  replicaCount=3",
            "  service.port=8080",
            "  [set]",
            "  image.tag=2.4.1",
            "  [templat]",
            "  apiVersion: apps/v1",
            "  kind: Deployment",
            "  metadata:",
            "    name: web",
            "  spec:",
            "    replicas: {{ .Values.replicaCount }}",
            "    template:",
            "      spec:",
            "        containers:",
            "          - name: web",
            "            image: \"{{ .Values.image.repository }}:{{ .Values.image.tag }}\"",
            "            ports:",
            "              - containerPort: {{ .Values.service.port }}",
            "            env:",
            "              - name: MODE",
            "                value: \"{{ .Values.env.mode }}\"",
            "",
            "Keluaran yang diharapkan:",
            "apiVersion: apps/v1",
            "kind: Deployment",
            "metadata:",
            "  name: web",
            "spec:",
            "  replicas: 3",
            "  template:",
            "    spec:",
            "      containers:",
            "        - name: web",
            "          image: \"toko-api:2.4.1\"",
            "          ports:",
            "            - containerPort: 8080",
            "          env:",
            "            - name: MODE",
            "              value: \"\"",
            "---",
            "kunci hilang: .Values.env.mode",
        ],
        "hints": [
            "Helm menggabungkan tiga sumber values menjadi satu pohon, lalu templat hanya membaca pohon hasil gabungan itu.",
            "Bangun dict bertingkat dengan memecah jalur di titik dan memakai setdefault untuk tiap tingkat, lalu proses sumber sesuai urutan prioritas supaya yang terakhir menimpa.",
            "Pakai re.sub dengan pola yang menangkap jalur sesudah .Values. dan fungsi pengganti yang menelusuri dict; kembalikan string kosong kalau kuncinya nggak ada.",
        ],
        "stdin": """[bawaan]
replicaCount=1
image.repository=toko-api
image.tag=2.4.0
service.port=80
[berkas]
replicaCount=3
service.port=8080
[set]
image.tag=2.4.1
[templat]
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: web
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.service.port }}
          env:
            - name: MODE
              value: "{{ .Values.env.mode }}"
""",
        "solution": "import re\nimport sys\n\nbagian = {\"bawaan\": [], \"berkas\": [], \"set\": [], \"templat\": []}\nkini = None\nfor baris in sys.stdin.read().splitlines():\n    if re.fullmatch(r\"\\[(\\w+)\\]\", baris.strip()):\n        kini = baris.strip()[1:-1]\n        continue\n    if kini and (baris.strip() or kini == \"templat\"):\n        bagian[kini].append(baris)\n\n\ndef pasang(values, jalur, nilai):\n    kunci = jalur.split(\".\")\n    for k in kunci[:-1]:\n        values = values.setdefault(k, {})\n    values[kunci[-1]] = nilai\n\n\nvalues = {}\nfor sumber in (\"bawaan\", \"berkas\", \"set\"):\n    for baris in bagian[sumber]:\n        jalur, nilai = baris.split(\"=\", 1)\n        pasang(values, jalur.strip(), nilai.strip())\n\nhilang = []\n\n\ndef ganti(m):\n    jalur = m.group(1)\n    v = values\n    for k in jalur.split(\".\"):\n        if isinstance(v, dict) and k in v:\n            v = v[k]\n        else:\n            if \".Values.\" + jalur not in hilang:\n                hilang.append(\".Values.\" + jalur)\n            return \"\"\n    return str(v)\n\n\nfor baris in bagian[\"templat\"]:\n    print(re.sub(r\"\\{\\{\\s*\\.Values\\.([\\w.]+)\\s*\\}\\}\", ganti, baris))\nprint(\"---\")\nprint(\"kunci hilang:\", \", \".join(hilang) if hilang else \"tidak ada\")\n",
    },
    {
        "title": "Latihan 19: Diff GitOps dan Deteksi Drift",
        "difficulty": "Sulit",
        "question": [
            "Tiru inti Argo CD: bandingkan manifest di Git dengan objek di",
            "klaster, lalu susun rencana sync.",
            "",
            "Masukan dari stdin berupa JSON dengan kunci 'prune' (true/false),",
            "'git', dan 'klaster'. Keduanya daftar objek berkunci kind,",
            "metadata.name, dan kolom lain bertingkat.",
            "",
            "Aturan:",
            "  - Kenali objek dengan kunci '<kind>/<nama>', proses urut abjad.",
            "  - Abaikan kolom milik klaster: status, metadata.uid, dan",
            "    metadata.resourceVersion.",
            "  - Ratakan kolom bertingkat jadi jalur bertitik (spec.replicas).",
            "  - Cetak 'Synced', atau 'OutOfSync' diikuti tiap kolom yang beda",
            "    (urut abjad) dalam bentuk '  <jalur>: git=<nilai> klaster=<nilai>'",
            "    dengan nilai ditulis sebagai JSON.",
            "  - Objek yang cuma ada di Git: 'OutOfSync (belum ada di klaster)'.",
            "  - Objek yang cuma ada di klaster:",
            "    'OutOfSync (tidak ada di Git, perlu prune)'.",
            "  - Terakhir cetak 'rencana sync:' lalu create, update, prune",
            "    (urutan itu). Kalau prune false, tulis",
            "    '  lewati prune <objek> (prune mati)'.",
            "",
            "Keluaran yang diharapkan:",
            "ConfigMap/web-config: OutOfSync (belum ada di klaster)",
            "Deployment/web: OutOfSync",
            "  spec.replicas: git=3 klaster=5",
            "Job/migrasi-lama: OutOfSync (tidak ada di Git, perlu prune)",
            "Service/web: Synced",
            "rencana sync:",
            "  create ConfigMap/web-config",
            "  update Deployment/web",
            "  lewati prune Job/migrasi-lama (prune mati)",
        ],
        "hints": [
            "Drift dihitung per kolom, jadi bandingkan dua objek sebagai daftar pasangan jalur dan nilai, bukan sebagai dict bersarang utuh.",
            "Tulis fungsi rekursif yang meratakan dict menjadi jalur bertitik sambil melewati jalur yang ada di himpunan kolom yang diabaikan.",
            "Gabungkan kunci objek dari Git dan klaster dengan operasi himpunan, urutkan, lalu tentukan untuk tiap kunci apakah ia create, update, prune, atau sudah Synced.",
        ],
        "stdin": """{"prune": false,
 "git": [
  {"kind": "Deployment", "metadata": {"name": "web"},
   "spec": {"replicas": 3, "image": "toko-api:2.4.1"}},
  {"kind": "Service", "metadata": {"name": "web"},
   "spec": {"port": 80, "targetPort": 8080}},
  {"kind": "ConfigMap", "metadata": {"name": "web-config"},
   "data": {"MODE": "produksi"}}
 ],
 "klaster": [
  {"kind": "Deployment", "metadata": {"name": "web", "uid": "a1"},
   "spec": {"replicas": 5, "image": "toko-api:2.4.1"},
   "status": {"readyReplicas": 5}},
  {"kind": "Service", "metadata": {"name": "web", "uid": "b2"},
   "spec": {"port": 80, "targetPort": 8080}},
  {"kind": "Job", "metadata": {"name": "migrasi-lama", "uid": "c3"},
   "spec": {"image": "toko-api:2.3.0"}}
 ]}
""",
        "solution": """import json
import sys

data = json.loads(sys.stdin.read())
ABAIKAN = {"status", "metadata.uid", "metadata.resourceVersion"}


def ratakan(obj, awalan=""):
    hasil = {}
    for k, v in obj.items():
        jalur = awalan + k
        if jalur in ABAIKAN:
            continue
        if isinstance(v, dict):
            hasil.update(ratakan(v, jalur + "."))
        else:
            hasil[jalur] = v
    return hasil


def kunci(obj):
    return obj["kind"] + "/" + obj["metadata"]["name"]


git = {kunci(o): ratakan(o) for o in data["git"]}
klaster = {kunci(o): ratakan(o) for o in data["klaster"]}
rencana = {"create": [], "update": [], "prune": []}

for k in sorted(set(git) | set(klaster)):
    if k not in klaster:
        print(f"{k}: OutOfSync (belum ada di klaster)")
        rencana["create"].append(k)
    elif k not in git:
        print(f"{k}: OutOfSync (tidak ada di Git, perlu prune)")
        rencana["prune"].append(k)
    else:
        beda = [j for j in sorted(set(git[k]) | set(klaster[k]))
                if git[k].get(j) != klaster[k].get(j)]
        if not beda:
            print(f"{k}: Synced")
            continue
        print(f"{k}: OutOfSync")
        for j in beda:
            print(f"  {j}: git={json.dumps(git[k].get(j))} "
                  f"klaster={json.dumps(klaster[k].get(j))}")
        rencana["update"].append(k)

print("rencana sync:")
for aksi in ("create", "update", "prune"):
    for k in rencana[aksi]:
        if aksi == "prune" and not data["prune"]:
            print(f"  lewati prune {k} (prune mati)")
        else:
            print(f"  {aksi} {k}")
""",
    },
    {
        "title": "Latihan 20: Fungsi rate() dari Counter Prometheus",
        "difficulty": "Sulit",
        "question": [
            "Tulis versi sederhana dua fungsi PromQL: increase()/rate() untuk",
            "counter yang bisa reset, dan histogram_quantile() dari bucket.",
            "",
            "Masukan dari stdin:",
            "  counter             lalu baris '<detik> <nilai>'",
            "  jendela A B         hanya sampel dengan A <= detik <= B dipakai",
            "  bucket              lalu baris '<le> <jumlah kumulatif>'",
            "                      (bucket terakhir '+Inf')",
            "  kuantil q           misalnya 0.95",
            "",
            "Aturan counter: jumlahkan selisih tiap pasangan sampel berurutan",
            "di dalam jendela. Kalau nilai turun, anggap counter reset ke 0,",
            "jadi kenaikannya adalah nilai baru itu sendiri. rate = increase",
            "dibagi selisih detik sampel pertama dan terakhir di jendela (tanpa",
            "ekstrapolasi). Cetak increase dengan format :g dan rate tiga",
            "angka di belakang koma.",
            "",
            "Aturan kuantil: peringkat = q x jumlah total (bucket +Inf). Cari",
            "bucket pertama yang jumlahnya >= peringkat, lalu interpolasi",
            "linear antara batas bawah bucket itu (batas bucket sebelumnya,",
            "atau 0) dan batas atasnya. Kalau yang terpilih bucket +Inf,",
            "hasilnya batas atas bucket terbatas terakhir. Cetak empat angka di",
            "belakang koma, dengan nama p<q x 100>.",
            "",
            "Contoh masukan:",
            "  counter",
            "  0 100",
            "  15 130",
            "  30 160",
            "  45 20",
            "  60 50",
            "  75 80",
            "  jendela 0 60",
            "  bucket",
            "  0.1 500",
            "  0.25 800",
            "  0.5 900",
            "  1 980",
            "  +Inf 1000",
            "  kuantil 0.95",
            "",
            "Keluaran yang diharapkan:",
            "sampel dalam jendela: 5",
            "reset terdeteksi: 1",
            "increase: 110",
            "rate: 1.833 per detik",
            "p95: 0.8125 detik",
        ],
        "hints": [
            "Counter yang turun nilainya bukan berarti ada yang dikurangi; prosesnya restart dan menghitung lagi dari nol.",
            "Pasangkan sampel berurutan dengan zip(daftar, daftar[1:]) supaya tiap selisih bisa diperiksa naik atau turun.",
            "Untuk kuantil, simpan batas dan jumlah bucket sebelumnya saat menelusuri daftar, lalu hitung bawah + (atas - bawah) x (peringkat - jumlah_bawah) / (jumlah - jumlah_bawah).",
        ],
        "stdin": """counter
0 100
15 130
30 160
45 20
60 50
75 80
jendela 0 60
bucket
0.1 500
0.25 800
0.5 900
1 980
+Inf 1000
kuantil 0.95
""",
        "solution": """import sys

sampel, bucket = [], []
awal = akhir = 0
q = 0.0
mode = None
for baris in sys.stdin.read().splitlines():
    b = baris.split()
    if not b:
        continue
    if b[0] in ("counter", "bucket"):
        mode = b[0]
    elif b[0] == "jendela":
        awal, akhir = int(b[1]), int(b[2])
    elif b[0] == "kuantil":
        q = float(b[1])
    elif mode == "counter":
        sampel.append((int(b[0]), float(b[1])))
    elif mode == "bucket":
        batas = float("inf") if b[0] == "+Inf" else float(b[0])
        bucket.append((batas, float(b[1])))

dalam = [(t, v) for t, v in sampel if awal <= t <= akhir]
naik, reset = 0.0, 0
for (t0, v0), (t1, v1) in zip(dalam, dalam[1:]):
    if v1 < v0:
        reset += 1
        naik += v1
    else:
        naik += v1 - v0
durasi = dalam[-1][0] - dalam[0][0]
print(f"sampel dalam jendela: {len(dalam)}")
print(f"reset terdeteksi: {reset}")
print(f"increase: {naik:g}")
print(f"rate: {naik / durasi:.3f} per detik")

total = bucket[-1][1]
peringkat = q * total
bawah_batas, bawah_jumlah = 0.0, 0.0
for batas, jumlah in bucket:
    if jumlah >= peringkat:
        if batas == float("inf"):
            hasil = bawah_batas
        else:
            hasil = bawah_batas + (batas - bawah_batas) * (
                (peringkat - bawah_jumlah) / (jumlah - bawah_jumlah))
        break
    bawah_batas, bawah_jumlah = batas, jumlah
print(f"p{round(q * 100)}: {hasil:.4f} detik")
""",
    },
    {
        "title": "Latihan 21: Pohon Trace dari Span",
        "difficulty": "Sulit",
        "question": [
            "Backend tracing menerima span dalam urutan acak. Susun span",
            "menjadi pohon, cetak berindentasi, dan tandai jalur kritis.",
            "",
            "Masukan dari stdin, satu span per baris:",
            "  <id> <parent> <nama> <mulai_ms> <selesai_ms>",
            "parent '-' berarti span akar (hanya ada satu).",
            "",
            "Aturan:",
            "  - Cetak tiap span sebagai '<nama> <durasi>ms', menjorok dua",
            "    spasi per tingkat. Anak diurutkan menurut waktu mulai.",
            "  - Jalur kritis: mulai dari akar, lalu berulang kali pilih anak",
            "    yang selesai paling akhir. Span di jalur kritis diberi ' *'",
            "    di ujung barisnya.",
            "  - Terakhir cetak 'jalur kritis: ' diikuti nama span di jalur",
            "    itu, dipisah ' > '.",
            "",
            "Contoh masukan:",
            "  s4 s2 SELECT-produk 30 70",
            "  s1 - GET-/checkout 0 250",
            "  s6 s5 POST-bank 120 230",
            "  s2 s1 layanan-stok 10 90",
            "  s3 s1 auth 5 20",
            "  s5 s1 layanan-bayar 100 240",
            "  s7 s2 redis-GET 15 25",
            "",
            "Keluaran yang diharapkan:",
            "GET-/checkout 250ms *",
            "  auth 15ms",
            "  layanan-stok 80ms",
            "    redis-GET 10ms",
            "    SELECT-produk 40ms",
            "  layanan-bayar 140ms *",
            "    POST-bank 110ms *",
            "jalur kritis: GET-/checkout > layanan-bayar > POST-bank",
        ],
        "hints": [
            "Urutan kedatangan span nggak penting; yang menyusun pohon adalah hubungan tiap span dengan id induknya.",
            "Simpan span dalam dict berkunci id dan buat dict kedua dari id induk ke daftar id anak, lalu cetak dengan fungsi rekursif yang menerima kedalaman.",
            "Jalur kritis bisa dicari dengan perulangan while: dari akar, ambil max(anak, key=waktu selesai) sampai span tanpa anak.",
        ],
        "stdin": """s4 s2 SELECT-produk 30 70
s1 - GET-/checkout 0 250
s6 s5 POST-bank 120 230
s2 s1 layanan-stok 10 90
s3 s1 auth 5 20
s5 s1 layanan-bayar 100 240
s7 s2 redis-GET 15 25
""",
        "solution": """import sys

span = {}
anak = {}
akar = None
for baris in sys.stdin.read().splitlines():
    b = baris.split()
    if not b:
        continue
    sid, induk, nama, mulai, selesai = b[0], b[1], b[2], int(b[3]), int(b[4])
    span[sid] = {"nama": nama, "mulai": mulai, "selesai": selesai}
    if induk == "-":
        akar = sid
    else:
        anak.setdefault(induk, []).append(sid)

kritis = []
s = akar
while s is not None:
    kritis.append(s)
    calon = anak.get(s, [])
    s = max(calon, key=lambda c: (span[c]["selesai"], c)) if calon else None


def cetak(sid, kedalaman):
    sp = span[sid]
    tanda = " *" if sid in kritis else ""
    print(f"{'  ' * kedalaman}{sp['nama']} {sp['selesai'] - sp['mulai']}ms{tanda}")
    for c in sorted(anak.get(sid, []), key=lambda c: (span[c]["mulai"], c)):
        cetak(c, kedalaman + 1)


cetak(akar, 0)
print("jalur kritis:", " > ".join(span[x]["nama"] for x in kritis))
""",
    },
    {
        "title": "Latihan 22: Alarm Anggaran dan Alokasi Biaya per Tag",
        "difficulty": "Lanjut",
        "question": [
            "Tiru laporan biaya bulanan: alokasi per tag tim, sumber tanpa tag,",
            "kapan ambang anggaran terlampaui, dan prakiraan akhir bulan.",
            "",
            "Masukan dari stdin: baris 'anggaran <dolar>', baris 'hari <jumlah",
            "hari dalam bulan>', lalu baris tagihan 'tanggal,layanan,tim,biaya'.",
            "Tim '-' berarti sumber daya tanpa tag.",
            "",
            "Yang dicetak:",
            "  1. 'biaya per tim:' lalu tiap tim (tanpa tag ditulis '(tanpa",
            "     tag)'), urut biaya terbesar, format f'  {tim:12} ${nilai:>7.2f}",
            "     {persen:5.1f}%' (dua spasi sebelum persen).",
            "  2. 'sumber tanpa tag:' diikuti layanan dan totalnya, urut abjad.",
            "  3. 'anggaran $<anggaran>:' lalu untuk ambang 50, 80, 100 persen:",
            "     tanggal pertama biaya kumulatif mencapai ambang itu, atau",
            "     'belum terlampaui'.",
            "  4. 'total <n> hari:' (n = tanggal terakhir di data) dan",
            "     'prakiraan akhir bulan:' = total / n x hari, ditambah",
            "     '  (melewati anggaran)' kalau lebih besar dari anggaran.",
            "",
            "Pakai modul decimal supaya penjumlahan uang nggak meleset.",
            "",
            "Masukan:",
            "  anggaran 300",
            "  hari 30",
            "  2026-10-01,EC2,toko,9.60",
            "  2026-10-01,RDS,toko,5.40",
            "  2026-10-01,NAT Gateway,-,3.24",
            "  2026-10-02,EC2,toko,9.60",
            "  2026-10-02,S3,data,2.10",
            "  2026-10-02,NAT Gateway,-,3.24",
            "  2026-10-03,EC2,toko,9.60",
            "  2026-10-03,EC2,data,24.00",
            "  2026-10-03,NAT Gateway,-,3.24",
            "  2026-10-04,EC2,toko,9.60",
            "  2026-10-04,EC2,data,24.00",
            "  2026-10-04,CloudWatch Logs,-,6.80",
            "  2026-10-05,EC2,toko,9.60",
            "  2026-10-05,EC2,data,24.00",
            "  2026-10-05,NAT Gateway,-,3.24",
            "  2026-10-06,EC2,toko,9.60",
            "  2026-10-06,EC2,data,24.00",
            "  2026-10-06,RDS,toko,5.40",
            "  2026-10-07,EC2,toko,9.60",
            "  2026-10-07,EC2,data,24.00",
            "  2026-10-07,NAT Gateway,-,3.24",
            "  2026-10-08,EC2,toko,9.60",
            "  2026-10-08,EC2,data,24.00",
            "  2026-10-08,CloudWatch Logs,-,6.80",
            "",
            "Keluaran yang diharapkan:",
            "biaya per tim:",
            "  data         $ 146.10   55.4%",
            "  toko         $  87.60   33.2%",
            "  (tanpa tag)  $  29.80   11.3%",
            "sumber tanpa tag: CloudWatch Logs $13.60, NAT Gateway $16.20",
            "anggaran $300.00:",
            "   50% terlampaui 2026-10-06 (kumulatif $186.26)",
            "   80% terlampaui 2026-10-08 (kumulatif $263.50)",
            "  100% belum terlampaui",
            "total 8 hari: $263.50",
            "prakiraan akhir bulan: $988.12  (melewati anggaran)",
        ],
        "hints": [
            "Laporan biaya selalu dimulai dari pertanyaan 'milik siapa', jadi kelompokkan dulu tiap baris tagihan menurut tim sebelum menghitung hal lain.",
            "Simpan jumlah per tim, jumlah per layanan tanpa tag, dan jumlah per tanggal dalam tiga dict terpisah, semuanya bernilai Decimal.",
            "Untuk ambang, telusuri tanggal secara urut sambil menambah kumulatif, dan catat tanggal pertama ketika kumulatif >= anggaran x ambang / 100.",
        ],
        "stdin": """anggaran 300
hari 30
2026-10-01,EC2,toko,9.60
2026-10-01,RDS,toko,5.40
2026-10-01,NAT Gateway,-,3.24
2026-10-02,EC2,toko,9.60
2026-10-02,S3,data,2.10
2026-10-02,NAT Gateway,-,3.24
2026-10-03,EC2,toko,9.60
2026-10-03,EC2,data,24.00
2026-10-03,NAT Gateway,-,3.24
2026-10-04,EC2,toko,9.60
2026-10-04,EC2,data,24.00
2026-10-04,CloudWatch Logs,-,6.80
2026-10-05,EC2,toko,9.60
2026-10-05,EC2,data,24.00
2026-10-05,NAT Gateway,-,3.24
2026-10-06,EC2,toko,9.60
2026-10-06,EC2,data,24.00
2026-10-06,RDS,toko,5.40
2026-10-07,EC2,toko,9.60
2026-10-07,EC2,data,24.00
2026-10-07,NAT Gateway,-,3.24
2026-10-08,EC2,toko,9.60
2026-10-08,EC2,data,24.00
2026-10-08,CloudWatch Logs,-,6.80
""",
        "solution": """import sys
from decimal import Decimal

anggaran = Decimal(0)
hari_bulan = 30
baris_tagihan = []
for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    if baris.startswith("anggaran "):
        anggaran = Decimal(baris.split()[1])
    elif baris.startswith("hari "):
        hari_bulan = int(baris.split()[1])
    else:
        tanggal, layanan, tim, biaya = baris.split(",")
        baris_tagihan.append((tanggal, layanan, tim, Decimal(biaya)))

per_tim = {}
tanpa_tag = {}
for tanggal, layanan, tim, biaya in baris_tagihan:
    if tim == "-":
        tanpa_tag[layanan] = tanpa_tag.get(layanan, Decimal(0)) + biaya
        tim = "(tanpa tag)"
    per_tim[tim] = per_tim.get(tim, Decimal(0)) + biaya

total = sum(per_tim.values())
print("biaya per tim:")
for tim, nilai in sorted(per_tim.items(), key=lambda x: (-x[1], x[0])):
    persen = nilai * 100 / total
    print(f"  {tim:12} ${nilai:>7.2f}  {persen:5.1f}%")
print("sumber tanpa tag:", ", ".join(
    f"{l} ${v:.2f}" for l, v in sorted(tanpa_tag.items())))

harian = {}
for tanggal, _, _, biaya in baris_tagihan:
    harian[tanggal] = harian.get(tanggal, Decimal(0)) + biaya
kumulatif = Decimal(0)
ambang = [50, 80, 100]
lewat = {}
for tanggal in sorted(harian):
    kumulatif += harian[tanggal]
    for a in ambang:
        if a not in lewat and kumulatif >= anggaran * a / 100:
            lewat[a] = (tanggal, kumulatif)
print(f"anggaran ${anggaran:.2f}:")
for a in ambang:
    if a in lewat:
        tgl, nilai = lewat[a]
        print(f"  {a:3}% terlampaui {tgl} (kumulatif ${nilai:.2f})")
    else:
        print(f"  {a:3}% belum terlampaui")

hari_ini = int(max(harian)[-2:])
prakiraan = total / hari_ini * hari_bulan
print(f"total {hari_ini} hari: ${total:.2f}")
print(f"prakiraan akhir bulan: ${prakiraan:.2f}"
      + ("  (melewati anggaran)" if prakiraan > anggaran else ""))
""",
    },
    {
        "title": "Latihan 23: Proyek Akhir: Platform Deploy Mini",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Satukan isi kurikulum ini dalam satu program: platform deploy",
            "mini yang membaca manifest, menjalankan pipeline dengan cache,",
            "melakukan rolling update, mencetak metrik, dan memutuskan alarm",
            "SLO. Semua memakai jam tiruan supaya hasilnya selalu sama.",
            "",
            "1. Pengurai YAML subset. Manifest datang dari stdin. Dukung",
            "   'kunci: nilai', peta bersarang dengan indentasi spasi, daftar",
            "   '- butir' berisi nilai tunggal, dan komentar '#'. Nilai yang",
            "   berupa angka bulat diubah jadi int. Tab ditolak.",
            "",
            "2. Pipeline sebagai DAG dengan cache. Tiap job di 'pipeline' boleh",
            "   punya 'butuh' (job lain) dan 'pakai' (nama berkas di",
            "   'berkas'). Urutkan dengan topological sort; kalau beberapa job",
            "   siap bersamaan, ambil yang namanya lebih dulu menurut abjad.",
            "   Hash job = sha256 dari nama job, lalu hash job yang dibutuhkan,",
            "   lalu 'nama=isi' tiap berkas yang dipakai. Hash yang sudah ada",
            "   di cache berarti CACHED, selain itu BUILD (lalu masuk cache).",
            "   Jalankan pipeline dua kali: sekali dengan 'berkas', sekali",
            "   lagi sesudah berkas ditimpa isi 'ubah'. Cache dipakai bersama.",
            "",
            "3. Rolling update dari 'dari' ke 'ke', dengan 'replika' pod,",
            "   maxSurge 'surge', dan maxUnavailable 0. Pod lama mulai dalam",
            "   keadaan siap. Pod baru siap setelah umurnya 'siap_setelah'",
            "   tick. Tiap tick (t=1 sampai 'batas'): naikkan umur pod baru",
            "   dan perbarui status siapnya; selama masih ada pod lama dan",
            "   jumlah pod siap lebih dari 'replika', hapus pod lama bernomor",
            "   terkecil; lalu selama jumlah pod kurang dari replika + surge",
            "   dan pod baru kurang dari replika, buat pod baru bernama",
            "   '<aplikasi>-<ke>-<nomor>'. Berhenti saat semua pod adalah",
            "   versi baru yang siap dan jumlahnya sama dengan replika. Kalau",
            "   batas habis, cetak '  rollout macet, kembalikan ke versi lama'.",
            "",
            "4. Metrik format teks Prometheus: jumlah job BUILD dan CACHED,",
            "   jumlah pod siap per versi, dan jumlah permintaan 2xx dan 5xx",
            "   dari 'permintaan' (tiap butir 'total/gagal' satu menit).",
            "",
            "5. Alarm SLO dengan dua jendela. Error budget = (100 - target) /",
            "   100. Burn rate = (jumlah gagal / jumlah total) / error budget.",
            "   Hitung untuk semua menit (jendela panjang) dan untuk",
            "   'jendela_pendek' menit terakhir. Alarm FIRING kalau keduanya",
            "   >= 'ambang', selain itu OK. Cetak burn rate dua angka di",
            "   belakang koma.",
            "",
            "Bentuk tiap baris persis seperti keluaran di bawah.",
            "",
            "Masukan:",
            "  aplikasi: toko",
            "  replika: 3",
            "  berkas:",
            "    app.py: kode-v2",
            "    tes.py: tes-a",
            "    Dockerfile: from-python-slim",
            "    README.md: dok-a",
            "  ubah:",
            "    tes.py: tes-b",
            "  pipeline:",
            "    lint:",
            "      pakai:",
            "        - app.py",
            "    tes:",
            "      butuh:",
            "        - lint",
            "      pakai:",
            "        - app.py",
            "        - tes.py",
            "    image:",
            "      butuh:",
            "        - tes",
            "      pakai:",
            "        - Dockerfile",
            "        - app.py",
            "    docs:",
            "      pakai:",
            "        - README.md",
            "  rilis:",
            "    dari: v1",
            "    ke: v2",
            "    surge: 1",
            "    siap_setelah: 2",
            "    batas: 12",
            "  permintaan:",
            "    - 1000/4",
            "    - 1000/6",
            "    - 1000/10",
            "    - 1000/30",
            "    - 1000/40",
            "    - 1000/38",
            "  slo:",
            "    target: 99",
            "    ambang: 2",
            "    jendela_pendek: 2",
            "",
            "Keluaran yang diharapkan:",
            "== pipeline 1 ==",
            "  docs   BUILD",
            "  lint   BUILD",
            "  tes    BUILD",
            "  image  BUILD",
            "== pipeline 2 (sesudah ubah: tes.py) ==",
            "  docs   CACHED",
            "  lint   CACHED",
            "  tes    BUILD",
            "  image  BUILD",
            "== rolling update v1 -> v2 ==",
            "  t=1 buat toko-v2-1 | v1 siap 3, v2 siap 0/1",
            "  t=2 menunggu | v1 siap 3, v2 siap 0/1",
            "  t=3 hapus toko-v1-1, buat toko-v2-2 | v1 siap 2, v2 siap 1/2",
            "  t=4 menunggu | v1 siap 2, v2 siap 1/2",
            "  t=5 hapus toko-v1-2, buat toko-v2-3 | v1 siap 1, v2 siap 2/3",
            "  t=6 menunggu | v1 siap 1, v2 siap 2/3",
            "  t=7 hapus toko-v1-3 | v1 siap 0, v2 siap 3/3",
            "  selesai di t=7",
            "== metrik ==",
            "# TYPE pipeline_job_total counter",
            "pipeline_job_total{hasil=\"build\"} 6",
            "pipeline_job_total{hasil=\"cached\"} 2",
            "# TYPE deploy_pod_siap gauge",
            "deploy_pod_siap{app=\"toko\",versi=\"v1\"} 0",
            "deploy_pod_siap{app=\"toko\",versi=\"v2\"} 3",
            "# TYPE http_requests_total counter",
            "http_requests_total{app=\"toko\",kode=\"2xx\"} 5872",
            "http_requests_total{app=\"toko\",kode=\"5xx\"} 128",
            "== SLO ==",
            "  target 99%, ambang burn rate 2",
            "  burn rate 6 menit: 2.13",
            "  burn rate 2 menit terakhir: 3.90",
            "  alarm: FIRING",
            "",
            "Perhatikan pipeline kedua: lint dan docs tetap CACHED karena",
            "masukannya nggak berubah, sedangkan image ikut BUILD walau",
            "berkasnya sama, karena hash tes yang dibutuhkannya berubah.",
            "Dan burn rate pendek 3,90 saja nggak cukup; alarm menyala karena",
            "jendela panjang juga sudah 2,13.",
        ],
        "hints": [
            "Pecah proyek ini jadi lima fungsi yang bisa diuji sendiri-sendiri, persis seperti latihan pengurai YAML, cache layer, DAG pipeline, reconciler, dan rate di bab-bab sebelumnya.",
            "Untuk pengurai YAML, ubah dulu tiap baris jadi pasangan (indentasi, isi) lalu tulis fungsi rekursif blok(i, indent) yang mengembalikan nilai dan indeks baris berikutnya; daftar dikenali dari isi yang diawali '- '.",
            "Untuk cache, hash setiap job dengan hashlib.sha256 lalu update() berturut-turut dengan nama job, hash dependensinya, dan 'nama=isi' tiap berkas, lalu simpan hexdigest() di sebuah set yang dipakai kedua putaran.",
            "Untuk rolling update, simpan pod sebagai dict berisi nama, versi, umur, dan siap; tiap tick, hapus pod lama dengan while selama jumlah siap > replika, lalu buat pod baru dengan while selama ruang surge masih ada.",
        ],
        "stdin": """aplikasi: toko
replika: 3
berkas:
  app.py: kode-v2
  tes.py: tes-a
  Dockerfile: from-python-slim
  README.md: dok-a
ubah:
  tes.py: tes-b
pipeline:
  lint:
    pakai:
      - app.py
  tes:
    butuh:
      - lint
    pakai:
      - app.py
      - tes.py
  image:
    butuh:
      - tes
    pakai:
      - Dockerfile
      - app.py
  docs:
    pakai:
      - README.md
rilis:
  dari: v1
  ke: v2
  surge: 1
  siap_setelah: 2
  batas: 12
permintaan:
  - 1000/4
  - 1000/6
  - 1000/10
  - 1000/30
  - 1000/40
  - 1000/38
slo:
  target: 99
  ambang: 2
  jendela_pendek: 2
""",
        "solution": "import hashlib\nimport sys\n\n\n# 1. Pengurai YAML subset: kunci: nilai, peta bersarang, daftar \"- butir\".\ndef urai_yaml(teks):\n    baris = []\n    for nomor, b in enumerate(teks.splitlines(), 1):\n        if \"\\t\" in b:\n            raise ValueError(f\"baris {nomor}: tab tidak boleh dipakai\")\n        isi = b.split(\"#\")[0].rstrip()\n        if isi.strip():\n            baris.append((len(isi) - len(isi.lstrip()), isi.strip()))\n\n    def nilai(teks_nilai):\n        return int(teks_nilai) if teks_nilai.lstrip(\"-\").isdigit() else teks_nilai\n\n    def blok(i, indent):\n        if baris[i][1].startswith(\"- \"):\n            hasil = []\n            while i < len(baris) and baris[i][0] == indent:\n                hasil.append(nilai(baris[i][1][2:].strip()))\n                i += 1\n            return hasil, i\n        hasil = {}\n        while i < len(baris) and baris[i][0] == indent:\n            kunci, _, sisa = baris[i][1].partition(\":\")\n            sisa = sisa.strip()\n            i += 1\n            if sisa:\n                hasil[kunci] = nilai(sisa)\n            elif i < len(baris) and baris[i][0] > indent:\n                hasil[kunci], i = blok(i, baris[i][0])\n            else:\n                hasil[kunci] = None\n        return hasil, i\n\n    return blok(0, baris[0][0])[0]\n\n\nmanifest = urai_yaml(sys.stdin.read())\nnama_app = manifest[\"aplikasi\"]\npipeline = manifest[\"pipeline\"]\nmetrik_build = {\"build\": 0, \"cached\": 0}\n\n\n# 2. Pipeline sebagai DAG dengan cache berbasis hash.\ndef urutan_dag(jobs):\n    sisa = {j: set(jobs[j].get(\"butuh\") or []) for j in jobs}\n    urut = []\n    while sisa:\n        siap = sorted(j for j in sisa if not sisa[j])\n        if not siap:\n            raise ValueError(\"siklus di pipeline: \" + \", \".join(sorted(sisa)))\n        j = siap[0]\n        urut.append(j)\n        del sisa[j]\n        for lain in sisa.values():\n            lain.discard(j)\n    return urut\n\n\ndef jalankan_pipeline(berkas, cache, label):\n    print(f\"== pipeline {label} ==\")\n    hash_job = {}\n    for job in urutan_dag(pipeline):\n        h = hashlib.sha256(job.encode())\n        for dep in pipeline[job].get(\"butuh\") or []:\n            h.update(hash_job[dep].encode())\n        for nama in pipeline[job].get(\"pakai\") or []:\n            h.update(f\"{nama}={berkas[nama]}\".encode())\n        hash_job[job] = h.hexdigest()\n        if hash_job[job] in cache:\n            hasil = \"CACHED\"\n            metrik_build[\"cached\"] += 1\n        else:\n            hasil = \"BUILD\"\n            metrik_build[\"build\"] += 1\n            cache.add(hash_job[job])\n        print(f\"  {job:6} {hasil}\")\n\n\nberkas = dict(manifest[\"berkas\"])\ncache = set()\njalankan_pipeline(berkas, cache, \"1\")\nberkas.update(manifest[\"ubah\"])\njalankan_pipeline(berkas, cache, \"2 (sesudah ubah: \" + \", \".join(manifest[\"ubah\"]) + \")\")\n\n# 3. Rolling update dengan health check tiruan dan jam tiruan.\nrilis = manifest[\"rilis\"]\nreplika = manifest[\"replika\"]\nsurge = rilis[\"surge\"]\nsiap_setelah = rilis[\"siap_setelah\"]\npods = [{\"nama\": f\"{nama_app}-{rilis['dari']}-{i}\", \"versi\": rilis[\"dari\"],\n         \"umur\": siap_setelah, \"siap\": True} for i in range(1, replika + 1)]\nnomor_baru = 0\nprint(f\"== rolling update {rilis['dari']} -> {rilis['ke']} ==\")\nfor t in range(1, rilis[\"batas\"] + 1):\n    aksi = []\n    for p in pods:\n        if p[\"versi\"] == rilis[\"ke\"]:\n            p[\"umur\"] += 1\n            p[\"siap\"] = p[\"umur\"] >= siap_setelah\n    lama = [p for p in pods if p[\"versi\"] == rilis[\"dari\"]]\n    while lama and sum(p[\"siap\"] for p in pods) > replika:\n        p = lama.pop(0)\n        pods.remove(p)\n        aksi.append(\"hapus \" + p[\"nama\"])\n    baru = [p for p in pods if p[\"versi\"] == rilis[\"ke\"]]\n    while len(pods) < replika + surge and len(baru) < replika:\n        nomor_baru += 1\n        p = {\"nama\": f\"{nama_app}-{rilis['ke']}-{nomor_baru}\", \"versi\": rilis[\"ke\"],\n             \"umur\": 0, \"siap\": False}\n        pods.append(p)\n        baru.append(p)\n        aksi.append(\"buat \" + p[\"nama\"])\n    siap_lama = sum(p[\"siap\"] for p in pods if p[\"versi\"] == rilis[\"dari\"])\n    siap_baru = sum(p[\"siap\"] for p in pods if p[\"versi\"] == rilis[\"ke\"])\n    jumlah_baru = sum(p[\"versi\"] == rilis[\"ke\"] for p in pods)\n    print(f\"  t={t} {', '.join(aksi) if aksi else 'menunggu'} | \"\n          f\"{rilis['dari']} siap {siap_lama}, {rilis['ke']} siap {siap_baru}/{jumlah_baru}\")\n    if siap_baru == replika and len(pods) == replika:\n        print(f\"  selesai di t={t}\")\n        break\nelse:\n    print(\"  rollout macet, kembalikan ke versi lama\")\n\n# 4. Metrik dalam format teks Prometheus.\npermintaan = [tuple(int(x) for x in m.split(\"/\")) for m in manifest[\"permintaan\"]]\ntotal = sum(p[0] for p in permintaan)\ngagal = sum(p[1] for p in permintaan)\nprint(\"== metrik ==\")\nprint(\"# TYPE pipeline_job_total counter\")\nfor hasil in (\"build\", \"cached\"):\n    print(f'pipeline_job_total{{hasil=\"{hasil}\"}} {metrik_build[hasil]}')\nprint(\"# TYPE deploy_pod_siap gauge\")\nfor versi in (rilis[\"dari\"], rilis[\"ke\"]):\n    jumlah = sum(p[\"siap\"] for p in pods if p[\"versi\"] == versi)\n    print(f'deploy_pod_siap{{app=\"{nama_app}\",versi=\"{versi}\"}} {jumlah}')\nprint(\"# TYPE http_requests_total counter\")\nprint(f'http_requests_total{{app=\"{nama_app}\",kode=\"2xx\"}} {total - gagal}')\nprint(f'http_requests_total{{app=\"{nama_app}\",kode=\"5xx\"}} {gagal}')\n\n# 5. Alarm SLO dengan dua jendela burn rate.\nslo = manifest[\"slo\"]\nanggaran_galat = (100 - slo[\"target\"]) / 100\n\n\ndef burn(daftar):\n    return sum(g for _, g in daftar) / sum(t for t, _ in daftar) / anggaran_galat\n\n\npanjang = burn(permintaan)\npendek = burn(permintaan[-slo[\"jendela_pendek\"]:])\nstatus = \"FIRING\" if panjang >= slo[\"ambang\"] and pendek >= slo[\"ambang\"] else \"OK\"\nprint(\"== SLO ==\")\nprint(f\"  target {slo['target']}%, ambang burn rate {slo['ambang']}\")\nprint(f\"  burn rate {len(permintaan)} menit: {panjang:.2f}\")\nprint(f\"  burn rate {slo['jendela_pendek']} menit terakhir: {pendek:.2f}\")\nprint(f\"  alarm: {status}\")\n",
    },
]
