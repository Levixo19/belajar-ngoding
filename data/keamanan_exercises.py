"""Kurikulum Keamanan Siber.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

KEAMANAN_EXERCISES = [
    {
        "title": "Latihan 1: Validasi Masukan dengan Daftar Putih",
        "difficulty": "Mudah",
        "question": [
            "Formulir pendaftaran mengirim data ke servermu, satu baris per",
            "isian, berbentuk jenis:nilai. Validasi tiap baris dengan daftar",
            "putih. Aturannya (spasi di sekitar jenis dan nilai dibuang dulu):",
            "",
            "  username  huruf kecil, angka, garis bawah; diawali huruf;",
            "            panjang 3-16",
            "  email     huruf kecil/angka/. _ + - lalu @ lalu domain yang",
            "            punya minimal satu titik, contoh ani@contoh.id",
            "  kodepos   tepat 5 angka, angka pertama bukan 0",
            "  umur      1-3 angka, nilainya 13 sampai 120",
            "",
            "Periksa berurutan dan cetak alasan pertama yang gagal:",
            "  1. Baris tanpa titik dua: DITOLAK <baris>: format harus jenis:nilai",
            "  2. Jenis lain: DITOLAK <jenis>: jenis tidak dikenal",
            "  3. Nilai lebih dari 64 karakter: DITOLAK <jenis>: lebih dari 64 karakter",
            "  4. Pola tidak cocok penuh: DITOLAK <jenis> <nilai>: pola tidak cocok",
            "  5. Umur di luar rentang: DITOLAK umur <nilai>: di luar rentang 13-120",
            "  6. Lolos semua: DITERIMA <jenis> <nilai>",
            "Baris kosong dilewati.",
            "",
            "Contoh masukan:",
            "  username:budi_01",
            "  username:Budi",
            "  username:ab",
            "  email:ani.s@sekolah.sch.id",
            "  email:ani@@contoh.id",
            "  kodepos:60111",
            "  kodepos:6011a",
            "  umur:17",
            "  umur:7",
            "  alamat:Jl. Mawar 3",
            "  tanpa titik dua",
            "",
            "Keluaran yang diharapkan (untuk contoh masukan di atas):",
            "DITERIMA username budi_01",
            "DITOLAK username Budi: pola tidak cocok",
            "DITOLAK username ab: pola tidak cocok",
            "DITERIMA email ani.s@sekolah.sch.id",
            "DITOLAK email ani@@contoh.id: pola tidak cocok",
            "DITERIMA kodepos 60111",
            "DITOLAK kodepos 6011a: pola tidak cocok",
            "DITERIMA umur 17",
            "DITOLAK umur 7: di luar rentang 13-120",
            "DITOLAK alamat: jenis tidak dikenal",
            "DITOLAK tanpa titik dua: format harus jenis:nilai",
        ],
        "hints": [
            "Tulis satu pola regex untuk tiap jenis di sebuah dict, supaya aturan tambahan cukup jadi satu baris baru.",
            "Pisahkan baris dengan str.partition(\":\"), lalu cek pemisahnya kosong atau tidak untuk mengenali baris tanpa titik dua.",
            "Pakai pola.fullmatch(nilai), bukan match, supaya sisa teks di belakang nilai ikut membuat pola gagal.",
            "Rentang umur dicek sesudah polanya cocok, dengan 13 <= int(nilai) <= 120.",
        ],
        "solution": "import re\nimport sys\n\nATURAN = {\n    \"username\": re.compile(r\"[a-z][a-z0-9_]{2,15}\"),\n    \"email\": re.compile(r\"[a-z0-9._+-]+@[a-z0-9-]+(\\.[a-z0-9-]+)+\"),\n    \"kodepos\": re.compile(r\"[1-9][0-9]{4}\"),\n    \"umur\": re.compile(r\"[0-9]{1,3}\"),\n}\n\nfor baris in sys.stdin.read().splitlines():\n    baris = baris.strip()\n    if not baris:\n        continue\n    jenis, pemisah, nilai = baris.partition(\":\")\n    jenis, nilai = jenis.strip(), nilai.strip()\n    if not pemisah:\n        print(f\"DITOLAK {baris}: format harus jenis:nilai\")\n    elif jenis not in ATURAN:\n        print(f\"DITOLAK {jenis}: jenis tidak dikenal\")\n    elif len(nilai) > 64:\n        print(f\"DITOLAK {jenis}: lebih dari 64 karakter\")\n    elif not ATURAN[jenis].fullmatch(nilai):\n        print(f\"DITOLAK {jenis} {nilai}: pola tidak cocok\")\n    elif jenis == \"umur\" and not 13 <= int(nilai) <= 120:\n        print(f\"DITOLAK umur {nilai}: di luar rentang 13-120\")\n    else:\n        print(f\"DITERIMA {jenis} {nilai}\")\n",
        "stdin_list": [
            """username:budi_01
username:Budi
username:ab
email:ani.s@sekolah.sch.id
email:ani@@contoh.id
kodepos:60111
kodepos:6011a
umur:17
umur:7
alamat:Jl. Mawar 3
tanpa titik dua
""",
            """username:cici_dev
email:cici+tugas@contoh.id
umur:130
kodepos:01234
username:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
""",
        ],
    },
    {
        "title": "Latihan 2: Daftar Ancaman STRIDE dari Diagram Alir",
        "difficulty": "Mudah",
        "question": [
            "Tiap baris masukan adalah satu benda di diagram alir data,",
            "berbentuk nama|jenis|lintas. Jenisnya entitas, proses,",
            "penyimpanan, atau aliran. Kolom lintas cuma berarti untuk",
            "aliran: ya kalau aliran itu menyeberangi batas kepercayaan.",
            "",
            "Pakai tabel aturan STRIDE per jenis ini:",
            "  entitas      S R",
            "  proses       S T R I D E",
            "  penyimpanan  T I D",
            "  aliran       T I D  (hanya kalau lintas = ya)",
            "",
            "Nama lengkap tiap huruf: S Spoofing, T Tampering,",
            "R Repudiation, I Information disclosure, D Denial of service,",
            "E Elevation of privilege.",
            "",
            "Untuk tiap baris cetak nama [jenis]: daftar nama ancaman",
            "dipisah koma, urut seperti tabel. Aliran yang tidak lintas",
            "batas dicetak nama [aliran]: di dalam batas kepercayaan,",
            "prioritas rendah, dan tidak dihitung. Terakhir cetak jumlah",
            "per huruf dan totalnya.",
            "",
            "Contoh masukan:",
            "  Pembeli|entitas|-",
            "  Aplikasi web|proses|-",
            "  Database pesanan|penyimpanan|-",
            "  Pembeli ke aplikasi|aliran|ya",
            "  Aplikasi ke database|aliran|tidak",
            "",
            "Keluaran yang diharapkan (untuk contoh masukan di atas):",
            "Pembeli [entitas]: Spoofing, Repudiation",
            "Aplikasi web [proses]: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege",
            "Database pesanan [penyimpanan]: Tampering, Information disclosure, Denial of service",
            "Pembeli ke aplikasi [aliran]: Tampering, Information disclosure, Denial of service",
            "Aplikasi ke database [aliran]: di dalam batas kepercayaan, prioritas rendah",
            "Ringkasan: S=2 T=3 R=2 I=3 D=3 E=1",
            "Total ancaman: 14",
        ],
        "hints": [
            "Simpan aturan sebagai dict dari jenis ke deretan huruf, misalnya proses menjadi teks \"STRIDE\", supaya bisa diulang huruf demi huruf.",
            "Siapkan penghitung untuk keenam huruf sejak awal, supaya huruf yang nol tetap muncul di ringkasan dengan urutan S T R I D E.",
            "Pecah baris dengan split(\"|\") dan lewati aliran yang kolom lintasnya bukan ya sebelum menambah penghitung.",
        ],
        "solution": """import sys

ATURAN = {
    "entitas": "SR",
    "proses": "STRIDE",
    "penyimpanan": "TID",
    "aliran": "TID",
}
NAMA = {
    "S": "Spoofing",
    "T": "Tampering",
    "R": "Repudiation",
    "I": "Information disclosure",
    "D": "Denial of service",
    "E": "Elevation of privilege",
}

hitung = {huruf: 0 for huruf in "STRIDE"}
for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    nama, jenis, lintas = [bagian.strip() for bagian in baris.split("|")]
    if jenis == "aliran" and lintas != "ya":
        print(f"{nama} [{jenis}]: di dalam batas kepercayaan, prioritas rendah")
        continue
    huruf_huruf = ATURAN[jenis]
    for huruf in huruf_huruf:
        hitung[huruf] += 1
    daftar = ", ".join(NAMA[h] for h in huruf_huruf)
    print(f"{nama} [{jenis}]: {daftar}")

ringkas = " ".join(f"{h}={n}" for h, n in hitung.items())
print(f"Ringkasan: {ringkas}")
print(f"Total ancaman: {sum(hitung.values())}")
""",
        "stdin_list": [
            """Pembeli|entitas|-
Aplikasi web|proses|-
Database pesanan|penyimpanan|-
Pembeli ke aplikasi|aliran|ya
Aplikasi ke database|aliran|tidak
""",
            """Kurir|entitas|-
Layanan ongkir|proses|-
API ekspedisi|entitas|-
Ongkir ke ekspedisi|aliran|ya
Log transaksi|penyimpanan|-
Layanan ke log|aliran|tidak
""",
        ],
    },
    {
        "title": "Latihan 3: Pemeriksa Integritas Berkas SHA-256",
        "difficulty": "Mudah",
        "question": [
            "Kamu menyimpan manifest berisi sidik SHA-256 semua berkas di",
            "server. Sekarang bandingkan keadaan berkas hari ini dengan",
            "manifest itu.",
            "",
            "Masukan punya dua bagian. Bagian [berkas] berisi nama|isi",
            "untuk berkas yang ada sekarang (hitung SHA-256 dari isinya,",
            "encode UTF-8). Bagian [manifest] berisi nama|sidik yang",
            "dicatat dulu. Sidik di manifest bisa ditulis huruf besar.",
            "",
            "Untuk tiap nama dari kedua bagian, urut alfabetis, cetak",
            "nama: STATUS dengan aturan:",
            "  OK       ada di keduanya dan sidiknya sama",
            "  BERUBAH  ada di keduanya tapi sidiknya beda",
            "  HILANG   ada di manifest, tidak ada di berkas",
            "  BARU     ada di berkas, tidak ada di manifest",
            "Terakhir cetak ringkasan jumlah tiap status dengan urutan",
            "OK, BERUBAH, HILANG, BARU. Bandingkan sidik dengan",
            "hmac.compare_digest.",
            "",
            "Contoh masukan (sidik dipotong di sini supaya muat; masukan",
            "aslinya berisi 64 karakter):",
            "  [berkas]",
            "  laporan.txt|isi laporan bulan oktober",
            "  logo.svg|logo toko versi 3",
            "  .env|APP_DEBUG=true",
            "  catatan.txt|rapat jumat jam 9",
            "  [manifest]",
            "  laporan.txt|8a56ef1024a5a4c2...",
            "  logo.svg|037130a40743715c...",
            "  .env|7e2faf775f552faf...",
            "  harga.csv|c4e27132c6721586...",
            "",
            "Keluaran yang diharapkan:",
            ".env: BERUBAH",
            "catatan.txt: BARU",
            "harga.csv: HILANG",
            "laporan.txt: OK",
            "logo.svg: OK",
            "Ringkasan: 2 OK, 1 BERUBAH, 1 HILANG, 1 BARU",
        ],
        "hints": [
            "Simpan kedua bagian di dua dict terpisah, lalu gabungkan nama-namanya dengan operasi himpunan supaya tidak ada yang terlewat.",
            "Hitung sidik bagian berkas dengan hashlib.sha256(isi.encode(\"utf-8\")).hexdigest(), dan ubah sidik manifest ke huruf kecil.",
            "Cek dulu apakah nama hilang dari salah satu dict, baru bandingkan sidiknya dengan hmac.compare_digest.",
        ],
        "solution": """import hashlib
import hmac
import sys

berkas, manifest = {}, {}
bagian = None
for baris in sys.stdin.read().splitlines():
    baris = baris.strip()
    if not baris:
        continue
    if baris in ("[berkas]", "[manifest]"):
        bagian = baris
        continue
    nama, _, nilai = baris.partition("|")
    if bagian == "[berkas]":
        berkas[nama] = hashlib.sha256(nilai.encode("utf-8")).hexdigest()
    else:
        manifest[nama] = nilai.lower()

hitung = {"OK": 0, "BERUBAH": 0, "HILANG": 0, "BARU": 0}
for nama in sorted(set(berkas) | set(manifest)):
    if nama not in berkas:
        status = "HILANG"
    elif nama not in manifest:
        status = "BARU"
    elif hmac.compare_digest(berkas[nama], manifest[nama]):
        status = "OK"
    else:
        status = "BERUBAH"
    hitung[status] += 1
    print(f"{nama}: {status}")

print("Ringkasan: " + ", ".join(f"{n} {s}" for s, n in hitung.items()))
""",
        "stdin_list": [
            """[berkas]
laporan.txt|isi laporan bulan oktober
logo.svg|logo toko versi 3
.env|APP_DEBUG=true
catatan.txt|rapat jumat jam 9
[manifest]
laporan.txt|8a56ef1024a5a4c2fbf30c8290379ebbc8f27b3d40d39afc3e5fceaf321c9a31
logo.svg|037130a40743715c82854cbda9a42daf8639a798e0270711fe605d78627f21f3
.env|7e2faf775f552faf20c42886a1725eb1b78ffc853baf3b9db3cf9f4ee1ad93ac
harga.csv|c4e27132c67215861b2452bbf9d4402fcaf8dff069333e56b8eb79c5bb74843d
""",
            """[berkas]
