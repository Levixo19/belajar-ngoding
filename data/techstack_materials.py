"""Kurikulum Tech Stack & Arsitektur.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

TECHSTACK_BAB = [
    {
        "judul": "Peta Besar: Mulai dari Mana",
        "ket": "Apa itu stack, perjalanan satu request, dan jalur belajar per peran",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Stack Web Klasik dan Pola MVC",
        "ket": "LAMP/LEMP, paket server lokal, MVC, dan cara halaman web dirender",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Stack JavaScript Full-Stack",
        "ket": "MERN dan variannya, Jamstack, sampai meta-framework",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Stack Framework Backend dan Frontend",
        "ket": "Pasangan framework populer di PHP, Python, Java, C#, dan HTML over the wire",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "Stack Cloud dan Peta Lintas Ranah",
        "ket": "Serverless, edge, BaaS, MACH, dan stack milik ranah lain",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Praktik Rekayasa: Kode yang Bisa Dipercaya",
        "ket": "Tes, review, versi, alur Git, dan kode bersih",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Pola Arsitektur Aplikasi",
        "ket": "Cara menyusun satu aplikasi dari dalam",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "System Design: Skala, Lalu Lintas, dan Cache",
        "ket": "Menangani lebih banyak pengguna tanpa menulis ulang aplikasi",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "System Design: Data Tersebar dan Keandalan",
        "ket": "Data di banyak server, pembatasan, dan bertahan saat ada yang mati",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Arsitektur Terdistribusi",
        "ket": "Microservices, event, dan pola agar layanan saling tahan banting",
        "tingkat": "mahir",
        "jumlah": 5,
    },
    {
        "judul": "Operasi, Rilis, dan Keamanan Arsitektur",
        "ket": "Merilis, memantau, dan mengamankan sistem yang sudah jalan",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Dokumentasi, Tim, dan Memilih Stack",
        "ket": "Mencatat keputusan, cara tim bekerja, dan memilih stack dengan kepala dingin",
        "tingkat": "mahir",
        "jumlah": 4,
    },
]

TECHSTACK_MATERIALS = [
    {
        "title": "1. Apa Itu Tech Stack dan Kenapa Pilihannya Banyak Sekali",
        "sections": [
            {
                "body": [
                    "Tech stack, atau sering disingkat stack, adalah kumpulan teknologi yang",
                    "dipakai bareng untuk membangun satu aplikasi. Kata stack artinya",
                    "tumpukan. Namanya begitu karena teknologinya memang bertumpuk: yang di",
                    "atas memakai yang di bawahnya.",
                    "",
                    "Bayangkan warung makan. Ada etalase yang dilihat pembeli, ada dapur",
                    "tempat masakan diolah, ada gudang bahan, dan ada bangunan beserta",
                    "listrik dan airnya. Pembeli cuma melihat etalase. Tapi warungnya nggak",
                    "jalan kalau salah satu bagian lain mogok. Aplikasi juga begitu.",
                    "",
                    "Waktu orang bilang \"stack kami Laravel, MySQL, dan Vue\", dia sedang",
                    "menyebut isi tiap bagian itu. Materi ini membantumu membaca kalimat",
                    "seperti itu: teknologi mana mengurus bagian mana, dan kurikulum mana di",
                    "aplikasi ini yang membahasnya.",
                ],
            },
            {
                "heading": "Empat lapisan yang hampir selalu ada",
                "body": [
                    "Hampir semua aplikasi web bisa dibagi jadi empat lapisan. Urutannya dari",
                    "yang paling dekat ke pengguna:",
                    "",
                    "  - Frontend: bagian yang tampil di layar dan disentuh pengguna. Isinya",
                    "    HTML, CSS, dan JavaScript, sering dibantu framework seperti React",
                    "    atau Vue. Kodenya berjalan di browser pengguna.",
                    "  - Backend: program di server yang menerima permintaan, menjalankan",
                    "    aturan bisnis seperti menghitung ongkir atau mengecek stok, lalu",
                    "    mengirim jawaban. Bahasanya bisa Python, PHP, Java, Go, C#,",
                    "    JavaScript lewat Node.js, dan banyak lagi.",
                    "  - Database: tempat data disimpan supaya nggak hilang saat server mati.",
                    "    Contohnya PostgreSQL, MySQL, SQLite, dan MongoDB.",
                    "  - Infrastruktur: mesin dan sistem tempat semua itu berjalan. Isinya",
                    "    sistem operasi (biasanya Linux), web server, kontainer, dan layanan",
                    "    cloud.",
                    "",
                    "Di bawah infrastruktur masih ada perangkat keras. Programmer web jarang",
                    "memikirkannya. Di dunia embedded, misalnya Arduino dan Raspberry Pi,",
                    "lapisan ini yang paling banyak diurus.",
                    "",
                    "Aplikasi mobile dan desktop juga punya lapisan yang sama. Bedanya,",
                    "frontend-nya berupa aplikasi yang dipasang di HP atau laptop. Backend",
                    "dan database-nya tetap ada di server.",
                ],
            },
            {
                "heading": "Membaca akronim stack",
                "body": [
                    "Beberapa kombinasi teknologi begitu sering dipakai bareng sampai dikasih",
                    "nama. Namanya biasanya akronim, yaitu singkatan dari huruf depan tiap",
                    "komponennya:",
                    "",
                    "  LAMP   Linux, Apache, MySQL, PHP",
                    "  MERN   MongoDB, Express, React, Node.js",
                    "  PERN   PostgreSQL, Express, React, Node.js",
                    "  TALL   Tailwind CSS, Alpine.js, Laravel, Livewire",
                    "",
                    "Urutan huruf di akronim cuma supaya enak diucapkan, dan nggak mengikuti",
                    "urutan lapisan. Di MERN, huruf pertama justru database, sedangkan huruf",
                    "ketiga frontend.",
                    "",
                    "Nama-nama ini juga nggak pernah disahkan lembaga mana pun. Kalau",
                    "proyekmu memakai MySQL di tempat MongoDB, aplikasinya tetap jalan, cuma",
                    "namanya sudah lain. Stack bernama dibahas satu per satu mulai bab 2.",
                    "Program di bawah ini mengelompokkan komponen dua stack menurut",
                    "lapisannya.",
                ],
            },
            {
                "heading": "Mengelompokkan komponen per lapisan",
                "code": """LAPISAN = {
    "Linux": "infrastruktur",
    "Apache": "infrastruktur",
    "MySQL": "database",
    "PHP": "backend",
    "MongoDB": "database",
    "Express": "backend",
    "React": "frontend",
    "Node.js": "backend",
}

STACK = {
    "LAMP": ["Linux", "Apache", "MySQL", "PHP"],
    "MERN": ["MongoDB", "Express", "React", "Node.js"],
}

URUTAN = ["frontend", "backend", "database", "infrastruktur"]

for nama, komponen in STACK.items():
    print(nama)
    for lapis in URUTAN:
        isi = [k for k in komponen if LAPISAN[k] == lapis]
        if isi:
            print(f"  {lapis:<13} {', '.join(isi)}")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  LAMP",
                    "    backend       PHP",
                    "    database      MySQL",
                    "    infrastruktur Linux, Apache",
                    "  MERN",
                    "    frontend      React",
                    "    backend       Express, Node.js",
                    "    database      MongoDB",
                    "",
                    "LAMP nggak punya baris frontend. Tampilannya tetap ada, yaitu HTML, CSS,",
                    "dan JavaScript yang dicetak oleh PHP. Akronimnya cuma menyebut komponen",
                    "di sisi server.",
                    "",
                    "Apache masuk infrastruktur karena dia web server: program yang menerima",
                    "permintaan dari browser lalu menyerahkannya ke PHP. Node.js dan Express",
                    "sama-sama di backend. Node.js menjalankan JavaScript di luar browser,",
                    "Express menata rute di atasnya.",
                ],
            },
            {
                "heading": "Kenapa pilihannya banyak sekali",
                "body": [
                    "Survei Developer Stack Overflow 2026 menanyakan bahasa yang dipakai",
                    "responden. Daftar hasilnya memuat 50 bahasa. Untuk framework web ada 40",
                    "nama, untuk database 30, dan untuk IDE 35. Itu baru yang masuk daftar",
                    "survei.",
                    "",
                    "Penyebabnya macam-macam:",
                    "",
                    "  - Tiap teknologi lahir untuk masalah tertentu. PHP dibuat untuk",
                    "    halaman web dinamis, Python banyak dipakai di data dan AI, Go",
                    "    dirancang untuk layanan jaringan yang melayani banyak permintaan",
                    "    sekaligus.",
                    "  - Teknologi lama nggak langsung hilang. Kode yang sudah jalan",
                    "    bertahun-tahun tetap dirawat, jadi teknologinya tetap dipakai dan",
                    "    orang yang menguasainya tetap dicari.",
                    "  - Perusahaan dan komunitas terus bikin alat baru untuk menambal",
                    "    kekurangan alat sebelumnya, lalu alat lama dan baru hidup",
                    "    berdampingan.",
                    "",
                    "Angka survei membantu membaca mana yang umum. Di survei 2026, JavaScript",
                    "dipakai 62% responden, Python dan SQL masing-masing 58%. Untuk database,",
                    "PostgreSQL 58% dan SQLite 42%. Untuk framework web, Node.js 46% dan",
                    "React 42%. Untuk editor, Visual Studio Code 71%.",
                    "",
                    "Ingat: angka itu persentase responden yang memakai, dan respondennya",
                    "kebanyakan pengunjung Stack Overflow. Jadi angka itu cocok untuk melihat",
                    "apa yang lazim. Untuk menyimpulkan apa yang terbaik bagi proyekmu, angka",
                    "itu belum cukup.",
                ],
            },
            {
                "heading": "Peta kurikulum di aplikasi ini",
                "body": [
                    "Kurikulum di aplikasi ini juga mengikuti lapisan tadi. Tabel di bawah",
                    "bisa kamu pakai sebagai peta. Kalau ketemu nama teknologi asing, cari",
                    "dulu lapisannya, baru buka kurikulum yang cocok.",
                    "",
                    "Survei 2024 juga menanyakan sistem operasi. Windows, macOS, dan Ubuntu",
                    "ada di urutan atas, disusul Android dan WSL. Sistem operasi itu bagian",
                    "dari lapisan infrastruktur, dan di aplikasi ini dibahas lewat CLI",
                    "Fedora. Perangkat seperti Raspberry Pi dan Arduino yang muncul di survei",
                    "yang sama dibahas di Embedded & IoT.",
                ],
            },
            {
                "heading": "Lapisan dan kurikulumnya",
                "bahasa": "teks",
                "code": """Lapisan           Kurikulum di aplikasi ini
----------------  ---------------------------------------------------
Frontend          HTML, CSS, JavaScript, TypeScript, Frontend Modern
Backend           Python, Java, Go, PHP, C#, Ruby, Rust, Kotlin,
                  Backend & API, Bikin Aplikasi
Database          SQL, Database & Penyimpanan Data
Infrastruktur     CLI Fedora, Bash, Git & GitHub, DevOps & Cloud
Perangkat keras   C, C++, Embedded & IoT
Lintas lapisan    Keamanan Siber, Data & Analitik, AI & Machine Learning,
                  Mobile & Desktop, Game & Grafis,
                  Bahasa Pemrograman Lain, Tech Stack & Arsitektur""",
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: mencoba belajar semua lapisan sekaligus. Pemula yang melihat",
                    "peta seperti tadi sering langsung memasang React, Docker, dan Kubernetes",
                    "di minggu pertama. Hasilnya nggak ada yang dipahami sampai tuntas.",
                    "Kuasai satu lapisan dulu sampai kamu bisa bikin sesuatu yang jalan.",
                    "",
                    "Kesalahan lain yang sering muncul: menyamakan stack dengan bahasa.",
                    "Python itu bahasa. Django itu framework yang ditulis dengan Python.",
                    "PostgreSQL itu database yang bisa dipakai dari bahasa apa pun. Stack",
                    "adalah gabungan ketiganya ditambah tempat menjalankannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan kerja programmer hampir selalu menyebut stack, misalnya",
                    "\"menguasai Laravel, MySQL, dan Vue.js\" atau \"pengalaman dengan React,",
                    "Node.js, dan PostgreSQL\". Blog teknik banyak perusahaan juga sering",
                    "menulis stack yang mereka pakai, lengkap dengan alasannya.",
                    "",
                    "Kasus kecil: kamu membaca lowongan magang yang meminta \"Next.js,",
                    "Express, PostgreSQL, Docker, dan GitHub Actions\". Kamu ingin tahu harus",
                    "mulai dari kurikulum mana.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis tiap nama di baris sendiri, lalu tandai lapisannya. Next.js",
                    "     frontend (ditambah sedikit server), Express backend, PostgreSQL",
                    "     database, Docker dan GitHub Actions infrastruktur.",
                    "  2. Cocokkan dengan peta tadi. Next.js ada di Frontend Modern, Express",
                    "     di Backend & API, PostgreSQL di SQL lalu Database & Penyimpanan",
                    "     Data, Docker dan GitHub Actions di DevOps & Cloud.",
                    "  3. Cari prasyarat bersama. Next.js dan Express sama-sama JavaScript,",
                    "     jadi kurikulum JavaScript duluan, disusul SQL.",
                    "  4. Susun urutannya: JavaScript, SQL, Git & GitHub, Frontend Modern,",
                    "     Backend & API, lalu DevOps & Cloud. Docker belakangan, karena kamu",
                    "     perlu punya aplikasi dulu sebelum ada yang dibungkus.",
                ],
            },
        ],
    },
    {
        "title": "2. Perjalanan Satu Request dari Browser sampai Database",
        "sections": [
            {
                "body": [
                    "Coba ketik toko.example.com/produk/7 di browser lalu tekan Enter. Nggak",
                    "sampai sedetik, halaman produk muncul. Di balik itu ada beberapa program",
                    "di beberapa komputer yang saling oper pesan. Materi ini mengikuti pesan",
                    "itu dari awal sampai balik lagi ke layarmu.",
                    "",
                    "Pola dasarnya disebut client-server. Client adalah pihak yang meminta,",
                    "misalnya browser atau aplikasi di HP. Server adalah program yang",
                    "menunggu permintaan lalu menjawabnya. Satu permintaan disebut request,",
                    "jawabannya disebut response. Seluruh web bekerja dengan pola ini.",
                    "Aplikasi mobile yang memanggil API dan program yang tersambung ke",
                    "database juga begitu.",
                ],
            },
            {
                "heading": "Langkah 1: DNS mencari alamat",
                "body": [
                    "Komputer di internet saling menemukan lewat alamat IP, deretan angka",
                    "seperti 203.0.113.10. Manusia lebih gampang mengingat nama. DNS (Domain",
                    "Name System) adalah sistem yang menerjemahkan nama domain jadi alamat",
                    "IP. Gampangnya, DNS itu buku telepon internet.",
                    "",
                    "Browser nggak langsung bertanya ke ujung dunia. Dia cek dulu catatan",
                    "yang tersimpan di komputermu. Kalau belum ada, pertanyaannya diteruskan",
                    "ke resolver, biasanya milik penyedia internetmu atau layanan seperti",
                    "1.1.1.1. Resolver bertanya berjenjang: ke server root, lalu ke server",
                    ".com, lalu ke server yang memegang domain itu.",
                    "",
                    "Jawabannya disimpan sementara selama TTL (time to live), misalnya 300",
                    "detik. Selama TTL belum habis, permintaan berikutnya nggak perlu",
                    "bertanya lagi. Makanya perubahan alamat DNS nggak langsung terasa di",
                    "semua komputer.",
                ],
            },
            {
                "heading": "Mengecek DNS dari terminal",
                "bahasa": "terminal",
                "code": """# tanya alamat IP sebuah domain (di Fedora ada di paket bind-utils)
dig +short example.com""",
            },
            {
                "heading": "Langkah 2: sambungan, lalu pesan HTTP",
                "body": [
                    "Sesudah tahu alamatnya, browser membuka sambungan TCP ke server itu di",
                    "port 443. Port adalah nomor pintu di satu komputer. Port 443 dipakai",
                    "HTTPS, port 80 dipakai HTTP biasa. Di atas sambungan itu browser dan",
                    "server menyepakati enkripsi TLS, supaya isi pesannya nggak bisa dibaca",
                    "orang di tengah jalan. Detail enkripsinya ada di kurikulum Keamanan",
                    "Siber.",
                    "",
                    "Baru sesudah itu browser mengirim request HTTP. Kalau ditulis sebagai",
                    "teks, isinya begini:",
                ],
            },
            {
                "heading": "Request HTTP",
                "bahasa": "http",
                "code": """GET /produk/7 HTTP/1.1
Host: toko.example.com
Accept: text/html
User-Agent: Mozilla/5.0""",
            },
            {
                "body": [
                    "GET artinya minta data. /produk/7 itu path, alamat di dalam situs. Host",
                    "memberi tahu server domain mana yang dimaksud, karena satu server bisa",
                    "melayani banyak domain. Baris-baris lain disebut header, keterangan",
                    "tambahan seperti jenis isi yang bisa diterima browser.",
                    "",
                    "Browser modern biasanya memakai HTTP/2 atau HTTP/3. Keduanya dikirim",
                    "dalam bentuk biner, dan HTTP/3 berjalan di atas protokol QUIC yang",
                    "memakai UDP. Isinya tetap sama: metode, path, dan header.",
                ],
            },
            {
                "heading": "Langkah 3: reverse proxy di depan aplikasi",
                "body": [
                    "Request itu biasanya nggak langsung sampai ke program aplikasi. Yang",
                    "pertama menerimanya adalah reverse proxy, server perantara yang berdiri",
                    "di depan aplikasi. Contohnya Nginx, Caddy, HAProxy, atau layanan seperti",
                    "Cloudflare. Tugasnya:",
                    "",
                    "  - Membuka enkripsi TLS, jadi aplikasi di belakangnya cukup bicara HTTP",
                    "    biasa.",
                    "  - Mengirim berkas statis seperti gambar, CSS, dan JavaScript langsung",
                    "    dari disk, tanpa mengganggu aplikasi.",
                    "  - Meneruskan sisanya ke aplikasi. Kalau aplikasinya punya beberapa",
                    "    salinan, proxy juga membagi request ke salinan-salinan itu.",
                    "",
                    "Menurut W3Techs (Oktober 2026), server yang paling sering terlihat di",
                    "depan situs web adalah Cloudflare Server (32,5%), Nginx (30,3%), dan",
                    "Apache (21,4%).",
                ],
            },
            {
                "heading": "Langkah 4: aplikasi dan database",
                "body": [
                    "Aplikasi menerima request yang diteruskan proxy. Dia mencocokkan path",
                    "dengan daftar rute, lalu menjalankan fungsi yang cocok. Untuk /produk/7,",
                    "fungsinya bertanya ke database: produk bernomor 7 itu apa?",
                    "",
                    "Database menjawab dengan baris data. Aplikasi menyusunnya jadi HTML",
                    "(atau JSON kalau yang meminta program lain), lalu mengirim response.",
                    "Baris pertama response memuat kode status: 200 artinya berhasil, 404",
                    "artinya nggak ditemukan, 500 artinya ada error di server.",
                    "",
                    "Response balik lewat jalan yang sama: aplikasi, proxy, internet,",
                    "browser. Browser membaca HTML-nya, lalu biasanya mengirim request baru",
                    "untuk CSS, gambar, dan JavaScript yang disebut di halaman itu. Program",
                    "di bawah ini meniru keempat langkah tadi dalam satu berkas.",
                ],
            },
            {
                "heading": "Simulasi satu request",
                "code": """import sqlite3

# Langkah 1: "DNS" menerjemahkan nama jadi alamat IP
DNS = {"toko.example.com": "203.0.113.10"}

# Langkah 4: database berisi satu tabel produk
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, harga INTEGER)")
db.executemany("INSERT INTO produk VALUES (?, ?, ?)",
               [(7, "Pensil 2B", 3500), (8, "Penghapus", 2000)])


def aplikasi(path):
    bagian = path.strip("/").split("/")
    if len(bagian) == 2 and bagian[0] == "produk" and bagian[1].isdigit():
        baris = db.execute("SELECT nama, harga FROM produk WHERE id = ?",
                           (int(bagian[1]),)).fetchone()
        if baris:
            return 200, f"<h1>{baris[0]}</h1><p>Rp{baris[1]}</p>"
    return 404, "<h1>Tidak ditemukan</h1>"


def reverse_proxy(path):
    # Langkah 3: berkas statis dijawab sendiri, sisanya ke aplikasi
    if path.endswith((".css", ".png", ".js")):
        return 200, f"(berkas {path} langsung dari disk)"
    return aplikasi(path)


def browser(alamat):
    domain, _, sisa = alamat.partition("/")
    print(f"> {alamat}")
    print(f"  DNS    : {domain} -> {DNS[domain]}")
    status, isi = reverse_proxy("/" + sisa)
    print(f"  status : {status}")
    print(f"  isi    : {isi}")


browser("toko.example.com/produk/7")
browser("toko.example.com/css/gaya.css")
browser("toko.example.com/produk/99")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  > toko.example.com/produk/7",
                    "    DNS    : toko.example.com -> 203.0.113.10",
                    "    status : 200",
                    "    isi    : <h1>Pensil 2B</h1><p>Rp3500</p>",
                    "  > toko.example.com/css/gaya.css",
                    "    DNS    : toko.example.com -> 203.0.113.10",
                    "    status : 200",
                    "    isi    : (berkas /css/gaya.css langsung dari disk)",
                    "  > toko.example.com/produk/99",
                    "    DNS    : toko.example.com -> 203.0.113.10",
                    "    status : 404",
                    "    isi    : <h1>Tidak ditemukan</h1>",
                    "",
                    "Tiap fungsi mewakili satu pihak. Di dunia nyata mereka program terpisah,",
                    "sering di komputer berbeda, dan saling bicara lewat jaringan. Urutannya",
                    "tetap sama: nama diterjemahkan, proxy memilah, aplikasi bertanya ke",
                    "database, jawaban dikirim balik.",
                    "",
                    "Request untuk gaya.css nggak pernah sampai ke aplikasi, karena proxy",
                    "langsung menjawabnya. Request ke produk 99 sampai ke database, tapi",
                    "database nggak punya barisnya, jadi aplikasi menjawab 404.",
                ],
            },
            {
                "heading": "Di mana sebuah request bisa macet",
                "body": [
                    "  - DNS salah atau perubahannya belum sampai: browser bilang alamatnya",
                    "    nggak ditemukan, padahal servernya sehat.",
                    "  - Sambungan ditolak atau kelamaan: server mati, port ditutup firewall,",
                    "    atau proxy nggak bisa menghubungi aplikasi. Nginx melaporkan yang",
                    "    terakhir sebagai 502 Bad Gateway.",
                    "  - Aplikasi error: response 500. Penyebabnya tercatat di log aplikasi.",
                    "  - Database lambat: halaman muncul, tapi lama. Biasanya karena query",
                    "    tanpa indeks atau terlalu banyak query untuk satu halaman.",
                    "",
                    "Kalau kamu hafal urutan langkahnya, kamu tahu harus mengecek di mana",
                    "dulu. Bab 8 dan bab 9 kurikulum ini membahas cara menjaga tiap langkah",
                    "tetap cepat saat penggunanya ribuan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tab Network di DevTools browser (tekan F12) menampilkan setiap request",
                    "yang dikirim sebuah halaman, lengkap dengan status, ukuran, dan",
                    "waktunya. Programmer web memakainya tiap hari untuk mencari langkah mana",
                    "yang bermasalah. Dari terminal, perintah dig dan curl -v dipakai untuk",
                    "hal yang sama.",
                    "",
                    "Kasus kecil: halaman toko temanmu cuma menampilkan \"502 Bad Gateway\"",
                    "dari Nginx. Dia panik dan bilang database-nya rusak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat dulu siapa yang menjawab. Halaman 502 dari Nginx artinya",
                    "     request sudah lewat DNS dan sampai ke proxy. Jadi DNS dan sambungan",
                    "     internet aman.",
                    "  2. Kode 502 artinya proxy gagal mendapat jawaban yang sah dari program",
                    "     di belakangnya. Cek apakah aplikasinya masih jalan, misalnya untuk",
                    "     aplikasi PHP:",
                    "      systemctl status php-fpm",
                    "  3. Kalau aplikasinya mati, baca log-nya untuk tahu kenapa. Kalau",
                    "     hidup, cocokkan alamat atau socket di konfigurasi Nginx dengan",
                    "     alamat tempat aplikasi menunggu.",
                    "  4. Database baru dicek kalau aplikasinya hidup tapi mencatat error",
                    "     koneksi database. Urutan ini menghemat waktu karena kamu mengikuti",
                    "     jalan yang ditempuh request.",
                ],
            },
        ],
    },
    {
        "title": "3. Jalur Belajar per Peran Berdasarkan Roadmap",
        "sections": [
            {
                "body": [
                    "Sesudah tahu ada banyak lapisan, biasanya muncul pertanyaan berikutnya:",
                    "harus belajar yang mana dulu. Itu tergantung pekerjaan yang kamu incar.",
                    "Programmer frontend dan analis data memakai alat yang jauh berbeda,",
                    "walau dasarnya sama.",
                    "",
                    "Rujukan yang banyak dipakai untuk pertanyaan ini adalah roadmap.sh,",
                    "situs berisi peta belajar yang dibuat Kamran Ahmed bersama komunitasnya.",
                    "Per Oktober 2026 ada 96 roadmap di halaman daftarnya. Rinciannya 32",
                    "roadmap peran (misalnya Frontend, Backend, DevOps), 55 roadmap skill",
                    "(misalnya Python, Docker, System Design), 4 roadmap untuk pemula, dan 5",
                    "roadmap praktik terbaik.",
                    "",
                    "Isi roadmap.sh nggak disalin ke aplikasi ini. Yang ada di sini cuma",
                    "pemetaannya: roadmap mana dijawab kurikulum mana, dan dengan urutan apa.",
                ],
            },
            {
                "heading": "Peran dan skill",
                "body": [
                    "Roadmap peran menjawab \"mau jadi apa\". Roadmap skill menjawab \"alat apa",
                    "yang dikuasai\". Satu peran butuh beberapa skill. Backend developer,",
                    "misalnya, butuh satu bahasa, SQL, Git, dan pemahaman API.",
                    "",
                    "Pilih peran dulu, baru skill. Kalau dibalik, kamu gampang terjebak",
                    "mengumpulkan sertifikat alat tanpa tahu alat itu dipakai untuk apa.",
                    "",
                    "Roadmap skill kebanyakan langsung cocok dengan nama kurikulum di sini.",
                    "Python ke Python, SQL ke SQL, roadmap Linux ke CLI Fedora. React, Vue,",
                    "Angular, dan Next.js ke Frontend Modern. Node.js, Django, Laravel, dan",
                    "Spring Boot ke Backend & API. MongoDB, Redis, dan Elasticsearch ke",
                    "Database & Penyimpanan Data. Docker, Kubernetes, AWS, dan Terraform ke",
                    "DevOps & Cloud. Roadmap System Design dan Software Design and",
                    "Architecture dijawab kurikulum yang sedang kamu baca.",
                ],
            },
            {
                "heading": "Peta peran ke kurikulum",
                "bahasa": "teks",
                "code": """Roadmap peran        Urutan kurikulum di aplikasi ini
-------------------  --------------------------------------------------
Frontend             HTML > CSS > JavaScript > TypeScript > Git & GitHub
                     > Frontend Modern > Tech Stack bab 1-3
Backend              satu bahasa (Python/Java/Go/PHP/C#) > SQL
                     > Git & GitHub > Backend & API > Database
                     > Tech Stack bab 8-10
Full Stack           jalur Frontend + jalur Backend > Tech Stack
Android              Kotlin > Git & GitHub > Mobile & Desktop
iOS                  Mobile & Desktop (Swift ada di Bahasa Lain)
DevOps               CLI Fedora > Bash > Git & GitHub > DevOps & Cloud
                     > Tech Stack bab 11
DevSecOps            jalur DevOps > Keamanan Siber
Data Analyst, BI     SQL > Python > Data & Analitik
Data Engineer        SQL > Python > Data & Analitik > DevOps & Cloud
AI Engineer, ML      Python > SQL > Data & Analitik > AI & ML
MLOps                jalur AI > DevOps & Cloud
QA                   satu bahasa > Tech Stack bab 6 > bagian tes di
                     Frontend Modern atau Backend & API
Software Architect   Backend & API > Bikin Aplikasi > Tech Stack
Cyber Security       CLI Fedora > Bash > Keamanan Siber
Game Developer       Game & Grafis (+ C# atau C++)
Technical Writer     Git & GitHub > Tech Stack bab 12""",
            },
            {
                "body": [
                    "Roadmap peran lain juga punya pasangan. PostgreSQL DBA ke SQL lalu",
                    "Database & Penyimpanan Data. API Design ke Backend & API lalu bab 8 dan",
                    "bab 10 kurikulum ini. Server Side Game Developer ke Game & Grafis lalu",
                    "Backend & API. AI Red Teaming ke AI & Machine Learning lalu Keamanan",
                    "Siber. Inference Engineering ikut jalur AI.",
                    "",
                    "Ada juga yang belum punya kurikulum sendiri. UX Design dan SEO cuma",
                    "tersentuh sebagian di Frontend Modern. Blockchain baru sebatas bahasa",
                    "Solidity di Bahasa Pemrograman Lain dan dasar kriptografi di Keamanan",
                    "Siber. Network Engineer terbantu CLI Fedora, DevOps & Cloud, dan",
                    "sebagian Keamanan Siber. Product Manager, Engineering Manager, dan",
                    "Developer Relations cukup memakai peta di bab 1 dan bab 12 kurikulum",
                    "ini.",
                    "",
                    "Satu celah lagi perlu kamu tahu dari awal. Roadmap Computer Science,",
                    "Data Structures and Algorithms, dan LeetCode belum punya kurikulum",
                    "khusus di sini. Sebagian isinya tersebar di latihan kurikulum bahasa.",
                    "Kalau kamu mengincar wawancara kerja yang menguji algoritma, siapkan",
                    "sumber tambahan.",
                ],
            },
            {
                "heading": "Alat kerja: editor dan IDE",
                "body": [
                    "IDE (integrated development environment) adalah editor kode yang",
                    "dilengkapi alat bantu seperti pelengkap otomatis, debugger, dan",
                    "terminal. Di Survei Stack Overflow 2026, Visual Studio Code dipakai 71%",
                    "responden. Di bawahnya ada Notepad++ dan Visual Studio (masing-masing",
                    "28%), Vim (27%), dan IntelliJ IDEA (24%).",
                    "",
                    "Beberapa peran punya IDE khas:",
                    "",
                    "  - Android: Android Studio. iOS: Xcode, yang cuma jalan di macOS.",
                    "  - Java dan Kotlin di backend: IntelliJ. C# dan .NET: Visual Studio",
                    "    atau Rider.",
                    "  - Data dan AI: Jupyter Notebook atau JupyterLab, PyCharm, dan RStudio",
                    "    untuk bahasa R.",
                    "  - Frontend, backend JavaScript, Python, Go, dan kebanyakan lainnya: VS",
                    "    Code sudah cukup.",
                    "",
                    "Editor berbantuan AI seperti Cursor (15% di survei yang sama) juga makin",
                    "sering dipakai, dan cara memakainya dengan aman dibahas di bab 12. Kalau",
                    "baru mulai, pilih satu editor dan pakai terus. Hafal pintasan satu",
                    "editor lebih berguna daripada mencoba lima editor.",
                ],
            },
            {
                "heading": "Tempat bertanya",
                "body": [
                    "Kamu bakal sering mentok, dan itu wajar. Survei yang sama menanyakan",
                    "platform komunitas yang rutin dipakai untuk urusan teknologi. Hasilnya:",
                    "GitHub 70%, Stack Overflow 69%, YouTube 58%, Reddit 54%, LinkedIn 38%,",
                    "dan Discord 33%.",
                    "",
                    "Pertanyaan yang cepat dijawab biasanya memuat ini:",
                    "",
                    "  - Apa yang sedang kamu coba lakukan, dalam satu atau dua kalimat.",
                    "  - Kode terkecil yang masih memunculkan masalahnya. Seluruh proyek",
                    "    terlalu panjang untuk dibaca orang lain.",
                    "  - Pesan error lengkap yang disalin sebagai teks, ditambah apa saja",
                    "    yang sudah kamu coba.",
                ],
            },
            {
                "heading": "Contoh: jalur sebagai data",
                "code": """JALUR = {
    "frontend": ["HTML", "CSS", "JavaScript", "TypeScript",
                 "Git & GitHub", "Frontend Modern"],
    "backend": ["Python", "SQL", "Git & GitHub",
                "Backend & API", "Database & Penyimpanan Data"],
    "devops": ["CLI Fedora", "Bash", "Git & GitHub", "DevOps & Cloud"],
}

SELESAI = {"HTML", "CSS", "Git & GitHub"}

peran = "frontend"
print(f"Jalur {peran}:")
for nomor, kurikulum in enumerate(JALUR[peran], start=1):
    tanda = "x" if kurikulum in SELESAI else " "
    print(f"  [{tanda}] {nomor}. {kurikulum}")

berikutnya = next(k for k in JALUR[peran] if k not in SELESAI)
print(f"Berikutnya: {berikutnya}")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Jalur frontend:",
                    "    [x] 1. HTML",
                    "    [x] 2. CSS",
                    "    [ ] 3. JavaScript",
                    "    [ ] 4. TypeScript",
                    "    [x] 5. Git & GitHub",
                    "    [ ] 6. Frontend Modern",
                    "  Berikutnya: JavaScript",
                    "",
                    "Ubah nilai peran jadi \"devops\" lalu jalankan lagi. Yang tercentang",
                    "tinggal Git & GitHub, dan saran berikutnya berubah jadi CLI Fedora. Git",
                    "& GitHub muncul di ketiga jalur, jadi kurikulum itu aman dikerjakan",
                    "kapan saja.",
                ],
            },
            {
                "heading": "Supaya peta nggak bikin tersesat",
                "body": [
                    "  - Roadmap itu peta. Kotak-kotak di sana nggak harus dicentang semua",
                    "    sebelum kamu boleh melamar kerja.",
                    "  - Selesaikan satu jalur sampai kamu bisa bikin satu proyek kecil yang",
                    "    jalan. Proyek itu lebih meyakinkan di lamaran daripada daftar",
                    "    kursus.",
                    "  - Sesudah satu jalur, lirik jalur sebelahnya. Orang frontend yang",
                    "    paham sedikit backend lebih gampang bekerja sama dengan tim backend.",
                    "",
                    "Ingat: peran-peran ini saling tumpang tindih. Banyak lowongan di",
                    "perusahaan kecil meminta satu orang memegang frontend dan backend",
                    "sekaligus. Di situ jalur Full Stack yang berlaku.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak program magang dan bootcamp menyusun silabusnya mirip roadmap",
                    "peran: dasar web dulu, lalu satu framework, lalu proyek akhir. Lowongan",
                    "kerja juga biasanya ditulis per peran, misalnya \"Frontend Developer\"",
                    "atau \"Data Analyst\", lengkap dengan daftar alat yang dipakai timnya.",
                    "",
                    "Kasus kecil: kamu PKL di kantor yang mengurus server dan website",
                    "sekolah. Pembimbingmu bilang kamu bakal banyak membantu di bagian",
                    "server. Kamu bingung mau belajar apa di sisa waktu PKL.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Terjemahkan pekerjaannya jadi peran. Mengurus server paling dekat",
                    "     dengan roadmap DevOps.",
                    "  2. Ambil urutannya dari peta: CLI Fedora, Bash, Git & GitHub, lalu",
                    "     DevOps & Cloud.",
                    "  3. Cocokkan dengan yang dipakai kantornya. Tanyakan sistem operasi",
                    "     server dan cara website-nya dipasang. Kalau ternyata website",
                    "     sekolah memakai PHP dan MySQL, tambahkan bab 2 kurikulum ini",
                    "     tentang stack web klasik.",
                    "  4. Mulai dari yang langsung kepakai minggu ini, yaitu perintah dasar",
                    "     Linux di CLI Fedora. Sisanya menyusul sambil kamu melihat pekerjaan",
                    "     sehari-hari tim.",
                ],
            },
        ],
    },
    {
        "title": "4. LAMP, LEMP, dan Paket Server Lokal",
        "sections": [
            {
                "body": [
                    "LAMP adalah stack web klasik. Isinya empat program terpisah: Linux",
                    "sebagai sistem operasi, Apache sebagai web server, MySQL atau MariaDB",
                    "sebagai database, dan PHP sebagai bahasa di sisi server. Namanya muncul",
                    "tahun 1998 di majalah komputer Jerman c't.",
                    "",
                    "Stack ini masih menopang sebagian besar web. Menurut W3Techs (Oktober",
                    "2026), PHP dipakai 69,4% situs yang bahasa server-nya diketahui, banyak",
                    "di antaranya lewat WordPress. Survei Stack Overflow 2026 mencatat MySQL",
                    "dipakai 35,1% responden, MariaDB 20,3%, dan PHP 18%.",
                    "",
                    "MariaDB adalah cabang (fork) dari MySQL yang dibuat sebagian pengembang",
                    "awal MySQL. Perintah SQL keduanya hampir sama, jadi yang kamu pelajari",
                    "di kurikulum SQL berlaku di dua-duanya.",
                    "",
                    "Jebakan: mengira stack ini satu program. Keempatnya dipasang dan",
                    "dinyalakan sendiri-sendiri, lalu harus disambungkan: web server ke PHP,",
                    "PHP ke database, dan hak akses folder situs harus benar.",
                ],
            },
            {
                "heading": "Apache dan Nginx: dua cara melayani",
                "body": [
                    "Web server adalah program yang menunggu request HTTP lalu menjawabnya.",
                    "Dua yang paling sering dipasangkan dengan PHP adalah Apache httpd dan",
                    "Nginx.",
                    "",
                    "Apache sudah ada sejak 1995. Dia bisa memuat PHP langsung di dalam",
                    "prosesnya lewat modul mod_php, atau meneruskannya ke PHP-FPM. Apache",
                    "juga membaca berkas .htaccess di tiap folder. Dengan berkas itu, pemilik",
                    "situs di shared hosting bisa mengatur alamat dan akses tanpa menyentuh",
                    "konfigurasi utama server.",
                    "",
                    "Nginx (dibaca engine-x, makanya hurufnya E) dirancang untuk melayani",
                    "banyak sambungan sekaligus dengan memori kecil. Nginx nggak bisa",
                    "menjalankan PHP sendiri. Dia meneruskan request ke PHP-FPM, program",
                    "terpisah yang menjaga sekumpulan proses PHP siap pakai. Protokol",
                    "penerusannya bernama FastCGI. Ganti Apache dengan Nginx dan kamu dapat",
                    "LEMP, kadang ditulis LNMP.",
                    "",
                    "Di data W3Techs Oktober 2026, Cloudflare Server terlihat di 32,5% situs,",
                    "Nginx 30,3%, Apache 21,4%, dan LiteSpeed 14,0%. Cloudflare ada di urutan",
                    "pertama karena banyak situs memasang layanan Cloudflare di depan server",
                    "aslinya. Di belakangnya tetap ada Nginx, Apache, atau server lain.",
                    "",
                    "Konfigurasi Nginx untuk aplikasi PHP seperti Laravel kira-kira begini:",
                ],
            },
            {
                "heading": "Server block Nginx untuk aplikasi PHP",
                "bahasa": "nginx",
                "code": "server {\n    listen 80;\n    server_name toko.test;\n    root /var/www/toko/public;\n    index index.php;\n\n    location / {\n        try_files $uri $uri/ /index.php?$query_string;\n    }\n\n    location ~ \\.php$ {\n        include fastcgi_params;\n        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;\n        fastcgi_pass unix:/run/php-fpm/www.sock;\n    }\n}",
            },
            {
                "body": [
                    "  - root menunjuk ke folder public, satu-satunya folder yang boleh",
                    "    dilihat pengunjung. Berkas konfigurasi dan kode aplikasi ada di luar",
                    "    folder itu.",
                    "  - try_files mencari berkas yang cocok dengan path. Kalau nggak ada,",
                    "    dia mencoba path itu sebagai folder. Kalau tetap nggak ada, request",
                    "    diserahkan ke /index.php. Dari index.php itu Laravel membaca path",
                    "    dan memilih rutenya.",
                    "  - Blok location yang kedua menangani berkas berakhiran .php.",
                    "    fastcgi_pass menunjuk socket tempat PHP-FPM menunggu. Di Fedora",
                    "    alamat bawaannya /run/php-fpm/www.sock.",
                    "",
                    "Program di bawah ini meniru keputusan yang diambil Nginx dengan",
                    "konfigurasi tadi, lalu menunjukkan apa yang terjadi kalau baris",
                    "try_files dihapus.",
                ],
            },
            {
                "heading": "Meniru keputusan Nginx",
                "code": """BERKAS_DI_DISK = {"/css/app.css", "/img/logo.png", "/index.php"}


def nginx(path, pakai_try_files=True):
    if path.endswith(".php"):
        return f"PHP-FPM menjalankan {path}"
    if path in BERKAS_DI_DISK:
        return "berkas statis dikirim langsung"
    if pakai_try_files:
        return f"PHP-FPM menjalankan /index.php (rute {path})"
    return "404 Not Found"


for path in ["/css/app.css", "/produk/7", "/index.php"]:
    print(f"{path:<13} -> {nginx(path)}")

print("tanpa try_files:")
print(f"{'/produk/7':<13} -> {nginx('/produk/7', pakai_try_files=False)}")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  /css/app.css  -> berkas statis dikirim langsung",
                    "  /produk/7     -> PHP-FPM menjalankan /index.php (rute /produk/7)",
                    "  /index.php    -> PHP-FPM menjalankan /index.php",
                    "  tanpa try_files:",
                    "  /produk/7     -> 404 Not Found",
                    "",
                    "Tanpa try_files, Nginx mencari berkas bernama produk/7 di disk, nggak",
                    "menemukannya, lalu menjawab 404. Halaman depan tetap tampil karena",
                    "alamat / langsung jatuh ke index.php lewat baris index. Itu yang membuat",
                    "masalah ini membingungkan: sebagian situs jalan, sebagian lagi nggak.",
                ],
            },
            {
                "heading": "Memasang di Fedora",
                "bahasa": "terminal",
                "code": """# LAMP: Apache (di Fedora paketnya bernama httpd), PHP, dan MariaDB
sudo dnf install httpd php php-fpm php-mysqlnd mariadb-server
sudo systemctl enable --now httpd php-fpm mariadb

# LEMP: Nginx menggantikan httpd
sudo dnf install nginx
sudo systemctl enable --now nginx""",
            },
            {
                "body": [
                    "Di Fedora, nama paket Apache adalah httpd. Di Ubuntu namanya apache2,",
                    "jadi tutorial dari distro lain sering nggak cocok persis. Fedora juga",
                    "memasang SELinux, yang menolak web server membaca folder di luar",
                    "/var/www sampai label keamanannya disetel. Arti tiap perintah tadi",
                    "dibahas di kurikulum CLI Fedora.",
                ],
            },
            {
                "heading": "Paket server lokal: XAMPP, Laragon, dan kawan-kawan",
                "body": [
                    "Memasang empat program satu per satu itu repot buat pemula, apalagi di",
                    "Windows. Karena itu muncul paket server lokal: satu pemasang yang berisi",
                    "semuanya.",
                    "",
                    "  - XAMPP berisi Apache, MariaDB, PHP, Perl, dan phpMyAdmin, dan banyak",
                    "    dipakai di sekolah. Rilis terakhirnya 8.2.12 tanggal 21 November",
                    "    2023, berisi Apache 2.4.58, MariaDB 10.4.32, dan PHP 8.2.12. Sampai",
                    "    Oktober 2026 belum ada rilis baru. MariaDB 10.4 di dalamnya sudah",
                    "    habis masa dukungannya, dan PHP 8.2 tinggal menerima perbaikan",
                    "    keamanan.",
                    "  - Laragon cuma untuk Windows. Isinya pilihan versi PHP, Node.js,",
                    "    Apache atau Nginx, MySQL, dan PostgreSQL, plus domain lokal",
                    "    berakhiran .test. Ada versi gratis dan versi berbayar.",
                    "  - WampServer untuk Windows dan MAMP, yang awalnya dibuat untuk macOS,",
                    "    bekerja dengan cara serupa.",
                    "",
                    "Jebakan: paket server lokal dibuat untuk belajar di komputer sendiri.",
                    "Akun root database-nya bawaan tanpa sandi, phpMyAdmin langsung masuk",
                    "sebagai root, dan kebiasaan menaruh semua berkas di htdocs nggak berlaku",
                    "di server sungguhan. Jangan pernah memakainya untuk server yang bisa",
                    "diakses dari internet.",
                    "",
                    "Pengganti yang lebih modern adalah Docker Compose. Tiap komponen jalan",
                    "di kontainernya sendiri, versinya ditulis di satu berkas, dan berkas itu",
                    "bisa dipakai siapa pun di tim. Contohnya:",
                ],
            },
            {
                "heading": "compose.yaml untuk PHP dan MariaDB",
                "bahasa": "yaml",
                "code": """services:
  web:
    image: php:8.4-apache
    ports:
      - "8080:80"
    volumes:
      - ./src:/var/www/html
  db:
    image: mariadb:lts
    environment:
      MARIADB_ROOT_PASSWORD: ganti-sandi-ini
      MARIADB_DATABASE: toko""",
            },
            {
                "body": [
                    "Berkas ini menyalakan dua kontainer. Kontainer web berisi Apache dan PHP",
                    "8.4, kontainer db berisi MariaDB versi LTS (dukungan jangka panjang).",
                    "Image php:8.4-apache belum memuat ekstensi untuk tersambung ke MariaDB.",
                    "Cara menambahkannya lewat Dockerfile dibahas di kurikulum DevOps &",
                    "Cloud, bersama cara menyimpan sandi di luar berkas yang di-commit.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Paket shared hosting murah biasanya menjual kombinasi PHP, MySQL atau",
                    "MariaDB, dan web server Apache, Nginx, atau LiteSpeed, sering dengan",
                    "panel seperti cPanel. Situs WordPress sekolah, toko kecil, dan blog",
                    "pribadi banyak yang berjalan di paket seperti itu.",
                    "",
                    "Kasus kecil: kamu memindahkan aplikasi Laravel tugas sekolah dari XAMPP",
                    "di laptop ke VPS Fedora yang memakai Nginx. Halaman depan tampil, tapi",
                    "setiap tautan lain menghasilkan 404.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bandingkan kedua tempat. Di laptop, Apache membaca berkas .htaccess",
                    "     bawaan Laravel di folder public, dan berkas itu mengarahkan semua",
                    "     alamat ke index.php. Nginx nggak membaca .htaccess sama sekali.",
                    "  2. Buka server block Nginx untuk situs itu. Pastikan root menunjuk ke",
                    "     folder public di dalam proyek.",
                    "  3. Tambahkan aturan yang tadinya dikerjakan .htaccess di dalam",
                    "     location /:",
                    "      try_files $uri $uri/ /index.php?$query_string;",
                    "  4. Uji konfigurasinya dengan sudo nginx -t, lalu muat ulang dengan",
                    "     sudo systemctl reload nginx. Buka lagi /produk/7. Kalau sekarang",
                    "     muncul 502, berarti PHP-FPM yang belum jalan, dan itu yang dicek",
                    "     berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "5. MVC dan Arsitektur Berlapis",
        "sections": [
            {
                "body": [
                    "Bayangkan satu berkas produk.php yang isinya campur aduk: membuka",
                    "koneksi database, menjalankan query, memeriksa isian formulir, lalu",
                    "mencetak HTML. Untuk halaman pertama, cara ini cepat. Begitu halamannya",
                    "puluhan, mengubah tampilan tabel bisa merusak query, dan nggak ada yang",
                    "berani menyentuh berkasnya.",
                    "",
                    "MVC (Model-View-Controller) membagi kode jadi tiga peran supaya hal itu",
                    "nggak terjadi:",
                    "",
                    "  - Model: data dan aturannya. Misalnya produk punya nama dan harga, dan",
                    "    harga nggak boleh negatif. Model juga yang berbicara dengan",
                    "    database.",
                    "  - View: tampilan. Tugasnya mengubah data jadi HTML atau teks lain,",
                    "    tanpa mengambil keputusan bisnis.",
                    "  - Controller: penerima input. Dia membaca request, memanggil model,",
                    "    lalu memilih view untuk menjawab.",
                    "",
                    "Pola ini lahir di bahasa Smalltalk pada akhir 1970-an, dirumuskan oleh",
                    "Trygve Reenskaug. Esai Martin Fowler \"GUI Architectures\" (2006) menyebut",
                    "MVC salah satu pola yang paling sering disalahpahami. Versi di framework",
                    "web memang sudah bergeser jauh dari versi aslinya untuk aplikasi",
                    "desktop.",
                ],
            },
            {
                "heading": "Satu request di aplikasi MVC",
                "body": [
                    "  1. Router mencocokkan GET /buku/2 dengan daftar rute, lalu memilih",
                    "     controller.",
                    "  2. Controller membaca parameter 2, lalu meminta model mencari buku",
                    "     bernomor 2.",
                    "  3. Model menjalankan query ke database dan mengembalikan datanya,",
                    "     termasuk jawaban atas aturan \"boleh dipinjam atau nggak\".",
                    "  4. Controller menyerahkan data itu ke view.",
                    "  5. View menyusun teks atau HTML, dan controller mengirimnya sebagai",
                    "     response.",
                    "",
                    "Program di bawah ini memakai urutan yang sama untuk aplikasi",
                    "perpustakaan kecil. Tiap peran ditandai komentar.",
                ],
            },
            {
                "heading": "MVC mini dengan SQLite",
                "code": """import sqlite3

# ---- model: data dan aturannya
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE buku (id INTEGER PRIMARY KEY, judul TEXT, stok INTEGER)")
db.executemany("INSERT INTO buku (judul, stok) VALUES (?, ?)",
               [("Laskar Pelangi", 3), ("Bumi Manusia", 0)])


def cari_buku(id_buku):
    return db.execute("SELECT id, judul, stok FROM buku WHERE id = ?",
                      (id_buku,)).fetchone()


def bisa_dipinjam(buku):
    return buku[2] > 0


# ---- view: data menjadi teks
def view_buku(buku, tersedia):
    status = "bisa dipinjam" if tersedia else "stok habis"
    return f"[{buku[0]}] {buku[1]} ({status})"


def view_404(pesan):
    return f"404: {pesan}"


# ---- controller: baca input, panggil model, pilih view
def controller_buku(id_teks):
    if not id_teks.isdigit():
        return view_404("nomor buku harus angka")
    buku = cari_buku(int(id_teks))
    if buku is None:
        return view_404(f"buku {id_teks} tidak ada")
    return view_buku(buku, bisa_dipinjam(buku))


# ---- router: bagian pertama path menentukan controller
RUTE = {"buku": controller_buku}


def tangani(path):
    nama, _, param = path.strip("/").partition("/")
    controller = RUTE.get(nama)
    if controller is None:
        return view_404(f"rute /{nama} tidak ada")
    return controller(param)


for path in ["/buku/1", "/buku/2", "/buku/9", "/anggota/1"]:
    print(f"{path:<11} {tangani(path)}")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  /buku/1     [1] Laskar Pelangi (bisa dipinjam)",
                    "  /buku/2     [2] Bumi Manusia (stok habis)",
                    "  /buku/9     404: buku 9 tidak ada",
                    "  /anggota/1  404: rute /anggota tidak ada",
                    "",
                    "Coba ubah tampilan di view_buku. Model dan controller nggak perlu",
                    "disentuh. Begitu juga sebaliknya: kalau aturan peminjaman berubah,",
                    "misalnya stok terakhir nggak boleh dipinjam, cukup bisa_dipinjam yang",
                    "diganti.",
                ],
            },
            {
                "heading": "MVC di framework sungguhan",
                "body": [
                    "Framework web di sisi server hampir semuanya menyiapkan folder untuk",
                    "tiga peran ini. Begitu kamu kenal polanya, proyek baru jadi lebih",
                    "gampang dibaca. Survei Stack Overflow 2026 mencatat ASP.NET Core dipakai",
                    "20% responden, Spring Boot 13%, Django 11%, Laravel 8%, dan Ruby on",
                    "Rails 6%.",
                ],
            },
            {
                "heading": "Letak tiap peran di lima framework",
                "bahasa": "teks",
                "code": """Framework          Model           View                Controller
-----------------  --------------  ------------------  ---------------------
Laravel (PHP)      app/Models      resources/views     app/Http/Controllers
Ruby on Rails      app/models      app/views           app/controllers
Django (Python)    models.py       templates/          views.py
Spring MVC (Java)  kelas @Entity   templates/          kelas @Controller
ASP.NET Core MVC   Models/         Views/              Controllers/""",
            },
            {
                "body": [
                    "Django memakai istilah sendiri, yaitu MTV (Model-Template-View).",
                    "Template di Django sama dengan view di MVC, dan view di Django sama",
                    "dengan controller di MVC. Isinya sama, cuma namanya yang bergeser, jadi",
                    "jangan bingung waktu membaca dokumentasinya.",
                    "",
                    "Di Laravel, rute dan controller untuk halaman detail produk kira-kira",
                    "begini:",
                ],
            },
            {
                "heading": "Rute dan controller Laravel",
                "bahasa": "php",
                "code": """// routes/web.php
Route::get('/produk/{produk}', [ProdukController::class, 'show']);

// app/Http/Controllers/ProdukController.php
class ProdukController extends Controller
{
    public function show(Produk $produk)
    {
        return view('produk.show', ['produk' => $produk]);
    }
}""",
            },
            {
                "body": [
                    "Laravel mengisi parameter $produk dari database berdasarkan {produk} di",
                    "rute. Fitur ini namanya route model binding. View produk.show menunjuk",
                    "berkas resources/views/produk/show.blade.php.",
                ],
            },
            {
                "heading": "MVP dan arsitektur berlapis",
                "body": [
                    "MVP (Model-View-Presenter) mirip MVC, dengan view yang dibuat pasif.",
                    "Presenter mengambil data dari model lalu menyuruh view menampilkan",
                    "sesuatu, sehingga presenter gampang dites tanpa layar sungguhan. Pola",
                    "ini banyak ditemui di aplikasi desktop dan aplikasi Android versi lama.",
                    "Aplikasi Android sekarang lebih sering memakai MVVM, yang dibahas di bab",
                    "7.",
                    "",
                    "Arsitektur berlapis (layered, atau N-tier) memperluas ide yang sama ke",
                    "seluruh aplikasi. Kodenya dibagi jadi lapisan bertumpuk: presentasi,",
                    "logika bisnis, dan akses data. Tiap lapisan cuma boleh memanggil lapisan",
                    "di bawahnya. Di proyek Laravel atau Spring, susunannya sering berbentuk",
                    "controller, lalu service, lalu repository.",
                    "",
                    "Kata tier kadang dipakai untuk pembagian fisik: frontend di satu mesin,",
                    "backend di mesin lain, database di mesin ketiga. Layer adalah pembagian",
                    "kode di dalam satu program. Satu program bisa punya tiga layer walau",
                    "berjalan di satu mesin.",
                    "",
                    "Panduan arsitektur Azure dari Microsoft mencatat kelemahan pola ini:",
                    "satu perubahan fitur sering menyentuh semua lapisan sekaligus. Cara",
                    "membangun lapisan service dan repository di Java dibahas tuntas di",
                    "kurikulum Bikin Aplikasi.",
                    "",
                    "Jebakan: controller gemuk. Semua aturan ditaruh di controller karena di",
                    "situ request pertama kali masuk. Lama-lama satu method berisi ratusan",
                    "baris, dan aturan yang sama ditulis ulang di controller lain. Aturan",
                    "bisnis tempatnya di model atau service.",
                    "",
                    "Kesalahan lain: view yang menjalankan query sendiri. Template Blade atau",
                    "Jinja memang bisa memanggil database, tapi hasilnya kembali ke berkas",
                    "campur aduk tadi. View cukup menerima data yang sudah disiapkan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan Laravel, Rails, Django, dan Spring hampir selalu meminta",
                    "pemahaman MVC, karena struktur folder bawaan framework itu memakai pola",
                    "ini. Waktu membuka proyek warisan, programmer biasanya mulai dari berkas",
                    "rute, lalu mengikuti controller-nya, baru ke model dan view.",
                    "",
                    "Kasus kecil: kamu diminta menampilkan kolom diskon di halaman detail",
                    "produk sebuah proyek Laravel yang belum pernah kamu lihat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari rutenya dulu. Buka routes/web.php dan cari alamat halaman",
                    "     detail, misalnya /produk/{produk}. Di situ tertulis controller dan",
                    "     method yang dipanggil.",
                    "  2. Buka controller itu. Biasanya isinya pendek: mengambil model lalu",
                    "     memanggil view('produk.show', ...). Dari situ kamu tahu nama",
                    "     view-nya.",
                    "  3. Tambahkan kolom diskon di lapisan data: migration untuk tabel",
                    "     produk, dan aturan di model kalau perlu, misalnya diskon nggak",
                    "     boleh lebih besar dari harga.",
                    "  4. Tampilkan di view resources/views/produk/show.blade.php:",
                    "      <p>Diskon: Rp{{ $produk->diskon }}</p>",
                    "     Controller nggak perlu diubah, karena dia sudah mengirim seluruh",
                    "     objek produk ke view.",
                ],
            },
        ],
    },
    {
        "title": "6. Pola Rendering Web: MPA, SPA, SSR, SSG, dan Islands",
        "sections": [
            {
                "body": [
                    "Setiap halaman web pada akhirnya berupa HTML yang dibaca browser. Yang",
                    "membedakan: HTML itu dibuat di mana, dan kapan. Bisa di server setiap",
                    "kali ada request, bisa di browser oleh JavaScript, bisa juga sekali saja",
                    "waktu situsnya dibangun. Pilihan ini disebut pola rendering, dan pola",
                    "ini ikut menentukan framework apa yang cocok.",
                    "",
                    "Istilahnya banyak dan mirip-mirip. Materi ini membahasnya satu per satu,",
                    "lalu merangkumnya dalam satu tabel.",
                ],
            },
            {
                "heading": "MPA dan SSR: HTML dibuat di server",
                "body": [
                    "MPA (multi-page application) adalah cara paling tua. Setiap klik tautan",
                    "mengirim request baru, server menyusun HTML utuh, dan browser memuat",
                    "ulang seluruh halaman. Laravel, Rails, dan Django dengan template",
                    "bawaannya bekerja begini. Contoh MVC di materi sebelumnya juga termasuk",
                    "jenis ini.",
                    "",
                    "SSR (server-side rendering) juga berarti HTML disusun di server per",
                    "request. Istilah ini sering dipakai di dunia framework JavaScript",
                    "seperti Next.js dan Nuxt: komponen React atau Vue dijalankan di server",
                    "jadi HTML, lalu dikirim ke browser.",
                    "",
                    "Kelebihannya, halaman langsung terbaca begitu HTML tiba, termasuk oleh",
                    "mesin pencari. Kekurangannya, tiap request membebani server, dan di",
                    "aplikasi multi-page pindah halaman berarti memuat ulang.",
                ],
            },
            {
                "heading": "SPA: HTML dibangun di browser",
                "body": [
                    "SPA (single-page application), disebut juga CSR (client-side rendering),",
                    "membalik urutannya. Server mengirim HTML yang hampir kosong ditambah",
                    "berkas JavaScript. JavaScript itu yang meminta data dalam bentuk JSON",
                    "lalu membangun halaman di browser.",
                    "",
                    "Sesudah dimuat, pindah halaman terasa cepat karena nggak ada pemuatan",
                    "ulang. Tapi layar pertama baru muncul setelah JavaScript selesai diunduh",
                    "dan dijalankan. Di HP murah dengan sinyal lemah, jedanya terasa.",
                    "Contohnya aplikasi React yang dibuat dengan Vite tanpa meta-framework.",
                    "",
                    "Program di bawah membandingkan HTML pertama yang dikirim kedua cara itu.",
                ],
            },
            {
                "heading": "HTML pertama: SSR dan CSR",
                "code": """import json

PRODUK = [{"nama": "Pensil 2B", "harga": 3500},
          {"nama": "Penghapus", "harga": 2000}]


def ssr():
    # server menyusun HTML lengkap untuk tiap request
    isi = "".join(f"<li>{p['nama']} Rp{p['harga']}</li>" for p in PRODUK)
    return f"<html><body><ul>{isi}</ul></body></html>"


def csr():
    # server cuma mengirim kerangka; datanya diminta JavaScript belakangan
    kerangka = ('<html><body><div id="root"></div>'
                '<script src="app.js"></script></body></html>')
    return kerangka, json.dumps(PRODUK)


html_ssr = ssr()
html_csr, data_csr = csr()

# "mesin pencari" yang cuma membaca HTML pertama, tanpa menjalankan JS
print("SSR: nama produk ada di HTML pertama?", "Pensil 2B" in html_ssr)
print("CSR: nama produk ada di HTML pertama?", "Pensil 2B" in html_csr)
print(f"CSR: datanya menyusul lewat request kedua, {len(data_csr)} byte JSON")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  SSR: nama produk ada di HTML pertama? True",
                    "  CSR: nama produk ada di HTML pertama? False",
                    "  CSR: datanya menyusul lewat request kedua, 76 byte JSON",
                    "",
                    "Mesin pencari besar seperti Google bisa menjalankan JavaScript, tapi",
                    "tahap itu menyusul sesudah HTML-nya dibaca. Situs yang perlu ditemukan",
                    "lewat pencarian, seperti toko dan blog, karena itu biasanya memilih SSR",
                    "atau SSG.",
                ],
            },
            {
                "heading": "SSG dan ISR: HTML dibuat lebih awal",
                "body": [
                    "SSG (static site generation) menyusun semua HTML sekali, waktu situs",
                    "dibangun (build). Hasilnya berkas statis yang tinggal dikirim, sering",
                    "lewat CDN, yaitu jaringan server yang menyimpan salinan berkas di banyak",
                    "kota. Cepat dan murah, cocok untuk blog, dokumentasi, dan halaman",
                    "pemasaran. Kekurangannya, data yang berubah baru terlihat setelah build",
                    "ulang.",
                    "",
                    "ISR (incremental static regeneration) adalah istilah dari Next.js untuk",
                    "jalan tengahnya. Halaman statis dibangun ulang di latar belakang setelah",
                    "jangka waktu tertentu, atau saat diminta, tanpa membangun ulang seluruh",
                    "situs.",
                ],
            },
            {
                "heading": "Hydration, streaming, dan islands",
                "body": [
                    "Hydration adalah langkah yang menyusul SSR. HTML dari server sudah",
                    "tampil, lalu JavaScript diunduh dan menempelkan perilaku ke elemennya,",
                    "misalnya membuat tombol bisa diklik. Sebelum hydration selesai, halaman",
                    "terlihat siap tapi tombolnya belum bereaksi.",
                    "",
                    "Streaming berarti server mengirim HTML sepotong demi sepotong. Bagian",
                    "atas halaman sudah tampil sementara bagian yang datanya lambat menyusul.",
                    "",
                    "Islands architecture memakai hydration seperlunya. Halamannya sebagian",
                    "besar HTML statis, dan cuma bagian interaktif seperti tombol keranjang",
                    "atau kolom pencarian yang diberi JavaScript. Bagian kecil itu disebut",
                    "pulau (island). Menurut dokumentasi Astro, istilah component island",
                    "dicetuskan Katie Sylor-Miller dari Etsy pada 2019, lalu dikembangkan",
                    "Jason Miller dalam tulisannya tahun 2020. Astro adalah framework yang",
                    "paling dikenal dengan pola ini.",
                ],
            },
            {
                "heading": "Ringkasan pola rendering",
                "bahasa": "teks",
                "code": """Pola      HTML dibuat              Cocok untuk            Contoh
--------  -----------------------  ---------------------  ----------------
MPA, SSR  di server, tiap request  toko, aplikasi bisnis  Laravel, Next.js
SPA, CSR  di browser, oleh JS      dasbor sesudah login   React + Vite
SSG       sekali, saat build       blog, dokumentasi      Astro, Hugo
ISR       build, lalu diulang      daftar produk besar    Next.js
Islands   statis + pulau JS        konten + sedikit UI    Astro""",
            },
            {
                "heading": "Memilih polanya",
                "body": [
                    "  - Halaman harus ditemukan lewat mesin pencari dan datanya sering",
                    "    berubah: SSR.",
                    "  - Isinya jarang berubah: SSG, ditambah islands kalau ada sedikit",
                    "    bagian interaktif.",
                    "  - Aplikasi di balik login yang interaksinya padat, misalnya dasbor",
                    "    admin atau editor: SPA cukup, karena mesin pencari memang nggak",
                    "    perlu masuk.",
                    "  - Banyak framework sekarang mencampur pola per halaman. Next.js, Nuxt,",
                    "    SvelteKit, dan Astro bisa membuat satu halaman statis dan halaman",
                    "    lain SSR di proyek yang sama.",
                    "",
                    "Survei Stack Overflow 2026 mencatat Next.js dipakai 21% responden, Astro",
                    "dan SvelteKit masing-masing 6%, dan Nuxt 4%. Meta-framework seperti ini",
                    "dibahas di bab 3 dan di kurikulum Frontend Modern.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Klik kanan di sebuah halaman lalu pilih View Page Source (Ctrl+U). Kalau",
                    "nama produk dan harganya terlihat di sumber itu, halamannya dirender di",
                    "server atau saat build. Kalau yang terlihat cuma <div id=\"root\"></div>",
                    "dan tag script, halamannya SPA. Cara ini bisa kamu pakai di situs mana",
                    "pun.",
                    "",
                    "Kasus kecil: toko roti langgananmu punya situs daftar produk buatan",
                    "React murni (SPA). Pemiliknya mengeluh produknya nggak muncul rapi di",
                    "hasil pencarian, dan halaman pertama lama terbuka di HP pelanggan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan dulu gejalanya. Buka View Page Source. Kalau isinya cuma",
                    "     kerangka kosong, mesin pencari dan HP lambat sama-sama harus",
                    "     menunggu JavaScript.",
                    "  2. Lihat seberapa sering datanya berubah. Daftar roti diganti beberapa",
                    "     kali seminggu, jadi SSG dengan build ulang tiap ada perubahan sudah",
                    "     cukup.",
                    "  3. Kalau perubahan harus langsung terlihat, misalnya stok harian,",
                    "     pilih SSR untuk halaman produk, atau ISR dengan jeda beberapa",
                    "     menit.",
                    "  4. Pertahankan bagian interaktif seperti keranjang sebagai komponen",
                    "     React di dalam halaman itu. Ini pola islands, dan framework seperti",
                    "     Astro atau Next.js bisa memakai ulang komponen React yang sudah",
                    "     ada.",
                ],
            },
        ],
    },
    {
        "title": "7. MERN dari Dekat: Satu Bahasa dari Database ke Browser",
        "sections": [
            {
                "body": [
                    "MERN adalah stack yang seluruhnya memakai JavaScript: MongoDB untuk",
                    "data, Express untuk server HTTP, React untuk tampilan, dan Node.js",
                    "sebagai runtime, yaitu program yang menjalankan JavaScript di luar",
                    "browser. Karena bahasanya satu, orang yang baru lulus kurikulum",
                    "JavaScript bisa mengerjakan frontend dan backend sekaligus.",
                    "",
                    "Datanya juga mengalir dalam satu bentuk dari ujung ke ujung, yaitu JSON.",
                    "Dokumen di MongoDB mirip objek JSON, Express mengirimnya sebagai JSON,",
                    "dan React menerimanya sebagai objek JavaScript biasa.",
                    "",
                    "Survei Stack Overflow 2026 mencatat Node.js dipakai 46% responden, React",
                    "42%, MongoDB 19,0%, dan Express 16%. Express, React, dan Node.js",
                    "berlisensi MIT. MongoDB Community Server memakai lisensi SSPL-1.0, yang",
                    "nggak diakui OSI sebagai lisensi open source. Halaman resmi MongoDB",
                    "sendiri menyebut stack ini varian dari stack berbasis Angular, yang",
                    "dibahas di materi berikutnya.",
                ],
            },
            {
                "heading": "Peran tiap huruf",
                "body": [
                    "  - MongoDB: database dokumen. Data disimpan sebagai dokumen mirip JSON",
                    "    (formatnya BSON) di dalam koleksi. Dokumen di satu koleksi nggak",
                    "    wajib punya field yang sama persis.",
                    "  - Express: framework web kecil di atas Node.js. Tugasnya memetakan",
                    "    rute ke fungsi dan menyusun middleware, yaitu fungsi yang dijalankan",
                    "    berantai sebelum rute, misalnya untuk mencatat log atau mengecek",
                    "    login.",
                    "  - React: pustaka untuk membangun tampilan dari komponen. Kodenya",
                    "    berjalan di browser. Proyek React biasanya dibuat dan dijalankan",
                    "    dengan Vite, alat build yang memaketkan berkas JavaScript.",
                    "  - Node.js: runtime yang menjalankan Express. Node.js juga yang",
                    "    menjalankan Vite dan npm di komputermu.",
                    "",
                    "Hampir semua proyek di stack ini memakai Mongoose, pustaka yang",
                    "menambahkan skema dan validasi di atas MongoDB. Kode server untuk daftar",
                    "produk kira-kira begini:",
                ],
            },
            {
                "heading": "server.js: Express dan Mongoose",
                "bahasa": "javascript",
                "code": """import express from 'express';
import mongoose from 'mongoose';

const Produk = mongoose.model('Produk', new mongoose.Schema({
  nama: { type: String, required: true },
  harga: { type: Number, min: 0 },
}));

const app = express();
app.use(express.json());

app.get('/api/produk', async (req, res) => {
  const daftar = await Produk.find().sort({ harga: 1 });
  res.json(daftar);
});

await mongoose.connect(process.env.MONGODB_URI);
app.listen(3000);""",
            },
            {
                "body": [
                    "Skema Mongoose menetapkan bahwa nama wajib ada dan harga nggak boleh",
                    "negatif. express.json() adalah middleware yang mengurai body request",
                    "berformat JSON. Rute GET /api/produk mengambil semua dokumen urut harga,",
                    "lalu res.json() mengirimnya sebagai JSON.",
                    "",
                    "Alamat database diambil dari variabel lingkungan MONGODB_URI, jadi nggak",
                    "tertulis di kode. Karena kode ini memakai import, package.json-nya perlu",
                    "berisi \"type\": \"module\". Di sisi browser, komponen React yang membaca",
                    "data itu begini:",
                ],
            },
            {
                "heading": "DaftarProduk.jsx",
                "bahasa": "jsx",
                "code": """import { useEffect, useState } from 'react';

export default function DaftarProduk() {
  const [produk, setProduk] = useState([]);

  useEffect(() => {
    fetch('/api/produk')
      .then((r) => r.json())
      .then(setProduk);
  }, []);

  return (
    <ul>
      {produk.map((p) => (
        <li key={p._id}>{p.nama}: Rp{p.harga}</li>
      ))}
    </ul>
  );
}""",
            },
            {
                "body": [
                    "useState menyimpan daftar produk, useEffect menjalankan fetch sekali",
                    "saat komponen muncul, dan r.json() mengubah teks response jadi objek.",
                    "Atribut key memakai _id, field pengenal yang dibuat MongoDB untuk setiap",
                    "dokumen.",
                    "",
                    "Saat pengembangan, Vite berjalan di port 5173 dan Express di port 3000.",
                    "Supaya fetch('/api/produk') sampai ke Express, Vite diatur meneruskan",
                    "alamat /api ke port 3000:",
                ],
            },
            {
                "heading": "vite.config.js",
                "bahasa": "javascript",
                "code": """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: { '/api': 'http://localhost:3000' },
  },
});""",
            },
            {
                "heading": "Satu data, empat tempat",
                "body": [
                    "Program di bawah ini jalan di Node.js tanpa paket apa pun. Dia meniru",
                    "perjalanan daftar produk tadi: dari koleksi, lewat rute, menyeberang",
                    "jaringan sebagai teks, lalu dirender.",
                ],
            },
            {
                "heading": "Meniru alur data JSON",
                "bahasa": "javascript",
                "code": """// Perjalanan satu daftar produk, tanpa server dan database sungguhan.

// 1. "MongoDB": koleksi berisi dokumen
const koleksiProduk = [
  { _id: 'a1', nama: 'Pensil 2B', harga: 3500 },
  { _id: 'a2', nama: 'Buku tulis', harga: 5000 },
  { _id: 'a3', nama: 'Penghapus', harga: 2000 },
];

// 2. "Express": rute GET /api/produk mengirim JSON urut harga
function getProduk() {
  const urut = [...koleksiProduk].sort((a, b) => a.harga - b.harga);
  return JSON.stringify(urut);
}

// 3. Yang lewat jaringan cuma teks
const bodyResponse = getProduk();
console.log('dikirim:', typeof bodyResponse, bodyResponse.length, 'karakter');

// 4. "React": teks diurai lagi jadi objek, lalu dirender
const produk = JSON.parse(bodyResponse);
for (const p of produk) {
  console.log(`<li key="${p._id}">${p.nama}: Rp${p.harga}</li>`);
}
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  dikirim: string 137 karakter",
                    "  <li key=\"a3\">Penghapus: Rp2000</li>",
                    "  <li key=\"a1\">Pensil 2B: Rp3500</li>",
                    "  <li key=\"a2\">Buku tulis: Rp5000</li>",
                    "",
                    "Yang lewat jaringan cuma teks. Express mengubah objek jadi teks dengan",
                    "JSON.stringify (res.json melakukannya untukmu), lalu browser mengubahnya",
                    "balik dengan JSON.parse (r.json() di kode React). Bentuk objeknya sama",
                    "di kedua ujung, termasuk field _id buatan MongoDB.",
                ],
            },
            {
                "heading": "Kapan MongoDB kurang cocok",
                "body": [
                    "Kelemahan stack ini justru di huruf pertamanya. MongoDB nyaman untuk",
                    "data yang bentuknya bebas dan dibaca utuh, misalnya profil pengguna, isi",
                    "artikel, atau log. Untuk data yang saling terkait erat, seperti pesanan,",
                    "stok, dan pembayaran, kamu bakal sering menggabungkan beberapa koleksi.",
                    "Di database relasional itu tinggal JOIN. Di MongoDB kamu memakai tahap",
                    "$lookup atau menulis penggabungannya sendiri di kode.",
                    "",
                    "Pergeseran ini terlihat di survei. PostgreSQL naik dari 48,7% di Survei",
                    "Stack Overflow 2024 jadi 57,9% di 2026, sementara MongoDB turun dari",
                    "24,8% jadi 19,0%. Banyak proyek JavaScript baru memakai PostgreSQL, yang",
                    "dibahas di materi berikutnya.",
                ],
            },
            {
                "heading": "Menyiapkan proyek",
                "bahasa": "terminal",
                "code": """# frontend: proyek React baru dengan Vite
npm create vite@latest toko-web -- --template react

# backend: folder terpisah berisi Express dan Mongoose
mkdir toko-api && cd toko-api
npm init -y
npm pkg set type=module
npm install express mongoose""",
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: menaruh rahasia di kode React. Semua kode frontend ikut",
                    "terkirim ke browser dan bisa dibaca siapa pun lewat DevTools. Alamat",
                    "database, sandi, dan kunci API cuma boleh ada di server, misalnya di",
                    "variabel lingkungan seperti MONGODB_URI.",
                    "",
                    "Kesalahan lain: lupa bahwa React dan Express jalan di dua port berbeda",
                    "saat pengembangan. Tanpa proxy Vite atau pengaturan CORS di Express,",
                    "browser menolak request dari port 5173 ke port 3000.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Stack ini paling sering muncul di bootcamp dan portofolio pemula:",
                    "aplikasi daftar tugas, media sosial sederhana, atau toko online dengan",
                    "React di depan dan API Express di belakang. Repositori contoh bernama",
                    "mern-app atau mern-stack gampang ditemukan di GitHub.",
                    "",
                    "Kasus kecil: toko online buatanmu menyimpan pesanan di koleksi orders,",
                    "berisi id pengguna dan daftar id produk. Halaman riwayat pesanan butuh",
                    "nama pengguna dan nama produk, dan halamannya lambat karena satu pesanan",
                    "memicu banyak query.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung dulu query-nya. Kalau tiap pesanan memicu satu query",
                    "     pengguna dan satu query per produk, sepuluh pesanan bisa jadi",
                    "     puluhan query.",
                    "  2. Untuk data yang memang harus dibekukan, simpan salinannya di",
                    "     dokumen pesanan, misalnya nama dan harga produk saat dibeli. Harga",
                    "     di pesanan seharusnya harga saat transaksi, jadi salinan ini justru",
                    "     benar.",
                    "  3. Kalau penggabungan tetap dibutuhkan, pakai satu agregasi $lookup di",
                    "     MongoDB:",
                    "      db.orders.aggregate([",
                    "        { $lookup: { from: \"users\", localField: \"userId\",",
                    "                     foreignField: \"_id\", as: \"pengguna\" } }",
                    "      ])",
                    "  4. Kalau hampir semua halaman butuh penggabungan seperti ini, itu",
                    "     tanda datamu relasional. Pertimbangkan PostgreSQL untuk proyek",
                    "     berikutnya, seperti varian di materi sesudah ini.",
                ],
            },
        ],
    },
    {
        "title": "8. MEAN, MEVN, dan PERN: Varian Stack JavaScript",
        "sections": [
            {
                "body": [
                    "Kerangka stack JavaScript dari materi sebelumnya bisa diubah dengan",
                    "mengganti satu huruf. Sisanya tetap: Node.js sebagai runtime dan Express",
                    "sebagai server HTTP. Tiga varian yang paling sering disebut punya nama",
                    "sendiri, dan tabel di bawah merangkum bedanya.",
                ],
            },
            {
                "heading": "Empat varian dalam satu tabel",
                "bahasa": "teks",
                "code": """Stack  Database    Server             Tampilan  Cocok untuk
-----  ----------  -----------------  --------  -------------------------
MERN   MongoDB     Express + Node.js  React     data bebas bentuk
MEAN   MongoDB     Express + Node.js  Angular   aplikasi bisnis, tim besar
MEVN   MongoDB     Express + Node.js  Vue       tim yang ingin kurva landai
PERN   PostgreSQL  Express + Node.js  React     data relasional""",
            },
            {
                "heading": "MEAN dan jebakan AngularJS",
                "body": [
                    "Varian dengan huruf A memakai Angular di lapisan tampilan. Angular",
                    "adalah framework lengkap buatan Google. Router, pengelola formulir, HTTP",
                    "client, dan dependency injection sudah termasuk, dan kodenya ditulis",
                    "dengan TypeScript. Strukturnya yang tegas cocok untuk tim besar yang",
                    "ingin semua orang menulis kode dengan cara sama. Halaman tutorial",
                    "angular.dev per Oktober 2026 menyebut Angular 22, dan survei 2026",
                    "mencatat Angular dipakai 16% responden.",
                    "",
                    "Jebakan: Angular dan AngularJS adalah dua framework berbeda.",
                    "AngularJS (versi 1.x) adalah generasi lama yang dukungannya berakhir",
                    "di akhir 2021. Angular (versi 2 ke atas) ditulis ulang dari nol.",
                    "Versi awal stack MEAN memakai AngularJS, jadi tutorial lama sering",
                    "sudah nggak berlaku. Survei 2026 masih mencatat AngularJS dipakai 6%",
                    "responden, kebanyakan untuk merawat aplikasi lama. Jangan memilihnya",
                    "untuk proyek baru.",
                ],
            },
            {
                "heading": "MEVN: Vue di lapisan tampilan",
                "body": [
                    "Varian dengan huruf V memakai Vue.js. Vue dikenal dengan kurva belajar",
                    "yang landai: satu komponen bisa ditulis dalam satu berkas .vue berisi",
                    "template, skrip, dan gaya. Survei 2026 mencatat Vue dipakai 17%",
                    "responden. Pasangannya biasanya Pinia untuk menyimpan state, Vue Router",
                    "untuk navigasi, dan Nuxt kalau butuh SSR. Vue juga sering dipasangkan",
                    "dengan Laravel, seperti yang bakal kamu lihat di bab 4.",
                    "",
                    "Komponen daftar produk yang sama, kalau ditulis dengan Vue:",
                ],
            },
            {
                "heading": "DaftarProduk.vue",
                "bahasa": "vue",
                "code": """<script setup>
import { ref, onMounted } from 'vue'

const produk = ref([])

onMounted(async () => {
  const r = await fetch('/api/produk')
  produk.value = await r.json()
})
</script>

<template>
  <ul>
    <li v-for="p in produk" :key="p._id">{{ p.nama }}</li>
  </ul>
</template>""",
            },
            {
                "heading": "PERN: PostgreSQL menggantikan MongoDB",
                "body": [
                    "Varian dengan huruf P di depan mengganti MongoDB dengan PostgreSQL,",
                    "database relasional yang di Survei Stack Overflow 2026 dipakai 57,9%",
                    "responden, tertinggi di kategori database. Lisensinya PostgreSQL License",
                    "yang longgar, mirip BSD dan MIT. Datanya berupa tabel dengan relasi, dan",
                    "query-nya SQL, persis yang kamu pelajari di kurikulum SQL. Nama PERN",
                    "cuma akronim komunitas, tanpa situs resmi.",
                    "",
                    "Di Node.js, PostgreSQL dipanggil lewat pustaka pg (node-postgres) atau",
                    "lewat ORM seperti Prisma dan Drizzle. Supabase, layanan PostgreSQL siap",
                    "pakai, juga sering jadi pasangannya. Rute detail produk dengan pg:",
                ],
            },
            {
                "heading": "Rute Express dengan node-postgres",
                "bahasa": "javascript",
                "code": """import pg from 'pg';

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });

// app dibuat dengan express() seperti di materi sebelumnya
app.get('/api/produk/:id', async (req, res) => {
  const hasil = await pool.query(
    'SELECT id, nama, harga FROM produk WHERE id = $1',
    [req.params.id],
  );
  if (hasil.rows.length === 0) {
    return res.status(404).json({ pesan: 'produk tidak ada' });
  }
  res.json(hasil.rows[0]);
});""",
            },
            {
                "body": [
                    "$1 adalah parameter. Nilainya dikirim terpisah dari teks query, jadi",
                    "isian pengguna nggak pernah dibaca sebagai perintah SQL. Program di",
                    "bawah memakai SQLite untuk menunjukkan apa yang terjadi kalau query",
                    "disusun dengan menyambung string.",
                ],
            },
            {
                "heading": "Menyambung string atau memakai parameter",
                "code": """import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT)")
db.executemany("INSERT INTO produk (nama) VALUES (?)",
               [("Pensil",), ("Buku",), ("Penghapus",)])

masukan = "1 OR 1=1"   # diketik pengguna di kolom pencarian

# salah: teks pengguna ditempel ke query
query = "SELECT nama FROM produk WHERE id = " + masukan
print("disambung :", [b[0] for b in db.execute(query)])

# benar: teks pengguna dikirim sebagai parameter
aman = db.execute("SELECT nama FROM produk WHERE id = ?", (masukan,))
print("parameter :", [b[0] for b in aman])
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  disambung : ['Pensil', 'Buku', 'Penghapus']",
                    "  parameter : []",
                    "",
                    "Query yang disambung menjadi WHERE id = 1 OR 1=1. Karena 1=1 selalu",
                    "benar, semua baris keluar. Dengan parameter, seluruh teks itu dianggap",
                    "satu nilai id yang nggak cocok dengan baris mana pun. Serangan ini",
                    "namanya SQL injection, dan dibahas lebih dalam di kurikulum Keamanan",
                    "Siber. Penanda parameter di SQLite ditulis ?, di pg ditulis $1, $2, dan",
                    "seterusnya. Idenya sama.",
                ],
            },
            {
                "heading": "NestJS sebagai pengganti Express",
                "body": [
                    "Express sengaja kecil dan nggak mengatur struktur folder. Di proyek",
                    "besar, kebebasan itu sering berakhir dengan susunan yang beda di tiap",
                    "tim. NestJS menjawabnya dengan struktur ala Angular: modul, controller,",
                    "service, dependency injection, dan TypeScript. Karena itu NestJS sering",
                    "dipilih tim yang frontend-nya Angular, dan namanya ikut masuk daftar",
                    "framework web di survei 2026.",
                ],
            },
            {
                "heading": "produk.controller.ts",
                "bahasa": "typescript",
                "code": """import { Controller, Get, Param } from '@nestjs/common';
import { ProdukService } from './produk.service';

@Controller('produk')
export class ProdukController {
  constructor(private readonly produkService: ProdukService) {}

  @Get(':id')
  ambil(@Param('id') id: string) {
    return this.produkService.cari(Number(id));
  }
}""",
            },
            {
                "body": [
                    "Dekorator @Controller dan @Get menggantikan app.get di Express.",
                    "ProdukService disuntikkan lewat konstruktor, pola yang sama dengan",
                    "Spring di bab 4. Di belakang layar, NestJS tetap memakai Express (atau",
                    "Fastify) sebagai server HTTP-nya.",
                ],
            },
            {
                "heading": "Memilih salah satunya",
                "body": [
                    "Cara memilih variannya:",
                    "",
                    "  - Datamu berupa tabel yang saling terkait, seperti pesanan, stok, dan",
                    "    keuangan: pakai PostgreSQL.",
                    "  - Datamu bebas bentuk dan dibaca utuh per dokumen: MongoDB dengan",
                    "    React atau Vue.",
                    "  - Timmu sudah memakai Angular, atau proyeknya aplikasi bisnis besar:",
                    "    Angular, dengan NestJS di server.",
                    "  - Masih bingung: React paling banyak dipakai (42% di survei 2026),",
                    "    jadi lowongan dan tutorialnya paling melimpah.",
                    "",
                    "Di semua varian, Node.js dan Express tetap sama. Kalau kamu sudah bisa",
                    "satu, pindah ke varian lain cuma berarti belajar satu bagian baru.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan web developer sering meminta kombinasi seperti \"React, Node.js,",
                    "PostgreSQL\" atau \"Vue, Express, MongoDB\", tanpa menyebut akronimnya.",
                    "Kalau kamu bisa membaca kombinasi itu sebagai varian stack JavaScript,",
                    "kamu langsung tahu bagian mana yang sudah kamu kuasai.",
                    "",
                    "Kasus kecil: kamu diminta membuat sistem kasir untuk koperasi sekolah,",
                    "berisi barang, stok, transaksi, dan laporan harian. Kakak kelasmu",
                    "menyarankan MongoDB karena tutorialnya banyak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Gambar dulu datanya. Barang punya stok, transaksi berisi beberapa",
                    "     barang, laporan menjumlahkan transaksi per hari. Semuanya saling",
                    "     terkait.",
                    "  2. Data seperti ini cocok dengan tabel dan relasi, jadi pilih",
                    "     PostgreSQL. Stack-nya jadi PostgreSQL, Express, React, dan Node.js.",
                    "  3. Laporan harian cukup satu query dengan JOIN dan GROUP BY. Kolom",
                    "     stok diberi CHECK (stok >= 0), dan pengurangan stok dijalankan di",
                    "     dalam transaksi database, supaya stok nggak pernah minus walau dua",
                    "     kasir menjual bersamaan.",
                    "  4. Bagian lain tetap: Express untuk API dan React untuk layar kasir.",
                    "     Semua query memakai parameter $1, $2, dan seterusnya.",
                ],
            },
        ],
    },
    {
        "title": "9. Dari Jamstack ke Next.js, T3, dan Meta-Framework",
        "sections": [
            {
                "body": [
                    "Pasangan React dan API Express punya beberapa masalah yang makin terasa",
                    "saat aplikasinya membesar. Layar pertama kosong sampai JavaScript",
                    "selesai jalan, mesin pencari kesulitan membaca isinya, dan ada dua",
                    "proyek yang harus di-deploy terpisah. Jawabannya datang bertahap:",
                    "pertama Jamstack, lalu meta-framework.",
                ],
            },
            {
                "heading": "Jamstack: bangun dulu, sajikan dari CDN",
                "body": [
                    "Jamstack dipopulerkan Netlify sekitar 2015 sampai 2016. Singkatan",
                    "awalnya JavaScript, APIs, Markup. Idenya: halaman dibangun lebih dulu",
                    "jadi HTML statis (SSG dari bab 2), disajikan dari CDN, dan data dinamis",
                    "diambil lewat API. Alatnya static site generator seperti Astro, Hugo,",
                    "dan Eleventy, ditambah headless CMS untuk menulis konten dan fungsi",
                    "serverless untuk bagian yang butuh server.",
                    "",
                    "Istilahnya sendiri sedang ditinggalkan. Sejak 2023, Netlify beralih ke",
                    "istilah composable web dan menutup Discord komunitas Jamstack. Situs",
                    "jamstack.org masih ada, dan tekniknya tetap dipakai di mana-mana. Jadi",
                    "yang perlu kamu kuasai konsepnya: pre-rendering, CDN, dan bedanya SSG",
                    "dengan SSR. Program di bawah adalah static site generator paling kecil.",
                ],
            },
            {
                "heading": "Static site generator mini",
                "code": """HALAMAN = {
    "index": ("Beranda", "Selamat datang di Toko Roti Melati."),
    "menu": ("Menu", "Roti sobek, bolu pandan, dan donat gula."),
    "kontak": ("Kontak", "Buka setiap hari pukul 06.00 sampai 20.00."),
}

TEMPLATE = ("<html><head><title>{judul}</title></head>"
            "<body><h1>{judul}</h1><p>{isi}</p></body></html>")

# build: semua HTML disusun sekarang, sekali saja
hasil = {}
for nama, (judul, isi) in HALAMAN.items():
    hasil[f"{nama}.html"] = TEMPLATE.format(judul=judul, isi=isi)

for berkas, html in hasil.items():
    print(f"{berkas:<12} {len(html):>3} byte")
print(f"build selesai: {len(hasil)} berkas siap diunggah ke CDN")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  index.html   119 byte",
                    "  menu.html    118 byte",
                    "  kontak.html  124 byte",
                    "  build selesai: 3 berkas siap diunggah ke CDN",
                    "",
                    "Semua kerja dilakukan sekali waktu build. Saat pengunjung datang, server",
                    "cuma mengirim berkas yang sudah jadi. Kalau jam buka toko berubah, kamu",
                    "ubah datanya lalu build ulang.",
                ],
            },
            {
                "heading": "Meta-framework: pustaka tampilan ditambah server",
                "body": [
                    "Meta-framework adalah framework yang dibangun di atas pustaka tampilan",
                    "seperti React, Vue, atau Svelte. Dia menambahkan bagian yang tadinya",
                    "dirakit sendiri: routing berbasis berkas, SSR dan SSG per halaman,",
                    "pengambilan data di server, dan proses build.",
                    "",
                    "  Next.js    di atas React",
                    "  Nuxt       di atas Vue",
                    "  SvelteKit  di atas Svelte",
                    "  Astro      islands, bisa memakai komponen React, Vue, atau Svelte",
                    "",
                    "Survei Stack Overflow 2026 mencatat Next.js dipakai 21% responden, Astro",
                    "dan SvelteKit masing-masing 6%, dan Nuxt 4%. Fitur meta-framework Remix",
                    "untuk React sudah dilebur ke React Router versi 7.",
                ],
            },
            {
                "heading": "Next.js full-stack",
                "body": [
                    "Pola stack yang paling sering terlihat sekarang belum punya akronim.",
                    "Next.js mengurus tampilan sekaligus backend, aplikasinya di-deploy ke",
                    "Vercel, dan datanya di PostgreSQL atau Supabase. Survei 2026 mencatat",
                    "Vercel dipakai 11% responden dan Supabase 8%. Bagian backend-nya datang",
                    "dari tiga fitur Next.js:",
                    "",
                    "  - Server Components: komponen React yang dijalankan di server.",
                    "    Komponen ini boleh langsung membaca database, dan hasilnya dikirim",
                    "    ke browser sebagai HTML.",
                    "  - Server Actions: fungsi bertanda 'use server' yang bisa dipanggil",
                    "    langsung dari formulir. Next.js membuatkan endpoint-nya sendiri.",
                    "  - Route Handlers: berkas route.ts untuk API biasa, misalnya webhook",
                    "    dari layanan pembayaran.",
                ],
            },
            {
                "heading": "Halaman produk dengan Server Component dan Server Action",
                "bahasa": "tsx",
                "code": """// app/produk/page.tsx
import { revalidatePath } from 'next/cache';
import { db } from '@/lib/db';

async function tambahProduk(formData: FormData) {
  'use server';
  await db.produk.create({ data: { nama: String(formData.get('nama')) } });
  revalidatePath('/produk');
}

export default async function HalamanProduk() {
  const produk = await db.produk.findMany({ orderBy: { nama: 'asc' } });
  return (
    <main>
      <ul>
        {produk.map((p) => <li key={p.id}>{p.nama}</li>)}
      </ul>
      <form action={tambahProduk}>
        <input name="nama" required />
        <button>Tambah</button>
      </form>
    </main>
  );
}""",
            },
            {
                "body": [
                    "HalamanProduk berjalan di server, jadi db.produk.findMany() nggak pernah",
                    "terkirim ke browser. Formulir memanggil tambahProduk tanpa fetch dan",
                    "tanpa rute Express. Sesudah data ditambah, revalidatePath menyuruh",
                    "Next.js menyusun ulang halaman /produk. Objek db di sini klien ORM,",
                    "misalnya Prisma.",
                    "",
                    "Jebakan: lupa batas server dan browser. Komponen yang butuh state atau",
                    "klik, seperti tombol keranjang, harus ditandai 'use client' di baris",
                    "pertama berkasnya. Sebaliknya, kode yang memegang rahasia jangan sampai",
                    "diimpor komponen client.",
                    "",
                    "Celah keamanan CVE-2025-29927 di Next.js (Maret 2025) memungkinkan",
                    "pemeriksaan di middleware dilewati dengan satu header buatan.",
                    "Pelajarannya: cek hak akses juga di dekat data, di Server Component atau",
                    "Server Action itu sendiri, jangan cuma di middleware.",
                ],
            },
            {
                "heading": "T3 Stack: tipe yang tersambung sampai ke layar",
                "body": [
                    "T3 Stack dibuat Theo Browne (t3.gg). Intinya Next.js dan TypeScript,",
                    "ditambah Tailwind CSS, tRPC, Prisma atau Drizzle untuk database, dan",
                    "NextAuth.js (sekarang bernama Auth.js) untuk login. Semuanya dipasang",
                    "lewat satu perintah: npm create t3-app@latest.",
                    "",
                    "Yang ditekankan adalah keamanan tipe. Kalau kolom di database berganti",
                    "nama, TypeScript langsung menandai setiap baris kode frontend yang masih",
                    "memakai nama lama, sebelum aplikasinya dijalankan. tRPC yang",
                    "menyambungkannya: fungsi di server bisa dipanggil dari browser seperti",
                    "fungsi biasa, lengkap dengan tipenya, tanpa menulis REST API.",
                ],
            },
            {
                "heading": "Router tRPC",
                "bahasa": "typescript",
                "code": """// src/server/api/routers/produk.ts
import { z } from 'zod';
import { createTRPCRouter, publicProcedure } from '~/server/api/trpc';

export const produkRouter = createTRPCRouter({
  ambil: publicProcedure
    .input(z.object({ id: z.number() }))
    .query(({ ctx, input }) => {
      return ctx.db.produk.findUnique({ where: { id: input.id } });
    }),
});""",
            },
            {
                "body": [
                    "Di komponen React, router ini dipanggil dengan",
                    "api.produk.ambil.useQuery({ id: 7 }). Kalau kamu mengirim { id: \"7\" },",
                    "compiler TypeScript menolaknya, karena input sudah dinyatakan angka",
                    "lewat Zod.",
                    "",
                    "Paket create-t3-app berlisensi MIT. Versi terbarunya saat materi ini",
                    "ditulis (Oktober 2026) adalah 7.40.0, rilis November 2025. Rilisnya",
                    "melambat, tapi template-nya masih dipakai. Template ini sengaja dibuat",
                    "ramping: state management dan kebutuhan lain ditambahkan sendiri.",
                ],
            },
            {
                "heading": "RedwoodJS dan pelajaran memilih framework kecil",
                "body": [
                    "RedwoodJS adalah framework full-stack yang merangkai React, GraphQL, dan",
                    "Prisma dalam satu proyek dengan struktur siap pakai. Menurut pengumuman",
                    "komunitas pada April 2025, framework itu diganti nama jadi",
                    "RedwoodGraphQL dan masuk mode pemeliharaan. Tim intinya pindah ke",
                    "RedwoodSDK, framework lain berbasis React Server Components khusus",
                    "Cloudflare. Sebagian komunitas melanjutkan versi lamanya lewat fork",
                    "bernama CedarJS.",
                    "",
                    "Pelajarannya berlaku untuk framework kecil mana pun: arah proyeknya bisa",
                    "berubah dalam setahun. Kalau konsep dasarnya kamu kuasai, seperti SSR,",
                    "routing, ORM, dan API, pindah ke framework lain jadi jauh lebih ringan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak situs perusahaan, toko online, dan dasbor SaaS (perangkat lunak",
                    "yang dijual sebagai layanan langganan) dibangun dengan Next.js. Situs",
                    "dokumentasi dan blog teknik banyak yang memakai Astro atau static site",
                    "generator lain. Kamu bisa menebaknya dari View Page Source: Next.js",
                    "biasanya meninggalkan jejak berupa folder /_next/ di alamat berkas",
                    "JavaScript-nya.",
                    "",
                    "Kasus kecil: sebuah UMKM punya toko online lama berupa React SPA di",
                    "Netlify dan API Express di server terpisah. Mereka ingin halaman",
                    "produknya muncul di pencarian dan cuma mau mengurus satu proyek.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan halaman ke Next.js. Komponen React yang sudah ada bisa",
                    "     dipakai ulang hampir apa adanya.",
                    "  2. Jadikan halaman daftar dan detail produk Server Component yang",
                    "     membaca database langsung. Hasilnya HTML lengkap yang terbaca mesin",
                    "     pencari.",
                    "  3. Pindahkan rute Express yang mengubah data, seperti checkout, jadi",
                    "     Server Action. Webhook dari layanan pembayaran dipindah jadi Route",
                    "     Handler.",
                    "  4. Beri 'use client' pada komponen yang butuh klik, seperti tombol",
                    "     keranjang. Hak akses dicek di Server Action-nya sendiri, jangan",
                    "     cuma di middleware.",
                ],
            },
        ],
    },
    {
        "title": "10. Stack Laravel: TALL dan Inertia",
        "sections": [
            {
                "body": [
                    "Laravel adalah framework PHP untuk aplikasi web, lengkap dengan routing,",
                    "ORM bernama Eloquent, antrean, dan autentikasi. Survei Stack Overflow",
                    "2026 mencatat Laravel dipakai 8% responden, dan dokumentasi resminya",
                    "saat materi ini ditulis (Oktober 2026) untuk Laravel 13.x.",
                    "",
                    "Begitu aplikasinya butuh tampilan interaktif, misalnya keranjang yang",
                    "berubah tanpa memuat ulang halaman, tim Laravel biasanya memilih satu",
                    "dari dua jalan. Jalan pertama, interaksinya ditulis dengan PHP lewat",
                    "Livewire. Jalan kedua, halamannya ditulis sebagai komponen React, Vue,",
                    "atau Svelte lewat Inertia, sementara rute dan controller tetap di",
                    "Laravel.",
                    "",
                    "Dua jalan itu sama-sama resmi. Perintah laravel new menawarkan empat",
                    "starter kit: React, Svelte, dan Vue yang dibangun dengan Inertia 3,",
                    "serta Livewire yang dibangun dengan Livewire 4 dan pustaka komponen Flux",
                    "UI. Semuanya memakai Tailwind dan Laravel Fortify untuk login.",
                ],
            },
            {
                "heading": "Membuat proyek Laravel",
                "bahasa": "terminal",
                "code": """# pemasang Laravel, sekali saja
composer global require laravel/installer

# proyek baru; pemasang menanyakan starter kit yang dipakai
laravel new toko
cd toko
npm install && npm run build
composer run dev""",
            },
            {
                "heading": "TALL: Tailwind, Alpine, Laravel, Livewire",
                "body": [
                    "Gabungan jalan pertama punya nama, TALL:",
                    "",
                    "  - Tailwind CSS: kelas-kelas kecil untuk gaya, ditulis langsung di",
                    "    HTML.",
                    "  - Alpine.js: JavaScript kecil untuk interaksi yang cukup terjadi di",
                    "    browser, ditulis lewat atribut seperti x-data dan x-show.",
                    "  - Laravel: framework di server.",
                    "  - Livewire: komponen yang logikanya kelas PHP. Interaksinya diproses",
                    "    di server, dan halamannya diperbarui tanpa memuat ulang.",
                    "",
                    "Situs lama tallstack.dev sekarang dialihkan ke livewire.laravel.com.",
                    "Versi Livewire terbaru saat materi ini ditulis 4.4.7 (28 September",
                    "2026), cabang 3.x masih dirawat, dan Alpine.js 3.17.4. Keempatnya",
                    "berlisensi MIT. Komponen Livewire terdiri dari kelas PHP dan view Blade:",
                ],
            },
            {
                "heading": "Kelas komponen Livewire",
                "bahasa": "php",
                "code": "// app/Livewire/Keranjang.php\nnamespace App\\Livewire;\n\nuse Livewire\\Component;\n\nclass Keranjang extends Component\n{\n    public int $jumlah = 1;\n\n    public function tambah(): void\n    {\n        $this->jumlah++;\n    }\n\n    public function render()\n    {\n        return view('livewire.keranjang');\n    }\n}",
            },
            {
                "heading": "View komponennya",
                "bahasa": "blade",
                "code": """{{-- resources/views/livewire/keranjang.blade.php --}}
<div>
    <button wire:click="tambah">+</button>
    <span>{{ $jumlah }} barang</span>

    <div x-data="{ buka: false }">
        <button @click="buka = !buka">Detail ongkir</button>
        <p x-show="buka">Ongkir dihitung saat checkout.</p>
    </div>
</div>""",
            },
            {
                "body": [
                    "Waktu tombol + diklik, Livewire mengirim request ke server berisi",
                    "keadaan komponen (nilai $jumlah) dan nama aksinya. Server menjalankan",
                    "tambah(), merender ulang Blade-nya, lalu mengirim HTML baru. Livewire di",
                    "browser menyunting halaman seperlunya tanpa memuat ulang.",
                    "",
                    "Bagian x-data milik Alpine berjalan murni di browser. Membuka dan",
                    "menutup detail ongkir nggak perlu ke server sama sekali. Pembagiannya:",
                    "yang butuh data atau aturan pakai Livewire, yang cuma urusan tampilan",
                    "pakai Alpine.",
                    "",
                    "Akibatnya, setiap aksi Livewire berarti satu perjalanan ke server. Di",
                    "jaringan lambat, tombolnya terasa telat. Untuk panel admin dan aplikasi",
                    "bisnis, hal ini biasanya nggak jadi masalah.",
                ],
            },
            {
                "heading": "Inertia: halaman React tanpa API terpisah",
                "body": [
                    "Inertia menyebut dirinya penghubung. Rute, controller, validasi, dan",
                    "autentikasi tetap di Laravel. Yang diganti cuma lapisan view: controller",
                    "mengirim nama komponen halaman beserta datanya (props), lalu React, Vue,",
                    "atau Svelte yang menggambarnya. Tim nggak perlu membuat REST API dan",
                    "nggak perlu mengurus dua proyek.",
                    "",
                    "Kombinasinya punya nama: VILT untuk Vue, Inertia, Laravel, Tailwind, dan",
                    "RILT untuk versi React. Versi Inertia terbaru saat materi ini ditulis",
                    "3.9.1 (9 Oktober 2026), dan cabang 2.x masih dirawat. Inertia juga",
                    "dipakai di luar Laravel, misalnya dengan Rails, Django, dan Phoenix,",
                    "lewat adapter masing-masing.",
                ],
            },
            {
                "heading": "Controller yang merender halaman Inertia",
                "bahasa": "php",
                "code": "// app/Http/Controllers/ProdukController.php\nuse Inertia\\Inertia;\n\nclass ProdukController extends Controller\n{\n    public function index()\n    {\n        return Inertia::render('Produk/Index', [\n            'produk' => Produk::orderBy('nama')->get(['id', 'nama', 'harga']),\n        ]);\n    }\n}",
            },
            {
                "heading": "Halaman React yang menerima props",
                "bahasa": "tsx",
                "code": """// resources/js/pages/Produk/Index.tsx
type Produk = { id: number; nama: string; harga: number };

export default function Index({ produk }: { produk: Produk[] }) {
  return (
    <ul>
      {produk.map((p) => (
        <li key={p.id}>
          {p.nama}: Rp{p.harga}
        </li>
      ))}
    </ul>
  );
}""",
            },
            {
                "body": [
                    "Di kunjungan pertama, Laravel mengirim HTML utuh. Di dalamnya ada tag",
                    "<script type=\"application/json\"> berisi page object: nama komponen,",
                    "props, url, dan version. Klik tautan berikutnya dikirim Inertia lewat",
                    "JavaScript dengan header X-Inertia: true, dan Laravel menjawab cuma",
                    "dengan page object dalam bentuk JSON. Halaman lalu diganti komponennya",
                    "tanpa memuat ulang.",
                    "",
                    "Program di bawah meniru dua jenis jawaban itu.",
                ],
            },
            {
                "heading": "Dua jenis jawaban Inertia",
                "code": "import json\n\n\ndef page_object():\n    return {\"component\": \"Produk/Index\",\n            \"props\": {\"produk\": [{\"id\": 1, \"nama\": \"Pensil\"}]},\n            \"url\": \"/produk\",\n            \"version\": \"a1b2\"}\n\n\ndef laravel(header):\n    page = json.dumps(page_object())\n    if header.get(\"X-Inertia\") == \"true\":\n        return \"application/json\", page\n    # kunjungan pertama: HTML utuh, page object di dalam tag script\n    aman = page.replace(\"/\", \"\\\\/\")\n    html = ('<div id=\"app\"></div>'\n            f'<script data-page=\"app\" type=\"application/json\">{aman}</script>')\n    return \"text/html\", html\n\n\nfor nama, header in [(\"kunjungan pertama\", {}),\n                     (\"klik tautan berikutnya\", {\"X-Inertia\": \"true\"})]:\n    jenis, isi = laravel(header)\n    print(f\"{nama}: {jenis}, {len(isi)} byte\")\n    if jenis == \"application/json\":\n        page = json.loads(isi)\n        print(f\"  komponen {page['component']}, props {list(page['props'])}\")\n",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  kunjungan pertama: text/html, 197 byte",
                    "  klik tautan berikutnya: application/json, 118 byte",
                    "    komponen Produk/Index, props ['produk']",
                    "",
                    "Tanda / di dalam JSON pada HTML ditulis \\/ supaya teks seperti </script>",
                    "di dalam data nggak menutup tag script lebih awal. Dokumentasi protokol",
                    "Inertia meminta hal yang sama.",
                ],
            },
            {
                "heading": "Livewire atau Inertia?",
                "body": [
                    "  - Timmu kuat di PHP dan nggak mau memelihara build JavaScript yang",
                    "    rumit: Livewire.",
                    "  - Butuh interaksi yang padat di browser, seperti editor atau",
                    "    seret-lepas, atau timmu sudah jago React atau Vue: Inertia.",
                    "  - Butuh panel admin cepat: Filament, kumpulan komponen admin siap",
                    "    pakai yang dibangun di atas Livewire.",
                    "  - Ada aplikasi mobile yang harus memanggil data yang sama: Laravel",
                    "    dengan API terpisah, misalnya memakai Sanctum untuk token, bisa",
                    "    lebih cocok daripada keduanya.",
                    "",
                    "Jebakan: mengira Inertia itu framework UI lalu mencari komponen tombol",
                    "di dalamnya. Inertia cuma protokol penghubung. Komponen tombol datang",
                    "dari React, Vue, atau Svelte, ditambah pustaka seperti shadcn/ui yang",
                    "dipasang starter kit.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Panel admin toko online, sistem informasi sekolah, dan aplikasi SaaS",
                    "kecil banyak yang dibangun dengan Laravel. Starter kit resmi dan",
                    "Filament membuat aplikasi CRUD lengkap dengan login bisa dikerjakan satu",
                    "atau dua orang.",
                    "",
                    "Kasus kecil: kamu membuat aplikasi peminjaman alat lab sekolah dengan",
                    "Laravel. Daftar alat butuh tombol pinjam yang langsung mengurangi stok",
                    "tanpa memuat ulang halaman. Kamu satu-satunya programmer, kuat di PHP,",
                    "dan baru sedikit belajar JavaScript.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan jalannya dari kemampuan tim. Kamu kuat di PHP,",
                    "     interaksinya sederhana, dan belum ada aplikasi mobile. Livewire",
                    "     cukup.",
                    "  2. Buat proyek dengan laravel new lalu pilih starter kit Livewire.",
                    "     Login dan tata letaknya sudah jadi.",
                    "  3. Buat komponen DaftarAlat dengan method pinjam($id) yang mengurangi",
                    "     stok lewat model. Aturan stok tetap di model, misalnya alat dengan",
                    "     stok 0 nggak bisa dipinjam.",
                    "  4. Di view-nya, pasang aksi di tombol:",
                    "      <button wire:click=\"pinjam({{ $alat->id }})\">Pinjam</button>",
                    "     Livewire mengirim aksinya ke server dan memperbarui baris itu.",
                    "     Kalau nanti butuh aplikasi mobile, baru pertimbangkan API terpisah.",
                ],
            },
        ],
    },
    {
        "title": "11. Stack Python: Django, FastAPI, dan React",
        "sections": [
            {
                "body": [
                    "Python dipakai 58% responden Survei Stack Overflow 2026. Di backend web,",
                    "dua framework Python yang paling sering dipasangkan dengan React adalah",
                    "Django dan FastAPI. Django dipakai 11% responden. FastAPI naik dari 9,9%",
                    "di survei 2024 jadi 14,8% di 2025, lalu 19% di 2026.",
                    "",
                    "Keduanya sama-sama bisa membuat API yang dibaca React. Bedanya ada di",
                    "apa yang dibawa sejak awal.",
                ],
            },
            {
                "heading": "Django + React lewat Django REST Framework",
                "body": [
                    "Django adalah framework yang \"baterainya sudah termasuk\": ORM, migrasi",
                    "database, autentikasi, formulir, dan panel admin otomatis untuk setiap",
                    "model. Lisensinya BSD-3-Clause.",
                    "",
                    "Untuk membuka API, Django dipasangkan dengan Django REST Framework",
                    "(DRF). DRF menambahkan serializer, yaitu pengubah objek model jadi JSON",
                    "dan sebaliknya sambil memvalidasi isinya. DRF juga punya viewset dan",
                    "router yang membuatkan rute CRUD. Versi terbarunya saat materi ini",
                    "ditulis 3.18.3 (6 Oktober 2026).",
                ],
            },
            {
                "heading": "Serializer, viewset, dan router DRF",
                "code": """# toko/api.py
from rest_framework import routers, serializers, viewsets

from toko.models import Produk


class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ["id", "nama", "harga"]


class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.order_by("nama")
    serializer_class = ProdukSerializer


router = routers.DefaultRouter()
router.register("produk", ProdukViewSet)
# di urls.py: path("api/", include(router.urls))""",
            },
            {
                "body": [
                    "Kode sependek itu sudah membuat GET dan POST di /api/produk/, ditambah",
                    "GET, PUT, PATCH, dan DELETE di /api/produk/1/. React di folder terpisah",
                    "memanggilnya dengan fetch, seperti di bab 3.",
                    "",
                    "Jebakan: CORS dan CSRF. Kalau React dilayani dari domain atau port lain,",
                    "browser menolak request ke Django sampai server mengizinkan asal itu,",
                    "biasanya lewat paket django-cors-headers. Kalau login memakai sesi",
                    "Django, request POST juga butuh token CSRF.",
                ],
            },
            {
                "heading": "FastAPI + React",
                "body": [
                    "FastAPI membaca petunjuk tipe (type hints) Python. Dari situ dia",
                    "mengerjakan tiga hal: mengubah parameter ke tipe yang benar, menolak",
                    "data yang salah dengan kode 422, dan membuat dokumentasi OpenAPI",
                    "otomatis di alamat /docs. FastAPI dijalankan oleh server seperti",
                    "Uvicorn, mendukung async, dan berlisensi MIT.",
                    "",
                    "Organisasi FastAPI merawat Full Stack FastAPI Template. Isinya backend",
                    "FastAPI dengan SQLModel dan PostgreSQL, frontend React dengan TypeScript",
                    "dan Vite, Tailwind dan shadcn/ui, tes Playwright, dan Docker Compose",
                    "dengan Traefik sebagai reverse proxy. Template ini nggak diberi nomor",
                    "versi rilis.",
                ],
            },
            {
                "heading": "Endpoint FastAPI",
                "code": """from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Produk(BaseModel):
    id: int
    nama: str
    harga: int


DATA = {1: Produk(id=1, nama="Pensil", harga=3000)}


@app.get("/produk/{produk_id}")
def ambil(produk_id: int) -> Produk:
    if produk_id not in DATA:
        raise HTTPException(status_code=404, detail="Produk tidak ada")
    return DATA[produk_id]""",
            },
            {
                "body": [
                    "Pydantic memeriksa bahwa Produk berisi id, nama, dan harga dengan tipe",
                    "yang benar. Anotasi produk_id: int membuat FastAPI mengubah teks dari",
                    "URL jadi angka, atau menolaknya.",
                    "",
                    "Jebakan: menulis async def lalu memanggil pustaka database yang blocking",
                    "di dalamnya. Selama query berjalan, server ikut menunggu, jadi",
                    "aplikasinya malah lebih lambat daripada def biasa. Pakai async def hanya",
                    "kalau pustakanya juga async. Kalau ragu, def biasa aman, karena FastAPI",
                    "menjalankannya di thread terpisah.",
                ],
            },
            {
                "heading": "Cara FastAPI memakai petunjuk tipe",
                "body": [
                    "Kemampuan membaca tipe itu datang dari pustaka standar Python. Program",
                    "di bawah meniru caranya dengan modul inspect: dekorator mendaftarkan",
                    "fungsi ke tabel rute, lalu anotasi parameter dipakai untuk mengubah teks",
                    "dari URL.",
                ],
            },
            {
                "heading": "Dekorator rute dan anotasi tipe",
                "code": """import inspect

RUTE = {}


def get(pola):
    def daftar(fungsi):
        RUTE[pola] = fungsi
        return fungsi
    return daftar


@get("/produk/{produk_id}")
def ambil(produk_id: int):
    return {"id": produk_id, "nama": "Pensil"}


def panggil(pola, nilai_dari_url):
    fungsi = RUTE[pola]
    argumen = {}
    for nama, p in inspect.signature(fungsi).parameters.items():
        try:
            argumen[nama] = p.annotation(nilai_dari_url)
        except ValueError:
            return 422, f"{nama} harus {p.annotation.__name__}"
    return 200, fungsi(**argumen)


print(panggil("/produk/{produk_id}", "7"))
print(panggil("/produk/{produk_id}", "abc"))
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  (200, {'id': 7, 'nama': 'Pensil'})",
                    "  (422, 'produk_id harus int')",
                    "",
                    "Nilai dari URL selalu berupa teks. Anotasi int yang mengubahnya jadi",
                    "angka atau menolaknya. FastAPI asli melakukan hal serupa dengan bantuan",
                    "Pydantic, dan sekalian menulis dokumentasi /docs dari informasi yang",
                    "sama.",
                ],
            },
            {
                "heading": "Django + htmx dan Django Ninja",
                "body": [
                    "Nggak semua proyek Django butuh React. Django + htmx mempertahankan",
                    "template Django dan menambah interaksi lewat atribut HTML, dengan server",
                    "mengirim potongan HTML. Pola ini dibahas di materi HTML over the wire di",
                    "akhir bab ini.",
                    "",
                    "Django Ninja menawarkan gaya FastAPI di atas Django. Endpoint ditulis",
                    "sebagai fungsi dengan petunjuk tipe dan skema Pydantic, dokumentasi",
                    "OpenAPI dibuat otomatis, sementara ORM dan admin Django tetap dipakai.",
                    "Ninja sering dipilih sebagai pengganti DRF yang lebih ringkas.",
                ],
            },
            {
                "heading": "Django atau FastAPI?",
                "body": [
                    "  - Butuh panel admin, login, dan banyak tabel sejak hari pertama:",
                    "    Django.",
                    "  - Membuat API murni, misalnya untuk aplikasi mobile atau layanan AI",
                    "    yang dipanggil aplikasi lain: FastAPI.",
                    "  - Timnya tim data atau AI yang sudah menulis Python: FastAPI biasanya",
                    "    paling cepat menyambungkan model ke web.",
                    "  - Butuh admin Django sekaligus API bergaya FastAPI: Django Ninja.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Django banyak dipakai untuk sistem informasi, portal berita, dan",
                    "aplikasi dengan data yang dikelola lewat panel admin. FastAPI banyak",
                    "dipakai untuk API yang melayani model machine learning, karena tim data",
                    "sudah memakai Python dan halaman /docs bisa langsung dibaca tim",
                    "frontend.",
                    "",
                    "Kasus kecil: timmu punya model Python yang menebak kategori pengaduan",
                    "pelanggan dari teksnya. Tim frontend ingin memanggilnya dari dasbor",
                    "React.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pilih FastAPI. Kebutuhannya satu endpoint API tanpa panel admin,",
                    "     dan modelnya sudah berupa kode Python.",
                    "  2. Tulis skema masukan dengan Pydantic, misalnya kelas Pengaduan",
                    "     berisi teks: str. FastAPI otomatis menolak request tanpa teks",
                    "     dengan kode 422.",
                    "  3. Buat endpoint POST /tebak yang memanggil model lalu mengembalikan",
                    "     kategorinya. Muat modelnya sekali saat server mulai, jangan di",
                    "     setiap request.",
                    "  4. Kirim alamat /docs ke tim frontend. Mereka bisa mencoba",
                    "     endpoint-nya dari browser dan melihat bentuk JSON yang harus",
                    "     dikirim. Kalau dasbor React dilayani dari domain lain, aktifkan",
                    "     CORSMiddleware untuk domain itu.",
                ],
            },
        ],
    },
    {
        "title": "12. Spring Boot dan Angular: Stack Korporat Java",
        "sections": [
            {
                "body": [
                    "Pasangan Spring Boot di backend dan Angular di frontend dikenal sebagai",
                    "stack korporat. Pasangan ini banyak dipakai untuk sistem perbankan,",
                    "asuransi, pemerintahan, ERP, dan aplikasi internal perusahaan besar.",
                    "Survei Stack Overflow 2026 mencatat Java dipakai 27,6% responden,",
                    "Angular 16%, dan Spring Boot 13%.",
                    "",
                    "Alasan organisasi besar memilihnya:",
                    "",
                    "  - Umur panjang. Java punya versi LTS yang didukung bertahun-tahun, dan",
                    "    kode lama umumnya masih bisa dikompilasi di versi baru.",
                    "  - Tipe yang ketat di dua sisi. Java di backend dan TypeScript di",
                    "    Angular menangkap banyak kesalahan sebelum aplikasi dijalankan. Ini",
                    "    penting kalau satu sistem dikerjakan puluhan orang.",
                    "  - Struktur yang seragam. Spring dan Angular sama-sama punya cara baku",
                    "    menyusun kode, termasuk dependency injection, jadi programmer bisa",
                    "    pindah antartim tanpa belajar ulang.",
                    "  - Ekosistem yang matang untuk keamanan, transaksi database, dan",
                    "    penghubung ke sistem lama seperti antrean pesan dan database Oracle.",
                ],
            },
            {
                "heading": "Spring Boot di belakang",
                "body": [
                    "Spring Boot adalah cara cepat memakai Spring, framework Java yang sudah",
                    "ada sejak awal 2000-an. Boot menyediakan konfigurasi otomatis, server",
                    "web yang tertanam di aplikasi, dan paket pemula (starter) seperti",
                    "spring-boot-starter-web. Hasil build-nya satu berkas jar yang langsung",
                    "bisa dijalankan. Lisensinya Apache-2.0.",
                    "",
                    "Inti Spring adalah dependency injection (DI). Kamu nggak membuat objek",
                    "dengan new sendiri. Kamu menyatakan apa yang dibutuhkan sebuah kelas di",
                    "konstruktornya, lalu kontainer Spring yang membuat objeknya dan",
                    "memasangkannya. Latihan di akhir bab ini membangun kontainer seperti itu",
                    "dalam versi mini.",
                ],
            },
            {
                "heading": "Controller REST di Spring Boot",
                "bahasa": "java",
                "code": """package com.toko.produk;

import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/produk")
public class ProdukController {
    private final ProdukService service;

    public ProdukController(ProdukService service) {
        this.service = service;
    }

    @GetMapping
    public List<ProdukDto> semua() {
        return service.semua();
    }
}""",
            },
            {
                "body": [
                    "@RestController menandai kelas yang menjawab request dengan JSON.",
                    "@GetMapping memetakan GET /api/produk ke method semua(). ProdukService",
                    "nggak dibuat di mana pun di kode ini. Spring yang membuatnya lalu",
                    "mengisinya lewat konstruktor. Susunan controller, service, dan",
                    "repository di belakangnya sama dengan yang dibangun di kurikulum Bikin",
                    "Aplikasi.",
                    "",
                    "Jebakan: anotasi seperti @Autowired dan @Transactional terasa seperti",
                    "sihir kalau konsep DI dan proxy belum dipahami. Kalau @Transactional",
                    "seolah nggak berpengaruh, penyebab yang sering muncul adalah method itu",
                    "dipanggil dari dalam kelas yang sama, sehingga proxy Spring nggak ikut",
                    "campur.",
                ],
            },
            {
                "heading": "Angular di depan",
                "body": [
                    "Proyek Angular biasanya dibuat dengan Angular CLI (perintah ng new) dan",
                    "ditulis dengan TypeScript. Versi terbarunya per Oktober 2026 adalah",
                    "Angular 22. Angular sekarang memakai komponen standalone, signal untuk",
                    "menyimpan keadaan, dan sintaks @for di template.",
                ],
            },
            {
                "heading": "Komponen Angular yang memanggil Spring",
                "bahasa": "typescript",
                "code": """import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { toSignal } from '@angular/core/rxjs-interop';

interface Produk {
  id: number;
  nama: string;
}

@Component({
  selector: 'app-daftar-produk',
  template: `
    <ul>
      @for (p of produk(); track p.id) {
        <li>{{ p.nama }}</li>
      }
    </ul>
  `,
})
export class DaftarProduk {
  private http = inject(HttpClient);
  produk = toSignal(this.http.get<Produk[]>('/api/produk'), {
    initialValue: [],
  });
}""",
            },
            {
                "body": [
                    "inject(HttpClient) meminta HttpClient dari sistem DI milik Angular,",
                    "persis seperti Spring menyuntikkan service. toSignal mengubah hasil",
                    "permintaan HTTP jadi signal yang dibaca template lewat produk(). Supaya",
                    "HttpClient tersedia, konfigurasi aplikasinya perlu memanggil",
                    "provideHttpClient().",
                ],
            },
            {
                "heading": "JHipster, Keycloak, dan migrasi database",
                "body": [
                    "JHipster adalah generator yang membuat kerangka proyek Spring Boot dan",
                    "Angular lengkap: login, entitas, tes, dan berkas Docker. Versi",
                    "terbarunya 9.4.0 (18 September 2026), dan sejak 9.3 JHipster hanya",
                    "mendukung Spring Boot 4 dan Angular 22. Selain Angular, JHipster bisa",
                    "menghasilkan frontend React atau Vue, dan bisa membuat arsitektur",
                    "microservices. Lisensinya Apache-2.0.",
                    "",
                    "Keycloak sering dipasang di samping pasangan ini sebagai penyedia",
                    "identitas: satu tempat login (SSO) untuk banyak aplikasi, memakai OAuth",
                    "2.0 dan OpenID Connect. Detailnya di bab 11.",
                    "",
                    "Perubahan struktur database ditulis sebagai migrasi bernomor yang ikut",
                    "tersimpan di Git, memakai Flyway atau Liquibase. JHipster sendiri",
                    "memakai Liquibase. Contoh berkas migrasi Flyway:",
                ],
            },
            {
                "heading": "Migrasi Flyway",
                "bahasa": "postgresql",
                "code": """-- src/main/resources/db/migration/V1__buat_tabel_produk.sql
CREATE TABLE produk (
    id BIGSERIAL PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    harga INTEGER NOT NULL CHECK (harga >= 0)
);""",
            },
            {
                "body": [
                    "Flyway menjalankan berkas V1, V2, dan seterusnya sesuai urutan nomornya,",
                    "lalu mencatat mana yang sudah dijalankan. Database di laptopmu, di",
                    "server uji, dan di produksi jadi punya struktur yang sama.",
                    "",
                    "Kembali ke DI. Program di bawah memperlihatkan gunanya: service yang",
                    "sama dipakai dengan repository sungguhan dan repository palsu untuk tes,",
                    "tanpa mengubah satu baris pun di service.",
                ],
            },
            {
                "heading": "Dependency injection dengan tangan",
                "code": """class RepoMemori:
    def __init__(self):
        self.data = {1: "Pensil", 2: "Buku"}

    def semua(self):
        return [self.data[k] for k in sorted(self.data)]


class RepoPalsu:
    def semua(self):
        return ["(data tes)"]


class ProdukService:
    def __init__(self, repo):       # kebutuhan dinyatakan di konstruktor
        self.repo = repo

    def daftar_huruf_besar(self):
        return [nama.upper() for nama in self.repo.semua()]


# "kontainer" versi tangan: kita sendiri yang memasangkan objeknya
untuk_aplikasi = ProdukService(RepoMemori())
untuk_tes = ProdukService(RepoPalsu())

print("aplikasi:", untuk_aplikasi.daftar_huruf_besar())
print("tes     :", untuk_tes.daftar_huruf_besar())
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  aplikasi: ['PENSIL', 'BUKU']",
                    "  tes     : ['(DATA TES)']",
                    "",
                    "Di Spring, baris pemasangan seperti itu dikerjakan kontainer berdasarkan",
                    "anotasi dan tipe. Di proyek dengan ratusan kelas, di situlah kerja yang",
                    "dihemat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan programmer di bank dan perusahaan besar sering meminta Java",
                    "dengan Spring Boot, ditambah Angular atau React di frontend, dan",
                    "pengalaman dengan Oracle atau PostgreSQL. Kalau kamu PKL di tempat",
                    "seperti itu, kamu kemungkinan diminta membaca kode Spring yang sudah",
                    "berjalan bertahun-tahun.",
                    "",
                    "Kasus kecil: di hari pertama PKL, kamu diminta menambah endpoint GET",
                    "/api/produk/{id} di proyek Spring Boot yang sudah punya ProdukController",
                    "dan ProdukService.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca dulu controller yang ada. @RequestMapping(\"/api/produk\") di",
                    "     atas kelas artinya semua method di dalamnya diawali alamat itu.",
                    "  2. Tambahkan method di service lebih dulu, misalnya cari(Long id) yang",
                    "     memanggil repository dan melempar exception kalau produknya nggak",
                    "     ada. Aturan bisnis tetap di service.",
                    "  3. Tambahkan method di controller:",
                    "      @GetMapping(\"/{id}\")",
                    "      public ProdukDto satu(@PathVariable Long id) {",
                    "          return service.cari(id);",
                    "      }",
                    "  4. Jalankan tes yang sudah ada, lalu tambah satu tes untuk id yang",
                    "     nggak ada. Jangan membuat ProdukService dengan new di controller.",
                    "     Biarkan Spring menyuntikkannya lewat konstruktor yang sudah ada.",
                ],
            },
        ],
    },
    {
        "title": "13. Stack .NET dan Blazor: C# dari Server sampai Browser",
        "sections": [
            {
                "body": [
                    "Pengguna ekosistem Microsoft punya stack sendiri: ASP.NET Core di server",
                    "dan Blazor untuk tampilan, semuanya dengan C#. Tim yang sudah menulis C#",
                    "untuk desktop atau backend bisa membuat tampilan web interaktif tanpa",
                    "pindah ke JavaScript.",
                    "",
                    ".NET, ASP.NET Core, dan Blazor berlisensi MIT dan jalan di Windows,",
                    "Linux, dan macOS. Versi LTS terbaru saat materi ini ditulis",
                    "(Oktober 2026) adalah .NET 10, dengan rilis patch 10.0.13 tanggal",
                    "13 Oktober 2026 dan dukungan sampai 14 November 2028. .NET 11 masih",
                    "berstatus release candidate.",
                    "",
                    "Survei Stack Overflow 2026 mencatat C# dipakai 27,1% responden, ASP.NET",
                    "Core 20%, ASP.NET versi lama yang berbasis .NET Framework 14%, dan",
                    "Blazor 7%.",
                ],
            },
            {
                "heading": "Satu komponen Blazor",
                "body": [
                    "Komponen Blazor ditulis di berkas .razor: HTML biasa yang dicampur C#.",
                    "Baris dan atribut yang diawali @ adalah C#.",
                ],
            },
            {
                "heading": "Keranjang.razor",
                "bahasa": "html",
                "code": """@page "/keranjang"
@rendermode InteractiveServer

<h1>Keranjang</h1>
<p>Jumlah barang: @jumlah</p>
<button @onclick="Tambah">Tambah</button>

@code {
    private int jumlah = 0;

    private void Tambah()
    {
        jumlah++;
    }
}""",
            },
            {
                "body": [
                    "@page memberi alamat halaman. @rendermode InteractiveServer memilih mode",
                    "render, yang dibahas sesudah ini. @onclick memanggil method C# Tambah,",
                    "dan @jumlah menampilkan nilainya. Kamu nggak menulis satu baris",
                    "JavaScript pun.",
                ],
            },
            {
                "heading": "Empat mode render dan akibatnya",
                "body": [
                    "  - Static SSR: komponen dirender di server jadi HTML biasa, tanpa",
                    "    interaksi, mirip aplikasi multi-page di bab 2. Mode ini dipakai",
                    "    kalau nggak ada mode yang disebut.",
                    "  - Interactive Server: komponen tetap berjalan di server. Browser dan",
                    "    server tersambung terus lewat SignalR, pustaka komunikasi real-time",
                    "    yang biasanya memakai WebSocket. Setiap klik dikirim ke server, dan",
                    "    server mengirim balik bagian halaman yang berubah. Unduhan awalnya",
                    "    kecil, tapi koneksinya harus terus hidup, dan setiap pengguna aktif",
                    "    memakan memori server.",
                    "  - Interactive WebAssembly: runtime .NET dan kode aplikasimu diunduh ke",
                    "    browser lalu dijalankan di sana lewat WebAssembly. Setelah termuat,",
                    "    interaksi nggak perlu ke server. Kekurangannya, unduhan awalnya",
                    "    besar.",
                    "  - Interactive Auto: mula-mula berjalan seperti Interactive Server",
                    "    supaya cepat tampil, sambil mengunduh runtime di latar belakang.",
                    "    Kunjungan berikutnya memakai WebAssembly.",
                    "",
                    "Mode bisa dipilih per komponen. Halaman profil boleh Static SSR,",
                    "sementara satu kotak obrolan di dalamnya Interactive Server. Mode yang",
                    "boleh dipakai didaftarkan di Program.cs:",
                ],
            },
            {
                "heading": "Program.cs",
                "bahasa": "csharp",
                "code": """var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents()
    .AddInteractiveWebAssemblyComponents();

var app = builder.Build();
...
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode()
    .AddInteractiveWebAssemblyRenderMode();

app.Run();""",
            },
            {
                "body": [
                    "Kalau AddInteractiveWebAssemblyComponents nggak dipanggil, komponen",
                    "bermode WebAssembly nggak bisa dipakai. Baris yang dilewati (tanda ...)",
                    "berisi pengaturan lain dari template proyek, seperti berkas statis dan",
                    "perlindungan formulir.",
                    "",
                    "Program di bawah meniru cara Interactive Server menghemat kiriman:",
                    "setelah klik, yang dikirim cuma bagian yang berubah.",
                ],
            },
            {
                "heading": "Mengirim perubahan saja",
                "code": """def render(jumlah):
    return ["<h1>Keranjang</h1>",
            f"<p>Jumlah barang: {jumlah}</p>",
            "<button>Tambah</button>"]


def beda(lama, baru):
    return [(i, b) for i, (a, b) in enumerate(zip(lama, baru)) if a != b]


layar = render(0)
for klik in range(1, 3):
    baru = render(klik)
    perubahan = beda(layar, baru)
    print(f"klik {klik}: kirim {len(perubahan)} dari {len(baru)} baris {perubahan}")
    layar = baru
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  klik 1: kirim 1 dari 3 baris [(1, '<p>Jumlah barang: 1</p>')]",
                    "  klik 2: kirim 1 dari 3 baris [(1, '<p>Jumlah barang: 2</p>')]",
                    "",
                    "Blazor membandingkan pohon render. Contoh ini memakai baris teks supaya",
                    "gampang dilihat, dan idenya sama: yang menyeberang jaringan cuma",
                    "perubahan.",
                ],
            },
            {
                "heading": "Pasangan Blazor lainnya",
                "body": [
                    "  - Entity Framework Core (EF Core): ORM resmi .NET. Kelas C# dipetakan",
                    "    ke tabel SQL Server, PostgreSQL, atau database lain, dan query",
                    "    ditulis dengan LINQ.",
                    "  - SignalR juga bisa dipakai langsung, di luar Blazor, untuk fitur",
                    "    real-time seperti notifikasi atau obrolan.",
                    "  - Blazor Hybrid memakai komponen yang sama di aplikasi desktop dan",
                    "    mobile lewat .NET MAUI. Komponennya dirender di dalam aplikasi",
                    "    dengan akses ke API perangkat. Detail aplikasi mobile ada di",
                    "    kurikulum Mobile & Desktop.",
                    "  - Pustaka komponen seperti MudBlazor dan Fluent UI Blazor menyediakan",
                    "    tombol, tabel, dan formulir siap pakai.",
                    "",
                    "Model EF Core untuk produk kira-kira begini:",
                ],
            },
            {
                "heading": "Model dan DbContext EF Core",
                "bahasa": "csharp",
                "code": """using Microsoft.EntityFrameworkCore;

public class Produk
{
    public int Id { get; set; }
    public string Nama { get; set; } = "";
    public decimal Harga { get; set; }
}

public class TokoDb(DbContextOptions<TokoDb> options) : DbContext(options)
{
    public DbSet<Produk> DaftarProduk => Set<Produk>();
}

// di service atau komponen:
// var murah = await db.DaftarProduk.Where(p => p.Harga < 5000).ToListAsync();""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Blazor banyak dipakai untuk aplikasi internal di perusahaan yang sudah",
                    "memakai produk Microsoft: dasbor, sistem lini bisnis, dan formulir",
                    "pengajuan yang tersambung ke SQL Server dan login Microsoft Entra ID.",
                    "",
                    "Kasus kecil: kantor cabang sebuah perusahaan memintamu membuat dasbor",
                    "stok gudang dengan Blazor. Penggunanya sekitar 30 karyawan di jaringan",
                    "kantor yang stabil, ditambah beberapa sales yang membukanya dari HP",
                    "dengan sinyal naik turun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan halamannya. Laporan bulanan cuma dibaca, jadi pakai Static",
                    "     SSR yang paling ringan.",
                    "  2. Dasbor stok untuk karyawan kantor butuh angka yang terus",
                    "     diperbarui. Jaringannya stabil dan penggunanya sedikit, jadi",
                    "     Interactive Server cocok, dan unduhan awalnya kecil.",
                    "  3. Halaman untuk sales sering kehilangan sinyal, dan Interactive",
                    "     Server bakal putus-sambung di sana. Pakai Interactive WebAssembly",
                    "     atau Auto, supaya tombol dan formulir tetap bereaksi walau sinyal",
                    "     hilang sebentar.",
                    "  4. Daftarkan kedua mode di Program.cs, lalu pasang @rendermode di tiap",
                    "     komponen sesuai keputusan tadi.",
                ],
            },
        ],
    },
    {
        "title": "14. Stack HTML over the Wire: Hotwire, PETAL, GOTH, BETH",
        "sections": [
            {
                "body": [
                    "Di stack SPA, server mengirim JSON dan browser menyusun HTML-nya dengan",
                    "JavaScript. Pendekatan HTML over the wire membaliknya lagi. Server yang",
                    "menyusun HTML seperti di aplikasi multi-page, tapi yang dikirim cuma",
                    "potongan untuk bagian halaman yang berubah. Pustaka kecil di browser",
                    "menukar potongan itu tanpa memuat ulang halaman.",
                    "",
                    "Hasilnya terasa seperti SPA, sementara logika dan tampilan tetap di satu",
                    "tempat, yaitu server. Nggak ada API terpisah, nggak ada state yang harus",
                    "disamakan di dua sisi, dan JavaScript yang ditulis tinggal sedikit.",
                    "Empat stack di bawah ini memakai ide yang sama dengan bahasa berbeda.",
                ],
            },
            {
                "heading": "Empat stack HTML over the wire",
                "bahasa": "teks",
                "code": """Stack          Bahasa      Komponen                           Status
-------------  ----------  ---------------------------------  -------------
Rails+Hotwire  Ruby        Rails, Turbo, Stimulus,            aktif
                           Hotwire Native
PETAL          Elixir      Phoenix, Elixir, Tailwind,         aktif, niche
                           Alpine.js, LiveView
GOTH           Go          Go net/http, templ, htmx           aktif, niche
BETH           TypeScript  Bun, Elysia, Turso, htmx           jarang dipakai""",
            },
            {
                "heading": "Rails + Hotwire",
                "body": [
                    "Hotwire dibuat tim di balik Basecamp. Namanya singkatan dari HTML Over",
                    "The Wire. Isinya:",
                    "",
                    "  - Turbo Drive: setiap klik tautan diambil di latar belakang, lalu isi",
                    "    body diganti tanpa memuat ulang seluruh halaman.",
                    "  - Turbo Frames: bagian halaman yang dibungkus frame bisa diganti",
                    "    sendiri. Klik di dalam frame cuma memperbarui frame itu.",
                    "  - Turbo Streams: server mengirim perintah kecil seperti tambahkan,",
                    "    ganti, atau hapus elemen tertentu, lewat response biasa atau",
                    "    WebSocket.",
                    "  - Stimulus: JavaScript kecil yang ditempel lewat atribut",
                    "    data-controller, untuk interaksi yang memang harus terjadi di",
                    "    browser.",
                    "  - Hotwire Native: membungkus aplikasi web yang sama jadi aplikasi",
                    "    Android dan iOS.",
                    "",
                    "Panduan resmi Rails menyebut \"Rails ships with Turbo\". Panduan yang",
                    "aktif saat materi ini ditulis bertanda Rails 8.1.4, dan versi Turbo",
                    "terbaru 8.0.23 (Januari 2026). Rails 8 juga menambahkan Solid Queue,",
                    "Solid Cache, Solid Cable, dan alat deploy Kamal, supaya satu server",
                    "cukup untuk aplikasi lengkap. Survei Stack Overflow 2026 mencatat Ruby",
                    "on Rails dipakai 6% responden. Turbo Frame di view Rails kira-kira",
                    "begini:",
                ],
            },
            {
                "heading": "Turbo Frame di view",
                "bahasa": "erb",
                "code": """<%# app/views/produk/show.html.erb %>
<h1><%= @produk.nama %></h1>

<%= turbo_frame_tag "stok_#{@produk.id}" do %>
  <p>Stok: belum dicek</p>
  <%= link_to "Cek stok", stok_produk_path(@produk) %>
<% end %>""",
            },
            {
                "heading": "Action yang menjawab frame itu",
                "bahasa": "ruby",
                "code": """class ProdukController < ApplicationController
  ...

  def stok
    @produk = Produk.find(params[:id])
    # merender app/views/produk/stok.html.erb, yang juga
    # berisi turbo_frame_tag dengan id yang sama
  end
end""",
            },
            {
                "body": [
                    "Tautan \"Cek stok\" ada di dalam frame stok_7. Waktu diklik, Turbo",
                    "mengambil halaman stok di latar belakang, mencari frame dengan id yang",
                    "sama di response, lalu mengganti isi frame itu saja. Judul produk di",
                    "luar frame nggak tersentuh. Kalau response nggak memuat frame ber-id",
                    "sama, Turbo menampilkan pesan bahwa isi frame hilang.",
                ],
            },
            {
                "heading": "PETAL: Phoenix LiveView",
                "body": [
                    "PETAL singkatan dari Phoenix, Elixir, Tailwind, Alpine.js, dan LiveView.",
                    "Elixir adalah bahasa yang berjalan di mesin virtual Erlang, terkenal",
                    "tangguh melayani banyak koneksi bersamaan. Phoenix framework web-nya,",
                    "dan LiveView membuat halaman interaktif yang keadaannya disimpan di",
                    "server.",
                    "",
                    "Setiap pengguna yang membuka halaman LiveView punya satu proses kecil di",
                    "server, tersambung ke browser lewat WebSocket. Saat tombol diklik, event",
                    "dikirim ke server, keadaan diubah, dan server mengirim balik bagian yang",
                    "berubah. Versi LiveView terbaru saat materi ini ditulis 1.2.12",
                    "(September 2026), berlisensi MIT. Survei 2026 mencatat Elixir dan",
                    "Phoenix masing-masing dipakai 3% responden. Aplikasi ini belum punya",
                    "kurikulum Elixir, jadi contoh berikut cukup dibaca.",
                ],
            },
            {
                "heading": "Komponen LiveView",
                "bahasa": "elixir",
                "code": "defmodule TokoWeb.KeranjangLive do\n  use TokoWeb, :live_view\n\n  def mount(_params, _session, socket) do\n    {:ok, assign(socket, jumlah: 0)}\n  end\n\n  def handle_event(\"tambah\", _params, socket) do\n    {:noreply, update(socket, :jumlah, &(&1 + 1))}\n  end\n\n  def render(assigns) do\n    ~H\"\"\"\n    <button phx-click=\"tambah\">Tambah</button>\n    <p>Jumlah barang: {@jumlah}</p>\n    \"\"\"\n  end\nend",
            },
            {
                "heading": "GOTH dan BETH",
                "body": [
                    "GOTH memakai Go untuk server (cukup pustaka net/http), templ untuk",
                    "komponen HTML yang dikompilasi jadi kode Go, dan htmx untuk interaksi.",
                    "Hasilnya satu berkas biner yang gampang dipasang. Versi templ saat",
                    "materi ini ditulis v0.3.1070 (Oktober 2026). Survei 2026 mencatat Go",
                    "dipakai 17% responden dan htmx 5%.",
                    "",
                    "htmx adalah pustaka JavaScript yang menambahkan atribut ke HTML biasa.",
                    "Atribut hx-get berarti \"kirim GET ke alamat ini\", hx-target menunjuk",
                    "elemen yang diisi, dan hx-swap menentukan cara mengisinya. htmx merilis",
                    "versi 4.0.0 pada 28 Agustus 2026, dan jalur 2.x masih dirawat, jadi cek",
                    "versi yang dipakai tutorial sebelum menyalin kodenya.",
                ],
            },
            {
                "heading": "Tombol htmx",
                "bahasa": "html",
                "code": """<button hx-get="/stok/7" hx-target="#stok-7" hx-swap="innerHTML">
  Cek stok
</button>
<span id="stok-7">belum dicek</span>""",
            },
            {
                "heading": "Handler Go yang menjawabnya",
                "bahasa": "go",
                "code": """func stok(w http.ResponseWriter, r *http.Request) {
	id := r.PathValue("id")
	fmt.Fprintf(w, "<strong>%d</strong> tersisa", hitungStok(id))
}

// di main: mux.HandleFunc("GET /stok/{id}", stok)""",
            },
            {
                "body": [
                    "Pola \"GET /stok/{id}\" dan r.PathValue tersedia di pustaka standar Go",
                    "sejak versi 1.22. Handler-nya menulis potongan HTML biasa, dan htmx",
                    "memasukkannya ke dalam elemen #stok-7.",
                    "",
                    "BETH ramai dibicarakan tahun 2023: Bun sebagai runtime JavaScript,",
                    "Elysia sebagai framework web, Turso sebagai database (SQLite yang bisa",
                    "disebar ke banyak lokasi, berbasis libSQL), dan htmx. Konsepnya sama",
                    "dengan stack Go tadi, bahasanya TypeScript. Pemakaiannya masih jarang.",
                    "Bun sendiri tercatat dipakai 9% responden survei 2026. Stack ini disebut",
                    "supaya kamu mengenali namanya, dan belum perlu dipelajari.",
                    "",
                    "Program di bawah meniru satu klik htmx: server mengirim potongan HTML,",
                    "lalu potongan itu masuk ke elemen sasaran.",
                ],
            },
            {
                "heading": "Meniru satu klik htmx",
                "code": """# isi tiap elemen ber-id di halaman yang sedang tampil
halaman = {
    "judul": "<h1>Pensil 2B</h1>",
    "stok-7": "belum dicek",
    "ulasan": "<p>2 ulasan</p>",
}


def server(path):
    # server merender potongan HTML untuk satu bagian saja
    if path == "/stok/7":
        return "<strong>12</strong> tersisa"
    return "<em>tidak ditemukan</em>"


def klik(hx_get, hx_target):
    potongan = server(hx_get)
    halaman[hx_target] = potongan       # hx-swap="innerHTML"
    print(f"GET {hx_get} -> {len(potongan)} byte HTML masuk ke #{hx_target}")


klik("/stok/7", "stok-7")
for id_elemen, isi in halaman.items():
    print(f"  #{id_elemen:<7} {isi}")
""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  GET /stok/7 -> 27 byte HTML masuk ke #stok-7",
                    "    #judul   <h1>Pensil 2B</h1>",
                    "    #stok-7  <strong>12</strong> tersisa",
                    "    #ulasan  <p>2 ulasan</p>",
                    "",
                    "Cuma isi #stok-7 yang berubah. Judul dan ulasan nggak dikirim ulang, dan",
                    "nggak ada JSON yang harus diubah jadi HTML di browser.",
                ],
            },
            {
                "heading": "Kapan pantas dipilih",
                "body": [
                    "  - Cocok untuk aplikasi CRUD, panel admin, toko, dan situs konten yang",
                    "    interaksinya berupa klik, formulir, dan daftar yang diperbarui.",
                    "  - Cocok untuk tim kecil yang ingin satu bahasa di server dan nggak mau",
                    "    memelihara SPA terpisah.",
                    "  - Kurang cocok untuk aplikasi yang harus jalan saat offline, atau yang",
                    "    interaksinya padat di browser seperti editor desain dan peta",
                    "    interaktif. Setiap interaksi yang butuh data berarti satu perjalanan",
                    "    ke server.",
                    "  - Perhitungkan aplikasi mobile. Kalau aplikasi mobile native butuh API",
                    "    JSON, API itu tetap harus dibuat, kecuali kamu memakai pembungkus",
                    "    seperti Hotwire Native.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Basecamp dibangun dengan Rails dan Hotwire, dan pembuatnya banyak",
                    "menulis tentang pendekatan ini. Banyak proyek Django dan Laravel juga",
                    "menambahkan htmx untuk interaksi kecil tanpa pindah ke React. Kamu bisa",
                    "mengenalinya dari atribut hx-get atau tag <turbo-frame> di View Page",
                    "Source.",
                    "",
                    "Kasus kecil: halaman daftar pesanan di aplikasi Django kantormu memuat",
                    "ulang seluruh halaman setiap kali admin menekan tombol \"tandai",
                    "terkirim\". Halamannya panjang, dan posisi gulir admin selalu kembali ke",
                    "atas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kamu nggak perlu menulis ulang jadi SPA. Pasang htmx di template",
                    "     dasar dengan satu tag script.",
                    "  2. Pecah baris pesanan jadi template kecil sendiri, misalnya",
                    "     _baris_pesanan.html, supaya bisa dirender terpisah.",
                    "  3. Ubah tombolnya:",
                    "      <button hx-post=\"/pesanan/41/terkirim\"",
                    "              hx-target=\"closest tr\" hx-swap=\"outerHTML\">",
                    "        Tandai terkirim",
                    "      </button>",
                    "  4. Di view Django, ubah status pesanan lalu kembalikan template",
                    "     _baris_pesanan.html saja. Karena ini POST, kirim juga token CSRF",
                    "     Django, misalnya lewat atribut hx-headers di tag body.",
                ],
            },
        ],
    },
    {
        "title": "15. Serverless dan Edge: Kode Tanpa Mengurus Server",
        "sections": [
            {
                "body": [
                    "Bayangkan kamu bikin API kecil untuk pendaftaran lomba 17-an di",
                    "kampungmu. API itu ramai tiga hari dalam setahun, lalu sepi. Kalau kamu",
                    "menyewa server yang nyala 24 jam, kamu bayar penuh untuk 362 hari yang",
                    "nganggur.",
                    "",
                    "Serverless menawarkan cara lain. Kamu cuma menulis fungsi. Penyedia",
                    "cloud yang menyalakan mesin waktu ada kejadian, menjalankan fungsimu,",
                    "lalu mematikannya lagi kalau sepi. Tagihannya dihitung per pemanggilan",
                    "dan per milidetik fungsi itu berjalan.",
                    "",
                    "Namanya memang menyesatkan. Servernya tetap ada. Bedanya, kamu nggak",
                    "perlu memasang sistem operasi, menambal keamanan, atau memikirkan berapa",
                    "mesin yang harus nyala. Semua itu diurus penyedianya.",
                    "",
                    "Artikel Mike Roberts di martinfowler.com (2018) membagi serverless jadi",
                    "dua bagian:",
                    "",
                    "  - FaaS (Function as a Service): kode buatanmu sendiri, dibungkus dalam",
                    "    fungsi kecil yang dijalankan saat dipicu kejadian. Contohnya AWS",
                    "    Lambda dan Cloudflare Workers.",
                    "  - BaaS (Backend as a Service): layanan jadi yang kamu pakai lewat API",
                    "    tanpa menulis servernya, misalnya database dan login siap pakai. Ini",
                    "    dibahas di materi berikutnya.",
                ],
            },
            {
                "heading": "Fungsi yang dipicu kejadian",
                "body": [
                    "Di dunia serverless, semuanya dimulai dari kejadian, atau event.",
                    "Kejadian bisa berupa request HTTP yang masuk, berkas yang diunggah ke",
                    "penyimpanan, pesan yang masuk antrean, atau jadwal seperti \"tiap jam",
                    "00.00\".",
                    "",
                    "Penyedia cloud menerjemahkan kejadian itu jadi data, lalu memanggil",
                    "fungsimu dengan data tersebut. Fungsi itu disebut handler. Di AWS Lambda",
                    "versi Python, bentuknya begini:",
                ],
                "code": """import json


def lambda_handler(event, context):
    # event: data kejadian dari API Gateway, bentuknya dict biasa
    params = event.get("queryStringParameters") or {}
    nama = params.get("nama", "dunia")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"pesan": f"Halo, {nama}!"}),
    }


# Di AWS, Lambda yang memanggil fungsi ini. Di sini kita panggil sendiri
# dengan event tiruan supaya bisa dicoba tanpa akun cloud.
for event in ({"queryStringParameters": {"nama": "Sari"}},
              {"queryStringParameters": None}):
    hasil = lambda_handler(event, None)
    print(hasil["statusCode"], hasil["body"])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  200 {\"pesan\": \"Halo, Sari!\"}",
                    "  200 {\"pesan\": \"Halo, dunia!\"}",
                    "",
                    "Fungsinya cuma menerima event dan mengembalikan jawaban. Nggak ada kode",
                    "untuk membuka port atau menunggu koneksi. Itu tugas API Gateway, layanan",
                    "AWS yang menerima request HTTP lalu meneruskannya ke Lambda sebagai",
                    "event.",
                    "",
                    "Kunci queryStringParameters bisa bernilai None atau nggak ada sama",
                    "sekali kalau alamatnya nggak punya tanda tanya. Makanya ada \"or {}\" di",
                    "baris pertama handler. Parameter context berisi info tentang pemanggilan",
                    "ini, misalnya sisa waktu sebelum fungsi dihentikan. Contoh ini nggak",
                    "memakainya.",
                ],
            },
            {
                "heading": "Cold start dan warm start",
                "body": [
                    "Fungsimu tetap butuh tempat berjalan. Lambda menyiapkan semacam mesin",
                    "kecil yang disebut lingkungan eksekusi, atau instans, lalu memuat kodemu",
                    "di sana. Penyiapan ini disebut fase inisialisasi.",
                    "",
                    "Panggilan pertama ke instans baru harus menunggu fase itu selesai.",
                    "Penundaan ini disebut cold start. Sesudahnya, instans dibiarkan hidup",
                    "sebentar. Kalau ada panggilan lagi, instans yang sama dipakai ulang",
                    "tanpa inisialisasi. Itu warm start. Kalau lama nggak dipanggil,",
                    "instansnya dibuang, dan panggilan berikutnya kena cold start lagi.",
                    "",
                    "Kode di luar handler, misalnya import dan pembukaan koneksi database,",
                    "cuma jalan saat inisialisasi. Program di bawah meniru perilaku itu untuk",
                    "satu instans:",
                ],
                "code": """import json

jumlah_init = 0
cache_harga = None          # hidup selama instansnya hidup


def muat_harga():
    # Pura-puranya mahal: buka koneksi database, baca konfigurasi
    global jumlah_init
    jumlah_init += 1
    return {"pensil": 2000, "buku": 5000}


def handler(event, context):
    global cache_harga
    dingin = cache_harga is None
    if dingin:
        cache_harga = muat_harga()
    barang = event["barang"]
    return {"cold": dingin, "body": json.dumps({barang: cache_harga[barang]})}


for barang in ["pensil", "buku", "pensil"]:
    hasil = handler({"barang": barang}, None)
    print("COLD" if hasil["cold"] else "WARM", hasil["body"])
print("muat_harga dipanggil", jumlah_init, "kali")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  COLD {\"pensil\": 2000}",
                    "  WARM {\"buku\": 5000}",
                    "  WARM {\"pensil\": 2000}",
                    "  muat_harga dipanggil 1 kali",
                    "",
                    "Pekerjaan mahal di muat_harga() cuma terjadi sekali, lalu hasilnya",
                    "dipakai ulang oleh panggilan yang hangat. Makanya koneksi database",
                    "biasanya dibuka di luar handler.",
                    "",
                    "Jebakan: variabel global seperti cache_harga hidup selama instansnya",
                    "hidup, tapi kamu nggak pernah tahu panggilan berikutnya jatuh ke instans",
                    "yang mana. Kalau sepuluh orang memanggil bersamaan, Lambda menyalakan",
                    "beberapa instans, dan masing-masing punya memori sendiri. Simpan data",
                    "penting di database, jangan di variabel.",
                    "",
                    "Ada dua cara mengurangi cold start di Lambda. Provisioned concurrency",
                    "menjaga sejumlah instans tetap siap, dengan biaya tambahan. SnapStart",
                    "menyimpan potret instans yang sudah diinisialisasi, lalu memulihkannya",
                    "saat dibutuhkan. Menurut dokumentasi AWS per Oktober 2026, SnapStart",
                    "mendukung Java 11 ke atas, Python 3.12 ke atas, dan .NET 8 ke atas.",
                ],
            },
            {
                "heading": "Batas dan biaya",
                "body": [
                    "Serverless punya pagar. Angka di bawah ini dari halaman kuota AWS Lambda",
                    "per Oktober 2026:",
                    "",
                    "  - Satu pemanggilan paling lama 15 menit (900 detik). Pekerjaan yang",
                    "    lebih lama harus dipecah atau dipindah ke layanan lain.",
                    "  - Memori bisa diatur dari 128 MB sampai 10.240 MB. Tenaga CPU ikut",
                    "    naik sebanding dengan memori.",
                    "  - Request dan respons sinkron masing-masing paling besar 6 MB.",
                    "    Unggahan berkas besar sebaiknya langsung ke penyimpanan seperti",
                    "    Amazon S3.",
                    "  - Satu region punya kuota bawaan 1.000 eksekusi bersamaan untuk",
                    "    seluruh akunmu. Kuota ini bisa dinaikkan lewat permintaan.",
                    "",
                    "Sejak 1 Agustus 2025, AWS juga menagih durasi fase inisialisasi untuk",
                    "semua fungsi. Cold start yang lama menambah tagihan, selain membuat",
                    "pengguna menunggu.",
                    "",
                    "Jebakan: biaya bisa membengkak tanpa terasa. Contoh klasiknya fungsi",
                    "yang dipicu berkas baru di sebuah bucket S3, lalu menyimpan hasilnya ke",
                    "bucket yang sama. Hasil itu memicu fungsi lagi, terus berulang, dan tiap",
                    "putaran ditagih. Pisahkan folder masukan dan keluaran, lalu pasang",
                    "peringatan anggaran di akun cloud-mu.",
                    "",
                    "Dokumentasi AWS tahun 2026 juga mulai memakai nama baru. Fungsi biasa",
                    "yang dipicu kejadian disebut Lambda Event Functions. Ada juga jenis",
                    "baru, Lambda Web Functions, untuk menjalankan server HTTP utuh secara",
                    "serverless. Kalau tutorial menyebut salah satunya, sekarang kamu tahu",
                    "bedanya.",
                ],
            },
            {
                "heading": "Stack serverless klasik di AWS",
                "body": [
                    "Kombinasi yang paling sering dicontohkan adalah Lambda, API Gateway, dan",
                    "DynamoDB. API Gateway menerima request HTTP, Lambda menjalankan",
                    "logikanya, dan DynamoDB menyimpan datanya. DynamoDB adalah database",
                    "kunci-nilai milik AWS yang juga serverless. Berkas seperti foto biasanya",
                    "masuk Amazon S3.",
                    "",
                    "Menyusun semua itu lewat klik di konsol cepat melelahkan dan susah",
                    "diulang. Orang memakai alat infrastructure as code, yaitu menuliskan",
                    "susunan layanan di berkas teks. Pilihannya:",
                    "",
                    "  - AWS SAM: perluasan CloudFormation buatan AWS. Templatenya berupa",
                    "    YAML, dan perintah \"sam local invoke\" bisa menjalankan fungsi di",
                    "    laptopmu.",
                    "  - Serverless Framework: alat lama yang populer, berkasnya",
                    "    serverless.yml. Mulai versi 4, alat ini gratis untuk individu dan",
                    "    organisasi beromzet di bawah 2 juta dolar AS per tahun. Di atas itu",
                    "    wajib berlangganan. Versi terbarunya saat materi ini ditulis",
                    "    (Oktober 2026) 4.44.0.",
                    "  - SST: open source dan ditulis dengan TypeScript. Versinya v4.17.2 per",
                    "    Oktober 2026.",
                    "  - AWS CDK: infrastruktur ditulis sebagai kode TypeScript, Python,",
                    "    Java, atau bahasa lain, lalu diterjemahkan jadi CloudFormation.",
                    "    Versinya v2.273.0 per Oktober 2026.",
                    "",
                    "Runtime Lambda terbaru per Oktober 2026 antara lain nodejs24.x,",
                    "python3.14, java25, dotnet10, dan ruby4.0. Contoh template berikut",
                    "memasang handler tadi di balik alamat GET /harga. Cara memakainya sampai",
                    "ke produksi dibahas di kurikulum DevOps & Cloud.",
                ],
                "bahasa": "yaml",
                "code": """AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Resources:
  HargaFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: app.lambda_handler
      Runtime: python3.14
      MemorySize: 256
      Timeout: 10
      Events:
        AmbilHarga:
          Type: HttpApi
          Properties:
            Path: /harga
            Method: get""",
            },
            {
                "heading": "Edge: fungsi di dekat pengguna",
                "body": [
                    "Lambda berjalan di region yang kamu pilih, misalnya Singapura atau",
                    "Jakarta. Pengguna di Medan dan di Jayapura sama-sama harus menjangkau",
                    "region itu. Edge computing membalik caranya: kodemu disebar ke banyak",
                    "lokasi jaringan, dan tiap request dilayani lokasi yang paling dekat",
                    "dengan penggunanya.",
                    "",
                    "Cloudflare Workers paling dikenal di kelompok ini. Workers nggak",
                    "menyalakan kontainer untuk tiap fungsi. Ia memakai isolate V8, yaitu",
                    "ruang terpisah di dalam mesin JavaScript yang sama dengan milik Chrome,",
                    "jadi memulai fungsi baru jauh lebih ringan. Bentuk kodenya mengikuti",
                    "fetch, API yang juga ada di browser:",
                ],
                "bahasa": "javascript",
                "code": """export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/halo") {
      const nama = url.searchParams.get("nama") ?? "dunia";
      return new Response(`Halo, ${nama}!`);
    }
    ...
    return new Response("Nggak ada di sini", { status: 404 });
  },
};""",
            },
            {
                "body": [
                    "Cloudflare memanggil fetch untuk setiap request yang masuk, dengan objek",
                    "Request yang sama seperti di browser. Alamat /halo?nama=Budi dijawab",
                    "\"Halo, Budi!\", dan alamat lain dijawab status 404. Baris ... menandai",
                    "rute lain yang dipotong dari contoh. Parameter env berisi sambungan ke",
                    "penyimpanan dan rahasia milik Worker itu.",
                    "",
                    "Paket gratis Workers memberi 100.000 request per hari dan 10 ms waktu",
                    "CPU per pemanggilan. Paket berbayarnya mulai 5 dolar AS per bulan.",
                    "Datanya disimpan di layanan pendamping:",
                    "",
                    "  - D1: database SQL berbasis SQLite.",
                    "  - Workers KV: penyimpanan kunci-nilai yang cepat dibaca dari mana",
                    "    saja. Perubahannya butuh waktu untuk menyebar ke semua lokasi.",
                    "  - R2: penyimpanan objek untuk berkas, kompatibel dengan API S3.",
                    "  - Durable Objects: objek yang statusnya dijamin cuma hidup di satu",
                    "    tempat, cocok untuk ruang chat atau penghitung.",
                    "",
                    "Jebakan: edge nggak otomatis lebih cepat. Kalau fungsimu jalan di lokasi",
                    "terdekat tapi databasenya di Amerika, tiap request tetap menyeberang",
                    "samudra. Workers juga belum menyediakan semua API Node.js; sebagian baru",
                    "tersedia lewat flag kompatibilitas.",
                    "",
                    "Untuk mencoba di laptop, panduan resminya memakai Wrangler, alat baris",
                    "perintah milik Cloudflare (versi 4.151.1 per Oktober 2026):",
                ],
                "bahasa": "terminal",
                "code": """npm create cloudflare@latest -- halo-worker
cd halo-worker
npx wrangler dev        # jalan di laptop, http://localhost:8787
npx wrangler deploy     # kirim ke jaringan Cloudflare""",
            },
            {
                "heading": "Pemain lain dan kapan memilih serverless",
                "body": [
                    "  - Vercel Functions dan Netlify Functions: platform deploy frontend",
                    "    yang sekalian menjalankan fungsi di belakang situsmu. Paket Hobby",
                    "    Vercel gratis, tapi khusus pemakaian pribadi nonkomersial. Netlify",
                    "    memakai paket berbasis kredit untuk akun baru sejak September 2025.",
                    "  - Azure Functions: layanan FaaS milik Microsoft. Runtime host-nya open",
                    "    source berlisensi MIT.",
                    "  - Google Cloud Run functions: dulu bernama Cloud Functions. Kuota",
                    "    gratisnya 2 juta request per bulan.",
                    "",
                    "Di Survei Stack Overflow 2026, AWS dipakai 42% responden, Cloudflare",
                    "25%, Firebase 11%, dan Vercel 11%. Angka itu untuk platformnya secara",
                    "keseluruhan. Survei itu nggak menanyakan serverless secara terpisah.",
                    "",
                    "Kategori survei yang memuat angka tadi bernama cloud development,",
                    "gabungan platform cloud, kontainer, package manager, dan alat build.",
                    "Sampai 2024 kategori itu masih terpecah jadi cloud platforms dan other",
                    "tools. Hampir semua isinya milik kurikulum DevOps & Cloud.",
                    "Pengecualiannya Unity, Godot, dan Unreal Engine dari daftar other tools",
                    "2024, yang dibahas di kurikulum Game & Grafis.",
                    "",
                    "Jadi kapan serverless pantas dipilih? Patokannya bentuk bebanmu:",
                    "",
                    "  Cocok                                Kurang cocok",
                    "  -----------------------------------  ---------------------------------",
                    "  Lalu lintas naik turun atau sepi     Beban tinggi dan stabil 24 jam",
                    "  Tugas pendek yang dipicu kejadian    Proses lebih dari 15 menit",
                    "  Webhook, cron, olah gambar, email    Latensi harus stabil tiap saat",
                    "  Tim kecil tanpa orang khusus server  Butuh kontrol penuh atas mesin",
                    "",
                    "Untuk beban yang stabil sepanjang hari, server atau kontainer yang nyala",
                    "terus sering lebih murah. Harga per satuan komputasi di serverless",
                    "biasanya lebih tinggi; kamu membayar kemudahannya. Hitung dulu perkiraan",
                    "jumlah request dan durasinya sebelum memutuskan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Serverless banyak dipakai untuk pekerjaan kecil yang datang sesekali.",
                    "Contohnya menerima webhook pembayaran, mengirim email konfirmasi",
                    "pesanan, membuat thumbnail foto yang baru diunggah ke toko online, dan",
                    "menyusun laporan terjadwal tiap malam.",
                    "",
                    "Kasus kecil: sebuah toko online kecil ingin setiap foto produk yang",
                    "diunggah penjual otomatis dibuatkan versi kecil selebar 300 piksel untuk",
                    "halaman daftar produk.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jadikan unggahan sebagai kejadian. Foto asli masuk ke bucket S3 di",
                    "     folder foto-asli/, dan bucket itu dipasangi pemicu yang memanggil",
                    "     fungsi Lambda.",
                    "  2. Di handler, ambil nama bucket dan nama berkas dari event, buat",
                    "     thumbnail, lalu simpan ke folder lain:",
                    "       for rekaman in event[\"Records\"]:",
                    "           bucket = rekaman[\"s3\"][\"bucket\"][\"name\"]",
                    "           kunci = rekaman[\"s3\"][\"object\"][\"key\"]",
                    "           tujuan = kunci.replace(\"foto-asli/\", \"thumbnail/\")",
                    "  3. Batasi pemicunya hanya untuk awalan foto-asli/. Kalau pemicu",
                    "     mendengarkan seluruh bucket, thumbnail yang baru disimpan akan",
                    "     memicu fungsi itu lagi tanpa henti.",
                    "  4. Jangan mencatat foto mana yang sudah diproses di variabel global.",
                    "     Kalau catatan itu perlu, simpan di DynamoDB.",
                    "  5. Uji handler di laptop dengan event tiruan berisi satu rekaman,",
                    "     seperti contoh lambda_handler di atas, sebelum memasang pemicunya",
                    "     di cloud.",
                ],
            },
        ],
    },
    {
        "title": "16. BaaS, Headless, dan MACH: Merakit dari Layanan Jadi",
        "sections": [
            {
                "body": [
                    "Hampir semua aplikasi butuh hal yang sama di belakang layar: database,",
                    "login, tempat menyimpan foto, dan kadang notifikasi real-time. Menulis",
                    "semuanya sendiri makan waktu berminggu-minggu sebelum fitur pertama yang",
                    "khas aplikasimu bisa dikerjakan.",
                    "",
                    "Backend as a Service, disingkat BaaS, menyediakan bagian-bagian itu siap",
                    "pakai. Aplikasi web atau mobile-mu bicara langsung ke layanannya lewat",
                    "SDK, yaitu pustaka resmi dari penyedia. Kamu menulis frontend dan aturan",
                    "aksesnya, sisanya disewa.",
                    "",
                    "Materi ini membahas tiga hal yang idenya mirip, yaitu merakit sistem",
                    "dari layanan jadi: BaaS, headless CMS, dan arsitektur komposabel untuk",
                    "perusahaan besar.",
                ],
            },
            {
                "heading": "Tiga BaaS yang paling sering kamu temui",
                "body": [
                    "Supabase dibangun di atas PostgreSQL. Isinya database, Auth untuk login,",
                    "Storage untuk berkas, Realtime untuk mengirim perubahan data langsung ke",
                    "aplikasi, dan Edge Functions untuk kode di server. Sebagian besar",
                    "komponennya open source berlisensi Apache-2.0, dan bisa dipasang sendiri",
                    "dengan Docker Compose. Di Survei Stack Overflow, pemakai Supabase",
                    "sebagai database naik dari 4% (2024) ke 6% (2025) lalu 8% (2026).",
                    "",
                    "Firebase milik Google. Isinya Cloud Firestore (database dokumen),",
                    "Realtime Database (database berbentuk satu pohon JSON), Authentication,",
                    "Cloud Functions, Hosting, dan Cloud Messaging untuk notifikasi. Untuk",
                    "proyek baru, Firebase umumnya mengarahkan ke Firestore. Sejak 2025 ada",
                    "juga Firebase Data Connect yang memakai PostgreSQL. Layanannya",
                    "proprietary, tapi SDK kliennya open source. Survei Stack Overflow 2026",
                    "mencatat Firebase dipakai 11% responden.",
                    "",
                    "PocketBase adalah satu berkas program buatan Go yang sudah berisi",
                    "database SQLite, login, dan halaman admin. Cukup diunduh lalu",
                    "dijalankan. Lisensinya MIT. Versinya v0.40.5 per Oktober 2026, dan",
                    "karena masih di bawah 1.0, perubahan yang merusak kompatibilitas masih",
                    "mungkin terjadi.",
                    "",
                    "  BaaS        Database         Bisa dipasang sendiri  Survei SO 2026",
                    "  ----------  ---------------  ---------------------  ---------------",
                    "  Supabase    PostgreSQL       ya (Docker Compose)    database 8%",
                    "  Firebase    Firestore, RTDB  tidak                  cloud 11%",
                    "  PocketBase  SQLite           ya (satu berkas)       database 1%",
                ],
            },
            {
                "heading": "Yang tetap jadi tugasmu: aturan akses",
                "body": [
                    "Di aplikasi biasa, backend-mu yang memeriksa \"boleh nggak orang ini",
                    "membaca data itu\". Di BaaS, aplikasi bicara langsung ke database.",
                    "Pemeriksaannya pindah ke aturan yang kamu pasang di layanan itu.",
                    "",
                    "Supabase memakai Row Level Security (RLS) milik PostgreSQL. Kamu menulis",
                    "policy, yaitu syarat yang ditempelkan ke setiap query. Contoh ini",
                    "membuat pengguna yang login cuma bisa membaca catatan miliknya sendiri:",
                ],
                "bahasa": "postgresql",
                "code": """alter table catatan enable row level security;

create policy "pemilik membaca catatannya sendiri"
on catatan for select
to authenticated
using ( (select auth.uid()) = user_id );""",
            },
            {
                "body": [
                    "Firebase Realtime Database memakai aturan berbentuk JSON. Aturan di",
                    "bawah sering dipasang saat mencoba-coba, lalu lupa diganti. Artinya",
                    "siapa pun yang tahu alamat proyekmu boleh membaca dan menulis seluruh",
                    "database:",
                ],
                "bahasa": "json",
                "code": """{
  "rules": {
    ".read": true,
    ".write": true
  }
}""",
            },
            {
                "heading": "Meniru RLS dengan SQLite",
                "body": [
                    "Supaya kelihatan apa yang dicegah RLS, program kecil ini memakai SQLite",
                    "bawaan Python. Fungsi pertama mengambil semua baris. Fungsi kedua selalu",
                    "menempelkan syarat pemilik, persis seperti policy tadi:",
                ],
                "code": """import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE catatan (id INTEGER, pemilik TEXT, isi TEXT)")
db.executemany("INSERT INTO catatan VALUES (?, ?, ?)", [
    (1, "sari", "PR matematika"),
    (2, "budi", "sandi wifi rumah"),
    (3, "sari", "beli tinta"),
])


def ambil_tanpa_aturan():
    return [isi for (isi,) in db.execute("SELECT isi FROM catatan")]


def ambil_dengan_aturan(pengguna):
    # Ini yang dikerjakan RLS: syarat pemilik selalu ditempelkan
    sql = "SELECT isi FROM catatan WHERE pemilik = ?"
    return [isi for (isi,) in db.execute(sql, (pengguna,))]


print("tanpa aturan:", ambil_tanpa_aturan())
print("sari:", ambil_dengan_aturan("sari"))
print("budi:", ambil_dengan_aturan("budi"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tanpa aturan: ['PR matematika', 'sandi wifi rumah', 'beli tinta']",
                    "  sari: ['PR matematika', 'beli tinta']",
                    "  budi: ['sandi wifi rumah']",
                    "",
                    "Tanpa aturan, Sari ikut melihat kata sandi wifi rumah Budi. Kebocoran",
                    "data di aplikasi BaaS hampir selalu berawal di sini: tabel dibuat, RLS",
                    "lupa dinyalakan, dan API otomatis Supabase menyajikan semua isinya ke",
                    "siapa pun.",
                    "",
                    "Jebakan: Supabase memberi dua kunci. Kunci anon boleh ditaruh di",
                    "aplikasi karena dibatasi RLS. Kunci service_role melewati semua RLS,",
                    "jadi jangan pernah dikirim ke browser atau dimasukkan ke aplikasi",
                    "mobile. Simpan di server atau di Edge Function saja.",
                ],
            },
            {
                "heading": "Headless CMS: isi terpisah dari tampilan",
                "body": [
                    "CMS (content management system) adalah aplikasi untuk mengelola isi",
                    "situs tanpa menyentuh kode, contohnya WordPress. CMS tradisional",
                    "menyimpan isi sekaligus membuat halaman HTML-nya.",
                    "",
                    "Headless CMS cuma menyimpan isi dan menyajikannya lewat API, biasanya",
                    "berupa JSON. Kepalanya, yaitu bagian tampilan, dipotong. Satu sumber isi",
                    "bisa dipakai situs web, aplikasi mobile, dan layar di toko sekaligus:",
                ],
                "code": "import json\n\n\ndef content_api(slug):\n    # Di dunia nyata ini respons JSON dari Contentful, Strapi, atau Sanity\n    artikel = {\n        \"promo-buku\": {\"judul\": \"Promo Awal Semester\",\n                       \"isi\": \"Diskon 20% untuk semua buku tulis.\"},\n    }\n    return json.dumps(artikel[slug])\n\n\ndef tampil_terminal(data):\n    return f\"== {data['judul']} ==\\n{data['isi']}\"\n\n\ndef tampil_html(data):\n    return f\"<h1>{data['judul']}</h1>\\n<p>{data['isi']}</p>\"\n\n\ndata = json.loads(content_api(\"promo-buku\"))\nprint(tampil_terminal(data))\nprint(tampil_html(data))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  == Promo Awal Semester ==",
                    "  Diskon 20% untuk semua buku tulis.",
                    "  <h1>Promo Awal Semester</h1>",
                    "  <p>Diskon 20% untuk semua buku tulis.</p>",
                    "",
                    "Data yang sama tampil di dua tempat dengan bentuk berbeda, dan",
                    "content_api() nggak tahu apa-apa soal tampilannya. Pilihan headless CMS",
                    "yang sering kamu temui:",
                    "",
                    "  - Contentful: layanan cloud berbayar dengan paket gratis, banyak",
                    "    dipakai perusahaan besar.",
                    "  - Strapi: open source berbasis Node.js yang bisa dipasang di servermu",
                    "    sendiri. Edisi komunitasnya berlisensi MIT, versinya 5.58.0 per",
                    "    Oktober 2026.",
                    "  - Sanity: layanan cloud. Editornya, Sanity Studio, open source dan",
                    "    bisa diubah sesukamu.",
                    "  - Payload: open source berlisensi MIT yang dipasang langsung di dalam",
                    "    proyek Next.js.",
                    "",
                    "WordPress sendiri juga bisa dipakai secara headless lewat REST API",
                    "bawaannya.",
                ],
            },
            {
                "heading": "MACH: merakit dari layanan terbaik",
                "body": [
                    "Perusahaan besar membawa ide headless lebih jauh. Mereka menyusun",
                    "seluruh sistem dari layanan pilihan yang disambung lewat API.",
                    "Singkatannya diambil dari empat prinsip:",
                    "",
                    "  - Microservices: tiap kemampuan bisnis jadi layanan sendiri.",
                    "  - API-first: semua fitur bisa dipakai lewat API.",
                    "  - Cloud-native SaaS: layanan disewa dari cloud dan diperbarui",
                    "    penyedianya.",
                    "  - Headless: tampilan terpisah dari backend.",
                    "",
                    "Contoh susunannya untuk toko online besar: commercetools untuk keranjang",
                    "dan pesanan, Contentful atau Contentstack untuk isi, Algolia untuk",
                    "pencarian, Next.js atau Nuxt untuk frontend, lalu CDN di depannya.",
                    "",
                    "MACH Alliance, organisasi nirlaba yang mempromosikan cara ini, didirikan",
                    "Juni 2020 oleh commercetools, Contentstack, EPAM, dan Valtech. Situs",
                    "resminya (dicek Oktober 2026) mengklaim komunitas lebih dari 250.000",
                    "praktisi dan menjalankan program sertifikasi.",
                    "",
                    "Untuk pemula, nilai terbesarnya ada di dua ide: headless dan API-first.",
                    "Arsitektur komposabel penuh butuh banyak langganan layanan dan tim yang",
                    "mampu menyambungkan semuanya, jadi wajar kalau cuma dipakai perusahaan",
                    "besar.",
                ],
            },
            {
                "heading": "Membangun sendiri atau merakit?",
                "body": [
                    "Nggak ada jawaban yang selalu benar. Timbang lima hal ini:",
                    "",
                    "  Pertimbangan        Merakit (BaaS, SaaS)        Membangun sendiri",
                    "  ------------------  --------------------------  ---------------------",
                    "  Kecepatan awal      cepat, hitungan hari        lambat, berminggu-minggu",
                    "  Biaya saat besar    bisa melonjak per pemakai   lebih bisa ditekan",
                    "  Kendali data        di tangan penyedia          di tanganmu",
                    "  Pindah penyedia     sulit (lock-in)             nggak perlu pindah",
                    "  Kemampuan tim       cukup paham frontend        butuh orang backend",
                    "",
                    "Lock-in artinya terkunci ke satu penyedia karena pindah terlalu mahal.",
                    "Supabase relatif aman soal ini karena isinya PostgreSQL biasa yang bisa",
                    "dibawa ke server lain. Data di Firestore lebih sulit dipindah karena",
                    "bentuk dan cara query-nya khas Google.",
                    "",
                    "Jalan tengah yang sering dipakai: mulai dengan BaaS supaya cepat sampai",
                    "ke pengguna, tulis logika bisnis di fungsi terpisah, dan pantau",
                    "tagihannya. Kalau suatu saat biaya atau batasannya mengganggu, bagian",
                    "itu dipindah ke backend sendiri. Kurikulum Backend & API membahas cara",
                    "membangunnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "BaaS banyak dipakai untuk MVP startup, aplikasi mobile kecil, prototipe",
                    "saat hackathon, dan aplikasi internal sekolah atau kantor. Headless CMS",
                    "dipakai situs berita, toko online, dan situs perusahaan yang isinya",
                    "diurus tim nonprogrammer.",
                    "",
                    "Kasus kecil: pengurus ekskul jurnalistik ingin aplikasi pengumuman.",
                    "Siswa login untuk membaca, dan cuma pengurus yang boleh menulis. Nggak",
                    "ada anggota yang bisa membuat backend.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pilih Supabase karena datanya PostgreSQL biasa dan login email",
                    "     sudah tersedia.",
                    "  2. Buat tabel pengumuman dengan kolom judul, isi, dan ditulis_oleh,",
                    "     plus tabel pengurus berisi id pengguna yang boleh menulis.",
                    "  3. Nyalakan RLS di tabel pengumuman, lalu pasang dua policy:",
                    "       create policy \"siswa login boleh membaca\"",
                    "       on pengumuman for select to authenticated",
                    "       using (true);",
                    "",
                    "       create policy \"cuma pengurus boleh menulis\"",
                    "       on pengumuman for insert to authenticated",
                    "       with check ((select auth.uid()) in",
                    "         (select user_id from pengurus));",
                    "  4. Di aplikasi, pakai kunci anon saja. Kunci service_role nggak boleh",
                    "     ikut ke aplikasi.",
                    "  5. Uji dengan akun siswa biasa: membaca harus berhasil, menulis",
                    "     pengumuman harus ditolak.",
                ],
            },
        ],
    },
    {
        "title": "17. Peta Stack Lintas Ranah: Data, AI, Mobile, Pemantauan",
        "sections": [
            {
                "body": [
                    "Stack bernama nggak cuma ada di dunia web. Tim data, tim AI, tim mobile,",
                    "dan tim operasi server juga punya paket teknologi yang namanya sering",
                    "muncul di lowongan kerja dan di obrolan programmer.",
                    "",
                    "Materi ini sebuah peta. Kamu nggak perlu menguasai isinya sekarang.",
                    "Cukup kenali namanya, tahu tugasnya, dan tahu kurikulum mana di aplikasi",
                    "ini yang membahasnya sampai detail. Begitu nama-nama ini muncul lagi,",
                    "kamu sudah punya tempat untuk menaruhnya.",
                ],
            },
            {
                "heading": "Peta singkat",
                "body": [
                    "Enam stack bernama di luar web yang paling sering kamu dengar, beserta",
                    "isinya dan kurikulum yang membahasnya:",
                ],
                "bahasa": "teks",
                "code": """Stack                 Komponen inti                       Kurikulum
--------------------  ----------------------------------  ----------------
ELK                   Elasticsearch, Logstash, Kibana     DevOps & Cloud
Prometheus + Grafana  Prometheus, Grafana, Loki, Tempo    DevOps & Cloud
Modern Data Stack     gudang data, dbt, orkestrator, BI   Data & Analitik
LLM + RAG             API model, vektor, MCP              AI & ML
Flutter + Firebase    Flutter, Dart, Firebase             Mobile & Desktop
React Native + Expo   React Native, Expo SDK              Mobile & Desktop""",
            },
            {
                "heading": "Elastic Stack (ELK)",
                "body": [
                    "ELK adalah singkatan tiga program. Elasticsearch menyimpan data dan",
                    "mencarinya dengan cepat. Logstash mengolah data yang masuk, misalnya",
                    "memecah baris log jadi kolom. Kibana menampilkan dasbor dan grafik.",
                    "Belakangan ditambah Beats atau Elastic Agent yang mengirim log dari tiap",
                    "server. Ada juga varian EFK yang mengganti Logstash dengan Fluentd atau",
                    "Fluent Bit.",
                    "",
                    "Pemakaiannya ada tiga: pusat log dari banyak server, fitur pencarian di",
                    "situs, dan analitik keamanan (SIEM). Inti kecepatannya adalah indeks",
                    "terbalik, struktur yang memetakan tiap kata ke daftar dokumen yang",
                    "memuatnya. Versi mininya begini:",
                ],
                "code": """dokumen = {
    1: "server web lambat saat jam makan siang",
    2: "login gagal karena kata sandi salah",
    3: "server database penuh, login lambat",
}

# Indeks terbalik: kata -> himpunan nomor dokumen yang memuatnya
indeks = {}
for nomor, teks in dokumen.items():
    for kata in teks.replace(",", "").split():
        indeks.setdefault(kata, set()).add(nomor)


def cari(*kata):
    hasil = set(dokumen)
    for k in kata:
        hasil &= indeks.get(k, set())
    return sorted(hasil)


print("lambat       :", cari("lambat"))
print("login lambat :", cari("login", "lambat"))
print("server penuh :", cari("server", "penuh"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  lambat       : [1, 3]",
                    "  login lambat : [3]",
                    "  server penuh : [3]",
                    "",
                    "Mencari \"login lambat\" cukup mengiris dua himpunan, tanpa membaca ulang",
                    "semua dokumen. Elasticsearch melakukan hal yang sama untuk miliaran",
                    "baris, ditambah pemberian skor relevansi.",
                    "",
                    "Sejarah lisensinya contoh bagus kenapa lisensi perlu dicek sebelum",
                    "memilih teknologi:",
                    "",
                    "  sampai 2021  Apache-2.0",
                    "  2021         pindah ke SSPL atau Elastic License",
                    "  2024         menambah AGPL-3.0 sebagai pilihan",
                    "",
                    "Waktu lisensinya berubah di 2021, AWS dan komunitas membuat fork bernama",
                    "OpenSearch yang tetap Apache-2.0. Versinya 3.9.0 per Oktober 2026.",
                    "",
                    "Di Survei Stack Overflow 2026, Elasticsearch dipakai 14,8% responden di",
                    "kategori database. Di kategori enterprise search, yaitu mesin pencari",
                    "untuk data perusahaan, Elastic dipilih 37% dan OpenSearch 17% dari 2.746",
                    "penjawab. Kategori enterprise search lengkap, termasuk Apache Solr dan",
                    "Algolia, dibahas di kurikulum Database & Penyimpanan Data.",
                ],
            },
            {
                "heading": "Prometheus dan Grafana (keluarga LGTM)",
                "body": [
                    "Prometheus mengumpulkan metrik, yaitu angka yang berubah sepanjang",
                    "waktu: jumlah request, persentase CPU, jumlah error. Caranya menarik:",
                    "tiap beberapa detik Prometheus membuka alamat /metrics di aplikasimu,",
                    "yang isinya baris teks seperti ini:",
                    "",
                    "  http_requests_total{method=\"GET\",status=\"200\"} 1027",
                    "  http_requests_total{method=\"GET\",status=\"500\"} 3",
                    "",
                    "Grafana menampilkan angka-angka itu sebagai dasbor dan mengirim",
                    "peringatan. Grafana Labs juga membuat Loki untuk log, Tempo untuk trace,",
                    "dan Mimir untuk metrik skala besar. Gabungannya sering disebut LGTM:",
                    "Loki, Grafana, Tempo, Mimir. Prometheus berlisensi Apache-2.0 dan",
                    "merupakan proyek CNCF. Grafana, Loki, Tempo, dan Mimir memakai lisensi",
                    "Affero GPL versi 3.",
                    "",
                    "Datanya ditanya dengan bahasa query bernama PromQL. Contoh berikut",
                    "menghitung laju error 500 per detik selama lima menit terakhir,",
                    "dikelompokkan per layanan:",
                ],
                "bahasa": "promql",
                "code": "sum by (layanan) (rate(http_requests_total{status=\"500\"}[5m]))",
            },
            {
                "heading": "Modern Data Stack",
                "body": [
                    "Ini label industri, bukan nama produk. Isinya rangkaian layanan untuk",
                    "analitik. Data dari banyak sumber, misalnya database aplikasi, iklan,",
                    "dan spreadsheet, dimuat ke gudang data. Sesudah itu baru diolah dengan",
                    "SQL. Urutan \"muat dulu, olah belakangan\" ini disebut ELT. Komponennya:",
                    "",
                    "  - Gudang data: Snowflake, BigQuery, Databricks, Amazon Redshift,",
                    "    ClickHouse, dan DuckDB untuk skala kecil.",
                    "  - Pemuat data: Fivetran dan Airbyte.",
                    "  - Transformasi: dbt, yang membuat query SQL bisa dites dan diberi",
                    "    versi seperti kode. dbt-core berlisensi Apache-2.0, versinya 1.12.6",
                    "    per Oktober 2026.",
                    "  - Orkestrasi: Airflow, Dagster, Prefect, yang menjadwalkan semua",
                    "    langkah.",
                    "  - BI: Power BI, Looker, Metabase, untuk dasbor manajemen.",
                    "",
                    "Survei Stack Overflow 2026 mencatat BigQuery 7%, DuckDB 6%, Snowflake",
                    "5%, Databricks SQL 4%, ClickHouse 4%, dan Redshift 2%. Semua ini dibahas",
                    "di kurikulum Data & Analitik. Library data Python seperti NumPy dan",
                    "pandas, yang dulu muncul di kategori other frameworks Survei Stack",
                    "Overflow 2024, juga tinggal di sana.",
                ],
            },
            {
                "heading": "Stack aplikasi LLM dan RAG",
                "body": [
                    "LLM (large language model) adalah model AI yang membaca dan menulis",
                    "teks. Aplikasi berbasis LLM, misalnya chatbot yang menjawab dari dokumen",
                    "perusahaan, biasanya memakai susunan ini:",
                    "",
                    "  - API model: Anthropic, OpenAI, Google, dan penyedia lain.",
                    "  - Orkestrasi: LangChain (versi 1.4.6 per Oktober 2026), LangGraph,",
                    "    LlamaIndex, OpenAI Agents SDK.",
                    "  - Pencarian vektor: pgvector (ekstensi PostgreSQL, versi 0.8.7),",
                    "    Chroma, Pinecone, Qdrant.",
                    "  - MCP (Model Context Protocol): standar untuk menyambungkan model ke",
                    "    alat dan sumber data. Spesifikasi terbarunya bertanggal 28 Juli",
                    "    2026, berlisensi MIT.",
                    "  - Observabilitas khusus LLM: LangSmith, Langfuse.",
                    "",
                    "RAG (retrieval-augmented generation) artinya model nggak menjawab dari",
                    "ingatannya saja. Aplikasi mencari dulu paragraf yang relevan dari",
                    "dokumenmu, lalu menempelkannya ke pertanyaan sebelum dikirim ke model.",
                    "Pencarian vektor dipakai di langkah mencari itu.",
                    "",
                    "Di Survei Stack Overflow 2026, penyedia model yang paling banyak dipakai",
                    "penjawab adalah Anthropic (74,6%) dan OpenAI (74,3%), disusul Google AI",
                    "(54,5%). Ekosistem ini berubah tiap beberapa bulan, jadi angka dan nama",
                    "alatnya cepat basi. Detailnya, termasuk PyTorch dan TensorFlow, dibahas",
                    "di kurikulum AI & Machine Learning.",
                ],
            },
            {
                "heading": "Flutter + Firebase dan React Native + Expo",
                "body": [
                    "Dua pasangan ini paling sering dipakai untuk membuat aplikasi Android",
                    "dan iOS dari satu kode.",
                    "",
                    "Flutter buatan Google memakai bahasa Dart. Satu kode bisa jadi aplikasi",
                    "Android, iOS, web, dan desktop. Lisensinya BSD-3-Clause, versi stabilnya",
                    "3.47 per Oktober 2026. Pasangannya Firebase untuk login, Firestore, dan",
                    "notifikasi push, jadi tim kecil bisa merilis aplikasi tanpa menulis",
                    "backend.",
                    "",
                    "React Native buatan Meta memakai JavaScript atau TypeScript dengan gaya",
                    "React. Expo adalah framework di atasnya yang memudahkan memulai, menguji",
                    "di ponsel, dan membangun aplikasi. Keduanya berlisensi MIT. Expo SDK 58,",
                    "yang memakai React Native 0.88, terbit Oktober 2026. Layanan build cloud",
                    "milik Expo berbayar dengan kuota gratis.",
                    "",
                    "Di Survei Stack Overflow 2024, kategori other frameworks mencatat",
                    "Flutter 9,4% dan React Native 8,4%. Kategori itu juga memuat SwiftUI,",
                    ".NET MAUI, Electron, dan Tauri. Semuanya milik kurikulum Mobile &",
                    "Desktop. Spring dan .NET dari kategori yang sama milik kurikulum Backend",
                    "& API, sedangkan RabbitMQ dan Kafka dibahas di bab Arsitektur",
                    "Terdistribusi kurikulum ini.",
                ],
            },
            {
                "heading": "Cara memakai peta ini",
                "body": [
                    "Waktu bertemu nama stack yang asing, ajukan empat pertanyaan:",
                    "",
                    "  1. Lapisan mana yang diurusnya: tampilan, logika, data, atau",
                    "     infrastruktur?",
                    "  2. Ranahnya apa: web, mobile, data, AI, atau operasi?",
                    "  3. Lisensinya apa, dan pernah berubah atau nggak?",
                    "  4. Siapa yang merawatnya: perusahaan, yayasan, atau komunitas?",
                    "",
                    "Jawaban keempatnya biasanya sudah cukup untuk memutuskan perlu",
                    "dipelajari sekarang atau nanti. Kamu nggak harus bisa semuanya. Pilih",
                    "ranah yang sesuai peran yang kamu incar, dan biarkan sisanya jadi peta.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan kerja sering mencampur stack dari beberapa ranah dalam satu",
                    "kalimat. Contohnya lowongan pengembang aplikasi mobile yang meminta",
                    "Flutter dan Firebase, lalu menambahkan \"paham Grafana\" dan \"pernah",
                    "memakai pgvector\" sebagai nilai tambah.",
                    "",
                    "Kasus kecil: kamu menemukan lowongan magang dengan daftar \"Flutter,",
                    "Firebase, Grafana, pgvector\" dan bingung harus mulai belajar dari mana.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Petakan tiap istilah dengan tabel di atas. Flutter dan Firebase",
                    "     masuk mobile, Grafana masuk pemantauan, pgvector masuk AI dan",
                    "     database.",
                    "  2. Baca deskripsi pekerjaannya. Kalau tugas utamanya \"membangun fitur",
                    "     aplikasi\", ranah intinya mobile.",
                    "  3. Urutkan belajarmu: kurikulum Mobile & Desktop dulu, lalu dasar",
                    "     pemantauan di DevOps & Cloud, lalu pencarian vektor di AI & Machine",
                    "     Learning kalau masih ada waktu.",
                    "  4. Bikin satu proyek kecil yang memakai pasangan utamanya, misalnya",
                    "     aplikasi catatan dengan Flutter dan Firebase.",
                    "  5. Di CV, tulis hanya yang sudah pernah kamu coba sendiri, dan",
                    "     sebutkan proyeknya.",
                ],
            },
        ],
    },
    {
        "title": "18. Piramida Tes, TDD, dan BDD",
        "sections": [
            {
                "body": [
                    "Tes otomatis adalah program yang memeriksa programmu. Kamu menulis",
                    "\"kalau fungsinya diberi ini, hasilnya harus itu\", lalu komputer mengecek",
                    "semuanya dalam hitungan detik, setiap kali kode berubah.",
                    "",
                    "Kamu sudah sering bertemu tes otomatis di aplikasi ini. Waktu kamu",
                    "mengirim jawaban latihan, aplikasi menjalankan kodemu lalu mencocokkan",
                    "keluarannya dengan kunci jawaban. Itu tes.",
                    "",
                    "Gunanya terasa saat aplikasi membesar. Perubahan kecil di satu tempat",
                    "bisa merusak tempat lain yang nggak kamu sentuh. Tanpa tes, kerusakan",
                    "itu baru ketahuan waktu pengguna mengeluh. Dengan tes, kerusakannya",
                    "ketahuan sebelum kodenya digabung.",
                ],
            },
            {
                "heading": "Tiga tingkat tes",
                "body": [
                    "  - Tes unit: menguji satu fungsi atau satu kelas, terpisah dari",
                    "    database dan jaringan. Jalannya hitungan milidetik, jadi kamu bisa",
                    "    punya ribuan.",
                    "  - Tes integrasi: menguji beberapa bagian sekaligus, misalnya kodemu",
                    "    bersama database sungguhan. Lebih lambat, tapi menangkap salah",
                    "    sambung yang lolos dari tes unit.",
                    "  - Tes end-to-end: menguji aplikasi utuh seperti pengguna memakainya,",
                    "    misalnya membuka browser, mengisi formulir, lalu menekan tombol.",
                    "    Paling meyakinkan, tapi paling lambat dan paling gampang gagal",
                    "    karena hal sepele.",
                    "",
                    "Piramida tes adalah pedoman porsinya. Mike Cohn mempopulerkannya lewat",
                    "buku Succeeding with Agile (2009). Dasarnya yang lebar diisi banyak tes",
                    "unit, bagian tengahnya tes integrasi secukupnya, dan puncaknya sedikit",
                    "tes end-to-end. Artikel Ham Vocke \"The Practical Test Pyramid\" (2018) di",
                    "martinfowler.com menambahkan satu saran: dorong tiap pemeriksaan ke",
                    "tingkat serendah mungkin yang masih bisa menangkap masalahnya.",
                    "",
                    "Ada juga gambar tandingan bernama testing trophy, dipopulerkan Kent C.",
                    "Dodds untuk aplikasi JavaScript. Bentuknya piala: tes integrasi paling",
                    "banyak, ditopang analisis statis seperti linter di bagian paling bawah.",
                    "Dua gambar ini berbeda soal bagian tengahnya, tapi sepakat soal",
                    "ujungnya: tes yang lambat dan rapuh cukup sedikit.",
                ],
            },
            {
                "heading": "Tes unit dengan unittest",
                "body": [
                    "Python punya modul unittest bawaan. Contoh di bawah menguji fungsi",
                    "ongkir dengan dua aturan: belanja mulai 100 ribu gratis ongkir, di",
                    "bawahnya kena 5.000 ditambah 2.000 per km. Setiap metode yang namanya",
                    "diawali test_ adalah satu tes.",
                ],
                "code": """import io
import unittest


def ongkir(total_belanja, jarak_km):
    if total_belanja >= 100_000:
        return 0
    return 5_000 + 2_000 * jarak_km


class TestOngkir(unittest.TestCase):
    def test_gratis_mulai_100rb(self):
        self.assertEqual(ongkir(100_000, 7), 0)

    def test_di_bawah_100rb_dihitung_per_km(self):
        self.assertEqual(ongkir(50_000, 3), 11_000)

    def test_jarak_nol_tetap_bayar_ongkos_dasar(self):
        self.assertEqual(ongkir(20_000, 0), 5_000)


# Biasanya cukup "python3 -m unittest" di terminal. Di sini hasilnya
# dirangkum manual supaya keluarannya sama setiap kali dijalankan.
rangkaian = unittest.defaultTestLoader.loadTestsFromTestCase(TestOngkir)
hasil = unittest.TextTestRunner(stream=io.StringIO()).run(rangkaian)
print("tes dijalankan:", hasil.testsRun)
print("gagal:", len(hasil.failures), "| error:", len(hasil.errors))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tes dijalankan: 3",
                    "  gagal: 0 | error: 0",
                    "",
                    "Di proyek sungguhan, tesnya disimpan di berkas sendiri, misalnya",
                    "test_ongkir.py, lalu dijalankan dengan perintah python3 -m unittest.",
                    "Bagian TextTestRunner di contoh cuma ada supaya hasilnya bisa dicetak",
                    "rapi di aplikasi ini.",
                    "",
                    "Di dunia Python, pytest lebih populer daripada unittest. Survei Stack",
                    "Overflow 2026 mencatat pytest dipakai 28% responden. Tes pytest cukup",
                    "berupa fungsi biasa dengan assert:",
                    "",
                    "  def test_gratis_mulai_100rb():",
                    "      assert ongkir(100_000, 7) == 0",
                    "",
                    "  def test_di_bawah_100rb_dihitung_per_km():",
                    "      assert ongkir(50_000, 3) == 11_000",
                    "",
                    "Nama tes yang bagus menjelaskan aturannya. Kalau",
                    "test_jarak_nol_tetap_bayar_ongkos_dasar gagal, kamu langsung tahu aturan",
                    "mana yang rusak tanpa membuka kodenya.",
                ],
            },
            {
                "heading": "TDD: tulis tesnya dulu",
                "body": [
                    "Test-driven development, atau TDD, membalik urutan biasa. Tesnya ditulis",
                    "lebih dulu, baru kodenya. Kent Beck mempopulerkan cara ini lewat Extreme",
                    "Programming di akhir 1990-an. Siklusnya pendek dan diulang terus:",
                    "",
                    "  1. Red: tulis satu tes untuk perilaku yang belum ada, jalankan, dan",
                    "     pastikan tes itu gagal. Tes yang langsung lulus berarti tesnya",
                    "     nggak menguji apa-apa.",
                    "  2. Green: tulis kode secukupnya supaya tes itu lulus. Boleh jelek",
                    "     dulu.",
                    "  3. Refactor: rapikan kodenya tanpa mengubah perilaku, sambil",
                    "     memastikan semua tes tetap lulus.",
                    "",
                    "Misalnya toko minta aturan baru: member dapat potongan ongkir 50%. Kamu",
                    "mulai dengan tes yang memanggil ongkir(50_000, 3, member=True) dan",
                    "mengharapkan 5_500. Tes itu gagal karena parameter member belum ada",
                    "(red). Kamu menambah parameternya dan membagi dua hasilnya (green).",
                    "Terakhir, angka 50 kamu pindahkan ke konstanta bernama supaya jelas",
                    "artinya (refactor).",
                    "",
                    "Manfaat TDD paling terasa untuk logika bisnis yang rumit dan untuk",
                    "memperbaiki bug: tulis dulu tes yang mereproduksi bug-nya, baru perbaiki",
                    "kodenya. Untuk eksplorasi tampilan atau prototipe yang akan dibuang,",
                    "menulis tes lebih dulu sering cuma memperlambat.",
                ],
            },
            {
                "heading": "BDD dan Gherkin",
                "body": [
                    "Behavior-driven development (BDD) lahir dari TDD dengan satu tambahan:",
                    "perilaku sistem disepakati bersama orang nonprogrammer lewat contoh",
                    "konkret. Contohnya ditulis dalam format Gherkin, kalimat biasa yang",
                    "diawali Given, When, dan Then:",
                    "",
                    "  Feature: Ongkos kirim",
                    "    Scenario: Belanja mulai 100 ribu gratis ongkir",
                    "      Given keranjang berisi barang senilai 120000",
                    "      When pembeli memilih alamat berjarak 7 km",
                    "      Then ongkos kirim yang tampil adalah 0",
                    "",
                    "Cucumber membagi BDD jadi tiga kegiatan: discovery (menemukan contoh",
                    "lewat diskusi), formulation (menuliskannya dalam Gherkin), dan",
                    "automation (menyambungkannya ke kode). Bagian otomasinya kira-kira",
                    "begini: tiap kalimat dicocokkan ke sebuah fungsi lewat pola teks.",
                ],
                "code": "import re\n\nlangkah = []\nkonteks = {}\n\n\ndef step(pola):\n    def daftarkan(fungsi):\n        langkah.append((re.compile(pola), fungsi))\n        return fungsi\n    return daftarkan\n\n\n@step(r\"keranjang berisi barang senilai (\\d+)\")\ndef isi_keranjang(nilai):\n    konteks[\"total\"] = int(nilai)\n\n\n@step(r\"alamat berjarak (\\d+) km\")\ndef pilih_alamat(km):\n    total = konteks[\"total\"]\n    konteks[\"ongkir\"] = 0 if total >= 100_000 else 5_000 + 2_000 * int(km)\n\n\n@step(r\"ongkos kirim yang tampil adalah (\\d+)\")\ndef cek_ongkir(harapan):\n    assert konteks[\"ongkir\"] == int(harapan), konteks[\"ongkir\"]\n\n\nskenario = \"\"\"\nGiven keranjang berisi barang senilai 120000\nWhen pembeli memilih alamat berjarak 7 km\nThen ongkos kirim yang tampil adalah 0\n\"\"\"\n\nfor baris in skenario.strip().splitlines():\n    for pola, fungsi in langkah:\n        cocok = pola.search(baris)\n        if cocok:\n            fungsi(*cocok.groups())\n            print(\"lulus:\", baris)\n            break",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  lulus: Given keranjang berisi barang senilai 120000",
                    "  lulus: When pembeli memilih alamat berjarak 7 km",
                    "  lulus: Then ongkos kirim yang tampil adalah 0",
                    "",
                    "Alat sungguhannya bekerja dengan cara yang sama. Cucumber (dipakai 5%",
                    "responden Survei Stack Overflow 2026) tersedia untuk banyak bahasa,",
                    "Behave untuk Python, Reqnroll sebagai penerus SpecFlow untuk .NET, dan",
                    "Robot Framework (2%) populer di tim QA.",
                    "",
                    "Manfaat BDD datang dari diskusinya. Kalau berkas Gherkin cuma ditulis",
                    "programmer sendirian, hasilnya tes biasa dengan kalimat yang lebih",
                    "panjang.",
                ],
            },
            {
                "heading": "Alat tes yang paling banyak dipakai",
                "body": [
                    "Survei Stack Overflow 2026 punya kategori code testing tools. Angka di",
                    "bawah adalah persen responden yang memakainya:",
                    "",
                    "  Kebutuhan                 Alat (persen pemakai)",
                    "  ------------------------  ----------------------------------------",
                    "  Tes unit Python           pytest 28%, unittest (bawaan)",
                    "  Tes unit JavaScript/TS    Jest 21%, Vitest 19%, Mocha 5%",
                    "  Tes unit Java             JUnit 21%, TestNG",
                    "  Tes unit C#               xUnit.net 11%, NUnit 9%, MSTest",
                    "  Tes unit Ruby dan PHP     RSpec 4%, PHPUnit 1%",
                    "  End-to-end di browser     Playwright 25%, Selenium 12%, Cypress 8%",
                    "  Uji API                   Postman/Newman 33%, Bruno 1%",
                    "  Integrasi dengan database Testcontainers 8%",
                    "  Uji beban                 k6",
                    "  BDD                       Cucumber 5%, Robot Framework 2%",
                    "",
                    "Dua hal terbaca dari tabel itu. Pertama, alat tes terikat bahasanya,",
                    "jadi pelajari yang cocok dengan bahasa yang kamu pakai. Kedua,",
                    "Playwright sekarang dipakai dua kali lebih banyak daripada Selenium",
                    "untuk tes browser. Per Oktober 2026 versi Playwright 1.64.1, Vitest",
                    "5.0.5, dan Jest 30.5.2.",
                    "",
                    "Kategori yang sama juga memuat alat pemantauan seperti Sentry dan",
                    "Datadog, serta alat review berbasis AI. Daftar lengkapnya dibahas sesuai",
                    "ranahnya di kurikulum Frontend Modern, Backend & API, dan DevOps &",
                    "Cloud.",
                ],
            },
            {
                "heading": "Jebakan saat mulai menulis tes",
                "body": [
                    "  - Mengejar coverage 100%. Coverage cuma mengukur baris mana yang",
                    "    pernah dijalankan tes, belum tentu hasilnya diperiksa. Tes tanpa",
                    "    assert pun bisa memberi coverage tinggi.",
                    "  - Tes yang bergantung pada jam, angka acak, atau urutan jalan. Tes",
                    "    seperti ini kadang lulus kadang gagal (disebut flaky), dan lama-lama",
                    "    orang berhenti percaya pada tesnya.",
                    "  - Menguji detail dalaman. Tes yang memeriksa urutan panggilan internal",
                    "    akan rusak setiap kali kode dirapikan, padahal perilakunya sama",
                    "    saja.",
                    "  - Terlalu banyak tes end-to-end. Rangkaian tes yang butuh 40 menit",
                    "    membuat orang malas menjalankannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua proyek tim memasang tes di CI (continuous integration),",
                    "yaitu server yang menjalankan seluruh tes setiap ada pull request. Toko",
                    "online, aplikasi kasir, dan pustaka open source di GitHub biasanya",
                    "menolak perubahan yang membuat satu tes saja gagal.",
                    "",
                    "Kasus kecil: seorang pembeli komplain. Belanjanya pas Rp100.000, tapi",
                    "tetap kena ongkir, padahal promonya berbunyi \"gratis ongkir mulai 100",
                    "ribu\".",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tulis dulu tes yang mereproduksi keluhannya:",
                    "       def test_pas_100rb_gratis(self):",
                    "           self.assertEqual(ongkir(100_000, 7), 0)",
                    "  2. Jalankan tesnya. Kalau gagal, berarti bug-nya berhasil ditangkap",
                    "     (red).",
                    "  3. Cari penyebabnya. Biasanya pembandingnya tertulis total_belanja >",
                    "     100_000, padahal aturannya \"mulai 100 ribu\", jadi harusnya >=.",
                    "  4. Perbaiki, lalu jalankan semua tes. Tes baru harus lulus, dan nggak",
                    "     boleh ada tes lama yang rusak (green).",
                    "  5. Commit tes itu bersama perbaikannya. Kalau suatu hari ada yang",
                    "     mengubah pembanding itu lagi, tes ini langsung menangkapnya.",
                ],
            },
        ],
    },
    {
        "title": "19. Code Review, Pair Programming, dan Linting",
        "sections": [
            {
                "body": [
                    "Code review artinya perubahan kodemu dibaca orang lain sebelum digabung",
                    "ke cabang utama. Di GitHub wadahnya disebut pull request (PR), di GitLab",
                    "namanya merge request. Isinya sama: daftar perubahan, deskripsi, dan",
                    "tempat berdiskusi baris demi baris.",
                    "",
                    "Tujuannya ada tiga. Bug tertangkap sebelum sampai ke pengguna. Kode",
                    "tetap bisa dibaca orang lain, termasuk dirimu enam bulan lagi.",
                    "Pengetahuan menyebar, jadi nggak ada bagian aplikasi yang cuma dipahami",
                    "satu orang.",
                    "",
                    "Yang ditinjau kodenya, bukan orangnya. Komentar \"fungsi ini menjalankan",
                    "query yang sama di dalam loop\" membantu. Komentar \"kok bisa nulis",
                    "begini\" nggak membantu siapa pun.",
                ],
            },
            {
                "heading": "Alur pull request",
                "body": [
                    "Alur yang dipakai hampir semua tim di GitHub kira-kira begini:",
                    "",
                    "  1. Buat cabang baru dari main untuk satu perubahan.",
                    "  2. Commit perubahanmu dalam langkah kecil yang masuk akal.",
                    "  3. Push cabangnya, lalu buka pull request dengan deskripsi: apa yang",
                    "     berubah, kenapa, dan cara mengujinya.",
                    "  4. CI menjalankan tes dan linter secara otomatis.",
                    "  5. Peninjau membaca dan berkomentar. Kamu memperbaiki, lalu peninjau",
                    "     melihat lagi.",
                    "  6. Setelah disetujui dan CI hijau, cabang digabung ke main, lalu",
                    "     dihapus.",
                    "",
                    "Perintahnya di terminal, dengan gh sebagai alat baris perintah resmi",
                    "GitHub:",
                ],
                "bahasa": "terminal",
                "code": """git switch -c perbaiki-ongkir
git commit -am "fix: gratis ongkir mulai tepat 100 ribu"
git push -u origin perbaiki-ongkir
gh pr create --fill""",
            },
            {
                "heading": "Yang dicari peninjau",
                "body": [
                    "Panduan code review milik Google (google.github.io/eng-practices)",
                    "terbuka untuk umum dan banyak dijadikan acuan. Isinya dua bagian: How to",
                    "do a code review untuk peninjau, dan The CL author's guide untuk penulis",
                    "perubahan. CL (changelist) adalah istilah Google untuk satu paket",
                    "perubahan, setara dengan pull request.",
                    "",
                    "Peninjau diminta memeriksa hal-hal ini:",
                    "",
                    "  - Desain: apakah perubahannya masuk akal dan ditaruh di tempat yang",
                    "    tepat.",
                    "  - Fungsionalitas: apakah kodenya melakukan yang dimaksud, termasuk di",
                    "    kasus batas.",
                    "  - Kerumitan: apakah ada bagian yang bisa dibuat lebih sederhana.",
                    "  - Tes: apakah ada tes yang benar dan berguna.",
                    "  - Penamaan dan komentar: nama yang jelas, dan komentar yang",
                    "    menjelaskan alasan.",
                    "  - Gaya dan dokumentasi: sesuai panduan gaya tim, dan dokumentasi ikut",
                    "    diperbarui.",
                    "",
                    "Patokan persetujuannya: setujui kalau perubahan itu jelas memperbaiki",
                    "kesehatan kode secara keseluruhan, walaupun belum sempurna. Peninjau",
                    "yang menunggu kesempurnaan membuat tim berhenti bergerak. Soal",
                    "kecepatan, panduan itu menulis bahwa satu hari kerja adalah waktu paling",
                    "lama untuk merespons permintaan review.",
                    "",
                    "Komentar yang baik spesifik dan menyebut alasannya. Saran kecil yang",
                    "boleh diabaikan diberi awalan \"Nit:\" supaya penulisnya tahu mana yang",
                    "wajib. Contohnya untuk perubahan ini:",
                    "",
                    "  -    if total_belanja > 100_000:",
                    "  +    if total_belanja >= 100_000:",
                    "           return 0",
                    "",
                    "  Kurang membantu  \"Salah.\"",
                    "  Membantu         \"Promonya 'mulai 100 ribu', jadi 100.000",
                    "                    harus gratis. Tolong tambahkan tes untuk",
                    "                    angka 100.000 juga.\"",
                    "  Saran kecil      \"Nit: 100_000 bisa jadi konstanta",
                    "                    BATAS_GRATIS_ONGKIR.\"",
                ],
            },
            {
                "heading": "Kalau kamu yang menulis perubahan",
                "body": [
                    "  - Bikin PR kecil. Panduan Google menyarankan perubahan kecil karena",
                    "    lebih cepat ditinjau, lebih teliti dibaca, dan lebih gampang",
                    "    dibatalkan kalau bermasalah.",
                    "  - Tulis deskripsi yang menjawab apa dan kenapa. Peninjau nggak ikut",
                    "    berada di kepalamu waktu kamu menulis kodenya.",
                    "  - Tinjau sendiri diff-mu sebelum meminta orang lain. Sisa print()",
                    "    untuk debugging dan berkas yang nggak sengaja ikut biasanya ketahuan",
                    "    di sini.",
                    "  - Tanggapi semua komentar, walau cuma dengan \"sudah diperbaiki\" atau",
                    "    penjelasan kenapa kamu memilih cara lain.",
                    "  - Pisahkan perubahan gaya, misalnya merapikan spasi atau mengganti",
                    "    nama secara massal, dari perubahan perilaku. Dengan begitu bagian",
                    "    yang penting nggak tenggelam.",
                ],
            },
            {
                "heading": "Pair programming dan mob programming",
                "body": [
                    "Pair programming adalah dua orang mengerjakan kode yang sama di satu",
                    "layar. Satu orang jadi driver yang mengetik. Satunya jadi navigator yang",
                    "memikirkan arah, membaca setiap baris, dan mengingatkan kalau ada yang",
                    "terlewat. Perannya ditukar secara berkala supaya dua-duanya tetap fokus.",
                    "",
                    "Mob programming, yang sekarang juga disebut ensemble programming,",
                    "membawa ide yang sama ke satu tim. Semua orang menghadap satu layar,",
                    "satu orang mengetik, sisanya mengarahkan.",
                    "",
                    "Cara ini mahal di jam kerja, tapi menyelesaikan beberapa hal sekaligus.",
                    "Review terjadi saat kode ditulis, anggota baru belajar langsung dari",
                    "yang senior, dan pengetahuan soal bagian sulit nggak menumpuk di satu",
                    "kepala. Banyak tim memakainya untuk masalah yang sulit dan untuk",
                    "membimbing anggota baru, nggak untuk semua pekerjaan.",
                    "",
                    "Asisten AI sering disebut teman pair programming. Bedanya, AI cuma bisa",
                    "jadi driver yang cepat mengetik. Peran navigator, yang memutuskan arah",
                    "dan memeriksa kebenarannya, tetap di tanganmu.",
                ],
            },
            {
                "heading": "Linter, formatter, dan analisis statis",
                "body": [
                    "Sebagian besar komentar review soal gaya bisa diserahkan ke mesin. Ada",
                    "tiga jenis alat yang memeriksa kode tanpa menjalankannya:",
                    "",
                    "  - Linter mencari kesalahan dan kebiasaan buruk: variabel yang nggak",
                    "    dipakai, import ganda, perbandingan yang selalu benar.",
                    "  - Formatter merapikan tampilan kode secara otomatis, seperti spasi,",
                    "    indentasi, dan panjang baris, sehingga seluruh tim punya gaya yang",
                    "    sama.",
                    "  - Analisis statis mencari bug dan celah keamanan yang lebih dalam,",
                    "    misalnya data dari pengguna yang langsung masuk ke query SQL.",
                    "",
                    "Cara kerja linter sederhana: baca kode baris demi baris, lalu cocokkan",
                    "dengan aturan. Program di bawah memeriksa tiga aturan dari panduan gaya",
                    "Python. Kodenya (E501, W291, W191) sama dengan yang dipakai pycodestyle",
                    "dan Ruff:",
                ],
                "code": "BATAS = 79\n\n\ndef periksa(sumber):\n    temuan = []\n    for nomor, baris in enumerate(sumber.splitlines(), 1):\n        if \"\\t\" in baris:\n            temuan.append((nomor, \"W191\", \"indentasi memakai tab\"))\n        if baris != baris.rstrip():\n            temuan.append((nomor, \"W291\", \"ada spasi di ujung baris\"))\n        if len(baris) > BATAS:\n            temuan.append((nomor, \"E501\", f\"panjang {len(baris)} > {BATAS}\"))\n    return temuan\n\n\ncontoh = (\n    \"def luas(p, l):\\n\"\n    \"\\treturn p * l \\n\"\n    \"print('luas kamar tidur utama di rumah nenek, dalam meter persegi:', \"\n    \"luas(4, 5))\\n\"\n)\nfor nomor, kode, pesan in periksa(contoh):\n    print(f\"baris {nomor}: {kode} {pesan}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  baris 2: W191 indentasi memakai tab",
                    "  baris 2: W291 ada spasi di ujung baris",
                    "  baris 3: E501 panjang 80 > 79",
                    "",
                    "Alat sungguhannya memeriksa ratusan aturan sekaligus:",
                    "",
                    "  Alat       Untuk                   Catatan (Oktober 2026)",
                    "  ---------  ----------------------  -------------------------------",
                    "  ESLint     linter JS/TS            10.13.0, MIT",
                    "  Prettier   formatter JS, CSS, dll  3.9.10, MIT",
                    "  Biome      linter + formatter JS   2.5.15, satu alat untuk dua",
                    "  Ruff       linter + formatter Py   ditulis dengan Rust",
                    "  gofmt      formatter Go            bawaan Go",
                    "  SonarQube  analisis statis         Community Build, LGPL-3.0",
                    "  CodeQL     analisis keamanan       buatan GitHub",
                    "  Semgrep    analisis pola           aturannya bisa ditulis sendiri",
                    "",
                    "ESLint dipakai 37% responden Survei Stack Overflow 2026, angka tertinggi",
                    "di seluruh kategori code testing tools. SonarQube 19%, CodeQL 5%, dan",
                    "Semgrep 2%. Biasanya alat ini dipasang di dua tempat: di editor supaya",
                    "kamu langsung melihat garis merah, dan di CI supaya PR yang melanggar",
                    "ditolak otomatis. Peninjau manusia jadi bisa fokus ke logika dan desain.",
                    "",
                    "Jebakan: menyalakan semua aturan sekaligus di proyek lama menghasilkan",
                    "ribuan peringatan, dan semua orang belajar mengabaikannya. Mulai dari",
                    "aturan yang paling penting, rapikan seluruh kode sekali dengan",
                    "formatter, lalu tambah aturan sedikit demi sedikit.",
                ],
            },
            {
                "heading": "Peninjau berbasis AI",
                "body": [
                    "Sekarang ada alat yang memberi komentar review otomatis di PR memakai",
                    "model AI. Survei Stack Overflow 2026 mencatat CodeRabbit dipakai 6%",
                    "responden, Graphite 2%, lalu Greptile, Qodo, dan Sourcery masing-masing",
                    "1%.",
                    "",
                    "Alat seperti ini cepat menemukan salah ketik, kasus kosong yang terlupa,",
                    "atau nama yang menyesatkan. Tapi ia juga bisa yakin sekali pada saran",
                    "yang keliru, dan ia nggak tahu alasan bisnis di balik perubahanmu.",
                    "Perlakukan komentarnya seperti komentar rekan baru yang rajin: dibaca,",
                    "dipertimbangkan, dan boleh ditolak. Keputusan merge tetap di tangan",
                    "manusia yang paham konteksnya.",
                    "",
                    "Platform tempat semua ini terjadi didominasi GitHub, yang dipakai 70%",
                    "responden survei yang sama di kategori platform komunitas. GitLab dan",
                    "Azure DevOps punya fitur review yang setara.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek open source di GitHub dan tim startup umumnya memasang aturan",
                    "cabang terlindungi. Cabang main nggak bisa di-push langsung, setiap PR",
                    "wajib disetujui minimal satu orang, dan semua pemeriksaan CI harus hijau",
                    "sebelum tombol merge aktif.",
                    "",
                    "Kasus kecil: temanmu membuka PR berisi fitur diskon member. Perubahannya",
                    "400 baris di 9 berkas, tanpa deskripsi dan tanpa tes, lalu kamu diminta",
                    "meninjaunya.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Minta deskripsi dulu: apa aturan diskonnya, dan dari mana aturan",
                    "     itu datang.",
                    "  2. Cek hasil CI. Kalau linter atau tes gagal, minta diperbaiki sebelum",
                    "     kamu membaca logikanya.",
                    "  3. Baca bagian yang menghitung diskon lebih dulu. Coba kasus batas di",
                    "     kepala: total nol, member tanpa riwayat belanja, dan diskon yang",
                    "     membuat total negatif.",
                    "  4. Minta tes untuk aturan itu, dan tulis komentarmu spesifik:",
                    "       Diskon 10% bisa membuat total turun di bawah batas",
                    "       gratis ongkir. Apakah itu disengaja? Tolong tambahkan",
                    "       tes untuk keranjang senilai 105.000.",
                    "  5. Sarankan memecah PR jadi tiga: perubahan data, perhitungan, dan",
                    "     tampilan.",
                    "  6. Tandai saran kecil dengan Nit: supaya temanmu tahu mana yang wajib",
                    "     dan mana yang boleh dilewati.",
                ],
            },
        ],
    },
    {
        "title": "20. Alur Git, Semantic Versioning, dan Conventional Commits",
        "sections": [
            {
                "body": [
                    "Tim yang bekerja di satu repositori butuh tiga kesepakatan: cabang mana",
                    "dipakai untuk apa, bagaimana nomor versi dinaikkan, dan bagaimana pesan",
                    "commit ditulis. Ketiganya saling terhubung. Pesan commit yang rapi bisa",
                    "dibaca mesin untuk menentukan nomor versi berikutnya.",
                    "",
                    "Perintah git dasarnya sudah dibahas di kurikulum Git & GitHub. Materi",
                    "ini membahas aturan mainnya.",
                ],
            },
            {
                "heading": "Tiga alur percabangan",
                "body": [
                    "GitFlow diperkenalkan Vincent Driessen di blognya pada 5 Januari 2010.",
                    "Ada cabang main untuk rilis dan develop untuk pekerjaan yang sedang",
                    "berjalan, lalu cabang feature/, release/, dan hotfix/ dengan aturan",
                    "masuk-keluarnya sendiri. Pada 5 Maret 2020, Driessen menambahkan catatan",
                    "refleksi di artikel itu. Untuk aplikasi web yang dirilis terus-menerus,",
                    "ia menyarankan alur yang lebih sederhana seperti GitHub flow. GitFlow",
                    "tetap cocok untuk perangkat lunak yang harus merawat beberapa versi",
                    "sekaligus, misalnya aplikasi desktop versi 2.x dan 3.x.",
                    "",
                    "GitHub flow jauh lebih ringkas: buat cabang dari main, commit, buka pull",
                    "request, review, merge ke main, lalu hapus cabangnya. Aturan tetapnya",
                    "cuma satu, main selalu siap dirilis.",
                    "",
                    "Trunk-based development lebih ketat lagi. Semua orang menggabungkan",
                    "kerjanya ke trunk, yaitu cabang utama, minimal sekali sehari. Cabangnya",
                    "hidup beberapa jam sampai satu-dua hari. Fitur yang belum selesai tetap",
                    "boleh masuk, tapi disembunyikan dengan feature flag, saklar di",
                    "konfigurasi yang menentukan fitur itu tampil atau nggak. Panduannya",
                    "dirawat di trunkbaseddevelopment.com.",
                    "",
                    "  Alur           Umur cabang       Cocok untuk",
                    "  -------------  ----------------  -------------------------------------",
                    "  GitFlow        lama, banyak      perangkat lunak dengan beberapa versi",
                    "  GitHub flow    beberapa hari     aplikasi web yang sering dirilis",
                    "  Trunk-based    jam sampai 2 hari tim dengan CI dan tes otomatis kuat",
                    "",
                    "Makin pendek umur cabang, makin sedikit konflik yang menumpuk. Syaratnya",
                    "tes otomatis yang bisa dipercaya, karena kode masuk ke main berkali-kali",
                    "sehari.",
                ],
            },
            {
                "heading": "Semantic Versioning",
                "body": [
                    "Semantic Versioning, atau SemVer, adalah aturan penomoran versi",
                    "berbentuk tiga angka yang dipisah titik:",
                    "",
                    "  MAJOR.MINOR.PATCH        contoh: 2.5.1",
                    "",
                    "Spesifikasinya ada di semver.org, versi 2.0.0. Intinya:",
                    "",
                    "  - Naikkan angka mayor (yang pertama) kalau ada perubahan yang membuat",
                    "    kode pemakai lama rusak, misalnya fungsi dihapus atau parameternya",
                    "    berubah.",
                    "  - Naikkan angka minor (yang kedua) kalau menambah fitur baru yang",
                    "    tetap kompatibel.",
                    "  - Naikkan angka patch (yang ketiga) untuk perbaikan bug yang",
                    "    kompatibel.",
                    "  - Angka di kanannya kembali ke nol. Dari 2.5.1, fitur baru jadi 2.6.0,",
                    "    dan perubahan yang merusak jadi 3.0.0.",
                    "  - Versi 0.y.z berarti masih tahap awal. Apa pun boleh berubah kapan",
                    "    saja, jadi jangan menganggapnya stabil.",
                    "",
                    "Jebakan: nomor versi memang ditulis sebagai teks, tapi nggak boleh",
                    "diurutkan seperti teks.",
                ],
                "code": """versi = ["1.10.0", "1.9.0", "1.2.0", "2.0.0"]


def sebagai_angka(v):
    return tuple(int(x) for x in v.split("."))


print("urut sebagai teks :", sorted(versi))
print("urut sebagai angka:", sorted(versi, key=sebagai_angka))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  urut sebagai teks : ['1.10.0', '1.2.0', '1.9.0', '2.0.0']",
                    "  urut sebagai angka: ['1.2.0', '1.9.0', '1.10.0', '2.0.0']",
                    "",
                    "Sebagai teks, \"1.10.0\" dianggap lebih kecil dari \"1.2.0\" karena karakter",
                    "\"1\" lebih kecil dari \"2\". Bandingkan angkanya satu per satu.",
                    "",
                    "SemVer juga mengenal versi pra-rilis dan metadata build:",
                    "",
                    "  - Pra-rilis ditulis sesudah tanda hubung: 1.0.0-alpha, 1.0.0-beta.2,",
                    "    1.0.0-rc.1. Versi pra-rilis selalu lebih rendah daripada versi",
                    "    normalnya.",
                    "  - Metadata build ditulis sesudah tanda plus: 1.0.0+20261019. Bagian",
                    "    ini diabaikan saat membandingkan versi.",
                    "  - Angka nggak boleh diawali nol. 01.2.3 dan 1.0.0-02 bukan versi yang",
                    "    sah.",
                    "",
                    "Urutan contoh dari semver.org:",
                    "",
                    "  1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta",
                    "    < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0",
                    "",
                    "Bagian pra-rilis dibandingkan per potongan yang dipisah titik. Potongan",
                    "angka dibandingkan sebagai angka, jadi beta.2 lebih kecil dari beta.11.",
                    "Potongan huruf dibandingkan menurut urutan karakter ASCII. Potongan",
                    "angka selalu lebih rendah daripada potongan huruf. Kalau semua potongan",
                    "di depannya sama, yang potongannya lebih banyak dianggap lebih tinggi.",
                    "Latihan bab ini memintamu menulis pembandingnya sendiri.",
                ],
            },
            {
                "heading": "Rentang versi: tanda ^ dan ~",
                "body": [
                    "Waktu memasang pustaka, kamu jarang menulis versi persis. Kamu menulis",
                    "rentang yang masih boleh dipakai. Di npm, aturannya begini:",
                    "",
                    "  ^1.2.3   >=1.2.3 dan <2.0.0   minor dan patch boleh naik",
                    "  ~1.2.3   >=1.2.3 dan <1.3.0   cuma patch yang boleh naik",
                    "  ^0.2.3   >=0.2.3 dan <0.3.0   versi 0.x dianggap belum stabil",
                    "  1.2.3    persis 1.2.3",
                    "",
                    "Tanda ^ paling sering dipakai karena SemVer menjanjikan versi minor",
                    "tetap kompatibel. Tapi janji itu dibuat manusia dan kadang dilanggar.",
                    "Karena itu ada lockfile, misalnya package-lock.json, yang mencatat versi",
                    "persis yang terpasang. Semua anggota tim dan server CI jadi memasang",
                    "versi yang sama.",
                    "",
                    "Composer (PHP) dan Cargo (Rust) memakai simbol yang mirip, tapi",
                    "detailnya sedikit berbeda, jadi cek dokumentasinya. Di Survei Stack",
                    "Overflow 2026, npm dipakai 55% responden, Cargo 16%, dan Composer 9%. Di",
                    "package.json, rentangnya tertulis seperti ini:",
                ],
                "bahasa": "json",
                "code": """{
  "name": "toko-kecil",
  "version": "1.4.2",
  "dependencies": {
    "express": "^5.1.0",
    "dayjs": "~1.11.13"
  }
}""",
            },
            {
                "heading": "Conventional Commits",
                "body": [
                    "Conventional Commits adalah format pesan commit yang bisa dibaca manusia",
                    "sekaligus mesin. Spesifikasinya versi 1.0.0 di conventionalcommits.org.",
                    "Baris pertamanya berbentuk:",
                    "",
                    "  <tipe>(scope opsional): deskripsi singkat",
                    "",
                    "Tipe yang memengaruhi versi:",
                    "",
                    "  - feat: menambah fitur baru, menaikkan angka minor.",
                    "  - fix: memperbaiki bug, menaikkan angka patch.",
                    "  - Tanda ! sesudah tipe atau scope, atau footer BREAKING CHANGE: di",
                    "    bawah pesan, menandai perubahan yang merusak dan menaikkan angka",
                    "    mayor.",
                    "",
                    "Tipe lain yang lazim, seperti build, chore, ci, docs, style, refactor,",
                    "perf, dan test, berasal dari konvensi tim Angular. Tipe-tipe itu nggak",
                    "menaikkan versi. Contoh pesannya:",
                    "",
                    "  feat(kurir): dukung kurir instan",
                    "  fix: ongkir negatif untuk jarak 0",
                    "  docs: perbaiki contoh di README",
                    "  refactor(api)!: hapus endpoint /v1/harga",
                    "",
                    "Riwayat repositori aplikasi belajar-codingV2 ini juga memakai gaya itu,",
                    "misalnya \"fix(runner): ...\" dan \"docs(agents): ...\". Jalankan git log",
                    "--oneline di proyek open source mana pun, dan kemungkinan besar kamu",
                    "menemukan pola yang sama.",
                ],
            },
            {
                "heading": "Changelog dan rilis otomatis",
                "body": [
                    "Changelog adalah berkas yang mencatat perubahan tiap versi untuk dibaca",
                    "manusia. Format yang populer, Keep a Changelog 1.1.0, mengelompokkan",
                    "perubahan jadi Added, Changed, Deprecated, Removed, Fixed, dan Security.",
                    "Bagian Unreleased di paling atas menampung perubahan yang belum dirilis.",
                    "",
                    "Karena pesan commit-nya terstruktur, langkah ini bisa diotomatisasi.",
                    "Alat seperti semantic-release dan release-please membaca commit sejak",
                    "tag terakhir, lalu mengambil kenaikan terbesar: mayor mengalahkan minor,",
                    "minor mengalahkan patch. Sesudah itu alat menghitung versi baru, menulis",
                    "changelog, dan membuat tag. commitlint dipasang di CI untuk menolak",
                    "pesan commit yang nggak sesuai format. Hasilnya kira-kira begini:",
                ],
                "bahasa": "markdown",
                "code": """# Changelog

## [Unreleased]

## [1.5.0] - 2026-10-19
### Added
- Dukungan kurir instan.

### Fixed
- Ongkir negatif untuk jarak 0 km.

## [1.4.2] - 2026-09-30
### Fixed
- Pembulatan ongkir ke ratusan terdekat.""",
            },
            {
                "heading": "Jebakan soal versi",
                "body": [
                    "  - Menaikkan angka mayor karena fiturnya besar. Angka mayor soal",
                    "    kompatibilitas. Fitur besar yang nggak merusak apa pun cukup",
                    "    menaikkan minor.",
                    "  - Mengubah isi versi yang sudah dirilis. SemVer melarangnya. Kalau",
                    "    1.4.2 ternyata salah, terbitkan 1.4.3.",
                    "  - Menganggap 0.x stabil. Pustaka 0.x boleh berubah total di versi",
                    "    minor berikutnya.",
                    "  - Pesan commit \"update\" atau \"fix bug\". Enam bulan lagi nggak ada yang",
                    "    tahu apa isinya, termasuk kamu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pustaka di npm, PyPI, Cargo, dan Composer memakai nomor versi untuk",
                    "menentukan pembaruan mana yang aman dipasang otomatis. Aplikasi mobile",
                    "di Play Store juga menampilkan nomor seperti 2.3.1 kepada penggunanya.",
                    "",
                    "Kasus kecil: kamu merawat pustaka kecil hitung-ongkir versi 1.4.2. Sejak",
                    "rilis terakhir ada tiga commit: \"fix: ongkir negatif untuk jarak 0\",",
                    "\"feat(kurir): dukung kurir instan\", dan \"docs: perbaiki contoh di",
                    "README\". Versi berikutnya berapa?",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Kelompokkan commit menurut tipenya: satu fix, satu feat, satu docs.",
                    "  2. Ambil kenaikan terbesar. feat menang atas fix, dan docs nggak",
                    "     dihitung, jadi yang naik angka minor.",
                    "  3. Nolkan angka di kanannya: 1.4.2 jadi 1.5.0.",
                    "  4. Tulis changelog: dukungan kurir instan di bawah Added, ongkir",
                    "     negatif di bawah Fixed.",
                    "  5. Buat tag lalu kirim ke remote:",
                    "       git tag v1.5.0",
                    "       git push origin v1.5.0",
                    "  6. Seandainya salah satu commit ditulis feat! atau punya footer",
                    "     BREAKING CHANGE, versinya jadi 2.0.0.",
                ],
            },
        ],
    },
    {
        "title": "21. Kode Bersih: SOLID, DRY, Refactoring, dan Design Pattern",
        "sections": [
            {
                "body": [
                    "Kode yang jalan belum tentu gampang diubah. Tiga bulan kemudian kamu",
                    "atau temanmu harus menambah fitur di kode itu. Di situlah kode yang",
                    "berantakan mulai mahal: satu perubahan kecil merusak tiga tempat lain.",
                    "",
                    "Materi ini merangkum prinsip yang paling sering dipakai programmer untuk",
                    "menjaga kode tetap bisa diubah. Anggap semuanya pedoman. Kalau mengikuti",
                    "satu prinsip malah membuat kode lebih susah dibaca, abaikan prinsip itu",
                    "untuk kasus tersebut.",
                    "",
                    "Contoh di sini memakai fungsi Python biasa. Penerapan lapisan domain,",
                    "repository, dan service di Java sudah dibahas di kurikulum Bikin",
                    "Aplikasi, jadi nggak diulang di sini.",
                ],
            },
            {
                "heading": "DRY, KISS, dan YAGNI",
                "body": [
                    "  - DRY (Don't Repeat Yourself), dari buku The Pragmatic Programmer",
                    "    (1999): setiap pengetahuan di sistem cukup punya satu tempat. Kalau",
                    "    diskon member 10% ditulis di halaman keranjang, di struk, dan di",
                    "    laporan, suatu hari diskonnya berubah dan salah satu tempat pasti",
                    "    terlupa.",
                    "  - KISS (Keep It Simple): pilih solusi paling sederhana yang",
                    "    menyelesaikan masalah. Kode cerdik yang cuma dipahami penulisnya",
                    "    jadi beban tim.",
                    "  - YAGNI (You Aren't Gonna Need It), dari Extreme Programming: jangan",
                    "    membangun fitur atau lapisan abstraksi sebelum memang dibutuhkan.",
                    "",
                    "Hati-hati dengan DRY. Yang nggak boleh diulang adalah pengetahuan. Dua",
                    "fungsi validasi yang hari ini sama persis, satu untuk umur siswa dan",
                    "satu untuk jumlah barang, punya alasan berubah yang berbeda. Kalau",
                    "disatukan, perubahan aturan umur ikut mengubah aturan barang.",
                    "",
                    "Banyak programmer memakai aturan tiga kali, yang populer lewat buku",
                    "Refactoring: duplikasi pertama dibiarkan, kedua dicatat, ketiga baru",
                    "dirapikan. Pada titik itu kamu sudah tahu bagian mana yang memang sama.",
                ],
            },
            {
                "heading": "Code smell dan refactoring",
                "body": [
                    "Refactoring artinya mengubah struktur kode tanpa mengubah perilakunya,",
                    "dalam langkah-langkah kecil yang aman. Istilah ini dipopulerkan Martin",
                    "Fowler lewat buku Refactoring. Edisi keduanya (2018) memakai contoh",
                    "JavaScript, dan daftar refactoring-nya, sekitar 70 jenis, bisa dibaca",
                    "gratis di refactoring.com.",
                    "",
                    "Tanda kode perlu dirapikan disebut code smell. Ia belum tentu bug, tapi",
                    "biasanya berujung masalah:",
                    "",
                    "  - Long Function: fungsi panjang yang mengerjakan banyak hal.",
                    "  - Duplicated Code: logika yang sama di beberapa tempat.",
                    "  - Long Parameter List: fungsi dengan banyak sekali parameter.",
                    "  - Mysterious Name: nama seperti t, data2, atau proses() yang nggak",
                    "    menjelaskan apa pun.",
                    "  - Magic number: angka seperti 15000 tanpa keterangan artinya.",
                    "",
                    "Contoh berikut menerapkan dua refactoring yang paling sering dipakai,",
                    "Extract Function dan Rename Variable, lalu memastikan hasilnya sama",
                    "dengan versi lama:",
                ],
                "code": """# Sebelum: satu fungsi mengerjakan semuanya, nama dan angkanya misterius
def struk(items, member):
    t = 0
    for nama, harga, jumlah in items:
        t = t + harga * jumlah
    if member:
        t = t - t * 10 // 100
    if t >= 100000:
        o = 0
    else:
        o = 15000
    return f"total {t}, ongkir {o}, bayar {t + o}"


# Sesudah: Extract Function + Rename Variable, perilakunya sama persis
DISKON_MEMBER_PERSEN = 10
BATAS_GRATIS_ONGKIR = 100_000
ONGKIR_STANDAR = 15_000


def subtotal(items):
    return sum(harga * jumlah for _, harga, jumlah in items)


def potong_diskon(total, member):
    if not member:
        return total
    return total - total * DISKON_MEMBER_PERSEN // 100


def ongkir(total):
    return 0 if total >= BATAS_GRATIS_ONGKIR else ONGKIR_STANDAR


def struk_baru(items, member):
    total = potong_diskon(subtotal(items), member)
    biaya_kirim = ongkir(total)
    return f"total {total}, ongkir {biaya_kirim}, bayar {total + biaya_kirim}"


keranjang = [("buku", 45_000, 2), ("pena", 5_000, 3)]
for member in (False, True):
    lama, baru = struk(keranjang, member), struk_baru(keranjang, member)
    assert lama == baru, (lama, baru)
    print(baru)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  total 105000, ongkir 0, bayar 105000",
                    "  total 94500, ongkir 15000, bayar 109500",
                    "",
                    "Assert di dalam loop memastikan perilaku lama dan baru sama untuk kedua",
                    "kasus. Di proyek sungguhan, peran itu dipegang tes otomatis. Tanpa tes,",
                    "kamu cuma menebak perilakunya masih sama.",
                    "",
                    "Perhatikan baris kedua keluarannya. Member membayar 109.500, lebih mahal",
                    "daripada pembeli biasa yang membayar 105.000. Diskon 10% membuat total",
                    "turun di bawah batas gratis ongkir, jadi member malah kena ongkir.",
                    "Refactoring sengaja nggak memperbaiki hal ini, karena memperbaikinya",
                    "berarti mengubah perilaku. Itu pekerjaan terpisah, dengan tesnya",
                    "sendiri, setelah aturannya ditanyakan ke pemilik toko.",
                ],
            },
            {
                "heading": "Lima prinsip SOLID",
                "body": [
                    "SOLID adalah lima prinsip desain berorientasi objek yang dikumpulkan",
                    "Robert C. Martin. Nama prinsipnya memang bahasa Inggris, dan nama itu",
                    "juga yang akan kamu dengar di wawancara kerja:",
                    "",
                    "  Huruf  Prinsip                 Artinya",
                    "  -----  ----------------------  -----------------------------------------",
                    "  S      Single Responsibility   satu kelas cuma punya satu alasan berubah",
                    "  O      Open/Closed             bisa ditambah tanpa mengubah kode lama",
                    "  L      Liskov Substitution     turunan bisa menggantikan induknya",
                    "  I      Interface Segregation   antarmuka kecil, sesuai yang dipakai",
                    "  D      Dependency Inversion    bergantung pada abstraksi",
                    "",
                    "  - Single Responsibility: kelas Laporan yang menghitung total, mencetak",
                    "    PDF, dan mengirim email punya tiga alasan berubah. Pisahkan jadi",
                    "    tiga, supaya mengganti format PDF nggak berisiko merusak",
                    "    hitungannya.",
                    "  - Open/Closed: menambah metode pembayaran baru seharusnya cukup dengan",
                    "    menambah satu kelas atau fungsi. Kalau caranya menyunting rantai",
                    "    if/elif yang makin panjang, prinsip ini dilanggar.",
                    "  - Liskov Substitution: kalau sebuah fungsi menerima objek Pembayaran,",
                    "    semua turunannya harus bisa dipakai di situ. Turunan yang melempar",
                    "    error \"metode ini nggak didukung\" melanggar prinsip ini.",
                    "  - Interface Segregation: jangan memaksa kelas mengisi metode yang",
                    "    nggak ia butuhkan. Printer struk nggak perlu punya metode scan()",
                    "    kosong hanya karena antarmukanya bernama Mesin.",
                    "  - Dependency Inversion: kode aturan bisnis bergantung pada antarmuka",
                    "    seperti PenyimpananPesanan, sedangkan MySQL cuma salah satu",
                    "    penerapannya. Ide ini jadi dasar arsitektur hexagonal di bab",
                    "    berikutnya.",
                ],
            },
            {
                "heading": "Design pattern dari Gang of Four",
                "body": [
                    "Design pattern adalah solusi umum yang sudah teruji untuk masalah desain",
                    "yang berulang. Daftar klasiknya berasal dari buku Design Patterns (1994)",
                    "karya empat penulis yang dijuluki Gang of Four (GoF). Isinya 23 pola",
                    "dalam tiga kelompok:",
                    "",
                    "  - Pola pembuatan (creational): Factory Method, Abstract Factory,",
                    "    Builder, Prototype, Singleton.",
                    "  - Pola struktur (structural): Adapter, Bridge, Composite, Decorator,",
                    "    Facade, Flyweight, Proxy.",
                    "  - Pola perilaku (behavioral): Chain of Responsibility, Command,",
                    "    Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy,",
                    "    Template Method, Visitor.",
                    "",
                    "Kamu nggak perlu menghafal semuanya. Lima yang paling sering muncul di",
                    "kode sehari-hari: Strategy, Decorator, dan Observer ada di program ini,",
                    "sedangkan Factory dan Adapter dijelaskan sesudahnya.",
                ],
                "code": """# Strategy: cara hitung ongkir bisa ditukar tanpa mengubah bayar()
def kurir_reguler(km):
    return 9_000 + 1_000 * km


def kurir_instan(km):
    return 15_000 + 2_500 * km


# Decorator: menambah log tanpa menyentuh isi fungsi yang dibungkus
def catat(fungsi):
    def bungkus(*args):
        hasil = fungsi(*args)
        print(f"[log] {fungsi.__name__}{args} = {hasil}")
        return hasil
    return bungkus


# Observer: siapa pun boleh mendaftar untuk dikabari saat pesanan dibayar
pendengar = []


def saat_dibayar(fungsi):
    pendengar.append(fungsi)
    return fungsi


@saat_dibayar
def kirim_email(nomor):
    print("email terkirim untuk pesanan", nomor)


@saat_dibayar
def kurangi_stok(nomor):
    print("stok dikurangi untuk pesanan", nomor)


def bayar(nomor, total, km, strategi):
    biaya = catat(strategi)(km)
    for kabari in pendengar:
        kabari(nomor)
    return total + biaya


print("bayar:", bayar("A17", 50_000, 4, kurir_instan))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  [log] kurir_instan(4,) = 25000",
                    "  email terkirim untuk pesanan A17",
                    "  stok dikurangi untuk pesanan A17",
                    "  bayar: 75000",
                    "",
                    "Strategy membuat cara hitung ongkir bisa ditukar tanpa mengubah fungsi",
                    "bayar(). Decorator membungkus fungsi untuk menambah perilaku, di sini",
                    "log, tanpa menyentuh isinya. Fitur @ di Python bentuknya mirip pola",
                    "Decorator GoF, walau asal-usulnya berbeda. Observer membuat bayar()",
                    "cukup mengabari daftar pendengar tanpa perlu tahu siapa saja yang",
                    "mendengar.",
                    "",
                    "Dua pola lagi yang sering kamu temui:",
                    "",
                    "  - Factory: fungsi atau kelas yang tugasnya memilih dan membuat objek,",
                    "    misalnya buat_kurir(\"instan\") yang mengembalikan kurir_instan. Kode",
                    "    pemanggil nggak perlu tahu detail tiap kurir.",
                    "  - Adapter: pembungkus yang menerjemahkan antarmuka satu pustaka ke",
                    "    bentuk yang diharapkan kodemu. Misalnya gateway pembayaran A punya",
                    "    metode charge(), gateway B punya create_payment(), dan adapter",
                    "    membuat keduanya terlihat sama: bayar(jumlah).",
                    "",
                    "Framework besar penuh pola ini. Spring memakai Factory dan Proxy di",
                    "mana-mana, Laravel punya Facade dan Observer, dan event listener di",
                    "JavaScript adalah Observer. Mengenali nama polanya membuat dokumentasi",
                    "framework jauh lebih gampang dibaca.",
                ],
            },
            {
                "heading": "Kapan prinsip ini malah merugikan",
                "body": [
                    "  - Pola untuk skrip 30 baris. Skrip sekali pakai nggak butuh Factory",
                    "    dan tiga antarmuka.",
                    "  - Abstraksi terlalu dini. Antarmuka dengan satu penerapan, dibuat",
                    "    karena \"siapa tahu nanti butuh\", melanggar YAGNI dan menambah satu",
                    "    lompatan setiap kali kode dibaca.",
                    "  - DRY yang dipaksakan. Menyatukan dua kode yang mirip tapi maknanya",
                    "    beda menghasilkan satu fungsi penuh parameter dan if.",
                    "  - Refactoring besar tanpa tes. Perilakunya berubah tanpa ada yang",
                    "    tahu.",
                    "",
                    "Patokan praktisnya: rapikan kode yang sering kamu ubah, dan biarkan kode",
                    "yang jarang disentuh. Kode jelek yang nggak pernah diubah jarang jadi",
                    "masalah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir dan toko online di Indonesia rutin menambah metode",
                    "pembayaran: kode QR, transfer bank, dompet digital, sampai paylater.",
                    "Setiap tambahan menguji struktur kodenya.",
                    "",
                    "Kasus kecil: fungsi bayar() di aplikasi kasir berisi rantai if/elif",
                    "untuk lima metode pembayaran. Setiap metode baru harus menyunting fungsi",
                    "itu, dan bulan lalu penambahan satu metode merusak metode lain.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pastikan ada tes untuk kelima metode yang sudah ada, sebelum",
                    "     menyentuh apa pun.",
                    "  2. Terapkan Extract Function: isi tiap cabang if/elif dipindah ke",
                    "     fungsinya sendiri, misalnya bayar_transfer() dan bayar_dompet().",
                    "  3. Ganti rantai if/elif dengan kamus yang memetakan nama metode ke",
                    "     fungsinya. Ini Strategy ditambah Factory sederhana:",
                    "       METODE = {",
                    "           \"transfer\": bayar_transfer,",
                    "           \"dompet\": bayar_dompet,",
                    "       }",
                    "       def bayar(metode, jumlah):",
                    "           return METODE[metode](jumlah)",
                    "  4. Metode baru sekarang cukup berupa satu fungsi baru dan satu baris",
                    "     di kamus. Fungsi lama nggak disentuh lagi, sesuai prinsip",
                    "     Open/Closed.",
                    "  5. Jalankan semua tes. Hasilnya harus sama persis dengan sebelum",
                    "     refactoring.",
                ],
            },
        ],
    },
    {
        "title": "22. Monolit dan Monolit Modular",
        "sections": [
            {
                "body": [
                    "Monolit adalah aplikasi yang dibangun dan di-deploy sebagai satu",
                    "kesatuan. Tampilan, logika bisnis, dan akses data ada di satu program,",
                    "biasanya berjalan sebagai satu proses dengan satu database. Hampir semua",
                    "aplikasi yang pernah kamu buat sejauh ini berbentuk monolit.",
                    "",
                    "Kata monolit sering dipakai seolah-olah ejekan, padahal yang jadi",
                    "masalah adalah monolit yang berantakan. Brian Foote dan Joseph Yoder",
                    "menyebut bentuk itu big ball of mud (1997): kode yang saling menempel",
                    "tanpa batas, sehingga menyentuh satu bagian berarti mengguncang",
                    "semuanya.",
                    "",
                    "Martin Fowler menulis artikel Monolith First (2015) dari pengamatannya.",
                    "Kisah microservices yang berhasil hampir selalu berawal dari monolit",
                    "yang tumbuh terlalu besar, sedangkan sistem yang dibangun sebagai",
                    "microservices sejak hari pertama sering berakhir bermasalah.",
                ],
            },
            {
                "heading": "Kenapa monolit jadi titik awal yang wajar",
                "body": [
                    "  - Satu repositori, satu perintah build, satu kali deploy.",
                    "  - Antarbagian saling memanggil lewat fungsi biasa. Cepat, tanpa",
                    "    jaringan, dan tanpa format data perantara.",
                    "  - Satu database berarti satu transaksi bisa mencakup pesanan dan stok",
                    "    sekaligus.",
                    "  - Debugging gampang: satu log, satu proses, dan stack trace yang utuh.",
                    "",
                    "Biayanya baru terasa saat aplikasi dan timnya membesar. Perubahan satu",
                    "baris tetap harus men-deploy seluruh aplikasi. Bagian yang butuh banyak",
                    "tenaga nggak bisa diperbanyak sendirian. Dua puluh orang yang menyunting",
                    "satu basis kode bisa saling menginjak setiap hari. Satu bug yang",
                    "menghabiskan memori menjatuhkan semua fitur sekaligus.",
                ],
            },
            {
                "heading": "Monolit modular",
                "body": [
                    "Monolit modular adalah jalan tengahnya. Aplikasinya tetap satu dan",
                    "di-deploy sekali, tapi kodenya dibagi tegas jadi modul per domain",
                    "bisnis, misalnya produk, pesanan, dan pembayaran. Aturannya:",
                    "",
                    "  - Setiap modul punya pintu resmi berupa antarmuka publik.",
                    "  - Modul lain cuma boleh masuk lewat pintu itu. Urusan dalam sebuah",
                    "    modul nggak boleh diimpor dari luar.",
                    "  - Data milik satu modul diubah lewat modul itu, walaupun tabelnya ada",
                    "    di database yang sama.",
                    "",
                    "  toko/",
                    "    produk/",
                    "      api.py          <- pintu resmi modul produk",
                    "      _harga.py       <- urusan dalam, modul lain dilarang impor",
                    "    pesanan/",
                    "      api.py",
                    "      _keranjang.py",
                    "    pembayaran/",
                    "      api.py",
                    "    main.py",
                    "",
                    "Kalau suatu hari modul pembayaran perlu dipecah jadi layanan sendiri,",
                    "batasnya sudah ada. Yang diganti cuma cara memanggilnya, dari panggilan",
                    "fungsi jadi panggilan lewat jaringan.",
                    "",
                    "Di dunia Java ada Spring Modulith, alat yang memeriksa aturan antarmodul",
                    "lewat tes dan menggambar diagram hubungannya. Versi stabilnya 2.1.1 (26",
                    "Agustus 2026), berlisensi Apache-2.0. Di .NET, tim biasanya memakai satu",
                    "project per modul supaya compiler ikut menjaga batasnya.",
                ],
            },
            {
                "heading": "Aplikasi ini sendiri contohnya",
                "body": [
                    "Aplikasi belajar-codingV2 yang sedang kamu pakai adalah monolit modular.",
                    "Semuanya dijalankan dari satu perintah, python3 main.py atau",
                    "belajar-web.py, tapi kodenya dibagi jadi beberapa paket:",
                    "  - inti/: mesinnya, misalnya runner.py yang menjalankan kode dan",
                    "    sorot.py yang mewarnai sintaks.",
                    "  - pelajar/: keadaan milik pelajar, misalnya progress.py dan bab.py.",
                    "  - layar/: antarmuka terminal.",
                    "  - webapp/: antarmuka web.",
                    "",
                    "Aturannya satu arah: paket bawah nggak boleh mengimpor paket di atasnya.",
                    "inti/ nggak tahu ada terminal atau web. Aturan seperti ini bisa",
                    "diperiksa otomatis dengan membaca import tiap berkas. Program di bawah",
                    "melakukannya dengan modul ast bawaan Python, pada isi berkas tiruan:",
                ],
                "code": "import ast\n\n# Angka kecil = lapisan bawah. Lapisan bawah dilarang mengimpor yang di atas.\nLAPISAN = {\"inti\": 0, \"pelajar\": 1, \"layar\": 2}\n\nberkas = {\n    \"inti/runner.py\": \"import os\\nimport subprocess\\n\",\n    \"pelajar/progress.py\": \"import json\\nfrom inti import runner\\n\",\n    \"layar/materials.py\": \"from pelajar import progress\\nfrom inti import sorot\\n\",\n    \"inti/contoh_salah.py\": \"from layar import utils\\n\",   # pelanggaran buatan\n}\n\n\ndef paket_diimpor(sumber):\n    for simpul in ast.walk(ast.parse(sumber)):\n        if isinstance(simpul, ast.ImportFrom) and simpul.module:\n            yield simpul.module.split(\".\")[0]\n        elif isinstance(simpul, ast.Import):\n            for nama in simpul.names:\n                yield nama.name.split(\".\")[0]\n\n\nfor jalur, sumber in berkas.items():\n    asal = jalur.split(\"/\")[0]\n    for tujuan in paket_diimpor(sumber):\n        if tujuan in LAPISAN and LAPISAN[tujuan] > LAPISAN[asal]:\n            print(f\"melanggar: {jalur} mengimpor {tujuan}\")\nprint(\"pemeriksaan selesai:\", len(berkas), \"berkas\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  melanggar: inti/contoh_salah.py mengimpor layar",
                    "  pemeriksaan selesai: 4 berkas",
                    "",
                    "Pemeriksaan seperti ini dipasang di CI, jadi pelanggaran batas modul",
                    "ketahuan saat pull request dibuka, jauh sebelum batasnya hancur.",
                ],
            },
            {
                "heading": "Tanda monolit perlu dipecah, dan tanda belum perlu",
                "body": [
                    "Tanda yang masuk akal untuk mulai memecah:",
                    "",
                    "  - Satu bagian butuh skala yang jauh berbeda, misalnya pengolah video",
                    "    yang butuh puluhan mesin sementara sisanya cukup satu.",
                    "  - Beberapa tim sering saling menunggu untuk deploy.",
                    "  - Satu bagian butuh teknologi yang berbeda, misalnya model AI di",
                    "    Python sementara aplikasinya ditulis dengan PHP.",
                    "",
                    "Tanda yang belum cukup kuat: \"microservices sedang tren\", \"perusahaan",
                    "besar memakainya\", atau tim yang cuma berisi tiga orang. Untuk kondisi",
                    "seperti itu, merapikan batas modul di dalam monolit hampir selalu lebih",
                    "murah. Cara memecah sistem dibahas di bab Arsitektur Terdistribusi.",
                    "",
                    "Jebakan: modular cuma di nama folder. Foldernya rapi per domain, tapi",
                    "setiap modul bebas mengimpor isi dalam modul lain dan menyunting tabel",
                    "milik modul lain. Hasilnya tetap bola lumpur, cuma berlabel.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak sistem informasi sekolah, aplikasi kasir, dan toko online UMKM",
                    "berupa satu aplikasi Laravel, Django, atau Rails yang di-deploy ke satu",
                    "server. Framework seperti itu memang dirancang untuk monolit, dan bisa",
                    "ditata jadi modular.",
                    "",
                    "Kasus kecil: aplikasi sekolahmu mengurus nilai, absensi, dan pembayaran",
                    "SPP. Semuanya ada di satu folder controllers raksasa, dan perubahan di",
                    "bagian SPP beberapa kali merusak halaman nilai.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Petakan domainnya dulu: akademik (nilai), kehadiran (absensi), dan",
                    "     keuangan (SPP).",
                    "  2. Buat satu folder per modul, masing-masing dengan berkas pintu resmi",
                    "     seperti api.py atau kelas service publik.",
                    "  3. Pindahkan kode sedikit demi sedikit. Setiap selesai satu pindahan,",
                    "     jalankan aplikasinya dan tesnya.",
                    "  4. Pasang pemeriksaan import di CI, mirip program ast tadi, supaya",
                    "     modul keuangan nggak lagi menyentuh isi dalam modul akademik.",
                    "  5. Tetap satu deploy dan satu database. Kelompokkan saja tabelnya per",
                    "     modul, misalnya dengan awalan nama tabel.",
                ],
            },
        ],
    },
    {
        "title": "23. Hexagonal, Onion, dan Clean Architecture",
        "sections": [
            {
                "body": [
                    "Bayangkan aturan diskon koperasi sekolah ditulis langsung di dalam",
                    "fungsi yang menerima request HTTP, sambil menjalankan query SQL di",
                    "tengah-tengahnya. Kodenya jalan. Tapi untuk menguji satu aturan diskon,",
                    "kamu harus menyalakan server web dan database. Kalau suatu hari",
                    "framework-nya diganti, aturan diskonnya ikut ditulis ulang.",
                    "",
                    "Tiga pola dari tahun yang berbeda menjawab masalah itu dengan ide yang",
                    "sama. Logika bisnis ditaruh di tengah. Detail teknis seperti database,",
                    "framework web, dan layanan luar ditaruh di pinggir. Ketergantungan",
                    "kodenya selalu menunjuk ke tengah.",
                ],
            },
            {
                "heading": "Hexagonal: port dan adapter",
                "body": [
                    "Alistair Cockburn menerbitkan hexagonal architecture pada 2005, dengan",
                    "nama lain ports and adapters. Dua istilahnya:",
                    "",
                    "  - Port: antarmuka yang didefinisikan oleh inti aplikasi, misalnya \"aku",
                    "    butuh tempat menyimpan pesanan\" atau \"aku menerima perintah membuat",
                    "    pesanan\".",
                    "  - Adapter: penerapan konkret sebuah port, misalnya penyimpanan ke",
                    "    PostgreSQL, controller HTTP, perintah terminal, atau penyimpanan di",
                    "    memori untuk tes.",
                    "",
                    "Adapter yang memanggil inti, seperti controller web atau tes, disebut",
                    "adapter pendorong (driving). Adapter yang dipanggil inti, seperti",
                    "database atau pengirim email, disebut adapter yang didorong (driven).",
                    "Bentuk segi enam di gambarnya cuma gaya menggambar. Jumlah sisinya nggak",
                    "punya arti.",
                ],
            },
            {
                "heading": "Contoh kecil dalam Python",
                "body": [
                    "Port ditulis dengan typing.Protocol, yaitu antarmuka yang cukup dipenuhi",
                    "bentuknya: kelas apa pun yang punya metode simpan() dan semua() dianggap",
                    "cocok. Fungsi buat_pesanan() nggak tahu datanya disimpan di mana:",
                ],
                "code": """from typing import Protocol


# ---- inti: aturan bisnis, nggak tahu soal database atau HTTP ----
class PenyimpananPesanan(Protocol):          # port keluar
    def simpan(self, pesanan: dict) -> None: ...
    def semua(self) -> list: ...


class Pemberitahu(Protocol):                  # port keluar
    def kabari(self, pesan: str) -> None: ...


def buat_pesanan(barang, jumlah, harga, gudang: PenyimpananPesanan,
                 pemberitahu: Pemberitahu):
    if jumlah <= 0:
        raise ValueError("jumlah harus positif")
    pesanan = {"no": len(gudang.semua()) + 1, "barang": barang,
               "total": jumlah * harga}
    gudang.simpan(pesanan)
    pemberitahu.kabari(f"pesanan {pesanan['no']} dibuat: {barang}")
    return pesanan


# ---- adapter: detail teknis yang bisa ditukar ----
class GudangMemori:
    def __init__(self):
        self.data = []

    def simpan(self, pesanan):
        self.data.append(pesanan)

    def semua(self):
        return self.data


class PemberitahuKonsol:
    def kabari(self, pesan):
        print("[notif]", pesan)


gudang = GudangMemori()
buat_pesanan("buku", 2, 45_000, gudang, PemberitahuKonsol())
buat_pesanan("pena", 3, 5_000, gudang, PemberitahuKonsol())
for p in gudang.semua():
    print(p)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  [notif] pesanan 1 dibuat: buku",
                    "  [notif] pesanan 2 dibuat: pena",
                    "  {'no': 1, 'barang': 'buku', 'total': 90000}",
                    "  {'no': 2, 'barang': 'pena', 'total': 15000}",
                    "",
                    "Di tes, kamu memakai GudangMemori. Di produksi, kamu menulis",
                    "GudangPostgres dengan metode simpan() dan semua() yang sama.",
                    "buat_pesanan() nggak perlu diubah, dan berkas intinya nggak pernah",
                    "mengimpor pustaka database apa pun.",
                    "",
                    "Pola ini adalah prinsip Dependency Inversion dari bab sebelumnya yang",
                    "diterapkan ke seluruh aplikasi: inti menentukan antarmukanya, lapisan",
                    "luar yang menyesuaikan diri.",
                ],
            },
            {
                "heading": "Onion dan Clean: gambar beda, aturan sama",
                "body": [
                    "Jeffrey Palermo memperkenalkan onion architecture pada 29 Juli 2008.",
                    "Gambarnya lingkaran berlapis seperti bawang: model domain di pusat, lalu",
                    "domain service, lalu application service, dan di kulit terluar ada",
                    "antarmuka pengguna, infrastruktur, dan tes.",
                    "",
                    "Robert C. Martin menulis The Clean Architecture pada 13 Agustus 2012.",
                    "Lingkarannya berisi entities (aturan bisnis inti), use cases (alur kerja",
                    "aplikasi), interface adapters (controller, presenter, gateway), lalu",
                    "frameworks and drivers di luar. Artikel itu menyebut dirinya menyatukan",
                    "hexagonal, onion, dan beberapa gagasan sejenis. Aturan utamanya diberi",
                    "nama dependency rule: ketergantungan kode sumber cuma boleh menunjuk ke",
                    "dalam.",
                    "",
                    "  Pola        Tahun  Di pusat            Di luar",
                    "  ----------  -----  ------------------  ---------------------------",
                    "  Hexagonal   2005   aplikasi (inti)     adapter: UI, DB, layanan",
                    "  Onion       2008   model domain        UI, infrastruktur, tes",
                    "  Clean       2012   entities, use case  frameworks and drivers",
                    "",
                    "Kalau kamu sudah membaca kurikulum Bikin Aplikasi, lapisan domain,",
                    "repository, dan service di sana adalah versi sederhana dari ide ini.",
                    "Panduan arsitektur Android resmi juga memakai pembagian serupa: lapisan",
                    "UI, lapisan domain yang opsional, dan lapisan data.",
                ],
            },
            {
                "heading": "Aturan ketergantungan dalam praktik",
                "body": [
                    "Cara paling gampang mengecek aturan ini adalah melihat import. Berkas di",
                    "lapisan dalam boleh mengimpor pustaka standar dan sesama lapisan dalam.",
                    "Berkas itu nggak boleh mengimpor framework web, driver database, atau",
                    "SDK layanan luar.",
                    "",
                    "  - Boleh: use case mengimpor entity Pesanan.",
                    "  - Boleh: adapter PostgreSQL mengimpor port PenyimpananPesanan dan",
                    "    pustaka psycopg.",
                    "  - Melanggar: entity Pesanan mengimpor modul ORM supaya bisa menyimpan",
                    "    dirinya sendiri.",
                    "  - Melanggar: use case membaca objek request milik framework web secara",
                    "    langsung.",
                    "",
                    "Pemeriksaan import otomatis seperti di materi monolit modular bisa",
                    "menjaga aturan ini di CI.",
                ],
            },
            {
                "heading": "Kapan ini berlebihan",
                "body": [
                    "Aplikasi CRUD kecil, yang kerjanya cuma menyimpan isian formulir lalu",
                    "menampilkannya lagi, hampir nggak punya logika bisnis. Membungkusnya",
                    "dengan port, adapter, use case, dan empat folder lapisan cuma menambah",
                    "berkas kosong yang harus dilompati setiap kali kode dibaca.",
                    "",
                    "Pola ini sepadan kalau logika bisnisnya rumit dan harus diuji tanpa",
                    "database, umur aplikasinya panjang, atau ada kemungkinan nyata",
                    "infrastrukturnya diganti. Jalan tengah yang murah: pisahkan dulu fungsi",
                    "bisnis yang murni dari kode framework. Port dan adapter ditambahkan saat",
                    "memang dibutuhkan.",
                    "",
                    "Jebakan: menyalin struktur folder \"clean architecture\" dari tutorial ke",
                    "setiap proyek. Strukturnya terlihat rapi, tapi kalau setiap antarmuka",
                    "cuma punya satu penerapan dan nggak pernah dites, kamu menanggung",
                    "biayanya tanpa menikmati manfaatnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola ini sering ditemui di aplikasi Android yang memisahkan domain,",
                    "data, dan presentation. Backend layanan keuangan yang aturannya rumit",
                    "juga sering memakainya, begitu pula sistem lama yang sedang dipindah ke",
                    "database lain.",
                    "",
                    "Kasus kecil: aturan diskon koperasi sekolah ditulis di dalam view Django",
                    "dan langsung memanggil ORM. Kamu diminta menulis tes untuk aturan itu",
                    "tanpa harus menyalakan database.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pindahkan perhitungannya ke fungsi murni yang menerima data biasa:",
                    "       def hitung_diskon(total, belanja_bulan_ini):",
                    "           if belanja_bulan_ini >= 200_000:",
                    "               return total * 5 // 100",
                    "           return 0",
                    "  2. Data yang dibutuhkan, seperti total belanja bulan ini, diambil di",
                    "     luar fungsi itu lalu dikirim sebagai parameter.",
                    "  3. View Django jadi adapter: membaca request, mengambil data lewat",
                    "     ORM, memanggil hitung_diskon(), lalu menampilkan hasilnya.",
                    "  4. Tes cukup memanggil hitung_diskon() dengan angka langsung, tanpa",
                    "     database dan tanpa server.",
                    "  5. Port dan adapter penuh baru ditambahkan kalau ada kebutuhan nyata,",
                    "     misalnya data anggota harus diambil dari dua sumber yang berbeda.",
                ],
            },
        ],
    },
    {
        "title": "24. Domain-Driven Design dan Vertical Slice",
        "sections": [
            {
                "body": [
                    "Domain-Driven Design (DDD) diperkenalkan Eric Evans lewat bukunya pada",
                    "2003. Idenya: struktur perangkat lunak mengikuti bahasa dan aturan yang",
                    "dipakai orang bisnisnya sehari-hari. Tabel database dan framework yang",
                    "menyesuaikan diri.",
                    "",
                    "DDD punya dua sisi. Sisi strategis membahas cara membagi sistem besar:",
                    "bahasa bersama dan bounded context. Sisi taktis membahas bentuk kodenya:",
                    "entity, value object, aggregate, repository, dan domain event. Sisi",
                    "strategis berguna hampir di semua proyek. Sisi taktis baru sepadan untuk",
                    "domain yang rumit.",
                ],
            },
            {
                "heading": "Ubiquitous language: satu bahasa bersama",
                "body": [
                    "Ubiquitous language adalah bahasa yang sama dipakai orang bisnis dan",
                    "kode. Kalau pengurus koperasi sekolah bilang \"anggota\", \"simpanan",
                    "wajib\", dan \"sisa hasil usaha\", kode juga memakai kata-kata itu,",
                    "misalnya kelas Anggota dan fungsi hitung_sisa_hasil_usaha(). Jangan",
                    "diterjemahkan jadi user, deposit_type_2, atau calc_profit().",
                    "",
                    "Manfaatnya terasa saat berdiskusi. Pengurus bisa membaca nama fungsi dan",
                    "langsung mengoreksi aturannya, dan programmer baru nggak perlu kamus",
                    "terjemahan antara rapat dan kode. Mulailah dengan glosarium kecil yang",
                    "ditulis bersama.",
                ],
            },
            {
                "heading": "Bounded context: kata sama, arti beda",
                "body": [
                    "Di toko online, kata \"produk\" punya arti berbeda bagi tiap bagian:",
                    "",
                    "  - Bagi etalase: nama, deskripsi, foto, dan kategori.",
                    "  - Bagi gudang: SKU, berat, ukuran kardus, dan lokasi rak.",
                    "  - Bagi keuangan: harga pokok, pajak, dan margin.",
                    "",
                    "Memaksa semuanya jadi satu kelas Produk dengan 40 atribut membuat setiap",
                    "tim saling mengganggu. DDD menyarankan bounded context: batas tempat",
                    "sebuah model berlaku. Di dalam konteks Gudang, Produk berarti barang",
                    "fisik. Di dalam konteks Etalase, Produk berarti isi yang dipajang.",
                    "Keduanya dihubungkan lewat ID dan terjemahan yang jelas.",
                    "",
                    "Bounded context sering jadi batas modul di monolit modular, dan kelak",
                    "bisa jadi batas layanan kalau sistemnya dipecah.",
                ],
            },
            {
                "heading": "Entity, value object, aggregate, dan domain event",
                "body": [
                    "  - Entity: punya identitas yang tetap walau atributnya berubah. Siswa",
                    "    yang pindah kelas tetap siswa yang sama karena nomor induknya sama.",
                    "  - Value object: ditentukan oleh nilainya dan nggak bisa diubah. Uang",
                    "    5.000 rupiah sama dengan uang 5.000 rupiah lain. Alamat dan rentang",
                    "    tanggal juga cocok jadi value object.",
                    "  - Aggregate: sekelompok objek dengan satu akar yang menjaga aturan.",
                    "    Pesanan beserta baris-barisnya diubah lewat objek Pesanan saja,",
                    "    supaya aturan seperti \"pesanan lunas nggak boleh ditambah\" nggak",
                    "    bisa dilewati.",
                    "  - Repository: tempat menyimpan dan mengambil aggregate. Contoh",
                    "    penerapannya di Java ada di kurikulum Bikin Aplikasi.",
                    "  - Domain event: kejadian penting di bisnis, dinamai dengan bentuk",
                    "    lampau, misalnya PesananDibayar.",
                    "",
                    "Program berikut menunjukkan value object Uang dan aggregate Pesanan:",
                ],
                "code": """from dataclasses import dataclass, field


@dataclass(frozen=True)
class Uang:                      # value object: sama kalau nilainya sama
    jumlah: int
    mata_uang: str = "IDR"

    def __add__(self, lain):
        if self.mata_uang != lain.mata_uang:
            raise ValueError("mata uang beda")
        return Uang(self.jumlah + lain.jumlah, self.mata_uang)


@dataclass
class Pesanan:                   # aggregate root: satu-satunya pintu ubah
    nomor: str
    baris: list = field(default_factory=list)
    lunas: bool = False
    kejadian: list = field(default_factory=list)

    def tambah(self, barang, harga: Uang, jumlah):
        if self.lunas:
            raise ValueError("pesanan sudah lunas, nggak bisa ditambah")
        if jumlah <= 0:
            raise ValueError("jumlah harus positif")
        self.baris.append((barang, harga, jumlah))

    def total(self):
        hasil = Uang(0)
        for _, harga, jumlah in self.baris:
            hasil = hasil + Uang(harga.jumlah * jumlah, harga.mata_uang)
        return hasil

    def bayar(self):
        self.lunas = True
        self.kejadian.append(("PesananDibayar", self.nomor, self.total().jumlah))


p = Pesanan("A17")
p.tambah("buku", Uang(45_000), 2)
p.tambah("pena", Uang(5_000), 3)
print(p.total())
print(Uang(5_000) == Uang(5_000))
p.bayar()
print(p.kejadian)
try:
    p.tambah("map", Uang(3_000), 1)
except ValueError as e:
    print("ditolak:", e)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Uang(jumlah=105000, mata_uang='IDR')",
                    "  True",
                    "  [('PesananDibayar', 'A17', 105000)]",
                    "  ditolak: pesanan sudah lunas, nggak bisa ditambah",
                    "",
                    "frozen=True membuat Uang nggak bisa diubah sesudah dibuat, dan dataclass",
                    "otomatis membandingkan dua objek Uang dari nilainya. Pesanan menolak",
                    "tambahan setelah lunas, dan pembayaran mencatat domain event yang bisa",
                    "dipakai bagian lain, misalnya modul gudang yang perlu mengurangi stok.",
                ],
            },
            {
                "heading": "Vertical slice: menyusun per fitur",
                "body": [
                    "Jimmy Bogard menulis tentang vertical slice architecture pada 19 April",
                    "2018. Kode disusun per fitur atau per jenis request, dari penanganan",
                    "request sampai akses data, alih-alih per lapisan teknis. Prinsipnya:",
                    "keterikatan antar irisan dibuat sekecil mungkin, keterikatan di dalam",
                    "satu irisan boleh sebesar yang dibutuhkan.",
                    "",
                    "  Per lapisan                   Per fitur (vertical slice)",
                    "  ----------------------------  ----------------------------",
                    "  controllers/                  daftar_produk/",
                    "    produk.py                     handler.py",
                    "    pesanan.py                    query.sql",
                    "  services/                     buat_pesanan/",
                    "    produk.py                     handler.py",
                    "    pesanan.py                    validasi.py",
                    "  repositories/                 bayar_pesanan/",
                    "    produk.py                     handler.py",
                    "    pesanan.py",
                    "",
                    "Untuk mengubah alur buat pesanan, susunan kiri memaksamu membuka tiga",
                    "folder. Susunan kanan cukup satu folder. Vertical slice populer di",
                    "komunitas .NET dan sering dipadukan dengan CQRS, pola yang dibahas di",
                    "bab Arsitektur Terdistribusi.",
                ],
            },
            {
                "heading": "Memakai keduanya dengan takaran yang pas",
                "body": [
                    "DDD dan vertical slice bisa dipakai bareng. DDD memberi batas besar",
                    "berupa bounded context. Vertical slice menata kode di dalam tiap batas",
                    "itu per fitur.",
                    "",
                    "Takarannya perlu dijaga. Untuk aplikasi CRUD sederhana, aggregate dan",
                    "domain event cuma menambah upacara. Bahasa bersama dan bounded context",
                    "hampir selalu berguna, bahkan untuk aplikasi kecil, karena keduanya soal",
                    "memahami bisnis. Jumlah berkasnya nggak bertambah karena itu.",
                    "",
                    "Untuk menemukan domain event dan batas konteks bersama orang bisnis,",
                    "banyak tim memakai lokakarya event storming: semua kejadian penting",
                    "ditulis di kertas tempel, lalu disusun di dinding sesuai urutan waktu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "DDD banyak dipakai di sistem dengan aturan bisnis rumit: aplikasi",
                    "logistik dan kurir, perbankan, asuransi, dan sistem informasi rumah",
                    "sakit. Vertical slice sering dipakai di aplikasi web dengan banyak fitur",
                    "yang saling lepas.",
                    "",
                    "Kasus kecil: di sebuah toko online, tim gudang dan tim pemasaran",
                    "sama-sama bilang \"produk\", tapi maksudnya berbeda. Satu tabel produk",
                    "berisi 40 kolom, dan perubahan dari satu tim berkali-kali merusak",
                    "halaman tim lain.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Wawancarai kedua tim dan tulis glosarium: apa arti produk bagi",
                    "     masing-masing.",
                    "  2. Akui ada dua bounded context, Etalase dan Gudang.",
                    "  3. Pisahkan modelnya. Etalase menyimpan nama, deskripsi, dan foto.",
                    "     Gudang menyimpan SKU, berat, dan lokasi rak.",
                    "  4. Hubungkan keduanya lewat ID produk dan domain event, misalnya",
                    "     StokHabis dari Gudang yang membuat Etalase menampilkan label",
                    "     \"habis\".",
                    "  5. Di dalam tiap konteks, susun kodenya per fitur supaya satu",
                    "     perubahan cukup menyentuh satu folder.",
                ],
            },
        ],
    },
    {
        "title": "25. MVVM, Aliran Data Satu Arah, dan Pola Lainnya",
        "sections": [
            {
                "body": [
                    "Materi ini peta pola yang akan kamu temui di framework UI, editor kode,",
                    "dan pipeline data. Tiap pola dapat penjelasan singkat dan contoh kecil.",
                    "Pendalamannya ada di kurikulum yang memakai pola itu sehari-hari.",
                ],
            },
            {
                "heading": "MVVM",
                "body": [
                    "MVVM (Model-View-ViewModel) diperkenalkan John Gossman dari Microsoft",
                    "sekitar 2005 untuk WPF. Model berisi data dan aturan bisnis. View adalah",
                    "tampilan. ViewModel menyimpan state dan perintah yang dibutuhkan",
                    "tampilan. View mengikat dirinya ke ViewModel lewat data binding, jadi",
                    "setiap kali state berubah, tampilannya ikut berubah tanpa disuruh.",
                    "",
                    "Pola ini dipakai .NET MAUI dan WPF, kelas ViewModel di Android Jetpack,",
                    "dan bentuk yang mirip ada di SwiftUI, Vue, serta Angular. Versi mininya:",
                ],
                "code": """class KeranjangViewModel:
    def __init__(self):
        self._jumlah = 0
        self._pengamat = []

    def amati(self, fungsi):            # View mengikat dirinya di sini
        self._pengamat.append(fungsi)
        fungsi(self.teks_tombol)

    @property
    def teks_tombol(self):
        return f"Keranjang ({self._jumlah})"

    def tambah_barang(self):             # perintah yang dipanggil View
        self._jumlah += 1
        for fungsi in self._pengamat:
            fungsi(self.teks_tombol)


vm = KeranjangViewModel()
vm.amati(lambda teks: print("tombol menampilkan:", teks))
vm.tambah_barang()
vm.tambah_barang()""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tombol menampilkan: Keranjang (0)",
                    "  tombol menampilkan: Keranjang (1)",
                    "  tombol menampilkan: Keranjang (2)",
                    "",
                    "View nggak menghitung apa pun. Ia cuma menampilkan teks_tombol dan",
                    "memanggil tambah_barang() saat diklik. Karena logikanya di ViewModel,",
                    "logika itu bisa dites tanpa layar sama sekali. Detail MVVM di Android",
                    "dibahas di kurikulum Mobile & Desktop.",
                ],
            },
            {
                "heading": "Aliran data satu arah",
                "body": [
                    "Kalau dua komponen menyimpan salinan data yang sama sendiri-sendiri,",
                    "cepat atau lambat keduanya berbeda. Aliran data satu arah mencegahnya",
                    "dengan aturan ketat:",
                    "",
                    "  1. State disimpan di satu tempat, yaitu store.",
                    "  2. Tampilan nggak mengubah state langsung. Ia mengirim aksi, misalnya",
                    "     {\"jenis\": \"tambah\", \"barang\": \"buku\"}.",
                    "  3. Fungsi reducer menghitung state baru dari state lama dan aksi itu.",
                    "  4. Tampilan digambar ulang dari state baru.",
                    "",
                    "Facebook memperkenalkan pola ini dengan nama Flux pada 2014. Redux",
                    "(2015) menyederhanakannya dan jadi standar di aplikasi React. Elm",
                    "Architecture menyebut bagian-bagiannya Model, View, Update. Di Android,",
                    "bentuk serupa disebut Model-View-Intent. Jetpack Compose dan Flutter",
                    "Bloc memakai ide yang sama. Per Oktober 2026, Redux Toolkit ada di versi",
                    "2.13.0, dan Zustand 5.0.15 jadi pilihan yang lebih ringan.",
                ],
                "code": "def reducer(state, aksi):\n    \"\"\"Fungsi murni: state lama + aksi -> state baru, tanpa mengubah yang lama.\"\"\"\n    if aksi[\"jenis\"] == \"tambah\":\n        isi = dict(state[\"isi\"])\n        isi[aksi[\"barang\"]] = isi.get(aksi[\"barang\"], 0) + 1\n        return {**state, \"isi\": isi}\n    if aksi[\"jenis\"] == \"hapus\":\n        isi = {k: v for k, v in state[\"isi\"].items() if k != aksi[\"barang\"]}\n        return {**state, \"isi\": isi}\n    return state\n\n\ndef tampilkan(state):\n    print(\"keranjang:\", state[\"isi\"])\n\n\nstate = {\"isi\": {}}\nfor aksi in [{\"jenis\": \"tambah\", \"barang\": \"buku\"},\n             {\"jenis\": \"tambah\", \"barang\": \"pena\"},\n             {\"jenis\": \"tambah\", \"barang\": \"buku\"},\n             {\"jenis\": \"hapus\", \"barang\": \"pena\"}]:\n    state = reducer(state, aksi)\n    tampilkan(state)",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  keranjang: {'buku': 1}",
                    "  keranjang: {'buku': 1, 'pena': 1}",
                    "  keranjang: {'buku': 2, 'pena': 1}",
                    "  keranjang: {'buku': 2}",
                    "",
                    "reducer() nggak pernah mengubah state lama. Ia selalu membuat dict baru.",
                    "Karena murni, deretan aksi yang sama selalu menghasilkan state yang",
                    "sama, jadi gampang dites dan gampang dilacak. Pengelolaan state di React",
                    "dibahas lebih dalam di kurikulum Frontend Modern.",
                ],
            },
            {
                "heading": "Microkernel: inti kecil, fitur lewat plugin",
                "body": [
                    "Arsitektur microkernel, atau arsitektur plugin, membuat inti aplikasi",
                    "kecil dan stabil. Fitur tambahan dipasang sebagai plugin lewat titik",
                    "ekstensi yang disediakan inti. Inti nggak tahu isi plugin. Ia cuma tahu",
                    "cara memuat dan memanggilnya.",
                    "",
                    "Kamu memakainya setiap hari. VS Code dan ekstensinya, WordPress dan",
                    "plugin-nya, Eclipse, serta browser dengan add-on, semuanya berbentuk",
                    "seperti ini. Untungnya, fitur bisa ditambah pihak lain tanpa menyentuh",
                    "inti. Risikonya, plugin yang buruk bisa memperlambat atau membobol",
                    "seluruh aplikasi. Situs WordPress dengan plugin yang lama nggak",
                    "diperbarui adalah contoh klasik risiko ini.",
                ],
            },
            {
                "heading": "Pipes and filters",
                "body": [
                    "Kamu sudah kenal pola ini dari kurikulum Bash:",
                    "",
                    "  cat app.log | grep ERROR | sort | uniq -c",
                    "",
                    "Pemrosesan dipecah jadi langkah kecil yang disebut filter. Setiap filter",
                    "membaca masukan, mengerjakan satu hal, lalu menulis keluaran. Pipe",
                    "menyambungkan keluaran satu filter ke masukan filter berikutnya. Filter",
                    "bisa ditukar, dipakai ulang, dan diuji sendiri-sendiri, tapi urutannya",
                    "menentukan hasil.",
                    "",
                    "Pola yang sama ada di pipeline ETL, di compiler (lexer, parser,",
                    "optimizer, pembuat kode), dan di middleware framework web. Panduan Azure",
                    "Architecture Center menambahkan satu syarat kalau antarfilter ada",
                    "antrean: filter harus tahan menerima pesan yang sama dua kali. Di",
                    "Python, generator cocok untuk filter karena data mengalir satu per satu:",
                ],
                "code": """log = [
    "08:00 INFO pesanan dibuat oleh sari@contoh.id",
    "08:01 ERROR pembayaran gagal untuk budi@contoh.id",
    "08:02 INFO stok diperbarui",
    "08:03 ERROR kurir tidak merespons",
]


def saring_error(baris):
    for b in baris:
        if " ERROR " in b:
            yield b


def sensor_email(baris):
    for b in baris:
        yield " ".join("***" if "@" in kata else kata for kata in b.split())


def nomori(baris):
    for i, b in enumerate(baris, 1):
        yield f"{i}. {b}"


for hasil in nomori(sensor_email(saring_error(log))):
    print(hasil)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  1. 08:01 ERROR pembayaran gagal untuk ***",
                    "  2. 08:03 ERROR kurir tidak merespons",
                    "",
                    "Setiap baris log mengalir lewat tiga filter satu per satu, tanpa list",
                    "perantara. Tukar urutan sensor_email dan saring_error, hasilnya tetap",
                    "sama. Tukar nomori ke paling depan, nomornya jadi 2 dan 4 karena",
                    "dihitung sebelum penyaringan. Latihan bab ini membangun pipeline yang",
                    "urutannya dibaca dari input.",
                ],
            },
            {
                "heading": "Peer-to-peer dan peta singkat",
                "body": [
                    "Di arsitektur peer-to-peer (P2P), setiap simpul jadi klien sekaligus",
                    "server, dan nggak ada pusat tunggal. BitTorrent membagi potongan berkas",
                    "antarpengguna. WebRTC membuat panggilan video tersambung langsung",
                    "antarbrowser, walau tetap butuh server kecil untuk mempertemukan",
                    "keduanya di awal. Blockchain juga P2P. Kelebihannya: nggak ada satu",
                    "titik yang membuat semuanya mati, dan kapasitas bertambah seiring jumlah",
                    "pengguna. Kekurangannya: sulit dikendalikan, sulit diamankan, dan rumit",
                    "saat simpulnya berada di balik NAT.",
                    "",
                    "Ringkasan pola di materi ini:",
                    "",
                    "  Pola                 Kamu temui di               Kurikulum lanjut",
                    "  -------------------  --------------------------  ----------------",
                    "  MVVM                 Android, .NET MAUI, WPF     Mobile & Desktop",
                    "  Aliran satu arah     React + Redux, Compose      Frontend Modern",
                    "  Microkernel          VS Code, WordPress          -",
                    "  Pipes and filters    shell, ETL, middleware      Bash, Data",
                    "  Peer-to-peer         BitTorrent, WebRTC          -",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Android modern memakai ViewModel, toko online berbasis React",
                    "memakai store untuk keranjang, editor seperti VS Code hidup dari",
                    "ekstensi, dan server memproses log lewat rangkaian filter.",
                    "",
                    "Kasus kecil: di toko online berbasis React, ikon keranjang di header",
                    "kadang menunjukkan 3 barang, padahal halaman keranjang menunjukkan 2.",
                    "Ternyata kedua komponen menyimpan salinan jumlah barangnya",
                    "masing-masing.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tentukan satu sumber data: state keranjang disimpan di satu store.",
                    "  2. Ubah kedua komponen supaya cuma membaca dari store, nggak lagi",
                    "     menyimpan salinan sendiri.",
                    "  3. Semua perubahan lewat aksi, misalnya tambah dan hapus.",
                    "  4. Tulis reducer murni untuk aksi-aksi itu, lalu tes dengan deretan",
                    "     aksi seperti contoh di atas.",
                    "  5. Pastikan ikon dan halaman keranjang menampilkan angka dari state",
                    "     yang sama setelah setiap aksi.",
                ],
            },
        ],
    },
    {
        "title": "26. Skalabilitas, Stateless, dan Estimasi Kasar",
        "sections": [
            {
                "body": [
                    "Skalabilitas adalah kemampuan sistem menangani beban yang bertambah",
                    "tanpa harus ditulis ulang. Bedakan dari kinerja. Masalah kinerja artinya",
                    "aplikasi lambat bahkan untuk satu pengguna. Masalah skalabilitas artinya",
                    "aplikasi cepat untuk satu pengguna, tapi melambat atau tumbang waktu",
                    "ramai.",
                    "",
                    "Bab ini dan dua bab berikutnya membahas system design, yaitu cara",
                    "merancang sistem supaya tetap jalan saat penggunanya bertambah. Rujukan",
                    "gratis yang paling sering dipakai adalah System Design Primer di GitHub",
                    "(berlisensi CC BY 4.0, sekitar 375 ribu bintang saat dicek Oktober 2026)",
                    "dan roadmap System Design di roadmap.sh.",
                ],
            },
            {
                "heading": "Vertikal atau horizontal",
                "body": [
                    "Ada dua cara menambah tenaga:",
                    "",
                    "  - Skala vertikal: membesarkan satu mesin, misalnya dari 2 CPU dan 4 GB",
                    "    RAM jadi 16 CPU dan 64 GB. Caranya gampang dan kodenya nggak perlu",
                    "    diubah. Batasnya adalah mesin terbesar yang bisa dibeli, dan kalau",
                    "    mesin itu mati, semuanya ikut mati.",
                    "  - Skala horizontal: menambah jumlah mesin, lalu membagi request di",
                    "    antara mereka dengan load balancer. Batasnya jauh lebih longgar, dan",
                    "    satu mesin mati nggak menjatuhkan semuanya. Syaratnya, aplikasinya",
                    "    harus siap dijalankan di banyak mesin sekaligus.",
                    "",
                    "Banyak aplikasi bisa bertahan lama hanya dengan skala vertikal. Satu",
                    "server database yang besar sanggup melayani beban yang mengejutkan",
                    "banyaknya. Skala horizontal baru wajib saat satu mesin sudah nggak",
                    "cukup, atau saat kamu butuh tetap hidup ketika satu mesin mati.",
                ],
            },
            {
                "heading": "Stateless: syarat sebelum memperbanyak server",
                "body": [
                    "State artinya data yang diingat aplikasi di antara dua request, misalnya",
                    "sesi login, isi keranjang, atau berkas yang baru diunggah. Server yang",
                    "menyimpan state di memorinya sendiri disebut stateful. Masalahnya muncul",
                    "begitu ada dua server:",
                ],
                "code": """class Server:
    def __init__(self, nama, penyimpanan_sesi):
        self.nama = nama
        self.sesi = penyimpanan_sesi

    def login(self, token, pengguna):
        self.sesi[token] = pengguna

    def profil(self, token):
        pengguna = self.sesi.get(token)
        sapaan = f"halo {pengguna}" if pengguna else "silakan login dulu"
        return f"server {self.nama}: {sapaan}"


# Stateful: tiap server menyimpan sesi di memorinya sendiri
a, b = Server("A", {}), Server("B", {})
a.login("tok-1", "sari")
print(a.profil("tok-1"))
print(b.profil("tok-1"))          # request berikutnya jatuh ke server B

# Stateless: sesi disimpan di satu tempat bersama, misalnya Redis/Valkey
bersama = {}
a, b = Server("A", bersama), Server("B", bersama)
a.login("tok-1", "sari")
print(b.profil("tok-1"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  server A: halo sari",
                    "  server B: silakan login dulu",
                    "  server B: halo sari",
                    "",
                    "Sari sudah login di server A, tapi request keduanya dilempar load",
                    "balancer ke server B yang nggak kenal dia. Supaya server bisa",
                    "diperbanyak, server harus stateless: semua state disimpan di luar",
                    "server, sehingga request mana pun boleh dilayani server mana pun.",
                    "Pilihannya:",
                    "",
                    "  - Penyimpanan sesi bersama, misalnya Redis, Valkey, atau database.",
                    "  - Token yang dibawa klien sendiri, misalnya JWT. Untung ruginya",
                    "    dibahas di bab Operasi, Rilis, dan Keamanan Arsitektur.",
                    "  - Berkas unggahan disimpan di penyimpanan objek seperti S3, jangan di",
                    "    disk lokal server.",
                    "  - Sticky session: load balancer selalu mengirim pengguna yang sama ke",
                    "    server yang sama. Cara ini cepat dipasang, tapi bebannya jadi nggak",
                    "    rata, dan sesi hilang kalau server itu mati.",
                ],
            },
            {
                "heading": "Latensi, throughput, dan persentil",
                "body": [
                    "Latensi adalah waktu yang dibutuhkan satu request sampai selesai.",
                    "Throughput adalah jumlah request yang bisa diselesaikan per detik.",
                    "Keduanya berbeda: jalan tol bisa punya throughput tinggi karena lajurnya",
                    "banyak, walau tiap mobil tetap butuh waktu yang sama untuk sampai.",
                    "",
                    "Rata-rata waktu respons sering menyesatkan. Pengguna merasakan request",
                    "yang lambat, dan request lambat tersembunyi di dalam rata-rata. Karena",
                    "itu orang memakai persentil. p95 artinya 95% request selesai dalam waktu",
                    "itu atau lebih cepat. p99 menunjukkan ekor paling lambat:",
                ],
                "code": "waktu_ms = [42, 38, 45, 40, 41, 39, 44, 43, 37, 1200,\n            40, 42, 39, 41, 46, 38, 40, 43, 44, 980]\n\n\ndef persentil(data, p):\n    \"\"\"Metode nearest-rank: ambil nilai ke-ceil(p% x n) dari data urut.\"\"\"\n    urut = sorted(data)\n    peringkat = -(-len(urut) * p // 100)       # pembulatan ke atas\n    return urut[max(peringkat, 1) - 1]\n\n\nprint(f\"rata-rata: {sum(waktu_ms) / len(waktu_ms):.1f} ms\")\nfor p in (50, 95, 99):\n    print(f\"p{p}: {persentil(waktu_ms, p)} ms\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  rata-rata: 146.1 ms",
                    "  p50: 41 ms",
                    "  p95: 980 ms",
                    "  p99: 1200 ms",
                    "",
                    "Rata-ratanya 146 ms dan kelihatan wajar. Padahal 18 dari 20 request",
                    "selesai sekitar 40 ms, sedangkan dua sisanya butuh lebih dari 900 ms.",
                    "p50 menunjukkan pengalaman pengguna biasa, dan p95 serta p99 menunjukkan",
                    "siapa yang menderita. Kalau satu halaman memanggil sepuluh layanan,",
                    "peluang salah satunya kena ekor lambat jauh lebih besar daripada satu",
                    "persen.",
                    "",
                    "Untuk perkiraan, programmer memakai angka patokan klasik yang",
                    "dikumpulkan System Design Primer. Perangkat keras sekarang lebih cepat,",
                    "jadi yang penting perbandingannya, bukan angka persisnya:",
                    "",
                    "  baca dari memori utama           sekitar 100 ns",
                    "  baca 1 MB berurutan dari memori  sekitar 250 mikrodetik",
                    "  bolak-balik di satu pusat data   sekitar 500 mikrodetik",
                    "  baca 1 MB berurutan dari SSD     sekitar 1 ms",
                    "  seek di harddisk                 sekitar 10 ms",
                    "  bolak-balik antarbenua           sekitar 150 ms",
                ],
            },
            {
                "heading": "Estimasi kasar",
                "body": [
                    "Estimasi kasar, atau back-of-the-envelope, adalah hitungan cepat di",
                    "kertas untuk mengira kebutuhan sebelum membangun. Angkanya nggak harus",
                    "persis. Yang dicari adalah urutan besarnya: puluhan, ribuan, atau jutaan",
                    "request per detik? Patokan pentingnya: satu hari ada 86.400 detik,",
                    "kira-kira 100 ribu. Misalnya ada 10 juta pengguna aktif harian,",
                    "masing-masing membuat 5 request:",
                ],
                "code": """pengguna_harian = 10_000_000
request_per_pengguna = 5
detik_sehari = 24 * 60 * 60                  # 86.400, kira-kira 10^5

total = pengguna_harian * request_per_pengguna
rata_rps = total / detik_sehari
puncak_rps = rata_rps * 3                    # asumsi: jam sibuk 3x rata-rata
log_gb_per_hari = total * 1 / 1_000_000      # 1 KB per request

print(f"request per hari : {total:,}")
print(f"rata-rata        : {rata_rps:.0f} request/detik")
print(f"puncak (3x)      : {puncak_rps:.0f} request/detik")
print(f"log per hari     : {log_gb_per_hari:.0f} GB")
print(f"log per tahun    : {log_gb_per_hari * 365 / 1000:.1f} TB")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  request per hari : 50,000,000",
                    "  rata-rata        : 579 request/detik",
                    "  puncak (3x)      : 1736 request/detik",
                    "  log per hari     : 50 GB",
                    "  log per tahun    : 18.2 TB",
                    "",
                    "Python memakai koma sebagai pemisah ribuan di format {:,}. Dari angka",
                    "ini kamu bisa lanjut menghitung. Kalau uji beban menunjukkan satu server",
                    "sanggup 500 request per detik, jam sibuk butuh 4 server, ditambah satu",
                    "cadangan kalau ada yang mati. Log 18 TB per tahun berarti kamu perlu",
                    "aturan berapa lama log disimpan sebelum dihapus.",
                    "",
                    "Jebakan: mengoptimasi sebelum mengukur. Banyak tim memasang cache dan",
                    "antrean di aplikasi yang penggunanya baru ratusan. Ukur dulu dengan uji",
                    "beban, misalnya memakai k6, baru tambah komponen di bagian yang terbukti",
                    "jadi hambatan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs pendaftaran sekolah, penjualan tiket konser, dan flash sale toko",
                    "online punya pola yang sama: sepi hampir sepanjang waktu, lalu dibanjiri",
                    "pengguna di jam tertentu.",
                    "",
                    "Kasus kecil: pendaftaran ekskul di sekolahmu dibuka serentak jam 07.00",
                    "untuk 1.200 siswa. Tahun lalu servernya tumbang. Waktu server kedua",
                    "ditambahkan, siswa yang sudah login malah sering ter-logout sendiri.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Estimasi dulu. Kalau tiap siswa membuat sekitar 10 request dalam 5",
                    "     menit pertama, totalnya 12.000 request dalam 300 detik, atau 40",
                    "     request per detik rata-rata. Puncaknya bisa beberapa kali lipat.",
                    "  2. Ukur kemampuan satu server dengan uji beban sebelum hari",
                    "     pendaftaran.",
                    "  3. Pindahkan sesi dari memori server ke Redis, Valkey, atau database",
                    "     supaya server jadi stateless. Masalah ter-logout tadi persis gejala",
                    "     sesi yang tertinggal di server A.",
                    "  4. Baru tambah server di belakang load balancer sesuai hasil hitungan.",
                    "  5. Saat hari H, pantau p95 dan p99, jangan cuma rata-rata.",
                ],
            },
        ],
    },
    {
        "title": "27. Load Balancer dan Reverse Proxy",
        "sections": [
            {
                "body": [
                    "Reverse proxy adalah server perantara yang berdiri di depan aplikasimu.",
                    "Pengguna mengira sedang bicara dengan aplikasimu, padahal semua request",
                    "diterima proxy dulu, lalu diteruskan ke server di belakangnya.",
                    "Kebalikannya, forward proxy berdiri di depan klien, misalnya proxy",
                    "kantor yang mewakili karyawan saat membuka internet.",
                    "",
                    "Load balancer membagi request ke beberapa server supaya nggak ada yang",
                    "kewalahan, dan berhenti mengirim ke server yang mati. Dua peran ini",
                    "sering dikerjakan program yang sama. Nginx, misalnya, bisa jadi reverse",
                    "proxy sekaligus load balancer.",
                ],
            },
            {
                "heading": "Kerja reverse proxy",
                "body": [
                    "  - Terminasi TLS: proxy yang mengurus HTTPS, jadi aplikasi di",
                    "    belakangnya cukup bicara HTTP biasa di jaringan internal.",
                    "  - Routing per alamat: /api diteruskan ke backend, alamat lain ke",
                    "    server frontend.",
                    "  - Kompresi dan cache untuk berkas statis.",
                    "  - Membatasi akses dan jumlah request, serta menyembunyikan alamat",
                    "    server asli.",
                    "",
                    "Menurut W3Techs (19 Oktober 2026), server yang paling sering terlihat di",
                    "depan situs web adalah Cloudflare Server (32,5%) dan Nginx (30,3%).",
                    "Caddy 1,1% dan Envoy 0,5%. Angka itu mengukur program yang menjawab",
                    "request di depan, jadi banyak di antaranya bekerja sebagai reverse",
                    "proxy.",
                ],
            },
            {
                "heading": "Algoritma pembagian",
                "body": [
                    "Load balancer harus memutuskan request ini dikirim ke server mana.",
                    "Algoritma yang paling umum:",
                    "",
                    "  - Round-robin: bergiliran. A, B, C, lalu kembali ke A. Ini bawaan",
                    "    Nginx.",
                    "  - Weighted round-robin: server yang lebih kuat diberi bobot lebih",
                    "    besar. Dengan bobot A=3, B=1, C=1, dari tiap lima request A mendapat",
                    "    tiga.",
                    "  - Least connections: request baru dikirim ke server dengan koneksi",
                    "    aktif paling sedikit. Cocok kalau durasi request beragam, karena",
                    "    server yang sedang mengerjakan request panjang nggak terus ditimpa.",
                    "  - IP hash: alamat IP yang sama selalu ke server yang sama. Ini salah",
                    "    satu cara membuat sticky session.",
                    "",
                    "Round-robin paling sederhana. itertools.cycle di Python sudah cukup",
                    "untuk menirunya:",
                ],
                "code": """from itertools import cycle

server = ["A", "B", "C"]
giliran = cycle(server)
for nomor in range(1, 8):
    print(f"request {nomor} -> server {next(giliran)}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  request 1 -> server A",
                    "  request 2 -> server B",
                    "  request 3 -> server C",
                    "  request 4 -> server A",
                    "  request 5 -> server B",
                    "  request 6 -> server C",
                    "  request 7 -> server A",
                    "",
                    "Weighted round-robin di Nginx memakai versi yang disebut smooth weighted",
                    "round-robin. Server berbobot besar nggak mendapat jatahnya",
                    "berturut-turut; jatahnya diselang-seling, sehingga urutan untuk bobot 3,",
                    "1, 1 menjadi A, B, A, C, A. Latihan bab ini memintamu menirunya.",
                    "",
                    "Jebakan: round-robin menganggap semua request sama berat. Kalau satu",
                    "request butuh 30 detik dan lainnya 10 ms, server yang kebagian request",
                    "berat jadi menumpuk antrean sementara server lain menganggur. Untuk pola",
                    "seperti itu, least connections lebih adil.",
                ],
            },
            {
                "heading": "Health check: kalau satu server mati",
                "body": [
                    "Load balancer perlu tahu server mana yang masih sehat. Ada dua cara:",
                    "",
                    "  - Aktif: load balancer rutin membuka alamat seperti /health di tiap",
                    "    server. Server yang gagal menjawab ditandai mati.",
                    "  - Pasif: load balancer menghitung kegagalan request biasa. Di Nginx,",
                    "    max_fails dan fail_timeout menentukan berapa kali gagal dalam",
                    "    rentang waktu tertentu sebelum server dilewati. Nilai bawaannya 1",
                    "    kali dan 10 detik.",
                    "",
                    "Server yang ditandai mati dilewati, lalu dicoba lagi setelah masa",
                    "tunggunya habis. Contoh konfigurasi Nginx berikut membagi request ke",
                    "tiga server dengan least connections, memberi bobot, menyetel batas",
                    "gagal, dan menyiapkan satu server cadangan yang baru dipakai kalau dua",
                    "lainnya mati:",
                ],
                "bahasa": "nginx",
                "code": """upstream toko_backend {
    least_conn;
    server 10.0.0.11:8000 weight=3;
    server 10.0.0.12:8000 max_fails=3 fail_timeout=30s;
    server 10.0.0.13:8000 backup;
}

server {
    listen 80;
    server_name toko.contoh.id;

    location / {
        proxy_pass http://toko_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}""",
            },
            {
                "heading": "L4 dan L7",
                "body": [
                    "Load balancer dibedakan menurut lapisan jaringan yang dibacanya. Load",
                    "balancer L4 bekerja di lapisan transport (TCP atau UDP). Ia cuma melihat",
                    "alamat IP dan port, nggak membuka isi request, jadi cepat dan bisa",
                    "dipakai untuk protokol apa pun.",
                    "",
                    "Load balancer L7 bekerja di lapisan aplikasi, biasanya HTTP. Ia membaca",
                    "path, header, dan cookie, sehingga bisa meneruskan /api ke satu kelompok",
                    "server dan /gambar ke kelompok lain, sekaligus mengurus HTTPS. Di AWS,",
                    "Network Load Balancer bekerja di L4 dan Application Load Balancer di L7.",
                ],
            },
            {
                "heading": "Pilihan perangkatnya",
                "body": [
                    "  Perangkat  Versi (Okt 2026)  Lisensi     Kekuatan",
                    "  ---------  ----------------  ----------  ----------------------------",
                    "  Nginx      1.30.6 stable     BSD-2       web server + proxy + LB",
                    "  HAProxy    cabang LTS 3.4    GPL-2.0     LB TCP/HTTP khusus, cepat",
                    "  Caddy      2.11.7            Apache-2.0  HTTPS otomatis",
                    "  Traefik    3.7.15            MIT         membaca label Docker/K8s",
                    "  Envoy      1.40.0            Apache-2.0  proxy untuk service mesh",
                    "",
                    "Nginx memakai nomor minor genap untuk cabang stable dan ganjil untuk",
                    "cabang mainline (1.31.7 per Oktober 2026). Caddy enak untuk pemula",
                    "karena HTTPS-nya jalan sendiri lewat Let's Encrypt. Traefik membaca",
                    "label kontainer Docker atau Kubernetes lalu menyusun rutenya otomatis.",
                    "Envoy biasanya dikonfigurasi lewat API, jarang ditulis tangan, dan jadi",
                    "dasar banyak service mesh.",
                    "",
                    "Di cloud, kamu biasanya menyewa load balancer jadi, seperti Elastic Load",
                    "Balancing di AWS atau Cloud Load Balancing di Google Cloud. Cara",
                    "memasang dan merawat semuanya di produksi dibahas di kurikulum DevOps &",
                    "Cloud.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang berjalan di dua atau tiga VPS biasanya memasang Nginx",
                    "di depan semuanya. Aplikasi yang dijalankan dengan Docker Compose sering",
                    "memakai Traefik atau Caddy sebagai pintu masuk.",
                    "",
                    "Kasus kecil: sebuah toko online punya dua server, satu lama dengan 2 CPU",
                    "dan satu baru dengan 8 CPU. Dengan round-robin, server lama selalu",
                    "kewalahan saat promo, sementara server baru santai.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Beri bobot sesuai kemampuan, misalnya server baru weight=4 dan",
                    "     server lama weight=1:",
                    "       upstream toko {",
                    "           server 10.0.0.21:8000 weight=4;",
                    "           server 10.0.0.20:8000 weight=1;",
                    "       }",
                    "  2. Kalau durasi request-nya beragam, pertimbangkan least_conn supaya",
                    "     server yang sibuk nggak terus ditimpa.",
                    "  3. Setel max_fails dan fail_timeout supaya server yang macet dilewati.",
                    "  4. Tambahkan alamat /health di aplikasi untuk dicek secara aktif.",
                    "  5. Uji dengan mematikan satu server di jam sepi. Pengguna harus tetap",
                    "     terlayani.",
                ],
            },
        ],
    },
    {
        "title": "28. Caching dan CDN",
        "sections": [
            {
                "body": [
                    "Cache adalah salinan data yang sering dibaca, ditaruh di tempat yang",
                    "lebih cepat dijangkau. Mirip buku yang sering kamu buka: kamu taruh di",
                    "meja, nggak dikembalikan ke rak perpustakaan setiap selesai membaca.",
                    "",
                    "Cache ada di banyak lapisan sekaligus:",
                    "",
                    "  - Browser menyimpan gambar, CSS, dan JavaScript sesuai header HTTP",
                    "    dari server.",
                    "  - CDN menyimpan salinan berkas di lokasi yang dekat dengan pengguna.",
                    "  - Aplikasi menyimpan hasil query atau hitungan mahal di memori,",
                    "    misalnya di Redis, Valkey, atau Memcached.",
                    "  - Database punya cache sendiri untuk halaman data yang sering dibaca.",
                ],
            },
            {
                "heading": "Cache-aside",
                "body": [
                    "Pola yang paling sering dipakai di aplikasi disebut cache-aside.",
                    "Aplikasi mengecek cache dulu. Kalau ada (hit), pakai. Kalau nggak ada",
                    "(miss), ambil dari database, simpan ke cache dengan masa berlaku, lalu",
                    "kembalikan. Masa berlaku itu disebut TTL (time to live). Program berikut",
                    "memakai jam palsu supaya hasilnya selalu sama:",
                ],
                "code": """db = {"produk:1": "Buku Tulis 38 lembar, Rp5.000"}
cache = {}            # kunci -> (nilai, kedaluwarsa_pada)
jam = 0               # jam palsu, dalam detik
TTL = 60


def ambil(kunci):
    data = cache.get(kunci)
    if data and data[1] > jam:
        return "HIT", data[0]
    nilai = db[kunci]                    # query lambat ke database
    cache[kunci] = (nilai, jam + TTL)
    return "MISS", nilai


def ubah_harga(kunci, nilai_baru):
    db[kunci] = nilai_baru               # 1. perbarui database dulu
    cache.pop(kunci, None)               # 2. baru hapus dari cache


for jam in (0, 10, 30):
    print(jam, *ambil("produk:1"))
ubah_harga("produk:1", "Buku Tulis 38 lembar, Rp5.500")
jam = 40
print(jam, *ambil("produk:1"))
jam = 120
print(jam, *ambil("produk:1"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  0 MISS Buku Tulis 38 lembar, Rp5.000",
                    "  10 HIT Buku Tulis 38 lembar, Rp5.000",
                    "  30 HIT Buku Tulis 38 lembar, Rp5.000",
                    "  40 MISS Buku Tulis 38 lembar, Rp5.500",
                    "  120 MISS Buku Tulis 38 lembar, Rp5.500",
                    "",
                    "Detik 0 kena miss dan mengisi cache. Detik 10 dan 30 kena hit tanpa",
                    "menyentuh database. Waktu harga berubah, data di database diperbarui",
                    "dulu, baru kunci cache-nya dihapus, jadi detik 40 membaca harga baru.",
                    "Detik 120 kena miss lagi karena TTL-nya habis di detik 100.",
                    "",
                    "Urutan \"database dulu, baru hapus cache\" disengaja. Panduan cache-aside",
                    "di Azure Architecture Center menjelaskan alasannya. Kalau cache dihapus",
                    "duluan, request lain bisa membaca database yang belum diperbarui, lalu",
                    "menyimpan harga lama itu ke cache lagi.",
                    "",
                    "Pola lain yang perlu kamu kenal:",
                    "",
                    "  - Write-through: setiap tulis langsung ke cache dan database",
                    "    bersamaan. Cache selalu segar, tapi menulis jadi lebih lambat.",
                    "  - Write-behind: tulis ke cache dulu, database diperbarui belakangan.",
                    "    Cepat, tapi data bisa hilang kalau cache mati sebelum sempat",
                    "    disalin.",
                    "  - Read-through: pustaka cache yang mengambil data dari database",
                    "    sendiri saat miss, jadi kode aplikasi cuma bicara dengan cache.",
                ],
            },
            {
                "heading": "TTL, eviction, dan LRU",
                "body": [
                    "Memori cache terbatas. Saat penuh, sebagian isi harus dibuang, dan",
                    "pembuangan ini disebut eviction. Aturan yang paling umum adalah LRU",
                    "(least recently used): buang yang paling lama nggak dipakai.",
                    "Alternatifnya LFU (paling jarang dipakai) dan FIFO (paling dulu masuk).",
                    "TTL dan eviction itu dua hal berbeda. TTL membuang data yang basi,",
                    "eviction membuang data supaya muat.",
                    "",
                    "Contoh LRU berkapasitas 3:",
                    "",
                    "  PUT pena   -> [pena]",
                    "  PUT buku   -> [pena, buku]",
                    "  PUT map    -> [pena, buku, map]",
                    "  GET pena   -> [buku, map, pena]     pena jadi paling baru",
                    "  PUT tas    -> [map, pena, tas]      buku dikeluarkan",
                    "",
                    "Python punya dekorator functools.lru_cache yang menerapkan aturan ini",
                    "untuk hasil fungsi:",
                ],
                "code": """from functools import lru_cache

panggilan_db = 0


@lru_cache(maxsize=2)
def harga(kode):
    global panggilan_db
    panggilan_db += 1                    # anggap ini query ke database
    return {"A1": 5000, "B2": 12000, "C3": 3000}[kode]


for kode in ["A1", "A1", "B2", "C3", "A1"]:
    harga(kode)
print("panggilan ke database:", panggilan_db)
print(harga.cache_info())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  panggilan ke database: 4",
                    "  CacheInfo(hits=1, misses=4, maxsize=2, currsize=2)",
                    "",
                    "Dengan kapasitas 2, panggilan C3 membuang A1, sehingga A1 yang terakhir",
                    "kena miss lagi. Dari lima panggilan, cuma satu yang hit. Latihan bab ini",
                    "memintamu membangun cache LRU sendiri.",
                    "",
                    "Bagian tersulit caching adalah invalidasi, yaitu memastikan cache nggak",
                    "menyajikan data basi. Caranya: TTL yang pendek untuk data yang sering",
                    "berubah, hapus kunci saat data ditulis, dan nama berkas berversi untuk",
                    "aset statis (app.3f9a.js), sehingga berkas baru otomatis punya alamat",
                    "baru.",
                    "",
                    "Jebakan: cache stampede. Kunci populer kedaluwarsa, lalu ratusan request",
                    "yang datang bersamaan kena miss dan menyerbu database di detik yang",
                    "sama. Penangkalnya: cuma satu request yang boleh mengisi ulang sementara",
                    "yang lain menunggu, atau TTL yang diberi sedikit acakan supaya nggak",
                    "habis serentak.",
                ],
            },
            {
                "heading": "Redis, Valkey, dan Memcached",
                "body": [
                    "Tiga penyimpanan kunci-nilai di memori yang paling sering dipakai",
                    "sebagai cache:",
                    "",
                    "  - Redis: versi 8.10.2 (September 2026), dipakai 28,3% responden Survei",
                    "    Stack Overflow 2026. Sampai versi 7.2 berlisensi BSD. Pada 2024",
                    "    lisensinya diganti jadi RSALv2 dan SSPLv1, lalu sejak Redis 8 ada",
                    "    tambahan pilihan Affero GPL versi 3.",
                    "  - Valkey: fork Redis yang lahir pada 2024 sebagai jawaban atas",
                    "    perubahan lisensi itu. Lisensinya BSD-3-Clause, versinya 9.1.2",
                    "    (Agustus 2026), dan pemakainya naik dari 2,4% (2025) ke 5% (2026).",
                    "    Fedora sudah memakai Valkey sebagai pengganti Redis sejak Fedora 41.",
                    "  - Memcached: versi 1.6.45 (Juli 2026), BSD-3-Clause. Lebih sederhana,",
                    "    cuma kunci dan nilai, dan datanya memang hilang saat restart. Untuk",
                    "    proyek baru, Redis atau Valkey lebih sering dipilih.",
                    "",
                    "Perintah dasarnya sama di Redis dan Valkey: simpan dengan TTL 60 detik,",
                    "ambil, cek sisa TTL, lalu hapus. Detail keduanya dibahas di kurikulum",
                    "Database & Penyimpanan Data.",
                ],
                "bahasa": "redis",
                "code": """SET produk:1 "Buku Tulis 38 lembar, Rp5.000" EX 60
GET produk:1
TTL produk:1
DEL produk:1""",
            },
            {
                "heading": "CDN",
                "body": [
                    "CDN (content delivery network) adalah jaringan server di banyak kota dan",
                    "negara yang menyimpan salinan berkasmu. Pengguna di Makassar mengambil",
                    "gambar dari server terdekat, nggak harus dari server asalmu di Jakarta",
                    "atau Singapura. Hasilnya situs lebih cepat, beban server asal turun, dan",
                    "serangan DDoS lebih mudah diredam.",
                    "",
                    "Penyedia besarnya Cloudflare, Amazon CloudFront, Fastly, Akamai, dan",
                    "Google Cloud CDN. Cloudflare dipakai 25% responden Survei Stack Overflow",
                    "2026.",
                    "",
                    "Apa yang boleh disimpan CDN dan berapa lama diatur lewat header HTTP",
                    "dari servermu. Untuk berkas berversi yang isinya nggak akan berubah:",
                ],
                "bahasa": "http",
                "code": "HTTP/1.1 200 OK\nContent-Type: text/javascript\nCache-Control: public, max-age=31536000, immutable\nETag: \"3f9a1c\"",
            },
            {
                "body": [
                    "public artinya boleh disimpan di cache bersama seperti CDN.",
                    "max-age=31536000 artinya simpan setahun. immutable memberi tahu browser",
                    "bahwa berkas ini nggak perlu dicek ulang. Untuk halaman HTML yang sering",
                    "berubah, pakai no-cache supaya browser selalu menanyakan versi terbaru.",
                    "Untuk data pribadi, pakai private atau no-store.",
                    "",
                    "Jebakan: menyimpan halaman berisi data pribadi di CDN, misalnya halaman",
                    "keranjang atau akun dengan header public. Pengguna berikutnya bisa",
                    "menerima salinan milik orang lain.",
                    "",
                    "MDN juga mencatat dua hal soal CDN publik untuk pustaka JavaScript.",
                    "Browser modern nggak lagi berbagi cache antarsitus, jadi pustaka dari",
                    "CDN publik nggak otomatis sudah tersimpan di browser pengunjung. Berkas",
                    "dari pihak ketiga juga sebaiknya dilindungi Subresource Integrity, yaitu",
                    "sidik jari berkas di tag script, supaya ketahuan kalau isinya diubah",
                    "orang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman produk toko online, artikel portal berita, dan gambar di situs",
                    "sekolah adalah kandidat cache yang bagus: dibaca ribuan kali, berubah",
                    "jarang.",
                    "",
                    "Kasus kecil: halaman produk sebuah toko online butuh 800 ms karena",
                    "query-nya menggabungkan lima tabel. Hampir semua pengunjung cuma",
                    "membaca, dan harga paling sering berubah seminggu sekali.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Ukur dulu untuk memastikan query itu memang penyebab lambatnya.",
                    "  2. Pasang cache-aside di Redis atau Valkey dengan kunci produk:<id>",
                    "     dan TTL lima menit.",
                    "  3. Saat admin mengubah harga, perbarui database dulu, baru hapus",
                    "     kuncinya:",
                    "       UPDATE produk SET harga = 5500 WHERE id = 1;",
                    "       DEL produk:1",
                    "  4. Kirim gambar dan CSS lewat CDN dengan nama berkas berversi.",
                    "  5. Jangan simpan halaman keranjang dan akun di CDN.",
                    "  6. Pantau rasio hit. Kalau rasionya rendah, mungkin TTL terlalu pendek",
                    "     atau kuncinya terlalu spesifik.",
                ],
            },
        ],
    },
    {
        "title": "29. Gaya Komunikasi API: REST, GraphQL, gRPC, Webhook",
        "sections": [
            {
                "body": [
                    "API adalah cara dua program saling bicara. Gaya komunikasinya menentukan",
                    "tiga hal: bentuk permintaannya, format datanya, dan siapa yang memulai",
                    "pembicaraan. Satu sistem biasanya memakai beberapa gaya sekaligus,",
                    "masing-masing di tempat yang cocok.",
                    "",
                    "Materi ini membahas posisi tiap gaya di gambar arsitektur. Cara",
                    "membangun API-nya dengan framework dibahas di kurikulum Backend & API.",
                ],
            },
            {
                "heading": "REST",
                "body": [
                    "REST memperlakukan data sebagai sumber daya yang punya alamat (URL).",
                    "Metode HTTP dipakai untuk mengolahnya: GET untuk membaca, POST untuk",
                    "membuat, PUT atau PATCH untuk mengubah, dan DELETE untuk menghapus.",
                    "Hasilnya ditandai kode status seperti 200, 201, 404, atau 500, dan",
                    "datanya biasanya JSON. Setiap request membawa semua yang dibutuhkan,",
                    "jadi servernya bisa stateless.",
                    "",
                    "Laporan Postman State of the API 2025 mencatat 93% respondennya memakai",
                    "REST. Banyak API yang mengaku REST cuma JSON lewat HTTP, dan itu nggak",
                    "masalah selama konsisten.",
                ],
                "bahasa": "http",
                "code": """GET /produk/17 HTTP/1.1
Host: api.toko.contoh.id
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{"id": 17, "nama": "Buku Tulis", "harga": 5000, "stok": 120}""",
            },
            {
                "heading": "GraphQL",
                "body": [
                    "REST punya dua masalah klasik. Over-fetching: klien menerima lebih",
                    "banyak kolom daripada yang dibutuhkan. Under-fetching: klien harus",
                    "memanggil beberapa alamat untuk menyusun satu halaman, misalnya produk",
                    "lalu ulasannya.",
                    "",
                    "GraphQL menjawabnya dengan satu alamat, biasanya /graphql, tempat klien",
                    "menulis query berbentuk data yang diinginkan. Server punya skema bertipe",
                    "yang menjelaskan semua data yang tersedia. Spesifikasinya dirawat",
                    "GraphQL Foundation; edisi terbarunya terbit September 2025, yang pertama",
                    "sejak 2021. Postman State of the API 2025 mencatat 33% respondennya",
                    "memakai GraphQL. Program berikut membandingkan ukuran jawabannya:",
                ],
                "code": """import json

produk = {"id": 17, "nama": "Buku Tulis", "harga": 5000, "stok": 120,
          "deskripsi": "Buku tulis 38 lembar bergaris, sampul tebal.",
          "berat_gram": 150, "pemasok": "CV Kertas Jaya"}


def rest_get_produk():
    return produk                        # semua kolom ikut terkirim


def graphql_produk(kolom_diminta):
    return {k: produk[k] for k in kolom_diminta}


rest = json.dumps(rest_get_produk())
gql = json.dumps(graphql_produk(["nama", "harga"]))
print("REST   :", len(rest), "byte")
print("GraphQL:", len(gql), "byte ->", gql)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  REST   : 169 byte",
                    "  GraphQL: 37 byte -> {\"nama\": \"Buku Tulis\", \"harga\": 5000}",
                    "",
                    "Aplikasi mobile dengan kuota terbatas merasakan bedanya. Query",
                    "sungguhannya ditulis seperti ini, dan sekaligus mengambil dua ulasan",
                    "terbaru dalam satu panggilan:",
                    "",
                    "  query {",
                    "    produk(id: 17) {",
                    "      nama",
                    "      harga",
                    "      ulasan(terbaru: 2) {",
                    "        bintang",
                    "        komentar",
                    "      }",
                    "    }",
                    "  }",
                    "",
                    "Harganya: caching HTTP lebih sulit karena semua query lewat satu alamat,",
                    "query yang terlalu dalam harus dibatasi, dan ada jebakan N+1, yaitu satu",
                    "query yang ternyata memicu ratusan query database. Pustaka seperti",
                    "DataLoader dipakai untuk mengatasinya.",
                ],
            },
            {
                "heading": "gRPC dan Protocol Buffers",
                "body": [
                    "RPC (remote procedure call) artinya memanggil fungsi di mesin lain",
                    "seolah-olah fungsi lokal. gRPC adalah kerangka RPC yang berasal dari",
                    "Google dan sekarang proyek CNCF; versi intinya 1.84.0 per September",
                    "2026. gRPC berjalan di atas HTTP/2 dan memakai Protocol Buffers, format",
                    "biner yang lebih ringkas dan lebih cepat diurai daripada JSON.",
                    "Kontraknya ditulis di berkas .proto, lalu kode klien dan server dibuat",
                    "otomatis untuk banyak bahasa.",
                    "",
                    "gRPC mendukung streaming dua arah dan paling sering dipakai antarlayanan",
                    "internal. Browser nggak bisa memanggil gRPC langsung; butuh gRPC-Web",
                    "atau Connect sebagai jembatan. Berkas baru sekarang juga boleh memakai",
                    "editions, misalnya edition = \"2023\", sebagai pengganti baris syntax.",
                ],
                "bahasa": "protobuf",
                "code": """syntax = "proto3";

package toko;

service Katalog {
  rpc AmbilProduk (PermintaanProduk) returns (Produk);
}

message PermintaanProduk {
  int32 id = 1;
}

message Produk {
  int32 id = 1;
  string nama = 2;
  int64 harga = 3;
}""",
            },
            {
                "heading": "WebSocket dan SSE",
                "body": [
                    "Tiga gaya tadi dimulai oleh klien. Kadang server yang perlu mengirim",
                    "duluan, misalnya pesan chat baru atau posisi driver ojek.",
                    "",
                    "WebSocket (RFC 6455, Desember 2011) membuka sambungan dua arah yang",
                    "tetap terbuka. Klien dan server bisa saling kirim kapan saja. Cocok",
                    "untuk chat, game multipemain, dan dokumen yang disunting bersama.",
                    "Postman State of the API 2025 mencatat 35% respondennya memakai",
                    "WebSocket.",
                    "",
                    "SSE (Server-Sent Events) lebih sederhana: server mengirim aliran pesan",
                    "satu arah ke klien lewat HTTP biasa, dan browser otomatis menyambung",
                    "ulang kalau putus. Cocok untuk notifikasi, skor langsung, atau jawaban",
                    "chatbot AI yang muncul kata demi kata.",
                    "",
                    "Jebakan: sambungan yang terus terbuka menyulitkan skala horizontal.",
                    "Pengguna A tersambung ke server 1, pengguna B ke server 2, padahal pesan",
                    "A harus sampai ke B. Biasanya dipasang pub/sub seperti Redis di",
                    "belakangnya untuk meneruskan pesan antarserver.",
                ],
            },
            {
                "heading": "Webhook",
                "body": [
                    "Webhook adalah kebalikan dari memanggil API. Kamu memberi layanan lain",
                    "sebuah alamat milikmu, lalu layanan itu mengirim POST ke alamat tersebut",
                    "setiap kali ada kejadian. Payment gateway mengabari tokomu saat",
                    "pembayaran lunas, GitHub mengabari server CI saat ada push.",
                    "",
                    "Karena alamatnya terbuka ke internet, penerima webhook wajib memeriksa",
                    "tanda tangan. Gateway menghitung HMAC, yaitu sidik jari dari isi pesan",
                    "dan kunci rahasia bersama, lalu mengirimnya di header. Penerima",
                    "menghitung ulang dan membandingkannya. Webhook juga bisa terkirim lebih",
                    "dari sekali, jadi penerima harus mengenali kiriman ulang:",
                ],
                "code": """import hashlib
import hmac
import json

RAHASIA = b"kunci-rahasia-dari-dasbor-gateway"
sudah_diproses = set()


def tanda_tangan(badan):
    return hmac.new(RAHASIA, badan, hashlib.sha256).hexdigest()


def terima_webhook(badan, tanda):
    if not hmac.compare_digest(tanda_tangan(badan), tanda):
        return 401, "tanda tangan salah"
    event = json.loads(badan)
    if event["id"] in sudah_diproses:          # kiriman ulang dari gateway
        return 200, "sudah diproses, dilewati"
    sudah_diproses.add(event["id"])
    return 200, f"pesanan {event['pesanan']} ditandai lunas"


badan = json.dumps({"id": "evt_01", "pesanan": "A17", "status": "lunas"})
badan = badan.encode()
asli = tanda_tangan(badan)
print(terima_webhook(badan, asli))
print(terima_webhook(badan, asli))
print(terima_webhook(badan, "palsu"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  (200, 'pesanan A17 ditandai lunas')",
                    "  (200, 'sudah diproses, dilewati')",
                    "  (401, 'tanda tangan salah')",
                    "",
                    "hmac.compare_digest membandingkan dengan waktu yang sama panjang untuk",
                    "semua masukan, supaya penyerang nggak bisa menebak tanda tangan dari",
                    "lamanya perbandingan. Nama header dan bagian yang ditandatangani berbeda",
                    "di tiap gateway, jadi ikuti dokumentasi gateway-mu. Balas cepat dengan",
                    "status 2xx lalu kerjakan sisanya di belakang, karena pengirim biasanya",
                    "mencoba ulang kalau balasanmu lama.",
                ],
            },
            {
                "heading": "API-first dan OpenAPI",
                "body": [
                    "API-first artinya kontrak API disepakati lebih dulu, baru server dan",
                    "kliennya dibangun. Tim frontend dan backend bisa bekerja bersamaan",
                    "karena sama-sama berpegang pada kontrak yang sama.",
                    "",
                    "Untuk REST, kontrak itu biasanya ditulis dengan OpenAPI Specification,",
                    "yang dulu bernama Swagger. Versi terbarunya 3.2.1 (10 September 2026),",
                    "berlisensi Apache-2.0. Versi 3.2.0 (September 2025) menambah tag",
                    "bersarang, metode HTTP tambahan, dan dukungan streaming seperti SSE.",
                    "Dari dokumen OpenAPI, alat seperti Swagger UI membuat halaman",
                    "dokumentasi, dan generator membuat kode klien. FastAPI, NestJS, ASP.NET",
                    "Core, dan springdoc untuk Spring bisa membuat dokumennya otomatis dari",
                    "kode. Untuk menguji API, Postman/Newman dipakai 33% responden Survei",
                    "Stack Overflow 2026. API berbasis event punya padanannya sendiri,",
                    "AsyncAPI.",
                    "",
                    "Contoh dokumen OpenAPI 3.2 untuk alamat GET /produk/{id}:",
                ],
                "bahasa": "yaml",
                "code": """openapi: 3.2.0
info:
  title: API Toko
  version: 1.0.0
paths:
  /produk/{id}:
    get:
      summary: Ambil satu produk
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        "200":
          description: Produk ditemukan
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Produk"
        "404":
          description: Produk nggak ada
components:
  schemas:
    Produk:
      type: object
      required: [id, nama, harga]
      properties:
        id: {type: integer}
        nama: {type: string}
        harga: {type: integer}""",
            },
            {
                "heading": "Memilih gaya",
                "body": [
                    "  Gaya       Yang memulai  Format            Cocok untuk",
                    "  ---------  ------------  ----------------  -----------------------",
                    "  REST       klien         JSON              API publik, CRUD",
                    "  GraphQL    klien         JSON sesuai minta tampilan yang beragam",
                    "  gRPC       klien         Protocol Buffers  antarlayanan internal",
                    "  WebSocket  dua arah      bebas             chat, game",
                    "  SSE        server        teks              notifikasi, streaming",
                    "  Webhook    penyedia      JSON              integrasi antarlayanan",
                    "",
                    "Memakai beberapa gaya dalam satu sistem itu normal. Yang perlu dihindari",
                    "adalah memilih gaya karena sedang ramai dibicarakan. Mulai dari REST",
                    "yang paling dikenal semua alat, lalu tambahkan gaya lain saat ada",
                    "masalah nyata yang dipecahkannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online menerima notifikasi pembayaran lewat webhook. Aplikasi ojek",
                    "mengirim posisi driver secara real-time. Layanan internal di perusahaan",
                    "besar saling memanggil lewat gRPC. API publik marketplace dan instansi",
                    "pemerintah umumnya REST dengan dokumen OpenAPI.",
                    "",
                    "Kasus kecil: kamu membangun toko online dengan tiga kebutuhan. Aplikasi",
                    "mobile dan web butuh data produk. Status pembayaran datang dari payment",
                    "gateway. Pembeli ingin melihat status pesanannya berubah tanpa",
                    "me-refresh halaman.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Data produk: REST dengan kontrak OpenAPI yang ditulis lebih dulu,",
                    "     supaya tim mobile dan web bisa bekerja bersamaan.",
                    "  2. Status pembayaran: webhook dari gateway, dengan pemeriksaan HMAC",
                    "     dan pencatatan id event supaya kiriman ulang nggak diproses dua",
                    "     kali.",
                    "  3. Status pesanan: SSE dari server ke halaman pesanan. Datanya cuma",
                    "     mengalir satu arah, jadi WebSocket belum perlu.",
                    "  4. gRPC baru dipertimbangkan kalau suatu hari layanan internal dipecah",
                    "     dan butuh panggilan yang cepat.",
                    "  5. GraphQL baru dipertimbangkan kalau tampilannya beragam sekali dan",
                    "     over-fetching terbukti jadi masalah.",
                ],
            },
        ],
    },
    {
        "title": "30. Memilih Database dan Replikasi",
        "sections": [
            {
                "body": [
                    "Di bab sebelumnya kamu sudah memperbanyak server aplikasi dan",
                    "menaruh cache di depannya. Server aplikasinya stateless, jadi",
                    "gampang digandakan. Database lain cerita. Dia menyimpan keadaan,",
                    "dan keadaan itu nggak bisa digandakan seenaknya.",
                    "",
                    "Begitu aplikasi makin ramai, biasanya muncul dua pertanyaan:",
                    "  - Jenis database apa yang cocok untuk data ini?",
                    "  - Kalau satu server database kewalahan atau mati, terus",
                    "    gimana?",
                    "",
                    "Materi ini menjawab dua-duanya. Bagian pertama soal memilih,",
                    "bagian kedua soal replikasi, yaitu menyimpan salinan data yang",
                    "sama di lebih dari satu server.",
                ],
            },
            {
                "heading": "Mulai dari pola akses",
                "body": [
                    "Pola akses itu cara datamu dipakai: apa yang ditulis, seberapa",
                    "sering, dan pertanyaan apa yang paling sering diajukan ke data",
                    "itu. Merek database baru dipilih sesudah pola aksesnya jelas.",
                    "",
                    "  jenis           cocok untuk                    contoh",
                    "  relasional      uang, stok, pesanan, JOIN      PostgreSQL, MySQL",
                    "  dokumen         objek utuh mirip JSON          MongoDB, Firestore",
                    "  kunci-nilai     sesi, cache, penghitung        Redis, Valkey",
                    "  kolom lebar     tulisan deras per kunci        Cassandra",
                    "  graf            relasi berantai                Neo4j",
                    "  deret waktu     data sensor, metrik            InfluxDB",
                    "  pencarian       teks bebas, relevansi          Elasticsearch",
                    "  vektor          kemiripan arti (embedding)     pgvector",
                    "  gudang data     ringkasan jutaan baris         BigQuery",
                    "",
                    "Untuk aplikasi bisnis biasa, jawaban awal yang aman hampir",
                    "selalu database relasional. Transaksinya menjaga saldo dan stok",
                    "tetap benar, dan SQL bisa menjawab pertanyaan yang belum",
                    "terpikir waktu skemanya dibuat.",
                    "",
                    "Aplikasi yang besar sering memakai beberapa jenis sekaligus.",
                    "Pesanan di PostgreSQL, sesi di Redis, pencarian produk di",
                    "Elasticsearch. Cara ini namanya polyglot persistence. Tiap data",
                    "disimpan di tempat yang paling cocok, dan bayarannya: tim harus",
                    "merawat lebih dari satu sistem dan menjaga datanya tetap",
                    "selaras.",
                    "",
                    "Survei Stack Overflow memperlihatkan arah pilihannya. PostgreSQL",
                    "naik dari 48,7% responden di survei 2024 jadi 57,9% di survei 2026.",
                    "MongoDB turun dari 24,8% jadi 19,0% di periode yang sama.",
                    "Urutan sepuluh besar 2026: PostgreSQL, SQLite (42,1%), MySQL",
                    "(35,1%), Redis (28,3%), SQL Server (27,1%), MariaDB (20,3%),",
                    "MongoDB, Elasticsearch (14,8%), Oracle (9,4%), dan DynamoDB",
                    "(9,3%). Angka ini menunjukkan apa yang banyak dipakai, belum",
                    "tentu apa yang cocok untuk proyekmu. Seluk-beluk tiap produk",
                    "dibahas di kurikulum Database & Penyimpanan Data.",
                ],
            },
            {
                "heading": "Replikasi: satu data, beberapa salinan",
                "body": [
                    "Replikasi artinya setiap perubahan di satu server database",
                    "disalin ke server lain. Server yang menerima tulisan disebut",
                    "primary. Server yang menerima salinan disebut replica, atau",
                    "standby kalau tugasnya menunggu untuk menggantikan primary.",
                    "",
                    "Replica dipakai untuk dua hal:",
                    "  - Membagi beban baca. Kebanyakan aplikasi web jauh lebih",
                    "    sering membaca daripada menulis. Halaman produk dibaca ribuan",
                    "    kali, harganya diubah sekali sehari. Pembacaan bisa dialihkan",
                    "    ke replica, yang dalam peran ini disebut read replica.",
                    "  - Mengambil alih saat primary mati. Proses ini namanya",
                    "    failover, dan dibahas lagi di materi High Availability.",
                    "",
                    "Dokumentasi PostgreSQL membedakan dua jenis standby. Warm",
                    "standby cuma menunggu dan belum bisa dipakai membaca. Hot",
                    "standby sudah bisa melayani query baca sambil menunggu.",
                    "",
                    "Masalahnya ada di kata \"disalin\". Penyalinan butuh waktu. Kalau",
                    "primary nggak menunggu replica selesai menyalin, replica selalu",
                    "tertinggal sedikit. Jarak itu disebut replication lag. Program di",
                    "bawah meniru keadaan itu dengan jam palsu dalam milidetik.",
                ],
            },
            {
                "heading": "Simulasi jeda replikasi",
                "code": """# Satu primary, satu replica, replikasi asinkron.
# Waktu memakai milidetik palsu supaya hasilnya selalu sama.
JEDA = 300          # replica tertinggal 300 ms dari primary

primary = {}
replica = {}
belum_sampai = []   # (waktu_tiba_di_replica, kunci, nilai)


def tulis(t, kunci, nilai):
    primary[kunci] = nilai
    belum_sampai.append((t + JEDA, kunci, nilai))


def baca_replica(t, kunci):
    while belum_sampai and belum_sampai[0][0] <= t:
        _, k, v = belum_sampai.pop(0)
        replica[k] = v
    return replica.get(kunci, "(belum ada)")


tulis(0, "nama", "Ani")
print("t=100  replica:", baca_replica(100, "nama"))
print("t=500  replica:", baca_replica(500, "nama"))
tulis(1000, "nama", "Ani Lestari")
print("t=1000 primary:", primary["nama"])
print("t=1050 replica:", baca_replica(1050, "nama"))
print("t=1400 replica:", baca_replica(1400, "nama"))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  t=100  replica: (belum ada)",
                    "  t=500  replica: Ani",
                    "  t=1000 primary: Ani Lestari",
                    "  t=1050 replica: Ani",
                    "  t=1400 replica: Ani Lestari",
                    "",
                    "Lihat baris t=1050. Primary sudah berisi \"Ani Lestari\", tapi",
                    "replica masih menjawab \"Ani\". Bayangkan Ani baru saja mengganti",
                    "namanya di halaman profil, lalu halaman itu dimuat ulang dan",
                    "membaca dari replica. Yang muncul nama lama, dan Ani mengira",
                    "tombol simpannya rusak.",
                    "",
                    "Masalah ini punya nama: read-your-writes, artinya orang yang",
                    "menulis harus bisa langsung membaca tulisannya sendiri. Cara",
                    "yang lazim dipakai:",
                    "  - Sesudah seseorang menulis, arahkan bacaan orang itu ke primary",
                    "    selama beberapa detik.",
                    "  - Baca dari primary untuk halaman yang baru saja diubah",
                    "    pemiliknya (profil, keranjang), dan dari replica untuk halaman",
                    "    umum (daftar produk, artikel).",
                    "  - Pakai replikasi sinkron untuk data yang memang nggak boleh",
                    "    tertinggal.",
                ],
            },
            {
                "heading": "Sinkron atau asinkron",
                "body": [
                    "Replikasi sinkron artinya primary baru menjawab \"tersimpan\"",
                    "sesudah minimal satu replica ikut menyimpan. Kalau primary",
                    "mendadak mati, datanya sudah ada di tempat lain. Bayarannya,",
                    "setiap tulisan jadi lebih lambat, dan kalau replica itu macet,",
                    "tulisan ikut tertahan.",
                    "",
                    "Replikasi asinkron artinya primary langsung menjawab, lalu",
                    "menyalin di belakang. Tulisan cepat, tapi kalau primary mati",
                    "sebelum salinan terkirim, perubahan beberapa detik terakhir bisa",
                    "hilang.",
                    "",
                    "  sinkron    data aman, tulisan lebih lambat   saldo, transaksi",
                    "  asinkron   tulisan cepat, bisa ada data basi  daftar produk",
                    "",
                    "Banyak sistem mencampur keduanya: satu replica sinkron di zona",
                    "terdekat supaya nggak ada data hilang, ditambah beberapa replica",
                    "asinkron untuk membagi beban baca.",
                    "",
                    "Jebakan: replica itu salinan hidup. Kalau ada yang menjalankan",
                    "DELETE tanpa WHERE di primary, replica ikut menghapusnya dalam",
                    "hitungan milidetik. Replikasi melindungimu dari server yang",
                    "mati. Dari kesalahan manusia, yang melindungi adalah backup",
                    "yang bisa dipulihkan ke titik waktu tertentu.",
                    "",
                    "Ingat: menambah replica cuma menolong beban baca. Kalau yang",
                    "kewalahan adalah tulisan, semua tulisan tetap masuk ke satu",
                    "primary. Untuk itu kamu butuh sharding, yang dibahas di materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online dan portal berita biasanya punya satu primary dan",
                    "beberapa read replica. Layanan database terkelola seperti Amazon",
                    "RDS, Google Cloud SQL, dan Azure Database for PostgreSQL",
                    "menyediakan read replica lewat beberapa klik. Dokumentasi",
                    "ketiganya sama-sama mengingatkan bahwa replica bisa tertinggal",
                    "dari primary.",
                    "",
                    "Kasus kecil: toko online UMKM baru memasang satu read replica",
                    "supaya halaman produk lebih cepat. Sehari kemudian ada keluhan:",
                    "pembeli yang baru checkout membuka \"Pesanan Saya\" dan",
                    "pesanannya belum muncul. Kalau dimuat ulang beberapa detik",
                    "kemudian, pesanannya ada.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali gejalanya. Data yang baru ditulis muncul terlambat,",
                    "     lalu muncul sendiri. Itu ciri khas replication lag, dan",
                    "     datanya nggak hilang.",
                    "  2. Pisahkan halaman menurut kebutuhannya. Daftar produk boleh",
                    "     sedikit basi. \"Pesanan Saya\" milik orang yang baru menulis,",
                    "     jadi harus membaca dari primary.",
                    "  3. Di kode, sediakan dua koneksi dan pilih per query:",
                    "       db_tulis = koneksi(\"primary\")",
                    "       db_baca = koneksi(\"replica\")",
                    "       pesanan = db_tulis.query(\"SELECT ... WHERE pembeli = ?\")",
                    "  4. Pantau angka lag replica. Kalau lag sering lewat beberapa",
                    "     detik, cari penyebabnya (replica terlalu kecil, jaringan, atau",
                    "     query berat di replica) sebelum menambah replica baru.",
                ],
            },
        ],
    },
    {
        "title": "31. Sharding, Consistent Hashing, dan Teorema CAP",
        "sections": [
            {
                "body": [
                    "Replikasi menyalin seluruh data ke tiap server. Itu menolong",
                    "beban baca, tapi ada dua hal yang nggak bisa ditolongnya. Kalau",
                    "datanya terlalu besar untuk satu mesin, atau tulisannya terlalu",
                    "deras untuk satu primary, kamu harus membagi datanya.",
                    "",
                    "Membagi data ke beberapa server disebut sharding atau partisi.",
                    "Tiap server, yang disebut shard, cuma menyimpan sebagian. Data",
                    "pelanggan A sampai M di satu shard, N sampai Z di shard lain,",
                    "misalnya.",
                    "",
                    "Panduan arsitektur Microsoft Azure menulis terus terang bahwa",
                    "sharding menambah kerumitan yang menetap selamanya. Saran",
                    "mereka: coba dulu server yang lebih besar, read replica, dan",
                    "cache. Sharding baru dipakai kalau ketiganya nggak cukup.",
                ],
            },
            {
                "heading": "Empat cara membagi",
                "body": [
                    "Kolom yang dipakai untuk menentukan sebuah baris masuk shard",
                    "mana disebut shard key. Cara memakainya ada empat:",
                    "  - Lookup. Ada tabel kecil yang mencatat \"sekolah 17 ada di",
                    "    shard 2\". Fleksibel, tapi tabel itu harus selalu dibaca dulu.",
                    "  - Range. Rentang nilai menentukan shard, misalnya tanggal",
                    "    pesanan per bulan. Gampang untuk query rentang, tapi rawan",
                    "    hot shard: semua pesanan baru menumpuk di shard bulan ini.",
                    "  - Hash. Nilai shard key diubah jadi angka acak tapi tetap, lalu",
                    "    angka itu menentukan shard. Datanya rata, tapi query rentang",
                    "    harus bertanya ke semua shard.",
                    "  - Geografis. Data pelanggan Indonesia di server Jakarta, data",
                    "    pelanggan Eropa di server Frankfurt. Kadang ini syarat hukum,",
                    "    karena ada aturan yang mewajibkan data warga disimpan di",
                    "    negaranya.",
                    "",
                    "Shard key yang baik punya banyak nilai berbeda, tersebar rata,",
                    "dan hampir selalu ada di query. Untuk aplikasi sekolah yang",
                    "dipakai banyak sekolah, id_sekolah biasanya pilihan yang masuk",
                    "akal: hampir semua query menyebut sekolahnya, dan data satu",
                    "sekolah tinggal di satu shard.",
                    "",
                    "Jebakan: jangan memakai angka auto-increment sebagai shard key",
                    "dengan cara range. Semua baris baru punya angka terbesar, jadi",
                    "semuanya masuk shard terakhir, dan shard lain menganggur.",
                    "",
                    "Satu lagi yang sering dilupakan: JOIN antar shard itu mahal.",
                    "Kalau data pesanan dan data pelanggan ada di shard berbeda,",
                    "aplikasi harus bertanya ke dua server lalu menggabungkan sendiri.",
                ],
            },
            {
                "heading": "Cara hash paling sederhana: mod N",
                "code": """import hashlib


def nomor_shard(kunci, banyak_shard):
    angka = int(hashlib.md5(kunci.encode()).hexdigest(), 16)
    return angka % banyak_shard


pindah = 0
for i in range(1, 9):
    kunci = f"pelanggan-{i}"
    lama = nomor_shard(kunci, 3)
    baru = nomor_shard(kunci, 4)
    catatan = "  pindah" if lama != baru else ""
    if lama != baru:
        pindah += 1
    print(f"{kunci}: shard {lama} -> shard {baru}{catatan}")
print(f"{pindah} dari 8 kunci harus dipindah")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  pelanggan-1: shard 1 -> shard 2  pindah",
                    "  pelanggan-2: shard 1 -> shard 2  pindah",
                    "  pelanggan-3: shard 2 -> shard 3  pindah",
                    "  pelanggan-4: shard 1 -> shard 1",
                    "  pelanggan-5: shard 0 -> shard 1  pindah",
                    "  pelanggan-6: shard 1 -> shard 1",
                    "  pelanggan-7: shard 1 -> shard 3  pindah",
                    "  pelanggan-8: shard 2 -> shard 0  pindah",
                    "  6 dari 8 kunci harus dipindah",
                    "",
                    "Program ini memakai hashlib.md5 dan sengaja nggak memakai fungsi",
                    "hash() bawaan Python. Hasil hash() untuk teks berubah tiap kali",
                    "Python dijalankan ulang, jadi kunci yang sama bisa mendarat di",
                    "shard berbeda besok pagi. Fungsi shard harus memberi jawaban yang",
                    "sama di semua server dan sepanjang waktu.",
                    "",
                    "Sekarang lihat angka terakhirnya. Waktu shard ketiga ditambah",
                    "jadi empat, enam dari delapan pelanggan pindah tempat. Di",
                    "database sungguhan, \"pindah\" berarti menyalin jutaan baris",
                    "lewat jaringan sambil aplikasi tetap melayani orang. Makin besar",
                    "N, makin banyak yang pindah, karena hampir semua sisa bagi",
                    "berubah begitu pembaginya berubah.",
                ],
            },
            {
                "heading": "Consistent hashing",
                "body": [
                    "Consistent hashing mengatasi masalah itu. Bayangkan sebuah jam",
                    "dinding raksasa berisi angka hash dari nol sampai paling besar,",
                    "melingkar. Tiap server ditaruh di beberapa titik di lingkaran",
                    "itu berdasarkan hash namanya. Tiap kunci juga di-hash, lalu",
                    "berjalan searah jarum jam sampai ketemu server pertama. Server",
                    "itulah pemiliknya.",
                    "",
                    "  0 ........ db-a ........ db-b ........ db-c ........ (kembali ke 0)",
                    "                 ^ user-7 jalan ke kanan, ketemu db-b",
                    "",
                    "Waktu server baru masuk, dia cuma mengambil kunci yang jatuh",
                    "tepat sebelum titiknya. Kunci lain tetap di tempatnya. Kira-kira",
                    "cuma 1/N kunci yang pindah, jauh lebih sedikit daripada cara",
                    "mod N.",
                    "",
                    "Satu server biasanya diberi banyak titik di lingkaran, yang",
                    "disebut node virtual. Tanpa node virtual, jarak antar server di",
                    "lingkaran nggak rata, dan satu server bisa kebagian separuh",
                    "data. Makin banyak node virtual, makin rata pembagiannya.",
                    "",
                    "Ide ini dipakai di banyak sistem terdistribusi. Makalah Dynamo",
                    "dari Amazon (2007) memakainya, begitu juga Apache Cassandra dan",
                    "banyak klien cache yang membagi kunci ke beberapa server",
                    "Memcached. Latihan di akhir bab ini memintamu membangun ring",
                    "kecil dan membandingkannya dengan mod N.",
                ],
            },
            {
                "heading": "Teorema CAP",
                "body": [
                    "Begitu data tersebar di beberapa server, kabel di antaranya bisa",
                    "putus. Kejadian ini disebut partition, yaitu server-server masih",
                    "hidup tapi nggak bisa saling bicara. Teorema CAP bilang: saat",
                    "partition terjadi, sistem harus memilih salah satu.",
                    "  - Consistency (C). Semua pembaca melihat data terbaru. Kalau",
                    "    nggak bisa dipastikan terbaru, sistem menolak menjawab.",
                    "  - Availability (A). Setiap permintaan tetap dijawab, walaupun",
                    "    jawabannya mungkin sudah basi.",
                    "",
                    "Huruf P, partition tolerance, bukan pilihan di sistem yang",
                    "tersebar lewat jaringan. Partition pasti suatu saat terjadi.",
                    "Jadi rumus \"pilih dua dari tiga\" yang sering dikutip itu",
                    "menyesatkan. Pilihan yang nyata baru muncul saat jaringan putus:",
                    "tolak atau jawab dengan data yang mungkin lama.",
                    "",
                    "Contoh pilihannya:",
                    "  - Penjualan tiket konser dengan kursi bernomor memilih C. Lebih",
                    "    baik pembeli melihat \"coba lagi\" daripada satu kursi terjual",
                    "    ke dua orang.",
                    "  - Jumlah like di media sosial memilih A. Angka yang telat",
                    "    beberapa detik nggak merugikan siapa pun.",
                    "",
                    "Dari situ lahir dua istilah. Konsistensi kuat artinya begitu",
                    "tulisan selesai, semua pembaca langsung melihatnya. Konsistensi",
                    "akhir (eventual consistency) artinya semua salinan pasti akan",
                    "sama, tapi nggak seketika. Replica asinkron di materi",
                    "sebelumnya adalah contoh konsistensi akhir.",
                    "",
                    "Ada perluasan CAP bernama PACELC. Isinya: kalau ada partition",
                    "(P), pilih A atau C. Kalau nggak ada (else, E), tetap ada",
                    "pilihan antara latensi rendah (L) atau konsistensi (C). Menunggu",
                    "replica sinkron itu memilih C dan membayar dengan latensi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan SaaS yang dipakai banyak sekolah atau banyak toko",
                    "(multi-tenant) sering membagi data per pelanggan. Vitess untuk",
                    "MySQL dan Citus untuk PostgreSQL adalah dua proyek open source",
                    "yang dipakai untuk men-shard database relasional, dan MongoDB",
                    "punya sharding bawaan dengan shard key yang dipilih pemakainya.",
                    "",
                    "Kasus kecil: aplikasi rapor online dipakai 300 sekolah. Tabel",
                    "nilai sudah 400 juta baris, dan satu server PostgreSQL mulai",
                    "kewalahan menulis di minggu pengisian rapor. Tim ingin membagi",
                    "datanya ke empat shard.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan dulu cara yang lebih murah sudah dicoba: server",
                    "     lebih besar, indeks yang tepat, dan read replica untuk",
                    "     laporan.",
                    "  2. Pilih shard key dari query yang paling sering. Hampir semua",
                    "     query menyebut sekolahnya, jadi id_sekolah cocok. Data satu",
                    "     sekolah tinggal di satu shard, jadi JOIN di dalam satu",
                    "     sekolah tetap jalan.",
                    "  3. Waspadai sekolah raksasa. Kalau satu sekolah punya data",
                    "     sepuluh kali lipat sekolah lain, dia bisa jadi hot shard.",
                    "     Tabel lookup memudahkan memindahkan sekolah itu ke shard",
                    "     sendiri.",
                    "  4. Pakai pembagian yang tahan penambahan shard (lookup atau",
                    "     consistent hashing), supaya shard kelima nanti nggak",
                    "     memaksa hampir semua data pindah.",
                ],
            },
        ],
    },
    {
        "title": "32. Rate Limiting dan Throttling",
        "sections": [
            {
                "body": [
                    "Halaman login yang terbuka ke internet akan dicoba ribuan sandi",
                    "oleh program otomatis. API gratis akan dipanggil sampai habis",
                    "oleh satu pengguna yang lupa memasang jeda di skripnya. Dua-duanya",
                    "bisa membuat server penuh dan pengguna lain ikut kena.",
                    "",
                    "Rate limiting artinya membatasi berapa kali seseorang boleh",
                    "mengirim permintaan dalam selang waktu tertentu, lalu menolak",
                    "sisanya. \"Seseorang\" di sini bisa berarti satu akun, satu",
                    "alamat IP, atau satu kunci API.",
                    "",
                    "Throttling sering dipakai sebagai sinonim. Kalau mau dibedakan,",
                    "throttling lebih ke memperlambat: permintaan yang berlebih",
                    "ditahan dulu di antrean, belum tentu ditolak. Di dokumentasi",
                    "berbagai produk kedua istilah ini sering tertukar, jadi selalu",
                    "cek apa yang dimaksud.",
                ],
            },
            {
                "heading": "Empat algoritma",
                "body": [
                    "Ada empat cara menghitung yang paling sering ditemui:",
                    "  - Token bucket. Tiap klien punya ember berisi token. Satu",
                    "    permintaan mengambil satu token. Ember diisi ulang dengan laju",
                    "    tetap sampai penuh. Kalau embernya kosong, permintaan ditolak.",
                    "    Lonjakan singkat boleh, asal nggak melebihi isi ember.",
                    "  - Leaky bucket. Permintaan masuk antrean, lalu keluar dengan",
                    "    laju tetap seperti air menetes dari ember bocor. Hasilnya rata,",
                    "    tapi permintaan bisa menunggu lama.",
                    "  - Fixed window. Hitung permintaan per jendela waktu, misalnya",
                    "    per menit kalender. Lewat batas, tolak sampai menit berikutnya.",
                    "    Gampang dibuat, tapi ada celah di batas jendela.",
                    "  - Sliding window. Jendelanya ikut bergeser bersama waktu: yang",
                    "    dihitung selalu enam puluh detik terakhir. Versi log mencatat",
                    "    waktu tiap permintaan. Versi counter memperkirakan dari dua",
                    "    jendela yang berdampingan supaya hemat memori.",
                    "",
                    "Celah fixed window paling gampang dilihat lewat program.",
                    "Aturannya sama di atas kertas, rata-rata lima permintaan per",
                    "enam puluh detik. Klien mengirim lima permintaan di detik ke-59",
                    "dan lima lagi di detik ke-60.",
                ],
            },
            {
                "heading": "Fixed window dan token bucket berdampingan",
                "code": """from fractions import Fraction

# Sepuluh request dari satu klien: lima di detik 59, lima di detik 60.
waktu = [59, 59, 59, 59, 59, 60, 60, 60, 60, 60]


def fixed_window(batas, lebar):
    hitung, hasil = {}, []
    for t in waktu:
        jendela = t // lebar
        hitung[jendela] = hitung.get(jendela, 0) + 1
        hasil.append(hitung[jendela] <= batas)
    return hasil


def token_bucket(kapasitas, laju):
    token, terakhir, hasil = Fraction(kapasitas), 0, []
    for t in waktu:
        token = min(kapasitas, token + (t - terakhir) * laju)
        terakhir = t
        if token >= 1:
            token -= 1
            hasil.append(True)
        else:
            hasil.append(False)
    return hasil


# Aturan yang sama di atas kertas: rata-rata 5 request per 60 detik.
for nama, hasil in [("fixed window", fixed_window(5, 60)),
                    ("token bucket", token_bucket(5, Fraction(5, 60)))]:
    tanda = "".join("v" if ok else "x" for ok in hasil)
    print(f"{nama:<13} {tanda}  diizinkan {sum(hasil)} dari {len(hasil)}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  fixed window  vvvvvvvvvv  diizinkan 10 dari 10",
                    "  token bucket  vvvvvxxxxx  diizinkan 5 dari 10",
                    "",
                    "Huruf v artinya diizinkan, x artinya ditolak. Fixed window",
                    "mengizinkan sepuluh permintaan dalam dua detik. Detik ke-59",
                    "masuk jendela pertama, detik ke-60 masuk jendela kedua, dan",
                    "masing-masing jendela masih punya jatah lima. Batasnya dua kali",
                    "lipat dari yang dimaksud, tepat di pergantian menit.",
                    "",
                    "Token bucket menolak lima yang terakhir. Embernya sudah habis di",
                    "detik ke-59, dan dalam satu detik cuma terisi 5/60 token. Program",
                    "memakai Fraction supaya hitungan pecahan itu persis, tanpa",
                    "selisih kecil khas bilangan float.",
                    "",
                    "Token bucket dipakai di banyak tempat karena gampang dijelaskan",
                    "ke pemakai API: \"boleh lonjakan sampai 5, rata-ratanya satu tiap",
                    "12 detik\". Yang perlu disimpan per klien cuma dua angka, yaitu",
                    "isi ember dan waktu terakhir diisi.",
                ],
            },
            {
                "heading": "Menolak dengan sopan: 429 dan Retry-After",
                "body": [
                    "Permintaan yang kena batas dijawab dengan status HTTP 429 Too",
                    "Many Requests. Sertakan header Retry-After yang memberi tahu",
                    "berapa detik lagi klien boleh mencoba. Klien yang baik membaca",
                    "header itu dan menunggu, nggak langsung mengulang.",
                ],
            },
            {
                "heading": "Contoh respons",
                "bahasa": "http",
                "code": """HTTP/1.1 429 Too Many Requests
Content-Type: application/json
Retry-After: 12

{"error": "Terlalu banyak percobaan. Coba lagi 12 detik lagi."}""",
            },
            {
                "body": [
                    "Banyak API juga mengirim header seperti X-RateLimit-Remaining",
                    "berisi sisa jatah. Header berawalan X- itu kebiasaan, belum",
                    "standar resmi, jadi namanya bisa beda di tiap layanan.",
                    "",
                    "Di Laravel, pembatas dideklarasikan dengan RateLimiter lalu",
                    "dipasang ke rute lewat middleware throttle. Starter kit Laravel",
                    "membatasi percobaan login lima kali per menit untuk tiap",
                    "pasangan email dan alamat IP. Versi ringkasnya begini:",
                ],
            },
            {
                "heading": "Pembatas login di Laravel (ringkas)",
                "bahasa": "php",
                "code": "use Illuminate\\Cache\\RateLimiting\\Limit;\nuse Illuminate\\Http\\Request;\nuse Illuminate\\Support\\Facades\\RateLimiter;\nuse Illuminate\\Support\\Str;\n\nRateLimiter::for('login', function (Request $request) {\n    $kunci = Str::lower($request->input('email')).'|'.$request->ip();\n    return Limit::perMinute(5)->by($kunci);\n});\n\n// di routes/web.php\nRoute::post('/login', [LoginController::class, 'store'])\n    ->middleware('throttle:login');",
            },
            {
                "body": [
                    "Kenapa kuncinya email ditambah IP? Kalau cuma IP, satu kantor",
                    "yang berbagi satu IP publik bisa saling mengunci. Kalau cuma",
                    "email, penyerang bisa mengunci akun orang lain dengan sengaja",
                    "salah sandi berkali-kali dari banyak tempat.",
                    "",
                    "Letak pembatas juga perlu dipikirkan. Pembatas bisa dipasang di",
                    "API gateway, di reverse proxy (Nginx punya modul limit_req), atau",
                    "di dalam aplikasi. Kalau aplikasimu berjalan di beberapa server,",
                    "hitungannya harus disimpan di tempat bersama seperti Redis.",
                    "Kalau tiap server menghitung sendiri, batas lima per menit",
                    "ternyata jadi lima per menit per server.",
                    "",
                    "Jebakan: retry yang nggak dikoordinasikan dengan rate limiting",
                    "bisa memperparah keadaan. Klien yang ditolak lalu langsung",
                    "mengulang, ditolak lagi, mengulang lagi, ikut menghabiskan",
                    "kapasitas server. Panduan Azure menyebut ini badai retry. Cara",
                    "mencegahnya dibahas di materi Retry, Idempotensi, dan Circuit",
                    "Breaker di bab berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua API publik membatasi pemakainya. GitHub, Stripe,",
                    "dan penyedia API AI menulis batasnya di dokumentasi dan menjawab",
                    "dengan 429 kalau batas terlewati. Halaman login bank dan",
                    "marketplace membatasi percobaan sandi per akun.",
                    "",
                    "Kasus kecil: API cek ongkir milik sebuah toko dipakai mitra",
                    "lewat kunci API. Satu mitra menjalankan skrip tanpa jeda dan",
                    "mengirim 3.000 permintaan per menit. Mitra lain jadi lambat.",
                    "Pemilik ingin tiap kunci boleh lonjakan 20 permintaan, dengan",
                    "rata-rata 2 per detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Terjemahkan keinginan itu ke token bucket: kapasitas 20",
                    "     token, laju isi ulang 2 token per detik, satu ember per",
                    "     kunci API.",
                    "  2. Simpan isi ember dan waktu terakhir di Redis supaya semua",
                    "     server aplikasi berbagi hitungan yang sama.",
                    "  3. Kalau ember kosong, jawab 429 dengan Retry-After. Waktu",
                    "     tunggunya dihitung dari kekurangan token dibagi laju:",
                    "       kurang = 1 - isi_ember",
                    "       retry_after = ceil(kurang / 2)",
                    "  4. Kabari mitra lewat dokumentasi, lalu pantau berapa 429 yang",
                    "     dikirim per kunci. Kunci yang terus kena batas mungkin butuh",
                    "     paket yang lebih besar, atau skripnya yang perlu dibetulkan.",
                ],
            },
        ],
    },
    {
        "title": "33. High Availability dan Pemulihan Bencana",
        "sections": [
            {
                "body": [
                    "Semua komponen pada akhirnya rusak. Disk aus, server kehabisan",
                    "memori, kabel listrik di pusat data dicabut orang, satu zona",
                    "cloud padam, atau seorang admin salah mengetik perintah. Yang bisa",
                    "kamu atur cuma apa yang terjadi sesudahnya.",
                    "",
                    "Ada dua istilah yang mirip tapi menjawab pertanyaan berbeda:",
                    "  - High availability (HA): bagaimana sistem tetap melayani",
                    "    walaupun ada komponen yang mati. Fokusnya menit dan detik.",
                    "  - Pemulihan bencana (disaster recovery, DR): bagaimana sistem",
                    "    bangkit lagi sesudah kejadian besar, misalnya satu region",
                    "    cloud lumpuh atau data terhapus. Fokusnya jam dan data yang",
                    "    hilang.",
                ],
            },
            {
                "heading": "Redundansi dan titik gagal tunggal",
                "body": [
                    "Titik gagal tunggal (single point of failure, SPOF) adalah",
                    "komponen yang kalau mati, seluruh sistem ikut mati. Satu server",
                    "database tanpa standby adalah SPOF. Satu load balancer juga.",
                    "",
                    "Obatnya redundansi: sediakan lebih dari satu, lalu siapkan cara",
                    "berpindah. Perpindahan itu disebut failover. Ada dua gaya:",
                    "  - Aktif-pasif. Satu server melayani, satu lagi menunggu. Kalau",
                    "    yang aktif mati, yang pasif naik. Sederhana, tapi server",
                    "    cadangan menganggur selama menunggu.",
                    "  - Aktif-aktif. Semua server melayani bersamaan. Kalau satu mati,",
                    "    sisanya menanggung bebannya. Lebih hemat, tapi untuk database",
                    "    jauh lebih rumit karena dua server bisa menerima tulisan yang",
                    "    saling bertabrakan.",
                    "",
                    "Supaya failover bisa terjadi, harus ada yang rajin mengecek.",
                    "Health check adalah permintaan kecil berkala, misalnya GET",
                    "/health tiap lima detik. Kalau gagal beberapa kali berturut-turut,",
                    "komponen itu dianggap mati. Jarak antara rusak dan ketahuan ini",
                    "ikut menentukan berapa lama pengguna melihat error.",
                    "",
                    "Di cloud, redundansi diatur per lokasi. Satu region (misalnya",
                    "Jakarta) berisi beberapa availability zone, yaitu pusat data",
                    "terpisah dengan listrik dan jaringan sendiri. Server di dua zona",
                    "tahan terhadap satu pusat data padam. Server di dua region tahan",
                    "terhadap satu kota terkena bencana, dengan biaya dan kerumitan",
                    "yang jauh lebih besar.",
                    "",
                    "Program berikut menghitung apa yang terjadi pada ketersediaan",
                    "kalau komponen disusun berderet atau berdampingan.",
                ],
            },
            {
                "heading": "Ketersediaan seri dan paralel",
                "code": """from fractions import Fraction

SETAHUN = 365 * 24 * 60          # menit dalam setahun


def tampil(nama, a):
    henti = (1 - a) * SETAHUN
    print(f"{nama:<28} {float(a * 100):8.4f}%  {float(henti):7.1f} menit/tahun")


server = Fraction(999, 1000)     # satu server aplikasi: 99,9%
database = Fraction(999, 1000)   # satu server database: 99,9%
dua_server = 1 - (1 - server) ** 2

tampil("1 server", server)
tampil("1 server + database", server * database)
tampil("2 server paralel", dua_server)
tampil("2 server paralel + database", dua_server * database)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  1 server                      99.9000%    525.6 menit/tahun",
                    "  1 server + database           99.8001%   1050.7 menit/tahun",
                    "  2 server paralel              99.9999%      0.5 menit/tahun",
                    "  2 server paralel + database   99.8999%    526.1 menit/tahun",
                    "",
                    "Komponen yang berderet (seri) harus hidup semua supaya sistem",
                    "jalan, jadi ketersediaannya dikalikan. Dua komponen 99,9% yang",
                    "berderet menghasilkan 99,8001%, dan waktu hentinya hampir dua",
                    "kali lipat. Makin panjang rantainya, makin turun angkanya.",
                    "",
                    "Komponen yang berdampingan (paralel) cukup hidup salah satunya.",
                    "Peluang dua-duanya mati bersamaan jauh lebih kecil, jadi angkanya",
                    "naik ke 99,9999%.",
                    "",
                    "Baris terakhir yang paling penting. Dua server aplikasi paralel",
                    "nggak banyak menolong kalau database di belakangnya cuma satu.",
                    "Ketersediaan sistem ditentukan mata rantai terlemahnya, dan di",
                    "sini mata rantai itu database tunggal.",
                    "",
                    "Ingat: hitungan paralel ini menganggap tiap server mati tanpa",
                    "terpengaruh yang lain, dan failover terjadi seketika. Kalau dua",
                    "server itu berbagi satu sumber listrik atau satu konfigurasi",
                    "yang salah, mereka mati bersamaan dan angka 99,9999% itu cuma",
                    "di atas kertas.",
                ],
            },
            {
                "heading": "RPO dan RTO",
                "body": [
                    "Dua angka ini menjawab \"seberapa parah boleh rusaknya\" dan",
                    "harus disepakati dengan pemilik bisnis, bukan ditebak tim teknis.",
                    "  - RPO (recovery point objective): berapa banyak data, diukur",
                    "    dalam waktu, yang boleh hilang. RPO 15 menit artinya data 15",
                    "    menit terakhir sebelum bencana boleh hilang.",
                    "  - RTO (recovery time objective): berapa lama sistem boleh mati",
                    "    sampai pulih. RTO 2 jam artinya sistem harus melayani lagi",
                    "    paling lambat dua jam sesudah kejadian.",
                    "",
                    "Backup harian memberi RPO paling buruk 24 jam. Replikasi",
                    "asinkron ke region lain bisa menurunkannya ke hitungan detik.",
                    "Makin kecil kedua angka itu, makin mahal biayanya.",
                    "",
                    "Panduan pemulihan bencana AWS mengelompokkan strateginya jadi",
                    "empat, dari yang paling murah sampai paling mahal:",
                    "",
                    "  strategi              cara kerja                      RPO/RTO",
                    "  backup and restore    pulihkan dari backup            jam",
                    "  pilot light           data direplikasi, server mati   puluhan menit",
                    "  warm standby          salinan kecil selalu menyala    menit",
                    "  multi-site aktif      dua lokasi melayani bersamaan   hampir nol",
                    "",
                    "Sekolah yang memakai sistem nilai online mungkin cukup dengan",
                    "backup and restore. Sistem pembayaran yang dipakai jutaan orang",
                    "biasanya butuh warm standby atau lebih.",
                ],
            },
            {
                "heading": "Backup yang belum pernah dipulihkan",
                "body": [
                    "Backup yang nggak pernah dicoba dipulihkan belum terbukti",
                    "berguna. Berkasnya bisa rusak, kunci enkripsinya hilang, atau",
                    "ternyata proses pemulihannya butuh dua hari, jauh di atas RTO.",
                    "Jadwalkan latihan pemulihan secara berkala dan catat berapa lama",
                    "waktunya.",
                    "",
                    "Aturan yang sering dipakai adalah 3-2-1: tiga salinan data, di",
                    "dua jenis media berbeda, satu di antaranya di lokasi lain. Ingat",
                    "juga bahwa replica database bukan backup. Kesalahan di primary",
                    "ikut tersalin ke replica dalam hitungan detik.",
                    "",
                    "Kalau mau bacaan yang tertata, AWS Well-Architected Framework",
                    "punya enam pilar: keunggulan operasional, keamanan, keandalan,",
                    "efisiensi kinerja, optimasi biaya, dan keberlanjutan. Dokumen",
                    "pilar keandalan (Reliability Pillar) bisa dibaca gratis dan",
                    "membahas redundansi, failover, dan pemulihan bencana. Cara",
                    "menjalankannya di AWS, Azure, dan Google Cloud dibahas di",
                    "kurikulum DevOps & Cloud.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan database terkelola di cloud umumnya menawarkan opsi",
                    "multi-AZ: satu standby di zona lain yang naik otomatis kalau",
                    "primary mati. Aplikasi bank dan dompet digital biasanya menaruh",
                    "salinan data di dua region, sementara toko kecil cukup dengan",
                    "backup harian yang disalin ke lokasi lain.",
                    "",
                    "Kasus kecil: koperasi simpan pinjam punya aplikasi web dengan",
                    "satu server aplikasi dan satu server database di satu pusat data.",
                    "Pengurus bilang aplikasi boleh mati paling lama satu jam, dan",
                    "transaksi yang sudah dicatat paling banyak boleh hilang lima",
                    "menit.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Terjemahkan ke angka: RTO 1 jam, RPO 5 menit.",
                    "  2. Cari SPOF-nya. Server aplikasi dan server database",
                    "     sama-sama tunggal, dan keduanya ada di satu lokasi.",
                    "  3. Backup harian nggak memenuhi RPO 5 menit. Pasang replikasi",
                    "     ke standby di lokasi lain, ditambah backup harian untuk",
                    "     melindungi dari kesalahan manusia.",
                    "  4. Siapkan server aplikasi kedua yang bisa dinyalakan cepat,",
                    "     lalu tulis langkah failover sebagai daftar periksa:",
                    "       1) pastikan primary memang mati",
                    "       2) naikkan standby jadi primary",
                    "       3) arahkan aplikasi ke primary baru",
                    "  5. Latih langkah itu sekali sebulan dan catat waktunya. Kalau",
                    "     lebih dari satu jam, sederhanakan langkahnya atau",
                    "     otomatiskan.",
                ],
            },
        ],
    },
    {
        "title": "34. Microservices: Kapan Memecah dan Berapa Harganya",
        "sections": [
            {
                "body": [
                    "Microservices adalah gaya arsitektur yang memecah satu aplikasi",
                    "jadi banyak layanan kecil. Tiap layanan mengurus satu kemampuan",
                    "bisnis, misalnya data produk, pembayaran, atau pengiriman. Tiap",
                    "layanan punya database sendiri, dan bisa di-deploy sendiri tanpa",
                    "menunggu layanan lain.",
                    "",
                    "Lawannya adalah monolit, yang sudah kamu kenal di bab Pola",
                    "Arsitektur Aplikasi: satu aplikasi, satu proses deploy, biasanya",
                    "satu database. Di sana juga dibahas saran \"monolith first\":",
                    "mulai dari monolit yang tertata, lalu pecah kalau memang perlu.",
                    "Materi ini membahas kapan \"memang perlu\" itu datang, dan berapa",
                    "harga yang harus dibayar sesudahnya.",
                    "",
                    "Gampangnya begini. Monolit itu satu dapur besar tempat semua koki",
                    "masak bareng. Microservices itu deretan warung kecil di food",
                    "court. Tiap warung bisa buka, tutup, dan ganti menu sendiri. Tapi",
                    "pesanan yang butuh nasi dari warung A dan sate dari warung B",
                    "harus diantar bolak-balik, dan kalau satu warung tutup, pesanan",
                    "gabungan itu ikut tertahan.",
                ],
            },
            {
                "heading": "Yang kamu dapat dan yang kamu bayar",
                "body": [
                    "  yang didapat                      yang dibayar",
                    "  deploy satu layanan tanpa yang    panggilan antarlayanan lewat",
                    "    lain                              jaringan bisa lambat dan gagal",
                    "  skala per bagian (cuma pencarian  data tersebar, transaksi lintas",
                    "    yang diperbanyak)                 layanan butuh pola khusus",
                    "  tim kecil memiliki layanannya     butuh log, metrik, dan trace",
                    "    sendiri                           yang menyatukan semua layanan",
                    "  boleh beda bahasa per layanan     infrastruktur deploy lebih",
                    "                                      rumit (kontainer, Kubernetes)",
                    "",
                    "Keuntungan terbesarnya ada di sisi organisasi. Kalau ada dua",
                    "puluh tim yang mengerjakan satu monolit, mereka saling menunggu:",
                    "satu perubahan kecil harus ikut jadwal rilis besar. Dengan",
                    "microservices, tim pembayaran bisa merilis tiga kali sehari tanpa",
                    "bertanya ke tim produk.",
                    "",
                    "Untuk tim lima orang, keuntungan itu hampir nggak terasa,",
                    "sedangkan bayarannya tetap penuh. Panduan arsitektur Azure",
                    "menyebut microservices cocok untuk domain yang rumit dan sering",
                    "berubah, dengan syarat praktik DevOps tim sudah matang.",
                    "",
                    "Soal angka pemakaian, data yang bisa dipegang memang terbatas.",
                    "Survei JetBrains 2022 mencatat 37% responden mengembangkan",
                    "microservices; laporan sesudahnya nggak menanyakan hal ini lagi.",
                    "Survei tahunan CNCF 2025 mencatat 82% pengguna kontainer sudah",
                    "menjalankan Kubernetes di produksi, dan Kubernetes adalah tempat",
                    "yang paling sering dipakai untuk menjalankan microservices.",
                ],
            },
            {
                "heading": "Monolit terdistribusi",
                "body": [
                    "Kesalahan yang paling sering terjadi saat memecah terlalu dini",
                    "punya nama: monolit terdistribusi. Layanannya memang banyak,",
                    "tapi semuanya masih saling bergantung erat. Ciri-cirinya:",
                    "  - Dua layanan atau lebih harus di-deploy bersamaan, karena",
                    "    kalau cuma satu yang berubah, yang lain rusak.",
                    "  - Beberapa layanan membaca dan menulis tabel yang sama di satu",
                    "    database bersama.",
                    "  - Satu klik pengguna memicu rantai panggilan sinkron A ke B ke C",
                    "    ke D. Kalau D lambat, semuanya lambat.",
                    "  - Menambah satu kolom di halaman produk butuh perubahan di lima",
                    "    layanan.",
                    "",
                    "Hasilnya lebih buruk dari dua pilihan lainnya: kerumitan",
                    "jaringan ala microservices, ditambah keterikatan ala monolit.",
                    "Banyak tim kemudian menggabungkan lagi layanan yang terlalu kecil.",
                    "",
                    "Batas layanan yang sehat biasanya mengikuti bounded context dari",
                    "Domain-Driven Design (bab Pola Arsitektur Aplikasi). Kalau dua",
                    "bagian selalu berubah bersamaan, kemungkinan besar keduanya satu",
                    "konteks dan sebaiknya tetap satu layanan.",
                ],
            },
            {
                "heading": "Dari SOA ke microservices",
                "body": [
                    "Sebelum microservices populer, sejak awal 2000-an korporat sudah",
                    "memakai service-oriented architecture (SOA). Sistemnya juga",
                    "disusun dari layanan, tapi layanannya besar, dipakai bersama",
                    "banyak aplikasi, dan biasanya bicara lewat protokol SOAP dengan",
                    "kontrak berformat WSDL.",
                    "",
                    "Di tengahnya sering ada enterprise service bus (ESB), yaitu",
                    "perantara pusat yang mengubah format pesan, mengarahkan, dan",
                    "menjalankan aturan bisnis. Microservices sengaja membalik pola",
                    "itu. Artikel Martin Fowler dan James Lewis menyebutnya smart",
                    "endpoints and dumb pipes: logika tinggal di layanan, jalurnya",
                    "cukup meneruskan pesan.",
                    "",
                    "Gaya ini statusnya menurun dan jarang dipilih untuk sistem baru.",
                    "Tapi kalau kamu magang di bank, perusahaan telekomunikasi, atau",
                    "perusahaan milik negara, kemungkinan besar kamu ketemu sistem",
                    "lama seperti itu yang masih jalan, dan istilahnya masih muncul",
                    "di lowongan kerja.",
                ],
            },
            {
                "heading": "Strangler fig: memecah sedikit demi sedikit",
                "body": [
                    "Menulis ulang monolit dari nol sekaligus adalah proyek yang",
                    "sering gagal. Sistem lama terus berubah selama sistem baru",
                    "dibangun, dan hari peralihan besarnya penuh risiko.",
                    "",
                    "Pola strangler fig menawarkan jalan bertahap. Namanya diambil",
                    "dari pohon ara pencekik yang tumbuh melilit pohon inang, lalu",
                    "pelan-pelan menggantikannya. Fowler memperbarui artikelnya soal",
                    "pola ini tahun 2024.",
                    "",
                    "Caranya: pasang router atau gateway di depan sistem lama. Semua",
                    "permintaan lewat router itu. Satu fitur dibangun ulang sebagai",
                    "layanan baru, lalu router mengalihkan rute fitur itu ke sana.",
                    "Ulangi per fitur sampai sistem lama nggak melayani apa-apa lagi.",
                ],
            },
            {
                "heading": "Router strangler fig",
                "code": """# Strangler fig: router di depan sistem lama memindahkan rute satu per satu.
def monolit(path):
    return f"monolit lama   {path}"


def layanan_baru(path):
    return f"layanan baru   {path}"


sudah_pindah = set()


def router(path):
    awalan = "/" + path.split("/")[1]
    if awalan in sudah_pindah:
        return layanan_baru(path)
    return monolit(path)


permintaan = ["/produk/7", "/keranjang", "/ongkir/bandung"]
for tahap, rute in enumerate([None, "/ongkir", "/produk"], 1):
    if rute:
        sudah_pindah.add(rute)
    print(f"Tahap {tahap}, sudah pindah: {sorted(sudah_pindah) or '-'}")
    for p in permintaan:
        print("  " + router(p))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Tahap 1, sudah pindah: -",
                    "    monolit lama   /produk/7",
                    "    monolit lama   /keranjang",
                    "    monolit lama   /ongkir/bandung",
                    "  Tahap 2, sudah pindah: ['/ongkir']",
                    "    monolit lama   /produk/7",
                    "    monolit lama   /keranjang",
                    "    layanan baru   /ongkir/bandung",
                    "  Tahap 3, sudah pindah: ['/ongkir', '/produk']",
                    "    layanan baru   /produk/7",
                    "    monolit lama   /keranjang",
                    "    layanan baru   /ongkir/bandung",
                    "",
                    "Pengguna nggak tahu apa-apa. Alamat yang dibukanya tetap sama.",
                    "Yang berubah cuma tujuan di balik router. Kalau layanan ongkir",
                    "yang baru bermasalah, cukup hapus \"/ongkir\" dari daftar dan",
                    "rute itu kembali ke monolit dalam hitungan detik.",
                    "",
                    "Mulailah dari fitur yang batasnya paling jelas dan paling sedikit",
                    "berbagi data, seperti hitung ongkir. Fitur yang menyentuh semua",
                    "tabel, seperti checkout, dipindah paling akhir.",
                    "",
                    "Pola yang sama dipakai untuk pindah framework. Aplikasi AngularJS",
                    "lama, misalnya, bisa dipindah ke Angular modern halaman demi",
                    "halaman dengan router di depannya.",
                ],
            },
            {
                "heading": "Micro-frontends",
                "body": [
                    "Ide microservices juga dibawa ke sisi tampilan. Micro-frontends",
                    "adalah gaya di mana beberapa aplikasi frontend, masing-masing",
                    "dirilis sendiri oleh tim berbeda, digabung jadi satu halaman",
                    "utuh. Definisinya dipopulerkan artikel Cam Jackson di situs",
                    "martinfowler.com tahun 2019.",
                    "",
                    "Contohnya portal belanja besar: tim pencarian memiliki kotak",
                    "cari dan hasil pencarian, tim checkout memiliki keranjang. Cara",
                    "menggabungkannya bisa lewat Module Federation di bundler, Web",
                    "Components, atau komposisi di server.",
                    "",
                    "Jebakan: di tim kecil, micro-frontends cuma menambah kerumitan.",
                    "Ukuran unduhan bisa membengkak karena tiap bagian membawa",
                    "pustakanya sendiri, dan tampilan gampang jadi nggak seragam.",
                    "Detail tekniknya ada di kurikulum Frontend Modern.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Marketplace dan aplikasi transportasi online di Indonesia sering",
                    "bercerita di blog teknik dan konferensi tentang peralihan dari",
                    "monolit ke ratusan layanan, lengkap dengan masalah yang muncul",
                    "sesudahnya. Di sisi lain, banyak startup kecil tetap memakai",
                    "monolit yang tertata bertahun-tahun dan baru memecah bagian yang",
                    "memang punya beban atau tim sendiri.",
                    "",
                    "Kasus kecil: toko online dengan satu monolit Laravel mulai",
                    "kewalahan di fitur hitung ongkir. Fitur itu memanggil API tiga",
                    "kurir, lambat, dan sering diubah karena tarif berganti. Tim ingin",
                    "memisahkannya tanpa mengganggu checkout.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan batasnya jelas. Hitung ongkir cuma butuh alamat",
                    "     asal, alamat tujuan, dan berat. Fitur ini nggak perlu tahu",
                    "     isi tabel pelanggan atau pesanan.",
                    "  2. Bangun layanan ongkir dengan database atau cache-nya sendiri.",
                    "     Jangan biarkan layanan baru membaca tabel monolit langsung.",
                    "  3. Pasang router di depan, lalu alihkan rutenya bertahap:",
                    "       /api/ongkir -> layanan-ongkir (mulai 10% pengguna)",
                    "       sisanya     -> monolit",
                    "  4. Bandingkan hasil dan waktu jawab keduanya. Kalau aman, naikkan",
                    "     ke 100%, lalu hapus kode ongkir dari monolit. Fitur lain tetap",
                    "     di monolit sampai ada alasan kuat untuk memindahkannya.",
                ],
            },
        ],
    },
    {
        "title": "35. Antrean Pesan dan Event-Driven Architecture",
        "sections": [
            {
                "body": [
                    "Waktu pembeli menekan tombol bayar, banyak hal harus terjadi:",
                    "stok dikurangi, email konfirmasi dikirim, faktur PDF dibuat,",
                    "gudang diberi tahu. Kalau semuanya dikerjakan berurutan sebelum",
                    "halaman menjawab, pembeli menunggu lama. Lebih buruk lagi, kalau",
                    "server email sedang lambat, seluruh checkout ikut lambat.",
                    "",
                    "Antrean pesan (message queue) memisahkan pekerjaan yang harus",
                    "dijawab sekarang dari pekerjaan yang boleh menyusul. Pengirim",
                    "pesan disebut produsen, penerimanya disebut konsumen. Produsen",
                    "menitipkan pesan di antrean lalu langsung lanjut. Konsumen",
                    "mengambilnya saat siap. Keduanya nggak harus hidup bersamaan.",
                    "",
                    "Mirip loket bank dengan mesin nomor antrean. Nasabah mengambil",
                    "nomor lalu boleh duduk. Teller memanggil satu per satu sesuai",
                    "kemampuannya. Kalau nasabah datang bergelombang, antreannya",
                    "memanjang, tapi teller nggak kewalahan.",
                ],
            },
            {
                "heading": "Background job dan web-queue-worker",
                "body": [
                    "Pekerjaan yang dititipkan di antrean lalu dikerjakan proses lain",
                    "disebut background job. Polanya punya nama di panduan arsitektur",
                    "Azure: web-queue-worker. Bagian web menjawab permintaan dengan",
                    "cepat, pekerjaan berat masuk antrean, dan worker terpisah",
                    "memprosesnya di belakang.",
                    "",
                    "Hampir semua framework backend punya alatnya:",
                    "  - Laravel Queue, dengan Horizon sebagai dasbornya.",
                    "  - Rails Active Job. Sejak Rails 8 ada Solid Queue yang menyimpan",
                    "    antrean di database, jadi nggak wajib memasang Redis.",
                    "  - Celery untuk Python, Sidekiq untuk Ruby, dan BullMQ untuk",
                    "    Node.js.",
                    "",
                    "Pola ini cocok untuk kirim email massal, ubah ukuran gambar,",
                    "bikin laporan PDF, dan impor data besar.",
                ],
            },
            {
                "heading": "Publish-subscribe dan event-driven",
                "body": [
                    "Antrean biasa mengantar satu pesan ke satu konsumen. Ada pola",
                    "lain bernama publish-subscribe (pub-sub). Penerbit mengumumkan",
                    "sebuah event, yaitu fakta bahwa sesuatu sudah terjadi, misalnya",
                    "\"pesanan dibuat\". Siapa pun yang berlangganan event itu ikut",
                    "menerima salinannya. Penerbit nggak tahu dan nggak peduli siapa",
                    "saja pelanggannya.",
                    "",
                    "Arsitektur yang komponennya berkomunikasi lewat event seperti",
                    "ini disebut event-driven architecture. Program di bawah membuat",
                    "event bus mini: satu event, dua pendengar, dan satu antrean",
                    "untuk pekerjaan yang lambat.",
                ],
            },
            {
                "heading": "Event bus dan antrean mini",
                "code": """from collections import deque

pendengar = {}            # nama event -> daftar fungsi yang mendengarkan
antrean_email = deque()   # pekerjaan lambat dititipkan di sini


def langganan(nama_event, fungsi):
    pendengar.setdefault(nama_event, []).append(fungsi)


def terbitkan(nama_event, data):
    for fungsi in pendengar.get(nama_event, []):
        fungsi(data)


def kurangi_stok(pesanan):
    print(f"stok {pesanan['barang']} dikurangi {pesanan['jumlah']}")


def titip_email(pesanan):
    antrean_email.append(f"email konfirmasi untuk {pesanan['pembeli']}")


langganan("pesanan_dibuat", kurangi_stok)
langganan("pesanan_dibuat", titip_email)

terbitkan("pesanan_dibuat", {"pembeli": "Ani", "barang": "kopi", "jumlah": 2})
terbitkan("pesanan_dibuat", {"pembeli": "Budi", "barang": "teh", "jumlah": 1})
print(f"checkout selesai, antrean berisi {len(antrean_email)} tugas")

# Worker biasanya proses terpisah yang mengambil tugas satu per satu.
while antrean_email:
    print("worker:", antrean_email.popleft())""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  stok kopi dikurangi 2",
                    "  stok teh dikurangi 1",
                    "  checkout selesai, antrean berisi 2 tugas",
                    "  worker: email konfirmasi untuk Ani",
                    "  worker: email konfirmasi untuk Budi",
                    "",
                    "Perhatikan urutannya. Checkout sudah selesai sebelum satu email",
                    "pun terkirim. Email dikerjakan worker belakangan, dan kalau server",
                    "email sedang mati, pesannya tetap menunggu di antrean.",
                    "",
                    "Sekarang bayangkan tim gudang minta diberi tahu setiap ada",
                    "pesanan. Cukup tambah satu langganan baru. Fungsi terbitkan dan",
                    "kode checkout nggak berubah sama sekali. Itu keuntungan utama",
                    "event-driven: penerbit dan pendengar terpisah.",
                    "",
                    "Kata \"event-driven\" sendiri sering dipakai untuk hal yang",
                    "berbeda-beda. Martin Fowler (2017) membedakan empat:",
                    "  - Event notification: event cuma memberi tahu \"ada yang",
                    "    berubah\", penerima bertanya sendiri detailnya.",
                    "  - Event-carried state transfer: event membawa data lengkap,",
                    "    jadi penerima nggak perlu bertanya balik.",
                    "  - Event sourcing: deretan event jadi sumber kebenaran data.",
                    "  - CQRS: model tulis dan model baca dipisah.",
                    "",
                    "Dua yang terakhir dibahas di materi berikutnya.",
                ],
            },
            {
                "heading": "Peta broker pesan",
                "body": [
                    "Di produksi, antrean nggak disimpan di memori program. Ia",
                    "disimpan di broker, yaitu server khusus yang menerima, menyimpan,",
                    "dan mengantar pesan.",
                    "",
                    "  broker            sifat utama                     lisensi",
                    "  RabbitMQ          antrean klasik, AMQP, routing    MPL-2.0",
                    "  Apache Kafka      log terurut yang bisa diputar    Apache-2.0",
                    "  Amazon SQS/SNS    antrean dan pub-sub terkelola    layanan AWS",
                    "  EventBridge       bus event terkelola AWS          layanan AWS",
                    "  Redis Streams     stream di atas Redis/Valkey      RSAL/SSPL/AGPL",
                    "  NATS              ringan, cepat, ada JetStream     Apache-2.0",
                    "",
                    "RabbitMQ cocok untuk antrean tugas biasa. Versi 4 menjadikan",
                    "quorum queue sebagai cara utama menyimpan antrean yang tahan",
                    "server mati.",
                    "",
                    "Kafka berbeda cara pikirnya. Kafka menyimpan pesan sebagai log",
                    "yang terus bertambah dan bisa dibaca ulang dari awal oleh",
                    "konsumen baru. Cocok untuk aliran data besar dan event yang",
                    "perlu diputar ulang. Sejak Kafka 4.0 (2025), ZooKeeper dihapus",
                    "dan Kafka cuma berjalan dalam mode KRaft.",
                    "",
                    "Amazon SQS, SNS, dan EventBridge adalah versi terkelola di AWS.",
                    "Padanannya di Google Cloud adalah Pub/Sub, di Azure ada Service",
                    "Bus dan Event Grid. Redis Streams praktis kalau Redis sudah ada",
                    "di stack-mu, dan Valkey (fork Redis berlisensi BSD) punya fitur",
                    "yang sama. NATS populer di ekosistem Go dan cloud native.",
                    "",
                    "Survei Stack Overflow 2024 mencatat RabbitMQ dipakai 10,9%",
                    "responden dan Kafka 9,4%. Redis, yang sering merangkap broker",
                    "antrean, dipakai 28,3% responden di survei 2026.",
                ],
            },
            {
                "heading": "Jebakan yang selalu datang",
                "body": [
                    "Antrean menyelesaikan satu masalah dan membawa beberapa masalah",
                    "baru:",
                    "  - Pesan bisa terkirim lebih dari sekali. Kebanyakan broker",
                    "    menjanjikan at-least-once, artinya \"minimal sekali\". Kalau",
                    "    konsumen mati sesudah memproses tapi sebelum melapor selesai,",
                    "    pesan yang sama dikirim lagi. Konsumen harus idempoten, aman",
                    "    menerima pesan yang sama dua kali.",
                    "  - Urutan nggak selalu terjaga, apalagi kalau konsumennya",
                    "    banyak.",
                    "  - Pesan yang selalu gagal (poison message) bisa diulang tanpa",
                    "    henti. Sesudah beberapa kali gagal, pindahkan ke dead-letter",
                    "    queue, yaitu antrean khusus untuk diperiksa manusia.",
                    "  - Datanya jadi konsisten akhir. Sesaat sesudah checkout, stok di",
                    "    layanan gudang mungkin belum berkurang.",
                    "",
                    "Latihan di akhir bab ini memintamu menulis konsumen yang mencoba",
                    "ulang dengan jeda, membuang id ganda, dan memindahkan pesan yang",
                    "terus gagal ke dead-letter queue.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Notifikasi \"pesananmu sedang dikemas\" di aplikasi belanja,",
                    "email reset sandi, dan laporan bulanan yang dikirim tengah malam",
                    "hampir selalu lewat antrean. Pembayaran online juga memakai",
                    "event: penyedia pembayaran mengirim webhook, aplikasi",
                    "menitipkannya di antrean, lalu worker memperbarui status pesanan.",
                    "",
                    "Kasus kecil: aplikasi pendaftaran lomba sekolah mengirim email",
                    "konfirmasi langsung di dalam proses pendaftaran. Saat pendaftaran",
                    "dibuka, 2.000 siswa mendaftar dalam sepuluh menit, server email",
                    "membatasi pengiriman, dan halaman pendaftaran jadi timeout.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan yang wajib sekarang dari yang boleh menyusul.",
                    "     Menyimpan data pendaftar wajib sekarang. Email boleh",
                    "     menyusul beberapa menit.",
                    "  2. Ganti pengiriman langsung dengan menitipkan tugas ke antrean.",
                    "     Di Laravel misalnya:",
                    "       KirimKonfirmasi::dispatch($pendaftar);",
                    "  3. Jalankan worker terpisah dengan jumlah yang sesuai batas",
                    "     server email, supaya pengiriman mengalir rata.",
                    "  4. Pasang dead-letter queue untuk email yang terus gagal,",
                    "     misalnya karena alamatnya salah ketik, lalu tampilkan di",
                    "     halaman admin supaya panitia bisa menghubungi siswanya.",
                ],
            },
        ],
    },
    {
        "title": "36. CQRS, Event Sourcing, dan Saga",
        "sections": [
            {
                "body": [
                    "Tiga pola di materi ini sering muncul di artikel arsitektur dan",
                    "wawancara kerja. Ketiganya berguna di sistem tertentu, dan",
                    "ketiganya juga sering dipasang di tempat yang nggak butuh.",
                    "Martin Fowler menulis soal CQRS bahwa untuk kebanyakan sistem,",
                    "pola itu menambah kerumitan yang berisiko. Jadi pelajari cara",
                    "kerjanya, lalu pakai cuma di bagian sistem yang memang butuh.",
                ],
            },
            {
                "heading": "CQRS: model tulis dan model baca dipisah",
                "body": [
                    "CQRS singkatan dari Command Query Responsibility Segregation.",
                    "Command adalah perintah yang mengubah data (buat pesanan, ubah",
                    "alamat). Query adalah pertanyaan yang cuma membaca (tampilkan",
                    "riwayat pesanan). CQRS memisahkan model untuk keduanya.",
                    "",
                    "Contohnya laporan penjualan toko. Sisi tulis menyimpan tiap",
                    "transaksi di tabel yang ternormalisasi, rapi untuk menjaga",
                    "kebenaran. Sisi baca menyimpan tabel ringkasan \"omzet per hari",
                    "per kategori\" yang sudah jadi. Halaman laporan tinggal membaca",
                    "ringkasan itu tanpa JOIN berat. Setiap ada transaksi baru, tabel",
                    "ringkasan diperbarui, biasanya lewat event.",
                    "",
                    "Bayarannya: sisi baca bisa tertinggal sebentar dari sisi tulis,",
                    "dan ada dua model yang harus dirawat. Jangan tertukar dengan CQS",
                    "(Command-Query Separation) dari Bertrand Meyer, yang berlaku di",
                    "tingkat fungsi: satu fungsi sebaiknya mengubah data atau",
                    "mengembalikan nilai, jangan dua-duanya.",
                ],
            },
            {
                "heading": "Event sourcing: simpan kejadiannya",
                "body": [
                    "Biasanya database menyimpan keadaan terakhir: saldo Ani 255.000.",
                    "Event sourcing menyimpan seluruh kejadian yang membuat saldo itu,",
                    "lalu keadaan sekarang dihitung ulang dengan memutar kejadiannya",
                    "dari awal.",
                    "",
                    "Kamu sebetulnya sudah memakai sesuatu yang mirip: Git. Git",
                    "menyimpan deretan commit, dan isi folder kerjamu adalah hasil",
                    "memutar commit-commit itu. Buku tabungan bank juga begitu: ada",
                    "daftar setor dan tarik, dan saldo di baris terakhir bisa dicek",
                    "ulang dari daftar itu.",
                ],
            },
            {
                "heading": "Saldo dari deretan event",
                "code": """from functools import reduce

# Yang disimpan cuma deretan kejadian. Saldo dihitung dari situ.
events = [
    ("rekening_dibuka", 0),
    ("disetor", 500_000),
    ("ditarik", 120_000),
    ("disetor", 75_000),
    ("ditarik", 200_000),
]


def terapkan(saldo, event):
    jenis, jumlah = event
    if jenis == "disetor":
        return saldo + jumlah
    if jenis == "ditarik":
        return saldo - jumlah
    return saldo


print(f"{'saldo sekarang':<24}:", reduce(terapkan, events, 0))
print(f"{'saldo sesudah event ke-3':<24}:", reduce(terapkan, events[:3], 0))

# Snapshot: simpan hasil sampai event ke-3, lalu putar sisanya saja.
snapshot = {"versi": 3, "saldo": reduce(terapkan, events[:3], 0)}
print(f"{'dihitung dari snapshot':<24}:", reduce(terapkan, events[3:], snapshot["saldo"]))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  saldo sekarang          : 255000",
                    "  saldo sesudah event ke-3: 380000",
                    "  dihitung dari snapshot  : 255000",
                    "",
                    "Baris kedua menunjukkan kekuatan event sourcing: kamu bisa",
                    "menjawab \"berapa saldonya waktu itu?\" untuk titik waktu mana",
                    "pun, dan tahu persis kenapa angkanya begitu. Karena itu pola ini",
                    "disukai untuk buku besar keuangan dan jejak audit.",
                    "",
                    "Kalau event-nya sudah jutaan, memutar dari awal setiap kali",
                    "jadi lambat. Solusinya snapshot: simpan keadaan di satu titik,",
                    "lalu putar event sesudahnya saja. Baris ketiga memberi hasil yang",
                    "sama dengan baris pertama, tapi cuma memutar dua event.",
                    "",
                    "Event sourcing hampir selalu dipasangkan dengan CQRS. Log event",
                    "jadi sisi tulis, dan tampilan yang enak dibaca dibangun dari",
                    "event itu sebagai sisi baca. Database khusus untuk pola ini",
                    "misalnya EventStoreDB (sekarang bermerek Kurrent). Survei Stack",
                    "Overflow 2024 mencatatnya dipakai 0,3% responden, jadi ini",
                    "memang pola untuk kebutuhan khusus.",
                    "",
                    "Jebakan: event lama nggak boleh diubah, jadi mengganti bentuk",
                    "event butuh rencana versi. Data pribadi yang suatu hari harus",
                    "dihapus juga jadi rumit kalau tertulis di log yang seharusnya",
                    "nggak pernah berubah.",
                ],
            },
            {
                "heading": "Saga: transaksi yang melewati banyak layanan",
                "body": [
                    "Di monolit dengan satu database, checkout bisa dibungkus satu",
                    "transaksi: kurangi stok, catat pembayaran, buat jadwal kirim.",
                    "Kalau satu gagal, ROLLBACK membatalkan semuanya. Di microservices,",
                    "stok, pembayaran, dan pengiriman ada di tiga layanan dengan tiga",
                    "database. Nggak ada satu transaksi yang bisa membungkus ketiganya.",
                    "",
                    "Saga memecah transaksi besar jadi rangkaian transaksi lokal.",
                    "Tiap langkah punya pasangan berupa transaksi kompensasi, yaitu",
                    "langkah yang membatalkan efeknya. Kalau langkah ketiga gagal,",
                    "kompensasi langkah kedua dan pertama dijalankan, urut terbalik.",
                    "",
                    "Ada dua gaya mengaturnya:",
                    "  - Koreografi. Tiap layanan bereaksi pada event layanan lain.",
                    "    Stok mendengar \"pesanan dibuat\", pembayaran mendengar \"stok",
                    "    dipesan\", dan seterusnya. Nggak ada pengatur pusat, tapi",
                    "    alurnya susah dilihat utuh.",
                    "  - Orkestrasi. Satu orkestrator menyuruh tiap layanan secara",
                    "    berurutan dan menjalankan kompensasi kalau ada yang gagal.",
                    "    Alurnya terbaca di satu tempat.",
                    "",
                    "Program berikut memakai gaya orkestrasi.",
                ],
            },
            {
                "heading": "Saga dengan kompensasi",
                "code": """# Saga dengan orkestrator: tiap langkah punya pasangan pembatalnya.
def pesan_stok(log):
    log.append("stok dipesan")
    return True


def kembalikan_stok(log):
    log.append("kompensasi: stok dikembalikan")


def tagih(log):
    log.append("pembayaran ditagih")
    return True


def refund(log):
    log.append("kompensasi: pembayaran direfund")


def jadwalkan_kurir(log):
    log.append("kurir menolak: alamat di luar jangkauan")
    return False


def batalkan_kurir(log):
    log.append("kompensasi: jadwal kurir dibatalkan")


LANGKAH = [(pesan_stok, kembalikan_stok), (tagih, refund),
           (jadwalkan_kurir, batalkan_kurir)]


def jalankan_saga(langkah):
    log, berhasil = [], []
    for lakukan, batalkan in langkah:
        if lakukan(log):
            berhasil.append(batalkan)
            continue
        for batal in reversed(berhasil):
            batal(log)
        log.append("saga gagal, pesanan dibatalkan dengan rapi")
        return log
    log.append("saga selesai, pesanan dikirim")
    return log


for baris in jalankan_saga(LANGKAH):
    print(baris)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  stok dipesan",
                    "  pembayaran ditagih",
                    "  kurir menolak: alamat di luar jangkauan",
                    "  kompensasi: pembayaran direfund",
                    "  kompensasi: stok dikembalikan",
                    "  saga gagal, pesanan dibatalkan dengan rapi",
                    "",
                    "Kompensasi beda dengan ROLLBACK. ROLLBACK membuat seolah",
                    "transaksinya nggak pernah ada. Kompensasi adalah transaksi baru",
                    "yang membalik efeknya, dan jejaknya tetap kelihatan. Pembeli",
                    "melihat tagihan lalu refund di riwayat pembayarannya. Selama",
                    "saga berjalan, orang lain juga bisa melihat keadaan setengah",
                    "jadi, misalnya stok yang sempat berkurang.",
                    "",
                    "Ada satu masalah halus. Layanan biasanya harus mengubah",
                    "databasenya dan menerbitkan event. Kalau database berhasil tapi",
                    "event gagal terkirim, saga macet. Pola outbox mengatasinya:",
                    "event ditulis ke tabel outbox di transaksi lokal yang sama, lalu",
                    "proses lain membaca tabel itu dan mengirimkannya ke broker.",
                    "",
                    "Menulis orkestrator yang tahan server mati di tengah jalan itu",
                    "sulit. Karena itu ada mesin workflow seperti Temporal, yang",
                    "menjamin alur kerja panjang tetap selesai walau prosesnya mati",
                    "dan dinyalakan ulang. Temporal berlisensi MIT, dan di survei",
                    "Stack Overflow 2026 ia dipakai 6% responden yang menjawab",
                    "pertanyaan alat otomasi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi pemesanan perjalanan yang menggabungkan tiket pesawat,",
                    "hotel, dan mobil sewaan adalah contoh klasik saga: kalau hotel",
                    "penuh, tiket yang sudah dipesan harus dibatalkan. Bank dan",
                    "dompet digital memakai pola yang mirip event sourcing untuk buku",
                    "besar, karena setiap perubahan saldo harus bisa ditelusuri.",
                    "",
                    "Kasus kecil: layanan pesan-antar makanan punya tiga layanan:",
                    "pesanan, pembayaran, dan pencarian kurir. Kadang pembayaran",
                    "sudah terpotong, tapi kurir nggak ketemu dalam lima menit, dan",
                    "pelanggan menunggu tanpa kejelasan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis langkahnya berurutan beserta kompensasinya:",
                    "       buat pesanan     <-> batalkan pesanan",
                    "       potong saldo     <-> kembalikan saldo",
                    "       cari kurir       <-> (tidak perlu, gagal = tidak ada efek)",
                    "  2. Pilih orkestrasi, karena alurnya perlu terlihat di satu",
                    "     tempat untuk tim layanan pelanggan.",
                    "  3. Beri batas waktu langkah cari kurir. Lewat lima menit,",
                    "     anggap gagal dan jalankan kompensasi urut terbalik.",
                    "  4. Pakai outbox dan kunci idempotensi supaya \"kembalikan saldo\"",
                    "     nggak terkirim dua kali walau event-nya terulang.",
                ],
            },
        ],
    },
    {
        "title": "37. Retry, Idempotensi, dan Circuit Breaker",
        "sections": [
            {
                "body": [
                    "Begitu layanan saling memanggil lewat jaringan, kegagalan jadi",
                    "kejadian sehari-hari. Paket hilang, layanan sedang restart, atau",
                    "database tujuan lagi sibuk. Tanpa rencana, tiga hal buruk bisa",
                    "terjadi:",
                    "  - Pengguna menunggu tanpa batas karena panggilan nggak pernah",
                    "    dijawab.",
                    "  - Semua klien mengulang bersamaan, sehingga layanan yang baru",
                    "    pulih langsung tumbang lagi.",
                    "  - Pembayaran yang diulang tertagih dua kali.",
                    "",
                    "Materi ini membahas empat alat untuk mencegahnya: timeout,",
                    "retry dengan backoff, idempotensi, dan circuit breaker.",
                ],
            },
            {
                "heading": "Timeout lebih dulu",
                "body": [
                    "Timeout adalah batas lama menunggu jawaban. Tanpa timeout,",
                    "satu layanan yang hang bisa menahan thread pemanggilnya",
                    "selamanya, dan thread yang tertahan itu lama-lama menghabiskan",
                    "kapasitas server pemanggil.",
                    "",
                    "Banyak pustaka HTTP nggak memasang timeout secara bawaan. Pustaka",
                    "requests di Python, misalnya, menunggu tanpa batas kalau",
                    "parameter timeout nggak diisi, dan dokumentasinya menyarankan",
                    "agar kode produksi selalu mengisinya. Pilih angkanya dari data:",
                    "sedikit di atas persentil p99 waktu jawab layanan tujuan.",
                ],
            },
            {
                "heading": "Retry dengan exponential backoff dan jitter",
                "body": [
                    "Retry artinya mengulang panggilan yang gagal. Yang layak diulang",
                    "cuma kegagalan sementara: timeout, 503 Service Unavailable, atau",
                    "429 yang disertai Retry-After. Error 400, 401, atau 404 nggak",
                    "akan sembuh dengan diulang.",
                    "",
                    "Jeda antar percobaan sebaiknya makin panjang: 100 ms, 200 ms,",
                    "400 ms, dan seterusnya. Pola ini disebut exponential backoff,",
                    "dan diberi atap supaya nggak menunggu kelamaan.",
                    "",
                    "Backoff saja belum cukup. Kalau seribu klien gagal di detik yang",
                    "sama, mereka juga akan mengulang di detik yang sama, lalu",
                    "gagal lagi bersama-sama. Jitter, yaitu jeda acak, menyebar",
                    "percobaan mereka. Artikel Marc Brooker di Amazon Builders'",
                    "Library merekomendasikan full jitter: jeda diacak antara nol",
                    "sampai batas backoff.",
                    "",
                    "Program di bawah memakai random.Random dengan benih tetap supaya",
                    "keluarannya selalu sama. Di kode sungguhan, benihnya jangan",
                    "ditetapkan. Bagian kedua program menunjukkan kunci idempotensi,",
                    "yang dibahas sesudahnya.",
                ],
            },
            {
                "heading": "Backoff, jitter, dan kunci idempotensi",
                "code": """import random

rng = random.Random(7)   # benih tetap supaya contoh ini selalu sama


def jeda_backoff(percobaan, dasar=100, atap=2000):
    batas = min(atap, dasar * 2 ** percobaan)
    return batas, int(rng.random() * batas)   # full jitter: acak 0..batas


print("percobaan  batas(ms)  jeda dengan jitter(ms)")
for ke in range(6):
    batas, jeda = jeda_backoff(ke)
    print(f"{ke + 1:>9}  {batas:>9}  {jeda:>22}")

# Kunci idempotensi: permintaan yang sama diulang tidak menagih dua kali.
sudah_diproses = {}


def bayar(kunci, jumlah):
    if kunci in sudah_diproses:
        return sudah_diproses[kunci] + " (ulangan, tidak ditagih lagi)"
    hasil = f"tertagih Rp{jumlah:,}".replace(",", ".")
    sudah_diproses[kunci] = hasil
    return hasil


print(bayar("pesanan-881-bayar", 85000))
print(bayar("pesanan-881-bayar", 85000))   # klien mengulang karena timeout
print(bayar("pesanan-882-bayar", 40000))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  percobaan  batas(ms)  jeda dengan jitter(ms)",
                    "          1        100                      32",
                    "          2        200                      30",
                    "          3        400                     260",
                    "          4        800                      57",
                    "          5       1600                     857",
                    "          6       2000                     731",
                    "  tertagih Rp85.000",
                    "  tertagih Rp85.000 (ulangan, tidak ditagih lagi)",
                    "  tertagih Rp40.000",
                    "",
                    "Kolom batas naik dua kali lipat sampai mentok di atap 2000 ms.",
                    "Kolom jitter melompat-lompat. Percobaan keempat malah lebih",
                    "pendek dari percobaan ketiga, dan memang begitu tujuannya: klien",
                    "yang berbeda mendapat jeda yang berbeda, jadi percobaan ulang",
                    "mereka tersebar.",
                    "",
                    "Batasi juga jumlah percobaan, misalnya tiga kali. Retry tanpa",
                    "batas di setiap lapisan bisa berlipat: kalau tiga lapisan",
                    "masing-masing mengulang tiga kali, satu klik pengguna jadi 27",
                    "panggilan ke layanan paling bawah.",
                ],
            },
            {
                "heading": "Idempotensi",
                "body": [
                    "Operasi idempoten aman diulang: hasilnya sama walau dijalankan",
                    "sekali atau sepuluh kali. Menurut aturan HTTP, GET, PUT, dan",
                    "DELETE seharusnya idempoten. POST nggak. Mengirim POST /bayar",
                    "dua kali bisa berarti dua pembayaran.",
                    "",
                    "Masalahnya, klien sering nggak tahu apakah panggilan pertamanya",
                    "berhasil. Bisa saja server sudah menagih, tapi jawabannya hilang",
                    "di jalan dan klien kena timeout. Kalau klien mengulang, terjadilah",
                    "tagihan ganda.",
                    "",
                    "Solusinya kunci idempotensi. Klien membuat satu kunci unik untuk",
                    "satu niat (\"bayar pesanan 881\") dan mengirimnya di header.",
                    "Server mencatat kunci yang sudah diproses beserta hasilnya. Kalau",
                    "kunci yang sama datang lagi, server mengembalikan hasil yang",
                    "tercatat tanpa menagih ulang. Itulah yang terjadi di baris kedua",
                    "keluaran tadi. Dokumentasi Stripe membolehkan kunci sampai 255",
                    "karakter, menyarankan UUID v4, dan meminta agar data sensitif",
                    "seperti alamat email nggak dipakai sebagai kunci.",
                    "",
                    "Konsumen antrean pesan butuh hal yang sama, karena broker bisa",
                    "mengirim pesan yang sama lebih dari sekali. Id pesan dipakai",
                    "sebagai kunci idempotensinya.",
                ],
            },
            {
                "heading": "Circuit breaker dan bulkhead",
                "body": [
                    "Retry menolong kalau gangguannya sebentar. Kalau layanan tujuan",
                    "mati lima menit, retry justru menambah beban dan membuat",
                    "pemanggil ikut lambat. Circuit breaker menghentikan panggilan",
                    "untuk sementara, mirip MCB listrik di rumah yang turun saat ada",
                    "korsleting supaya kabelnya nggak terbakar.",
                    "",
                    "Circuit breaker punya tiga keadaan:",
                    "  - Closed. Normal, panggilan diteruskan, kegagalan dihitung.",
                    "  - Open. Kegagalan melewati ambang. Panggilan langsung ditolak",
                    "    tanpa menyentuh layanan tujuan, selama masa tunggu.",
                    "  - Half-open. Masa tunggu habis. Sebagian kecil panggilan uji",
                    "    diteruskan. Kalau berhasil, kembali closed. Kalau gagal,",
                    "    kembali open.",
                    "",
                    "Panduan Azure menegaskan bahwa retry dan circuit breaker punya",
                    "tujuan berbeda. Retry berharap panggilan berikutnya berhasil.",
                    "Circuit breaker mencegah panggilan yang kemungkinan besar gagal.",
                    "Keduanya sering dipasang bersama: retry di dalam, breaker di",
                    "luarnya. Saat breaker open, aplikasi bisa memberi jawaban",
                    "cadangan (fallback), misalnya ongkir perkiraan dari tabel.",
                    "",
                    "Bulkhead adalah sekat di lambung kapal. Kalau satu ruang bocor,",
                    "air nggak membanjiri ruang lain. Di perangkat lunak, bulkhead",
                    "berarti memisahkan kolam koneksi atau thread per tujuan. Kalau",
                    "layanan ongkir hang, yang habis cuma kolam untuk ongkir, dan",
                    "panggilan ke layanan produk tetap jalan.",
                    "",
                    "Kamu jarang menulis semua ini dari nol. Resilience4j (Java,",
                    "Apache-2.0) dan Polly (.NET, BSD-3-Clause) menyediakan retry,",
                    "circuit breaker, bulkhead, dan timeout. Service mesh juga bisa",
                    "melakukannya di luar kode, dibahas di materi berikutnya. Contoh",
                    "konfigurasi Resilience4j di Spring Boot:",
                ],
            },
            {
                "heading": "Konfigurasi Resilience4j (application.yml)",
                "bahasa": "yaml",
                "code": """resilience4j:
  circuitbreaker:
    instances:
      ongkir:
        slidingWindowSize: 10
        failureRateThreshold: 50
        waitDurationInOpenState: 30s
        permittedNumberOfCallsInHalfOpenState: 3""",
            },
            {
                "body": [
                    "Artinya: lihat sepuluh panggilan terakhir ke layanan ongkir.",
                    "Kalau separuhnya gagal, breaker open selama 30 detik. Sesudah",
                    "itu tiga panggilan uji boleh lewat untuk menentukan nasibnya.",
                    "",
                    "Pustaka sungguhan memakai persentase kegagalan di jendela",
                    "geser seperti ini. Latihan di akhir bab memakai versi yang lebih",
                    "sederhana, yaitu jumlah kegagalan beruntun, supaya ketiga",
                    "keadaannya gampang diikuti.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi toko online yang memanggil API kurir, API pembayaran,",
                    "dan API pajak hampir pasti memakai timeout, retry, dan circuit",
                    "breaker. Penyedia pembayaran seperti Stripe menyediakan kunci",
                    "idempotensi persis untuk kasus klien yang mengulang karena",
                    "timeout.",
                    "",
                    "Kasus kecil: halaman checkout sebuah toko memanggil API ongkir",
                    "pihak ketiga. Suatu siang API itu lambat 30 detik per panggilan.",
                    "Checkout ikut macet, padahal pembayaran dan stok baik-baik saja.",
                    "Sesudah API ongkir pulih, toko masih lambat beberapa menit karena",
                    "semua permintaan yang tertunda mengulang bersamaan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang timeout yang masuk akal, misalnya 2 detik, karena",
                    "     p99 API ongkir biasanya 600 ms.",
                    "  2. Retry paling banyak dua kali dengan backoff dan full jitter,",
                    "     supaya percobaan ulang nggak datang serentak.",
                    "  3. Bungkus dengan circuit breaker. Kalau separuh dari sepuluh",
                    "     panggilan terakhir gagal, open selama 30 detik.",
                    "  4. Sediakan fallback saat breaker open:",
                    "       ongkir = tabel_tarif_perkiraan[kota_tujuan]",
                    "       tampilkan(\"Ongkir perkiraan, final dihitung saat dikemas\")",
                    "  5. Pisahkan kolam koneksi untuk API ongkir (bulkhead), supaya",
                    "     panggilan ke layanan lain nggak ikut tertahan.",
                ],
            },
        ],
    },
    {
        "title": "38. API Gateway, BFF, dan Service Mesh",
        "sections": [
            {
                "body": [
                    "Bayangkan aplikasi HP sebuah toko harus tahu alamat sepuluh",
                    "layanan: produk, ongkir, keranjang, pembayaran, dan seterusnya.",
                    "Tiap kali satu layanan pindah alamat, aplikasi harus dirilis",
                    "ulang. Tiap layanan juga harus memeriksa token, membatasi",
                    "permintaan, dan mencatat log sendiri-sendiri.",
                    "",
                    "Tiga pola di materi ini merapikan lalu lintas itu. API gateway",
                    "mengurus pintu masuk dari luar. Backend for Frontend membentuk",
                    "data untuk tiap jenis tampilan. Service mesh mengurus lalu lintas",
                    "di antara layanan di dalam.",
                ],
            },
            {
                "heading": "API gateway",
                "body": [
                    "API gateway adalah satu pintu masuk untuk semua klien. Ia",
                    "meneruskan permintaan ke layanan yang tepat berdasarkan path,",
                    "sekaligus mengurus hal yang dibutuhkan semua layanan:",
                    "  - memeriksa token dan identitas,",
                    "  - rate limiting (bab sebelumnya),",
                    "  - mengakhiri TLS, jadi layanan di dalam nggak perlu mengurus",
                    "    sertifikat,",
                    "  - mencatat log dan metrik setiap permintaan,",
                    "  - menggabungkan beberapa jawaban jadi satu.",
                    "",
                    "Roadmap System Design di roadmap.sh memecahnya jadi tiga pola",
                    "turunan: gateway routing (meneruskan), gateway aggregation",
                    "(menggabungkan), dan gateway offloading (mengambil alih tugas",
                    "bersama seperti TLS).",
                    "",
                    "Produk yang sering dipakai: Kong, Envoy, Nginx, Amazon API",
                    "Gateway, dan Azure API Management. Konfigurasinya biasanya",
                    "deklaratif. Contoh berkas kong.yml berikut mendaftarkan satu",
                    "layanan, satu rute, dan pembatas 60 permintaan per menit:",
                ],
            },
            {
                "heading": "Konfigurasi deklaratif Kong (kong.yml)",
                "bahasa": "yaml",
                "code": """_format_version: "3.0"
services:
  - name: produk
    url: http://produk:8080
    routes:
      - name: rute-produk
        paths:
          - /produk
    plugins:
      - name: rate-limiting
        config:
          minute: 60""",
            },
            {
                "heading": "Backend for Frontend",
                "body": [
                    "Aplikasi web dan aplikasi HP sering butuh data yang berbeda dari",
                    "layanan yang sama. Halaman web produk menampilkan deskripsi",
                    "panjang dan ulasan. Kartu produk di aplikasi HP cuma butuh nama,",
                    "harga, dan ongkir, dan jaringan seluler mahal untuk data yang",
                    "nggak dipakai.",
                    "",
                    "Backend for Frontend (BFF) adalah backend khusus untuk satu jenis",
                    "tampilan. BFF mobile memanggil beberapa layanan, menggabungkan",
                    "hasilnya, lalu mengirim persis yang dibutuhkan aplikasi HP.",
                    "Istilah ini dicetuskan Phil Calçado di SoundCloud dan",
                    "dipopulerkan Sam Newman. Di dunia JavaScript, Route Handlers",
                    "Next.js sering berperan sebagai BFF untuk frontend-nya sendiri.",
                    "",
                    "Program berikut membuat gateway mini dan BFF mobile di atasnya.",
                ],
            },
            {
                "heading": "Gateway mini dan BFF mobile",
                "code": "# Dua layanan di belakang gateway. Datanya ditulis langsung supaya ringkas.\ndef layanan_produk(path):\n    return {\"id\": 7, \"nama\": \"Kopi Gayo 250 g\", \"harga\": 85000,\n            \"deskripsi\": \"Arabika dari Aceh Tengah, sangrai sedang.\",\n            \"ulasan\": 128, \"stok_gudang\": {\"bdg\": 40, \"jkt\": 12}}\n\n\ndef layanan_ongkir(path):\n    return {\"kota\": path.split(\"/\")[-1], \"biaya\": 12000}\n\n\nRUTE = {\"/produk\": layanan_produk, \"/ongkir\": layanan_ongkir}\nTOKEN_SAH = {\"tok-ani\": \"ani\"}\n\n\ndef gateway(path, token):\n    \"\"\"Satu pintu masuk: cek token, lalu teruskan menurut awalan path.\"\"\"\n    if token not in TOKEN_SAH:\n        return 401, {\"error\": \"token tidak sah\"}\n    for awalan, layanan in RUTE.items():\n        if path.startswith(awalan):\n            return 200, layanan(path)\n    return 404, {\"error\": \"rute tidak ada\"}\n\n\ndef bff_mobile(id_produk, kota, token):\n    \"\"\"Backend khusus aplikasi HP: gabungkan dua panggilan, kirim seperlunya.\"\"\"\n    kode, produk = gateway(f\"/produk/{id_produk}\", token)\n    if kode != 200:\n        return kode, produk\n    _, ongkir = gateway(f\"/ongkir/{kota}\", token)\n    return 200, {\"nama\": produk[\"nama\"], \"harga\": produk[\"harga\"],\n                 \"ongkir\": ongkir[\"biaya\"]}\n\n\nkode, data = gateway(\"/produk/7\", \"tok-ani\")\nprint(\"web   :\", kode, \"kolom:\", \", \".join(data))\nprint(\"mobile:\", *bff_mobile(7, \"bandung\", \"tok-ani\"))\nprint(\"asing :\", *gateway(\"/produk/7\", \"tok-palsu\"))\nprint(\"salah :\", *gateway(\"/promo\", \"tok-ani\"))",
            },
            {
                "body": [
                    "Keluaran:",
                    "  web   : 200 kolom: id, nama, harga, deskripsi, ulasan, stok_gudang",
                    "  mobile: 200 {'nama': 'Kopi Gayo 250 g', 'harga': 85000, 'ongkir': 12000}",
                    "  asing : 401 {'error': 'token tidak sah'}",
                    "  salah : 404 {'error': 'rute tidak ada'}",
                    "",
                    "Web menerima enam kolom langsung dari layanan produk. Aplikasi HP",
                    "cukup satu panggilan ke BFF dan menerima tiga kolom, termasuk",
                    "ongkir yang diambil BFF dari layanan lain. Pemeriksaan token",
                    "cuma ditulis sekali di gateway, dan berlaku untuk semua rute.",
                    "",
                    "Bedanya dengan gateway: gateway satu untuk semua klien dan",
                    "sebaiknya tetap tipis, sedangkan BFF satu per jenis tampilan dan",
                    "boleh berisi logika penggabungan untuk tampilan itu. Biasanya BFF",
                    "dimiliki tim frontend yang memakainya. GraphQL adalah jalan lain",
                    "untuk masalah yang sama: klien sendiri yang memilih kolom yang",
                    "dibutuhkan.",
                ],
            },
            {
                "heading": "Service mesh dan sidecar",
                "body": [
                    "Gateway mengurus lalu lintas dari luar ke dalam. Di dalam,",
                    "layanan juga saling memanggil, dan tiap panggilan butuh hal yang",
                    "sama: enkripsi, retry, timeout, metrik. Menulisnya di tiap",
                    "layanan, apalagi kalau bahasanya beda-beda, cepat jadi berantakan.",
                    "",
                    "Service mesh memindahkan urusan itu ke luar kode. Di samping tiap",
                    "layanan dipasang proses pendamping bernama sidecar, biasanya",
                    "proxy Envoy. Semua lalu lintas masuk dan keluar layanan lewat",
                    "sidecar itu. Sidecar yang mengenkripsi koneksi antarlayanan",
                    "(mTLS), mengulang yang gagal, membagi lalu lintas untuk canary,",
                    "dan mengirim metrik.",
                    "",
                    "Dua yang paling dikenal:",
                    "  - Istio. Versi stabil terbaru saat materi ini ditulis (Oktober",
                    "    2026) adalah 1.31.2. Sejak 2024 Istio juga punya mode ambient",
                    "    yang bekerja tanpa sidecar per layanan.",
                    "  - Linkerd. Lebih ringan dan sederhana. Sejak Februari 2024",
                    "    proyek open source-nya cuma merilis versi edge, sedangkan",
                    "    rilis stabil disediakan vendor (Buoyant).",
                    "",
                    "Keduanya proyek CNCF berlisensi Apache-2.0 dan berjalan di atas",
                    "Kubernetes. Cara memasangnya ada di kurikulum DevOps & Cloud.",
                    "",
                    "Status jujurnya: banyak organisasi menilai service mesh terlalu",
                    "rumit untuk tim kecil. Ia masuk akal saat layanannya puluhan",
                    "atau ratusan dan butuh enkripsi antarlayanan yang seragam.",
                ],
            },
            {
                "heading": "Kapan nggak perlu",
                "body": [
                    "  keadaanmu                              cukup pakai",
                    "  satu monolit, satu frontend            reverse proxy (Nginx, Caddy)",
                    "  beberapa layanan, API publik            API gateway",
                    "  web dan HP butuh data berbeda           gateway + BFF per tampilan",
                    "  puluhan layanan, wajib mTLS internal    gateway + service mesh",
                    "",
                    "Mulailah dari baris teratas yang cocok dengan keadaanmu. Turun",
                    "ke baris berikutnya kalau ada masalah nyata yang nggak bisa",
                    "diselesaikan baris sebelumnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi belanja yang punya versi web dan aplikasi HP hampir",
                    "selalu punya gateway di depan layanannya. Aplikasi serverless di",
                    "AWS memakai Amazon API Gateway sebagai pintu masuk fungsi Lambda.",
                    "Perusahaan dengan ratusan layanan di Kubernetes memakai Istio",
                    "atau Linkerd untuk enkripsi antarlayanan.",
                    "",
                    "Kasus kecil: aplikasi HP sebuah toko memanggil lima layanan",
                    "langsung untuk menampilkan satu halaman produk. Di jaringan 3G",
                    "halaman itu butuh delapan detik, dan tiap layanan memeriksa",
                    "token dengan cara yang sedikit berbeda.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang API gateway sebagai satu-satunya pintu dari luar, dan",
                    "     pindahkan pemeriksaan token ke sana.",
                    "  2. Buat BFF mobile dengan satu endpoint yang memanggil kelima",
                    "     layanan dari dalam pusat data, lalu mengirim satu jawaban",
                    "     ringkas:",
                    "       GET /mobile/produk/7?kota=bandung",
                    "       -> {nama, harga, ongkir, stok_tersedia}",
                    "  3. Panggil kelima layanan dari BFF secara paralel dengan timeout",
                    "     per layanan. Kalau layanan ulasan lambat, kirim halaman tanpa",
                    "     ulasan daripada menahan seluruh halaman.",
                    "  4. Tunda service mesh. Dengan lima layanan, gateway dan BFF",
                    "     sudah menyelesaikan masalahnya.",
                ],
            },
        ],
    },
    {
        "title": "39. CI/CD dan Strategi Deployment",
        "sections": [
            {
                "body": [
                    "Cara merilis yang masih sering ditemui di proyek kecil: Jumat",
                    "malam, seseorang menyalin berkas ke server lewat FTP, lalu",
                    "berharap nggak ada yang rusak. Kalau rusak, dia mencoba ingat",
                    "berkas mana saja yang tadi diganti.",
                    "",
                    "Materi ini membahas jalur yang lebih bisa dipercaya. Dari commit",
                    "sampai produksi, kode melewati langkah otomatis yang sama setiap",
                    "kali. Sesudah itu ada cara memasang versi baru tanpa mematikan",
                    "layanan, dan cara mengukur apakah prosesnya membaik.",
                ],
            },
            {
                "heading": "CI, continuous delivery, continuous deployment",
                "body": [
                    "Tiga istilah ini sering disingkat CI/CD dan sering tertukar:",
                    "  - Continuous integration (CI). Setiap anggota tim menggabungkan",
                    "    perubahannya ke cabang utama minimal sekali sehari, dan setiap",
                    "    gabungan diperiksa build dan tes otomatis. Tujuannya menemukan",
                    "    benturan selagi masih kecil.",
                    "  - Continuous delivery. Setiap perubahan yang lolos pemeriksaan",
                    "    selalu dalam keadaan siap dirilis. Merilisnya tinggal menekan",
                    "    satu tombol, dan keputusan kapan menekannya ada di manusia.",
                    "  - Continuous deployment. Selangkah lebih jauh: setiap perubahan",
                    "    yang lolos langsung dipasang ke produksi tanpa tombol.",
                    "",
                    "Artikel Martin Fowler tentang continuous integration, yang",
                    "direvisi tahun 2024, memuat beberapa praktik yang bisa langsung",
                    "kamu pegang. Build harus cukup cepat, idealnya di bawah sepuluh",
                    "menit. Build yang rusak diperbaiki lebih dulu sebelum pekerjaan",
                    "lain.",
                    "",
                    "Pipeline adalah urutan langkah otomatis itu: ambil kode, pasang",
                    "dependensi, jalankan linter dan tes, bangun artefak, lalu",
                    "deploy. Contoh pipeline GitHub Actions paling sederhana untuk",
                    "proyek Python:",
                ],
            },
            {
                "heading": ".github/workflows/ci.yml",
                "bahasa": "yaml",
                "code": """name: ci
on:
  push:
    branches: [main]
  pull_request:

jobs:
  tes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: "3.14"
      - run: python -m unittest discover -s tests""",
            },
            {
                "body": [
                    "Setiap push ke main dan setiap pull request menjalankan tes di",
                    "mesin bersih milik GitHub. Kalau tes gagal, pull request ditandai",
                    "merah dan tim tahu sebelum menggabungkannya. Saat materi ini",
                    "ditulis (Oktober 2026), versi mayor terbaru actions/checkout dan",
                    "actions/setup-python sama-sama v7.",
                    "",
                    "Alat lain mengerjakan hal yang sama dengan berkas konfigurasi",
                    "berbeda: GitLab CI memakai .gitlab-ci.yml, Jenkins (open source,",
                    "MIT) memakai Jenkinsfile. Survei Stack Overflow 2026 nggak",
                    "menanyakan alat CI secara terpisah, tapi GitHub sendiri dipakai",
                    "70% responden sebagai platform komunitas. Detail menulis pipeline",
                    "dibahas di kurikulum DevOps & Cloud.",
                ],
            },
            {
                "heading": "Tiga cara memasang versi baru",
                "body": [
                    "Memasang versi baru tanpa mematikan layanan bisa dilakukan",
                    "dengan tiga cara:",
                    "  - Rolling. Server diganti satu per satu. Selama proses, versi",
                    "    lama dan baru hidup berdampingan. Hemat, tapi rollback juga",
                    "    harus bergulir satu per satu.",
                    "  - Blue-green. Ada dua lingkungan identik. Blue melayani",
                    "    pengguna, green diisi versi baru dan dites. Lalu lalu lintas",
                    "    dipindah sekaligus ke green. Kalau bermasalah, pindahkan",
                    "    kembali ke blue dalam hitungan detik. Bayarannya, kapasitas",
                    "    server dua kali lipat selama peralihan. Fowler menulis pola",
                    "    ini tahun 2010.",
                    "  - Canary. Versi baru diberikan ke sebagian kecil pengguna dulu,",
                    "    misalnya 5%. Kalau error dan latensinya normal, porsinya",
                    "    dinaikkan bertahap. Namanya dari burung kenari yang dulu",
                    "    dibawa ke tambang untuk mendeteksi gas beracun lebih dulu.",
                    "",
                    "Pembagian canary sebaiknya stabil: pengguna yang sama selalu",
                    "mendapat versi yang sama. Kalau dibagi acak per permintaan,",
                    "seseorang bisa melihat tampilan baru, lalu lama, lalu baru lagi.",
                    "Program berikut membagi pengguna ke ember 0 sampai 99 memakai",
                    "hash dari id-nya.",
                ],
            },
            {
                "heading": "Pembagian canary yang stabil",
                "code": "import hashlib\n\n\ndef ember(id_pengguna):\n    \"\"\"Angka 0..99 yang selalu sama untuk pengguna yang sama.\"\"\"\n    return int(hashlib.sha256(id_pengguna.encode()).hexdigest(), 16) % 100\n\n\ndef versi_untuk(id_pengguna, persen_canary):\n    return \"v2 canary\" if ember(id_pengguna) < persen_canary else \"v1\"\n\n\nfor nama in [\"ani\", \"budi\", \"citra\", \"dedi\", \"maya\"]:\n    print(f\"{nama:<6} ember {ember(nama):>2}  10%: {versi_untuk(nama, 10):<9}\"\n          f\"  25%: {versi_untuk(nama, 25)}\")\n\nfor persen in (10, 25):\n    dapat = sum(1 for i in range(10_000) if ember(f\"user-{i}\") < persen)\n    print(f\"canary {persen}%: {dapat} dari 10000 pengguna\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ani    ember 81  10%: v1         25%: v1",
                    "  budi   ember 52  10%: v1         25%: v1",
                    "  citra  ember 10  10%: v1         25%: v2 canary",
                    "  dedi   ember 24  10%: v1         25%: v2 canary",
                    "  maya   ember  1  10%: v2 canary  25%: v2 canary",
                    "  canary 10%: 998 dari 10000 pengguna",
                    "  canary 25%: 2453 dari 10000 pengguna",
                    "",
                    "Maya sudah dapat versi baru di tahap 10%, dan tetap dapat saat",
                    "porsinya naik ke 25%. Citra dan Dedi baru ikut di tahap 25%.",
                    "Nggak ada pengguna yang bolak-balik antar versi. Dari sepuluh",
                    "ribu pengguna, yang kebagian canary mendekati 10% dan 25%, cukup",
                    "dekat untuk dipakai membandingkan error kedua versi.",
                ],
            },
            {
                "heading": "Feature flags dan DORA metrics",
                "body": [
                    "Feature flag adalah saklar di konfigurasi yang menyalakan atau",
                    "mematikan fitur tanpa deploy ulang. Dengannya, deploy (memasang",
                    "kode) dan rilis (membuka fitur ke pengguna) jadi dua kejadian",
                    "terpisah. Kode fitur yang belum jadi boleh ikut ter-deploy",
                    "dalam keadaan mati.",
                    "",
                    "Artikel Pete Hodgson di situs martinfowler.com (2017) membagi",
                    "flag jadi empat jenis menurut tujuannya:",
                    "  - release: menyembunyikan fitur yang belum selesai,",
                    "  - experiment: membandingkan dua versi (uji A/B),",
                    "  - ops: mematikan fitur berat saat sistem kewalahan,",
                    "  - permissioning: membuka fitur untuk kelompok tertentu.",
                    "",
                    "Jebakan: flag yang lupa dibersihkan menumpuk jadi utang teknis.",
                    "Kode penuh cabang if untuk flag yang sudah setahun menyala",
                    "susah dibaca dan susah dites. Beri tiap flag rilis tanggal",
                    "kedaluwarsa.",
                    "",
                    "Lalu bagaimana tahu prosesmu membaik? Riset DORA menghasilkan",
                    "ukuran yang sekarang berjumlah lima (dulu empat):",
                    "  - change lead time: dari commit sampai berjalan di produksi,",
                    "  - deployment frequency: seberapa sering deploy ke produksi,",
                    "  - failed deployment recovery time: lama pulih dari deploy",
                    "    yang gagal,",
                    "  - change fail rate: persentase deploy yang menimbulkan masalah,",
                    "  - deployment rework rate: persentase deploy yang nggak",
                    "    direncanakan, dilakukan untuk menambal masalah di produksi.",
                    "",
                    "Dua yang pertama mengukur kecepatan, tiga sisanya mengukur",
                    "stabilitas. Tim yang bagus menaikkan keduanya bersamaan. Deploy",
                    "yang sering membuat tiap perubahan lebih kecil, jadi lebih",
                    "gampang diperiksa dan dipulihkan kalau salah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi web dan aplikasi HP besar merilis perubahan berkali-kali",
                    "sehari lewat pipeline, dan fitur baru biasanya muncul bertahap",
                    "ke sebagian pengguna dulu. Karena itu dua temanmu kadang melihat",
                    "tampilan berbeda di aplikasi yang sama.",
                    "",
                    "Kasus kecil: tim kecil sebuah koperasi digital merilis sebulan",
                    "sekali dengan menyalin berkas ke server. Setiap rilis menimbulkan",
                    "error yang baru ketahuan besoknya, dan rollback butuh setengah",
                    "hari.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang CI dulu: setiap pull request menjalankan tes otomatis,",
                    "     dan cabang utama nggak boleh menerima kode yang merah.",
                    "  2. Bangun artefak sekali (misalnya image kontainer bertanda",
                    "     versi), lalu pakai artefak yang sama untuk staging dan",
                    "     produksi.",
                    "  3. Pakai blue-green: siapkan lingkungan kedua, tes di sana,",
                    "     lalu pindahkan lalu lintas. Rollback cukup memindahkan",
                    "     kembali.",
                    "  4. Sembunyikan fitur yang belum selesai di balik flag, supaya",
                    "     rilis bisa sering tanpa menunggu semua fitur rampung:",
                    "       if flag_aktif(\"simpanan_berjangka\", pengguna):",
                    "           tampilkan_menu_simpanan_berjangka()",
                    "  5. Catat change lead time dan failed deployment recovery time",
                    "     tiap bulan supaya perbaikannya kelihatan dalam angka.",
                ],
            },
        ],
    },
    {
        "title": "40. Twelve-Factor App, IaC, dan GitOps",
        "sections": [
            {
                "body": [
                    "\"Di laptopku jalan kok.\" Kalimat ini muncul kalau aplikasi",
                    "bergantung pada hal yang cuma ada di satu mesin. Misalnya versi",
                    "pustaka yang kebetulan terpasang, berkas konfigurasi yang nggak",
                    "ikut repositori, atau server yang disetel tangan bertahun-tahun",
                    "lalu dan nggak ada yang ingat caranya.",
                    "",
                    "Materi ini membahas tiga kebiasaan yang mencegahnya.",
                    "Twelve-Factor App mengatur cara aplikasi ditulis.",
                    "Infrastructure as Code mengatur cara server dibuat. GitOps",
                    "mengatur cara keduanya dipasang.",
                ],
            },
            {
                "heading": "Dua belas faktor",
                "body": [
                    "Twelve-Factor App ditulis Adam Wiggins, salah satu pendiri",
                    "Heroku, tahun 2011. Isinya dua belas prinsip untuk aplikasi",
                    "yang gampang di-deploy dan diperbanyak:",
                    "  1. Codebase: satu repositori untuk satu aplikasi, di-deploy ke",
                    "     banyak lingkungan.",
                    "  2. Dependencies: semua dependensi dideklarasikan, jangan",
                    "     mengandalkan yang kebetulan terpasang.",
                    "  3. Config: konfigurasi disimpan di environment, di luar kode.",
                    "  4. Backing services: database, cache, dan email diperlakukan",
                    "     sebagai sumber daya yang dipasang lewat alamat.",
                    "  5. Build, release, run: tiga tahap yang dipisah tegas.",
                    "  6. Processes: proses aplikasi stateless.",
                    "  7. Port binding: aplikasi melayani lewat port miliknya sendiri.",
                    "  8. Concurrency: diperbanyak dengan menambah proses.",
                    "  9. Disposability: cepat dinyalakan, rapi saat dimatikan.",
                    "  10. Dev/prod parity: lingkungan pengembangan semirip mungkin",
                    "      dengan produksi.",
                    "  11. Logs: log ditulis sebagai aliran ke stdout.",
                    "  12. Admin processes: tugas admin dijalankan sebagai proses",
                    "      sekali jalan.",
                    "",
                    "Situs 12factor.net masih bertuliskan pembaruan terakhir 2017.",
                    "Tanggal 12 November 2024 dokumennya dibuka sebagai proyek open",
                    "source berlisensi CC BY 4.0, dan komunitas sedang menyusun",
                    "revisinya. Prinsip-prinsipnya tetap jadi dasar cara aplikasi",
                    "dijalankan di Docker, Kubernetes, dan platform cloud.",
                ],
            },
            {
                "heading": "Konfigurasi dari environment",
                "code": """import os

# Konfigurasi dibaca dari environment, dengan nilai bawaan untuk laptop.
DB_URL = os.environ.get("TOKO_DB_URL", "sqlite:///toko-dev.db")
DEBUG = os.environ.get("TOKO_DEBUG", "1") == "1"
PORT = int(os.environ.get("TOKO_PORT", "8000"))

print("database:", DB_URL)
print("debug   :", DEBUG)
print("port    :", PORT)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  database: sqlite:///toko-dev.db",
                    "  debug   : True",
                    "  port    : 8000",
                    "",
                    "Di laptopmu, nilai bawaannya yang terpakai. Di server produksi,",
                    "variabel environment untuk alamat database diisi alamat",
                    "sungguhan, dan variabel debug diisi 0. Kodenya persis sama, yang",
                    "berbeda cuma lingkungannya. Itu inti faktor ketiga.",
                    "",
                    "Jebakan: kata sandi database jangan pernah ditulis di kode atau",
                    "di-commit ke Git. Riwayat Git menyimpannya selamanya, walau",
                    "barisnya sudah dihapus di commit berikutnya. Berkas .env boleh",
                    "dipakai di laptop, tapi masukkan ke .gitignore. Di produksi,",
                    "rahasia disimpan di pengelola rahasia milik platform.",
                ],
            },
            {
                "heading": "Infrastructure as Code",
                "body": [
                    "Infrastructure as Code (IaC) artinya server, jaringan, dan",
                    "layanan cloud ditulis sebagai berkas kode, disimpan di Git, lalu",
                    "dibuat atau diubah oleh alat. Lingkungan staging dan produksi",
                    "bisa dibuat identik, dan setiap perubahan infrastruktur punya",
                    "riwayat dan bisa di-review seperti kode biasa.",
                    "",
                    "  alat         gaya                             lisensi",
                    "  Terraform    deklaratif, bahasa HCL            BUSL (sejak 2023)",
                    "  OpenTofu     fork Terraform, bahasa HCL        MPL-2.0",
                    "  Ansible      mengatur isi server lewat SSH     GPL-3.0",
                    "  Pulumi       pakai Python, TypeScript, Go      Apache-2.0",
                    "  Helm         paket aplikasi untuk Kubernetes   Apache-2.0",
                    "",
                    "Terraform paling banyak dipakai. Agustus 2023, mulai versi 1.6,",
                    "HashiCorp mengganti lisensinya ke BUSL, yang menurut OSI nggak",
                    "termasuk lisensi open source. Sebagai tanggapan, komunitas",
                    "membuat OpenTofu di bawah Linux Foundation, dengan bahasa dan",
                    "perintah yang hampir sama. HashiCorp sendiri sekarang milik IBM.",
                    "Survei Stack Overflow 2026 mencatat Terraform dipakai 18%",
                    "responden, Ansible dan Helm masing-masing 12%, OpenTofu 4%, dan",
                    "Pulumi 2%.",
                    "",
                    "Contoh berkas HCL yang meminta satu bucket penyimpanan di region",
                    "AWS Jakarta:",
                ],
            },
            {
                "heading": "main.tf",
                "bahasa": "hcl",
                "code": """provider "aws" {
  region = "ap-southeast-3"
}

resource "aws_s3_bucket" "foto_produk" {
  bucket = "toko-melati-foto-produk"
}""",
            },
            {
                "body": [
                    "Berkas itu menulis keadaan yang diinginkan, bukan langkah-langkah",
                    "membuatnya. Alurnya selalu tiga perintah:",
                    "  tofu init    unduh plugin penyedia (provider)",
                    "  tofu plan    tunjukkan apa yang akan dibuat, diubah, dihapus",
                    "  tofu apply   jalankan rencananya",
                    "",
                    "Dengan Terraform, ganti tofu dengan terraform. Inti dari plan",
                    "adalah membandingkan keadaan yang diinginkan dengan keadaan",
                    "nyata, lalu menyusun daftar perbedaannya. Program berikut",
                    "meniru langkah itu dengan dua dict.",
                ],
            },
            {
                "heading": "Rencana dari dua keadaan",
                "code": """# Inti "terraform plan": bandingkan keadaan yang diinginkan dengan yang nyata.
diinginkan = {
    "server-web-1": {"ukuran": "kecil", "zona": "a"},
    "server-web-2": {"ukuran": "kecil", "zona": "b"},
    "database": {"ukuran": "besar", "zona": "a"},
}
nyata = {
    "server-web-1": {"ukuran": "kecil", "zona": "a"},
    "database": {"ukuran": "sedang", "zona": "a"},
    "server-coba": {"ukuran": "kecil", "zona": "a"},
}

rencana = []
for nama in sorted(diinginkan.keys() | nyata.keys()):
    mau, ada = diinginkan.get(nama), nyata.get(nama)
    if ada is None:
        rencana.append(f"+ buat   {nama} {mau}")
    elif mau is None:
        rencana.append(f"- hapus  {nama}")
    elif mau != ada:
        beda = {k: f"{ada.get(k)} -> {v}" for k, v in mau.items() if ada.get(k) != v}
        rencana.append(f"~ ubah   {nama} {beda}")

for baris in rencana:
    print(baris)
if not rencana:
    print("Tidak ada perubahan.")
print(f"Rencana: {sum(r[0] == '+' for r in rencana)} dibuat, "
      f"{sum(r[0] == '~' for r in rencana)} diubah, "
      f"{sum(r[0] == '-' for r in rencana)} dihapus.")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ~ ubah   database {'ukuran': 'sedang -> besar'}",
                    "  - hapus  server-coba",
                    "  + buat   server-web-2 {'ukuran': 'kecil', 'zona': 'b'}",
                    "  Rencana: 1 dibuat, 1 diubah, 1 dihapus.",
                    "",
                    "Server-coba yang dulu dibuat tangan dan dilupakan ketahuan dan",
                    "dijadwalkan dihapus. Itu salah satu manfaat IaC: semua yang",
                    "nggak tertulis di kode dianggap asing. Selalu baca rencananya",
                    "sebelum apply. Tanda minus di depan database produksi adalah",
                    "hal terakhir yang ingin kamu lewatkan.",
                ],
            },
            {
                "heading": "GitOps",
                "body": [
                    "GitOps membawa ide yang sama ke proses deploy. Keadaan sistem",
                    "yang diinginkan, misalnya versi aplikasi dan jumlah replikanya",
                    "di Kubernetes, disimpan di repositori Git. Sebuah agen di dalam",
                    "klaster terus membandingkan isi Git dengan keadaan nyata, lalu",
                    "menyamakannya. Mau deploy versi baru? Ubah nomor versinya lewat",
                    "pull request. Mau rollback? Revert commit-nya.",
                    "",
                    "Bedanya dengan pipeline CI biasa ada di arah perintahnya. Di",
                    "pipeline biasa, CI mendorong (push) perubahan ke server. Di",
                    "GitOps, agen di klaster menarik (pull) dari Git, jadi kunci",
                    "akses klaster nggak perlu disimpan di sistem CI.",
                    "",
                    "Dua alat utamanya sama-sama proyek CNCF berlisensi Apache-2.0:",
                    "  - Argo CD, versi terbaru saat materi ini ditulis v3.5.5,",
                    "    lengkap dengan dasbor web.",
                    "  - Flux, versi v2.9.6. Perusahaan pendirinya, Weaveworks, tutup",
                    "    Februari 2024, dan proyeknya diteruskan pemelihara dari",
                    "    vendor lain.",
                    "",
                    "Survei CNCF 2025 mencatat 58% organisasi yang tergolong",
                    "\"cloud native innovators\" sudah memakai GitOps secara luas,",
                    "dibanding 23% pada kelompok \"adopters\". Cara memakainya",
                    "dibahas di kurikulum DevOps & Cloud.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang memakai cloud biasanya menyimpan seluruh",
                    "infrastrukturnya sebagai berkas Terraform atau OpenTofu di satu",
                    "repositori, dan setiap perubahan lewat pull request yang",
                    "menampilkan hasil plan. Aplikasi di Kubernetes sering dipasang",
                    "lewat Argo CD atau Flux.",
                    "",
                    "Kasus kecil: aplikasi sekolah berjalan di satu VPS yang disetel",
                    "tangan oleh alumni yang sudah lulus. Server perlu dipindah ke",
                    "penyedia lain, dan nggak ada yang tahu paket apa saja yang",
                    "terpasang atau di mana kata sandi database disimpan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Periksa aplikasinya terhadap dua belas faktor. Cari",
                    "     konfigurasi dan kata sandi yang tertulis di kode, lalu",
                    "     pindahkan ke environment.",
                    "  2. Tulis server barunya sebagai kode: OpenTofu untuk membuat",
                    "     VPS dan firewall, Ansible untuk memasang paketnya.",
                    "  3. Jalankan plan, baca hasilnya bersama satu orang lain, baru",
                    "     apply:",
                    "       tofu plan -out=rencana",
                    "       tofu apply rencana",
                    "  4. Simpan semua berkas di Git. Kalau server ini rusak lagi,",
                    "     server pengganti bisa dibuat ulang dari repositori yang sama.",
                ],
            },
        ],
    },
    {
        "title": "41. Observability, SLO, dan Budaya SRE",
        "sections": [
            {
                "body": [
                    "Pukul dua pagi, pelanggan mengeluh checkout lambat. Monitoring",
                    "biasa bisa memberi tahu bahwa ada masalah: grafik latensi naik,",
                    "alarm berbunyi. Observability menjawab pertanyaan berikutnya:",
                    "kenapa, di layanan mana, dan untuk permintaan yang mana.",
                    "",
                    "Observability adalah kemampuan memahami apa yang terjadi di",
                    "dalam sistem cuma dari data yang dikeluarkannya. Materi ini",
                    "membahas data itu, lalu cara menentukan seberapa andal sistem",
                    "harus dibuat, dan kebiasaan tim yang menjaganya.",
                ],
            },
            {
                "heading": "Tiga sinyal",
                "body": [
                    "Data observability biasanya dibagi tiga:",
                    "  - Log: catatan kejadian satu per satu. \"Pembayaran pesanan",
                    "    881 gagal: saldo kurang.\"",
                    "  - Metrik: angka yang diukur sepanjang waktu. Jumlah permintaan",
                    "    per detik, persentase error, pemakaian memori.",
                    "  - Trace: jejak satu permintaan saat melewati banyak layanan,",
                    "    lengkap dengan lama tiap langkahnya.",
                    "",
                    "Metrik bagus untuk alarm, karena murah disimpan dan gampang",
                    "digambar. Log bagus untuk detail satu kejadian. Trace menjawab",
                    "\"waktu tiga detik ini habis di mana?\" saat satu klik melewati",
                    "lima layanan.",
                    "",
                    "Supaya log bisa dicari dan disaring mesin, tulis sebagai log",
                    "terstruktur: satu baris JSON per kejadian, dengan kolom yang",
                    "tetap. Sertakan trace id, yaitu penanda unik satu permintaan",
                    "yang diteruskan dari layanan ke layanan.",
                ],
            },
            {
                "heading": "Log terstruktur dengan trace id",
                "code": """import json

catatan = []   # di produksi baris-baris ini dikirim ke stdout lalu dikumpulkan


def log(trace_id, layanan, pesan, **data):
    baris = {"trace": trace_id, "layanan": layanan, "pesan": pesan, **data}
    catatan.append(json.dumps(baris, separators=(",", ":")))


def layanan_ongkir(trace_id, kota):
    log(trace_id, "ongkir", "hitung", kota=kota, ms=420)
    return 12000


def checkout(trace_id, pembeli):
    log(trace_id, "checkout", "mulai", pembeli=pembeli)
    biaya = layanan_ongkir(trace_id, "bogor")
    log(trace_id, "checkout", "selesai", total=85000 + biaya)


checkout("a1f3", "ani")
checkout("b7c9", "budi")

# Mencari semua jejak satu permintaan: saring menurut trace_id.
for baris in catatan:
    data = json.loads(baris)
    if data["trace"] == "a1f3":
        print(baris)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  {\"trace\":\"a1f3\",\"layanan\":\"checkout\",\"pesan\":\"mulai\",\"pembeli\":\"ani\"}",
                    "  {\"trace\":\"a1f3\",\"layanan\":\"ongkir\",\"pesan\":\"hitung\",\"kota\":\"bogor\",\"ms\":420}",
                    "  {\"trace\":\"a1f3\",\"layanan\":\"checkout\",\"pesan\":\"selesai\",\"total\":97000}",
                    "",
                    "Ada enam baris log, tiga milik Ani dan tiga milik Budi. Dengan",
                    "menyaring trace a1f3, ketiga langkah permintaan Ani terkumpul,",
                    "padahal dua di antaranya ditulis layanan yang berbeda. Di",
                    "produksi, pencarian seperti ini dilakukan alat pengumpul log,",
                    "bukan perulangan Python.",
                    "",
                    "Jebakan: jangan pernah menulis kata sandi, token, atau nomor",
                    "kartu ke log. Log disalin ke banyak tempat dan dibaca banyak",
                    "orang, jadi data rahasia di sana sama saja dengan bocor.",
                ],
            },
            {
                "heading": "OpenTelemetry",
                "body": [
                    "Dulu tiap alat pemantauan punya pustaka sendiri, dan pindah alat",
                    "berarti mengganti kode di semua layanan. OpenTelemetry adalah",
                    "standar terbuka untuk menghasilkan dan mengirim ketiga sinyal",
                    "itu. Kode cukup memakai API OpenTelemetry, lalu datanya bisa",
                    "dikirim ke alat apa pun yang menerimanya.",
                    "",
                    "OpenTelemetry proyek CNCF berlisensi Apache-2.0, dan menurut",
                    "CNCF kecepatan kontribusinya tertinggi kedua sesudah Kubernetes.",
                    "Spesifikasi terbarunya saat materi ini ditulis adalah versi",
                    "1.61.0 (14 September 2026). Contoh membuat trace di Python:",
                ],
            },
            {
                "heading": "Dua span dalam satu trace",
                "code": """from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

penyedia = TracerProvider()
penyedia.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(penyedia)
tracer = trace.get_tracer("toko.checkout")


def hitung_ongkir(keranjang):
    with tracer.start_as_current_span("hitung_ongkir"):
        return 12000


def checkout(keranjang):
    with tracer.start_as_current_span("checkout") as span:
        span.set_attribute("keranjang.jumlah_barang", len(keranjang))
        return hitung_ongkir(keranjang)


checkout(["kopi", "gula"])""",
            },
            {
                "body": [
                    "Contoh ini butuh paket opentelemetry-api dan opentelemetry-sdk.",
                    "Span adalah satu langkah di dalam trace. Saat dijalankan, kedua",
                    "span dicetak sebagai JSON dengan trace_id yang sama, dan span",
                    "hitung_ongkir mencatat checkout sebagai induknya. Di produksi,",
                    "ConsoleSpanExporter diganti pengirim ke kolektor.",
                    "",
                    "Data itu lalu ditampung di backend pemantauan. Prometheus (versi",
                    "3.15.0) menyimpan metrik dan biasanya dipasangkan dengan Grafana",
                    "untuk dasbor. Jaeger menampilkan trace. Sentry, Datadog, dan New",
                    "Relic adalah layanan siap pakai. Di survei Stack Overflow 2026,",
                    "Sentry dipakai 14% responden, Datadog 11%, dan New Relic 4%.",
                    "Prometheus tercatat 11,8% di survei 2025. Cara memasangnya ada",
                    "di kurikulum DevOps & Cloud.",
                ],
            },
            {
                "heading": "SLI, SLO, dan SLA",
                "body": [
                    "Seberapa andal sistem harus dibuat? Buku Site Reliability",
                    "Engineering dari Google, yang bisa dibaca gratis di sre.google,",
                    "memakai tiga istilah:",
                    "  - SLI (service level indicator): angka yang diukur. Misalnya",
                    "    persentase permintaan yang sukses, atau persentase permintaan",
                    "    yang selesai di bawah 300 ms.",
                    "  - SLO (service level objective): target untuk angka itu.",
                    "    \"99,9% permintaan sukses dalam 30 hari.\"",
                    "  - SLA (service level agreement): janji tertulis ke pelanggan",
                    "    beserta sanksinya, misalnya potongan biaya. SLA biasanya lebih",
                    "    longgar dari SLO, supaya tim sempat bereaksi sebelum janjinya",
                    "    dilanggar.",
                    "",
                    "Untuk memilih apa yang dipantau, buku itu menyarankan empat",
                    "sinyal emas: latensi, lalu lintas, error, dan saturasi (seberapa",
                    "penuh sumber dayanya). Latensi sebaiknya diukur dengan persentil",
                    "seperti p99, karena rata-rata menyembunyikan pengguna yang paling",
                    "menderita.",
                    "",
                    "Satu angka di belakang koma membuat beda besar. Waktu henti yang",
                    "diizinkan dalam 30 hari:",
                    "",
                    "  SLO       waktu henti per 30 hari",
                    "  99%       7 jam 12 menit",
                    "  99,5%     3 jam 36 menit",
                    "  99,9%     43 menit 12 detik",
                    "  99,95%    21 menit 36 detik",
                    "  99,99%    4 menit 19 detik",
                    "",
                    "Target 100% hampir selalu keliru. Setiap angka sembilan",
                    "tambahan jauh lebih mahal, dan ada batas yang bisa dirasakan",
                    "pengguna. Buku SRE memberi contoh: pengguna yang ponselnya",
                    "andal 99% nggak bisa membedakan layanan 99,99% dari 99,999%.",
                ],
            },
            {
                "heading": "Error budget dan postmortem",
                "body": [
                    "Kalau SLO-nya 99,9%, berarti 0,1% kegagalan boleh terjadi. Jatah",
                    "itu disebut error budget. Selama jatahnya masih ada, tim boleh",
                    "merilis fitur dengan cepat. Kalau jatahnya habis, tim berhenti",
                    "merilis fitur dan memperbaiki keandalan dulu. Dengan begitu,",
                    "perdebatan \"cepat atau stabil\" diputuskan oleh angka.",
                    "",
                    "Burn rate adalah seberapa cepat jatah itu dihabiskan. Burn rate",
                    "1 berarti jatah habis tepat di akhir periode. Burn rate 10",
                    "berarti jatah sebulan habis dalam tiga hari, dan itu alasan yang",
                    "bagus untuk membangunkan orang.",
                    "",
                    "Ingat: setiap alarm yang membangunkan engineer jaga (on-call)",
                    "harus bisa ditindaklanjuti. Alarm yang sering berbunyi tanpa",
                    "tindakan membuat orang terbiasa mengabaikannya.",
                    "",
                    "Sesudah insiden, tim menulis postmortem tanpa menyalahkan",
                    "(blameless). Isinya dampak, kronologi, akar masalah, dan",
                    "tindakan perbaikan, tanpa menunjuk siapa yang salah ketik. Buku",
                    "SRE Google menyebut budaya ini dipinjam dari dunia kesehatan dan",
                    "penerbangan. Alasannya: orang yang takut disalahkan cenderung",
                    "menyembunyikan informasi yang justru paling dibutuhkan untuk",
                    "mencegah kejadian berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan cloud besar menerbitkan SLA berisi persentase",
                    "ketersediaan dan kompensasi kalau janjinya dilanggar. Tim di",
                    "balik aplikasi pembayaran dan marketplace biasanya punya dasbor",
                    "empat sinyal emas dan jadwal on-call bergiliran.",
                    "",
                    "Kasus kecil: aplikasi ujian online sekolah sering dikeluhkan",
                    "lambat saat ujian serentak, tapi tim baru tahu dari grup",
                    "WhatsApp guru. Nggak ada yang tahu seberapa sering itu terjadi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pilih SLI yang dirasakan siswa: persentase permintaan kirim",
                    "     jawaban yang sukses dan selesai di bawah satu detik.",
                    "  2. Sepakati SLO dengan pihak sekolah, misalnya 99,5% selama",
                    "     jam ujian. Itu berarti 5 dari setiap 1.000 permintaan boleh",
                    "     gagal atau lambat.",
                    "  3. Tambahkan trace id dan log terstruktur di setiap layanan,",
                    "     supaya permintaan yang lambat bisa ditelusuri:",
                    "       {\"trace\":\"c9e2\",\"layanan\":\"jawaban\",\"ms\":2300}",
                    "  4. Pasang alarm berdasarkan burn rate, bukan setiap error",
                    "     tunggal, lalu tulis postmortem tanpa menyalahkan untuk setiap",
                    "     kejadian yang menghabiskan jatah error.",
                ],
            },
        ],
    },
    {
        "title": "42. Identitas dan Rantai Pasok dalam Arsitektur",
        "sections": [
            {
                "body": [
                    "Ada dua hal yang sering lupa digambar di diagram arsitektur.",
                    "Pertama, identitas: bagaimana setiap layanan tahu siapa yang",
                    "sedang memanggilnya. Kedua, rantai pasok: kode yang nggak kamu",
                    "tulis sendiri tapi ikut berjalan di aplikasimu, yaitu semua",
                    "pustaka dan alat build.",
                    "",
                    "Dua-duanya punya ranah sendiri. Serangan, kriptografi, dan",
                    "daftar risiko OWASP Top 10:2025 dibahas tuntas di kurikulum",
                    "Keamanan Siber. Materi ini membahas letak keduanya di gambar",
                    "arsitektur dan keputusan yang harus kamu ambil di sana.",
                ],
            },
            {
                "heading": "Sesi atau token",
                "body": [
                    "Sesudah login, aplikasi perlu mengenali pengguna di setiap",
                    "permintaan berikutnya. Ada dua cara utama:",
                    "  - Sesi di server. Server menyimpan data login di memori atau",
                    "    database, lalu memberi browser cookie berisi id sesi. Kalau",
                    "    servernya banyak, sesi harus disimpan di tempat bersama",
                    "    seperti Redis, karena server aplikasi harus stateless (bab",
                    "    System Design: Skala, Lalu Lintas, dan Cache).",
                    "  - Token yang dibawa klien. Server memberi token bertanda",
                    "    tangan, biasanya berformat JWT (JSON Web Token), berisi siapa",
                    "    penggunanya dan kapan kedaluwarsa. Server mana pun bisa",
                    "    memeriksa tanda tangannya tanpa bertanya ke database.",
                    "",
                    "Program berikut membuat dan memeriksa JWT dengan pustaka standar",
                    "Python. Waktunya jam palsu supaya hasilnya selalu sama.",
                ],
            },
            {
                "heading": "JWT buatan sendiri dengan HMAC",
                "code": """import base64
import hashlib
import hmac
import json

RAHASIA = b"rahasia-contoh-yang-di-produksi-diambil-dari-env"


def b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def dari_b64(teks):
    return base64.urlsafe_b64decode(teks + "=" * (-len(teks) % 4))


def tanda_tangan(kepala, badan):
    return b64(hmac.new(RAHASIA, f"{kepala}.{badan}".encode(), hashlib.sha256).digest())


def buat_token(isi):
    kepala = b64(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    badan = b64(json.dumps(isi).encode())
    return f"{kepala}.{badan}.{tanda_tangan(kepala, badan)}"


def periksa(token, sekarang):
    kepala, badan, tanda = token.split(".")
    if not hmac.compare_digest(tanda, tanda_tangan(kepala, badan)):
        return "ditolak: tanda tangan tidak cocok"
    isi = json.loads(dari_b64(badan))
    if sekarang >= isi["exp"]:
        return "ditolak: sudah kedaluwarsa"
    return f"sah, pengguna {isi['sub']} dengan peran {isi['peran']}"


token = buat_token({"sub": "ani", "peran": "siswa", "exp": 1000})
kepala, badan, tanda = token.split(".")
print("isi   :", dari_b64(badan).decode())
print("t=900 :", periksa(token, 900))
print("t=1000:", periksa(token, 1000))

# Penyerang mengubah peran jadi admin tanpa tahu rahasianya.
badan_palsu = b64(json.dumps({"sub": "ani", "peran": "admin", "exp": 1000}).encode())
print("palsu :", periksa(f"{kepala}.{badan_palsu}.{tanda}", 900))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  isi   : {\"sub\": \"ani\", \"peran\": \"siswa\", \"exp\": 1000}",
                    "  t=900 : sah, pengguna ani dengan peran siswa",
                    "  t=1000: ditolak: sudah kedaluwarsa",
                    "  palsu : ditolak: tanda tangan tidak cocok",
                    "",
                    "Baris pertama penting: isi JWT cuma dikodekan base64, nggak",
                    "dienkripsi. Siapa pun yang memegang tokennya bisa membaca isinya,",
                    "jadi jangan taruh data rahasia di sana. Yang dijamin cuma",
                    "keasliannya. Begitu satu huruf isinya diubah, tanda tangannya",
                    "nggak cocok lagi, seperti baris terakhir.",
                    "",
                    "Kelemahan utama JWT: token yang sudah diberikan nggak bisa",
                    "dicabut sebelum kedaluwarsa, kecuali kamu menyimpan daftar",
                    "blokir, dan daftar itu membawa kembali penyimpanan bersama yang",
                    "tadinya mau dihindari. Karena itu masa berlaku token dibuat",
                    "pendek, misalnya lima belas menit, lalu diperbarui dengan",
                    "refresh token.",
                    "",
                    "Jebakan: menyimpan token di localStorage membuatnya bisa dibaca",
                    "skrip apa pun di halaman, termasuk skrip sisipan penyerang",
                    "(XSS). Cookie HttpOnly nggak bisa dibaca JavaScript. Di proyek",
                    "sungguhan, pakai pustaka JWT yang sudah teruji dan tetapkan",
                    "algoritma yang diterima, jangan menulis sendiri seperti contoh",
                    "ini.",
                ],
            },
            {
                "heading": "OAuth 2.0, OpenID Connect, dan SSO",
                "body": [
                    "OAuth 2.0 adalah standar untuk memberi izin akses. Aplikasi",
                    "cetak foto, misalnya, minta izin membaca album Google Photos-mu",
                    "tanpa pernah tahu kata sandi Google-mu. Yang diberikan cuma",
                    "access token dengan izin terbatas.",
                    "",
                    "OAuth sendiri nggak menjelaskan siapa penggunanya. OpenID",
                    "Connect (OIDC) menambahkan lapisan identitas di atasnya: selain",
                    "access token, aplikasi menerima ID token berformat JWT yang",
                    "berisi siapa yang login. Tombol \"Masuk dengan Google\" memakai",
                    "OIDC. Aplikasi di HP dan aplikasi satu halaman memakai tambahan",
                    "PKCE supaya kode otorisasinya nggak bisa dicuri di tengah jalan.",
                    "",
                    "Single sign-on (SSO) berarti login sekali untuk banyak aplikasi,",
                    "misalnya satu akun kantor untuk email, wiki, dan aplikasi HR.",
                    "Menurut oauth.net, OAuth 2.1, yang merapikan praktik terbaik",
                    "OAuth 2.0, masih dalam penyusunan.",
                    "",
                    "Penyedia identitas adalah server yang mengurus semua itu, jadi",
                    "aplikasimu nggak perlu menyimpan kata sandi sendiri:",
                    "  - Keycloak: open source (Apache-2.0), dipasang di servermu",
                    "    sendiri. Versi terbaru saat materi ini ditulis 26.8.1, yang",
                    "    menambal 23 celah keamanan.",
                    "  - Auth0 dan Okta: layanan siap pakai. Auth0 sudah dimiliki Okta",
                    "    sejak 2021.",
                    "  - Microsoft Entra ID, untuk organisasi yang memakai Microsoft",
                    "    365.",
                    "",
                    "Di survei Stack Overflow 2026, di antara 4.052 responden yang",
                    "menjawab pertanyaan alat operasi keamanan, Auth0 dipakai 30%,",
                    "Okta 29%, dan Keycloak 19%.",
                ],
            },
            {
                "heading": "Rantai pasok perangkat lunak",
                "body": [
                    "Aplikasi web biasa bisa membawa ratusan paket pihak ketiga,",
                    "kebanyakan tanpa kamu sadari karena ikut terpasang sebagai",
                    "dependensi dari dependensi. Dua kejadian yang sering dikutip:",
                    "  - 2016, paket npm kecil bernama left-pad ditarik pembuatnya,",
                    "    dan build ribuan proyek mendadak gagal.",
                    "  - 2024, ditemukan pintu belakang di xz-utils, pustaka kompresi",
                    "    yang ada di hampir semua distro Linux. Penyusupnya sudah",
                    "    bertahun-tahun ikut merawat proyek itu sebelum menyisipkan",
                    "    kodenya.",
                    "",
                    "Pertahanannya berlapis:",
                    "  - Lockfile, misalnya package-lock.json, uv.lock, Cargo.lock,",
                    "    atau composer.lock, mengunci versi persis setiap paket.",
                    "    Commit berkas itu, lalu pasang dengan perintah yang patuh",
                    "    pada lockfile, seperti npm ci, supaya build hari ini dan",
                    "    besok memakai isi yang sama.",
                    "  - SBOM (software bill of materials) adalah daftar bahan",
                    "    perangkat lunakmu. Dua format bakunya CycloneDX dan SPDX.",
                    "    Saat celah baru diumumkan, SBOM menjawab \"kita kena atau",
                    "    nggak?\" dalam hitungan menit.",
                    "  - SLSA, yang spesifikasinya kini versi 1.2, adalah kerangka",
                    "    untuk memastikan artefak build nggak diubah di tengah jalan",
                    "    antara kode sumber dan server produksi.",
                    "  - Dependabot (bawaan GitHub) dan Renovate membuka pull request",
                    "    otomatis saat ada versi baru atau celah keamanan.",
                    "",
                    "Contoh konfigurasi Dependabot untuk proyek Python:",
                ],
            },
            {
                "heading": ".github/dependabot.yml",
                "bahasa": "yaml",
                "code": "version: 2\nupdates:\n  - package-ecosystem: \"pip\"\n    directory: \"/\"\n    schedule:\n      interval: \"weekly\"",
            },
            {
                "heading": "Keamanan di setiap tahap",
                "body": [
                    "Secure SDLC artinya keamanan dimasukkan ke setiap tahap",
                    "pengembangan, bukan diperiksa sekali sebelum rilis. Bentuk",
                    "nyatanya di arsitektur:",
                    "  - saat merancang: daftar ancaman untuk tiap batas kepercayaan,",
                    "    misalnya di antara internet dan gateway,",
                    "  - saat menulis kode: code review dan analisis statis seperti",
                    "    CodeQL, Semgrep, atau Snyk Code,",
                    "  - saat build: pemindaian dependensi dan pemindaian rahasia yang",
                    "    nggak sengaja ter-commit,",
                    "  - saat berjalan: log keamanan dan pembaruan rutin.",
                    "",
                    "Aplikasi tempat kamu belajar ini sengaja tanpa dependensi pihak",
                    "ketiga di sisi server. Rantai pasoknya cuma Python dan pustaka",
                    "standarnya, jadi permukaan serangannya kecil. Itu satu contoh",
                    "keputusan arsitektur yang ikut menentukan keamanan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Portal kampus dan kantor biasanya memakai SSO, jadi satu akun",
                    "membuka email, LMS, dan sistem akademik. Proyek di GitHub banyak",
                    "yang menerima pull request otomatis dari Dependabot setiap",
                    "pekan, dan perusahaan yang menjual perangkat lunak ke pemerintah",
                    "atau bank makin sering diminta melampirkan SBOM.",
                    "",
                    "Kasus kecil: sebuah yayasan punya tiga aplikasi web (PPDB,",
                    "perpustakaan, dan keuangan) dengan tiga tabel pengguna terpisah.",
                    "Guru harus mengingat tiga kata sandi, dan akun guru yang sudah",
                    "pindah kerja sering lupa dinonaktifkan di salah satunya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang satu penyedia identitas, misalnya Keycloak di server",
                    "     yayasan, sebagai satu-satunya tempat kata sandi disimpan.",
                    "  2. Ubah ketiga aplikasi jadi klien OIDC. Aplikasi menerima ID",
                    "     token, lalu membuat sesinya sendiri:",
                    "       pengguna = verifikasi_id_token(token, penerbit, klien_id)",
                    "       sesi[\"user\"] = pengguna[\"sub\"]",
                    "  3. Atur peran (guru, staf keuangan, admin) di penyedia",
                    "     identitas, dan biarkan tiap aplikasi membaca perannya dari",
                    "     token.",
                    "  4. Saat ada guru pindah kerja, cukup nonaktifkan satu akun di",
                    "     Keycloak. Ketiga aplikasi otomatis menolaknya begitu",
                    "     sesinya habis.",
                ],
            },
        ],
    },
    {
        "title": "43. ADR, C4 Model, dan Dokumentasi Arsitektur",
        "sections": [
            {
                "body": [
                    "Setahun sesudah sebuah aplikasi jadi, anggota tim baru biasanya",
                    "bertanya hal yang sama. Kenapa pakai PostgreSQL, bukan MongoDB?",
                    "Kenapa masih monolit? Kenapa ada dua layanan yang mengurus",
                    "pembayaran? Orang yang memutuskan sering sudah pindah kerja, dan",
                    "alasannya ikut hilang bersamanya.",
                    "",
                    "Materi ini membahas tiga alat untuk mencegahnya: catatan",
                    "keputusan (ADR), diagram berlapis (C4 model), dan cara menulis",
                    "dokumentasi yang memang dibaca orang.",
                ],
            },
            {
                "heading": "Architecture Decision Record",
                "body": [
                    "Architecture Decision Record (ADR) adalah catatan pendek untuk",
                    "satu keputusan arsitektur. Bentuknya dipopulerkan Michael Nygard",
                    "lewat tulisan \"Documenting Architecture Decisions\" tahun 2011.",
                    "Isinya lima bagian:",
                    "  - Judul: keputusan dalam satu kalimat, diberi nomor urut.",
                    "  - Status: diusulkan, diterima, atau digantikan ADR lain.",
                    "  - Konteks: keadaan dan batasan yang memaksa keputusan diambil.",
                    "  - Keputusan: apa yang dipilih.",
                    "  - Konsekuensi: apa yang jadi lebih mudah dan apa yang jadi",
                    "    lebih sulit, termasuk yang buruk.",
                    "",
                    "ADR disimpan sebagai berkas Markdown di repositori, misalnya di",
                    "folder docs/adr, dan ikut di-review lewat pull request. Kalau",
                    "keputusan berubah, ADR lama nggak disunting. Statusnya diganti",
                    "jadi \"digantikan ADR 7\", lalu ADR baru ditulis. Dengan begitu",
                    "riwayat alasannya tetap utuh.",
                    "",
                    "Selain template Nygard, ada template Markdown Any Decision Records",
                    "yang menambahkan bagian pilihan yang dipertimbangkan beserta",
                    "plus-minusnya. Kumpulan template dan alat lainnya ada di",
                    "adr.github.io.",
                ],
            },
            {
                "heading": "docs/adr/0003-simpan-pesanan-di-postgresql.md",
                "bahasa": "markdown",
                "code": """# 3. Simpan data pesanan di PostgreSQL

Status: diterima (2026-10-19)

## Konteks
Pesanan, pembayaran, dan stok harus selalu cocok satu sama lain.
Tim berisi dua orang yang sudah terbiasa dengan SQL.

## Keputusan
Kita memakai PostgreSQL dengan transaksi untuk ketiga tabel itu.

## Konsekuensi
- Laporan penjualan bisa ditulis dengan SQL biasa.
- Skema harus diubah lewat migrasi; nggak bisa asal menambah kolom.
- Kalau nanti butuh pencarian teks yang canggih, perlu alat tambahan.""",
            },
            {
                "body": [
                    "Karena ADR berupa berkas di repositori, kelengkapannya bisa",
                    "diperiksa otomatis di pipeline CI, sama seperti kode. Cara",
                    "memperlakukan dokumentasi seperti kode ini disebut docs as code:",
                    "ditulis di repositori, di-review, dan dibangun otomatis. Program",
                    "berikut memeriksa ADR yang lupa diberi bagian Konsekuensi.",
                ],
            },
            {
                "heading": "Pemeriksa ADR di CI",
                "code": "# Docs as code: CI menolak ADR yang bagiannya belum lengkap.\nADR = \"\"\"# 3. Simpan data pesanan di PostgreSQL\n\nStatus: diterima (2026-10-19)\n\n## Konteks\nPesanan, pembayaran, dan stok harus selalu cocok satu sama lain.\n\n## Keputusan\nKita memakai PostgreSQL dengan transaksi untuk ketiga tabel itu.\n\"\"\"\n\nWAJIB = [\"Status:\", \"## Konteks\", \"## Keputusan\", \"## Konsekuensi\"]\n\njudul = ADR.splitlines()[0].lstrip(\"# \")\nkurang = [bagian for bagian in WAJIB if bagian not in ADR]\nprint(\"ADR   :\", judul)\nif kurang:\n    print(\"DITOLAK, bagian yang belum ada:\", \", \".join(kurang))\nelse:\n    print(\"LENGKAP\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ADR   : 3. Simpan data pesanan di PostgreSQL",
                    "  DITOLAK, bagian yang belum ada: ## Konsekuensi",
                    "",
                    "Bagian Konsekuensi paling sering dilupakan, padahal di situlah",
                    "nilai ADR. Keputusan tanpa konsekuensi yang ditulis terdengar",
                    "sempurna, dan pembaca berikutnya nggak tahu harga yang sudah",
                    "disepakati.",
                    "",
                    "Berkas catatan untuk agen di repositori aplikasi ini berisi",
                    "banyak ADR tak resmi. Misalnya keputusan bahwa aplikasi berjalan",
                    "tanpa dependensi pihak ketiga, lengkap dengan alasannya dan",
                    "aturan yang menjaganya.",
                ],
            },
            {
                "heading": "C4 model: diagram dengan empat tingkat zoom",
                "body": [
                    "Diagram arsitektur yang digambar bebas sering membingungkan.",
                    "Kotak apa artinya? Panah ke mana? Detailnya terlalu banyak untuk",
                    "manajer dan terlalu sedikit untuk developer. C4 model, buatan",
                    "Simon Brown, memecahnya jadi empat tingkat, mirip peta yang",
                    "di-zoom:",
                    "  1. System context: sistemmu sebagai satu kotak, siapa",
                    "     penggunanya, dan sistem luar apa yang diajaknya bicara.",
                    "     Bisa dibaca orang non-teknis.",
                    "  2. Container: bagian yang bisa dijalankan atau di-deploy",
                    "     sendiri, misalnya aplikasi web, aplikasi HP, API, dan",
                    "     database. Container di sini bukan container Docker.",
                    "  3. Component: modul utama di dalam satu container.",
                    "  4. Code: class dan fungsi. Tingkat ini jarang digambar tangan,",
                    "     karena cepat basi dan bisa dihasilkan dari kode.",
                    "",
                    "  [Pembeli] --belanja--> [Sistem Toko Melati] --tagih--> [Midtrans]",
                    "                                 |",
                    "                                 +--kirim resi--> [API kurir]",
                    "",
                    "Diagram tingkat satu untuk toko online kira-kira seperti di",
                    "atas. Diagram C4 bisa ditulis sebagai teks lalu digambar alat:",
                    "Structurizr punya bahasa khusus untuk C4, dan PlantUML punya",
                    "pustaka C4-PlantUML. Karena berupa teks, diagramnya bisa",
                    "disimpan dan di-review di Git. Situs c4model.com berlisensi",
                    "CC BY 4.0.",
                ],
            },
            {
                "heading": "Dokumentasi yang dibaca orang",
                "body": [
                    "Kerangka Diataxis, dibuat Daniele Procida, membagi dokumentasi",
                    "jadi empat jenis menurut kebutuhan pembacanya:",
                    "  - Tutorial: belajar sambil mengerjakan, untuk pemula.",
                    "  - Panduan how-to: langkah menyelesaikan satu tugas, misalnya",
                    "    \"cara menambah metode pembayaran\".",
                    "  - Referensi: informasi lengkap dan kering, misalnya daftar",
                    "    endpoint API.",
                    "  - Penjelasan: alasan dan latar belakang. ADR termasuk di sini.",
                    "",
                    "Dokumentasi yang membingungkan biasanya mencampur keempatnya di",
                    "satu halaman. Paling sedikit, setiap proyek butuh README yang",
                    "menjawab: ini apa, cara memasang, cara menjalankan, cara",
                    "menjalankan tes, dan lisensinya. Situs dokumentasi yang lebih",
                    "besar sering dibangun dengan MkDocs, Docusaurus, atau Sphinx.",
                    "",
                    "Di perusahaan, dokumentasi sering tinggal di wiki. Survei Stack",
                    "Overflow 2026 menanyakan alat manajemen pengetahuan ke 9.142",
                    "responden: Confluence dipakai 55%, Google Workspace 41%,",
                    "SharePoint 32%, dan Notion 19%. Survei 2025 mencatat berkas",
                    "Markdown dipakai 34,8% responden untuk dokumentasi kode,",
                    "Confluence 32,8%, Notion 16,5%, dan Obsidian 16,1%. Untuk",
                    "obrolan harian, survei 2024 mencatat Microsoft Teams, Slack,",
                    "Zoom, dan Discord di urutan teratas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek open source besar menyimpan ADR di repositorinya,",
                    "dan tim di perusahaan memakai diagram C4 saat merancang fitur",
                    "baru atau memperkenalkan sistem ke anggota yang baru masuk.",
                    "",
                    "Kasus kecil: kamu magang di sebuah startup. Pembimbingmu bilang",
                    "\"tolong pelajari arsitekturnya\", tapi satu-satunya dokumen",
                    "adalah diagram lama berisi 40 kotak tanpa keterangan, dan tim",
                    "sedang berdebat apakah perlu pindah dari MySQL ke PostgreSQL.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Gambar ulang dari atas: diagram system context dulu, satu",
                    "     kotak sistem dengan pengguna dan sistem luarnya. Tanyakan ke",
                    "     pembimbing apakah gambarnya sudah benar.",
                    "  2. Lanjutkan ke diagram container: aplikasi web, API, worker,",
                    "     database, dan cache. Simpan sebagai teks di repositori.",
                    "  3. Bantu tim menulis ADR untuk perdebatan database itu, dengan",
                    "     konteks dan konsekuensi yang jujur:",
                    "       # 8. Tetap memakai MySQL untuk tahun ini",
                    "       Status: diusulkan",
                    "  4. Tambahkan pemeriksa ADR ke CI supaya ADR berikutnya selalu",
                    "     punya bagian Konteks, Keputusan, dan Konsekuensi.",
                ],
            },
        ],
    },
    {
        "title": "44. Cara Tim Bekerja: Agile, Monorepo, dan Asisten AI",
        "sections": [
            {
                "body": [
                    "Hari pertama PKL atau magang, kamu akan mendengar kata seperti",
                    "sprint, standup, backlog, tiket, dan monorepo. Kamu juga akan",
                    "melihat rekan kerja menyuruh agen AI menulis kode. Materi ini",
                    "menjelaskan ritme kerja itu, supaya kamu bisa langsung ikut dan",
                    "tahu batas tanggung jawabmu.",
                ],
            },
            {
                "heading": "Agile, Scrum, dan Kanban",
                "body": [
                    "Agile adalah cara kerja dalam putaran pendek dengan umpan balik",
                    "terus-menerus. Dasarnya Agile Manifesto (2001), yang berisi",
                    "empat nilai:",
                    "  - individu dan interaksi lebih dari proses dan alat,",
                    "  - perangkat lunak yang jalan lebih dari dokumentasi lengkap,",
                    "  - kolaborasi dengan pelanggan lebih dari negosiasi kontrak,",
                    "  - menanggapi perubahan lebih dari mengikuti rencana.",
                    "",
                    "Scrum adalah kerangka Agile yang paling banyak dipakai. Aturannya",
                    "ada di Scrum Guide edisi 2020 karya Ken Schwaber dan Jeff",
                    "Sutherland:",
                    "  - Tiga peran: Product Owner yang mengurutkan pekerjaan, Scrum",
                    "    Master yang menjaga prosesnya, dan Developers.",
                    "  - Sprint: putaran kerja paling lama satu bulan, sering dua",
                    "    pekan.",
                    "  - Acara: Sprint Planning, Daily Scrum (15 menit, sering disebut",
                    "    standup), Sprint Review, dan Sprint Retrospective.",
                    "  - Artefak: Product Backlog, Sprint Backlog, dan Increment,",
                    "    yaitu hasil kerja yang bisa dipakai di akhir sprint.",
                    "",
                    "Kanban lebih longgar. Pekerjaan ditulis di kartu yang bergerak di",
                    "papan, misalnya kolom To Do, Doing, dan Done. Aturan utamanya",
                    "batas WIP (work in progress), yaitu jumlah maksimal kartu di",
                    "kolom Doing. Batas itu memaksa tim menyelesaikan sebelum",
                    "memulai yang baru. Ukuran yang diperhatikan adalah lead time,",
                    "lama sebuah kartu dari masuk sampai selesai.",
                    "",
                    "  aspek          Scrum                      Kanban",
                    "  ritme          sprint tetap               alur terus-menerus",
                    "  peran          tiga peran baku            tidak diwajibkan",
                    "  perubahan      tunggu sprint berikutnya   kapan saja",
                    "  ukuran utama   hasil per sprint           lead time",
                    "",
                    "Alatnya: survei Stack Overflow 2025 mencatat Jira dipakai 46,4%",
                    "responden, Trello 13,7%, dan Linear 3,7%. GitHub Projects juga",
                    "sering dipakai tim yang kodenya di GitHub.",
                ],
            },
            {
                "heading": "Monorepo atau polyrepo",
                "body": [
                    "Polyrepo artinya tiap proyek punya repositorinya sendiri:",
                    "frontend di satu repo, backend di repo lain, pustaka bersama di",
                    "repo ketiga. Monorepo artinya semuanya di satu repositori.",
                    "",
                    "Monorepo memudahkan perubahan yang menyentuh banyak bagian.",
                    "Mengubah aturan validasi dan semua pemakainya bisa selesai di",
                    "satu pull request. Masalahnya, kalau setiap perubahan",
                    "menjalankan semua tes semua proyek, CI jadi lambat sekali. Alat",
                    "monorepo menjawabnya dengan cara yang sama: cari paket yang",
                    "berubah, lalu bangun dan tes paket itu beserta semua",
                    "pemakainya. Program berikut meniru langkah itu.",
                ],
            },
            {
                "heading": "Paket yang terdampak perubahan",
                "code": """# Monorepo: paket mana yang perlu dibangun ulang dan dites?
BERGANTUNG = {              # paket -> paket lain yang dipakainya
    "web": ["ui", "api-klien"],
    "admin": ["ui", "api-klien"],
    "api": ["validasi"],
    "api-klien": ["validasi"],
    "ui": [],
    "validasi": [],
}
berubah = ["packages/validasi/aturan.ts", "packages/validasi/README.md"]

# Balik arah panahnya: siapa saja yang memakai sebuah paket?
dipakai_oleh = {nama: [] for nama in BERGANTUNG}
for paket, daftar in BERGANTUNG.items():
    for d in daftar:
        dipakai_oleh[d].append(paket)

kena = {jalur.split("/")[1] for jalur in berubah}
antre = list(kena)
while antre:
    paket = antre.pop()
    for pemakai in dipakai_oleh[paket]:
        if pemakai not in kena:
            kena.add(pemakai)
            antre.append(pemakai)

print("berubah langsung:", sorted({j.split("/")[1] for j in berubah}))
print("perlu dites     :", sorted(kena))
print("dilewati        :", sorted(set(BERGANTUNG) - kena))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  berubah langsung: ['validasi']",
                    "  perlu dites     : ['admin', 'api', 'api-klien', 'validasi', 'web']",
                    "  dilewati        : ['ui']",
                    "",
                    "Paket validasi dipakai api dan api-klien, dan api-klien dipakai",
                    "web dan admin. Jadi lima paket ikut dites, dan ui yang nggak",
                    "bergantung pada validasi dilewati. Di monorepo berisi ratusan",
                    "paket, cara ini memangkas waktu CI dari jam ke menit.",
                    "",
                    "Alat yang mengerjakannya: Nx dan Turborepo untuk proyek",
                    "JavaScript/TypeScript, pnpm workspaces untuk mengelola banyak",
                    "paket dalam satu repo, dan Bazel (open source dari Google) untuk",
                    "monorepo raksasa lintas bahasa. Go dan Rust punya workspace",
                    "bawaan. Di survei Stack Overflow 2026, pnpm dipakai 19%",
                    "responden, Yarn 17%, dan Bazel 3%. Google dan Meta dikenal",
                    "memakai monorepo raksasa. Situs monorepo.tools yang sering",
                    "dikutip dibuat tim Nx, jadi bacalah sebagai pandangan satu",
                    "vendor.",
                ],
            },
            {
                "heading": "pnpm-workspace.yaml",
                "bahasa": "yaml",
                "code": "packages:\n  - \"apps/*\"\n  - \"packages/*\"",
            },
            {
                "heading": "Bekerja bersama asisten dan agen AI",
                "body": [
                    "Survei Stack Overflow 2026, seperti dilaporkan IT Brief,",
                    "mencatat 65,9% responden memakai asisten atau agen koding, dan",
                    "62,5% memakai alat chat umum. Di antara pemakai agen koding,",
                    "Claude Code dipakai 66%, GitHub Copilot 59%, OpenAI Codex 30%,",
                    "dan Cursor 26%. Tapi cuma 6,6% yang mau memercayakan keputusan",
                    "penting ke AI, dan 78,7% menganggap sumber jawaban penting saat",
                    "menilai kode atau jawaban buatan AI.",
                    "",
                    "Angka terakhir itu menunjukkan batas tanggung jawabnya. Kode yang",
                    "kamu commit tetap kodemu, siapa pun yang mengetiknya. Kebiasaan",
                    "yang menjaga kendali tetap di tanganmu:",
                    "  - Minta pekerjaan kecil yang bisa kamu periksa, satu perubahan",
                    "    per permintaan.",
                    "  - Baca diff-nya seperti membaca pull request dari orang asing.",
                    "    Kalau ada baris yang nggak kamu pahami, tanyakan atau buang.",
                    "  - Minta tes, lalu jalankan sendiri. Tes yang ditulis bersama",
                    "    kodenya juga perlu dicek: apakah benar menguji kasus yang",
                    "    sulit?",
                    "  - Jangan menempelkan rahasia, data pelanggan, atau kode milik",
                    "    kantor ke layanan yang belum diizinkan kantormu.",
                    "  - Cek ulang nama pustaka dan versi yang disarankan. AI bisa",
                    "    menyebut paket yang nggak ada, dan penyerang pernah",
                    "    mendaftarkan nama paket palsu seperti itu.",
                    "",
                    "Roadmap.sh sekarang punya roadmap khusus seperti Claude Code dan",
                    "Vibe Coding, dan kurikulum AI & Machine Learning membahas cara",
                    "kerja model di baliknya. Keterampilan yang paling lama bertahan",
                    "tetap kemampuan membaca kode dan membuktikan kode itu benar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim produk di startup dan perusahaan teknologi umumnya memakai",
                    "sprint dua pekan dengan papan Jira atau Linear. Tim operasi dan",
                    "dukungan lebih sering memakai Kanban karena pekerjaannya datang",
                    "kapan saja. Proyek TypeScript full-stack makin sering disimpan",
                    "dalam satu monorepo dengan pnpm workspaces dan Turborepo atau Nx.",
                    "",
                    "Kasus kecil: di minggu pertama PKL kamu diberi tiket \"perbaiki",
                    "validasi nomor HP di form pendaftaran\". Repositorinya monorepo",
                    "berisi aplikasi web, admin, dan API, dan kantor membolehkan",
                    "asisten AI yang sudah disetujui.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca tiketnya sampai paham kriteria selesainya. Tanyakan di",
                    "     standup kalau ada yang nggak jelas, misalnya apakah nomor",
                    "     berawalan +62 harus diterima.",
                    "  2. Temukan paket yang memegang aturannya. Di contoh tadi itu",
                    "     paket validasi, yang dipakai web, admin, dan API.",
                    "  3. Minta asisten AI menulis tes untuk kasus yang disepakati,",
                    "     periksa tesnya, lalu jalankan dan pastikan gagal sebelum",
                    "     perbaikan:",
                    "       pnpm --filter validasi test",
                    "  4. Perbaiki, jalankan tes paket yang terdampak, lalu buka pull",
                    "     request kecil yang menyebut nomor tiketnya. Pindahkan",
                    "     kartunya ke kolom review.",
                ],
            },
        ],
    },
    {
        "title": "45. Cara Memilih Stack: Kriteria, Lisensi, dan Umur",
        "sections": [
            {
                "body": [
                    "Sebelas bab sebelumnya menunjukkan puluhan stack, dan tiap",
                    "tahun akan muncul yang baru. Menghafal semuanya mustahil.",
                    "Yang bisa kamu bawa adalah cara menilai: daftar pertanyaan yang",
                    "tetap berlaku untuk teknologi yang bahkan belum lahir hari ini.",
                ],
            },
            {
                "heading": "Kriteria yang dipakai developer sungguhan",
                "body": [
                    "Survei Stack Overflow 2026, seperti dilaporkan IT Brief,",
                    "menanyakan alasan developer merekomendasikan sebuah teknologi.",
                    "Jawaban teratas adalah keandalan, kinerja, dan stabilitas",
                    "(17,3%), lalu produktivitas atau hemat waktu (15,9%), dan",
                    "kekuatan komunitas atau ekosistem (12,9%). Fitur AI cuma dipilih",
                    "2,3%.",
                    "",
                    "Dari situ, kriteria memilih stack bisa disusun begini:",
                    "  - Kebutuhan. Berapa pengguna, apakah perlu real-time, apakah",
                    "    harus muncul di mesin pencari, apakah data pribadi terlibat.",
                    "    Kebutuhan menyingkirkan pilihan lebih cepat dari apa pun.",
                    "  - Kemampuan tim. Stack yang dikuasai tim hampir selalu lebih",
                    "    cepat jadi daripada stack yang lebih bagus di atas kertas.",
                    "  - Ekosistem. Pustaka, dokumentasi, dan jawaban di internet",
                    "    untuk masalah yang pasti akan kamu temui.",
                    "  - Biaya. Hosting, lisensi, dan waktu orang, yang biasanya",
                    "    paling mahal.",
                    "  - Rekrutmen. Bisakah kantor mencari pengganti kalau kamu pindah?",
                    "  - Umur dan dukungan. Masih dirawat, punya jadwal versi LTS, dan",
                    "    nggak bergantung pada satu orang.",
                ],
            },
            {
                "heading": "Membaca survei dengan benar",
                "body": [
                    "Tiap survei mengukur kelompok orang yang berbeda:",
                    "  - Survei Stack Overflow bertanya ke developer yang mau mengisi,",
                    "    jadi condong ke pengguna situs itu.",
                    "  - W3Techs menghitung situs web, bukan developer. Angka PHP 69,4%",
                    "    di sana berarti situs, termasuk jutaan situs WordPress.",
                    "  - Survei CNCF bertanya ke organisasi yang sudah memakai",
                    "    teknologi cloud native.",
                    "  - JetBrains State of Developer Ecosystem edisi 2026 belum",
                    "    terbit saat materi ini ditulis, dan edisi 2025 nggak memuat",
                    "    data arsitektur.",
                    "",
                    "Angka popularitas menjawab \"apakah gampang cari bantuan dan",
                    "orang\". Ia nggak menjawab \"apakah cocok untuk masalahku\".",
                    "MongoDB dipakai 19,0% responden Stack Overflow 2026, tapi kalau",
                    "datamu uang dan stok yang saling terkait, angka itu nggak",
                    "mengubah kenyataan bahwa database relasional lebih cocok.",
                ],
            },
            {
                "heading": "Lisensi dan sejarah perubahannya",
                "body": [
                    "Lisensi menentukan apa yang boleh kamu lakukan dengan sebuah",
                    "perangkat lunak. Kelompok besarnya:",
                    "  - Permisif: MIT, BSD, Apache-2.0. Boleh dipakai, diubah, dan",
                    "    dijual, asal pemberitahuan lisensinya dipertahankan.",
                    "  - Copyleft: GPL mewajibkan kode turunan yang didistribusikan",
                    "    ikut terbuka. AGPL memperluasnya ke layanan yang diakses",
                    "    lewat jaringan. MPL lebih lunak, kewajibannya per berkas.",
                    "  - Source-available: kodenya bisa dibaca, tapi ada batasan,",
                    "    misalnya dilarang dijual sebagai layanan cloud. Contohnya SSPL",
                    "    dan BUSL. Lisensi seperti ini nggak diakui OSI sebagai open",
                    "    source.",
                    "",
                    "Lisensi bisa berubah di tengah jalan, dan beberapa proyek besar",
                    "sudah membuktikannya:",
                    "",
                    "  proyek          perubahan                        tanggapan",
                    "  MongoDB         2018 pindah ke SSPL              banyak yang beralih",
                    "  Elasticsearch   2021 SSPL/Elastic License,        fork OpenSearch",
                    "                  2024 tambah pilihan AGPL",
                    "  Redis           2024 RSAL/SSPL, Redis 8 tambah    fork Valkey",
                    "                  pilihan AGPL",
                    "  Terraform       2023 pindah ke BUSL (v1.6)        fork OpenTofu",
                    "  Serverless Fw   v4 berbayar untuk perusahaan      SST, AWS SAM",
                    "                  beromzet di atas 2 juta dolar",
                    "",
                    "Polanya mirip: perusahaan di balik proyek mengetatkan lisensi,",
                    "lalu komunitas membuat fork yang tetap terbuka. Valkey, misalnya,",
                    "sekarang jadi paket bawaan di Fedora sejak versi 41. Program",
                    "berikut memeriksa daftar calon komponen terhadap kebijakan",
                    "lisensi sebuah tim.",
                ],
            },
            {
                "heading": "Pemeriksa kebijakan lisensi",
                "code": """# Periksa lisensi calon komponen terhadap kebijakan tim.
PERMISIF = {"MIT", "BSD-3-Clause", "Apache-2.0", "PostgreSQL"}
COPYLEFT = {"MPL-2.0", "GPL-2.0", "GPL-3.0", "AGPL-3.0"}

calon = [
    ("PostgreSQL", ["PostgreSQL"]),
    ("MongoDB Community", ["SSPL-1.0"]),
    ("Redis 8", ["RSALv2", "SSPLv1", "AGPL-3.0"]),
    ("Valkey", ["BSD-3-Clause"]),
    ("Terraform", ["BUSL-1.1"]),
    ("OpenTofu", ["MPL-2.0"]),
]

for nama, pilihan in calon:
    if any(lisensi in PERMISIF for lisensi in pilihan):
        status = "aman"
    elif any(lisensi in COPYLEFT for lisensi in pilihan):
        status = "cek syarat copyleft"
    else:
        status = "non-OSI, minta izin"
    print(f"{nama:<18} {'/'.join(pilihan):<23} {status}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  PostgreSQL         PostgreSQL              aman",
                    "  MongoDB Community  SSPL-1.0                non-OSI, minta izin",
                    "  Redis 8            RSALv2/SSPLv1/AGPL-3.0  cek syarat copyleft",
                    "  Valkey             BSD-3-Clause            aman",
                    "  Terraform          BUSL-1.1                non-OSI, minta izin",
                    "  OpenTofu           MPL-2.0                 cek syarat copyleft",
                    "",
                    "Redis 8 punya tiga pilihan lisensi, dan pemakai boleh memilih",
                    "salah satunya. Pilihan AGPL-nya diakui OSI, jadi Redis 8 masuk",
                    "kelompok copyleft. Pemeriksa seperti ini nggak menggantikan",
                    "nasihat hukum, tapi membuat tim berhenti sejenak sebelum",
                    "memasang komponen yang syaratnya belum dibaca.",
                ],
            },
            {
                "heading": "Ketergantungan vendor dan tanda usang",
                "body": [
                    "Vendor lock-in artinya pindah dari sebuah layanan jadi amat",
                    "mahal karena kodemu terikat pada API khususnya. Firebase dan",
                    "DynamoDB nyaman, tapi query dan aturan keamanannya nggak bisa",
                    "dibawa ke tempat lain. Cara mengurangi risikonya: pilih antarmuka",
                    "standar kalau ada (SQL, API yang kompatibel S3, OpenTelemetry),",
                    "dan kumpulkan kode yang menyentuh layanan itu di satu lapisan.",
                    "",
                    "Teknologi juga bisa menua. Contoh dari bab-bab sebelumnya:",
                    "  - AngularJS habis dukungan akhir 2021, tapi masih dipakai 6%",
                    "    responden Stack Overflow 2026, kebanyakan di kode lama.",
                    "  - XAMPP tertahan di versi 8.2.12 sejak November 2023.",
                    "  - Istilah Jamstack ditinggalkan Netlify sejak 2023, walau",
                    "    tekniknya tetap hidup.",
                    "  - RedwoodJS masuk mode pemeliharaan sejak April 2025.",
                    "",
                    "Tanda yang bisa kamu cek sendiri di halaman proyeknya: kapan",
                    "rilis terakhir, apakah issue dijawab, berapa orang pemeliharanya,",
                    "dan apakah ada jadwal dukungan jangka panjang. Proyek yang",
                    "bergantung pada satu orang punya risiko besar walau kodenya",
                    "bagus.",
                    "",
                    "  daftar periksa sebelum memilih",
                    "  1. kebutuhan apa yang wajib dan mana yang cuma diinginkan?",
                    "  2. apakah tim sudah bisa, atau berapa lama belajarnya?",
                    "  3. lisensinya apa, dan pernah berubah atau tidak?",
                    "  4. rilis terakhir kapan, pemeliharanya berapa orang?",
                    "  5. kalau harus pindah dua tahun lagi, apa yang ikut terkunci?",
                    "  6. berapa biaya bulanannya saat pengguna sepuluh kali lipat?",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim teknik di perusahaan biasanya punya daftar teknologi yang",
                    "disetujui dan proses untuk mengusulkan yang baru, sering berupa",
                    "ADR. Saat Terraform berganti lisensi tahun 2023, banyak tim",
                    "infrastruktur menimbang ulang dan sebagian pindah ke OpenTofu.",
                    "",
                    "Kasus kecil: temanmu ingin memakai framework JavaScript baru",
                    "yang sedang ramai di media sosial untuk proyek sistem",
                    "informasi koperasi yang harus dirawat lima tahun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan daftar periksa di atas untuk framework itu dan",
                    "     untuk satu pilihan yang sudah mapan, misalnya Laravel.",
                    "  2. Buka halaman rilisnya. Catat umur proyek, jumlah pemelihara",
                    "     aktif, dan apakah ada versi LTS.",
                    "  3. Baca berkas lisensinya, termasuk riwayat perubahannya.",
                    "  4. Tulis hasilnya sebagai ADR berstatus diusulkan:",
                    "       ## Konsekuensi",
                    "       - Framework baru: dua anggota tim perlu belajar 1 bulan.",
                    "       - Laravel: sudah dikuasai, ekosistem paket matang.",
                    "  5. Biarkan tim memutuskan dari ADR itu. Keputusannya tercatat,",
                    "     dan bisa ditinjau ulang setahun lagi.",
                ],
            },
        ],
    },
    {
        "title": "46. Studi Kasus Memilih Stack untuk Tiga Proyek",
        "sections": [
            {
                "body": [
                    "Materi terakhir ini memakai semua bab sebelumnya untuk tiga",
                    "proyek yang mungkin kamu temui sesudah lulus. Untuk tiap",
                    "proyek, alurnya sama: tulis kebutuhan, singkirkan pilihan yang",
                    "melanggar syarat wajib, beri skor sisanya dengan bobot, lalu",
                    "tulis keputusannya sebagai ADR.",
                    "",
                    "Skor dalam matriks keputusan itu subjektif. Gunanya membuat",
                    "alasan terlihat dan bisa diperdebatkan, bukan menghasilkan",
                    "jawaban pasti. Kalau bobotnya diubah lalu juaranya ikut berubah,",
                    "itu tanda pilihannya memang dekat dan perlu dibicarakan.",
                ],
            },
            {
                "heading": "Proyek 1: toko online UMKM",
                "body": [
                    "Usaha keripik tempe di Malang ingin toko online dengan domain",
                    "sendiri. Produknya sekitar 40, pembayaran lewat payment gateway",
                    "seperti Midtrans atau Xendit, dan yang merawat nanti cuma",
                    "pemiliknya dibantu satu pelajar PKL. Dananya kecil.",
                    "",
                    "Syarat wajib \"punya situs dengan domain sendiri\" langsung",
                    "menyingkirkan pilihan berjualan cuma di marketplace, walau",
                    "marketplace tetap bagus sebagai saluran tambahan. Sisanya",
                    "dinilai:",
                ],
            },
            {
                "heading": "Matriks keputusan dengan dua bobot",
                "code": """# Matriks keputusan untuk toko online UMKM. Skor 1 (buruk) sampai 5 (baik).
CALON = {
    "WordPress + WooCommerce": {"biaya": 4, "tim": 4, "cepat": 5, "kendali": 3},
    "Laravel + Livewire": {"biaya": 4, "tim": 3, "cepat": 2, "kendali": 5},
    "Next.js + Supabase": {"biaya": 3, "tim": 2, "cepat": 3, "kendali": 5},
}


def peringkat(judul, bobot):
    maks = 5 * sum(bobot.values())
    hasil = {nama: sum(bobot[k] * skor[k] for k in bobot)
             for nama, skor in CALON.items()}
    print(f"{judul} (maksimal {maks}):")
    for nama, total in sorted(hasil.items(), key=lambda p: (-p[1], p[0])):
        print(f"  {nama:<24} {total}")


peringkat("Toko kecil, dirawat sendiri", {"biaya": 5, "tim": 4, "cepat": 4, "kendali": 1})
peringkat("Butuh fitur grosir khusus", {"biaya": 3, "tim": 3, "cepat": 2, "kendali": 5})""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Toko kecil, dirawat sendiri (maksimal 70):",
                    "    WordPress + WooCommerce  59",
                    "    Laravel + Livewire       45",
                    "    Next.js + Supabase       40",
                    "  Butuh fitur grosir khusus (maksimal 65):",
                    "    Laravel + Livewire       50",
                    "    WordPress + WooCommerce  49",
                    "    Next.js + Supabase       46",
                    "",
                    "Untuk toko kecil yang dirawat sendiri, WordPress dengan",
                    "WooCommerce di hosting LAMP menang jauh. Pemilik bisa menambah",
                    "produk tanpa developer, dan hostingnya murah (bab Stack Web",
                    "Klasik dan Pola MVC). Tapi kalau toko butuh fitur khusus, misalnya",
                    "harga grosir bertingkat per reseller, bobot kendali naik dan",
                    "Laravel dengan Livewire (bab Stack Framework Backend dan",
                    "Frontend) menyusul tipis. Selisih 50 lawan 49 artinya kedua",
                    "pilihan sama-sama masuk akal, dan yang memutuskan adalah siapa",
                    "yang akan merawatnya.",
                ],
            },
            {
                "heading": "Proyek 2: sistem informasi sekolah",
                "body": [
                    "Sebuah SMK ingin aplikasi nilai, absensi, dan rapor untuk 1.000",
                    "siswa dan 60 guru. Tim pengembangnya dua guru produktif yang",
                    "menguasai PHP. Data siswa termasuk data pribadi yang dilindungi",
                    "Undang-Undang Pelindungan Data Pribadi (UU 27/2022). Aplikasi",
                    "harus bertahan minimal lima tahun.",
                    "",
                    "Keputusan yang masuk akal:",
                    "  - Arsitektur: monolit modular (bab Pola Arsitektur Aplikasi).",
                    "    Seribu siswa jauh dari batas satu server. Microservices cuma",
                    "    menambah beban untuk tim dua orang.",
                    "  - Stack: Laravel dengan PostgreSQL atau MySQL, karena tim",
                    "    sudah menguasai PHP dan Laravel punya autentikasi, antrean,",
                    "    dan pembuat PDF yang matang.",
                    "  - Keandalan: backup harian ke lokasi lain dan latihan",
                    "    pemulihan tiap semester. RPO 24 jam dan RTO setengah hari",
                    "    masih bisa diterima sekolah, asal disepakati tertulis.",
                    "  - Keamanan: hak akses per peran (guru, wali kelas, admin), log",
                    "    perubahan nilai, rate limiting di halaman login, dan",
                    "    dependensi yang dipantau Dependabot.",
                    "  - Dokumentasi: README untuk guru penerus dan ADR untuk setiap",
                    "    keputusan besar, karena pengembangnya bisa berganti.",
                ],
            },
            {
                "heading": "Proyek 3: aplikasi antrean klinik real-time",
                "body": [
                    "Sebuah startup membuat layanan antrean untuk banyak klinik",
                    "(SaaS multi-tenant). Pasien melihat nomornya bergerak secara",
                    "real-time di HP, dan layar di ruang tunggu ikut berubah.",
                    "Targetnya 300 klinik dalam setahun. Timnya empat orang yang",
                    "menguasai TypeScript.",
                    "",
                    "  kebutuhan                    pilihan                bab",
                    "  bahasa yang dikuasai tim     TypeScript, Next.js    03",
                    "  data klinik dan pasien       PostgreSQL, id_klinik  09",
                    "  nomor bergerak real-time     WebSocket + Redis      08, 10",
                    "  pengingat SMS/WA             antrean pesan, worker  10",
                    "  satu klinik nggak boleh      rate limit per klinik  09",
                    "    menghabiskan kapasitas",
                    "  rilis tanpa mengganggu       CI/CD, canary          11",
                    "  tahu kalau ada masalah       SLO 99,9%, trace       11",
                    "",
                    "Satu yang sengaja nggak dipilih: microservices. Dengan empat",
                    "orang, monolit modular berbahasa TypeScript dengan worker",
                    "terpisah untuk pengiriman pesan sudah cukup. Batas modulnya",
                    "(antrean, klinik, notifikasi, tagihan) ditulis sejak awal, jadi",
                    "kalau satu modul nanti perlu dipisah, strangler fig bisa",
                    "dipakai. Pilihan lain yang juga masuk akal untuk tim yang",
                    "berbeda: Laravel dengan Reverb untuk WebSocket, atau Phoenix",
                    "LiveView kalau timnya menguasai Elixir.",
                    "",
                    "Ingat: ketiga keputusan di materi ini benar untuk konteksnya",
                    "masing-masing. Ganti timnya, dananya, atau jumlah penggunanya,",
                    "dan jawabannya bisa ikut berubah. Karena itu konteks selalu",
                    "ditulis di bagian paling atas ADR.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Konsultan dan software house di Indonesia menghadapi pertanyaan",
                    "\"pakai apa?\" di hampir setiap proyek baru, dan biasanya",
                    "menjawabnya dengan dokumen usulan teknis berisi kebutuhan,",
                    "pilihan yang dipertimbangkan, dan alasan pilihan akhirnya.",
                    "",
                    "Kasus kecil: perpustakaan daerah minta aplikasi peminjaman buku",
                    "dengan daftar buku yang bisa dicari dari HP. Anggarannya terbatas,",
                    "yang merawat satu staf IT yang bisa Python, dan pengunjung",
                    "situsnya sekitar 2.000 orang per hari.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis syarat wajib: bisa dirawat staf yang menguasai Python,",
                    "     data disimpan di server milik daerah, dan bisa dicari dari",
                    "     HP. Syarat ini menyingkirkan BaaS tertutup.",
                    "  2. Pilih kriteria dan bobotnya bersama kepala perpustakaan:",
                    "     biaya, kemampuan staf, waktu jadi, dan kemudahan perawatan.",
                    "  3. Nilai dua atau tiga calon, misalnya Django dengan",
                    "     PostgreSQL, FastAPI dengan React, dan Django dengan htmx:",
                    "       skor = sum(bobot[k] * nilai[k] for k in bobot)",
                    "  4. Tulis pemenangnya sebagai ADR, lengkap dengan konsekuensinya",
                    "     dan alasan calon lain kalah. Latihan terakhir sebelum",
                    "     proyek akhir memintamu membuat program matriks keputusan",
                    "     seperti ini.",
                ],
            },
        ],
    },
]
