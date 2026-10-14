"""Peta Karier: profesi yang bisa dicapai dari kurikulum aplikasi ini.

Ini DATA, ditulis tangan. Logikanya (kesiapan, kuis kecocokan, jalur
perpindahan) tinggal di `pelajar/karier.py`, karena kesiapan dihitung dari
progres pelajar dan hanya boleh punya satu definisi.

Aturan isi yang mengikat:

* `bekal` adalah daftar KELOMPOK kurikulum. Kelompok berisi satu kunci berarti
  kurikulum itu wajib; berisi beberapa berarti "salah satu cukup" (misalnya
  backend boleh lewat Python, Java, Go, atau PHP). Setiap kunci wajib ada di
  `LANGUAGES` -- dijaga tests/test_karier.py.
* `gaji` HANYA diisi kalau ada sumber publik yang angkanya terbaca langsung di
  halamannya, lengkap dengan alamat dan tanggal diperiksa. Profesi tanpa
  sumber dibiarkan tanpa gaji: angka tebakan di layar karier lebih merugikan
  pelajar daripada tidak ada angka sama sekali.
* `sertifikasi` boleh kosong. Beberapa bidang (embedded, systems programming,
  technical writing) memang tidak punya sertifikasi yang diakui luas, dan
  mengarang satu demi kelengkapan tabel adalah kebohongan kecil.
* `peta` berisi slug roadmap.sh yang ADA (diperiksa terhadap folder roadmaps
  repo developer-roadmap). Yang ditautkan cuma alamatnya, sesuai lisensinya.
"""

RUMPUN = [
    {"id": "web", "label": "Web", "ket":
        "Membangun apa yang dibuka orang di browser, dan server di baliknya."},
    {"id": "mobile", "label": "Mobile", "ket":
        "Aplikasi di ponsel: layar kecil, baterai terbatas, jaringan putus-sambung."},
    {"id": "data", "label": "Data & AI", "ket":
        "Mengumpulkan, merawat, dan membaca data sampai jadi keputusan atau model."},
    {"id": "infra", "label": "Infrastruktur & DevOps", "ket":
        "Server, cloud, dan otomasi yang membuat kode orang lain tetap hidup."},
    {"id": "sistem", "label": "Sistem, game & desktop", "ket":
        "Dekat dengan mesin: memori, perangkat keras, mesin game, aplikasi desktop."},
    {"id": "mutu", "label": "Mutu & keamanan", "ket":
        "Memastikan perangkat lunak benar, tahan serangan, dan tidak bocor."},
    {"id": "arah", "label": "Arah & kepemimpinan", "ket":
        "Memutuskan bentuk sistem, memimpin tim, dan menuliskannya untuk orang lain."},
]

JENJANG = {
    "pemula": "Bisa dimulai dari nol",
    "menengah": "Biasanya butuh 2-4 tahun pengalaman",
    "senior": "Peran senior",
}

KEAHLIAN = {
    "ui-web": "Antarmuka web", "aksesibilitas": "Aksesibilitas",
    "javascript": "JavaScript & TypeScript", "api-http": "API & HTTP",
    "basis-data": "Basis data & SQL", "arsitektur": "Arsitektur perangkat lunak",
    "pemrograman-sistem": "Pemrograman sistem", "memori-kinerja": "Memori & kinerja",
    "mobile": "Pengembangan mobile", "analisis-data": "Analisis data",
    "statistika": "Statistika", "pipeline-data": "Pipeline data",
    "ml": "Machine learning", "linux": "Linux & shell", "otomasi": "Otomasi & skrip",
    "cloud": "Cloud", "container": "Container & Kubernetes",
    "observability": "Monitoring & observability", "jaringan": "Jaringan",
    "keamanan": "Keamanan aplikasi", "pengujian": "Pengujian",
    "perangkat-keras": "Perangkat keras", "grafis-game": "Grafis & game",
    "desktop": "Aplikasi desktop", "komunikasi": "Komunikasi & dokumentasi",
    "kepemimpinan": "Memimpin tim", "git-kolaborasi": "Git & kolaborasi",
    "desain-sistem": "Desain sistem",
}

_ONET = "https://www.onetonline.org/link/summary/"

