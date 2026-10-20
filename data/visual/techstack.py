"""Gambar konsep kurikulum Tech Stack & Arsitektur. Skema: inti/visual.py."""

VISUAL = {
    "Apa Itu Tech Stack dan Kenapa Pilihannya Banyak Sekali": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "Lapisan stack, yang paling atas paling dekat ke pengguna",
            "ket": "Frontend memakai backend, backend memakai database, dan semuanya berjalan di atas infrastruktur dan perangkat keras.",
            "mode": "tumpukan",
            "isi": [
                "Perangkat keras",
                "Infrastruktur",
                "Database",
                "Backend",
                "Frontend",
            ],
            "label": "satu aplikasi web",
        },
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Yang paling banyak dipakai di Survei Stack Overflow 2026",
            "ket": "Persentase responden yang memakai, bukan pangsa pasar.",
            "tabel": [
                {
                    "nama": "survei 2026",
                    "kolom": [
                        "kategori",
                        "teratas",
                        "persen",
                    ],
                    "baris": [
                        [
                            "bahasa",
                            "JavaScript",
                            "62%",
                        ],
                        [
                            "database",
                            "PostgreSQL",
                            "58%",
                        ],
                        [
                            "framework web",
                            "Node.js",
                            "46%",
                        ],
                        [
                            "editor",
                            "VS Code",
                            "71%",
                        ],
                    ],
                },
            ],
        },
    ],
    "Perjalanan Satu Request dari Browser sampai Database": [
        {
            "setelah": 7,
            "jenis": "urutan",
            "judul": "Satu request dari browser sampai database dan balik lagi",
            "ket": "Proxy dan aplikasi digabung jadi Server supaya gambarnya ringkas. Nilainya sama dengan simulasi di bawah.",
            "pelaku": [
                "Browser",
                "DNS",
                "Server",
                "Database",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "toko.example.com?",
                ],
                [
                    1,
                    0,
                    "203.0.113.10",
                ],
                [
                    0,
                    2,
                    "GET /produk/7",
                ],
                [
                    2,
                    3,
                    "SELECT ... WHERE id = 7",
                ],
                [
                    3,
                    2,
                    "Pensil 2B, 3500",
                ],
                [
                    2,
                    0,
                    "200 + HTML",
                ],
            ],
        },
    ],
    "Jalur Belajar per Peran Berdasarkan Roadmap": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Memakai peta: satu peran, satu jalur, satu proyek",
            "ket": "Contoh di bawah menyimpan jalur sebagai daftar dan menyarankan kurikulum pertama yang belum selesai.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Pilih satu peran",
                },
                {
                    "jenis": "proses",
                    "teks": "Ambil kurikulum berikutnya",
                },
                {
                    "jenis": "proses",
                    "teks": "Kerjakan materi, kuis, latihan",
                },
                {
                    "jenis": "keputusan",
                    "teks": "Masih ada di jalur ini?",
                    "ya": 1,
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Bikin satu proyek kecil",
                },
                {
                    "jenis": "selesai",
                    "teks": "Lirik jalur sebelahnya",
                },
            ],
        },
    ],
    "LAMP, LEMP, dan Paket Server Lokal": [
        {
            "setelah": 0,
            "jenis": "tumpukan",
            "judul": "LAMP: empat program yang ditumpuk",
            "ket": "Huruf akronimnya dibaca dari bawah: Linux, Apache, MySQL, PHP. Di LEMP, Apache diganti Nginx.",
            "mode": "tumpukan",
            "isi": [
                "Linux",
                "Apache httpd",
                "MySQL / MariaDB",
                "PHP",
            ],
            "label": "satu server LAMP",
        },
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "LEMP: Nginx menjawab berkas statis, PHP lewat PHP-FPM",
            "ket": "Sesuai konfigurasi di atas: app.css ada di disk, sedangkan /produk/7 diserahkan ke index.php.",
            "pelaku": [
                "Browser",
                "Nginx",
                "PHP-FPM",
                "MySQL",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /css/app.css",
                ],
                [
                    1,
                    0,
                    "berkas dari disk",
                ],
                [
                    0,
                    1,
                    "GET /produk/7",
                ],
                [
                    1,
                    2,
                    "FastCGI: /index.php",
                ],
                [
                    2,
                    3,
                    "SELECT ... produk 7",
                ],
                [
                    3,
                    2,
                    "baris produk 7",
                ],
                [
                    2,
                    1,
                    "HTML",
                ],
                [
                    1,
                    0,
                    "200 + HTML",
                ],
            ],
        },
    ],
    "MVC dan Arsitektur Berlapis": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "GET /buku/2 melewati controller, model, lalu view",
            "ket": "Nilainya sama dengan program di atas: Bumi Manusia stoknya 0, jadi model menjawab belum bisa dipinjam.",
            "pelaku": [
                "Pengguna",
                "Controller",
                "Model",
                "View",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /buku/2",
                ],
                [
                    1,
                    2,
                    "cari_buku(2)",
                ],
                [
                    2,
                    1,
                    "Bumi Manusia, stok 0",
                ],
                [
                    1,
                    2,
                    "bisa_dipinjam?",
                ],
                [
                    2,
                    1,
                    "False",
                ],
                [
                    1,
                    3,
                    "view_buku(buku, False)",
                ],
                [
                    3,
                    1,
                    "teks hasil",
                ],
                [
                    1,
                    0,
                    "[2] Bumi Manusia (stok habis)",
                ],
            ],
        },
    ],
    "Pola Rendering Web: MPA, SPA, SSR, SSG, dan Islands": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Di mana dan kapan HTML dibuat",
            "ket": "Ringkasan tabel di atas. Banyak framework sekarang bisa mencampur beberapa pola dalam satu proyek.",
            "tabel": [
                {
                    "nama": "pola rendering",
                    "kolom": [
                        "pola",
                        "HTML dibuat",
                        "kelebihan",
                    ],
                    "baris": [
                        [
                            "MPA / SSR",
                            "di server",
                            "langsung terbaca",
                        ],
                        [
                            "SPA / CSR",
                            "di browser",
                            "pindah cepat",
                        ],
                        [
                            "SSG",
                            "saat build",
                            "cepat, murah",
                        ],
                        [
                            "ISR",
                            "build + ulang",
                            "statis + segar",
                        ],
                        [
                            "Islands",
                            "statis + pulau",
                            "JS seperlunya",
                        ],
                    ],
                },
            ],
        },
    ],
    "MERN dari Dekat: Satu Bahasa dari Database ke Browser": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Satu request daftar produk di stack MERN",
            "ket": "Express memanggil Mongoose, MongoDB mengembalikan dokumen, dan React menerima JSON yang sudah urut harga.",
            "pelaku": [
                "React",
                "Express",
                "MongoDB",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /api/produk",
                ],
                [
                    1,
                    2,
                    "find().sort({ harga: 1 })",
                ],
                [
                    2,
                    1,
                    "3 dokumen",
                ],
                [
                    1,
                    0,
                    "JSON urut harga",
                ],
            ],
        },
    ],
    "MEAN, MEVN, dan PERN: Varian Stack JavaScript": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Empat varian, satu kerangka Node.js dan Express",
            "ket": "Yang berganti cuma database atau tampilan. Server HTTP-nya tetap Express di atas Node.js.",
            "tabel": [
                {
                    "nama": "varian",
                    "kolom": [
                        "stack",
                        "database",
                        "tampilan",
                    ],
                    "baris": [
                        [
                            "MERN",
                            "MongoDB",
                            "React",
                        ],
                        [
                            "MEAN",
                            "MongoDB",
                            "Angular",
                        ],
                        [
                            "MEVN",
                            "MongoDB",
                            "Vue",
                        ],
                        [
                            "PERN",
                            "PostgreSQL",
                            "React",
                        ],
                    ],
                },
            ],
        },
    ],
    "Dari Jamstack ke Next.js, T3, dan Meta-Framework": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Jamstack: kerja berat di waktu build, CDN tinggal mengirim",
            "ket": "Sama dengan program di bawah: tiga halaman disusun sekali, lalu pengunjung cuma menerima berkas jadi.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Data + template",
                },
                {
                    "jenis": "proses",
                    "teks": "Build: susun semua HTML",
                },
                {
                    "jenis": "proses",
                    "teks": "Unggah berkas ke CDN",
                },
                {
                    "jenis": "masukan",
                    "teks": "Pengunjung minta menu.html",
                },
                {
                    "jenis": "proses",
                    "teks": "CDN terdekat kirim berkas",
                },
                {
                    "jenis": "selesai",
                    "teks": "Browser tampilkan HTML",
                },
            ],
        },
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Meta-framework dan pustaka di bawahnya",
            "ket": "Persentase responden Survei Stack Overflow 2026.",
            "tabel": [
                {
                    "nama": "meta-framework",
                    "kolom": [
                        "nama",
                        "di atas",
                        "survei 2026",
                    ],
                    "baris": [
                        [
                            "Next.js",
                            "React",
                            "21%",
                        ],
                        [
                            "Astro",
                            "React/Vue/Svelte",
                            "6%",
                        ],
                        [
                            "SvelteKit",
                            "Svelte",
                            "6%",
                        ],
                        [
                            "Nuxt",
                            "Vue",
                            "4%",
                        ],
                    ],
                },
            ],
        },
    ],
    "Stack Laravel: TALL dan Inertia": [
        {
            "setelah": 9,
            "jenis": "urutan",
            "judul": "Inertia: HTML utuh sekali, lalu cuma page object",
            "ket": "Kunjungan pertama membawa HTML lengkap. Klik berikutnya membawa header X-Inertia dan dijawab JSON.",
            "pelaku": [
                "Browser",
                "Laravel",
                "React",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /produk",
                ],
                [
                    1,
                    0,
                    "HTML + page object",
                ],
                [
                    0,
                    2,
                    "render Produk/Index",
                ],
                [
                    0,
                    1,
                    "klik: GET /produk, X-Inertia",
                ],
                [
                    1,
                    0,
                    "JSON page object",
                ],
                [
                    0,
                    2,
                    "render ulang dengan props baru",
                ],
            ],
        },
    ],
    "Stack Python: Django, FastAPI, dan React": [
        {
            "setelah": 11,
            "jenis": "tabel",
            "judul": "Django dan FastAPI berdampingan",
            "ket": "Angka survei dari Survei Stack Overflow 2026. Django juga punya view async, tapi ORM-nya belum sepenuhnya async.",
            "tabel": [
                {
                    "nama": "dua framework Python",
                    "kolom": [
                        "aspek",
                        "Django",
                        "FastAPI",
                    ],
                    "baris": [
                        [
                            "panel admin",
                            "bawaan",
                            "tidak ada",
                        ],
                        [
                            "validasi",
                            "form, serializer",
                            "type hints",
                        ],
                        [
                            "dokumentasi API",
                            "lewat paket",
                            "otomatis /docs",
                        ],
                        [
                            "async",
                            "sebagian",
                            "bawaan",
                        ],
                        [
                            "survei 2026",
                            "11%",
                            "19%",
                        ],
                    ],
                },
            ],
        },
    ],
    "Spring Boot dan Angular: Stack Korporat Java": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Angular meminta, Spring Boot menjawab dengan JSON",
            "ket": "Controller memanggil service, service memanggil repository, dan repository menjalankan query.",
            "pelaku": [
                "Angular",
                "Spring Boot",
                "PostgreSQL",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /api/produk",
                ],
                [
                    1,
                    2,
                    "SELECT ... FROM produk",
                ],
                [
                    2,
                    1,
                    "baris produk",
                ],
                [
                    1,
                    0,
                    "JSON List<ProdukDto>",
                ],
            ],
        },
    ],
    "Stack .NET dan Blazor: C# dari Server sampai Browser": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Empat mode render Blazor",
            "ket": "Interactive Server dan Interactive WebAssembly disingkat jadi Server dan WebAssembly.",
            "tabel": [
                {
                    "nama": "mode render",
                    "kolom": [
                        "mode",
                        "interaksi",
                        "unduhan awal",
                    ],
                    "baris": [
                        [
                            "Static SSR",
                            "tidak ada",
                            "kecil",
                        ],
                        [
                            "Server",
                            "lewat server",
                            "kecil",
                        ],
                        [
                            "WebAssembly",
                            "di browser",
                            "besar",
                        ],
                        [
                            "Auto",
                            "server > browser",
                            "kecil lalu besar",
                        ],
                    ],
                },
            ],
        },
    ],
    "Stack HTML over the Wire: Hotwire, PETAL, GOTH, BETH": [
        {
            "setelah": 12,
            "jenis": "urutan",
            "judul": "Satu klik htmx: potongan HTML menggantikan isi satu elemen",
            "ket": "Nilainya sama dengan tombol dan handler Go di atas.",
            "pelaku": [
                "Pengguna",
                "Browser+htmx",
                "Server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "klik Cek stok",
                ],
                [
                    1,
                    2,
                    "GET /stok/7",
                ],
                [
                    2,
                    1,
                    "<strong>12</strong> tersisa",
                ],
                [
                    1,
                    0,
                    "isi #stok-7 diganti",
                ],
            ],
        },
    ],
    "Serverless dan Edge: Kode Tanpa Mengurus Server": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Satu kejadian, dua jalan: cold start atau warm start",
            "ket": "Sama dengan contoh di atas: panggilan pertama menjalankan muat_harga(), dua panggilan berikutnya memakai instans yang masih hangat.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "kejadian masuk (event)",
                    "ke": 1,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada instans yang hangat?",
                    "ya": 3,
                    "tidak": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "cold start: jalankan init",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "jalankan handler(event)",
                    "ke": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "kirim respons",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "instans menunggu, lalu dibuang",
                },
            ],
        },
    ],
    "BaaS, Headless, dan MACH: Merakit dari Layanan Jadi": [
        {
            "setelah": 7,
            "jenis": "pohon",
            "judul": "Satu sumber isi, banyak tampilan",
            "ket": "Inti headless: content API nggak tahu siapa yang memakai datanya. Dua cabang pertama ada di contoh kode di atas.",
            "akar": {
                "teks": "Content API (JSON)",
                "anak": [
                    {
                        "teks": "tampil_terminal()",
                    },
                    {
                        "teks": "tampil_html()",
                    },
                    {
                        "teks": "aplikasi mobile",
                    },
                ],
            },
        },
    ],
    "Peta Stack Lintas Ranah: Data, AI, Mobile, Pemantauan": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Stack bernama di luar web dan kurikulum pemiliknya",
            "ket": "Modern Data artinya Modern Data Stack, RN artinya React Native. Detail tiap stack ada di kurikulum kolom kanan.",
            "tabel": [
                {
                    "kolom": [
                        "stack",
                        "ranah",
                        "kurikulum",
                    ],
                    "baris": [
                        [
                            "ELK",
                            "log, pencarian",
                            "DevOps & Cloud",
                        ],
                        [
                            "Prom + Grafana",
                            "pemantauan",
                            "DevOps & Cloud",
                        ],
                        [
                            "Modern Data",
                            "data",
                            "Data & Analitik",
                        ],
                        [
                            "LLM + RAG",
                            "AI",
                            "AI & ML",
                        ],
                        [
                            "Flutter+Firebase",
                            "mobile",
                            "Mobile & Desktop",
                        ],
                        [
                            "RN + Expo",
                            "mobile",
                            "Mobile & Desktop",
                        ],
                    ],
                },
            ],
        },
    ],
    "Piramida Tes, TDD, dan BDD": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "Piramida tes: makin ke atas, makin sedikit dan makin lambat",
            "ket": "Tes unit di dasar paling banyak dan paling cepat. Tes end-to-end di puncak paling meyakinkan, tapi cukup sedikit.",
            "label": "piramida tes",
            "isi": [
                "unit (banyak)",
                "integrasi",
                "end-to-end",
            ],
        },
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Siklus TDD: red, green, refactor",
            "ket": "Setiap putaran cuma menambah satu perilaku kecil, misalnya potongan ongkir member di contoh atas.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "pilih satu perilaku kecil",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "red: tulis tes, pastikan gagal",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "green: kode secukupnya",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "semua tes lulus?",
                    "ya": 4,
                    "tidak": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "refactor: rapikan kode",
                    "ke": 5,
                },
                {
                    "jenis": "keputusan",
                    "teks": "masih ada perilaku lain?",
                    "ya": 1,
                    "tidak": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "fitur selesai",
                },
            ],
        },
    ],
    "Code Review, Pair Programming, dan Linting": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Perjalanan satu pull request sampai masuk main",
            "ket": "Putaran perbaikan bisa terjadi berkali-kali. Merge baru terjadi setelah CI hijau dan peninjau setuju.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "buat cabang dari main",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "commit perubahan kecil",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "buka pull request",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "CI: tes dan linter jalan",
                    "ke": 4,
                },
                {
                    "jenis": "keputusan",
                    "teks": "peninjau setuju?",
                    "ya": 6,
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "perbaiki sesuai komentar",
                    "ke": 3,
                },
                {
                    "jenis": "selesai",
                    "teks": "merge ke main, hapus cabang",
                },
            ],
        },
    ],
    "Alur Git, Semantic Versioning, dan Conventional Commits": [
        {
            "setelah": 1,
            "jenis": "git",
            "judul": "Cabang pendek yang cepat kembali ke main",
            "ket": "Gaya GitHub flow dan trunk-based: tiap cabang cuma memuat satu perubahan, lalu langsung digabung ke main.",
            "commit": [
                {
                    "id": "a1",
                    "cabang": "main",
                    "pesan": "rilis 1.4.2",
                },
                {
                    "id": "b1",
                    "cabang": "fix-ongkir",
                    "induk": [
                        "a1",
                    ],
                    "pesan": "fix: ongkir negatif",
                },
                {
                    "id": "a2",
                    "cabang": "main",
                    "induk": [
                        "a1",
                        "b1",
                    ],
                    "pesan": "merge fix-ongkir",
                },
                {
                    "id": "c1",
                    "cabang": "kurir-instan",
                    "induk": [
                        "a2",
                    ],
                    "pesan": "feat: kurir instan",
                },
                {
                    "id": "a3",
                    "cabang": "main",
                    "induk": [
                        "a2",
                        "c1",
                    ],
                    "pesan": "merge kurir-instan",
                },
            ],
            "label": {
                "main": "a3",
            },
            "head": "main",
        },
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Dari versi 1.4.2, jenis commit menentukan versi berikutnya",
            "ket": "Kalau beberapa commit dirilis bersama, yang dipakai kenaikan terbesar. docs dan tipe lain nggak menaikkan versi.",
            "tabel": [
                {
                    "kolom": [
                        "jenis commit",
                        "dari",
                        "jadi",
                    ],
                    "baris": [
                        [
                            "fix",
                            "1.4.2",
                            "1.4.3",
                        ],
                        [
                            "feat",
                            "1.4.2",
                            "1.5.0",
                        ],
                        [
                            "feat! (merusak)",
                            "1.4.2",
                            "2.0.0",
                        ],
                        [
                            "docs",
                            "1.4.2",
                            "1.4.2",
                        ],
                    ],
                },
            ],
        },
    ],
    "Kode Bersih: SOLID, DRY, Refactoring, dan Design Pattern": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Lima prinsip SOLID dan gejala pelanggarannya",
            "ket": "Gejala di kolom kanan paling gampang dikenali saat code review. Contohnya sama dengan penjelasan di atas.",
            "tabel": [
                {
                    "kolom": [
                        "huruf",
                        "nama",
                        "gejala dilanggar",
                    ],
                    "baris": [
                        [
                            "S",
                            "Single Resp.",
                            "kelas serba bisa",
                        ],
                        [
                            "O",
                            "Open/Closed",
                            "if/elif menumpuk",
                        ],
                        [
                            "L",
                            "Liskov",
                            "turunan menolak",
                        ],
                        [
                            "I",
                            "Interface Segr.",
                            "metode kosong",
                        ],
                        [
                            "D",
                            "Dependency Inv.",
                            "MySQL langsung",
                        ],
                    ],
                },
            ],
        },
    ],
    "Monolit dan Monolit Modular": [
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Satu aplikasi, beberapa paket dengan arah yang jelas",
            "ket": "Susunan aplikasi Belajar Ngoding. Paket di bawah (inti) nggak pernah mengimpor paket yang memakainya.",
            "akar": {
                "teks": "Belajar Ngoding",
                "anak": [
                    {
                        "teks": "inti/",
                        "anak": [
                            {
                                "teks": "runner.py",
                            },
                            {
                                "teks": "sorot.py",
                            },
                        ],
                    },
                    {
                        "teks": "pelajar/",
                        "anak": [
                            {
                                "teks": "progress.py",
                            },
                            {
                                "teks": "bab.py",
                            },
                        ],
                    },
                    {
                        "teks": "layar/",
                        "anak": [
                            {
                                "teks": "materials.py",
                            },
                        ],
                    },
                    {
                        "teks": "webapp/",
                        "anak": [
                            {
                                "teks": "api.py",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Hexagonal, Onion, dan Clean Architecture": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Tiga nama, satu ide: logika bisnis di tengah",
            "ket": "Ketiganya berbeda istilah dan gambar. Aturan yang sama: lapisan dalam nggak mengenal lapisan luar.",
            "tabel": [
                {
                    "kolom": [
                        "pola",
                        "tahun",
                        "di pusat",
                        "di luar",
                    ],
                    "baris": [
                        [
                            "Hexagonal",
                            "2005",
                            "aplikasi",
                            "adapter",
                        ],
                        [
                            "Onion",
                            "2008",
                            "model domain",
                            "infrastruktur",
                        ],
                        [
                            "Clean",
                            "2012",
                            "entities",
                            "frameworks",
                        ],
                    ],
                },
            ],
        },
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Arah import selalu menuju ke dalam",
            "ket": "Panah menunjukkan siapa mengimpor siapa. Entity di ujung nggak mengimpor apa pun dari lapisan lain.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "frameworks & drivers (web, DB)",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "interface adapters",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "use cases (buat pesanan)",
                    "ke": 3,
                },
                {
                    "jenis": "selesai",
                    "teks": "entities (aturan inti)",
                },
            ],
        },
    ],
    "Domain-Driven Design dan Vertical Slice": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Bounded context berisi aggregate, aggregate berisi objek",
            "ket": "Pesanan dan Uang sama dengan contoh kode. Konteks Gudang punya modelnya sendiri walaupun tokonya sama.",
            "akar": {
                "teks": "Toko",
                "anak": [
                    {
                        "teks": "Konteks Penjualan",
                        "anak": [
                            {
                                "teks": "Pesanan (agregat)",
                                "anak": [
                                    {
                                        "teks": "baris pesanan",
                                    },
                                    {
                                        "teks": "Uang (nilai)",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "Konteks Gudang",
                        "anak": [
                            {
                                "teks": "Stok (agregat)",
                                "anak": [
                                    {
                                        "teks": "lokasi rak",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "MVVM, Aliran Data Satu Arah, dan Pola Lainnya": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Aliran data satu arah: aksi, reducer, state, tampilan",
            "ket": "Sesuai contoh reducer: tampilan nggak pernah mengubah state langsung, ia cuma mengirim aksi.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "pengguna klik Tambah",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "kirim aksi {jenis: tambah}",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "reducer(state, aksi)",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "state baru disimpan di store",
                    "ke": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "tampilan digambar ulang",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "menunggu aksi berikutnya",
                },
            ],
        },
    ],
    "Skalabilitas, Stateless, dan Estimasi Kasar": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Skala vertikal dan horizontal",
            "ket": "Horizontal butuh server yang stateless. Vertikal nggak mengubah kode, tapi tetap satu titik gagal.",
            "tabel": [
                {
                    "kolom": [
                        "aspek",
                        "vertikal",
                        "horizontal",
                    ],
                    "baris": [
                        [
                            "caranya",
                            "mesin diperbesar",
                            "tambah mesin",
                        ],
                        [
                            "batas",
                            "mesin terbesar",
                            "lebih longgar",
                        ],
                        [
                            "satu mesin mati",
                            "semua mati",
                            "sisanya jalan",
                        ],
                        [
                            "syarat kode",
                            "nggak berubah",
                            "wajib stateless",
                        ],
                        [
                            "kerumitan",
                            "rendah",
                            "lebih tinggi",
                        ],
                    ],
                },
            ],
        },
    ],
    "Load Balancer dan Reverse Proxy": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Load balancer melewati server yang gagal health check",
            "ket": "Setelah B ketahuan mati, request berikutnya dikirim ke A. Pengguna nggak melihat error.",
            "pelaku": [
                "Klien",
                "Load balancer",
                "Server A",
                "Server B",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /produk",
                ],
                [
                    1,
                    2,
                    "teruskan (giliran A)",
                ],
                [
                    2,
                    1,
                    "200 OK",
                ],
                [
                    1,
                    0,
                    "200 OK",
                ],
                [
                    1,
                    3,
                    "GET /health",
                ],
                [
                    3,
                    1,
                    "timeout: B ditandai mati",
                ],
                [
                    0,
                    1,
                    "GET /keranjang",
                ],
                [
                    1,
                    2,
                    "B dilewati, kirim ke A",
                ],
                [
                    2,
                    1,
                    "200 OK",
                ],
                [
                    1,
                    0,
                    "200 OK",
                ],
            ],
        },
    ],
    "Caching dan CDN": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Cache-aside: cek cache dulu, database kalau terpaksa",
            "ket": "Sama dengan contoh kode: detik 0 miss, detik 10 dan 30 hit, TTL 60 detik.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "permintaan GET produk:1",
                    "ke": 1,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada di cache dan belum basi?",
                    "ya": 2,
                    "tidak": 3,
                },
                {
                    "jenis": "keluaran",
                    "teks": "HIT: kirim dari cache",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "MISS: query ke database",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "simpan ke cache, TTL 60 detik",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "kirim ke pengguna",
                },
            ],
        },
        {
            "setelah": 3,
            "jenis": "larik",
            "judul": "Urutan LRU sesudah PUT tas",
            "ket": "Keadaan akhir contoh di atas. buku dikeluarkan karena paling lama nggak dipakai.",
            "nama": "cache LRU",
            "isi": [
                "map",
                "pena",
                "tas",
            ],
            "penunjuk": {
                "lama": 0,
                "baru": 2,
            },
        },
    ],
    "Gaya Komunikasi API: REST, GraphQL, gRPC, Webhook": [
        {
            "setelah": 9,
            "jenis": "tabel",
            "judul": "Enam gaya komunikasi dan tempatnya",
            "ket": "Sama dengan tabel di atas. Satu sistem boleh memakai beberapa gaya sekaligus.",
            "tabel": [
                {
                    "kolom": [
                        "gaya",
                        "yang memulai",
                        "format",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            "REST",
                            "klien",
                            "JSON",
                            "API publik",
                        ],
                        [
                            "GraphQL",
                            "klien",
                            "JSON pilihan",
                            "tampilan beragam",
                        ],
                        [
                            "gRPC",
                            "klien",
                            "protobuf",
                            "antarlayanan",
                        ],
                        [
                            "WebSocket",
                            "dua arah",
                            "bebas",
                            "chat, game",
                        ],
                        [
                            "SSE",
                            "server",
                            "teks",
                            "notifikasi",
                        ],
                        [
                            "Webhook",
                            "penyedia",
                            "JSON",
                            "integrasi",
                        ],
                    ],
                },
            ],
        },
        {
            "setelah": 7,
            "jenis": "urutan",
            "judul": "Webhook pembayaran: gateway yang mengabari toko",
            "ket": "Toko nggak perlu bertanya terus. Gateway mengirim POST begitu pembayaran lunas, lalu toko membalas 200.",
            "pelaku": [
                "Pembeli",
                "Toko",
                "Gateway bayar",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "checkout pesanan A17",
                ],
                [
                    1,
                    2,
                    "buat tagihan",
                ],
                [
                    2,
                    0,
                    "halaman bayar kode QR",
                ],
                [
                    0,
                    2,
                    "bayar",
                ],
                [
                    2,
                    1,
                    "POST /webhook (lunas)",
                ],
                [
                    1,
                    2,
                    "200 OK",
                ],
                [
                    1,
                    0,
                    "email: pesanan lunas",
                ],
            ],
        },
    ],
    "Memilih Database dan Replikasi": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Ani membaca nama lamanya dari replica",
            "ket": "Sama dengan program di atas: perubahan tiba di replica 300 ms sesudah ditulis.",
            "pelaku": [
                "Aplikasi",
                "Primary",
                "Replica",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "t=1000 UPDATE nama",
                ],
                [
                    1,
                    0,
                    "tersimpan",
                ],
                [
                    0,
                    2,
                    "t=1050 SELECT nama",
                ],
                [
                    2,
                    0,
                    "'Ani' (data lama)",
                ],
                [
                    1,
                    2,
                    "t=1300 perubahan tiba",
                ],
                [
                    0,
                    2,
                    "t=1400 SELECT nama",
                ],
                [
                    2,
                    0,
                    "'Ani Lestari'",
                ],
            ],
        },
    ],
    "Sharding, Consistent Hashing, dan Teorema CAP": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Kunci yang pindah saat 3 shard jadi 4 (mod N)",
            "ket": "Nilai dari program di atas. Baris yang disorot tetap di shard yang sama.",
            "tabel": [
                {
                    "kolom": [
                        "kunci",
                        "mod 3",
                        "mod 4",
                    ],
                    "baris": [
                        [
                            "pelanggan-1",
                            "1",
                            "2",
                        ],
                        [
                            "pelanggan-2",
                            "1",
                            "2",
                        ],
                        [
                            "pelanggan-3",
                            "2",
                            "3",
                        ],
                        [
                            "pelanggan-4",
                            "1",
                            "1",
                        ],
                        [
                            "pelanggan-5",
                            "0",
                            "1",
                        ],
                        [
                            "pelanggan-6",
                            "1",
                            "1",
                        ],
                        [
                            "pelanggan-7",
                            "1",
                            "3",
                        ],
                        [
                            "pelanggan-8",
                            "2",
                            "0",
                        ],
                    ],
                    "sorot_baris": [3, 5],
                },
            ],
            "panah": "6 dari 8 kunci harus dipindah",
        },
    ],
    "Rate Limiting dan Throttling": [
        {
            "setelah": 1,
            "jenis": "tumpukan",
            "judul": "Ember token sesudah dua permintaan",
            "ket": "Kapasitas 5. Tiap permintaan mengambil satu token, ember terisi lagi pelan-pelan.",
            "mode": "tumpukan",
            "isi": [
                "token",
                "token",
                "token",
            ],
            "label": "ember klien: sisa 3 dari 5",
            "operasi": "ambil 1 per request",
        },
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Empat algoritma rate limiting",
            "tabel": [
                {
                    "kolom": [
                        "algoritma",
                        "lonjakan",
                        "disimpan",
                    ],
                    "baris": [
                        [
                            "token bucket",
                            "boleh, terbatas",
                            "2 angka/klien",
                        ],
                        [
                            "leaky bucket",
                            "diratakan",
                            "antrean",
                        ],
                        [
                            "fixed window",
                            "bisa 2x di batas",
                            "1 angka/jendela",
                        ],
                        [
                            "sliding window",
                            "halus",
                            "log atau 2 angka",
                        ],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "High Availability dan Pemulihan Bencana": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Failover aktif-pasif setelah health check gagal",
            "pelaku": [
                "Klien",
                "Pengalih",
                "Primary",
                "Standby",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /saldo",
                ],
                [
                    1,
                    2,
                    "teruskan",
                ],
                [
                    1,
                    2,
                    "GET /health (gagal 3x)",
                ],
                [
                    1,
                    3,
                    "naikkan jadi primary",
                ],
                [
                    0,
                    1,
                    "GET /saldo",
                ],
                [
                    1,
                    3,
                    "teruskan ke primary baru",
                ],
            ],
        },
    ],
    "Microservices: Kapan Memecah dan Berapa Harganya": [
        {
            "setelah": 6,
            "jenis": "alur",
            "judul": "Strangler fig: memindahkan fitur bertahap",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Semua rute ke monolit",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Pasang router di depan monolit",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Bangun satu fitur sebagai layanan",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Alihkan rute fitur itu",
                    "ke": 4,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Masih ada fitur di monolit?",
                    "ya": 2,
                    "tidak": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "Matikan monolit",
                },
            ],
        },
    ],
    "Antrean Pesan dan Event-Driven Architecture": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Produsen dan konsumen nggak harus hidup bersamaan",
            "pelaku": [
                "Checkout",
                "Broker",
                "Worker email",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "titip: email untuk Ani",
                ],
                [
                    1,
                    0,
                    "diterima",
                ],
                [
                    0,
                    1,
                    "titip: email untuk Budi",
                ],
                [
                    2,
                    1,
                    "ambil pesan berikutnya",
                ],
                [
                    1,
                    2,
                    "email untuk Ani",
                ],
                [
                    2,
                    1,
                    "selesai (ack)",
                ],
            ],
        },
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "Isi antrean sesudah dua checkout",
            "ket": "Sama dengan program di atas: yang masuk duluan diambil worker duluan.",
            "mode": "antrean",
            "isi": [
                "email untuk Ani",
                "email untuk Budi",
            ],
            "label": "antrean_email",
            "operasi": "popleft()",
        },
    ],
    "CQRS, Event Sourcing, dan Saga": [
        {
            "setelah": 4,
            "jenis": "larik",
            "judul": "Log event rekening, dengan titik snapshot",
            "ket": "Saldo 380.000 di snapshot, lalu dua event terakhir diputar: hasilnya 255.000.",
            "nama": "events",
            "isi": [
                "dibuka",
                "+500rb",
                "-120rb",
                "+75rb",
                "-200rb",
            ],
            "penunjuk": {
                "snapshot": 2,
            },
            "rentang": [3, 5],
        },
        {
            "setelah": 7,
            "jenis": "alur",
            "judul": "Saga: langkah gagal memicu kompensasi urut terbalik",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Pesanan masuk",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Pesan stok",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Tagih pembayaran",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Kurir didapat?",
                    "ya": 4,
                    "tidak": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "Pesanan dikirim",
                },
                {
                    "jenis": "proses",
                    "teks": "Kompensasi: refund",
                    "ke": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "Kompensasi: kembalikan stok",
                    "ke": 7,
                },
                {
                    "jenis": "selesai",
                    "teks": "Pesanan dibatalkan",
                },
            ],
        },
    ],
    "Retry, Idempotensi, dan Circuit Breaker": [
        {
            "setelah": 6,
            "jenis": "alur",
            "judul": "Tiga keadaan circuit breaker",
            "langkah": [
                {
                    "jenis": "proses",
                    "teks": "Closed: teruskan, hitung gagal",
                    "ke": 1,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Gagal lewat ambang?",
                    "ya": 2,
                    "tidak": 0,
                },
                {
                    "jenis": "proses",
                    "teks": "Open: tolak cepat",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Tunggu masa jeda habis",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Half-open: kirim panggilan uji",
                    "ke": 5,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Panggilan uji berhasil?",
                    "ya": 0,
                    "tidak": 2,
                },
            ],
        },
    ],
    "API Gateway, BFF, dan Service Mesh": [
        {
            "setelah": 5,
            "jenis": "urutan",
            "judul": "Aplikasi HP cukup sekali memanggil BFF",
            "ket": "Sama dengan program di atas: BFF menggabungkan produk dan ongkir.",
            "pelaku": [
                "Aplikasi HP",
                "BFF mobile",
                "Gateway",
                "Layanan",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "produk 7, kota bandung",
                ],
                [
                    1,
                    2,
                    "GET /produk/7",
                ],
                [
                    2,
                    3,
                    "layanan produk",
                ],
                [
                    3,
                    1,
                    "6 kolom produk",
                ],
                [
                    1,
                    2,
                    "GET /ongkir/bandung",
                ],
                [
                    3,
                    1,
                    "biaya 12000",
                ],
                [
                    1,
                    0,
                    "nama, harga, ongkir",
                ],
            ],
        },
    ],
    "CI/CD dan Strategi Deployment": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Jalur dari commit sampai produksi",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Push atau pull request",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Linter dan tes otomatis",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Semua lolos?",
                    "ya": 3,
                    "tidak": 6,
                },
                {
                    "jenis": "proses",
                    "teks": "Bangun artefak bertanda versi",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Deploy ke staging",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "Deploy ke produksi (canary)",
                },
                {
                    "jenis": "selesai",
                    "teks": "Tandai merah, perbaiki dulu",
                },
            ],
        },
    ],
    "Twelve-Factor App, IaC, dan GitOps": [
        {
            "setelah": 8,
            "jenis": "alur",
            "judul": "Keadaan diinginkan dibandingkan keadaan nyata",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Keadaan diinginkan (berkas Git)",
                    "ke": 2,
                },
                {
                    "jenis": "masukan",
                    "teks": "Keadaan nyata (server, cloud)",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Bandingkan keduanya",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Ada perbedaan?",
                    "ya": 4,
                    "tidak": 6,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Rencana: buat, ubah, hapus",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "Review lalu apply",
                    "ke": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "Nyata sama dengan diinginkan",
                },
            ],
        },
    ],
    "Observability, SLO, dan Budaya SRE": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Waktu henti yang diizinkan per 30 hari",
            "ket": "Sama dengan tabel di atas. Tiap angka sembilan tambahan memotong waktu henti sepuluh kali.",
            "tabel": [
                {
                    "kolom": [
                        "SLO",
                        "waktu henti",
                    ],
                    "baris": [
                        [
                            "99%",
                            "7 j 12 m",
                        ],
                        [
                            "99,5%",
                            "3 j 36 m",
                        ],
                        [
                            "99,9%",
                            "43 m 12 d",
                        ],
                        [
                            "99,95%",
                            "21 m 36 d",
                        ],
                        [
                            "99,99%",
                            "4 m 19 d",
                        ],
                    ],
                    "sorot_baris": [2],
                },
            ],
        },
    ],
    "Identitas dan Rantai Pasok dalam Arsitektur": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Login lewat OpenID Connect",
            "ket": "Alur kode otorisasi dengan PKCE. Kata sandi cuma diketik di penyedia identitas.",
            "pelaku": [
                "Pengguna",
                "Aplikasi",
                "Penyedia ID",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "buka /login",
                ],
                [
                    1,
                    0,
                    "alihkan ke penyedia",
                ],
                [
                    0,
                    2,
                    "ketik sandi, setujui",
                ],
                [
                    2,
                    0,
                    "alihkan balik + kode",
                ],
                [
                    0,
                    1,
                    "serahkan kode",
                ],
                [
                    1,
                    2,
                    "tukar kode (+ PKCE)",
                ],
                [
                    2,
                    1,
                    "ID token + access token",
                ],
                [
                    1,
                    0,
                    "cookie sesi aplikasi",
                ],
            ],
        },
    ],
    "ADR, C4 Model, dan Dokumentasi Arsitektur": [
        {
            "setelah": 6,
            "jenis": "pohon",
            "judul": "Empat tingkat zoom C4 untuk toko online",
            "ket": "Akar adalah tingkat 1 (sistem), lalu container, komponen, dan kode.",
            "akar": {
                "teks": "Sistem Toko Melati",
                "anak": [
                    {
                        "teks": "Aplikasi web",
                        "anak": [
                            {
                                "teks": "Modul pesanan",
                                "anak": [
                                    {
                                        "teks": "class Pesanan",
                                    },
                                ],
                            },
                            {
                                "teks": "Modul pembayaran",
                            },
                        ],
                    },
                    {
                        "teks": "Aplikasi HP",
                    },
                    {
                        "teks": "Database",
                    },
                ],
            },
        },
    ],
    "Cara Tim Bekerja: Agile, Monorepo, dan Asisten AI": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Scrum dibandingkan Kanban",
            "tabel": [
                {
                    "kolom": [
                        "aspek",
                        "Scrum",
                        "Kanban",
                    ],
                    "baris": [
                        [
                            "ritme",
                            "sprint tetap",
                            "terus-menerus",
                        ],
                        [
                            "peran",
                            "tiga peran baku",
                            "bebas",
                        ],
                        [
                            "perubahan",
                            "sprint berikut",
                            "kapan saja",
                        ],
                        [
                            "ukuran",
                            "hasil per sprint",
                            "lead time",
                        ],
                    ],
                },
            ],
        },
    ],
    "Cara Memilih Stack: Kriteria, Lisensi, dan Umur": [
        {
            "setelah": 6,
            "jenis": "tabel",
            "judul": "Hasil pemeriksaan lisensi",
            "ket": "Sama dengan keluaran program di atas.",
            "tabel": [
                {
                    "kolom": [
                        "komponen",
                        "lisensi",
                        "status",
                    ],
                    "baris": [
                        [
                            "PostgreSQL",
                            "PostgreSQL",
                            "aman",
                        ],
                        [
                            "MongoDB",
                            "SSPL-1.0",
                            "minta izin",
                        ],
                        [
                            "Redis 8",
                            "RSAL/SSPL/AGPL",
                            "cek copyleft",
                        ],
                        [
                            "Valkey",
                            "BSD-3-Clause",
                            "aman",
                        ],
                        [
                            "Terraform",
                            "BUSL-1.1",
                            "minta izin",
                        ],
                        [
                            "OpenTofu",
                            "MPL-2.0",
                            "cek copyleft",
                        ],
                    ],
                },
            ],
        },
    ],
    "Studi Kasus Memilih Stack untuk Tiga Proyek": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Matriks keputusan toko UMKM, dua skenario bobot",
            "ket": "Nilai dari program di atas. Juaranya berganti saat bobot kendali naik.",
            "tabel": [
                {
                    "kolom": [
                        "calon",
                        "dirawat sendiri",
                        "fitur khusus",
                    ],
                    "baris": [
                        [
                            "WooCommerce",
                            "59",
                            "49",
                        ],
                        [
                            "Laravel+Livewire",
                            "45",
                            "50",
                        ],
                        [
                            "Next.js+Supabase",
                            "40",
                            "46",
                        ],
                    ],
                },
            ],
        },
    ],
}
