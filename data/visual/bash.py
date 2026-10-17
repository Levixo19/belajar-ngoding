"""Gambar konsep kurikulum Bash. Skema: inti/visual.py.

Bash nggak punya objek atau tipe data yang bisa digambar sebagai kotak, jadi
gambar di sini menunjukkan tiga hal yang paling susah dibayangkan dari teks:
ALUR (kondisi, perulangan, urutan pencarian PATH, berkas setelan mana yang
dibaca), POHON (folder, proses anak, JSON), dan DERET (bit izin, deskriptor,
argumen, isi array). Nilai di tiap gambar sama dengan contoh kode di dekatnya.
"""

VISUAL = {
    "Pengenalan Shell & Bash": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Apa yang terjadi waktu kamu mengetik ./program.sh",
            "ket": "Shebang dibaca sistem, bukan bash. Sesudah bash jalan, isi "
                   "berkas dibaca baris demi baris dari atas.",
            "langkah": [
                {"jenis": "mulai", "teks": "kamu ketik ./program.sh"},
                {"jenis": "proses", "teks": "sistem baca baris shebang"},
                {"jenis": "proses", "teks": "env cari bash di folder PATH"},
                {"jenis": "proses", "teks": "bash baca berkas baris demi baris"},
                {"jenis": "keluaran", "teks": "echo: Halo Dunia!"},
                {"jenis": "keluaran", "teks": "echo: Aku sedang belajar Bash."},
                {"jenis": "selesai", "teks": "baris habis, script selesai"},
            ],
        },
    ],
    "Izin Berkas & Hak Akses": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "Sepuluh karakter -rwxr-xr-x dibaca dari kiri",
            "ket": "Karakter pertama jenisnya, lalu tiga huruf untuk pemilik, tiga "
                   "untuk grup, tiga untuk lainnya. Ini izin sapa.sh, alias 755.",
            "nama": "sapa.sh",
            "isi": ["-", "r", "w", "x", "r", "-", "x", "r", "-", "x"],
            "penunjuk": {"jenis": 0, "pemilik": 1, "grup": 4, "lainnya": 7},
        },
    ],
    "Variabel & Quoting": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "Satu variabel nama=\"Andi\", empat cara menulisnya",
            "ket": "Petik ganda memproses $nama, petik tunggal membiarkannya apa "
                   "adanya, dan $'...' cuma memproses escape seperti \\n.",
            "tabel": [
                {
                    "kolom": ["ditulis", "hasil", "catatan"],
                    "baris": [
                        ["\"Halo $nama\"", "Halo Andi", "diproses"],
                        ["'Halo $nama'", "Halo $nama", "apa adanya"],
                        ["Halo $nama", "Halo Andi", "jalan, rawan"],
                        ["$'a\\nb'", "a, lalu b", "escape diproses"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Input & Output": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "Format dua spesifier mengambil argumen dua-dua tiap putaran",
            "ket": "printf '%-10s %5d\\n' apel 12 semangka 3 jeruk 108 memakai "
                   "formatnya tiga kali, jadi tabelnya tiga baris.",
            "nama": "argumen printf",
            "isi": ["apel", "12", "semangka", "3", "jeruk", "108"],
            "penunjuk": {"putaran1": 0, "putaran2": 2, "putaran3": 4},
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "cat data.txt | grep \"error\" | wc -l, dibaca kiri ke kanan",
            "ket": "Tiap tanda | menyambung keluaran perintah di kirinya jadi "
                   "masukan perintah di kanannya.",
            "langkah": [
                {"jenis": "masukan", "teks": "cat data.txt: semua baris"},
                {"jenis": "proses", "teks": "grep \"error\": sisakan yang cocok"},
                {"jenis": "proses", "teks": "wc -l: hitung barisnya"},
                {"jenis": "keluaran", "teks": "satu angka di layar"},
            ],
        },
    ],
    "Aliran Data & Deskriptor": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "Tiga saluran yang udah terbuka di setiap perintah",
            "ket": "Nomor kotaknya itulah nomor deskriptor. Makanya 2> berarti "
                   "stderr dan 2>&1 berarti sambungkan 2 ke tujuan 1.",
            "nama": "deskriptor",
            "isi": ["stdin", "stdout", "stderr"],
            "sorot": [2],
        },
        {
            "setelah": 4,
            "jenis": "larik",
            "judul": "IFS=',' read -ra nama <<< \"$teks\" memecah teks jadi array",
            "ket": "teks berisi andi,budi,citra. Indeks mulai dari 0, jadi "
                   "${nama[1]} adalah budi, orang kedua.",
            "nama": "nama",
            "isi": ["andi", "budi", "citra"],
            "sorot": [1],
        },
    ],
    "Proses, source, dan Subshell": [
        {
            "setelah": 4,
            "jenis": "pohon",
            "judul": "Tiga tempat yang jalan di proses anak, dan apa yang hilang",
            "ket": "Perubahan di proses anak ikut mati bersamanya. source x.sh dan "
                   "{ } nggak ada di pohon ini, karena keduanya jalan di shell itu "
                   "sendiri.",
            "akar": {
                "teks": "shell terminalmu",
                "anak": [
                    {"teks": "bash x.sh", "anak": [{"teks": "cd, var: hilang"}]},
                    {"teks": "( ... ) subshell", "anak": [{"teks": "cd, var: hilang"}]},
                    {"teks": "sisi kanan pipe", "anak": [{"teks": "read: hilang"}]},
                ],
            },
        },
    ],
    "Shell Interaktif: .bashrc, alias, dan PATH": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Berkas setelan mana yang dibaca, tergantung jenis shell-nya",
            "ket": "Disederhanakan: kalau ~/.bash_profile nggak ada, bash mencoba "
                   "~/.bash_login lalu ~/.profile. Baris jembatan itu dipasang "
                   "distro, bukan aturan bash.",
            "langkah": [
                {"jenis": "mulai", "teks": "bash dinyalakan"},
                {"jenis": "keputusan", "teks": "shell login? (SSH, su -)", "tidak": 4},
                {"jenis": "proses", "teks": "baca ~/.bash_profile"},
                {"jenis": "proses", "teks": "jembatan: . ~/.bashrc", "ke": 7},
                {"jenis": "keputusan", "teks": "interaktif? (tab terminal)", "tidak": 6},
                {"jenis": "proses", "teks": "baca ~/.bashrc", "ke": 7},
                {"jenis": "proses", "teks": "script: nggak baca dua-duanya"},
                {"jenis": "selesai", "teks": "mulai menjalankan perintah"},
            ],
        },
        {
            "setelah": 3,
            "jenis": "alur",
            "judul": "Cara bash mencari program waktu kamu mengetik ls",
            "ket": "Folder PATH diperiksa dari kiri ke kanan, dan pencarian "
                   "berhenti di folder pertama yang punya programnya.",
            "langkah": [
                {"jenis": "mulai", "teks": "kamu ketik ls"},
                {"jenis": "proses", "teks": "ambil folder PATH berikutnya"},
                {"jenis": "keputusan", "teks": "ada program ls di sana?", "tidak": 4},
                {"jenis": "keluaran", "teks": "jalankan, berhenti mencari", "ke": 6},
                {"jenis": "keputusan", "teks": "masih ada folder lain?", "ya": 1, "tidak": 5},
                {"jenis": "keluaran", "teks": "command not found"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "Aritmatika & Angka": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "a=15 dan b=4: pembagian bash membuang pecahannya",
            "ket": "Nilainya sama dengan contoh di atas. Cuma bc yang memberi "
                   "angka di belakang koma.",
            "tabel": [
                {
                    "kolom": ["tulisan", "hasil"],
                    "baris": [
                        ["$((a + b))", "19"],
                        ["$((a - b))", "11"],
                        ["$((a * b))", "60"],
                        ["$((a / b))", "3"],
                        ["$((a % b))", "3"],
                        ["bc, scale=3", "3.750"],
                    ],
                    "sorot_baris": [3],
                },
            ],
        },
    ],
    "Percabangan (if, case)": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "if, elif, else memeriksa syarat dari atas, berhenti di yang pertama benar",
            "ket": "Nilai 80 gagal di syarat pertama, lolos di syarat kedua, jadi "
                   "yang tercetak Nilai B dan syarat ketiga nggak pernah diperiksa.",
            "langkah": [
                {"jenis": "masukan", "teks": "read nilai"},
                {"jenis": "keputusan", "teks": "nilai -ge 85 ?", "tidak": 3},
                {"jenis": "keluaran", "teks": "Nilai A", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai -ge 75 ?", "tidak": 5},
                {"jenis": "keluaran", "teks": "Nilai B", "ke": 8},
                {"jenis": "keputusan", "teks": "nilai -ge 60 ?", "tidak": 7},
                {"jenis": "keluaran", "teks": "Nilai C", "ke": 8},
                {"jenis": "keluaran", "teks": "Tidak Lulus"},
                {"jenis": "selesai", "teks": "fi"},
            ],
        },
    ],
    "Perulangan (for, while, until)": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "{0..10..2} mekar jadi enam angka sebelum for mulai",
            "ket": "Brace expansion menyusun daftarnya dulu, lalu for mengambil "
                   "isinya satu per satu.",
            "nama": "{0..10..2}",
            "isi": ["0", "2", "4", "6", "8", "10"],
        },
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "while memeriksa syaratnya dulu, baru menjalankan isinya",
            "ket": "Contoh menjumlahkan 1 sampai 10. Begitu i jadi 11, syaratnya "
                   "salah dan perulangan selesai.",
            "langkah": [
                {"jenis": "mulai", "teks": "i=1, total=0"},
                {"jenis": "keputusan", "teks": "[[ $i -le 10 ]] ?", "tidak": 4},
                {"jenis": "proses", "teks": "total=$((total + i))"},
                {"jenis": "proses", "teks": "((i++))", "ke": 1},
                {"jenis": "keluaran", "teks": "Jumlah 1..10 = 55"},
                {"jenis": "selesai", "teks": "done"},
            ],
        },
    ],
    "Array": [
        {
            "setelah": 1,
            "jenis": "larik",
            "judul": "${buah[@]:1:2} mulai di indeks 1 dan mengambil dua item",
            "ket": "Ini isi buah sesudah buah+=(\"pisang\"). Hasil potongannya "
                   "jeruk mangga.",
            "nama": "buah",
            "isi": ["apel", "jeruk", "mangga", "pisang"],
            "rentang": [1, 3],
        },
    ],
    "Fungsi": [
        {
            "setelah": 3,
            "jenis": "tabel",
            "judul": "Argumen yang diterima cetak_daftar, dengan dan tanpa petik",
            "ket": "Tanpa petik, \"jeruk manis\" pecah di spasinya, jadi fungsinya "
                   "menerima empat item, bukan tiga.",
            "tabel": [
                {
                    "kolom": ["dipanggil", "$#", "$1", "$2", "$3", "$4"],
                    "baris": [
                        ["\"${buah[@]}\"", "3", "apel", "jeruk manis", "mangga", ""],
                        ["${buah[@]}", "4", "apel", "jeruk", "manis", "mangga"],
                    ],
                    "sorot_baris": [0],
                },
            ],
        },
    ],
    "Argumen & Exit Code": [
        {
            "setelah": 0,
            "jenis": "variabel",
            "judul": "./backup.sh /data /cadangan, dilihat dari dalam script",
            "ket": "$0 nama script-nya sendiri. Argumen yang kamu ketik mulai "
                   "dari $1.",
            "isi": [
                ["$0", "./backup.sh"],
                ["$1", "/data"],
                ["$2", "/cadangan"],
                ["$#", "2"],
            ],
        },
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "mkdir data && cd data: cd cuma jalan kalau mkdir sukses",
            "ket": "&& melihat exit code perintah di kirinya. 0 artinya sukses.",
            "langkah": [
                {"jenis": "proses", "teks": "mkdir data"},
                {"jenis": "keputusan", "teks": "exit code 0?", "tidak": 3},
                {"jenis": "proses", "teks": "cd data"},
                {"jenis": "selesai", "teks": "lanjut ke baris berikutnya"},
            ],
        },
    ],
    "Opsi Baris Perintah & getopts": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "while getopts mengambil satu opsi per putaran, lalu shift",
            "ket": "Sesudah perulangan, shift $((OPTIND - 1)) membuang semua opsi "
                   "yang udah terbaca.",
            "langkah": [
                {"jenis": "mulai", "teks": "OPTIND=1"},
                {"jenis": "keputusan", "teks": "getopts dapat opsi? (status 0)", "tidak": 4},
                {"jenis": "proses", "teks": "case $opt: h, v, o, \\?, :"},
                {"jenis": "proses", "teks": "OPTIND maju ke argumen berikut", "ke": 1},
                {"jenis": "proses", "teks": "shift $((OPTIND - 1))"},
                {"jenis": "keluaran", "teks": "$1 = posisional pertama"},
                {"jenis": "selesai", "teks": "kerjakan berkasnya"},
            ],
        },
    ],
    "Pola: Glob dan Regex": [
        {
            "setelah": 3,
            "jenis": "variabel",
            "judul": "Tiga grup ( ) di pola tanggal mengisi BASH_REMATCH",
            "ket": "Indeks 0 berisi seluruh teks yang cocok, lalu tiap grup sesuai "
                   "urutan kurung bukanya.",
            "isi": [
                ["BASH_REMATCH[0]", "2024-05-17"],
                ["BASH_REMATCH[1]", "2024"],
                ["BASH_REMATCH[2]", "05"],
                ["BASH_REMATCH[3]", "17"],
            ],
        },
    ],
    "Operasi String": [
        {
            "setelah": 0,
            "jenis": "larik",
            "judul": "${teks:0:7} mulai di indeks 0 dan mengambil tujuh karakter",
            "ket": "Cuma 12 karakter awal \"Belajar Bash Itu Seru\" yang digambar. "
                   "Kotak ␣ itu spasi. Hasil potongannya Belajar.",
            "nama": "teks",
            "isi": ["B", "e", "l", "a", "j", "a", "r", "␣", "B", "a", "s", "h"],
            "rentang": [0, 7],
        },
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "# dan ## membuang dari depan, % dan %% dari belakang",
            "ket": "berkas=\"/home/andi/laporan.tar.gz\". Tanda tunggal membuang yang "
                   "terpendek, tanda ganda yang terpanjang. ... = /home/andi.",
            "tabel": [
                {
                    "kolom": ["tulisan", "hasil"],
                    "baris": [
                        ["${berkas##*/}", "laporan.tar.gz"],
                        ["${berkas%/*}", "/home/andi"],
                        ["${berkas%.gz}", ".../laporan.tar"],
                        ["${berkas%%.*}", ".../laporan"],
                    ],
                },
            ],
        },
    ],
    "Bekerja dengan File & Folder": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Perulangan *.txt di contoh, termasuk pengaman [[ -e ]]",
            "ket": "Kalau folder nggak punya .txt, pola mentah *.txt jadi "
                   "satu-satunya nama, dan [[ -e ]] yang membuangnya.",
            "langkah": [
                {"jenis": "mulai", "teks": "folder=\"${1:-.}\""},
                {"jenis": "keputusan", "teks": "masih ada nama dari *.txt?", "tidak": 6},
                {"jenis": "keputusan", "teks": "[[ -e \"$berkas\" ]] ?", "tidak": 1},
                {"jenis": "proses", "teks": "baris=$(wc -l < \"$berkas\")"},
                {"jenis": "keluaran", "teks": "printf nama dan jumlah baris"},
                {"jenis": "proses", "teks": "jumlah++, total_baris += baris", "ke": 1},
                {"jenis": "keluaran", "teks": "N file, total M baris"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
    "find, xargs, dan Pemrosesan Massal": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "Pohon yang dibuat contoh find, ditelusuri sampai ke dasar",
            "ket": "find proyek -type f -name '*.log' menemukan server.log dan "
                   "kosong.log. Glob *.log di folder kerja nggak menemukan apa pun, "
                   "karena ia cuma melihat satu tingkat.",
            "akar": {
                "teks": "folder kerja",
                "anak": [
                    {"teks": "proyek/", "anak": [
                        {"teks": "src/", "anak": [{"teks": "utama.sh"}, {"teks": "bantu.sh"}]},
                        {"teks": "log/", "anak": [{"teks": "server.log"}, {"teks": "kosong.log"}]},
                        {"teks": "README.md"},
                    ]},
                    {"teks": "arsip/", "anak": [
                        {"teks": "laporan akhir.txt"},
                        {"teks": "lama.log"},
                        {"teks": "baru.log"},
                    ]},
                    {"teks": "patokan"},
                ],
            },
        },
    ],
    "grep, sed, dan awk": [
        {
            "setelah": 1,
            "jenis": "tabel",
            "judul": "awk -F',' memecah tiap baris nilai.csv jadi kolom $1, $2, $3",
            "ket": "Syarat $2 > 75 cuma lolos di baris andi dan citra, jadi itulah "
                   "dua baris yang dicetak.",
            "tabel": [
                {
                    "nama": "nilai.csv",
                    "kolom": ["$1", "$2", "$3"],
                    "baris": [
                        ["andi", "80", "90"],
                        ["budi", "70", "65"],
                        ["citra", "95", "88"],
                        ["dedi", "55", "60"],
                    ],
                    "sorot_baris": [0, 2],
                    "sorot_kolom": ["$2"],
                },
            ],
        },
    ],
    "Proses Latar Belakang, Sinyal, dan trap": [
        {
            "setelah": 4,
            "jenis": "alur",
            "judul": "Nyalakan di latar, tunggu siap, dan trap EXIT yang mematikan",
            "ket": "trap dipasang tepat sesudah $! diketahui. Jalan mana pun yang "
                   "diambil, server dimatikan waktu script berakhir.",
            "langkah": [
                {"jenis": "mulai", "teks": "server & lalu pid=$!"},
                {"jenis": "proses", "teks": "trap 'kill \"$pid\"' EXIT"},
                {"jenis": "keputusan", "teks": "berkas tanda siap ada?", "ya": 5, "tidak": 3},
                {"jenis": "keputusan", "teks": "masih ada jatah percobaan?", "tidak": 5},
                {"jenis": "proses", "teks": "sleep 0.5", "ke": 2},
                {"jenis": "proses", "teks": "pakai servernya"},
                {"jenis": "selesai", "teks": "script berakhir, trap EXIT jalan"},
            ],
        },
    ],
    "Alat Pendamping: curl, jq, date, tar": [
        {
            "setelah": 1,
            "jenis": "pohon",
            "judul": "pegawai.json sebagai pohon, tempat filter jq berjalan",
            "ket": ".pegawai[].nama masuk ke pegawai, membuka tiap elemen, lalu "
                   "mengambil nama: Andi, Budi, Citra. Kunci lain disembunyikan.",
            "akar": {
                "teks": "{ }",
                "anak": [
                    {"teks": "kantor", "anak": [{"teks": "\"Cabang Selatan\""}]},
                    {"teks": "pegawai [ ]", "anak": [
                        {"teks": "[0]", "anak": [{"teks": "nama: \"Andi\""}, {"teks": "aktif: true"}]},
                        {"teks": "[1]", "anak": [{"teks": "nama: \"Budi\""}, {"teks": "aktif: false"}]},
                        {"teks": "[2]", "anak": [{"teks": "nama: \"Citra\""}, {"teks": "aktif: true"}]},
                    ]},
                ],
            },
        },
    ],
    "Debugging & Praktik Baik": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Jalannya utama() di kerangka backup.sh",
            "ket": "Tiap pemeriksaan yang gagal berakhir di galat(), yang menulis "
                   "ke stderr lalu exit 1.",
            "langkah": [
                {"jenis": "mulai", "teks": "utama \"$@\""},
                {"jenis": "keputusan", "teks": "argumen pertama -h?", "tidak": 3},
                {"jenis": "keluaran", "teks": "bantuan, lalu exit 0", "ke": 8},
                {"jenis": "keputusan", "teks": "tepat 2 argumen?", "tidak": 7},
                {"jenis": "keputusan", "teks": "folder sumber ada?", "tidak": 7},
                {"jenis": "proses", "teks": "mkdir -p tujuan, cp -r"},
                {"jenis": "keluaran", "teks": "pesan: Selesai menyalin", "ke": 8},
                {"jenis": "keluaran", "teks": "galat: pesan ke stderr, exit 1"},
                {"jenis": "selesai", "teks": "script berakhir"},
            ],
        },
    ],
    "Bash vs sh: Portabilitas & POSIX": [
        {
            "setelah": 0,
            "jenis": "pohon",
            "judul": "/bin/sh itu peran, dan tiap sistem mengisinya dengan program lain",
            "ket": "Cuma di Fedora, Arch, dan macOS sh-nya bash, jadi script penuh "
                   "bashism bisa lolos di sana lalu bisa gagal di Debian atau Alpine.",
            "akar": {
                "teks": "/bin/sh",
                "anak": [
                    {"teks": "Debian, Ubuntu", "anak": [{"teks": "dash"}]},
                    {"teks": "Alpine", "anak": [{"teks": "busybox ash"}]},
                    {"teks": "Fedora, Arch", "anak": [{"teks": "bash mode sh"}]},
                    {"teks": "macOS", "anak": [{"teks": "bash 3.2 mode sh"}]},
                ],
            },
        },
    ],
    "Fitur Bash Lanjutan": [
        {
            "setelah": 3,
            "jenis": "larik",
            "judul": "uji | tee hasil.log: satu kode keluar untuk tiap tahap",
            "ket": "$? cuma melihat kotak terakhir, milik tee. Kegagalan uji ada di "
                   "${PIPESTATUS[0]}, dan harus disalin sebelum perintah lain jalan.",
            "nama": "PIPESTATUS",
            "isi": ["1", "0"],
            "sorot": [0],
            "penunjuk": {"uji": 0, "tee": 1},
        },
    ],
    "Studi Kasus: Pengelola Catatan": [
        {
            "setelah": 1,
            "jenis": "alur",
            "judul": "Dari ./catatan.sh perintah argumen sampai fungsi yang tepat",
            "ket": "Disederhanakan: daftar, cari, hapus, dan hitung masing-masing "
                   "punya cabang case sendiri yang memanggil fungsi bernama sama.",
            "langkah": [
                {"jenis": "mulai", "teks": "./catatan.sh perintah argumen"},
                {"jenis": "proses", "teks": "siapkan: touch berkas catatan"},
                {"jenis": "proses", "teks": "perintah=${1:-bantuan}; shift"},
                {"jenis": "keputusan", "teks": "perintah tambah?", "tidak": 5},
                {"jenis": "proses", "teks": "tambah \"$@\"", "ke": 8},
                {"jenis": "keputusan", "teks": "daftar/cari/hapus/hitung?", "tidak": 7},
                {"jenis": "proses", "teks": "panggil fungsi bernama sama", "ke": 8},
                {"jenis": "keluaran", "teks": "cabang *: bantuan"},
                {"jenis": "selesai", "teks": "selesai"},
            ],
        },
    ],
}