laporan.txt|laporan bulan oktober (revisi)
logo.svg|logo toko versi 3
[manifest]
logo.svg|037130A40743715C82854CBDA9A42DAF8639A798E0270711FE605D78627F21F3
laporan.txt|0a63af16dd517f9d2a0bcc92964e205cc0008625a24f87cd9c9a7ba0878be036
""",
        ],
    },
    {
        "title": "Latihan 4: Hash Password dengan Salt dan PBKDF2",
        "difficulty": "Menengah",
        "question": [
            "Buat penyimpanan password mini. Tiap baris masukan salah satu",
            "dari dua perintah:",
            "  daftar <nama> <password> <salt_hex>",
            "  login <nama> <password>",
            "",
            "Untuk daftar, hitung hashlib.pbkdf2_hmac(\"sha256\", password",
            "UTF-8, bytes.fromhex(salt_hex), 1000) lalu simpan string",
            "pbkdf2_sha256$1000$<salt_hex>$<hash_hex>. Cetak string itu",
            "dengan 48 karakter terakhirnya diganti ... (jadi yang terlihat",
            "cuma 16 karakter awal hash):",
            "  simpan <nama>: pbkdf2_sha256$1000$<salt_hex>$<16 hex>...",
            "",
            "Untuk login, ambil iterasi dan salt dari string tersimpan,",
            "hitung ulang, bandingkan dengan hmac.compare_digest, lalu cetak",
            "login <nama>: BERHASIL atau login <nama>: GAGAL. Pengguna yang",
            "belum terdaftar juga GAGAL, dengan pesan yang sama persis,",
            "supaya penyerang tidak bisa menebak nama mana yang terdaftar.",
            "",
            "Di akhir cetak <jumlah> pengguna, <jumlah> hash berbeda.",
            "(Iterasi 1000 dipakai supaya latihan cepat; di produksi minimal",
            "600000.)",
            "",
            "Contoh masukan:",
            "  daftar ani rahasia123 9f3c2a7d51e04b8a",
            "  daftar budi rahasia123 04d1e6b2a9c87f35",
            "  daftar cici kopi-susu 77aa10be3c4d5e6f",
            "  login ani rahasia123",
            "  login ani Rahasia123",
            "  login budi rahasia123",
            "  login dodi apa-saja",
            "",
            "Keluaran yang diharapkan:",
            "simpan ani: pbkdf2_sha256$1000$9f3c2a7d51e04b8a$76f0e045ddc1b683...",
            "simpan budi: pbkdf2_sha256$1000$04d1e6b2a9c87f35$3784c9c856cb2b95...",
            "simpan cici: pbkdf2_sha256$1000$77aa10be3c4d5e6f$89de271f3067c915...",
            "login ani: BERHASIL",
            "login ani: GAGAL",
            "login budi: BERHASIL",
            "login dodi: GAGAL",
            "3 pengguna, 3 hash berbeda",
            "",
            "Perhatikan Ani dan Budi berpassword sama, tapi hash-nya beda",
            "karena salt-nya beda.",
        ],
        "hints": [
            "Simpan akun di dict dari nama ke string tersimpan, dan pecah string itu kembali dengan split(\"$\") saat login.",
            "Buat satu fungsi pembantu yang menerima password, salt dalam bentuk hex, dan jumlah iterasi, lalu mengembalikan hash dalam bentuk hex.",
            "Hash SHA-256 berupa 64 karakter hex, jadi menyisakan 16 karakter awalnya sama dengan membuang 48 karakter terakhir dari string.",
            "Hitung hash berbeda dengan himpunan berisi bagian keempat dari tiap string tersimpan.",
        ],
        "solution": """import hashlib
import hmac
import sys

ITERASI = 1000  # kecil supaya latihan cepat; di produksi minimal 600000


def turunkan(password, salt_hex, iterasi):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                               bytes.fromhex(salt_hex), iterasi).hex()


akun = {}
for baris in sys.stdin.read().splitlines():
    bagian = baris.split()
    if not bagian:
        continue
    if bagian[0] == "daftar":
        _, nama, password, salt_hex = bagian
        nilai = turunkan(password, salt_hex, ITERASI)
        akun[nama] = f"pbkdf2_sha256${ITERASI}${salt_hex}${nilai}"
        print(f"simpan {nama}: {akun[nama][:-48]}...")
    elif bagian[0] == "login":
        _, nama, password = bagian
        berhasil = False
        if nama in akun:
            _, iterasi, salt_hex, nilai = akun[nama].split("$")
            coba = turunkan(password, salt_hex, int(iterasi))
            berhasil = hmac.compare_digest(coba, nilai)
        print(f"login {nama}: {'BERHASIL' if berhasil else 'GAGAL'}")

beda = len({nilai.split('$')[3] for nilai in akun.values()})
print(f"{len(akun)} pengguna, {beda} hash berbeda")
""",
        "stdin_list": [
            """daftar ani rahasia123 9f3c2a7d51e04b8a
daftar budi rahasia123 04d1e6b2a9c87f35
daftar cici kopi-susu 77aa10be3c4d5e6f
login ani rahasia123
login ani Rahasia123
login budi rahasia123
login dodi apa-saja
""",
            """login eka senja-di-pantai
daftar eka senja-di-pantai 0011223344556677
login eka senja-di-pantai
login eka senja-di-Pantai
""",
        ],
    },
    {
        "title": "Latihan 5: Token Bertanda Tangan HMAC dengan Masa Berlaku",
        "difficulty": "Menengah",
        "question": [
            "Buat token mini mirip JWT, lalu periksa beberapa token pada jam",
            "tiruan. Kunci rahasianya b\"kunci-latihan-bab3\".",
            "",
            "Cara membuat token untuk (sub, exp):",
            "  1. payload = json.dumps({\"sub\": sub, \"exp\": exp},",
            "     separators=(\",\", \":\"), sort_keys=True)",
            "  2. bagian = base64url(payload UTF-8), tanpa tanda = di ujung",
            "  3. tanda = base64url(HMAC-SHA256(kunci, bagian ASCII)), tanpa =",
            "  4. token = bagian + \".\" + tanda",
            "",
            "Tiap baris masukan: nama exp jam aksi. Buat token untuk",
            "(nama, exp), lalu ubah sesuai aksi:",
            "  asli   token apa adanya",
            "  ubah   ganti bagian depan dengan bagian milik sub \"admin\"",
            "         (exp sama), tapi pertahankan tanda yang lama",
            "  rusak  buang semua titik dari token",
            "",
            "Periksa token pada jam itu, berurutan:",
            "  1. Kalau dipecah dengan titik tidak menghasilkan tepat 2",
            "     bagian: RUSAK",
            "  2. Kalau tanda tidak cocok (pakai hmac.compare_digest):",
            "     TANDA_TANGAN_SALAH",
            "  3. Kalau jam >= exp: KEDALUWARSA",
            "  4. Selain itu: VALID (sub=<sub dari payload>)",
            "",
            "Cetak <nama> <aksi> @<jam>: <hasil>. Untuk baris pertama saja,",
            "sebelum hasilnya, cetak juga Token pertama: <token asli> dan",
            "Isi payload tanpa kunci: <payload hasil decode>, untuk",
            "menunjukkan bahwa isi token bisa dibaca siapa saja.",
            "",
            "Contoh masukan:",
            "  ani 1300 1200 asli",
            "  ani 1300 1300 asli",
            "  budi 2000 1000 ubah",
            "  cici 2000 1000 rusak",
            "  dodi 1500 1499 asli",
            "",
            "Keluaran yang diharapkan:",
            "Token pertama: eyJleHAiOjEzMDAsInN1YiI6ImFuaSJ9.hsTnnoNXxRbrZK4XUh2GIKdrk7V2My05il8drWZVdhs",
            "Isi payload tanpa kunci: {\"exp\":1300,\"sub\":\"ani\"}",
            "ani asli @1200: VALID (sub=ani)",
            "ani asli @1300: KEDALUWARSA",
            "budi ubah @1000: TANDA_TANGAN_SALAH",
            "cici rusak @1000: RUSAK",
            "dodi asli @1499: VALID (sub=dodi)",
        ],
        "hints": [
            "Pisahkan pekerjaannya jadi empat fungsi kecil: encode base64url, decode base64url, hitung tanda, dan periksa token.",
            "base64.urlsafe_b64encode menambahkan tanda = di ujung, jadi buang dengan rstrip(b\"=\"), dan saat decode tambahkan lagi sebanyak (-len(teks) % 4).",
            "Periksa tanda sebelum membaca isi payload, supaya data dari token palsu tidak pernah dipercaya.",
            "Untuk aksi ubah, buat token baru milik admin, ambil bagian sebelum titiknya, lalu sambung dengan tanda dari token asli.",
        ],
        "solution": """import base64
import hashlib
import hmac
import json
import sys

KUNCI = b"kunci-latihan-bab3"


def b64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def buka_b64url(teks):
    return base64.urlsafe_b64decode(teks + "=" * (-len(teks) % 4))


def tanda(bagian_payload):
    return b64url(hmac.new(KUNCI, bagian_payload.encode("ascii"), hashlib.sha256).digest())


def buat(sub, exp):
    isi = json.dumps({"sub": sub, "exp": exp}, separators=(",", ":"), sort_keys=True)
    bagian = b64url(isi.encode("utf-8"))
    return f"{bagian}.{tanda(bagian)}"


def periksa(token, jam):
    potongan = token.split(".")
    if len(potongan) != 2:
        return "RUSAK"
    bagian, tanda_kiriman = potongan
    if not hmac.compare_digest(tanda(bagian), tanda_kiriman):
        return "TANDA_TANGAN_SALAH"
    try:
        isi = json.loads(buka_b64url(bagian))
    except ValueError:
        return "RUSAK"
    if jam >= isi["exp"]:
        return "KEDALUWARSA"
    return f"VALID (sub={isi['sub']})"


pertama = True
for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    nama, exp, jam, aksi = baris.split()
    exp, jam = int(exp), int(jam)
    token = buat(nama, exp)
    if pertama:
        print("Token pertama:", token)
        print("Isi payload tanpa kunci:", buka_b64url(token.split(".")[0]).decode())
        pertama = False
    if aksi == "ubah":
        palsu = buat("admin", exp).split(".")[0]
        token = palsu + "." + token.split(".")[1]
    elif aksi == "rusak":
        token = token.replace(".", "")
    print(f"{nama} {aksi} @{jam}: {periksa(token, jam)}")
""",
        "stdin_list": [
            """ani 1300 1200 asli
ani 1300 1300 asli
budi 2000 1000 ubah
cici 2000 1000 rusak
dodi 1500 1499 asli
""",
            """eka 500 100 ubah
eka 500 499 asli
eka 500 501 asli
""",
        ],
    },
    {
        "title": "Latihan 6: RBAC Mini dengan Peran Bertingkat",
        "difficulty": "Menengah",
        "question": [
            "Buat pemeriksa izin dengan peran yang mewarisi peran lain.",
            "Masukan punya empat bagian:",
            "",
            "  [peran]     nama: izin1, izin2   atau   nama < induk: izin",
            "              (peran mewarisi semua izin induknya, bertingkat)",
            "  [pengguna]  nama: peran",
            "  [artikel]   nomor: pemilik",
            "  [minta]     nama izin [nomor]",
            "",
            "Pisahkan nama dan daftar izin dengan \": \" (titik dua lalu spasi),",
            "karena nama izin sendiri memuat titik dua.",
            "",
            "Untuk tiap permintaan, periksa berurutan:",
            "  1. Pengguna tidak ada: TOLAK <permintaan> (pengguna tidak dikenal)",
            "  2. Izin tidak ada di peran itu maupun leluhurnya:",
            "     TOLAK <permintaan> (tidak punya izin)",
            "  3. Izinnya artikel:tulis atau artikel:hapus, ada nomor artikel,",
            "     peran pengguna bukan admin, dan ia bukan pemilik artikel:",
            "     TOLAK <permintaan> (bukan pemilik)",
            "  4. Selain itu: IZINKAN <permintaan> (<jalur peran>)",
            "",
            "Jalur peran adalah urutan dari peran pengguna sampai peran yang",
            "memberi izin itu, dipisah \" > \". <permintaan> adalah baris",
            "permintaan apa adanya.",
            "",
            "Contoh masukan:",
            "  [peran]",
            "  pembaca: artikel:baca",
            "  editor < pembaca: artikel:tulis",
            "  admin < editor: pengguna:kelola, artikel:hapus",
            "  [pengguna]",
            "  ani: admin",
            "  budi: editor",
            "  cici: pembaca",
            "  [artikel]",
            "  1: budi",
            "  2: cici",
            "  [minta]",
            "  budi artikel:tulis 1",
            "  budi artikel:tulis 2",
            "  cici artikel:baca 1",
            "  cici artikel:tulis 2",
            "  ani artikel:baca 2",
            "  ani artikel:hapus 1",
            "  ani pengguna:kelola",
            "  dodi artikel:baca 1",
            "",
            "Keluaran yang diharapkan:",
            "IZINKAN budi artikel:tulis 1 (editor)",
            "TOLAK budi artikel:tulis 2 (bukan pemilik)",
            "IZINKAN cici artikel:baca 1 (pembaca)",
            "TOLAK cici artikel:tulis 2 (tidak punya izin)",
            "IZINKAN ani artikel:baca 2 (admin > editor > pembaca)",
            "IZINKAN ani artikel:hapus 1 (admin)",
            "IZINKAN ani pengguna:kelola (admin)",
            "TOLAK dodi artikel:baca 1 (pengguna tidak dikenal)",
            "",
            "Cici pemilik artikel 2, tapi tetap ditolak karena perannya",
            "tidak punya izin tulis. Kepemilikan cuma membatasi, tidak",
            "pernah menambah izin.",
        ],
        "hints": [
            "Simpan dua dict untuk peran: satu dari nama ke induknya (atau None), satu lagi dari nama ke himpunan izin yang ditulis langsung.",
            "Cari izin dengan berjalan dari peran pengguna ke induknya terus sampai ketemu atau sampai induknya None, sambil mencatat nama peran yang dilewati.",
            "Pakai str.partition(\": \") untuk memisahkan nama dari daftar izin, lalu partition(\" < \") untuk menemukan induknya.",
            "Ikuti urutan pemeriksaan di soal dan pakai continue di tiap penolakan, supaya hanya satu alasan yang tercetak.",
        ],
        "solution": """import sys

induk, izin_langsung = {}, {}
peran_pengguna, pemilik = {}, {}
bagian = None
permintaan = []
for baris in sys.stdin.read().splitlines():
    baris = baris.strip()
    if not baris:
        continue
    if baris.startswith("["):
        bagian = baris
        continue
    if bagian == "[peran]":
        kiri, _, kanan = baris.partition(": ")
        nama, _, ortu = kiri.partition(" < ")
        induk[nama] = ortu or None
        izin_langsung[nama] = {i.strip() for i in kanan.split(",") if i.strip()}
    elif bagian == "[pengguna]":
        nama, _, peran = baris.partition(": ")
        peran_pengguna[nama] = peran
    elif bagian == "[artikel]":
        nomor, _, nama = baris.partition(": ")
        pemilik[nomor] = nama
    elif bagian == "[minta]":
        permintaan.append(baris.split())


def jalur_izin(peran, izin):
    jalur = []
    while peran is not None:
        jalur.append(peran)
        if izin in izin_langsung[peran]:
            return jalur
        peran = induk[peran]
    return None


for minta in permintaan:
    nama, izin = minta[0], minta[1]
    nomor = minta[2] if len(minta) > 2 else None
    teks = " ".join(minta)
    if nama not in peran_pengguna:
        print(f"TOLAK {teks} (pengguna tidak dikenal)")
        continue
    peran = peran_pengguna[nama]
    jalur = jalur_izin(peran, izin)
    if jalur is None:
        print(f"TOLAK {teks} (tidak punya izin)")
        continue
    perlu_pemilik = izin in ("artikel:tulis", "artikel:hapus") and nomor is not None
    if perlu_pemilik and peran != "admin" and pemilik.get(nomor) != nama:
        print(f"TOLAK {teks} (bukan pemilik)")
        continue
    print(f"IZINKAN {teks} ({' > '.join(jalur)})")
