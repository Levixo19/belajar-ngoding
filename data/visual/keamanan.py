"""Gambar konsep kurikulum Keamanan Siber. Skema: inti/visual.py."""

VISUAL = {
    "Keamanan Siber dari Sisi Bertahan: CIA dan Risiko": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Tiga sifat yang dijaga dan penangkalnya",
            "tabel": [
                {
                    "kolom": [
                        "Sifat",
                        "Contoh rusak",
                        "Penangkal",
                    ],
                    "baris": [
                        [
                            "Kerahasiaan",
                            "nilai bocor",
                            "enkripsi, akses",
                        ],
                        [
                            "Integritas",
                            "nilai diganti",
                            "tanda tangan",
                        ],
                        [
                            "Ketersediaan",
                            "situs mati",
                            "cadangan",
                        ],
                    ],
                },
            ],
            "ket": "Penangkal di kolom kanan cuma contoh. Tiap sifat punya banyak penangkal lain.",
        },
        {
            "setelah": 5,
            "jenis": "tumpukan",
            "judul": "Pertahanan berlapis untuk aplikasi web",
            "mode": "tumpukan",
            "isi": [
                "Pemantauan log",
                "Firewall",
                "Pembaruan rutin",
                "Login + MFA",
                "Validasi + izin",
                "Enkripsi, backup",
            ],
            "label": "luar ke dalam",
            "ket": "Penyerang harus menembus lapis demi lapis, dan tiap lapis memberi kesempatan untuk ketahuan.",
        },
    ],
    "Etika, Hukum, dan Lab Legal untuk Belajar Keamanan": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Saat menemukan tanda celah",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Menemukan tanda celah",
                    "ke": 1,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Milikmu atau ada izin tertulis?",
                    "ya": 2,
                    "tidak": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Uji sesuai cakupan izin",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Berhenti, jangan ambil data",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Lapor lewat kanal resmi",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "Pemilik memperbaiki",
                    "ke": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "Publikasi sesudah beres",
                },
            ],
            "ket": "Di kedua cabang, laporan ke pemilik sistem tetap ada. Bedanya, tanpa izin kamu berhenti di tanda pertama.",
        },
    ],
    "Threat Modeling dengan STRIDE dan PASTA": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Diagram alir login: data melintasi batas",
            "pelaku": [
                "Pengguna",
                "Web",
                "API",
                "Database",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "isi form login (lintas batas)",
                ],
                [
                    1,
                    2,
                    "POST /login",
                ],
                [
                    2,
                    3,
                    "cari pengguna",
                ],
                [
                    3,
                    2,
                    "hash password",
                ],
                [
                    2,
                    1,
                    "cookie sesi",
                ],
                [
                    1,
                    0,
                    "halaman dasbor",
                ],
            ],
            "ket": "Panah pertama menyeberang dari internet ke servermu. Di situlah keenam pertanyaan paling perlu ditanyakan.",
        },
    ],
    "Secure SDLC: Keamanan di Setiap Tahap Pengembangan": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Tahap SDLC dan kegiatan keamanannya",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Kebutuhan: abuse case",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Desain: threat modeling",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "Kode: review + pemindai rahasia",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "Uji: SAST, SCA, kasus jahat",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "Rilis: konfigurasi dikeraskan",
                    "ke": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "Operasi: patch + pantau log",
                },
            ],
            "ket": "Tiap tahap punya pemeriksaan sendiri. Makin kiri celah ketahuan, makin murah memperbaikinya.",
        },
    ],
    "Hash, Checksum, dan Integritas Data": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Memeriksa keaslian unduhan dengan hash",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "Unduh berkas",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "Hitung SHA-256 berkasmu",
                    "ke": 2,
                },
                {
                    "jenis": "masukan",
                    "teks": "Ambil sidik dari situs resmi",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "Ke-64 karakter sama?",
                    "ya": 4,
                    "tidak": 5,
                },
                {
                    "jenis": "selesai",
                    "teks": "Berkas boleh dipakai",
                },
                {
                    "jenis": "selesai",
                    "teks": "Hapus, unduh ulang",
                },
            ],
            "ket": "Sidik pembanding harus datang dari jalur yang berbeda dengan berkasnya, kalau tidak penyerang bisa menukar keduanya sekaligus.",
        },
    ],
    "Menyimpan Password: Salt, PBKDF2, bcrypt, dan Argon2": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Cara menyimpan password, dari buruk ke baik",
            "tabel": [
                {
                    "kolom": [
                        "Cara",
                        "Nilai",
                        "Masalah",
                    ],
                    "baris": [
                        [
                            "Teks polos",
                            "buruk",
                            "langsung terbaca",
                        ],
                        [
                            "Enkripsi",
                            "buruk",
                            "kunci ikut bocor",
                        ],
                        [
                            "MD5/SHA polos",
                            "buruk",
                            "cepat ditebak",
                        ],
                        [
                            "SHA + salt",
                            "kurang",
                            "masih cepat",
                        ],
                        [
                            "PBKDF2",
                            "layak",
                            "cuma beban CPU",
                        ],
                        [
                            "bcrypt",
                            "baik",
                            "batas 72 byte",
                        ],
                        [
                            "Argon2id",
                            "terbaik",
                            "butuh paket",
                        ],
                    ],
                    "sorot_baris": [6],
                },
            ],
            "ket": "Tiga baris terbawah semuanya sah dipakai. Argon2id disarankan untuk aplikasi baru.",
        },
    ],
    "Enkripsi Simetris, Asimetris, dan Tanda Tangan Digital": [
        {
            "setelah": 4,
            "jenis": "urutan",
            "judul": "Enkripsi hibrida: kunci publik untuk berbagi kunci sesi",
            "pelaku": [
                "Alice",
                "Bob",
            ],
            "pesan": [
                [
                    1,
                    0,
                    "kunci publik Bob",
                ],
                [
                    0,
                    1,
                    "kunci sesi, dikunci publik Bob",
                ],
                [
                    0,
                    1,
                    "pesan, dienkripsi AES-GCM",
                ],
                [
                    1,
                    0,
                    "balasan, dienkripsi AES-GCM",
                ],
            ],
            "ket": "Penyadap bisa melihat semua panah. Tanpa kunci privat Bob, ia nggak bisa membuka kunci sesi, jadi isi pesan tetap rahasia.",
        },
    ],
    "Sertifikat, PKI, dan Manajemen Kunci": [
        {
            "setelah": 3,
            "jenis": "pohon",
            "judul": "Rantai kepercayaan sertifikat",
            "akar": {
                "teks": "Contoh Root X1",
                "anak": [
                    {
                        "teks": "Contoh CA R1",
                        "anak": [
                            {
                                "teks": "tokokecil.example",
                            },
                            {
                                "teks": "kopi.example",
                            },
                        ],
                    },
                    {
                        "teks": "Contoh CA R2",
                        "anak": [
                            {
                                "teks": "bank.example",
                            },
                        ],
                    },
                ],
            },
            "ket": "Root ada di root store browser. Sertifikat situs dipercaya kalau rantainya sampai ke root itu.",
        },
    ],
    "Autentikasi: Password, MFA, dan Passkey": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Tiga jenis faktor autentikasi",
            "tabel": [
                {
                    "kolom": [
                        "Faktor",
                        "Contoh",
                        "Kelemahan",
                    ],
                    "baris": [
                        [
                            "Tahu",
                            "password, PIN",
                            "bisa ditebak",
                        ],
                        [
                            "Punya",
                            "ponsel, kunci",
                            "bisa hilang",
                        ],
                        [
                            "Melekat",
                            "sidik jari",
                            "tak bisa diganti",
                        ],
                    ],
                },
            ],
            "ket": "MFA berarti dua baris yang berbeda dari tabel ini, bukan dua isian dari baris yang sama.",
        },
    ],
    "Sesi, Cookie, dan JWT": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Login dengan sesi di server",
            "pelaku": [
                "Browser",
                "Server",
                "Redis",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "POST /login",
                ],
                [
                    1,
                    2,
                    "simpan sesi q8Zr -> user 42",
                ],
                [
                    1,
                    0,
                    "Set-Cookie: sesi=q8Zr",
                ],
                [
                    0,
                    1,
                    "GET /pesanan + cookie",
                ],
                [
                    1,
                    2,
                    "ambil sesi q8Zr",
                ],
                [
                    2,
                    1,
                    "user 42",
                ],
                [
                    1,
                    0,
                    "daftar pesanan user 42",
                ],
            ],
            "ket": "Browser cuma memegang nomor tiket. Data siapa penggunanya tetap di server.",
        },
    ],
    "OAuth 2.0, OpenID Connect, dan SSO": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Authorization code dengan PKCE",
            "pelaku": [
                "Pengguna",
                "Aplikasi",
                "Server auth",
                "API",
            ],
            "pesan": [
                [
                    1,
                    2,
                    "arahkan + code_challenge",
                ],
                [
                    0,
                    2,
                    "login dan setujui izin",
                ],
                [
                    2,
                    1,
                    "code (lewat redirect)",
                ],
                [
                    1,
                    2,
                    "code + code_verifier",
                ],
                [
                    2,
                    1,
                    "access token + ID token",
                ],
                [
                    1,
                    3,
                    "GET /data + access token",
                ],
                [
                    3,
                    1,
                    "data",
                ],
            ],
            "ket": "Password cuma diketik di server auth. Aplikasi menerima token, dan code yang dicuri nggak berguna tanpa code_verifier.",
        },
    ],
    "Otorisasi: RBAC, Least Privilege, dan Policy as Code": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Matriks peran dan izin",
            "tabel": [
                {
                    "kolom": [
                        "Izin",
                        "pembaca",
                        "penulis",
                        "admin",
                    ],
                    "baris": [
                        [
                            "artikel:baca",
                            "ya",
                            "ya",
                            "ya",
                        ],
                        [
                            "artikel:tulis",
                            "-",
                            "milik sendiri",
                            "ya",
                        ],
                        [
                            "artikel:hapus",
                            "-",
                            "-",
                            "ya",
                        ],
                        [
                            "pengguna:kelola",
                            "-",
                            "-",
                            "ya",
                        ],
                    ],
                },
            ],
            "ket": "Sel kosong berarti ditolak. Sel milik sendiri adalah aturan kepemilikan yang mencegah IDOR.",
        },
    ],
    "Peta Penyedia Identitas: Keycloak, Auth0, Okta, Ping": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Empat penyedia identitas",
            "tabel": [
                {
                    "kolom": [
                        "Penyedia",
                        "Model",
                        "Lisensi",
                        "SO 2026",
                    ],
                    "baris": [
                        [
                            "Auth0",
                            "SaaS",
                            "proprietary",
                            "30%",
                        ],
                        [
                            "Okta",
                            "SaaS",
                            "proprietary",
                            "29%",
                        ],
                        [
                            "Keycloak",
                            "pasang sendiri",
                            "Apache-2.0",
                            "19%",
                        ],
                        [
                            "Ping Identity",
                            "SaaS + on-prem",
                            "proprietary",
                            "5%",
                        ],
                    ],
                    "sorot_baris": [2],
                },
            ],
            "ket": "Persentase dari Survei Stack Overflow 2026, kategori alat operasi keamanan. Keycloak satu-satunya yang open source.",
        },
    ],
    "OWASP Top 10:2025: Peta Risiko Aplikasi Web": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Sepuluh kategori Top 10:2025 dan bab yang membahasnya",
            "ket": "Nama kategori diringkas. A04 dan A07 dibahas di bab 02 dan 03, A03 dan A08 di bab 06.",
            "tabel": [
                {
                    "nama": "A01 sampai A05",
                    "kolom": [
                        "kode",
                        "risiko",
                        "bab",
                    ],
                    "baris": [
                        [
                            "A01",
                            "akses rusak",
                            "04",
                        ],
                        [
                            "A02",
                            "salah konfig",
                            "04",
                        ],
                        [
                            "A03",
                            "rantai pasok",
                            "06",
                        ],
                        [
                            "A04",
                            "kriptografi",
                            "02",
                        ],
                        [
                            "A05",
                            "injeksi",
                            "04",
                        ],
                    ],
                },
                {
                    "nama": "A06 sampai A10",
                    "kolom": [
                        "kode",
                        "risiko",
                        "bab",
                    ],
                    "baris": [
                        [
                            "A06",
                            "desain lemah",
                            "04",
                        ],
                        [
                            "A07",
                            "autentikasi",
                            "03",
                        ],
                        [
                            "A08",
                            "integritas",
                            "06",
                        ],
                        [
                            "A09",
                            "log dan alert",
                            "04",
                        ],
                        [
                            "A10",
                            "error salah urus",
                            "04",
                        ],
                    ],
                },
            ],
        },
    ],
    "Kontrol Akses Rusak dan Salah Konfigurasi": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Server menolak pesanan milik orang lain",
            "ket": "Ini alur lihat_aman. Syarat pemilik ikut di query, jadi database nggak mengembalikan baris pesanan 1043 ke Ani.",
            "pelaku": [
                "Ani",
                "server",
                "database",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /pesanan/1043",
                ],
                [
                    1,
                    2,
                    "id=1043 AND pemilik=ani",
                ],
                [
                    2,
                    1,
                    "0 baris",
                ],
                [
                    1,
                    0,
                    "404 tidak ada",
                ],
            ],
        },
    ],
    "Injeksi dan XSS: Validasi Masukan dan Encoding Keluaran": [
        {
            "setelah": 6,
            "jenis": "alur",
            "judul": "Masukan diperiksa, dikirim sebagai data, di-escape saat tampil",
            "ket": "Validasi menolak bentuk yang salah, query berparameter menjaga database, dan escape menjaga browser.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "nama dari formulir",
                },
                {
                    "jenis": "keputusan",
                    "teks": "lolos daftar putih?",
                    "tidak": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "query dengan placeholder ?",
                },
                {
                    "jenis": "proses",
                    "teks": "html.escape(hasil)",
                },
                {
                    "jenis": "keluaran",
                    "teks": "tampilkan di halaman",
                    "ke": 6,
                },
                {
                    "jenis": "keluaran",
                    "teks": "400: format nama salah",
                },
                {
                    "jenis": "selesai",
                    "teks": "selesai",
                },
            ],
        },
    ],
    "Desain Tidak Aman, Logging Lemah, dan Exception Bocor": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Pesan error untuk pengguna: yang bocor dan yang aman",
            "ket": "Detail teknis tetap dicatat, tapi di log server dengan kode kejadian yang sama.",
            "tabel": [
                {
                    "kolom": [
                        "kejadian",
                        "pesan bocor",
                        "pesan aman",
                    ],
                    "baris": [
                        [
                            "saldo kurang",
                            "CHECK failed",
                            "kode TRF-01",
                        ],
                        [
                            "kolom salah",
                            "no such column",
                            "kode E-7F3A",
                        ],
                        [
                            "login gagal",
                            "user tak ada",
                            "data salah",
                        ],
                        [
                            "berkas hilang",
                            "/home/deploy/..",
                            "tidak ditemukan",
                        ],
                    ],
                    "sorot_kolom": [
                        "pesan aman",
                    ],
                },
            ],
        },
    ],
    "Rate Limiting, Brute Force, dan Perlindungan Login": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Isi ember token per permintaan, kapasitas 3",
            "ket": "Sama dengan keluaran contoh: ember terisi 0,5 token per detik dan tiap permintaan yang lolos mengambil 1 token.",
            "tabel": [
                {
                    "kolom": [
                        "detik",
                        "hasil",
                        "sisa token",
                    ],
                    "baris": [
                        [
                            "0",
                            "izinkan",
                            "2.0",
                        ],
                        [
                            "0",
                            "izinkan",
                            "1.0",
                        ],
                        [
                            "0",
                            "izinkan",
                            "0.0",
                        ],
                        [
                            "0",
                            "tolak 429",
                            "0.0",
                        ],
                        [
                            "1",
                            "tolak 429",
                            "0.5",
                        ],
                        [
                            "2",
                            "izinkan",
                            "0.0",
                        ],
                        [
                            "6",
                            "izinkan",
                            "1.0",
                        ],
                        [
                            "6",
                            "izinkan",
                            "0.0",
                        ],
                    ],
                    "sorot_baris": [3, 4],
                },
            ],
        },
    ],
    "Header Keamanan, CORS, dan Cookie Aman": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Header keamanan, yang dicegah, dan contoh nilai aman",
            "ket": "Nilai lengkap ada di contoh middleware. Cookie sesi juga butuh HttpOnly dan SameSite.",
            "tabel": [
                {
                    "kolom": [
                        "header",
                        "mencegah",
                        "nilai aman",
                    ],
                    "baris": [
                        [
                            "CSP",
                            "skrip asing",
                            "default-src self",
                        ],
                        [
                            "HSTS",
                            "turun ke HTTP",
                            "max-age 1 tahun",
                        ],
                        [
                            "nosniff",
                            "tebak jenis",
                            "nosniff",
                        ],
                        [
                            "Referrer-Policy",
                            "bocor URL",
                            "strict-origin..",
                        ],
                        [
                            "Set-Cookie",
                            "curi sesi",
                            "Secure; HttpOnly",
                        ],
                    ],
                },
            ],
        },
    ],
    "Keamanan API: Skema, Kunci API, dan Logging Aman": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Urutan pemeriksaan sebelum handler API dijalankan",
            "ket": "Tiap pemeriksaan yang gagal langsung menjawab dengan status yang sesuai, tanpa menyentuh logika bisnis.",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "permintaan masuk",
                },
                {
                    "jenis": "keputusan",
                    "teks": "kunci API sah?",
                    "tidak": 6,
                },
                {
                    "jenis": "keputusan",
                    "teks": "lolos validasi skema?",
                    "tidak": 7,
                },
                {
                    "jenis": "keputusan",
                    "teks": "boleh akses objek ini?",
                    "tidak": 8,
                },
                {
                    "jenis": "proses",
                    "teks": "jalankan handler",
                },
                {
                    "jenis": "selesai",
                    "teks": "200 + log ringkas",
                },
                {
                    "jenis": "keluaran",
                    "teks": "401 tanpa autentikasi",
                    "ke": 9,
                },
                {
                    "jenis": "keluaran",
                    "teks": "400 + alasan",
                    "ke": 9,
                },
                {
                    "jenis": "keluaran",
                    "teks": "403 atau 404",
                    "ke": 9,
                },
                {
                    "jenis": "selesai",
                    "teks": "catat penolakan",
                },
            ],
        },
    ],
    "Manajemen Rahasia: Kunci Tidak Boleh Ada di Kode": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Urutan menanggapi rahasia yang bocor",
            "ket": "Mencabut kunci selalu didahulukan. Membersihkan riwayat Git cuma merapikan, karena salinan lama nggak ikut hilang.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "rahasia ketahuan bocor",
                },
                {
                    "jenis": "proses",
                    "teks": "buat kunci baru, cabut lama",
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada akses asing di log?",
                    "tidak": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "tangani sebagai insiden",
                },
                {
                    "jenis": "proses",
                    "teks": "bersihkan riwayat Git",
                },
                {
                    "jenis": "selesai",
                    "teks": "pasang pemindai rahasia",
                },
            ],
        },
    ],
    "Vault dan OpenBao: Brankas Rahasia Terpusat": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Aplikasi meminta kredensial database sementara ke Vault",
            "ket": "Vault membuat user baru di database untuk tiap permintaan dan menghapusnya lagi saat lease habis.",
            "pelaku": [
                "aplikasi",
                "Vault",
                "database",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "login (AppRole)",
                ],
                [
                    1,
                    0,
                    "token, TTL 1 jam",
                ],
                [
                    0,
                    1,
                    "read database/creds/baca",
                ],
                [
                    1,
                    2,
                    "CREATE USER v-baca-1",
                ],
                [
                    1,
                    0,
                    "user + password, lease 1j",
                ],
                [
                    0,
                    2,
                    "query sebagai v-baca-1",
                ],
                [
                    1,
                    2,
                    "lease habis: DROP USER",
                ],
            ],
        },
    ],
    "Rahasia di Git dan Kubernetes: SOPS, Sealed Secrets, ESO": [
        {
            "setelah": 8,
            "jenis": "tabel",
            "judul": "Tiga cara menyalurkan rahasia lewat GitOps",
            "ket": "Ketiganya berakhir sebagai Secret Kubernetes di klaster, jadi izin membaca Secret tetap harus dibatasi.",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "di Git",
                        "kunci di",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            "SOPS",
                            "nilai dienkripsi",
                            "KMS / age",
                            "review di Git",
                        ],
                        [
                            "Sealed Secrets",
                            "SealedSecret",
                            "controller",
                            "1-2 klaster",
                        ],
                        [
                            "ESO",
                            "petunjuk saja",
                            "brankas pusat",
                            "ada Vault/cloud",
                        ],
                    ],
                },
            ],
        },
    ],
    "Rantai Pasok Perangkat Lunak: Lockfile dan Dependensi": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "Dua dependensi langsung menarik dependensi transitif",
            "ket": "Contoh yang diringkas dari aplikasi Flask kecil. markupsafe dibawa dua paket sekaligus, dan nggak pernah kamu tulis sendiri di requirements.txt.",
            "akar": {
                "teks": "toko-web",
                "anak": [
                    {
                        "teks": "flask",
                        "anak": [
                            {
                                "teks": "werkzeug",
                                "anak": [
                                    {
                                        "teks": "markupsafe",
                                    },
                                ],
                            },
                            {
                                "teks": "jinja2",
                                "anak": [
                                    {
                                        "teks": "markupsafe",
                                    },
                                ],
                            },
                            {
                                "teks": "itsdangerous",
                            },
                            {
                                "teks": "click",
                            },
                            {
                                "teks": "blinker",
                            },
                        ],
                    },
                    {
                        "teks": "requests",
                        "anak": [
                            {
                                "teks": "urllib3",
                            },
                            {
                                "teks": "idna",
                            },
                            {
                                "teks": "certifi",
                            },
                            {
                                "teks": "charset-normalizer",
                            },
                        ],
                    },
                ],
            },
        },
    ],
    "SBOM dan Tanda Tangan Artefak: Syft dan Sigstore": [
        {
            "setelah": 5,
            "jenis": "alur",
            "judul": "Artefak dibuatkan SBOM, ditandatangani, lalu diverifikasi",
            "ket": "Verifikasi di sisi deploy yang membuat tanda tangan berguna. Image yang gagal verifikasi nggak dijalankan.",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "build image di CI",
                },
                {
                    "jenis": "proses",
                    "teks": "syft: buat SBOM",
                },
                {
                    "jenis": "proses",
                    "teks": "cosign sign (keyless)",
                },
                {
                    "jenis": "proses",
                    "teks": "dorong ke registry",
                },
                {
                    "jenis": "keputusan",
                    "teks": "cosign verify lolos?",
                    "tidak": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "deploy ke klaster",
                },
                {
                    "jenis": "keluaran",
                    "teks": "tolak image",
                },
            ],
        },
    ],
    "DevSecOps: SAST, SCA, DAST, dan Gerbang Kualitas": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Pemeriksaan keamanan di sepanjang pipeline",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "commit / pull request",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "secret scan + SAST",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "SCA + IaC scan",
                    "ke": 3,
                },
                {
                    "jenis": "proses",
                    "teks": "build image",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "scan image container",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "deploy staging + DAST",
                    "ke": 6,
                },
                {
                    "jenis": "keputusan",
                    "teks": "ada temuan yang memblokir?",
                    "ya": 7,
                    "tidak": 8,
                },
                {
                    "jenis": "selesai",
                    "teks": "pipeline berhenti, perbaiki",
                },
                {
                    "jenis": "selesai",
                    "teks": "deploy ke produksi",
                },
            ],
            "ket": "Yang cepat di depan, yang butuh aplikasi berjalan di belakang.",
        },
    ],
    "Analisis Kode Statis: SonarQube dan CodeQL": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "SonarQube dan CodeQL berdampingan",
            "tabel": [
                {
                    "kolom": [
                        "aspek",
                        "SonarQube",
                        "CodeQL",
                    ],
                    "baris": [
                        [
                            "pembuat",
                            "SonarSource",
                            "GitHub",
                        ],
                        [
                            "fokus",
                            "mutu & keamanan",
                            "celah keamanan",
                        ],
                        [
                            "cara kerja",
                            "aturan bahasa",
                            "kueri QL",
                        ],
                        [
                            "gratis untuk",
                            "Community Build",
                            "repo publik",
                        ],
                        [
                            "gerbang",
                            "quality gate",
                            "cek di PR",
                        ],
                    ],
                },
            ],
            "ket": "Banyak tim memakai keduanya: SonarQube untuk mutu, CodeQL untuk celah.",
        },
    ],
    "Memindai Dependensi dan Image: Trivy dan Snyk": [
        {
            "setelah": 7,
            "jenis": "tabel",
            "judul": "Prioritas perbaikan dari hasil pemindaian",
            "tabel": [
                {
                    "kolom": [
                        "prioritas",
                        "kapan",
                        "batas",
                    ],
                    "baris": [
                        [
                            "P1",
                            "KEV & publik",
                            "hari ini",
                        ],
                        [
                            "P2",
                            "tinggi, publik",
                            "minggu ini",
                        ],
                        [
                            "P3",
                            "tinggi, internal",
                            "sprint depan",
                        ],
                        [
                            "P4",
                            "belum ada fix",
                            "pantau",
                        ],
                    ],
                    "sorot_baris": [0],
                },
            ],
            "ket": "Sama dengan aturan di program contoh. Tim boleh menyetel batasnya sendiri.",
        },
    ],
    "Memindai Infrastructure as Code: Checkov dan KICS": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Aturan Checkov untuk contoh di materi ini",
            "tabel": [
                {
                    "kolom": [
                        "ID",
                        "pelanggaran",
                    ],
                    "baris": [
                        [
                            "CKV_AWS_20",
                            "bucket publik",
                        ],
                        [
                            "CKV_AWS_24",
                            "SSH 0.0.0.0/0",
                        ],
                        [
                            "CKV_AWS_19",
                            "enkripsi S3 mati",
                        ],
                        [
                            "CKV_AWS_16",
                            "RDS tak enkripsi",
                        ],
                    ],
                },
            ],
            "ket": "Deskripsi lengkapnya ada di indeks kebijakan Checkov untuk Terraform.",
        },
    ],
    "Memetakan Jaringan Sendiri dengan Nmap": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Tiga status port yang paling sering muncul",
            "tabel": [
                {
                    "kolom": [
                        "status",
                        "artinya",
                        "tindakan",
                    ],
                    "baris": [
                        [
                            "open",
                            "ada layanan",
                            "cocokkan izin",
                        ],
                        [
                            "closed",
                            "tanpa layanan",
                            "biarkan",
                        ],
                        [
                            "filtered",
                            "tak ada jawaban",
                            "periksa firewall",
                        ],
                    ],
                    "sorot_baris": [0],
                },
            ],
            "ket": "Tiga status lain (unfiltered, open|filtered, closed|filtered) lebih jarang.",
        },
    ],
    "Menguji Aplikasi Web Sendiri: ZAP dan Burp Suite": [
        {
            "setelah": 1,
            "jenis": "urutan",
            "judul": "Proxy penguji di antara browser dan aplikasi lab",
            "pelaku": [
                "browser",
                "proxy penguji",
                "Juice Shop",
            ],
            "pesan": [
                [
                    0,
                    1,
                    "GET /rest/products",
                ],
                [
                    1,
                    2,
                    "diteruskan apa adanya",
                ],
                [
                    2,
                    1,
                    "jawaban + header",
                ],
                [
                    1,
                    0,
                    "dicatat, diteruskan",
                ],
                [
                    1,
                    2,
                    "dikirim ulang, diubah",
                ],
                [
                    2,
                    1,
                    "jawaban dibandingkan",
                ],
            ],
            "ket": "Semuanya di laptop sendiri: browser, proxy, dan aplikasi di localhost:3000.",
        },
    ],
    "Pemindai Kerentanan: Nessus, OpenVAS, dan Qualys": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Tiga pemindai kerentanan dan tempatnya",
            "tabel": [
                {
                    "kolom": [
                        "alat",
                        "lisensi",
                        "cocok untuk",
                    ],
                    "baris": [
                        [
                            "Nessus",
                            "proprietary",
                            "tim kecil-sedang",
                        ],
                        [
                            "OpenVAS",
                            "GPL/AGPL",
                            "lab, hemat biaya",
                        ],
                        [
                            "Qualys",
                            "SaaS berbayar",
                            "ribuan aset",
                        ],
                    ],
                },
            ],
            "ket": "Nessus Essentials gratis untuk non-komersial dengan batas jumlah IP.",
        },
    ],
    "Log Keamanan dan SIEM: Mendeteksi Serangan": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Dari baris log sampai alert",
            "langkah": [
                {
                    "jenis": "masukan",
                    "teks": "log auth, web, audit, cloud",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "kumpulkan + normalkan",
                    "ke": 2,
                },
                {
                    "jenis": "proses",
                    "teks": "korelasi dengan aturan",
                    "ke": 3,
                },
                {
                    "jenis": "keputusan",
                    "teks": "kondisi aturan terpenuhi?",
                    "ya": 4,
                    "tidak": 5,
                },
                {
                    "jenis": "keluaran",
                    "teks": "alert ke analis",
                },
                {
                    "jenis": "selesai",
                    "teks": "disimpan untuk investigasi",
                },
            ],
            "ket": "Log yang nggak memicu alert tetap disimpan, karena dibutuhkan saat investigasi.",
        },
    ],
    "Respons Insiden, SOAR, dan Postmortem": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Siklus respons insiden",
            "langkah": [
                {
                    "jenis": "mulai",
                    "teks": "persiapan: playbook, kontak",
                    "ke": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "deteksi dan analisis",
                    "ke": 2,
                },
                {
                    "jenis": "keputusan",
                    "teks": "insiden sungguhan?",
                    "ya": 3,
                    "tidak": 1,
                },
                {
                    "jenis": "proses",
                    "teks": "tahan (containment)",
                    "ke": 4,
                },
                {
                    "jenis": "proses",
                    "teks": "bersihkan (eradication)",
                    "ke": 5,
                },
                {
                    "jenis": "proses",
                    "teks": "pulihkan (recovery)",
                    "ke": 6,
                },
                {
                    "jenis": "selesai",
                    "teks": "pelajari: postmortem",
                },
            ],
            "ket": "Hasil postmortem kembali jadi bahan persiapan untuk insiden berikutnya.",
        },
    ],
    "Keamanan Cloud dan Kubernetes: IAM, CSPM, dan Wiz": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Salah konfigurasi cloud yang paling sering",
            "tabel": [
                {
                    "kolom": [
                        "salah setelan",
                        "perbaikan",
                    ],
                    "baris": [
                        [
                            "root dipakai",
                            "MFA, simpan",
                        ],
                        [
                            "access key lama",
                            "role sementara",
                        ],
                        [
                            "Action \"*\"",
                            "izin minimal",
                        ],
                        [
                            "bucket publik",
                            "Block Public",
                        ],
                        [
                            "SSH 0.0.0.0/0",
                            "bastion / SSM",
                        ],
                        [
                            "IMDSv1",
                            "wajib IMDSv2",
                        ],
                    ],
                },
            ],
            "ket": "Versi ringkas tabel di prosa. Semuanya terlihat dari konfigurasi, tanpa menyerang apa pun.",
        },
    ],
    "Peta Vendor Keamanan Perusahaan: EDR, PAM, Firewall": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Kategori produk keamanan perusahaan",
            "tabel": [
                {
                    "kolom": [
                        "kategori",
                        "vendor",
                        "SO 2026",
                    ],
                    "baris": [
                        [
                            "EDR",
                            "CrowdStrike",
                            "12%",
                        ],
                        [
                            "EDR",
                            "SentinelOne",
                            "6%",
                        ],
                        [
                            "PAM",
                            "CyberArk",
                            "6%",
                        ],
                        [
                            "PAM",
                            "BeyondTrust",
                            "5%",
                        ],
                        [
                            "NGFW",
                            "Fortinet",
                            "9%",
                        ],
                        [
                            "AppSec",
                            "Checkmarx",
                            "5%",
                        ],
                        [
                            "CNAPP",
                            "Wiz",
                            "5%",
                        ],
                    ],
                },
            ],
            "ket": "Angka dari Survei Stack Overflow 2026, kategori alat operasi keamanan.",
        },
    ],
    "Kepatuhan: ISO 27001, SOC 2, NIST CSF, dan UU PDP": [
        {
            "setelah": 4,
            "jenis": "tabel",
            "judul": "Standar, siapa yang butuh, dan buktinya",
            "tabel": [
                {
                    "kolom": [
                        "standar",
                        "biasanya untuk",
                        "bukti",
                    ],
                    "baris": [
                        [
                            "ISO 27001",
                            "sertifikasi",
                            "ISMS + Annex A",
                        ],
                        [
                            "SOC 2",
                            "SaaS ke klien AS",
                            "laporan Type II",
                        ],
                        [
                            "NIST CSF 2.0",
                            "semua organisasi",
                            "profil + target",
                        ],
                        [
                            "PCI DSS 4.0.1",
                            "data kartu",
                            "scan, pentest",
                        ],
                        [
                            "UU PDP",
                            "data pribadi RI",
                            "lapor 3x24 jam",
                        ],
                    ],
                },
            ],
            "ket": "Satu organisasi bisa terkena beberapa sekaligus, dan banyak kontrolnya tumpang tindih.",
        },
    ],
    "Privasi Data: Klasifikasi, Retensi, dan Minimalisasi": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Kelas data dan perlakuannya",
            "tabel": [
                {
                    "kolom": [
                        "kelas",
                        "contoh",
                        "perlakuan",
                    ],
                    "baris": [
                        [
                            "publik",
                            "harga produk",
                            "bebas dibaca",
                        ],
                        [
                            "internal",
                            "notulen rapat",
                            "login kantor",
                        ],
                        [
                            "rahasia",
                            "email, NIK",
                            "enkripsi, samar",
                        ],
                        [
                            "spesifik",
                            "kesehatan, anak",
                            "akses minimal",
                        ],
                    ],
                    "sorot_baris": [3],
                },
            ],
            "ket": "Kelas spesifik mengikuti Pasal 4 UU PDP. Skema kelas lain boleh, asal dipakai konsisten.",
        },
    ],
}
