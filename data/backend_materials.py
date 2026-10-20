"""Kurikulum Backend & API.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

BACKEND_BAB = [
    {
        "judul": "Cara Kerja Backend",
        "ket": "Dari permintaan HTTP sampai respons: peran backend, kontrak aplikasi, router, dan middleware.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Merancang API REST",
        "ket": "Sumber daya, validasi, pesan error, dokumentasi OpenAPI, dan CORS.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "JavaScript di Server: Node.js, Express, NestJS",
        "ket": "Membangun API dengan Node.js, dari Express yang minimalis sampai NestJS yang terstruktur.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "Python di Server: Flask dan FastAPI",
        "ket": "Dua framework Python paling banyak dipakai untuk API, lengkap dengan ORM-nya.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Django dan Ekosistem Python",
        "ket": "Framework Python 'serba ada', API dengan DRF, dan peta framework Python lain.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Spring Boot dan Dunia JVM",
        "ket": "Backend Java yang dominan di perusahaan, JPA, dan peta framework JVM.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "ASP.NET Core dan Dunia .NET",
        "ket": "Minimal API, controller, EF Core, dan ekosistem .NET di sekitarnya.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Laravel dan Dunia PHP",
        "ket": "Framework PHP paling populer: rute, Blade, Eloquent, dan Sanctum.",
        "tingkat": "menengah",
        "jumlah": 2,
    },
    {
        "judul": "Ruby on Rails dan Framework Konvensi Lain",
        "ket": "Rails dengan Active Record, lalu peta framework PHP dan Ruby.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Go, Rust, dan Peta Lintas Bahasa",
        "ket": "API Go dengan net/http dan Gin, peta Go/Rust/bahasa lain, dan peta ORM.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Autentikasi",
        "ket": "Session, cookie, kata sandi, token, JWT, dan pustaka auth per framework.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "OAuth, SSO, dan Otorisasi",
        "ket": "OAuth 2.0, OpenID Connect, Keycloak, otorisasi, rate limiting, dan layanan identitas.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Cache, Antrean, dan Message Broker",
        "ket": "Redis dan Valkey, antrean tugas, RabbitMQ, Kafka, dan peta pemain lain.",
        "tingkat": "mahir",
        "jumlah": 6,
    },
    {
        "judul": "Real-time dan Gaya API Lanjutan",
        "ket": "WebSocket, SSE, GraphQL, gRPC, dan gaya RPC lain.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "Deploy dan Arsitektur Backend",
        "ket": "Nginx, server aplikasi, arsitektur backend, backend instan, dan proyek akhir.",
        "tingkat": "mahir",
        "jumlah": 5,
    },
]

BACKEND_MATERIALS = [
    {
        "title": "1. Apa Itu Backend dan Kenapa API Ada",
        "sections": [
            {
                "body": [
                    "Waktu kamu menekan tombol Bayar di aplikasi toko online, layar",
                    "ponselmu nggak tahu apakah barangnya masih ada. Yang tahu adalah",
                    "sebuah program di komputer lain, entah di mana. Program itu",
                    "menerima pesananmu, mengecek stok, mengurangi saldo, mencatat",
                    "transaksi, lalu mengirim balasan: berhasil atau gagal.",
                    "",
                    "Program itu namanya backend. Backend adalah bagian aplikasi yang",
                    "jalan di server, yaitu komputer yang menunggu permintaan dari",
                    "komputer lain. Lawannya frontend: halaman web atau aplikasi",
                    "ponsel yang dilihat dan disentuh pengguna.",
                    "",
                    "Pembagian kerjanya kira-kira begini:",
                    "  frontend  ->  menampilkan data dan menerima klik",
                    "  backend   ->  memutuskan apa yang boleh terjadi",
                    "  database  ->  menyimpan data supaya nggak hilang",
                    "",
                    "Kamu sudah kenal dua dari tiga lapisan itu. HTML dan JavaScript",
                    "di browser itu frontend, dan SQL itu bahasa untuk bicara dengan",
                    "database. Kurikulum ini mengisi bagian tengahnya.",
                ],
            },
            {
                "heading": "Klien, server, dan API",
                "body": [
                    "Pihak yang meminta disebut klien. Klien bisa browser, aplikasi",
                    "Android, aplikasi kasir, atau program lain. Pihak yang menjawab",
                    "disebut server. Satu backend biasanya melayani banyak klien",
                    "sekaligus.",
                    "",
                    "Supaya klien dan server bisa saling paham, keduanya harus",
                    "sepakat soal bentuk pesannya. Kesepakatan itu namanya API,",
                    "singkatan dari Application Programming Interface. Gampangnya,",
                    "API itu daftar menu plus cara memesannya: alamat mana yang bisa",
                    "dipanggil, data apa yang harus dikirim, dan balasan seperti apa",
                    "yang bakal datang.",
                    "",
                    "Di backend web, API hampir selalu berjalan di atas HTTP, dan",
                    "datanya dikirim sebagai JSON. Contohnya satu permintaan dan",
                    "balasannya:",
                    "",
                    "  permintaan:  GET /stok/pensil",
                    "  balasan:     200 {\"barang\": \"pensil\", \"sisa\": 12}",
                    "",
                    "Klien nggak perlu tahu stok disimpan di tabel apa atau ditulis",
                    "pakai bahasa apa. Ia cukup tahu menunya. Server juga boleh",
                    "mengganti isi dapurnya kapan saja, asal menunya tetap sama.",
                ],
            },
            {
                "heading": "Backend kecil yang bisa dijalankan",
                "code": "import json\n\n# \"Database\" pura-pura: dict biasa di memori.\nstok = {\"pensil\": 12, \"buku tulis\": 0}\n\n\ndef backend(metode, path):\n    \"\"\"Terima permintaan, cek aturannya, lalu kirim balasan.\"\"\"\n    if not path.startswith(\"/stok/\"):\n        return 404, {\"error\": \"alamat nggak dikenal\"}\n    if metode != \"GET\":\n        return 405, {\"error\": \"alamat ini cuma bisa dibaca\"}\n    barang = path.removeprefix(\"/stok/\").replace(\"-\", \" \")\n    if barang not in stok:\n        return 404, {\"error\": f\"{barang} nggak dijual\"}\n    return 200, {\"barang\": barang, \"sisa\": stok[barang]}\n\n\nfor metode, path in [(\"GET\", \"/stok/pensil\"),\n                     (\"GET\", \"/stok/buku-tulis\"),\n                     (\"GET\", \"/stok/penghapus\"),\n                     (\"DELETE\", \"/stok/pensil\")]:\n    status, isi = backend(metode, path)\n    print(metode, path, \"->\", status, json.dumps(isi))",
            },
            {
                "body": [
                    "Keluaran:",
                    "GET /stok/pensil -> 200 {\"barang\": \"pensil\", \"sisa\": 12}",
                    "GET /stok/buku-tulis -> 200 {\"barang\": \"buku tulis\", \"sisa\": 0}",
                    "GET /stok/penghapus -> 404 {\"error\": \"penghapus nggak dijual\"}",
                    "DELETE /stok/pensil -> 405 {\"error\": \"alamat ini cuma bisa dibaca\"}",
                    "",
                    "Program ini belum menyentuh jaringan sama sekali, tapi pola",
                    "kerjanya sudah sama dengan backend sungguhan. Masuk sebuah",
                    "permintaan (metode dan alamat), backend mengecek aturannya, lalu",
                    "keluar sebuah balasan berisi angka status dan data.",
                    "",
                    "Angka 200, 404, dan 405 itu kode status HTTP. Artinya dibahas di",
                    "materi berikutnya. Untuk sekarang cukup tahu: 200 berarti",
                    "berhasil, 404 berarti barangnya nggak ada, dan 405 berarti",
                    "alamatnya ada tapi caranya salah.",
                ],
            },
            {
                "heading": "Kenapa aplikasi nggak langsung ke database?",
                "body": [
                    "Pertanyaan ini wajar. Aplikasi Android toh bisa saja membuka",
                    "koneksi ke MySQL dan menjalankan SELECT sendiri. Masalahnya ada",
                    "tiga:",
                    "  1. Kata sandi database ikut tertanam di aplikasi. Siapa pun",
                    "     yang membongkar berkas APK bisa menemukannya, lalu menghapus",
                    "     seluruh tabel.",
                    "  2. Aturan bisnis bisa dilewati. Kalau pengecekan \"stok harus",
                    "     cukup\" cuma ada di aplikasi, orang yang mengirim perintah",
                    "     sendiri nggak kena aturan itu. Aturan yang ditaruh di backend",
                    "     berlaku untuk semua klien.",
                    "  3. Klien makin banyak, logikanya terpecah. Web, Android, iOS,",
                    "     dan aplikasi kasir harus menulis ulang aturan yang sama.",
                    "     Dengan backend, aturan itu ditulis sekali.",
                    "",
                    "Jadi backend berdiri di tengah sebagai satu-satunya pintu ke",
                    "data. Klien boleh banyak dan boleh berganti, pintunya tetap satu.",
                ],
            },
            {
                "heading": "Kenapa framework ada",
                "body": [
                    "Backend kecil di atas cuma menangani satu jenis alamat. Backend",
                    "sungguhan harus mengerjakan banyak hal yang sama berulang-ulang:",
                    "  - membaca teks HTTP mentah jadi metode, alamat, header, dan body",
                    "  - mencocokkan alamat ke fungsi yang tepat (routing)",
                    "  - mengecek data yang masuk dan menolak yang salah bentuk",
                    "  - mengurus login, cookie, dan header keamanan",
                    "  - mengubah data jadi JSON lalu mengirim balasannya",
                    "",
                    "Framework adalah kumpulan kode yang sudah mengerjakan bagian",
                    "berulang itu, ditambah aturan main tentang di mana kodemu",
                    "ditaruh. Kamu tinggal menulis bagian yang khas aplikasimu.",
                    "Express di JavaScript, Flask dan FastAPI di Python, Spring Boot",
                    "di Java, Laravel di PHP, semuanya framework backend.",
                    "",
                    "Bab ini dan bab berikutnya sengaja memakai Python polos tanpa",
                    "framework. Tujuannya supaya kamu lihat apa yang dikerjakan",
                    "framework di balik layar. Mulai bab 3, tiap bab membahas",
                    "framework dari satu bahasa. Kamu boleh membaca bab bahasa yang",
                    "kamu kuasai saja dan melompati sisanya. Dasar bahasanya sendiri",
                    "nggak diajarkan ulang di sini; kalau ada yang asing, buka",
                    "kurikulum bahasanya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi ojek online, dompet digital, dan marketplace punya versi",
                    "Android, iOS, dan web yang memanggil API yang sama. Kalau kamu",
                    "membuka DevTools di versi webnya (klik kanan, Inspect, tab",
                    "Network), kelihatan browser mengirim permintaan ke alamat",
                    "seperti /api/... dan menerima balasan JSON. Itu pintu yang sama",
                    "dengan yang dipakai aplikasi ponselnya.",
                    "",
                    "Kasus kecil: koperasi sekolah mau punya halaman web untuk siswa",
                    "dan aplikasi Android untuk kasir. Ketua koperasi minta saldo",
                    "siswa nggak boleh minus, apa pun aplikasinya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan apa yang dilihat dan apa yang diputuskan. Daftar",
                    "     barang dan tombol beli itu frontend. Keputusan \"saldo cukup",
                    "     atau nggak\" itu backend.",
                    "  2. Rancang menunya dulu, misalnya GET /barang untuk daftar",
                    "     barang dan POST /transaksi untuk membeli.",
                    "  3. Taruh aturan saldo cuma di backend, di fungsi yang menangani",
                    "     POST /transaksi:",
                    "       if saldo < total:",
                    "           return 409, {\"error\": \"saldo nggak cukup\"}",
                    "  4. Halaman web dan aplikasi kasir sama-sama memanggil alamat",
                    "     itu. Aturan saldo otomatis berlaku untuk keduanya, dan nggak",
                    "     ada kata sandi database di aplikasi mana pun.",
                ],
            },
        ],
    },
    {
        "title": "2. HTTP dari Dekat: Metode, Status, Header, dan HTTPS",
        "sections": [
            {
                "body": [
                    "HTTP adalah bahasa yang dipakai klien dan server web untuk",
                    "saling bicara. Bentuknya cuma teks dengan aturan tata letak yang",
                    "ketat. Kalau kamu bisa membaca teks itu, kamu bisa mengerti",
                    "hampir semua masalah backend yang bakal kamu temui.",
                    "",
                    "Satu percakapan HTTP selalu sepasang: klien mengirim permintaan",
                    "(request), server membalas dengan respons (response). Ini",
                    "permintaan untuk membuat pesanan baru, persis seperti yang",
                    "lewat di kabel:",
                ],
            },
            {
                "heading": "Permintaan dan respons mentah",
                "bahasa": "http",
                "code": """POST /pesanan HTTP/1.1
Host: toko.test
Content-Type: application/json
Content-Length: 31

{"menu": "es teh", "jumlah": 2}

HTTP/1.1 201 Created
Content-Type: application/json
Location: /pesanan/88

{"id": 88, "status": "diproses"}""",
            },
            {
                "body": [
                    "Bagian atas itu permintaan, bagian bawah responsnya. Keduanya",
                    "punya susunan yang sama:",
                    "  1. Baris pertama. Di permintaan isinya metode, alamat, dan",
                    "     versi HTTP. Di respons isinya versi, kode status, dan",
                    "     frasa singkat.",
                    "  2. Header. Satu baris satu keterangan, bentuknya Nama: nilai.",
                    "  3. Satu baris kosong. Ini penanda header sudah selesai.",
                    "  4. Body, yaitu isi pesannya. Boleh kosong.",
                    "",
                    "Header Host wajib ada di HTTP/1.1, karena satu server sering",
                    "melayani banyak nama situs sekaligus. Nama header nggak peduli",
                    "huruf besar-kecil: content-type dan Content-Type itu sama.",
                    "",
                    "Metode adalah kata kerja permintaan. Yang paling sering kamu",
                    "pakai:",
                    "  GET     ambil data, nggak mengubah apa pun",
                    "  POST    kirim data baru, misalnya membuat pesanan",
                    "  PUT     ganti satu data seluruhnya",
                    "  PATCH   ubah sebagian data",
                    "  DELETE  hapus data",
                    "  HEAD    sama seperti GET tapi tanpa body",
                    "  OPTIONS tanya metode apa saja yang boleh",
                    "",
                    "GET, HEAD, dan OPTIONS disebut aman (safe): memanggilnya nggak",
                    "boleh mengubah data. Makanya jangan pernah bikin alamat seperti",
                    "GET /hapus-akun. Browser, mesin pencari, dan fitur pratinjau",
                    "tautan di aplikasi chat bisa memanggil GET sendiri tanpa diklik",
                    "siapa pun.",
                ],
            },
            {
                "heading": "Kode status",
                "body": [
                    "Kode status adalah tiga angka di baris pertama respons. Angka",
                    "pertamanya menyebut kelompok:",
                    "  1xx  informasi, jarang kamu urus sendiri",
                    "  2xx  berhasil",
                    "  3xx  pindah alamat atau pakai salinan yang sudah ada",
                    "  4xx  kesalahan di pihak klien",
                    "  5xx  kesalahan di pihak server",
                    "",
                    "Yang wajib kamu hafal karena dipakai tiap hari:",
                    "  200 OK                  berhasil, ada isinya",
                    "  201 Created             data baru berhasil dibuat",
                    "  204 No Content          berhasil, sengaja tanpa body",
                    "  301/308                 pindah permanen ke alamat lain",
                    "  304 Not Modified        salinan di klien masih berlaku",
                    "  400 Bad Request         permintaan rusak, misalnya JSON cacat",
                    "  401 Unauthorized        belum login atau tokennya salah",
                    "  403 Forbidden           sudah login, tapi nggak berhak",
                    "  404 Not Found           alamat atau datanya nggak ada",
                    "  405 Method Not Allowed  alamatnya ada, metodenya salah",
                    "  409 Conflict            bentrok dengan keadaan sekarang",
                    "  422 Unprocessable       bentuknya benar, isinya nggak sah",
                    "  429 Too Many Requests   klien terlalu sering memanggil",
                    "  500 Internal Error      ada yang rusak di kode server",
                    "  503 Service Unavailable server sedang nggak bisa melayani",
                    "",
                    "Jebakan: banyak pemula membalas semua hal dengan 200, lalu",
                    "menaruh {\"error\": ...} di body. Klien jadi harus membaca isi",
                    "body dulu untuk tahu berhasil atau gagal. Alat pemantau, cache,",
                    "dan pustaka HTTP di klien juga ikut tertipu, karena semuanya",
                    "membaca kode status lebih dulu.",
                    "",
                    "Bedakan 401 dan 403. Nama resmi 401 memang Unauthorized, tapi",
                    "artinya \"aku nggak tahu kamu siapa\". Kalau server tahu kamu",
                    "siapa dan kamu tetap nggak boleh, itu 403.",
                ],
            },
            {
                "heading": "Membuat respons dengan tangan",
                "code": "import json\nfrom http import HTTPStatus\n\n\ndef buat_respons(kode, data):\n    body = json.dumps(data, ensure_ascii=False).encode(\"utf-8\")\n    status = HTTPStatus(kode)\n    baris = [\n        f\"HTTP/1.1 {status.value} {status.phrase}\",\n        \"Content-Type: application/json; charset=utf-8\",\n        f\"Content-Length: {len(body)}\",\n    ]\n    # HTTP memisahkan baris dengan \\r\\n, lalu satu baris kosong\n    # sebelum body.\n    return \"\\r\\n\".join(baris) + \"\\r\\n\\r\\n\" + body.decode(\"utf-8\")\n\n\nteks = buat_respons(201, {\"nama\": \"Kafé Senja\"})\nprint(teks.replace(\"\\r\\n\", \"\\n\"))\nprint()\nprint(\"huruf di body:\", len('{\"nama\": \"Kafé Senja\"}'))\nprint(HTTPStatus(404).phrase, \"|\", HTTPStatus(422).phrase)",
            },
            {
                "body": [
                    "Keluaran:",
                    "HTTP/1.1 201 Created",
                    "Content-Type: application/json; charset=utf-8",
                    "Content-Length: 23",
                    "",
                    "{\"nama\": \"Kafé Senja\"}",
                    "",
                    "huruf di body: 22",
                    "Not Found | Unprocessable Content",
                    "",
                    "Perhatikan Content-Length 23, padahal body-nya 22 huruf. Header",
                    "itu menghitung byte, bukan huruf. Huruf é butuh dua byte di",
                    "UTF-8. Kalau angkanya kurang, klien memotong body; kalau lebih,",
                    "klien menunggu byte yang nggak pernah datang. Framework",
                    "menghitungnya untukmu, tapi bug ini muncul lagi begitu kamu",
                    "menulis respons sendiri.",
                    "",
                    "Frasa 422 di Python versi baru tertulis Unprocessable Content.",
                    "Nama itu berasal dari RFC 9110, dokumen standar HTTP terbitan",
                    "Juni 2022. Dokumentasi lama masih menyebutnya Unprocessable",
                    "Entity. Kodenya sama, cuma namanya diperbarui.",
                ],
            },
            {
                "heading": "Stateless, HTTP/2, dan HTTP/3",
                "body": [
                    "HTTP itu stateless, artinya server nggak mengingat permintaan",
                    "sebelumnya. Tiap permintaan berdiri sendiri. Kalau server perlu",
                    "tahu kamu sudah login, permintaanmu sendiri yang harus membawa",
                    "buktinya, biasanya lewat cookie atau token di header. Cara",
                    "kerjanya dibahas di bab Autentikasi.",
                    "",
                    "Versi HTTP ada tiga yang masih dipakai:",
                    "  - HTTP/1.1 berupa teks seperti contoh di atas. Satu koneksi",
                    "    melayani satu permintaan dalam satu waktu.",
                    "  - HTTP/2 mengirim pesan yang sama dalam bentuk biner dan",
                    "    memecahnya jadi potongan kecil, sehingga banyak permintaan",
                    "    bisa lewat satu koneksi bersamaan.",
                    "  - HTTP/3 memakai QUIC di atas UDP, sehingga satu paket yang",
                    "    hilang nggak menahan permintaan lain.",
                    "",
                    "Kabar baiknya, arti metode, status, dan header sama persis di",
                    "ketiga versi. Semuanya diatur RFC 9110 sampai RFC 9114, terbit",
                    "Juni 2022. Kodemu di backend hampir nggak pernah peduli versi",
                    "mana yang dipakai klien; urusan itu diserahkan ke web server",
                    "seperti Nginx.",
                ],
            },
            {
                "heading": "HTTPS dan TLS",
                "body": [
                    "HTTP polos dikirim apa adanya. Siapa pun yang berada di jalur",
                    "yang sama, misalnya di Wi-Fi kafe, bisa membaca kata sandimu.",
                    "HTTPS adalah HTTP yang dibungkus TLS (Transport Layer Security).",
                    "TLS memberi tiga jaminan:",
                    "  - Kerahasiaan: isi pesan dienkripsi, jadi nggak bisa diintip.",
                    "  - Keutuhan: pesan yang diubah di jalan bakal ketahuan.",
                    "  - Keaslian: server membuktikan dirinya lewat sertifikat yang",
                    "    ditandatangani lembaga tepercaya (certificate authority).",
                    "",
                    "Sebelum permintaan pertama dikirim, klien dan server melakukan",
                    "jabat tangan (handshake) untuk menyepakati kunci enkripsi. Di",
                    "TLS 1.3 (RFC 8446, terbit Agustus 2018) jabat tangan ini cukup",
                    "satu kali bolak-balik. TLS 1.0 dan 1.1 sudah dinyatakan usang",
                    "lewat RFC 8996, jadi jangan diaktifkan lagi.",
                    "",
                    "Di backend kamu jarang menulis kode TLS sendiri. Biasanya web",
                    "server atau layanan hosting yang memasang sertifikat, misalnya",
                    "sertifikat gratis dari Let's Encrypt. Cara memasangnya di",
                    "produksi dibahas di kurikulum DevOps. Yang perlu kamu pegang",
                    "sekarang: API yang menerima kata sandi atau token wajib lewat",
                    "HTTPS.",
                ],
            },
            {
                "heading": "Mencoba sendiri dengan curl",
                "bahasa": "terminal",
                "code": "# -i menampilkan baris status dan header respons\ncurl -i https://example.com\n\n# -v menampilkan permintaan yang dikirim dan jabat tangan TLS\ncurl -v https://example.com -o /dev/null\n\n# mengirim JSON dengan POST\ncurl -i -X POST https://contoh.test/pesanan \\\n  -H 'Content-Type: application/json' \\\n  -d '{\"menu\": \"es teh\", \"jumlah\": 2}'",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tab Network di DevTools browser menampilkan tiap permintaan HTTP",
                    "yang dikirim sebuah halaman, lengkap dengan metode, kode status,",
                    "header, dan body-nya. Programmer backend dan frontend memakai",
                    "tab ini tiap hari untuk menjawab pertanyaan \"yang salah itu",
                    "klien atau server?\". Jawabannya hampir selalu kelihatan dari",
                    "kode status.",
                    "",
                    "Kasus kecil: form pendaftaran di aplikasimu selalu menampilkan",
                    "\"Pendaftaran berhasil!\", bahkan saat email sudah dipakai orang",
                    "lain. Di tab Network kelihatan backend membalas 200 dengan body",
                    "{\"error\": \"email sudah terdaftar\"}.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan kode yang tepat untuk tiap hasil. Akun baru",
                    "     terbuat itu 201. Email sudah dipakai itu bentrok dengan data",
                    "     yang ada, jadi 409. Email kosong atau salah bentuk itu 422.",
                    "  2. Ubah backend supaya membalas dengan kode itu, misalnya:",
                    "       if email_sudah_ada(email):",
                    "           return 409, {\"error\": \"email sudah terdaftar\"}",
                    "  3. Ubah frontend supaya membaca kode status lebih dulu, baru",
                    "     body. Hanya 2xx yang boleh menampilkan pesan berhasil.",
                    "  4. Cek lagi di tab Network: permintaan yang gagal sekarang",
                    "     tampil merah, dan form menampilkan pesan error yang benar.",
                ],
            },
        ],
    },
    {
        "title": "3. Aplikasi Sebagai Fungsi: WSGI, ASGI, dan Rack",
        "sections": [
            {
                "body": [
                    "Di produksi, backend Python jarang menerima koneksi jaringan",
                    "sendiri. Yang menerima koneksi adalah server aplikasi seperti",
                    "Gunicorn atau Uvicorn. Yang berisi logika adalah aplikasimu,",
                    "yang ditulis pakai Flask, Django, atau FastAPI. Dua program itu",
                    "dibuat orang yang berbeda, tapi bisa dipasang-pasangkan bebas.",
                    "",
                    "Bisa begitu karena ada kontrak di antara keduanya. Kontraknya",
                    "sederhana: aplikasi itu cuma sebuah fungsi. Server membaca teks",
                    "HTTP dari jaringan, mengubahnya jadi data Python, memanggil",
                    "fungsi aplikasimu, lalu mengubah hasilnya kembali jadi teks",
                    "HTTP. Aplikasi nggak pernah menyentuh jaringan.",
                    "",
                    "Di Python kontrak itu namanya WSGI (Web Server Gateway",
                    "Interface), ditulis di PEP 3333. Aplikasinya adalah fungsi",
                    "dengan dua parameter:",
                    "  - environ: dict berisi keterangan permintaan, misalnya",
                    "    REQUEST_METHOD, PATH_INFO, QUERY_STRING, dan header.",
                    "  - start_response: fungsi dari server yang dipanggil aplikasi",
                    "    untuk menyetor status dan daftar header.",
                    "Fungsi itu mengembalikan iterable berisi bytes, yaitu body",
                    "responsnya.",
                ],
            },
            {
                "heading": "Aplikasi WSGI, diuji tanpa membuka port",
                "code": "from wsgiref.util import setup_testing_defaults\n\n\ndef aplikasi(environ, start_response):\n    \"\"\"Aplikasi WSGI: fungsi biasa dengan dua parameter.\"\"\"\n    jenis = [(\"Content-Type\", \"text/plain; charset=utf-8\")]\n    if environ[\"PATH_INFO\"] == \"/\":\n        start_response(\"200 OK\", jenis)\n        return [b\"Halo dari WSGI\"]\n    start_response(\"404 Not Found\", jenis)\n    return [b\"Halaman nggak ada\"]\n\n\ndef panggil(metode, path):\n    \"\"\"Berlagak jadi server: siapkan environ, tangkap status, gabung body.\"\"\"\n    environ = {\"REQUEST_METHOD\": metode, \"PATH_INFO\": path}\n    setup_testing_defaults(environ)\n    catatan = {}\n\n    def start_response(status, headers):\n        catatan[\"status\"] = status\n        catatan[\"headers\"] = headers\n\n    body = b\"\".join(aplikasi(environ, start_response))\n    print(metode, path, \"->\", catatan[\"status\"], \"|\", body.decode())\n\n\npanggil(\"GET\", \"/\")\npanggil(\"GET\", \"/kontak\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "GET / -> 200 OK | Halo dari WSGI",
                    "GET /kontak -> 404 Not Found | Halaman nggak ada",
                    "",
                    "Fungsi panggil di situ berperan sebagai server. Ia menyiapkan",
                    "environ, mengisi sisa kuncinya dengan nilai bawaan lewat",
                    "setup_testing_defaults, menyediakan start_response yang cuma",
                    "mencatat, lalu menggabungkan body. Semua itu terjadi di memori.",
                    "Nggak ada port yang dibuka dan nggak ada browser yang terlibat.",
                    "",
                    "Begitulah cara framework menguji aplikasi. Test client di Flask",
                    "dan Django bekerja persis seperti fungsi panggil itu: membuat",
                    "environ palsu, memanggil aplikasimu, lalu membaca hasilnya.",
                    "Tesnya cepat, dan bisa jalan di komputer tanpa jaringan.",
                    "",
                    "Untuk melihatnya di browser, pustaka standar Python punya server",
                    "kecil yang mengikuti kontrak ini. Server ini cuma untuk belajar,",
                    "jangan dipakai di produksi:",
                ],
            },
            {
                "heading": "Menyalakan server percobaan",
                "code": """from wsgiref.simple_server import make_server

# fungsi aplikasi dari contoh di atas ditaruh di sini
...

with make_server("127.0.0.1", 8000, aplikasi) as server:
    print("Buka http://127.0.0.1:8000")
    server.serve_forever()""",
            },
            {
                "heading": "ASGI: kontrak untuk aplikasi async",
                "body": [
                    "Kontrak tadi lahir saat satu permintaan selalu berarti satu",
                    "jawaban lalu selesai. Koneksi yang lama terbuka, seperti",
                    "WebSocket untuk chat, nggak cocok dengan bentuk itu. Selain itu,",
                    "fungsinya nggak bisa memakai async/await.",
                    "",
                    "ASGI (Asynchronous Server Gateway Interface) adalah penerusnya.",
                    "Aplikasi ASGI adalah fungsi async dengan tiga parameter:",
                    "  - scope: dict keterangan koneksi, mirip environ.",
                    "  - receive: fungsi async untuk mengambil pesan dari klien.",
                    "  - send: fungsi async untuk mengirim pesan ke klien.",
                    "Respons dikirim sebagai beberapa pesan, jadi koneksi bisa tetap",
                    "terbuka dan mengirim data sedikit demi sedikit.",
                    "",
                    "FastAPI dan Starlette adalah framework ASGI, dan Django juga",
                    "bisa berjalan sebagai ASGI. Server yang menjalankannya misalnya",
                    "Uvicorn. Contoh ini memanggil aplikasi ASGI secara langsung,",
                    "lagi-lagi tanpa jaringan:",
                ],
            },
            {
                "heading": "Aplikasi ASGI",
                "code": "import asyncio\n\n\nasync def aplikasi(scope, receive, send):\n    \"\"\"Aplikasi ASGI: fungsi async dengan tiga parameter.\"\"\"\n    pesan = await receive()\n    teks = b\"Kamu mengirim \" + pesan[\"body\"]\n    await send({\"type\": \"http.response.start\", \"status\": 200,\n                \"headers\": [(b\"content-type\", b\"text/plain\")]})\n    await send({\"type\": \"http.response.body\", \"body\": teks})\n\n\nasync def main():\n    scope = {\"type\": \"http\", \"method\": \"POST\", \"path\": \"/gema\"}\n\n    async def receive():\n        return {\"type\": \"http.request\", \"body\": b\"halo\", \"more_body\": False}\n\n    async def send(pesan):\n        isi = pesan.get(\"status\") or pesan[\"body\"].decode()\n        print(pesan[\"type\"], \"|\", isi)\n\n    await aplikasi(scope, receive, send)\n\n\nasyncio.run(main())",
            },
            {
                "body": [
                    "Keluaran:",
                    "http.response.start | 200",
                    "http.response.body | Kamu mengirim halo",
                    "",
                    "Respons terbagi dua pesan: pembuka berisi status dan header,",
                    "lalu body. Untuk respons yang panjang, aplikasi boleh mengirim",
                    "banyak pesan body berturut-turut. Kemampuan ini yang dipakai",
                    "untuk streaming, misalnya jawaban chatbot yang muncul kata demi",
                    "kata.",
                ],
            },
            {
                "heading": "Rack: kontrak yang sama di Ruby",
                "body": [
                    "Ide \"aplikasi = fungsi\" juga dipakai bahasa lain. Di Ruby",
                    "namanya Rack. Aplikasi Rack adalah objek apa pun yang punya",
                    "method call(env), dan hasilnya larik berisi tiga hal: status,",
                    "hash header, dan body yang bisa di-each. Rails dan Sinatra",
                    "berdiri di atas Rack. Versi stabil terbaru saat materi ini",
                    "ditulis (Oktober 2026) adalah Rack 3.2.7. Sejak Rack 3, nama",
                    "header di hash wajib huruf kecil.",
                    "",
                    "Contoh di bawah memanggil aplikasi Rack dengan env buatan",
                    "sendiri. Ia cuma butuh Ruby, tanpa memasang gem apa pun:",
                ],
            },
            {
                "heading": "Aplikasi Rack tanpa server",
                "bahasa": "ruby",
                "code": """# Aplikasi Rack: objek apa pun yang punya method call(env).
app = lambda do |env|
  if env["PATH_INFO"] == "/"
    [200, { "content-type" => "text/plain" }, ["Halo dari Rack"]]
  else
    [404, { "content-type" => "text/plain" }, ["Halaman nggak ada"]]
  end
end

["/", "/kontak"].each do |path|
  status, headers, body = app.call({ "REQUEST_METHOD" => "GET", "PATH_INFO" => path })
  puts "#{path} -> #{status} #{headers['content-type']} | #{body.join}"
end""",
            },
            {
                "body": [
                    "Keluaran:",
                    "/ -> 200 text/plain | Halo dari Rack",
                    "/kontak -> 404 text/plain | Halaman nggak ada",
                    "",
                    "Bahasa lain punya kontrak serupa: PHP punya PSR-15, Java punya",
                    "Servlet, dan Node.js memakai pasangan objek req dan res. Namanya",
                    "beda-beda, polanya sama. Begitu paham satu, kamu bakal mengenali",
                    "yang lain.",
                    "",
                    "Jebakan: body di kontrak Python ini wajib bytes, bukan str. Kalau aplikasimu",
                    "mengembalikan [\"halo\"], server bakal menolak dengan error",
                    "tipe. Framework mengurus ini untukmu, tapi kesalahan ini sering",
                    "muncul saat menulis middleware sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Flask di produksi biasanya dijalankan dengan perintah",
                    "seperti gunicorn app:app. Artinya Gunicorn mengimpor modul app",
                    "lalu mencari objek bernama app di dalamnya, yaitu fungsi aplikasi",
                    "buatan Flask. Kalau suatu hari Gunicorn diganti server lain,",
                    "kode Flask-mu nggak perlu diubah satu baris pun.",
                    "",
                    "Kasus kecil: kamu menulis aplikasi berbentuk fungsi tadi dan ingin",
                    "memastikan alamat asing dijawab 404. Server CI (komputer yang",
                    "menjalankan tes otomatis tiap kali kode dikirim) nggak",
                    "mengizinkan membuka port.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jangan menyalakan server. Panggil fungsi aplikasinya",
                    "     langsung, seperti fungsi panggil di contoh tadi.",
                    "  2. Siapkan environ yang cuma berisi bagian yang penting, lalu",
                    "     lengkapi dengan setup_testing_defaults(environ).",
                    "  3. Buat start_response yang menyimpan status ke sebuah dict,",
                    "     lalu periksa isinya:",
                    "       assert catatan[\"status\"].startswith(\"404\")",
                    "  4. Gabungkan body dengan b\"\".join(...) dan periksa juga",
                    "     isinya. Tes ini jalan dalam hitungan milidetik, tanpa",
                    "     jaringan.",
                ],
            },
        ],
    },
    {
        "title": "4. Router dan Middleware dari Nol",
        "sections": [
            {
                "body": [
                    "Aplikasi di materi sebelumnya cuma mengenal dua alamat,",
                    "dan pemilihannya pakai if. Backend sungguhan bisa punya ratusan",
                    "alamat. Menulis ratusan if jelas nggak masuk akal. Yang dipakai",
                    "adalah router.",
                    "",
                    "Router adalah tabel yang memasangkan metode dan pola alamat",
                    "dengan fungsi penanganannya. Fungsi penanganan itu disebut",
                    "handler. Pola alamat boleh punya bagian yang berubah-ubah,",
                    "namanya parameter path. Misalnya pola /produk/{id} cocok",
                    "dengan /produk/42 dan /produk/7, dan nilai id-nya diserahkan",
                    "ke handler.",
                    "",
                    "Contoh berikut router kecil yang mengubah tiap pola jadi regex,",
                    "yaitu pola pencarian teks. Bagian {id} diganti dengan kelompok",
                    "bernama yang menangkap apa saja selain garis miring.",
                ],
            },
            {
                "heading": "Router kecil dengan parameter path",
                "code": "import re\n\nrute = []\n\n\ndef tambah(metode, pola, handler):\n    # \"/produk/{id}\" diubah jadi regex \"^/produk/(?P<id>[^/]+)$\"\n    regex = \"^\" + re.sub(r\"\\{(\\w+)\\}\", r\"(?P<\\1>[^/]+)\", pola) + \"$\"\n    rute.append((metode, re.compile(regex), handler))\n\n\ndef cari(metode, path):\n    for m, regex, handler in rute:\n        cocok = regex.match(path)\n        if cocok and m == metode:\n            return handler, cocok.groupdict()\n    return None, {}\n\n\ntambah(\"GET\", \"/produk\", \"daftar_produk\")\ntambah(\"GET\", \"/produk/{id}\", \"lihat_produk\")\ntambah(\"GET\", \"/toko/{toko}/produk/{id}\", \"produk_di_toko\")\n\nfor path in [\"/produk\", \"/produk/42\", \"/toko/bandung/produk/7\",\n             \"/produk/42/ulasan\"]:\n    handler, param = cari(\"GET\", path)\n    print(f\"{path:24} -> {handler} {param}\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "/produk                  -> daftar_produk {}",
                    "/produk/42               -> lihat_produk {'id': '42'}",
                    "/toko/bandung/produk/7   -> produk_di_toko {'toko': 'bandung', 'id': '7'}",
                    "/produk/42/ulasan        -> None {}",
                    "",
                    "Ada tiga hal yang perlu kamu perhatikan:",
                    "  - Nilai parameter selalu string. id-nya '42', bukan 42.",
                    "    Framework seperti Flask dan FastAPI bisa mengubahnya jadi",
                    "    int kalau kamu memintanya.",
                    "  - Tanda ^ dan $ membuat polanya harus cocok dengan seluruh",
                    "    alamat. Tanpa keduanya, /produk/42/ulasan ikut cocok dengan",
                    "    /produk/{id}.",
                    "  - Router ini menjawab None untuk dua keadaan yang berbeda:",
                    "    alamat yang memang nggak ada, dan alamat yang ada tapi",
                    "    metodenya salah. Router yang baik membedakan keduanya jadi",
                    "    404 dan 405. Itu tugasmu di latihan bab ini.",
                    "",
                    "Urutan pendaftaran juga berpengaruh. Router sederhana memakai",
                    "rute pertama yang cocok. Kalau /produk/{id} didaftarkan sebelum",
                    "/produk/terlaris, alamat /produk/terlaris bakal ditangkap rute",
                    "pertama dengan id bernilai terlaris. Sebagian framework memilih",
                    "pola yang paling spesifik secara otomatis, sebagian lagi",
                    "mengikuti urutan. Baca dokumentasi frameworkmu soal ini.",
                ],
            },
            {
                "heading": "Middleware: kode yang dilewati semua permintaan",
                "body": [
                    "Ada pekerjaan yang harus dilakukan untuk hampir semua",
                    "permintaan: mencatat log, mengecek login, menambah header",
                    "keamanan, mengukur waktu. Kalau ditulis di tiap handler,",
                    "kodenya berulang dan gampang lupa satu.",
                    "",
                    "Middleware adalah fungsi yang berdiri di antara server dan",
                    "handler. Ia menerima permintaan, boleh melakukan sesuatu, lalu",
                    "memutuskan: teruskan ke langkah berikutnya, atau langsung",
                    "membalas sendiri. Beberapa middleware disusun jadi rantai.",
                    "",
                    "Ada dua gaya yang perlu kamu kenal:",
                    "  - Gaya next(), dipakai Express. Middleware menerima fungsi",
                    "    next dan memanggilnya kalau permintaan boleh lanjut.",
                    "  - Gaya bawang (onion), dipakai Koa dan juga oleh contoh di",
                    "    bawah. Tiap middleware membungkus langkah berikutnya, jadi",
                    "    ia bisa menjalankan kode sebelum dan sesudah handler.",
                    "    Permintaan masuk lapis demi lapis sampai ke handler, lalu",
                    "    responsnya keluar lewat lapisan yang sama dalam urutan",
                    "    terbalik.",
                ],
            },
            {
                "heading": "Rantai middleware gaya bawang",
                "code": """def pencatat(req, lanjut):
    print("pencatat: masuk", req["path"])
    res = lanjut(req)
    print("pencatat: keluar dengan status", res["status"])
    return res


def wajib_login(req, lanjut):
    if req.get("token") != "rahasia":
        print("wajib_login: ditolak, handler nggak dipanggil")
        return {"status": 401, "body": "login dulu"}
    return lanjut(req)


def profil(req):
    print("profil: menyiapkan data")
    return {"status": 200, "body": "profil Budi"}


def bungkus(mw, lanjut):
    def langkah(req):
        return mw(req, lanjut)
    return langkah


def susun(daftar, akhir):
    lanjut = akhir
    for mw in reversed(daftar):
        lanjut = bungkus(mw, lanjut)
    return lanjut


app = susun([pencatat, wajib_login], profil)
print(app({"path": "/profil", "token": "rahasia"}))
print()
print(app({"path": "/profil"}))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "pencatat: masuk /profil",
                    "profil: menyiapkan data",
                    "pencatat: keluar dengan status 200",
                    "{'status': 200, 'body': 'profil Budi'}",
                    "",
                    "pencatat: masuk /profil",
                    "wajib_login: ditolak, handler nggak dipanggil",
                    "pencatat: keluar dengan status 401",
                    "{'status': 401, 'body': 'login dulu'}",
                    "",
                    "Fungsi susun membungkus dari belakang: profil dibungkus",
                    "wajib_login, lalu hasilnya dibungkus pencatat. Jadi pencatat",
                    "jadi lapisan terluar. Ia sempat mencatat keluar walaupun",
                    "permintaan kedua ditolak di tengah jalan, karena kode",
                    "sesudah lanjut(req) tetap jalan saat jawaban kembali.",
                    "",
                    "Perhatikan juga bahwa wajib_login yang menolak nggak memanggil",
                    "lanjut sama sekali. Itu cara middleware menghentikan rantai:",
                    "handler profil nggak pernah dijalankan untuk tamu tanpa token.",
                    "",
                    "Urutan di daftar itu penting. Kalau pencatat ditaruh sesudah",
                    "wajib_login, permintaan yang ditolak nggak bakal tercatat di",
                    "log, padahal justru itu yang ingin kamu lihat saat ada orang",
                    "mencoba masuk tanpa izin.",
                ],
            },
            {
                "heading": "Bentuk yang sama di framework",
                "body": [
                    "Di Express, middleware didaftarkan dengan app.use dan diteruskan",
                    "dengan next(). Parameter path ditulis dengan titik dua:",
                ],
            },
            {
                "heading": "Express: app.use dan next()",
                "code": """const express = require("express");
const app = express();

app.use((req, res, next) => {
  console.log(req.method, req.path);
  next(); // tanpa ini, permintaan berhenti di sini
});

app.get("/produk/:id", (req, res) => {
  res.json({ id: req.params.id });
});""",
            },
            {
                "body": [
                    "Jebakan: di Express, middleware yang nggak memanggil next() dan",
                    "juga nggak mengirim respons membuat permintaan menggantung.",
                    "Nggak ada error yang muncul. Klien cuma menunggu sampai batas",
                    "waktunya habis, lalu menyerah.",
                    "",
                    "Koa memakai gaya bawang dengan async/await, mirip contoh Python",
                    "tadi. Kode sesudah await next() jalan setelah handler selesai,",
                    "jadi cocok untuk mengukur lama sebuah permintaan:",
                ],
            },
            {
                "heading": "Koa: await next()",
                "code": """const Koa = require("koa");
const app = new Koa();

app.use(async (ctx, next) => {
  const mulai = Date.now();
  await next();
  console.log(ctx.method, ctx.path, Date.now() - mulai, "ms");
});

app.use(async (ctx) => {
  ctx.body = "halo";
});""",
            },
            {
                "body": [
                    "Flask menyediakan decorator @app.before_request dan",
                    "@app.after_request untuk tujuan yang sama. Selain itu, aplikasi",
                    "Flask itu fungsi berkontrak WSGI, jadi kamu bisa membungkusnya",
                    "dengan fungsi lain yang berkontrak sama dan memanggilnya di",
                    "dalam. Polanya persis fungsi bungkus di contoh tadi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua backend punya middleware untuk log permintaan,",
                    "pengecekan login, CORS, kompresi, dan pembatas jumlah",
                    "permintaan. Contohnya paket morgan dan cors di Express,",
                    "daftar middleware Django di berkas settings.py, atau",
                    "app.UseAuthentication() di ASP.NET Core.",
                    "Urutan daftar itu menentukan siapa yang jalan lebih dulu.",
                    "",
                    "Kasus kecil: di aplikasi Express temanmu, halaman /admin ternyata",
                    "bisa dibuka tanpa login. Middleware cekLogin sudah ditulis dan",
                    "sudah didaftarkan dengan app.use(cekLogin).",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka berkas utama dan lihat urutan pendaftarannya. Express",
                    "     menjalankan middleware dan rute sesuai urutan ditulis.",
                    "  2. Ternyata app.get(\"/admin\", ...) ditulis di atas",
                    "     app.use(cekLogin). Rute /admin sudah mengirim respons",
                    "     sebelum cekLogin sempat dilewati.",
                    "  3. Pindahkan pendaftaran middleware ke atas semua rute yang",
                    "     dilindungi, atau pasang langsung di rutenya:",
                    "       app.get(\"/admin\", cekLogin, tampilkanAdmin);",
                    "  4. Coba lagi tanpa login. Sekarang /admin dijawab 401, dan",
                    "     halaman publik lain tetap bisa dibuka.",
                ],
            },
        ],
    },
    {
        "title": "5. Merancang Sumber Daya REST yang Rapi",
        "sections": [
            {
                "body": [
                    "Bab sebelumnya membahas cara backend menerima permintaan. Bab",
                    "ini membahas pertanyaan berikutnya: alamat dan metode apa saja",
                    "yang sebaiknya disediakan? API yang alamatnya asal-asalan",
                    "seperti /ambilSemuaBuku, /hapusBukuById, dan /update_buku_v2",
                    "memang bisa jalan, tapi tiap orang yang memakainya harus",
                    "menghafal satu per satu.",
                    "",
                    "REST (Representational State Transfer) adalah gaya merancang API",
                    "di atas HTTP. Istilahnya berasal dari disertasi Roy Fielding",
                    "tahun 2000. Idenya: data dianggap sebagai sumber daya",
                    "(resource) yang punya alamat sendiri, lalu dimanipulasi dengan",
                    "metode HTTP standar. Alamatnya kata benda, metodenya kata kerja.",
                    "",
                    "Gaya ini paling banyak dipakai. Laporan Postman State of the",
                    "API 2025 mencatat 93% respondennya memakai REST.",
                ],
            },
            {
                "heading": "Koleksi dan item",
                "body": [
                    "Satu jenis sumber daya biasanya punya dua alamat: koleksi dan",
                    "item. Koleksi memakai kata benda jamak, item menambahkan",
                    "pengenalnya:",
                    "  GET    /buku      daftar buku",
                    "  POST   /buku      tambah buku baru",
                    "  GET    /buku/2    detail buku nomor 2",
                    "  PUT    /buku/2    ganti seluruh data buku 2",
                    "  PATCH  /buku/2    ubah sebagian data buku 2",
                    "  DELETE /buku/2    hapus buku 2",
                    "",
                    "Enam operasi itu cuma butuh dua alamat. Orang yang sudah paham",
                    "polanya bisa menebak alamat untuk sumber daya lain tanpa",
                    "membaca dokumentasi: /anggota, /anggota/15, dan seterusnya.",
                    "",
                    "Hubungan antar sumber daya boleh ditulis bersarang, misalnya",
                    "GET /buku/2/ulasan untuk ulasan milik buku 2. Tapi jangan lebih",
                    "dari satu tingkat. Alamat seperti",
                    "/toko/3/rak/8/buku/2/ulasan/40 susah dipakai, padahal ulasan 40",
                    "cukup dicapai lewat /ulasan/40.",
                    "",
                    "Penyaringan, pengurutan, dan pencarian ditaruh di query string,",
                    "jangan dibuatkan alamat baru:",
                    "  GET /buku?penulis=tere-liye&sort=-tahun&q=hujan",
                    "Tanda minus di depan tahun lazim dipakai untuk urutan menurun.",
                ],
            },
            {
                "heading": "CRUD di memori",
                "code": """import json

buku = {1: {"id": 1, "judul": "Laskar Pelangi"}}
id_berikut = 2


def tangani(metode, path, body=None):
    global id_berikut
    bagian = path.strip("/").split("/")
    if bagian[0] != "buku" or len(bagian) > 2:
        return 404, None
    if len(bagian) == 1:                      # koleksi: /buku
        if metode == "GET":
            return 200, list(buku.values())
        if metode == "POST":
            data = {"id": id_berikut, **body}
            buku[id_berikut] = data
            id_berikut += 1
            return 201, data
        return 405, None
    id_buku = int(bagian[1])                  # satu item: /buku/2
    if metode == "GET":
        return (200, buku[id_buku]) if id_buku in buku else (404, None)
    if metode == "PUT":
        baru = id_buku not in buku
        buku[id_buku] = {"id": id_buku, **body}
        return (201 if baru else 200), buku[id_buku]
    if metode == "DELETE":
        if buku.pop(id_buku, None) is None:
            return 404, None
        return 204, None
    return 405, None


for metode, path, body in [
    ("POST", "/buku", {"judul": "Bumi Manusia"}),
    ("POST", "/buku", {"judul": "Bumi Manusia"}),
    ("PUT", "/buku/2", {"judul": "Bumi Manusia, cetakan 2"}),
    ("PUT", "/buku/2", {"judul": "Bumi Manusia, cetakan 2"}),
    ("DELETE", "/buku/3", None),
    ("DELETE", "/buku/3", None),
    ("GET", "/buku", None),
]:
    status, isi = tangani(metode, path, body)
    if isinstance(isi, list):        # untuk daftar, cukup tampilkan id-nya
        isi = [b["id"] for b in isi]
    print(f"{metode:6} {path:8} -> {status} {json.dumps(isi)}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "POST   /buku    -> 201 {\"id\": 2, \"judul\": \"Bumi Manusia\"}",
                    "POST   /buku    -> 201 {\"id\": 3, \"judul\": \"Bumi Manusia\"}",
                    "PUT    /buku/2  -> 200 {\"id\": 2, \"judul\": \"Bumi Manusia, cetakan 2\"}",
                    "PUT    /buku/2  -> 200 {\"id\": 2, \"judul\": \"Bumi Manusia, cetakan 2\"}",
                    "DELETE /buku/3  -> 204 null",
                    "DELETE /buku/3  -> 404 null",
                    "GET    /buku    -> 200 [1, 2]",
                    "",
                    "Contoh ini sengaja mengirim tiap permintaan dua kali, supaya",
                    "kelihatan satu sifat penting bernama idempoten. Operasi",
                    "idempoten adalah operasi yang hasil akhirnya sama, mau",
                    "dijalankan sekali atau berkali-kali.",
                    "  - POST dua kali membuat dua buku (id 2 dan 3). POST nggak",
                    "    idempoten.",
                    "  - PUT dua kali tetap menyisakan satu buku 2 dengan judul yang",
                    "    sama. PUT idempoten.",
                    "  - DELETE kedua dijawab 404, tapi keadaan datanya sama saja:",
                    "    buku 3 tetap nggak ada. DELETE idempoten. Idempoten itu soal",
                    "    keadaan data, kodenya boleh beda.",
                    "  - GET nggak mengubah apa pun, jadi jelas idempoten.",
                    "  - PATCH belum tentu. PATCH \"tambah stok 5\" yang dikirim dua",
                    "    kali menambah 10.",
                    "",
                    "Sifat ini penting karena jaringan nggak bisa dipercaya. Klien",
                    "yang nggak menerima jawaban nggak tahu apakah permintaannya",
                    "sampai atau hilang. Mengirim ulang PUT atau DELETE aman.",
                    "Mengirim ulang POST pembayaran bisa memotong saldo dua kali.",
                    "Untuk POST yang berbahaya, banyak API meminta header",
                    "Idempotency-Key berisi kode unik dari klien. Server yang melihat",
                    "kode yang sama dua kali cukup mengembalikan jawaban yang dulu.",
                    "Header itu masih berupa draf standar di IETF, tapi sudah lazim",
                    "dipakai layanan pembayaran. Penerapannya dibahas di bab",
                    "Otorisasi.",
                ],
            },
            {
                "heading": "Paginasi: jangan kirim sejuta baris",
                "body": [
                    "GET /buku di toko dengan sejuta buku nggak boleh mengirim",
                    "sejuta baris sekaligus. Daftar dipecah jadi halaman. Ada dua",
                    "cara yang umum:",
                    "",
                    "Paginasi offset memakai nomor halaman:",
                    "  GET /buku?page=3&per_page=20",
                    "Di database jadinya LIMIT 20 OFFSET 40. Gampang dibuat, dan",
                    "klien bisa langsung melompat ke halaman 50. Kekurangannya, kalau",
                    "ada buku baru masuk saat pengguna pindah halaman, satu buku",
                    "bergeser dan tampil dua kali. Offset yang besar juga makin",
                    "lambat, karena database tetap harus melewati baris-baris yang",
                    "dilompati.",
                    "",
                    "Paginasi cursor memakai penanda posisi terakhir:",
                    "  GET /buku?limit=20&after=eyJpZCI6MTAyfQ",
                    "Penanda after biasanya kode acak bagi klien yang isinya \"lanjut",
                    "sesudah id 102\". Di database jadinya WHERE id > 102. Hasilnya",
                    "stabil walaupun ada data baru, dan cepat di halaman berapa pun.",
                    "Kekurangannya, klien nggak bisa melompat ke halaman tertentu.",
                    "Timeline media sosial dan riwayat transaksi biasanya memakai",
                    "cara ini.",
                    "",
                    "Apa pun caranya, sertakan keterangan halaman di respons, misalnya",
                    "objek meta berisi total, dan tautan next serta prev. Klien",
                    "tinggal mengikuti tautan, nggak perlu menyusun alamat sendiri.",
                ],
            },
            {
                "heading": "Versi API dan REST yang \"sungguhan\"",
                "body": [
                    "API yang sudah dipakai orang nggak boleh diubah seenaknya.",
                    "Mengganti nama field nama jadi nama_lengkap membuat semua",
                    "aplikasi lama rusak. Perubahan seperti itu dikeluarkan sebagai",
                    "versi baru. Cara yang paling sering dipakai adalah menaruh versi",
                    "di alamat: /v1/buku dan /v2/buku. Ada juga yang memakai header.",
                    "Contohnya API REST GitHub, yang membaca header",
                    "X-GitHub-Api-Version berisi tanggal versi. Menambah field baru",
                    "biasanya aman tanpa versi baru, asal klien mengabaikan field",
                    "yang nggak ia kenal.",
                    "",
                    "Satu lagi soal nama. Banyak API yang menyebut dirinya REST",
                    "aslinya cuma JSON lewat HTTP dengan alamat yang rapi. Menurut",
                    "Fielding, REST yang utuh juga menuntut HATEOAS (Hypermedia as the",
                    "Engine of Application State). Artinya respons membawa tautan ke",
                    "aksi berikutnya. Klien cukup tahu alamat pintu masuknya, sisanya",
                    "mengikuti tautan. Bagian ini jarang diterapkan penuh. Model",
                    "kematangan Richardson menggolongkan API dalam empat tingkat,",
                    "dari satu alamat untuk semuanya (tingkat 0), sumber daya",
                    "(tingkat 1), metode HTTP yang tepat (tingkat 2), sampai tautan",
                    "hypermedia (tingkat 3). Kebanyakan API publik yang rapi berhenti",
                    "di tingkat 2, dan untuk dipakai sehari-hari itu sudah cukup.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dokumentasi API publik yang besar memakai pola yang sama.",
                    "Contohnya API REST GitHub: GET /repos/{owner}/{repo}/issues untuk",
                    "daftar issue, POST ke alamat yang sama untuk membuat issue, dan",
                    "PATCH /repos/{owner}/{repo}/issues/{nomor} untuk mengubahnya.",
                    "Respons daftarnya dipecah per halaman dan membawa tautan",
                    "halaman berikutnya di header Link.",
                    "",
                    "Kasus kecil: perpustakaan sekolah sudah punya API dengan alamat",
                    "/getBuku, /tambahBuku, /hapusBuku?id=5, dan /cariBukuByPenulis.",
                    "Semua alamat itu memakai POST, dan selalu dibalas 200. Kamu",
                    "diminta merapikannya tanpa membuat aplikasi lama mendadak",
                    "rusak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan sumber dayanya: buku. Koleksinya /buku, itemnya",
                    "     /buku/{id}.",
                    "  2. Petakan tiap alamat lama ke metode yang tepat:",
                    "       /getBuku            -> GET    /v1/buku",
                    "       /tambahBuku         -> POST   /v1/buku       (201)",
                    "       /hapusBuku?id=5     -> DELETE /v1/buku/5     (204)",
                    "       /cariBukuByPenulis  -> GET    /v1/buku?penulis=...",
                    "  3. Tambahkan paginasi di GET /v1/buku sejak awal, karena",
                    "     menambahkannya belakangan termasuk perubahan yang merusak",
                    "     klien lama.",
                    "  4. Biarkan alamat lama tetap hidup sementara, lalu umumkan",
                    "     batas waktu kapan alamat lama dimatikan.",
                ],
            },
        ],
    },
    {
        "title": "6. Validasi Input dan Pesan Error yang Jelas",
        "sections": [
            {
                "body": [
                    "Aturan pertama membuat API: jangan percaya data yang masuk.",
                    "Form di frontend boleh sudah mengecek umur minimal 13, tapi",
                    "siapa pun bisa mengirim permintaan langsung dengan curl dan",
                    "melewati form itu. Pengecekan di frontend cuma untuk kenyamanan",
                    "pengguna. Pengecekan yang menentukan ada di backend.",
                    "",
                    "Validasi adalah pengecekan bahwa data yang masuk berbentuk",
                    "benar dan isinya masuk akal: field wajib ada, tipenya benar,",
                    "angkanya di rentang yang wajar, teksnya nggak kepanjangan. Data",
                    "yang lolos validasi baru boleh diproses dan disimpan.",
                    "",
                    "Ada dua jenis kesalahan yang sebaiknya dibedakan:",
                    "  - Body yang nggak bisa dibaca sama sekali, misalnya JSON",
                    "    terpotong atau kurung kurawalnya kurang. Balas 400 Bad",
                    "    Request.",
                    "  - Body yang bisa dibaca, tapi isinya melanggar aturan, misalnya",
                    "    umur berisi teks atau email tanpa @. Balas 422 Unprocessable",
                    "    Content.",
                    "",
                    "Pembagian ini dipakai FastAPI dan banyak API lain. Sebagian",
                    "framework, misalnya ASP.NET Core, membalas 400 untuk keduanya.",
                    "Dua-duanya sah. Yang penting satu API konsisten memakai satu",
                    "aturan.",
                ],
            },
            {
                "heading": "Menjelaskan bentuk data dengan JSON Schema",
                "body": [
                    "Aturan validasi bisa ditulis sebagai kode, bisa juga sebagai",
                    "data. JSON Schema adalah bahasa standar untuk menjelaskan bentuk",
                    "JSON yang sah. Versi yang dipakai sekarang bernama 2020-12, dan",
                    "OpenAPI 3.1 serta 3.2 memakai versi itu. Skema untuk data",
                    "pendaftaran kira-kira begini:",
                ],
            },
            {
                "heading": "Skema pendaftaran",
                "bahasa": "json",
                "code": """{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["nama", "umur", "email"],
  "properties": {
    "nama": {"type": "string", "minLength": 1, "maxLength": 80},
    "umur": {"type": "integer", "minimum": 13},
    "email": {"type": "string", "format": "email"}
  },
  "additionalProperties": false
}""",
            },
            {
                "body": [
                    "Satu skema bisa dipakai di banyak tempat: untuk memvalidasi",
                    "permintaan di backend, untuk dokumentasi, dan untuk membangkitkan",
                    "form di frontend. additionalProperties false artinya field lain",
                    "di luar daftar ditolak. Ini mencegah klien menyelipkan field",
                    "seperti \"is_admin\": true yang nggak seharusnya bisa diisi.",
                    "",
                    "Di framework, kamu jarang menulis JSON Schema dengan tangan.",
                    "Biasanya aturan ditulis di bahasa pemrogramannya, lalu skema",
                    "dibangkitkan otomatis:",
                    "  - Pydantic di Python: kelas dengan type hints. FastAPI",
                    "    memakainya, dibahas di bab 4.",
                    "  - Zod di TypeScript: skema yang sekaligus menurunkan tipe",
                    "    TypeScript. Dipakai bersama Express di bab 3.",
                    "  - FluentValidation di .NET: aturan ditulis berantai seperti",
                    "    RuleFor(x => x.Umur).GreaterThanOrEqualTo(13).",
                    "",
                    "Supaya kelihatan apa yang dikerjakan pustaka-pustaka itu,",
                    "contoh berikut menulis validasi dengan tangan dan membalas",
                    "errornya dalam format standar.",
                ],
            },
            {
                "heading": "Validasi dan Problem Details dengan tangan",
                "code": "import json\n\n\ndef validasi(data):\n    \"\"\"Kumpulkan semua kesalahan sekaligus, jangan berhenti di yang pertama.\"\"\"\n    galat = []\n    nama = data.get(\"nama\")\n    if not isinstance(nama, str) or not nama.strip():\n        galat.append({\"field\": \"nama\", \"pesan\": \"wajib diisi\"})\n    umur = data.get(\"umur\")\n    if not isinstance(umur, int) or isinstance(umur, bool):\n        galat.append({\"field\": \"umur\", \"pesan\": \"harus bilangan bulat\"})\n    elif umur < 13:\n        galat.append({\"field\": \"umur\", \"pesan\": \"minimal 13\"})\n    if \"@\" not in str(data.get(\"email\", \"\")):\n        galat.append({\"field\": \"email\", \"pesan\": \"format email salah\"})\n    return galat\n\n\ndef daftar(teks):\n    try:\n        data = json.loads(teks)\n    except json.JSONDecodeError as e:\n        return 400, {\"type\": \"about:blank\", \"title\": \"Bad Request\",\n                     \"status\": 400, \"detail\": f\"JSON rusak di kolom {e.colno}\"}\n    galat = validasi(data) if isinstance(data, dict) else [\n        {\"field\": \"\", \"pesan\": \"body harus objek JSON\"}]\n    if galat:\n        return 422, {\"type\": \"https://toko.test/masalah/validasi\",\n                     \"title\": \"Data pendaftaran nggak sah\", \"status\": 422,\n                     \"detail\": f\"{len(galat)} field bermasalah\",\n                     \"errors\": galat}\n    return 201, {\"nama\": data[\"nama\"]}\n\n\nfor body in ['{\"nama\": \"Sari\", \"umur\": 17, \"email\": \"sari@toko.test\"}',\n             '{\"nama\": \"Sari\",',\n             '{\"nama\": \"\", \"umur\": \"12\", \"email\": \"sari\"}']:\n    status, isi = daftar(body)\n    print(status, json.dumps(isi, indent=2))",
            },
            {
                "body": [
                    "Keluaran:",
                    "201 {",
                    "  \"nama\": \"Sari\"",
                    "}",
                    "400 {",
                    "  \"type\": \"about:blank\",",
                    "  \"title\": \"Bad Request\",",
                    "  \"status\": 400,",
                    "  \"detail\": \"JSON rusak di kolom 17\"",
                    "}",
                    "422 {",
                    "  \"type\": \"https://toko.test/masalah/validasi\",",
                    "  \"title\": \"Data pendaftaran nggak sah\",",
                    "  \"status\": 422,",
                    "  \"detail\": \"3 field bermasalah\",",
                    "  \"errors\": [",
                    "    {",
                    "      \"field\": \"nama\",",
                    "      \"pesan\": \"wajib diisi\"",
                    "    },",
                    "    {",
                    "      \"field\": \"umur\",",
                    "      \"pesan\": \"harus bilangan bulat\"",
                    "    },",
                    "    {",
                    "      \"field\": \"email\",",
                    "      \"pesan\": \"format email salah\"",
                    "    }",
                    "  ]",
                    "}",
                    "",
                    "Perhatikan permintaan ketiga. Tiga kesalahan dilaporkan",
                    "sekaligus. Kalau validasi berhenti di kesalahan pertama,",
                    "pengguna harus mengirim form tiga kali untuk menemukan tiga",
                    "kesalahan.",
                    "",
                    "Perhatikan juga umur \"12\" berupa teks ditolak walaupun isinya",
                    "angka. Beberapa pustaka, termasuk Pydantic dalam mode bawaannya,",
                    "mau mengubah \"12\" jadi 12 secara otomatis. Itu pilihan desain;",
                    "yang penting kamu tahu pustakamu melakukannya atau nggak.",
                ],
            },
            {
                "heading": "Problem Details: bentuk error yang seragam",
                "body": [
                    "Tanpa kesepakatan, tiap API punya bentuk error sendiri. Ada yang",
                    "{\"error\": \"...\"}, ada yang {\"message\": \"...\"}, ada yang",
                    "{\"errors\": [...]}. Klien yang memakai lima API harus menulis",
                    "lima cara membaca error.",
                    "",
                    "RFC 9457 (Problem Details for HTTP APIs), terbit Juli 2023,",
                    "menetapkan bentuk standarnya. RFC ini menggantikan RFC 7807 yang",
                    "lebih lama, dan isinya hampir sama, jadi kalau kamu menemukan",
                    "dokumentasi yang menyebut 7807, maksudnya hal yang sama. Respons",
                    "error memakai Content-Type application/problem+json, dengan",
                    "field berikut:",
                    "  type      alamat yang menjelaskan jenis masalahnya; about:blank",
                    "            kalau nggak ada penjelasan khusus",
                    "  title     ringkasan singkat yang sama untuk semua kejadian",
                    "            sejenis",
                    "  status    kode status HTTP, diulang di body",
                    "  detail    penjelasan untuk kejadian yang ini",
                    "  instance  alamat kejadian ini, misalnya /daftar/8812 (opsional)",
                    "",
                    "Field tambahan boleh ditambahkan, seperti errors di contoh tadi.",
                    "Kalau type berisi about:blank, title sebaiknya sama dengan frasa",
                    "kode statusnya, misalnya Bad Request.",
                    "",
                    "Jebakan: jangan pernah mengirim stack trace atau pesan error",
                    "database ke klien. Pesan seperti duplicate key value violates",
                    "unique constraint \"users_email_key\" membocorkan nama tabel dan",
                    "kolommu. Catat detailnya di log server, kirim ke klien kalimat",
                    "yang aman dan berguna.",
                    "",
                    "Framework besar sudah mendukung format ini. ASP.NET Core punya",
                    "ProblemDetails bawaan, Spring punya kelas ProblemDetail, dan di",
                    "FastAPI atau Express kamu bisa memasangnya lewat handler error.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Form pendaftaran di aplikasi besar menandai semua field yang",
                    "salah sekaligus, masing-masing dengan pesannya di bawah kotak",
                    "isian. Yang membuat itu mungkin adalah backend yang membalas",
                    "daftar error lengkap dengan nama field-nya, seperti contoh di",
                    "materi ini, sehingga frontend tinggal menempelkan tiap pesan ke",
                    "kotak yang tepat.",
                    "",
                    "Kasus kecil: API toko membalas error dengan bentuk berbeda-beda.",
                    "Login salah membalas {\"msg\": \"gagal\"}, stok habis membalas",
                    "teks polos \"Stok habis\", dan data salah membalas 500 dengan",
                    "stack trace Python. Tim aplikasi Android mengeluh.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Sepakati satu bentuk untuk semua error: Problem Details",
                    "     dengan Content-Type application/problem+json.",
                    "  2. Buat satu fungsi pembantu supaya bentuknya nggak melenceng:",
                    "       def masalah(status, title, detail, **tambahan):",
                    "           return status, {\"type\": \"about:blank\",",
                    "                           \"title\": title, \"status\": status,",
                    "                           \"detail\": detail, **tambahan}",
                    "  3. Ganti tiap balasan error lama dengan fungsi itu, dengan kode",
                    "     yang tepat: 401 untuk login salah, 409 untuk stok habis, 422",
                    "     untuk data salah lengkap dengan errors per field.",
                    "  4. Tangkap semua exception yang lolos di satu tempat, catat ke",
                    "     log, lalu balas 500 dengan detail umum tanpa stack trace.",
                ],
            },
        ],
    },
    {
        "title": "7. Dokumentasi dan Pengujian API dengan OpenAPI",
        "sections": [
            {
                "body": [
                    "API dipakai orang lain: tim frontend, tim aplikasi ponsel, atau",
                    "perusahaan mitra. Mereka perlu tahu alamat apa saja yang ada,",
                    "data apa yang harus dikirim, dan balasan apa yang bakal datang.",
                    "Dokumentasi yang ditulis tangan di dokumen terpisah biasanya",
                    "cepat basi. Kode berubah, dokumennya lupa diubah.",
                    "",
                    "OpenAPI Specification adalah format standar untuk menjelaskan",
                    "API REST dalam satu berkas YAML atau JSON. Dulu namanya Swagger;",
                    "sejak versi 3 namanya OpenAPI, dan Swagger sekarang jadi nama",
                    "keluarga alatnya. Versi terbarunya saat materi ini ditulis",
                    "(Oktober 2026) adalah 3.2.1, perbaikan teks dari 3.2.0 yang",
                    "terbit September 2025. Versi 3.2 menambah tag bersarang, metode",
                    "HTTP tambahan, dan cara menjelaskan respons streaming seperti",
                    "SSE. Banyak alat masih paling lancar dengan 3.1, jadi contoh di",
                    "bawah memakai 3.1.1.",
                ],
            },
            {
                "heading": "Dokumen OpenAPI kecil",
                "bahasa": "yaml",
                "code": """openapi: 3.1.1
info:
  title: API Toko Buku
  version: 1.0.0
paths:
  /buku:
    get:
      summary: Daftar buku
      responses:
        "200":
          description: Daftar buku per halaman
    post:
      summary: Tambah buku
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Buku"
      responses:
        "201":
          description: Buku berhasil dibuat
        "422":
          description: Data nggak sah
  /buku/{id}:
    get:
      summary: Detail buku
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        "200":
          description: Satu buku
        "404":
          description: Buku nggak ada
components:
  schemas:
    Buku:
      type: object
      required: [judul]
      properties:
        judul:
          type: string
          minLength: 1""",
            },
            {
                "body": [
                    "Bagian-bagiannya:",
                    "  - openapi: versi spesifikasi yang dipakai berkas ini.",
                    "  - info: nama dan versi API-mu sendiri, nggak ada hubungannya",
                    "    dengan versi spesifikasi.",
                    "  - paths: daftar alamat, lalu metode di bawahnya, lalu",
                    "    parameter, body permintaan, dan kemungkinan respons.",
                    "  - components: bagian yang dipakai berulang, misalnya skema",
                    "    Buku. Bagian lain merujuknya dengan $ref, jadi skemanya",
                    "    cukup ditulis sekali. Skema di sini memakai JSON Schema",
                    "    yang dibahas di materi sebelumnya.",
                    "",
                    "Dari satu berkas ini bisa lahir banyak hal: halaman",
                    "dokumentasi, kode klien untuk berbagai bahasa, server tiruan",
                    "(mock) untuk tim frontend, dan tes yang mengecek apakah server",
                    "menepati janjinya.",
                    "",
                    "Ada dua cara membuat berkas ini. Design-first: berkas OpenAPI",
                    "ditulis dan disepakati dulu, baru kode dibuat. Code-first:",
                    "kode ditulis dulu, lalu framework membangkitkan berkasnya.",
                    "FastAPI, NestJS, ASP.NET Core (lewat paket",
                    "Microsoft.AspNetCore.OpenApi), dan Spring (lewat springdoc)",
                    "bisa melakukan cara kedua. Mulai .NET 9, templat ASP.NET Core",
                    "nggak lagi menyertakan Swashbuckle dan beralih ke paket bawaan",
                    "Microsoft itu.",
                ],
            },
            {
                "heading": "Membaca dokumen OpenAPI dari program",
                "code": "DOKUMEN = {\n    \"openapi\": \"3.1.1\",\n    \"info\": {\"title\": \"API Toko Buku\", \"version\": \"1.0.0\"},\n    \"paths\": {\n        \"/buku\": {\n            \"get\": {\"summary\": \"Daftar buku\", \"responses\": {\"200\": {}}},\n            \"post\": {\"summary\": \"Tambah buku\",\n                     \"responses\": {\"201\": {}, \"422\": {}}},\n        },\n        \"/buku/{id}\": {\n            \"get\": {\"summary\": \"Detail buku\",\n                    \"responses\": {\"200\": {}, \"404\": {}}},\n            \"delete\": {\"summary\": \"Hapus buku\",\n                       \"responses\": {\"204\": {}, \"404\": {}}},\n        },\n    },\n}\n\nprint(DOKUMEN[\"info\"][\"title\"], DOKUMEN[\"info\"][\"version\"])\nfor path, operasi in DOKUMEN[\"paths\"].items():\n    for metode, op in operasi.items():\n        kode = \", \".join(op[\"responses\"])\n        print(f\"  {metode.upper():6} {path:11} {op['summary']:12} [{kode}]\")\n\n\ndef sesuai_kontrak(metode, path, status):\n    \"\"\"Apakah status ini memang dijanjikan dokumen untuk operasi itu?\"\"\"\n    op = DOKUMEN[\"paths\"].get(path, {}).get(metode.lower())\n    return op is not None and str(status) in op[\"responses\"]\n\n\nprint(sesuai_kontrak(\"POST\", \"/buku\", 201))\nprint(sesuai_kontrak(\"POST\", \"/buku\", 400))\nprint(sesuai_kontrak(\"PATCH\", \"/buku/{id}\", 200))",
            },
            {
                "body": [
                    "Keluaran:",
                    "API Toko Buku 1.0.0",
                    "  GET    /buku       Daftar buku  [200]",
                    "  POST   /buku       Tambah buku  [201, 422]",
                    "  GET    /buku/{id}  Detail buku  [200, 404]",
                    "  DELETE /buku/{id}  Hapus buku   [204, 404]",
                    "True",
                    "False",
                    "False",
                    "",
                    "Berkas OpenAPI cuma data biasa, jadi program bisa membacanya.",
                    "Fungsi sesuai_kontrak itu bentuk paling sederhana dari tes",
                    "kontrak (contract test): server yang membalas 400 untuk POST",
                    "/buku sedang mengingkari dokumennya sendiri, karena yang",
                    "dijanjikan cuma 201 dan 422. Alat seperti Schemathesis dan",
                    "Dredd melakukan hal ini secara lengkap, sampai ke bentuk",
                    "body-nya.",
                ],
            },
            {
                "heading": "Swagger UI dan klien API",
                "body": [
                    "Swagger UI membaca berkas OpenAPI lalu menampilkannya sebagai",
                    "halaman web interaktif. Tiap endpoint punya tombol Try it out",
                    "untuk mencoba langsung dari browser. Lisensinya Apache-2.0, dan",
                    "versi terbarunya saat materi ini ditulis adalah 5.33.3. Redoc",
                    "dan Scalar adalah alternatif yang tampilannya lebih modern dan",
                    "makin sering dipakai.",
                    "",
                    "Untuk menguji API selama pengembangan, kamu butuh klien API,",
                    "yaitu program untuk menyusun dan mengirim permintaan:",
                    "  - curl: perintah terminal yang ada di hampir semua komputer.",
                    "    Cocok untuk satu-dua permintaan dan untuk skrip.",
                    "  - Postman: aplikasi paling populer. Survei Stack Overflow 2026",
                    "    mencatat 32,6% responden memakai Postman atau Newman (versi",
                    "    baris perintahnya). Lisensinya proprietary dengan paket",
                    "    gratis, dan banyak fiturnya butuh akun cloud.",
                    "  - Bruno: open source berlisensi MIT. Koleksi permintaan",
                    "    disimpan sebagai berkas teks biasa, jadi bisa ikut masuk",
                    "    repositori Git bersama kodenya, tanpa akun. Pemakainya",
                    "    masih kecil (0,6% di survei yang sama) tapi tumbuh.",
                    "  - Insomnia: buatan Kong, berlisensi Apache-2.0, mendukung REST,",
                    "    GraphQL, gRPC, dan WebSocket.",
                    "",
                    "Editor seperti VS Code (dengan ekstensi REST Client) dan IDE",
                    "JetBrains juga bisa menjalankan berkas .http, yaitu berkas teks",
                    "berisi permintaan HTTP mentah seperti yang kamu pelajari di",
                    "bab 1:",
                ],
            },
            {
                "heading": "berkas buku.http",
                "bahasa": "http",
                "code": """### Daftar buku halaman 2
GET http://localhost:8000/buku?page=2
Accept: application/json

### Tambah buku
POST http://localhost:8000/buku
Content-Type: application/json

{"judul": "Ronggeng Dukuh Paruk"}""",
            },
            {
                "heading": "Dengan curl",
                "bahasa": "terminal",
                "code": "curl -i 'http://localhost:8000/buku?page=2'\n\ncurl -i -X POST http://localhost:8000/buku \\\n  -H 'Content-Type: application/json' \\\n  -d '{\"judul\": \"Ronggeng Dukuh Paruk\"}'",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak perusahaan menerbitkan berkas OpenAPI untuk API publiknya,",
                    "misalnya GitHub yang menaruh deskripsi OpenAPI API REST-nya di",
                    "repositori github/rest-api-description. Di proyek kantor, berkas",
                    "seperti itu biasanya ikut disimpan di repositori, dan halaman",
                    "Swagger UI-nya dibuka tim frontend tiap kali mereka butuh",
                    "contoh permintaan.",
                    "",
                    "Kasus kecil: tim aplikasi Android sering salah memanggil API",
                    "karena dokumentasinya berupa dokumen teks yang sudah enam bulan",
                    "nggak diperbarui. Kamu memakai FastAPI dan ingin dokumentasinya",
                    "selalu cocok dengan kode.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pakai pendekatan code-first. FastAPI membangkitkan berkas",
                    "     OpenAPI di /openapi.json dan Swagger UI di /docs dari kode",
                    "     yang sama.",
                    "  2. Isi summary dan contoh di kodenya, supaya halaman",
                    "     dokumentasi nggak cuma berisi daftar alamat.",
                    "  3. Simpan salinan berkas OpenAPI ke repositori di tiap rilis:",
                    "       curl -s http://localhost:8000/openapi.json > openapi.json",
                    "  4. Bandingkan berkas itu dengan rilis sebelumnya. Field yang",
                    "     hilang atau berganti nama langsung kelihatan sebagai",
                    "     perubahan yang merusak klien, sebelum aplikasinya rilis.",
                ],
            },
        ],
    },
    {
        "title": "8. CORS: Saat Browser Menolak Respons API",
        "sections": [
            {
                "body": [
                    "Hampir semua orang yang membuat API pertamanya ketemu pesan ini",
                    "di konsol browser: blocked by CORS policy: No",
                    "'Access-Control-Allow-Origin' header is present. Anehnya, API",
                    "yang sama bisa dipanggil lancar lewat curl atau Postman.",
                    "",
                    "Penyebabnya aturan keamanan di browser yang namanya same-origin",
                    "policy. Kode JavaScript di sebuah halaman cuma boleh membaca",
                    "respons dari asal (origin) yang sama dengan halamannya. Asal",
                    "adalah gabungan tiga hal: skema, nama host, dan port.",
                    "  https://toko.test        dan https://toko.test/api   sama",
                    "  https://toko.test        dan https://api.toko.test   beda host",
                    "  http://localhost:5173    dan http://localhost:8000   beda port",
                    "  http://toko.test         dan https://toko.test       beda skema",
                    "",
                    "Aturan ini melindungi penggunanya. Tanpa aturan itu, halaman",
                    "situs iseng yang kamu buka bisa memanggil API bank tanpa kamu sadari",
                    "dengan cookie login milikmu, lalu membaca saldomu.",
                ],
            },
            {
                "heading": "CORS: izin dari server",
                "body": [
                    "CORS (Cross-Origin Resource Sharing) adalah cara server",
                    "memberi izin supaya halaman dari asal lain boleh membaca",
                    "responsnya. Izin itu dikirim lewat header Access-Control-*.",
                    "Aturannya bagian dari Fetch Standard yang dikelola WHATWG.",
                    "",
                    "Untuk permintaan sederhana, misalnya GET biasa, browser",
                    "mengirim permintaannya, lalu memeriksa respons. Kalau respons",
                    "membawa Access-Control-Allow-Origin yang cocok dengan asal",
                    "halaman, JavaScript boleh membacanya. Kalau nggak, browser",
                    "menyembunyikan respons itu dan menulis error di konsol.",
                    "",
                    "Untuk permintaan yang lebih berisiko, browser bertanya dulu.",
                    "Pertanyaan ini disebut preflight: permintaan OPTIONS yang",
                    "dikirim browser sendiri sebelum permintaan aslinya. Preflight",
                    "terjadi kalau permintaannya memakai metode selain GET, HEAD,",
                    "dan POST, membawa header di luar daftar aman (misalnya",
                    "Authorization), atau memakai Content-Type selain tiga jenis",
                    "bawaan form. Content-Type application/json termasuk yang",
                    "memicu preflight, jadi hampir semua panggilan API dari",
                    "JavaScript melewati preflight.",
                ],
            },
            {
                "heading": "Menentukan header CORS",
                "code": "ASAL_DIIZINKAN = {\"https://toko.test\", \"https://admin.toko.test\"}\n\n\ndef header_cors(metode, origin, metode_diminta=None):\n    \"\"\"Header CORS yang ditambahkan server ke respons.\"\"\"\n    if origin not in ASAL_DIIZINKAN:\n        return {}                 # tanpa header: browser yang memblokir\n    header = {\"Access-Control-Allow-Origin\": origin, \"Vary\": \"Origin\"}\n    if metode == \"OPTIONS\" and metode_diminta:      # ini preflight\n        header[\"Access-Control-Allow-Methods\"] = \"GET, POST, PATCH, DELETE\"\n        header[\"Access-Control-Allow-Headers\"] = \"Content-Type, Authorization\"\n        header[\"Access-Control-Max-Age\"] = \"600\"\n    return header\n\n\nkasus = [\n    (\"GET\", \"https://toko.test\", None),\n    (\"OPTIONS\", \"https://admin.toko.test\", \"DELETE\"),\n    (\"GET\", \"https://situs-iseng.test\", None),\n]\nfor metode, origin, diminta in kasus:\n    print(metode, origin)\n    hasil = header_cors(metode, origin, diminta)\n    for nama, nilai in hasil.items():\n        print(\"  \", nama + \":\", nilai)\n    if not hasil:\n        print(\"   (nggak ada header CORS)\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "GET https://toko.test",
                    "   Access-Control-Allow-Origin: https://toko.test",
                    "   Vary: Origin",
                    "OPTIONS https://admin.toko.test",
                    "   Access-Control-Allow-Origin: https://admin.toko.test",
                    "   Vary: Origin",
                    "   Access-Control-Allow-Methods: GET, POST, PATCH, DELETE",
                    "   Access-Control-Allow-Headers: Content-Type, Authorization",
                    "   Access-Control-Max-Age: 600",
                    "GET https://situs-iseng.test",
                    "   (nggak ada header CORS)",
                    "",
                    "Arti tiap header:",
                    "  - Allow-Origin: asal yang diizinkan membaca respons.",
                    "  - Allow-Methods dan Allow-Headers: jawaban preflight, metode",
                    "    dan header apa saja yang boleh dipakai permintaan aslinya.",
                    "  - Max-Age: berapa detik browser boleh mengingat jawaban",
                    "    preflight, supaya nggak bertanya ulang tiap kali.",
                    "  - Vary: Origin: memberi tahu cache bahwa respons ini berbeda",
                    "    untuk tiap asal. Tanpa itu, cache bisa menyajikan respons",
                    "    untuk toko.test ke halaman admin.toko.test.",
                    "",
                    "Server mengulang asal yang cocok dari daftar izin, bukan",
                    "menulis tanda bintang. Allow-Origin: * memang mengizinkan semua",
                    "asal, tapi nggak boleh dipakai bersama",
                    "Access-Control-Allow-Credentials: true. Browser menolak",
                    "kombinasi itu, karena artinya setiap situs boleh membaca data",
                    "pengguna yang sedang login.",
                ],
            },
            {
                "heading": "Yang sering salah dipahami",
                "body": [
                    "Ingat: CORS melindungi pengguna browser, bukan servermu. curl,",
                    "Postman, dan program backend lain nggak peduli header CORS sama",
                    "sekali. Siapa pun tetap bisa memanggil API-mu dari luar",
                    "browser. Jadi jangan pernah mengandalkan CORS sebagai pengganti",
                    "login atau pengecekan izin.",
                    "",
                    "Hal kedua: untuk permintaan sederhana, server tetap menjalankan",
                    "permintaannya. Browser cuma menyembunyikan responsnya dari",
                    "JavaScript. POST form biasa dari situs lain tetap sampai dan",
                    "tetap diproses. Perlindungan dari serangan seperti itu (CSRF)",
                    "adalah urusan lain, dibahas di bab Autentikasi.",
                    "",
                    "Jebakan: jalan pintas \"izinkan semua asal\" yang sering",
                    "disarankan di forum. Selama pengembangan mungkin terasa praktis,",
                    "tapi kebiasaan itu sering terbawa ke produksi. Tulis daftar asal",
                    "yang memang dipakai, dan baca daftarnya dari konfigurasi supaya",
                    "beda antara laptop dan server.",
                    "",
                    "Di framework, kamu jarang menulis header ini sendiri. Express",
                    "punya paket cors, FastAPI punya CORSMiddleware, Flask punya",
                    "ekstensi Flask-CORS, dan ASP.NET Core punya AddCors. Semuanya",
                    "menerima daftar asal yang diizinkan, lalu menjawab preflight",
                    "secara otomatis. Saat pengembangan, alternatifnya adalah proxy",
                    "di server pengembangan frontend (misalnya fitur proxy di Vite),",
                    "sehingga browser mengira API berasal dari asal yang sama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola paling umum di proyek web modern: frontend React atau Vue",
                    "dilayani dari https://app.contoh.test, sedangkan API dari",
                    "https://api.contoh.test. Karena host-nya beda, API wajib",
                    "mengirim header CORS untuk asal app.contoh.test. Saat",
                    "pengembangan, frontend biasanya jalan di http://localhost:5173",
                    "dan API di http://localhost:8000, yang juga beda asal karena",
                    "port-nya beda.",
                    "",
                    "Kasus kecil: frontend di http://localhost:5173 memanggil",
                    "fetch(\"http://localhost:8000/pesanan\", {method: \"DELETE\",",
                    "headers: {Authorization: \"Bearer ...\"}}). Konsol menulis error",
                    "CORS, padahal GET /pesanan dari halaman yang sama lancar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka tab Network. Kelihatan permintaan OPTIONS /pesanan",
                    "     yang dibalas 404 atau tanpa header Allow-Methods. Itu",
                    "     preflight, dipicu metode DELETE dan header Authorization.",
                    "  2. Pastikan server menjawab OPTIONS untuk alamat itu dengan",
                    "     status 2xx, bukan diteruskan ke router biasa yang nggak",
                    "     mengenal OPTIONS.",
                    "  3. Sertakan izinnya di jawaban preflight:",
                    "       Access-Control-Allow-Origin: http://localhost:5173",
                    "       Access-Control-Allow-Methods: GET, POST, DELETE",
                    "       Access-Control-Allow-Headers: Authorization, Content-Type",
                    "  4. Coba lagi. Preflight sekarang 204, lalu DELETE yang asli",
                    "     menyusul dan responsnya bisa dibaca JavaScript.",
                ],
            },
        ],
    },
    {
        "title": "9. Node.js dan Express: Server JavaScript Pertama",
        "sections": [
            {
                "body": [
                    "Bab ini butuh kurikulum JavaScript, terutama fungsi, modul, dan",
                    "async/await. Untuk dua materi NestJS kamu juga butuh kurikulum",
                    "TypeScript. Kalau belum, kamu boleh melompat ke bab 4 (Python)",
                    "dulu dan kembali ke sini nanti.",
                    "",
                    "JavaScript lahir untuk browser. Node.js adalah program yang",
                    "menjalankan JavaScript di luar browser, misalnya di server.",
                    "Mesinnya V8, mesin JavaScript yang sama dengan Chrome, ditambah",
                    "pustaka untuk membaca berkas, membuka koneksi jaringan, dan",
                    "menjalankan server HTTP.",
                    "",
                    "Node.js teknologi yang paling banyak dipakai di kategori web",
                    "framework dan teknologi pada Survei Stack Overflow 2026: 46,4%",
                    "responden. Express, framework yang dibahas di materi ini, dipakai",
                    "15,6%. Satu bahasa untuk frontend dan backend memang menarik:",
                    "kamu cuma perlu menguasai satu bahasa untuk membuat aplikasi web",
                    "utuh.",
                ],
            },
            {
                "heading": "Versi Node.js yang dipakai sekarang",
                "body": [
                    "Node.js punya dua jenis rilis. Rilis Current berisi fitur",
                    "terbaru. Rilis LTS (Long Term Support) dirawat bertahun-tahun",
                    "dan itulah yang dipakai di server produksi. Saat materi ini",
                    "ditulis (Oktober 2026), keadaannya begini:",
                    "  - Node.js 24 \"Krypton\" adalah LTS aktif, versi 24.22.0.",
                    "  - Node.js 26 masih Current (26.12.0) dan dijadwalkan jadi LTS",
                    "    pada 28 Oktober 2026.",
                    "  - Node.js 22 masih menerima perbaikan sampai April 2027.",
                    "  - Node.js 20 sudah berhenti dirawat sejak April 2026. Jangan",
                    "    dipakai untuk proyek baru.",
                    "",
                    "Mulai Node.js 27, jadwalnya berubah: satu versi mayor per tahun,",
                    "dan setiap versi mayor jadi LTS sesudah enam bulan. Dulu cuma",
                    "versi bernomor genap yang jadi LTS. Cek jadwal terbarunya di",
                    "nodejs.org sebelum memilih versi untuk proyekmu.",
                    "",
                    "Node.js versi baru juga bisa menjalankan berkas .ts yang",
                    "sederhana secara langsung. Fitur ini disebut type stripping:",
                    "anotasi tipe dibuang begitu saja tanpa dicek. Untuk proyek",
                    "besar, pengecekan tipe tetap pakai tsc dari TypeScript.",
                ],
            },
            {
                "heading": "Event loop: satu juru masak yang nggak pernah menunggu",
                "body": [
                    "Node.js menjalankan kode JavaScript-mu di satu thread. Bayangkan",
                    "satu juru masak di dapur warung. Ia menaruh panci di kompor,",
                    "lalu langsung memotong sayur untuk pesanan lain tanpa menunggu",
                    "airnya mendidih. Begitu air mendidih, ia kembali ke panci itu.",
                    "",
                    "Begitu juga Node. Saat kode meminta data dari database atau",
                    "berkas, Node menyerahkan pekerjaan menunggu itu ke sistem operasi",
                    "dan langsung melayani permintaan lain. Saat datanya siap, fungsi",
                    "lanjutannya dimasukkan ke antrean. Mekanisme yang mengambil",
                    "pekerjaan dari antrean satu per satu itu namanya event loop.",
                    "",
                    "Urutannya bisa kamu lihat sendiri:",
                ],
            },
            {
                "heading": "Urutan eksekusi di event loop",
                "bahasa": "javascript",
                "code": """console.log("1. kode biasa jalan duluan");

setTimeout(() => {
  console.log("4. setTimeout 0 ms, giliran antrean timer");
}, 0);

Promise.resolve().then(() => {
  console.log("3. promise selesai, didahulukan sebelum timer");
});

console.log("2. kode biasa berikutnya, nggak menunggu siapa pun");""",
            },
            {
                "body": [
                    "Keluaran:",
                    "1. kode biasa jalan duluan",
                    "2. kode biasa berikutnya, nggak menunggu siapa pun",
                    "3. promise selesai, didahulukan sebelum timer",
                    "4. setTimeout 0 ms, giliran antrean timer",
                    "",
                    "Kode biasa selalu selesai dulu. Sesudah itu baru antrean",
                    "dikerjakan: lanjutan promise lebih dulu, lalu timer. Walaupun",
                    "timernya 0 milidetik, ia tetap harus menunggu giliran.",
                    "",
                    "Jebakan: karena juru masaknya cuma satu, kerja CPU yang berat",
                    "membuat semua pelanggan menunggu. Fungsi yang mengolah gambar",
                    "atau menghitung laporan besar selama dua detik membuat seluruh",
                    "server diam dua detik, termasuk untuk pengguna yang cuma minta",
                    "halaman kecil. Pindahkan kerja seperti itu ke worker_threads,",
                    "ke proses terpisah, atau ke antrean tugas (dibahas di bab 13).",
                ],
            },
            {
                "heading": "Server HTTP tanpa framework",
                "bahasa": "javascript",
                "code": """const http = require("node:http");

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Halo dari Node");
    return;
  }
  res.writeHead(404);
  res.end();
});

// menyalakan server, jalankan di komputermu sendiri
...
server.listen(3000, () => console.log("http://localhost:3000"));""",
            },
            {
                "body": [
                    "Modul node:http adalah versi Node dari kontrak \"aplikasi =",
                    "fungsi\" di bab 1: fungsi yang menerima objek req dan res.",
                    "Semua sisanya kamu tulis sendiri, termasuk mencocokkan alamat",
                    "dan membaca body JSON yang datang sepotong-sepotong. Express",
                    "mengerjakan bagian itu untukmu.",
                ],
            },
            {
                "heading": "Memasang Express",
                "bahasa": "terminal",
                "code": """mkdir toko-api && cd toko-api
npm init -y
npm install express
node app.js""",
            },
            {
                "heading": "app.js",
                "bahasa": "javascript",
                "code": """const express = require("express");

const app = express();
app.use(express.json()); // middleware: isi req.body dari JSON

const produk = [{ id: 1, nama: "Pensil", harga: 3000 }];

app.get("/produk", (req, res) => {
  res.json(produk);
});

app.get("/produk/:id", (req, res) => {
  const item = produk.find((p) => p.id === Number(req.params.id));
  if (!item) return res.status(404).json({ error: "nggak ada" });
  res.json(item);
});

app.post("/produk", (req, res) => {
  const baru = { id: produk.length + 1, ...req.body };
  produk.push(baru);
  res.status(201).json(baru);
});

app.listen(3000, () => console.log("http://localhost:3000"));""",
            },
            {
                "body": [
                    "Semua konsep di bab 1 muncul di sini dengan nama lain:",
                    "  router             ->  app.get, app.post, app.delete, ...",
                    "  parameter path     ->  :id, dibaca lewat req.params.id",
                    "  query string       ->  req.query",
                    "  middleware         ->  app.use(fungsi)",
                    "  lanjut ke berikut  ->  next()",
                    "  respons            ->  res.status(201).json(...)",
                    "",
                    "Nilai req.params.id selalu string, makanya diubah dengan Number",
                    "sebelum dibandingkan. Tanpa express.json(), req.body kosong",
                    "(undefined di Express 5), karena Express nggak membaca body",
                    "kalau nggak diminta.",
                ],
            },
            {
                "heading": "Express 5 dan tutorial lama",
                "body": [
                    "Express 5 stabil sejak Oktober 2024. Versi terbarunya saat",
                    "materi ini ditulis adalah 5.3.0, dan jalur 4.x masih menerima",
                    "perbaikan. Masalahnya, sebagian besar tutorial di internet masih",
                    "ditulis untuk Express 4. Perbedaan yang paling sering bikin",
                    "bingung:",
                    "  - Error di handler async diteruskan otomatis ke penangan",
                    "    error. Di Express 4, promise yang ditolak bisa membuat",
                    "    permintaan menggantung kalau kamu lupa .catch(next).",
                    "  - Wildcard wajib bernama: tulis /*splat, bukan /*. Parameter",
                    "    opsional ditulis dengan kurung kurawal, misalnya",
                    "    /:file{.:ext}, bukan /:file.:ext?.",
                    "  - req.query nggak bisa ditimpa lagi.",
                    "  - Beberapa method lama dihapus: app.del jadi app.delete,",
                    "    res.sendfile jadi res.sendFile, dan res.json(obj, 201) jadi",
                    "    res.status(201).json(obj).",
                    "  - Express 5 butuh Node.js 18 ke atas.",
                    "",
                    "Kalau contoh dari internet error dengan pesan tentang",
                    "path-to-regexp, hampir pasti itu sintaks rute Express 4.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Express sering dipakai sebagai backend API untuk frontend React",
                    "atau Vue, sebagai server kecil di belakang aplikasi ponsel, dan",
                    "sebagai fondasi framework lain. NestJS, misalnya, memakai",
                    "Express di bawahnya secara bawaan. Banyak lowongan backend",
                    "Node.js menyebut Express sebagai syarat, karena hampir semua",
                    "kode Node lama memakainya.",
                    "",
                    "Kasus kecil: kamu menyalin contoh dari blog tahun 2021 ke proyek",
                    "Express 5. Rute app.get(\"/berkas/*\", ...) membuat aplikasi",
                    "gagal menyala dengan error dari path-to-regexp, dan handler",
                    "async yang gagal membaca database membuat permintaan",
                    "menggantung di server lama temanmu yang masih Express 4.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek versi yang terpasang dengan npm ls express.",
                    "  2. Di Express 5, beri nama wildcard-nya:",
                    "       app.get(\"/berkas/*jalur\", (req, res) => {",
                    "         res.json({ jalur: req.params.jalur });",
                    "       });",
                    "  3. Di server Express 4, bungkus handler async dengan",
                    "     try/catch lalu panggil next(err), atau tingkatkan ke",
                    "     Express 5 yang meneruskan error async secara otomatis.",
                    "  4. Untuk migrasi proyek besar, tim Express menyediakan",
                    "     codemod: npx codemod@latest @expressjs/v5-migration-recipe.",
                ],
            },
        ],
    },
    {
        "title": "10. API Express Lengkap dengan Validasi dan Prisma",
        "sections": [
            {
                "body": [
                    "app.js satu berkas cukup untuk mencoba. Begitu API punya puluhan",
                    "rute, validasi, dan database, satu berkas jadi sulit dirawat.",
                    "Express nggak memaksakan struktur folder apa pun. Itu kelebihan",
                    "sekaligus kekurangannya: tiap tim harus memutuskan sendiri.",
                    "",
                    "Struktur yang umum dipakai memisahkan rute, middleware, dan",
                    "akses data:",
                ],
            },
            {
                "heading": "Struktur folder",
                "bahasa": "teks",
                "code": """toko-api/
  package.json
  prisma.config.ts
  prisma/
    schema.prisma        model dan tabel
    migrations/          riwayat perubahan skema
  src/
    app.js               merakit middleware dan rute
    server.js            menyalakan app.listen
    routes/buku.js       rute /buku
    middleware/validasi.js
    db.js                satu objek PrismaClient""",
            },
            {
                "body": [
                    "app.js dipisah dari server.js supaya aplikasinya bisa diuji",
                    "tanpa menyalakan port. Pustaka tes seperti supertest menerima",
                    "objek app dan memanggilnya langsung, mirip fungsi panggil di",
                    "materi kontrak aplikasi di bab 1.",
                    "",
                    "Rute untuk satu sumber daya dikumpulkan di express.Router(),",
                    "lalu dipasang di app.js dengan awalan alamatnya. Validasi",
                    "memakai Zod, pustaka skema untuk JavaScript dan TypeScript.",
                    "Versi terbarunya saat materi ini ditulis adalah 4.6.7. Zod 4",
                    "(rilis 2025) lebih cepat dari Zod 3 dan punya varian kecil",
                    "bernama zod/mini.",
                ],
            },
            {
                "heading": "src/middleware/validasi.js",
                "bahasa": "javascript",
                "code": """// Pabrik middleware: terima skema Zod, kembalikan middleware Express.
function validasi(skema) {
  return (req, res, next) => {
    const hasil = skema.safeParse(req.body);
    if (!hasil.success) {
      return res.status(422).type("application/problem+json").json({
        type: "about:blank",
        title: "Unprocessable Content",
        status: 422,
        detail: "Data buku nggak sah",
        errors: hasil.error.issues.map((i) => ({
          field: i.path.join("."),
          pesan: i.message,
        })),
      });
    }
    req.body = hasil.data; // data yang sudah bersih dan bertipe benar
    next();
  };
}

module.exports = { validasi };""",
            },
            {
                "heading": "src/routes/buku.js",
                "bahasa": "javascript",
                "code": """const express = require("express");
const { z } = require("zod");
const { validasi } = require("../middleware/validasi");

const router = express.Router();
const buku = new Map([[1, { id: 1, judul: "Laskar Pelangi", tahun: 2005 }]]);
let idBerikut = 2;

const SkemaBuku = z.object({
  judul: z.string().trim().min(1, "judul wajib diisi").max(200),
  tahun: z.number().int().min(1900).max(2100),
});

router.get("/", (req, res) => {
  res.json([...buku.values()]);
});

router.post("/", validasi(SkemaBuku), (req, res) => {
  const item = { id: idBerikut++, ...req.body };
  buku.set(item.id, item);
  res.status(201).location(`/buku/${item.id}`).json(item);
});

module.exports = router;""",
            },
            {
                "heading": "src/app.js",
                "bahasa": "javascript",
                "code": """const express = require("express");
const rutBuku = require("./routes/buku");

const app = express();
app.use(express.json());
app.use("/buku", rutBuku);

// Penangan error: empat parameter, didaftarkan paling akhir.
app.use((err, req, res, next) => {
  console.error(err); // detail lengkap cuma masuk log server
  const status = err.status ?? 500;
  res.status(status).json({
    title: status < 500 ? err.message : "Internal Server Error",
    status,
  });
});

module.exports = app;""",
            },
            {
                "body": [
                    "Contoh ini sudah dijalankan dengan Express 5.3.0 dan Zod 4.6.7.",
                    "Mengirim {\"judul\": \"  \", \"tahun\": \"1980\"} ke POST /buku",
                    "menghasilkan 422 dengan dua error: judul wajib diisi (spasi",
                    "dibuang dulu oleh trim) dan tahun bukan angka. Body yang JSON-nya",
                    "terpotong ditolak express.json() dengan status 400 lalu sampai",
                    "ke penangan error, karena error dari pembaca JSON membawa",
                    "err.status.",
                    "",
                    "Penangan error dikenali Express dari jumlah parameternya: empat.",
                    "Kalau kamu menulisnya dengan tiga parameter, Express",
                    "menganggapnya middleware biasa. Ia juga harus didaftarkan",
                    "paling akhir, sesudah semua rute.",
                ],
            },
            {
                "heading": "Prisma: database dengan klien bertipe",
                "body": [
                    "Data di Map hilang begitu server mati. Untuk menyimpan ke",
                    "database, banyak proyek Node memakai ORM. ORM (Object-Relational",
                    "Mapping) adalah pustaka yang menerjemahkan objek di kode jadi",
                    "baris di tabel dan sebaliknya, jadi kamu jarang menulis SQL",
                    "sendiri. Prisma salah satu yang paling populer di Node dan",
                    "TypeScript.",
                    "",
                    "Cara kerja Prisma berbeda dari ORM lain. Model ditulis di berkas",
                    "schema.prisma, lalu Prisma membangkitkan klien bertipe dari",
                    "berkas itu. Editor jadi bisa menebak nama tabel dan kolom, dan",
                    "salah ketik ketahuan sebelum kode dijalankan.",
                    "",
                    "Soal versi, ada yang sering bikin bingung. Prisma 7 meninggalkan",
                    "mesin kueri berbahasa Rust dan menggantinya dengan penyusun",
                    "kueri berbahasa TypeScript. Klien sekarang butuh driver adapter,",
                    "yaitu paket penghubung ke driver database, misalnya",
                    "@prisma/adapter-better-sqlite3. Versi produksi terbarunya saat",
                    "materi ini ditulis adalah 7.10.1. Anehnya, tag latest di npm",
                    "sekarang menunjuk 8.0.0-rc, versi yang belum final. Jadi",
                    "sebutkan versinya secara eksplisit saat memasang.",
                ],
            },
            {
                "heading": "Memasang Prisma 7",
                "bahasa": "terminal",
                "code": """npm install -D prisma@7 @types/better-sqlite3
npm install @prisma/client@7 @prisma/adapter-better-sqlite3 dotenv
npx prisma init --datasource-provider sqlite

# sesudah menulis model:
npx prisma migrate dev --name buat-tabel-buku
npx prisma generate""",
            },
            {
                "heading": "prisma/schema.prisma",
                "bahasa": "prisma",
                "code": """generator client {
  provider = "prisma-client"
  output   = "../generated/prisma"
}

datasource db {
  provider = "sqlite"
}

model Buku {
  id        Int      @id @default(autoincrement())
  judul     String
  tahun     Int
  penulis   Penulis  @relation(fields: [penulisId], references: [id])
  penulisId Int
  dibuat    DateTime @default(now())
}

model Penulis {
  id   Int    @id @default(autoincrement())
  nama String @unique
  buku Buku[]
}""",
            },
            {
                "heading": "src/db.ts dan pemakaiannya",
                "bahasa": "typescript",
                "code": """import "dotenv/config";
import { PrismaBetterSqlite3 } from "@prisma/adapter-better-sqlite3";
import { PrismaClient } from "../generated/prisma/client";

const adapter = new PrismaBetterSqlite3({ url: process.env.DATABASE_URL });
export const prisma = new PrismaClient({ adapter });

// di handler GET /buku?page=2
const daftar = await prisma.buku.findMany({
  where: { tahun: { gte: 2000 } },
  include: { penulis: true },  // ikut ambil data penulis
  orderBy: { judul: "asc" },
  skip: 10,
  take: 10,
});

// di handler POST /buku, sesudah lolos validasi Zod
const baru = await prisma.buku.create({
  data: { judul: "Bumi Manusia", tahun: 1980, penulisId: 3 },
});""",
            },
            {
                "body": [
                    "URL database diambil dari variabel lingkungan DATABASE_URL di",
                    "berkas .env, misalnya file:./dev.db untuk SQLite. Berkas",
                    "prisma.config.ts yang dibuat prisma init memberi tahu Prisma",
                    "letak skema, folder migrasi, dan URL itu.",
                    "",
                    "Dua kode error Prisma yang paling sering kamu tangkap: P2002",
                    "saat data melanggar kolom unik (jawab 409), dan P2025 saat data",
                    "yang mau diubah atau dihapus nggak ada (jawab 404). Soal",
                    "migrasi, indeks, dan transaksi dibahas mendalam di kurikulum",
                    "Database.",
                    "",
                    "Prisma bukan satu-satunya pilihan. Drizzle, Sequelize, Knex,",
                    "TypeORM, dan lainnya dibandingkan di materi peta ORM pada bab",
                    "10. TypeORM juga dipakai di materi NestJS sesudah ini.",
                ],
            },
            {
                "heading": "Halaman HTML dari server: template engine",
                "body": [
                    "Nggak semua backend cuma mengirim JSON. Panel admin sederhana",
                    "atau halaman toko bisa dirakit di server, lalu dikirim sebagai",
                    "HTML jadi. Alat yang menggabungkan data dengan kerangka HTML",
                    "disebut template engine. Di Express, template engine dipasang",
                    "dengan app.set(\"view engine\", \"ejs\"), lalu dipakai dengan",
                    "res.render(\"daftar-buku\", { buku }).",
                    "",
                    "Tiga yang paling sering ditemui di proyek Express:",
                    "  - EJS: HTML biasa dengan sisipan JavaScript. Versi terbarunya",
                    "    7.0.2, lisensi Apache-2.0.",
                    "  - Pug (dulu Jade): HTML ditulis tanpa tag penutup, susunannya",
                    "    ditentukan indentasi, misalnya baris li= b.judul. Rilisnya",
                    "    makin jarang, jadi kurang cocok untuk proyek baru.",
                    "  - Handlebars: template tanpa logika rumit, nilai ditulis",
                    "    {{judul}}, dengan helper untuk perulangan dan kondisi.",
                ],
            },
            {
                "heading": "views/daftar-buku.ejs",
                "bahasa": "html",
                "code": """<h1>Daftar Buku</h1>
<ul>
  <% buku.forEach((b) => { %>
    <li><%= b.judul %> (<%= b.tahun %>)</li>
  <% }) %>
</ul>""",
            },
            {
                "body": [
                    "Jebakan: di EJS, <%= %> meng-escape HTML, sedangkan <%- %>",
                    "menulis apa adanya. Judul buku berisi <script> yang ditulis",
                    "pakai <%- %> bakal dijalankan browser pembaca. Itu celah XSS.",
                    "Pakai <%- %> cuma untuk HTML yang kamu buat sendiri. Handlebars",
                    "punya aturan yang mirip: {{ }} aman, {{{ }}} mentah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak startup memulai backend-nya dengan susunan seperti di",
                    "materi ini: Express, validasi skema, dan ORM, dengan app.js",
                    "terpisah dari server.js supaya tesnya cepat. Saat kodenya",
                    "membesar, sebagian pindah ke framework yang lebih terstruktur",
                    "seperti NestJS, yang dibahas berikutnya.",
                    "",
                    "Kasus kecil: toko buku ingin GET /buku bisa disaring tahun dan",
                    "dipecah per halaman. Saat ini handler-nya mengambil semua baris",
                    "dengan prisma.buku.findMany() lalu memotongnya di JavaScript.",
                    "Dengan 50 ribu buku, permintaan itu lambat sekali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Validasi query dulu dengan Zod. z.coerce mengubah teks dari",
                    "     query string jadi angka:",
                    "       const Q = z.object({",
                    "         page: z.coerce.number().int().min(1).default(1),",
                    "         tahun: z.coerce.number().int().optional(),",
                    "       });",
                    "  2. Teruskan saringan dan halaman ke database lewat where, skip,",
                    "     dan take, supaya yang diambil cuma 10 baris:",
                    "       const q = Q.parse(req.query);",
                    "       prisma.buku.findMany({ where: { tahun: q.tahun },",
                    "         skip: (q.page - 1) * 10, take: 10 });",
                    "  3. Hitung total dengan prisma.buku.count({ where }) untuk",
                    "     mengisi meta paginasi.",
                    "  4. Bandingkan waktunya. Database cuma mengirim 10 baris, bukan",
                    "     50 ribu.",
                ],
            },
        ],
    },
    {
        "title": "11. NestJS: Modul, Controller, dan Provider",
        "sections": [
            {
                "body": [
                    "Express memberi kebebasan penuh. Di tim berisi sepuluh orang,",
                    "kebebasan itu sering berujung sepuluh gaya: ada yang menaruh",
                    "query database di rute, ada yang di folder services, ada yang",
                    "di models. Orang baru harus mempelajari aturan tak tertulis",
                    "tiap proyek.",
                    "",
                    "NestJS adalah framework Node.js yang menetapkan strukturnya",
                    "sejak awal. Ia ditulis dengan TypeScript, memakai decorator",
                    "(tanda @ di atas kelas dan method), dan terinspirasi Angular",
                    "serta Spring. Di bawahnya, NestJS tetap memakai Express secara",
                    "bawaan, atau Fastify kalau kamu memilihnya.",
                    "",
                    "NestJS dipakai 5,8% responden Survei Stack Overflow 2026, dan",
                    "pemakaiannya terus naik. Versi terbarunya saat materi ini",
                    "ditulis adalah 12.1.3. NestJS 12 memakai ES module, jadi proyek",
                    "barunya menulis impor berkas lokal dengan akhiran .js, misalnya",
                    "./buku.service.js, walaupun berkas aslinya .ts.",
                ],
            },
            {
                "heading": "Tiga bahan utama",
                "body": [
                    "  - Controller: kelas yang menerima permintaan HTTP. Method-nya",
                    "    ditandai @Get, @Post, dan seterusnya. Tugasnya cuma membaca",
                    "    permintaan dan menyerahkan pekerjaan.",
                    "  - Provider: kelas yang mengerjakan sesuatu, biasanya service",
                    "    berisi logika bisnis atau repository yang bicara dengan",
                    "    database. Ditandai @Injectable.",
                    "  - Modul: kelas bertanda @Module yang mengelompokkan controller",
                    "    dan provider untuk satu fitur. Aplikasi punya satu modul akar",
                    "    (AppModule) yang mengimpor modul-modul fitur.",
                    "",
                    "Proyek baru dan berkas-berkas fitur dibuat dengan CLI Nest:",
                ],
            },
            {
                "heading": "Membuat proyek dan satu fitur",
                "bahasa": "terminal",
                "code": """npx @nestjs/cli new toko-api
cd toko-api
npx nest generate resource buku   # modul, controller, service, DTO
npm run start:dev                 # menyala ulang tiap berkas berubah""",
            },
            {
                "heading": "src/buku/buku.service.ts",
                "bahasa": "typescript",
                "code": """import { Injectable, NotFoundException } from "@nestjs/common";

export interface Buku {
  id: number;
  judul: string;
}

@Injectable()
export class BukuService {
  private readonly buku: Buku[] = [{ id: 1, judul: "Laskar Pelangi" }];

  semua(): Buku[] {
    return this.buku;
  }

  satu(id: number): Buku {
    const item = this.buku.find((b) => b.id === id);
    if (!item) throw new NotFoundException(`Buku ${id} nggak ada`);
    return item;
  }
}""",
            },
            {
                "heading": "src/buku/buku.controller.ts",
                "bahasa": "typescript",
                "code": """import { Controller, Get, Param, ParseIntPipe } from "@nestjs/common";
import { BukuService } from "./buku.service.js";

@Controller("buku")
export class BukuController {
  // Nest yang membuat BukuService lalu mengopernya ke sini.
  constructor(private readonly bukuService: BukuService) {}

  @Get()
  semua() {
    return this.bukuService.semua(); // otomatis jadi JSON
  }

  @Get(":id")
  satu(@Param("id", ParseIntPipe) id: number) {
    return this.bukuService.satu(id);
  }
}""",
            },
            {
                "heading": "src/buku/buku.module.ts dan src/app.module.ts",
                "bahasa": "typescript",
                "code": """import { Module } from "@nestjs/common";
import { BukuController } from "./buku.controller.js";
import { BukuService } from "./buku.service.js";

@Module({
  controllers: [BukuController],
  providers: [BukuService],
  exports: [BukuService], // boleh dipakai modul lain yang mengimpor
})
export class BukuModule {}

// app.module.ts
@Module({ imports: [BukuModule] })
export class AppModule {}""",
            },
            {
                "body": [
                    "Perhatikan apa yang nggak ada di kode itu. Nggak ada app.get,",
                    "nggak ada res.json, dan nggak ada new BukuService(). Decorator",
                    "@Controller(\"buku\") dan @Get(\":id\") memberi tahu Nest rute",
                    "mana yang ditangani method mana. Nilai yang dikembalikan method",
                    "otomatis dikirim sebagai JSON dengan status 200 (201 untuk",
                    "@Post). NotFoundException otomatis jadi respons 404.",
                    "",
                    "ParseIntPipe mengubah \":id\" dari string jadi number. Kalau",
                    "isinya bukan angka, misalnya /buku/abc, Nest langsung membalas",
                    "400 sebelum method-nya dipanggil.",
                ],
            },
            {
                "heading": "Dependency injection",
                "body": [
                    "Konsep terpenting di NestJS adalah dependency injection (DI).",
                    "Dependensi adalah objek lain yang dibutuhkan sebuah kelas untuk",
                    "bekerja. BukuController butuh BukuService. Ada dua cara",
                    "mendapatkannya:",
                    "  - Kelas membuat sendiri: this.service = new BukuService().",
                    "    Controller jadi terikat ke satu jenis service, dan susah",
                    "    diganti service palsu saat dites.",
                    "  - Kelas menerima dari luar lewat constructor. Itulah dependency",
                    "    injection: dependensi \"disuntikkan\" oleh pihak lain.",
                    "",
                    "Ide dasarnya nggak butuh framework. Contoh ini JavaScript polos:",
                ],
            },
            {
                "heading": "Dependency injection dengan tangan",
                "bahasa": "javascript",
                "code": """// Tanpa framework: dependensi dioper lewat constructor.
class RepoBukuMemori {
  constructor() {
    this.data = [{ id: 1, judul: "Laskar Pelangi" }];
  }
  semua() {
    return this.data;
  }
}

class RepoBukuPalsu {
  semua() {
    return [{ id: 99, judul: "Buku Uji" }];
  }
}

class BukuService {
  constructor(repo) {
    this.repo = repo; // service nggak peduli repo jenis apa
  }
  judulSemua() {
    return this.repo.semua().map((b) => b.judul);
  }
}

const asli = new BukuService(new RepoBukuMemori());
const uji = new BukuService(new RepoBukuPalsu());
console.log("produksi:", asli.judulSemua());
console.log("tes     :", uji.judulSemua());""",
            },
            {
                "body": [
                    "Keluaran:",
                    "produksi: [ 'Laskar Pelangi' ]",
                    "tes     : [ 'Buku Uji' ]",
                    "",
                    "Kelas BukuService yang sama dipakai dengan dua repo berbeda,",
                    "tanpa diubah satu baris pun. Di aplikasi kecil, mengoper",
                    "dependensi dengan tangan masih gampang. Di aplikasi dengan",
                    "ratusan kelas, urusan \"siapa dibuat duluan dan dioper ke mana\"",
                    "jadi rumit. Di situ peran kontainer DI.",
                    "",
                    "Kontainer DI di NestJS membaca tipe parameter constructor.",
                    "Saat melihat constructor(private readonly bukuService:",
                    "BukuService), ia mencari provider BukuService di modul itu,",
                    "membuatnya kalau belum ada, lalu mengopernya. Secara bawaan tiap",
                    "provider cuma dibuat sekali (singleton) dan dipakai bersama.",
                    "Di latihan bab ini kamu membuat kontainer kecil seperti itu",
                    "sendiri.",
                    "",
                    "Jebakan: error Nest can't resolve dependencies of",
                    "BukuController hampir selalu berarti provider-nya belum",
                    "didaftarkan di providers modul itu, atau modul pemiliknya belum",
                    "diimpor dan belum mengekspor provider tersebut.",
                ],
            },
            {
                "heading": "Kapan memilih NestJS",
                "body": [
                    "NestJS cocok untuk tim yang lebih dari beberapa orang, aplikasi",
                    "yang bakal hidup bertahun-tahun, dan programmer yang datang",
                    "dari Java atau C#, karena polanya mirip Spring dan ASP.NET.",
                    "Strukturnya juga memudahkan pengujian, karena tiap provider bisa",
                    "diganti versi palsu lewat Test.createTestingModule.",
                    "",
                    "Untuk API kecil atau prototipe, Express atau Hono lebih cepat",
                    "dipakai. NestJS menambah banyak berkas dan konsep: modul,",
                    "decorator, pipe, guard, interceptor. Dokumentasi resminya",
                    "gratis dan lengkap; kursus resminya berbayar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "NestJS banyak dipakai untuk backend aplikasi perusahaan yang",
                    "ditulis TypeScript dari ujung ke ujung, misalnya frontend",
                    "Angular atau React dengan backend NestJS di satu monorepo.",
                    "Lowongan backend TypeScript sering menyebut NestJS bersama",
                    "TypeORM atau Prisma.",
                    "",
                    "Kasus kecil: fitur laporan butuh daftar buku dari BukuService.",
                    "Kamu membuat LaporanModule, lalu menyuntikkan BukuService ke",
                    "LaporanService. Aplikasi gagal menyala dengan pesan Nest can't",
                    "resolve dependencies of the LaporanService (?).",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesannya: tanda tanya menunjuk parameter constructor",
                    "     yang nggak ketemu, yaitu BukuService.",
                    "  2. Pastikan BukuModule mengekspor provider-nya:",
                    "       exports: [BukuService]",
                    "  3. Impor BukuModule di modul yang membutuhkan:",
                    "       @Module({ imports: [BukuModule],",
                    "                 providers: [LaporanService] })",
                    "  4. Jangan mendaftarkan BukuService lagi di providers",
                    "     LaporanModule. Itu membuat salinan kedua yang datanya",
                    "     terpisah dari salinan di BukuModule.",
                ],
            },
        ],
    },
    {
        "title": "12. NestJS dengan TypeORM, Pipe Validasi, dan Swagger",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menyimpan buku di array. Materi ini",
                    "melengkapinya jadi API sungguhan: data di database lewat",
                    "TypeORM, body divalidasi dengan pipe, dan dokumentasi OpenAPI",
                    "dibangkitkan otomatis. Semua kode di sini sudah dijalankan",
                    "dengan NestJS 12.1.3, TypeORM 1.1.2, @nestjs/typeorm 12.0.2,",
                    "dan @nestjs/swagger 12.0.2.",
                    "",
                    "TypeORM adalah ORM TypeScript yang memakai decorator, cocok",
                    "dengan gaya NestJS. Setelah bertahun-tahun di versi 0.3.x,",
                    "TypeORM akhirnya mencapai 1.x. Jalur 0.3.x sekarang disebut",
                    "legacy, dan banyak tutorial serta kode NestJS lama masih",
                    "memakainya. Prisma, MikroORM, dan Drizzle juga bisa dipakai di",
                    "NestJS.",
                ],
            },
            {
                "heading": "Memasang paketnya",
                "bahasa": "terminal",
                "code": """npm install @nestjs/typeorm typeorm pg
npm install class-validator class-transformer
npm install @nestjs/swagger""",
            },
            {
                "heading": "src/buku/buku.entity.ts",
                "bahasa": "typescript",
                "code": """import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn } from "typeorm";

@Entity()
export class Buku {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ length: 200 })
  judul: string;

  @Column()
  tahun: number;

  @CreateDateColumn()
  dibuatPada: Date;
}""",
            },
            {
                "body": [
                    "Entity adalah kelas yang mewakili satu tabel. Tiap properti",
                    "bertanda @Column jadi satu kolom. Lalu modul fitur mendaftarkan",
                    "entity itu, dan service menerima repository-nya lewat DI:",
                ],
            },
            {
                "heading": "Modul dan service dengan repository",
                "bahasa": "typescript",
                "code": """import { Injectable, Module, NotFoundException } from "@nestjs/common";
import { InjectRepository, TypeOrmModule } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { Buku } from "./buku.entity.js";
import { BuatBukuDto } from "./buat-buku.dto.js";

@Injectable()
export class BukuService {
  constructor(
    @InjectRepository(Buku)
    private readonly repo: Repository<Buku>,
  ) {}

  semua(): Promise<Buku[]> {
    return this.repo.find({ order: { id: "ASC" } });
  }

  async satu(id: number): Promise<Buku> {
    const buku = await this.repo.findOneBy({ id });
    if (!buku) throw new NotFoundException(`Buku ${id} nggak ada`);
    return buku;
  }

  tambah(data: BuatBukuDto): Promise<Buku> {
    return this.repo.save(this.repo.create(data));
  }
}

@Module({
  imports: [TypeOrmModule.forFeature([Buku])],
  controllers: [BukuController],
  providers: [BukuService],
})
export class BukuModule {}""",
            },
            {
                "heading": "Koneksi database di AppModule",
                "bahasa": "typescript",
                "code": """import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { BukuModule } from "./buku/buku.module.js";

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: "postgres",
      url: process.env.DATABASE_URL,
      autoLoadEntities: true, // entity dari forFeature ikut terdaftar
      synchronize: false,     // perubahan tabel lewat migrasi
    }),
    BukuModule,
  ],
})
export class AppModule {}""",
            },
            {
                "body": [
                    "Jebakan: banyak tutorial memasang synchronize: true. Dengan",
                    "itu, TypeORM mengubah tabel supaya cocok dengan entity setiap",
                    "kali aplikasi menyala. Enak untuk mencoba, berbahaya di",
                    "produksi: mengganti nama properti bisa berarti kolom lama",
                    "dihapus beserta isinya. Di produksi, pakai migrasi yang",
                    "dibangkitkan dan diperiksa dulu. Migrasi dibahas di kurikulum",
                    "Database.",
                ],
            },
            {
                "heading": "DTO dan ValidationPipe",
                "body": [
                    "DTO (Data Transfer Object) adalah kelas yang menjelaskan bentuk",
                    "data yang boleh masuk. Aturan validasinya ditulis sebagai",
                    "decorator dari pustaka class-validator:",
                ],
            },
            {
                "heading": "src/buku/buat-buku.dto.ts",
                "bahasa": "typescript",
                "code": """import { IsInt, IsString, Length, Max, Min } from "class-validator";
import { ApiProperty } from "@nestjs/swagger";

export class BuatBukuDto {
  @ApiProperty({ example: "Laskar Pelangi" })
  @IsString()
  @Length(1, 200)
  judul: string;

  @ApiProperty({ example: 2005 })
  @IsInt()
  @Min(1900)
  @Max(2100)
  tahun: number;
}""",
            },
            {
                "heading": "src/main.ts",
                "bahasa": "typescript",
                "code": """import { NestFactory } from "@nestjs/core";
import { ValidationPipe } from "@nestjs/common";
import { DocumentBuilder, SwaggerModule } from "@nestjs/swagger";
import { AppModule } from "./app.module.js";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(
    new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true }),
  );

  const konfig = new DocumentBuilder().setTitle("API Toko Buku").setVersion("1.0.0").build();
  SwaggerModule.setup("docs", app, SwaggerModule.createDocument(app, konfig));

  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();""",
            },
            {
                "body": [
                    "Pipe adalah langkah yang mengubah atau memeriksa data sebelum",
                    "sampai ke method controller. ParseIntPipe yang kamu lihat di",
                    "materi sebelumnya juga pipe. ValidationPipe memeriksa body",
                    "terhadap aturan di DTO. Pilihannya:",
                    "  - whitelist: properti yang nggak ada di DTO dibuang.",
                    "  - forbidNonWhitelisted: properti asing malah membuat",
                    "    permintaan ditolak. Ini mencegah klien menyelipkan field",
                    "    seperti isAdmin.",
                    "  - transform: body diubah jadi objek kelas DTO sungguhan.",
                    "",
                    "Saat diuji, POST /buku dikirimi {\"judul\": \"\", \"tahun\": 1800,",
                    "\"admin\": true}. Balasannya 400 berisi tiga pesan: property admin",
                    "should not exist, judul must be longer than or equal to 1",
                    "characters, dan tahun must not be less than 1900. Perhatikan",
                    "statusnya 400, bukan 422 seperti FastAPI. Kalau API-mu memilih",
                    "422, ValidationPipe menerima pilihan errorHttpStatusCode.",
                    "",
                    "SwaggerModule membaca controller, decorator, dan DTO, lalu",
                    "membangun dokumen OpenAPI. Halaman Swagger UI tersedia di /docs",
                    "dan dokumen JSON-nya di /docs-json. Saat diuji, dokumen yang",
                    "dihasilkan bertanda openapi 3.0.0. @ApiProperty menambahkan",
                    "contoh nilai ke dokumen itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Susunan NestJS + TypeORM atau Prisma + ValidationPipe + Swagger",
                    "adalah kerangka yang sering dipakai untuk API internal",
                    "perusahaan. Tim frontend membuka /docs untuk melihat bentuk",
                    "data, sementara backend menjaga aturan validasi di satu tempat,",
                    "yaitu DTO.",
                    "",
                    "Kasus kecil: penguji menemukan bahwa POST /anggota menerima",
                    "{\"nama\": \"Tono\", \"peran\": \"admin\"} dan anggota baru",
                    "langsung jadi admin. DTO-nya cuma punya field nama, tapi",
                    "service menyimpan seluruh body ke repository.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang ValidationPipe global dengan whitelist dan",
                    "     forbidNonWhitelisted di main.ts.",
                    "  2. Pastikan parameter controller bertipe DTO, bukan any:",
                    "       tambah(@Body() data: BuatAnggotaDto)",
                    "     Tanpa tipe kelas, ValidationPipe nggak tahu aturan apa",
                    "     yang harus diperiksa.",
                    "  3. Kirim ulang body yang sama. Sekarang dibalas 400 dengan",
                    "     pesan property peran should not exist.",
                    "  4. Tetapkan peran di service, misalnya peran: \"anggota\",",
                    "     jangan pernah diambil dari body.",
                ],
            },
        ],
    },
    {
        "title": "13. Peta Framework dan Runtime JavaScript",
        "sections": [
            {
                "body": [
                    "Express dan NestJS bukan satu-satunya pilihan. Ekosistem",
                    "JavaScript di server punya beberapa runtime dan belasan",
                    "framework. Materi ini memetakan semuanya supaya kamu bisa",
                    "mengenali nama yang muncul di lowongan kerja atau proyek warisan,",
                    "dan tahu mana yang layak dipilih untuk proyek baru.",
                    "",
                    "Angka versi di bawah adalah versi stabil terbaru saat materi ini",
                    "ditulis (Oktober 2026). Persentase berasal dari Survei Stack",
                    "Overflow 2026, kategori web framework dan teknologi.",
                ],
            },
            {
                "heading": "Runtime: tempat JavaScript dijalankan",
                "bahasa": "teks",
                "code": """runtime   versi    lisensi  catatan
Node.js   24 LTS   MIT      paling banyak dipakai, 46,4%
Deno      2.9.7    MIT      izin eksplisit, TypeScript bawaan, 4,0%
Bun       1.4.3    MIT      serba ada dan cepat, sekitar 9%""",
            },
            {
                "body": [
                    "Deno dibuat oleh pencipta Node.js sendiri, Ryan Dahl, untuk",
                    "memperbaiki hal yang ia sesali di Node. Program Deno nggak boleh",
                    "membaca berkas atau membuka jaringan kecuali diberi izin, misalnya",
                    "deno run --allow-net server.ts. TypeScript langsung jalan tanpa",
                    "langkah kompilasi. Sejak Deno 2 (2024), paket npm bisa dipakai",
                    "dengan lancar. Framework yang populer di Deno antara lain Oak.",
                    "",
                    "Bun menggabungkan runtime, pengelola paket, bundler, dan",
                    "penguji dalam satu program, dan terkenal karena kecepatannya.",
                    "Bun diakuisisi Anthropic pada Desember 2025 dan tetap open source",
                    "dengan lisensi MIT. Sebagian besar API Node didukung, tapi belum",
                    "semuanya. Uji dulu pustaka yang memakai modul native sebelum",
                    "memindahkan aplikasi produksi.",
                ],
            },
            {
                "heading": "Server kecil di Deno",
                "bahasa": "typescript",
                "code": """// jalankan dengan: deno run --allow-net server.ts
...
Deno.serve({ port: 8000 }, (req: Request) => {
  const url = new URL(req.url);
  return Response.json({ path: url.pathname });
});""",
            },
            {
                "body": [
                    "Perhatikan bentuknya: fungsi menerima Request dan mengembalikan",
                    "Response. Itu objek standar web yang sama dengan fetch di",
                    "browser. Bun dan Cloudflare Workers memakai bentuk yang sama,",
                    "dan framework Hono dibangun di atas bentuk itu.",
                ],
            },
            {
                "heading": "Framework yang aktif dipilih untuk proyek baru",
                "body": [
                    "Fastify (5.12.7, MIT, 3,5%) fokus pada kecepatan. Tiap rute",
                    "boleh membawa JSON Schema untuk body dan respons; skema itu",
                    "dipakai untuk validasi sekaligus mempercepat pembuatan JSON.",
                    "Logger Pino sudah bawaan, dan plugin-nya terenkapsulasi. Fastify",
                    "proyek di bawah OpenJS Foundation, dan versi 6 sedang alpha.",
                    "",
                    "Hono (4.13.13, MIT, 2,8%, dengan admired 51,2%) adalah framework",
                    "kecil di atas Request dan Response standar web. Kode yang sama",
                    "jalan di Cloudflare Workers, Deno, Bun, Node, dan AWS Lambda.",
                    "Hono mendapat kepuasan tertinggi di kategori back-end pada State",
                    "of JS 2025. Hono 5 sedang dalam tahap release candidate. Hono",
                    "cocok jadi framework kedua sesudah Express.",
                    "",
                    "Koa (3.2.1, MIT, 0,9%) dibuat tim pembuat Express, dengan",
                    "middleware gaya bawang memakai async/await, seperti yang kamu",
                    "lihat di bab 1. Koa 3 rilis 2025, tapi pemakaiannya tumbuh",
                    "pelan.",
                    "",
                    "AdonisJS (7.6.0, MIT) adalah framework lengkap bergaya Laravel:",
                    "ORM Lucid, autentikasi, validasi, dan CLI sudah satu paket. Cocok",
                    "untuk yang ingin semua keputusan sudah diambil framework.",
                ],
            },
            {
                "heading": "Hono dan Fastify sekilas",
                "bahasa": "javascript",
                "code": """// Hono
import { Hono } from "hono";
const app = new Hono();
app.get("/buku/:id", (c) => c.json({ id: c.req.param("id") }));
export default app;

// Fastify: skema body ikut menentukan validasi
import Fastify from "fastify";
const fastify = Fastify({ logger: true });
fastify.post("/buku", {
  schema: {
    body: {
      type: "object",
      required: ["judul"],
      properties: { judul: { type: "string", minLength: 1 } },
    },
  },
}, async (req, reply) => reply.code(201).send(req.body));""",
            },
            {
                "heading": "Yang khusus, menurun, atau warisan",
                "body": [
                    "hapi (21.4.10, BSD-3-Clause) awalnya dibuat di Walmart. Rute",
                    "ditulis sebagai objek konfigurasi, dengan validasi memakai Joi",
                    "dan sistem plugin yang kuat. Masih dirawat, tapi jarang dipilih",
                    "untuk proyek baru.",
                    "",
                    "ElysiaJS (1.4.30, MIT) dibuat khusus untuk Bun, dengan tipe",
                    "TypeScript yang tersambung dari rute sampai klien. Jalur 1.4.x",
                    "sekarang cuma menerima perbaikan keamanan, karena pengembangan",
                    "pindah ke Elysia 2 yang masih beta.",
                    "",
                    "Nitro (2.13.4, MIT) adalah toolkit server dari ekosistem UnJS",
                    "yang dipakai Nuxt, sehingga satu server bisa di-deploy ke banyak",
                    "platform. h3 adalah lapisan HTTP minimal di bawahnya. Biasanya",
                    "kamu bertemu Nitro lewat Nuxt di kurikulum Frontend.",
                    "",
                    "Meteor (3.5.2, MIT) platform full-stack lama dengan sinkronisasi",
                    "data real-time bawaan. Meteor 3 pindah ke async, tapi statusnya",
                    "menurun: masih dirawat, jarang dipilih untuk proyek baru.",
                    "",
                    "Sails.js (1.5.18, MIT) framework MVC bergaya Rails dengan ORM",
                    "Waterline dan API otomatis. Statusnya menurun, dan biasanya cuma",
                    "ditemui di proyek warisan.",
                    "",
                    "LoopBack (7.0.15, MIT) dari IBM/StrongLoop membangkitkan endpoint",
                    "REST dan OpenAPI dari model data. Masih rilis, komunitasnya kecil",
                    "dan menurun.",
                    "",
                    "Feathers (5.0.50, MIT) membuat API REST dan real-time sekaligus",
                    "dengan pola service yang seragam. Komunitasnya kecil tapi aktif,",
                    "dan versi 6 sedang disiapkan.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  - Belajar dan proyek pertama: Express. Paling banyak contoh,",
                    "    paling banyak dipakai di kode yang bakal kamu warisi.",
                    "  - Tim besar, TypeScript, aplikasi jangka panjang: NestJS.",
                    "  - Butuh cepat dan validasi berbasis skema: Fastify.",
                    "  - Jalan di edge seperti Cloudflare Workers, atau ingin satu",
                    "    kode untuk banyak runtime: Hono.",
                    "  - Ingin semua sudah lengkap ala Laravel: AdonisJS.",
                    "  - Meteor, Sails, dan LoopBack: pelajari kalau memang mewarisi",
                    "    proyeknya, jangan dipilih untuk proyek baru.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pilihan runtime dan framework biasanya ditentukan tempat",
                    "aplikasinya jalan. API yang dijalankan di Cloudflare Workers",
                    "atau Vercel Edge sering memakai Hono, karena runtime di sana",
                    "bukan Node penuh. API di server biasa atau kontainer Docker",
                    "lebih sering memakai Express, Fastify, atau NestJS di atas",
                    "Node LTS.",
                    "",
                    "Kasus kecil: timmu ingin mencoba Bun karena katanya lebih cepat.",
                    "API-nya memakai Express dan pustaka pengolah gambar yang",
                    "memakai modul native.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan seluruh tes otomatis dengan bun test atau bun run",
                    "     di cabang terpisah, tanpa mengubah kode.",
                    "  2. Perhatikan pustaka yang memakai modul native. Itu bagian",
                    "     yang paling mungkin belum didukung.",
                    "  3. Ukur waktu respons dengan beban yang sama di Node dan Bun,",
                    "     jangan cuma percaya angka di situs resminya.",
                    "  4. Kalau ada pustaka yang gagal, tetap di Node untuk produksi.",
                    "     Bun masih bisa dipakai sebagai pengelola paket dan penguji,",
                    "     karena bagian itu nggak memengaruhi server.",
                ],
            },
        ],
    },
    {
        "title": "14. Flask: Microframework yang Mudah Dibaca",
        "sections": [
            {
                "body": [
                    "Bab ini butuh kurikulum Python sampai decorator, type hints,",
                    "dan async. Kalau ada yang asing, buka lagi materinya di sana.",
                    "",
                    "Flask adalah framework web Python yang intinya kecil: routing,",
                    "objek permintaan dan respons, dan template. Hal lain seperti",
                    "database, login, atau form dipasang lewat ekstensi kalau memang",
                    "dibutuhkan. Karena itu Flask disebut microframework. Kata micro",
                    "di situ soal inti yang kecil; aplikasi Flask sendiri bisa besar.",
                    "",
                    "Flask dibangun dari beberapa proyek keluarga Pallets: Werkzeug",
                    "untuk urusan HTTP dan kontrak aplikasi, Jinja untuk template, dan Click",
                    "untuk perintah terminal. Versi terbarunya saat materi ini",
                    "ditulis (Oktober 2026) adalah 3.1.3, berlisensi BSD-3-Clause.",
                    "Survei Stack Overflow 2026 mencatat 12,5% responden memakainya,",
                    "dan survei State of Python 2025 mencatat 34% pengembang Python.",
                    "Pengguna barunya sekarang banyak beralih ke FastAPI, yang",
                    "dibahas di materi ketiga bab ini.",
                ],
            },
            {
                "heading": "Memasang dan menjalankan",
                "bahasa": "terminal",
                "code": """python3 -m venv .venv
source .venv/bin/activate
pip install flask
flask --app app run --debug    # buka http://127.0.0.1:5000""",
            },
            {
                "heading": "app.py",
                "code": """from flask import Flask, abort, render_template, request

app = Flask(__name__)

BUKU = {
    1: {"id": 1, "judul": "Laskar Pelangi", "tahun": 2005},
    2: {"id": 2, "judul": "Bumi Manusia", "tahun": 1980},
}


@app.get("/")
def beranda():
    return render_template("beranda.html", buku=BUKU.values())


@app.get("/api/buku")
def daftar_buku():
    tahun = request.args.get("tahun", type=int)
    return [b for b in BUKU.values() if tahun is None or b["tahun"] == tahun]


@app.get("/api/buku/<int:id_buku>")
def satu_buku(id_buku):
    if id_buku not in BUKU:
        abort(404)
    return BUKU[id_buku]


@app.post("/api/buku")
def tambah_buku():
    data = request.get_json(silent=True) or {}
    judul = str(data.get("judul", "")).strip()
    if not judul:
        return {"title": "Unprocessable Content", "status": 422,
                "detail": "judul wajib diisi"}, 422
    item = {"id": max(BUKU) + 1, "judul": judul, "tahun": data.get("tahun")}
    BUKU[item["id"]] = item
    return item, 201""",
            },
            {
                "body": [
                    "Bandingkan dengan router buatan sendiri di bab 1:",
                    "  - @app.get(\"/api/buku\") adalah decorator yang mendaftarkan",
                    "    fungsi di bawahnya ke tabel rute. Ada juga @app.post,",
                    "    @app.put, @app.delete, dan bentuk umum @app.route(...,",
                    "    methods=[...]).",
                    "  - <int:id_buku> adalah parameter path dengan konverter. Flask",
                    "    mengubahnya jadi int sebelum memanggil fungsimu. Alamat",
                    "    /api/buku/abc nggak cocok dengan pola itu, jadi dijawab 404",
                    "    tanpa fungsimu dipanggil.",
                    "  - request.args berisi query string, request.get_json() berisi",
                    "    body JSON. Keduanya diambil dari objek request global yang",
                    "    disiapkan Flask untuk tiap permintaan.",
                    "  - Fungsi yang mengembalikan dict atau list otomatis dikirim",
                    "    sebagai JSON. Tuple (isi, 201) menyetel kode status.",
                    "  - abort(404) menghentikan fungsi dan membalas 404.",
                    "",
                    "Ingat: --debug cuma untuk laptopmu. Mode debug menyalakan",
                    "debugger interaktif Werkzeug, yang membuat siapa pun yang bisa",
                    "membuka halaman error bisa menjalankan kode Python di server.",
                    "Jangan pernah menyalakannya di server yang bisa diakses orang.",
                ],
            },
            {
                "heading": "Template Jinja",
                "body": [
                    "Route beranda memanggil render_template. Flask mencari berkas",
                    "itu di folder templates, lalu mengisinya dengan Jinja, mesin",
                    "template Python yang versinya saat ini 3.1.6. Sintaksnya:",
                    "  {{ nilai }}           menulis nilai",
                    "  {% for ... %}         perintah, misalnya perulangan dan if",
                    "  {% extends \"...\" %}   mewarisi kerangka halaman lain",
                    "  {% block nama %}      bagian yang boleh diisi halaman anak",
                    "",
                    "Pewarisan membuat kerangka halaman cukup ditulis sekali di",
                    "dasar.html, lalu tiap halaman cuma mengisi bloknya:",
                ],
            },
            {
                "heading": "templates/dasar.html",
                "bahasa": "jinja",
                "code": """<!doctype html>
<html lang="id">
<head><title>{% block judul %}Toko Buku{% endblock %}</title></head>
<body>
  {% block isi %}{% endblock %}
</body>
</html>""",
            },
            {
                "heading": "templates/beranda.html",
                "bahasa": "jinja",
                "code": """{% extends "dasar.html" %}
{% block isi %}
  <h1>Daftar Buku</h1>
  <ul>
    {% for b in buku %}
      <li>{{ b.judul }} ({{ b.tahun }})</li>
    {% else %}
      <li>Belum ada buku.</li>
    {% endfor %}
  </ul>
{% endblock %}""",
            },
            {
                "body": [
                    "Bagian {% else %} di dalam for jalan kalau daftarnya kosong.",
                    "Itu fitur khas Jinja yang menghemat satu if.",
                    "",
                    "Untuk berkas berakhiran .html, Flask menyalakan autoescape:",
                    "karakter seperti < dan > di dalam {{ }} diubah jadi &lt; dan",
                    "&gt;. Saat diuji, judul berisi <b>Bumi</b> tampil sebagai teks",
                    "apa adanya, bukan huruf tebal. Itu yang melindungi halamanmu",
                    "dari XSS. Filter |safe mematikan perlindungan itu, jadi pakai",
                    "cuma untuk HTML yang kamu tulis sendiri.",
                ],
            },
            {
                "heading": "Menguji tanpa membuka port",
                "code": """from app import app

klien = app.test_client()

r = klien.get("/api/buku?tahun=2005")
print(r.status_code, r.get_json())

r = klien.post("/api/buku", json={"judul": "  "})
print(r.status_code, r.get_json()["detail"])
...""",
            },
            {
                "body": [
                    "test_client membuat environ palsu lalu memanggil aplikasi WSGI",
                    "Flask secara langsung, persis teknik di bab 1. Saat dijalankan,",
                    "dua permintaan di atas menghasilkan 200 dengan satu buku dan",
                    "422 dengan pesan judul wajib diisi. Tes seperti ini biasanya",
                    "ditulis dengan pytest, yang dibahas di kurikulum Python.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Flask sering dipakai untuk API kecil, dasbor internal, dan",
                    "layanan yang membungkus model machine learning: skrip Python",
                    "yang sudah ada tinggal diberi beberapa route. Banyak tutorial",
                    "pengembangan web Python juga mulai dari Flask karena kodenya",
                    "pendek.",
                    "",
                    "Kasus kecil: pengelola perpustakaan sekolah punya daftar buku",
                    "di berkas CSV dan ingin halaman web sederhana untuk mencari",
                    "buku berdasarkan tahun, plus endpoint JSON untuk aplikasi",
                    "Android buatan temanmu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca CSV sekali saat aplikasi menyala pakai modul csv, dan",
                    "     simpan ke list of dict.",
                    "  2. Buat route /api/buku yang menyaring dengan",
                    "     request.args.get(\"tahun\", type=int) dan mengembalikan",
                    "     list itu. Flask otomatis mengubahnya jadi JSON.",
                    "  3. Buat route / yang memanggil render_template dengan daftar",
                    "     yang sama, dan template Jinja yang mewarisi dasar.html.",
                    "  4. Tulis dua tes dengan app.test_client(): satu untuk tahun",
                    "     yang ada, satu untuk tahun yang kosong. Jalankan dengan",
                    "     flask --app app run tanpa --debug saat dipasang di komputer",
                    "     perpustakaan.",
                ],
            },
        ],
    },
    {
        "title": "15. Flask dengan SQLAlchemy dan Blueprint",
        "sections": [
            {
                "body": [
                    "Satu berkas app.py cukup sampai kira-kira beberapa ratus baris.",
                    "Sesudah itu kamu butuh dua hal: cara memecah route ke beberapa",
                    "berkas, dan cara menyimpan data ke database sungguhan. Di Flask,",
                    "jawabannya blueprint dan SQLAlchemy.",
                    "",
                    "Blueprint adalah kumpulan route yang bisa didaftarkan ke",
                    "aplikasi dengan awalan alamat tertentu. Satu fitur, satu",
                    "blueprint: buku, anggota, peminjaman. Aplikasinya sendiri dibuat",
                    "di fungsi bernama create_app, pola yang disebut application",
                    "factory. Dengan factory, tes bisa membuat aplikasi dengan",
                    "konfigurasi berbeda, misalnya database di memori.",
                ],
            },
            {
                "heading": "Susunan folder",
                "bahasa": "teks",
                "code": """perpus/
  toko/
    __init__.py      create_app()
    model.py         db dan model SQLAlchemy
    buku.py          blueprint /api/buku
    anggota.py       blueprint /api/anggota
    templates/
  migrations/        dibuat Flask-Migrate (Alembic)
  tests/
  pyproject.toml""",
            },
            {
                "heading": "SQLAlchemy 2.x: gaya baru",
                "body": [
                    "SQLAlchemy adalah toolkit SQL dan ORM terpenting di Python.",
                    "Ia punya dua lapisan: Core, untuk menulis SQL sebagai ekspresi",
                    "Python, dan ORM, untuk memetakan kelas ke tabel. Versi",
                    "terbarunya saat materi ini ditulis adalah 2.1.5.",
                    "",
                    "Sejak 2.0, cara menulisnya berubah. Model memakai anotasi",
                    "Mapped[...] dan mapped_column, dan kueri ditulis dengan",
                    "select(). Gaya lama seperti Buku.query.filter_by(...) masih",
                    "jalan lewat Flask-SQLAlchemy, tapi sudah dianggap warisan. Kalau",
                    "kamu menemukan tutorial yang memakai db.Column tanpa Mapped,",
                    "itu gaya 1.x.",
                    "",
                    "Di Flask, SQLAlchemy biasanya dipasang lewat ekstensi",
                    "Flask-SQLAlchemy (saat ini 3.1.1), yang mengurus sesi per",
                    "permintaan dan konfigurasi koneksinya.",
                ],
            },
            {
                "heading": "toko/model.py",
                "code": """from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Penulis(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nama: Mapped[str] = mapped_column(String(100), unique=True)
    buku: Mapped[list["Buku"]] = relationship(back_populates="penulis")


class Buku(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    judul: Mapped[str] = mapped_column(String(200))
    tahun: Mapped[int]
    penulis_id: Mapped[int] = mapped_column(ForeignKey("penulis.id"))
    penulis: Mapped[Penulis] = relationship(back_populates="buku")""",
            },
            {
                "body": [
                    "Tipe di Mapped menentukan kolomnya. Mapped[int] jadi kolom",
                    "bilangan bulat yang wajib diisi, Mapped[str | None] jadi kolom",
                    "yang boleh kosong. relationship menghubungkan dua kelas, jadi",
                    "kamu bisa menulis buku.penulis.nama dan penulis.buku tanpa",
                    "menulis JOIN sendiri.",
                ],
            },
            {
                "heading": "toko/buku.py dan toko/__init__.py",
                "code": """from flask import Blueprint, Flask, request

from .model import Buku, db

bp = Blueprint("buku", __name__, url_prefix="/api/buku")


def jadi_dict(b):
    return {"id": b.id, "judul": b.judul, "tahun": b.tahun,
            "penulis": b.penulis.nama}


@bp.get("/")
def daftar():
    kueri = db.select(Buku).order_by(Buku.judul)
    tahun = request.args.get("tahun", type=int)
    if tahun is not None:
        kueri = kueri.where(Buku.tahun == tahun)
    return [jadi_dict(b) for b in db.session.scalars(kueri)]


@bp.get("/<int:id_buku>")
def satu(id_buku):
    return jadi_dict(db.get_or_404(Buku, id_buku))


# toko/__init__.py
def create_app(konfig=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///toko.db"
    app.config.update(konfig or {})
    db.init_app(app)
    app.register_blueprint(bp)
    return app""",
            },
            {
                "body": [
                    "Kode ini sudah dijalankan dengan Flask 3.1.3, Flask-SQLAlchemy",
                    "3.1.1, dan SQLAlchemy 2.1.5, memakai database SQLite di memori",
                    "(sqlite://) untuk tes. Beberapa hal yang kelihatan saat diuji:",
                    "  - GET /api/buku/?tahun=2007 cuma mengambil buku tahun itu,",
                    "    karena saringan diteruskan ke SQL lewat where.",
                    "  - db.get_or_404 membalas 404 untuk id yang nggak ada, tanpa",
                    "    kamu menulis if.",
                    "  - GET /api/buku tanpa garis miring di akhir dibalas 308",
                    "    (redirect permanen) ke /api/buku/. Flask melakukannya karena",
                    "    rute didaftarkan dengan garis miring. Sebagian klien API",
                    "    nggak mengikuti redirect untuk POST, jadi tentukan satu",
                    "    bentuk dan pakai konsisten.",
                    "",
                    "Jebakan: jadi_dict membaca b.penulis.nama untuk tiap buku.",
                    "Secara bawaan, relasi itu dimuat saat pertama dibaca, jadi 100",
                    "buku berarti 100 kueri tambahan ke tabel penulis. Masalah ini",
                    "disebut N+1. Perbaikannya, minta SQLAlchemy memuat relasinya",
                    "sekaligus dengan",
                    ".options(selectinload(Buku.penulis)) di kuerinya. N+1 dan cara",
                    "mendeteksinya dibahas mendalam di kurikulum Database.",
                ],
            },
            {
                "heading": "Migrasi dengan Alembic",
                "body": [
                    "Tabel di database berubah seiring aplikasi tumbuh: kolom",
                    "baru, indeks baru, tabel baru. Mengubahnya dengan tangan di",
                    "tiap server rawan lupa. Alembic adalah alat migrasi untuk",
                    "SQLAlchemy. Tiap perubahan skema disimpan sebagai berkas revisi",
                    "bernomor yang punya fungsi upgrade dan downgrade, jadi database",
                    "di laptop, server uji, dan produksi bisa dibawa ke versi yang",
                    "sama. Versinya saat ini 1.20.0.",
                    "",
                    "Di Flask, Alembic biasanya dipakai lewat ekstensi Flask-Migrate",
                    "yang menambahkan perintah flask db:",
                ],
            },
            {
                "heading": "Perintah migrasi",
                "bahasa": "terminal",
                "code": """pip install flask-sqlalchemy flask-migrate
flask --app toko db init                          # sekali saja
flask --app toko db migrate -m "tambah tabel buku"  # buat revisi
flask --app toko db upgrade                       # terapkan ke database""",
            },
            {
                "body": [
                    "Perintah migrate membandingkan model dengan isi database lalu",
                    "menulis berkas revisi otomatis. Selalu baca berkas itu sebelum",
                    "menjalankan upgrade. Alembic nggak bisa membedakan kolom yang",
                    "diganti nama dengan kolom yang dihapus lalu dibuat baru, dan",
                    "salah tebak di sini berarti isi kolomnya hilang. Konsep migrasi",
                    "ini sama di Django, Laravel, Rails, dan Flyway, dan dibahas",
                    "lengkap di kurikulum Database.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Flask yang dirawat lama hampir selalu memakai susunan",
                    "ini: create_app, blueprint per fitur, Flask-SQLAlchemy, dan",
                    "Flask-Migrate. Kalau kamu mewarisi proyek Flask di tempat PKL,",
                    "cari dulu create_app dan register_blueprint untuk memetakan",
                    "fiturnya.",
                    "",
                    "Kasus kecil: halaman daftar buku perpustakaan makin lambat.",
                    "Isinya 300 buku, dan log database menunjukkan 301 kueri tiap",
                    "kali halaman dibuka.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali polanya: satu kueri untuk daftar buku, lalu satu",
                    "     kueri penulis untuk tiap buku. Itu N+1 dari b.penulis.",
                    "  2. Muat relasinya sekaligus:",
                    "       from sqlalchemy.orm import selectinload",
                    "       kueri = db.select(Buku).options(selectinload(Buku.penulis))",
                    "  3. Pasang SQLALCHEMY_ECHO = True sebentar di konfigurasi",
                    "     untuk melihat SQL yang dikirim. Sekarang cuma ada dua",
                    "     kueri: daftar buku dan penulis yang terlibat.",
                    "  4. Tambahkan paginasi dengan db.paginate(kueri, page=...,",
                    "     per_page=20) supaya halamannya tetap cepat saat bukunya",
                    "     ribuan.",
                ],
            },
        ],
    },
    {
        "title": "16. FastAPI: Type Hints Jadi Validasi dan Dokumen",
        "sections": [
            {
                "body": [
                    "Di Flask, validasi body kamu tulis sendiri: cek field ada,",
                    "cek tipenya, susun pesan error. FastAPI mengambil jalan lain.",
                    "Kamu menulis type hints, yaitu anotasi tipe Python yang sudah",
                    "kamu kenal di kurikulum Python. FastAPI memakai anotasi itu",
                    "untuk tiga hal sekaligus: membaca dan mengubah tipe data yang",
                    "masuk, menolak data yang salah dengan 422, dan membangkitkan",
                    "dokumentasi OpenAPI.",
                    "",
                    "FastAPI framework Python yang tumbuh paling cepat. Survei Stack",
                    "Overflow 2026 mencatat 18,5% responden memakainya, tertinggi di",
                    "antara framework Python, dan survei State of Python 2025",
                    "mencatat 38% pengembang Python, naik dari 29% setahun",
                    "sebelumnya. Versi terbarunya saat materi ini ditulis adalah",
                    "0.146.0. Nomornya memang masih 0.x walaupun sudah dipakai luas",
                    "di produksi, jadi kunci versinya di requirements supaya",
                    "pembaruan nggak mengejutkan.",
                ],
            },
            {
                "heading": "Memasang dan menjalankan",
                "bahasa": "terminal",
                "code": """pip install "fastapi[standard]"
fastapi dev main.py     # mode pengembangan, menyala ulang otomatis
# buka http://127.0.0.1:8000/docs""",
            },
            {
                "heading": "main.py",
                "code": """from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API Toko Buku", version="1.0.0")


class BukuBaru(BaseModel):
    judul: str = Field(min_length=1, max_length=200)
    tahun: int = Field(ge=1900, le=2100)
    tag: list[str] = []


class Buku(BukuBaru):
    id: int


BUKU: dict[int, Buku] = {
    1: Buku(id=1, judul="Laskar Pelangi", tahun=2005, tag=["novel"]),
}


@app.get("/buku")
def daftar_buku(tahun: int | None = None, batas: int = 10) -> list[Buku]:
    hasil = [b for b in BUKU.values() if tahun is None or b.tahun == tahun]
    return hasil[:batas]


@app.get("/buku/{id_buku}")
def satu_buku(id_buku: int) -> Buku:
    if id_buku not in BUKU:
        raise HTTPException(status_code=404, detail="Buku nggak ada")
    return BUKU[id_buku]


@app.post("/buku", status_code=201)
def tambah_buku(data: BukuBaru) -> Buku:
    buku = Buku(id=max(BUKU) + 1, **data.model_dump())
    BUKU[buku.id] = buku
    return buku""",
            },
            {
                "body": [
                    "FastAPI menebak asal tiap parameter dari bentuknya:",
                    "  - Nama yang muncul di alamat, seperti {id_buku}, adalah",
                    "    parameter path.",
                    "  - Parameter bertipe sederhana lain, seperti tahun dan batas,",
                    "    diambil dari query string. Yang punya nilai bawaan boleh",
                    "    nggak dikirim.",
                    "  - Parameter bertipe model Pydantic, seperti data: BukuBaru,",
                    "    diambil dari body JSON.",
                    "",
                    "Anotasi kembalian -> Buku juga dipakai. FastAPI menyaring",
                    "respons supaya cuma berisi field model itu, dan mencatat",
                    "bentuknya di dokumentasi. Ini mencegah field rahasia seperti",
                    "hash kata sandi ikut terkirim tanpa sengaja.",
                ],
            },
            {
                "heading": "Pydantic: model yang memvalidasi dirinya sendiri",
                "body": [
                    "BukuBaru adalah model Pydantic, pustaka validasi data berbasis",
                    "type hints. Versi terbarunya saat ini 2.14.1. Field(...)",
                    "menambahkan aturan: min_length dan max_length untuk teks, ge",
                    "(greater or equal) dan le (less or equal) untuk angka.",
                    "",
                    "Contoh di atas sudah dijalankan dengan FastAPI 0.146.0 dan",
                    "Pydantic 2.14.1 lewat TestClient. Ini yang terjadi:",
                    "  - POST /buku dengan {\"judul\": \"Bumi Manusia\", \"tahun\":",
                    "    \"1980\"} diterima dengan 201. Teks \"1980\" diubah jadi",
                    "    angka 1980, karena Pydantic secara bawaan bersikap longgar",
                    "    untuk teks yang jelas berisi angka.",
                    "  - GET /buku/abc dibalas 422, karena abc bukan int.",
                    "  - POST /buku dengan judul kosong dan tahun 1800 dibalas 422",
                    "    berisi dua error sekaligus.",
                    "",
                    "Bentuk error 422 dari FastAPI begini (dipotong):",
                ],
            },
            {
                "heading": "Respons 422 bawaan FastAPI",
                "bahasa": "json",
                "code": """{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "judul"],
      "msg": "String should have at least 1 character",
      "input": "",
      "ctx": {"min_length": 1}
    },
    {
      "type": "greater_than_equal",
      "loc": ["body", "tahun"],
      "msg": "Input should be greater than or equal to 1900",
      "input": 1800,
      "ctx": {"ge": 1900}
    }
  ]
}""",
            },
            {
                "body": [
                    "loc menyebut letak kesalahannya: di body, field judul. Bentuk",
                    "ini bukan Problem Details RFC 9457. Kalau API-mu sudah memakai",
                    "Problem Details, pasang penangan exception untuk",
                    "RequestValidationError dan susun ulang bentuknya di sana.",
                    "",
                    "Jebakan: banyak tutorial masih memakai Pydantic v1. Di v2,",
                    "beberapa nama berganti. .dict() jadi .model_dump(), .json()",
                    "jadi .model_dump_json(), decorator @validator jadi",
                    "@field_validator, dan class Config di dalam model jadi",
                    "model_config = ConfigDict(...). Inti v2 ditulis ulang dalam Rust",
                    "(pydantic-core), jadi jauh lebih cepat dari v1. Kode v1 yang",
                    "disalin mentah biasanya memunculkan peringatan usang atau error.",
                ],
            },
            {
                "heading": "Dokumentasi yang jadi sendiri",
                "body": [
                    "Buka /docs dan kamu dapat Swagger UI yang berisi semua endpoint,",
                    "lengkap dengan skema BukuBaru dan tombol untuk mencobanya. /redoc",
                    "menampilkan dokumen yang sama dengan gaya Redoc, dan",
                    "/openapi.json berisi dokumen OpenAPI mentahnya. Saat diuji,",
                    "dokumen itu bertanda openapi 3.1.0. Semua ini dibangkitkan dari",
                    "type hints yang sama dengan yang dipakai untuk validasi, jadi",
                    "dokumentasinya nggak bisa tertinggal dari kode.",
                    "",
                    "Di bawahnya, FastAPI berdiri di atas Starlette, toolkit ASGI",
                    "ringan yang sudah melewati versi 1.0 (saat ini 1.9.0). Routing,",
                    "middleware, WebSocket, dan respons streaming itu milik",
                    "Starlette; FastAPI menambahkan lapisan type hints, Pydantic, dan",
                    "dependency injection. Karena itu aplikasi FastAPI adalah",
                    "aplikasi ASGI, kontrak yang kamu pelajari di bab 1.",
                    "",
                    "Untuk tes, from fastapi.testclient import TestClient lalu",
                    "TestClient(app).get(\"/buku\"). TestClient butuh paket httpx;",
                    "Starlette versi terbaru mulai menyarankan httpx2 sebagai",
                    "penggantinya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "FastAPI banyak dipakai untuk menyajikan model machine learning",
                    "dan layanan AI sebagai API, karena ekosistem AI memang berbahasa",
                    "Python dan FastAPI bisa melayani respons streaming. Dokumentasi",
                    "otomatis di /docs juga membuat tim frontend bisa langsung",
                    "mencoba endpoint tanpa menunggu dokumentasi ditulis.",
                    "",
                    "Kasus kecil: endpoint pendaftaran FastAPI menerima umur",
                    "negatif dan email tanpa @, dan responsnya ikut mengirim field",
                    "kata_sandi_hash ke klien.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan model masuk dan model keluar. Model masuk berisi",
                    "     aturan validasi:",
                    "       class DaftarMasuk(BaseModel):",
                    "           email: EmailStr",
                    "           umur: int = Field(ge=13)",
                    "           kata_sandi: str = Field(min_length=8)",
                    "  2. EmailStr butuh paket tambahan email-validator, jadi pasang",
                    "     dengan pip install \"pydantic[email]\".",
                    "  3. Buat model keluar tanpa field rahasia, misalnya",
                    "     class Pengguna(BaseModel) berisi id, email, dan umur, lalu",
                    "     tulis -> Pengguna sebagai anotasi kembalian endpoint.",
                    "  4. Cek /docs. Skema masuk dan keluar sekarang terlihat",
                    "     berbeda, dan kata_sandi_hash nggak pernah muncul di",
                    "     respons.",
                ],
            },
        ],
    },
    {
        "title": "17. FastAPI Async, Dependency, dan SQLModel",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya menulis endpoint dengan def biasa. FastAPI",
                    "juga menerima async def. Keduanya sah, dan memilih yang salah",
                    "bisa membuat server terasa macet. Materi ini membahas pilihan",
                    "itu, lalu dua alat yang dipakai hampir di semua aplikasi FastAPI:",
                    "dependency dan database lewat SQLModel.",
                ],
            },
            {
                "heading": "def atau async def",
                "body": [
                    "FastAPI berjalan di atas event loop asyncio, mirip juru masak",
                    "tunggal di materi Node.js bab 3. Aturannya:",
                    "  - Endpoint async def dijalankan langsung di event loop. Di",
                    "    dalamnya, semua yang menunggu wajib memakai await dengan",
                    "    pustaka async, misalnya httpx.AsyncClient atau driver",
                    "    database async.",
                    "  - Endpoint def biasa dijalankan FastAPI di thread terpisah",
                    "    (threadpool), jadi boleh memakai pustaka yang memblokir",
                    "    seperti requests atau driver database biasa.",
                    "",
                    "Masalah muncul kalau kamu menulis async def lalu memanggil",
                    "fungsi yang memblokir di dalamnya. Contoh ini memperlihatkan",
                    "bedanya dengan asyncio polos:",
                ],
            },
            {
                "heading": "await versus fungsi yang memblokir",
                "code": """import asyncio
import time


async def tugas_async(nama):
    print(nama, "mulai")
    await asyncio.sleep(0.05)     # menunggu sambil memberi giliran ke yang lain
    print(nama, "selesai")


async def tugas_blocking(nama):
    print(nama, "mulai")
    time.sleep(0.05)              # menahan seluruh event loop
    print(nama, "selesai")


async def main():
    print("-- await asyncio.sleep --")
    await asyncio.gather(tugas_async("A"), tugas_async("B"))
    print("-- time.sleep di dalam async def --")
    await asyncio.gather(tugas_blocking("C"), tugas_blocking("D"))


asyncio.run(main())""",
            },
            {
                "body": [
                    "Keluaran:",
                    "-- await asyncio.sleep --",
                    "A mulai",
                    "B mulai",
                    "A selesai",
                    "B selesai",
                    "-- time.sleep di dalam async def --",
                    "C mulai",
                    "C selesai",
                    "D mulai",
                    "D selesai",
                    "",
                    "A dan B berjalan bergantian, karena await memberi giliran ke",
                    "tugas lain selama menunggu. C menahan event loop sampai",
                    "selesai, jadi D baru mulai sesudahnya. Di server FastAPI, \"D\"",
                    "itu adalah semua pengguna lain yang sedang menunggu jawaban.",
                    "",
                    "Pegangan praktisnya: kalau pustaka yang kamu pakai nggak punya",
                    "versi async, tulis endpoint-nya dengan def biasa. Kalau",
                    "terpaksa memanggil fungsi yang memblokir dari async def,",
                    "bungkus dengan run_in_threadpool dari Starlette atau",
                    "asyncio.to_thread.",
                ],
            },
            {
                "heading": "Dependency: Depends",
                "body": [
                    "Banyak endpoint butuh hal yang sama: sesi database, pengguna",
                    "yang sedang login, atau parameter paginasi. FastAPI",
                    "menyediakannya lewat dependency, yaitu fungsi biasa yang",
                    "hasilnya disuntikkan ke parameter endpoint dengan Depends.",
                    "Ini dependency injection yang kamu kenal dari NestJS di bab 3,",
                    "dalam bentuk fungsi.",
                    "",
                    "Dependency boleh punya parameter sendiri (query, header, atau",
                    "dependency lain), dan FastAPI menyusun semuanya. Dependency",
                    "yang memakai yield menjalankan kode sesudah yield setelah",
                    "respons selesai. Pola ini dipakai untuk membuka dan menutup",
                    "sesi database. Annotated dipakai supaya deklarasinya cukup",
                    "ditulis sekali lalu dipakai di banyak endpoint.",
                ],
            },
            {
                "heading": "SQLModel: satu kelas untuk Pydantic dan tabel",
                "body": [
                    "SQLModel adalah pustaka dari pembuat FastAPI yang menggabungkan",
                    "model Pydantic dan model SQLAlchemy dalam satu kelas. Kelas",
                    "dengan table=True jadi tabel; kelas tanpa itu jadi model",
                    "Pydantic biasa. Versinya masih 0.0.48, jadi API-nya masih bisa",
                    "berubah. Tutorial resminya ramah pemula dan menjelaskan SQL dari",
                    "nol.",
                    "",
                    "Contoh berikut menggabungkan semuanya. Kodenya sudah dijalankan",
                    "dengan FastAPI 0.146.0 dan SQLModel 0.0.48:",
                ],
            },
            {
                "heading": "main.py",
                "code": """from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///toko.db")


class BukuBaru(SQLModel):                    # bentuk data masuk, divalidasi
    judul: str = Field(min_length=1, max_length=200)
    tahun: int = Field(ge=1900, le=2100)


class Buku(BukuBaru, table=True):            # tabel di database
    id: int | None = Field(default=None, primary_key=True)


def ambil_sesi():
    with Session(engine) as sesi:
        yield sesi                           # dipakai endpoint, lalu ditutup


def halaman(page: int = Query(1, ge=1), per_page: int = Query(10, ge=1, le=50)):
    return {"offset": (page - 1) * per_page, "limit": per_page}


def wajib_token(authorization: str | None = Header(default=None)):
    if authorization != "Bearer rahasia":
        raise HTTPException(status_code=401, detail="Token salah")


Sesi = Annotated[Session, Depends(ambil_sesi)]
Halaman = Annotated[dict, Depends(halaman)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)     # saat aplikasi menyala
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/buku")
def daftar_buku(sesi: Sesi, hal: Halaman) -> list[Buku]:
    kueri = select(Buku).order_by(Buku.judul).offset(hal["offset"]).limit(hal["limit"])
    return sesi.exec(kueri).all()


@app.post("/buku", status_code=201, dependencies=[Depends(wajib_token)])
def tambah_buku(data: BukuBaru, sesi: Sesi) -> Buku:
    buku = Buku.model_validate(data)
    sesi.add(buku)
    sesi.commit()
    sesi.refresh(buku)
    return buku""",
            },
            {
                "body": [
                    "Yang terlihat saat diuji:",
                    "  - POST /buku tanpa header Authorization dibalas 401 oleh",
                    "    wajib_token, sebelum fungsi tambah_buku dipanggil.",
                    "  - GET /buku?page=0 dibalas 422, karena aturan ge=1 di",
                    "    dependency halaman ikut diperiksa.",
                    "  - Endpoint ditulis dengan def biasa, karena Session SQLModel",
                    "    memakai driver yang memblokir. Mereka jalan di threadpool.",
                    "",
                    "Ada tiga jebakan yang sempat muncul saat contoh ini disusun:",
                    "  1. Kelas dengan table=True nggak menjalankan validasi Field",
                    "     saat dibuat. Versi pertama contoh ini menerima judul",
                    "     kosong. Karena itu body diterima sebagai BukuBaru (tanpa",
                    "     table=True), lalu diubah dengan Buku.model_validate.",
                    "  2. Header wajib yang nggak dikirim membuat FastAPI membalas",
                    "     422, bukan 401. Supaya klien tanpa token mendapat 401,",
                    "     header-nya dibuat opsional lalu dicek sendiri.",
                    "  3. @app.on_event(\"startup\") sudah usang. Kode yang harus",
                    "     jalan saat aplikasi menyala ditaruh di fungsi lifespan.",
                ],
            },
            {
                "heading": "Menjalankan di server: Uvicorn",
                "body": [
                    "Aplikasi ASGI butuh server ASGI. FastAPI memakai Uvicorn,",
                    "server ASGI yang cepat (saat ini 0.54.0, juga masih 0.x).",
                    "Perintah fastapi dev dan fastapi run di baliknya menjalankan",
                    "Uvicorn untukmu. Pilihan lainnya Hypercorn dan Granian.",
                    "",
                    "Satu proses Uvicorn memakai satu inti CPU. Untuk memakai semua",
                    "inti, jalankan beberapa proses pekerja (worker). Dulu caranya",
                    "Gunicorn sebagai pengelola proses dengan kelas worker Uvicorn;",
                    "sekarang Uvicorn bisa mengelola worker sendiri. Konfigurasi",
                    "lengkapnya di belakang Nginx dibahas di bab 15 dan kurikulum",
                    "DevOps.",
                ],
            },
            {
                "heading": "Menjalankan untuk produksi",
                "bahasa": "terminal",
                "code": """fastapi run main.py --workers 4
# atau langsung dengan Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola Depends untuk sesi database dan pengguna yang login",
                    "muncul di hampir semua proyek FastAPI. Templat proyek resmi",
                    "\"Full Stack FastAPI Template\" dari pembuat FastAPI memakai",
                    "SQLModel, dependency sesi dengan yield, dan dependency untuk",
                    "pengguna yang sedang login, persis bentuk di materi ini.",
                    "",
                    "Kasus kecil: API rekomendasi buku memanggil layanan lain lewat",
                    "requests.get di dalam endpoint async def. Saat ada 20 pengguna",
                    "bersamaan, waktu respons naik dari 200 milidetik jadi beberapa",
                    "detik, padahal CPU server santai.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali gejalanya: CPU rendah tapi semua permintaan antre.",
                    "     Itu tanda event loop tertahan fungsi yang memblokir.",
                    "  2. Pilihan tercepat: ganti async def jadi def. FastAPI akan",
                    "     menjalankannya di threadpool.",
                    "  3. Pilihan yang lebih hemat: tetap async def, tapi ganti",
                    "     requests dengan klien async:",
                    "       async with httpx.AsyncClient() as klien:",
                    "           r = await klien.get(url, timeout=5)",
                    "  4. Uji lagi dengan 20 permintaan bersamaan. Waktu respons",
                    "     kembali mendekati waktu layanan yang dipanggil.",
                ],
            },
        ],
    },
    {
        "title": "18. Django: Model, View, Template, dan Admin",
        "sections": [
            {
                "body": [
                    "Di bab sebelumnya kamu sudah kenal Flask dan FastAPI. Keduanya kecil:",
                    "yang dikasih cuma router dan cara membalas permintaan. Database, login,",
                    "form, dan halaman admin kamu rakit sendiri dari paket lain.",
                    "",
                    "Django mengambil jalan sebaliknya. Ia framework web Python yang datang",
                    "dengan baterai lengkap, istilah aslinya batteries included. Isinya ORM",
                    "untuk database, sistem migrasi, autentikasi, form, template, dan halaman",
                    "admin yang jadi sendiri dari model datamu. Django lahir di redaksi",
                    "sebuah koran di Amerika dan dirilis terbuka tahun 2005, jadi kebutuhan",
                    "awalnya memang aplikasi yang isinya banyak dan harus cepat dikelola",
                    "orang non-programmer.",
                    "",
                    "Prasyaratnya kurikulum Python (class, decorator, modul) dan kurikulum",
                    "SQL. Kamu nggak perlu hafal SQL-nya, tapi paham tabel, baris, dan relasi",
                    "bikin ORM Django jauh lebih masuk akal.",
                ],
            },
            {
                "heading": "Bikin proyek dan app",
                "bahasa": "terminal",
                "code": """python3 -m venv .venv
source .venv/bin/activate
pip install django
django-admin startproject toko .
python manage.py startapp gudang
python manage.py runserver""",
            },
            {
                "body": [
                    "Django membedakan dua hal yang sering bikin bingung di awal. Proyek",
                    "(project) itu satu situs utuh beserta pengaturannya. App itu satu bagian",
                    "fitur di dalamnya, misalnya daftar produk, keranjang, atau blog. Satu",
                    "proyek biasanya berisi beberapa app, dan satu app bisa dipindah ke",
                    "proyek lain.",
                    "",
                    "Perintah startproject membuat folder toko berisi settings.py (semua",
                    "pengaturan), urls.py (peta alamat paling atas), serta asgi.py dan",
                    "wsgi.py, dua pintu masuk untuk server aplikasi. Ingat kontrak aplikasi",
                    "sebagai fungsi di bab 01: berkas itulah yang nanti dipanggil Gunicorn",
                    "atau Uvicorn. Database bawaannya SQLite, berkas db.sqlite3 di folder",
                    "proyek, jadi kamu bisa langsung mulai tanpa memasang server database.",
                    "",
                    "App baru belum dikenal Django sampai kamu mendaftarkannya di",
                    "settings.py:",
                    "",
                    "  INSTALLED_APPS = [",
                    "      \"django.contrib.admin\",",
                    "      \"django.contrib.auth\",",
                    "      ...",
                    "      \"gudang\",",
                    "  ]",
                    "",
                    "Jebakan: lupa langkah ini membuat model app itu nggak pernah punya",
                    "tabel. Pesan galatnya menyebut model yang nggak ada di INSTALLED_APPS,",
                    "jadi cek di situ dulu.",
                ],
            },
            {
                "heading": "Model: tabel yang ditulis sebagai class",
                "code": """from django.db import models


class Kategori(models.Model):
    nama = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nama


class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)
    kategori = models.ForeignKey(
        Kategori, on_delete=models.PROTECT, related_name="produk"
    )
    dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nama"]

    def __str__(self):
        return self.nama""",
            },
            {
                "body": [
                    "Satu class model sama dengan satu tabel, satu atribut sama dengan satu",
                    "kolom. Kolom id dibuat otomatis. ForeignKey membuat relasi banyak ke",
                    "satu: banyak produk masuk satu kategori. on_delete=models.PROTECT",
                    "menolak penghapusan kategori yang masih punya produk, dan related_name",
                    "membuat kamu bisa menulis kategori.produk.all() dari sisi sebaliknya.",
                    "",
                    "Tabelnya belum ada sampai kamu membuat dan menjalankan migrasi:",
                    "",
                    "  python manage.py makemigrations gudang",
                    "  python manage.py migrate",
                    "",
                    "makemigrations membandingkan model dengan migrasi yang sudah ada lalu",
                    "menulis berkas baru di gudang/migrations. migrate menjalankan",
                    "berkas-berkas itu ke database. Berkas migrasi ikut di-commit ke Git,",
                    "karena dari situlah database rekan setimmu dibangun dengan bentuk yang",
                    "sama.",
                ],
            },
            {
                "heading": "QuerySet yang malas",
                "body": [
                    "Django ORM memakai pola Active Record: objek modelnya sendiri yang tahu",
                    "cara menyimpan diri (produk.save()). Untuk membaca data kamu memakai",
                    "QuerySet:",
                    "",
                    "  murah = Produk.objects.filter(harga__lte=10000).exclude(stok=0)",
                    "  murah = murah.order_by(\"-harga\")[:5]",
                    "",
                    "Dua baris itu belum menyentuh database sama sekali. QuerySet itu malas",
                    "(lazy): ia cuma mencatat syarat. SQL baru dikirim saat datanya diminta,",
                    "misalnya diulang dengan for, diubah jadi list, atau dihitung len-nya.",
                    "Akhiran seperti __lte, __gte, dan __contains disebut lookup, dan [:5]",
                    "diterjemahkan jadi LIMIT 5.",
                    "",
                    "Malas itu menguntungkan, tapi ada jebakannya. Kalau kamu mengulang",
                    "produk lalu membaca p.kategori.nama, Django mengambil kategori satu per",
                    "satu: satu kueri untuk daftar produk, lalu satu kueri lagi untuk tiap",
                    "produk. Ini yang disebut masalah N+1. Saat diuji dengan tujuh produk,",
                    "perulangan polos mengirim 8 kueri. Dengan select_related(\"kategori\")",
                    "Django memakai JOIN dan cukup 1 kueri. Untuk relasi banyak ke banyak",
                    "pasangannya prefetch_related. Pembahasan N+1 yang lebih dalam ada di",
                    "kurikulum Database.",
                ],
            },
            {
                "heading": "View dan URLconf",
                "code": """from django.shortcuts import get_object_or_404, render

from .models import Produk


def daftar_produk(request):
    semua = Produk.objects.select_related("kategori").filter(stok__gt=0)
    return render(request, "gudang/daftar.html", {"produk": semua})


def detail_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    return render(request, "gudang/detail.html", {"produk": produk})""",
            },
            {
                "body": [
                    "View di Django adalah fungsi yang menerima objek request dan",
                    "mengembalikan respons. Bentuknya persis kontrak \"aplikasi sebagai",
                    "fungsi\" dari bab 01, cuma lebih nyaman. render mengisi template dengan",
                    "data, get_object_or_404 membalas 404 kalau barisnya nggak ada.",
                    "",
                    "Alamat dipetakan di URLconf. Buat gudang/urls.py:",
                    "",
                    "  from django.urls import path",
                    "",
                    "  from . import views",
                    "",
                    "  app_name = \"gudang\"",
                    "  urlpatterns = [",
                    "      path(\"\", views.daftar_produk, name=\"daftar\"),",
                    "      path(\"<int:pk>/\", views.detail_produk, name=\"detail\"),",
                    "  ]",
                    "",
                    "lalu sambungkan ke toko/urls.py dengan path(\"produk/\",",
                    "include(\"gudang.urls\")). Sekarang /produk/ memanggil daftar_produk dan",
                    "/produk/1/ memanggil detail_produk dengan pk=1. <int:pk> disebut path",
                    "converter: ia menolak /produk/abc/ sebelum view-mu dipanggil.",
                    "",
                    "Django menyebut susunannya MVT: Model (data), View (logika), Template",
                    "(tampilan). Kalau kamu pernah dengar MVC, view Django mengerjakan tugas",
                    "controller, dan template mengerjakan tugas view.",
                ],
            },
            {
                "heading": "Template",
                "bahasa": "html",
                "code": """<h1>Produk</h1>
<ul>
  {% for p in produk %}
    <li>
      <a href="{% url 'gudang:detail' p.pk %}">{{ p.nama }}</a>
      ({{ p.kategori.nama }}) Rp{{ p.harga }}
    </li>
  {% empty %}
    <li>Belum ada produk.</li>
  {% endfor %}
</ul>""",
            },
            {
                "body": [
                    "Simpan di gudang/templates/gudang/daftar.html. Bahasa template Django",
                    "mirip Jinja yang kamu pakai di Flask: {{ ... }} mencetak nilai, {% ...",
                    "%} menjalankan perintah seperti for dan url. Nilai yang dicetak otomatis",
                    "di-escape, jadi nama produk berisi <script> tampil sebagai teks biasa,",
                    "nggak dijalankan browser.",
                ],
            },
            {
                "heading": "Admin yang jadi sendiri",
                "code": """from django.contrib import admin

from .models import Kategori, Produk


@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ["nama", "kategori", "harga", "stok"]
    list_filter = ["kategori"]
    search_fields = ["nama"]


admin.site.register(Kategori)""",
            },
            {
                "body": [
                    "Simpan di gudang/admin.py, buat akun dengan python manage.py",
                    "createsuperuser, lalu buka /admin/. Kamu langsung dapat halaman untuk",
                    "menambah, mengubah, mencari, dan menyaring produk, lengkap dengan login",
                    "dan izin per pengguna. Fitur ini yang paling sering jadi alasan orang",
                    "memilih Django: tim konten atau admin toko bisa bekerja di hari pertama,",
                    "sebelum frontend-nya selesai.",
                    "",
                    "Admin ini ditujukan untuk orang dalam. Untuk pembeli atau pengguna umum,",
                    "tetap bikin halaman atau API sendiri.",
                ],
            },
            {
                "heading": "Kapan memilih Django, dan versinya",
                "body": [
                    "Pilih Django kalau aplikasinya berpusat pada data yang dikelola manusia:",
                    "toko, sistem informasi sekolah, portal berita, aplikasi internal kantor.",
                    "Kalau yang kamu butuhkan cuma API kecil yang cepat, FastAPI atau Flask",
                    "lebih ringkas. Django juga mendukung view async, tapi sebagian besar",
                    "ekosistemnya masih ditulis sinkron.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), versi terbarunya 6.1.2. Django",
                    "merilis versi fitur kira-kira tiap delapan bulan. Versi 5.2 berstatus",
                    "LTS (dukungan jangka panjang) sampai April 2028, jadi itu pilihan aman",
                    "untuk proyek kantor yang jarang di-upgrade. Lisensinya BSD-3-Clause. Di",
                    "Survei Stack Overflow 2026, 11,3% responden memakai Django, dan survei",
                    "JetBrains bersama PSF tahun 2025 mencatat 35% pengembang Python",
                    "memakainya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Django banyak dipakai untuk portal berita, sistem informasi kampus,",
                    "aplikasi pendaftaran, dan dasbor internal, karena admin bawaannya",
                    "menghemat berminggu-minggu kerja membuat halaman pengelola data.",
                    "",
                    "Kasus kecil: kamu PKL di koperasi sekolah. Pengurus ingin mencatat",
                    "barang dan stok lewat browser minggu ini juga, sementara aplikasi",
                    "kasirnya baru dibuat bulan depan.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat proyek dan app inventaris, daftarkan app-nya di",
                    "     INSTALLED_APPS.",
                    "  2. Tulis model Barang (nama, harga, stok) dan Kategori, lalu jalankan",
                    "     makemigrations dan migrate.",
                    "  3. Daftarkan kedua model di admin.py dengan list_display dan",
                    "     search_fields supaya pengurus bisa mencari barang.",
                    "  4. Buat akun lewat createsuperuser untuk tiap pengurus, dan beri izin",
                    "     sesuai tugasnya di halaman admin.",
                    "  5. Nanti aplikasi kasir tinggal membaca tabel yang sama lewat API",
                    "     (materi berikutnya).",
                ],
            },
        ],
    },
    {
        "title": "19. API Django dengan DRF dan Django Ninja",
        "sections": [
            {
                "body": [
                    "View Django di materi sebelumnya membalas dengan halaman HTML. Aplikasi",
                    "Android, frontend React, atau sistem kasir butuh hal lain: data JSON.",
                    "Kamu bisa saja mengembalikan JsonResponse dari view biasa. Masalahnya,",
                    "lama-lama kamu menulis ulang hal yang sama di tiap endpoint: membaca",
                    "body, memvalidasi isinya, mengubah objek jadi JSON, memeriksa login,",
                    "membagi hasil per halaman.",
                    "",
                    "Dua pustaka mengurus pekerjaan itu di atas Django. Django REST Framework",
                    "(DRF) adalah yang paling tua dan paling banyak dipakai. Django Ninja",
                    "lebih baru dan gayanya mirip FastAPI. Keduanya memakai model dan ORM",
                    "yang sama dari materi sebelumnya.",
                ],
            },
            {
                "heading": "Serializer: penerjemah dua arah",
                "code": """from rest_framework import serializers

from .models import Kategori, Produk


class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.SlugRelatedField(
        slug_field="nama", queryset=Kategori.objects.all()
    )

    class Meta:
        model = Produk
        fields = ["id", "nama", "harga", "stok", "kategori"]

    def validate_harga(self, nilai):
        if nilai < 1000:
            raise serializers.ValidationError("Harga minimal Rp1.000.")
        return nilai""",
            },
            {
                "body": [
                    "Pasang dulu dengan pip install djangorestframework lalu tambahkan",
                    "\"rest_framework\" ke INSTALLED_APPS. Serializer bekerja dua arah. Ke",
                    "luar, ia mengubah objek Produk jadi dict yang siap dijadikan JSON. Ke",
                    "dalam, ia memeriksa JSON dari klien sebelum disimpan.",
                    "",
                    "ModelSerializer membaca tipe kolom dari model, jadi kamu nggak perlu",
                    "menulis ulang aturan dasar seperti \"harga harus bilangan bulat positif\".",
                    "Aturan bisnis tambahan ditulis di method validate_<nama_kolom>.",
                    "SlugRelatedField membuat kategori tampil sebagai namanya (\"Minuman\")",
                    "alih-alih angka id.",
                ],
            },
            {
                "heading": "ViewSet dan router",
                "code": """from rest_framework import permissions, viewsets

from .models import Produk
from .serializers import ProdukSerializer


class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.select_related("kategori")
    serializer_class = ProdukSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]""",
            },
            {
                "body": [
                    "Satu ModelViewSet berisi enam aksi CRUD sekaligus. Router yang",
                    "membuatkan alamatnya. Di toko/urls.py:",
                    "",
                    "  from rest_framework.routers import DefaultRouter",
                    "",
                    "  from gudang.api import ProdukViewSet",
                    "",
                    "  router = DefaultRouter()",
                    "  router.register(\"produk\", ProdukViewSet)",
                    "  urlpatterns = [path(\"api/\", include(router.urls))]",
                    "",
                    "Hasilnya:",
                    "",
                    "  GET     /api/produk/       list            200",
                    "  POST    /api/produk/       create          201",
                    "  GET     /api/produk/3/     retrieve        200 atau 404",
                    "  PUT     /api/produk/3/     update          200",
                    "  PATCH   /api/produk/3/     partial_update  200",
                    "  DELETE  /api/produk/3/     destroy         204",
                    "",
                    "Waktu contoh ini dicoba, POST tanpa login dibalas 403 karena",
                    "IsAuthenticatedOrReadOnly cuma mengizinkan baca untuk tamu. Sesudah",
                    "login, harga 500 dibalas 400 dengan body {\"harga\": [\"Harga minimal",
                    "Rp1.000.\"]}, dan data yang benar dibalas 201 berisi produk baru beserta",
                    "id-nya. Buka /api/produk/ di browser dan kamu dapat halaman API yang",
                    "bisa dijelajah (browsable API), lengkap dengan form untuk mencoba POST.",
                    "",
                    "Pengaturan yang berlaku untuk semua endpoint ditulis sekali di",
                    "settings.py, misalnya paginasi:",
                    "",
                    "  REST_FRAMEWORK = {",
                    "      \"DEFAULT_PAGINATION_CLASS\":",
                    "          \"rest_framework.pagination.PageNumberPagination\",",
                    "      \"PAGE_SIZE\": 20,",
                    "  }",
                ],
            },
            {
                "heading": "Django Ninja: type hints jadi validasi",
                "code": """from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from .models import Produk

api = NinjaAPI()


class ProdukOut(Schema):
    id: int
    nama: str
    harga: int


class ProdukIn(Schema):
    nama: str
    harga: int
    kategori_id: int


@api.get("/produk", response=list[ProdukOut])
def daftar(request):
    return Produk.objects.all()


@api.get("/produk/{produk_id}", response=ProdukOut)
def detail(request, produk_id: int):
    return get_object_or_404(Produk, id=produk_id)


@api.post("/produk", response={201: ProdukOut})
def tambah(request, data: ProdukIn):
    produk = Produk.objects.create(**data.model_dump())
    return 201, produk""",
            },
            {
                "body": [
                    "Kalau kamu sudah membaca materi FastAPI, bentuk ini terasa akrab. Schema",
                    "adalah model Pydantic. Tipe di parameter fungsi menentukan apa yang",
                    "divalidasi, dan response menentukan bentuk jawaban. Pasang dengan pip",
                    "install django-ninja, lalu sambungkan dengan path(\"api/\", api.urls).",
                    "Dokumentasi OpenAPI interaktif langsung tersedia di /api/docs.",
                    "",
                    "Saat diuji, POST tanpa harga dan kategori_id dibalas 422 dengan daftar",
                    "galat berbentuk {\"type\": \"missing\", \"loc\": [\"body\", \"data\", \"harga\"],",
                    "...}. Bentuknya sama dengan FastAPI, jadi frontend yang sudah terbiasa",
                    "dengan FastAPI nggak perlu menyesuaikan diri.",
                ],
            },
            {
                "heading": "Login, izin, dan pengujian",
                "body": [
                    "DRF memisahkan dua pertanyaan. Autentikasi menjawab \"siapa kamu\", izin",
                    "(permission) menjawab \"boleh atau tidak\". Untuk autentikasi ada",
                    "SessionAuthentication yang memakai cookie login Django (cocok kalau",
                    "frontend-nya satu domain), TokenAuthentication yang memberi tiap",
                    "pengguna satu token tetap, dan paket djangorestframework-simplejwt untuk",
                    "JWT. Cara kerja sesi, token, dan JWT dibahas di bab Autentikasi.",
                    "",
                    "Izin bawaan seperti IsAuthenticated dan IsAdminUser berlaku untuk",
                    "seluruh endpoint. Aturan per objek, misalnya \"cuma pemilik yang boleh",
                    "mengubah tokonya\", ditulis sebagai class sendiri:",
                    "",
                    "  from rest_framework import permissions",
                    "",
                    "",
                    "  class HanyaPemilik(permissions.BasePermission):",
                    "      def has_object_permission(self, request, view, obj):",
                    "          if request.method in permissions.SAFE_METHODS:",
                    "              return True",
                    "          return obj.pemilik == request.user",
                    "",
                    "SAFE_METHODS berisi GET, HEAD, dan OPTIONS, jadi siapa pun boleh",
                    "membaca, tapi cuma pemilik yang boleh mengubah atau menghapus. Lupa",
                    "pemeriksaan per objek seperti ini adalah celah API yang paling sering",
                    "ditemukan, dan namanya akan kamu temui lagi di bab Otorisasi.",
                    "",
                    "API juga gampang diuji tanpa membuka browser. APITestCase menyediakan",
                    "klien palsu yang memanggil aplikasi langsung, persis gagasan menguji",
                    "aplikasi tanpa membuka port di bab 01:",
                    "",
                    "  from rest_framework.test import APITestCase",
                    "",
                    "",
                    "  class ProdukApiTest(APITestCase):",
                    "      def test_tamu_tidak_boleh_menambah(self):",
                    "          r = self.client.post(\"/api/produk/\", {\"nama\": \"Air\"},",
                    "                               format=\"json\")",
                    "          self.assertEqual(r.status_code, 403)",
                    "",
                    "Jalankan dengan python manage.py test. Django membuat database uji",
                    "sementara, menjalankan tesnya, lalu membuangnya lagi, jadi data aslimu",
                    "aman.",
                ],
            },
            {
                "heading": "DRF atau Ninja?",
                "body": [
                    "                   DRF                     Django Ninja",
                    "  gaya             class, serializer       fungsi, type hints",
                    "  validasi         serializer              Pydantic",
                    "  dokumentasi      perlu paket tambahan    OpenAPI bawaan",
                    "  halaman coba     browsable API           Swagger UI di /docs",
                    "  async            terbatas                didukung",
                    "  ekosistem        sangat luas             lebih kecil",
                    "",
                    "Pilih DRF kalau kamu bergabung dengan proyek yang sudah ada (kemungkinan",
                    "besar memakai DRF) atau butuh paket pendukungnya yang banyak, seperti",
                    "djangorestframework-simplejwt untuk login berbasis JWT (dibahas di bab",
                    "Autentikasi). Pilih Ninja untuk proyek baru yang ingin kode ringkas,",
                    "dokumentasi otomatis, dan endpoint async.",
                    "",
                    "Versi stabil saat materi ini ditulis (Oktober 2026): DRF 3.18.3",
                    "berlisensi BSD-3-Clause, Django Ninja 1.7.1 berlisensi MIT.",
                    "",
                    "Jebakan: lupa select_related di queryset viewset. Serializer yang",
                    "membaca kategori tiap produk akan mengulang masalah N+1 dari materi",
                    "sebelumnya, cuma kali ini tersembunyi di balik satu baris fields.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola Django sebagai panel admin plus DRF atau Ninja sebagai API dipakai",
                    "di banyak produk yang punya aplikasi seluler: aplikasi pemesanan,",
                    "absensi, dan marketplace kecil. Data dikelola lewat /admin/, sedangkan",
                    "aplikasi ponsel membaca dan menulis lewat /api/.",
                    "",
                    "Kasus kecil: aplikasi kasir koperasi dari materi sebelumnya butuh",
                    "endpoint untuk melihat barang dan mengurangi stok, tapi kasir nggak",
                    "boleh mengubah harga.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat BarangSerializer dengan fields id, nama, harga, stok, dan",
                    "     jadikan harga read_only lewat read_only_fields di Meta.",
                    "  2. Buat BarangViewSet turunan ModelViewSet dengan permission_classes",
                    "     IsAuthenticated, lalu daftarkan di DefaultRouter.",
                    "  3. Uji dengan klien API: GET /api/barang/ harus 200, PATCH berisi stok",
                    "     baru harus 200, PATCH berisi harga baru harus tetap menyimpan harga",
                    "     lama.",
                    "  4. Tambahkan paginasi global di REST_FRAMEWORK supaya daftar barang",
                    "     yang panjang nggak dikirim sekaligus.",
                ],
            },
        ],
    },
    {
        "title": "20. Peta Framework Python",
        "sections": [
            {
                "body": [
                    "Flask, FastAPI, dan Django menguasai sebagian besar proyek Python. Di",
                    "luar ketiganya masih ada beberapa framework yang akan kamu temui di kode",
                    "lama, di roadmap belajar, atau di lowongan tertentu. Materi ini peta",
                    "singkatnya, supaya kamu tahu masing-masing itu apa dan kapan masuk akal",
                    "dipilih.",
                    "",
                    "Satu istilah dari bab 01 yang membantu membaca peta ini. WSGI adalah",
                    "kontrak lama untuk aplikasi sinkron, dan ASGI kontrak baru yang",
                    "mendukung async dan WebSocket. Framework ASGI biasanya dijalankan",
                    "Uvicorn atau Granian, sedangkan framework sinkron biasanya dijalankan",
                    "Gunicorn.",
                ],
            },
            {
                "heading": "Tabel perbandingan",
                "bahasa": "teks",
                "code": """Framework  Kontrak        Versi (Okt 2026)  Status
Litestar   ASGI           2.25.0            aktif
Quart      ASGI           0.23.1            aktif (proyek Pallets)
Sanic      ASGI/server    25.12.1           stabil
Falcon     WSGI dan ASGI  4.4.0             stabil
aiohttp    asyncio        3.14.5            aktif, lebih sering klien
Tornado    asyncio        6.5.10            dirawat, jarang dipilih
Pyramid    WSGI           2.1.0             menurun
Bottle     WSGI           0.13.4            stabil, rilis jarang""",
            },
            {
                "heading": "Yang modern dan async",
                "body": [
                    "Litestar (dulu bernama Starlite) adalah framework ASGI lengkap:",
                    "dependency injection, validasi, plugin ORM, dan OpenAPI bawaan. Ia",
                    "pesaing paling dekat FastAPI. Satu beda yang terasa saat dicoba: data",
                    "yang nggak valid dibalas 400, sedangkan FastAPI membalas 422. Lisensinya",
                    "MIT.",
                    "",
                    "Quart adalah Flask versi async, dirawat proyek Pallets yang sama dengan",
                    "Flask. API-nya hampir identik, jadi kode Flask bisa dipindah dengan",
                    "menambah async dan await. Pilih ini kalau timmu sudah nyaman dengan",
                    "Flask tapi butuh WebSocket atau banyak panggilan jaringan bersamaan.",
                    "",
                    "Sanic dirancang cepat sejak awal dan membawa server sendiri, jadi bisa",
                    "jalan tanpa Uvicorn. Nomor versinya berbasis tahun.bulan: 25.12 berarti",
                    "Desember 2025.",
                    "",
                    "  from quart import Quart",
                    "",
                    "  app = Quart(__name__)",
                    "",
                    "",
                    "  @app.get(\"/halo/<nama>\")",
                    "  async def halo(nama):",
                    "      return {\"pesan\": f\"Halo, {nama}!\"}",
                    "",
                    "Contoh Quart di atas sama persis dengan Flask, kecuali kata async. Waktu",
                    "diuji dengan test client Quart, /halo/Sari dibalas 200 dengan {\"pesan\":",
                    "\"Halo, Sari!\"}.",
                ],
            },
            {
                "heading": "Yang ramping dan yang senior",
                "body": [
                    "Falcon fokus ke API REST yang cepat dan minim lapisan. Rutenya mengarah",
                    "ke class \"resource\" dengan method on_get, on_post, dan seterusnya. Ia",
                    "mendukung kedua kontrak, sinkron dan async, sekaligus.",
                    "",
                    "aiohttp adalah pustaka HTTP async untuk klien dan server. Di proyek",
                    "nyata ia jauh lebih sering dipakai sebagai klien, misalnya untuk",
                    "memanggil ratusan API pihak ketiga bersamaan, daripada sebagai server.",
                    "",
                    "Tornado termasuk framework async generasi awal, lahir di FriendFeed",
                    "sebelum asyncio ada. Ia masih dirawat dan tercantum di roadmap.sh",
                    "Python, tapi jarang dipilih untuk proyek baru. Kamu akan menemuinya di",
                    "sistem lama dan di beberapa alat, misalnya server Jupyter generasi lama.",
                    "",
                    "Pyramid dari Pylons Project fleksibel dari aplikasi kecil sampai besar,",
                    "tapi komunitasnya mengecil. Kalau kamu mewarisi proyek Pyramid, rawat.",
                    "Kalau mulai dari nol, pilih yang lain.",
                    "",
                    "Bottle adalah microframework satu berkas tanpa dependensi. Rilisnya",
                    "jarang (0.13.4 terbit Juni 2025), tapi justru karena kecil ia enak",
                    "dibaca untuk memahami cara framework bekerja. Coba buka bottle.py dan",
                    "cari method __call__: di situ kontrak aplikasi sebagai fungsi dari bab",
                    "01 terlihat utuh.",
                ],
            },
            {
                "heading": "Contoh kecil: Falcon",
                "body": [
                    "Supaya terasa bedanya, ini satu endpoint di Falcon. Rutenya nggak",
                    "menunjuk fungsi, tapi objek resource. Falcon memanggil method yang",
                    "namanya cocok dengan metode HTTP:",
                    "",
                    "  import falcon",
                    "",
                    "",
                    "  class SumberTugas:",
                    "      def on_get(self, req, resp, tugas_id):",
                    "          resp.media = {\"id\": tugas_id, \"judul\": \"Belajar Falcon\"}",
                    "",
                    "",
                    "  app = falcon.App()",
                    "  app.add_route(\"/tugas/{tugas_id:int}\", SumberTugas())",
                    "",
                    "resp.media diubah Falcon jadi JSON. {tugas_id:int} menolak nilai yang",
                    "bukan angka sebelum on_get dipanggil. Saat diuji dengan falcon.testing,",
                    "GET /tugas/3 dibalas {\"id\": 3, \"judul\": \"Belajar Falcon\"}. Kalau nanti",
                    "kamu menambah on_delete di class yang sama, alamat yang sama langsung",
                    "menerima DELETE juga.",
                    "",
                    "Cara cepat menilai status sebuah framework: lihat tanggal rilis",
                    "terakhirnya, berapa lama isu dibiarkan tanpa jawaban, dan apakah",
                    "dokumentasinya masih menyebut versi Python terbaru. Angka bintang GitHub",
                    "kurang berguna karena nggak pernah turun walau proyeknya sudah",
                    "ditinggal.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  1. Butuh admin, auth, dan ORM sekaligus: Django.",
                    "  2. Butuh API dengan validasi dan dokumentasi otomatis: FastAPI, atau",
                    "     Litestar kalau ingin DI dan plugin yang lebih lengkap.",
                    "  3. Sudah punya kode Flask dan butuh async: Quart.",
                    "  4. API kecil yang mengejar kecepatan dan lapisan setipis mungkin:",
                    "     Falcon.",
                    "  5. Mewarisi Tornado atau Pyramid: pelajari secukupnya untuk merawat,",
                    "     rencanakan migrasi kalau aplikasinya terus tumbuh.",
                    "",
                    "Jebakan: memilih framework karena angka benchmark. Di aplikasi nyata,",
                    "waktu respons hampir selalu habis di database dan panggilan jaringan,",
                    "jadi selisih kecepatan router jarang terasa. Ukuran komunitas,",
                    "dokumentasi, dan pustaka pendukung biasanya lebih menentukan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Framework kecil seperti Falcon dan Litestar sering dipakai untuk layanan",
                    "internal bertugas tunggal, misalnya layanan pembuat PDF atau penerus",
                    "webhook, sementara aplikasi utamanya tetap Django atau FastAPI.",
                    "",
                    "Kasus kecil: timmu mewarisi layanan notifikasi lama berbasis Tornado",
                    "yang makin susah dirawat, dan kamu diminta mengusulkan pengganti.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Catat apa yang dikerjakan layanan itu: endpoint, WebSocket atau",
                    "     bukan, dan pustaka async yang dipakai.",
                    "  2. Kalau ada WebSocket dan banyak I/O bersamaan, pilih framework ASGI",
                    "     (FastAPI, Litestar, atau Quart).",
                    "  3. Tulis ulang satu endpoint dulu di framework baru, jalankan",
                    "     berdampingan di belakang reverse proxy, dan bandingkan hasilnya",
                    "     dengan yang lama.",
                    "  4. Pindahkan endpoint lain satu per satu, lalu matikan layanan Tornado",
                    "     setelah lalu lintasnya nol.",
                ],
            },
        ],
    },
    {
        "title": "21. Spring Boot: Proyek Pertama dan Dependency Injection",
        "sections": [
            {
                "body": [
                    "Kalau kamu membuka lowongan backend di bank, perusahaan asuransi, atau",
                    "operator seluler, nama Spring Boot sering muncul. Ia framework Java",
                    "untuk membuat aplikasi web dan API yang siap dipakai di produksi. Di",
                    "Survei Stack Overflow 2026, 12,8% responden memakainya, dan setengah",
                    "dari pemakainya ingin terus memakainya.",
                    "",
                    "Ada dua nama yang sering tertukar. Spring Framework adalah intinya:",
                    "kontainer yang membuat dan menyambungkan objek, Spring MVC untuk web,",
                    "dan dukungan transaksi. Spring Boot berdiri di atasnya dan mengurus hal",
                    "yang dulu ditulis manual: pengaturan otomatis, server web yang sudah",
                    "tertanam, dan paket dependensi siap pakai. Hampir semua proyek Spring",
                    "baru dimulai dari Spring Boot.",
                    "",
                    "Prasyaratnya kurikulum Java: class, interface, dan anotasi. Bagian Ktor",
                    "di materi peta nanti butuh kurikulum Kotlin.",
                ],
            },
            {
                "heading": "Masalahnya: siapa yang membuat objek?",
                "body": [
                    "Bayangkan ProdukService butuh repository untuk menyimpan data. Cara",
                    "paling gampang, service membuat sendiri dengan new. Masalahnya, service",
                    "jadi terikat ke satu jenis penyimpanan. Mau diuji dengan data palsu,",
                    "harus mengubah kodenya. Mau pindah dari memori ke PostgreSQL, harus",
                    "mengubah kodenya lagi.",
                    "",
                    "Dependency injection (DI) membalik arahnya: service cuma bilang \"aku",
                    "butuh sesuatu yang bisa menyimpan produk\", lalu pihak lain yang",
                    "memberikannya lewat konstruktor. Mirip juru masak yang nggak belanja",
                    "sendiri; bahan diantar pemasok, dan ia tinggal memasak. Pihak yang",
                    "mengantar itu disebut kontainer IoC (inversion of control, pembalikan",
                    "kendali). Contoh di bawah menunjukkan DI tanpa Spring sama sekali,",
                    "supaya kelihatan apa yang nanti dikerjakan Spring untukmu.",
                ],
            },
            {
                "heading": "DI dengan tangan",
                "bahasa": "java",
                "code": """import java.util.ArrayList;
import java.util.List;

interface ProdukRepository {
    void simpan(String nama);
    List<String> semua();
}

class RepositoriMemori implements ProdukRepository {
    private final List<String> data = new ArrayList<>();

    public void simpan(String nama) { data.add(nama); }

    public List<String> semua() { return data; }
}

class ProdukService {
    private final ProdukRepository repo;

    // Dependensi masuk lewat konstruktor, bukan dibuat sendiri
    ProdukService(ProdukRepository repo) {
        this.repo = repo;
    }

    String tambah(String nama) {
        if (nama.isBlank()) {
            return "ditolak: nama kosong";
        }
        repo.simpan(nama);
        return "tersimpan: " + nama;
    }

    int jumlah() { return repo.semua().size(); }
}

public class Main {
    public static void main(String[] args) {
        // Di Spring, dua baris ini dikerjakan kontainer IoC
        ProdukRepository repo = new RepositoriMemori();
        ProdukService service = new ProdukService(repo);

        System.out.println(service.tambah("Teh Botol"));
        System.out.println(service.tambah(" "));
        System.out.println(service.tambah("Kopi Susu"));
        System.out.println("jumlah produk: " + service.jumlah());
    }
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "",
                    "  tersimpan: Teh Botol",
                    "  ditolak: nama kosong",
                    "  tersimpan: Kopi Susu",
                    "  jumlah produk: 2",
                    "",
                    "ProdukService nggak tahu dan nggak peduli datanya disimpan di mana. Ia",
                    "cuma kenal interface ProdukRepository. Untuk pengujian, kamu bisa",
                    "memberinya repository palsu; untuk produksi, repository yang menyimpan",
                    "ke database. Kelas service-nya sendiri nggak berubah satu baris pun.",
                    "",
                    "Di aplikasi sungguhan ada puluhan kelas seperti ini, dan",
                    "menyambungkannya dengan tangan di main jadi melelahkan. Spring mengambil",
                    "alih pekerjaan itu: kamu menandai kelas dengan @Service atau",
                    "@Repository, dan kontainer Spring yang membuat objeknya lalu mengisi",
                    "konstruktornya.",
                ],
            },
            {
                "heading": "Proyek pertama",
                "bahasa": "terminal",
                "code": "curl https://start.spring.io/starter.zip \\\n  -d type=maven-project -d javaVersion=21 \\\n  -d dependencies=web,validation,data-jpa,postgresql \\\n  -d name=toko -o toko.zip\nunzip toko.zip -d toko && cd toko\n./mvnw spring-boot:run",
            },
            {
                "body": [
                    "Perintah curl itu memanggil Spring Initializr, situs pembuat kerangka",
                    "proyek yang juga bisa kamu buka lewat browser di start.spring.io. Setiap",
                    "nama di dependencies adalah starter: satu dependensi yang membawa",
                    "sekumpulan pustaka yang biasa dipakai bersama. spring-boot-starter-web",
                    "misalnya membawa Spring MVC, Tomcat sebagai server tertanam, dan Jackson",
                    "untuk JSON.",
                    "",
                    "Kelas utamanya pendek sekali:",
                    "",
                    "  package com.contoh.toko;",
                    "",
                    "  import org.springframework.boot.SpringApplication;",
                    "  import org.springframework.boot.autoconfigure.SpringBootApplication;",
                    "",
                    "  @SpringBootApplication",
                    "  public class TokoApplication {",
                    "      public static void main(String[] args) {",
                    "          SpringApplication.run(TokoApplication.class, args);",
                    "      }",
                    "  }",
                    "",
                    "@SpringBootApplication menyalakan tiga hal. Pemindaian komponen mencari",
                    "kelas bertanda @Component, @Service, @Repository, dan @RestController di",
                    "paket yang sama atau di bawahnya. Autoconfiguration melihat pustaka apa",
                    "yang ada lalu memasang pengaturan yang masuk akal, misalnya \"ada driver",
                    "PostgreSQL, berarti siapkan koneksi database\". Lalu kelas itu sendiri",
                    "boleh berisi pengaturan tambahan.",
                    "",
                    "Jebakan: autoconfiguration terasa seperti sulap, dan pemula sering nggak",
                    "tahu kenapa sesuatu terpasang. Jalankan aplikasi dengan --debug, dan",
                    "Spring mencetak laporan pengaturan mana yang aktif beserta alasannya.",
                    "Kelas yang ditaruh di luar paket com.contoh.toko juga nggak akan",
                    "ditemukan pemindaian komponen.",
                ],
            },
            {
                "heading": "Controller REST",
                "bahasa": "java",
                "code": """package com.contoh.toko.produk;

import java.util.List;

import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/produk")
public class ProdukController {

    private final ProdukService service;

    public ProdukController(ProdukService service) {
        this.service = service;
    }

    @GetMapping
    public List<Produk> semua() {
        return service.semua();
    }

    @GetMapping("/{id}")
    public Produk satu(@PathVariable Long id) {
        return service.cari(id);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Produk tambah(@Valid @RequestBody ProdukBaru data) {
        return service.tambah(data);
    }
}""",
            },
            {
                "body": [
                    "Bentuknya sama dengan DI tangan tadi: ProdukController meminta",
                    "ProdukService di konstruktornya, dan Spring yang mengisinya. Objek yang",
                    "dikelola Spring disebut bean, dan secara bawaan tiap bean dibuat sekali",
                    "lalu dipakai bersama (singleton). Hindari @Autowired di atas field;",
                    "injeksi lewat konstruktor membuat dependensi kelihatan dan gampang",
                    "diganti saat pengujian.",
                    "",
                    "Permintaan HTTP pertama kali diterima DispatcherServlet, \"resepsionis\"",
                    "Spring MVC. Ia mencari method controller yang cocok dari anotasi",
                    "@GetMapping atau @PostMapping, mengisi @PathVariable dari URL, mengubah",
                    "body JSON jadi objek lewat @RequestBody, lalu mengubah nilai",
                    "kembaliannya jadi JSON. ProdukBaru bisa berupa record dengan anotasi",
                    "validasi:",
                    "",
                    "  public record ProdukBaru(@NotBlank String nama,",
                    "                           @Min(1000) int harga) {}",
                    "",
                    "Karena ada @Valid, body yang namanya kosong atau harganya di bawah 1000",
                    "dibalas 400 sebelum method tambah dipanggil.",
                ],
            },
            {
                "heading": "Thymeleaf untuk halaman HTML",
                "bahasa": "html",
                "code": """<ul>
  <li th:each="p : ${produk}">
    <span th:text="${p.nama}">Nama produk</span>
    <span th:text="${p.harga}">0</span>
  </li>
</ul>""",
            },
            {
                "body": [
                    "Kalau aplikasimu membalas halaman HTML, bukan JSON, pasangan bawaannya",
                    "Thymeleaf (versi 3.1.5 saat materi ini ditulis). Controller-nya memakai",
                    "@Controller, memasukkan data ke objek Model, lalu mengembalikan nama",
                    "template seperti \"daftar\". Thymeleaf menulis perintahnya sebagai atribut",
                    "HTML (th:each, th:text), jadi berkas templatenya tetap bisa dibuka",
                    "langsung di browser sebagai HTML biasa. Teks contoh di dalam span",
                    "diganti isi sungguhan saat dirender, dan nilainya otomatis di-escape.",
                    "Pendahulunya, JSP, masih ada di aplikasi lama tapi nggak dipakai lagi di",
                    "proyek Spring Boot baru.",
                ],
            },
            {
                "heading": "javax atau jakarta? Versi saat ini",
                "body": [
                    "Spring Boot 4 rilis November 2025 dan berdiri di atas Spring Framework 7",
                    "serta Jakarta EE 11. Saat materi ini ditulis (Oktober 2026), versi",
                    "stabil terbarunya 4.1.1 dan Spring Framework 7.0.9, keduanya berlisensi",
                    "Apache-2.0. Butuh minimal Java 17.",
                    "",
                    "Jebakan yang paling sering menimpa pemula: tutorial lama. Sampai Spring",
                    "Boot 2, anotasi seperti @Entity dan @Valid diimpor dari paket javax.",
                    "Sejak Jakarta EE 9 namanya berganti jadi jakarta, dan Spring Boot 3 ke",
                    "atas cuma mengenal jakarta. Kalau kamu menyalin kode berisi import",
                    "javax.persistence ke proyek baru, kodenya gagal dikompilasi. Ganti",
                    "awalannya jadi jakarta. Banyak contoh di internet juga masih memakai",
                    "cara konfigurasi Spring Security lama yang sudah dihapus; itu dibahas di",
                    "bab Autentikasi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Spring Boot banyak dipakai untuk sistem perbankan inti, layanan",
                    "pembayaran, aplikasi kepegawaian, dan API internal perusahaan besar,",
                    "karena ekosistemnya lengkap dan pengembang Java mudah dicari.",
                    "",
                    "Kasus kecil: kamu diminta membuat API daftar cabang kantor yang dibaca",
                    "aplikasi seluler, dan nanti datanya akan pindah dari daftar tetap ke",
                    "database.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat proyek di Spring Initializr dengan starter web dan validation.",
                    "  2. Tulis interface CabangRepository dan satu implementasi berbasis",
                    "     List di memori, beri anotasi @Repository.",
                    "  3. Buat CabangService yang menerima CabangRepository lewat",
                    "     konstruktor, lalu CabangController dengan @GetMapping.",
                    "  4. Saat database siap, ganti implementasi repository dengan Spring",
                    "     Data JPA (materi berikutnya). Service dan controller nggak perlu",
                    "     disentuh sama sekali, karena keduanya cuma kenal interface-nya.",
                ],
            },
        ],
    },
    {
        "title": "22. Spring Data JPA dan Hibernate di Spring Boot",
        "sections": [
            {
                "body": [
                    "Menyimpan data dari Java ke database melewati beberapa lapisan, dan",
                    "nama-namanya sering dipakai bergantian seolah sama. Dari bawah ke atas:",
                    "",
                    "  - JDBC: API bawaan Java untuk terhubung ke database dan menjalankan",
                    "    SQL. Tiap database menyediakan driver JDBC-nya.",
                    "  - JPA (Jakarta Persistence): spesifikasi, alias daftar aturan, untuk",
                    "    memetakan objek ke tabel. Versi terbarunya 3.2, bagian dari Jakarta",
                    "    EE 11.",
                    "  - Hibernate ORM: implementasi JPA yang paling banyak dipakai.",
                    "    Implementasi lain misalnya EclipseLink.",
                    "  - Spring Data JPA: lapisan Spring di atas JPA. Kamu cukup menulis",
                    "    interface, implementasinya dibuatkan.",
                    "",
                    "Starter data-jpa memasang ketiga lapisan atas sekaligus, dan starter",
                    "postgresql menambahkan driver JDBC-nya.",
                ],
            },
            {
                "heading": "JDBC polos, supaya tahu apa yang disembunyikan",
                "bahasa": "java",
                "code": """String sql = "SELECT id, nama, harga FROM produk WHERE harga < ?";
try (Connection conn = dataSource.getConnection();
     PreparedStatement st = conn.prepareStatement(sql)) {
    st.setInt(1, 20000);
    try (ResultSet rs = st.executeQuery()) {
        while (rs.next()) {
            hasil.add(new Produk(rs.getLong("id"),
                    rs.getString("nama"), rs.getInt("harga")));
        }
    }
}""",
            },
            {
                "body": [
                    "Tanda ? diisi lewat setInt, bukan disambung ke string SQL. Itu yang",
                    "mencegah SQL injection, dan JPA melakukan hal yang sama di belakang",
                    "layar. Sisanya pekerjaan rutin: membuka koneksi, mengisi parameter,",
                    "membaca kolom satu per satu, menutup semuanya. Pekerjaan rutin itu yang",
                    "diambil alih lapisan di atasnya.",
                ],
            },
            {
                "heading": "Entity",
                "bahasa": "java",
                "code": """package com.contoh.toko.produk;

import jakarta.persistence.*;

@Entity
public class Produk {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String nama;

    private int harga;

    @ManyToOne(fetch = FetchType.LAZY)
    private Kategori kategori;

    protected Produk() {}   // dibutuhkan JPA

    public Produk(String nama, int harga, Kategori kategori) {
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
    }

    // getter dihilangkan supaya ringkas
}""",
            },
            {
                "body": [
                    "@Entity menandai kelas yang punya tabel. @Id dan @GeneratedValue membuat",
                    "kolom id yang diisi database. @ManyToOne adalah relasi banyak produk ke",
                    "satu kategori, dan FetchType.LAZY berarti kategori baru diambil saat",
                    "kamu memanggil getKategori(). Konstruktor tanpa parameter wajib ada",
                    "karena Hibernate membuat objek dulu baru mengisi field-nya.",
                ],
            },
            {
                "heading": "Repository dari sebuah interface",
                "bahasa": "java",
                "code": """package com.contoh.toko.produk;

import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface ProdukRepository extends JpaRepository<Produk, Long> {

    List<Produk> findByNamaContainingIgnoreCase(String kata);

    List<Produk> findByHargaLessThanOrderByHargaAsc(int batas);

    long countByKategoriNama(String namaKategori);

    Page<Produk> findByKategoriNama(String nama, Pageable halaman);

    @Query("select p from Produk p join fetch p.kategori where p.harga < :batas")
    List<Produk> murahBesertaKategori(@Param("batas") int batas);
}""",
            },
            {
                "body": [
                    "Interface ini nggak punya implementasi, dan memang nggak perlu. Dengan",
                    "mewarisi JpaRepository kamu langsung dapat save, findById, findAll,",
                    "deleteById, dan count. Method lain dibaca Spring Data dari namanya:",
                    "findByHargaLessThanOrderByHargaAsc diterjemahkan jadi kueri harga < ?",
                    "yang diurutkan naik. countByKategoriNama bahkan menyeberang relasi ke",
                    "kolom nama di tabel kategori. Kalau namanya menyebut properti yang nggak",
                    "ada, aplikasi gagal saat dinyalakan, jadi kesalahan ketik ketahuan",
                    "sebelum ada pengguna yang kena.",
                    "",
                    "Kueri yang terlalu rumit untuk dijadikan nama method ditulis dengan",
                    "@Query dalam JPQL, bahasa kueri JPA yang menyebut nama kelas dan field,",
                    "bukan tabel dan kolom. join fetch di contoh itu mengambil kategori dalam",
                    "kueri yang sama, cara JPA menghindari masalah N+1. Parameter Pageable",
                    "membuat paginasi gratis: PageRequest.of(0, 20) mengambil 20 baris",
                    "pertama sekaligus menghitung totalnya.",
                ],
            },
            {
                "heading": "Pengaturan koneksi",
                "bahasa": "ini",
                "code": """spring.datasource.url=jdbc:postgresql://localhost:5432/toko
spring.datasource.username=toko
spring.datasource.password=${DB_PASSWORD}
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.open-in-view=false""",
            },
            {
                "body": [
                    "Isi itu masuk ke src/main/resources/application.properties. Kata sandi",
                    "dibaca dari variabel lingkungan DB_PASSWORD, jadi nggak ikut ter-commit.",
                    "ddl-auto menentukan apakah Hibernate boleh mengubah tabel. Nilai create",
                    "dan update enak untuk coba-coba, tapi berbahaya di produksi karena",
                    "Hibernate bisa mengubah atau menghapus kolom tanpa kamu sadari. Di",
                    "produksi pakai validate (cuma memeriksa tabel cocok dengan entity) dan",
                    "serahkan perubahan tabel ke alat migrasi.",
                    "",
                    "open-in-view secara bawaan menyala di Spring Boot, dan Spring mencetak",
                    "peringatan soal itu saat aplikasi mulai. Ia menahan koneksi database",
                    "sampai respons selesai ditulis, supaya relasi LAZY masih bisa dibaca di",
                    "mana saja. Mematikannya memaksa kamu mengambil semua data yang",
                    "dibutuhkan di service, yang lebih jelas dan lebih hemat koneksi.",
                ],
            },
            {
                "heading": "Migrasi: Flyway atau Liquibase",
                "bahasa": "postgresql",
                "code": """-- src/main/resources/db/migration/V1__buat_tabel_produk.sql
CREATE TABLE kategori (
    id   BIGSERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE produk (
    id          BIGSERIAL PRIMARY KEY,
    nama        VARCHAR(100) NOT NULL,
    harga       INTEGER NOT NULL,
    kategori_id BIGINT REFERENCES kategori (id)
);""",
            },
            {
                "body": [
                    "Flyway menjalankan berkas SQL bernomor (V1__, V2__, dan seterusnya)",
                    "secara berurutan, lalu mencatat yang sudah jalan di tabel",
                    "flyway_schema_history. Tambahkan dependensinya, dan Spring Boot",
                    "menjalankan migrasi otomatis setiap aplikasi mulai. Flyway dibuat",
                    "Redgate; edisi Community-nya berlisensi Apache-2.0, versi terbarunya",
                    "13.10.3 saat materi ini ditulis.",
                    "",
                    "Liquibase memakai changelog dalam XML, YAML, JSON, atau SQL, dan kuat di",
                    "urusan rollback (membatalkan perubahan). Perhatikan lisensinya: sejak",
                    "versi 5.0, Liquibase memakai FSL-1.1 (Functional Source License).",
                    "Kodenya bisa dibaca dan dipakai, tapi untuk versi baru ia bukan lisensi",
                    "open source dalam arti resmi; tiap versi baru berubah jadi Apache-2.0",
                    "dua tahun sesudah dirilis. Versi terbarunya 5.0.4. Untuk proyek kantor,",
                    "tanyakan dulu ke tim apakah lisensi seperti itu boleh dipakai.",
                ],
            },
            {
                "heading": "Hibernate: lisensi baru, jebakan lama",
                "body": [
                    "Hibernate ORM 7 pindah lisensi dari LGPL-2.1 ke Apache-2.0, lisensi yang",
                    "sama dengan Spring. Modul Envers, pencatat riwayat perubahan data, nggak",
                    "ikut dilisensi ulang. Versi stabil terbarunya 7.4.13 (Oktober 2026),",
                    "sementara 8.0 masih beta. Spring Data JPA sendiri di versi 4.1.1.",
                    "",
                    "Ada dua galat yang hampir pasti kamu temui. Yang pertama",
                    "LazyInitializationException, muncul saat relasi LAZY dibaca sesudah sesi",
                    "database ditutup. Yang kedua masalah N+1, saat perulangan atas daftar",
                    "produk memicu satu kueri kategori per produk. Obat keduanya biasanya",
                    "sama: ambil relasinya sejak awal dengan join fetch atau @EntityGraph.",
                    "Siklus hidup entity, transaksi, dan indeks dibahas mendalam di kurikulum",
                    "Database.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Spring Data JPA dipakai di hampir semua aplikasi Spring Boot yang",
                    "menyimpan data relasional, dari sistem pemesanan tiket sampai aplikasi",
                    "koperasi simpan pinjam, biasanya dipasangkan dengan Flyway atau",
                    "Liquibase.",
                    "",
                    "Kasus kecil: endpoint daftar pesanan di aplikasimu makin lambat. Log SQL",
                    "menunjukkan ratusan kueri SELECT ke tabel pelanggan untuk satu halaman",
                    "berisi 100 pesanan.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Nyalakan spring.jpa.show-sql=true di lingkungan pengembangan dan",
                    "     hitung kuerinya untuk satu permintaan.",
                    "  2. Cari perulangan yang memanggil pesanan.getPelanggan(); itu sumber",
                    "     N+1.",
                    "  3. Tambahkan method repository dengan @Query yang memakai join fetch",
                    "     p.pelanggan, atau pasang @EntityGraph di method yang sudah ada.",
                    "  4. Pakai Pageable supaya satu halaman cuma mengambil 20 pesanan, lalu",
                    "     ukur lagi: targetnya satu atau dua kueri per permintaan.",
                ],
            },
        ],
    },
    {
        "title": "23. Peta Framework Java, Kotlin, dan JVM",
        "sections": [
            {
                "body": [
                    "Spring Boot memang paling banyak dipakai, tapi JVM (mesin yang",
                    "menjalankan Java dan Kotlin) punya banyak framework lain. Sebagian",
                    "bersaing langsung dengan Spring Boot, sebagian melengkapinya, dan",
                    "sebagian tinggal warisan yang masih harus dirawat. Versi di tabel ini",
                    "per Oktober 2026.",
                ],
            },
            {
                "heading": "Tabel perbandingan",
                "bahasa": "teks",
                "code": """Nama          Bahasa         Versi            Status
Spring Cloud  Java/Kotlin    2025.1.2         aktif, pelengkap Spring Boot
Quarkus       Java/Kotlin    3.40.1           aktif, 4.0 beta
Micronaut     Java/Kotlin    Platform 5.2.2   aktif
Jakarta EE    Java           11               aktif, 12 dikembangkan
Helidon       Java           27.0.0           aktif, LTS 4.5.x
Vert.x        Java/Kotlin    5.2.1            aktif
Javalin       Java/Kotlin    7.2.3            aktif
Ktor          Kotlin         3.6.0            aktif
Play          Scala/Java     3.0.12           menurun
Dropwizard    Java           5.0.2            menurun
Apache Struts Java           7.4.0            usang untuk proyek baru""",
            },
            {
                "heading": "Pesaing Spring Boot",
                "body": [
                    "Quarkus dari Red Hat dirancang untuk kontainer dan cloud: start dalam",
                    "hitungan milidetik dan memori kecil, terutama kalau dikompilasi jadi",
                    "program native lewat GraalVM. Ia memakai API standar Jakarta EE dan",
                    "MicroProfile, jadi ilmunya terbawa ke server lain. Di Survei Stack",
                    "Overflow 2026 pemakainya cuma 0,3%, tapi 80,8% pemakainya ingin terus",
                    "memakainya, angka tertinggi di kategori web framework. Quarkus 4.0 beta",
                    "pertama terbit 1 Oktober 2026.",
                    "",
                    "Micronaut mengerjakan dependency injection saat kompilasi, tanpa",
                    "refleksi saat program jalan. Hasilnya start cepat dan cocok untuk",
                    "serverless. Ia mendukung Java, Kotlin, dan Groovy.",
                    "",
                    "Helidon dari Oracle punya dua gaya: Helidon SE yang ringan berbasis",
                    "virtual threads, dan Helidon MP yang mengikuti MicroProfile. Helidon 27",
                    "mengikuti nomor JDK dan butuh Java 27, sedangkan Helidon 4 tetap jadi",
                    "jalur LTS.",
                    "",
                    "Jakarta EE (dulu Java EE) adalah kumpulan spesifikasi, jadi ia nggak",
                    "diunduh sebagai satu framework. Isinya antara lain Servlet, JPA,",
                    "Contexts and Dependency Injection, REST, dan Bean Validation. Server",
                    "seperti WildFly, Payara, dan Open Liberty mengimplementasikannya, dan",
                    "Spring sendiri memakai banyak spesifikasinya.",
                ],
            },
            {
                "heading": "Yang ringan dan yang berbasis event",
                "body": [
                    "Javalin terasa seperti Express versi Java: kecil, tanpa anotasi, dan",
                    "enak untuk API sederhana atau untuk belajar sebelum masuk Spring. Di",
                    "Javalin 7, rute wajib didaftarkan di dalam config saat aplikasi dibuat:",
                    "",
                    "  import io.javalin.Javalin;",
                    "",
                    "  public class Main {",
                    "      public static void main(String[] args) {",
                    "          Javalin.create(config -> {",
                    "              config.routes.get(\"/halo/{nama}\", ctx ->",
                    "                  ctx.result(\"Halo, \" + ctx.pathParam(\"nama\") + \"!\"));",
                    "          }).start(7070);",
                    "      }",
                    "  }",
                    "",
                    "Ktor buatan JetBrains adalah pilihan alami sesudah kurikulum Kotlin. Ia",
                    "dibangun di atas coroutine, jadi kode async-nya terbaca seperti kode",
                    "biasa. Versi 3.6 menambah dukungan OpenID Connect dan HTTP/2. Pasangan",
                    "ORM-nya biasanya Exposed, juga dari JetBrains.",
                    "",
                    "  fun main() {",
                    "      embeddedServer(Netty, port = 8080) {",
                    "          routing {",
                    "              get(\"/halo/{nama}\") {",
                    "                  val nama = call.parameters[\"nama\"]",
                    "                  call.respondText(\"Halo, $nama!\")",
                    "              }",
                    "          }",
                    "      }.start(wait = true)",
                    "  }",
                    "",
                    "Eclipse Vert.x adalah toolkit reaktif berbasis event loop, mirip cara",
                    "kerja Node.js tapi di JVM. Cocok untuk layanan yang memegang banyak",
                    "koneksi sekaligus, dengan gaya kode yang lebih menantang.",
                ],
            },
            {
                "heading": "Pelengkap dan warisan",
                "body": [
                    "Spring Cloud adalah kumpulan proyek Spring untuk sistem terdistribusi:",
                    "gateway, config server, service discovery, circuit breaker, dan klien",
                    "HTTP OpenFeign. Nomor versinya berupa release train (2025.1.2, nama",
                    "sandi Oakwood) yang dipasangkan dengan versi Spring Boot tertentu.",
                    "Sebagian fungsinya, seperti service discovery, kini sering diambil alih",
                    "Kubernetes.",
                    "",
                    "Play Framework untuk Scala dan Java pindah dari Akka ke Apache Pekko di",
                    "versi 3, dan komunitasnya mengecil. Dropwizard merangkai Jetty, Jersey,",
                    "dan Jackson jadi paket siap produksi; masih dirawat, tapi jarang dipilih",
                    "untuk proyek baru.",
                    "",
                    "Apache Struts adalah framework MVC lama berbasis action dan JSP. Ia",
                    "masih mendapat rilis keamanan, tapi namanya identik dengan sistem",
                    "warisan, termasuk kebocoran data Equifax tahun 2017 yang terjadi lewat",
                    "celah Struts yang belum ditambal. Pelajari kalau pekerjaanmu merawat",
                    "sistem lama; jangan pilih untuk proyek baru.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  1. Bergabung dengan tim Java di perusahaan: hampir pasti Spring Boot,",
                    "     kadang Jakarta EE.",
                    "  2. Layanan kecil di kontainer yang harus start cepat dan hemat memori:",
                    "     Quarkus atau Micronaut.",
                    "  3. Tim Kotlin yang ingin framework ringan: Ktor.",
                    "  4. Belajar konsep web Java tanpa banyak anotasi: Javalin.",
                    "  5. Merawat Struts, Play, atau Dropwizard: pelajari secukupnya dan",
                    "     siapkan rencana migrasi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Quarkus dan Micronaut sering dipakai untuk layanan yang berjalan di",
                    "Kubernetes atau sebagai fungsi serverless, tempat waktu start dan memori",
                    "langsung jadi biaya. Spring Boot tetap jadi pilihan utama untuk aplikasi",
                    "bisnis yang besar.",
                    "",
                    "Kasus kecil: kantor tempatmu PKL menjalankan aplikasi Struts 2 lama dan",
                    "kamu diminta menilai risikonya.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek versi Struts di pom.xml atau folder lib, lalu bandingkan dengan",
                    "     versi yang masih dirawat di struts.apache.org.",
                    "  2. Cari pengumuman keamanan untuk versi itu dan catat celah yang belum",
                    "     ditambal.",
                    "  3. Usulkan dua langkah: tambal ke versi Struts yang masih dirawat",
                    "     sekarang juga, lalu pindahkan fitur satu per satu ke Spring Boot.",
                    "  4. Mulai migrasi dari fitur baca saja (laporan, pencarian), karena",
                    "     risikonya paling kecil.",
                ],
            },
        ],
    },
    {
        "title": "24. ASP.NET Core Minimal API: Endpoint Pertama",
        "sections": [
            {
                "body": [
                    "ASP.NET Core adalah framework web lintas platform dari Microsoft. Dengan",
                    "satu framework kamu bisa membuat API, situs MVC, halaman Razor, aplikasi",
                    "real-time dengan SignalR, sampai layanan gRPC. Ia jalan di Linux, macOS,",
                    "dan Windows, dan kodenya terbuka dengan lisensi MIT.",
                    "",
                    "Angkanya besar. Di Survei Stack Overflow 2026, ASP.NET Core dipakai",
                    "19,9% responden, tertinggi di antara framework backend di kategori itu.",
                    "Survei JetBrains tentang .NET tahun 2025 mencatat 70% pengembang C#",
                    "memakainya.",
                    "",
                    "Jangan tertukar dengan ASP.NET lama, yang cuma jalan di Windows di atas",
                    ".NET Framework 4.x. Statusnya dibahas di materi peta bab ini.",
                    "Prasyaratnya kurikulum C#: record, LINQ, dan async/await.",
                ],
            },
            {
                "heading": "Bikin dan jalankan",
                "bahasa": "terminal",
                "code": """dotnet new web -n Toko
cd Toko
dotnet watch""",
            },
            {
                "body": [
                    "dotnet new web membuat proyek web paling kosong. dotnet watch",
                    "menjalankannya dan memuat ulang setiap kali berkas disimpan. Isi",
                    "Program.cs bawaannya cuma beberapa baris. Kita ganti dengan API produk",
                    "kecil di bawah ini.",
                ],
            },
            {
                "heading": "Program.cs",
                "bahasa": "csharp",
                "code": """using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<IProdukRepo, ProdukRepoMemori>();

var app = builder.Build();

app.MapGet("/api/produk", (IProdukRepo repo) => repo.Semua());

app.MapGet("/api/produk/{id:int}", (int id, IProdukRepo repo) =>
    repo.Cari(id) is Produk p ? Results.Ok(p) : Results.NotFound());

app.MapPost("/api/produk", (ProdukBaru baru, IProdukRepo repo) =>
{
    if (string.IsNullOrWhiteSpace(baru.Nama))
    {
        return Results.ValidationProblem(new Dictionary<string, string[]>
        {
            ["nama"] = ["Nama wajib diisi."]
        });
    }
    var p = repo.Tambah(baru);
    return Results.Created($"/api/produk/{p.Id}", p);
});

app.Run();

record Produk(int Id, string Nama, int Harga);
record ProdukBaru(string Nama, int Harga);

interface IProdukRepo
{
    IEnumerable<Produk> Semua();
    Produk? Cari(int id);
    Produk Tambah(ProdukBaru baru);
}

class ProdukRepoMemori : IProdukRepo
{
    private readonly List<Produk> _data = [new(1, "Teh Botol", 5000)];

    public IEnumerable<Produk> Semua() => _data;

    public Produk? Cari(int id) => _data.FirstOrDefault(p => p.Id == id);

    public Produk Tambah(ProdukBaru baru)
    {
        var p = new Produk(_data.Count + 1, baru.Nama, baru.Harga);
        _data.Add(p);
        return p;
    }
}""",
            },
            {
                "body": [
                    "Templat resmi menyalakan implicit usings, jadi baris using di atas",
                    "biasanya nggak perlu ditulis. Di sini ditulis supaya kelihatan dari mana",
                    "WebApplication dan Results berasal.",
                    "",
                    "Programnya punya dua tahap. Di tahap builder kamu mendaftarkan layanan",
                    "ke kontainer DI bawaan, misalnya \"kalau ada yang minta IProdukRepo,",
                    "berikan ProdukRepoMemori\". Sesudah Build(), kamu menyusun pipeline dan",
                    "memetakan endpoint. MapGet dan MapPost menerima pola rute dan sebuah",
                    "fungsi.",
                    "",
                    "Yang menarik adalah parameter fungsinya. ASP.NET Core melihat tipe dan",
                    "namanya lalu mengisinya sendiri. int id diambil dari rute ({id:int} juga",
                    "menolak yang bukan angka), IProdukRepo diambil dari kontainer DI, dan",
                    "ProdukBaru dibaca dari body JSON. Ini disebut parameter binding.",
                    "",
                    "Waktu contoh ini dicoba, GET /api/produk/9 dibalas 404. POST dengan nama",
                    "kosong dibalas 400 berformat Problem Details:",
                    "",
                    "  {\"type\": \"https://tools.ietf.org/html/rfc9110#section-15.5.1\",",
                    "   \"title\": \"One or more validation errors occurred.\",",
                    "   \"status\": 400,",
                    "   \"errors\": {\"nama\": [\"Nama wajib diisi.\"]}}",
                    "",
                    "POST yang benar dibalas 201 Created dengan header Location:",
                    "/api/produk/2. Perhatikan nama properti JSON-nya huruf kecil (nama,",
                    "harga) walau di C# ditulis Nama dan Harga; serializer bawaannya memakai",
                    "camelCase.",
                ],
            },
            {
                "heading": "Umur layanan di kontainer DI",
                "body": [
                    "Saat mendaftarkan layanan, kamu memilih berapa lama objeknya hidup:",
                    "",
                    "  - AddSingleton: satu objek untuk seluruh umur aplikasi. Cocok untuk",
                    "    yang tanpa keadaan per pengguna, seperti pengaturan atau cache.",
                    "  - AddScoped: satu objek per permintaan HTTP. DbContext milik EF Core",
                    "    didaftarkan begini.",
                    "  - AddTransient: objek baru setiap kali diminta.",
                    "",
                    "Jebakan: memasukkan layanan scoped ke dalam singleton. Singleton hidup",
                    "selamanya, jadi DbContext di dalamnya ikut hidup selamanya dan dipakai",
                    "bersama banyak permintaan sekaligus. Di mode Development, ASP.NET Core",
                    "menolak susunan itu dengan pesan cannot consume scoped service from",
                    "singleton.",
                ],
            },
            {
                "heading": "Pipeline middleware",
                "body": [
                    "Sebelum sampai ke endpoint, permintaan melewati deretan middleware,",
                    "persis gagasan rantai middleware di bab 01. Urutannya ditentukan urutan",
                    "baris di Program.cs:",
                    "",
                    "  app.UseExceptionHandler(\"/error\");",
                    "  app.UseHttpsRedirection();",
                    "  app.UseCors();",
                    "  app.UseAuthentication();",
                    "  app.UseAuthorization();",
                    "",
                    "  app.Use(async (context, next) =>",
                    "  {",
                    "      var mulai = DateTime.UtcNow;",
                    "      await next(context);",
                    "      var ms = (DateTime.UtcNow - mulai).TotalMilliseconds;",
                    "      app.Logger.LogInformation(\"{Path} {Ms} ms\", context.Request.Path, ms);",
                    "  });",
                    "",
                    "  app.MapGet(\"/api/produk\", ...);",
                    "",
                    "Middleware buatan sendiri ditulis dengan app.Use: kode sebelum await",
                    "next(context) jalan saat permintaan masuk, kode sesudahnya jalan saat",
                    "respons kembali. Kalau next nggak dipanggil, rantainya berhenti di situ.",
                    "",
                    "Urutan itu bukan hiasan. UseAuthentication (mencari tahu siapa",
                    "pemanggilnya) harus sebelum UseAuthorization (memeriksa izinnya). Kalau",
                    "terbalik, pemeriksa izin selalu melihat pengguna anonim.",
                    "UseExceptionHandler ditaruh paling awal supaya bisa menangkap galat dari",
                    "semua yang ada sesudahnya.",
                ],
            },
            {
                "heading": "OpenAPI dan versi",
                "body": [
                    "Sejak .NET 9, templat proyek nggak lagi menyertakan Swashbuckle.",
                    "Penggantinya paket Microsoft.AspNetCore.OpenApi:",
                    "builder.Services.AddOpenApi() lalu app.MapOpenApi() menyajikan dokumen",
                    "di /openapi/v1.json. Halaman uji interaktif seperti Swagger UI atau",
                    "Scalar dipasang terpisah kalau kamu mau.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), versi terbarunya .NET 10 LTS",
                    "dengan ASP.NET Core 10.0.13. .NET merilis versi mayor tiap November, dan",
                    ".NET 10 didukung sampai 14 November 2028. .NET 8 dan .NET 9 berhenti",
                    "didukung pada 10 November 2026, jadi proyek yang masih di sana perlu",
                    "segera di-upgrade.",
                    "",
                    "Ingat juga soal lisensi pustaka populer. MediatR mulai versi 13 dan",
                    "AutoMapper mulai versi 15 berpindah ke lisensi ganda RPL-1.5 atau",
                    "komersial sejak 2025. Tutorial lama sering memasang keduanya seolah",
                    "gratis untuk semua orang. Untuk proyek kantor, cek dulu syaratnya, atau",
                    "pakai versi lama yang masih berlisensi bebas, atau tulis kodenya",
                    "sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "ASP.NET Core banyak dipakai untuk API layanan keuangan, sistem ERP dan",
                    "HR, portal pemerintahan, dan backend game, terutama di organisasi yang",
                    "sudah memakai produk Microsoft.",
                    "",
                    "Kasus kecil: kamu diminta membuat endpoint cek status pesanan untuk",
                    "chatbot layanan pelanggan, tanpa database dulu.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jalankan dotnet new web, lalu tulis record Pesanan dan interface",
                    "     IPesananRepo dengan implementasi di memori.",
                    "  2. Daftarkan repo sebagai singleton dan petakan",
                    "     MapGet(\"/api/pesanan/{kode}\") yang membalas Results.Ok atau",
                    "     Results.NotFound.",
                    "  3. Tambahkan middleware app.Use yang mencatat lama tiap permintaan,",
                    "     supaya kamu tahu kalau chatbot menunggu terlalu lama.",
                    "  4. Pasang AddOpenApi dan MapOpenApi, lalu kirim alamat",
                    "     /openapi/v1.json ke tim chatbot sebagai kontrak.",
                ],
            },
        ],
    },
    {
        "title": "25. ASP.NET Core dengan Controller dan EF Core",
        "sections": [
            {
                "body": [
                    "Minimal API enak untuk layanan kecil. Begitu endpoint-nya puluhan dan",
                    "dikerjakan banyak orang, banyak tim memilih controller: kelas yang",
                    "mengelompokkan endpoint satu sumber daya, dengan rute dan aturan",
                    "validasi ditulis sebagai atribut. Keduanya memakai pipeline, DI, dan",
                    "konfigurasi yang sama, jadi pilihannya soal kerapian, bukan kemampuan.",
                    "",
                    "Untuk database, pasangan bawaannya Entity Framework Core (EF Core), ORM",
                    "resmi .NET. Survei JetBrains tentang .NET tahun 2025 mencatat 42%",
                    "responden memakainya.",
                ],
            },
            {
                "heading": "Entity dan DbContext",
                "bahasa": "csharp",
                "code": """using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

public class Kategori
{
    public int Id { get; set; }
    public string Nama { get; set; } = "";
}

public class Barang
{
    public int Id { get; set; }

    [Required, MaxLength(100)]
    public string Nama { get; set; } = "";

    [Range(1000, int.MaxValue)]
    public int Harga { get; set; }

    public int KategoriId { get; set; }
    public Kategori? Kategori { get; set; }
}

public class TokoDbContext(DbContextOptions<TokoDbContext> options)
    : DbContext(options)
{
    public DbSet<Barang> Barang => Set<Barang>();
    public DbSet<Kategori> Kategori => Set<Kategori>();
}""",
            },
            {
                "body": [
                    "EF Core memakai pendekatan code first: kelas C# biasa dijadikan tabel.",
                    "Properti Id otomatis jadi primary key, KategoriId jadi foreign key, dan",
                    "properti Kategori adalah navigasi ke objek terkait. Atribut seperti",
                    "[Required] dan [Range] dipakai dua kali: untuk bentuk kolom dan untuk",
                    "validasi input. DbContext mewakili satu sesi kerja dengan database, dan",
                    "tiap DbSet mewakili satu tabel.",
                    "",
                    "Daftarkan di Program.cs lalu buat migrasi:",
                    "",
                    "  builder.Services.AddDbContext<TokoDbContext>(o =>",
                    "      o.UseNpgsql(builder.Configuration.GetConnectionString(\"Toko\")));",
                    "  builder.Services.AddControllers();",
                    "  ...",
                    "  app.MapControllers();",
                    "",
                    "  dotnet tool install --global dotnet-ef",
                    "  dotnet ef migrations add Awal",
                    "  dotnet ef database update",
                    "",
                    "UseNpgsql datang dari paket Npgsql.EntityFrameworkCore.PostgreSQL. Untuk",
                    "SQLite pakai Microsoft.EntityFrameworkCore.Sqlite dan UseSqlite.",
                    "AddDbContext mendaftarkan DbContext sebagai layanan scoped, satu per",
                    "permintaan.",
                ],
            },
            {
                "heading": "Controller",
                "bahasa": "csharp",
                "code": """using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

[ApiController]
[Route("api/[controller]")]
public class BarangController(TokoDbContext db) : ControllerBase
{
    [HttpGet]
    public async Task<List<Barang>> Semua() =>
        await db.Barang.Include(b => b.Kategori).AsNoTracking().ToListAsync();

    [HttpGet("{id:int}")]
    public async Task<ActionResult<Barang>> Satu(int id)
    {
        var b = await db.Barang.FindAsync(id);
        return b is null ? NotFound() : b;
    }

    [HttpPost]
    public async Task<ActionResult<Barang>> Tambah(Barang baru)
    {
        db.Barang.Add(baru);
        await db.SaveChangesAsync();
        return CreatedAtAction(nameof(Satu), new { id = baru.Id }, baru);
    }

    [HttpPatch("{id:int}/harga")]
    public async Task<IActionResult> UbahHarga(int id, [FromBody] int hargaBaru)
    {
        var b = await db.Barang.FindAsync(id);
        if (b is null) return NotFound();
        b.Harga = hargaBaru;
        await db.SaveChangesAsync();
        return NoContent();
    }
}""",
            },
            {
                "body": [
                    "[Route(\"api/[controller]\")] mengambil nama kelas tanpa akhiran",
                    "Controller, jadi alamatnya /api/barang. [ApiController] menyalakan",
                    "validasi otomatis. Waktu dicoba, POST dengan harga 500 dibalas 400",
                    "berisi \"Harga\": [\"The field Harga must be between 1000 and 2147483647.\"]",
                    "tanpa method Tambah sempat dipanggil. CreatedAtAction membalas 201 dan",
                    "menulis header Location yang menunjuk ke method Satu.",
                    "",
                    "Include(b => b.Kategori) mengambil kategori dalam kueri yang sama (eager",
                    "loading), cara EF Core menghindari N+1. AsNoTracking memberi tahu EF",
                    "Core bahwa data ini cuma dibaca, jadi ia nggak perlu menyiapkan",
                    "pelacakan perubahan. Lebih hemat untuk endpoint daftar.",
                ],
            },
            {
                "heading": "Change tracker",
                "body": [
                    "Lihat UbahHarga. Nggak ada perintah UPDATE di sana. FindAsync memuat",
                    "barang dan EF Core memotret nilai aslinya. Saat SaveChangesAsync",
                    "dipanggil, ia membandingkan objek dengan potretnya lalu cuma mengirim",
                    "kolom yang berubah. Log SQL waktu contoh ini dicoba:",
                    "",
                    "  UPDATE \"Barang\" SET \"Harga\" = @p0",
                    "  WHERE \"Id\" = @p1",
                    "",
                    "Bagian EF Core yang mengerjakan ini disebut change tracker. Objek baru",
                    "yang di-Add dikirim sebagai INSERT, objek yang di-Remove sebagai DELETE,",
                    "dan semuanya dikirim dalam satu transaksi. Latihan bab ini memintamu",
                    "membuat versi mininya.",
                    "",
                    "Jebakan: lazy loading. Kalau dinyalakan, membaca b.Kategori di dalam",
                    "perulangan memicu satu kueri per barang. Jebakan lain, ekspresi LINQ",
                    "yang nggak bisa diterjemahkan ke SQL. EF Core modern menolaknya dengan",
                    "galat, tapi kode yang memanggil ToList() terlalu awal tetap menarik",
                    "seluruh tabel ke memori sebelum disaring. Pendalaman N+1, migrasi, dan",
                    "transaksi ada di kurikulum Database.",
                ],
            },
            {
                "heading": "Validasi dengan FluentValidation",
                "body": [
                    "DataAnnotations cukup untuk aturan sederhana. Untuk aturan yang lebih",
                    "panjang atau bergantung pada kolom lain, banyak tim memakai",
                    "FluentValidation (versi 12.2.0, lisensi Apache-2.0). Aturannya ditulis",
                    "berantai di kelas terpisah, jadi model tetap bersih:",
                    "",
                    "  public class BarangValidator : AbstractValidator<Barang>",
                    "  {",
                    "      public BarangValidator()",
                    "      {",
                    "          RuleFor(x => x.Nama).NotEmpty().MaximumLength(100);",
                    "          RuleFor(x => x.Harga).GreaterThanOrEqualTo(1000);",
                    "      }",
                    "  }",
                    "",
                    "Padanannya di Java adalah Jakarta Bean Validation yang kamu lihat di bab",
                    "Spring Boot.",
                ],
            },
            {
                "heading": "Kapan Dapper, kapan NHibernate",
                "body": [
                    "Dapper adalah micro-ORM dari tim Stack Overflow (versi 2.1.89, lisensi",
                    "Apache-2.0). Kamu menulis SQL sendiri, Dapper cuma memetakan hasilnya ke",
                    "objek dengan cepat:",
                    "",
                    "  var murah = await conn.QueryAsync<Barang>(",
                    "      \"SELECT Id, Nama, Harga FROM Barang WHERE Harga < @Batas\",",
                    "      new { Batas = 20000 });",
                    "",
                    "@Batas diisi sebagai parameter, jadi tetap aman dari SQL injection.",
                    "Pilih Dapper untuk laporan dengan SQL rumit atau jalur yang harus",
                    "secepat mungkin. Banyak proyek memakai keduanya: EF Core untuk CRUD",
                    "harian, Dapper untuk kueri berat.",
                    "",
                    "NHibernate adalah port Hibernate ke .NET dan ORM utama sebelum EF Core",
                    "dominan. Versi 5.7.0 masih dirilis dengan lisensi LGPL-2.1, tapi",
                    "pemakainya menurun. Kamu akan menemuinya di aplikasi .NET Framework",
                    "lama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pasangan controller dan EF Core adalah bentuk paling umum aplikasi",
                    "ASP.NET Core di perusahaan: sistem gudang, aplikasi klaim asuransi, dan",
                    "portal karyawan.",
                    "",
                    "Kasus kecil: laporan penjualan bulanan di aplikasi kantor makin lambat",
                    "karena kueri LINQ-nya menggabungkan lima tabel dan menghasilkan SQL yang",
                    "susah dibaca.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Aktifkan log SQL EF Core di lingkungan pengembangan dan salin SQL",
                    "     yang dihasilkan untuk laporan itu.",
                    "  2. Tulis ulang kuerinya sebagai SQL biasa yang kamu pahami, lalu uji",
                    "     langsung di database sampai hasilnya sama.",
                    "  3. Pindahkan kueri laporan itu ke Dapper dengan",
                    "     QueryAsync<BarisLaporan>, dan biarkan CRUD lain tetap memakai EF",
                    "     Core.",
                    "  4. Bandingkan waktu respons sebelum dan sesudah, dan catat alasannya",
                    "     di kode supaya rekan setim nggak mengembalikannya ke LINQ.",
                ],
            },
        ],
    },
    {
        "title": "26. Peta Ekosistem .NET di Luar ASP.NET Core",
        "sections": [
            {
                "body": [
                    "Di sekitar ASP.NET Core ada beberapa nama yang sering muncul di lowongan",
                    "dan dokumentasi Microsoft. Sebagian bagian dari ASP.NET Core sendiri,",
                    "sebagian proyek terpisah, dan satu adalah generasi lama yang masih",
                    "banyak dirawat. Versi di bawah per Oktober 2026.",
                ],
            },
            {
                "heading": "Tabel perbandingan",
                "bahasa": "teks",
                "code": """Nama                    Versi                 Gunanya                    Status
ASP.NET (.NET Fx 4.x)   .NET Framework 4.8.1  web lama, Windows + IIS    pemeliharaan saja
Blazor                  bagian ASP.NET Core   UI web dengan C#           aktif
Aspire                  13.6.1                susun dan pantau layanan   aktif, tumbuh
Orleans                 10.4.0                virtual actor terdistribusi aktif
YARP                    2.3.0                 pustaka reverse proxy      aktif
Ocelot                  25.0.2                API gateway via JSON       aktif""",
            },
            {
                "heading": "ASP.NET lama: rawat, jangan mulai",
                "body": [
                    "ASP.NET di atas .NET Framework 4.x mencakup Web Forms, MVC 5, dan Web",
                    "API 2. Ia cuma jalan di Windows dengan web server Microsoft, dan .NET",
                    "Framework 4.8.1 (2022) adalah rilis terakhirnya; sekarang statusnya",
                    "pemeliharaan saja. Walau begitu, di Survei Stack Overflow 2026 masih",
                    "13,9% responden memakainya. Artinya banyak aplikasi kantor yang menunggu",
                    "dimigrasi, dan orang yang paham keduanya dicari. Untuk proyek baru,",
                    "selalu pilih ASP.NET Core.",
                ],
            },
            {
                "heading": "Blazor",
                "bahasa": "razor",
                "code": """@page "/hitung"
@rendermode InteractiveServer

<h1>Hitungan: @jumlah</h1>
<button @onclick="Tambah">Tambah</button>

@code {
    private int jumlah = 0;
    private void Tambah() => jumlah++;
}""",
            },
            {
                "body": [
                    "Blazor membuat UI web interaktif dengan C# alih-alih JavaScript.",
                    "Komponennya bisa jalan di server, dengan klik dikirim lewat koneksi",
                    "SignalR, atau di browser lewat WebAssembly. @rendermode menentukan",
                    "pilihan itu per komponen. Di Survei Stack Overflow 2026 pemakainya 6,7%.",
                    "Ia setengah frontend, jadi menarik untuk tim yang semuanya ahli C#.",
                ],
            },
            {
                "heading": "Aspire dan Orleans",
                "body": [
                    "Aspire (dulu .NET Aspire) membantu menyusun aplikasi yang terdiri dari",
                    "beberapa bagian, misalnya API, database, dan cache, dari satu proyek",
                    "AppHost. Satu perintah menjalankan semuanya di laptop lengkap dengan",
                    "dasbor log dan metrik. Nomor versinya melompat ke 13 bersamaan dengan",
                    "pergantian nama, dan dokumentasinya kini di aspire.dev. Survei JetBrains",
                    "tentang .NET 2025 mencatat pemakainya naik dari 6% ke 9%.",
                    "",
                    "Orleans adalah framework virtual actor dari Microsoft. Tiap \"aktor\"",
                    "(disebut grain) mewakili satu benda, misalnya satu pemain game atau satu",
                    "keranjang belanja, dan Orleans yang mengatur di server mana aktor itu",
                    "hidup. Ini topik mahir untuk sistem berskala besar; cukup tahu namanya",
                    "dulu.",
                ],
            },
            {
                "heading": "YARP dan Ocelot",
                "bahasa": "json",
                "code": """{
  "ReverseProxy": {
    "Routes": {
      "rute-api": {
        "ClusterId": "kluster-api",
        "Match": { "Path": "/api/{**sisa}" }
      }
    },
    "Clusters": {
      "kluster-api": {
        "Destinations": {
          "satu": { "Address": "http://localhost:5001/" }
        }
      }
    }
  }
}""",
            },
            {
                "body": [
                    "Yet Another Reverse Proxy (disingkat Yarp) adalah pustaka Microsoft",
                    "untuk membangun gateway atau reverse proxy sendiri di atas ASP.NET Core.",
                    "Konfigurasi di atas meneruskan semua permintaan /api/... ke layanan di",
                    "port 5001. Di Program.cs cukup AddReverseProxy().LoadFromConfig(...) dan",
                    "MapReverseProxy(). Karena ia aplikasi ASP.NET Core biasa, kamu bisa",
                    "menambahkan middleware sendiri, misalnya pemeriksa token, sebelum",
                    "permintaan diteruskan.",
                    "",
                    "Ocelot adalah API gateway open source untuk .NET yang diatur lewat",
                    "berkas JSON berisi rute naik (upstream) dan rute turun (downstream).",
                    "Keduanya menyelesaikan masalah yang sama. Yarp lebih fleksibel dan",
                    "dirawat Microsoft, Ocelot lebih cepat dipasang untuk kasus standar.",
                    "Gateway di cloud dibahas di kurikulum DevOps.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak kantor pemerintahan dan perusahaan masih menjalankan aplikasi",
                    "ASP.NET Web Forms atau MVC 5 di server Windows, dan migrasi ke ASP.NET",
                    "Core jadi pekerjaan rutin tim .NET.",
                    "",
                    "Kasus kecil: aplikasi absensi MVC 5 di kantormu harus pindah ke ASP.NET",
                    "Core tanpa mematikan layanan berhari-hari.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang aplikasi ASP.NET Core baru berisi Yarp di depan aplikasi",
                    "     lama, dan teruskan semua rute ke aplikasi lama dulu.",
                    "  2. Tulis ulang satu fitur, misalnya rekap bulanan, di ASP.NET Core,",
                    "     lalu ubah rute /rekap supaya ditangani aplikasi baru.",
                    "  3. Ulangi per fitur sambil memantau galat, sampai nggak ada lagi rute",
                    "     yang diteruskan ke aplikasi lama.",
                    "  4. Matikan aplikasi MVC 5 dan server Windows-nya setelah lalu",
                    "     lintasnya nol selama beberapa minggu.",
                ],
            },
        ],
    },
    {
        "title": "27. Laravel: Rute, Controller, dan Blade",
        "sections": [
            {
                "body": [
                    "Kalau kamu mencari lowongan web developer PHP di Indonesia, Laravel",
                    "hampir selalu disebut. Ia framework PHP paling populer: survei JetBrains",
                    "tentang PHP tahun 2025 mencatat 64% pengembang PHP memakainya, jauh di",
                    "atas yang lain. Di Survei Stack Overflow 2026 angkanya 7,6% dari seluruh",
                    "responden.",
                    "",
                    "Laravel datang dengan banyak hal siap pakai: routing, ORM Eloquent,",
                    "template Blade, antrean tugas, autentikasi, dan Artisan, alat baris",
                    "perintah yang membuatkan berkas untukmu.",
                    "",
                    "Di sekelilingnya ada alat resmi. Sail dan Herd untuk lingkungan",
                    "pengembangan, Forge dan Laravel Cloud untuk deploy, Octane untuk server",
                    "yang lebih cepat, serta Telescope dan Pulse untuk memantau aplikasi.",
                    "",
                    "Prasyaratnya kurikulum PHP: class, namespace, dan Composer (pengelola",
                    "paket PHP).",
                ],
            },
            {
                "heading": "Bikin proyek",
                "bahasa": "terminal",
                "code": """composer create-project laravel/laravel toko
cd toko
php artisan serve
php artisan make:model Produk -mc
php artisan route:list""",
            },
            {
                "body": [
                    "php artisan serve menyalakan server pengembangan di",
                    "http://127.0.0.1:8000. make:model Produk -mc membuat model Produk",
                    "sekaligus migrasi (-m) dan controller (-c). route:list mencetak semua",
                    "rute yang terdaftar, berguna saat kamu bingung kenapa sebuah alamat",
                    "membalas 404.",
                    "",
                    "Folder yang paling sering kamu buka: routes untuk peta alamat,",
                    "app/Http/Controllers untuk controller, app/Models untuk model,",
                    "database/migrations untuk migrasi, dan resources/views untuk template",
                    "Blade. Sejak Laravel 11, kerangkanya dirampingkan; pendaftaran",
                    "middleware dan penanganan galat pindah ke bootstrap/app.php.",
                ],
            },
            {
                "heading": "Rute",
                "bahasa": "php",
                "code": "use App\\Http\\Controllers\\ProdukController;\nuse Illuminate\\Support\\Facades\\Route;\n\nRoute::get('/', fn () => view('beranda'));\n\nRoute::get('/produk', [ProdukController::class, 'index'])\n    ->name('produk.index');\nRoute::get('/produk/{produk}', [ProdukController::class, 'show'])\n    ->name('produk.show');\n\nRoute::middleware('auth')->group(function () {\n    Route::get('/dasbor', fn () => view('dasbor'))->name('dasbor');\n});",
            },
            {
                "body": [
                    "Isi itu berada di routes/web.php (di berkasnya, baris pertama tetap",
                    "<?php). Tiap rute menunjuk ke fungsi pendek atau ke method controller.",
                    "->name() memberi nama rute, jadi di template kamu menulis",
                    "route('produk.show', $p) alih-alih mengetik alamat manual; kalau",
                    "alamatnya berubah, tautan ikut berubah sendiri.",
                    "",
                    "Route::middleware('auth')->group(...) memasang middleware ke sekelompok",
                    "rute. Middleware auth mengalihkan tamu ke halaman login sebelum",
                    "controller dipanggil, persis rantai middleware di bab 01. Sintaks",
                    "Route:: itu disebut facade: cara singkat memanggil layanan dari",
                    "kontainer Laravel. Enak ditulis, tapi menyembunyikan dependensinya, jadi",
                    "pemula sering nggak sadar bahwa di baliknya ada dependency injection.",
                ],
            },
            {
                "heading": "Controller",
                "bahasa": "php",
                "code": "namespace App\\Http\\Controllers;\n\nuse App\\Models\\Produk;\n\nclass ProdukController extends Controller\n{\n    public function index()\n    {\n        $produk = Produk::with('kategori')\n            ->where('stok', '>', 0)\n            ->orderBy('nama')\n            ->paginate(20);\n\n        return view('produk.index', ['produk' => $produk]);\n    }\n\n    public function show(Produk $produk)\n    {\n        return view('produk.show', compact('produk'));\n    }\n}",
            },
            {
                "body": [
                    "Perhatikan method show. Parameternya bertipe Produk dan namanya sama",
                    "dengan {produk} di rute. Laravel mencari baris dengan id itu sendiri,",
                    "dan membalas 404 kalau nggak ada. Fitur ini disebut route model binding.",
                    "",
                    "with('kategori') mengambil kategori semua produk dalam satu kueri",
                    "tambahan, bukan satu kueri per produk. paginate(20) membagi hasil per 20",
                    "baris dan membaca nomor halaman dari ?page= di URL.",
                ],
            },
            {
                "heading": "Blade",
                "bahasa": "blade",
                "code": """@extends('layouts.app')

@section('isi')
  <h1>Produk</h1>
  <ul>
    @forelse ($produk as $p)
      <li>
        <a href="{{ route('produk.show', $p) }}">{{ $p->nama }}</a>
        ({{ $p->kategori->nama }})
        Rp{{ number_format($p->harga, 0, ',', '.') }}
      </li>
    @empty
      <li>Belum ada produk.</li>
    @endforelse
  </ul>

  {{ $produk->links() }}
@endsection""",
            },
            {
                "body": [
                    "Simpan di resources/views/produk/index.blade.php; nama view produk.index",
                    "menunjuk ke berkas itu. @extends memakai tata letak induk, @section",
                    "mengisi bagiannya. {{ ... }} mencetak nilai yang sudah di-escape, jadi",
                    "aman dari XSS. Ada juga {!! ... !!} yang mencetak apa adanya. Jebakan:",
                    "memakai {!! !!} untuk teks dari pengguna sama dengan membuka pintu XSS.",
                    "Pakai hanya untuk HTML yang kamu buat sendiri.",
                    "",
                    "number_format mengubah 18000 jadi 18.000 dengan titik sebagai pemisah",
                    "ribuan, dan $produk->links() mencetak tombol halaman dari paginate.",
                ],
            },
            {
                "heading": "Satu baris untuk tujuh rute",
                "body": [
                    "Halaman CRUD biasanya butuh tujuh rute yang polanya selalu sama. Laravel",
                    "menyingkatnya jadi satu baris:",
                    "",
                    "  Route::resource('produk', ProdukController::class);",
                    "",
                    "  GET        /produk                 index    daftar",
                    "  GET        /produk/create          create   form tambah",
                    "  POST       /produk                 store    simpan baru",
                    "  GET        /produk/{produk}        show     detail",
                    "  GET        /produk/{produk}/edit   edit     form ubah",
                    "  PUT/PATCH  /produk/{produk}        update   simpan ubahan",
                    "  DELETE     /produk/{produk}        destroy  hapus",
                    "",
                    "php artisan make:controller ProdukController --resource membuatkan",
                    "ketujuh method kosongnya. Untuk API yang nggak butuh halaman form, pakai",
                    "Route::apiResource, yang membuang create dan edit.",
                    "",
                    "Jebakan: form HTML yang mengirim POST, PUT, atau DELETE ke rute web",
                    "wajib memuat @csrf di dalam tag form. Tanpa itu Laravel menolak",
                    "permintaannya dengan status 419 Page Expired. Token itu melindungi dari",
                    "CSRF, yaitu situs lain yang mengirim form atas nama penggunamu tanpa ia",
                    "sadari; detailnya ada di bab Autentikasi.",
                ],
            },
            {
                "heading": "Status dan versi",
                "body": [
                    "Laravel merilis versi mayor setahun sekali. Saat materi ini ditulis",
                    "(Oktober 2026), versi terbarunya 13.37.0, versi untuk tahun 2026,",
                    "berlisensi MIT. Laravel memakai banyak komponen Symfony di dalamnya,",
                    "jadi ilmu salah satunya membantu memahami yang lain.",
                    "",
                    "Untuk aplikasi yang butuh halaman login, registrasi, dan dasbor siap",
                    "pakai, Laravel menyediakan starter kit resmi. Banyak proyek lokal juga",
                    "memakai Livewire atau Inertia supaya halaman terasa interaktif tanpa",
                    "memisahkan frontend; itu dibahas dari sisi frontend di kurikulum",
                    "Frontend.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laravel dipakai di banyak sistem informasi sekolah, aplikasi kasir dan",
                    "toko daring UMKM, portal desa, sampai sistem internal perusahaan, karena",
                    "hosting PHP murah dan pengembang Laravel mudah dicari.",
                    "",
                    "Kasus kecil: kamu PKL di sebuah percetakan yang ingin menampilkan daftar",
                    "layanan dan harga di web, dengan halaman dasbor yang cuma boleh dibuka",
                    "karyawan.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat proyek dengan composer create-project, lalu make:model Layanan",
                    "     -mc.",
                    "  2. Tulis rute /layanan ke LayananController@index dan tampilkan",
                    "     datanya dengan Blade memakai @forelse.",
                    "  3. Bungkus rute /dasbor dengan Route::middleware('auth') supaya tamu",
                    "     dialihkan ke login.",
                    "  4. Jalankan php artisan route:list untuk memastikan semua rute dan",
                    "     middleware-nya sesuai rencana.",
                ],
            },
        ],
    },
    {
        "title": "28. Laravel dengan Eloquent, Validasi, dan Sanctum",
        "sections": [
            {
                "body": [
                    "Di bawah Eloquent dan semua ORM PHP ada PDO (PHP Data Objects),",
                    "antarmuka database bawaan PHP. Melihatnya sekali membantu memahami apa",
                    "yang dikerjakan Eloquent untukmu, terutama soal prepared statement.",
                    "Contoh ini memakai SQLite di memori, jadi bisa langsung dijalankan.",
                ],
            },
            {
                "heading": "PDO polos",
                "bahasa": "php",
                "code": """<?php
$db = new PDO('sqlite::memory:');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, harga INTEGER)');

$tambah = $db->prepare('INSERT INTO produk (nama, harga) VALUES (?, ?)');
foreach ([['Teh Botol', 5000], ['Kopi Susu', 18000], ['Roti', 12000]] as $baris) {
    $tambah->execute($baris);
}

$cari = $db->prepare('SELECT nama, harga FROM produk WHERE harga < :batas ORDER BY harga');
$cari->execute(['batas' => 15000]);
foreach ($cari->fetchAll(PDO::FETCH_ASSOC) as $p) {
    echo $p['nama'] . ': ' . $p['harga'] . PHP_EOL;
}

$jahat = "' OR '1'='1";
$cek = $db->prepare('SELECT COUNT(*) FROM produk WHERE nama = ?');
$cek->execute([$jahat]);
echo 'cocok untuk input jahat: ' . $cek->fetchColumn() . PHP_EOL;""",
            },
            {
                "body": [
                    "Keluaran:",
                    "",
                    "  Teh Botol: 5000",
                    "  Roti: 12000",
                    "  cocok untuk input jahat: 0",
                    "",
                    "prepare membuat perintah dengan tempat kosong (? atau :batas), dan",
                    "execute mengisinya. Nilainya dikirim terpisah dari teks SQL, jadi input",
                    "jahat ' OR '1'='1 cuma dianggap nama produk yang aneh dan nggak cocok",
                    "dengan apa pun. Kalau nilai itu disambung langsung ke string SQL,",
                    "kuerinya berubah arti dan semua baris ikut terbaca. Eloquent selalu",
                    "memakai prepared statement di belakang layar.",
                ],
            },
            {
                "heading": "Migrasi dan model",
                "bahasa": "php",
                "code": "use Illuminate\\Database\\Migrations\\Migration;\nuse Illuminate\\Database\\Schema\\Blueprint;\nuse Illuminate\\Support\\Facades\\Schema;\n\nreturn new class extends Migration\n{\n    public function up(): void\n    {\n        Schema::create('produk', function (Blueprint $table) {\n            $table->id();\n            $table->foreignId('kategori_id')->constrained('kategori');\n            $table->string('nama', 100);\n            $table->unsignedInteger('harga');\n            $table->unsignedInteger('stok')->default(0);\n            $table->timestamps();\n        });\n    }\n\n    public function down(): void\n    {\n        Schema::dropIfExists('produk');\n    }\n};",
            },
            {
                "body": [
                    "up membuat tabel, down membatalkannya. timestamps() menambah kolom",
                    "created_at dan updated_at yang diisi Eloquent otomatis. Jalankan dengan",
                    "php artisan migrate. Modelnya:",
                    "",
                    "  namespace App\\Models;",
                    "",
                    "  use Illuminate\\Database\\Eloquent\\Model;",
                    "  use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;",
                    "",
                    "  class Produk extends Model",
                    "  {",
                    "      protected $table = 'produk';",
                    "      protected $fillable = ['nama', 'harga', 'stok', 'kategori_id'];",
                    "",
                    "      protected function casts(): array",
                    "      {",
                    "          return ['harga' => 'integer', 'stok' => 'integer'];",
                    "      }",
                    "",
                    "      public function kategori(): BelongsTo",
                    "      {",
                    "          return $this->belongsTo(Kategori::class);",
                    "      }",
                    "",
                    "      public function scopeTersedia($query)",
                    "      {",
                    "          return $query->where('stok', '>', 0);",
                    "      }",
                    "  }",
                    "",
                    "Jebakan: Laravel menebak nama tabel dari nama model dengan aturan jamak",
                    "bahasa Inggris, jadi model Produk dicari di tabel produks. Karena tabel",
                    "kita bernama produk, baris $table = 'produk' wajib ada.",
                    "",
                    "$fillable mendaftar kolom yang boleh diisi massal lewat",
                    "Produk::create($data). Tanpa daftar ini, pengguna nakal bisa mengirim",
                    "kolom tambahan seperti is_admin=1 di form dan ikut tersimpan. Kategori",
                    "punya pasangan relasinya: return $this->hasMany(Produk::class).",
                ],
            },
            {
                "heading": "Membaca dan menulis dengan Eloquent",
                "body": [
                    "  $p = Produk::find(1);",
                    "  $p->harga = 5500;",
                    "  $p->save();                       // UPDATE produk SET harga = ...",
                    "",
                    "  $murah = Produk::tersedia()->where('harga', '<', 10000)->get();",
                    "  $semua = Produk::with('kategori')->get();   // 2 kueri, bukan N+1",
                    "  $kategori = Kategori::find(1);",
                    "  $kategori->produk;                // semua produk kategori 1",
                    "",
                    "Eloquent berpola Active Record seperti Django ORM: objek model sendiri",
                    "yang tahu cara menyimpan dirinya. Ia juga mencatat kolom mana yang",
                    "berubah, jadi save() cuma mengirim kolom itu. scopeTersedia dipanggil",
                    "sebagai tersedia(), cara rapi memberi nama ke syarat yang sering",
                    "dipakai.",
                    "",
                    "Masalah N+1 juga ada di sini. Tanpa with('kategori'), perulangan yang",
                    "membaca $p->kategori->nama memicu satu kueri per produk. Kamu bisa",
                    "menyuruh Laravel menolak lazy loading saat pengembangan dengan",
                    "Model::preventLazyLoading(), supaya kesalahan ini ketahuan cepat.",
                    "Pendalamannya ada di kurikulum Database.",
                ],
            },
            {
                "heading": "Validasi dengan Form Request",
                "bahasa": "php",
                "code": "namespace App\\Http\\Requests;\n\nuse Illuminate\\Foundation\\Http\\FormRequest;\n\nclass SimpanProdukRequest extends FormRequest\n{\n    public function authorize(): bool\n    {\n        return true;\n    }\n\n    public function rules(): array\n    {\n        return [\n            'nama' => ['required', 'string', 'max:100'],\n            'harga' => ['required', 'integer', 'min:1000'],\n            'kategori_id' => ['required', 'exists:kategori,id'],\n        ];\n    }\n}",
            },
            {
                "body": [
                    "Buat dengan php artisan make:request SimpanProdukRequest. Cukup tulis",
                    "tipenya di parameter method controller, dan Laravel memvalidasi sebelum",
                    "method-nya dipanggil:",
                    "",
                    "  public function store(SimpanProdukRequest $request)",
                    "  {",
                    "      $produk = Produk::create($request->validated());",
                    "      return response()->json($produk, 201);",
                    "  }",
                    "",
                    "Untuk permintaan JSON yang gagal validasi, Laravel membalas 422 berisi",
                    "message dan errors per kolom. Untuk form HTML, ia mengalihkan kembali ke",
                    "halaman form beserta pesan galatnya. Aturan exists:kategori,id memeriksa",
                    "id kategori memang ada di tabel. $request->validated() cuma berisi kolom",
                    "yang lolos aturan, jadi aman dipakai untuk create.",
                ],
            },
            {
                "heading": "Membentuk JSON dengan API Resource",
                "body": [
                    "Mengembalikan model langsung sebagai JSON memang bisa, tapi semua kolom",
                    "ikut keluar, termasuk yang nggak perlu dilihat klien. API Resource",
                    "adalah kelas kecil yang menentukan bentuk JSON-nya:",
                    "",
                    "  class ProdukResource extends JsonResource",
                    "  {",
                    "      public function toArray(Request $request): array",
                    "      {",
                    "          return [",
                    "              'id' => $this->id,",
                    "              'nama' => $this->nama,",
                    "              'harga' => $this->harga,",
                    "              'kategori' => $this->whenLoaded('kategori',",
                    "                  fn () => $this->kategori->nama),",
                    "          ];",
                    "      }",
                    "  }",
                    "",
                    "  return ProdukResource::collection(",
                    "      Produk::with('kategori')->paginate(20));",
                    "",
                    "whenLoaded cuma mengisi kategori kalau relasinya sudah diambil dengan",
                    "with(), jadi resource ini nggak pernah memicu N+1 tanpa kamu sadari.",
                    "Koleksi yang dipaginasi dibungkus kunci data, ditambah links dan meta",
                    "berisi nomor halaman dan total, bentuk yang mudah dibaca aplikasi",
                    "seluler. Buat dengan php artisan make:resource ProdukResource.",
                ],
            },
            {
                "heading": "Token API dengan Sanctum",
                "body": [
                    "Laravel punya dua paket resmi untuk autentikasi API. Sanctum memberi",
                    "token API sederhana untuk aplikasi seluler atau skrip, dan autentikasi",
                    "berbasis cookie untuk SPA di domain yang sama. Passport adalah server",
                    "OAuth2 lengkap, dibutuhkan kalau aplikasi pihak ketiga harus meminta",
                    "izin atas nama penggunamu. Dokumentasi Laravel menyarankan Sanctum",
                    "kecuali kamu memang butuh OAuth2.",
                    "",
                    "php artisan install:api memasang Sanctum dan membuat routes/api.php.",
                    "Lalu:",
                    "",
                    "  // routes/api.php",
                    "  Route::get('/produk', [Api\\ProdukController::class, 'index']);",
                    "  Route::middleware('auth:sanctum')->group(function () {",
                    "      Route::post('/produk', [Api\\ProdukController::class, 'store']);",
                    "  });",
                    "",
                    "  // saat login berhasil (model User memakai trait HasApiTokens)",
                    "  $token = $user->createToken('aplikasi-kasir')->plainTextToken;",
                    "",
                    "Klien menyimpan token itu dan mengirimkannya di header Authorization:",
                    "Bearer <token>. Sanctum menyimpan token dalam bentuk hash di tabel",
                    "personal_access_tokens, jadi kalau database bocor, token aslinya nggak",
                    "ikut terbaca. Konsep token bearer dibahas lebih lengkap di bab",
                    "Autentikasi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kombinasi Eloquent, Form Request, dan Sanctum adalah bentuk umum backend",
                    "Laravel untuk aplikasi seluler: aplikasi ojek lokal, aplikasi absensi,",
                    "dan aplikasi pemesanan katering.",
                    "",
                    "Kasus kecil: aplikasi kasir Android butuh API untuk menambah produk,",
                    "tapi cuma akun kasir yang sudah login yang boleh menambah.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jalankan php artisan install:api, lalu tambahkan trait HasApiTokens",
                    "     ke model User.",
                    "  2. Buat endpoint login yang memeriksa kata sandi lalu mengembalikan",
                    "     createToken('kasir')->plainTextToken.",
                    "  3. Buat SimpanProdukRequest dengan aturan nama, harga, dan",
                    "     kategori_id, lalu pakai di method store.",
                    "  4. Lindungi POST /api/produk dengan auth:sanctum, dan uji: tanpa token",
                    "     harus 401, data salah harus 422, data benar harus 201.",
                ],
            },
        ],
    },
    {
        "title": "29. Ruby on Rails: Konvensi, Generator, dan MVC",
        "sections": [
            {
                "body": [
                    "Ruby on Rails, atau cukup Rails, adalah framework web full-stack untuk",
                    "bahasa Ruby. Ia mempopulerkan prinsip convention over configuration:",
                    "kalau kamu mengikuti kebiasaan penamaan yang disepakati, Rails menebak",
                    "sisanya dan kamu nggak perlu menulis berkas pengaturan. Banyak framework",
                    "sesudahnya meniru gagasan ini, termasuk Laravel yang kamu lihat di bab",
                    "sebelumnya.",
                    "",
                    "Di Survei Stack Overflow 2026 Rails dipakai 5,7% responden, dan separuh",
                    "pemakainya ingin terus memakainya. Angkanya lebih kecil daripada Laravel",
                    "atau Django, tapi Rails masih dipakai banyak perusahaan rintisan dan",
                    "produk SaaS yang sudah berumur.",
                    "",
                    "Prasyaratnya kurikulum Ruby, terutama blok (do ... end), simbol (:nama),",
                    "dan modul. Rails banyak memakai metaprogramming, yaitu kode yang membuat",
                    "method lain saat program jalan. Tanpa dasar Ruby, semua itu terasa",
                    "seperti sulap.",
                ],
            },
            {
                "heading": "Bikin aplikasi dengan generator",
                "bahasa": "terminal",
                "code": """gem install rails
rails new toko --database=postgresql
cd toko
bin/rails generate scaffold Produk nama:string harga:integer stok:integer
bin/rails db:migrate
bin/rails server
bin/rails routes""",
            },
            {
                "body": [
                    "rails new membuat kerangka lengkap. generate scaffold membuat sekaligus",
                    "model, migrasi, controller berisi tujuh aksi, view untuk tiap aksi,",
                    "rute, dan tes. Scaffold bagus untuk melihat bentuk aplikasi Rails yang",
                    "utuh; di proyek nyata orang lebih sering memakai generator yang lebih",
                    "kecil seperti generate model dan generate controller.",
                    "",
                    "Jebakan untuk penamaan berbahasa Indonesia: Rails membentuk nama jamak",
                    "dengan aturan bahasa Inggris. Model Produk akan disimpan di tabel",
                    "produks dan rutenya jadi /produks. Kalau mau tetap produk, daftarkan",
                    "katanya sebagai kata yang nggak punya bentuk jamak di",
                    "config/initializers/inflections.rb sebelum menjalankan generator:",
                ],
            },
            {
                "heading": "Aturan kata",
                "bahasa": "ruby",
                "code": """ActiveSupport::Inflector.inflections(:en) do |inflect|
  inflect.uncountable %w[produk kategori]
end
...""",
            },
            {
                "body": [
                    "Sesudah itu tabelnya bernama produk dan alamatnya /produk. Satu efek",
                    "sampingnya: karena bentuk tunggal dan jamaknya sama, helper untuk daftar",
                    "produk bernama produk_index_path, sedangkan produk_path(@produk)",
                    "menunjuk ke satu produk.",
                    "",
                    "Struktur folder Rails mengikuti pola MVC. Model di app/models,",
                    "controller di app/controllers, view di app/views, dan rute di",
                    "config/routes.rb. Migrasi tinggal di db/migrate.",
                ],
            },
            {
                "heading": "Rute dan controller",
                "bahasa": "ruby",
                "code": """# config/routes.rb
Rails.application.routes.draw do
  resources :produk
  root "produk#index"
end

# app/controllers/produk_controller.rb
class ProdukController < ApplicationController
  before_action :set_produk, only: %i[show edit update destroy]

  def index
    @produk = Produk.includes(:kategori).where("stok > 0").order(:nama)
  end

  def show
  end

  def create
    @produk = Produk.new(produk_params)
    if @produk.save
      redirect_to @produk, notice: "Produk tersimpan."
    else
      render :new, status: 422
    end
  end

  ...

  private

  def set_produk
    @produk = Produk.find(params[:id])
  end

  def produk_params
    params.expect(produk: [:nama, :harga, :stok, :kategori_id])
  end
end""",
            },
            {
                "body": [
                    "Satu baris resources :produk membuat tujuh rute CRUD sekaligus;",
                    "daftarnya ada di materi berikutnya. Rails menghubungkan rute ke",
                    "controller lewat nama: produk#index berarti method index di",
                    "ProdukController. Variabel berawalan @ otomatis bisa dibaca view, jadi",
                    "index nggak perlu memanggil render. Rails mencari",
                    "app/views/produk/index.html.erb sendiri.",
                    "",
                    "before_action menjalankan set_produk sebelum aksi tertentu, mirip",
                    "middleware tapi per controller. Produk.find membalas 404 kalau id-nya",
                    "nggak ada. params.expect, cara baru sejak Rails 8, cuma meloloskan kolom",
                    "yang disebut, jadi pengguna nggak bisa menyelipkan kolom lain lewat",
                    "form. Di Rails versi lama kamu akan melihat",
                    "params.require(:produk).permit(...) untuk tujuan yang sama.",
                ],
            },
            {
                "heading": "View dengan ERB",
                "bahasa": "erb",
                "code": """<h1>Produk</h1>
<ul>
  <% @produk.each do |p| %>
    <li>
      <%= link_to p.nama, p %>
      (<%= p.kategori.nama %>) Rp<%= p.harga %>
    </li>
  <% end %>
</ul>
<%= link_to "Tambah produk", new_produk_path %>""",
            },
            {
                "body": [
                    "Template Rails memakai Embedded Ruby. <% ... %> menjalankan kode tanpa",
                    "mencetak, <%= ... %> mencetak hasilnya dan otomatis meng-escape HTML.",
                    "link_to p.nama, p membuat tautan ke halaman produk itu, karena Rails",
                    "tahu alamat sebuah objek dari nama kelasnya. Lagi-lagi konvensi.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), versi terbarunya Rails 8.1.4,",
                    "berlisensi MIT. Rails 8 membawa banyak perubahan yang dibahas di materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Satu nama, banyak sambungan",
                "body": [
                    "Coba perhatikan berapa banyak hal yang tersambung hanya karena satu kata",
                    "produk:",
                    "",
                    "  tabel database     produk",
                    "  kelas model        Produk          app/models/produk.rb",
                    "  controller         ProdukController",
                    "  folder view        app/views/produk/",
                    "  rute               resources :produk",
                    "  helper alamat      produk_path(@produk), new_produk_path",
                    "",
                    "Nggak ada satu pun berkas pengaturan yang menghubungkan semua itu. Kalau",
                    "kamu memberi nama yang menyimpang, misalnya tabelnya barang padahal",
                    "modelnya Produk, kamu harus memberi tahu Rails sendiri dengan",
                    "self.table_name = \"barang\" di model. Bisa, tapi setiap penyimpangan",
                    "adalah satu hal lagi yang harus diingat rekan setimmu.",
                    "",
                    "Untuk bagian tampilan, Rails sejak versi 7 memakai Hotwire (Turbo dan",
                    "Stimulus) sebagai bawaan: halaman tetap dibuat di server, tapi bagian",
                    "yang berubah dikirim ulang tanpa memuat seluruh halaman. Jadi aplikasi",
                    "Rails bisa terasa interaktif tanpa framework JavaScript besar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rails dipakai di banyak produk SaaS, toko daring, dan platform komunitas",
                    "yang dibangun tim kecil, karena generator dan konvensinya membuat fitur",
                    "CRUD jadi dalam hitungan jam.",
                    "",
                    "Kasus kecil: seorang pemilik kursus musik ingin aplikasi pendaftaran",
                    "murid sederhana minggu ini, dengan daftar murid, form tambah, dan",
                    "halaman detail.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Daftarkan kata murid sebagai uncountable di inflections.rb supaya",
                    "     tabelnya bernama murid.",
                    "  2. Jalankan bin/rails generate scaffold Murid nama:string",
                    "     alat_musik:string telepon:string, lalu bin/rails db:migrate.",
                    "  3. Buka /murid dan coba tambah, ubah, dan hapus data dari halaman yang",
                    "     dibuat scaffold.",
                    "  4. Tambahkan validasi nama wajib di model, lalu rapikan template view",
                    "     sesuai kebutuhan pemilik kursus.",
                ],
            },
        ],
    },
    {
        "title": "30. Active Record dan Resource di Rails",
        "sections": [
            {
                "body": [
                    "Active Record adalah ORM bawaan Rails, dan namanya sama dengan pola yang",
                    "ia populerkan: satu objek mewakili satu baris, dan objek itu sendiri",
                    "tahu cara menyimpan, mengubah, dan menghapus dirinya. Django ORM dan",
                    "Eloquent memakai pola yang sama. Kebalikannya pola Data Mapper",
                    "(Hibernate, Doctrine), tempat objek data polos dan penyimpanan diurus",
                    "kelas terpisah.",
                    "",
                    "Migrasi Rails ditulis dalam Ruby:",
                    "",
                    "  class CreateProduk < ActiveRecord::Migration[8.1]",
                    "    def change",
                    "      create_table :produk do |t|",
                    "        t.string :nama, null: false",
                    "        t.integer :harga, null: false",
                    "        t.integer :stok, default: 0",
                    "        t.references :kategori, null: false, foreign_key: true",
                    "        t.timestamps",
                    "      end",
                    "    end",
                    "  end",
                    "",
                    "Method change cukup menulis arah maju; Rails tahu cara membaliknya untuk",
                    "bin/rails db:rollback. t.references membuat kolom kategori_id beserta",
                    "indeks dan foreign key.",
                ],
            },
            {
                "heading": "Model, asosiasi, dan validasi",
                "bahasa": "ruby",
                "code": """class Produk < ApplicationRecord
  belongs_to :kategori
  validates :nama, presence: true, length: { maximum: 100 }
  validates :harga, numericality: { only_integer: true,
                                    greater_than_or_equal_to: 1000 }
  scope :tersedia, -> { where("stok > 0") }
  ...
end

class Kategori < ApplicationRecord
  has_many :produk, dependent: :restrict_with_error
end""",
            },
            {
                "body": [
                    "Kolom tabel nggak ditulis di model; Active Record membacanya dari",
                    "database saat aplikasi mulai. belongs_to dan has_many membuat method",
                    "relasi seperti produk.kategori dan kategori.produk. dependent:",
                    ":restrict_with_error menolak penghapusan kategori yang masih punya",
                    "produk. Validasi dijalankan saat save; kalau gagal, save mengembalikan",
                    "false dan pesan galatnya ada di produk.errors.",
                    "",
                    "Coba di bin/rails console:",
                    "",
                    "  p = Produk.new(nama: \"\", harga: 500)",
                    "  p.save                      # => false",
                    "  p.errors.full_messages      # => [\"Kategori must exist\",",
                    "                              #     \"Nama can't be blank\", ...]",
                    "  Produk.tersedia.where(harga: ..10_000).order(:harga)",
                    "  Produk.includes(:kategori).each { |x| puts x.kategori.nama }",
                    "",
                    "Rentang ..10_000 diterjemahkan jadi harga <= 10000. includes mengambil",
                    "kategori dalam kueri tambahan supaya perulangan nggak memicu N+1. Pesan",
                    "galat bawaannya berbahasa Inggris; terjemahannya bisa dipasang lewat",
                    "berkas lokal config/locales.",
                ],
            },
            {
                "heading": "Tujuh rute dari resources",
                "body": [
                    "resources :produk di config/routes.rb menghasilkan tujuh aksi. Begini",
                    "kira-kira isi bin/rails routes, tanpa kolom nama helper:",
                    "",
                    "  GET     /produk           produk#index",
                    "  POST    /produk           produk#create",
                    "  GET     /produk/new       produk#new",
                    "  GET     /produk/:id/edit  produk#edit",
                    "  GET     /produk/:id       produk#show",
                    "  PATCH   /produk/:id       produk#update",
                    "  PUT     /produk/:id       produk#update",
                    "  DELETE  /produk/:id       produk#destroy",
                    "",
                    "Batasi dengan only atau except, misalnya resources :ulasan, only:",
                    "[:index, :create]. Resource bisa bersarang: resources :produk do",
                    "resources :ulasan end menghasilkan alamat seperti",
                    "/produk/:produk_id/ulasan. Latihan bab ini memintamu membuat pembangkit",
                    "tabel rute seperti ini.",
                ],
            },
            {
                "heading": "Mode API",
                "body": [
                    "Untuk backend yang cuma melayani JSON, buat aplikasinya dengan rails new",
                    "toko_api --api. Rails membuang middleware dan generator yang khusus",
                    "untuk halaman HTML, dan controller mewarisi ActionController::API.",
                    "Controller-nya membalas JSON langsung:",
                    "",
                    "  def create",
                    "    produk = Produk.new(produk_params)",
                    "    if produk.save",
                    "      render json: produk, status: :created",
                    "    else",
                    "      render json: { errors: produk.errors }, status: 422",
                    "    end",
                    "  end",
                ],
            },
            {
                "heading": "Callback dan transaksi",
                "body": [
                    "Active Record bisa menjalankan kode di titik tertentu siklus hidup",
                    "objek, misalnya sebelum disimpan. Ini disebut callback:",
                    "",
                    "  class Produk < ApplicationRecord",
                    "    before_save { self.nama = nama.strip }",
                    "  end",
                    "",
                    "  Produk.transaction do",
                    "    pesanan.save!",
                    "    produk.decrement!(:stok, pesanan.jumlah)",
                    "  end",
                    "",
                    "Callback cocok untuk merapikan data seperti membuang spasi di ujung",
                    "nama. Jebakan: menaruh logika bisnis besar di callback, misalnya",
                    "mengirim email atau memanggil API pembayaran. Lama-lama nggak ada yang",
                    "tahu apa saja yang terjadi saat sebuah objek disimpan, dan tes jadi",
                    "lambat.",
                    "",
                    "Blok transaction memastikan dua perubahan itu terjadi bersama atau nggak",
                    "sama sekali. Method berakhiran tanda seru (save!, decrement!) melempar",
                    "exception kalau gagal, dan exception itulah yang membatalkan transaksi.",
                    "save tanpa tanda seru cuma mengembalikan false, jadi di dalam transaksi",
                    "kegagalannya terlewat. Transaksi dibahas lebih dalam di kurikulum",
                    "Database.",
                ],
            },
            {
                "heading": "Yang baru di Rails 8",
                "body": [
                    "Rails 8 berusaha supaya satu aplikasi bisa jalan tanpa banyak layanan",
                    "tambahan. Solid Queue menjalankan antrean tugas latar belakang, Solid",
                    "Cache menyimpan cache, dan Solid Cable melayani WebSocket, ketiganya",
                    "memakai database biasa alih-alih Redis. Ada juga generator bin/rails",
                    "generate authentication yang membuat login berbasis sesi sederhana,",
                    "alternatif ringan untuk gem Devise. Untuk deploy, Rails 8 memakai Kamal",
                    "2, alat yang memasang aplikasi dalam kontainer ke server mana pun lewat",
                    "SSH.",
                    "",
                    "Antrean tugas dan cache dibahas lebih lengkap di bab Cache, Antrean, dan",
                    "Message Broker, sedangkan deploy di kurikulum DevOps.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rails dengan Active Record dipakai di banyak produk SaaS dan",
                    "marketplace. Mode API-nya sering jadi backend aplikasi seluler yang",
                    "dibuat tim kecil, karena validasi dan relasinya selesai dalam beberapa",
                    "baris.",
                    "",
                    "Kasus kecil: aplikasi kursus musik dari materi sebelumnya kini butuh API",
                    "jadwal les untuk aplikasi seluler, dan jadwal milik guru yang masih",
                    "punya murid nggak boleh terhapus.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat model Guru dan Jadwal; Jadwal belongs_to :guru, dan Guru",
                    "     has_many :jadwal dengan dependent: :restrict_with_error.",
                    "  2. Tambahkan validasi hari dan jam wajib diisi di model Jadwal.",
                    "  3. Tulis resources :guru do resources :jadwal, only: [:index, :create]",
                    "     end, lalu cek hasilnya dengan bin/rails routes.",
                    "  4. Di controller, balas render json dengan status :created atau 422",
                    "     berisi errors supaya aplikasi seluler tahu kolom mana yang salah.",
                ],
            },
        ],
    },
    {
        "title": "31. Peta Framework PHP dan Ruby",
        "sections": [
            {
                "body": [
                    "Laravel dan Rails menguasai dunianya masing-masing, tapi di proyek nyata",
                    "kamu akan bertemu framework lain, terutama di PHP. Banyak lowongan dan",
                    "proyek pemerintah daerah masih memakai CodeIgniter, dan banyak",
                    "perusahaan Eropa memakai Symfony. Versi di bawah per Oktober 2026.",
                ],
            },
            {
                "heading": "PHP: tabel perbandingan",
                "bahasa": "teks",
                "code": """Nama            Versi                 Gaya                       Status
Symfony         8.1.9 (LTS 7.4.21)    komponen, Doctrine, Twig   aktif
CodeIgniter     4.7.5                 ringan, konfigurasi minim  CI4 aktif, CI3 usang
Yii             2.0.55                generator kode Gii         menurun
CakePHP         5.4.3                 konvensi                   stabil
Slim            4.15.3                microframework PSR         stabil
Laminas/Mezzio  laminas-mvc 3.8.0     komponen, middleware       MVC pensiun
Phalcon         5.23.0                ekstensi C                 stabil, komunitas kecil
Doctrine ORM    3.7.5                 Data Mapper                aktif
Twig            3.30.0                template engine            aktif""",
            },
            {
                "heading": "Symfony dan pasangannya",
                "body": [
                    "Symfony adalah framework PHP modular yang komponennya dipakai ulang di",
                    "banyak proyek lain, termasuk Laravel dan Drupal. Di Survei Stack",
                    "Overflow 2026 pemakainya 4,0%, dan survei JetBrains tentang PHP tahun",
                    "2025 mencatat 23%. Versi 8.1 rilis Mei 2026 dan butuh PHP 8.4; jalur",
                    "LTS-nya 7.4, yang mendapat perbaikan keamanan sampai November 2029. Rute",
                    "biasanya ditulis sebagai atribut di atas method:",
                    "",
                    "  #[Route('/produk/{id}', name: 'produk_show', methods: ['GET'])]",
                    "  public function show(Produk $produk): Response",
                    "  {",
                    "      return $this->render('produk/show.html.twig', [",
                    "          'produk' => $produk,",
                    "      ]);",
                    "  }",
                    "",
                    "Pasangan bawaannya Doctrine ORM dan Twig. Doctrine berpola Data Mapper",
                    "dengan Unit of Work: entity cuma kelas data polos, dan EntityManager",
                    "yang mencatat perubahan lalu menyimpannya sekaligus saat flush()",
                    "dipanggil. Ini kebalikan Eloquent, tempat $produk->save() dipanggil di",
                    "objeknya sendiri. Twig adalah template engine yang meng-escape keluaran",
                    "secara otomatis, dengan sintaks {{ produk.nama }} yang mirip Jinja.",
                ],
            },
            {
                "heading": "Framework PHP lainnya",
                "body": [
                    "CodeIgniter terkenal ringan dan gampang dipelajari, makanya banyak",
                    "dipakai di sekolah, kampus, dan proyek pemerintah daerah. Bedakan",
                    "versinya: CodeIgniter 3 sudah usang dan nggak dikembangkan lagi,",
                    "sedangkan CodeIgniter 4 aktif dan ditulis ulang dengan namespace dan",
                    "Composer. Kalau mewarisi proyek CI3, rencanakan migrasi.",
                    "",
                    "Yii 2 kini dalam pemeliharaan sementara Yii 3 dirilis bertahap per",
                    "paket. CakePHP termasuk framework PHP tertua yang masih aktif dan,",
                    "seperti Rails, mengandalkan konvensi. Slim adalah microframework untuk",
                    "API kecil yang mengikuti standar PSR-7 (objek permintaan dan respons)",
                    "dan PSR-15 (middleware); rilis 4.15.3 menambal celah yang memungkinkan",
                    "batasan rute dilewati. Phalcon dipasang sebagai ekstensi C sehingga",
                    "cepat, tapi butuh akses server untuk memasangnya.",
                    "",
                    "Laminas adalah kelanjutan Zend Framework di bawah Linux Foundation. Pada",
                    "Juni 2025 pengurusnya mengumumkan Laminas MVC pensiun dan cuma menerima",
                    "perbaikan keamanan. Komponen Laminas lain dan Mezzio, framework",
                    "middleware-nya, masih aktif.",
                ],
            },
            {
                "heading": "Ruby di luar Rails",
                "body": [
                    "  require \"sinatra\"",
                    "",
                    "  get \"/halo/:nama\" do",
                    "    \"Halo, #{params[:nama]}!\"",
                    "  end",
                    "",
                    "Sinatra (versi 4.2.1) adalah microframework Ruby dengan DSL seperti di",
                    "atas: metode HTTP, pola rute, lalu blok yang mengembalikan isi respons.",
                    "Gaya ini menginspirasi Express dan Flask. Cocok untuk API kecil atau",
                    "sebagai jembatan sebelum Rails.",
                    "",
                    "Semua framework Ruby di sini berdiri di atas Rack, kontrak \"aplikasi",
                    "sebagai fungsi\" versi Ruby yang kamu lihat di bab 01. Hanami (3.0.2)",
                    "adalah alternatif Rails yang menekankan arsitektur bersih dan modular,",
                    "dengan komunitas kecil. Roda (3.109.0, rilis bulanan) memakai routing",
                    "tree: rute ditulis sebagai cabang bersarang sehingga cepat dan mudah",
                    "dibaca. Grape (4.0.1) adalah DSL khusus API REST yang bisa dipasang di",
                    "dalam aplikasi Rails atau berdiri sendiri di atas Rack.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  1. Proyek baru PHP: Laravel, atau Symfony kalau tim butuh komponen",
                    "     yang bisa dipilih satu per satu dan dukungan LTS panjang.",
                    "  2. Mewarisi CodeIgniter 3, Yii 2, atau Laminas MVC: rawat, lalu",
                    "     rencanakan migrasi ke CodeIgniter 4, Laravel, atau Symfony.",
                    "  3. API kecil di PHP: Slim. Di Ruby: Sinatra, Roda, atau Grape.",
                    "  4. Proyek baru Ruby yang lengkap: Rails; Hanami kalau tim ingin",
                    "     pemisahan lapisan yang lebih tegas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi layanan publik daerah dan sistem informasi sekolah di",
                    "Indonesia dibangun dengan CodeIgniter 3 bertahun-tahun lalu, dan",
                    "memindahkannya ke CodeIgniter 4 atau Laravel jadi pekerjaan rutin",
                    "pengembang PHP lokal.",
                    "",
                    "Kasus kecil: kamu diminta menambah fitur di aplikasi CodeIgniter 3 milik",
                    "dinas, padahal versi itu sudah usang.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek versi persis di system/core/CodeIgniter.php dan catat versi PHP",
                    "     server yang dipakai.",
                    "  2. Kerjakan fitur yang diminta di CI3 dulu supaya layanan nggak",
                    "     terganggu, sambil mencatat bagian yang sering bermasalah.",
                    "  3. Usulkan migrasi bertahap ke CodeIgniter 4, dimulai dari modul yang",
                    "     paling kecil, karena struktur folder dan namespace-nya berbeda.",
                    "  4. Tulis tes untuk modul yang dipindah supaya perilaku lama dan baru",
                    "     bisa dibandingkan.",
                ],
            },
        ],
    },
    {
        "title": "32. Go net/http: Server API Tanpa Framework",
        "sections": [
            {
                "body": [
                    "Di banyak bahasa, membuat API berarti memilih framework dulu. Di Go,",
                    "banyak tim memulai tanpa framework sama sekali. Pustaka standarnya,",
                    "paket net/http, sudah cukup untuk server produksi: ia menangani HTTP/1.1",
                    "dan HTTP/2, koneksi bersamaan, dan batas waktu. Survei tren bahasa Go",
                    "dari JetBrains tahun 2025 mencatat 32% pengembang Go memakai net/http",
                    "langsung.",
                    "",
                    "Alasan terbesarnya Go 1.22. Sejak versi itu, router bawaannya (ServeMux)",
                    "mengerti metode HTTP dan wildcard di path, dua hal yang dulu jadi alasan",
                    "utama memasang router pihak ketiga. Saat materi ini ditulis (Oktober",
                    "2026) versi Go terbarunya 1.27.2.",
                    "",
                    "Prasyaratnya kurikulum Go: struct, method, interface, error, dan",
                    "goroutine. Contoh di bawah bisa dijalankan langsung. Ia nggak membuka",
                    "port; permintaannya dibuat dengan paket httptest, persis cara kamu",
                    "menguji handler.",
                ],
            },
            {
                "heading": "Tipe data dan handler",
                "bahasa": "go",
                "code": """type Produk struct {
	ID    int    `json:"id"`
	Nama  string `json:"nama"`
	Harga int    `json:"harga"`
}

type Toko struct {
	mu      sync.Mutex
	produk  map[int]Produk
	berikut int
}

func (t *Toko) ambil(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(r.PathValue("id"))
	if err != nil {
		http.Error(w, "id harus angka", http.StatusBadRequest)
		return
	}
	t.mu.Lock()
	p, ada := t.produk[id]
	t.mu.Unlock()
	if !ada {
		http.NotFound(w, r)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(p)
}

func (t *Toko) tambah(w http.ResponseWriter, r *http.Request) {
	var p Produk
	if err := json.NewDecoder(r.Body).Decode(&p); err != nil || p.Nama == "" {
		http.Error(w, "body tidak valid", http.StatusUnprocessableEntity)
		return
	}
	t.mu.Lock()
	t.berikut++
	p.ID = t.berikut
	t.produk[p.ID] = p
	t.mu.Unlock()
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(p)
}""",
            },
            {
                "body": [
                    "Simpan semuanya di satu berkas main.go yang diawali package main dan",
                    "import berikut, lalu tambahkan fungsi main di bawah ini:",
                    "",
                    "  package main",
                    "",
                    "  import (",
                    "      \"encoding/json\"",
                    "      \"fmt\"",
                    "      \"net/http\"",
                    "      \"net/http/httptest\"",
                    "      \"strconv\"",
                    "      \"strings\"",
                    "      \"sync\"",
                    "  )",
                ],
            },
            {
                "heading": "Router dan uji tanpa port",
                "bahasa": "go",
                "code": """func main() {
	toko := &Toko{
		produk:  map[int]Produk{1: {ID: 1, Nama: "Teh Botol", Harga: 5000}},
		berikut: 1,
	}
	mux := http.NewServeMux()
	mux.HandleFunc("GET /produk/{id}", toko.ambil)
	mux.HandleFunc("POST /produk", toko.tambah)

	// Di server sungguhan: http.ListenAndServe(":8080", mux)
	coba := func(metode, alamat, body string) {
		req := httptest.NewRequest(metode, alamat, strings.NewReader(body))
		rec := httptest.NewRecorder()
		mux.ServeHTTP(rec, req)
		fmt.Printf("%s %s -> %d %s", metode, alamat, rec.Code, rec.Body.String())
	}
	coba("GET", "/produk/1", "")
	coba("GET", "/produk/9", "")
	coba("GET", "/produk/abc", "")
	coba("POST", "/produk", `{"nama":"Kopi","harga":18000}`)
	coba("DELETE", "/produk/1", "")
}""",
            },
            {
                "body": [
                    "Jalankan dengan go run main.go. Kompilasi pertama butuh belasan detik",
                    "karena paket net/http ikut dikompilasi, jalankan berikutnya hampir",
                    "seketika.",
                    "",
                    "Keluaran:",
                    "  GET /produk/1 -> 200 {\"id\":1,\"nama\":\"Teh Botol\",\"harga\":5000}",
                    "  GET /produk/9 -> 404 404 page not found",
                    "  GET /produk/abc -> 400 id harus angka",
                    "  POST /produk -> 201 {\"id\":2,\"nama\":\"Kopi\",\"harga\":18000}",
                    "  DELETE /produk/1 -> 405 Method Not Allowed",
                    "",
                    "Pola \"GET /produk/{id}\" berisi metode dan wildcard. r.PathValue(\"id\")",
                    "membaca nilainya. Permintaan DELETE ke path yang cocok tapi metodenya",
                    "nggak terdaftar dibalas 405 Method Not Allowed oleh ServeMux sendiri,",
                    "dan alamat yang nggak cocok sama sekali dibalas 404.",
                    "",
                    "Handler di Go adalah fungsi dengan dua parameter: http.ResponseWriter",
                    "untuk menulis respons dan *http.Request untuk membaca permintaan.",
                    "Urutannya penting: header ditulis dulu, lalu WriteHeader untuk status,",
                    "lalu body. Kalau body ditulis lebih dulu, Go otomatis mengirim status",
                    "200 dan header yang diatur sesudahnya diabaikan.",
                    "",
                    "Ingat juga sync.Mutex. Server Go melayani tiap permintaan di goroutine",
                    "sendiri, jadi dua permintaan bisa menulis map produk bersamaan. Map Go",
                    "nggak aman untuk itu; tanpa kunci, program bisa berhenti dengan galat",
                    "concurrent map writes.",
                ],
            },
            {
                "heading": "Aturan pola ServeMux",
                "body": [
                    "Bentuk pola yang bisa kamu tulis sejak Go 1.22:",
                    "",
                    "  \"GET /produk/{id}\"      metode GET, satu segmen jadi id",
                    "  \"/produk/\"              awalan: /produk/ dan semua di bawahnya",
                    "  \"GET /berkas/{path...}\" sisa path, misalnya a/b/c.txt",
                    "  \"GET /{$}\"              cuma tepat /, bukan /apa-saja",
                    "  \"POST /produk\"          metode POST saja",
                    "",
                    "Pola GET juga melayani HEAD. Kalau dua pola sama-sama cocok, yang lebih",
                    "spesifik menang. Lebih spesifik artinya cocok dengan sebagian dari",
                    "permintaan yang dicocokkan pola lain: GET /produk/terbaru mengalahkan",
                    "GET /produk/{id} untuk alamat /produk/terbaru. Kalau ada dua pola yang",
                    "saling tumpang tapi nggak ada yang lebih spesifik, misalnya GET",
                    "/produk/{id} dan GET /{jenis}/terbaru, Go menolak mendaftarkannya dan",
                    "program panic saat mulai. Latihan bab ini memintamu meniru aturan itu.",
                ],
            },
            {
                "heading": "Middleware tanpa framework",
                "body": [
                    "Middleware di Go cuma fungsi yang menerima http.Handler dan",
                    "mengembalikan http.Handler baru:",
                    "",
                    "  func catat(next http.Handler) http.Handler {",
                    "      return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {",
                    "          mulai := time.Now()",
                    "          next.ServeHTTP(w, r)",
                    "          log.Printf(\"%s %s %v\", r.Method, r.URL.Path, time.Since(mulai))",
                    "      })",
                    "  }",
                    "",
                    "  http.ListenAndServe(\":8080\", catat(mux))",
                    "",
                    "Bentuknya sama dengan gaya \"bawang\" di bab 01: kode sebelum",
                    "next.ServeHTTP jalan saat masuk, kode sesudahnya jalan saat keluar.",
                    "Karena semua router dan framework Go yang dibangun di atas net/http",
                    "memakai bentuk ini, middleware yang kamu tulis bisa dipakai ulang di",
                    "mana saja.",
                    "",
                    "Jebakan: http.ListenAndServe tanpa batas waktu. Untuk produksi, buat",
                    "&http.Server{Addr: \":8080\", Handler: mux, ReadHeaderTimeout: 5 *",
                    "time.Second} supaya klien yang sengaja mengirim header pelan-pelan nggak",
                    "menahan koneksi selamanya.",
                ],
            },
            {
                "heading": "database/sql",
                "body": [
                    "Untuk database, Go punya antarmuka bawaan database/sql lengkap dengan",
                    "connection pool. Drivernya dipasang terpisah dan mendaftarkan diri lewat",
                    "import kosong:",
                    "",
                    "  import (",
                    "      \"database/sql\"",
                    "      _ \"github.com/jackc/pgx/v5/stdlib\"",
                    "  )",
                    "",
                    "  db, err := sql.Open(\"pgx\", os.Getenv(\"DATABASE_URL\"))",
                    "  ...",
                    "  var p Produk",
                    "  err = db.QueryRowContext(ctx,",
                    "      \"SELECT id, nama, harga FROM produk WHERE id = $1\", id).",
                    "      Scan(&p.ID, &p.Nama, &p.Harga)",
                    "  if errors.Is(err, sql.ErrNoRows) {",
                    "      http.NotFound(w, r)",
                    "      return",
                    "  }",
                    "",
                    "$1 adalah placeholder PostgreSQL; nilainya dikirim terpisah dari SQL.",
                    "sql.Open belum membuka koneksi apa pun, ia cuma menyiapkan pool, jadi",
                    "panggil db.PingContext saat mulai kalau ingin tahu databasenya bisa",
                    "dihubungi. QueryRowContext menerima context dari r.Context(), sehingga",
                    "kueri ikut dibatalkan kalau klien memutus permintaannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "net/http dipakai untuk layanan backend berkinerja tinggi seperti gateway",
                    "pembayaran, layanan notifikasi, dan API internal, karena hasil kompilasi",
                    "Go berupa satu berkas biner yang gampang dipasang dan hemat memori.",
                    "",
                    "Kasus kecil: kamu diminta membuat layanan cek ongkos kirim kecil yang",
                    "dipanggil aplikasi toko, dan tim nggak ingin menambah dependensi pihak",
                    "ketiga.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat http.NewServeMux dengan pola \"GET /ongkir/{kota}\" dan baca",
                    "     kotanya lewat r.PathValue.",
                    "  2. Simpan tarif di map yang dibaca saja, jadi nggak perlu mutex, lalu",
                    "     balas JSON dengan json.NewEncoder.",
                    "  3. Tulis tes dengan httptest.NewRecorder untuk kota yang ada (200) dan",
                    "     yang nggak ada (404).",
                    "  4. Bungkus mux dengan middleware pencatat dan jalankan lewat",
                    "     http.Server yang punya ReadHeaderTimeout.",
                ],
            },
        ],
    },
    {
        "title": "33. Gin dan GORM untuk API Go",
        "sections": [
            {
                "body": [
                    "Walau net/http sudah cukup, Gin tetap framework web Go yang paling",
                    "banyak dipakai: survei JetBrains tahun 2025 mencatat 48% pengembang Go",
                    "memakainya, naik dari 41% di tahun 2020. Gin juga yang paling sering",
                    "muncul di lowongan. Yang ditawarkannya: router cepat, middleware siap",
                    "pakai, serta binding dan validasi JSON dalam satu baris. Versi",
                    "terbarunya 1.12.0 (Februari 2026), dan versi ini butuh Go 1.24 ke atas.",
                ],
            },
            {
                "heading": "API dengan Gin",
                "bahasa": "go",
                "code": """package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type ProdukBaru struct {
	Nama  string `json:"nama" binding:"required,max=100"`
	Harga int    `json:"harga" binding:"required,gte=1000"`
}

func main() {
	r := gin.Default()

	r.GET("/produk/:id", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"id": c.Param("id")})
	})

	r.POST("/produk", func(c *gin.Context) {
		var in ProdukBaru
		if err := c.ShouldBindJSON(&in); err != nil {
			c.JSON(http.StatusUnprocessableEntity, gin.H{"galat": err.Error()})
			return
		}
		c.JSON(http.StatusCreated, in)
	})

	r.Run(":8080")
}""",
            },
            {
                "body": [
                    "gin.Default() sudah memasang dua middleware: Logger yang mencatat tiap",
                    "permintaan dan Recovery yang mengubah panic jadi respons 500 alih-alih",
                    "mematikan server. Parameter path di Gin ditulis :id, beda dengan {id}",
                    "milik ServeMux. Tag binding di struct dibaca pustaka validator, jadi",
                    "JSON tanpa nama atau dengan harga di bawah 1000 langsung ditolak oleh",
                    "ShouldBindJSON. gin.H cuma singkatan untuk map[string]any.",
                    "",
                    "Satu catatan: *gin.Context bukan http.Handler biasa. Middleware Gin",
                    "ditulis sebagai func(c *gin.Context) yang memanggil c.Next(), jadi",
                    "middleware net/http standar perlu dibungkus dulu sebelum bisa dipakai.",
                ],
            },
            {
                "heading": "GORM",
                "bahasa": "go",
                "code": """type Kategori struct {
	ID   uint
	Nama string `gorm:"size:50;uniqueIndex"`
}

type Produk struct {
	gorm.Model
	Nama       string `gorm:"size:100;not null"`
	Harga      int
	KategoriID uint
	Kategori   Kategori
}

db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
...
db.AutoMigrate(&Kategori{}, &Produk{})
db.Create(&Produk{Nama: "Teh", Harga: 5000, KategoriID: 1})

var murah []Produk
db.Preload("Kategori").Where("harga < ?", 10000).Order("harga").Find(&murah)""",
            },
            {
                "body": [
                    "GORM (versi 1.31.2) adalah ORM paling populer di Go. gorm.Model",
                    "menyisipkan kolom ID, CreatedAt, UpdatedAt, dan DeletedAt. Kolom",
                    "terakhir itu membuat Delete jadi soft delete: baris cuma ditandai",
                    "terhapus dan disembunyikan dari kueri biasa, tanpa dibuang dari tabel.",
                    "Banyak pemula kaget karena tabelnya nggak pernah mengecil.",
                    "",
                    "Preload(\"Kategori\") mengambil kategori dalam satu kueri tambahan, cara",
                    "ORM ini menghindari N+1. AutoMigrate praktis saat belajar, tapi ia cuma",
                    "menambah, nggak pernah menghapus kolom; untuk produksi, banyak tim",
                    "memakai alat migrasi terpisah seperti golang-migrate atau goose.",
                ],
            },
            {
                "heading": "SQL dulu: sqlc, sqlx, ent, dan pgx",
                "bahasa": "postgresql",
                "code": """-- query.sql, dibaca sqlc
-- name: ProdukMurah :many
SELECT id, nama, harga FROM produk WHERE harga < $1 ORDER BY harga;""",
            },
            {
                "body": [
                    "Banyak programmer Go memilih menulis SQL sendiri. sqlc (1.31.1) membaca",
                    "berkas SQL seperti di atas beserta skema tabelnya, lalu membangkitkan",
                    "kode Go bertipe aman. Dari kueri itu ia membuat method kira-kira seperti",
                    "ini:",
                    "",
                    "  func (q *Queries) ProdukMurah(ctx context.Context,",
                    "      harga int32) ([]ProdukMurahRow, error)",
                    "",
                    "Kalau kolom atau tipenya salah, kesalahannya ketahuan saat kode",
                    "dibangkitkan, bukan saat aplikasi jalan. Cocok untuk kamu yang kuat di",
                    "kurikulum SQL.",
                    "",
                    "sqlx (1.4.0, rilis April 2024) memperluas database/sql supaya baris",
                    "hasil langsung dipetakan ke struct. Rilisnya jarang, tapi stabil dan",
                    "masih banyak dipakai. ent (0.14.6) dari Meta memakai pendekatan skema",
                    "sebagai kode: kamu menulis skema dalam Go, ent membangkitkan kode akses",
                    "data lengkap dengan relasi berbentuk graf. pgx (5.11.0) adalah driver",
                    "PostgreSQL murni Go yang cepat. Ia driver, jadi sering jadi fondasi di",
                    "bawah sqlc atau dipakai langsung.",
                    "",
                    "Jebakan: memakai ORM lalu menulis setiap kueri dengan Raw. Kalau hampir",
                    "semua kuerimu SQL mentah, kamu cuma membayar lapisan ORM tanpa",
                    "memakainya; sqlc atau sqlx lebih jujur untuk gaya itu. Perbandingan ORM",
                    "dan migrasi yang lebih dalam ada di kurikulum Database.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Gin bersama sebuah ORM atau sqlc dipakai di banyak backend aplikasi ojek",
                    "daring, dompet digital, dan marketplace. Biasanya untuk layanan yang",
                    "harus melayani banyak permintaan dengan server kecil.",
                    "",
                    "Kasus kecil: API daftar transaksi di aplikasi dompet digital lambat, dan",
                    "log menunjukkan ORM-nya mengirim satu kueri pengguna untuk setiap",
                    "transaksi di halaman itu.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Aktifkan log kueri dengan db.Debug() untuk endpoint itu dan hitung",
                    "     jumlah kueri per permintaan.",
                    "  2. Tambahkan Preload(\"Pengguna\") di kueri transaksi, atau ganti dengan",
                    "     Joins kalau cuma butuh satu kolom dari tabel pengguna.",
                    "  3. Untuk laporan bulanan yang berat, tulis SQL-nya sendiri dan",
                    "     bangkitkan fungsinya dengan sqlc.",
                    "  4. Ukur ulang dan pastikan jumlah kueri per halaman tetap walau jumlah",
                    "     transaksinya bertambah.",
                ],
            },
        ],
    },
    {
        "title": "34. Peta Framework Go, Rust, dan Bahasa Lain",
        "sections": [
            {
                "body": [
                    "Materi ini memetakan framework backend di Go, Rust, Elixir, Swift, C++,",
                    "dan Dart. Kamu nggak perlu menguasai semuanya; cukup tahu masing-masing",
                    "itu apa, sehingga saat bertemu di lowongan atau kode orang lain, kamu",
                    "tahu harus mulai belajar dari mana. Versi di tabel per Oktober 2026.",
                ],
            },
            {
                "heading": "Tabel perbandingan",
                "bahasa": "teks",
                "code": """Nama        Bahasa  Versi          Catatan singkat                  Status
Echo        Go      5.4.0          minimalis, middleware lengkap    aktif (v5)
Fiber       Go      3.6.1          gaya Express, di atas fasthttp   aktif (v3)
chi         Go      5.5.0          router, 100% net/http            aktif
Gorilla mux Go      1.8.1          router lama sebelum Go 1.22      menurun
Beego       Go      2.3.10         MVC full-stack                   menurun
Axum        Rust    0.8.9          dari tim Tokio, extractor        aktif, masih 0.x
Actix Web   Rust    4.17.0         matang, sangat cepat             aktif
Rocket      Rust    0.5.1          makro, request guard             menurun
Warp        Rust    0.4.3          filter yang dikomposisi          stabil
Poem        Rust    3.1.12         OpenAPI bawaan                   stabil, rilis jarang
Loco        Rust    1.2.0          gaya Rails di atas Axum          aktif
Tokio       Rust    1.53.3         runtime async                    aktif
hyper       Rust    1.12.0         HTTP tingkat rendah              aktif
Phoenix     Elixir  1.8.15         Channels, LiveView               aktif
Vapor       Swift   4.122.2        server-side Swift                aktif, komunitas kecil
Drogon      C++     1.9.14         async C++17/20, ORM bawaan       aktif
Serverpod   Dart    4.0.4          server untuk Flutter             aktif""",
            },
            {
                "heading": "Go",
                "body": [
                    "Echo dan Gin adalah dua framework Go \"lengkap\" yang paling sering",
                    "dibandingkan. Echo kini di versi 5 dengan jalur import berakhiran /v5,",
                    "jadi kode dari tutorial v4 perlu diubah import-nya; rilis 5.4.0 juga",
                    "menambal enam celah keamanan. Survei JetBrains 2025 mencatat 16%",
                    "pengembang Go memakai Echo.",
                    "",
                    "chi adalah router ringan yang 100% kompatibel dengan net/http, jadi",
                    "handler dan middleware standar langsung bisa dipakai. Pilihan populer",
                    "bagi yang ingin sedikit bantuan tanpa framework besar. Fiber meniru gaya",
                    "Express, tapi dibangun di atas fasthttp, bukan net/http. Akibatnya",
                    "cepat, tapi middleware Go standar nggak langsung cocok dengannya.",
                    "",
                    "Gorilla mux adalah router paling terkenal sebelum Go 1.22. Proyeknya",
                    "sempat diarsipkan tahun 2022 lalu dihidupkan kembali; masih banyak di",
                    "kode lama, tapi untuk proyek baru router bawaan sudah cukup. Beego",
                    "adalah framework MVC lengkap dengan ORM dan cache sendiri, populer di",
                    "Tiongkok, dengan rilis yang makin jarang.",
                ],
            },
            {
                "heading": "Rust",
                "body": [
                    "  use axum::{extract::Path, routing::get, Json, Router};",
                    "  use serde_json::{json, Value};",
                    "",
                    "  async fn ambil(Path(id): Path<u32>) -> Json<Value> {",
                    "      Json(json!({ \"id\": id, \"nama\": \"Teh Botol\" }))",
                    "  }",
                    "",
                    "  #[tokio::main]",
                    "  async fn main() {",
                    "      let app = Router::new().route(\"/produk/{id}\", get(ambil));",
                    "      let listener = tokio::net::TcpListener::bind(\"0.0.0.0:3000\")",
                    "          .await",
                    "          .unwrap();",
                    "      axum::serve(listener, app).await.unwrap();",
                    "  }",
                    "",
                    "Axum dibuat tim Tokio. Parameter handler disebut extractor: Path<u32>",
                    "mengambil dan memeriksa id dari URL, dan kalau bukan angka Axum menolak",
                    "permintaannya sebelum handler dipanggil. Sejak 0.8, parameter path",
                    "ditulis /{id}, bukan /:id seperti di tutorial lama. Di Survei Stack",
                    "Overflow 2026 pemakainya 3,6%, tapi 70,6% pemakainya ingin terus",
                    "memakainya. Prasyaratnya kurikulum Rust, terutama async dan trait.",
                    "",
                    "Actix Web lebih tua, matang, dan sering ada di puncak benchmark. Rocket",
                    "mengutamakan kenyamanan lewat makro dan request guard, tapi rilis stabil",
                    "terakhirnya Mei 2024, sehingga untuk proyek baru Axum lebih aman. Warp",
                    "menyusun rute dari filter yang digabung-gabung. Poem punya dukungan",
                    "OpenAPI bawaan lewat poem-openapi. Loco membawa gaya Rails (generator,",
                    "job, mailer) di atas Axum dengan SeaORM.",
                    "",
                    "Di bawah hampir semuanya ada Tokio, runtime async standar de facto di",
                    "Rust, dan hyper, pustaka HTTP tingkat rendah yang jarang dipakai",
                    "langsung. Runtime alternatif async-std sudah nggak dikembangkan lagi.",
                ],
            },
            {
                "heading": "Bahasa lain",
                "body": [
                    "Phoenix untuk Elixir berjalan di mesin virtual Erlang yang terkenal",
                    "tahan gangguan. Fitur Channels dan LiveView membuat aplikasi real-time",
                    "dan halaman interaktif tanpa banyak JavaScript. Di Survei Stack Overflow",
                    "2026 pemakainya 2,5% dan 69,5% ingin terus memakainya. Aplikasi ini",
                    "belum punya kurikulum Elixir, jadi anggap Phoenix sebagai wawasan dulu.",
                    "",
                    "Vapor adalah framework server untuk Swift, menarik untuk tim iOS yang",
                    "ingin satu bahasa di aplikasi dan server. Drogon adalah framework",
                    "C++17/20 asinkron berkinerja tinggi dengan ORM bawaan. Serverpod adalah",
                    "server aplikasi dalam Dart yang membangkitkan kode klien otomatis untuk",
                    "aplikasi Flutter.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  1. Go, proyek baru: mulai dari net/http, tambah chi kalau butuh grup",
                    "     rute dan middleware siap pakai, atau Gin kalau timmu sudah terbiasa",
                    "     dengannya.",
                    "  2. Rust, proyek baru: Axum. Actix Web juga aman; hindari memulai",
                    "     proyek baru dengan Rocket.",
                    "  3. Aplikasi real-time dengan banyak koneksi dan tim yang mau belajar",
                    "     bahasa baru: Phoenix.",
                    "  4. Mewarisi Gorilla atau Beego: rawat, dan pertimbangkan pindah ke",
                    "     router bawaan atau chi saat ada kesempatan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rust dengan Axum dan Actix Web makin sering dipakai untuk layanan yang",
                    "sensitif terhadap kinerja dan memori, misalnya proxy, layanan pencarian,",
                    "dan pemroses data real-time. Go dengan chi atau Gin banyak dipakai untuk",
                    "layanan mikro di perusahaan teknologi.",
                    "",
                    "Kasus kecil: timmu mewarisi layanan Go yang memakai gorilla/mux dan",
                    "ingin mengurangi dependensi.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Daftar semua rute dan cari fitur mux yang dipakai, misalnya",
                    "     variabel path, pembatasan metode, dan subrouter.",
                    "  2. Terjemahkan pola seperti /produk/{id} dengan Methods(\"GET\") ke pola",
                    "     ServeMux \"GET /produk/{id}\".",
                    "  3. Ganti mux.Vars(r)[\"id\"] dengan r.PathValue(\"id\") dan jalankan tes",
                    "     untuk tiap rute.",
                    "  4. Kalau subrouter dan grup middleware terlalu banyak, pindah ke chi,",
                    "     yang tetap kompatibel dengan net/http.",
                ],
            },
        ],
    },
    {
        "title": "35. Peta ORM dan Query Builder Lintas Bahasa",
        "sections": [
            {
                "body": [
                    "Sepanjang bab 05 sampai 10 kamu sudah bertemu Django ORM, Hibernate, EF",
                    "Core, Eloquent, Active Record, dan ORM Go. Hampir setiap bahasa punya",
                    "beberapa alat lagi untuk bicara dengan database. Supaya nggak tenggelam",
                    "di nama, kelompokkan dulu berdasarkan polanya:",
                    "",
                    "  - Active Record: objek model menyimpan dirinya sendiri",
                    "    (produk.save()). Contoh: Eloquent, Rails, Django ORM.",
                    "  - Data Mapper: objek data polos, penyimpanan diurus kelas lain dengan",
                    "    Unit of Work. Contoh: Hibernate, Doctrine, EF Core.",
                    "  - Query builder: kamu menyusun SQL dengan method berantai, hasilnya",
                    "    baris biasa, bukan objek model.",
                    "  - Pemeta SQL dan pembangkit kode: kamu menulis SQL, alatnya memetakan",
                    "    hasil atau membangkitkan fungsi bertipe.",
                    "",
                    "Query builder paling gampang dipahami kalau kamu membuat versi mininya",
                    "sendiri:",
                ],
            },
            {
                "heading": "Query builder mini",
                "code": """import sqlite3


class Kueri:
    def __init__(self, tabel):
        self.tabel, self.syarat, self.nilai, self.urut = tabel, [], [], ""

    def where(self, kolom, op, nilai):
        self.syarat.append(f"{kolom} {op} ?")
        self.nilai.append(nilai)
        return self

    def order_by(self, kolom):
        self.urut = f" ORDER BY {kolom}"
        return self

    def sql(self):
        teks = f"SELECT * FROM {self.tabel}"
        if self.syarat:
            teks += " WHERE " + " AND ".join(self.syarat)
        return teks + self.urut, self.nilai


db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, harga INTEGER)")
db.executemany("INSERT INTO produk (nama, harga) VALUES (?, ?)",
               [("Teh", 5000), ("Kopi", 18000), ("Roti", 12000)])

sql, nilai = Kueri("produk").where("harga", "<", 15000).order_by("harga").sql()
print(sql, nilai)
for baris in db.execute(sql, nilai):
    print(baris)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  SELECT * FROM produk WHERE harga < ? ORDER BY harga [15000]",
                    "  (1, 'Teh', 5000)",
                    "  (3, 'Roti', 12000)",
                    "",
                    "Setiap method mengembalikan self, jadi pemanggilan bisa dirantai. Nilai",
                    "disimpan terpisah sebagai parameter ?, sedangkan nama kolom ditulis",
                    "langsung, makanya query builder sungguhan memeriksa nama kolom sebelum",
                    "dimasukkan. Knex dan Kysely bekerja dengan gagasan yang sama, dengan",
                    "pemeriksaan dan dukungan dialek SQL yang jauh lebih lengkap.",
                ],
            },
            {
                "heading": "Tabel besar",
                "bahasa": "teks",
                "code": """Alat           Bahasa      Versi (Okt 2026)  Pola                     Status
Drizzle ORM    TypeScript  0.45.4            builder bergaya SQL      aktif, 1.0 beta
Sequelize      JS/TS       6.37.8            Active Record            menurun, v7 alpha
Knex.js        JS/TS       3.3.0             query builder + migrasi  stabil
Kysely         TypeScript  0.29.7            query builder bertipe    aktif
MikroORM       TypeScript  7.2.5             Data Mapper + UoW        aktif
Mongoose       JS/TS       9.11.2            ODM untuk MongoDB        aktif
Objection.js   JS/TS       4.2.0             ORM di atas Knex         aktif kembali
Peewee         Python      4.5.3             Active Record kecil      stabil
Tortoise ORM   Python      1.1.9             async, mirip Django ORM  aktif
MyBatis        Java        3.5.19            pemeta SQL               stabil, rilis jarang
jOOQ           Java/Kotlin 3.21.9            SQL bertipe, kode dari skema  aktif
Exposed        Kotlin      1.6.0             DSL + DAO                aktif
Ebean          Java/Kotlin 19.6.0            ORM sederhana            stabil
Sequel         Ruby        5.109.0           toolkit + ORM            aktif
Diesel         Rust        2.3.14            ORM + builder, cek saat kompilasi  aktif
SQLx           Rust        0.9.0             SQL dicek saat kompilasi aktif
SeaORM         Rust        2.0.4             ORM async di atas SQLx   aktif
Ecto           Elixir      3.14.2            schema + changeset       aktif""",
            },
            {
                "heading": "JavaScript dan TypeScript",
                "body": [
                    "Drizzle ORM menulis skema sebagai kode TypeScript dan kuerinya terasa",
                    "seperti SQL bertipe; tumbuh cepat dan cocok kalau kamu sudah paham SQL.",
                    "Sequelize adalah ORM Node.js tertua yang masih banyak dipakai, sering",
                    "ditemui di proyek PKL, tapi versi 7-nya tertahan lama di tahap alpha",
                    "sehingga proyek baru cenderung memilih Prisma atau Drizzle. Knex.js",
                    "adalah query builder dengan sistem migrasi, dan Objection.js adalah ORM",
                    "di atas Knex; banyak artikel lama menyebut Objection ditinggalkan,",
                    "padahal kini dirawat ulang oleh organisasi ditojs dan sudah merilis",
                    "versi 4. Kysely adalah query builder yang tipenya diperiksa TypeScript",
                    "sampai ke nama kolom. MikroORM memakai Data Mapper dan Unit of Work",
                    "seperti Hibernate. Mongoose bukan ORM untuk SQL; ia object document",
                    "mapper untuk MongoDB dengan skema dan validasi.",
                ],
            },
            {
                "heading": "Python, JVM, dan Ruby",
                "body": [
                    "Peewee adalah ORM Python kecil untuk SQLite, PostgreSQL, dan MySQL, enak",
                    "untuk skrip dan aplikasi kecil. Tortoise ORM adalah ORM async yang",
                    "API-nya terinspirasi Django ORM, sering dipasangkan dengan framework",
                    "ASGI.",
                    "",
                    "Di dunia JVM, MyBatis memetakan SQL yang kamu tulis sendiri (di XML atau",
                    "anotasi) ke objek; masih banyak di aplikasi perusahaan. jOOQ",
                    "membangkitkan kode dari skema database sehingga kueri ditulis seperti",
                    "SQL tapi diperiksa compiler; edisi open source-nya untuk database open",
                    "source, sedangkan Oracle dan SQL Server butuh lisensi berbayar. Exposed",
                    "dari JetBrains adalah pasangan alami Ktor, dengan dua gaya: DSL mirip",
                    "SQL dan DAO. Ebean adalah ORM Java yang lebih sederhana daripada",
                    "Hibernate.",
                    "",
                    "Sequel adalah toolkit database Ruby yang fleksibel, alternatif Active",
                    "Record bagi yang ingin kendali lebih besar atas SQL.",
                ],
            },
            {
                "heading": "Rust dan Elixir",
                "body": [
                    "Diesel adalah ORM dan query builder Rust yang memeriksa kueri saat",
                    "kompilasi, jadi kolom yang salah ketik nggak akan lolos jadi program.",
                    "SQLx untuk Rust (proyek berbeda dengan sqlx milik Go walau namanya sama)",
                    "membiarkanmu menulis SQL biasa lalu memeriksanya terhadap database",
                    "sungguhan saat kompilasi. SeaORM adalah ORM async yang dibangun di atas",
                    "SQLx dan dipakai Loco.",
                    "",
                    "Ecto di Elixir sengaja nggak menyebut dirinya ORM. Ia memisahkan schema,",
                    "query, dan changeset, yaitu objek yang menampung data masuk beserta",
                    "validasinya sebelum disimpan. Gagasan changeset menarik dibandingkan",
                    "dengan validasi di model Rails atau Django.",
                    "",
                    "Pendalaman soal N+1, indeks, transaksi, dan migrasi untuk semua alat ini",
                    "ada di kurikulum Database.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Satu perusahaan sering memakai lebih dari satu pola sekaligus: ORM untuk",
                    "CRUD harian, query builder atau SQL mentah untuk laporan, dan alat",
                    "migrasi terpisah untuk perubahan tabel.",
                    "",
                    "Kasus kecil: kamu bergabung dengan proyek Node.js yang memakai Sequelize",
                    "versi 6, dan tim ingin tahu apakah perlu pindah.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek versi di package.json dan catat fitur Sequelize yang dipakai:",
                    "     model, asosiasi, migrasi, atau kueri mentah.",
                    "  2. Kalau proyeknya stabil dan versi 6 masih menerima rilis,",
                    "     pertahankan dulu; pindah ORM itu mahal.",
                    "  3. Untuk modul baru, coba Drizzle atau Kysely berdampingan di satu",
                    "     modul kecil dan bandingkan kejelasan kodenya.",
                    "  4. Putuskan bersama tim berdasarkan hasil percobaan itu, dan tulis",
                    "     alasannya supaya keputusan berikutnya nggak mulai dari nol.",
                ],
            },
        ],
    },
    {
        "title": "36. Session, Cookie, dan Menyimpan Kata Sandi",
        "sections": [
            {
                "body": [
                    "Di bab 01 kamu sudah tahu HTTP itu stateless: tiap permintaan berdiri",
                    "sendiri, dan server nggak ingat siapa yang barusan datang. Padahal",
                    "hampir semua aplikasi perlu tahu siapa yang sedang login. Bab ini",
                    "membahas autentikasi, yaitu memastikan \"kamu memang orang yang kamu",
                    "akui\". Pertanyaan berikutnya, \"kamu boleh melakukan apa\", disebut",
                    "otorisasi dan dibahas di bab berikutnya.",
                    "",
                    "Ada dua keluarga besar cara mengingat pengguna. Pertama, sesi: server",
                    "menyimpan catatan login, dan browser cuma memegang nomor tiketnya di",
                    "cookie. Kedua, token: klien memegang bukti yang bisa diperiksa server,",
                    "dibahas di materi berikutnya. Untuk aplikasi web biasa yang dibuka di",
                    "browser, sesi dengan cookie masih jadi pilihan paling aman dan paling",
                    "sederhana.",
                ],
            },
            {
                "heading": "Alur login berbasis sesi",
                "body": [
                    "  1. Pengguna mengirim nama dan sandi ke POST /login.",
                    "  2. Server mencocokkan sandi dengan hash yang tersimpan.",
                    "  3. Kalau cocok, server membuat id sesi acak, menyimpan \"id ini milik",
                    "     budi, berlaku sampai jam sekian\" di penyimpan sesi, lalu membalas",
                    "     dengan header Set-Cookie.",
                    "  4. Browser menyimpan cookie itu dan otomatis mengirimkannya di header",
                    "     Cookie pada setiap permintaan berikutnya ke situs yang sama.",
                    "  5. Server membaca id sesi dari cookie, mencarinya di penyimpan sesi,",
                    "     dan tahu siapa penggunanya.",
                    "  6. Saat logout, server menghapus sesinya. Cookie di browser jadi nggak",
                    "     berarti apa-apa lagi.",
                    "",
                    "Penyimpan sesi bisa berupa memori (cuma cocok untuk satu server), tabel",
                    "database, atau Redis, yang dibahas di bab Cache, Antrean, dan Message",
                    "Broker. Karena catatannya di server, sesi bisa dicabut kapan saja,",
                    "misalnya saat pengguna mengganti sandi.",
                ],
            },
            {
                "heading": "Atribut cookie yang wajib kamu kenal",
                "body": [
                    "  - HttpOnly: JavaScript di halaman nggak bisa membaca cookie ini. Kalau",
                    "    ada celah XSS, skrip penyerang tetap nggak bisa mencuri id sesi.",
                    "  - Secure: cookie cuma dikirim lewat HTTPS, jadi nggak bocor di Wi-Fi",
                    "    umum.",
                    "  - SameSite=Lax: cookie nggak ikut terkirim saat situs lain mengirim",
                    "    form POST ke situsmu. Ini lapisan pertama melawan CSRF (cross-site",
                    "    request forgery), yaitu situs jahat yang membuat browser korban",
                    "    mengirim permintaan atas namanya. Strict lebih ketat lagi, None",
                    "    mematikannya (dan wajib dipasangkan dengan Secure).",
                    "  - Max-Age atau Expires: umur cookie. Tanpa keduanya, cookie hilang",
                    "    saat browser ditutup.",
                    "  - Path dan Domain: di mana cookie berlaku. Hati-hati dengan Domain,",
                    "    karena memasangnya membuat cookie ikut terkirim ke semua subdomain.",
                    "",
                    "Form yang mengubah data sebaiknya tetap memakai token CSRF. Framework",
                    "sudah menyediakannya: {% csrf_token %} di Django, @csrf di Laravel, dan",
                    "authenticity token di Rails.",
                    "",
                    "Jebakan: lupa mengganti id sesi saat login. Kalau penyerang berhasil",
                    "menanamkan id sesi tertentu di browser korban sebelum korban login, lalu",
                    "id itu tetap dipakai sesudah login, penyerang ikut masuk. Serangan ini",
                    "disebut session fixation, dan obatnya selalu membuat id baru setiap kali",
                    "login berhasil. Latihan bab ini memintamu melakukannya.",
                ],
            },
            {
                "heading": "Menyimpan kata sandi",
                "body": [
                    "Sandi nggak boleh disimpan apa adanya, dan nggak boleh cuma di-hash",
                    "dengan MD5, SHA-1, atau SHA-256. Fungsi-fungsi itu dirancang cepat, dan",
                    "GPU modern bisa mencoba miliaran hash MD5 per detik. Kalau database",
                    "bocor, sandi yang lemah ketemu dalam hitungan menit. MD5 dan SHA-1 juga",
                    "sudah usang untuk tanda tangan digital. SHA-256 tetap dipakai untuk",
                    "memeriksa keutuhan berkas dan untuk HMAC, tapi bukan untuk sandi.",
                    "",
                    "Yang dipakai adalah fungsi hash sandi yang sengaja lambat dan memakai",
                    "garam (salt): data acak yang berbeda untuk tiap pengguna dan disimpan",
                    "bersama hasilnya. Garam membuat dua pengguna dengan sandi sama punya",
                    "hash berbeda, sehingga tabel tebakan yang disiapkan sebelumnya nggak",
                    "berguna. Urutan rekomendasi OWASP (Password Storage Cheat Sheet):",
                    "",
                    "  - Argon2id, pemenang Password Hashing Competition 2015 dan dibakukan",
                    "    di RFC 9106 (2021). Minimal memori 19 MiB, 2 iterasi, 1 paralel.",
                    "  - scrypt (RFC 7914), kalau Argon2id nggak tersedia. Minimal N=2^17,",
                    "    r=8, p=1.",
                    "  - bcrypt, untuk sistem lama, dengan work factor minimal 10. Batas",
                    "    inputnya 72 byte; sisanya dipotong tanpa peringatan.",
                    "  - PBKDF2-HMAC-SHA256 (RFC 8018) dengan 600.000 iterasi, kalau aturan",
                    "    kepatuhan mewajibkan algoritma yang disetujui FIPS.",
                    "",
                    "Kabar baiknya, kamu hampir nggak pernah menulis ini sendiri. Django",
                    "memakai PBKDF2 secara bawaan, Laravel bcrypt, dan Spring Security",
                    "memakai DelegatingPasswordEncoder yang menyimpan nama algoritma di depan",
                    "hash. Contoh di bawah memakai scrypt dari pustaka standar Python supaya",
                    "bisa dijalankan di sini.",
                ],
            },
            {
                "heading": "Hash sandi dan cookie sesi dengan pustaka standar",
                "code": """import hashlib
import hmac
from http.cookies import SimpleCookie


def hash_sandi(sandi, garam):
    kunci = hashlib.scrypt(sandi.encode(), salt=garam, n=2**14, r=8, p=1, dklen=32)
    return f"scrypt${2**14}$8$1${garam.hex()}${kunci.hex()}"


def cocok(sandi, tersimpan):
    _, n, r, p, garam, kunci = tersimpan.split("$")
    uji = hashlib.scrypt(sandi.encode(), salt=bytes.fromhex(garam),
                         n=int(n), r=int(r), p=int(p), dklen=32)
    return hmac.compare_digest(uji.hex(), kunci)


# Di aplikasi nyata garam dibuat dengan os.urandom(16), berbeda tiap pengguna.
garam = bytes.fromhex("8f3a1c2b9d0e4f5a6b7c8d9e0f1a2b3c")
tersimpan = hash_sandi("kopi-susu-2026", garam)
print(tersimpan[:45] + "...")
print("sandi benar:", cocok("kopi-susu-2026", tersimpan))
print("sandi salah:", cocok("kopi-susu-2025", tersimpan))

# Di aplikasi nyata id sesi dibuat dengan secrets.token_urlsafe(32).
kue = SimpleCookie()
kue["sid"] = "a1b2"
kue["sid"].update({"httponly": True, "secure": True, "samesite": "Lax",
                   "path": "/", "max-age": 1800})
print(kue.output())""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  scrypt$16384$8$1$8f3a1c2b9d0e4f5a6b7c8d9e0f1a...",
                    "  sandi benar: True",
                    "  sandi salah: False",
                    "  Set-Cookie: sid=a1b2; HttpOnly; Max-Age=1800; Path=/; SameSite=Lax; Secure",
                    "",
                    "Hasil hash menyimpan semua parameternya: nama algoritma, N, r, p, garam,",
                    "lalu hash-nya. Dengan begitu kamu bisa menaikkan parameter di kemudian",
                    "hari tanpa mematahkan sandi lama; saat pengguna login dengan sandi lama,",
                    "hitung ulang dengan parameter baru lalu simpan. Contoh ini memakai",
                    "N=2^14 supaya cepat jalan di aplikasi; di produksi ikuti angka",
                    "rekomendasi di atas.",
                    "",
                    "hmac.compare_digest membandingkan dua nilai dalam waktu yang sama berapa",
                    "pun huruf yang cocok. Perbandingan biasa dengan == berhenti di huruf",
                    "pertama yang beda, dan selisih waktu kecil itu bisa diukur penyerang.",
                    "Baris terakhir adalah header Set-Cookie yang dibuat modul http.cookies,",
                    "lengkap dengan keempat atribut penting.",
                    "",
                    "Aturan cookie sendiri dibakukan di RFC 6265 (April 2011), dan revisinya,",
                    "RFC 6265bis, masih berupa draf saat materi ini ditulis (Oktober 2026).",
                    "Pembahasan dari sisi penyerang ada di kurikulum Keamanan Siber.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Login berbasis sesi dan cookie dipakai di hampir semua aplikasi web yang",
                    "dirender server: portal akademik, internet banking versi web, panel",
                    "admin toko, dan dasbor internal kantor.",
                    "",
                    "Kasus kecil: aplikasi absensi sekolahmu menyimpan sandi guru dengan MD5,",
                    "dan kepala sekolah minta diperbaiki tanpa memaksa semua guru membuat",
                    "sandi baru hari itu juga.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tambahkan kolom penanda algoritma, lalu bungkus hash MD5 lama",
                    "     dengan hash lambat: simpan scrypt(md5(sandi)) beserta garamnya,",
                    "     sehingga semua akun langsung terlindungi.",
                    "  2. Saat guru login, periksa dengan cara yang sama, lalu hitung ulang",
                    "     hash dari sandi aslinya dengan Argon2id atau scrypt murni dan",
                    "     simpan sebagai format baru.",
                    "  3. Pastikan cookie sesinya memakai HttpOnly, Secure, dan SameSite=Lax,",
                    "     dan id sesi diganti setiap kali login.",
                    "  4. Setelah beberapa bulan, paksa reset sandi untuk akun yang masih",
                    "     memakai format lama.",
                ],
            },
        ],
    },
    {
        "title": "37. Basic Auth, API Key, Token Bearer, dan JWT",
        "sections": [
            {
                "body": [
                    "Cookie paling enak untuk browser. Klien lain, seperti aplikasi seluler,",
                    "skrip, atau server lain yang memanggil API-mu, biasanya membawa bukti",
                    "identitasnya sendiri di header Authorization. Ada beberapa skema, dan",
                    "masing-masing cocok untuk keadaan yang berbeda.",
                ],
            },
            {
                "heading": "Basic Auth dan API key",
                "body": [
                    "HTTP Basic Authentication (RFC 7617) adalah yang paling sederhana: nama",
                    "dan sandi digabung dengan titik dua, dikodekan base64, lalu dikirim di",
                    "setiap permintaan sebagai Authorization: Basic .... Base64 cuma",
                    "pengodean, bukan enkripsi; siapa pun yang melihat headernya bisa",
                    "membaliknya dalam satu baris. Karena itu Basic Auth hanya boleh lewat",
                    "HTTPS, dan cocoknya untuk alat internal atau pengujian.",
                    "",
                    "API key adalah string rahasia yang mengenali aplikasi pemanggil, bukan",
                    "orangnya. Biasanya dikirim di header khusus seperti x-api-key. Aturan",
                    "merawatnya:",
                    "",
                    "  - Simpan hash-nya di database, bukan nilai aslinya, dan tampilkan",
                    "    nilai asli sekali saja saat dibuat.",
                    "  - Beri awalan yang mudah dikenali, misalnya tk_live_, supaya kunci",
                    "    yang bocor di repositori publik mudah dipindai.",
                    "  - Batasi wewenang tiap kunci dan sediakan cara mencabut serta",
                    "    menggantinya.",
                    "  - Jangan pernah menaruh API key rahasia di kode frontend atau aplikasi",
                    "    seluler; siapa pun bisa membongkarnya.",
                ],
            },
            {
                "heading": "Token bearer",
                "body": [
                    "Skema bearer (RFC 6750) artinya \"siapa pun yang memegang token ini",
                    "dianggap berhak\", seperti tiket konser. Klien mengirim Authorization:",
                    "Bearer <token>. Tokennya bisa berupa string acak tanpa arti (opaque)",
                    "yang dicari server di database, mirip id sesi, atau berupa JWT yang",
                    "isinya bisa diperiksa tanpa melihat database. Token Sanctum di bab",
                    "Laravel termasuk jenis pertama. Karena pemegangnya dianggap berhak,",
                    "token bearer wajib dikirim lewat HTTPS dan diberi umur.",
                ],
            },
            {
                "heading": "JWT dari dekat",
                "code": """import base64
import hashlib
import hmac
import json

# Basic Auth: base64 cuma pengodean, siapa pun bisa membaliknya
header = "Basic " + base64.b64encode(b"budi:rahasia1").decode()
print(header)
print(base64.b64decode(header.split()[1]).decode())


def b64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def tanda_tangan(kunci, teks):
    return b64url(hmac.new(kunci, teks.encode(), hashlib.sha256).digest())


kunci = b"contoh-saja-pakai-32-byte-acak-di-produksi"
kepala = b64url(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
isi = b64url(json.dumps({"sub": "42", "peran": "kasir", "exp": 1700000900}).encode())
token = f"{kepala}.{isi}.{tanda_tangan(kunci, kepala + '.' + isi)}"
print(token.count("."), "titik, panjang", len(token))

# Payload bisa dibaca siapa saja tanpa kunci
print(base64.urlsafe_b64decode(isi + "=" * (-len(isi) % 4)).decode())


def sah(tok):
    k, i, t = tok.split(".")
    return hmac.compare_digest(tanda_tangan(kunci, k + "." + i), t)


palsu = b64url(json.dumps({"sub": "42", "peran": "admin", "exp": 1700000900}).encode())
ttd = token.split(".")[2]
print("asli :", sah(token))
print("palsu:", sah(f"{kepala}.{palsu}.{ttd}"))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Basic YnVkaTpyYWhhc2lhMQ==",
                    "  budi:rahasia1",
                    "  2 titik, panjang 152",
                    "  {\"sub\": \"42\", \"peran\": \"kasir\", \"exp\": 1700000900}",
                    "  asli : True",
                    "  palsu: False",
                    "",
                    "JWT (JSON Web Token, RFC 7519) terdiri dari tiga bagian yang dipisah",
                    "titik: header, payload, dan signature, masing-masing dikodekan base64url",
                    "tanpa tanda = di ujung. Header menyebut algoritmanya. Payload berisi",
                    "klaim seperti sub (subjek, biasanya id pengguna), exp (waktu kedaluwarsa",
                    "dalam detik sejak 1970), iat (waktu dibuat), iss (penerbit), dan aud",
                    "(untuk siapa token itu). Signature HS256 adalah HMAC-SHA256 dari header",
                    "dan payload dengan kunci rahasia.",
                    "",
                    "Perhatikan dua hal dari keluaran tadi. Payload bisa dibaca siapa saja",
                    "tanpa kunci, jadi jangan menaruh data rahasia di sana. Mengubah satu",
                    "huruf payload, misalnya peran kasir jadi admin, membuat tanda tangannya",
                    "nggak cocok lagi, dan itulah yang membuat server bisa memercayai isinya",
                    "tanpa menyimpan sesi.",
                ],
            },
            {
                "heading": "Risiko JWT",
                "body": [
                    "  - alg none: token tanpa tanda tangan. Pustaka yang membaca algoritma",
                    "    dari header token lalu menurutinya bisa menerima token palsu. Selalu",
                    "    tentukan algoritma yang boleh di sisi server.",
                    "  - Kebingungan algoritma: server yang memakai RS256 (kunci publik) bisa",
                    "    dibohongi token HS256 yang ditandatangani dengan kunci publiknya",
                    "    sendiri, kalau algoritmanya nggak dikunci.",
                    "  - Kunci HS256 yang lemah bisa ditebak secara offline dari satu token",
                    "    saja. Pakai minimal 32 byte acak.",
                    "  - Nggak bisa dicabut. JWT tetap sah sampai exp, walau penggunanya",
                    "    sudah logout atau diblokir. Obatnya umur pendek (misalnya 15 menit)",
                    "    ditambah refresh token yang disimpan dan bisa dicabut di server,",
                    "    atau daftar hitam berdasarkan klaim jti.",
                    "",
                    "Praktik terbaiknya dikumpulkan di RFC 8725. Satu lagi pertanyaan klasik:",
                    "token disimpan di mana di browser? localStorage bisa dibaca skrip XSS,",
                    "sedangkan cookie HttpOnly nggak bisa. Begitu kamu menyimpan JWT di",
                    "cookie HttpOnly, kamu sudah kembali ke model sesi, dengan token yang",
                    "lebih besar.",
                ],
            },
            {
                "heading": "JWT di Node.js",
                "bahasa": "javascript",
                "code": """const jwt = require('jsonwebtoken');

const rahasia = process.env.JWT_RAHASIA;
const token = jwt.sign({ sub: '42', peran: 'kasir' }, rahasia, {
  algorithm: 'HS256',
  expiresIn: '15m',
});

const isi = jwt.verify(token, rahasia, { algorithms: ['HS256'] });
console.log(isi.sub, isi.peran);""",
            },
            {
                "body": [
                    "jsonwebtoken adalah pustaka npm paling umum untuk JWT di Node.js,",
                    "dirawat Auth0, versi 9.0.3 (Desember 2025), lisensi MIT. Jebakan yang",
                    "sering terjadi: memanggil verify tanpa opsi algorithms. Alternatif yang",
                    "lebih modern adalah pustaka jose, yang memakai Web Crypto sehingga jalan",
                    "juga di runtime edge. Di Python padanannya PyJWT, di Java pustaka",
                    "seperti jjwt atau Nimbus, tapi untuk latihan bab ini kamu membuatnya",
                    "sendiri dengan hmac dan base64.",
                ],
            },
            {
                "heading": "Sesi atau token?",
                "body": [
                    "                       sesi + cookie           JWT",
                    "  disimpan di          server                  klien",
                    "  bisa dicabut         kapan saja              tunggu exp (atau daftar hitam)",
                    "  cocok untuk          web di browser          API seluler, antar layanan",
                    "  ukuran per request   id pendek               ratusan byte",
                    "  risiko utama         CSRF                    kunci bocor, alg salah",
                    "",
                    "Aturan praktisnya: aplikasi web biasa pakai sesi. API untuk aplikasi",
                    "seluler milikmu sendiri bisa pakai token opaque atau JWT berumur pendek.",
                    "JWT paling berguna saat banyak layanan perlu memeriksa identitas tanpa",
                    "bertanya ke satu database pusat, dan itu juga cara kerja OpenID Connect",
                    "di bab berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "API key dipakai hampir semua layanan pihak ketiga seperti gerbang",
                    "pembayaran dan layanan pengiriman pesan, sedangkan JWT dipakai sebagai",
                    "token akses di aplikasi seluler dan di sistem login tunggal.",
                    "",
                    "Kasus kecil: aplikasi kasir Android memakai JWT tanpa exp, dan salah",
                    "satu ponsel kasir hilang. Token di ponsel itu masih bisa dipakai untuk",
                    "mencatat transaksi.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Ganti kunci HS256 di server sekarang juga; semua token lama",
                    "     langsung ditolak, termasuk yang ada di ponsel hilang.",
                    "  2. Ubah penerbitan token: access token berumur 15 menit plus refresh",
                    "     token yang disimpan di tabel dan bisa dicabut per perangkat.",
                    "  3. Tambahkan exp dan pastikan verifikasi menolak token yang sudah",
                    "     lewat waktunya, dengan algoritma dikunci ke HS256.",
                    "  4. Sediakan tombol \"keluar dari semua perangkat\" yang menghapus semua",
                    "     refresh token milik pengguna itu.",
                ],
            },
        ],
    },
    {
        "title": "38. Peta Pustaka Autentikasi per Framework",
        "sections": [
            {
                "body": [
                    "Menulis autentikasi sendiri dari nol jarang jadi pilihan yang baik.",
                    "Setiap framework punya pustaka bawaan atau pustaka yang sudah jadi",
                    "standar, dan pustaka itu sudah memikirkan hash sandi, token CSRF, reset",
                    "sandi, dan banyak celah yang mungkin belum terpikir olehmu. Tabel ini",
                    "per Oktober 2026.",
                ],
            },
            {
                "heading": "Tabel perbandingan",
                "bahasa": "teks",
                "code": """Pustaka               Untuk              Versi        Status
Spring Security       Spring             7.1.1        aktif
ASP.NET Core Identity ASP.NET Core       bagian 10.x  aktif
Devise                Rails              5.0.4        aktif
django-allauth        Django             65.20.0      aktif
Laravel Sanctum       Laravel            (bab 08)     aktif
Passport.js           Express/Node.js    0.7.0        stabil, rilis terakhir 2023
Better Auth           TypeScript         1.7.11       aktif, tumbuh cepat
Auth.js (NextAuth)    Next.js dan JS     4.24.15      pemeliharaan saja
Lucia                 TypeScript         3.2.2        usang, kini panduan""",
            },
            {
                "heading": "Framework besar",
                "body": [
                    "Spring Security adalah kerangka autentikasi dan otorisasi standar di",
                    "Spring: rantai filter, login form, OAuth2 dan OIDC, serta resource",
                    "server JWT. Versi 7 menyertai Spring Boot 4. Jebakannya ada di tutorial",
                    "lama: kelas WebSecurityConfigurerAdapter sudah dihapus. Konfigurasinya",
                    "sekarang berupa bean SecurityFilterChain:",
                    "",
                    "  @Bean",
                    "  SecurityFilterChain filterChain(HttpSecurity http) throws Exception {",
                    "      http",
                    "          .authorizeHttpRequests(auth -> auth",
                    "              .requestMatchers(\"/api/publik/**\").permitAll()",
                    "              .anyRequest().authenticated())",
                    "          .oauth2ResourceServer(oauth ->",
                    "              oauth.jwt(Customizer.withDefaults()));",
                    "      return http.build();",
                    "  }",
                    "",
                    "ASP.NET Core Identity adalah sistem keanggotaan bawaan ASP.NET Core:",
                    "pengguna, sandi, peran, 2FA, dan sejak .NET 8 endpoint API identitas",
                    "siap pakai lewat MapIdentityApi. Ia sudah termasuk di SDK, jadi nggak",
                    "perlu paket pihak ketiga.",
                    "",
                    "Devise adalah solusi autentikasi paling populer di Rails: registrasi,",
                    "login, reset sandi, konfirmasi email. Rails 8 kini punya generator",
                    "autentikasi bawaan sebagai alternatif yang lebih ringan. Untuk otorisasi",
                    "di Rails, pasangannya biasanya Pundit atau CanCanCan.",
                    "",
                    "django-allauth menambah registrasi, login lewat akun sosial (OAuth dan",
                    "OIDC), dan MFA ke Django, di atas sistem auth bawaan Django. Untuk API",
                    "dengan DRF, orang sering menambah djangorestframework-simplejwt. Di",
                    "Laravel, pilihannya Sanctum atau Passport, seperti di bab 08.",
                ],
            },
            {
                "heading": "Dunia JavaScript dan TypeScript",
                "body": [
                    "Passport.js adalah middleware autentikasi untuk Express dengan ratusan",
                    "strategi: lokal (nama dan sandi), JWT, Google, GitHub, sampai SAML.",
                    "Rilis terakhirnya 0.7.0 pada November 2023, tapi masih umum di proyek",
                    "Express.",
                    "",
                    "Auth.js (dulu NextAuth.js) lama jadi pilihan utama untuk Next.js. Sejak",
                    "22 September 2025 proyek ini dikelola tim Better Auth dalam mode",
                    "pemeliharaan: cuma tambalan keamanan, tanpa fitur baru, dan versi 5-nya",
                    "nggak pernah keluar dari beta. Proyek baru disarankan memakai Better",
                    "Auth, pustaka TypeScript lengkap (email dan sandi, OAuth, passkey, 2FA,",
                    "organisasi) yang dipasang di backend-mu sendiri dan nggak terikat satu",
                    "framework:",
                    "",
                    "  import { betterAuth } from \"better-auth\";",
                    "",
                    "  export const auth = betterAuth({",
                    "    database: ...,",
                    "    emailAndPassword: { enabled: true },",
                    "    socialProviders: {",
                    "      github: {",
                    "        clientId: process.env.GITHUB_CLIENT_ID,",
                    "        clientSecret: process.env.GITHUB_CLIENT_SECRET,",
                    "      },",
                    "    },",
                    "  });",
                    "",
                    "Lucia pernah populer sebagai pustaka sesi TypeScript, tapi paket npm-nya",
                    "kini ditandai deprecated. Situsnya berubah jadi panduan cara membangun",
                    "sesi sendiri, dan justru bagus dibaca untuk memahami konsep di materi",
                    "pertama bab ini.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  1. Pakai pustaka bawaan framework-mu dulu: Spring Security, ASP.NET",
                    "     Core Identity, sistem auth Django, Laravel, atau generator Rails 8.",
                    "  2. Butuh login sosial dan MFA di Django atau Rails: django-allauth",
                    "     atau Devise.",
                    "  3. Proyek TypeScript baru: Better Auth. Proyek Auth.js yang sudah",
                    "     jalan boleh dirawat, tapi rencanakan pindah.",
                    "  4. Butuh banyak aplikasi berbagi satu login, atau login lewat kantor:",
                    "     layanan identitas dan SSO, dibahas di bab berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua aplikasi produksi memakai pustaka auth yang sudah matang:",
                    "portal kampus berbasis Django dengan allauth, aplikasi SaaS Rails dengan",
                    "Devise, dan sistem perbankan Spring dengan Spring Security.",
                    "",
                    "Kasus kecil: proyek Next.js di tempat PKL-mu memakai Auth.js versi 4,",
                    "dan tim bertanya apakah perlu pindah sekarang.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek versi persis di package.json dan pastikan sudah memakai rilis",
                    "     4.24 terbaru yang masih mendapat tambalan keamanan.",
                    "  2. Catat fitur yang dipakai: provider OAuth, login email, adapter",
                    "     database, dan callback khusus.",
                    "  3. Coba Better Auth di cabang terpisah untuk satu provider dulu, dan",
                    "     bandingkan bentuk tabel penggunanya.",
                    "  4. Jadwalkan migrasi saat ada fitur auth baru yang harus dibangun,",
                    "     supaya kerjanya nggak dua kali.",
                ],
            },
        ],
    },
    {
        "title": "39. OAuth 2.0 dan PKCE: Izin Tanpa Kata Sandi",
        "sections": [
            {
                "body": [
                    "Bayangkan kamu bikin aplikasi pengingat jadwal. Supaya bisa mengingatkan",
                    "rapat, aplikasimu perlu membaca kalender Google milik pengguna. Cara",
                    "paling gampang kelihatannya begini: minta pengguna mengetik email dan",
                    "kata sandi Google-nya, lalu aplikasimu login atas namanya.",
                    "",
                    "Cara itu berbahaya. Aplikasimu jadi pegang kunci seluruh akun: email,",
                    "foto, dokumen, semuanya. Pengguna nggak bisa membatasi izinnya cuma ke",
                    "kalender, dan satu-satunya cara mencabut akses adalah mengganti kata",
                    "sandi, yang sekaligus memutus semua aplikasi lain.",
                    "",
                    "OAuth 2.0 lahir untuk masalah ini. Pengguna login langsung di halaman",
                    "Google, bukan di aplikasimu. Google lalu memberi aplikasimu access",
                    "token, yaitu semacam kartu akses yang cuma berlaku untuk izin tertentu",
                    "dan untuk waktu terbatas. Kata sandinya nggak pernah lewat aplikasimu.",
                    "",
                    "OAuth 2.0 ditetapkan di RFC 6749 (Oktober 2012). Ia mengatur otorisasi,",
                    "yaitu urusan \"boleh mengakses apa\". Urusan \"pengguna ini siapa\"",
                    "diselesaikan lapisan di atasnya, OpenID Connect, yang dibahas di materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Empat pihak dalam OAuth",
                "body": [
                    "Istilah OAuth terdengar berat, padahal pihaknya cuma empat:",
                    "",
                    "  - Resource owner: pemilik data, yaitu pengguna.",
                    "  - Client: aplikasi yang minta akses, yaitu aplikasi pengingat",
                    "    jadwalmu.",
                    "  - Authorization server: server yang memeriksa login dan menerbitkan",
                    "    token, misalnya accounts.google.com.",
                    "  - Resource server: API yang menyimpan datanya, misalnya API Google",
                    "    Calendar.",
                    "",
                    "Izin yang diminta ditulis sebagai scope, yaitu daftar kata yang",
                    "disepakati authorization server, misalnya calendar.readonly. Access",
                    "token biasanya berumur pendek, hitungan menit sampai satu jam. Supaya",
                    "pengguna nggak perlu login ulang terus, server bisa ikut memberi refresh",
                    "token yang dipakai untuk meminta access token baru.",
                    "",
                    "Client juga dibedakan jadi dua jenis. Confidential client punya tempat",
                    "aman untuk menyimpan rahasia (client secret), misalnya backend di",
                    "server. Public client nggak punya tempat seperti itu: aplikasi mobile",
                    "dan aplikasi JavaScript di browser bisa dibongkar siapa saja, jadi",
                    "rahasia apa pun di dalamnya bisa dicuri.",
                ],
            },
            {
                "heading": "Authorization code flow",
                "body": [
                    "Flow (alur) yang dipakai hampir semua aplikasi sekarang adalah",
                    "authorization code flow. Urutannya:",
                    "",
                    "  1. Aplikasi mengarahkan browser pengguna ke halaman /authorize milik",
                    "     authorization server, membawa client_id, redirect_uri, scope, dan",
                    "     state.",
                    "  2. Pengguna login dan menyetujui izinnya di halaman itu.",
                    "  3. Authorization server mengarahkan browser kembali ke redirect_uri",
                    "     aplikasi sambil membawa code, yaitu kode sekali pakai yang berumur",
                    "     pendek.",
                    "  4. Backend aplikasi menukar code itu dengan access token lewat",
                    "     permintaan POST ke /token. Pertukaran ini terjadi antar-server,",
                    "     nggak lewat browser.",
                    "  5. Aplikasi memanggil API dengan header Authorization: Bearer diikuti",
                    "     tokennya.",
                    "",
                    "Parameter state adalah nilai acak yang disimpan aplikasi sebelum langkah",
                    "1 lalu dicocokkan di langkah 3. Tanpa state, penyerang bisa menyodorkan",
                    "code miliknya sendiri ke aplikasimu, sehingga korban tanpa sadar",
                    "tersambung ke akun penyerang.",
                ],
            },
            {
                "heading": "Dua permintaan pentingnya",
                "bahasa": "http",
                "code": """GET /authorize?response_type=code&client_id=pengingat-app
    &redirect_uri=https%3A%2F%2Fpengingat.example%2Fcallback
    &scope=openid%20calendar.readonly&state=af0ifjsldkj
    &code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
    &code_challenge_method=S256 HTTP/1.1
Host: auth.example.com

POST /token HTTP/1.1
Host: auth.example.com
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA
&redirect_uri=https%3A%2F%2Fpengingat.example%2Fcallback
&client_id=pengingat-app
&code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk""",
            },
            {
                "heading": "PKCE: pengaman untuk code",
                "body": [
                    "Di langkah 3, code lewat browser sebagai bagian URL. Di ponsel, aplikasi",
                    "jahat bisa mendaftarkan skema URL yang sama lalu mencegat code itu.",
                    "Kalau penukaran code cuma butuh client_id yang memang publik, pencuri",
                    "code bisa langsung mendapat token.",
                    "",
                    "Pengaman bernama Proof Key for Code Exchange (RFC 7636), disingkat",
                    "seperti judul bagian ini dan dibaca \"piksi\", menutup celah itu. Sebelum",
                    "langkah 1, aplikasi membuat code_verifier, yaitu string acak 43 sampai",
                    "128 karakter. Ia mengirim hash SHA-256 dari string itu sebagai",
                    "code_challenge. Waktu menukar code di langkah 4, aplikasi wajib",
                    "menyertakan code_verifier aslinya. Server menghitung ulang hash-nya, dan",
                    "kalau nggak cocok, penukaran ditolak. Pencuri code nggak punya verifier,",
                    "jadi code curiannya nggak berguna.",
                    "",
                    "Program di bawah memakai contoh dari Appendix B RFC 7636. Verifier-nya",
                    "dipatok supaya hasilnya bisa kamu cocokkan dengan RFC; di aplikasi",
                    "sungguhan verifier dibuat dengan secrets.token_urlsafe(32).",
                ],
            },
            {
                "heading": "Menghitung code_challenge",
                "code": """import base64
import hashlib
from urllib.parse import urlencode

verifier = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
digest = hashlib.sha256(verifier.encode("ascii")).digest()
challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
print("challenge:", challenge)

parameter = {
    "response_type": "code",
    "client_id": "pengingat-app",
    "redirect_uri": "https://pengingat.example/callback",
    "scope": "openid calendar.readonly",
    "state": "af0ifjsldkj",
    "code_challenge": challenge,
    "code_challenge_method": "S256",
}
url = "https://auth.example.com/authorize?" + urlencode(parameter)
for potong in url.split("&"):
    print(potong)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  challenge: E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
                    "  https://auth.example.com/authorize?response_type=code",
                    "  client_id=pengingat-app",
                    "  redirect_uri=https%3A%2F%2Fpengingat.example%2Fcallback",
                    "  scope=openid+calendar.readonly",
                    "  state=af0ifjsldkj",
                    "  code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
                    "  code_challenge_method=S256",
                    "",
                    "Base64 di sini memakai varian urlsafe tanpa tanda = di ujung, karena",
                    "hasilnya ditaruh di URL. Lupa membuang = adalah penyebab paling umum",
                    "penukaran code ditolak server.",
                ],
            },
            {
                "heading": "Flow yang sudah usang dan OAuth 2.1",
                "body": [
                    "RFC 6749 menyebut beberapa flow lain. Sebagian sudah nggak boleh dipakai",
                    "untuk aplikasi baru:",
                    "",
                    "  - Implicit flow: token langsung dikirim di URL tanpa tahap penukaran",
                    "    code. Token jadi tercatat di riwayat browser dan log. Usang, ganti",
                    "    dengan authorization code beserta code_verifier.",
                    "  - Resource owner password credentials: aplikasi menerima kata sandi",
                    "    pengguna lalu menukarnya dengan token. Ini mengulang masalah yang",
                    "    mau dihapus OAuth. Usang.",
                    "  - Client credentials: aplikasi meminta token atas nama dirinya",
                    "    sendiri, tanpa pengguna. Masih dipakai untuk komunikasi",
                    "    antar-server, misalnya layanan laporan memanggil layanan pembayaran.",
                    "  - Device authorization grant (RFC 8628): untuk perangkat tanpa",
                    "    keyboard seperti smart TV. Layar menampilkan kode pendek, pengguna",
                    "    memasukkannya di ponsel.",
                    "",
                    "Praktik keamanan terbaru dikumpulkan di RFC 9700, OAuth 2.0 Security",
                    "Best Current Practice, yang terbit Januari 2025. Isinya lalu dirangkum",
                    "jadi OAuth 2.1: code_verifier wajib untuk semua client, implicit dan",
                    "password grant dihapus, redirect_uri harus cocok persis, dan refresh",
                    "token untuk public client harus dirotasi atau diikat ke pengirimnya.",
                    "Saat materi ini ditulis (Oktober 2026), OAuth 2.1 masih draf IETF",
                    "(draft-ietf-oauth-v2-1-16, September 2026) dengan target diajukan ke",
                    "badan pengarah IETF pada Desember 2026. Status draf nggak berarti boleh",
                    "diabaikan: isinya sudah jadi cara yang benar memakai OAuth hari ini.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: memakai access token sebagai bukti login. Access token",
                    "ditujukan untuk resource server, dan isinya nggak dijamin menyebut siapa",
                    "penggunanya. Aplikasi lain yang menerima token curian bisa mengira",
                    "pemegangnya adalah korban. Untuk login, pakai ID token dari OpenID",
                    "Connect.",
                    "",
                    "  - Mencocokkan redirect_uri dengan awalan saja. Penyerang bisa",
                    "    mendaftarkan https://pengingat.example.jahat.com dan menerima code",
                    "    korban. Server wajib mencocokkan string utuh.",
                    "  - Menyimpan access token di localStorage aplikasi browser. Skrip XSS",
                    "    bisa membacanya. Pola yang dianjurkan untuk aplikasi web adalah",
                    "    backend for frontend: token disimpan di server, browser cuma",
                    "    memegang cookie sesi HttpOnly.",
                    "  - Meminta scope sebanyak-banyaknya \"biar aman\". Makin besar izinnya,",
                    "    makin besar kerugian kalau token bocor, dan makin banyak pengguna",
                    "    yang menolak di layar persetujuan.",
                    "",
                    "Sisi serangan OAuth, misalnya pembajakan redirect dan pencurian token,",
                    "dibahas lebih dalam di kurikulum Keamanan Siber.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tombol \"Hubungkan dengan Google Drive\" di aplikasi desain, integrasi",
                    "GitHub di layanan CI, dan aplikasi pihak ketiga yang membaca kalender",
                    "semuanya memakai authorization code flow. Layar persetujuan yang",
                    "menyebut \"aplikasi ini ingin melihat kalendermu\" adalah langkah 2 flow",
                    "tadi, dan daftar izinnya adalah scope.",
                    "",
                    "Kasus kecil: kamu membuat aplikasi web pengingat jadwal dan ingin",
                    "membaca Google Calendar pengguna tanpa pernah menyentuh kata sandinya.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Daftarkan aplikasi di Google Cloud Console, pilih jenis aplikasi",
                    "     web, lalu isi redirect URI yang persis, misalnya",
                    "     https://pengingat.example/callback.",
                    "  2. Di backend, buat state dan code_verifier acak per login, simpan di",
                    "     sesi, lalu arahkan browser ke URL /authorize dengan scope",
                    "     calendar.readonly dan code_challenge S256.",
                    "  3. Di rute /callback, tolak permintaan kalau state berbeda dari yang",
                    "     tersimpan, lalu tukar code beserta code_verifier di endpoint token.",
                    "  4. Simpan access token dan refresh token di database server,",
                    "     terenkripsi, bukan di browser. Browser cukup memegang cookie sesi",
                    "     HttpOnly.",
                    "  5. Saat API membalas 401 karena token kedaluwarsa, minta token baru",
                    "     dengan refresh token lalu ulangi permintaannya sekali.",
                ],
            },
        ],
    },
    {
        "title": "40. OpenID Connect, SSO, dan Keycloak",
        "sections": [
            {
                "body": [
                    "OAuth menjawab \"aplikasi ini boleh mengakses apa\". Untuk tombol \"Masuk",
                    "dengan Google\", yang dibutuhkan pertanyaan lain: \"orang ini siapa\".",
                    "OpenID Connect, disingkat OIDC, menambahkan jawaban itu di atas OAuth",
                    "2.0 tanpa mengubah flow-nya.",
                    "",
                    "Caranya, aplikasi menambahkan scope openid saat memanggil /authorize. Di",
                    "langkah penukaran code, authorization server (dalam OIDC disebut OpenID",
                    "Provider) mengembalikan satu benda tambahan: ID token. ID token adalah",
                    "JWT, format token yang sudah kamu pelajari di materi Basic Auth, API",
                    "Key, Token Bearer, dan JWT. Isinya pernyataan tentang pengguna yang",
                    "ditandatangani provider.",
                    "",
                    "Spesifikasi yang berlaku adalah OpenID Connect Core 1.0 (incorporating",
                    "errata set 2, Desember 2023), yang juga sudah diterbitkan sebagai",
                    "standar internasional ISO.",
                ],
            },
            {
                "heading": "Isi ID token",
                "body": [
                    "Bagian tengah (payload) ID token berisi klaim, yaitu pasangan nama dan",
                    "nilai. Yang wajib kamu periksa:",
                    "",
                    "  - iss (issuer): siapa penerbitnya. Harus persis alamat provider yang",
                    "    kamu percaya.",
                    "  - aud (audience): untuk siapa token ini. Harus memuat client_id",
                    "    aplikasimu. Token yang diterbitkan untuk aplikasi lain jangan",
                    "    diterima.",
                    "  - exp dan iat: kapan kedaluwarsa dan kapan dibuat, dalam detik sejak 1",
                    "    Januari 1970 (Unix time).",
                    "  - sub (subject): ID unik pengguna di provider itu. Pakai sub, bukan",
                    "    email, sebagai kunci akun, karena email bisa berganti.",
                    "  - nonce: nilai acak yang dikirim aplikasi saat /authorize. Kalau nonce",
                    "    di token berbeda dengan yang tersimpan di sesi, token itu hasil",
                    "    putar ulang (replay).",
                    "",
                    "Sebelum membaca klaim apa pun, tanda tangan token wajib diverifikasi",
                    "dengan kunci publik provider. Provider menerbitkan kunci-kuncinya di",
                    "alamat jwks_uri, dan semua alamat penting tercantum di dokumen",
                    "discovery: /.well-known/openid-configuration. Pustaka seperti authlib",
                    "(Python), jose (JavaScript), dan Spring Security mengurus verifikasi",
                    "tanda tangan. Program di bawah cuma menunjukkan pemeriksaan klaim",
                    "sesudahnya.",
                ],
            },
            {
                "heading": "Memeriksa klaim ID token",
                "code": """def periksa_klaim(klaim, sekarang, harap):
    if klaim.get("iss") != harap["iss"]:
        return "ditolak: penerbit asing"
    aud = klaim.get("aud")
    daftar_aud = aud if isinstance(aud, list) else [aud]
    if harap["client_id"] not in daftar_aud:
        return "ditolak: bukan untuk aplikasi ini"
    if sekarang >= klaim.get("exp", 0):
        return "ditolak: kedaluwarsa"
    if klaim.get("nonce") != harap["nonce"]:
        return "ditolak: nonce tidak cocok"
    return "diterima, pengguna " + klaim["sub"]


harap = {"iss": "https://sso.contoh.id/realms/kantor",
         "client_id": "portal-hr", "nonce": "n-0S6_WzA2Mj"}
token = {"iss": "https://sso.contoh.id/realms/kantor", "aud": "portal-hr",
         "sub": "f81d4fae-7dec", "exp": 1760000600, "iat": 1760000000,
         "nonce": "n-0S6_WzA2Mj", "email": "budi@contoh.id"}

print(periksa_klaim(token, 1760000100, harap))
print(periksa_klaim(token, 1760000700, harap))
print(periksa_klaim(dict(token, aud="aplikasi-lain"), 1760000100, harap))
print(periksa_klaim(dict(token, nonce="lama"), 1760000100, harap))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  diterima, pengguna f81d4fae-7dec",
                    "  ditolak: kedaluwarsa",
                    "  ditolak: bukan untuk aplikasi ini",
                    "  ditolak: nonce tidak cocok",
                    "",
                    "Waktu dioper sebagai parameter sekarang, bukan dibaca dari jam komputer.",
                    "Selain membuat contoh ini selalu sama hasilnya, pola ini juga yang",
                    "membuat kode verifikasi gampang diuji.",
                ],
            },
            {
                "heading": "SSO dan Keycloak",
                "body": [
                    "Single sign-on (SSO) artinya sekali login, banyak aplikasi terbuka.",
                    "Karyawan login sekali di portal kantor, lalu aplikasi cuti, aplikasi",
                    "absensi, dan wiki internal langsung mengenalinya. Semua aplikasi itu",
                    "menjadi client OIDC dari satu provider yang sama, dan provider mengingat",
                    "sesi login di cookie miliknya sendiri.",
                    "",
                    "Keycloak adalah server identitas open source yang paling sering dipakai",
                    "untuk peran itu kalau kamu ingin menjalankannya sendiri. Ia berasal dari",
                    "Red Hat, sekarang proyek CNCF, berlisensi Apache-2.0. Di Survei Stack",
                    "Overflow 2026 (kategori Security Operations Tools), 18,6% responden",
                    "memakainya. Versi stabil terbaru saat materi ini ditulis (Oktober 2026)",
                    "adalah 26.8.1, rilis yang menambal 23 celah keamanan, jadi selalu",
                    "perbarui.",
                    "",
                    "Konsep Keycloak yang perlu kamu kenal:",
                    "",
                    "  - Realm: ruang terpisah berisi pengguna, aplikasi, dan aturan. Satu",
                    "    Keycloak bisa melayani beberapa realm, misalnya kantor dan",
                    "    pelanggan.",
                    "  - Client: aplikasi yang didaftarkan, lengkap dengan redirect URI dan",
                    "    jenisnya (publik atau rahasia).",
                    "  - User dan role: pengguna beserta peran yang akan ikut masuk ke token.",
                    "  - Identity provider: Keycloak bisa meneruskan login ke Google, GitHub,",
                    "    atau server SAML perusahaan lain.",
                    "",
                    "Alamat penerbit (iss) sebuah realm berbentuk",
                    "https://host/realms/nama-realm, dan dokumen discovery-nya ada di bawah",
                    "alamat itu.",
                ],
            },
            {
                "heading": "Menyalakan Keycloak untuk percobaan",
                "bahasa": "terminal",
                "code": "# mode pengembangan saja, jangan dipakai di produksi\ndocker run -p 127.0.0.1:8080:8080 \\\n  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin \\\n  -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin \\\n  quay.io/keycloak/keycloak:26.8.1 start-dev\n\n# sesudah membuat realm \"kantor\" di konsol admin:\ncurl http://localhost:8080/realms/kantor/.well-known/openid-configuration",
            },
            {
                "heading": "SAML, passkeys, dan 2FA",
                "body": [
                    "SAML 2.0 adalah standar SSO generasi sebelum OIDC, terbit sebagai",
                    "standar terbuka tahun 2005. Pesannya berupa dokumen XML bertanda tangan",
                    "yang dikirim lewat browser. Di dunia enterprise ia masih wajib ada,",
                    "misalnya untuk login ke aplikasi SaaS lewat direktori perusahaan. Untuk",
                    "sistem baru, pilih OIDC kalau tersedia: JSON lebih gampang diurai",
                    "daripada XML, dan OIDC juga jalan di aplikasi mobile. Keycloak bisa",
                    "berbicara dua-duanya, jadi ia sering jadi penerjemah antara aplikasi",
                    "OIDC dan perusahaan yang cuma punya SAML.",
                    "",
                    "Passkeys adalah login tanpa kata sandi berbasis standar W3C WebAuthn.",
                    "Perangkat pengguna membuat pasangan kunci: kunci privat tetap di",
                    "perangkat (dibuka dengan sidik jari, wajah, atau kode angka), kunci",
                    "publik disimpan server. Saat login, server mengirim tantangan acak dan",
                    "perangkat menandatanganinya. Karena tanda tangannya terikat ke nama",
                    "domain, halaman phishing di domain lain nggak bisa memakainya. WebAuthn",
                    "Level 3 menjadi W3C Recommendation pada 25 Agustus 2026.",
                    "",
                    "Two-factor authentication (2FA) menambah faktor kedua sesudah kata",
                    "sandi. Yang paling umum adalah TOTP (RFC 6238): aplikasi authenticator",
                    "di ponsel dan server sama-sama menyimpan satu rahasia, lalu",
                    "masing-masing menghitung kode dari rahasia itu ditambah jam sekarang",
                    "dibagi 30 detik. Kodenya cocok tanpa perlu komunikasi apa pun. TOTP",
                    "dibangun di atas HOTP (RFC 4226), yang memakai penghitung, bukan jam.",
                    "Latihan bab ini memintamu menulisnya sendiri dan mencocokkannya dengan",
                    "vektor uji resmi RFC.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: membaca klaim email di ID token lalu langsung menganggapnya",
                    "sebagai akun lokal. Beberapa provider mengizinkan email yang belum",
                    "diverifikasi. Periksa klaim email_verified, dan tautkan akun lewat",
                    "pasangan iss dan sub.",
                    "",
                    "  - Memverifikasi ID token di frontend lalu mengirim \"sudah login\" ke",
                    "    backend. Backend wajib memverifikasi sendiri.",
                    "  - Lupa logout di provider. Menghapus cookie aplikasi saja nggak cukup",
                    "    untuk SSO, karena sesi di Keycloak masih hidup dan pengguna langsung",
                    "    masuk lagi. Arahkan ke end_session_endpoint.",
                    "  - Membiarkan jam server melenceng. Pemeriksaan exp yang terlalu ketat",
                    "    menolak token yang sah. Pustaka biasanya memberi toleransi beberapa",
                    "    detik.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kampus dan perusahaan menengah sering menjalankan Keycloak atau server",
                    "sejenis supaya mahasiswa atau karyawan cukup punya satu akun untuk",
                    "portal akademik, e-learning, dan email. Aplikasi baru tinggal",
                    "didaftarkan sebagai client, tanpa membuat tabel pengguna sendiri.",
                    "",
                    "Kasus kecil: kantormu punya aplikasi cuti (Flask) dan aplikasi absensi",
                    "(Express). Atasan ingin karyawan login sekali saja, dan hanya karyawan",
                    "dengan peran hrd yang boleh menyetujui cuti.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jalankan Keycloak, buat realm kantor, lalu daftarkan dua client:",
                    "     aplikasi-cuti dan aplikasi-absensi, masing-masing dengan redirect",
                    "     URI-nya.",
                    "  2. Buat role hrd di realm, berikan ke akun yang berhak, dan pastikan",
                    "     role ikut dimasukkan ke token (client scope roles).",
                    "  3. Di kedua aplikasi, pasang pustaka OIDC dan arahkan ke alamat",
                    "     discovery https://sso.kantor/realms/kantor.",
                    "  4. Di backend, verifikasi tanda tangan, iss, aud, exp, dan nonce;",
                    "     simpan sub sebagai ID pengguna lokal.",
                    "  5. Di rute persetujuan cuti, tolak dengan 403 kalau role hrd tidak ada",
                    "     di token.",
                ],
            },
        ],
    },
    {
        "title": "41. Otorisasi, Rate Limiting, dan Celah API Umum",
        "sections": [
            {
                "body": [
                    "Autentikasi menjawab \"kamu siapa\". Otorisasi menjawab \"kamu boleh apa\".",
                    "Banyak API sudah benar di bagian pertama tapi bolong di bagian kedua:",
                    "pengguna yang sah bisa membaca atau mengubah data milik orang lain cukup",
                    "dengan mengganti angka di URL.",
                    "",
                    "Materi ini membahas tiga hal yang menjaga API tetap waras sesudah",
                    "pengguna berhasil login: model otorisasi, pembatasan laju permintaan,",
                    "dan daftar celah API yang paling sering ditemukan.",
                ],
            },
            {
                "heading": "RBAC, ABAC, dan ReBAC",
                "body": [
                    "Ada tiga cara umum memutuskan izin:",
                    "",
                    "  - RBAC (role-based access control): izin melekat pada peran. Peran",
                    "    admin boleh menghapus, peran editor boleh mengubah. Mudah",
                    "    dimengerti, cocok untuk aplikasi kantor.",
                    "  - ABAC (attribute-based access control): izin dihitung dari atribut",
                    "    pengguna, data, dan keadaan. Contoh aturannya: manajer boleh",
                    "    menyetujui cuti kalau departemennya sama dengan pemohon dan sekarang",
                    "    jam kerja. Lebih lentur, tapi aturannya lebih susah diaudit.",
                    "  - ReBAC (relationship-based access control): izin mengikuti hubungan.",
                    "    Kamu boleh membaca dokumen kalau kamu anggota tim yang memiliki",
                    "    folder tempat dokumen itu berada. Modelnya diambil dari makalah",
                    "    Google Zanzibar, sistem izin di balik Google Drive.",
                    "",
                    "Di aplikasi kecil, aturan cukup ditulis sebagai kode. Begitu aturannya",
                    "banyak atau dipakai beberapa layanan, orang mulai memakai mesin",
                    "kebijakan. Casbin adalah pustaka yang membaca berkas model dan kebijakan",
                    "untuk ACL, RBAC, atau ABAC, tersedia untuk Go, Java, Node, Python, dan",
                    "lainnya. Ia kini proyek inkubasi Apache, berlisensi Apache-2.0. OpenFGA",
                    "adalah server ReBAC bergaya Zanzibar, proyek CNCF berlisensi Apache-2.0;",
                    "versi terbarunya saat materi ini ditulis adalah 1.22.0 (Oktober 2026).",
                ],
            },
            {
                "heading": "Pemeriksaan per objek",
                "code": """IZIN_PERAN = {
    "admin": {"baca", "ubah", "hapus"},
    "staf": {"baca", "ubah"},
    "tamu": {"baca"},
}

faktur = {
    101: {"pemilik": "budi", "total": 250000},
    102: {"pemilik": "sari", "total": 90000},
}


def boleh(pengguna, aksi, id_faktur):
    if aksi not in IZIN_PERAN.get(pengguna["peran"], set()):
        return "403 peran tidak mengizinkan " + aksi
    data = faktur.get(id_faktur)
    if data is None:
        return "404"
    if pengguna["peran"] != "admin" and data["pemilik"] != pengguna["nama"]:
        return "404"
    return "200 " + aksi + " faktur " + str(id_faktur)


budi = {"nama": "budi", "peran": "staf"}
admin = {"nama": "rina", "peran": "admin"}
print(boleh(budi, "ubah", 101))
print(boleh(budi, "baca", 102))
print(boleh(budi, "hapus", 101))
print(boleh(admin, "hapus", 102))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  200 ubah faktur 101",
                    "  404",
                    "  403 peran tidak mengizinkan hapus",
                    "  200 hapus faktur 102",
                    "",
                    "Perhatikan baris kedua. Budi punya peran staf yang boleh membaca, tapi",
                    "faktur 102 milik Sari. Pemeriksaan peran saja akan meloloskannya.",
                    "Pemeriksaan kepemilikan per objek ini yang paling sering dilupakan. API",
                    "sengaja menjawab 404, bukan 403, supaya penyerang nggak tahu faktur",
                    "nomor itu ada.",
                ],
            },
            {
                "heading": "OWASP API Security Top 10 (edisi 2023)",
                "body": [
                    "Komunitas keamanan aplikasi terbuka Open Worldwide Application Security",
                    "Project menerbitkan daftar sepuluh risiko API paling kritis. Edisi",
                    "terbarunya masih edisi 2023, dirilis dengan lisensi Creative Commons",
                    "Attribution-ShareAlike 4.0:",
                    "",
                    "  API1   Broken Object Level Authorization (BOLA)",
                    "  API2   Broken Authentication",
                    "  API3   Broken Object Property Level Authorization",
                    "  API4   Unrestricted Resource Consumption",
                    "  API5   Broken Function Level Authorization",
                    "  API6   Unrestricted Access to Sensitive Business Flows",
                    "  API7   Server Side Request Forgery (SSRF)",
                    "  API8   Security Misconfiguration",
                    "  API9   Improper Inventory Management",
                    "  API10  Unsafe Consumption of APIs",
                    "",
                    "Nomor satu adalah kasus faktur tadi: objek bisa diakses dengan menebak",
                    "ID-nya. Nomor tiga mirip, tapi di tingkat kolom, misalnya pengguna bisa",
                    "mengirim field is_admin di body PATCH dan servernya menyimpan apa",
                    "adanya. Nomor lima terjadi kalau endpoint admin cuma disembunyikan dari",
                    "menu tapi nggak dijaga. Nomor empat menyangkut permintaan tanpa batas,",
                    "yang dijawab dengan rate limiting di bagian berikut. Sisi serangan tiap",
                    "risiko dibahas di kurikulum Keamanan Siber.",
                ],
            },
            {
                "heading": "Rate limiting dengan token bucket",
                "body": [
                    "Rate limiting membatasi berapa banyak permintaan yang boleh dikirim satu",
                    "klien dalam waktu tertentu. Tujuannya melindungi server dari banjir",
                    "permintaan, membuat percobaan menebak kata sandi jadi lambat, dan",
                    "membagi kapasitas secara adil.",
                    "",
                    "Algoritma yang paling sering dipakai adalah token bucket. Bayangkan",
                    "ember berisi paling banyak N token. Tiap permintaan mengambil satu",
                    "token. Token diisi ulang dengan laju tetap, misalnya satu per detik.",
                    "Kalau ember kosong, permintaan ditolak dengan status 429 Too Many",
                    "Requests dan header Retry-After yang memberi tahu klien berapa detik",
                    "harus menunggu. Ember penuh mengizinkan ledakan singkat sampai N",
                    "permintaan, lalu lajunya turun ke laju isi ulang.",
                    "",
                    "Alternatifnya fixed window (hitung per menit, reset di awal menit), yang",
                    "gampang tapi mengizinkan dua kali batas di sekitar pergantian menit, dan",
                    "sliding window yang lebih halus. Throttling adalah saudaranya:",
                    "permintaan diperlambat atau diantrekan, bukan ditolak.",
                ],
            },
            {
                "heading": "Token bucket dengan jam palsu",
                "code": """class Ember:
    def __init__(self, kapasitas, laju):
        self.kapasitas = kapasitas
        self.laju = laju
        self.token = kapasitas
        self.terakhir = 0

    def ambil(self, t):
        self.token = min(self.kapasitas,
                         self.token + (t - self.terakhir) * self.laju)
        self.terakhir = t
        if self.token >= 1:
            self.token -= 1
            return "200"
        tunggu = (1 - self.token) / self.laju
        return "429 Retry-After=" + str(int(tunggu + 0.999))


ember = Ember(kapasitas=2, laju=0.5)
for t in [0, 0, 0, 1, 2, 6]:
    print("t=" + str(t), ember.ambil(t))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  t=0 200",
                    "  t=0 200",
                    "  t=0 429 Retry-After=2",
                    "  t=1 429 Retry-After=1",
                    "  t=2 200",
                    "  t=6 200",
                    "",
                    "Jam dioper sebagai angka, bukan dibaca dari time.time(). Di server",
                    "sungguhan, ember disimpan per klien (per IP, per API key, atau per",
                    "pengguna) di Redis supaya semua instance server berbagi hitungan yang",
                    "sama.",
                ],
            },
            {
                "heading": "Idempotency key",
                "body": [
                    "Klien mobile mengirim POST /pembayaran, lalu sinyal putus sebelum",
                    "respons datang. Klien nggak tahu pembayarannya sudah tercatat atau",
                    "belum. Kalau ia mengulang, bisa terjadi dua kali tagihan.",
                    "",
                    "Solusinya idempotency key: klien membuat ID unik per operasi dan",
                    "mengirimkannya di header, umumnya Idempotency-Key. Server menyimpan",
                    "respons pertama untuk key itu. Permintaan berikutnya dengan key yang",
                    "sama langsung dijawab dengan respons tersimpan tanpa memproses ulang.",
                    "Pola ini dipakai API pembayaran seperti Stripe, dan header-nya sedang",
                    "dibakukan di draf IETF httpapi-idempotency-key-header. Simpan key dengan",
                    "masa berlaku, misalnya 24 jam, dan ikat ke pengguna supaya key orang",
                    "lain nggak bisa dipakai.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "API publik seperti GitHub dan layanan pembayaran membalas 429 begitu",
                    "batas terlampaui dan mencantumkan sisa kuota di header respons. Celah",
                    "otorisasi per objek juga termasuk temuan yang paling sering dilaporkan",
                    "di program bug bounty, karena cukup ditemukan dengan mengganti angka ID",
                    "di URL.",
                    "",
                    "Kasus kecil: API toko onlinemu punya endpoint GET /pesanan/{id}. Penguji",
                    "menemukan bahwa pelanggan A bisa membaca pesanan pelanggan B, dan",
                    "endpoint login bisa dicoba ribuan kali per menit.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Di handler pesanan, ambil data dengan syarat pemilik, misalnya",
                    "     WHERE id = ? AND pelanggan_id = ?, lalu balas 404 kalau kosong.",
                    "  2. Tulis tes otomatis yang login sebagai A lalu meminta pesanan milik",
                    "     B, dan pastikan jawabannya 404.",
                    "  3. Pasang token bucket di endpoint login, kuncinya gabungan IP dan",
                    "     nama pengguna, misalnya 5 token dengan isi ulang satu per menit.",
                    "  4. Balas 429 dengan header Retry-After, dan catat penolakan ke log",
                    "     supaya serangan terlihat di dasbor.",
                    "  5. Untuk POST pembayaran, wajibkan header Idempotency-Key dan simpan",
                    "     respons pertamanya selama 24 jam.",
                ],
            },
        ],
    },
    {
        "title": "42. Peta Layanan Identitas Terkelola",
        "sections": [
            {
                "body": [
                    "Menulis login sendiri berarti mengurus tabel pengguna, hash kata sandi,",
                    "lupa kata sandi, verifikasi email, 2FA, passkeys, login sosial, SSO",
                    "perusahaan, dan audit log. Itu pekerjaan berbulan-bulan, dan satu",
                    "kesalahan kecil bisa membocorkan semua akun. Karena itu banyak tim",
                    "menyerahkannya ke layanan identitas.",
                    "",
                    "Pilihannya terbagi dua. Layanan SaaS (dijalankan vendor, kamu membayar",
                    "per pengguna aktif) dan server self-hosted (kamu jalankan sendiri,",
                    "gratis lisensinya tapi kamu yang mengurus server dan pembaruannya).",
                    "Hampir semuanya berbicara OIDC dan OAuth, jadi kode backend-mu tetap",
                    "memakai pola yang sama dengan materi OpenID Connect, SSO, dan Keycloak.",
                ],
            },
            {
                "heading": "Tabel perbandingan",
                "bahasa": "teks",
                "code": """Layanan                  Jenis        Lisensi                  Cocok untuk
-----------------------  -----------  -----------------------  -------------------------
Auth0                    SaaS         proprietary (milik Okta) aplikasi pelanggan, startup
Okta                     SaaS         proprietary              SSO karyawan perusahaan
Microsoft Entra ID       SaaS         proprietary              kantor yang pakai M365
Amazon Cognito           SaaS         proprietary              aplikasi di AWS
Firebase Authentication  SaaS         proprietary, SDK Apache  aplikasi mobile/web Firebase
Supabase Auth            SaaS/sendiri MIT                      aplikasi di atas Postgres
Clerk                    SaaS         proprietary              Next.js, komponen UI siap
Ping Identity            SaaS/sendiri proprietary              enterprise besar
OneLogin                 SaaS         proprietary              SSO karyawan
Keycloak                 sendiri      Apache-2.0               SSO serba ada, gratis
Ory Kratos/Hydra/Keto    sendiri/SaaS Apache-2.0               blok bangunan terpisah
authentik                sendiri      MIT + fitur Enterprise   homelab, kantor kecil
ZITADEL                  sendiri/SaaS AGPL-3.0 (sejak v3)      multi-tenant, passkeys""",
            },
            {
                "heading": "Layanan SaaS",
                "body": [
                    "Auth0 adalah layanan identitas untuk aplikasi pelanggan: login sosial,",
                    "MFA, dan halaman login yang bisa diatur tampilannya. Sejak 2021 ia milik",
                    "Okta. Di Survei Stack Overflow 2026 (kategori Security Operations Tools,",
                    "n = 4.052) Auth0 dipakai 29,7% responden, tertinggi di kategori itu.",
                    "",
                    "Okta condong ke identitas karyawan: SSO ke ratusan aplikasi SaaS kantor,",
                    "manajemen akun, dan MFA. Survei yang sama mencatatnya di 28,7%.",
                    "",
                    "Microsoft Entra ID, dulu Azure AD, adalah direktori akun kerja dan",
                    "sekolah di ekosistem Microsoft 365. Survei mencatatnya cuma 0,8%, angka",
                    "yang hampir pasti terlalu kecil karena layanan ini ikut terbundel di",
                    "Microsoft 365. Kalau kantormu memakai Teams dan Outlook, akunmu sudah",
                    "ada di Entra ID.",
                    "",
                    "Amazon Cognito adalah direktori pengguna terkelola di AWS. Firebase",
                    "Authentication menyediakan login email, nomor telepon, Google, dan Apple",
                    "untuk aplikasi Firebase; backend-mu tetap wajib memverifikasi ID token",
                    "yang dikirim aplikasi. Clerk menjual komponen UI login siap pakai dan",
                    "populer di ekosistem Next.js. Ping Identity (4,6% di survei tadi) dan",
                    "OneLogin (3,0%, milik One Identity) melayani SSO dan federasi untuk",
                    "organisasi besar.",
                ],
            },
            {
                "heading": "Server self-hosted",
                "body": [
                    "Keycloak sudah dibahas di materi sebelumnya: paling lengkap, Apache-2.0,",
                    "dan paling banyak tutorialnya.",
                    "",
                    "Supabase Auth adalah layanan login milik Supabase yang terhubung",
                    "langsung ke Row Level Security PostgreSQL. Kodenya berlisensi MIT, jadi",
                    "bisa dijalankan sendiri, walau kebanyakan orang memakainya lewat",
                    "Supabase Cloud. Versi terbarunya saat materi ini ditulis adalah 2.197.0.",
                    "",
                    "Ory memecah identitas jadi beberapa server Apache-2.0: Kratos untuk",
                    "pendaftaran dan login, Hydra sebagai server OAuth2 dan OIDC, dan Keto",
                    "untuk otorisasi bergaya Zanzibar. Penomorannya berbasis tahun, misalnya",
                    "Kratos dan Hydra 26.2.0. Cocok kalau kamu ingin membangun alur login",
                    "sendiri tapi nggak mau menulis kriptografinya.",
                    "",
                    "authentik adalah penyedia identitas self-hosted (SSO, OIDC, SAML, LDAP,",
                    "proxy) yang inti kodenya MIT dengan fitur Enterprise berbayar. Ia banyak",
                    "dipakai di homelab dan kantor kecil; versi terbarunya 2026.8.4.",
                    "",
                    "ZITADEL mendukung OIDC, SAML, passkeys, dan multi-tenant. Perhatikan",
                    "lisensinya: sejak versi 3 servernya pindah dari Apache-2.0 ke AGPL-3.0,",
                    "sementara API dan SDK-nya tetap Apache-2.0. AGPL mewajibkan kamu membuka",
                    "kode modifikasi kalau server yang sudah diubah kamu sediakan untuk orang",
                    "lain lewat jaringan. Versi terbarunya 4.19.5.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "Beberapa pertanyaan yang membantu:",
                    "",
                    "  - Penggunanya siapa? Pelanggan umum cocok dengan Auth0, Clerk,",
                    "    Firebase, atau Supabase. Karyawan cocok dengan Okta, Entra ID, atau",
                    "    Keycloak.",
                    "  - Data boleh di luar negeri? Aturan perlindungan data pribadi bisa",
                    "    mewajibkan data disimpan di wilayah tertentu. Server self-hosted",
                    "    memberi kendali penuh.",
                    "  - Berapa pengguna aktif? Harga SaaS dihitung per pengguna aktif",
                    "    bulanan. Di puluhan ribu pengguna, tagihannya bisa lebih mahal dari",
                    "    gaji orang yang merawat Keycloak.",
                    "  - Siapa yang memperbarui? Server self-hosted harus rajin diperbarui,",
                    "    contohnya rilis Keycloak yang menambal 23 celah sekaligus.",
                    "",
                    "Jebakan: mengunci logika aplikasi ke fitur khas satu vendor, misalnya",
                    "menyimpan data profil penting hanya di metadata Auth0. Simpan data",
                    "aplikasimu di database-mu sendiri dengan kunci sub, supaya pindah",
                    "provider cuma berarti mengganti konfigurasi OIDC.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Startup aplikasi mobile sering memulai dengan Firebase Authentication",
                    "atau Auth0 karena gratis di jumlah pengguna kecil. Perusahaan yang sudah",
                    "memakai Microsoft 365 hampir selalu memasang SSO aplikasi internalnya ke",
                    "Entra ID. Instansi yang datanya wajib di server sendiri cenderung",
                    "memilih Keycloak.",
                    "",
                    "Kasus kecil: sekolahmu ingin aplikasi nilai online. Gurunya sudah punya",
                    "akun Google Workspace sekolah, sedangkan orang tua murid belum punya",
                    "akun apa pun, dan anggarannya nol.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jalankan Keycloak di server sekolah, buat satu realm sekolah.",
                    "  2. Tambahkan Google sebagai identity provider di realm itu, dibatasi",
                    "     ke domain sekolah, supaya guru login dengan akun sekolahnya.",
                    "  3. Aktifkan pendaftaran mandiri dengan verifikasi email untuk orang",
                    "     tua, ditambah TOTP sebagai faktor kedua.",
                    "  4. Daftarkan aplikasi nilai sebagai client OIDC, dan bedakan akses",
                    "     lewat role guru dan orang-tua.",
                    "  5. Jadwalkan pembaruan Keycloak tiap ada rilis keamanan, dan cadangkan",
                    "     database-nya.",
                ],
            },
        ],
    },
    {
        "title": "43. Cache dengan Redis dan Valkey",
        "sections": [
            {
                "body": [
                    "Halaman detail produk di toko onlinemu dibuka ribuan kali sehari. Tiap",
                    "kali dibuka, backend menjalankan kueri yang menggabungkan lima tabel dan",
                    "makan 200 milidetik. Padahal data produk itu cuma berubah beberapa kali",
                    "sehari. Database bekerja keras menghitung jawaban yang sama",
                    "berulang-ulang.",
                    "",
                    "Cache adalah tempat menyimpan salinan jawaban yang mahal dihitung,",
                    "supaya permintaan berikutnya bisa dijawab dari salinan itu. Kalau data",
                    "yang dicari ada di cache, namanya cache hit. Kalau nggak ada, namanya",
                    "cache miss, dan aplikasi harus mengambil dari sumber aslinya.",
                    "",
                    "Cache yang paling sering dipakai backend adalah Redis: server penyimpan",
                    "pasangan kunci dan nilai di memori, jadi membaca satu kunci biasanya",
                    "cuma butuh kurang dari satu milidetik. Di Survei Stack Overflow 2026",
                    "(kategori Databases), Redis dipakai 28,3% responden. Redis sebagai",
                    "database lengkap, termasuk persistensinya, dibahas di kurikulum",
                    "Database. Di sini kita memakainya dari sisi aplikasi.",
                ],
            },
            {
                "heading": "Pola cache-aside",
                "body": [
                    "Pola yang paling umum disebut cache-aside, atau lazy loading. Aplikasi",
                    "yang mengatur cache-nya sendiri:",
                    "",
                    "  1. Cari kunci di cache, misalnya produk:42.",
                    "  2. Kalau ada (hit), langsung pakai.",
                    "  3. Kalau nggak ada (miss), ambil dari database, simpan ke cache dengan",
                    "     TTL, lalu pakai.",
                    "",
                    "TTL (time to live) adalah umur salinan di cache. Sesudah TTL habis,",
                    "salinannya dibuang otomatis dan permintaan berikutnya akan miss lalu",
                    "mengambil data segar. TTL adalah pengaman terakhir: walaupun kamu lupa",
                    "membuang salinan lama, data basi nggak akan bertahan selamanya.",
                    "",
                    "Dua pola lain yang perlu kamu kenal namanya: write-through (setiap",
                    "penulisan ke database langsung juga menulis ke cache) dan write-behind",
                    "(penulisan masuk cache dulu, lalu dicicil ke database). Write-behind",
                    "cepat tapi berisiko kehilangan data kalau server cache mati sebelum",
                    "sempat menulis.",
                ],
            },
            {
                "heading": "Cache-aside dengan jam palsu",
                "code": """class Cache:
    def __init__(self):
        self.isi = {}

    def get(self, kunci, sekarang):
        ada = self.isi.get(kunci)
        if ada is None or ada[1] <= sekarang:
            self.isi.pop(kunci, None)
            return None
        return ada[0]

    def set(self, kunci, nilai, ttl, sekarang):
        self.isi[kunci] = (nilai, sekarang + ttl)


panggilan_db = 0


def ambil_produk_dari_db(id_produk):
    global panggilan_db
    panggilan_db += 1
    return {"id": id_produk, "nama": "Kopi Gayo", "harga": 85000}


cache = Cache()


def produk(id_produk, sekarang):
    kunci = f"produk:{id_produk}"
    data = cache.get(kunci, sekarang)
    if data is not None:
        return "hit", data
    data = ambil_produk_dari_db(id_produk)
    cache.set(kunci, data, ttl=60, sekarang=sekarang)
    return "miss", data


for t in [0, 5, 30, 59, 60, 61]:
    status, data = produk(42, t)
    print(f"t={t:>2} {status:4} {data['nama']}")
print("kueri ke database:", panggilan_db)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  t= 0 miss Kopi Gayo",
                    "  t= 5 hit  Kopi Gayo",
                    "  t=30 hit  Kopi Gayo",
                    "  t=59 hit  Kopi Gayo",
                    "  t=60 miss Kopi Gayo",
                    "  t=61 hit  Kopi Gayo",
                    "  kueri ke database: 2",
                    "",
                    "Enam permintaan, dua kueri. Di Redis sungguhan, TTL dipasang lewat opsi",
                    "EX pada perintah set, dan Redis sendiri yang membuang kunci kedaluwarsa.",
                    "Perintah yang sama di redis-cli:",
                ],
            },
            {
                "heading": "Perintahnya di Redis",
                "bahasa": "redis",
                "code": "SET produk:42 \"{\\\"nama\\\":\\\"Kopi Gayo\\\",\\\"harga\\\":85000}\" EX 60\nGET produk:42\nTTL produk:42\nDEL produk:42",
            },
            {
                "heading": "Invalidasi dan stampede",
                "body": [
                    "Saat admin mengubah harga, salinan di cache sudah basi. Langkah paling",
                    "aman: ubah database dulu, baru hapus kunci di cache. Permintaan",
                    "berikutnya akan miss dan mengambil harga baru. Menghapus lebih aman",
                    "daripada menimpa, karena dua penulisan yang balapan bisa meninggalkan",
                    "nilai lama di cache.",
                    "",
                    "Masalah lain muncul di produk yang ramai sekali. Begitu TTL habis,",
                    "ratusan permintaan miss bersamaan dan semuanya menembak database dengan",
                    "kueri yang sama. Kejadian ini disebut cache stampede. Cara mengatasinya:",
                    "",
                    "  - Kunci sementara: permintaan pertama yang miss memasang kunci lewat",
                    "    set dengan opsi nx (cuma berhasil kalau kunci belum ada), lalu",
                    "    mengisi cache. Permintaan lain menunggu sebentar dan membaca ulang.",
                    "  - Jitter: tambahkan angka acak kecil ke TTL supaya kunci-kunci nggak",
                    "    kedaluwarsa di detik yang sama.",
                    "  - Penyegaran dini: perbarui salinan sedikit sebelum TTL habis, selagi",
                    "    salinan lama masih dilayani.",
                ],
            },
            {
                "heading": "Lapisan cache: browser, CDN, aplikasi",
                "body": [
                    "Redis cuma satu lapisan. Sebelum permintaan sampai ke aplikasimu, ada",
                    "dua lapisan lain yang dikendalikan lewat header HTTP (RFC 9111):",
                    "",
                    "  - Browser menyimpan respons sesuai header Cache-Control.",
                    "    Cache-Control: max-age=300 berarti boleh dipakai ulang lima menit",
                    "    tanpa bertanya ke server.",
                    "  - CDN (content delivery network) seperti Cloudflare menyimpan salinan",
                    "    di server yang dekat dengan pengguna. Header s-maxage berlaku khusus",
                    "    untuk cache bersama seperti CDN.",
                    "",
                    "Untuk data yang mungkin berubah, server bisa mengirim ETag, yaitu sidik",
                    "jari isi respons. Browser mengirimnya balik di header If-None-Match.",
                    "Kalau isinya belum berubah, server menjawab 304 Not Modified tanpa body,",
                    "jadi yang dikirim ulang cuma beberapa baris header.",
                ],
            },
            {
                "heading": "Revalidasi dengan ETag",
                "bahasa": "http",
                "code": """GET /api/produk/42 HTTP/1.1
Host: toko.example
If-None-Match: "a1b2c3"

HTTP/1.1 304 Not Modified
ETag: "a1b2c3"
Cache-Control: max-age=60""",
            },
            {
                "heading": "Redis, Valkey, dan Memcached",
                "body": [
                    "Sampai versi 7.2, Redis berlisensi BSD-3-Clause. Pada Maret 2024,",
                    "perusahaan Redis mengganti lisensi versi berikutnya (7.4) menjadi RSALv2",
                    "dan SSPLv1, dua lisensi yang nggak diakui sebagai open source oleh OSI.",
                    "Beberapa minggu kemudian, Linux Foundation bersama para kontributor",
                    "membuat fork dari Redis 7.2.4 bernama Valkey, tetap berlisensi",
                    "BSD-3-Clause. Mulai Redis 8 (2025), Redis menambahkan AGPLv3 sebagai",
                    "pilihan ketiga, jadi Redis kembali bisa dipakai dengan lisensi open",
                    "source.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), versi stabil terbaru Redis",
                    "adalah 8.10.2 dan Valkey 9.1.2. Valkey dipakai 5,0% responden Survei",
                    "Stack Overflow 2026, naik dari 2,4% setahun sebelumnya. Untuk kode",
                    "aplikasi, keduanya hampir sama: perintahnya sama dan pustaka klien Redis",
                    "bisa tersambung ke Valkey. Banyak penyedia cloud kini menawarkan Valkey",
                    "sebagai layanan terkelola.",
                    "",
                    "Memcached lebih tua dan lebih sederhana: cuma menyimpan string, nggak",
                    "punya persistensi, nggak punya struktur data seperti list atau hash.",
                    "Kelebihannya, ia multithread dan protokol teksnya gampang. Versi",
                    "terbarunya 1.6.45 (BSD-3-Clause). Untuk proyek baru, kebanyakan tim",
                    "memilih Redis atau Valkey karena fiturnya lebih banyak.",
                ],
            },
            {
                "heading": "Memakainya dari Python",
                "code": """import json

import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def produk(id_produk, db):
    kunci = f"produk:{id_produk}"
    teks = r.get(kunci)
    if teks is not None:
        return json.loads(teks)
    data = db.ambil_produk(id_produk)
    r.set(kunci, json.dumps(data), ex=60)
    return data""",
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: menganggap cache sebagai tempat penyimpanan utama. Kalau Redis",
                    "dimulai ulang tanpa persistensi, semua isinya hilang. Semua yang ada di",
                    "cache harus bisa dibangun ulang dari sumber aslinya.",
                    "",
                    "  - Lupa memasang TTL. Kunci tanpa TTL menumpuk sampai memori penuh,",
                    "    lalu Redis mulai membuang kunci sesuai kebijakan maxmemory-policy,",
                    "    atau menolak penulisan.",
                    "  - Menaruh data milik pengguna di kunci yang sama untuk semua orang,",
                    "    misalnya keranjang:terbaru. Sertakan ID pengguna di nama kunci.",
                    "  - Membuka port 6379 ke internet tanpa kata sandi. Redis yang terbuka",
                    "    sering diserang dan dipakai menyimpan skrip jahat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs berita, toko online, dan aplikasi media sosial menyimpan halaman",
                    "populer, hasil hitungan peringkat, dan profil pengguna di Redis atau",
                    "Valkey. Berkas statis seperti gambar dan skrip disajikan lewat CDN",
                    "dengan Cache-Control panjang.",
                    "",
                    "Kasus kecil: endpoint GET /api/produk/{id} di tokomu lambat saat promo,",
                    "karena satu produk diskon dibuka ribuan kali per menit.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Terapkan cache-aside dengan kunci produk:{id} dan TTL 60 detik",
                    "     ditambah jitter acak 0 sampai 10 detik.",
                    "  2. Di handler ubah produk, simpan ke database dulu, lalu hapus kunci",
                    "     produk:{id}.",
                    "  3. Untuk produk diskon, pasang kunci sementara dengan opsi nx supaya",
                    "     cuma satu permintaan yang mengisi ulang cache.",
                    "  4. Tambahkan header ETag dan Cache-Control: max-age=30 di respons,",
                    "     sehingga browser dan CDN ikut menahan beban.",
                    "  5. Pantau rasio hit di dasbor. Rasio yang turun drastis biasanya",
                    "     berarti kunci terlalu cepat dihapus atau TTL terlalu pendek.",
                ],
            },
        ],
    },
    {
        "title": "44. Redis untuk Sesi, Pub/Sub, dan Antrean Tugas",
        "sections": [
            {
                "body": [
                    "Redis bisa lebih dari sekadar cache. Tiga pemakaian lain yang sering",
                    "muncul di backend: menyimpan sesi login, menyiarkan pesan ke banyak",
                    "pendengar, dan menjadi antrean pekerjaan yang dikerjakan di belakang",
                    "layar.",
                ],
            },
            {
                "heading": "Sesi di Redis",
                "body": [
                    "Di materi Session, Cookie, dan Menyimpan Kata Sandi, sesi disimpan di",
                    "memori proses server. Itu langsung bermasalah begitu aplikasimu berjalan",
                    "di dua server di belakang load balancer: pengguna login di server A,",
                    "permintaan berikutnya mendarat di server B yang nggak kenal sesinya.",
                    "",
                    "Solusinya, simpan sesi di Redis yang dipakai bersama semua server.",
                    "Kuncinya ID sesi dari cookie, nilainya data sesi, dan TTL-nya sama",
                    "dengan umur sesi. Hampir semua framework punya adaptornya:",
                    "Flask-Session, connect-redis untuk Express, SESSION_DRIVER=redis di",
                    "Laravel, dan Spring Session.",
                ],
            },
            {
                "heading": "Pub/Sub dan Streams",
                "body": [
                    "Pub/Sub (publish/subscribe) adalah siaran: satu pengirim menerbitkan",
                    "pesan ke sebuah channel, dan semua klien yang sedang berlangganan",
                    "channel itu menerimanya. Pemakaian umumnya memberi tahu semua server",
                    "WebSocket bahwa ada pesan chat baru. Kelemahannya, Pub/Sub nggak",
                    "menyimpan apa pun. Klien yang sedang putus saat pesan dikirim nggak akan",
                    "pernah menerimanya.",
                    "",
                    "Redis Streams menutup kekurangan itu. Stream adalah log yang terus",
                    "bertambah: tiap entri punya ID berurutan dan tetap tersimpan. Pembaca",
                    "bisa bergabung dalam consumer group, membaca entri yang belum diambil",
                    "anggota lain, lalu mengonfirmasi dengan perintah xack. Entri yang",
                    "diambil tapi belum dikonfirmasi bisa diambil alih anggota lain kalau",
                    "pembaca pertama mati. Konsep consumer group ini mirip Kafka, yang",
                    "dibahas dua materi lagi.",
                ],
            },
            {
                "heading": "Perintah Pub/Sub dan Streams",
                "bahasa": "redis",
                "code": """# terminal 1
SUBSCRIBE chat:umum
# terminal 2
PUBLISH chat:umum "halo semua"

XADD pesanan * id 501 total 125000
XGROUP CREATE pesanan gudang $ MKSTREAM
XREADGROUP GROUP gudang pekerja-1 COUNT 10 STREAMS pesanan >
XACK pesanan gudang 1760000000000-0""",
            },
            {
                "heading": "Antrean tugas",
                "body": [
                    "Pengguna mendaftar, lalu aplikasimu harus mengirim email selamat datang.",
                    "Server email kadang butuh tiga detik untuk menjawab, dan kadang gagal.",
                    "Kalau pengiriman dilakukan di dalam handler, pengguna menunggu tiga",
                    "detik, dan kalau server email gagal, pendaftarannya ikut gagal.",
                    "",
                    "Antrean tugas (task queue, job queue) memindahkan kerja lambat itu ke",
                    "belakang. Handler cuma menaruh tugas \"kirim email ke budi\" ke antrean",
                    "lalu langsung menjawab 201. Proses terpisah bernama worker mengambil",
                    "tugas dari antrean dan mengerjakannya. Kalau gagal, tugas dicoba ulang",
                    "dengan jeda yang makin lama, disebut exponential backoff. Tugas yang",
                    "terus gagal dipindahkan ke dead letter queue supaya bisa diperiksa",
                    "manusia.",
                    "",
                    "Karena tugas bisa dicoba ulang, worker mungkin mengerjakan tugas yang",
                    "sama dua kali, misalnya kalau worker mati tepat sesudah mengirim email",
                    "tapi sebelum melapor selesai. Karena itu tugas harus idempoten:",
                    "dikerjakan dua kali hasilnya sama dengan sekali. Caranya, catat ID tugas",
                    "yang sudah selesai dan lewati kalau muncul lagi.",
                ],
            },
            {
                "heading": "Worker dengan retry dan backoff",
                "code": """from collections import deque

antrean = deque([
    {"id": "t1", "kerja": "email budi", "gagal_dulu": 0},
    {"id": "t2", "kerja": "email sari", "gagal_dulu": 2},
    {"id": "t3", "kerja": "resize foto", "gagal_dulu": 5},
])
MAKS_COBA = 3
mati = []
jam = 0

while antrean:
    tugas = antrean.popleft()
    tugas["coba"] = tugas.get("coba", 0) + 1
    if tugas.get("tunda", 0) > jam:
        jam = tugas["tunda"]
    if tugas["coba"] <= tugas["gagal_dulu"]:
        if tugas["coba"] >= MAKS_COBA:
            print(f"t={jam:>2} {tugas['id']} gagal ke-{tugas['coba']}, "
                  "pindah ke dead letter")
            mati.append(tugas["id"])
            continue
        jeda = 2 ** tugas["coba"]
        tugas["tunda"] = jam + jeda
        print(f"t={jam:>2} {tugas['id']} gagal ke-{tugas['coba']}, "
              f"coba lagi {jeda} detik lagi")
        antrean.append(tugas)
    else:
        print(f"t={jam:>2} {tugas['id']} selesai: {tugas['kerja']}")

print("dead letter:", mati)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  t= 0 t1 selesai: email budi",
                    "  t= 0 t2 gagal ke-1, coba lagi 2 detik lagi",
                    "  t= 0 t3 gagal ke-1, coba lagi 2 detik lagi",
                    "  t= 2 t2 gagal ke-2, coba lagi 4 detik lagi",
                    "  t= 2 t3 gagal ke-2, coba lagi 4 detik lagi",
                    "  t= 6 t2 selesai: email sari",
                    "  t= 6 t3 gagal ke-3, pindah ke dead letter",
                    "  dead letter: ['t3']",
                    "",
                    "Jam dan pola gagalnya dipatok supaya alurnya kelihatan. Di pustaka",
                    "sungguhan, jadwal coba ulang dan dead letter sudah disediakan, kamu",
                    "cukup mengatur angkanya.",
                ],
            },
            {
                "heading": "Pustaka antrean per bahasa",
                "body": [
                    "Kamu jarang menulis antrean sendiri. Pustaka yang umum, versinya per",
                    "Oktober 2026:",
                    "",
                    "  - Celery (Python, 5.6.3, BSD-3-Clause): paling lengkap, broker bisa",
                    "    Redis atau RabbitMQ, mendukung tugas terjadwal. Argumen tugas harus",
                    "    bisa diubah jadi JSON, jadi kirim ID, jangan objek ORM.",
                    "  - RQ atau Redis Queue (Python, 2.12.0, BSD-2-Clause): jauh lebih",
                    "    sederhana dari Celery, khusus Redis.",
                    "  - BullMQ (Node.js, 6.3.17, MIT): standar antrean di dunia Node,",
                    "    penerus Bull, di atas Redis.",
                    "  - Sidekiq (Ruby, 8.1.7): versi open source berlisensi LGPL-3.0, dengan",
                    "    edisi Pro dan Enterprise berbayar. Umum sekali di aplikasi Rails.",
                    "  - Solid Queue (Ruby, 1.7.0, MIT): antrean bawaan Rails 8 yang",
                    "    menyimpan tugas di database biasa, tanpa Redis. Pola \"database",
                    "    sebagai antrean\" ini sedang naik karena mengurangi satu server yang",
                    "    harus dirawat.",
                ],
            },
            {
                "heading": "Celery dalam beberapa baris",
                "code": """from celery import Celery

app = Celery("toko", broker="redis://localhost:6379/0")


@app.task(bind=True, max_retries=3, autoretry_for=(ConnectionError,),
          retry_backoff=True)
def kirim_email_sambutan(self, id_pengguna):
    pengguna = Pengguna.ambil(id_pengguna)
    layanan_email.kirim(pengguna.email, "Selamat datang!")


# di handler pendaftaran:
# kirim_email_sambutan.delay(pengguna_baru.id)""",
            },
            {
                "heading": "Hal yang sama dengan BullMQ",
                "bahasa": "javascript",
                "code": """const { Queue, Worker } = require('bullmq');
const koneksi = { host: 'localhost', port: 6379 };

const antrean = new Queue('email', { connection: koneksi });

async function daftarkan(idPengguna) {
  await antrean.add('sambutan', { idPengguna },
    { attempts: 3, backoff: { type: 'exponential', delay: 1000 } });
}

new Worker('email', async (job) => {
  await kirimEmail(job.data.idPengguna);
}, { connection: koneksi });""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Email konfirmasi, pembuatan PDF faktur, kompresi video yang diunggah,",
                    "dan sinkronisasi stok ke marketplace hampir selalu dikerjakan worker,",
                    "bukan di dalam handler HTTP. Aplikasi chat memakai Pub/Sub supaya pesan",
                    "yang diterima satu server WebSocket diteruskan ke server lain.",
                    "",
                    "Kasus kecil: endpoint POST /pesanan di aplikasi Flask-mu butuh lima",
                    "detik karena sekaligus membuat PDF faktur dan mengirim email. Kadang",
                    "server email gagal dan pesanan pelanggan ikut batal.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Simpan pesanan ke database, lalu langsung balas 201 ke pelanggan.",
                    "  2. Sesudah menyimpan, taruh dua tugas ke antrean Celery atau RQ:",
                    "     buat_faktur(id_pesanan) dan kirim_email(id_pesanan).",
                    "  3. Jalankan worker sebagai proses terpisah, dengan retry tiga kali dan",
                    "     backoff eksponensial.",
                    "  4. Di dalam tugas, periksa dulu apakah faktur untuk pesanan itu sudah",
                    "     ada, supaya pengulangan nggak membuat faktur ganda.",
                    "  5. Pantau dead letter queue dan kirim notifikasi ke tim kalau isinya",
                    "     bertambah.",
                ],
            },
        ],
    },
    {
        "title": "45. RabbitMQ: Exchange, Antrean, dan Acknowledgement",
        "sections": [
            {
                "body": [
                    "Antrean di Redis cocok untuk tugas latar dari satu aplikasi. Begitu",
                    "banyak layanan saling berkirim pesan, aturan pengiriman mulai rumit.",
                    "Pesanan baru harus sampai ke layanan gudang, layanan email, dan layanan",
                    "analitik. Pesanan dari Jakarta cuma untuk gudang Jakarta. Pesan nggak",
                    "boleh hilang walaupun satu layanan sedang mati.",
                    "",
                    "Message broker adalah server khusus yang menerima, menyimpan, dan",
                    "meneruskan pesan sesuai aturan. RabbitMQ adalah broker open source yang",
                    "paling banyak dipakai untuk pola ini. Ia ditulis dengan Erlang,",
                    "berlisensi MPL-2.0, dan versi stabil terbarunya saat materi ini ditulis",
                    "(Oktober 2026) adalah 4.3.6.",
                ],
            },
            {
                "heading": "Produser, exchange, binding, antrean",
                "body": [
                    "Di RabbitMQ, produser (pengirim) nggak menaruh pesan langsung ke",
                    "antrean. Ia mengirim ke exchange, semacam kantor pos yang memutuskan",
                    "pesan harus ke mana. Exchange dihubungkan ke antrean lewat binding,",
                    "yaitu aturan pencocokan. Konsumen (penerima) membaca dari antrean.",
                    "",
                    "Tiap pesan membawa routing key, label pendek seperti",
                    "pesanan.jakarta.baru. Jenis exchange menentukan cara routing key",
                    "dicocokkan:",
                    "",
                    "  - direct: pesan masuk ke antrean yang binding key-nya sama persis",
                    "    dengan routing key.",
                    "  - fanout: pesan disalin ke semua antrean yang terhubung, routing key",
                    "    diabaikan. Cocok untuk siaran.",
                    "  - topic: binding key berupa pola. Tanda * cocok dengan tepat satu",
                    "    kata, tanda # cocok dengan nol kata atau lebih. Kata dipisah titik.",
                    "  - headers: pencocokan memakai header pesan, bukan routing key. Jarang",
                    "    dipakai.",
                    "",
                    "Model exchange dan binding ini berasal dari protokol asli RabbitMQ,",
                    "Advanced Message Queuing Protocol versi 0-9-1.",
                ],
            },
            {
                "heading": "Meniru topic exchange",
                "code": """def cocok(pola, kunci):
    p, k = pola.split("."), kunci.split(".")

    def jalan(i, j):
        if i == len(p):
            return j == len(k)
        if p[i] == "#":
            return any(jalan(i + 1, x) for x in range(j, len(k) + 1))
        if j < len(k) and (p[i] == "*" or p[i] == k[j]):
            return jalan(i + 1, j + 1)
        return False

    return jalan(0, 0)


binding = [
    ("pesanan.jakarta.*", "gudang-jakarta"),
    ("pesanan.*.baru", "email"),
    ("pesanan.#", "analitik"),
    ("#.batal", "keuangan"),
]

for kunci in ["pesanan.jakarta.baru", "pesanan.medan.baru",
              "pesanan.jakarta.batal", "stok.habis"]:
    tujuan = [antrean for pola, antrean in binding if cocok(pola, kunci)]
    print(f"{kunci:22} -> {tujuan or 'dibuang'}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  pesanan.jakarta.baru   -> ['gudang-jakarta', 'email', 'analitik']",
                    "  pesanan.medan.baru     -> ['email', 'analitik']",
                    "  pesanan.jakarta.batal  -> ['gudang-jakarta', 'analitik', 'keuangan']",
                    "  stok.habis             -> dibuang",
                    "",
                    "Pesan yang nggak cocok dengan binding mana pun dibuang oleh exchange.",
                    "Kalau itu nggak boleh terjadi, pasang alternate exchange atau kirim",
                    "dengan flag mandatory supaya produser diberi tahu.",
                ],
            },
            {
                "heading": "Acknowledgement: pesan nggak hilang di tengah jalan",
                "body": [
                    "Konsumen menerima pesan lalu mati sebelum selesai memprosesnya. Kalau",
                    "RabbitMQ langsung membuang pesan saat dikirim, pesanan itu hilang.",
                    "Karena itu konsumen mengirim acknowledgement (ack) sesudah selesai.",
                    "Selama ack belum datang, pesan tetap dipegang broker. Kalau koneksi",
                    "konsumen putus, pesan dikirim ulang ke konsumen lain.",
                    "",
                    "Konsumen juga bisa mengirim nack (negative acknowledgement) untuk",
                    "menolak pesan, dengan pilihan dikembalikan ke antrean atau dibuang.",
                    "Pesan yang ditolak atau kedaluwarsa bisa diteruskan ke dead letter",
                    "exchange untuk diperiksa. Setelan prefetch membatasi berapa pesan tanpa",
                    "ack yang boleh dipegang satu konsumen, supaya konsumen lambat nggak",
                    "menimbun pesan.",
                    "",
                    "Akibat dari pengiriman ulang: konsumen bisa menerima pesan yang sama dua",
                    "kali. Jaminan yang kamu dapat adalah at-least-once (paling sedikit",
                    "sekali), jadi konsumen tetap harus idempoten.",
                ],
            },
            {
                "heading": "Quorum queue dan RabbitMQ 4",
                "body": [
                    "Supaya antrean tetap hidup saat satu server broker mati, RabbitMQ",
                    "menyalin antrean ke beberapa node. Cara lama bernama classic mirrored",
                    "queue, dan cara itu sudah dihapus di RabbitMQ 4.0. Penggantinya quorum",
                    "queue, yang memakai algoritma konsensus Raft: pesan dianggap tersimpan",
                    "kalau mayoritas node sudah menyimpannya. Untuk antrean penting di",
                    "produksi, pilih quorum queue. RabbitMQ juga punya stream, antrean",
                    "berbentuk log yang bisa dibaca ulang seperti Kafka.",
                    "",
                    "RabbitMQ 4 juga menjadikan versi 1.0 protokol itu sebagai protokol inti,",
                    "di samping 0-9-1 yang lama. Dua versi itu protokol yang berbeda jauh",
                    "walau namanya mirip: 1.0 adalah standar terbuka yang lebih umum dan",
                    "nggak punya konsep exchange. RabbitMQ 4 butuh Erlang 27 ke atas.",
                    "Tutorial resminya ada enam bagian dan tersedia untuk Python, Java,",
                    "JavaScript, Go, C#, PHP, dan Ruby.",
                ],
            },
            {
                "heading": "Konsumen dengan pika (Python)",
                "code": """import pika

koneksi = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
kanal = koneksi.channel()
kanal.exchange_declare(exchange="pesanan", exchange_type="topic")
kanal.queue_declare(queue="email", durable=True,
                    arguments={"x-queue-type": "quorum"})
kanal.queue_bind(queue="email", exchange="pesanan",
                 routing_key="pesanan.*.baru")
kanal.basic_qos(prefetch_count=10)


def terima(ch, method, properties, body):
    kirim_email_pesanan(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


kanal.basic_consume(queue="email", on_message_callback=terima)
kanal.start_consuming()""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem pemesanan, logistik, dan perbankan memakai RabbitMQ untuk",
                    "menyambungkan layanan yang ditulis tim berbeda dengan bahasa berbeda.",
                    "Layanan pembayaran cukup menerbitkan satu pesan pembayaran.berhasil, dan",
                    "layanan lain yang tertarik memasang binding sendiri tanpa mengubah kode",
                    "pembayaran.",
                    "",
                    "Kasus kecil: tokomu punya layanan gudang Jakarta dan gudang Surabaya.",
                    "Setiap pesanan harus masuk ke gudang kotanya, sementara layanan laporan",
                    "harus menerima semua pesanan.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat topic exchange bernama pesanan.",
                    "  2. Kirim pesan dengan routing key pesanan.<kota>.baru, misalnya",
                    "     pesanan.surabaya.baru.",
                    "  3. Buat quorum queue gudang-jakarta dengan binding pesanan.jakarta.*,",
                    "     dan gudang-surabaya dengan pesanan.surabaya.*.",
                    "  4. Buat antrean laporan dengan binding pesanan.#.",
                    "  5. Di tiap konsumen, kirim ack hanya sesudah data tersimpan, dan",
                    "     abaikan pesanan yang ID-nya sudah pernah diproses.",
                ],
            },
        ],
    },
    {
        "title": "46. Kafka: Log, Partisi, dan Consumer Group",
        "sections": [
            {
                "body": [
                    "RabbitMQ menghapus pesan begitu konsumen mengirim ack. Itu pas untuk",
                    "tugas: sekali dikerjakan, selesai. Tapi ada kebutuhan lain. Tim analitik",
                    "ingin membaca ulang semua kejadian klik seminggu terakhir. Layanan",
                    "rekomendasi baru ingin mulai dari kejadian paling awal. Untuk itu pesan",
                    "harus tetap disimpan walaupun sudah dibaca.",
                    "",
                    "Apache Kafka dirancang dengan cara pandang itu. Kafka adalah log",
                    "append-only terdistribusi: pesan cuma ditambahkan di ujung, nggak pernah",
                    "diubah, dan disimpan sampai batas umur atau ukuran tertentu, misalnya",
                    "tujuh hari. Membaca pesan nggak menghapusnya. Tiap pembaca cuma",
                    "mengingat sampai mana ia sudah membaca.",
                    "",
                    "Kafka berlisensi Apache-2.0. Versi stabil terbarunya saat materi ini",
                    "ditulis (Oktober 2026) adalah 4.3.1.",
                ],
            },
            {
                "heading": "Topik, partisi, dan offset",
                "body": [
                    "Pesan dikelompokkan dalam topik, misalnya pesanan atau klik. Satu topik",
                    "dipecah jadi beberapa partisi supaya bisa ditulis dan dibaca paralel",
                    "oleh banyak server. Tiap partisi adalah log terurut, dan posisi pesan di",
                    "dalamnya disebut offset: 0, 1, 2, dan seterusnya.",
                    "",
                    "Pesan boleh membawa kunci (key). Produser menghitung hash dari kunci",
                    "untuk memilih partisi, jadi semua pesan berkunci sama masuk partisi yang",
                    "sama dan urutannya terjaga. Semua kejadian milik pelanggan 7 selalu",
                    "terbaca berurutan. Urutan antar-partisi nggak dijamin.",
                    "",
                    "Setiap partisi disalin ke beberapa broker (replication factor), biasanya",
                    "tiga. Satu salinan jadi leader yang melayani tulis, yang lain mengikuti.",
                    "Kalau leader mati, salah satu pengikut yang sudah sinkron",
                    "menggantikannya.",
                ],
            },
            {
                "heading": "Consumer group",
                "body": [
                    "Konsumen yang bekerja sama tergabung dalam consumer group. Kafka membagi",
                    "partisi ke anggota grup: satu partisi cuma dibaca satu anggota dalam",
                    "grup yang sama. Topik dengan tiga partisi bisa dibaca paralel oleh",
                    "paling banyak tiga konsumen dalam satu grup; konsumen keempat akan",
                    "menganggur.",
                    "",
                    "Grup menyimpan offset terakhir yang sudah diproses tiap partisi lewat",
                    "commit. Kalau ada anggota keluar atau masuk, partisi dibagi ulang",
                    "(rebalance), dan anggota baru melanjutkan dari offset yang terakhir",
                    "di-commit. Pesan yang sudah diproses tapi belum di-commit akan dibaca",
                    "lagi, jadi lagi-lagi konsumen harus idempoten.",
                    "",
                    "Grup yang berbeda membaca secara mandiri. Grup gudang dan grup analitik",
                    "bisa membaca topik pesanan yang sama, masing-masing dengan offset",
                    "sendiri. Ini beda utamanya dengan antrean biasa: satu pesan dibaca",
                    "banyak grup, dan bisa dibaca ulang dengan memundurkan offset.",
                ],
            },
            {
                "heading": "Log berpartisi versi mini",
                "code": """import zlib

JUMLAH_PARTISI = 3
partisi = [[] for _ in range(JUMLAH_PARTISI)]


def kirim(kunci, nilai):
    p = zlib.crc32(kunci.encode()) % JUMLAH_PARTISI
    partisi[p].append((kunci, nilai))
    print(f"kirim {kunci}={nilai} -> partisi {p} offset {len(partisi[p]) - 1}")


for kunci, nilai in [("budi", "pesan"), ("andi", "pesan"), ("budi", "bayar"),
                     ("toko-3", "stok"), ("andi", "batal")]:
    kirim(kunci, nilai)

offset = {"gudang": [0, 0, 0], "analitik": [0, 0, 0]}


def baca(grup, p):
    hasil = partisi[p][offset[grup][p]:]
    offset[grup][p] = len(partisi[p])
    return hasil


print("gudang baca p1:", baca("gudang", 1))
print("gudang baca p1 lagi:", baca("gudang", 1))
print("analitik baca p1:", baca("analitik", 1))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  kirim budi=pesan -> partisi 1 offset 0",
                    "  kirim andi=pesan -> partisi 2 offset 0",
                    "  kirim budi=bayar -> partisi 1 offset 1",
                    "  kirim toko-3=stok -> partisi 0 offset 0",
                    "  kirim andi=batal -> partisi 2 offset 1",
                    "  gudang baca p1: [('budi', 'pesan'), ('budi', 'bayar')]",
                    "  gudang baca p1 lagi: []",
                    "  analitik baca p1: [('budi', 'pesan'), ('budi', 'bayar')]",
                    "",
                    "Kafka sungguhan memakai hash murmur2 untuk kunci, bukan crc32. Polanya",
                    "sama: kunci yang sama selalu ke partisi yang sama. Perhatikan juga bahwa",
                    "grup analitik tetap mendapat dua pesan yang sudah dibaca grup gudang.",
                ],
            },
            {
                "heading": "Kafka 4 tanpa ZooKeeper",
                "body": [
                    "Dulu Kafka butuh ZooKeeper, sistem terpisah untuk menyimpan metadata",
                    "klaster dan memilih controller. Menjalankan dua sistem terdistribusi",
                    "sekaligus merepotkan. Kafka lalu membuat mode KRaft, yang menyimpan",
                    "metadata di dalam Kafka sendiri memakai algoritma konsensus Raft. Sejak",
                    "Kafka 4.0 (2025), ZooKeeper dihapus total; klaster baru maupun yang",
                    "dimigrasi wajib KRaft. Tutorial lama yang dimulai dengan menyalakan",
                    "ZooKeeper sudah nggak berlaku.",
                    "",
                    "Redpanda adalah alternatif yang ditulis dengan C++ dan kompatibel dengan",
                    "API Kafka, jadi klien Kafka bisa tersambung tanpa diubah. Ia nggak butuh",
                    "JVM dan klaim utamanya latensi rendah. Perhatikan lisensinya: Community",
                    "Edition memakai BSL-1.1, yang bukan lisensi open source versi OSI. Versi",
                    "terbarunya 26.2.2.",
                    "",
                    "Untuk klien Node.js, hati-hati dengan kafkajs: rilis terakhirnya 2.2.4",
                    "tahun 2023 dan nggak dirawat lagi. Pakai klien resmi Confluent",
                    "(@confluentinc/kafka-javascript) atau klien lain yang aktif.",
                ],
            },
            {
                "heading": "Kafka atau RabbitMQ",
                "body": [
                    "Pilih Kafka kalau datanya berupa aliran kejadian bervolume besar, perlu",
                    "dibaca banyak tim, dan perlu bisa diputar ulang: log klik, perubahan",
                    "data dari database (change data capture), telemetri. Pilih RabbitMQ",
                    "kalau yang dikirim adalah tugas yang dikerjakan sekali, aturannya perlu",
                    "routing yang lentur, dan volumenya sedang. Untuk tugas latar satu",
                    "aplikasi, antrean di Redis atau database biasanya cukup. Menyalakan",
                    "klaster Kafka untuk mengirim email sambutan adalah berlebihan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Platform e-commerce dan ride-hailing memakai Kafka untuk aliran kejadian",
                    "seperti pesanan dibuat, lokasi pengemudi, dan klik produk. Satu topik",
                    "dibaca layanan stok, layanan notifikasi, dan gudang data sekaligus.",
                    "Layanan baru bisa memutar ulang kejadian dari awal masa simpan untuk",
                    "membangun datanya.",
                    "",
                    "Kasus kecil: kamu menambahkan layanan poin loyalitas yang harus",
                    "menghitung poin dari semua pesanan tujuh hari terakhir, tanpa mengganggu",
                    "layanan gudang yang sudah membaca topik pesanan.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pastikan masa simpan topik pesanan paling sedikit tujuh hari.",
                    "  2. Buat consumer group baru bernama poin, terpisah dari grup gudang.",
                    "  3. Atur grup itu mulai dari offset paling awal",
                    "     (auto.offset.reset=earliest) supaya membaca seluruh isi log.",
                    "  4. Simpan ID pesanan yang sudah dihitung, supaya pesan yang terbaca",
                    "     ulang sesudah rebalance nggak menggandakan poin.",
                    "  5. Commit offset sesudah poin tersimpan, bukan sebelumnya.",
                ],
            },
        ],
    },
    {
        "title": "47. Peta Message Broker dan Antrean Lainnya",
        "sections": [
            {
                "body": [
                    "RabbitMQ dan Kafka cuma dua dari banyak pilihan. Materi ini memetakan",
                    "sisanya dalam empat kelompok: broker yang kamu jalankan sendiri,",
                    "protokol khusus, layanan antrean di cloud, dan pustaka antrean tugas per",
                    "bahasa. Versi yang disebut adalah rilis terbaru per Oktober 2026.",
                ],
            },
            {
                "heading": "Tabel ringkas",
                "bahasa": "teks",
                "code": """Nama                 Jenis                   Lisensi              Catatan
-------------------  ----------------------  -------------------  -----------------------
NATS + JetStream     broker ringan           Apache-2.0           CNCF, populer di Go
Apache Pulsar        log + antrean           Apache-2.0           5.0 LTS sampai 2028
ActiveMQ Classic     broker JMS              Apache-2.0           banyak di sistem lama
Apache Artemis       broker JMS/AMQP         Apache-2.0           dulu ActiveMQ Artemis
Apache RocketMQ      broker                  Apache-2.0           kuat di ekosistem Alibaba
ZeroMQ               pustaka tanpa broker    MPL-2.0              rilis terakhir 2023
MQTT + Mosquitto     protokol IoT + broker   EPL-2.0/EDL-1.0      perangkat kecil
Amazon SQS / SNS     layanan cloud           proprietary          antrean + siaran AWS
Google Cloud Pub/Sub layanan cloud           proprietary          siaran GCP
Azure Service Bus    layanan cloud           proprietary          antrean + topik Azure
Dramatiq             antrean tugas Python    LGPL-3.0             alternatif Celery
Hangfire             antrean tugas .NET      LGPL-3.0 + Pro       dasbor bawaan
Quartz.NET           penjadwal .NET          Apache-2.0           tugas terjadwal
MassTransit          bus pesan .NET          v9 komersial         v8 masih Apache-2.0
Oban                 antrean tugas Elixir    Apache-2.0 + Pro     disimpan di Postgres
Asynq                antrean tugas Go        MIT                  di atas Redis, masih 0.x""",
            },
            {
                "heading": "Broker yang dijalankan sendiri",
                "body": [
                    "NATS adalah broker ringan berbentuk satu berkas program Go, proyek CNCF",
                    "berlisensi Apache-2.0 (versi 2.15.1). Bawaannya pub/sub tanpa",
                    "penyimpanan dengan latensi rendah sekali. JetStream adalah lapisan di",
                    "atasnya yang menambah penyimpanan, pembacaan ulang, dan consumer,",
                    "sehingga ia bisa bersaing dengan Kafka untuk beban menengah.",
                    "",
                    "Apache Pulsar memisahkan lapisan penyajian (broker) dari lapisan",
                    "penyimpanan (Apache BookKeeper), dan mendukung pola antrean maupun log",
                    "dalam satu sistem. Versi 5.0.0 adalah rilis LTS yang didukung sampai",
                    "Oktober 2028.",
                    "",
                    "Apache ActiveMQ Classic (6.3.2) adalah broker Java lama yang mengikuti",
                    "standar JMS (Java Message Service) dan masih banyak di sistem",
                    "perusahaan. Saudaranya yang lebih modern dulu bernama ActiveMQ Artemis,",
                    "sekarang berganti nama menjadi Apache Artemis (2.57.0). Apache RocketMQ",
                    "(5.5.1) berasal dari Alibaba dan kuat untuk transaksi berpesan di",
                    "e-commerce.",
                    "",
                    "ZeroMQ berbeda sendiri: ia pustaka soket, bukan server broker. Aplikasi",
                    "saling tersambung langsung dengan pola pub/sub atau permintaan-jawaban.",
                    "Rilis terakhirnya 4.3.5 tahun 2023, yang sekaligus memindahkan",
                    "lisensinya dari LGPL-3.0 ke MPL-2.0.",
                ],
            },
            {
                "heading": "MQTT dan layanan cloud",
                "body": [
                    "MQTT adalah protokol pub/sub yang hemat sekali, dirancang untuk",
                    "perangkat kecil dengan jaringan tidak stabil, misalnya sensor suhu yang",
                    "mengirim angka tiap menit. Versi yang berlaku MQTT 5.0 (2019). Eclipse",
                    "Mosquitto adalah broker MQTT yang paling sering dipakai, ditulis dengan",
                    "C, berlisensi ganda Eclipse Public License 2.0 dan Eclipse Distribution",
                    "License 1.0. Topik MQTT memakai garis miring dan wildcard + serta #,",
                    "mirip topic exchange RabbitMQ. Detailnya dibahas di kurikulum Embedded",
                    "dan IoT.",
                    "",
                    "Kalau aplikasimu sudah di cloud, layanan antrean terkelola sering lebih",
                    "murah daripada merawat broker sendiri. Amazon SQS adalah antrean",
                    "sederhana, sedangkan Amazon SNS menyiarkan satu pesan ke banyak",
                    "penerima; keduanya sering dipasangkan. Google Cloud Pub/Sub adalah",
                    "layanan siaran dengan langganan push atau pull. Azure Service Bus",
                    "menyediakan antrean dan topik dengan fitur perusahaan seperti sesi pesan",
                    "dan transaksi. Semuanya proprietary, jadi pindah penyedia berarti",
                    "mengganti kode klien.",
                ],
            },
            {
                "heading": "Pustaka antrean tugas lain",
                "body": [
                    "Dramatiq (Python, 2.2.1, LGPL-3.0) adalah alternatif Celery yang lebih",
                    "sederhana, dengan broker RabbitMQ atau Redis.",
                    "",
                    "Di .NET, Hangfire (1.8.25) menjalankan tugas latar dan tugas terjadwal",
                    "dengan dasbor web bawaan; intinya LGPL-3.0 dan ada edisi Pro berbayar.",
                    "Quartz.NET (4.5.1, Apache-2.0) adalah penjadwal ala cron; versi",
                    "Java-nya, Quartz Scheduler, juga umum di dunia Spring. MassTransit",
                    "adalah lapisan bus pesan di atas RabbitMQ, Azure Service Bus, atau SQS.",
                    "Jebakan: MassTransit v9 berlisensi komersial, sedangkan v8 ke bawah",
                    "masih Apache-2.0. Proyek belajar sebaiknya memakai v8 atau alternatif",
                    "open source seperti Wolverine.",
                    "",
                    "Oban (Elixir, 2.24.2, Apache-2.0 dengan Oban Pro berbayar) menyimpan",
                    "tugas di PostgreSQL, satu keluarga dengan Solid Queue di Rails. Asynq",
                    "(Go, 0.26.0, MIT) adalah antrean tugas di atas Redis dengan dasbor web;",
                    "versinya masih 0.x, jadi API-nya bisa berubah.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  - Tugas latar di satu aplikasi: pustaka antrean bahasamu (Celery,",
                    "    BullMQ, Sidekiq, Solid Queue, Hangfire, Oban, Asynq).",
                    "  - Banyak layanan dengan routing rumit: RabbitMQ, Artemis, atau layanan",
                    "    cloud seperti Azure Service Bus.",
                    "  - Aliran kejadian besar yang perlu diputar ulang: Kafka, Redpanda,",
                    "    Pulsar, atau JetStream.",
                    "  - Perangkat IoT: MQTT dengan Mosquitto.",
                    "  - Sudah sepenuhnya di satu cloud: SQS/SNS, Pub/Sub, atau Service Bus.",
                    "",
                    "Jebakan: memilih broker karena terdengar canggih. Setiap broker adalah",
                    "server tambahan yang harus dipantau, diperbarui, dan dicadangkan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi .NET di perusahaan sering memakai Hangfire untuk laporan malam",
                    "dan Azure Service Bus untuk pesan antar-layanan. Sistem rumah pintar",
                    "mengirim data sensor lewat MQTT ke Mosquitto, lalu satu layanan",
                    "meneruskannya ke Kafka untuk dianalisis.",
                    "",
                    "Kasus kecil: kantormu memakai ASP.NET Core dan ingin mengirim rekap",
                    "absensi tiap pukul 17.00, plus memproses unggahan berkas di latar.",
                    "Anggaran lisensi nol.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pakai Hangfire edisi open source dengan penyimpanan di database",
                    "     yang sudah ada.",
                    "  2. Daftarkan tugas berulang dengan ekspresi cron untuk rekap pukul",
                    "     17.00.",
                    "  3. Antrekan pemrosesan unggahan sebagai tugas fire-and-forget dari",
                    "     controller.",
                    "  4. Kalau nanti butuh bus pesan, pilih MassTransit v8 atau Wolverine,",
                    "     dan catat bahwa MassTransit v9 berbayar.",
                ],
            },
        ],
    },
    {
        "title": "48. Peta Cache dan Penyimpanan Memori Lainnya",
        "sections": [
            {
                "body": [
                    "Kata cache dipakai untuk tiga hal yang berbeda letaknya, dan memilih",
                    "alat yang salah adalah kesalahan yang sering terjadi.",
                    "",
                    "  - Cache lokal (in-process): tinggal di memori proses aplikasimu",
                    "    sendiri. Paling cepat karena nggak lewat jaringan, tapi tiap",
                    "    instance aplikasi punya salinan sendiri dan isinya hilang saat",
                    "    proses dimulai ulang.",
                    "  - Cache terdistribusi: server terpisah yang dipakai bersama semua",
                    "    instance, seperti Redis dan Valkey. Lebih lambat sedikit karena",
                    "    lewat jaringan, tapi semua server melihat isi yang sama.",
                    "  - Cache HTTP: berdiri di depan aplikasi dan menyimpan respons HTTP",
                    "    utuh, seperti CDN atau reverse proxy cache.",
                ],
            },
            {
                "heading": "Cache lokal paling sederhana",
                "code": """from functools import lru_cache

hitung = 0


@lru_cache(maxsize=2)
def ongkir(kota):
    global hitung
    hitung += 1
    return {"jakarta": 9000, "bandung": 12000, "medan": 25000}[kota]


for kota in ["jakarta", "jakarta", "bandung", "medan", "jakarta"]:
    print(kota, ongkir(kota))
print("dihitung:", hitung, ongkir.cache_info())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  jakarta 9000",
                    "  jakarta 9000",
                    "  bandung 12000",
                    "  medan 25000",
                    "  jakarta 9000",
                    "  dihitung: 4 CacheInfo(hits=1, misses=4, maxsize=2, currsize=2)",
                    "",
                    "Dengan maxsize=2, jakarta tergusur saat medan masuk, jadi permintaan",
                    "terakhir dihitung ulang. Itulah LRU (least recently used): yang paling",
                    "lama nggak dipakai dibuang lebih dulu. Caffeine dan Ehcache adalah versi",
                    "jauh lebih lengkap dari ide ini di dunia Java.",
                ],
            },
            {
                "heading": "Tabel ringkas",
                "bahasa": "teks",
                "code": """Nama                Letak            Bahasa  Lisensi              Status
------------------  ---------------  ------  -------------------  ----------------------
Dragonfly           terdistribusi    C++     BSL-1.1              aktif, kompatibel Redis
KeyDB               terdistribusi    C++     BSD-3-Clause         menurun, rilis 2023
Garnet              terdistribusi    C#      MIT                  aktif, dari Microsoft
Hazelcast           terdistribusi    Java    Apache-2.0 + Ent.    aktif
Varnish/Vinyl Cache cache HTTP       C       BSD-2-Clause         aktif, dua garis nama
Caffeine            lokal            Java    Apache-2.0           aktif
Ehcache             lokal/tier       Java    Apache-2.0           matang, milik IBM""",
            },
            {
                "heading": "Pesaing Redis",
                "body": [
                    "Dragonfly (2.0.2) adalah server yang memahami perintah Redis dan",
                    "Memcached, ditulis ulang dengan C++ supaya memakai semua inti CPU dalam",
                    "satu proses. Lisensinya BSL-1.1, jadi ada batasan pemakaian komersial",
                    "tertentu; baca dulu sebelum menawarkannya sebagai layanan.",
                    "",
                    "KeyDB adalah fork Redis yang multithread, BSD-3-Clause. Rilis",
                    "terakhirnya 6.3.4 pada Oktober 2023 dan sejak itu nggak ada rilis lagi.",
                    "Ia masih ada di sistem yang sudah memakainya, tapi jangan dipilih untuk",
                    "proyek baru; Valkey adalah pengganti berlisensi BSD yang aktif.",
                    "",
                    "Garnet (2.2.3, MIT) adalah server cache dari Microsoft Research yang",
                    "ditulis dengan C# dan berbicara dengan protokol Redis. Rilis 2.2.3",
                    "menghapus dukungan .NET 8.",
                    "",
                    "Hazelcast (5.7.0) adalah data grid Java: peta terdistribusi, antrean,",
                    "dan komputasi di atas memori banyak node, dengan edisi Community",
                    "Apache-2.0 dan edisi Enterprise berbayar. Ia sering ditanam langsung di",
                    "aplikasi Spring.",
                ],
            },
            {
                "heading": "Cache HTTP dan cache lokal Java",
                "body": [
                    "Varnish Cache adalah reverse proxy khusus cache HTTP yang dikonfigurasi",
                    "dengan bahasa VCL. Ia ditaruh di depan situs berita atau toko untuk",
                    "menyimpan halaman utuh. Nama ini sekarang punya dua garis keturunan:",
                    "proyek komunitas aslinya berganti nama menjadi Vinyl Cache (diumumkan",
                    "2025, rilis 9.1.0 pada September 2026), sementara perusahaan Varnish",
                    "Software meneruskan Varnish Cache. Kalau membaca tutorial, perhatikan",
                    "yang mana yang dimaksud. Lisensinya BSD-2-Clause.",
                    "",
                    "Caffeine (3.3.1, Apache-2.0) adalah cache lokal Java berkinerja tinggi",
                    "dengan kebijakan penggusuran yang lebih pintar dari LRU biasa. Spring",
                    "Boot memakainya sebagai pilihan cache lokal lewat anotasi @Cacheable.",
                    "Ehcache (3.11.1, Apache-2.0) adalah cache Java yang lebih tua, bisa",
                    "bertingkat dari memori ke disk; rilis 3.11.1 tahun 2025 adalah rilis",
                    "pertama di bawah kepemilikan IBM, dan jalur berikutnya butuh Java 17.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  - Satu instance aplikasi, data kecil, boleh hilang saat restart: cache",
                    "    lokal (lru_cache, Caffeine).",
                    "  - Banyak instance yang harus melihat isi sama: Redis atau Valkey.",
                    "    Dragonfly dan Garnet layak dicoba kalau butuh kinerja lebih dan",
                    "    lisensinya cocok.",
                    "  - Halaman utuh yang sama untuk semua pengunjung: cache HTTP di depan",
                    "    aplikasi, yaitu CDN atau Varnish/Vinyl Cache.",
                    "",
                    "Banyak sistem memakai dua lapis sekaligus: cache lokal berumur beberapa",
                    "detik di depan Redis, supaya kunci yang paling panas bahkan nggak perlu",
                    "lewat jaringan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs berita memasang Varnish atau CDN di depan halaman artikel,",
                    "sehingga lonjakan pembaca saat berita viral hampir nggak menyentuh",
                    "server aplikasi. Aplikasi Spring sering memakai Caffeine untuk tabel",
                    "referensi kecil seperti daftar provinsi.",
                    "",
                    "Kasus kecil: API Spring Boot-mu membaca daftar kode provinsi dari",
                    "database di setiap permintaan, padahal datanya hampir nggak pernah",
                    "berubah dan aplikasimu berjalan di tiga instance.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Karena data kecil dan boleh sedikit berbeda antar-instance selama",
                    "     beberapa menit, pakai cache lokal Caffeine, bukan Redis.",
                    "  2. Tandai method pengambilnya dengan @Cacheable(\"provinsi\").",
                    "  3. Atur umur entri sepuluh menit dan ukuran maksimum kecil.",
                    "  4. Kalau suatu saat data harus langsung seragam di tiga instance,",
                    "     pindahkan ke Redis atau Valkey.",
                ],
            },
        ],
    },
    {
        "title": "49. WebSocket, SSE, dan Long Polling",
        "sections": [
            {
                "body": [
                    "HTTP biasa selalu dimulai dari klien: browser bertanya, server menjawab,",
                    "selesai. Server nggak bisa tiba-tiba mengirim sesuatu kalau nggak",
                    "ditanya. Padahal banyak fitur butuh itu: pesan chat baru, notifikasi",
                    "pesanan, harga yang berubah, progres unggahan, dan jawaban chatbot AI",
                    "yang muncul kata demi kata.",
                    "",
                    "Ada empat cara untuk membuat server terasa \"mendorong\" data, dari yang",
                    "paling sederhana sampai yang paling lengkap: short polling, long",
                    "polling, Server-Sent Events, dan WebSocket.",
                ],
            },
            {
                "heading": "Short polling dan long polling",
                "body": [
                    "Short polling artinya klien bertanya berulang dengan jadwal tetap,",
                    "misalnya tiap lima detik: \"ada pesan baru?\". Gampang dibuat dengan",
                    "endpoint REST biasa. Kekurangannya, kebanyakan jawaban berbunyi \"belum",
                    "ada\", dan pesan baru bisa terlambat sampai lima detik. Seribu pengguna",
                    "berarti dua ratus permintaan per detik yang hampir semuanya sia-sia.",
                    "",
                    "Long polling memperbaikinya. Klien bertanya, dan server sengaja menahan",
                    "jawabannya sampai ada data baru atau sampai batas waktu, misalnya 30",
                    "detik. Begitu jawaban datang, klien langsung bertanya lagi. Pesan sampai",
                    "hampir seketika dan permintaan kosong berkurang. Harganya, server harus",
                    "sanggup menahan banyak koneksi yang menunggu. Long polling masih dipakai",
                    "sebagai cadangan, misalnya oleh Socket.IO saat WebSocket diblokir",
                    "jaringan kantor.",
                ],
            },
            {
                "heading": "Server-Sent Events",
                "body": [
                    "Server-Sent Events (SSE) memakai satu respons HTTP yang nggak pernah",
                    "ditutup. Server mengirim header Content-Type: text/event-stream, lalu",
                    "menulis event satu per satu kapan saja ia mau. Formatnya teks polos:",
                    "baris data: berisi isi event, baris event: opsional untuk nama jenisnya,",
                    "baris id: untuk nomor urut, dan satu baris kosong menandai akhir event.",
                    "",
                    "Di browser, objek EventSource membaca aliran itu. Kalau koneksi putus,",
                    "EventSource otomatis menyambung ulang dan mengirim header Last-Event-ID,",
                    "sehingga server bisa melanjutkan dari event terakhir yang diterima. SSE",
                    "cuma satu arah, dari server ke klien. Untuk mengirim sesuatu ke server,",
                    "klien tetap memakai permintaan HTTP biasa.",
                    "",
                    "SSE sedang naik daun karena chatbot AI. API model bahasa besar",
                    "mengalirkan jawaban token demi token lewat SSE, supaya teks muncul",
                    "sedikit demi sedikit dan nggak menunggu seluruh jawaban selesai. OpenAPI",
                    "3.2 bahkan menambahkan cara mendeskripsikan aliran seperti ini.",
                    "Spesifikasi SSE sendiri adalah bagian dari HTML Living Standard milik",
                    "WHATWG, tanpa nomor versi.",
                ],
            },
            {
                "heading": "Membentuk aliran SSE",
                "code": "def event_sse(data, event=None, id_event=None):\n    baris = []\n    if event:\n        baris.append(f\"event: {event}\")\n    if id_event is not None:\n        baris.append(f\"id: {id_event}\")\n    for potong in data.split(\"\\n\"):\n        baris.append(f\"data: {potong}\")\n    return \"\\n\".join(baris) + \"\\n\\n\"\n\n\naliran = (event_sse(\"Halo\", event=\"token\", id_event=1)\n          + event_sse(\"dunia\", event=\"token\", id_event=2)\n          + event_sse(\"baris satu\\nbaris dua\", id_event=3)\n          + event_sse(\"[SELESAI]\", event=\"tutup\"))\nprint(aliran, end=\"\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  event: token",
                    "  id: 1",
                    "  data: Halo",
                    "  ",
                    "  event: token",
                    "  id: 2",
                    "  data: dunia",
                    "  ",
                    "  id: 3",
                    "  data: baris satu",
                    "  data: baris dua",
                    "  ",
                    "  event: tutup",
                    "  data: [SELESAI]",
                    "",
                    "Data yang berisi baris baru dipecah jadi beberapa baris data:, dan",
                    "EventSource akan menyambungnya lagi dengan karakter baris baru.",
                    "",
                    "Jebakan: memasang SSE di belakang Nginx tanpa setelan apa pun. Nginx",
                    "menampung (buffer) respons dari aplikasi sebelum meneruskannya, jadi",
                    "event baru sampai ke browser bergerombol atau baru muncul di akhir.",
                    "Matikan dengan proxy_buffering off di blok location-nya, atau kirim",
                    "header X-Accel-Buffering: no dari aplikasi.",
                ],
            },
            {
                "heading": "WebSocket",
                "body": [
                    "WebSocket (RFC 6455, Desember 2011) membuka saluran dua arah yang tetap",
                    "tersambung. Ia dimulai sebagai permintaan HTTP biasa dengan header",
                    "Upgrade: websocket. Klien menyertakan Sec-WebSocket-Key berisi nilai",
                    "acak. Server menyambungnya dengan string tetap dari RFC, menghitung",
                    "SHA-1, mengubahnya jadi base64, lalu menjawab 101 Switching Protocols",
                    "dengan hasil itu di header Sec-WebSocket-Accept. Sesudah itu koneksi TCP",
                    "yang sama nggak lagi berbicara HTTP. Kedua pihak bertukar frame, yaitu",
                    "potongan pesan kecil, kapan pun mereka mau.",
                    "",
                    "Program di bawah menghitung jawaban jabat tangan dengan contoh persis",
                    "dari RFC 6455 bagian 1.3.",
                ],
            },
            {
                "heading": "Menghitung Sec-WebSocket-Accept",
                "code": """import base64
import hashlib

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def jawaban_jabat_tangan(kunci_klien):
    digest = hashlib.sha1((kunci_klien + GUID).encode("ascii")).digest()
    return base64.b64encode(digest).decode("ascii")


kunci = "dGhlIHNhbXBsZSBub25jZQ=="
print("HTTP/1.1 101 Switching Protocols")
print("Upgrade: websocket")
print("Connection: Upgrade")
print("Sec-WebSocket-Accept:", jawaban_jabat_tangan(kunci))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  HTTP/1.1 101 Switching Protocols",
                    "  Upgrade: websocket",
                    "  Connection: Upgrade",
                    "  Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=",
                    "",
                    "Kamu nggak perlu menulis ini sendiri di aplikasi sungguhan; pustaka",
                    "WebSocket sudah mengurusnya. Tapi melihatnya sekali membuat jelas kenapa",
                    "WebSocket bisa lewat port 80 dan 443 yang sama dengan HTTP. Menurut",
                    "Postman State of the API 2025, 35% responden memakai WebSocket.",
                ],
            },
            {
                "heading": "Tantangan skala",
                "body": [
                    "Koneksi real-time hidup lama, dan itu mengubah cara server diskalakan:",
                    "",
                    "  - Tiap koneksi memakan memori dan satu deskriptor berkas. Server harus",
                    "    memakai model async (event loop) supaya ribuan koneksi yang diam",
                    "    nggak menghabiskan thread.",
                    "  - Pengguna A tersambung ke server 1, pengguna B ke server 2. Supaya",
                    "    pesan A sampai ke B, server-server itu butuh jalur pesan bersama,",
                    "    biasanya Redis Pub/Sub, yang dibahas di materi Redis untuk Sesi,",
                    "    Pub/Sub, dan Antrean Tugas.",
                    "  - Koneksi bisa mati tanpa kabar karena jaringan seluler. Kirim ping",
                    "    berkala (heartbeat) dan buat klien menyambung ulang dengan jeda yang",
                    "    makin panjang.",
                    "  - Load balancer harus mendukung koneksi panjang dan, untuk beberapa",
                    "    pustaka, sticky session, yaitu pengguna yang sama selalu diarahkan",
                    "    ke server yang sama.",
                ],
            },
            {
                "heading": "Pustaka real-time",
                "body": [
                    "Socket.IO (4.8.4, MIT) adalah pustaka JavaScript paling dikenal untuk",
                    "real-time. Ia menambahkan ruang (room), acknowledgement, dan sambung",
                    "ulang otomatis, serta jatuh ke long polling kalau WebSocket gagal.",
                    "Jebakan: Socket.IO memakai protokolnya sendiri di atas WebSocket, jadi",
                    "klien Socket.IO nggak bisa tersambung ke server WebSocket polos, dan",
                    "sebaliknya.",
                    "",
                    "SignalR adalah padanannya di ASP.NET Core, ikut dirilis bersama ASP.NET",
                    "Core (versi 10.0.13 saat materi ini ditulis, MIT). Ia memilih transport",
                    "terbaik secara otomatis: WebSocket, lalu SSE, lalu long polling.",
                    "",
                    "Centrifugo (6.9.7, Apache-2.0) adalah server real-time mandiri yang",
                    "ditulis dengan Go. Backend-mu, dalam bahasa apa pun, cukup mengirim",
                    "pesan ke Centrifugo lewat API, dan Centrifugo yang mengurus ribuan",
                    "koneksi WebSocket atau SSE ke klien.",
                ],
            },
            {
                "heading": "Socket.IO di server Node",
                "bahasa": "javascript",
                "code": """const { Server } = require('socket.io');
const io = new Server(3000, { cors: { origin: 'https://toko.example' } });

io.on('connection', (socket) => {
  socket.join('pesanan:' + socket.handshake.auth.idToko);
  socket.on('chat', (teks) => {
    io.to('pesanan:' + socket.handshake.auth.idToko).emit('chat', teks);
  });
});""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi chat, papan skor pertandingan, dan dasbor pengemudi ojek daring",
                    "memakai WebSocket karena butuh dua arah. Antarmuka chatbot AI dan",
                    "notifikasi \"pesananmu sedang dikemas\" banyak yang memakai SSE karena",
                    "alirannya cuma dari server. Aplikasi lama yang belum boleh mengubah",
                    "infrastruktur sering bertahan dengan long polling.",
                    "",
                    "Kasus kecil: kamu ingin halaman status pesanan di toko onlinemu berubah",
                    "sendiri saat kurir mengambil paket, tanpa pelanggan menekan tombol muat",
                    "ulang.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Karena alirannya cuma dari server, pilih SSE, bukan WebSocket.",
                    "  2. Buat endpoint GET /pesanan/{id}/status yang menjawab dengan",
                    "     Content-Type: text/event-stream dan menulis event setiap status",
                    "     berubah.",
                    "  3. Saat status berubah di server mana pun, terbitkan pesan ke channel",
                    "     Redis pesanan:{id}; endpoint SSE berlangganan channel itu.",
                    "  4. Di Nginx, matikan proxy_buffering untuk lokasi itu dan perpanjang",
                    "     proxy_read_timeout.",
                    "  5. Di browser, pakai new EventSource(url), dan sertakan id di tiap",
                    "     event supaya sambung ulang melanjutkan dari status terakhir.",
                ],
            },
        ],
    },
    {
        "title": "50. GraphQL: Skema, Resolver, dan Server",
        "sections": [
            {
                "body": [
                    "Layar profil di aplikasi mobile butuh nama pengguna, tiga judul",
                    "postingan terakhirnya, dan jumlah suka tiap postingan. Dengan REST,",
                    "aplikasi mungkin memanggil GET /users/7, lalu GET /users/7/posts, lalu",
                    "satu panggilan lagi per postingan. Masing-masing mengembalikan lebih",
                    "banyak field dari yang dibutuhkan. Masalah pertama disebut underfetching",
                    "(satu panggilan nggak cukup), yang kedua overfetching (data kebanyakan).",
                    "",
                    "GraphQL membalik cara bertanyanya. Server menyediakan satu endpoint,",
                    "biasanya POST /graphql, dan satu skema yang menggambarkan semua data.",
                    "Klien mengirim kueri yang menyebut persis field yang ia mau, dan",
                    "jawabannya berbentuk sama dengan kuerinya. Spesifikasinya dikelola",
                    "GraphQL Foundation; edisi terbarunya September 2025, edisi baru pertama",
                    "sejak 2021. Di Postman State of the API 2025, 33% responden memakai",
                    "GraphQL.",
                ],
            },
            {
                "heading": "Skema",
                "body": [
                    "Skema ditulis dalam bahasa skema GraphQL (SDL). Tiap tipe punya field",
                    "bertipe. Tanda ! berarti nggak boleh null, dan kurung siku berarti",
                    "daftar. Tiga tipe akar menjadi pintu masuk: Query untuk membaca,",
                    "Mutation untuk mengubah, dan Subscription untuk berlangganan event",
                    "(biasanya lewat WebSocket).",
                ],
            },
            {
                "heading": "Skema kecil",
                "bahasa": "graphql",
                "code": """type User {
  id: ID!
  name: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  likes: Int!
}

type Query {
  me: User
  users: [User!]!
}

type Mutation {
  createPost(title: String!): Post!
}""",
            },
            {
                "heading": "Kueri dan jawabannya",
                "bahasa": "graphql",
                "code": """query Profil {
  me {
    name
    posts {
      title
      likes
    }
  }
}

# jawaban server (JSON):
# {"data": {"me": {"name": "Budi",
#   "posts": [{"title": "Belajar API", "likes": 12}]}}}""",
            },
            {
                "heading": "Resolver dan masalah N+1",
                "body": [
                    "Di server, tiap field punya resolver, yaitu fungsi yang mengambil",
                    "nilainya. Resolver users mengambil daftar pengguna, lalu untuk setiap",
                    "pengguna resolver posts dipanggil. Kalau tiap panggilan resolver posts",
                    "menjalankan satu kueri SQL, daftar 100 pengguna berarti 1 + 100 kueri.",
                    "Ini masalah N+1 yang sama dengan di ORM, cuma sekarang muncul dari",
                    "bentuk kueri klien.",
                    "",
                    "Solusi bakunya DataLoader: resolver nggak langsung mengambil data, tapi",
                    "mendaftarkan kunci yang ia butuhkan. Sesudah semua resolver di satu",
                    "tingkat selesai mendaftar, DataLoader menjalankan satu kueri untuk semua",
                    "kunci sekaligus (misalnya WHERE user_id IN (...)) lalu membagikan",
                    "hasilnya. Program di bawah menunjukkan bedanya dengan menghitung kueri.",
                ],
            },
            {
                "heading": "Menghitung kueri: N+1 lawan batch",
                "code": """USERS = [{"id": 1, "name": "Budi"}, {"id": 2, "name": "Sari"},
         {"id": 3, "name": "Andi"}]
POSTS = [{"user": 1, "title": "Belajar API"}, {"user": 1, "title": "Cache"},
         {"user": 3, "title": "Kafka"}]
log = []


def kueri_post_milik(id_user):
    log.append(f"SELECT * FROM posts WHERE user_id = {id_user}")
    return [p for p in POSTS if p["user"] == id_user]


def kueri_post_batch(daftar_id):
    isi = ", ".join(str(i) for i in daftar_id)
    log.append(f"SELECT * FROM posts WHERE user_id IN ({isi})")
    return {i: [p for p in POSTS if p["user"] == i] for i in daftar_id}


def resolve_naif():
    return {u["name"]: [p["title"] for p in kueri_post_milik(u["id"])]
            for u in USERS}


def resolve_dataloader():
    kunci = [u["id"] for u in USERS]
    hasil = kueri_post_batch(kunci)
    return {u["name"]: [p["title"] for p in hasil[u["id"]]] for u in USERS}


print(resolve_naif())
print("kueri:", len(log))
log.clear()
print(resolve_dataloader())
print("kueri:", len(log), "->", log[0])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  {'Budi': ['Belajar API', 'Cache'], 'Sari': [], 'Andi': ['Kafka']}",
                    "  kueri: 3",
                    "  {'Budi': ['Belajar API', 'Cache'], 'Sari': [], 'Andi': ['Kafka']}",
                    "  kueri: 1 -> SELECT * FROM posts WHERE user_id IN (1, 2, 3)",
                    "",
                    "Jawabannya sama, kuerinya turun dari tiga jadi satu. Dengan 100",
                    "pengguna, bedanya 100 lawan 1. Pustaka DataLoader ada untuk hampir semua",
                    "server GraphQL.",
                ],
            },
            {
                "heading": "Hal yang berbeda dari REST",
                "body": [
                    "  - Kode status: GraphQL biasanya menjawab 200 walaupun ada kesalahan,",
                    "    dan kesalahannya ada di array errors di body. Pemantauan yang cuma",
                    "    melihat kode status nggak akan melihatnya.",
                    "  - Cache HTTP: semua kueri lewat POST ke satu URL, jadi CDN dan cache",
                    "    browser nggak bisa bekerja seperti di REST. Solusi yang umum adalah",
                    "    persisted query, yaitu kueri disimpan di server dan dipanggil dengan",
                    "    ID lewat GET.",
                    "  - Keamanan: klien bisa mengirim kueri yang terlalu dalam, misalnya",
                    "    user, posts, author, posts, terus berulang, yang membebani server.",
                    "    Pasang batas kedalaman dan batas kompleksitas kueri.",
                    "  - Otorisasi tetap per field atau per objek. Skema yang rapi nggak",
                    "    otomatis mencegah celah otorisasi per objek dari materi otorisasi.",
                    "",
                    "Pilih GraphQL kalau kliennya banyak jenis (web, mobile, mitra) dengan",
                    "kebutuhan data yang berbeda-beda. Untuk API publik sederhana atau",
                    "layanan yang butuh cache CDN, REST biasanya lebih mudah.",
                ],
            },
            {
                "heading": "Server GraphQL per bahasa",
                "body": [
                    "Versi berikut adalah rilis terbaru per Oktober 2026:",
                    "",
                    "  - JavaScript/TypeScript: Apollo Server (5.5.1, MIT; jalur v4 sudah",
                    "    habis masa dukungannya) dan GraphQL Yoga (5.24.6, MIT) yang lebih",
                    "    netral platform. Keduanya dibangun di atas graphql-js (paket",
                    "    graphql, 17.0.2), implementasi referensi spesifikasinya. Banyak",
                    "    pustaka masih terkunci ke graphql 16, jadi periksa kecocokan sebelum",
                    "    naik ke 17.",
                    "  - .NET: Hot Chocolate (16.6.8, MIT).",
                    "  - Java: graphql-java (26.1, MIT), dan Spring for GraphQL yang",
                    "    membungkusnya untuk Spring Boot.",
                    "  - Python: Strawberry (0.336.0, MIT) yang mendefinisikan skema dari",
                    "    type hints. Graphene (3.4.3) sedang menurun; rilis terakhirnya",
                    "    November 2024, jadi untuk proyek baru pilih Strawberry.",
                    "  - Go: gqlgen (0.17.95, MIT) yang membangkitkan kode Go dari berkas",
                    "    skema.",
                    "  - Rust: async-graphql (7.2.1, MIT atau Apache-2.0).",
                    "",
                    "Ada dua aliran: schema-first (tulis SDL dulu, lalu resolver, seperti",
                    "gqlgen dan Apollo) dan code-first (tulis kelas atau fungsi, skema",
                    "dibangkitkan, seperti Strawberry dan Hot Chocolate).",
                ],
            },
            {
                "heading": "Apollo Server",
                "bahasa": "javascript",
                "code": """import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

const typeDefs = `
  type Post { title: String!, likes: Int! }
  type Query { posts: [Post!]! }
`;
const resolvers = {
  Query: { posts: () => [{ title: 'Belajar API', likes: 12 }] },
};

const server = new ApolloServer({ typeDefs, resolvers });
const { url } = await startStandaloneServer(server, { listen: { port: 4000 } });
console.log('siap di', url);""",
            },
            {
                "heading": "Strawberry (Python)",
                "code": """import strawberry


@strawberry.type
class Post:
    title: str
    likes: int


@strawberry.type
class Query:
    @strawberry.field
    def posts(self) -> list[Post]:
        return [Post(title="Belajar API", likes=12)]


schema = strawberry.Schema(query=Query)
hasil = schema.execute_sync("{ posts { title } }")
print(hasil.data)""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "GitHub dan Shopify menyediakan API publik berbasis GraphQL di samping",
                    "REST. Di dalam perusahaan, GraphQL sering dipasang sebagai lapisan",
                    "gabungan di depan beberapa layanan, supaya aplikasi mobile cukup",
                    "memanggil satu endpoint.",
                    "",
                    "Kasus kecil: aplikasi mobile tokomu memanggil lima endpoint REST untuk",
                    "menampilkan satu halaman beranda, dan tiap pembaruan layar butuh",
                    "endpoint baru dari tim backend.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tulis skema GraphQL untuk data beranda: produk unggulan, kategori,",
                    "     dan keranjang pengguna.",
                    "  2. Buat resolver yang memanggil layanan atau tabel yang sudah ada,",
                    "     tanpa mengubah logika bisnisnya.",
                    "  3. Pasang DataLoader di resolver yang mengambil data per produk supaya",
                    "     nggak terjadi N+1.",
                    "  4. Batasi kedalaman kueri dan aktifkan persisted query untuk aplikasi",
                    "     mobile.",
                    "  5. Pantau array errors di respons, di samping kode status HTTP.",
                ],
            },
        ],
    },
    {
        "title": "51. gRPC, Protobuf, dan Gaya RPC Lain",
        "sections": [
            {
                "body": [
                    "REST berpikir dalam sumber daya: ada pesanan, ambil atau ubah. RPC",
                    "(remote procedure call) berpikir dalam fungsi: panggil",
                    "HitungOngkir(asal, tujuan, berat) di server lain seolah-olah fungsi",
                    "lokal. Gaya ini cocok untuk komunikasi antar-layanan di dalam satu",
                    "sistem, tempat kedua sisi dikendalikan tim yang sama dan yang paling",
                    "penting adalah cepat dan bertipe jelas.",
                    "",
                    "Materi ini membahas gRPC beserta Protocol Buffers. Sesudahnya ada peta",
                    "gaya RPC lain: tRPC dan oRPC di dunia TypeScript, protokol berbasis JSON",
                    "yang dipakai editor kode dan alat AI, serta protokol XML dan OData di",
                    "sistem perusahaan yang lebih tua.",
                ],
            },
            {
                "heading": "Protocol Buffers",
                "body": [
                    "Protocol Buffers, biasa disebut protobuf, adalah format serialisasi dari",
                    "Google. Kamu menulis bentuk pesan di berkas .proto, lalu kompilator",
                    "protoc membangkitkan kelas untuk banyak bahasa. Datanya dikirim dalam",
                    "bentuk biner yang ringkas, bukan teks seperti JSON.",
                    "",
                    "Di kabel, yang dikirim adalah nomor field, sedangkan namanya cuma ada di",
                    "berkas .proto. Karena itu nomor field nggak boleh diubah sesudah",
                    "dipakai. Field yang dihapus nomornya wajib ditandai reserved supaya",
                    "nggak dipakai ulang; kalau dipakai ulang, klien lama akan membaca data",
                    "baru dengan arti yang salah.",
                    "",
                    "Protobuf berlisensi BSD-3-Clause. Versi terbarunya saat materi ini",
                    "ditulis adalah v36.2. Sejak 2023, berkas .proto memakai editions",
                    "(edition = \"2023\" atau \"2024\") sebagai pengganti baris syntax",
                    "proto2/proto3, walau berkas proto3 lama tetap didukung.",
                ],
            },
            {
                "heading": "Berkas ongkir.proto",
                "bahasa": "protobuf",
                "code": """syntax = "proto3";

package ongkir.v1;

service Ongkir {
  rpc Hitung (PermintaanOngkir) returns (HasilOngkir);
  rpc PantauKurir (IdPaket) returns (stream PosisiKurir);
}

message PermintaanOngkir {
  string asal = 1;
  string tujuan = 2;
  int32 berat_gram = 3;
  reserved 4;            // dulu 'kode_promo', jangan dipakai ulang
}

message HasilOngkir {
  int64 biaya = 1;
  int32 estimasi_hari = 2;
}

message IdPaket { string id = 1; }
message PosisiKurir { double lat = 1; double lon = 2; }""",
            },
            {
                "heading": "Seperti apa bentuk birinya",
                "body": [
                    "Supaya \"biner yang ringkas\" nggak cuma slogan, program di bawah",
                    "mengodekan pesan dengan tangan, persis contoh di dokumentasi resmi",
                    "protobuf. Tiap field diawali satu byte tag berisi nomor field dan jenis",
                    "datanya. Angka disimpan sebagai varint: tujuh bit per byte, dan bit",
                    "tertinggi menandai masih ada byte berikutnya.",
                ],
            },
            {
                "heading": "Mengodekan protobuf dengan tangan",
                "code": """import json


def varint(n):
    hasil = bytearray()
    while True:
        tujuh = n & 0x7F
        n >>= 7
        if n:
            hasil.append(tujuh | 0x80)
        else:
            hasil.append(tujuh)
            return bytes(hasil)


def field_angka(nomor, nilai):
    return varint(nomor << 3 | 0) + varint(nilai)


def field_teks(nomor, teks):
    data = teks.encode("utf-8")
    return varint(nomor << 3 | 2) + varint(len(data)) + data


pesan = field_angka(1, 150)
print("a=150         ->", pesan.hex(" "))
pesan2 = field_angka(1, 150) + field_teks(2, "testing")
print("a=150 b=testing ->", pesan2.hex(" "), f"({len(pesan2)} byte)")
teks_json = json.dumps({"a": 150, "b": "testing"}, separators=(",", ":"))
print("JSON yang sama ->", teks_json, f"({len(teks_json)} byte)")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  a=150         -> 08 96 01",
                    "  a=150 b=testing -> 08 96 01 12 07 74 65 73 74 69 6e 67 (12 byte)",
                    "  JSON yang sama -> {\"a\":150,\"b\":\"testing\"} (23 byte)",
                    "",
                    "Byte 08 artinya field nomor 1 berjenis varint, lalu 96 01 adalah 150.",
                    "Pesan protobuf kira-kira separuh ukuran JSON-nya, dan selisihnya makin",
                    "besar untuk pesan dengan banyak angka.",
                ],
            },
            {
                "heading": "gRPC",
                "body": [
                    "gRPC adalah kerangka RPC yang memakai protobuf untuk pesan dan HTTP/2",
                    "untuk transport. Dari satu berkas .proto, protoc membangkitkan stub",
                    "klien (objek dengan method Hitung yang tinggal dipanggil) dan kerangka",
                    "server untuk Go, Java, Python, C#, Node.js, C++, dan lainnya; di Rust",
                    "lewat pustaka tonic. Klien Go bisa memanggil server Java tanpa ada yang",
                    "menulis kode pengurai.",
                    "",
                    "gRPC punya empat jenis panggilan: unary (satu permintaan satu jawaban),",
                    "server streaming (seperti PantauKurir di atas), client streaming, dan",
                    "bidirectional streaming. Ia juga membawa deadline: klien menentukan",
                    "batas waktu, dan kalau lewat, panggilan dibatalkan di kedua sisi.",
                    "",
                    "gRPC adalah proyek CNCF berlisensi Apache-2.0; rilis inti terbarunya",
                    "1.84.0 (September 2026), dan tiap bahasa punya penomoran sendiri.",
                    "Keterbatasannya: browser nggak bisa memanggil gRPC secara langsung",
                    "karena nggak memberi akses ke frame HTTP/2. Untuk itu ada gRPC-Web dan",
                    "Connect, yang menerjemahkan panggilan dari browser. Data biner juga",
                    "nggak bisa dibaca mata atau dicoba dengan curl biasa, jadi butuh alat",
                    "seperti grpcurl.",
                ],
            },
            {
                "heading": "tRPC dan oRPC",
                "body": [
                    "Kalau frontend dan backend sama-sama TypeScript dan ada di satu",
                    "repositori, tRPC menawarkan RPC tanpa berkas skema dan tanpa pembangkit",
                    "kode. Tipe fungsi di server langsung dibaca TypeScript di klien,",
                    "sehingga salah ketik nama field sudah ketahuan di editor. Versi",
                    "stabilnya 11.19.0 (MIT). Keterikatan itu juga batasannya: API tRPC nggak",
                    "cocok untuk klien bahasa lain atau API publik.",
                    "",
                    "oRPC (1.15.7, MIT) adalah pendatang baru dengan ide yang sama, ditambah",
                    "kemampuan membangkitkan dokumen OpenAPI supaya klien non-TypeScript",
                    "tetap bisa memakainya. Di survei State of JS 2025, oRPC mendapat 34",
                    "sebutan di isian bebas, tertinggi di daftar itu.",
                ],
            },
            {
                "heading": "Contoh tRPC",
                "bahasa": "typescript",
                "code": """import { initTRPC } from '@trpc/server';
import { z } from 'zod';

const t = initTRPC.create();

export const appRouter = t.router({
  hitungOngkir: t.procedure
    .input(z.object({ asal: z.string(), tujuan: z.string(), berat: z.number() }))
    .query(({ input }) => ({ biaya: 9000 + Math.ceil(input.berat / 1000) * 2000 })),
});

export type AppRouter = typeof appRouter;""",
            },
            {
                "heading": "JSON-RPC 2.0, SOAP, dan OData",
                "body": [
                    "JSON-RPC 2.0 adalah protokol RPC paling sederhana: permintaan berupa",
                    "objek JSON berisi jsonrpc, method, params, dan id; jawabannya berisi",
                    "result atau error dengan id yang sama. Permintaan tanpa id disebut",
                    "notifikasi dan nggak dijawab. Beberapa permintaan bisa dikirim sekaligus",
                    "dalam satu array (batch). Spesifikasinya nggak berubah sejak 2013, tapi",
                    "hidup lagi karena dipakai Language Server Protocol (penghubung editor",
                    "kode dengan pemeriksa bahasa) dan Model Context Protocol (penghubung",
                    "aplikasi AI dengan alat). Latihan bab ini memintamu menulis servernya.",
                    "",
                    "SOAP (versi 1.2, rekomendasi W3C 2007) adalah generasi RPC sebelum REST",
                    "populer: pesannya amplop XML, dan kontraknya ditulis dalam WSDL.",
                    "Statusnya menurun dan nggak dipilih untuk proyek baru, tapi kamu masih",
                    "akan menemuinya saat mengintegrasikan sistem bank, asuransi, atau",
                    "instansi lama. Cukup bisa membaca WSDL-nya dan memanggilnya dengan",
                    "pustaka klien.",
                    "",
                    "OData (versi 4.01, standar terbuka) adalah aturan REST dengan bahasa",
                    "kueri di URL, misalnya /Produk?$filter=harga lt",
                    "50000&$select=nama&$top=10. Ia kuat di ekosistem Microsoft dan SAP,",
                    "jarang di luar itu.",
                ],
            },
            {
                "heading": "Bentuk pesannya",
                "bahasa": "json",
                "code": """--> {"jsonrpc": "2.0", "method": "hitungOngkir",
     "params": {"asal": "Bandung", "tujuan": "Medan", "berat": 1200}, "id": 7}
<-- {"jsonrpc": "2.0", "result": {"biaya": 13000}, "id": 7}

--> {"jsonrpc": "2.0", "method": "tidakAda", "id": 8}
<-- {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 8}""",
            },
            {
                "heading": "Amplop SOAP",
                "bahasa": "xml",
                "code": """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:o="http://kurir.example/ongkir">
  <soap:Body>
    <o:HitungOngkir>
      <o:Asal>Bandung</o:Asal>
      <o:Tujuan>Medan</o:Tujuan>
      <o:BeratGram>1200</o:BeratGram>
    </o:HitungOngkir>
  </soap:Body>
</soap:Envelope>""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem dengan puluhan layanan internal, seperti platform pembayaran dan",
                    "logistik, banyak memakai gRPC antar-layanan karena pesannya kecil dan",
                    "kontraknya bertipe. API ke luar tetap REST atau GraphQL. Editor seperti",
                    "VS Code berbicara dengan server bahasa lewat protokol JSON tadi, dan",
                    "banyak integrasi lama ke bank masih memakai amplop XML.",
                    "",
                    "Kasus kecil: layanan checkout (Go) memanggil layanan ongkir (Java) lewat",
                    "REST JSON. Nama field sering nggak cocok setelah salah satu tim",
                    "mengubahnya, dan bug baru ketahuan di produksi.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tulis kontraknya di ongkir.proto dan simpan di repositori bersama",
                    "     yang dipakai kedua tim.",
                    "  2. Bangkitkan stub Go untuk checkout dan kerangka server Java untuk",
                    "     ongkir dengan protoc di pipeline CI.",
                    "  3. Pasang deadline, misalnya 500 milidetik, di setiap panggilan dari",
                    "     checkout.",
                    "  4. Kalau field dihapus, tandai nomornya reserved; jangan pernah",
                    "     memakai ulang nomor lama.",
                    "  5. Biarkan API publik untuk aplikasi mobile tetap REST, dan pakai gRPC",
                    "     hanya di dalam jaringan internal.",
                ],
            },
        ],
    },
    {
        "title": "52. Nginx Sebagai Reverse Proxy untuk API",
        "sections": [
            {
                "body": [
                    "Aplikasi Flask, Express, atau Laravel-mu sudah jalan di localhost:8000.",
                    "Untuk dibuka orang lain, kamu bisa saja membuka port itu langsung ke",
                    "internet. Masalahnya, server aplikasi biasanya nggak dirancang untuk",
                    "berhadapan langsung dengan internet: ia lemah menghadapi klien yang",
                    "lambat, nggak mengurus HTTPS, dan buang tenaga kalau harus menyajikan",
                    "gambar dan berkas CSS.",
                    "",
                    "Karena itu di depan aplikasi hampir selalu dipasang reverse proxy, yaitu",
                    "server yang menerima semua permintaan dari luar lalu meneruskannya ke",
                    "aplikasi di belakangnya. Tugasnya:",
                    "",
                    "  - Mengurus HTTPS (TLS termination), jadi aplikasi cukup berbicara HTTP",
                    "    biasa di jaringan dalam.",
                    "  - Menyajikan berkas statis langsung dari disk, jauh lebih cepat",
                    "    daripada lewat kode aplikasi.",
                    "  - Menampung permintaan dari klien yang lambat (buffering), supaya",
                    "    worker aplikasi nggak tertahan menunggu ponsel dengan sinyal lemah.",
                    "  - Membagi beban ke beberapa instance aplikasi (load balancing),",
                    "    membatasi ukuran unggahan, dan mengompres respons.",
                    "",
                    "Nginx adalah reverse proxy yang paling sering dipakai untuk itu, dan",
                    "roadmap.sh Backend merekomendasikannya di bagian Web Servers. Ia ditulis",
                    "dengan C dan berlisensi BSD-2-Clause.",
                ],
            },
            {
                "heading": "Versi stable dan mainline",
                "body": [
                    "Nginx punya dua jalur rilis. Mainline (bernomor minor ganjil) berisi",
                    "fitur terbaru, sedangkan stable (bernomor minor genap) cuma menerima",
                    "perbaikan penting. Saat materi ini ditulis (Oktober 2026), versi stable",
                    "terbarunya 1.30.6 dan mainline 1.31.7, dirilis 14 Oktober 2026 dengan",
                    "tambalan lima celah keamanan. Untuk server pertamamu, paket nginx dari",
                    "distro sudah cukup, asal rajin diperbarui.",
                    "",
                    "Jangan tertukar dengan Nginx Unit, server aplikasi terpisah buatan tim",
                    "yang sama. Proyek Unit sudah diarsipkan pada 8 Oktober 2025, jadi jangan",
                    "dipilih untuk proyek baru.",
                ],
            },
            {
                "heading": "Konfigurasi minimal untuk API",
                "bahasa": "nginx",
                "code": """upstream aplikasi {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;          # instance kedua, dibagi bergiliran
}

server {
    listen 80;
    server_name api.toko.example;
    client_max_body_size 10m;       # batas unggahan

    location /static/ {
        root /srv/toko;             # /static/logo.png -> /srv/toko/static/logo.png
        expires 7d;
    }

    location /api/ {
        proxy_pass http://aplikasi;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api/stream/ {
        proxy_pass http://aplikasi;
        proxy_buffering off;        # wajib untuk SSE
        proxy_read_timeout 1h;
    }
}""",
            },
            {
                "heading": "Cara membacanya",
                "body": [
                    "Blok upstream memberi nama ke kelompok server aplikasi. Blok server",
                    "mewakili satu situs, dipilih menurut listen dan server_name. Di",
                    "dalamnya, blok location menentukan apa yang dilakukan untuk tiap awalan",
                    "URL.",
                    "",
                    "Nginx memilih location dengan urutan ini:",
                    "",
                    "  1. Kecocokan persis (location = /path) menang lebih dulu.",
                    "  2. Kalau nggak ada, dicari awalan terpanjang. Awalan yang ditandai ^~",
                    "     langsung dipakai.",
                    "  3. Kalau nggak, location regex (~ atau ~*) diperiksa sesuai urutan",
                    "     tulis, dan yang pertama cocok menang.",
                    "  4. Kalau nggak ada regex yang cocok, awalan terpanjang tadi yang",
                    "     dipakai.",
                    "",
                    "Karena itu permintaan /api/stream/harga masuk ke blok ketiga, yang",
                    "awalannya lebih panjang daripada blok /api/.",
                    "",
                    "Empat baris proxy_set_header itu penting. Tanpa mereka, aplikasimu",
                    "melihat semua permintaan datang dari 127.0.0.1 lewat HTTP biasa.",
                    "Framework membaca X-Forwarded-Proto untuk tahu bahwa pengguna aslinya",
                    "memakai HTTPS, misalnya saat membuat URL redirect atau memasang cookie",
                    "Secure.",
                ],
            },
            {
                "heading": "Jebakan garis miring di proxy_pass",
                "body": [
                    "Jebakan: menambah atau membuang satu garis miring di proxy_pass mengubah",
                    "URL yang diterima aplikasi. Kalau proxy_pass cuma berisi alamat tanpa",
                    "path (http://aplikasi), URL diteruskan apa adanya. Kalau ada path,",
                    "termasuk satu garis miring saja (http://aplikasi/), bagian URL yang",
                    "cocok dengan location diganti dengan path itu. Program di bawah meniru",
                    "aturan itu.",
                ],
            },
            {
                "heading": "Meniru aturan proxy_pass",
                "code": """def diteruskan_ke(location, proxy_pass, uri):
    sisa = proxy_pass.split("://", 1)[1]
    host, garis, path = sisa.partition("/")
    if not garis:
        return uri
    return "/" + path + uri[len(location):]


kasus = [
    ("/api/", "http://aplikasi", "/api/produk"),
    ("/api/", "http://aplikasi/", "/api/produk"),
    ("/api/", "http://aplikasi/v2/", "/api/produk"),
    ("/api", "http://aplikasi/", "/api/produk"),
]
for location, proxy_pass, uri in kasus:
    hasil = diteruskan_ke(location, proxy_pass, uri)
    print(f"location {location:6} proxy_pass {proxy_pass:20} {uri} -> {hasil}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  location /api/  proxy_pass http://aplikasi      /api/produk -> /api/produk",
                    "  location /api/  proxy_pass http://aplikasi/     /api/produk -> /produk",
                    "  location /api/  proxy_pass http://aplikasi/v2/  /api/produk -> /v2/produk",
                    "  location /api   proxy_pass http://aplikasi/     /api/produk -> //produk",
                    "",
                    "Baris terakhir adalah kesalahan klasik: location tanpa garis miring di",
                    "ujung dipasangkan dengan proxy_pass bergaris miring, dan aplikasi",
                    "menerima //produk lalu menjawab 404. Pasangkan garis miringnya: keduanya",
                    "pakai, atau keduanya nggak.",
                ],
            },
            {
                "heading": "Menguji dan memuat ulang",
                "bahasa": "terminal",
                "code": """sudo nginx -t                    # periksa sintaks sebelum dipakai
sudo systemctl reload nginx      # muat konfigurasi baru tanpa memutus koneksi
sudo tail -f /var/log/nginx/error.log

# khusus Fedora/RHEL: izinkan Nginx tersambung ke aplikasi di port lain
sudo setsebool -P httpd_can_network_connect 1""",
            },
            {
                "heading": "Kesalahan yang sering muncul",
                "body": [
                    "  - 502 Bad Gateway: Nginx nggak bisa menghubungi aplikasi. Biasanya",
                    "    aplikasinya mati atau mendengar di port lain. Di Fedora, penyebab",
                    "    yang sering terlupa adalah SELinux yang melarang Nginx membuka",
                    "    koneksi jaringan; error.log akan menyebut permission denied, dan",
                    "    perintah setsebool di atas membukanya.",
                    "  - 504 Gateway Timeout: aplikasi terlalu lama menjawab. Perbaiki kueri",
                    "    yang lambat atau pindahkan kerja berat ke antrean tugas, jangan",
                    "    buru-buru menaikkan proxy_read_timeout.",
                    "  - 413 Request Entity Too Large: unggahan melebihi",
                    "    client_max_body_size, yang bawaannya cuma 1 MB.",
                    "  - Aplikasi mempercayai X-Forwarded-For dari siapa saja. Header itu",
                    "    bisa dipalsukan klien, jadi atur framework supaya cuma",
                    "    mempercayainya dari alamat proxy-mu sendiri.",
                    "",
                    "Memasang sertifikat HTTPS dengan Certbot, menjalankan Nginx di",
                    "kontainer, dan gateway di cloud dibahas di kurikulum DevOps dan Cloud.",
                    "Unit systemd untuk menjalankan aplikasimu dibahas di kurikulum CLI",
                    "Fedora.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir setiap VPS yang menjalankan aplikasi web punya Nginx atau server",
                    "sejenis di depannya. Nginx mendengar di port 80 dan 443. Gunicorn,",
                    "PHP-FPM, Puma, atau Node mendengar di port lokal yang nggak bisa",
                    "dijangkau dari luar.",
                    "",
                    "Kasus kecil: kamu menyewa VPS Fedora untuk API FastAPI tokomu. Aplikasi",
                    "jalan di 127.0.0.1:8000, gambar produk ada di /srv/toko/static, dan",
                    "halaman status pesanan memakai SSE.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang nginx dari repositori distro dan buat berkas",
                    "     /etc/nginx/conf.d/toko.conf berisi blok server seperti contoh di",
                    "     atas.",
                    "  2. Arahkan location /static/ ke /srv/toko dengan root, dan location",
                    "     /api/ ke upstream aplikasi lengkap dengan empat proxy_set_header.",
                    "  3. Buat location khusus untuk aliran SSE dengan proxy_buffering off",
                    "     dan proxy_read_timeout yang panjang.",
                    "  4. Jalankan nginx -t, nyalakan setsebool httpd_can_network_connect,",
                    "     lalu systemctl reload nginx.",
                    "  5. Uji dengan curl -i http://api.toko.example/api/produk dan baca",
                    "     error.log kalau muncul 502.",
                ],
            },
        ],
    },
    {
        "title": "53. Server Aplikasi di Belakang Nginx",
        "sections": [
            {
                "body": [
                    "Nginx nggak bisa menjalankan kode Python, PHP, atau Ruby. Yang",
                    "menjalankannya adalah server aplikasi: program yang memuat kodemu,",
                    "menyiapkan beberapa worker, dan menerjemahkan permintaan HTTP ke kontrak",
                    "bahasamu. Di materi Aplikasi Sebagai Fungsi: WSGI, ASGI, dan Rack kamu",
                    "sudah melihat kontrak itu: aplikasi adalah fungsi, dan server",
                    "aplikasilah yang memanggilnya.",
                ],
            },
            {
                "heading": "Server aplikasi per bahasa",
                "bahasa": "teks",
                "code": """Bahasa   Server aplikasi        Protokol ke aplikasi   Versi (Okt 2026)  Lisensi
-------  ---------------------  ---------------------  ----------------  ------------
Python   Gunicorn               WSGI                   26.2.0            MIT
Python   Uvicorn                ASGI                   0.54.0            BSD-3-Clause
PHP      PHP-FPM                FastCGI dari Nginx     PHP 8.5.10        PHP License
Ruby     Puma                   Rack                   8.0.2             BSD-3-Clause
C#       Kestrel                ASP.NET Core           10.0.13           MIT
Java     Apache Tomcat          Jakarta Servlet        11.0.27           Apache-2.0
Node.js  modul http + PM2       proses Node langsung   PM2 7.0.4         AGPL-3.0""",
            },
            {
                "heading": "Python: Gunicorn dan Uvicorn",
                "body": [
                    "Gunicorn menjalankan aplikasi Python sinkron seperti Flask dan Django.",
                    "Ia membuat satu proses master yang mengawasi beberapa proses worker;",
                    "kalau satu worker mati, master menggantinya. Dokumentasi Gunicorn",
                    "menyarankan jumlah worker awal (2 x jumlah inti CPU) + 1, lalu",
                    "disesuaikan dengan hasil pengukuran. Server dua inti berarti lima",
                    "worker.",
                    "",
                    "Uvicorn menjalankan aplikasi ASGI seperti FastAPI dan Starlette, memakai",
                    "event loop sehingga satu worker bisa melayani banyak koneksi yang sedang",
                    "menunggu. Versinya masih 0.x. Uvicorn bisa menjalankan beberapa worker",
                    "sendiri lewat opsi --workers. Alternatif yang lebih baru adalah Granian",
                    "(ditulis dengan Rust) dan Hypercorn.",
                ],
            },
            {
                "heading": "Menjalankannya",
                "bahasa": "terminal",
                "code": """# Flask/Django (WSGI), 5 worker, cuma mendengar di localhost
gunicorn --workers 5 --bind 127.0.0.1:8000 toko.wsgi:application

# FastAPI (ASGI), 4 worker
uvicorn toko.main:app --host 127.0.0.1 --port 8000 --workers 4""",
            },
            {
                "heading": "PHP, Ruby, .NET, Java, dan Node",
                "body": [
                    "PHP-FPM (FastCGI Process Manager) adalah cara standar menjalankan PHP di",
                    "belakang Nginx. Nginx meneruskan permintaan berkas .php lewat protokol",
                    "FastCGI ke soket PHP-FPM, dan PHP-FPM mengatur kolam proses worker.",
                    "Setelan terpentingnya pm.max_children, yaitu jumlah maksimum proses:",
                    "kebanyakan berarti RAM habis, terlalu sedikit berarti permintaan antre.",
                    "Model ini sekarang ditantang runtime worker seperti FrankenPHP,",
                    "RoadRunner, dan Swoole yang dibahas di materi peta berikutnya.",
                    "",
                    "Puma adalah server Rack bawaan Rails. Ia menggabungkan beberapa proses",
                    "worker dengan beberapa thread per worker. Rails 8 juga memperkenalkan",
                    "Thruster, proxy HTTP/2 kecil yang bisa dipasang di depan Puma.",
                    "",
                    "Kestrel adalah server bawaan ASP.NET Core yang ikut terpasang di setiap",
                    "aplikasi .NET. Dokumentasi resmi Microsoft punya panduan menjalankan",
                    "aplikasi ASP.NET Core di Linux dengan Nginx di depannya, yang cocok",
                    "untuk VPS Fedora.",
                    "",
                    "Apache Tomcat adalah wadah servlet Java. Spring Boot menanamkan Tomcat",
                    "di dalam berkas jar, jadi kamu jarang memasangnya terpisah. Jebakan:",
                    "Tomcat 10 ke atas memakai paket jakarta.*, sedangkan Tomcat 9 (9.0.123)",
                    "masih javax.*. Aplikasi lama nggak bisa dipindah ke Tomcat baru tanpa",
                    "mengganti import.",
                    "",
                    "Node.js sudah membawa server HTTP sendiri, jadi yang dibutuhkan cuma",
                    "pengawas proses. PM2 menjaga proses tetap hidup, menjalankan beberapa",
                    "instance, dan menyimpan log. Lisensinya AGPL-3.0, dan itu berpengaruh",
                    "kalau kamu memodifikasi dan menyebarkannya. Di server yang memakai",
                    "Docker atau systemd, PM2 sering nggak diperlukan lagi.",
                ],
            },
            {
                "heading": "The Twelve-Factor App",
                "body": [
                    "The Twelve-Factor App adalah kumpulan dua belas prinsip untuk aplikasi",
                    "yang gampang di-deploy, ditulis tim Heroku dan sejak 2024 dikelola",
                    "sebagai proyek open source. Prinsip yang paling langsung terasa saat",
                    "deploy:",
                    "",
                    "  - Konfigurasi dari environment variable. Alamat database, kunci",
                    "    rahasia, dan mode debug dibaca dari variabel lingkungan, bukan",
                    "    ditulis di kode. Kode yang sama bisa jalan di laptop dan server",
                    "    hanya dengan variabel berbeda.",
                    "  - Log ke stdout. Aplikasi menulis log ke keluaran standar, dan",
                    "    lingkungannya (systemd, Docker) yang menyimpan dan memutarnya.",
                    "  - Proses tanpa keadaan. Jangan menyimpan sesi atau unggahan di memori",
                    "    atau disk lokal satu server; simpan di database, Redis, atau",
                    "    penyimpanan objek, supaya instance bisa ditambah atau dimatikan",
                    "    kapan saja.",
                    "  - Cepat menyala, rapi saat dimatikan. Saat menerima sinyal berhenti,",
                    "    selesaikan permintaan yang sedang jalan lalu keluar.",
                    "  - Lingkungan pengembangan semirip mungkin dengan produksi, misalnya",
                    "    sama-sama PostgreSQL, bukan SQLite di laptop.",
                ],
            },
            {
                "heading": "Membaca konfigurasi dari environment",
                "code": """def baca_konfigurasi(env):
    galat = []
    port = env.get("PORT", "8000")
    if not port.isdigit():
        galat.append("PORT harus angka")
    if "DATABASE_URL" not in env:
        galat.append("DATABASE_URL wajib diisi")
    debug = env.get("DEBUG", "false").lower() in ("1", "true", "yes")
    if galat:
        return None, galat
    return {"port": int(port), "db": env["DATABASE_URL"],
            "debug": debug}, []


laptop = {"DATABASE_URL": "postgresql://localhost/toko_dev", "DEBUG": "true"}
server = {"DATABASE_URL": "postgresql://db.internal/toko", "PORT": "8001"}
rusak = {"PORT": "delapan ribu"}

for nama, env in [("laptop", laptop), ("server", server), ("rusak", rusak)]:
    konfig, galat = baca_konfigurasi(env)
    if konfig:
        print(nama, "-> port", konfig["port"], "debug", konfig["debug"])
    else:
        print(nama, "-> GAGAL:", "; ".join(galat))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  laptop -> port 8000 debug True",
                    "  server -> port 8001 debug False",
                    "  rusak -> GAGAL: PORT harus angka; DATABASE_URL wajib diisi",
                    "",
                    "Di aplikasi sungguhan, fungsi ini dipanggil dengan os.environ. Di sini",
                    "env dioper sebagai dict supaya hasilnya sama di mesin mana pun.",
                    "Perhatikan juga bahwa aplikasi menolak menyala kalau konfigurasinya",
                    "salah, jadi kesalahannya ketahuan saat deploy, bukan saat pengguna",
                    "pertama datang.",
                ],
            },
            {
                "heading": "Unit systemd untuk Gunicorn",
                "bahasa": "ini",
                "code": """[Unit]
Description=API toko (Gunicorn)
After=network.target

[Service]
User=toko
WorkingDirectory=/srv/toko
Environment=DATABASE_URL=postgresql://db.internal/toko
ExecStart=/srv/toko/venv/bin/gunicorn --workers 5 --bind 127.0.0.1:8000 toko.wsgi:application
Restart=on-failure

[Install]
WantedBy=multi-user.target""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Django di VPS biasanya berbentuk Nginx di port 443, Gunicorn di",
                    "127.0.0.1:8000, dan unit systemd yang menyalakan Gunicorn saat server",
                    "boot. Aplikasi Laravel berbentuk Nginx dengan PHP-FPM, dan aplikasi",
                    "Rails berbentuk Nginx atau Thruster dengan Puma.",
                    "",
                    "Kasus kecil: API Flask-mu di VPS dua inti sering melambat saat ramai.",
                    "Ternyata ia dijalankan dengan flask run, server pengembangan yang memang",
                    "nggak ditujukan untuk produksi, dan alamat database ditulis langsung di",
                    "kode.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pindahkan alamat database dan SECRET_KEY ke environment variable,",
                    "     lalu baca dengan os.environ di awal aplikasi.",
                    "  2. Pasang Gunicorn di virtualenv dan jalankan dengan lima worker,",
                    "     mendengar di 127.0.0.1:8000.",
                    "  3. Buat unit systemd dengan Restart=on-failure supaya aplikasi menyala",
                    "     lagi kalau mati.",
                    "  4. Pasang Nginx di depannya sebagai reverse proxy dan arahkan /static/",
                    "     ke folder statis.",
                    "  5. Pastikan log ditulis ke stdout, lalu baca dengan journalctl -u",
                    "     toko.",
                ],
            },
        ],
    },
    {
        "title": "54. Peta Web Server dan Server Aplikasi",
        "sections": [
            {
                "body": [
                    "Nginx dan server aplikasi bawaan tiap bahasa sudah menutup kebanyakan",
                    "kebutuhan. Tapi kamu akan bertemu banyak nama lain: di XAMPP saat",
                    "belajar PHP, di konfigurasi Kubernetes kantor, atau di tutorial yang",
                    "menjanjikan HTTPS otomatis. Materi ini memetakannya dalam dua kelompok:",
                    "web server dan proxy di depan, serta server aplikasi alternatif. Versi",
                    "yang disebut adalah rilis terbaru per Oktober 2026.",
                ],
            },
            {
                "heading": "Tabel ringkas",
                "bahasa": "teks",
                "code": """Nama               Kelompok            Bahasa  Lisensi             Status
-----------------  ------------------  ------  ------------------  ------------------------
Apache httpd       web server          C       Apache-2.0          matang, umum di XAMPP
Caddy              web server          Go      Apache-2.0          aktif, HTTPS otomatis
Traefik            proxy kontainer     Go      MIT                 aktif, v3
HAProxy            load balancer       C       GPL-2.0             aktif, 3.4 LTS
Envoy              proxy L7            C++     Apache-2.0          aktif, CNCF graduated
Microsoft IIS      web server Windows  C++     proprietary         matang, IIS 10.0
OpenLiteSpeed      web server          C       GPL-3.0             aktif
Angie              web server          C       BSD-2-Clause        aktif, fork Nginx
Eclipse Jetty      server Java         Java    EPL-2.0/Apache-2.0  aktif
Undertow           server Java         Java    Apache-2.0          matang
Granian            server Python       Rust    BSD-3-Clause        aktif
uWSGI              server Python       C       GPL-2.0             pemeliharaan saja
FrankenPHP         server PHP          Go + C  MIT                 aktif, PHP Foundation
RoadRunner         server PHP          Go      MIT                 aktif, penomoran baru
Swoole             runtime PHP         C++     Apache-2.0          aktif""",
            },
            {
                "heading": "Web server dan proxy di depan",
                "body": [
                    "Apache HTTP Server, biasa disebut httpd (2.4.69), adalah web server lama",
                    "yang masih ada di mana-mana. Banyak pelajar pertama kali bertemu backend",
                    "lewat XAMPP, paket berisi Apache, MariaDB, dan PHP. Apache bisa",
                    "menjalankan PHP langsung lewat modul dan dikonfigurasi per folder dengan",
                    "berkas .htaccess. Pangsanya menurun dibanding Nginx, tapi kamu pasti",
                    "akan menemuinya di hosting bersama.",
                    "",
                    "Caddy (2.11.7) ditulis dengan Go dan terkenal karena HTTPS otomatis:",
                    "tulis nama domain di Caddyfile, dan Caddy mengurus sertifikatnya",
                    "sendiri. Ia ramah untuk deploy pertama.",
                    "",
                    "Traefik (3.7.15, MIT) dirancang untuk dunia kontainer. Ia membaca label",
                    "di kontainer Docker atau sumber daya Kubernetes lalu membuat rute",
                    "sendiri; jalur 2.11 masih menerima tambalan keamanan. HAProxy adalah",
                    "load balancer TCP dan HTTP yang terkenal stabil; cabang 3.4 adalah LTS",
                    "yang didukung sampai kuartal kedua 2031. Envoy (1.40.0) adalah proxy L7",
                    "dari dunia service mesh, proyek CNCF graduated; rilis 1.40 menyatakan",
                    "HTTP/3 dan QUIC stabil. Envoy lebih dekat ke kurikulum DevOps.",
                    "",
                    "Internet Information Services dari Microsoft adalah web server bawaan",
                    "Windows Server, versinya 10.0 sejak 2016 sampai Windows Server 2025.",
                    "Kamu akan menemuinya di kantor yang menjalankan aplikasi ASP.NET lama.",
                    "OpenLiteSpeed (1.9.3, GPL-3.0) adalah edisi gratis LiteSpeed Web Server",
                    "yang populer di hosting WordPress. Angie (1.12.4, BSD-2-Clause) adalah",
                    "fork Nginx yang ikut menyerap tambalan keamanan Nginx, misalnya",
                    "perbaikan dari nginx 1.31.7.",
                ],
            },
            {
                "heading": "Caddyfile yang setara",
                "bahasa": "teks",
                "code": """api.toko.example {
    handle_path /static/* {
        root * /srv/toko/static
        file_server
    }
    reverse_proxy /api/* 127.0.0.1:8000 127.0.0.1:8001
}""",
            },
            {
                "heading": "Server aplikasi alternatif",
                "body": [
                    "Di Java, Eclipse Jetty (12.1.14) dan Undertow (2.4.4.Final) adalah",
                    "alternatif Tomcat. Spring Boot bisa memakai Jetty sebagai server",
                    "tertanam, dan Undertow dipakai di WildFly serta pernah jadi pilihan di",
                    "Quarkus generasi awal.",
                    "",
                    "Di Python, Granian (2.8.4) adalah server untuk aplikasi sinkron maupun",
                    "ASGI yang ditulis dengan Rust. uWSGI (2.0.31) dulu umum sekali, tapi",
                    "dokumentasinya sendiri menyatakan proyek itu dalam mode pemeliharaan,",
                    "cuma perbaikan bug. Masih ada di sistem lama; untuk proyek baru pakai",
                    "Gunicorn, Uvicorn, atau Granian.",
                    "",
                    "Di PHP, model PHP-FPM memuat ulang seluruh aplikasi di setiap",
                    "permintaan. Runtime worker memuat aplikasi sekali lalu melayani banyak",
                    "permintaan, jadi jauh lebih cepat. FrankenPHP (1.13.1, MIT) ditulis",
                    "dengan Go di atas Caddy, kini ada di bawah organisasi GitHub php dan",
                    "didukung PHP Foundation. RoadRunner (Go, MIT) merilis 3.0.0 dan",
                    "meninggalkan penomoran berbasis tahun seperti v2025.x. Swoole (6.2.3,",
                    "Apache-2.0) adalah ekstensi C++ yang memberi PHP coroutine dan server",
                    "sendiri; dokumentasi utamanya berbahasa Tionghoa, dan ada fork bernama",
                    "OpenSwoole.",
                    "",
                    "Jebakan: di runtime worker, variabel global dan objek statis hidup terus",
                    "antar-permintaan. Data pengguna A bisa bocor ke permintaan pengguna B",
                    "kalau kodenya masih berasumsi semuanya dimulai bersih di tiap",
                    "permintaan.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "  - Deploy pertama di VPS dan ingin HTTPS tanpa repot: Caddy.",
                    "  - Butuh dokumentasi dan contoh paling banyak: Nginx.",
                    "  - Hosting bersama atau XAMPP di laptop: Apache httpd.",
                    "  - Banyak kontainer yang datang dan pergi: Traefik.",
                    "  - Load balancer di depan banyak server: HAProxy atau Nginx.",
                    "  - Service mesh dan gateway di Kubernetes: Envoy.",
                    "  - Aplikasi Laravel atau Symfony yang butuh lebih cepat: coba",
                    "    FrankenPHP atau RoadRunner, sesudah memeriksa kode dari keadaan",
                    "    global.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hosting bersama murah umumnya masih memakai Apache atau LiteSpeed.",
                    "Platform berbasis Kubernetes sering memakai Traefik atau Envoy sebagai",
                    "pintu masuk. Banyak tim kecil memilih Caddy di VPS karena sertifikat",
                    "HTTPS-nya diperbarui sendiri.",
                    "",
                    "Kasus kecil: kamu memindahkan proyek Laravel dari XAMPP di laptop ke",
                    "VPS, dan ingin HTTPS otomatis tanpa belajar Certbot dulu.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang PHP-FPM dan Caddy di VPS.",
                    "  2. Tulis Caddyfile dengan nama domainmu, root ke folder public",
                    "     Laravel, dan php_fastcgi yang menunjuk soket PHP-FPM.",
                    "  3. Arahkan DNS domain ke IP VPS, lalu jalankan Caddy; ia akan meminta",
                    "     sertifikat sendiri.",
                    "  4. Pindahkan pengaturan yang dulu di .htaccess ke Caddyfile, karena",
                    "     .htaccess cuma dibaca Apache.",
                    "  5. Kalau nanti butuh lebih cepat, uji FrankenPHP di lingkungan staging",
                    "     sebelum produksi.",
                ],
            },
        ],
    },
    {
        "title": "55. Arsitektur Backend: Monolit, Event, dan Ketahanan",
        "sections": [
            {
                "body": [
                    "Sejauh ini kita membangun satu aplikasi backend. Begitu tim dan fiturnya",
                    "tumbuh, muncul pertanyaan arsitektur: tetap satu aplikasi atau dipecah?",
                    "Bagaimana layanan saling memberi tahu? Apa yang terjadi kalau layanan",
                    "pembayaran lambat? Materi ini membahasnya dari sisi orang yang membuat",
                    "API. Pola arsitektur dan system design yang lebih luas dibahas di",
                    "kurikulum Tech Stack dan Arsitektur.",
                ],
            },
            {
                "heading": "Monolit modular dan microservices",
                "body": [
                    "Monolit adalah satu aplikasi yang di-deploy sebagai satu kesatuan.",
                    "Microservices memecah sistem jadi banyak layanan kecil yang",
                    "masing-masing punya database dan jadwal deploy sendiri, dan",
                    "berkomunikasi lewat jaringan.",
                    "",
                    "Microservices memberi kebebasan: tim stok bisa deploy tanpa menunggu tim",
                    "pembayaran. Harganya mahal: panggilan fungsi berubah jadi panggilan",
                    "jaringan yang bisa gagal, transaksi database tunggal hilang, dan butuh",
                    "pemantauan, tracing, serta otomasi deploy yang matang.",
                    "",
                    "Arah yang banyak dipilih sejak 2025 adalah monolit modular: satu",
                    "aplikasi, tapi kodenya dibagi jadi modul berbatas tegas (pesanan, stok,",
                    "pembayaran) yang cuma saling memanggil lewat antarmuka publik",
                    "masing-masing. Laporan JetBrains State of .NET 2025 mencatat tren mundur",
                    "dari \"microservices sejak awal\" ke pola ini. Kalau suatu modul nanti",
                    "memang perlu berdiri sendiri, batasnya sudah jelas dan pemisahannya jauh",
                    "lebih mudah.",
                ],
            },
            {
                "heading": "Event-driven, CQRS, dan event sourcing",
                "body": [
                    "Di arsitektur event-driven, layanan nggak memanggil satu sama lain",
                    "secara langsung. Layanan pesanan cukup menerbitkan event PesananDibuat",
                    "ke broker seperti Kafka atau RabbitMQ, dan layanan stok, email, serta",
                    "poin yang tertarik masing-masing mendengarkan. Pengirim nggak perlu tahu",
                    "siapa pendengarnya.",
                    "",
                    "CQRS (command query responsibility segregation) memisahkan jalur menulis",
                    "dan jalur membaca. Perintah (command) seperti TarikSaldo diperiksa",
                    "aturan bisnisnya lalu disimpan; kueri dilayani dari model baca terpisah",
                    "yang bentuknya disiapkan untuk layar, misalnya tabel ringkasan saldo.",
                    "",
                    "Event sourcing menyimpan riwayat event, bukan keadaan terakhir. Saldo",
                    "rekening nggak disimpan sebagai satu angka, tapi dihitung ulang dari",
                    "deretan event dibuka, disetor, ditarik. Keuntungannya, kamu punya jejak",
                    "audit lengkap dan bisa membangun model baca baru kapan saja.",
                    "Kerugiannya, desainnya lebih rumit dan skema event lama harus tetap bisa",
                    "dibaca selamanya. Pakai kalau riwayat memang inti bisnisnya, seperti",
                    "keuangan.",
                ],
            },
            {
                "heading": "Rekening dari deretan event",
                "code": """event = [
    {"jenis": "dibuka", "rek": "A-01", "nama": "Budi"},
    {"jenis": "disetor", "rek": "A-01", "jumlah": 500000},
    {"jenis": "ditarik", "rek": "A-01", "jumlah": 120000},
    {"jenis": "dibuka", "rek": "A-02", "nama": "Sari"},
    {"jenis": "disetor", "rek": "A-02", "jumlah": 75000},
]


def saldo(rek):
    total = 0
    for e in event:
        if e["rek"] != rek:
            continue
        if e["jenis"] == "disetor":
            total += e["jumlah"]
        elif e["jenis"] == "ditarik":
            total -= e["jumlah"]
    return total


def tarik(rek, jumlah):
    if jumlah > saldo(rek):
        return f"tolak: saldo {rek} cuma {saldo(rek)}"
    event.append({"jenis": "ditarik", "rek": rek, "jumlah": jumlah})
    return f"ok: event ditarik {jumlah} dicatat"


print(tarik("A-02", 100000))
print(tarik("A-01", 300000))
model_baca = {e["rek"]: saldo(e["rek"]) for e in event}
print("model baca:", model_baca)
print("jumlah event:", len(event))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  tolak: saldo A-02 cuma 75000",
                    "  ok: event ditarik 300000 dicatat",
                    "  model baca: {'A-01': 80000, 'A-02': 75000}",
                    "  jumlah event: 6",
                    "",
                    "Fungsi tarik adalah sisi command: ia memeriksa aturan lalu menambah",
                    "event. model_baca adalah sisi query yang dibangun ulang dari event. Di",
                    "sistem sungguhan, model baca diperbarui setiap ada event baru dan",
                    "disimpan di tabel sendiri.",
                ],
            },
            {
                "heading": "Webhooks dan AsyncAPI",
                "body": [
                    "Webhook adalah event yang dikirim ke luar sistem: layanan lain memanggil",
                    "URL milikmu saat sesuatu terjadi, misalnya gerbang pembayaran memanggil",
                    "POST /webhook/pembayaran saat pelanggan selesai membayar. Menurut",
                    "Postman State of the API 2025, 50% responden memakai webhook.",
                    "",
                    "Karena URL webhook bisa dipanggil siapa saja, penerima wajib memeriksa",
                    "tanda tangan. Pengirim menghitung HMAC dari isi pesan dengan rahasia",
                    "bersama dan mengirimnya di header. Penerima menghitung ulang dan",
                    "membandingkannya dengan hmac.compare_digest, yang waktunya nggak bocor",
                    "lewat lama pembandingan. Sertakan cap waktu di bagian yang",
                    "ditandatangani dan tolak pesan yang terlalu tua supaya pesan lama nggak",
                    "bisa diputar ulang. Pengirim juga selalu mengulang kalau gagal, jadi",
                    "simpan ID webhook dan abaikan duplikat. Inisiatif Standard Webhooks",
                    "(spesifikasi berlisensi Apache-2.0) membakukan bentuk header-nya.",
                ],
            },
            {
                "heading": "Memverifikasi tanda tangan webhook",
                "code": """import base64
import hashlib
import hmac

RAHASIA = b"rahasia-bersama-dari-dasbor"
TOLERANSI = 300


def tanda_tangan(id_pesan, waktu, body):
    isi = f"{id_pesan}.{waktu}.{body}".encode()
    digest = hmac.new(RAHASIA, isi, hashlib.sha256).digest()
    return "v1," + base64.b64encode(digest).decode()


def verifikasi(header, body, sekarang, sudah_diproses):
    if abs(sekarang - int(header["webhook-timestamp"])) > TOLERANSI:
        return "400 cap waktu terlalu jauh"
    harap = tanda_tangan(header["webhook-id"], header["webhook-timestamp"], body)
    if not hmac.compare_digest(harap, header["webhook-signature"]):
        return "401 tanda tangan salah"
    if header["webhook-id"] in sudah_diproses:
        return "200 duplikat, diabaikan"
    sudah_diproses.add(header["webhook-id"])
    return "200 diproses"


body = '{"pesanan": 501, "status": "lunas"}'
header = {"webhook-id": "msg_1", "webhook-timestamp": "1760000000",
          "webhook-signature": tanda_tangan("msg_1", "1760000000", body)}
diproses = set()
print(verifikasi(header, body, 1760000010, diproses))
print(verifikasi(header, body, 1760000020, diproses))
print(verifikasi(header, body.replace("lunas", "batal"), 1760000030, diproses))
print(verifikasi(header, body, 1760009999, diproses))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  200 diproses",
                    "  200 duplikat, diabaikan",
                    "  401 tanda tangan salah",
                    "  400 cap waktu terlalu jauh",
                    "",
                    "Untuk API berbasis event, ada AsyncAPI, saudara OpenAPI untuk pesan: ia",
                    "mendeskripsikan channel, operasi kirim dan terima, serta bentuk pesannya",
                    "dalam YAML. Versi terbarunya 3.1.0 (Januari 2026), proyek Linux",
                    "Foundation berlisensi Apache-2.0.",
                ],
            },
            {
                "heading": "Potongan dokumen AsyncAPI",
                "bahasa": "yaml",
                "code": """asyncapi: 3.1.0
info:
  title: Event Toko
  version: 1.0.0
channels:
  pesananDibuat:
    address: pesanan.dibuat
    messages:
      PesananDibuat:
        payload:
          type: object
          properties:
            id: { type: integer }
            total: { type: integer }
operations:
  terbitkanPesanan:
    action: send
    channel:
      $ref: '#/channels/pesananDibuat'""",
            },
            {
                "heading": "Gateway, alur kerja tahan lama, dan serverless",
                "body": [
                    "API gateway adalah pintu tunggal di depan banyak layanan: ia mengurus",
                    "autentikasi, rate limit, dan routing ke layanan yang benar. Kong Gateway",
                    "adalah salah satu yang paling dikenal, berjalan di atas OpenResty (Nginx",
                    "ditambah Lua). Perhatikan status lisensinya: repositori open source Kong",
                    "di GitHub berhenti di jalur 3.9 (rilis terakhirnya 3.9.4), sedangkan",
                    "Kong Gateway Enterprise sudah sampai 3.16 pada Oktober 2026. Jawaban tim",
                    "dukungan Kong yang dikutip di forum diskusi resmi proyeknya menyebut",
                    "build 3.9 sebagai build gratis penuh terakhir. Sebelum memilihnya untuk",
                    "proyek baru, cek ketentuan terbaru di situs Kong, atau lihat Envoy dan",
                    "Traefik di materi peta web server, serta reverse proxy .NET di materi",
                    "peta ekosistem .NET.",
                    "",
                    "Temporal (server 1.32.1, MIT) menawarkan durable execution: kamu menulis",
                    "alur kerja panjang, misalnya \"tagih kartu, tunggu tiga hari, kirim",
                    "pengingat, batalkan kalau belum bayar\", sebagai kode biasa. Temporal",
                    "mencatat setiap langkah, jadi kalau server mati di tengah jalan, alurnya",
                    "dilanjutkan dari langkah terakhir. Kategori ini sedang naik, bersama",
                    "Inngest dan Restate.",
                    "",
                    "Serverless atau functions-as-a-service menjalankan fungsimu hanya saat",
                    "ada permintaan, tanpa server yang kamu urus sendiri, dan biayanya",
                    "dihitung per eksekusi. Contohnya AWS Lambda, Cloudflare Workers, dan",
                    "Vercel Functions; di Survei Stack Overflow 2026, Cloudflare dipakai 25%",
                    "dan Vercel 11% responden kategori Cloud development. Cocok untuk beban",
                    "yang naik-turun tajam. Jebakannya cold start (panggilan pertama lambat",
                    "karena fungsi harus disiapkan dulu), batas waktu eksekusi, dan koneksi",
                    "database yang membludak kalau tiap fungsi membuka koneksi sendiri.",
                ],
            },
            {
                "heading": "Pola ketahanan",
                "body": [
                    "Layanan yang kamu panggil pasti suatu saat lambat atau mati. Tanpa",
                    "persiapan, kelambatan itu menular: semua worker-mu habis menunggu, dan",
                    "aplikasimu ikut tumbang. Lima pola untuk mencegahnya:",
                    "",
                    "  - Timeout: setiap panggilan ke luar punya batas waktu. Tanpa timeout,",
                    "    satu layanan macet bisa menahan worker selamanya.",
                    "  - Retry dengan backoff dan jitter: ulangi panggilan yang gagal dengan",
                    "    jeda yang makin panjang ditambah sedikit acak, dan hanya untuk",
                    "    operasi yang idempoten.",
                    "  - Circuit breaker: kalau kegagalan beruntun melewati ambang, breaker",
                    "    terbuka (open) dan panggilan berikutnya langsung ditolak tanpa",
                    "    menyentuh layanan itu. Sesudah waktu tunggu, breaker setengah",
                    "    terbuka (half-open) dan meloloskan satu panggilan uji. Berhasil",
                    "    berarti tertutup lagi (closed), gagal berarti terbuka lagi.",
                    "  - Bulkhead: batasi jumlah koneksi atau thread per layanan tujuan,",
                    "    seperti sekat di kapal, supaya satu layanan yang macet nggak",
                    "    menghabiskan semua sumber daya.",
                    "  - Graceful degradation: kalau layanan rekomendasi mati, tampilkan",
                    "    produk terlaris dari cache, jangan halaman error.",
                    "",
                    "Kamu nggak perlu menulisnya sendiri di produksi: Polly di .NET dan",
                    "Resilience4j di Java menyediakan semuanya. Latihan bab ini memintamu",
                    "menulis circuit breaker dengan jam palsu supaya perpindahan statusnya",
                    "kelihatan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Gerbang pembayaran mengabari toko online lewat webhook bertanda tangan.",
                    "Aplikasi besar memasang circuit breaker di setiap panggilan ke layanan",
                    "lain, sehingga gangguan di satu layanan cuma mematikan satu fitur, bukan",
                    "seluruh aplikasi.",
                    "",
                    "Kasus kecil: halaman checkout tokomu ikut macet setiap kali API ongkir",
                    "pihak ketiga lambat, dan sesekali pesanan tercatat dua kali karena",
                    "webhook pembayaran datang berulang.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang timeout dua detik di panggilan ke API ongkir.",
                    "  2. Bungkus panggilan itu dengan circuit breaker: terbuka sesudah lima",
                    "     kegagalan beruntun, coba lagi sesudah 30 detik.",
                    "  3. Saat breaker terbuka, tampilkan ongkir tarif tetap dari tabel",
                    "     cadangan dan tandai \"perkiraan\".",
                    "  4. Di endpoint webhook, verifikasi HMAC dan cap waktu, lalu simpan",
                    "     webhook-id di tabel ber-indeks unik.",
                    "  5. Proses webhook di antrean tugas dan langsung balas 200, supaya",
                    "     pengirim nggak mengulang karena menunggu terlalu lama.",
                ],
            },
        ],
    },
    {
        "title": "56. Peta CMS Headless dan Backend-as-a-Service",
        "sections": [
            {
                "body": [
                    "Nggak semua proyek butuh backend yang ditulis dari nol. Blog perusahaan,",
                    "daftar produk sederhana, atau aplikasi mobile prototipe sering cukup",
                    "dengan CMS atau backend-as-a-service (BaaS). CMS (content management",
                    "system) memberi panel admin untuk mengelola konten. CMS headless",
                    "menyediakan panel admin dan API, tapi tanpa tampilan; frontend-nya kamu",
                    "buat sendiri, misalnya dengan Next.js atau Nuxt yang dibahas di",
                    "kurikulum Frontend Modern. BaaS menyediakan database, autentikasi,",
                    "penyimpanan berkas, dan fungsi siap pakai lewat SDK.",
                    "",
                    "Pertanyaan yang perlu kamu jawab sebelum memilih: seberapa jauh logika",
                    "bisnismu menyimpang dari CRUD biasa, siapa yang memegang datanya, dan",
                    "apa lisensinya.",
                ],
            },
            {
                "heading": "Tabel ringkas",
                "bahasa": "teks",
                "code": """Nama        Jenis              Teknologi          Lisensi              Versi (Okt 2026)
----------  -----------------  -----------------  -------------------  ----------------
WordPress   CMS (+ REST API)   PHP                GPL-2.0-or-later     7.1.3
Drupal      CMS (+ JSON:API)   PHP                GPL-2.0-or-later     11.4.10
Strapi      CMS headless       Node.js            MIT (Community)      5.58.0
Directus    CMS headless       Node.js            BSL-1.1              12.5.0
Payload     CMS headless       Next.js            MIT                  3.91.0
Supabase    BaaS               PostgreSQL         Apache-2.0 (umumnya) layanan + self-host
Firebase    BaaS               layanan Google     proprietary          layanan
PocketBase  BaaS satu berkas   Go + SQLite        MIT                  0.40.5
Appwrite    BaaS               PHP/TS, Docker     BSD-3-Clause         2.5.0
Hasura      API GraphQL instan Haskell/Rust       Apache-2.0 (v2 CE)   v2.51.0""",
            },
            {
                "heading": "CMS: WordPress, Drupal, dan yang headless",
                "body": [
                    "WordPress adalah CMS paling banyak dipakai untuk situs konten. Di Survei",
                    "Stack Overflow 2026 ia dipakai 13,3% responden, dan di JetBrains State",
                    "of PHP 2025, 25% pengembang PHP bekerja dengannya. Selain tema,",
                    "WordPress punya REST API bawaan di /wp-json/wp/v2/, jadi bisa dipakai",
                    "sebagai CMS headless. Hanya rilis terbaru jalur 7.1 yang dirawat, jadi",
                    "selalu perbarui. Menulis plugin WordPress adalah pekerjaan backend PHP",
                    "sungguhan, dan pasarnya besar.",
                    "",
                    "Drupal (jalur 11.4, versi 12.0 masih beta) lebih kuat untuk struktur",
                    "konten rumit dan hak akses berlapis, sering dipakai situs instansi dan",
                    "universitas. Pemakainya 2,0% di survei yang sama dan pangsanya menurun",
                    "pelan.",
                    "",
                    "Strapi adalah CMS headless Node.js yang paling dikenal; edisi",
                    "Community-nya MIT dengan fitur Enterprise berbayar. Directus membungkus",
                    "database SQL yang sudah ada dengan panel admin dan API; perhatikan",
                    "lisensinya BSL-1.1, gratis untuk organisasi di bawah ambang pendapatan",
                    "tertentu tapi bukan open source versi OSI. Payload (MIT) ditanam",
                    "langsung di dalam aplikasi Next.js, jadi CMS dan frontend hidup di satu",
                    "proyek.",
                ],
            },
            {
                "heading": "Membaca WordPress sebagai API",
                "bahasa": "terminal",
                "code": "curl \"https://blog.example/wp-json/wp/v2/posts?per_page=3&_fields=id,title,date\"",
            },
            {
                "heading": "Backend-as-a-Service",
                "body": [
                    "Supabase dibangun di atas PostgreSQL: kamu mendapat database Postgres",
                    "asli, API REST dan GraphQL otomatis, autentikasi, penyimpanan berkas,",
                    "dan langganan real-time. Hak akses diatur lewat Row Level Security di",
                    "Postgres. Sebagian besar komponennya Apache-2.0 dan bisa dijalankan",
                    "sendiri. Survei Stack Overflow 2026 mencatat Supabase di 8% (kategori",
                    "Databases) dan 7% (Cloud development).",
                    "",
                    "Firebase dari Google menyediakan Cloud Firestore, Realtime Database,",
                    "Authentication, dan Cloud Functions. Survei yang sama mencatat Firebase",
                    "11% di kategori Cloud development. Layanannya proprietary, sedangkan",
                    "SDK-nya Apache-2.0. Risiko terbesarnya vendor lock-in: model data",
                    "Firestore dan aturan keamanannya khas Firebase, jadi pindah ke tempat",
                    "lain berarti menulis ulang banyak bagian.",
                    "",
                    "PocketBase (MIT) adalah backend lengkap dalam satu berkas program Go",
                    "dengan SQLite di dalamnya: database, autentikasi, panel admin, dan API",
                    "real-time. Ia contoh bagus bahwa backend bisa sesederhana itu, tapi",
                    "versinya masih 0.x, jadi API-nya bisa berubah antar-rilis. Appwrite",
                    "(BSD-3-Clause) adalah BaaS open source yang dijalankan lewat Docker,",
                    "dengan cakupan mirip Firebase.",
                    "",
                    "Hasura membangkitkan API GraphQL langsung dari skema database. Community",
                    "Edition v2 (Apache-2.0) masih dirawat, sementara pengembangan utamanya",
                    "pindah ke Hasura DDN (v3).",
                ],
            },
            {
                "heading": "Kapan nggak perlu menulis backend sendiri",
                "body": [
                    "  - Situs konten dengan editor non-programmer: WordPress, atau CMS",
                    "    headless kalau frontend-nya dibuat terpisah.",
                    "  - Prototipe aplikasi mobile yang butuh login dan data dalam seminggu:",
                    "    Supabase, Firebase, atau PocketBase.",
                    "  - Aplikasi dengan aturan bisnis rumit, integrasi pembayaran, dan alur",
                    "    persetujuan: tulis backend sendiri, mungkin dengan BaaS untuk",
                    "    sebagian fiturnya saja.",
                    "",
                    "Jebakan: menaruh semua logika bisnis di aturan keamanan BaaS dan kode",
                    "frontend. Saat aturannya makin rumit, kamu akan butuh backend juga, dan",
                    "memindahkannya belakangan lebih mahal. Periksa juga lisensi (BSL, GPL)",
                    "dan ke mana data penggunamu disimpan sebelum mulai.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak situs perusahaan dan media kecil berjalan di WordPress. Startup",
                    "memakai Supabase atau Firebase untuk meluncurkan versi pertama",
                    "aplikasinya, lalu menambah backend sendiri untuk bagian yang butuh",
                    "logika khusus. Situs dokumentasi dan toko kecil sering memakai CMS",
                    "headless dengan frontend Next.js.",
                    "",
                    "Kasus kecil: UMKM kue ingin situs daftar produk yang isinya bisa diubah",
                    "pemiliknya sendiri, plus aplikasi pesanan sederhana. Anggaran kecil dan",
                    "programmer-nya cuma kamu.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Untuk daftar produk, pakai WordPress atau Strapi supaya pemilik",
                    "     bisa mengubah foto dan harga lewat panel admin.",
                    "  2. Untuk pesanan, pakai Supabase: tabel pesanan di Postgres, login",
                    "     pelanggan lewat Supabase Auth.",
                    "  3. Atur Row Level Security supaya pelanggan cuma bisa membaca",
                    "     pesanannya sendiri.",
                    "  4. Simpan logika yang menyentuh uang, misalnya konfirmasi pembayaran,",
                    "     di fungsi server atau backend kecil, jangan di aplikasi klien.",
                    "  5. Catat ketergantungan pada tiap layanan beserta lisensinya, supaya",
                    "     kalau nanti harus pindah, kamu tahu bagian mana yang perlu ditulis",
                    "     ulang.",
                ],
            },
        ],
    },
]