""",
        "stdin_list": [
            """[peran]
pembaca: artikel:baca
editor < pembaca: artikel:tulis
admin < editor: pengguna:kelola, artikel:hapus
[pengguna]
ani: admin
budi: editor
cici: pembaca
[artikel]
1: budi
2: cici
[minta]
budi artikel:tulis 1
budi artikel:tulis 2
cici artikel:baca 1
cici artikel:tulis 2
ani artikel:baca 2
ani artikel:hapus 1
ani pengguna:kelola
dodi artikel:baca 1
""",
            """[peran]
tamu: katalog:lihat
kasir < tamu: pesanan:buat, artikel:tulis
manajer < kasir: laporan:lihat, artikel:hapus
[pengguna]
rina: manajer
soni: kasir
[artikel]
7: soni
8: rina
[minta]
soni katalog:lihat
soni artikel:tulis 8
rina artikel:hapus 7
rina artikel:hapus 8
soni laporan:lihat
""",
        ],
    },
    {
        "title": "Latihan 7: Query Aman dengan Parameter di SQLite",
        "difficulty": "Menengah",
        "question": [
            "Buat database SQLite di memori (sqlite3.connect(\":memory:\"))",
            "dengan tabel pengguna (id INTEGER, nama TEXT, peran TEXT) berisi:",
            "",
            "  1  budi    admin",
            "  2  sari    editor",
            "  3  o'neil  pembaca",
            "  4  wati    pembaca",
            "",
            "Tulis dua fungsi pencari nama:",
            "",
            "  - cari_rentan(nama): menyusun query dengan menyambung teks,",
            "    \"SELECT id FROM pengguna WHERE nama = '\" + nama + \"'\".",
            "    Kalau query gagal dijalankan (sqlite3.Error), hasilnya ERROR.",
            "  - cari_aman(nama): query yang sama dengan placeholder ?.",
            "",
            "Baca stdin baris demi baris. Untuk tiap baris yang tidak kosong,",
            "cetak: <masukan>: rentan=<jumlah baris atau ERROR> aman=<jumlah>",
            "",
            "Database ini milikmu sendiri dan hidup di memori. Tujuannya",
            "melihat kenapa versi rentan rusak, bukan menyerang sistem lain.",
            "",
            "Keluaran yang diharapkan:",
            "budi: rentan=1 aman=1",
            "o'neil: rentan=ERROR aman=1",
            "x' OR '1'='1: rentan=4 aman=0",
            "dodi: rentan=0 aman=0",
        ],
        "hints": [
            "Perhatikan nama o'neil: tanda kutipnya menutup string SQL lebih awal di versi rentan, sementara versi aman memperlakukannya sebagai data biasa.",
            "Tangkap sqlite3.Error di cari_rentan dan kembalikan teks ERROR, lalu hitung hasil fetchall() dengan len().",
            "Versi aman memanggil db.execute(\"SELECT id FROM pengguna WHERE nama = ?\", (nama,)), perhatikan koma di tuple satu elemen.",
        ],
        "solution": """import sqlite3
import sys

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE pengguna (id INTEGER, nama TEXT, peran TEXT)")
db.executemany("INSERT INTO pengguna VALUES (?, ?, ?)", [
    (1, "budi", "admin"),
    (2, "sari", "editor"),
    (3, "o'neil", "pembaca"),
    (4, "wati", "pembaca"),
])


def cari_rentan(nama):
    sql = "SELECT id FROM pengguna WHERE nama = '" + nama + "'"
    try:
        return str(len(db.execute(sql).fetchall()))
    except sqlite3.Error:
        return "ERROR"


def cari_aman(nama):
    sql = "SELECT id FROM pengguna WHERE nama = ?"
    return str(len(db.execute(sql, (nama,)).fetchall()))


for baris in sys.stdin.read().splitlines():
    if not baris:
        continue
    print(f"{baris}: rentan={cari_rentan(baris)} aman={cari_aman(baris)}")
""",
        "stdin": """budi
o'neil
x' OR '1'='1
dodi
""",
    },
    {
        "title": "Latihan 8: Pencegah XSS dengan Escape HTML",
        "difficulty": "Menengah",
        "question": [
            "Buku tamu menerima baris berformat nama|situs|komentar dari stdin.",
            "Komentar boleh memuat tanda |, jadi pecah baris paling banyak",
            "jadi tiga bagian (split(\"|\", 2)).",
            "",
            "Untuk tiap baris, cetak satu elemen daftar:",
            "",
            "  <li><a href=\"SITUS\">NAMA</a>: KOMENTAR</li>",
            "",
            "Aturannya:",
            "",
            "  - NAMA, KOMENTAR, dan SITUS di-escape dengan html.escape",
            "    (tanda kutip ikut di-escape).",
            "  - SITUS dibuang spasinya di kiri-kanan. Kalau huruf kecilnya",
            "    tidak diawali http: atau https:, ganti dengan # dan hitung",
            "    sebagai tautan ditolak.",
            "  - Di akhir, cetak: tautan ditolak: <jumlah>",
            "",
            "Keluaran yang diharapkan:",
            "<li><a href=\"https://budi.example\">Budi</a>: Mantap, kopinya enak!</li>",
            "<li><a href=\"https://sari.example/?a=1&amp;b=2\">Sari &lt;b&gt;</a>: &lt;script&gt;alert(1)&lt;/script&gt;</li>",
            "<li><a href=\"#\">Iseng</a>: klik namaku</li>",
            "<li><a href=\"#\">Tono</a>: &quot;kutip&quot; &amp; &#x27;apostrof&#x27; | garis</li>",
            "tautan ditolak: 2",
        ],
        "hints": [
            "Ada dua bahaya berbeda: tag di nama dan komentar (diatasi escape) dan skema javascript: di href yang tetap jalan walau sudah di-escape (diatasi daftar putih skema).",
            "Bandingkan situs.strip().lower() dengan tuple (\"http:\", \"https:\") lewat startswith, karena penyerang bisa menulis JavaScript: dengan huruf besar atau spasi di depan.",
            "Susun keluaran dengan f-string yang memanggil html.escape untuk ketiga bagian, lalu cetak penghitung tautan ditolak sesudah perulangan.",
        ],
        "solution": """import html
import sys

SKEMA_AMAN = ("http:", "https:")
ditolak = 0

for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    nama, situs, komentar = baris.split("|", 2)
    tautan = situs.strip()
    if not tautan.lower().startswith(SKEMA_AMAN):
        tautan = "#"
        ditolak += 1
    print(f'<li><a href="{html.escape(tautan)}">{html.escape(nama)}</a>: '
          f'{html.escape(komentar)}</li>')

print(f"tautan ditolak: {ditolak}")
""",
        "stdin": """Budi|https://budi.example|Mantap, kopinya enak!
Sari <b>|https://sari.example/?a=1&b=2|<script>alert(1)</script>
Iseng|javascript:alert(1)|klik namaku
Tono|  JavaScript:alert(1)|"kutip" & 'apostrof' | garis
""",
    },
    {
        "title": "Latihan 9: Rate Limiter Login dengan Jam Tiruan",
        "difficulty": "Menengah",
        "question": [
            "Tiap baris stdin adalah satu percobaan login:",
            "",
            "  <detik> <ip> <user> <gagal|sukses>",
            "",
            "Proses baris berurutan dengan aturan ini:",
            "",
            "  1. Kalau akun user sedang terkunci (detik kunci dibuka masih",
            "     lebih besar dari detik sekarang), cetak TERKUNCI.",
            "  2. Kalau belum, pakai token bucket per pasangan (ip, user):",
            "     kapasitas 3 token, terisi 1 token tiap 20 detik, satu",
            "     percobaan memakai 1 token. Hitung dalam miliToken (bilangan",
            "     bulat): kapasitas 3000, biaya 1000, isi 50 per detik. Ember",
            "     baru mulai penuh. Kalau token kurang dari 1000, cetak",
            "     TOLAK_429.",
            "  3. Kalau token cukup, cetak IZINKAN lalu lihat hasilnya.",
            "     sukses mengosongkan hitungan gagal beruntun milik user.",
            "     gagal menambah hitungan itu. Begitu mencapai 5, akun",
            "     dikunci 60 detik, hitungannya kembali 0, dan cetak baris",
            "     tambahan: \"  akun <user> dikunci sampai detik <d>\".",
            "",
            "Format baris keputusan: <detik> <ip> <user> <keputusan>",
            "",
            "Keluaran yang diharapkan:",
            "0 203.0.113.7 budi IZINKAN",
            "1 203.0.113.7 budi IZINKAN",
            "2 203.0.113.7 budi IZINKAN",
            "3 203.0.113.7 budi TOLAK_429",
            "5 198.51.100.4 budi IZINKAN",
            "6 198.51.100.8 budi IZINKAN",
            "  akun budi dikunci sampai detik 66",
            "7 10.0.0.2 sari IZINKAN",
            "30 10.0.0.9 budi TERKUNCI",
            "41 203.0.113.7 sari IZINKAN",
            "70 10.0.0.9 budi IZINKAN",
        ],
        "hints": [
            "Ada tiga keadaan yang perlu disimpan: isi ember per pasangan (ip, user), hitungan gagal per user, dan detik kunci dibuka per user.",
            "Periksa kunci akun lebih dulu, baru isi ulang ember dengan rumus min(kapasitas, token + selisih_detik * 50), dan ingat percobaan yang ditolak 429 atau TERKUNCI nggak menambah hitungan gagal.",
            "Simpan ember sebagai dict berkunci tuple, misalnya ember[(ip, user)] = [token, detik_terakhir], dan ambil nilai awal dengan ember.get((ip, user), [3000, detik]).",
        ],
        "solution": """import sys

KAPASITAS = 3000      # 3 token, dihitung dalam miliToken supaya tetap bilangan bulat
BIAYA = 1000          # satu percobaan = 1 token
ISI_PER_DETIK = 50    # 1 token tiap 20 detik
BATAS_GAGAL = 5
LAMA_KUNCI = 60

ember = {}            # (ip, user) -> [miliToken, detik_terakhir]
gagal = {}            # user -> jumlah gagal beruntun
terkunci = {}         # user -> detik kunci dibuka

for baris in sys.stdin.read().splitlines():
    if not baris.strip():
        continue
    detik, ip, user, hasil = baris.split()
    detik = int(detik)

    if terkunci.get(user, -1) > detik:
        print(f"{detik} {ip} {user} TERKUNCI")
        continue

    token, terakhir = ember.get((ip, user), [KAPASITAS, detik])
    token = min(KAPASITAS, token + (detik - terakhir) * ISI_PER_DETIK)
    if token < BIAYA:
        ember[(ip, user)] = [token, detik]
        print(f"{detik} {ip} {user} TOLAK_429")
        continue
    ember[(ip, user)] = [token - BIAYA, detik]
    print(f"{detik} {ip} {user} IZINKAN")

    if hasil == "sukses":
        gagal[user] = 0
    else:
        gagal[user] = gagal.get(user, 0) + 1
        if gagal[user] >= BATAS_GAGAL:
            terkunci[user] = detik + LAMA_KUNCI
            gagal[user] = 0
            print(f"  akun {user} dikunci sampai detik {terkunci[user]}")
""",
        "stdin_list": [
            """0 203.0.113.7 budi gagal
1 203.0.113.7 budi gagal
2 203.0.113.7 budi gagal
3 203.0.113.7 budi gagal
5 198.51.100.4 budi gagal
6 198.51.100.8 budi gagal
7 10.0.0.2 sari sukses
30 10.0.0.9 budi sukses
41 203.0.113.7 sari gagal
70 10.0.0.9 budi sukses
""",
            """0 10.0.0.5 dina gagal
