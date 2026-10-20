"""Kurikulum Keamanan Siber.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

KEAMANAN_BAB = [
    {
        "judul": "Pola Pikir Bertahan dan Etika",
        "ket": "Cara berpikir seperti penjaga, batas hukum, dan memasukkan keamanan sejak desain.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Kriptografi Terapan",
        "ket": "Hash, password, enkripsi, dan sertifikat yang dipakai sehari-hari.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Autentikasi dan Otorisasi",
        "ket": "Memastikan siapa penggunanya dan apa yang boleh ia lakukan.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "OWASP Top 10:2025",
        "ket": "Risiko keamanan aplikasi web paling penting beserta perbaikannya.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Keamanan API dan Perlindungan Layanan",
        "ket": "Rate limiting, header keamanan, dan API yang tahan disalahgunakan.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Rahasia dan Rantai Pasok",
        "ket": "Menyimpan kunci dengan benar dan menjaga dependensi serta artefak.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "DevSecOps: Pemindaian di Pipeline",
        "ket": "Memasang pemeriksa keamanan otomatis di CI.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Menguji Sistem Milik Sendiri",
        "ket": "Memindai jaringan dan aplikasi sendiri dengan alat penguji, di lab yang legal.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "Deteksi, Respons, dan Keamanan Cloud",
        "ket": "Mengenali serangan dari log, menanganinya, dan mengamankan akun cloud.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Kepatuhan, Privasi, dan Proyek Akhir",
        "ket": "Standar dan regulasi, perlindungan data pribadi, lalu proyek audit.",
        "tingkat": "mahir",
        "jumlah": 2,
    },
]

KEAMANAN_MATERIALS = [
    {
        "title": "1. Keamanan Siber dari Sisi Bertahan: CIA dan Risiko",
        "sections": [
            {
                "body": [
                    "Kalau dengar kata hacker, yang kebayang biasanya orang berhoodie",
                    "yang ngetik cepat di layar hitam. Kurikulum ini mengambil sisi",
                    "sebaliknya: kamu belajar jadi penjaga. Tugas penjaga adalah",
                    "memastikan sistem tetap jalan, datanya nggak bocor, dan isinya",
                    "nggak diubah orang yang nggak berhak.",
                    "",
                    "Bayangkan kamu mengurus rumah kos. Kamu nggak mungkin menjaga",
                    "pintu 24 jam. Yang bisa kamu lakukan: memasang kunci yang bagus,",
                    "memberi kunci cadangan cuma ke penghuni, memasang lampu di",
                    "lorong, dan mencatat siapa yang keluar masuk. Keamanan siber",
                    "bekerja dengan cara yang sama. Kamu nggak bisa menghapus semua",
                    "kemungkinan serangan, tapi kamu bisa membuatnya mahal, lambat,",
                    "dan ketahuan.",
                    "",
                    "Materi ini memberi dua alat pikir yang dipakai sepanjang",
                    "kurikulum: tiga sifat yang dijaga (sering disingkat CIA), dan",
                    "cara menilai risiko supaya tenagamu dipakai untuk hal yang",
                    "paling penting dulu.",
                ],
            },
            {
                "heading": "Tiga hal yang dijaga",
                "body": [
                    "Hampir semua masalah keamanan bisa dimasukkan ke salah satu",
                    "dari tiga kotak ini:",
                    "",
                    "  - Kerahasiaan (confidentiality): data cuma bisa dibaca orang",
                    "    yang berhak. Contoh pelanggarannya: daftar nilai siswa",
                    "    tersebar di grup WhatsApp, atau nomor KTP pelanggan bocor.",
                    "  - Integritas (integrity): data nggak berubah tanpa izin, dan",
                    "    kalau berubah, perubahannya ketahuan. Contoh pelanggarannya:",
                    "    nilai rapor diganti, atau nomor rekening tujuan di invoice",
                    "    ditukar.",
                    "  - Ketersediaan (availability): sistem bisa dipakai saat",
                    "    dibutuhkan. Contoh pelanggarannya: situs pendaftaran sekolah",
                    "    mati di hari terakhir pendaftaran.",
                    "",
                    "Huruf depan istilah Inggrisnya itulah yang membentuk singkatan",
                    "CIA. Gunanya praktis. Saat ada kejadian, tanyakan sifat mana yang",
                    "rusak. Jawabannya langsung menunjukkan jenis perlindungan yang",
                    "kurang: enkripsi dan kontrol akses untuk kerahasiaan, tanda",
                    "tangan dan log untuk integritas, cadangan dan kapasitas untuk",
                    "ketersediaan.",
                    "",
                    "Ketiganya sering tarik-menarik. Mengunci data rapat-rapat",
                    "menaikkan kerahasiaan, tapi kalau kuncinya hilang, datanya",
                    "nggak tersedia lagi untuk siapa pun. Pekerjaan penjaga adalah",
                    "mencari titik seimbangnya.",
                ],
            },
            {
                "heading": "Aset, ancaman, kerentanan, risiko",
                "body": [
                    "Empat istilah ini sering tertukar, padahal artinya beda:",
                    "",
                    "  - Aset: sesuatu yang berharga dan perlu dilindungi. Database",
                    "    pelanggan, akun admin, reputasi toko, bahkan waktu kerja.",
                    "  - Ancaman: siapa atau apa yang bisa merugikan aset. Penipu,",
                    "    pegawai yang kesal, bot yang menebak password, atau banjir",
                    "    yang merendam ruang server.",
                    "  - Kerentanan: celah yang bisa dimanfaatkan ancaman. Password",
                    "    admin \"admin123\", server yang nggak pernah diperbarui, form",
                    "    yang menerima masukan apa saja.",
                    "  - Risiko: kemungkinan ancaman memanfaatkan kerentanan, dikali",
                    "    seberapa parah akibatnya kalau itu terjadi.",
                    "",
                    "Contoh satu kalimat: bot (ancaman) bisa menebak password admin",
                    "yang lemah (kerentanan) lalu menguras saldo toko (aset), dan",
                    "karena tebakan seperti itu sering terjadi dan akibatnya besar,",
                    "risikonya tinggi.",
                ],
            },
            {
                "heading": "Menilai risiko dengan dua angka",
                "code": """# Daftar risiko toko online kecil: (ancaman, kemungkinan, dampak)
# Skala 1 sampai 5. Angkanya hasil diskusi tim, bukan rumus pasti.
risiko = [
    ("Password admin ditebak", 4, 5),
    ("Server mati saat promo", 3, 4),
    ("Laptop kasir dicuri", 2, 3),
    ("Database terhapus, backup nggak ada", 2, 5),
    ("Halaman depan dicoret-coret", 2, 2),
]


def tingkat(skor):
    if skor >= 15:
        return "tinggi"
    if skor >= 8:
        return "sedang"
    return "rendah"


urut = sorted(risiko, key=lambda r: r[1] * r[2], reverse=True)
for ancaman, kemungkinan, dampak in urut:
    skor = kemungkinan * dampak
    print(f"{skor:>2}  {tingkat(skor):<7} {ancaman}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  20  tinggi  Password admin ditebak",
                    "  12  sedang  Server mati saat promo",
                    "  10  sedang  Database terhapus, backup nggak ada",
                    "   6  rendah  Laptop kasir dicuri",
                    "   4  rendah  Halaman depan dicoret-coret",
                    "",
                    "Tabel sederhana seperti ini namanya register risiko. Angkanya",
                    "kasar, dan itu nggak apa-apa. Tujuannya membuat tim sepakat",
                    "soal urutan kerja: password admin dibereskan duluan, coretan di",
                    "halaman depan belakangan.",
                    "",
                    "Untuk tiap risiko ada empat pilihan sikap:",
                    "  - Kurangi: pasang perlindungan. Misalnya MFA untuk akun admin.",
                    "  - Hindari: buang fitur atau data penyebabnya. Toko yang nggak",
                    "    menyimpan nomor kartu kredit nggak bisa membocorkannya.",
                    "  - Alihkan: serahkan ke pihak lain, misalnya memakai payment",
                    "    gateway atau asuransi.",
                    "  - Terima: risikonya kecil dan biaya penangkalnya lebih mahal.",
                    "    Keputusan ini sah asal dicatat dan disetujui pemiliknya.",
                ],
            },
            {
                "heading": "Pertahanan berlapis",
                "body": [
                    "Satu perlindungan pasti suatu hari gagal. Password bisa bocor,",
                    "firewall bisa salah setel, programmer bisa lupa satu validasi.",
                    "Karena itu sistem yang baik dijaga beberapa lapis, istilahnya",
                    "defense in depth. Penyerang yang lolos satu lapis masih harus",
                    "menembus lapis berikutnya, dan tiap lapis memberi kesempatan",
                    "untuk ketahuan.",
                    "",
                    "Contoh lapisan untuk aplikasi web biasa, dari luar ke dalam:",
                    "  1. Pemantauan log dan alert, supaya kejadian aneh terlihat.",
                    "  2. Firewall yang cuma membuka port yang memang dipakai.",
                    "  3. Server dan pustaka yang rutin diperbarui.",
                    "  4. Login dengan MFA dan batas percobaan.",
                    "  5. Aplikasi yang memvalidasi masukan dan memeriksa hak akses",
                    "     di setiap permintaan.",
                    "  6. Data sensitif yang dienkripsi, plus cadangan yang disimpan",
                    "     terpisah.",
                    "",
                    "Ingat: lapisan yang sama dua kali nggak dihitung dua lapis.",
                    "Dua firewall dengan aturan yang sama akan gagal bersama-sama.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: merasa aman karena sistemnya kecil. Bot penebak",
                    "password dan pemindai otomatis nggak memilih korban berdasarkan",
                    "ukuran. Mereka mencoba semua alamat yang bisa dijangkau, termasuk",
                    "blog pribadimu dan server latihan yang lupa kamu matikan.",
                    "",
                    "Jebakan lain adalah menganggap keamanan sebagai alat yang",
                    "dibeli sekali. Antivirus atau firewall mahal nggak menolong",
                    "kalau password admin masih bawaan pabrik. Kebanyakan kebocoran",
                    "berasal dari hal sederhana yang terlewat: password lemah,",
                    "pembaruan yang ditunda, dan hak akses yang terlalu luas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pada Juni 2024, Pusat Data Nasional Sementara di Surabaya",
                    "terkena ransomware, yaitu program jahat yang mengunci data lalu",
                    "meminta tebusan. Ratusan instansi pemerintah terdampak, dan",
                    "layanan imigrasi di bandara sempat terganggu. Belakangan",
                    "terungkap sebagian besar data di sana nggak punya cadangan. Dari",
                    "sudut pandang tiga sifat tadi, yang paling telak terpukul adalah",
                    "ketersediaan, dan lapisan yang hilang adalah cadangan yang",
                    "terpisah dari sistem utama.",
                    "",
                    "Kasus kecil: temanmu punya toko online kecil dan bertanya,",
                    "\"Aku harus mulai mengamankan dari mana?\"",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis daftar aset bersama dia: database pesanan, akun admin,",
                    "     akun payment gateway, domain, dan laptop kasir.",
                    "  2. Untuk tiap aset, tanyakan sifat mana yang paling merugikan",
                    "     kalau rusak: bocor, berubah, atau nggak bisa dipakai.",
                    "  3. Tulis lima sampai sepuluh risiko, beri angka kemungkinan dan",
                    "     dampak 1 sampai 5, lalu urutkan seperti program di atas.",
                    "  4. Kerjakan tiga teratas dulu. Biasanya hasilnya MFA di semua",
                    "     akun admin, pembaruan rutin, dan backup harian yang disimpan",
                    "     di tempat lain.",
                    "  5. Ulangi daftar itu tiap tiga bulan, atau tiap ada fitur baru.",
                ],
            },
        ],
    },
    {
        "title": "2. Etika, Hukum, dan Lab Legal untuk Belajar Keamanan",
        "sections": [
            {
                "body": [
                    "Alat yang dipakai penjaga dan penyerang sering sama persis.",
                    "Pemindai port yang dipakai admin untuk mengecek servernya sendiri",
                    "adalah program yang sama dengan yang dipakai penjahat untuk",
                    "mencari korban. Yang membedakan keduanya cuma satu hal: izin.",
                    "",
                    "Aturan ini berlaku di seluruh kurikulum, dan materi lain akan",
                    "merujuk ke sini:",
                    "",
                    "  - Alat penguji dan pemindai hanya boleh diarahkan ke sistem",
                    "    milikmu sendiri: laptopmu, VM di laptopmu, container yang kamu",
                    "    jalankan, atau aplikasi latihan di localhost.",
                    "  - Selain itu, hanya ke lab yang memang disediakan untuk",
                    "    latihan, misalnya Web Security Academy atau kompetisi CTF,",
                    "    dan cuma di dalam aturan main mereka.",
                    "  - Untuk pekerjaan sungguhan (menguji sistem kantor atau klien),",
                    "    wajib ada izin tertulis dari pemilik sistem sebelum satu",
                    "    perintah pun dijalankan.",
                    "",
                    "\"Cuma penasaran\" dan \"nggak merusak apa-apa\" nggak mengubah",
                    "status perbuatannya. Server sekolahmu juga bukan milikmu, walau",
                    "kamu siswanya.",
                ],
            },
            {
                "heading": "Yang diatur hukum di Indonesia",
                "body": [
                    "Sejak 2 Januari 2026, Kitab Undang-Undang Hukum Pidana yang baru",
                    "(Undang-Undang Nomor 1 Tahun 2023) berlaku. Larangan mengakses",
                    "komputer orang lain tanpa hak dulu ada di Pasal 30 UU ITE.",
                    "Pasal itu dan pasal pidananya dicabut oleh kitab yang baru, dan",
                    "larangannya sekarang ada di Pasal 332. Isinya, diringkas dari",
                    "teks resminya:",
                    "",
                    "  - Ayat (1): sengaja dan tanpa hak mengakses komputer atau",
                    "    sistem elektronik milik orang lain dengan cara apa pun.",
                    "    Ancamannya penjara paling lama 6 tahun atau denda paling",
                    "    banyak kategori V (Rp500 juta).",
                    "  - Ayat (2): sama, dengan tujuan memperoleh informasi atau",
                    "    dokumen elektronik. Ancamannya paling lama 7 tahun.",
                    "  - Ayat (3): sama, dengan menerobos atau menjebol sistem",
                    "    pengamanan. Ancamannya paling lama 8 tahun atau denda paling",
                    "    banyak kategori VI (Rp2 miliar).",
                    "",
                    "Perhatikan frasa \"dengan cara apa pun\". Pasal itu nggak",
                    "mensyaratkan ada kerusakan, dan nggak mengecualikan orang yang",
                    "niatnya cuma mencoba. Mengganti angka di URL untuk melihat data",
                    "akun orang lain sudah termasuk mengakses tanpa hak.",
                    "",
                    "Data pribadi juga dilindungi Undang-Undang Nomor 27 Tahun 2022",
                    "tentang Pelindungan Data Pribadi. Menyimpan atau menyebarkan",
                    "data orang yang kamu temukan dari celah bisa jadi masalah",
                    "tersendiri. Ringkasan ini bahan belajar, bukan nasihat hukum.",
                    "Untuk kasus sungguhan, tanyakan ke ahli hukum.",
                ],
            },
            {
                "heading": "Izin tertulis untuk pekerjaan sungguhan",
                "body": [
                    "Penguji keamanan profesional (pentester) nggak mulai kerja",
                    "sebelum memegang dokumen izin yang ditandatangani pemilik",
                    "sistem. Dokumen itu biasanya memuat:",
                    "",
                    "  - Cakupan: alamat IP, domain, dan aplikasi mana saja yang boleh",
                    "    diuji, dan mana yang dilarang.",
                    "  - Waktu: tanggal dan jam pengujian, supaya tim operasional",
                    "    nggak panik melihat lalu lintas aneh.",
                    "  - Cara: teknik yang boleh dan nggak boleh, misalnya larangan",
                    "    membanjiri server atau menipu pegawai.",
                    "  - Kontak darurat dari kedua pihak.",
                    "  - Cara menangani data yang ditemukan selama pengujian.",
                    "",
                    "Program bug bounty memakai prinsip yang sama dalam bentuk",
                    "halaman aturan publik. Perusahaan menulis apa yang boleh diuji,",
                    "dan berjanji nggak menuntut orang yang mengikuti aturan itu.",
                    "Keluar dari cakupan berarti keluar dari perlindungan.",
                ],
            },
            {
                "heading": "Menemukan celah di sistem orang lain",
                "body": [
                    "Kadang celah ketemu tanpa dicari. Misalnya kamu sadar halaman",
                    "profil di aplikasi kampus menampilkan data mahasiswa lain kalau",
                    "angka di URL-nya berubah. Langkah yang bertanggung jawab,",
                    "biasanya disebut coordinated disclosure:",
                    "",
                    "  1. Berhenti. Jangan mencoba lebih jauh untuk \"memastikan\".",
                    "  2. Jangan mengambil, menyimpan, atau membagikan data orang",
                    "     lain. Catat seperlunya: halaman apa dan langkah apa.",
                    "  3. Cari kanal resmi. Banyak situs memasang berkas",
                    "     /.well-known/security.txt (standar RFC 9116) yang berisi",
                    "     alamat pelaporan.",
                    "  4. Laporkan dengan sopan dan jelas, tanpa meminta imbalan",
                    "     sebagai syarat. Permintaan uang supaya celahnya nggak",
                    "     disebar adalah pemerasan.",
                    "  5. Beri waktu untuk memperbaiki. Tim Project Zero di Google,",
                    "     misalnya, memakai batas 90 hari sebelum detail dibuka.",
                    "  6. Publikasikan detail teknis hanya sesudah diperbaiki, dan",
                    "     sebaiknya bersama pemilik sistem.",
                    "",
                    "Program di bawah membaca isi security.txt dan mengecek dua",
                    "medan yang diwajibkan standarnya: Contact dan Expires.",
                ],
            },
            {
                "heading": "Membaca security.txt",
                "code": "from datetime import date\n\nisi = \"\"\"\\\n# security.txt milik tokokecil.example\nContact: mailto:keamanan@tokokecil.example\nContact: https://tokokecil.example/lapor-celah\nExpires: 2027-06-30T00:00:00Z\nPreferred-Languages: id, en\nPolicy: https://tokokecil.example/kebijakan-keamanan\n\"\"\"\n\nhari_ini = date(2026, 10, 19)  # dipatok supaya hasilnya selalu sama\n\nmedan = {}\nfor baris in isi.splitlines():\n    baris = baris.strip()\n    if not baris or baris.startswith(\"#\"):\n        continue\n    nama, _, nilai = baris.partition(\":\")\n    medan.setdefault(nama.strip().lower(), []).append(nilai.strip())\n\nkontak = medan.get(\"contact\", [])\nif kontak:\n    for k in kontak:\n        print(\"Kontak:\", k)\nelse:\n    print(\"Masalah: Contact wajib ada\")\n\nexpires = medan.get(\"expires\", [])\nif len(expires) != 1:\n    print(\"Masalah: Expires wajib ada, tepat satu kali\")\nelse:\n    tanggal = date.fromisoformat(expires[0][:10])\n    sisa = (tanggal - hari_ini).days\n    if sisa < 0:\n        print(\"Masalah: berkas ini sudah kedaluwarsa\")\n    else:\n        print(f\"Berlaku sampai {tanggal} ({sisa} hari lagi)\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Kontak: mailto:keamanan@tokokecil.example",
                    "  Kontak: https://tokokecil.example/lapor-celah",
                    "  Berlaku sampai 2027-06-30 (254 hari lagi)",
                    "",
                    "Expires diwajibkan supaya alamat kontak yang sudah basi nggak",
                    "dipakai bertahun-tahun. Kalau kamu mengelola situs, pasang",
                    "berkas ini dan pasang pengingat untuk memperbaruinya. Pelapor",
                    "yang beritikad baik jadi tahu harus ke mana.",
                ],
            },
            {
                "heading": "Membangun lab latihan sendiri",
                "body": [
                    "Kabar baiknya, tempat latihan yang legal itu murah, bahkan",
                    "gratis. Pilihannya dari yang paling dekat:",
                    "",
                    "  - Mesin virtual (VM) di laptopmu, lewat VirtualBox, GNOME",
                    "    Boxes, atau virt-manager. VM yang rusak tinggal dihapus.",
                    "    Distribusi Kali Linux sudah membawa banyak alat penguji.",
                    "  - Container dengan Podman atau Docker untuk menjalankan",
                    "    aplikasi yang sengaja dibuat rentan.",
                    "  - OWASP Juice Shop: toko online palsu yang sengaja penuh celah,",
                    "    lengkap dengan papan skor tantangan. Jalankan di localhost.",
                    "  - Web Security Academy dari PortSwigger: materi dan lab",
                    "    keamanan web gratis, cukup daftar akun.",
                    "  - Kompetisi CTF (capture the flag), lomba memecahkan soal",
                    "    keamanan. picoCTF dari Carnegie Mellon University ramah",
                    "    pemula, dan CTFtime.org mendaftar jadwal lomba lainnya.",
                ],
            },
            {
                "heading": "Menjalankan Juice Shop di laptop sendiri",
                "bahasa": "terminal",
                "code": """# Ikat ke 127.0.0.1 supaya aplikasi rentan ini nggak bisa
# dijangkau komputer lain di jaringan Wi-Fi yang sama.
podman run --rm -p 127.0.0.1:3000:3000 docker.io/bkimminich/juice-shop

# Lalu buka http://localhost:3000 di browser.""",
            },
            {
                "heading": "Jebakan saat berlatih",
                "body": [
                    "Jebakan: menjalankan aplikasi rentan dengan -p 3000:3000 tanpa",
                    "alamat. Bentuk itu membuka port di semua antarmuka jaringan,",
                    "jadi siapa pun di kafe atau kos yang sama bisa ikut menyerang",
                    "laptopmu lewat aplikasi itu. Selalu tulis 127.0.0.1 di depannya.",
                    "",
                    "Jebakan kedua: mencoba teknik dari tutorial ke situs sungguhan",
                    "\"cuma sekali\". Log server mencatat alamat IP-mu, dan alasan",
                    "belajar nggak menghapus catatan itu. Kalau ingin mencoba teknik",
                    "baru, cari lab yang menyediakannya, atau bangun sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak perusahaan teknologi besar membuka program bug bounty di",
                    "platform seperti HackerOne dan Bugcrowd. Halaman programnya",
                    "menulis domain yang boleh diuji, jenis celah yang dicari, dan",
                    "teknik yang dilarang. Pelapor yang mengikuti aturan mendapat",
                    "imbalan dan perlindungan. Pelapor yang keluar dari aturan",
                    "kehilangan keduanya.",
                    "",
                    "Kasus kecil: saat membuka rapor online, kamu melihat URL",
                    "berakhiran ?id=1532. Iseng mengganti jadi 1533, muncul rapor",
                    "teman sekelasmu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tutup halaman itu dan jangan mencoba nomor lain.",
                    "  2. Jangan memotret atau menyebarkan rapor temanmu. Catat saja",
                    "     alamat halamannya dan langkah yang kamu lakukan.",
                    "  3. Cari kanal resmi: security.txt di situsnya, alamat email",
                    "     admin, atau guru yang mengurus sistem itu.",
                    "  4. Laporkan secara tertulis: halaman mana, langkahnya, dan",
                    "     dampaknya (data siswa lain bisa dilihat).",
                    "  5. Tanyakan kabar perbaikannya sesudah beberapa minggu, dan",
                    "     jangan cerita detailnya ke orang lain sebelum beres.",
                ],
            },
        ],
    },
    {
        "title": "3. Threat Modeling dengan STRIDE dan PASTA",
        "sections": [
            {
                "body": [
                    "Threat modeling adalah kegiatan duduk bersama sebelum kode",
                    "ditulis, lalu bertanya: apa saja yang bisa salah dengan desain",
                    "ini? Ibaratnya arsitek yang memikirkan jalur evakuasi kebakaran",
                    "saat gambar rumah masih di kertas. Memindahkan tangga di kertas",
                    "itu gampang. Memindahkannya sesudah rumah jadi butuh bongkar",
                    "tembok.",
                    "",
                    "Komunitas threat modeling merangkum kegiatannya dalam empat",
                    "pertanyaan:",
                    "  1. Apa yang sedang kita kerjakan?",
                    "  2. Apa yang bisa salah?",
                    "  3. Apa yang akan kita lakukan soal itu?",
                    "  4. Sudahkah kita mengerjakannya dengan cukup baik?",
                    "",
                    "Pertanyaan pertama dijawab dengan gambar. Pertanyaan kedua",
                    "dijawab dengan bantuan daftar pancingan, dan yang paling",
                    "terkenal dibahas di bawah.",
                ],
            },
            {
                "heading": "Gambar dulu: diagram alir data",
                "body": [
                    "Gambar yang biasa dipakai adalah diagram alir data (data flow",
                    "diagram). Isinya cuma lima jenis benda:",
                    "",
                    "  - Entitas luar: orang atau sistem di luar kendalimu, misalnya",
                    "    pembeli atau layanan ekspedisi.",
                    "  - Proses: kode yang kamu jalankan, misalnya aplikasi web atau",
                    "    API.",
                    "  - Penyimpanan: tempat data diam, misalnya database atau folder",
                    "    unggahan.",
                    "  - Aliran data: panah yang menunjukkan data berpindah dari mana",
                    "    ke mana.",
                    "  - Batas kepercayaan (trust boundary): garis tempat tingkat",
                    "    kepercayaan berubah, misalnya antara internet dan servermu.",
                    "",
                    "Batas kepercayaan adalah tempat paling subur untuk masalah. Data",
                    "yang menyeberang dari luar ke dalam harus dianggap mencurigakan",
                    "sampai terbukti sebaliknya.",
                ],
            },
            {
                "heading": "Enam pertanyaan STRIDE",
                "body": [
                    "Daftar pancingan ini disusun di Microsoft pada 1999 oleh Loren",
                    "Kohnfelder dan Praerit Garg. Tiap hurufnya satu jenis ancaman,",
                    "dan tiap jenis",
                    "melanggar satu sifat yang ingin kamu jaga:",
                    "",
                    "  Huruf  Ancaman                  Sifat yang dilanggar",
                    "  S      Spoofing (menyamar)      autentikasi",
                    "  T      Tampering (mengubah)     integritas",
                    "  R      Repudiation (menyangkal) bukti tindakan",
                    "  I      Information disclosure   kerahasiaan",
                    "  D      Denial of service        ketersediaan",
                    "  E      Elevation of privilege   otorisasi",
                    "",
                    "Cara pakainya: tunjuk satu benda di diagram, lalu tanyakan",
                    "keenam huruf itu satu per satu. Bisakah orang menyamar jadi",
                    "pengguna ini? Bisakah data di panah ini diubah di tengah jalan?",
                    "Kalau admin menghapus pesanan, adakah bukti siapa pelakunya?",
                    "",
                    "Hasilnya daftar ancaman beserta penangkalnya. Program di bawah",
                    "mengelompokkan daftar seperti itu untuk fitur login toko online.",
                ],
            },
            {
                "heading": "Daftar ancaman fitur login",
                "code": """NAMA = {
    "S": "Spoofing (menyamar)",
    "T": "Tampering (mengubah data)",
    "R": "Repudiation (menyangkal)",
    "I": "Information disclosure (bocor)",
    "D": "Denial of service (melumpuhkan)",
    "E": "Elevation of privilege (naik hak)",
}

# (kategori, ancaman, penangkal) untuk fitur login toko online
ancaman = [
    ("S", "login pakai password curian", "MFA dan batas percobaan"),
    ("T", "harga di keranjang diubah dari browser", "hitung ulang di server"),
    ("R", "admin menyangkal menghapus pesanan", "log audit"),
    ("I", "pesan error menampilkan query SQL", "pesan error umum"),
    ("I", "backup database ada di folder publik", "simpan di luar web root"),
    ("D", "form login dibanjiri permintaan", "rate limiting"),
    ("E", "pembeli biasa membuka /admin", "cek peran di server"),
]

for huruf in "STRIDE":
    temuan = [a for a in ancaman if a[0] == huruf]
    print(f"{NAMA[huruf]}: {len(temuan)}")
    for _, apa, tangkal in temuan:
        print(f"    {apa} -> {tangkal}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Spoofing (menyamar): 1",
                    "      login pakai password curian -> MFA dan batas percobaan",
                    "  Tampering (mengubah data): 1",
                    "      harga di keranjang diubah dari browser -> hitung ulang di server",
                    "  Repudiation (menyangkal): 1",
                    "      admin menyangkal menghapus pesanan -> log audit",
                    "  Information disclosure (bocor): 2",
                    "      pesan error menampilkan query SQL -> pesan error umum",
                    "      backup database ada di folder publik -> simpan di luar web root",
                    "  Denial of service (melumpuhkan): 1",
                    "      form login dibanjiri permintaan -> rate limiting",
                    "  Elevation of privilege (naik hak): 1",
                    "      pembeli biasa membuka /admin -> cek peran di server",
                    "",
                    "Kategori yang isinya nol justru menarik untuk dibahas. Kalau",
                    "tim nggak menemukan satu ancaman pun di satu huruf, biasanya",
                    "itu tanda huruf itu belum dipikirkan serius.",
                    "",
                    "Perhatikan juga ancaman Tampering di atas. Harga yang dikirim",
                    "browser bisa diubah siapa saja lewat alat developer di browser.",
                    "Server harus menghitung ulang harga dari database, bukan",
                    "percaya pada angka kiriman pengguna.",
                ],
            },
            {
                "heading": "Permukaan serangan",
                "body": [
                    "Permukaan serangan (attack surface) adalah semua titik tempat",
                    "penyerang bisa memasukkan sesuatu ke sistemmu. Contohnya form,",
                    "endpoint API, unggahan berkas, panel admin, port yang terbuka,",
                    "bahkan pustaka pihak ketiga yang ikut terpasang.",
                    "",
                    "Memetakannya sering memberi kemenangan termurah. Panel admin",
                    "yang cuma dipakai tiga orang nggak perlu terbuka ke seluruh",
                    "internet. Endpoint lama yang sudah nggak dipakai aplikasi",
                    "seluler versi baru bisa dimatikan. Tiap titik yang ditutup",
                    "adalah titik yang nggak perlu dijaga lagi.",
                ],
            },
            {
                "heading": "PASTA: tujuh tahap berbasis risiko",
                "body": [
                    "PASTA (Process for Attack Simulation and Threat Analysis)",
                    "diperkenalkan Tony UcedaVélez dan Marco Morana. Enam pertanyaan",
                    "tadi berangkat dari diagram teknis. Pendekatan ini berangkat",
                    "dari tujuan bisnis, lalu turun ke teknis. Tujuh tahapnya:",
                    "",
                    "  1. Tentukan tujuan bisnis dan kebutuhan kepatuhan.",
                    "  2. Tentukan cakupan teknis: komponen, infrastruktur, data.",
                    "  3. Uraikan aplikasi jadi diagram alir data.",
                    "  4. Analisis ancaman: siapa penyerangnya dan apa motifnya.",
                    "  5. Analisis kerentanan yang sudah diketahui di komponennya.",
                    "  6. Modelkan serangan, misalnya dengan pohon serangan.",
                    "  7. Analisis risiko dan dampak, lalu pilih penangkal.",
                    "",
                    "Pendekatan ini lebih berat dan biasanya dipakai organisasi yang",
                    "harus menjelaskan keputusan keamanannya ke manajemen dalam",
                    "bahasa kerugian bisnis. Untuk tim kecil atau satu fitur, enam",
                    "pertanyaan di atas diagram sederhana sudah cukup.",
                    "",
                    "Alat bantu gratis yang sering dipakai: Threat Dragon dari",
                    "OWASP (berbasis web, open source) dan Microsoft Threat Modeling Tool",
                    "(untuk Windows). Papan tulis dan spidol pun cukup.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: menganggap threat modeling sebagai dokumen sekali",
                    "jadi. Desain berubah tiap ada fitur baru, jadi diagramnya ikut",
                    "berubah. Sesi lima belas menit tiap ada fitur besar lebih",
                    "berguna daripada dokumen tebal yang dibuat sekali setahun.",
                    "",
                    "Jebakan lain adalah berhenti di daftar ancaman. Daftar yang",
                    "nggak berubah jadi tugas di papan kerja tim akan dilupakan.",
                    "Tiap ancaman perlu pemilik, keputusan (kurangi, hindari,",
                    "alihkan, atau terima), dan tanggal.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Threat Dragon dan Microsoft Threat Modeling Tool sama-sama",
                    "menggambar diagram alir data lalu mengusulkan ancaman per benda",
                    "di diagram, memakai keenam kategori tadi. Di banyak tim,",
                    "sesi threat modeling jadi syarat sebelum fitur yang menyentuh",
                    "pembayaran atau data pribadi boleh mulai dikerjakan.",
                    "",
                    "Kasus kecil: timmu akan menambah fitur \"unggah foto profil\" di",
                    "aplikasi komunitas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Gambar: pengguna (entitas luar), aplikasi web (proses),",
                    "     folder unggahan (penyimpanan), dan panah di antaranya.",
                    "     Tandai batas kepercayaan antara pengguna dan aplikasi.",
                    "  2. Tanyakan keenam huruf. Contoh jawaban: berkas berisi skrip",
                    "     yang menyamar jadi gambar (T), foto pengguna lain bisa",
                    "     diunduh lewat nama berkas yang ditebak (I), berkas raksasa",
                    "     menghabiskan disk (D).",
                    "  3. Pilih penangkal: cek jenis berkas dari isinya, ganti nama",
                    "     berkas dengan nama acak, batasi ukuran, dan simpan di luar",
                    "     folder yang bisa dieksekusi.",
                    "  4. Masukkan tiap penangkal sebagai tugas, lengkap dengan",
                    "     pemiliknya.",
                ],
            },
        ],
    },
    {
        "title": "4. Secure SDLC: Keamanan di Setiap Tahap Pengembangan",
        "sections": [
            {
                "body": [
                    "SDLC (software development life cycle) adalah tahap-tahap",
                    "membuat perangkat lunak: menentukan kebutuhan, mendesain,",
                    "menulis kode, menguji, merilis, lalu mengoperasikan. Secure",
                    "SDLC berarti tiap tahap itu punya kegiatan keamanannya sendiri,",
                    "alih-alih satu pemeriksaan besar tepat sebelum rilis.",
                    "",
                    "Alasannya soal biaya. Celah yang ketahuan saat desain cukup",
                    "dibetulkan dengan menghapus satu kotak di diagram. Celah yang",
                    "ketahuan sesudah rilis harus dibetulkan di kode, diuji ulang,",
                    "dirilis ulang, dan mungkin datanya sudah keburu bocor. Gerakan",
                    "memindahkan pemeriksaan ke tahap lebih awal ini disebut shift",
                    "left, karena di garis waktu proyek, tahap awal ada di kiri.",
                ],
            },
            {
                "heading": "Kegiatan keamanan per tahap",
                "body": [
                    "  - Kebutuhan: tulis kebutuhan keamanan bersama fitur. Selain",
                    "    \"pengguna bisa reset password\", tulis juga abuse case,",
                    "    misalnya \"penyerang mencoba reset password orang lain\".",
                    "  - Desain: threat modeling, memilih cara login, menentukan",
                    "    data mana yang harus dienkripsi.",
                    "  - Kode: pedoman koding aman, code review yang ikut melihat",
                    "    sisi keamanan, dan pemindai rahasia supaya kunci API nggak",
                    "    ikut ter-commit.",
                    "  - Uji: tes untuk kasus jahat di samping kasus normal,",
                    "    analisis kode statis (SAST), dan pemindaian dependensi (SCA).",
                    "  - Rilis: konfigurasi produksi yang dikeraskan, artefak yang",
                    "    ditandatangani, dan rahasia yang diambil dari brankas.",
                    "  - Operasi: pembaruan rutin, pemantauan log, dan rencana",
                    "    respons insiden yang sudah pernah dilatih.",
                    "",
                    "Jangan kaget kalau banyak istilah di atas masih asing. Bab-bab",
                    "berikutnya membahasnya satu per satu, termasuk pemindai otomatis",
                    "di bab DevSecOps.",
                ],
            },
            {
                "heading": "Contoh kegiatan di tahap kode: daftar putih",
                "body": [
                    "Satu kebiasaan koding aman yang paling sering dipakai adalah",
                    "validasi masukan dengan daftar putih (allowlist). Daftar putih",
                    "menulis apa yang boleh, lalu menolak sisanya. Kebalikannya,",
                    "daftar hitam (blocklist), menulis apa yang dilarang lalu",
                    "menerima sisanya.",
                    "",
                    "Masalah daftar hitam: penyerang cuma perlu satu bentuk yang",
                    "lupa kamu larang. Program di bawah membandingkan keduanya untuk",
                    "username yang aturannya huruf kecil, angka, dan garis bawah,",
                    "diawali huruf, panjang 3 sampai 16.",
                ],
            },
            {
                "heading": "Daftar hitam lawan daftar putih",
                "code": "import re\n\nPOLA_USERNAME = re.compile(r\"[a-z][a-z0-9_]{2,15}\")\nDAFTAR_HITAM = [\"<\", \">\", \"'\", \";\", \"--\"]\n\n\ndef lolos_daftar_hitam(nama):\n    return not any(tanda in nama for tanda in DAFTAR_HITAM)\n\n\ndef lolos_daftar_putih(nama):\n    return POLA_USERNAME.fullmatch(nama) is not None\n\n\ncontoh = [\"budi_01\", \"ab\", \"budi<b>\", \"budi%27\", \"budi\\u202e\", \"Budi\"]\nfor nama in contoh:\n    hitam = \"lolos\" if lolos_daftar_hitam(nama) else \"ditolak\"\n    putih = \"lolos\" if lolos_daftar_putih(nama) else \"ditolak\"\n    print(f\"{nama!r:14} hitam: {hitam:8} putih: {putih}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  'budi_01'      hitam: lolos    putih: lolos",
                    "  'ab'           hitam: lolos    putih: ditolak",
                    "  'budi<b>'      hitam: ditolak  putih: ditolak",
                    "  'budi%27'      hitam: lolos    putih: ditolak",
                    "  'budi\\u202e'   hitam: lolos    putih: ditolak",
                    "  'Budi'         hitam: lolos    putih: ditolak",
                    "",
                    "Daftar hitam meloloskan budi%27, yaitu tanda kutip yang ditulis",
                    "dalam bentuk URL encoding. Ia juga meloloskan karakter U+202E,",
                    "karakter tak terlihat yang membalik arah tulisan dan pernah",
                    "dipakai untuk menyamarkan nama berkas. Daftar putih menolak",
                    "keduanya tanpa perlu tahu triknya, karena keduanya memang nggak",
                    "ada di daftar yang boleh.",
                    "",
                    "Ingat: pakai fullmatch, bukan match atau search. Fungsi match",
                    "cuma mengecek awal teks, jadi \"budi<script>\" tetap dianggap",
                    "cocok karena diawali \"budi\".",
                ],
            },
            {
                "heading": "Kerangka yang dipakai industri",
                "body": [
                    "Kamu nggak perlu menyusun daftar kegiatan dari nol. Beberapa",
                    "kerangka yang sering dirujuk:",
                    "",
                    "  - Secure Software Development Framework (SSDF), dokumen",
                    "    SP 800-218 dari NIST, lembaga standar Amerika Serikat. Isinya",
                    "    praktik yang dikelompokkan jadi empat: menyiapkan organisasi,",
                    "    melindungi perangkat lunak, membuat perangkat lunak yang",
                    "    aman, dan menanggapi kerentanan.",
                    "  - Software Assurance Maturity Model dari OWASP: model untuk",
                    "    mengukur seberapa matang praktik keamanan sebuah tim, dan apa",
                    "    langkah berikutnya.",
                    "  - Application Security Verification Standard dari OWASP:",
                    "    daftar persyaratan keamanan aplikasi web yang bisa dijadikan",
                    "    checklist saat desain dan pengujian.",
                    "  - Microsoft SDL: proses yang dipakai Microsoft sejak 2004 dan",
                    "    dipublikasikan untuk umum.",
                    "",
                    "OWASP (Open Worldwide Application Security Project) adalah",
                    "yayasan nirlaba yang juga menerbitkan daftar Top 10 risiko",
                    "aplikasi web. Daftar itu dibahas tersendiri di bab 4.",
                ],
            },
            {
                "heading": "Definisi selesai yang memuat keamanan",
                "bahasa": "teks",
                "code": """Fitur dianggap selesai kalau:
[ ] Ancaman di desainnya sudah dibahas (minimal 15 menit STRIDE)
[ ] Semua masukan divalidasi dengan daftar putih di server
[ ] Hak akses dicek di server untuk setiap permintaan
[ ] Ada tes untuk minimal satu kasus jahat
[ ] Pemindai dependensi dan rahasia di CI hijau
[ ] Kejadian penting (login, ubah peran, hapus data) tercatat di log
[ ] Pesan error ke pengguna nggak membocorkan detail teknis""",
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: menyerahkan semua urusan keamanan ke \"tim keamanan\"",
                    "di akhir proyek. Di tim kecil, tim itu sering nggak ada. Di tim",
                    "besar, mereka cuma sempat melihat sebagian kecil kode. Yang",
                    "paling tahu letak celah biasanya programmer yang menulisnya.",
                    "",
                    "Satu lagi: validasi di browser saja. Validasi JavaScript di",
                    "halaman web membantu pengguna mengisi form dengan benar, tapi",
                    "penyerang bisa mengirim permintaan langsung ke server tanpa",
                    "lewat halaman itu. Validasi yang menjaga keamanan selalu ada di",
                    "server.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kebocoran Equifax pada 2017 sering dipakai sebagai contoh",
                    "tahap operasi yang bolong. Celah di Apache Struts (CVE-2017-5638)",
                    "sudah punya tambalan sejak Maret 2017, tapi satu sistem Equifax",
                    "nggak kunjung diperbarui. Penyerang masuk lewat celah itu, dan",
                    "data pribadi sekitar 147 juta orang bocor. Celahnya sudah",
                    "dikenal luas. Yang bolong adalah proses yang memastikan",
                    "tambalan terpasang di semua server.",
                    "",
                    "Kasus kecil: timmu bertiga, tanpa anggaran alat berbayar, dan",
                    "ingin mulai menerapkan secure SDLC minggu ini.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tempel checklist \"definisi selesai\" di atas ke templat",
                    "     pull request di repositori.",
                    "  2. Tambahkan satu pertanyaan wajib di code review: \"masukan",
                    "     apa yang datang dari luar, dan di mana divalidasi?\"",
                    "  3. Nyalakan fitur gratis di platform repositorimu, misalnya",
                    "     peringatan dependensi rentan dan pemindai rahasia.",
                    "  4. Jadwalkan sesi threat modeling singkat tiap ada fitur yang",
                    "     menyentuh login, pembayaran, atau data pribadi.",
                    "  5. Catat semua server dan pustaka yang dipakai, lalu tetapkan",
                    "     satu hari tiap bulan untuk memperbaruinya.",
                ],
            },
        ],
    },
    {
        "title": "5. Hash, Checksum, dan Integritas Data",
        "sections": [
            {
                "body": [
                    "Kamu mengunduh berkas instalasi Linux sebesar 2 GB. Gimana",
                    "caranya tahu berkas itu sama persis dengan yang dibuat",
                    "pembuatnya? Bisa saja unduhannya rusak di tengah jalan, atau",
                    "lebih buruk, ada orang yang menukarnya dengan versi berisi",
                    "program jahat.",
                    "",
                    "Jawabannya fungsi hash. Fungsi hash menerima data sebesar apa",
                    "pun dan mengeluarkan deretan angka berukuran tetap, sering",
                    "disebut sidik jari atau digest. Ubah satu huruf saja di",
                    "datanya, sidiknya berubah total. Kalau sidik berkasmu sama",
                    "dengan sidik yang diumumkan pembuatnya, isinya sama.",
                    "",
                    "Hash yang dipakai untuk keamanan (hash kriptografis) punya tiga",
                    "sifat penting:",
                    "  - Satu arah: dari sidik, kamu nggak bisa menghitung balik",
                    "    datanya.",
                    "  - Tahan tabrakan: praktis mustahil menemukan dua data berbeda",
                    "    dengan sidik yang sama.",
                    "  - Efek longsor: perubahan kecil di data mengubah sekitar",
                    "    separuh bit sidiknya.",
                    "",
                    "Kamu sudah memakai hash setiap hari tanpa sadar. ID commit Git",
                    "adalah hash dari isi commit-nya. Layanan penyimpanan awan",
                    "memakai hash untuk mengenali berkas yang sama supaya nggak",
                    "disimpan dua kali. Dan aplikasi yang benar menyimpan hash",
                    "password, bukan password-nya, dengan cara khusus yang dibahas di",
                    "materi berikutnya.",
                ],
            },
            {
                "heading": "SHA-256 di Python",
                "code": """import hashlib

for teks in ["halo", "Halo", "halo!"]:
    sidik = hashlib.sha256(teks.encode("utf-8")).hexdigest()
    print(f"{teks:6} {sidik[:24]}...")

besar = b"x" * 1_000_000
print("panjang sidik 1 MB:", len(hashlib.sha256(besar).hexdigest()), "karakter hex")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  halo   a4e63bcacf6c172ad84f9f45...",
                    "  Halo   4e86512d9a0af8a743d42a1a...",
                    "  halo!  4e97e674b7166de709fa8a59...",
                    "  panjang sidik 1 MB: 64 karakter hex",
                    "",
                    "Satu huruf kapital atau satu tanda seru sudah membuat sidiknya",
                    "nggak mirip sama sekali. Teks empat huruf dan data satu juta",
                    "byte sama-sama menghasilkan 64 karakter heksadesimal, yaitu 256",
                    "bit. Dari situlah angka 256 di namanya.",
                    "",
                    "Perhatikan .encode(\"utf-8\"). Fungsi hash bekerja pada byte,",
                    "bukan pada teks. Kalau dua program meng-encode teks yang sama",
                    "dengan cara berbeda, sidiknya ikut berbeda.",
                ],
            },
            {
                "heading": "Algoritme mana yang masih aman",
                "body": [
                    "  Algoritme   Status (Oktober 2026)",
                    "  MD5         rusak sejak 2004; jangan untuk keamanan",
                    "  SHA-1       rusak; tabrakan nyata dibuat pada 2017",
                    "  SHA-256     aman, paling umum dipakai",
                    "  SHA-512     aman, keluaran lebih panjang",
                    "  SHA-3       aman, standar sejak 2015, desainnya beda dari SHA-2",
                    "  BLAKE2      aman dan cepat, ada di hashlib (blake2b, blake2s)",
                    "",
                    "Tabrakan SHA-1 pertama dipublikasikan peneliti Google dan CWI",
                    "Amsterdam pada 2017 dengan nama SHAttered: dua berkas PDF",
                    "berbeda dengan sidik SHA-1 yang sama. Sejak itu, sistem yang",
                    "memakai SHA-1 untuk tanda tangan atau sertifikat dianggap",
                    "rentan. MD5 dan SHA-1 masih boleh muncul untuk hal yang nggak",
                    "berurusan dengan penyerang, misalnya nama berkas cache.",
                    "",
                    "Ada juga checksum seperti CRC32 (zlib.crc32 di Python). Checksum",
                    "dirancang untuk mendeteksi kerusakan tak sengaja, misalnya bit",
                    "yang terbalik di kabel. Penyerang bisa dengan mudah membuat data",
                    "palsu dengan CRC32 yang sama, jadi checksum jenis ini bukan alat",
                    "keamanan.",
                ],
            },
            {
                "heading": "Hash saja belum cukup: HMAC",
                "body": [
                    "Hash membuktikan data nggak berubah, asal sidik pembandingnya",
                    "kamu dapat dari tempat tepercaya. Kalau penyerang bisa mengubah",
                    "pesan, ia juga bisa menghitung ulang sidiknya. SHA-256 bisa",
                    "dihitung siapa saja.",
                    "",
                    "HMAC (hash-based message authentication code) menambahkan kunci",
                    "rahasia ke perhitungannya. Hanya pihak yang memegang kunci yang",
                    "bisa membuat tanda yang benar. Contohnya webhook pembayaran:",
                    "server pembayaran memberi tahu tokomu bahwa pesanan sudah",
                    "lunas, dan tokomu harus yakin pesan itu nggak dipalsukan.",
                ],
            },
            {
                "heading": "Memeriksa pesan webhook",
                "code": """import hashlib
import hmac

KUNCI = b"kunci-webhook-contoh"  # di produksi: secrets.token_bytes(32), disimpan di brankas


def tanda(pesan):
    return hmac.new(KUNCI, pesan, hashlib.sha256).hexdigest()


# Server pembayaran mengirim pesan beserta tanda HMAC-nya.
pesan = b'{"order": 1532, "status": "lunas"}'
tanda_kiriman = tanda(pesan)

# Server toko memeriksa sebelum menandai pesanan lunas.
for isi in [pesan, b'{"order": 1533, "status": "lunas"}']:
    cocok = hmac.compare_digest(tanda(isi), tanda_kiriman)
    print(isi.decode(), "->", "terima" if cocok else "tolak")

# Hash biasa nggak menolong: siapa pun bisa menghitung ulang.
palsu = b'{"order": 1533, "status": "lunas"}'
print("sha256 polos bisa dihitung penyerang:", hashlib.sha256(palsu).hexdigest()[:16])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  {\"order\": 1532, \"status\": \"lunas\"} -> terima",
                    "  {\"order\": 1533, \"status\": \"lunas\"} -> tolak",
                    "  sha256 polos bisa dihitung penyerang: 623aa3b52d00c334",
                    "",
                    "Pesan yang nomor pesanannya diganti ditolak, karena tandanya",
                    "nggak cocok lagi dan penyerang nggak punya kunci untuk membuat",
                    "tanda baru.",
                    "",
                    "Jebakan: membandingkan tanda dengan ==. Operator itu berhenti",
                    "di karakter pertama yang beda, jadi waktunya sedikit berbeda",
                    "tergantung berapa karakter awal yang cocok. Dengan mengukur",
                    "waktu ribuan kali, penyerang bisa menebak tanda karakter demi",
                    "karakter. hmac.compare_digest selalu memakan waktu yang sama,",
                    "jadi celah itu tertutup.",
                ],
            },
            {
                "heading": "Memeriksa unduhan di terminal",
                "bahasa": "terminal",
                "code": """# Hitung sidik berkas yang baru diunduh
sha256sum Fedora-Workstation-Live-44.iso

# Cara yang lebih aman: periksa dulu tanda tangan berkas CHECKSUM,
# lalu cocokkan semua sidik di dalamnya. Nama berkas persisnya
# ada di halaman unduhan resmi.
gpgv --keyring ./fedora.gpg Fedora-Workstation-44-x86_64-CHECKSUM
sha256sum --ignore-missing -c Fedora-Workstation-44-x86_64-CHECKSUM""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Distribusi Linux seperti Fedora dan Ubuntu menerbitkan berkas",
                    "berisi sidik SHA-256 untuk tiap image instalasi, dan berkas itu",
                    "ditandatangani dengan kunci GPG proyeknya. GitHub memakai HMAC",
                    "untuk webhook: tiap kiriman membawa header X-Hub-Signature-256",
                    "berisi HMAC-SHA256 dari isi permintaan, dihitung dengan secret",
                    "yang kamu tentukan saat membuat webhook.",
                    "",
                    "Kasus kecil: kamu mengunduh installer aplikasi dari situs",
                    "cermin (mirror) karena situs utamanya lambat, lalu ragu",
                    "berkasnya asli.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ambil sidik SHA-256 resmi dari situs utama lewat HTTPS,",
                    "     bukan dari situs cermin tempat kamu mengunduh.",
                    "  2. Hitung sidik berkasmu dengan sha256sum, atau dengan Python:",
                    "       hashlib.sha256(open(nama, \"rb\").read()).hexdigest()",
                    "  3. Bandingkan seluruh 64 karakternya, jangan cuma beberapa",
                    "     karakter awal.",
                    "  4. Kalau proyeknya menyediakan tanda tangan GPG untuk berkas",
                    "     sidik, periksa juga tanda tangan itu.",
                    "  5. Kalau beda, hapus berkasnya dan unduh ulang dari sumber",
                    "     resmi. Jangan dijalankan \"untuk dicoba dulu\".",
                ],
            },
        ],
    },
    {
        "title": "6. Menyimpan Password: Salt, PBKDF2, bcrypt, dan Argon2",
        "sections": [
            {
                "body": [
                    "Anggap suatu hari database aplikasimu bocor. Ini bukan",
                    "skenario aneh. Backup yang salah taruh atau satu celah SQL",
                    "injection sudah cukup. Pertanyaannya: apa yang didapat penyerang",
                    "dari kolom password?",
                    "",
                    "Jawabannya tergantung cara kamu menyimpan password. Urutan dari",
                    "yang paling buruk:",
                    "",
                    "  1. Teks polos. Penyerang langsung punya semua password. Karena",
                    "     banyak orang memakai password yang sama di banyak tempat,",
                    "     akun email dan bank mereka ikut terancam.",
                    "  2. Dienkripsi. Kelihatannya aman, tapi kunci enkripsinya",
                    "     biasanya ada di server yang sama dan ikut bocor.",
                    "  3. Hash cepat seperti MD5 atau SHA-256 polos. Penyerang nggak",
                    "     bisa menghitung balik, tapi bisa menebak: hash jutaan",
                    "     password umum, lalu cocokkan.",
                    "  4. Hash cepat dengan salt. Lebih baik, tapi tebakannya masih",
                    "     murah.",
                    "  5. Hash khusus password yang sengaja lambat, dengan salt.",
                    "     Ini yang benar.",
                ],
            },
            {
                "heading": "Kenapa hash cepat itu masalah",
                "body": [
                    "SHA-256 dirancang supaya cepat, dan itu bagus untuk memeriksa",
                    "unduhan 2 GB. Untuk password, kecepatan itu berpihak ke",
                    "penyerang. Satu kartu grafis (GPU) bisa menghitung miliaran",
                    "SHA-256 per detik. Daftar password bocor yang beredar di",
                    "internet berisi ratusan juta password sungguhan, jadi password",
                    "seperti rahasia123 ketemu dalam sekejap.",
                    "",
                    "Masalah kedua: password yang sama menghasilkan hash yang sama.",
                    "Penyerang cukup menghitung hash sejuta password umum sekali,",
                    "lalu mencocokkannya ke semua database bocor. Tabel hasil",
                    "hitungan jadi seperti itu disebut rainbow table.",
                    "",
                    "Salt memecahkan masalah kedua. Salt adalah data acak yang dibuat",
                    "baru untuk tiap pengguna dan ikut disimpan di samping hash-nya.",
                    "Salt bukan rahasia. Gunanya membuat password yang sama",
                    "menghasilkan hash berbeda, sehingga tabel tebakan harus",
                    "dihitung ulang untuk tiap pengguna.",
                    "",
                    "Masalah pertama dipecahkan dengan fungsi yang sengaja lambat.",
                    "Login yang makan 0,1 detik nggak terasa bagi pengguna, tapi",
                    "membuat penyerang yang ingin mencoba semiliar tebakan butuh",
                    "waktu bertahun-tahun.",
                ],
            },
            {
                "heading": "PBKDF2 dari pustaka standar",
                "code": """import hashlib
import hmac

ITERASI = 600_000  # angka minimal OWASP untuk PBKDF2-HMAC-SHA256


def hash_password(password, salt):
    turunan = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERASI)
    return f"pbkdf2_sha256${ITERASI}${salt.hex()}${turunan.hex()}"


def cek_password(password, tersimpan):
    _, iterasi, salt_hex, hash_hex = tersimpan.split("$")
    turunan = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                                  bytes.fromhex(salt_hex), int(iterasi))
    return hmac.compare_digest(turunan.hex(), hash_hex)


# Cara salah: SHA-256 polos. Password sama, hash sama.
for nama in ["ani", "budi"]:
    print(nama, hashlib.sha256(b"rahasia123").hexdigest()[:16])

# Cara benar: salt acak per pengguna. Salt di sini dipatok supaya
# keluarannya bisa dicocokkan; di produksi pakai secrets.token_bytes(16).
salt_ani = bytes.fromhex("9f3c2a7d51e04b8a")
salt_budi = bytes.fromhex("04d1e6b2a9c87f35")
akun = {
    "ani": hash_password("rahasia123", salt_ani),
    "budi": hash_password("rahasia123", salt_budi),
}
for nama, tersimpan in akun.items():
    algoritme, iterasi, salt, nilai = tersimpan.split("$")
    print(nama, algoritme, iterasi, salt, nilai[:16])

print("login ani benar:", cek_password("rahasia123", akun["ani"]))
print("login ani salah:", cek_password("rahasia124", akun["ani"]))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ani bee5688aea66a474",
                    "  budi bee5688aea66a474",
                    "  ani pbkdf2_sha256 600000 9f3c2a7d51e04b8a 6f664df3df28d2a9",
                    "  budi pbkdf2_sha256 600000 04d1e6b2a9c87f35 70eed21b6404af5b",
                    "  login ani benar: True",
                    "  login ani salah: False",
                    "",
                    "Dua baris pertama membocorkan bahwa Ani dan Budi memakai",
                    "password yang sama. Dengan salt, hash keduanya nggak mirip.",
                    "",
                    "Format algoritme$iterasi$salt$hash menyimpan semua yang",
                    "dibutuhkan untuk memeriksa ulang. Saat angka iterasi dinaikkan",
                    "tahun depan, hash lama tetap bisa diperiksa karena iterasinya",
                    "tercatat di situ. Django memakai format yang mirip.",
                ],
            },
            {
                "heading": "bcrypt, scrypt, dan Argon2",
                "body": [
                    "PBKDF2 aman kalau iterasinya cukup, tapi ia cuma membebani",
                    "prosesor. Penyerang dengan GPU atau chip khusus masih bisa",
                    "menjalankan banyak tebakan sekaligus. Algoritme yang lebih baru",
                    "juga membebani memori, dan memori jauh lebih mahal untuk",
                    "dikalikan ribuan kali.",
                    "",
                    "  - bcrypt (1999): masih banyak dipakai, faktor kerja minimal 10",
                    "    menurut OWASP. Batasnya, password cuma dibaca sampai 72 byte.",
                    "    Paket bcrypt versi 5.0 untuk Python menolak password lebih",
                    "    panjang dari itu dengan ValueError, alih-alih memotongnya",
                    "    tanpa bilang-bilang seperti versi lama.",
                    "  - scrypt: membebani memori, dan sudah tersedia di pustaka",
                    "    standar sebagai hashlib.scrypt.",
                    "  - Argon2id: pemenang Password Hashing Competition 2015 dan",
                    "    distandarkan sebagai RFC 9106 pada 2021. Ini pilihan pertama",
                    "    yang disarankan OWASP Password Storage Cheat Sheet untuk",
                    "    aplikasi baru.",
                    "",
                    "Angka minimal dari cheat sheet itu saat materi ini ditulis",
                    "(Oktober 2026):",
                    "  - Argon2id: memori 19 MiB, 2 iterasi, 1 jalur paralel.",
                    "  - scrypt: N=2^17, r=8, p=1.",
                    "  - bcrypt: faktor kerja 10.",
                    "  - PBKDF2-HMAC-SHA256: 600.000 iterasi.",
                    "",
                    "Pustaka standar Python nggak punya bcrypt maupun Argon2. Untuk",
                    "keduanya pakai paket yang sudah teruji, dan jangan pernah",
                    "menulis algoritme hash password sendiri.",
                ],
            },
            {
                "heading": "Argon2id dengan paket argon2-cffi",
                "code": """from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()  # bawaan: Argon2id, profil RFC 9106 hemat memori
tersimpan = ph.hash("kopi-susu-gula-aren")
print(tersimpan[:30] + "...")  # $argon2id$v=19$m=65536,t=3,p=4...

try:
    ph.verify(tersimpan, "tebakan-salah")
except VerifyMismatchError:
    print("password salah")

print(ph.verify(tersimpan, "kopi-susu-gula-aren"))  # True
print(ph.check_needs_rehash(tersimpan))  # True kalau parameter sudah usang""",
            },
            {
                "body": [
                    "String hasilnya memuat nama algoritme, versinya, dan",
                    "parameternya: m=65536 berarti 64 MiB memori, t=3 berarti tiga",
                    "putaran, p=4 berarti empat jalur. Salt acaknya dibuat otomatis",
                    "dan ikut tersimpan di string itu.",
                    "",
                    "Satu lapis tambahan yang kadang dipakai adalah pepper: kunci",
                    "rahasia yang sama untuk semua password dan disimpan terpisah",
                    "dari database, misalnya di brankas rahasia. Database yang bocor",
                    "tanpa pepper-nya jadi jauh lebih susah ditebak.",
                    "",
                    "Ingat: jangan membatasi panjang password terlalu pendek atau",
                    "melarang karakter tertentu. Hash selalu menghasilkan panjang",
                    "yang sama, jadi password 40 karakter nggak membuat kolom",
                    "database membengkak.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pada 2012, sekitar 6,5 juta hash password LinkedIn tersebar di",
                    "internet. Hash-nya SHA-1 tanpa salt, sehingga sebagian besar",
                    "cepat ditebak. Pada 2016 ternyata yang bocor jauh lebih banyak,",
                    "sekitar 117 juta akun. Kasus Adobe 2013 menunjukkan jebakan yang",
                    "lain: password di sana dienkripsi, bukan di-hash, dan petunjuk",
                    "password yang ikut bocor membantu orang menebak isinya.",
                    "",
                    "Kasus kecil: kamu mewarisi aplikasi lama yang menyimpan password",
                    "sebagai MD5 polos, dan pengguna nggak boleh dipaksa reset",
                    "password semuanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambah kolom yang mencatat algoritme tiap baris, misalnya",
                    "     md5 atau argon2id.",
                    "  2. Hari ini juga, bungkus semua hash lama: simpan",
                    "       argon2id(md5_lama)",
                    "     dan tandai barisnya md5+argon2id. Hash MD5 telanjang hilang",
                    "     dari database tanpa perlu password aslinya.",
                    "  3. Saat pengguna login dengan benar, kamu memegang password",
                    "     aslinya sesaat. Ganti hash-nya jadi argon2id(password) murni.",
                    "  4. Sesudah beberapa bulan, minta reset password hanya untuk",
                    "     akun yang masih memakai bentuk bungkusan.",
                    "  5. Pastikan password nggak pernah masuk log, termasuk log",
                    "     error dan log permintaan.",
                ],
            },
        ],
    },
    {
        "title": "7. Enkripsi Simetris, Asimetris, dan Tanda Tangan Digital",
        "sections": [
            {
                "body": [
                    "Hash itu satu arah. Enkripsi dua arah: data diacak dengan",
                    "kunci, lalu bisa dikembalikan dengan kunci yang tepat. Data",
                    "aslinya disebut plaintext, hasil acakannya ciphertext.",
                    "",
                    "Ada dua keluarga besar enkripsi, dan bedanya ada di kunci:",
                    "  - Simetris: satu kunci yang sama untuk mengunci dan membuka.",
                    "    Seperti gembok angka yang kodenya kamu bagi ke teman.",
                    "  - Asimetris: sepasang kunci. Kunci publik boleh disebar ke",
                    "    siapa saja, kunci privat disimpan sendiri. Apa yang dikunci",
                    "    dengan kunci publik cuma bisa dibuka kunci privat",
                    "    pasangannya. Seperti kotak surat: semua orang bisa",
                    "    memasukkan surat, tapi cuma pemilik kunci yang bisa",
                    "    mengambilnya.",
                ],
            },
            {
                "heading": "Simetris: cepat, tapi kuncinya harus dibagi",
                "body": [
                    "Algoritme simetris standar saat ini adalah AES (Advanced",
                    "Encryption Standard). Ia dipakai di hampir semua tempat: HTTPS,",
                    "enkripsi disk, Wi-Fi, aplikasi pesan. Kuncinya 128 atau 256 bit.",
                    "Prosesor modern punya instruksi khusus untuknya, jadi",
                    "enkripsinya ringan.",
                    "",
                    "Algoritme saja belum cukup. Cara menerapkannya ke data panjang",
                    "disebut mode. Mode yang disarankan sekarang adalah GCM, yang",
                    "sekaligus mengenkripsi dan memeriksa keaslian. Kalau ciphertext",
                    "diubah satu bit, proses buka langsung gagal. Mode lama bernama",
                    "ECB mengenkripsi tiap blok terpisah, sehingga blok yang sama",
                    "menghasilkan sandi yang sama dan pola gambar tetap kelihatan.",
                    "ChaCha20-Poly1305 adalah pilihan setara yang cepat di ponsel",
                    "tanpa instruksi khusus AES.",
                    "",
                    "Masalah besar simetris adalah membagi kuncinya. Kalau kamu dan",
                    "temanmu belum pernah ketemu, bagaimana kode gemboknya sampai ke",
                    "dia tanpa ikut terbaca orang lain? Dan makin banyak orang,",
                    "makin banyak kunci yang harus dikelola.",
                ],
            },
            {
                "heading": "Berapa banyak kunci yang dibutuhkan",
                "code": """print(" orang   kunci bersama   pasangan kunci")
for n in [2, 10, 100, 1000]:
    simetris = n * (n - 1) // 2   # satu kunci untuk tiap pasang orang
    asimetris = n                 # satu pasangan kunci per orang
    print(f"{n:>6}   {simetris:>13}   {asimetris:>14}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "   orang   kunci bersama   pasangan kunci",
                    "       2               1                2",
                    "      10              45               10",
                    "     100            4950              100",
                    "    1000          499500             1000",
                    "",
                    "Seribu orang yang ingin bisa saling berkirim pesan rahasia",
                    "butuh hampir setengah juta kunci simetris. Dengan kunci",
                    "asimetris, cukup seribu pasang: tiap orang mengumumkan kunci",
                    "publiknya.",
                ],
            },
            {
                "heading": "Asimetris dan cara HTTPS menggabungkannya",
                "body": [
                    "Algoritme asimetris yang umum:",
                    "  - RSA (1977): masih paling banyak dipakai. Panjang kunci",
                    "    minimal yang wajar sekarang 2048 bit.",
                    "  - Kriptografi kurva eliptik: kuncinya jauh lebih pendek untuk",
                    "    kekuatan setara. X25519 dipakai untuk bertukar kunci, Ed25519",
                    "    untuk tanda tangan, dan P-256 banyak dipakai di sertifikat.",
                    "",
                    "Asimetris jauh lebih lambat daripada simetris. Karena itu",
                    "praktiknya selalu hibrida. Saat browser membuka situs HTTPS,",
                    "keduanya memakai pertukaran kunci asimetris untuk menyepakati",
                    "kunci sesi secara rahasia, lalu seluruh data dienkripsi dengan",
                    "kunci sesi itu, memakai mode GCM atau ChaCha20-Poly1305.",
                    "",
                    "Satu perubahan yang sedang berjalan: komputer kuantum di masa",
                    "depan diperkirakan bisa memecahkan RSA dan kurva eliptik. Badan",
                    "standar Amerika Serikat (NIST) menerbitkan standar pengganti pada",
                    "Agustus 2024, salah satunya ML-KEM untuk pertukaran kunci.",
                    "Browser besar dan OpenSSH 10.0 sudah memakai gabungan X25519",
                    "dengan algoritme baru itu secara bawaan, supaya data yang",
                    "direkam hari ini tetap aman nanti.",
                ],
            },
            {
                "heading": "Tanda tangan digital",
                "body": [
                    "Pasangan kunci juga bisa dipakai terbalik. Pemilik menandatangani",
                    "data dengan kunci privatnya, dan siapa pun memeriksanya dengan",
                    "kunci publik. Kalau pemeriksaan berhasil, dua hal terbukti: data",
                    "itu dibuat pemegang kunci privat, dan isinya nggak berubah",
                    "sejak ditandatangani.",
                    "",
                    "Bedanya dengan HMAC: HMAC memakai satu kunci bersama, jadi siapa",
                    "pun yang bisa memeriksa juga bisa memalsukan. Tanda tangan",
                    "digital bisa diperiksa jutaan orang tanpa satu pun bisa",
                    "memalsukannya. Karena sifat itu, pembaruan aplikasi, paket",
                    "Linux, dan sertifikat HTTPS memakai tanda tangan digital.",
                    "",
                    "Pustaka standar Python nggak menyediakan enkripsi simetris",
                    "maupun tanda tangan digital. Paket yang lazim dipakai adalah",
                    "cryptography. Kedua",
                    "contoh di bawah butuh paket itu.",
                ],
            },
            {
                "heading": "AES-GCM dengan paket cryptography",
                "code": """import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

kunci = AESGCM.generate_key(bit_length=256)  # simpan di KMS atau brankas
aes = AESGCM(kunci)
nonce = os.urandom(12)                       # wajib baru untuk tiap pesan
sandi = aes.encrypt(nonce, b"nomor rekening 1234567890", b"pesanan-1532")
print(len(sandi))                            # 41: 25 byte isi + 16 byte tag
print(aes.decrypt(nonce, sandi, b"pesanan-1532"))""",
            },
            {
                "heading": "Tanda tangan Ed25519",
                "code": """from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

kunci_privat = Ed25519PrivateKey.generate()   # disimpan pemilik, nggak dibagi
kunci_publik = kunci_privat.public_key()      # boleh dibagikan ke siapa saja

pesan = b"rilis aplikasi versi 2.4.1"
tanda = kunci_privat.sign(pesan)
print(len(tanda))                             # tanda tangan Ed25519: 64 byte

kunci_publik.verify(tanda, pesan)             # diam berarti cocok
try:
    kunci_publik.verify(tanda, b"rilis aplikasi versi 2.4.2")
except InvalidSignature:
    print("tanda tangan nggak cocok")""",
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: memakai ulang nonce di mode GCM. Nonce adalah angka",
                    "yang wajib berbeda untuk tiap pesan dengan kunci yang sama.",
                    "Memakai nonce yang sama dua kali bisa membocorkan isi pesan dan",
                    "membuat penyerang bisa memalsukan tag. Di contoh atas, nonce",
                    "diambil dari os.urandom, dan harus disimpan bersama ciphertext",
                    "karena dibutuhkan saat membuka.",
                    "",
                    "Jebakan kedua: merancang skema enkripsi sendiri, misalnya XOR",
                    "dengan kata sandi atau base64 yang dianggap \"diacak\". Base64",
                    "cuma cara menulis byte sebagai huruf, siapa pun bisa",
                    "membaliknya. Pakai pustaka yang sudah teruji dan resep yang",
                    "sudah jadi.",
                ],
            },
            {
                "heading": "Membuat pasangan kunci di terminal",
                "bahasa": "terminal",
                "code": """# Kunci SSH untuk login ke server atau push ke GitHub
ssh-keygen -t ed25519 -C "ani@laptop"

# Mengirim berkas terenkripsi ke teman dengan age
age-keygen -o kunci-ani.txt          # mencetak kunci publik Ani
age -r age1contohkuncipublikteman... -o laporan.pdf.age laporan.pdf
age -d -i kunci-ani.txt laporan-dari-teman.pdf.age > laporan.pdf""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap kali kamu membuka situs HTTPS, TLS 1.3 menjalankan",
                    "pertukaran kunci asimetris, memeriksa tanda tangan di",
                    "sertifikat situs, lalu mengenkripsi lalu lintasnya dengan",
                    "enkripsi simetris. WhatsApp memakai Signal Protocol untuk",
                    "enkripsi ujung ke ujung, yang menggabungkan kurva eliptik untuk",
                    "menyepakati kunci dengan enkripsi simetris untuk isi pesannya.",
                    "",
                    "Kasus kecil: kamu harus mengirim berkas berisi data pelanggan ke",
                    "rekan kerja lewat email.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Minta rekanmu membuat pasangan kunci, misalnya dengan",
                    "     age-keygen, lalu mengirim kunci publiknya ke kamu. Kunci",
                    "     privatnya tetap di laptopnya.",
                    "  2. Pastikan kunci publik itu benar miliknya, misalnya dengan",
                    "     mengecek beberapa karakternya lewat telepon.",
                    "  3. Enkripsi berkasnya dengan kunci publik itu, lalu kirim",
                    "     berkas .age-nya lewat email.",
                    "  4. Hanya rekanmu yang bisa membukanya, walau emailnya terbaca",
                    "     orang lain.",
                    "  5. Sesudah selesai dipakai, hapus salinan berkas aslinya dari",
                    "     folder unduhan.",
                ],
            },
        ],
    },
    {
        "title": "8. Sertifikat, PKI, dan Manajemen Kunci",
        "sections": [
            {
                "body": [
                    "Kunci publik memecahkan masalah berbagi kunci, tapi memunculkan",
                    "masalah baru. Waktu browsermu menerima kunci publik dari",
                    "bank.example, bagaimana ia tahu kunci itu benar milik bank, dan",
                    "bukan milik orang yang menyadap Wi-Fi kafe?",
                    "",
                    "Jawabannya sertifikat. Sertifikat adalah dokumen digital yang",
                    "berbunyi kira-kira \"kunci publik ini milik bank.example\", lalu",
                    "ditandatangani pihak yang dipercaya browser, yaitu certificate",
                    "authority (CA). Seluruh sistem CA, sertifikat, dan aturan",
                    "kepercayaannya disebut PKI (public key infrastructure).",
                    "",
                    "Analoginya KTP. Polisi percaya namamu karena KTP-mu diterbitkan",
                    "pemerintah, bukan karena kamu sendiri yang bilang.",
                ],
            },
            {
                "heading": "Isi sertifikat X.509",
                "body": [
                    "Sertifikat di web memakai format X.509. Medan yang paling",
                    "sering kamu baca:",
                    "  - Subject: pemilik sertifikat.",
                    "  - Subject Alternative Name: daftar nama domain yang sah untuk",
                    "    sertifikat ini. Browser memeriksa medan ini, bukan Subject.",
                    "  - Issuer: CA yang menandatangani.",
                    "  - Not Before dan Not After: rentang masa berlaku.",
                    "  - Public Key: kunci publik pemilik.",
                    "  - Signature: tanda tangan digital dari Issuer.",
                ],
            },
            {
                "heading": "Melihat sertifikat dengan openssl",
                "bahasa": "terminal",
                "code": """# Membaca berkas sertifikat
openssl x509 -in situs.pem -noout -subject -issuer -dates -ext subjectAltName

# Mengambil rantai sertifikat dari server milikmu sendiri
openssl s_client -connect tokokecil.example:443 -servername tokokecil.example -showcerts </dev/null

# Menguji perpanjangan otomatis Let's Encrypt tanpa benar-benar memperpanjang
sudo certbot renew --dry-run""",
            },
            {
                "heading": "Rantai kepercayaan",
                "body": [
                    "CA utama (root CA) jarang menandatangani sertifikat situs",
                    "langsung. Kunci privat root disimpan offline dan dijaga ketat.",
                    "Root menandatangani sertifikat CA perantara (intermediate), dan",
                    "intermediate itulah yang menandatangani sertifikat situs.",
                    "",
                    "Browser dan sistem operasi membawa daftar root yang dipercaya,",
                    "disebut root store. Mozilla, Microsoft, Apple, dan Google",
                    "masing-masing mengelola root store sendiri. Saat menerima",
                    "sertifikat situs, browser menelusuri rantainya ke atas sampai",
                    "ketemu root yang ada di daftarnya, sambil memeriksa tanda",
                    "tangan dan masa berlaku di tiap mata rantai.",
                    "",
                    "Program di bawah meniru penelusuran itu tanpa kriptografi,",
                    "cukup untuk melihat logikanya.",
                ],
            },
            {
                "heading": "Menelusuri rantai sertifikat",
                "code": """from datetime import date

hari_ini = date(2026, 10, 19)  # dipatok supaya hasilnya selalu sama

# nama -> (penerbit, tanggal berakhir)
sertifikat = {
    "tokokecil.example": ("Contoh CA R1", date(2026, 11, 2)),
    "Contoh CA R1": ("Contoh Root X1", date(2029, 3, 1)),
    "Contoh Root X1": ("Contoh Root X1", date(2035, 6, 1)),
}
root_tepercaya = {"Contoh Root X1"}  # bawaan sistem operasi atau browser


def periksa_rantai(nama):
    for _ in range(5):  # rantai yang kelewat panjang dianggap rusak
        penerbit, berakhir = sertifikat[nama]
        sisa = (berakhir - hari_ini).days
        catatan = "kedaluwarsa" if sisa < 0 else f"{sisa} hari lagi"
        if 0 <= sisa < 30:
            catatan += ", segera perpanjang"
        print(f"  {nama} (oleh {penerbit}): {catatan}")
        if sisa < 0:
            return False
        if nama == penerbit:
            return nama in root_tepercaya
        nama = penerbit
    return False


print("Rantai untuk tokokecil.example:")
print("Hasil:", "tepercaya" if periksa_rantai("tokokecil.example") else "ditolak")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Rantai untuk tokokecil.example:",
                    "    tokokecil.example (oleh Contoh CA R1): 14 hari lagi, segera perpanjang",
                    "    Contoh CA R1 (oleh Contoh Root X1): 864 hari lagi",
                    "    Contoh Root X1 (oleh Contoh Root X1): 3147 hari lagi",
                    "  Hasil: tepercaya",
                    "",
                    "Root menandatangani dirinya sendiri, jadi ia dipercaya semata",
                    "karena ada di root store. Sertifikat situs yang tinggal 14 hari",
                    "harus segera diperpanjang. Situs dengan sertifikat kedaluwarsa",
                    "langsung menampilkan halaman peringatan merah di browser.",
                ],
            },
            {
                "heading": "Masa berlaku makin pendek",
                "body": [
                    "Let's Encrypt menerbitkan sertifikat gratis lewat protokol",
                    "otomatis, misalnya dengan alat certbot. Sertifikatnya berlaku 90",
                    "hari, dan sedang diperpendek bertahap. Menurut pengumuman",
                    "resminya:",
                    "  - Sejak 13 Mei 2026, profil opsional tlsserver berlaku 45 hari.",
                    "  - Pada 10 Februari 2027, profil bawaan turun ke 64 hari.",
                    "  - Pada 16 Februari 2028, profil bawaan turun ke 45 hari.",
                    "",
                    "Ini bagian dari aturan industri. CA/Browser Forum adalah forum",
                    "tempat CA dan pembuat browser menyepakati aturan. Pada 2025",
                    "forum itu memutuskan masa berlaku maksimal sertifikat publik",
                    "turun bertahap mulai Maret 2026, dari 398 hari sampai tinggal 47",
                    "hari pada Maret 2029. Akibatnya, perpanjangan manual setahun",
                    "sekali sudah nggak mungkin lagi. Semua harus otomatis.",
                    "",
                    "Mekanisme pengaman lain adalah Certificate Transparency. Tiap",
                    "sertifikat publik dicatat di log terbuka, jadi pemilik domain",
                    "bisa mengecek (misalnya lewat crt.sh) apakah ada sertifikat",
                    "untuk domainnya yang nggak pernah ia minta.",
                ],
            },
            {
                "heading": "Manajemen kunci di produksi",
                "body": [
                    "Kriptografi cuma sekuat penyimpanan kuncinya. Kunci enkripsi yang",
                    "ditulis di kode program akan ikut ter-commit ke Git dan bocor",
                    "bersama repositorinya. Di produksi, kunci dikelola layanan",
                    "khusus yang disebut KMS (key management service): AWS KMS,",
                    "Google Cloud KMS, atau Azure Key Vault. Di bawahnya biasanya ada",
                    "HSM (hardware security module), perangkat keras yang membuat",
                    "dan memakai kunci tanpa pernah mengeluarkannya.",
                    "",
                    "Pola yang umum disebut envelope encryption:",
                    "  1. Aplikasi meminta KMS membuat data key, yaitu kunci",
                    "     simetris untuk mengenkripsi data.",
                    "  2. Data dienkripsi dengan data key itu di aplikasi.",
                    "  3. Data key dienkripsi oleh master key yang nggak pernah",
                    "     keluar dari KMS, lalu disimpan di samping datanya.",
                    "  4. Untuk membuka, aplikasi meminta KMS membuka data key.",
                    "     Setiap permintaan itu tercatat di log audit.",
                    "",
                    "Rotasi kunci berarti mengganti kunci secara berkala atau saat",
                    "dicurigai bocor. Dengan envelope encryption, merotasi master key",
                    "cukup mengenkripsi ulang data key yang kecil, bukan seluruh",
                    "data. Brankas rahasia seperti Vault dibahas di bab 6.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pada 2023, kelompok yang dijuluki Storm-0558 memakai kunci",
                    "penandatangan milik Microsoft untuk memalsukan token login, lalu",
                    "membaca email sekitar 25 organisasi, termasuk lembaga pemerintah",
                    "Amerika Serikat. Laporan Cyber Safety Review Board tahun 2024",
                    "menyoroti kunci tua yang masih dipercaya sistem dan rotasi",
                    "kunci yang terhenti. Kasus DigiNotar pada 2011 menunjukkan sisi",
                    "lain: CA Belanda itu dibobol, sertifikat palsu untuk domain",
                    "Google diterbitkan, dan browser mencabut kepercayaan padanya",
                    "sampai perusahaannya bangkrut.",
                    "",
                    "Kasus kecil: situs toko temanmu tiba-tiba menampilkan",
                    "peringatan \"koneksi tidak aman\" di semua browser.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Periksa tanggal Not After sertifikatnya dengan openssl",
                    "     x509 -dates, atau klik ikon gembok di browser.",
                    "  2. Kalau kedaluwarsa, perpanjang sekarang (misalnya certbot",
                    "     renew) dan muat ulang server web.",
                    "  3. Cari tahu kenapa perpanjangan otomatisnya gagal: timer",
                    "     yang mati, port 80 yang tertutup, atau DNS yang berubah.",
                    "  4. Pasang pemantau yang memberi peringatan 14 hari sebelum",
                    "     kedaluwarsa, seperti program penelusur rantai di atas.",
                    "  5. Uji perpanjangan otomatis dengan --dry-run tiap kali",
                    "     konfigurasi server diubah.",
                ],
            },
        ],
    },
    {
        "title": "9. Autentikasi: Password, MFA, dan Passkey",
        "sections": [
            {
                "body": [
                    "Dua kata ini sering tertukar, jadi kita bereskan dulu:",
                    "  - Autentikasi menjawab \"kamu siapa?\". Contohnya login.",
                    "  - Otorisasi menjawab \"kamu boleh apa?\". Contohnya pembeli",
                    "    biasa nggak boleh membuka halaman admin.",
                    "",
                    "Materi ini membahas autentikasi. Otorisasi dapat materinya",
                    "sendiri di akhir bab.",
                    "",
                    "Untuk membuktikan diri, pengguna menunjukkan satu atau lebih",
                    "faktor. Ada tiga jenis faktor:",
                    "  - Sesuatu yang kamu tahu: password, PIN, jawaban pertanyaan",
                    "    rahasia.",
                    "  - Sesuatu yang kamu punya: ponsel berisi aplikasi",
                    "    autentikator, kunci keamanan USB, kartu.",
                    "  - Sesuatu yang melekat padamu: sidik jari, wajah.",
                    "",
                    "MFA (multi-factor authentication) berarti memakai minimal dua",
                    "jenis faktor yang berbeda. Password ditambah kode angka belum MFA,",
                    "karena keduanya sama-sama sesuatu yang kamu tahu dan bisa",
                    "dicuri dengan cara yang sama.",
                ],
            },
            {
                "heading": "Aturan password yang berlaku sekarang",
                "body": [
                    "Banyak aturan password lama justru membuat password lebih",
                    "lemah. Aturan \"wajib huruf besar, angka, dan simbol, ganti tiap",
                    "90 hari\" menghasilkan password seperti Rahasia1! yang diganti",
                    "jadi Rahasia2! tiga bulan kemudian.",
                    "",
                    "Pedoman SP 800-63B revisi 4 dari NIST (lembaga standar Amerika",
                    "Serikat), terbit final pada Agustus 2025, mengubah arah itu:",
                    "  - Panjang minimal 15 karakter kalau password jadi satu-satunya",
                    "    faktor, dan 8 karakter kalau ia bagian dari MFA.",
                    "  - Dilarang mewajibkan campuran jenis karakter.",
                    "  - Dilarang memaksa ganti password berkala. Ganti hanya kalau",
                    "    ada tanda password itu bocor.",
                    "  - Wajib menolak password yang ada di daftar password umum",
                    "    atau password yang pernah bocor.",
                    "",
                    "Untuk mengecek password bocor tanpa mengirim password-nya,",
                    "layanan Pwned Passwords memakai trik k-anonymity. Aplikasimu",
                    "cuma mengirim 5 karakter awal hash SHA-1 password, lalu",
                    "menerima ratusan hash berawalan sama dan mencocokkan sisanya",
                    "sendiri. Layanan itu nggak pernah tahu password mana yang dicek.",
                    "",
                    "Satu lagi: izinkan paste di kolom password. Pengelola password",
                    "(password manager) bekerja dengan menempelkan password panjang",
                    "yang acak, dan itulah jenis password terbaik.",
                ],
            },
            {
                "heading": "Kode sekali pakai dari aplikasi autentikator",
                "body": [
                    "Aplikasi seperti Google Authenticator, Microsoft Authenticator,",
                    "atau Aegis menampilkan kode enam angka yang berganti tiap 30",
                    "detik. Namanya TOTP (time-based one-time password), standar RFC",
                    "6238. Cara kerjanya sederhana:",
                    "  1. Saat kamu memindai kode QR, server dan ponselmu menyimpan",
                    "     rahasia yang sama.",
                    "  2. Tiap 30 detik, keduanya menghitung HMAC dari rahasia itu",
                    "     dan nomor urut jendela waktu sekarang.",
                    "  3. Hasilnya dipotong jadi enam angka. Kalau angkamu sama",
                    "     dengan hitungan server, kamu lolos.",
                    "",
                    "Ponselnya nggak perlu internet, karena yang dibutuhkan cuma",
                    "rahasia dan jam. Program di bawah menghitung TOTP dengan",
                    "pustaka standar, memakai contoh resmi dari RFC-nya.",
                ],
            },
            {
                "heading": "Menghitung TOTP",
                "code": """import hashlib
import hmac
import struct


def totp(rahasia, waktu, langkah=30, digit=6):
    pencacah = waktu // langkah                       # berganti tiap 30 detik
    pesan = struct.pack(">Q", pencacah)               # 8 byte, big-endian
    hasil = hmac.new(rahasia, pesan, hashlib.sha1).digest()
    geser = hasil[-1] & 0x0F                          # "dynamic truncation"
    angka = struct.unpack(">I", hasil[geser:geser + 4])[0] & 0x7FFFFFFF
    return str(angka % 10 ** digit).zfill(digit)


# Rahasia contoh dari RFC 6238. Aplikasi sungguhan membuat rahasia acak
# saat pengguna memindai kode QR, lalu menyimpannya di kedua sisi.
rahasia = b"12345678901234567890"
for waktu in [59, 89, 1111111109, 1234567890]:
    print(f"detik {waktu:>10}: {totp(rahasia, waktu)}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  detik         59: 287082",
                    "  detik         89: 359152",
                    "  detik 1111111109: 081804",
                    "  detik 1234567890: 005924",
                    "",
                    "Detik 59 dan 89 jatuh di jendela 30 detik yang berbeda, jadi",
                    "kodenya berbeda. Angka 287082, 081804, dan 005924 sama dengan",
                    "enam digit terakhir tabel contoh di RFC 6238. Perhatikan zfill:",
                    "kode boleh diawali nol, jadi harus disimpan sebagai teks.",
                    "",
                    "Di aplikasi sungguhan, pakai pustaka yang sudah teruji, di",
                    "Python misalnya pyotp. Lalu tambahkan dua hal. Terima juga kode",
                    "dari satu jendela sebelum dan sesudahnya, untuk jam yang sedikit",
                    "meleset. Dan tolak kode yang sudah pernah dipakai.",
                ],
            },
            {
                "heading": "Kenapa SMS OTP paling lemah",
                "body": [
                    "Kode lewat SMS masih jauh lebih baik daripada password saja,",
                    "tapi ia faktor kedua yang paling lemah:",
                    "  - SIM swap: penipu meyakinkan gerai operator untuk",
                    "    memindahkan nomormu ke kartu miliknya, lalu semua SMS masuk",
                    "    ke dia.",
                    "  - Halaman phishing bisa meminta kode SMS dan langsung",
                    "    memakainya di situs asli dalam hitungan detik.",
                    "  - SMS bisa terbaca di layar kunci ponsel.",
                    "",
                    "Pedoman tadi menandai autentikasi lewat jaringan telepon sebagai",
                    "\"restricted\": boleh, tapi dengan syarat tambahan dan jalur",
                    "lain yang ditawarkan.",
                    "",
                    "Notifikasi push (\"Apakah ini kamu? Ya / Tidak\") punya jebakan",
                    "lain bernama MFA fatigue. Penyerang yang sudah tahu password",
                    "mengirim notifikasi berulang-ulang sampai korban menekan Ya",
                    "karena kesal. Penangkalnya number matching: layar login",
                    "menampilkan angka, dan pengguna harus mengetik angka itu di",
                    "ponselnya.",
                ],
            },
            {
                "heading": "Passkey: login tanpa password yang tahan phishing",
                "body": [
                    "Passkey memakai standar FIDO2 dan WebAuthn. Saat mendaftar,",
                    "perangkatmu membuat pasangan kunci khusus untuk satu situs.",
                    "Kunci publik dikirim ke server, kunci privat tinggal di",
                    "perangkat dan dibuka dengan sidik jari, wajah, atau kode kunci",
                    "layar. Saat login, server mengirim tantangan acak, dan",
                    "perangkat menandatanganinya.",
                    "",
                    "Kekuatan utamanya: kunci itu terikat ke nama domain. Passkey",
                    "untuk bank.example nggak akan mau menandatangani tantangan dari",
                    "bank-example.co yang palsu, walau tampilannya mirip. Server juga",
                    "cuma menyimpan kunci publik, jadi database bocor nggak memberi",
                    "penyerang apa pun untuk dipakai login.",
                    "",
                    "Ada dua bentuk passkey:",
                    "  - Tersinkron: disalin lewat akun, misalnya Google Password",
                    "    Manager atau iCloud Keychain, jadi ikut pindah ke ponsel",
                    "    baru.",
                    "  - Terikat perangkat: tinggal di satu kunci keamanan fisik dan",
                    "    nggak bisa disalin. Pedoman NIST cuma mengizinkan bentuk ini",
                    "    untuk tingkat keamanan tertingginya.",
                    "",
                    "Jebakan: lupa menyiapkan jalur pemulihan. Pengguna yang",
                    "kehilangan ponsel harus punya cara lain masuk, misalnya kode",
                    "pemulihan yang dicetak, atau passkey kedua di perangkat lain.",
                    "Jalur pemulihan yang lemah (cuma pertanyaan rahasia) membatalkan",
                    "semua kekuatan tadi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pada September 2022, penyerang masuk ke sistem internal Uber",
                    "memakai password seorang kontraktor. Menurut pernyataan Uber,",
                    "penyerang mengirim permintaan persetujuan MFA berulang-ulang,",
                    "dan kontraktor itu akhirnya menyetujui salah satunya. Itu",
                    "contoh MFA fatigue yang terdokumentasi. Sejak itu, banyak",
                    "penyedia identitas mewajibkan number matching untuk notifikasi",
                    "push.",
                    "",
                    "Kasus kecil: kamu membangun login untuk aplikasi koperasi",
                    "sekolah, dan pengurus ingin login yang aman tanpa merepotkan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Simpan password dengan Argon2id, minimal 15 karakter kalau",
                    "     belum ada MFA, tanpa aturan campuran karakter.",
                    "  2. Tolak password yang ada di daftar password bocor.",
                    "  3. Tawarkan TOTP dari aplikasi autentikator sebagai faktor",
                    "     kedua, dan wajibkan untuk akun pengurus.",
                    "  4. Tawarkan passkey sebagai pilihan login tanpa password.",
                    "  5. Beri sepuluh kode pemulihan sekali pakai saat MFA",
                    "     dinyalakan, dan minta pengguna menyimpannya.",
                    "  6. Batasi percobaan login yang gagal, yang dibahas lebih",
                    "     lengkap di bab 5.",
                ],
            },
        ],
    },
    {
        "title": "10. Sesi, Cookie, dan JWT",
        "sections": [
            {
                "body": [
                    "HTTP itu pelupa. Tiap permintaan berdiri sendiri, dan server",
                    "nggak ingat bahwa permintaan barusan datang dari orang yang",
                    "sama yang login semenit lalu. Supaya kamu nggak perlu mengetik",
                    "password di tiap klik, aplikasi butuh cara mengingat siapa",
                    "kamu. Ada dua cara utama: sesi di server dan token yang dibawa",
                    "klien.",
                ],
            },
            {
                "heading": "Sesi di server",
                "body": [
                    "Cara klasiknya begini:",
                    "  1. Kamu login dengan benar.",
                    "  2. Server membuat ID sesi acak yang panjang, misalnya dengan",
                    "     secrets.token_urlsafe(32), lalu menyimpan data \"ID ini milik",
                    "     pengguna 42\" di database atau Redis.",
                    "  3. Server mengirim ID itu ke browser sebagai cookie.",
                    "  4. Browser mengirim cookie itu otomatis di setiap permintaan",
                    "     berikutnya, dan server mencari datanya.",
                    "",
                    "ID sesinya sendiri nggak berarti apa-apa. Ia seperti nomor",
                    "tiket penitipan tas: yang penting tasnya, dan tasnya disimpan",
                    "petugas. Logout berarti petugas membuang catatan tiket itu, dan",
                    "tiketnya langsung nggak berlaku lagi.",
                ],
            },
            {
                "heading": "Cookie yang dikirim server",
                "bahasa": "http",
                "code": """HTTP/1.1 200 OK
Set-Cookie: sesi=q8Zr2vXk...; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=3600""",
            },
            {
                "body": [
                    "Atribut-atribut di cookie itu bagian dari pertahanannya:",
                    "  - HttpOnly: JavaScript di halaman nggak bisa membaca cookie",
                    "    ini. Kalau ada celah XSS, cookie sesi tetap aman.",
                    "  - Secure: cookie cuma dikirim lewat HTTPS.",
                    "  - SameSite=Lax: cookie nggak ikut terkirim di kebanyakan",
                    "    permintaan yang dipicu situs lain, jadi serangan CSRF",
                    "    (memalsukan permintaan dari situs lain) jauh lebih susah.",
                    "  - Max-Age: umur cookie dalam detik.",
                    "",
                    "Dua kebiasaan wajib lainnya. Buat ID sesi baru tepat sesudah",
                    "login berhasil, supaya ID yang mungkin sudah diketahui",
                    "penyerang sebelum login nggak ikut naik status. Serangan itu",
                    "namanya session fixation. Lalu beri batas waktu: sesi berakhir",
                    "kalau nggak dipakai sekian menit, dan berakhir mutlak sesudah",
                    "sekian jam walau terus dipakai.",
                ],
            },
            {
                "heading": "JWT: token yang membawa datanya sendiri",
                "body": [
                    "JWT (JSON Web Token, RFC 7519) mengambil pendekatan lain.",
                    "Datanya nggak disimpan di server. Server menulis data itu ke",
                    "dalam token, menandatanganinya, lalu memberikannya ke klien.",
                    "Saat token dikirim balik, server cukup memeriksa tanda",
                    "tangannya, tanpa perlu mencari apa pun di database.",
                    "",
                    "JWT terdiri dari tiga bagian yang dipisah titik:",
                    "header.payload.tanda_tangan. Header dan payload adalah JSON",
                    "yang ditulis dalam base64url, yaitu base64 versi aman untuk",
                    "URL. Payload berisi klaim, misalnya sub (siapa penggunanya),",
                    "exp (kapan kedaluwarsa, dalam detik sejak 1970), iss (siapa",
                    "penerbitnya), dan aud (untuk layanan mana token ini).",
                    "",
                    "Hal yang paling sering disalahpahami: JWT biasa cuma",
                    "ditandatangani, nggak dienkripsi. Siapa pun yang memegang",
                    "tokennya bisa membaca isinya. Program di bawah membukanya tanpa",
                    "kunci apa pun.",
                ],
            },
            {
                "heading": "Membaca isi JWT tanpa kunci",
                "code": """import base64
import json

token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
         ".eyJzdWIiOiJhbmkiLCJyb2xlIjoicGVtYmVsaSIsImV4cCI6MTc5MzAwMDAwMH0"
         ".UzjbQZraH0ElwaieV9_T83R4uOmKnSC1r3ucBGcVOSM")


def buka_base64url(bagian):
    return base64.urlsafe_b64decode(bagian + "=" * (-len(bagian) % 4))


header, payload, tanda = token.split(".")
print("header :", json.loads(buka_base64url(header)))
print("payload:", json.loads(buka_base64url(payload)))
print("tanda  :", len(buka_base64url(tanda)), "byte hasil HMAC-SHA256")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  header : {'alg': 'HS256', 'typ': 'JWT'}",
                    "  payload: {'sub': 'ani', 'role': 'pembeli', 'exp': 1793000000}",
                    "  tanda  : 32 byte hasil HMAC-SHA256",
                    "",
                    "Isi token terbaca utuh. Jadi jangan pernah menaruh password,",
                    "nomor KTP, atau rahasia lain di payload. Yang dilindungi tanda",
                    "tangan adalah keasliannya: kalau ada yang mengganti role jadi",
                    "admin, tanda tangannya nggak cocok lagi dan server menolak.",
                    "",
                    "HS256 berarti tanda tangan HMAC-SHA256 dengan satu kunci rahasia",
                    "bersama. Ada juga RS256, ES256, dan EdDSA yang memakai pasangan",
                    "kunci, cocok kalau banyak layanan perlu memeriksa token tapi",
                    "cuma satu yang boleh membuatnya.",
                ],
            },
            {
                "heading": "Jebakan JWT",
                "body": [
                    "  - Menerima alg yang dipilih token. Header bisa ditulis",
                    "    penyerang. Pustaka lama pernah menerima alg none (tanpa",
                    "    tanda tangan sama sekali), atau tertipu memeriksa token HS256",
                    "    memakai kunci publik RSA sebagai kunci HMAC. Pustaka",
                    "    jsonwebtoken untuk Node.js sebelum versi 4.2.2 kena masalah",
                    "    kedua (CVE-2015-9235). Selalu tetapkan algoritme yang",
                    "    diterima di sisi server.",
                    "  - Kunci HS256 yang pendek. Token yang bocor bisa dipakai untuk",
                    "    menebak kunci secara offline. Pakai kunci acak minimal 256",
                    "    bit.",
                    "  - Nggak bisa dicabut. Token yang sudah keluar tetap sah sampai",
                    "    exp, walau pengguna sudah logout atau ganti password.",
                    "    Karena itu access token dibuat berumur pendek (5 sampai 15",
                    "    menit) dan diperbarui dengan refresh token yang disimpan dan",
                    "    bisa dicabut di server.",
                    "  - Disimpan di localStorage. Satu celah XSS cukup untuk mencuri",
                    "    semua token. Untuk aplikasi web biasa, cookie HttpOnly lebih",
                    "    aman.",
                    "",
                    "Panduan praktik terbaiknya ada di RFC 8725 (JSON Web Token Best",
                    "Current Practices).",
                ],
            },
            {
                "heading": "Kapan memilih yang mana",
                "body": [
                    "  Kebutuhan                                 Pilihan yang wajar",
                    "  Aplikasi web biasa dengan backend sendiri  sesi di server",
                    "  Logout harus langsung berlaku              sesi di server",
                    "  API dipakai banyak layanan berbeda         JWT berumur pendek",
                    "  Token dari penyedia login (OAuth/OIDC)     JWT, mengikuti standar",
                    "",
                    "Kalau ragu, mulai dari sesi di server. Framework seperti Django,",
                    "Laravel, dan Rails menyediakannya bawaan, lengkap dengan atribut",
                    "cookie yang aman. JWT baru masuk akal kalau ada beberapa layanan",
                    "yang perlu memeriksa identitas tanpa bertanya ke satu database",
                    "pusat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Penyedia identitas seperti Keycloak dan Auth0 menerbitkan access",
                    "token berbentuk JWT, dan API memeriksanya dengan kunci publik",
                    "yang diumumkan penyedia lewat alamat JWKS (daftar kunci publik",
                    "berformat JSON). Sementara itu, halaman web milik aplikasi",
                    "biasanya tetap memakai cookie sesi.",
                    "",
                    "Kasus kecil: pengguna aplikasimu melapor akunnya dibajak. Ia",
                    "sudah ganti password, tapi penyerang masih bisa memakai API",
                    "selama beberapa hari, karena access token JWT-nya berumur",
                    "tujuh hari.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Turunkan umur access token jadi 10 menit.",
                    "  2. Pakai refresh token yang disimpan di database, dan diganti",
                    "     baru setiap kali dipakai (rotasi).",
                    "  3. Saat password diganti atau pengguna menekan \"keluar dari",
                    "     semua perangkat\", hapus semua refresh token miliknya.",
                    "  4. Untuk kasus darurat, simpan angka versi token per pengguna",
                    "     di database, masukkan ke klaim, lalu naikkan angkanya untuk",
                    "     membatalkan semua token lama sekaligus.",
                    "  5. Catat di log setiap refresh token yang dipakai dua kali.",
                    "     Itu tanda token tersebut dicuri.",
                ],
            },
        ],
    },
    {
        "title": "11. OAuth 2.0, OpenID Connect, dan SSO",
        "sections": [
            {
                "body": [
                    "Dulu, aplikasi yang ingin membaca kontak email-mu meminta",
                    "password email-mu langsung. Ini buruk dari segala sisi:",
                    "aplikasi itu dapat akses penuh, kamu nggak bisa mencabut",
                    "aksesnya tanpa ganti password, dan password-mu tersimpan di",
                    "tempat yang nggak kamu kendalikan.",
                    "",
                    "OAuth 2.0 (RFC 6749, terbit 2012) memecahkan masalah itu.",
                    "Aplikasi nggak pernah melihat password-mu. Kamu login di server",
                    "pemilik data, menyetujui izin terbatas (misalnya \"baca kontak",
                    "saja\"), lalu aplikasi menerima access token untuk izin itu.",
                    "Token bisa dicabut kapan saja tanpa menyentuh password.",
                    "",
                    "Ada empat peran:",
                    "  - Pemilik sumber daya: kamu.",
                    "  - Klien: aplikasi yang ingin akses.",
                    "  - Server otorisasi: tempat kamu login dan memberi izin,",
                    "    misalnya Google, GitHub, atau Keycloak milik kantormu.",
                    "  - Server sumber daya: API yang menyimpan datanya.",
                ],
            },
            {
                "heading": "Alur authorization code dengan PKCE",
                "body": [
                    "Dari beberapa alur di OAuth, yang dipakai untuk hampir semua",
                    "aplikasi sekarang adalah authorization code dengan PKCE (Proof",
                    "Key for Code Exchange, RFC 7636). Langkahnya:",
                    "  1. Aplikasi membuat teks acak rahasia bernama code_verifier,",
                    "     lalu menghitung code_challenge dari hash SHA-256-nya.",
                    "  2. Aplikasi mengarahkan browser ke server otorisasi, membawa",
                    "     code_challenge.",
                    "  3. Kamu login dan menyetujui izinnya di server otorisasi.",
                    "  4. Server otorisasi mengarahkan browser kembali ke aplikasi",
                    "     dengan membawa code, yaitu kode sekali pakai yang berumur",
                    "     pendek.",
                    "  5. Aplikasi menukar code itu dengan token, sambil mengirim",
                    "     code_verifier aslinya.",
                    "  6. Server otorisasi menghitung ulang hash code_verifier. Kalau",
                    "     cocok dengan code_challenge di langkah 2, token diberikan.",
                    "",
                    "Gunanya langkah tambahan ini: kalau code di langkah 4 dicuri",
                    "(misalnya oleh",
                    "aplikasi jahat di ponsel yang ikut menangkap alamat redirect),",
                    "pencurinya tetap nggak bisa menukarnya. Ia nggak punya",
                    "code_verifier.",
                ],
            },
            {
                "heading": "Membuat code_challenge",
                "code": """import base64
import hashlib


def base64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


# Di aplikasi sungguhan: code_verifier = secrets.token_urlsafe(32).
# Nilai ini contoh resmi dari RFC 7636, supaya hasilnya bisa dicocokkan.
code_verifier = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
code_challenge = base64url(hashlib.sha256(code_verifier.encode("ascii")).digest())

print("verifier  :", code_verifier)
print("challenge :", code_challenge)
print("cocok RFC :", code_challenge == "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  verifier  : dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk",
                    "  challenge : E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
                    "  cocok RFC : True",
                    "",
                    "code_challenge boleh terlihat siapa saja, karena hash nggak bisa",
                    "dibalik. code_verifier tetap di aplikasi sampai langkah",
                    "penukaran.",
                ],
            },
            {
                "heading": "Dua permintaan yang terjadi",
                "bahasa": "http",
                "code": """# Langkah 2: browser diarahkan ke server otorisasi
GET /authorize?response_type=code
    &client_id=aplikasi-koperasi
    &redirect_uri=https://koperasi.example/callback
    &scope=openid%20profile%20email
    &state=Jf83kQ...
    &code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
    &code_challenge_method=S256
Host: login.sekolah.example

# Langkah 5: aplikasi menukar code dengan token
POST /token
Host: login.sekolah.example
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=SplxlOBeZQ...
&redirect_uri=https://koperasi.example/callback
&client_id=aplikasi-koperasi
&code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk""",
            },
            {
                "body": [
                    "Parameter state adalah teks acak yang disimpan aplikasi sebelum",
                    "mengarahkan browser, lalu dicocokkan saat browser kembali.",
                    "Kalau nggak cocok, permintaan itu bukan lanjutan login yang",
                    "dimulai aplikasimu, dan harus ditolak.",
                    "",
                    "Dua alur lama sudah nggak disarankan. Implicit flow mengirim",
                    "token langsung di URL, dan password grant membuat aplikasi",
                    "menerima password pengguna lagi. Panduan keamanan OAuth 2.0",
                    "(RFC 9700, Januari 2025) melarang keduanya. OAuth 2.1 merangkum",
                    "aturan-aturan itu dan mewajibkan code_challenge untuk semua",
                    "klien. Saat",
                    "materi ini ditulis, OAuth 2.1 masih berstatus draf di IETF.",
                ],
            },
            {
                "heading": "OpenID Connect: menambah identitas",
                "body": [
                    "OAuth dirancang untuk otorisasi: memberi aplikasi izin akses",
                    "ke data. Access token cuma berarti \"pembawa token ini boleh",
                    "membaca kontak\". Token itu nggak menjelaskan siapa yang login.",
                    "",
                    "Banyak aplikasi dulu memakai OAuth untuk login dengan cara",
                    "masing-masing, dan banyak yang salah. OpenID Connect (OIDC,",
                    "dari OpenID Foundation, 2014) membakukan lapisan identitas di",
                    "atas OAuth 2.0:",
                    "  - Scope openid di permintaan menandakan aplikasi ingin login",
                    "    OIDC.",
                    "  - Selain access token, server memberi ID token, yaitu JWT yang",
                    "    berisi siapa penggunanya (sub), siapa penerbitnya (iss),",
                    "    untuk aplikasi mana (aud), dan kapan ia login.",
                    "  - Ada endpoint userinfo untuk mengambil data profil.",
                    "",
                    "Ingat: ID token untuk aplikasimu sendiri, access token untuk",
                    "API. Jangan mengirim ID token ke API sebagai tanda izin, dan",
                    "jangan memakai access token sebagai bukti siapa yang login.",
                ],
            },
            {
                "heading": "SSO: sekali login untuk banyak aplikasi",
                "body": [
                    "SSO (single sign-on) berarti pengguna login sekali di satu",
                    "server identitas, lalu bisa masuk ke banyak aplikasi tanpa",
                    "login ulang. Di kantor, itu berarti satu akun untuk email,",
                    "aplikasi absensi, dan dasbor internal. Untuk tim keamanan,",
                    "keuntungannya besar: pegawai yang keluar cukup dinonaktifkan di",
                    "satu tempat, dan aturan MFA ditetapkan di satu tempat.",
                    "",
                    "SSO modern biasanya berjalan di atas OIDC. Di perusahaan besar",
                    "kamu juga akan bertemu SAML 2.0, standar berbasis XML yang",
                    "lebih tua tapi masih banyak dipakai aplikasi bisnis. Penyedia",
                    "identitas seperti Keycloak bisa melayani keduanya. Pilihan",
                    "penyedianya dibahas di materi terakhir bab ini.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tombol \"Masuk dengan Google\" atau \"Sign in with GitHub\" yang",
                    "ada di banyak situs adalah OpenID Connect di atas OAuth 2.0.",
                    "Situs itu menerima ID token berisi identitasmu, tanpa pernah",
                    "melihat password Google atau GitHub-mu.",
                    "",
                    "Kasus kecil: sekolahmu sudah punya Keycloak, dan kamu diminta",
                    "membuat aplikasi koperasi berbasis web yang login lewat akun",
                    "sekolah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftarkan aplikasi sebagai klien di Keycloak, dengan",
                    "     alamat redirect yang ditulis persis, tanpa wildcard.",
                    "  2. Pakai pustaka OIDC yang sudah teruji untuk bahasamu, dan",
                    "     pilih alur authorization code dengan code_challenge.",
                    "  3. Simpan dan cocokkan state di setiap login.",
                    "  4. Saat ID token datang, periksa tanda tangan, iss, aud, dan",
                    "     exp-nya. Pustaka yang baik melakukannya untukmu.",
                    "  5. Sesudah itu, buat sesi di server aplikasimu sendiri dan",
                    "     simpan ID-nya di cookie HttpOnly. Token dari Keycloak nggak",
                    "     perlu sampai ke JavaScript di browser.",
                ],
            },
        ],
    },
    {
        "title": "12. Otorisasi: RBAC, Least Privilege, dan Policy as Code",
        "sections": [
            {
                "body": [
                    "Sesudah aplikasi tahu siapa kamu, pertanyaan berikutnya:",
                    "kamu boleh apa? Pertanyaan ini harus dijawab di server, di",
                    "setiap permintaan. Menyembunyikan tombol Hapus dari tampilan",
                    "pembeli nggak cukup, karena siapa pun bisa mengirim permintaan",
                    "DELETE langsung ke API.",
                    "",
                    "Dua prinsip mendasari semua model otorisasi:",
                    "  - Tolak secara bawaan (deny by default). Kalau nggak ada",
                    "    aturan yang mengizinkan, jawabannya tolak. Fitur baru yang",
                    "    lupa diberi aturan jadi tertutup, bukan terbuka.",
                    "  - Least privilege. Tiap pengguna, program, dan akun layanan",
                    "    cuma diberi izin yang dibutuhkan untuk pekerjaannya, dan",
                    "    cuma selama dibutuhkan.",
                ],
            },
            {
                "heading": "Model-model otorisasi",
                "body": [
                    "  - ACL (access control list): tiap benda punya daftar siapa",
                    "    boleh apa. Contohnya izin berkas di Linux atau berbagi",
                    "    dokumen di Google Drive. Gampang dipahami, tapi susah",
                    "    dikelola kalau penggunanya ribuan.",
                    "  - RBAC (role-based access control): izin diberikan ke peran,",
                    "    dan pengguna diberi peran. Guru, siswa, admin. Saat ada guru",
                    "    baru, cukup beri peran guru.",
                    "  - ABAC (attribute-based access control): keputusan memakai",
                    "    atribut. Misalnya \"guru boleh mengubah nilai kalau ia",
                    "    mengajar kelas itu dan sekarang masih masa input nilai\".",
                    "  - ReBAC (relationship-based): keputusan dari hubungan antar",
                    "    benda, seperti \"anggota folder ini boleh membaca semua",
                    "    dokumen di dalamnya\". OpenFGA dan SpiceDB memakai model ini.",
                    "",
                    "Di praktik, kebanyakan aplikasi memakai RBAC ditambah beberapa",
                    "aturan atribut. Aturan yang paling sering lupa adalah",
                    "kepemilikan: penulis boleh mengedit artikel, tapi artikelnya",
                    "sendiri saja. Lupa aturan ini menghasilkan celah IDOR (insecure",
                    "direct object reference): pengguna mengganti angka ID di",
                    "permintaan lalu bisa mengubah data milik orang lain.",
                ],
            },
            {
                "heading": "RBAC dengan aturan kepemilikan",
                "code": """IZIN_PERAN = {
    "pembaca": {"artikel:baca"},
    "penulis": {"artikel:baca", "artikel:tulis"},
    "admin": {"artikel:baca", "artikel:tulis", "artikel:hapus", "pengguna:kelola"},
}
peran_pengguna = {"ani": "admin", "budi": "penulis", "cici": "pembaca"}
pemilik_artikel = {101: "budi", 102: "ani"}


def periksa(nama, izin, artikel):
    peran = peran_pengguna.get(nama)
    if peran is None or izin not in IZIN_PERAN[peran]:
        return "TOLAK", "nggak punya izin"          # bawaannya menolak
    if izin == "artikel:tulis" and peran != "admin":
        if pemilik_artikel.get(artikel) != nama:   # cegah IDOR
            return "TOLAK", "bukan pemilik"
    return "IZINKAN", peran


permintaan = [
    ("budi", "artikel:tulis", 101),
    ("budi", "artikel:tulis", 102),
    ("cici", "artikel:tulis", 101),
    ("cici", "artikel:baca", 102),
    ("ani", "artikel:hapus", 101),
    ("eko", "artikel:baca", 101),
]
for nama, izin, artikel in permintaan:
    hasil, alasan = periksa(nama, izin, artikel)
    print(f"{hasil:7} {nama:4} {izin:13} {artikel}  ({alasan})")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  IZINKAN budi artikel:tulis 101  (penulis)",
                    "  TOLAK   budi artikel:tulis 102  (bukan pemilik)",
                    "  TOLAK   cici artikel:tulis 101  (nggak punya izin)",
                    "  IZINKAN cici artikel:baca  102  (pembaca)",
                    "  IZINKAN ani  artikel:hapus 101  (admin)",
                    "  TOLAK   eko  artikel:baca  101  (nggak punya izin)",
                    "",
                    "Budi penulis, tapi artikel 102 milik Ani, jadi ditolak. Eko",
                    "nggak ada di daftar pengguna, dan fungsi itu menolaknya tanpa",
                    "perlu aturan khusus. Itulah tolak secara bawaan.",
                    "",
                    "Perhatikan juga bentuk izinnya: sumber:aksi. Menamai izin",
                    "dengan pola tetap membuat aturan gampang dibaca dan gampang",
                    "dicari waktu audit.",
                ],
            },
            {
                "heading": "Policy as code dengan Open Policy Agent",
                "body": [
                    "Kalau aturan akses tersebar di puluhan if di banyak layanan,",
                    "nggak ada yang bisa menjawab pertanyaan sederhana seperti \"siapa",
                    "saja yang boleh menghapus data pelanggan?\". Policy as code",
                    "memindahkan aturan itu ke berkas kebijakan tersendiri yang",
                    "disimpan di Git, di-review, dan diuji seperti kode biasa.",
                    "",
                    "Open Policy Agent (OPA) adalah mesin kebijakan serbaguna yang",
                    "berstatus graduated di CNCF, berlisensi Apache-2.0. Versi",
                    "stabil terbarunya saat materi ini ditulis (Oktober 2026) adalah",
                    "1.21.2. Aplikasi mengirim data permintaan dalam bentuk JSON, dan",
                    "mesin itu menjawab boleh atau tidak berdasarkan kebijakan yang",
                    "ditulis dalam bahasa Rego. Kebijakan yang setara dengan program",
                    "Python di atas:",
                ],
            },
            {
                "heading": "Kebijakan Rego",
                "bahasa": "rego",
                "code": """package toko.otorisasi

default allow := false

izin_peran := {
    "pembaca": {"artikel:baca"},
    "penulis": {"artikel:baca", "artikel:tulis"},
    "admin": {"artikel:baca", "artikel:tulis", "artikel:hapus", "pengguna:kelola"},
}

punya_izin if {
    input.action in izin_peran[input.user.peran]
}

allow if {
    punya_izin
    input.user.peran == "admin"
}

allow if {
    punya_izin
    input.action != "artikel:tulis"
}

allow if {
    punya_izin
    input.action == "artikel:tulis"
    input.resource.pemilik == input.user.nama
}""",
            },
            {
                "body": [
                    "Di Kubernetes, mesin yang sama dipakai lewat Gatekeeper untuk",
                    "menolak konfigurasi yang melanggar aturan, misalnya container",
                    "yang berjalan sebagai root. Alternatif yang sering kamu temui:",
                    "  - Cedar: bahasa kebijakan open source dari AWS, dipakai di",
                    "    Amazon Verified Permissions.",
                    "  - Kyverno: mesin kebijakan khusus Kubernetes yang ditulis",
                    "    dalam YAML.",
                    "  - Casbin: pustaka otorisasi yang dipanggil langsung dari kode",
                    "    aplikasi, tersedia untuk banyak bahasa.",
                    "",
                    "Untuk aplikasi kecil, fungsi periksa seperti di atas, ditaruh",
                    "di satu tempat dan dipanggil di setiap handler, sudah cukup.",
                    "Mesin kebijakan baru terasa manfaatnya kalau layanan dan",
                    "aturannya mulai banyak.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pada 2019, data lebih dari 100 juta nasabah Capital One di",
                    "Amerika Serikat bocor dari layanan penyimpanan AWS. Penyerang",
                    "memanfaatkan firewall aplikasi web yang salah konfigurasi untuk",
                    "mengambil kredensial sebuah peran IAM. Peran itu punya izin",
                    "membaca jauh lebih banyak bucket daripada yang dibutuhkan",
                    "pekerjaannya. Kalau least privilege diterapkan, kredensial yang",
                    "dicuri itu cuma bisa membuka sedikit data. Cara menyetel IAM di",
                    "AWS dibahas di kurikulum DevOps, materi \"AWS IAM: Siapa Boleh",
                    "Melakukan Apa\".",
                    "",
                    "Kasus kecil: aplikasi nilai sekolah. Guru boleh mengubah nilai,",
                    "tapi ternyata guru matematika kelas 10 bisa mengubah nilai",
                    "bahasa Inggris kelas 12.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya dalam satu kalimat: guru boleh mengubah",
                    "     nilai kalau ia tercatat mengajar mata pelajaran itu di",
                    "     kelas itu.",
                    "  2. Simpan relasi guru, mata pelajaran, dan kelas di database.",
                    "  3. Buat satu fungsi pemeriksa yang menerima guru dan nilai yang",
                    "     mau diubah, dan bawaannya menolak.",
                    "  4. Panggil fungsi itu di server, di setiap endpoint yang",
                    "     mengubah nilai, termasuk endpoint impor massal.",
                    "  5. Tulis tes untuk kasus yang harus ditolak, di samping kasus",
                    "     yang harus diizinkan.",
                ],
            },
        ],
    },
    {
        "title": "13. Peta Penyedia Identitas: Keycloak, Auth0, Okta, Ping",
        "sections": [
            {
                "body": [
                    "Login yang benar ternyata banyak bagiannya: penyimpanan",
                    "password, MFA, passkey, reset password, OAuth, OIDC, SSO,",
                    "penguncian akun, dan log audit. Membangun semuanya sendiri",
                    "butuh waktu berbulan-bulan, dan tiap bagian bisa jadi celah.",
                    "",
                    "Karena itu banyak tim memakai penyedia identitas (identity",
                    "provider, sering disingkat IdP). Aplikasimu cukup bicara OIDC",
                    "dengan IdP, dan IdP yang mengurus sisanya. Pertanyaan utamanya:",
                    "pasang sendiri, atau pakai layanan orang lain?",
                ],
            },
            {
                "heading": "Empat nama yang paling sering muncul",
                "body": [
                    "  Penyedia       Model               Lisensi       SO 2026",
                    "  Auth0          layanan (SaaS)      proprietary   30%",
                    "  Okta           layanan (SaaS)      proprietary   29%",
                    "  Keycloak       pasang sendiri      Apache-2.0    19%",
                    "  Ping Identity  layanan + on-prem   proprietary    5%",
                    "",
                    "Angka di kolom terakhir dari Survei Stack Overflow 2026,",
                    "kategori alat operasi keamanan: persentase responden kategori",
                    "itu yang memakai alat tersebut. Auth0 ada di urutan pertama",
                    "kategori itu.",
                ],
            },
            {
                "heading": "Keycloak",
                "body": [
                    "Keycloak adalah server identitas open source yang ditulis dalam",
                    "Java, berlisensi Apache-2.0, dan berstatus proyek inkubasi di",
                    "CNCF. Versi terbarunya saat materi ini ditulis adalah 26.8.1,",
                    "rilis 13 Oktober 2026. Ia mendukung OIDC, OAuth 2.0, dan SAML,",
                    "bisa mengambil pengguna dari LDAP atau Active Directory, dan",
                    "punya konsol admin berbasis web. Red Hat menjual dukungan",
                    "komersialnya dengan nama Red Hat build of Keycloak.",
                    "",
                    "Kelebihannya: gratis, data pengguna tetap di servermu, dan bisa",
                    "dikustomisasi. Kekurangannya: kamu yang menanggung pemasangan,",
                    "pembaruan keamanan, cadangan database, dan ketersediaannya.",
                    "Kalau server Keycloak mati, semua aplikasi yang bergantung",
                    "padanya ikut nggak bisa login.",
                ],
            },
            {
                "heading": "Mencoba Keycloak di laptop",
                "bahasa": "terminal",
                "code": "# Mode pengembangan, hanya untuk belajar di laptop sendiri.\npodman run -p 127.0.0.1:8080:8080 \\\n  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin \\\n  -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin \\\n  quay.io/keycloak/keycloak:26.8.1 start-dev\n\n# Konsol admin: http://localhost:8080/admin",
            },
            {
                "heading": "Auth0, Okta, dan Ping Identity",
                "body": [
                    "  - Auth0: layanan identitas untuk aplikasi pelanggan (login",
                    "    sosial, MFA, manajemen pengguna). Okta membelinya pada 2021,",
                    "    dan keduanya kini satu perusahaan dengan produk terpisah.",
                    "    Populer di kalangan pengembang karena SDK dan dokumentasinya",
                    "    lengkap.",
                    "  - Okta: fokus ke identitas tenaga kerja. Karyawan login sekali",
                    "    lalu bisa masuk ke puluhan aplikasi SaaS kantor, dan akunnya",
                    "    otomatis dimatikan saat ia keluar.",
                    "  - Ping Identity: platform identitas untuk perusahaan besar,",
                    "    termasuk bank, dengan pilihan dipasang di server sendiri.",
                    "    Ping diakuisisi Thoma Bravo pada 2022 lalu digabung dengan",
                    "    ForgeRock pada 2023.",
                    "",
                    "Pilihan lain yang sering ditemui:",
                    "  - Microsoft Entra ID (dulu Azure Active Directory), di",
                    "    perusahaan yang memakai Microsoft 365.",
                    "  - Amazon Cognito dan Firebase Authentication, di aplikasi yang",
                    "    sudah memakai awan masing-masing.",
                    "  - Proyek open source seperti authentik, Zitadel, dan Authelia.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "Pertanyaan yang biasanya menentukan:",
                    "  - Siapa penggunanya? Pelanggan aplikasi (Auth0, Cognito,",
                    "    Firebase, Keycloak) atau karyawan kantor (Okta, Entra ID,",
                    "    Ping)?",
                    "  - Adakah aturan data harus tinggal di server sendiri atau di",
                    "    negara tertentu? Kalau ada, pasang sendiri lebih mudah",
                    "    dibuktikan.",
                    "  - Adakah orang yang sanggup mengoperasikan server identitas",
                    "    24 jam? Kalau nggak ada, layanan lebih aman.",
                    "  - Berapa biayanya kalau pengguna aktif naik sepuluh kali",
                    "    lipat? Layanan SaaS biasanya dihitung per pengguna aktif.",
                    "  - Seberapa mudah pindah? Pakai standar OIDC dan SAML, jangan",
                    "    fitur khusus vendor, supaya pindah penyedia nggak berarti",
                    "    menulis ulang aplikasi.",
                    "",
                    "Jebakan: menganggap layanan SaaS membuatmu bebas urusan",
                    "keamanan. Konfigurasinya tetap tanggung jawabmu: alamat",
                    "redirect yang terlalu longgar, MFA yang nggak diwajibkan, atau",
                    "akun admin IdP tanpa passkey tetap jadi celah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Penyedia identitas adalah sasaran favorit, karena membobolnya",
                    "berarti membuka banyak aplikasi sekaligus. Pada",
                    "Oktober 2023, sistem dukungan pelanggan Okta dibobol. Penyerang",
                    "mengambil berkas HAR (rekaman lalu lintas browser) yang diunggah",
                    "pelanggan saat meminta bantuan, dan sebagian berkas itu memuat",
                    "token sesi aktif. Pelajarannya berlaku untuk semua IdP: hapus",
                    "token dan cookie dari berkas diagnosis sebelum dikirim ke siapa",
                    "pun.",
                    "",
                    "Kasus kecil: startup tempatmu PKL membuat aplikasi kasir untuk",
                    "UMKM. Timnya tiga orang, belum ada yang mengurus server, dan",
                    "pengguna ditargetkan beberapa ribu toko.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis kebutuhannya: login pemilik toko dan kasir, MFA untuk",
                    "     pemilik, login dengan Google sebagai pilihan.",
                    "  2. Karena belum ada orang yang mengoperasikan server, condong",
                    "     ke layanan SaaS, lalu bandingkan biaya per pengguna aktif",
                    "     di dua atau tiga penyedia.",
                    "  3. Integrasikan lewat OIDC standar dengan pustaka umum, bukan",
                    "     SDK yang mengunci ke satu vendor.",
                    "  4. Wajibkan passkey atau TOTP untuk akun admin di dasbor",
                    "     penyedianya.",
                    "  5. Catat rencana keluar: kalau suatu hari pindah ke Keycloak,",
                    "     data apa yang perlu diekspor dan bagaimana password-nya",
                    "     dipindahkan.",
                ],
            },
        ],
    },
    {
        "title": "14. OWASP Top 10:2025: Peta Risiko Aplikasi Web",
        "sections": [
            {
                "body": [
                    "Kalau kamu baru pertama kali diminta \"ngecek keamanan\" sebuah",
                    "aplikasi web, pertanyaan pertamanya biasanya: ngecek apa dulu?",
                    "Celah keamanan itu ada ribuan jenis. Kamu butuh peta yang",
                    "bilang mana yang paling sering kejadian dan paling mahal",
                    "akibatnya.",
                    "",
                    "Peta itu namanya OWASP Top 10. Pembuatnya Open Worldwide",
                    "Application Security Project, komunitas nirlaba yang",
                    "membuat panduan, alat, dan standar keamanan aplikasi secara",
                    "gratis. Top 10 adalah daftar sepuluh kategori risiko aplikasi",
                    "web yang paling penting menurut data dan pengalaman praktisi.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), edisi terbarunya adalah",
                    "Top 10:2025, diumumkan November 2025. Ini edisi kedelapan;",
                    "edisi sebelumnya terbit tahun 2021 dan 2017. Daftarnya disusun",
                    "dari data pengujian ratusan ribu aplikasi yang disumbang banyak",
                    "perusahaan, ditambah survei ke praktisi. Delapan kategori",
                    "dipilih dari data, dua lagi dinaikkan lewat survei karena",
                    "risikonya nyata tapi belum banyak tertangkap alat uji.",
                    "",
                    "Tiap kategori adalah kumpulan jenis kelemahan dari daftar",
                    "Common Weakness Enumeration, yaitu daftar kelemahan perangkat",
                    "lunak yang diberi nomor. XSS misalnya bernomor 79. Edisi 2025",
                    "memetakan 248 jenis kelemahan ke dalam sepuluh kategori.",
                ],
            },
            {
                "heading": "Sepuluh kategori dan tempat membahasnya",
                "body": [
                    "Nama resminya berbahasa Inggris. Kolom kanan menunjuk bab di",
                    "kurikulum ini yang membahas perbaikannya:",
                    "",
                    "  Kode  Nama resmi                          Dibahas di",
                    "  A01   Broken Access Control               bab 04",
                    "  A02   Security Misconfiguration           bab 04",
                    "  A03   Software Supply Chain Failures      bab 06",
                    "  A04   Cryptographic Failures              bab 02",
                    "  A05   Injection                           bab 04",
                    "  A06   Insecure Design                     bab 04",
                    "  A07   Authentication Failures             bab 03",
                    "  A08   Software or Data Integrity Failures bab 06",
                    "  A09   Security Logging and Alerting       bab 04",
                    "        Failures",
                    "  A10   Mishandling of Exceptional          bab 04",
                    "        Conditions",
                    "",
                    "Kriptografi yang salah pakai (A04) ada di bab Kriptografi",
                    "Terapan, misalnya materi Menyimpan Password: Salt, PBKDF2,",
                    "bcrypt, dan Argon2. Login yang lemah (A07) ada di bab",
                    "Autentikasi dan Otorisasi. Rantai pasok (A03) dan integritas",
                    "(A08) ada di bab Rahasia dan Rantai Pasok, materi Rantai Pasok",
                    "Perangkat Lunak: Lockfile dan Dependensi.",
                ],
            },
            {
                "heading": "Apa yang bergeser dari edisi 2021",
                "code": """# Posisi kategori di edisi 2025, dibandingkan edisi 2021.
# None artinya kategori itu belum ada di 2021.
daftar = [
    ("A01", "Broken Access Control", 1),
    ("A02", "Security Misconfiguration", 5),
    ("A03", "Software Supply Chain Failures", None),
    ("A04", "Cryptographic Failures", 2),
    ("A05", "Injection", 3),
    ("A06", "Insecure Design", 4),
    ("A07", "Authentication Failures", 7),
    ("A08", "Software or Data Integrity Failures", 8),
    ("A09", "Security Logging and Alerting Failures", 9),
    ("A10", "Mishandling of Exceptional Conditions", None),
]

for kode, nama, dulu in daftar:
    kini = int(kode[1:])
    if dulu is None:
        arah = "baru"
    elif dulu > kini:
        arah = f"naik dari #{dulu}"
    elif dulu < kini:
        arah = f"turun dari #{dulu}"
    else:
        arah = "tetap"
    print(f"{kode}  {nama:<40} {arah}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  A01  Broken Access Control                    tetap",
                    "  A02  Security Misconfiguration                naik dari #5",
                    "  A03  Software Supply Chain Failures           baru",
                    "  A04  Cryptographic Failures                   turun dari #2",
                    "  A05  Injection                                turun dari #3",
                    "  A06  Insecure Design                          turun dari #4",
                    "  A07  Authentication Failures                  tetap",
                    "  A08  Software or Data Integrity Failures      tetap",
                    "  A09  Security Logging and Alerting Failures   tetap",
                    "  A10  Mishandling of Exceptional Conditions    baru",
                    "",
                    "Program kecil ini cuma membandingkan dua angka per baris, tapi",
                    "hasilnya merangkum perubahan terbesar edisi 2025:",
                    "",
                    "  - Dua kategori baru. A03 Software Supply Chain Failures",
                    "    memperluas kategori lama soal komponen usang jadi seluruh",
                    "    rantai: dependensi, alat build, dan pipeline. A10",
                    "    Mishandling of Exceptional Conditions membahas program yang",
                    "    salah bersikap saat ada error.",
                    "  - Salah konfigurasi naik dari nomor 5 ke nomor 2. Aplikasi",
                    "    sekarang lebih banyak diatur lewat berkas konfigurasi, dan",
                    "    makin banyak setelan berarti makin banyak yang bisa salah.",
                    "  - SSRF (Server-Side Request Forgery) nggak berdiri sendiri",
                    "    lagi. Ia dilebur ke A01 karena intinya sama: server mau",
                    "    mengakses sesuatu yang mestinya nggak boleh.",
                    "  - A07 dan A09 ganti nama. A09 sekarang menyebut alerting,",
                    "    karena log yang nggak pernah memicu peringatan nggak",
                    "    menolong siapa pun.",
                    "",
                    "Injeksi turun ke nomor 5. Itu bukan berarti injeksi sudah",
                    "jarang. Framework modern makin banyak memasang pengaman bawaan,",
                    "sehingga kategori lain menyusul.",
                ],
            },
            {
                "heading": "Cara memakai daftar ini",
                "body": [
                    "Top 10 adalah dokumen penyadaran. Gunanya membuat developer,",
                    "penguji, dan manajer punya bahasa yang sama soal risiko. Ia",
                    "nggak dirancang sebagai daftar periksa lengkap.",
                    "",
                    "Untuk memeriksa aplikasi secara menyeluruh, proyek yang sama",
                    "punya Application Security Verification Standard (ASVS), yang",
                    "versi stabil terbarunya 5.0.0. Isinya ratusan syarat yang",
                    "bisa dicentang satu per satu, dibagi per tingkat ketelitian.",
                    "Untuk cara memperbaiki, buka Cheat Sheet Series: kumpulan",
                    "panduan singkat per topik, dari SQL injection sampai upload",
                    "berkas.",
                    "",
                    "Selain daftar untuk aplikasi web, ada juga API Security Top 10",
                    "(edisi 2023, dibahas di bab berikutnya) dan Top 10 for LLM",
                    "Applications untuk aplikasi yang memakai model bahasa.",
                    "",
                    "Jebakan: nomor urut bukan urutan prioritas untuk aplikasimu.",
                    "Aplikasi internal tanpa login mungkin nggak peduli A07, tapi",
                    "rawan sekali di A02. Urutkan perbaikan menurut risiko di",
                    "aplikasimu sendiri, dengan cara di bab 01.",
                    "",
                    "Ingat: lolos dari sepuluh kategori ini nggak berarti aplikasi",
                    "aman. Daftar ini merangkum yang paling sering, dan penyerang",
                    "nggak terikat pada daftar mana pun.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan uji penetrasi dan alat pemindai seperti ZAP atau",
                    "SonarQube sering memberi label kategori Top 10 pada tiap",
                    "temuannya. Label itu dipakai tim untuk mengelompokkan",
                    "pekerjaan dan untuk melapor ke manajemen tanpa harus",
                    "menjelaskan tiap jenis kelemahan.",
                    "",
                    "Kasus kecil: tim kecilmu menerima laporan audit tahun lalu",
                    "berisi 30 temuan berlabel edisi 2021. Atasan minta ringkasan",
                    "per kategori edisi 2025, lengkap dengan urutan pengerjaan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Petakan label lama ke label baru. Contohnya A05:2021",
                    "     Security Misconfiguration jadi A02:2025, dan A03:2021",
                    "     Injection jadi A05:2025. Temuan SSRF (A10:2021) masuk",
                    "     A01:2025.",
                    "  2. Temuan soal pustaka usang (A06:2021) masuk A03:2025, dan",
                    "     sekalian cek apakah lockfile dan pipeline-mu juga",
                    "     tercakup.",
                    "  3. Hitung jumlah temuan per kategori baru, lalu urutkan",
                    "     menurut dampak di aplikasimu, bukan menurut nomor",
                    "     kategori.",
                    "  4. Untuk tiap kategori, tautkan halaman Cheat Sheet Series",
                    "     yang relevan supaya developer langsung tahu cara",
                    "     memperbaikinya.",
                ],
            },
        ],
    },
    {
        "title": "15. Kontrol Akses Rusak dan Salah Konfigurasi",
        "sections": [
            {
                "body": [
                    "Dua kategori teratas Top 10:2025 punya satu kesamaan: kodenya",
                    "sering kelihatan benar, aplikasinya jalan normal, dan nggak",
                    "ada error. Celahnya baru kelihatan kalau seseorang mencoba",
                    "hal yang nggak kamu duga.",
                    "",
                    "A01 Broken Access Control artinya kontrol akses yang rusak.",
                    "Ingat bedanya dari bab Autentikasi dan Otorisasi: autentikasi",
                    "menjawab \"kamu siapa\", otorisasi menjawab \"kamu boleh apa\".",
                    "A01 terjadi waktu aplikasi sudah tahu kamu siapa, tapi lupa",
                    "ngecek apakah kamu boleh melakukan yang kamu minta.",
                    "",
                    "Bentuk yang paling sering namanya IDOR (Insecure Direct Object",
                    "Reference). Aplikasi menerima nomor objek dari pengguna, lalu",
                    "langsung mengambil objek itu tanpa ngecek pemiliknya. Contohnya",
                    "halaman /pesanan/1042. Ani login, membuka pesanannya sendiri,",
                    "lalu mengganti angka di alamat jadi 1043. Kalau server cuma",
                    "ngecek \"sudah login\", Ani bisa membaca alamat rumah Budi.",
                ],
            },
            {
                "heading": "Handler rentan dan handler yang memeriksa pemilik",
                "code": """pesanan = {
    1042: {"pemilik": "ani", "isi": "2 kopi susu", "alamat": "Jl. Melati 7"},
    1043: {"pemilik": "budi", "isi": "1 roti bakar", "alamat": "Jl. Kenanga 12"},
}


def lihat_rentan(pengguna, id_pesanan):
    # Cuma memeriksa "sudah login atau belum", lalu percaya pada id dari URL.
    data = pesanan.get(id_pesanan)
    if data is None:
        return 404, "tidak ada"
    return 200, data["alamat"]


def lihat_aman(pengguna, id_pesanan):
    data = pesanan.get(id_pesanan)
    # Pesanan milik orang lain diperlakukan sama dengan pesanan yang tidak ada.
    if data is None or data["pemilik"] != pengguna:
        return 404, "tidak ada"
    return 200, data["alamat"]


for fungsi in (lihat_rentan, lihat_aman):
    print(fungsi.__name__)
    for id_pesanan in (1042, 1043, 9999):
        status, isi = fungsi("ani", id_pesanan)
        print(f"  ani minta /pesanan/{id_pesanan} -> {status} {isi}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  lihat_rentan",
                    "    ani minta /pesanan/1042 -> 200 Jl. Melati 7",
                    "    ani minta /pesanan/1043 -> 200 Jl. Kenanga 12",
                    "    ani minta /pesanan/9999 -> 404 tidak ada",
                    "  lihat_aman",
                    "    ani minta /pesanan/1042 -> 200 Jl. Melati 7",
                    "    ani minta /pesanan/1043 -> 404 tidak ada",
                    "    ani minta /pesanan/9999 -> 404 tidak ada",
                    "",
                    "Perbaikannya cuma satu syarat tambahan: pemilik pesanan harus",
                    "sama dengan pengguna yang sedang login. Di aplikasi sungguhan,",
                    "syarat itu paling aman ditaruh di query-nya sendiri:",
                    "",
                    "  SELECT * FROM pesanan WHERE id = ? AND pemilik_id = ?",
                    "",
                    "Dengan begitu, pesanan orang lain nggak pernah terambil dari",
                    "database, jadi nggak bisa bocor walau kode sesudahnya lupa",
                    "ngecek.",
                    "",
                    "Perhatikan juga jawaban 404 untuk pesanan milik orang lain.",
                    "Kalau server menjawab 403 (dilarang), penyerang jadi tahu",
                    "pesanan 1043 itu ada. Dua-duanya boleh dipakai; yang penting",
                    "isinya nggak bocor.",
                    "",
                    "Jebakan: mengganti angka urut dengan UUID acak nggak menutup",
                    "IDOR. Tebakannya memang jadi susah, tapi UUID tetap bisa bocor",
                    "lewat tautan yang dibagikan, log, atau respons API lain.",
                    "Pemeriksaan pemilik tetap wajib.",
                ],
            },
            {
                "heading": "Bentuk lain kontrol akses yang rusak",
                "body": [
                    "  - Eskalasi hak ke atas. Pengguna biasa memanggil",
                    "    /admin/hapus-pengguna dan server menurut, karena tombolnya",
                    "    cuma disembunyikan di tampilan. Menyembunyikan tombol itu",
                    "    urusan tampilan; pemeriksaan peran tetap harus ada di",
                    "    server.",
                    "  - Mengubah data lewat parameter. Formulir profil mengirim",
                    "    peran=pembaca, lalu seseorang mengubahnya jadi peran=admin",
                    "    sebelum dikirim.",
                    "  - CORS yang terlalu longgar, sehingga situs lain boleh membaca",
                    "    data penggunamu. Detailnya di bab 05.",
                    "  - SSRF. Server diminta mengambil URL dari pengguna, misalnya",
                    "    untuk pratinjau tautan, lalu dipakai untuk mengakses alamat",
                    "    internal seperti 169.254.169.254, alamat metadata di",
                    "    banyak layanan cloud. Pertahanannya daftar tujuan yang",
                    "    diizinkan, dan menolak alamat internal setelah nama domain",
                    "    diubah ke IP.",
                    "",
                    "Pola pertahanannya sama untuk semuanya: tolak secara bawaan",
                    "(deny by default), lalu izinkan yang memang perlu saja. Taruh",
                    "pemeriksaan di satu tempat yang dilewati semua permintaan,",
                    "misalnya middleware atau lapisan layanan, supaya nggak ada",
                    "endpoint yang lupa.",
                ],
            },
            {
                "heading": "A02: salah konfigurasi",
                "body": [
                    "Security Misconfiguration artinya aplikasinya sendiri benar,",
                    "tapi setelannya membuka celah. Contoh yang sering ketemu:",
                    "",
                    "  - Mode debug menyala di produksi. Halaman error menampilkan",
                    "    traceback, isi variabel, kadang setelan rahasia. Debugger",
                    "    interaktif Werkzeug (dipakai Flask) bahkan bisa menjalankan",
                    "    kode Python dari browser.",
                    "  - Akun bawaan seperti admin/admin belum diganti.",
                    "  - Daftar isi folder (directory listing) aktif, sehingga",
                    "    berkas cadangan seperti backup.sql bisa diunduh.",
                    "  - Header yang mengumumkan versi server, sehingga penyerang",
                    "    tahu celah mana yang cocok.",
                    "  - Port database terbuka ke internet, atau bucket penyimpanan",
                    "    cloud yang bisa dibaca publik.",
                    "  - Pengurai XML yang masih mengizinkan entitas eksternal",
                    "    milik XML, sehingga isi berkas server bisa ikut terbaca.",
                    "",
                    "Cara paling ampuh mencegahnya adalah memperlakukan setelan",
                    "seperti kode: disimpan di Git, ditinjau, dan dicek otomatis",
                    "sebelum naik ke produksi. Program di bawah ini versi mini",
                    "pemeriksa seperti itu.",
                ],
            },
            {
                "heading": "Pemeriksa setelan sederhana",
                "code": """# Setelan yang sering lupa diganti sebelum aplikasi naik ke produksi.
setelan = {
    "DEBUG": True,
    "ADMIN_PASSWORD": "admin",
    "DIRECTORY_LISTING": False,
    "SERVER_TOKENS": "full",
    "ALLOWED_HOSTS": ["*"],
}

aturan = [
    ("DEBUG", lambda v: v is False, "mode debug menampilkan traceback ke pengunjung"),
    ("ADMIN_PASSWORD", lambda v: v not in ("admin", "password", "123456"),
     "password bawaan gampang ditebak"),
    ("DIRECTORY_LISTING", lambda v: v is False, "isi folder bisa dijelajahi"),
    ("SERVER_TOKENS", lambda v: v == "off", "versi server diumumkan di header"),
    ("ALLOWED_HOSTS", lambda v: "*" not in v, "semua nama host diterima"),
]

masalah = 0
for kunci, aman, alasan in aturan:
    if aman(setelan[kunci]):
        print(f"OK     {kunci}")
    else:
        masalah += 1
        print(f"UBAH   {kunci}: {alasan}")
print(f"{masalah} setelan perlu diubah")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  UBAH   DEBUG: mode debug menampilkan traceback ke pengunjung",
                    "  UBAH   ADMIN_PASSWORD: password bawaan gampang ditebak",
                    "  OK     DIRECTORY_LISTING",
                    "  UBAH   SERVER_TOKENS: versi server diumumkan di header",
                    "  UBAH   ALLOWED_HOSTS: semua nama host diterima",
                    "  4 setelan perlu diubah",
                    "",
                    "Tiap aturan ditulis sebagai fungsi kecil yang menjawab \"aman",
                    "atau nggak\". Pola yang sama dipakai alat pemindai konfigurasi",
                    "sungguhan seperti Checkov, yang dibahas di bab 07.",
                    "Untuk Nginx, dua setelan di contoh tadi ditulis begini:",
                ],
            },
            {
                "heading": "Potongan konfigurasi Nginx",
                "bahasa": "nginx",
                "code": """server {
    server_tokens off;   # jangan tampilkan versi Nginx
    autoindex off;       # jangan tampilkan daftar isi folder
}""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data orang lain yang terbuka lewat angka di URL termasuk",
                    "temuan yang paling sering dilaporkan di program bug bounty.",
                    "Itu program resmi tempat perusahaan membayar orang yang",
                    "melaporkan celah di sistemnya. Polanya",
                    "hampir selalu sama: angka di URL atau di badan permintaan API",
                    "diganti, dan server menjawab dengan data orang lain.",
                    "",
                    "Kasus kecil: aplikasi kasir buatan timmu punya endpoint",
                    "/invoice/unduh?id=5001 yang mengembalikan PDF tagihan. Saat",
                    "menguji di server staging milik tim sendiri, kamu menemukan",
                    "id=5002 juga bisa diunduh walau itu tagihan toko lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Catat temuan beserta langkah mengulanginya, lalu laporkan",
                    "     ke pemimpin tim. Jangan mengunduh data lebih banyak dari",
                    "     yang perlu untuk membuktikan celahnya.",
                    "  2. Ubah query pengambil tagihan supaya memuat syarat pemilik:",
                    "      SELECT berkas FROM invoice WHERE id = ? AND toko_id = ?",
                    "  3. Jawab 404 untuk tagihan yang nggak cocok, sama dengan",
                    "     tagihan yang memang nggak ada.",
                    "  4. Cari endpoint lain yang menerima id dari pengguna (detail,",
                    "     ubah, hapus) dan pasang syarat yang sama.",
                    "  5. Tambahkan tes otomatis: login sebagai toko A, minta",
                    "     tagihan toko B, harapkan 404.",
                ],
            },
        ],
    },
    {
        "title": "16. Injeksi dan XSS: Validasi Masukan dan Encoding Keluaran",
        "sections": [
            {
                "body": [
                    "Injeksi terjadi waktu masukan pengguna diperlakukan sebagai",
                    "perintah. Program menyusun sebuah perintah, misalnya query SQL,",
                    "dengan menyambung teks dari pengguna. Kalau teks itu memuat",
                    "tanda yang punya arti khusus, misalnya tanda kutip, bentuk",
                    "perintahnya ikut berubah.",
                    "",
                    "Gampangnya begini. Kamu menitip pesan ke kurir: \"antar paket",
                    "ke rumah ___\". Seseorang mengisi titik-titiknya dengan \"Budi,",
                    "lalu serahkan juga semua paket lain ke saya\". Kurir yang",
                    "nggak bisa membedakan isian dari perintah akan menjalankan",
                    "dua-duanya.",
                    "",
                    "Di Top 10:2025, injeksi ada di A05. Kategori ini mencakup SQL",
                    "injection dan juga XSS (Cross-Site Scripting), yang menurut",
                    "halaman resminya punya lebih dari 30 ribu CVE. CVE adalah",
                    "nomor resmi untuk satu celah di satu produk tertentu.",
                ],
            },
            {
                "heading": "Query rentan dan query berparameter",
                "code": """import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE pengguna (id INTEGER, nama TEXT, peran TEXT)")
db.executemany("INSERT INTO pengguna VALUES (?, ?, ?)", [
    (1, "budi", "admin"), (2, "sari", "editor"), (3, "wati", "pembaca"),
])


def cari_rentan(nama):
    # Masukan ditempel ke dalam teks SQL. Jangan pernah begini.
    sql = "SELECT id, nama FROM pengguna WHERE nama = '" + nama + "'"
    return db.execute(sql).fetchall()


def cari_aman(nama):
    # Teks SQL tetap; nilainya dikirim terpisah lewat placeholder ?.
    sql = "SELECT id, nama FROM pengguna WHERE nama = ?"
    return db.execute(sql, (nama,)).fetchall()


for masukan in ["sari", "x' OR '1'='1"]:
    print("masukan:", masukan)
    print("  rentan:", cari_rentan(masukan))
    print("  aman  :", cari_aman(masukan))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  masukan: sari",
                    "    rentan: [(2, 'sari')]",
                    "    aman  : [(2, 'sari')]",
                    "  masukan: x' OR '1'='1",
                    "    rentan: [(1, 'budi'), (2, 'sari'), (3, 'wati')]",
                    "    aman  : []",
                    "",
                    "Dengan masukan biasa, dua fungsi memberi hasil yang sama. Beda",
                    "kelihatan di masukan kedua. Di cari_rentan, teks SQL-nya jadi:",
                    "",
                    "  SELECT id, nama FROM pengguna WHERE nama = 'x' OR '1'='1'",
                    "",
                    "Syarat '1'='1' selalu benar, jadi semua baris ikut keluar.",
                    "Di aplikasi login, pola yang sama bisa melewati pemeriksaan",
                    "password.",
                    "",
                    "Di cari_aman, teks SQL nggak pernah berubah. Nilainya dikirim",
                    "ke SQLite secara terpisah, dan SQLite memperlakukannya sebagai",
                    "data utuh. Yang dicari jadi nama yang huruf per hurufnya",
                    "x' OR '1'='1, dan nama seperti itu memang nggak ada. Cara ini",
                    "namanya query berparameter (parameterized query atau prepared",
                    "statement), dan halaman resmi A05 menyebutnya sebagai",
                    "pertahanan utama.",
                ],
            },
            {
                "heading": "Aturan query berparameter",
                "body": [
                    "  - Placeholder cuma bisa menggantikan nilai. Nama tabel, nama",
                    "    kolom, dan arah ORDER BY nggak bisa diparameterkan. Untuk",
                    "    itu, cocokkan masukan dengan daftar putih nama yang boleh,",
                    "    misalnya {\"harga\", \"nama\", \"tanggal\"}.",
                    "  - Tanda placeholder beda per pustaka: ? untuk sqlite3,",
                    "    %s untuk psycopg (PostgreSQL), :nama untuk banyak ORM.",
                    "  - ORM seperti SQLAlchemy atau Django ORM memakai parameter",
                    "    secara bawaan. Celahnya kembali begitu kamu menulis query",
                    "    mentah dengan f-string di dalam ORM itu.",
                    "",
                    "Injeksi juga ada di luar SQL. Memanggil perintah sistem lewat",
                    "subprocess.run(..., shell=True) dengan teks dari pengguna",
                    "membuka injeksi perintah OS. Kirim argumennya sebagai daftar,",
                    "misalnya [\"convert\", nama_berkas, \"hasil.png\"], tanpa",
                    "shell=True. Pola yang sama berlaku untuk LDAP, query NoSQL,",
                    "dan mesin templat.",
                ],
            },
            {
                "heading": "XSS: masukan yang jadi skrip di browser orang lain",
                "code": """import html

komentar = '<script>alert(1)</script> Kopinya enak & murah'

rentan = "<p>" + komentar + "</p>"
aman = "<p>" + html.escape(komentar) + "</p>"

print(rentan)
print(aman)

# Di dalam atribut, tanda kutip juga harus di-escape.
nama = 'Sari" onmouseover="alert(1)'
print('<input value="' + html.escape(nama, quote=True) + '">')""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  <p><script>alert(1)</script> Kopinya enak & murah</p>",
                    "  <p>&lt;script&gt;alert(1)&lt;/script&gt; Kopinya enak &amp; murah</p>",
                    "  <input value=\"Sari&quot; onmouseover=&quot;alert(1)\">",
                    "",
                    "XSS terjadi waktu masukan pengguna ditampilkan di halaman",
                    "orang lain tanpa diubah dulu. Browser pengunjung membaca",
                    "<script> di baris pertama sebagai skrip sungguhan dan",
                    "menjalankannya dengan hak akses situsmu. Skrip seperti itu",
                    "bisa mengirim permintaan atas nama korban atau membaca isi",
                    "halaman yang sedang ia lihat.",
                    "",
                    "Ada tiga jenis:",
                    "",
                    "  - Stored: masukan tersimpan di database (komentar, nama",
                    "    profil) lalu tampil ke semua pengunjung.",
                    "  - Reflected: masukan dari URL langsung dipantulkan ke",
                    "    halaman, misalnya \"Hasil pencarian untuk ...\".",
                    "  - DOM-based: JavaScript di browser sendiri yang menulis",
                    "    masukan ke halaman lewat innerHTML.",
                    "",
                    "Pertahanannya encoding keluaran: ubah karakter khusus jadi",
                    "bentuk aman tepat sebelum ditampilkan. html.escape mengubah <",
                    "jadi &lt;, > jadi &gt;, dan & jadi &amp;. Browser lalu",
                    "menampilkannya sebagai teks biasa.",
                    "",
                    "Encoding harus sesuai konteks. Di dalam isi elemen, cukup < >",
                    "dan &. Di dalam atribut, tanda kutip juga wajib di-escape;",
                    "lihat baris ketiga keluaran. Di dalam URL pakai",
                    "urllib.parse.quote, dan atribut href wajib dicek skemanya:",
                    "javascript:alert(1) lolos dari html.escape tapi tetap",
                    "dijalankan browser saat diklik.",
                ],
            },
            {
                "heading": "Validasi masukan: lapisan pertama, bukan satu-satunya",
                "body": [
                    "Validasi masukan artinya menolak data yang bentuknya salah",
                    "sejak awal: umur harus angka 0 sampai 150, kode pos lima",
                    "digit, username cuma huruf kecil dan angka. Pakai daftar",
                    "putih (yang boleh), bukan daftar hitam (yang dilarang). Daftar",
                    "hitam selalu ketinggalan satu cara penulisan.",
                    "",
                    "Validasi mengurangi banyak serangan, tapi nggak bisa",
                    "menggantikan query berparameter dan encoding keluaran. Nama",
                    "o'neil itu sah, dan komentar boleh memuat tanda <. Data yang",
                    "sah tetap harus diperlakukan sebagai data.",
                    "",
                    "Kabar baiknya, framework modern melakukan encoding untukmu.",
                    "Jinja2 di Flask, templat Django, dan JSX di React meng-escape",
                    "keluaran secara bawaan. Celah biasanya muncul di jalan pintas",
                    "yang mematikan pengaman itu: filter |safe di Jinja2,",
                    "mark_safe di Django, dangerouslySetInnerHTML di React, dan",
                    "innerHTML di JavaScript polos. Kalau cuma mau menampilkan",
                    "teks, pakai textContent.",
                    "",
                    "Ingat: CSP (Content Security Policy) bisa jadi lapisan kedua",
                    "yang menahan skrip asing walau ada XSS yang lolos. Caranya",
                    "dibahas di bab 05.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kolom komentar, nama profil, ulasan produk, dan kotak",
                    "pencarian adalah tempat XSS paling sering ditemukan, karena",
                    "semuanya menampilkan ulang tulisan pengguna. SQL injection",
                    "paling sering muncul di fitur pencarian dan penyaringan yang",
                    "query-nya disusun dari beberapa pilihan pengguna.",
                    "",
                    "Kasus kecil: toko online kecil menampilkan ulasan pembeli apa",
                    "adanya. Seorang pembeli iseng menulis ulasan berisi tag",
                    "<b> yang belum ditutup, dan sejak itu seluruh halaman produk",
                    "jadi tebal. Pemilik toko minta kamu memperbaikinya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali gejalanya. Tag dari ulasan ikut ditafsirkan",
                    "     browser, artinya keluaran nggak di-escape. Kalau tag <b>",
                    "     bisa masuk, tag <script> juga bisa.",
                    "  2. Cari tempat ulasan ditampilkan, lalu escape di situ:",
                    "      \"<p>\" + html.escape(ulasan) + \"</p>\"",
                    "     atau hapus filter |safe kalau templatnya memakai Jinja2.",
                    "  3. Jangan menghapus tag dari data di database. Simpan apa",
                    "     adanya, escape saat menampilkan. Data mentahnya mungkin",
                    "     dipakai di tempat lain dengan konteks berbeda.",
                    "  4. Cek query pencarian ulasan juga. Kalau disusun dengan",
                    "     menyambung teks, ganti dengan placeholder ?.",
                ],
            },
        ],
    },
    {
        "title": "17. Desain Tidak Aman, Logging Lemah, dan Exception Bocor",
        "sections": [
            {
                "body": [
                    "Tiga kategori di materi ini jarang ketahuan lewat pemindai",
                    "otomatis. Celahnya ada di keputusan: apa yang dirancang, apa",
                    "yang dicatat, dan apa yang terjadi waktu ada yang gagal.",
                    "",
                    "A06 Insecure Design adalah celah di rancangan, sebelum satu",
                    "baris kode pun ditulis. Kodenya bisa rapi dan bebas bug, tapi",
                    "aturannya sendiri yang salah. Contohnya:",
                    "",
                    "  - Kode OTP enam digit yang boleh ditebak tanpa batas. Satu",
                    "    juta kemungkinan habis dicoba dalam hitungan jam.",
                    "  - Voucher diskon yang bisa dipakai berkali-kali karena",
                    "    rancangannya nggak menyebut \"satu kali per akun\".",
                    "  - Keranjang belanja yang menerima jumlah barang negatif,",
                    "    sehingga total belanja berkurang.",
                    "  - Reset password lewat pertanyaan rahasia seperti \"nama ibu",
                    "    kandung\", yang jawabannya sering ada di media sosial.",
                    "",
                    "Perbaikan kode nggak bisa menolong rancangan yang salah. Yang",
                    "menolong adalah threat modeling sebelum membangun, seperti di",
                    "materi Threat Modeling dengan STRIDE dan PASTA. Tulis juga",
                    "abuse case di samping user story: \"sebagai pembeli, saya",
                    "ingin pakai voucher\" dipasangkan dengan \"sebagai penipu,",
                    "saya ingin pakai voucher yang sama sepuluh kali\".",
                ],
            },
            {
                "heading": "A09: log yang menolong, bukan yang membocorkan",
                "body": [
                    "A09 Security Logging and Alerting Failures terjadi waktu",
                    "serangan berlangsung tapi nggak ada yang tahu. Lognya nggak",
                    "ada, atau ada tapi nggak dibaca, atau dibaca tapi nggak",
                    "pernah memicu peringatan.",
                    "",
                    "Kejadian yang wajib dicatat:",
                    "",
                    "  - Login berhasil dan gagal, beserta IP dan waktunya.",
                    "  - Akses yang ditolak (403, 404 untuk objek milik orang lain).",
                    "  - Perubahan hak: peran diubah, pengguna baru dibuat, password",
                    "    direset.",
                    "  - Masukan yang gagal validasi dalam jumlah besar.",
                    "",
                    "Yang nggak boleh masuk log: password, token sesi, kunci API,",
                    "kode OTP, nomor kartu lengkap, dan data pribadi yang nggak",
                    "perlu. Log biasanya dibaca lebih banyak orang daripada",
                    "database, dan disimpan lebih lama.",
                    "",
                    "Satu lagi: log injection. Kalau username berisi karakter baris",
                    "baru, penyerang bisa menyelipkan baris palsu yang kelihatan",
                    "seperti catatan sungguhan. Log berformat JSON menutup celah",
                    "ini, karena json.dumps mengubah baris baru jadi tulisan \\n.",
                ],
            },
            {
                "heading": "Log JSON dengan nilai rahasia disamarkan",
                "code": "import json\n\nRAHASIA = {\"password\", \"token\", \"otp\"}\n\n\ndef catat(aksi, **data):\n    bersih = {}\n    for kunci, nilai in data.items():\n        bersih[kunci] = \"***\" if kunci in RAHASIA else nilai\n    # json.dumps mengubah baris baru di nilai jadi \\n, jadi satu kejadian\n    # selalu tetap satu baris.\n    print(json.dumps({\"aksi\": aksi, **bersih}, separators=(\",\", \":\")))\n\n\ncatat(\"login_gagal\", user=\"budi\", ip=\"10.0.0.7\", password=\"rahasia123\")\ncatat(\"login_gagal\", user=\"budi\\nlogin_sukses admin\", ip=\"10.0.0.7\")\ncatat(\"peran_diubah\", oleh=\"sari\", target=\"wati\", peran=\"editor\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  {\"aksi\":\"login_gagal\",\"user\":\"budi\",\"ip\":\"10.0.0.7\",\"password\":\"***\"}",
                    "  {\"aksi\":\"login_gagal\",\"user\":\"budi\\nlogin_sukses admin\",\"ip\":\"10.0.0.7\"}",
                    "  {\"aksi\":\"peran_diubah\",\"oleh\":\"sari\",\"target\":\"wati\",\"peran\":\"editor\"}",
                    "",
                    "Baris kedua menunjukkan percobaan menyelipkan baris palsu",
                    "\"login_sukses admin\". Hasilnya tetap satu baris, dan baris",
                    "barunya tertulis sebagai \\n di dalam nilai user. Kunci",
                    "rahasia seperti password diganti tiga bintang sebelum",
                    "dicatat.",
                    "",
                    "Log baru berguna kalau ada yang membaca. Kirim log ke satu",
                    "tempat terpusat, lalu pasang peringatan untuk pola yang",
                    "jelas, misalnya lebih dari 20 login gagal per menit dari satu",
                    "IP. Cara membangun deteksi seperti itu dibahas di bab 09.",
                ],
            },
            {
                "heading": "A10: waktu program menemui keadaan tak terduga",
                "body": [
                    "A10 Mishandling of Exceptional Conditions adalah kategori baru",
                    "di 2025. Isinya program yang salah bersikap waktu ada error:",
                    "koneksi database putus, berkas nggak ada, masukan kosong, atau",
                    "layanan lain nggak menjawab. Ada tiga pola utama.",
                    "",
                    "Pertama, gagal terbuka (fail open). Fungsi pemeriksa izin",
                    "melempar exception, lalu kode pemanggilnya menangkap semua",
                    "error dan melanjutkan seolah izinnya ada. Bentuk yang benar",
                    "adalah gagal tertutup (fail closed): kalau ragu, tolak.",
                    "",
                    "Kedua, pesan error yang bocor. Traceback, pesan error SQL",
                    "lengkap dengan nama tabel, atau jalur berkas server membantu",
                    "penyerang menyusun serangan berikutnya. Pengguna cukup dapat",
                    "pesan umum plus kode kejadian. Detailnya ditulis ke log",
                    "server, ditandai kode yang sama.",
                    "",
                    "Ketiga, proses setengah jalan. Transfer saldo yang sudah",
                    "menambah saldo penerima tapi gagal mengurangi saldo pengirim",
                    "harus dibatalkan seluruhnya. Transaksi database ada untuk",
                    "itu.",
                ],
            },
            {
                "heading": "Transaksi yang dibatalkan utuh saat gagal",
                "code": """import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE saldo (nama TEXT PRIMARY KEY, uang INTEGER CHECK (uang >= 0))")
db.executemany("INSERT INTO saldo VALUES (?, ?)", [("ani", 100), ("budi", 50)])
db.commit()


def transfer(dari, ke, jumlah):
    try:
        with db:  # commit kalau sukses, rollback kalau ada exception
            db.execute("UPDATE saldo SET uang = uang + ? WHERE nama = ?", (jumlah, ke))
            db.execute("UPDATE saldo SET uang = uang - ? WHERE nama = ?", (jumlah, dari))
        return "berhasil"
    except sqlite3.IntegrityError:
        # Detail teknis cukup di log server; pengguna dapat pesan umum.
        return "gagal: saldo tidak cukup (kode TRF-01)"


print(transfer("ani", "budi", 30))
print(transfer("ani", "budi", 500))
print(db.execute("SELECT nama, uang FROM saldo ORDER BY nama").fetchall())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  berhasil",
                    "  gagal: saldo tidak cukup (kode TRF-01)",
                    "  [('ani', 70), ('budi', 80)]",
                    "",
                    "Transfer kedua sempat menambah 500 ke saldo Budi, lalu gagal",
                    "di UPDATE kedua karena saldo Ani akan jadi negatif dan",
                    "melanggar CHECK. Blok with db membatalkan dua-duanya, jadi",
                    "saldo Budi tetap 80. Pengguna menerima pesan umum dengan kode",
                    "TRF-01, tanpa nama tabel atau isi query.",
                    "",
                    "Jebakan: except Exception: pass, atau except kosong, adalah",
                    "cara tercepat membuat program gagal terbuka. Tangkap jenis",
                    "error yang memang kamu tahu cara menanganinya. Sisanya biarkan",
                    "naik ke penangan global yang mencatat detail ke log dan",
                    "menjawab pengguna dengan pesan umum.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman error yang menampilkan pesan database lengkap masih",
                    "sering ditemukan di aplikasi yang dibangun terburu-buru,",
                    "biasanya karena mode debug lupa dimatikan. Di sisi lain,",
                    "banyak kebocoran data baru ketahuan berbulan-bulan kemudian",
                    "karena nggak ada peringatan yang menyala.",
                    "",
                    "Kasus kecil: pengguna aplikasi pendaftaran kursus mengirim",
                    "tangkapan layar halaman error. Isinya traceback Python dengan",
                    "pesan sqlite3.OperationalError: no such column: emial, jalur",
                    "/home/deploy/app/db.py, dan potongan query lengkap.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Perbaiki penyebab langsungnya dulu: salah ketik emial di",
                    "     query.",
                    "  2. Matikan mode debug di produksi, lalu pasang penangan error",
                    "     global yang menjawab \"Terjadi kesalahan, kode kejadian",
                    "     E-7F3A\" dan menulis traceback lengkap ke log server",
                    "     dengan kode yang sama.",
                    "  3. Cek log untuk masa sebelum perbaikan. Kalau ada banyak",
                    "     error SQL dari satu IP dengan masukan aneh, anggap ada yang",
                    "     sedang mencoba injeksi, dan periksa query lain di modul",
                    "     yang sama.",
                    "  4. Pasang peringatan: lebih dari sepuluh error 500 dalam lima",
                    "     menit mengirim notifikasi ke tim.",
                ],
            },
        ],
    },
    {
        "title": "18. Rate Limiting, Brute Force, dan Perlindungan Login",
        "sections": [
            {
                "body": [
                    "Formulir login yang nggak dibatasi bisa dicoba ribuan kali per",
                    "menit oleh program. Ada tiga pola serangan yang sering",
                    "ketemu:",
                    "",
                    "  - Brute force: satu akun dicoba dengan banyak password",
                    "    sampai ada yang cocok.",
                    "  - Credential stuffing: pasangan email dan password yang",
                    "    bocor dari situs lain dicoba satu per satu di situsmu.",
                    "    Serangan ini berhasil karena banyak orang memakai password",
                    "    yang sama di banyak tempat.",
                    "  - Password spraying: satu password umum, misalnya",
                    "    Bandung2026!, dicoba ke banyak akun sekaligus, supaya tiap",
                    "    akun cuma gagal sekali.",
                    "",
                    "Pertahanan dasarnya rate limiting: membatasi berapa banyak",
                    "permintaan yang boleh datang dalam selang waktu tertentu.",
                    "Permintaan yang melebihi batas ditolak dengan status HTTP 429",
                    "Too Many Requests, biasanya disertai header Retry-After yang",
                    "memberi tahu berapa detik klien harus menunggu.",
                    "",
                    "Rate limiting juga melindungi hal lain: API publik yang",
                    "berkuota, endpoint mahal seperti ekspor laporan, dan server",
                    "dari satu klien yang menghabiskan seluruh kapasitas.",
                ],
            },
            {
                "heading": "Empat algoritme yang umum",
                "body": [
                    "  - Fixed window. Hitung permintaan per menit kalender, reset",
                    "    tiap pergantian menit. Paling sederhana, tapi penyerang",
                    "    bisa mengirim jatah penuh di detik terakhir menit pertama",
                    "    lalu jatah penuh lagi di detik pertama menit berikutnya.",
                    "  - Sliding window. Hitung permintaan dalam 60 detik terakhir",
                    "    dari sekarang, jadi lonjakan di batas menit hilang.",
                    "  - Token bucket. Bayangkan ember berisi token. Tiap",
                    "    permintaan mengambil satu token, dan ember terisi lagi",
                    "    pelan-pelan dengan laju tetap. Lonjakan kecil diizinkan",
                    "    selama embernya masih ada isi.",
                    "  - Leaky bucket. Permintaan masuk antrean dan diproses dengan",
                    "    laju tetap, seperti ember bocor yang meneteskan air.",
                    "    Hasilnya lalu lintas yang rata.",
                    "",
                    "Token bucket paling sering dipakai untuk API dan login, karena",
                    "ramah ke pengguna sah yang kadang mengklik dua kali, tapi",
                    "tetap menahan program yang mengirim terus-menerus.",
                ],
            },
            {
                "heading": "Token bucket dengan jam tiruan",
                "code": "class TokenBucket:\n    \"\"\"Ember berisi token. Tiap permintaan mengambil satu token.\"\"\"\n\n    def __init__(self, kapasitas, isi_per_detik):\n        self.kapasitas = float(kapasitas)\n        self.isi_per_detik = isi_per_detik\n        self.token = float(kapasitas)\n        self.terakhir = 0\n\n    def izinkan(self, sekarang):\n        # Tambah token sesuai waktu yang lewat, tapi jangan melebihi kapasitas.\n        lewat = sekarang - self.terakhir\n        self.token = min(self.kapasitas, self.token + lewat * self.isi_per_detik)\n        self.terakhir = sekarang\n        if self.token >= 1:\n            self.token -= 1\n            return True\n        return False\n\n\nember = TokenBucket(kapasitas=3, isi_per_detik=0.5)  # 1 token tiap 2 detik\nfor detik in [0, 0, 0, 0, 1, 2, 6, 6]:\n    hasil = \"izinkan\" if ember.izinkan(detik) else \"tolak 429\"\n    print(f\"detik {detik}: {hasil:<9} sisa token {ember.token}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  detik 0: izinkan   sisa token 2.0",
                    "  detik 0: izinkan   sisa token 1.0",
                    "  detik 0: izinkan   sisa token 0.0",
                    "  detik 0: tolak 429 sisa token 0.0",
                    "  detik 1: tolak 429 sisa token 0.5",
                    "  detik 2: izinkan   sisa token 0.0",
                    "  detik 6: izinkan   sisa token 1.0",
                    "  detik 6: izinkan   sisa token 0.0",
                    "",
                    "Tiga permintaan pertama di detik 0 lolos karena ember penuh.",
                    "Yang keempat ditolak. Di detik 1 baru ada setengah token, jadi",
                    "masih ditolak. Di detik 2 token genap satu lagi. Sesudah empat",
                    "detik tanpa permintaan, ember terisi dua token, jadi dua",
                    "permintaan di detik 6 lolos.",
                    "",
                    "Waktu di contoh ini jam tiruan, yaitu angka yang kita berikan",
                    "sendiri. Di aplikasi sungguhan, nilainya dari time.monotonic(),",
                    "jam yang nggak mundur walau jam sistem diubah. Jam tiruan",
                    "membuat perilakunya bisa diuji tanpa menunggu.",
                ],
            },
            {
                "heading": "Kunci pembatas: per IP, per akun, atau keduanya",
                "body": [
                    "Rate limiter perlu tahu siapa yang dihitung. Pilihannya:",
                    "",
                    "  - Per IP. Gampang, tapi banyak pengguna seluler di",
                    "    Indonesia berbagi satu IP publik lewat CGNAT (Carrier-Grade",
                    "    NAT), jadi batas yang terlalu ketat ikut menghukum orang",
                    "    lain. Penyerang juga bisa berganti IP.",
                    "  - Per akun. Menahan brute force ke satu akun dari banyak IP,",
                    "    tapi nggak menahan password spraying.",
                    "  - Per pasangan IP dan akun, ditambah batas global per IP",
                    "    yang lebih longgar. Kombinasi ini yang paling sering",
                    "    dipakai. Starter kit Laravel misalnya membatasi login 5 kali",
                    "    per menit per pasangan email dan IP.",
                    "",
                    "Penguncian akun (lockout) setelah sekian kali gagal juga",
                    "umum, tapi hati-hati. Kalau akun terkunci permanen sampai",
                    "admin membukanya, siapa pun bisa mengunci akun orang lain",
                    "dengan sengaja salah password lima kali. Pakai kunci",
                    "sementara yang makin lama tiap kali terulang, atau minta",
                    "CAPTCHA sesudah beberapa kali gagal. Panduan NIST SP 800-63B",
                    "menyarankan percobaan gagal beruntun per akun dibatasi",
                    "paling banyak 100 kali.",
                    "",
                    "Jebakan: pesan \"username tidak ditemukan\" dan \"password",
                    "salah\" yang berbeda memberi tahu penyerang akun mana yang",
                    "ada. Pakai satu pesan untuk dua-duanya, misalnya \"email atau",
                    "password salah\".",
                    "",
                    "Pertahanan terkuat untuk credential stuffing tetap MFA, yang",
                    "dibahas di materi Autentikasi: Password, MFA, dan Passkey.",
                ],
            },
            {
                "heading": "Membatasi di Nginx",
                "bahasa": "nginx",
                "code": """# Zona bernama login: 10 MB memori, laju 5 permintaan per menit per IP.
limit_req_zone $binary_remote_addr zone=login:10m rate=5r/m;

server {
    location = /login {
        limit_req zone=login burst=3 nodelay;
        limit_req_status 429;
        proxy_pass http://aplikasi;
    }
}""",
            },
            {
                "body": [
                    "Rate limiting bisa dipasang di beberapa lapisan. Di reverse",
                    "proxy seperti Nginx (limit_req di atas), di API gateway, di",
                    "layanan CDN atau WAF (Web Application Firewall), atau di kode",
                    "aplikasi. Lapisan depan murah dan cepat, tapi cuma kenal IP.",
                    "Lapisan aplikasi kenal akun dan bisa membedakan login gagal",
                    "dari login sukses.",
                    "",
                    "Kalau aplikasimu berjalan di beberapa server, penghitungnya",
                    "harus disimpan di tempat bersama, biasanya Redis. Penghitung",
                    "di memori tiap server membuat batas 5 kali jadi 5 kali",
                    "jumlah server.",
                    "",
                    "Serangan DDoS (Distributed Denial of Service) berskala besar",
                    "datang dari puluhan ribu mesin sekaligus dan bisa memenuhi",
                    "jaringan sebelum sampai ke aplikasimu. Rate limiting di",
                    "aplikasi nggak cukup untuk itu. Yang menahannya penyedia",
                    "jaringan, CDN, atau layanan perlindungan DDoS di depan",
                    "servermu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online dan aplikasi dompet digital rutin menerima",
                    "gelombang credential stuffing setiap kali ada kebocoran besar",
                    "di situs lain. Tandanya mudah dikenali di log: banyak login",
                    "gagal ke banyak akun berbeda, dari banyak IP, dengan pola",
                    "waktu yang terlalu teratur untuk manusia.",
                    "",
                    "Kasus kecil: dalam satu jam, endpoint /login aplikasi",
                    "katering langganan menerima 40 ribu percobaan gagal ke 12 ribu",
                    "akun dari 300 IP. Tiap IP cuma mencoba beberapa kali per",
                    "menit, jadi batas per IP yang longgar nggak pernah tersentuh.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambah pembatas per akun di aplikasi, di samping batas per",
                    "     IP, misalnya 5 percobaan per 15 menit per email.",
                    "  2. Tampilkan CAPTCHA sesudah 3 kali gagal untuk akun itu,",
                    "     supaya pengguna sah tetap bisa masuk.",
                    "  3. Pasang batas global: kalau login gagal di seluruh",
                    "     aplikasi melonjak sepuluh kali lipat dari biasanya,",
                    "     kirim peringatan ke tim.",
                    "  4. Paksa reset password untuk akun yang berhasil dimasuki",
                    "     dari IP yang ikut serangan, lalu tawarkan MFA.",
                    "  5. Pastikan pesan login gagal sama untuk email terdaftar dan",
                    "     tidak terdaftar.",
                ],
            },
        ],
    },
    {
        "title": "19. Header Keamanan, CORS, dan Cookie Aman",
        "sections": [
            {
                "body": [
                    "Banyak perlindungan di browser cuma menyala kalau server",
                    "memintanya. Cara memintanya lewat header HTTP, yaitu baris",
                    "keterangan yang ikut dikirim bersama tiap respons. Isi",
                    "halamannya sama persis, tapi browser bersikap beda tergantung",
                    "header yang menyertainya.",
                    "",
                    "Lima header yang paling penting:",
                    "",
                    "  - Content-Security-Policy (CSP). Daftar sumber yang boleh",
                    "    dimuat halaman: skrip, gaya, gambar, iframe. Kalau ada XSS",
                    "    yang lolos, skrip dari sumber yang nggak terdaftar ditolak",
                    "    browser.",
                    "  - Strict-Transport-Security (HSTS). Menyuruh browser selalu",
                    "    memakai HTTPS ke domain ini selama max-age detik, walau",
                    "    pengguna mengetik http://.",
                    "  - X-Content-Type-Options: nosniff. Melarang browser menebak",
                    "    jenis berkas. Tanpa ini, berkas teks yang diunggah",
                    "    pengguna bisa ditafsirkan sebagai skrip.",
                    "  - Referrer-Policy. Mengatur seberapa banyak alamat halaman",
                    "    asal yang dikirim ke situs lain saat pengguna mengklik",
                    "    tautan. URL kadang memuat token atau nomor pesanan.",
                    "  - Set-Cookie dengan atribut yang benar, dibahas di bawah.",
                ],
            },
            {
                "heading": "Middleware yang memasang header di setiap respons",
                "code": """HEADER_AMAN = {
    "Content-Security-Policy": "default-src 'self'; frame-ancestors 'none'",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


def pasang_header(respons):
    # Middleware: dipanggil untuk setiap respons sebelum dikirim.
    for nama, nilai in HEADER_AMAN.items():
        respons["header"].setdefault(nama, nilai)
    respons["header"].pop("Server", None)  # jangan umumkan versi server
    return respons


respons = {"status": 200, "header": {"Server": "nginx/1.18.0",
                                     "Content-Type": "text/html"}}
for nama, nilai in pasang_header(respons)["header"].items():
    print(f"{nama}: {nilai}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Content-Type: text/html",
                    "  Content-Security-Policy: default-src 'self'; frame-ancestors 'none'",
                    "  Strict-Transport-Security: max-age=31536000; includeSubDomains",
                    "  X-Content-Type-Options: nosniff",
                    "  Referrer-Policy: strict-origin-when-cross-origin",
                    "",
                    "Header dipasang di satu tempat yang dilewati semua respons,",
                    "jadi nggak ada halaman yang kelupaan. setdefault dipakai",
                    "supaya halaman yang butuh nilai khusus masih bisa menimpanya.",
                    "Di Flask, tempatnya fungsi after_request. Di Express ada paket",
                    "helmet. Di Nginx, perintah add_header.",
                    "",
                    "Arti nilai-nilainya:",
                    "",
                    "  - default-src 'self' artinya semua jenis sumber cuma boleh",
                    "    dari domain sendiri. Skrip inline (<script> yang isinya",
                    "    langsung di HTML) juga ditolak. Kalau terpaksa perlu skrip",
                    "    inline, pakai nonce, yaitu angka acak per respons yang",
                    "    ditulis di header dan di tag skripnya. Menambah",
                    "    'unsafe-inline' membuat CSP hampir nggak berguna melawan",
                    "    XSS.",
                    "  - frame-ancestors 'none' melarang halamanmu dimuat di iframe",
                    "    situs lain. Ini menahan clickjacking, yaitu tombol di",
                    "    situsmu ditutupi tampilan palsu supaya pengguna mengklik",
                    "    tanpa sadar. Header lama X-Frame-Options: DENY melakukan hal",
                    "    serupa dan masih boleh dipasang untuk browser tua.",
                    "  - max-age=31536000 sama dengan satu tahun. Browser",
                    "    mengabaikan HSTS yang dikirim lewat HTTP biasa, jadi header",
                    "    ini cuma berlaku dari respons HTTPS. Untuk masuk daftar",
                    "    preload browser, max-age minimal satu tahun dan",
                    "    includeSubDomains wajib ada.",
                    "  - strict-origin-when-cross-origin mengirim alamat lengkap ke",
                    "    situs sendiri, tapi cuma nama domain ke situs lain. Ini",
                    "    juga perilaku bawaan browser modern kalau header-nya nggak",
                    "    ada.",
                    "",
                    "Jebakan: menyalakan CSP ketat langsung di produksi bisa",
                    "mematikan skrip analitik atau widget pembayaran. Mulai dengan",
                    "Content-Security-Policy-Report-Only, yang cuma melaporkan",
                    "pelanggaran tanpa memblokir, lalu ketatkan bertahap.",
                ],
            },
            {
                "heading": "Cookie dengan atribut lengkap",
                "bahasa": "http",
                "code": """HTTP/1.1 200 OK
Set-Cookie: __Host-sesi=8f3a2c; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=3600""",
            },
            {
                "body": [
                    "Cookie sesi adalah tanda pengenal pengguna yang sudah login.",
                    "Siapa pun yang memegangnya dianggap pengguna itu. Atributnya",
                    "menentukan siapa yang bisa memegangnya:",
                    "",
                    "  - Secure: cookie cuma dikirim lewat HTTPS.",
                    "  - HttpOnly: JavaScript di halaman nggak bisa membaca cookie",
                    "    lewat document.cookie, jadi XSS nggak bisa langsung",
                    "    mencurinya.",
                    "  - SameSite: mengatur apakah cookie ikut terkirim pada",
                    "    permintaan yang berasal dari situs lain. Strict nggak",
                    "    pernah ikut. Lax ikut hanya saat pengguna membuka tautan",
                    "    biasa (navigasi GET). None selalu ikut dan wajib disertai",
                    "    Secure. Beberapa browser, misalnya Chrome, memperlakukan",
                    "    cookie tanpa SameSite sebagai Lax.",
                    "  - Awalan __Host- di nama cookie memaksa browser menolak",
                    "    cookie itu kecuali ia Secure, Path=/, dan tanpa atribut",
                    "    Domain. Cookie jadi terikat ke satu nama host saja.",
                    "",
                    "SameSite=Lax menahan sebagian besar CSRF (Cross-Site Request",
                    "Forgery), yaitu situs jahat yang membuat browser korban",
                    "mengirim formulir ke situsmu dengan cookie korban. Untuk aksi",
                    "penting, token CSRF di formulir tetap dianjurkan.",
                ],
            },
            {
                "heading": "CORS: yang dicegah dan yang nggak",
                "body": [
                    "Browser punya aturan dasar namanya same-origin policy: skrip",
                    "dari situs A nggak boleh membaca respons dari situs B. Origin",
                    "adalah gabungan skema, domain, dan port, misalnya",
                    "https://toko.example:443.",
                    "",
                    "CORS (Cross-Origin Resource Sharing) adalah cara server B",
                    "melonggarkan aturan itu untuk origin tertentu, lewat header",
                    "seperti ini:",
                    "",
                    "  Access-Control-Allow-Origin: https://admin.toko.example",
                    "  Access-Control-Allow-Credentials: true",
                    "",
                    "Untuk permintaan yang bukan GET atau POST sederhana, browser",
                    "lebih dulu mengirim permintaan OPTIONS yang disebut preflight,",
                    "untuk bertanya apakah server mengizinkan.",
                    "",
                    "Hal yang sering disalahpahami: CORS nggak melindungi servermu",
                    "dari permintaan. curl, Postman, dan skrip Python sama sekali",
                    "nggak peduli CORS. Yang diatur CORS cuma satu: boleh nggak",
                    "JavaScript di origin lain membaca jawaban server di browser",
                    "korban. Autentikasi dan otorisasi tetap harus ada di server.",
                    "",
                    "Ingat: kesalahan CORS paling berbahaya adalah server yang",
                    "menyalin isi header Origin apa pun ke",
                    "Access-Control-Allow-Origin sambil mengizinkan credentials.",
                    "Artinya situs mana pun boleh membaca data pengguna yang sedang",
                    "login. Tulis daftar origin yang diizinkan secara eksplisit.",
                    "Nilai * memang ada, tapi browser menolaknya kalau dipakai",
                    "bersama credentials.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mozilla HTTP Observatory, yang sekarang ada di situs MDN,",
                    "memberi nilai pada header keamanan sebuah situs dan",
                    "menjelaskan header mana yang kurang. Banyak tim memakainya,",
                    "atau pemindai sejenis di pipeline, sebelum rilis.",
                    "",
                    "Kasus kecil: pemindai memberi panel admin toko online milik",
                    "timmu nilai F. Hasilnya: nggak ada CSP, nggak ada HSTS, cookie",
                    "sesi tanpa Secure dan HttpOnly, dan CORS menyalin Origin apa",
                    "pun dengan credentials.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Perbaiki cookie dulu, karena risikonya paling langsung:",
                    "      Set-Cookie: __Host-sesi=...; Path=/; Secure; HttpOnly;",
                    "        SameSite=Lax",
                    "  2. Ganti CORS jadi daftar putih origin yang memang memanggil",
                    "     API ini. Kalau panel admin cuma dipanggil dari domainnya",
                    "     sendiri, CORS nggak perlu diaktifkan sama sekali.",
                    "  3. Pasang HSTS dengan max-age pendek dulu, misalnya 300",
                    "     detik, pastikan semua subdomain sudah HTTPS, baru naikkan",
                    "     ke 31536000.",
                    "  4. Pasang CSP dalam mode Report-Only selama seminggu, baca",
                    "     laporannya, lalu ubah jadi Content-Security-Policy.",
                    "  5. Tambahkan nosniff dan Referrer-Policy, lalu pindai ulang.",
                ],
            },
        ],
    },
    {
        "title": "20. Keamanan API: Skema, Kunci API, dan Logging Aman",
        "sections": [
            {
                "body": [
                    "API (Application Programming Interface) di sini artinya",
                    "alamat-alamat di server yang dipanggil program lain, misalnya",
                    "aplikasi seluler atau frontend React, dan menjawab dengan",
                    "JSON. API lebih gampang disalahgunakan daripada halaman web,",
                    "karena penyerang nggak perlu tampilan sama sekali. Ia cukup",
                    "mengirim JSON buatannya sendiri.",
                    "",
                    "Proyek OWASP punya daftar khusus untuk API. Edisi terbarunya",
                    "saat materi ini ditulis masih 2023:",
                    "",
                    "  API1  Broken Object Level Authorization (sama dengan IDOR)",
                    "  API2  Broken Authentication",
                    "  API3  Broken Object Property Level Authorization",
                    "  API4  Unrestricted Resource Consumption",
                    "  API5  Broken Function Level Authorization",
                    "  API6  Unrestricted Access to Sensitive Business Flows",
                    "  API7  Server Side Request Forgery",
                    "  API8  Security Misconfiguration",
                    "  API9  Improper Inventory Management",
                    "  API10 Unsafe Consumption of APIs",
                    "",
                    "Sebagian sudah kamu kenal dari bab 04. Materi ini fokus ke",
                    "tiga kebiasaan yang menutup banyak nomor sekaligus: validasi",
                    "skema, kunci API yang dikelola dengan benar, dan log yang",
                    "nggak membocorkan data.",
                ],
            },
            {
                "heading": "Validasi skema: tolak yang nggak dikenal",
                "code": """SKEMA = {
    "nama": {"tipe": str, "maks": 50},
    "jumlah": {"tipe": int, "min": 1, "maks": 99},
    "catatan": {"tipe": str, "maks": 200, "opsional": True},
}


def validasi(data):
    galat = []
    for kunci in data:
        if kunci not in SKEMA:
            galat.append(f"{kunci}: field tidak dikenal")
    for kunci, aturan in SKEMA.items():
        if kunci not in data:
            if not aturan.get("opsional"):
                galat.append(f"{kunci}: wajib ada")
            continue
        nilai = data[kunci]
        if type(nilai) is not aturan["tipe"]:
            galat.append(f"{kunci}: harus {aturan['tipe'].__name__}")
        elif isinstance(nilai, str) and len(nilai) > aturan["maks"]:
            galat.append(f"{kunci}: paling panjang {aturan['maks']} huruf")
        elif isinstance(nilai, int) and not aturan["min"] <= nilai <= aturan["maks"]:
            galat.append(f"{kunci}: harus {aturan['min']} sampai {aturan['maks']}")
    return galat


permintaan = [
    {"nama": "Kopi susu", "jumlah": 2},
    {"nama": "Kopi susu", "jumlah": -5},
    {"nama": "Kopi susu", "jumlah": "2", "is_admin": True},
]
for data in permintaan:
    galat = validasi(data)
    print("DITERIMA" if not galat else "DITOLAK: " + "; ".join(galat))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  DITERIMA",
                    "  DITOLAK: jumlah: harus 1 sampai 99",
                    "  DITOLAK: is_admin: field tidak dikenal; jumlah: harus int",
                    "",
                    "Permintaan kedua ditolak karena jumlah negatif, celah desain",
                    "yang sudah kamu lihat di bab 04. Permintaan ketiga lebih",
                    "menarik. Field is_admin nggak ada di skema, dan ini pola",
                    "API3 (sering disebut mass assignment). Kode yang menyalin",
                    "seluruh JSON ke objek pengguna, misalnya",
                    "pengguna.update(**data), akan ikut mengubah is_admin. Skema",
                    "yang menolak field tak dikenal menutup celah itu.",
                    "",
                    "Hal yang sama berlaku ke arah sebaliknya. Jangan kirim seluruh",
                    "baris database ke klien lalu berharap aplikasinya cuma",
                    "menampilkan sebagian. Pilih field yang memang boleh dilihat.",
                    "Kolom hash_password, alamat lengkap, dan catatan internal",
                    "nggak boleh ikut walau tampilannya nggak memakainya.",
                    "",
                    "Di dunia nyata kamu jarang menulis validator sendiri. Ada JSON",
                    "Schema yang bisa dipakai lintas bahasa, spesifikasi OpenAPI",
                    "yang menggambarkan seluruh API, Pydantic di Python (dipakai",
                    "FastAPI), dan Zod di TypeScript. Konsepnya sama dengan contoh",
                    "di atas: tipe, batas, field wajib, dan tolak sisanya.",
                    "",
                    "Batasi juga ukuran. Body permintaan maksimal sekian kilobyte,",
                    "daftar hasil dipaginasi dengan batas atas (misalnya ?limit=",
                    "paling besar 100), dan tiap permintaan punya batas waktu.",
                    "Tanpa itu, satu permintaan ?limit=1000000 bisa menghabiskan",
                    "memori server. Itulah API4.",
                ],
            },
            {
                "heading": "Kunci API: identitas aplikasi, bukan pengguna",
                "code": """import hashlib
import hmac

# Kunci dibuat sekali dengan secrets.token_urlsafe(32), ditampilkan ke pemilik,
# lalu yang disimpan cuma hash-nya. Di sini ditulis tetap supaya hasilnya sama.
kunci_asli = "tk_live_Q2hhbmdlTWVJblByb2R1Y3Rpb24hIQ"
tersimpan = {
    "awalan": kunci_asli[:12],
    "sha256": hashlib.sha256(kunci_asli.encode()).hexdigest(),
    "izin": ["pesanan:baca"],
}


def periksa(kunci_dikirim):
    hash_dikirim = hashlib.sha256(kunci_dikirim.encode()).hexdigest()
    # compare_digest membandingkan tanpa bocor lewat lama waktu.
    return hmac.compare_digest(hash_dikirim, tersimpan["sha256"])


print("awalan untuk dikenali:", tersimpan["awalan"])
print("kunci benar :", periksa(kunci_asli))
print("kunci salah :", periksa("tk_live_tebak-tebakan"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  awalan untuk dikenali: tk_live_Q2hh",
                    "  kunci benar : True",
                    "  kunci salah : False",
                    "",
                    "Kunci API mengenali aplikasi atau integrasi yang memanggil,",
                    "misalnya server kasir yang mengirim data penjualan. Aturan",
                    "mengelolanya:",
                    "",
                    "  - Buat dengan secrets, panjang dan acak. Tampilkan sekali",
                    "    saja ke pemiliknya, lalu simpan hash-nya, persis seperti",
                    "    password.",
                    "  - SHA-256 polos cukup untuk kunci API, walau nggak cukup",
                    "    untuk password. Kunci acak 32 byte nggak bisa ditebak",
                    "    lewat kamus, jadi hash lambat seperti PBKDF2 nggak",
                    "    diperlukan.",
                    "  - Beri awalan yang jelas, misalnya tk_live_. Awalan membantu",
                    "    pemilik mengenali kuncinya di dasbor, dan membantu pemindai",
                    "    rahasia menemukan kunci yang bocor ke GitHub. Token GitHub",
                    "    sendiri memakai awalan seperti ghp_.",
                    "  - Batasi izinnya (scope), beri masa berlaku, dan sediakan",
                    "    tombol untuk mencabut dan membuat ulang.",
                    "  - Kirim lewat header, misalnya Authorization: Bearer ...,",
                    "    bukan di URL. URL tercatat di log server, riwayat browser,",
                    "    dan header Referer.",
                    "",
                    "Jebakan: kunci API yang ditanam di aplikasi seluler atau di",
                    "JavaScript frontend bukan rahasia lagi. Siapa pun bisa",
                    "membongkar aplikasinya dan menemukan kunci itu. Kunci seperti",
                    "itu cuma boleh punya izin yang memang aman untuk publik.",
                ],
            },
            {
                "heading": "Log API yang aman",
                "body": [
                    "Log API sebaiknya menjawab siapa memanggil apa, kapan, dan",
                    "hasilnya apa: ID permintaan, awalan kunci atau ID pengguna,",
                    "metode dan jalur, status, dan lama proses. Itu cukup untuk",
                    "menyelidiki insiden.",
                    "",
                    "Yang nggak boleh ikut tercatat:",
                    "",
                    "  - Header Authorization dan Cookie, utuh maupun sebagian",
                    "    besar.",
                    "  - Body permintaan login, reset password, dan pembayaran.",
                    "  - Nomor kartu lengkap, NIK, nomor telepon, dan alamat,",
                    "    kecuali memang wajib dan sudah disamarkan, misalnya",
                    "    nomor kartu cuma empat digit terakhir.",
                    "  - Query string yang memuat token.",
                    "",
                    "Simpan juga daftar semua API yang hidup, termasuk versi lama",
                    "seperti /v1 yang masih menyala. Endpoint lama yang terlupakan",
                    "biasanya nggak ikut diperbarui pengamannya. Itulah API9.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Penyedia API besar, misalnya layanan pembayaran dan GitHub,",
                    "memakai kunci berawalan yang bisa dikenali, menampilkan kunci",
                    "baru sekali saja, dan menyediakan tombol rotasi. GitHub juga",
                    "memindai repositori publik untuk menemukan token yang bocor.",
                    "",
                    "Kasus kecil: aplikasi seluler sebuah klinik memanggil",
                    "GET /api/dokter/12 dan menampilkan nama serta jadwal. Saat",
                    "menguji API itu di server staging milik tim sendiri, kamu",
                    "melihat JSON-nya ternyata juga memuat nomor HP pribadi dan",
                    "NIK dokter, walau aplikasinya nggak menampilkannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Anggap data itu sudah bocor, karena siapa pun yang",
                    "     memasang aplikasi bisa melihat JSON-nya. Laporkan ke",
                    "     pemimpin tim.",
                    "  2. Buat skema respons publik yang cuma berisi field yang",
                    "     ditampilkan:",
                    "      {\"id\": 12, \"nama\": \"...\", \"spesialis\": \"...\",",
                    "       \"jadwal\": [...]}",
                    "  3. Ubah handler supaya membangun respons dari skema itu,",
                    "     bukan mengirim seluruh baris database.",
                    "  4. Cek endpoint lain dengan pola yang sama, termasuk versi",
                    "     lama seperti /api/v1 yang mungkin masih hidup.",
                    "  5. Pastikan log API nggak mencatat body respons yang memuat",
                    "     data pribadi.",
                ],
            },
        ],
    },
    {
        "title": "21. Manajemen Rahasia: Kunci Tidak Boleh Ada di Kode",
        "sections": [
            {
                "body": [
                    "Rahasia (secret) adalah nilai yang memberi akses ke sesuatu:",
                    "password database, kunci API layanan pembayaran, token bot,",
                    "kunci privat SSH, kunci penanda tangan token. Siapa pun yang",
                    "memegangnya bisa bertindak atas nama aplikasimu.",
                    "",
                    "Cara paling gampang menyimpan rahasia adalah menulisnya",
                    "langsung di kode:",
                    "",
                    "  DB_PASSWORD = \"rahasia123\"",
                    "",
                    "Masalahnya, kode berpindah ke banyak tempat. Ia masuk riwayat",
                    "Git dan tetap ada di sana walau barisnya dihapus di commit",
                    "berikutnya. Ia ikut ter-clone ke laptop setiap anggota tim,",
                    "tersalin ke server CI, terbungkus di image container, dan",
                    "kalau repositorinya pernah publik walau sebentar, bisa sudah",
                    "diambil program pemindai otomatis.",
                    "",
                    "Ingat: apa pun yang dikirim ke browser atau dipaket di",
                    "aplikasi seluler itu publik. Kunci di JavaScript frontend atau",
                    "di berkas APK bisa dibaca siapa pun yang mau repot",
                    "membongkarnya.",
                ],
            },
            {
                "heading": "Langkah pertama: variabel lingkungan",
                "code": """import os

WAJIB = ["TOKO_DB_URL", "TOKO_DB_PASS", "TOKO_KUNCI_BAYAR"]


def muat_konfigurasi():
    kurang = [nama for nama in WAJIB if not os.environ.get(nama)]
    if kurang:
        # Gagal tertutup: lebih baik aplikasi menolak menyala daripada
        # berjalan dengan password kosong atau nilai bawaan.
        raise SystemExit("konfigurasi belum lengkap: " + ", ".join(kurang))
    return {nama: os.environ[nama] for nama in WAJIB}


try:
    konfigurasi = muat_konfigurasi()
except SystemExit as e:
    print(e)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  konfigurasi belum lengkap: TOKO_DB_URL, TOKO_DB_PASS, TOKO_KUNCI_BAYAR",
                    "",
                    "Program ini mengambil rahasia dari variabel lingkungan",
                    "(environment variable), yaitu nilai yang dipasang di proses",
                    "dari luar, bukan ditulis di kode. Karena di sini belum ada",
                    "yang dipasang, program menolak menyala dan menyebut apa saja",
                    "yang kurang. Itu jauh lebih baik daripada menyala sambil",
                    "memakai password kosong tanpa ada yang tahu.",
                    "",
                    "Cara ini bagian dari prinsip The Twelve-Factor App: konfigurasi",
                    "yang berbeda per lingkungan disimpan di environment. Untuk",
                    "pengembangan lokal, nilainya sering ditaruh di berkas .env",
                    "yang dibaca pustaka seperti python-dotenv. Berkas .env wajib",
                    "masuk .gitignore. Yang boleh di-commit cuma .env.example",
                    "berisi nama variabel tanpa nilai.",
                    "",
                    "Variabel lingkungan punya batas. Nilainya bisa terbaca proses",
                    "lain milik user yang sama, ikut tercetak di laporan error, dan",
                    "diwarisi semua proses anak. Untuk produksi, tempat yang lebih",
                    "baik adalah layanan manajemen rahasia.",
                ],
            },
            {
                "heading": "Layanan manajemen rahasia di cloud",
                "body": [
                    "Tiga penyedia cloud besar masing-masing punya layanan sendiri:",
                    "",
                    "  Layanan               Penyedia   Isinya",
                    "  Secrets Manager       AWS        rahasia + rotasi otomatis",
                    "  KMS                   AWS        kunci enkripsi",
                    "  Secret Manager        Google     rahasia berversi",
                    "  Key Vault             Azure      rahasia, kunci, sertifikat",
                    "",
                    "Cara pakainya mirip. Aplikasi berjalan dengan identitas cloud",
                    "(misalnya IAM role di AWS), lalu meminta rahasia lewat API",
                    "saat menyala. Izin baca diatur per rahasia, setiap akses",
                    "tercatat di log audit, dan rahasia bisa punya beberapa versi",
                    "sehingga rotasi nggak memutus aplikasi yang sedang berjalan.",
                    "AWS Secrets Manager bisa merotasi password database sendiri",
                    "lewat fungsi Lambda terjadwal.",
                    "",
                    "KMS (Key Management Service) agak beda. Ia menyimpan kunci",
                    "enkripsi yang nggak pernah keluar dari layanannya. Pola",
                    "umumnya envelope encryption: data dienkripsi dengan kunci data",
                    "acak, lalu kunci data itu dienkripsi dengan kunci induk di",
                    "KMS. Yang disimpan di samping data cuma kunci data versi",
                    "terenkripsi.",
                    "",
                    "Bagian penting yang sering terlewat adalah kredensial untuk",
                    "mengakses layanan rahasia itu sendiri. Jawabannya identitas",
                    "bawaan platform, bukan kunci statis lagi. Detailnya ada di",
                    "kurikulum DevOps, materi AWS IAM: Siapa Boleh Melakukan Apa",
                    "dan GitHub Actions: Secrets, OIDC, dan Keamanan Workflow.",
                ],
            },
            {
                "heading": "Kalau rahasia terlanjur bocor",
                "body": [
                    "Anggap rahasia yang pernah ter-commit sudah bocor, walau",
                    "repositorinya privat dan commit-nya sudah dihapus. Urutannya:",
                    "",
                    "  1. Cabut dan ganti dulu. Buat kunci baru, pasang di",
                    "     aplikasi, lalu matikan kunci lama. Langkah ini yang",
                    "     menghentikan kerugian.",
                    "  2. Periksa log akses layanan itu sejak rahasia ter-commit.",
                    "     Ada pemakaian dari IP atau waktu yang aneh?",
                    "  3. Bersihkan riwayat Git dengan git filter-repo kalau perlu.",
                    "     Langkah ini cuma merapikan; salinan yang sudah di-clone",
                    "     orang lain nggak ikut terhapus.",
                    "  4. Pasang pencegah supaya nggak terulang.",
                    "",
                    "Untuk pencegahan, GitHub punya secret scanning dan push",
                    "protection, yang menolak push berisi pola rahasia yang",
                    "dikenal. Push protection aktif secara bawaan untuk repositori",
                    "publik. Di laptop sendiri, alat seperti Gitleaks bisa",
                    "dipasang sebagai pre-commit hook. Pemindaian rahasia di",
                    "pipeline dibahas di bab 07.",
                    "",
                    "Jebakan: menghapus baris rahasia di commit baru nggak",
                    "menghapusnya dari riwayat. git log -p masih menampilkannya,",
                    "dan pemindai rahasia memang membaca seluruh riwayat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pada Oktober 2022, Toyota mengumumkan bahwa kunci akses ke",
                    "server data layanan T-Connect ikut terunggah ke GitHub",
                    "bersama sebagian kode sumbernya, dan terpampang di sana",
                    "hampir lima tahun. Kasus seperti ini terus berulang di banyak",
                    "perusahaan, dan hampir selalu bermula dari satu berkas",
                    "konfigurasi yang ikut ter-commit.",
                    "",
                    "Kasus kecil: anak magang di timmu tanpa sengaja meng-commit",
                    "berkas .env berisi server key payment gateway ke repositori",
                    "GitHub publik. Lima belas menit kemudian ia sadar dan",
                    "menghapus berkas itu di commit berikutnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka dasbor payment gateway, buat server key baru, pasang",
                    "     di server produksi, lalu nonaktifkan key lama. Lima belas",
                    "     menit sudah cukup untuk dipungut pemindai otomatis.",
                    "  2. Periksa riwayat transaksi dan log API sejak commit itu",
                    "     untuk aktivitas yang nggak dikenal.",
                    "  3. Tambahkan .env ke .gitignore, commit .env.example tanpa",
                    "     nilai, dan pasang Gitleaks sebagai pre-commit hook.",
                    "  4. Pindahkan key produksi ke secret manager supaya laptop",
                    "     developer nggak perlu menyimpannya sama sekali.",
                    "  5. Jangan menyalahkan anak magangnya. Catat kejadiannya dan",
                    "     perbaiki prosesnya supaya kesalahan yang sama ditolak",
                    "     sebelum sampai ke GitHub.",
                ],
            },
        ],
    },
    {
        "title": "22. Vault dan OpenBao: Brankas Rahasia Terpusat",
        "sections": [
            {
                "body": [
                    "Kalau aplikasimu berjalan di banyak server, di beberapa cloud,",
                    "atau di pusat data sendiri, layanan rahasia milik satu",
                    "penyedia cloud mulai terasa sempit. Di situ orang memakai",
                    "brankas rahasia terpusat yang bisa dipasang sendiri.",
                    "",
                    "HashiCorp Vault adalah yang paling banyak dipakai. Vault",
                    "ditulis dengan Go. Saat materi ini ditulis (Oktober 2026),",
                    "rilis stabil terbarunya v2.2.0, terbit 15 Oktober 2026.",
                    "Lisensinya BUSL-1.1 (Business Source License) sejak Agustus",
                    "2023. Kodenya boleh dibaca dan dipakai, tapi nggak boleh",
                    "dipakai untuk membuat layanan yang bersaing dengan HashiCorp,",
                    "jadi nggak termasuk open source menurut definisi OSI. HashiCorp",
                    "sendiri sekarang bagian dari IBM.",
                    "",
                    "Perubahan lisensi itu melahirkan OpenBao, fork Vault dari kode",
                    "terakhir yang masih berlisensi MPL-2.0. OpenBao dikelola",
                    "komunitas di bawah OpenSSF, bagian dari Linux Foundation.",
                    "Rilis terbarunya v2.7.1 (1 Oktober 2026). Nama perintahnya",
                    "bao. Konsep dan sebagian besar API-nya sama dengan Vault,",
                    "jadi semua yang kamu pelajari di sini berlaku untuk",
                    "keduanya.",
                ],
            },
            {
                "heading": "Konsep utama",
                "body": [
                    "  - Secrets engine: modul yang menyimpan atau membuat rahasia.",
                    "    KV (key-value) menyimpan rahasia statis berversi. Engine",
                    "    database membuat user database baru setiap kali diminta.",
                    "    Engine transit mengenkripsi data tanpa memberikan",
                    "    kuncinya. Engine PKI menerbitkan sertifikat.",
                    "  - Auth method: cara aplikasi membuktikan dirinya ke Vault,",
                    "    misalnya AppRole, service account Kubernetes, OIDC, atau",
                    "    identitas cloud. Hasilnya token Vault yang berumur pendek.",
                    "  - Policy: aturan path mana yang boleh dibaca atau ditulis",
                    "    oleh token tertentu.",
                    "  - Lease: masa berlaku. Rahasia dinamis selalu punya lease,",
                    "    dan begitu lease habis atau dicabut, kredensialnya ikut",
                    "    dihapus.",
                    "  - Audit device: log setiap permintaan ke Vault, termasuk",
                    "    yang ditolak.",
                    "  - Seal dan unseal: Vault menyimpan datanya terenkripsi. Saat",
                    "    baru menyala ia dalam keadaan tersegel dan nggak bisa",
                    "    membaca apa pun sampai dibuka, baik dengan beberapa",
                    "    potongan kunci yang dipegang orang berbeda (Shamir), atau",
                    "    otomatis lewat KMS cloud.",
                    "",
                    "Yang membuat Vault beda dari sekadar tempat menyimpan adalah",
                    "dynamic secrets. Aplikasi nggak lagi memegang satu password",
                    "database yang berlaku selamanya. Tiap kali butuh, ia meminta",
                    "ke Vault, dan Vault membuat user database baru yang berlaku,",
                    "misalnya, satu jam. Kalau kredensial itu bocor, umurnya",
                    "pendek, dan log audit menunjukkan siapa yang memintanya.",
                ],
            },
            {
                "heading": "Tiruan dynamic secrets dengan jam tiruan",
                "code": "class BrankasMini:\n    \"\"\"Tiruan konsep dynamic secrets: kredensial dibuat saat diminta,\n    punya masa berlaku (lease), dan tiap akses dicatat.\"\"\"\n\n    def __init__(self):\n        self.lease = {}\n        self.audit = []\n        self.nomor = 0\n\n    def minta(self, peminta, peran, ttl, sekarang):\n        self.nomor += 1\n        user = f\"v-{peran}-{self.nomor}\"\n        self.lease[user] = sekarang + ttl\n        self.audit.append(f\"t={sekarang} {peminta} minta {peran} -> {user}\")\n        return user\n\n    def bersihkan(self, sekarang):\n        for user, habis in list(self.lease.items()):\n            if habis <= sekarang:\n                del self.lease[user]\n                self.audit.append(f\"t={sekarang} lease {user} habis, user dihapus\")\n\n    def cabut(self, user, sekarang):\n        self.lease.pop(user, None)\n        self.audit.append(f\"t={sekarang} lease {user} dicabut manual\")\n\n\nb = BrankasMini()\nb.minta(\"api-pesanan\", \"baca\", ttl=3600, sekarang=0)\nb.minta(\"laporan-malam\", \"baca\", ttl=600, sekarang=100)\nb.bersihkan(sekarang=900)\nb.cabut(\"v-baca-1\", sekarang=1000)\nb.minta(\"api-pesanan\", \"baca\", ttl=3600, sekarang=1001)\nprint(\"lease aktif:\", sorted(b.lease))\nfor baris in b.audit:\n    print(baris)",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  lease aktif: ['v-baca-3']",
                    "  t=0 api-pesanan minta baca -> v-baca-1",
                    "  t=100 laporan-malam minta baca -> v-baca-2",
                    "  t=900 lease v-baca-2 habis, user dihapus",
                    "  t=1000 lease v-baca-1 dicabut manual",
                    "  t=1001 api-pesanan minta baca -> v-baca-3",
                    "",
                    "Ini tiruan konsepnya saja, tanpa enkripsi dan tanpa database",
                    "sungguhan. Perhatikan tiga hal. Tiap peminta dapat user",
                    "sendiri, jadi log audit bisa menunjuk siapa memakai apa. User",
                    "laporan-malam hilang sendiri begitu lease 600 detiknya habis.",
                    "Dan saat v-baca-1 dicurigai bocor, cukup cabut lease itu;",
                    "aplikasi tinggal meminta kredensial baru.",
                    "",
                    "Python stdlib nggak punya AES, jadi contoh ini nggak",
                    "mengenkripsi apa pun. Jangan menulis algoritme enkripsi",
                    "sendiri untuk produksi; biarkan Vault atau KMS yang",
                    "mengerjakannya.",
                ],
            },
            {
                "heading": "Mencoba Vault di laptop sendiri",
                "bahasa": "terminal",
                "code": """# Mode dev: data di memori, langsung terbuka, ada root token. Hanya untuk belajar.
vault server -dev

# Di terminal lain
export VAULT_ADDR=http://127.0.0.1:8200
vault kv put secret/toko db_password=contoh-saja
vault kv get -field=db_password secret/toko
vault kv metadata get secret/toko      # lihat daftar versi""",
            },
            {
                "heading": "Policy yang cuma boleh membaca",
                "bahasa": "hcl",
                "code": """# Aplikasi toko cuma boleh membaca rahasia miliknya sendiri.
path "secret/data/toko/*" {
  capabilities = ["read"]
}

path "database/creds/toko-baca" {
  capabilities = ["read"]
}""",
            },
            {
                "body": [
                    "Mode dev menyimpan semuanya di memori, langsung dalam keadaan",
                    "terbuka, dan mencetak root token di layar. Cocok untuk",
                    "mencoba perintah, dan berbahaya kalau dipakai di server",
                    "sungguhan. Vault produksi butuh penyimpanan permanen (Vault",
                    "punya penyimpanan bawaan bernama integrated storage), TLS,",
                    "minimal tiga node supaya tetap hidup kalau satu mati, dan",
                    "prosedur unseal yang jelas.",
                    "",
                    "Jebakan: root token dari proses inisialisasi nggak boleh",
                    "dipakai untuk pekerjaan sehari-hari. Pakai untuk membuat",
                    "policy dan akun admin pertama, lalu cabut. Siapa pun yang",
                    "memegang root token bisa membaca seluruh isi brankas.",
                    "",
                    "Kapan memilih Vault atau OpenBao, dan kapan cukup layanan",
                    "cloud? Kalau semua aplikasimu tinggal di satu cloud, layanan",
                    "bawaan cloud itu lebih murah dirawat. Vault atau OpenBao",
                    "masuk akal kalau kamu butuh dynamic secrets ke banyak jenis",
                    "sistem, berjalan di beberapa cloud atau pusat data sendiri,",
                    "atau butuh PKI internal. Pilih OpenBao kalau lisensi open",
                    "source jadi syarat, misalnya untuk produk yang kamu jual",
                    "ulang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Vault sering dipasang di klaster Kubernetes. Aplikasi masuk",
                    "dengan service account-nya, dan Vault Agent atau External",
                    "Secrets Operator (materi berikutnya) menyalurkan rahasia ke",
                    "pod. Tim keamanan biasanya memakai log audit Vault untuk",
                    "menjawab pertanyaan \"siapa yang membaca rahasia ini minggu",
                    "lalu\".",
                    "",
                    "Kasus kecil: lima layanan di perusahaanmu memakai satu user",
                    "database bernama app dengan password yang sama sejak tiga",
                    "tahun lalu. Password itu muncul di tangkapan layar yang",
                    "dibagikan di grup chat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ganti password user app sekarang dan pasang di kelima",
                    "     layanan, supaya kebocorannya berhenti.",
                    "  2. Nyalakan engine database di Vault (atau OpenBao) dan buat",
                    "     satu peran per layanan, masing-masing dengan izin SQL",
                    "     sesempit mungkin.",
                    "  3. Ubah tiap layanan supaya meminta kredensial ke",
                    "     database/creds/<peran> saat menyala dan memperpanjang",
                    "     lease-nya selama berjalan.",
                    "  4. Setelah kelima layanan pindah, hapus user app.",
                    "  5. Nyalakan audit device dan kirim lognya ke penyimpanan",
                    "     log terpusat.",
                ],
            },
        ],
    },
    {
        "title": "23. Rahasia di Git dan Kubernetes: SOPS, Sealed Secrets, ESO",
        "sections": [
            {
                "body": [
                    "Tim yang memakai GitOps menyimpan seluruh keadaan sistem di",
                    "Git: kode, konfigurasi, dan manifest Kubernetes. Alat seperti",
                    "Argo CD atau Flux lalu menyamakan klaster dengan isi",
                    "repositori. Pertanyaannya, rahasia ditaruh di mana? Kalau",
                    "rahasia nggak di Git, GitOps-nya bolong. Kalau di Git dalam",
                    "bentuk polos, semua yang bisa membaca repositori bisa",
                    "membaca rahasianya.",
                    "",
                    "Banyak orang mengira objek Secret di Kubernetes sudah",
                    "terenkripsi. Isinya cuma di-encode base64, dan base64 itu",
                    "cara menulis ulang data, bukan cara menyembunyikannya:",
                ],
            },
            {
                "heading": "Membaca isi Secret Kubernetes",
                "code": """import base64

# Potongan Secret Kubernetes: nilai di bawah data: cuma di-encode base64.
data = {"password": "cmFoYXNpYTEyMw==", "user": "dG9rbw=="}
for kunci, nilai in data.items():
    print(kunci, "=", base64.b64decode(nilai).decode())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  password = rahasia123",
                    "  user = toko",
                    "",
                    "Satu baris b64decode sudah cukup. Kubernetes memang bisa",
                    "mengenkripsi Secret saat disimpan di etcd, tapi itu harus",
                    "dinyalakan admin klaster, dan nggak menolong apa pun kalau",
                    "manifest-nya di-commit ke Git. Tiga alat di bawah ini",
                    "menjawab masalah itu dengan cara berbeda.",
                ],
            },
            {
                "heading": "SOPS: enkripsi nilai, kunci tetap terbaca",
                "body": [
                    "SOPS mengenkripsi nilai di dalam berkas YAML, JSON, ENV, atau",
                    "INI, tapi membiarkan nama kuncinya terbaca. Hasilnya tetap",
                    "bisa di-diff dan di-review: kamu bisa melihat bahwa",
                    "db_password berubah tanpa tahu isinya. Alat ini juga",
                    "menyimpan MAC (kode pengecek keutuhan) atas seluruh isi, jadi",
                    "perubahan yang dibuat dengan tangan langsung ketahuan.",
                    "",
                    "Kunci enkripsinya bisa dari age, PGP, AWS KMS, Google Cloud",
                    "KMS, Azure Key Vault, atau Vault transit. Aturan kunci mana",
                    "untuk berkas mana ditulis di .sops.yaml. Saat materi ini",
                    "ditulis, rilis terbarunya v3.13.3 (23 Juli 2026), berlisensi",
                    "MPL-2.0, dan dikelola di bawah CNCF. Flux bisa mendekripsi",
                    "berkas seperti ini langsung saat menerapkannya ke klaster.",
                ],
            },
            {
                "heading": "Isi berkas sesudah dienkripsi SOPS (dipotong)",
                "bahasa": "yaml",
                "code": """db_user: ENC[AES256_GCM,data:dG9r...,iv:...,tag:...,type:str]
db_password: ENC[AES256_GCM,data:k3Jx...,iv:...,tag:...,type:str]
sops:
    age:
        - recipient: age1...
    lastmodified: "2026-10-19T08:00:00Z"
    mac: ENC[AES256_GCM,data:...,type:str]""",
            },
            {
                "heading": "Perintah SOPS dengan age",
                "bahasa": "terminal",
                "code": """age-keygen -o kunci.txt                     # simpan di luar repositori
sops --encrypt --age age1contohpenerima rahasia.yaml > rahasia.enc.yaml
sops rahasia.enc.yaml                        # buka di editor, simpan terenkripsi lagi
sops --decrypt rahasia.enc.yaml""",
            },
            {
                "heading": "Sealed Secrets dan External Secrets Operator",
                "body": [
                    "Sealed Secrets memakai kunci publik. Di klaster berjalan",
                    "sebuah controller yang menyimpan kunci privat. Developer",
                    "memakai perintah kubeseal untuk mengenkripsi Secret biasa",
                    "dengan kunci publik klaster, hasilnya objek SealedSecret yang",
                    "aman di-commit. Hanya controller di klaster itu yang bisa",
                    "membukanya kembali jadi Secret. Konsekuensinya, kunci privat",
                    "controller wajib dicadangkan; kalau klaster dibangun ulang",
                    "tanpa kunci itu, semua SealedSecret lama nggak bisa dibuka.",
                    "Proyeknya milik bitnami-labs, berlisensi Apache-2.0, rilis",
                    "terbarunya v0.40.0 (10 September 2026). Sejak daftar image",
                    "Bitnami berubah pada Agustus 2025, cek dari mana image",
                    "controller-mu diambil.",
                    "",
                    "External Secrets Operator (ESO) mengambil pendekatan lain:",
                    "rahasianya sama sekali nggak masuk Git. Yang di-commit cuma",
                    "petunjuk, misalnya \"ambil rahasia toko/db dari AWS Secrets",
                    "Manager\". Operator di klaster lalu mengambil nilainya dan",
                    "membuat Secret Kubernetes, serta menyegarkannya berkala.",
                    "Sumbernya bisa Vault, OpenBao, AWS Secrets Manager, Google",
                    "Secret Manager, Azure Key Vault, dan banyak lagi. Operator",
                    "ini proyek CNCF berlisensi Apache-2.0. Rilis terbaru yang",
                    "tercatat saat materi ini ditulis berlabel chart Helm 2.13.0",
                    "(16 Oktober 2026).",
                ],
            },
            {
                "heading": "Manifest ExternalSecret",
                "bahasa": "yaml",
                "code": """apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: toko-db
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets
    kind: ClusterSecretStore
  target:
    name: toko-db          # nama Secret Kubernetes yang dibuat
  data:
    - secretKey: password
      remoteRef:
        key: toko/db
        property: password""",
            },
            {
                "body": [
                    "Cara memilih di antara ketiganya:",
                    "",
                    "  - SOPS cocok kalau rahasianya memang mau disimpan dan",
                    "    di-review di Git, dan tim sudah punya KMS atau mau",
                    "    mengelola kunci age. Bisa dipakai di luar Kubernetes juga.",
                    "  - Sealed Secrets cocok untuk tim kecil dengan satu atau dua",
                    "    klaster yang nggak punya brankas rahasia pusat.",
                    "  - ESO cocok kalau sumber kebenarannya sudah ada di brankas",
                    "    pusat (Vault, layanan cloud) dan rotasi dikerjakan di",
                    "    sana.",
                    "",
                    "Jebakan: ketiga alat ini akhirnya membuat Secret Kubernetes",
                    "biasa di dalam klaster. Siapa pun yang punya izin get secrets",
                    "di namespace itu tetap bisa membacanya. Batasi izin RBAC",
                    "klaster, dan nyalakan enkripsi etcd.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dokumentasi Flux punya panduan resmi memakai SOPS, sementara",
                    "pengguna Argo CD lebih sering memilih Sealed Secrets atau ESO,",
                    "karena Argo CD sendiri nggak memilih satu cara mengelola",
                    "rahasia.",
                    "",
                    "Kasus kecil: timmu punya tiga klaster (dev, staging,",
                    "produksi) yang dikelola Argo CD, dan semua rahasia produksi",
                    "sudah tersimpan di Vault. Sekarang password database masih",
                    "di-commit sebagai Secret biasa dalam bentuk base64.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Anggap password yang pernah di-commit sudah bocor. Ganti",
                    "     di database dan simpan nilai barunya di Vault.",
                    "  2. Pasang External Secrets Operator di tiap klaster dengan",
                    "     satu ClusterSecretStore yang masuk ke Vault lewat auth",
                    "     method Kubernetes.",
                    "  3. Ganti manifest Secret di Git dengan ExternalSecret yang",
                    "     menunjuk path di Vault.",
                    "  4. Hapus manifest Secret lama dari repositori, dan batasi",
                    "     izin get secrets di namespace produksi.",
                ],
            },
        ],
    },
    {
        "title": "24. Rantai Pasok Perangkat Lunak: Lockfile dan Dependensi",
        "sections": [
            {
                "body": [
                    "Aplikasi web biasa mungkin cuma berisi beberapa ribu baris",
                    "kode tulisanmu sendiri, tapi menarik ratusan paket dari npm",
                    "atau PyPI. Paket yang kamu tulis di requirements.txt disebut",
                    "dependensi langsung. Paket yang dibutuhkan paket itu disebut",
                    "dependensi transitif, dan jumlahnya biasanya jauh lebih",
                    "banyak. Semua kode itu ikut berjalan dengan hak akses yang",
                    "sama dengan kodemu.",
                    "",
                    "Rantai pasok perangkat lunak adalah semua yang ikut membentuk",
                    "aplikasimu: paket, alat build, server CI, image dasar",
                    "container, sampai akun developer yang bisa menerbitkan paket.",
                    "Top 10:2025 memberinya kategori sendiri di nomor 3, Software",
                    "Supply Chain Failures. Kategori A08, Software or Data",
                    "Integrity Failures, menyusul untuk hal-hal yang dipakai tanpa",
                    "dicek keasliannya: pembaruan tanpa tanda tangan, plugin dari",
                    "sumber sembarang, dan pipeline yang bisa diubah siapa saja.",
                ],
            },
            {
                "heading": "Kasus yang membentuk cara kerja hari ini",
                "body": [
                    "  - Log4Shell (CVE-2021-44228, Desember 2021). Celah di pustaka",
                    "    logging Java bernama Log4j. Banyak tim butuh berhari-hari",
                    "    cuma untuk tahu aplikasi mana yang memakainya, sering",
                    "    sebagai dependensi transitif.",
                    "  - Backdoor xz-utils (CVE-2024-3094, Maret 2024). Seseorang",
                    "    membangun kepercayaan sebagai kontributor selama sekitar",
                    "    dua tahun, lalu menyisipkan kode tersembunyi di versi 5.6.0",
                    "    dan 5.6.1 pustaka kompresi xz. Kode itu ketahuan sebelum",
                    "    masuk rilis stabil kebanyakan distro, setelah developer",
                    "    Andres Freund menyelidiki login SSH yang terasa setengah",
                    "    detik lebih lambat.",
                    "  - Typosquatting: paket jahat dengan nama mirip paket populer,",
                    "    misalnya selisih satu huruf, menunggu orang salah ketik.",
                    "  - Dependency confusion: paket publik diberi nama yang sama",
                    "    dengan paket internal perusahaan, lalu terpasang karena",
                    "    pengelola paket memilih versi tertinggi dari sumber mana",
                    "    pun.",
                    "",
                    "Pelajarannya: tahu apa saja yang terpasang, kunci versinya,",
                    "pastikan yang diunduh sama dengan yang diharapkan, dan pantau",
                    "celah baru.",
                ],
            },
            {
                "heading": "Lockfile: versi dan hash yang dikunci",
                "body": [
                    "Rentang versi di package.json, misalnya ^4.18.0, artinya",
                    "\"versi berapa pun dari 4.18.0 sampai sebelum 5.0.0\". Tanpa",
                    "kunci, build hari ini dan build bulan depan bisa memasang",
                    "versi berbeda tanpa ada yang mengubah satu baris pun.",
                    "",
                    "Lockfile mencatat versi persis setiap paket, termasuk yang",
                    "transitif, ditambah hash isinya. Namanya beda per ekosistem:",
                    "",
                    "  Ekosistem   Lockfile                     Pasang persis",
                    "  npm         package-lock.json            npm ci",
                    "  pnpm        pnpm-lock.yaml               pnpm install --frozen-lockfile",
                    "  Python      uv.lock, poetry.lock         uv sync --locked",
                    "  Rust        Cargo.lock                   cargo build --locked",
                    "  Go          go.sum                       go mod verify",
                    "  PHP         composer.lock                composer install",
                    "",
                    "Lockfile wajib di-commit untuk aplikasi. Di CI, pakai",
                    "perintah di kolom kanan: npm ci gagal kalau lockfile nggak",
                    "cocok dengan package.json, sedangkan npm install akan",
                    "memperbarui lockfile tanpa bertanya. Untuk pip, bentuk paling ketatnya",
                    "requirements.txt dengan hash dan opsi --require-hashes.",
                ],
            },
            {
                "heading": "Kenapa hash di lockfile penting",
                "code": "import hashlib\n\n# Isi berkas paket yang diunduh (di sini cuma teks pendek sebagai tiruan).\npaket_asli = b\"def format_rupiah(n): return f'Rp{n:,}'\\n\"\npaket_disusupi = paket_asli + b\"# baris tambahan dari penyusup\\n\"\n\n# Hash yang tercatat di lockfile waktu dependensi pertama kali ditambahkan.\nlock = {\"format-rupiah==1.2.0\": hashlib.sha256(paket_asli).hexdigest()}\nprint(\"di lockfile:\", lock[\"format-rupiah==1.2.0\"][:16], \"...\")\n\nfor nama, isi in [(\"unduhan pertama\", paket_asli), (\"unduhan kedua\", paket_disusupi)]:\n    hasil = hashlib.sha256(isi).hexdigest()\n    cocok = hasil == lock[\"format-rupiah==1.2.0\"]\n    print(f\"{nama}: {hasil[:16]} ... {'pasang' if cocok else 'TOLAK, hash beda'}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  di lockfile: 57f7bfc77022b21f ...",
                    "  unduhan pertama: 57f7bfc77022b21f ... pasang",
                    "  unduhan kedua: 2c052dc251f78516 ... TOLAK, hash beda",
                    "",
                    "Nama dan versinya sama, tapi isinya berubah satu baris, jadi",
                    "hash-nya berbeda total. Pengelola paket yang membaca hash dari",
                    "lockfile menolak memasang. Ini yang menahan paket yang diganti",
                    "di tengah jalan atau di server cermin (mirror).",
                    "",
                    "Hash nggak menolong kalau versi jahat itu yang pertama kali",
                    "masuk lockfile, seperti kasus xz-utils. Untuk itu kamu butuh",
                    "pemantauan celah dan kebiasaan meninjau pembaruan.",
                ],
            },
            {
                "heading": "Memantau dan memperbarui",
                "body": [
                    "  - Basis data celah: GitHub Advisory Database dan OSV (osv.dev)",
                    "    mengumpulkan celah per paket dan rentang versinya.",
                    "  - Pemeriksa lokal: npm audit, pip-audit, cargo audit, dan",
                    "    govulncheck membandingkan lockfile dengan basis data itu.",
                    "  - Dependabot (bawaan GitHub) dan Renovate (dari Mend, bisa",
                    "    dipasang sendiri) membuka pull request otomatis untuk",
                    "    pembaruan, lengkap dengan catatan rilisnya. Tugasmu",
                    "    meninjau dan menggabungkannya, bukan menumpuknya.",
                    "  - Kurangi dependensi. Paket yang nggak ada nggak bisa",
                    "    disusupi. Aplikasi belajar-codingV2 yang sedang kamu pakai",
                    "    ini sengaja cuma memakai pustaka standar Python, dan itu",
                    "    keputusan rantai pasok.",
                    "",
                    "Untuk menilai kematangan proses build, OpenSSF punya kerangka",
                    "SLSA (Supply-chain Levels for Software Artifacts), saat ini",
                    "versi 1.2. Jalur build-nya punya empat tingkat:",
                    "",
                    "  - L0: belum ada jaminan apa pun.",
                    "  - L1: ada catatan asal-usul build (provenance).",
                    "  - L2: provenance-nya ditandatangani platform build.",
                    "  - L3: platform build-nya diperkeras, sehingga satu build",
                    "    nggak bisa mencemari build lain.",
                    "",
                    "Ingat: memperbarui dependensi bukan pekerjaan sekali setahun.",
                    "Pembaruan kecil yang rutin jauh lebih gampang ditinjau",
                    "daripada lompatan tiga versi mayor saat ada celah darurat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Repositori di GitHub yang menyalakan Dependabot menerima pull",
                    "request seperti \"Bump urllib3 from 2.2.1 to 2.2.2\" lengkap",
                    "dengan tautan ke advisori yang ditutupnya. Sebagian besar",
                    "celah yang ditemukan pemeriksa ada di dependensi transitif,",
                    "bukan di paket yang kamu tulis sendiri.",
                    "",
                    "Kasus kecil: npm audit melaporkan celah tingkat tinggi di",
                    "paket bernama semver versi lama. Masalahnya, kamu nggak pernah",
                    "memasang semver; ia dibawa paket lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari siapa yang membawanya:",
                    "      npm ls semver",
                    "  2. Perbarui paket induknya ke versi yang sudah memakai semver",
                    "     baru. Ini cara paling bersih.",
                    "  3. Kalau induknya belum diperbarui, paksa versi transitif",
                    "     lewat bagian overrides di package.json, lalu jalankan",
                    "     tes untuk memastikan nggak ada yang rusak.",
                    "  4. Jalankan npm ci di CI supaya lockfile baru itu yang",
                    "     dipakai, dan commit perubahan lockfile-nya.",
                    "  5. Catat keputusannya di pull request, termasuk kalau celah",
                    "     itu dinilai nggak terjangkau dari kodemu.",
                ],
            },
        ],
    },
    {
        "title": "25. SBOM dan Tanda Tangan Artefak: Syft dan Sigstore",
        "sections": [
            {
                "body": [
                    "Waktu Log4Shell diumumkan, pertanyaan pertama di banyak",
                    "perusahaan adalah \"kita kena atau nggak?\". Tim yang nggak",
                    "punya daftar komponen harus membongkar ratusan image satu per",
                    "satu. Tim yang punya daftar cukup mencari satu nama.",
                    "",
                    "Daftar itu namanya SBOM (Software Bill of Materials), daftar",
                    "bahan perangkat lunak. Isinya semua komponen di dalam sebuah",
                    "artefak: nama, versi, sumber, lisensi, dan hubungan antar",
                    "komponennya. Ada dua format standar:",
                    "",
                    "  - SPDX, dari Linux Foundation, sudah jadi standar",
                    "    internasional ISO/IEC 5962:2021.",
                    "  - CycloneDX, dari komunitas OWASP, juga distandarkan sebagai",
                    "    ECMA-424.",
                    "",
                    "Regulasi ikut mendorong. Perintah Eksekutif 14028 di Amerika",
                    "Serikat (2021) meminta SBOM untuk perangkat lunak yang dibeli",
                    "pemerintahnya. Cyber Resilience Act di Uni Eropa mewajibkan",
                    "produsen produk digital mendokumentasikan komponennya;",
                    "kewajibannya berlaku bertahap, pelaporan mulai September 2026",
                    "dan sebagian besar kewajiban lain Desember 2027.",
                ],
            },
            {
                "heading": "SBOM CycloneDX mini dari requirements",
                "code": "import json\n\nrequirements = \"\"\"\nflask==3.1.2\nrequests==2.32.5\n\"\"\"\n\nkomponen = []\nfor baris in requirements.split():\n    nama, versi = baris.split(\"==\")\n    komponen.append({\n        \"type\": \"library\",\n        \"name\": nama,\n        \"version\": versi,\n        \"purl\": f\"pkg:pypi/{nama}@{versi}\",\n    })\n\nsbom = {\n    \"bomFormat\": \"CycloneDX\",\n    \"specVersion\": \"1.6\",\n    \"metadata\": {\"component\": {\"type\": \"application\", \"name\": \"toko-web\"}},\n    \"components\": komponen,\n}\nprint(json.dumps(sbom, indent=2))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  {",
                    "    \"bomFormat\": \"CycloneDX\",",
                    "    \"specVersion\": \"1.6\",",
                    "    \"metadata\": {",
                    "      \"component\": {",
                    "        \"type\": \"application\",",
                    "        \"name\": \"toko-web\"",
                    "      }",
                    "    },",
                    "    \"components\": [",
                    "      {",
                    "        \"type\": \"library\",",
                    "        \"name\": \"flask\",",
                    "        \"version\": \"3.1.2\",",
                    "        \"purl\": \"pkg:pypi/flask@3.1.2\"",
                    "      },",
                    "",
                    "Keluarannya dipotong; komponen requests menyusul dengan bentuk",
                    "yang sama. Field purl (package URL) adalah alamat baku sebuah",
                    "paket: ekosistem, nama, dan versi dalam satu teks. Pemindai",
                    "celah memakai purl untuk mencocokkan komponen dengan basis",
                    "data celah.",
                    "",
                    "SBOM sungguhan juga memuat dependensi transitif, hash, dan",
                    "lisensi, dan nggak ditulis tangan. Alatnya membaca lockfile,",
                    "isi image, atau berkas biner lalu menyusunnya otomatis.",
                ],
            },
            {
                "heading": "Membuat SBOM dengan Syft",
                "bahasa": "terminal",
                "code": """# Dari folder proyek sendiri
syft dir:. -o cyclonedx-json > sbom.cdx.json

# Dari image container
syft ghcr.io/contoh/toko-web:1.5.0 -o spdx-json > sbom.spdx.json

# Cari celah dari SBOM tanpa memindai ulang image
grype sbom:sbom.cdx.json""",
            },
            {
                "body": [
                    "Syft dibuat Anchore, ditulis dengan Go, berlisensi Apache-2.0.",
                    "Saat materi ini ditulis, rilis terbarunya v1.54.1 (6 Oktober",
                    "2026). Ia membaca puluhan jenis lockfile dan paket sistem",
                    "operasi di dalam image. Pasangannya Grype, pemindai celah dari",
                    "pembuat yang sama. Trivy, yang dibahas di bab 07, juga bisa",
                    "membuat SBOM.",
                    "",
                    "SBOM baru berguna kalau disimpan bersama artefaknya dan bisa",
                    "dicari. Kebiasaan yang baik: buat SBOM di pipeline setiap",
                    "kali image dibangun, lalu simpan di registry yang sama dengan",
                    "image-nya.",
                ],
            },
            {
                "heading": "Tanda tangan: membuktikan artefak dari pipeline sendiri",
                "body": [
                    "SBOM menjawab \"isinya apa\". Pertanyaan berikutnya: image",
                    "yang mau di-deploy ini benar dibangun pipeline kita, atau",
                    "sudah diganti orang di registry? Yang bisa membuktikannya",
                    "tanda tangan digital, yang konsepnya ada di materi Enkripsi",
                    "Simetris, Asimetris, dan Tanda Tangan Digital.",
                    "",
                    "Masalah klasiknya ada di kunci. Kunci privat penanda tangan",
                    "harus disimpan bertahun-tahun, dirotasi, dan dijaga supaya",
                    "nggak bocor. Sigstore, proyek OpenSSF, menawarkan keyless",
                    "signing:",
                    "",
                    "  1. Pipeline atau developer login lewat OIDC, misalnya",
                    "     identitas workflow GitHub Actions.",
                    "  2. Fulcio, otoritas sertifikat milik Sigstore, menerbitkan",
                    "     sertifikat berumur beberapa menit untuk identitas itu.",
                    "  3. cosign menandatangani artefak dengan kunci sementara.",
                    "  4. Tanda tangannya dicatat di Rekor, log transparansi yang",
                    "     cuma bisa ditambah dan bisa diperiksa siapa pun.",
                    "",
                    "Saat verifikasi, yang dicek adalah identitasnya: \"artefak ini",
                    "ditandatangani workflow release.yml di repositori",
                    "contoh/toko-web\". Nggak ada kunci jangka panjang yang bisa",
                    "dicuri. cosign berlisensi Apache-2.0; rilis terbarunya saat",
                    "materi ini ditulis v3.1.3 (6 Agustus 2026), yang menutup celah",
                    "verifikasi pada format bundle lama. npm dan PyPI memakai",
                    "Sigstore untuk provenance paket.",
                ],
            },
            {
                "heading": "Menandatangani dan memverifikasi image",
                "bahasa": "terminal",
                "code": "# Di pipeline (identitas OIDC dari CI)\ncosign sign ghcr.io/contoh/toko-web@sha256:4f1c...\n\n# Saat deploy: tolak kalau penanda tangannya bukan workflow rilis kita\ncosign verify ghcr.io/contoh/toko-web@sha256:4f1c... \\\n  --certificate-identity-regexp '^https://github.com/contoh/toko-web/' \\\n  --certificate-oidc-issuer https://token.actions.githubusercontent.com",
            },
            {
                "heading": "Log transparansi mini berantai hash",
                "code": """import hashlib

log = []  # log transparansi mini: tiap catatan memuat hash catatan sebelumnya


def tambah(isi):
    sebelum = log[-1]["hash"] if log else "0" * 64
    h = hashlib.sha256((sebelum + isi).encode()).hexdigest()
    log.append({"isi": isi, "sebelum": sebelum, "hash": h})


def periksa():
    sebelum = "0" * 64
    for i, c in enumerate(log):
        h = hashlib.sha256((sebelum + c["isi"]).encode()).hexdigest()
        if c["sebelum"] != sebelum or c["hash"] != h:
            return f"rusak di catatan {i}"
        sebelum = c["hash"]
    return "utuh"


tambah("ci@toko menandatangani toko-web:1.4.0")
tambah("ci@toko menandatangani toko-web:1.4.1")
tambah("ci@toko menandatangani toko-web:1.5.0")
print(periksa())
log[1]["isi"] = "penyusup menandatangani toko-web:1.4.1"
print(periksa())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  utuh",
                    "  rusak di catatan 1",
                    "",
                    "Tiap catatan menyimpan hash catatan sebelumnya. Mengubah satu",
                    "catatan lama membuat rantai hash sesudahnya nggak cocok lagi.",
                    "Rekor memakai struktur yang lebih canggih (pohon Merkle),",
                    "tapi idenya sama: catatan lama nggak bisa diubah tanpa ketahuan.",
                    "",
                    "Jebakan: tanda tangan tanpa verifikasi saat deploy nggak",
                    "melindungi apa pun. Pasang pemeriksanya di tempat image",
                    "diterima, misalnya admission controller Kubernetes seperti",
                    "Kyverno atau policy-controller Sigstore, dan tolak image yang",
                    "nggak lolos. Rujuk image dengan digest sha256, bukan tag",
                    "seperti :latest yang bisa dipindah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek Kubernetes menandatangani artefak rilisnya dengan",
                    "Sigstore, dan halaman dokumentasinya menunjukkan cara",
                    "memverifikasinya dengan cosign. Banyak registry container,",
                    "termasuk GitHub Container Registry, bisa menyimpan tanda",
                    "tangan dan SBOM di samping image.",
                    "",
                    "Kasus kecil: ada pengumuman celah kritis di sebuah pustaka",
                    "kompresi, dan atasan bertanya dalam satu jam: dari 40 image",
                    "produksi, mana yang memakainya?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kalau SBOM sudah dibuat di pipeline, kumpulkan SBOM untuk",
                    "     40 digest yang sedang berjalan.",
                    "  2. Cari nama paket dan rentang versi rentan di semua SBOM",
                    "     itu, misalnya dengan grype sbom:<berkas> atau pencarian",
                    "     purl biasa.",
                    "  3. Bangun ulang image yang terdampak dengan versi perbaikan,",
                    "     tandatangani dengan cosign, dan buat SBOM barunya.",
                    "  4. Kalau ternyata belum ada SBOM, jalankan syft ke 40 image",
                    "     itu sekarang, lalu pasang langkah SBOM dan tanda tangan",
                    "     di pipeline supaya lain kali jawabannya keluar dalam",
                    "     hitungan menit.",
                ],
            },
        ],
    },
    {
        "title": "26. DevSecOps: SAST, SCA, DAST, dan Gerbang Kualitas",
        "sections": [
            {
                "body": [
                    "Di bab-bab sebelumnya kamu sudah tahu bentuk celah yang sering",
                    "muncul: injeksi, rahasia yang ikut ter-commit, dependensi yang",
                    "rentan. Masalahnya, manusia gampang lupa ngecek. Reviewer yang",
                    "capek di jam lima sore bisa melewatkan satu baris `eval()`.",
                    "",
                    "DevSecOps adalah kebiasaan memasang pemeriksaan keamanan di",
                    "dalam pipeline CI/CD, jadi setiap commit diperiksa mesin dengan",
                    "cara yang sama. Istilah yang sering menempel padanya adalah",
                    "shift left, artinya memindahkan pemeriksaan ke kiri garis waktu,",
                    "ke tahap yang lebih awal. Celah yang ketahuan waktu pull request",
                    "cukup diperbaiki pembuatnya sendiri. Celah yang ketahuan di",
                    "produksi butuh rapat, hotfix, dan kadang laporan insiden.",
                    "",
                    "Pipeline-nya sendiri sudah dibahas di kurikulum DevOps. Kalau",
                    "belum pernah menulis workflow, baca dulu materi \"GitHub Actions:",
                    "Secrets, OIDC, dan Keamanan Workflow\" di sana.",
                ],
            },
            {
                "heading": "Lima jenis pemeriksaan",
                "body": [
                    "Tiap jenis pemeriksaan melihat benda yang berbeda, jadi mereka",
                    "saling melengkapi. Satu alat nggak bisa menggantikan semuanya.",
                    "",
                    "  jenis         yang diperiksa              contoh alat",
                    "  secret scan   teks rahasia di kode/riwayat Gitleaks, TruffleHog",
                    "  SAST          kode sumber, tanpa dijalankan SonarQube, CodeQL",
                    "  SCA           dependensi pihak ketiga      Trivy, Snyk",
                    "  IaC scan      berkas infrastruktur         Checkov, KICS",
                    "  DAST          aplikasi yang sedang jalan   ZAP, Burp Suite",
                    "",
                    "SAST (static application security testing) membaca kode tanpa",
                    "menjalankannya. Ia pintar menemukan pola seperti masukan pengguna",
                    "yang mengalir ke query SQL. Semgrep juga sering dipakai di sini",
                    "karena aturannya gampang ditulis sendiri.",
                    "",
                    "SCA (software composition analysis) mencocokkan daftar",
                    "dependensimu dengan basis data celah yang sudah diketahui (CVE).",
                    "Kode buatanmu bisa bersih, tapi pustaka yang kamu pakai mungkin",
                    "punya celah.",
                    "",
                    "DAST (dynamic application security testing) menembak aplikasi",
                    "yang sudah berjalan dari luar, persis seperti pengguna. Ia bisa",
                    "menemukan header keamanan yang hilang atau halaman error yang",
                    "membocorkan informasi, hal yang nggak kelihatan dari kode saja.",
                    "",
                    "Pemindaian image container biasanya digabung dengan SCA, karena",
                    "isinya juga paket: paket sistem operasi di image dasar ditambah",
                    "pustaka aplikasimu.",
                ],
            },
            {
                "heading": "Urutannya di pipeline",
                "body": [
                    "Pemeriksaan yang cepat ditaruh paling awal supaya umpan baliknya",
                    "datang dalam hitungan detik. Yang lambat dan butuh aplikasi",
                    "berjalan ditaruh belakangan.",
                    "",
                    "  1. Secret scan, bahkan sebelum push lewat pre-commit hook.",
                    "  2. SAST dan SCA di setiap pull request.",
                    "  3. IaC scan di pull request yang menyentuh berkas Terraform",
                    "     atau manifest Kubernetes.",
                    "  4. Scan image sesudah image dibangun, sebelum di-push ke",
                    "     registry.",
                    "  5. DAST terhadap lingkungan staging sesudah deploy ke sana.",
                    "",
                    "Secret scan ditaruh paling depan karena rahasia yang sudah",
                    "ter-push harus dianggap bocor. Menghapus barisnya di commit",
                    "berikutnya nggak menolong, karena riwayat Git masih menyimpannya.",
                    "Kuncinya tetap harus dicabut dan diganti.",
                ],
            },
            {
                "heading": "Contoh workflow",
                "bahasa": "yaml",
                "code": """name: keamanan
on: [pull_request]
permissions:
  contents: read
jobs:
  periksa:
    runs-on: ubuntu-latest
    steps:
      # Di proyek sungguhan, pin action ke SHA commit, bukan tag.
      - uses: actions/checkout@v5
        with:
          fetch-depth: 0
      - name: Cari rahasia di seluruh riwayat
        run: gitleaks git --redact .
      - name: Dependensi dan konfigurasi
        run: trivy fs --scanners vuln,misconfig --exit-code 1 --severity HIGH,CRITICAL .
      - name: Analisis statis
        run: semgrep scan --error""",
            },
            {
                "body": [
                    "Contoh di atas mengandaikan ketiga alat sudah terpasang di",
                    "runner. Yang penting dilihat adalah polanya. Tiap langkah keluar",
                    "dengan kode bukan nol kalau ada temuan, dan kode keluar itulah",
                    "yang membuat job gagal. `permissions: contents: read` membatasi",
                    "token workflow supaya langkah pemindai nggak bisa menulis ke",
                    "repo.",
                    "",
                    "Soal pin ke SHA commit: action pihak ketiga pernah dibajak.",
                    "Pada Maret 2025, tag-tag `tj-actions/changed-files` diarahkan ke",
                    "commit jahat yang mencetak rahasia CI ke log. Repo yang memakai",
                    "SHA commit lama nggak ikut kena.",
                ],
            },
            {
                "heading": "Gerbang kualitas",
                "body": [
                    "Gerbang kualitas (quality gate) adalah aturan yang memutuskan",
                    "pipeline boleh lanjut atau berhenti. Kalau setiap temuan",
                    "memblokir, tim akan frustrasi lalu mematikan pemindainya. Kalau",
                    "nggak ada yang memblokir, laporan pemindai cuma jadi arsip.",
                    "",
                    "Pola yang banyak dipakai:",
                    "  - Blokir hanya temuan baru di kode yang diubah. Utang lama",
                    "    dicatat dan dicicil, jangan dijadikan alasan menahan semua",
                    "    pull request.",
                    "  - Blokir hanya tingkat tertentu, misalnya kritis dan tinggi.",
                    "  - Sediakan pengecualian yang tertulis: siapa yang menyetujui,",
                    "    alasannya, dan tanggal kedaluwarsanya.",
                    "",
                    "Program di bawah meniru keputusan gerbang seperti itu.",
                ],
            },
            {
                "heading": "Gerbang mini",
                "code": """# Gerbang keamanan mini: temuan dari beberapa pemeriksa digabung,
# lalu diputuskan apakah pipeline boleh lanjut.
temuan = [
    {"alat": "secret", "tingkat": "KRITIS", "baru": True, "id": "kunci-aws"},
    {"alat": "sast", "tingkat": "TINGGI", "baru": False, "id": "sql-injeksi"},
    {"alat": "sca", "tingkat": "SEDANG", "baru": True, "id": "lodash-lama"},
    {"alat": "sca", "tingkat": "TINGGI", "baru": True, "id": "openssl-cve"},
]
pengecualian = {"openssl-cve"}   # sudah disetujui tim, ada tanggal kedaluwarsa
MEMBLOKIR = {"KRITIS", "TINGGI"}

blokir = []
for t in temuan:
    if not t["baru"]:
        status = "utang lama, dicatat"
    elif t["id"] in pengecualian:
        status = "dikecualikan"
    elif t["tingkat"] in MEMBLOKIR:
        status = "MEMBLOKIR"
        blokir.append(t["id"])
    else:
        status = "peringatan"
    print(f"{t['alat']:7}{t['tingkat']:8}{t['id']:13}{status}")

print("Gerbang:", "GAGAL" if blokir else "LULUS", blokir)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  secret KRITIS  kunci-aws    MEMBLOKIR",
                    "  sast   TINGGI  sql-injeksi  utang lama, dicatat",
                    "  sca    SEDANG  lodash-lama  peringatan",
                    "  sca    TINGGI  openssl-cve  dikecualikan",
                    "  Gerbang: GAGAL ['kunci-aws']",
                    "",
                    "Perhatikan `sql-injeksi`. Tingkatnya tinggi, tapi ia temuan",
                    "lama, jadi nggak menahan pull request ini. Temuan itu tetap",
                    "harus masuk antrean perbaikan, kalau nggak ia akan tinggal di",
                    "sana selamanya.",
                    "",
                    "Jebakan: menjalankan pemindai dengan `|| true` supaya pipeline",
                    "\"nggak rewel\". Pemindainya tetap jalan dan menghabiskan menit",
                    "CI, tapi hasilnya nggak pernah memengaruhi apa pun.",
                    "",
                    "Ingat: pemindai otomatis cuma menangkap pola yang sudah",
                    "dikenal. Celah logika bisnis, misalnya kupon yang bisa dipakai",
                    "berulang kali, tetap butuh review manusia dan threat modeling.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Platform Git besar sudah membawa sebagian pemeriksaan ini.",
                    "GitHub punya secret scanning, Dependabot, dan code scanning",
                    "dengan CodeQL. GitLab punya template SAST, secret detection, dan",
                    "dependency scanning yang bisa dinyalakan lewat `.gitlab-ci.yml`.",
                    "Panduan DevSecOps dari OWASP memetakan jenis pemeriksaan ini ke",
                    "tahap-tahap pipeline.",
                    "",
                    "Kasus kecil: tim tiga orang baru menyalakan Trivy dan Semgrep.",
                    "Hari pertama ada 214 temuan, dan semua pull request merah.",
                    "Seminggu kemudian seseorang menambah `|| true` ke kedua langkah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hapus `|| true`. Jalankan pemindai dalam mode laporan saja",
                    "     di cabang utama untuk mencatat garis dasar (baseline).",
                    "  2. Atur gerbang supaya hanya temuan baru bertingkat kritis",
                    "     dan tinggi yang memblokir pull request.",
                    "  3. Bagi 214 temuan lama per tingkat. Masukkan yang kritis ke",
                    "     sprint ini, sisanya dicicil beberapa per sprint.",
                    "  4. Untuk positif palsu, tulis pengecualian di berkas konfigurasi",
                    "     alat dengan alasan dan tanggal kedaluwarsa, jangan dimatikan",
                    "     lewat pipeline.",
                ],
            },
        ],
    },
    {
        "title": "27. Analisis Kode Statis: SonarQube dan CodeQL",
        "sections": [
            {
                "body": [
                    "Analisis kode statis artinya membaca kode tanpa menjalankannya,",
                    "lalu mencari pola yang berbahaya atau jelek. Linter seperti",
                    "flake8 dan ESLint sudah melakukan versi kecilnya. Alat SAST",
                    "melangkah lebih jauh: ia bisa melacak data dari satu fungsi ke",
                    "fungsi lain.",
                    "",
                    "Materi ini membahas dua alat yang paling sering kamu temui.",
                    "SonarQube dipakai banyak perusahaan sebagai gerbang kualitas di",
                    "CI. CodeQL adalah mesin di balik code scanning GitHub. Di Survei",
                    "Stack Overflow 2026, SonarQube/SonarCloud dipakai 19% responden",
                    "untuk pengujian kode, sedangkan CodeQL 5%.",
                ],
            },
            {
                "heading": "Cara alat SAST berpikir",
                "body": [
                    "Langkah pertamanya selalu sama: kode diurai jadi pohon sintaks",
                    "abstrak (abstract syntax tree). Di pohon itu, `eval(teks)` sudah",
                    "berubah jadi simpul \"panggilan fungsi bernama eval dengan satu",
                    "argumen\". Komentar dan string yang kebetulan berisi kata eval",
                    "nggak ikut tertangkap, beda dengan grep.",
                    "",
                    "Python punya modul `ast` di pustaka standar, jadi kamu bisa",
                    "mencoba cara kerjanya sendiri. Program di bawah mencari",
                    "`pickle.loads`, fungsi yang bisa menjalankan kode sembarang kalau",
                    "datanya berasal dari luar.",
                ],
            },
            {
                "heading": "Aturan SAST mini",
                "code": """import ast

kode = '''
import pickle, json

def muat_sesi(data):
    return pickle.loads(data)

def muat_profil(teks):
    return json.loads(teks)
'''

for node in ast.walk(ast.parse(kode)):
    if (isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "pickle"
            and node.func.attr in ("load", "loads")):
        print(f"baris {node.lineno}: pickle.{node.func.attr} pada data luar"
              " bisa menjalankan kode")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  baris 5: pickle.loads pada data luar bisa menjalankan kode",
                    "",
                    "`json.loads` di baris 8 nggak dilaporkan, karena aturannya",
                    "spesifik ke objek `pickle`. Baris 5 karena string `kode` diawali",
                    "baris kosong.",
                    "",
                    "Alat sungguhan menambah satu hal penting: analisis aliran data",
                    "(taint analysis). Data dari luar disebut source, misalnya",
                    "parameter permintaan HTTP. Fungsi berbahaya disebut sink,",
                    "misalnya eksekusi query SQL. Alat melaporkan celah kalau ada",
                    "jalan dari source ke sink tanpa melewati pembersih (sanitizer).",
                    "Contoh di bawah butuh Flask, jadi cukup dibaca.",
                ],
            },
            {
                "heading": "Source sampai sink",
                "code": """import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.get("/cari")
def cari():
    nama = request.args["nama"]                 # source
    db = sqlite3.connect("toko.db")
    sql = "SELECT * FROM produk WHERE nama = '" + nama + "'"
    return str(db.execute(sql).fetchall())      # sink


# Perbaikannya: db.execute("... WHERE nama = ?", (nama,))""",
            },
            {
                "heading": "SonarQube",
                "body": [
                    "SonarQube dibuat SonarSource. Ia memeriksa bug, code smell",
                    "(kode yang jalan tapi susah dirawat), kerentanan, duplikasi, dan",
                    "cakupan tes. Ada beberapa bentuk produk:",
                    "  - SonarQube Community Build: gratis, berlisensi LGPL-3.0,",
                    "    dipasang sendiri. Versi terbarunya saat materi ini ditulis",
                    "    (Oktober 2026) adalah 26.10, dirilis 12 Oktober 2026. Nomor",
                    "    versinya berpola tahun.bulan karena rilisnya bulanan.",
                    "  - SonarQube Server: edisi berbayar untuk dipasang sendiri,",
                    "    dengan fitur seperti analisis cabang dan pull request.",
                    "  - SonarQube Cloud: layanan SaaS, dulu bernama SonarCloud.",
                    "  - SonarQube for IDE: plugin editor, dulu bernama SonarLint.",
                    "",
                    "SonarQube membedakan dua jenis temuan keamanan. Vulnerability",
                    "adalah celah yang hampir pasti harus diperbaiki. Security",
                    "hotspot adalah kode sensitif yang perlu ditinjau manusia,",
                    "misalnya pemakaian kriptografi atau cookie. Hotspot bisa saja",
                    "aman, tapi harus ada orang yang memutuskannya.",
                    "",
                    "Gerbang bawaannya bernama Sonar way. Dokumentasi resminya",
                    "menyebut empat syarat, semuanya untuk kode baru. Nggak ada issue",
                    "baru, semua security hotspot baru sudah ditinjau, cakupan tes",
                    "kode baru minimal 80%, dan duplikasi kode baru paling banyak",
                    "3%. Fokus ke kode baru sengaja dipilih supaya proyek lama tetap",
                    "bisa memakai gerbang tanpa harus membereskan semua utang dulu.",
                ],
            },
            {
                "heading": "Menjalankan pemindaian",
                "bahasa": "terminal",
                "code": "# Server SonarQube lokal di lab sendiri, lalu pemindai di folder proyek\nsonar-scanner \\\n  -Dsonar.projectKey=toko-ani \\\n  -Dsonar.sources=. \\\n  -Dsonar.host.url=http://localhost:9000 \\\n  -Dsonar.token=$SONAR_TOKEN",
            },
            {
                "heading": "CodeQL",
                "body": [
                    "CodeQL memperlakukan kode sebagai basis data. Kodemu diubah jadi",
                    "database CodeQL, lalu ditanya memakai bahasa kueri bernama QL.",
                    "Kuerinya dikemas dalam paket, misalnya `py/sql-injection` untuk",
                    "Python. CLI terbarunya saat materi ini ditulis adalah 2.27.2,",
                    "dirilis 7 Oktober 2026.",
                    "",
                    "Untuk pemula, cara termudah adalah default setup: buka repo di",
                    "GitHub, masuk Settings, Code security, lalu nyalakan code",
                    "scanning. GitHub memilih bahasa dan kueri sendiri. Kalau butuh",
                    "kendali lebih, pakai advanced setup berupa workflow yang",
                    "memanggil `github/codeql-action` (versi mayor terbarunya v4).",
                    "",
                    "Soal lisensi: CodeQL gratis untuk repo publik dan untuk riset.",
                    "Repo privat milik organisasi butuh lisensi berbayar dari GitHub",
                    "(paket Code Security).",
                    "",
                    "  aspek          SonarQube                 CodeQL",
                    "  pembuat        SonarSource               GitHub",
                    "  fokus          mutu dan keamanan         celah keamanan",
                    "  cara kerja     aturan per bahasa         kueri QL atas database",
                    "  gratis untuk   Community Build           repo publik",
                    "  hasil di       dasbor + quality gate     tab Security, komentar PR",
                ],
            },
            {
                "heading": "Positif palsu dan cara menanganinya",
                "body": [
                    "Positif palsu (false positive) adalah temuan yang ternyata",
                    "aman. Contohnya, query yang disambung string tapi nilainya",
                    "berasal dari daftar tetap di kode, bukan dari pengguna.",
                    "",
                    "Yang benar adalah menandainya di alat, lengkap dengan alasan.",
                    "SonarQube punya status \"Accept\" atau \"False positive\" untuk",
                    "issue, dan CodeQL punya tombol \"Dismiss alert\" dengan pilihan",
                    "alasan. Keduanya tercatat siapa yang memutuskan.",
                    "",
                    "Jebakan: mematikan seluruh aturan karena satu positif palsu.",
                    "Aturan itu juga menjaga ratusan tempat lain yang nggak kamu lihat.",
                    "",
                    "Ingat: nol temuan dari SAST bukan bukti aplikasi aman. Celah",
                    "otorisasi, misalnya pengguna yang bisa membuka pesanan orang lain",
                    "cukup dengan mengganti angka ID di URL, sering lolos. Kodenya",
                    "terlihat wajar, yang salah adalah pengecekan yang nggak ditulis.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek open source di GitHub memasang badge Quality Gate",
                    "dari SonarQube Cloud di README, dan tab Security repo publik",
                    "menampilkan hasil code scanning CodeQL. Dua-duanya bisa kamu",
                    "lihat di repo terkenal tanpa login.",
                    "",
                    "Kasus kecil: CodeQL menandai `py/sql-injection` di fungsi",
                    "laporan. Developer yakin aman, karena nama tabelnya diambil dari",
                    "parameter `jenis` yang \"cuma dipakai admin\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Telusuri jalur yang ditunjukkan CodeQL dari source ke sink.",
                    "     Kalau `jenis` datang dari permintaan HTTP, itu source dari",
                    "     luar, siapa pun penggunanya.",
                    "  2. Nama tabel nggak bisa diberi placeholder `?`. Pakai daftar",
                    "     putih:",
                    "       TABEL = {\"harian\": \"laporan_harian\", \"bulanan\": \"laporan_bulanan\"}",
                    "       nama_tabel = TABEL[jenis]",
                    "  3. Jalankan ulang analisis. Alert tertutup sendiri karena",
                    "     jalurnya sekarang melewati daftar putih.",
                    "  4. Kalau ternyata memang positif palsu, dismiss dengan alasan",
                    "     tertulis supaya reviewer berikutnya paham.",
                ],
            },
        ],
    },
    {
        "title": "28. Memindai Dependensi dan Image: Trivy dan Snyk",
        "sections": [
            {
                "body": [
                    "Aplikasi web biasa memakai ratusan paket pihak ketiga, dan",
                    "image container membawa ratusan paket sistem operasi lagi.",
                    "Kamu nggak menulis satu pun dari kode itu, tapi celahnya tetap",
                    "jadi celah aplikasimu.",
                    "",
                    "Pemindai SCA dan pemindai image menjawab satu pertanyaan:",
                    "\"dari semua paket yang terpasang, mana yang punya celah yang",
                    "sudah diketahui umum?\" Celah yang diketahui umum biasanya punya",
                    "nomor CVE (Common Vulnerabilities and Exposures), misalnya",
                    "CVE-2021-44228 untuk Log4Shell.",
                    "",
                    "Materi \"Rantai Pasok Perangkat Lunak: Lockfile dan Dependensi\"",
                    "di bab 06 sudah menjelaskan kenapa lockfile penting. Di sini",
                    "lockfile itu dipakai sebagai daftar yang dipindai.",
                ],
            },
            {
                "heading": "Trivy",
                "body": [
                    "Trivy adalah pemindai open source dari Aqua Security, ditulis",
                    "dalam Go dan berlisensi Apache-2.0. Versinya masih bernomor 0.x.",
                    "Saat materi ini ditulis (Oktober 2026), rilis terbarunya v0.76.0",
                    "tanggal 14 Oktober 2026.",
                    "",
                    "Satu program Trivy bisa memindai beberapa hal:",
                    "  - `trivy image`: paket OS dan pustaka di dalam image.",
                    "  - `trivy fs`: folder proyek, termasuk lockfile.",
                    "  - `trivy config`: salah konfigurasi di Terraform, Dockerfile,",
                    "    dan manifest Kubernetes. Pemindai tfsec yang dulu terpisah",
                    "    sudah dilebur ke sini.",
                    "  - `--scanners secret`: rahasia yang tertinggal di berkas.",
                    "  - `--format cyclonedx`: membuat SBOM.",
                    "",
                    "Trivy juga jadi pemindai bawaan registry Harbor, dan punya",
                    "Trivy Operator untuk memindai terus-menerus di dalam klaster",
                    "Kubernetes.",
                ],
            },
            {
                "heading": "Perintah Trivy",
                "bahasa": "terminal",
                "code": """# Image buatanmu sendiri, cuma tingkat tinggi, gagal kalau ada temuan
trivy image --severity HIGH,CRITICAL --exit-code 1 toko-ani:1.4.0

# Sembunyikan celah yang belum punya versi perbaikan
trivy image --ignore-unfixed toko-ani:1.4.0

# Folder proyek: dependensi dan salah konfigurasi
trivy fs --scanners vuln,misconfig .""",
            },
            {
                "heading": "Snyk",
                "body": [
                    "Snyk adalah platform komersial untuk keamanan developer. Bagian",
                    "intinya SCA, ditambah Snyk Code (SAST), Snyk Container, dan Snyk",
                    "IaC. CLI-nya open source berlisensi Apache-2.0, tapi hasilnya",
                    "diproses di layanan Snyk, jadi butuh akun. Paket gratisnya",
                    "dibatasi jumlah tes per bulan. Versi CLI terbaru saat materi ini",
                    "ditulis 1.1308.1.",
                    "",
                    "Kelebihan Snyk ada di saran perbaikan: ia bisa membuka pull",
                    "request yang menaikkan versi paket ke versi aman terdekat, dan",
                    "bisa memantau proyek terus-menerus lewat `snyk monitor`. Snyk",
                    "Learn berisi pelajaran keamanan gratis yang enak dipakai",
                    "sebagai bahan tambahan.",
                ],
            },
            {
                "heading": "Perintah Snyk",
                "bahasa": "terminal",
                "code": """snyk auth                               # sekali, membuka browser
snyk test --severity-threshold=high     # dependensi di folder ini
snyk container test toko-ani:1.4.0      # image
snyk iac test infra/                    # berkas Terraform
snyk monitor                            # kirim snapshot untuk dipantau""",
            },
            {
                "body": [
                    "Alat lain yang sering kamu temui: Grype dari Anchore, pemindai",
                    "open source yang mirip Trivy. Ada juga Dependabot di GitHub, yang",
                    "membuka pull request pembaruan dependensi secara otomatis.",
                ],
            },
            {
                "heading": "Memilih mana yang diperbaiki dulu",
                "body": [
                    "Pemindaian pertama hampir selalu menghasilkan puluhan temuan.",
                    "Mengurutkan cuma menurut skor CVSS (skala 0 sampai 10) sering",
                    "menyesatkan. Celah 9,8 di pustaka yang nggak pernah dipanggil",
                    "bisa kalah penting dari celah 7,5 yang sedang aktif dieksploitasi.",
                    "",
                    "Pertanyaan yang lebih berguna:",
                    "  - Sudah ada versi perbaikannya? Kalau belum, yang bisa",
                    "    dilakukan cuma mitigasi dan memantau.",
                    "  - Celahnya ada di daftar Known Exploited Vulnerabilities milik",
                    "    badan keamanan siber Amerika Serikat (CISA)? Daftar itu, yang",
                    "    biasa disingkat KEV, berisi celah yang terbukti sudah dipakai",
                    "    menyerang. Skor EPSS memberi perkiraan peluang sebuah celah",
                    "    dieksploitasi dalam 30 hari ke depan.",
                    "  - Paketnya ada di layanan yang menghadap internet, atau cuma",
                    "    di alat build internal?",
                    "  - Kode yang rentan memang dipanggil aplikasimu?",
                    "",
                    "Program di bawah menggabungkan beberapa pertanyaan itu jadi",
                    "urutan kerja. ID-nya karangan, supaya nggak tertukar dengan CVE",
                    "sungguhan.",
                ],
            },
            {
                "heading": "Urutan perbaikan",
                "code": """# Data tiruan dengan ID karangan. Bentuknya mirip keluaran pemindai:
# skor CVSS, ada versi perbaikan atau belum, masuk katalog KEV atau tidak,
# dan apakah paketnya terpasang di image yang menghadap internet.
temuan = [
    ("CONTOH-01", "libexpat", 9.8, True, False, False),
    ("CONTOH-02", "openssl", 7.5, True, True, True),
    ("CONTOH-03", "zlib", 5.3, False, False, True),
    ("CONTOH-04", "curl", 8.1, True, False, True),
]


def prioritas(cvss, ada_fix, kev, publik):
    if kev and publik:
        return "P1 hari ini"
    if cvss >= 7.0 and ada_fix and publik:
        return "P2 minggu ini"
    if cvss >= 7.0 and ada_fix:
        return "P3 sprint depan"
    if not ada_fix:
        return "P4 pantau"
    return "P4 jadwalkan"


urut = sorted(temuan, key=lambda t: prioritas(*t[2:]))
for id_, paket, cvss, ada_fix, kev, publik in urut:
    print(f"{id_}  {paket:9}{cvss:>4}  {prioritas(cvss, ada_fix, kev, publik)}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  CONTOH-02  openssl   7.5  P1 hari ini",
                    "  CONTOH-04  curl      8.1  P2 minggu ini",
                    "  CONTOH-01  libexpat  9.8  P3 sprint depan",
                    "  CONTOH-03  zlib      5.3  P4 pantau",
                    "",
                    "Skor tertinggi (9,8) malah turun ke P3 karena paketnya cuma ada",
                    "di layanan internal. Aturan seperti ini sebaiknya ditulis dan",
                    "disepakati tim sebelum ada insiden, bukan diputuskan dadakan.",
                    "",
                    "Jebakan: memperbaiki image dengan menaikkan versi pustaka",
                    "aplikasi, padahal celahnya ada di paket OS image dasar. Lihat",
                    "kolom target di laporan Trivy. Celah di `debian 12` diperbaiki",
                    "dengan membangun ulang di atas image dasar yang lebih baru.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Desember 2021, Log4Shell (CVE-2021-44228) di pustaka Java Log4j",
                    "membuat banyak tim kebingungan mencari di mana saja Log4j",
                    "terpasang, termasuk sebagai dependensi transitif yang nggak",
                    "pernah mereka tulis. Tim yang sudah rutin memindai image dan",
                    "lockfile bisa menjawab pertanyaan itu jauh lebih cepat.",
                    "",
                    "Kasus kecil: laporan Trivy untuk image `toko-ani:1.4.0` berisi",
                    "38 temuan HIGH. Developer menghabiskan sehari menaikkan versi",
                    "paket Python, tapi jumlahnya cuma turun jadi 35.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kelompokkan temuan menurut kolom Target. Ternyata 33 temuan",
                    "     ada di paket OS image dasar, bukan di requirements.txt.",
                    "  2. Ganti image dasar ke versi slim yang lebih baru, lalu bangun",
                    "     ulang:",
                    "       FROM python:3.13-slim",
                    "  3. Pindai ulang dengan `trivy image --ignore-unfixed` untuk",
                    "     melihat apa yang memang bisa diperbaiki sekarang.",
                    "  4. Sisanya catat di `.trivyignore` lengkap dengan alasan dan",
                    "     tanggal tinjau ulang, lalu pasang pemindaian terjadwal.",
                ],
            },
        ],
    },
    {
        "title": "29. Memindai Infrastructure as Code: Checkov dan KICS",
        "sections": [
            {
                "body": [
                    "Infrastructure as Code (IaC) artinya server, jaringan, dan",
                    "bucket penyimpanan ditulis sebagai berkas teks, misalnya",
                    "Terraform atau manifest Kubernetes, lalu dibuat oleh alat.",
                    "Kurikulum DevOps membahas cara menulisnya. Kabar baiknya untuk",
                    "keamanan: karena infrastrukturnya berupa teks, ia bisa dipindai",
                    "sebelum dibuat.",
                    "",
                    "Banyak kebocoran data di cloud bukan akibat peretasan canggih.",
                    "Penyebabnya bucket yang terbuka untuk publik, database tanpa",
                    "enkripsi, atau port SSH yang menerima koneksi dari seluruh",
                    "internet. Semua itu kelihatan di berkas Terraform sebelum",
                    "`terraform apply` dijalankan.",
                ],
            },
            {
                "heading": "Berkas yang bermasalah",
                "bahasa": "hcl",
                "code": """resource "aws_s3_bucket_acl" "foto" {
  bucket = aws_s3_bucket.foto.id
  acl    = "public-read"
}

resource "aws_security_group" "ssh" {
  name = "ssh-admin"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}""",
            },
            {
                "body": [
                    "Dua masalah di sini. Bucket `foto` bisa dibaca siapa saja, dan",
                    "port 22 terbuka untuk semua alamat (0.0.0.0/0 artinya \"semua",
                    "alamat IPv4\"). Bot di internet memindai port SSH terus-menerus,",
                    "jadi server seperti ini akan langsung menerima tebakan password.",
                ],
            },
            {
                "heading": "Checkov",
                "body": [
                    "Checkov adalah pemindai IaC open source yang ditulis dalam",
                    "Python, berlisensi Apache-2.0. Pembuatnya Bridgecrew, yang",
                    "kemudian dibeli Palo Alto Networks. Rilisnya sering sekali, dan",
                    "saat materi ini ditulis versi terbarunya 3.3.29 (13 Oktober",
                    "2026). Ia membaca Terraform, CloudFormation, Kubernetes,",
                    "Helm, Dockerfile, dan beberapa format lain.",
                    "",
                    "Tiap aturan punya ID. Beberapa yang relevan dengan contoh tadi,",
                    "dengan deskripsi dari indeks kebijakan resminya:",
                    "  - CKV_AWS_20: bucket S3 punya ACL yang mengizinkan baca publik.",
                    "  - CKV_AWS_24: security group nggak boleh menerima 0.0.0.0/0 ke",
                    "    port 22.",
                    "  - CKV_AWS_19: data di bucket S3 harus terenkripsi saat disimpan.",
                    "  - CKV_AWS_16: data di RDS harus terenkripsi saat disimpan.",
                ],
            },
            {
                "heading": "Menjalankan Checkov",
                "bahasa": "terminal",
                "code": """pip install checkov          # di virtualenv, bukan global
checkov -d infra/            # pindai satu folder
checkov -d infra/ --compact  # ringkas, tanpa potongan kode

# Memindai hasil plan, supaya nilai variabel ikut terhitung
terraform plan -out tfplan
terraform show -json tfplan > tfplan.json
checkov -f tfplan.json""",
            },
            {
                "body": [
                    "Keluarannya kira-kira berbentuk seperti ini (dipangkas):",
                    "",
                    "  Check: CKV_AWS_24: \"Ensure no security groups allow ingress",
                    "         from 0.0.0.0:0 to port 22\"",
                    "      FAILED for resource: aws_security_group.ssh",
                    "      File: /main.tf:6-14",
                    "",
                    "  Passed checks: 12, Failed checks: 2, Skipped checks: 0",
                    "",
                    "Checkov keluar dengan kode 1 kalau ada pemeriksaan yang gagal,",
                    "jadi langsung bisa dipakai sebagai gerbang di CI.",
                    "",
                    "Kadang pelanggaran itu disengaja. Bucket untuk hosting situs",
                    "statis memang harus bisa dibaca publik. Untuk itu ada komentar",
                    "pengecualian di dalam resource, lengkap dengan alasannya:",
                ],
            },
            {
                "heading": "Pengecualian yang tertulis",
                "bahasa": "hcl",
                "code": """resource "aws_s3_bucket_acl" "situs" {
  #checkov:skip=CKV_AWS_20:Bucket ini hosting situs statis publik
  bucket = aws_s3_bucket.situs.id
  acl    = "public-read"
}""",
            },
            {
                "heading": "KICS",
                "body": [
                    "KICS (Keeping Infrastructure as Code Secure) adalah pemindai IaC",
                    "open source dari Checkmarx, ditulis dalam Go dan berlisensi",
                    "Apache-2.0. Versi terbarunya saat materi ini ditulis v2.2.0,",
                    "dirilis 17 September 2026. Aturannya ditulis dalam Rego, bahasa",
                    "yang sama dengan Open Policy Agent di bab 03, dan ia membaca",
                    "Terraform, Kubernetes, Dockerfile, Ansible, dan lainnya.",
                    "",
                    "Fungsi keduanya mirip. Pilih salah satu yang cocok",
                    "dengan ekosistem timmu. Trivy juga bisa memeriksa salah",
                    "konfigurasi lewat `trivy config`, jadi tim yang sudah memakai",
                    "Trivy untuk image kadang nggak menambah alat lagi.",
                ],
            },
            {
                "heading": "Menjalankan KICS",
                "bahasa": "terminal",
                "code": "kics scan -p infra/ -o hasil-kics/",
            },
            {
                "heading": "Pemeriksa Dockerfile mini",
                "body": [
                    "Cara kerja alat-alat ini sederhana: baca berkas, cocokkan dengan",
                    "aturan, laporkan pelanggaran. Program di bawah menerapkan tiga",
                    "aturan Dockerfile yang juga dimiliki Checkov, dalam bentuk mini.",
                ],
            },
            {
                "heading": "Contoh pemeriksa",
                "code": "dockerfile = \"\"\"FROM python:latest\nCOPY . /app\nRUN pip install -r /app/requirements.txt\nENV API_KEY=sk_live_contoh123\nCMD [\"python\", \"/app/main.py\"]\"\"\"\n\nada_user = False\nfor no, baris in enumerate(dockerfile.splitlines(), 1):\n    perintah, _, isi = baris.partition(\" \")\n    if perintah == \"FROM\" and (\":\" not in isi or isi.endswith(\":latest\")):\n        print(f\"baris {no}: image tanpa versi tetap ({isi})\")\n    if perintah == \"ENV\" and any(k in isi.upper() for k in (\"KEY\", \"TOKEN\", \"PASS\")):\n        print(f\"baris {no}: rahasia di ENV ikut tersimpan di image\")\n    if perintah == \"USER\":\n        ada_user = isi.strip() not in (\"root\", \"0\")\nif not ada_user:\n    print(\"akhir berkas: tidak ada USER, container jalan sebagai root\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "  baris 1: image tanpa versi tetap (python:latest)",
                    "  baris 4: rahasia di ENV ikut tersimpan di image",
                    "  akhir berkas: tidak ada USER, container jalan sebagai root",
                    "",
                    "Jebakan: memindai berkas `.tf` saja lalu merasa aman. Nilai",
                    "variabel dan modul dari registry baru kelihatan di hasil",
                    "`terraform plan`. Kalau bisa, pindai juga JSON hasil plan.",
                    "",
                    "Ingat: pemindai IaC cuma melihat apa yang ditulis di kode.",
                    "Perubahan yang diklik manual di konsol cloud nggak kelihatan.",
                    "Itu urusan CSPM, yang dibahas di bab 09.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bucket S3 yang terbuka untuk publik berulang kali jadi berita",
                    "kebocoran data. AWS sendiri menanggapinya dengan mengaktifkan",
                    "S3 Block Public Access dan menonaktifkan ACL secara bawaan untuk",
                    "bucket baru sejak April 2023. Konfigurasi lama dan modul",
                    "Terraform lama masih bisa membukanya lagi, dan di situ pemindai",
                    "IaC berguna.",
                    "",
                    "Kasus kecil: pull request menambah modul Terraform untuk",
                    "database pesanan. Checkov gagal dengan CKV_AWS_16, dan penulis",
                    "pull request bertanya apakah boleh di-skip karena \"cuma",
                    "staging\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tanya dulu datanya. Kalau staging berisi salinan data",
                    "     pelanggan, aturannya sama dengan produksi.",
                    "  2. Perbaiki di kodenya, jangan di-skip:",
                    "       storage_encrypted = true",
                    "  3. Enkripsi RDS nggak bisa dinyalakan di tempat untuk",
                    "     database yang sudah ada. Rencanakan snapshot, salin dengan",
                    "     enkripsi, lalu pulihkan, dan catat itu di pull request.",
                    "  4. Kalau ada skip yang memang sah, tulis alasannya di komentar",
                    "     `#checkov:skip` supaya bisa diaudit.",
                ],
            },
        ],
    },
    {
        "title": "30. Memetakan Jaringan Sendiri dengan Nmap",
        "sections": [
            {
                "heading": "Aturan lab",
                "body": [
                    "Aturan dulu, sebelum satu perintah pun: alat di materi ini hanya",
                    "boleh diarahkan ke sistem milikmu sendiri atau ke lab yang memang",
                    "disediakan untuk latihan. Contohnya mesin virtual di laptopmu,",
                    "container di localhost, aplikasi latihan seperti Juice Shop",
                    "yang kamu jalankan sendiri, lab Web Security Academy dari",
                    "PortSwigger, dan soal kompetisi CTF. Jaringan kantor, kampus,",
                    "WiFi kafe, atau situs orang lain nggak termasuk, walaupun kamu",
                    "\"cuma mau lihat\".",
                    "",
                    "Kalau nanti kamu menguji sistem orang lain sebagai pekerjaan,",
                    "syaratnya izin tertulis dari pemilik sistem yang menyebut target,",
                    "waktu, dan jenis pengujian yang boleh. Alasannya ada di materi",
                    "\"Etika, Hukum, dan Lab Legal untuk Belajar Keamanan\" di bab 01.",
                    "Kalau belum membacanya, baca dulu sebelum lanjut.",
                ],
            },
            {
                "heading": "Kenapa memetakan jaringan sendiri",
                "body": [
                    "Kamu nggak bisa melindungi sesuatu yang kamu nggak tahu ada.",
                    "Contohnya server uji coba yang lalu dilupakan, atau database yang",
                    "ternyata menerima koneksi dari mana saja. Bisa juga panel admin",
                    "yang terbuka di port 8080. Semua itu sering baru ketahuan saat",
                    "orang lain menemukannya duluan.",
                    "",
                    "Memetakan jaringan artinya membuat daftar host (mesin yang",
                    "hidup) dan port yang terbuka di tiap host, lalu mencocokkannya",
                    "dengan daftar yang seharusnya. Port itu nomor pintu layanan di",
                    "sebuah mesin: SSH biasanya di 22, HTTP di 80, HTTPS di 443,",
                    "PostgreSQL di 5432. Port yang terbuka tapi nggak ada di daftar",
                    "adalah pekerjaan rumah: tutup, atau catat kenapa harus terbuka.",
                    "",
                    "Nmap adalah alat klasik untuk pekerjaan ini. Ditulis dalam C dan",
                    "C++, dengan mesin skrip berbahasa Lua (Nmap Scripting Engine).",
                    "Lisensinya Nmap Public Source License, turunan GPLv2 dengan",
                    "syarat tambahan.",
                    "Saat materi ini ditulis (Oktober 2026), tag rilis terbarunya di",
                    "repositori resminya adalah 7.992, tanggal 12 Oktober 2026. Ada",
                    "juga Zenmap, tampilan grafisnya, kalau kamu lebih suka klik.",
                ],
            },
            {
                "heading": "Menyiapkan lab",
                "body": [
                    "Lab paling murah ada di laptopmu sendiri:",
                    "  - Localhost (127.0.0.1). Pindai mesinmu sendiri untuk melihat",
                    "    layanan apa saja yang sedang mendengarkan.",
                    "  - Jaringan host-only VirtualBox. Bawaannya memakai rentang",
                    "    192.168.56.0/24, dan jaringan ini cuma bisa dijangkau dari",
                    "    laptopmu dan mesin virtual di dalamnya.",
                    "  - Container di localhost, misalnya database atau aplikasi",
                    "    latihan, dengan port yang diterbitkan ke 127.0.0.1 saja.",
                    "",
                    "Contoh di materi ini memakai rentang 192.168.56.0/24 dengan dua",
                    "mesin virtual: `web-lab` di .10 dan `db-lab` di .20.",
                ],
            },
            {
                "heading": "Perintah dasar",
                "bahasa": "terminal",
                "code": """# Mesinmu sendiri: 1000 port TCP yang paling umum (bawaan Nmap)
nmap 127.0.0.1

# Host mana yang hidup di jaringan host-only lab, tanpa pindai port
nmap -sn 192.168.56.0/24

# Semua 65535 port TCP satu VM lab, plus nama dan versi layanannya
nmap -p- -sV 192.168.56.10

# Simpan hasil dalam tiga format: biasa, XML, dan grepable
nmap -sV -oA hasil/lab-2026-10-19 192.168.56.0/24""",
            },
            {
                "body": [
                    "Tanpa hak root, Nmap memakai connect scan (`-sT`), yaitu",
                    "membuka koneksi TCP biasa ke tiap port. Dengan `sudo`, bawaannya",
                    "SYN scan (`-sS`) yang lebih cepat karena nggak menyelesaikan",
                    "jabat tangan TCP. Untuk lab sendiri dua-duanya cukup.",
                    "",
                    "Format grepable (`-oG`) menaruh satu host per baris, jadi enak",
                    "diolah program. Format XML (`-oX`) paling lengkap dan dipakai",
                    "alat lain sebagai masukan.",
                ],
            },
            {
                "heading": "Membaca status port",
                "body": [
                    "Nmap memberi tiap port salah satu dari enam status. Tiga yang",
                    "paling sering muncul:",
                    "",
                    "  status     artinya                                  tindakan",
                    "  open       ada layanan yang menerima koneksi         cocokkan",
                    "  closed     host menjawab, tapi nggak ada layanan     biarkan",
                    "  filtered   nggak ada jawaban, kemungkinan firewall   periksa",
                    "",
                    "Tiga sisanya lebih jarang: unfiltered (port bisa dijangkau tapi",
                    "Nmap nggak bisa memastikan terbuka atau tertutup), open|filtered,",
                    "dan closed|filtered. Dua yang terakhir muncul saat Nmap nggak",
                    "bisa membedakan dua kemungkinan itu, sering terjadi di pindaian",
                    "UDP.",
                    "",
                    "Contoh keluaran untuk satu VM lab:",
                    "",
                    "  PORT     STATE    SERVICE    VERSION",
                    "  22/tcp   open     ssh        OpenSSH 9.6 (protocol 2.0)",
                    "  80/tcp   open     http       nginx 1.26.2",
                    "  3306/tcp open     mysql      MySQL 8.0.40",
                    "  8080/tcp filtered http-proxy",
                    "",
                    "Kalau daftar izin `web-lab` cuma 22, 80, dan 443, berarti MySQL",
                    "di 3306 nggak seharusnya bisa dijangkau dari jaringan. Database",
                    "cukup mendengarkan di 127.0.0.1, atau dibatasi firewall supaya",
                    "cuma server aplikasi yang boleh masuk.",
                ],
            },
            {
                "heading": "Membandingkan dua pemindaian",
                "body": [
                    "Pemindaian sekali jalan cuma memotret satu saat. Yang lebih",
                    "berguna adalah memindai rutin lalu melihat apa yang berubah.",
                    "Nmap membawa alat `ndiff` untuk membandingkan dua berkas XML.",
                    "Program di bawah meniru idenya dengan himpunan Python.",
                ],
            },
            {
                "heading": "Selisih dua pemindaian",
                "code": """# Hasil dua pemindaian lab sendiri, sudah diringkas jadi port terbuka per host.
kemarin = {
    "192.168.56.10": {"22/tcp", "80/tcp"},
    "192.168.56.20": {"22/tcp", "5432/tcp"},
}
hari_ini = {
    "192.168.56.10": {"22/tcp", "80/tcp", "8080/tcp"},
    "192.168.56.20": {"22/tcp"},
    "192.168.56.30": {"22/tcp"},
}

for ip in sorted(kemarin.keys() | hari_ini.keys()):
    lama = kemarin.get(ip, set())
    baru = hari_ini.get(ip, set())
    if ip not in kemarin:
        print(f"{ip}: host baru, port {sorted(baru)}")
        continue
    for port in sorted(baru - lama):
        print(f"{ip}: port baru terbuka {port}")
    for port in sorted(lama - baru):
        print(f"{ip}: port hilang {port}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  192.168.56.10: port baru terbuka 8080/tcp",
                    "  192.168.56.20: port hilang 5432/tcp",
                    "  192.168.56.30: host baru, port ['22/tcp']",
                    "",
                    "Tiga baris itu masing-masing pertanyaan untuk tim. Siapa yang",
                    "menyalakan layanan di 8080? Kenapa PostgreSQL hilang, mati atau",
                    "pindah? Mesin .30 itu punya siapa?",
                ],
            },
            {
                "heading": "Menutup yang nggak perlu",
                "bahasa": "terminal",
                "code": """# Di VM lab Fedora: layanan apa yang mendengarkan, dan prosesnya apa
sudo ss -tlnp

# Lihat aturan firewalld, lalu tutup layanan yang nggak perlu
sudo firewall-cmd --list-all
sudo firewall-cmd --permanent --remove-service=mysql
sudo firewall-cmd --reload""",
            },
            {
                "body": [
                    "Firewall cuma menambal dari luar. Perbaikan yang lebih bersih",
                    "adalah mengatur layanannya sendiri, misalnya MySQL dengan",
                    "`bind-address = 127.0.0.1`, atau mematikan layanan yang memang",
                    "nggak dipakai.",
                    "",
                    "Jebakan: memindai dari laptop yang sama lalu menyimpulkan semua",
                    "aman. Firewall sering mengizinkan koneksi dari mesin tertentu,",
                    "jadi hasilnya tergantung dari mana kamu memindai. Pindai dari",
                    "posisi yang ingin kamu uji, misalnya dari VM lain di jaringan",
                    "lab.",
                    "",
                    "Ingat: Nmap punya skrip yang bisa melakukan lebih dari",
                    "sekadar melihat port, termasuk mencoba login. Di lab sendiri itu",
                    "boleh dipelajari. Di luar lab, aturan izin di awal materi tetap",
                    "berlaku untuk setiap skrip.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mesin pencari perangkat seperti Shodan dan Censys terus memindai",
                    "internet dan mencatat port terbuka beserta bannernya. Database",
                    "seperti MongoDB, Elasticsearch, dan Redis yang terbuka tanpa",
                    "password berulang kali ditemukan lewat cara ini lalu datanya",
                    "dihapus atau disandera. Pemilik yang rutin memetakan jaringannya",
                    "sendiri bisa menutupnya lebih dulu.",
                    "",
                    "Kasus kecil: kamu mengurus dua VM lab, `web-lab` dan `db-lab`.",
                    "Daftar izinnya: web-lab boleh 22, 80, 443; db-lab cuma 22 dan",
                    "5432. Kamu ingin tahu apakah keadaannya masih sesuai.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindai jaringan host-only dari VM ketiga dan simpan hasil",
                    "     grepable:",
                    "       nmap -sV -oG lab.gnmap 192.168.56.0/24",
                    "  2. Ambil baris yang memuat Ports: untuk tiap host, dan catat",
                    "     port berstatus open beserta layanannya.",
                    "  3. Bandingkan dengan daftar izin. Port open yang nggak ada di",
                    "     daftar masuk laporan \"harus ditutup\".",
                    "  4. Tutup di layanannya atau di firewalld, lalu pindai ulang",
                    "     untuk membuktikan port itu sekarang closed atau filtered.",
                    "  5. Jadwalkan pemindaian yang sama tiap minggu dan bandingkan",
                    "     dengan hasil sebelumnya memakai ndiff.",
                ],
            },
        ],
    },
    {
        "title": "31. Menguji Aplikasi Web Sendiri: ZAP dan Burp Suite",
        "sections": [
            {
                "heading": "Aturan lab",
                "body": [
                    "Aturan dulu, sebelum satu perintah pun: alat di materi ini hanya",
                    "boleh diarahkan ke sistem milikmu sendiri atau ke lab yang memang",
                    "disediakan untuk latihan. Contohnya mesin virtual di laptopmu,",
                    "container di localhost, aplikasi latihan seperti Juice Shop",
                    "yang kamu jalankan sendiri, lab Web Security Academy dari",
                    "PortSwigger, dan soal kompetisi CTF. Jaringan kantor, kampus,",
                    "WiFi kafe, atau situs orang lain nggak termasuk, walaupun kamu",
                    "\"cuma mau lihat\".",
                    "",
                    "Kalau nanti kamu menguji sistem orang lain sebagai pekerjaan,",
                    "syaratnya izin tertulis dari pemilik sistem yang menyebut target,",
                    "waktu, dan jenis pengujian yang boleh. Alasannya ada di materi",
                    "\"Etika, Hukum, dan Lab Legal untuk Belajar Keamanan\" di bab 01.",
                    "Kalau belum membacanya, baca dulu sebelum lanjut.",
                ],
            },
            {
                "heading": "Apa yang dilakukan penguji web",
                "body": [
                    "Bab 04 membahas celah aplikasi web dari sisi kode. Materi ini",
                    "melihatnya dari luar: aplikasi dijalankan, lalu permintaannya",
                    "diamati dan diuji. Ini yang disebut DAST di bab 07.",
                    "",
                    "Dua alat yang paling sering dipakai bekerja dengan cara yang",
                    "sama. Mereka berdiri sebagai proxy di antara browser dan",
                    "aplikasi. Proxy itu perantara: setiap permintaan dari browser",
                    "lewat dia dulu sebelum sampai ke server, dan setiap jawaban",
                    "server lewat dia sebelum sampai ke browser. Dari posisi itu alat",
                    "bisa mencatat, menahan, mengubah, lalu mengirim ulang permintaan.",
                    "",
                    "Lab yang dipakai di sini: Juice Shop dari OWASP, toko online yang",
                    "sengaja dibuat penuh celah untuk latihan. Jalankan di laptopmu",
                    "dan terbitkan port-nya ke 127.0.0.1 saja, supaya orang lain di",
                    "jaringan yang sama nggak bisa ikut membukanya.",
                ],
            },
            {
                "heading": "Menyalakan lab Juice Shop",
                "bahasa": "terminal",
                "code": """docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
# buka http://localhost:3000 di browser""",
            },
            {
                "heading": "ZAP",
                "body": [
                    "ZAP adalah alat DAST open source berlisensi Apache-2.0, ditulis",
                    "dalam Java. Dulu ia proyek di bawah yayasan OWASP. Sejak",
                    "September 2024 proyeknya pindah dan sekarang bernama ZAP by",
                    "Checkmarx. Rilis stabil terbarunya saat materi ini ditulis",
                    "(Oktober 2026) adalah 2.17.0, dirilis 15 Desember 2025. Selain",
                    "itu ada rilis mingguan untuk yang ingin fitur terbaru.",
                    "",
                    "Ada dua cara memeriksa:",
                    "  - Passive scan: cuma membaca permintaan dan jawaban yang lewat,",
                    "    lalu mencari masalah seperti header keamanan yang hilang.",
                    "    Nggak mengirim apa pun yang aneh ke aplikasi.",
                    "  - Active scan: sengaja mengirim masukan berbahaya ke setiap",
                    "    parameter untuk melihat reaksi aplikasi. Ini serangan",
                    "    sungguhan dalam versi otomatis, jadi cuma untuk lab sendiri",
                    "    atau sistem yang izinnya tertulis.",
                    "",
                    "Untuk CI tersedia skrip siap pakai di image Docker resminya.",
                    "`zap-baseline.py` menjelajah aplikasi sebentar (bawaannya satu",
                    "menit) lalu menjalankan passive scan saja. `zap-full-scan.py`",
                    "menambah active scan. `zap-api-scan.py` memakai definisi",
                    "OpenAPI untuk menguji API.",
                ],
            },
            {
                "heading": "Baseline scan ke lab sendiri",
                "bahasa": "terminal",
                "code": "# --network host supaya container ZAP bisa menjangkau localhost:3000\ndocker run --rm --network host -v \"$(pwd)\":/zap/wrk:rw \\\n  ghcr.io/zaproxy/zaproxy:stable \\\n  zap-baseline.py -t http://localhost:3000 -J laporan.json -r laporan.html",
            },
            {
                "body": [
                    "Kode keluar baseline scan bisa dipakai sebagai gerbang: 0 berarti",
                    "aman, 1 berarti ada aturan berstatus gagal, 2 berarti cuma ada",
                    "peringatan (WARN), dan 3 berarti terjadi galat lain. Status tiap",
                    "aturan bisa diatur lewat berkas konfigurasi (`-c`), misalnya",
                    "menaikkan aturan 10038 (header CSP hilang) dari peringatan jadi",
                    "gagal.",
                    "",
                    "Laporan JSON-nya bisa diolah program. Contoh di bawah memakai",
                    "versi yang dipangkas dari laporan Juice Shop di localhost.",
                ],
            },
            {
                "heading": "Meringkas laporan ZAP",
                "code": "import json\n\n# Laporan JSON ZAP yang dipangkas: satu situs, tiga alert.\nlaporan = json.loads(\"\"\"\n{\"site\": [{\"@name\": \"http://localhost:3000\", \"alerts\": [\n  {\"pluginid\": \"10038\", \"alert\": \"Content Security Policy (CSP) Header Not Set\",\n   \"riskcode\": \"2\", \"count\": \"14\"},\n  {\"pluginid\": \"10021\", \"alert\": \"X-Content-Type-Options Header Missing\",\n   \"riskcode\": \"1\", \"count\": \"9\"},\n  {\"pluginid\": \"10027\", \"alert\": \"Information Disclosure - Suspicious Comments\",\n   \"riskcode\": \"0\", \"count\": \"3\"}]}]}\n\"\"\")\n\nRISIKO = {\"3\": \"Tinggi\", \"2\": \"Sedang\", \"1\": \"Rendah\", \"0\": \"Info\"}\nfor situs in laporan[\"site\"]:\n    print(situs[\"@name\"])\n    alerts = sorted(situs[\"alerts\"], key=lambda a: a[\"riskcode\"], reverse=True)\n    for a in alerts:\n        print(f\"  {RISIKO[a['riskcode']]:7}{a['pluginid']:>6}  x{a['count']:<3} {a['alert']}\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "  http://localhost:3000",
                    "    Sedang  10038  x14  Content Security Policy (CSP) Header Not Set",
                    "    Rendah  10021  x9   X-Content-Type-Options Header Missing",
                    "    Info    10027  x3   Information Disclosure - Suspicious Comments",
                    "",
                    "Angka `x14` artinya alert yang sama ditemukan di 14 URL. Satu",
                    "perbaikan di konfigurasi server, misalnya memasang header CSP",
                    "untuk semua halaman, menutup keempat belasnya sekaligus. Header",
                    "keamanan dibahas di bab 05.",
                ],
            },
            {
                "heading": "Burp Suite",
                "body": [
                    "Burp Suite buatan PortSwigger adalah alat yang paling sering",
                    "dipakai penguji penetrasi web profesional. Nomor versinya",
                    "berpola tahun.bulan, dan rilis terbaru yang tercantum di halaman",
                    "rilis resminya saat materi ini ditulis adalah 2026.10, tanggal 12",
                    "Oktober 2026. Ada tiga edisi:",
                    "  - Community Edition: gratis, cukup untuk belajar. Proxy,",
                    "    Repeater, dan Decoder lengkap, tapi tanpa pemindai otomatis",
                    "    dan Intruder-nya dibatasi kecepatannya.",
                    "  - Professional: berbayar per tahun, menambah pemindai",
                    "    otomatis dan fitur untuk pengujian harian.",
                    "  - Burp Suite DAST: dulu bernama Enterprise Edition, untuk",
                    "    pemindaian terjadwal skala organisasi.",
                    "",
                    "Alur kerja dasarnya di lab Juice Shop:",
                    "  1. Buka browser bawaan Burp (Chromium yang sudah diarahkan ke",
                    "     proxy-nya), lalu jelajahi http://localhost:3000.",
                    "  2. Lihat riwayat permintaan di tab Proxy, HTTP history.",
                    "  3. Kirim satu permintaan ke Repeater, ubah satu parameter,",
                    "     kirim lagi, dan bandingkan jawabannya. Di situ kamu melihat",
                    "     apakah server memeriksa masukan dengan benar.",
                    "",
                    "PortSwigger juga membuat Web Security Academy, kumpulan materi",
                    "dan lab gratis yang sah untuk diserang. Lab-nya berjalan di",
                    "server mereka khusus untuk latihan, jadi cocok sebagai lanjutan",
                    "Juice Shop.",
                ],
            },
            {
                "heading": "ZAP atau Burp",
                "body": [
                    "  aspek          ZAP                       Burp Suite",
                    "  lisensi        Apache-2.0, gratis        Community gratis, Pro bayar",
                    "  pemindai aktif ada, gratis               cuma di edisi berbayar",
                    "  otomasi CI     skrip Docker siap pakai   lewat edisi DAST",
                    "  cocok untuk    gerbang CI, belajar       pengujian manual mendalam",
                    "",
                    "Banyak orang memakai keduanya: alat gratis di pipeline, lalu Burp",
                    "saat menelusuri satu temuan dengan tangan.",
                    "",
                    "Jebakan: menjalankan active scan ke aplikasi staging yang",
                    "terhubung ke layanan sungguhan. Active scan bisa mengisi",
                    "formulir ratusan kali, mengirim email ke alamat palsu, atau",
                    "menghapus data. Pakai data uji dan lingkungan yang boleh rusak.",
                    "",
                    "Ingat: aturan izin di awal materi ini juga berlaku untuk proxy.",
                    "Mencegat lalu lintas orang lain di jaringan yang sama, walaupun",
                    "cuma untuk dilihat, sudah di luar lab.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program bug bounty seperti di HackerOne dan Bugcrowd memberi",
                    "izin tertulis lewat halaman cakupan (scope): domain mana yang",
                    "boleh diuji dan jenis pengujian apa yang dilarang. Banyak",
                    "program melarang pemindaian otomatis yang membanjiri server.",
                    "Di sisi tim pengembang, baseline scan di CI adalah cara",
                    "yang umum untuk menangkap header yang hilang sebelum rilis.",
                    "",
                    "Kasus kecil: aplikasi tokomu jalan di Docker Compose di laptop.",
                    "Kamu ingin setiap pull request dicek baseline scan, dan pull",
                    "request gagal kalau header CSP hilang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Di job CI, nyalakan aplikasi dengan Compose dan tunggu",
                    "     sampai halaman utamanya menjawab.",
                    "  2. Buat berkas aturan dengan `-g zap.conf` sekali, lalu ubah",
                    "     baris aturan 10038 jadi status gagal:",
                    "       10038  FAIL  (Content Security Policy (CSP) Header Not Set)",
                    "  3. Jalankan baseline scan dengan `-c zap.conf` ke alamat",
                    "     aplikasi di runner CI itu sendiri.",
                    "  4. Biarkan kode keluar 1 menggagalkan job, dan simpan",
                    "     laporan HTML sebagai artefak supaya bisa dibaca reviewer.",
                ],
            },
        ],
    },
    {
        "title": "32. Pemindai Kerentanan: Nessus, OpenVAS, dan Qualys",
        "sections": [
            {
                "heading": "Aturan lab",
                "body": [
                    "Aturan dulu, sebelum satu perintah pun: alat di materi ini hanya",
                    "boleh diarahkan ke sistem milikmu sendiri atau ke lab yang memang",
                    "disediakan untuk latihan. Contohnya mesin virtual di laptopmu,",
                    "container di localhost, aplikasi latihan seperti Juice Shop",
                    "yang kamu jalankan sendiri, lab Web Security Academy dari",
                    "PortSwigger, dan soal kompetisi CTF. Jaringan kantor, kampus,",
                    "WiFi kafe, atau situs orang lain nggak termasuk, walaupun kamu",
                    "\"cuma mau lihat\".",
                    "",
                    "Kalau nanti kamu menguji sistem orang lain sebagai pekerjaan,",
                    "syaratnya izin tertulis dari pemilik sistem yang menyebut target,",
                    "waktu, dan jenis pengujian yang boleh. Alasannya ada di materi",
                    "\"Etika, Hukum, dan Lab Legal untuk Belajar Keamanan\" di bab 01.",
                    "Kalau belum membacanya, baca dulu sebelum lanjut.",
                ],
            },
            {
                "heading": "Beda dengan Nmap dan ZAP",
                "body": [
                    "Nmap menjawab \"port apa yang terbuka\". Penguji web menjawab",
                    "\"apa yang salah di aplikasi web ini\". Pemindai kerentanan menjawab",
                    "pertanyaan yang lebih luas: \"dari semua layanan, sistem operasi,",
                    "dan perangkat di jaringan ini, mana yang punya celah yang sudah",
                    "diketahui?\"",
                    "",
                    "Cara kerjanya kurang lebih begini:",
                    "  1. Menemukan host yang hidup dan port yang terbuka, mirip Nmap.",
                    "  2. Mengenali layanan dan versinya dari banner atau jawaban",
                    "     protokol.",
                    "  3. Menjalankan ribuan pemeriksaan kecil. Tiap pemeriksaan",
                    "     mencari satu celah atau satu salah konfigurasi. Nessus",
                    "     menyebutnya plugin, OpenVAS menyebutnya NVT (Network",
                    "     Vulnerability Test).",
                    "  4. Menyusun laporan dengan tingkat keparahan, biasanya dari",
                    "     skor CVSS, plus saran perbaikan.",
                    "",
                    "Pemeriksaan tanpa login (unauthenticated) cuma melihat dari",
                    "luar, jadi banyak menebak dari nomor versi. Pemeriksaan dengan",
                    "login (credentialed scan) masuk ke mesin lewat SSH atau akun",
                    "Windows, lalu membaca daftar paket yang terpasang. Hasilnya",
                    "jauh lebih akurat, dan akun yang dipakai cukup akun baca saja.",
                ],
            },
            {
                "heading": "Nessus",
                "body": [
                    "Nessus buatan Tenable adalah pemindai kerentanan komersial yang",
                    "paling dikenal. Versi terbarunya saat materi ini ditulis adalah",
                    "10.12.5, dirilis 1 Oktober 2026. Edisinya:",
                    "  - Nessus Essentials: gratis untuk penggunaan non-komersial,",
                    "    misalnya pelajar dan jaringan rumah. Menurut halaman resmi",
                    "    Tenable saat materi ini ditulis, batasnya 5 alamat IP.",
                    "  - Nessus Professional dan Nessus Expert: berbayar, untuk",
                    "    konsultan dan tim keamanan.",
                    "",
                    "Untuk skala perusahaan, Tenable menjual platform terpusat yang",
                    "memakai mesin Nessus sebagai pemindainya.",
                ],
            },
            {
                "heading": "OpenVAS dan Greenbone",
                "body": [
                    "OpenVAS adalah pemindai kerentanan open source dari Greenbone.",
                    "Paket lengkapnya kini disebut Greenbone Community Edition,",
                    "terdiri dari beberapa komponen: `openvas-scanner` yang",
                    "menjalankan NVT, `gvmd` yang mengatur tugas dan hasil, dan",
                    "Greenbone Security Assistant sebagai tampilan webnya.",
                    "Komponennya berlisensi GPL dan AGPL. Rilis terbaru",
                    "`openvas-scanner` saat materi ini ditulis v23.52.0, tanggal 16",
                    "Oktober 2026.",
                    "",
                    "Pemeriksaannya datang dari feed. Greenbone Community Feed gratis,",
                    "sedangkan feed berbayar Greenbone untuk perusahaan memuat lebih",
                    "banyak pemeriksaan. Greenbone menyediakan panduan memasang",
                    "Community Edition lewat container, dan itu cara paling mudah",
                    "untuk lab di laptop.",
                ],
            },
            {
                "heading": "Qualys",
                "body": [
                    "Qualys adalah platform keamanan berbasis cloud dan berlisensi",
                    "proprietary. Produk manajemen kerentanannya bernama VMDR",
                    "(Vulnerability Management, Detection and Response). Pemindaian",
                    "dilakukan lewat perangkat pemindai di jaringanmu atau lewat",
                    "agen kecil yang dipasang di tiap mesin, lalu hasilnya dikumpulkan",
                    "di cloud Qualys. Qualys juga punya pemindai aplikasi web.",
                    "",
                    "  alat       lisensi                   cocok untuk",
                    "  Nessus     proprietary, Essentials   konsultan, tim kecil-menengah",
                    "             gratis non-komersial",
                    "  OpenVAS    GPL/AGPL, gratis          lab, organisasi hemat biaya",
                    "  Qualys     proprietary, SaaS         perusahaan dengan ribuan aset",
                ],
            },
            {
                "heading": "Membaca laporan",
                "body": [
                    "Laporan pemindai bisa berisi ratusan baris, dan semuanya nggak",
                    "mungkin diperbaiki hari ini. Yang perlu kamu lakukan adalah",
                    "memilah:",
                    "  - Urutkan menurut keparahan dan paparan. Mesin yang menghadap",
                    "    internet didahulukan.",
                    "  - Beri batas waktu per tingkat, misalnya kritis 7 hari dan",
                    "    tinggi 30 hari. Angkanya kesepakatan organisasi, bukan",
                    "    aturan alat.",
                    "  - Curigai temuan yang cuma berdasar nomor versi. Distro seperti",
                    "    Fedora, Red Hat Enterprise Linux, dan Debian sering menambal",
                    "    celah tanpa mengubah nomor versi utama paketnya (backport).",
                    "    Pemindai tanpa login bisa menganggapnya masih rentan.",
                    "",
                    "Program di bawah mengubah ringkasan laporan jadi daftar kerja",
                    "berbatas tanggal.",
                ],
            },
            {
                "heading": "Daftar kerja dari laporan",
                "code": """from datetime import date, timedelta

TANGGAL_PINDAI = date(2026, 10, 19)
BATAS_HARI = {"Kritis": 7, "Tinggi": 30, "Sedang": 90, "Rendah": 180}

# Ringkasan laporan pemindai di lab sendiri (data tiruan).
# Tanda * = temuan dari nomor versi paket distro, cek backport dulu.
temuan = [
    ("192.168.56.10", "Kritis", "OpenSSH versi lama", True),
    ("192.168.56.10", "Sedang", "sertifikat self-signed", False),
    ("192.168.56.20", "Tinggi", "PostgreSQL versi lama", True),
    ("192.168.56.20", "Rendah", "banner memperlihatkan versi", False),
]

urutan = list(BATAS_HARI)
for ip, tingkat, judul, distro in sorted(temuan, key=lambda t: urutan.index(t[1])):
    batas = TANGGAL_PINDAI + timedelta(days=BATAS_HARI[tingkat])
    tanda = "*" if distro else " "
    print(f"{batas} {tanda} {tingkat:7}{ip:15}{judul}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  2026-10-26 * Kritis 192.168.56.10  OpenSSH versi lama",
                    "  2026-11-18 * Tinggi 192.168.56.20  PostgreSQL versi lama",
                    "  2027-01-17   Sedang 192.168.56.10  sertifikat self-signed",
                    "  2027-04-17   Rendah 192.168.56.20  banner memperlihatkan versi",
                    "",
                    "Tanda bintang bukan berarti temuannya boleh diabaikan. Cek",
                    "dulu dengan perintah paket distro, misalnya `rpm -q --changelog",
                    "openssh-server | grep CVE`. Kalau nomor CVE-nya ada di changelog,",
                    "tandai temuan itu sebagai positif palsu di pemindai, lengkap",
                    "dengan buktinya.",
                    "",
                    "Jebakan: menjalankan pemindaian penuh ke server produksi di jam",
                    "sibuk tanpa memberi tahu siapa pun. Sebagian pemeriksaan bisa",
                    "membuat layanan lama macet. Jadwalkan, beri tahu tim operasi,",
                    "dan mulai dari lingkungan uji.",
                    "",
                    "Ingat: pemindai kerentanan cuma tahu celah yang sudah punya",
                    "pemeriksaan. Celah di aplikasi buatanmu sendiri tetap urusan",
                    "SAST, DAST, dan review kode.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Standar pembayaran kartu PCI DSS mewajibkan pemindaian",
                    "kerentanan internal dan eksternal secara berkala, dan pemindaian",
                    "eksternalnya harus dilakukan vendor pemindai yang disetujui",
                    "(Approved Scanning Vendor). Karena itu laporan Nessus, Qualys,",
                    "atau sejenisnya sering jadi bukti yang diminta auditor, topik",
                    "yang muncul lagi di bab 10.",
                    "",
                    "Kasus kecil: kamu memasang Greenbone Community Edition di",
                    "laptop, lalu memindai dua VM lab. Laporannya berisi 41 temuan,",
                    "dan 12 di antaranya menyebut OpenSSH di VM Fedora \"di bawah",
                    "versi perbaikan\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ulangi pemindaian sebagai credentialed scan dengan akun SSH",
                    "     khusus yang cuma boleh membaca, supaya pemindai melihat",
                    "     paket yang memang terpasang.",
                    "  2. Untuk temuan OpenSSH yang tersisa, cek changelog paketnya:",
                    "       rpm -q --changelog openssh-server | grep CVE-",
                    "  3. Kalau CVE-nya sudah ditambal lewat backport, tandai positif",
                    "     palsu dengan catatan. Kalau belum, jalankan `sudo dnf",
                    "     upgrade openssh-server` di VM itu.",
                    "  4. Pindai ulang, lalu simpan laporan sebelum dan sesudah",
                    "     sebagai bukti perbaikan.",
                ],
            },
        ],
    },
    {
        "title": "33. Log Keamanan dan SIEM: Mendeteksi Serangan",
        "sections": [
            {
                "body": [
                    "Semua pencegahan di bab-bab sebelumnya bisa saja jebol. Kunci",
                    "bocor lewat laptop yang dicuri, atau ada celah baru yang belum",
                    "punya tambalan. Pertanyaannya bergeser dari \"bagaimana mencegah\"",
                    "ke \"seberapa cepat kita tahu\". Jawabannya hampir selalu ada di",
                    "log, catatan kejadian yang ditulis sistem setiap kali sesuatu",
                    "terjadi.",
                    "",
                    "Masalahnya, log tersebar di puluhan tempat dan jumlahnya jutaan",
                    "baris per hari. Nggak ada orang yang sanggup membacanya satu per",
                    "satu. Di situlah SIEM (security information and event",
                    "management) dipakai.",
                ],
            },
            {
                "heading": "Log apa yang perlu dikumpulkan",
                "body": [
                    "Mulai dari log yang menjawab \"siapa melakukan apa, kapan, dari",
                    "mana, dan berhasil atau tidak\":",
                    "  - Log autentikasi: login sukses dan gagal, di server (sshd)",
                    "    maupun di aplikasimu sendiri.",
                    "  - Log akses web: alamat IP, jalur, kode status.",
                    "  - Log audit aplikasi: siapa mengubah hak akses, siapa membuat",
                    "    kunci API, siapa mengekspor data.",
                    "  - Log audit cloud: AWS CloudTrail, Azure Activity Log, dan",
                    "    Google Cloud Audit Logs mencatat setiap panggilan API ke",
                    "    akun cloud.",
                    "  - Log DNS, firewall, dan agen keamanan di laptop atau server.",
                    "",
                    "Tiga syarat supaya log bisa dipakai saat dibutuhkan:",
                    "  1. Jam semua mesin disinkronkan (NTP) dan sebaiknya ditulis",
                    "     dalam UTC. Garis waktu dari tiga log yang jamnya berbeda",
                    "     lima menit bakal menyesatkan.",
                    "  2. Log dikirim ke tempat terpisah yang nggak bisa dihapus oleh",
                    "     akun yang sama dengan server asalnya. Penyerang yang masuk",
                    "     biasanya mencoba menghapus jejak.",
                    "  3. Log disimpan cukup lama. Banyak serangan baru ketahuan",
                    "     berminggu-minggu kemudian.",
                    "",
                    "Jebakan: mencatat terlalu banyak, termasuk password, token, dan",
                    "data pribadi. Log yang bocor jadi kebocoran baru. Bab 05 sudah",
                    "membahas cara menyamarkan nilai sensitif sebelum ditulis.",
                ],
            },
            {
                "heading": "Cara kerja SIEM",
                "body": [
                    "SIEM menjalankan empat pekerjaan berurutan:",
                    "  1. Mengumpulkan log dari semua sumber lewat agen atau API.",
                    "  2. Menormalkan formatnya, supaya \"IP sumber\" dari log nginx",
                    "     dan dari CloudTrail punya nama medan yang sama.",
                    "  3. Mengorelasikan, yaitu menghubungkan kejadian dari sumber",
                    "     yang berbeda. Contohnya enam login gagal lalu satu sukses",
                    "     dari IP yang sama.",
                    "  4. Membuat alert untuk analis, dan menyimpan semuanya supaya",
                    "     bisa dicari saat investigasi.",
                    "",
                    "Produk yang paling sering kamu temui:",
                    "  - Splunk Enterprise Security. Splunk sudah dimiliki Cisco",
                    "    sejak Maret 2024. Bahasa pencariannya bernama SPL.",
                    "  - Microsoft Sentinel, SIEM berbasis cloud di Azure. Pilihan",
                    "    alami untuk organisasi yang sudah memakai Microsoft 365.",
                    "  - Elastic Security, dibangun di atas Elasticsearch. Bisa",
                    "    dipasang sendiri atau dipakai sebagai layanan Elastic Cloud.",
                    "  - Wazuh, platform open source berlisensi GPL-2.0 dengan agen",
                    "    untuk Linux, Windows, dan macOS. Paling realistis untuk lab",
                    "    di laptop karena gratis dan bisa dijalankan di container.",
                ],
            },
            {
                "heading": "Aturan deteksi",
                "body": [
                    "Aturan deteksi adalah kondisi yang kalau terpenuhi memicu alert.",
                    "Supaya aturan bisa dipakai di SIEM mana pun, komunitas membuat",
                    "format Sigma: aturan ditulis sekali dalam YAML, lalu diubah ke",
                    "bahasa kueri tiap produk. Banyak aturan juga diberi label teknik",
                    "dari kerangka ATT&CK, kumpulan taktik dan teknik penyerang. Tebak",
                    "password berulang, misalnya, adalah teknik T1110 (Brute Force).",
                ],
            },
            {
                "heading": "Aturan Sigma sederhana",
                "bahasa": "yaml",
                "code": """title: Login SSH dengan user yang tidak ada
status: experimental
logsource:
  product: linux
  service: auth
detection:
  kata_kunci:
    - 'Failed password for invalid user'
  condition: kata_kunci
level: low
tags:
  - attack.t1110""",
            },
            {
                "body": [
                    "Aturan di atas cuma mencocokkan satu baris. Aturan yang lebih",
                    "berguna biasanya melibatkan hitungan dan jendela waktu, dan itu",
                    "dikerjakan di bagian korelasi SIEM. Program di bawah meniru satu",
                    "aturan korelasi: akun yang login sukses dari tiga IP berbeda",
                    "atau lebih dalam 10 menit. Bisa jadi kredensialnya dipakai orang",
                    "lain.",
                ],
            },
            {
                "heading": "Korelasi mini",
                "code": """# Aturan korelasi: satu akun login sukses dari 3 IP berbeda atau lebih
# dalam 10 menit. Data sudah dinormalisasi: (detik, user, ip).
login = [
    (0, "sari", "192.0.2.15"),
    (120, "budi", "192.0.2.40"),
    (300, "budi", "203.0.113.7"),
    (420, "budi", "198.51.100.9"),
    (900, "sari", "192.0.2.15"),
    (2000, "budi", "192.0.2.40"),
]
JENDELA = 600

for i, (t, user, _) in enumerate(login):
    ip_dalam_jendela = {ip for t2, u2, ip in login[:i + 1]
                        if u2 == user and t - t2 <= JENDELA}
    if len(ip_dalam_jendela) >= 3:
        print(f"ALERT t={t}: {user} login dari {len(ip_dalam_jendela)} IP dalam 10 menit")
        print("  " + ", ".join(sorted(ip_dalam_jendela)))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ALERT t=420: budi login dari 3 IP dalam 10 menit",
                    "    192.0.2.40, 198.51.100.9, 203.0.113.7",
                    "",
                    "Login budi di t=2000 nggak memicu alert lagi karena dua IP",
                    "lainnya sudah lewat dari jendela 10 menit. Alamat-alamat ini",
                    "berasal dari rentang yang disediakan khusus untuk dokumentasi,",
                    "jadi aman dipakai sebagai contoh.",
                    "",
                    "Ingat: aturan yang terlalu sensitif menghasilkan ratusan alert",
                    "palsu sehari, dan analis akan berhenti membacanya. Setiap aturan",
                    "baru perlu disetel: ukur berapa kali ia menyala dalam seminggu,",
                    "lalu periksa berapa yang memang serangan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim SOC (security operations center) di bank, perusahaan",
                    "telekomunikasi, dan penyedia cloud bekerja di depan SIEM",
                    "sepanjang hari. Untuk server pribadi, alat sederhana seperti",
                    "fail2ban sudah menerapkan ide yang sama: membaca log",
                    "autentikasi, menghitung kegagalan per IP, lalu memblokirnya",
                    "lewat firewall.",
                    "",
                    "Kasus kecil: VPS kecilmu menjalankan SSH di port 22. Kamu ingin",
                    "tahu apakah ada yang sedang menebak password, tanpa memasang",
                    "SIEM besar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat log sshd lewat journald:",
                    "       sudo journalctl -u sshd --since \"1 hour ago\"",
                    "  2. Hitung baris \"Failed password\" per IP. Kalau satu IP gagal",
                    "     lebih dari lima kali dalam semenit, itu tebakan otomatis.",
                    "  3. Cari baris \"Accepted\" dari IP yang sama. Kalau ada,",
                    "     anggap akun itu sudah jebol dan mulai respons insiden.",
                    "  4. Pencegahan jangka panjangnya: matikan login password dan",
                    "     pakai kunci SSH (`PasswordAuthentication no`), lalu pasang",
                    "     fail2ban atau kirim log ke Wazuh.",
                ],
            },
        ],
    },
    {
        "title": "34. Respons Insiden, SOAR, dan Postmortem",
        "sections": [
            {
                "body": [
                    "Alert menyala, dan ternyata bukan alarm palsu. Akun budi login",
                    "dari IP asing, membuat kunci API baru, lalu mengekspor data",
                    "pelanggan. Apa yang dilakukan pertama kali?",
                    "",
                    "Respons insiden adalah rangkaian langkah yang sudah disepakati",
                    "sebelumnya untuk menangani kejadian seperti ini. Kata kuncinya",
                    "\"sebelumnya\". Tim yang baru memikirkan siapa yang boleh",
                    "mematikan server di tengah insiden akan kehilangan jam-jam",
                    "paling berharga.",
                ],
            },
            {
                "heading": "Siklus respons insiden",
                "body": [
                    "Panduan yang paling sering dirujuk berasal dari NIST, lembaga",
                    "standar Amerika Serikat. Edisi lamanya, SP 800-61 Revisi 2",
                    "(2012), membagi respons jadi empat fase: persiapan; deteksi dan",
                    "analisis; penahanan, pembersihan, dan pemulihan; serta kegiatan",
                    "sesudah insiden. Pada April 2025 terbit Revisi 3 yang",
                    "menggantikannya. Revisi 3 menyusun ulang rekomendasinya mengikuti",
                    "enam fungsi CSF 2.0 (Govern, Identify, Protect, Detect,",
                    "Respond, Recover), yang dibahas di bab 10.",
                    "",
                    "Di lapangan, banyak tim tetap memakai enam langkah yang mudah",
                    "diingat:",
                    "  1. Persiapan: playbook, daftar kontak, akses darurat, dan log",
                    "     yang memang sudah dikumpulkan.",
                    "  2. Deteksi dan analisis: memastikan ini insiden sungguhan,",
                    "     menilai dampaknya, dan mencatat setiap temuan dengan jamnya.",
                    "  3. Penahanan (containment): menghentikan kerusakan supaya nggak",
                    "     menyebar. Contohnya menonaktifkan akun atau mengisolasi mesin.",
                    "  4. Pembersihan (eradication): membuang penyebabnya, misalnya",
                    "     kunci yang bocor, akun tambahan buatan penyerang, atau",
                    "     celah yang dipakai masuk.",
                    "  5. Pemulihan (recovery): mengembalikan layanan ke keadaan",
                    "     normal sambil diawasi lebih ketat.",
                    "  6. Pelajaran: postmortem dan perbaikan supaya kejadian yang",
                    "     sama nggak terulang.",
                ],
            },
            {
                "heading": "Jaga bukti sebelum membersihkan",
                "body": [
                    "Insting pertama banyak orang adalah langsung memasang ulang",
                    "server yang dibobol. Masalahnya, memasang ulang juga menghapus",
                    "bukti: proses yang berjalan, isi memori, berkas yang ditinggal",
                    "penyerang. Tanpa bukti itu kamu nggak tahu bagaimana penyerang",
                    "masuk, dan pintunya bisa dipakai lagi minggu depan.",
                    "",
                    "Urutan yang lebih aman: tahan dulu (putus dari jaringan, cabut",
                    "kredensial), ambil salinan bukti (snapshot disk, log, daftar",
                    "proses), baru bersihkan. Di cloud, snapshot volume sebelum",
                    "instance dimatikan biasanya cuma butuh satu perintah.",
                    "",
                    "Jebakan: menghubungi penyerang atau \"membalas\" ke IP-nya.",
                    "Selain melanggar hukum, itu memberi tahu penyerang bahwa ia",
                    "sudah ketahuan. Fokus ke sistemmu sendiri.",
                ],
            },
            {
                "heading": "Playbook dan SOAR",
                "body": [
                    "Playbook adalah resep tertulis untuk satu jenis insiden: kunci",
                    "bocor, akun dibajak, ransomware, dan seterusnya. Isinya langkah",
                    "demi langkah, siapa yang mengerjakan, dan siapa yang harus",
                    "dikabari.",
                    "",
                    "SOAR (security orchestration, automation and response)",
                    "menjalankan bagian playbook yang bisa diotomatiskan. Contohnya",
                    "menonaktifkan akun, memblokir IP, atau membuka tiket, begitu",
                    "SIEM menyalakan alert tertentu. Contoh produknya:",
                    "",
                    "  produk                    catatan",
                    "  Splunk SOAR               dulu bernama Phantom",
                    "  Cortex XSOAR              dari Palo Alto Networks",
                    "  playbook Sentinel         dibangun dengan Azure Logic Apps",
                    "  Shuffle                   open source",
                    "  Tines                     otomasi alur kerja keamanan",
                    "",
                    "Program di bawah meniru playbook \"kunci API bocor\" dalam mode",
                    "latihan: semua langkah dicetak, nggak ada yang dijalankan. Mode",
                    "seperti ini dipakai untuk menguji playbook sebelum dipercaya",
                    "menyentuh sistem sungguhan.",
                ],
            },
            {
                "heading": "Playbook mode latihan",
                "code": """# Playbook "kunci API bocor" dalam mode latihan (dry run): setiap langkah
# cuma dicatat, tidak ada yang benar-benar dicabut.
insiden = {"kunci": "kunci-7", "pemilik": "budi", "ip": "203.0.113.7"}

playbook = [
    ("tahan", "nonaktifkan kunci {kunci}"),
    ("tahan", "blokir IP {ip} di WAF"),
    ("tahan", "paksa logout semua sesi {pemilik}"),
    ("bukti", "salin log audit 24 jam terakhir ke penyimpanan read-only"),
    ("bersihkan", "buat kunci baru untuk {pemilik}, simpan di brankas rahasia"),
    ("komunikasi", "kabari pemilik layanan dan catat di tiket insiden"),
]

for nomor, (tahap, langkah) in enumerate(playbook, 1):
    print(f"{nomor}. [{tahap}] {langkah.format(**insiden)}")
print(f"mode latihan: {len(playbook)} langkah dicatat, 0 dijalankan")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  1. [tahan] nonaktifkan kunci kunci-7",
                    "  2. [tahan] blokir IP 203.0.113.7 di WAF",
                    "  3. [tahan] paksa logout semua sesi budi",
                    "  4. [bukti] salin log audit 24 jam terakhir ke penyimpanan read-only",
                    "  5. [bersihkan] buat kunci baru untuk budi, simpan di brankas rahasia",
                    "  6. [komunikasi] kabari pemilik layanan dan catat di tiket insiden",
                    "  mode latihan: 6 langkah dicatat, 0 dijalankan",
                    "",
                    "Kalau insidennya melibatkan data pribadi pelanggan, ada tenggat",
                    "hukum. UU Pelindungan Data Pribadi mewajibkan pemberitahuan",
                    "tertulis paling lambat 3 x 24 jam. Rinciannya di bab 10.",
                ],
            },
            {
                "heading": "Postmortem tanpa menyalahkan",
                "body": [
                    "Sesudah layanan pulih, tim menulis postmortem: laporan tentang",
                    "apa yang terjadi, dampaknya, penyebabnya, dan apa yang akan",
                    "diubah. Buku Site Reliability Engineering dari Google",
                    "mempopulerkan istilah blameless postmortem, yaitu postmortem",
                    "yang mencari penyebab di sistem dan proses, bukan di orang.",
                    "",
                    "Alasannya praktis. Kalau orang yang salah klik dihukum, insiden",
                    "berikutnya akan disembunyikan. Pertanyaan yang lebih berguna",
                    "adalah \"kenapa sistem kita membiarkan satu klik itu berakibat",
                    "sebesar ini?\".",
                    "",
                    "Isi postmortem yang baik:",
                    "  - Ringkasan dua-tiga kalimat dan dampaknya dalam angka.",
                    "  - Garis waktu dalam UTC, dari tanda pertama sampai pulih.",
                    "  - Penyebab utama dan faktor yang memperparah.",
                    "  - Apa yang berjalan baik, misalnya alert yang menyala cepat.",
                    "  - Tindakan perbaikan, masing-masing dengan pemilik dan tenggat.",
                    "",
                    "Ingat: postmortem tanpa tindakan yang dikerjakan cuma dokumen.",
                    "Pantau daftar tindakannya seperti pekerjaan biasa sampai selesai.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak perusahaan teknologi menerbitkan postmortem insiden",
                    "besarnya ke publik, misalnya di blog teknik mereka, lengkap",
                    "dengan garis waktu dan daftar perbaikan. Membaca beberapa di",
                    "antaranya adalah cara cepat belajar bentuk postmortem yang baik.",
                    "",
                    "Kasus kecil: pukul 10.15 UTC, alert menyala. Kunci API milik",
                    "budi dipakai dari IP yang belum pernah terlihat, dan dipakai",
                    "untuk mengunduh laporan pelanggan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tahan: nonaktifkan kunci itu dan paksa logout semua sesi",
                    "     budi. Catat jamnya.",
                    "  2. Bukti: salin log audit dan log akses 24 jam terakhir ke",
                    "     penyimpanan yang nggak bisa diubah.",
                    "  3. Analisis: susun garis waktu dari log web, auth, dan audit",
                    "     dalam UTC. Cari kapan kunci dibuat dan dari mana.",
                    "  4. Bersihkan dan pulihkan: buat kunci baru lewat brankas",
                    "     rahasia, cabut kunci lain yang dibuat di jendela waktu",
                    "     yang sama.",
                    "  5. Kalau data pribadi terungkap, siapkan pemberitahuan dalam",
                    "     3 x 24 jam. Seminggu kemudian, tulis postmortem tanpa",
                    "     menyalahkan, lengkap dengan pemilik tiap tindakan.",
                ],
            },
        ],
    },
    {
        "title": "35. Keamanan Cloud dan Kubernetes: IAM, CSPM, dan Wiz",
        "sections": [
            {
                "body": [
                    "Di cloud, penyedia menjaga gedung, server fisik, dan jaringan",
                    "intinya. Yang kamu jaga adalah konfigurasi: siapa boleh",
                    "mengakses apa, bucket mana yang publik, port mana yang terbuka.",
                    "Pembagian ini disebut shared responsibility model, dan semua",
                    "penyedia besar menuliskannya di dokumentasi mereka.",
                    "",
                    "Akibatnya, kebocoran di cloud paling sering berasal dari salah",
                    "konfigurasi, bukan dari jebolnya pusat data. Praktik IAM di AWS",
                    "dibahas di kurikulum DevOps, materi \"AWS IAM: Siapa Boleh",
                    "Melakukan Apa\". Di sini fokusnya ke kesalahan yang paling sering",
                    "berujung kebocoran, dan cara menemukannya.",
                ],
            },
            {
                "heading": "Salah konfigurasi yang paling sering",
                "body": [
                    "  salah konfigurasi                 perbaikan",
                    "  akun root dipakai sehari-hari     kunci root, pakai MFA",
                    "  access key permanen di laptop     role + kredensial sementara",
                    "  kebijakan Action \"*\"               izin seminimal mungkin",
                    "  bucket penyimpanan publik         Block Public Access",
                    "  SSH/RDP terbuka ke 0.0.0.0/0      akses lewat bastion atau SSM",
                    "  log audit mati                    CloudTrail di semua region",
                    "  metadata instance versi lama      wajibkan IMDSv2",
                    "",
                    "Baris terakhir butuh penjelasan. Setiap mesin virtual di AWS bisa",
                    "bertanya ke alamat khusus (instance metadata service) untuk",
                    "mendapat kredensial role-nya. Versi pertama layanan itu menjawab",
                    "permintaan GET biasa. Kalau aplikasi di mesin itu punya celah",
                    "SSRF, yaitu bisa disuruh mengambil URL pilihan penyerang,",
                    "kredensialnya ikut terambil. IMDSv2 mewajibkan token sesi lebih",
                    "dulu, jadi trik itu jauh lebih sulit.",
                ],
            },
            {
                "heading": "Memeriksa kebijakan IAM",
                "body": [
                    "Kebijakan IAM ditulis dalam JSON. Program di bawah mencari tiga",
                    "tanda bahaya: aksi berupa wildcard, resource `*`, dan aksi yang",
                    "bisa dipakai menaikkan hak sendiri, seperti `iam:PassRole`.",
                ],
            },
            {
                "heading": "Pemeriksa kebijakan",
                "code": "import json\n\nkebijakan = json.loads(\"\"\"\n{\"Version\": \"2012-10-17\", \"Statement\": [\n  {\"Effect\": \"Allow\", \"Action\": \"s3:GetObject\", \"Resource\": \"arn:aws:s3:::foto-produk/*\"},\n  {\"Effect\": \"Allow\", \"Action\": \"s3:*\", \"Resource\": \"*\"},\n  {\"Effect\": \"Allow\", \"Action\": [\"iam:PassRole\", \"ec2:RunInstances\"], \"Resource\": \"*\"}\n]}\n\"\"\")\n\nBERBAHAYA = {\"iam:PassRole\", \"iam:CreateAccessKey\", \"iam:AttachUserPolicy\"}\n\nfor no, st in enumerate(kebijakan[\"Statement\"], 1):\n    if st[\"Effect\"] != \"Allow\":\n        continue\n    aksi = st[\"Action\"] if isinstance(st[\"Action\"], list) else [st[\"Action\"]]\n    masalah = []\n    if any(a == \"*\" or a.endswith(\":*\") for a in aksi):\n        masalah.append(\"aksi wildcard\")\n    if st[\"Resource\"] == \"*\":\n        masalah.append(\"semua resource\")\n    if BERBAHAYA & set(aksi):\n        masalah.append(\"bisa menaikkan hak: \" + \", \".join(sorted(BERBAHAYA & set(aksi))))\n    print(f\"Statement {no}: \" + (\"; \".join(masalah) if masalah else \"OK\"))",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Statement 1: OK",
                    "  Statement 2: aksi wildcard; semua resource",
                    "  Statement 3: semua resource; bisa menaikkan hak: iam:PassRole",
                    "",
                    "`iam:PassRole` bersama `ec2:RunInstances` artinya pemegang",
                    "kebijakan bisa menyalakan mesin dengan role apa pun, termasuk",
                    "role admin, lalu memakai kredensial mesin itu. AWS menyediakan",
                    "IAM Access Analyzer untuk pemeriksaan seperti ini dalam skala",
                    "akun.",
                ],
            },
            {
                "heading": "CSPM, CNAPP, dan Wiz",
                "body": [
                    "Memeriksa satu kebijakan bisa dengan tangan. Memeriksa ribuan",
                    "resource di puluhan akun butuh alat. CSPM (cloud security",
                    "posture management) terus membaca konfigurasi akun cloud lewat",
                    "API dan membandingkannya dengan aturan, mirip Checkov di bab 07.",
                    "Bedanya, ia melihat keadaan yang sedang berjalan, termasuk",
                    "perubahan yang diklik manual di konsol. Payung yang lebih besar",
                    "disebut cloud-native application protection platform: CSPM",
                    "ditambah pemindaian image, beban kerja, dan identitas.",
                    "",
                    "Wiz adalah salah satu platform jenis ini yang paling dikenal. Ia",
                    "bekerja tanpa agen. Cukup beri akses baca ke akun AWS, Azure,",
                    "atau Google Cloud, lalu Wiz memetakan jalur serangan, misalnya",
                    "\"mesin publik ini punya celah dan role-nya boleh membaca bucket",
                    "data pelanggan\". Google menyelesaikan akuisisi Wiz pada 11 Maret",
                    "2026 senilai US$32 miliar, dan Wiz tetap mendukung banyak cloud.",
                    "Survei Stack Overflow 2026 mencatat 5% responden memakainya.",
                    "",
                    "Alternatifnya antara lain layanan bawaan penyedia (AWS Security",
                    "Hub, Microsoft Defender for Cloud) dan alat open source seperti",
                    "Prowler untuk audit akun cloud dari terminal.",
                ],
            },
            {
                "heading": "Kubernetes",
                "body": [
                    "Klaster Kubernetes punya lapisan keamanannya sendiri:",
                    "  - RBAC Kubernetes. Role dan ClusterRole mengatur siapa boleh",
                    "    melakukan apa di klaster. Hindari memberi `cluster-admin`",
                    "    ke akun layanan aplikasi.",
                    "  - Pod Security Standards, tiga tingkat aturan untuk pod:",
                    "    privileged (bebas), baseline (mencegah hak berbahaya yang",
                    "    sudah dikenal), dan restricted (paling ketat). Penegaknya",
                    "    Pod Security Admission, yang dipasang lewat label namespace.",
                    "    PodSecurityPolicy yang lama sudah dihapus sejak Kubernetes",
                    "    1.25.",
                    "  - Secret di Kubernetes cuma di-encode base64, bukan dienkripsi.",
                    "    Nyalakan enkripsi at rest di etcd, atau pakai pendekatan di",
                    "    bab 06.",
                    "  - NetworkPolicy membatasi pod mana boleh bicara dengan pod",
                    "    mana. Tanpa itu, semua pod bisa saling menjangkau.",
                    "  - Admission controller memeriksa manifest sebelum diterima.",
                    "    Gatekeeper dari proyek Open Policy Agent memakai kebijakan Rego",
                    "    (bab 03), dan Kyverno",
                    "    memakai kebijakan berbentuk YAML.",
                    "  - Falco, proyek CNCF, mendeteksi perilaku aneh saat container",
                    "    berjalan, misalnya shell yang tiba-tiba dibuka di dalamnya.",
                ],
            },
            {
                "heading": "Namespace dan pod yang ketat",
                "bahasa": "yaml",
                "code": """apiVersion: v1
kind: Namespace
metadata:
  name: toko
  labels:
    pod-security.kubernetes.io/enforce: restricted
---
apiVersion: v1
kind: Pod
metadata:
  name: web
  namespace: toko
spec:
  containers:
    - name: web
      image: registry.contoh.id/toko-web:1.4.0
      securityContext:
        runAsNonRoot: true
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
        seccompProfile:
          type: RuntimeDefault""",
            },
            {
                "heading": "Kebijakan Gatekeeper dalam Rego",
                "bahasa": "rego",
                "code": """package k8spolos

violation contains {"msg": msg} if {
    some c in input.review.object.spec.containers
    c.securityContext.privileged
    msg := sprintf("container %v tidak boleh privileged", [c.name])
}""",
            },
            {
                "body": [
                    "Jebakan: menyalakan semua aturan ketat sekaligus di klaster yang",
                    "sudah berjalan. Pod lama yang melanggar akan gagal dibuat ulang.",
                    "Pod Security Admission punya mode `warn` dan `audit` untuk",
                    "melihat dulu apa saja yang akan ditolak sebelum `enforce`.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tahun 2019, Capital One mengumumkan kebocoran data yang menurut",
                    "pengumuman resminya menyangkut sekitar 100 juta orang di Amerika",
                    "Serikat dan 6 juta di Kanada. Menurut dokumen pengadilan dan",
                    "banyak analisis sesudahnya, penyerang memanfaatkan firewall",
                    "aplikasi web yang salah konfigurasi untuk melakukan SSRF ke",
                    "layanan metadata, mengambil kredensial role, lalu membaca isi",
                    "bucket S3. Kasus ini sering dipakai sebagai alasan mewajibkan",
                    "IMDSv2.",
                    "",
                    "Kasus kecil: kamu diminta mengaudit akun AWS tim yang kecil.",
                    "Belum ada alat CSPM berbayar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan akun root punya MFA dan nggak punya access key.",
                    "  2. Jalankan pemeriksaan open source dengan akses baca saja:",
                    "       prowler aws",
                    "  3. Urutkan temuan: bucket publik, security group 0.0.0.0/0",
                    "     ke port admin, dan kebijakan dengan Action \"*\" dulu.",
                    "  4. Wajibkan IMDSv2 di semua instance (`HttpTokens=required`),",
                    "     lalu nyalakan CloudTrail untuk semua region.",
                    "  5. Ulangi pemeriksaan tiap bulan, atau pasang di pipeline",
                    "     terjadwal supaya hasilnya bisa dibandingkan.",
                ],
            },
        ],
    },
    {
        "title": "36. Peta Vendor Keamanan Perusahaan: EDR, PAM, Firewall",
        "sections": [
            {
                "body": [
                    "Begitu kamu masuk ke perusahaan menengah atau besar, kamu akan",
                    "mendengar nama produk keamanan di rapat, di dokumen arsitektur,",
                    "dan di lowongan kerja. Materi ini peta: apa kategori produknya,",
                    "masalah apa yang dipecahkan, dan siapa vendor utamanya. Kamu",
                    "nggak perlu bisa mengoperasikan semuanya. Cukup tahu tempatnya.",
                    "",
                    "Angka pemakaian di bawah berasal dari Survei Stack Overflow 2026,",
                    "kategori alat operasi keamanan. Respondennya developer, jadi",
                    "angkanya menggambarkan apa yang dilihat developer, belum tentu",
                    "pangsa pasar.",
                ],
            },
            {
                "heading": "Kategori dan vendornya",
                "body": [
                    "  kategori       untuk apa                      contoh vendor",
                    "  EDR / XDR      deteksi serangan di laptop     CrowdStrike Falcon (12%),",
                    "                 dan server                     SentinelOne (6%)",
                    "  PAM            mengamankan akun admin         CyberArk (6%),",
                    "                                                BeyondTrust (5%)",
                    "  NGFW           firewall, VPN, SD-WAN          Fortinet (9%)",
                    "  SIEM           log dan deteksi                Splunk",
                    "  AppSec         SAST, SCA, keamanan API        Checkmarx (5%),",
                    "                                                pemilik ZAP dan KICS",
                    "  CNAPP          keamanan akun cloud            Wiz (5%)",
                    "",
                    "Endpoint detection and response (EDR) adalah agen di setiap",
                    "laptop dan server yang merekam perilaku proses, mendeteksi pola",
                    "serangan, dan bisa mengisolasi mesin dari jaringan dengan satu",
                    "klik. XDR memperluasnya ke sumber lain seperti email dan cloud.",
                    "CrowdStrike Falcon dan SentinelOne adalah dua nama terbesar di",
                    "sini, dan Microsoft Defender for Endpoint juga banyak dipakai",
                    "di organisasi pengguna Windows.",
                    "",
                    "Privileged access management (PAM) menyimpan password akun",
                    "admin di brankas, meminjamkannya sementara, dan merekam sesi",
                    "admin. CyberArk adalah pemimpin lama di kategori ini. Palo Alto",
                    "Networks mengumumkan akuisisinya pada Juli 2025. Saat materi ini",
                    "ditulis, halaman pers CyberArk sudah dialihkan ke situs Palo",
                    "Alto Networks, dan platformnya dipasarkan dengan nama Idira.",
                    "BeyondTrust bermain di kategori yang sama, ditambah akses",
                    "jarak jauh untuk tim dukungan.",
                    "",
                    "NGFW (next-generation firewall) memeriksa lalu lintas sampai ke",
                    "tingkat aplikasi, nggak berhenti di nomor port. Fortinet dengan",
                    "FortiGate, Palo Alto Networks, dan Cisco adalah pemain besarnya.",
                    "",
                    "Checkmarx menjual platform keamanan aplikasi untuk perusahaan,",
                    "dan sekarang juga memegang dua alat open source yang sudah kamu",
                    "kenal dari bab 07 dan bab 08 (lihat tabel). Splunk muncul lagi di",
                    "sini karena SIEM-nya (materi pertama bab ini) termasuk produk",
                    "keamanan perusahaan yang paling luas dipakai.",
                ],
            },
            {
                "heading": "Perangkat di tepi jaringan",
                "body": [
                    "Firewall dan gerbang VPN berdiri di tepi jaringan, menghadap",
                    "internet, jadi celahnya diburu penyerang. Celah VPN SSL FortiOS",
                    "CVE-2018-13379, misalnya, masuk daftar celah yang terbukti",
                    "dieksploitasi milik badan keamanan siber Amerika Serikat. Celah",
                    "itu bertahun-tahun dipakai untuk mencuri kredensial VPN dari",
                    "perangkat yang nggak ditambal.",
                    "Pelajarannya berlaku untuk semua vendor: perangkat keamanan juga",
                    "perangkat lunak, dan harus ikut jadwal patch yang paling cepat.",
                ],
            },
            {
                "heading": "Studi kasus: 19 Juli 2024",
                "body": [
                    "Pada 19 Juli 2024 pukul 04.09 UTC, CrowdStrike mengirim",
                    "pembaruan konfigurasi untuk sensor Falcon di Windows, yang",
                    "mereka sebut Channel File 291. Pembaruan itu memicu galat logika",
                    "yang membuat Windows crash dengan layar biru, pada sensor versi",
                    "7.11 ke atas. Menurut penjelasan teknis CrowdStrike, perbaikannya",
                    "dikirim pukul 05.27 UTC, sekitar 78 menit kemudian. Linux dan",
                    "macOS nggak terdampak.",
                    "",
                    "Masalahnya, komputer yang sudah crash nggak bisa menerima",
                    "perbaikan otomatis. Microsoft memperkirakan sekitar 8,5 juta",
                    "perangkat Windows terdampak. Banyak di antaranya harus",
                    "dipulihkan dengan tangan: masuk safe mode, hapus berkas yang",
                    "rusak, dan untuk laptop terenkripsi BitLocker, masukkan kunci",
                    "pemulihannya satu per satu. Maskapai, rumah sakit, dan bank di",
                    "banyak negara terganggu selama berhari-hari.",
                    "",
                    "Pelajaran untuk keamanan dan rilis perangkat lunak:",
                    "  - Produk keamanan berjalan dengan hak tertinggi di sistem,",
                    "    jadi kesalahannya juga berdampak paling besar.",
                    "  - Pembaruan, sekecil apa pun, dikirim bertahap: cincin",
                    "    internal dulu, lalu sebagian kecil pelanggan (canary), baru",
                    "    semuanya. Laporan tinjauan pasca-insiden CrowdStrike sendiri",
                    "    menjanjikan rilis bertahap untuk pembaruan kontennya.",
                    "  - Rencana pemulihan perlu diuji, termasuk di mana kunci",
                    "    pemulihan disimpan kalau semua laptop mati bersamaan.",
                    "",
                    "Program di bawah meniru rilis bertahap dengan angka karangan.",
                    "Pembaruan yang buruk berhenti di cincin kecil.",
                ],
            },
            {
                "heading": "Rilis bertahap",
                "code": """# Rilis bertahap: pembaruan dikirim ke cincin kecil dulu, dan berhenti
# kalau angka crash di cincin itu melewati batas.
cincin = [("internal", 50), ("canary 1%", 1_000), ("10%", 10_000), ("semua", 100_000)]
crash = {"internal": 0, "canary 1%": 870, "10%": 9_100, "semua": 92_000}
BATAS = 0.01   # berhenti kalau lebih dari 1% perangkat crash

terkena = 0
for nama, jumlah in cincin:
    terkena += jumlah
    rasio = crash[nama] / jumlah
    print(f"{nama:10} {jumlah:>7} perangkat, crash {rasio:.1%}")
    if rasio > BATAS:
        print(f"BERHENTI di {nama}, rollback. Total perangkat terkena: {terkena}")
        break""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  internal        50 perangkat, crash 0.0%",
                    "  canary 1%     1000 perangkat, crash 87.0%",
                    "  BERHENTI di canary 1%, rollback. Total perangkat terkena: 1050",
                    "",
                    "Kenapa cincin internal lolos? Di contoh ini mesin internal",
                    "kebetulan nggak memicu galatnya. Karena itu cincin canary harus",
                    "berisi perangkat yang beragam, jangan mesin tim sendiri saja.",
                    "",
                    "Jebakan: memilih vendor dari daftar fitur saja. Tanyakan juga",
                    "bagaimana mereka merilis pembaruan, apakah pelanggan bisa",
                    "mengatur penundaan, dan apa rencana pemulihannya kalau",
                    "pembaruan mereka sendiri yang bermasalah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan analis SOC di Indonesia sering mencantumkan pengalaman",
                    "dengan SIEM (Splunk, Sentinel, atau Wazuh) dan agen endpoint",
                    "(CrowdStrike atau SentinelOne). Sebagian vendor menyediakan pelatihan dan",
                    "sertifikasi dasar gratis, dan Wazuh bisa dipasang sendiri untuk",
                    "latihan.",
                    "",
                    "Kasus kecil: kantor tempatmu PKL memakai satu produk endpoint. Kepala",
                    "IT bertanya apa yang perlu disiapkan supaya kejadian seperti 19",
                    "Juli 2024 nggak melumpuhkan kantor.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek apakah konsol produk itu mengizinkan kebijakan pembaruan",
                    "     bertahap, misalnya sebagian kecil laptop menerima versi baru",
                    "     lebih dulu.",
                    "  2. Bagi perangkat jadi cincin: laptop tim IT, lalu satu",
                    "     divisi kecil, lalu semuanya.",
                    "  3. Simpan kunci pemulihan BitLocker di tempat yang bisa",
                    "     diakses walaupun laptop admin ikut mati, misalnya di akun",
                    "     identitas cloud dan salinan cetak di brankas.",
                    "  4. Tulis langkah pemulihan manual satu halaman dan uji di",
                    "     satu laptop cadangan.",
                ],
            },
        ],
    },
    {
        "title": "37. Kepatuhan: ISO 27001, SOC 2, NIST CSF, dan UU PDP",
        "sections": [
            {
                "body": [
                    "Sampai bab ini kamu belajar mengamankan sistem dari sisi teknis.",
                    "Di perusahaan, ada satu pertanyaan lagi yang selalu datang:",
                    "\"buktinya mana?\". Pelanggan besar, bank, dan regulator nggak",
                    "cukup diberi janji bahwa sistemmu aman. Mereka minta bukti yang",
                    "bisa diperiksa pihak ketiga.",
                    "",
                    "Kepatuhan (compliance) adalah pekerjaan memenuhi standar atau",
                    "aturan tertentu, lalu membuktikannya ke auditor. Standar memberi",
                    "daftar kontrol, yaitu langkah pengamanan yang harus ada. Auditor",
                    "memeriksa apakah kontrol itu memang ada dan memang dijalankan.",
                    "",
                    "Kepatuhan nggak sama dengan aman. Organisasi yang lulus audit",
                    "tetap bisa dibobol. Tapi standar yang baik memaksa hal-hal dasar",
                    "dikerjakan dengan rutin: daftar aset, hak akses ditinjau, backup",
                    "diuji, insiden punya prosedur.",
                ],
            },
            {
                "heading": "ISO/IEC 27001:2022",
                "body": [
                    "ISO 27001 adalah standar internasional untuk sistem manajemen",
                    "keamanan informasi (information security management system).",
                    "Isinya dua bagian. Bagian",
                    "utama (klausul 4 sampai 10) meminta organisasi menetapkan",
                    "cakupan, menilai risiko, memilih kontrol, mengukur, dan terus",
                    "memperbaiki. Lampiran A berisi 93 kontrol yang dikelompokkan",
                    "jadi empat tema: organisasi (37), orang (8), fisik (14), dan",
                    "teknologi (34).",
                    "",
                    "Edisi yang berlaku adalah 2022. Sertifikat edisi 2013 sudah",
                    "harus beralih paling lambat 31 Oktober 2025. Sertifikat",
                    "dikeluarkan lembaga sertifikasi yang terakreditasi, berlaku tiga",
                    "tahun, dengan audit pengawasan setiap tahun. Dokumen standarnya",
                    "sendiri berbayar.",
                    "",
                    "Contoh kontrol di Lampiran A yang berhubungan dengan bab-bab",
                    "sebelumnya: 5.15 kontrol akses (bab 03), 8.8 manajemen",
                    "kerentanan teknis (bab 07 dan 08), 8.15 logging (bab 09), dan",
                    "8.24 penggunaan kriptografi (bab 02).",
                ],
            },
            {
                "heading": "SOC 2",
                "body": [
                    "SOC 2 adalah kerangka audit dari AICPA, asosiasi akuntan publik",
                    "Amerika Serikat. Biasanya diminta pelanggan perusahaan dari",
                    "penyedia SaaS. Hasilnya berupa laporan dari kantor akuntan",
                    "publik, bukan sertifikat.",
                    "",
                    "Laporannya menilai kontrol berdasarkan Trust Services Criteria:",
                    "keamanan (selalu wajib), ketersediaan, integritas pemrosesan,",
                    "kerahasiaan, dan privasi. Ada dua jenis:",
                    "  - Type I: apakah kontrolnya dirancang dengan benar, dinilai",
                    "    pada satu tanggal.",
                    "  - Type II: apakah kontrolnya memang berjalan selama satu",
                    "    periode, biasanya beberapa bulan sampai setahun. Pelanggan",
                    "    besar umumnya meminta yang ini.",
                ],
            },
            {
                "heading": "NIST CSF 2.0 dan PCI DSS",
                "body": [
                    "NIST Cybersecurity Framework 2.0 terbit 26 Februari 2024, gratis,",
                    "dan ditujukan untuk organisasi apa pun. Isinya enam fungsi:",
                    "  - Govern: strategi, peran, dan kebijakan keamanan. Fungsi ini",
                    "    baru di versi 2.0.",
                    "  - Identify: tahu aset dan risikonya.",
                    "  - Protect: kontrol pencegahan.",
                    "  - Detect: menemukan serangan.",
                    "  - Respond: menangani insiden.",
                    "  - Recover: memulihkan layanan.",
                    "",
                    "CSF bukan sesuatu yang disertifikasi. Ia dipakai untuk memotret",
                    "keadaan sekarang, menetapkan target, lalu menyusun rencana.",
                    "",
                    "PCI DSS adalah standar keamanan untuk siapa pun yang menyimpan,",
                    "memproses, atau mengirim data kartu pembayaran. Versi yang",
                    "berlaku saat materi ini ditulis adalah 4.0.1 (Juni 2024), dan",
                    "persyaratan yang sempat ditunda di versi 4.0 wajib dipenuhi",
                    "sejak 31 Maret 2025. Cara paling umum mengurangi beban PCI DSS",
                    "adalah nggak menyimpan nomor kartu sama sekali, misalnya memakai",
                    "halaman pembayaran milik payment gateway.",
                ],
            },
            {
                "heading": "UU Pelindungan Data Pribadi",
                "body": [
                    "Di Indonesia, aturan yang paling penting untuk developer adalah",
                    "UU Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU",
                    "PDP), disahkan 17 Oktober 2022. Pasal 74 memberi waktu dua tahun",
                    "untuk menyesuaikan diri, jadi sejak Oktober 2024 semua pihak",
                    "yang memproses data pribadi wajib mematuhinya.",
                    "",
                    "Hal yang paling sering menyentuh pekerjaan developer, dibaca",
                    "dari teks undang-undangnya:",
                    "  - Pasal 4: data pribadi dibagi dua. Yang bersifat spesifik:",
                    "    kesehatan, biometrik, genetika, catatan kejahatan, data anak,",
                    "    dan keuangan pribadi. Yang bersifat umum: nama lengkap, jenis",
                    "    kelamin, kewarganegaraan, agama, status perkawinan, dan data",
                    "    yang dikombinasikan untuk mengenali seseorang.",
                    "  - Pasal 20: pemrosesan wajib punya dasar, misalnya persetujuan",
                    "    eksplisit, perjanjian, kewajiban hukum, atau kepentingan yang",
                    "    sah.",
                    "  - Pasal 46: kalau terjadi kegagalan pelindungan data pribadi,",
                    "    pengendali data wajib memberi tahu subjek data dan lembaga",
                    "    pengawas secara tertulis paling lambat 3 x 24 jam.",
                    "  - Pasal 53: organisasi tertentu, misalnya yang memproses data",
                    "    spesifik dalam skala besar, wajib menunjuk pejabat pelindungan",
                    "    data pribadi.",
                    "  - Pasal 57: sanksi administratif, termasuk denda paling tinggi",
                    "    2% dari pendapatan tahunan.",
                    "  - Pasal 67: pidana untuk orang yang dengan sengaja dan melawan",
                    "    hukum memperoleh, mengungkapkan, atau menggunakan data",
                    "    pribadi milik orang lain, sampai 5 tahun penjara dan/atau",
                    "    denda Rp5 miliar.",
                    "",
                    "Lembaga pengawas yang disebut di pasal-pasal itu ditetapkan oleh",
                    "Presiden (Pasal 58). Ketentuan pelaksananya diatur lewat",
                    "peraturan pemerintah, jadi cek peraturan terbaru di situs resmi",
                    "seperti peraturan.bpk.go.id sebelum menyusun prosedur di tempat",
                    "kerja.",
                ],
            },
            {
                "heading": "Bukti untuk auditor",
                "body": [
                    "Pekerjaan kepatuhan sehari-hari banyak berupa mengumpulkan",
                    "bukti: tangkapan layar konfigurasi, laporan pemindaian, catatan",
                    "tinjauan hak akses, hasil uji pemulihan backup. Bukti yang",
                    "terlalu tua dianggap nggak menggambarkan keadaan sekarang.",
                    "Program di bawah memeriksa umur bukti beberapa kontrol menjelang",
                    "audit.",
                ],
            },
            {
                "heading": "Celah bukti menjelang audit",
                "code": """from datetime import date

TANGGAL_AUDIT = date(2026, 11, 1)
MAKS_UMUR_HARI = 365   # bukti lebih tua dari setahun dianggap basi

# Kontrol Annex A ISO/IEC 27001:2022 dan tanggal bukti terakhir.
kontrol = [
    ("5.15", "Kontrol akses", date(2026, 9, 30)),
    ("5.24", "Perencanaan manajemen insiden", date(2025, 6, 12)),
    ("8.8", "Manajemen kerentanan teknis", date(2026, 10, 20)),
    ("8.13", "Cadangan informasi", None),
    ("8.15", "Logging", date(2026, 8, 3)),
]

celah = 0
for nomor, nama, bukti in kontrol:
    if bukti is None:
        status = "TIDAK ADA BUKTI"
        celah += 1
    elif (TANGGAL_AUDIT - bukti).days > MAKS_UMUR_HARI:
        status = f"BASI ({(TANGGAL_AUDIT - bukti).days} hari)"
        celah += 1
    else:
        status = "siap"
    print(f"A.{nomor:5} {nama:31} {status}")
print(f"{celah} dari {len(kontrol)} kontrol perlu dibereskan sebelum audit")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  A.5.15  Kontrol akses                   siap",
                    "  A.5.24  Perencanaan manajemen insiden   BASI (507 hari)",
                    "  A.8.8   Manajemen kerentanan teknis     siap",
                    "  A.8.13  Cadangan informasi              TIDAK ADA BUKTI",
                    "  A.8.15  Logging                         siap",
                    "  2 dari 5 kontrol perlu dibereskan sebelum audit",
                    "",
                    "Banyak tim memakai platform otomasi kepatuhan yang menarik bukti",
                    "langsung dari akun cloud dan repo. Prinsipnya sama dengan",
                    "program kecil ini: daftar kontrol, bukti, dan umurnya.",
                    "",
                    "Jebakan: menulis kebijakan yang bagus di dokumen tapi nggak",
                    "pernah dijalankan. Auditor Type II meminta contoh dari periode",
                    "audit, misalnya tiket tinjauan akses bulan Maret, dan kebijakan",
                    "tanpa jejak pelaksanaan akan ketahuan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Penyedia cloud besar menerbitkan laporan SOC 2 dan sertifikat",
                    "ISO 27001 mereka di halaman kepatuhan (misalnya AWS Artifact),",
                    "karena pelanggan perusahaan memintanya sebelum menandatangani",
                    "kontrak. Startup SaaS di Indonesia yang menjual ke bank juga",
                    "sering diminta ISO 27001 sebagai syarat tender.",
                    "",
                    "Kasus kecil: aplikasi toko online tempatmu PKL menyimpan nama,",
                    "alamat, nomor HP, dan riwayat belanja. Atasanmu bertanya apa",
                    "yang harus disiapkan supaya sesuai UU PDP.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat daftar data pribadi yang disimpan, di tabel mana, dan",
                    "     untuk tujuan apa. Tandai yang termasuk data spesifik.",
                    "  2. Tulis dasar pemrosesannya per tujuan, misalnya perjanjian",
                    "     untuk pengiriman barang dan persetujuan untuk promosi.",
                    "  3. Siapkan prosedur insiden yang memuat tenggat pemberitahuan",
                    "     3 x 24 jam: siapa yang memutuskan, siapa yang menulis, dan",
                    "     templat isinya (data apa yang terungkap, kapan, dan upaya",
                    "     penanganannya).",
                    "  4. Tetapkan masa simpan tiap jenis data dan cara menghapusnya.",
                    "     Materi berikutnya membahas ini lebih rinci.",
                ],
            },
        ],
    },
    {
        "title": "38. Privasi Data: Klasifikasi, Retensi, dan Minimalisasi",
        "sections": [
            {
                "body": [
                    "Cara paling ampuh melindungi data adalah nggak menyimpannya.",
                    "Data yang nggak ada nggak bisa bocor, nggak perlu dienkripsi,",
                    "dan nggak perlu dihapus saat pelanggan memintanya.",
                    "",
                    "Materi ini membahas kebiasaan kecil yang membuat aplikasimu",
                    "menyimpan data pribadi seperlunya saja: memberi kelas pada",
                    "data, mengumpulkan secukupnya, menyamarkan saat ditampilkan,",
                    "dan menghapus saat masa simpannya habis. Prinsip ini juga",
                    "tertulis di Pasal 16 UU PDP: pemrosesan dilakukan secara",
                    "terbatas dan spesifik, sesuai tujuannya.",
                ],
            },
            {
                "heading": "Klasifikasi data",
                "body": [
                    "Klasifikasi artinya memberi label pada data menurut akibatnya",
                    "kalau bocor. Label itu yang menentukan perlakuannya. Contoh",
                    "skema empat kelas yang banyak dipakai:",
                    "",
                    "  kelas        contoh                        perlakuan",
                    "  publik       harga produk, artikel blog    bebas dibaca",
                    "  internal     notulen rapat, SOP            butuh login kantor",
                    "  rahasia      email, nomor HP, NIK, alamat  enkripsi, disamarkan",
                    "  spesifik     data kesehatan, data anak     akses paling sempit",
                    "",
                    "Kelas spesifik di tabel ini mengikuti daftar data pribadi",
                    "spesifik di Pasal 4 UU PDP. NIK nggak masuk daftar itu, tapi ia",
                    "kunci yang menghubungkan banyak data lain tentang seseorang,",
                    "jadi wajar diperlakukan sebagai rahasia.",
                    "",
                    "Yang penting, label itu dipakai di kode dan infrastruktur. Kolom",
                    "berkelas rahasia ditandai di skema database, ikut disamarkan di",
                    "log, dan nggak boleh disalin ke lingkungan staging apa adanya.",
                ],
            },
            {
                "heading": "Minimalisasi",
                "body": [
                    "Minimalisasi data artinya cuma mengumpulkan yang memang dipakai",
                    "untuk tujuan yang sudah disebut. Beberapa pertanyaan yang bisa",
                    "kamu ajukan ke setiap kolom di formulir:",
                    "  - Kolom ini dipakai untuk apa? Kalau jawabannya \"siapa tahu",
                    "    nanti perlu\", buang.",
                    "  - Butuh tanggal lahir lengkap, atau cukup tahu sudah 17",
                    "    tahun?",
                    "  - Butuh salinan foto KTP, atau cukup hasil verifikasinya?",
                    "  - Butuh alamat lengkap untuk akun yang cuma membeli produk",
                    "    digital?",
                    "",
                    "Hal yang sama berlaku untuk log dan analitik. Alamat IP lengkap,",
                    "nomor HP di URL, dan isi formulir di log debug adalah data",
                    "pribadi juga.",
                ],
            },
            {
                "heading": "Menyamarkan, pseudonim, dan anonim",
                "body": [
                    "Tiga istilah ini sering tertukar:",
                    "  - Penyamaran (masking): sebagian nilai ditutup saat",
                    "    ditampilkan, misalnya a***@contoh.id. Data aslinya tetap",
                    "    tersimpan.",
                    "  - Pseudonimisasi: identitas diganti kode, dan tabel pemetaan",
                    "    kode ke orang disimpan terpisah. Orang yang memegang tabel",
                    "    itu masih bisa mengembalikannya, jadi hukum tetap",
                    "    menganggapnya data pribadi.",
                    "  - Anonimisasi: data diubah sampai orangnya nggak bisa dikenali",
                    "    lagi, bahkan dengan menggabungkan data lain. Ini jauh lebih",
                    "    sulit dari kelihatannya.",
                    "",
                    "Jebakan: menganggap hash SHA-256 dari email sebagai data anonim.",
                    "Siapa pun yang punya daftar email bisa menghitung hash yang sama",
                    "lalu mencocokkannya. Hash seperti itu paling jauh pseudonim.",
                    "",
                    "Program di bawah memperlihatkan penyamaran untuk tampilan dan",
                    "pemeriksaan masa simpan.",
                ],
            },
            {
                "heading": "Penyamaran dan retensi",
                "code": "import re\nfrom datetime import date\n\ndef samarkan_email(email):\n    nama, domain = email.split(\"@\")\n    return nama[0] + \"***@\" + domain\n\ndef samarkan_hp(nomor):\n    angka = re.sub(r\"\\D\", \"\", nomor)\n    return angka[:4] + \"*\" * (len(angka) - 7) + angka[-3:]\n\ndef samarkan_nik(nik):\n    return \"*\" * 12 + nik[-4:]\n\npelanggan = {\"nama\": \"Ani Lestari\", \"email\": \"ani.lestari@contoh.id\",\n             \"hp\": \"0812-3456-7890\", \"nik\": \"3174012345678901\"}\nprint(samarkan_email(pelanggan[\"email\"]))\nprint(samarkan_hp(pelanggan[\"hp\"]))\nprint(samarkan_nik(pelanggan[\"nik\"]))\n\n# Retensi: data yang lewat masa simpannya dihapus.\nHARI_INI = date(2026, 10, 19)\nRETENSI_HARI = {\"log_akses\": 90, \"keranjang_ditinggal\": 30, \"faktur\": 3650}\ndata = [(\"log_akses\", date(2026, 6, 1)), (\"keranjang_ditinggal\", date(2026, 10, 1)),\n        (\"faktur\", date(2020, 1, 15))]\nfor jenis, dibuat in data:\n    umur = (HARI_INI - dibuat).days\n    tindakan = \"hapus\" if umur > RETENSI_HARI[jenis] else \"simpan\"\n    print(f\"{jenis:20} umur {umur:4} hari -> {tindakan}\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "  a***@contoh.id",
                    "  0812*****890",
                    "  ************8901",
                    "  log_akses            umur  140 hari -> hapus",
                    "  keranjang_ditinggal  umur   18 hari -> simpan",
                    "  faktur               umur 2469 hari -> simpan",
                    "",
                    "Faktur disimpan lama karena ada kewajiban hukum lain, yaitu",
                    "aturan perpajakan yang meminta dokumen pembukuan disimpan",
                    "sepuluh tahun. Masa simpan selalu ditentukan per jenis data,",
                    "dengan alasan yang tertulis.",
                ],
            },
            {
                "heading": "Retensi dan hak subjek data",
                "body": [
                    "Retensi adalah berapa lama data disimpan. UU PDP Pasal 43",
                    "mewajibkan pengendali menghapus data pribadi kalau sudah nggak",
                    "diperlukan untuk tujuannya, kalau persetujuannya ditarik, atau",
                    "kalau pemiliknya meminta. Pasal 44 mengatur pemusnahan, misalnya",
                    "saat masa retensinya habis. Di kode, ini biasanya berupa tugas",
                    "terjadwal yang menghapus baris yang lewat masa simpan, termasuk",
                    "di backup dan salinan analitik.",
                    "",
                    "Undang-undang yang sama memberi subjek data, yaitu orang yang",
                    "datanya diproses, sejumlah hak. Beberapa di antaranya:",
                    "  - mengakses dan mendapat salinan datanya (Pasal 7),",
                    "  - memperbaiki data yang salah (Pasal 6),",
                    "  - meminta penghapusan (Pasal 8),",
                    "  - menarik persetujuan (Pasal 9),",
                    "  - mengajukan keberatan atas keputusan yang sepenuhnya",
                    "    otomatis (Pasal 10).",
                    "",
                    "Aplikasi yang dirancang dengan baik punya tombol atau prosedur",
                    "untuk semua itu. Alamat email yang nggak pernah dibalas nggak",
                    "masuk hitungan.",
                    "",
                    "Ingat: menghapus akun pengguna harus juga menghapus atau",
                    "menganonimkan datanya di tabel lain, log, dan sistem pihak",
                    "ketiga yang pernah menerima salinannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi besar menyediakan fitur unduh data dan hapus",
                    "akun di halaman pengaturan, sebagian karena aturan seperti GDPR",
                    "di Eropa dan UU PDP di Indonesia. Kebocoran data yang ramai",
                    "diberitakan sering melibatkan data yang sudah nggak",
                    "dipakai lagi tapi nggak pernah dihapus.",
                    "",
                    "Kasus kecil: tabel `pengguna` aplikasimu punya kolom",
                    "`foto_ktp`, `tanggal_lahir`, dan `nik`. Fiturnya cuma butuh",
                    "memastikan pembeli sudah 17 tahun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ganti tiga kolom itu dengan satu kolom hasil verifikasi:",
                    "       sudah_17 BOOLEAN, diverifikasi_pada DATE",
                    "  2. Untuk data lama, isi kolom baru dari tanggal lahir yang ada,",
                    "     lalu hapus kolom foto_ktp dan nik setelah backup terenkripsi",
                    "     yang diperlukan audit dibuat dan diberi masa simpan.",
                    "  3. Pastikan log dan layanan pihak ketiga nggak lagi menerima",
                    "     NIK, dan samarkan NIK lama di log yang masih disimpan.",
                    "  4. Catat perubahan itu di daftar pemrosesan data pribadi, lengkap",
                    "     dengan alasan dan tanggal.",
                ],
            },
        ],
    },
]
