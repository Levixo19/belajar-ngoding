"""Gambar konsep kurikulum Frontend Modern. Skema: inti/visual.py."""

VISUAL = {
    "Kenapa Framework Frontend Ada": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Satu jalur untuk setiap perubahan",
            "ket": "Handler cuma mengubah state. Tampilan selalu dibuat dari state, jadi nggak bisa ketinggalan.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Pengguna klik Tambah",
                },
                {
                    "jenis": "proses",
                    "teks": "Handler mengubah state",
                },
                {
                    "jenis": "proses",
                    "teks": "tampilan(state) dipanggil ulang",
                },
                {
                    "jenis": "proses",
                    "teks": "Bandingkan dengan tampilan lama",
                },
                {
                    "jenis": "keluaran",
                    "teks": "DOM yang beda saja diubah",
                },
            ],
        },
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "DOM manual dan framework untuk pekerjaan yang sama",
            "tabel": [
                {
                    "kolom": [
                        "urusan",
                        "DOM manual",
                        "framework",
                    ],
                    "baris": [
                        [
                            "data berubah",
                            "ubah tiap elemen",
                            "ubah state",
                        ],
                        [
                            "tampilan baru",
                            "cari tiap tempat",
                            "ubah satu fungsi",
                        ],
                        [
                            "dipakai ulang",
                            "salin HTML",
                            "pakai komponen",
                        ],
                        [
                            "biaya awal",
                            "nol",
                            "belajar + build",
                        ],
                    ],
                },
            ],
        },
    ],
    "Node.js dan npm sebagai Alat Kerja": [
        {
            "setelah": 8,
            "jenis": "pohon",
            "judul": "Folder proyek sesudah npm install",
            "ket": "Yang di-commit: package.json, lockfile, dan src. node_modules dibuat ulang dari lockfile.",
            "akar": {
                "teks": "toko-kopi/",
                "anak": [
                    {
                        "teks": "package.json",
                    },
                    {
                        "teks": "package-lock.json",
                    },
                    {
                        "teks": ".gitignore",
                    },
                    {
                        "teks": "src/",
                        "anak": [
                            {
                                "teks": "main.js",
                            },
                        ],
                    },
                    {
                        "teks": "node_modules/",
                        "anak": [
                            {
                                "teks": "react/",
                            },
                            {
                                "teks": "vite/",
                            },
                            {
                                "teks": "(ratusan lagi)",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "pnpm, Yarn, dan Manajer Versi Node": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Empat manajer paket, satu package.json",
            "ket": "Semua membaca package.json yang sama. Yang beda lockfile dan cara menyimpan paket.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "lockfile",
                        "node_modules",
                    ],
                    "baris": [
                        [
                            "npm",
                            "package-lock",
                            "rata, disalin",
                        ],
                        [
                            "pnpm",
                            "pnpm-lock.yaml",
                            "tautan, ketat",
                        ],
                        [
                            "Yarn 4",
                            "yarn.lock",
                            "PnP atau biasa",
                        ],
                        [
                            "bun install",
                            "bun.lock",
                            "rata, cepat",
                        ],
                    ],
                },
            ],
        },
    ],
    "WCAG 2.2 dan Kontras Warna": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Ambang kontras WCAG 2.2",
            "ket": "Teks besar: minimal 24px, atau 18,66px tebal. Rasio dibandingkan tanpa dibulatkan.",
            "tabel": [
                {
                    "kolom": [
                        "isi",
                        "AA",
                        "AAA",
                    ],
                    "baris": [
                        [
                            "teks normal",
                            "4,5:1",
                            "7:1",
                        ],
                        [
                            "teks besar",
                            "3:1",
                            "4,5:1",
                        ],
                        [
                            "ikon dan garis",
                            "3:1",
                            "-",
                        ],
                    ],
                    "sorot_kolom": [
                        "AA",
                    ],
                },
            ],
        },
    ],
    "WAI-ARIA dan Nama yang Dibacakan": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Pohon aksesibilitas sebuah kartu produk",
            "ket": "Div pembungkus dan ikon hiasan nggak muncul. Yang tersisa cuma elemen yang punya peran dan nama.",
            "akar": {
                "teks": "dokumen",
                "anak": [
                    {
                        "teks": "navigation",
                        "anak": [
                            {
                                "teks": "link: Beranda",
                            },
                            {
                                "teks": "link: Promo",
                            },
                        ],
                    },
                    {
                        "teks": "main",
                        "anak": [
                            {
                                "teks": "heading: Kopi",
                            },
                            {
                                "teks": "img: Kopi susu",
                            },
                            {
                                "teks": "button: Tambah",
                            },
                            {
                                "teks": "button: (kosong)",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "DevTools dan Alat Uji Aksesibilitas": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Alat uji aksesibilitas dan kapan dipakai",
            "ket": "Angka pemakai dari State of HTML 2025. Semua alat ini cuma menangkap masalah yang bisa dihitung mesin.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "dipakai saat",
                        "pemakai SoHTML",
                    ],
                    "baris": [
                        [
                            "DevTools",
                            "menulis kode",
                            "2.259",
                        ],
                        [
                            "Lighthouse",
                            "audit halaman",
                            "1.983",
                        ],
                        [
                            "axe-core",
                            "tes dan CI",
                            "1.145",
                        ],
                        [
                            "WAVE",
                            "tinjau visual",
                            "648",
                        ],
                        [
                            "Insights",
                            "uji terpandu",
                            "523",
                        ],
                        [
                            "Pa11y",
                            "banyak URL",
                            "188",
                        ],
                    ],
                },
            ],
        },
    ],
    "Pembaca Layar: Mencoba Orca di Fedora": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Pembaca layar dan tempatnya",
            "ket": "Orca bisa langsung dicoba di Fedora. Pengguna desktop sungguhan paling banyak memakai NVDA dan JAWS.",
            "tabel": [
                {
                    "kolom": [
                        "nama",
                        "sistem",
                        "lisensi",
                    ],
                    "baris": [
                        [
                            "Orca",
                            "Linux GNOME",
                            "LGPL",
                        ],
                        [
                            "NVDA",
                            "Windows",
                            "GPL-2.0",
                        ],
                        [
                            "JAWS",
                            "Windows",
                            "berbayar",
                        ],
                        [
                            "Narrator",
                            "Windows",
                            "bawaan",
                        ],
                        [
                            "VoiceOver",
                            "Apple",
                            "bawaan",
                        ],
                        [
                            "TalkBack",
                            "Android",
                            "bawaan",
                        ],
                        [
                            "ChromeVox",
                            "ChromeOS",
                            "bawaan",
                        ],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Komponen dan Virtual DOM dari Nol": [
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Pohon virtual DOM untuk menu di atas",
            "ket": "Komponen Kartu dan Harga sudah dipanggil, jadi yang tersisa cuma tag HTML dan teks.",
            "akar": {
                "teks": "ul#menu",
                "anak": [
                    {
                        "teks": "li",
                        "anak": [
                            {
                                "teks": "b",
                                "anak": [
                                    {
                                        "teks": "\"Kopi <susu>\"",
                                    },
                                ],
                            },
                            {
                                "teks": "\" \"",
                            },
                            {
                                "teks": "span.harga",
                                "anak": [
                                    {
                                        "teks": "\"Rp\"",
                                    },
                                    {
                                        "teks": "18000",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "li",
                        "anak": [
                            {
                                "teks": "b",
                                "anak": [
                                    {
                                        "teks": "\"Teh tarik\"",
                                    },
                                ],
                            },
                            {
                                "teks": "\" \"",
                            },
                            {
                                "teks": "span.harga",
                            },
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Contoh daftar patch dari satu diff",
            "ket": "Pohon lama tiga tugas, pohon baru dua tugas plus satu paragraf. Jalur dihitung dari 0.",
            "tabel": [
                {
                    "kolom": [
                        "patch",
                        "jalur",
                        "isi",
                    ],
                    "baris": [
                        [
                            "ATRIBUT",
                            "0.1.0",
                            "class -> selesai",
                        ],
                        [
                            "TEKS",
                            "0.1.1.0",
                            "motor -> mobil",
                        ],
                        [
                            "HAPUS",
                            "0.1.2",
                            "<li>",
                        ],
                        [
                            "TAMBAH",
                            "0.2",
                            "<p>",
                        ],
                        [
                            "GANTI",
                            "0.3",
                            "<p> -> <div>",
                        ],
                    ],
                },
            ],
        },
    ],
    "Signal dan Proxy Reaktif dari Nol": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Perjalanan satu perubahan signal",
            "ket": "Effect yang nggak membaca signal itu nggak pernah dipanggil.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "jumlah.value = 2",
                },
                {
                    "jenis": "proses",
                    "teks": "Ambil daftar pelanggan jumlah",
                },
                {
                    "jenis": "keputusan",
                    "teks": "Masih ada pelanggan?",
                    "ya": 3,
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "Jalankan ulang efeknya",
                },
                {
                    "jenis": "proses",
                    "teks": "Catat ulang signal yang dibaca",
                    "ke": 2,
                },
                {
                    "jenis": "selesai",
                    "teks": "Tampilan sudah baru",
                },
            ],
        },
    ],
    "Render di Server, Statis, dan Hydration": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "SSR lalu hydration",
            "ket": "Halaman sudah terlihat sejak HTML tiba, tapi baru bisa diklik sesudah hydration.",
            "pelaku": [
                "browser",
                "server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /produk/kopi",
                ],
                [
                    1,
                    1,
                    "renderToString(App)",
                ],
                [
                    1,
                    0,
                    "HTML lengkap",
                ],
                [
                    0,
                    0,
                    "tampil, belum bisa diklik",
                ],
                [
                    0,
                    1,
                    "GET app.js",
                ],
                [
                    1,
                    0,
                    "berkas JavaScript",
                ],
                [
                    0,
                    0,
                    "hydrate: pasang listener",
                ],
            ],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Kapan HTML dibuat di tiap mode",
            "tabel": [
                {
                    "kolom": [
                        "mode",
                        "HTML dibuat",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            "CSR",
                            "di browser",
                            "dasbor login",
                        ],
                        [
                            "SSR",
                            "tiap permintaan",
                            "stok berubah",
                        ],
                        [
                            "SSG",
                            "saat build",
                            "blog, dokumen",
                        ],
                        [
                            "ISR",
                            "build + berkala",
                            "katalog besar",
                        ],
                        [
                            "islands",
                            "build/server",
                            "interaksi kecil",
                        ],
                    ],
                },
            ],
        },
    ],
    "Web Components, Lit, dan Stencil": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Shadow root di dalam kartu-produk",
            "ket": "Isi dari luar (small) tetap di light DOM dan ditampilkan di tempat slot.",
            "akar": {
                "teks": "kartu-produk",
                "anak": [
                    {
                        "teks": "#shadow-root",
                        "anak": [
                            {
                                "teks": "style",
                            },
                            {
                                "teks": "div.kartu",
                                "anak": [
                                    {
                                        "teks": "b",
                                    },
                                    {
                                        "teks": "span",
                                    },
                                    {
                                        "teks": "slot",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "small (light DOM)",
                    },
                ],
            },
        },
    ],
    "Tailwind CSS: Berpikir dengan Kelas Utility": [
        {
            "setelah": 3,
            "jenis": "tata",
            "judul": "Kartu dengan md:flex-row md:items-center",
            "ket": "Di layar 48rem ke atas isi kartu berjajar. Di ponsel, flex-col membuatnya bertumpuk.",
            "mode": "flex",
            "arah": "row",
            "align": "center",
            "item": [
                "img",
                "judul+harga",
                "tombol Beli",
            ],
        },
    ],
    "Tailwind v4: Tema, Varian, dan Plugin": [
        {
            "setelah": 10,
            "jenis": "tabel",
            "judul": "Yang berubah dari Tailwind v3 ke v4",
            "tabel": [
                {
                    "kolom": [
                        "urusan",
                        "v3",
                        "v4",
                    ],
                    "baris": [
                        [
                            "konfigurasi",
                            "config.js",
                            "@theme di CSS",
                        ],
                        [
                            "memuat",
                            "@tailwind x3",
                            "@import",
                        ],
                        [
                            "cari kelas",
                            "content manual",
                            "otomatis",
                        ],
                        [
                            "plugin",
                            "plugins: [...]",
                            "@plugin",
                        ],
                        [
                            "container query",
                            "plugin",
                            "bawaan",
                        ],
                    ],
                    "sorot_kolom": [
                        "v4",
                    ],
                },
            ],
        },
    ],
    "Sass, PostCSS, dan Pipeline CSS": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Perjalanan CSS dari editor ke browser",
            "ket": "Nggak semua proyek memakai semua tahap. Proyek Tailwind biasanya tanpa Sass dan PurgeCSS.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "gaya.scss yang kamu tulis",
                },
                {
                    "jenis": "proses",
                    "teks": "Sass: jadi CSS biasa",
                },
                {
                    "jenis": "proses",
                    "teks": "Stylelint: cek kesalahan",
                },
                {
                    "jenis": "proses",
                    "teks": "PostCSS: prefix, fitur baru",
                },
                {
                    "jenis": "proses",
                    "teks": "Buang kelas tak terpakai",
                },
                {
                    "jenis": "proses",
                    "teks": "Minify: cssnano / Lightning",
                },
                {
                    "jenis": "keluaran",
                    "teks": "style.min.css ke browser",
                },
            ],
        },
    ],
    "Bootstrap, CSS Modules, dan Peta Cara Menata Gaya": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Kapan gaya dibuat, dan statusnya",
            "ket": "Kolom kedua menentukan biaya di browser. Yang dibuat saat build nggak menambah kerja saat halaman berjalan.",
            "tabel": [
                {
                    "kolom": [
                        "pendekatan",
                        "CSS dibuat",
                        "status",
                    ],
                    "baris": [
                        [
                            "Bootstrap",
                            "sudah jadi",
                            "stabil-matang",
                        ],
                        [
                            "Tailwind",
                            "saat build",
                            "aktif",
                        ],
                        [
                            "CSS Modules",
                            "saat build",
                            "stabil-matang",
                        ],
                        [
                            "styled-comp.",
                            "di browser",
                            "perawatan",
                        ],
                        [
                            "Emotion",
                            "di browser",
                            "menurun",
                        ],
                        [
                            "vanilla-extract",
                            "saat build",
                            "aktif",
                        ],
                        [
                            "StyleX",
                            "saat build",
                            "aktif, 0.x",
                        ],
                    ],
                },
            ],
        },
    ],
    "Bundler dari Nol: Graf Modul dan Tree-Shaking": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Tiga tahap kerja bundler",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Entry: main.js",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Resolve: ikuti tiap import",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Transform: buang tipe, ubah JSX",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Tree-shaking dan minify",
                    "ke": 4,
                },
                {
                    "jenis": "selesai",
                    "teks": "Bundel di folder dist/",
                },
            ],
        },
        {
            "setelah": 5,
            "jenis": "pohon",
            "judul": "Graf modul dari main.js",
            "ket": "lama.js nggak pernah di-import, jadi nggak muncul di graf.",
            "akar": {
                "teks": "main.js",
                "anak": [
                    {
                        "teks": "uang.js",
                        "anak": [
                            {
                                "teks": "formatRupiah",
                            },
                        ],
                    },
                    {
                        "teks": "teks.js",
                        "anak": [
                            {
                                "teks": "sapa",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Vite 8 dan Rolldown": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Dev server Vite melayani modul satu per satu",
            "pelaku": [
                "browser",
                "dev server",
                "berkas src/",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /src/main.tsx",
                ],
                [
                    1,
                    2,
                    "baca main.tsx",
                ],
                [
                    1,
                    0,
                    "JS tanpa tipe dan JSX",
                ],
                [
                    0,
                    1,
                    "GET /src/App.tsx",
                ],
                [
                    1,
                    0,
                    "App.tsx versi JS",
                ],
                [
                    2,
                    1,
                    "App.tsx disimpan ulang",
                ],
                [
                    1,
                    0,
                    "HMR: tukar App saja",
                ],
            ],
        },
    ],
    "Peta Build Tool: webpack sampai Turbopack": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Bundler yang paling sering kamu temui",
            "tabel": [
                {
                    "kolom": [
                        "Alat",
                        "Ditulis",
                        "Status",
                        "Dipakai oleh",
                    ],
                    "baris": [
                        [
                            "webpack",
                            "JavaScript",
                            "menurun",
                            "proyek lama",
                        ],
                        [
                            "Vite",
                            "TS + Rust",
                            "aktif",
                            "proyek baru",
                        ],
                        [
                            "Rspack",
                            "Rust",
                            "aktif",
                            "migrasi webpack",
                        ],
                        [
                            "esbuild",
                            "Go",
                            "aktif",
                            "Angular CLI",
                        ],
                        [
                            "Turbopack",
                            "Rust",
                            "aktif",
                            "Next.js 16",
                        ],
                        [
                            "Parcel",
                            "JS + Rust",
                            "stabil-matang",
                            "prototipe",
                        ],
                    ],
                    "sorot_baris": [1],
                },
            ],
        },
    ],
    "TypeScript di Proyek Frontend": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Siapa mengerjakan apa pada berkas .ts",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Berkas App.tsx",
                    "ke": 1,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Perintah yang dijalankan?",
                    "ya": 2,
                    "tidak": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "tsc --noEmit: cek tipe",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Vite: buang tipe, ubah JSX",
                    "ke": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Daftar error tipe",
                },
                {
                    "jenis": "keluaran",
                    "teks": "JavaScript untuk browser",
                },
            ],
            "ket": "Cabang ya = tsc, cabang tidak = Vite. Keduanya membaca berkas yang sama.",
        },
    ],
    "ESLint 10, Prettier, dan Biome": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Linter dan formatter",
            "tabel": [
                {
                    "kolom": [
                        "Hal",
                        "Linter",
                        "Formatter",
                    ],
                    "baris": [
                        [
                            "Peduli pada",
                            "pola rawan bug",
                            "tampilan kode",
                        ],
                        [
                            "Contoh temuan",
                            "== bukan ===",
                            "indentasi",
                        ],
                        [
                            "Bisa mengubah",
                            "sebagian (--fix)",
                            "seluruh berkas",
                        ],
                        [
                            "Alat utama",
                            "ESLint",
                            "Prettier",
                        ],
                        [
                            "Alternatif Rust",
                            "oxlint, Biome",
                            "Biome, oxfmt",
                        ],
                    ],
                },
            ],
        },
    ],
    "React: JSX, Komponen, dan Props": [
        {
            "setelah": 6,
            "jenis": "pohon",
            "judul": "Props mengalir dari induk ke anak",
            "ket": "Tiap simpul adalah komponen; panahnya arah props.",
            "akar": {
                "teks": "App",
                "anak": [
                    {
                        "teks": "Header",
                        "anak": [
                            {
                                "teks": "Logo",
                            },
                            {
                                "teks": "Keranjang jumlah=3",
                            },
                        ],
                    },
                    {
                        "teks": "DaftarProduk",
                        "anak": [
                            {
                                "teks": "KartuProduk Kopi",
                            },
                            {
                                "teks": "KartuProduk Teh",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "State, Hooks, dan Efek di React": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Satu klik sampai efek berjalan",
            "pelaku": [
                "pengguna",
                "komponen",
                "React",
                "DOM",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "klik tombol",
                ],
                [
                    1,
                    2,
                    "setAngka(a => a + 1)",
                ],
                [
                    2,
                    1,
                    "render: panggil Penghitung()",
                ],
                [
                    1,
                    2,
                    "pohon elemen baru",
                ],
                [
                    2,
                    3,
                    "commit: ubah teks tombol",
                ],
                [
                    2,
                    1,
                    "jalankan useEffect",
                ],
            ],
        },
    ],
    "React Modern: Context, Suspense, dan Server Components": [
        {
            "setelah": 5,
            "jenis": "pohon",
            "judul": "Batas server dan klien di satu halaman",
            "ket": "Yang bertanda klien ikut dikirim ke browser sebagai JavaScript.",
            "akar": {
                "teks": "layout (server)",
                "anak": [
                    {
                        "teks": "Header (server)",
                        "anak": [
                            {
                                "teks": "Cari (klien)",
                            },
                        ],
                    },
                    {
                        "teks": "HalamanProduk",
                        "anak": [
                            {
                                "teks": "Kartu (server)",
                            },
                            {
                                "teks": "TombolSuka (klien)",
                            },
                        ],
                    },
                    {
                        "teks": "Footer (server)",
                    },
                ],
            },
        },
    ],
    "Mengetik Komponen React dengan TypeScript": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Pola tipe yang paling sering dipakai",
            "tabel": [
                {
                    "kolom": [
                        "Kebutuhan",
                        "Tipe",
                    ],
                    "baris": [
                        [
                            "isi komponen",
                            "ReactNode",
                        ],
                        [
                            "ketik di input",
                            "ChangeEvent<...>",
                        ],
                        [
                            "kirim form",
                            "FormEvent<...>",
                        ],
                        [
                            "boleh kosong",
                            "useState<T|null>",
                        ],
                        [
                            "ref elemen",
                            "useRef<HTMLxxx>",
                        ],
                        [
                            "semua atribut",
                            "ComponentProps<>",
                        ],
                    ],
                },
            ],
        },
    ],
    "Rute di React: React Router dan TanStack Router": [
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Rute bersarang dan Outlet",
            "ket": "Tata selalu tampil; anaknya dirender di dalam <Outlet />.",
            "akar": {
                "teks": "/ (Tata)",
                "anak": [
                    {
                        "teks": "index: Beranda",
                    },
                    {
                        "teks": "produk",
                        "anak": [
                            {
                                "teks": ":id DetailProduk",
                                "anak": [
                                    {
                                        "teks": "ulasan",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "* TidakDitemukan",
                    },
                ],
            },
        },
    ],
    "Server State: TanStack Query, SWR, dan Klien API": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Stale-while-revalidate",
            "pelaku": [
                "komponen",
                "cache",
                "server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "minta ['produk', 1]",
                ],
                [
                    1,
                    2,
                    "belum ada: GET /produk/1",
                ],
                [
                    2,
                    1,
                    "data versi 1",
                ],
                [
                    1,
                    0,
                    "tampilkan versi 1",
                ],
                [
                    0,
                    1,
                    "minta lagi (sudah basi)",
                ],
                [
                    1,
                    0,
                    "versi 1 seketika",
                ],
                [
                    1,
                    2,
                    "ambil ulang di latar",
                ],
                [
                    2,
                    1,
                    "data versi 2",
                ],
                [
                    1,
                    0,
                    "render ulang versi 2",
                ],
            ],
        },
    ],
    "Client State: Redux Toolkit, Zustand, dan Jotai": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Satu putaran Redux",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Klik: tambah ke keranjang",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "dispatch(tambah('Kopi'))",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "reducer(state, action)",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "store menyimpan state baru",
                    "ke": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "komponen pelanggan render ulang",
                },
            ],
        },
    ],
    "Form dan Validasi: React Hook Form dan Zod": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Perjalanan satu kiriman form",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "Pengguna menekan Daftar",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "handleSubmit baca semua input",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Lolos skema Zod?",
                    "ya": 3,
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "kirim(data) ke server",
                    "ke": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "Error per kolom di layar",
                },
                {
                    "jenis": "selesai",
                    "teks": "Server memvalidasi lagi",
                },
            ],
        },
    ],
    "Vue: Template dan Reaktivitas": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Dari perubahan data ke tampilan",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "jumlah.value = 3",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "setter memberi tahu pelanggan",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "computed total ditandai basi",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "render masuk antrean",
                    "ke": 4,
                },
                {
                    "jenis": "keluaran",
                    "teks": "DOM diperbarui sekali",
                },
            ],
        },
    ],
    "Vue Composition API dan Komponen Satu Berkas": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Props turun, event naik",
            "ket": "Data mengalir ke bawah lewat props; anak memberi kabar lewat emit.",
            "akar": {
                "teks": "App.vue",
                "anak": [
                    {
                        "teks": "Header.vue",
                        "anak": [
                            {
                                "teks": "props: jumlah=2",
                            },
                        ],
                    },
                    {
                        "teks": "DaftarProduk.vue",
                        "anak": [
                            {
                                "teks": "KartuProduk Kopi",
                                "anak": [
                                    {
                                        "teks": "emit: tambah",
                                    },
                                ],
                            },
                            {
                                "teks": "KartuProduk Teh",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Pinia, Vue Router, dan Peta Ekosistem Vue": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Ekosistem Vue sekilas",
            "tabel": [
                {
                    "kolom": [
                        "Pustaka",
                        "Peran",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Pinia",
                            "store resmi",
                            "aktif",
                        ],
                        [
                            "Vuex",
                            "store lama",
                            "usang",
                        ],
                        [
                            "Vue Router",
                            "rute resmi",
                            "aktif",
                        ],
                        [
                            "Vuetify",
                            "komponen",
                            "aktif",
                        ],
                        [
                            "Element Plus",
                            "komponen admin",
                            "aktif",
                        ],
                        [
                            "Quasar",
                            "lintas platform",
                            "aktif",
                        ],
                        [
                            "VeeValidate",
                            "validasi form",
                            "stabil-matang",
                        ],
                        [
                            "Vuelidate",
                            "validasi form",
                            "menurun",
                        ],
                    ],
                    "sorot_baris": [0, 2],
                },
            ],
        },
    ],
    "Angular: Komponen Standalone, Template, dan Signals": [
        {
            "setelah": 8,
            "jenis": "tabel",
            "judul": "Angular lama dan modern",
            "tabel": [
                {
                    "kolom": [
                        "Hal",
                        "Lama",
                        "Sekarang",
                    ],
                    "baris": [
                        [
                            "Wadah",
                            "NgModule",
                            "standalone",
                        ],
                        [
                            "Kontrol alur",
                            "*ngIf, *ngFor",
                            "@if, @for",
                        ],
                        [
                            "Data masuk",
                            "@Input()",
                            "input()",
                        ],
                        [
                            "Perubahan",
                            "Zone.js",
                            "signals",
                        ],
                        [
                            "Injeksi",
                            "constructor",
                            "inject()",
                        ],
                        [
                            "Tes unit",
                            "Karma",
                            "Vitest",
                        ],
                    ],
                },
            ],
        },
    ],
    "Dependency Injection, Service, dan RxJS di Angular": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Injector bertingkat",
            "ket": "inject() mencari dari injector terdekat, lalu naik ke akar.",
            "akar": {
                "teks": "Injector akar",
                "anak": [
                    {
                        "teks": "LayananProduk",
                        "anak": [],
                    },
                    {
                        "teks": "HalamanToko",
                        "anak": [
                            {
                                "teks": "DaftarProduk",
                            },
                            {
                                "teks": "Keranjang",
                                "anak": [
                                    {
                                        "teks": "LayananDiskon",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
        {
            "setelah": 6,
            "jenis": "urutan",
            "judul": "Aliran ketikan melewati operator",
            "pelaku": [
                "input",
                "debounceTime",
                "distinct",
                "switchMap",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "k, ko, kop (cepat)",
                ],
                [
                    1,
                    2,
                    "kop pada t=550",
                ],
                [
                    2,
                    3,
                    "kop",
                ],
                [
                    0,
                    1,
                    "kopi, kopi , kopi s",
                ],
                [
                    1,
                    2,
                    "kopi s pada t=1400",
                ],
                [
                    2,
                    3,
                    "kopi s (batalkan kop)",
                ],
                [
                    0,
                    1,
                    "kopi s lagi",
                ],
                [
                    1,
                    2,
                    "kopi s pada t=2100",
                ],
            ],
        },
    ],
    "Peta Ekosistem Angular: NgRx, Material, dan Analog": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Ekosistem Angular sekilas",
            "tabel": [
                {
                    "kolom": [
                        "Pustaka",
                        "Peran",
                        "Status",
                    ],
                    "baris": [
                        [
                            "NgRx",
                            "state",
                            "aktif",
                        ],
                        [
                            "NGXS",
                            "state",
                            "aktif",
                        ],
                        [
                            "Elf",
                            "state RxJS",
                            "menurun",
                        ],
                        [
                            "Angular Material",
                            "komponen resmi",
                            "aktif",
                        ],
                        [
                            "Analog",
                            "meta-framework",
                            "aktif",
                        ],
                        [
                            "AngularJS",
                            "generasi pertama",
                            "usang",
                        ],
                    ],
                    "sorot_baris": [5],
                },
            ],
        },
    ],
    "Svelte 5: Komponen dan Runes": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari berkas .svelte ke DOM, tanpa virtual DOM",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Berkas Penghitung.svelte",
                },
                {
                    "jenis": "proses",
                    "teks": "Compiler membaca rune dan markup",
                },
                {
                    "jenis": "proses",
                    "teks": "Keluar JS biasa + CSS terlingkup",
                },
                {
                    "jenis": "proses",
                    "teks": "jumlah++ memanggil pembaruan",
                },
                {
                    "jenis": "selesai",
                    "teks": "Satu simpul teks di DOM berubah",
                },
            ],
        },
    ],
    "SvelteKit: Rute, Load, dan Form Action": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Folder src/routes menentukan alamat halaman",
            "akar": {
                "teks": "src/routes",
                "anak": [
                    {
                        "teks": "+layout.svelte",
                    },
                    {
                        "teks": "+page.svelte  /",
                    },
                    {
                        "teks": "tentang",
                        "anak": [
                            {
                                "teks": "+page.svelte",
                            },
                        ],
                    },
                    {
                        "teks": "menu",
                        "anak": [
                            {
                                "teks": "+page.server.js",
                            },
                            {
                                "teks": "+page.svelte",
                            },
                            {
                                "teks": "[id]",
                                "anak": [
                                    {
                                        "teks": "+page.js",
                                    },
                                    {
                                        "teks": "+page.svelte",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "htmx, Alpine.js, dan Hotwire: HTML dari Server": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Klik tombol ber-hx-get sampai isinya tertukar",
            "pelaku": [
                "pengguna",
                "htmx",
                "server",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "klik tombol hx-get=/menu",
                ],
                [
                    1,
                    2,
                    "GET /menu",
                ],
                [
                    2,
                    1,
                    "potongan HTML <p>...</p>",
                ],
                [
                    1,
                    0,
                    "isi #isi diganti (innerHTML)",
                ],
            ],
        },
    ],
    "Peta Framework UI: Solid, Preact, Qwik, dan Lainnya": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Framework di luar empat besar dan ide utamanya",
            "tabel": [
                {
                    "kolom": [
                        "Framework",
                        "Ide utama",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Solid",
                            "signal",
                            "aktif",
                        ],
                        [
                            "Preact",
                            "React 3 kB",
                            "aktif",
                        ],
                        [
                            "Qwik",
                            "resumable",
                            "menurun",
                        ],
                        [
                            "Ember.js",
                            "konvensi",
                            "stabil-matang",
                        ],
                        [
                            "Elm",
                            "bahasa sendiri",
                            "stabil-matang",
                        ],
                        [
                            "Marko",
                            "streaming HTML",
                            "aktif",
                        ],
                        [
                            "Aurelia",
                            "binding 2 arah",
                            "menurun",
                        ],
                        [
                            "Blazor",
                            "C# + Wasm",
                            "aktif",
                        ],
                    ],
                },
            ],
        },
    ],
    "Kode Warisan: jQuery, Moment, dan Penggantinya": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Pustaka lama dan pengganti modernnya",
            "tabel": [
                {
                    "kolom": [
                        "Pustaka lama",
                        "Pengganti",
                    ],
                    "baris": [
                        [
                            "jQuery",
                            "DOM API bawaan",
                        ],
                        [
                            "$.ajax",
                            "fetch",
                        ],
                        [
                            "Backbone.js",
                            "React/Vue/Svelte",
                        ],
                        [
                            "Knockout.js",
                            "signal, Vue",
                        ],
                        [
                            "Lodash",
                            "fungsi bawaan",
                        ],
                        [
                            "Moment.js",
                            "date-fns, Day.js",
                        ],
                        [
                            "core-js penuh",
                            "polyfill perlu",
                        ],
                    ],
                },
            ],
            "ket": "Lodash masih dirawat; yang lain di kolom kiri sebaiknya nggak dipilih untuk proyek baru.",
        },
    ],
    "Unit Test: node:test, Vitest, dan Jest": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Tiga langkah satu unit test",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Arrange: siapkan keranjang",
                },
                {
                    "jenis": "proses",
                    "teks": "Act: panggil hitungTotal()",
                },
                {
                    "jenis": "keputusan",
                    "teks": "Assert: hasil === 48000?",
                    "ya": 3,
                    "tidak": 4,
                },
                {
                    "jenis": "selesai",
                    "teks": "Tes lulus",
                },
                {
                    "jenis": "keluaran",
                    "teks": "Tes gagal: cetak nilai nyata",
                },
            ],
        },
    ],
    "Testing Library dan DOM Palsu": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Pohon peran yang dilihat getByRole",
            "akar": {
                "teks": "form",
                "anak": [
                    {
                        "teks": "heading Masuk",
                    },
                    {
                        "teks": "textbox Email",
                    },
                    {
                        "teks": "password: tanpa",
                    },
                    {
                        "teks": "button Masuk",
                    },
                    {
                        "teks": "div diklik: tanpa",
                    },
                ],
            },
            "ket": "Input password dan div yang bisa diklik nggak punya peran, jadi getByRole nggak menemukannya.",
        },
    ],
    "Mock API dengan MSW dan Katalog Komponen Storybook": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "MSW mencegat fetch sebelum keluar ke jaringan",
            "pelaku": [
                "kode aplikasi",
                "fetch",
                "handler MSW",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "fetch('/api/users/7')",
                ],
                [
                    1,
                    2,
                    "cocok GET /api/users/:id",
                ],
                [
                    2,
                    1,
                    "HttpResponse.json(...)",
                ],
                [
                    1,
                    0,
                    "respons palsu status 200",
                ],
            ],
        },
    ],
    "End-to-End dengan Playwright dan Peta Alat E2E": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Piramida tes: dari dasar yang banyak ke puncak yang sedikit",
            "tabel": [
                {
                    "kolom": [
                        "Lapisan",
                        "Alat",
                        "Jumlah tes",
                    ],
                    "baris": [
                        [
                            "E2E",
                            "Playwright",
                            "sedikit",
                        ],
                        [
                            "Komponen",
                            "Testing Library",
                            "sedang",
                        ],
                        [
                            "Unit",
                            "node:test/Vitest",
                            "banyak",
                        ],
                        [
                            "Katalog",
                            "Storybook",
                            "per komponen",
                        ],
                    ],
                },
            ],
        },
    ],
    "Next.js: App Router dan Server Components": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Folder app/ dan alamat yang dihasilkannya",
            "akar": {
                "teks": "app",
                "anak": [
                    {
                        "teks": "layout.tsx",
                    },
                    {
                        "teks": "page.tsx  /",
                    },
                    {
                        "teks": "menu",
                        "anak": [
                            {
                                "teks": "page.tsx  /menu",
                            },
                            {
                                "teks": "[id]",
                                "anak": [
                                    {
                                        "teks": "page.tsx",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "docs",
                        "anak": [
                            {
                                "teks": "[...slug]",
                                "anak": [
                                    {
                                        "teks": "page.tsx",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "teks": "(pemasaran)",
                        "anak": [
                            {
                                "teks": "tentang",
                            },
                        ],
                    },
                    {
                        "teks": "api/pesanan",
                        "anak": [
                            {
                                "teks": "route.ts",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "Next.js: Data, Cache, dan Deploy": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Satu permintaan: kerangka dulu, bagian dinamis menyusul",
            "pelaku": [
                "browser",
                "server Next",
                "database",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /menu",
                ],
                [
                    1,
                    2,
                    "daftarMenu() jika cache kosong",
                ],
                [
                    2,
                    1,
                    "baris menu (disimpan cache)",
                ],
                [
                    1,
                    0,
                    "HTML kerangka + daftar menu",
                ],
                [
                    1,
                    2,
                    "ambilPoin(sesi)",
                ],
                [
                    2,
                    1,
                    "poin member",
                ],
                [
                    1,
                    0,
                    "potongan Suspense (stream)",
                ],
            ],
        },
    ],
    "Nuxt dan Astro: Vue Full-stack dan Islands": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Next.js, Nuxt, dan Astro berdampingan",
            "tabel": [
                {
                    "kolom": [
                        "Hal",
                        "Next.js",
                        "Nuxt",
                        "Astro",
                    ],
                    "baris": [
                        [
                            "Basis UI",
                            "React",
                            "Vue",
                            "apa saja",
                        ],
                        [
                            "JS ke browser",
                            "semua halaman",
                            "semua halaman",
                            "pulau saja",
                        ],
                        [
                            "Cocok untuk",
                            "aplikasi web",
                            "aplikasi Vue",
                            "situs konten",
                        ],
                        [
                            "Server",
                            "Node/Vercel",
                            "Nitro",
                            "adapter",
                        ],
                    ],
                },
            ],
        },
    ],
    "Peta Meta-framework dan Generator Situs Statis": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Meta-framework dan SSG di luar empat besar",
            "tabel": [
                {
                    "kolom": [
                        "Nama",
                        "Basis",
                        "Jenis",
                        "Status",
                    ],
                    "baris": [
                        [
                            "React Router",
                            "React",
                            "framework",
                            "aktif",
                        ],
                        [
                            "Remix 3",
                            "fork Preact",
                            "framework",
                            "baru",
                        ],
                        [
                            "TanStack Start",
                            "React",
                            "framework",
                            "naik",
                        ],
                        [
                            "Gatsby",
                            "React",
                            "SSG",
                            "menurun",
                        ],
                        [
                            "Docusaurus",
                            "React",
                            "SSG docs",
                            "aktif",
                        ],
                        [
                            "VitePress",
                            "Vue",
                            "SSG docs",
                            "aktif",
                        ],
                        [
                            "Hugo",
                            "Go",
                            "SSG",
                            "aktif",
                        ],
                        [
                            "Jekyll",
                            "Ruby",
                            "SSG",
                            "stabil-matang",
                        ],
                    ],
                },
            ],
        },
    ],
    "Komponen Headless, shadcn/ui, dan Pustaka Komponen": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Siapa memegang perilaku dan siapa memegang gaya",
            "tabel": [
                {
                    "kolom": [
                        "Jenis",
                        "Contoh",
                        "Perilaku",
                        "Gaya",
                    ],
                    "baris": [
                        [
                            "Headless",
                            "Radix, Ark UI",
                            "pustaka",
                            "kamu",
                        ],
                        [
                            "Salin kode",
                            "shadcn/ui",
                            "pustaka",
                            "kodemu",
                        ],
                        [
                            "Bergaya",
                            "MUI, Ant Design",
                            "pustaka",
                            "pustaka",
                        ],
                    ],
                },
            ],
        },
    ],
    "Animasi dan Grafis: Motion, GSAP, D3, dan Three.js": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Posisi kotak (piksel) di tiap waktu",
            "tabel": [
                {
                    "kolom": [
                        "ms",
                        "linear",
                        "easeOut",
                        "pegas",
                    ],
                    "baris": [
                        [
                            "0",
                            "0",
                            "0",
                            "0",
                        ],
                        [
                            "125",
                            "25",
                            "58",
                            "122",
                        ],
                        [
                            "250",
                            "50",
                            "88",
                            "95",
                        ],
                        [
                            "375",
                            "75",
                            "98",
                            "101",
                        ],
                        [
                            "500",
                            "100",
                            "100",
                            "100",
                        ],
                    ],
                },
            ],
            "ket": "Pegas sempat melewati tujuan (122) sebelum diam di 100.",
        },
    ],
    "Monorepo: Workspaces, Turborepo, dan Nx": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Monorepo: aplikasi di apps/, kode bersama di packages/",
            "akar": {
                "teks": "kafe",
                "anak": [
                    {
                        "teks": "turbo.json",
                    },
                    {
                        "teks": "apps",
                        "anak": [
                            {
                                "teks": "web",
                            },
                            {
                                "teks": "admin",
                            },
                            {
                                "teks": "docs",
                            },
                        ],
                    },
                    {
                        "teks": "packages",
                        "anak": [
                            {
                                "teks": "ui",
                            },
                            {
                                "teks": "utils",
                            },
                            {
                                "teks": "config",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "PWA: Service Worker dan Strategi Cache": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Service worker berdiri di antara halaman dan jaringan",
            "pelaku": [
                "halaman",
                "service worker",
                "cache",
                "jaringan",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /menu",
                ],
                [
                    1,
                    3,
                    "network-first: coba dulu",
                ],
                [
                    3,
                    1,
                    "gagal (offline)",
                ],
                [
                    1,
                    2,
                    "caches.match(/menu)",
                ],
                [
                    2,
                    1,
                    "salinan terakhir",
                ],
                [
                    1,
                    0,
                    "respons dari cache",
                ],
            ],
        },
    ],
    "WebAssembly untuk Developer Frontend": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari kode C atau Rust sampai dipanggil JavaScript",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Kode C/C++/Rust",
                },
                {
                    "jenis": "proses",
                    "teks": "Emscripten / wasm-pack",
                },
                {
                    "jenis": "keluaran",
                    "teks": "Berkas .wasm + perekat JS",
                },
                {
                    "jenis": "proses",
                    "teks": "JS: WebAssembly.instantiate",
                },
                {
                    "jenis": "selesai",
                    "teks": "JS memanggil fungsi ekspor",
                },
            ],
        },
        {
            "setelah": 4,
            "jenis": "larik",
            "judul": "Linear memory sesudah JS menulis 20 dan 22",
            "nama": "byte",
            "isi": [
                "20",
                "0",
                "0",
                "0",
                "22",
                "0",
                "0",
                "0",
            ],
            "penunjuk": {
                "pa": 0,
                "pb": 4,
            },
            "ket": "Setiap i32 memakai 4 byte, urutan little-endian.",
        },
    ],
    "Desktop dan Mobile dari Teknologi Web": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Membawa aplikasi web ke desktop dan ponsel",
            "tabel": [
                {
                    "kolom": [
                        "Kerangka",
                        "Tampilan",
                        "Backend",
                        "Status",
                    ],
                    "baris": [
                        [
                            "Electron",
                            "Chromium dibawa",
                            "Node.js",
                            "aktif",
                        ],
                        [
                            "Tauri",
                            "webview sistem",
                            "Rust",
                            "aktif",
                        ],
                        [
                            "Wails",
                            "webview sistem",
                            "Go",
                            "aktif",
                        ],
                        [
                            "NW.js",
                            "Chromium dibawa",
                            "Node.js",
                            "menurun",
                        ],
                        [
                            "Capacitor",
                            "webview ponsel",
                            "plugin native",
                            "aktif",
                        ],
                        [
                            "Cordova",
                            "webview ponsel",
                            "plugin native",
                            "menurun",
                        ],
                    ],
                },
            ],
        },
    ],
    "Deno, Bun, Edge, dan Tempat Deploy Frontend": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Runtime JavaScript di luar browser",
            "tabel": [
                {
                    "kolom": [
                        "Runtime",
                        "Kekuatan",
                        "Perhatikan",
                    ],
                    "baris": [
                        [
                            "Node.js LTS",
                            "ekosistem",
                            "pilihan aman",
                        ],
                        [
                            "Deno",
                            "izin eksplisit",
                            "awalan npm:",
                        ],
                        [
                            "Bun",
                            "kecepatan",
                            "modul native",
                        ],
                        [
                            "Workers",
                            "dekat pengguna",
                            "bukan Node",
                        ],
                    ],
                },
            ],
        },
    ],
}