0 10.0.0.5 dina gagal
0 10.0.0.5 dina gagal
0 10.0.0.5 dina gagal
20 10.0.0.5 dina sukses
21 10.0.0.5 dina gagal
""",
        ],
    },
    {
        "title": "Latihan 10: Pemeriksa Header Keamanan HTTP",
        "difficulty": "Menengah",
        "question": [
            "Stdin berisi satu respons HTTP mentah: baris status, header,",
            "baris kosong, lalu body. Nama header tidak peka huruf",
            "besar-kecil, dan Set-Cookie boleh muncul lebih dari sekali.",
            "",
            "Periksa header berikut, cetak satu baris per pemeriksaan dengan",
            "format f\"{status:<10} {nama}\" ditambah \": alasan\" kalau ada:",
            "",
            "  - Content-Security-Policy: tidak ada = GAGAL (tidak ada);",
            "    memuat 'unsafe-inline' = PERINGATAN (memakai",
            "    'unsafe-inline'); selain itu LULUS.",
            "  - Strict-Transport-Security: tidak ada = GAGAL (tidak ada);",
            "    max-age di bawah 31536000 = PERINGATAN (max-age <n> kurang",
            "    dari setahun); selain itu LULUS.",
            "  - X-Content-Type-Options: nilainya nosniff = LULUS; selain",
            "    itu GAGAL (harus nosniff).",
            "  - Referrer-Policy: tidak ada = PERINGATAN (tidak ada);",
            "    unsafe-url atau no-referrer-when-downgrade = PERINGATAN",
            "    (<nilai> membocorkan URL lengkap); selain itu LULUS.",
            "  - Tiap Set-Cookie, dengan nama \"cookie <nama>\": cek atribut",
            "    Secure, HttpOnly, SameSite (urutan itu). Tanpa Secure =",
            "    GAGAL, kurang yang lain saja = PERINGATAN, alasannya",
            "    \"kurang \" lalu daftar yang kurang dipisah \", \".",
            "",
            "Terakhir cetak ringkasan jumlah LULUS, PERINGATAN, dan GAGAL.",
            "",
            "Keluaran yang diharapkan:",
            "PERINGATAN Content-Security-Policy: memakai 'unsafe-inline'",
            "PERINGATAN Strict-Transport-Security: max-age 86400 kurang dari setahun",
            "GAGAL      X-Content-Type-Options: harus nosniff",
            "PERINGATAN Referrer-Policy: unsafe-url membocorkan URL lengkap",
            "GAGAL      cookie sesi: kurang Secure, SameSite",
            "PERINGATAN cookie tema: kurang HttpOnly, SameSite",
            "ringkasan: 0 LULUS, 4 PERINGATAN, 2 GAGAL",
        ],
        "hints": [
            "Header berakhir di baris kosong pertama, dan karena namanya tidak peka huruf besar-kecil, simpan semuanya dalam huruf kecil sebelum dicari.",
            "Simpan Set-Cookie di list tersendiri karena bisa lebih dari satu, lalu pecah tiap cookie dengan ; dan ambil nama atributnya sebelum tanda = dalam huruf kecil.",
            "Untuk HSTS, pecah nilainya dengan ;, cari bagian yang diawali max-age=, ubah sisanya jadi int, lalu bandingkan dengan 31536000.",
        ],
        "solution": "import sys\n\nteks = sys.stdin.read()\nkepala = teks.split(\"\\n\\n\", 1)[0].splitlines()[1:]   # buang baris status\n\nheader = {}\ncookie = []\nfor baris in kepala:\n    if \":\" not in baris:\n        continue\n    nama, nilai = baris.split(\":\", 1)\n    nama, nilai = nama.strip().lower(), nilai.strip()\n    if nama == \"set-cookie\":\n        cookie.append(nilai)\n    else:\n        header[nama] = nilai\n\nhasil = []\n\n\ndef lapor(status, nama, alasan=\"\"):\n    hasil.append(status)\n    print(f\"{status:<10} {nama}\" + (f\": {alasan}\" if alasan else \"\"))\n\n\ncsp = header.get(\"content-security-policy\")\nif csp is None:\n    lapor(\"GAGAL\", \"Content-Security-Policy\", \"tidak ada\")\nelif \"'unsafe-inline'\" in csp:\n    lapor(\"PERINGATAN\", \"Content-Security-Policy\", \"memakai 'unsafe-inline'\")\nelse:\n    lapor(\"LULUS\", \"Content-Security-Policy\")\n\nhsts = header.get(\"strict-transport-security\")\nif hsts is None:\n    lapor(\"GAGAL\", \"Strict-Transport-Security\", \"tidak ada\")\nelse:\n    umur = 0\n    for bagian in hsts.split(\";\"):\n        bagian = bagian.strip().lower()\n        if bagian.startswith(\"max-age=\"):\n            umur = int(bagian[len(\"max-age=\"):])\n    if umur < 31536000:\n        lapor(\"PERINGATAN\", \"Strict-Transport-Security\",\n              f\"max-age {umur} kurang dari setahun\")\n    else:\n        lapor(\"LULUS\", \"Strict-Transport-Security\")\n\nif header.get(\"x-content-type-options\", \"\").lower() == \"nosniff\":\n    lapor(\"LULUS\", \"X-Content-Type-Options\")\nelse:\n    lapor(\"GAGAL\", \"X-Content-Type-Options\", \"harus nosniff\")\n\nrp = header.get(\"referrer-policy\")\nif rp is None:\n    lapor(\"PERINGATAN\", \"Referrer-Policy\", \"tidak ada\")\nelif rp.lower() in (\"unsafe-url\", \"no-referrer-when-downgrade\"):\n    lapor(\"PERINGATAN\", \"Referrer-Policy\", f\"{rp} membocorkan URL lengkap\")\nelse:\n    lapor(\"LULUS\", \"Referrer-Policy\")\n\nfor c in cookie:\n    bagian = [b.strip() for b in c.split(\";\")]\n    nama = bagian[0].split(\"=\", 1)[0]\n    atribut = {b.split(\"=\", 1)[0].lower() for b in bagian[1:]}\n    kurang = [a for a in (\"Secure\", \"HttpOnly\", \"SameSite\") if a.lower() not in atribut]\n    if \"Secure\" in kurang:\n        lapor(\"GAGAL\", f\"cookie {nama}\", \"kurang \" + \", \".join(kurang))\n    elif kurang:\n        lapor(\"PERINGATAN\", f\"cookie {nama}\", \"kurang \" + \", \".join(kurang))\n    else:\n        lapor(\"LULUS\", f\"cookie {nama}\")\n\nprint(f\"ringkasan: {hasil.count('LULUS')} LULUS, {hasil.count('PERINGATAN')} PERINGATAN, \"\n      f\"{hasil.count('GAGAL')} GAGAL\")\n",
        "stdin_list": [
            """HTTP/1.1 200 OK
Server: Apache/2.4.41
Content-Security-Policy: script-src 'self' 'unsafe-inline'
Strict-Transport-Security: max-age=86400
Referrer-Policy: unsafe-url
Set-Cookie: sesi=77ab; Path=/; HttpOnly
Set-Cookie: tema=gelap; Path=/; Secure

<html>halo</html>
""",
            """HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
Content-Security-Policy: default-src 'self'; frame-ancestors 'none'
strict-transport-security: max-age=63072000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Set-Cookie: sesi=a81f; Path=/; Secure; HttpOnly; SameSite=Lax

<html>halo</html>
""",
        ],
    },
    {
        "title": "Latihan 11: Pemindai Secret di Teks",
        "difficulty": "Menengah",
        "question": [
            "Pindai teks dari stdin (isi berkas kode, .env, atau log milikmu",
            "sendiri) dan laporkan rahasia yang mungkin ikut tertulis.",
            "",
            "Periksa tiap baris (nomor mulai 1) dengan tiga pola ini, urut:",
            "",
            "  - aws_access_key: AKIA diikuti 16 huruf besar atau angka.",
            "  - github_token: gh, salah satu dari p o u s r, garis bawah,",
            "    lalu 36 huruf atau angka.",
            "  - private_key: baris -----BEGIN ... PRIVATE KEY-----.",
            "",
            "Lalu cari calon string acak: 20 karakter atau lebih dari",
            "[A-Za-z0-9+/=_-] yang bukan bagian dari temuan pola di baris",
            "yang sama. Hitung entropi Shannon-nya (jumlah -p * log2(p) per",
            "huruf). Kalau 4.0 atau lebih, laporkan sebagai entropi_tinggi",
            "beserta nilainya dua angka di belakang koma.",
            "",
            "Samarkan nilai: kalau panjangnya lebih dari 8, tampilkan 4",
            "huruf pertama, bintang sebanyak sisa tengahnya, dan 4 huruf",
            "terakhir. Untuk private_key tulis (header kunci privat).",
            "Terakhir cetak total temuan.",
            "",
            "Keluaran yang diharapkan:",
            "baris 2: aws_access_key AKIA************MPLE",
            "baris 3: github_token ghp_********************************5678",
            "baris 5: private_key (header kunci privat)",
            "baris 6: entropi_tinggi Zx8q****************6hJ1 (4.58)",
            "total temuan: 4",
        ],
        "hints": [
            "Pola berawalan tetap (AKIA, ghp_, header PEM) menangkap jenis kunci yang dikenal, sedangkan entropi menangkap string acak yang polanya nggak dikenal; string biasa seperti nama_tabel_panjang punya entropi rendah karena hurufnya berulang.",
            "Simpan teks temuan pola untuk tiap baris, lalu lewati calon entropi yang sama dengan atau memuat temuan itu supaya satu kunci nggak dilaporkan dua kali.",
            "Entropi dihitung dari frekuensi tiap huruf: kumpulkan hitungan di dict, lalu jumlahkan -(c/n) * math.log2(c/n) untuk setiap hitungan c.",
        ],
        "solution": """import math
import re
import sys

POLA = [
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9]{36}")),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
CALON = re.compile(r"[A-Za-z0-9+/=_-]{20,}")


def entropi(teks):
    hitung = {}
    for huruf in teks:
        hitung[huruf] = hitung.get(huruf, 0) + 1
    n = len(teks)
    return -sum(c / n * math.log2(c / n) for c in hitung.values())


def samarkan(nilai):
    if len(nilai) <= 8:
        return "*" * len(nilai)
    return nilai[:4] + "*" * (len(nilai) - 8) + nilai[-4:]


temuan = 0
for nomor, baris in enumerate(sys.stdin.read().splitlines(), 1):
    sudah = []
    for jenis, pola in POLA:
        for m in pola.finditer(baris):
            sudah.append(m.group())
            temuan += 1
            if jenis == "private_key":
                print(f"baris {nomor}: {jenis} (header kunci privat)")
            else:
                print(f"baris {nomor}: {jenis} {samarkan(m.group())}")
    for m in CALON.finditer(baris):
        nilai = m.group()
        if any(nilai in s or s in nilai for s in sudah):
            continue
        e = entropi(nilai)
        if e >= 4.0:
            temuan += 1
            print(f"baris {nomor}: entropi_tinggi {samarkan(nilai)} ({e:.2f})")

print(f"total temuan: {temuan}")
""",
        "stdin_list": [
            """# konfigurasi contoh
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
GITHUB_TOKEN = "ghp_contohTokenPalsuUntukLatihan12345678"
nama_tabel = "konfigurasi_bawaan_aplikasi"
-----BEGIN OPENSSH PRIVATE KEY-----
sesi_rahasia: Zx8qL2vN9tR4wK7mP3sY6hJ1
print("halo dunia")
""",
            """DEBUG=false
DB_PASSWORD=${TOKO_DB_PASSWORD}
pesan = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
""",
        ],
    },
    {
        "title": "Latihan 12: Pencocok Dependensi Rentan dari Lockfile",
        "difficulty": "Lanjut",
        "question": [
            "Stdin berisi satu objek JSON dengan dua kunci:",
            "",
            "  - \"paket\": nama paket -> versi terpasang (dari lockfile).",
            "  - \"advisori\": daftar celah, tiap item punya id, paket,",
            "    rentan (syarat versi, beberapa syarat dipisah koma, operator",
            "    < <= > >= ==), perbaikan (versi yang sudah aman), dan",
            "    keparahan (kritis, tinggi, sedang, rendah).",
            "",
            "Versi berbentuk angka.angka.angka dan wajib dibandingkan sebagai",
            "angka: 0.4.2 lebih kecil dari 0.10.0.",
            "",
            "Untuk tiap paket yang terkena minimal satu advisori, versi aman",
            "terdekatnya adalah versi perbaikan tertinggi di antara advisori",
            "yang mengenainya, dan keparahannya yang paling parah. Cetak",
            "urut keparahan (kritis dulu), lalu nama paket:",
            "",
            "  [<keparahan>] <paket> <versi> -> <versi aman> (<id urut, dipisah koma>)",
            "",
            "Terakhir cetak: aman: <jumlah tak terkena> dari <jumlah> paket",
            "",
            "Contoh masukan (dipotong):",
            "",
            "  {\"paket\": {\"kopi-parser\": \"2.3.1\", ...},",
            "   \"advisori\": [{\"id\": \"CONTOH-2026-0102\", \"paket\": \"kopi-parser\",",
            "     \"rentan\": \">=2.0.0,<2.3.5\", \"perbaikan\": \"2.3.5\",",
            "     \"keparahan\": \"kritis\"}, ...]}",
            "",
            "Nama paket dan nomor advisori di latihan ini rekaan.",
            "",
            "Keluaran yang diharapkan:",
            "[kritis] kopi-parser 2.3.1 -> 2.3.5 (CONTOH-2026-0102)",
            "[tinggi] lumbung-http 1.9.0 -> 1.9.4 (CONTOH-2026-0101, CONTOH-2026-0104)",
            "[rendah] pustaka-tanggal 0.4.2 -> 0.10.0 (CONTOH-2026-0105)",
            "aman: 2 dari 5 paket",
        ],
        "hints": [
            "Membandingkan versi sebagai teks memberi hasil salah (\"0.10.0\" < \"0.4.2\" menurut urutan huruf), jadi ubah dulu tiap versi jadi tuple angka.",
            "Satu advisori mengenai paket kalau semua syarat dalam kolom rentan terpenuhi, jadi pecah dengan koma, kenali operatornya (cek <= dan >= sebelum < dan >), lalu bandingkan tuple.",
            "Kumpulkan hasil per paket di dict berisi versi perbaikan tertinggi, keparahan terparah, dan daftar id, lalu urutkan dengan key=lambda n: (URUTAN[keparahan], n).",
        ],
        "solution": """import json
import sys

URUTAN = {"kritis": 0, "tinggi": 1, "sedang": 2, "rendah": 3}


def versi(teks):
    return tuple(int(x) for x in teks.split("."))


def cocok(v, syarat):
    for bagian in syarat.split(","):
        bagian = bagian.strip()
        for op in ("<=", ">=", "==", "<", ">"):
            if bagian.startswith(op):
                batas = versi(bagian[len(op):])
                break
        ok = {"<": v < batas, "<=": v <= batas, ">": v > batas,
              ">=": v >= batas, "==": v == batas}[op]
        if not ok:
            return False
    return True


data = json.loads(sys.stdin.read())
paket = data["paket"]
rentan = {}
for adv in data["advisori"]:
    nama = adv["paket"]
    if nama not in paket or not cocok(versi(paket[nama]), adv["rentan"]):
        continue
    r = rentan.setdefault(nama, {"perbaikan": "0.0.0", "keparahan": "rendah", "id": []})
    if versi(adv["perbaikan"]) > versi(r["perbaikan"]):
        r["perbaikan"] = adv["perbaikan"]
    if URUTAN[adv["keparahan"]] < URUTAN[r["keparahan"]]:
        r["keparahan"] = adv["keparahan"]
    r["id"].append(adv["id"])

for nama in sorted(rentan, key=lambda n: (URUTAN[rentan[n]["keparahan"]], n)):
    r = rentan[nama]
    print(f"[{r['keparahan']}] {nama} {paket[nama]} -> {r['perbaikan']} "
          f"({', '.join(sorted(r['id']))})")
print(f"aman: {len(paket) - len(rentan)} dari {len(paket)} paket")
""",
        "stdin_list": [
            """{"paket": {"kopi-parser": "2.3.1", "lumbung-http": "1.9.0", "pustaka-tanggal": "0.4.2", "warna-cli": "5.0.0", "zip-ringan": "3.1.0"}, "advisori": [{"id": "CONTOH-2026-0101", "paket": "lumbung-http", "rentan": "<1.9.4", "perbaikan": "1.9.4", "keparahan": "tinggi"}, {"id": "CONTOH-2026-0102", "paket": "kopi-parser", "rentan": ">=2.0.0,<2.3.5", "perbaikan": "2.3.5", "keparahan": "kritis"}, {"id": "CONTOH-2026-0103", "paket": "warna-cli", "rentan": "<4.2.0", "perbaikan": "4.2.0", "keparahan": "sedang"}, {"id": "CONTOH-2026-0104", "paket": "lumbung-http", "rentan": ">=1.8.0,<=1.9.1", "perbaikan": "1.9.2", "keparahan": "sedang"}, {"id": "CONTOH-2026-0105", "paket": "pustaka-tanggal", "rentan": "<0.10.0", "perbaikan": "0.10.0", "keparahan": "rendah"}]}
""",
            """{"paket": {"warna-cli": "4.1.9", "zip-ringan": "3.0.0"}, "advisori": [{"id": "CONTOH-2026-0103", "paket": "warna-cli", "rentan": "<4.2.0", "perbaikan": "4.2.0", "keparahan": "sedang"}, {"id": "CONTOH-2026-0201", "paket": "zip-ringan", "rentan": "==3.0.1", "perbaikan": "3.0.2", "keparahan": "kritis"}]}
