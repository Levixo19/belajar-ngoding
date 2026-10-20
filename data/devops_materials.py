"""Kurikulum DevOps & Cloud.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

DEVOPS_BAB = [
    {
        "judul": "Fondasi DevOps: Linux, SSH, dan YAML",
        "ket": "Cara kerja DevOps dan bekal server yang dipakai di semua bab berikutnya.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Jaringan dan Web Server",
        "ket": "Port, DNS, HTTPS, dan Nginx sebagai pintu depan aplikasi.",
        "tingkat": "dasar",
        "jumlah": 5,
    },
    {
        "judul": "Container dengan Docker",
        "ket": "Membungkus aplikasi jadi image dan menjalankannya sebagai container.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Compose, Podman, dan Registry",
        "ket": "Banyak container sekaligus, container tanpa root, dan tempat menyimpan image.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "CI/CD dengan GitHub Actions",
        "ket": "Pipeline otomatis dari commit sampai deploy.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "Cloud dan Layanan Inti AWS",
        "ket": "Konsep cloud dan layanan AWS yang dipakai hampir semua aplikasi.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "Serverless, Edge, dan PaaS",
        "ket": "Menjalankan kode tanpa mengurus server.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Infrastructure as Code",
        "ket": "Menulis infrastruktur dan konfigurasi server sebagai kode dengan Terraform dan Ansible.",
        "tingkat": "menengah",
        "jumlah": 6,
    },
    {
        "judul": "Kubernetes",
        "ket": "Orkestrasi container lewat keadaan yang diinginkan.",
        "tingkat": "mahir",
        "jumlah": 5,
    },
    {
        "judul": "Helm dan GitOps",
        "ket": "Mengemas aplikasi Kubernetes dan men-deploy lewat Git.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Observability",
        "ket": "Metrik, log, dan trace untuk tahu apa yang terjadi di produksi.",
        "tingkat": "mahir",
        "jumlah": 7,
    },
    {
        "judul": "Biaya Cloud dan Proyek Akhir",
        "ket": "Mengendalikan tagihan cloud, lalu menyatukan semuanya dalam satu proyek.",
        "tingkat": "mahir",
        "jumlah": 1,
    },
]

DEVOPS_MATERIALS = [
    {
        "title": "1. Apa Itu DevOps, SRE, dan Metrik DORA",
        "sections": [
            {
                "body": [
                    "Bayangin sebuah toko online yang dikerjakan dua tim. Tim pengembang",
                    "menulis fitur baru selama tiga bulan. Begitu selesai, kodenya diserahkan",
                    "ke tim operasi, yaitu orang-orang yang mengurus server. Tim operasi baru",
                    "pertama kali melihat kode itu, dan malam rilisnya kacau. Ada pustaka",
                    "yang belum terpasang di server, ada konfigurasi yang beda dengan laptop",
                    "pengembang, dan nggak ada yang tahu siapa yang harus membetulkannya.",
                    "",
                    "Pola ini dulu umum. Rilis jadi jarang, besar, dan menakutkan. Makin",
                    "jarang rilis, makin banyak perubahan yang menumpuk, dan makin susah",
                    "mencari penyebab kalau ada yang rusak.",
                    "",
                    "DevOps lahir dari keluhan itu. Namanya gabungan dev (development,",
                    "pengembangan) dan ops (operations, operasi). DevOps adalah cara kerja:",
                    "tim yang menulis kode ikut bertanggung jawab sampai kode itu jalan di",
                    "server sungguhan, dan semua langkah yang bisa diulang dibuat otomatis.",
                    "Hasilnya rilis kecil yang sering, yang gampang dicek dan gampang",
                    "dibatalkan.",
                    "",
                    "Pemula sering mengira belajar DevOps sama dengan belajar Docker. Docker,",
                    "Kubernetes, dan Terraform memang alat yang dipakai orang DevOps, dan",
                    "semuanya dibahas di kurikulum ini. Tapi alat itu cuma membantu cara",
                    "kerjanya. Tim yang memakai Kubernetes tapi masih rilis tiga bulan sekali",
                    "dengan serah terima yang kacau belum menjalankan DevOps.",
                ],
            },
            {
                "heading": "Siklus yang terus berputar",
                "body": [
                    "Pekerjaan DevOps biasa digambar sebagai lingkaran yang nggak pernah",
                    "selesai. Tiap perubahan, sekecil apa pun, melewati langkah yang sama:",
                    "",
                    "  1. Plan: menentukan apa yang mau dibuat atau dibetulkan.",
                    "  2. Code: menulis kodenya, disimpan di Git.",
                    "  3. Build: mengubah kode jadi sesuatu yang bisa dijalankan, misalnya",
                    "     image container.",
                    "  4. Test: menjalankan tes otomatis.",
                    "  5. Release: menandai hasil build sebagai siap dipakai.",
                    "  6. Deploy: memasangnya di server.",
                    "  7. Operate: menjaga aplikasinya tetap jalan.",
                    "  8. Monitor: mengamati apa yang terjadi, lalu hasil pengamatannya jadi",
                    "     bahan untuk langkah plan berikutnya.",
                    "",
                    "Langkah 3 sampai 6 biasanya dikerjakan mesin lewat pipeline CI/CD, yang",
                    "dibahas di bab CI/CD dengan GitHub Actions. Langkah 8 dibahas di bab",
                    "Observability. Yang penting sekarang: lingkarannya berputar cepat. Tim",
                    "yang sehat bisa melewati satu putaran dalam hitungan jam.",
                ],
            },
            {
                "heading": "SRE: operasi dikerjakan seperti rekayasa",
                "body": [
                    "SRE (Site Reliability Engineering) adalah cara Google menjalankan",
                    "operasi, dan sekarang dipakai banyak perusahaan lain. Idenya sederhana:",
                    "pekerjaan operasi dikerjakan oleh orang yang berpikir seperti",
                    "programmer. Kalau ada tugas manual yang diulang tiap minggu, tugas itu",
                    "ditulis jadi program.",
                    "",
                    "Tiga istilah SRE yang bakal sering kamu temui:",
                    "  - Toil: pekerjaan manual yang berulang dan nggak menambah nilai,",
                    "    misalnya me-restart server yang sama tiap pagi. SRE berusaha",
                    "    menguranginya.",
                    "  - SLO (Service Level Objective): target keandalan yang disepakati,",
                    "    misalnya 99,9% permintaan berhasil dalam 30 hari.",
                    "  - Error budget: sisa \"jatah gagal\" dari SLO. Dengan target 99,9%,",
                    "    jatahnya 0,1%. Selama jatah masih ada, tim boleh rilis fitur baru",
                    "    dengan berani. Kalau jatah habis, tim fokus ke keandalan dulu.",
                    "",
                    "Buku SRE dari Google bisa dibaca gratis di sre.google. SLO dan error",
                    "budget dibahas lagi lebih rinci di bab Observability.",
                ],
            },
            {
                "heading": "Metrik DORA: cara mengukur tim",
                "body": [
                    "Gimana caranya tahu sebuah tim sudah bekerja dengan baik? DORA (DevOps",
                    "Research and Assessment) adalah program riset yang sekarang dijalankan",
                    "Google Cloud. Mereka menerbitkan laporan tiap tahun di dora.dev, dan",
                    "empat ukuran dari riset itu jadi bahasa bersama di industri:",
                    "",
                    "  Metrik                  Pertanyaannya",
                    "  Deployment frequency    seberapa sering kita deploy ke produksi?",
                    "  Change lead time        berapa lama dari commit sampai jalan di produksi?",
                    "  Change fail rate        berapa persen deploy yang langsung bikin masalah?",
                    "  Recovery time           berapa lama memulihkan deploy yang gagal?",
                    "",
                    "Dua metrik pertama mengukur kecepatan. Dua terakhir mengukur kestabilan.",
                    "Temuan riset itu yang paling sering dikutip: tim yang cepat ternyata",
                    "cenderung juga stabil. Rilis kecil yang sering lebih gampang dicek dan",
                    "lebih gampang dibatalkan daripada rilis besar yang jarang.",
                    "",
                    "Metrik keempat dulu disebut MTTR (mean time to restore). Panduan di",
                    "dora.dev sekarang menamainya failed deployment recovery time, dan",
                    "menambah metrik kelima, yaitu deployment rework rate: persentase deploy",
                    "tambahan yang terpaksa dilakukan karena ada insiden di produksi.",
                ],
            },
            {
                "heading": "Menghitung metrik dari catatan deploy",
                "code": """from statistics import median

# Catatan deploy satu tim selama dua minggu.
# (tanggal, berhasil?, menit dari commit sampai produksi, menit pulih)
deploy = [
    ("2026-10-05", True, 95, 0),
    ("2026-10-06", True, 140, 0),
    ("2026-10-08", False, 210, 50),
    ("2026-10-09", True, 80, 0),
    ("2026-10-12", True, 120, 0),
    ("2026-10-13", True, 60, 0),
    ("2026-10-15", False, 180, 25),
    ("2026-10-16", True, 100, 0),
]

minggu = 2
gagal = [d for d in deploy if not d[1]]

print("Frekuensi deploy :", len(deploy) / minggu, "per minggu")
print("Lead time median :", median(d[2] for d in deploy), "menit")
print("Change fail rate :", round(100 * len(gagal) / len(deploy)), "%")
print("Waktu pulih rata :", sum(d[3] for d in gagal) / len(gagal), "menit")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Frekuensi deploy : 4.0 per minggu",
                    "  Lead time median : 110.0 menit",
                    "  Change fail rate : 25 %",
                    "  Waktu pulih rata : 37.5 menit",
                    "",
                    "Lead time memakai median, yaitu nilai tengah sesudah datanya diurutkan.",
                    "Rata-rata gampang ketarik oleh satu deploy yang kebetulan lama sekali.",
                    "Median lebih jujur menggambarkan deploy yang biasa.",
                    "",
                    "Waktu pulih cuma dihitung dari deploy yang gagal. Deploy yang berhasil",
                    "nggak perlu dipulihkan, jadi angka nol mereka nggak ikut dirata-rata.",
                    "Kalau ikut, hasilnya kelihatan bagus padahal salah.",
                    "",
                    "Di tim sungguhan, datanya diambil dari riwayat pipeline CI/CD dan",
                    "catatan insiden, bukan diketik manual. Latihan pertama bab ini memintamu",
                    "menghitung keempat angka ini dari catatan yang dibaca lewat input.",
                ],
            },
            {
                "heading": "12-Factor App: aplikasi yang gampang di-deploy",
                "body": [
                    "Selain metrik, ada satu daftar lagi yang sering dirujuk orang DevOps,",
                    "yaitu 12-Factor App di 12factor.net. Isinya dua belas kebiasaan yang",
                    "bikin aplikasi gampang dipindah dari laptop ke server mana pun. Empat",
                    "yang paling kerasa dampaknya buat pemula:",
                    "",
                    "  Faktor            Artinya dalam praktik",
                    "  Config            setelan (alamat database, kunci API) dibaca dari",
                    "                    variabel lingkungan, tidak ditulis di kode",
                    "  Logs              aplikasi menulis log ke stdout; urusan menyimpan",
                    "                    log diserahkan ke lingkungannya",
                    "  Processes         proses tidak menyimpan data penting di disk atau",
                    "                    memorinya sendiri, jadi boleh dimatikan kapan saja",
                    "  Dev/prod parity   laptop dan server dibuat semirip mungkin",
                    "",
                    "Kamu bakal ketemu keempatnya lagi. Config lewat variabel lingkungan",
                    "muncul di Docker Compose, log ke stdout muncul di bab Observability, dan",
                    "proses yang boleh dimatikan kapan saja jadi dasar cara kerja Kubernetes.",
                ],
            },
            {
                "heading": "Peta kurikulum ini",
                "body": [
                    "Kurikulum ini menganggap kamu sudah lewat kurikulum CLI Fedora, Bash,",
                    "dan Git. Dasar Linux seperti berpindah folder, izin berkas, dan menulis",
                    "skrip nggak diulang di sini.",
                    "",
                    "Urutannya sengaja dibuat begini:",
                    "  - Bab 01 sampai 02: server Linux, SSH, YAML, jaringan, dan web server.",
                    "    Port dan DNS paling sering jadi sumber bingung waktu container",
                    "    pertamamu nggak bisa diakses, jadi keduanya dipelajari lebih dulu.",
                    "  - Bab 03 sampai 04: container dengan Docker, Compose, dan Podman.",
                    "  - Bab 05: CI/CD, yang bisa dicoba tanpa akun cloud.",
                    "  - Bab 06 sampai 08: cloud, serverless, dan infrastructure as code.",
                    "  - Bab 09 sampai 11: Kubernetes, GitOps, dan observability.",
                    "  - Bab 12: biaya cloud, lalu proyek akhir.",
                    "",
                    "Keamanan punya kurikulum sendiri, Keamanan Siber. Di sini keamanan cuma",
                    "disinggung di tempat yang memang butuh, misalnya login SSH dan rahasia",
                    "di pipeline.",
                    "",
                    "Semua perintah di kurikulum ini (docker, kubectl, terraform, dan",
                    "lainnya) ditulis sebagai contoh untuk dibaca. Aplikasi ini nggak pernah",
                    "menjalankannya, karena perintah itu bisa mengubah mesin atau akun cloud",
                    "sungguhan. Latihannya berupa simulasi kecil dalam Python yang bisa",
                    "dinilai tanpa internet.",
                ],
            },
            {
                "heading": "Kesalahan yang sering terjadi",
                "body": [
                    "Jebakan: memakai keempat metrik tadi untuk membandingkan atau menghukum orang.",
                    "Begitu angka dipakai untuk menilai individu, orang mulai memecah satu",
                    "perubahan jadi sepuluh deploy kecil supaya frekuensinya naik, dan",
                    "angkanya berhenti bercerita apa pun. Metrik ini dipakai untuk melihat",
                    "kemajuan satu tim dari waktu ke waktu.",
                    "",
                    "Kesalahan kedua: membuat tim baru bernama \"tim DevOps\" yang tugasnya",
                    "persis tim operasi lama. Tembok antara pengembang dan operasi tetap ada,",
                    "cuma namanya yang berganti.",
                    "",
                    "Kesalahan ketiga: langsung loncat ke Kubernetes sebelum paham Linux,",
                    "jaringan, dan container. Kubernetes menumpuk di atas ketiganya. Kalau",
                    "dasarnya belum kuat, pesan error Kubernetes bakal terasa seperti teka-teki.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Platform Git seperti GitHub dan GitLab mencatat setiap commit, setiap",
                    "jalannya pipeline, dan setiap deploy. GitLab punya halaman analitik",
                    "bawaan yang menampilkan keempat metrik tadi dari catatan itu, dan tim",
                    "memakai laporan tahunan di dora.dev sebagai pembanding.",
                    "",
                    "Kasus kecil: tim aplikasi kasir tempat kamu PKL rilis sebulan sekali,",
                    "dan dua dari tiga rilis terakhir bikin aplikasinya error sampai harus",
                    "dibatalkan. Ketua tim minta kamu menunjukkan dengan angka apa yang",
                    "salah, lalu mengusulkan perbaikan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kumpulkan catatan rilis tiga bulan terakhir dari riwayat Git dan",
                    "     catatan insiden: tanggal deploy, berhasil atau gagal, dan berapa",
                    "     lama sampai pulih.",
                    "  2. Hitung keempat metriknya. Di kasus ini frekuensinya sekitar",
                    "     sekali sebulan dan change fail rate-nya 67%.",
                    "  3. Cari penyebab rilis gagal. Biasanya rilis bulanan membawa puluhan",
                    "     perubahan sekaligus, jadi susah tahu perubahan mana yang merusak.",
                    "  4. Usulkan rilis yang lebih kecil dan lebih sering, didukung tes",
                    "     otomatis di pipeline, lalu hitung ulang metriknya sebulan kemudian",
                    "     untuk membuktikan apakah usulannya berhasil.",
                ],
            },
        ],
    },
    {
        "title": "2. Linux Server, SSH, dan Firewall untuk DevOps",
        "sections": [
            {
                "body": [
                    "Server itu komputer yang tugasnya melayani komputer lain, dan biasanya",
                    "nggak punya layar maupun keyboard. Letaknya di pusat data atau di cloud,",
                    "dan kamu mengurusnya dari jauh lewat terminal. Hampir semua server di",
                    "internet memakai Linux.",
                    "",
                    "Kurikulum CLI Fedora sudah mengajarkan perintah dasar Linux. Materi ini",
                    "menambah tiga hal yang khas pekerjaan server. Pertama, menjalankan",
                    "aplikasi sebagai layanan yang hidup terus. Kedua, masuk dari jauh dengan",
                    "aman lewat SSH. Ketiga, menutup semua pintu kecuali yang perlu dibuka.",
                ],
            },
            {
                "heading": "Distro server yang bakal kamu temui",
                "body": [
                    "Distro adalah paket lengkap Linux: kernel, program bawaan, dan manajer",
                    "paket. Di server, yang dicari adalah umur dukungan yang panjang, supaya",
                    "nggak perlu upgrade besar tiap tahun. Versi di bawah ini yang terbaru",
                    "saat materi ini ditulis (Oktober 2026):",
                    "",
                    "  Sistem              Versi terbaru            Keterangan",
                    "  Ubuntu Server       26.04.1 LTS              paling umum di VPS dan cloud",
                    "  Debian              13.7                     stabil, dasar dari Ubuntu",
                    "  Red Hat Enterprise  10.2                     langganan berbayar, perusahaan",
                    "  Rocky, AlmaLinux    mengikuti versi Red Hat  turunan gratis keluarga Red Hat",
                    "  Windows Server      2025                     aplikasi .NET lama, Active",
                    "                                               Directory",
                    "  FreeBSD             15.1                     firewall (pfSense, OPNsense)",
                    "  NetBSD              11.0                     sistem khusus",
                    "  Solaris             -                        menurun, praktis cuma di",
                    "                                               sistem lama Oracle",
                    "",
                    "LTS artinya long-term support: versi yang dirawat bertahun-tahun.",
                    "Fedora yang kamu pakai sekarang satu keluarga dengan Red Hat, jadi",
                    "perintahnya (dnf, firewalld, SELinux) langsung terpakai di server Rocky",
                    "atau AlmaLinux. Ubuntu dan Debian memakai apt dan ufw, tapi systemd dan",
                    "SSH-nya sama persis.",
                ],
            },
            {
                "heading": "Aplikasi sebagai layanan systemd",
                "body": [
                    "Kalau kamu menjalankan python3 app.py di terminal lalu menutup",
                    "terminalnya, aplikasinya ikut mati. Di server, aplikasi harus hidup",
                    "terus, nyala lagi sesudah server di-restart, dan dihidupkan ulang kalau",
                    "crash. Tugas itu dipegang systemd, program pertama yang jalan waktu",
                    "Linux menyala.",
                    "",
                    "Caranya: tulis berkas unit, yaitu berkas teks pendek yang menjelaskan",
                    "cara menjalankan aplikasimu. Berkas di bawah disimpan sebagai",
                    "/etc/systemd/system/toko.service.",
                ],
            },
            {
                "heading": "Berkas unit toko.service",
                "bahasa": "ini",
                "code": """[Unit]
Description=Aplikasi toko online
After=network-online.target

[Service]
User=toko
WorkingDirectory=/srv/toko
ExecStart=/usr/bin/python3 app.py
Environment=PORT=8000
Restart=on-failure

[Install]
WantedBy=multi-user.target""",
            },
            {
                "heading": "Mengurus layanannya",
                "bahasa": "terminal",
                "code": """sudo systemctl daemon-reload          # baca ulang berkas unit
sudo systemctl enable --now toko      # nyalakan sekarang dan tiap boot
systemctl status toko                 # hidup atau mati, plus log terakhir
journalctl -u toko -f                 # ikuti log layanan secara langsung
sudo systemctl restart toko           # sesudah kode diperbarui""",
            },
            {
                "body": [
                    "User=toko membuat aplikasinya jalan sebagai pengguna biasa bernama",
                    "toko, bukan root. Kalau aplikasinya dibobol, penyerang cuma dapat hak",
                    "pengguna itu. Restart=on-failure menghidupkan ulang aplikasi kalau ia",
                    "berhenti karena error.",
                    "",
                    "Semua yang dicetak aplikasi ke stdout dan stderr ditangkap journald,",
                    "pencatat log milik systemd. Itu yang dibaca journalctl. Jadi aplikasimu",
                    "cukup mencetak log biasa, sesuai kebiasaan 12-Factor tadi.",
                ],
            },
            {
                "heading": "SSH: masuk ke server dari jauh",
                "body": [
                    "SSH (Secure Shell) adalah cara masuk ke terminal server lewat jaringan",
                    "dengan koneksi terenkripsi. Program yang dipakai hampir semua orang",
                    "adalah OpenSSH. Versi terbarunya 10.6, dirilis 6 Oktober 2026. Sejak",
                    "versi 10.0, OpenSSH membuang algoritma tanda tangan lama yang lemah,",
                    "dan memakai pertukaran kunci pasca-kuantum (mlkem768x25519-sha256)",
                    "sebagai bawaan. Fedora 44 saat ini memaketkan OpenSSH 10.2.",
                    "",
                    "SSH bisa memakai password, tapi cara yang dianjurkan adalah pasangan",
                    "kunci. Kunci privat disimpan di laptopmu dan nggak pernah dikirim ke",
                    "mana pun. Kunci publik ditaruh di server. Waktu login, server memberi",
                    "tantangan yang cuma bisa dijawab oleh pemegang kunci privat. Mirip",
                    "gembok dan anak kunci: gemboknya boleh dibagikan ke banyak server,",
                    "anak kuncinya kamu pegang sendiri.",
                ],
            },
            {
                "heading": "Membuat dan memasang kunci",
                "bahasa": "terminal",
                "code": """ssh-keygen -t ed25519 -C "budi@laptop"     # buat pasangan kunci
ssh-copy-id budi@203.0.113.10              # pasang kunci publik di server
ssh budi@203.0.113.10                      # login tanpa password
ssh -L 5432:localhost:5432 budi@203.0.113.10   # terowongan ke database""",
            },
            {
                "body": [
                    "Perintah terakhir membuat terowongan (tunnel): port 5432 di laptopmu",
                    "diteruskan lewat SSH ke port 5432 di server. Dengan begitu kamu bisa",
                    "membuka database server dari laptop tanpa membuka port database ke",
                    "internet.",
                    "",
                    "Supaya nggak mengetik alamat panjang terus, tulis singkatannya di",
                    "~/.ssh/config:",
                    "",
                    "  Host toko",
                    "      HostName 203.0.113.10",
                    "      User budi",
                    "      IdentityFile ~/.ssh/id_ed25519",
                    "",
                    "Sesudah itu cukup ketik ssh toko.",
                    "",
                    "Begitu login berkunci sudah jalan, tutup pintu yang lain. Buat berkas",
                    "/etc/ssh/sshd_config.d/50-keras.conf di server:",
                    "",
                    "  PasswordAuthentication no",
                    "  PermitRootLogin no",
                    "",
                    "lalu jalankan sudo systemctl reload sshd. Server di internet dicoba",
                    "masuk oleh program otomatis tiap menit, dan dua baris itu menutup cara",
                    "yang paling sering mereka pakai: menebak password, terutama password",
                    "root.",
                    "",
                    "Jebakan: jangan menutup sesi SSH yang sedang terbuka sebelum mencoba",
                    "login dari terminal kedua. Kalau konfigurasimu salah, sesi pertama itu",
                    "satu-satunya jalan untuk membetulkannya.",
                ],
            },
            {
                "heading": "Membaca log percobaan login",
                "code": "from collections import Counter\n\nlog = \"\"\"\\\nOct 19 02:11:04 vps sshd[812]: Failed password for root from 203.0.113.7 port 51022 ssh2\nOct 19 02:11:09 vps sshd[812]: Failed password for root from 203.0.113.7 port 51022 ssh2\nOct 19 02:13:40 vps sshd[830]: Failed password for invalid user admin from 198.51.100.23 port 40110 ssh2\nOct 19 02:14:02 vps sshd[835]: Accepted publickey for budi from 192.0.2.44 port 52218 ssh2\nOct 19 02:15:17 vps sshd[841]: Failed password for root from 203.0.113.7 port 51388 ssh2\nOct 19 02:16:55 vps sshd[850]: Failed password for invalid user oracle from 198.51.100.23 port 40990 ssh2\n\"\"\"\n\ngagal = Counter()\nfor baris in log.splitlines():\n    if \"Failed password\" in baris:\n        ip = baris.split(\" from \")[1].split()[0]\n        gagal[ip] += 1\n    elif \"Accepted publickey\" in baris:\n        print(\"masuk sah :\", baris.split(\" for \")[1].split()[0])\n\nfor ip, jumlah in gagal.most_common():\n    print(f\"{ip:<15} {jumlah} kali gagal\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  masuk sah : budi",
                    "  203.0.113.7     3 kali gagal",
                    "  198.51.100.23   2 kali gagal",
                    "",
                    "Baris log itu tiruan dari keluaran journalctl -u sshd. Alamat",
                    "203.0.113.x dan 198.51.100.x memang disediakan khusus untuk contoh",
                    "dokumentasi, jadi bukan milik siapa pun. Di server sungguhan, alat",
                    "seperti fail2ban membaca log ini dan memblokir alamat yang gagal",
                    "berkali-kali.",
                ],
            },
            {
                "heading": "Firewall: cuma buka pintu yang perlu",
                "body": [
                    "Firewall adalah aturan yang memutuskan lalu lintas mana yang boleh",
                    "masuk dan mana yang ditolak, berdasarkan alamat, port, dan protokol.",
                    "Port itu nomor pintu di sebuah komputer: SSH biasanya di 22, HTTP di",
                    "80, HTTPS di 443. Server web yang sehat cuma membuka tiga port itu, dan",
                    "port database seperti 5432 tetap tertutup dari internet.",
                    "",
                    "Di Linux, aturan firewall dijalankan oleh nftables di dalam kernel,",
                    "pengganti iptables yang lama. Jarang ada yang menulis aturan nftables",
                    "langsung. Biasanya kamu memakai alat di atasnya:",
                    "  - firewalld di Fedora, Rocky, dan AlmaLinux. Aturannya dikelompokkan",
                    "    per zona.",
                    "  - ufw di Ubuntu dan Debian, dengan perintah yang lebih pendek.",
                    "  - Di cloud, ada security group yang bekerja di luar mesinnya. Ini",
                    "    dibahas di bab Cloud dan Layanan Inti AWS.",
                ],
            },
            {
                "heading": "firewalld dan ufw",
                "bahasa": "terminal",
                "code": """# Fedora, Rocky, AlmaLinux
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
sudo firewall-cmd --list-all

# Ubuntu, Debian
sudo ufw allow OpenSSH
sudo ufw allow 80,443/tcp
sudo ufw enable
sudo ufw status""",
            },
            {
                "body": [
                    "Di ufw, izinkan SSH dulu sebelum ufw enable. Urutan sebaliknya bisa",
                    "mengunci kamu dari server sendiri.",
                    "",
                    "Jebakan: Docker menulis aturan firewall-nya sendiri langsung ke kernel.",
                    "Port yang dibuka container dengan -p 5432:5432 bisa diakses dari",
                    "internet walaupun ufw atau firewalld bilang port itu tertutup. Cara",
                    "aman membukanya dibahas di materi Volume, Jaringan, dan Image Docker",
                    "yang Aman.",
                    "",
                    "Satu lagi yang bakal kamu temui di server Windows: PowerShell. Ini shell",
                    "dan bahasa skrip dari Microsoft yang mengalirkan objek, bukan teks,",
                    "dari satu perintah ke perintah berikutnya. Versi terbarunya 7.6.7",
                    "(13 Oktober 2026), berlisensi MIT, dan bisa jalan di Linux lewat",
                    "perintah pwsh. Windows PowerShell 5.1 bawaan Windows adalah versi lama",
                    "yang berbeda. PowerShell dipakai untuk otomasi Windows Server dan Azure,",
                    "dan bahasanya dibahas di kurikulum Bahasa Pemrograman Lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Penyedia VPS lokal maupun luar negeri biasanya menyerahkan server baru",
                    "dengan login root dan password, plus port 22 yang terbuka ke internet.",
                    "Beberapa menit sesudah server menyala, log SSH-nya sudah berisi",
                    "percobaan login dari alamat yang nggak dikenal.",
                    "",
                    "Kasus kecil: kamu baru menyewa VPS Ubuntu untuk aplikasi Flask buatanmu.",
                    "Sehari kemudian journalctl -u ssh berisi ribuan baris Failed password",
                    "for root, dan aplikasinya mati tiap kali VPS di-restart.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat pengguna biasa dengan hak sudo, lalu pasang kunci publikmu",
                    "     dengan ssh-copy-id.",
                    "  2. Buka terminal kedua dan pastikan login berkunci berhasil.",
                    "  3. Tulis PasswordAuthentication no dan PermitRootLogin no di berkas",
                    "     /etc/ssh/sshd_config.d/50-keras.conf, lalu reload sshd. Di Ubuntu,",
                    "     nama layanannya ssh, bukan sshd.",
                    "  4. Aktifkan ufw dengan aturan OpenSSH, 80, dan 443 saja.",
                    "  5. Tulis berkas unit systemd untuk aplikasinya dengan",
                    "     Restart=on-failure, lalu jalankan:",
                    "       sudo systemctl enable --now flaskku",
                    "  6. Restart VPS sekali, lalu cek systemctl status flaskku untuk",
                    "     memastikan aplikasinya nyala sendiri.",
                ],
            },
        ],
    },
    {
        "title": "3. YAML, Bahasa Konfigurasi Alat DevOps",
        "sections": [
            {
                "body": [
                    "Hampir semua alat di kurikulum ini membaca konfigurasinya dari berkas",
                    "YAML: compose.yaml milik Docker Compose, manifest Kubernetes, workflow",
                    "GitHub Actions, .gitlab-ci.yml, playbook Ansible, sampai values Helm.",
                    "Kalau kamu bisa membaca YAML dengan lancar, separuh kebingungan di bab",
                    "berikutnya hilang.",
                    "",
                    "YAML adalah format teks untuk menulis data terstruktur, mirip JSON tapi",
                    "lebih enak dibaca manusia. Bedanya yang paling besar: struktur di YAML",
                    "ditandai dengan indentasi, bukan kurung kurawal. Spesifikasi terbarunya",
                    "YAML 1.2.2, terbit Oktober 2021, dan jarang berubah.",
                ],
            },
            {
                "heading": "Tiga bentuk data",
                "body": [
                    "Semua berkas YAML disusun dari tiga bentuk saja:",
                    "",
                    "  - Mapping: pasangan kunci dan nilai, ditulis kunci: nilai. Sama",
                    "    dengan dict di Python.",
                    "  - Sequence: daftar berurutan, tiap butir diawali tanda hubung dan",
                    "    satu spasi. Sama dengan list di Python.",
                    "  - Scalar: nilai tunggal, misalnya teks, angka, atau true dan false.",
                    "",
                    "Ketiganya boleh disarangkan. Mapping bisa berisi daftar, daftar bisa",
                    "berisi mapping, dan seterusnya. Yang menentukan sesuatu ada di dalam",
                    "apa cuma jumlah spasi di awal baris.",
                ],
            },
            {
                "heading": "Contoh konfigurasi",
                "bahasa": "yaml",
                "code": """# konfigurasi aplikasi toko
aplikasi: toko
versi: "1.10"
server:
  host: 0.0.0.0
  port: 8080
fitur:
  - keranjang
  - pembayaran
admin:
  - nama: budi
    email: budi@contoh.id
  - nama: sari
    email: sari@contoh.id
pesan_sambutan: |
  Selamat datang di toko kami.
  Gratis ongkir untuk Jawa.""",
            },
            {
                "body": [
                    "Kita baca bagian per bagian:",
                    "  - Baris yang diawali # adalah komentar.",
                    "  - server berisi mapping dua kunci, host dan port, karena keduanya",
                    "    menjorok dua spasi di bawahnya.",
                    "  - fitur berisi daftar dua teks.",
                    "  - admin berisi daftar yang tiap butirnya mapping. Perhatikan email",
                    "    sejajar dengan nama, bukan dengan tanda hubung. Tanda hubung itu",
                    "    milik butir daftar, dan nama serta email sama-sama isi butir itu.",
                    "  - Tanda | setelah pesan_sambutan berarti teks banyak baris, dan",
                    "    pindah barisnya dipertahankan. Kalau pakai >, baris-barisnya",
                    "    disambung jadi satu paragraf.",
                    "  - versi diberi tanda kutip. Alasannya ada di bagian jebakan nanti.",
                    "",
                    "Data yang sama kalau ditulis sebagai JSON:",
                ],
            },
            {
                "heading": "Isi yang sama dalam JSON",
                "bahasa": "json",
                "code": "{\n  \"aplikasi\": \"toko\",\n  \"versi\": \"1.10\",\n  \"server\": {\"host\": \"0.0.0.0\", \"port\": 8080},\n  \"fitur\": [\"keranjang\", \"pembayaran\"],\n  \"admin\": [\n    {\"nama\": \"budi\", \"email\": \"budi@contoh.id\"},\n    {\"nama\": \"sari\", \"email\": \"sari@contoh.id\"}\n  ],\n  \"pesan_sambutan\": \"Selamat datang di toko kami.\\nGratis ongkir untuk Jawa.\\n\"\n}",
            },
            {
                "body": [
                    "YAML 1.2 dirancang supaya setiap berkas JSON yang sah juga YAML yang",
                    "sah. Jadi kalau suatu saat ragu, nilai bergaya JSON seperti",
                    "[\"keranjang\", \"pembayaran\"] boleh dipakai di dalam berkas YAML.",
                    "",
                    "Satu berkas YAML boleh berisi beberapa dokumen, dipisah baris ---.",
                    "Bentuk ini sering kamu temui di manifest Kubernetes, yang menaruh",
                    "beberapa objek dalam satu berkas.",
                    "",
                    "Python nggak punya pengurai YAML bawaan. Pustaka yang paling sering",
                    "dipakai, PyYAML, harus dipasang terpisah dengan pip. Karena latihan di",
                    "aplikasi ini cuma boleh memakai pustaka standar, latihan kedua bab ini",
                    "memintamu menulis pengurai YAML mini sendiri.",
                ],
            },
            {
                "heading": "Jebakan indentasi",
                "body": [
                    "Indentasi di YAML harus memakai spasi. Tab dilarang oleh spesifikasinya,",
                    "dan pengurai mana pun bakal menolak berkas yang memakai tab. Banyak",
                    "editor menyisipkan karakter tab waktu kamu menekan tombol Tab, jadi",
                    "atur editormu supaya Tab menghasilkan dua spasi untuk berkas .yaml.",
                    "",
                    "Kesalahan indentasi yang lebih licik adalah yang tetap sah. Contohnya:",
                    "",
                    "  server:",
                    "    host: 0.0.0.0",
                    "  port: 8080",
                    "",
                    "port di sini sejajar dengan server, jadi ia jadi kunci tingkat atas,",
                    "bukan bagian dari server. Pengurainya nggak protes. Aplikasinya yang",
                    "kemudian bingung karena server.port nggak ada. Alat seperti yamllint",
                    "membantu menangkap kesalahan semacam ini sebelum berkasnya dipakai.",
                ],
            },
            {
                "heading": "Jebakan YAML 1.1: no bisa jadi false",
                "code": "import re\n\n# Aturan YAML 1.1 yang masih dipakai banyak pustaka, misalnya PyYAML.\nBENAR = {\"yes\", \"true\", \"on\"}\nSALAH = {\"no\", \"false\", \"off\"}\n\n\ndef tafsir_yaml11(teks):\n    kecil = teks.lower()\n    if kecil in BENAR:\n        return True\n    if kecil in SALAH:\n        return False\n    if re.fullmatch(r\"0[0-7]+\", teks):\n        return int(teks, 8)                 # angka oktal\n    if re.fullmatch(r\"\\d+:[0-5]\\d\", teks):\n        jam, menit = teks.split(\":\")\n        return int(jam) * 60 + int(menit)   # angka basis 60\n    if re.fullmatch(r\"\\d+\\.\\d+\", teks):\n        return float(teks)\n    if re.fullmatch(r\"\\d+\", teks):\n        return int(teks)\n    return teks\n\n\nfor nilai in [\"NO\", \"on\", \"1.10\", \"0755\", \"22:30\", \"nginx\"]:\n    hasil = tafsir_yaml11(nilai)\n    print(f\"{nilai:<6} -> {hasil!r}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  NO     -> False",
                    "  on     -> True",
                    "  1.10   -> 1.1",
                    "  0755   -> 493",
                    "  22:30  -> 1350",
                    "",
                    "Program ini meniru cara pengurai YAML 1.1 menebak tipe nilai yang",
                    "nggak diberi tanda kutip. Fungsinya disederhanakan: YAML 1.1 cuma",
                    "mengenali bentuk huruf kecil, huruf besar di awal, atau huruf besar",
                    "semua (no, No, NO), sedangkan program ini menerima campuran apa pun.",
                    "",
                    "Hasilnya mengejutkan banyak orang:",
                    "  - NO, kode negara Norwegia, berubah jadi False. Kasus ini terkenal",
                    "    dengan nama \"Norway problem\".",
                    "  - versi 1.10 jadi angka 1.1, jadi dua versi yang beda terbaca sama.",
                    "  - 0755 dibaca sebagai bilangan oktal, jadi 493.",
                    "  - 22:30 dibaca sebagai bilangan basis 60, jadi 1350.",
                    "",
                    "YAML 1.2 sudah membuang sebagian besar aturan ini: yang dianggap",
                    "boolean tinggal true dan false. Masalahnya, banyak pustaka populer,",
                    "termasuk PyYAML, masih mengikuti YAML 1.1. Kamu nggak selalu tahu",
                    "pengurai mana yang membaca berkasmu.",
                    "",
                    "Ingat: aturan amannya cuma satu. Beri tanda kutip pada setiap nilai",
                    "yang harus tetap teks: nomor versi, kode negara, jam, kode pos, dan",
                    "semua yang diawali angka nol.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Workflow GitHub Actions selalu diawali kunci on:, yang menentukan kapan",
                    "workflow dijalankan. GitHub membacanya dengan benar, tapi skrip Python",
                    "yang membaca berkas workflow yang sama lewat PyYAML mendapat kunci True,",
                    "karena PyYAML mengikuti YAML 1.1. Kasus seperti ini sering muncul di",
                    "skrip pemeriksa konfigurasi buatan tim sendiri.",
                    "",
                    "Kasus kecil: kamu menulis skrip Python yang membaca daftar negara",
                    "pengiriman dari berkas YAML. Isinya [ID, MY, SG, NO]. Skripnya error",
                    "karena salah satu butir ternyata boolean, bukan teks, dan di",
                    "konfigurasi workflow-mu kunci on: juga hilang dari hasil bacaan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cetak tipe tiap nilai yang terbaca. Butir keempat ternyata False",
                    "     dan kunci on jadi True. Dari situ kelihatan penyebabnya aturan",
                    "     YAML 1.1, bukan salah ketik.",
                    "  2. Beri tanda kutip pada nilai yang harus tetap teks:",
                    "       negara: [\"ID\", \"MY\", \"SG\", \"NO\"]",
                    "  3. Untuk kunci on di workflow, jangan mengubah berkasnya karena",
                    "     GitHub membutuhkannya. Di skripmu, cari kunci True sebagai",
                    "     cadangan, atau pakai pengurai yang mendukung YAML 1.2 seperti",
                    "     ruamel.yaml.",
                    "  4. Pasang yamllint di pipeline supaya nilai yang rawan ketahuan",
                    "     sebelum berkasnya dipakai.",
                ],
            },
        ],
    },
    {
        "title": "4. Protokol Jaringan, Port, dan Alat Diagnosis",
        "sections": [
            {
                "body": [
                    "\"Websitenya nggak bisa dibuka.\" Kalimat ini bakal sering kamu dengar,",
                    "dan penyebabnya bisa di mana saja. Nama domainnya bisa salah arah,",
                    "servernya mati, port-nya ditutup firewall, atau aplikasinya crash. Bisa",
                    "juga aplikasinya jalan tapi cuma mau menerima koneksi dari dirinya",
                    "sendiri. Orang yang",
                    "nggak paham jaringan bakal menebak-nebak. Orang yang paham bisa",
                    "mempersempit penyebabnya dalam lima menit.",
                    "",
                    "Materi ini membekali kamu dengan peta jaringan secukupnya, lalu urutan",
                    "pemeriksaan yang bisa dipakai setiap kali ada yang nggak bisa diakses.",
                ],
            },
            {
                "heading": "Alamat IP dan port",
                "body": [
                    "Setiap komputer di jaringan punya alamat IP, misalnya 203.0.113.10",
                    "untuk IPv4 atau 2001:db8::10 untuk IPv6. Alamat ini menunjuk mesinnya.",
                    "Satu mesin bisa menjalankan banyak program yang sama-sama menunggu",
                    "koneksi, jadi dibutuhkan nomor kedua, yaitu port.",
                    "",
                    "Gampangnya, alamat IP itu alamat gedung, port itu nomor ruangan. Port",
                    "yang sering kamu temui:",
                    "",
                    "  Port   Layanan",
                    "  22     SSH",
                    "  53     DNS",
                    "  80     HTTP",
                    "  443    HTTPS",
                    "  5432   PostgreSQL",
                    "  3306   MySQL",
                    "  6379   Redis",
                    "",
                    "Satu hal lagi yang sering bikin bingung: alamat tempat program",
                    "mendengarkan. Program yang mendengarkan di 127.0.0.1 cuma bisa dihubungi",
                    "dari mesin itu sendiri. Program yang mendengarkan di 0.0.0.0 menerima",
                    "koneksi dari jaringan mana pun. Banyak server pengembangan, misalnya",
                    "Flask, memakai 127.0.0.1 sebagai bawaan. Kalau kamu menjalankannya di",
                    "server lalu membuka alamat server dari laptop, hasilnya gagal walaupun",
                    "aplikasinya jalan.",
                ],
            },
            {
                "heading": "TCP, UDP, dan lapisan-lapisannya",
                "body": [
                    "Data di jaringan dikirim lewat beberapa lapisan. Tiap lapisan punya",
                    "tugas sendiri dan nggak perlu tahu urusan lapisan lain. Model TCP/IP",
                    "yang dipakai internet punya empat lapisan:",
                    "",
                    "  Lapisan          Contoh               Tugasnya",
                    "  Aplikasi         HTTP, DNS, SSH       isi percakapannya",
                    "  Transport        TCP, UDP             mengantar ke port yang benar",
                    "  Internet         IP                   mengantar ke mesin yang benar",
                    "  Akses jaringan   Ethernet, Wi-Fi      kabel dan sinyalnya",
                    "",
                    "Di buku dan wawancara kerja kamu juga bakal ketemu model OSI yang",
                    "tujuh lapisan. Isinya sama, cuma dipecah lebih halus. Orang sering",
                    "menyebut \"L4\" untuk transport dan \"L7\" untuk aplikasi, dan istilah ini",
                    "dipakai lagi waktu membahas load balancer.",
                    "",
                    "Di lapisan transport ada dua pilihan:",
                    "  - TCP memastikan semua data sampai, utuh, dan berurutan. Sebelum",
                    "    mengirim data, kedua pihak berjabat tangan dulu. HTTP/1.1, HTTP/2,",
                    "    SSH, dan koneksi database memakai TCP.",
                    "  - UDP langsung mengirim tanpa jabat tangan dan tanpa jaminan sampai.",
                    "    Lebih cepat, cocok untuk DNS, panggilan video, dan game.",
                    "",
                    "HTTP sendiri punya tiga versi yang masih dipakai. HTTP/1.1 berbentuk",
                    "teks dan satu koneksi melayani satu permintaan pada satu waktu. HTTP/2",
                    "memakai format biner dan bisa melayani banyak permintaan sekaligus",
                    "lewat satu koneksi TCP. HTTP/3 berjalan di atas QUIC, protokol baru",
                    "yang memakai UDP, supaya satu paket yang hilang nggak menahan semua",
                    "permintaan lain. HTTPS adalah HTTP yang dibungkus enkripsi TLS, yang",
                    "dibahas di materi Nginx Lanjutan.",
                    "",
                    "Beberapa protokol lain yang bakal muncul di pekerjaan:",
                    "  - FTP (port 21) mengirim berkas tanpa enkripsi, termasuk password-nya.",
                    "    Pakai SFTP, yang berjalan di atas SSH di port 22.",
                    "  - SNMP dipakai untuk memantau perangkat jaringan seperti router dan",
                    "    switch.",
                    "  - Virtual LAN membagi satu switch fisik jadi beberapa jaringan terpisah,",
                    "    misalnya jaringan kasir dan jaringan Wi-Fi tamu.",
                ],
            },
            {
                "heading": "Seperti apa permintaan HTTP itu",
                "code": "mentah = (\n    \"GET /produk?kategori=kopi HTTP/1.1\\r\\n\"\n    \"Host: toko.contoh.id\\r\\n\"\n    \"User-Agent: curl/8.15.0\\r\\n\"\n    \"Accept: */*\\r\\n\"\n    \"\\r\\n\"\n)\n\nkepala, _, badan = mentah.partition(\"\\r\\n\\r\\n\")\nbaris = kepala.split(\"\\r\\n\")\nmetode, jalur, versi = baris[0].split(\" \")\nheader = {}\nfor b in baris[1:]:\n    nama, _, nilai = b.partition(\": \")\n    header[nama.lower()] = nilai\n\nprint(\"metode :\", metode)\nprint(\"jalur  :\", jalur)\nprint(\"versi  :\", versi)\nprint(\"host   :\", header[\"host\"])\nprint(\"badan  :\", repr(badan))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  metode : GET",
                    "  jalur  : /produk?kategori=kopi",
                    "  versi  : HTTP/1.1",
                    "  host   : toko.contoh.id",
                    "  badan  : ''",
                    "",
                    "Permintaan HTTP/1.1 cuma teks. Baris pertama berisi metode, jalur, dan",
                    "versi. Sesudahnya header, satu per baris, lalu satu baris kosong, lalu",
                    "badan (kosong untuk GET). Header Host penting sekali: satu server",
                    "dengan satu alamat IP bisa melayani banyak domain, dan Host yang",
                    "memberi tahu domain mana yang diminta. Nginx memakainya di materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Membaca pesan error koneksi",
                "body": [
                    "Tiga pesan error ini kelihatan mirip, padahal masing-masing menunjuk",
                    "tempat yang beda:",
                    "",
                    "  Pesan                    Artinya",
                    "  Could not resolve host   DNS gagal: nama domain tidak jadi alamat IP",
                    "  Connection refused       mesin dihubungi dan menjawab, tapi tidak ada",
                    "                           program yang mendengarkan di port itu",
                    "  Connection timed out     tidak ada jawaban sama sekali: firewall",
                    "                           membuang paketnya, atau mesinnya tak terjangkau",
                    "",
                    "Refused itu kabar yang lumayan baik. Jaringannya sampai, mesinnya hidup,",
                    "tinggal cari tahu kenapa programnya nggak mendengarkan. Timeout biasanya",
                    "urusan firewall atau security group.",
                ],
            },
            {
                "heading": "Kotak perkakas diagnosis",
                "bahasa": "terminal",
                "code": """dig +short toko.contoh.id             # 1. DNS: nama ini jadi IP berapa?
ping -c 3 203.0.113.10                # 2. mesinnya terjangkau?
traceroute 203.0.113.10               #    lewat mana saja, putus di mana?
nc -vz 203.0.113.10 443               # 3. port-nya terbuka?
curl -v https://toko.contoh.id/       # 4. HTTP-nya menjawab apa?

# di servernya sendiri
ss -tlnp                              # program apa mendengarkan di port mana
sudo tcpdump -i any port 443          # rekam paket yang lewat""",
            },
            {
                "body": [
                    "Urutannya mengikuti lapisan, dari bawah ke atas: nama, mesin, port,",
                    "lalu aplikasi. Berhenti di langkah pertama yang gagal, karena di situlah",
                    "masalahnya.",
                    "",
                    "Beberapa catatan:",
                    "  - ping memakai ICMP, yang sering diblokir di cloud. Ping gagal belum",
                    "    tentu mesinnya mati. Kalau nc ke port 443 berhasil, mesinnya hidup.",
                    "  - mtr menggabungkan ping dan traceroute dalam satu tampilan yang",
                    "    terus diperbarui.",
                    "  - ss -tlnp di server menunjukkan alamat dengar tiap program. Kalau",
                    "    di sana tertulis 127.0.0.1:8000, aplikasinya memang cuma menerima",
                    "    koneksi lokal.",
                    "  - Rekaman tcpdump bisa disimpan ke berkas lalu dibuka di Wireshark,",
                    "    yang menampilkan isi tiap paket dengan rapi.",
                    "",
                    "Jebakan: menyimpulkan \"servernya down\" dari satu ping yang gagal, lalu",
                    "me-restart server yang masih sehat. Selalu cek port dan HTTP-nya",
                    "sebelum menyentuh apa pun.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua tiket dukungan untuk aplikasi web yang baru dipasang",
                    "berbunyi \"nggak bisa diakses\". Perintah dig, nc, curl, dan ss ada di",
                    "hampir semua server Linux, dan tim operasi biasanya punya urutan",
                    "pemeriksaan tertulis yang mirip urutan di atas.",
                    "",
                    "Kasus kecil: kamu menjalankan aplikasi Flask di VPS dengan perintah",
                    "flask run --port 8000. Dari laptop, curl http://203.0.113.10:8000",
                    "menunggu lama lalu menyerah dengan pesan timeout. Di VPS sendiri,",
                    "curl http://127.0.0.1:8000 berhasil.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Aplikasinya jalan, karena curl lokal berhasil. Jadi masalahnya",
                    "     ada di jalan antara laptop dan aplikasi.",
                    "  2. Jalankan ss -tlnp di VPS. Hasilnya menunjukkan 127.0.0.1:8000,",
                    "     artinya Flask cuma mendengarkan koneksi lokal.",
                    "  3. Pesan timeout juga menunjuk firewall. Cek dengan",
                    "     sudo ufw status, dan port 8000 ternyata belum dibuka.",
                    "  4. Cara rapinya: biarkan Flask tetap di 127.0.0.1, lalu pasang Nginx",
                    "     di port 80 sebagai pintu depannya. Itu isi materi Nginx: Web",
                    "     Server dan Reverse Proxy. Port 8000 nggak perlu dibuka ke",
                    "     internet sama sekali.",
                ],
            },
        ],
    },
    {
        "title": "5. DNS: Dari Nama Domain ke Alamat IP",
        "sections": [
            {
                "body": [
                    "Komputer saling menghubungi lewat alamat IP, tapi manusia lebih gampang",
                    "mengingat nama seperti toko.id. DNS (Domain Name System) adalah sistem",
                    "yang menerjemahkan nama itu jadi alamat IP. Gampangnya, DNS itu buku",
                    "telepon internet.",
                    "",
                    "Buat orang DevOps, DNS muncul di mana-mana: mengarahkan domain ke",
                    "server baru, membuktikan kepemilikan domain ke Google atau GitHub,",
                    "mengatur email supaya nggak masuk spam, sampai memasang HTTPS. DNS juga",
                    "penyebab keluhan klasik: \"domainnya sudah kuganti dari tadi, kok masih",
                    "ke server lama?\"",
                ],
            },
            {
                "heading": "Jenis record yang perlu kamu kenal",
                "body": [
                    "Isi DNS untuk satu domain disebut zona, dan tiap barisnya disebut",
                    "record. Tiap record punya nama, jenis, nilai, dan TTL (time to live):",
                    "",
                    "  Jenis   Isinya                                Contoh nilai",
                    "  A       alamat IPv4                           203.0.113.10",
                    "  AAAA    alamat IPv6                           2001:db8::10",
                    "  CNAME   nama lain yang harus dicari lagi      toko.id",
                    "  MX      server penerima email                 10 mail.toko.id",
                    "  TXT     teks bebas: verifikasi, SPF, DKIM     v=spf1 ... ~all",
                    "  NS      server yang memegang zona ini         ns1.penyedia.net",
                    "  CAA     CA yang boleh menerbitkan sertifikat  0 issue \"letsencrypt.org\"",
                    "",
                    "Record alias (baris ketiga di tabel) membuat satu nama",
                    "menunjuk ke nama lain. Misalnya www.toko.id diarahkan ke toko.id, jadi",
                    "kalau alamat IP toko.id berubah, www ikut berubah tanpa disunting.",
                    "Layanan seperti Netlify dan Vercel biasanya memintamu membuat alias ke",
                    "nama milik mereka.",
                ],
            },
            {
                "heading": "Mengikuti rantai alias",
                "code": """zona = {
    "www.toko.id": ("CNAME", "toko.id"),
    "toko.id": ("A", "203.0.113.10"),
    "blog.toko.id": ("CNAME", "toko-blog.netlify.app"),
    "toko-blog.netlify.app": ("A", "198.51.100.77"),
}


def resolve(nama):
    while True:
        tipe, nilai = zona[nama]
        print(f"  {nama} {tipe} {nilai}")
        if tipe == "A":
            return nilai
        nama = nilai


for nama in ["www.toko.id", "blog.toko.id"]:
    print(nama)
    print("  =>", resolve(nama))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  www.toko.id",
                    "    www.toko.id CNAME toko.id",
                    "    toko.id A 203.0.113.10",
                    "    => 203.0.113.10",
                    "  blog.toko.id",
                    "    blog.toko.id CNAME toko-blog.netlify.app",
                    "    toko-blog.netlify.app A 198.51.100.77",
                    "    => 198.51.100.77",
                    "",
                    "Program ini menyederhanakan banyak hal. Zona sungguhan tersebar di",
                    "banyak server, dan alias bisa menunjuk ke zona milik orang lain,",
                    "seperti blog yang menunjuk ke Netlify. Program ini juga akan berputar",
                    "terus kalau dua alias saling menunjuk. Latihan bab ini memintamu",
                    "menambal kekurangan itu dan menambahkan cache.",
                ],
            },
            {
                "heading": "Perjalanan satu pertanyaan DNS",
                "body": [
                    "Waktu browsermu perlu alamat toko.id, urutannya kira-kira begini:",
                    "",
                    "  1. Sistem operasi mengecek cache-nya sendiri dan berkas /etc/hosts.",
                    "  2. Kalau belum ada, pertanyaan dikirim ke resolver rekursif. Ini",
                    "     server DNS milik penyedia internetmu, atau resolver publik seperti",
                    "     1.1.1.1 (Cloudflare) dan 8.8.8.8 (Google).",
                    "  3. Resolver bertanya ke server root: \"siapa yang tahu soal .id?\"",
                    "     Root menjawab daftar server untuk .id.",
                    "  4. Resolver bertanya ke server .id, yang dikelola PANDI: \"siapa yang",
                    "     tahu soal toko.id?\" Jawabannya server NS milik toko.id.",
                    "  5. Resolver bertanya ke server otoritatif toko.id, yaitu server yang",
                    "     memegang zona aslinya. Dari sini alamat IP-nya didapat.",
                    "  6. Resolver menyimpan jawabannya di cache selama TTL, lalu",
                    "     mengirimkannya ke laptopmu.",
                    "",
                    "Langkah 3 sampai 5 cuma terjadi kalau cache resolver kosong. Sebagian",
                    "besar pertanyaan dijawab langsung dari cache, dan itu yang membuat DNS",
                    "cepat.",
                ],
            },
            {
                "heading": "TTL dan mitos propagasi",
                "body": [
                    "TTL adalah berapa detik sebuah jawaban boleh disimpan di cache. Kalau",
                    "record A toko.id punya TTL 3600, resolver di seluruh dunia boleh terus",
                    "menjawab dengan alamat lama sampai satu jam sesudah mereka terakhir",
                    "bertanya.",
                    "",
                    "Orang menyebut jeda ini \"propagasi DNS\", seolah perubahan merambat",
                    "pelan-pelan dari satu server ke server lain. Yang terjadi lebih",
                    "sederhana: cache di banyak resolver belum kedaluwarsa. Begitu TTL",
                    "habis, resolver bertanya lagi dan dapat alamat baru.",
                    "",
                    "Akibatnya bisa direncanakan. Sehari sebelum pindah server, turunkan",
                    "TTL record-nya jadi 300 detik. Tunggu sampai TTL lama (misalnya satu",
                    "jam) lewat, baru ganti alamatnya. Sesudah pindah dan semuanya stabil,",
                    "naikkan lagi TTL-nya.",
                    "",
                    "Jebakan: record alias nggak boleh dipasang di apex, yaitu nama domain",
                    "polos tanpa awalan seperti toko.id. Standar DNS melarang alias hidup",
                    "berdampingan dengan record lain, dan apex selalu punya record NS dan",
                    "SOA. Banyak penyedia DNS menyediakan jalan keluar, misalnya fitur",
                    "flattening di Cloudflare. Penyedia itu sendiri yang mencari alamat IP",
                    "tujuannya, lalu menjawab sebagai record A biasa.",
                ],
            },
            {
                "heading": "Bertanya langsung dengan dig",
                "bahasa": "terminal",
                "code": """dig toko.id                    # jawaban lengkap, termasuk TTL tersisa
dig +short www.toko.id         # cuma hasilnya
dig toko.id MX                 # server email
dig @1.1.1.1 toko.id           # tanya resolver tertentu
dig @ns1.penyedia.net toko.id  # tanya server otoritatif langsung
dig +trace toko.id             # ikuti jalannya dari root
resolvectl query toko.id       # Fedora: lewat systemd-resolved""",
            },
            {
                "body": [
                    "Angka TTL di keluaran dig dari resolver adalah sisa waktu cache-nya,",
                    "jadi angkanya mengecil kalau kamu bertanya berulang kali. Bertanya ke",
                    "server otoritatif langsung memberi jawaban terbaru tanpa cache. Kalau",
                    "server otoritatif sudah menjawab alamat baru tapi resolver masih",
                    "menjawab yang lama, berarti kamu cuma perlu menunggu TTL habis.",
                    "",
                    "Ingat: berkas /etc/hosts menang atas DNS di mesin itu. Entri lama yang",
                    "lupa dihapus dari sana bisa membuat satu laptop terus menuju server",
                    "lama, sementara semua orang lain sudah pindah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Domain .id dan .co.id dibeli lewat registrar, lalu zonanya diurus di",
                    "penyedia DNS, misalnya registrar itu sendiri atau Cloudflare. Pindah",
                    "hosting, memasang toko online, dan menyambungkan email kantor semuanya",
                    "berujung ke menyunting record di panel penyedia DNS.",
                    "",
                    "Kasus kecil: toko online pindah dari hosting lama ke VPS baru. Record",
                    "A toko.id sudah diganti ke alamat VPS dua jam lalu, tapi sebagian",
                    "pembeli masih masuk ke server lama dan pesanan mereka tercatat di",
                    "sana.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tanya server otoritatif langsung dengan",
                    "     dig @ns1.penyedia.net toko.id. Kalau jawabannya alamat baru,",
                    "     zonanya sudah benar.",
                    "  2. Tanya beberapa resolver publik, misalnya dig @8.8.8.8 toko.id,",
                    "     dan lihat angka TTL tersisa. Ternyata TTL lamanya 86400, satu",
                    "     hari penuh.",
                    "  3. Biarkan server lama tetap hidup sampai TTL lama itu lewat, dan",
                    "     arahkan aplikasinya ke database yang sama dengan server baru",
                    "     supaya pesanan nggak terpecah.",
                    "  4. Untuk pindahan berikutnya, turunkan TTL ke 300 sehari sebelumnya.",
                ],
            },
        ],
    },
    {
        "title": "6. Nginx: Web Server dan Reverse Proxy",
        "sections": [
            {
                "body": [
                    "Aplikasi Flask, Express, atau Spring yang kamu tulis bisa langsung",
                    "menerima permintaan HTTP. Tapi di server sungguhan, hampir selalu ada",
                    "satu program lagi di depannya: web server. Ia yang menerima semua",
                    "permintaan dari internet di port 80 dan 443, lalu memutuskan apa yang",
                    "harus dilakukan.",
                    "",
                    "Nginx (dibaca \"engine-x\") adalah web server yang paling sering dipakai",
                    "untuk tugas ini. Ia punya dua peran:",
                    "  - Menyajikan berkas statis seperti HTML, CSS, gambar, dan hasil build",
                    "    React, langsung dari disk. Untuk tugas ini Nginx jauh lebih cepat",
                    "    daripada aplikasimu.",
                    "  - Jadi reverse proxy: meneruskan permintaan ke aplikasimu yang jalan",
                    "    di port lain, lalu mengembalikan jawabannya ke pengunjung.",
                    "",
                    "Reverse proxy berdiri di depan server dan mewakili server. Kebalikannya",
                    "forward proxy, yang berdiri di depan klien dan mewakili klien, misalnya",
                    "proxy kantor yang dipakai karyawan untuk keluar ke internet. Dua istilah",
                    "ini sering tertukar.",
                ],
            },
            {
                "heading": "Versi dan cara memasang",
                "body": [
                    "Saat materi ini ditulis (Oktober 2026), versi stabil Nginx adalah",
                    "1.30.6 dan versi mainline 1.31.7, keduanya dirilis 14 Oktober 2026",
                    "dengan beberapa perbaikan keamanan. Nomor minor genap berarti stable,",
                    "ganjil berarti mainline. Pengembang Nginx sendiri menyarankan mainline,",
                    "tapi distro Linux biasanya memaketkan cabang stable. Nginx berlisensi",
                    "BSD dan sekarang dimiliki perusahaan F5.",
                    "",
                    "Di Fedora, Rocky, dan AlmaLinux, Nginx dipasang dengan dnf. Konfigurasi",
                    "utamanya /etc/nginx/nginx.conf, dan konfigurasi per situs ditaruh",
                    "sebagai berkas .conf di /etc/nginx/conf.d/. Di Ubuntu dan Debian",
                    "susunannya sedikit beda: berkas situs ditaruh di sites-available lalu",
                    "ditautkan ke sites-enabled.",
                ],
            },
            {
                "heading": "Memasang dan menyalakan",
                "bahasa": "terminal",
                "code": """sudo dnf install nginx
sudo systemctl enable --now nginx
curl -I http://localhost/          # harus menjawab 200 OK

sudo nginx -t                      # periksa konfigurasi sebelum dipakai
sudo systemctl reload nginx        # pakai konfigurasi baru tanpa memutus koneksi
sudo tail -f /var/log/nginx/error.log""",
            },
            {
                "heading": "Menyajikan situs statis",
                "bahasa": "nginx",
                "code": """server {
    listen 80;
    server_name toko.id www.toko.id;

    root /srv/toko/public;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}""",
            },
            {
                "body": [
                    "Konfigurasi Nginx tersusun dari direktif yang diakhiri titik koma, dan",
                    "blok yang dibungkus kurung kurawal:",
                    "  - server adalah satu situs. Nginx memilih blok server berdasarkan",
                    "    port dan header Host yang dikirim browser, jadi satu Nginx bisa",
                    "    melayani banyak domain sekaligus.",
                    "  - root menunjuk folder berkasnya. Permintaan /gaya.css dicari di",
                    "    /srv/toko/public/gaya.css.",
                    "  - location memilih aturan berdasarkan jalur di URL. Urutan",
                    "    pencocokannya punya aturan sendiri yang dibahas di materi",
                    "    berikutnya.",
                    "  - try_files mencoba beberapa kemungkinan berurutan. Di sini: berkas",
                    "    persis, lalu folder, lalu kalau dua-duanya nggak ada, jawab 404.",
                    "",
                    "Untuk aplikasi satu halaman (React, Vue) yang mengatur rute sendiri di",
                    "browser, ganti =404 dengan /index.html. Dengan begitu alamat seperti",
                    "/produk/12 tetap dilayani index.html, dan router di browser yang",
                    "menentukan halaman mana yang tampil.",
                    "",
                    "Jebakan: tanda titik koma yang hilang. nginx -t akan menolak",
                    "konfigurasinya dan menyebut baris yang salah. Biasakan menjalankan",
                    "nginx -t sebelum reload. Kalau konfigurasi yang rusak telanjur di-reload,",
                    "Nginx menolaknya dan tetap memakai konfigurasi lama, tapi kalau kamu",
                    "memakai restart, Nginx bisa mati sama sekali.",
                ],
            },
            {
                "heading": "Meneruskan ke aplikasi",
                "bahasa": "nginx",
                "code": """server {
    listen 80;
    server_name toko.id;

    location /static/ {
        root /srv/toko;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}""",
            },
            {
                "body": [
                    "Sekarang aplikasimu cukup mendengarkan di 127.0.0.1:8000, dan port itu",
                    "nggak perlu dibuka ke internet. Berkas di /static/ disajikan Nginx",
                    "langsung dari /srv/toko/static, sisanya diteruskan ke aplikasi.",
                    "",
                    "Empat baris proxy_set_header itu penting. Dari sudut pandang aplikasi,",
                    "semua permintaan sekarang datang dari Nginx di 127.0.0.1. Tanpa header",
                    "tambahan, aplikasimu nggak tahu domain apa yang diminta, alamat asli",
                    "pengunjungnya, atau apakah pengunjung memakai HTTPS. Framework seperti",
                    "Flask dan Django punya pengaturan untuk membaca header X-Forwarded ini.",
                    "",
                    "Dua kode error yang sering muncul dari reverse proxy:",
                    "  - 502 Bad Gateway: Nginx gagal menghubungi aplikasinya. Biasanya",
                    "    aplikasinya mati, salah port, atau ditolak SELinux.",
                    "  - 504 Gateway Timeout: aplikasinya terhubung tapi terlalu lama",
                    "    menjawab. Batas bawaannya 60 detik, diatur dengan",
                    "    proxy_read_timeout.",
                    "",
                    "Jebakan khusus Fedora dan keluarga Red Hat: SELinux melarang Nginx",
                    "membuka koneksi jaringan ke port aplikasi. Gejalanya 502, dan di",
                    "error.log tertulis Permission denied while connecting to upstream.",
                    "Jangan matikan SELinux. Izinkan dengan",
                    "sudo setsebool -P httpd_can_network_connect 1.",
                ],
            },
            {
                "heading": "Menghitung kode status dari log akses",
                "code": "from collections import Counter\n\nakses = \"\"\"\\\n203.0.113.5 - - [19/Oct/2026:08:01:12 +0700] \"GET / HTTP/1.1\" 200 5120 \"-\" \"Mozilla/5.0\"\n203.0.113.5 - - [19/Oct/2026:08:01:13 +0700] \"GET /gaya.css HTTP/1.1\" 200 1830 \"-\" \"Mozilla/5.0\"\n198.51.100.9 - - [19/Oct/2026:08:02:40 +0700] \"GET /api/produk HTTP/1.1\" 502 157 \"-\" \"curl/8.15.0\"\n198.51.100.9 - - [19/Oct/2026:08:02:41 +0700] \"GET /api/produk HTTP/1.1\" 502 157 \"-\" \"curl/8.15.0\"\n192.0.2.33 - - [19/Oct/2026:08:03:05 +0700] \"GET /lama.html HTTP/1.1\" 404 153 \"-\" \"Mozilla/5.0\"\n\"\"\"\n\nstatus = Counter()\nfor baris in akses.splitlines():\n    permintaan = baris.split('\"')[1]\n    kode = baris.split('\"')[2].split()[0]\n    status[kode] += 1\n    if kode.startswith(\"5\"):\n        print(\"perlu dicek:\", kode, permintaan)\n\nfor kode in sorted(status):\n    print(kode, status[kode], \"kali\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  perlu dicek: 502 GET /api/produk HTTP/1.1",
                    "  perlu dicek: 502 GET /api/produk HTTP/1.1",
                    "  200 2 kali",
                    "  404 1 kali",
                    "  502 2 kali",
                    "",
                    "Baris-baris itu meniru format log akses bawaan Nginx, yang tersimpan di",
                    "/var/log/nginx/access.log. Tiap baris memuat alamat pengunjung, waktu,",
                    "permintaan, kode status, ukuran jawaban, dan nama browser. Kode 5xx",
                    "berarti masalah di sisi server, dan itu yang pertama kamu cari kalau",
                    "ada keluhan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Susunan \"Nginx di depan, aplikasi di belakang\" dipakai di VPS kecil",
                    "sampai server perusahaan, untuk aplikasi PHP, Python, Node.js, maupun",
                    "Java. Image container resmi nginx di Docker Hub juga sering dipakai",
                    "untuk menyajikan hasil build aplikasi React atau Vue.",
                    "",
                    "Kasus kecil: aplikasi Django di server Rocky Linux jalan di",
                    "127.0.0.1:8000 lewat systemd. Kamu menambahkan blok server dengan",
                    "proxy_pass ke sana, tapi browser menampilkan 502 Bad Gateway.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan aplikasinya hidup: curl http://127.0.0.1:8000 dari",
                    "     server itu. Kalau berhasil, masalahnya di antara Nginx dan",
                    "     aplikasi.",
                    "  2. Baca /var/log/nginx/error.log. Di sana tertulis",
                    "     (13: Permission denied) while connecting to upstream.",
                    "  3. Pesan Permission denied di Rocky hampir selalu SELinux. Izinkan",
                    "     Nginx menghubungi aplikasi:",
                    "       sudo setsebool -P httpd_can_network_connect 1",
                    "  4. Muat ulang halamannya. Kalau sekarang tampil tapi CSS-nya hilang,",
                    "     tambahkan location /static/ yang menunjuk folder hasil",
                    "     collectstatic, lalu nginx -t dan reload.",
                ],
            },
        ],
    },
    {
        "title": "7. Nginx Lanjutan: HTTPS, location, dan Load Balancing",
        "sections": [
            {
                "body": [
                    "Situs yang masih memakai HTTP polos ditandai \"Not secure\" oleh browser,",
                    "dan semua yang dikirim pengunjungnya, termasuk password, bisa dibaca",
                    "siapa pun yang berada di jaringan yang sama. Materi ini membahas tiga",
                    "hal yang hampir selalu dibutuhkan sesudah Nginx pertamamu jalan:",
                    "memasang HTTPS, memahami location mana yang dipilih Nginx, dan membagi",
                    "beban ke beberapa server aplikasi.",
                ],
            },
            {
                "heading": "TLS dan sertifikat",
                "body": [
                    "HTTPS adalah HTTP yang dibungkus TLS (Transport Layer Security). TLS",
                    "melakukan dua hal: mengenkripsi koneksi supaya isinya nggak bisa dibaca",
                    "di jalan, dan membuktikan bahwa server yang kamu hubungi memang pemilik",
                    "domain itu. Versi terbarunya TLS 1.3, dibakukan di RFC 8446 pada Agustus",
                    "2018. Nama lama TLS adalah SSL, dan orang masih sering bilang \"pasang",
                    "SSL\" walaupun yang dipasang TLS.",
                    "",
                    "Bukti kepemilikan domain itu berupa sertifikat X.509. Isinya nama",
                    "domain, kunci publik server, masa berlaku, dan tanda tangan dari CA",
                    "(certificate authority), yaitu lembaga yang dipercaya browser. Browser",
                    "memeriksa rantainya: sertifikat situs ditandatangani CA perantara, dan",
                    "CA perantara ditandatangani CA akar yang sudah tertanam di browser.",
                    "",
                    "Detail kriptografinya dibahas di kurikulum Keamanan Siber. Di sini",
                    "cukup tahu cara mendapatkan sertifikat dan memasangnya.",
                ],
            },
            {
                "heading": "Let's Encrypt dan Certbot",
                "body": [
                    "Let's Encrypt adalah CA gratis yang dijalankan lembaga nirlaba Internet",
                    "Security Research Group. Sertifikatnya diminta dan diperbarui otomatis",
                    "lewat protokol ACME. Program klien resminya Certbot, buatan Electronic",
                    "Frontier Foundation, yang bisa sekalian menyunting konfigurasi Nginx",
                    "untukmu.",
                    "",
                    "Waktu kamu meminta sertifikat, Let's Encrypt perlu bukti bahwa kamu",
                    "menguasai domainnya. Cara yang paling umum, tantangan HTTP-01, meminta",
                    "servermu menyajikan sebuah token di alamat",
                    "http://domainmu/.well-known/acme-challenge/. Karena itu port 80 harus",
                    "terbuka dan record DNS-nya sudah menunjuk ke server itu. Untuk",
                    "sertifikat wildcard seperti *.toko.id, dipakai tantangan DNS-01: kamu",
                    "membuktikan kepemilikan lewat record TXT.",
                ],
            },
            {
                "heading": "Meminta sertifikat dengan Certbot",
                "bahasa": "terminal",
                "code": """sudo dnf install certbot python3-certbot-nginx
sudo certbot --nginx -d toko.id -d www.toko.id
sudo certbot renew --dry-run           # uji perpanjangan tanpa benar-benar memperpanjang
systemctl list-timers | grep certbot   # pastikan timer perpanjangan otomatis aktif""",
            },
            {
                "body": [
                    "Masa berlaku sertifikat Let's Encrypt saat ini 90 hari, dan akan terus",
                    "memendek. Pada 7 Oktober 2026 Let's Encrypt mengumumkan sertifikat",
                    "64 hari mulai Februari 2027, sebagai langkah menuju 45 hari. Di tingkat",
                    "industri, CA/Browser Forum memutuskan masa berlaku sertifikat publik",
                    "menyusut bertahap sampai 47 hari pada 2029. Let's Encrypt juga sudah",
                    "berhenti mengirim email pengingat kedaluwarsa sejak Juni 2025.",
                    "",
                    "Artinya perpanjangan manual sudah nggak masuk akal. Certbot memasang",
                    "timer systemd yang mencoba memperpanjang dua kali sehari. Di sebagian",
                    "distro timer itu perlu dinyalakan sendiri, jadi selalu cek dengan",
                    "systemctl list-timers sesudah memasang Certbot.",
                ],
            },
            {
                "heading": "Konfigurasi HTTPS yang umum",
                "bahasa": "nginx",
                "code": """server {
    listen 80;
    server_name toko.id www.toko.id;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    http2 on;
    server_name toko.id www.toko.id;

    ssl_certificate     /etc/letsencrypt/live/toko.id/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/toko.id/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    add_header Strict-Transport-Security "max-age=31536000" always;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}""",
            },
            {
                "body": [
                    "Blok pertama mengalihkan semua permintaan HTTP ke HTTPS dengan kode",
                    "301. Blok kedua melayani HTTPS. fullchain.pem berisi sertifikat situs",
                    "plus CA perantaranya. Kalau yang dipasang cuma sertifikat situs, browser",
                    "di laptop mungkin tetap lancar, tapi aplikasi ponsel dan curl bisa",
                    "menolak karena rantainya putus.",
                    "",
                    "Header Strict-Transport-Security (HSTS) menyuruh browser selalu memakai",
                    "HTTPS untuk domain ini selama setahun, bahkan kalau pengguna mengetik",
                    "http://. Pasang sesudah HTTPS-mu yakin stabil, karena browser akan",
                    "mengingatnya.",
                ],
            },
            {
                "heading": "Urutan Nginx memilih location",
                "body": [
                    "Satu permintaan cuma dilayani satu blok location. Kalau ada beberapa",
                    "yang cocok, Nginx memilih dengan urutan ini:",
                    "",
                    "  Bentuk                Arti                       Kapan dipilih",
                    "  location = /x         jalur persis /x            langsung, kalau persis sama",
                    "  location ^~ /x/       awalan, tanpa cek regex    kalau ia awalan terpanjang",
                    "  location ~ pola       regex, peka huruf          regex pertama yang cocok,",
                    "  location ~* pola      regex, tidak peka huruf    sesuai urutan di berkas",
                    "  location /x/          awalan biasa               awalan terpanjang, kalau",
                    "                                                   tidak ada regex yang cocok",
                    "",
                    "Langkahnya:",
                    "  1. Cari location = yang persis sama. Kalau ada, selesai.",
                    "  2. Cari awalan terpanjang di antara semua location awalan (yang biasa",
                    "     maupun ^~). Ingat yang terpanjang itu.",
                    "  3. Kalau awalan terpanjang tadi bertanda ^~, pakai itu. Selesai.",
                    "  4. Periksa location regex satu per satu sesuai urutan tulisnya.",
                    "     Regex pertama yang cocok dipakai.",
                    "  5. Kalau nggak ada regex yang cocok, pakai awalan terpanjang dari",
                    "     langkah 2.",
                    "",
                    "Urutan tulis cuma berpengaruh untuk regex. Untuk awalan, yang dipilih",
                    "selalu yang terpanjang, di mana pun ia ditulis. Contohnya, dengan",
                    "location /static/ dan location ~* \\.(png|jpg)$, permintaan",
                    "/static/logo.png dilayani blok regex, karena regex diperiksa sesudah",
                    "awalan. Kalau maksudmu semua di bawah /static/ dilayani blok awalan,",
                    "tulis location ^~ /static/.",
                    "",
                    "Latihan kedua bab ini memintamu menulis pencocok location yang",
                    "mengikuti kelima langkah tadi.",
                ],
            },
            {
                "heading": "Membagi beban ke beberapa server",
                "bahasa": "nginx",
                "code": """upstream aplikasi {
    server 10.0.1.11:8000 weight=5;
    server 10.0.1.12:8000;
    server 10.0.1.13:8000 max_fails=3 fail_timeout=30s;
    server 10.0.1.14:8000 backup;
}

server {
    listen 443 ssl;
    server_name toko.id;
    # ... baris sertifikat seperti di atas ...

    location / {
        proxy_pass http://aplikasi;
    }
}""",
            },
            {
                "body": [
                    "Load balancer membagi permintaan ke beberapa server supaya nggak ada",
                    "satu server yang kewalahan, dan supaya situs tetap hidup kalau satu",
                    "server mati. Nginx bisa jadi load balancer lewat blok upstream.",
                    "",
                    "Cara membaginya:",
                    "  - Round robin, bawaan: giliran satu per satu. weight=5 membuat server",
                    "    itu dapat lima kali lebih banyak giliran.",
                    "  - least_conn: kirim ke server yang sedang paling sedikit koneksinya.",
                    "    Cocok kalau lama tiap permintaan beda-beda jauh.",
                    "  - ip_hash: pengunjung yang sama selalu ke server yang sama. Dipakai",
                    "    aplikasi lama yang menyimpan sesi login di memori server.",
                    "",
                    "max_fails dan fail_timeout adalah health check pasif: kalau sebuah",
                    "server gagal menjawab tiga kali, Nginx berhenti mengirim ke sana selama",
                    "30 detik. backup cuma dipakai kalau semua server lain tumbang.",
                    "Pemeriksaan aktif, yaitu menghubungi server secara berkala walaupun",
                    "nggak ada pengunjung, adalah fitur versi berbayar Nginx Plus. Di versi",
                    "gratis, HAProxy atau load balancer dari cloud biasanya mengambil peran",
                    "itu.",
                    "",
                    "Load balancer seperti ini bekerja di L7, karena ia membaca permintaan",
                    "HTTP. Ada juga load balancer L4 yang cuma meneruskan koneksi TCP tanpa",
                    "membaca isinya. Nginx bisa melakukannya lewat blok stream, misalnya",
                    "untuk membagi koneksi database.",
                ],
            },
            {
                "heading": "Round robin berbobot ala Nginx",
                "code": """# Weighted round robin "halus" seperti yang dipakai Nginx.
server = {"app1": 5, "app2": 1, "app3": 1}
skor = {nama: 0 for nama in server}
total = sum(server.values())

urutan = []
for _ in range(7):
    for nama, bobot in server.items():
        skor[nama] += bobot
    terpilih = max(skor, key=skor.get)
    skor[terpilih] -= total
    urutan.append(terpilih)

print(" ".join(urutan))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  app1 app1 app2 app1 app3 app1 app1",
                    "",
                    "Dalam tujuh giliran, app1 dapat lima dan sisanya masing-masing satu,",
                    "sesuai bobotnya. Yang menarik adalah urutannya. Cara naif akan",
                    "mengirim lima permintaan berturut-turut ke app1, lalu satu ke app2, dan",
                    "satu ke app3. Algoritma ini menyelipkan app2 dan app3 di tengah, supaya",
                    "app1 nggak menerima lonjakan beruntun.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang ramai saat promo tanggal kembar biasanya menjalankan",
                    "beberapa server aplikasi di belakang satu load balancer, entah Nginx,",
                    "HAProxy, atau load balancer dari penyedia cloud. HTTPS-nya dipasang di",
                    "load balancer itu, dan server aplikasinya cuma menerima HTTP dari",
                    "jaringan internal.",
                    "",
                    "Kasus kecil: situs toko.id baru dipasang HTTPS dengan Certbot. Tiga",
                    "bulan kemudian pelanggan melapor browser menampilkan peringatan",
                    "sertifikat kedaluwarsa. Di saat yang sama, gambar produk di",
                    "/static/produk/ ikut kena aturan cache regex yang salah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek masa berlaku dengan sudo certbot certificates. Sertifikatnya",
                    "     memang sudah lewat 90 hari.",
                    "  2. Jalankan systemctl list-timers | grep certbot. Timernya ternyata",
                    "     nggak aktif, jadi perpanjangan otomatis nggak pernah jalan.",
                    "     Nyalakan timernya dengan systemctl enable --now, lalu jalankan",
                    "     sudo certbot renew sekali.",
                    "  3. Uji dengan sudo certbot renew --dry-run supaya yakin perpanjangan",
                    "     berikutnya berhasil tanpa campur tangan.",
                    "  4. Untuk gambar, ganti location /static/ jadi location ^~ /static/",
                    "     supaya regex nggak diperiksa lagi, lalu nginx -t dan reload.",
                ],
            },
        ],
    },
    {
        "title": "8. Peta Web Server, VPN, dan Email untuk Server",
        "sections": [
            {
                "body": [
                    "Nginx bukan satu-satunya pilihan. Di pekerjaan kamu bakal mewarisi",
                    "server yang memakai Apache, homelab teman yang memakai Caddy, atau",
                    "klaster yang memakai Traefik. Materi ini peta singkat: apa saja",
                    "alternatifnya, kapan masing-masing cocok, dan statusnya sekarang. Di",
                    "bagian akhir ada dua urusan server yang sering muncul bersamaan: VPN",
                    "untuk akses jarak jauh, dan email supaya pesan dari aplikasimu nggak",
                    "masuk folder spam.",
                    "",
                    "Versi yang disebut di sini adalah yang terbaru saat materi ini ditulis",
                    "(Oktober 2026).",
                ],
            },
            {
                "heading": "Web server dan reverse proxy lain",
                "body": [
                    "  Nama      Versi terbaru      Lisensi      Status",
                    "  Nginx     1.30.6 / 1.31.7    BSD          aktif, paling umum",
                    "  Apache    2.4.69             Apache-2.0   stabil-matang",
                    "  Caddy     2.11.7             Apache-2.0   aktif",
                    "  Traefik   3.7.15             MIT          aktif",
                    "  HAProxy   3.4 (LTS)          GPL-2.0      aktif",
                    "  IIS       10.0               proprietary  menurun",
                    "",
                    "Apache HTTP Server (paket httpd di Fedora) adalah web server tertua",
                    "yang masih dipakai luas. Kelebihannya berkas .htaccess: pengaturan per",
                    "folder yang bisa diubah tanpa menyentuh konfigurasi utama. Karena itu",
                    "Apache jadi andalan hosting bersama dengan cPanel, aplikasi PHP lama,",
                    "dan WordPress. Proyek baru cenderung memilih Nginx atau Caddy.",
                    "",
                    "Caddy terkenal karena HTTPS-nya otomatis. Begitu kamu menulis nama",
                    "domain, Caddy sendiri yang meminta dan memperbarui sertifikat Let's",
                    "Encrypt. Konfigurasi reverse proxy lengkapnya cuma tiga baris:",
                    "",
                    "  toko.id {",
                    "      reverse_proxy 127.0.0.1:8000",
                    "  }",
                    "",
                    "Itu yang membuat Caddy pilihan bagus untuk proyek pribadi dan homelab.",
                    "",
                    "Traefik membaca konfigurasinya dari tempat lain, misalnya label di",
                    "container Docker atau objek di Kubernetes. Begitu container baru dengan",
                    "label yang tepat menyala, Traefik langsung membuat rutenya tanpa perlu",
                    "disunting. Traefik juga jadi ingress bawaan k3s, distribusi Kubernetes",
                    "ringan yang dibahas di bab Kubernetes.",
                    "",
                    "HAProxy adalah load balancer dan proxy TCP/HTTP yang fokus ke kinerja.",
                    "Cabang 3.4 adalah versi LTS yang dirilis Juni 2026 dan didukung sampai",
                    "2031. Pilih HAProxy kalau tugas utamanya membagi beban, termasuk koneksi",
                    "TCP non-HTTP seperti database.",
                    "",
                    "Internet Information Services (IIS) adalah web server bawaan Windows",
                    "Server. Kamu cuma akan menemuinya di aplikasi ASP.NET lama. Aplikasi",
                    ".NET modern biasanya jalan di server Kestrel bawaan .NET, di dalam",
                    "container Linux.",
                ],
            },
            {
                "heading": "Contoh label Traefik di Compose",
                "bahasa": "yaml",
                "code": """services:
  traefik:
    image: traefik:v3.7
    command:
      - --providers.docker=true
      - --entrypoints.web.address=:80
    ports:
      - "80:80"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro

  toko:
    image: ghcr.io/contoh/toko:1.4.0
    labels:
      - traefik.http.routers.toko.rule=Host(`toko.id`)
      - traefik.http.services.toko.loadbalancer.server.port=8000""",
            },
            {
                "body": [
                    "Berkas di atas memakai Docker Compose, yang dibahas di bab 04. Untuk",
                    "sekarang cukup perhatikan bagian labels: rute toko.id ditulis di",
                    "samping layanannya sendiri, bukan di berkas konfigurasi proxy. Itu ciri",
                    "khas Traefik.",
                    "",
                    "Jebakan: memberi Traefik akses ke /var/run/docker.sock sama dengan",
                    "memberi kendali penuh atas Docker di mesin itu. Pemasangan serius",
                    "memakai proxy socket yang cuma mengizinkan pembacaan.",
                ],
            },
            {
                "heading": "VPN untuk akses jarak jauh",
                "body": [
                    "VPN (virtual private network) menyambungkan perangkat lewat internet",
                    "seolah mereka ada di jaringan lokal yang sama, dengan koneksi",
                    "terenkripsi. Di DevOps, VPN dipakai supaya panel admin, database, dan",
                    "SSH nggak perlu dibuka ke internet.",
                    "",
                    "  Nama        Versi terbaru   Cara kerja",
                    "  WireGuard   ikut kernel     protokol VPN ringkas di kernel Linux",
                    "  OpenVPN     2.7.8           VPN berbasis TLS, sudah lama dipakai",
                    "  Tailscale   1.104.1         mesh VPN di atas WireGuard, tanpa buka port",
                    "  ZeroTier    1.16.2          jaringan virtual peer-to-peer",
                    "",
                    "WireGuard sudah jadi bagian kernel Linux sejak versi 5.6 (2020).",
                    "Konfigurasinya pendek: tiap perangkat punya pasangan kunci, dan kamu",
                    "menulis kunci publik lawan bicaranya beserta alamat yang boleh lewat.",
                    "OpenVPN lebih tua dan masih banyak di VPN perusahaan, tapi WireGuard",
                    "lebih cepat dan lebih sederhana untuk dipasang baru.",
                    "",
                    "Tailscale membangun jaringan mesh di atas WireGuard. Kamu login di",
                    "setiap perangkat, dan semuanya bisa saling menghubungi tanpa membuka",
                    "port apa pun di router. Klien Tailscale open source, tapi server",
                    "koordinasinya milik Tailscale. Ada paket gratis untuk pemakaian",
                    "pribadi, dan Headscale adalah alternatif server koordinasi yang bisa",
                    "dipasang sendiri. ZeroTier menawarkan hal serupa dengan pendekatan",
                    "jaringan virtual seperti satu LAN.",
                ],
            },
            {
                "heading": "Email dari aplikasi",
                "body": [
                    "Aplikasi hampir selalu perlu mengirim email: reset password,",
                    "konfirmasi pesanan, notifikasi. Protokolnya:",
                    "  - SMTP untuk mengirim. Antarserver email memakai port 25, sedangkan",
                    "    aplikasi mengirim lewat port 587 atau 465, keduanya terenkripsi.",
                    "  - IMAP (port 993) dan POP3 (port 995) untuk mengambil email dari",
                    "    kotak masuk. Aplikasi jarang membutuhkannya.",
                    "",
                    "Mengirim email itu gampang. Yang susah adalah membuat email itu",
                    "diterima dan nggak masuk spam. Penerima seperti Gmail memeriksa tiga",
                    "record DNS di domain pengirim:",
                    "",
                    "  Record   Isinya",
                    "  SPF      daftar server yang boleh mengirim email atas nama domainmu",
                    "  DKIM     kunci publik untuk memeriksa tanda tangan di setiap email",
                    "  DMARC    apa yang harus dilakukan penerima kalau SPF dan DKIM gagal,",
                    "           dan ke mana laporan dikirim",
                    "",
                    "Sejak Februari 2024, Google dan Yahoo mewajibkan ketiganya untuk",
                    "pengirim email massal. Domain yang belum memasang ketiga record itu",
                    "sekarang gampang sekali masuk spam.",
                    "",
                    "Menjalankan server email sendiri jarang sepadan dengan repotnya.",
                    "Banyak penyedia cloud juga membatasi koneksi keluar ke port 25 secara",
                    "bawaan. Kebanyakan tim memakai layanan pengirim seperti Amazon SES atau",
                    "SendGrid, lalu memasang record SPF dan tanda tangan yang mereka berikan.",
                ],
            },
            {
                "heading": "Membaca record SPF dan DMARC",
                "code": """catatan = {
    "toko.id": "v=spf1 include:_spf.google.com include:amazonses.com ~all",
    "_dmarc.toko.id": "v=DMARC1; p=quarantine; rua=mailto:dmarc@toko.id; pct=100",
}


def urai_dmarc(teks):
    hasil = {}
    for bagian in teks.split(";"):
        kunci, _, nilai = bagian.strip().partition("=")
        if kunci:
            hasil[kunci] = nilai
    return hasil


spf = catatan["toko.id"].split()
print("SPF mengizinkan:", ", ".join(s[8:] for s in spf if s.startswith("include:")))
print("SPF untuk yang lain:", spf[-1])

dmarc = urai_dmarc(catatan["_dmarc.toko.id"])
print("Kebijakan DMARC:", dmarc["p"])
print("Laporan dikirim ke:", dmarc["rua"])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  SPF mengizinkan: _spf.google.com, amazonses.com",
                    "  SPF untuk yang lain: ~all",
                    "  Kebijakan DMARC: quarantine",
                    "  Laporan dikirim ke: mailto:dmarc@toko.id",
                    "",
                    "Kedua record itu berjenis TXT. SPF ditaruh di nama domain itu sendiri,",
                    "kebijakan penerima di nama _dmarc. ~all artinya server lain yang",
                    "nggak terdaftar dianggap mencurigakan, sedangkan -all menolak mereka",
                    "mentah-mentah. p=quarantine menyuruh penerima memasukkan email yang",
                    "gagal ke folder spam. Pilihan lainnya none (cuma kirim laporan) dan",
                    "reject (tolak).",
                    "",
                    "Ingat: domain cuma boleh punya satu record SPF. Kalau kamu memakai dua",
                    "layanan pengirim, gabungkan keduanya dalam satu record dengan dua",
                    "include, seperti contoh di atas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online dan aplikasi SaaS hampir selalu mengirim email transaksional",
                    "lewat layanan pengirim khusus, sementara email kantor",
                    "memakai Google Workspace atau Microsoft 365. Keduanya harus tercantum",
                    "di record SPF yang sama.",
                    "",
                    "Kasus kecil: email reset password dari aplikasi toko.id selalu masuk",
                    "folder spam di Gmail. Aplikasinya mengirim lewat layanan Amazon,",
                    "sedangkan email kantornya memakai Google Workspace.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka salah satu email yang masuk spam di Gmail, pilih \"Show",
                    "     original\", lalu lihat hasil ketiga pemeriksaannya. Di kasus ini",
                    "     SPF gagal untuk server milik Amazon.",
                    "  2. Cek record SPF dengan dig toko.id TXT. Isinya cuma",
                    "     include:_spf.google.com, jadi server Amazon belum diizinkan.",
                    "  3. Ganti jadi satu record yang memuat keduanya:",
                    "       v=spf1 include:_spf.google.com include:amazonses.com ~all",
                    "  4. Pasang record tanda tangan dari panel layanan Amazon, lalu tambah",
                    "     record kebijakan di _dmarc.toko.id dengan p=none dulu. Baca",
                    "     laporannya beberapa hari, dan naikkan ke quarantine kalau sudah",
                    "     nggak ada pengirim sah yang gagal.",
                ],
            },
        ],
    },
    {
        "title": "9. Container dan Image: Kenapa Docker Ada",
        "sections": [
            {
                "body": [
                    "\"Di laptopku jalan kok.\" Kalimat ini muncul setiap kali aplikasi yang",
                    "lancar di laptop pengembang ternyata error di server. Penyebabnya",
                    "hampir selalu perbedaan lingkungan: versi Python yang beda, pustaka",
                    "sistem yang belum terpasang, variabel lingkungan yang lupa diisi, atau",
                    "berkas konfigurasi yang cuma ada di laptop.",
                    "",
                    "Docker memecahkan masalah itu dengan membungkus aplikasi beserta semua",
                    "kebutuhannya jadi satu paket yang disebut image. Image yang sama",
                    "dijalankan di laptop, di server tes, dan di server produksi, jadi",
                    "lingkungannya ikut sama.",
                ],
            },
            {
                "heading": "Container itu apa, dan bedanya dengan VM",
                "body": [
                    "Image yang sedang dijalankan disebut container. Container adalah proses",
                    "biasa di Linux yang dikurung: ia cuma bisa melihat berkas, jaringan,",
                    "dan proses miliknya sendiri, dan jatah CPU serta memorinya bisa",
                    "dibatasi. Pengurungan itu dikerjakan dua fitur kernel Linux, yaitu",
                    "namespaces (membatasi apa yang terlihat) dan cgroups (membatasi berapa",
                    "banyak sumber daya yang boleh dipakai).",
                    "",
                    "Bandingkan dengan mesin virtual (VM). VM meniru satu komputer utuh,",
                    "lengkap dengan kernel sistem operasinya sendiri. Container nggak punya",
                    "kernel sendiri; semua container di satu mesin memakai kernel milik",
                    "mesin itu.",
                    "",
                    "  Hal            VM                         Container",
                    "  Kernel         punya sendiri              memakai kernel host",
                    "  Waktu nyala    puluhan detik sampai menit kurang dari satu detik",
                    "  Ukuran         gigabyte                   megabyte sampai ratusan MB",
                    "  Isolasi        lebih kuat                 cukup, tapi berbagi kernel",
                    "  Cocok untuk    OS berbeda, isolasi ketat  aplikasi dan layanannya",
                    "",
                    "Karena berbagi kernel, container Linux butuh kernel Linux. Di Windows",
                    "dan macOS, Docker Desktop menjalankan satu VM Linux kecil di belakang",
                    "layar, dan semua container hidup di dalam VM itu.",
                ],
            },
            {
                "heading": "Image, container, dan registry",
                "body": [
                    "Tiga istilah ini dipakai terus di bab ini:",
                    "  - Image: cetakan yang hanya bisa dibaca. Isinya sistem berkas mini",
                    "    (misalnya Debian dengan Python), kode aplikasimu, dan perintah yang",
                    "    dijalankan saat container menyala.",
                    "  - Container: satu salinan image yang sedang hidup. Dari satu image",
                    "    kamu bisa menjalankan sepuluh container sekaligus. Perubahan yang",
                    "    terjadi di dalam container nggak mengubah image-nya.",
                    "  - Registry: gudang tempat image disimpan dan dibagikan. Yang paling",
                    "    besar Docker Hub, yang menyimpan image resmi seperti nginx,",
                    "    postgres, dan python. Registry dibahas lebih rinci di bab 04.",
                    "",
                    "Perumpamaannya: image itu resep yang sudah dicetak, container itu kue",
                    "yang dibuat dari resep itu. Satu resep bisa dipakai bikin banyak kue,",
                    "dan kue yang digigit nggak mengubah resepnya.",
                ],
            },
            {
                "heading": "Container pertamamu",
                "bahasa": "terminal",
                "code": """docker run hello-world                  # tarik image, jalankan, selesai
docker run -d --name web -p 8080:80 nginx:1.30
docker ps                               # container yang sedang hidup
curl http://localhost:8080/             # halaman sambutan Nginx
docker logs web                         # keluaran container
docker exec -it web sh                  # masuk ke shell di dalam container
docker stop web                         # hentikan
docker rm web                           # hapus containernya
docker images                           # image yang tersimpan lokal""",
            },
            {
                "body": [
                    "Perintah kedua yang paling banyak isinya:",
                    "  - -d menjalankan container di latar belakang.",
                    "  - --name web memberi nama supaya gampang dirujuk.",
                    "  - -p 8080:80 menyambungkan port 8080 di mesinmu ke port 80 di dalam",
                    "    container. Nginx di dalam container mendengarkan di port 80, tapi",
                    "    dari luar kamu mengaksesnya lewat 8080. Ini sambungan langsung ke",
                    "    materi port di bab 02: tanpa -p, Nginx tetap jalan, tapi nggak ada",
                    "    pintu dari luar ke sana.",
                    "  - nginx:1.30 adalah nama image dan tag-nya. Tag menunjuk versi. Kalau",
                    "    tag nggak ditulis, Docker memakai latest.",
                    "",
                    "docker stop mengirim sinyal SIGTERM supaya aplikasi berhenti dengan",
                    "rapi, lalu SIGKILL kalau sesudah 10 detik aplikasinya belum berhenti.",
                    "docker rm menghapus containernya, termasuk semua yang tertulis di",
                    "dalamnya. Data yang perlu disimpan harus ditaruh di volume, yang",
                    "dibahas di materi Volume, Jaringan, dan Image Docker yang Aman.",
                ],
            },
            {
                "heading": "Keadaan sebuah container",
                "code": """# Perintah docker yang sah untuk tiap keadaan container.
TRANSISI = {
    ("created", "start"): "running",
    ("running", "pause"): "paused",
    ("paused", "unpause"): "running",
    ("running", "stop"): "exited",
    ("exited", "start"): "running",
    ("exited", "rm"): "dihapus",
    ("created", "rm"): "dihapus",
}

keadaan = "created"
for perintah in ["start", "pause", "unpause", "rm", "stop", "rm"]:
    baru = TRANSISI.get((keadaan, perintah))
    if baru is None:
        print(f"{perintah:<8} ditolak: container sedang {keadaan}")
        continue
    print(f"{perintah:<8} {keadaan} -> {baru}")
    keadaan = baru""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  start    created -> running",
                    "  pause    running -> paused",
                    "  unpause  paused -> running",
                    "  rm       ditolak: container sedang running",
                    "  stop     running -> exited",
                    "  rm       exited -> dihapus",
                    "",
                    "Program ini meniru siklus hidup container. docker ps -a menampilkan",
                    "keadaan ini di kolom status. Container yang sedang running nggak bisa",
                    "dihapus begitu saja. Docker menolak dengan pesan yang menyuruhmu",
                    "menghentikannya dulu, atau memakai docker rm -f untuk memaksa.",
                ],
            },
            {
                "heading": "Docker Engine, Docker Desktop, dan Fedora",
                "body": [
                    "Docker Engine adalah mesin intinya: program dockerd yang jalan di latar",
                    "belakang, ditambah perintah docker yang kamu ketik. Kodenya open source",
                    "(proyek Moby, lisensi Apache-2.0). Saat materi ini ditulis, versi",
                    "terbarunya 29.9.1, dirilis 14 Oktober 2026.",
                    "",
                    "Docker Desktop adalah aplikasi grafis untuk Windows, macOS, dan Linux",
                    "yang membungkus Docker Engine di dalam VM, plus Compose dan Kubernetes",
                    "lokal. Versi terbarunya 4.95.0 (12 Oktober 2026). Lisensinya beda:",
                    "gratis untuk pribadi, pendidikan, open source nonkomersial, dan usaha",
                    "kecil (di bawah 250 karyawan dan di bawah US$10 juta pendapatan per",
                    "tahun). Perusahaan yang lebih besar wajib berlangganan.",
                    "",
                    "Di Linux, termasuk Fedora, pakai Docker Engine langsung atau Podman.",
                    "Docker Desktop di Linux menjalankan VM terpisah, jadi image yang kamu",
                    "bangun di sana nggak kelihatan dari Docker Engine di mesin yang sama.",
                    "Fedora sendiri memasang Podman sebagai bawaan. Perintahnya hampir sama",
                    "dengan docker, dan dibahas di bab 04.",
                    "",
                    "Di Survei Stack Overflow 2026, Docker (digabung dengan Docker Compose)",
                    "dipakai 59,1% responden kategori pengembangan cloud, peringkat pertama",
                    "di kategorinya.",
                ],
            },
            {
                "heading": "Kesalahan yang sering terjadi",
                "body": [
                    "Jebakan: menganggap container seperti VM kecil, lalu menyimpan data",
                    "penting di dalamnya. Begitu container dihapus dan dibuat ulang, misalnya",
                    "saat memperbarui image, semua yang tertulis di dalamnya hilang.",
                    "",
                    "Kesalahan kedua: memakai tag latest di server. latest cuma label yang",
                    "bisa digeser kapan saja ke versi baru. Hari ini latest berarti Nginx",
                    "1.30, bulan depan bisa versi lain, dan server yang di-restart tiba-tiba",
                    "memakai versi yang belum pernah kamu uji. Tulis versinya, misalnya",
                    "nginx:1.30.",
                    "",
                    "Kesalahan ketiga: lupa -p, lalu bingung kenapa aplikasinya nggak bisa",
                    "dibuka padahal docker ps menunjukkan container-nya hidup.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Image resmi seperti postgres, redis, nginx, dan python di Docker Hub",
                    "dipakai jutaan pengembang untuk menjalankan database dan layanan",
                    "pendukung di laptop tanpa memasangnya langsung di sistem. Satu perintah",
                    "docker run, dan PostgreSQL versi berapa pun sudah jalan.",
                    "",
                    "Kasus kecil: proyek PKL-mu butuh PostgreSQL 17, tapi laptopmu sudah",
                    "memakai PostgreSQL 16 untuk proyek lain, dan dua versi itu nggak bisa",
                    "dipasang berdampingan dengan mudah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan versi yang dibutuhkan sebagai container, dengan port",
                    "     host yang belum dipakai:",
                    "       docker run -d --name pg17 -e POSTGRES_PASSWORD=rahasia \\",
                    "         -p 127.0.0.1:5433:5432 postgres:17",
                    "  2. Hubungkan aplikasimu ke localhost port 5433. PostgreSQL 16 di",
                    "     laptop tetap memakai 5432.",
                    "  3. Cek dengan docker logs pg17 sampai muncul tulisan bahwa database",
                    "     siap menerima koneksi.",
                    "  4. Ingat bahwa datanya hilang kalau container dihapus. Materi Volume,",
                    "     Jaringan, dan Image Docker yang Aman menunjukkan cara menyimpannya",
                    "     di volume.",
                ],
            },
        ],
    },
    {
        "title": "10. Dockerfile dan Cache Layer",
        "sections": [
            {
                "body": [
                    "Image resmi seperti nginx dan postgres sudah jadi. Untuk aplikasimu",
                    "sendiri, kamu harus membuat image-nya. Resepnya ditulis di berkas teks",
                    "bernama Dockerfile, berisi instruksi yang dijalankan berurutan dari",
                    "atas ke bawah.",
                    "",
                    "Materi ini membahas cara menulis Dockerfile, lalu hal yang",
                    "membedakan Dockerfile yang dibangun dalam lima detik dari yang dibangun",
                    "dalam lima menit: urutan instruksinya.",
                ],
            },
            {
                "heading": "Dockerfile pertama",
                "bahasa": "dockerfile",
                "code": """FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE 8000

CMD ["python", "app.py"]""",
            },
            {
                "body": [
                    "Arti tiap instruksi:",
                    "",
                    "  Instruksi   Fungsinya",
                    "  FROM        image dasar tempat kita mulai; di sini Python 3.14 versi",
                    "              slim yang isinya dikurangi",
                    "  WORKDIR     folder kerja di dalam image; dibuat kalau belum ada",
                    "  COPY        menyalin berkas dari folder proyek ke dalam image",
                    "  RUN         menjalankan perintah saat image dibangun",
                    "  ENV         variabel lingkungan bawaan",
                    "  EXPOSE      catatan port yang dipakai aplikasi; tidak membuka port",
                    "  CMD         perintah yang dijalankan saat container menyala",
                    "",
                    "Bedakan RUN dan CMD. RUN dijalankan sekali, waktu image dibangun,",
                    "hasilnya ikut tersimpan di image. CMD nggak dijalankan saat membangun;",
                    "ia cuma dicatat, lalu dijalankan setiap kali container menyala.",
                    "",
                    "EXPOSE sering disalahpahami. Ia cuma dokumentasi. Port tetap harus",
                    "dibuka dengan -p waktu docker run.",
                ],
            },
            {
                "heading": "Membangun dan menjalankan",
                "bahasa": "terminal",
                "code": """docker build -t toko:1.0 .        # titik = folder proyek sebagai konteks
docker run -d -p 8000:8000 toko:1.0
docker history toko:1.0            # lihat layer dan ukurannya""",
            },
            {
                "heading": "Layer: image tersusun dari lapisan",
                "body": [
                    "Image bukan satu berkas besar. Ia tersusun dari layer, yaitu lapisan",
                    "perubahan yang ditumpuk. Instruksi yang mengubah isi berkas (FROM, COPY,",
                    "RUN) menghasilkan layer baru. Instruksi lain seperti ENV dan CMD cuma",
                    "menambah keterangan.",
                    "",
                    "Layer ini yang membuat Docker hemat. Sepuluh image yang sama-sama",
                    "memakai python:3.14-slim cuma menyimpan layer Python itu sekali di",
                    "disk. Waktu menarik image baru dari registry, Docker cuma mengunduh",
                    "layer yang belum ia punya.",
                    "",
                    "Saat docker build dijalankan ulang, Docker mencoba memakai layer dari",
                    "build sebelumnya. Aturannya:",
                    "  1. Untuk setiap instruksi, Docker mengecek apakah instruksi itu",
                    "     persis sama dengan sebelumnya, dan apakah layer di bawahnya juga",
                    "     diambil dari cache.",
                    "  2. Untuk COPY, Docker juga mengecek isi berkas yang disalin. Satu",
                    "     huruf berubah di satu berkas, cache COPY itu batal.",
                    "  3. Begitu satu instruksi batal dari cache, semua instruksi di",
                    "     bawahnya ikut dibangun ulang, walaupun instruksinya sendiri nggak",
                    "     berubah.",
                    "",
                    "Aturan nomor 3 itu yang paling penting. Cache Docker seperti tumpukan",
                    "piring: kalau piring ketiga diganti, semua piring di atasnya harus",
                    "diangkat dan ditaruh ulang.",
                ],
            },
            {
                "heading": "Urutan yang salah dan yang benar",
                "bahasa": "dockerfile",
                "code": """# LAMBAT: setiap perubahan kode memicu pip install ulang
FROM python:3.14-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]

# CEPAT: pip install cuma diulang kalau requirements.txt berubah
FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]""",
            },
            {
                "body": [
                    "Di versi lambat, COPY . . menyalin semua berkas proyek, termasuk",
                    "app.py. Kamu mengubah satu baris di app.py, maka cache COPY batal, dan",
                    "RUN pip install di bawahnya ikut diulang. Memasang ulang semua pustaka",
                    "bisa makan beberapa menit, padahal daftar pustakanya nggak berubah.",
                    "",
                    "Di versi cepat, requirements.txt disalin sendiri lebih dulu. Selama",
                    "isinya sama, COPY itu dan RUN pip install di bawahnya diambil dari",
                    "cache. Yang dibangun ulang cuma COPY . . di bagian bawah, dan itu",
                    "selesai dalam hitungan detik.",
                    "",
                    "Prinsip umumnya: taruh yang jarang berubah di atas, yang sering berubah",
                    "di bawah. Pola yang sama berlaku untuk bahasa lain: package.json lalu",
                    "npm ci untuk Node.js, go.mod lalu go mod download untuk Go, pom.xml",
                    "untuk Maven.",
                    "",
                    "Keluaran docker build menandai layer yang diambil dari cache dengan",
                    "tulisan khusus di ujung barisnya. Kira-kira begini untuk versi cepat,",
                    "sesudah app.py diubah:",
                    "",
                    "  #5 [2/5] WORKDIR /app                                   CACHED",
                    "  #6 [3/5] COPY requirements.txt .                        CACHED",
                    "  #7 [4/5] RUN pip install --no-cache-dir -r ...          CACHED",
                    "  #8 [5/5] COPY . .                                       0.1s",
                    "",
                    "Latihan bab ini memintamu menulis simulasi aturan cache tadi dengan",
                    "hash berantai, persis cara Docker menentukan apakah sebuah layer boleh",
                    "dipakai ulang.",
                ],
            },
            {
                "heading": ".dockerignore dan jebakan cache",
                "body": [
                    "COPY . . menyalin semua isi folder proyek ke dalam image, termasuk yang",
                    "nggak perlu: folder .git, venv, node_modules, berkas log, dan berkas",
                    ".env berisi password. Selain membuat image gemuk, berkas yang sering",
                    "berubah seperti log ikut membatalkan cache. Buat berkas .dockerignore",
                    "di samping Dockerfile, formatnya mirip .gitignore:",
                    "",
                    "  .git",
                    "  .venv",
                    "  __pycache__",
                    "  *.log",
                    "  .env",
                    "",
                    "Jebakan: cache RUN cuma melihat teks perintahnya, bukan hasilnya. Baris",
                    "RUN apt-get update akan terus diambil dari cache selama teksnya sama,",
                    "walaupun daftar paket di internet sudah berubah berbulan-bulan. Gabungkan",
                    "apt-get update dan apt-get install dalam satu RUN, dan bangun ulang",
                    "tanpa cache sesekali dengan docker build --no-cache supaya pembaruan",
                    "keamanan ikut masuk.",
                    "",
                    "Satu lagi soal CMD. Tulis dalam bentuk daftar seperti",
                    "CMD [\"python\", \"app.py\"], bukan CMD python app.py. Bentuk kedua",
                    "dijalankan lewat /bin/sh, jadi aplikasimu bukan proses utama di",
                    "container. Sinyal berhenti dari docker stop ditangkap shell, bukan",
                    "aplikasimu, dan docker stop baru selesai sesudah menunggu 10 detik lalu",
                    "membunuh paksa.",
                    "",
                    "Sejak Docker Engine 23.0, pembangun bawaan Docker adalah BuildKit, yang",
                    "bisa membangun beberapa tahap sekaligus dan menyimpan cache dengan lebih",
                    "pintar. Kamu nggak perlu menyalakannya sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pipeline CI di GitHub Actions atau GitLab CI membangun image setiap ada",
                    "commit. Di sana urutan Dockerfile langsung kerasa di tagihan dan waktu",
                    "tunggu: Dockerfile yang urutannya salah bisa membuat setiap commit",
                    "menunggu beberapa menit hanya untuk memasang ulang pustaka yang sama.",
                    "",
                    "Kasus kecil: tim Node.js mengeluh setiap docker build makan empat",
                    "menit, bahkan kalau yang diubah cuma satu baris teks. Dockerfile mereka",
                    "berbunyi FROM node:24, WORKDIR /app, COPY . ., RUN npm ci, lalu",
                    "CMD [\"node\", \"server.js\"].",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan docker build dua kali berturut-turut sesudah mengubah",
                    "     satu berkas, dan lihat baris mana yang nggak diambil dari cache.",
                    "     Ternyata RUN npm ci selalu diulang.",
                    "  2. Penyebabnya COPY . . di atas npm ci, jadi setiap perubahan kode",
                    "     membatalkan cache npm ci.",
                    "  3. Pindahkan dependensinya ke atas:",
                    "       COPY package.json package-lock.json ./",
                    "       RUN npm ci",
                    "       COPY . .",
                    "  4. Tambahkan .dockerignore berisi node_modules dan .git supaya isi",
                    "     folder lokal nggak ikut tersalin. Build sesudah perubahan kode",
                    "     sekarang selesai dalam hitungan detik.",
                ],
            },
        ],
    },
    {
        "title": "11. Volume, Jaringan, dan Image Docker yang Aman",
        "sections": [
            {
                "body": [
                    "Container yang kamu jalankan sejauh ini berdiri sendiri: datanya hilang",
                    "kalau dihapus, dan ia nggak tahu ada container lain. Aplikasi sungguhan",
                    "butuh tiga hal lagi: tempat menyimpan data yang awet, cara antar",
                    "container saling menghubungi, dan image yang kecil serta nggak mudah",
                    "dibobol. Materi ini membahas ketiganya.",
                ],
            },
            {
                "heading": "Tiga cara menyimpan data",
                "body": [
                    "Sistem berkas di dalam container bersifat sementara. Begitu container",
                    "dihapus, semua yang ditulis di sana ikut hilang. Untuk data yang harus",
                    "awet, seperti isi database atau berkas unggahan pengguna, ada tiga",
                    "pilihan:",
                    "",
                    "  Jenis          Letak data                    Cocok untuk",
                    "  Volume         diurus Docker, di             data database, data",
                    "                 /var/lib/docker/volumes       aplikasi yang awet",
                    "  Bind mount     folder pilihanmu di host      kode saat pengembangan,",
                    "                                               berkas konfigurasi",
                    "  tmpfs          memori, hilang saat berhenti  berkas sementara rahasia",
                    "",
                    "Volume adalah pilihan bawaan untuk data. Docker yang menentukan letak",
                    "berkasnya, dan volume tetap ada walaupun container yang memakainya",
                    "dihapus. Bind mount menyambungkan folder tertentu di laptopmu ke dalam",
                    "container, jadi perubahan di satu sisi langsung terlihat di sisi lain.",
                ],
            },
            {
                "heading": "Volume dan bind mount",
                "bahasa": "terminal",
                "code": "docker volume create pgdata\ndocker run -d --name db -e POSTGRES_PASSWORD=rahasia \\\n  -v pgdata:/var/lib/postgresql/data postgres:17\ndocker volume ls\n\n# bind mount: folder proyek ke dalam container (pengembangan)\ndocker run -d -p 8080:80 -v \"$PWD/public\":/usr/share/nginx/html:ro,Z nginx:1.30",
            },
            {
                "body": [
                    "Dengan -v pgdata:/var/lib/postgresql/data, isi database tersimpan di",
                    "volume pgdata. Kamu bisa menghapus container db, menjalankan container",
                    "baru dengan PostgreSQL versi patch berikutnya, menyambungkan volume yang",
                    "sama, dan datanya masih ada.",
                    "",
                    "Di bind mount, ro artinya read only: container cuma boleh membaca.",
                    "Huruf Z khusus untuk sistem yang memakai SELinux seperti Fedora. Tanpa",
                    "Z, SELinux melarang container membaca folder dari home-mu, dan",
                    "gejalanya error Permission denied yang membingungkan.",
                ],
            },
            {
                "heading": "Jaringan antar container",
                "body": [
                    "Setiap container punya alamat IP sendiri di jaringan virtual buatan",
                    "Docker. Alamat itu berubah setiap container dibuat ulang, jadi jangan",
                    "pernah menulis alamat IP container di konfigurasi.",
                    "",
                    "Caranya: buat jaringan sendiri. Di jaringan buatan sendiri (user-defined",
                    "bridge), Docker menjalankan DNS kecil, sehingga container bisa saling",
                    "memanggil lewat namanya. Jaringan bawaan bernama bridge nggak punya",
                    "fitur ini, dan itu sumber kebingungan yang umum.",
                ],
            },
            {
                "heading": "Aplikasi dan database di satu jaringan",
                "bahasa": "terminal",
                "code": "docker network create tokonet\ndocker run -d --name db --network tokonet \\\n  -e POSTGRES_PASSWORD=rahasia -v pgdata:/var/lib/postgresql/data postgres:17\ndocker run -d --name web --network tokonet -p 8000:8000 \\\n  -e DATABASE_URL=postgresql://postgres:rahasia@db:5432/postgres toko:1.0",
            },
            {
                "body": [
                    "Perhatikan alamat database di DATABASE_URL: host-nya db, nama",
                    "container database. DNS di jaringan tokonet menerjemahkan nama itu ke",
                    "alamat IP container db yang sekarang.",
                    "",
                    "Container db sama sekali nggak diberi -p. Database cuma perlu diakses",
                    "oleh web, dan keduanya ada di jaringan yang sama, jadi nggak ada alasan",
                    "membuka port database ke luar mesin.",
                    "",
                    "Pilihan lain yang kadang kamu temui adalah --network host. Container",
                    "memakai jaringan mesin langsung, tanpa pemisahan. Gampang, tapi port",
                    "container dan port mesin bisa bentrok, dan isolasinya hilang.",
                ],
            },
            {
                "heading": "Membaca nilai -p dengan teliti",
                "code": "def urai_port(spek):\n    \"\"\"Urai nilai -p docker run: [ip:]port_host:port_container[/protokol].\"\"\"\n    spek, _, protokol = spek.partition(\"/\")\n    bagian = spek.split(\":\")\n    if len(bagian) == 3:\n        ip, host, container = bagian\n    else:\n        ip, (host, container) = \"0.0.0.0\", bagian\n    return ip, int(host), int(container), protokol or \"tcp\"\n\n\nfor spek in [\"8080:80\", \"127.0.0.1:5432:5432\", \"53:53/udp\"]:\n    ip, host, container, protokol = urai_port(spek)\n    terbuka = \"semua alamat\" if ip == \"0.0.0.0\" else \"cuma \" + ip\n    print(f\"{spek:<20} host {host} -> container {container}/{protokol}, {terbuka}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  8080:80              host 8080 -> container 80/tcp, semua alamat",
                    "  127.0.0.1:5432:5432  host 5432 -> container 5432/tcp, cuma 127.0.0.1",
                    "  53:53/udp            host 53 -> container 53/udp, semua alamat",
                    "",
                    "Yang paling penting di sini kolom terakhir. -p 5432:5432 tanpa alamat",
                    "berarti port itu dibuka untuk semua alamat, termasuk dari internet.",
                    "Docker menulis aturan firewall-nya sendiri ke kernel, jadi ufw atau",
                    "firewalld nggak bisa menghalanginya.",
                    "",
                    "Jebakan: menjalankan database dengan -p 5432:5432 di VPS karena \"cuma",
                    "sementara\". Program pemindai di internet mencari port database yang",
                    "terbuka setiap hari. Kalau port database memang perlu dibuka di",
                    "mesinmu, tulis alamatnya: -p 127.0.0.1:5432:5432. Lebih baik lagi,",
                    "jangan dibuka sama sekali dan pakai jaringan Docker seperti contoh",
                    "sebelumnya.",
                ],
            },
            {
                "heading": "Image yang kecil dan aman",
                "bahasa": "dockerfile",
                "code": """# tahap 1: membangun
FROM python:3.14-slim AS pembangun
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/pasang -r requirements.txt

# tahap 2: image akhir, tanpa alat bangun
FROM python:3.14-slim
WORKDIR /app
COPY --from=pembangun /pasang /usr/local
COPY . .
RUN useradd --create-home toko
USER toko
CMD ["python", "app.py"]""",
            },
            {
                "body": [
                    "Ini multi-stage build: satu Dockerfile dengan beberapa FROM. Tahap",
                    "pertama dipakai untuk membangun, tahap terakhir jadi image yang",
                    "dikirim. Alat yang cuma dibutuhkan saat membangun, misalnya compiler C",
                    "untuk pustaka tertentu, tertinggal di tahap pertama. Untuk bahasa yang",
                    "dikompilasi seperti Go, hasilnya bisa jauh lebih kecil: tahap akhir cuma",
                    "berisi satu berkas program.",
                    "",
                    "Kebiasaan lain untuk image yang aman:",
                    "  - Pilih image dasar yang kecil: varian slim, alpine (lebih kecil",
                    "    lagi, tapi memakai pustaka C musl yang kadang bikin masalah untuk",
                    "    pustaka Python), atau distroless yang bahkan nggak punya shell.",
                    "    Makin sedikit isinya, makin sedikit celah keamanannya.",
                    "  - Jalankan sebagai pengguna biasa dengan USER. Tanpa itu, proses di",
                    "    container berjalan sebagai root. Kalau aplikasinya dibobol,",
                    "    penyerang langsung jadi root di dalam container.",
                    "  - Jangan pernah menyalin rahasia ke image, baik lewat COPY .env",
                    "    maupun ARG. Siapa pun yang punya image-nya bisa membongkar semua",
                    "    layer dan membaca isinya, walaupun berkasnya dihapus di layer",
                    "    berikutnya. Kirim rahasia saat container jalan lewat variabel",
                    "    lingkungan, atau saat build lewat RUN --mount=type=secret.",
                    "  - Tulis versi image dasar dengan jelas, dan bangun ulang secara",
                    "    berkala supaya pembaruan keamanan ikut masuk.",
                    "  - Pindai image dengan Docker Scout atau Trivy untuk menemukan pustaka",
                    "    yang punya celah keamanan. Alat pemindai dibahas di kurikulum",
                    "    Keamanan Siber.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan kebocoran data yang berawal dari database terbuka ke internet",
                    "muncul berkali-kali tiap tahun, dan banyak di antaranya berasal dari",
                    "container database yang port-nya di-publish ke semua alamat. Pemindai",
                    "otomatis menemukan port seperti itu dalam hitungan jam.",
                    "",
                    "Kasus kecil: kamu menjalankan aplikasi dan PostgreSQL di VPS dengan dua",
                    "perintah docker run. Database memakai -p 5432:5432 supaya aplikasi bisa",
                    "terhubung lewat alamat IP VPS. Setelah server di-restart untuk update,",
                    "semua data hilang, dan log PostgreSQL penuh percobaan login dari",
                    "alamat asing.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Data hilang karena nggak ada volume. Buat volume dan sambungkan:",
                    "       -v pgdata:/var/lib/postgresql/data",
                    "  2. Percobaan login asing datang karena port 5432 terbuka ke semua",
                    "     alamat. Buat jaringan dengan docker network create tokonet, lalu",
                    "     jalankan kedua container dengan --network tokonet.",
                    "  3. Hapus -p dari container database, dan ganti alamat database di",
                    "     aplikasi jadi db:5432, memakai nama container.",
                    "  4. Cek dari laptop dengan nc -vz alamat-vps 5432. Hasilnya harus",
                    "     gagal, sementara aplikasinya tetap bisa membaca database.",
                ],
            },
        ],
    },
    {
        "title": "12. Docker Compose: Banyak Container dalam Satu Berkas",
        "sections": [
            {
                "body": [
                    "Di akhir bab 03 kamu menjalankan aplikasi dan database dengan dua",
                    "perintah docker run yang panjang, plus satu perintah membuat jaringan",
                    "dan satu lagi membuat volume. Aplikasi sungguhan biasanya butuh lebih:",
                    "aplikasi web, database, cache, mungkin satu worker untuk pekerjaan",
                    "latar belakang. Mengetik semua perintah itu setiap kali, dengan urutan",
                    "yang benar, gampang salah dan susah dibagikan ke teman satu tim.",
                    "",
                    "Docker Compose memecahkan itu. Semua container, jaringan, dan volume",
                    "ditulis di satu berkas YAML bernama compose.yaml, lalu dijalankan",
                    "dengan satu perintah. Berkas itu disimpan di Git bersama kode, jadi",
                    "siapa pun yang meng-clone proyekmu bisa menjalankan seluruh tumpukan",
                    "yang sama.",
                ],
            },
            {
                "heading": "compose.yaml pertama",
                "bahasa": "yaml",
                "code": """services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://toko:rahasia@db:5432/toko
      REDIS_URL: redis://cache:6379/0
    depends_on:
      - db
      - cache

  db:
    image: postgres:17
    environment:
      POSTGRES_USER: toko
      POSTGRES_PASSWORD: rahasia
      POSTGRES_DB: toko
    volumes:
      - pgdata:/var/lib/postgresql/data

  cache:
    image: redis:8

volumes:
  pgdata:""",
            },
            {
                "body": [
                    "Kita baca dari atas:",
                    "  - services berisi tiga layanan. Satu layanan kira-kira sama dengan",
                    "    satu perintah docker run.",
                    "  - web dibangun dari Dockerfile di folder yang sama (build: .). Port",
                    "    8000 dibuka ke host, dan alamat database serta cache diberikan",
                    "    lewat variabel lingkungan.",
                    "  - db dan cache memakai image jadi dari Docker Hub. Keduanya nggak",
                    "    membuka port ke host, karena cuma web yang perlu menghubungi",
                    "    mereka.",
                    "  - volumes di tingkat atas mendeklarasikan volume pgdata. Layanan db",
                    "    memakainya untuk menyimpan isi database.",
                    "",
                    "Ada yang nggak ditulis tapi tetap terjadi: Compose otomatis",
                    "membuat satu jaringan untuk proyek ini dan memasukkan ketiga layanan ke",
                    "sana. Di jaringan itu, nama layanan bisa dipakai sebagai nama host.",
                    "Karena itu web bisa menghubungi database lewat alamat db:5432 dan",
                    "cache lewat cache:6379, persis seperti jaringan buatan sendiri di bab",
                    "03.",
                    "",
                    "depends_on membuat Compose menyalakan db dan cache sebelum web. Tapi",
                    "ini cuma soal urutan menyalakan, bukan soal siap. Materi berikutnya",
                    "membahas kenapa itu sering bikin masalah.",
                ],
            },
            {
                "heading": "Perintah sehari-hari",
                "bahasa": "terminal",
                "code": """docker compose up -d            # bangun (kalau perlu) dan nyalakan semua
docker compose ps               # keadaan tiap layanan
docker compose logs -f web      # ikuti log satu layanan
docker compose exec db psql -U toko   # masuk ke container yang hidup
docker compose up -d --build    # bangun ulang image sesudah kode berubah
docker compose down             # hentikan dan hapus container + jaringan
docker compose down -v          # ... dan hapus volume juga (data hilang!)""",
            },
            {
                "body": [
                    "Compose memberi nama berdasarkan folder proyek. Kalau foldernya bernama",
                    "toko, jaringannya toko_default dan container-nya toko-web-1, toko-db-1,",
                    "dan seterusnya. Angka di belakang dipakai kalau satu layanan dijalankan",
                    "lebih dari satu salinan.",
                    "",
                    "docker compose down aman untuk data: container dan jaringannya dihapus,",
                    "tapi volume pgdata tetap ada, dan up berikutnya memakai data yang sama.",
                    "Jebakan: down -v ikut menghapus volume. Perintah itu cocok untuk",
                    "mengulang dari nol di laptop, tapi jangan pernah dijalankan di server",
                    "yang datanya penting.",
                ],
            },
            {
                "heading": "Memeriksa compose.yaml sebelum dijalankan",
                "code": """# compose.yaml yang sudah diurai jadi dict (Python tidak punya pengurai YAML).
compose = {
    "services": {
        "web": {"build": ".", "ports": ["8000:8000"], "depends_on": ["db"]},
        "db": {"image": "postgres:17", "volumes": ["pgdata:/var/lib/postgresql/data"]},
        "admin": {"image": "adminer:5", "ports": ["8000:8080"]},
        "cache": {"image": "valkey/valkey:8", "volumes": ["cachedata:/data"]},
    },
    "volumes": {"pgdata": {}},
}

masalah = []
port_host = {}
for nama, layanan in compose["services"].items():
    for port in layanan.get("ports", []):
        host = port.split(":")[0]
        if host in port_host:
            masalah.append(f"port {host} dipakai {port_host[host]} dan {nama}")
        port_host[host] = nama
    for vol in layanan.get("volumes", []):
        sumber = vol.split(":")[0]
        if not sumber.startswith((".", "/")) and sumber not in compose["volumes"]:
            masalah.append(f"volume {sumber} di {nama} belum dideklarasikan")
    for dep in layanan.get("depends_on", []):
        if dep not in compose["services"]:
            masalah.append(f"{nama} bergantung pada {dep} yang tidak ada")

print(len(masalah), "masalah ditemukan")
for m in masalah:
    print("-", m)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  2 masalah ditemukan",
                    "  - port 8000 dipakai web dan admin",
                    "  - volume cachedata di cache belum dideklarasikan",
                    "",
                    "Dua kesalahan ini sering terjadi waktu compose.yaml makin panjang. Dua",
                    "layanan yang meminta port host yang sama membuat salah satunya gagal",
                    "menyala. Volume bernama yang nggak dideklarasikan di bagian volumes",
                    "ditolak Compose sebelum apa pun dijalankan. Sumber yang diawali titik",
                    "atau garis miring dianggap bind mount ke folder, jadi nggak perlu",
                    "dideklarasikan.",
                    "",
                    "Compose sendiri punya pemeriksa: docker compose config membaca",
                    "berkasnya, menggabungkan semua pengaturan, lalu mencetak hasil akhirnya",
                    "atau pesan kesalahannya.",
                ],
            },
            {
                "heading": "Versi, sejarah, dan jebakannya",
                "body": [
                    "Compose yang dipakai sekarang adalah plugin Docker yang dipanggil",
                    "dengan docker compose, pakai spasi. Versi terbarunya v5.6.0, dirilis",
                    "2 Oktober 2026. Compose generasi pertama ditulis dengan Python dan",
                    "dipanggil dengan docker-compose, pakai tanda hubung. Versi itu sudah",
                    "lama berhenti dirawat. Kalau tutorial yang kamu baca memakai",
                    "docker-compose, perintahnya hampir selalu tetap jalan dengan",
                    "docker compose.",
                    "",
                    "Berkas lama sering diawali baris version: \"3.8\". Kunci version itu",
                    "sudah usang, dan Compose sekarang cuma memberi peringatan lalu",
                    "mengabaikannya. Hapus saja.",
                    "",
                    "Beberapa jebakan lain:",
                    "  - Password di compose.yaml ikut masuk Git. Untuk proyek sungguhan,",
                    "    pindahkan ke berkas .env yang nggak di-commit. Caranya dibahas di",
                    "    materi berikutnya.",
                    "  - Mengubah compose.yaml lalu cuma menjalankan docker compose restart.",
                    "    restart nggak membaca ulang konfigurasi. Pakai docker compose up -d,",
                    "    yang membuat ulang container yang konfigurasinya berubah.",
                    "  - Naik versi major database dengan cuma mengganti tag image, misalnya",
                    "    postgres:17 ke versi berikutnya. Data PostgreSQL versi lama nggak",
                    "    bisa langsung dibaca versi major baru, dan mulai image postgres:18",
                    "    letak data bawaannya juga berubah. Baca catatan di halaman image-nya",
                    "    dan siapkan backup sebelum naik versi.",
                    "",
                    "Compose cocok untuk lingkungan pengembangan, demo, dan server kecil",
                    "satu mesin. Untuk banyak mesin dengan pemulihan otomatis, tempatnya",
                    "Kubernetes, yang dibahas di bab Kubernetes.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek open source menaruh compose.yaml di repositorinya supaya",
                    "calon kontributor bisa menjalankan aplikasi beserta database dan",
                    "layanan pendukungnya dengan satu perintah. Aplikasi self-hosted seperti",
                    "Nextcloud dan Gitea juga menyediakan contoh compose.yaml di",
                    "dokumentasinya.",
                    "",
                    "Kasus kecil: anggota tim baru butuh setengah hari untuk menyiapkan",
                    "laptopnya: memasang PostgreSQL, Redis, membuat database, dan mengatur",
                    "variabel lingkungan sesuai catatan di README yang sudah ketinggalan",
                    "zaman.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis compose.yaml berisi web, db, dan cache seperti contoh di",
                    "     atas, lengkap dengan volume untuk database.",
                    "  2. Ganti alamat database dan cache di kode supaya dibaca dari",
                    "     variabel lingkungan, dengan nama host db dan cache.",
                    "  3. Jalankan docker compose config untuk memastikan berkasnya sah,",
                    "     lalu docker compose up -d dan buka aplikasinya.",
                    "  4. Ganti seluruh petunjuk pemasangan di README jadi dua baris:",
                    "     git clone, lalu docker compose up -d.",
                ],
            },
        ],
    },
    {
        "title": "13. Compose Lanjutan: Healthcheck, Variabel, dan Profil",
        "sections": [
            {
                "body": [
                    "compose.yaml dari materi sebelumnya jalan, tapi punya tiga masalah yang",
                    "bakal kamu temui cepat atau lambat. Aplikasi web kadang crash waktu",
                    "pertama menyala karena database belum siap. Password tertulis langsung",
                    "di berkas yang masuk Git. Dan layanan tambahan seperti panel admin",
                    "database ikut menyala di semua lingkungan, padahal cuma dibutuhkan",
                    "sesekali.",
                    "",
                    "Materi ini menambal ketiganya: healthcheck, variabel, dan profil.",
                ],
            },
            {
                "heading": "Menyala belum tentu siap",
                "body": [
                    "depends_on dalam bentuk daftar biasa cuma menjamin urutan menyalakan.",
                    "Compose menyalakan container db, lalu langsung menyalakan web tanpa",
                    "menunggu PostgreSQL di dalamnya selesai bersiap. PostgreSQL butuh",
                    "beberapa detik untuk membuat berkas data dan mulai menerima koneksi,",
                    "apalagi waktu pertama kali dijalankan. Selama beberapa detik itu,",
                    "aplikasi yang mencoba terhubung mendapat connection refused, lalu",
                    "crash.",
                    "",
                    "Jalan keluarnya: beri db sebuah healthcheck, yaitu perintah yang",
                    "dijalankan berkala untuk mengecek apakah layanannya benar siap. Lalu",
                    "suruh web menunggu sampai db dinyatakan sehat.",
                ],
            },
            {
                "heading": "Healthcheck, depends_on bersyarat, dan profil",
                "bahasa": "yaml",
                "code": """services:
  web:
    image: ghcr.io/contoh/toko:${TAG:-dev}
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://toko:${DB_PASSWORD}@db:5432/toko
    depends_on:
      db:
        condition: service_healthy
      migrasi:
        condition: service_completed_successfully
    restart: unless-stopped

  migrasi:
    image: ghcr.io/contoh/toko:${TAG:-dev}
    command: ["python", "manage.py", "migrate"]
    environment:
      DATABASE_URL: postgresql://toko:${DB_PASSWORD}@db:5432/toko
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:17
    environment:
      POSTGRES_USER: toko
      POSTGRES_PASSWORD: ${DB_PASSWORD:?isi DB_PASSWORD di berkas .env}
      POSTGRES_DB: toko
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U toko -d toko"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 10s

  adminer:
    image: adminer:5
    profiles: ["debug"]
    ports:
      - "127.0.0.1:8080:8080"

volumes:
  pgdata:""",
            },
            {
                "body": [
                    "Bagian healthcheck di db menjalankan pg_isready, alat bawaan image",
                    "postgres, setiap 5 detik. Kalau gagal 10 kali berturut-turut, db",
                    "dinyatakan tidak sehat. start_period memberi 10 detik pertama sebagai",
                    "masa pemanasan: kegagalan di masa itu nggak dihitung.",
                    "",
                    "depends_on sekarang memakai bentuk panjang dengan condition:",
                    "  - service_started: cuma menunggu container menyala. Ini yang dipakai",
                    "    bentuk daftar biasa.",
                    "  - service_healthy: menunggu healthcheck layanan itu lulus.",
                    "  - service_completed_successfully: menunggu container itu selesai",
                    "    dengan kode keluar 0. Cocok untuk tugas sekali jalan seperti",
                    "    migrasi database.",
                    "",
                    "Urutannya sekarang: db menyala, healthcheck-nya lulus, migrasi jalan",
                    "dan selesai, baru web menyala. restart: unless-stopped membuat web",
                    "dinyalakan ulang kalau crash atau kalau Docker di-restart, kecuali kamu",
                    "sendiri yang menghentikannya.",
                    "",
                    "Jebakan: healthcheck yang mengecek terlalu dangkal. Mengecek \"port 5432",
                    "terbuka\" bisa lulus sebelum database siap menerima query. Pakai alat",
                    "yang memang ditujukan untuk itu, seperti pg_isready untuk PostgreSQL",
                    "atau redis-cli ping untuk Redis.",
                ],
            },
            {
                "heading": "Variabel dan berkas .env",
                "body": [
                    "Tulisan ${...} di compose.yaml diganti dengan nilai variabel lingkungan",
                    "sebelum berkasnya dipakai. Proses ini disebut interpolasi. Nilainya",
                    "diambil dari variabel di shell-mu, atau dari berkas bernama .env di",
                    "folder yang sama dengan compose.yaml. Kalau keduanya ada, nilai dari",
                    "shell yang dipakai.",
                    "",
                    "Isi .env untuk contoh di atas:",
                ],
            },
            {
                "heading": "Berkas .env (jangan di-commit)",
                "bahasa": "env",
                "code": """TAG=1.4.0
DB_PASSWORD=ganti-dengan-password-panjang""",
            },
            {
                "body": [
                    "Masukkan .env ke .gitignore, lalu commit berkas .env.example berisi",
                    "nama variabelnya saja, supaya anggota tim tahu apa yang harus diisi.",
                    "",
                    "Ada beberapa bentuk penulisan:",
                    "",
                    "  Bentuk           Hasilnya",
                    "  ${VAR}           nilai VAR; kosong kalau tidak ada",
                    "  ${VAR:-bawaan}   bawaan, kalau VAR tidak ada atau kosong",
                    "  ${VAR-bawaan}    bawaan, kalau VAR tidak ada (kosong tetap kosong)",
                    "  ${VAR:?pesan}    berhenti dengan pesan, kalau VAR tidak ada atau kosong",
                    "",
                    "Bentuk :? paling berguna untuk rahasia. Daripada database menyala",
                    "dengan password kosong, Compose menolak jalan dan menampilkan pesanmu.",
                    "",
                    "Bedakan .env dengan pengaturan env_file di dalam layanan. .env dipakai",
                    "Compose untuk mengisi ${...} di compose.yaml. env_file: berkas.env di",
                    "sebuah layanan mengirim seluruh isi berkas itu sebagai variabel",
                    "lingkungan ke dalam container-nya. Dua hal ini sering tertukar.",
                ],
            },
            {
                "heading": "Meniru interpolasi Compose",
                "code": "import re\n\nPOLA = re.compile(r\"\\$\\{(\\w+)(?:(:?[-?])([^}]*))?\\}\")\n\n\ndef isi(teks, env):\n    def ganti(cocok):\n        nama, tanda, sisanya = cocok.groups()\n        nilai = env.get(nama)\n        kosong = nilai is None or (tanda and tanda.startswith(\":\") and nilai == \"\")\n        if tanda in (\"-\", \":-\") and kosong:\n            return sisanya\n        if tanda in (\"?\", \":?\") and kosong:\n            raise ValueError(f\"{nama}: {sisanya}\")\n        return nilai or \"\"\n    return POLA.sub(ganti, teks)\n\n\nenv = {\"TAG\": \"1.4.0\", \"DEBUG\": \"\"}\nfor baris in [\"image: toko:${TAG}\",\n              \"image: postgres:${PG_VERSI:-17}\",\n              \"DEBUG=${DEBUG:-0}\",\n              \"DEBUG=${DEBUG-0}\",\n              \"password: ${DB_PASSWORD:?wajib}\"]:\n    try:\n        print(f\"{baris:<32} -> {isi(baris, env)}\")\n    except ValueError as e:\n        print(f\"{baris:<32} -> galat: {e}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  image: toko:${TAG}               -> image: toko:1.4.0",
                    "  image: postgres:${PG_VERSI:-17}  -> image: postgres:17",
                    "  DEBUG=${DEBUG:-0}                -> DEBUG=0",
                    "  DEBUG=${DEBUG-0}                 -> DEBUG=",
                    "  password: ${DB_PASSWORD:?wajib}  -> galat: DB_PASSWORD: wajib",
                    "",
                    "Perhatikan baris ketiga dan keempat. DEBUG ada tapi kosong. Dengan :-,",
                    "nilai kosong dianggap sama dengan tidak ada, jadi bawaannya dipakai.",
                    "Tanpa titik dua, nilai kosong tetap dipakai apa adanya.",
                    "",
                    "Untuk melihat hasil interpolasi Compose yang asli, jalankan",
                    "docker compose config. Perintah itu mencetak compose.yaml yang sudah",
                    "diisi semua nilainya.",
                ],
            },
            {
                "heading": "Profil dan berkas tambahan",
                "bahasa": "terminal",
                "code": """docker compose up -d                       # tanpa adminer
docker compose --profile debug up -d       # adminer ikut menyala
docker compose -f compose.yaml -f compose.prod.yaml up -d
docker compose config                      # lihat hasil gabungan akhirnya""",
            },
            {
                "body": [
                    "Layanan yang diberi profiles cuma menyala kalau profilnya diaktifkan",
                    "dengan --profile atau variabel COMPOSE_PROFILES. Layanan tanpa profiles",
                    "selalu menyala. Panel admin database, alat debug, dan layanan email",
                    "tiruan cocok diberi profil.",
                    "",
                    "Untuk perbedaan antarlingkungan yang lebih besar, pakai beberapa",
                    "berkas. Berkas compose.override.yaml, kalau ada, otomatis digabungkan",
                    "di atas compose.yaml. Biasanya isinya pengaturan khusus laptop,",
                    "misalnya bind mount folder kode supaya perubahan langsung terlihat.",
                    "Untuk server, tulis compose.prod.yaml dan sebutkan kedua berkas dengan",
                    "-f. Nilai di berkas yang disebut belakangan menimpa yang lebih dulu.",
                    "",
                    "Ingat: profil dan berkas tambahan cuma memilih apa yang dijalankan.",
                    "Rahasia tetap harus datang dari .env atau dari pengelola rahasia,",
                    "bukan ditulis di salah satu berkas compose.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kombinasi healthcheck dan depends_on bersyarat dipakai hampir di semua",
                    "compose.yaml yang punya database, dan contoh resmi di dokumentasi",
                    "Docker juga memakainya. Berkas .env.example di samping compose.yaml",
                    "juga sudah jadi kebiasaan umum di proyek open source.",
                    "",
                    "Kasus kecil: setiap pagi, docker compose up -d di laptopmu berakhir",
                    "dengan container web berstatus exited. Lognya berisi connection",
                    "refused ke db:5432. Kalau web dinyalakan ulang semenit kemudian,",
                    "semuanya lancar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Gejalanya menunjukkan web menyala sebelum PostgreSQL siap. depends_on",
                    "     yang dipakai masih bentuk daftar biasa, jadi Compose nggak",
                    "     menunggu.",
                    "  2. Tambahkan healthcheck ke db:",
                    "       test: [\"CMD-SHELL\", \"pg_isready -U toko -d toko\"]",
                    "  3. Ubah depends_on di web jadi bentuk panjang dengan",
                    "     condition: service_healthy.",
                    "  4. Jalankan docker compose up -d lagi, lalu docker compose ps. Kolom",
                    "     status db menunjukkan healthy sebelum web menyala.",
                ],
            },
        ],
    },
    {
        "title": "14. Podman: Container Tanpa Root di Fedora",
        "sections": [
            {
                "body": [
                    "Coba ketik podman --version di terminal Fedora-mu. Hampir pasti sudah",
                    "ada. Podman adalah mesin container buatan Red Hat yang terpasang bawaan",
                    "di Fedora, Red Hat Enterprise Linux, Rocky, dan AlmaLinux. Perintahnya",
                    "sengaja dibuat hampir sama dengan docker, jadi semua yang kamu pelajari",
                    "di bab 03 langsung bisa dipakai.",
                    "",
                    "Bedanya ada di cara kerja. Docker memakai satu program latar belakang,",
                    "dockerd, yang berjalan sebagai root dan mengurus semua container.",
                    "Podman nggak punya program latar belakang seperti itu (daemonless).",
                    "Setiap container adalah proses biasa milik pengguna yang menjalankannya,",
                    "dan bisa jalan tanpa hak root sama sekali (rootless).",
                ],
            },
            {
                "heading": "Kenapa rootless penting",
                "body": [
                    "Siapa pun yang bisa memerintah dockerd punya kendali setara root atas",
                    "mesin itu, karena dockerd sendiri berjalan sebagai root. Karena itu",
                    "grup docker di Linux dianggap setara dengan akses sudo.",
                    "",
                    "Podman rootless memakai fitur kernel bernama user namespace. Di dalam",
                    "container, prosesnya merasa jadi root (UID 0). Di luar, di mata kernel",
                    "host, proses itu cuma pengguna biasa, yaitu kamu. Kalau ada yang berhasil",
                    "keluar dari container, ia cuma dapat hak penggunamu, bukan root.",
                    "",
                    "UID yang lain di dalam container dipetakan ke rentang khusus milikmu,",
                    "yang tercatat di /etc/subuid. Fedora membuat rentang itu otomatis untuk",
                    "setiap pengguna baru.",
                ],
            },
            {
                "heading": "Peta UID rootless",
                "code": """# Isi /etc/subuid untuk pengguna budi (UID 1000) di host.
subuid = "budi:100000:65536"
uid_host_budi = 1000

nama, awal, jumlah = subuid.split(":")
awal, jumlah = int(awal), int(jumlah)


def ke_host(uid_container):
    if uid_container == 0:
        return uid_host_budi            # root di container = budi di host
    if 1 <= uid_container <= jumlah:
        return awal + uid_container - 1
    return None                         # di luar jatah: tidak dipetakan


for uid in [0, 1, 999, 65536, 70000]:
    hasil = ke_host(uid)
    teks = "tidak dipetakan" if hasil is None else f"UID host {hasil}"
    print(f"UID container {uid:>5} -> {teks}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  UID container     0 -> UID host 1000",
                    "  UID container     1 -> UID host 100000",
                    "  UID container   999 -> UID host 100998",
                    "  UID container 65536 -> UID host 165535",
                    "  UID container 70000 -> tidak dipetakan",
                    "",
                    "Baris 999 menjelaskan satu kebingungan yang sering muncul. Image",
                    "postgres menjalankan databasenya sebagai pengguna dengan UID 999. Kalau",
                    "kamu melihat folder data volume itu dari host dengan ls -ln, pemiliknya",
                    "tertulis 100998, bukan namamu. Itu normal. Untuk masuk ke ruang UID",
                    "container dari host, pakai podman unshare, misalnya",
                    "podman unshare ls -ln folder-data.",
                ],
            },
            {
                "heading": "Perintah yang sama, plus pod",
                "bahasa": "terminal",
                "code": """podman run -d --name web -p 8080:80 docker.io/library/nginx:1.30
podman ps
podman logs web

# pod: beberapa container berbagi jaringan, seperti Pod di Kubernetes
podman pod create --name toko -p 8000:8000
podman run -d --pod toko --name db -e POSTGRES_PASSWORD=rahasia docker.io/library/postgres:17
podman run -d --pod toko --name web ghcr.io/contoh/toko:1.4.0
podman kube generate toko > toko.yaml   # jadi manifest Kubernetes
podman kube play toko.yaml              # jalankan lagi dari manifest""",
            },
            {
                "body": [
                    "Pod adalah sekelompok container yang berbagi satu jaringan, jadi web",
                    "bisa menghubungi database di localhost:5432. Konsep ini dipinjam",
                    "langsung dari Kubernetes, dan podman kube generate bisa mengubah pod",
                    "yang sedang jalan jadi manifest Kubernetes. Kamu bakal ketemu Pod lagi",
                    "di bab Kubernetes.",
                    "",
                    "Kalau terbiasa mengetik docker, pasang paket podman-docker. Paket itu",
                    "menyediakan perintah docker yang meneruskan semuanya ke Podman. Untuk",
                    "berkas compose.yaml, ada perintah podman compose, yang meneruskan",
                    "pekerjaannya ke docker-compose atau podman-compose yang terpasang.",
                ],
            },
            {
                "heading": "Tiga jebakan khas Podman",
                "body": [
                    "Jebakan: menulis nama image pendek seperti nginx. Docker selalu",
                    "menganggapnya docker.io/library/nginx. Podman nggak berasumsi begitu:",
                    "ia mencari di daftar registry yang diatur di",
                    "/etc/containers/registries.conf. Untuk nama populer, Fedora sudah",
                    "menyediakan daftar alias, tapi nama lain bisa memunculkan pertanyaan",
                    "\"pilih registry mana\" atau gagal di skrip yang nggak bisa menjawab.",
                    "Biasakan menulis nama lengkap, seperti docker.io/library/nginx:1.30.",
                    "",
                    "Jebakan kedua: port di bawah 1024. Pengguna biasa nggak boleh membuka",
                    "port 80 atau 443, jadi podman run -p 80:80 gagal dalam mode rootless.",
                    "Pakai port tinggi seperti 8080 dan pasang reverse proxy di depannya,",
                    "atau turunkan batas lewat pengaturan kernel",
                    "net.ipv4.ip_unprivileged_port_start.",
                    "",
                    "Jebakan ketiga: jaringan rootless lebih lambat dan sedikit beda",
                    "perilakunya dibanding jaringan Docker yang dijalankan root. Sejak",
                    "Podman 5, jaringan rootless bawaan memakai pasta. Biasanya kamu nggak",
                    "perlu memikirkannya, tapi ingat ini kalau mengukur kecepatan jaringan",
                    "container.",
                ],
            },
            {
                "heading": "Quadlet: container sebagai layanan systemd",
                "body": [
                    "Container yang dijalankan dengan podman run mati kalau mesin",
                    "di-restart. Di bab 01 kamu menulis berkas unit systemd untuk aplikasi",
                    "Python. Untuk container, Podman menyediakan Quadlet: kamu menulis",
                    "berkas .container berformat mirip unit systemd, dan Quadlet mengubahnya",
                    "jadi layanan systemd sungguhan.",
                    "",
                    "Berkas ini disimpan sebagai ~/.config/containers/systemd/situs.container",
                    "untuk container milik pengguna biasa:",
                ],
            },
            {
                "heading": "situs.container",
                "bahasa": "ini",
                "code": """[Unit]
Description=Situs toko statis

[Container]
Image=docker.io/library/nginx:1.30
PublishPort=8080:80
Volume=%h/situs:/usr/share/nginx/html:ro,Z

[Service]
Restart=always

[Install]
WantedBy=default.target""",
            },
            {
                "heading": "Menyalakan layanan Quadlet",
                "bahasa": "terminal",
                "code": """systemctl --user daemon-reload
systemctl --user start situs.service
systemctl --user status situs.service
loginctl enable-linger $USER     # layanan tetap jalan walau kamu logout""",
            },
            {
                "body": [
                    "Quadlet menggantikan cara lama podman generate systemd, yang sudah",
                    "dinyatakan usang. Bagian [Install] di berkas .container yang membuat",
                    "layanannya menyala otomatis saat boot, jadi kamu nggak perlu",
                    "systemctl enable. Tanpa enable-linger, layanan milik pengguna biasa",
                    "berhenti begitu pengguna itu logout.",
                    "",
                    "Saat materi ini ditulis, versi terbaru Podman adalah 6.1.4 (12 Oktober",
                    "2026). Cabang 5.8 masih dirawat dan dapat rilis 5.8.9 di hari yang",
                    "sama, dan Fedora 44 masih memaketkan cabang 5.8. Lisensinya Apache-2.0.",
                    "Di Survei Stack Overflow 2026, Podman dipakai 13,0% responden kategori",
                    "pengembangan cloud, naik dari 11,1% di survei 2025. Untuk tampilan",
                    "grafis seperti Docker Desktop, ada Podman Desktop.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Server keluarga Red Hat di perusahaan sering melarang daemon Docker",
                    "karena alasan keamanan, dan memakai Podman yang sudah disertakan",
                    "distronya. Homelab berbasis Fedora juga banyak menjalankan layanan",
                    "seperti Jellyfin atau Nextcloud sebagai berkas Quadlet.",
                    "",
                    "Kasus kecil: kamu ingin situs portofolio statismu tetap hidup di mini",
                    "PC Fedora di rumah, menyala sendiri setelah listrik padam, tanpa",
                    "memasang Docker dan tanpa hak root. Percobaan pertama dengan",
                    "podman run -p 80:80 langsung gagal.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Port 80 butuh hak khusus untuk pengguna biasa. Pakai 8080 dulu.",
                    "  2. Tulis berkas situs.container seperti contoh di atas di",
                    "     ~/.config/containers/systemd/, dengan nama image lengkap dan Z di",
                    "     volume karena Fedora memakai SELinux.",
                    "  3. Jalankan systemctl --user daemon-reload dan",
                    "     systemctl --user start situs.service, lalu buka",
                    "     http://localhost:8080.",
                    "  4. Jalankan loginctl enable-linger $USER, lalu restart mini PC-nya",
                    "     dan cek apakah situsnya menyala sendiri tanpa kamu login.",
                ],
            },
        ],
    },
    {
        "title": "15. Registry dan Runtime: Docker Hub, containerd, LXC",
        "sections": [
            {
                "body": [
                    "Sejauh ini kamu mengetik nama image seperti postgres:17 lalu image itu",
                    "muncul begitu saja. Materi ini membuka dua kotak hitam. Pertama, dari",
                    "mana image datang dan ke mana image buatanmu disimpan. Kedua, program",
                    "apa yang menjalankan container waktu kamu mengetik docker",
                    "run. Di akhir ada peta singkat soal system container dan virtualisasi,",
                    "yang sering muncul di server kantor dan homelab.",
                ],
            },
            {
                "heading": "Membaca nama image lengkap",
                "body": [
                    "Nama image lengkap terdiri dari beberapa bagian:",
                    "",
                    "  ghcr.io/contoh/tim/toko:1.4.0@sha256:9f86d081...",
                    "  |       |          |    |     |",
                    "  |       |          |    |     digest: sidik jari isi image",
                    "  |       |          |    tag: label versi",
                    "  |       |          nama repositori",
                    "  |       namespace: pemilik (pengguna atau organisasi)",
                    "  registry: server tempat image disimpan",
                    "",
                    "Kalau bagian depan dihilangkan, Docker mengisi bawaannya. nginx berarti",
                    "docker.io/library/nginx:latest. library adalah namespace khusus untuk",
                    "image resmi di Docker Hub. bitnami/redis berarti",
                    "docker.io/bitnami/redis:latest. Bagian pertama dianggap registry cuma",
                    "kalau memuat titik, titik dua, atau berupa localhost, seperti ghcr.io",
                    "atau localhost:5000.",
                    "",
                    "Bedanya tag dan digest penting sekali. Tag bisa dipindah: pemilik image",
                    "boleh mendorong isi baru dengan tag yang sama. Digest adalah hash",
                    "sha256 dari isi image, jadi digest yang sama pasti isinya sama.",
                ],
            },
            {
                "heading": "Tag bisa ditimpa, digest tidak",
                "code": """import hashlib

registry = {}   # tag -> digest
blob = {}       # digest -> isi image


def push(tag, isi):
    digest = "sha256:" + hashlib.sha256(isi.encode()).hexdigest()[:12]
    registry[tag] = digest
    blob[digest] = isi
    print(f"push {tag:<12} -> {digest}")
    return digest


d1 = push("toko:1.4", "kode versi 1.4.0")
push("toko:1.4", "kode versi 1.4.1")      # tag yang sama ditimpa

print("tarik toko:1.4     :", blob[registry["toko:1.4"]])
print("tarik toko@" + d1, ":", blob[d1])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  push toko:1.4     -> sha256:ec4f475d2bc4",
                    "  push toko:1.4     -> sha256:5aea77493fcd",
                    "  tarik toko:1.4     : kode versi 1.4.1",
                    "  tarik toko@sha256:ec4f475d2bc4 : kode versi 1.4.0",
                    "",
                    "Digest di contoh ini dipotong jadi 12 huruf supaya muat; digest asli",
                    "panjangnya 64 huruf heksadesimal. Sesudah tag toko:1.4 ditimpa, siapa",
                    "pun yang menarik lewat tag dapat versi baru. Yang menarik lewat digest",
                    "tetap dapat versi lama, persis yang ia minta. Sistem yang butuh",
                    "kepastian, seperti manifest Kubernetes di produksi, sering menulis",
                    "digest untuk alasan ini.",
                ],
            },
            {
                "heading": "Registry yang bakal kamu temui",
                "body": [
                    "  Registry                   Pemilik     Keterangan",
                    "  Docker Hub (docker.io)     Docker      terbesar, image resmi, batas tarik",
                    "  GHCR (ghcr.io)             GitHub      terhubung ke repositori GitHub",
                    "  Amazon ECR                 AWS         privat, dipakai bersama EKS dan ECS",
                    "  Artifact Registry          Google      pengganti Container Registry lama",
                    "  Azure Container Registry   Microsoft   untuk layanan Azure",
                    "  Harbor                     CNCF        open source, dipasang sendiri",
                    "",
                    "Docker Hub membatasi jumlah tarikan. Menurut dokumentasi resminya,",
                    "pengguna tanpa login dibatasi 100 tarikan per 6 jam per alamat IPv4",
                    "(atau per blok IPv6 /64), dan akun Personal gratis 200 tarikan per 6",
                    "jam. Server CI yang berbagi satu alamat IP bisa menabrak batas ini.",
                    "Solusinya login dengan akun, memakai cermin (mirror) registry, atau",
                    "menyimpan salinan image di registry sendiri.",
                    "",
                    "GHCR praktis untuk proyek di GitHub, karena pipeline GitHub Actions",
                    "bisa mendorong image ke sana tanpa akun tambahan. Setiap penyedia cloud",
                    "punya registry sendiri yang terhubung dengan sistem izinnya. Google",
                    "Container Registry yang lama sudah dihentikan dan digantikan Artifact",
                    "Registry.",
                    "",
                    "Harbor adalah registry open source yang dipasang sendiri, lengkap",
                    "dengan pengaturan hak akses per proyek, pemindaian celah keamanan, dan",
                    "replikasi ke registry lain. Versi terbarunya 2.15.4 (9 Oktober 2026),",
                    "dan statusnya proyek graduated di CNCF (Cloud Native Computing",
                    "Foundation), yayasan yang juga menaungi Kubernetes. Perusahaan sering",
                    "memakainya sebagai registry privat sekaligus cache untuk Docker Hub.",
                    "",
                    "Jebakan: menggantungkan diri pada image pihak ketiga tanpa salinan",
                    "sendiri. Mulai 28 Agustus 2025, Bitnami (milik Broadcom) memindahkan",
                    "image gratisnya ke docker.io/bitnamilegacy tanpa pembaruan lagi. Banyak",
                    "compose.yaml dan chart Helm yang menulis bitnami/postgresql atau",
                    "bitnami/redis mendadak gagal menarik image atau tertinggal di versi",
                    "lama.",
                ],
            },
            {
                "heading": "Siapa yang sebenarnya menjalankan container",
                "body": [
                    "Perintah docker run melewati beberapa lapis program:",
                    "",
                    "  1. docker, perintah yang kamu ketik, mengirim permintaan ke dockerd.",
                    "  2. dockerd (Docker Engine) mengurus image, jaringan, dan volume, lalu",
                    "     menyerahkan urusan container ke containerd.",
                    "  3. containerd mengurus siklus hidup container: menarik layer,",
                    "     menyiapkan sistem berkas, menyalakan, dan menghentikan.",
                    "  4. runc membuat proses container sungguhan dengan namespaces dan",
                    "     cgroups, lalu menyerahkan prosesnya ke containerd.",
                    "",
                    "Semua lapis itu bisa saling ganti karena mengikuti standar OCI (Open",
                    "Container Initiative): format image, cara menjalankan container, dan",
                    "cara registry membagikan image. Image yang dibangun Docker bisa",
                    "dijalankan Podman, dan sebaliknya.",
                    "",
                    "containerd adalah proyek graduated CNCF. Versi terbarunya 2.4.2",
                    "(13 Oktober 2026), dan versi itulah yang dibawa Docker Engine 29.9.1.",
                    "Selain dipakai Docker, containerd jadi runtime bawaan layanan",
                    "Kubernetes terkelola seperti EKS, GKE, dan AKS, juga k3s.",
                    "",
                    "Kubernetes berbicara dengan runtime lewat antarmuka bernama CRI",
                    "(Container Runtime Interface). Sejak Kubernetes 1.24 (2022), Kubernetes",
                    "nggak lagi bisa memakai Docker Engine secara langsung; ia memakai",
                    "containerd atau CRI-O. CRI-O adalah runtime ringan yang dibuat khusus",
                    "untuk Kubernetes dan dipakai OpenShift. Nomor versinya mengikuti",
                    "Kubernetes; versi terbarunya 1.37.2 (2 Oktober 2026). Image buatan",
                    "Docker tetap jalan di sana, karena semuanya mengikuti standar OCI.",
                ],
            },
            {
                "heading": "System container dan virtualisasi",
                "body": [
                    "Container Docker dan Podman disebut application container: isinya satu",
                    "aplikasi, dan ia mati kalau aplikasinya berhenti. Ada jenis lain,",
                    "system container, yang berisi satu sistem Linux utuh lengkap dengan",
                    "systemd. Rasanya seperti VM ringan: kamu bisa SSH ke dalamnya, memasang",
                    "paket dengan dnf, dan menjalankan banyak layanan.",
                    "",
                    "  Nama           Jenis                Keterangan",
                    "  LXC            system container     dasar dari semuanya, sudah lama ada",
                    "  LXD            pengelola LXC        sekarang dikelola Canonical",
                    "  Incus          pengelola LXC + VM   fork komunitas dari LXD sejak 2023",
                    "  Proxmox VE     platform virtualisasi VM KVM dan LXC lewat panel web",
                    "  VMware vSphere platform virtualisasi masih dominan di pusat data",
                    "",
                    "Incus lahir tahun 2023 sesudah LXD keluar dari komunitas",
                    "linuxcontainers.org. Saat materi ini ditulis, cabang dukungan panjang",
                    "Incus 7.0 dapat rilis 7.0.2 (16 Oktober 2026), dan rilis fitur",
                    "terbarunya 7.5.1. Incus enak dipakai untuk lab berisi banyak \"mesin\"",
                    "Linux di satu laptop.",
                    "",
                    "Proxmox VE (versi 9.2, Mei 2026, lisensi AGPL-3.0) menjalankan VM dan",
                    "container LXC dari satu antarmuka web, dan banyak dipakai di homelab",
                    "serta kantor kecil-menengah. Banyak perusahaan meliriknya sejak",
                    "Broadcom mengubah cara lisensi VMware pada 2024. Meski begitu, VMware",
                    "vSphere masih menguasai banyak pusat data perusahaan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pipeline CI yang membangun image biasanya mendorongnya ke GHCR, ECR,",
                    "atau registry perusahaan, lalu server produksi menariknya dari sana.",
                    "Banyak perusahaan menaruh Harbor atau cermin registry di jaringannya",
                    "supaya ratusan mesin CI nggak menabrak batas tarik Docker Hub.",
                    "",
                    "Kasus kecil: pipeline CI di kantor tiba-tiba gagal di langkah docker",
                    "pull dengan pesan toomanyrequests, dan beberapa build lain gagal karena",
                    "image bitnami/redis yang mereka pakai nggak bisa ditarik lagi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pesan toomanyrequests berarti batas tarik Docker Hub. Semua mesin",
                    "     CI keluar lewat satu alamat IP kantor dan menarik tanpa login,",
                    "     jadi berbagi jatah 100 tarikan per 6 jam.",
                    "  2. Login ke Docker Hub dari CI dengan akun organisasi, lalu pasang",
                    "     Harbor atau cermin registry sebagai cache supaya image yang sama",
                    "     cuma ditarik sekali.",
                    "  3. Untuk image Bitnami, ganti ke image resmi di Docker Hub, misalnya",
                    "     docker.io/library/redis:8, lalu sesuaikan variabel lingkungannya",
                    "     karena nama variabel image Bitnami berbeda.",
                    "  4. Salin image yang dipakai produksi ke registry sendiri dan tulis",
                    "     digest-nya, supaya build nggak lagi bergantung pada keputusan",
                    "     pemilik image di luar.",
                ],
            },
        ],
    },
    {
        "title": "16. GitHub Actions: Pipeline Pertama dari Commit ke Tes",
        "sections": [
            {
                "body": [
                    "Pernah dengar kalimat \"di laptopku jalan kok\"? Kode yang lulus di laptop",
                    "satu orang belum tentu lulus di laptop orang lain. Bisa jadi ada paket yang",
                    "lupa dicatat, versi Python-nya beda, atau tesnya memang nggak pernah",
                    "dijalankan sebelum di-push.",
                    "",
                    "CI/CD menjawab masalah itu dengan menyerahkan pengecekan ke mesin yang",
                    "netral. Tiap kali ada perubahan, mesin itu mengambil kode terbaru, memasang",
                    "semua dependensinya dari nol, lalu menjalankan tes. Hasilnya kelihatan oleh",
                    "semua orang di tim.",
                    "",
                    "  - CI (continuous integration): tiap perubahan langsung digabung dan dites",
                    "    otomatis, jadi kesalahan ketahuan beberapa menit sesudah ditulis, bukan",
                    "    berminggu-minggu kemudian.",
                    "  - CD (continuous delivery): kode yang lulus tes selalu siap dirilis.",
                    "    Tombol rilisnya masih ditekan manusia.",
                    "  - CD (continuous deployment): sama, tapi rilisnya juga otomatis. Lulus tes",
                    "    berarti langsung sampai ke pengguna.",
                    "",
                    "Rangkaian langkah otomatis itu disebut pipeline. Gampangnya, pipeline itu",
                    "jalur perakitan: kode masuk di satu ujung, lewat pos cek satu per satu, dan",
                    "keluar di ujung lain sebagai aplikasi yang siap dipakai. Kalau satu pos",
                    "menolak, jalurnya berhenti di situ.",
                ],
            },
            {
                "heading": "Istilah yang dipakai GitHub Actions",
                "body": [
                    "GitHub Actions adalah layanan CI/CD bawaan GitHub. Kamu nggak perlu memasang",
                    "server apa pun. Cukup taruh berkas YAML di repositori, dan GitHub yang",
                    "menjalankannya. Ada lima istilah yang bakal muncul terus:",
                    "",
                    "  - Workflow: satu berkas YAML di folder .github/workflows. Satu repositori",
                    "    boleh punya banyak workflow.",
                    "  - Event: kejadian yang memicu workflow, misalnya push, pull_request,",
                    "    jadwal (schedule), atau tombol manual (workflow_dispatch).",
                    "  - Job: sekumpulan langkah yang jalan di satu mesin. Job yang berbeda jalan",
                    "    di mesin yang berbeda dan, kalau nggak diatur, jalan bersamaan.",
                    "  - Step: satu langkah di dalam job. Isinya perintah shell (run) atau action",
                    "    siap pakai buatan orang lain (uses).",
                    "  - Runner: mesin yang menjalankan job. GitHub menyediakan runner Linux,",
                    "    Windows, dan macOS, atau kamu bisa memasang runner sendiri (self-hosted",
                    "    runner).",
                    "",
                    "Action adalah langkah yang sudah dikemas dan dibagikan, misalnya",
                    "actions/checkout untuk mengambil isi repositori. Kamu memanggilnya dengan",
                    "nama pemilik, nama repo, dan versinya.",
                ],
            },
            {
                "heading": "Workflow pertama",
                "body": [
                    "Simpan berkas ini sebagai .github/workflows/tes.yml di repositori Python",
                    "yang punya requirements.txt dan folder tests:",
                ],
                "code": """name: Tes

on:
  push:
    branches: [main]
  pull_request:

jobs:
  tes:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: "3.14"
      - run: pip install -r requirements.txt
      - run: python -m pytest""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Baca dari atas ke bawah:",
                    "",
                    "  - name: nama yang tampil di tab Actions.",
                    "  - on: workflow ini jalan saat ada push ke cabang main dan saat ada pull",
                    "    request.",
                    "  - jobs.tes: satu job bernama tes. runs-on memilih runner Ubuntu versi",
                    "    terbaru yang disediakan GitHub, dan timeout-minutes menghentikan job",
                    "    yang macet sesudah 15 menit.",
                    "  - steps: ambil kode, pasang Python 3.14, pasang dependensi, lalu jalankan",
                    "    pytest.",
                    "",
                    "Versi di belakang @ menunjuk rilis action-nya. Saat materi ini ditulis",
                    "(Oktober 2026), actions/checkout dan actions/setup-python sama-sama sudah di",
                    "seri v7, keduanya dirilis Juli 2026. Workflow dari artikel lama yang masih",
                    "memakai @v3 atau @v4 sering masih jalan, tapi GitHub memberi peringatan soal",
                    "versi Node.js yang sudah pensiun di dalam action itu.",
                    "",
                    "Step run dianggap gagal kalau perintahnya keluar dengan kode selain nol.",
                    "pytest keluar dengan kode 1 kalau ada tes yang gagal, jadi job ikut gagal,",
                    "dan commit-mu dapat tanda silang merah.",
                ],
            },
            {
                "heading": "Apa yang terjadi saat kamu push",
                "body": [
                    "Begitu commit sampai di GitHub, layanan Actions membaca semua berkas di",
                    ".github/workflows dan mencari yang event-nya cocok. Untuk tiap job, GitHub",
                    "menyalakan mesin virtual baru yang masih bersih. Mesin itu nggak ingat apa",
                    "pun dari run sebelumnya, makanya langkah pertama hampir selalu checkout.",
                    "",
                    "Sesudah job selesai, mesinnya dibuang. Log tiap step bisa kamu buka di tab",
                    "Actions. Kalau workflow dipicu pull request, hasilnya juga muncul di halaman",
                    "pull request itu, jadi peninjau tahu tesnya lulus sebelum mereka membaca",
                    "kodenya.",
                ],
            },
            {
                "heading": "Job berurutan dengan needs",
                "body": [
                    "Job dalam satu workflow jalan bersamaan kecuali kamu bilang lain. Kata kunci",
                    "needs membuat sebuah job menunggu job lain lulus dulu. Kalau job",
                    "prasyaratnya gagal, job yang menunggu ikut dilewati.",
                ],
                "code": """jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - run: pipx run ruff check .

  tes:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - run: python -m pytest

  build:
    needs: tes
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - run: docker build -t aplikasi:${{ github.sha }} .""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Baris if membuat job build cuma jalan di cabang main. Di pull request, lint",
                    "dan tes tetap jalan, tapi build dilewati. Ekspresi ${{ github.sha }} diganti",
                    "GitHub dengan hash commit yang sedang diproses, jadi tiap image punya tag",
                    "yang unik.",
                    "",
                    "Kumpulan job beserta needs-nya membentuk DAG (directed acyclic graph), yaitu",
                    "graf berarah yang nggak boleh melingkar. Program kecil di bawah meniru cara",
                    "GitHub menentukan job mana yang boleh jalan di tiap putaran:",
                ],
                "code": """needs = {
    "lint": [],
    "tes": ["lint"],
    "build": ["tes"],
    "dokumen": ["lint"],
    "deploy": ["build", "dokumen"],
}

selesai = []
putaran = 0
while len(selesai) < len(needs):
    putaran += 1
    siap = [job for job, syarat in needs.items()
            if job not in selesai and all(s in selesai for s in syarat)]
    print(f"putaran {putaran}: {', '.join(siap)}")
    selesai += siap""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  putaran 1: lint",
                    "  putaran 2: tes, dokumen",
                    "  putaran 3: build",
                    "  putaran 4: deploy",
                    "",
                    "Job tes dan dokumen sama-sama cuma menunggu lint, jadi keduanya jalan",
                    "bersamaan di putaran 2. Deploy baru jalan sesudah build dan dokumen selesai.",
                    "Kalau needs-nya melingkar, GitHub menolak workflow itu sebelum satu job pun",
                    "jalan.",
                ],
            },
            {
                "heading": "Biaya, batas, dan jebakan",
                "body": [
                    "Untuk repositori publik, runner standar GitHub gratis. Repositori privat",
                    "dapat jatah menit gratis per bulan sesuai paket akunmu, dan kelebihannya",
                    "ditagih per menit. Per 1 Januari 2026 GitHub menurunkan harga runner yang",
                    "mereka sediakan sampai 39 persen. Rencana memungut biaya untuk runner yang",
                    "kamu pasang sendiri sempat diumumkan untuk Maret 2026, lalu ditunda setelah",
                    "banyak protes.",
                    "",
                    "Tanpa timeout-minutes, satu job baru dihentikan paksa sesudah 360 menit",
                    "(enam jam). Tes yang macet karena menunggu input bisa menghabiskan jatah",
                    "menit sebulan dalam beberapa run, jadi pasang batas yang masuk akal.",
                    "",
                    "Jebakan: berkas workflow wajib ada di .github/workflows, bukan",
                    ".github/workflow atau folder lain. Salah satu huruf saja, GitHub nggak",
                    "memberi pesan galat apa pun dan workflow-nya nggak pernah jalan.",
                    "",
                    "Jebakan: indentasi YAML. steps yang menjorok satu spasi kurang dibaca",
                    "sebagai kunci lain. Tab Actions biasanya menunjukkan baris yang salah, jadi",
                    "buka tab itu dulu sebelum menebak-nebak.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua proyek open source besar di GitHub menjalankan workflow tes di",
                    "tiap pull request. Buka repositori pustaka Python populer mana pun, lalu",
                    "lihat folder .github/workflows dan tab Actions-nya. Di sana kelihatan",
                    "seberapa sering tes mereka jalan dan run mana saja yang gagal.",
                    "",
                    "Kasus kecil: kamu dan dua teman PKL mengerjakan satu repositori. Sudah dua",
                    "kali cabang main rusak karena ada yang push tanpa menjalankan tes, dan",
                    "kalian baru sadar besoknya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat .github/workflows/tes.yml seperti contoh di atas, lalu push ke",
                    "     cabang baru dan buka pull request.",
                    "  2. Buka tab Actions. Kalau run pertama merah, klik step yang gagal dan",
                    "     baca baris terakhir log-nya, biasanya paket yang lupa dicatat di",
                    "     requirements.txt.",
                    "  3. Di Settings, bagian Branches atau Rulesets, lindungi cabang main dan",
                    "     wajibkan job tes lulus sebelum pull request boleh di-merge.",
                    "  4. Minta satu teman membuat pull request yang sengaja merusak satu tes.",
                    "     Tombol merge harus terkunci sampai tesnya diperbaiki.",
                ],
            },
        ],
    },
    {
        "title": "17. GitHub Actions: Matriks, Cache, dan Artefak",
        "sections": [
            {
                "body": [
                    "Workflow pertama di materi sebelumnya menguji kodemu di satu versi Python",
                    "dan satu sistem operasi. Itu cukup untuk aplikasi yang cuma jalan di satu",
                    "server. Lain cerita kalau kamu menulis pustaka yang dipakai orang lain: ada",
                    "yang masih di Python 3.12, ada yang sudah 3.14, ada yang pakai Windows.",
                    "",
                    "Bab ini membahas tiga fitur yang dipakai hampir semua workflow serius.",
                    "Matriks menguji banyak kombinasi sekaligus. Cache mempercepat run dengan",
                    "menyimpan hasil unduhan. Artefak menyimpan berkas hasil job supaya bisa",
                    "dipakai job lain atau diunduh.",
                ],
            },
            {
                "heading": "Matriks: satu job, banyak kombinasi",
                "body": [
                    "strategy.matrix berisi daftar nilai. GitHub membuat satu job untuk tiap",
                    "kombinasi nilai, dan nilainya bisa dibaca lewat ekspresi ${{ matrix.nama }}.",
                ],
                "code": """jobs:
  tes:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest]
        python: ["3.12", "3.13", "3.14"]
        exclude:
          - os: windows-latest
            python: "3.12"
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: ${{ matrix.python }}
      - run: python -m pytest""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Dua sistem operasi kali tiga versi Python menghasilkan enam kombinasi.",
                    "exclude membuang satu, jadi yang jalan lima job. Versi Python sengaja",
                    "ditulis dalam tanda kutip. Tanpa kutip, YAML membaca 3.10 sebagai angka 3.1,",
                    "dan setup-python akan memasang versi yang salah.",
                    "",
                    "Program ini menghitung kombinasi dengan cara yang sama, memakai",
                    "itertools.product (perkalian kartesius, yaitu semua pasangan yang mungkin",
                    "dari beberapa daftar):",
                ],
                "code": """import itertools

matriks = {
    "os": ["ubuntu-latest", "windows-latest"],
    "python": ["3.12", "3.13", "3.14"],
}
exclude = [{"os": "windows-latest", "python": "3.12"}]

kunci = list(matriks)
semua = [dict(zip(kunci, nilai))
         for nilai in itertools.product(*matriks.values())]
jobs = [k for k in semua
        if not any(all(k[x] == v for x, v in e.items()) for e in exclude)]

for i, job in enumerate(jobs, 1):
    print(i, job["os"], job["python"])
print("dibuang exclude:", len(semua) - len(jobs))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  1 ubuntu-latest 3.12",
                    "  2 ubuntu-latest 3.13",
                    "  3 ubuntu-latest 3.14",
                    "  4 windows-latest 3.13",
                    "  5 windows-latest 3.14",
                    "  dibuang exclude: 1",
                    "",
                    "Selain exclude ada include, yang menambah nilai ke kombinasi yang sudah ada",
                    "atau membuat kombinasi baru. Aturannya agak licin dan jadi bahan latihan di",
                    "akhir bab ini.",
                    "",
                    "  - fail-fast: bawaannya true. Begitu satu job matriks gagal, job lain yang",
                    "    belum selesai dibatalkan. Set false kalau kamu ingin melihat semua",
                    "    kombinasi yang gagal.",
                    "  - max-parallel: batas job matriks yang jalan bersamaan, berguna kalau",
                    "    tesnya memukul server uji yang kecil.",
                    "  - Satu matriks paling banyak menghasilkan 256 job per run workflow.",
                ],
            },
            {
                "heading": "Cache: jangan unduh ulang yang sama",
                "body": [
                    "Tiap job mulai di mesin bersih, jadi pip mengunduh ulang semua paket di",
                    "setiap run. Untuk proyek dengan dependensi besar, itu bisa makan beberapa",
                    "menit. Cache menyimpan folder tertentu di akhir job, lalu mengembalikannya",
                    "di run berikutnya kalau kuncinya cocok.",
                ],
                "code": """      - uses: actions/setup-python@v7
        with:
          python-version: "3.14"
          cache: pip

      # atau, untuk folder apa pun:
      - uses: actions/cache@v6
        with:
          path: ~/.cache/pip
          key: pip-${{ runner.os }}-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            pip-${{ runner.os }}-""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Kunci cache memuat hash isi requirements.txt. Selama berkas itu nggak",
                    "berubah, kuncinya sama dan cache dipakai. Begitu kamu menambah paket, hash",
                    "berubah, kunci baru dibuat, dan pip mengunduh paket yang kurang saja kalau",
                    "restore-keys menemukan cache lama yang awalannya cocok.",
                    "",
                    "Batasnya: total cache satu repositori bawaannya 10 GB. Cache yang nggak",
                    "diakses lebih dari tujuh hari dihapus, dan kalau batasnya terlewati, yang",
                    "paling lama nggak dipakai dibuang duluan.",
                    "",
                    "Jebakan: cache itu sekadar mempercepat, bukan tempat menyimpan hasil.",
                    "Workflow harus tetap lulus kalau cache-nya kosong. Kalau kodemu cuma jalan",
                    "saat cache ada, berarti ada langkah pemasangan yang hilang.",
                ],
            },
            {
                "heading": "Artefak: berkas hasil job",
                "body": [
                    "Artefak adalah berkas yang kamu simpan dari sebuah job: hasil build, laporan",
                    "coverage, atau log. Artefak bisa diunduh dari halaman run, dan bisa diambil",
                    "job lain di workflow yang sama.",
                ],
                "code": """jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - run: python -m pip install build && python -m build
      - uses: actions/upload-artifact@v7
        with:
          name: paket
          path: dist/
          retention-days: 14

  rilis:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v8
        with:
          name: paket
          path: dist/
      - run: ls dist/""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Tanpa retention-days, artefak disimpan 90 hari. Sejak upload-artifact v4,",
                    "artefak dengan nama yang sama nggak bisa diunggah dua kali dalam satu run,",
                    "jadi job matriks perlu nama berbeda, misalnya paket-${{ matrix.os }}. Saat",
                    "materi ini ditulis, upload-artifact ada di v7 dan download-artifact di v8.",
                    "",
                    "Perbedaan cache dan artefak gampang diingat dari pertanyaannya. Cache",
                    "menjawab \"bisa lebih cepat nggak?\" untuk barang yang jarang berubah, seperti",
                    "paket unduhan. Artefak menjawab \"hasilnya mana?\" untuk barang yang dibuat",
                    "run ini, seperti berkas .whl atau laporan tes.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pustaka Python populer biasanya menguji tiap pull request di beberapa versi",
                    "Python dan beberapa sistem operasi lewat matriks. Kamu bisa melihat daftar",
                    "job matriksnya di tab Actions repositori mereka: tiap baris di sana satu",
                    "kombinasi.",
                    "",
                    "Kasus kecil: workflow tes timmu butuh 9 menit, dan 6 menit di antaranya",
                    "habis untuk pip install. Kalian juga ingin memastikan aplikasinya jalan di",
                    "Python 3.13 dan 3.14.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambahkan cache: pip di langkah setup-python, lalu jalankan workflow",
                    "     dua kali. Run kedua harus menulis cache hit di log.",
                    "  2. Ubah job tes jadi matriks python: [\"3.13\", \"3.14\"], dengan versi dalam",
                    "     tanda kutip.",
                    "  3. Set fail-fast: false selama masa peralihan, supaya kalian tahu versi",
                    "     mana saja yang gagal.",
                    "  4. Unggah laporan pytest sebagai artefak bernama laporan-${{ matrix.python",
                    "     }} supaya namanya nggak bentrok.",
                ],
            },
        ],
    },
    {
        "title": "18. GitHub Actions: Secrets, OIDC, dan Keamanan Workflow",
        "sections": [
            {
                "body": [
                    "Begitu workflow-mu mulai men-deploy, ia butuh kunci: token registry, kata",
                    "sandi database, akses ke akun cloud. Workflow juga menjalankan kode dari",
                    "banyak pihak, mulai dari action buatan orang lain sampai pull request dari",
                    "orang yang nggak kamu kenal. Dua hal itu kalau digabung jadi sasaran empuk.",
                    "",
                    "Materi ini membahas tiga lapis pengaman: menyimpan rahasia dengan benar,",
                    "mengganti kunci statis dengan OIDC, dan menutup celah rantai pasok di",
                    "workflow itu sendiri. Topik keamanan yang lebih luas ada di kurikulum",
                    "Keamanan Siber.",
                ],
            },
            {
                "heading": "Secrets dan GITHUB_TOKEN",
                "body": [
                    "Secret adalah nilai rahasia yang kamu simpan di Settings, Secrets and",
                    "variables. Di workflow, kamu memanggilnya lewat ekspresi secrets diikuti",
                    "nama secret-nya. GitHub menyamarkan nilainya jadi *** di log, dan secret",
                    "nggak dikirim ke workflow yang dipicu pull request dari fork, supaya orang",
                    "asing nggak bisa mencurinya lewat pull request.",
                    "",
                    "Secret bisa diikat ke environment, misalnya production. Environment bisa",
                    "diberi syarat peninjau, jadi job yang memakai secret produksi menunggu",
                    "persetujuan manusia dulu sebelum jalan.",
                    "",
                    "Selain secret buatanmu, tiap run otomatis mendapat GITHUB_TOKEN: token",
                    "sementara untuk repositori itu sendiri, misalnya untuk memberi komentar di",
                    "pull request. Izinnya sebaiknya dipersempit di awal berkas, lalu dibuka per",
                    "job kalau memang perlu:",
                ],
                "code": """permissions:
  contents: read

jobs:
  komentar:
    permissions:
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - run: gh pr comment "$NOMOR" --body "Tes lulus"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NOMOR: ${{ github.event.pull_request.number }}""",
                "bahasa": "yaml",
            },
            {
                "heading": "OIDC: deploy tanpa kunci statis",
                "body": [
                    "Cara lama men-deploy ke AWS dari CI adalah membuat access key untuk satu",
                    "pengguna IAM, lalu menyimpannya sebagai secret. Kunci itu berlaku selamanya",
                    "sampai dicabut. Kalau bocor lewat log, fork, atau laptop seseorang,",
                    "penyerang bisa memakainya dari mana pun.",
                    "",
                    "OIDC (OpenID Connect) membalik caranya. GitHub bertindak sebagai penerbit",
                    "identitas. Saat job jalan, runner meminta token pendek dari GitHub yang",
                    "isinya kurang lebih \"aku job dari repo ini, cabang main\". AWS memeriksa",
                    "token itu, mencocokkannya dengan aturan kepercayaan di sebuah role IAM, lalu",
                    "memberi kredensial sementara yang kedaluwarsa dalam hitungan jam. Nggak ada",
                    "kunci yang disimpan di mana pun.",
                ],
                "code": """permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v7
      - uses: aws-actions/configure-aws-credentials@v6
        with:
          role-to-assume: arn:aws:iam::123456789012:role/deploy-dari-github
          aws-region: ap-southeast-3
      - run: aws s3 sync ./situs s3://contoh-situs-statis --delete""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Izin id-token: write wajib ada, karena tanpanya runner nggak boleh meminta",
                    "token OIDC. ap-southeast-3 adalah region AWS di Jakarta. Di sisi AWS, role",
                    "deploy-dari-github punya aturan kepercayaan yang membatasi siapa yang boleh",
                    "memakainya:",
                ],
                "code": """{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
      "token.actions.githubusercontent.com:sub": "repo:tim-kita/situs:environment:production"
    }
  }
}""",
                "bahasa": "json",
            },
            {
                "body": [
                    "Kunci sub adalah bagian yang paling sering salah. Kalau kamu menulis",
                    "repo:tim-kita/*, semua cabang dan semua workflow di repositori itu boleh",
                    "memakai role produksi, termasuk cabang yang baru dibuat orang lima menit",
                    "lalu. Persempit ke environment atau cabang tertentu. Pola yang sama berlaku",
                    "untuk Google Cloud (Workload Identity Federation) dan Azure (federated",
                    "credential).",
                ],
            },
            {
                "heading": "Rantai pasok: action pihak ketiga",
                "body": [
                    "Baris uses: tj-actions/changed-files@v45 artinya \"jalankan kode apa pun yang",
                    "sekarang ditunjuk tag v45\". Tag di Git bisa dipindah. Itulah yang terjadi",
                    "pada Maret 2025: penyerang mengambil alih akses ke action",
                    "tj-actions/changed-files, yang dipakai puluhan ribu repositori, lalu",
                    "memindahkan tag-tag lamanya ke commit jahat. Commit itu membaca memori",
                    "runner dan mencetak secret ke log workflow. Di repositori publik, log itu",
                    "bisa dibaca siapa saja.",
                    "",
                    "Pengamannya adalah mem-pin action ke SHA commit lengkap, 40 karakter",
                    "heksadesimal. SHA nggak bisa dipindah ke kode lain. Komentar di belakangnya",
                    "mencatat versi supaya manusia tetap bisa membacanya, dan Dependabot bisa",
                    "memperbarui keduanya lewat pull request:",
                ],
                "code": "      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1",
                "bahasa": "yaml",
            },
            {
                "heading": "Injeksi lewat ekspresi",
                "body": [
                    "Ekspresi ${{ }} ditempel ke skrip sebelum shell menjalankannya. Kalau isinya",
                    "datang dari orang luar, misalnya judul pull request, orang itu bisa menulis",
                    "judul berisi perintah shell. Solusinya: masukkan data itu ke variabel",
                    "lingkungan dengan env, lalu pakai variabel itu di dalam tanda kutip, seperti",
                    "nomor pull request di contoh komentar tadi.",
                    "",
                    "Hindari juga pull_request_target untuk menjalankan kode dari pull request.",
                    "Event itu jalan dengan secret repositori tujuan, jadi checkout kode dari",
                    "fork di sana sama dengan menyerahkan secret ke penulis fork. Program di",
                    "bawah memeriksa dua pola berbahaya pertama di sebuah workflow:",
                ],
                "code": "import re\n\nworkflow = \"\"\"\npermissions:\n  contents: read\njobs:\n  sapa:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1\n      - uses: tj-actions/changed-files@v45\n      - run: echo \"Judul: ${{ github.event.pull_request.title }}\"\n\"\"\"\n\nSHA = re.compile(r\"@[0-9a-f]{40}$\")\nfor nomor, baris in enumerate(workflow.splitlines()):\n    teks = baris.strip()\n    if teks.startswith(\"- uses:\") and not SHA.search(teks):\n        print(f\"baris {nomor}: action belum dipin ke SHA\")\n    if \"run:\" in teks and \"${{ github.event.\" in teks:\n        print(f\"baris {nomor}: data event masuk langsung ke shell\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  baris 8: action belum dipin ke SHA",
                    "  baris 9: data event masuk langsung ke shell",
                    "",
                    "Alat sungguhan seperti zizmor dan actionlint mengecek jauh lebih banyak",
                    "pola, dan bisa kamu pasang sebagai job di workflow itu sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setelah kasus tj-actions/changed-files, banyak organisasi mulai mewajibkan",
                    "action dipin ke SHA, dan GitHub menambahkan pengaturan untuk membatasi",
                    "action mana yang boleh dipakai di sebuah organisasi. Panduan pengerasan",
                    "GitHub Actions di dokumentasi resmi GitHub memuat daftar periksanya.",
                    "",
                    "Kasus kecil: workflow deploy situs statis timmu memakai secret",
                    "AWS_ACCESS_KEY_ID dan AWS_SECRET_ACCESS_KEY yang dibuat dua tahun lalu, plus",
                    "tiga action pihak ketiga yang ditulis dengan tag @v2.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat identity provider OIDC untuk token.actions.githubusercontent.com",
                    "     di IAM, lalu role baru dengan sub yang dibatasi ke environment",
                    "     production.",
                    "  2. Ganti langkah kredensial dengan configure-aws-credentials dan",
                    "     role-to-assume, tambahkan permissions id-token: write.",
                    "  3. Sesudah deploy lewat OIDC berhasil, nonaktifkan lalu hapus access key",
                    "     lama, kemudian hapus dua secret-nya.",
                    "  4. Pin ketiga action ke SHA lengkap dengan komentar versinya, dan aktifkan",
                    "     Dependabot untuk ekosistem github-actions.",
                ],
            },
        ],
    },
    {
        "title": "19. GitLab CI dan Jenkins",
        "sections": [
            {
                "body": [
                    "GitHub Actions memang paling banyak dipakai untuk proyek pribadi dan open",
                    "source. Begitu kamu masuk kantor, ceritanya bisa lain. Banyak perusahaan",
                    "menyimpan kodenya di GitLab yang mereka pasang sendiri, atau punya server",
                    "Jenkins yang sudah jalan sepuluh tahun dan menjalankan ratusan job.",
                    "",
                    "Menurut survei CI/CD JetBrains 2025, GitHub Actions dipakai 62 persen",
                    "responden untuk proyek pribadi, GitLab CI 24 persen, dan Jenkins 14 persen.",
                    "Di organisasi, angka GitLab CI dan Jenkins jauh lebih tinggi, walau tiap",
                    "publikasi JetBrains menyebut angka yang sedikit berbeda. Kabar baiknya,",
                    "konsepnya sama: pemicu, job, urutan, artefak. Yang berubah cuma ejaannya.",
                ],
            },
            {
                "heading": "GitLab CI/CD: .gitlab-ci.yml",
                "body": [
                    "GitLab CI/CD terpasang di setiap GitLab, baik gitlab.com maupun GitLab yang",
                    "dipasang sendiri (self-managed). Konfigurasinya satu berkas .gitlab-ci.yml",
                    "di akar repositori, yang di GitLab disebut project. Job dijalankan oleh",
                    "GitLab Runner, program yang bisa kamu pasang di server mana pun.",
                ],
                "code": """stages:
  - tes
  - build
  - deploy

default:
  image: python:3.14-slim

tes-unit:
  stage: tes
  script:
    - pip install -r requirements.txt
    - python -m pytest --junitxml=laporan.xml
  artifacts:
    reports:
      junit: laporan.xml

build-image:
  stage: build
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" .
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

deploy-produksi:
  stage: deploy
  script:
    - ./deploy.sh
  environment: production
  when: manual""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "  - stages menentukan urutan tahap. Semua job di satu stage jalan bersamaan,",
                    "    dan stage berikutnya baru mulai kalau stage sebelumnya lulus. Kalau",
                    "    ingin melompati urutan stage, pakai needs, sama seperti di GitHub",
                    "    Actions.",
                    "  - image memilih image container tempat script jalan. Di GitHub Actions",
                    "    kamu memasang Python dengan action, di GitLab biasanya kamu langsung",
                    "    memilih image yang sudah berisi Python.",
                    "  - rules mengatur kapan job dibuat. Variabel seperti $CI_COMMIT_BRANCH dan",
                    "    $CI_REGISTRY_IMAGE disediakan GitLab.",
                    "  - when: manual membuat job menunggu tombol diklik. Ini cara umum membuat",
                    "    continuous delivery: semua otomatis sampai tepat sebelum produksi.",
                    "  - artifacts:reports:junit membuat hasil tes tampil di halaman merge",
                    "    request, sebutan GitLab untuk pull request.",
                    "",
                    "GitLab merilis versi baru tiap bulan, pada hari Kamis ketiga. Saat materi",
                    "ini ditulis, versi terbarunya GitLab 19.5 (15 Oktober 2026). Edisi Community",
                    "berlisensi MIT, sedangkan edisi Enterprise berbayar.",
                ],
            },
            {
                "heading": "Jenkins: server otomasi tertua yang masih dominan",
                "body": [
                    "Jenkins adalah server CI/CD open source (lisensi MIT) yang kamu pasang dan",
                    "urus sendiri. Ia ditulis dengan Java dan bisa diperluas dengan ribuan",
                    "plugin. Arsitekturnya terdiri dari controller, yaitu server pusat yang",
                    "menyimpan konfigurasi dan antarmuka web, dan agent, yaitu mesin yang",
                    "menjalankan build.",
                    "",
                    "Pipeline Jenkins ditulis di berkas Jenkinsfile dengan bahasa berbasis",
                    "Groovy. Gaya yang dianjurkan adalah declarative pipeline:",
                ],
                "code": """pipeline {
    agent { docker { image 'python:3.14-slim' } }
    options { timeout(time: 15, unit: 'MINUTES') }
    stages {
        stage('Tes') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m pytest --junitxml=laporan.xml'
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                input message: 'Deploy ke produksi?'
                sh './deploy.sh'
            }
        }
    }
    post {
        always { junit 'laporan.xml' }
    }
}""",
                "bahasa": "groovy",
            },
            {
                "body": [
                    "Blok agent memilih tempat build jalan, stages berisi tahap, when membatasi",
                    "stage ke cabang main, input menunggu persetujuan manusia, dan post",
                    "menjalankan langkah sesudah pipeline selesai, apa pun hasilnya. Langkah",
                    "junit di sana butuh plugin JUnit, salah satu dari plugin yang biasanya ikut",
                    "terpasang.",
                    "",
                    "Versi LTS (long-term support) terbaru saat materi ini ditulis adalah Jenkins",
                    "2.580.1, dirilis 30 September 2026. Sejak 2.555.1, Jenkins butuh Java 21",
                    "atau Java 25 di controller. Server lama yang masih memakai Java 17 harus",
                    "memperbarui Java-nya dulu sebelum memperbarui Jenkins.",
                    "",
                    "Jebakan: plugin adalah kekuatan sekaligus titik lemah Jenkins. Plugin yang",
                    "lama nggak diperbarui sering punya celah keamanan, dan pembaruan satu plugin",
                    "bisa merusak plugin lain. Biasakan memasang plugin sesedikit mungkin dan",
                    "membaca daftar peringatan keamanan di halaman Manage Jenkins.",
                    "",
                    "Jebakan: jangan biarkan controller ikut menjalankan build. Build yang jalan",
                    "di controller bisa membaca semua kredensial yang tersimpan di sana. Set",
                    "jumlah executor controller ke nol dan jalankan build di agent.",
                ],
            },
            {
                "heading": "Kapan memilih yang mana",
                "body": [
                    "  - GitHub Actions: kodenya sudah di GitHub, kamu ingin mulai tanpa mengurus",
                    "    server, dan butuh banyak action siap pakai.",
                    "  - GitLab CI/CD: perusahaan memakai GitLab, terutama yang dipasang sendiri",
                    "    karena aturan data harus tinggal di server milik sendiri. Satu aplikasi",
                    "    untuk repositori, CI, registry, dan issue.",
                    "  - Jenkins: sudah ada dan berjalan, butuh integrasi dengan sistem lama yang",
                    "    nggak punya plugin di tempat lain, atau build harus jalan di jaringan",
                    "    tertutup. Untuk proyek baru, tim biasanya memilih CI berbasis YAML.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak bank, perusahaan telekomunikasi, dan instansi yang menyimpan kode di",
                    "jaringan internal memakai GitLab self-managed atau Jenkins. Lowongan DevOps",
                    "di Indonesia sering menyebut salah satunya, jadi kamu akan ketemu",
                    ".gitlab-ci.yml atau Jenkinsfile cepat atau lambat.",
                    "",
                    "Kasus kecil: tempat PKL-mu pindah dari GitHub ke GitLab self-managed, dan",
                    "workflow tes dari materi pertama bab ini harus ikut pindah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Petakan istilahnya: workflow jadi .gitlab-ci.yml, job tetap job,",
                    "     runs-on jadi image (plus tag runner kalau perlu), needs tetap needs.",
                    "  2. Ganti langkah checkout dengan tidak menulis apa pun, karena GitLab",
                    "     Runner mengambil kode secara otomatis.",
                    "  3. Ganti setup-python dengan image: python:3.14-slim, lalu salin perintah",
                    "     pip dan pytest ke script.",
                    "  4. Pindahkan secret ke Settings, CI/CD, Variables, dan tandai Masked serta",
                    "     Protected supaya cuma dipakai di cabang terlindungi.",
                ],
            },
        ],
    },
    {
        "title": "20. Peta CI/CD Lain dan Repositori Artefak",
        "sections": [
            {
                "body": [
                    "Selain tiga alat besar tadi, ada banyak layanan CI/CD lain. Kamu nggak perlu",
                    "mempelajari semuanya. Cukup kenal namanya, tahu posisinya, dan tahu",
                    "statusnya, supaya nggak kaget saat membaca README lama atau lowongan kerja.",
                    "",
                    "Bagian kedua materi ini membahas repositori artefak: tempat menyimpan hasil",
                    "build supaya yang dites dan yang dirilis adalah berkas yang sama.",
                ],
            },
            {
                "heading": "Peta layanan CI/CD",
                "code": """Alat                 Model                       Status (Oktober 2026)
-------------------  --------------------------  ---------------------
CircleCI             SaaS, ada runner sendiri    stabil, pangsa turun
Azure Pipelines      SaaS atau Azure DevOps      stabil
                     Server
Bitbucket Pipelines  SaaS di Bitbucket Cloud     stabil, pangsa kecil
TeamCity             server dari JetBrains       stabil, rilis 2026.2
Buildkite            dasbor SaaS, agent sendiri  aktif, agent v4.6.0
Travis CI            SaaS                        menurun
GoCD                 server open source          menurun, rilis 26.1.0""",
                "bahasa": "teks",
            },
            {
                "body": [
                    "  - CircleCI: layanan CI di cloud dengan orbs, paket konfigurasi siap pakai.",
                    "    Pada Januari 2023 CircleCI meminta semua pelanggan memutar ulang secret",
                    "    mereka karena ada pencurian data di sistemnya. Kejadian itu sering",
                    "    dipakai sebagai contoh kenapa secret perlu bisa diganti dengan cepat.",
                    "  - Azure Pipelines: bagian dari Azure DevOps milik Microsoft, ada versi",
                    "    cloud (Services) dan versi pasang sendiri (Azure DevOps Server).",
                    "    Konfigurasinya juga YAML. Sering ditemui di perusahaan yang memakai .NET",
                    "    dan Azure.",
                    "  - Bitbucket Pipelines: CI bawaan Bitbucket Cloud dari Atlassian. Produk",
                    "    Bitbucket Server sudah berhenti didukung sejak Februari 2024, yang",
                    "    tersisa versi Cloud dan Data Center.",
                    "  - TeamCity: server CI dari JetBrains, pembuat IntelliJ. Ada paket pasang",
                    "    sendiri gratis dengan batas tertentu. Versi terbaru saat materi ini",
                    "    ditulis 2026.2 (September 2026).",
                    "  - Buildkite: dasbor dan pengatur jadwalnya di cloud Buildkite, tapi build",
                    "    jalan di agent yang kamu pasang di mesinmu sendiri. Cocok kalau kode",
                    "    nggak boleh keluar dari jaringan kantor.",
                    "  - Travis CI: pelopor CI untuk proyek open source di GitHub. Kuota",
                    "    gratisnya untuk open source dicabut sekitar 2020-2021, dan banyak proyek",
                    "    pindah ke GitHub Actions. Lencana Travis masih sering terlihat di README",
                    "    lama, tapi jangan dipilih untuk proyek baru.",
                    "  - GoCD: server continuous delivery open source dari Thoughtworks dengan",
                    "    tampilan value stream map. Masih dirilis, tapi komunitasnya kecil.",
                ],
            },
            {
                "heading": "Bangun sekali, promosikan artefak yang sama",
                "body": [
                    "Bayangkan pipeline yang membangun ulang aplikasi di tiap tahap: sekali untuk",
                    "staging, sekali lagi untuk produksi. Kedua build itu bisa berbeda, misalnya",
                    "karena ada paket yang naik versi di antara keduanya. Yang dites di staging",
                    "ternyata bukan yang sampai ke pengguna.",
                    "",
                    "Prinsip yang dipakai tim DevOps: bangun sekali, lalu promosikan berkas yang",
                    "sama dari satu tahap ke tahap berikutnya. Supaya bisa begitu, hasil build",
                    "disimpan di repositori artefak, lengkap dengan checksum. Checksum adalah",
                    "sidik jari isi berkas: satu bita saja berubah, sidik jarinya berubah total.",
                ],
                "code": """import hashlib

repo = {"dev": {}, "staging": {}, "produksi": {}}


def unggah(nama, isi):
    repo["dev"][nama] = hashlib.sha256(isi).hexdigest()
    print(f"unggah {nama} ke dev, sha256 {repo['dev'][nama][:12]}")


def promosi(nama, dari, ke, isi_diterima):
    harap = repo[dari][nama]
    nyata = hashlib.sha256(isi_diterima).hexdigest()
    if nyata != harap:
        print(f"TOLAK {nama}: checksum berubah antara {dari} dan {ke}")
        return
    repo[ke][nama] = harap
    print(f"promosi {nama}: {dari} -> {ke}")


berkas = b"isi aplikasi versi 1.4.0"
unggah("aplikasi-1.4.0.whl", berkas)
promosi("aplikasi-1.4.0.whl", "dev", "staging", berkas)
promosi("aplikasi-1.4.0.whl", "staging", "produksi", berkas + b" disisipi")
print("di produksi:", sorted(repo["produksi"]))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  unggah aplikasi-1.4.0.whl ke dev, sha256 366d2a1ecfef",
                    "  promosi aplikasi-1.4.0.whl: dev -> staging",
                    "  TOLAK aplikasi-1.4.0.whl: checksum berubah antara staging dan produksi",
                    "  di produksi: []",
                    "",
                    "Berkas yang isinya berubah di tengah jalan ditolak, jadi produksi tetap",
                    "kosong sampai ada berkas yang terbukti sama dengan yang dites.",
                ],
            },
            {
                "heading": "Repositori artefak dan otomasi runbook",
                "body": [
                    "  - JFrog Artifactory: repositori artefak universal. Satu server bisa",
                    "    menyimpan paket Maven, npm, PyPI, image Docker, dan chart Helm,",
                    "    sekaligus jadi proxy yang menyimpan salinan paket dari internet. Standar",
                    "    di banyak perusahaan besar. Ada edisi open source yang fiturnya",
                    "    terbatas.",
                    "  - Sonatype Nexus Repository: fungsi serupa. Sejak versi 3.77 edisi",
                    "    gratisnya bernama Community Edition, dan menurut forum komunitas",
                    "    Sonatype, sejak 3.87 edisi itu dibatasi 40.000 komponen dan 100.000",
                    "    permintaan per hari. Versi terbaru yang tercatat saat materi ini ditulis",
                    "    3.97.0.",
                    "  - Registry container seperti GHCR dan Docker Hub, yang dibahas di bab 04,",
                    "    adalah repositori artefak khusus image.",
                    "  - Rundeck: alat otomasi operasional yang sering dipasang di dekat CI.",
                    "    Rundeckmenjalankan prosedur operasional, misalnya restart layanan atau",
                    "    skrip perbaikan, lewat antarmuka web dengan kontrol akses dan catatan",
                    "    audit siapa menjalankan apa. Edisi Community berlisensi Apache-2.0,",
                    "    versi terbaru 6.2.1 (September 2026), dan sejak 2020 dipelihara",
                    "    PagerDuty.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perusahaan yang merilis aplikasi Java atau .NET biasanya punya Artifactory",
                    "atau Nexus di jaringan internal. Pipeline mengunggah berkas .jar atau paket",
                    "NuGet sekali, lalu tahap deploy cuma mengambil berkas dengan versi dan",
                    "checksum tertentu dari sana.",
                    "",
                    "Kasus kecil: pipeline timmu menjalankan docker build tiga kali: di tahap",
                    "tes, staging, dan produksi. Minggu lalu produksi rusak padahal staging",
                    "lulus, karena image dasar sempat diperbarui di antara dua build.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bangun image sekali di job build, beri tag SHA commit, lalu dorong ke",
                    "     registry.",
                    "  2. Tahap staging dan produksi cuma menarik image dengan tag itu, nggak",
                    "     pernah menjalankan docker build lagi.",
                    "  3. Catat digest image (sha256:...) di log rilis, dan deploy memakai digest",
                    "     itu supaya isinya dijamin sama.",
                    "  4. Kalau pakai Artifactory atau Nexus, pisahkan repositori dev, staging,",
                    "     dan produksi, lalu pindahkan artefak lewat promosi.",
                ],
            },
        ],
    },
    {
        "title": "21. Dasar Cloud dan Peta Penyedia: AWS, Google Cloud, Azure",
        "sections": [
            {
                "body": [
                    "Dulu, kalau mau bikin aplikasi yang bisa diakses orang banyak, kamu harus",
                    "beli server, menaruhnya di ruangan berpendingin, dan menunggu",
                    "berminggu-minggu sampai barangnya datang. Kalau ternyata pengunjungnya sepi,",
                    "servernya nganggur. Kalau tiba-tiba ramai, servernya kewalahan dan beli yang",
                    "baru butuh waktu lagi.",
                    "",
                    "Cloud mengubah itu jadi sewa. Kamu menyewa komputer, penyimpanan, dan",
                    "layanan lewat internet, menyalakannya dalam hitungan menit, dan membayar",
                    "sesuai pemakaian. Mirip listrik PLN: kamu nggak membangun pembangkit",
                    "sendiri, cukup bayar per kWh yang terpakai.",
                    "",
                    "Menurut Survei Stack Overflow 2026, 59,5 persen responden memakai platform",
                    "atau alat yang berhubungan dengan cloud. Jadi hampir pasti kamu akan",
                    "bersentuhan dengan salah satunya.",
                ],
            },
            {
                "heading": "IaaS, PaaS, SaaS",
                "body": [
                    "Layanan cloud biasanya dikelompokkan menurut seberapa banyak yang kamu urus",
                    "sendiri:",
                    "",
                    "  - IaaS (Infrastructure as a Service): kamu menyewa mesin virtual,",
                    "    jaringan, dan disk. Sistem operasi, aplikasi, dan pembaruan keamanannya",
                    "    kamu yang urus. Contoh: Amazon EC2.",
                    "  - PaaS (Platform as a Service): kamu cuma mengirim kode atau container,",
                    "    penyedia yang mengurus server dan sistem operasinya. Contoh: Google",
                    "    Cloud Run, Heroku, Render.",
                    "  - SaaS (Software as a Service): aplikasi jadi yang tinggal dipakai lewat",
                    "    browser. Contoh: Gmail, Google Docs.",
                    "",
                    "Makin ke bawah daftar itu, makin sedikit yang kamu urus, tapi makin sedikit",
                    "juga yang bisa kamu atur. Bab berikutnya membahas serverless, yang posisinya",
                    "mirip PaaS tapi lebih kecil lagi: kamu cuma menyerahkan satu fungsi.",
                ],
            },
            {
                "heading": "Region, availability zone, dan shared responsibility",
                "body": [
                    "Penyedia cloud punya pusat data di banyak negara. Satu wilayah geografis",
                    "disebut region, misalnya ap-southeast-3 milik AWS di Jakarta. Di dalam satu",
                    "region ada beberapa availability zone (AZ): pusat data terpisah dengan",
                    "listrik dan jaringan sendiri, cukup dekat untuk saling tersambung cepat.",
                    "Aplikasi yang penting dipasang di minimal dua AZ, supaya kalau satu gedung",
                    "mati, yang lain tetap jalan.",
                    "",
                    "Region terdekat dari Indonesia sekarang ada di Jakarta untuk tiga penyedia",
                    "besar: AWS (ap-southeast-3), Google Cloud (asia-southeast2), dan Azure",
                    "(Indonesia Central). Memilih region dekat pengguna membuat aplikasi terasa",
                    "lebih cepat, dan kadang diwajibkan aturan soal lokasi data.",
                    "",
                    "Shared responsibility model adalah pembagian tanggung jawab keamanan.",
                    "Penyedia menjaga keamanan cloud-nya: gedung, perangkat keras, jaringan inti,",
                    "dan lapisan virtualisasi. Kamu menjaga apa yang kamu taruh di dalamnya:",
                    "data, akun dan izin, sistem operasi di VM, dan konfigurasi. Bucket",
                    "penyimpanan yang terbuka untuk umum karena salah setelan adalah tanggung",
                    "jawabmu, bukan tanggung jawab AWS.",
                ],
            },
            {
                "heading": "Tiga penyedia besar, nama berbeda untuk hal yang sama",
                "body": [
                    "Pangsa pasar infrastruktur cloud kuartal pertama 2026 menurut Synergy",
                    "Research: AWS 28 persen, Microsoft Azure 21 persen, Google Cloud 14 persen.",
                    "Di Survei Stack Overflow 2026, AWS dipakai 41,8 persen responden, Azure 25,1",
                    "persen, dan Google Cloud 24,5 persen.",
                    "",
                    "Kabar baiknya, konsepnya sama di ketiganya. Yang berbeda cuma nama. Bab ini",
                    "memakai AWS sebagai contoh karena paling banyak dipakai. Tabel ini membantu",
                    "kalau kantormu ternyata memakai yang lain:",
                ],
                "code": """Kebutuhan            AWS                 Google Cloud          Azure
-------------------  ------------------  --------------------  ----------------------
Mesin virtual        EC2                 Compute Engine        Virtual Machines
Jaringan privat      VPC                 VPC                   Virtual Network
Object storage       S3                  Cloud Storage         Blob Storage
Database relasional  RDS, Aurora         Cloud SQL, AlloyDB    Azure Database
NoSQL terkelola      DynamoDB            Firestore, Bigtable   Cosmos DB
Identitas & izin     IAM                 Cloud IAM             Entra ID + Azure RBAC
DNS                  Route 53            Cloud DNS             Azure DNS
Load balancer        ELB (ALB, NLB)      Cloud Load Balancing  Load Balancer
Pemantauan           CloudWatch          Cloud Observability   Azure Monitor
Fungsi serverless    Lambda              Cloud Run functions   Azure Functions
IaC bawaan           CloudFormation      Infrastructure Mgr    ARM / Bicep""",
                "bahasa": "teks",
            },
            {
                "heading": "Penyedia lain yang perlu kamu kenal",
                "body": [
                    "  - Oracle Cloud Infrastructure (OCI): kuat untuk database Oracle. Paket",
                    "    Always Free-nya paling longgar untuk belajar: mesin Ampere A1 setara",
                    "    empat inti prosesor dan 24 GB RAM, plus kredit uji coba US$300.",
                    "    Pendaftarannya butuh kartu kredit dan nomor HP.",
                    "  - DigitalOcean: cloud sederhana untuk developer dan usaha kecil. VPS-nya",
                    "    disebut Droplet. Tutorial komunitasnya tentang Linux dan Nginx jadi",
                    "    rujukan gratis yang bagus. Dipakai 9,6 persen responden Stack Overflow",
                    "    2026.",
                    "  - Hetzner: penyedia VPS asal Jerman yang terkenal murah, dipakai 7,8",
                    "    persen responden survei yang sama. Layanan terkelolanya sedikit, cocok",
                    "    untuk belajar mengurus server sendiri.",
                    "  - Alibaba Cloud: terbesar di Tiongkok dan punya region Jakarta. Hati-hati",
                    "    istilah: ECS di Alibaba berarti VM (setara EC2), sedangkan ECS di AWS",
                    "    adalah layanan container.",
                    "  - IBM Cloud: fokus ke hybrid cloud dan Red Hat OpenShift. Porsinya di",
                    "    kalangan developer kecil (1,3 persen di survei 2026), jadi jarang jadi",
                    "    pilihan pertama.",
                    "  - Penyedia VPS lain seperti Vultr, Akamai (dulu Linode), Contabo, dan",
                    "    penyedia lokal Indonesia: menjual VPS dan layanan dasar, kadang dengan",
                    "    harga rupiah dan pusat data di dalam negeri. Nggak ada angka survei",
                    "    global untuk penyedia lokal.",
                ],
            },
            {
                "heading": "Paket gratis dan jebakan tagihan",
                "body": [
                    "Sejak 15 Juli 2025, akun AWS baru mendapat kredit US$100 dan bisa menambah",
                    "sampai US$100 lagi dengan menyelesaikan aktivitas tertentu. Akun di paket",
                    "Free ditutup otomatis setelah enam bulan atau saat kreditnya habis, mana",
                    "yang lebih dulu, kecuali kamu pindah ke paket berbayar. Lebih dari 30",
                    "layanan tetap gratis sampai batas pemakaian bulanan tertentu. Google Cloud",
                    "memberi kredit US$300 selama 90 hari, dan Azure US$200 untuk 30 hari.",
                    "",
                    "Jebakan: tagihan cloud datang dari barang yang lupa dimatikan. Load",
                    "balancer, NAT gateway, dan alamat IPv4 publik ditagih per jam walau nggak",
                    "ada pengunjung sama sekali. Materi EC2 dan VPC nanti menghitung contohnya.",
                    "",
                    "Jebakan: access key yang ikut ter-commit ke GitHub. Ada bot yang memindai",
                    "repositori publik untuk mencari kunci cloud, lalu memakainya untuk menambang",
                    "kripto atas tagihanmu. Pasang alarm anggaran di hari pertama membuat akun.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Startup di Indonesia umumnya memakai salah satu dari tiga penyedia besar",
                    "dengan region Jakarta, sementara proyek pribadi dan UMKM sering memakai VPS",
                    "murah. Halaman harga tiap penyedia punya kalkulator resmi, misalnya AWS",
                    "Pricing Calculator, yang bisa kamu pakai tanpa akun.",
                    "",
                    "Kasus kecil: kamu mau belajar AWS dengan akun pribadi tanpa takut tagihan",
                    "kejutan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar akun, lalu aktifkan MFA untuk pengguna root dan jangan pakai",
                    "     root untuk pekerjaan sehari-hari.",
                    "  2. Di Billing, buat budget US$5 per bulan dengan notifikasi email di 50,",
                    "     80, dan 100 persen.",
                    "  3. Pilih region Jakarta (ap-southeast-3) atau region yang ditunjuk materi",
                    "     latihan, dan pakai region yang sama terus supaya sumber daya nggak",
                    "     tercecer.",
                    "  4. Tiap selesai latihan, buka Tag Editor atau Resource Explorer dan",
                    "     pastikan nggak ada sumber daya yang masih menyala.",
                ],
            },
        ],
    },
    {
        "title": "22. AWS IAM: Siapa Boleh Melakukan Apa",
        "sections": [
            {
                "body": [
                    "Begitu akun AWS dipakai lebih dari satu orang atau satu aplikasi,",
                    "pertanyaannya jadi \"siapa boleh melakukan apa terhadap apa\". Developer boleh",
                    "membaca log, tapi nggak boleh menghapus database produksi. Aplikasi boleh",
                    "menulis ke satu bucket, tapi nggak boleh membuat server baru.",
                    "",
                    "IAM (Identity and Access Management) adalah layanan AWS yang menjawab",
                    "pertanyaan itu. Layanannya gratis, dan setiap panggilan ke AWS, baik dari",
                    "konsol web, perintah aws, maupun kode aplikasi, selalu diperiksa IAM dulu.",
                ],
            },
            {
                "heading": "Pengguna, grup, role, dan policy",
                "body": [
                    "  - Pengguna root: akun yang dibuat saat mendaftar, dengan akses penuh dan",
                    "    nggak bisa dibatasi. Aktifkan MFA dan simpan baik-baik, jangan dipakai",
                    "    sehari-hari.",
                    "  - Pengguna IAM (user): identitas permanen untuk orang atau program, bisa",
                    "    punya kata sandi dan access key. Untuk orang, AWS sekarang menganjurkan",
                    "    login lewat IAM Identity Center.",
                    "  - Grup: kumpulan pengguna yang berbagi izin, misalnya grup developer.",
                    "  - Role: identitas tanpa kata sandi yang dipakai sementara. Server EC2,",
                    "    fungsi Lambda, atau job GitHub Actions lewat OIDC \"memakai\" role dan",
                    "    mendapat kredensial yang kedaluwarsa sendiri.",
                    "  - Policy: dokumen JSON berisi aturan izin, ditempel ke pengguna, grup,",
                    "    atau role.",
                ],
            },
            {
                "heading": "Membaca sebuah policy",
                "body": [
                    "Policy terdiri dari satu atau beberapa pernyataan (Statement). Tiap",
                    "pernyataan punya Effect (Allow atau Deny), Action (operasi apa), dan",
                    "Resource (terhadap sumber daya mana). Sumber daya ditulis sebagai ARN",
                    "(Amazon Resource Name), alamat unik tiap sumber daya di AWS.",
                ],
                "code": """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BacaLaporan",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::laporan-tim",
        "arn:aws:s3:::laporan-tim/*"
      ]
    },
    {
      "Sid": "LindungiArsip",
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::laporan-tim/arsip/*"
    }
  ]
}""",
                "bahasa": "json",
            },
            {
                "body": [
                    "Version 2012-10-17 bukan tanggal policy-mu dibuat. Itu versi bahasa policy,",
                    "dan selalu ditulis begitu. Sid cuma label bebas. Tanda * adalah wildcard:",
                    "s3:* berarti semua operasi S3, dan laporan-tim/* berarti semua objek di",
                    "bucket laporan-tim.",
                    "",
                    "Perhatikan ListBucket butuh ARN bucket-nya sendiri, sedangkan GetObject",
                    "butuh ARN objek (dengan /*). Salah menulis salah satunya adalah penyebab",
                    "paling umum pesan AccessDenied yang membingungkan.",
                ],
            },
            {
                "heading": "Urutan keputusan: Deny menang",
                "body": [
                    "Saat ada permintaan, IAM mengumpulkan semua pernyataan yang cocok dari semua",
                    "policy yang berlaku, lalu memutuskan dengan urutan:",
                    "",
                    "  1. Ada Deny eksplisit yang cocok? Ditolak, titik.",
                    "  2. Kalau nggak ada, ada Allow yang cocok? Diizinkan.",
                    "  3. Kalau nggak ada keduanya? Ditolak juga. Ini disebut tolak bawaan",
                    "     (implicit deny).",
                    "",
                    "Program kecil di bawah meniru urutan itu, tanpa wildcard supaya logikanya",
                    "kelihatan:",
                ],
                "code": """kebijakan = [
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "laporan/okt.csv"},
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "laporan/gaji.csv"},
    {"Effect": "Deny", "Action": "s3:GetObject", "Resource": "laporan/gaji.csv"},
]


def putuskan(aksi, sumber):
    cocok = [p["Effect"] for p in kebijakan
             if p["Action"] == aksi and p["Resource"] == sumber]
    if "Deny" in cocok:
        return "ditolak (Deny eksplisit)"
    if "Allow" in cocok:
        return "diizinkan"
    return "ditolak (tolak bawaan)"


for aksi, sumber in [("s3:GetObject", "laporan/okt.csv"),
                     ("s3:GetObject", "laporan/gaji.csv"),
                     ("s3:DeleteObject", "laporan/okt.csv")]:
    print(f"{aksi} {sumber}: {putuskan(aksi, sumber)}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  s3:GetObject laporan/okt.csv: diizinkan",
                    "  s3:GetObject laporan/gaji.csv: ditolak (Deny eksplisit)",
                    "  s3:DeleteObject laporan/okt.csv: ditolak (tolak bawaan)",
                    "",
                    "Berkas gaji.csv punya Allow dan Deny sekaligus, dan Deny menang.",
                    "DeleteObject nggak disebut di mana pun, jadi ditolak tanpa perlu ditulis.",
                    "Akun AWS dengan organisasi juga punya lapisan lain, seperti SCP dan",
                    "permission boundary, tapi semuanya ikut aturan dasar yang sama: Deny di mana",
                    "pun menang.",
                ],
            },
            {
                "heading": "Least privilege dan jebakannya",
                "body": [
                    "Prinsip least privilege berarti memberi izin sekecil mungkin yang masih",
                    "cukup untuk pekerjaannya. Mulai dari nol, tambah satu per satu saat ada yang",
                    "ditolak. IAM Access Analyzer bisa membuatkan policy dari aktivitas yang",
                    "tercatat di CloudTrail, jadi kamu nggak perlu menebak.",
                    "",
                    "Jebakan: menempel AdministratorAccess ke aplikasi \"biar cepat jalan\". Kalau",
                    "aplikasinya dibobol, penyerang mendapat seluruh akun.",
                    "",
                    "Jebakan: access key permanen di laptop dan di server. Server EC2 dan Lambda",
                    "sebaiknya memakai role, yang kredensialnya diputar otomatis. Di CI pakai",
                    "OIDC seperti di bab CI/CD.",
                    "",
                    "Padanannya di penyedia lain: Google Cloud IAM, dan di Azure kombinasi",
                    "Microsoft Entra ID (dulu Azure AD) untuk identitas plus Azure RBAC untuk",
                    "izin.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di perusahaan, developer biasanya login lewat IAM Identity Center dengan",
                    "akun kantor, lalu memilih role per akun AWS, misalnya ReadOnly di produksi",
                    "dan PowerUser di akun pengembangan. Dokumen \"Security best practices in IAM\"",
                    "di dokumentasi AWS memuat daftar periksanya.",
                    "",
                    "Kasus kecil: aplikasi unggah foto di EC2 memakai access key milik pengguna",
                    "IAM yang punya AdministratorAccess. Kamu diminta memperbaikinya tanpa",
                    "mematikan aplikasi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat role untuk EC2 dengan policy yang cuma mengizinkan s3:PutObject",
                    "     dan s3:GetObject ke arn:aws:s3:::foto-pelanggan/*.",
                    "  2. Pasang role itu ke instance sebagai instance profile. SDK AWS akan",
                    "     memakainya otomatis tanpa perubahan kode.",
                    "  3. Hapus access key dari berkas konfigurasi aplikasi, restart aplikasi,",
                    "     dan uji unggah foto.",
                    "  4. Nonaktifkan lalu hapus access key lama, dan cabut AdministratorAccess",
                    "     dari pengguna itu.",
                ],
            },
        ],
    },
    {
        "title": "23. EC2 dan VPC: Server dan Jaringan di AWS",
        "sections": [
            {
                "body": [
                    "EC2 (Elastic Compute Cloud) adalah layanan untuk menyewa mesin virtual, yang",
                    "di AWS disebut instance. Kamu memilih ukuran, sistem operasi, dan lokasi,",
                    "lalu dalam satu-dua menit instance-nya menyala dan bisa kamu masuki lewat",
                    "SSH, persis seperti server Linux di bab 01. Tagihannya dihitung per detik",
                    "untuk Linux.",
                    "",
                    "Instance selalu tinggal di dalam VPC (Virtual Private Cloud), jaringan",
                    "privat milikmu di dalam AWS. Kalau EC2 itu rumahnya, VPC itu kompleks",
                    "perumahannya: kamu yang menentukan jalan, gerbang, dan siapa boleh masuk.",
                ],
            },
            {
                "heading": "Konsep EC2 yang perlu kamu tahu",
                "body": [
                    "  - Tipe instance: kombinasi CPU dan memori. Namanya berpola, misalnya",
                    "    t4g.micro: keluarga t (bisa \"meledak\" sebentar di atas jatah CPU-nya),",
                    "    generasi 4, g untuk prosesor Graviton (ARM), ukuran micro.",
                    "  - AMI (Amazon Machine Image): citra disk awal, misalnya Amazon Linux 2023,",
                    "    Ubuntu, atau image buatanmu sendiri.",
                    "  - EBS (Elastic Block Store): disk jaringan yang ditempel ke instance.",
                    "    Datanya tetap ada walau instance dihentikan.",
                    "  - Key pair: pasangan kunci SSH. AWS menyimpan kunci publiknya, kamu",
                    "    menyimpan kunci privat.",
                    "  - Security group: firewall per instance yang stateful, artinya balasan",
                    "    untuk koneksi yang diizinkan otomatis boleh lewat. Kamu cuma menulis",
                    "    aturan masuk, misalnya port 443 dari mana saja dan port 22 dari IP",
                    "    kantor saja.",
                    "  - Cara bayar: On-Demand dibayar per detik tanpa komitmen. Spot memakai",
                    "    sisa kapasitas AWS dengan potongan besar, tapi bisa diambil kembali",
                    "    dengan peringatan dua menit. Savings Plans memberi diskon dengan",
                    "    komitmen satu atau tiga tahun.",
                ],
            },
            {
                "heading": "CIDR: menulis rentang alamat",
                "body": [
                    "Saat membuat VPC, kamu memilih blok alamat IP dalam notasi CIDR, misalnya",
                    "10.0.0.0/16. Angka di belakang garis miring adalah jumlah bit awal yang",
                    "dikunci sebagai alamat jaringan. Alamat IPv4 punya 32 bit, jadi /16",
                    "menyisakan 16 bit untuk host, atau 65.536 alamat. /24 menyisakan 8 bit,",
                    "alias 256 alamat. Ukuran VPC di AWS boleh antara /16 dan /28.",
                    "",
                    "VPC lalu dipecah jadi subnet, potongan yang lebih kecil. Modul ipaddress",
                    "bawaan Python bisa menghitungnya:",
                ],
                "code": """import ipaddress

vpc = ipaddress.ip_network("10.0.0.0/16")
print("alamat di VPC:", vpc.num_addresses)

semua_24 = list(vpc.subnets(new_prefix=24))
print("jumlah subnet /24:", len(semua_24))
for s in semua_24[:3]:
    print(" ", s, "berisi", s.num_addresses, "alamat,",
          s.num_addresses - 5, "bisa dipakai")

publik = semua_24[0]
alamat = list(publik)
print("dicadangkan AWS:", [str(a) for a in alamat[:4]], str(alamat[-1]))
print("10.0.0.77 di subnet publik?",
      ipaddress.ip_address("10.0.0.77") in publik)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  alamat di VPC: 65536",
                    "  jumlah subnet /24: 256",
                    "    10.0.0.0/24 berisi 256 alamat, 251 bisa dipakai",
                    "    10.0.1.0/24 berisi 256 alamat, 251 bisa dipakai",
                    "    10.0.2.0/24 berisi 256 alamat, 251 bisa dipakai",
                    "  dicadangkan AWS: ['10.0.0.0', '10.0.0.1', '10.0.0.2', '10.0.0.3'] 10.0.0.255",
                    "  10.0.0.77 di subnet publik? True",
                    "",
                    "Kenapa 251, bukan 256? AWS mencadangkan lima alamat di setiap subnet: empat",
                    "pertama (alamat jaringan, router VPC, DNS, dan satu cadangan) dan satu",
                    "terakhir. Subnet /28 yang cuma berisi 16 alamat jadi tinggal 11 yang bisa",
                    "dipakai.",
                ],
            },
            {
                "heading": "Subnet publik dan privat",
                "body": [
                    "Subnet sendiri nggak punya sifat publik atau privat. Sifat itu datang dari",
                    "route table, tabel yang menentukan ke mana paket dikirim:",
                    "",
                    "  - Subnet publik: route table-nya punya rute 0.0.0.0/0 ke internet gateway.",
                    "    Instance dengan IP publik di sini bisa dihubungi dari internet.",
                    "    Tempatnya load balancer dan bastion.",
                    "  - Subnet privat: nggak ada rute ke internet gateway. Database dan server",
                    "    aplikasi ditaruh di sini, jadi nggak bisa dihubungi langsung dari luar.",
                    "  - NAT gateway: dipasang di subnet publik supaya instance di subnet privat",
                    "    bisa keluar ke internet, misalnya untuk mengunduh paket, tanpa bisa",
                    "    dihubungi dari luar.",
                    "",
                    "Selain security group ada network ACL, firewall per subnet yang stateless:",
                    "aturan masuk dan keluar ditulis terpisah. Sebagian besar tim cukup memakai",
                    "security group.",
                ],
            },
            {
                "heading": "Berapa biaya barang yang lupa dimatikan",
                "body": [
                    "NAT gateway dan alamat IPv4 publik ditagih per jam selama ada, dipakai atau",
                    "nggak. Sejak Februari 2024 AWS menagih setiap alamat IPv4 publik. Dengan",
                    "harga region US East (N. Virginia) saat materi ini ditulis, hitungannya",
                    "begini:",
                ],
                "code": """JAM_SEBULAN = 730          # rata-rata jam dalam sebulan, angka AWS

nat_per_jam = 0.045        # NAT gateway, US East (N. Virginia)
nat_per_gb = 0.045         # data yang diproses NAT gateway
ipv4_per_jam = 0.005       # tiap alamat IPv4 publik

nat = nat_per_jam * JAM_SEBULAN + nat_per_gb * 50
ipv4 = ipv4_per_jam * JAM_SEBULAN * 3

print(f"NAT gateway + 50 GB : US$ {nat:6.2f}")
print(f"3 IPv4 publik       : US$ {ipv4:6.2f}")
print(f"total sebulan       : US$ {nat + ipv4:6.2f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  NAT gateway + 50 GB : US$  35.10",
                    "  3 IPv4 publik       : US$  10.95",
                    "  total sebulan       : US$  46.05",
                    "",
                    "Harga di region lain, termasuk Jakarta, sedikit berbeda, jadi cek halaman",
                    "harga resminya. Untuk lingkungan belajar, matikan NAT gateway sesudah",
                    "latihan atau pakai VPC endpoint untuk akses ke S3.",
                    "",
                    "Padanan EC2 di penyedia lain: Google Compute Engine, Azure Virtual Machines,",
                    "Alibaba ECS, dan DigitalOcean Droplet. Padanan VPC: Google VPC dan Azure",
                    "Virtual Network.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Arsitektur web yang umum di AWS memakai satu VPC per lingkungan (dev,",
                    "staging, produksi), dua AZ, subnet publik untuk load balancer, dan subnet",
                    "privat untuk server aplikasi serta database. Modul Terraform resmi komunitas",
                    "untuk VPC, yang dibahas di bab 08, membuat susunan ini dengan beberapa baris",
                    "saja.",
                    "",
                    "Kasus kecil: kamu diminta menyiapkan jaringan untuk aplikasi baru dengan VPC",
                    "10.20.0.0/16 di dua AZ, server aplikasi nggak boleh punya IP publik, dan",
                    "tagihan jaringan harus kecil.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat dua subnet publik /24 (10.20.0.0/24 dan 10.20.1.0/24) dan dua",
                    "     subnet privat /20, satu pasang per AZ.",
                    "  2. Pasang internet gateway dan rute 0.0.0.0/0 ke sana hanya di route table",
                    "     subnet publik.",
                    "  3. Taruh load balancer di subnet publik, instance aplikasi di subnet",
                    "     privat dengan security group yang cuma menerima port aplikasi dari",
                    "     security group load balancer.",
                    "  4. Untuk lingkungan dev, pakai satu NAT gateway saja dan matikan di luar",
                    "     jam kerja, atau ganti dengan VPC endpoint kalau yang dibutuhkan cuma",
                    "     akses ke S3.",
                ],
            },
        ],
    },
    {
        "title": "24. S3 dan CloudFront: Berkas dan CDN di AWS",
        "sections": [
            {
                "body": [
                    "Aplikasi hampir selalu menyimpan berkas: foto profil, PDF invoice, cadangan",
                    "database, berkas situs statis. Menaruhnya di disk server punya masalah:",
                    "disknya bisa penuh, dan kalau ada dua server, berkas di server satu nggak",
                    "kelihatan di server lain.",
                    "",
                    "Amazon S3 (Simple Storage Service) adalah object storage: penyimpanan berkas",
                    "yang diakses lewat HTTP, kapasitasnya nggak perlu kamu atur, dan dipakai",
                    "bersama oleh semua server. API S3 sudah jadi standar tidak resmi. Google",
                    "Cloud Storage, Azure Blob Storage, Cloudflare R2, DigitalOcean Spaces, dan",
                    "MinIO semuanya menyediakan API yang mirip atau kompatibel.",
                ],
            },
            {
                "heading": "Bucket, objek, dan kunci",
                "body": [
                    "  - Bucket: wadah berkas dengan nama unik di seluruh dunia, misalnya",
                    "    foto-toko-ani-2026. Bucket dibuat di satu region.",
                    "  - Objek: satu berkas beserta metadatanya, ukurannya sampai 5 TB.",
                    "  - Kunci (key): nama lengkap objek, misalnya produk/2026/sepatu.jpg. S3",
                    "    nggak punya folder. Garis miring di kunci cuma ditampilkan seperti",
                    "    folder oleh konsol.",
                ],
                "code": """aws s3 mb s3://foto-toko-ani-2026 --region ap-southeast-3
aws s3 cp sepatu.jpg s3://foto-toko-ani-2026/produk/2026/sepatu.jpg
aws s3 ls s3://foto-toko-ani-2026/produk/ --recursive
aws s3 sync ./situs s3://situs-toko-ani --delete""",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "sync menyamakan isi folder lokal dengan bucket. Opsi --delete ikut menghapus",
                    "objek di bucket yang sudah nggak ada di folder lokal, jadi periksa dulu",
                    "folder sumbernya sebelum menjalankannya.",
                    "",
                    "S3 punya beberapa kelas penyimpanan. Standard untuk berkas yang sering",
                    "dibaca, Standard-IA untuk yang jarang dibaca tapi harus cepat saat",
                    "dibutuhkan, dan keluarga Glacier untuk arsip yang murah disimpan tapi lambat",
                    "atau mahal diambil. Lifecycle rule bisa memindahkan objek tua ke kelas yang",
                    "lebih murah secara otomatis.",
                ],
            },
            {
                "heading": "Bucket yang bocor",
                "body": [
                    "Kasus kebocoran data karena bucket S3 terbuka untuk umum sudah terjadi",
                    "berkali-kali, dari data pelanggan sampai cadangan database. Penyebabnya",
                    "hampir selalu setelan, bukan celah di S3.",
                    "",
                    "Sejak April 2023, bucket baru otomatis memakai Block Public Access dan ACL",
                    "dimatikan. Artinya bucket baru tertutup kecuali kamu sengaja membukanya.",
                    "Sejak Januari 2023 objek baru juga dienkripsi otomatis di sisi server.",
                    "Aturannya untukmu sederhana: biarkan Block Public Access menyala, dan",
                    "sajikan berkas publik lewat CloudFront.",
                    "",
                    "Untuk berkas privat yang harus bisa diunduh pengguna tertentu, misalnya",
                    "invoice, pakai presigned URL: tautan sementara yang ditandatangani",
                    "aplikasimu dan kedaluwarsa sendiri setelah beberapa menit.",
                ],
            },
            {
                "heading": "CloudFront: CDN di depan S3",
                "body": [
                    "CDN (Content Delivery Network) adalah jaringan server cache di banyak kota.",
                    "Pengguna di Makassar mengambil berkas dari lokasi tepi (edge) terdekat,",
                    "bukan dari region tempat bucket berada. Kalau edge belum punya salinannya,",
                    "edge mengambil dari asalnya (origin), menyimpannya selama waktu tertentu",
                    "(TTL), lalu melayani permintaan berikutnya dari cache.",
                    "",
                    "Amazon CloudFront adalah CDN milik AWS. Pemain CDN lain: Cloudflare, Akamai,",
                    "Fastly, dan Google Cloud CDN. Pola yang dianjurkan untuk situs statis adalah",
                    "bucket privat plus distribusi CloudFront dengan origin access control, jadi",
                    "cuma CloudFront yang boleh membaca bucket-nya. Policy bucket-nya kira- kira",
                    "begini:",
                ],
                "code": """{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "cloudfront.amazonaws.com"},
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::situs-toko-ani/*",
    "Condition": {
      "StringEquals": {
        "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E2CONTOH"
      }
    }
  }]
}""",
                "bahasa": "json",
            },
            {
                "heading": "Kenapa nama berkas diberi versi",
                "body": [
                    "Menghapus cache di semua edge (invalidation) itu lambat dan dibatasi",
                    "jumlahnya. Cara yang dipakai hampir semua build tool frontend adalah memberi",
                    "sidik isi di nama berkas, misalnya app.3f9a.css. Isi berubah, nama berubah,",
                    "dan cache lama nggak pernah dipakai lagi. Program ini meniru satu lokasi",
                    "edge:",
                ],
                "code": """TTL = 3600   # detik, sama dengan Cache-Control: max-age=3600

cache = {}           # isi satu lokasi edge: nama -> detik disimpan
ke_origin = 0


def minta(nama, detik):
    global ke_origin
    if nama in cache and detik - cache[nama] < TTL:
        return "HIT "
    cache[nama] = detik
    ke_origin += 1
    return "MISS"


permintaan = [
    (0, "app.css"), (5, "app.css"), (1800, "app.css"),
    (3700, "app.css"),
    (3710, "app.3f9a.css"), (3720, "app.3f9a.css"),
]
for detik, nama in permintaan:
    print(f"detik {detik:>4}  {minta(nama, detik)}  {nama}")
print("permintaan ke S3:", ke_origin, "dari", len(permintaan))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  detik    0  MISS  app.css",
                    "  detik    5  HIT   app.css",
                    "  detik 1800  HIT   app.css",
                    "  detik 3700  MISS  app.css",
                    "  detik 3710  MISS  app.3f9a.css",
                    "  detik 3720  HIT   app.3f9a.css",
                    "  permintaan ke S3: 3 dari 6",
                    "",
                    "Selama TTL satu jam, app.css dilayani dari cache walau kamu sudah mengunggah",
                    "versi baru ke S3. Pengguna baru melihat versi baru di detik 3700. Berkas",
                    "bernama app.3f9a.css langsung terambil karena namanya belum pernah ada di",
                    "cache.",
                    "",
                    "Jebakan: biaya egress, yaitu biaya data keluar dari cloud ke internet. S3",
                    "dan EC2 menagihnya per GB. Lalu lintas lewat CloudFront biasanya lebih murah",
                    "daripada langsung dari S3, dan R2 milik Cloudflare menonjolkan nol biaya",
                    "egress sebagai daya jualnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak situs dokumentasi, landing page, dan aplikasi React yang sudah",
                    "di-build disajikan dari S3 lewat CloudFront, atau dari layanan serupa di",
                    "penyedia lain. Halaman \"Hosting a static website\" di dokumentasi S3 dan",
                    "CloudFront memuat langkah resminya.",
                    "",
                    "Kasus kecil: kamu mengunggah situs portofolio ke bucket S3 dan mengaktifkan",
                    "akses publik supaya bisa dibuka. Temanmu mengingatkan bahwa itu bukan pola",
                    "yang dianjurkan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Nyalakan lagi Block Public Access di bucket itu.",
                    "  2. Buat distribusi CloudFront dengan bucket sebagai origin dan pilih",
                    "     origin access control.",
                    "  3. Tempel bucket policy yang hanya mengizinkan cloudfront.amazonaws.com",
                    "     dengan SourceArn distribusimu.",
                    "  4. Atur build supaya nama berkas CSS dan JS memuat hash isi, lalu set",
                    "     Cache-Control panjang untuk berkas itu dan pendek untuk index.html.",
                ],
            },
        ],
    },
    {
        "title": "25. RDS, DynamoDB, ELB, Route 53, dan CloudWatch",
        "sections": [
            {
                "body": [
                    "Sejauh ini kamu sudah punya server (EC2), jaringan (VPC), dan tempat berkas",
                    "(S3). Aplikasi web sungguhan butuh beberapa potong lagi: database, pembagi",
                    "beban di depan beberapa server, nama domain, dan cara tahu kalau ada yang",
                    "rusak. Materi ini menyusun semuanya jadi arsitektur tiga lapis yang umum",
                    "dipakai.",
                ],
            },
            {
                "heading": "RDS dan Aurora: database relasional terkelola",
                "body": [
                    "Memasang PostgreSQL sendiri di EC2 bisa saja, tapi kamu jadi harus mengurus",
                    "backup, patch, replika, dan pemulihan saat disk rusak. Amazon RDS",
                    "(Relational Database Service) mengurus semua itu. Mesin yang didukung antara",
                    "lain PostgreSQL, MySQL, MariaDB, SQL Server, dan Oracle.",
                    "",
                    "Amazon Aurora adalah database buatan AWS yang kompatibel dengan MySQL dan",
                    "PostgreSQL, dengan penyimpanan yang direplikasi otomatis ke beberapa AZ.",
                    "Fitur Multi-AZ di RDS menyiapkan salinan siaga di AZ lain yang otomatis",
                    "mengambil alih kalau yang utama mati.",
                    "",
                    "Jebakan: database di subnet publik dengan port 5432 terbuka. Taruh RDS di",
                    "subnet privat, dan izinkan koneksi hanya dari security group server",
                    "aplikasi. Padanannya: Cloud SQL dan AlloyDB di Google Cloud, Azure Database",
                    "for PostgreSQL atau MySQL dan Azure SQL Database di Azure.",
                ],
            },
            {
                "heading": "DynamoDB: NoSQL tanpa server",
                "body": [
                    "Amazon DynamoDB adalah database key-value dan dokumen yang skalanya diatur",
                    "otomatis. Kamu nggak memilih ukuran server sama sekali. Tiap item diambil",
                    "lewat partition key, dan boleh ditambah sort key untuk mengurutkan item yang",
                    "berbagi partition key. Satu item paling besar 400 KB.",
                    "",
                    "Cara berpikirnya kebalikan dari SQL. Di SQL kamu merancang tabel dulu, lalu",
                    "menulis kueri apa pun yang dibutuhkan. Di DynamoDB kamu mendaftar pola akses",
                    "dulu (\"ambil semua pesanan satu pelanggan, urut tanggal\"), lalu merancang",
                    "kunci supaya pola itu jadi satu Query. Program ini meniru caranya:",
                ],
                "code": """tabel = {
    ("PELANGGAN#ani", "PROFIL"): {"kota": "Bandung"},
    ("PELANGGAN#ani", "PESANAN#2026-10-02"): {"total": 85000},
    ("PELANGGAN#ani", "PESANAN#2026-10-15"): {"total": 120000},
    ("PELANGGAN#budi", "PROFIL"): {"kota": "Medan"},
    ("PELANGGAN#budi", "PESANAN#2026-09-30"): {"total": 40000},
}


def query(pk, awalan_sk):
    # Mirip Query DynamoDB: satu partition key, sort key berawalan tertentu
    hasil = [(sk, isi) for (p, sk), isi in tabel.items()
             if p == pk and sk.startswith(awalan_sk)]
    return sorted(hasil)


for sk, isi in query("PELANGGAN#ani", "PESANAN#"):
    print(sk, isi)
print("profil budi:", query("PELANGGAN#budi", "PROFIL"))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  PESANAN#2026-10-02 {'total': 85000}",
                    "  PESANAN#2026-10-15 {'total': 120000}",
                    "  profil budi: [('PROFIL', {'kota': 'Medan'})]",
                    "",
                    "Profil dan pesanan satu pelanggan tinggal di partition yang sama, dibedakan",
                    "awalan sort key. Mencari \"semua pesanan di atas 100.000 dari semua",
                    "pelanggan\" justru mahal, karena pola itu nggak dirancang dari awal. Pilih",
                    "RDS kalau kuerimu beragam dan sering berubah, pilih DynamoDB kalau pola",
                    "aksesnya jelas dan butuh skala besar tanpa mengurus server. Padanannya:",
                    "Firestore atau Bigtable, dan Azure Cosmos DB.",
                ],
            },
            {
                "heading": "ELB dan Route 53: pintu depan",
                "body": [
                    "Elastic Load Balancing membagi permintaan ke beberapa instance dan berhenti",
                    "mengirim ke instance yang gagal health check, sama seperti upstream Nginx di",
                    "bab 02, tapi dikelola AWS:",
                    "",
                    "  - ALB (Application Load Balancer): bekerja di lapisan HTTP (L7). Bisa",
                    "    memilih tujuan menurut path atau host, dan memasang sertifikat HTTPS",
                    "    gratis dari AWS Certificate Manager.",
                    "  - NLB (Network Load Balancer): bekerja di lapisan TCP dan UDP (L4), cepat,",
                    "    dan cocok untuk protokol selain HTTP.",
                    "",
                    "Amazon Route 53 adalah layanan DNS terkelola sekaligus tempat membeli",
                    "domain. Record alias bisa mengarahkan domain utama (tokoani.id, tanpa www)",
                    "langsung ke ALB atau CloudFront. Record yang cuma menunjuk nama lain nggak",
                    "boleh dipasang di domain utama. Route 53 juga punya kebijakan routing",
                    "seperti weighted (bagi persen), latency (region tercepat), dan failover",
                    "(pindah ke cadangan kalau health check gagal).",
                    "",
                    "Jebakan: load balancer ditagih per jam walau tanpa lalu lintas. ALB sisa",
                    "latihan yang lupa dihapus akan muncul di tagihan tiap bulan.",
                ],
            },
            {
                "heading": "CloudWatch: tahu kalau ada yang rusak",
                "body": [
                    "Amazon CloudWatch mengumpulkan metrik (CPU, jumlah permintaan, latensi),",
                    "log, dan alarm. Alarm memantau satu metrik dan mengirim notifikasi lewat",
                    "SNS, misalnya email, kalau melewati ambang.",
                ],
                "code": "aws cloudwatch put-metric-alarm \\\n  --alarm-name alb-5xx-tinggi \\\n  --namespace AWS/ApplicationELB \\\n  --metric-name HTTPCode_Target_5XX_Count \\\n  --dimensions Name=LoadBalancer,Value=app/toko-ani/50dc6c495c0c9188 \\\n  --statistic Sum --period 300 --evaluation-periods 2 \\\n  --threshold 20 --comparison-operator GreaterThanThreshold \\\n  --alarm-actions arn:aws:sns:ap-southeast-3:123456789012:tim-ops",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "Alarm itu menyala kalau ada lebih dari 20 galat 5xx dalam lima menit, dua",
                    "periode berturut-turut. Dua periode dipakai supaya lonjakan sesaat nggak",
                    "membangunkan orang. Bab Observability nanti membahas cara memilih ambang",
                    "dengan lebih rapi.",
                    "",
                    "Jebakan: grup log CloudWatch bawaannya disimpan selamanya. Log yang terus",
                    "bertambah bertahun-tahun bisa membengkakkan tagihan. Atur retensi, misalnya",
                    "30 hari untuk log aplikasi biasa.",
                    "",
                    "Padanannya di Google Cloud adalah Google Cloud Observability (Cloud Logging",
                    "dan Cloud Monitoring). Nama lamanya Stackdriver, yang masih muncul di",
                    "dokumen dan roadmap lama. Di Azure namanya Azure Monitor.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Arsitektur tiga lapis seperti ini sering dipakai sebagai contoh di materi",
                    "resmi AWS, termasuk AWS Well-Architected Framework. DNS di Route 53, ALB di",
                    "subnet publik, EC2 atau container di subnet privat, dan RDS Multi-AZ di",
                    "belakangnya.",
                    "",
                    "Kasus kecil: toko online temanmu masih satu VPS berisi aplikasi dan MySQL",
                    "sekaligus. Tiap ada promo, situsnya mati dan nggak ada yang tahu sampai",
                    "pelanggan protes di media sosial.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan database ke RDS MySQL Multi-AZ di subnet privat, dengan",
                    "     backup otomatis tujuh hari.",
                    "  2. Jalankan dua instance aplikasi di dua AZ di belakang satu ALB dengan",
                    "     health check ke /sehat.",
                    "  3. Arahkan domain ke ALB lewat record alias di Route 53, dan pasang",
                    "     sertifikat dari Certificate Manager di ALB.",
                    "  4. Buat alarm CloudWatch untuk galat 5xx dan instance yang nggak sehat,",
                    "     kirim ke email tim lewat SNS.",
                ],
            },
        ],
    },
    {
        "title": "26. AWS Lambda: Menjalankan Fungsi Tanpa Server",
        "sections": [
            {
                "body": [
                    "Di bab sebelumnya kamu menyewa server EC2 yang menyala 24 jam. Untuk",
                    "pekerjaan yang datang sesekali, misalnya membuat thumbnail tiap ada foto",
                    "diunggah, server itu lebih sering nganggur daripada bekerja, tapi tetap",
                    "ditagih tiap jam.",
                    "",
                    "AWS Lambda menawarkan cara lain. Kamu cuma menulis satu fungsi, lalu memberi",
                    "tahu AWS kejadian apa yang memicunya. AWS yang menyiapkan tempat",
                    "menjalankannya, memanggil fungsimu, dan membuang tempat itu kalau sudah lama",
                    "nggak dipakai. Tagihannya dihitung per permintaan dan per milidetik fungsi",
                    "berjalan, dikali besar memori yang kamu pilih.",
                    "",
                    "Model ini disebut serverless atau FaaS (Function as a Service). Servernya",
                    "tetap ada, tapi kamu nggak memasang sistem operasi, nggak menambal keamanan,",
                    "dan nggak memikirkan berapa mesin yang harus nyala. Lambda dirilis 2014 dan",
                    "sampai sekarang jadi layanan FaaS terbesar.",
                ],
            },
            {
                "heading": "Handler, event, dan context",
                "body": [
                    "Fungsi yang dipanggil Lambda disebut handler. Ia menerima dua argumen. event",
                    "berisi data kejadian dalam bentuk dict, misalnya informasi berkas yang baru",
                    "diunggah ke S3. context berisi informasi tentang pemanggilan itu, misalnya",
                    "sisa waktu sebelum fungsi dihentikan paksa.",
                    "",
                    "Contoh di bawah adalah handler yang dipicu S3. Bagian bawahnya membuat event",
                    "dan context tiruan supaya bisa kamu jalankan tanpa akun AWS:",
                ],
                "code": """import json
import urllib.parse

UKURAN_MAKS = 5 * 1024 * 1024        # 5 MB


def lambda_handler(event, context):
    hasil = []
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        kunci = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
        ukuran = record["s3"]["object"]["size"]
        status = "tolak: terlalu besar" if ukuran > UKURAN_MAKS else "buat thumbnail"
        hasil.append(f"{bucket}/{kunci}: {status}")
    sisa = context.get_remaining_time_in_millis()
    return {"diproses": hasil, "sisa_ms": sisa}


class ContextTiruan:
    # Di AWS, objek context disediakan Lambda. Di sini kita tiru satu metodenya.
    def get_remaining_time_in_millis(self):
        return 2950


event_tiruan = {"Records": [
    {"s3": {"bucket": {"name": "foto-toko"},
            "object": {"key": "produk/sepatu+merah.jpg", "size": 204800}}},
    {"s3": {"bucket": {"name": "foto-toko"},
            "object": {"key": "produk/video.mp4", "size": 73400320}}},
]}
print(json.dumps(lambda_handler(event_tiruan, ContextTiruan()), indent=2))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  {",
                    "    \"diproses\": [",
                    "      \"foto-toko/produk/sepatu merah.jpg: buat thumbnail\",",
                    "      \"foto-toko/produk/video.mp4: tolak: terlalu besar\"",
                    "    ],",
                    "    \"sisa_ms\": 2950",
                    "  }",
                    "",
                    "Nama berkas di event S3 di-encode seperti di URL, jadi spasi berubah jadi",
                    "tanda plus. unquote_plus mengembalikannya. Satu event S3 bisa berisi lebih",
                    "dari satu record, makanya handler selalu memutar daftar Records.",
                ],
            },
            {
                "heading": "Cold start dan warm start",
                "body": [
                    "Saat fungsimu dipanggil pertama kali, Lambda harus menyiapkan lingkungan",
                    "eksekusi: mesin kecil terisolasi, runtime Python, lalu kode di luar handler",
                    "seperti import dan pembukaan koneksi database. Penundaan di panggilan",
                    "pertama ini disebut cold start.",
                    "",
                    "Sesudahnya lingkungan itu dibiarkan hidup sebentar. Panggilan berikutnya",
                    "memakai ulang lingkungan yang sama tanpa persiapan: warm start. Variabel",
                    "global dan koneksi yang dibuka di luar handler masih ada. Kalau lama nggak",
                    "dipanggil, lingkungannya dibuang, dan AWS nggak menjanjikan berapa lama",
                    "persisnya.",
                    "",
                    "  - Taruh pekerjaan mahal yang bisa dipakai ulang, seperti membuat klien",
                    "    database, di luar handler.",
                    "  - Jangan simpan data pengguna di variabel global. Panggilan berikutnya",
                    "    bisa dari pengguna lain yang kebetulan mendarat di lingkungan yang sama.",
                    "  - Untuk Java, Python, dan .NET ada SnapStart, yang menyimpan potret",
                    "    lingkungan yang sudah siap supaya cold start lebih singkat. Provisioned",
                    "    concurrency menjaga sejumlah lingkungan tetap hangat, dengan biaya",
                    "    tambahan.",
                ],
            },
            {
                "heading": "Batas yang perlu kamu tahu",
                "body": [
                    "Angka di bawah dari halaman kuota resmi Lambda saat materi ini ditulis",
                    "(Oktober 2026):",
                    "",
                    "  - Waktu jalan paling lama 15 menit per pemanggilan. Pekerjaan yang lebih",
                    "    lama harus dipecah atau dipindah ke container.",
                    "  - Memori 128 MB sampai 10.240 MB. CPU ikut naik sebanding memori; di 1.769",
                    "    MB fungsimu setara satu vCPU.",
                    "  - Ukuran data masuk dan keluar untuk panggilan sinkron 6 MB masing-masing,",
                    "    untuk panggilan asinkron 1 MB.",
                    "  - Paket .zip paling besar 50 MB terkompresi atau 250 MB setelah dibuka,",
                    "    termasuk layer. Image container boleh sampai 10 GB.",
                    "  - Folder /tmp bisa diatur antara 512 MB dan 10.240 MB, dan isinya hilang",
                    "    saat lingkungan dibuang.",
                    "  - Konkurensi bawaan 1.000 per region, dan akun baru bisa mulai dengan",
                    "    kuota lebih kecil yang dinaikkan AWS otomatis.",
                    "",
                    "Paket gratis Lambda termasuk yang always free: satu juta permintaan dan",
                    "400.000 GB-detik per bulan.",
                ],
            },
            {
                "heading": "Runtime yang didukung",
                "body": [
                    "Runtime adalah bahasa beserta versinya. Yang terbaru saat materi ini",
                    "ditulis: python3.14, nodejs24.x, java25, dotnet10, dan ruby4.0. Node.js 26",
                    "dan Python 3.15 masih pratinjau dengan target rilis November 2026. Go dan",
                    "Rust dijalankan lewat runtime khusus sistem operasi (provided.al2023).",
                    "",
                    "Jebakan: runtime punya tanggal pensiun. Amazon Linux 2 berakhir 30 Juni",
                    "2026, dan runtime yang dibangun di atasnya, seperti python3.10 dan",
                    "python3.11, sedang dipensiunkan bertahap. Fungsi lama tetap jalan, tapi",
                    "lama-lama nggak bisa diperbarui. Pasang pengingat untuk naik versi.",
                    "",
                    "Dokumentasi AWS sejak 2026 menyebut fungsi Lambda biasa sebagai Lambda Event",
                    "Functions, dan ada jenis baru bernama Lambda Web Functions untuk menjalankan",
                    "aplikasi web sebagai server HTTP. Kalau kamu membaca dua nama itu di",
                    "dokumentasi, yang dibahas di materi ini adalah Event Functions.",
                ],
            },
            {
                "heading": "Men-deploy dari terminal",
                "body": [
                    "Untuk mencoba sekali, AWS CLI cukup. Proyek sungguhan biasanya memakai AWS",
                    "SAM, Serverless Framework, Terraform, atau CDK. Perintah ini membuat dan",
                    "memanggil fungsi; role-nya harus sudah ada dengan izin menulis log ke",
                    "CloudWatch:",
                ],
                "code": "zip fungsi.zip app.py\naws lambda create-function --function-name thumbnail \\\n  --runtime python3.14 --handler app.lambda_handler \\\n  --role arn:aws:iam::123456789012:role/lambda-thumbnail \\\n  --zip-file fileb://fungsi.zip --timeout 30 --memory-size 512\naws lambda invoke --function-name thumbnail \\\n  --payload fileb://event.json hasil.json\naws logs tail /aws/lambda/thumbnail --follow",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "Semua print dan galat dari fungsi masuk ke CloudWatch Logs di grup",
                    "/aws/lambda/<nama-fungsi>. Perintah terakhir menampilkan log itu secara",
                    "langsung, berguna saat mencari tahu kenapa fungsi gagal.",
                    "",
                    "Lambda kurang pas untuk pekerjaan yang jalan terus berjam-jam. Untuk lalu",
                    "lintas yang tinggi dan stabil sepanjang hari, server biasa sering lebih",
                    "murah. Aplikasi yang butuh koneksi panjang dengan banyak status di memori",
                    "juga lebih cocok di server.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola paling umum Lambda adalah pekerjaan latar belakang yang dipicu",
                    "kejadian: membuat thumbnail saat foto masuk S3, mengirim email saat pesanan",
                    "dibuat, atau tugas terjadwal tiap malam. Serverless Land, situs milik AWS,",
                    "mengumpulkan contoh pola seperti ini lengkap dengan kodenya.",
                    "",
                    "Kasus kecil: toko online temanmu ingin setiap foto produk yang diunggah ke",
                    "bucket otomatis dikecilkan jadi thumbnail 300 piksel, tanpa menyewa server",
                    "tambahan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis handler seperti contoh di atas, dengan Pillow untuk mengecilkan",
                    "     gambar, dan uji dulu dengan event tiruan di laptop.",
                    "  2. Buat role berizin s3:GetObject di bucket asal, s3:PutObject di bucket",
                    "     thumbnail, dan izin menulis log.",
                    "  3. Deploy fungsinya, lalu pasang notifikasi event S3 untuk",
                    "     s3:ObjectCreated:* dengan filter awalan produk/.",
                    "  4. Tulis hasil ke bucket lain, bukan bucket yang sama, supaya thumbnail",
                    "     yang baru dibuat nggak memicu fungsi lagi tanpa henti.",
                ],
            },
        ],
    },
    {
        "title": "27. Lambda dengan API Gateway, SQS, dan EventBridge",
        "sections": [
            {
                "body": [
                    "Lambda jarang berdiri sendiri. Fungsi perlu dipicu sesuatu: ada permintaan",
                    "HTTP dari aplikasi, ada pesan di antrean, atau ada jadwal. Materi ini",
                    "membahas tiga layanan yang paling sering dipasangkan dengan Lambda dan pola",
                    "yang dibentuknya.",
                ],
            },
            {
                "heading": "API Gateway: pintu HTTP untuk fungsi",
                "body": [
                    "Amazon API Gateway menerima permintaan HTTP, memeriksa autentikasi dan batas",
                    "laju, lalu meneruskannya ke Lambda sebagai event. Fungsimu cuma",
                    "mengembalikan dict berisi statusCode dan body, tanpa membuka port.",
                    "",
                    "  - HTTP API: lebih sederhana dan lebih murah, cukup untuk sebagian besar",
                    "    API.",
                    "  - REST API: fitur lebih lengkap seperti API key dengan kuota per",
                    "    pelanggan, validasi permintaan, dan cache.",
                    "  - WebSocket API: koneksi dua arah, misalnya untuk obrolan.",
                    "",
                    "Dua batas yang sering bikin bingung. Pertama, API Gateway memutus permintaan",
                    "sinkron yang jalan kira-kira lebih dari 30 detik, walau Lambda-nya boleh",
                    "jalan 15 menit. Pekerjaan lama harus dipindah ke latar belakang. Kedua,",
                    "batas laju bawaan per akun adalah 10.000 permintaan per detik, tapi di",
                    "beberapa region baru, termasuk Jakarta, bawaannya 2.500.",
                    "",
                    "Padanannya: Google API Gateway dan Apigee, serta Azure API Management.",
                ],
            },
            {
                "heading": "SQS: antrean supaya pekerjaan nggak hilang",
                "body": [
                    "Bayangkan pengguna menekan tombol \"kirim invoice\", dan fungsi pembuat PDF",
                    "butuh 20 detik. Daripada membuat pengguna menunggu, API menaruh pesan di",
                    "antrean lalu langsung menjawab \"sedang diproses\". Fungsi lain mengambil",
                    "pesan itu di belakang layar.",
                    "",
                    "Amazon SQS (Simple Queue Service) adalah layanan antrean pesan. Cara",
                    "kerjanya punya satu konsep penting, visibility timeout:",
                    "",
                    "  - Saat konsumen menerima pesan, pesan itu nggak dihapus, cuma",
                    "    disembunyikan selama visibility timeout (bawaannya 30 detik, bisa sampai",
                    "    12 jam).",
                    "  - Kalau konsumen selesai, ia menghapus pesannya.",
                    "  - Kalau konsumen gagal atau mati di tengah jalan, pesan muncul lagi",
                    "    setelah timeout habis dan bisa diambil ulang.",
                    "  - Pesan disimpan bawaannya empat hari, paling lama 14 hari.",
                    "",
                    "Antrean Standard menjamin pesan sampai minimal sekali, jadi pesan yang sama",
                    "kadang bisa terkirim dua kali. Kode konsumenmu harus aman diproses ulang,",
                    "misalnya mengecek apakah invoice itu sudah pernah dibuat. Antrean FIFO",
                    "menjaga urutan dan mencegah duplikat, dengan throughput yang lebih terbatas.",
                ],
            },
            {
                "heading": "DLQ dan kegagalan sebagian",
                "body": [
                    "Pesan yang selalu gagal, misalnya karena datanya rusak, akan muncul lagi dan",
                    "lagi. DLQ (dead-letter queue) adalah antrean kedua untuk menampungnya. Di",
                    "antrean utama kamu memasang redrive policy dengan maxReceiveCount, misalnya",
                    "3: sesudah diterima tiga kali tanpa dihapus, pesan dipindah ke DLQ. Tim lalu",
                    "bisa memeriksa isinya dan memasang alarm kalau DLQ nggak kosong.",
                    "",
                    "Lambda mengambil pesan SQS dalam batch. Kalau satu pesan gagal dan fungsinya",
                    "melempar exception, seluruh batch dianggap gagal dan pesan yang sudah",
                    "berhasil ikut diulang. Dengan pengaturan ReportBatchItemFailures, fungsi",
                    "cukup melaporkan pesan mana yang gagal:",
                ],
                "code": """import json


def proses(pesanan):
    if pesanan["jumlah"] <= 0:
        raise ValueError("jumlah harus positif")
    print(f"  simpan pesanan {pesanan['id']} x{pesanan['jumlah']}")


def lambda_handler(event, context):
    gagal = []
    for record in event["Records"]:
        try:
            proses(json.loads(record["body"]))
        except (ValueError, KeyError) as e:
            print(f"  gagal {record['messageId']}: {e}")
            gagal.append({"itemIdentifier": record["messageId"]})
    return {"batchItemFailures": gagal}


batch = {"Records": [
    {"messageId": "m-1", "body": json.dumps({"id": "P01", "jumlah": 2})},
    {"messageId": "m-2", "body": json.dumps({"id": "P02", "jumlah": 0})},
    {"messageId": "m-3", "body": json.dumps({"id": "P03", "jumlah": 1})},
]}
print("hasil:", lambda_handler(batch, None))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "    simpan pesanan P01 x2",
                    "    gagal m-2: jumlah harus positif",
                    "    simpan pesanan P03 x1",
                    "  hasil: {'batchItemFailures': [{'itemIdentifier': 'm-2'}]}",
                    "",
                    "Cuma m-2 yang dikembalikan ke antrean. P01 dan P03 dianggap selesai dan",
                    "dihapus.",
                ],
            },
            {
                "heading": "SNS dan EventBridge: satu kejadian, banyak penerima",
                "body": [
                    "  - Amazon SNS (Simple Notification Service): pub/sub. Satu pesan yang",
                    "    diterbitkan ke sebuah topic dikirim ke semua pelanggannya sekaligus,",
                    "    misalnya beberapa antrean SQS, fungsi Lambda, atau email. Pola ini",
                    "    disebut fan-out.",
                    "  - Amazon EventBridge: bus event dengan aturan penyaringan. Layanan AWS,",
                    "    aplikasimu, dan aplikasi SaaS mengirim event ke bus, lalu aturan",
                    "    memutuskan event mana dikirim ke target mana. EventBridge Scheduler",
                    "    menjalankan target menurut jadwal, cocok untuk tugas seperti cron.",
                ],
                "code": """{
  "source": ["toko.pesanan"],
  "detail-type": ["PesananDibuat"],
  "detail": {
    "total": [{"numeric": [">=", 1000000]}]
  }
}""",
                "bahasa": "json",
            },
            {
                "body": [
                    "Pola event di atas cuma meneruskan event PesananDibuat dengan total minimal",
                    "satu juta, misalnya ke fungsi yang memberi tahu tim penjualan. Pengirim",
                    "event nggak perlu tahu siapa saja penerimanya, jadi menambah penerima baru",
                    "nggak perlu mengubah kode pengirim.",
                    "",
                    "Padanannya: Google Pub/Sub dan Cloud Tasks, serta Azure Service Bus dan",
                    "Event Grid.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Arsitektur API Gateway, Lambda, SQS, dan DynamoDB sering dipakai untuk",
                    "backend aplikasi kecil sampai menengah, misalnya pemrosesan pesanan atau",
                    "formulir pendaftaran acara yang ramai cuma beberapa hari. Dokumentasi Lambda",
                    "punya tutorial resmi untuk tiap pasangan itu.",
                    "",
                    "Kasus kecil: API pendaftaran lomba milik panitia 17-an sering timeout karena",
                    "fungsi Lambda-nya langsung membuat sertifikat PDF, dan kadang sertifikat",
                    "dobel terkirim.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ubah fungsi API jadi cuma memvalidasi data, menaruh pesan di SQS, lalu",
                    "     menjawab 202 Accepted.",
                    "  2. Buat fungsi kedua yang dipicu SQS untuk membuat PDF, dengan visibility",
                    "     timeout minimal enam kali timeout fungsinya, sesuai saran dokumentasi",
                    "     AWS.",
                    "  3. Pasang DLQ dengan maxReceiveCount 3 dan alarm CloudWatch kalau jumlah",
                    "     pesan di DLQ lebih dari nol.",
                    "  4. Simpan nomor pendaftaran yang sudah dibuatkan sertifikat di DynamoDB,",
                    "     dan lewati pesan yang nomornya sudah ada.",
                ],
            },
        ],
    },
    {
        "title": "28. Cloudflare Workers dan Platform Edge",
        "sections": [
            {
                "body": [
                    "Lambda berjalan di satu region yang kamu pilih. Pengguna di Jayapura yang",
                    "memanggil fungsi di Jakarta tetap harus menunggu data menyeberang pulau.",
                    "Edge computing memindahkan kodenya ke banyak pusat data sekaligus, sehingga",
                    "permintaan dijawab dari lokasi terdekat pengguna.",
                    "",
                    "Cloudflare adalah perusahaan jaringan yang awalnya terkenal karena DNS dan",
                    "CDN-nya, lalu menambah platform untuk developer. Di Survei Stack Overflow",
                    "2026, produk Cloudflare dipakai 24,6 persen responden, naik dari 20,1 persen",
                    "setahun sebelumnya.",
                ],
            },
            {
                "heading": "Layanan Cloudflare yang sering dipakai",
                "body": [
                    "  - DNS dan CDN: banyak orang mulai dari sini, karena paket gratisnya sudah",
                    "    memberi DNS cepat, cache, dan sertifikat HTTPS.",
                    "  - Perlindungan DDoS dan WAF (web application firewall): menyaring lalu",
                    "    lintas jahat sebelum sampai ke servermu.",
                    "  - Tunnel: program cloudflared di servermu membuka koneksi keluar ke",
                    "    Cloudflare, jadi aplikasi bisa diakses dari internet tanpa membuka port",
                    "    apa pun di firewall.",
                    "  - R2: object storage yang API-nya kompatibel dengan S3 dan nggak menagih",
                    "    biaya egress.",
                    "  - Pages: hosting situs statis dan frontend dari repositori Git.",
                    "  - Workers: menjalankan kodemu di jaringan edge Cloudflare. Ini yang",
                    "    dibahas di sisa materi.",
                ],
            },
            {
                "heading": "Cara kerja Workers",
                "body": [
                    "Lambda menyalakan lingkungan eksekusi berisi runtime lengkap. Workers",
                    "memakai V8 isolate, ruang terisolasi di dalam mesin JavaScript V8 yang juga",
                    "dipakai Chrome. Satu proses bisa menampung ribuan isolate, dan isolate baru",
                    "siap dalam hitungan milidetik. Akibatnya cold start hampir nggak terasa.",
                    "",
                    "Konsekuensinya, Workers bukan Node.js penuh. Kode Worker memakai API web",
                    "standar seperti fetch, Request, dan Response. Sebagian API Node.js tersedia",
                    "lewat flag kompatibilitas nodejs_compat, tapi nggak semuanya. Pustaka npm",
                    "yang memakai modul Node yang nggak didukung akan gagal saat build atau saat",
                    "jalan.",
                    "",
                    "Worker paling sederhana mengekspor objek dengan metode fetch, yang dipanggil",
                    "untuk setiap permintaan:",
                ],
                "code": """export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === "/halo") {
      const nama = url.searchParams.get("nama") ?? "dunia";
      return Response.json({ pesan: `Halo, ${nama}!` });
    }

    if (url.pathname.startsWith("/catatan/")) {
      const kunci = url.pathname.slice("/catatan/".length);
      const isi = await env.CATATAN.get(kunci);   // binding KV
      return isi === null
        ? new Response("nggak ada", { status: 404 })
        : new Response(isi);
    }
    ...
    return new Response("Not found", { status: 404 });
  },
};""",
                "bahasa": "javascript",
            },
            {
                "body": [
                    "Parameter env berisi binding, yaitu sambungan ke layanan lain yang kamu",
                    "daftarkan di konfigurasi. KV dipakai untuk simpanan key-value, D1 untuk",
                    "database SQLite, R2 untuk berkas, dan Queues untuk antrean. Durable Objects",
                    "menyimpan status yang butuh satu pemilik, misalnya ruang obrolan. Baris ...",
                    "menandai rute lain yang dipotong dari contoh ini.",
                ],
            },
            {
                "heading": "Wrangler dan konfigurasi",
                "body": [
                    "Wrangler adalah CLI resmi untuk Workers. Saat materi ini ditulis, seri",
                    "versinya 4.x dan rata-rata keluar lebih dari sekali seminggu. Proyek baru",
                    "dibuat dengan create-cloudflare, dijalankan lokal dengan wrangler dev, dan",
                    "di-deploy dengan wrangler deploy:",
                ],
                "code": """npm create cloudflare@latest -- catatan-edge
cd catatan-edge
npx wrangler kv namespace create CATATAN
npx wrangler dev
npx wrangler deploy""",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "Konfigurasinya ada di wrangler.jsonc atau wrangler.toml:",
                ],
                "code": "name = \"catatan-edge\"\nmain = \"src/index.js\"\ncompatibility_date = \"2026-10-01\"\ncompatibility_flags = [\"nodejs_compat\"]\n\n[[kv_namespaces]]\nbinding = \"CATATAN\"\nid = \"id-dari-perintah-kv-namespace-create\"",
                "bahasa": "toml",
            },
            {
                "heading": "Paket gratis dan batasnya",
                "body": [
                    "Menurut halaman harga resmi saat materi ini ditulis, paket Free memberi",
                    "100.000 permintaan per hari dan 10 milidetik waktu CPU per pemanggilan.",
                    "Paket berbayar mulai US$5 per bulan, sudah termasuk 10 juta permintaan dan",
                    "30 juta milidetik CPU per bulan. Permintaan ke aset statis gratis dan tanpa",
                    "batas.",
                    "",
                    "Waktu CPU berbeda dengan waktu tunggu. Worker yang menunggu jawaban fetch ke",
                    "server lain selama dua detik nggak menghabiskan jatah CPU selama menunggu",
                    "itu. Yang dihitung cuma waktu kodemu sedang bekerja, jadi 10 milidetik cukup",
                    "untuk banyak API kecil, tapi nggak cukup untuk mengolah gambar.",
                    "",
                    "Jebakan: bergantung pada satu penyedia jaringan. Gangguan global Cloudflare",
                    "pada November 2025 membuat banyak situs yang memakainya nggak bisa diakses",
                    "beberapa jam. Untuk layanan penting, siapkan rencana kalau penyedia di",
                    "depanmu sedang bermasalah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Workers sering dipakai untuk API kecil, pengalihan URL, A/B test, penambahan",
                    "header keamanan, dan pemendek tautan, karena jaraknya dekat dengan pengguna",
                    "dan paket gratisnya cukup untuk proyek pribadi. Learning Center Cloudflare",
                    "menjelaskan dasar DNS, CDN, dan DDoS dengan bahasa yang mudah.",
                    "",
                    "Kasus kecil: kamu punya server kecil di rumah yang menjalankan aplikasi",
                    "catatan, tapi penyedia internetmu nggak memberi IP publik dan kamu nggak mau",
                    "membuka port di router.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan DNS domainmu ke Cloudflare di paket Free.",
                    "  2. Pasang cloudflared di server rumah, lalu buat Tunnel yang mengarahkan",
                    "     catatan.domainmu.id ke localhost:8080.",
                    "  3. Aktifkan Cloudflare Access supaya cuma email-mu yang bisa membuka",
                    "     aplikasi itu.",
                    "  4. Untuk bagian yang sering dibaca dan jarang berubah, buat Worker dengan",
                    "     binding KV sebagai cache di depan servermu.",
                ],
            },
        ],
    },
    {
        "title": "29. Peta Platform Deploy: Cloud Run, Vercel, Heroku, Firebase",
        "sections": [
            {
                "body": [
                    "Di antara \"sewa server dan urus sendiri\" dan \"tulis satu fungsi\", ada banyak",
                    "platform yang menerima kode atau container lalu mengurus sisanya. Pilihan",
                    "ini sering lebih cocok untuk proyek pertama, portofolio, atau startup kecil",
                    "yang belum punya tim DevOps.",
                    "",
                    "Yang paling sering berubah di platform-platform ini adalah aturan paket",
                    "gratisnya. Angka di bawah dicek saat materi ini ditulis (Oktober 2026);",
                    "selalu baca halaman harga resminya sebelum memilih.",
                ],
            },
            {
                "heading": "Container dan fungsi di penyedia besar",
                "body": [
                    "  - Google Cloud Run: menjalankan container apa pun sebagai layanan yang",
                    "    menskalakan otomatis, termasuk sampai nol saat sepi. Kamu cukup punya",
                    "    Dockerfile. Free tier bulanannya 2 juta permintaan, 180.000 vCPU-detik,",
                    "    dan 360.000 GB-detik. Google Cloud Functions sekarang bernama Cloud Run",
                    "    functions. Padanannya di AWS adalah App Runner atau Fargate, di Azure",
                    "    adalah Container Apps.",
                    "  - Azure Functions: FaaS milik Microsoft dengan model trigger dan binding.",
                    "    Trigger adalah pemicu (HTTP, antrean, timer), binding adalah sambungan",
                    "    masukan dan keluaran yang ditulis deklaratif. Host runtime-nya open",
                    "    source berlisensi MIT.",
                ],
                "code": "gcloud run deploy toko-api --source . --region asia-southeast2 \\\n  --allow-unauthenticated",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "Perintah itu membangun container dari kode di folder sekarang, menyimpannya",
                    "di Artifact Registry, lalu menjalankannya di region Jakarta. Opsi",
                    "--allow-unauthenticated membuat layanannya bisa dibuka publik; tanpa opsi",
                    "itu, pemanggil harus punya izin IAM.",
                ],
            },
            {
                "heading": "Platform untuk frontend",
                "body": [
                    "  - Vercel: dibuat oleh pembuat Next.js. Tiap push ke Git menghasilkan URL",
                    "    preview, jadi peninjau bisa membuka versi pull request sebelum di-merge.",
                    "    Paket Hobby gratis hanya untuk pemakaian pribadi non-komersial, dan",
                    "    kalau kuotanya terlewati, fitur dijeda sampai 30 hari. Dipakai 10,7",
                    "    persen responden Stack Overflow 2026.",
                    "  - Netlify: hosting situs statis dan frontend dengan fungsi serverless,",
                    "    formulir, dan preview deploy. Netlify yang mempopulerkan istilah",
                    "    Jamstack. Sejak September 2025 akun baru memakai paket berbasis kredit:",
                    "    Free 300 kredit per bulan, Personal US$9, dan Pro US$20 per anggota.",
                ],
            },
            {
                "heading": "PaaS: kirim kode, platform yang urus",
                "body": [
                    "  - Heroku: pelopor PaaS dengan deploy lewat git push dan berkas Procfile.",
                    "    Dyno gratisnya dihapus November 2022. Pada 6 Februari 2026 Salesforce",
                    "    mengumumkan Heroku masuk mode sustaining engineering: tanpa fitur baru",
                    "    dan tanpa kontrak Enterprise untuk pelanggan baru. Konsepnya masih layak",
                    "    dipelajari, tapi jangan dijadikan tujuan deploy pertama untuk proyek",
                    "    baru.",
                    "  - Render: PaaS modern yang sering disebut pengganti Heroku, untuk web",
                    "    service, worker, cron, Postgres, dan Redis. Di paket gratis, web service",
                    "    tidur setelah 15 menit tanpa lalu lintas, jadi permintaan pertama",
                    "    sesudahnya lambat. Jatahnya 750 jam instans per bulan per workspace, dan",
                    "    Postgres gratis kedaluwarsa 30 hari setelah dibuat.",
                    "  - Railway: PaaS dengan antarmuka kanvas untuk menyusun layanan dan",
                    "    database. Ada uji coba 30 hari dengan hibah US$5, lalu paket Free berisi",
                    "    kredit US$1 per bulan; paket Hobby US$5 per bulan.",
                    "  - Fly.io: menjalankan container sebagai micro-VM di banyak region dekat",
                    "    pengguna. Nggak ada free tier untuk pengguna baru; bayar sesuai pakai",
                    "    dengan kartu kredit, dengan uji coba singkat.",
                    "",
                    "Procfile adalah warisan Heroku yang masih dipahami beberapa platform lain.",
                    "Isinya cuma daftar proses:",
                ],
                "code": """web: gunicorn toko.wsgi --bind 0.0.0.0:$PORT
worker: python worker.py""",
                "bahasa": "teks",
            },
            {
                "body": [
                    "Platform memberi tahu aplikasimu port mana yang harus dipakai lewat variabel",
                    "lingkungan PORT. Aplikasi yang menulis port 8000 secara tetap akan gagal",
                    "health check di banyak PaaS. Prinsip ini berasal dari The Twelve-Factor App:",
                    "konfigurasi lewat variabel lingkungan, bukan ditulis di kode.",
                ],
            },
            {
                "heading": "BaaS: backend siap pakai",
                "body": [
                    "  - Firebase: Backend-as-a-Service milik Google dengan autentikasi, database",
                    "    Firestore, Hosting, Cloud Functions, notifikasi push, dan Crashlytics.",
                    "    Dipakai 11,1 persen responden Stack Overflow 2026.",
                    "  - Supabase: alternatif Firebase berbasis PostgreSQL, dengan auth, storage,",
                    "    realtime, dan edge functions. Sebagian besar komponennya berlisensi",
                    "    Apache-2.0 dan bisa dipasang sendiri dengan Docker Compose. Dipakai 6,9",
                    "    persen responden survei yang sama.",
                    "",
                    "Jebakan: di BaaS, frontend bicara langsung ke database. Penjaganya cuma",
                    "aturan keamanan: Security Rules di Firebase dan Row Level Security di",
                    "Supabase. Aturan yang lupa dipasang berarti siapa pun yang membuka DevTools",
                    "bisa membaca seluruh tabel. Kunci service_role Supabase nggak boleh pernah",
                    "dikirim ke frontend.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Developer frontend sering memakai Vercel atau Netlify untuk portofolio dan",
                    "proyek klien, sementara aplikasi backend kecil banyak yang jalan di Cloud",
                    "Run, Render, atau Railway. Semua platform itu punya halaman status dan",
                    "halaman harga yang bisa kamu pantau.",
                    "",
                    "Kasus kecil: kamu punya aplikasi Flask kecil plus database untuk tugas PKL,",
                    "budget nol rupiah, dan pembimbing ingin bisa membukanya kapan saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan aplikasi membaca port dari variabel PORT dan URL database dari",
                    "     variabel lingkungan.",
                    "  2. Bandingkan tiga calon: Cloud Run (free tier bulanan, butuh kartu",
                    "     kredit), Render (gratis tapi tidur 15 menit), dan Railway (kredit",
                    "     kecil).",
                    "  3. Kalau memilih Render, beri tahu pembimbing bahwa buka pertama bisa",
                    "     lambat, dan cadangkan database sebelum 30 hari karena Postgres",
                    "     gratisnya kedaluwarsa.",
                    "  4. Catat tanggal pengecekan harga di README, karena aturan paket gratis",
                    "     bisa berubah sewaktu-waktu.",
                ],
            },
        ],
    },
    {
        "title": "30. Terraform: Infrastruktur Ditulis sebagai Kode",
        "sections": [
            {
                "body": [
                    "Di bab cloud, kamu membuat VPC, subnet, dan bucket dengan mengeklik konsol",
                    "atau mengetik perintah aws satu per satu. Cara itu cepat untuk belajar, tapi",
                    "bermasalah begitu infrastrukturnya tumbuh. Tiga bulan kemudian nggak ada",
                    "yang ingat setelan apa yang dipilih, lingkungan staging ternyata beda dengan",
                    "produksi, dan membuat ulang semuanya di region lain butuh berhari-hari.",
                    "",
                    "Infrastructure as Code (IaC) artinya infrastruktur ditulis di berkas teks,",
                    "disimpan di Git, ditinjau lewat pull request, lalu dibuat oleh alat. Berkas",
                    "itu jadi catatan yang selalu sesuai dengan kenyataan, dan lingkungan baru",
                    "bisa dibuat dari berkas yang sama.",
                    "",
                    "Terraform adalah alat IaC yang paling banyak dipakai: 18,3 persen responden",
                    "Survei Stack Overflow 2026. Versi terbarunya saat materi ini ditulis 1.16.6",
                    "(14 Oktober 2026). Sejak versi 1.6 (Agustus 2023) lisensinya BUSL-1.1, yang",
                    "membatasi pemakaian untuk produk pesaing HashiCorp. Sejak Februari 2025",
                    "HashiCorp dimiliki IBM. Fork open source-nya, OpenTofu, dibahas di materi",
                    "peta di akhir bab ini; perintah dan sintaksnya hampir sama.",
                ],
            },
            {
                "heading": "Deklaratif: tulis hasil akhirnya",
                "body": [
                    "Skrip bash menulis langkah: buat ini, lalu itu. Terraform bersifat",
                    "deklaratif: kamu menulis keadaan akhir yang kamu inginkan, dan Terraform",
                    "menghitung sendiri langkah untuk mencapainya. Kalau VPC sudah ada dan",
                    "sesuai, Terraform nggak membuatnya lagi. Kalau ada yang beda, ia mengubah",
                    "bagian yang beda saja.",
                    "",
                    "Bahasanya HCL (HashiCorp Configuration Language). Isinya blok-blok dengan",
                    "pola jenis \"label\" { atribut = nilai }. Terraform membaca semua berkas .tf",
                    "di satu folder sekaligus, jadi pembagian berkas cuma soal kerapian.",
                ],
            },
            {
                "heading": "Konfigurasi pertama",
                "body": [
                    "Simpan sebagai main.tf di folder kosong:",
                ],
                "code": """terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "ap-southeast-3"
}

resource "aws_vpc" "utama" {
  cidr_block = "10.0.0.0/16"
  tags       = { Name = "toko-utama" }
}

resource "aws_subnet" "publik" {
  vpc_id     = aws_vpc.utama.id
  cidr_block = "10.0.1.0/24"
}

output "vpc_id" {
  value = aws_vpc.utama.id
}""",
                "bahasa": "hcl",
            },
            {
                "body": [
                    "  - terraform: syarat versi Terraform dan provider. Provider adalah plugin",
                    "    yang tahu cara bicara dengan satu layanan, di sini AWS. ~> 6.0 berarti",
                    "    versi 6.x mana pun, tapi bukan 7.0.",
                    "  - provider: setelan provider, misalnya region.",
                    "  - variable: masukan yang bisa diganti tanpa mengubah kode, lewat berkas",
                    "    .tfvars atau opsi -var.",
                    "  - resource: satu objek infrastruktur. Labelnya dua: jenis (aws_vpc) dan",
                    "    nama lokal (utama). Alamatnya jadi aws_vpc.utama.",
                    "  - output: nilai yang dicetak sesudah apply, misalnya ID VPC.",
                    "",
                    "Perhatikan vpc_id = aws_vpc.utama.id. Itu referensi, dan Terraform",
                    "memakainya untuk menyusun urutan: subnet nggak bisa dibuat sebelum VPC-nya",
                    "ada. Program ini meniru caranya membaca referensi dan menyusun gelombang",
                    "pembuatan:",
                ],
                "code": "import re\n\n# Atribut tiap resource, disalin dari main.tf di atas (disederhanakan)\nresource = {\n    \"aws_vpc.utama\": {\"cidr_block\": \"10.0.0.0/16\"},\n    \"aws_subnet.publik\": {\"vpc_id\": \"aws_vpc.utama.id\",\n                          \"cidr_block\": \"10.0.1.0/24\"},\n    \"aws_security_group.web\": {\"vpc_id\": \"aws_vpc.utama.id\"},\n    \"aws_instance.web\": {\"subnet_id\": \"aws_subnet.publik.id\",\n                         \"vpc_security_group_ids\": \"aws_security_group.web.id\"},\n}\n\nREF = re.compile(r\"(aws_\\w+\\.\\w+)\\.\\w+\")\nbutuh = {nama: {m for v in attr.values() for m in REF.findall(v)}\n         for nama, attr in resource.items()}\n\ndibuat = []\nwhile len(dibuat) < len(resource):\n    gelombang = sorted(n for n in resource\n                       if n not in dibuat and butuh[n] <= set(dibuat))\n    print(\"buat bersamaan:\", \", \".join(gelombang))\n    dibuat += gelombang",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  buat bersamaan: aws_vpc.utama",
                    "  buat bersamaan: aws_security_group.web, aws_subnet.publik",
                    "  buat bersamaan: aws_instance.web",
                    "",
                    "Security group dan subnet sama-sama cuma butuh VPC, jadi keduanya dibuat",
                    "bersamaan. Terraform melakukan hal yang sama dengan membangun graf",
                    "dependensi, dan bawaannya menjalankan sampai 10 operasi paralel.",
                ],
            },
            {
                "heading": "Siklus init, plan, apply, destroy",
                "code": """terraform init       # unduh provider, siapkan backend
terraform fmt        # rapikan format semua berkas .tf
terraform validate   # cek sintaks dan referensi
terraform plan -out=rencana.tfplan
terraform apply rencana.tfplan
terraform output vpc_id
terraform destroy    # hapus semua yang dikelola konfigurasi ini""",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "init cukup dijalankan sekali per folder, atau saat provider dan backend",
                    "berubah. plan menampilkan apa yang akan dibuat, diubah, atau dihapus, tanpa",
                    "menyentuh apa pun. Menyimpan plan ke berkas lalu meng-apply berkas itu",
                    "menjamin yang dijalankan persis yang sudah kamu baca. Kredensial AWS dibaca",
                    "dari tempat yang sama dengan AWS CLI, jadi jangan pernah menulis access key",
                    "di berkas .tf.",
                    "",
                    "Jebakan: destroy menghapus semua yang dikelola folder itu, termasuk",
                    "database. Untuk sumber daya penting, tambahkan blok lifecycle berisi",
                    "prevent_destroy = true supaya Terraform menolak menghapusnya.",
                    "",
                    "Jebakan: mengubah sumber daya lewat konsol padahal ia dikelola Terraform.",
                    "Plan berikutnya akan mengembalikannya ke isi berkas, dan perubahan manualmu",
                    "hilang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua tim yang memakai cloud secara serius menyimpan infrastrukturnya",
                    "sebagai kode, dan Terraform paling sering disebut di lowongan DevOps dan",
                    "cloud engineer. Registry Terraform (registry.terraform.io) memuat",
                    "dokumentasi setiap resource lengkap dengan contoh.",
                    "",
                    "Kasus kecil: bucket S3 untuk foto toko dibuat manual setahun lalu. Sekarang",
                    "kamu diminta membuat bucket yang sama persis untuk lingkungan staging, dan",
                    "nggak ada yang ingat setelannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis resource aws_s3_bucket, aws_s3_bucket_versioning, dan",
                    "     aws_s3_bucket_public_access_block di main.tf.",
                    "  2. Ambil alih bucket produksi yang sudah ada dengan blok import, lalu",
                    "     jalankan plan sampai hasilnya No changes, tanda berkasmu sudah sama",
                    "     dengan kenyataan.",
                    "  3. Ubah nama bucket jadi variabel, lalu buat berkas staging.tfvars dan",
                    "     produksi.tfvars.",
                    "  4. Jalankan plan dan apply dengan -var-file=staging.tfvars untuk membuat",
                    "     bucket staging dari kode yang sama.",
                ],
            },
        ],
    },
    {
        "title": "31. Terraform State, Plan, dan Backend Jarak Jauh",
        "sections": [
            {
                "body": [
                    "Terraform perlu tahu bahwa aws_vpc.utama di berkasmu adalah VPC vpc-0a1b2c",
                    "di akun AWS. Catatan itu disebut state: berkas JSON yang mencatat pasangan",
                    "antara alamat di konfigurasi dan objek sungguhan, beserta atribut terakhir",
                    "yang diketahui. Bawaannya disimpan di terraform.tfstate di folder kerja.",
                    "",
                    "Setiap plan membandingkan tiga hal: konfigurasi (yang kamu mau), state (yang",
                    "terakhir dicatat), dan keadaan sungguhan di cloud (yang dibaca ulang saat",
                    "refresh). Selisihnya jadi rencana.",
                ],
            },
            {
                "heading": "Membaca hasil plan",
                "code": """Terraform will perform the following actions:

  # aws_instance.web will be updated in-place
  ~ resource "aws_instance" "web" {
      ~ instance_type = "t3.micro" -> "t3.small"
        id            = "i-0abc123"
    }

  # aws_instance.batch must be replaced
-/+ resource "aws_instance" "batch" {
      ~ ami = "ami-0a1" -> "ami-0b2" # forces replacement
    }

  # aws_s3_bucket.foto will be created
  + resource "aws_s3_bucket" "foto" {
      + bucket = "foto-toko-2026"
    }

Plan: 2 to add, 1 to change, 1 to destroy.""",
                "bahasa": "teks",
            },
            {
                "body": [
                    "  - + create: objek baru akan dibuat.",
                    "  - ~ update in-place: objek diubah tanpa dihapus. Mengganti instance_type",
                    "    cukup menghentikan lalu menyalakan ulang instance.",
                    "  - -/+ replace: objek dihapus lalu dibuat ulang, karena ada atribut yang",
                    "    nggak bisa diubah di tempat. Terraform menandainya dengan forces",
                    "    replacement. Mengganti AMI berarti instance baru, disk root baru, dan IP",
                    "    privat baru.",
                    "  - - destroy: objek akan dihapus karena sudah nggak ada di konfigurasi.",
                    "  - <= read: data source yang hanya dibaca, misalnya mencari AMI terbaru.",
                    "",
                    "Replace dihitung dua kali di ringkasan: satu to add dan satu to destroy.",
                    "Biasakan membaca baris Plan sebelum mengetik yes. Kalau kamu cuma mengganti",
                    "tag tapi plan bilang 1 to destroy, berhenti dan cari tahu dulu.",
                ],
            },
            {
                "heading": "State memuat rahasia",
                "body": [
                    "State menyimpan atribut apa adanya, termasuk kata sandi database yang kamu",
                    "set lewat Terraform. Program ini mencari atribut yang mencurigakan di sebuah",
                    "state tiruan:",
                ],
                "code": "import json\n\nstate = json.loads(\"\"\"\n{\n  \"version\": 4,\n  \"terraform_version\": \"1.16.6\",\n  \"resources\": [\n    {\"type\": \"aws_db_instance\", \"name\": \"utama\",\n     \"instances\": [{\"attributes\": {\"identifier\": \"toko-db\",\n                                   \"username\": \"admin\",\n                                   \"password\": \"Rahasia123!\"}}]},\n    {\"type\": \"aws_s3_bucket\", \"name\": \"foto\",\n     \"instances\": [{\"attributes\": {\"bucket\": \"foto-toko-2026\"}}]}\n  ]\n}\n\"\"\")\n\nCURIGA = (\"password\", \"secret\", \"token\", \"private_key\")\nfor r in state[\"resources\"]:\n    for inst in r[\"instances\"]:\n        for kunci, nilai in inst[\"attributes\"].items():\n            if any(c in kunci for c in CURIGA):\n                print(f\"{r['type']}.{r['name']}: {kunci} = {nilai}\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  aws_db_instance.utama: password = Rahasia123!",
                    "",
                    "Menandai variabel dengan sensitive = true cuma menyembunyikannya dari",
                    "tampilan plan, bukan dari berkas state. Karena itu:",
                    "",
                    "  - Jangan pernah commit terraform.tfstate. Masukkan *.tfstate dan",
                    "    *.tfstate.* ke .gitignore, juga folder .terraform.",
                    "  - Commit .terraform.lock.hcl. Berkas itu mengunci versi provider supaya",
                    "    semua orang memakai versi yang sama.",
                    "  - Simpan state di backend jarak jauh yang terenkripsi dan aksesnya",
                    "    dibatasi.",
                ],
            },
            {
                "heading": "Backend jarak jauh dan locking",
                "body": [
                    "State di laptop cuma cocok untuk belajar sendiri. Begitu ada dua orang, atau",
                    "ada pipeline CI, state harus disimpan di satu tempat bersama. Tempat itu",
                    "disebut backend. Backend juga harus punya locking, yaitu kunci yang mencegah",
                    "dua apply berjalan bersamaan dan saling menimpa state.",
                ],
                "code": """terraform {
  backend "s3" {
    bucket       = "state-terraform-toko"
    key          = "produksi/jaringan.tfstate"
    region       = "ap-southeast-3"
    encrypt      = true
    use_lockfile = true
  }
}""",
                "bahasa": "hcl",
            },
            {
                "body": [
                    "use_lockfile = true membuat Terraform menaruh berkas kunci .tflock di bucket",
                    "yang sama. Cara lama memakai tabel DynamoDB untuk locking, dan menurut",
                    "dokumentasi resmi cara itu sudah usang dan akan dihapus di versi minor",
                    "mendatang. Aktifkan versioning di bucket state supaya state lama bisa",
                    "dipulihkan kalau rusak.",
                    "",
                    "Pilihan backend lain: HCP Terraform (layanan HashiCorp), Google Cloud",
                    "Storage, Azure Blob Storage, dan HTTP. Paket gratis lama HCP Terraform",
                    "berakhir 31 Maret 2026 dan diganti paket Free dengan batas 500 resource",
                    "terkelola.",
                ],
            },
            {
                "heading": "Perintah untuk merawat state",
                "code": """terraform state list
terraform state show aws_instance.web
terraform plan -refresh-only     # lihat drift tanpa mengubah apa pun
terraform force-unlock <ID-KUNCI>""",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "Drift adalah perbedaan antara state dan kenyataan karena ada yang mengubah",
                    "lewat konsol. plan -refresh-only menampilkannya tanpa mengubah",
                    "infrastruktur. Untuk mengganti nama resource di kode tanpa menghapus",
                    "objeknya, pakai blok moved di konfigurasi. Untuk mengambil alih objek yang",
                    "dibuat manual, pakai blok import.",
                    "",
                    "Jebakan: force-unlock saat apply orang lain masih berjalan. Pakai hanya",
                    "kalau kamu yakin prosesnya sudah mati, misalnya runner CI yang dihentikan di",
                    "tengah jalan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang memakai Terraform biasanya punya satu bucket khusus state per akun,",
                    "dengan versioning, enkripsi, dan akses yang cuma diberikan ke role CI dan",
                    "beberapa orang. Dokumentasi backend s3 di situs HashiCorp memuat daftar izin",
                    "IAM yang dibutuhkan.",
                    "",
                    "Kasus kecil: terraform.tfstate milik proyek PKL ternyata ikut ter-commit ke",
                    "repositori GitHub tim, dan di dalamnya ada kata sandi RDS.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Anggap kata sandi itu bocor: ganti kata sandi database sekarang juga.",
                    "  2. Buat bucket state dengan versioning dan Block Public Access, tambahkan",
                    "     blok backend s3 dengan use_lockfile, lalu jalankan terraform init",
                    "     -migrate-state.",
                    "  3. Hapus terraform.tfstate dari repositori dan tambahkan pola *.tfstate ke",
                    "     .gitignore. Riwayat Git masih menyimpannya, jadi bersihkan riwayat atau",
                    "     anggap semua isinya sudah bocor.",
                    "  4. Ke depan, minta RDS membuat dan menyimpan kata sandinya sendiri di",
                    "     Secrets Manager (manage_master_user_password), supaya kata sandinya",
                    "     nggak pernah masuk state.",
                ],
            },
        ],
    },
    {
        "title": "32. Modul Terraform dan Terraform di Pipeline",
        "sections": [
            {
                "body": [
                    "Begitu konfigurasi tumbuh, kamu akan menyalin blok yang sama berkali-kali:",
                    "VPC untuk dev, VPC untuk staging, VPC untuk produksi. Salinan yang lupa",
                    "diperbarui adalah awal dari lingkungan yang nggak sama lagi. Modul",
                    "memecahkan itu.",
                    "",
                    "Modul adalah folder berisi berkas .tf yang dipanggil dari konfigurasi lain,",
                    "mirip fungsi di pemrograman. Masukannya variable, keluarannya output. Setiap",
                    "folder Terraform pun sudah modul; folder tempat kamu menjalankan perintah",
                    "disebut root module.",
                ],
            },
            {
                "heading": "Struktur folder yang umum",
                "code": """infra/
├── modules/
│   └── web/
│       ├── main.tf        resource: ALB, ASG, security group
│       ├── variables.tf   masukan: nama, ukuran, subnet
│       └── outputs.tf     keluaran: url
└── lingkungan/
    ├── staging/
    │   ├── main.tf        memanggil modules/web
    │   └── backend.tf     state: staging/web.tfstate
    └── produksi/
        ├── main.tf
        └── backend.tf     state: produksi/web.tfstate""",
                "bahasa": "teks",
            },
            {
                "body": [
                    "Tiap lingkungan punya folder dan state sendiri. Kesalahan di staging nggak",
                    "bisa merusak state produksi, dan izin untuk meng-apply produksi bisa",
                    "dibatasi ke orang dan pipeline tertentu.",
                ],
            },
            {
                "heading": "Memanggil modul",
                "code": """module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 6.7"

  name            = "toko-staging"
  cidr            = "10.20.0.0/16"
  azs             = ["ap-southeast-3a", "ap-southeast-3b"]
  public_subnets  = ["10.20.0.0/24", "10.20.1.0/24"]
  private_subnets = ["10.20.16.0/20", "10.20.32.0/20"]

  enable_nat_gateway = true
  single_nat_gateway = true
}

module "web" {
  source     = "../../modules/web"
  nama       = "toko-staging"
  subnet_ids = module.vpc.private_subnets
}""",
                "bahasa": "hcl",
            },
            {
                "body": [
                    "Modul pertama diambil dari Terraform Registry. Modul VPC buatan komunitas",
                    "terraform-aws-modules adalah salah satu yang paling banyak dipakai, dan",
                    "versi terbarunya saat materi ini ditulis 6.7.3. single_nat_gateway = true",
                    "memasang satu NAT gateway saja untuk menghemat biaya di staging, seperti",
                    "saran di bab cloud.",
                    "",
                    "Modul kedua diambil dari folder lokal. Output modul VPC",
                    "(module.vpc.private_subnets) langsung jadi masukan modul web.",
                    "",
                    "Jebakan: tanpa version, modul dari registry selalu mengambil versi terbaru",
                    "saat init, dan suatu hari versi mayor baru mengubah perilakunya. Selalu",
                    "tulis batas versi untuk modul dan provider.",
                    "",
                    "Jebakan: modul yang terlalu dini. Membungkus satu resource jadi modul cuma",
                    "menambah lapisan. Buat modul kalau ada pola yang memang dipakai ulang di dua",
                    "tempat atau lebih.",
                ],
            },
            {
                "heading": "Terraform di pipeline",
                "body": [
                    "Menjalankan apply dari laptop masing-masing berarti nggak ada catatan siapa",
                    "mengubah apa, dan kredensial produksi tersebar di banyak laptop. Pola yang",
                    "dipakai banyak tim: plan otomatis di setiap pull request, apply cuma dari",
                    "cabang main dengan persetujuan. Kredensial cloud diambil lewat OIDC seperti",
                    "di bab CI/CD.",
                ],
                "code": "name: terraform\non:\n  pull_request:\n    paths: [\"infra/**\"]\n  push:\n    branches: [main]\n    paths: [\"infra/**\"]\n\npermissions:\n  id-token: write\n  contents: read\n  pull-requests: write\n\njobs:\n  plan:\n    runs-on: ubuntu-latest\n    defaults:\n      run:\n        working-directory: infra/lingkungan/staging\n    steps:\n      - uses: actions/checkout@v7\n      - uses: hashicorp/setup-terraform@v4\n      - uses: aws-actions/configure-aws-credentials@v6\n        with:\n          role-to-assume: arn:aws:iam::123456789012:role/terraform-plan\n          aws-region: ap-southeast-3\n      - run: terraform init -input=false\n      - run: terraform fmt -check\n      - run: terraform validate\n      - run: terraform plan -input=false -out=rencana.tfplan\n\n  apply:\n    needs: plan\n    if: github.ref == 'refs/heads/main'\n    environment: staging\n    runs-on: ubuntu-latest\n    steps:\n      - run: echo \"init, plan ulang, lalu apply dengan role terraform-apply\"",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Role untuk plan sebaiknya cuma bisa membaca, sedangkan role untuk apply",
                    "punya izin menulis dan cuma bisa dipakai dari environment yang dilindungi",
                    "persetujuan. Job apply di contoh disingkat; di proyek sungguhan ia",
                    "menjalankan init, plan, lalu apply, atau mengambil berkas plan dari job",
                    "sebelumnya sebagai artefak.",
                    "",
                    "Dua alat yang sering ditambahkan ke job plan. Checkov memindai kode",
                    "Terraform untuk salah konfigurasi keamanan, misalnya bucket tanpa enkripsi;",
                    "detailnya ada di kurikulum Keamanan Siber. Infracost menghitung perkiraan",
                    "perubahan biaya bulanan dan menuliskannya sebagai komentar di pull request,",
                    "jadi peninjau tahu bahwa perubahan itu menambah US$33 sebulan sebelum",
                    "di-merge. Versi Infracost saat materi ini ditulis 0.10.46.",
                ],
            },
            {
                "heading": "Workspace atau folder terpisah?",
                "body": [
                    "Terraform punya fitur workspace: satu folder konfigurasi dengan beberapa",
                    "state terpisah, dipilih lewat terraform workspace select staging.",
                    "Kelihatannya praktis untuk memisahkan lingkungan, tapi semua workspace",
                    "memakai backend dan kredensial yang sama, dan perbedaan antar lingkungan",
                    "harus ditulis sebagai kondisi di kode.",
                    "",
                    "Dokumentasi HashiCorp sendiri menyebut workspace CLI kurang cocok untuk",
                    "memisahkan lingkungan yang butuh kredensial dan kontrol akses berbeda,",
                    "misalnya staging dan produksi. Untuk kasus itu, folder terpisah per",
                    "lingkungan seperti struktur di atas lebih aman. Workspace tetap berguna",
                    "untuk salinan sementara, misalnya satu lingkungan uji per pull request yang",
                    "dihapus sesudah di-merge.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola plan di pull request dan apply dari cabang utama adalah bentuk paling",
                    "umum Terraform di tim. Atlantis, HCP Terraform, dan Spacelift adalah alat",
                    "yang khusus menjalankan alur ini, dan GitHub Actions dengan setup-terraform",
                    "adalah versi paling sederhananya.",
                    "",
                    "Kasus kecil: tim kalian bertiga sering meng-apply Terraform staging dari",
                    "laptop masing-masing, dan minggu lalu dua apply bertabrakan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan state ke backend s3 dengan use_lockfile seperti di materi",
                    "     sebelumnya.",
                    "  2. Buat dua role IAM lewat OIDC: terraform-plan yang cuma membaca dan",
                    "     terraform-apply yang bisa menulis.",
                    "  3. Tambahkan workflow seperti contoh, lalu lindungi environment staging",
                    "     dengan satu peninjau wajib.",
                    "  4. Cabut izin tulis AWS dari akun pribadi, sehingga satu-satunya jalan",
                    "     mengubah staging adalah lewat pull request.",
                ],
            },
        ],
    },
    {
        "title": "33. Ansible: Otomasi Server Lewat SSH",
        "sections": [
            {
                "body": [
                    "Terraform membuat servernya. Tapi server baru masih kosong: belum ada Nginx,",
                    "belum ada pengguna aplikasi, SSH-nya masih mengizinkan login root.",
                    "Mengurusnya satu per satu lewat SSH masih bisa untuk satu server. Untuk dua",
                    "puluh server, kamu butuh alat.",
                    "",
                    "Ansible adalah alat otomasi konfigurasi tanpa agen. Dari satu mesin, yang",
                    "disebut control node, Ansible masuk lewat SSH ke banyak server sekaligus dan",
                    "menjalankan tugas yang kamu tulis. Server target cuma butuh SSH dan Python,",
                    "nggak perlu program khusus yang berjalan terus.",
                    "",
                    "Ansible dipakai 12,0 persen responden Survei Stack Overflow 2026, terbanyak",
                    "di antara alat manajemen konfigurasi. Ia ditulis dengan Python, berlisensi",
                    "GPL-3.0, dan dipelihara Red Hat bersama komunitas. Saat materi ini ditulis,",
                    "versi ansible-core terbaru 2.21.5, dan paket komunitas ansible (core plus",
                    "ratusan koleksi modul) 14.5.0.",
                ],
            },
            {
                "heading": "Inventaris: daftar server",
                "body": [
                    "Inventaris adalah daftar host yang dikelompokkan. Bentuk INI paling ringkas:",
                ],
                "code": """[web]
web1.toko.id
web2.toko.id ansible_port=2222

[db]
db1.toko.id

[produksi:children]
web
db

[all:vars]
ansible_user=deploy""",
                "bahasa": "ini",
            },
            {
                "body": [
                    "Grup produksi berisi grup web dan db lewat :children. Variabel seperti",
                    "ansible_port dan ansible_user mengatur cara Ansible terhubung. Program ini",
                    "membaca bentuk yang sama untuk menunjukkan anggota tiap grup:",
                ],
                "code": "inventaris = \"\"\"\n[web]\nweb1.toko.id\nweb2.toko.id ansible_port=2222\n\n[db]\ndb1.toko.id\n\n[produksi:children]\nweb\ndb\n\"\"\"\n\ngrup, anak, sekarang = {}, {}, None\nfor baris in inventaris.strip().splitlines():\n    if baris.startswith(\"[\"):\n        nama = baris.strip(\"[]\")\n        if nama.endswith(\":children\"):\n            sekarang = (\"anak\", nama.split(\":\")[0])\n            anak[sekarang[1]] = []\n        else:\n            sekarang = (\"host\", nama)\n            grup[nama] = []\n    elif baris.strip():\n        jenis, nama = sekarang\n        (anak if jenis == \"anak\" else grup)[nama].append(baris.split()[0])\n\nfor induk, daftar in anak.items():\n    grup[induk] = [h for g in daftar for h in grup[g]]\nfor nama in sorted(grup):\n    print(f\"{nama:<9}\", \", \".join(grup[nama]))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  db        db1.toko.id",
                    "  produksi  web1.toko.id, web2.toko.id, db1.toko.id",
                    "  web       web1.toko.id, web2.toko.id",
                    "",
                    "Inventaris juga bisa ditulis dalam YAML, atau dibuat dinamis dari API cloud,",
                    "misalnya semua instance EC2 bertag env=produksi.",
                ],
            },
            {
                "heading": "Perintah ad-hoc",
                "body": [
                    "Untuk tugas sekali jalan, kamu nggak perlu menulis berkas apa pun:",
                ],
                "code": "pipx install --include-deps ansible\nansible all -i inventaris.ini -m ansible.builtin.ping\nansible web -i inventaris.ini -m ansible.builtin.command -a \"uptime\"\nansible web -i inventaris.ini -m ansible.builtin.dnf \\\n  -a \"name=nginx state=present\" --become",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "-m memilih modul, yaitu unit kerja Ansible seperti ping, command, dnf, copy,",
                    "atau service. Nama lengkapnya memakai awalan koleksi, misalnya",
                    "ansible.builtin.dnf. --become menjalankan tugas dengan sudo di host target.",
                    "Modul ping bukan ping jaringan; ia mengecek Ansible bisa masuk lewat SSH dan",
                    "menjalankan Python di sana.",
                ],
            },
            {
                "heading": "Playbook pertama",
                "body": [
                    "Tugas yang perlu diulang ditulis di playbook, berkas YAML berisi satu atau",
                    "beberapa play. Satu play memetakan grup host ke daftar tugas:",
                ],
                "code": """- name: Siapkan server web
  hosts: web
  become: true
  tasks:
    - name: Pasang Nginx
      ansible.builtin.dnf:
        name: nginx
        state: present

    - name: Matikan login root lewat SSH
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: "^#?PermitRootLogin"
        line: "PermitRootLogin no"
        validate: "sshd -t -f %s"
      notify: Restart sshd

    - name: Nginx menyala dan ikut start saat boot
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true

  handlers:
    - name: Restart sshd
      ansible.builtin.service:
        name: sshd
        state: restarted""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Tiap tugas menulis keadaan yang diinginkan (state: present, state: started),",
                    "bukan perintah. Handler cuma jalan kalau ada tugas yang memanggilnya lewat",
                    "notify dan tugas itu memang mengubah sesuatu, jadi sshd nggak di-restart",
                    "tiap kali playbook jalan. validate memeriksa berkas sshd_config baru sebelum",
                    "dipasang, supaya salah ketik nggak membuatmu terkunci di luar server.",
                ],
                "code": """ansible-playbook -i inventaris.ini web.yml --check --diff
ansible-playbook -i inventaris.ini web.yml""",
                "bahasa": "terminal",
            },
            {
                "body": [
                    "--check --diff menampilkan apa yang akan berubah tanpa mengubah apa pun,",
                    "mirip terraform plan. Di akhir setiap run, Ansible mencetak rekap (play",
                    "recap) berisi hitungan ok, changed, failed, dan unreachable per host.",
                    "",
                    "Jebakan: indentasi YAML dan tanda hubung. Tugas adalah item daftar di bawah",
                    "tasks, jadi diawali - dan menjorok sejajar. Satu spasi meleset membuat",
                    "Ansible mengira nama modul adalah atribut tugas.",
                ],
            },
            {
                "heading": "Ansible, skrip bash, atau Terraform?",
                "body": [
                    "Skrip bash yang dijalankan lewat SSH bisa mengerjakan hal yang sama, tapi",
                    "semua pengecekannya harus kamu tulis sendiri. Paket sudah terpasang atau",
                    "belum? Baris sudah ada atau belum? Layanan perlu di-restart atau nggak?",
                    "Ansible sudah menyediakan modul yang melakukan pengecekan itu, plus laporan",
                    "ok dan changed per host.",
                    "",
                    "Terraform dan Ansible saling melengkapi. Terraform paling kuat untuk membuat",
                    "dan menghapus sumber daya cloud karena ia mencatat state. Ansible paling",
                    "kuat untuk mengatur isi server yang sudah ada. Pola yang umum: Terraform",
                    "membuat VPC dan instance, lalu Ansible memasang paket dan konfigurasi di",
                    "instance itu. Kalau aplikasimu sudah jalan sebagai container di layanan",
                    "terkelola, kebutuhan Ansible biasanya mengecil.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Ansible sering dipakai untuk menyiapkan server baru, menambal paket di",
                    "banyak server sekaligus, dan menyebarkan konfigurasi seperti pengguna dan",
                    "kunci SSH. Dokumentasi resmi Ansible punya indeks modul ansible.builtin",
                    "lengkap dengan contoh tiap modul.",
                    "",
                    "Kasus kecil: tim kamu baru menyewa lima VPS Fedora, dan semuanya harus punya",
                    "pengguna deploy, kunci SSH tim, Nginx, dan SSH tanpa login root.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis inventaris berisi kelima host di grup web, dengan ansible_user",
                    "     root untuk run pertama saja.",
                    "  2. Tulis playbook dengan modul ansible.builtin.user,",
                    "     ansible.posix.authorized_key, dnf, lineinfile, dan service.",
                    "  3. Jalankan dengan --check --diff dulu, baru jalankan sungguhan.",
                    "  4. Ganti ansible_user jadi deploy, lalu jalankan sekali lagi. Rekap di",
                    "     akhir harus menunjukkan changed=0 di semua host.",
                ],
            },
        ],
    },
    {
        "title": "34. Ansible Lanjutan: Role, Template, dan Idempotensi",
        "sections": [
            {
                "body": [
                    "Playbook yang berisi semua tugas dalam satu berkas cepat jadi panjang.",
                    "Server web, server database, dan server pemantauan berbagi sebagian tugas,",
                    "misalnya pengerasan SSH, tapi beda di bagian lain. Ansible menyusunnya lewat",
                    "role: paket berisi tugas, template, dan variabel untuk satu peran.",
                ],
            },
            {
                "heading": "Struktur role",
                "code": """roles/
└── nginx/
    ├── defaults/main.yml    nilai bawaan variabel (mudah ditimpa)
    ├── vars/main.yml        variabel yang jarang diubah
    ├── tasks/main.yml       daftar tugas
    ├── handlers/main.yml    handler, misalnya reload nginx
    ├── templates/
    │   └── situs.conf.j2    template Jinja2
    ├── files/               berkas yang disalin apa adanya
    └── meta/main.yml        dependensi ke role lain""",
                "bahasa": "teks",
            },
            {
                "body": [
                    "Kerangka ini bisa dibuat dengan ansible-galaxy role init nginx. Ansible",
                    "otomatis membaca berkas main.yml di tiap folder, jadi playbook-nya tinggal",
                    "menyebut nama role:",
                ],
                "code": """- name: Server web
  hosts: web
  become: true
  roles:
    - common
    - role: nginx
      vars:
        nama_domain: tokoani.id
        port_aplikasi: 8000""",
                "bahasa": "yaml",
            },
            {
                "heading": "Template Jinja2",
                "body": [
                    "Berkas konfigurasi yang beda sedikit antar server ditulis sebagai template",
                    "Jinja2. {{ }} diganti nilai variabel, dan {% %} untuk logika seperti",
                    "perulangan:",
                ],
                "code": """# Dikelola Ansible. Perubahan manual akan ditimpa.
upstream aplikasi {
{% for host in groups['app'] %}
    server {{ hostvars[host]['ansible_host'] }}:{{ port_aplikasi }};
{% endfor %}
}

server {
    listen 80;
    server_name {{ nama_domain }};
    location / {
        proxy_pass http://aplikasi;
    }
}""",
                "bahasa": "jinja",
            },
            {
                "body": [
                    "Tugas di role memakai modul template untuk mengisi dan menyalin berkasnya,",
                    "lalu memanggil handler kalau isinya berubah:",
                ],
                "code": """- name: Pasang konfigurasi situs
  ansible.builtin.template:
    src: situs.conf.j2
    dest: /etc/nginx/conf.d/situs.conf
    mode: "0644"
    validate: "nginx -t -c /etc/nginx/nginx.conf"
  notify: Reload nginx""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Begitu ada server app baru di inventaris, run berikutnya menambahkannya ke",
                    "upstream secara otomatis. Variabel di defaults/main.yml punya prioritas",
                    "paling rendah, jadi gampang ditimpa dari playbook atau group_vars, sedangkan",
                    "vars/main.yml lebih sulit ditimpa. Taruh nilai yang memang boleh diubah",
                    "pemakai role di defaults.",
                ],
            },
            {
                "heading": "Idempotensi",
                "body": [
                    "Idempoten artinya menjalankan sesuatu sekali atau sepuluh kali hasilnya",
                    "sama. Playbook yang idempoten aman dijalankan ulang kapan saja: run pertama",
                    "mengubah yang perlu, run berikutnya melapor changed=0 karena semuanya sudah",
                    "sesuai. Itu juga cara cepat mendeteksi drift: kalau run rutin tiba-tiba",
                    "melapor changed, ada yang mengubah server di luar Ansible.",
                    "",
                    "Modul seperti dnf, lineinfile, dan template idempoten karena mereka",
                    "memeriksa keadaan dulu. Modul command dan shell nggak: Ansible nggak tahu",
                    "apa yang dilakukan perintahmu, jadi ia menjalankannya lagi dan selalu",
                    "melapor changed. Bedanya kelihatan di program ini:",
                ],
                "code": "def lineinfile(berkas, baris):\n    \"\"\"Seperti modul lineinfile: tambah hanya kalau belum ada.\"\"\"\n    if baris in berkas:\n        return \"ok\"\n    berkas.append(baris)\n    return \"changed\"\n\n\ndef shell_echo(berkas, baris):\n    \"\"\"Seperti shell: echo baris >> berkas. Selalu menambah.\"\"\"\n    berkas.append(baris)\n    return \"changed\"\n\n\nfor nama, fungsi in [(\"lineinfile\", lineinfile), (\"shell echo\", shell_echo)]:\n    berkas = [\"Port 22\"]\n    hasil = [fungsi(berkas, \"PermitRootLogin no\") for _ in range(3)]\n    print(f\"{nama:<10} {hasil} -> {len(berkas)} baris\")",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  lineinfile ['changed', 'ok', 'ok'] -> 2 baris",
                    "  shell echo ['changed', 'changed', 'changed'] -> 4 baris",
                    "",
                    "Kalau terpaksa memakai command atau shell, beri tahu Ansible cara menilai",
                    "perubahannya. creates: /jalur/berkas melewati tugas kalau berkas itu sudah",
                    "ada, dan changed_when menentukan kapan tugas dianggap mengubah sesuatu:",
                ],
                "code": """- name: Jalankan migrasi database
  ansible.builtin.command: /opt/toko/bin/migrasi --status-dulu
  register: migrasi
  changed_when: "'diterapkan' in migrasi.stdout"

- name: Unduh dan ekstrak aplikasi sekali saja
  ansible.builtin.unarchive:
    src: https://contoh.id/rilis/toko-1.4.0.tar.gz
    dest: /opt/toko
    remote_src: true
    creates: /opt/toko/VERSION""",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Jebakan: menyimpan kata sandi di group_vars dalam bentuk teks biasa. Ansible",
                    "Vault mengenkripsi berkas atau nilai variabel, dan kunci pembukanya",
                    "diberikan saat playbook dijalankan. Manajemen rahasia yang lebih luas",
                    "dibahas di kurikulum Keamanan Siber.",
                    "",
                    "Role buatan komunitas bisa diambil dari Ansible Galaxy, dan kumpulan modul",
                    "untuk layanan tertentu, seperti community.general atau amazon.aws, dikemas",
                    "sebagai collection. Periksa dulu kodenya dan kunci versinya di",
                    "requirements.yml, sama seperti action pihak ketiga di GitHub Actions.",
                ],
            },
            {
                "heading": "Fakta host dan kondisi when",
                "body": [
                    "Di awal setiap play, Ansible mengumpulkan fakta tentang host: distribusi",
                    "Linux, versi, alamat IP, jumlah memori. Fakta itu bisa dipakai di kondisi",
                    "when, jadi satu role bisa melayani Fedora dan Ubuntu sekaligus:",
                ],
                "code": "- name: Pasang Nginx di keluarga Red Hat\n  ansible.builtin.dnf:\n    name: nginx\n    state: present\n  when: ansible_facts[\"os_family\"] == \"RedHat\"\n\n- name: Pasang Nginx di keluarga Debian\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n    update_cache: true\n  when: ansible_facts[\"os_family\"] == \"Debian\"",
                "bahasa": "yaml",
            },
            {
                "body": [
                    "Untuk paket yang namanya sama di dua keluarga, modul ansible.builtin.package",
                    "memilih pengelola paket yang cocok secara otomatis. Kalau fakta nggak",
                    "dibutuhkan, gather_facts: false di play mempercepat run, terutama dengan",
                    "banyak host.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak tim menjalankan playbook Ansible secara terjadwal, misalnya tiap",
                    "malam dalam mode --check, untuk mendeteksi server yang konfigurasinya",
                    "bergeser. Proyek ansible-lint dan Molecule dipakai untuk memeriksa dan",
                    "menguji role sebelum dipakai di produksi.",
                    "",
                    "Kasus kecil: playbook lama di kantor selalu melapor changed=12 tiap",
                    "dijalankan, jadi nggak ada yang tahu kapan sebuah run memang mengubah",
                    "server.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan playbook dua kali berturut-turut dan catat tugas mana yang",
                    "     changed di run kedua.",
                    "  2. Ganti tugas shell echo ... >> berkas dengan lineinfile atau",
                    "     blockinfile.",
                    "  3. Untuk tugas command yang memang perlu, tambahkan creates atau",
                    "     changed_when sesuai keluaran perintahnya.",
                    "  4. Ulangi sampai run kedua melapor changed=0, lalu jalankan ansible-lint",
                    "     dan perbaiki peringatan no-changed-when.",
                ],
            },
        ],
    },
    {
        "title": "35. Peta IaC: OpenTofu, Pulumi, CloudFormation, Chef, Puppet",
        "sections": [
            {
                "body": [
                    "Terraform dan Ansible bukan satu-satunya pilihan. Sebagian alternatifnya",
                    "lahir karena urusan lisensi, sebagian karena ingin memakai bahasa",
                    "pemrograman biasa, dan sebagian adalah generasi lebih tua yang masih",
                    "menjalankan banyak server perusahaan.",
                ],
            },
            {
                "heading": "Peta alat",
                "code": """Alat            Jenis                 Bahasa            Lisensi       Status
--------------  --------------------  ----------------  ------------  -----------
Terraform       provisioning          HCL               BUSL-1.1      aktif
OpenTofu        provisioning          HCL               MPL-2.0       aktif
Pulumi          provisioning          Python, TS, Go    Apache-2.0    aktif
CloudFormation  provisioning (AWS)    YAML/JSON         proprietary   matang
AWS CDK         provisioning (AWS)    TS, Python, dll.  Apache-2.0    aktif
Packer          membuat image mesin   HCL               BUSL-1.1      matang
Ansible         konfigurasi, agentless YAML             GPL-3.0       aktif
Chef            konfigurasi, agen     Ruby              Apache-2.0*   menurun
Puppet/OpenVox  konfigurasi, agen     Puppet DSL        Apache-2.0*   menurun
Salt            konfigurasi, agen     YAML + Jinja      Apache-2.0    menurun

* kode sumbernya Apache-2.0, tapi biner resmi Chef dan Puppet butuh lisensi
  komersial; OpenVox adalah fork komunitas Puppet.""",
                "bahasa": "teks",
            },
            {
                "heading": "OpenTofu: fork open source Terraform",
                "body": [
                    "OpenTofu lahir pada 2023 setelah HashiCorp mengganti lisensi Terraform ke",
                    "BUSL. Proyeknya ada di bawah Linux Foundation, berlisensi MPL-2.0, dan",
                    "perintahnya tofu. Sintaks HCL dan provider-nya hampir sama, jadi sebagian",
                    "besar konfigurasi Terraform bisa langsung dipakai. Fitur khasnya enkripsi",
                    "state bawaan sejak versi 1.7. Versi terbarunya saat materi ini ditulis",
                    "1.13.1 (1 Oktober 2026), dan dipakai 3,6 persen responden Survei Stack",
                    "Overflow 2026.",
                    "",
                    "Pilih OpenTofu kalau lisensi open source penting bagi organisasimu, atau",
                    "kalau butuh enkripsi state tanpa layanan berbayar. Konsep di tiga materi",
                    "Terraform tadi berlaku sama, tinggal ganti terraform dengan tofu.",
                ],
            },
            {
                "heading": "Pulumi dan AWS CDK: IaC dengan bahasa pemrograman",
                "body": [
                    "Pulumi menulis infrastruktur dengan Python, TypeScript, Go, C#, atau Java.",
                    "Perulangan, fungsi, dan tes unit jadi bisa dipakai langsung. CLI dan SDK-nya",
                    "berlisensi Apache-2.0, versi terbaru 3.270.0 (rilisnya hampir tiap minggu),",
                    "dipakai 2,0 persen responden survei yang sama.",
                ],
                "code": """import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("foto-toko", force_destroy=False)
aws.s3.BucketPublicAccessBlock("foto-toko-tertutup",
                               bucket=bucket.id,
                               block_public_acls=True,
                               block_public_policy=True)
pulumi.export("nama_bucket", bucket.bucket)""",
            },
            {
                "body": [
                    "AWS CloudFormation adalah IaC bawaan AWS: template YAML atau JSON menjadi",
                    "stack yang dibuat, diubah, dan dihapus bersama. Layanannya gratis, kamu cuma",
                    "membayar sumber dayanya. AWS CDK menulis infrastruktur dengan bahasa",
                    "pemrograman lalu mengubahnya jadi template CloudFormation; versinya 2.273.0",
                    "saat materi ini ditulis, dan CDK v1 sudah berhenti didukung sejak 2023.",
                    "Jangan tertukar dengan CDK for Terraform (CDKTF), yang repositorinya",
                    "diarsipkan 10 Desember 2025.",
                    "",
                    "Padanan di penyedia lain: Azure punya ARM template dan Bicep, Google Cloud",
                    "punya Infrastructure Manager yang berbasis Terraform sebagai pengganti",
                    "Deployment Manager.",
                    "",
                    "Packer, juga dari HashiCorp, membuat golden image: image mesin (AMI, image",
                    "VM) yang sudah berisi paket dan konfigurasi, sehingga server baru langsung",
                    "siap tanpa menunggu Ansible jalan. Versi terbarunya 1.16.1, berlisensi",
                    "BUSL-1.1.",
                ],
            },
            {
                "heading": "Generasi lama: Chef, Puppet, Salt",
                "body": [
                    "Sebelum Ansible populer, manajemen konfigurasi dikuasai alat berbasis agen:",
                    "program kecil berjalan di setiap server dan menarik konfigurasi dari server",
                    "pusat secara berkala. Ketiganya masih ditemui di perusahaan besar, tapi",
                    "proyek baru jarang memilihnya.",
                    "",
                    "  - Chef (Chef Infra): konfigurasi ditulis sebagai cookbook dan recipe dalam",
                    "    Ruby. Sekarang milik Progress. Chef Infra Client seri 19 beralih ke",
                    "    paket berbasis Habitat, dan biner resminya butuh lisensi komersial.",
                    "  - Puppet: deklaratif dengan bahasa Puppet sendiri. Setelah Perforce",
                    "    berhenti merilis biner open source, komunitas membuat fork bernama",
                    "    OpenVox. OpenVox 9.1.0 dirilis 13 Oktober 2026.",
                    "  - Salt (SaltStack): cepat karena memakai bus pesan antara master dan",
                    "    minion. Sekarang dimiliki Broadcom lewat VMware. Versi terbarunya 3008.3",
                    "    (September 2026).",
                    "",
                    "Kalau kamu ketemu salah satunya di tempat kerja, konsepnya sama dengan",
                    "Ansible: keadaan yang diinginkan, idempotensi, dan pemisahan data dari kode.",
                    "Yang berbeda bahasanya dan arah komunikasinya (agen menarik, bukan control",
                    "node mendorong).",
                ],
            },
            {
                "heading": "Kapan memilih yang mana",
                "body": [
                    "  - Infrastruktur di beberapa penyedia, atau ingin keterampilan yang paling",
                    "    banyak dicari: Terraform atau OpenTofu.",
                    "  - Tim yang lebih nyaman dengan Python atau TypeScript dan ingin menguji",
                    "    infrastruktur dengan tes unit: Pulumi, atau CDK kalau semuanya di AWS.",
                    "  - Semua di AWS dan ingin tanpa state yang diurus sendiri: CloudFormation,",
                    "    karena state-nya disimpan AWS sebagai stack.",
                    "  - Mengatur isi server: Ansible untuk proyek baru. Chef, Puppet, atau Salt",
                    "    kalau memang sudah terpasang dan berjalan.",
                    "  - Server yang harus siap dalam hitungan detik saat diskalakan: image dari",
                    "    Packer, supaya nggak menunggu konfigurasi jalan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di lowongan kerja, Terraform dan Ansible paling sering muncul.",
                    "CloudFormation dan CDK banyak dipakai tim yang sepenuhnya di AWS, dan Bicep",
                    "di tim Azure. Chef dan Puppet biasanya muncul di lowongan perusahaan lama",
                    "yang sedang bermigrasi.",
                    "",
                    "Kasus kecil: organisasimu ingin berhenti bergantung pada Terraform karena",
                    "lisensinya, dan kamu diminta mengecek apakah repositori infrastruktur yang",
                    "ada bisa pindah ke OpenTofu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang tofu, lalu jalankan tofu init dan tofu plan di salinan",
                    "     repositori, memakai state yang sama dalam mode baca.",
                    "  2. Pastikan plan berbunyi No changes. Kalau ada perbedaan, catat fitur",
                    "     Terraform mana yang belum didukung versi OpenTofu itu.",
                    "  3. Ganti hashicorp/setup-terraform dengan opentofu/setup-opentofu di",
                    "     workflow pull request.",
                    "  4. Pindahkan satu lingkungan kecil dulu, misalnya dev, dan pertimbangkan",
                    "     menyalakan enkripsi state sesudah migrasi berjalan stabil.",
                ],
            },
        ],
    },
    {
        "title": "36. Kubernetes: Arsitektur, Reconciliation, dan Klaster Lokal",
        "sections": [
            {
                "body": [
                    "Di bab Docker kamu menjalankan container dengan satu perintah di satu",
                    "mesin. Itu cukup untuk laptop atau satu server kecil. Masalahnya muncul",
                    "waktu aplikasinya tumbuh: sepuluh container tersebar di lima server.",
                    "Siapa yang menyalakan ulang container yang crash jam dua pagi? Siapa",
                    "yang memindahkan container kalau satu server mati? Siapa yang mengganti",
                    "versi lama ke versi baru satu per satu supaya pengguna nggak kena",
                    "downtime?",
                    "",
                    "Kalau dikerjakan manual, jawabannya kamu, lewat SSH, sambil ngantuk.",
                    "Kubernetes dibuat untuk mengambil alih pekerjaan itu. Ia disebut sistem",
                    "orkestrasi container: ia mengatur di mana container jalan, berapa",
                    "jumlahnya, dan apa yang harus dilakukan kalau ada yang rusak.",
                    "",
                    "Namanya dari bahasa Yunani yang artinya juru mudi. Sering disingkat k8s,",
                    "karena ada delapan huruf antara huruf k dan s. Kubernetes lahir di",
                    "Google, dibuka sebagai proyek open source tahun 2014, dan sekarang",
                    "dipelihara di bawah CNCF (Cloud Native Computing Foundation) dengan",
                    "lisensi Apache-2.0.",
                ],
            },
            {
                "heading": "Keadaan yang diinginkan",
                "body": [
                    "Cara kerja Kubernetes beda dengan skrip deploy biasa. Skrip biasa berisi",
                    "perintah: jalankan container ini, lalu itu, lalu buka port ini. Gaya ini",
                    "disebut imperatif. Di Kubernetes kamu menulis keadaan yang kamu mau,",
                    "misalnya \"aplikasi web, image toko-api:2.4.1, tiga replika\". Gaya ini",
                    "disebut deklaratif. Tulisan itu namanya spec.",
                    "",
                    "Sesudah spec dikirim, Kubernetes terus membandingkan keinginanmu dengan",
                    "kenyataan di klaster. Kalau cuma ada dua container yang hidup, ia",
                    "membuat satu lagi. Kalau ada empat, ia mematikan satu. Proses",
                    "membandingkan lalu membetulkan ini disebut reconciliation, dan bagian",
                    "yang mengerjakannya disebut controller.",
                    "",
                    "Gampangnya, mirip AC dengan termostat. Kamu cuma bilang \"24 derajat\". AC",
                    "mengukur suhu ruangan terus-menerus, lalu menyala atau berhenti sendiri",
                    "sampai suhunya pas. Kamu nggak pernah menyuruh \"nyalakan kompresor lima",
                    "menit\". Kalau pintu dibuka dan ruangan panas lagi, AC bekerja lagi tanpa",
                    "disuruh.",
                    "",
                    "Akibat pentingnya: kamu jarang menyuruh Kubernetes melakukan sesuatu",
                    "secara langsung. Kamu mengubah spec, lalu controller yang mencari cara",
                    "supaya kenyataan menyusul.",
                ],
            },
            {
                "heading": "Reconciliation loop versi mini",
                "code": """diinginkan = 3
pod = ["web-1", "web-2"]
nomor = 2
kejadian = {2: "web-1"}   # detik ke-2: pod web-1 mati

for detik in range(1, 5):
    if detik in kejadian:
        pod.remove(kejadian[detik])
        print(f"detik {detik}: {kejadian[detik]} mati")
    selisih = diinginkan - len(pod)
    if selisih > 0:
        for _ in range(selisih):
            nomor += 1
            pod.append(f"web-{nomor}")
        print(f"detik {detik}: kurang {selisih}, buat pod -> {pod}")
    else:
        print(f"detik {detik}: sesuai, {len(pod)} pod")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  detik 1: kurang 1, buat pod -> ['web-1', 'web-2', 'web-3']",
                    "  detik 2: web-1 mati",
                    "  detik 2: kurang 1, buat pod -> ['web-2', 'web-3', 'web-4']",
                    "  detik 3: sesuai, 3 pod",
                    "  detik 4: sesuai, 3 pod",
                    "",
                    "Program kecil ini meniru inti setiap controller. Ia nggak peduli kenapa",
                    "web-1 mati. Ia cuma melihat jumlah yang ada, membandingkan dengan jumlah",
                    "yang diminta, lalu bertindak. Controller sungguhan bekerja sama persis,",
                    "bedanya ia membaca keadaan dari API server dan bereaksi saat ada",
                    "perubahan, bukan tiap detik.",
                    "",
                    "Perhatikan juga pod pengganti diberi nama baru (web-4), bukan web-1",
                    "lagi. Di Kubernetes pun begitu: pod yang mati nggak dihidupkan kembali,",
                    "tapi diganti pod baru dengan nama dan alamat IP baru. Ini sebabnya",
                    "aplikasi di Kubernetes nggak boleh menyimpan data penting di dalam",
                    "container.",
                ],
            },
            {
                "heading": "Isi sebuah klaster",
                "body": [
                    "Klaster Kubernetes terdiri dari dua bagian: control plane (otaknya) dan",
                    "node (mesin pekerja). Node bisa server fisik, VM di cloud, atau",
                    "container di laptop.",
                    "",
                    "Komponen control plane:",
                    "",
                    "  - kube-apiserver: satu-satunya pintu masuk. Perintah kubectl,",
                    "    controller, dan node semuanya bicara lewat API server, nggak pernah",
                    "    langsung ke komponen lain.",
                    "  - etcd: database key-value tempat seluruh spec dan status klaster",
                    "    disimpan. Kehilangan etcd tanpa backup berarti kehilangan isi",
                    "    klaster.",
                    "  - kube-scheduler: memilih node untuk tiap pod baru berdasarkan sisa",
                    "    CPU dan memori serta aturan penempatan.",
                    "  - kube-controller-manager: tempat puluhan controller jalan, misalnya",
                    "    yang menjaga jumlah replika.",
                    "",
                    "Komponen di tiap node:",
                    "",
                    "  - kubelet: agen yang menerima daftar pod untuk node itu, lalu menyuruh",
                    "    container runtime menjalankannya dan melaporkan statusnya.",
                    "  - container runtime: yang menjalankan container sungguhan, biasanya",
                    "    containerd atau CRI-O, lewat antarmuka bernama CRI.",
                    "  - kube-proxy: mengatur aturan jaringan supaya alamat Service sampai ke",
                    "    pod yang tepat. Service dibahas dua materi lagi.",
                    "",
                    "Unit terkecil yang dijadwalkan Kubernetes bukan container tunggal.",
                    "Namanya pod: satu atau beberapa container yang selalu ditempatkan",
                    "bersama di satu node dan berbagi alamat IP. Kebanyakan pod cuma berisi",
                    "satu container.",
                ],
            },
            {
                "heading": "Mencoba di laptop: kind, minikube, k3s",
                "body": [
                    "Kamu nggak perlu akun cloud untuk belajar. Tiga alat ini membuat klaster",
                    "kecil di laptop. Angka versinya dari halaman rilis resmi masing-masing,",
                    "dicek saat materi ini ditulis (Oktober 2026).",
                    "",
                    "  Alat      Versi          Cara kerja                      Cocok untuk",
                    "  kind      v0.33.0        node berupa container           uji cepat, CI",
                    "  minikube  v1.39.0        satu node di VM/container       belajar fitur",
                    "  k3s       v1.37.1+k3s1   satu biner, Kubernetes ringan   edge, Raspberry Pi",
                    "",
                    "kind (Kubernetes in Docker) dipelihara komunitas Kubernetes dan dipakai",
                    "untuk menguji Kubernetes itu sendiri. Klasternya bisa dibuat dan dibuang",
                    "dalam semenit. Di Fedora yang memakai Podman, kind punya dukungan Podman",
                    "lewat provider tersendiri; cek dokumentasinya untuk batasannya.",
                    "",
                    "minikube adalah alat resmi proyek Kubernetes untuk klaster satu node. Ia",
                    "butuh sekitar 2 CPU dan 2 GB RAM bebas, dan punya banyak addon yang bisa",
                    "dinyalakan dengan satu perintah, misalnya dasbor dan metrics-server.",
                    "",
                    "k3s buatan Rancher (sekarang bagian dari SUSE) dan termasuk proyek CNCF.",
                    "Semuanya dibungkus jadi satu biner kecil. Untuk satu node, ia memakai",
                    "SQLite sebagai pengganti etcd. k3s sering dipakai di server murah dan",
                    "perangkat edge, jadi kegunaannya lebih luas daripada sekadar belajar.",
                ],
            },
            {
                "heading": "Perintah pertama",
                "bahasa": "terminal",
                "code": """# kind: buat klaster bernama belajar (butuh Docker atau Podman)
kind create cluster --name belajar

# lihat node dan komponen sistem
kubectl get nodes
kubectl get pods -n kube-system
kubectl cluster-info

# buang klasternya kalau sudah selesai
kind delete cluster --name belajar

# alternatif: minikube
minikube start
minikube addons enable metrics-server""",
            },
            {
                "heading": "Versi dan kapan belum perlu Kubernetes",
                "body": [
                    "Saat materi ini ditulis (Oktober 2026), rilis terbaru Kubernetes adalah",
                    "1.37.1 (15 September 2026). Proyeknya merilis versi minor baru kira-kira",
                    "tiap empat bulan dan merawat tiga cabang sekaligus, sekarang 1.37, 1.36,",
                    "dan 1.35. Tiap cabang dapat perbaikan sekitar satu tahun. Artinya",
                    "klaster yang nggak pernah di-upgrade akan keluar dari masa dukungan",
                    "dalam setahun.",
                    "",
                    "Kubernetes dipakai luas. Survei Stack Overflow 2026 mencatat 26,0%",
                    "responden kategori cloud development memakainya, dan survei tahunan CNCF",
                    "2025 menyebut 82% pengguna container menjalankan Kubernetes di produksi.",
                    "",
                    "Jebakan: belajar Kubernetes sebelum nyaman dengan Linux, jaringan, dan",
                    "Docker. Hampir semua error di Kubernetes ujungnya soal port, DNS, izin",
                    "berkas, atau image yang salah. Kalau dasarnya belum kuat, pesan errornya",
                    "terasa acak.",
                    "",
                    "Kubernetes juga punya ongkos: control plane harus dirawat dan",
                    "di-upgrade, dan konsepnya banyak. Satu aplikasi dengan satu database",
                    "biasanya cukup pakai Docker Compose atau platform seperti Cloud Run.",
                    "Kubernetes mulai masuk akal kalau layanannya banyak, timnya lebih dari",
                    "satu, dan butuh deploy berkali-kali sehari tanpa downtime.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang sedang tumbuh biasanya punya beberapa layanan terpisah:",
                    "API daftar produk, keranjang, pembayaran, dan pekerja latar yang",
                    "mengirim email. Tim seperti ini sering memindahkan layanannya dari",
                    "beberapa VM yang diurus manual ke satu klaster Kubernetes terkelola.",
                    "Tujuannya supaya container yang crash diganti otomatis dan server yang",
                    "mati nggak perlu ditangani malam itu juga.",
                    "",
                    "Kasus kecil: kamu baru membuat klaster kind dan menjalankan kubectl get",
                    "nodes, tapi node-nya berstatus NotReady selama beberapa menit.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tunggu satu atau dua menit dulu. Node baru menunggu komponen",
                    "     jaringannya siap, dan status NotReady di awal itu wajar.",
                    "  2. Kalau masih NotReady, lihat pod sistemnya dengan kubectl get pods",
                    "     -n kube-system dan cari yang statusnya bukan Running.",
                    "  3. Baca rinciannya dengan kubectl describe node lalu perhatikan bagian",
                    "     Conditions dan Events di bawah.",
                    "  4. Kalau penyebabnya laptop kehabisan memori atau disk, tutup aplikasi",
                    "     lain atau buang klaster lama dengan kind delete cluster, lalu buat",
                    "     ulang.",
                ],
            },
        ],
    },
    {
        "title": "37. Pod, Deployment, dan Strategi Rilis",
        "sections": [
            {
                "body": [
                    "Pod adalah unit terkecil di Kubernetes: satu atau beberapa container",
                    "yang selalu jalan bersama di node yang sama. Container dalam satu pod",
                    "berbagi alamat IP (mereka bisa saling memanggil lewat localhost) dan",
                    "bisa berbagi volume. Pola yang umum: satu container aplikasi, kadang",
                    "ditemani container kecil pembantu, misalnya pengirim log. Container",
                    "pembantu ini disebut sidecar.",
                    "",
                    "Pod itu sementara. Kalau node-nya mati, pod ikut hilang dan nggak",
                    "dipindahkan. Karena itu di produksi kamu hampir nggak pernah membuat pod",
                    "langsung. Kamu membuat objek yang mengurus pod untukmu, dan yang paling",
                    "sering dipakai untuk aplikasi tanpa data lokal adalah Deployment.",
                ],
            },
            {
                "heading": "Deployment, ReplicaSet, dan Pod",
                "body": [
                    "Hubungan ketiganya bertingkat. Deployment menyimpan keinginanmu: image",
                    "apa, berapa replika, bagaimana cara mengganti versi. Deployment membuat",
                    "ReplicaSet, controller yang tugasnya cuma satu: menjaga jumlah pod",
                    "dengan template tertentu tetap sesuai angka replika. ReplicaSet lalu",
                    "membuat pod.",
                    "",
                    "Tiap kali image atau isi template berubah, Deployment membuat ReplicaSet",
                    "baru dan pelan-pelan memindahkan replika dari ReplicaSet lama ke yang",
                    "baru. ReplicaSet lama disimpan dengan nol replika supaya bisa dipakai",
                    "untuk rollback. Bawaannya, sepuluh ReplicaSet lama disimpan (diatur",
                    "lewat revisionHistoryLimit).",
                    "",
                    "Cara Deployment tahu pod mana miliknya adalah lewat label, yaitu",
                    "pasangan kunci dan nilai yang ditempel di objek, misalnya app: web.",
                    "Bagian selector di Deployment harus cocok dengan label di template pod.",
                    "Kalau nggak cocok, kubectl menolak manifestnya.",
                ],
            },
            {
                "heading": "Manifest Deployment",
                "bahasa": "yaml",
                "code": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web            # harus sama dengan label template
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1         # boleh kelebihan 1 pod saat ganti versi
      maxUnavailable: 0   # jangan pernah kurang dari 3 yang siap
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: toko-api:2.4.1
          ports:
            - containerPort: 8080""",
            },
            {
                "heading": "Perintah sehari-hari",
                "bahasa": "terminal",
                "code": """kubectl apply -f deployment.yaml
kubectl get deployment,replicaset,pods -l app=web

# ganti versi image, lalu ikuti prosesnya
kubectl set image deployment/web web=toko-api:2.5.0
kubectl rollout status deployment/web

# riwayat dan rollback
kubectl rollout history deployment/web
kubectl rollout undo deployment/web

# ubah jumlah replika
kubectl scale deployment/web --replicas=5""",
            },
            {
                "heading": "Rolling update",
                "body": [
                    "Strategi bawaan Deployment adalah RollingUpdate: pod versi baru dibuat",
                    "sedikit demi sedikit, dan pod versi lama dimatikan setelah pengganti",
                    "siap. Dua angka yang mengaturnya:",
                    "",
                    "  - maxSurge: berapa pod boleh ada di atas jumlah replika selama proses.",
                    "    Bawaannya 25%.",
                    "  - maxUnavailable: berapa pod boleh nggak siap selama proses. Bawaannya",
                    "    juga 25%.",
                    "",
                    "Dengan manifest di atas (maxSurge 1, maxUnavailable 0, tiga replika),",
                    "urutannya: buat satu pod v2, tunggu sampai siap, matikan satu pod v1,",
                    "ulangi sampai semua v2. Selama proses selalu ada minimal tiga pod siap",
                    "melayani. Ongkosnya, kamu butuh ruang untuk satu pod ekstra.",
                    "",
                    "Strategi kedua adalah Recreate: semua pod lama dimatikan dulu, baru pod",
                    "baru dibuat. Ada jeda downtime, tapi kadang memang perlu, misalnya kalau",
                    "dua versi aplikasi nggak boleh jalan bersamaan karena memakai skema",
                    "database yang berbeda.",
                    "",
                    "Kata \"siap\" di sini punya arti teknis. Kubernetes menganggap pod siap",
                    "kalau readiness probe-nya lulus. Tanpa readiness probe, pod dianggap",
                    "siap begitu containernya jalan, padahal aplikasinya mungkin masih memuat",
                    "konfigurasi. Probe dibahas di materi ConfigMap, Secret, Probe, dan Batas",
                    "Resource di bab ini.",
                ],
            },
            {
                "heading": "Blue-green dan canary",
                "body": [
                    "Deployment cuma mengenal dua strategi di atas. Dua strategi rilis lain",
                    "yang sering kamu dengar dibangun di atasnya.",
                    "",
                    "Blue-green: kamu menjalankan dua Deployment lengkap, misalnya web-blue",
                    "(versi lama) dan web-green (versi baru). Pengguna diarahkan ke blue",
                    "lewat Service. Setelah green dicek, selector Service dipindah ke green",
                    "dalam satu langkah. Kalau ada masalah, pindahkan balik. Ongkosnya,",
                    "kapasitas dua kali lipat selama masa peralihan.",
                    "",
                    "Canary: versi baru diberi sebagian kecil lalu lintas dulu, misalnya 10%,",
                    "sambil angka error-nya diawasi. Kalau aman, porsinya dinaikkan. Cara",
                    "paling kasar adalah mengatur jumlah replika (9 pod lama, 1 pod baru).",
                    "Cara yang lebih tepat memakai pembagian bobot di Gateway API atau",
                    "service mesh, yang dibahas di materi berikutnya. Untuk mengotomatiskan",
                    "canary, banyak tim memakai Argo Rollouts atau Flagger, yang menaikkan",
                    "porsi sendiri berdasarkan metrik.",
                    "",
                    "  Strategi        Downtime  Butuh kapasitas ekstra  Rollback",
                    "  Recreate        ada       nggak                   deploy ulang versi lama",
                    "  RollingUpdate   nggak     sedikit (maxSurge)      kubectl rollout undo",
                    "  Blue-green      nggak     dua kali lipat          pindah selector",
                    "  Canary          nggak     sedikit                 kembalikan bobot ke 0%",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: memakai tag latest. Kalau image-nya selalu toko-api:latest,",
                    "template Deployment nggak berubah saat kamu mendorong versi baru, jadi",
                    "Kubernetes nggak melakukan rolling update apa pun. Riwayat rollout juga",
                    "jadi nggak berguna karena semua revisi menunjuk tag yang sama. Pakai tag",
                    "versi atau digest.",
                    "",
                    "Mengedit pod langsung juga percuma. Pod milik Deployment akan",
                    "dikembalikan ke template begitu ia diganti. Perubahan selalu masuk lewat",
                    "manifest Deployment.",
                    "",
                    "Rollback dengan kubectl rollout undo cuma mengembalikan template pod. Ia",
                    "nggak mengembalikan database. Kalau versi baru sudah mengubah skema",
                    "tabel, versi lama mungkin tetap error setelah rollback.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan web yang dipakai terus-menerus, seperti aplikasi ojek online",
                    "atau dompet digital, nggak bisa menunggu jam sepi untuk deploy. Rolling",
                    "update dengan readiness probe membuat tim bisa merilis versi baru di",
                    "siang hari sambil pengguna tetap bertransaksi.",
                    "",
                    "Kasus kecil: setelah kubectl set image ke versi 2.5.0, kubectl rollout",
                    "status berhenti di \"1 out of 3 new replicas have been updated\" dan pod",
                    "barunya berstatus CrashLoopBackOff.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Lihat penyebabnya dengan kubectl logs pada pod baru dan kubectl",
                    "     describe pod untuk membaca bagian Events.",
                    "  2. Karena maxUnavailable 0, dua pod lama masih melayani pengguna, jadi",
                    "     kamu punya waktu. Kembalikan dulu dengan kubectl rollout undo",
                    "     deployment/web.",
                    "  3. Cek dengan kubectl rollout status deployment/web sampai muncul",
                    "     successfully rolled out.",
                    "  4. Perbaiki penyebabnya, misalnya variabel lingkungan yang lupa",
                    "     ditambahkan, lalu rilis ulang dengan tag versi baru seperti 2.5.1.",
                ],
            },
        ],
    },
    {
        "title": "38. Service, Ingress, dan Gateway API",
        "sections": [
            {
                "body": [
                    "Pod datang dan pergi, dan tiap pod baru mendapat alamat IP baru. Kalau",
                    "layanan keranjang memanggil layanan produk lewat IP pod, alamat itu basi",
                    "begitu pod produk diganti. Kubernetes menyelesaikannya dengan Service:",
                    "satu nama dan satu alamat tetap yang meneruskan permintaan ke pod mana",
                    "pun yang sedang hidup dan cocok labelnya.",
                    "",
                    "Di bab Jaringan dan Web Server kamu sudah kenal reverse proxy dan load",
                    "balancer. Service adalah load balancer kecil di dalam klaster, dan",
                    "Gateway API adalah reverse proxy di pintu depannya.",
                ],
            },
            {
                "heading": "Service",
                "bahasa": "yaml",
                "code": """apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: ClusterIP
  selector:
    app: web          # pod berlabel app=web jadi tujuan
  ports:
    - port: 80        # port milik Service
      targetPort: 8080  # port container di pod""",
            },
            {
                "body": [
                    "Service di atas mendapat alamat IP virtual dan nama DNS di dalam",
                    "klaster: web, atau lengkapnya web.default.svc.cluster.local (default",
                    "adalah nama namespace-nya). Pod lain cukup memanggil http://web. Daftar",
                    "pod tujuannya disimpan Kubernetes di objek EndpointSlice dan diperbarui",
                    "otomatis setiap ada pod yang siap atau berhenti.",
                    "",
                    "Yang mengubah alamat virtual itu jadi alamat pod sungguhan adalah",
                    "kube-proxy di tiap node, dengan memasang aturan iptables, IPVS, atau",
                    "nftables di kernel. Pod yang readiness probe-nya gagal dikeluarkan dari",
                    "daftar, jadi ia nggak menerima permintaan.",
                    "",
                    "Ada empat jenis Service:",
                    "",
                    "  - ClusterIP (bawaan): cuma bisa diakses dari dalam klaster. Dipakai",
                    "    untuk komunikasi antarlayanan.",
                    "  - NodePort: membuka port yang sama di setiap node, dari rentang 30000",
                    "    sampai 32767. Berguna untuk percobaan, jarang dipakai langsung di",
                    "    produksi.",
                    "  - LoadBalancer: meminta load balancer dari penyedia cloud. Praktis,",
                    "    tapi tiap Service jenis ini biasanya berarti satu load balancer yang",
                    "    ditagih terpisah.",
                    "  - ExternalName: alias DNS ke nama di luar klaster, misalnya database",
                    "    terkelola.",
                    "",
                    "Jebakan: port dan targetPort tertukar. port adalah yang dipanggil klien,",
                    "targetPort adalah yang didengarkan aplikasi di container. Kalau",
                    "targetPort salah, Service-nya ada, DNS-nya jalan, tapi permintaan",
                    "berakhir dengan connection refused.",
                ],
            },
            {
                "heading": "Ingress dan pensiunnya Ingress NGINX",
                "body": [
                    "Untuk lalu lintas HTTP dari internet, membuat satu LoadBalancer per",
                    "layanan itu boros. Solusi lamanya adalah Ingress: satu pintu yang",
                    "membagi permintaan berdasarkan host dan path, misalnya",
                    "toko.contoh.id/api ke Service api dan sisanya ke Service web. Objek",
                    "Ingress sendiri cuma aturan. Yang mengerjakannya adalah Ingress",
                    "controller yang harus kamu pasang.",
                    "",
                    "Controller paling populer selama bertahun-tahun adalah ingress-nginx",
                    "milik komunitas Kubernetes. Pada November 2025 blog resmi Kubernetes",
                    "mengumumkan pensiunnya: perawatan seadanya sampai Maret 2026, setelah",
                    "itu nggak ada rilis, perbaikan bug, atau perbaikan keamanan lagi.",
                    "Pemasangan yang sudah ada tetap jalan, tapi makin lama makin rawan.",
                    "Untuk migrasi, proyek Kubernetes merilis alat ingress2gateway 1.0 pada",
                    "Maret 2026.",
                    "",
                    "Jangan tertukar dengan Nginx Ingress Controller milik F5. Itu produk",
                    "lain dengan nama mirip dan masih dirawat. Tutorial lama yang menyuruh",
                    "\"pasang ingress-nginx\" sekarang perlu dibaca dengan hati-hati.",
                    "",
                    "API Ingress sendiri masih ada dan stabil, tapi dibekukan: fitur baru",
                    "masuk ke Gateway API.",
                ],
            },
            {
                "heading": "Gateway API",
                "body": [
                    "Gateway API adalah pengganti Ingress yang lebih lengkap. Ia memecah",
                    "tanggung jawab jadi tiga objek, sesuai siapa yang biasanya mengurusnya:",
                    "",
                    "  - GatewayClass: jenis implementasi, dipasang penyedia infrastruktur.",
                    "    Contohnya Envoy Gateway, Istio, Cilium, Nginx Gateway Fabric, dan",
                    "    Traefik.",
                    "  - Gateway: pintu masuk dengan listener (port, protokol, sertifikat",
                    "    TLS), diurus tim platform.",
                    "  - HTTPRoute: aturan rute milik tim aplikasi, misalnya path /api ke",
                    "    Service api.",
                    "",
                    "Pemisahan ini berguna di klaster bersama. Tim aplikasi bisa mengubah",
                    "rutenya sendiri tanpa menyentuh sertifikat atau port milik tim platform.",
                    "Gateway API juga punya fitur yang dulu cuma bisa lewat anotasi khusus",
                    "tiap controller, misalnya pembagian bobot untuk canary dan pencocokan",
                    "header. Saat materi ini ditulis, rilis stabil terbarunya ada di seri",
                    "1.6.",
                ],
            },
            {
                "heading": "Gateway dan HTTPRoute dengan canary 90/10",
                "bahasa": "yaml",
                "code": """apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: pintu-depan
spec:
  gatewayClassName: eg        # nama GatewayClass yang terpasang
  listeners:
    - name: http
      protocol: HTTP
      port: 80
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: toko
spec:
  parentRefs:
    - name: pintu-depan
  hostnames:
    - toko.contoh.id
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: web-v1
          port: 80
          weight: 90
        - name: web-v2
          port: 80
          weight: 10""",
            },
            {
                "heading": "Memeriksa dari terminal",
                "bahasa": "terminal",
                "code": """kubectl get service,endpointslice -l app=web

# coba panggil dari laptop tanpa membuka port ke internet
kubectl port-forward service/web 8080:80
curl -s localhost:8080/healthz

# status Gateway dan rute
kubectl get gateway,httproute
kubectl describe httproute toko""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak klaster dibangun di masa ketika ingress-nginx jadi pilihan",
                    "standar, jadi pensiunnya menyentuh banyak tim sekaligus. Sepanjang 2026,",
                    "pekerjaan rutin tim platform di banyak perusahaan adalah memindahkan",
                    "aturan Ingress ke Gateway dan HTTPRoute sambil memastikan nggak ada rute",
                    "yang hilang.",
                    "",
                    "Kasus kecil: setelah membuat Service web, permintaan dari pod lain ke",
                    "http://web terus timeout, padahal pod web berstatus Running.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek apakah Service punya tujuan dengan kubectl get endpointslice -l",
                    "     kubernetes.io/service-name=web. Kalau daftar alamatnya kosong,",
                    "     selector nggak cocok dengan label pod.",
                    "  2. Bandingkan label pod (kubectl get pods --show-labels) dengan bagian",
                    "     selector di Service. Huruf besar kecil dan ejaan harus persis sama.",
                    "  3. Kalau alamatnya ada, cek apakah pod-nya siap (kolom Ready",
                    "     menunjukkan 1/1). Pod yang belum siap nggak dimasukkan ke daftar",
                    "     tujuan.",
                    "  4. Terakhir, cocokkan targetPort dengan port yang memang didengarkan",
                    "     aplikasi di dalam container.",
                ],
            },
        ],
    },
    {
        "title": "39. ConfigMap, Secret, Probe, dan Batas Resource",
        "sections": [
            {
                "body": [
                    "Image container sebaiknya sama persis di semua lingkungan: image yang",
                    "lolos tes di staging adalah image yang naik ke produksi. Yang berbeda",
                    "cuma konfigurasinya, misalnya alamat database dan tingkat log. Prinsip",
                    "ini datang dari 12-Factor yang kamu temui di bab pertama: konfigurasi",
                    "disimpan di lingkungan, bukan di dalam kode.",
                    "",
                    "Materi ini membahas empat hal yang membuat pod siap produksi: tempat",
                    "konfigurasi (ConfigMap), tempat rahasia (Secret), cara Kubernetes tahu",
                    "aplikasimu sehat (probe), dan batas CPU serta memori (requests dan",
                    "limits).",
                ],
            },
            {
                "heading": "ConfigMap dan Secret",
                "bahasa": "yaml",
                "code": """apiVersion: v1
kind: ConfigMap
metadata:
  name: web-config
data:
  LOG_LEVEL: info
  DB_HOST: db.toko.svc.cluster.local
---
apiVersion: v1
kind: Secret
metadata:
  name: web-rahasia
type: Opaque
stringData:              # ditulis polos, disimpan sebagai base64
  DB_PASSWORD: s3cr3t-toko
---
# potongan template pod di Deployment
containers:
  - name: web
    image: toko-api:2.4.1
    envFrom:
      - configMapRef:
          name: web-config
      - secretRef:
          name: web-rahasia""",
            },
            {
                "body": [
                    "ConfigMap menyimpan konfigurasi biasa sebagai pasangan kunci dan nilai.",
                    "Isinya bisa dimasukkan ke container sebagai variabel lingkungan (seperti",
                    "di atas) atau sebagai berkas di dalam volume. Bedanya penting: variabel",
                    "lingkungan cuma dibaca saat container start, sedangkan berkas dari",
                    "volume diperbarui Kubernetes beberapa saat setelah ConfigMap berubah.",
                    "Mengubah ConfigMap yang dipakai lewat envFrom nggak berpengaruh sampai",
                    "pod-nya diganti.",
                    "",
                    "Secret bentuknya mirip, khusus untuk data rahasia. Nama \"Secret\" sering",
                    "bikin orang mengira isinya terenkripsi. Ternyata nggak: nilainya cuma",
                    "dikodekan base64, dan base64 bisa dibalik siapa pun tanpa kunci.",
                ],
            },
            {
                "heading": "Base64 bukan enkripsi",
                "code": """import base64

# seperti yang terlihat di kubectl get secret web-rahasia -o yaml
data = {"DB_PASSWORD": base64.b64encode(b"s3cr3t-toko").decode()}

for kunci, nilai in data.items():
    print(kunci, "tersimpan sebagai", nilai)
    print(kunci, "dibaca balik      ", base64.b64decode(nilai).decode())""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  DB_PASSWORD tersimpan sebagai czNjcjN0LXRva28=",
                    "  DB_PASSWORD dibaca balik       s3cr3t-toko",
                    "",
                    "Jadi pengaman Secret ada di tempat lain. Pertama, RBAC yang membatasi",
                    "siapa boleh membaca Secret. Kedua, enkripsi etcd yang harus dinyalakan",
                    "(di klaster terkelola biasanya sudah aktif atau tinggal dinyalakan).",
                    "Ketiga, kebiasaan nggak pernah menaruh manifest Secret berisi nilai asli",
                    "di Git. Alat seperti External Secrets Operator dan Sealed Secrets",
                    "dibahas di kurikulum Keamanan Siber.",
                ],
            },
            {
                "heading": "Liveness, readiness, dan startup probe",
                "body": [
                    "Probe adalah pemeriksaan kesehatan yang dijalankan kubelet secara",
                    "berkala, lewat permintaan HTTP, koneksi TCP, atau perintah di dalam",
                    "container. Ada tiga jenis, dan akibat gagalnya berbeda:",
                    "",
                    "  - liveness: \"apakah aplikasi macet?\" Kalau gagal beberapa kali",
                    "    berturut-turut, container di-restart.",
                    "  - readiness: \"apakah aplikasi siap menerima permintaan?\" Kalau gagal,",
                    "    pod dikeluarkan dari daftar tujuan Service sampai lulus lagi.",
                    "    Container nggak di-restart.",
                    "  - startup: \"apakah aplikasi sudah selesai menyala?\" Selama startup",
                    "    probe belum lulus, dua probe lain ditunda. Cocok untuk aplikasi yang",
                    "    butuh waktu lama untuk start, misalnya aplikasi Java besar.",
                    "",
                    "Jebakan: liveness probe yang ikut mengecek database. Begitu database",
                    "lambat sebentar, semua pod gagal liveness, semua di-restart bersamaan,",
                    "dan gangguan kecil berubah jadi layanan mati total. Liveness cukup",
                    "menjawab apakah proses ini masih hidup. Ketergantungan ke luar, kalau",
                    "perlu, masuk ke readiness.",
                ],
            },
            {
                "heading": "Probe dan resource di template pod",
                "bahasa": "yaml",
                "code": """containers:
  - name: web
    image: toko-api:2.4.1
    startupProbe:
      httpGet: {path: /healthz, port: 8080}
      failureThreshold: 30     # beri waktu 30 x 2 detik untuk start
      periodSeconds: 2
    livenessProbe:
      httpGet: {path: /healthz, port: 8080}
      periodSeconds: 10
    readinessProbe:
      httpGet: {path: /ready, port: 8080}
      periodSeconds: 5
    resources:
      requests:
        cpu: 250m              # seperempat core, dipakai scheduler
        memory: 256Mi
      limits:
        memory: 512Mi          # lewat dari ini: OOMKilled""",
            },
            {
                "heading": "Requests dan limits",
                "body": [
                    "requests adalah jatah yang dipesan. Scheduler memakai angka ini untuk",
                    "memilih node: pod dengan request 250m CPU cuma ditaruh di node yang sisa",
                    "jatahnya masih cukup. Satuan CPU memakai milicore, jadi 1000m sama",
                    "dengan satu core. Memori memakai Mi (mebibyte) atau Gi.",
                    "",
                    "limits adalah batas atas saat pod berjalan. Akibat melewatinya beda",
                    "untuk CPU dan memori. CPU yang melewati limit diperlambat (throttling),",
                    "prosesnya tetap hidup. Memori yang melewati limit membuat container",
                    "dibunuh kernel, dan statusnya tercatat OOMKilled.",
                    "",
                    "Dari kombinasi keduanya, Kubernetes memberi tiap pod kelas QoS. Ada",
                    "tiga: Guaranteed (requests sama dengan limits untuk CPU dan memori),",
                    "Burstable (ada requests, limits lebih besar atau kosong), dan BestEffort",
                    "(keduanya kosong). Saat node kehabisan memori, pod BestEffort yang",
                    "pertama diusir.",
                    "",
                    "Ingat: pod tanpa requests dianggap butuh nol. Scheduler bisa menumpuk",
                    "banyak pod seperti itu di satu node sampai node-nya kewalahan. Banyak",
                    "tim sengaja nggak memasang limit CPU supaya aplikasi nggak di-throttle,",
                    "tapi tetap memasang request CPU dan limit memori.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Java atau Node.js yang memorinya pelan-pelan naik adalah",
                    "penyebab klasik pod yang restart tiap beberapa jam. Tanpa limit memori,",
                    "satu pod seperti itu bisa menghabiskan memori node dan ikut menjatuhkan",
                    "pod lain di node yang sama. Dengan limit, yang mati cuma pod itu, lalu",
                    "diganti.",
                    "",
                    "Kasus kecil: angka di kolom Restarts pada kubectl get pods untuk pod web",
                    "terus naik, dan kamu curiga kehabisan memori.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jalankan kubectl describe pod lalu cari bagian Last State. Kalau",
                    "     tertulis Reason: OOMKilled, container dibunuh karena melewati limit",
                    "     memori.",
                    "  2. Lihat pemakaian nyatanya dengan kubectl top pod (butuh",
                    "     metrics-server) dan bandingkan dengan limit 512Mi.",
                    "  3. Kalau pemakaian normalnya memang dekat limit, naikkan request dan",
                    "     limit memori, misalnya ke 512Mi dan 768Mi.",
                    "  4. Kalau grafik pemakaiannya terus naik tanpa turun, itu tanda",
                    "     kebocoran memori di aplikasi. Menaikkan limit cuma menunda restart;",
                    "     perbaikannya ada di kode.",
                ],
            },
        ],
    },
    {
        "title": "40. Peta Orkestrasi: EKS, ECS, OpenShift, Nomad, Service Mesh",
        "sections": [
            {
                "body": [
                    "Menjalankan Kubernetes sendiri berarti merawat control plane: upgrade",
                    "tiap beberapa bulan, backup etcd, sertifikat, dan pemantauan. Banyak tim",
                    "memilih menyerahkan pekerjaan itu ke pihak lain, atau memakai",
                    "orkestrator yang lebih sederhana. Materi ini memetakan pilihannya,",
                    "ditambah service mesh, lapisan yang sering dipasang di atas Kubernetes",
                    "saat layanannya sudah banyak.",
                    "",
                    "  Pilihan          Jenis                   Lisensi           Status",
                    "  EKS, GKE, AKS    Kubernetes terkelola    layanan berbayar  aktif",
                    "  ECS, Fargate     orkestrator milik AWS   layanan berbayar  aktif",
                    "  OpenShift, OKD   Kubernetes perusahaan   langganan/Apache  aktif",
                    "  Rancher          manajer banyak klaster  Apache-2.0        aktif",
                    "  Nomad            penjadwal serbaguna     BUSL-1.1          stabil-matang",
                    "  Docker Swarm     mode orkestrasi Docker  Apache-2.0        menurun",
                    "  Istio, Linkerd   service mesh            Apache-2.0        aktif",
                    "  Envoy            proxy L4/L7             Apache-2.0        aktif",
                    "  Consul           discovery, KV, mesh     BUSL-1.1          stabil-matang",
                ],
            },
            {
                "heading": "Kubernetes terkelola: EKS, GKE, AKS",
                "body": [
                    "Amazon EKS, Google GKE, dan Azure AKS menjalankan control plane untukmu.",
                    "Kamu tetap memakai kubectl dan manifest yang sama, tapi upgrade etcd dan",
                    "API server diurus penyedia. Ini cara paling umum menjalankan Kubernetes",
                    "di produksi. Versi Kubernetes di layanan ini mengikuti versi upstream",
                    "dengan jeda beberapa minggu sampai bulan.",
                    "",
                    "Node pun bisa ikut diserahkan. GKE Autopilot dan EKS Auto Mode memilih,",
                    "menambah, dan memperbarui node sendiri; kamu cukup menulis pod beserta",
                    "requests-nya.",
                    "",
                    "Jebakan: yang ditagih lebih dari node. EKS menagih biaya per jam untuk",
                    "tiap klaster. Service jenis LoadBalancer membuat load balancer cloud",
                    "sungguhan, dan node di subnet privat butuh NAT gateway yang ditagih per",
                    "jam dan per GB. Klaster latihan yang lupa dimatikan selama sebulan bisa",
                    "menghasilkan tagihan yang mengejutkan. Bab terakhir membahas cara",
                    "mengawasinya.",
                ],
            },
            {
                "heading": "Amazon ECS dan AWS Fargate",
                "body": [
                    "ECS (Elastic Container Service) adalah orkestrator container buatan AWS",
                    "sendiri, lebih sederhana daripada Kubernetes. Konsepnya: task definition",
                    "(mirip spec pod) dan service (menjaga jumlah task, mirip Deployment).",
                    "Fargate adalah cara menjalankan task tanpa mengurus server sama sekali:",
                    "kamu memesan CPU dan memori per task, AWS yang menyediakan mesinnya.",
                    "Fargate juga bisa dipakai untuk pod EKS.",
                    "",
                    "ECS cocok kalau semua infrastrukturmu memang di AWS dan timnya kecil.",
                    "Padanannya di cloud lain adalah Google Cloud Run dan Azure Container",
                    "Apps. Hati-hati dengan nama: Alibaba Cloud memakai singkatan ECS untuk",
                    "layanan VM-nya, artinya beda sama sekali.",
                ],
            },
            {
                "heading": "OpenShift dan Rancher",
                "body": [
                    "Red Hat OpenShift adalah Kubernetes versi perusahaan: sudah termasuk",
                    "registry, pipeline, konsol web, dan aturan keamanan bawaan yang ketat.",
                    "Versi minor terbarunya saat materi ini ditulis adalah 4.22 (rilis umum",
                    "Juni 2026). Produk utamanya berlangganan, sedangkan versi komunitasnya",
                    "berlisensi Apache-2.0. OpenShift banyak dipakai bank, telko, dan",
                    "instansi yang butuh dukungan vendor.",
                    "",
                    "Jebakan khas OpenShift: container dijalankan dengan UID acak yang bukan",
                    "root. Image yang menuntut root atau menulis ke folder milik root gagal",
                    "jalan di sana, padahal lancar di Docker.",
                    "",
                    "Rancher (buatan SUSE, versi terbaru v2.15.2) adalah antarmuka web untuk",
                    "mengelola banyak klaster sekaligus, termasuk klaster EKS, GKE, AKS, dan",
                    "k3s, dari satu tempat. Jangan tertukar dengan Rancher Desktop, aplikasi",
                    "desktop untuk menjalankan container dan Kubernetes di laptop.",
                ],
            },
            {
                "heading": "Nomad dan Docker Swarm",
                "body": [
                    "HashiCorp Nomad adalah penjadwal beban kerja yang lebih sederhana dari",
                    "Kubernetes. Ia bisa menjalankan container, biner biasa, sampai VM,",
                    "dengan satu biner dan konsep yang lebih sedikit. Saat materi ini",
                    "ditulis, Nomad ada di seri 2.x. Sejak Agustus 2023 produk HashiCorp",
                    "memakai lisensi BUSL-1.1, yang menurut OSI bukan lisensi open source,",
                    "dan HashiCorp sendiri sudah diakuisisi IBM (selesai Februari 2025).",
                    "Nomad masih dirilis, tapi pangsanya kecil dibanding Kubernetes.",
                    "",
                    "Docker Swarm, tepatnya swarm mode di dalam Docker Engine, menjalankan",
                    "layanan di beberapa mesin dengan perintah yang mirip Docker Compose. Ia",
                    "masih dipelihara sebagai bagian Docker Engine, tapi ekosistem dan",
                    "lowongan kerja sudah pindah ke Kubernetes. Kamu mungkin menemuinya di",
                    "sistem lama; untuk proyek baru jarang dipilih.",
                ],
            },
            {
                "heading": "Service mesh: Istio, Linkerd, Envoy, Consul",
                "body": [
                    "Begitu layanannya puluhan, muncul kebutuhan yang berulang di semua",
                    "layanan: enkripsi antarlayanan, retry otomatis, pembagian lalu lintas",
                    "untuk canary, dan metrik tiap panggilan. Service mesh memindahkan semua",
                    "itu dari kode aplikasi ke lapisan jaringan. Caranya klasik dengan",
                    "sidecar, yaitu proxy kecil di setiap pod yang mencegat semua lalu",
                    "lintas. Cara yang lebih baru tanpa sidecar: proxy per node.",
                    "",
                    "  - Istio: mesh paling lengkap, proyek CNCF graduated, versi 1.31.2 (16",
                    "    Oktober 2026). Mode ambient tanpa sidecar sudah stabil sejak 2024.",
                    "  - Linkerd: lebih ringan dan lebih sederhana. Sejak Februari 2024",
                    "    proyek open source-nya cuma merilis versi edge (terbaru",
                    "    edge-26.10.1); rilis stabil seperti 2.20 (diumumkan Juni 2026)",
                    "    disediakan vendor, terutama Buoyant.",
                    "  - Envoy: proxy L4/L7 yang jadi dasar Istio, banyak implementasi",
                    "    Gateway API, dan load balancer cloud. Versi v1.40.0 (13 Oktober",
                    "    2026). Konfigurasinya biasanya dikirim otomatis lewat xDS API,",
                    "    jarang ditulis tangan.",
                    "  - Consul: service discovery, penyimpanan key-value, dan mesh dari",
                    "    HashiCorp, versi v2.0.4 (10 September 2026), lisensi BUSL-1.1.",
                    "    Sebagian fungsinya sudah tergeser fitur bawaan Kubernetes.",
                    "",
                    "Kapan mesh layak dipasang? Kalau layanannya sudah banyak, ada kewajiban",
                    "mTLS antarlayanan dari tim keamanan, dan ada orang yang sanggup",
                    "merawatnya. Untuk lima layanan dan satu tim, mesh biasanya menambah",
                    "masalah lebih banyak daripada yang ia selesaikan: proxy tambahan memakan",
                    "memori, dan satu salah konfigurasi bisa memutus semua layanan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Startup kecil biasanya mulai dari layanan seperti ECS, Cloud Run, atau",
                    "Kubernetes terkelola, karena nggak punya orang khusus untuk merawat",
                    "control plane. Perusahaan besar di sektor yang diawasi ketat, seperti",
                    "perbankan, lebih sering memilih OpenShift atau Rancher karena butuh",
                    "dukungan vendor dan klaster di pusat data sendiri.",
                    "",
                    "Kasus kecil: timmu (tiga orang, enam layanan, semuanya di AWS) diminta",
                    "memilih tempat menjalankan container untuk produk baru.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tulis kebutuhannya dulu: berapa layanan, apakah butuh deploy tanpa",
                    "     downtime, dan siapa yang akan merawat platformnya.",
                    "  2. Kalau belum ada yang paham Kubernetes dan semuanya di AWS, ECS",
                    "     dengan Fargate biasanya paling cepat jalan dan paling sedikit",
                    "     dirawat.",
                    "  3. Kalau tim berencana pindah cloud atau sudah memakai alat ekosistem",
                    "     Kubernetes seperti Helm dan Argo CD, pilih EKS dengan Auto Mode.",
                    "  4. Tunda service mesh. Catat sebagai pilihan untuk nanti kalau jumlah",
                    "     layanan dan kebutuhan mTLS sudah nyata.",
                ],
            },
        ],
    },
    {
        "title": "41. Helm: Memasang Aplikasi dengan Chart",
        "sections": [
            {
                "body": [
                    "Memasang Prometheus di Kubernetes dengan tangan berarti menulis belasan",
                    "manifest: Deployment, Service, ConfigMap, ServiceAccount, aturan RBAC,",
                    "dan seterusnya. Lalu tiap kali ada versi baru, kamu harus tahu bagian",
                    "mana yang berubah. Kerjaan seperti ini persis yang diselesaikan manajer",
                    "paket di Linux: di Fedora kamu cukup dnf install, nggak perlu menyalin",
                    "berkas satu per satu.",
                    "",
                    "Helm adalah manajer paket untuk Kubernetes. Empat istilahnya:",
                    "",
                    "  - chart: paket berisi templat manifest plus nilai bawaannya.",
                    "  - values: nilai yang mengisi templat, misalnya jumlah replika atau tag",
                    "    image. Kamu mengubah perilaku chart lewat values, tanpa menyunting",
                    "    templatnya.",
                    "  - release: satu pemasangan chart di klaster, diberi nama. Chart yang",
                    "    sama bisa dipasang dua kali dengan nama release berbeda.",
                    "  - repository: tempat chart disimpan, berupa situs HTTP berisi berkas",
                    "    index atau registry OCI yang sama dengan tempat image container.",
                    "",
                    "Helm berlisensi Apache-2.0 dan termasuk proyek CNCF. Survei tahunan CNCF",
                    "2025 mencatat 75% responden memilih Helm sebagai manajer paket",
                    "Kubernetes, dan Survei Stack Overflow 2026 mencatat 12,4%.",
                ],
            },
            {
                "heading": "Memasang chart dari repository",
                "bahasa": "terminal",
                "code": "# daftarkan repository, lalu cari chart\nhelm repo add prometheus-community https://prometheus-community.github.io/helm-charts\nhelm repo update\nhelm search repo prometheus-community/prometheus\n\n# lihat values bawaan sebelum memasang\nhelm show values prometheus-community/prometheus > bawaan.yaml\n\n# pasang dengan nama release 'pantau' di namespace pantau\nhelm install pantau prometheus-community/prometheus \\\n  --namespace pantau --create-namespace \\\n  -f values-prod.yaml\n\nhelm list -n pantau\nhelm status pantau -n pantau",
            },
            {
                "body": [
                    "Perintah helm install merender templat chart memakai values, lalu",
                    "mengirim hasilnya ke API server seperti kubectl apply. Informasi release",
                    "(chart apa, values apa, revisi keberapa) disimpan Helm sebagai objek",
                    "Secret di namespace release itu. Karena itu Helm nggak butuh server",
                    "khusus di klaster.",
                    "",
                    "Chart juga bisa dipasang langsung dari registry OCI, misalnya helm",
                    "install web oci://registry.contoh.id/charts/toko --version 1.4.0. Makin",
                    "banyak proyek mendistribusikan chart dengan cara ini.",
                ],
            },
            {
                "heading": "Urutan prioritas values",
                "body": [
                    "Satu kunci bisa diisi di beberapa tempat. Helm memakai urutan ini, dari",
                    "yang paling lemah ke yang paling kuat:",
                    "",
                    "  1. values.yaml bawaan di dalam chart.",
                    "  2. Berkas yang diberikan dengan -f atau --values. Kalau ada beberapa",
                    "     -f, berkas yang ditulis paling akhir menang.",
                    "  3. Nilai dari --set dan sejenisnya di baris perintah.",
                    "",
                    "Contohnya, values.yaml chart menulis replicaCount: 1, values-prod.yaml",
                    "menulis replicaCount: 3, dan perintahnya memakai --set replicaCount=5.",
                    "Hasilnya lima replika.",
                    "",
                    "Jebakan: menyimpan konfigurasi produksi di --set yang diketik manual.",
                    "Kalau saat upgrade kamu memberi values baru tapi lupa mengulang --set",
                    "lama, kunci yang lupa itu kembali ke nilai bawaan chart. Simpan semua",
                    "nilai di berkas yang ikut di-commit, lalu pakai -f berkas yang sama",
                    "setiap install dan upgrade.",
                ],
            },
            {
                "heading": "Upgrade, riwayat, dan rollback",
                "bahasa": "terminal",
                "code": "# naik versi chart atau ganti values\nhelm upgrade pantau prometheus-community/prometheus \\\n  -n pantau -f values-prod.yaml\n\n# install kalau belum ada, upgrade kalau sudah (enak untuk CI)\nhelm upgrade --install pantau prometheus-community/prometheus \\\n  -n pantau -f values-prod.yaml\n\nhelm history pantau -n pantau\nhelm rollback pantau 1 -n pantau\nhelm uninstall pantau -n pantau",
            },
            {
                "body": [
                    "Tiap install, upgrade, dan rollback menambah nomor revisi. Rollback",
                    "nggak menghapus riwayat: kembali ke revisi 1 dari revisi 2 menghasilkan",
                    "revisi 3 yang isinya sama dengan revisi 1. Jadi helm history selalu",
                    "menceritakan urutan kejadian apa adanya.",
                    "",
                    "Seperti rollback Deployment, helm rollback cuma mengembalikan objek",
                    "Kubernetes. Data di volume atau database yang sudah diubah versi baru",
                    "nggak ikut kembali.",
                ],
            },
            {
                "heading": "Helm 4 dan statusnya",
                "body": [
                    "Helm 4 dirilis akhir 2025, mayor pertama sejak Helm 3 tahun 2019. Saat",
                    "materi ini ditulis (Oktober 2026), versi terbarunya v4.3.1 (15 Oktober",
                    "2026). Perubahan pentingnya: sistem plugin baru yang mendukung plugin",
                    "WebAssembly, dukungan server-side apply, dan cara menunggu objek siap",
                    "yang lebih akurat. Chart lama (apiVersion v2) tetap bisa dipakai, tapi",
                    "beberapa flag CLI dan keluaran berubah, jadi skrip CI lama perlu dicek.",
                    "",
                    "Helm 3 masih menerima rilis perbaikan (v3.22.1 terbit di hari yang sama",
                    "dengan v4.3.1), tapi halaman rilisnya menyatakan 3.22 adalah rilis minor",
                    "terakhir Helm 3. Untuk belajar dan proyek baru, pakai Helm 4.",
                    "",
                    "Jebakan: chart yang dulu populer bisa berubah status. Pada 2025 Bitnami",
                    "menghentikan sebagian besar image gratisnya dan memindahkan image lama",
                    "ke repository bitnamilegacy, sehingga banyak chart lama merujuk image",
                    "yang nggak lagi diperbarui. Sebelum memakai chart pihak ketiga, cek",
                    "kapan terakhir dirilis dan image apa yang dipakainya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua perangkat pendukung di klaster, seperti Prometheus,",
                    "Grafana, cert-manager, dan Argo CD sendiri, dipasang lewat chart Helm",
                    "resmi proyeknya. Tim platform biasanya menyimpan values tiap chart di",
                    "repository Git, satu berkas per lingkungan, supaya pemasangan bisa",
                    "diulang persis.",
                    "",
                    "Kasus kecil: setelah helm upgrade, Prometheus gagal start, dan kamu",
                    "ingin kembali ke keadaan sebelum upgrade secepatnya.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Lihat riwayatnya dengan helm history pantau -n pantau dan cari",
                    "     revisi terakhir yang berstatus deployed sebelum upgrade, misalnya",
                    "     revisi 4.",
                    "  2. Kembalikan dengan helm rollback pantau 4 -n pantau. Helm membuat",
                    "     revisi baru berisi konfigurasi revisi 4.",
                    "  3. Pastikan pod-nya sehat lagi dengan kubectl get pods -n pantau.",
                    "  4. Bandingkan values lama dan baru dengan helm get values pantau",
                    "     --revision 4 -n pantau dan revisi yang gagal, lalu perbaiki berkas",
                    "     values sebelum mencoba upgrade lagi.",
                ],
            },
        ],
    },
    {
        "title": "42. Membuat Chart Helm dan Kapan Memilih Kustomize",
        "sections": [
            {
                "body": [
                    "Memakai chart orang lain itu satu hal. Untuk aplikasimu sendiri, kamu",
                    "bisa membuat chart supaya deploy ke staging dan produksi cuma beda",
                    "berkas values. Ada juga pendekatan lain tanpa templat sama sekali, yaitu",
                    "Kustomize. Materi ini membahas keduanya dan kapan memilih yang mana.",
                    "",
                    "Cara tercepat memulai chart adalah helm create toko. Perintah itu",
                    "membuat kerangka lengkap yang langsung bisa dipasang:",
                    "",
                    "  toko/",
                    "    Chart.yaml          nama, versi chart, versi aplikasi",
                    "    values.yaml         nilai bawaan",
                    "    charts/             chart lain yang jadi dependensi",
                    "    templates/",
                    "      deployment.yaml",
                    "      service.yaml",
                    "      _helpers.tpl      potongan templat yang dipakai ulang",
                    "      NOTES.txt         pesan yang muncul sesudah install",
                    "      tests/            uji sederhana untuk helm test",
                    "    .helmignore",
                ],
            },
            {
                "heading": "Chart.yaml dan values.yaml",
                "bahasa": "yaml",
                "code": """# Chart.yaml
apiVersion: v2
name: toko
version: 1.4.0        # versi chart, naik tiap templat berubah
appVersion: "2.4.1"   # versi aplikasi di dalamnya
---
# values.yaml
replicaCount: 1
image:
  repository: toko-api
  tag: ""             # kosong: pakai appVersion
service:
  port: 80
resources:
  requests:
    cpu: 250m
    memory: 256Mi""",
            },
            {
                "heading": "Templat",
                "bahasa": "yaml",
                "code": """# templates/deployment.yaml (dipendekkan)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "toko.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          env:
            - name: DB_HOST
              value: {{ required "db.host wajib diisi" .Values.db.host | quote }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}""",
            },
            {
                "body": [
                    "Templat Helm memakai bahasa templat Go. Bagian di antara {{ dan }}",
                    "diganti nilai saat render. Objek yang paling sering dipakai: .Values",
                    "(isi values), .Release (nama dan namespace release), dan .Chart (isi",
                    "Chart.yaml). Tanda | menyalurkan nilai ke fungsi berikutnya, mirip pipe",
                    "di shell. Fungsi default memberi nilai cadangan, quote membungkus dengan",
                    "tanda kutip, dan toYaml lalu nindent menyisipkan blok YAML dengan",
                    "indentasi yang pas.",
                    "",
                    "Chart juga punya versinya sendiri, terpisah dari versi aplikasi. Kolom",
                    "version di Chart.yaml mengikuti aturan SemVer (mayor.minor.patch) dan",
                    "wajib dinaikkan setiap templat atau values bawaan berubah, sedangkan",
                    "appVersion cuma label versi aplikasi di dalamnya. Chart lain yang",
                    "dibutuhkan, misalnya chart PostgreSQL, ditulis di bagian dependencies",
                    "pada Chart.yaml lalu diunduh ke folder charts/ dengan helm dependency",
                    "update.",
                    "",
                    "Ingat: kunci yang nggak ada di values dirender Helm sebagai teks kosong,",
                    "tanpa error. Typo seperti .Values.replicaCont menghasilkan replicas",
                    "kosong, dan masalahnya baru ketahuan saat manifest ditolak atau",
                    "berperilaku aneh. Fungsi required di contoh atas membuat render gagal",
                    "dengan pesan jelas kalau nilai wajib lupa diisi.",
                    "",
                    "Sebelum memasang, cek hasil render dengan perintah di bawah. Kebiasaan",
                    "ini menghemat banyak waktu karena error templat ketahuan di laptop.",
                ],
            },
            {
                "heading": "Memeriksa dan membagikan chart",
                "bahasa": "terminal",
                "code": """helm lint ./toko
helm template web ./toko -f values-staging.yaml   # lihat YAML hasil render
helm install web ./toko --dry-run=server -f values-staging.yaml

# bungkus dan dorong ke registry OCI
helm package ./toko
helm push toko-1.4.0.tgz oci://registry.contoh.id/charts""",
            },
            {
                "heading": "Kustomize: base dan overlay",
                "body": [
                    "Kustomize menempuh jalan lain. Manifest-nya tetap YAML Kubernetes biasa",
                    "yang bisa langsung dipasang, tanpa {{ }}. Perbedaan antarlingkungan",
                    "ditulis sebagai tambalan (patch) di folder overlay:",
                    "",
                    "  app/",
                    "    base/",
                    "      deployment.yaml",
                    "      service.yaml",
                    "      kustomization.yaml",
                    "    overlays/",
                    "      staging/kustomization.yaml",
                    "      prod/kustomization.yaml",
                    "",
                    "Kustomize sudah tertanam di kubectl, jadi kamu cukup menjalankan kubectl",
                    "apply -k overlays/prod. Versi mandirinya, saat materi ini ditulis,",
                    "kustomize/v5.8.3 (Oktober 2026). Versi yang tertanam di kubectl biasanya",
                    "tertinggal beberapa rilis dari versi mandiri, jadi fitur terbaru kadang",
                    "belum ada di kubectl.",
                ],
            },
            {
                "heading": "Overlay produksi",
                "bahasa": "yaml",
                "code": """# overlays/prod/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: toko-prod
resources:
  - ../../base
images:
  - name: toko-api
    newTag: "2.4.1"
patches:
  - target:
      kind: Deployment
      name: web
    patch: |-
      - op: replace
        path: /spec/replicas
        value: 5""",
            },
            {
                "heading": "Helm atau Kustomize?",
                "body": [
                    "  Pertanyaan                                   Lebih cocok",
                    "  Membagikan aplikasi ke orang lain?           Helm (chart punya versi)",
                    "  Pemasang perlu banyak pilihan konfigurasi?   Helm",
                    "  Aplikasi milik sendiri, beda sedikit per     Kustomize",
                    "  lingkungan?",
                    "  Tim nggak mau belajar templat Go?            Kustomize",
                    "  Perlu rollback dengan riwayat revisi?        Helm (helm rollback)",
                    "",
                    "Keduanya nggak saling meniadakan. Banyak tim memasang aplikasi pihak",
                    "ketiga dengan Helm dan menulis manifest aplikasinya sendiri dengan",
                    "Kustomize. Argo CD, yang dibahas di materi berikutnya, bisa membaca",
                    "keduanya. Kustomize bahkan bisa merender chart Helm lalu menambalnya.",
                    "",
                    "Jebakan: chart buatan sendiri yang terlalu banyak pilihan. Kalau tiap",
                    "baris manifest dibungkus if dan values.yaml-nya ratusan baris, chart",
                    "jadi lebih susah dibaca daripada YAML aslinya. Untuk aplikasi internal,",
                    "mulai dari sedikit values saja dan tambah hanya kalau memang dibutuhkan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek open source yang ingin mudah dipasang orang lain hampir selalu",
                    "menyediakan chart Helm resmi. Sebaliknya, banyak tim produk yang hanya",
                    "men-deploy aplikasinya sendiri ke dua atau tiga lingkungan memilih",
                    "Kustomize, karena manifest-nya tetap bisa dibaca dan di-review sebagai",
                    "YAML biasa di pull request.",
                    "",
                    "Kasus kecil: sesudah helm install, Deployment-mu punya replicas kosong",
                    "dan kubectl menolak manifestnya dengan pesan validasi.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Render tanpa memasang dengan helm template web ./toko -f",
                    "     values-prod.yaml lalu cari baris replicas di hasilnya.",
                    "  2. Kalau barisnya kosong, bandingkan nama kunci di templat",
                    "     (.Values.replicaCount) dengan nama di values-prod.yaml. Typo",
                    "     seperti replicaCont sering jadi penyebab.",
                    "  3. Betulkan nama kuncinya, lalu bungkus nilai penting dengan fungsi",
                    "     required supaya kesalahan serupa langsung menggagalkan render.",
                    "  4. Tambahkan helm lint dan helm template ke pipeline CI supaya",
                    "     pemeriksaan ini jalan di setiap pull request.",
                ],
            },
        ],
    },
    {
        "title": "43. GitOps dengan Argo CD",
        "sections": [
            {
                "body": [
                    "Di bab CI/CD, pipeline GitHub Actions berhenti di membangun image dan",
                    "mendorongnya ke registry. Langkah sesudahnya, memasang image itu ke",
                    "klaster, bisa dikerjakan dua cara.",
                    "",
                    "Cara dorong (push): pipeline CI menjalankan kubectl apply atau helm",
                    "upgrade ke klaster. Artinya CI harus memegang kredensial klaster, dan",
                    "siapa pun yang bisa mengubah pipeline bisa mengubah produksi. Kalau ada",
                    "yang mengubah klaster langsung dengan kubectl, nggak ada yang tahu",
                    "sampai deploy berikutnya menimpanya.",
                    "",
                    "Cara tarik (pull): ada agen yang berjalan di dalam klaster, terus",
                    "membaca repository Git, lalu menyamakan klaster dengan isi Git. Cara ini",
                    "disebut GitOps. CI cukup mengubah isi Git, misalnya tag image di berkas",
                    "values, dan nggak pernah menyentuh klaster.",
                ],
            },
            {
                "heading": "Empat prinsip GitOps",
                "body": [
                    "Proyek OpenGitOps merumuskan GitOps lewat empat prinsip:",
                    "",
                    "  1. Deklaratif: keadaan sistem ditulis sebagai keinginan, persis spec",
                    "     Kubernetes yang kamu pelajari di bab sebelumnya.",
                    "  2. Berversi dan nggak bisa diubah tanpa jejak: keinginan disimpan di",
                    "     Git, jadi setiap perubahan punya commit, penulis, dan riwayat.",
                    "  3. Ditarik otomatis: agen di sisi target menarik perubahan, bukan",
                    "     didorong dari luar.",
                    "  4. Direkonsiliasi terus-menerus: agen membandingkan keinginan dengan",
                    "     kenyataan dan membetulkan selisihnya, seperti controller",
                    "     Kubernetes.",
                    "",
                    "Kalau kamu sudah paham reconciliation loop, GitOps adalah loop yang sama",
                    "dengan sumber kebenaran yang dipindah ke Git. Untuk deploy, kamu membuat",
                    "pull request. Untuk rollback, kamu me-revert commit.",
                ],
            },
            {
                "heading": "Argo CD",
                "body": [
                    "Argo CD adalah alat GitOps paling banyak dipakai untuk Kubernetes. Ia",
                    "proyek CNCF graduated dengan lisensi Apache-2.0. Survei pengguna Argo CD",
                    "yang diumumkan CNCF pada Juli 2025 menyebut hampir 60% klaster",
                    "Kubernetes milik responden dikelola Argo CD, dan 97% responden",
                    "memakainya di produksi. Saat materi ini ditulis (Oktober 2026), versi",
                    "terbarunya v3.5.5 (12 Oktober 2026). Argo CD 3.0 yang rilis 2025",
                    "mengubah sejumlah pengaturan bawaan, termasuk RBAC, jadi panduan untuk",
                    "versi 2.x perlu dibaca hati-hati.",
                    "",
                    "Komponen utamanya:",
                    "",
                    "  - application controller: menjalankan loop rekonsiliasi, membandingkan",
                    "    Git dengan klaster, dan melakukan sync.",
                    "  - repo server: mengambil isi repository lalu merender manifest dari",
                    "    YAML biasa, Kustomize, atau chart Helm.",
                    "  - API server dan UI web: tempat kamu melihat status tiap aplikasi,",
                    "    diff, dan riwayatnya.",
                    "",
                    "Unit kerja Argo CD bernama Application: satu objek yang bilang \"isi",
                    "folder ini di repository itu harus terpasang di namespace ini di klaster",
                    "ini\".",
                ],
            },
            {
                "heading": "Memasang Argo CD",
                "bahasa": "terminal",
                "code": "kubectl create namespace argocd\nkubectl apply -n argocd --server-side --force-conflicts \\\n  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml\n\n# buka UI di laptop, lalu ambil kata sandi admin awal\nkubectl port-forward svc/argocd-server -n argocd 8080:443\nargocd admin initial-password -n argocd\n\n# perintah CLI yang sering dipakai\nargocd login localhost:8080\nargocd app list\nargocd app get toko-prod\nargocd app diff toko-prod\nargocd app sync toko-prod",
            },
            {
                "heading": "Application pertama",
                "bahasa": "yaml",
                "code": """apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: toko-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/contoh/toko-deploy.git
    targetRevision: main
    path: overlays/prod          # folder Kustomize
  destination:
    server: https://kubernetes.default.svc   # klaster tempat Argo CD berada
    namespace: toko-prod
  syncPolicy:
    automated:
      prune: true      # hapus objek yang dihapus dari Git
      selfHeal: true   # kembalikan perubahan manual di klaster
    syncOptions:
      - CreateNamespace=true""",
            },
            {
                "body": [
                    "Begitu objek ini dibuat, Argo CD mengambil isi folder overlays/prod,",
                    "merendernya dengan Kustomize, membandingkannya dengan isi namespace",
                    "toko-prod, lalu memasang yang belum ada. Bawaannya, Argo CD memeriksa",
                    "repository kira-kira tiap tiga menit. Untuk reaksi yang lebih cepat,",
                    "repository bisa mengirim webhook ke Argo CD setiap ada push.",
                    "",
                    "Pola yang umum dipakai: kode aplikasi dan konfigurasi deploy disimpan di",
                    "dua repository terpisah. Repository kode memicu CI yang membangun image",
                    "toko-api:2.5.0 lalu membuat commit kecil yang mengubah newTag di",
                    "repository deploy. Argo CD melihat commit itu dan melakukan sync. Dengan",
                    "begitu, riwayat Git repository deploy sekaligus jadi catatan semua yang",
                    "pernah naik ke produksi.",
                    "",
                    "Jebakan: menaruh Secret berisi nilai asli di repository deploy karena",
                    "\"semuanya harus di Git\". Yang masuk Git cukup rujukannya, misalnya objek",
                    "ExternalSecret atau SealedSecret yang terenkripsi. Topik ini dibahas di",
                    "kurikulum Keamanan Siber.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perusahaan yang punya banyak klaster, misalnya satu per region atau satu",
                    "per tim, memakai Argo CD supaya status semua aplikasi terlihat di satu",
                    "layar. Setiap perubahan produksi juga tercatat sebagai pull request yang",
                    "di-review. Audit \"siapa mengubah apa dan kapan\" jadi cukup dengan",
                    "membaca riwayat Git.",
                    "",
                    "Kasus kecil: kamu menggabungkan pull request yang menaikkan tag image ke",
                    "2.5.0, tapi lima menit kemudian aplikasi di klaster masih versi 2.4.1.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buka argocd app get toko-prod dan lihat status sync serta revisi",
                    "     Git yang terakhir dibaca. Kalau revisinya masih commit lama, Argo",
                    "     CD belum melihat perubahanmu.",
                    "  2. Pastikan targetRevision dan path di Application memang menunjuk",
                    "     branch dan folder yang kamu ubah. Mengubah overlays/staging nggak",
                    "     berpengaruh ke aplikasi yang membaca overlays/prod.",
                    "  3. Kalau statusnya OutOfSync tapi nggak ada sync otomatis, cek apakah",
                    "     syncPolicy.automated terpasang. Tanpa itu, sync harus dipicu manual",
                    "     dengan argocd app sync toko-prod.",
                    "  4. Kalau sync jalan tapi pod baru gagal, kesehatannya tampil Degraded.",
                    "     Lanjutkan pemeriksaan dengan kubectl describe pod seperti di bab",
                    "     Kubernetes.",
                ],
            },
        ],
    },
    {
        "title": "44. Argo CD Lanjutan: Drift, Rollback, dan Flux",
        "sections": [
            {
                "body": [
                    "Sesudah Argo CD berjalan, pertanyaan berikutnya muncul dari kejadian",
                    "sehari-hari. Bagaimana kalau ada orang yang mengubah klaster langsung",
                    "dengan kubectl? Bagaimana cara rollback kalau versi baru rusak?",
                    "Bagaimana memastikan migrasi database jalan sebelum aplikasinya diganti?",
                    "Materi ini menjawab ketiganya, lalu mengenalkan Flux, alternatif utama",
                    "Argo CD.",
                ],
            },
            {
                "heading": "Drift dan status aplikasi",
                "body": [
                    "Drift adalah selisih antara isi Git dan isi klaster yang muncul bukan",
                    "dari Git, misalnya seseorang menjalankan kubectl scale deployment/web",
                    "--replicas=5 saat panik. Argo CD menampilkan dua status terpisah:",
                    "",
                    "  - status sync: Synced (klaster sama dengan Git) atau OutOfSync (ada",
                    "    selisih).",
                    "  - status kesehatan: Healthy, Progressing (sedang berubah), Degraded",
                    "    (gagal), Missing (belum ada), atau Suspended.",
                    "",
                    "Keduanya bisa berbeda. Aplikasi bisa Synced tapi Degraded, artinya yang",
                    "terpasang sudah persis Git, tapi isinya memang rusak.",
                    "",
                    "Dengan selfHeal: true, Argo CD langsung mengembalikan drift ke isi Git.",
                    "Tanpa selfHeal, aplikasinya cuma ditandai OutOfSync dan menunggu kamu.",
                    "",
                    "Beberapa kolom memang wajar berbeda. Contohnya spec.replicas yang diubah",
                    "HorizontalPodAutoscaler sesuai beban. Kalau kolom itu nggak",
                    "dikecualikan, Argo CD dan autoscaler akan saling membatalkan.",
                    "Pengecualiannya ditulis di ignoreDifferences.",
                ],
            },
            {
                "heading": "Mengecualikan kolom milik autoscaler",
                "bahasa": "yaml",
                "code": """spec:
  ignoreDifferences:
    - group: apps
      kind: Deployment
      name: web
      jsonPointers:
        - /spec/replicas
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - RespectIgnoreDifferences=true""",
            },
            {
                "heading": "Prune dan rollback",
                "body": [
                    "Objek yang dihapus dari Git nggak otomatis dihapus dari klaster. Sync",
                    "otomatis cuma melakukan prune (menghapus objek yang sudah nggak ada di",
                    "Git) kalau prune: true dipasang. Bawaannya dimatikan, karena salah hapus",
                    "folder di Git bisa berarti salah hapus aplikasi di produksi. Objek yang",
                    "menunggu dihapus ditandai di UI sebagai butuh prune.",
                    "",
                    "Untuk rollback ada dua jalan. Jalan GitOps adalah git revert commit yang",
                    "merusak, lalu biarkan Argo CD sync. Klaster kembali, dan riwayat Git",
                    "tetap jujur. Jalan kedua adalah argocd app rollback ke riwayat deploy",
                    "sebelumnya, tapi perintah ini ditolak selama sync otomatis aktif, karena",
                    "sync otomatis akan langsung menimpa hasil rollback dengan isi Git lagi.",
                    "Dalam praktik, git revert hampir selalu pilihan yang benar.",
                ],
            },
            {
                "heading": "Sync wave dan hook",
                "body": [
                    "Kadang urutan pemasangan penting. Migrasi skema database harus selesai",
                    "sebelum versi aplikasi yang memakainya jalan. Argo CD mengatur urutan",
                    "lewat anotasi:",
                    "",
                    "  - argocd.argoproj.io/sync-wave: angka gelombang. Objek dengan angka",
                    "    lebih kecil dipasang dan ditunggu sampai sehat lebih dulu. Bawaannya",
                    "    0, dan angka negatif boleh.",
                    "  - argocd.argoproj.io/hook: menandai objek, biasanya Job, untuk",
                    "    dijalankan pada fase tertentu, misalnya PreSync (sebelum sync) atau",
                    "    PostSync (sesudahnya).",
                    "",
                    "Untuk banyak aplikasi sekaligus, Argo CD punya pola app of apps (satu",
                    "Application yang isinya Application lain) dan objek ApplicationSet yang",
                    "membuat Application dari daftar klaster atau folder secara otomatis.",
                ],
            },
            {
                "heading": "Job migrasi sebagai hook PreSync",
                "bahasa": "yaml",
                "code": """apiVersion: batch/v1
kind: Job
metadata:
  name: migrasi-db
  annotations:
    argocd.argoproj.io/hook: PreSync
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrasi
          image: toko-api:2.5.0
          command: ["python", "manage.py", "migrate"]""",
            },
            {
                "heading": "Flux",
                "body": [
                    "Flux adalah alat GitOps kedua yang juga proyek CNCF graduated dan",
                    "berlisensi Apache-2.0. Saat materi ini ditulis, versi terbarunya v2.9.6",
                    "(1 Oktober 2026). Weaveworks, perusahaan yang memulainya, tutup pada",
                    "Februari 2024, tapi proyeknya berlanjut dengan pemelihara dari vendor",
                    "lain.",
                    "",
                    "Flux tersusun dari beberapa controller kecil, masing-masing dengan objek",
                    "sendiri. Ada source-controller (mengambil isi Git, repository Helm, atau",
                    "artefak OCI), kustomize-controller (memasang folder Kustomize),",
                    "helm-controller (mengelola objek HelmRelease), dan notification-",
                    "controller (mengirim kabar ke Slack atau menerima webhook). Semuanya",
                    "diatur lewat YAML dan CLI flux; UI web bukan bagian inti proyeknya.",
                    "",
                    "  Aspek          Argo CD                     Flux",
                    "  Unit utama     Application                 Kustomization, HelmRelease",
                    "  UI web         bawaan, lengkap             di luar proyek inti",
                    "  Chart Helm     dirender jadi manifest      dipasang sebagai release Helm",
                    "  Multi-klaster  satu Argo CD, banyak        biasanya satu Flux per klaster",
                    "                 klaster",
                    "  Cocok untuk    tim yang ingin satu layar   tim yang suka semua lewat Git",
                ],
            },
            {
                "heading": "Memulai Flux",
                "bahasa": "terminal",
                "code": "flux check --pre\nflux bootstrap github \\\n  --owner=contoh --repository=toko-deploy \\\n  --branch=main --path=./clusters/prod --personal\n\nflux get kustomizations\nflux reconcile kustomization flux-system --with-source",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang memakai GitOps biasanya mengunci akses tulis kubectl ke",
                    "produksi untuk kebanyakan orang. Perubahan darurat pun lewat pull",
                    "request kecil, sehingga setelah insiden selesai, riwayat Git menunjukkan",
                    "persis apa yang diubah dan kapan.",
                    "",
                    "Kasus kecil: rekanmu menaikkan replika web ke 8 lewat kubectl saat ramai",
                    "pengunjung. Beberapa detik kemudian replikanya kembali ke 3, dan ia",
                    "mengira klasternya rusak.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jelaskan bahwa ini selfHeal: Argo CD melihat drift dari isi Git",
                    "     (replicas: 3) dan mengembalikannya. Klasternya bekerja sesuai",
                    "     rancangan.",
                    "  2. Kalau kebutuhan itu sementara, ubah replicas di repository deploy",
                    "     lewat pull request kecil, lalu biarkan Argo CD sync.",
                    "  3. Kalau jumlah replika memang harus naik turun mengikuti beban,",
                    "     pasang HorizontalPodAutoscaler dan tambahkan /spec/replicas ke",
                    "     ignoreDifferences.",
                    "  4. Catat kejadian ini di runbook tim supaya orang berikutnya tahu",
                    "     jalurnya lewat Git, bukan kubectl.",
                ],
            },
        ],
    },
    {
        "title": "45. Dasar Observability: Metrik, Log, Trace, dan SLO",
        "sections": [
            {
                "body": [
                    "Aplikasi yang sudah jalan di produksi seperti mobil yang sedang melaju:",
                    "kamu nggak bisa membongkar mesinnya untuk mengecek. Yang kamu punya cuma",
                    "dasbor dan suara mesinnya. Observability adalah kemampuan memahami apa",
                    "yang terjadi di dalam sistem dari data yang ia keluarkan, tanpa harus",
                    "masuk dan menebak.",
                    "",
                    "Bedanya dengan monitoring biasa: monitoring menjawab pertanyaan yang",
                    "sudah kamu siapkan (\"CPU di atas 90%?\"). Observability juga menolong",
                    "menjawab pertanyaan yang baru muncul saat insiden, misalnya \"kenapa",
                    "checkout lambat cuma untuk pengguna di aplikasi Android versi lama?\"",
                ],
            },
            {
                "heading": "Tiga sinyal: metrik, log, trace",
                "body": [
                    "  - Metrik: angka yang diukur berkala, misalnya jumlah permintaan per",
                    "    detik atau pemakaian memori. Murah disimpan dan cepat ditanya, cocok",
                    "    untuk grafik dan alert. Kelemahannya, metrik nggak menceritakan",
                    "    permintaan mana yang bermasalah.",
                    "  - Log: catatan kejadian satu per satu, misalnya \"pembayaran pesanan",
                    "    A-1002 gagal, kode 502\". Kaya detail, tapi volumenya besar dan mahal",
                    "    kalau disimpan lama.",
                    "  - Trace: jejak satu permintaan yang melewati banyak layanan, lengkap",
                    "    dengan berapa lama tiap langkahnya. Menjawab pertanyaan \"lambatnya",
                    "    di bagian mana\".",
                    "",
                    "Ketiganya saling melengkapi. Alur yang umum saat insiden: metrik memberi",
                    "tahu ada masalah (error naik), trace menunjukkan layanan mana yang",
                    "bermasalah, dan log di layanan itu menjelaskan sebabnya. OpenTelemetry,",
                    "yang dibahas tiga materi lagi, juga sedang mengembangkan sinyal keempat",
                    "bernama profile, yaitu rekaman fungsi mana yang memakan CPU.",
                ],
            },
            {
                "heading": "Empat golden signals",
                "body": [
                    "Buku Site Reliability Engineering dari Google menyarankan empat hal yang",
                    "paling dulu diukur untuk layanan yang melayani pengguna:",
                    "",
                    "  - Latency: berapa lama permintaan dilayani. Pisahkan latensi",
                    "    permintaan yang berhasil dan yang gagal, karena error yang cepat",
                    "    bisa menurunkan rata-rata dan menyesatkan.",
                    "  - Traffic: seberapa ramai, misalnya permintaan per detik.",
                    "  - Errors: berapa banyak permintaan yang gagal, misalnya persentase",
                    "    respons 5xx.",
                    "  - Saturation: seberapa penuh sumber dayanya, misalnya CPU, memori,",
                    "    atau panjang antrean.",
                    "",
                    "Kalau kamu cuma sempat memasang empat grafik untuk sebuah layanan,",
                    "pasang empat ini.",
                ],
            },
            {
                "heading": "SLI, SLO, SLA, dan error budget",
                "body": [
                    "SLI (service level indicator) adalah angka yang diukur, misalnya",
                    "\"persentase permintaan checkout yang berhasil dalam waktu di bawah 500",
                    "ms\". SLO (service level objective) adalah target internal untuk angka",
                    "itu, misalnya 99,9% dalam 30 hari. SLA (service level agreement) adalah",
                    "janji ke pelanggan yang ada akibat hukum atau ganti ruginya, dan",
                    "biasanya dibuat lebih longgar dari SLO.",
                    "",
                    "Kebalikan dari SLO adalah error budget: jatah gagal yang boleh dipakai.",
                    "SLO 99,9% berarti 0,1% boleh gagal. Kalau budget masih banyak, tim boleh",
                    "merilis lebih berani. Kalau budget hampir habis, tim mengerem rilis dan",
                    "fokus ke keandalan. Dengan begitu, perdebatan \"kecepatan atau",
                    "stabilitas\" diputuskan oleh angka.",
                ],
            },
            {
                "heading": "Menghitung jatah gagal dan membaca persentil",
                "code": """menit_sebulan = 30 * 24 * 60
for target in (99.0, 99.5, 99.9, 99.99):
    jatah = menit_sebulan * (100 - target) / 100
    print(f"SLO {target}%: boleh mati {jatah:.1f} menit per 30 hari")

# latensi 10 permintaan, dalam milidetik
latensi = [120, 95, 110, 130, 105, 98, 115, 2400, 101, 2600]
urut = sorted(latensi)
rata = sum(latensi) / len(latensi)
p50 = urut[4]   # peringkat ke-5 dari 10
p90 = urut[8]   # peringkat ke-9 dari 10
print(f"rata-rata {rata:.1f} ms, p50 {p50} ms, p90 {p90} ms")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  SLO 99.0%: boleh mati 432.0 menit per 30 hari",
                    "  SLO 99.5%: boleh mati 216.0 menit per 30 hari",
                    "  SLO 99.9%: boleh mati 43.2 menit per 30 hari",
                    "  SLO 99.99%: boleh mati 4.3 menit per 30 hari",
                    "  rata-rata 587.4 ms, p50 110 ms, p90 2400 ms",
                    "",
                    "Tiap tambahan angka sembilan memotong jatah jadi sepersepuluh. Empat",
                    "menit sebulan berarti deploy yang gagal sekali saja sudah menghabiskan",
                    "budget, jadi target setinggi itu butuh biaya dan disiplin yang jauh",
                    "lebih besar. Pilih SLO yang memang dibutuhkan pengguna.",
                    "",
                    "Bagian kedua menunjukkan kenapa latensi diukur dengan persentil, bukan",
                    "rata-rata. Rata-ratanya 587 ms, angka yang nggak dialami siapa pun:",
                    "delapan orang menunggu sekitar 100 ms, dua orang menunggu lebih dari dua",
                    "detik. p50 (median) bilang separuh permintaan selesai dalam 110 ms, dan",
                    "p90 bilang satu dari sepuluh permintaan butuh 2400 ms atau lebih. Dua",
                    "pengguna yang menunggu itulah yang menulis ulasan bintang satu.",
                ],
            },
            {
                "heading": "Alert yang pantas membangunkan orang",
                "body": [
                    "Alert yang terlalu banyak sama buruknya dengan nggak ada alert. Kalau",
                    "ponsel jaga berbunyi lima kali semalam untuk hal yang nggak perlu",
                    "ditindak, orang belajar mengabaikannya, termasuk saat alert yang penting",
                    "datang. Kondisi ini disebut alert fatigue.",
                    "",
                    "Pegangan yang dipakai banyak tim SRE:",
                    "",
                    "  - Alert yang memanggil orang (page) cuma untuk gejala yang dirasakan",
                    "    pengguna dan butuh tindakan segera, misalnya error rate checkout",
                    "    naik atau error budget terbakar cepat.",
                    "  - Penyebab seperti CPU tinggi atau disk 80% dikirim sebagai tiket atau",
                    "    pesan kanal, bukan page, kecuali memang akan menjatuhkan layanan",
                    "    dalam hitungan jam.",
                    "  - Tiap alert punya runbook: tautan ke langkah pertama yang harus",
                    "    dicoba.",
                    "",
                    "Cara modern menulis alert SLO adalah lewat burn rate, yaitu seberapa",
                    "cepat error budget dihabiskan dibanding laju yang \"pas\" untuk 30 hari.",
                    "Burn rate 1 berarti budget habis tepat di akhir periode, burn rate 10",
                    "berarti habis dalam tiga hari. Proyek akhir kurikulum ini memakai ide",
                    "tersebut.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan publik seperti penyedia cloud dan platform pembayaran menulis",
                    "target ketersediaan di halaman SLA mereka, misalnya 99,9% atau 99,95%",
                    "per bulan, lengkap dengan potongan tagihan kalau target itu meleset. Di",
                    "balik SLA tersebut, tim mereka memakai SLO internal yang lebih ketat",
                    "supaya punya ruang sebelum janji ke pelanggan dilanggar.",
                    "",
                    "Kasus kecil: atasanmu minta \"pokoknya checkout harus 100% nyala\" dan",
                    "meminta alert setiap ada satu error.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tunjukkan bahwa 100% mustahil dan membuat setiap rilis jadi",
                    "     pelanggaran. Bahkan jaringan pengguna sendiri gagal sesekali.",
                    "  2. Usulkan SLI yang jelas, misalnya persentase permintaan checkout",
                    "     yang berhasil di bawah 500 ms, diukur di load balancer.",
                    "  3. Sepakati SLO yang realistis, misalnya 99,9% per 30 hari, dan hitung",
                    "     jatahnya: 43,2 menit.",
                    "  4. Ganti alert per error dengan alert burn rate, supaya orang",
                    "     dipanggil hanya saat budget habis terlalu cepat.",
                ],
            },
        ],
    },
    {
        "title": "46. Prometheus: Mengumpulkan Metrik dari Aplikasi",
        "sections": [
            {
                "body": [
                    "Prometheus adalah sistem pemantauan sekaligus database deret waktu (time",
                    "series), yaitu database yang menyimpan angka beserta waktu",
                    "pengukurannya. Ia lahir di SoundCloud tahun 2012, jadi proyek kedua yang",
                    "lulus dari CNCF sesudah Kubernetes, dan berlisensi Apache-2.0. Saat",
                    "materi ini ditulis (Oktober 2026), versi terbarunya 3.15.0 (24 September",
                    "2026). Prometheus 3.0 yang rilis November 2024 membawa antarmuka web",
                    "baru dan kemampuan menerima data OpenTelemetry. Survei Stack Overflow",
                    "2025 mencatat 11,8% responden memakainya.",
                ],
            },
            {
                "heading": "Model pull",
                "body": [
                    "Kebanyakan sistem pemantauan lama menunggu aplikasi mengirim data",
                    "(push). Prometheus kebalikannya: ia yang datang mengambil. Aplikasi",
                    "cukup menyediakan halaman HTTP, biasanya /metrics, berisi angka-angka",
                    "saat itu dalam format teks. Prometheus membaca halaman itu tiap selang",
                    "waktu tertentu. Proses ini disebut scrape, dan alamat yang dibaca",
                    "disebut target.",
                    "",
                    "Keuntungannya: Prometheus tahu kalau target mati, karena scrape-nya",
                    "gagal. Metrik bawaan up bernilai 0 untuk target yang nggak bisa",
                    "dihubungi, dan itu sudah jadi alert yang berguna. Aplikasi juga nggak",
                    "perlu tahu alamat Prometheus.",
                    "",
                    "Untuk program yang hidupnya sebentar, misalnya job backup tiap malam,",
                    "model pull nggak cocok karena job-nya sudah selesai sebelum sempat",
                    "di-scrape. Untuk kasus ini ada Pushgateway, tempat job menitipkan",
                    "metriknya.",
                ],
            },
            {
                "heading": "Empat jenis metrik",
                "body": [
                    "  - Counter: angka yang cuma bisa naik, dan kembali ke nol kalau proses",
                    "    restart. Contoh: total permintaan, total error. Nama counter",
                    "    diakhiri _total. Dari sebuah counter, yang menarik adalah lajunya,",
                    "    yang dihitung dengan fungsi rate() di materi berikutnya.",
                    "  - Gauge: angka yang bisa naik dan turun. Contoh: memori terpakai,",
                    "    jumlah koneksi aktif, suhu.",
                    "  - Histogram: menghitung berapa pengamatan yang masuk tiap ember",
                    "    (bucket), misalnya berapa permintaan selesai di bawah 0,1 detik, di",
                    "    bawah 0,25 detik, dan seterusnya. Dari bucket ini Prometheus bisa",
                    "    memperkirakan persentil.",
                    "  - Summary: mirip histogram, tapi persentilnya dihitung di aplikasi.",
                    "    Kelemahannya, summary dari beberapa pod nggak bisa digabung, jadi",
                    "    histogram lebih sering dipilih.",
                    "",
                    "Tiap metrik bisa punya label, pasangan kunci dan nilai yang memecah satu",
                    "metrik jadi beberapa deret, misalnya method=\"GET\" dan status=\"200\".",
                    "Setiap kombinasi label yang berbeda adalah satu deret waktu tersendiri.",
                ],
            },
            {
                "heading": "Menginstrumentasi aplikasi Python",
                "code": """from prometheus_client import Counter, Histogram, generate_latest

PERMINTAAN = Counter("http_requests", "Jumlah permintaan HTTP",
                     ["method", "status"])
LATENSI = Histogram("http_request_duration_seconds", "Lama permintaan",
                    buckets=[0.1, 0.25, 0.5, 1.0])


def tangani(method, status, detik):
    PERMINTAAN.labels(method=method, status=status).inc()
    LATENSI.observe(detik)


tangani("GET", "200", 0.08)
tangani("GET", "200", 0.3)
tangani("POST", "500", 0.7)
print(generate_latest().decode())   # isi halaman /metrics""",
            },
            {
                "body": [
                    "Sebagian isi yang dicetak (diuji dengan prometheus_client 0.26):",
                    "",
                    "  # TYPE http_requests_total counter",
                    "  http_requests_total{method=\"GET\",status=\"200\"} 2.0",
                    "  http_requests_total{method=\"POST\",status=\"500\"} 1.0",
                    "  # TYPE http_request_duration_seconds histogram",
                    "  http_request_duration_seconds_bucket{le=\"0.1\"} 1.0",
                    "  http_request_duration_seconds_bucket{le=\"0.25\"} 1.0",
                    "  http_request_duration_seconds_bucket{le=\"0.5\"} 2.0",
                    "  http_request_duration_seconds_bucket{le=\"1.0\"} 3.0",
                    "  http_request_duration_seconds_bucket{le=\"+Inf\"} 3.0",
                    "  http_request_duration_seconds_count 3.0",
                    "  http_request_duration_seconds_sum 1.08",
                    "",
                    "Perhatikan dua hal. Pustaka menambahkan akhiran _total sendiri ke nama",
                    "counter. Dan bucket histogram bersifat kumulatif: le=\"0.5\" bernilai 2",
                    "artinya dua permintaan selesai dalam 0,5 detik atau kurang, termasuk",
                    "yang 0,08 detik. Di aplikasi web sungguhan, halaman ini disajikan lewat",
                    "start_http_server(8000) atau integrasi dengan framework web-mu.",
                ],
            },
            {
                "heading": "Konfigurasi scrape",
                "bahasa": "yaml",
                "code": """# prometheus.yml
global:
  scrape_interval: 15s      # bawaannya 1m kalau tidak ditulis

rule_files:
  - alert-toko.yml

scrape_configs:
  - job_name: toko-api
    static_configs:
      - targets: ["toko-api:8000"]

  - job_name: node          # node_exporter di tiap server
    static_configs:
      - targets: ["server-1:9100", "server-2:9100"]""",
            },
            {
                "heading": "Exporter dan penemuan target",
                "body": [
                    "Aplikasi yang nggak bisa kamu ubah, seperti Linux, PostgreSQL, atau",
                    "Nginx, dipantau lewat exporter: program kecil yang membaca keadaan",
                    "sistem itu lalu menyajikannya dalam format Prometheus. Yang paling",
                    "sering dipakai node_exporter (CPU, memori, disk, jaringan server, port",
                    "bawaan 9100) dan blackbox_exporter (mengecek dari luar apakah situs bisa",
                    "dibuka). Di Kubernetes, kube-state-metrics menyajikan keadaan objek",
                    "seperti jumlah replika siap.",
                    "",
                    "Di Kubernetes, menulis daftar target tangan nggak mungkin karena pod",
                    "datang dan pergi. Prometheus punya service discovery, misalnya",
                    "kubernetes_sd_configs, yang membaca daftar pod dari API server. Banyak",
                    "klaster memasang Prometheus lewat chart kube-prometheus-stack, yang",
                    "membawa Prometheus Operator dan objek ServiceMonitor untuk memilih",
                    "target berdasarkan label.",
                    "",
                    "Prometheus menyimpan data di disk lokal satu server. Untuk penyimpanan",
                    "jangka panjang dan banyak klaster, orang menambahkan Thanos atau Grafana",
                    "Mimir di belakangnya.",
                ],
            },
            {
                "heading": "Jebakan kardinalitas",
                "body": [
                    "Jebakan: memasang label dengan nilai yang nggak terbatas, seperti",
                    "user_id, alamat email, atau URL lengkap dengan ID pesanan. Setiap nilai",
                    "unik membuat deret waktu baru. Sejuta pengguna berarti sejuta deret",
                    "untuk satu metrik, dan memori Prometheus naik sampai prosesnya mati.",
                    "Jumlah kombinasi nilai label disebut kardinalitas.",
                    "",
                    "Label yang aman punya sedikit nilai yang bisa kamu sebutkan: method,",
                    "status, nama layanan, region. Untuk path, pakai pola rutenya",
                    "(/pesanan/{id}), bukan path aslinya (/pesanan/A-1001). Detail per",
                    "pengguna atau per pesanan tempatnya di log dan trace.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Prometheus jadi pemantau bawaan di hampir semua klaster Kubernetes, dan",
                    "banyak perangkat lunak server populer menyediakan endpoint /metrics atau",
                    "exporter resminya sendiri. Layanan terkelola seperti Amazon Managed",
                    "Service for Prometheus dan Grafana Cloud menerima data dengan format dan",
                    "bahasa kueri yang sama.",
                    "",
                    "Kasus kecil: memori server Prometheus-mu naik terus sejak tim backend",
                    "menambahkan metrik baru minggu lalu, dan sekarang prosesnya restart tiap",
                    "beberapa jam.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buka halaman Status lalu TSDB Status di antarmuka web Prometheus.",
                    "     Di sana ada daftar metrik dan label dengan jumlah deret terbanyak.",
                    "  2. Cari label yang nilainya nggak terbatas, misalnya path berisi ID",
                    "     pesanan atau label user_id pada metrik baru itu.",
                    "  3. Minta tim backend mengganti label itu dengan pola rute, atau",
                    "     membuangnya. Detail per pesanan dipindah ke log.",
                    "  4. Sementara menunggu rilis perbaikan, buang label tersebut saat",
                    "     scrape dengan aturan metric_relabel_configs berisi action",
                    "     labeldrop.",
                ],
            },
        ],
    },
    {
        "title": "47. PromQL, Alert, dan Dasbor Grafana",
        "sections": [
            {
                "body": [
                    "Data di Prometheus ditanya dengan PromQL, bahasa kueri khusus deret",
                    "waktu. Bentuknya mirip memanggil fungsi matematika, bukan seperti SQL.",
                    "Kueri paling sederhana adalah nama metrik, misalnya up, yang",
                    "mengembalikan nilai terbaru untuk setiap deret. Hasil seperti ini",
                    "disebut instant vector.",
                    "",
                    "Label dipakai untuk menyaring: http_requests_total{status=\"500\"} cuma",
                    "mengambil deret dengan status 500. Operatornya =, !=, =~ (cocok pola",
                    "regex), dan !~. Kalau ditambah rentang waktu dalam kurung siku, misalnya",
                    "http_requests_total[5m], hasilnya semua sampel lima menit terakhir untuk",
                    "tiap deret. Bentuk ini disebut range vector dan jadi masukan fungsi",
                    "seperti rate().",
                ],
            },
            {
                "heading": "Counter, rate(), dan increase()",
                "body": [
                    "Nilai mentah counter jarang berguna: angka 1.204.311 permintaan nggak",
                    "menjawab apakah sekarang sedang ramai. Yang kamu mau adalah lajunya.",
                    "rate(http_requests_total[5m]) menghitung kenaikan rata-rata per detik",
                    "selama lima menit terakhir. increase() menghitung total kenaikan di",
                    "rentang itu.",
                    "",
                    "Kedua fungsi ini paham counter yang reset. Kalau pod restart, counter",
                    "mulai lagi dari nol. rate() melihat nilai yang tiba-tiba turun sebagai",
                    "reset, lalu menganggap kenaikannya dihitung dari nol, bukan sebagai",
                    "penurunan. Contoh dengan sampel tiap 15 detik:",
                    "",
                    "  detik    nilai    kenaikan",
                    "  0        100",
                    "  15       130      30",
                    "  30       160      30",
                    "  45        20      20   (reset: dihitung dari 0)",
                    "  60        50      30",
                    "",
                    "Total kenaikan 110 dalam 60 detik, jadi lajunya sekitar 1,83 per detik.",
                    "Prometheus sungguhan sedikit mengekstrapolasi ke tepi jendela, jadi",
                    "angkanya bisa beda tipis. Latihan bab ini memintamu menulis versi",
                    "sederhananya sendiri.",
                    "",
                    "Ingat: rentang di dalam rate() sebaiknya minimal empat kali interval",
                    "scrape. Dengan scrape 15 detik, [1m] masih aman, tapi [30s] sering cuma",
                    "berisi dua sampel dan grafiknya jadi patah-patah.",
                ],
            },
            {
                "heading": "Kueri yang paling sering dipakai",
                "bahasa": "promql",
                "code": """# permintaan per detik, dijumlah per status
sum by (status) (rate(http_requests_total[5m]))

# rasio error: permintaan 5xx dibagi semua permintaan
sum(rate(http_requests_total{status=~"5.."}[5m]))
  / sum(rate(http_requests_total[5m]))

# p95 latensi dari histogram
histogram_quantile(0.95,
  sum by (le) (rate(http_request_duration_seconds_bucket[5m])))

# pemakaian CPU tiap server (0 sampai 1)
1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m]))""",
            },
            {
                "body": [
                    "sum by (status) menjumlahkan semua deret dan cuma menyisakan label",
                    "status, mirip GROUP BY di SQL. histogram_quantile() memperkirakan",
                    "persentil dari bucket dengan interpolasi linear di dalam bucket tempat",
                    "persentil itu jatuh. Akibatnya, ketelitian persentil bergantung pada",
                    "pilihan bucket. Kalau bucket-mu 0,5 dan 1 detik, p95 yang dilaporkan",
                    "0,81 detik cuma bisa dipastikan berada \"antara 0,5 dan 1 detik\".",
                ],
            },
            {
                "heading": "Aturan alert",
                "bahasa": "yaml",
                "code": "# alert-toko.yml\ngroups:\n  - name: toko-api\n    rules:\n      - alert: ErrorRateTinggi\n        expr: |\n          sum(rate(http_requests_total{status=~\"5..\"}[5m]))\n            / sum(rate(http_requests_total[5m])) > 0.05\n        for: 10m               # harus bertahan 10 menit dulu\n        labels:\n          severity: page\n        annotations:\n          summary: \"Lebih dari 5% permintaan toko-api gagal\"\n          runbook_url: \"https://wiki.contoh.id/runbook/error-rate\"",
            },
            {
                "body": [
                    "Prometheus mengevaluasi aturan ini berkala. Kalau ekspresinya benar,",
                    "alert masuk keadaan pending, dan baru jadi firing kalau tetap benar",
                    "selama durasi for. Ini mencegah lonjakan sesaat memanggil orang.",
                    "",
                    "Alert yang firing dikirim ke Alertmanager, komponen terpisah yang",
                    "memutuskan ke mana dan bagaimana alert dikirim:",
                    "",
                    "  - routing: alert severity page ke PagerDuty, sisanya ke kanal Slack",
                    "    atau email.",
                    "  - grouping: lima puluh pod yang gagal bersamaan dikirim sebagai satu",
                    "    notifikasi, bukan lima puluh.",
                    "  - inhibition: kalau alert \"klaster mati\" sedang aktif, alert",
                    "    turunannya ditahan.",
                    "  - silence: membisukan alert sementara, misalnya selama jadwal",
                    "    perawatan.",
                ],
            },
            {
                "heading": "Dasbor Grafana",
                "body": [
                    "Grafana adalah aplikasi dasbor yang membaca data dari banyak sumber:",
                    "Prometheus, Loki, Elasticsearch, database SQL, dan layanan cloud. Saat",
                    "materi ini ditulis, versi terbarunya v13.2.4 (13 Oktober 2026), dengan",
                    "lisensi AGPL-3.0 sejak 2021. Grafana Labs juga menjual Grafana Cloud,",
                    "yang punya paket gratis berkuota.",
                    "",
                    "Satu dasbor terdiri dari panel, dan tiap panel berisi kueri PromQL plus",
                    "pilihan tampilan (grafik garis, angka tunggal, tabel, heatmap). Variabel",
                    "dasbor seperti $namespace atau $pod membuat satu dasbor bisa dipakai",
                    "untuk banyak layanan lewat menu pilihan di atasnya.",
                    "",
                    "Grafana juga bisa membuat alert sendiri. Pilih salah satu tempat alert",
                    "(Prometheus dengan Alertmanager, atau Grafana) supaya aturan nggak",
                    "tersebar di dua tempat. Untuk banyak dasbor, simpan definisinya sebagai",
                    "berkas JSON di Git dan pasang lewat provisioning, supaya dasbor yang",
                    "terhapus bisa dipulihkan.",
                    "",
                    "Ada ribuan dasbor siap pakai di galeri grafana.com, misalnya dasbor Node",
                    "Exporter Full untuk server Linux. Itu titik awal yang baik, tapi dasbor",
                    "terbaik untuk layananmu biasanya dimulai dari empat golden signals di",
                    "materi pertama bab ini.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola yang umum di tim produk adalah satu dasbor per layanan. Baris",
                    "atasnya berisi empat golden signals, baris berikutnya berisi saturasi",
                    "dependensinya (database, cache, antrean), dan tiap alert punya tautan ke",
                    "runbook di deskripsinya. Saat insiden, orang yang jaga membuka dasbor",
                    "itu lebih dulu.",
                    "",
                    "Kasus kecil: grafik permintaan per detik di Grafana tiba-tiba turun",
                    "tajam lalu melonjak lagi tiap kali ada deploy, padahal pengguna nggak",
                    "merasakan apa pun.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek kuerinya. Kalau panel menampilkan nilai mentah",
                    "     http_requests_total, penurunan itu adalah counter yang reset karena",
                    "     pod baru mulai dari nol.",
                    "  2. Ganti kuerinya jadi sum(rate(http_requests_total[5m])) supaya reset",
                    "     ditangani rate().",
                    "  3. Pastikan sum dilakukan sesudah rate, bukan sebelum. rate(sum(...))",
                    "     menjumlahkan counter dari banyak pod dulu, dan reset satu pod",
                    "     terbaca sebagai penurunan besar.",
                    "  4. Simpan dasbor yang sudah benar ke Git sebagai JSON supaya",
                    "     perbaikannya nggak hilang.",
                ],
            },
        ],
    },
    {
        "title": "48. OpenTelemetry: Satu Standar untuk Telemetri",
        "sections": [
            {
                "body": [
                    "Dulu tiap vendor observability punya agen dan pustaka sendiri. Pindah",
                    "dari satu vendor ke vendor lain berarti mengganti kode instrumentasi di",
                    "semua layanan, pekerjaan yang bisa makan berbulan-bulan. Data yang",
                    "dikirim pun beda format, jadi trace dari satu alat nggak bisa dibaca",
                    "alat lain.",
                    "",
                    "OpenTelemetry (sering disingkat OTel) menyelesaikannya dengan satu",
                    "standar terbuka untuk menghasilkan dan mengirim trace, metrik, dan log.",
                    "Proyek ini lahir tahun 2019 dari penggabungan OpenTracing dan",
                    "OpenCensus, berada di bawah CNCF, dan berlisensi Apache-2.0. Menurut",
                    "CNCF, laju kontribusinya kedua tertinggi sesudah Kubernetes. Hampir",
                    "semua vendor besar, dari Datadog sampai layanan cloud, sekarang menerima",
                    "data OpenTelemetry.",
                ],
            },
            {
                "heading": "Bagian-bagiannya",
                "body": [
                    "  - API: antarmuka yang dipanggil kode aplikasi dan pustaka, misalnya",
                    "    \"mulai span bernama checkout\".",
                    "  - SDK: implementasi API di tiap bahasa yang mengumpulkan, mengambil",
                    "    sampel, dan mengirim data. Kematangannya beda per bahasa dan per",
                    "    sinyal, jadi cek halaman status bahasamu.",
                    "  - Protokol bawaan bernama OTLP, lewat gRPC di port 4317 atau HTTP di",
                    "    port 4318.",
                    "  - Collector: program terpisah yang menerima telemetri, mengolahnya,",
                    "    lalu meneruskannya ke satu atau beberapa backend.",
                    "  - Semantic conventions: nama atribut yang disepakati, misalnya",
                    "    http.request.method dan service.name, supaya data dari bahasa",
                    "    berbeda bisa dibandingkan.",
                    "",
                    "Yang paling penting dipahami: OpenTelemetry bukan tempat menyimpan data",
                    "dan nggak punya antarmuka untuk melihatnya. Ia cuma menghasilkan dan",
                    "mengantar. Penyimpanannya tetap Prometheus, Jaeger, Loki, atau vendor",
                    "pilihanmu. Karena itu kamu bisa ganti backend cukup dengan mengubah",
                    "konfigurasi Collector, tanpa menyentuh kode aplikasi.",
                ],
            },
            {
                "heading": "Instrumentasi otomatis untuk Python",
                "bahasa": "terminal",
                "code": """pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install   # pasang instrumentasi pustaka yang terdeteksi

export OTEL_SERVICE_NAME=toko-api
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
opentelemetry-instrument python app.py""",
            },
            {
                "body": [
                    "Instrumentasi otomatis membungkus pustaka populer seperti Flask, Django,",
                    "requests, dan driver database, sehingga span untuk tiap permintaan HTTP",
                    "dan kueri database muncul tanpa mengubah kode. Bahasa lain punya cara",
                    "serupa: agen Java (berkas jar yang dipasang lewat -javaagent), paket",
                    "Node.js, dan operator Kubernetes yang menyuntikkan instrumentasi ke pod.",
                    "",
                    "Untuk langkah yang khusus bisnismu, misalnya \"hitung ongkir\", kamu",
                    "menambah span sendiri lewat API.",
                ],
            },
            {
                "heading": "Span manual dengan SDK",
                "code": """from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

provider = TracerProvider(resource=Resource.create({"service.name": "toko-api"}))
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("toko.checkout")


def cek_stok(produk_id):
    with tracer.start_as_current_span("cek_stok") as span:
        span.set_attribute("produk.id", produk_id)
        return 5


with tracer.start_as_current_span("checkout") as span:
    span.set_attribute("keranjang.jumlah", 2)
    if cek_stok("P001") < 1:
        span.set_status(trace.Status(trace.StatusCode.ERROR, "stok habis"))""",
            },
            {
                "body": [
                    "Contoh ini diuji dengan opentelemetry-sdk 1.45. Ia mencetak dua span",
                    "dalam format JSON ke layar: cek_stok dan checkout. Keduanya punya",
                    "trace_id yang sama, dan parent_id milik cek_stok sama dengan span_id",
                    "milik checkout. Hubungan induk dan anak itu terbentuk sendiri karena",
                    "cek_stok dipanggil di dalam blok with milik checkout. Di produksi,",
                    "ConsoleSpanExporter diganti exporter yang mengirim span ke Collector.",
                ],
            },
            {
                "heading": "Collector: receivers, processors, exporters",
                "bahasa": "yaml",
                "code": """# otelcol.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:                 # kirim per kelompok, hemat koneksi

exporters:
  otlp_grpc/jaeger:
    endpoint: jaeger:4317
    tls:
      insecure: true
  prometheus:            # ada di distribusi contrib
    endpoint: 0.0.0.0:8889
  debug:

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp_grpc/jaeger, debug]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheus]""",
            },
            {
                "body": [
                    "Collector bekerja sebagai pipa: receivers menerima data, processors",
                    "mengolahnya (mengelompokkan, menyaring, menambah atau membuang atribut,",
                    "mengambil sampel), lalu exporters mengirimnya. Satu Collector bisa punya",
                    "beberapa pipa terpisah untuk trace, metrik, dan log. Ia biasa dipasang",
                    "di dua tempat: sebagai agen di tiap node yang dekat dengan aplikasi, dan",
                    "sebagai gateway terpusat sebelum data keluar ke backend.",
                    "",
                    "Collector tersedia dalam beberapa distribusi: core (komponen inti),",
                    "contrib (ratusan komponen tambahan), dan distribusi vendor seperti",
                    "Grafana Alloy. Saat materi ini ditulis, versi Collector adalah v0.163.1",
                    "(16 Oktober 2026). Nomornya masih 0.x walau dipakai luas, jadi baca",
                    "catatan rilis sebelum upgrade karena nama komponen kadang berubah.",
                    "Contohnya, tutorial lama menulis exporter otlp dan otlphttp; di versi",
                    "baru namanya otlp_grpc dan otlp_http, dan otlphttp sudah dinyatakan",
                    "usang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perusahaan yang memakai beberapa backend sekaligus, misalnya Prometheus",
                    "untuk metrik dan vendor SaaS untuk trace, biasanya menaruh Collector di",
                    "tengah. Saat kontrak vendor berganti, yang diubah cuma bagian exporters,",
                    "dan ratusan layanan nggak perlu dirilis ulang.",
                    "",
                    "Kasus kecil: aplikasi Python sudah dijalankan dengan",
                    "opentelemetry-instrument, tapi nggak ada satu trace pun yang muncul di",
                    "Jaeger.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tambahkan exporter debug di pipa traces Collector lalu lihat log",
                    "     Collector. Kalau span muncul di sana, masalahnya di antara",
                    "     Collector dan Jaeger.",
                    "  2. Kalau span nggak sampai ke Collector, cocokkan protokol dan port:",
                    "     http/protobuf harus ke 4318, gRPC ke 4317. Salah pasangan adalah",
                    "     penyebab yang paling sering.",
                    "  3. Pastikan OTEL_SERVICE_NAME terisi supaya trace mudah dicari di",
                    "     Jaeger dan nggak tercatat sebagai unknown_service.",
                    "  4. Kalau masih kosong, jalankan aplikasinya dengan",
                    "     OTEL_TRACES_EXPORTER=console untuk memastikan instrumentasinya",
                    "     memang menghasilkan span.",
                ],
            },
        ],
    },
    {
        "title": "49. Tracing dengan OpenTelemetry dan Jaeger",
        "sections": [
            {
                "body": [
                    "Pengguna mengeluh checkout lambat. Satu permintaan checkout melewati API",
                    "gateway, layanan keranjang, layanan stok, Redis, PostgreSQL, layanan",
                    "pembayaran, dan bank. Metrik bilang \"checkout p95 2 detik\", tapi nggak",
                    "bilang dua detik itu habis di mana. Membaca log tujuh layanan satu per",
                    "satu sambil mencocokkan jam juga melelahkan.",
                    "",
                    "Distributed tracing menjawabnya dengan merekam perjalanan satu",
                    "permintaan sebagai satu trace. Trace terdiri dari span, dan tiap span",
                    "adalah satu langkah kerja dengan waktu mulai dan selesai.",
                ],
            },
            {
                "heading": "Anatomi trace dan span",
                "body": [
                    "Tiap span menyimpan:",
                    "",
                    "  - trace_id: nomor yang sama untuk semua span dalam satu permintaan.",
                    "  - span_id: nomor unik span itu sendiri.",
                    "  - parent span id: span induknya. Span tanpa induk adalah span akar,",
                    "    biasanya permintaan yang pertama masuk.",
                    "  - nama, waktu mulai, dan durasi.",
                    "  - atribut: detail tambahan, misalnya http.request.method atau",
                    "    db.system.",
                    "  - event: kejadian bercap waktu di dalam span, misalnya exception yang",
                    "    dilempar.",
                    "  - status: OK, Error, atau belum diatur.",
                    "",
                    "Karena tiap span tahu induknya, backend bisa menyusun semua span jadi",
                    "pohon dan menggambarnya sebagai diagram air terjun (waterfall): batang",
                    "panjang untuk langkah yang lama, menjorok sesuai kedalamannya.",
                ],
            },
            {
                "heading": "Propagasi konteks",
                "body": [
                    "Bagaimana layanan stok tahu trace_id milik permintaan yang datang dari",
                    "layanan keranjang? Nomornya ikut dikirim di header HTTP. Standar W3C",
                    "Trace Context menetapkan header traceparent, dan SDK OpenTelemetry",
                    "menambahkan serta membacanya secara otomatis. Proses ini disebut",
                    "propagasi konteks. Kalau satu layanan di tengah nggak ikut meneruskan",
                    "header ini, trace-nya putus jadi dua.",
                ],
            },
            {
                "heading": "Membaca header traceparent",
                "code": """# contoh header dari spesifikasi W3C Trace Context
header = "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"

versi, trace_id, parent_id, flags = header.split("-")
print("versi    :", versi)
print("trace-id :", trace_id, f"({len(trace_id)} digit heksadesimal)")
print("parent-id:", parent_id, f"({len(parent_id)} digit heksadesimal)")
print("sampled  :", int(flags, 16) & 1 == 1)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  versi    : 00",
                    "  trace-id : 4bf92f3577b34da6a3ce929d0e0e4736 (32 digit heksadesimal)",
                    "  parent-id: 00f067aa0ba902b7 (16 digit heksadesimal)",
                    "  sampled  : True",
                    "",
                    "Bagian terakhir adalah flag. Bit paling kanan bernama sampled, yang",
                    "memberi tahu layanan berikutnya bahwa trace ini sedang direkam. Dengan",
                    "begitu semua layanan sepakat merekam atau nggak merekam permintaan yang",
                    "sama, dan trace-nya nggak bolong di tengah.",
                ],
            },
            {
                "heading": "Sampling",
                "body": [
                    "Merekam setiap permintaan di layanan yang ramai itu mahal. Ada dua cara",
                    "mengambil sampel:",
                    "",
                    "  - Head sampling: keputusan diambil di awal permintaan, misalnya rekam",
                    "    10% secara acak. Murah dan sederhana, tapi trace yang error atau",
                    "    lambat bisa ikut terbuang karena keputusannya diambil sebelum",
                    "    hasilnya ketahuan.",
                    "  - Tail sampling: semua span dikumpulkan dulu di Collector, lalu",
                    "    keputusan diambil setelah trace selesai, misalnya simpan semua yang",
                    "    error, semua yang lebih dari 1 detik, dan 5% sisanya. Lebih berguna,",
                    "    tapi Collector butuh memori untuk menahan span sampai trace lengkap.",
                ],
            },
            {
                "heading": "Jaeger",
                "body": [
                    "Jaeger adalah sistem distributed tracing open source, proyek CNCF",
                    "graduated, berlisensi Apache-2.0. Saat materi ini ditulis, versi",
                    "terbarunya v2.22.0 (6 Oktober 2026). Jaeger v2 dibangun di atas",
                    "OpenTelemetry Collector, jadi ia langsung menerima data OpenTelemetry.",
                    "Pustaka klien Jaeger yang lama sudah usang; aplikasi diinstrumentasi",
                    "dengan SDK OpenTelemetry. Untuk mencoba di laptop, jalankan image",
                    "all-in-one di bawah lalu buka antarmukanya di localhost:16686.",
                    "",
                    "Alternatif Jaeger yang sering kamu temui adalah Grafana Tempo, yang",
                    "menyimpan trace di object storage dan menyatu dengan dasbor Grafana, dan",
                    "Zipkin, sistem tracing yang lebih tua. Banyak vendor SaaS juga menerima",
                    "trace OpenTelemetry secara langsung.",
                ],
            },
            {
                "heading": "Menjalankan Jaeger di laptop",
                "bahasa": "terminal",
                "code": "docker run --rm --name jaeger \\\n  -p 16686:16686 \\\n  -p 4317:4317 \\\n  -p 4318:4318 \\\n  cr.jaegertracing.io/jaegertracing/jaeger:2.22.0\n\n# di terminal lain: kirim trace dari aplikasi Python\nOTEL_SERVICE_NAME=toko-api \\\nOTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \\\nOTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318 \\\n  opentelemetry-instrument python app.py",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi yang terdiri dari banyak layanan kecil, seperti marketplace",
                    "atau aplikasi pemesanan makanan, hampir mustahil di-debug tanpa tracing.",
                    "Pertanyaan \"kenapa checkout lambat sejak jam sembilan\" biasanya terjawab",
                    "dengan membuka beberapa trace yang lambat dan melihat batang terpanjang",
                    "di diagram air terjunnya.",
                    "",
                    "Kasus kecil: trace checkout berdurasi 250 ms. Di diagram air terjun ada",
                    "auth 15 ms, layanan stok 80 ms, dan layanan bayar 140 ms yang di",
                    "dalamnya memanggil bank 110 ms. Tim stok bersikeras layanan merekalah",
                    "yang perlu dipercepat.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cari jalur kritis, yaitu rangkaian span yang menentukan kapan",
                    "     permintaan selesai. Mulai dari span akar, lalu ikuti anak yang",
                    "     selesai paling akhir.",
                    "  2. Di contoh ini jalurnya checkout, layanan bayar, lalu panggilan",
                    "     bank. Layanan stok selesai jauh lebih awal, jadi mempercepatnya",
                    "     nggak memendekkan checkout.",
                    "  3. Fokuskan perbaikan ke panggilan bank: apakah ada timeout yang",
                    "     terlalu longgar, retry berulang, atau koneksi baru yang dibuat tiap",
                    "     permintaan.",
                    "  4. Bandingkan beberapa trace lambat lain sebelum memutuskan. Satu",
                    "     trace bisa saja kebetulan.",
                ],
            },
        ],
    },
    {
        "title": "50. Log Terpusat: Loki, Alloy, ELK, dan Fluent Bit",
        "sections": [
            {
                "body": [
                    "Di satu server, log dibaca dengan journalctl atau tail. Di klaster",
                    "dengan puluhan pod yang terus berganti, cara itu berhenti bekerja: pod",
                    "yang crash membawa lognya pergi, dan satu permintaan meninggalkan jejak",
                    "di lima pod berbeda. Log terpusat berarti semua log dikirim ke satu",
                    "tempat yang bisa dicari, sambil diberi label asal layanan, pod, dan",
                    "lingkungannya.",
                    "",
                    "Rantainya selalu sama: aplikasi menulis log, pengumpul (collector atau",
                    "agent) di tiap node membacanya, lalu mengirim ke penyimpanan, dan kamu",
                    "mencarinya lewat antarmuka kueri.",
                ],
            },
            {
                "heading": "Log terstruktur",
                "body": [
                    "Aplikasi di container sebaiknya menulis log ke stdout, bukan ke berkas.",
                    "Runtime container menyimpannya dan pengumpul membacanya dari sana.",
                    "Formatnya pun sebaiknya terstruktur, biasanya JSON satu baris per",
                    "kejadian, supaya kolom seperti order_id dan kode bisa disaring tanpa",
                    "regex yang rapuh.",
                ],
            },
            {
                "heading": "Log JSON dengan modul logging",
                "code": """import json
import logging
import sys


class FormatJSON(logging.Formatter):
    def format(self, record):
        data = {"level": record.levelname.lower(),
                "pesan": record.getMessage()}
        data.update(getattr(record, "konteks", {}))
        return json.dumps(data, ensure_ascii=False)


penangan = logging.StreamHandler(sys.stdout)
penangan.setFormatter(FormatJSON())
log = logging.getLogger("toko.checkout")
log.addHandler(penangan)
log.setLevel(logging.INFO)

log.info("pesanan dibuat", extra={"konteks": {"order_id": "A-1001"}})
log.debug("isi keranjang", extra={"konteks": {"order_id": "A-1001"}})
log.error("bayar gagal", extra={"konteks": {"id": "A-1002", "kode": 502}})""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  {\"level\": \"info\", \"pesan\": \"pesanan dibuat\", \"order_id\": \"A-1001\"}",
                    "  {\"level\": \"error\", \"pesan\": \"bayar gagal\", \"id\": \"A-1002\", \"kode\": 502}",
                    "",
                    "Baris debug nggak tercetak karena level logger diset INFO. Di produksi,",
                    "formatter biasanya juga menambahkan waktu dan trace_id. Menyisipkan",
                    "trace_id ke tiap baris log membuat kamu bisa melompat dari trace yang",
                    "lambat ke log persis milik permintaan itu.",
                ],
            },
            {
                "heading": "Grafana Loki dan Alloy",
                "body": [
                    "Grafana Loki adalah sistem log yang sengaja cuma mengindeks label (app,",
                    "namespace, pod), bukan isi lognya. Isi log dikompres dan disimpan di",
                    "object storage seperti S3. Hasilnya jauh lebih murah daripada mengindeks",
                    "setiap kata, dengan ongkos pencarian teks bebas yang lebih lambat. Saat",
                    "materi ini ditulis, versinya v3.7.8, berlisensi AGPL-3.0. Loki ditanya",
                    "dengan LogQL, yang bentuknya mirip PromQL.",
                    "",
                    "Agen pengirim log lama untuk Loki, Promtail, berstatus EOL sejak 2 Maret",
                    "2026: nggak ada pengembangan maupun dukungan lagi. Penggantinya Grafana",
                    "Alloy (v1.20.1, Apache-2.0), kolektor telemetri Grafana yang merupakan",
                    "distribusi OpenTelemetry Collector dan juga menggantikan Grafana Agent.",
                    "Banyak tutorial Loki di internet masih memakai Promtail, jadi waspadai",
                    "tanggal tulisannya. Alloy punya perintah untuk mengubah konfigurasi",
                    "Promtail lama ke formatnya sendiri.",
                ],
            },
            {
                "heading": "LogQL dan migrasi dari Promtail",
                "bahasa": "terminal",
                "code": """# LogQL (diketik di Grafana Explore atau logcli):
#   baris dari toko-api yang memuat 'gagal', diurai JSON, kode >= 500
#   {app="toko-api"} |= "gagal" | json | kode >= 500
#   jumlah baris error per aplikasi dalam 5 menit
#   sum by (app) (count_over_time({namespace="toko"} |= "error" [5m]))

logcli query '{app="toko-api"} |= "gagal" | json | kode >= 500'

# ubah konfigurasi Promtail lama jadi konfigurasi Alloy
alloy convert --source-format=promtail --output=config.alloy promtail.yaml""",
            },
            {
                "heading": "Elastic Stack dan OpenSearch",
                "body": [
                    "Elastic Stack, dulu disebut ELK, terdiri dari Elasticsearch (mesin",
                    "pencari dan penyimpanan), Logstash (pengolah data), Kibana (antarmuka),",
                    "dan Beats (agen pengirim ringan). Elasticsearch mengindeks seluruh isi",
                    "log, jadi pencarian teks bebas dan analisis cepat, dengan ongkos disk",
                    "dan memori yang besar. Ia berjalan di JVM dan terkenal rakus memori.",
                    "Versi terbarunya saat materi ini ditulis Elasticsearch 9.5.5.",
                    "",
                    "Lisensinya pernah berubah. Sejak 2021 Elastic memakai SSPL dan Elastic",
                    "License 2.0, lalu sejak Agustus 2024 menambahkan AGPL-3.0 sebagai",
                    "pilihan. Perubahan 2021 itu memicu AWS membuat fork bernama OpenSearch,",
                    "yang sekarang dikelola di bawah Linux Foundation dengan lisensi",
                    "Apache-2.0. Layanan log terkelola di AWS memakai OpenSearch.",
                ],
            },
            {
                "heading": "Fluent Bit dan pilihan lain",
                "body": [
                    "Fluent Bit adalah pengumpul dan pengirim log yang ringan: membaca log,",
                    "mengurai, menyaring, lalu mengirim ke hampir tujuan apa pun (Loki,",
                    "Elasticsearch, OpenSearch, S3, vendor SaaS). Versinya v5.1.4 (16 Oktober",
                    "2026), Apache-2.0. Fluentd adalah pendahulunya yang lebih tua dan lebih",
                    "berat; untuk pemasangan baru, Fluent Bit yang biasanya dipilih.",
                    "",
                    "  Alat         Jenis                     Lisensi           Catatan",
                    "  Graylog      platform log terpusat     SSPL + komersial  versi 7.2.0",
                    "  OpenObserve  log, metrik, trace hemat  AGPL-3.0          pendatang baru",
                    "  Sumo Logic   log dan SIEM, SaaS        proprietary       pemain ceruk",
                    "  Papertrail   log sederhana, SaaS       proprietary       milik SolarWinds",
                    "",
                    "Jebakan: log tanpa batas retensi. Log debug yang tersimpan selamanya",
                    "adalah salah satu sumber tagihan cloud yang paling sering bikin kaget.",
                    "Tentukan berapa lama tiap jenis log disimpan, misalnya 14 hari untuk log",
                    "aplikasi dan setahun untuk log audit.",
                ],
            },
            {
                "heading": "Fluent Bit mengirim ke Loki",
                "bahasa": "yaml",
                "code": """# fluent-bit.yaml
pipeline:
  inputs:
    - name: tail
      path: /var/log/toko/*.log
      tag: toko
  outputs:
    - name: loki
      match: toko
      host: loki.pantau.svc
      port: 3100
      labels: app=toko-api""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim kecil yang sudah memakai Grafana dan Prometheus sering memilih Loki",
                    "karena murah dan satu antarmuka dengan metrik. Perusahaan yang butuh",
                    "pencarian teks bebas di volume besar, misalnya untuk analisis keamanan,",
                    "lebih sering memakai Elasticsearch, OpenSearch, atau layanan SaaS.",
                    "",
                    "Kasus kecil: kamu mengikuti tutorial Loki dari 2023 yang memasang",
                    "Promtail, lalu rekan setim bilang Promtail sudah nggak didukung.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pastikan statusnya di dokumentasi resmi Loki: Promtail EOL sejak 2",
                    "     Maret 2026 dan semua pengembangan pindah ke Grafana Alloy.",
                    "  2. Ubah berkas konfigurasi Promtail dengan alloy convert",
                    "     --source-format=promtail, lalu baca hasilnya dan rapikan bagian",
                    "     yang diberi peringatan.",
                    "  3. Pasang Alloy berdampingan dengan Promtail sebentar dan bandingkan",
                    "     apakah log yang masuk ke Loki sama lengkapnya.",
                    "  4. Setelah yakin, copot Promtail dan perbarui catatan tim supaya",
                    "     tutorial lama nggak dipakai lagi.",
                ],
            },
        ],
    },
    {
        "title": "51. Peta Observability dan On-Call: Datadog sampai PagerDuty",
        "sections": [
            {
                "body": [
                    "Merakit Prometheus, Loki, Jaeger, dan Grafana sendiri itu gratis",
                    "lisensinya tapi butuh orang untuk merawatnya. Banyak tim memilih layanan",
                    "SaaS yang menggabungkan semua sinyal dalam satu tempat. Materi ini",
                    "memetakan pilihan yang sering kamu temui di lowongan kerja, ditambah",
                    "alat on-call yang memastikan alert sampai ke orang yang tepat.",
                    "",
                    "  Layanan    Fokus                          Lisensi      Status",
                    "  Datadog    metrik, log, APM, RUM          proprietary  aktif",
                    "  Sentry     error tracking, performa       FSL / SaaS   aktif",
                    "  New Relic  APM dan observability          proprietary  stabil-matang",
                    "  Splunk     analitik log dan SIEM          proprietary  aktif",
                    "  Dynatrace  APM perusahaan                 proprietary  aktif",
                    "  Zabbix     pemantauan server, jaringan    AGPL-3.0     stabil-matang",
                    "  Sysdig     pemantauan container           proprietary  aktif",
                    "  Wavefront  metrik (Broadcom)              proprietary  ditutup 2025",
                    "  PagerDuty  on-call dan insiden            proprietary  aktif",
                    "  Opsgenie   on-call (Atlassian)            proprietary  tutup 2027",
                ],
            },
            {
                "heading": "Platform observability SaaS",
                "body": [
                    "Datadog adalah pemimpin observability SaaS: metrik, log, APM",
                    "(application performance monitoring), RUM (pemantauan dari browser",
                    "pengguna), dan pemantauan keamanan dalam satu layanan. Agennya",
                    "berlisensi Apache-2.0, layanannya proprietary; versi agen terbaru saat",
                    "materi ini ditulis 7.84.3. Survei Stack Overflow 2025 mencatat 8,9%",
                    "responden kategori cloud development memakainya. Tagihannya dihitung per",
                    "host, per GB log, dan per metrik kustom, dan bisa membengkak cepat tanpa",
                    "pengawasan.",
                    "",
                    "New Relic adalah platform APM SaaS yang lebih tua, diambil alih",
                    "Francisco Partners dan TPG pada 2023. Pangsanya stabil tapi kecil di",
                    "kalangan pengembang (3,8% di Survei Stack Overflow 2025), dan ia punya",
                    "paket gratis berbasis kuota data.",
                    "",
                    "Dynatrace adalah platform APM perusahaan dengan agen OneAgent yang",
                    "memasang instrumentasi otomatis dan analisis berbasis AI. Splunk kuat di",
                    "analitik log dan SIEM perusahaan, dan diakuisisi Cisco (selesai Maret",
                    "2024); sisi keamanannya dibahas di kurikulum Keamanan Siber. Sysdig",
                    "fokus ke pemantauan dan keamanan container, dan merupakan pencipta",
                    "Falco, proyek CNCF untuk mendeteksi perilaku mencurigakan di container.",
                ],
            },
            {
                "heading": "Sentry dan Zabbix",
                "body": [
                    "Sentry fokus ke error aplikasi. Setiap exception di produksi dikirim",
                    "lengkap dengan stack trace, versi rilis, browser atau perangkat, dan",
                    "langkah pengguna sebelum error. Error yang sama dikelompokkan jadi satu",
                    "masalah, sehingga kamu tahu bug mana yang mengenai paling banyak",
                    "pengguna. Survei Stack Overflow 2026 mencatat 14% responden memakainya",
                    "sebagai alat pengujian kode. Versi self-hosted terbarunya 26.10.0 dengan",
                    "lisensi FSL (Functional Source License), yang berubah jadi Apache-2.0",
                    "atau MIT dua tahun setelah rilis; saat rilis, FSL belum termasuk lisensi",
                    "open source menurut OSI.",
                    "",
                    "Zabbix adalah sistem pemantauan open source tradisional untuk server,",
                    "perangkat jaringan (lewat SNMP), dan aplikasi. Versi terbarunya 7.4.15,",
                    "dengan 7.0 sebagai rilis LTS, dan lisensinya AGPL-3.0 sejak 7.0",
                    "(sebelumnya GPL-2.0). Zabbix masih kuat di pusat data dan jaringan",
                    "kantor; lingkungan cloud-native biasanya memilih Prometheus.",
                ],
            },
            {
                "heading": "Layanan yang sudah atau akan ditutup",
                "body": [
                    "Wavefront (sempat bernama Tanzu Observability) milik VMware dan kemudian",
                    "Broadcom berhenti dijual pada 31 Agustus 2024 dan layanannya ditutup 31",
                    "Oktober 2025. Ia masih tercantum di beberapa roadmap belajar, tapi",
                    "sekarang cuma contoh layanan yang ditutup.",
                    "",
                    "Opsgenie, layanan on-call milik Atlassian, berhenti menerima pelanggan",
                    "baru sejak 4 Juni 2025. Layanannya akan ditutup dan datanya dihapus pada",
                    "5 April 2027, dan pengguna diarahkan pindah ke Jira Service Management",
                    "atau Compass. Kalau tempat kerjamu masih memakai Opsgenie, migrasinya",
                    "perlu direncanakan sebelum tanggal itu.",
                    "",
                    "Kejadian seperti ini alasan banyak tim lebih suka instrumentasi berbasis",
                    "OpenTelemetry: kalau vendornya tutup, yang diganti cuma tujuan kirimnya.",
                ],
            },
            {
                "heading": "On-call dan PagerDuty",
                "body": [
                    "On-call adalah giliran jaga: satu orang (atau beberapa) yang siap",
                    "menanggapi alert di luar jam kerja selama periode tertentu, misalnya",
                    "seminggu. PagerDuty adalah pemimpin kategori ini. Ia menerima alert dari",
                    "Alertmanager, Datadog, atau sumber lain, lalu menjalankan aturan:",
                    "",
                    "  - jadwal: siapa yang jaga minggu ini, termasuk pergantian dan",
                    "    cadangan.",
                    "  - eskalasi: kalau orang pertama nggak merespons dalam, misalnya, 15",
                    "    menit, panggil orang kedua, lalu ketua tim.",
                    "  - pengelompokan dan peredaman: alert yang mirip disatukan supaya",
                    "    ponsel nggak berbunyi puluhan kali.",
                    "",
                    "Alternatif yang sering disebut adalah incident.io dan Jira Service",
                    "Management.",
                    "",
                    "Sesudah insiden selesai, tim yang sehat menulis postmortem tanpa",
                    "menyalahkan orang (blameless): apa yang terjadi, dampaknya, linimasa,",
                    "penyebab, dan tindakan supaya nggak terulang. Fokusnya ke sistem dan",
                    "proses. Pertanyaannya \"kenapa sistem membiarkan satu salah ketik",
                    "menjatuhkan produksi\", bukan \"siapa yang salah ketik\".",
                ],
            },
            {
                "heading": "Merakit sendiri atau SaaS?",
                "body": [
                    "  Pertimbangan               Rakit sendiri          SaaS",
                    "  Biaya lisensi              nol                    per host / per GB",
                    "  Biaya orang                butuh yang merawat     kecil",
                    "  Data keluar perusahaan     nggak                  ya",
                    "  Waktu sampai jalan         hari sampai minggu     jam",
                    "  Risiko vendor tutup/mahal  rendah                 ada",
                    "",
                    "Tim kecil sering mulai dari SaaS dengan paket gratis atau Grafana Cloud,",
                    "lalu memindahkan sebagian ke alat sendiri saat tagihannya mulai terasa.",
                    "Perusahaan yang datanya nggak boleh keluar karena aturan biasanya",
                    "merakit sendiri sejak awal.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan DevOps dan SRE di Indonesia sering mencantumkan kombinasi",
                    "Prometheus dan Grafana untuk metrik, satu sistem log (Loki, ELK, atau",
                    "OpenSearch), Sentry untuk error aplikasi, dan satu alat on-call. Paham",
                    "konsepnya membuat pindah dari satu alat ke alat lain jauh lebih cepat.",
                    "",
                    "Kasus kecil: timmu masih memakai Opsgenie untuk jadwal jaga, dan",
                    "sekarang Oktober 2026.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Catat tanggal pentingnya: layanan ditutup dan data dihapus 5 April",
                    "     2027, jadi masih ada sekitar lima bulan.",
                    "  2. Ekspor jadwal, aturan eskalasi, dan daftar integrasi yang sekarang",
                    "     mengirim alert ke Opsgenie.",
                    "  3. Pilih pengganti, misalnya Jira Service Management yang disarankan",
                    "     Atlassian atau PagerDuty, lalu jalankan keduanya bersamaan selama",
                    "     beberapa minggu.",
                    "  4. Uji eskalasi dengan alert percobaan sebelum mematikan Opsgenie,",
                    "     supaya nggak ada malam ketika alert penting nggak sampai ke siapa",
                    "     pun.",
                ],
            },
        ],
    },
    {
        "title": "52. FinOps: Membaca dan Menekan Tagihan Cloud",
        "sections": [
            {
                "body": [
                    "Cloud ditagih per pemakaian: per jam, per GB, per permintaan. Enaknya,",
                    "kamu bisa mulai tanpa membeli server. Nggak enaknya, nggak ada yang",
                    "menghentikanmu saat pemakaian membengkak. Klaster latihan yang lupa",
                    "dihapus, log debug yang disimpan selamanya, atau satu skrip yang",
                    "mengunduh data berulang-ulang bisa muncul sebagai tagihan ratusan dolar",
                    "di akhir bulan.",
                    "",
                    "FinOps adalah praktik mengelola biaya cloud bersama-sama oleh tim",
                    "teknik, keuangan, dan bisnis. Tujuannya supaya setiap rupiah yang keluar",
                    "bisa dijelaskan: dipakai tim mana, untuk apa, dan apakah sepadan. Hemat",
                    "cuma salah satu hasilnya. FinOps Foundation membagi praktiknya jadi tiga",
                    "fase yang terus berputar: Inform (lihat dan pahami biayanya), Optimize",
                    "(tekan yang boros), dan Operate (jadikan kebiasaan dan aturan).",
                    "",
                    "Masalah ini dialami hampir semua perusahaan. Laporan Flexera State of",
                    "the Cloud 2026 (lebih dari 750 responden) mencatat 85% organisasi",
                    "menyebut mengelola biaya cloud sebagai tantangan, dan 63% sudah punya",
                    "tim FinOps.",
                ],
            },
            {
                "heading": "Langkah pertama: alarm anggaran",
                "body": [
                    "Sebelum membuat apa pun di akun cloud baru, pasang alarm anggaran.",
                    "Ketiga penyedia besar punya alat bawaan yang gratis dipakai: AWS Budgets",
                    "dan Cost Explorer, Google Cloud Billing (budget dan alert), serta Azure",
                    "Cost Management. Kamu menentukan batas, misalnya 50 dolar sebulan, lalu",
                    "meminta email saat pemakaian nyata melewati 80% dan saat prakiraan akhir",
                    "bulan melewati 100%.",
                    "",
                    "Jebakan: mengira alarm anggaran mematikan sumber daya. Alarm cuma",
                    "memberi tahu. Server, database, dan NAT gateway tetap jalan dan tetap",
                    "ditagih sesudah email terkirim. AWS Budgets bisa diberi aksi otomatis,",
                    "misalnya menghentikan instance tertentu, tapi itu harus kamu pasang",
                    "sendiri. Google Cloud juga menyatakan budget nggak membatasi",
                    "pengeluaran; mematikan billing otomatis harus dirakit sendiri lewat",
                    "notifikasi budget.",
                    "",
                    "Notifikasi berbasis prakiraan (forecast) berguna karena datang lebih",
                    "awal. Kalau pemakaian minggu pertama sudah menunjukkan tagihan akhir",
                    "bulan akan tiga kali lipat anggaran, kamu tahu di hari ketujuh, bukan di",
                    "hari ketiga puluh.",
                ],
            },
            {
                "heading": "Membuat budget dengan AWS CLI",
                "bahasa": "terminal",
                "code": "aws budgets create-budget --account-id 111122223333 \\\n  --budget file://anggaran.json \\\n  --notifications-with-subscribers file://notifikasi.json\n\n# biaya harian bulan ini, dipecah per tag 'tim'\naws ce get-cost-and-usage \\\n  --time-period Start=2026-10-01,End=2026-10-19 \\\n  --granularity DAILY --metrics UnblendedCost \\\n  --group-by Type=TAG,Key=tim",
            },
            {
                "heading": "Isi anggaran.json dan notifikasi.json",
                "bahasa": "json",
                "code": """{
  "BudgetName": "lab-bulanan",
  "BudgetLimit": {"Amount": "50", "Unit": "USD"},
  "TimeUnit": "MONTHLY",
  "BudgetType": "COST"
}

[
  {"Notification": {"NotificationType": "ACTUAL",
                    "ComparisonOperator": "GREATER_THAN",
                    "Threshold": 80, "ThresholdType": "PERCENTAGE"},
   "Subscribers": [{"SubscriptionType": "EMAIL", "Address": "kamu@contoh.id"}]},
  {"Notification": {"NotificationType": "FORECASTED",
                    "ComparisonOperator": "GREATER_THAN",
                    "Threshold": 100, "ThresholdType": "PERCENTAGE"},
   "Subscribers": [{"SubscriptionType": "EMAIL", "Address": "kamu@contoh.id"}]}
]""",
            },
            {
                "heading": "Tag: tahu biaya milik siapa",
                "body": [
                    "Tagihan yang cuma bilang \"EC2: 400 dolar\" nggak menolong siapa pun",
                    "mengambil keputusan. Tag adalah label kunci dan nilai yang ditempel ke",
                    "sumber daya, misalnya tim=toko, lingkungan=prod, proyek=checkout. Dengan",
                    "tag, tagihan bisa dipecah per tim dan per lingkungan.",
                    "",
                    "Di AWS, tag buatanmu baru muncul di Cost Explorer setelah diaktifkan",
                    "sebagai cost allocation tag di konsol Billing. Banyak orang rajin",
                    "memasang tag lalu bingung kenapa laporannya kosong. Cara paling aman",
                    "supaya nggak ada yang lupa diberi tag adalah memasangnya otomatis dari",
                    "Terraform, seperti contoh di bawah, lalu menolak pull request yang",
                    "membuat sumber daya tanpa tag wajib.",
                    "",
                    "Sumber daya yang tetap tanpa tag dikumpulkan di satu baris \"tanpa tag\"",
                    "dalam laporan. Kalau baris itu besar, itu tugas pertama yang harus",
                    "dibereskan, karena biaya tanpa pemilik nggak akan pernah ada yang",
                    "menekan.",
                ],
            },
            {
                "heading": "Tag bawaan dari Terraform",
                "bahasa": "hcl",
                "code": """provider "aws" {
  region = "ap-southeast-3"   # Jakarta

  default_tags {
    tags = {
      tim        = "toko"
      lingkungan = "staging"
      dikelola   = "terraform"
    }
  }
}""",
            },
            {
                "heading": "Sumber biaya kejutan",
                "body": [
                    "Biaya yang paling sering bikin kaget jarang datang dari server utama.",
                    "Biasanya datang dari hal kecil yang ditagih terus-menerus:",
                    "",
                    "  - Data keluar (egress): data yang dikirim dari cloud ke internet",
                    "    ditagih per GB, sementara data masuk umumnya gratis.",
                    "  - NAT gateway: ditagih per jam selama ada, ditambah per GB data yang",
                    "    lewat. Server di subnet privat yang mengunduh image besar setiap",
                    "    deploy membayar dua kali.",
                    "  - Alamat IPv4 publik: sejak Februari 2024 AWS menagih setiap alamat",
                    "    IPv4 publik per jam, termasuk yang sedang nggak dipakai.",
                    "  - Log tanpa batas retensi: grup log CloudWatch bawaannya disimpan",
                    "    selamanya kalau retensinya nggak diatur.",
                    "  - Snapshot dan volume yatim: disk dan cadangan dari server yang sudah",
                    "    dihapus tetap ditagih per GB per bulan.",
                    "  - Load balancer dan klaster yang menganggur: tetap ditagih per jam",
                    "    walau nggak ada lalu lintas. EKS juga menagih biaya per klaster per",
                    "    jam.",
                    "  - Lab yang lupa dimatikan: semua yang di atas, berjalan 24 jam sehari.",
                    "",
                    "Program di bawah menghitung tagihan sebulan sebuah lab kecil yang lupa",
                    "dihapus. Harganya contoh yang mendekati harga region us-east-1; angka",
                    "resmi berbeda per region dan bisa berubah, jadi selalu cek halaman harga",
                    "penyedianya.",
                ],
            },
            {
                "heading": "Harga sebuah lab yang lupa dihapus",
                "code": """JAM_SEBULAN = 730   # rata-rata jam dalam sebulan

# harga contoh per jam dalam USD, kira-kira region us-east-1;
# cek lagi di halaman harga resmi sebelum dipakai menghitung
lab = {
    "NAT gateway": 0.045,
    "load balancer": 0.0225,
    "2 alamat IPv4 publik": 2 * 0.005,
    "VM kecil": 0.0208,
}

total = 0
for nama, per_jam in lab.items():
    sebulan = per_jam * JAM_SEBULAN
    total += sebulan
    print(f"{nama:22} ${sebulan:7.2f}")
print(f"{'total lupa dimatikan':22} ${total:7.2f}")
print(f"{'dipakai 10 jam/hari':22} ${total * 10 / 24:7.2f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  NAT gateway            $  32.85",
                    "  load balancer          $  16.43",
                    "  2 alamat IPv4 publik   $   7.30",
                    "  VM kecil               $  15.18",
                    "  total lupa dimatikan   $  71.76",
                    "  dipakai 10 jam/hari    $  29.90",
                    "",
                    "Perhatikan bahwa VM-nya justru bukan yang termahal. NAT gateway dan load",
                    "balancer yang nggak terlihat di layar sehari-hari menyumbang dua pertiga",
                    "tagihan. Lab yang dibuat dan dihapus dengan Terraform tiap selesai",
                    "dipakai menekan tagihannya jadi kurang dari separuh, ditambah biaya data",
                    "yang nggak dihitung di sini.",
                ],
            },
            {
                "heading": "Menekan tagihan",
                "body": [
                    "Setelah tahu biayanya dipakai siapa, baru masuk fase optimasi. Urutan",
                    "yang biasanya paling cepat terasa:",
                    "",
                    "  1. Hapus yang nggak dipakai: volume dan snapshot yatim, load balancer",
                    "     tanpa target, alamat IP menganggur, lingkungan uji yang sudah",
                    "     selesai.",
                    "  2. Sesuaikan ukuran (rightsizing): server yang CPU-nya rata-rata 5%",
                    "     bisa turun satu atau dua ukuran. Data pemakaian di CloudWatch atau",
                    "     Prometheus jadi dasarnya.",
                    "  3. Matikan di luar jam kerja: lingkungan pengembangan yang menyala 10",
                    "     jam sehari, lima hari seminggu, cuma memakai sekitar 30% jam dalam",
                    "     seminggu.",
                    "  4. Atur retensi dan kelas penyimpanan: log aplikasi cukup belasan",
                    "     hari, dan berkas lama di S3 bisa dipindah otomatis ke kelas yang",
                    "     lebih murah lewat lifecycle rule.",
                    "  5. Komitmen untuk beban yang stabil: Savings Plans atau Reserved",
                    "     Instances memberi potongan dengan imbalan janji pemakaian satu atau",
                    "     tiga tahun.",
                    "  6. Spot untuk pekerjaan yang boleh terputus: kapasitas sisa dengan",
                    "     potongan besar, tapi bisa diambil kembali oleh AWS dengan",
                    "     pemberitahuan dua menit. Cocok untuk job batch dan runner CI, bukan",
                    "     untuk database utama.",
                    "",
                    "Ingat: berhemat yang merusak keandalan bukan penghematan. Mematikan",
                    "replika database demi biaya bisa lebih mahal saat terjadi gangguan.",
                    "Putuskan bersama pemilik layanan, dengan SLO dari bab Observability",
                    "sebagai pegangan.",
                ],
            },
            {
                "heading": "Biaya di pull request: Infracost",
                "bahasa": "terminal",
                "code": """# perkiraan biaya bulanan kode Terraform di folder ini
infracost breakdown --path .

# simpan angka branch utama, lalu bandingkan dengan perubahan
infracost breakdown --path . --format json --out-file infracost-base.json
infracost diff --path . --compare-to infracost-base.json""",
            },
            {
                "body": [
                    "Infracost membaca kode Terraform lalu memperkirakan biaya bulanan sumber",
                    "daya di dalamnya. Gunanya paling terasa di pull request: komentar",
                    "otomatis seperti \"perubahan ini menambah sekitar 120 dolar per bulan\"",
                    "muncul sebelum kode digabung, saat mengubahnya masih murah. CLI-nya",
                    "berlisensi Apache-2.0 dan versinya saat materi ini ditulis v0.10.46",
                    "(September 2026), masih bernomor 0.x. Perkiraannya cuma untuk harga yang",
                    "bisa dibaca dari kode; biaya yang bergantung pemakaian, seperti data",
                    "keluar, perlu diberi angka perkiraan sendiri.",
                    "",
                    "Untuk Kubernetes, tagihan cloud cuma bilang berapa biaya node, bukan",
                    "berapa bagian tiap aplikasi. OpenCost, proyek CNCF berlisensi Apache-2.0",
                    "(versi v1.121.3 saat materi ini ditulis), membagi biaya klaster per",
                    "namespace, Deployment, atau label berdasarkan requests CPU dan memori",
                    "tiap pod. Ia juga menunjukkan biaya menganggur, yaitu kapasitas node",
                    "yang dibayar tapi nggak dipesan pod mana pun. Kubecost adalah versi",
                    "komersial yang dibangun di atas OpenCost dan diakuisisi IBM pada 2024.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mahasiswa dan peserta bootcamp yang mencoba cloud dengan kartu kredit",
                    "pribadi sering terkena tagihan dari lab yang lupa dihapus. Karena itu",
                    "banyak panduan resmi penyedia cloud menyarankan langkah pertama di akun",
                    "baru adalah memasang budget alert. Di perusahaan, laporan biaya per tim",
                    "setiap bulan membuat tiap tim merasa memiliki tagihannya sendiri.",
                    "",
                    "Kasus kecil: email AWS Budgets bilang pemakaian bulan ini sudah 80% dari",
                    "anggaran 50 dolar padahal baru tanggal 9, dan kamu cuma ingat membuat",
                    "satu VM kecil untuk latihan.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buka Cost Explorer, pilih bulan ini, dan kelompokkan menurut",
                    "     layanan untuk melihat dari mana biayanya datang.",
                    "  2. Kalau yang terbesar NAT gateway, load balancer, atau EKS, cari sisa",
                    "     lab sebelumnya. Bagian Resource Groups dan Tag Editor bisa",
                    "     menampilkan sumber daya di semua region sekaligus.",
                    "  3. Hapus sumber dayanya, lebih baik lewat terraform destroy kalau dulu",
                    "     dibuat dengan Terraform, supaya nggak ada yang tertinggal.",
                    "  4. Pasang aturan supaya nggak terulang: tag wajib di semua sumber",
                    "     daya, retensi log yang terbatas, dan kebiasaan menghapus lab begitu",
                    "     selesai dipakai.",
                ],
            },
        ],
    },
]
