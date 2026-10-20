"""Kurikulum Backend & API.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

BACKEND_EXERCISES = [
    {
        "title": "Latihan 1: Pengurai Permintaan HTTP Mentah",
        "difficulty": "Mudah",
        "question": [
            "Backend selalu mulai dari teks HTTP mentah. Tulis program yang",
            "membaca satu permintaan HTTP dari input, lalu mencetak isinya",
            "dengan rapi.",
            "",
            "Bentuk input: baris pertama berisi metode, target, dan versi.",
            "Sesudahnya baris header berbentuk Nama: nilai, lalu satu baris",
            "kosong, lalu body (boleh kosong).",
            "",
            "Cetak berurutan:",
            "  - metode, path (tanpa query), dan versi",
            "  - query sebagai dict yang kuncinya diurutkan; pasangan dipisah",
            "    &, kunci dan nilai dipisah =, dan + diganti spasi",
            "  - header, satu per baris dengan dua spasi di depan, nama header",
            "    huruf kecil, diurutkan menurut nama",
            "  - panjang body dalam byte UTF-8 (baris baru di akhir input",
            "    nggak dihitung)",
            "",
            "Untuk input berikut:",
            "  GET /cari?q=kopi+susu&hal=2 HTTP/1.1",
            "  Host: toko.test",
            "  Accept: */*",
            "  User-Agent: curl/8.11",
            "  (baris kosong)",
            "",
            "Keluaran yang diharapkan:",
            "metode: GET",
            "path: /cari",
            "versi: HTTP/1.1",
            "query: {'hal': '2', 'q': 'kopi susu'}",
            "header:",
            "  accept: */*",
            "  host: toko.test",
            "  user-agent: curl/8.11",
            "panjang body: 0",
            "",
            "Program juga diuji dengan permintaan POST yang membawa body JSON.",
        ],
        "hints": [
            "Pisahkan input jadi baris-baris, lalu ingat bahwa baris kosong pertama adalah batas antara header dan body.",
            "Baris pertama dipecah dengan split(\" \") jadi tiga bagian, lalu target dipecah lagi dengan partition(\"?\") untuk memisahkan path dan query.",
            "Untuk header pakai partition(\":\") lalu strip() dan lower(); untuk panjang body hitung len(body.encode(\"utf-8\")).",
        ],
        "stdin_list": [
            """GET /cari?q=kopi+susu&hal=2 HTTP/1.1