""",
        ],
    },
    {
        "title": "Latihan 13: Pemeriksa Statis Mini dengan Modul ast",
        "difficulty": "Lanjut",
        "question": [
            "Buat pemeriksa SAST kecil. Program membaca kode Python dari stdin,",
            "mengurainya dengan modul ast, lalu melaporkan lima pola:",
            "",
            "  eval-exec         panggilan eval() atau exec()",
            "  shell-true        panggilan subprocess.<apa saja> dengan shell=True",
            "  md5-lemah         panggilan hashlib.md5()",
            "  rahasia-tertanam  assignment ke nama yang (huruf kecilnya) memuat",
            "                    password, passwd, sandi, secret, token, atau",
            "                    api_key, dengan nilai string tetap yang tidak kosong",
            "  except-kosong     except: tanpa jenis exception",
            "",
            "Pesan tiap aturan, persis:",
            "  eval-exec         <nama>() menjalankan teks sebagai kode",
            "  shell-true        <subprocess.nama> dengan shell=True",
            "  md5-lemah         MD5 tidak layak untuk password",
            "  rahasia-tertanam  <nama variabel> berisi teks tetap",
            "  except-kosong     except: menelan semua error",
            "",
            "Cetak tiap temuan dengan format baris:aturan:pesan, urut menurut",
            "nomor baris lalu nama aturan. Baris terakhir: <N> temuan.",
            "Pakai ast, bukan pencarian teks, supaya komentar dan string tidak",
            "ikut tertangkap.",
            "",
            "Contoh masukan pertama:",
            "  # app.py",
            "  import hashlib",
            "  import subprocess",
            "",
            "  DB_PASSWORD = \"rahasia123\"",
            "  nama_toko = \"Toko Ani\"",
            "",
            "",
            "  def hitung(ekspresi):",
            "      return eval(ekspresi)",
            "",
            "",
            "  def cadangkan(folder):",
            "      subprocess.run(\"tar czf cadangan.tgz \" + folder, shell=True)",
            "      subprocess.run([\"ls\", folder])",
            "",
            "",
            "  def simpan(sandi):",
            "      try:",
            "          return hashlib.md5(sandi.encode()).hexdigest()",
            "      except:",
            "          return None",
            "",
            "Keluaran yang diharapkan:",
            "5:rahasia-tertanam:DB_PASSWORD berisi teks tetap",
            "10:eval-exec:eval() menjalankan teks sebagai kode",
            "14:shell-true:subprocess.run dengan shell=True",
            "20:md5-lemah:MD5 tidak layak untuk password",
            "21:except-kosong:except: menelan semua error",
            "5 temuan",
            "",
            "Masukan kedua adalah versi yang sudah diperbaiki, diawali baris",
            "# aman.py.",
            "",
            "Untuk input # aman.py, keluarannya:",
            "0 temuan",
        ],
        "hints": [
            "ast.parse mengubah teks jadi pohon, dan ast.walk mengunjungi setiap simpulnya satu per satu.",
            "Panggilan fungsi adalah ast.Call; namanya ada di node.func, berupa ast.Name (eval) atau ast.Attribute dengan value ast.Name (hashlib.md5).",
            "Untuk shell=True, periksa node.keywords: cari kw.arg == 'shell' yang nilainya ast.Constant bernilai True; untuk except kosong, cari ast.ExceptHandler yang type-nya None.",
            "Kumpulkan temuan sebagai tuple (baris, aturan, pesan), lalu sorted() otomatis mengurutkan menurut baris dulu, kemudian aturan.",
        ],
        "solution": """import ast
import sys

NAMA_RAHASIA = ("password", "passwd", "sandi", "secret", "token", "api_key")


def nama_fungsi(node):
    f = node.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name):
        return f.value.id + "." + f.attr
    return ""


def periksa(kode):
    temuan = []
    for node in ast.walk(ast.parse(kode)):
        if isinstance(node, ast.Call):
            nama = nama_fungsi(node)
            if nama in ("eval", "exec"):
                temuan.append((node.lineno, "eval-exec",
                               nama + "() menjalankan teks sebagai kode"))
            elif nama.startswith("subprocess."):
                for kw in node.keywords:
                    if (kw.arg == "shell" and isinstance(kw.value, ast.Constant)
                            and kw.value.value is True):
                        temuan.append((node.lineno, "shell-true",
                                       nama + " dengan shell=True"))
            elif nama == "hashlib.md5":
                temuan.append((node.lineno, "md5-lemah",
                               "MD5 tidak layak untuk password"))
        elif isinstance(node, ast.Assign):
            if (isinstance(node.value, ast.Constant)
                    and isinstance(node.value.value, str) and node.value.value):
                for target in node.targets:
                    if (isinstance(target, ast.Name)
                            and any(k in target.id.lower() for k in NAMA_RAHASIA)):
                        temuan.append((node.lineno, "rahasia-tertanam",
                                       target.id + " berisi teks tetap"))
        elif isinstance(node, ast.ExceptHandler) and node.type is None:
            temuan.append((node.lineno, "except-kosong",
                           "except: menelan semua error"))
    return sorted(temuan)


hasil = periksa(sys.stdin.read())
for baris, aturan, pesan in hasil:
    print(f"{baris}:{aturan}:{pesan}")
print(f"{len(hasil)} temuan")
""",
        "stdin_list": [
            """# app.py
import hashlib
import subprocess

DB_PASSWORD = "rahasia123"
nama_toko = "Toko Ani"


def hitung(ekspresi):
    return eval(ekspresi)


def cadangkan(folder):
    subprocess.run("tar czf cadangan.tgz " + folder, shell=True)
    subprocess.run(["ls", folder])


def simpan(sandi):
    try:
        return hashlib.md5(sandi.encode()).hexdigest()
    except:
        return None
""",
            """# aman.py
import hashlib
import os
import subprocess

DB_PASSWORD = os.environ["DB_PASSWORD"]


def cadangkan(folder):
    subprocess.run(["tar", "czf", "cadangan.tgz", folder], check=True)


def ringkas(data):
    try:
        return hashlib.sha256(data).hexdigest()
    except TypeError:
        return None
""",
        ],
    },
    {
        "title": "Latihan 14: Aturan Kebijakan untuk Konfigurasi Cloud",
        "difficulty": "Lanjut",
        "question": [
            "Buat pemindai kebijakan kecil seperti Checkov. Program membaca",
            "daftar sumber daya cloud dalam bentuk JSON dari stdin. Tiap",
            "sumber daya punya \"jenis\" dan \"nama\", ditambah medan sesuai",
            "jenisnya:",
            "",
            "  bucket          acl (teks), enkripsi (true/false)",
            "  security_group  ingress: daftar {cidr, dari, sampai}",
            "  database        enkripsi (true/false), backup_hari (angka)",
            "",
            "Terapkan lima aturan, berurutan menurut ID:",
            "",
            "  ATR-01  bucket          bucket tidak boleh publik",
            "          (acl bukan public-read atau public-read-write)",
            "  ATR-02  bucket          bucket wajib terenkripsi",
            "  ATR-03  security_group  port 22 tidak boleh terbuka ke internet",
            "          (gagal kalau ada ingress dengan cidr 0.0.0.0/0 atau",
            "          ::/0 yang rentang dari..sampai memuat 22)",
            "  ATR-04  database        database wajib terenkripsi",
            "  ATR-05  database        backup database minimal 7 hari",
            "",
            "Untuk tiap aturan, periksa setiap sumber daya berjenis yang cocok",
            "sesuai urutan di masukan. Cetak satu baris per pemeriksaan:",
            "status dirapatkan kiri selebar 6 (PASSED atau FAILED), dua spasi,",
            "ID, dua spasi, jenis.nama, dua spasi, judul aturan. Sesudahnya",
            "cetak jumlah lulus dan gagal, lalu keputusan gerbang.",
            "",
            "Contoh masukan:",
            "  [",
            "    {\"jenis\": \"bucket\", \"nama\": \"foto-produk\", \"acl\": \"public-read\", \"enkripsi\": true},",
            "    {\"jenis\": \"bucket\", \"nama\": \"cadangan\", \"acl\": \"private\", \"enkripsi\": false},",
            "    {\"jenis\": \"security_group\", \"nama\": \"web\", \"ingress\": [",
            "      {\"cidr\": \"0.0.0.0/0\", \"dari\": 443, \"sampai\": 443},",
            "      {\"cidr\": \"10.0.0.0/16\", \"dari\": 22, \"sampai\": 22}]},",
            "    {\"jenis\": \"security_group\", \"nama\": \"lama\", \"ingress\": [",
            "      {\"cidr\": \"0.0.0.0/0\", \"dari\": 0, \"sampai\": 65535}]},",
            "    {\"jenis\": \"database\", \"nama\": \"pesanan\", \"enkripsi\": true, \"backup_hari\": 1}",
            "  ]",
            "",
            "Keluaran yang diharapkan:",
            "FAILED  ATR-01  bucket.foto-produk  bucket tidak boleh publik",
            "PASSED  ATR-01  bucket.cadangan  bucket tidak boleh publik",
            "PASSED  ATR-02  bucket.foto-produk  bucket wajib terenkripsi",
            "FAILED  ATR-02  bucket.cadangan  bucket wajib terenkripsi",
            "PASSED  ATR-03  security_group.web  port 22 tidak boleh terbuka ke internet",
            "FAILED  ATR-03  security_group.lama  port 22 tidak boleh terbuka ke internet",
            "PASSED  ATR-04  database.pesanan  database wajib terenkripsi",
            "FAILED  ATR-05  database.pesanan  backup database minimal 7 hari",
            "Lulus: 4, Gagal: 4",
            "Gerbang: GAGAL",
            "",
            "Kalau tidak ada yang gagal, baris terakhir berbunyi Gerbang: LULUS.",
            "Sumber daya yang medannya tidak ada dianggap tidak aman (enkripsi",
            "tidak ada = gagal, backup_hari tidak ada = 0).",
        ],
        "hints": [
            "Pisahkan tiap aturan jadi fungsi kecil yang menerima satu sumber daya dan mengembalikan True kalau aman.",
            "Simpan aturan dalam daftar tuple (ID, jenis, judul, fungsi), lalu buat dua perulangan: luar untuk aturan, dalam untuk sumber daya.",
            "Pakai r.get('enkripsi') is True dan r.get('backup_hari', 0) supaya medan yang hilang dianggap gagal.",
            "Format status dengan f\"{status:6}\" supaya PASSED dan FAILED sama lebarnya.",
        ],
        "solution": """import json
import sys


def bucket_tidak_publik(r):
    return r.get("acl") not in ("public-read", "public-read-write")


def bucket_terenkripsi(r):
    return r.get("enkripsi") is True


def ssh_tidak_terbuka(r):
    for aturan in r.get("ingress", []):
        terbuka = aturan["cidr"] in ("0.0.0.0/0", "::/0")
        if terbuka and aturan["dari"] <= 22 <= aturan["sampai"]:
            return False
    return True


def db_terenkripsi(r):
    return r.get("enkripsi") is True


def db_ada_backup(r):
    return r.get("backup_hari", 0) >= 7


ATURAN = [
    ("ATR-01", "bucket", "bucket tidak boleh publik", bucket_tidak_publik),
    ("ATR-02", "bucket", "bucket wajib terenkripsi", bucket_terenkripsi),
    ("ATR-03", "security_group", "port 22 tidak boleh terbuka ke internet",
     ssh_tidak_terbuka),
    ("ATR-04", "database", "database wajib terenkripsi", db_terenkripsi),
    ("ATR-05", "database", "backup database minimal 7 hari", db_ada_backup),
]

sumber_daya = json.load(sys.stdin)
lulus = gagal = 0
for kode, jenis, judul, cek in ATURAN:
    for r in sumber_daya:
        if r["jenis"] != jenis:
            continue
        if cek(r):
            status = "PASSED"
            lulus += 1
        else:
            status = "FAILED"
            gagal += 1
        print(f"{status:6}  {kode}  {jenis}.{r['nama']}  {judul}")