PROFESI = [
    # ------------------------------------------------------------------ web
    {
        "id": "frontend-developer", "nama": "Frontend Developer", "rumpun": "web",
        "jenjang": "pemula",
        "ringkas": "Mengubah desain jadi halaman web yang cepat, rapi di semua "
                   "ukuran layar, dan bisa dipakai siapa saja.",
        "harian": [
            "Membangun komponen antarmuka dari desain Figma",
            "Menyambungkan halaman ke API backend dan menangani keadaan muat, kosong, dan galat",
            "Memeriksa tampilan di berbagai browser dan ukuran layar",
            "Memperbaiki masalah aksesibilitas dan kecepatan muat halaman",
            "Meninjau pull request rekan dan menulis tes komponen",
        ],
        "keahlian": ["ui-web", "aksesibilitas", "javascript", "api-http", "git-kolaborasi"],
        "alat": ["VS Code", "Chrome DevTools", "React", "Vue", "Vite", "Figma", "Git"],
        "sertifikasi": [
            {"nama": "Meta Front-End Developer Professional Certificate",
             "penerbit": "Meta lewat Coursera", "tingkat": "pemula"},
            {"nama": "Responsive Web Design Certification", "penerbit": "freeCodeCamp",
             "tingkat": "pemula"},
        ],
        "masuk": "Pintu yang paling sering dilewati pemula: portofolio berisi dua "
                 "atau tiga halaman nyata sering lebih berbicara daripada ijazah.",
        "naik": ["fullstack-developer", "tech-lead"],
        "dekat": ["backend-developer", "android-developer", "qa-engineer"],
        "bekal": [["html"], ["css"], ["javascript"], ["git"]],
        "pelengkap": ["typescript"],
        "proyek": [
            "Halaman portofolio pribadi yang lolos audit Lighthouse di atas 90",
            "Dasbor cuaca yang memanggil API publik tanpa kunci, lengkap dengan keadaan galat",
            "Komponen formulir yang bisa dipakai penuh dengan papan ketik saja",
        ],
        "peta": ["frontend", "frontend-beginner", "javascript", "react"],
        "sumber": [{"judul": "O*NET OnLine: Web Developers (15-1254.00)",
                    "url": _ONET + "15-1254.00"}],
    },
    {
        "id": "backend-developer", "nama": "Backend Developer", "rumpun": "web",
        "jenjang": "pemula",
        "ringkas": "Menulis layanan di sisi server: API, logika bisnis, dan "
                   "penyimpanan data yang dipakai aplikasi web dan mobile.",
        "harian": [
            "Merancang dan menulis endpoint API beserta validasi masukannya",
            "Menulis query dan migrasi basis data",
            "Menulis tes unit dan tes integrasi untuk layanan",
            "Membaca log dan metrik saat ada laporan lambat atau galat",
            "Berdiskusi dengan frontend soal bentuk data yang dikirim",
        ],
        "keahlian": ["api-http", "basis-data", "arsitektur", "pengujian", "git-kolaborasi"],
        "alat": ["Spring Boot", "Django", "FastAPI", "Express", "Laravel", "PostgreSQL",
                 "Redis", "Docker", "Postman"],
        "sertifikasi": [
            {"nama": "Oracle Certified Professional: Java SE 21 Developer (1Z0-830)",
             "penerbit": "Oracle", "tingkat": "menengah"},
            {"nama": "PCAP: Certified Associate Python Programmer",
             "penerbit": "Python Institute", "tingkat": "pemula"},
            {"nama": "AWS Certified Developer - Associate (DVA-C02)",
             "penerbit": "Amazon Web Services", "tingkat": "menengah"},
        ],
        "masuk": "Bisa dimulai dari nol, tapi lowongan junior biasanya meminta satu "
                 "bahasa backend dikuasai sungguh-sungguh plus SQL dan Git.",
        "naik": ["fullstack-developer", "software-architect", "tech-lead"],
        "dekat": ["data-engineer", "devops-engineer", "frontend-developer",
                  "dotnet-developer"],
        "bekal": [["python", "java", "go", "php"], ["sql"], ["git"], ["aplikasi"]],
        "pelengkap": ["bash", "javascript"],
        "proyek": [
            "API daftar tugas dengan autentikasi, paginasi, dan tes otomatis",
            "Layanan pemendek URL yang mencatat jumlah klik per hari",
            "Integrasi pembayaran tiruan dengan webhook dan penanganan kegagalan",
        ],
        "peta": ["backend", "backend-beginner", "api-design", "sql"],
        "sumber": [{"judul": "O*NET OnLine: Software Developers (15-1252.00)",
                    "url": _ONET + "15-1252.00"}],
    },
    {
        "id": "fullstack-developer", "nama": "Full Stack Developer", "rumpun": "web",
        "jenjang": "menengah",
        "ringkas": "Menangani satu fitur dari layar sampai basis data, sering di "
                   "startup atau tim kecil yang butuh orang serba bisa.",
        "harian": [
            "Membangun fitur utuh: tampilan, API, dan skema data",
            "Memutuskan logika mana yang di browser dan mana yang di server",
            "Menyiapkan deploy sederhana dan memantau setelah rilis",
            "Memperbaiki bug yang melintasi batas frontend dan backend",
        ],
        "keahlian": ["ui-web", "javascript", "api-http", "basis-data", "git-kolaborasi"],
        "alat": ["React", "Next.js", "Node.js", "PostgreSQL", "Docker", "Vercel", "Git"],
        "sertifikasi": [
            {"nama": "AWS Certified Developer - Associate (DVA-C02)",
             "penerbit": "Amazon Web Services", "tingkat": "menengah"},
            {"nama": "Full Stack Developer Certification", "penerbit": "freeCodeCamp",
             "tingkat": "pemula"},
        ],
        "masuk": "Jarang jadi pekerjaan pertama. Umumnya dari frontend atau backend "
                 "yang lalu belajar sisi satunya.",
        "naik": ["tech-lead", "software-architect"],
        "dekat": ["frontend-developer", "backend-developer", "devops-engineer"],
        "bekal": [["html"], ["css"], ["javascript"], ["sql"], ["git"],
                  ["python", "java", "go", "php", "typescript"]],
        "pelengkap": ["aplikasi", "bash"],
        "proyek": [
            "Aplikasi catatan dengan login, berbagi, dan pencarian, dari nol sampai online",
            "Toko daring mini: katalog, keranjang, dan halaman admin",
            "Papan kanban waktu nyata dengan WebSocket",
        ],
        "peta": ["full-stack", "frontend", "backend"],
        "sumber": [{"judul": "O*NET OnLine: Web Developers (15-1254.00)",
                    "url": _ONET + "15-1254.00"}],
    },
    # --------------------------------------------------------------- mobile
    {
        "id": "android-developer", "nama": "Android Developer", "rumpun": "mobile",
        "jenjang": "pemula",
        "ringkas": "Membangun aplikasi Android dengan Kotlin: tampilan, data "
                   "lokal, sinkronisasi, dan rilis di Play Store.",
        "harian": [
            "Membangun layar dengan Jetpack Compose",
            "Menyimpan data lokal dan menyinkronkannya saat jaringan kembali",
            "Mengurus izin, notifikasi, dan siklus hidup aplikasi",
            "Menyiapkan build rilis dan membaca laporan crash",
        ],
        "keahlian": ["mobile", "api-http", "arsitektur", "pengujian", "git-kolaborasi"],
        "alat": ["Android Studio", "Kotlin", "Jetpack Compose", "Room", "Retrofit",
                 "Gradle", "Firebase Crashlytics"],
        "sertifikasi": [
            {"nama": "Meta Android Developer Professional Certificate",
             "penerbit": "Meta lewat Coursera", "tingkat": "pemula"},
        ],
        "masuk": "Indonesia pasar Android yang sangat besar, jadi lowongan junior "
                 "cukup banyak. Satu aplikasi yang sungguh terbit di Play Store "
                 "adalah portofolio terkuat.",
        "naik": ["tech-lead", "software-architect"],
        "dekat": ["frontend-developer", "backend-developer", "qa-engineer"],
        "bekal": [["kotlin"], ["java"], ["git"]],
        "pelengkap": ["sql", "aplikasi"],
        "proyek": [
            "Aplikasi pencatat keuangan harian yang tetap jalan tanpa internet",
            "Klien berita yang memuat data dari API publik dengan cache lokal",
            "Aplikasi kecil yang benar-benar terbit di Play Store",
        ],
        "peta": ["android", "kotlin"],
        "sumber": [{"judul": "O*NET OnLine: Software Developers (15-1252.00)",
                    "url": _ONET + "15-1252.00"}],
    },
    # ----------------------------------------------------------------- data
    {
        "id": "data-analyst", "nama": "Data Analyst", "rumpun": "data",
        "jenjang": "pemula",
        "ringkas": "Menjawab pertanyaan bisnis dengan data: menarik, "
                   "membersihkan, menghitung, lalu menceritakannya lewat grafik.",
        "harian": [
            "Menulis query SQL untuk laporan mingguan",
            "Membersihkan data yang berantakan dengan Python atau spreadsheet",
            "Membangun dasbor untuk tim penjualan atau operasional",
            "Menjelaskan temuan ke orang yang tidak membaca angka setiap hari",
        ],
        "keahlian": ["analisis-data", "basis-data", "statistika", "komunikasi"],
        "alat": ["SQL", "Python", "pandas", "Jupyter", "Excel", "Power BI", "Looker Studio"],
        "sertifikasi": [
            {"nama": "Google Data Analytics Professional Certificate",
             "penerbit": "Google lewat Coursera", "tingkat": "pemula"},
            {"nama": "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
             "penerbit": "Microsoft", "tingkat": "menengah"},
        ],
        "masuk": "Banyak yang masuk dari jurusan non-TI. SQL yang kuat dan satu "
                 "laporan analisis yang dipublikasikan sering cukup untuk posisi pertama.",
        "naik": ["data-engineer", "machine-learning-engineer"],
        "dekat": ["database-administrator", "data-engineer"],
        "bekal": [["sql"], ["python"]],
        "pelengkap": ["git"],
        "proyek": [
            "Analisis data terbuka pemerintah (mis. Satu Data Indonesia) lengkap dengan kesimpulan",
            "Dasbor penjualan dari CSV tiruan dengan metrik mingguan",
            "Notebook yang membuktikan atau membantah satu dugaan dengan data",
        ],
        "peta": ["data-analyst", "python-data-analysis", "sql", "power-bi"],
        "sumber": [{"judul": "O*NET OnLine: Business Intelligence Analysts (15-2051.01)",
                    "url": _ONET + "15-2051.01"}],
    },
    {
        "id": "data-engineer", "nama": "Data Engineer", "rumpun": "data",
        "jenjang": "menengah",
        "ringkas": "Membangun pipa yang memindahkan data dari banyak sumber ke "
                   "gudang data, tepat waktu dan bisa dipercaya.",
        "harian": [
            "Menulis pipeline ETL atau ELT yang berjalan terjadwal",
            "Merancang tabel gudang data dan partisinya",
            "Memantau pipeline yang gagal tengah malam dan memperbaikinya",
            "Menulis pemeriksaan mutu data sebelum dipakai analis",
        ],
        "keahlian": ["pipeline-data", "basis-data", "otomasi", "cloud", "linux"],
        "alat": ["Python", "SQL", "Apache Airflow", "dbt", "Apache Spark", "BigQuery",
                 "Kafka", "Docker"],
        "sertifikasi": [
            {"nama": "Google Cloud Professional Data Engineer",
             "penerbit": "Google Cloud", "tingkat": "menengah"},
            {"nama": "Databricks Certified Data Engineer Associate",
             "penerbit": "Databricks", "tingkat": "menengah"},
        ],
        "masuk": "Biasanya dari backend developer atau data analyst yang mulai "
                 "mengurus pipa datanya sendiri.",
        "naik": ["software-architect", "tech-lead"],
        "dekat": ["data-analyst", "backend-developer", "database-administrator",
                  "machine-learning-engineer"],
        "bekal": [["python"], ["sql"], ["bash"], ["git"]],
        "pelengkap": ["fedora", "go", "java"],
        "proyek": [
            "Pipeline harian yang menarik API publik, membersihkannya, dan memuat ke SQLite",
            "Pemeriksa mutu data yang menolak muatan bila kolom wajib kosong",
            "Gudang data mini dengan skema bintang dari data transaksi tiruan",
        ],
        "peta": ["data-engineer", "python", "sql"],
        "sumber": [{"judul": "O*NET OnLine: Data Warehousing Specialists (15-1243.01)",
                    "url": _ONET + "15-1243.01"}],
    },
    {
        "id": "database-administrator", "nama": "Database Administrator",
        "rumpun": "data", "jenjang": "menengah",
        "ringkas": "Menjaga basis data tetap cepat, aman, dan bisa dipulihkan: "
                   "cadangan, indeks, replikasi, dan hak akses.",
        "harian": [
            "Memeriksa query lambat dan menambah indeks yang tepat",
            "Menguji pemulihan dari cadangan, bukan cuma membuat cadangan",
            "Mengatur replikasi dan failover",
            "Meninjau migrasi skema dari tim pengembang sebelum dijalankan",
        ],
        "keahlian": ["basis-data", "linux", "keamanan", "observability"],
        "alat": ["PostgreSQL", "MySQL", "Oracle Database", "SQL Server", "pgBackRest",
                 "Prometheus"],
        "sertifikasi": [
            {"nama": "Oracle Database SQL Certified Associate (1Z0-071)",
             "penerbit": "Oracle", "tingkat": "pemula"},
            {"nama": "Microsoft Certified: Azure Database Administrator Associate (DP-300)",
             "penerbit": "Microsoft", "tingkat": "menengah"},
        ],
        "masuk": "Umumnya dari pengembang atau sysadmin yang paling sering "
                 "menangani basis data di timnya. Banyak dibutuhkan bank dan BUMN.",
        "naik": ["software-architect"],
        "dekat": ["data-engineer", "linux-sysadmin", "backend-developer"],
        "bekal": [["sql"], ["fedora"], ["bash"]],
        "pelengkap": ["python"],
        "proyek": [
            "Skrip cadangan dan uji pemulihan otomatis untuk PostgreSQL",
            "Laporan query paling lambat dari log, dengan usulan indeks",
            "Replikasi primer-sekunder di dua container beserta uji failover",
        ],
        "peta": ["postgresql-dba", "sql"],
        "sumber": [{"judul": "O*NET OnLine: Database Administrators (15-1242.00)",
                    "url": _ONET + "15-1242.00"}],
    },
    {
        "id": "machine-learning-engineer", "nama": "Machine Learning Engineer",
        "rumpun": "data", "jenjang": "menengah",
        "ringkas": "Membawa model machine learning dari notebook ke produksi: "
                   "pelatihan, evaluasi, penyajian, dan pemantauan.",
        "harian": [
            "Menyiapkan data latih dan fitur",
            "Melatih dan mengevaluasi model terhadap metrik bisnis",
            "Menyajikan model lewat API dan memantau mutunya",
            "Menulis pipeline pelatihan ulang yang bisa diulang",
        ],
        "keahlian": ["ml", "statistika", "pipeline-data", "api-http", "cloud"],
        "alat": ["Python", "scikit-learn", "PyTorch", "Jupyter", "MLflow", "Docker",
                 "FastAPI"],
        "sertifikasi": [
            {"nama": "Google Cloud Professional Machine Learning Engineer",
             "penerbit": "Google Cloud", "tingkat": "menengah"},
            {"nama": "AWS Certified Machine Learning Engineer - Associate (MLA-C01)",
             "penerbit": "Amazon Web Services", "tingkat": "menengah"},
        ],
        "masuk": "Butuh dasar matematika (aljabar linear, statistika) di samping "
                 "pemrograman. Sering dari data analyst atau backend developer.",
        "naik": ["software-architect", "tech-lead"],
        "dekat": ["data-engineer", "data-analyst", "backend-developer"],
        "bekal": [["python"], ["sql"], ["git"]],
        "pelengkap": ["bash", "aplikasi"],
        "proyek": [
            "Model klasifikasi sederhana yang disajikan lewat API dan diuji",
            "Perbandingan tiga model pada data publik dengan metrik yang jujur",
            "Pemantau pergeseran data yang memberi peringatan saat distribusi berubah",
        ],
        "peta": ["machine-learning", "mlops", "ai-engineer", "python"],
        "sumber": [{"judul": "O*NET OnLine: Data Scientists (15-2051.00)",
                    "url": _ONET + "15-2051.00"}],
    },
    # ---------------------------------------------------------------- infra
    {
        "id": "linux-sysadmin", "nama": "System Administrator (Linux)",
        "rumpun": "infra", "jenjang": "pemula",
        "ringkas": "Menjaga server Linux tetap hidup, mutakhir, dan aman: "
                   "pengguna, layanan, cadangan, dan pemantauan.",
        "harian": [
            "Memasang pembaruan dan memastikan layanan kembali hidup",
            "Membaca log saat ada laporan gangguan",
            "Mengatur pengguna, izin, dan kunci SSH",
            "Menulis skrip bash untuk pekerjaan yang berulang",
        ],
        "keahlian": ["linux", "otomasi", "jaringan", "keamanan", "observability"],
        "alat": ["Fedora/RHEL", "systemd", "SSH", "bash", "Ansible", "Zabbix", "rsync"],
        "sertifikasi": [
            {"nama": "Red Hat Certified System Administrator (RHCSA, EX200)",
             "penerbit": "Red Hat", "tingkat": "pemula"},
            {"nama": "LPIC-1 Linux Administrator",
             "penerbit": "Linux Professional Institute", "tingkat": "pemula"},
            {"nama": "CompTIA Linux+", "penerbit": "CompTIA", "tingkat": "pemula"},
        ],
        "masuk": "Pintu masuk klasik ke dunia infrastruktur. RHCSA dihargai karena "
                 "ujiannya praktik langsung di mesin, bukan pilihan ganda.",
        "naik": ["devops-engineer", "site-reliability-engineer", "cloud-engineer"],
        "dekat": ["database-administrator", "devops-engineer"],
        "bekal": [["fedora"], ["bash"], ["git"]],
        "pelengkap": ["python"],
        "proyek": [
            "Server rumah dengan layanan systemd buatan sendiri dan pemantauannya",
            "Skrip pengerasan server yang bisa dijalankan ulang tanpa merusak",
            "Cadangan otomatis dengan rotasi dan uji pemulihan",
        ],
        "peta": ["linux", "shell-bash"],
        "sumber": [{"judul": "O*NET OnLine: Network and Computer Systems "
                             "Administrators (15-1244.00)", "url": _ONET + "15-1244.00"}],
    },
    {
        "id": "devops-engineer", "nama": "DevOps Engineer", "rumpun": "infra",
        "jenjang": "menengah",
        "ringkas": "Mengotomasi jalan kode dari commit sampai produksi: CI/CD, "
                   "container, dan infrastruktur yang ditulis sebagai kode.",
        "harian": [
            "Merawat pipeline CI/CD dan mempercepat build",
            "Menulis Dockerfile dan manifest Kubernetes",
            "Menulis infrastruktur sebagai kode dengan Terraform",
            "Membantu tim pengembang men-debug deploy yang gagal",
        ],
        "keahlian": ["otomasi", "container", "cloud", "linux", "git-kolaborasi"],
        "alat": ["GitHub Actions", "GitLab CI", "Docker", "Kubernetes", "Terraform",
                 "Ansible", "Prometheus"],
        "sertifikasi": [
            {"nama": "Certified Kubernetes Administrator (CKA)",
             "penerbit": "Cloud Native Computing Foundation", "tingkat": "menengah"},
            {"nama": "HashiCorp Certified: Terraform Associate",
             "penerbit": "HashiCorp", "tingkat": "menengah"},
            {"nama": "AWS Certified DevOps Engineer - Professional (DOP-C02)",
             "penerbit": "Amazon Web Services", "tingkat": "senior"},
        ],
        "masuk": "Hampir selalu dari sysadmin atau backend developer. Git, Linux, "
                 "dan satu bahasa skrip adalah syarat yang tidak bisa dilewati.",
        "naik": ["site-reliability-engineer", "software-architect", "tech-lead"],
        "dekat": ["linux-sysadmin", "cloud-engineer", "backend-developer"],
        "bekal": [["git"], ["bash"], ["fedora"], ["python", "go"]],
        "pelengkap": ["aplikasi"],
        "proyek": [
            "Pipeline CI yang menjalankan tes, membangun image, dan deploy ke server uji",
            "Lingkungan pengembangan lengkap dengan satu perintah docker compose",
            "Infrastruktur web kecil di cloud yang seluruhnya ditulis dengan Terraform",
        ],
        "peta": ["devops", "devops-beginner", "docker", "kubernetes", "terraform"],
        "sumber": [{"judul": "O*NET OnLine: Computer Systems Engineers/Architects "
                             "(15-1299.08)", "url": _ONET + "15-1299.08"}],
    },
    {
        "id": "site-reliability-engineer", "nama": "Site Reliability Engineer",
        "rumpun": "infra", "jenjang": "menengah",
        "ringkas": "Menjaga layanan besar tetap andal dengan cara seorang "
                   "programmer: target keandalan, otomasi, dan postmortem.",
        "harian": [
            "Menetapkan dan memantau SLO beserta anggaran galatnya",
            "Menulis alat otomasi untuk menghapus pekerjaan manual berulang",
            "Bergiliran jaga dan menangani insiden",
            "Menulis postmortem tanpa menyalahkan orang",
        ],
        "keahlian": ["observability", "otomasi", "container", "linux", "desain-sistem"],
        "alat": ["Prometheus", "Grafana", "OpenTelemetry", "Kubernetes", "Go", "Python",
                 "PagerDuty"],
        "sertifikasi": [
            {"nama": "Certified Kubernetes Administrator (CKA)",
             "penerbit": "Cloud Native Computing Foundation", "tingkat": "menengah"},
            {"nama": "Google Cloud Professional Cloud DevOps Engineer",
             "penerbit": "Google Cloud", "tingkat": "menengah"},
        ],
        "masuk": "Peran yang lahir di perusahaan berskala besar. Di Indonesia "
                 "umumnya ada di e-commerce, fintech, dan perusahaan teknologi besar.",
        "naik": ["software-architect", "tech-lead"],
        "dekat": ["devops-engineer", "cloud-engineer", "backend-developer"],
        "bekal": [["go", "python"], ["bash"], ["fedora"], ["git"]],
        "pelengkap": ["aplikasi"],
        "proyek": [
            "Dasbor SLO untuk layanan kecil lengkap dengan peringatan anggaran galat",
            "Uji beban dan laporan kapasitas satu API",
            "Postmortem tertulis dari kegagalan yang sengaja kamu ciptakan sendiri",
        ],
        "peta": ["devops", "kubernetes", "system-design"],
        "sumber": [{"judul": "Google: Site Reliability Engineering (buku SRE)",
                    "url": "https://sre.google/sre-book/table-of-contents/"}],
    },
    {
        "id": "cloud-engineer", "nama": "Cloud Engineer", "rumpun": "infra",
        "jenjang": "menengah",
        "ringkas": "Merancang dan menjalankan infrastruktur di AWS, Google "
                   "Cloud, atau Azure: jaringan, komputasi, penyimpanan, dan biaya.",
        "harian": [
            "Menyiapkan jaringan virtual, server, dan basis data terkelola",
            "Mengatur hak akses IAM dengan prinsip seminimal mungkin",
            "Memantau dan menekan tagihan cloud bulanan",
            "Memindahkan aplikasi dari server sendiri ke cloud",
        ],
        "keahlian": ["cloud", "jaringan", "otomasi", "keamanan", "linux"],
        "alat": ["AWS", "Google Cloud", "Azure", "Terraform", "AWS CLI", "Kubernetes"],
        "sertifikasi": [
            {"nama": "AWS Certified Solutions Architect - Associate (SAA-C03)",
             "penerbit": "Amazon Web Services", "tingkat": "menengah"},
            {"nama": "Microsoft Certified: Azure Administrator Associate (AZ-104)",
             "penerbit": "Microsoft", "tingkat": "menengah"},
            {"nama": "Google Cloud Associate Cloud Engineer",
             "penerbit": "Google Cloud", "tingkat": "pemula"},
        ],
        "masuk": "Sertifikasi cloud tingkat associate sering jadi syarat formal. "
                 "Tanpa pengalaman Linux dan jaringan, sertifikat itu tidak berdiri sendiri.",
        "naik": ["software-architect", "site-reliability-engineer"],
        "dekat": ["devops-engineer", "linux-sysadmin"],
        "bekal": [["fedora"], ["bash"], ["git"], ["python", "go"]],
        "pelengkap": ["sql"],
        "proyek": [
            "Situs statis dengan CDN dan HTTPS di cloud, seluruhnya dengan Terraform",
            "Laporan biaya bulanan otomatis dari tagihan cloud",
            "Aplikasi tiga lapis dengan jaringan privat dan basis data terkelola",
        ],
        "peta": ["aws", "devops", "terraform"],
        "sumber": [{"judul": "O*NET OnLine: Computer Systems Engineers/Architects "
                             "(15-1299.08)", "url": _ONET + "15-1299.08"}],
    },
    # --------------------------------------------------------------- sistem
    {
        "id": "embedded-engineer", "nama": "Embedded Software Engineer",
        "rumpun": "sistem", "jenjang": "menengah",
        "ringkas": "Menulis perangkat lunak untuk mikrokontroler dan perangkat "
                   "keras: memori yang sempit, waktu yang ketat, tanpa sistem operasi besar.",
        "harian": [
            "Menulis driver untuk sensor dan periferal",
            "Mengukur pemakaian memori dan daya",
            "Men-debug dengan osiloskop dan debugger perangkat keras",
            "Membaca lembar data (datasheet) chip",
        ],
        "keahlian": ["pemrograman-sistem", "memori-kinerja", "perangkat-keras"],
        "alat": ["C", "C++", "GCC ARM", "STM32CubeIDE", "ESP-IDF", "PlatformIO",
                 "logic analyzer"],
        "sertifikasi": [],
        "masuk": "Tidak ada sertifikasi baku yang diakui luas. Proyek nyata di "
                 "papan seperti ESP32 atau STM32 lebih dihargai. Banyak yang "
                 "berlatar teknik elektro.",
        "naik": ["software-architect", "tech-lead"],
        "dekat": ["systems-programmer", "game-programmer"],
        "bekal": [["c"], ["cpp"], ["git"]],
        "pelengkap": ["rust", "bash"],
        "proyek": [
            "Stasiun cuaca ESP32 yang mengirim data ke server kecil",
            "Driver sensor I2C yang ditulis dari membaca datasheet-nya langsung",
            "Firmware hemat daya yang tidur di antara pembacaan",
        ],
        "peta": ["c", "cpp"],
        "sumber": [{"judul": "O*NET OnLine: Software Developers (15-1252.00)",
                    "url": _ONET + "15-1252.00"}],
    },
    {
        "id": "systems-programmer", "nama": "Systems Programmer",
        "rumpun": "sistem", "jenjang": "menengah",
        "ringkas": "Membangun perangkat lunak yang dipakai perangkat lunak lain: "
                   "basis data, runtime, compiler, proxy, dan alat baris perintah.",
        "harian": [
            "Mengoptimalkan jalur kode yang paling panas dengan profiler",
            "Menulis kode konkuren yang benar di bawah beban",
            "Membaca kode sumber proyek open source yang dipakai",
            "Menulis benchmark dan tes properti",
        ],
        "keahlian": ["pemrograman-sistem", "memori-kinerja", "linux", "jaringan"],
        "alat": ["Rust", "C++", "Go", "perf", "gdb", "Valgrind", "Cargo"],
        "sertifikasi": [],
        "masuk": "Kontribusi ke proyek open source sering jadi jalan masuk paling "
                 "jelas, karena kodenya terbuka untuk dinilai siapa pun.",
        "naik": ["software-architect", "tech-lead"],
        "dekat": ["embedded-engineer", "backend-developer", "site-reliability-engineer"],
        "bekal": [["c", "cpp", "rust"], ["go", "rust", "cpp"], ["fedora"], ["git"]],
        "pelengkap": ["bash"],
        "proyek": [
            "Basis data key-value sederhana dengan log tulis-depan",
            "Shell mini dengan pipa dan pengalihan",
            "Server HTTP dari nol di atas socket",
        ],
        "peta": ["rust", "cpp", "computer-science"],
        "sumber": [{"judul": "O*NET OnLine: Software Developers (15-1252.00)",
                    "url": _ONET + "15-1252.00"}],
    },
    {
        "id": "game-programmer", "nama": "Game Programmer", "rumpun": "sistem",
        "jenjang": "menengah",
        "ringkas": "Menulis logika permainan, fisika, kecerdasan musuh, dan "
                   "kinerja grafis di mesin game seperti Unity atau Unreal.",
        "harian": [
            "Menerjemahkan rancangan permainan jadi mekanik yang bisa dimainkan",
            "Mengoptimalkan frame rate di perangkat kelas bawah",
            "Membangun alat bantu untuk desainer level",
            "Memperbaiki bug yang hanya muncul di satu platform",
        ],
        "keahlian": ["grafis-game", "memori-kinerja", "arsitektur"],
        "alat": ["Unity", "C#", "Unreal Engine", "C++", "Godot", "Blender", "RenderDoc"],
        "sertifikasi": [
            {"nama": "Unity Certified Associate: Programmer", "penerbit": "Unity",
             "tingkat": "pemula"},
            {"nama": "Unity Certified Professional: Programmer", "penerbit": "Unity",
             "tingkat": "menengah"},
        ],
        "masuk": "Studio game Indonesia kebanyakan studio kecil. Game jam dan satu "
                 "game kecil yang selesai dan bisa dimainkan adalah portofolio utama.",
        "naik": ["tech-lead"],
        "dekat": ["systems-programmer", "dotnet-developer", "embedded-engineer"],
        "bekal": [["csharp", "cpp"], ["git"]],
        "pelengkap": ["c"],
        "proyek": [
            "Game 2D kecil yang selesai dan bisa diunduh",
            "Prototipe fisika sederhana tanpa mesin game",
            "Entri game jam 48 jam",
        ],
        "peta": ["game-developer", "cpp"],
        "sumber": [{"judul": "O*NET OnLine: Video Game Designers (15-1255.01)",
                    "url": _ONET + "15-1255.01"}],
    },
    {
        "id": "dotnet-developer", "nama": ".NET Developer", "rumpun": "sistem",
        "jenjang": "pemula",
        "ringkas": "Membangun aplikasi bisnis dengan C# dan .NET: web API, "
                   "aplikasi desktop internal, dan integrasi sistem perusahaan.",
        "harian": [
            "Menulis API dengan ASP.NET Core",
            "Merawat aplikasi desktop internal perusahaan",
            "Menulis query dengan Entity Framework dan SQL Server",
            "Mengintegrasikan sistem lama dengan layanan baru",
        ],
        "keahlian": ["api-http", "basis-data", "desktop", "arsitektur"],
        "alat": ["Visual Studio", "C#", "ASP.NET Core", "Entity Framework",
                 "SQL Server", "Azure"],
        "sertifikasi": [
            {"nama": "Microsoft Certified: Azure Developer Associate (AZ-204)",
             "penerbit": "Microsoft", "tingkat": "menengah"},
        ],
        "masuk": "Banyak dicari perusahaan korporat, perbankan, dan instansi "
                 "yang memakai ekosistem Microsoft. Visual Basic masih ditemui di "
                 "sistem lama yang dirawat.",
        "naik": ["software-architect", "tech-lead"],
        "dekat": ["backend-developer", "game-programmer"],
        "bekal": [["csharp"], ["sql"], ["git"]],
        "pelengkap": ["vb", "aplikasi"],
        "proyek": [
            "Web API inventaris dengan ASP.NET Core dan Entity Framework",
            "Aplikasi desktop kecil untuk mengelola data pelanggan",
            "Layanan latar belakang yang menyinkronkan dua sistem",
        ],
        "peta": ["aspnet-core"],
        "sumber": [{"judul": "O*NET OnLine: Software Developers (15-1252.00)",
                    "url": _ONET + "15-1252.00"}],
    },
    # ----------------------------------------------------------------- mutu
    {
        "id": "qa-engineer", "nama": "QA / Test Automation Engineer",
        "rumpun": "mutu", "jenjang": "pemula",
        "ringkas": "Menemukan cacat sebelum pengguna menemukannya: menyusun "
                   "skenario uji dan mengotomasinya.",
        "harian": [
            "Menyusun skenario uji dari kebutuhan fitur",
            "Menulis tes otomatis end-to-end dan tes API",
            "Melaporkan bug dengan langkah reproduksi yang jelas",
            "Menjaga tes otomatis tetap stabil di CI",
        ],
        "keahlian": ["pengujian", "otomasi", "api-http", "komunikasi"],
        "alat": ["Playwright", "Cypress", "Selenium", "Postman", "pytest", "JUnit", "Jira"],
        "sertifikasi": [
            {"nama": "ISTQB Certified Tester Foundation Level (CTFL v4.0)",
             "penerbit": "ISTQB", "tingkat": "pemula"},
            {"nama": "ISTQB Certified Tester Test Automation Engineering",
             "penerbit": "ISTQB", "tingkat": "menengah"},
        ],
        "masuk": "Pintu masuk yang ramah untuk pemula yang teliti. Kemampuan "
                 "menulis kode tes membedakan QA otomasi dari QA manual.",
        "naik": ["tech-lead", "application-security-engineer"],
        "dekat": ["frontend-developer", "backend-developer", "android-developer"],
        "bekal": [["javascript", "python", "java"], ["git"], ["html"]],
        "pelengkap": ["sql", "aplikasi"],
        "proyek": [
            "Rangkaian tes end-to-end untuk aplikasi web contoh dengan Playwright",
            "Koleksi tes API yang berjalan otomatis di CI",
            "Laporan bug yang mendokumentasikan tiga cacat nyata di proyek open source",
        ],
        "peta": ["qa"],
        "sumber": [{"judul": "O*NET OnLine: Software Quality Assurance Analysts "
                             "and Testers (15-1253.00)", "url": _ONET + "15-1253.00"}],
    },
    {
        "id": "application-security-engineer",
        "nama": "Application Security Engineer", "rumpun": "mutu",
        "jenjang": "menengah",
        "ringkas": "Membuat aplikasi sulit dibobol: meninjau kode, menguji "
                   "celah, dan mengajari pengembang menulis kode yang aman.",
        "harian": [
            "Meninjau kode untuk celah seperti injeksi SQL dan XSS",
            "Menjalankan pemindai keamanan di pipeline CI",
            "Menguji aplikasi dari sudut pandang penyerang",
            "Menyusun panduan pemrograman aman untuk tim",
        ],
        "keahlian": ["keamanan", "api-http", "jaringan", "komunikasi"],
        "alat": ["Burp Suite", "OWASP ZAP", "Semgrep", "Trivy", "Wireshark", "Kali Linux"],
        "sertifikasi": [
            {"nama": "CompTIA Security+ (SY0-701)", "penerbit": "CompTIA",
             "tingkat": "pemula"},
            {"nama": "OffSec Web Expert (OSWE)", "penerbit": "OffSec",
             "tingkat": "senior"},
            {"nama": "Certified Secure Software Lifecycle Professional (CSSLP)",
             "penerbit": "ISC2", "tingkat": "senior"},
        ],
        "masuk": "Hampir selalu dari pengembang yang tertarik keamanan. Memahami "
                 "cara aplikasi dibangun adalah syarat untuk memahami cara ia dibobol.",
        "naik": ["software-architect"],
        "dekat": ["backend-developer", "qa-engineer", "devops-engineer"],
        "bekal": [["php", "python", "java", "javascript"], ["sql"], ["fedora"],
                  ["bash"]],
        "pelengkap": ["html", "git"],
        "proyek": [
            "Laporan uji keamanan untuk aplikasi latihan yang sengaja rentan",
            "Aturan Semgrep untuk satu pola celah yang sering muncul",
            "Penulisan ulang aman untuk sebuah endpoint yang rentan injeksi",
        ],
        "peta": ["cyber-security", "devsecops", "api-design"],
        "sumber": [{"judul": "O*NET OnLine: Information Security Analysts (15-1212.00)",
                    "url": _ONET + "15-1212.00"},
                   {"judul": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/"}],
    },
    # ----------------------------------------------------------------- arah
    {
        "id": "software-architect", "nama": "Software Architect", "rumpun": "arah",
        "jenjang": "senior",
        "ringkas": "Memutuskan bentuk besar sebuah sistem dan menuliskan "
                   "alasannya, supaya tim bisa membangunnya tanpa saling bertabrakan.",
        "harian": [
            "Menulis dokumen desain dan Architecture Decision Record",
            "Menimbang pilihan teknologi berdasarkan biaya dan risiko",
            "Meninjau desain dan kode di titik-titik kritis",
            "Menjelaskan konsekuensi teknis ke pemangku kepentingan bisnis",
        ],
        "keahlian": ["arsitektur", "desain-sistem", "komunikasi", "cloud"],
        "alat": ["draw.io", "C4 model", "ADR", "Structurizr", "Terraform"],
        "sertifikasi": [
            {"nama": "AWS Certified Solutions Architect - Professional (SAP-C02)",
             "penerbit": "Amazon Web Services", "tingkat": "senior"},
            {"nama": "iSAQB Certified Professional for Software Architecture "
                     "- Foundation Level (CPSA-F)", "penerbit": "iSAQB",
             "tingkat": "menengah"},
            {"nama": "TOGAF Enterprise Architecture Foundation",
             "penerbit": "The Open Group", "tingkat": "menengah"},
        ],
        "masuk": "Hampir selalu lewat promosi dari pengembang senior yang sudah "
                 "pernah merasakan sendiri akibat keputusan desain yang buruk.",
        "naik": ["tech-lead"],
        "dekat": ["tech-lead", "backend-developer", "cloud-engineer"],
        "bekal": [["aplikasi"], ["java", "python", "go", "csharp"], ["sql"], ["git"]],
        "pelengkap": ["bash", "fedora"],
        "proyek": [
            "Dokumen desain sistem pemesanan tiket, lengkap dengan alternatif yang ditolak",
            "Tiga ADR untuk keputusan nyata di proyekmu sendiri",
            "Diagram C4 untuk aplikasi yang sudah kamu bangun",
        ],
        "peta": ["software-architect", "software-design-architecture", "system-design"],
        "sumber": [{"judul": "O*NET OnLine: Computer Systems Engineers/Architects "
                             "(15-1299.08)", "url": _ONET + "15-1299.08"}],
    },
    {
        "id": "tech-lead", "nama": "Tech Lead / Engineering Manager",
        "rumpun": "arah", "jenjang": "senior",
        "ringkas": "Memimpin tim pengembang: arah teknis, pembagian kerja, "
                   "tinjauan kode, dan pertumbuhan tiap anggotanya.",
        "harian": [
            "Memecah rencana produk jadi pekerjaan yang bisa dikerjakan tim",
            "Meninjau kode dan keputusan teknis penting",
            "Satu-satu dengan anggota tim",
            "Menjaga keseimbangan antara fitur baru dan utang teknis",
        ],
        "keahlian": ["kepemimpinan", "komunikasi", "arsitektur", "git-kolaborasi"],
        "alat": ["Jira", "Linear", "GitHub", "Notion", "Slack"],
        "sertifikasi": [
            {"nama": "Professional Scrum Master I (PSM I)", "penerbit": "Scrum.org",
             "tingkat": "menengah"},
        ],
        "masuk": "Lewat promosi. Yang dinilai bukan kode terbaik, melainkan apakah "
                 "tim di sekitarmu jadi lebih produktif.",
        "naik": [],
        "dekat": ["software-architect", "fullstack-developer", "backend-developer"],
        "bekal": [["git"], ["aplikasi"], ["java", "python", "go", "javascript"]],
        "pelengkap": ["sql"],
        "proyek": [
            "Panduan kontribusi dan template pull request untuk proyek tim",
            "Rencana onboarding dua minggu untuk anggota baru",
            "Retrospektif tertulis dari satu proyek yang kamu pimpin",
        ],
        "peta": ["engineering-manager", "code-review"],
        "sumber": [{"judul": "O*NET OnLine: Computer and Information Systems "
                             "Managers (11-3021.00)", "url": _ONET + "11-3021.00"}],
    },
    {
        "id": "technical-writer", "nama": "Technical Writer", "rumpun": "arah",
        "jenjang": "pemula",
        "ringkas": "Menulis dokumentasi yang membuat orang berhasil memakai "
                   "perangkat lunak: panduan, rujukan API, dan tutorial.",
        "harian": [
            "Mewawancarai pengembang soal fitur baru",
            "Menulis dan menguji tutorial langkah demi langkah",
            "Merawat rujukan API agar sama dengan kodenya",
            "Menulis dokumentasi dalam Markdown di repositori Git",
        ],
        "keahlian": ["komunikasi", "git-kolaborasi", "api-http"],
        "alat": ["Markdown", "Git", "Docusaurus", "MkDocs", "OpenAPI", "Vale"],
        "sertifikasi": [],
        "masuk": "Tidak ada sertifikasi baku. Contoh tulisan dokumentasi yang "
                 "dipublikasikan, misalnya kontribusi ke dokumentasi open source, "
                 "adalah bukti terkuat.",
        "naik": ["tech-lead"],
        "dekat": ["qa-engineer", "frontend-developer"],
        "bekal": [["git"], ["html"], ["python", "javascript"]],
        "pelengkap": ["bash"],
        "proyek": [
            "Tutorial pemula untuk alat open source favoritmu",
            "Rujukan API yang dibuat dari spesifikasi OpenAPI",
            "Perbaikan dokumentasi yang diterima di proyek open source",
        ],
        "peta": ["technical-writer", "devrel"],
        "sumber": [{"judul": "O*NET OnLine: Technical Writers (27-3042.00)",
                    "url": _ONET + "27-3042.00"}],
    },
]

# Kuis kecocokan. Tiap opsi memberi bobot ke KEAHLIAN; skor profesi adalah
# jumlah bobot keahliannya, dinormalkan dengan akar jumlah keahliannya supaya
# profesi dengan daftar keahlian panjang tidak otomatis menang.
KUIS = [
    {"q": "Bagian mana dari pembuatan aplikasi yang paling membuatmu penasaran?",
     "opsi": [
         {"label": "Tampilan yang dilihat dan disentuh orang",
          "bobot": {"ui-web": 3, "aksesibilitas": 2, "mobile": 1}},
         {"label": "Logika dan data di balik layar",
          "bobot": {"api-http": 3, "basis-data": 2, "arsitektur": 1}},
         {"label": "Mesin di bawahnya: memori, kinerja, perangkat keras",
          "bobot": {"pemrograman-sistem": 3, "memori-kinerja": 2}},
         {"label": "Server dan otomasi yang membuat semuanya tetap hidup",
          "bobot": {"linux": 2, "otomasi": 3, "container": 2}},
     ]},
    {"q": "Kamu paling puas ketika...", "opsi": [
        {"label": "Grafik membuktikan dugaanku benar atau salah",
         "bobot": {"analisis-data": 3, "statistika": 3}},
        {"label": "Sesuatu yang kubuat dipakai banyak orang tanpa keluhan",
         "bobot": {"ui-web": 2, "mobile": 2, "pengujian": 1}},
        {"label": "Aku menemukan celah yang orang lain lewatkan",
         "bobot": {"keamanan": 3, "pengujian": 2}},
        {"label": "Pekerjaan berulang hilang karena skrip yang kutulis",
         "bobot": {"otomasi": 3, "linux": 1, "pipeline-data": 1}},
    ]},
    {"q": "Jam dua pagi ada yang rusak. Peran apa yang paling kamu nikmati?", "opsi": [
        {"label": "Membaca log dan grafik sampai ketemu sebabnya",
         "bobot": {"observability": 3, "linux": 2}},
        {"label": "Memastikan data tidak hilang dan bisa dipulihkan",
         "bobot": {"basis-data": 3, "pipeline-data": 1}},
        {"label": "Memastikan celahnya tertutup dan tidak terulang",
         "bobot": {"keamanan": 3}},
        {"label": "Menjelaskan apa yang terjadi kepada semua orang",
         "bobot": {"komunikasi": 3, "kepemimpinan": 2}},
    ]},
    {"q": "Mana yang paling ingin kamu bangun tahun depan?", "opsi": [
        {"label": "Aplikasi Android yang terbit di Play Store",
         "bobot": {"mobile": 3, "api-http": 1}},
        {"label": "Game kecil yang bisa dimainkan teman-teman",
         "bobot": {"grafis-game": 3, "memori-kinerja": 1}},
        {"label": "Model yang menebak sesuatu dari data",
         "bobot": {"ml": 3, "statistika": 2, "analisis-data": 1}},
        {"label": "Alat yang terhubung ke sensor dan perangkat keras",
         "bobot": {"perangkat-keras": 3, "pemrograman-sistem": 2}},
    ]},
    {"q": "Bagaimana kamu paling suka bekerja dengan orang lain?", "opsi": [
        {"label": "Memimpin dan membagi pekerjaan",
         "bobot": {"kepemimpinan": 3, "komunikasi": 1}},
        {"label": "Menuliskan sesuatu sampai orang lain paham",
         "bobot": {"komunikasi": 3, "git-kolaborasi": 1}},
        {"label": "Fokus sendiri lalu menyerahkan hasil yang rapi",
         "bobot": {"pemrograman-sistem": 1, "arsitektur": 1, "memori-kinerja": 1}},
        {"label": "Meninjau pekerjaan orang dan menemukan masalahnya",
         "bobot": {"pengujian": 3, "keamanan": 1, "git-kolaborasi": 1}},
    ]},
    {"q": "Dokumen mana yang paling tidak membuatmu bosan?", "opsi": [
        {"label": "Diagram arsitektur dan alasan di balik keputusan",
         "bobot": {"arsitektur": 3, "desain-sistem": 3}},
        {"label": "Spesifikasi API dan contoh permintaannya",
         "bobot": {"api-http": 3, "komunikasi": 1}},
        {"label": "Datasheet chip dan diagram pewaktuan",
         "bobot": {"perangkat-keras": 3}},
        {"label": "Konfigurasi server dan berkas pipeline",
         "bobot": {"container": 2, "cloud": 2, "otomasi": 1}},
    ]},
]


# Gaji bulanan, diperiksa 2026-10-14. HANYA halaman yang memang untuk peran
# itu; angka dari halaman "pendekatan" (QA yang bercampur QA pabrik, game
# developer yang bercampur artis, tech lead lewat IT manager, systems
# programmer lewat software engineer umum) sengaja tidak dipakai, begitu juga
# rentang technical writer di Indeed (Rp 1,57-25,7 juta dari 22 laporan) yang
# terlalu lebar untuk berarti apa pun. Angka Jobstreet adalah kisaran rata-rata
# dari iklan lowongan, bukan survei gaji karyawan.
_JS = "https://id.jobstreet.com/id/career-advice/role/"
GAJI = {
    "frontend-developer": ("Rp 6,25 juta - Rp 9,13 juta", "Jobstreet Indonesia, Gaji Front End Developer (Oktober 2026)", _JS + "frontend-developer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "backend-developer": ("Rp 6,25 juta - Rp 8,5 juta", "Jobstreet Indonesia, Gaji Backend Developer (Oktober 2026)", _JS + "backend-developer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "fullstack-developer": ("Rp 6 juta - Rp 9 juta", "Jobstreet Indonesia, Gaji Full Stack Developer (Oktober 2026)", _JS + "full-stack-developer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "android-developer": ("Rp 7 juta - Rp 10 juta", "Jobstreet Indonesia, Gaji Android Developer (Oktober 2026)", _JS + "android-developer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "data-analyst": ("Rp 5 juta - Rp 7,94 juta", "Jobstreet Indonesia, Gaji Analis Data (Oktober 2026)", _JS + "data-analyst/salary", "Kisaran rata-rata dari iklan lowongan."),
    "data-engineer": ("Rp 8,65 juta - Rp 11,65 juta", "Jobstreet Indonesia, Gaji Data Engineer (Oktober 2026)", _JS + "data-engineer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "database-administrator": ("Rp 6,07 juta - Rp 18,97 juta", "Indeed Indonesia, Gaji Database Administrator (diperbarui 5 September 2026)", "https://id.indeed.com/career/database-administrator/salaries", "Hanya 22 laporan gaji; rata-ratanya Rp 10,73 juta."),
    "linux-sysadmin": ("Rp 4,75 juta - Rp 6,4 juta", "Jobstreet Indonesia, Gaji Admin Sistem (Oktober 2026)", _JS + "systems-administrator/salary", "Untuk admin sistem secara umum, tidak khusus Linux."),
    "devops-engineer": ("Rp 7,06 juta - Rp 8,88 juta", "Jobstreet Indonesia, Gaji DevOps Engineer (Oktober 2026)", _JS + "devops-engineer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "dotnet-developer": ("Rp 8 juta - Rp 11 juta", "Jobstreet Indonesia, Gaji .Net Developer (Oktober 2026)", _JS + "dot-net-software-developer/salary", "Kisaran rata-rata dari iklan lowongan."),
    "software-architect": ("Rp 21,38 juta - Rp 23,63 juta", "Jobstreet Indonesia, Gaji Software Architect (Oktober 2026)", _JS + "software-architect/salary", "Kisaran rata-rata dari iklan lowongan."),
}

for _p in PROFESI:
    if _p["id"] in GAJI:
        _rentang, _sumber, _url, _konteks = GAJI[_p["id"]]
        _p["gaji"] = {"rentang": _rentang + " per bulan", "sumber": _sumber,
                      "url": _url, "konteks": _konteks, "diperiksa": "2026-10-14"}