Host: toko.test
Accept: */*
User-Agent: curl/8.11

""",
            """POST /pesanan HTTP/1.1
Host: toko.test
Content-Type: application/json
X-Request-ID: abc-123

{"menu": "es teh", "jumlah": 2}
""",
        ],
        "solution": "import sys\n\nteks = sys.stdin.read()\nbaris = [b.rstrip(\"\\r\") for b in teks.split(\"\\n\")]\n\nmetode, target, versi = baris[0].split(\" \")\npath, _, teks_query = target.partition(\"?\")\npasangan = {}\nfor potong in teks_query.split(\"&\"):\n    if potong:\n        kunci, _, nilai = potong.partition(\"=\")\n        pasangan[kunci] = nilai.replace(\"+\", \" \")\nquery = dict(sorted(pasangan.items()))\n\nheader = {}\ni = 1\nwhile i < len(baris) and baris[i] != \"\":\n    nama, _, nilai = baris[i].partition(\":\")\n    header[nama.strip().lower()] = nilai.strip()\n    i += 1\n\nbody = \"\\n\".join(baris[i + 1:]).rstrip(\"\\n\")\n\nprint(\"metode:\", metode)\nprint(\"path:\", path)\nprint(\"versi:\", versi)\nprint(\"query:\", query)\nprint(\"header:\")\nfor nama in sorted(header):\n    print(f\"  {nama}: {header[nama]}\")\nprint(\"panjang body:\", len(body.encode(\"utf-8\")))\n",
    },
    {
        "title": "Latihan 2: Router Mini dengan Parameter Path",
        "difficulty": "Mudah",
        "question": [
            "Lengkapi router dari materi supaya bisa membedakan 404 dan 405.",
            "Daftar rute ditanam di program:",
            "  GET    /users                       daftar_user",
            "  POST   /users                       buat_user",
            "  GET    /users/{id}                  lihat_user",
            "  DELETE /users/{id}                  hapus_user",
            "  GET    /users/{id}/posts/{post_id}  lihat_post",
            "",
            "Input berisi beberapa baris berbentuk METODE PATH. Untuk tiap",
            "baris, cetak baris itu, lalu -> dan hasilnya:",
            "  - cocok: 200, nama handler, lalu parameter nama=nilai sesuai",
            "    urutan di pola, dipisah spasi",
            "  - path cocok tapi metodenya nggak ada: 405 Method Not Allowed",
            "    dengan daftar metode yang sah diurutkan abjad",
            "  - path nggak cocok sama sekali: 404 Not Found",
            "",
            "Untuk input:",
            "  GET /users",
            "  POST /users",
            "  GET /users/7",
            "  GET /users/7/posts/3",
            "  PUT /users/7",
            "  DELETE /users",
            "  GET /produk",
            "  GET /users/7/",
            "",
            "Keluaran yang diharapkan:",
            "GET /users -> 200 daftar_user",
            "POST /users -> 200 buat_user",
            "GET /users/7 -> 200 lihat_user id=7",
            "GET /users/7/posts/3 -> 200 lihat_post id=7 post_id=3",
            "PUT /users/7 -> 405 Method Not Allowed (Allow: DELETE, GET)",
            "DELETE /users -> 405 Method Not Allowed (Allow: GET, POST)",
            "GET /produk -> 404 Not Found",
            "GET /users/7/ -> 404 Not Found",
        ],
        "hints": [
            "Keputusan 405 butuh informasi dari semua rute: sebuah path baru bisa dinyatakan 404 kalau nggak ada satu pun pola yang cocok, apa pun metodenya.",
            "Saat menelusuri rute, kumpulkan metode dari pola yang path-nya cocok tapi metodenya beda ke sebuah set, lalu putuskan 405 atau 404 sesudah perulangan selesai.",
            "Ubah pola jadi regex dengan re.sub(r\"\\{(\\w+)\\}\", r\"(?P<\\1>[^/]+)\", pola) dan apit dengan ^ dan $, lalu pakai groupdict() untuk parameternya.",
        ],
        "stdin": """GET /users
POST /users
GET /users/7
GET /users/7/posts/3
PUT /users/7
DELETE /users
GET /produk
GET /users/7/
""",
        "solution": "import re\nimport sys\n\nRUTE = [\n    (\"GET\", \"/users\", \"daftar_user\"),\n    (\"POST\", \"/users\", \"buat_user\"),\n    (\"GET\", \"/users/{id}\", \"lihat_user\"),\n    (\"DELETE\", \"/users/{id}\", \"hapus_user\"),\n    (\"GET\", \"/users/{id}/posts/{post_id}\", \"lihat_post\"),\n]\n\n\ndef jadi_regex(pola):\n    return re.compile(\"^\" + re.sub(r\"\\{(\\w+)\\}\", r\"(?P<\\1>[^/]+)\", pola) + \"$\")\n\n\nTABEL = [(m, jadi_regex(p), h) for m, p, h in RUTE]\n\n\ndef cocokkan(metode, path):\n    metode_lain = set()\n    for m, regex, handler in TABEL:\n        hasil = regex.match(path)\n        if not hasil:\n            continue\n        if m == metode:\n            return 200, handler, hasil.groupdict()\n        metode_lain.add(m)\n    if metode_lain:\n        return 405, None, sorted(metode_lain)\n    return 404, None, None\n\n\nfor baris in sys.stdin.read().splitlines():\n    if not baris.strip():\n        continue\n    metode, path = baris.split()\n    status, handler, data = cocokkan(metode, path)\n    if status == 200:\n        param = \" \".join(f\"{k}={v}\" for k, v in data.items())\n        print(f\"{baris} -> 200 {handler} {param}\".rstrip())\n    elif status == 405:\n        print(f\"{baris} -> 405 Method Not Allowed (Allow: {', '.join(data)})\")\n    else:\n        print(f\"{baris} -> 404 Not Found\")\n",
    },
    {
        "title": "Latihan 3: Validator Skema JSON Mini",
        "difficulty": "Mudah",
        "question": [
            "Tulis validator kecil yang meniru sebagian JSON Schema. Skema",
            "berikut ditanam di program:",
            "",
            "  SKEMA = {",
            "      \"type\": \"object\",",
            "      \"required\": [\"nama\", \"umur\"],",
            "      \"properties\": {",
            "          \"nama\": {\"type\": \"string\", \"minLength\": 2},",
            "          \"umur\": {\"type\": \"integer\", \"minimum\": 0},",
            "          \"tinggi\": {\"type\": \"number\", \"minimum\": 50},",
            "          \"aktif\": {\"type\": \"boolean\"},",
            "          \"alamat\": {",
            "              \"type\": \"object\",",
            "              \"required\": [\"kota\"],",
            "              \"properties\": {",
            "                  \"kota\": {\"type\": \"string\", \"minLength\": 3},",
            "              },",
            "          },",
            "      },",
            "  }",
            "",
            "Aturannya:",
            "  - type: object, string, integer, number, atau boolean. true dan",
            "    false bukan integer maupun number. number menerima bilangan",
            "    bulat dan pecahan.",
            "  - Kalau tipenya salah, laporkan tipenya saja dan jangan periksa",
            "    aturan lain untuk nilai itu.",
            "  - required diperiksa dulu sesuai urutannya, baru properties",
            "    sesuai urutan di skema. Properti yang nggak ada dilewati.",
            "  - Jalur memakai bentuk /umur atau /alamat/kota; akar ditulis /.",
            "  - Pesan: \"wajib ada\", \"tipe harus <tipe>\", \"minLength <n>\",",
            "    \"minimum <n>\".",
            "",
            "Input berisi satu dokumen JSON per baris. Cetak \"baris N: valid\",",
            "atau semua kesalahan dipisah \"; \", atau \"JSON rusak\".",
            "",
            "Keluaran yang diharapkan:",
            "baris 1: valid",
            "baris 2: /nama: minLength 2; /umur: minimum 0",
            "baris 3: /nama: wajib ada; /umur: tipe harus integer",
            "baris 4: /alamat/kota: minLength 3",
            "baris 5: /aktif: tipe harus boolean; /alamat/kota: wajib ada",
            "baris 6: /: tipe harus object",
            "baris 7: JSON rusak",
        ],
        "hints": [
            "Objek di dalam objek diperiksa dengan aturan yang sama, jadi satu fungsi rekursif yang menerima nilai, skema, dan jalurnya sudah cukup untuk semua tingkat.",
            "Periksa tipe paling awal dan langsung kembali kalau salah; kalau tipenya object, periksa required lalu panggil fungsi itu lagi untuk tiap properti yang ada.",
            "Karena bool adalah turunan int di Python, cek integer dengan isinstance(nilai, int) and not isinstance(nilai, bool), dan tangkap json.JSONDecodeError untuk baris yang rusak.",
        ],
        "stdin": """{"nama": "Sari", "umur": 17}
{"nama": "S", "umur": -1}
{"umur": true, "tinggi": 160.5}
{"nama": "Budi", "umur": 20, "alamat": {"kota": "Bo"}}
{"nama": "Ayu", "umur": 9, "alamat": {}, "aktif": "ya"}
[1, 2]
{"nama": "Rudi", "umur": 30,
""",
        "solution": """import json
import sys

SKEMA = {
    "type": "object",
    "required": ["nama", "umur"],
    "properties": {
        "nama": {"type": "string", "minLength": 2},
        "umur": {"type": "integer", "minimum": 0},
        "tinggi": {"type": "number", "minimum": 50},
        "aktif": {"type": "boolean"},
        "alamat": {
            "type": "object",
            "required": ["kota"],
            "properties": {"kota": {"type": "string", "minLength": 3}},
        },
    },
}


def cocok_tipe(nilai, tipe):
    if tipe == "object":
        return isinstance(nilai, dict)
    if tipe == "string":
        return isinstance(nilai, str)
    if tipe == "boolean":
        return isinstance(nilai, bool)
    if tipe == "integer":
        return isinstance(nilai, int) and not isinstance(nilai, bool)
    if tipe == "number":
        return isinstance(nilai, (int, float)) and not isinstance(nilai, bool)
    return False


def periksa(nilai, skema, jalur, galat):
    if not cocok_tipe(nilai, skema["type"]):
        galat.append(f"{jalur or '/'}: tipe harus {skema['type']}")
        return
    if skema["type"] == "object":
        for kunci in skema.get("required", []):
            if kunci not in nilai:
                galat.append(f"{jalur}/{kunci}: wajib ada")
        for kunci, sub in skema.get("properties", {}).items():
            if kunci in nilai:
                periksa(nilai[kunci], sub, f"{jalur}/{kunci}", galat)
    if "minLength" in skema and len(nilai) < skema["minLength"]:
        galat.append(f"{jalur}: minLength {skema['minLength']}")
    if "minimum" in skema and nilai < skema["minimum"]:
        galat.append(f"{jalur}: minimum {skema['minimum']}")


for nomor, baris in enumerate(sys.stdin.read().splitlines(), 1):
    try:
        dokumen = json.loads(baris)
    except json.JSONDecodeError:
        print(f"baris {nomor}: JSON rusak")
        continue
    galat = []
    periksa(dokumen, SKEMA, "", galat)
    print(f"baris {nomor}: " + ("valid" if not galat else "; ".join(galat)))
""",
    },
    {
        "title": "Latihan 4: Paginasi dan Error Problem Details",
        "difficulty": "Menengah",
        "question": [
            "Buat handler untuk GET /barang dengan paginasi offset. Datanya 23",
            "item bernama barang-01 sampai barang-23, ditanam di program.",
            "",
            "Input satu baris berisi query string tanpa tanda tanya, misalnya",
            "page=2&per_page=5. Aturannya:",
            "  - page bawaan 1, harus bilangan bulat minimal 1.",
            "  - per_page bawaan 10, harus bilangan bulat 1 sampai 20.",
            "  - Query yang salah dibalas 400 dengan detail \"page harus",
            "    minimal 1\", \"per_page harus 1 sampai 20\", atau \"<nama>",
            "    harus bilangan bulat\". page diperiksa lebih dulu.",
            "  - page melewati halaman terakhir dibalas 404 dengan detail",
            "    \"halaman N nggak ada, total M halaman\".",
            "  - Respons sukses berisi data, links (next dan prev, null kalau",
            "    nggak ada), dan meta (page, per_page, total, total_pages).",
            "  - Error memakai Problem Details: type about:blank, title berupa",
            "    frasa status (Bad Request atau Not Found), status, detail.",
            "",
            "Cetak tiga bagian: baris GET /barang?<query>, baris status dan",
            "Content-Type, lalu body dengan json.dumps(body, sort_keys=True,",
            "indent=2).",
            "",
            "Untuk input page=2&per_page=5, keluarannya:",
            "GET /barang?page=2&per_page=5",
            "200 application/json",
            "{",
            "  \"data\": [",
            "    \"barang-06\",",
            "    \"barang-07\",",
            "    \"barang-08\",",
            "    \"barang-09\",",
            "    \"barang-10\"",
            "  ],",
            "  \"links\": {",
            "    \"next\": \"/barang?page=3&per_page=5\",",
            "    \"prev\": \"/barang?page=1&per_page=5\"",
            "  },",
            "  \"meta\": {",
            "    \"page\": 2,",
            "    \"per_page\": 5,",
            "    \"total\": 23,",
            "    \"total_pages\": 5",
            "  }",
            "}",
            "",
            "Untuk input per_page=abc, keluarannya:",
            "GET /barang?per_page=abc",
            "400 application/problem+json",
            "{",
            "  \"detail\": \"per_page harus bilangan bulat\",",
            "  \"status\": 400,",
            "  \"title\": \"Bad Request\",",
            "  \"type\": \"about:blank\"",
            "}",
            "",
            "Untuk input page=4&per_page=8, keluarannya:",
            "GET /barang?page=4&per_page=8",
            "404 application/problem+json",
            "{",
            "  \"detail\": \"halaman 4 nggak ada, total 3 halaman\",",
            "  \"status\": 404,",
            "  \"title\": \"Not Found\",",
            "  \"type\": \"about:blank\"",
            "}",
        ],
        "hints": [
            "Pisahkan tiga urusan: membaca query jadi dict, memvalidasi angka dengan pesan yang tepat, lalu menghitung potongan data dan tautannya.",
            "Jumlah halaman adalah pembagian yang dibulatkan ke atas, yaitu (total + per_page - 1) // per_page, dan item pertama halaman p ada di indeks (p - 1) * per_page.",
            "Pakai str.isdigit() untuk memastikan teks berisi bilangan bulat sebelum int(), dan isi next atau prev dengan None supaya json.dumps menulis null.",
        ],
        "stdin_list": [
            """page=2&per_page=5
""",
            """page=3
""",
            """per_page=abc
""",
            """page=0
""",
            """page=4&per_page=8
""",
            """per_page=50
""",
        ],
        "solution": "import json\nimport sys\n\nBARANG = [f\"barang-{i:02d}\" for i in range(1, 24)]   # 23 item\nPER_HALAMAN_MAKS = 20\n\n\ndef masalah(status, title, detail):\n    return status, \"application/problem+json\", {\n        \"type\": \"about:blank\", \"title\": title,\n        \"status\": status, \"detail\": detail}\n\n\ndef bilangan(teks, nama, bawah, atas=None):\n    \"\"\"(angka, None) kalau sah, (None, pesan) kalau nggak.\"\"\"\n    if not teks.isdigit():\n        return None, f\"{nama} harus bilangan bulat\"\n    angka = int(teks)\n    if angka < bawah or (atas is not None and angka > atas):\n        batas = f\"{bawah} sampai {atas}\" if atas else f\"minimal {bawah}\"\n        return None, f\"{nama} harus {batas}\"\n    return angka, None\n\n\ndef tautan(halaman, per):\n    return f\"/barang?page={halaman}&per_page={per}\"\n\n\ndef daftar_barang(query):\n    param = {}\n    for potong in query.split(\"&\"):\n        if potong:\n            kunci, _, nilai = potong.partition(\"=\")\n            param[kunci] = nilai\n    page, galat = bilangan(param.get(\"page\", \"1\"), \"page\", 1)\n    if galat:\n        return masalah(400, \"Bad Request\", galat)\n    per, galat = bilangan(param.get(\"per_page\", \"10\"), \"per_page\", 1,\n                          PER_HALAMAN_MAKS)\n    if galat:\n        return masalah(400, \"Bad Request\", galat)\n    total_halaman = (len(BARANG) + per - 1) // per\n    if page > total_halaman:\n        return masalah(404, \"Not Found\",\n                       f\"halaman {page} nggak ada, total {total_halaman} halaman\")\n    awal = (page - 1) * per\n    body = {\n        \"data\": BARANG[awal:awal + per],\n        \"meta\": {\"page\": page, \"per_page\": per, \"total\": len(BARANG),\n                 \"total_pages\": total_halaman},\n        \"links\": {\n            \"next\": tautan(page + 1, per) if page < total_halaman else None,\n            \"prev\": tautan(page - 1, per) if page > 1 else None,\n        },\n    }\n    return 200, \"application/json\", body\n\n\nfor query in sys.stdin.read().splitlines():\n    status, jenis, body = daftar_barang(query.strip())\n    print(f\"GET /barang?{query.strip()}\")\n    print(status, jenis)\n    print(json.dumps(body, sort_keys=True, indent=2))\n",
    },
    {
        "title": "Latihan 5: Rantai Middleware Gaya Express",
        "difficulty": "Menengah",
        "question": [
            "Tiru cara Express menjalankan middleware, ditulis di Python. Buat",
            "kelas Respons (status(kode) yang mengembalikan dirinya, send(body),",
            "dan penanda terkirim) dan kelas App dengan:",
            "  - use(fn): middleware untuk semua permintaan",
            "  - get(path, fn): handler untuk GET dengan path persis",
            "  - tangani(req): menjalankan lapisan sesuai urutan daftar",
            "",
            "Aturan seperti Express:",
            "  - Fungsi biasa dipanggil fn(req, res, next). Lapisan berikutnya",
            "    cuma jalan kalau next() dipanggil.",
            "  - Fungsi berparameter empat, fn(err, req, res, next), adalah",
            "    penangan error. Ia dilewati selama nggak ada error.",
            "  - Kalau sebuah lapisan melempar exception, lompat ke penangan",
            "    error berikutnya.",
            "",
            "Pakai fungsi dan urutan pendaftaran ini persis:",
            "  pencatat: cetak \"  pencatat: METODE PATH\", lalu next()",
            "  cek_admin: path diawali /admin dan token bukan \"rahasia\" ->",
            "    cetak \"  cek_admin: ditolak\", kirim 401 \"butuh login\"; selain",
            "    itu cetak \"  cek_admin: lewat\", lalu next()",
            "  GET / -> kirim \"halo\"",
            "  GET /admin -> kirim \"panel admin\"",
            "  GET /rusak -> raise ValueError(\"database mati\")",
            "  GET /diam -> cetak \"  diam: lupa mengirim respons\" saja",
            "  tidak_ketemu: kirim 404 \"Cannot METODE PATH\"",
            "  penangan_error: cetak \"  penangan_error: <pesan>\", kirim 500",
            "    \"terjadi kesalahan\"",
            "",
            "Input: satu permintaan per baris, METODE PATH [token]. Cetak",
            "\">> \" diikuti baris itu, jejak lapisannya, lalu \"<< kode body\",",
            "atau \"<< menggantung, klien menunggu sampai timeout\" kalau nggak",
            "ada yang mengirim respons.",
            "",
            "Keluaran yang diharapkan:",
            ">> GET /",
            "  pencatat: GET /",
            "  cek_admin: lewat",
            "<< 200 halo",
            ">> GET /admin",
            "  pencatat: GET /admin",
            "  cek_admin: ditolak",
            "<< 401 butuh login",
            ">> GET /admin rahasia",
            "  pencatat: GET /admin",
            "  cek_admin: lewat",
            "<< 200 panel admin",
            ">> GET /rusak",
            "  pencatat: GET /rusak",
            "  cek_admin: lewat",
            "  penangan_error: database mati",
            "<< 500 terjadi kesalahan",
            ">> GET /diam",
            "  pencatat: GET /diam",
            "  cek_admin: lewat",
            "  diam: lupa mengirim respons",
            "<< menggantung, klien menunggu sampai timeout",
            ">> POST /",
            "  pencatat: POST /",
            "  cek_admin: lewat",
            "<< 404 Cannot POST /",
            ">> GET /kontak",
            "  pencatat: GET /kontak",
            "  cek_admin: lewat",
            "<< 404 Cannot GET /kontak",
        ],
        "hints": [
            "Simpan semua lapisan di satu daftar berisi metode, path, dan fungsi, karena Express pun menelusuri satu daftar dari atas ke bawah untuk tiap permintaan.",
            "Buat fungsi jalankan(i, err) yang mencari lapisan cocok mulai indeks i, lalu berikan next berupa fungsi yang memanggil jalankan(i_berikutnya, err) sehingga rantai berlanjut hanya saat next dipanggil.",
            "Jumlah parameter fungsi bisa dihitung dengan len(inspect.signature(fn).parameters), dan pembungkus try/except di sekitar pemanggilan fn yang memanggil jalankan(i, e) akan mengalihkan exception ke penangan error.",
        ],
        "stdin": """GET /
GET /admin
GET /admin rahasia
GET /rusak
GET /diam
POST /
GET /kontak
""",
        "solution": """import inspect
import sys


class Respons:
    def __init__(self):
        self.kode = 200
        self.body = None
        self.terkirim = False

    def status(self, kode):
        self.kode = kode
        return self

    def send(self, body):
        self.body = body
        self.terkirim = True


class App:
    def __init__(self):
        self.lapisan = []          # (metode, path, fungsi); None = semua

    def use(self, fn):
        self.lapisan.append((None, None, fn))

    def get(self, path, fn):
        self.lapisan.append(("GET", path, fn))

    def tangani(self, req):
        res = Respons()

        def jalankan(i, err=None):
            while i < len(self.lapisan):
                metode, path, fn = self.lapisan[i]
                i += 1
                if metode and (metode != req["metode"] or path != req["path"]):
                    continue
                penangan_error = len(inspect.signature(fn).parameters) == 4
                if penangan_error != (err is not None):
                    continue
                lanjut = lambda e=None, i=i: jalankan(i, e)
                try:
                    if err is not None:
                        fn(err, req, res, lanjut)
                    else:
                        fn(req, res, lanjut)
                except Exception as e:
                    jalankan(i, e)
                return

        jalankan(0)
        return res


def pencatat(req, res, next):
    print(f"  pencatat: {req['metode']} {req['path']}")
    next()


def cek_admin(req, res, next):
    if req["path"].startswith("/admin") and req["token"] != "rahasia":
        print("  cek_admin: ditolak")
        res.status(401).send("butuh login")
        return
    print("  cek_admin: lewat")
    next()


def beranda(req, res, next):
    res.send("halo")


def admin(req, res, next):
    res.send("panel admin")


def rusak(req, res, next):
    raise ValueError("database mati")


def diam(req, res, next):
    print("  diam: lupa mengirim respons")


def tidak_ketemu(req, res, next):
    res.status(404).send(f"Cannot {req['metode']} {req['path']}")


def penangan_error(err, req, res, next):
    print(f"  penangan_error: {err}")
    res.status(500).send("terjadi kesalahan")


app = App()
app.use(pencatat)
app.use(cek_admin)
app.get("/", beranda)
app.get("/admin", admin)
app.get("/rusak", rusak)
app.get("/diam", diam)
app.use(tidak_ketemu)
app.use(penangan_error)

for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    bagian = baris.split()
    req = {"metode": bagian[0], "path": bagian[1],
           "token": bagian[2] if len(bagian) > 2 else ""}
    print(">>", baris)
    res = app.tangani(req)
    if res.terkirim:
        print("<<", res.kode, res.body)
    else:
        print("<< menggantung, klien menunggu sampai timeout")
""",
    },
    {
        "title": "Latihan 6: Kontainer Dependency Injection Mini",
        "difficulty": "Menengah",
        "question": [
            "Buat kontainer DI kecil seperti yang dipakai NestJS, ditiru di",
            "Python. Kelas Kontainer punya:",
            "  - daftar(kelas, singleton=True)",
            "  - ambil(kelas): membuat objek kelas itu. Dependensinya dibaca",
            "    dari anotasi tipe parameter __init__ (pakai",
            "    typing.get_type_hints supaya anotasi berupa string seperti",
            "    \"Telur\" ikut terbaca), lalu diambil dari kontainer juga.",
            "  - Kelas singleton dibuat sekali lalu disimpan; yang bukan",
            "    singleton dibuat baru tiap kali diambil.",
            "  - Kelas yang belum didaftarkan: LookupError \"<Nama> belum",
            "    didaftarkan\".",
            "  - Dependensi melingkar: LookupError \"dependensi melingkar:",
            "    A -> B -> A\" memakai nama kelas.",
            "",
            "Pakai kelas-kelas ini, masing-masing mencetak saat dibuat:",
            "  Konfigurasi()                   \"membuat Konfigurasi\",",
            "                                  atribut url_db \"sqlite:///toko.db\"",
            "  Database(konfig: Konfigurasi)   \"membuat Database untuk <url_db>\"",
            "  Pencatat()                      \"membuat Pencatat\"",
            "  RepoBuku(db: Database)          \"membuat RepoBuku\"",
            "  LayananBuku(repo: RepoBuku, pencatat: Pencatat,",
            "              konfig: Konfigurasi) \"membuat LayananBuku\"",
            "  Ayam(telur: \"Telur\"), Telur(ayam: Ayam), Kucing (tanpa",
            "  dependensi, nggak didaftarkan)",
            "Simpan tiap dependensi sebagai atribut bernama sama.",
            "",
            "Skenario: daftarkan semuanya kecuali Kucing, dengan Pencatat",
            "bukan singleton. Ambil LayananBuku dua kali, cetak \"layanan",
            "sama:\" dan \"konfigurasi dipakai bersama:\" (konfig layanan",
            "versus konfig milik database di dalam repo). Ambil Pencatat dua",
            "kali dan cetak \"pencatat sama:\". Terakhir ambil Ayam lalu",
            "Kucing, cetak \"galat:\" diikuti pesannya.",
            "",
            "Keluaran yang diharapkan:",
            "membuat Konfigurasi",
            "membuat Database untuk sqlite:///toko.db",
            "membuat RepoBuku",
            "membuat Pencatat",
            "membuat LayananBuku",
            "layanan sama: True",
            "konfigurasi dipakai bersama: True",
            "membuat Pencatat",
            "membuat Pencatat",
            "pencatat sama: False",
            "galat: dependensi melingkar: Ayam -> Telur -> Ayam",
            "galat: Kucing belum didaftarkan",
        ],
        "hints": [
            "Membuat LayananBuku berarti lebih dulu membuat semua yang ia minta, dan itu berlaku juga untuk dependensi dari dependensinya, jadi ambil() paling enak ditulis rekursif.",
            "Bawa daftar kelas yang sedang dibuat sebagai parameter jejak; kalau kelas yang diminta sudah ada di jejak, berarti ada lingkaran dan rantainya tinggal disusun dari jejak itu.",
            "Nama parameter didapat dari inspect.signature(kelas.__init__) (lewati self), tipenya dari typing.get_type_hints(kelas.__init__), lalu buat objeknya dengan kelas(**argumen).",
        ],
        "solution": """import inspect
import typing


class Kontainer:
    def __init__(self):
        self.terdaftar = {}        # kelas -> singleton?
        self.simpanan = {}         # kelas -> objek singleton yang sudah dibuat

    def daftar(self, kelas, singleton=True):
        self.terdaftar[kelas] = singleton

    def ambil(self, kelas, jejak=()):
        if kelas in jejak:
            rantai = " -> ".join(k.__name__ for k in jejak + (kelas,))
            raise LookupError(f"dependensi melingkar: {rantai}")
        if kelas not in self.terdaftar:
            raise LookupError(f"{kelas.__name__} belum didaftarkan")
        if kelas in self.simpanan:
            return self.simpanan[kelas]
        petunjuk = typing.get_type_hints(kelas.__init__)
        argumen = {}
        for nama in inspect.signature(kelas.__init__).parameters:
            if nama == "self":
                continue
            argumen[nama] = self.ambil(petunjuk[nama], jejak + (kelas,))
        objek = kelas(**argumen)
        if self.terdaftar[kelas]:
            self.simpanan[kelas] = objek
        return objek


class Konfigurasi:
    def __init__(self):
        print("membuat Konfigurasi")
        self.url_db = "sqlite:///toko.db"


class Database:
    def __init__(self, konfig: Konfigurasi):
        print("membuat Database untuk", konfig.url_db)
        self.konfig = konfig


class Pencatat:
    def __init__(self):
        print("membuat Pencatat")


class RepoBuku:
    def __init__(self, db: Database):
        print("membuat RepoBuku")
        self.db = db


class LayananBuku:
    def __init__(self, repo: RepoBuku, pencatat: Pencatat, konfig: Konfigurasi):
        print("membuat LayananBuku")
        self.repo = repo
        self.pencatat = pencatat
        self.konfig = konfig


class Ayam:
    def __init__(self, telur: "Telur"):
        self.telur = telur


class Telur:
    def __init__(self, ayam: Ayam):
        self.ayam = ayam


class Kucing:
    pass


k = Kontainer()
k.daftar(Konfigurasi)
k.daftar(Database)
k.daftar(RepoBuku)
k.daftar(LayananBuku)
k.daftar(Pencatat, singleton=False)
k.daftar(Ayam)
k.daftar(Telur)

l1 = k.ambil(LayananBuku)
l2 = k.ambil(LayananBuku)
print("layanan sama:", l1 is l2)
print("konfigurasi dipakai bersama:", l1.konfig is l1.repo.db.konfig)
p1 = k.ambil(Pencatat)
p2 = k.ambil(Pencatat)
print("pencatat sama:", p1 is p2)
for kelas in (Ayam, Kucing):
    try:
        k.ambil(kelas)
    except LookupError as e:
        print("galat:", e)
""",
    },
    {
        "title": "Latihan 7: Decorator Rute ala Flask",
        "difficulty": "Menengah",
        "question": [
            "Buat kelas App yang meniru cara Flask mendaftarkan rute, lalu",
            "panggil aplikasinya sebagai fungsi WSGI.",
            "",
            "  - @app.route(pola, methods=(\"GET\",)) adalah decorator yang",
            "    mendaftarkan fungsi dan mengembalikan fungsi itu apa adanya.",
            "  - Pola boleh memuat <nama> (teks apa pun tanpa garis miring)",
            "    dan <int:nama> (cuma angka, diubah jadi int sebelum dioper).",
            "  - Fungsi mengembalikan teks (status 200) atau tuple (teks,",
            "    kode).",
            "  - App dipanggil sebagai app(environ, start_response). Status",
            "    ditulis \"<kode> <frasa>\" memakai http.HTTPStatus.",
            "  - Path cocok tapi metodenya nggak: 405 dengan body \"Allow: \"",
            "    diikuti metode yang sah, urut abjad. Nggak cocok sama sekali:",
            "    404 dengan body \"halaman nggak ada\".",
            "",
            "Daftarkan rute ini:",
            "  /                              -> \"Beranda\"",
            "  /hello/<name>                  -> \"Halo, <name>!\"",
            "  /buku/<int:id_buku>            -> \"Buku nomor <id> (tipe <tipe>)\"",
            "  /buku, methods=[\"POST\"]        -> (\"Buku dibuat\", 201)",
            "  /toko/<kota>/buku/<int:id_buku> -> \"Buku <id> di <kota>\"",
            "",
            "Input berisi baris METODE PATH. Untuk tiap baris, buat environ",
            "berisi REQUEST_METHOD dan PATH_INFO, panggil app, lalu cetak",
            "\"METODE PATH -> status | body\".",
            "",
            "Keluaran yang diharapkan:",
            "GET / -> 200 OK | Beranda",
            "GET /hello/budi -> 200 OK | Halo, budi!",
            "GET /buku/42 -> 200 OK | Buku nomor 42 (tipe int)",
            "GET /buku/abc -> 404 Not Found | halaman nggak ada",
            "POST /buku -> 201 Created | Buku dibuat",
            "GET /buku -> 405 Method Not Allowed | Allow: POST",
            "DELETE /hello/sari -> 405 Method Not Allowed | Allow: GET",
            "GET /toko/bandung/buku/7 -> 200 OK | Buku 7 di bandung",
        ],
        "hints": [
            "Decorator yang menerima argumen adalah fungsi yang mengembalikan decorator, jadi route(pola, methods) mengembalikan fungsi daftar yang menerima fungsi handler dan mencatatnya.",
            "Saat mendaftar, ubah pola jadi regex dan catat sekalian fungsi pengubah untuk tiap nama parameter, supaya saat dipanggil kamu tinggal menerapkannya ke hasil groupdict().",
            "re.sub(r\"<(?:(\\w+):)?(\\w+)>\", ganti, pola) dengan fungsi ganti bisa menghasilkan (?P<nama>\\d+) untuk int dan (?P<nama>[^/]+) untuk teks; apit hasilnya dengan ^ dan $.",
        ],
        "stdin": """GET /
GET /hello/budi
GET /buku/42
GET /buku/abc
POST /buku
GET /buku
DELETE /hello/sari
GET /toko/bandung/buku/7
""",
        "solution": "import re\nimport sys\nfrom http import HTTPStatus\n\nKONVERTER = {\"int\": (r\"\\d+\", int), \"string\": (r\"[^/]+\", str)}\n\n\nclass App:\n    def __init__(self):\n        self.rute = []                 # (regex, metode, fungsi, konversi)\n\n    def route(self, pola, methods=(\"GET\",)):\n        def daftar(fungsi):\n            konversi = {}\n\n            def ganti(cocok):\n                jenis, nama = cocok.group(1) or \"string\", cocok.group(2)\n                regex, ubah = KONVERTER[jenis]\n                konversi[nama] = ubah\n                return f\"(?P<{nama}>{regex})\"\n\n            regex = re.sub(r\"<(?:(\\w+):)?(\\w+)>\", ganti, pola)\n            self.rute.append((re.compile(f\"^{regex}$\"), set(methods),\n                              fungsi, konversi))\n            return fungsi\n        return daftar\n\n    def __call__(self, environ, start_response):\n        metode, path = environ[\"REQUEST_METHOD\"], environ[\"PATH_INFO\"]\n        izin = set()\n        for regex, metode_rute, fungsi, konversi in self.rute:\n            cocok = regex.match(path)\n            if not cocok:\n                continue\n            if metode not in metode_rute:\n                izin |= metode_rute\n                continue\n            argumen = {k: konversi[k](v) for k, v in cocok.groupdict().items()}\n            hasil = fungsi(**argumen)\n            body, kode = hasil if isinstance(hasil, tuple) else (hasil, 200)\n            return self.balas(start_response, kode, body)\n        if izin:\n            return self.balas(start_response, 405, \"Allow: \" + \", \".join(sorted(izin)))\n        return self.balas(start_response, 404, \"halaman nggak ada\")\n\n    def balas(self, start_response, kode, body):\n        status = f\"{kode} {HTTPStatus(kode).phrase}\"\n        start_response(status, [(\"Content-Type\", \"text/plain; charset=utf-8\")])\n        return [body.encode(\"utf-8\")]\n\n\napp = App()\n\n\n@app.route(\"/\")\ndef beranda():\n    return \"Beranda\"\n\n\n@app.route(\"/hello/<name>\")\ndef halo(name):\n    return f\"Halo, {name}!\"\n\n\n@app.route(\"/buku/<int:id_buku>\")\ndef lihat_buku(id_buku):\n    return f\"Buku nomor {id_buku} (tipe {type(id_buku).__name__})\"\n\n\n@app.route(\"/buku\", methods=[\"POST\"])\ndef tambah_buku():\n    return \"Buku dibuat\", 201\n\n\n@app.route(\"/toko/<kota>/buku/<int:id_buku>\")\ndef buku_di_toko(kota, id_buku):\n    return f\"Buku {id_buku} di {kota}\"\n\n\ndef panggil(metode, path):\n    catatan = {}\n\n    def start_response(status, headers):\n        catatan[\"status\"] = status\n\n    environ = {\"REQUEST_METHOD\": metode, \"PATH_INFO\": path}\n    body = b\"\".join(app(environ, start_response)).decode(\"utf-8\")\n    print(f\"{metode} {path} -> {catatan['status']} | {body}\")\n\n\nfor baris in sys.stdin.read().splitlines():\n    if baris.strip():\n        panggil(*baris.split())\n",
    },
    {
        "title": "Latihan 8: Validasi dari Type Hints ala FastAPI",
        "difficulty": "Menengah",
        "question": [
            "FastAPI membaca type hints untuk memvalidasi body. Tiru caranya",
            "dengan dataclass berikut (pakai persis):",
            "",
            "  @dataclass",
            "  class Pesanan:",
            "      menu: str",
            "      jumlah: int",
            "      harga: float",
            "      pedas: bool = False",
            "      catatan: Optional[str] = None",
            "      tambahan: list[int] = field(default_factory=list)",
            "",
            "Tulis fungsi muat(kelas, data) yang membaca tipe dengan",
            "typing.get_type_hints dan dataclasses.fields, lalu mengubah tiap",
            "nilai seperti mode longgar Pydantic (disederhanakan):",
            "  - str: cuma teks.",
            "  - int: int (bukan bool), atau teks berisi digit saja.",
            "  - float: int atau float (bukan bool), atau teks yang bisa",
            "    diubah float().",
            "  - bool: True/False, atau teks \"true\"/\"false\".",
            "  - Optional[X]: None diterima, selain itu diperiksa sebagai X.",
            "  - list[X]: harus list, tiap elemen diperiksa sebagai X dengan",
            "    indeksnya ditambahkan ke loc.",
            "  - Field tanpa nilai bawaan yang nggak dikirim: \"Field required\".",
            "",
            "Pesan error: \"Input should be a valid string\", \"... integer\",",
            "\"... number\", \"... boolean\", atau \"... list\", dengan loc",
            "seperti [\"body\", \"tambahan\", 1]. Kumpulkan semua error sesuai",
            "urutan field.",
            "",
            "Input berisi satu objek JSON per baris. Kalau sah, cetak \"200\"",
            "dan objeknya. Kalau nggak, cetak \"422\" lalu tiap error di",
            "baris sendiri: tiga spasi dan json.dumps(error).",
            "",
            "Keluaran yang diharapkan:",
            "200 Pesanan(menu='nasi goreng', jumlah=2, harga=15000.0, pedas=False, catatan=None, tambahan=[])",
            "200 Pesanan(menu='mi ayam', jumlah=3, harga=12500.5, pedas=True, catatan=None, tambahan=[1, 2])",
            "422",
            "   {\"loc\": [\"body\", \"jumlah\"], \"msg\": \"Input should be a valid integer\"}",
            "422",
            "   {\"loc\": [\"body\", \"menu\"], \"msg\": \"Field required\"}",
            "   {\"loc\": [\"body\", \"jumlah\"], \"msg\": \"Input should be a valid integer\"}",
            "   {\"loc\": [\"body\", \"harga\"], \"msg\": \"Input should be a valid number\"}",
            "   {\"loc\": [\"body\", \"tambahan\", 1], \"msg\": \"Input should be a valid integer\"}",
            "422",
            "   {\"loc\": [\"body\", \"menu\"], \"msg\": \"Input should be a valid string\"}",
            "   {\"loc\": [\"body\", \"pedas\"], \"msg\": \"Input should be a valid boolean\"}",
            "   {\"loc\": [\"body\", \"tambahan\"], \"msg\": \"Input should be a valid list\"}",
        ],
        "hints": [
            "Tipe seperti Optional[str] dan list[int] adalah tipe bertingkat, jadi fungsi pengubah paling enak ditulis rekursif: kupas lapisan luarnya, lalu panggil dirinya untuk tipe di dalam.",
            "typing.get_origin(tipe) memberi typing.Union untuk Optional dan list untuk list[int], sedangkan typing.get_args(tipe) memberi isinya; field wajib adalah yang default dan default_factory-nya sama-sama dataclasses.MISSING.",
            "Ingat bahwa True juga lolos isinstance(x, int), jadi periksa bool lebih dulu atau tolak bool secara eksplisit saat mengubah ke int dan float.",
        ],
        "stdin": """{"menu": "nasi goreng", "jumlah": 2, "harga": 15000}
{"menu": "mi ayam", "jumlah": "3", "harga": "12500.5", "pedas": "true", "tambahan": [1, "2"]}
{"menu": "soto", "jumlah": 1.5, "harga": 10000, "catatan": null}
{"jumlah": true, "harga": "murah", "tambahan": [1, "dua", 3]}
{"menu": 7, "jumlah": 1, "harga": 5000, "pedas": "iya", "tambahan": "keju"}
""",
        "solution": "import dataclasses\nimport json\nimport sys\nimport typing\nfrom dataclasses import dataclass, field\nfrom typing import Optional\n\n\n@dataclass\nclass Pesanan:\n    menu: str\n    jumlah: int\n    harga: float\n    pedas: bool = False\n    catatan: Optional[str] = None\n    tambahan: list[int] = field(default_factory=list)\n\n\nPESAN = {\n    str: \"Input should be a valid string\",\n    int: \"Input should be a valid integer\",\n    float: \"Input should be a valid number\",\n    bool: \"Input should be a valid boolean\",\n    list: \"Input should be a valid list\",\n}\n\n\ndef ubah(nilai, tipe, loc, galat):\n    \"\"\"Ubah nilai ke tipe; kalau gagal, catat galat dan kembalikan None.\"\"\"\n    asal, argumen = typing.get_origin(tipe), typing.get_args(tipe)\n    if asal is typing.Union:                      # Optional[X] = Union[X, None]\n        if nilai is None:\n            return None\n        tipe = [a for a in argumen if a is not type(None)][0]\n        return ubah(nilai, tipe, loc, galat)\n    if asal is list:\n        if not isinstance(nilai, list):\n            galat.append({\"loc\": loc, \"msg\": PESAN[list]})\n            return None\n        return [ubah(v, argumen[0], loc + [i], galat) for i, v in enumerate(nilai)]\n    if tipe is bool:\n        if isinstance(nilai, bool):\n            return nilai\n        if nilai in (\"true\", \"false\"):\n            return nilai == \"true\"\n    elif tipe is int:\n        if isinstance(nilai, int) and not isinstance(nilai, bool):\n            return nilai\n        if isinstance(nilai, str) and nilai.isdigit():\n            return int(nilai)\n    elif tipe is float:\n        if isinstance(nilai, (int, float)) and not isinstance(nilai, bool):\n            return float(nilai)\n        if isinstance(nilai, str):\n            try:\n                return float(nilai)\n            except ValueError:\n                pass\n    elif tipe is str and isinstance(nilai, str):\n        return nilai\n    galat.append({\"loc\": loc, \"msg\": PESAN[tipe]})\n    return None\n\n\ndef muat(kelas, data):\n    \"\"\"(objek, []) kalau sah, (None, daftar galat) kalau nggak.\"\"\"\n    petunjuk = typing.get_type_hints(kelas)\n    galat, hasil = [], {}\n    for f in dataclasses.fields(kelas):\n        loc = [\"body\", f.name]\n        if f.name not in data:\n            wajib = (f.default is dataclasses.MISSING\n                     and f.default_factory is dataclasses.MISSING)\n            if wajib:\n                galat.append({\"loc\": loc, \"msg\": \"Field required\"})\n            continue\n        hasil[f.name] = ubah(data[f.name], petunjuk[f.name], loc, galat)\n    if galat:\n        return None, galat\n    return kelas(**hasil), []\n\n\nfor baris in sys.stdin.read().splitlines():\n    if not baris.strip():\n        continue\n    objek, galat = muat(Pesanan, json.loads(baris))\n    if objek:\n        print(\"200\", objek)\n    else:\n        print(\"422\")\n        for g in galat:\n            print(\"  \", json.dumps(g))\n",
    },
    {
        "title": "Latihan 9: QuerySet Malas ala Django ORM",
        "difficulty": "Menengah",
        "question": [
            "Tiru QuerySet Django di atas sqlite3. Database :memory: berisi tabel",
            "pelanggan (id, nama, umur, kota) dengan enam baris tetap:",
            "",
            "  1 Ani 17 Bandung      4 Dodi 19 Surabaya",
            "  2 Budi 25 Jakarta     5 Eka 45 Jakarta",
            "  3 Citra 31 Bandung    6 Fajar 15 Jakarta",
            "",
            "Stdin berisi satu operasi per baris: filter KUNCI=NILAI, exclude",
            "KUNCI=NILAI, order_by KOLOM (awali - untuk menurun), dan slice AWAL",
            "AKHIR (seperti qs[awal:akhir]). KUNCI bisa berupa kolom saja (sama",
            "dengan) atau kolom__gt, __gte, __lt, __lte. NILAI yang berupa angka",
            "dijadikan int.",
            "",
            "Aturannya:",
            "",
            "  - Tiap operasi mengembalikan QuerySet baru tanpa menyentuh database.",
            "  - Bangun SQL berparameter (tanda ?): SELECT * FROM pelanggan, lalu",
            "    WHERE dengan syarat digabung AND (exclude jadi NOT (...)), ORDER BY,",
            "    dan LIMIT n OFFSET m.",
            "  - Cetak SQL, params, dan jumlah kueri sebelum iterasi (harus 0).",
            "  - Ulangi QuerySet dua kali; kueri cuma boleh dikirim sekali (simpan",
            "    hasilnya). Cetak tiap baris lalu jumlah kueri.",
            "  - Kolom yang tidak ada: cetak galat: kolom 'X' tidak ada, lalu kueri",
            "    dijalankan: 0, dan berhenti.",
            "",
            "",
            "Contoh pertama, empat baris input:",
            "",
            "  filter umur__gte=18",
            "  exclude kota=Bandung",
            "  order_by -nama",
            "  slice 0 2",
            "",
            "",
            "Untuk input filter umur__gte=18, keluarannya:",
            "",
            "SQL: SELECT * FROM pelanggan WHERE umur >= ? AND NOT (kota = ?) ORDER BY nama DESC LIMIT 2 OFFSET 0",
            "params: [18, 'Bandung']",
            "kueri sebelum iterasi: 0",
            "- Eka (45, Jakarta)",
            "- Dodi (19, Surabaya)",
            "kueri sesudah dua kali iterasi: 1",
            "",
            "",
            "Contoh kedua, dua baris input:",
            "",
            "  filter kota=Jakarta",
            "  order_by umur",
            "",
            "",
            "Untuk input filter kota=Jakarta, keluarannya:",
            "",
            "SQL: SELECT * FROM pelanggan WHERE kota = ? ORDER BY umur",
            "params: ['Jakarta']",
            "kueri sebelum iterasi: 0",
            "- Fajar (15, Jakarta)",
            "- Budi (25, Jakarta)",
            "- Eka (45, Jakarta)",
            "kueri sesudah dua kali iterasi: 1",
            "",
            "",
            "Contoh ketiga, input yang baris keduanya filter gaji__gt=5:",
            "",
            "  exclude kota=Bandung",
            "  filter gaji__gt=5",
            "",
            "",
            "Untuk input exclude kota=Bandung, keluarannya:",
            "",
            "galat: kolom 'gaji' tidak ada",
            "kueri dijalankan: 0",
        ],
        "hints": [
            "Simpan syarat, urutan, dan potongan sebagai atribut, lalu buat SQL hanya di method sql() dan eksekusi hanya di __iter__.",
            "Method filter dan kawan-kawannya membuat objek baru lewat satu fungsi salin, supaya QuerySet lama nggak ikut berubah.",
            "Pisahkan kunci dengan partition(\"__\") dan petakan lookup ke operator lewat dict seperti {\"gte\": \">=\"}.",
            "Pakai atribut cache yang awalnya None, dan isi dengan fetchall() di __iter__ hanya kalau masih None.",
        ],
        "solution": """import sqlite3
import sys

KOLOM = ["id", "nama", "umur", "kota"]
OPERATOR = {"exact": "=", "gt": ">", "gte": ">=", "lt": "<", "lte": "<="}

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE pelanggan (id INTEGER PRIMARY KEY, nama TEXT,"
           " umur INTEGER, kota TEXT)")
db.executemany("INSERT INTO pelanggan VALUES (?, ?, ?, ?)", [
    (1, "Ani", 17, "Bandung"), (2, "Budi", 25, "Jakarta"),
    (3, "Citra", 31, "Bandung"), (4, "Dodi", 19, "Surabaya"),
    (5, "Eka", 45, "Jakarta"), (6, "Fajar", 15, "Jakarta"),
])
jumlah_kueri = 0


class QuerySet:
    def __init__(self, syarat=(), urut=None, potong=None):
        self.syarat = list(syarat)
        self.urut = urut
        self.potong = potong
        self.cache = None

    def _salin(self, **ubah):
        baru = QuerySet(self.syarat, self.urut, self.potong)
        for nama, nilai in ubah.items():
            setattr(baru, nama, nilai)
        return baru

    def _kondisi(self, teks):
        kunci, nilai = teks.split("=", 1)
        kolom, _, lookup = kunci.partition("__")
        if kolom not in KOLOM:
            raise ValueError(f"kolom '{kolom}' tidak ada")
        if (lookup or "exact") not in OPERATOR:
            raise ValueError(f"lookup '{lookup}' tidak dikenal")
        nilai = int(nilai) if nilai.isdigit() else nilai
        return f"{kolom} {OPERATOR[lookup or 'exact']} ?", nilai

    def filter(self, teks):
        return self._salin(syarat=self.syarat + [(False, *self._kondisi(teks))])

    def exclude(self, teks):
        return self._salin(syarat=self.syarat + [(True, *self._kondisi(teks))])

    def order_by(self, kolom):
        if kolom.lstrip("-") not in KOLOM:
            raise ValueError(f"kolom '{kolom.lstrip('-')}' tidak ada")
        arah = " DESC" if kolom.startswith("-") else ""
        return self._salin(urut=kolom.lstrip("-") + arah)

    def __getitem__(self, irisan):
        return self._salin(potong=(irisan.start or 0, irisan.stop))

    def sql(self):
        teks = "SELECT * FROM pelanggan"
        bagian = [f"NOT ({k})" if tidak else k for tidak, k, _ in self.syarat]
        if bagian:
            teks += " WHERE " + " AND ".join(bagian)
        if self.urut:
            teks += " ORDER BY " + self.urut
        if self.potong:
            awal, akhir = self.potong
            teks += f" LIMIT {akhir - awal} OFFSET {awal}"
        return teks, [nilai for _, _, nilai in self.syarat]

    def __iter__(self):
        global jumlah_kueri
        if self.cache is None:
            jumlah_kueri += 1
            self.cache = db.execute(*self.sql()).fetchall()
        return iter(self.cache)


qs = QuerySet()
try:
    for baris in sys.stdin.read().splitlines():
        if not baris.strip():
            continue
        perintah, argumen = baris.split(maxsplit=1)
        if perintah == "slice":
            awal, akhir = map(int, argumen.split())
            qs = qs[awal:akhir]
        else:
            qs = getattr(qs, perintah)(argumen)
except ValueError as e:
    print("galat:", e)
    print("kueri dijalankan:", jumlah_kueri)
    sys.exit()

teks, parameter = qs.sql()
print("SQL:", teks)
print("params:", parameter)
print("kueri sebelum iterasi:", jumlah_kueri)
for _id, nama, umur, kota in qs:
    print(f"- {nama} ({umur}, {kota})")
for _ in qs:
    pass
print("kueri sesudah dua kali iterasi:", jumlah_kueri)""",
        "stdin_list": [
            """filter umur__gte=18
exclude kota=Bandung
order_by -nama
slice 0 2
""",
            """filter kota=Jakarta
order_by umur
""",
            """exclude umur__lt=18
order_by -umur
slice 1 3
""",
            """exclude kota=Bandung
filter gaji__gt=5
""",
        ],
    },
    {
        "title": "Latihan 10: Kueri dari Nama Metode ala Spring Data",
        "difficulty": "Menengah",
        "question": [
            "Spring Data membuat kueri dari nama method repository. Tiru",
            "penerjemahnya di Python. Entity-nya Pengguna dengan properti name,",
            "email, age, active, dan createdAt, disimpan di tabel pengguna. Nama",
            "kolom adalah properti dalam snake_case (createdAt jadi created_at).",
            "",
            "Stdin berisi satu nama method per baris. Aturannya:",
            "",
            "  - Awalan find menghasilkan SELECT *, count menghasilkan SELECT",
            "    COUNT(*), exists menghasilkan SELECT 1 dan diakhiri LIMIT 1. Awalan",
            "    lain ditolak.",
            "  - Sesudah By ada syarat yang dipisah And atau Or. Akhiran",
            "    GreaterThanEqual, LessThanEqual, GreaterThan, LessThan, Between,",
            "    Containing, IsNotNull, IsNull, Not, True, False menjadi >=, <=, >,",
            "    <, BETWEEN ? AND ?, LIKE ?, IS NOT NULL, IS NULL, <> ?, = TRUE, =",
            "    FALSE. Tanpa akhiran berarti = ?.",
            "  - Parameter dinomori urut: ?1, ?2, dan seterusnya.",
            "  - OrderBy diikuti satu atau lebih Properti+Asc/Desc.",
            "  - Properti yang tidak ada ditolak dengan pesan galat.",
            "",
            "Cetak nama method, lalu SQL atau galat menjorok dua spasi.",
            "",
            "",
            "Untuk input findByNameAndAgeGreaterThan, keluarannya:",
            "",
            "findByNameAndAgeGreaterThan",
            "  SELECT * FROM pengguna WHERE name = ?1 AND age > ?2",
            "findByEmailOrderByCreatedAtDesc",
            "  SELECT * FROM pengguna WHERE email = ?1 ORDER BY created_at DESC",
            "countByActiveTrue",
            "  SELECT COUNT(*) FROM pengguna WHERE active = TRUE",
            "",
            "",
            "Untuk input existsByEmail, keluarannya:",
            "",
            "existsByEmail",
            "  SELECT 1 FROM pengguna WHERE email = ?1 LIMIT 1",
            "findByAgeBetweenOrderByAgeAscNameDesc",
            "  SELECT * FROM pengguna WHERE age BETWEEN ?1 AND ?2 ORDER BY age ASC, name DESC",
            "findByNameContainingOrEmailIsNull",
            "  SELECT * FROM pengguna WHERE name LIKE ?1 OR email IS NULL",
            "",
            "",
            "Untuk input findByUsername, keluarannya:",
            "",
            "findByUsername",
            "  galat: properti 'username' tidak ada di Pengguna",
            "ambilByName",
            "  galat: awalan 'ambil' tidak dikenal (pakai find, count, atau exists)",
            "findByAgeGreaterThanEqualAndActiveFalse",
            "  SELECT * FROM pengguna WHERE age >= ?1 AND active = FALSE",
        ],
        "hints": [
            "Pecah nama method jadi tiga bagian: awalan sebelum By, syarat, dan urutan sesudah OrderBy.",
            "Pisahkan syarat dengan re.split dan pola (And|Or) yang diapit huruf kecil di kiri dan huruf besar di kanan, supaya kata penghubungnya ikut tersimpan.",
            "Periksa daftar akhiran satu per satu dengan endswith, dan anggap sisa di depannya sebagai nama properti.",
            "Ubah properti ke snake_case dengan re.sub(r\"([A-Z])\", r\"_\\1\", nama).lower() setelah huruf pertamanya dikecilkan.",
        ],
        "solution": "import re\nimport sys\n\nTABEL = \"pengguna\"\nPROPERTI = [\"name\", \"email\", \"age\", \"active\", \"createdAt\"]\nAKHIRAN = [\n    (\"GreaterThanEqual\", \">= ?\"), (\"LessThanEqual\", \"<= ?\"),\n    (\"GreaterThan\", \"> ?\"), (\"LessThan\", \"< ?\"),\n    (\"Between\", \"BETWEEN ? AND ?\"), (\"Containing\", \"LIKE ?\"),\n    (\"IsNotNull\", \"IS NOT NULL\"), (\"IsNull\", \"IS NULL\"),\n    (\"Not\", \"<> ?\"), (\"True\", \"= TRUE\"), (\"False\", \"= FALSE\"),\n]\nAWALAN = {\"find\": \"SELECT *\", \"count\": \"SELECT COUNT(*)\", \"exists\": \"SELECT 1\"}\n\n\ndef kolom(nama):\n    prop = nama[:1].lower() + nama[1:]\n    if prop not in PROPERTI:\n        raise ValueError(f\"properti '{prop}' tidak ada di Pengguna\")\n    return re.sub(r\"([A-Z])\", r\"_\\1\", prop).lower()\n\n\ndef syarat(potong, nomor):\n    for akhiran, pola in AKHIRAN:\n        if potong.endswith(akhiran) and len(potong) > len(akhiran):\n            nama, operator = potong[:-len(akhiran)], pola\n            break\n    else:\n        nama, operator = potong, \"= ?\"\n    hasil = \"\"\n    for huruf in operator:\n        if huruf == \"?\":\n            hasil += f\"?{nomor}\"\n            nomor += 1\n        else:\n            hasil += huruf\n    return kolom(nama) + \" \" + hasil, nomor\n\n\ndef terjemahkan(metode):\n    cocok = re.fullmatch(r\"([a-z]+)By(\\w+)\", metode)\n    if not cocok or cocok.group(1) not in AWALAN:\n        awal = cocok.group(1) if cocok else metode\n        raise ValueError(f\"awalan '{awal}' tidak dikenal (pakai find, count, \"\n                         \"atau exists)\")\n    awalan, sisa = cocok.groups()\n    kriteria, _, urutan = sisa.partition(\"OrderBy\")\n    bagian = re.split(r\"(?<=[a-z0-9])(And|Or)(?=[A-Z])\", kriteria)\n    where, nomor = [], 1\n    for i, potong in enumerate(bagian):\n        if i % 2:\n            where.append(potong.upper())\n        else:\n            teks, nomor = syarat(potong, nomor)\n            where.append(teks)\n    sql = f\"{AWALAN[awalan]} FROM {TABEL} WHERE \" + \" \".join(where)\n    if urutan:\n        susunan = []\n        for nama, arah in re.findall(r\"([A-Z][a-zA-Z]*?)(Asc|Desc)\", urutan):\n            susunan.append(f\"{kolom(nama)} {arah.upper()}\")\n        sql += \" ORDER BY \" + \", \".join(susunan)\n    if awalan == \"exists\":\n        sql += \" LIMIT 1\"\n    return sql\n\n\nfor baris in sys.stdin.read().split():\n    print(baris)\n    try:\n        print(\"  \" + terjemahkan(baris))\n    except ValueError as e:\n        print(\"  galat:\", e)",
        "stdin_list": [
            """findByNameAndAgeGreaterThan
findByEmailOrderByCreatedAtDesc
countByActiveTrue
""",
            """existsByEmail
findByAgeBetweenOrderByAgeAscNameDesc
findByNameContainingOrEmailIsNull
""",
            """findByUsername
ambilByName
findByAgeGreaterThanEqualAndActiveFalse
""",
        ],
    },
    {
        "title": "Latihan 11: Pelacak Perubahan ala EF Core",
        "difficulty": "Lanjut",
        "question": [
            "Tiru change tracker EF Core di Python. \"Database\" berupa dict tetap",
            "berisi tabel produk:",
            "",
            "  id 1: nama Teh,  harga 5000,  stok 10",
            "  id 2: nama Kopi, harga 18000, stok 5",
            "  id 3: nama Roti, harga 12000, stok 0",
            "",
            "Stdin berisi perintah, satu per baris:",
            "",
            "  - load ID: mulai melacak produk itu dan potret nilai aslinya. ID yang",
            "    tidak ada: cetak galat: produk ID tidak ada.",
            "  - set ID KOLOM NILAI: ubah nilai di memori. NILAI boleh berspasi; yang",
            "    berupa angka dijadikan int. Kunci yang belum dimuat: cetak galat:",
            "    produk ID belum dimuat.",
            "  - add NAMA HARGA STOK: objek baru berkeadaan Added dengan kunci",
            "    sementara baru1, baru2, dan seterusnya. Cetak ditambah sebagai",
            "    KUNCI.",
            "  - remove KUNCI: tandai Deleted. Objek Added yang di-remove cukup",
            "    dilupakan, tanpa SQL apa pun.",
            "  - status: cetak keadaan tiap objek (Unchanged, Modified, Added,",
            "    Deleted), id lama terurut dulu lalu kunci baru. Objek yang nilainya",
            "    diubah lalu dikembalikan ke nilai asli kembali Unchanged.",
            "  - save: kirim INSERT dulu (id baru = id terbesar + 1), lalu UPDATE",
            "    yang cuma memuat kolom berubah (urutan nama, harga, stok), lalu",
            "    DELETE. Akhiri dengan disimpan: N perintah, atau cetak tidak ada",
            "    perubahan. Sesudah disimpan, semua objek jadi Unchanged dengan",
            "    potret baru.",
            "",
            "",
            "Untuk input load 1, keluarannya:",
            "",
            "ditambah sebagai baru1",
            "status: 1 Modified, 2 Unchanged, baru1 Added",
            "INSERT INTO produk (nama, harga, stok) VALUES ('Susu', 9000, 3)  -- baru1 jadi id 4",
            "UPDATE produk SET harga = 5500, stok = 12 WHERE id = 1",
            "disimpan: 2 perintah",
            "status: 1 Unchanged, 2 Unchanged, 4 Unchanged",
            "tidak ada perubahan",
            "",
            "",
            "Untuk input load 3, keluarannya:",
            "",
            "ditambah sebagai baru1",
            "galat: produk 2 belum dimuat",
            "status: 3 Deleted",
            "DELETE FROM produk WHERE id = 3",
            "disimpan: 1 perintah",
            "",
            "",
            "Untuk input load 9, keluarannya:",
            "",
            "galat: produk 9 tidak ada",
            "status: 2 Modified",
            "status: 2 Unchanged",
            "tidak ada perubahan",
        ],
        "hints": [
            "Simpan dua salinan nilai untuk tiap objek yang dilacak: nilai yang sedang dipakai dan potret aslinya saat dimuat.",
            "Keadaan Modified nggak perlu disimpan, cukup dihitung dengan membandingkan nilai sekarang dengan potretnya.",
            "Hanya Added dan Deleted yang perlu dicatat sebagai penanda, karena keduanya nggak bisa disimpulkan dari perbandingan nilai.",
            "Di save, lakukan tiga putaran terpisah untuk INSERT, UPDATE, dan DELETE, lalu perbarui dict database dan potretnya di tiap putaran.",
        ],
        "solution": "import sys\n\nKOLOM = [\"nama\", \"harga\", \"stok\"]\nDB = {\n    1: {\"nama\": \"Teh\", \"harga\": 5000, \"stok\": 10},\n    2: {\"nama\": \"Kopi\", \"harga\": 18000, \"stok\": 5},\n    3: {\"nama\": \"Roti\", \"harga\": 12000, \"stok\": 0},\n}\n\n\ndef sql_nilai(v):\n    return str(v) if isinstance(v, int) else f\"'{v}'\"\n\n\nclass Entri:\n    def __init__(self, kunci, nilai, keadaan):\n        self.kunci = kunci\n        self.nilai = dict(nilai)\n        self.asli = dict(nilai)\n        self.dasar = keadaan\n\n    def keadaan(self):\n        if self.dasar in (\"Added\", \"Deleted\"):\n            return self.dasar\n        return \"Modified\" if self.nilai != self.asli else \"Unchanged\"\n\n\nclass DbContext:\n    def __init__(self):\n        self.lacak = {}\n        self.nomor_baru = 0\n\n    def load(self, kunci):\n        kunci = int(kunci)\n        if kunci not in DB:\n            return f\"galat: produk {kunci} tidak ada\"\n        self.lacak.setdefault(kunci, Entri(kunci, DB[kunci], \"Unchanged\"))\n        return None\n\n    def ambil(self, kunci):\n        kunci = int(kunci) if kunci.isdigit() else kunci\n        if kunci not in self.lacak:\n            raise KeyError(f\"galat: produk {kunci} belum dimuat\")\n        return self.lacak[kunci]\n\n    def set(self, kunci, kolom, nilai):\n        e = self.ambil(kunci)\n        e.nilai[kolom] = int(nilai) if nilai.isdigit() else nilai\n\n    def add(self, nama, harga, stok):\n        self.nomor_baru += 1\n        kunci = f\"baru{self.nomor_baru}\"\n        nilai = {\"nama\": nama, \"harga\": int(harga), \"stok\": int(stok)}\n        self.lacak[kunci] = Entri(kunci, nilai, \"Added\")\n        return kunci\n\n    def remove(self, kunci):\n        e = self.ambil(kunci)\n        if e.dasar == \"Added\":\n            del self.lacak[e.kunci]      # belum pernah disimpan: cukup lupakan\n        else:\n            e.dasar = \"Deleted\"\n\n    def urut(self):\n        lama = sorted(k for k in self.lacak if isinstance(k, int))\n        baru = [k for k in self.lacak if not isinstance(k, int)]\n        return [self.lacak[k] for k in lama + baru]\n\n    def status(self):\n        isi = [f\"{e.kunci} {e.keadaan()}\" for e in self.urut()]\n        return \"status: \" + (\", \".join(isi) if isi else \"kosong\")\n\n    def save_changes(self):\n        perintah = []\n        for e in self.urut():\n            if e.keadaan() == \"Added\":\n                kunci = max(DB) + 1\n                DB[kunci] = dict(e.nilai)\n                nilai = \", \".join(sql_nilai(e.nilai[k]) for k in KOLOM)\n                perintah.append(f\"INSERT INTO produk (nama, harga, stok) \"\n                                f\"VALUES ({nilai})  -- {e.kunci} jadi id {kunci}\")\n                del self.lacak[e.kunci]\n                self.lacak[kunci] = Entri(kunci, e.nilai, \"Unchanged\")\n        for e in self.urut():\n            if e.keadaan() == \"Modified\":\n                ubah = [k for k in KOLOM if e.nilai[k] != e.asli[k]]\n                isi = \", \".join(f\"{k} = {sql_nilai(e.nilai[k])}\" for k in ubah)\n                perintah.append(f\"UPDATE produk SET {isi} WHERE id = {e.kunci}\")\n                DB[e.kunci] = dict(e.nilai)\n                e.asli = dict(e.nilai)\n        for e in self.urut():\n            if e.keadaan() == \"Deleted\":\n                perintah.append(f\"DELETE FROM produk WHERE id = {e.kunci}\")\n                del DB[e.kunci]\n                del self.lacak[e.kunci]\n        if not perintah:\n            return [\"tidak ada perubahan\"]\n        return perintah + [f\"disimpan: {len(perintah)} perintah\"]\n\n\ndb = DbContext()\nfor baris in sys.stdin.read().splitlines():\n    bagian = baris.split(maxsplit=3)\n    if not bagian:\n        continue\n    try:\n        if bagian[0] == \"load\":\n            pesan = db.load(bagian[1])\n            if pesan:\n                print(pesan)\n        elif bagian[0] == \"set\":\n            db.set(*bagian[1:4])\n        elif bagian[0] == \"add\":\n            print(\"ditambah sebagai\", db.add(*bagian[1:4]))\n        elif bagian[0] == \"remove\":\n            db.remove(bagian[1])\n        elif bagian[0] == \"status\":\n            print(db.status())\n        elif bagian[0] == \"save\":\n            print(\"\\n\".join(db.save_changes()))\n    except KeyError as e:\n        print(e.args[0])",
        "stdin_list": [
            """load 1
load 2
set 1 harga 5500
set 1 stok 12
set 2 harga 18000
add Susu 9000 3
status
save
status
save
""",
            """load 3
remove 3
add Gula 15000 7
remove baru1
set 2 stok 1
status
save
""",
            """load 9
load 2
set 2 nama Kopi Susu
status
set 2 nama Kopi
status
save
""",
        ],
    },
    {
        "title": "Latihan 12: Active Record Mini dengan sqlite3",
        "difficulty": "Lanjut",
        "question": [
            "Buat kelas dasar Model bergaya Eloquent di atas sqlite3 (:memory:).",
            "Turunannya Kategori (tabel kategori, kolom nama) dan Produk (tabel",
            "produk, kolom nama, harga, kategori_id). Setiap SQL yang dijalankan",
            "dicetak dengan format SQL: <perintah> <daftar parameter>.",
            "",
            "Stdin berisi perintah, satu per baris. Cetak dulu > lalu perintahnya,",
            "kemudian hasilnya menjorok dua spasi:",
            "",
            "  - create MODEL k=v ...: INSERT semua kolom, lalu cetak objeknya",
            "    seperti Produk(id=1, nama=Teh, harga=5000, kategori_id=1).",
            "  - find MODEL ID: SELECT berdasarkan id, cetak objek atau tidak",
            "    ditemukan.",
            "  - update MODEL ID k=v ...: find, ubah, lalu save(). UPDATE cuma memuat",
            "    kolom yang nilainya berbeda; kalau tidak ada yang berbeda, cetak",
            "    tidak ada perubahan, tidak ada SQL.",
            "  - delete MODEL ID: find lalu DELETE.",
            "  - where MODEL KOLOM OP NILAI: SELECT dengan ORDER BY id, cetak tiap",
            "    objek lalu (N baris). Kolom yang tidak ada: cetak galat: kolom 'X'",
            "    tidak ada di TABEL, tanpa SQL.",
            "  - relasi kategori ID produk: has_many, ambil produk milik kategori",
            "    itu.",
            "",
            "Nilai yang berupa angka dijadikan int.",
            "",
            "",
            "Untuk input create kategori nama=Minuman, keluarannya:",
            "",
            "> create kategori nama=Minuman",
            "  SQL: INSERT INTO kategori (nama) VALUES (?) ['Minuman']",
            "  Kategori(id=1, nama=Minuman)",
            "> create produk nama=Teh harga=5000 kategori_id=1",
            "  SQL: INSERT INTO produk (nama, harga, kategori_id) VALUES (?, ?, ?) ['Teh', 5000, 1]",
            "  Produk(id=1, nama=Teh, harga=5000, kategori_id=1)",
            "> create produk nama=Kopi harga=18000 kategori_id=1",
            "  SQL: INSERT INTO produk (nama, harga, kategori_id) VALUES (?, ?, ?) ['Kopi', 18000, 1]",
            "  Produk(id=2, nama=Kopi, harga=18000, kategori_id=1)",
            "> find produk 1",
            "  SQL: SELECT * FROM produk WHERE id = ? [1]",
            "  Produk(id=1, nama=Teh, harga=5000, kategori_id=1)",
            "> update produk 1 harga=5500",
            "  SQL: SELECT * FROM produk WHERE id = ? [1]",
            "  SQL: UPDATE produk SET harga = ? WHERE id = ? [5500, 1]",
            "> update produk 2 harga=18000",
            "  SQL: SELECT * FROM produk WHERE id = ? [2]",
            "  tidak ada perubahan, tidak ada SQL",
            "> relasi kategori 1 produk",
            "  SQL: SELECT * FROM kategori WHERE id = ? [1]",
            "  SQL: SELECT * FROM produk WHERE kategori_id = ? ORDER BY id [1]",
            "  Produk(id=1, nama=Teh, harga=5500, kategori_id=1)",
            "  Produk(id=2, nama=Kopi, harga=18000, kategori_id=1)",
            "",
            "",
            "Untuk input create produk nama=Roti harga=12000 kategori_id=1, keluarannya:",
            "",
            "> create produk nama=Roti harga=12000 kategori_id=1",
            "  SQL: INSERT INTO produk (nama, harga, kategori_id) VALUES (?, ?, ?) ['Roti', 12000, 1]",
            "  Produk(id=1, nama=Roti, harga=12000, kategori_id=1)",
            "> create produk nama=Susu harga=9000 kategori_id=2",
            "  SQL: INSERT INTO produk (nama, harga, kategori_id) VALUES (?, ?, ?) ['Susu', 9000, 2]",
            "  Produk(id=2, nama=Susu, harga=9000, kategori_id=2)",
            "> where produk harga < 10000",
            "  SQL: SELECT * FROM produk WHERE harga < ? ORDER BY id [10000]",
            "  Produk(id=2, nama=Susu, harga=9000, kategori_id=2)",
            "  (1 baris)",
            "> delete produk 1",
            "  SQL: SELECT * FROM produk WHERE id = ? [1]",
            "  SQL: DELETE FROM produk WHERE id = ? [1]",
            "> find produk 1",
            "  SQL: SELECT * FROM produk WHERE id = ? [1]",
            "  tidak ditemukan",
            "> where produk berat > 1",
            "  galat: kolom 'berat' tidak ada di produk",
        ],
        "hints": [
            "Simpan nama tabel dan daftar kolom sebagai atribut kelas, lalu tulis create, find, dan where sebagai classmethod di Model.",
            "Simpan salinan data asli saat objek dibuat atau dimuat, supaya save() bisa membandingkan dan memilih kolom yang berubah.",
            "Satukan semua eksekusi SQL di satu fungsi yang mencetak perintah dan parameternya sebelum memanggil db.execute.",
            "Periksa nama kolom terhadap daftar kolom sebelum menyusun SQL, karena nama kolom nggak bisa dikirim sebagai parameter ?.",
        ],
        "solution": "import sqlite3\nimport sys\n\ndb = sqlite3.connect(\":memory:\")\ndb.executescript(\"\"\"\nCREATE TABLE kategori (id INTEGER PRIMARY KEY, nama TEXT);\nCREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, harga INTEGER,\n                     kategori_id INTEGER);\n\"\"\")\nOPERATOR = {\"=\", \"!=\", \">\", \"<\", \">=\", \"<=\"}\n\n\ndef jalankan(sql, nilai=()):\n    print(f\"  SQL: {sql} {list(nilai)}\")\n    return db.execute(sql, nilai)\n\n\nclass Model:\n    tabel = \"\"\n    kolom = []\n\n    def __init__(self, **data):\n        self.id = data.pop(\"id\", None)\n        self.data = dict(data)\n        self.asli = dict(data)\n\n    def __repr__(self):\n        isi = \", \".join(f\"{k}={self.data[k]}\" for k in self.kolom)\n        return f\"{type(self).__name__}(id={self.id}, {isi})\"\n\n    @classmethod\n    def periksa(cls, nama):\n        if nama not in cls.kolom and nama != \"id\":\n            raise ValueError(f\"kolom '{nama}' tidak ada di {cls.tabel}\")\n\n    @classmethod\n    def dari_baris(cls, baris):\n        return cls(**dict(zip([\"id\"] + cls.kolom, baris)))\n\n    @classmethod\n    def create(cls, **data):\n        for nama in data:\n            cls.periksa(nama)\n        obj = cls(**{k: data.get(k) for k in cls.kolom})\n        obj.save()\n        return obj\n\n    @classmethod\n    def find(cls, kunci):\n        baris = jalankan(f\"SELECT * FROM {cls.tabel} WHERE id = ?\",\n                         [kunci]).fetchone()\n        return cls.dari_baris(baris) if baris else None\n\n    @classmethod\n    def where(cls, nama, op, nilai):\n        cls.periksa(nama)\n        if op not in OPERATOR:\n            raise ValueError(f\"operator '{op}' tidak dikenal\")\n        sql = f\"SELECT * FROM {cls.tabel} WHERE {nama} {op} ? ORDER BY id\"\n        return [cls.dari_baris(b) for b in jalankan(sql, [nilai]).fetchall()]\n\n    def save(self):\n        if self.id is None:\n            daftar = \", \".join(self.kolom)\n            tanda = \", \".join(\"?\" for _ in self.kolom)\n            sql = f\"INSERT INTO {self.tabel} ({daftar}) VALUES ({tanda})\"\n            self.id = jalankan(sql, [self.data[k] for k in self.kolom]).lastrowid\n        else:\n            berubah = [k for k in self.kolom if self.data[k] != self.asli[k]]\n            if not berubah:\n                print(\"  tidak ada perubahan, tidak ada SQL\")\n                return\n            isi = \", \".join(f\"{k} = ?\" for k in berubah)\n            jalankan(f\"UPDATE {self.tabel} SET {isi} WHERE id = ?\",\n                     [self.data[k] for k in berubah] + [self.id])\n        self.asli = dict(self.data)\n\n    def delete(self):\n        jalankan(f\"DELETE FROM {self.tabel} WHERE id = ?\", [self.id])\n\n    def has_many(self, kelas, kunci_asing):\n        sql = f\"SELECT * FROM {kelas.tabel} WHERE {kunci_asing} = ? ORDER BY id\"\n        return [kelas.dari_baris(b) for b in jalankan(sql, [self.id]).fetchall()]\n\n\nclass Kategori(Model):\n    tabel = \"kategori\"\n    kolom = [\"nama\"]\n\n    def produk(self):\n        return self.has_many(Produk, \"kategori_id\")\n\n\nclass Produk(Model):\n    tabel = \"produk\"\n    kolom = [\"nama\", \"harga\", \"kategori_id\"]\n\n\nMODEL = {\"kategori\": Kategori, \"produk\": Produk}\n\n\ndef nilai(teks):\n    return int(teks) if teks.isdigit() else teks\n\n\ndef pasangan(daftar):\n    return {k: nilai(v) for k, v in (x.split(\"=\", 1) for x in daftar)}\n\n\nfor baris in sys.stdin.read().splitlines():\n    if not baris.strip():\n        continue\n    print(\">\", baris)\n    kata = baris.split()\n    perintah, kelas = kata[0], MODEL[kata[1]]\n    try:\n        if perintah == \"create\":\n            print(\"  \" + repr(kelas.create(**pasangan(kata[2:]))))\n        elif perintah == \"find\":\n            obj = kelas.find(int(kata[2]))\n            print(\"  \" + (repr(obj) if obj else \"tidak ditemukan\"))\n        elif perintah == \"update\":\n            obj = kelas.find(int(kata[2]))\n            ubah = pasangan(kata[3:])\n            for k in ubah:\n                kelas.periksa(k)\n            obj.data.update(ubah)\n            obj.save()\n        elif perintah == \"delete\":\n            kelas.find(int(kata[2])).delete()\n        elif perintah == \"where\":\n            hasil = kelas.where(kata[2], kata[3], nilai(kata[4]))\n            for obj in hasil:\n                print(\"  \" + repr(obj))\n            print(f\"  ({len(hasil)} baris)\")\n        elif perintah == \"relasi\":\n            for obj in getattr(kelas.find(int(kata[2])), kata[3])():\n                print(\"  \" + repr(obj))\n    except ValueError as e:\n        print(\"  galat:\", e)",
        "stdin_list": [
            """create kategori nama=Minuman
create produk nama=Teh harga=5000 kategori_id=1
create produk nama=Kopi harga=18000 kategori_id=1
find produk 1
update produk 1 harga=5500
update produk 2 harga=18000
relasi kategori 1 produk
""",
            """create produk nama=Roti harga=12000 kategori_id=1
create produk nama=Susu harga=9000 kategori_id=2
where produk harga < 10000
delete produk 1
find produk 1
where produk berat > 1
""",
        ],
    },
    {
        "title": "Latihan 13: Rute RESTful dari resources ala Rails",
        "difficulty": "Lanjut",
        "question": [
            "Tiru bin/rails routes di Python. Stdin berisi baris-baris",
            "config/routes.rb dengan bentuk:",
            "",
            "  resources :NAMA",
            "  resources :NAMA, only: [:aksi, :aksi]",
            "  resources :NAMA, except: [:aksi]",
            "  resources :NAMA do        (lalu resource anak, ditutup end)",
            "",
            "Aturannya:",
            "",
            "  - Tujuh aksi dicetak dengan urutan index (GET /nama), create (POST",
            "    /nama), new (GET /nama/new), edit (GET /nama/:id/edit), show (GET",
            "    /nama/:id), update dua kali (PATCH lalu PUT /nama/:id), dan destroy",
            "    (DELETE /nama/:id).",
            "  - only memilih aksi, except membuangnya. Aksi di luar tujuh itu: cetak",
            "    galat: aksi 'X' tidak dikenal, lalu berhenti.",
            "  - Resource anak di dalam blok do mendapat awalan",
            "    /induk/:induk_tunggal_id. Bentuk tunggal: buang s di akhir, atau",
            "    ganti ies jadi y. Rute anak dicetak sesudah rute induknya (urutan di",
            "    Rails asli bisa sedikit berbeda).",
            "  - Cetak kepala kolom Verb, URI Pattern, Controller#Action. Lebar kolom",
            "    pertama dan kedua = isi terpanjang di kolom itu (termasuk judulnya),",
            "    dipisah dua spasi. Akhiri dengan (N rute).",
            "",
            "",
            "Untuk input resources :articles, keluarannya:",
            "",
            "Verb    URI Pattern         Controller#Action",
            "GET     /articles           articles#index",
            "POST    /articles           articles#create",
            "GET     /articles/new       articles#new",
            "GET     /articles/:id/edit  articles#edit",
            "GET     /articles/:id       articles#show",
            "PATCH   /articles/:id       articles#update",
            "PUT     /articles/:id       articles#update",
            "DELETE  /articles/:id       articles#destroy",
            "(8 rute)",
            "",
            "",
            "Contoh kedua, lima baris input:",
            "",
            "  resources :users do",
            "    resources :comments, only: [:index, :create]",
            "  end",
            "  resources :categories, only: [:index, :show]",
            "  resources :articles, except: [:new, :edit]",
            "",
            "",
            "Untuk input resources :users do, keluarannya:",
            "",
            "Verb    URI Pattern               Controller#Action",
            "GET     /users                    users#index",
            "POST    /users                    users#create",
            "GET     /users/new                users#new",
            "GET     /users/:id/edit           users#edit",
            "GET     /users/:id                users#show",
            "PATCH   /users/:id                users#update",
            "PUT     /users/:id                users#update",
            "DELETE  /users/:id                users#destroy",
            "GET     /users/:user_id/comments  comments#index",
            "POST    /users/:user_id/comments  comments#create",
            "GET     /categories               categories#index",
            "GET     /categories/:id           categories#show",
            "GET     /articles                 articles#index",
            "POST    /articles                 articles#create",
            "GET     /articles/:id             articles#show",
            "PATCH   /articles/:id             articles#update",
            "PUT     /articles/:id             articles#update",
            "DELETE  /articles/:id             articles#destroy",
            "(18 rute)",
            "",
            "",
            "Contoh ketiga:",
            "",
            "  resources :photos",
            "  resources :albums, only: [:index, :publish]",
            "",
            "",
            "Untuk input resources :photos, keluarannya:",
            "",
            "galat: aksi 'publish' tidak dikenal",
        ],
        "hints": [
            "Simpan tujuh aksi sebagai daftar tuple (aksi, verb, akhiran path) dengan urutan yang diminta, lalu saring dengan himpunan aksi yang dipilih.",
            "Pakai satu regex untuk mengurai baris resources, termasuk bagian only atau except dan kata do di akhir.",
            "Simpan nama induk saat bertemu do dan kosongkan lagi saat bertemu end, supaya resource di antaranya mendapat awalan.",
            "Hitung lebar kolom dengan max() atas panjang isi dan judul, lalu cetak dengan f-string seperti f\"{verb:<{lebar}}\".",
        ],
        "solution": "import re\nimport sys\n\nURUTAN = [\n    (\"index\", \"GET\", \"\"), (\"create\", \"POST\", \"\"), (\"new\", \"GET\", \"/new\"),\n    (\"edit\", \"GET\", \"/:id/edit\"), (\"show\", \"GET\", \"/:id\"),\n    (\"update\", \"PATCH\", \"/:id\"), (\"update\", \"PUT\", \"/:id\"),\n    (\"destroy\", \"DELETE\", \"/:id\"),\n]\nAKSI = {\"index\", \"create\", \"new\", \"edit\", \"show\", \"update\", \"destroy\"}\nPOLA = re.compile(r\"resources :(\\w+)(?:, (only|except): \\[([^\\]]*)\\])?( do)?$\")\n\n\ndef tunggal(nama):\n    if nama.endswith(\"ies\"):\n        return nama[:-3] + \"y\"\n    return nama[:-1] if nama.endswith(\"s\") else nama\n\n\ndef rute(nama, pilihan, daftar, induk):\n    aksi = set(AKSI)\n    if pilihan:\n        dipilih = {a.strip().lstrip(\":\") for a in daftar.split(\",\") if a.strip()}\n        asing = sorted(dipilih - AKSI)\n        if asing:\n            raise ValueError(f\"aksi '{asing[0]}' tidak dikenal\")\n        aksi = dipilih if pilihan == \"only\" else AKSI - dipilih\n    awal = f\"/{induk}/:{tunggal(induk)}_id\" if induk else \"\"\n    return [(verb, f\"{awal}/{nama}{akhir}\", f\"{nama}#{a}\")\n            for a, verb, akhir in URUTAN if a in aksi]\n\n\nhasil, induk = [], None\nfor baris in sys.stdin.read().splitlines():\n    teks = baris.strip()\n    if not teks:\n        continue\n    if teks == \"end\":\n        induk = None\n        continue\n    cocok = POLA.match(teks)\n    try:\n        if not cocok:\n            raise ValueError(f\"baris tidak dikenal: {teks}\")\n        nama, pilihan, daftar, blok_do = cocok.groups()\n        hasil += rute(nama, pilihan, daftar, induk)\n        if blok_do:\n            induk = nama\n    except ValueError as e:\n        print(\"galat:\", e)\n        sys.exit()\n\nlebar_verb = max(len(\"Verb\"), *(len(v) for v, _, _ in hasil))\nlebar_jalur = max(len(\"URI Pattern\"), *(len(p) for _, p, _ in hasil))\nprint(f\"{'Verb':<{lebar_verb}}  {'URI Pattern':<{lebar_jalur}}  Controller#Action\")\nfor verb, jalur, aksi in hasil:\n    print(f\"{verb:<{lebar_verb}}  {jalur:<{lebar_jalur}}  {aksi}\")\nprint(f\"({len(hasil)} rute)\")",
        "stdin_list": [
            """resources :articles
""",
            """resources :users do
  resources :comments, only: [:index, :create]
end
resources :categories, only: [:index, :show]
resources :articles, except: [:new, :edit]
""",
            """resources :photos
resources :albums, only: [:index, :publish]
""",
        ],
    },
    {
        "title": "Latihan 14: Mux Bergaya Go 1.22 dengan Prioritas Pola",
        "difficulty": "Lanjut",
        "question": [
            "Tiru pemilihan pola ServeMux Go 1.22 di Python. Stdin berisi baris pola",
            "METODE /path atau pola /path (tanpa metode berarti semua metode), dan",
            "baris minta METODE /path.",
            "",
            "Segmen pola: teks biasa, {nama} (tepat satu segmen yang tidak kosong),",
            "{nama...} di akhir (sisa path, boleh kosong sesudah garis miring), garis",
            "miring di akhir pola (sama dengan sisa tanpa nama), dan {$} di akhir",
            "(cuma path yang berakhir tepat di garis miring itu).",
            "",
            "Pola P lebih spesifik daripada Q kalau semua permintaan yang cocok",
            "dengan P juga cocok dengan Q, tapi tidak sebaliknya. Metodenya ikut",
            "dihitung: pola tanpa metode mencakup semua metode. Versi mini ini tidak",
            "membahas HEAD dan host.",
            "",
            "  - pola: kalau pola baru tumpang tindih dengan pola lama (ada",
            "    permintaan yang cocok dengan keduanya) dan tidak ada yang lebih",
            "    spesifik, cetak konflik: BARU dengan LAMA dan jangan daftarkan (Go",
            "    asli panic di sini).",
            "  - minta: pilih pola paling spesifik yang cocok dengan path dan metode,",
            "    cetak METODE /path -> POLA beserta nilai wildcard bernama",
            "    (nama=nilai). Path cocok tapi metodenya tidak: cetak 405 Allow:",
            "    dengan metode yang terdaftar, urut abjad. Tidak ada yang cocok: 404.",
            "",
            "",
            "Untuk input pola GET /items/{id}, keluarannya:",
            "",
            "GET /items/7 -> GET /items/{id} id=7",
            "GET /items/latest -> GET /items/latest",
            "GET /items/7/foto -> /items/",
            "DELETE /items/7 -> /items/",
            "PUT /items -> 405 Allow: POST",
            "GET / -> GET /{$}",
            "GET /lain -> 404",
            "",
            "",
            "Untuk input pola GET /files/{path...}, keluarannya:",
            "",
            "konflik: /files/{nama} dengan GET /files/{path...}",
            "konflik: GET /files/{path...} dengan GET /files/{path...}",
            "konflik: GET /{a}/x dengan GET /files/{path...}",
            "GET /files/readme -> GET /files/readme",
            "GET /files/a/b -> GET /files/{path...} path=a/b",
            "GET /files/ -> GET /files/{path...} path=",
            "POST /files/a -> 405 Allow: GET",
            "",
            "",
            "Untuk input pola GET /users/{id}, keluarannya:",
            "",
            "GET /users/5/posts/9 -> GET /users/{id}/posts/{pid} id=5 pid=9",
            "GET /users/ -> 404",
            "GET /users/5 -> GET /users/{id} id=5",
        ],
        "hints": [
            "Ubah tiap pola jadi metode dan daftar segmen bertipe, misalnya (\"lit\", \"items\"), (\"liar\", \"id\"), (\"sisa\", \"path\"), dan (\"akhir\", None).",
            "Tulis fungsi subset(a, b) yang menelusuri dua daftar segmen secara rekursif, karena aturan lebih spesifik tinggal memanggilnya dua arah.",
            "Tulis juga fungsi tumpang(a, b) yang menjawab apakah ada path yang cocok dengan keduanya, lalu konflik terjadi kalau tumpang benar tapi tidak ada yang lebih spesifik.",
            "Pecah path permintaan dengan path.split(\"/\")[1:], sehingga /items/ menjadi [\"items\", \"\"] dan segmen kosong itu bisa dicocokkan dengan sisa atau {$}.",
        ],
        "solution": "import sys\n\n\ndef urai(teks):\n    \"\"\"'GET /items/{id}' -> (metode atau None, daftar segmen).\"\"\"\n    metode, _, jalur = teks.rpartition(\" \")\n    potong = jalur.split(\"/\")[1:]\n    segmen = []\n    for i, s in enumerate(potong):\n        akhir = i == len(potong) - 1\n        if s == \"{$}\":\n            segmen.append((\"akhir\", None))\n        elif s.startswith(\"{\") and s.endswith(\"...}\"):\n            segmen.append((\"sisa\", s[1:-4]))\n        elif s.startswith(\"{\") and s.endswith(\"}\"):\n            segmen.append((\"liar\", s[1:-1]))\n        elif s == \"\" and akhir and i > 0:\n            segmen.append((\"sisa\", None))      # garis miring di ujung\n        elif s == \"\" and akhir:\n            segmen.append((\"sisa\", None))      # pola \"/\" saja\n        else:\n            segmen.append((\"lit\", s))\n    return (metode or None), segmen\n\n\ndef subset(a, b):\n    \"\"\"Apakah setiap jalur yang cocok dengan a juga cocok dengan b?\"\"\"\n    if not a or not b:\n        return not a and not b\n    (ja, na), (jb, nb) = a[0], b[0]\n    if jb == \"sisa\":\n        return True\n    if ja == \"sisa\":\n        return False\n    if ja == \"akhir\" or jb == \"akhir\":\n        return ja == jb\n    if jb == \"liar\" or (ja == \"lit\" and na == nb):\n        return subset(a[1:], b[1:])\n    return False\n\n\ndef tumpang(a, b):\n    \"\"\"Apakah ada jalur yang cocok dengan a dan b sekaligus?\"\"\"\n    if not a or not b:\n        return not a and not b\n    (ja, na), (jb, nb) = a[0], b[0]\n    if ja == \"sisa\" or jb == \"sisa\":\n        return True\n    if ja == \"akhir\" or jb == \"akhir\":\n        return ja == jb\n    if ja == \"lit\" and jb == \"lit\" and na != nb:\n        return False\n    return tumpang(a[1:], b[1:])\n\n\ndef lebih_spesifik(p, q):\n    (mp, sp), (mq, sq) = p, q\n    p_dalam_q = subset(sp, sq) and (mq is None or mp == mq)\n    q_dalam_p = subset(sq, sp) and (mp is None or mp == mq)\n    return p_dalam_q and not q_dalam_p\n\n\ndef cocok(segmen, potong):\n    \"\"\"Nilai wildcard (dict) kalau jalur cocok, None kalau tidak.\"\"\"\n    nilai = {}\n    for i, (jenis, nama) in enumerate(segmen):\n        if jenis == \"sisa\":\n            if i >= len(potong):\n                return None\n            if nama:\n                nilai[nama] = \"/\".join(potong[i:])\n            return nilai\n        if i >= len(potong):\n            return None\n        if jenis == \"akhir\":\n            return nilai if potong[i:] == [\"\"] else None\n        if jenis == \"liar\":\n            if potong[i] == \"\":\n                return None\n            nilai[nama] = potong[i]\n        elif potong[i] != nama:\n            return None\n    return nilai if len(potong) == len(segmen) else None\n\n\nterdaftar = []\nfor baris in sys.stdin.read().splitlines():\n    perintah, _, isi = baris.partition(\" \")\n    if perintah == \"pola\":\n        baru = urai(isi)\n        bentrok = None\n        for teks, lama in terdaftar:\n            metode_lap = baru[0] is None or lama[0] is None or baru[0] == lama[0]\n            if (metode_lap and tumpang(baru[1], lama[1])\n                    and not lebih_spesifik(baru, lama)\n                    and not lebih_spesifik(lama, baru)):\n                bentrok = teks\n                break\n        if bentrok:\n            print(f\"konflik: {isi} dengan {bentrok}\")\n        else:\n            terdaftar.append((isi, baru))\n    elif perintah == \"minta\":\n        metode, jalur = isi.split(\" \", 1)\n        potong = jalur.split(\"/\")[1:]\n        calon, metode_lain = [], set()\n        for teks, (m, segmen) in terdaftar:\n            nilai = cocok(segmen, potong)\n            if nilai is None:\n                continue\n            if m is None or m == metode:\n                calon.append((teks, (m, segmen), nilai))\n            else:\n                metode_lain.add(m)\n        if not calon:\n            if metode_lain:\n                print(f\"{isi} -> 405 Allow: {', '.join(sorted(metode_lain))}\")\n            else:\n                print(f\"{isi} -> 404\")\n            continue\n        menang = calon[0]\n        for c in calon[1:]:\n            if lebih_spesifik(c[1], menang[1]):\n                menang = c\n        teks, _, nilai = menang\n        isian = \"\".join(f\" {k}={v}\" for k, v in nilai.items())\n        print(f\"{isi} -> {teks}{isian}\")",
        "stdin_list": [
            """pola GET /items/{id}
pola GET /items/latest
pola /items/
pola POST /items
pola GET /{$}
minta GET /items/7
minta GET /items/latest
minta GET /items/7/foto
minta DELETE /items/7
minta PUT /items
minta GET /
minta GET /lain
""",
            """pola GET /files/{path...}
pola /files/{nama}
pola GET /files/{path...}
pola GET /{a}/x
pola GET /files/readme
minta GET /files/readme
minta GET /files/a/b
minta GET /files/
minta POST /files/a
""",
            """pola GET /users/{id}
pola GET /users/{id}/posts/{pid}
minta GET /users/5/posts/9
minta GET /users/
minta GET /users/5
""",
        ],
    },
    {
        "title": "Latihan 15: Sesi dan Cookie dengan Jam Palsu",
        "difficulty": "Lanjut",
        "question": [
            "Buat penyimpan sesi di memori. Jam disuntikkan: tiap baris stdin diawali",
            "t=DETIK. Pengguna tetap: budi dengan sandi rahasia1 dan sari dengan",
            "sandi kopi2026 (anggap pemeriksaan hash sandinya sudah ada). Sesi",
            "berumur 1800 detik sejak login, dan id sesi diambil dari penghitung: s1,",
            "s2, dan seterusnya (di aplikasi nyata pakai secrets.token_urlsafe).",
            "",
            "Perintahnya di bawah ini. Tiap baris keluaran diawali t=DETIK PERINTAH:",
            "lalu hasilnya.",
            "",
            "  - LOGIN nama sandi [sid=X]: sandi salah cetak 401 nama atau sandi",
            "    salah. Kalau ada sid=X yang masih tercatat, buang dulu dan cetak",
            "    sesi lama X dibuang. Lalu cetak 200 Set-Cookie: sid=BARU; HttpOnly;",
            "    Secure; SameSite=Lax; Path=/; Max-Age=1800.",
            "  - GET [sid=X]: tanpa sid cetak 401 belum login; sid tak dikenal cetak",
            "    401 sesi tidak dikenal; kalau t >= waktu habis, hapus sesinya dan",
            "    cetak 401 sesi kedaluwarsa; selain itu 200 halo NAMA, sisa N detik.",
            "  - LOGOUT sid=X: hapus sesi dan cetak 200 dengan Set-Cookie sid kosong",
            "    dan Max-Age=0.",
            "  - Di akhir cetak sesi aktif: daftar sid urut abjad, atau tidak ada.",
            "",
            "",
            "Untuk input t=100 LOGIN budi rahasia1, keluarannya:",
            "",
            "t=100 LOGIN: 200 Set-Cookie: sid=s1; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1800",
            "t=150 GET: 200 halo budi, sisa 1750 detik",
            "t=200 GET: 401 belum login",
            "t=1900 GET: 401 sesi kedaluwarsa",
            "t=1950 LOGIN: 401 nama atau sandi salah",
            "t=2000 LOGIN: 200 Set-Cookie: sid=s2; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1800",
            "t=2100 LOGOUT: 200 Set-Cookie: sid=; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=0",
            "t=2150 GET: 401 sesi tidak dikenal",
            "sesi aktif: tidak ada",
            "",
            "",
            "Untuk input t=0 LOGIN sari kopi2026, keluarannya:",
            "",
            "t=0 LOGIN: 200 Set-Cookie: sid=s1; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1800",
            "t=10 LOGIN: sesi lama s1 dibuang",
            "t=10 LOGIN: 200 Set-Cookie: sid=s2; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1800",
            "t=20 GET: 401 sesi tidak dikenal",
            "t=30 GET: 200 halo sari, sisa 1780 detik",
            "t=40 GET: 401 sesi tidak dikenal",
            "sesi aktif: s2",
        ],
        "hints": [
            "Simpan sesi sebagai dict dari id ke pasangan (nama, waktu habis), dan jangan pernah membaca jam sistem.",
            "Pisahkan tiap baris jadi waktu, perintah, sid (kalau ada kata berawalan sid=), dan argumen sisanya.",
            "Tulis satu fungsi periksa(sid, t) yang mengembalikan nama atau alasan penolakan, lalu pakai di GET.",
            "Saat LOGIN berhasil, buang sid lama lebih dulu supaya id sesi selalu baru, persis obat session fixation.",
        ],
        "solution": "import sys\n\nPENGGUNA = {\"budi\": \"rahasia1\", \"sari\": \"kopi2026\"}\nUMUR = 1800\nATRIBUT = \"HttpOnly; Secure; SameSite=Lax; Path=/\"\n\nsesi = {}          # sid -> (nama, kedaluwarsa)\nnomor = 0\n\n\ndef cookie(sid, umur):\n    return f\"Set-Cookie: sid={sid}; {ATRIBUT}; Max-Age={umur}\"\n\n\ndef periksa(sid, t):\n    \"\"\"(nama, None) kalau sesi sah, atau (None, alasan).\"\"\"\n    if sid is None:\n        return None, \"belum login\"\n    if sid not in sesi:\n        return None, \"sesi tidak dikenal\"\n    nama, habis = sesi[sid]\n    if t >= habis:\n        del sesi[sid]\n        return None, \"sesi kedaluwarsa\"\n    return nama, None\n\n\nfor baris in sys.stdin.read().splitlines():\n    kata = baris.split()\n    if not kata:\n        continue\n    t = int(kata[0][2:])\n    perintah = kata[1]\n    sid = next((k[4:] for k in kata[2:] if k.startswith(\"sid=\")), None)\n    argumen = [k for k in kata[2:] if not k.startswith(\"sid=\")]\n    awal = f\"t={t} {perintah}:\"\n\n    if perintah == \"LOGIN\":\n        nama, sandi = argumen\n        if PENGGUNA.get(nama) != sandi:\n            print(awal, \"401 nama atau sandi salah\")\n            continue\n        if sid in sesi:\n            del sesi[sid]\n            print(awal, f\"sesi lama {sid} dibuang\")\n        nomor += 1\n        baru = f\"s{nomor}\"\n        sesi[baru] = (nama, t + UMUR)\n        print(awal, \"200\", cookie(baru, UMUR))\n    elif perintah == \"GET\":\n        nama, alasan = periksa(sid, t)\n        if alasan:\n            print(awal, \"401\", alasan)\n        else:\n            print(awal, f\"200 halo {nama}, sisa {sesi[sid][1] - t} detik\")\n    elif perintah == \"LOGOUT\":\n        sesi.pop(sid, None)\n        print(awal, \"200\", cookie(\"\", 0))\nprint(\"sesi aktif:\", \", \".join(sorted(sesi)) or \"tidak ada\")",
        "stdin_list": [
            """t=100 LOGIN budi rahasia1
t=150 GET sid=s1
t=200 GET
t=1900 GET sid=s1
t=1950 LOGIN sari salah
t=2000 LOGIN sari kopi2026
t=2100 LOGOUT sid=s2
t=2150 GET sid=s2
""",
            """t=0 LOGIN sari kopi2026
t=10 LOGIN sari kopi2026 sid=s1
t=20 GET sid=s1
t=30 GET sid=s2
t=40 GET sid=s99
""",
        ],
    },
    {
        "title": "Latihan 16: JWT HS256 Buatan Sendiri",
        "difficulty": "Lanjut",
        "question": [
            "Buat dan verifikasi JWT HS256 hanya dengan hmac, hashlib, base64, dan",
            "json. Kuncinya b\"kunci-rahasia-latihan\". Header selalu",
            "{\"alg\":\"HS256\",\"typ\":\"JWT\"}. JSON ditulis dengan sort_keys=True dan",
            "separators=(\",\", \":\"), lalu dikodekan base64url tanpa tanda = di ujung.",
            "",
            "Perintah di stdin:",
            "",
            "  - buat k=v ...: buat token dari klaim itu (nilai angka jadi int) dan",
            "    cetak token $N: TOKEN, N mulai dari 1.",
            "  - cek DETIK TOKEN: TOKEN boleh berupa $N (token buatan sebelumnya).",
            "    Cetak cek LABEL pada t=DETIK: HASIL. LABEL adalah $N, atau 12 huruf",
            "    pertama token diikuti ....",
            "",
            "HASIL diperiksa berurutan: bukan tiga bagian atau gagal diurai jadi",
            "ditolak: format salah; alg selain HS256 jadi ditolak: alg X tidak",
            "diterima; tanda tangan beda jadi ditolak: tanda tangan salah (bandingkan",
            "dengan hmac.compare_digest); tanpa exp atau DETIK >= exp jadi ditolak:",
            "kedaluwarsa; selain itu sah: diikuti payload dalam JSON ringkas.",
            "",
            "",
            "Untuk input buat sub=budi peran=kasir exp=1700000900, keluarannya:",
            "",
            "token $1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDAwMDA5MDAsInBlcmFuIjoia2FzaXIiLCJzdWIiOiJidWRpIn0._VmvEzA67Zl-mxv0EEZjZEnvtvlYya_cQhe1ixqCYd8",
            "cek $1 pada t=1700000000: sah: {\"exp\":1700000900,\"peran\":\"kasir\",\"sub\":\"budi\"}",
            "cek $1 pada t=1700000900: ditolak: kedaluwarsa",
            "cek eyJhbGciOiJI... pada t=1700000000: ditolak: tanda tangan salah",
            "cek eyJhbGciOiJu... pada t=1700000000: ditolak: alg none tidak diterima",
            "cek bukan-token... pada t=1700000000: ditolak: format salah",
            "",
            "",
            "Untuk input buat sub=sari peran=admin exp=500, keluarannya:",
            "",
            "token $1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjUwMCwicGVyYW4iOiJhZG1pbiIsInN1YiI6InNhcmkifQ.ct_od5qIbhdzAb2YhO-ZJbHjI4nAHaFc1TIJqAOI5kA",
            "token $2: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEwMCwic3ViIjoidGFtdSJ9.ckYX8hxeNgJDntRTBe0ItuLBnjPzj3F1y1YWqo90hTg",
            "cek $2 pada t=99: sah: {\"exp\":100,\"sub\":\"tamu\"}",
            "cek $2 pada t=100: ditolak: kedaluwarsa",
            "cek $1 pada t=400: sah: {\"exp\":500,\"peran\":\"admin\",\"sub\":\"sari\"}",
        ],
        "hints": [
            "Mulai dari dua fungsi kecil, b64 dan unb64, karena base64url tanpa padding dipakai di semua bagian token.",
            "Tanda tangan dihitung dari teks kepala.badan yang sudah dikodekan, bukan dari dict aslinya.",
            "Periksa alg dari header sebelum menghitung tanda tangan, supaya token alg none ditolak dengan alasan yang tepat.",
            "Untuk unb64, tambahkan \"=\" * (-len(teks) % 4) sebelum memanggil base64.urlsafe_b64decode.",
        ],
        "solution": """import base64
import hashlib
import hmac
import json
import sys

KUNCI = b"kunci-rahasia-latihan"


def b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def unb64(teks):
    return base64.urlsafe_b64decode(teks + "=" * (-len(teks) % 4))


def json_ringkas(isi):
    return json.dumps(isi, sort_keys=True, separators=(",", ":")).encode()


def tanda_tangan(bagian):
    return b64(hmac.new(KUNCI, bagian.encode(), hashlib.sha256).digest())


def buat(payload):
    kepala = b64(json_ringkas({"alg": "HS256", "typ": "JWT"}))
    badan = b64(json_ringkas(payload))
    return f"{kepala}.{badan}.{tanda_tangan(kepala + '.' + badan)}"


def cek(token, sekarang):
    bagian = token.split(".")
    if len(bagian) != 3:
        return "ditolak: format salah"
    try:
        kepala = json.loads(unb64(bagian[0]))
        payload = json.loads(unb64(bagian[1]))
    except ValueError:
        return "ditolak: format salah"
    if kepala.get("alg") != "HS256":
        return f"ditolak: alg {kepala.get('alg')} tidak diterima"
    harap = tanda_tangan(bagian[0] + "." + bagian[1])
    if not hmac.compare_digest(harap, bagian[2]):
        return "ditolak: tanda tangan salah"
    if "exp" not in payload or sekarang >= payload["exp"]:
        return "ditolak: kedaluwarsa"
    return "sah: " + json_ringkas(payload).decode()


dibuat = []
for baris in sys.stdin.read().splitlines():
    kata = baris.split()
    if not kata:
        continue
    if kata[0] == "buat":
        payload = {}
        for pasang in kata[1:]:
            k, v = pasang.split("=", 1)
            payload[k] = int(v) if v.isdigit() else v
        dibuat.append(buat(payload))
        print(f"token ${len(dibuat)}: {dibuat[-1]}")
    elif kata[0] == "cek":
        sekarang, token = int(kata[1]), kata[2]
        if token.startswith("$"):
            token = dibuat[int(token[1:]) - 1]
            label = kata[2]
        else:
            label = token[:12] + "..."
        print(f"cek {label} pada t={sekarang}: {cek(token, sekarang)}")""",
        "stdin_list": [
            """buat sub=budi peran=kasir exp=1700000900
cek 1700000000 $1
cek 1700000900 $1
cek 1700000000 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDAwMDA5MDAsInBlcmFuIjoiYWRtaW4iLCJzdWIiOiJidWRpIn0._VmvEzA67Zl-mxv0EEZjZEnvtvlYya_cQhe1ixqCYd8
cek 1700000000 eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJleHAiOjE3MDAwMDA5MDAsInBlcmFuIjoiYWRtaW4iLCJzdWIiOiJidWRpIn0.
cek 1700000000 bukan-token
""",
            """buat sub=sari peran=admin exp=500
buat sub=tamu exp=100
cek 99 $2
cek 100 $2
cek 400 $1
""",
        ],
    },
    {
        "title": "Latihan 17: TOTP dengan Vektor Uji RFC 6238",
        "difficulty": "Lanjut",
        "question": [
            "Tulis HOTP dan TOTP sendiri dengan modul hmac, struct, dan hashlib",
            "(SHA-1, 8 digit, langkah 30 detik), lalu cocokkan dengan vektor",
            "uji Appendix B RFC 6238. Rahasianya dipatok: string ASCII",
            "\"12345678901234567890\". Jam tidak dibaca dari komputer; waktu",
            "(detik Unix) datang dari input.",
            "",
            "Tiap baris input berupa salah satu perintah:",
            "  totp T          cetak: T=<T> langkah=<T // 30> kode=<8 digit>",
            "  cek T KODE      periksa KODE dengan toleransi satu langkah:",
            "                  coba langkah sekarang, lalu -1, lalu +1.",
            "                  cetak: cek T=<T> <KODE>: valid (geser <+0/-1/+1>)",
            "                  atau:  cek T=<T> <KODE>: tidak valid",
            "",
            "Ingat cara HOTP memotong hasil HMAC: ambil 4 bit terakhir byte",
            "terakhir sebagai posisi, baca 4 byte mulai posisi itu sebagai",
            "bilangan big-endian, buang bit tertinggi, lalu modulo 10^8.",
            "",
            "Untuk input totp 59, keluarannya:",
            "T=59 langkah=1 kode=94287082",
            "T=1111111109 langkah=37037036 kode=07081804",
            "T=1111111111 langkah=37037037 kode=14050471",
            "T=1234567890 langkah=41152263 kode=89005924",
            "T=2000000000 langkah=66666666 kode=69279037",
            "T=20000000000 langkah=666666666 kode=65353130",
            "",
            "Untuk input cek 59 94287082, keluarannya:",
            "cek T=59 94287082: valid (geser +0)",
            "cek T=89 94287082: valid (geser -1)",
            "cek T=29 94287082: valid (geser +1)",
            "cek T=120 94287082: tidak valid",
            "cek T=1111111111 07081804: valid (geser -1)",
            "cek T=1111111111 00000000: tidak valid",
        ],
        "hints": [
            "TOTP adalah HOTP yang penghitungnya diganti waktu dibagi 30, jadi tulis fungsi hotp dulu lalu totp cukup memanggilnya.",
            "Penghitung dikemas jadi 8 byte big-endian dengan struct.pack('>Q', n), lalu HMAC-SHA1 dengan kunci rahasia menghasilkan 20 byte.",
            "Posisi potongan adalah h[-1] & 0x0F, angkanya struct.unpack('>I', h[p:p+4])[0] & 0x7FFFFFFF, dan hasilnya diisi nol di depan dengan zfill(8).",
        ],
        "solution": """import hmac
import struct
import sys

RAHASIA = b"12345678901234567890"
LANGKAH = 30
DIGIT = 8


def hotp(kunci, penghitung):
    pesan = struct.pack(">Q", penghitung)
    h = hmac.new(kunci, pesan, "sha1").digest()
    geser = h[-1] & 0x0F
    angka = struct.unpack(">I", h[geser:geser + 4])[0] & 0x7FFFFFFF
    return str(angka % 10 ** DIGIT).zfill(DIGIT)


def totp(kunci, t):
    return hotp(kunci, t // LANGKAH)


def cek(kunci, t, kode):
    for geser in (0, -1, 1):
        penghitung = t // LANGKAH + geser
        if penghitung >= 0 and hotp(kunci, penghitung) == kode:
            return geser
    return None


for baris in sys.stdin.read().splitlines():
    bagian = baris.split()
    if not bagian:
        continue
    if bagian[0] == "totp":
        t = int(bagian[1])
        print(f"T={t} langkah={t // LANGKAH} kode={totp(RAHASIA, t)}")
    elif bagian[0] == "cek":
        t, kode = int(bagian[1]), bagian[2]
        geser = cek(RAHASIA, t, kode)
        if geser is None:
            print(f"cek T={t} {kode}: tidak valid")
        else:
            print(f"cek T={t} {kode}: valid (geser {geser:+d})")
""",
        "stdin_list": [
            """totp 59
totp 1111111109
totp 1111111111
totp 1234567890
totp 2000000000
totp 20000000000
""",
            """cek 59 94287082
cek 89 94287082
cek 29 94287082
cek 120 94287082
cek 1111111111 07081804
cek 1111111111 00000000
""",
        ],
    },
    {
        "title": "Latihan 18: Token Bucket dengan Jam Palsu",
        "difficulty": "Lanjut",
        "question": [
            "Buat rate limiter token bucket per alamat IP, lengkap dengan",
            "idempotency key. Jam disuntikkan lewat input, bukan time.time().",
            "",
            "Aturan:",
            "  - Tiap IP punya ember sendiri: kapasitas 3 token, mulai penuh",
            "    pada t=0, diisi ulang 1 token per detik (pecahan ikut dihitung,",
            "    tidak melebihi kapasitas).",
            "  - Tiap baris input: t=<detik, boleh desimal> ip=<nama> dan",
            "    opsional key=<idempotency key>.",
            "  - Kalau token >= 1: ambil satu, cetak",
            "    t=<t> <ip> 200 sisa=<token bulat yang tersisa>",
            "  - Kalau kurang: cetak t=<t> <ip> 429 Retry-After=<detik>, dengan",
            "    detik = waktu sampai token penuh satu, dibulatkan ke atas.",
            "  - Respons 200 yang membawa key disimpan per (ip, key). Permintaan",
            "    berikutnya dengan ip dan key yang sama tidak mengambil token;",
            "    cetak respons tersimpan diikuti (ulang key=<key>).",
            "    Respons 429 tidak disimpan.",
            "",
            "Hitung dalam mili-token (bilangan bulat) supaya pecahan desimal",
            "tidak menimbulkan galat pembulatan.",
            "",
            "Untuk input t=0.0 ip=A, keluarannya:",
            "t=0.0 A 200 sisa=2",
            "t=0.1 A 200 sisa=1",
            "t=0.2 A 200 sisa=0",
            "t=0.3 A 429 Retry-After=1",
            "t=0.3 B 200 sisa=2",
            "t=1.2 A 200 sisa=0",
            "t=1.2 A 429 Retry-After=1",
            "t=5.0 A 200 sisa=2",
            "",
            "Untuk input t=0 ip=C key=bayar-1, keluarannya:",
            "t=0 C 200 sisa=2",
            "t=0.5 C 200 sisa=2 (ulang key=bayar-1)",
            "t=0.6 C 200 sisa=1",
            "t=0.7 C 200 sisa=0",
            "t=0.8 C 429 Retry-After=1",
            "t=0.9 C 200 sisa=2 (ulang key=bayar-1)",
            "t=2.5 C 200 sisa=1",
            "t=2.6 C 200 sisa=1 (ulang key=bayar-2)",
        ],
        "hints": [
            "Simpan untuk tiap IP dua angka saja: sisa token dan waktu permintaan terakhir, lalu isi ulang berdasarkan jedanya setiap kali ada permintaan baru.",
            "Kalau satu token = 1000 mili-token dan lajunya 1 token per detik, maka tiap milidetik jeda menambah tepat 1 mili-token.",
            "Untuk idempotency, pakai dict berkunci tuple (ip, key) yang diperiksa sebelum ember disentuh, dan isi dict itu hanya ketika hasilnya 200.",
        ],
        "solution": """import sys

KAPASITAS = 3
MS_PER_TOKEN = 1000


class Ember:
    def __init__(self):
        self.mili_token = KAPASITAS * MS_PER_TOKEN
        self.terakhir = 0

    def ambil(self, t_ms):
        jeda = t_ms - self.terakhir
        self.terakhir = t_ms
        self.mili_token = min(KAPASITAS * MS_PER_TOKEN, self.mili_token + jeda)
        if self.mili_token >= MS_PER_TOKEN:
            self.mili_token -= MS_PER_TOKEN
            return True, 0
        kurang = MS_PER_TOKEN - self.mili_token
        return False, (kurang + 999) // 1000


def ke_ms(teks):
    detik, _, pecahan = teks.partition(".")
    pecahan = (pecahan + "000")[:3]
    return int(detik) * 1000 + int(pecahan)


ember = {}
simpanan = {}
for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    medan = dict(potong.split("=", 1) for potong in baris.split())
    t_teks, ip, key = medan["t"], medan["ip"], medan.get("key")
    awal = f"t={t_teks} {ip}"
    if key and (ip, key) in simpanan:
        print(f"{awal} {simpanan[(ip, key)]} (ulang key={key})")
        continue
    e = ember.setdefault(ip, Ember())
    lolos, tunggu = e.ambil(ke_ms(t_teks))
    if lolos:
        respons = f"200 sisa={e.mili_token // MS_PER_TOKEN}"
        if key:
            simpanan[(ip, key)] = respons
        print(f"{awal} {respons}")
    else:
        print(f"{awal} 429 Retry-After={tunggu}")
""",
        "stdin_list": [
            """t=0.0 ip=A
t=0.1 ip=A
t=0.2 ip=A
t=0.3 ip=A
t=0.3 ip=B
t=1.2 ip=A
t=1.2 ip=A
t=5.0 ip=A
""",
            """t=0 ip=C key=bayar-1
t=0.5 ip=C key=bayar-1
t=0.6 ip=C
t=0.7 ip=C
t=0.8 ip=C key=bayar-2
t=0.9 ip=C key=bayar-1
t=2.5 ip=C key=bayar-2
t=2.6 ip=C key=bayar-2
""",
        ],
    },
    {
        "title": "Latihan 19: Cache LRU dengan TTL",
        "difficulty": "Lanjut",
        "question": [
            "Buat cache berkapasitas 3 dengan penggusuran LRU dan TTL, di atas",
            "collections.OrderedDict. Jam disuntikkan: mulai dari 0 dan hanya",
            "maju lewat perintah TICK.",
            "",
            "Perintah (satu per baris):",
            "  SET kunci nilai [ttl]   simpan; tanpa ttl berarti tidak pernah",
            "                          kedaluwarsa. Entri kedaluwarsa kalau",
            "                          jam >= jam_simpan + ttl.",
            "  GET kunci               ambil; GET yang berhasil membuat kunci",
            "                          jadi yang paling baru dipakai.",
            "  TICK n                  majukan jam n detik.",
            "",
            "Aturan SET untuk kunci baru: buang dulu semua entri yang sudah",
            "kedaluwarsa (urut dari yang paling lama dipakai), lalu kalau",
            "masih penuh, gusur entri yang paling lama tidak dipakai. SET",
            "untuk kunci yang sudah ada cukup menimpa nilainya dan menjadikannya",
            "paling baru. Catatan buang/gusur ditulis di dalam kurung siku.",
            "",
            "Di akhir, cetak urutan isi dari yang paling lama ke paling baru",
            "dipakai, lalu statistik hit, miss, dan hit_rate (persen, dibulatkan",
            "ke bawah).",
            "",
            "Untuk input SET a 1, keluarannya:",
            "SET a OK",
            "SET b OK",
            "SET c OK",
            "GET a -> 1",
            "SET d OK [gusur b]",
            "GET b -> miss",
            "GET c -> 3",
            "SET e OK [gusur a]",
            "isi (lama -> baru): d c e",
            "hit=2 miss=1 hit_rate=66%",
        ],
        "hints": [
            "Simpan nilai bersama waktu habisnya, misalnya tuple (nilai, habis) dengan habis None untuk entri tanpa TTL.",
            "OrderedDict menjaga urutan: move_to_end(k) menjadikan k paling baru, dan popitem(last=False) mengambil yang paling lama.",
            "Periksa kedaluwarsa di dua tempat saja: saat GET (balas miss lalu hapus) dan saat SET kunci baru (buang semua yang habis sebelum menggusur).",
        ],
        "solution": """import sys
from collections import OrderedDict

KAPASITAS = 3


class CacheLRU:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.isi = OrderedDict()
        self.jam = 0
        self.hit = 0
        self.miss = 0

    def _kedaluwarsa(self, kunci):
        _, habis = self.isi[kunci]
        return habis is not None and habis <= self.jam

    def set(self, kunci, nilai, ttl):
        habis = None if ttl is None else self.jam + ttl
        catatan = []
        if kunci in self.isi:
            del self.isi[kunci]
        else:
            for k in [k for k in self.isi if self._kedaluwarsa(k)]:
                del self.isi[k]
                catatan.append(f"buang {k} (kedaluwarsa)")
            if len(self.isi) >= self.kapasitas:
                lama, _ = self.isi.popitem(last=False)
                catatan.append(f"gusur {lama}")
        self.isi[kunci] = (nilai, habis)
        tambahan = f" [{', '.join(catatan)}]" if catatan else ""
        return f"SET {kunci} OK{tambahan}"

    def get(self, kunci):
        if kunci not in self.isi:
            self.miss += 1
            return f"GET {kunci} -> miss"
        if self._kedaluwarsa(kunci):
            del self.isi[kunci]
            self.miss += 1
            return f"GET {kunci} -> miss (kedaluwarsa)"
        self.isi.move_to_end(kunci)
        self.hit += 1
        return f"GET {kunci} -> {self.isi[kunci][0]}"


cache = CacheLRU(KAPASITAS)
for baris in sys.stdin.read().splitlines():
    bagian = baris.split()
    if not bagian:
        continue
    if bagian[0] == "SET":
        ttl = int(bagian[3]) if len(bagian) > 3 else None
        print(cache.set(bagian[1], bagian[2], ttl))
    elif bagian[0] == "GET":
        print(cache.get(bagian[1]))
    elif bagian[0] == "TICK":
        cache.jam += int(bagian[1])
        print(f"TICK -> jam={cache.jam}")

urutan = " ".join(cache.isi)
total = cache.hit + cache.miss
rasio = 100 * cache.hit // total if total else 0
print(f"isi (lama -> baru): {urutan}")
print(f"hit={cache.hit} miss={cache.miss} hit_rate={rasio}%")
""",
        "stdin_list": [
            """SET a 1
SET b 2
SET c 3
GET a
SET d 4
GET b
GET c
SET e 5
""",
            """SET sesi:1 budi 10
SET sesi:2 sari 30
SET konfig gelap
TICK 5
GET sesi:1
TICK 5
GET sesi:1
GET konfig
SET sesi:3 andi 10
SET sesi:4 rina
TICK 25
GET sesi:2
SET sesi:5 dodi 5
GET konfig
""",
        ],
    },
    {
        "title": "Latihan 20: Log Kafka Mini dengan Consumer Group",
        "difficulty": "Sulit",
        "question": [
            "Tiru Kafka di Python: topik berpartisi, offset per consumer group,",
            "commit, dan rebalance. Perintah (satu per baris):",
            "",
            "  topik N              buat topik dengan N partisi (p0..pN-1).",
            "  kirim KUNCI NILAI    partisi = zlib.crc32(KUNCI.encode()) % N;",
            "                       cetak kirim KUNCI:NILAI -> p<partisi>@<offset>",
            "  gabung GRUP NAMA     NAMA masuk GRUP, lalu rebalance.",
            "  keluar GRUP NAMA     NAMA keluar dari GRUP, lalu rebalance.",
            "  poll GRUP NAMA MAKS  baca paling banyak MAKS pesan dari partisi",
            "                       milik NAMA (urut nomor partisi), mulai dari",
            "                       posisi baca grup; cetak p<p>@<offset>=<isi>",
            "                       dipisah koma, atau - kalau kosong.",
            "  commit GRUP NAMA     simpan posisi baca partisi milik NAMA sebagai",
            "                       offset commit grup; cetak semua commit grup.",
            "  isi                  cetak isi tiap partisi.",
            "",
            "Rebalance: urutkan nama anggota, bagikan partisi 0, 1, 2, ...",
            "bergiliran ke anggota menurut urutan itu. Sesudah rebalance, posisi",
            "baca semua partisi kembali ke offset commit (belum pernah commit",
            "berarti 0), jadi pesan yang belum di-commit terbaca lagi.",
            "",
            "Untuk input topik 3, keluarannya:",
            "topik dibuat dengan 3 partisi",
            "kirim budi:pesan -> p1@0",
            "kirim andi:pesan -> p2@0",
            "kirim toko-3:stok -> p0@0",
            "kirim budi:bayar -> p1@1",
            "kirim rina:pesan -> p2@1",
            "kirim u2:klik -> p0@1",
            "rebalance gudang: k1=[0, 1, 2]",
            "poll gudang/k1: p0@0=toko-3:stok, p0@1=u2:klik, p1@0=budi:pesan",
            "commit gudang/k1: p0=2, p1=1, p2=0",
            "rebalance gudang: k1=[0, 2], k2=[1]",
            "poll gudang/k2: p1@1=budi:bayar",
            "poll gudang/k1: p2@0=andi:pesan, p2@1=rina:pesan",
            "rebalance analitik: a1=[0, 1, 2]",
            "poll analitik/a1: p0@0=toko-3:stok, p0@1=u2:klik",
            "p0: toko-3:stok u2:klik",
            "p1: budi:pesan budi:bayar",
            "p2: andi:pesan rina:pesan",
        ],
        "hints": [
            "Pisahkan dua angka per partisi di tiap grup: posisi baca yang maju saat poll, dan offset commit yang hanya berubah saat commit.",
            "Rebalance cukup membangun ulang pembagian partisi dari nama anggota yang diurutkan, lalu menyalin offset commit ke posisi baca.",
            "Simpan tiap grup sebagai objek berisi daftar anggota, dict pembagian nama ke daftar partisi, dict commit, dan dict posisi, lalu poll berjalan dari posisi sampai ujung log atau sampai MAKS.",
        ],
        "solution": """import sys
import zlib


class Grup:
    def __init__(self):
        self.anggota = []
        self.bagian = {}
        self.commit = {}
        self.posisi = {}


partisi = []
grup = {}


def rebalance(nama):
    g = grup[nama]
    g.bagian = {k: [] for k in g.anggota}
    urut = sorted(g.anggota)
    for p in range(len(partisi)):
        if urut:
            g.bagian[urut[p % len(urut)]].append(p)
    g.posisi = dict(g.commit)
    rincian = ", ".join(f"{k}={g.bagian[k]}" for k in urut) or "kosong"
    print(f"rebalance {nama}: {rincian}")


for baris in sys.stdin.read().splitlines():
    b = baris.split()
    if not b:
        continue
    if b[0] == "topik":
        partisi = [[] for _ in range(int(b[1]))]
        print(f"topik dibuat dengan {b[1]} partisi")
    elif b[0] == "kirim":
        kunci, nilai = b[1], b[2]
        p = zlib.crc32(kunci.encode()) % len(partisi)
        partisi[p].append(f"{kunci}:{nilai}")
        print(f"kirim {kunci}:{nilai} -> p{p}@{len(partisi[p]) - 1}")
    elif b[0] == "gabung":
        g = grup.setdefault(b[1], Grup())
        g.anggota.append(b[2])
        rebalance(b[1])
    elif b[0] == "keluar":
        grup[b[1]].anggota.remove(b[2])
        rebalance(b[1])
    elif b[0] == "poll":
        g, konsumen, maks = grup[b[1]], b[2], int(b[3])
        dapat = []
        for p in g.bagian.get(konsumen, []):
            mulai = g.posisi.get(p, 0)
            while mulai < len(partisi[p]) and len(dapat) < maks:
                dapat.append(f"p{p}@{mulai}={partisi[p][mulai]}")
                mulai += 1
            g.posisi[p] = mulai
        print(f"poll {b[1]}/{konsumen}: {', '.join(dapat) or '-'}")
    elif b[0] == "commit":
        g, konsumen = grup[b[1]], b[2]
        for p in g.bagian.get(konsumen, []):
            if p in g.posisi:
                g.commit[p] = g.posisi[p]
        rincian = ", ".join(f"p{p}={g.commit[p]}" for p in sorted(g.commit))
        print(f"commit {b[1]}/{konsumen}: {rincian}")
    elif b[0] == "isi":
        for p, log in enumerate(partisi):
            print(f"p{p}: {' '.join(log) or '-'}")
""",
        "stdin_list": [
            """topik 3
kirim budi pesan
kirim andi pesan
kirim toko-3 stok
kirim budi bayar
kirim rina pesan
kirim u2 klik
gabung gudang k1
poll gudang k1 3
commit gudang k1
gabung gudang k2
poll gudang k2 5
poll gudang k1 5
gabung analitik a1
poll analitik a1 2
isi
""",
            """topik 2
kirim A satu
kirim B dua
kirim C tiga
kirim D empat
gabung g x
gabung g y
poll g x 10
poll g y 1
commit g y
keluar g y
poll g x 10
commit g x
kirim B lima
poll g x 10
isi
""",
        ],
    },
    {
        "title": "Latihan 21: Pelaksana Kueri GraphQL Mini",
        "difficulty": "Sulit",
        "question": [
            "Tulis pengurai dan pelaksana GraphQL mini. Kueri dibaca dari stdin",
            "(boleh beberapa baris), tanpa argumen, alias, variabel, atau",
            "fragment. Kata query dan nama operasi di depannya boleh ada.",
            "",
            "Skema dan data ditanam di kode:",
            "  Query { me: User, users: [User] }",
            "  User  { id: ID, name: String, posts: [Post] }",
            "  Post  { id: ID, title: String, likes: Int }",
            "  me = Budi (id 1, dua post), users = Budi dan Sari (Sari tanpa post)",
            "",
            "Validasi dulu seluruh kueri terhadap skema. Pesan galat (urut sesuai",
            "kemunculan di kueri):",
            "  field tak ada : Cannot query field \"X\" on type \"T\".",
            "  objek tanpa { }: Field \"X\" of type \"T\" must have a selection",
            "                  of subfields.",
            "  skalar diberi { }: Field \"X\" must not have a selection since",
            "                  type \"T\" has no subfields.",
            "Kalau ada galat, cetak {\"errors\": [...]} tanpa data. Kalau tidak,",
            "cetak {\"data\": ...} yang bentuknya persis mengikuti kueri. Cetak",
            "dengan json.dumps(..., indent=2).",
            "",
            "Untuk input { me { name posts { title } } }, keluarannya:",
            "{",
            "  \"data\": {",
            "    \"me\": {",
            "      \"name\": \"Budi\",",
            "      \"posts\": [",
            "        {",
            "          \"title\": \"Belajar API\"",
            "        },",
            "        {",
            "          \"title\": \"Cache\"",
            "        }",
            "      ]",
            "    }",
            "  }",
            "}",
            "",
            "Untuk input { me { name email posts } }, keluarannya:",
            "{",
            "  \"errors\": [",
            "    {",
            "      \"message\": \"Cannot query field \\\"email\\\" on type \\\"User\\\".\"",
            "    },",
            "    {",
            "      \"message\": \"Field \\\"posts\\\" of type \\\"[Post]\\\" must have a selection of subfields.\"",
            "    }",
            "  ]",
            "}",
        ],
        "hints": [
            "Pisahkan tiga tahap seperti server sungguhan: pecah teks jadi token, urai token jadi pohon pilihan field, lalu periksa pohon itu terhadap skema sebelum menjalankannya.",
            "Token cukup tiga jenis: kurung kurawal buka, kurung kurawal tutup, dan nama; pengurai rekursif membaca nama demi nama sampai bertemu kurung tutup, dan kalau sesudah nama ada kurung buka, ia memanggil dirinya sendiri.",
            "Simpan tipe field sebagai string seperti \"[Post]\"; buang kurung siku untuk mendapat tipe dasarnya, dan kalau tipenya daftar, jalankan pilihan anak untuk setiap elemen.",
        ],
        "solution": """import json
import sys

DATA_USERS = [
    {"id": "1", "name": "Budi", "posts": [
        {"id": "10", "title": "Belajar API", "likes": 12},
        {"id": "11", "title": "Cache", "likes": 4}]},
    {"id": "2", "name": "Sari", "posts": []},
]

SKEMA = {
    "Query": {"me": "User", "users": "[User]"},
    "User": {"id": "ID", "name": "String", "posts": "[Post]"},
    "Post": {"id": "ID", "title": "String", "likes": "Int"},
}
SKALAR = {"ID", "String", "Int"}

RESOLVER = {
    ("Query", "me"): lambda induk: DATA_USERS[0],
    ("Query", "users"): lambda induk: DATA_USERS,
}


def token(teks):
    hasil, kata = [], ""
    for c in teks:
        if c in "{}":
            if kata:
                hasil.append(kata)
                kata = ""
            hasil.append(c)
        elif c.isspace():
            if kata:
                hasil.append(kata)
                kata = ""
        else:
            kata += c
    if kata:
        hasil.append(kata)
    return hasil


def urai(tok, i):
    pilihan = []
    i += 1
    while tok[i] != "}":
        nama = tok[i]
        i += 1
        anak = None
        if i < len(tok) and tok[i] == "{":
            anak, i = urai(tok, i)
        pilihan.append((nama, anak))
    return pilihan, i + 1


def tipe_dasar(tipe):
    return tipe.strip("[]")


def periksa(tipe, pilihan, galat):
    for nama, anak in pilihan:
        if nama not in SKEMA[tipe]:
            galat.append(f'Cannot query field "{nama}" on type "{tipe}".')
            continue
        tf = SKEMA[tipe][nama]
        dasar = tipe_dasar(tf)
        if dasar in SKALAR and anak is not None:
            galat.append(f'Field "{nama}" must not have a selection since '
                         f'type "{tf}" has no subfields.')
        elif dasar not in SKALAR and anak is None:
            galat.append(f'Field "{nama}" of type "{tf}" must have a '
                         'selection of subfields.')
        elif anak is not None:
            periksa(dasar, anak, galat)


def jalankan(tipe, objek, pilihan):
    hasil = {}
    for nama, anak in pilihan:
        tf = SKEMA[tipe][nama]
        resolver = RESOLVER.get((tipe, nama), lambda induk, n=nama: induk[n])
        nilai = resolver(objek)
        dasar = tipe_dasar(tf)
        if dasar in SKALAR or nilai is None:
            hasil[nama] = nilai
        elif tf.startswith("["):
            hasil[nama] = [jalankan(dasar, x, anak) for x in nilai]
        else:
            hasil[nama] = jalankan(dasar, nilai, anak)
    return hasil


teks = sys.stdin.read()
tok = token(teks)
if tok and tok[0] == "query":
    tok = tok[1:]
    if tok and tok[0] != "{":
        tok = tok[1:]
pilihan, _ = urai(tok, 0)
galat = []
periksa("Query", pilihan, galat)
if galat:
    jawab = {"errors": [{"message": g} for g in galat]}
else:
    jawab = {"data": jalankan("Query", None, pilihan)}
print(json.dumps(jawab, indent=2, ensure_ascii=False))
""",
        "stdin_list": [
            """{ me { name posts { title } } }
""",
            """query Semua {
  users {
    id
    name
    posts { likes }
  }
}
""",
            """{ me { name email posts } }
""",
            """{ users { name { first } } }
""",
        ],
    },
    {
        "title": "Latihan 22: Server JSON-RPC 2.0 dengan Batch",
        "difficulty": "Sulit",
        "question": [
            "Tulis fungsi handle(teks) -> teks atau None yang mematuhi",
            "spesifikasi JSON-RPC 2.0, lalu jalankan untuk setiap baris stdin.",
            "Cetak hasilnya, atau (tanpa respons) kalau handle mengembalikan None.",
            "",
            "Metode terdaftar: tambah(a, b), kurang(a, b), sapa(nama). params",
            "boleh array (urut posisi) atau objek (nama argumen persis).",
            "",
            "Aturan:",
            "  - Bukan JSON sah             -> -32700 Parse error, id null.",
            "  - Bukan objek, jsonrpc bukan \"2.0\", method bukan string, atau",
            "    params bukan array/objek  -> -32600 Invalid Request, id null.",
            "  - Metode tidak ada           -> -32601 Method not found.",
            "  - Jumlah/nama params salah   -> -32602 Invalid params.",
            "  - Tanpa medan id = notifikasi: dijalankan, tapi tidak dijawab,",
            "    termasuk kalau gagal.",
            "  - Array = batch: jawab array berisi respons non-notifikasi",
            "    dengan urutan yang sama; batch kosong -> satu objek -32600;",
            "    batch yang isinya notifikasi semua -> tanpa respons.",
            "  - Urutan kunci respons: jsonrpc, result/error, id. Cetak dengan",
            "    json.dumps bawaan.",
            "",
            "Untuk input {\"jsonrpc\": \"2.0\", \"method\": \"tambah\", \"params\": [2, 3], \"id\": 1}, keluarannya:",
            "{\"jsonrpc\": \"2.0\", \"result\": 5, \"id\": 1}",
            "{\"jsonrpc\": \"2.0\", \"result\": \"Halo, Sari!\", \"id\": \"a\"}",
            "(tanpa respons)",
            "{\"jsonrpc\": \"2.0\", \"error\": {\"code\": -32601, \"message\": \"Method not found\"}, \"id\": 2}",
            "{\"jsonrpc\": \"2.0\", \"error\": {\"code\": -32602, \"message\": \"Invalid params\"}, \"id\": 3}",
            "{\"jsonrpc\": \"2.0\", \"error\": {\"code\": -32700, \"message\": \"Parse error\"}, \"id\": null}",
            "",
            "Untuk input [{\"jsonrpc\": \"2.0\", \"method\": \"tambah\", \"params\": [1, 2], \"id\": \"1\"}, {\"jsonrpc\": \"2.0\", \"method\": \"sapa\", \"params\": [\"Budi\"]}, {\"foo\": \"boo\"}, {\"jsonrpc\": \"2.0\", \"method\": \"kurang\", \"params\": {\"a\": 9, \"b\": 4}, \"id\": \"5\"}], keluarannya:",
            "[{\"jsonrpc\": \"2.0\", \"result\": 3, \"id\": \"1\"}, {\"jsonrpc\": \"2.0\", \"error\": {\"code\": -32600, \"message\": \"Invalid Request\"}, \"id\": null}, {\"jsonrpc\": \"2.0\", \"result\": 5, \"id\": \"5\"}]",
            "{\"jsonrpc\": \"2.0\", \"error\": {\"code\": -32600, \"message\": \"Invalid Request\"}, \"id\": null}",
            "(tanpa respons)",
            "{\"jsonrpc\": \"2.0\", \"error\": {\"code\": -32600, \"message\": \"Invalid Request\"}, \"id\": null}",
        ],
        "hints": [
            "Tulis dulu fungsi yang menangani satu objek permintaan dan mengembalikan dict respons atau None, lalu handle cukup mengurus JSON tidak sah dan batch.",
            "Bedakan notifikasi dengan memeriksa apakah kunci id ada di dict, bukan apakah nilainya None, karena \"id\": null tetap permintaan yang harus dijawab.",
            "Untuk params objek, bandingkan sorted(params) dengan daftar nama argumen yang diharapkan, lalu susun argumennya sesuai urutan daftar itu.",
        ],
        "solution": """import json
import sys


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def sapa(nama):
    return f"Halo, {nama}!"


METODE = {"tambah": tambah, "kurang": kurang, "sapa": sapa}
ARGUMEN = {"tambah": ["a", "b"], "kurang": ["a", "b"], "sapa": ["nama"]}


def galat(kode, pesan, id_=None):
    return {"jsonrpc": "2.0", "error": {"code": kode, "message": pesan},
            "id": id_}


def satu(req):
    if (not isinstance(req, dict) or req.get("jsonrpc") != "2.0"
            or not isinstance(req.get("method"), str)
            or ("params" in req and not isinstance(req["params"], (list, dict)))):
        return galat(-32600, "Invalid Request")
    notifikasi = "id" not in req
    id_ = req.get("id")
    nama = req["method"]
    if nama not in METODE:
        return None if notifikasi else galat(-32601, "Method not found", id_)
    params = req.get("params", [])
    harap = ARGUMEN[nama]
    if isinstance(params, dict):
        if sorted(params) != sorted(harap):
            return None if notifikasi else galat(-32602, "Invalid params", id_)
        args = [params[k] for k in harap]
    else:
        if len(params) != len(harap):
            return None if notifikasi else galat(-32602, "Invalid params", id_)
        args = params
    try:
        hasil = METODE[nama](*args)
    except TypeError:
        return None if notifikasi else galat(-32602, "Invalid params", id_)
    if notifikasi:
        return None
    return {"jsonrpc": "2.0", "result": hasil, "id": id_}


def handle(teks):
    try:
        data = json.loads(teks)
    except json.JSONDecodeError:
        return json.dumps(galat(-32700, "Parse error"))
    if isinstance(data, list):
        if not data:
            return json.dumps(galat(-32600, "Invalid Request"))
        jawab = [r for r in (satu(x) for x in data) if r is not None]
        return json.dumps(jawab) if jawab else None
    r = satu(data)
    return None if r is None else json.dumps(r)


for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    keluar = handle(baris)
    print(keluar if keluar is not None else "(tanpa respons)")
""",
        "stdin_list": [
            """{"jsonrpc": "2.0", "method": "tambah", "params": [2, 3], "id": 1}
{"jsonrpc": "2.0", "method": "sapa", "params": {"nama": "Sari"}, "id": "a"}
{"jsonrpc": "2.0", "method": "tambah", "params": [1, 1]}
{"jsonrpc": "2.0", "method": "kali", "params": [2, 3], "id": 2}
{"jsonrpc": "2.0", "method": "tambah", "params": [1], "id": 3}
{"jsonrpc": "2.0", "method": "tambah", "params": [1, 2
""",
            """[{"jsonrpc": "2.0", "method": "tambah", "params": [1, 2], "id": "1"}, {"jsonrpc": "2.0", "method": "sapa", "params": ["Budi"]}, {"foo": "boo"}, {"jsonrpc": "2.0", "method": "kurang", "params": {"a": 9, "b": 4}, "id": "5"}]
[]
[{"jsonrpc": "2.0", "method": "sapa", "params": ["A"]}, {"jsonrpc": "2.0", "method": "tidakada"}]
{"jsonrpc": "1.0", "method": "tambah", "params": [1, 2], "id": 9}
""",
        ],
    },
    {
        "title": "Latihan 23: Circuit Breaker dengan Jam Palsu",
        "difficulty": "Sulit",
        "question": [
            "Buat kelas circuit breaker yang membungkus layanan palsu. Baris",
            "pertama input berisi konfigurasi ambang=<n> tunggu=<detik>.",
            "Baris berikutnya berbentuk t=<detik> ok atau t=<detik> gagal:",
            "itulah jawaban layanan KALAU dipanggil pada detik itu.",
            "",
            "Aturan:",
            "  - closed: panggil layanan. Sukses mengembalikan hitungan gagal",
            "    ke 0. Gagal menambah hitungan; kalau mencapai ambang, breaker",
            "    jadi open sampai t + tunggu.",
            "  - open dan t < batas: jangan panggil layanan, cetak tolak cepat.",
            "  - open dan t >= batas: half-open, loloskan satu panggilan uji.",
            "    Sukses -> closed (gagal=0). Gagal -> open lagi sampai t + tunggu.",
            "",
            "Format tiap baris keluaran:",
            "  t=<t> panggil -> sukses|gagal | <status>",
            "  t=<t> uji coba (half-open) -> sukses|gagal | <status>",
            "  t=<t> tolak cepat | <status>",
            "dengan <status> = closed gagal=<n> atau open sampai t=<batas>.",
            "Terakhir cetak dipanggil=<n> ditolak=<n>.",
            "",
            "Untuk input ambang=3 tunggu=10, keluarannya:",
            "t=0 panggil -> sukses | closed gagal=0",
            "t=1 panggil -> gagal | closed gagal=1",
            "t=2 panggil -> gagal | closed gagal=2",
            "t=3 panggil -> sukses | closed gagal=0",
            "t=4 panggil -> gagal | closed gagal=1",
            "t=5 panggil -> gagal | closed gagal=2",
            "t=6 panggil -> gagal | open sampai t=16",
            "t=8 tolak cepat | open sampai t=16",
            "t=15 tolak cepat | open sampai t=16",
            "t=16 uji coba (half-open) -> gagal | open sampai t=26",
            "t=20 tolak cepat | open sampai t=26",
            "t=27 uji coba (half-open) -> sukses | closed gagal=0",
            "t=28 panggil -> sukses | closed gagal=0",
            "dipanggil=10 ditolak=3",
        ],
        "hints": [
            "Breaker cuma butuh beberapa keadaan: status, hitungan gagal beruntun, dan detik sampai kapan ia terbuka; jam datang dari input, jadi jangan memanggil time.time().",
            "Saat status open, bandingkan t dengan batasnya: kalau belum lewat, tolak tanpa menyentuh layanan; kalau sudah, tandai panggilan ini sebagai uji coba.",
            "Pada uji coba, satu kegagalan langsung membuka breaker lagi tanpa melihat ambang, sedangkan pada status closed breaker baru terbuka kalau hitungan gagal mencapai ambang.",
        ],
        "solution": "import sys\n\n\nclass Breaker:\n    def __init__(self, ambang, tunggu):\n        self.ambang = ambang\n        self.tunggu = tunggu\n        self.status = \"closed\"\n        self.gagal = 0\n        self.buka_sampai = 0\n        self.dipanggil = 0\n        self.ditolak = 0\n\n    def keterangan(self):\n        if self.status == \"open\":\n            return f\"open sampai t={self.buka_sampai}\"\n        return f\"closed gagal={self.gagal}\"\n\n    def panggil(self, t, hasil_layanan):\n        uji = False\n        if self.status == \"open\":\n            if t < self.buka_sampai:\n                self.ditolak += 1\n                return f\"t={t} tolak cepat | {self.keterangan()}\"\n            uji = True\n        self.dipanggil += 1\n        label = \"uji coba (half-open)\" if uji else \"panggil\"\n        if hasil_layanan == \"ok\":\n            self.status, self.gagal = \"closed\", 0\n            return f\"t={t} {label} -> sukses | {self.keterangan()}\"\n        self.gagal += 1\n        if uji or self.gagal >= self.ambang:\n            self.status = \"open\"\n            self.buka_sampai = t + self.tunggu\n        return f\"t={t} {label} -> gagal | {self.keterangan()}\"\n\n\nbaris = sys.stdin.read().split(\"\\n\")\nkonfig = dict(p.split(\"=\") for p in baris[0].split())\nbreaker = Breaker(int(konfig[\"ambang\"]), int(konfig[\"tunggu\"]))\nfor b in baris[1:]:\n    if not b.strip():\n        continue\n    waktu, hasil = b.split()\n    print(breaker.panggil(int(waktu[2:]), hasil))\nprint(f\"dipanggil={breaker.dipanggil} ditolak={breaker.ditolak}\")\n",
        "stdin_list": [
            """ambang=3 tunggu=10
t=0 ok
t=1 gagal
t=2 gagal
t=3 ok
t=4 gagal
t=5 gagal
t=6 gagal
t=8 ok
t=15 ok
t=16 gagal
t=20 ok
t=27 ok
t=28 ok
""",
            """ambang=1 tunggu=5
t=0 gagal
t=1 ok
t=5 ok
t=6 gagal
t=7 ok
t=11 ok
""",
        ],
    },
    {
        "title": "Latihan 24: API Mini Lengkap: Router, Auth, dan Paginasi",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: bangun API \"tugas\" lengkap sebagai fungsi murni,",
            "tanpa membuka port. Inti programnya app(teks_permintaan, ctx) yang",
            "menerima permintaan HTTP mentah dan mengembalikan respons HTTP",
            "mentah (baris dipisah \\r\\n, header dan body dipisah baris kosong).",
            "",
            "Input: beberapa blok. Tiap blok diawali baris \"@ t=<detik> ip=<ip>\"",
            "(jam dan alamat klien disuntikkan), diikuti permintaan HTTP mentah",
            "sampai blok berikutnya. Data tugas, ember rate limit, dan log",
            "dipakai bersama semua blok dalam satu input.",
            "",
            "Keluaran: untuk tiap blok cetak \">>> \" + baris pertama permintaan,",
            "lalu setiap baris respons diberi awalan \"| \" (spasi di ujung",
            "dibuang, jadi baris kosong tercetak sebagai \"|\"). Di akhir cetak",
            "\"== log ==\" dan satu baris log per permintaan:",
            "t=<t> <ip> <METODE> <path tanpa query> -> <status>.",
            "",
            "Rantai middleware (urut): log -> rate limit -> router + auth.",
            "  - Rate limit: token bucket per ip, kapasitas 5, isi ulang 1 token",
            "    per detik. Kosong -> 429 dengan header Retry-After: 1.",
            "  - Router: cocokkan pola dengan parameter {id:int}. Path cocok",
            "    tapi metode tidak -> 405 dengan header Allow (metode yang ada,",
            "    urut seperti tabel rute, dipisah \", \"). Tak cocok -> 404.",
            "  - Auth: semua rute kecuali POST /login wajib",
            "    Authorization: Bearer <JWT>. Tanpa header -> 401 dengan",
            "    WWW-Authenticate: Bearer. Token salah -> 401 dengan",
            "    WWW-Authenticate: Bearer error=\"invalid_token\", detail salah",
            "    satu dari: token rusak / algoritma tidak diizinkan / tanda",
            "    tangan tidak cocok / token kedaluwarsa (t >= exp).",
            "",
            "JWT HS256 dengan kunci b\"kunci-rahasia-proyek\": header",
            "{\"alg\":\"HS256\",\"typ\":\"JWT\"}, payload {\"sub\":<user>,\"exp\":<t+3600>},",
            "keduanya json.dumps(..., separators=(\",\", \":\")), base64url tanpa",
            "padding. Pengguna: budi dengan sandi rahasia123, disimpan sebagai",
            "pbkdf2_hmac(\"sha256\", sandi, b\"garam-tetap\", 1000).hex().",
            "",
            "Rute:",
            "  POST   /login             -> 200 {\"token\": ...} atau 401",
            "  GET    /tugas             -> 200 daftar berhalaman",
            "  POST   /tugas             -> 201 + header Location: /tugas/<id>",
            "  GET    /tugas/{id:int}    -> 200 atau 404",
            "  PATCH  /tugas/{id:int}    -> 200 (ubah sebagian) atau 404",
            "  DELETE /tugas/{id:int}    -> 204 tanpa body, atau 404",
            "",
            "Validasi body tugas: judul wajib (kecuali PATCH), teks tidak kosong,",
            "paling panjang 60 huruf, disimpan setelah strip(); selesai opsional,",
            "harus boolean, bawaan false. Body bukan JSON -> 400. Validasi",
            "gagal -> 422 dengan anggota tambahan errors: daftar {field, msg}.",
            "Paginasi: page dan per_page bilangan bulat >= 1 (bawaan 1 dan 10,",
            "per_page paling besar 50), selain itu 400. Respons berisi data,",
            "meta (page, per_page, total, total_pages minimal 1), dan links",
            "(next, prev berupa /tugas?page=<p>&per_page=<n> atau null).",
            "",
            "Semua galat memakai application/problem+json (RFC 9457) dengan",
            "type \"about:blank\", title = frasa status, status, dan detail.",
            "Body JSON dicetak dengan json.dumps(obj, ensure_ascii=False) dan",
            "urutan kunci seperti contoh. Header Content-Type ditulis sesudah",
            "baris status bila ada body, lalu header tambahan.",
            "",
            "Untuk input @ t=0 ip=10.0.0.1, keluarannya:",
            ">>> POST /login HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"token\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw\"}",
            ">>> POST /tugas HTTP/1.1",
            "| HTTP/1.1 201 Created",
            "| Content-Type: application/json",
            "| Location: /tugas/1",
            "|",
            "| {\"id\": 1, \"judul\": \"Pasang Nginx\", \"selesai\": false}",
            ">>> POST /tugas HTTP/1.1",
            "| HTTP/1.1 201 Created",
            "| Content-Type: application/json",
            "| Location: /tugas/2",
            "|",
            "| {\"id\": 2, \"judul\": \"Tulis unit systemd\", \"selesai\": false}",
            ">>> POST /tugas HTTP/1.1",
            "| HTTP/1.1 201 Created",
            "| Content-Type: application/json",
            "| Location: /tugas/3",
            "|",
            "| {\"id\": 3, \"judul\": \"Baca Twelve-Factor\", \"selesai\": false}",
            ">>> GET /tugas?page=1&per_page=2 HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [{\"id\": 1, \"judul\": \"Pasang Nginx\", \"selesai\": false}, {\"id\": 2, \"judul\": \"Tulis unit systemd\", \"selesai\": false}], \"meta\": {\"page\": 1, \"per_page\": 2, \"total\": 3, \"total_pages\": 2}, \"links\": {\"next\": \"/tugas?page=2&per_page=2\", \"prev\": null}}",
            ">>> PATCH /tugas/2 HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"id\": 2, \"judul\": \"Tulis unit systemd\", \"selesai\": true}",
            ">>> DELETE /tugas/1 HTTP/1.1",
            "| HTTP/1.1 204 No Content",
            "|",
            ">>> GET /tugas/1 HTTP/1.1",
            "| HTTP/1.1 404 Not Found",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Not Found\", \"status\": 404, \"detail\": \"tugas 1 tidak ada\"}",
            ">>> GET /tugas?page=2&per_page=1 HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [{\"id\": 3, \"judul\": \"Baca Twelve-Factor\", \"selesai\": false}], \"meta\": {\"page\": 2, \"per_page\": 1, \"total\": 2, \"total_pages\": 2}, \"links\": {\"next\": null, \"prev\": \"/tugas?page=1&per_page=1\"}}",
            "== log ==",
            "t=0 10.0.0.1 POST /login -> 200",
            "t=1 10.0.0.1 POST /tugas -> 201",
            "t=2 10.0.0.1 POST /tugas -> 201",
            "t=3 10.0.0.1 POST /tugas -> 201",
            "t=4 10.0.0.1 GET /tugas -> 200",
            "t=5 10.0.0.1 PATCH /tugas/2 -> 200",
            "t=6 10.0.0.1 DELETE /tugas/1 -> 204",
            "t=7 10.0.0.1 GET /tugas/1 -> 404",
            "t=8 10.0.0.1 GET /tugas -> 200",
            "",
            "Untuk input @ t=0 ip=10.0.0.2, keluarannya:",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 401 Unauthorized",
            "| Content-Type: application/problem+json",
            "| WWW-Authenticate: Bearer",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unauthorized\", \"status\": 401, \"detail\": \"butuh header Authorization: Bearer <token>\"}",
            ">>> POST /login HTTP/1.1",
            "| HTTP/1.1 401 Unauthorized",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unauthorized\", \"status\": 401, \"detail\": \"username atau password salah\"}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 401 Unauthorized",
            "| Content-Type: application/problem+json",
            "| WWW-Authenticate: Bearer error=\"invalid_token\"",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unauthorized\", \"status\": 401, \"detail\": \"tanda tangan tidak cocok\"}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 401 Unauthorized",
            "| Content-Type: application/problem+json",
            "| WWW-Authenticate: Bearer error=\"invalid_token\"",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unauthorized\", \"status\": 401, \"detail\": \"algoritma tidak diizinkan\"}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 401 Unauthorized",
            "| Content-Type: application/problem+json",
            "| WWW-Authenticate: Bearer error=\"invalid_token\"",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unauthorized\", \"status\": 401, \"detail\": \"token kedaluwarsa\"}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            "== log ==",
            "t=0 10.0.0.2 GET /tugas -> 401",
            "t=1 10.0.0.2 POST /login -> 401",
            "t=2 10.0.0.2 GET /tugas -> 401",
            "t=3 10.0.0.2 GET /tugas -> 401",
            "t=3600 10.0.0.2 GET /tugas -> 401",
            "t=3601 10.0.0.2 GET /tugas -> 200",
            "",
            "Untuk input @ t=0 ip=10.0.0.3, keluarannya:",
            ">>> POST /tugas HTTP/1.1",
            "| HTTP/1.1 400 Bad Request",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Bad Request\", \"status\": 400, \"detail\": \"body bukan JSON yang sah\"}",
            ">>> POST /tugas HTTP/1.1",
            "| HTTP/1.1 422 Unprocessable Content",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unprocessable Content\", \"status\": 422, \"detail\": \"data tugas tidak valid\", \"errors\": [{\"field\": \"judul\", \"msg\": \"wajib diisi\"}, {\"field\": \"selesai\", \"msg\": \"harus true atau false\"}]}",
            ">>> POST /tugas HTTP/1.1",
            "| HTTP/1.1 422 Unprocessable Content",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Unprocessable Content\", \"status\": 422, \"detail\": \"data tugas tidak valid\", \"errors\": [{\"field\": \"judul\", \"msg\": \"paling panjang 60 huruf\"}, {\"field\": \"selesai\", \"msg\": \"harus true atau false\"}]}",
            ">>> PUT /tugas/1 HTTP/1.1",
            "| HTTP/1.1 405 Method Not Allowed",
            "| Content-Type: application/problem+json",
            "| Allow: GET, PATCH, DELETE",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Method Not Allowed\", \"status\": 405, \"detail\": \"metode PUT tidak didukung di /tugas/1\"}",
            ">>> GET /laporan HTTP/1.1",
            "| HTTP/1.1 404 Not Found",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Not Found\", \"status\": 404, \"detail\": \"tidak ada rute untuk /laporan\"}",
            ">>> GET /tugas?page=0 HTTP/1.1",
            "| HTTP/1.1 400 Bad Request",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Bad Request\", \"status\": 400, \"detail\": \"page dan per_page harus bilangan bulat 1..50\"}",
            ">>> GET /tugas/abc HTTP/1.1",
            "| HTTP/1.1 404 Not Found",
            "| Content-Type: application/problem+json",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Not Found\", \"status\": 404, \"detail\": \"tidak ada rute untuk /tugas/abc\"}",
            "== log ==",
            "t=0 10.0.0.3 POST /tugas -> 400",
            "t=1 10.0.0.3 POST /tugas -> 422",
            "t=2 10.0.0.3 POST /tugas -> 422",
            "t=3 10.0.0.3 PUT /tugas/1 -> 405",
            "t=4 10.0.0.3 GET /laporan -> 404",
            "t=5 10.0.0.3 GET /tugas -> 400",
            "t=6 10.0.0.3 GET /tugas/abc -> 404",
            "",
            "Untuk input @ t=0 ip=10.0.0.4, keluarannya:",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 429 Too Many Requests",
            "| Content-Type: application/problem+json",
            "| Retry-After: 1",
            "|",
            "| {\"type\": \"about:blank\", \"title\": \"Too Many Requests\", \"status\": 429, \"detail\": \"terlalu banyak permintaan, tunggu sebentar\"}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            ">>> GET /tugas HTTP/1.1",
            "| HTTP/1.1 200 OK",
            "| Content-Type: application/json",
            "|",
            "| {\"data\": [], \"meta\": {\"page\": 1, \"per_page\": 10, \"total\": 0, \"total_pages\": 1}, \"links\": {\"next\": null, \"prev\": null}}",
            "== log ==",
            "t=0 10.0.0.4 GET /tugas -> 200",
            "t=0 10.0.0.4 GET /tugas -> 200",
            "t=0 10.0.0.4 GET /tugas -> 200",
            "t=0 10.0.0.4 GET /tugas -> 200",
            "t=0 10.0.0.4 GET /tugas -> 200",
            "t=0 10.0.0.4 GET /tugas -> 429",
            "t=0 10.0.0.5 GET /tugas -> 200",
            "t=2 10.0.0.4 GET /tugas -> 200",
        ],
        "hints": [
            "Pecah pekerjaan jadi lapisan yang bisa diuji sendiri-sendiri: pengurai teks HTTP, penulis respons, router, middleware, dan handler per rute, persis seperti bab 1 sampai 12 membangunnya satu per satu.",
            "Buat middleware berbentuk fungsi (req, ctx, lanjut) dan rangkai dengan fungsi rekursif yang memanggil middleware ke-i dengan lanjut yang menunjuk middleware ke-i+1, sehingga log tetap mencatat status 429 dari rate limit.",
            "Untuk JWT, verifikasi berurutan: pecah tiga bagian, tolak alg selain HS256, bandingkan tanda tangan dengan hmac.compare_digest, baru periksa exp terhadap jam dari ctx.",
            "Respons cukup dict berisi status, body, header tambahan, dan jenis konten; satu fungsi masalah(status, detail, **tambahan) membuat semua galat RFC 9457 sekaligus.",
        ],
        "solution": "import base64\nimport hashlib\nimport hmac\nimport json\nimport sys\n\nKUNCI_JWT = b\"kunci-rahasia-proyek\"\nGARAM = b\"garam-tetap\"\nPENGGUNA = {\"budi\": hashlib.pbkdf2_hmac(\"sha256\", b\"rahasia123\", GARAM, 1000).hex()}\nKAPASITAS, MAKS_JUDUL, MAKS_PER_PAGE = 5, 60, 50\nALASAN = {200: \"OK\", 201: \"Created\", 204: \"No Content\", 400: \"Bad Request\",\n          401: \"Unauthorized\", 404: \"Not Found\", 405: \"Method Not Allowed\",\n          422: \"Unprocessable Content\", 429: \"Too Many Requests\"}\n\n\ndef b64(data):\n    return base64.urlsafe_b64encode(data).rstrip(b\"=\").decode()\n\n\ndef unb64(teks):\n    return base64.urlsafe_b64decode(teks + \"=\" * (-len(teks) % 4))\n\n\ndef kompak(obj):\n    return json.dumps(obj, separators=(\",\", \":\"))\n\n\ndef buat_jwt(sub, sekarang):\n    kepala = b64(kompak({\"alg\": \"HS256\", \"typ\": \"JWT\"}).encode())\n    isi = b64(kompak({\"sub\": sub, \"exp\": sekarang + 3600}).encode())\n    tanda = hmac.new(KUNCI_JWT, f\"{kepala}.{isi}\".encode(), \"sha256\").digest()\n    return f\"{kepala}.{isi}.{b64(tanda)}\"\n\n\ndef cek_jwt(token, sekarang):\n    try:\n        kepala, isi, tanda = token.split(\".\")\n        h = json.loads(unb64(kepala))\n        p = json.loads(unb64(isi))\n    except ValueError:\n        return None, \"token rusak\"\n    if h.get(\"alg\") != \"HS256\":\n        return None, \"algoritma tidak diizinkan\"\n    harap = hmac.new(KUNCI_JWT, f\"{kepala}.{isi}\".encode(), \"sha256\").digest()\n    if not hmac.compare_digest(b64(harap), tanda):\n        return None, \"tanda tangan tidak cocok\"\n    if sekarang >= p.get(\"exp\", 0):\n        return None, \"token kedaluwarsa\"\n    return p[\"sub\"], None\n\n\ndef respons(status, body=None, header=None, jenis=\"application/json\"):\n    return {\"status\": status, \"body\": body, \"header\": header or {}, \"jenis\": jenis}\n\n\ndef masalah(status, detail, **tambahan):\n    body = {\"type\": \"about:blank\", \"title\": ALASAN[status], \"status\": status,\n            \"detail\": detail}\n    body.update(tambahan)\n    return respons(status, body, jenis=\"application/problem+json\")\n\n\n# ------------------------------------------------------------------ handler\n\ndef h_login(req, ctx, param):\n    try:\n        data = json.loads(req[\"body\"] or \"\")\n    except ValueError:\n        return masalah(400, \"body bukan JSON yang sah\")\n    nama, sandi = data.get(\"username\"), data.get(\"password\")\n    simpan = PENGGUNA.get(nama)\n    hitung = hashlib.pbkdf2_hmac(\"sha256\", str(sandi).encode(), GARAM, 1000).hex()\n    if simpan is None or not hmac.compare_digest(simpan, hitung):\n        return masalah(401, \"username atau password salah\")\n    return respons(200, {\"token\": buat_jwt(nama, ctx[\"now\"])})\n\n\ndef validasi(data, sebagian):\n    galat = []\n    if not isinstance(data, dict):\n        return [{\"field\": \"/\", \"msg\": \"harus objek JSON\"}]\n    if \"judul\" in data:\n        j = data[\"judul\"]\n        if not isinstance(j, str) or not j.strip():\n            galat.append({\"field\": \"judul\", \"msg\": \"harus teks yang tidak kosong\"})\n        elif len(j) > MAKS_JUDUL:\n            galat.append({\"field\": \"judul\", \"msg\": f\"paling panjang {MAKS_JUDUL} huruf\"})\n    elif not sebagian:\n        galat.append({\"field\": \"judul\", \"msg\": \"wajib diisi\"})\n    if \"selesai\" in data and not isinstance(data[\"selesai\"], bool):\n        galat.append({\"field\": \"selesai\", \"msg\": \"harus true atau false\"})\n    return galat\n\n\ndef baca_json(req):\n    try:\n        return json.loads(req[\"body\"] or \"\"), None\n    except ValueError:\n        return None, masalah(400, \"body bukan JSON yang sah\")\n\n\ndef h_buat(req, ctx, param):\n    data, salah = baca_json(req)\n    if salah:\n        return salah\n    galat = validasi(data, sebagian=False)\n    if galat:\n        return masalah(422, \"data tugas tidak valid\", errors=galat)\n    db = ctx[\"db\"]\n    db[\"urut\"] += 1\n    tugas = {\"id\": db[\"urut\"], \"judul\": data[\"judul\"].strip(),\n             \"selesai\": data.get(\"selesai\", False)}\n    db[\"tugas\"][tugas[\"id\"]] = tugas\n    return respons(201, tugas, {\"Location\": f\"/tugas/{tugas['id']}\"})\n\n\ndef angka_query(query, nama, bawaan):\n    if nama not in query:\n        return bawaan\n    teks = query[nama]\n    return int(teks) if teks.isdigit() and int(teks) >= 1 else None\n\n\ndef h_daftar(req, ctx, param):\n    page = angka_query(req[\"query\"], \"page\", 1)\n    per_page = angka_query(req[\"query\"], \"per_page\", 10)\n    if page is None or per_page is None or per_page > MAKS_PER_PAGE:\n        return masalah(400, f\"page dan per_page harus bilangan bulat 1..{MAKS_PER_PAGE}\")\n    semua = [ctx[\"db\"][\"tugas\"][k] for k in sorted(ctx[\"db\"][\"tugas\"])]\n    total = len(semua)\n    halaman = max(1, -(-total // per_page))\n    data = semua[(page - 1) * per_page: page * per_page]\n\n    def tautan(p):\n        return f\"/tugas?page={p}&per_page={per_page}\"\n\n    return respons(200, {\n        \"data\": data,\n        \"meta\": {\"page\": page, \"per_page\": per_page, \"total\": total,\n                 \"total_pages\": halaman},\n        \"links\": {\"next\": tautan(page + 1) if page < halaman else None,\n                  \"prev\": tautan(page - 1) if 1 < page <= halaman else None},\n    })\n\n\ndef ambil(ctx, param):\n    return ctx[\"db\"][\"tugas\"].get(int(param[\"id\"]))\n\n\ndef h_satu(req, ctx, param):\n    tugas = ambil(ctx, param)\n    if tugas is None:\n        return masalah(404, f\"tugas {param['id']} tidak ada\")\n    return respons(200, tugas)\n\n\ndef h_ubah(req, ctx, param):\n    tugas = ambil(ctx, param)\n    if tugas is None:\n        return masalah(404, f\"tugas {param['id']} tidak ada\")\n    data, salah = baca_json(req)\n    if salah:\n        return salah\n    galat = validasi(data, sebagian=True)\n    if galat:\n        return masalah(422, \"data tugas tidak valid\", errors=galat)\n    if \"judul\" in data:\n        tugas[\"judul\"] = data[\"judul\"].strip()\n    if \"selesai\" in data:\n        tugas[\"selesai\"] = data[\"selesai\"]\n    return respons(200, tugas)\n\n\ndef h_hapus(req, ctx, param):\n    if ambil(ctx, param) is None:\n        return masalah(404, f\"tugas {param['id']} tidak ada\")\n    del ctx[\"db\"][\"tugas\"][int(param[\"id\"])]\n    return respons(204)\n\n\nRUTE = [\n    (\"POST\", \"/login\", h_login, False),\n    (\"GET\", \"/tugas\", h_daftar, True),\n    (\"POST\", \"/tugas\", h_buat, True),\n    (\"GET\", \"/tugas/{id:int}\", h_satu, True),\n    (\"PATCH\", \"/tugas/{id:int}\", h_ubah, True),\n    (\"DELETE\", \"/tugas/{id:int}\", h_hapus, True),\n]\n\n\ndef cocok(pola, path):\n    a, b = pola.strip(\"/\").split(\"/\"), path.strip(\"/\").split(\"/\")\n    if len(a) != len(b):\n        return None\n    param = {}\n    for x, y in zip(a, b):\n        if x.startswith(\"{\"):\n            nama, _, jenis = x[1:-1].partition(\":\")\n            if jenis == \"int\" and not y.isdigit():\n                return None\n            param[nama] = y\n        elif x != y:\n            return None\n    return param\n\n\ndef cari_rute(metode, path):\n    izin = []\n    for m, pola, handler, butuh_auth in RUTE:\n        param = cocok(pola, path)\n        if param is None:\n            continue\n        if m == metode:\n            return handler, param, butuh_auth, None\n        izin.append(m)\n    return None, None, None, izin\n\n\n# --------------------------------------------------------------- middleware\n\ndef mw_log(req, ctx, lanjut):\n    hasil = lanjut(req, ctx)\n    ctx[\"log\"].append(f\"t={ctx['now']} {ctx['ip']} {req['method']} {req['path']} \"\n                      f\"-> {hasil['status']}\")\n    return hasil\n\n\ndef mw_rate_limit(req, ctx, lanjut):\n    ember = ctx[\"ember\"].setdefault(ctx[\"ip\"], [KAPASITAS, ctx[\"now\"]])\n    ember[0] = min(KAPASITAS, ember[0] + (ctx[\"now\"] - ember[1]))\n    ember[1] = ctx[\"now\"]\n    if ember[0] < 1:\n        hasil = masalah(429, \"terlalu banyak permintaan, tunggu sebentar\")\n        hasil[\"header\"][\"Retry-After\"] = \"1\"\n        return hasil\n    ember[0] -= 1\n    return lanjut(req, ctx)\n\n\ndef mw_auth_dan_rute(req, ctx, lanjut):\n    handler, param, butuh_auth, izin = cari_rute(req[\"method\"], req[\"path\"])\n    if handler is None:\n        if izin:\n            hasil = masalah(405, f\"metode {req['method']} tidak didukung di {req['path']}\")\n            hasil[\"header\"][\"Allow\"] = \", \".join(izin)\n            return hasil\n        return masalah(404, f\"tidak ada rute untuk {req['path']}\")\n    if butuh_auth:\n        auth = req[\"header\"].get(\"authorization\", \"\")\n        if not auth.startswith(\"Bearer \"):\n            hasil = masalah(401, \"butuh header Authorization: Bearer <token>\")\n            hasil[\"header\"][\"WWW-Authenticate\"] = \"Bearer\"\n            return hasil\n        sub, alasan = cek_jwt(auth[7:], ctx[\"now\"])\n        if sub is None:\n            hasil = masalah(401, alasan)\n            hasil[\"header\"][\"WWW-Authenticate\"] = 'Bearer error=\"invalid_token\"'\n            return hasil\n        ctx[\"user\"] = sub\n    return handler(req, ctx, param)\n\n\nRANTAI = [mw_log, mw_rate_limit, mw_auth_dan_rute]\n\n\ndef jalankan_rantai(req, ctx, i=0):\n    if i == len(RANTAI):\n        return masalah(404, \"akhir rantai\")\n    return RANTAI[i](req, ctx, lambda r, c: jalankan_rantai(r, c, i + 1))\n\n\n# ---------------------------------------------------------------- HTTP teks\n\ndef urai_permintaan(teks):\n    kepala, _, body = teks.partition(\"\\n\\n\")\n    baris = kepala.split(\"\\n\")\n    metode, target, _ = baris[0].split(\" \")\n    path, _, qs = target.partition(\"?\")\n    query = dict(p.split(\"=\", 1) for p in qs.split(\"&\") if \"=\" in p)\n    header = {}\n    for b in baris[1:]:\n        nama, _, nilai = b.partition(\":\")\n        header[nama.strip().lower()] = nilai.strip()\n    return {\"method\": metode, \"path\": path, \"query\": query, \"header\": header,\n            \"body\": body.strip()}\n\n\ndef tulis_respons(hasil):\n    baris = [f\"HTTP/1.1 {hasil['status']} {ALASAN[hasil['status']]}\"]\n    if hasil[\"body\"] is not None:\n        baris.append(f\"Content-Type: {hasil['jenis']}\")\n    for nama, nilai in hasil[\"header\"].items():\n        baris.append(f\"{nama}: {nilai}\")\n    baris.append(\"\")\n    if hasil[\"body\"] is not None:\n        baris.append(json.dumps(hasil[\"body\"], ensure_ascii=False))\n    return \"\\r\\n\".join(baris)\n\n\ndef app(teks_permintaan, ctx):\n    return tulis_respons(jalankan_rantai(urai_permintaan(teks_permintaan), ctx))\n\n\ndef main():\n    db = {\"urut\": 0, \"tugas\": {}}\n    bersama = {\"db\": db, \"ember\": {}, \"log\": []}\n    blok = []\n    for baris in sys.stdin.read().split(\"\\n\"):\n        if baris.startswith(\"@\"):\n            blok.append([baris, []])\n        elif blok:\n            blok[-1][1].append(baris)\n    for kepala, isi in blok:\n        medan = dict(p.split(\"=\", 1) for p in kepala[1:].split())\n        ctx = dict(bersama, now=int(medan[\"t\"]), ip=medan[\"ip\"], user=None)\n        teks = \"\\n\".join(isi).strip(\"\\n\")\n        print(\">>> \" + teks.split(\"\\n\")[0])\n        for b in app(teks, ctx).split(\"\\r\\n\"):\n            print((\"| \" + b).rstrip())\n    print(\"== log ==\")\n    for b in bersama[\"log\"]:\n        print(b)\n\n\nmain()\n",
        "stdin_list": [
            """@ t=0 ip=10.0.0.1
POST /login HTTP/1.1
Host: api.tugas.example
Content-Type: application/json

{"username": "budi", "password": "rahasia123"}
@ t=1 ip=10.0.0.1
POST /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"judul": "Pasang Nginx"}
@ t=2 ip=10.0.0.1
POST /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"judul": "Tulis unit systemd", "selesai": false}
@ t=3 ip=10.0.0.1
POST /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"judul": "Baca Twelve-Factor"}
@ t=4 ip=10.0.0.1
GET /tugas?page=1&per_page=2 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=5 ip=10.0.0.1
PATCH /tugas/2 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"selesai": true}
@ t=6 ip=10.0.0.1
DELETE /tugas/1 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=7 ip=10.0.0.1
GET /tugas/1 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=8 ip=10.0.0.1
GET /tugas?page=2&per_page=1 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
""",
            """@ t=0 ip=10.0.0.2
GET /tugas HTTP/1.1
Host: api.tugas.example
@ t=1 ip=10.0.0.2
POST /login HTTP/1.1
Host: api.tugas.example
Content-Type: application/json

{"username": "budi", "password": "salah"}
@ t=2 ip=10.0.0.2
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHAA
@ t=3 ip=10.0.0.2
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.
@ t=3600 ip=10.0.0.2
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=3601 ip=10.0.0.2
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjo2NjAwfQ.qW2wRoyZ0apZ6B9Y6XzlyyEZZPOLhtA1qA3p-yj9Kkw
""",
            """@ t=0 ip=10.0.0.3
POST /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"judul": "lupa kutip}
@ t=1 ip=10.0.0.3
POST /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"selesai": "belum"}
@ t=2 ip=10.0.0.3
POST /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"judul": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "selesai": 1}
@ t=3 ip=10.0.0.3
PUT /tugas/1 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
Content-Type: application/json

{"judul": "a"}
@ t=4 ip=10.0.0.3
GET /laporan HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=5 ip=10.0.0.3
GET /tugas?page=0 HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=6 ip=10.0.0.3
GET /tugas/abc HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
""",
            """@ t=0 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=0 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=0 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=0 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=0 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=0 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=0 ip=10.0.0.5
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
@ t=2 ip=10.0.0.4
GET /tugas HTTP/1.1
Host: api.tugas.example
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWRpIiwiZXhwIjozNjAwfQ.UtjYECbyWmhcoKg2FrWYdGJMCJafh8EUIGsnBVIpHRw
""",
        ],
    },
]