print(f"Lulus: {lulus}, Gagal: {gagal}")
print("Gerbang: " + ("GAGAL" if gagal else "LULUS"))
""",
        "stdin_list": [
            """[
  {"jenis": "bucket", "nama": "foto-produk", "acl": "public-read", "enkripsi": true},
  {"jenis": "bucket", "nama": "cadangan", "acl": "private", "enkripsi": false},
  {"jenis": "security_group", "nama": "web", "ingress": [
    {"cidr": "0.0.0.0/0", "dari": 443, "sampai": 443},
    {"cidr": "10.0.0.0/16", "dari": 22, "sampai": 22}]},
  {"jenis": "security_group", "nama": "lama", "ingress": [
    {"cidr": "0.0.0.0/0", "dari": 0, "sampai": 65535}]},
  {"jenis": "database", "nama": "pesanan", "enkripsi": true, "backup_hari": 1}
]
""",
            """[
  {"jenis": "bucket", "nama": "laporan", "acl": "private", "enkripsi": true},
  {"jenis": "database", "nama": "akun", "enkripsi": true, "backup_hari": 14},
  {"jenis": "database", "nama": "uji"}
]
""",
        ],
    },
    {
        "title": "Latihan 15: Laporan Port Terbuka dari Hasil Pemindaian",
        "difficulty": "Lanjut",
        "question": [
            "Kamu punya hasil pemindaian Nmap format grepable dari jaringan lab",
            "sendiri (192.168.56.0/24) dan daftar port yang diizinkan per host.",
            "Buat program yang mencetak port mana yang harus ditutup.",
            "",
            "Masukan dari stdin terdiri dari dua bagian, [hasil] dan [izin].",
            "",
            "Bagian [hasil] berisi baris keluaran nmap -oG. Abaikan baris yang",
            "diawali # dan baris yang tidak memuat Ports:. Baris yang penting",
            "berbentuk (di berkas aslinya, pemisah kolomnya karakter tab):",
            "  Host: <ip> (<nama>)  Ports: <port>, <port>, ...  Ignored State: ...",
            "Tiap <port> berbentuk nomor/status/protokol//layanan//versi/",
            "(kolom ke-4 dan ke-6 kosong). Ambil hanya port berstatus open.",
            "",
            "Bagian [izin] berisi baris: <nama> <port/protokol> <port/protokol> ...",
            "",
            "Aturan laporan:",
            "  - Host diurutkan menurut alamat IP secara numerik",
            "    (192.168.56.5 sebelum 192.168.56.10). Pakai modul ipaddress.",
            "  - Baris kepala host: <ip> <nama>. Kalau nama host tidak ada di",
            "    [izin], tambahkan \": tidak ada di daftar izin\".",
            "  - Di bawahnya, port open yang tidak diizinkan, urut menurut",
            "    nomor port, dengan format \"  TUTUP <port>/<proto> <layanan>",
            "    <versi>\" (tanpa spasi di ujung kalau versi kosong). Untuk host",
            "    yang tidak terdaftar, labelnya TINJAU, bukan TUTUP.",
            "  - Kalau tidak ada port yang dilaporkan, cetak",
            "    \"  aman: semua port terbuka ada di daftar izin\".",
            "  - Baris terakhir: Ringkasan: <h> host, <t> port harus ditutup,",
            "    <r> port perlu ditinjau.",
            "",
            "Contoh masukan (tab ditampilkan sebagai dua spasi):",
            "  [hasil]",
            "  # Nmap 7.992 scan initiated as: nmap -sV -oG lab.gnmap 192.168.56.0/24",
            "  Host: 192.168.56.10 (web-lab)  Status: Up",
            "  Host: 192.168.56.10 (web-lab)  Ports: 22/open/tcp//ssh//OpenSSH 9.6/, 80/open/tcp//http//nginx 1.26/, 3306/open/tcp//mysql//MySQL 8.0/, 8080/filtered/tcp//http-proxy///  Ignored State: closed (996)",
            "  Host: 192.168.56.20 (db-lab)  Status: Up",
            "  Host: 192.168.56.20 (db-lab)  Ports: 22/open/tcp//ssh//OpenSSH 9.6/, 5432/open/tcp//postgresql//PostgreSQL/  Ignored State: closed (998)",
            "  Host: 192.168.56.5 (router-lab)  Status: Up",
            "  Host: 192.168.56.5 (router-lab)  Ports: 53/open/udp//domain///, 80/open/tcp//http//lighttpd/  Ignored State: closed (998)",
            "  # Nmap done: 256 IP addresses (3 hosts up) scanned in 41.20 seconds",
            "  [izin]",
            "  web-lab 22/tcp 80/tcp 443/tcp",
            "  db-lab 22/tcp 5432/tcp",
            "",
            "Keluaran yang diharapkan:",
            "192.168.56.5 router-lab: tidak ada di daftar izin",
            "  TINJAU 53/udp domain",
            "  TINJAU 80/tcp http lighttpd",
            "192.168.56.10 web-lab",
            "  TUTUP 3306/tcp mysql MySQL 8.0",
            "192.168.56.20 db-lab",
            "  aman: semua port terbuka ada di daftar izin",
            "Ringkasan: 3 host, 1 port harus ditutup, 2 port perlu ditinjau",
        ],
        "hints": [
            "Baca semua baris dulu, lalu pisahkan menurut bagian [hasil] dan [izin] dengan variabel penanda bagian yang sedang dibaca.",
            "Ambil ip dan nama dengan re.match(r\"Host: (\\S+) \\(([^)]*)\\)\", baris), lalu potong teks sesudah Ports: sampai sebelum Ignored State:.",
            "Pecah teks port dengan koma, lalu tiap port dengan garis miring: kolom 0 nomor, 1 status, 2 protokol, 4 layanan, 6 versi.",
            "Urutkan host dengan sorted(host, key=ipaddress.ip_address), dan bandingkan f\"{port}/{proto}\" dengan himpunan izin host itu.",
        ],
        "solution": "import ipaddress\nimport re\nimport sys\n\nhost = {}       # ip -> (nama, [(port, proto, layanan, versi)])\nizin = {}       # nama -> set(\"22/tcp\", ...)\nbagian = None\nfor baris in sys.stdin.read().splitlines():\n    baris = baris.strip()\n    if baris in (\"[hasil]\", \"[izin]\"):\n        bagian = baris\n        continue\n    if not baris or baris.startswith(\"#\"):\n        continue\n    if bagian == \"[izin]\":\n        nama, *port = baris.split()\n        izin[nama] = set(port)\n        continue\n    cocok = re.match(r\"Host: (\\S+) \\(([^)]*)\\)\", baris)\n    if not cocok or \"Ports:\" not in baris:\n        continue\n    ip, nama = cocok.groups()\n    teks = baris.split(\"Ports:\", 1)[1].split(\"Ignored State:\")[0].strip()\n    daftar = []\n    for isian in teks.split(\",\"):\n        kolom = isian.strip().split(\"/\")\n        port, status, proto, layanan, versi = kolom[0], kolom[1], kolom[2], kolom[4], kolom[6]\n        if status == \"open\":\n            daftar.append((int(port), proto, layanan, versi))\n    host[ip] = (nama, daftar)\n\ntotal_tutup = total_tinjau = 0\nfor ip in sorted(host, key=ipaddress.ip_address):\n    nama, daftar = host[ip]\n    if nama not in izin:\n        print(f\"{ip} {nama}: tidak ada di daftar izin\")\n    else:\n        print(f\"{ip} {nama}\")\n    boleh = izin.get(nama, set())\n    tutup = [p for p in sorted(daftar) if f\"{p[0]}/{p[1]}\" not in boleh]\n    label = \"TUTUP\" if nama in izin else \"TINJAU\"\n    for port, proto, layanan, versi in tutup:\n        print(f\"  {label} {port}/{proto} {layanan} {versi}\".rstrip())\n    if not tutup:\n        print(\"  aman: semua port terbuka ada di daftar izin\")\n    if nama in izin:\n        total_tutup += len(tutup)\n    else:\n        total_tinjau += len(tutup)\nprint(f\"Ringkasan: {len(host)} host, {total_tutup} port harus ditutup, \"\n      f\"{total_tinjau} port perlu ditinjau\")\n",
        "stdin": """[hasil]
# Nmap 7.992 scan initiated as: nmap -sV -oG lab.gnmap 192.168.56.0/24
Host: 192.168.56.10 (web-lab)	Status: Up
Host: 192.168.56.10 (web-lab)	Ports: 22/open/tcp//ssh//OpenSSH 9.6/, 80/open/tcp//http//nginx 1.26/, 3306/open/tcp//mysql//MySQL 8.0/, 8080/filtered/tcp//http-proxy///	Ignored State: closed (996)
Host: 192.168.56.20 (db-lab)	Status: Up
Host: 192.168.56.20 (db-lab)	Ports: 22/open/tcp//ssh//OpenSSH 9.6/, 5432/open/tcp//postgresql//PostgreSQL/	Ignored State: closed (998)
Host: 192.168.56.5 (router-lab)	Status: Up
Host: 192.168.56.5 (router-lab)	Ports: 53/open/udp//domain///, 80/open/tcp//http//lighttpd/	Ignored State: closed (998)
# Nmap done: 256 IP addresses (3 hosts up) scanned in 41.20 seconds
[izin]
web-lab 22/tcp 80/tcp 443/tcp
db-lab 22/tcp 5432/tcp
""",
    },
    {
        "title": "Latihan 16: Pemindai Log Brute Force",
        "difficulty": "Lanjut",
        "question": [
            "Buat pemindai log autentikasi SSH. Program membaca baris auth.log",
            "tiruan dari stdin (sudah urut waktu) dan mencetak alert.",
            "",
            "Baris yang penting berbentuk:",
            "  Oct 19 10:00:01 web1 sshd[1201]: Failed password for budi from 203.0.113.7 port 50122 ssh2",
            "  Oct 19 10:00:15 web1 sshd[1202]: Failed password for invalid user admin from 203.0.113.7 port 50130 ssh2",
            "  Oct 19 10:01:30 web1 sshd[1205]: Accepted password for budi from 203.0.113.7 port 50160 ssh2",
            "Abaikan baris lain.",
            "",
            "Tiga aturan:",
            "  USER_TIDAK_ADA        Failed password for invalid user X. Laporkan",
            "                        sekali per pasangan (IP, user).",
            "  BRUTE_FORCE           sebuah IP punya lebih dari 5 login gagal",
            "                        dalam 60 detik (jendela geser: kegagalan",
            "                        yang waktunya >= sekarang - 60 detik ikut",
            "                        dihitung). Laporkan sekali per IP, saat",
            "                        syaratnya pertama kali terpenuhi.",
            "  SUKSES_SETELAH_GAGAL  login Accepted dari IP yang sudah kena",
            "                        BRUTE_FORCE.",
            "",
            "Format alert, satu per baris sesuai urutan kejadian:",
            "  <jam> USER_TIDAK_ADA <ip> user <user>",
            "  <jam> BRUTE_FORCE <ip> <n> gagal dalam 60 detik",
            "  <jam> SUKSES_SETELAH_GAGAL <ip> user <user>",
            "Kalau satu baris memicu USER_TIDAK_ADA dan BRUTE_FORCE sekaligus,",
            "cetak USER_TIDAK_ADA dulu. Baris terakhir adalah ringkasan.",
            "Tanggal di log tidak punya tahun; ubah bulan, tanggal, dan jam jadi",
            "hitungan detik sendiri, jangan pakai strptime tanpa tahun.",
            "",
            "Masukan contoh berisi 18 baris: sari salah dua kali lalu berhasil",
            "(normal), 203.0.113.7 menebak cepat lalu berhasil, dan",
            "198.51.100.9 menebak pelan, satu kali tiap 50 detik.",
            "",
            "Keluaran yang diharapkan:",
            "10:00:15 USER_TIDAK_ADA 203.0.113.7 user admin",
            "10:00:52 BRUTE_FORCE 203.0.113.7 6 gagal dalam 60 detik",
            "10:01:30 SUKSES_SETELAH_GAGAL 203.0.113.7 user budi",
            "10:03:00 USER_TIDAK_ADA 198.51.100.9 user oracle",
            "10:04:40 USER_TIDAK_ADA 198.51.100.9 user test",
            "Ringkasan: BRUTE_FORCE=1, SUKSES_SETELAH_GAGAL=1, USER_TIDAK_ADA=3",
            "",
            "Perhatikan 198.51.100.9 tidak kena BRUTE_FORCE walaupun gagal tujuh",
            "kali. Penyerang yang sabar bisa lolos dari jendela pendek.",
        ],
        "hints": [
            "Satu regex bisa menangkap bulan, tanggal, jam, menit, detik, Failed atau Accepted, kata 'invalid user' yang opsional, nama user, dan IP.",
            "Untuk jendela geser, simpan waktu kegagalan per IP di collections.deque, lalu buang dari depan selama waktunya lebih kecil dari sekarang - 60.",
            "Pakai himpunan untuk IP yang sudah ditandai BRUTE_FORCE dan pasangan (ip, user) yang sudah dilaporkan, supaya alert tidak berulang.",
            "Detik bisa dihitung sebagai (((bulan * 31 + tanggal) * 24 + jam) * 60 + menit) * 60 + detik; angkanya cuma dipakai untuk membandingkan.",
        ],
        "solution": "import re\nimport sys\nfrom collections import defaultdict, deque\n\nBULAN = {\"Jan\": 1, \"Feb\": 2, \"Mar\": 3, \"Apr\": 4, \"May\": 5, \"Jun\": 6,\n         \"Jul\": 7, \"Aug\": 8, \"Sep\": 9, \"Oct\": 10, \"Nov\": 11, \"Dec\": 12}\nPOLA = re.compile(\n    r\"^(\\w{3}) +(\\d+) (\\d\\d):(\\d\\d):(\\d\\d) \\S+ sshd\\[\\d+\\]: \"\n    r\"(Failed|Accepted) password for (invalid user )?(\\S+) from (\\S+) port\")\n\ngagal = defaultdict(deque)   # ip -> waktu gagal dalam 60 detik terakhir\nditandai = set()             # ip yang sudah kena BRUTE_FORCE\nuser_asing = set()           # (ip, user) yang sudah dilaporkan\njumlah = defaultdict(int)\n\nfor baris in sys.stdin:\n    m = POLA.match(baris)\n    if not m:\n        continue\n    bln, tgl, jam, mnt, dtk, hasil, invalid, user, ip = m.groups()\n    detik = (((BULAN[bln] * 31 + int(tgl)) * 24 + int(jam)) * 60 + int(mnt)) * 60 + int(dtk)\n    waktu = f\"{jam}:{mnt}:{dtk}\"\n    if hasil == \"Failed\":\n        if invalid and (ip, user) not in user_asing:\n            user_asing.add((ip, user))\n            print(f\"{waktu} USER_TIDAK_ADA {ip} user {user}\")\n            jumlah[\"USER_TIDAK_ADA\"] += 1\n        antre = gagal[ip]\n        antre.append(detik)\n        while antre[0] < detik - 60:\n            antre.popleft()\n        if len(antre) > 5 and ip not in ditandai:\n            ditandai.add(ip)\n            print(f\"{waktu} BRUTE_FORCE {ip} {len(antre)} gagal dalam 60 detik\")\n            jumlah[\"BRUTE_FORCE\"] += 1\n    elif ip in ditandai:\n        print(f\"{waktu} SUKSES_SETELAH_GAGAL {ip} user {user}\")\n        jumlah[\"SUKSES_SETELAH_GAGAL\"] += 1\n\nprint(\"Ringkasan:\", \", \".join(f\"{k}={jumlah[k]}\" for k in\n      (\"BRUTE_FORCE\", \"SUKSES_SETELAH_GAGAL\", \"USER_TIDAK_ADA\")))",
        "stdin": """Oct 19 09:58:10 web1 sshd[1100]: Failed password for sari from 192.0.2.15 port 41000 ssh2
