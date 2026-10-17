BASH_QUIZZES = [
    {
        "title": "Kuis 1: Dasar Bash & Variabel",
        "questions": [
            {
                "q": "Baris #!/usr/bin/env bash di awal script disebut?",
                "options": ["Header", "Shebang", "Prolog", "Manifest"],
                "answer": 1,
                "explanation": "Shebang memberi tahu sistem program mana yang harus menjalankan berkas ini.",
            },
            {
                "q": "Manakah cara membuat variabel yang BENAR di bash?",
                "options": ["nama = \"Andi\"", "nama=\"Andi\"", "var nama = \"Andi\"", "let nama = \"Andi\""],
                "answer": 1,
                "explanation": ("Nggak boleh ada spasi di sekitar tanda =. Dengan spasi, bash mengira "
                                "'nama' itu nama perintah. var dan let nggak dipakai untuk mengisi teks."),
            },
            {
                "q": "Apa perbedaan \"$nama\" dan '$nama'?",
                "options": [
                    "Nggak ada bedanya, keduanya mengisi variabel",
                    "Petik ganda mengisi variabel, petik tunggal apa adanya",
                    "Petik tunggal mengisi variabel, ganda apa adanya",
                    "Petik tunggal cuma boleh dipakai untuk satu huruf",
                ],
                "answer": 1,
                "explanation": ("Di dalam petik ganda, $nama dan $(...) diganti isinya. Di dalam petik "
                                "tunggal semuanya literal, jadi yang tercetak tetap tulisan $nama."),
            },
            {
                "q": "Perintah apa yang memberi izin eksekusi pada file script?",
                "options": ["chown +x file.sh", "chmod +x file.sh", "exec file.sh", "chmod 644 file.sh"],
                "answer": 1,
                "explanation": ("chmod +x menambahkan bit executable, jadi berkasnya bisa dijalankan "
                                "dengan ./file.sh. chmod 644 justru nggak memberi izin eksekusi ke siapa "
                                "pun, dan chown mengganti pemilik."),
            },
            {
                "q": "Variabel khusus $? berisi apa?",
                "options": [
                    "Jumlah argumen yang diberikan ke script",
                    "Nama script yang sedang berjalan",
                    "Kode keluar perintah terakhir",
                    "Process ID dari script itu sendiri",
                ],
                "answer": 2,
                "explanation": ("$? menyimpan exit code perintah terakhir; 0 berarti sukses. Jumlah "
                                "argumen ada di $#, nama script di $0, dan PID di $$."),
            },
            {
                "q": "Bagaimana cara menyimpan hasil sebuah perintah ke variabel?",
                "options": ["x = $(date)", "x=$(date)", "x=$date", "x=\"date\""],
                "answer": 1,
                "explanation": ("$(perintah) disebut command substitution: perintahnya dijalankan, lalu "
                                "output-nya jadi nilai. $date cuma membaca variabel bernama date, dan "
                                "spasi di sekitar = tetap dilarang."),
            },
            {
                "q": "Kenapa ${nama} lebih aman daripada $nama?",
                "options": [
                    "Kurung kurawal bikin bash jalan lebih cepat",
                    "Batas nama variabel jadi jelas kalau ditempel teks",
                    "Kurung kurawal otomatis menambahkan petik ganda",
                    "Cuma bentuk berkurawal yang sah di bash",
                ],
                "answer": 1,
                "explanation": ("Pada \"${nama}ku\", kurawal menandai bahwa nama variabelnya 'nama', "
                                "bukan 'namaku'. Kurawal nggak menggantikan petik ganda."),
            },
            {
                "q": "Berapa tipe data yang dikenal bash untuk variabel biasa?",
                "options": [
                    "Empat: int, float, string, bool",
                    "Dua: angka dan teks",
                    "Pada dasarnya satu: semuanya string",
                    "Tiga: int, string, dan array",
                ],
                "answer": 2,
                "explanation": ("Bash nggak punya sistem tipe seperti bahasa lain. Nilai disimpan sebagai "
                                "string dan baru diperlakukan sebagai angka saat dihitung, misalnya di $(( ))."),
            },
        ],
    },
    {
        "title": "Kuis 2: Input, Output & Aritmatika",
        "questions": [
            {
                "q": "Perintah untuk membaca input dari keyboard adalah?",
                "options": ["input", "read", "scan", "gets"],
                "answer": 1,
                "explanation": "read menyimpan baris yang diketik ke dalam variabel.",
            },
            {
                "q": "Apa arti operator > dalam 'echo halo > file.txt'?",
                "options": [
                    "Menambahkan teks ke akhir file",
                    "Menulis ke file, menimpa isi lamanya",
                    "Membandingkan dua nilai",
                    "Membaca isi file.txt sebagai input",
                ],
                "answer": 1,
                "explanation": "> menimpa isi file. Untuk menambahkan di akhir pakai >>, dan untuk membaca dari file pakai <.",
            },
            {
                "q": "Berapa hasil dari echo $((10 / 3)) ?",
                "options": ["3.33", "3", "4", "error"],
                "answer": 1,
                "explanation": "Aritmatika bawaan bash cuma bilangan bulat, jadi sisa pembagiannya dibuang.",
            },
            {
                "q": "Untuk perhitungan desimal di bash, alat yang umum dipakai adalah?",
                "options": ["expr atau let", "bc atau awk", "$(( )) dan let", "declare -i"],
                "answer": 1,
                "explanation": ("bc dan awk bisa menghitung bilangan pecahan. expr, let, $(( )), dan "
                                "declare -i semuanya cuma kenal bilangan bulat."),
            },
            {
                "q": "Apa fungsi tanda | (pipe)?",
                "options": [
                    "Menjalankan perintah kanan kalau kiri gagal",
                    "Mengirim output kiri jadi input kanan",
                    "Menyimpan output kiri ke sebuah file",
                    "Menjalankan kanan sesudah kiri selesai",
                ],
                "answer": 1,
                "explanation": ("Pipe merangkai perintah: output yang satu langsung jadi input berikutnya. "
                                "Yang jalan kalau gagal itu ||, yang menyimpan ke file itu >, dan yang "
                                "sekadar berurutan itu titik koma."),
            },
            {
                "q": "Ke mana '2> galat.log' mengalihkan keluaran?",
                "options": [
                    "Output normal saja",
                    "Pesan error (stderr) saja",
                    "Output dan error sekaligus",
                    "Input dari file",
                ],
                "answer": 1,
                "explanation": "Deskriptor 2 adalah stderr. Deskriptor 1 adalah stdout, dan 0 adalah stdin.",
            },
            {
                "q": "Apa guna /dev/null?",
                "options": [
                    "Tempat menyimpan log sistem",
                    "Membuang output yang nggak diperlukan",
                    "Folder untuk berkas sementara",
                    "Berkas pengaturan bawaan bash",
                ],
                "answer": 1,
                "explanation": ("/dev/null itu tempat sampah sistem: semua yang ditulis ke sana langsung "
                                "hilang. Folder sementara itu /tmp."),
            },
            {
                "q": "Mana yang lebih bisa diandalkan lintas shell untuk output berformat?",
                "options": ["echo -e", "printf", "cat", "write"],
                "answer": 1,
                "explanation": "Perilaku echo -e berbeda antar shell, sedangkan printf konsisten di mana-mana.",
            },
        ],
    },
    {
        "title": "Kuis 3: Percabangan",
        "questions": [
            {
                "q": "Kata kunci penutup blok if di bash adalah?",
                "options": ["end", "endif", "fi", "done"],
                "answer": 2,
                "explanation": "Blok if ditutup dengan 'fi', yaitu kata 'if' dibalik.",
            },
            {
                "q": "Operator perbandingan untuk 'lebih besar dari' pada ANGKA di dalam [[ ]] adalah?",
                "options": [">", "-gt", "-ge", "-lt"],
                "answer": 1,
                "explanation": ("Untuk angka pakai -gt (greater than). -ge artinya lebih besar atau sama "
                                "dengan, -lt lebih kecil. Tanda > di dalam [[ ]] membandingkan urutan "
                                "abjad, bukan nilai."),
            },
            {
                "q": "Kenapa [[ ]] lebih disarankan daripada [ ] ?",
                "options": [
                    "Lebih pendek dan cepat diketik",
                    "Aman untuk variabel kosong, dan bisa && serta regex",
                    "Cuma [[ ]] yang bisa membandingkan angka",
                    "[ ] sudah dihapus dari bash versi baru",
                ],
                "answer": 1,
                "explanation": ("[[ ]] adalah keyword bash yang nggak memecah isi variabel, jadi variabel "
                                "kosong atau berspasi nggak bikin error. [ ] masih ada dan juga kenal -gt."),
            },
            {
                "q": "Operator -z pada [[ -z \"$x\" ]] memeriksa apa?",
                "options": [
                    "Apakah x berupa angka nol",
                    "Apakah string x kosong",
                    "Apakah file x ada",
                    "Apakah x sudah dideklarasikan",
                ],
                "answer": 1,
                "explanation": "-z benar kalau panjang string nol. Kebalikannya -n, untuk string yang nggak kosong.",
            },
            {
                "q": "Operator untuk memeriksa apakah sebuah FOLDER ada?",
                "options": ["-f", "-d", "-e", "-r"],
                "answer": 1,
                "explanation": "-d untuk folder, -f untuk berkas biasa, -e untuk keduanya (ada, apa pun jenisnya).",
            },
            {
                "q": "Setiap cabang di dalam blok case harus diakhiri dengan?",
                "options": ["break", ";;", "}", "esac"],
                "answer": 1,
                "explanation": ";; menandai akhir sebuah cabang case. Blok case-nya sendiri ditutup 'esac'.",
            },
            {
                "q": "Pola apa yang berfungsi sebagai 'default' di dalam case?",
                "options": ["default", "else", "*", "_"],
                "answer": 2,
                "explanation": "Tanda * cocok dengan apa pun, jadi ditaruh paling akhir sebagai cabang default.",
            },
            {
                "q": "Perintah 'mkdir data && cd data' berarti?",
                "options": [
                    "Jalankan keduanya bersamaan",
                    "cd cuma jalan kalau mkdir berhasil",
                    "cd cuma jalan kalau mkdir gagal",
                    "Jalankan cd lebih dulu",
                ],
                "answer": 1,
                "explanation": ("&& menjalankan perintah kanan cuma kalau perintah kiri keluar dengan "
                                "kode 0. Yang jalan kalau gagal itu ||."),
            },
        ],
    },
    {
        "title": "Kuis 4: Perulangan & Array",
        "questions": [
            {
                "q": "Blok perulangan di bash diapit oleh kata kunci?",
                "options": ["begin ... end", "do ... done", "{ ... }", "loop ... pool"],
                "answer": 1,
                "explanation": "Semua bentuk perulangan bash (for, while, until) memakai do dan done.",
            },
            {
                "q": "Apa hasil dari for i in {1..5}; do echo $i; done ?",
                "options": [
                    "Mencetak teks '{1..5}'",
                    "Mencetak angka 1 sampai 5",
                    "Mencetak angka 1 sampai 4",
                    "Error",
                ],
                "answer": 1,
                "explanation": "{1..5} adalah brace expansion yang menghasilkan deret 1 2 3 4 5, ujungnya ikut.",
            },
            {
                "q": "Bagaimana cara BENAR membaca file baris demi baris?",
                "options": [
                    "for baris in $(cat file); do ... done",
                    "while IFS= read -r baris; do ... done < file",
                    "while IFS= read -r baris < file; do ... done",
                    "cat file | for baris; do ... done",
                ],
                "answer": 1,
                "explanation": ("Pengalihan < file ditaruh sesudah done supaya berkasnya dibuka sekali. "
                                "Kalau ditaruh di read, berkasnya dibuka ulang tiap putaran dan yang "
                                "terbaca baris pertama terus. for dengan $(cat) memecah per kata, bukan per baris."),
            },
            {
                "q": "Bagaimana mengakses SELURUH isi array bernama buah?",
                "options": ["$buah", "${buah}", "${buah[@]}", "${buah[*all]}"],
                "answer": 2,
                "explanation": "$buah dan ${buah} cuma memberi elemen pertama. Untuk semua elemen pakai \"${buah[@]}\".",
            },
            {
                "q": "Ekspresi ${#buah[@]} menghasilkan apa?",
                "options": [
                    "Elemen pertama",
                    "Jumlah elemen array",
                    "Panjang karakter elemen pertama",
                    "Indeks terakhir",
                ],
                "answer": 1,
                "explanation": "Tanda # di depan nama array memberikan banyaknya elemen.",
            },
            {
                "q": "Apa yang WAJIB dilakukan sebelum memakai associative array?",
                "options": [
                    "Nggak ada, langsung pakai",
                    "declare -A namaarray",
                    "declare -a namaarray",
                    "set -A namaarray",
                ],
                "answer": 1,
                "explanation": ("Huruf A besar untuk associative, a kecil untuk array berindeks angka. "
                                "Tanpa declare -A, bash memperlakukannya sebagai array indeks angka "
                                "dan hasilnya salah tanpa pesan error."),
            },
            {
                "q": "Perintah 'continue' di dalam perulangan berfungsi untuk?",
                "options": [
                    "Keluar dari perulangan sepenuhnya",
                    "Lompat ke putaran berikutnya",
                    "Mengulang putaran yang sama sekali lagi",
                    "Menghentikan seluruh script",
                ],
                "answer": 1,
                "explanation": "continue melewati sisa badan perulangan dan langsung lanjut ke putaran berikutnya. Yang keluar dari perulangan itu break.",
            },
            {
                "q": "Apa beda while dan until?",
                "options": [
                    "until jalan selama benar, while jalan sampai benar",
                    "while jalan selama benar, until jalan sampai benar",
                    "until cuma bisa dipakai untuk membandingkan angka",
                    "Sama saja, until cuma nama lain dari while",
                ],
                "answer": 1,
                "explanation": "until kebalikan while: badan perulangannya jalan selama kondisinya masih salah, dan berhenti begitu kondisinya benar.",
            },
        ],
    },
    {
        "title": "Kuis 5: Fungsi, String & Praktik Baik",
        "questions": [
            {
                "q": "Bagaimana cara memanggil fungsi bernama sapa dengan argumen \"Andi\"?",
                "options": ["sapa(\"Andi\")", "sapa \"Andi\"", "call sapa Andi", "$sapa(Andi)"],
                "answer": 1,
                "explanation": "Fungsi bash dipanggil seperti perintah biasa: nama diikuti argumen yang dipisah spasi, tanpa kurung.",
            },
            {
                "q": "Perintah return di dalam fungsi bash mengirimkan apa?",
                "options": [
                    "Nilai apa pun, termasuk teks",
                    "Kode status 0 sampai 255",
                    "String hasil olahan fungsi",
                    "Seluruh isi array sekaligus",
                ],
                "answer": 1,
                "explanation": "return cuma untuk exit code. Untuk mengirim data, cetak dengan echo lalu tangkap dengan $(...).",
            },
            {
                "q": "Apa gunanya kata kunci local di dalam fungsi?",
                "options": [
                    "Bikin fungsi jalan lebih cepat",
                    "Variabelnya cuma hidup di dalam fungsi",
                    "Bikin variabel jadi read-only",
                    "Mengekspor variabel ke proses anak",
                ],
                "answer": 1,
                "explanation": ("Tanpa local, variabel bersifat global dan bisa menimpa variabel bernama "
                                "sama di luar fungsi. read-only itu readonly, dan mengekspor itu export."),
            },
            {
                "q": "Ekspresi ${berkas##*/} pada \"/home/andi/data.txt\" menghasilkan?",
                "options": ["/home/andi", "data.txt", "home", ".txt"],
                "answer": 1,
                "explanation": "## membuang pencocokan terpanjang dari depan, jadi semua sampai garis miring terakhir hilang dan tersisa nama berkasnya.",
            },
            {
                "q": "Ekspresi ${nama:-Tamu} berarti?",
                "options": [
                    "Simpan 'Tamu' ke nama kalau kosong",
                    "Pakai isi nama, atau 'Tamu' kalau kosong",
                    "Bandingkan isi nama dengan teks Tamu",
                    "Hapus 'Tamu' dari ujung isi nama",
                ],
                "answer": 1,
                "explanation": ("Bentuk :- memberi nilai bawaan tanpa mengubah isi variabelnya. Yang "
                                "sekalian menyimpan 'Tamu' ke variabel itu bentuk :=."),
            },
            {
                "q": "Apa efek dari 'set -e' di awal script?",
                "options": [
                    "Menampilkan tiap perintah sebelum dijalankan",
                    "Berhenti begitu ada perintah yang gagal",
                    "Menganggap variabel yang belum ada sebagai error",
                    "Mengabaikan semua error dan jalan terus",
                ],
                "answer": 1,
                "explanation": ("set -e menghentikan script saat ada perintah yang keluar dengan kode bukan "
                                "nol. Menampilkan tiap perintah itu set -x, dan menolak variabel yang belum "
                                "ada itu set -u."),
            },
            {
                "q": "Alat linter yang dipakai untuk memeriksa kualitas script bash adalah?",
                "options": ["markdownlint", "shellcheck", "pylint", "eslint"],
                "answer": 1,
                "explanation": ("shellcheck menganalisis script dan menangkap kesalahan umum seperti "
                                "variabel tanpa petik. Tiga lainnya linter untuk Markdown, Python, dan JavaScript."),
            },
            {
                "q": "Kenapa variabel sebaiknya selalu dibungkus petik ganda, seperti rm \"$file\"?",
                "options": [
                    "Supaya lebih rapi dan enak dibaca",
                    "Supaya nama berspasi tetap jadi satu argumen",
                    "Supaya isi variabel nggak diganti nilainya",
                    "Karena bash menolak variabel tanpa petik",
                ],
                "answer": 1,
                "explanation": ("Tanpa petik, bash memecah nilai berdasarkan spasi. Nama berkas 'laporan "
                                "akhir.txt' dianggap dua berkas berbeda. Petik ganda tetap mengganti "
                                "variabel dengan isinya."),
            },
        ],
    },
]
