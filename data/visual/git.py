"""Gambar konsep kurikulum Git & GitHub. Skema: inti/visual.py."""

VISUAL = {
    "Apa Itu Git & Masalah yang Ia Selesaikan": [
        {
            "setelah": 1,
            "jenis": "git",
            "judul": "Tiga commit, satu garis waktu",
            "ket": "Tiap titik menyimpan isi semua berkas saat itu. main menunjuk "
                   "commit terbaru, dan HEAD menandai posisimu sekarang.",
            "commit": [
                {"id": "c1", "induk": [], "cabang": "main", "pesan": "halaman awal"},
                {"id": "c2", "induk": ["c1"], "cabang": "main", "pesan": "tambah menu"},
                {"id": "c3", "induk": ["c2"], "cabang": "main",
                 "pesan": "perbaiki salah ketik"},
            ],
            "label": {"main": "c3"},
            "head": "main",
        },
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Sinkronisasi itu langkah yang kamu jalankan sendiri",
            "ket": "Andi dan Budi sama-sama memegang seluruh riwayat. GitHub cuma "
                   "tempat bertemu, dan commit baru pindah lewat push dan pull.",
            "pelaku": ["laptop Andi", "GitHub", "laptop Budi"],
            "pesan": [
                [0, 0, "commit (tanpa internet)"],
                [0, 1, "push: kirim commit Andi"],
                [1, 2, "pull: Budi ambil commit Andi"],
                [2, 1, "push: kirim commit Budi"],
                [1, 0, "pull: Andi ambil commit Budi"],
            ],
        },
    ],
    "Memasang Git & Memperkenalkan Diri": [
        {
            "setelah": 5,
            "jenis": "tabel",
            "judul": "Tiga lapis setelan, yang paling dekat ke proyek menang",
            "ket": "Kalau user.email ditulis di dua lapis, Git memakai yang dari "
                   "--local untuk proyek itu.",
            "tabel": [{
                "nama": "git config",
                "kolom": ["lapis", "berkas", "berlaku untuk"],
                "baris": [
                    ["--system", "/etc/gitconfig", "semua pengguna"],
                    ["--global", "~/.gitconfig", "kamu, semua repo"],
                    ["--local", ".git/config", "repo ini saja"],
                ],
                "sorot_baris": [2],
            }],
            "panah": "lapis bawah menimpa lapis di atasnya",
        },
    ],
    "Tiga Area Kerja & Commit Pertama": [
        {
            "setelah": 0,
            "jenis": "urutan",
            "judul": "Perubahan berjalan lewat tiga tempat",
            "ket": "git add memindahkan perubahan ke ruang tunggu, git commit "
                   "mencatatnya ke riwayat. Folder kerjamu tetap berisi berkasnya.",
            "pelaku": ["Folder kerja", "Staging", "Repository"],
            "pesan": [
                [0, 0, "sunting catatan.txt"],
                [0, 1, "git add catatan.txt"],
                [1, 2, "git commit -m \"...\""],
            ],
        },
        {
            "setelah": 7,
            "jenis": "alur",
            "judul": "Putaran kerja harian yang terus diulang",
            "ket": "Selalu lewat git status dulu sebelum add, supaya kamu tahu "
                   "berkas mana yang ikut.",
            "langkah": [
                {"jenis": "mulai", "teks": "Mulai bekerja"},
                {"jenis": "proses", "teks": "Sunting berkas"},
                {"jenis": "proses", "teks": "git status"},
                {"jenis": "proses", "teks": "git add <berkas>"},
                {"jenis": "proses", "teks": "git commit -m \"...\"", "ke": 1},
            ],
        },
    ],
    "Membaca Status, Diff, dan Riwayat": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Dua kolom huruf di git status --short",
            "ket": "Kolom kiri keadaan di staging, kolom kanan keadaan di folder "
                   "kerja. Sel bertulisan spasi artinya kolom itu kosong.",
            "tabel": [{
                "nama": "git status --short",
                "kolom": ["berkas", "kiri", "kanan", "artinya"],
                "baris": [
                    ["catatan.txt", "M", "spasi", "sudah di-add"],
                    ["menu.txt", "spasi", "M", "belum di-add"],
                    ["baru.txt", "A", "spasi", "baru, di-add"],
                    ["coba.txt", "?", "?", "untracked"],
                    ["tabel.txt", "M", "M", "di-add lalu ubah"],
                ],
                "sorot_baris": [4],
            }],
        },
        {
            "setelah": 6,
            "jenis": "git",
            "judul": "HEAD, HEAD~1, HEAD~2: menghitung mundur dari posisimu",
            "ket": "Teks di samping tiap commit di sini adalah nama panggilannya. "
                   "git show HEAD~1 menampilkan commit tepat sebelum yang terbaru.",
            "commit": [
                {"id": "a", "induk": [], "cabang": "main", "pesan": "HEAD~3"},
                {"id": "b", "induk": ["a"], "cabang": "main", "pesan": "HEAD~2"},
                {"id": "c", "induk": ["b"], "cabang": "main", "pesan": "HEAD~1"},
                {"id": "d", "induk": ["c"], "cabang": "main", "pesan": "HEAD"},
            ],
            "label": {"main": "d"},
            "head": "main",
        },
    ],
    ".gitignore: Berkas yang Tidak Boleh Masuk Riwayat": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Folder proyek dilihat lewat .gitignore tadi",
            "ket": "Tanda × artinya cocok dengan salah satu pola, jadi Git "
                   "mengabaikannya. __pycache__/ tertangkap di folder mana pun, "
                   "karena polanya tanpa garis miring di depan.",
            "akar": {"teks": "proyek/", "anak": [
                {"teks": ".gitignore"},
                {"teks": "app.py"},
                {"teks": ".env ×"},
                {"teks": "build/ ×"},
                {"teks": "node_modules/ ×"},
                {"teks": "src/", "anak": [
                    {"teks": "hitung.py"},
                    {"teks": "__pycache__/ ×"},
                ]},
            ]},
        },
    ],
    "Mengubah Nama, Memindah, dan Menghapus Berkas Terlacak": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "git mv itu tiga langkah yang dipadatkan jadi satu",
            "ket": "Hasil akhirnya sama dengan mv biasa lalu git add untuk nama "
                   "lama dan nama baru.",
            "langkah": [
                {"jenis": "mulai", "teks": "git mv catatan.txt jurnal.txt"},
                {"jenis": "proses", "teks": "Pindahkan berkas di disk"},
                {"jenis": "proses", "teks": "git rm catatan.txt"},
                {"jenis": "proses", "teks": "git add jurnal.txt"},
                {"jenis": "keluaran", "teks": "R  catatan.txt -> jurnal.txt"},
            ],
        },
    ],
    "Membatalkan dengan Aman: restore, amend, revert": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Pilih perintah dari seberapa jauh perubahannya sudah pergi",
            "ket": "Sama dengan tabel di atas, dibaca sebagai pertanyaan. Cuma "
                   "git restore <berkas> yang membuang pekerjaan tanpa bisa kembali.",
            "langkah": [
                {"jenis": "mulai", "teks": "Mau membatalkan perubahan"},
                {"jenis": "keputusan", "teks": "Sudah di-commit?", "tidak": 5},
                {"jenis": "keputusan", "teks": "Sudah di-push?", "tidak": 4},
                {"jenis": "selesai", "teks": "git revert <hash>"},
                {"jenis": "selesai", "teks": "git commit --amend"},
                {"jenis": "keputusan", "teks": "Sudah di-add?", "tidak": 7},
                {"jenis": "selesai", "teks": "git restore --staged <berkas>"},
                {"jenis": "selesai", "teks": "git restore <berkas>"},
            ],
        },
        {
            "setelah": 6,
            "jenis": "git",
            "judul": "revert menambah commit, riwayat lama tetap utuh",
            "ket": "Commit D isinya kebalikan dari C. Siapa pun yang membaca log "
                   "bisa melihat perubahannya dan pembatalannya.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main",
                 "pesan": "Hapus tombol bayar"},
                {"id": "D", "induk": ["C"], "cabang": "main",
                 "pesan": "Revert C"},
            ],
            "label": {"main": "D"},
            "head": "main",
        },
    ],
    "Branch: Apa Itu dan Kenapa Begitu Murah": [
        {
            "setelah": 1,
            "jenis": "git",
            "judul": "Commit baru cuma memajukan cabang yang ditunjuk HEAD",
            "ket": "main diam di E. Dua commit baru hanya ada di fitur, karena HEAD "
                   "menunjuk fitur waktu keduanya dibuat.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["C"], "cabang": "main"},
                {"id": "E", "induk": ["D"], "cabang": "main"},
                {"id": "F", "induk": ["E"], "cabang": "fitur"},
                {"id": "G", "induk": ["F"], "cabang": "fitur"},
            ],
            "label": {"main": "E", "fitur": "G"},
            "head": "fitur",
        },
        {
            "setelah": 3,
            "jenis": "git",
            "judul": "Keluaran git log --graph --all tadi, digambar ulang",
            "ket": "6f8a adalah titik temunya. Sesudah itu main maju satu commit "
                   "dan fitur maju dua, dan keduanya belum bertemu lagi.",
            "commit": [
                {"id": "6f8a", "induk": [], "cabang": "main",
                 "pesan": "Rilis versi 1.0"},
                {"id": "7a9b", "induk": ["6f8a"], "cabang": "main",
                 "pesan": "Perbaiki tautan kaki"},
                {"id": "8b0c", "induk": ["6f8a"], "cabang": "fitur",
                 "pesan": "Buat halaman ulasan"},
                {"id": "9c1d", "induk": ["8b0c"], "cabang": "fitur",
                 "pesan": "Tambah formulir ulasan"},
            ],
            "label": {"main": "7a9b", "fitur": "9c1d"},
            "head": "fitur",
        },
    ],
    "Membuat, Berpindah, dan Menghapus Branch": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Folder yang sama, isinya ikut cabang yang dipijak",
            "ket": "Waktu kamu switch ke main, ulasan.html hilang dari folder "
                   "kerja. Isinya aman di commit cabang fitur-ulasan.",
            "tabel": [
                {"nama": "di main", "kolom": ["berkas"],
                 "baris": [["index.html"], ["gaya.css"]]},
                {"nama": "di fitur-ulasan", "kolom": ["berkas"],
                 "baris": [["index.html"], ["gaya.css"], ["ulasan.html"]],
                 "sorot_baris": [2]},
            ],
            "panah": "git switch menulis ulang folder kerja",
        },
    ],
    "Merge: Fast-forward vs Merge Commit": [
        {
            "setelah": 2,
            "jenis": "git",
            "judul": "Sesudah fast-forward: main tinggal dimajukan, tanpa commit baru",
            "ket": "main belum bergerak sejak fitur dibuat, jadi git merge fitur "
                   "memindahkan main dari C ke E. Riwayatnya tetap satu garis.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["C"], "cabang": "main"},
                {"id": "E", "induk": ["D"], "cabang": "main"},
            ],
            "label": {"main": "E", "fitur": "E"},
            "head": "main",
        },
        {
            "setelah": 3,
            "jenis": "git",
            "judul": "Merge commit M punya dua induk",
            "ket": "B nenek moyang bersamanya. Git membandingkan perubahan D dan G "
                   "sejak B, lalu membuat M di main.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["C"], "cabang": "main"},
                {"id": "E", "induk": ["B"], "cabang": "fitur"},
                {"id": "F", "induk": ["E"], "cabang": "fitur"},
                {"id": "G", "induk": ["F"], "cabang": "fitur"},
                {"id": "M", "induk": ["D", "G"], "cabang": "main",
                 "pesan": "Merge branch 'fitur'"},
            ],
            "label": {"main": "M", "fitur": "G"},
            "head": "main",
        },
    ],
    "Konflik Merge dan Cara Menyelesaikannya": [
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Dari CONFLICT sampai merge selesai",
            "ket": "Commit ditolak selama git status masih menyebut Unmerged paths. "
                   "Penanda yang lupa dihapus nggak dicegah, jadi cek dengan grep.",
            "langkah": [
                {"jenis": "mulai", "teks": "git merge fitur-slogan"},
                {"jenis": "keputusan", "teks": "Muncul CONFLICT?", "tidak": 7},
                {"jenis": "proses", "teks": "Buka berkas, putuskan isinya"},
                {"jenis": "proses", "teks": "Hapus ketiga baris penanda"},
                {"jenis": "proses", "teks": "git add judul.txt"},
                {"jenis": "keputusan", "teks": "Masih ada Unmerged paths?",
                 "ya": 2, "tidak": 6},
                {"jenis": "proses", "teks": "git commit"},
                {"jenis": "selesai", "teks": "Merge selesai"},
            ],
        },
    ],
    "Remote: clone, fetch, dan pull": [
        {
            "setelah": 4,
            "jenis": "git",
            "judul": "main lokalmu dua commit di depan origin/main",
            "ket": "origin/main cuma bergerak waktu fetch, pull, atau push. git "
                   "status melaporkannya sebagai ahead by 2 commits.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["C"], "cabang": "main"},
                {"id": "E", "induk": ["D"], "cabang": "main"},
            ],
            "label": {"main": "E", "origin/main": "C"},
            "head": "main",
        },
        {
            "setelah": 5,
            "jenis": "git",
            "judul": "Sesudah git fetch: commit baru datang, main belum disentuh",
            "ket": "git log main..origin/main menampilkan D dan E. git pull "
                   "sesudahnya memajukan main ke E lewat fast-forward.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["C"], "cabang": "origin/main"},
                {"id": "E", "induk": ["D"], "cabang": "origin/main"},
            ],
            "label": {"main": "C", "origin/main": "E"},
            "head": "main",
        },
    ],
    "GitHub: Akun, Kunci SSH, dan Repo Pertama": [
        {
            "setelah": 3,
            "jenis": "urutan",
            "judul": "Kunci SSH dipasang sekali, lalu push nggak pernah minta sandi",
            "ket": "Kunci privat nggak pernah meninggalkan laptopmu. Yang kamu "
                   "tempel di GitHub cuma kunci publik (.pub).",
            "pelaku": ["Laptopmu", "GitHub"],
            "pesan": [
                [0, 0, "ssh-keygen -t ed25519"],
                [0, 1, "tempel isi id_ed25519.pub"],
                [0, 1, "ssh -T git@github.com"],
                [1, 0, "Hi namamu! ...authenticated"],
                [0, 1, "git push -u origin main"],
            ],
        },
    ],
    "Push, Pull, dan Alur Harian": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Hari kerja dengan remote: pull di awal, push di akhir",
            "ket": "Di antara pull dan push boleh ada banyak commit. Yang belum "
                   "di-push cuma ada di satu laptop.",
            "langkah": [
                {"jenis": "mulai", "teks": "Awal hari"},
                {"jenis": "proses", "teks": "git pull"},
                {"jenis": "proses", "teks": "Sunting berkas"},
                {"jenis": "proses", "teks": "git add ."},
                {"jenis": "proses", "teks": "git commit -m \"...\""},
                {"jenis": "proses", "teks": "git push", "ke": 1},
            ],
        },
        {
            "setelah": 1,
            "jenis": "git",
            "judul": "Push ditolak karena origin punya commit F yang belum kamu punya",
            "ket": "git pull membuat merge commit yang menyatukan E dan F. Sesudah "
                   "itu push-mu jadi fast-forward di sisi remote.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["C"], "cabang": "main"},
                {"id": "E", "induk": ["D"], "cabang": "main"},
                {"id": "F", "induk": ["C"], "cabang": "origin/main"},
            ],
            "label": {"main": "E", "origin/main": "F"},
            "head": "main",
        },
    ],
    "Pull Request: Alur Kerja Tim di GitHub": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Satu pull request dari push sampai merge",
            "ket": "Commit perbaikan masuk ke PR yang sama karena dikirim ke "
                   "cabang yang sama. Nggak perlu membuka PR baru.",
            "pelaku": ["Kamu", "GitHub", "CI", "Peninjau"],
            "pesan": [
                [0, 1, "push fitur/ekspor-csv"],
                [0, 1, "buka pull request"],
                [1, 2, "jalankan tes"],
                [2, 1, "centang hijau"],
                [3, 1, "Request changes"],
                [0, 1, "push commit perbaikan"],
                [3, 1, "Approve"],
                [0, 1, "tekan Merge, hapus cabang"],
                [1, 0, "git pull di main"],
            ],
        },
        {
            "setelah": 3,
            "jenis": "git",
            "judul": "Squash and merge: tiga commit dilebur jadi satu di main",
            "ket": "S cuma punya satu induk, jadi riwayat main tetap lurus. "
                   "Rincian E, F, dan G nggak ikut masuk ke main.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "E", "induk": ["B"], "cabang": "fitur"},
                {"id": "F", "induk": ["E"], "cabang": "fitur"},
                {"id": "G", "induk": ["F"], "cabang": "fitur"},
                {"id": "S", "induk": ["B"], "cabang": "main",
                 "pesan": "isi E+F+G sekaligus"},
            ],
            "label": {"main": "S", "fitur": "G"},
            "head": "main",
        },
    ],
    "reset: Memundurkan HEAD dengan Tiga Tingkat Kekuatan": [
        {
            "setelah": 0,
            "jenis": "git",
            "judul": "Sesudah git reset --soft HEAD~1",
            "ket": "main mundur ke B. C masih ada di basis data, cuma nggak "
                   "ditunjuk siapa pun, dan ORIG_HEAD mengingatnya.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "tanpa penunjuk"},
            ],
            "label": {"main": "B", "ORIG_HEAD": "C"},
            "head": "main",
        },
    ],
    "Rebase: Riwayat Lurus dan rebase -i": [
        {
            "setelah": 0,
            "jenis": "git",
            "judul": "Cara pertama, merge main ke fitur: ada commit M",
            "ket": "Riwayatnya mencatat apa adanya bahwa dua garis pernah berjalan "
                   "sejajar. D dan E tetap dengan hash lamanya.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D", "induk": ["A"], "cabang": "fitur"},
                {"id": "E", "induk": ["D"], "cabang": "fitur"},
                {"id": "M", "induk": ["E", "C"], "cabang": "fitur"},
            ],
            "label": {"main": "C", "fitur": "M"},
            "head": "fitur",
        },
        {
            "setelah": 0,
            "jenis": "git",
            "judul": "Cara kedua, rebase main: D dan E disalin ulang di atas C",
            "ket": "D' dan E' commit baru dengan hash baru. D dan E yang lama "
                   "ditinggalkan, makanya cabang yang sudah dipakai orang lain "
                   "nggak boleh di-rebase.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main"},
                {"id": "D'", "induk": ["C"], "cabang": "fitur"},
                {"id": "E'", "induk": ["D'"], "cabang": "fitur"},
            ],
            "label": {"main": "C", "fitur": "E'"},
            "head": "fitur",
        },
    ],
    "Stash, Cherry-pick, dan Tag": [
        {
            "setelah": 2,
            "jenis": "git",
            "judul": "cherry-pick menyalin perubahan C ke main sebagai C'",
            "ket": "C' isinya sama dengan C tapi hash-nya beda, karena induknya B. "
                   "Commit D di fitur nggak ikut terbawa.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "D", "induk": ["A"], "cabang": "fitur"},
                {"id": "C", "induk": ["D"], "cabang": "fitur"},
                {"id": "C'", "induk": ["B"], "cabang": "main"},
            ],
            "label": {"main": "C'", "fitur": "C"},
            "head": "main",
        },
        {
            "setelah": 3,
            "jenis": "git",
            "judul": "Tag diam di tempat, cabang terus maju",
            "ket": "v1.0 tetap menunjuk C. Di F, git describe mencetak "
                   "v1.0-3-g diikuti potongan hash F, artinya tiga commit sesudah v1.0.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "main"},
                {"id": "C", "induk": ["B"], "cabang": "main", "pesan": "Rilis pertama"},
                {"id": "D", "induk": ["C"], "cabang": "main"},
                {"id": "E", "induk": ["D"], "cabang": "main"},
                {"id": "F", "induk": ["E"], "cabang": "main"},
            ],
            "label": {"main": "F", "v1.0": "C"},
            "head": "main",
        },
    ],
    "Reflog dan Bisect: Jaring Pengaman dan Detektif": [
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "Langkah pertama bisect: periksa commit di tengah",
            "ket": "Kalau c4 ternyata baik, pelakunya pasti di c5 sampai HEAD. "
                   "Tiap jawaban membuang separuh kandidat.",
            "nama": "riwayat",
            "isi": ["v1.0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
                    "HEAD"],
            "penunjuk": {"baik": 0, "coba": 4, "buruk": 9},
            "rentang": [1, 10],
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Putaran bisect sampai Git menyebut pelakunya",
            "ket": "git bisect run mengerjakan putaran ini sendiri: kode keluar 0 "
                   "berarti good, selain itu bad.",
            "langkah": [
                {"jenis": "mulai", "teks": "git bisect start"},
                {"jenis": "proses", "teks": "bisect bad, lalu good v1.0"},
                {"jenis": "proses", "teks": "Git pindah ke commit tengah"},
                {"jenis": "keputusan", "teks": "Tes lulus di commit ini?",
                 "tidak": 5},
                {"jenis": "proses", "teks": "git bisect good", "ke": 6},
                {"jenis": "proses", "teks": "git bisect bad"},
                {"jenis": "keputusan", "teks": "Git menyebut pelakunya?",
                 "tidak": 2},
                {"jenis": "selesai", "teks": "git bisect reset"},
            ],
        },
    ],
    "Konvensi Tim: Model Cabang, Hooks, dan CI": [
        {
            "setelah": 0,
            "jenis": "git",
            "judul": "GitHub Flow: cabang fitur pendek yang masuk lewat PR",
            "ket": "Tiap fitur hidup beberapa hari di cabangnya, lalu digabung ke "
                   "main dengan merge commit. main selalu siap rilis.",
            "commit": [
                {"id": "A", "induk": [], "cabang": "main"},
                {"id": "B", "induk": ["A"], "cabang": "fitur/login"},
                {"id": "M1", "induk": ["A", "B"], "cabang": "main"},
                {"id": "C", "induk": ["M1"], "cabang": "fitur/cari"},
                {"id": "D", "induk": ["C"], "cabang": "fitur/cari"},
                {"id": "M2", "induk": ["M1", "D"], "cabang": "main"},
            ],
            "label": {"main": "M2"},
            "head": "main",
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Hook pre-commit bisa membatalkan commit",
            "ket": "Skrip di .githooks/pre-commit menjalankan tes. Kalau keluar "
                   "dengan kode selain 0, commit-nya nggak pernah dibuat.",
            "langkah": [
                {"jenis": "mulai", "teks": "git commit -m \"...\""},
                {"jenis": "proses", "teks": "Git jalankan pre-commit"},
                {"jenis": "keputusan", "teks": "Skrip keluar dengan kode 0?",
                 "tidak": 4},
                {"jenis": "selesai", "teks": "Commit dibuat"},
                {"jenis": "selesai", "teks": "Commit batal, betulkan dulu"},
            ],
        },
    ],
}