Oct 19 09:58:20 web1 sshd[1100]: Failed password for sari from 192.0.2.15 port 41002 ssh2
Oct 19 09:58:31 web1 sshd[1101]: Accepted password for sari from 192.0.2.15 port 41004 ssh2
Oct 19 10:00:01 web1 sshd[1201]: Failed password for budi from 203.0.113.7 port 50122 ssh2
Oct 19 10:00:09 web1 sshd[1201]: Failed password for budi from 203.0.113.7 port 50124 ssh2
Oct 19 10:00:15 web1 sshd[1202]: Failed password for invalid user admin from 203.0.113.7 port 50130 ssh2
Oct 19 10:00:22 web1 sshd[1202]: Failed password for budi from 203.0.113.7 port 50131 ssh2
Oct 19 10:00:40 web1 sshd[1203]: Failed password for budi from 203.0.113.7 port 50140 ssh2
Oct 19 10:00:52 web1 sshd[1203]: Failed password for budi from 203.0.113.7 port 50142 ssh2
Oct 19 10:00:58 web1 sshd[1204]: Failed password for budi from 203.0.113.7 port 50150 ssh2
Oct 19 10:01:30 web1 sshd[1205]: Accepted password for budi from 203.0.113.7 port 50160 ssh2
Oct 19 10:03:00 web1 sshd[1300]: Failed password for invalid user oracle from 198.51.100.9 port 60001 ssh2
Oct 19 10:03:50 web1 sshd[1301]: Failed password for invalid user oracle from 198.51.100.9 port 60002 ssh2
Oct 19 10:04:40 web1 sshd[1302]: Failed password for invalid user test from 198.51.100.9 port 60003 ssh2
Oct 19 10:05:30 web1 sshd[1303]: Failed password for root from 198.51.100.9 port 60004 ssh2
Oct 19 10:06:20 web1 sshd[1304]: Failed password for root from 198.51.100.9 port 60005 ssh2
Oct 19 10:07:10 web1 sshd[1305]: Failed password for root from 198.51.100.9 port 60006 ssh2
Oct 19 10:08:00 web1 sshd[1306]: Failed password for root from 198.51.100.9 port 60007 ssh2
""",
    },
    {
        "title": "Latihan 17: Garis Waktu Insiden dari Beberapa Log",
        "difficulty": "Sulit",
        "question": [
            "Saat insiden, kamu harus menggabungkan log dari beberapa sistem",
            "yang menulis waktu dengan cara berbeda. Buat program yang",
            "menyusun garis waktu untuk satu IP mencurigakan.",
            "",
            "Masukan dari stdin:",
            "  - Baris ip_curiga=<ip>.",
            "  - Bagian [web]: log akses nginx, waktu lokal dengan zona waktu.",
            "      203.0.113.7 - - [19/Oct/2026:17:02:11 +0700] \"POST /login HTTP/1.1\" 401 512",
            "  - Bagian [auth]: waktu ISO 8601 dalam UTC.",
            "      2026-10-19T10:04:55Z login_sukses user=budi ip=203.0.113.7",
            "  - Bagian [audit]: waktu berupa detik sejak epoch Unix (UTC).",
            "      1792404543 user=budi aksi=ekspor objek=pelanggan.csv",
            "",
            "Aturan:",
            "  1. Ambil semua kejadian web dan auth dari ip_curiga. Isi kejadian",
            "     web: \"<metode> <jalur> <status>\", isi auth: nama kejadiannya.",
            "  2. Pengguna terdampak = user yang punya login_sukses dari",
            "     ip_curiga.",
            "  3. Ambil kejadian audit milik pengguna terdampak yang waktunya",
            "     sama dengan atau sesudah kejadian pertama dari ip_curiga.",
            "     Isinya: \"<aksi> <objek>\".",
            "  4. Ubah semua waktu ke UTC, lalu urutkan menurut waktu. Kalau",
            "     waktunya sama, urutkan menurut nama sumber (audit, auth, web).",
            "  5. Kolom \"siapa\": IP untuk web, user untuk auth dan audit.",
            "",
            "Format baris: <YYYY-MM-DD HH:MM:SS>Z, dua spasi, sumber dirapatkan",
            "kiri selebar 6, siapa dirapatkan kiri selebar 13, lalu isinya.",
            "Ditutup baris pengguna terdampak dan rentang waktu.",
            "",
            "Contoh masukan:",
            "  ip_curiga=203.0.113.7",
            "  [web]",
            "  198.51.100.20 - - [19/Oct/2026:16:59:58 +0700] \"GET / HTTP/1.1\" 200 5120",
            "  203.0.113.7 - - [19/Oct/2026:17:02:11 +0700] \"POST /login HTTP/1.1\" 401 512",
            "  203.0.113.7 - - [19/Oct/2026:17:02:19 +0700] \"POST /login HTTP/1.1\" 401 512",
            "  203.0.113.7 - - [19/Oct/2026:17:04:55 +0700] \"POST /login HTTP/1.1\" 200 734",
            "  203.0.113.7 - - [19/Oct/2026:17:08:30 +0700] \"GET /admin/ekspor HTTP/1.1\" 200 88211",
            "  [auth]",
            "  2026-10-19T10:02:11Z login_gagal user=budi ip=203.0.113.7",
            "  2026-10-19T10:02:19Z login_gagal user=budi ip=203.0.113.7",
            "  2026-10-19T10:04:55Z login_sukses user=budi ip=203.0.113.7",
            "  2026-10-19T10:06:00Z login_sukses user=sari ip=192.0.2.15",
            "  [audit]",
            "  1792402200 user=budi aksi=ubah_profil objek=budi",
            "  1792404312 user=budi aksi=tambah_kunci_api objek=kunci-7",
            "  1792404465 user=sari aksi=lihat objek=laporan-oktober",
            "  1792404543 user=budi aksi=ekspor objek=pelanggan.csv",
            "",
            "Keluaran yang diharapkan:",
            "Garis waktu untuk 203.0.113.7 (UTC)",
            "2026-10-19 10:02:11Z  auth  budi         login_gagal",
            "2026-10-19 10:02:11Z  web   203.0.113.7  POST /login 401",
            "2026-10-19 10:02:19Z  auth  budi         login_gagal",
            "2026-10-19 10:02:19Z  web   203.0.113.7  POST /login 401",
            "2026-10-19 10:04:55Z  auth  budi         login_sukses",
            "2026-10-19 10:04:55Z  web   203.0.113.7  POST /login 200",
            "2026-10-19 10:05:12Z  audit budi         tambah_kunci_api kunci-7",
            "2026-10-19 10:08:30Z  web   203.0.113.7  GET /admin/ekspor 200",
            "2026-10-19 10:09:03Z  audit budi         ekspor pelanggan.csv",
            "Pengguna terdampak: budi",
            "Rentang: 10:02:11Z sampai 10:09:03Z",
            "",
            "Audit ubah_profil pukul 09:30 tidak ikut karena terjadi sebelum",
            "IP itu muncul pertama kali.",
        ],
        "hints": [
            "Simpan setiap kejadian sebagai tuple yang diawali objek datetime ber-zona waktu, supaya sorted() mengurutkan dengan benar.",
            "datetime.strptime dengan format \"%d/%b/%Y:%H:%M:%S %z\" membaca waktu nginx beserta zonanya, lalu .astimezone(timezone.utc) mengubahnya ke UTC.",
            "Untuk ISO 8601, ganti akhiran Z jadi +00:00 sebelum datetime.fromisoformat; untuk epoch, pakai datetime.fromtimestamp(detik, timezone.utc).",
            "Susun tuple (waktu, sumber, siapa, isi) supaya waktu yang sama otomatis diurutkan menurut nama sumber.",
        ],
        "solution": "import re\nimport sys\nfrom datetime import datetime, timezone\n\nWEB = re.compile(r'^(\\S+) \\S+ \\S+ \\[([^\\]]+)\\] \"(\\S+) (\\S+) [^\"]*\" (\\d{3})')\nAUTH = re.compile(r\"^(\\S+) (\\S+) user=(\\S+) ip=(\\S+)\")\nAUDIT = re.compile(r\"^(\\d+) user=(\\S+) aksi=(\\S+) objek=(\\S+)\")\n\nip_curiga = None\nbagian = None\nweb, auth, audit = [], [], []\nfor baris in sys.stdin.read().splitlines():\n    baris = baris.strip()\n    if not baris:\n        continue\n    if baris.startswith(\"ip_curiga=\"):\n        ip_curiga = baris.split(\"=\", 1)[1]\n    elif baris in (\"[web]\", \"[auth]\", \"[audit]\"):\n        bagian = baris\n    elif bagian == \"[web]\":\n        ip, waktu, metode, jalur, status = WEB.match(baris).groups()\n        t = datetime.strptime(waktu, \"%d/%b/%Y:%H:%M:%S %z\")\n        web.append((t.astimezone(timezone.utc), ip, f\"{metode} {jalur} {status}\"))\n    elif bagian == \"[auth]\":\n        waktu, kejadian, user, ip = AUTH.match(baris).groups()\n        t = datetime.fromisoformat(waktu.replace(\"Z\", \"+00:00\"))\n        auth.append((t, ip, user, kejadian))\n    elif bagian == \"[audit]\":\n        detik, user, aksi, objek = AUDIT.match(baris).groups()\n        t = datetime.fromtimestamp(int(detik), timezone.utc)\n        audit.append((t, user, f\"{aksi} {objek}\"))\n\nkejadian = []\nfor t, ip, isi in web:\n    if ip == ip_curiga:\n        kejadian.append((t, \"web\", ip, isi))\npengguna = set()\nfor t, ip, user, isi in auth:\n    if ip == ip_curiga:\n        kejadian.append((t, \"auth\", user, isi))\n        if isi == \"login_sukses\":\n            pengguna.add(user)\nmulai = min(t for t, *_ in kejadian)\nfor t, user, isi in audit:\n    if user in pengguna and t >= mulai:\n        kejadian.append((t, \"audit\", user, isi))\n\nkejadian.sort()\nprint(f\"Garis waktu untuk {ip_curiga} (UTC)\")\nfor t, sumber, siapa, isi in kejadian:\n    print(f\"{t:%Y-%m-%d %H:%M:%S}Z  {sumber:6}{siapa:13}{isi}\")\nprint(\"Pengguna terdampak:\", \", \".join(sorted(pengguna)) or \"-\")\nprint(f\"Rentang: {kejadian[0][0]:%H:%M:%S}Z sampai {kejadian[-1][0]:%H:%M:%S}Z\")",
        "stdin": """ip_curiga=203.0.113.7
