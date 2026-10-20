"""Gambar konsep kurikulum DevOps & Cloud. Skema: inti/visual.py."""

VISUAL = {
    "Apa Itu DevOps, SRE, dan Metrik DORA": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Siklus DevOps yang terus berputar",
            "ket": "Hasil langkah monitor jadi bahan langkah plan berikutnya.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Plan",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Code (simpan di Git)",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Build",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Tes otomatis lulus?",
                    "ya": 4,
                    "tidak": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Release",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "Deploy",
                    "ke": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "Operate",
                    "ke": 7,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Monitor",
                    "ke": 0,
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Empat metrik DORA",
            "ket": "Dua mengukur kecepatan, dua mengukur kestabilan.",
            "tabel": [
                {
                    "kolom": [
                        "Metrik",
                        "Mengukur",
                        "Contoh",
                    ],
                    "baris": [
                        [
                            "Deploy frequency",
                            "kecepatan",
                            "4 per minggu",
                        ],
                        [
                            "Lead time",
                            "kecepatan",
                            "110 menit",
                        ],
                        [
                            "Change fail rate",
                            "kestabilan",
                            "25%",
                        ],
                        [
                            "Recovery time",
                            "kestabilan",
                            "37,5 menit",
                        ],
                    ],
                },
            ],
        },
    ],
    "Linux Server, SSH, dan Firewall untuk DevOps": [
        {
            "setelah": 7,
            "jenis": "urutan",
            "judul": "Login SSH dengan pasangan kunci",
            "ket": "Kunci privat nggak pernah meninggalkan laptop; yang dikirim cuma tanda tangannya.",
            "pelaku": [
                "laptop",
                "server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "halo, aku budi",
                ],
                [
                    1,
                    0,
                    "kunci publik ada, ini tantangan",
                ],
                [
                    0,
                    1,
                    "tantangan ditandatangani privat",
                ],
                [
                    1,
                    0,
                    "tanda tangan cocok, silakan",
                ],
            ],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Distro server dan statusnya",
            "ket": "Versi terbaru saat materi ditulis, Oktober 2026.",
            "tabel": [
                {
                    "kolom": [
                        "Sistem",
                        "Versi",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Ubuntu Server",
                            "26.04.1 LTS",
                            "aktif",
                        ],
                        [
                            "Debian",
                            "13.7",
                            "aktif",
                        ],
                        [
                            "Red Hat (RHEL)",
                            "10.2",
                            "aktif",
                        ],
                        [
                            "Windows Server",
                            "2025",
                            "aktif",
                        ],
                        [
                            "FreeBSD",
                            "15.1",
                            "aktif",
                        ],
                        [
                            "Solaris",
                            "-",
                            "menurun",
                        ],
                    ],
                },
            ],
        },
    ],
    "YAML, Bahasa Konfigurasi Alat DevOps": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Struktur dokumen YAML di atas",
            "ket": "Indentasi menentukan siapa anak siapa. Daftar ditandai [0], [1].",
            "akar": {
                "teks": "dokumen",
                "anak": [
                    {
                        "teks": "aplikasi: toko",
                    },
                    {
                        "teks": "versi: \"1.10\"",
                    },
                    {
                        "teks": "server",
                        "anak": [
                            {
                                "teks": "host: 0.0.0.0",
                            },
                            {
                                "teks": "port: 8080",
                            },
                        ],
                    },
                    {
                        "teks": "fitur",
                        "anak": [
                            {
                                "teks": "[0] keranjang",
                            },
                            {
                                "teks": "[1] pembayaran",
                            },
                        ],
                    },
                    {
                        "teks": "admin",
                        "anak": [
                            {
                                "teks": "[0]",
                                "anak": [
                                    {
                                        "teks": "nama: budi",
                                    },
                                    {
                                        "teks": "email",
                                    },
                                ],
                            },
                            {
                                "teks": "[1]",
                                "anak": [
                                    {
                                        "teks": "nama: sari",
                                    },
                                    {
                                        "teks": "email",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "pesan_sambutan",
                    },
                ],
            },
        },
    ],
    "Protokol Jaringan, Port, dan Alat Diagnosis": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "judul": "Empat lapisan model TCP/IP",
            "ket": "Data turun dari lapisan aplikasi ke kabel, lalu naik lagi di mesin tujuan.",
            "isi": [
                "Aplikasi: HTTP",
                "Transport: TCP/UDP",
                "Internet: IP",
                "Akses: Ethernet",
            ],
            "label": "lapisan",
        },
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Satu permintaan HTTP di atas TCP",
            "ket": "Jabat tangan TCP dulu, baru permintaan HTTP dikirim.",
            "pelaku": [
                "curl",
                "server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "SYN (mau sambung)",
                ],
                [
                    1,
                    0,
                    "SYN-ACK (boleh)",
                ],
                [
                    0,
                    1,
                    "ACK, lalu GET /produk",
                ],
                [
                    1,
                    0,
                    "HTTP/1.1 200 OK",
                ],
            ],
        },
    ],
    "DNS: Dari Nama Domain ke Alamat IP": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Resolver mencari alamat toko.id",
            "ket": "Pertanyaan ke root, .id, dan server otoritatif cuma terjadi saat cache kosong.",
            "pelaku": [
                "laptop",
                "resolver",
                "root & .id",
                "otoritatif",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "toko.id alamatnya?",
                ],
                [
                    1,
                    2,
                    "siapa pegang .id lalu toko.id?",
                ],
                [
                    2,
                    1,
                    "tanya ns1.penyedia.net",
                ],
                [
                    1,
                    3,
                    "toko.id A?",
                ],
                [
                    3,
                    1,
                    "203.0.113.10, TTL 3600",
                ],
                [
                    1,
                    0,
                    "203.0.113.10 (disimpan)",
                ],
            ],
        },
    ],
    "Nginx: Web Server dan Reverse Proxy": [
        {
            "setelah": 6,
            "jenis": "urutan",
            "judul": "Nginx sebagai reverse proxy",
            "ket": "Berkas statis dijawab Nginx sendiri; sisanya diteruskan ke aplikasi.",
            "pelaku": [
                "browser",
                "Nginx :80",
                "aplikasi :8000",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /static/gaya.css",
                ],
                [
                    1,
                    0,
                    "200, dari disk",
                ],
                [
                    0,
                    1,
                    "GET /produk",
                ],
                [
                    1,
                    2,
                    "GET /produk + X-Forwarded-For",
                ],
                [
                    2,
                    1,
                    "200 HTML",
                ],
                [
                    1,
                    0,
                    "200 HTML",
                ],
            ],
        },
    ],
    "Nginx Lanjutan: HTTPS, location, dan Load Balancing": [
        {
            "setelah": 8,
            "jenis": "tabel",
            "judul": "Prioritas location di Nginx",
            "ket": "Persis dulu, lalu awalan ^~ terpanjang, lalu regex urut berkas, lalu awalan terpanjang.",
            "tabel": [
                {
                    "kolom": [
                        "Urutan",
                        "Bentuk",
                        "Cara menang",
                    ],
                    "baris": [
                        [
                            "1",
                            "= /x",
                            "persis sama",
                        ],
                        [
                            "2",
                            "^~ /x/",
                            "terpanjang",
                        ],
                        [
                            "3",
                            "~ dan ~*",
                            "regex pertama",
                        ],
                        [
                            "4",
                            "/x/",
                            "terpanjang",
                        ],
                    ],
                },
            ],
        },
        {
            "setelah": 12,
            "jenis": "larik",
            "nama": "giliran",
            "judul": "Tujuh giliran dengan bobot 5, 1, 1",
            "ket": "app2 dan app3 diselipkan di tengah, bukan di akhir.",
            "isi": [
                "app1",
                "app1",
                "app2",
                "app1",
                "app3",
                "app1",
                "app1",
            ],
            "sorot": [2, 4],
        },
    ],
    "Peta Web Server, VPN, dan Email untuk Server": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Web server dan reverse proxy",
            "ket": "Status per Oktober 2026.",
            "tabel": [
                {
                    "kolom": [
                        "Nama",
                        "Kekuatan",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Nginx",
                            "statis + proxy",
                            "aktif",
                        ],
                        [
                            "Apache",
                            ".htaccess, PHP",
                            "stabil-matang",
                        ],
                        [
                            "Caddy",
                            "HTTPS otomatis",
                            "aktif",
                        ],
                        [
                            "Traefik",
                            "label container",
                            "aktif",
                        ],
                        [
                            "HAProxy",
                            "load balancer",
                            "aktif",
                        ],
                        [
                            "IIS",
                            "ASP.NET lama",
                            "menurun",
                        ],
                    ],
                },
            ],
        },
    ],
    "Container dan Image: Kenapa Docker Ada": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "Mesin virtual: tiap VM bawa kernel sendiri",
            "ket": "Dibaca dari atas ke bawah: aplikasi di puncak, perangkat keras di dasar.",
            "isi": [
                "aplikasi",
                "pustaka",
                "kernel tamu",
                "hypervisor",
                "kernel host",
                "perangkat keras",
            ],
            "label": "VM",
        },
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "Container: berbagi kernel host",
            "ket": "Nggak ada kernel tamu, jadi container nyala dalam hitungan detik.",
            "isi": [
                "aplikasi",
                "pustaka",
                "Docker Engine",
                "kernel host",
                "perangkat keras",
            ],
            "label": "container",
        },
    ],
    "Dockerfile dan Cache Layer": [
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "Layer image toko:1.0",
            "ket": "Layer paling bawah paling jarang berubah. Satu layer batal, semua di atasnya ikut dibangun ulang.",
            "isi": [
                "COPY . .",
                "RUN pip install",
                "COPY requirements",
                "WORKDIR /app",
                "python:3.14-slim",
            ],
            "label": "layer",
            "operasi": "app.py berubah",
        },
    ],
    "Volume, Jaringan, dan Image Docker yang Aman": [
        {
            "setelah": 5,
            "jenis": "urutan",
            "judul": "Container saling memanggil lewat nama",
            "ket": "DNS bawaan jaringan buatan sendiri menerjemahkan nama container ke alamat IP-nya.",
            "pelaku": [
                "web",
                "DNS Docker",
                "db",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "alamat db?",
                ],
                [
                    1,
                    0,
                    "172.18.0.2",
                ],
                [
                    0,
                    2,
                    "koneksi ke 172.18.0.2:5432",
                ],
                [
                    2,
                    0,
                    "hasil query",
                ],
            ],
        },
    ],
    "Docker Compose: Banyak Container dalam Satu Berkas": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Isi compose.yaml",
            "ket": "Tiga layanan dan satu volume. Jaringan dibuat Compose sendiri.",
            "akar": {
                "teks": "compose.yaml",
                "anak": [
                    {
                        "teks": "services",
                        "anak": [
                            {
                                "teks": "web",
                                "anak": [
                                    {
                                        "teks": "build: .",
                                    },
                                    {
                                        "teks": "ports 8000",
                                    },
                                    {
                                        "teks": "depends_on",
                                    },
                                ],
                            },
                            {
                                "teks": "db",
                                "anak": [
                                    {
                                        "teks": "postgres:17",
                                    },
                                    {
                                        "teks": "pgdata",
                                    },
                                ],
                            },
                            {
                                "teks": "cache",
                                "anak": [
                                    {
                                        "teks": "redis:8",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "volumes",
                        "anak": [
                            {
                                "teks": "pgdata",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Compose Lanjutan: Healthcheck, Variabel, dan Profil": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "web menunggu db sehat dan migrasi selesai",
            "ket": "Kegagalan selama start_period nggak dihitung.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "docker compose up -d",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "nyalakan db",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "pg_isready lulus?",
                    "ya": 4,
                    "tidak": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "tunggu 5 detik",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "jalankan migrasi",
                    "ke": 5,
                },
                {
                    "jenis": "keputusan",
                    "teks": "migrasi keluar dengan 0?",
                    "ya": 6,
                    "tidak": 7,
                },
                {
                    "jenis": "selesai",
                    "teks": "nyalakan web",
                },
                {
                    "jenis": "selesai",
                    "teks": "web tidak dinyalakan",
                },
            ],
        },
    ],
    "Podman: Container Tanpa Root di Fedora": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Docker dan Podman",
            "ket": "Perintahnya hampir sama; cara kerjanya yang beda.",
            "tabel": [
                {
                    "kolom": [
                        "Hal",
                        "Docker",
                        "Podman",
                    ],
                    "baris": [
                        [
                            "Daemon",
                            "dockerd (root)",
                            "tidak ada",
                        ],
                        [
                            "Tanpa root",
                            "opsional",
                            "bawaan",
                        ],
                        [
                            "Nama pendek",
                            "docker.io",
                            "registries.conf",
                        ],
                        [
                            "Pod",
                            "tidak ada",
                            "ada",
                        ],
                        [
                            "Layanan systemd",
                            "unit manual",
                            "Quadlet",
                        ],
                        [
                            "Fedora",
                            "pasang sendiri",
                            "bawaan",
                        ],
                    ],
                },
            ],
        },
    ],
    "Registry dan Runtime: Docker Hub, containerd, LXC": [
        {
            "setelah": 5,
            "jenis": "tumpukan",
            "judul": "Lapisan di balik docker run",
            "ket": "Tiap lapisan menyerahkan pekerjaan ke lapisan di bawahnya.",
            "isi": [
                "docker (CLI)",
                "dockerd",
                "containerd",
                "runc",
                "kernel Linux",
            ],
            "label": "runtime",
        },
    ],
    "GitHub Actions: Pipeline Pertama dari Commit ke Tes": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Perjalanan satu push sampai tanda centang",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "git push ke main",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "GitHub baca .github/workflows",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "runner baru dinyalakan",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "checkout, pasang, jalankan tes",
                    "ke": 4,
                },
                {
                    "jenis": "keputusan",
                    "teks": "semua step keluar kode 0?",
                    "ya": 5,
                    "tidak": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "centang hijau di commit",
                },
                {
                    "jenis": "selesai",
                    "teks": "silang merah, log disimpan",
                },
            ],
        },
    ],
    "GitHub Actions: Matriks, Cache, dan Artefak": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Lima job dari matriks os x python dengan satu exclude",
            "tabel": [
                {
                    "nama": "job yang dibuat",
                    "kolom": [
                        "os",
                        "3.12",
                        "3.13",
                        "3.14",
                    ],
                    "baris": [
                        [
                            "ubuntu-latest",
                            "jalan",
                            "jalan",
                            "jalan",
                        ],
                        [
                            "windows-latest",
                            "dibuang",
                            "jalan",
                            "jalan",
                        ],
                    ],
                    "sorot_baris": [1],
                },
            ],
            "ket": "Sel dibuang adalah kombinasi yang dicoret exclude.",
        },
    ],
    "GitHub Actions: Secrets, OIDC, dan Keamanan Workflow": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Deploy lewat OIDC, tanpa kunci yang disimpan",
            "pelaku": [
                "runner",
                "OIDC GitHub",
                "AWS STS",
                "S3",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "minta token (id-token)",
                ],
                [
                    1,
                    0,
                    "JWT: repo, environment",
                ],
                [
                    0,
                    2,
                    "AssumeRoleWithWebIdentity",
                ],
                [
                    2,
                    2,
                    "cek aud dan sub",
                ],
                [
                    2,
                    0,
                    "kredensial sementara",
                ],
                [
                    0,
                    3,
                    "aws s3 sync",
                ],
            ],
        },
    ],
    "GitLab CI dan Jenkins": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Tiga alat, konsep yang sama",
            "tabel": [
                {
                    "kolom": [
                        "Konsep",
                        "GitHub Actions",
                        "GitLab CI",
                        "Jenkins",
                    ],
                    "baris": [
                        [
                            "Berkas",
                            "workflows/*.yml",
                            ".gitlab-ci.yml",
                            "Jenkinsfile",
                        ],
                        [
                            "Mesin build",
                            "runner",
                            "GitLab Runner",
                            "agent",
                        ],
                        [
                            "Urutan",
                            "needs",
                            "stages, needs",
                            "stages",
                        ],
                        [
                            "Persetujuan",
                            "environment",
                            "when: manual",
                            "input",
                        ],
                        [
                            "Dipasang",
                            "SaaS, sendiri",
                            "SaaS, sendiri",
                            "sendiri",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta CI/CD Lain dan Repositori Artefak": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Alat CI/CD selain tiga besar",
            "tabel": [
                {
                    "kolom": [
                        "Alat",
                        "Model",
                        "Status",
                    ],
                    "baris": [
                        [
                            "CircleCI",
                            "SaaS",
                            "stabil",
                        ],
                        [
                            "Azure Pipelines",
                            "SaaS atau server",
                            "stabil",
                        ],
                        [
                            "Bitbucket",
                            "SaaS",
                            "stabil, kecil",
                        ],
                        [
                            "TeamCity",
                            "server",
                            "stabil",
                        ],
                        [
                            "Buildkite",
                            "hibrida",
                            "aktif",
                        ],
                        [
                            "Travis CI",
                            "SaaS",
                            "menurun",
                        ],
                        [
                            "GoCD",
                            "server",
                            "menurun",
                        ],
                    ],
                    "sorot_baris": [5, 6],
                },
            ],
        },
    ],
    "Dasar Cloud dan Peta Penyedia: AWS, Google Cloud, Azure": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Nama layanan yang sama di tiga penyedia",
            "tabel": [
                {
                    "kolom": [
                        "Kebutuhan",
                        "AWS",
                        "Google Cloud",
                        "Azure",
                    ],
                    "baris": [
                        [
                            "Mesin virtual",
                            "EC2",
                            "Compute Engine",
                            "Virtual Machines",
                        ],
                        [
                            "Object storage",
                            "S3",
                            "Cloud Storage",
                            "Blob Storage",
                        ],
                        [
                            "Database SQL",
                            "RDS",
                            "Cloud SQL",
                            "Azure Database",
                        ],
                        [
                            "NoSQL",
                            "DynamoDB",
                            "Firestore",
                            "Cosmos DB",
                        ],
                        [
                            "Identitas",
                            "IAM",
                            "Cloud IAM",
                            "Entra ID",
                        ],
                        [
                            "Fungsi",
                            "Lambda",
                            "Run functions",
                            "Azure Functions",
                        ],
                    ],
                },
            ],
        },
    ],
    "AWS IAM: Siapa Boleh Melakukan Apa": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Cara IAM memutuskan satu permintaan",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "permintaan masuk",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "kumpulkan pernyataan yang cocok",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada Deny yang cocok?",
                    "ya": 4,
                    "tidak": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada Allow yang cocok?",
                    "ya": 5,
                    "tidak": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "ditolak (Deny eksplisit)",
                },
                {
                    "jenis": "selesai",
                    "teks": "diizinkan",
                },
                {
                    "jenis": "selesai",
                    "teks": "ditolak (tolak bawaan)",
                },
            ],
        },
    ],
    "EC2 dan VPC: Server dan Jaringan di AWS": [
        {
            "setelah": 2,
            "jenis": "bit",
            "angka": 240,
            "lebar": 8,
            "label": "oktet ke-3 netmask /20",
            "judul": "Netmask /20: 16 bit pertama + 4 bit di oktet ketiga",
            "ket": "255.255.240.0: empat bit kiri oktet ketiga ikut dikunci, jadi satu subnet /20 berisi 4.096 alamat.",
        },
        {
            "setelah": 5,
            "jenis": "pohon",
            "judul": "Satu VPC, dua AZ, subnet publik dan privat",
            "akar": {
                "teks": "VPC 10.0.0.0/16",
                "anak": [
                    {
                        "teks": "AZ a",
                        "anak": [
                            {
                                "teks": "publik-a /24",
                                "anak": [
                                    {
                                        "teks": "load balancer",
                                    },
                                    {
                                        "teks": "NAT gateway",
                                    },
                                ],
                            },
                            {
                                "teks": "privat-a /20",
                                "anak": [
                                    {
                                        "teks": "EC2 aplikasi",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "AZ b",
                        "anak": [
                            {
                                "teks": "publik-b /24",
                                "anak": [
                                    {
                                        "teks": "load balancer",
                                    },
                                ],
                            },
                            {
                                "teks": "privat-b /20",
                                "anak": [
                                    {
                                        "teks": "EC2 aplikasi",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "S3 dan CloudFront: Berkas dan CDN di AWS": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Permintaan pertama dan kedua lewat CDN",
            "pelaku": [
                "pengguna",
                "edge CDN",
                "S3 (origin)",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET app.3f9a.css",
                ],
                [
                    1,
                    2,
                    "MISS: ambil ke origin",
                ],
                [
                    2,
                    1,
                    "berkas + Cache-Control",
                ],
                [
                    1,
                    0,
                    "berkas (disimpan di edge)",
                ],
                [
                    0,
                    1,
                    "GET app.3f9a.css lagi",
                ],
                [
                    1,
                    0,
                    "HIT: langsung dari cache",
                ],
            ],
        },
    ],
    "RDS, DynamoDB, ELB, Route 53, dan CloudWatch": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Satu permintaan di arsitektur tiga lapis",
            "pelaku": [
                "Route 53",
                "ALB",
                "EC2",
                "RDS",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "tokoani.id -> alamat ALB",
                ],
                [
                    1,
                    2,
                    "teruskan ke instance sehat",
                ],
                [
                    2,
                    3,
                    "SELECT pesanan",
                ],
                [
                    3,
                    2,
                    "baris data",
                ],
                [
                    2,
                    1,
                    "HTTP 200",
                ],
            ],
        },
    ],
    "AWS Lambda: Menjalankan Fungsi Tanpa Server": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Satu unggahan foto memicu Lambda",
            "pelaku": [
                "pengguna",
                "S3",
                "Lambda",
                "CloudWatch",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "unggah sepatu.jpg",
                ],
                [
                    1,
                    2,
                    "event ObjectCreated",
                ],
                [
                    2,
                    2,
                    "cold start (kalau perlu)",
                ],
                [
                    2,
                    1,
                    "simpan thumbnail",
                ],
                [
                    2,
                    3,
                    "log print dan durasi",
                ],
            ],
        },
    ],
    "Lambda dengan API Gateway, SQS, dan EventBridge": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Perjalanan pesan dari API sampai DLQ",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "POST /daftar ke API Gateway",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Lambda API kirim pesan ke SQS",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Lambda pekerja terima pesan",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "proses berhasil?",
                    "ya": 4,
                    "tidak": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "pesan dihapus",
                },
                {
                    "jenis": "keputusan",
                    "teks": "sudah diterima 3 kali?",
                    "ya": 6,
                    "tidak": 2,
                },
                {
                    "jenis": "selesai",
                    "teks": "pindah ke DLQ, alarm menyala",
                },
            ],
        },
    ],
    "Cloudflare Workers dan Platform Edge": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Permintaan dijawab di edge, origin cuma kalau perlu",
            "pelaku": [
                "pengguna",
                "edge",
                "origin",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /halo?nama=Sari",
                ],
                [
                    1,
                    0,
                    "Worker menjawab langsung",
                ],
                [
                    0,
                    1,
                    "GET /laporan",
                ],
                [
                    1,
                    2,
                    "fetch ke server asal",
                ],
                [
                    2,
                    1,
                    "data laporan",
                ],
                [
                    1,
                    0,
                    "jawaban + header cache",
                ],
            ],
        },
    ],
    "Peta Platform Deploy: Cloud Run, Vercel, Heroku, Firebase": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Platform deploy dan status paket gratisnya",
            "tabel": [
                {
                    "kolom": [
                        "Platform",
                        "Model",
                        "Gratis?",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Cloud Run",
                            "container",
                            "free tier",
                            "aktif",
                        ],
                        [
                            "Vercel",
                            "frontend",
                            "non-komersial",
                            "aktif",
                        ],
                        [
                            "Netlify",
                            "frontend",
                            "300 kredit",
                            "stabil",
                        ],
                        [
                            "Render",
                            "PaaS",
                            "tidur 15 mnt",
                            "aktif",
                        ],
                        [
                            "Railway",
                            "PaaS",
                            "kredit US$1",
                            "aktif",
                        ],
                        [
                            "Fly.io",
                            "micro-VM",
                            "tidak ada",
                            "aktif",
                        ],
                        [
                            "Heroku",
                            "PaaS",
                            "tidak ada",
                            "menurun",
                        ],
                        [
                            "Firebase",
                            "BaaS",
                            "ada",
                            "aktif",
                        ],
                    ],
                    "sorot_baris": [6],
                },
            ],
        },
    ],
    "Terraform: Infrastruktur Ditulis sebagai Kode": [
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Siklus kerja Terraform",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "tulis atau ubah berkas .tf",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "terraform init (sekali)",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "terraform plan -out",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "rencananya sesuai harapan?",
                    "ya": 4,
                    "tidak": 0,
                },
                {
                    "jenis": "proses",
                    "teks": "terraform apply rencana",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "state diperbarui",
                },
            ],
        },
    ],
    "Terraform State, Plan, dan Backend Jarak Jauh": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Simbol di hasil terraform plan",
            "tabel": [
                {
                    "kolom": [
                        "Simbol",
                        "Arti",
                        "Contoh",
                    ],
                    "baris": [
                        [
                            "+",
                            "dibuat",
                            "bucket baru",
                        ],
                        [
                            "~",
                            "diubah di tempat",
                            "instance_type",
                        ],
                        [
                            "-/+",
                            "hapus lalu buat",
                            "ganti AMI",
                        ],
                        [
                            "-",
                            "dihapus",
                            "resource dibuang",
                        ],
                        [
                            "<=",
                            "dibaca",
                            "data source",
                        ],
                    ],
                    "sorot_baris": [2],
                },
            ],
            "ket": "Replace (-/+) dihitung sebagai satu add dan satu destroy.",
        },
    ],
    "Modul Terraform dan Terraform di Pipeline": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Satu modul, dua lingkungan dengan state terpisah",
            "akar": {
                "teks": "infra/",
                "anak": [
                    {
                        "teks": "modules/web",
                        "anak": [
                            {
                                "teks": "main.tf",
                            },
                            {
                                "teks": "variables.tf",
                            },
                            {
                                "teks": "outputs.tf",
                            },
                        ],
                    },
                    {
                        "teks": "lingkungan/",
                        "anak": [
                            {
                                "teks": "staging/",
                                "anak": [
                                    {
                                        "teks": "main.tf",
                                    },
                                    {
                                        "teks": "backend.tf",
                                    },
                                ],
                            },
                            {
                                "teks": "produksi/",
                                "anak": [
                                    {
                                        "teks": "main.tf",
                                    },
                                    {
                                        "teks": "backend.tf",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Ansible: Otomasi Server Lewat SSH": [
        {
            "setelah": 7,
            "jenis": "urutan",
            "judul": "Satu tugas Ansible di satu host",
            "pelaku": [
                "control node",
                "host target",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "SSH masuk sebagai deploy",
                ],
                [
                    0,
                    1,
                    "salin modul dnf (Python)",
                ],
                [
                    1,
                    1,
                    "jalankan modul, cek nginx",
                ],
                [
                    1,
                    0,
                    "JSON: changed true/false",
                ],
                [
                    0,
                    0,
                    "catat ok/changed, notify",
                ],
            ],
        },
    ],
    "Ansible Lanjutan: Role, Template, dan Idempotensi": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Isi satu role Ansible",
            "akar": {
                "teks": "roles/nginx",
                "anak": [
                    {
                        "teks": "defaults/main.yml",
                    },
                    {
                        "teks": "vars/main.yml",
                    },
                    {
                        "teks": "tasks/main.yml",
                    },
                    {
                        "teks": "handlers/main.yml",
                    },
                    {
                        "teks": "templates/",
                        "anak": [
                            {
                                "teks": "situs.conf.j2",
                            },
                        ],
                    },
                    {
                        "teks": "meta/main.yml",
                    },
                ],
            },
        },
    ],
    "Peta IaC: OpenTofu, Pulumi, CloudFormation, Chef, Puppet": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Alat IaC, bahasa, lisensi, dan statusnya",
            "tabel": [
                {
                    "kolom": [
                        "Alat",
                        "Bahasa",
                        "Lisensi",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Terraform",
                            "HCL",
                            "BUSL-1.1",
                            "aktif",
                        ],
                        [
                            "OpenTofu",
                            "HCL",
                            "MPL-2.0",
                            "aktif",
                        ],
                        [
                            "Pulumi",
                            "Python, TS, Go",
                            "Apache-2.0",
                            "aktif",
                        ],
                        [
                            "CloudFormation",
                            "YAML/JSON",
                            "proprietary",
                            "matang",
                        ],
                        [
                            "Ansible",
                            "YAML",
                            "GPL-3.0",
                            "aktif",
                        ],
                        [
                            "Chef",
                            "Ruby",
                            "komersial",
                            "menurun",
                        ],
                        [
                            "Puppet",
                            "Puppet DSL",
                            "komersial",
                            "menurun",
                        ],
                        [
                            "Salt",
                            "YAML",
                            "Apache-2.0",
                            "menurun",
                        ],
                    ],
                    "sorot_baris": [5, 6, 7],
                },
            ],
            "ket": "Chef dan Puppet: kode sumber Apache-2.0, biner resmi berlisensi komersial.",
        },
    ],
    "Kubernetes: Arsitektur, Reconciliation, dan Klaster Lokal": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Reconciliation loop sebuah controller",
            "ket": "Controller nggak pernah selesai: ia terus mengamati dan membetulkan selisih.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Baca spec (diinginkan)",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Amati status (aktual)",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Aktual sama dengan spec?",
                    "ya": 4,
                    "tidak": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Buat atau hapus objek",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Tunggu perubahan berikutnya",
                    "ke": 0,
                },
            ],
        },
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Isi klaster Kubernetes kecil",
            "akar": {
                "teks": "klaster",
                "anak": [
                    {
                        "teks": "control plane",
                        "anak": [
                            {
                                "teks": "kube-apiserver",
                            },
                            {
                                "teks": "etcd",
                            },
                            {
                                "teks": "kube-scheduler",
                            },
                            {
                                "teks": "controller-manager",
                            },
                        ],
                    },
                    {
                        "teks": "node-1",
                        "anak": [
                            {
                                "teks": "kubelet",
                            },
                            {
                                "teks": "containerd",
                            },
                            {
                                "teks": "kube-proxy",
                            },
                            {
                                "teks": "pod web-2",
                            },
                        ],
                    },
                    {
                        "teks": "node-2",
                        "anak": [
                            {
                                "teks": "kubelet",
                            },
                            {
                                "teks": "pod web-3",
                            },
                            {
                                "teks": "pod web-4",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Pod, Deployment, dan Strategi Rilis": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Rolling update 3 replika, maxSurge 1, maxUnavailable 0",
            "pelaku": [
                "Deployment",
                "RS lama (v1)",
                "RS baru (v2)",
            ],
            "pesan": [
                [
                    0,
                    2,
                    "skala ke 1 (pod v2 ke-1)",
                ],
                [
                    2,
                    0,
                    "pod v2 ke-1 siap",
                ],
                [
                    0,
                    1,
                    "skala ke 2",
                ],
                [
                    0,
                    2,
                    "skala ke 2",
                ],
                [
                    2,
                    0,
                    "pod v2 ke-2 siap",
                ],
                [
                    0,
                    1,
                    "skala ke 1",
                ],
                [
                    0,
                    2,
                    "skala ke 3",
                ],
                [
                    2,
                    0,
                    "pod v2 ke-3 siap",
                ],
                [
                    0,
                    1,
                    "skala ke 0 (simpan riwayat)",
                ],
            ],
        },
    ],
    "Service, Ingress, dan Gateway API": [
        {
            "setelah": 5,
            "jenis": "urutan",
            "judul": "Satu permintaan dari internet sampai ke pod",
            "pelaku": [
                "pengguna",
                "Gateway",
                "Service web",
                "Pod web-2",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET toko.contoh.id/",
                ],
                [
                    1,
                    1,
                    "cocokkan HTTPRoute toko",
                ],
                [
                    1,
                    2,
                    "teruskan ke web-v1 (bobot 90)",
                ],
                [
                    2,
                    3,
                    "pilih pod yang siap",
                ],
                [
                    3,
                    0,
                    "200 OK",
                ],
            ],
        },
    ],
    "ConfigMap, Secret, Probe, dan Batas Resource": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Tiga probe dan akibat gagalnya",
            "tabel": [
                {
                    "kolom": [
                        "Probe",
                        "Kalau gagal",
                        "Menjawab",
                    ],
                    "baris": [
                        [
                            "liveness",
                            "di-restart",
                            "macet?",
                        ],
                        [
                            "readiness",
                            "tak dapat trafik",
                            "siap melayani?",
                        ],
                        [
                            "startup",
                            "tunda probe lain",
                            "sudah menyala?",
                        ],
                    ],
                    "sorot_kolom": [
                        "Kalau gagal",
                    ],
                },
            ],
        },
    ],
    "Peta Orkestrasi: EKS, ECS, OpenShift, Nomad, Service Mesh": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Pilihan orkestrasi dan statusnya",
            "tabel": [
                {
                    "kolom": [
                        "Pilihan",
                        "Jenis",
                        "Status",
                    ],
                    "baris": [
                        [
                            "EKS/GKE/AKS",
                            "K8s terkelola",
                            "aktif",
                        ],
                        [
                            "ECS + Fargate",
                            "orkestrator AWS",
                            "aktif",
                        ],
                        [
                            "OpenShift",
                            "K8s perusahaan",
                            "aktif",
                        ],
                        [
                            "Rancher",
                            "manajer klaster",
                            "aktif",
                        ],
                        [
                            "Nomad",
                            "penjadwal",
                            "stabil-matang",
                        ],
                        [
                            "Docker Swarm",
                            "mode Docker",
                            "menurun",
                        ],
                        [
                            "Istio/Linkerd",
                            "service mesh",
                            "aktif",
                        ],
                        [
                            "Consul",
                            "discovery + mesh",
                            "stabil-matang",
                        ],
                    ],
                },
            ],
        },
    ],
    "Helm: Memasang Aplikasi dengan Chart": [
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Siklus hidup sebuah release Helm",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "helm install (revisi 1)",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "helm upgrade (revisi 2)",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Versi baru sehat?",
                    "ya": 4,
                    "tidak": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "helm rollback 1 (revisi 3)",
                    "ke": 4,
                },
                {
                    "jenis": "selesai",
                    "teks": "Release berjalan",
                },
            ],
        },
    ],
    "Membuat Chart Helm dan Kapan Memilih Kustomize": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Kerangka chart hasil helm create toko",
            "akar": {
                "teks": "toko/",
                "anak": [
                    {
                        "teks": "Chart.yaml",
                    },
                    {
                        "teks": "values.yaml",
                    },
                    {
                        "teks": "charts/",
                    },
                    {
                        "teks": "templates/",
                        "anak": [
                            {
                                "teks": "deployment.yaml",
                            },
                            {
                                "teks": "service.yaml",
                            },
                            {
                                "teks": "_helpers.tpl",
                            },
                            {
                                "teks": "NOTES.txt",
                            },
                            {
                                "teks": "tests/",
                            },
                        ],
                    },
                    {
                        "teks": ".helmignore",
                    },
                ],
            },
        },
    ],
    "GitOps dengan Argo CD": [
        {
            "setelah": 5,
            "jenis": "urutan",
            "judul": "Alur GitOps dari pull request sampai klaster",
            "pelaku": [
                "developer",
                "Git",
                "Argo CD",
                "klaster",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "merge PR: newTag 2.5.0",
                ],
                [
                    2,
                    1,
                    "ambil revisi terbaru",
                ],
                [
                    2,
                    2,
                    "render dan bandingkan",
                ],
                [
                    2,
                    3,
                    "sync: apply manifest",
                ],
                [
                    3,
                    2,
                    "status Healthy",
                ],
                [
                    2,
                    0,
                    "UI: Synced, Healthy",
                ],
            ],
        },
    ],
    "Argo CD Lanjutan: Drift, Rollback, dan Flux": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Argo CD dan Flux secara ringkas",
            "tabel": [
                {
                    "kolom": [
                        "Aspek",
                        "Argo CD",
                        "Flux",
                    ],
                    "baris": [
                        [
                            "Unit utama",
                            "Application",
                            "Kustomization",
                        ],
                        [
                            "UI web",
                            "bawaan",
                            "di luar inti",
                        ],
                        [
                            "Chart Helm",
                            "dirender Argo",
                            "HelmRelease",
                        ],
                        [
                            "Multi-klaster",
                            "satu Argo pusat",
                            "Flux per klaster",
                        ],
                        [
                            "Versi Okt 2026",
                            "v3.5.5",
                            "v2.9.6",
                        ],
                    ],
                },
            ],
        },
    ],
    "Dasar Observability: Metrik, Log, Trace, dan SLO": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Empat golden signals",
            "tabel": [
                {
                    "kolom": [
                        "Sinyal",
                        "Pertanyaan",
                        "Contoh metrik",
                    ],
                    "baris": [
                        [
                            "Latency",
                            "seberapa lama?",
                            "p95 durasi",
                        ],
                        [
                            "Traffic",
                            "seberapa ramai?",
                            "permintaan/detik",
                        ],
                        [
                            "Errors",
                            "berapa gagal?",
                            "% respons 5xx",
                        ],
                        [
                            "Saturation",
                            "seberapa penuh?",
                            "CPU, antrean",
                        ],
                    ],
                },
            ],
        },
    ],
    "Prometheus: Mengumpulkan Metrik dari Aplikasi": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Prometheus mengambil metrik dari target",
            "pelaku": [
                "Prometheus",
                "toko-api",
                "node_exporter",
                "Alertmanager",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /metrics (tiap 15 detik)",
                ],
                [
                    1,
                    0,
                    "teks metrik",
                ],
                [
                    0,
                    2,
                    "GET /metrics",
                ],
                [
                    2,
                    0,
                    "teks metrik",
                ],
                [
                    0,
                    0,
                    "simpan, evaluasi aturan",
                ],
                [
                    0,
                    3,
                    "kirim alert yang firing",
                ],
            ],
        },
    ],
    "PromQL, Alert, dan Dasbor Grafana": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Counter yang reset dan kenaikannya",
            "ket": "Total kenaikan 110 dalam 60 detik, sekitar 1,83 per detik.",
            "tabel": [
                {
                    "kolom": [
                        "detik",
                        "nilai counter",
                        "kenaikan",
                    ],
                    "baris": [
                        [
                            "0",
                            "100",
                            "",
                        ],
                        [
                            "15",
                            "130",
                            "30",
                        ],
                        [
                            "30",
                            "160",
                            "30",
                        ],
                        [
                            "45",
                            "20",
                            "20 (reset)",
                        ],
                        [
                            "60",
                            "50",
                            "30",
                        ],
                    ],
                    "sorot_baris": [3],
                },
            ],
        },
    ],
    "OpenTelemetry: Satu Standar untuk Telemetri": [
        {
            "setelah": 7,
            "jenis": "alur",
            "judul": "Perjalanan telemetri lewat OpenTelemetry Collector",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Aplikasi + SDK OpenTelemetry",
                    "ke": 1,
                },
                {
                    "jenis": "masukan",
                    "teks": "receiver otlp (4317/4318)",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "processor batch, filter",
                    "ke": 3,
                },
                {
                    "jenis": "keluaran",
                    "teks": "exporter ke backend",
                    "ke": 4,
                },
                {
                    "jenis": "selesai",
                    "teks": "Jaeger, Prometheus, vendor",
                },
            ],
        },
    ],
    "Tracing dengan OpenTelemetry dan Jaeger": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Span induk dan anak dalam satu trace checkout",
            "ket": "Jalur kritis: checkout, bayar, lalu panggilan bank.",
            "akar": {
                "teks": "checkout 250ms",
                "anak": [
                    {
                        "teks": "auth 15ms",
                    },
                    {
                        "teks": "stok 80ms",
                        "anak": [
                            {
                                "teks": "redis GET 10ms",
                            },
                            {
                                "teks": "SELECT 40ms",
                            },
                        ],
                    },
                    {
                        "teks": "bayar 140ms",
                        "anak": [
                            {
                                "teks": "POST bank 110ms",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Log Terpusat: Loki, Alloy, ELK, dan Fluent Bit": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Rantai log terpusat",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Aplikasi tulis JSON ke stdout",
                    "ke": 1,
                },
                {
                    "jenis": "masukan",
                    "teks": "Alloy / Fluent Bit membaca",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Beri label, saring, urai",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Simpan: Loki / Elasticsearch",
                    "ke": 4,
                },
                {
                    "jenis": "selesai",
                    "teks": "Cari di Grafana / Kibana",
                },
            ],
        },
    ],
    "Peta Observability dan On-Call: Datadog sampai PagerDuty": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Layanan observability dan on-call",
            "tabel": [
                {
                    "kolom": [
                        "Layanan",
                        "Fokus",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Datadog",
                            "observability",
                            "aktif",
                        ],
                        [
                            "Sentry",
                            "error tracking",
                            "aktif",
                        ],
                        [
                            "New Relic",
                            "APM",
                            "stabil-matang",
                        ],
                        [
                            "Splunk",
                            "log dan SIEM",
                            "aktif",
                        ],
                        [
                            "Zabbix",
                            "server, jaringan",
                            "stabil-matang",
                        ],
                        [
                            "PagerDuty",
                            "on-call",
                            "aktif",
                        ],
                        [
                            "Wavefront",
                            "metrik",
                            "ditutup 2025",
                        ],
                        [
                            "Opsgenie",
                            "on-call",
                            "tutup Apr 2027",
                        ],
                    ],
                    "sorot_baris": [6, 7],
                },
            ],
        },
    ],
    "FinOps: Membaca dan Menekan Tagihan Cloud": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Sumber biaya kejutan di cloud",
            "tabel": [
                {
                    "kolom": [
                        "Sumber",
                        "Kenapa kaget",
                    ],
                    "baris": [
                        [
                            "data keluar",
                            "per GB keluar",
                        ],
                        [
                            "NAT gateway",
                            "per jam + per GB",
                        ],
                        [
                            "IPv4 publik",
                            "tiap alamat/jam",
                        ],
                        [
                            "log",
                            "simpan selamanya",
                        ],
                        [
                            "snapshot yatim",
                            "lupa dihapus",
                        ],
                        [
                            "LB menganggur",
                            "tetap ditagih",
                        ],
                        [
                            "lab lupa mati",
                            "jalan 24 jam",
                        ],
                    ],
                },
            ],
        },
    ],
}