[web]
198.51.100.20 - - [19/Oct/2026:16:59:58 +0700] "GET / HTTP/1.1" 200 5120
203.0.113.7 - - [19/Oct/2026:17:02:11 +0700] "POST /login HTTP/1.1" 401 512
203.0.113.7 - - [19/Oct/2026:17:02:19 +0700] "POST /login HTTP/1.1" 401 512
203.0.113.7 - - [19/Oct/2026:17:04:55 +0700] "POST /login HTTP/1.1" 200 734
203.0.113.7 - - [19/Oct/2026:17:08:30 +0700] "GET /admin/ekspor HTTP/1.1" 200 88211
[auth]
2026-10-19T10:02:11Z login_gagal user=budi ip=203.0.113.7
2026-10-19T10:02:19Z login_gagal user=budi ip=203.0.113.7
2026-10-19T10:04:55Z login_sukses user=budi ip=203.0.113.7
2026-10-19T10:06:00Z login_sukses user=sari ip=192.0.2.15
[audit]
1792402200 user=budi aksi=ubah_profil objek=budi
1792404312 user=budi aksi=tambah_kunci_api objek=kunci-7
1792404465 user=sari aksi=lihat objek=laporan-oktober
1792404543 user=budi aksi=ekspor objek=pelanggan.csv
""",
    },
    {
        "title": "Latihan 18: Proyek Akhir: Auditor Keamanan Aplikasi Mini",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir kurikulum ini menggabungkan pemeriksaan dari bab 02",
            "sampai bab 09 jadi satu auditor kecil. Program membaca satu",
            "berkas teks berbagian dari stdin, lalu mencetak laporan temuan",
            "urut tingkat keparahan dan skor akhir.",
            "",
            "Baris sebelum bagian pertama (misalnya komentar # audit ...)",
            "diabaikan. Baris kosong diabaikan. Ada enam bagian:",
            "",
            "[header] respons HTTP. Baris pertama baris status, sisanya",
            "Nama: nilai (nama header tidak peka huruf besar-kecil).",
            "  SEDANG  Content-Security-Policy tidak ada",
            "  SEDANG  Strict-Transport-Security tidak ada",
            "  RENDAH  max-age HSTS kurang dari 180 hari",
            "          (kalau max-age=N ada dan N < 15552000, atau tidak ada)",
            "  RENDAH  X-Content-Type-Options bukan nosniff",
            "  SEDANG  cookie <nama> tanpa Secure      (per Set-Cookie)",
            "  SEDANG  cookie <nama> tanpa HttpOnly",
            "  RENDAH  cookie <nama> tanpa SameSite",
            "",
            "[pengguna] baris <nama> <simpanan>.",
            "  SEDANG  <nama>: iterasi PBKDF2 <n> < 600000",
            "          (simpanan pbkdf2_sha256$<iterasi>$<salt>$<hash>)",
            "  TINGGI  <nama>: hash MD5 tanpa salt   (tepat 32 digit heksa)",
            "  KRITIS  <nama>: password disimpan polos   (selain dua di atas)",
            "",
            "[peran] baris peran <nama> = izin1, izin2 dan <user> = <peran>.",
            "",
            "[kode] potongan kode sumber, nomor baris dihitung dari 1 di",
            "bagian ini. Nilai rahasia disamarkan: 4 huruf pertama, ...,",
            "4 huruf terakhir.",
            "  KRITIS  baris <n>: kunci akses AWS <samaran>   (AKIA + 16 huruf",
            "          kapital/angka)",
            "  KRITIS  baris <n>: private key tertanam",
            "          (-----BEGIN ... PRIVATE KEY-----)",
            "  TINGGI  baris <n>: <kata> tertanam <samaran>",
            "          (password, sandi, atau secret, boleh diikuti huruf lain,",
            "          lalu = \"nilai\"; <kata> ditulis huruf kecil)",
            "",
            "[log] baris t=<detik> <JENIS> kunci=nilai ...",
            "  TINGGI  t=<t>: brute force dari <ip>",
            "          (GAGAL lebih dari 5 kali dari satu IP dalam 60 detik,",
            "          jendela geser, sekali per IP)",
            "  KRITIS  t=<t>: <user> login sukses sesudah brute force",
            "          (SUKSES dari IP yang sudah kena brute force)",
            "  KRITIS  t=<t>: <user> (<peran>) berhasil <izin> tanpa izin",
            "          (AKSI hasil=200 yang izinnya tidak dimiliki perannya;",
            "          temuan ini dilaporkan dengan bagian peran)",
            "",
            "[dependensi] baris pakai <paket> <versi> dan advisori <paket>",
            "<versi_perbaikan> <TINGKAT> <kode>.",
            "  <TINGKAT>  <paket> <versi> rentan (<kode>), naikkan ke <perbaikan>",
            "          (kalau versi terpasang lebih kecil dari versi perbaikan;",
            "          bandingkan angka per bagian, bukan teks)",
            "",
            "Laporan: baris LAPORAN AUDIT KEAMANAN, lalu satu baris per temuan",
            "[<TINGKAT>] <bagian>: <pesan>, diurutkan KRITIS, TINGGI, SEDANG,",
            "RENDAH. Temuan setingkat mengikuti urutan pemeriksaan: header,",
            "pengguna, kode, log (termasuk temuan peran), dependensi. Skor =",
            "100 dikurangi 15 per KRITIS, 8 per TINGGI, 4 per SEDANG, 1 per",
            "RENDAH, paling kecil 0.",
            "",
            "Contoh masukan pertama:",
            "  # audit toko-ani v1",
            "  [header]",
            "  HTTP/1.1 200 OK",
            "  Content-Type: text/html; charset=utf-8",
            "  strict-transport-security: max-age=3600",
            "  X-Content-Type-Options: nosniff",
            "  Set-Cookie: sesi=a81f; Path=/; HttpOnly",
            "  [pengguna]",
            "  ani pbkdf2_sha256$600000$garam01$82396046d6aa012e85b098cf13e0f62bf27668f99bf657f360778049ce7e2b75",
            "  budi pbkdf2_sha256$100000$garam02$a4318a16bb44205f5ea58aabd36c03e25a5734681e2fa3799b5903ca5f89d1b1",
            "  citra 5f4dcc3b5aa765d61d8327deb882cf99",
            "  [peran]",
            "  peran pembaca = laporan:baca",
            "  peran editor = laporan:baca, laporan:ubah",
            "  peran admin = laporan:baca, laporan:ubah, pengguna:hapus",
            "  ani = admin",
            "  budi = editor",
            "  citra = pembaca",
            "  [kode]",
            "  import os",
            "  AWS_KEY = \"AKIAIOSFODNN7EXAMPLE\"",
            "  DB_PASSWORD = \"toko-ani-2026\"",
            "  API_TOKEN = os.environ[\"API_TOKEN\"]",
            "  [log]",
            "  t=100 GAGAL ip=203.0.113.7 user=ani",
            "  t=108 GAGAL ip=203.0.113.7 user=ani",
            "  t=115 GAGAL ip=203.0.113.7 user=ani",
            "  t=121 GAGAL ip=203.0.113.7 user=ani",
            "  t=130 GAGAL ip=203.0.113.7 user=ani",
            "  t=139 GAGAL ip=203.0.113.7 user=ani",
            "  t=170 SUKSES ip=203.0.113.7 user=ani",
            "  t=300 AKSI user=citra izin=pengguna:hapus hasil=200",
            "  t=310 AKSI user=budi izin=laporan:ubah hasil=200",
            "  t=320 AKSI user=citra izin=laporan:ubah hasil=403",
            "  [dependensi]",
            "  pakai requests 2.31.0",
            "  pakai jinja2 3.1.6",
            "  advisori requests 2.32.4 TINGGI ADV-001",
            "  advisori jinja2 3.1.5 SEDANG ADV-002",
            "",
            "Keluaran yang diharapkan:",
            "LAPORAN AUDIT KEAMANAN",
            "[KRITIS] kode: baris 2: kunci akses AWS AKIA...MPLE",
            "[KRITIS] log: t=170: ani login sukses sesudah brute force",
            "[KRITIS] peran: t=300: citra (pembaca) berhasil pengguna:hapus tanpa izin",
            "[TINGGI] pengguna: citra: hash MD5 tanpa salt",
            "[TINGGI] kode: baris 3: password tertanam toko...2026",
            "[TINGGI] log: t=139: brute force dari 203.0.113.7",
            "[TINGGI] dependensi: requests 2.31.0 rentan (ADV-001), naikkan ke 2.32.4",
            "[SEDANG] header: Content-Security-Policy tidak ada",
            "[SEDANG] header: cookie sesi tanpa Secure",
            "[SEDANG] pengguna: budi: iterasi PBKDF2 100000 < 600000",
            "[RENDAH] header: max-age HSTS kurang dari 180 hari",
            "[RENDAH] header: cookie sesi tanpa SameSite",
            "Skor: 9/100 (KRITIS=3 TINGGI=4 SEDANG=3 RENDAH=2)",
            "",
            "Masukan kedua adalah versi sesudah diperbaiki, diawali",
            "# audit toko-ani v2. Cookie-nya masih belum memakai SameSite.",
            "",
            "Untuk input # audit toko-ani v2, keluarannya:",
            "LAPORAN AUDIT KEAMANAN",
            "[RENDAH] header: cookie sesi tanpa SameSite",
            "Skor: 99/100 (KRITIS=0 TINGGI=0 SEDANG=0 RENDAH=1)",
        ],
        "hints": [
            "Pecah pekerjaan jadi fungsi kecil per bagian, dan biarkan semuanya memanggil satu fungsi lapor(tingkat, bagian, pesan) yang menambah ke daftar temuan.",
            "Baca dulu seluruh masukan jadi dict nama bagian -> daftar baris, dengan re.fullmatch(r\"\\[(\\w+)\\]\", baris) untuk mengenali kepala bagian.",
            "Bagian peran harus dibaca sebelum log, karena pemeriksaan AKSI butuh peta user -> peran -> himpunan izin.",
            "Untuk brute force, pakai lagi pola deque jendela geser dari latihan pemindai log; untuk versi, ubah \"2.31.0\" jadi tuple (2, 31, 0) sebelum dibandingkan.",
            "Urutkan dengan sorted(temuan, key=lambda x: TINGKAT.index(x[0])); sorted di Python stabil, jadi urutan pemeriksaan untuk tingkat yang sama tetap terjaga.",
        ],
        "solution": "import re\nimport sys\nfrom collections import defaultdict, deque\n\nTINGKAT = [\"KRITIS\", \"TINGGI\", \"SEDANG\", \"RENDAH\"]\nBOBOT = {\"KRITIS\": 15, \"TINGGI\": 8, \"SEDANG\": 4, \"RENDAH\": 1}\ntemuan = []      # (tingkat, bagian, pesan), urutan ditemukan\n\n\ndef lapor(tingkat, bagian, pesan):\n    temuan.append((tingkat, bagian, pesan))\n\n\ndef baca_bagian(teks):\n    bagian, nama = defaultdict(list), None\n    for baris in teks.splitlines():\n        m = re.fullmatch(r\"\\[(\\w+)\\]\", baris.strip())\n        if m:\n            nama = m.group(1)\n        elif nama and baris.strip():\n            bagian[nama].append(baris.rstrip())\n    return bagian\n\n\ndef cek_header(baris):\n    header, cookie = {}, []\n    for b in baris[1:]:                       # baris pertama: status HTTP\n        nama, _, nilai = b.partition(\":\")\n        nama, nilai = nama.strip().lower(), nilai.strip()\n        if nama == \"set-cookie\":\n            cookie.append(nilai)\n        else:\n            header[nama] = nilai\n    if \"content-security-policy\" not in header:\n        lapor(\"SEDANG\", \"header\", \"Content-Security-Policy tidak ada\")\n    hsts = header.get(\"strict-transport-security\")\n    if hsts is None:\n        lapor(\"SEDANG\", \"header\", \"Strict-Transport-Security tidak ada\")\n    else:\n        m = re.search(r\"max-age=(\\d+)\", hsts)\n        if not m or int(m.group(1)) < 15552000:\n            lapor(\"RENDAH\", \"header\", \"max-age HSTS kurang dari 180 hari\")\n    if header.get(\"x-content-type-options\", \"\").lower() != \"nosniff\":\n        lapor(\"RENDAH\", \"header\", \"X-Content-Type-Options bukan nosniff\")\n    for c in cookie:\n        nama = c.split(\"=\", 1)[0]\n        atribut = [a.strip().lower() for a in c.split(\";\")[1:]]\n        if \"secure\" not in atribut:\n            lapor(\"SEDANG\", \"header\", f\"cookie {nama} tanpa Secure\")\n        if \"httponly\" not in atribut:\n            lapor(\"SEDANG\", \"header\", f\"cookie {nama} tanpa HttpOnly\")\n        if not any(a.startswith(\"samesite=\") for a in atribut):\n            lapor(\"RENDAH\", \"header\", f\"cookie {nama} tanpa SameSite\")\n\n\ndef cek_pengguna(baris):\n    for b in baris:\n        nama, simpanan = b.split()\n        bagian = simpanan.split(\"$\")\n        if len(bagian) == 4 and bagian[0] == \"pbkdf2_sha256\":\n            if int(bagian[1]) < 600000:\n                lapor(\"SEDANG\", \"pengguna\", f\"{nama}: iterasi PBKDF2 {bagian[1]} < 600000\")\n        elif re.fullmatch(r\"[0-9a-f]{32}\", simpanan):\n            lapor(\"TINGGI\", \"pengguna\", f\"{nama}: hash MD5 tanpa salt\")\n        else:\n            lapor(\"KRITIS\", \"pengguna\", f\"{nama}: password disimpan polos\")\n\n\ndef baca_peran(baris):\n    izin_peran, peran_user = {}, {}\n    for b in baris:\n        kiri, _, kanan = b.partition(\"=\")\n        kiri, kanan = kiri.strip(), kanan.strip()\n        if kiri.startswith(\"peran \"):\n            izin_peran[kiri[6:].strip()] = {x.strip() for x in kanan.split(\",\")}\n        else:\n            peran_user[kiri] = kanan\n    return izin_peran, peran_user\n\n\ndef samarkan(nilai):\n    return nilai[:4] + \"...\" + nilai[-4:]\n\n\ndef cek_kode(baris):\n    for no, b in enumerate(baris, 1):\n        for kunci in re.findall(r\"AKIA[0-9A-Z]{16}\", b):\n            lapor(\"KRITIS\", \"kode\", f\"baris {no}: kunci akses AWS {samarkan(kunci)}\")\n        if re.search(r\"-----BEGIN [A-Z ]*PRIVATE KEY-----\", b):\n            lapor(\"KRITIS\", \"kode\", f\"baris {no}: private key tertanam\")\n        m = re.search(r\"(password|sandi|secret)\\w*\\s*=\\s*\\\"([^\\\"]+)\\\"\", b, re.I)\n        if m:\n            lapor(\"TINGGI\", \"kode\", f\"baris {no}: {m.group(1).lower()} tertanam {samarkan(m.group(2))}\")\n\n\ndef cek_log(baris, izin_peran, peran_user):\n    gagal, ditandai = defaultdict(deque), set()\n    for b in baris:\n        medan = dict(x.split(\"=\", 1) for x in b.split() if \"=\" in x)\n        jenis = b.split()[1]\n        t = int(medan[\"t\"])\n        if jenis == \"GAGAL\":\n            antre = gagal[medan[\"ip\"]]\n            antre.append(t)\n            while antre[0] < t - 60:\n                antre.popleft()\n            if len(antre) > 5 and medan[\"ip\"] not in ditandai:\n                ditandai.add(medan[\"ip\"])\n                lapor(\"TINGGI\", \"log\", f\"t={t}: brute force dari {medan['ip']}\")\n        elif jenis == \"SUKSES\" and medan[\"ip\"] in ditandai:\n            lapor(\"KRITIS\", \"log\", f\"t={t}: {medan['user']} login sukses sesudah brute force\")\n        elif jenis == \"AKSI\" and medan[\"hasil\"] == \"200\":\n            peran = peran_user.get(medan[\"user\"])\n            if medan[\"izin\"] not in izin_peran.get(peran, set()):\n                lapor(\"KRITIS\", \"peran\", f\"t={t}: {medan['user']} ({peran}) berhasil {medan['izin']} tanpa izin\")\n\n\ndef versi(teks):\n    return tuple(int(x) for x in teks.split(\".\"))\n\n\ndef cek_dependensi(baris):\n    pakai, advisori = {}, []\n    for b in baris:\n        kolom = b.split()\n        if kolom[0] == \"pakai\":\n            pakai[kolom[1]] = kolom[2]\n        elif kolom[0] == \"advisori\":\n            advisori.append(kolom[1:])\n    for paket, perbaikan, tingkat, kode in advisori:\n        if paket in pakai and versi(pakai[paket]) < versi(perbaikan):\n            lapor(tingkat, \"dependensi\", f\"{paket} {pakai[paket]} rentan ({kode}), naikkan ke {perbaikan}\")\n\n\nbagian = baca_bagian(sys.stdin.read())\ncek_header(bagian[\"header\"])\ncek_pengguna(bagian[\"pengguna\"])\nizin_peran, peran_user = baca_peran(bagian[\"peran\"])\ncek_kode(bagian[\"kode\"])\ncek_log(bagian[\"log\"], izin_peran, peran_user)\ncek_dependensi(bagian[\"dependensi\"])\n\nprint(\"LAPORAN AUDIT KEAMANAN\")\nfor tingkat, bag, pesan in sorted(temuan, key=lambda x: TINGKAT.index(x[0])):\n    print(f\"[{tingkat}] {bag}: {pesan}\")\njumlah = {t: sum(1 for x in temuan if x[0] == t) for t in TINGKAT}\nskor = max(0, 100 - sum(BOBOT[t] * n for t, n in jumlah.items()))\nprint(f\"Skor: {skor}/100 (\" + \" \".join(f\"{t}={jumlah[t]}\" for t in TINGKAT) + \")\")",
        "stdin_list": [
            """# audit toko-ani v1
[header]
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
strict-transport-security: max-age=3600
X-Content-Type-Options: nosniff
Set-Cookie: sesi=a81f; Path=/; HttpOnly
[pengguna]
ani pbkdf2_sha256$600000$garam01$82396046d6aa012e85b098cf13e0f62bf27668f99bf657f360778049ce7e2b75
budi pbkdf2_sha256$100000$garam02$a4318a16bb44205f5ea58aabd36c03e25a5734681e2fa3799b5903ca5f89d1b1
citra 5f4dcc3b5aa765d61d8327deb882cf99
[peran]
peran pembaca = laporan:baca
peran editor = laporan:baca, laporan:ubah
peran admin = laporan:baca, laporan:ubah, pengguna:hapus
ani = admin
budi = editor
citra = pembaca
[kode]
import os
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "toko-ani-2026"
API_TOKEN = os.environ["API_TOKEN"]
[log]
t=100 GAGAL ip=203.0.113.7 user=ani
t=108 GAGAL ip=203.0.113.7 user=ani
t=115 GAGAL ip=203.0.113.7 user=ani
t=121 GAGAL ip=203.0.113.7 user=ani
t=130 GAGAL ip=203.0.113.7 user=ani
t=139 GAGAL ip=203.0.113.7 user=ani
t=170 SUKSES ip=203.0.113.7 user=ani
t=300 AKSI user=citra izin=pengguna:hapus hasil=200
t=310 AKSI user=budi izin=laporan:ubah hasil=200
t=320 AKSI user=citra izin=laporan:ubah hasil=403
[dependensi]
pakai requests 2.31.0
pakai jinja2 3.1.6
advisori requests 2.32.4 TINGGI ADV-001
advisori jinja2 3.1.5 SEDANG ADV-002
""",
            """# audit toko-ani v2
[header]
HTTP/1.1 200 OK
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Set-Cookie: sesi=c03d; Path=/; Secure; HttpOnly
[pengguna]
ani pbkdf2_sha256$600000$garam01$82396046d6aa012e85b098cf13e0f62bf27668f99bf657f360778049ce7e2b75
budi pbkdf2_sha256$600000$garam03$c69b0197db5236050a9ede10df61fdd1c21a9ef0f85228adfa3346a1a1ea0530
[peran]
peran pembaca = laporan:baca
peran admin = laporan:baca, pengguna:hapus
ani = admin
budi = pembaca
[kode]
import os
DB_PASSWORD = os.environ["DB_PASSWORD"]
[log]
t=100 GAGAL ip=192.0.2.15 user=budi
t=140 SUKSES ip=192.0.2.15 user=budi
t=200 AKSI user=budi izin=pengguna:hapus hasil=403
[dependensi]
pakai requests 2.32.4
advisori requests 2.32.4 TINGGI ADV-001
""",
        ],
    },
]
