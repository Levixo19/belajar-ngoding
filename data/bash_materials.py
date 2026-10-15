BASH_MATERIALS = [
    {
        "title": "1. Pengenalan Shell & Bash",
        "sections": [
            {
                "body": [
                    "Shell adalah program yang menerima perintah berupa teks, lalu",
                    "menjalankannya. Gampangnya, shell itu perantara antara kamu dan kernel,",
                    "yaitu inti sistem operasi. Kamu ngetik perintah, shell yang nyampein ke",
                    "sistem supaya dikerjakan.",
                    "",
                    "Shell ada banyak macamnya, misalnya sh, bash, zsh, fish, dash, dan ksh.",
                    "",
                    "Bash singkatan dari Bourne Again SHell.",
                    "  - Bash jadi shell bawaan di kebanyakan distro Linux dan di WSL.",
                    "  - Bash dibikin Brian Fox tahun 1989 sebagai pengganti sh yang bebas",
                    "    dipakai siapa aja.",
                    "  - macOS sekarang pakai zsh sebagai bawaan, tapi bash tetap ada di",
                    "    sana.",
                    "",
                    "Kenapa belajar Bash?",
                    "  - Buat ngotomatiskan tugas yang berulang, misalnya backup, deploy,",
                    "    atau mengubah format berkas.",
                    "  - Kamu bakal butuh Bash kalau kerja di server, pakai Docker, atau",
                    "    ngurus CI/CD, yaitu proses yang otomatis menguji dan memasang",
                    "    program tiap kali kodenya berubah.",
                    "  - Bash udah terpasang di mana-mana, jadi nggak perlu install apa pun.",
                    "",
                    "Mau tahu versi bash di komputermu? Ketik ini di terminal:",
                    "  bash --version",
                    "",
                    "Ada dua cara memakai bash:",
                    "  1. Interaktif: kamu ngetik perintah satu per satu di terminal, dan",
                    "     tiap perintah langsung dijalankan.",
                    "  2. Script: perintah-perintahnya kamu simpan dulu di berkas .sh, lalu",
                    "     berkas itu dijalankan. Script itu cuma berkas teks berisi daftar",
                    "     perintah.",
                ]
            },
            {
                "heading": "Script pertama",
                "code": """#!/usr/bin/env bash
echo "Halo Dunia!"
echo "Aku sedang belajar Bash." """
            },
            {
                "body": [
                    "Baris pertama script tadi namanya shebang:",
                    "",
                    "  #!/usr/bin/env bash",
                    "",
                    "Shebang ngasih tahu sistem: \"jalankan berkas ini pakai bash\". Tempatnya",
                    "harus di baris pertama, tanpa spasi di depannya. Kamu juga bakal sering",
                    "ketemu bentuk #!/bin/bash. Bentuk yang pakai env lebih gampang dibawa",
                    "ke komputer lain, karena env nyari bash di PATH. PATH itu daftar folder",
                    "tempat sistem mencari program.",
                    "",
                    "Sesudah shebang ada echo \"...\". echo adalah perintah untuk menampilkan",
                    "teks ke layar.",
                    "",
                    "Ada dua cara menjalankan script ini:",
                    "  1. Lewat bash langsung: bash program.sh. Ini cara paling gampang,",
                    "     karena berkasnya nggak perlu izin eksekusi, yaitu izin untuk",
                    "     dijalankan sebagai program.",
                    "  2. Kasih izin eksekusi dulu, baru jalankan berkasnya:",
                    "       chmod +x program.sh",
                    "       ./program.sh",
                    "     chmod +x memberi izin \"boleh dijalankan\". Tanda ./ artinya \"berkas",
                    "     yang ada di folder ini\".",
                    "",
                    "Komentar ditulis pakai tanda pagar. Bash nggak menjalankan apa pun yang",
                    "ada sesudah tanda itu:",
                    "",
                    "  # ini komentar, diabaikan bash",
                    "",
                    "Bash nggak punya komentar banyak baris yang resmi. Kalau komentarnya",
                    "panjang, kasih # di awal tiap baris.",
                    "",
                    "Kalau mau nulis beberapa perintah di satu baris, pisahkan pakai titik",
                    "koma:",
                    "",
                    "  mkdir catatan ; cd catatan",
                    "",
                    "Dua perintah itu dijalankan berurutan, apa pun hasil perintah yang",
                    "pertama. Jadi kalau mkdir gagal, cd tetap dicoba.",
                    "",
                    "Kebalikannya juga bisa: satu perintah dipecah jadi beberapa baris.",
                    "Caranya, taruh backslash (\\) di ujung baris. Backslash itu nyambungin",
                    "baris itu ke baris berikutnya:",
                    "",
                    "  cp -r \\",
                    "      laporan/ \\",
                    "      cadangan/",
                    "",
                    "Bash membacanya sebagai satu perintah utuh. Ini berguna buat perintah",
                    "yang panjang, misalnya curl dengan sepuluh opsi atau docker run yang",
                    "penuh flag. Perintahnya jadi enak dibaca, dan perubahannya gampang",
                    "dilihat waktu dua versi berkas dibandingkan pakai diff.",
                    "",
                    "Jebakan: backslash harus jadi karakter paling akhir di barisnya. Kalau",
                    "sesudahnya ada satu spasi aja, sambungannya batal. Bash nganggap",
                    "perintahnya udah selesai di situ, lalu ngeluh soal argumen yang kurang,",
                    "atau menjalankan baris berikutnya sebagai perintah sendiri. Spasi itu",
                    "nggak kelihatan di layar, jadi ingat-ingat aja gejalanya.",
                ]
            },
        ],
    },
    {
        "title": "2. Izin Berkas & Hak Akses",
        "sections": [
            {
                "body": [
                    "Dari perintah pertama, kamu udah sering lihat baris kayak gini, dan",
                    "mungkin kamu lewati aja:",
                    "",
                    "  $ ls -l",
                    "  -rw-r--r--  1 andi tim   142 Jan  5 09:11 catatan.txt",
                    "  -rwxr-xr-x  1 andi tim    59 Jan  5 09:12 sapa.sh",
                    "  drwxr-xr-x  2 andi tim  4096 Jan  5 09:12 arsip",
                    "",
                    "Kolom pertama itu isinya izin berkas, yaitu aturan siapa boleh ngapain",
                    "terhadap berkas itu. Panjangnya sepuluh karakter, dibaca dari kiri:",
                    "",
                    "  -  rwx  r-x  r-x",
                    "  ^   ^    ^    ^",
                    "  |   |    |    +--- LAINNYA (other): siapa pun lagi di mesin ini",
                    "  |   |    +-------- GRUP (group): anggota grup pemilik berkas",
                    "  |   +------------- PEMILIK (user): akun yang memiliki berkas",
                    "  +----------------- jenis: - berkas biasa, d folder, l symlink",
                    "",
                    "Karakter pertama menunjukkan jenisnya. Huruf l artinya symlink, yaitu",
                    "jalan pintas yang menunjuk ke berkas lain. Nama pemilik dan grupnya ada",
                    "di kolom 3 dan 4 (di contoh atas: andi dan tim).",
                    "",
                    "Tiap golongan isinya tiga huruf, urutannya selalu r, w, x. Tiap huruf",
                    "itu disebut bit izin, semacam saklar yang bisa nyala atau mati. Tanda -",
                    "artinya saklarnya mati.",
                    "",
                    "Untuk berkas, artinya begini:",
                    "  r  boleh dibaca isinya (cat, grep, cp, editor)",
                    "  w  boleh diubah isinya",
                    "  x  boleh dijalankan sebagai program",
                    "",
                    "Untuk folder hurufnya sama, tapi artinya beda. Bagian ini yang paling",
                    "sering bikin salah paham:",
                    "  r  boleh melihat DAFTAR NAMA di dalamnya (ls)",
                    "  x  boleh MASUK dan menyentuh isinya (cd, membuka berkas di dalamnya)",
                    "  w  boleh menambah, mengganti nama, dan MENGHAPUS berkas di dalamnya",
                    "",
                    "Akibatnya ada dua hal yang kelihatan aneh, tapi memang begitu aturannya:",
                    "  - Folder yang punya r tapi nggak punya x: nama berkasnya kelihatan,",
                    "    tapi isinya nggak bisa dibuka.",
                    "  - Folder yang punya x tapi nggak punya r: daftar isinya nggak bisa",
                    "    dilihat, tapi berkas yang namanya udah kamu tahu tetap bisa dibuka.",
                    "",
                    "Untuk melihat izin folder itu sendiri, bukan izin isinya, pakai ls -ld:",
                    "  ls -ld arsip",
                    "",
                    "Perintah stat menampilkan hal yang sama dengan lebih ringkas:",
                    "  stat -c '%a %A %n' arsip",
                    "",
                    "Cara pakai stat di atas berlaku di GNU/Linux. Di macOS opsinya beda,",
                    "tapi ls -l sama aja di mana-mana.",
                    "",
                    "Ada tiga jebakan yang biasanya baru ketahuan waktu kamu kena sendiri:",
                    "  1. Yang dipakai adalah golongan pertama yang cocok denganmu, walaupun",
                    "     golongan lain lebih longgar. Misalnya berkas milikmu berizin",
                    "     ----rwxrwx (77). Seisi mesin boleh membacanya, kecuali kamu. Kamu",
                    "     pemiliknya, jadi yang berlaku cuma tiga huruf pertama, dan tiga",
                    "     huruf itu kosong.",
                    "  2. Izin menghapus berkas ditentukan oleh foldernya, bukan oleh berkas",
                    "     itu sendiri. Berkas berizin r-------- pun tetap bisa kamu hapus",
                    "     kalau kamu boleh menulis di foldernya. rm cuma nanya 'remove",
                    "     write-protected regular file?', lalu nurut begitu kamu jawab y.",
                    "  3. Bit x di berkas cuma menentukan boleh-nggaknya berkas itu",
                    "     dijalankan langsung. Tanpa x, kamu masih bisa menjalankannya lewat",
                    "     'bash sapa.sh'. Yang dijalankan di situ adalah bash, dan bash cuma",
                    "     perlu membaca berkasnya. Ini juga yang menjelaskan dua cara",
                    "     menjalankan script di materi Pengenalan Shell & Bash.",
                ],
            },
            {
                "heading": "Melihat dan mengubah izin",
                "code": """#!/usr/bin/env bash
# Semua percobaan dikerjakan di folder sendiri, dan folder itu dihapus lagi
# di baris terakhir supaya folder kerjamu tetap bersih.
mkdir -p coba-izin
cd coba-izin || exit 1

echo "halo" > catatan.txt
printf '#!/usr/bin/env bash\\necho "  (sapa.sh berhasil dijalankan)"\\n' > sapa.sh
mkdir arsip

chmod 644 catatan.txt    # rw- r-- r--
chmod 755 sapa.sh        # rwx r-x r-x
chmod 700 arsip          # rwx --- ---

echo "== ls -l =="
ls -l

echo
echo "== stat: angka dan huruf berdampingan =="
stat -c '%a  %A  %U %G  %n' catatan.txt sapa.sh arsip

echo
echo "== bit x menentukan boleh-tidaknya dijalankan =="
./sapa.sh

chmod 644 sapa.sh
echo "setelah chmod 644: $(stat -c '%a %A' sapa.sh)"
./sapa.sh || echo "  ditolak, exit code $?  (126 = berkasnya ada, tapi tidak boleh dijalankan)"

echo
echo "== bash tetap mau membacanya, karena bit r masih menyala =="
bash sapa.sh

cd ..
rm -rf coba-izin""",
            },
            {
                "body": [
                    "Nulis sembilan huruf rwx tiap kali itu capek, jadi ada bentuk angka.",
                    "Tiap bit punya nilai:",
                    "",
                    "  r = 4      w = 2      x = 1",
                    "",
                    "Jumlahkan bit yang nyala, satu angka untuk tiap golongan. Kemungkinannya",
                    "cuma delapan:",
                    "",
                    "  0  ---  tidak boleh apa-apa       4  r--  baca saja",
                    "  1  --x  eksekusi saja             5  r-x  baca + eksekusi",
                    "  2  -w-  tulis saja                6  rw-  baca + tulis",
                    "  3  -wx  tulis + eksekusi          7  rwx  semuanya",
                    "",
                    "Tiga angka berurutan artinya pemilik, grup, lainnya. Yang sering dipakai",
                    "cuma beberapa:",
                    "",
                    "  755 = rwx r-x r-x   script & folder: semua boleh pakai, cuma pemilik ubah",
                    "  644 = rw- r-- r--   berkas biasa: semua boleh baca, cuma pemilik boleh ubah",
                    "  700 = rwx --- ---   folder pribadi: orang lain tidak bisa masuk sama sekali",
                    "  600 = rw- --- ---   berkas rahasia: cuma pemilik yang boleh membacanya",
                    "",
                    "Untuk membaca angkanya, tinggal dibalik: r-x itu 4 + 0 + 1 = 5.",
                    "",
                    "Selain angka, ada bentuk simbolik. Di sini kamu nyebut siapa yang diubah",
                    "dan operasinya:",
                    "",
                    "  siapa    : u pemilik, g grup, o lainnya, a semua",
                    "  operasi  : + tambah, - cabut, = pasang persis (sisanya dimatikan)",
                    "",
                    "  chmod u+x sapa.sh      nyalakan x untuk pemilik saja",
                    "  chmod go-r rahasia     cabut r dari grup dan lainnya",
                    "  chmod a+r bacaan.txt   semua orang boleh baca",
                    "  chmod u=rw,go= data    pemilik rw, grup dan lainnya kosong (= 600)",
                    "",
                    "Kapan pakai yang mana?",
                    "  - Pakai angka kalau kamu mau memastikan keadaan akhirnya. 644 selalu",
                    "    berarti 644, apa pun izin sebelumnya. Bentuk ini yang dipakai di",
                    "    dalam script.",
                    "  - Pakai simbolik kalau kamu cuma mau mengubah satu bit dan membiarkan",
                    "    sisanya.",
                    "",
                    "Jebakan: chmod +x tanpa nyebut siapa itu nggak sama dengan chmod a+x.",
                    "Kalau \"siapa\" nggak ditulis, chmod menyaringnya dulu pakai umask kamu.",
                    "umask dibahas di bagian berikutnya.",
                    "",
                    "  umask 022, berkas 644  ->  chmod +x  ->  755",
                    "  umask 077, berkas 644  ->  chmod +x  ->  744",
                    "",
                    "Di baris kedua, grup dan lainnya nggak kebagian x.",
                    "",
                    "Dari sinilah sering muncul script yang jalan di mesinmu, tapi di mesin",
                    "lain kena 'Permission denied'. Kalau memang mau semua orang bisa",
                    "menjalankannya, tulis chmod a+x atau chmod 755. Jangan bergantung pada",
                    "umask yang kebetulan pas.",
                ],
            },
            {
                "heading": "umask, berkas rahasia, dan cek root",
                "body": [
                    "Izin berkas baru itu ada asalnya. Ada saringan yang namanya umask.",
                    "  - Berkas baru berangkat dari 666 (rw-rw-rw-), folder baru dari 777",
                    "    (rwxrwxrwx).",
                    "  - Lalu bit yang tercantum di umask dimatikan.",
                    "  - Berkas baru nggak pernah lahir dengan bit x. Makanya script baru",
                    "    selalu perlu satu kali chmod +x sebelum bisa dipanggil dengan ./",
                    "",
                    "Cara melihat dan mengubahnya:",
                    "",
                    "  umask         lihat nilai sekarang, misalnya 0022",
                    "  umask 077     ubah, berlaku sampai shell ditutup",
                    "",
                    "Hati-hati: umask itu operasi bit, bukan pengurangan. Untuk 022 hasilnya",
                    "kebetulan sama dengan pengurangan (666 - 022 = 644), jadi banyak orang",
                    "ngira rumusnya memang dikurangi. Coba umask 023. Hasilnya 644, bukan",
                    "643. Angka 3 di umask artinya w dan x dimatikan. Golongan lainnya",
                    "tadinya rw- (6), w-nya dimatikan jadi r-- (4), dan x memang udah mati",
                    "dari awal. Jadi pegang cara kerjanya, yaitu bit yang ada di umask",
                    "dimatikan, dan lupakan rumus pengurangan.",
                    "",
                    "Baris if [[ ... ]] di contoh berikut dibahas lengkap di materi",
                    "Percabangan. Untuk sekarang, baca aja sebagai \"kalau ... maka ...\".",
                ],
                "code": """#!/usr/bin/env bash
# umask, berkas rahasia, dan pola cek root.
mkdir -p coba-umask
cd coba-umask || exit 1

# umask = daftar bit yang DIMATIKAN saat sesuatu yang baru dibuat.
umask 022
echo "isi rahasia" > kunci_a.txt
mkdir map_a

umask 077
echo "isi rahasia" > kunci_b.txt
mkdir map_b

echo "umask 022 -> berkas $(stat -c %a kunci_a.txt), folder $(stat -c %a map_a)"
echo "umask 077 -> berkas $(stat -c %a kunci_b.txt), folder $(stat -c %a map_b)"

# Berkas rahasia: cabut hak grup dan lainnya sampai habis.
chmod 600 kunci_a.txt
stat -c 'kunci_a.txt: %a %A  pemilik=%U grup=%G' kunci_a.txt

# Pola cek root di kepala script yang memang butuh hak penuh.
if [[ $EUID -ne 0 ]]; then
    echo "Bukan root. EUID=$EUID, id -u=$(id -u), whoami=$(whoami)"
    echo "Di script sungguhan, baris berikutnya adalah: exit 1"
fi

cd ..
rm -rf coba-umask""",
            },
            {
                "body": [
                    "Untuk kunci SSH, izin 600 itu wajib. ssh menolak jalan kalau kunci",
                    "privatmu terlalu longgar. Kalau kuncinya berizin 644, yang muncul",
                    "begini:",
                    "",
                    "  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                    "  @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @",
                    "  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                    "  Permissions 0644 for 'id_ed25519' are too open.",
                    "  This private key will be ignored.",
                    "  git@github.com: Permission denied (publickey).",
                    "",
                    "Lihat baris terakhirnya. Yang tersisa cuma 'Permission denied', sama",
                    "persis dengan pesan kalau kuncinya salah atau belum didaftarkan. Banyak",
                    "orang lalu bikin ulang kuncinya, padahal obatnya cuma dua perintah:",
                    "",
                    "  chmod 700 ~/.ssh",
                    "  chmod 600 ~/.ssh/id_ed25519",
                    "",
                    "Aturan yang sama berlaku untuk berkas .env, token API, dan berkas",
                    "konfigurasi yang berisi password. Alasannya praktis: banyak program",
                    "menolak memakai berkas rahasia yang bisa dibaca semua orang.",
                    "",
                    "sudo menjalankan satu perintah sebagai pengguna lain. Kalau penggunanya",
                    "nggak disebut, bawaannya root, yaitu akun admin yang boleh melakukan apa",
                    "aja:",
                    "",
                    "  sudo dnf install git       jalankan perintah itu sebagai root",
                    "  sudo -u postgres psql      jalankan sebagai pengguna postgres",
                    "  sudo -i                    buka shell root sampai kamu ketik exit",
                    "",
                    "Root bisa menembus semua bit rwx, dan nggak ada berkas yang bisa",
                    "menolaknya. Makanya menjalankan script orang lain sebagai root sama aja",
                    "dengan nyerahin seluruh mesin ke penulis script itu. Apalagi pola",
                    "'curl <alamat> | sudo bash', karena script-nya langsung jalan tanpa",
                    "sempat kamu baca satu baris pun. Unduh dulu ke berkas, baca isinya, baru",
                    "jalankan. Dan jangan pakai sudo kalau memang nggak perlu.",
                    "",
                    "chown dan chgrp mengubah siapa pemilik berkasnya. Izinnya nggak",
                    "disentuh:",
                    "",
                    "  sudo chown andi berkas.txt       ganti pemilik",
                    "  sudo chown andi:tim berkas.txt   ganti pemilik dan grup sekaligus",
                    "  sudo chgrp tim berkas.txt        ganti grup saja",
                    "  sudo chown -R andi:tim folder/   -R = seluruh isi folder ikut",
                    "",
                    "Menyerahkan berkas ke orang lain hampir selalu butuh root. Jadi kalau",
                    "chown kena 'Operation not permitted', itu memang aturannya, bukan bug.",
                    "",
                    "Jebakan yang paling sering bikin orang bingung:",
                    "",
                    "  $ sudo echo '127.0.0.1 lokal' > /etc/hosts",
                    "  bash: /etc/hosts: Permission denied",
                    "",
                    "Udah pakai sudo, kok masih ditolak? Soalnya tanda > dikerjakan oleh",
                    "shell-mu sendiri, sebelum sudo sempat jalan. Yang naik jadi root cuma",
                    "echo. Berkas /etc/hosts udah telanjur dibuka atas namamu, dan gagal di",
                    "situ. Cara mengatasinya dibahas di materi Aliran Data & Deskriptor.",
                    "",
                    "Beberapa jebakan lain yang perlu kamu ingat:",
                    "  - chmod -R 777 biar \"kelar dulu\" artinya siapa pun boleh menulis ulang",
                    "    programmu. Di folder web, itu sama aja dengan mempersilakan orang",
                    "    naruh kodenya di situ.",
                    "  - 777 hampir nggak pernah jadi jawaban yang benar. Cari golongan mana",
                    "    yang memang kurang izinnya, lalu kasih izin ke golongan itu aja.",
                    "  - cp tanpa -p bikin salinan dengan izin baru yang disaring umask, bukan",
                    "    izin aslinya. Salinan dari berkas 755 bisa jadi 700.",
                    "  - Cek root satu baris yang sering ada di kepala script:",
                    "      [[ $EUID -ne 0 ]] && { echo \"jalankan sebagai root\" >&2; exit 1; }",
                    "    Bentuk yang lebih portabel, artinya nggak bergantung pada fitur",
                    "    bash, memakai id -u: [[ \"$(id -u)\" -ne 0 ]]. $EUID itu fitur bash,",
                    "    sedangkan id -u ada di semua shell.",
                ],
            },
        ],
    },
    {
        "title": "3. Variabel & Quoting",
        "sections": [
            {
                "body": [
                    "Variabel adalah nama untuk menyimpan sebuah nilai. Bikinnya gampang:",
                    "tulis namanya, tanda sama dengan, lalu isinya.",
                    "  nama=\"Andi\"",
                    "",
                    "Aturan ini yang paling sering bikin error: nggak boleh ada spasi di",
                    "sekitar tanda sama dengan.",
                    "  nama=\"Andi\"     BENAR",
                    "  nama = \"Andi\"   SALAH -> bash mengira 'nama' adalah perintah",
                    "",
                    "Kalau ada spasinya, bash ngira nama itu sebuah perintah, lalu nyoba",
                    "menjalankannya dengan = dan \"Andi\" sebagai argumennya.",
                    "",
                    "Untuk membaca isi variabel, pakai tanda dolar:",
                    "  echo $nama",
                    "  echo ${nama}     <- bentuk aman, dipakai kalau menempel teks lain",
                    "",
                    "Kurung kurawal di ${nama} gunanya menandai di mana nama variabelnya",
                    "selesai. Bedanya kelihatan waktu variabel ditempel ke teks lain:",
                    "  echo \"$namaku\"    -> bash cari variabel bernama 'namaku'",
                    "  echo \"${nama}ku\"  -> bash cari 'nama', lalu tempel 'ku'",
                    "",
                    "Bash nggak punya tipe data. Semua nilai disimpan sebagai string, yaitu",
                    "teks. Angka 5 pun buat bash cuma teks \"5\".",
                ]
            },
            {
                "heading": "Tiga jenis tanda kutip",
                "code": """nama="Andi"

echo "Halo $nama"     # Halo Andi     -> variabel DIPROSES
echo 'Halo $nama'     # Halo $nama    -> semua apa adanya
echo Halo $nama       # Halo Andi     -> jalan, tapi rawan

# Backtick / $() menjalankan perintah lalu ambil hasilnya
sekarang=$(date +%Y)
echo "Tahun sekarang: $sekarang" """
            },
            {
                "body": [
                    "Ringkasan tanda kutip, atau quoting:",
                    "",
                    "  \"petik ganda\"  -> variabel & $(...) diproses. INI YANG UMUM.",
                    "  'petik tunggal' -> semua literal, tidak ada yang diproses.",
                    "  $(perintah)     -> command substitution, ambil output perintah.",
                    "  $'...'          -> ANSI-C quoting: \\n, \\t, \\e jadi karakter ASLI.",
                    "",
                    "Command substitution artinya bash menjalankan perintah di dalam $( ),",
                    "lalu keluarannya dipakai sebagai teks di tempat itu.",
                    "",
                    "Bentuk keempat paling gampang salah dibaca, justru oleh orang yang udah",
                    "hafal \"petik tunggal berarti apa adanya\". Tanda dolar di depannya",
                    "mengubah aturan itu, khusus untuk escape. Escape itu kode pendek",
                    "berawalan backslash untuk karakter yang susah diketik, misalnya \\n untuk",
                    "baris baru dan \\t untuk tab:",
                    "",
                    "  echo 'a\\nb'    -> a\\nb       petik tunggal biasa, apa adanya",
                    "  echo $'a\\nb'   -> a          lalu b di baris berikutnya",
                    "",
                    "Bentuk ini dipakai kalau kamu butuh tab atau baris baru sebagai isi",
                    "variabel, bukan teks yang kebetulan berisi backslash:",
                    "  pemisah=$'\\t'          satu karakter tab sungguhan",
                    "  printf $'\\e[31m'       \\e = karakter escape, ini awalan kode warna",
                    "",
                    "Aturan yang paling penting di materi ini: selalu bungkus variabel dengan",
                    "petik ganda.",
                    "  file=\"laporan akhir.txt\"",
                    "  rm $file      -> SALAH, dibaca sebagai 2 file: 'laporan' & 'akhir.txt'",
                    "  rm \"$file\"    -> BENAR, dibaca sebagai 1 nama file",
                    "",
                    "Tanpa petik, bash memecah isi variabel di setiap spasi. Jadi rm yang",
                    "pertama mencoba menghapus dua berkas, laporan dan akhir.txt.",
                    "",
                    "Bash juga punya variabel khusus yang isinya diisi sendiri:",
                    "  $0    nama script",
                    "  $1..$9  argumen ke-1 sampai ke-9",
                    "  $#    jumlah argumen",
                    "  $@    semua argumen (sebagai daftar terpisah)",
                    "  $?    kode keluar perintah terakhir (0 = sukses)",
                    "  $$    process ID script ini",
                    "",
                    "Process ID (PID) adalah nomor yang dikasih sistem ke tiap program yang",
                    "sedang jalan.",
                    "",
                    "Lalu ada variabel lingkungan (environment). Variabel ini ikut diwariskan",
                    "ke program lain yang kamu jalankan dari shell, yang disebut proses anak.",
                    "Beberapa udah ada dari awal, misalnya HOME, USER, dan PATH. Variabel",
                    "buatanmu sendiri baru ikut diwariskan kalau di-export:",
                    "  echo $HOME $USER $PATH",
                    "  export API_KEY=\"rahasia\"   # supaya diwariskan ke proses anak",
                ]
            },
            {
                "heading": "$( ) membuka konteks kutip BARU",
                "body": [
                    "Apa pun yang ada di dalam $( ) dibaca dari nol, terpisah dari yang di",
                    "luarnya. Petik ganda di dalamnya nggak menutup petik ganda di luarnya.",
                    "Dua-duanya nggak saling kenal.",
                    "",
                    "  echo \"Total: $(wc -l < \"$BERKAS\") baris\"",
                    "",
                    "Petik di sekitar $BERKAS itu benar dan memang harus ada. Sekilas, bagian",
                    "\"Total: $(wc -l < \" kelihatan seperti udah menutup petiknya, jadi ada",
                    "orang yang menghapus petik di dalam supaya kelihatan rapi. Akibatnya",
                    "nama berkas yang ada spasinya nggak terlindungi lagi. Itu persis aturan",
                    "petik ganda yang baru kamu pelajari di atas.",
                    "",
                    "Aturan ini berlaku bertingkat: $( ) di dalam $( ) juga membuka",
                    "konteksnya sendiri lagi.",
                    "",
                    "Satu lagi soal contoh $(date +%Y) tadi. Tanda + di situ bukan opsi dan",
                    "bukan bagian nama perintah. Tanda itu menandai bahwa sisanya adalah",
                    "string format, yaitu pola tampilan tanggal. %Y artinya tahun empat",
                    "digit. Daftar lengkap formatnya ada di materi Alat Pendamping: curl, jq,",
                    "date, tar.",
                ]
            },
            {
                "heading": "IFS dan awalan variabel sekali pakai",
                "body": [
                    "IFS (Internal Field Separator) itu variabel biasa, bukan perintah",
                    "khusus. Isinya daftar karakter yang dipakai bash sebagai pemisah kata.",
                    "Bawaannya spasi, tab, dan baris baru. Makanya bash memecah kata di",
                    "spasi.",
                    "",
                    "  IFS=','    -> yang dianggap pemisah tinggal koma",
                    "  IFS=       -> daftarnya KOSONG, tidak ada yang dipecah sama sekali",
                    "",
                    "Dua bentuk itu kelihatan mirip, padahal artinya berlawanan. Yang pertama",
                    "mengganti daftar pemisah, yang kedua mengosongkannya. Nanti kamu bakal",
                    "ketemu dua-duanya di tempat yang berbeda. Bedanya cuma ada atau nggaknya",
                    "isi di sebelah kanan tanda sama dengan.",
                    "",
                    "Ada juga yang namanya awalan variabel. Kalau pemberian nilai ke variabel",
                    "ditulis di depan sebuah perintah, variabel itu cuma hidup selama",
                    "perintah itu berjalan:",
                    "",
                    "  LC_ALL=C sort daftar.txt     sort diurut aturan C, shell tak berubah",
                    "  DEBUG=1 ./app.sh             app melihat DEBUG=1, terminalmu tidak",
                    "  IFS=',' read -ra bagian      IFS koma cuma untuk read yang ini",
                    "",
                    "Begitu perintahnya selesai, nilai lama balik sendiri, jadi nggak perlu",
                    "dipulihkan. Karena itu bentuk IFS=',' read ... aman ditaruh di tengah",
                    "script tanpa merusak apa pun sesudahnya.",
                    "",
                    "Kalau IFS harus berubah untuk beberapa perintah sekaligus, awalan nggak",
                    "bisa dipakai. Simpan nilai lamanya, lalu pulihkan sendiri:",
                    "",
                    "  LAMA=$IFS",
                    "  IFS=:",
                    "  ...beberapa perintah...",
                    "  IFS=$LAMA",
                ]
            },
        ],
    },
    {
        "title": "4. Input & Output",
        "sections": [
            {
                "body": [
                    "Untuk menampilkan output, alias keluaran, ada beberapa cara:",
                    "  echo \"teks\"           paling umum",
                    "  echo -n \"teks\"        tanpa pindah baris di akhir",
                    "  echo -e \"a\\tb\"        aktifkan escape seperti \\t dan \\n",
                    "  printf \"%s\\n\" \"teks\"  lebih presisi, mirip C",
                    "",
                    "printf lebih bisa diandalkan daripada echo -e, karena perilakunya sama",
                    "di semua shell.",
                    "",
                    "Format printf yang sering dipakai:",
                    "  %s    string",
                    "  %d    bilangan bulat",
                    "  %.2f  desimal 2 angka di belakang koma",
                    "  \\n    baris baru",
                    "  \\t    tab",
                    "",
                    "Angka di antara % dan hurufnya mengatur lebar kolom:",
                    "  %5d    lebar 5, rata KANAN            ->  '   42'",
                    "  %-5d   tanda minus = rata KIRI        ->  '42   '",
                    "  %-25s  teks rata kiri selebar 25 kolom",
                    "  %03d   lebar 3, sisanya diisi NOL     ->  '007'",
                    "",
                    "Isi yang lebih panjang dari lebar yang diminta nggak dipotong. Kolomnya",
                    "yang melar. Jadi lebar itu jaminan minimal, bukan batas.",
                    "",
                    "Dengan cara ini kamu bisa bikin tabel yang lurus tanpa ngitung spasi",
                    "sendiri:",
                    "  printf \"%-10s %5d\\n\" \"apel\" 12",
                    "  printf \"%-10s %5d\\n\" \"semangka\" 3",
                    "",
                    "Hasilnya:",
                    "",
                    "  apel          12",
                    "  semangka       3",
                    "",
                    "Kalau spasinya diitung manual, nama yang nambah satu huruf aja udah",
                    "cukup buat merusak seluruh kolom.",
                ]
            },
            {
                "heading": "printf mengulang formatnya sampai argumen habis",
                "body": [
                    "Sifat printf yang satu ini paling sering bikin heran. Kalau argumennya",
                    "lebih banyak daripada spesifier %, yaitu kode format seperti %s atau %d,",
                    "printf nggak membuang sisanya. Dia memakai formatnya lagi dari awal",
                    "sampai semua argumen terpakai.",
                    "",
                    "  printf '%s\\n' apel jeruk mangga",
                    "",
                    "Satu %s dengan tiga argumen hasilnya tiga baris: apel, jeruk, dan",
                    "mangga. Makanya printf '%s\\n' jadi cara baku untuk mencetak daftar apa",
                    "pun satu per baris, termasuk seluruh isi array nanti.",
                    "",
                    "Kalau formatnya punya dua spesifier, argumennya diambil dua-dua tiap",
                    "putaran. Satu putaran jadi satu baris tabel.",
                    "",
                    "Kalau argumennya malah kurang, yang kosong dianggap string kosong atau",
                    "angka 0, dan printf nggak ngeluh.",
                ],
                "code": """#!/usr/bin/env bash

# Satu spesifier, banyak argumen: formatnya dipakai berulang.
printf '%s\\n' apel jeruk mangga

echo "---"

# Dua spesifier: printf mengambil argumen DUA-DUA tiap putaran.
printf '%-10s %5d\\n' apel 12 semangka 3 jeruk 108

echo "---"

# Lebar dan perataan bikin kolom lurus tanpa menghitung spasi.
printf '%-10s|\\n' "kiri"
printf '%10s|\\n'  "kanan"
printf '%03d\\n'   7"""
            },
            {
                "heading": "Membaca input dari user",
                "code": """#!/usr/bin/env bash

read -p "Siapa namamu? " nama
echo "Halo, $nama!"

# -s menyembunyikan ketikan, cocok untuk password
read -s -p "Password: " sandi
echo
echo "Panjang password: ${#sandi} karakter"

# Membaca beberapa nilai sekaligus
read -p "Masukkan 2 angka: " a b
echo "Jumlah: $((a + b))" """
            },
            {
                "body": [
                    "Ada dua bentuk di contoh tadi yang belum waktunya dibahas. Nggak usah",
                    "dipikirin dulu, dua-duanya dijelasin lengkap nanti:",
                    "  ${#sandi}     panjang sebuah string. Lihat materi Operasi String.",
                    "  $((a + b))    hitungan angka. Lihat materi Aritmatika & Angka.",
                    "",
                    "Opsi read yang berguna:",
                    "  -p \"teks\"   tampilkan prompt lebih dulu",
                    "  -s          silent, ketikan tidak terlihat",
                    "  -r          jangan proses backslash (SELALU pakai ini)",
                    "  -a arr      simpan hasil ke array",
                    "  -t 5        batas waktu 5 detik",
                    "",
                    "Prompt itu teks pertanyaan yang muncul sebelum pengguna ngetik.",
                    "",
                    "Redirection artinya mengalihkan dari mana input diambil dan ke mana",
                    "output dikirim:",
                    "  perintah > file     tulis output ke file (TIMPA isi lama)",
                    "  perintah >> file    tambahkan output ke akhir file",
                    "  perintah < file     ambil input dari file",
                    "  perintah 2> file    alihkan pesan error saja",
                    "  perintah &> file    alihkan output DAN error",
                    "  perintah > /dev/null  buang output (tempat sampah sistem)",
                    "",
                    "Pipe (tanda |) menyambung output satu perintah jadi input perintah",
                    "berikutnya:",
                    "  cat data.txt | grep \"error\" | wc -l",
                    "",
                    "Artinya: baca berkasnya, saring baris yang mengandung 'error', lalu",
                    "hitung berapa barisnya.",
                ]
            },
        ],
    },
    {
        "title": "5. Aliran Data & Deskriptor",
        "sections": [
            {
                "body": [
                    "Setiap perintah yang jalan di Linux lahir dengan tiga saluran yang udah",
                    "terbuka. Ini aturan sistem operasinya, jadi berlaku juga di luar bash:",
                    "untuk python, java, curl, dan program apa pun yang kamu panggil dari",
                    "script.",
                    "",
                    "  Nomor  Nama     Arah     Isinya",
                    "  0      stdin    masuk    data yang dibaca perintah",
                    "  1      stdout   keluar   hasil kerja yang sebenarnya",
                    "  2      stderr   keluar   pesan error dan peringatan",
                    "",
                    "Angka di kolom pertama itu namanya file descriptor. Di sini kita sebut",
                    "deskriptor aja. Deskriptor adalah nomor yang dipakai program untuk",
                    "menunjuk saluran yang terbuka. Kernel nggak kenal kata 'stdout'. Yang",
                    "dia pegang cuma angka 1.",
                    "",
                    "Keluaran dipecah jadi dua jalur supaya hasil kerja bisa disaring lewat",
                    "pipe tanpa kecampur pesan error. Itu alasan di balik echo \"...\" >&2 yang",
                    "dipakai di materi Argumen & Exit Code.",
                    "",
                    "Redirection yang udah kamu kenal ternyata cuma bentuk singkat:",
                    "",
                    "  perintah > berkas     sama saja dengan   perintah 1> berkas",
                    "  perintah < berkas     sama saja dengan   perintah 0< berkas",
                    "  perintah 2> berkas    alihkan stderr saja, hasil tetap ke layar",
                    "",
                    "Angka 1 dan 0 boleh nggak ditulis, karena dua itu yang paling sering",
                    "dipakai. Angka 2 nggak punya bentuk singkat, jadi harus ditulis.",
                    "",
                    "Cara membaca N>&M: \"sambungkan deskriptor N ke tempat yang sekarang",
                    "ditunjuk deskriptor M\". Tanda & di situ artinya yang ada sesudahnya",
                    "adalah nomor deskriptor, bukan nama berkas.",
                    "",
                    "  2>&1    stderr ikut ke mana pun stdout sedang mengarah",
                    "  2>1     SALAH - membuat berkas bernama 1, lalu menaruh pesan error di sana",
                    "",
                    "Salah ketik 2>1 nggak ngasih peringatan apa pun. Script tetap jalan,",
                    "pesan error-nya hilang, dan di folder muncul berkas aneh bernama 1.",
                    "Kalau kamu pernah lihat berkas bernama 1 di server, sekarang kamu tahu",
                    "asalnya.",
                    "",
                    "Jebakan: redirection dikerjakan urut dari kiri ke kanan. Waktu 2>&1",
                    "dikerjakan, dia menyalin tujuan stdout saat itu juga. Kalau stdout",
                    "dipindah belakangan, stderr nggak ikut pindah. Bandingkan dua baris",
                    "ini:",
                    "",
                    "  perintah >catatan.log 2>&1",
                    "",
                    "Di sini 1 dipindah ke berkas dulu, baru 2 menyusul ke tempat yang sama.",
                    "Dua-duanya masuk berkas, dan biasanya memang ini yang kamu mau.",
                    "",
                    "  perintah 2>&1 >catatan.log",
                    "",
                    "Di sini 2 disambungkan ke layar dulu, karena waktu itu 1 masih menunjuk",
                    "ke layar. Sesudah itu baru 1 pindah ke berkas. Akibatnya error tetap",
                    "muncul di layar. Ini bug yang sering banget kejadian: lognya kelihatan",
                    "bersih, padahal error-nya cuma nggak tercatat.",
                    "",
                    "Satu catatan sebelum kamu coba contoh di bawah. Di aplikasi ini,",
                    "keluaran stderr ditampilkan di panel yang terpisah dari keluaran biasa,",
                    "jadi urutan barisnya bisa kelihatan beda dari di terminal. Itu bukan",
                    "tanda gagal. Malah itu bukti bahwa ada dua aliran yang ditampung di dua",
                    "tempat.",
                ],
            },
            {
                "heading": "Membuktikan sendiri, bukan menghafal",
                "code": """#!/usr/bin/env bash

dua_aliran() {
    echo "ini hasil kerja"        # lewat stdout, deskriptor 1
    echo "ini pesan error" >&2    # lewat stderr, deskriptor 2
}

echo "== apa adanya: dua-duanya sampai ke layar =="
dua_aliran

echo
echo "== stdout dibuang, error tetap terlihat =="
dua_aliran >/dev/null

echo
echo "== error dibuang, hasil tetap terlihat =="
dua_aliran 2>/dev/null

echo
echo "== urutan BENAR: >berkas dulu, baru 2>&1 =="
dua_aliran >kumpul.log 2>&1
cat kumpul.log

echo
echo "== urutan TERBALIK: 2>&1 dulu, baru >berkas =="
dua_aliran 2>&1 >bocor.log
echo "-- isi bocor.log ternyata cuma ini: --"
cat bocor.log

rm -f kumpul.log bocor.log""",
            },
            {
                "body": [
                    "Pola yang paling sering kamu temui di script orang lain:",
                    "",
                    "  perintah >/dev/null 2>&1    diamkan semuanya, hasil maupun error",
                    "  perintah 2>/dev/null        diamkan errornya saja, hasil tetap terlihat",
                    "",
                    "/dev/null adalah berkas khusus yang menelan apa pun yang ditulis ke",
                    "sana. Bentuk pendek &>/dev/null dari materi Input & Output hasilnya sama",
                    "persis, tapi &> cuma dimengerti bash dan zsh. Kalau baris pertama",
                    "script-mu #!/bin/sh, tulis >/dev/null 2>&1. Bentuk itu jalan di mana",
                    "pun.",
                    "",
                    "Sekarang exec. Kalau exec dipakai tanpa nama perintah, yang dialihkan",
                    "adalah aliran script itu sendiri, dan berlaku terus sampai script",
                    "selesai:",
                    "",
                    "  exec >>\"$LOG\" 2>&1",
                    "",
                    "Baris ini ditaruh di kepala script. Sesudahnya, semua echo, semua pesan",
                    "error, dan keluaran semua perintah yang dipanggil masuk ke berkas log.",
                    "Tanpa exec, kamu harus nempelin >>\"$LOG\" 2>&1 di tiap baris, dan satu",
                    "baris yang kelupaan udah cukup bikin log-nya bolong.",
                    "",
                    "Sesudah exec >>\"$LOG\", layar nggak bisa dipanggil balik begitu aja.",
                    "Kalau masih butuh, simpan dulu tujuan lamanya di deskriptor cadangan:",
                    "",
                    "  exec 4>&1        salin tujuan stdout sekarang ke deskriptor 4",
                    "  exec >&4         kembalikan stdout ke tempat yang tadi disimpan",
                    "  exec 4>&-        tutup deskriptor 4, tanda minus artinya 'tutup'",
                    "",
                    "Deskriptor 3 ke atas bebas kamu pakai. 0, 1, dan 2 udah ada pemiliknya.",
                    "  exec 3<data.txt   buka data.txt untuk dibaca lewat deskriptor 3",
                    "  read -r baris <&3 baca satu baris dari deskriptor 3, bukan dari stdin",
                    "  exec 3<&-         tutup lagi",
                    "",
                    "Gunanya buat perulangan yang membaca berkas, tapi di dalamnya masih",
                    "perlu nanya ke pengguna. Kalau berkasnya disambungkan ke stdin biasa,",
                    "read yang di dalam loop bakal ikut makan baris berkas, bukan jawaban",
                    "orangnya.",
                    "",
                    "Kalau exec dipakai dengan nama perintah, artinya lain lagi. Script",
                    "mengganti dirinya sendiri dengan perintah itu. Prosesnya tetap sama,",
                    "PID-nya juga sama, dan nggak ada proses anak.",
                    "",
                    "  exec \"$@\"",
                    "",
                    "Ini baris penutup entrypoint.sh di hampir semua image Docker. Script itu",
                    "nyiapin konfigurasi, lalu hilang dan digantikan aplikasi aslinya. Karena",
                    "PID-nya nggak berubah, sinyal stop dari Docker sampai ke aplikasi, dan",
                    "nggak nyangkut di script pembungkus.",
                    "",
                    "tee membelah satu keluaran jadi dua tujuan, layar dan berkas:",
                    "  perintah | tee catatan.log      timpa isi lama",
                    "  perintah | tee -a catatan.log   tambahkan di belakang (append)",
                    "",
                    "tee juga jalan keluar dari jebakan sudo di materi Izin Berkas. Pada sudo",
                    "perintah > /etc/x, yang dijalankan sebagai root cuma 'perintah'.",
                    "Pengalihan > dikerjakan shell-mu yang biasa, jadi tetap ditolak. Yang",
                    "benar begini:",
                    "  echo \"isi baru\" | sudo tee /etc/contoh.conf >/dev/null",
                    "",
                    "Di sini yang jalan sebagai root adalah tee, jadi dia berhak menulis ke",
                    "berkas itu.",
                ],
            },
            {
                "heading": "exec, tee, dan deskriptor tambahan",
                "code": """#!/usr/bin/env bash
set -euo pipefail

LOG="jalan.log"

# tee: satu keluaran, dua tujuan -- layar DAN berkas.
echo "mulai memproses" | tee "$LOG"
echo "sedang bekerja"  | tee -a "$LOG"

# Simpan layar aslinya di deskriptor 4 supaya bisa dipakai lagi nanti.
exec 4>&1

# Sejak baris ini SEMUA keluaran pindah ke log. Tidak perlu >>log lagi.
exec >>"$LOG" 2>&1
echo "baris ini masuk log, bukan layar"
echo "pesan error pun ikut masuk log" >&2

# Sambungkan lagi stdout ke layar yang tadi disimpan, lalu tutup fd 4.
exec >&4 2>&1
exec 4>&-

echo
echo "== isi $LOG =="
cat "$LOG"

# Deskriptor 3 untuk membaca berkas sedikit demi sedikit.
printf 'anggur\\nmangga\\n' > buah.txt
exec 3< buah.txt
read -r satu <&3
read -r dua <&3
exec 3<&-
echo
echo "dibaca lewat fd 3: $satu lalu $dua"

rm -f "$LOG" buah.txt""",
            },
            {
                "body": [
                    "Ada tiga jalan pintas yang udah dipakai di materi lain tanpa dijelasin.",
                    "Sekarang kita bahas asalnya.",
                    "",
                    "Yang pertama, here-string <<<. Tanda ini memberi satu string sebagai",
                    "stdin sebuah perintah:",
                    "",
                    "  read -ra bagian <<< \"$teks\"   pecah string jadi array",
                    "  grep -q pola <<< \"$teks\"      periksa isi string tanpa berkas sementara",
                    "  jq . <<< \"$json\"              suapkan JSON yang sudah ada di variabel",
                    "",
                    "Tanpa <<<, kamu mungkin nulis echo \"$teks\" | read ..., dan itu nggak",
                    "jalan. Sisi kanan pipe dijalankan di proses terpisah, jadi variabel yang",
                    "diisi read di sana ikut hilang begitu pipe selesai. <<< nggak bikin",
                    "proses baru, makanya variabelnya tetap ada.",
                    "",
                    "Satu hal kecil: <<< menambahkan satu baris baru di ujung string.",
                    "",
                    "Bedanya dengan heredoc << (dibahas di materi grep, sed, dan awk):",
                    "  <<< 'satu string', ditulis di baris yang sama",
                    "  <<  blok banyak baris, ditutup penanda tersendiri seperti EOF",
                    "",
                    "Yang kedua, isi=$(<berkas.txt). Bentuk ini membaca seluruh isi berkas ke",
                    "variabel. Hasilnya sama dengan $(cat berkas.txt), tapi program cat sama",
                    "sekali nggak dijalankan, karena bash membaca berkasnya sendiri.",
                    "Dua-duanya membuang baris baru di ujung berkas, jadi jangan kaget kalau",
                    "panjangnya berkurang.",
                    "",
                    "Yang ketiga, perintah kosong, yaitu tanda titik dua (:). Perintah ini",
                    "nggak ngapa-ngapain dan selalu sukses (exit 0).",
                    "",
                    "  : > berkas            kosongkan berkas; yang bekerja tanda >, bukan :",
                    "  while :; do           sama saja dengan while true, cuma lebih pendek",
                    "  : \"${VAR:?wajib diisi}\"  hentikan script kalau VAR kosong",
                    "",
                    "Baris ketiga itu trik yang praktis. ${VAR:?pesan} sendiri udah bisa",
                    "menghentikan script, tapi dia harus jadi bagian dari sebuah perintah.",
                    "Kalau ditulis sendirian, nilainya bakal dicoba dijalankan sebagai",
                    "perintah. Makanya di depannya dikasih :, perintah yang nggak",
                    "ngapa-ngapain, sehingga yang tersisa cuma pemeriksaannya. Kalau VAR",
                    "kosong, pesannya muncul begini, lalu script berhenti:",
                    "",
                    "  coba.sh: line 4: VAR: wajib diisi        (lalu keluar dengan kode 1)",
                ],
                "code": """#!/usr/bin/env bash
set -euo pipefail

teks="andi,budi,citra"

# <<< menyodorkan SATU string sebagai stdin perintah di sebelah kirinya.
IFS=',' read -ra nama <<< "$teks"
echo "orang kedua: ${nama[1]}"

if grep -q "budi" <<< "$teks"; then
    echo "budi ada di daftar"
fi

echo "jumlah bita: $(wc -c <<< "$teks")   <- 15 huruf + 1 baris baru dari <<<"

# $(<berkas) membaca isi berkas tanpa memanggil program cat sama sekali.
printf 'baris satu\\nbaris dua\\n' > sementara.txt
isi=$(<sementara.txt)
echo "== isi berkas =="
echo "$isi"

# : tidak mengerjakan apa pun dan selalu sukses.
KONFIG="/etc/app.conf"
: "${KONFIG:?variabel KONFIG wajib diisi}"
echo "konfig dipakai: $KONFIG"

: > sementara.txt
echo "sesudah ': >' isinya tinggal $(wc -c < sementara.txt) bita"

n=0
while :; do
    n=$((n + 1))
    [[ $n -ge 3 ]] && break
done
echo "while : berhenti di n=$n"

rm -f sementara.txt""",
            },
        ],
    },
    {
        "title": "6. Proses, source, dan Subshell",
        "sections": [
            {
                "body": [
                    "Ada tiga cara menjalankan berkas .sh, dan akibatnya beda-beda:",
                    "",
                    "  bash x.sh     Bash BARU dijalankan sebagai proses anak untuk",
                    "                membaca x.sh. Tidak butuh izin eksekusi maupun",
                    "                shebang.",
                    "  ./x.sh        Sistem yang menjalankan berkasnya sendiri. Butuh",
                    "                izin x (chmod +x) DAN shebang. Tetap proses anak.",
                    "  source x.sh   TIDAK ada proses baru. Isi x.sh dibaca dan",
                    "                dijalankan oleh shell yang sedang kamu pakai,",
                    "                seolah kamu mengetiknya sendiri satu per satu.",
                    "  . x.sh        Sama persis dengan source. Titik itu memang nama",
                    "                perintahnya.",
                    "",
                    "Proses anak itu apa? Proses adalah program yang sedang jalan, dan tiap",
                    "proses punya nomor sendiri. Waktu shell menjalankan sebuah program, dia",
                    "bikin proses baru, lalu menyerahkan pekerjaannya ke proses itu. Proses",
                    "baru itulah proses anak. Nomornya yang kamu lihat lewat $$ di materi",
                    "Variabel & Quoting.",
                    "",
                    "Proses anak dapat bekal warisan dari induknya, tapi hidupnya sendiri.",
                    "Begitu dia selesai, semua yang dia ubah ikut hilang bersama prosesnya.",
                    "",
                    "Akibatnya ada tiga hal yang paling sering bikin orang bingung:",
                    "  - cd di dalam ./x.sh nggak memindahkan folder terminalmu. Yang pindah",
                    "    adalah proses anak, dan proses itu udah mati begitu script selesai.",
                    "  - Variabel yang dibuat di dalam ./x.sh udah nggak ada lagi sesudah",
                    "    script selesai.",
                    "  - Karena itu, perintah seperti \"aktifkan virtualenv\" atau \"muat ulang",
                    "    konfigurasi\" selalu dipakai dengan source. Kalau nggak, perintahnya",
                    "    nggak berpengaruh apa pun, dan dari luar kelihatannya seperti nggak",
                    "    terjadi apa-apa.",
                    "",
                    "export cuma menjawab satu pertanyaan: variabel ini ikut turun ke proses",
                    "anak atau nggak?",
                    "",
                    "  nama=\"Andi\"      hanya ada di shell ini",
                    "  export nama      ikut turun ke setiap proses anak sesudahnya",
                    "  export API=\"x\"   membuat dan menandai sekaligus",
                    "",
                    "Arahnya cuma satu: ke bawah, nggak pernah ke atas. Anak boleh mengubah",
                    "nilai warisannya sesuka hati, dan induknya nggak bakal tahu. Nggak ada",
                    "cara bikin ./x.sh mengubah variabel di terminal yang memanggilnya. Kalau",
                    "kamu memang butuh itu, jawabannya source, bukan export.",
                ],
            },
            {
                "heading": "Bukti: bash x.sh vs source x.sh",
                "body": [
                    "Berkas yang sama persis dijalankan dengan dua cara. Perhatikan isi",
                    "variabel warna dan hasil pwd.",
                ],
                "code": """#!/usr/bin/env bash
# Bedanya MENJALANKAN sebuah script dan MEN-SOURCE-nya.

cd /tmp                      # mulai dari folder yang pasti ada
mkdir -p contoh-source

# Buat satu script kecil sebagai bahan percobaan.
printf '%s\\n' 'warna="biru"' 'cd /tmp/contoh-source' > contoh-anak.sh

warna="merah"
echo "sebelum        : warna=$warna, pwd=$PWD"

bash contoh-anak.sh          # PROSES ANAK -> perubahannya ikut mati
echo "setelah bash   : warna=$warna, pwd=$PWD"

source contoh-anak.sh        # dijalankan DI SINI -> perubahannya menempel
echo "setelah source : warna=$warna, pwd=$PWD"

cd /tmp
rm -f contoh-anak.sh
rmdir contoh-source""",
            },
            {
                "heading": "Memecah proyek jadi beberapa berkas",
                "body": [
                    "Keluaran contoh di atas:",
                    "",
                    "  sebelum        : warna=merah, pwd=/tmp",
                    "  setelah bash   : warna=merah, pwd=/tmp",
                    "  setelah source : warna=biru, pwd=/tmp/contoh-source",
                    "",
                    "Baris kedua itu intinya. contoh-anak.sh udah mengubah warna dan udah",
                    "pindah folder, tapi semua itu terjadi di proses lain yang langsung mati",
                    "sesudahnya. Baris ketiga menjalankan berkas yang sama persis, dan kali",
                    "ini bekasnya tertinggal, karena nggak ada proses baru yang lahir.",
                    "",
                    "Makanya kalau proyek bash dipecah jadi beberapa berkas, berkas lain",
                    "dimuat pakai source, bukan dijalankan:",
                    "",
                    "  source lib/umum.sh    muat kumpulan fungsi buatanmu sendiri",
                    "  . lib/umum.sh         sama saja, cuma lebih pendek",
                    "  . venv/bin/activate   mengubah PATH shell-mu; wajib source,",
                    "                        dijalankan biasa jadi percuma",
                    "  . /etc/os-release     isinya baris NAME=... VERSION=...,",
                    "                        langsung jadi variabel siap pakai",
                    "  source ~/.bashrc      memuat ulang konfigurasi shell tanpa",
                    "                        perlu menutup terminal",
                    "",
                    "Titik sendirian di awal baris sering dikira salah ketik, padahal itu",
                    "perintah. '. berkas' dan 'source berkas' itu perintah yang sama. Titik",
                    "lebih tua dan lebih portabel, source lebih enak dibaca. Di kode",
                    "sungguhan kamu bakal ketemu dua-duanya, kadang di berkas yang sama.",
                    "",
                    "Berkas yang di-source nggak harus punya shebang dan nggak perlu izin",
                    "eksekusi. Berkas itu nggak pernah dijalankan sebagai program, cuma",
                    "dibaca sebagai teks perintah. Akibatnya, berkas yang kamu source bisa",
                    "ngapain aja terhadap shell-mu. Jangan pernah source berkas yang isinya",
                    "nggak kamu percayai.",
                ],
            },
            {
                "heading": "Script yang tahu foldernya sendiri",
                "body": [
                    "Script hampir selalu punya berkas pendamping, misalnya lib/umum.sh,",
                    "config, atau template. Kalau kamu nulis 'source lib/umum.sh' begitu aja,",
                    "bash nyari lib/umum.sh mulai dari folder tempat orang yang memanggil",
                    "script itu berada, bukan dari folder script-nya. Kalau script dipanggil",
                    "dari folder lain, dia langsung gagal. Pesan error-nya cuma 'No such file",
                    "or directory', yang nggak menjelaskan apa-apa.",
                    "",
                    "Jalan keluarnya satu pola yang muncul di ribuan script. Kita bedah dari",
                    "dalam ke luar:",
                    "",
                    "  ${BASH_SOURCE[0]}  jalur berkas yang isinya sedang dibaca",
                    "                     bash. BASH_SOURCE itu array (lihat materi",
                    "                     Array); [0] berarti berkas paling dalam,",
                    "                     yaitu berkas ini sendiri.",
                    "  $(dirname ...)     buang nama berkasnya, sisakan foldernya.",
                    "                     Hasilnya bisa masih relatif: '.' atau '..'.",
                    "  $(cd ... && pwd)   masuk ke folder itu lalu tanya 'sebenarnya",
                    "                     aku di mana?'. pwd selalu menjawab dengan",
                    "                     jalur ABSOLUT.",
                    "  Seluruh $( )       jalan di subshell, jadi cd di dalamnya",
                    "                     tidak ikut memindahkan script-mu. Itu yang",
                    "                     membuat idiom ini aman.",
                    "",
                    "Jalur absolut artinya jalur lengkap yang dimulai dari /, misalnya",
                    "/home/andi/proyek. Jalur relatif dihitung dari folder saat ini.",
                    "",
                    "dirname, basename, dan realpath itu program terpisah, bukan bagian dari",
                    "bahasa bash:",
                    "  dirname /home/andi/laporan.txt   -> /home/andi",
                    "  basename /home/andi/laporan.txt  -> laporan.txt",
                    "  basename laporan.txt .txt        -> laporan",
                    "  realpath ../data                 -> absolut, symlink lurus",
                    "",
                    "Nanti di materi Operasi String kamu bakal ketemu cara lain untuk dua",
                    "yang pertama: ${jalur%/*} setara dengan dirname, dan ${jalur##*/} setara",
                    "dengan basename. Bentuk ${} nggak memanggil program lain, jadi jauh",
                    "lebih cepat di dalam perulangan. dirname dan basename lebih enak dibaca",
                    "dan lebih rapi menangani kasus aneh, misalnya jalur yang sama sekali",
                    "nggak punya garis miring. Dua-duanya wajar dipakai.",
                    "",
                    "Lalu ada baris penjaga di contoh di bawah:",
                    "  if [[ \"${BASH_SOURCE[0]}\" == \"$0\" ]]; then",
                    "",
                    "Artinya: \"berkas ini sedang dijalankan langsung, nggak di-source\". Ini",
                    "padanan bash untuk if __name__ == \"__main__\" di Python. Gunanya, satu",
                    "berkas bisa jadi pustaka (di-source supaya fungsinya bisa dipakai)",
                    "sekaligus program (dijalankan langsung untuk mengerjakan sesuatu), dan",
                    "dua peran itu nggak saling ganggu.",
                    "",
                    "Kenapa nggak pakai $0 aja? Waktu sebuah berkas di-source, $0 tetap",
                    "berisi nama pemanggilnya, bukan nama berkas yang sedang dibaca. Cuma",
                    "BASH_SOURCE yang tahu berkas mana yang isinya sedang dijalankan.",
                ],
                "code": """#!/usr/bin/env bash
# Idiom SCRIPT_DIR: tetap benar dipanggil dari folder mana pun.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Berkas ini : ${BASH_SOURCE[0]}"
echo "Nama saja  : $(basename "${BASH_SOURCE[0]}")"
echo "Foldernya  : $SCRIPT_DIR"

# Penjaga: blok ini hanya jalan kalau berkas DIEKSEKUSI langsung,
# dan diam kalau berkas ini di-source oleh script lain.
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    echo "Mode       : dijalankan langsung"
else
    echo "Mode       : sedang di-source"
fi""",
            },
            {
                "heading": "Kurawal { }, kurung ( ), dan jebakan pipe",
                "body": [
                    "Dua tanda ini bentuknya mirip, tapi artinya jauh beda:",
                    "",
                    "  { perintah1; perintah2; }  kelompokkan, TETAP di shell ini",
                    "  ( perintah1; perintah2 )   kelompokkan, jalan di SUBSHELL",
                    "",
                    "Subshell itu salinan shell yang jalan sebagai proses anak. Apa pun yang",
                    "berubah di dalamnya hilang begitu subshell selesai.",
                    "",
                    "Ada dua aturan { } yang wajib kamu hafal. Kalau dilanggar, pesan",
                    "error-nya sama sekali nggak nyebut penyebabnya.",
                    "  1. Wajib ada spasi sesudah {. Kalau ditulis '{echo a; }', hasilnya",
                    "     gagal, karena '{echo' terbaca sebagai satu nama perintah.",
                    "  2. Wajib ada ; atau baris baru sebelum }. Kalau ditulis '{ echo a }',",
                    "     hasilnya gagal, karena } nggak pernah dianggap penutup.",
                    "",
                    "Yang muncul di layar biasanya 'syntax error near unexpected token }',",
                    "atau malah 'unexpected end of file'. Dua-duanya menunjuk ke tempat yang",
                    "salah. Jadi begitu lihat pesan itu, yang pertama kamu cek adalah spasi",
                    "dan titik komanya. ( ) bebas dari dua aturan ini, karena kurung udah",
                    "jadi pemisah sendiri.",
                    "",
                    "Ini yang nggak pernah bocor keluar dari ( ):",
                    "  - cd, variabel, set -x, shopt, dan umask. Semuanya balik seperti",
                    "    semula begitu kurungnya ditutup.",
                    "  - exit di dalam ( ) cuma menutup subshell-nya. Script induk jalan",
                    "    terus, dan angka exit itu jadi nilai $? sesudahnya.",
                    "  - Sebaliknya, exit di dalam { } menghentikan seluruh script.",
                    "",
                    "Ada dua pola yang bakal sering kamu temui di kode orang. Yang pertama:",
                    "",
                    "  (cd \"$dir\" && make)",
                    "",
                    "Ini menjalankan make di folder lain tanpa perlu cd balik. && bikin make",
                    "batal kalau cd gagal. Tanpa &&, make bakal jalan di folder yang salah,",
                    "dan nggak ada yang mencegahnya.",
                    "",
                    "Yang kedua:",
                    "",
                    "  perintah || { echo \"pesan\" >&2; exit 1; }",
                    "",
                    "Kalau perintah gagal, kerjakan dua hal sekaligus: cetak pesan ke",
                    "stderr, lalu keluar. Di sini harus { }, bukan ( ), karena exit-nya harus",
                    "mematikan script induknya. Bentuk ini muncul lagi di kerangka script di",
                    "materi Debugging & Praktik Baik dan di studi kasus penutup.",
                    "",
                    "Jebakan pipe: tiap sisi sebuah pipe dijalankan di subshell-nya sendiri.",
                    "Jadi 'echo halo | read -r kata' memang mengisi variabel kata, tapi di",
                    "proses sebelah yang mati begitu pipe selesai. Nggak ada pesan error apa",
                    "pun. Variabelnya cuma kosong.",
                    "",
                    "Yang paling sering kena adalah perulangan:",
                    "  n=0",
                    "  cat data.txt | while read -r baris; do ((n++)); done",
                    "  echo \"$n\"    -> tetap 0, bukan jumlah baris",
                    "",
                    "Perbaikannya: buang pipe-nya, alihkan berkasnya langsung ke perulangan.",
                    "  n=0",
                    "  while read -r baris; do ((n++)); done < data.txt",
                    "  echo \"$n\"    -> benar",
                    "",
                    "Jadi kalau ada variabel yang tiba-tiba kosong lagi sesudah sebuah",
                    "perulangan, cek dulu: apakah perulangan itu ada di sisi kanan pipe?",
                    "",
                    "Untuk memastikan program yang dibutuhkan memang terpasang:",
                    "  command -v jq >/dev/null 2>&1 || { echo \"butuh jq\" >&2; exit 1; }",
                    "",
                    "command -v mencetak lokasi program dan memberi status 0 kalau programnya",
                    "ketemu. >/dev/null 2>&1 membuang cetakannya, jadi yang dipakai cuma",
                    "statusnya. Taruh pemeriksaan seperti ini di awal script. Berhenti di",
                    "baris pertama dengan pesan yang jelas jauh lebih baik daripada gagal di",
                    "tengah pekerjaan, waktu separuh berkas udah telanjur dipindah.",
                    "",
                    "Jangan pakai 'which' untuk ini. which itu program luar, perilakunya",
                    "beda-beda di tiap sistem, dan dia nggak tahu apa-apa soal fungsi maupun",
                    "alias.",
                    "",
                    "type menjawab pertanyaan \"nama ini termasuk jenis apa?\":",
                    "  type -t echo       -> builtin   bawaan bash sendiri",
                    "  type -t sed        -> file      program di salah satu PATH",
                    "  type -t ll         -> alias     kalau kamu punya alias itu",
                    "  type namafungsimu  -> menampilkan seluruh isi fungsinya",
                    "",
                    "Ini alat pertama yang kamu pakai waktu sebuah perintah berperilaku aneh.",
                    "Sering ternyata nama itu udah dipakai fungsi atau alias, bukan program",
                    "yang kamu kira.",
                ],
                "code": """#!/usr/bin/env bash

pesan="awal"
cd /tmp

# ( ... ) = SUBSHELL. Isinya jalan di proses terpisah.
(
    pesan="diubah di kurung"
    cd /usr
    echo "di dalam ( ) : pesan=$pesan, pwd=$PWD"
)
echo "setelah  ( ) : pesan=$pesan, pwd=$PWD"

# { ... ; } = PENGELOMPOKAN saja. Tetap di shell yang sama.
{
    pesan="diubah di kurawal"
    cd /usr
}
echo "setelah  { } : pesan=$pesan, pwd=$PWD"

# Sisi KANAN pipe juga subshell, jadi kata tidak pernah terisi di sini.
echo "halo" | read -r kata
echo "lewat pipe   : kata='${kata:-(kosong)}'"
read -r kata <<< "halo"
echo "tanpa pipe   : kata='$kata'"

# Idiom sehari-hari: pastikan programnya ada, lalu kerja di folder lain.
command -v ls >/dev/null 2>&1 || { echo "butuh ls" >&2; exit 1; }
(cd /etc && ls hosts)
echo "masih di     : $PWD" """,
            },
        ],
    },
    {
        "title": "7. Shell Interaktif: .bashrc, alias, dan PATH",
        "sections": [
            {
                "body": [
                    "Tiap kali kamu buka terminal baru, bash nggak mulai dari nol. Dia baca",
                    "dulu beberapa berkas setelan di folder home-mu, lalu menjalankan isinya",
                    "baris demi baris, persis seperti kamu sendiri yang ngetik.",
                    "",
                    "Nama berkas setelan itu diawali titik, jadi nggak muncul di 'ls' biasa.",
                    "Untuk melihatnya, pakai 'ls -a ~'. Kumpulan berkas ini biasa disebut",
                    "dotfiles.",
                    "",
                    "  ~/.bashrc         setelan shell interaktif: alias, prompt, riwayat, PATH",
                    "  ~/.bash_profile   setelan shell login: dijalankan saat kamu login",
                    "  ~/.profile        versi netral, dibaca juga oleh shell selain bash",
                    "  ~/.bash_history   bukan setelan - ini catatan perintah yang pernah diketik",
                    "",
                    "Tanda ~ artinya folder home-mu, jadi ~/.bashrc sama dengan",
                    "/home/levi/.bashrc.",
                    "",
                    "Berkas mana yang dibaca tergantung jenis shell-nya:",
                    "",
                    "  Shell LOGIN         -> ~/.bash_profile (kalau tidak ada: ~/.bash_login,",
                    "                         kalau itu pun tidak ada: ~/.profile)",
                    "    Terjadi saat: masuk lewat SSH, login di layar teks, 'su - pengguna'.",
                    "",
                    "  Shell NON-LOGIN     -> ~/.bashrc",
                    "    Terjadi saat: membuka tab terminal baru di desktop. Paling sering.",
                    "",
                    "  Shell NON-INTERAKTIF -> tidak membaca dua-duanya.",
                    "    Terjadi saat: 'bash script.sh'. Script kamu TIDAK mewarisi isi ~/.bashrc.",
                    "",
                    "Dari sini muncul keluhan yang sering banget: \"setelanku kok nggak",
                    "kepakai?\"",
                    "  - Baris export ditaruh di ~/.bashrc, lalu kamu masuk lewat SSH. Yang",
                    "    dibaca ~/.bash_profile, jadi baris itu nggak pernah ikut jalan.",
                    "  - Baris export ditaruh di ~/.bash_profile, lalu kamu buka tab terminal",
                    "    baru. Yang dibaca ~/.bashrc. Hasilnya sama: nggak kepakai.",
                    "",
                    "Karena itu, hampir semua distro masang jembatan di ~/.bash_profile.",
                    "Dengan begitu, cuma ada satu berkas yang perlu kamu sunting:",
                    "",
                    "  # isi ~/.bash_profile",
                    "  [[ -f ~/.bashrc ]] && . ~/.bashrc",
                    "",
                    "Baris itu artinya: kalau ~/.bashrc ada, baca juga isinya.",
                    "",
                    "Sesudah kamu nyunting ~/.bashrc, perubahannya belum berlaku di terminal",
                    "yang lagi terbuka. Ada dua cara supaya berlaku:",
                    "  1. Tutup terminal, lalu buka lagi.",
                    "  2. Jalankan source ~/.bashrc untuk membaca ulang setelannya di shell",
                    "     yang sekarang jalan.",
                    "",
                    "Harus pakai source, bukan bash ~/.bashrc. Alasannya ada di materi",
                    "Proses, source, dan Subshell: kalau dijalankan sebagai script,",
                    "setelannya ikut mati bersama proses anaknya, dan terminalmu nggak",
                    "berubah sama sekali.",
                ],
            },
            {
                "heading": "Potongan khas isi ~/.bashrc",
                "code": "#!/usr/bin/env bash\n# Potongan yang khas ada di ~/.bashrc. Di sini ia dijalankan sebagai script\n# biasa supaya efek tiap barisnya kelihatan, tanpa mengubah setelan aslimu.\n\n# 1. PATH -- taruh folder program pribadi di DEPAN daftar bawaan\nexport PATH=\"$HOME/.local/bin:$PATH\"\n\n# 2. Alias -- nama pendek untuk perintah yang sering diketik\nalias ll='ls -alF'\nalias gs='git status'\nalias ..='cd ..'\n\n# 3. Riwayat perintah\nHISTSIZE=10000\nHISTFILESIZE=20000\nHISTCONTROL=ignorespace:erasedups\nshopt -s histappend\n\n# 4. Bentuk prompt: pengguna@mesin:folder$\nPS1='\\u@\\h:\\w\\$ '\n\n# 5. Menjalankan keluaran sebuah perintah sebagai kode\n# eval \"$(pyenv init -)\"\n\necho \"PATH kini diawali : ${PATH%%:*}\"\necho \"Definisi alias ll : $(alias ll)\"\necho \"Riwayat disimpan  : $HISTSIZE baris\"\necho \"Bentuk prompt PS1 : $PS1\"",
            },
            {
                "body": [
                    "Alias adalah nama pendek untuk perintah yang panjang.",
                    "",
                    "  alias ll='ls -alF'        pakai petik TUNGGAL supaya isinya tidak diproses",
                    "  alias gs='git status'     sekarang di terminal.",
                    "  alias                     tampilkan semua alias yang aktif",
                    "  unalias ll                hapus satu alias",
                    "  \\ls                       jalankan 'ls' asli, lewati aliasnya",
                    "",
                    "Alias cuma menggantikan kata pertama sebuah perintah. Alias juga nggak",
                    "bisa menerima argumen di tengah-tengahnya. Kalau butuh itu, pakai",
                    "fungsi.",
                    "",
                    "Jebakan terbesar: alias nggak berlaku di dalam script. Script jalan di",
                    "shell non-interaktif, dan bash sengaja mematikan alias di sana. Jadi",
                    "script yang memakai 'll' atau 'gs' bakal gagal dengan 'command not",
                    "found' di mesin siapa pun, termasuk mesinmu. Alias itu cuma buat",
                    "mempermudah ngetik, dan nggak ikut jadi bagian program. Di script,",
                    "tulis perintah lengkapnya.",
                    "",
                    "Jebakan lain: alias rm='rm -i' rasanya aman, karena rm jadi selalu",
                    "nanya dulu. Tapi alias itu melatih jarimu langsung tekan Enter tanpa",
                    "membaca. Lalu di mesin orang lain, atau di dalam script, alias itu",
                    "nggak ada. Konfirmasinya hilang, dan kebiasaan hati-hatimu juga udah",
                    "keburu hilang.",
                    "",
                    "Riwayat perintah bikin kamu jarang perlu ngetik ulang:",
                    "",
                    "  history            tampilkan perintah lama, bernomor",
                    "  !!                 ulangi perintah terakhir (sudo !!  = ulangi pakai sudo)",
                    "  !542               jalankan perintah nomor 542 dari daftar history",
                    "  !$                 argumen TERAKHIR dari perintah sebelumnya",
                    "  Ctrl-R             cari mundur sambil mengetik. Tekan lagi untuk yang",
                    "                     lebih lama, Enter untuk menjalankan, Esc untuk sunting.",
                    "",
                    "Setelan riwayat biasanya ditaruh di ~/.bashrc:",
                    "  HISTSIZE=10000              berapa baris disimpan di memori",
                    "  HISTFILESIZE=20000          berapa baris disimpan di ~/.bash_history",
                    "  HISTCONTROL=ignorespace     perintah yang DIAWALI SPASI tidak dicatat",
                    "  HISTCONTROL=erasedups       hapus duplikat lama",
                    "  shopt -s histappend         tambahkan ke berkas, jangan timpa isinya",
                    "",
                    "Dua baris HISTCONTROL di atas itu pilihan, bukan pasangan. Kalau",
                    "ditulis dua-duanya, baris kedua menimpa yang pertama. Mau dua-duanya",
                    "sekaligus? Gabungkan pakai titik dua: HISTCONTROL=ignorespace:erasedups.",
                    "",
                    "ignorespace itu praktis. Ketik satu spasi sebelum perintah yang berisi",
                    "password atau token, dan perintah itu nggak masuk ke ~/.bash_history.",
                    "",
                    "Prompt adalah teks yang muncul di depan kursor waktu bash nunggu",
                    "perintah. Bentuknya diatur variabel PS1 dan PS2.",
                    "",
                    "PS1 mengatur prompt utama. Di dalamnya, \\u artinya nama pengguna, \\h",
                    "nama mesin, \\w folder saat ini, dan \\$ jadi # kalau kamu root. PS2",
                    "adalah prompt lanjutan, yang muncul sebagai '>' waktu perintahmu belum",
                    "selesai, misalnya karena petiknya belum ditutup. Untuk sekarang cukup",
                    "kenali namanya aja. Kalau kamu buka .bashrc milik orang, deretan",
                    "karakter aneh yang paling bikin pusing biasanya cuma PS1.",
                    "",
                    "Dotfiles adalah berkas yang paling sering disalin orang di GitHub,",
                    "karena isinya hasil kebiasaan bertahun-tahun. Kalau kamu baca .bashrc",
                    "milik orang lain, jangan baca dari atas ke bawah. Pilah dulu per jenis:",
                    "  - baris export, yaitu setelan lingkungan;",
                    "  - baris alias, yaitu singkatan;",
                    "  - baris PS1 atau PROMPT, yaitu tampilan;",
                    "  - baris eval, yaitu kode yang ditempelkan alat lain.",
                    "",
                    "Sisanya biasanya penjaga yang bunyinya \"kalau berkasnya ada, baca\".",
                    "Salin satu baris aja tiap kali, lalu source dan lihat efeknya.",
                ],
            },
            {
                "heading": "PATH: daftar tempat shell mencari perintah",
                "body": [
                    "Waktu kamu ngetik 'ls', bash nggak tahu program bernama ls ada di mana.",
                    "Dia lihat variabel PATH. PATH itu satu string berisi daftar folder yang",
                    "dipisah titik dua. Bash memeriksa folder-folder itu dari kiri ke kanan,",
                    "dan berhenti di folder pertama yang punya program itu. Kalau daftarnya",
                    "habis dan programnya tetap nggak ketemu, muncul 'command not found'.",
                    "",
                    "Untuk menambahkan folder sendiri ke PATH, tulisannya selalu begini:",
                    "",
                    "  export PATH=\"$HOME/.local/bin:$PATH\"",
                    "",
                    "Artinya: PATH yang baru = folder baru, titik dua, lalu seluruh isi PATH",
                    "yang lama.",
                    "  - $PATH di sebelah kanan itu wajib. Dia menyalin daftar lama supaya",
                    "    nggak hilang.",
                    "  - Folder baru yang ditaruh di depan bikin versimu menang atas versi",
                    "    bawaan sistem. Kalau ditaruh di belakang",
                    "    (\"$PATH:$HOME/.local/bin\"), yang bawaan menang duluan.",
                    "",
                    "Kesalahan yang bikin terminal kerasa rusak:",
                    "",
                    "  export PATH=\"$HOME/.local/bin\"      <- lupa menyebut $PATH lama",
                    "",
                    "Sesudah baris itu, ls, mv, grep, bahkan nano nggak ketemu lagi, karena",
                    "/usr/bin udah nggak ada di daftar. Terminalnya nggak rusak, cuma",
                    "kehilangan alamat. Tutup terminal lalu buka lagi, semuanya normal. Yang",
                    "gawat kalau baris itu telanjur kamu simpan di ~/.bashrc, karena tiap",
                    "terminal baru bakal langsung rusak.",
                    "",
                    "Jangan masukkan titik (folder saat ini) ke PATH:",
                    "",
                    "  export PATH=\".:$PATH\"      <- kelihatan praktis, sebenarnya berbahaya",
                    "",
                    "Dengan PATH begitu, masuk ke sebuah folder lalu ngetik 'ls' bisa",
                    "menjalankan berkas bernama ls milik folder itu, bukan ls yang asli.",
                    "Cukup sekali kamu buka folder hasil unduhan orang, dan perintah paling",
                    "biasa pun bisa jadi jebakan. Kalau mau menjalankan program di folder",
                    "saat ini, tulis ./program. Itulah gunanya tanda ./ yang udah kamu pakai",
                    "sejak materi pertama.",
                    "",
                    "Lalu di mana nulisnya supaya permanen? export PATH=... di dalam script",
                    "cuma berlaku selama script itu jalan. Script adalah proses anak, dan",
                    "begitu dia selesai, PATH terminalmu nggak berubah sama sekali.",
                    "Alasannya ada di materi Proses, source, dan Subshell. Jadi nggak ada",
                    "script pemasang yang bisa mengubah PATH-mu secara langsung. Yang bisa",
                    "dia lakukan cuma menambahkan barisnya ke ~/.bashrc. Itulah yang terjadi",
                    "tiap kali panduan pemasangan nyuruh kamu menutup lalu membuka lagi",
                    "terminalnya.",
                    "",
                    "Cek hasilnya dengan:",
                    "  command -v nama_program   (atau: which nama_program)",
                ],
                "code": "#!/usr/bin/env bash\n# Melihat PATH sebagai daftar folder biasa, bukan sebagai mantra.\n\ncontoh=\"/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin\"\n\necho \"1) PATH itu SATU string. Folder-foldernya dipisah titik dua:\"\necho \"   $contoh\"\n\necho\necho \"2) Dipecah per baris supaya urutannya kelihatan:\"\necho \"$contoh\" | tr ':' '\\n' | sed 's/^/   /'\n\necho\necho \"3) Shell mencari dari ATAS ke bawah lalu berhenti di yang pertama cocok.\"\nbaru=\"$HOME/bin:$contoh\"\necho \"   Menambah di depan -> ${baru%%:*} yang dicoba paling awal.\"\n\necho\necho \"4) Perintah 'ls' yang sebenarnya dipakai ada di:\"\necho \"   $(command -v ls)\"\n\necho\necho \"5) Perubahan berikut hanya hidup selama script ini berjalan:\"\nexport PATH=\"/tmp/binku:$PATH\"\necho \"   PATH sekarang diawali: ${PATH%%:*}\"\necho \"   Begitu script selesai, PATH terminalmu kembali seperti semula\"",
            },
            {
                "heading": "eval: menjalankan teks sebagai kode",
                "body": [
                    "Baris yang paling membingungkan di dotfiles orang biasanya bentuknya",
                    "kayak gini:",
                    "",
                    "  eval \"$(pyenv init -)\"",
                    "  eval \"$(ssh-agent -s)\"",
                    "  eval \"$(dircolors -b)\"",
                    "",
                    "Bacanya dari dalam ke luar. pyenv di situ adalah program biasa, dan",
                    "urutan kerjanya begini:",
                    "  1. 'pyenv init -' dijalankan. Keluarannya berupa teks yang isinya kode",
                    "     bash, yaitu beberapa export dan definisi fungsi.",
                    "  2. $( ... ) menangkap teks itu.",
                    "  3. eval menjalankan teks itu sebagai perintah, di shell yang sekarang.",
                    "",
                    "Kenapa harus muter begitu? pyenv adalah program terpisah, dan program",
                    "terpisah nggak bisa mengubah variabel shell yang memanggilnya, karena",
                    "variabel cuma turun ke bawah. Jadi pyenv nitip kodenya sebagai teks,",
                    "dan shell-mu sendiri yang menjalankannya. Coba buktikan: jalankan",
                    "'ssh-agent -s' tanpa eval. Kamu bakal lihat baris-baris export yang",
                    "cuma tercetak, tanpa efek apa pun.",
                    "",
                    "Sisi bahayanya: eval menjalankan apa aja yang ada di dalam teksnya.",
                    "Kalau sebagian teks itu berasal dari pengguna, dari nama berkas, atau",
                    "dari jawaban server, pengguna itu bisa menjalankan perintah apa pun",
                    "dengan hak aksesmu, termasuk rm -rf. Ini persis yang diperingatkan",
                    "shellcheck, alat pemeriksa script bash, tiap kali dia lihat eval.",
                    "",
                    "Aturan praktisnya: pakai eval cuma untuk teks yang kamu percaya penuh,",
                    "biasanya keluaran alat yang kamu pasang sendiri. Untuk kebutuhan lain",
                    "hampir selalu ada cara yang lebih aman: array untuk menyusun perintah,",
                    "dan case untuk memilih salah satu dari beberapa perintah yang tetap.",
                ],
                "code": """#!/usr/bin/env bash
# eval = "ambil teks ini, lalu jalankan isinya sebagai perintah bash".

siapkan() {
    echo 'export PROYEK="belajar-bash"'
    echo 'alias bersih="rm -f *.tmp"'
}

echo "Teks yang DIHASILKAN perintah siapkan:"
siapkan | sed 's/^/   /'

echo
echo "Tanpa eval, teks itu cuma teks:"
echo "   PROYEK = '${PROYEK:-(masih kosong)}'"

eval "$(siapkan)"

echo
echo "Setelah eval, teks tadi benar-benar dijalankan:"
echo "   PROYEK = '$PROYEK'"

echo
echo "Sisi bahayanya -- teks yang di-eval datang dari luar:"
masukan='Andi"; echo "   <- baris ini diselundupkan lewat isian nama'
eval "echo \\"   Halo, $masukan\\"" """,
            },
        ],
    },
    {
        "title": "8. Aritmatika & Angka",
        "sections": [
            {
                "body": [
                    "Buat bash, semua nilai itu string. Jadi kalau mau ngitung, kamu perlu",
                    "sintaks khusus, yaitu cara penulisan yang memberi tahu bash bahwa isinya",
                    "angka.",
                    "",
                    "Cara utamanya $(( ... )):",
                    "  hasil=$((5 + 3))",
                    "  echo $((10 / 3))     -> 3  (PEMBAGIAN BULAT, sisa dibuang)",
                    "  echo $((10 % 3))     -> 1  (sisa bagi)",
                    "  echo $((2 ** 8))     -> 256 (pangkat)",
                    "",
                    "Di dalam $(( )), tanda $ di depan nama variabel boleh nggak ditulis:",
                    "  a=5; b=3",
                    "  echo $((a + b))      -> sama saja dengan $(($a + $b))",
                    "",
                    "Ingat: bash nggak bisa menghitung pecahan desimal. Hasil bagi selalu",
                    "dibulatkan ke bawah, dan sisanya dibuang.",
                    "  echo $((10 / 4))     -> 2, bukan 2.5",
                    "",
                    "Kalau butuh desimal, pakai bc atau awk:",
                    "  echo \"scale=2; 10/4\" | bc     -> 2.50",
                    "  awk 'BEGIN {printf \"%.2f\\n\", 10/4}'  -> 2.50",
                    "",
                    "scale=2 di bc artinya \"pakai dua angka di belakang koma\".",
                ]
            },
            {
                "heading": "Contoh lengkap",
                "code": """#!/usr/bin/env bash

a=15
b=4

echo "$a + $b = $((a + b))"
echo "$a - $b = $((a - b))"
echo "$a * $b = $((a * b))"
echo "$a / $b = $((a / b))   (bulat)"
echo "$a % $b = $((a % b))"

# Increment
hitung=0
((hitung++))
((hitung += 5))
echo "hitung = $hitung"

# Desimal dengan bc
echo "scale=3; $a / $b" | bc"""
            },
            {
                "body": [
                    "Ada juga operator singkat untuk mengubah nilai variabel. Semuanya",
                    "dipakai di dalam (( )):",
                    "  ((x += 5))    sama dengan x = x + 5",
                    "  ((x -= 2))",
                    "  ((x *= 3))",
                    "  ((x++))       naikkan 1",
                    "  ((x--))       turunkan 1",
                    "",
                    "Jebakan: hati-hati dengan ((x++)) waktu x masih 0. Kalau x bernilai 0,",
                    "((x++)) mengembalikan status 1, yang artinya dianggap gagal. Kalau",
                    "script-mu pakai 'set -e', script-nya bisa langsung berhenti di situ.",
                    "Yang aman, tulis ((x++)) || true, atau x=$((x + 1)).",
                    "",
                    "Status di sini adalah angka yang ditinggalkan tiap perintah setelah",
                    "selesai: 0 artinya sukses, selain 0 artinya gagal. ((x++)) memakai",
                    "nilai x sebelum dinaikkan, yaitu 0, dan buat (( )) nilai 0 artinya",
                    "salah.",
                    "",
                    "Kamu juga bakal ketemu let dan expr. Dua-duanya cara lama:",
                    "  let \"hasil = 5 + 3\"",
                    "  hasil=$(expr 5 + 3)",
                    "",
                    "Keduanya masih jalan, tapi sekarang orang lebih suka pakai $(( )).",
                ]
            },
        ],
    },
    {
        "title": "9. Percabangan (if, case)",
        "sections": [
            {
                "body": [
                    "if dipakai untuk menjalankan perintah cuma kalau sebuah kondisi",
                    "terpenuhi. Bentuk dasarnya:",
                    "",
                    "  if [[ kondisi ]]; then",
                    "      perintah",
                    "  elif [[ kondisi_lain ]]; then",
                    "      perintah",
                    "  else",
                    "      perintah",
                    "  fi",
                    "",
                    "Penutupnya 'fi', yaitu kata if yang dibalik. Penutup ini wajib ada.",
                    "",
                    "Pakai [[ ]] (kurung siku ganda), jangan [ ] tunggal.",
                    "  - [[ ]] itu fitur bash. Lebih aman, dan bisa dipakai bareng && || dan",
                    "    regex.",
                    "  - [ ] itu perintah lama yang lebih rewel soal spasi dan variabel",
                    "    kosong.",
                    "",
                    "\"Lama\" di sini nggak berarti usang. [ ] malah ada di semua shell,",
                    "sedangkan [[ ]] cuma milik bash. Selama shebang-mu bash, pakai [[ ]].",
                    "Begitu berkasnya #!/bin/sh, [ ] jadi satu-satunya pilihan. Soal ini",
                    "dibahas di materi Bash vs sh: Portabilitas & POSIX.",
                    "",
                    "Untuk membandingkan angka:",
                    "  -eq  sama dengan        -ne  tidak sama",
                    "  -gt  lebih besar        -ge  lebih besar atau sama",
                    "  -lt  lebih kecil        -le  lebih kecil atau sama",
                    "",
                    "Untuk membandingkan teks:",
                    "  ==   sama dengan        !=   tidak sama",
                    "  <    urutan abjad lebih dulu",
                    "  -z   string KOSONG      -n   string TIDAK kosong",
                    "",
                    "Untuk memeriksa berkas:",
                    "  -f  file biasa ada      -d  folder ada",
                    "  -e  ada (apa pun)       -r  bisa dibaca",
                    "  -w  bisa ditulis        -s  ada dan tidak kosong",
                ]
            },
            {
                "heading": "Contoh if",
                "code": """#!/usr/bin/env bash

read -p "Masukkan nilai: " nilai

if [[ $nilai -ge 85 ]]; then
    echo "Nilai A"
elif [[ $nilai -ge 75 ]]; then
    echo "Nilai B"
elif [[ $nilai -ge 60 ]]; then
    echo "Nilai C"
else
    echo "Tidak Lulus"
fi

# Menggabungkan kondisi
if [[ $nilai -ge 0 && $nilai -le 100 ]]; then
    echo "Nilai valid"
fi

# Cek file
if [[ -f "data.txt" ]]; then
    echo "File ada"
else
    echo "File tidak ditemukan"
fi"""
            },
            {
                "heading": "Perintah biasa boleh jadi kondisi",
                "body": [
                    "if nggak wajib pakai kurung siku. Yang dilihat if cuma exit code dari",
                    "perintah yang kamu taruh sesudahnya. Exit code adalah angka status yang",
                    "ditinggalkan perintah begitu selesai: 0 artinya \"benar\", selain 0",
                    "artinya \"salah\". [[ ]] sendiri ternyata juga cuma perintah yang",
                    "mengembalikan 0 atau 1.",
                    "",
                    "  if grep -q \"gagal\" catatan.log; then",
                    "      echo \"ada kegagalan di log\"",
                    "  fi",
                    "",
                    "  if command -v jq >/dev/null; then",
                    "      echo \"jq terpasang, boleh lanjut\"",
                    "  fi",
                    "",
                    "  if mkdir -p /data/baru; then echo \"folder siap\"; fi",
                    "",
                    "Perhatikan -q di grep dan >/dev/null di command. Dua-duanya membungkam",
                    "keluaran perintahnya, karena yang dipakai cuma statusnya. Tanpa itu,",
                    "hasil pencarian ikut muncul di layar padahal nggak diminta.",
                    "",
                    "Tanda seru di depan membalik statusnya, sama seperti di dalam [[ ]].",
                    "Jadi baris berikut tetap enak dibaca, walaupun nggak ada satu pun",
                    "kurung siku di dalamnya:",
                    "",
                    "  if ! command -v git >/dev/null; then",
                    "      echo \"git belum terpasang\" >&2",
                    "      exit 1",
                    "  fi",
                ]
            },
            {
                "heading": "case untuk banyak pilihan",
                "code": """#!/usr/bin/env bash

read -p "Pilih menu (a/b/c): " pilihan

case "$pilihan" in
    a|A)
        echo "Kamu pilih A"
        ;;
    b|B)
        echo "Kamu pilih B"
        ;;
    [0-9])
        echo "Kamu memasukkan angka"
        ;;
    *)
        echo "Pilihan tidak dikenal"
        ;;
esac"""
            },
            {
                "body": [
                    "Aturan case:",
                    "  - Tiap cabang ditutup dengan ;; (titik koma dua kali).",
                    "  - Tanda | memisahkan beberapa pola untuk satu cabang.",
                    "  - * adalah cabang bawaan, mirip else.",
                    "  - Penutup bloknya 'esac', yaitu kata case yang dibalik.",
                    "  - Pola boleh pakai wildcard (karakter pengganti): *.txt, [0-9], ??",
                    "",
                    "Kalau yang dibandingkan cuma satu variabel, case jauh lebih rapi",
                    "daripada if-elif yang berderet panjang.",
                    "",
                    "Perbandingan angka juga bisa pakai (( )):",
                    "  if (( nilai >= 75 )); then",
                    "",
                    "Di dalam (( )), kamu bisa pakai >, <, dan >= seperti di bahasa lain.",
                ]
            },
        ],
    },
    {
        "title": "10. Perulangan (for, while, until)",
        "sections": [
            {
                "body": [
                    "Perulangan dipakai untuk menjalankan perintah yang sama berkali-kali.",
                    "Bash punya empat bentuk bawaan:",
                    "  1. for ... in mengulang untuk setiap item dalam daftar.",
                    "  2. for (( )) bergaya C, pakai penghitung.",
                    "  3. while mengulang selama kondisinya benar.",
                    "  4. until mengulang sampai kondisinya benar. Ini kebalikan while.",
                    "",
                    "Isi perulangan diapit kata 'do' dan 'done'.",
                ]
            },
            {
                "heading": "Berbagai bentuk for",
                "code": """#!/usr/bin/env bash

# Daftar nilai langsung
for buah in apel jeruk mangga; do
    echo "Buah: $buah"
done

# Rentang angka (brace expansion)
for i in {1..5}; do
    echo "Angka $i"
done

# Rentang dengan loncatan 2
for i in {0..10..2}; do
    echo "Genap: $i"
done

# Gaya C
for (( i = 1; i <= 5; i++ )); do
    echo "Iterasi ke-$i"
done

# Mengulang file di folder
for berkas in *.txt; do
    echo "Ditemukan: $berkas"
done"""
            },
            {
                "heading": "while dan until",
                "code": """#!/usr/bin/env bash

# while: ulang selama kondisi BENAR
i=1
total=0
while [[ $i -le 10 ]]; do
    total=$((total + i))
    ((i++))
done
echo "Jumlah 1..10 = $total"

# until: ulang sampai kondisi BENAR
n=5
until [[ $n -eq 0 ]]; do
    echo "Hitung mundur: $n"
    ((n--))
done

# Membaca file baris demi baris (pola paling penting!)
while IFS= read -r baris; do
    echo "Baris: $baris"
done < "data.txt" """
            },
            {
                "body": [
                    "Pola untuk membaca berkas baris demi baris:",
                    "  while IFS= read -r baris; do ... done < file",
                    "",
                    "  IFS=   mematikan pemotongan spasi, jadi spasi di awal/akhir",
                    "         baris ikut terbaca apa adanya.",
                    "  -r     mencegah backslash diproses sebagai escape.",
                    "",
                    "Hafalkan pola ini. Ini cara yang benar untuk membaca berkas di bash.",
                    "",
                    "Jangan pakai for baris in $(cat file). Bentuk itu memecah isi berkas di",
                    "setiap spasi, bukan di setiap baris.",
                    "",
                    "Mengendalikan perulangan:",
                    "  break      keluar dari perulangan",
                    "  continue   lompat ke iterasi berikutnya",
                    "  break 2    keluar dari 2 tingkat perulangan sekaligus",
                    "",
                    "Iterasi artinya satu putaran perulangan.",
                    "",
                    "Perulangan tanpa akhir:",
                    "  while true; do ... done",
                    "",
                    "Di dalamnya wajib ada break. Kalau nggak, script-nya nggak bakal",
                    "berhenti.",
                ]
            },
            {
                "heading": "select: menu bernomor yang dibuatkan bash",
                "body": [
                    "Ada bentuk kelima yang jarang diajarkan, tapi sering muncul di script",
                    "instalasi dan alat admin. select bikin menu bernomor dari sebuah daftar,",
                    "membaca ketikan pengguna, lalu mengulang terus sampai ketemu break.",
                    "",
                    "  PS3=\"Pilih nomor: \"",
                    "  select warna in merah hijau biru; do",
                    "      case \"$warna\" in",
                    "          merah|hijau|biru) echo \"kamu pilih $warna\"; break ;;",
                    "          *) echo \"nomor $REPLY tidak ada di daftar\" ;;",
                    "      esac",
                    "  done",
                    "",
                    "Yang muncul di layar:",
                    "  1) merah",
                    "  2) hijau",
                    "  3) biru",
                    "  Pilih nomor:",
                    "",
                    "Tiga hal soal menu ini:",
                    "  - PS3 adalah teks prompt-nya. Kalau nggak diisi, bash pakai '#?', yang",
                    "    nggak menjelaskan apa-apa ke pengguna.",
                    "  - $REPLY berisi apa yang diketik pengguna, apa adanya.",
                    "  - $warna berisi nilai yang dipilih. Isinya kosong kalau yang diketik",
                    "    bukan nomor yang ada di daftar. Karena itu ada cabang *) di atas.",
                    "",
                    "select nggak berhenti sendiri. Tanpa break, menunya ditampilkan lagi",
                    "terus-menerus, dan pengguna baru bisa keluar dengan Ctrl-D.",
                ]
            },
        ],
    },
    {
        "title": "11. Array",
        "sections": [
            {
                "body": [
                    "Array adalah satu variabel yang isinya banyak nilai, berurutan. Bash",
                    "punya dua jenis array:",
                    "  1. Array biasa, yang indeksnya angka dan mulai dari 0. Indeks itu",
                    "     nomor urut tiap item.",
                    "  2. Associative array atau map, yang indeksnya berupa teks. Jenis ini",
                    "     butuh bash versi 4 ke atas.",
                    "",
                    "Membuat array biasa:",
                    "  buah=(\"apel\" \"jeruk\" \"mangga\")",
                    "",
                    "Mengakses isinya:",
                    "  ${buah[0]}      item pertama",
                    "  ${buah[-1]}     item terakhir",
                    "  ${buah[@]}      SEMUA item",
                    "  ${#buah[@]}     JUMLAH item",
                    "  ${!buah[@]}     semua INDEKS",
                    "",
                    "Perhatikan kurung kurawalnya:",
                    "  $buah      -> hanya memberi item pertama, bukan seluruh array!",
                    "  ${buah[@]} -> baru seluruh array.",
                    "",
                    "Selalu bungkus pakai petik: \"${buah[@]}\". Tanpa petik, item yang ada",
                    "spasinya bakal terpecah.",
                ]
            },
            {
                "heading": "Operasi array",
                "code": """#!/usr/bin/env bash

buah=("apel" "jeruk" "mangga")

echo "Pertama : ${buah[0]}"
echo "Terakhir: ${buah[-1]}"
echo "Jumlah  : ${#buah[@]}"

# Tambah item di akhir
buah+=("pisang")

# Ulangi isi array
for b in "${buah[@]}"; do
    echo "- $b"
done

# Ulangi dengan indeks
for i in "${!buah[@]}"; do
    echo "$i: ${buah[i]}"
done

# Potong array: mulai indeks 1, ambil 2 item
echo "${buah[@]:1:2}"

# Hapus item indeks 1
unset 'buah[1]'"""
            },
            {
                "heading": "[@] dan [*]: dua cara menyebut seluruh array",
                "body": [
                    "Selain [@], ada [*]. Dua-duanya berarti \"seluruh isi array\". Bedanya",
                    "baru kelihatan begitu dibungkus petik ganda:",
                    "",
                    "  \"${buah[@]}\"   -> N kata terpisah, satu kata per elemen",
                    "  \"${buah[*]}\"   -> SATU kata, semua elemen disambung jadi satu",
                    "",
                    "Penyambungnya adalah karakter pertama dari IFS, yang biasanya spasi.",
                    "",
                    "  buah=(\"apel\" \"jeruk manis\" \"mangga\")",
                    "  for b in \"${buah[@]}\"; do echo \"- $b\"; done",
                    "      -> tiga baris, 'jeruk manis' tetap utuh",
                    "  echo \"${buah[*]}\"",
                    "      -> apel jeruk manis mangga        (satu baris, satu kata)",
                    "",
                    "Aturan pakainya pendek aja:",
                    "  Mau MENGULANG atau meneruskan ke perintah lain -> \"${arr[@]}\".",
                    "  Mau MENCETAK isinya jadi satu baris ringkas    -> \"${arr[*]}\".",
                    "",
                    "  menipis=(\"susu\" \"telur\")",
                    "  echo \"Stok menipis: ${menipis[*]}\"   -> Stok menipis: susu telur",
                    "",
                    "Penyambungnya bisa diganti sebentar lewat IFS:",
                    "  LAMA=$IFS; IFS=,; echo \"${menipis[*]}\"; IFS=$LAMA   -> susu,telur",
                    "",
                    "Ini pasangan persis dari $@ dan $* untuk argumen script, yang dibahas di",
                    "materi Argumen & Exit Code. Aturannya sama, cuma bendanya beda.",
                ]
            },
            {
                "heading": "Associative array (map)",
                "code": """#!/usr/bin/env bash

# WAJIB dideklarasikan dulu dengan declare -A
declare -A umur
umur["andi"]=25
umur["budi"]=30
umur["citra"]=28

echo "Umur andi: ${umur[andi]}"
echo "Jumlah data: ${#umur[@]}"

# Ulangi semua pasangan (urutan TIDAK terjamin!)
for nama in "${!umur[@]}"; do
    echo "$nama berumur ${umur[$nama]}"
done

# Cek apakah kunci ada
if [[ -v umur["andi"] ]]; then
    echo "Data andi tersedia"
fi"""
            },
            {
                "body": [
                    "Beberapa hal soal associative array:",
                    "  - Wajib pakai declare -A sebelum dipakai. Kalau lupa, bash",
                    "    memperlakukannya sebagai array biasa, dan hasilnya kacau.",
                    "  - Urutan isinya waktu diulang nggak terjamin. Kalau butuh urut,",
                    "    saring lewat sort:",
                    "      for k in $(echo \"${!umur[@]}\" | tr ' ' '\\n' | sort); do",
                    "    tr di situ menukar satu karakter dengan karakter lain. Di sini tiap",
                    "    spasi diganti baris baru. Ini perlu, karena ${!umur[@]} keluar",
                    "    sebagai satu baris berisi semua kunci, sedangkan sort mengurutkan",
                    "    baris, bukan kata di dalam satu baris. Tanpa tr, sort cuma menerima",
                    "    satu baris dan mengembalikannya apa adanya.",
                    "  - Butuh bash versi 4 ke atas. macOS bawaan masih pakai bash 3.2. Cek",
                    "    versimu dengan echo $BASH_VERSION.",
                    "",
                    "Memecah string jadi array:",
                    "  teks=\"a,b,c\"",
                    "  IFS=',' read -ra bagian <<< \"$teks\"",
                    "  echo \"${bagian[1]}\"   -> b",
                    "",
                    "Mengisi array dari berkas, satu baris jadi satu elemen:",
                    "  mapfile -t baris < catatan.txt",
                    "  echo \"${#baris[@]} baris terbaca\"",
                    "",
                    "-t membuang karakter baris baru di ujung tiap elemen. Tanpa -t, tiap",
                    "elemen ikut membawa baris barunya. mapfile butuh bash 4 ke atas. Bentuk",
                    "lengkapnya, termasuk mengisi array dari keluaran sebuah perintah, ada di",
                    "materi find, xargs, dan Pemrosesan Massal.",
                ]
            },
        ],
    },
    {
        "title": "12. Fungsi",
        "sections": [
            {
                "body": [
                    "Fungsi adalah sekumpulan perintah yang dikasih nama, supaya bisa",
                    "dipanggil berkali-kali tanpa ditulis ulang. Ada dua cara menulisnya, dan",
                    "hasilnya sama aja:",
                    "",
                    "  nama_fungsi() {",
                    "      perintah",
                    "  }",
                    "",
                    "  function nama_fungsi {",
                    "      perintah",
                    "  }",
                    "",
                    "Bentuk pertama lebih portabel, jadi pakai itu aja.",
                    "",
                    "Fungsi harus didefinisikan sebelum dipanggil, karena bash membaca script",
                    "dari atas ke bawah.",
                    "",
                    "Cara memanggil fungsi sama seperti memanggil perintah biasa:",
                    "  sapa \"Andi\"          <- TANPA kurung, argumen dipisah spasi",
                    "  BUKAN sapa(\"Andi\")",
                    "",
                    "Di dalam fungsi, argumennya dibaca lewat $1, $2, $3, dan seterusnya.",
                    "  $#   jumlah argumen yang dikirim",
                    "  $@   semua argumen",
                ]
            },
            {
                "heading": "Fungsi dasar",
                "code": """#!/usr/bin/env bash

sapa() {
    echo "Halo, $1! Selamat datang."
}

jumlahkan() {
    local a=$1
    local b=$2
    echo $((a + b))
}

sapa "Andi"
sapa "Budi"

# Ambil hasil fungsi lewat command substitution
hasil=$(jumlahkan 7 5)
echo "7 + 5 = $hasil" """
            },
            {
                "body": [
                    "Ada dua cara fungsi \"mengembalikan\" nilai.",
                    "",
                    "Cara pertama untuk data: fungsi mencetak hasilnya pakai echo, lalu",
                    "pemanggilnya menangkap cetakan itu pakai $( ).",
                    "  jumlahkan() { echo $(($1 + $2)); }",
                    "  hasil=$(jumlahkan 3 4)",
                    "",
                    "Cara kedua untuk status: pakai return, dengan nilai 0 sampai 255.",
                    "  cek_genap() {",
                    "      if (( $1 % 2 == 0 )); then return 0; else return 1; fi",
                    "  }",
                    "  if cek_genap 4; then echo \"genap\"; fi",
                    "",
                    "Ingat: return di bash nggak dipakai untuk mengirim data seperti di",
                    "Python atau Java. return cuma mengirim kode status.",
                    "  0     = sukses / benar",
                    "  1-255 = gagal / salah",
                    "",
                    "Hati-hati, ini kebalikan dari kebiasaan banyak bahasa lain, yang",
                    "menganggap 0 itu salah.",
                    "",
                    "Lalu ada kata kunci local. Tanpa local, semua variabel di bash bersifat",
                    "global, artinya bisa dipakai dan diubah dari mana aja. Variabel di",
                    "dalam fungsi bisa menimpa variabel di luar yang namanya sama. Jadi",
                    "selalu pakai local untuk variabel di dalam fungsi.",
                ]
            },
            {
                "heading": "Mengoper array ke fungsi",
                "body": [
                    "Begitu kamu punya array dan punya fungsi, pertanyaan ini pasti muncul:",
                    "gimana cara ngirim array-nya ke dalam fungsi?",
                    "",
                    "Fungsi bash menerima argumen sebagai daftar kata, bukan sebagai satu",
                    "benda utuh. Jadi array dikirim dengan cara dipecah jadi argumen-argumen,",
                    "lalu dirakit ulang di dalam fungsi:",
                    "",
                    "  cetak_daftar() {",
                    "      local daftar=(\"$@\")",
                    "      echo \"${#daftar[@]} item\"",
                    "  }",
                    "",
                    "  buah=(\"apel\" \"jeruk manis\")",
                    "  cetak_daftar \"${buah[@]}\"",
                    "",
                    "Petik di \"${buah[@]}\" wajib. Tanpa petik, 'jeruk manis' pecah jadi dua",
                    "argumen, dan fungsinya menerima tiga item, bukan dua.",
                    "",
                    "Ada dua batasan, supaya kamu nggak kaget nanti:",
                    "  - Yang sampai ke fungsi adalah salinan. Mengubah daftar di dalam",
                    "    fungsi nggak menyentuh buah yang di luar.",
                    "  - Cuma bisa satu array. Begitu ada argumen lain ikut dikirim, fungsi",
                    "    nggak punya cara untuk tahu di mana array-nya berakhir.",
                    "",
                    "Kalau kamu perlu mengubah array milik pemanggil, atau perlu ngirim dua",
                    "array sekaligus, caranya pakai nameref (local -n). Itu dibahas di materi",
                    "Fitur Bash Lanjutan.",
                ],
                "code": """#!/usr/bin/env bash

cetak_daftar() {
    local daftar=("$@")
    echo "menerima ${#daftar[@]} item:"
    for x in "${daftar[@]}"; do
        echo "  - $x"
    done
}

buah=("apel" "jeruk manis" "mangga")

echo "== dengan petik: tiap elemen utuh =="
cetak_daftar "${buah[@]}"

echo "== tanpa petik: 'jeruk manis' pecah dua =="
cetak_daftar ${buah[@]}"""
            },
            {
                "heading": "local vs global",
                "code": """#!/usr/bin/env bash

nilai="luar"

tanpa_local() {
    nilai="diubah"
}

dengan_local() {
    local nilai="aman"
}

dengan_local
echo "Setelah dengan_local  : $nilai"   # luar

tanpa_local
echo "Setelah tanpa_local   : $nilai"   # diubah"""
            },
        ],
    },
    {
        "title": "13. Argumen & Exit Code",
        "sections": [
            {
                "body": [
                    "Script bisa menerima argumen dari baris perintah. Argumen adalah kata",
                    "yang kamu tulis sesudah nama script waktu menjalankannya:",
                    "  ./backup.sh /data /cadangan",
                    "",
                    "Di dalam script, argumen itu bisa dibaca begini:",
                    "  $0   ./backup.sh   (nama script)",
                    "  $1   /data",
                    "  $2   /cadangan",
                    "  $#   2             (jumlah argumen)",
                    "  $@   semua argumen sebagai daftar terpisah",
                    "  $*   semua argumen sebagai SATU string",
                    "",
                    "$* jadi satu string kalau dibungkus petik (\"$*\"). Waktu meneruskan",
                    "argumen ke perintah lain, selalu pakai \"$@\", jangan \"$*\".",
                    "",
                    "Exit code, atau kode keluar, adalah angka yang dikembalikan tiap",
                    "perintah waktu selesai:",
                    "  0        = SUKSES",
                    "  bukan 0  = GAGAL",
                    "",
                    "Ini memang kebalikan dari tebakan banyak orang: di sini 0 artinya",
                    "berhasil.",
                    "",
                    "Exit code perintah terakhir bisa kamu cek lewat $?. Untuk mengatur exit",
                    "code script-mu sendiri, pakai exit 0 atau exit 1.",
                ]
            },
            {
                "heading": "Validasi argumen",
                "code": """#!/usr/bin/env bash

if [[ $# -lt 2 ]]; then
    echo "Cara pakai: $0 <sumber> <tujuan>" >&2
    exit 1
fi

sumber="$1"
tujuan="$2"

if [[ ! -d "$sumber" ]]; then
    echo "Error: folder '$sumber' tidak ada" >&2
    exit 2
fi

echo "Menyalin $sumber ke $tujuan..."
exit 0"""
            },
            {
                "body": [
                    "Perhatikan >&2 di contoh di atas. Tanda itu mengalihkan pesan ke stderr,",
                    "yaitu aliran khusus untuk error, bukan ke stdout. Pesan error harus ke",
                    "stderr supaya nggak mengotori output yang mungkin lagi di-pipe ke",
                    "perintah lain.",
                    "",
                    "Kamu bisa menyambung perintah berdasarkan hasilnya:",
                    "  perintah1 && perintah2    jalankan 2 kalau 1 SUKSES",
                    "  perintah1 || perintah2    jalankan 2 kalau 1 GAGAL",
                    "  perintah1 ; perintah2     jalankan 2 apa pun hasilnya",
                    "",
                    "  mkdir data && cd data",
                    "  cd /folder/salah || echo \"Gagal masuk folder\"",
                    "",
                    "Ada tiga pengaman yang sebaiknya ada di tiap script yang dipakai",
                    "beneran:",
                    "  set -e   hentikan script saat ada perintah gagal",
                    "  set -u   error kalau ada variabel belum didefinisikan",
                    "  set -o pipefail   pipe dianggap gagal kalau ada bagian gagal",
                    "",
                    "Ketiganya biasa ditulis singkat di baris kedua script:",
                    "  set -euo pipefail",
                ]
            },
        ],
    },
    {
        "title": "14. Opsi Baris Perintah & getopts",
        "sections": [
            {
                "body": [
                    "Kamu udah bisa membaca argumen lewat $1, $2, dan $# (materi Argumen &",
                    "Exit Code). Sekarang lihat cara perintah yang kamu pakai tiap hari",
                    "dipanggil:",
                    "",
                    "  cp -r -v sumber/ tujuan/",
                    "  grep -n -i \"error\" catatan.log",
                    "  tar -c -z -f arsip.tar.gz folder/",
                    "",
                    "Di situ ada dua jenis argumen, dan masing-masing punya tugas sendiri.",
                    "",
                    "Yang pertama argumen posisional, misalnya sumber/, tujuan/, dan",
                    "catatan.log. Artinya ditentukan oleh urutannya: yang pertama sumber,",
                    "yang kedua tujuan. Biasanya wajib ada. Kalau urutannya tertukar,",
                    "hasilnya salah, dan nggak ada yang protes.",
                    "",
                    "Yang kedua opsi, sering juga disebut flag atau switch, misalnya -r, -v,",
                    "-n, -i, dan -f arsip.tar.gz. Artinya ditentukan oleh hurufnya, bukan",
                    "posisinya. Urutannya boleh ditukar, dan boleh juga nggak ditulis sama",
                    "sekali. Opsi yang nggak ditulis memakai nilai bawaan.",
                    "",
                    "Opsi sendiri ada dua macam:",
                    "  - Opsi saklar nggak membawa nilai, misalnya -v, -r, -n. Kalau ditulis",
                    "    artinya nyala, kalau nggak ditulis artinya mati.",
                    "  - Opsi bernilai mengambil satu argumen sesudahnya, misalnya",
                    "    -o hasil.txt atau -f arsip.tar.gz.",
                    "",
                    "Hampir semua alat Unix mengikuti kesepakatan yang sama. Hafalkan",
                    "bentuknya, nggak perlu hafal alatnya:",
                    "",
                    "  - -abc sama dengan -a -b -c. Saklar boleh digabung jadi satu",
                    "    gerombolan.",
                    "  - -o hasil.txt sama dengan -ohasil.txt. Nilainya boleh nempel ke",
                    "    hurufnya.",
                    "  - --verbose adalah bentuk panjang, lebih gampang dibaca di script. Ini",
                    "    gaya GNU, bukan POSIX.",
                    "  - --out=hasil adalah bentuk panjang yang membawa nilai lewat tanda sama",
                    "    dengan.",
                    "  - -h atau --help hampir selalu ada. Alat yang nggak menyediakannya",
                    "    terasa rusak.",
                    "  - -- adalah penanda \"opsi habis di sini\". Semua sesudahnya dianggap",
                    "    posisional, apa pun bentuknya.",
                    "",
                    "Kenapa alat sungguhan hampir selalu punya dua jenis argumen ini? Yang",
                    "wajib dan yang pilihan butuh cara penyebutan yang beda. Kalau semuanya",
                    "posisional, menambah satu pilihan baru berarti menggeser arti argumen",
                    "ke-3. Semua pemanggilan lama yang udah tertulis di script orang lain",
                    "mendadak salah arti. Opsi bisa ditambah kapan aja tanpa mengusik yang",
                    "udah ada.",
                    "",
                    "Makanya blok penguraian opsi biasanya ada di 20 sampai 30 baris pertama",
                    "sebuah script. Bagian ini yang paling dulu kamu baca kalau mau tahu",
                    "\"script ini dipanggilnya gimana?\".",
                    "",
                    "Bash punya perintah bawaan untuk mengurai opsi pendek, namanya getopts.",
                    "Jangan ketuker dengan getopt (tanpa huruf s). getopt itu program",
                    "terpisah dari paket util-linux, bukan bawaan bash, dan versi lamanya",
                    "merusak argumen yang ada spasinya. Yang dipakai di sini getopts.",
                ],
            },
            {
                "heading": "Script utuh dengan -h, -v, dan -o BERKAS",
                "code": """#!/usr/bin/env bash
set -euo pipefail

NAMA="${0##*/}"

bantuan() {
    cat << EOF
Penggunaan: $NAMA [-h] [-v] [-o BERKAS] SUMBER...

Opsi:
  -h          tampilkan bantuan ini lalu keluar
  -v          mode cerewet (verbose)
  -o BERKAS   tulis hasil ke BERKAS (bawaan: layar)
EOF
}

jalan() {
    local OPTIND=1 opt
    local cerewet=0 keluaran="layar"

    while getopts ":hvo:" opt; do
        case "$opt" in
            h)  bantuan; return 0 ;;
            v)  cerewet=1 ;;
            o)  keluaran="$OPTARG" ;;
            \\?) echo "$NAMA: opsi tak dikenal: -$OPTARG" >&2; return 2 ;;
            :)  echo "$NAMA: opsi -$OPTARG butuh sebuah nilai" >&2; return 2 ;;
        esac
    done

    shift $((OPTIND - 1))

    echo "  cerewet  = $cerewet"
    echo "  keluaran = $keluaran"
    echo "  sisa     = $# argumen posisional: $*"
}

# Biasanya cukup: jalan "$@". Di sini kita panggil berkali-kali dengan
# kombinasi berbeda supaya kamu lihat hasil penguraiannya sekaligus.
coba() {
    echo "--- $NAMA $* ---"
    jalan "$@" || echo "  (berhenti, status $?)"
    echo
}

coba laporan.txt
coba -h
coba -v laporan.txt
coba -o hasil.log -v laporan.txt data.csv
coba -vo hasil.log laporan.txt
coba laporan.txt -v
coba -x laporan.txt
coba -o""",
            },
            {
                "body": [
                    "Kita baca baris kuncinya pelan-pelan:",
                    "",
                    "  while getopts \":hvo:\" opt; do",
                    "",
                    "getopts dipanggil berulang-ulang. Tiap panggilan mengambil satu opsi",
                    "berikutnya, menaruh hurufnya di variabel opt, lalu memberi status 0",
                    "supaya while berputar lagi. Begitu opsinya habis, statusnya bukan 0, dan",
                    "perulangannya berhenti sendiri.",
                    "",
                    "String \":hvo:\" adalah daftar opsi yang diterima. Titik duanya punya dua",
                    "arti, tergantung letaknya. Bagian ini yang paling sering bikin bingung",
                    "waktu membaca kode orang:",
                    "",
                    "  - Titik dua sesudah huruf, seperti o:, artinya opsi itu wajib membawa",
                    "    nilai.",
                    "  - Titik dua di paling depan, seperti :hvo:, artinya mode senyap.",
                    "    getopts nggak mencetak pesan error-nya sendiri, dan urusan salah",
                    "    diserahkan ke kamu.",
                    "",
                    "Jadi \":hvo:\" artinya: tangani sendiri kesalahannya, terima -h dan -v",
                    "tanpa nilai, dan terima -o yang membawa nilai. Kalau titik dua di depan",
                    "nggak ada, getopts mencetak pesan error versinya sendiri dalam bahasa",
                    "Inggris ke stderr, dan cabang :) nggak pernah kena sama sekali.",
                    "",
                    "getopts mengisi tiga variabel:",
                    "",
                    "  - $opt berisi huruf opsi yang barusan ditemukan. Nama variabelnya kamu",
                    "    yang pilih.",
                    "  - $OPTARG berisi nilai milik opsi itu, kalau opsinya memang bernilai.",
                    "  - $OPTIND berisi nomor argumen berikutnya yang belum diurai. Variabel",
                    "    ini dikelola getopts sendiri.",
                    "",
                    "Di mode senyap, $OPTARG juga dipakai untuk hal lain. Kalau opsinya nggak",
                    "dikenal, atau nilainya nggak dikasih, $OPTARG berisi huruf yang",
                    "bermasalah. Karena itu pesan \"opsi -$OPTARG butuh sebuah nilai\" bisa",
                    "menyebut huruf yang tepat.",
                    "",
                    "  shift $((OPTIND - 1))",
                    "",
                    "Baris ini nggak boleh lupa. Sesudah perulangan selesai, OPTIND menunjuk",
                    "argumen pertama yang bukan opsi. shift membuang semua opsi yang udah",
                    "dibaca, sehingga $1 kembali berarti \"argumen posisional pertama\" dan $#",
                    "kembali berarti \"berapa berkas yang dikirim\". Kalau baris ini lupa,",
                    "semua kode sesudahnya membaca $1 sebagai \"-v\".",
                    "",
                    "Ada dua cabang case yang selalu ada di kode nyata:",
                    "  - \\?) untuk opsi yang nggak ada di daftar. Backslash-nya wajib. Di",
                    "    dalam case, tanda tanya sendirian adalah wildcard yang cocok dengan",
                    "    satu karakter apa pun. Tanpa backslash, cabang ini ikut menelan",
                    "    cabang :) di bawahnya.",
                    "  - :) untuk opsi bernilai yang nilainya nggak dikasih, misalnya -o di",
                    "    ujung baris.",
                    "",
                    "Di dua cabang itu, keluar dengan status 2, bukan 1. Kesepakatan di Unix:",
                    "1 artinya \"pekerjaannya gagal\", 2 artinya \"cara memanggilnya salah\".",
                    "Arti angka keluar ada di materi Argumen & Exit Code.",
                    "",
                    "Jebakan 1: getopts berhenti di argumen pertama yang bukan opsi. Lihat",
                    "baris keluaran untuk 'coba laporan.txt -v' di atas: cerewet tetap 0.",
                    "Begitu getopts ketemu laporan.txt, dia nganggap opsinya udah habis, jadi",
                    "-v masuk ke argumen posisional. Ini aturan POSIX, bukan bug. Beberapa",
                    "alat GNU sengaja melanggarnya (ls berkas -l tetap jalan), jadi banyak",
                    "orang ngira semua alat begitu. Script bash-mu nggak begitu. Tulis",
                    "opsinya dulu, baru berkasnya.",
                    "",
                    "Jebakan 2: OPTIND nggak balik sendiri ke 1. OPTIND itu variabel biasa",
                    "yang hidup sampai script selesai. Kalau penguraian opsi ditaruh di dalam",
                    "fungsi, dan fungsinya dipanggil dua kali, panggilan kedua mulai dari",
                    "posisi terakhir. Opsinya dilewati tanpa satu pun pesan error. Makanya",
                    "baris pertama fungsi jalan() berbunyi local OPTIND=1. Kalau",
                    "penguraiannya nggak di dalam fungsi, tulis OPTIND=1 sebelum",
                    "perulangannya.",
                    "",
                    "Catatan: waktu kamu mencoba contohnya, pesan error di situ sengaja",
                    "dikirim ke stderr (>&2). Jadi di aplikasi ini, pesan itu muncul di panel",
                    "yang terpisah dari keluaran biasa. Itu perilaku yang benar, bukan tanda",
                    "gagal.",
                ],
            },
            {
                "heading": "Opsi panjang: getopts tidak bisa, urai sendiri",
                "code": """#!/usr/bin/env bash
set -euo pipefail

NAMA="${0##*/}"

galat() { echo "$NAMA: $*" >&2; }

urai() {
    local keluaran="layar" paksa=0 cerewet=0

    while [[ $# -gt 0 ]]; do
        case "$1" in
            -o|--out)
                [[ $# -ge 2 ]] || { galat "$1 butuh sebuah nilai"; return 2; }
                keluaran="$2"; shift 2 ;;
            --out=*)
                keluaran="${1#*=}"; shift ;;
            -f|--force)
                paksa=1; shift ;;
            -v|--verbose)
                cerewet=1; shift ;;
            -h|--help)
                echo "  (di sini bantuan() dipanggil, lalu return 0)"; return 0 ;;
            --)
                shift; break ;;
            -?*)
                galat "opsi tak dikenal: $1"; return 2 ;;
            *)
                break ;;
        esac
    done

    echo "  keluaran = $keluaran"
    echo "  paksa    = $paksa"
    echo "  cerewet  = $cerewet"
    echo "  sisa     = $# berkas: $*"
}

coba() {
    echo "--- $NAMA $* ---"
    urai "$@" || echo "  (berhenti, status $?)"
    echo
}

coba --verbose laporan.txt
coba --out hasil.log --force laporan.txt
coba --out=hasil.log laporan.txt
coba -f --out
coba --salah laporan.txt
coba --force -- -berkas-diawali-strip.txt""",
            },
            {
                "body": [
                    "Ada satu batas getopts yang perlu kamu tahu sebelum nyari-nyari di",
                    "dokumentasi: getopts cuma ngerti opsi pendek satu huruf. Nggak ada",
                    "saklar apa pun yang bikin dia paham --verbose. Kalau script-mu butuh",
                    "opsi panjang, penguraiannya ditulis sendiri seperti contoh di atas. Pola",
                    "ini bakal kamu temui di ribuan script di GitHub, jadi kenali bentuknya",
                    "sampai hafal.",
                    "",
                    "Cara membaca perulangannya:",
                    "  while [[ $# -gt 0 ]]   selama masih ada argumen tersisa",
                    "  case \"$1\" in           lihat argumen paling depan",
                    "  shift                  buang 1 argumen (saklar: hurufnya saja)",
                    "  shift 2                buang 2 argumen (opsi bernilai: namanya DAN nilainya)",
                    "  break                  keluar dari perulangan; sisanya posisional",
                    "",
                    "Urutan cabangnya penting. case berhenti di cabang pertama yang cocok.",
                    "Jadi cabang penangkap -?* harus ada di bawah semua opsi yang dikenal.",
                    "Kalau ditaruh di atas, semua opsimu sendiri bakal dilaporkan sebagai",
                    "\"tak dikenal\".",
                    "",
                    "Kenapa -?*, bukan -* seperti yang sering ditulis orang? Pola -* juga",
                    "cocok dengan tanda strip sendirian. Padahal menurut kesepakatan Unix,",
                    "satu strip artinya \"baca dari stdin\" (cat - | ...), dan itu argumen yang",
                    "sah, bukan opsi yang salah ketik. -?* mewajibkan paling sedikit satu",
                    "karakter sesudah stripnya.",
                    "",
                    "Penanda dua strip (--) artinya \"opsi habis di sini\". Semua yang datang",
                    "sesudah tanda itu diperlakukan sebagai argumen biasa, walaupun diawali",
                    "strip. Ini ada gunanya: nama berkas boleh aja diawali strip, dan tanpa",
                    "penanda itu, alat yang kamu panggil bakal membacanya sebagai opsi.",
                    "",
                    "  rm -- \"$berkas\"             aman walaupun isi $berkas ternyata \"-rf\"",
                    "  grep -- \"-pola\" data.txt    cari teks '-pola', bukan opsi -p -o -l -a",
                    "  git checkout -- berkas.txt  berkas.txt, bukan cabang bernama itu",
                    "",
                    "Biasakan menaruh penanda itu di tiap perintah yang menerima nama berkas",
                    "dari variabel atau dari input orang lain. Pengaman ini gratis, dan sesekali",
                    "bakal menyelamatkanmu.",
                    "",
                    "Teks di bantuan() dan daftar opsi itu dua tempat yang ngomongin hal",
                    "yang sama. Masalahnya, string \":hvo:\" (atau daftar cabang case) dan",
                    "bantuan() nggak saling ngecek. Kalau isinya beda, nggak ada yang error.",
                    "Pengguna baca -q di bantuan, mencobanya, lalu dibalas \"opsi tak",
                    "dikenal\". Aturannya sederhana: tiap kali kamu nambah satu huruf ke",
                    "daftar opsi, tambahkan juga satu baris ke bantuan() saat itu juga,",
                    "sebelum ngetik apa pun yang lain.",
                    "",
                    "Bedakan juga dua keadaan ini, karena sering ketuker:",
                    "  - Pengguna minta bantuan (-h): cetak ke stdout, lalu exit 0. Dia",
                    "    dapat yang dia minta.",
                    "  - Pengguna salah memanggil: kirim pesan ke stderr, lalu exit 2. Ini",
                    "    kegagalan.",
                    "",
                    "Kalau bantuan karena salah panggil dicetak ke stdout dengan exit 0,",
                    "script lain yang memanggil script-mu bakal ngira semuanya beres, lalu",
                    "lanjut dengan data kosong.",
                    "",
                    "Daftar periksa waktu membaca blok opsi di script orang lain:",
                    "  1. Huruf apa aja yang diterima, dan mana yang butuh nilai? Lihat titik",
                    "     duanya.",
                    "  2. Ada shift $((OPTIND - 1)) atau nggak? Kalau nggak ada, $1",
                    "     sesudahnya masih berupa opsi.",
                    "  3. Opsi yang nggak dikenal ditolak atau didiamkan?",
                    "  4. Apa nilai bawaan tiap variabel sebelum perulangan? Itulah perilaku",
                    "     script kalau dipanggil tanpa opsi.",
                ],
            },
        ],
    },
    {
        "title": "15. Pola: Glob dan Regex",
        "sections": [
            {
                "body": [
                    "Pola adalah cara menulis \"teks yang bentuknya kira-kira begini\". Di bash",
                    "ada dua bahasa pola yang beda. Bentuknya mirip, tapi artinya nggak sama,",
                    "dan dua-duanya paling sering ketuker.",
                    "",
                    "Glob dipakai untuk nama berkas dan pencocokan sederhana:",
                    "  - nama berkas di baris perintah, misalnya ls *.txt atau rm foto?.jpg;",
                    "  - pola di dalam 'case ... in', yang udah kamu pakai di materi",
                    "    Percabangan;",
                    "  - operator == dan != di dalam [[ ]].",
                    "",
                    "Regex (regular expression) dipakai untuk isi teks:",
                    "  - operator =~ di dalam [[ ]];",
                    "  - grep, sed, dan awk.",
                    "",
                    "Jebakan yang paling sering kejadian ada di tanda bintang:",
                    "",
                    "  *  di GLOB  = 'apa saja, sepanjang apa pun, boleh kosong'",
                    "  *  di REGEX = 'nol kali atau lebih dari YANG TEPAT SEBELUMNYA'",
                    "",
                    "  ls data*          -> berkas yang namanya diawali 'data'",
                    "  grep 'data*' f    -> baris yang memuat 'dat' lalu nol atau lebih 'a'",
                    "                       jadi 'dat' saja sudah cocok. Bukan itu maksudmu.",
                    "",
                    "Tabel ini layak dihafal:",
                    "",
                    "  tanda   arti di GLOB                  arti di REGEX",
                    "  -----   ---------------------------   ----------------------------------",
                    "  *       apa saja, berapa pun          nol atau lebih dari yang sebelumnya",
                    "  ?       TEPAT satu karakter           yang sebelumnya boleh ada boleh tidak",
                    "  .       titik biasa, tidak istimewa   satu karakter apa pun",
                    "  [abc]   satu dari a, b, c             satu dari a, b, c  (SAMA)",
                    "  [!x]    apa pun kecuali x             di regex ditulis [^x]",
                    "  ^  $    huruf biasa                   awal baris dan akhir baris",
                    "",
                    "Daftar glob selengkapnya:",
                    "  *          nol karakter atau lebih, apa saja",
                    "  ?          tepat satu karakter",
                    "  [abc]      satu karakter: a, b, atau c",
                    "  [0-9]      satu karakter dalam rentang 0 sampai 9",
                    "  [a-z0-9]   rentang boleh digabung",
                    "  [!x]       apa pun KECUALI x    ([^x] juga jalan di bash)",
                    "",
                    "Brace expansion, yaitu kurung kurawal {}, sering dikira glob. Padahal",
                    "cara kerjanya lain:",
                    "  {jpg,png}   -> jpg png",
                    "  {1..5}      -> 1 2 3 4 5",
                    "  {01..03}    -> 01 02 03   (nol di depan ikut dipertahankan)",
                    "",
                    "Kurung kurawal diurai lebih dulu, dan nggak pernah melihat isi folder.",
                    "Makanya 'echo bab-{a,b}.md' tetap mencetak dua nama, walaupun berkasnya",
                    "nggak ada.",
                    "",
                    "Kalau nggak ada satu pun berkas yang cocok, bash menyerahkan polanya apa",
                    "adanya. Ini sumber bug yang klasik: 'for f in *.txt' tetap jalan satu",
                    "putaran, dengan f berisi teks '*.txt'. Penangkalnya ada di materi",
                    "Bekerja dengan File & Folder: [[ -e \"$f\" ]] || continue, atau",
                    "shopt -s nullglob.",
                    "",
                    "Tiga hal kecil yang bisa menghindarkan kamu dari banyak kebingungan:",
                    "  - Pola yang dikutip nggak diurai. ls \"*.txt\" mencari berkas yang",
                    "    namanya persis *.txt.",
                    "  - Berkas tersembunyi (namanya diawali titik) nggak pernah kena *.",
                    "  - Hasilnya diurutkan sebagai teks, bukan angka. Jadi foto10.jpg bisa",
                    "    muncul sebelum foto2.jpg.",
                ],
            },
            {
                "heading": "Glob di depan mata",
                "code": """#!/usr/bin/env bash
# Berkas di bawah ini dibuat sendiri oleh script, lalu dibereskan lagi di akhir.
mkdir -p contoh-pola
cd contoh-pola || exit 1
touch catatan.txt tugas.txt data.csv foto1.jpg foto2.jpg foto10.jpg

lihat() {                    # $1 = polanya apa adanya, sisanya = hasil mekarnya
    printf '%-16s -> %s\\n' "$1" "${*:2}"
}

echo "Isi folder: catatan.txt tugas.txt data.csv foto1.jpg foto2.jpg foto10.jpg"
echo
lihat '*.txt'         *.txt
lihat 'foto?.jpg'     foto?.jpg
lihat 'foto[0-9].jpg' foto[0-9].jpg
lihat '[cd]*'         [cd]*
lihat '[!cd]*'        [!cd]*
lihat '*.{jpg,csv}'   *.{jpg,csv}
lihat '*.pdf'         *.pdf

echo
echo "Sesudah 'shopt -s nullglob' pola tanpa hasil jadi daftar kosong:"
shopt -s nullglob
lihat '*.pdf'         *.pdf

echo
echo "Brace expansion tidak melihat isi folder sama sekali:"
echo "  {1..5}       ->" {1..5}
echo "  {01..03}     ->" {01..03}
echo "  bab-{a,b}.md ->" bab-{a,b}.md

echo
berkas="catatan.txt"
if [[ "$berkas" == *.txt ]]; then
    echo "[[ == ]] memakai glob  : '$berkas' berakhiran .txt"
fi
if [[ "$berkas" == "*.txt" ]]; then
    echo "polanya dikutip        : cocok"
else
    echo "polanya dikutip        : TIDAK cocok, jadi nama harfiah '*.txt'"
fi
case "$berkas" in
    *.txt) echo "case juga memakai glob : berkas teks" ;;
    *)     echo "case juga memakai glob : bukan berkas teks" ;;
esac

rm -f catatan.txt tugas.txt data.csv foto1.jpg foto2.jpg foto10.jpg
cd ..
rmdir contoh-pola""",
            },
            {
                "body": [
                    "Sekarang regex. Begitu kosakatanya kamu kuasai, regex bisa dipakai di",
                    "=~, grep, sed, awk, dan hampir semua bahasa pemrograman lain yang bakal",
                    "kamu temui.",
                    "",
                    "Penjangkar menunjuk posisi, bukan karakter:",
                    "  ^      awal baris.   ^andi cocok kalau baris DIMULAI dengan andi",
                    "  $      akhir baris.  txt$ cocok kalau baris DIAKHIRI txt",
                    "  ^...$  dipakai berpasangan artinya: SELURUH teks harus persis begini",
                    "",
                    "Karakter, masing-masing mewakili satu huruf:",
                    "  .          satu karakter apa pun",
                    "  [abc]      satu dari a, b, c",
                    "  [^abc]     satu karakter selain a, b, c   (regex pakai ^, glob pakai !)",
                    "  [a-z0-9]   rentang, boleh digabung",
                    "  \\          matikan arti khusus karakter sesudahnya",
                    "",
                    "Tanda pengulangan selalu berlaku untuk karakter atau grup yang ada",
                    "tepat di sebelah kirinya:",
                    "  *      nol kali atau lebih",
                    "  +      satu kali atau lebih",
                    "  ?      nol atau satu kali (boleh ada, boleh tidak)",
                    "  {3}    tepat 3 kali",
                    "  {2,}   2 kali atau lebih",
                    "  {2,5}  antara 2 sampai 5 kali",
                    "",
                    "  ab*     -> a, ab, abbb        yang diulang cuma huruf b",
                    "  (ab)*   -> kosong, ab, ababab   yang diulang seluruh grup",
                    "",
                    "Sebagian besar regex yang rusak berasal dari salah membaca \"hal yang",
                    "sebelumnya\" ini.",
                    "",
                    "Grup dan pilihan:",
                    "  ( )    kelompokkan, sekaligus TANGKAP isinya supaya bisa diambil lagi",
                    "  |      atau.  ^(ya|tidak)$ cocok untuk 'ya' maupun 'tidak'",
                    "",
                    "Jebakan paling mahal di regex adalah titik:",
                    "  ^data.txt$    dibaca 'data', SATU KARAKTER APA PUN, lalu 'txt'.",
                    "                Jadi dataXtxt dan data-txt ikut dianggap cocok.",
                    "  ^data\\.txt$   barulah berarti titik yang sungguhan titik.",
                    "",
                    "Pola yang lupa di-escape nggak error dan nggak protes. Dia cuma",
                    "menerima terlalu banyak, dan kesalahannya baru ketahuan lama kemudian.",
                    "Karakter yang perlu di-escape kalau maksudnya karakter itu sendiri:",
                    "  . * + ? ( ) [ ] { } | ^ $ \\",
                    "",
                    "Ada juga kelas siap pakai, ditulis dengan kurung siku berlapis:",
                    "  [[:digit:]]   angka         setara [0-9]",
                    "  [[:alpha:]]   huruf         setara [A-Za-z]",
                    "  [[:alnum:]]   huruf & angka",
                    "  [[:space:]]   spasi, tab, baris baru",
                    "  [[:upper:]] [[:lower:]] [[:punct:]]",
                    "",
                    "Kurung siku luar tetap kurung siku kelas karakter. Jadi \"angka atau",
                    "titik\" ditulis [[:digit:].], bukan [:digit:.].",
                    "",
                    "Bedanya dengan [0-9]: kelas POSIX ikut aturan bahasa yang dipakai",
                    "sistem, sedangkan [0-9] selalu persis sepuluh angka ASCII itu aja.",
                ],
            },
            {
                "heading": "Regex di dalam [[ =~ ]]",
                "code": """#!/usr/bin/env bash

cocok() {                       # $1 = teks yang diuji, $2 = polanya
    local teks="$1" pola="$2"
    if [[ "$teks" =~ $pola ]]; then
        printf '  %-10s ~ %-24s COCOK\\n' "$teks" "$pola"
    else
        printf '  %-10s ~ %-24s tidak\\n' "$teks" "$pola"
    fi
}

angka='^[0-9]+$'
echo "Seluruh teks harus angka:"
cocok "2024"  "$angka"
cocok "20a4"  "$angka"
cocok "12 34" "$angka"
cocok ""      "$angka"

echo
echo "Titik tanpa backslash cocok dengan KARAKTER APA SAJA:"
cocok "dataXtxt" '^data.txt$'
cocok "dataXtxt" '^data\\.txt$'
cocok "data.txt" '^data\\.txt$'

echo
nama='^[A-Za-z_][A-Za-z0-9_]*$'
echo "Pola nama variabel, hasil mengubah pola angka tadi:"
cocok "hitung"   "$nama"
cocok "_tmp2"    "$nama"
cocok "2hitung"  "$nama"
cocok "hitung-2" "$nama"

echo
echo "Grup ( ) menyimpan potongannya ke BASH_REMATCH:"
tanggal="2024-05-17"
if [[ "$tanggal" =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})$ ]]; then
    echo "  utuh    : ${BASH_REMATCH[0]}"
    echo "  tahun   : ${BASH_REMATCH[1]}"
    echo "  bulan   : ${BASH_REMATCH[2]}"
    echo "  tanggal : ${BASH_REMATCH[3]}"
fi

echo
echo "Pola yang DIKUTIP berhenti jadi regex:"
if [[ "2024" =~ "^[0-9]+$" ]]; then
    echo "  cocok"
else
    echo "  tidak cocok -- yang dicari jadi teks harfiah: ^[0-9]+\\$"
fi""",
            },
            {
                "heading": "Satu regex, dua dialek: BRE dan ERE",
                "body": [
                    "Ada tiga aturan dari contoh tadi yang sering bikin orang buntu:",
                    "  - Polanya nggak boleh dibungkus petik ganda. Begitu dikutip, bash",
                    "    membacanya sebagai teks biasa, dan =~ jadi cuma pembanding string.",
                    "  - Teks di sebelah kiri justru sebaiknya dikutip, seperti biasa.",
                    "  - Cara yang paling aman dan paling enak dibaca: taruh pola di",
                    "    variabel, lalu pakai variabel itu tanpa kutip. Itu yang dilakukan",
                    "    fungsi cocok() di atas.",
                    "",
                    "Sekarang soal backslash-backslash aneh di kode orang lain. grep dan sed",
                    "lahir sebelum regex punya bentuk baku, jadi ada dua dialek:",
                    "",
                    "  BRE (Basic Regular Expression) - mode bawaan grep dan sed",
                    "      + ? { } ( ) | TIDAK istimewa. Supaya jadi metakarakter harus di-escape:",
                    "      \\+   \\?   \\{2,\\}   \\(   \\)   \\|",
                    "  ERE (Extended Regular Expression) - grep -E, sed -E, dan awk",
                    "      + ? { } ( ) | langsung istimewa, tanpa backslash sama sekali.",
                    "",
                    "Metakarakter adalah karakter yang punya arti khusus di dalam pola.",
                    "",
                    "Jadi dua baris ini artinya sama persis:",
                    "  grep 'a\\+' berkas",
                    "  grep -E 'a+' berkas",
                    "",
                    "Di BRE, backslash rasanya terbalik: \\( artinya grup, sedangkan ( cuma",
                    "kurung biasa. Di ERE justru kebalikannya. Makanya pola yang disalin dari",
                    "contoh grep sering nggak jalan begitu ditempel ke awk, dan sebaliknya.",
                    "",
                    "  bash [[ =~ ]]  -> ERE",
                    "  awk            -> ERE, tidak punya mode lain",
                    "  grep dan sed   -> BRE, kecuali diberi -E",
                    "",
                    "Catatan: \\+, \\?, dan \\| di BRE itu tambahan GNU, bukan bagian dari",
                    "POSIX. Di grep bawaan macOS atau BusyBox, belum tentu ada. Kalau ragu,",
                    "pakai -E.",
                    "",
                    "Pola dibangun sedikit demi sedikit, jangan disalin bulat-bulat. Naikkan",
                    "setingkat demi setingkat:",
                    "  ^[0-9]+$                  seluruh teks angka semua",
                    "  ^-?[0-9]+$                boleh ada tanda minus di depan",
                    "  ^-?[0-9]+(\\.[0-9]+)?$     boleh berdesimal, dan bagian desimalnya opsional",
                    "  ^[A-Za-z_][A-Za-z0-9_]*$  nama variabel: huruf/_ dulu, sisanya bebas",
                    "",
                    "Pola terakhir menjelaskan karakter pertama dan sisanya secara terpisah.",
                    "Cara berpikir seperti itu bakal sering kamu pakai di regex sungguhan.",
                    "",
                    "Di bawah, pola yang sama dijalankan lewat grep, sed, dan awk. Tiga alat",
                    "itu dibahas lengkap di materi berikutnya. Yang berubah cuma alatnya,",
                    "polanya tetap.",
                ],
                "code": """#!/usr/bin/env bash

cat > pengguna.txt << 'EOF'
andi 3 aktif
budi 12 nonaktif
citra 7 aktif
dedi 100 aktif
EOF

echo "== Baris yang angkanya 2 digit atau lebih =="
echo "-- ERE : grep -E '[0-9]{2,}'"
grep -E '[0-9]{2,}' pengguna.txt
echo "-- BRE : grep '[0-9]\\{2,\\}'"
grep '[0-9]\\{2,\\}' pengguna.txt

echo
echo "== Tukar kolom 1 dan 2 =="
echo "-- ERE : sed -E 's/^([a-z]+) ([0-9]+)/\\2 \\1/'"
sed -E 's/^([a-z]+) ([0-9]+)/\\2 \\1/' pengguna.txt
echo "-- BRE : sed 's/^\\([a-z]\\+\\) \\([0-9]\\+\\)/\\2 \\1/'"
sed 's/^\\([a-z]\\+\\) \\([0-9]\\+\\)/\\2 \\1/' pengguna.txt

echo
echo "== awk selalu ERE, tidak punya mode lain =="
awk '$3 ~ /^aktif$/ { print $1, $2 }' pengguna.txt

echo
echo "== Kelas POSIX: isinya sama, bacanya lebih jelas =="
grep -E '^[[:alpha:]]+ [[:digit:]]+ [[:alpha:]]+$' pengguna.txt

rm -f pengguna.txt""",
            },
        ],
    },
    {
        "title": "16. Operasi String",
        "sections": [
            {
                "body": [
                    "Bash punya banyak operasi string bawaan lewat ${}. Cara ini lebih cepat",
                    "daripada memanggil program luar seperti sed.",
                    "",
                    "Panjang string:",
                    "  ${#teks}",
                    "",
                    "Menyambung string:",
                    "  lengkap=\"$depan $belakang\"    rakit langsung di dalam petik",
                    "  pesan=\"Halo\"",
                    "  pesan+=\" dunia\"               tempel di BELAKANG isi yang ada",
                    "",
                    "Tanda += di situ adalah arti ketiga dari tanda yang sama. Di dalam",
                    "(( )), += menjumlahkan angka. Di array, += menambah elemen. Di string",
                    "biasa, += menempel teks. Yang menentukan artinya adalah jenis",
                    "variabelnya, bukan isinya. Variabel biasa yang kebetulan isinya angka",
                    "tetap ditempel, nggak dijumlahkan: n=0 lalu n+=1 hasilnya \"01\", bukan",
                    "1. Cara bikin variabel yang dihitung sebagai angka ada di materi Fitur",
                    "Bash Lanjutan.",
                    "",
                    "+= paling sering dipakai untuk mengumpulkan hasil di dalam perulangan,",
                    "sepotong demi sepotong. Bentuk ${kata:i:1} di bawah ini dijelaskan di",
                    "bagian Substring, tepat sesudah blok ini:",
                    "  terbalik=\"\"",
                    "  for (( i = ${#kata} - 1; i >= 0; i-- )); do",
                    "      terbalik+=\"${kata:i:1}\"",
                    "  done",
                    "",
                    "Substring, yaitu potongan dari sebuah string:",
                    "  ${teks:4}       mulai indeks 4 sampai akhir",
                    "  ${teks:0:5}     mulai indeks 0, ambil 5 karakter",
                    "  ${teks: -3}     3 karakter terakhir (perhatikan spasi!)",
                    "",
                    "Indeks dihitung dari 0, jadi karakter pertama ada di indeks 0.",
                    "",
                    "Mengganti isi:",
                    "  ${teks/lama/baru}    ganti kemunculan PERTAMA",
                    "  ${teks//lama/baru}   ganti SEMUA kemunculan",
                    "  ${teks/#awal/baru}   ganti kalau ada di awal",
                    "  ${teks/%akhir/baru}  ganti kalau ada di akhir",
                    "",
                    "Membuang pola:",
                    "  ${berkas%.txt}       buang '.txt' dari akhir (terpendek)",
                    "  ${berkas%%.*}        buang dari titik pertama (terpanjang)",
                    "  ${jalur#*/}          buang sampai '/' pertama dari awal",
                    "  ${jalur##*/}         buang sampai '/' terakhir -> nama file",
                    "",
                    "Mengubah huruf besar dan kecil (butuh bash 4 ke atas):",
                    "  ${teks^^}   SEMUA HURUF BESAR",
                    "  ${teks,,}   semua huruf kecil",
                    "  ${teks^}    Huruf pertama besar",
                ]
            },
            {
                "heading": "Contoh praktis",
                "code": """#!/usr/bin/env bash

teks="Belajar Bash Itu Seru"

echo "Panjang  : ${#teks}"
echo "Potong   : ${teks:0:7}"
echo "Ganti    : ${teks/Bash/Shell}"
echo "Besar    : ${teks^^}"
echo "Kecil    : ${teks,,}"

berkas="/home/andi/laporan.tar.gz"
echo "Nama file  : ${berkas##*/}"
echo "Folder     : ${berkas%/*}"
echo "Tanpa .gz  : ${berkas%.gz}"
echo "Tanpa ext  : ${berkas%%.*}"

# Nilai bawaan kalau variabel kosong
echo "Halo, ${nama_belum_ada:-Tamu}" """
            },
            {
                "body": [
                    "Nilai bawaan dan pemeriksaan isi:",
                    "  ${var:-bawaan}   pakai 'bawaan' KALAU var kosong",
                    "  ${var:=bawaan}   sama, TAPI sekalian set var-nya",
                    "  ${var:?pesan}    error dengan 'pesan' kalau var kosong",
                    "  ${var:+isi}      pakai 'isi' KALAU var TIDAK kosong",
                    "",
                    "Bentuk ini berguna banget untuk konfigurasi:",
                    "  PORT=\"${PORT:-8080}\"",
                    "",
                    "Artinya: pakai PORT dari environment, dan kalau nggak ada, pakai 8080.",
                    "",
                    "Mencocokkan string dengan regex:",
                    "  if [[ \"$email\" =~ ^[a-z]+@[a-z]+\\.[a-z]+$ ]]; then",
                    "      echo \"Format email valid\"",
                    "  fi",
                    "",
                    "Bagian yang ditangkap grup (bagian pola di dalam kurung) disimpan di",
                    "array BASH_REMATCH:",
                    "  ${BASH_REMATCH[0]} seluruh yang cocok",
                    "  ${BASH_REMATCH[1]} grup pertama",
                ]
            },
        ],
    },
    {
        "title": "17. Bekerja dengan File & Folder",
        "sections": [
            {
                "body": [
                    "Ini perintah dasar yang paling sering dipakai di script:",
                    "",
                    "  ls        daftar isi folder",
                    "  cd        pindah folder",
                    "  pwd       tampilkan folder saat ini",
                    "  ls -l     daftar lengkap: izin, pemilik, ukuran, waktu ubah",
                    "  cd -      balik ke folder yang barusan ditinggalkan",
                    "  pushd     pindah folder TAPI ingat yang lama (ditumpuk)",
                    "  popd      balik ke folder yang tadi ditumpuk pushd",
                    "  mkdir -p  buat folder (termasuk induknya)",
                    "  cp -r     salin (r = termasuk isi folder)",
                    "  mv        pindah atau ganti nama",
                    "  rm -rf    hapus paksa (BERBAHAYA, cek dua kali!)",
                    "  touch     buat file kosong / ubah waktu akses",
                    "  cat       tampilkan isi file",
                    "  head -n 5 5 baris pertama",
                    "  tail -n 5 5 baris terakhir",
                    "  wc -l     hitung jumlah baris",
                    "  find      cari file berdasarkan kriteria",
                    "  grep      cari teks di dalam file",
                    "  sed       ganti teks",
                    "  awk       olah data per kolom",
                    "  sort      urutkan baris",
                    "  uniq      hilangkan duplikat berurutan",
                    "  cut       ambil kolom tertentu",
                    "  basename  dari sebuah jalur, ambil nama berkasnya saja",
                    "  dirname   dari sebuah jalur, ambil foldernya saja",
                    "  realpath  jadikan jalur mutlak, .. dan symlink dibereskan",
                    "  chmod     ubah izin berkas",
                    "  tee       tulis ke berkas SEKALIGUS tampilkan ke layar",
                    "  tr        tukar atau buang karakter, misalnya spasi jadi baris baru",
                    "",
                    "Contoh basename dan dirname:",
                    "  basename /home/andi/laporan.txt   -> laporan.txt",
                    "  dirname  /home/andi/laporan.txt   -> /home/andi",
                    "",
                    "Bash punya padanan bawaan untuk basename dan dirname, yaitu ${jalur##*/}",
                    "dan ${jalur%/*} dari materi Operasi String. Bentuk bawaan lebih cepat,",
                    "karena nggak memanggil program luar. basename dan dirname lebih enak",
                    "dibaca. Dua-duanya lazim dipakai.",
                ]
            },
            {
                "heading": "Script pemrosesan file",
                "code": """#!/usr/bin/env bash
set -euo pipefail

folder="${1:-.}"

if [[ ! -d "$folder" ]]; then
    echo "Folder tidak ada: $folder" >&2
    exit 1
fi

jumlah=0
total_baris=0

for berkas in "$folder"/*.txt; do
    # Kalau tidak ada file .txt, pola tidak berkembang
    [[ -e "$berkas" ]] || continue

    baris=$(wc -l < "$berkas")
    nama="${berkas##*/}"
    printf "%-25s %5d baris\\n" "$nama" "$baris"

    ((jumlah++))
    ((total_baris += baris))
done

echo "---"
echo "$jumlah file, total $total_baris baris" """
            },
            {
                "body": [
                    "Perhatikan baris ini:",
                    "  [[ -e \"$berkas\" ]] || continue",
                    "",
                    "Kalau nggak ada berkas .txt sama sekali, bash ngasih pola mentah",
                    "'*.txt' sebagai nama berkas. Pemeriksaan -e mencegah script memproses",
                    "nama berkas palsu itu.",
                    "",
                    "Cara lain: nyalakan nullglob di awal script.",
                    "  shopt -s nullglob",
                    "",
                    "Dengan nullglob, pola yang nggak cocok dengan apa pun jadi daftar",
                    "kosong.",
                    "",
                    "Membuat berkas sementara dengan aman:",
                    "  tmp=$(mktemp)",
                    "  trap 'rm -f \"$tmp\"' EXIT",
                    "",
                    "mktemp bikin berkas baru dengan nama acak yang dijamin belum dipakai.",
                    "trap menjalankan perintah waktu script berakhir, termasuk kalau",
                    "dihentikan di tengah jalan. Ini cara yang benar untuk membersihkan",
                    "berkas sementara supaya nggak menumpuk.",
                    "",
                    "EXIT cuma satu dari sekumpulan kejadian yang bisa ditangkap trap. Yang",
                    "juga sering dipakai:",
                    "  INT    pemakai menekan Ctrl-C",
                    "  TERM   permintaan berhenti baik-baik, misalnya dari kill",
                    "  ERR    ada perintah yang gagal",
                    "",
                    "Kamu boleh nyebut beberapa sekaligus:",
                    "  trap bersihkan EXIT INT TERM",
                    "",
                    "Detailnya ada di materi Proses Latar Belakang, Sinyal, dan trap.",
                    "",
                    "Perhatikan juga bentuk di contoh atas:",
                    "  baris=$(wc -l < \"$berkas\")",
                    "",
                    "Kenapa pakai <, bukan wc -l \"$berkas\"? Soalnya hasilnya beda:",
                    "  wc -l catatan.txt    ->  3 catatan.txt     angka DAN nama berkas",
                    "  wc -l < catatan.txt  ->  3                 angkanya saja",
                    "",
                    "Dengan <, wc nggak pernah tahu nama berkasnya. Dia cuma menerima isinya",
                    "lewat stdin, jadi nggak ada nama yang bisa ikut dicetak. Kalau angkanya",
                    "mau kamu hitung atau cetak sendiri, selalu pakai bentuk <. Bentuk tanpa",
                    "< malah berguna waktu kamu memang mau namanya ikut, misalnya wc -l *.txt",
                    "untuk membandingkan banyak berkas.",
                ]
            },
        ],
    },
    {
        "title": "18. find, xargs, dan Pemrosesan Massal",
        "sections": [
            {
                "body": [
                    "Sejauh ini kamu nyari berkas pakai pola glob, misalnya for berkas in",
                    "*.txt. Glob cuma melihat satu tingkat folder. Begitu berkasnya tersebar",
                    "di dalam subfolder, dan subfolder di dalamnya lagi, glob udah nggak bisa",
                    "bantu.",
                    "",
                    "find menyusuri seluruh pohon folder, lalu menyaring hasilnya pakai",
                    "predikat. Predikat adalah syarat yang harus dipenuhi sebuah berkas",
                    "supaya ikut ditampilkan.",
                    "",
                    "  find <tempat mulai> <predikat...>",
                    "  find .           -> semua isi folder ini sampai ke dasar, tanpa saringan",
                    "",
                    "Predikat yang paling sering dipakai:",
                    "",
                    "  -type f          berkas biasa",
                    "  -type d          folder",
                    "  -type l          symlink",
                    "  -name '*.log'    NAMA cocok pola glob (huruf besar/kecil dibedakan)",
                    "  -iname '*.LOG'   sama, tapi abaikan besar/kecil huruf",
                    "  -path '*/log/*'  yang dicocokkan JALUR lengkapnya, bukan cuma nama berkasnya",
                    "  -maxdepth 2      jangan turun lebih dari 2 tingkat",
                    "  -mindepth 1      lewati titik awalnya sendiri",
                    "  -size +10M       lebih besar dari 10 MB (+ lebih dari, - kurang dari, k/M/G)",
                    "  -empty           berukuran nol",
                    "  -mtime +7        terakhir diubah lebih dari 7 hari lalu (-7 = kurang dari)",
                    "  -mmin -30        terakhir diubah kurang dari 30 menit lalu",
                    "  -newer patokan   lebih baru daripada berkas bernama 'patokan'",
                    "  -user levi       milik pemakai tertentu",
                    "",
                    "Catatan soal -mtime: find menghitung umur berkas dalam hari utuh, dan",
                    "pecahan harinya dibuang. Jadi -mtime +7 baru cocok untuk berkas yang",
                    "terakhir diubah paling sedikit 8 x 24 jam yang lalu.",
                    "",
                    "Jebakan pertama, dan hampir semua orang pernah kena: petik di -name.",
                    "",
                    "  find . -name *.log      SALAH",
                    "  find . -name '*.log'    BENAR",
                    "",
                    "Tanpa petik, *.log diurai duluan oleh shell (lihat materi Variabel &",
                    "Quoting), jadi find nggak pernah melihat polanya.",
                    "",
                    "Kalau di folder saat ini kebetulan ada satu berkas .log, find menerima",
                    "nama berkas itu sebagai polanya. Semua .log di subfolder dilewatkan",
                    "begitu aja, tanpa satu pun pesan error. Ini bug yang paling susah",
                    "dicari: perintahnya sukses, tapi angkanya salah.",
                    "",
                    "Kalau ada dua berkas .log atau lebih, find berhenti dengan pesan ini:",
                    "  find: paths must precede expression: 'c.log'",
                    "  find: possible unquoted pattern after predicate '-name'?",
                    "",
                    "Baris kedua itu yang menunjuk penyebab aslinya. Masalahnya udah terjadi",
                    "sebelum find sempat jalan.",
                    "",
                    "Predikat bisa digabung:",
                    "  -a          DAN  (boleh dihilangkan: dua predikat berdampingan sudah DAN)",
                    "  -o          ATAU",
                    "  !           BUKAN",
                    "  \\( ... \\)   tanda kurung untuk mengatur urutan",
                    "",
                    "  find . -type f -name '*.sh' -o -name '*.md'",
                    "",
                    "Baris di atas dibaca (berkas dan *.sh) atau (*.md). Jadi folder yang",
                    "namanya berakhiran .md ikut kena.",
                    "",
                    "  find . -type f \\( -name '*.sh' -o -name '*.md' \\)",
                    "",
                    "Baru baris ini yang kamu maksud: berkas biasa yang namanya *.sh atau",
                    "*.md.",
                    "",
                    "Kurungnya wajib di-escape. ( dan ) tanpa backslash itu sintaks subshell",
                    "milik bash, jadi find nggak bakal pernah melihatnya. Bentuk '(' yang",
                    "dikasih petik juga sah.",
                    "",
                    "Terakhir, ini sering bikin heran: urutan hasil find nggak dijamin.",
                    "Urutannya ngikutin susunan direktori di sistem berkas, yang bisa beda di",
                    "tiap mesin. Kalau urutannya penting, sambung dengan | sort seperti di",
                    "contoh berikut.",
                ],
            },
            {
                "heading": "find dengan berbagai predikat",
                "code": """#!/usr/bin/env bash
set -euo pipefail

# Pohon contohnya dibuat sendiri supaya contoh ini bisa dijalankan apa adanya.
kerja=$(mktemp -d)
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

mkdir -p proyek/src proyek/log arsip
echo "halo"          > proyek/src/utama.sh
echo "dunia"         > proyek/src/bantu.sh
echo "judul"         > proyek/README.md
printf 'a\\nb\\nc\\n' > proyek/log/server.log
: > proyek/log/kosong.log
: > "arsip/laporan akhir.txt"
echo "isi lama"      > arsip/lama.log
echo "isi baru"      > arsip/baru.log
echo "penanda"       > patokan

# Waktunya dipatok supaya hasil -newer selalu sama, bukan ikut jam mesin.
touch -d '2020-01-01' arsip/lama.log "arsip/laporan akhir.txt"
touch -d '2022-01-01' patokan
touch -d '2024-01-01' arsip/baru.log

echo "== semua berkas .log di bawah proyek =="
find proyek -type f -name '*.log' | sort

echo
echo "== folder saja, cuma satu tingkat =="
find proyek -maxdepth 1 -type d | sort

echo
echo "== .sh ATAU .md, tapi bukan README =="
find proyek -type f \\
     \\( -name '*.sh' -o -name '*.md' \\) ! -name 'README.md' | sort

echo
echo "== berkas berukuran nol =="
find proyek arsip -type f -empty | sort

echo
echo "== lebih baru daripada berkas 'patokan' =="
find arsip -type f -newer patokan | sort""",
            },
            {
                "body": [
                    "find nggak cuma bisa mencetak nama. find juga bisa menjalankan sesuatu",
                    "untuk tiap hasil, dan bentuknya ada dua.",
                    "",
                    "  -exec perintah {} \\;",
                    "",
                    "Di sini {} diganti nama berkas yang ketemu, dan perintahnya dipanggil",
                    "sekali untuk tiap berkas. Seribu berkas berarti seribu proses.",
                    "Hasilnya benar, tapi lambat.",
                    "",
                    "  -exec perintah {} +",
                    "",
                    "Di sini nama-nama berkas ditumpuk jadi satu daftar panjang, dan",
                    "perintahnya dipanggil sesedikit mungkin, biasanya cukup sekali. Bentuk",
                    "ini yang kamu mau untuk grep, wc, rm, dan chmod.",
                    "",
                    "Titik koma di bentuk pertama di-escape karena ; adalah pemisah perintah",
                    "milik bash. Tanpa \\, bash memotong barisnya di situ, dan find nggak",
                    "pernah tahu bagian -exec-nya udah selesai. Bentuk ';' yang dikasih",
                    "petik juga sah. Tanda + nggak perlu diapa-apain.",
                    "",
                    "Ada juga -delete, yang menghapus berkas yang ketemu tanpa memanggil rm.",
                    "",
                    "Kebiasaan yang bisa menyelamatkanmu: jalankan find-nya tanpa aksi dulu.",
                    "",
                    "  find . -name '*.tmp'            <- lihat dulu daftar korbannya",
                    "  find . -name '*.tmp' -delete    <- baru hapus, kalau daftarnya memang benar",
                    "",
                    "-delete nggak nanya dulu, nggak bisa dibatalkan, dan nggak punya tempat",
                    "sampah. Satu salah ketik di polanya udah cukup bikin berkas yang salah",
                    "ikut terhapus. Taruh juga -delete di paling belakang. find membaca",
                    "predikat dari kiri ke kanan, jadi 'find . -delete -name x' menghapus",
                    "dulu, baru nyaring belakangan.",
                    "",
                    "Sekarang xargs. Cara kerjanya beda dengan pipe biasa:",
                    "",
                    "  echo berkas.txt | cat          cat menerima TEKS 'berkas.txt' di stdin",
                    "                                 lalu mencetak teks itu. Berkasnya tak dibuka.",
                    "  echo berkas.txt | xargs cat    xargs menyusun perintah 'cat berkas.txt'",
                    "                                 lalu menjalankannya. Isi berkasnya keluar.",
                    "",
                    "Jadi pipe ngasih data ke stdin, sedangkan xargs mengubah data itu jadi",
                    "argumen. Banyak perintah (rm, mv, mkdir, chmod) sama sekali nggak",
                    "membaca stdin. Buat perintah seperti itu, xargs satu-satunya jalan.",
                    "",
                    "Opsi xargs yang perlu kamu kenal:",
                    "  -0        pemisahnya byte NUL, bukan spasi/baris. Pasangan dari -print0.",
                    "  -n 1      maksimal 1 argumen tiap panggilan (2, 3, ... juga boleh)",
                    "  -I{}      taruh argumennya di posisi {}; satu baris masukan per panggilan",
                    "  -P 4      jalankan 4 panggilan sekaligus. Cepat, tapi keluarannya bisa",
                    "            saling menyela dan urutannya tidak lagi terjamin.",
                    "  -r        jangan jalankan apa pun kalau masukannya kosong. Tanpa ini,",
                    "            GNU xargs tetap memanggil perintahnya sekali tanpa argumen.",
                    "",
                    "Pasangan pengaman untuk nama berkas yang ada spasinya:",
                    "  find . -name '*.log' -print0 | xargs -0 rm --",
                    "",
                    "Secara bawaan, xargs memotong masukannya di setiap spasi. Nama",
                    "'laporan akhir.log' jadi dua argumen, dan rm menghapus apa pun yang",
                    "kebetulan bernama 'laporan'. -print0 memisahkan nama dengan byte NUL,",
                    "satu-satunya byte yang nggak mungkin ada di dalam nama berkas. Lalu -0",
                    "nyuruh xargs memakai pemisah itu. Aturannya sama dengan yang udah kamu",
                    "pakai sejak \"$berkas\": nama boleh berisi spasi, dan kodemu harus tetap",
                    "benar.",
                    "",
                    "Kapan pakai yang mana? Kalau sumbernya memang find, -exec ... +",
                    "biasanya lebih pendek dan udah aman tanpa trik NUL. xargs lebih cocok",
                    "kalau sumbernya bukan find, misalnya keluaran grep -l atau isi sebuah",
                    "berkas daftar, atau kalau kamu butuh -P untuk kerja paralel.",
                ],
            },
            {
                "heading": "-exec, xargs, dan nama berkas berspasi",
                "code": """#!/usr/bin/env bash
set -euo pipefail

kerja=$(mktemp -d)
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

mkdir -p sampah
printf 'satu\\ndua\\n'          > "sampah/laporan akhir.log"
printf 'tiga\\n'                > "sampah/data mentah.log"
printf 'empat\\nlima\\nenam\\n' > sampah/rapi.log

echo "== -exec ... \\;  -> wc dipanggil 3 kali, tidak ada baris total =="
find sampah -type f -name '*.log' -exec wc -l {} \\; | sort

echo
echo "== -exec ... +   -> wc dipanggil SEKALI, muncul baris total =="
find sampah -type f -name '*.log' -exec wc -l {} + | sort

echo
echo "== xargs mengubah BARIS jadi ARGUMEN =="
printf 'apel\\njeruk\\nmangga\\n' | xargs echo "Buah:"

echo
echo "== -n 1 : satu argumen tiap panggilan =="
printf 'apel\\njeruk\\n' | xargs -n 1 echo "->"

echo
echo "== -I{} : argumennya ditaruh di posisi yang kamu pilih =="
printf 'apel\\njeruk\\n' | xargs -I{} echo "Aku suka {} sekali"

echo
echo "== SALAH: nama berspasi dipecah xargs jadi dua argumen =="
find sampah -type f -name '*.log' | xargs -n 1 echo "arg:" | sort

echo
echo "== BENAR: -print0 dipasangkan dengan -0 =="
find sampah -type f -name '*.log' -print0 | xargs -0 -n 1 echo "arg:" | sort

echo
echo "== hapus dengan aman, lalu hitung sisanya =="
find sampah -type f -name '*.log' -print0 | xargs -0 -r rm --
find sampah -type f | wc -l""",
            },
            {
                "heading": "Process substitution dan mapfile",
                "body": [
                    "Process substitution, yaitu <(perintah), berlaku persis seperti nama",
                    "berkas.",
                    "",
                    "Bash menjalankan perintahnya di latar belakang, lalu menyerahkan jalur",
                    "semu seperti /dev/fd/63 ke perintah luar. Perintah luar ngira dia",
                    "membuka berkas biasa. Jadi semua kasus \"perintah ini maunya berkas,",
                    "padahal yang aku punya cuma keluaran perintah lain\" beres dengan cara",
                    "ini.",
                    "",
                    "  diff <(sort a.txt) <(sort b.txt)   membandingkan tanpa 2 berkas sementara",
                    "  comm <(sort a.txt) <(sort b.txt)   melihat mana yang cuma ada di salah satu",
                    "",
                    ">(perintah) arahnya kebalikannya: apa yang ditulis ke situ jadi stdin",
                    "perintah itu. Contohnya: perintah > >(gzip > catatan.gz)",
                    "",
                    "Dua-duanya fitur bash, nggak ada di sh. Script dengan shebang #!/bin/sh",
                    "bakal gagal.",
                    "",
                    "Ini juga jawaban untuk jebakan pipe di materi Proses, source, dan",
                    "Subshell. Perulangan di sisi kanan pipe jalan di subshell, jadi variabel",
                    "yang diubah di dalamnya hilang begitu pipe selesai. Kalau sumbernya",
                    "berkas, obatnya < berkas. Kalau sumbernya perintah, obatnya ini:",
                    "",
                    "  while IFS= read -r baris; do ... done < <(perintah)",
                    "",
                    "Perhatikan spasi di antara < dan <(. Kalau dirapatkan jadi <<(, bash",
                    "langsung menolak dengan 'syntax error near unexpected token'.",
                    "",
                    "mapfile (nama lainnya readarray) mengisi array dari banyak baris",
                    "sekaligus:",
                    "  mapfile -t buah < daftar.txt",
                    "  mapfile -t berkas < <(find . -name '*.md' | sort)",
                    "",
                    "-t membuang karakter baris baru di ujung tiap item. Tanpa -t, tiap item",
                    "masih menyimpan \\n di belakangnya, dan perbandingan seperti",
                    "[[ ${buah[0]} == apel ]] gagal tanpa alasan yang kelihatan.",
                    "",
                    "mapfile butuh bash 4 ke atas. Kalau script-nya harus jalan di bash 3.2",
                    "bawaan macOS, pakai lagi while read dengan array+=(\"$baris\") di",
                    "dalamnya.",
                ],
                "code": """#!/usr/bin/env bash
set -euo pipefail

kerja=$(mktemp -d)
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

printf 'apel\\njeruk\\nmangga\\n'  > kiri.txt
printf 'apel\\nmangga\\npisang\\n' > kanan.txt

echo "== diff dua keluaran perintah, tanpa berkas sementara =="
diff <(sort kiri.txt) <(sort kanan.txt) || true

echo
echo "== comm: kolom 1 hanya kiri, 2 hanya kanan, 3 keduanya =="
comm <(sort kiri.txt) <(sort kanan.txt)

echo
echo "== SALAH: perulangan di kanan pipe, n hilang lagi =="
n=0
printf 'a\\nb\\nc\\n' | while IFS= read -r baris; do
    n=$((n + 1))
done
echo "n setelah pipe    = $n"

echo
echo "== BENAR: sumbernya perintah, dibaca lewat < <(...) =="
n=0
while IFS= read -r baris; do
    n=$((n + 1))
done < <(printf 'a\\nb\\nc\\n')
echo "n setelah < <(..) = $n"

echo
echo "== mapfile: isi berkas jadi array sekali jalan =="
mapfile -t buah < kiri.txt
echo "jumlah=${#buah[@]}  item ke-2=${buah[1]}"

echo
echo "== mapfile dari keluaran find =="
mapfile -t berkas < <(find . -maxdepth 1 -type f -name '*.txt' | sort)
printf 'berkas: %s\\n' "${berkas[@]}" """,
            },
        ],
    },
    {
        "title": "19. grep, sed, dan awk",
        "sections": [
            {
                "body": [
                    "grep, sed, dan awk adalah tiga alat klasik untuk mengolah teks. Begitu",
                    "kamu bisa pakai ketiganya, banyak pekerjaan script jadi jauh lebih",
                    "gampang.",
                    "",
                    "grep mencari baris yang cocok dengan sebuah pola:",
                    "  grep \"kata\" file.txt",
                    "  grep -i    abaikan huruf besar/kecil",
                    "  grep -v    tampilkan yang TIDAK cocok",
                    "  grep -n    tampilkan nomor baris",
                    "  grep -c    hitung jumlah baris yang cocok",
                    "  grep -r    cari rekursif di dalam folder",
                    "  grep -E    pakai regex diperluas (sama dengan egrep)",
                    "  grep -q    diam: tidak mencetak apa pun, cuma memberi exit code.",
                    "             Inilah bentuk yang dipakai sebagai KONDISI:",
                    "               if grep -q \"gagal\" app.log; then ... fi",
                    "  grep -l    cetak NAMA BERKAS yang cocok saja, bukan barisnya.",
                    "             Pasangan alami xargs: grep -rl \"TODO\" . | xargs wc -l",
                    "  grep -o    cetak bagian yang COCOK saja, bukan seluruh barisnya",
                    "  grep -w    cocokkan sebagai kata utuh; 'ada' tidak lagi kena 'adalah'",
                    "  grep -A2   ikut tampilkan 2 baris SESUDAH yang cocok",
                    "  grep -B2   ikut tampilkan 2 baris SEBELUM yang cocok",
                    "  grep -C2   dua-duanya, 2 baris di sekelilingnya",
                    "",
                    "Rekursif artinya ikut masuk ke semua subfolder.",
                    "",
                    "sed (stream editor) dipakai untuk mengganti teks:",
                    "  sed 's/lama/baru/' file      ganti pertama tiap baris",
                    "  sed 's/lama/baru/g' file     ganti SEMUA (g = global)",
                    "  sed -i 's/a/b/g' file        ubah file LANGSUNG",
                    "  sed -n '5p' file             cetak baris ke-5 saja",
                    "  sed '2d' file                hapus baris ke-2",
                    "  sed '/pola/d' file           hapus baris yang cocok pola",
                    "",
                    "awk dipakai untuk mengolah data yang berbentuk kolom:",
                    "  awk '{print $1}' file        cetak kolom pertama",
                    "  awk -F',' '{print $2}'       pemisah koma, cetak kolom 2",
                    "  awk '$3 > 100 {print $1}'    saring berdasarkan nilai kolom",
                    "  awk '{s += $2} END {print s}'  jumlahkan kolom 2",
                ]
            },
            {
                "heading": "Contoh gabungan",
                "code": """#!/usr/bin/env bash

# Buat data contoh
cat > nilai.csv << 'EOF'
andi,80,90
budi,70,65
citra,95,88
dedi,55,60
EOF

echo "== Semua data =="
cat nilai.csv

echo
echo "== Yang nilai pertamanya di atas 75 =="
awk -F',' '$2 > 75 {print $1, $2}' nilai.csv

echo
echo "== Rata-rata kolom 2 =="
awk -F',' '{jml += $2; n++} END {printf "%.2f\\n", jml/n}' nilai.csv

echo
echo "== Nama diurutkan =="
cut -d',' -f1 nilai.csv | sort

rm -f nilai.csv"""
            },
            {
                "body": [
                    "Perhatikan heredoc di contoh:",
                    "  cat > nilai.csv << 'EOF'",
                    "  ...isi...",
                    "  EOF",
                    "",
                    "Heredoc dipakai untuk menulis blok teks banyak baris ke berkas atau ke",
                    "sebuah perintah.",
                    "  << 'EOF'  dengan petik  -> isi apa adanya, $variabel TIDAK diproses",
                    "  << EOF    tanpa petik   -> $variabel DIPROSES",
                    "  <<- EOF   tanda minus   -> tab di awal baris diabaikan",
                    "",
                    "Kata penanda EOF boleh diganti kata lain, asal pembuka dan penutupnya",
                    "sama.",
                    "",
                    "Jangan ketuker dengan <<< (here-string) dari materi Aliran Data &",
                    "Deskriptor. Bedanya cuma jumlah tanda kurang-dari, jadi dua-duanya",
                    "gampang banget ketuker:",
                    "  <<  EOF      blok BANYAK baris, ditutup penanda di baris sendiri",
                    "  <<< \"teks\"   SATU string, ditulis di baris yang sama",
                    "",
                    "Dua-duanya sama-sama ngisi stdin sebuah perintah. Bedanya cuma seberapa",
                    "banyak teks yang diisikan.",
                    "",
                    "Variabel bawaan awk yang berguna:",
                    "  $0    seluruh baris",
                    "  $1..  kolom ke-n",
                    "  NF    jumlah kolom di baris ini",
                    "  NR    nomor baris saat ini",
                    "  FS    pemisah kolom input",
                    "  OFS   pemisah kolom output",
                    "",
                    "Contohnya:",
                    "  awk '{print NR, NF, $NF}' file",
                    "",
                    "Perintah itu mencetak nomor baris, jumlah kolom, dan kolom terakhir.",
                ]
            },
        ],
    },
    {
        "title": "20. Proses Latar Belakang, Sinyal, dan trap",
        "sections": [
            {
                "body": [
                    "Perintah biasa menahan shell. Kamu nggak dapat giliran lagi sampai",
                    "perintahnya selesai. Satu tanda & di ujung baris mengubah itu.",
                    "",
                    "  ./laporan.sh      shell menunggu sampai selesai, baru lanjut",
                    "  ./laporan.sh &    shell melepasnya, lalu LANGSUNG lanjut ke baris berikutnya",
                    "",
                    "Perintah yang dilepas begitu disebut berjalan di latar belakang.",
                    "",
                    "& dan && cuma beda satu huruf, tapi artinya sama sekali nggak",
                    "berhubungan:",
                    "",
                    "  a && b    jalankan b KALAU a sukses  (materi Argumen & Exit Code)",
                    "  a & b     lepas a ke latar belakang, lalu langsung jalankan b",
                    "",
                    "  mkdir data && cd data    benar",
                    "  mkdir data & cd data     bug: cd jalan tanpa menunggu mkdir selesai",
                    "",
                    "Salah ketik ini nggak pernah ngasih pesan error. Kadang jalan, kadang",
                    "gagal, tergantung mana yang kebetulan lebih cepat. Jadi kalau kamu",
                    "lihat satu & di tempat yang kamu kira &&, curigai itu duluan.",
                    "",
                    "Proses latar belakang tetap anak dari shell-mu (lihat materi Proses,",
                    "source, dan Subshell). Dia memakai layar yang sama, jadi keluarannya",
                    "tetap muncul, bercampur dengan keluaran lain, kadang di tengah baris.",
                    "Kalau ada beberapa proses, kasih masing-masing berkas log sendiri:",
                    "  ./tugas.sh satu > tugas-1.log 2>&1 &",
                    "  ./tugas.sh dua  > tugas-2.log 2>&1 &",
                    "",
                    "$! berisi PID proses latar belakang yang paling baru dilepas. Variabel",
                    "ini melengkapi keluarga variabel khusus dari materi Variabel & Quoting:",
                    "",
                    "  $?   kode keluar perintah terakhir       $#   jumlah argumen",
                    "  $@   semua argumen                       $$   PID script ini sendiri",
                    "  $!   PID proses latar belakang terakhir",
                    "",
                    "Simpan nilainya segera, karena satu & berikutnya langsung menimpanya:",
                    "  ./server.sh &",
                    "  pid=$!         <- wajib tepat di baris sesudahnya",
                    "",
                    "wait menahan script sampai anak-anaknya selesai:",
                    "",
                    "  wait           tunggu SEMUA proses latar belakang; kodenya selalu 0",
                    "  wait \"$pid\"    tunggu satu proses, dan $? jadi kode keluar proses ITU",
                    "  wait -n        tunggu yang mana pun selesai duluan (bash 4.3+)",
                    "",
                    "Perhatikan baris pertama: wait polos nggak pernah ngasih tahu kalau ada",
                    "yang gagal. Bahkan set -e pun diam soal proses latar belakang, karena",
                    "kegagalannya terjadi di proses lain, dan shell-mu nggak pernah",
                    "melihatnya. Satu-satunya cara untuk tahu: wait per PID, lalu periksa $?",
                    "sendiri, seperti di contoh berikutnya.",
                    "",
                    "Kalau nggak ada wait sama sekali, script yang selesai duluan",
                    "meninggalkan anak-anaknya setengah jalan. Hampir selalu, yang kamu mau",
                    "adalah wait.",
                    "",
                    "Ada tiga perintah pendamping yang cuma berguna di terminal interaktif,",
                    "bukan di script:",
                    "",
                    "  jobs      daftar pekerjaan shell ini, bernomor [1] [2] ...",
                    "  fg %1     tarik pekerjaan 1 kembali ke depan",
                    "  bg %1     lanjutkan pekerjaan yang sedang dijeda, kali ini di latar belakang",
                    "  Ctrl-Z    jeda pekerjaan yang sedang di depan, lalu pilih fg atau bg",
                    "",
                    "[1] itu nomor job, bukan PID. %1 dipakai jobs, fg, bg, dan kill,",
                    "sedangkan PID dari $! bisa dipakai di mana aja. Di dalam script, jobs",
                    "biasanya kosong dan fg nggak ada gunanya, karena nggak ada orang yang",
                    "nonton di \"depan\".",
                ],
            },
            {
                "heading": "Pola paralel: &, $!, lalu wait per-PID",
                "body": [
                    "Alasan utama orang berhenti mengerjakan sesuatu satu per satu: tiga",
                    "pemeriksaan yang masing-masing lambat nggak perlu antre. Perhatikan",
                    "urutan keluarannya. Yang dilepas pertama malah selesai terakhir, dan itu",
                    "bukti bahwa mereka jalan bareng.",
                ],
                "code": """#!/usr/bin/env bash
# Satu & di ujung baris = lepas ke latar belakang, lalu lanjut tanpa menunggu.

periksa() {
    local nama="$1" lama="$2" hasil="$3"
    sleep "$lama"                 # anggap ini kerja sungguhan yang lambat
    echo "  $nama selesai"
    return "$hasil"
}

host=("web-1" "web-2" "db-1")
lama=(1.2     0.4     0.8)
hasil=(0      0       3)          # db-1 sengaja dibuat gagal

pids=()
for i in "${!host[@]}"; do
    periksa "${host[i]}" "${lama[i]}" "${hasil[i]}" &
    pids+=("$!")                  # $! = PID yang BARU dilepas; simpan SEGERA
done

echo "tiga pemeriksaan jalan sekaligus, tidak ada yang ditunggu dulu"

gagal=0
for i in "${!pids[@]}"; do
    wait "${pids[i]}"             # tahan sampai proses ITU saja selesai
    kode=$?                       # dan $? jadi kode keluar proses itu
    if (( kode == 0 )); then
        echo "${host[i]} : sukses"
    else
        echo "${host[i]} : GAGAL (kode $kode)"
        gagal=1
    fi
done

echo "berurutan butuh 2,4 detik; cara ini selesai dalam 1,2 detik"
echo "ada yang gagal? $gagal"
# Di script sungguhan, baris penutupnya:  exit "$gagal"
""",
            },
            {
                "heading": "Sinyal: pesan sependek satu kata",
                "body": [
                    "Sinyal adalah pesan yang sangat pendek dari kernel ke sebuah proses.",
                    "Isinya cuma satu nama. Mirip ketukan pintu: proses yang diketuk masih",
                    "boleh siap-siap dulu, misalnya menyimpan pekerjaan atau menghapus berkas",
                    "sementara, sebelum berhenti.",
                    "",
                    "  Nama  Nomor  Datang dari                              Bisa ditangkap?",
                    "  INT     2    kamu menekan Ctrl-C                      ya",
                    "  TERM   15    kill tanpa opsi; permintaan yang sopan   ya",
                    "  HUP     1    terminal ditutup, sesi SSH putus         ya",
                    "  QUIT    3    Ctrl-\\                                   ya",
                    "  KILL    9    kill -9                                  TIDAK PERNAH",
                    "  STOP   19    jeda paksa                               TIDAK PERNAH",
                    "",
                    "KILL dan STOP nggak pernah sampai ke programnya. Kernel sendiri yang",
                    "mengerjakannya. Karena itu kill -9 nggak ngasih kesempatan program untuk",
                    "membereskan diri: berkas sementara tertinggal, berkas yang baru setengah",
                    "ditulis dibiarkan rusak, dan kunci nggak dilepas. Jadikan kill -9",
                    "pilihan terakhir.",
                    "",
                    "Cara mengirim sinyal:",
                    "",
                    "  kill 12345         kirim TERM (bawaan). Ini yang selalu dicoba pertama.",
                    "  kill -TERM 12345   sama saja, ditulis terang-terangan",
                    "  kill -9 12345      kirim KILL; sama dengan kill -KILL 12345",
                    "  kill -0 12345      TIDAK mengirim apa-apa, cuma cek 'masih ada atau tidak'",
                    "  kill -l            daftar semua nama sinyal di sistemmu",
                    "",
                    "Nama kill itu menyesatkan. Yang dikerjakan kill adalah mengirim sinyal,",
                    "dan sinyalnya belum tentu membunuh. Contohnya kill -0 di atas, yang",
                    "malah dipakai untuk memeriksa.",
                    "",
                    "Kalau yang kamu tahu cuma namanya, bukan PID-nya:",
                    "  pgrep -f 'server.py'   cetak PID semua proses yang cocok",
                    "  pkill -f 'server.py'   kirim TERM ke semuanya sekaligus",
                    "",
                    "Selalu jalankan pgrep dulu dan baca daftarnya, baru pkill. -f",
                    "mencocokkan seluruh baris perintah, bukan cuma nama programnya. Jadi",
                    "pola yang terlalu longgar bisa ikut membunuh editor atau terminal yang",
                    "kebetulan memuat kata itu di judulnya.",
                    "",
                    "Menutup terminal mengirim HUP ke semua yang jalan di dalamnya. Proses",
                    "latar belakang ikut mati. Makanya './lama.sh &' lalu logout sering",
                    "berakhir sia-sia, dan orang ngira script-nya yang rusak.",
                    "",
                    "  nohup ./lama.sh &                    kebal HUP; keluarannya ke nohup.out",
                    "  nohup ./lama.sh > jalan.log 2>&1 &   lebih rapi: tentukan sendiri lognya",
                    "  disown -h %1                         untuk yang TERLANJUR jalan tanpa nohup",
                    "",
                    "Untuk yang serius, misalnya harus hidup lagi sesudah mesin reboot,",
                    "pakai systemd, supervisor, atau tmux/screen. nohup nggak cukup untuk",
                    "itu.",
                    "",
                    "Proses yang mati karena sinyal nomor N memberi exit code 128 + N. Ini",
                    "angka-angka yang bakal sering kamu temui waktu membaca log atau hasil",
                    "CI:",
                    "",
                    "  130 = 128 + 2    dihentikan Ctrl-C (INT)",
                    "  143 = 128 + 15   dihentikan kill biasa (TERM)",
                    "  137 = 128 + 9    dihentikan kill -9. Di Docker sering karena memori habis.",
                    "  124              perintah timeout menyerah karena waktunya habis",
                    "  127              perintah tak ditemukan: salah ketik, atau tidak di PATH",
                    "  126              berkas ada tapi tak boleh dijalankan (materi Izin Berkas)",
                ],
            },
            {
                "heading": "trap: memasang penangan lebih dulu",
                "body": [
                    "trap memasang penangan (handler). Artinya kira-kira: \"kalau kejadian ini",
                    "datang, kerjakan ini dulu\".",
                    "",
                    "  trap 'perintah' KEJADIAN [KEJADIAN ...]",
                    "  trap nama_fungsi KEJADIAN",
                    "",
                    "Kejadiannya boleh nama sinyal (INT, TERM, HUP), boleh juga kejadian",
                    "buatan bash:",
                    "  EXIT    script berakhir, DENGAN CARA APA PUN",
                    "  ERR     ada perintah yang mengembalikan kode bukan 0",
                    "  DEBUG   sebelum setiap perintah; alat pelacak, jarang dipakai sehari-hari",
                    "",
                    "Materi Bekerja dengan File & Folder udah memakai salah satu bentuknya:",
                    "  tmp=$(mktemp)",
                    "  trap 'rm -f \"$tmp\"' EXIT",
                    "",
                    "Yang belum dibahas di sana: kejadian EXIT memang seluas namanya.",
                    "Penangannya ikut jalan waktu script kena Ctrl-C dan kena kill biasa,",
                    "nggak cuma waktu selesai normal. Yang lolos cuma kill -9, dan sinyal itu",
                    "memang nggak bisa ditangkap siapa pun.",
                    "",
                    "Lalu kenapa banyak script nulis 'trap bersihkan EXIT INT TERM'?",
                    "Penulisnya ngira EXIT nggak cukup. Akibatnya, waktu Ctrl-C ditekan,",
                    "bersihkan jalan dua kali: sekali dari trap INT, sekali lagi dari trap",
                    "EXIT. Kalau isinya cuma rm -f, nggak ada yang kelihatan salah. Tapi",
                    "kalau penangannya mencetak laporan atau mengirim notifikasi, barulah",
                    "ketahuan.",
                    "",
                    "Dua aturan yang bisa menyelamatkanmu:",
                    "  1. Pasang trap sebelum bagian yang perlu dibersihkan bisa gagal, bukan",
                    "     sesudahnya.",
                    "  2. Penangan pembersih harus aman dijalankan dua kali, misalnya rm -f,",
                    "     kill 2>/dev/null, atau mkdir -p. Kalau nggak bisa dibuat begitu,",
                    "     cabut sendiri trap-nya.",
                    "",
                    "Mencabut trap yang udah dipasang:",
                    "  trap - EXIT        kembalikan EXIT ke perilaku bawaan, tanpa penangan",
                    "  trap - INT TERM    boleh beberapa sekaligus",
                    "  trap -p            tampilkan trap apa saja yang sedang terpasang",
                    "",
                    "  bersihkan() { rm -rf \"$kerja\"; }",
                    "  trap bersihkan EXIT",
                    "  trap 'bersihkan; trap - EXIT; exit 130' INT  <- EXIT dicabut, tak dobel",
                    "",
                    "Jebakan terbesar: penangan sinyal yang nggak memanggil exit bikin script",
                    "lanjut ke baris berikutnya, seolah nggak terjadi apa-apa. Coba tulis",
                    "trap 'echo dibatalkan' INT, lalu tekan Ctrl-C. Pesannya muncul, tapi",
                    "script-nya jalan terus. Orang bakal nekan Ctrl-C berkali-kali sambil",
                    "bingung kenapa script-nya nggak mau berhenti. Penangan yang memang",
                    "dimaksudkan untuk menghentikan script wajib diakhiri exit.",
                    "",
                    "Angkanya juga jangan asal. Pakai exit 130 untuk INT dan exit 143 untuk",
                    "TERM, supaya siapa pun yang membaca kode keluarnya tahu script ini",
                    "berhenti karena sinyal.",
                ],
                "code": """#!/usr/bin/env bash
# trap = "kalau kejadian ini datang, kerjakan ini dulu".

tmp=$(mktemp)
echo "berkas sementara : $tmp"

bersihkan() {
    echo "  [bersihkan] menghapus $tmp"
    rm -f "$tmp"
}

trap bersihkan EXIT                             # jalan APA PUN cara script berakhir
trap 'echo "  [INT] Ctrl-C ditangkap"; exit 130' INT
trap 'echo "  [ERR] perintah gagal di baris $LINENO"' ERR

echo "data penting" > "$tmp"
echo "isi berkas       : $(cat "$tmp")"

false                                           # memicu ERR; script tetap lanjut
echo "setelah false, script masih hidup"

echo "kirim INT ke diri sendiri (PID $$)"
kill -INT "$$"

echo "BARIS INI TIDAK PERNAH TERCETAK"
""",
            },
            {
                "heading": "Nyalakan, tunggu siap, lalu pastikan mati",
                "body": [
                    "Pola ini muncul di hampir semua script uji dan script demo: nyalakan",
                    "sesuatu, pakai, lalu pastikan dia mati, termasuk kalau kamu menekan",
                    "Ctrl-C di tengah jalan.",
                    "",
                    "  ./server.sh &",
                    "  pid=$!",
                    "  trap 'kill \"$pid\" 2>/dev/null' EXIT",
                    "  ...pakai servernya...",
                    "  wait \"$pid\"     kalau memang mau menemani sampai server berhenti sendiri",
                    "",
                    "Urutannya penting: & dulu, lalu $! langsung, baru trap. Kalau trap",
                    "dipasang sebelum $pid diisi, kill dijalankan dengan argumen kosong.",
                    "Bash menolaknya dengan pesan 'not a pid or valid job spec' (di contoh",
                    "ini pesannya malah dibuang oleh 2>/dev/null), dan server-nya nggak ikut",
                    "dimatikan.",
                    "",
                    "Satu jebakan yang sering bikin orang buang waktu: kill \"$pid\" cuma",
                    "membunuh proses yang kamu lepas, nggak termasuk cucu-cucunya. Kalau yang",
                    "dilepas adalah script pembungkus yang di dalamnya memanggil program",
                    "lain, yang mati cuma pembungkusnya. Programnya tetap hidup dan memegang",
                    "port, sehingga percobaan berikutnya gagal dengan 'address already in",
                    "use'. Ada dua jalan keluar. Pakai exec di script pembungkus (materi",
                    "Aliran Data & Deskriptor) supaya PID-nya nggak berubah, atau bereskan",
                    "juga anaknya dengan pkill -P \"$pid\".",
                    "",
                    "sleep menjeda script. Satuannya detik, dan angka pecahan diterima di",
                    "Linux dan macOS:",
                    "  sleep 5      sleep 0.5      sleep 2m      sleep 1h",
                    "",
                    "Gunanya untuk memberi jeda di antara percobaan, misalnya:",
                    "  - menunggu layanan siap sebelum dikirimi permintaan, persis seperti",
                    "    contoh di bawah;",
                    "  - mengulang permintaan yang gagal, dengan jeda yang makin panjang",
                    "    tiap kali;",
                    "  - polling, yaitu memeriksa berkas atau status secara berkala tanpa",
                    "    menghabiskan CPU.",
                    "",
                    "Jangan nulis 'sleep 30' asal-asalan sebagai pengganti pemeriksaan. Di",
                    "mesin yang lambat, 30 detik tetap kurang. Di mesin yang cepat, cuma",
                    "buang waktu. Perulangan \"periksa, lalu jeda\" dengan batas jumlah",
                    "percobaan selalu lebih baik.",
                    "",
                    "timeout membatasi perintah yang bisa menggantung selamanya:",
                    "  timeout 30 curl -s https://contoh.com   menyerah setelah 30 detik",
                    "  timeout 5s ./mungkin-macet.sh           satuan boleh ditulis: s m h d",
                    "  timeout -s KILL 5 ./bandel              kirim KILL, bukan TERM",
                    "  timeout -k 5 30 ./bandel                TERM; 5 detik kemudian KILL",
                    "",
                    "Baris terakhir mengirim TERM dulu, lalu KILL kalau prosesnya masih hidup",
                    "5 detik kemudian.",
                    "",
                    "Kode keluarnya 124 kalau waktunya habis. Cuma dengan cara ini kamu bisa",
                    "membedakan \"gagal menjawab\" dari \"nggak pernah menjawab\". Bungkus tiap",
                    "perintah jaringan di script yang jalan otomatis dengan timeout. Tanpa",
                    "itu, satu server yang diam bisa menggantung seluruh pipeline sampai ada",
                    "orang yang sadar.",
                ],
                "code": """#!/usr/bin/env bash
# Nyalakan sesuatu di latar, tunggu siap, dan pastikan ia mati apa pun yang terjadi.

kerja=$(mktemp -d)
tanda="$kerja/siap"

# "Server" palsu: butuh 0,8 detik untuk siap, lalu hidup terus.
# exec membuat sleep MENGGANTI subshell-nya, jadi $! benar-benar PID
# program yang nanti mau dimatikan -- bukan PID pembungkusnya.
( sleep 0.8; touch "$tanda"; exec sleep 30 ) &
pid=$!

# Dipasang PERSIS setelah PID diketahui, sebelum ada baris yang bisa gagal.
trap 'kill "$pid" 2>/dev/null; rm -rf "$kerja"' EXIT

echo "server dinyalakan, PID $pid"

for n in 1 2 3 4 5 6; do
    if [[ -e "$tanda" ]]; then
        echo "siap pada percobaan ke-$n"
        break
    fi
    echo "belum siap, jeda 0,5 detik (percobaan ke-$n)"
    sleep 0.5
done

timeout 1 sleep 5
echo "timeout 1 sleep 5   -> exit code $?   (124 = waktunya habis)"

timeout 1 sleep 0.2
echo "timeout 1 sleep 0.2 -> exit code $?   (selesai sebelum batas)"

kill -0 "$pid" 2>/dev/null && echo "server masih hidup; trap EXIT yang mematikannya"
""",
            },
        ],
    },
    {
        "title": "21. Alat Pendamping: curl, jq, date, tar",
        "sections": [
            {
                "body": [
                    "Script bash yang isinya murni bash hampir tidak ada. Kosakata bash sendiri kecil: variabel,",
                    "if, for, fungsi, pipe. Semua pekerjaan sesungguhnya - mengunduh, membaca JSON, menghitung",
                    "tanggal, mengemas berkas - dikerjakan PROGRAM LAIN yang dipanggil script.",
                    "",
                    "Jadi bash itu perekat, dan membaca script orang lain berarti mengenali alat-alat yang",
                    "direkatkannya. Kamu sudah kenal grep, sed, dan awk dari materi sebelumnya. Empat nama di",
                    "bawah ini muncul sama seringnya di kode nyata, dan tanpa mengenalinya sebuah script yang",
                    "sebetulnya sederhana akan terlihat seperti sandi.",
                    "",
                    "CURL - mengambil dan mengirim data lewat jaringan",
                    "  Namanya dari 'client URL'. Bawaannya: isi respons dicetak ke stdout, jadi bisa langsung",
                    "  dipipe atau ditangkap dengan $(...).",
                    "",
                    "  curl https://contoh.id/data.json",
                    "",
                    "Rangkaian yang paling sering kamu lihat adalah -fsSL. Itu EMPAT opsi yang digabung, dan",
                    "tiap hurufnya menutup satu masalah yang berbeda:",
                    "",
                    "  -f  (--fail)        gagal beneran kalau status HTTP 4xx/5xx.",
                    "                      Tanpa -f, curl menganggap halaman '404 Not Found' sebagai SUKSES:",
                    "                      exit code tetap 0 dan isi halaman errornya ikut tersimpan.",
                    "  -s  (--silent)      matikan bilah progres.",
                    "  -S  (--show-error)  tapi pesan error tetap ditampilkan. -s sendirian membuat curl bisu",
                    "                      total, termasuk saat gagal. Itu sebabnya -sS selalu berpasangan.",
                    "  -L  (--location)    ikuti pengalihan 301/302. Tanpa ini kamu menyimpan halaman",
                    "                      'Moved Permanently' yang isinya nyaris kosong.",
                    "",
                    "Opsi lain yang wajib dikenali:",
                    "  -o nama.json        simpan ke berkas bernama itu (o kecil = kamu yang menamai)",
                    "  -O                  simpan pakai nama dari URL-nya (O besar = curl yang menamai)",
                    "  -H \"Judul: nilai\"    tambah header, mis. -H \"Authorization: Bearer $TOKEN\"",
                    "  -d '{\"a\":1}'        kirim badan permintaan. Adanya -d otomatis membuat metodenya POST",
                    "  -X PUT              tetapkan metode sendiri. Tidak perlu ditulis kalau sudah ada -d",
                    "  --max-time 30       batas total waktu. Tanpa ini script bisa menggantung selamanya",
                    "  --retry 3           ulangi kalau gagal karena masalah jaringan sementara",
                    "  -w '%{http_code}'   cetak kode status saja, biasanya bersama -o /dev/null",
                    "",
                    "Exit code curl yang sering ketemu: 0 sukses, 6 nama host tidak ketemu, 7 tidak bisa",
                    "menyambung, 28 kehabisan waktu, dan 22 kalau -f dipakai dan servernya menjawab 4xx/5xx.",
                    "",
                    "wget melakukan hal serupa dengan tombol yang berbeda: wget -qO- URL setara curl -s URL",
                    "(hasil ke stdout), sedangkan wget -q URL menyimpan ke berkas seperti curl -O.",
                    "",
                    "KENAPA curl -fsSL URL | bash ADA DI MANA-MANA",
                    "  Halaman pemasangan suka memberi satu baris seperti ini karena ia bekerja di distro apa",
                    "  pun tanpa paket manager. Yang perlu kamu sadari: baris itu MENJALANKAN kode orang lain",
                    "  dengan hak akses kamu, tanpa kamu pernah melihat isinya. Dua bahaya tambahan yang tidak",
                    "  kelihatan: server bisa mengirim isi berbeda kepada curl dan kepada browser, dan kalau",
                    "  koneksi putus di tengah, bash sudah telanjur menjalankan separuh script.",
                    "",
                    "  Bentuk amannya cuma butuh satu langkah lagi:",
                    "    curl -fsSL https://contoh.id/pasang.sh -o pasang.sh",
                    "    less pasang.sh        # baca dulu",
                    "    bash pasang.sh",
                ],
            },
            {
                "heading": "jq: satu-satunya cara waras menangani JSON",
                "body": [
                    "Hampir semua API sekarang menjawab dengan JSON, dan bash tidak punya tipe data untuk itu -",
                    "baginya JSON cuma seuntai teks panjang.",
                    "",
                    "Godaannya adalah memotongnya dengan grep atau sed. Itu selalu rapuh, dan alasannya bukan",
                    "selera:",
                    "  - JSON tidak peduli baris baru. Server yang sama bisa mengirim rapi hari ini dan satu",
                    "    baris panjang besok. Semua pola yang mengandalkan 'satu objek satu baris' langsung mati.",
                    "  - Urutan kunci tidak dijamin.",
                    "  - Nilai boleh memuat tanda kutip yang di-escape, kurung, bahkan potongan JSON lain.",
                    "  - Spasi di sekitar titik dua bebas.",
                    "Aturan praktis: begitu kamu menulis regex KEDUA untuk JSON yang sama, berhenti dan pasang jq.",
                    "",
                    "jq bukan bawaan sistem: sudo dnf install jq / sudo apt install jq / brew install jq.",
                    "Karena itu script yang memakainya sebaiknya memeriksa dulu dengan command -v (contoh di",
                    "bawah) supaya pesannya jelas, bukan 'jq: command not found' di tengah proses.",
                    "",
                    "Filter jq yang menutupi sebagian besar kebutuhan:",
                    "  .                 seluruh isi, sekaligus dirapikan dan diberi warna",
                    "  .kunci            ambil satu nilai",
                    "  .a.b.c            masuk ke dalam objek bersarang",
                    "  .daftar[]         BUKA array jadi banyak nilai, satu per baris",
                    "  .daftar[0]        elemen pertama",
                    "  .daftar[].nama    ambil satu kunci dari tiap elemen",
                    "  select(syarat)    teruskan yang memenuhi syarat saja",
                    "  length, add       jumlah elemen, dan jumlahkan angka di sebuah array",
                    "  sort_by(.gaji)    urutkan; beri tanda minus (-.gaji) untuk urutan menurun",
                    "  // \"cadangan\"     nilai pengganti kalau yang kiri null",
                    "",
                    "Tiga hal yang paling sering bikin bingung:",
                    "",
                    "  1. Tanda | di dalam petik tunggal itu MILIK jq, bukan pipe shell. Bentuknya sama persis,",
                    "     tapi yang di dalam '...' dikerjakan jq sendiri, dan yang di luar oleh bash.",
                    "",
                    "  2. Tanpa -r, string keluar LENGKAP DENGAN tanda kutipnya. Ini penyebab nomor satu",
                    "     variabel bash yang isinya \"Andi\" berikut petiknya, lalu perbandingan == gagal terus",
                    "     padahal di layar terlihat sama. -r artinya raw: keluarkan teksnya saja.",
                    "",
                    "  3. Kunci yang tidak ada menghasilkan null, BUKAN error. Dengan -r, null tercetak sebagai",
                    "     kata 'null' dan diam-diam masuk ke variabelmu. Tutup dengan // \"nilai cadangan\".",
                    "",
                    "Untuk menyisipkan nilai dari shell ke dalam filter, pakai --arg nama nilai lalu rujuk",
                    "sebagai $nama. Menempel \"$var\" langsung ke tengah filter adalah lubang injeksi yang sama",
                    "bentuknya dengan SQL injection.",
                ],
                "code": """#!/usr/bin/env bash
set -euo pipefail

# jq bukan bawaan sistem. command -v memeriksa apakah sebuah perintah ada.
command -v jq >/dev/null || { echo "jq belum terpasang: sudo dnf install jq"; exit 0; }

cat > pegawai.json << 'EOF'
{
  "kantor": "Cabang Selatan",
  "pegawai": [
    {"nama": "Andi",  "divisi": "gudang", "gaji": 4500000, "aktif": true},
    {"nama": "Budi",  "divisi": "kantor", "gaji": 6200000, "aktif": false},
    {"nama": "Citra", "divisi": "gudang", "gaji": 7100000, "aktif": true, "telepon": "0812"}
  ]
}
EOF

echo "== satu nilai: perhatikan tanda kutipnya masih ikut =="
jq '.kantor' pegawai.json
echo "== nilai yang sama dengan -r: kutipnya hilang =="
jq -r '.kantor' pegawai.json

echo
echo "== .pegawai[] membuka array jadi baris-baris =="
jq -r '.pegawai[].nama' pegawai.json

echo
echo "== select() menyaring; tanda | di dalam petik itu milik jq =="
jq -r '.pegawai[] | select(.aktif) | .nama' pegawai.json

echo
echo "== kunci yang tidak ada jadi null, // memberi nilai cadangan =="
jq -r '.pegawai[] | "\\(.nama): \\(.telepon // "tidak ada")"' pegawai.json

echo
echo "== menghitung tanpa keluar dari jq =="
echo "jumlah orang  : $(jq '.pegawai | length' pegawai.json)"
echo "total gaji    : $(jq '[.pegawai[].gaji] | add' pegawai.json)"
echo "gaji tertinggi: $(jq -r '.pegawai | sort_by(-.gaji)[0].nama' pegawai.json)"

echo
echo "== --arg menyuntikkan nilai shell dengan aman =="
cari="gudang"
jq -r --arg d "$cari" '.pegawai[] | select(.divisi == $d) | .nama' pegawai.json

echo
echo "== keluaran jq dipecah lagi oleh bash =="
jq -r '.pegawai[] | select(.aktif) | "\\(.nama)=\\(.gaji)"' pegawai.json |
while IFS='=' read -r nama gaji; do
    printf "%-8s %10d\\n" "$nama" "$gaji"
done

rm -f pegawai.json""",
            },
            {
                "heading": "date: yang diawali + itu format, bukan opsi",
                "body": [
                    "date tanpa argumen mencetak waktu sekarang dalam bentuk panjang untuk manusia. Yang membuat",
                    "orang bingung waktu membaca script adalah argumen berawalan +, seperti di $(date +%Y) yang",
                    "sempat lewat di materi Variabel & Quoting.",
                    "",
                    "  Argumen yang diawali + BUKAN opsi. Itu STRING FORMAT.",
                    "",
                    "Karena itu bentuknya date +%Y dan bukan date --year. Semua yang bukan %X di dalam string itu",
                    "dicetak apa adanya, jadi tanda hubung di +%Y-%m-%d cuma teks biasa. Kalau formatnya memuat",
                    "spasi, bungkus dengan petik: date +'%F %T'.",
                    "",
                    "  %Y  tahun 4 digit      2024        %F  sama dengan %Y-%m-%d",
                    "  %m  bulan 2 digit      03          %T  sama dengan %H:%M:%S",
                    "  %d  tanggal 2 digit    15          %s  detik sejak 1 Januari 1970 (epoch)",
                    "  %H  jam 24 jam         08          %z  selisih zona waktu, mis. +0700",
                    "  %M  menit              30          %A  nama hari, mengikuti bahasa sistem",
                    "  %S  detik              45          %-d tanpa nol di depan: 5, bukan 05",
                    "",
                    "date -u memakai UTC, bukan zona waktu mesin. Ini bukan detail sepele: dua server di zona",
                    "berbeda yang menulis ke log yang sama akan menghasilkan urutan waktu yang mustahil dibaca.",
                    "Aturan praktis untuk log dan nama arsip - pakai -u, atau simpan epoch (%s) yang memang",
                    "tidak punya zona.",
                    "",
                    "date -d \"teks\" menghitung waktu LAIN, bukan sekarang. Ia memahami bahasa sehari-hari:",
                    "  date -d 'yesterday' +%F        date -d '2 hours ago' +%T",
                    "  date -d '2024-03-15' +%A       date -d @1710491445 +%F     (@ berarti epoch)",
                    "",
                    "DUA JEBAKAN YANG BENAR-BENAR MENJEBAK",
                    "",
                    "  1. -d dan -u -d itu milik GNU coreutils, yaitu Linux. Di macOS/BSD perintahnya lain sama",
                    "     sekali: date -v-1d +%F untuk kemarin, date -r 1710491445 untuk epoch. Script tanggal",
                    "     yang mulus di Linux bisa langsung mati di laptop rekanmu.",
                    "",
                    "  2. Kalau teks waktunya SUDAH memuat jam, tanda + atau - sesudahnya dibaca sebagai ZONA",
                    "     WAKTU, bukan pergeseran hari. Ini diam-diam memberi jawaban yang salah:",
                    "",
                    "       date -u -d \"2024-03-15 08:30:45 + 7 days\"  -> 2024-03-16 01:30:45   SALAH",
                    "         '+7' ditelan sebagai zona +0700, lalu sisa kata 'days' dihitung sebagai 1 hari.",
                    "       date -u -d \"2024-03-15 08:30:45 UTC + 7 days\" -> 2024-03-22 08:30:45   BENAR",
                    "",
                    "     Sebutkan zonanya, atau tulis tanpa tanda: '7 days' dan '1 day ago' aman.",
                    "",
                    "Untuk cap waktu di nama berkas, urutan besar-ke-kecil (%Y%m%d) bukan selera: dengan urutan",
                    "itu, urut alfabet = urut waktu, sehingga ls dan sort langsung memberi hasil yang benar.",
                    "Dan pakai %H%M%S, bukan %T - %T menghasilkan titik dua, yang bermasalah di Windows dan",
                    "menyusahkan waktu berkasnya disalin lewat scp.",
                ],
                "code": "#!/usr/bin/env bash\nset -euo pipefail\n\n# Tanggalnya sengaja DIPATOK supaya hasil contoh ini sama tiap kali dijalankan.\n# Di script sungguhan kamu membuang bagian -u -d \"$ACUAN\" dan memakai waktu\n# sekarang: date +%F, date +%s, dan seterusnya.\nACUAN=\"2024-03-15 08:30:45 UTC\"\n\np() { printf \"%-24s %s\\n\" \"$1\" \"$2\"; }\n\np \"tanpa format sama sekali\" \"$(date -u -d \"$ACUAN\")\"\np \"+%Y-%m-%d\"               \"$(date -u -d \"$ACUAN\" +%Y-%m-%d)\"\np \"+%F  (pintasan sama)\"    \"$(date -u -d \"$ACUAN\" +%F)\"\np \"+%H:%M:%S\"               \"$(date -u -d \"$ACUAN\" +%H:%M:%S)\"\np \"+%T  (pintasan sama)\"    \"$(date -u -d \"$ACUAN\" +%T)\"\np \"+%Y%m%d-%H%M%S\"          \"$(date -u -d \"$ACUAN\" +%Y%m%d-%H%M%S)\"\np \"+%s  (detik epoch)\"      \"$(date -u -d \"$ACUAN\" +%s)\"\np \"format berspasi\"         \"$(date -u -d \"$ACUAN\" +'%d/%m/%Y pukul %H.%M')\"\np \"sehari sebelumnya\"       \"$(date -u -d \"$ACUAN - 1 day\" +%F)\"\np \"seminggu sesudahnya\"     \"$(date -u -d \"$ACUAN + 7 days\" +%F)\"\n\necho\necho \"-- epoch cuma bilangan bulat, jadi selisih waktu itu pengurangan biasa --\"\nmulai=$(date -u -d \"$ACUAN\" +%s)\nselesai=$(( mulai + 95 ))\necho \"mulai   : $mulai -> $(date -u -d \"@$mulai\" +%T)\"\necho \"selesai : $selesai -> $(date -u -d \"@$selesai\" +%T)\"\necho \"lama    : $(( selesai - mulai )) detik\"\n\necho\necho \"-- cap waktu dipakai untuk menamai berkas --\"\necho \"berkas log   : app-$(date -u -d \"$ACUAN\" +%F).log\"\necho \"berkas arsip : backup-$(date -u -d \"$ACUAN\" +%Y%m%d-%H%M%S).tar.gz\"",
            },
            {
                "heading": "tar, gzip, checksum, rsync, envsubst",
                "body": [
                    "Dua hal yang sering dikira satu:",
                    "  tar   MENGGABUNGKAN banyak berkas jadi satu, tanpa memampatkan sedikit pun.",
                    "  gzip  MEMAMPATKAN satu berkas, tanpa bisa menggabungkan apa pun.",
                    "Itu sebabnya namanya bertingkat dua: .tar.gz artinya digabung dulu, baru dimampatkan.",
                    "",
                    "Huruf-huruf tar (boleh ditulis tanpa tanda minus, warisan lama):",
                    "  c  create, bikin arsip baru        z  lewatkan gzip  (.gz)",
                    "  x  extract, bongkar                j  lewatkan bzip2 (.bz2)",
                    "  t  table, lihat isinya saja        J  lewatkan xz    (.xz)",
                    "  f  berkas arsipnya bernama ...     v  verbose, sebutkan tiap berkas",
                    "",
                    "  tar czf arsip.tar.gz folder/    kemas",
                    "  tar tzf arsip.tar.gz            lihat isi, tanpa membongkar",
                    "  tar xzf arsip.tar.gz -C tujuan/ bongkar ke folder tertentu",
                    "",
                    "Jebakan tar yang bisa membuatmu kehilangan data:",
                    "  - f harus persis sebelum nama arsip, dan ARSIPNYA DITULIS DULUAN. Kalau urutannya",
                    "    terbalik jadi tar czf laporan.txt arsip.tar.gz, maka laporan.txt-lah yang ditimpa",
                    "    jadi arsip. Isinya hilang tanpa satu pun pertanyaan.",
                    "  - Selalu tar tzf dulu sebelum membongkar arsip dari internet. Ada arsip yang isinya",
                    "    langsung berhamburan ke folder saat ini ('tarbomb') alih-alih rapi di dalam satu",
                    "    folder. Bongkar di folder kosong atau pakai -C.",
                    "  - tar czf a.tar.gz /home/vi/demo menyimpan jalur panjang itu di dalam arsip dan",
                    "    memberi peringatan 'Removing leading /'. Lebih rapi: tar czf a.tar.gz -C /home/vi demo",
                    "",
                    "gzip berkas.txt MENGGANTI berkasnya jadi berkas.txt.gz - yang asli lenyap. Pakai gzip -k",
                    "kalau ingin menyimpan keduanya, gunzip untuk mengembalikan, dan zcat / zgrep untuk",
                    "membaca isi .gz tanpa membongkarnya lebih dulu.",
                    "",
                    "MEMERIKSA UNDUHAN. Unduhan yang terpotong di tengah tetap terhitung 'berhasil' oleh curl",
                    "kalau servernya tidak menyebutkan panjangnya. Karena itu berkas rilis biasanya disertai",
                    "berkas .sha256:",
                    "  sha256sum arsip.tar.gz > arsip.tar.gz.sha256    buat sidik jarinya",
                    "  sha256sum -c arsip.tar.gz.sha256                periksa -> 'OK' atau 'FAILED'",
                    "md5sum bekerja dengan pola yang sama, tapi md5 sudah lama tidak aman untuk urusan",
                    "keamanan; anggap saja alat pemeriksa kerusakan, bukan bukti keaslian.",
                    "",
                    "MENYALIN ANTAR TEMPAT.",
                    "  rsync -av --delete sumber/ tujuan/",
                    "    -a  pertahankan izin, waktu, dan link       -v  sebutkan yang disalin",
                    "    --delete  hapus di tujuan yang sudah tidak ada di sumber",
                    "  Kelebihannya atas cp -r: rsync cuma memindahkan bagian yang BERUBAH, jadi backup kedua",
                    "  dan seterusnya jauh lebih cepat.",
                    "",
                    "  Garis miring di ujung SUMBER menentukan segalanya, dan ini kesalahan klasik:",
                    "    rsync -av data/ cadangan/   -> ISI data masuk ke cadangan/",
                    "    rsync -av data  cadangan/   -> foldernya sendiri masuk, jadi cadangan/data/",
                    "  Gabungan salah miring dan --delete bisa menghapus isi folder tujuan. Coba dulu dengan",
                    "  -n (--dry-run) yang cuma melaporkan rencananya tanpa menyentuh apa pun.",
                    "",
                    "  Untuk antar mesin, keduanya lewat ssh: scp berkas.txt user@host:/srv/app/ untuk sekali",
                    "  salin, atau rsync -av data/ user@host:/srv/app/data/ untuk yang berulang.",
                    "",
                    "envsubst mengisi ${VAR} di sebuah templat dengan nilai dari lingkungan - dipakai di mana-",
                    "mana untuk membuat berkas konfigurasi di dalam container. Jebakannya besar: tanpa daftar",
                    "putih, ia melahap SEMUA yang berbentuk $NAMA, termasuk $host milik nginx yang seharusnya",
                    "dibiarkan. Karena $host tidak ada di lingkungan, hasilnya jadi kosong. Batasi dengan",
                    "menyebutkan nama yang boleh diganti: envsubst '${PORT} ${NAMA_APP}' < templat.conf",
                ],
                "code": "#!/usr/bin/env bash\nset -euo pipefail\n\nrm -rf contoh-arsip hasil-bongkar\nmkdir -p contoh-arsip/laporan\necho \"penjualan januari\"  > contoh-arsip/laporan/jan.txt\necho \"penjualan februari\" > contoh-arsip/laporan/feb.txt\necho \"catatan singkat\"    > contoh-arsip/README.txt\n\ncap=$(date -u -d \"2024-03-15 08:30:00 UTC\" +%Y%m%d-%H%M%S)\narsip=\"backup-$cap.tar.gz\"\n\n# c=create  z=gzip  f=nama berkas arsip. Nama arsip ditulis DULUAN.\ntar czf \"$arsip\" contoh-arsip\necho \"arsip dibuat: $arsip\"\n\necho\necho \"== t = daftar isi, tanpa membongkar apa pun ==\"\ntar tzf \"$arsip\"\n\necho\necho \"== sidik jari, supaya ketahuan kalau berkasnya rusak ==\"\nsha256sum \"$arsip\" > \"$arsip.sha256\"\nsha256sum -c \"$arsip.sha256\"\n\necho\necho \"== x = bongkar, -C = ke folder mana ==\"\nmkdir -p hasil-bongkar\ntar xzf \"$arsip\" -C hasil-bongkar\nfind hasil-bongkar -type f | sort\n\necho\necho \"== envsubst: isi templat dari variabel lingkungan ==\"\ncat > templat.conf << 'EOF'\nserver {\n    listen ${PORT};\n    server_name ${NAMA_APP}.contoh.id;\n    proxy_set_header Host $host;\n}\nEOF\nexport PORT=8080 NAMA_APP=tokoku\n\necho '-- envsubst polos: $host punya nginx ikut dimakan jadi kosong --'\nenvsubst < templat.conf\n\necho '-- dibatasi: hanya dua nama ini yang boleh diganti --'\nenvsubst '${PORT} ${NAMA_APP}' < templat.conf\n\nrm -rf contoh-arsip hasil-bongkar templat.conf \"$arsip\" \"$arsip.sha256\"",
            },
            {
                "heading": "Semuanya dalam satu script backup",
                "body": [
                    "Bentuk di bawah ini adalah kerangka yang berulang di ribuan script nyata: ambil data,",
                    "periksa isinya, kemas dengan nama bercap waktu, catat ke log. Urutan membacanya:",
                    "",
                    "  1. Periksa dulu semua alat yang dibutuhkan ada, sebelum mengerjakan apa pun. Gagal di",
                    "     awal jauh lebih baik daripada gagal setelah setengah pekerjaan terlanjur jalan.",
                    "  2. mktemp + trap ... EXIT untuk berkas sementara - polanya sudah dipakai di materi",
                    "     Bekerja dengan File & Folder.",
                    "  3. curl -fsSL ... -o \"$tmp\" mengunduh; karena ada -f dan set -e, status 404 langsung",
                    "     menghentikan script alih-alih mengarsipkan halaman error.",
                    "  4. jq membaca hasilnya sebagai data, bukan sebagai teks.",
                    "  5. tar czf dengan cap waktu di namanya, lalu sha256sum sebagai bukti arsipnya utuh.",
                    "  6. tee -a menaruh tiap kabar di layar DAN di log sekaligus.",
                    "",
                    "Dua baris sengaja dipatok supaya contoh ini bisa dijalankan berulang kali dengan hasil",
                    "yang persis sama:",
                    "  - SUMBER memakai skema file:// (curl memang bisa membaca berkas lokal). Di script",
                    "    sungguhan isinya https://...",
                    "  - cap waktu diambil dari tanggal tetap. Aslinya cap=$(date +%Y%m%d-%H%M%S).",
                ],
                "code": "#!/usr/bin/env bash\nset -euo pipefail\n\n# --- Data contoh. Di dunia nyata bagian ini datang dari server. -------------\nmkdir -p data-gudang\ncat > data-gudang/pesanan.json << 'EOF'\n{\n  \"toko\": \"Cabang Selatan\",\n  \"pesanan\": [\n    {\"id\": \"P-001\", \"barang\": \"kopi\", \"jumlah\": 3, \"lunas\": true},\n    {\"id\": \"P-002\", \"barang\": \"gula\", \"jumlah\": 1, \"lunas\": false},\n    {\"id\": \"P-003\", \"barang\": \"teh\",  \"jumlah\": 5, \"lunas\": true}\n  ]\n}\nEOF\n\n# file:// dipakai supaya contoh ini jalan tanpa jaringan.\n# Di script sungguhan: SUMBER=\"https://api.contoh.id/pesanan.json\"\nSUMBER=\"file://$PWD/data-gudang/pesanan.json\"\nLOG=\"riwayat-backup.log\"\n\n# Cap waktu dipatok supaya hasilnya sama tiap dijalankan.\n# Aslinya: cap=$(date +%Y%m%d-%H%M%S) dan tanggal=$(date +%F)\ncap=$(date -u -d \"2024-03-15 08:30:00 UTC\" +%Y%m%d-%H%M%S)\ntanggal=$(date -u -d \"2024-03-15 08:30:00 UTC\" +%F)\n\ncatat() {\n    echo \"[$tanggal] $*\" | tee -a \"$LOG\"\n}\n\nfor alat in curl jq tar; do\n    command -v \"$alat\" >/dev/null || { echo \"Butuh $alat, belum terpasang.\" >&2; exit 1; }\ndone\n\ntmp=$(mktemp)\ntrap 'rm -f \"$tmp\"' EXIT\n\ncatat \"mengunduh $SUMBER\"\ncurl -fsSL \"$SUMBER\" -o \"$tmp\"\n\njumlah=$(jq '.pesanan | length' \"$tmp\")\nlunas=$(jq '[.pesanan[] | select(.lunas)] | length' \"$tmp\")\ncatat \"diterima $jumlah pesanan, $lunas sudah lunas\"\n\ncp \"$tmp\" data-gudang/pesanan.json\narsip=\"backup-$cap.tar.gz\"\ntar czf \"$arsip\" data-gudang\ncatat \"arsip $arsip dibuat\"\n\nsha256sum \"$arsip\" > \"$arsip.sha256\"\nsha256sum -c --quiet \"$arsip.sha256\" && catat \"sidik jari cocok\"\n\necho\necho \"== isi $LOG ==\"\ncat \"$LOG\"\n\nrm -rf data-gudang \"$arsip\" \"$arsip.sha256\" \"$LOG\"",
            },
        ],
    },
    {
        "title": "22. Debugging & Praktik Baik",
        "sections": [
            {
                "body": [
                    "Cara men-debug script bash:",
                    "",
                    "1. bash -x script.sh",
                    "     Tampilkan setiap perintah sebelum dijalankan.",
                    "     Cara tercepat melihat di mana script salah jalan.",
                    "",
                    "2. set -x  /  set +x di dalam script",
                    "     Nyalakan pelacakan hanya di bagian tertentu.",
                    "",
                    "3. bash -n script.sh",
                    "     Cek sintaks saja, tanpa menjalankan apa pun.",
                    "",
                    "4. shellcheck script.sh",
                    "     Alat linter khusus bash. WAJIB dipakai.",
                    "     Menangkap bug yang tidak kelihatan mata, seperti",
                    "     variabel tanpa petik atau perbandingan yang salah.",
                    "     Pasang: apt install shellcheck / brew install shellcheck",
                    "",
                    "5. echo untuk melacak nilai",
                    "     echo \"DEBUG: nilai=$nilai\" >&2",
                    "     Kirim ke stderr supaya tidak mengganggu output asli.",
                    "",
                    "6. trap 'echo \"gagal di baris $LINENO\" >&2' ERR",
                    "     Pasang di awal script: begitu ada perintah yang gagal, nomor",
                    "     barisnya tercetak sendiri. Paling menolong pada script panjang",
                    "     yang jalan dengan set -e, karena set -e berhenti diam-diam",
                    "     tanpa memberi tahu di mana ia berhenti.",
                ]
            },
            {
                "heading": "Kerangka script yang baik",
                "code": """#!/usr/bin/env bash
#
# backup.sh - Menyalin folder ke lokasi cadangan
# Penggunaan: ./backup.sh <sumber> <tujuan>

set -euo pipefail

readonly NAMA_SCRIPT="${0##*/}"

pesan() {
    echo "[$NAMA_SCRIPT] $*"
}

galat() {
    echo "[$NAMA_SCRIPT] ERROR: $*" >&2
    exit 1
}

bantuan() {
    cat << EOF
Penggunaan: $NAMA_SCRIPT <sumber> <tujuan>

Menyalin isi folder sumber ke folder tujuan.

Opsi:
  -h    Tampilkan bantuan ini
EOF
}

utama() {
    [[ "${1:-}" == "-h" ]] && { bantuan; exit 0; }
    [[ $# -eq 2 ]] || galat "Butuh 2 argumen. Lihat -h."

    local sumber="$1" tujuan="$2"
    [[ -d "$sumber" ]] || galat "Folder '$sumber' tidak ada"

    mkdir -p "$tujuan"
    cp -r "$sumber/." "$tujuan/"
    pesan "Selesai menyalin ke $tujuan"
}

utama "$@" """
            },
            {
                "body": [
                    "Praktik baik yang dipakai di kerangka di atas:",
                    "",
                    "  1. Shebang #!/usr/bin/env bash",
                    "  2. Komentar penjelasan di kepala file",
                    "  3. set -euo pipefail untuk berhenti saat ada masalah",
                    "  4. readonly untuk nilai yang tidak boleh berubah",
                    "  5. Fungsi pesan() dan galat() supaya output konsisten",
                    "  6. Fungsi bantuan() dengan heredoc",
                    "  7. Semua logika di dalam fungsi utama()",
                    "  8. Panggil utama \"$@\" di baris terakhir",
                    "  9. local untuk semua variabel di dalam fungsi",
                    " 10. Semua variabel dibungkus petik ganda",
                    "",
                    "Kesalahan pemula yang paling sering:",
                    "  - Spasi di sekitar = saat membuat variabel",
                    "  - Lupa membungkus variabel dengan petik",
                    "  - Pakai [ ] padahal [[ ]] lebih aman",
                    "  - Pakai -eq untuk membandingkan teks (itu untuk angka)",
                    "  - Mengira return mengirim data, padahal cuma status",
                    "  - rm -rf \"$folder/\"* tanpa memastikan $folder tidak kosong",
                ]
            },
            {
                "heading": "Dua hal yang belum ada di kerangka itu",
                "body": [
                    "Kerangka di atas sudah cukup untuk script yang kamu pakai sendiri.",
                    "Begitu ia dipakai orang lain, dua hal ini biasanya ditambahkan.",
                    "",
                    "1. PERIKSA DEPENDENSI SEBELUM MULAI BEKERJA.",
                    "   Pemeriksaan command -v beserta alasannya sudah dibahas di materi",
                    "   Proses, source, dan Subshell. Yang baru di sini cuma bentuknya:",
                    "   dengan galat() sudah tersedia, satu perulangan cukup untuk",
                    "   memeriksa berapa pun alat yang dipakai.",
                    "",
                    "     for alat in jq curl; do",
                    "         command -v \"$alat\" >/dev/null 2>&1 || galat \"butuh $alat\"",
                    "     done",
                    "",
                    "   Tempatnya di BARIS PERTAMA utama(), bukan di kepala berkas.",
                    "   Fungsi harus sudah terbaca sebelum dipanggil, dan galat() baru",
                    "   didefinisikan di tengah berkas. Ditaruh di atasnya, script yang",
                    "   kekurangan alat justru menjawab 'galat: command not found' -",
                    "   tepat di saat pesannya paling dibutuhkan.",
                    "",
                    "2. URAIKAN OPSI DENGAN getopts.",
                    "   Baris [[ \"${1:-}\" == \"-h\" ]] di kerangka itu cuma mengenali -h,",
                    "   dan cuma kalau ia argumen PERTAMA. Begitu opsinya bertambah jadi",
                    "   -v, -o berkas, atau gabungan -hv, ganti dengan getopts - caranya",
                    "   ada di materi Opsi Baris Perintah & getopts.",
                ]
            },
        ],
    },
    {
        "title": "23. Bash vs sh: Portabilitas & POSIX",
        "sections": [
            {
                "body": [
                    "Sepanjang kurikulum ini shebang-nya selalu #!/usr/bin/env bash. Sekarang saatnya",
                    "tahu apa yang terjadi kalau baris itu diganti jadi #!/bin/sh — karena kamu PASTI",
                    "akan bertemu berkas semacam itu, dan isinya terlihat aneh kalau tidak tahu sebabnya.",
                    "",
                    "sh BUKAN nama pendek dari bash. sh adalah SPESIFIKASI: daftar fitur minimum yang",
                    "disepakati standar bernama POSIX. Program mana yang mengisi peran itu berbeda-beda",
                    "tiap sistem:",
                    "",
                    "  Sistem                 Yang jadi /bin/sh        Besarnya",
                    "  Debian, Ubuntu         dash                     sekitar 120 KB",
                    "  Alpine (image Docker)  busybox ash              satu biner untuk ratusan perintah",
                    "  Fedora, Arch           bash dalam mode sh       sekitar 1,5 MB",
                    "  macOS                  bash 3.2 dalam mode sh   -",
                    "",
                    "Cek punya mesinmu sendiri:",
                    "  ls -l /bin/sh",
                    "  readlink -f /bin/sh",
                    "",
                    "Kenapa Debian repot memakai shell mungil, bukan bash saja? Karena /bin/sh dipanggil",
                    "ribuan kali saat sistem menyala, dan dash menyala jauh lebih cepat serta memakan",
                    "memori jauh lebih sedikit. Alpine lebih ekstrem: bash memang TIDAK terpasang di sana.",
                    "Kecilnya bukan kebetulan atau keterbelakangan — itu tujuan desainnya.",
                    "",
                    "Di mana kamu akan bertemu script sh, mau atau tidak:",
                    "  - Dockerfile: RUN dan ENTRYPOINT bentuk shell memanggil /bin/sh -c, bukan bash",
                    "  - image Alpine dan image 'slim' lain yang sengaja dipangkas",
                    "  - git hook di .git/hooks/, script init di /etc/init.d, dan entri cron",
                    "  - ./configure bawaan proyek C, dan installer bergaya 'curl -fsSL ... | sh'",
                    "",
                    "Fitur bash yang tidak ada di sh punya sebutan sendiri di dunia nyata: BASHISM.",
                    "Kamu akan melihat kata itu di laporan bug dan di komentar kode.",
                ],
            },
            {
                "heading": "bashisme.sh — mulus di bash, hancur di sh",
                "code": """#!/usr/bin/env bash
# Tiap bagian di sini butuh bash. Ganti shebang-nya jadi #!/bin/sh
# dan berkas ini rusak sebelum sempat mencetak apa pun.

nama="levi anggara"
buah=("apel" "jeruk" "mangga")

if [[ "$nama" == *anggara* ]]; then
    echo "1. [[ ]]   : pola cocok, tanpa perlu grep"
fi

echo "2. array   : ${buah[1]}, jumlah ${#buah[@]}"
echo "3. ^^      : ${nama^^}"

pesan="halo"
pesan+=" dunia"
echo "4. +=      : $pesan"

n=0
((n++))
((n += 7))
echo "5. (( ))   : $n"

read -r depan belakang <<< "$nama"
echo "6. <<<     : depan=$depan belakang=$belakang"

ls /folder/tidak/ada &> /dev/null
echo "7. &>      : pesan error tadi terbuang rapi"

echo "warna=merah" > konfig.sh
source ./konfig.sh
echo "8. source  : warna=$warna"
rm -f konfig.sh

tab=$'\\t'
echo "9. C-quote : ada tab sungguhan di sini ->${tab}<- selesai" """,
            },
            {
                "body": [
                    "Jalankan berkas di atas dengan bash: sembilan baris keluar rapi, tidak ada keluhan.",
                    "Sekarang ubah baris pertamanya jadi #!/bin/sh, jalankan di Debian atau Alpine, dan",
                    "kamu dapat deretan pesan yang tidak satu pun menyebut kata 'bash':",
                    "",
                    "  Syntax error: word unexpected (expecting \")\")   <- baris buah=(...)",
                    "  Syntax error: redirection unexpected            <- baris <<<",
                    "  [[: not found                                   <- [[ ]] bukan sintaks di sh",
                    "  Bad substitution                                <- ${nama^^}",
                    "  pesan+= dunia: not found                        <- += pada string",
                    "  n++: not found                                  <- (( )) dibaca jadi subshell",
                    "  source: not found                               <- sh cuma punya titik: . berkas",
                    "",
                    "Perhatikan dua hal yang membuat pesan ini sulit dikenali pemula.",
                    "",
                    "Pertama, urutannya. Dua yang berlabel 'Syntax error' ketahuan saat sh MEMBACA",
                    "berkasnya, sebelum satu baris pun dijalankan. Jadi script tidak mencetak apa-apa",
                    "sama sekali — bukan 'jalan separuh lalu berhenti'. Nomor barisnya pun menunjuk ke",
                    "tempat sh menyerah, bukan selalu ke baris yang salah.",
                    "",
                    "Kedua, kata 'not found'. Bagi sh, [[ dan n++ dan source cuma NAMA PERINTAH biasa",
                    "yang kebetulan tidak ada di PATH. Ia tidak tahu kamu sedang bermaksud memakai fitur",
                    "bash, jadi ia tidak bisa memberi tahu itu. 'command not found' pada tanda kurung",
                    "siku hampir selalu berarti satu hal: script bash dijalankan oleh shell yang bukan",
                    "bash.",
                    "",
                    "Yang paling jahat justru bashism yang TIDAK memberi pesan apa pun:",
                    "",
                    "  ls /folder/tidak/ada &> /dev/null",
                    "",
                    "  Di sh, & adalah operator 'jalankan di latar belakang' dan ia MENUTUP perintah.",
                    "  Baris itu dibaca jadi dua: 'ls ... &' dilepas ke latar, lalu '> /dev/null'",
                    "  berdiri sendiri sebagai perintah kosong yang cuma membuat berkas. Akibatnya:",
                    "  pesan error tetap tumpah ke layar, dan script lanjut seolah semua beres.",
                    "  Kalau maksudmu 'cmd &> laporan.log', berkas laporan.log dibuat lalu dikosongkan",
                    "  dan tidak pernah diisi apa-apa. Tidak ada error, cuma hasil yang salah.",
                    "",
                    "Daftar bashism dan padanan POSIX-nya. Kolom kanan jalan di bash MAUPUN sh:",
                    "",
                    "  bash                          POSIX sh",
                    "  [[ \"$a\" == \"$b\" ]]            [ \"$a\" = \"$b\" ]        (satu = saja)",
                    "  [[ $a == x && $b == y ]]      [ \"$a\" = x ] && [ \"$b\" = y ]",
                    "  [[ \"$t\" == *abc* ]]           case \"$t\" in *abc*) ... ;; esac",
                    "  [[ \"$t\" =~ ^[0-9]+$ ]]        case \"$t\" in \"\"|*[!0-9]*) BUKAN angka ;; esac",
                    "  arr=(a b c) ; ${arr[1]}       set -- a b c ; $2",
                    "  declare -A peta               tidak ada padanannya sama sekali",
                    "  ((n++))                       n=$((n + 1))",
                    "  teks+=\"lagi\"                  teks=\"${teks}lagi\"",
                    "  ${teks^^} / ${teks,,}         tr '[:lower:]' '[:upper:]'",
                    "  ${teks:0:5}                   printf '%.5s' \"$teks\"",
                    "  ${teks/lama/baru}             sed 's/lama/baru/'",
                    "  read x <<< \"$teks\"            heredoc: read x << EOF ... EOF",
                    "  cmd &> berkas                 cmd > berkas 2>&1",
                    "  echo -e \"a\\tb\"                printf 'a\\tb\\n'",
                    "  $'\\t'  (C-quote)              printf, atau tab sungguhan di dalam petik",
                    "  function f { ... }            f() { ... }",
                    "  source berkas                 . ./berkas",
                    "  local x=1                     ADA di dash & busybox, tapi bukan janji POSIX",
                    "",
                    "Baris terakhir itu jebakan halus: local jalan di hampir semua sh yang akan kamu",
                    "temui, jadi orang memakainya terus. Tapi ia tidak dijamin standar. Kalau targetmu",
                    "benar-benar 'shell apa pun', pakai nama variabel berawalan khas seperti _cetak_n.",
                    "",
                    "Perhatikan juga ${teks:0:5} dan ${teks/lama/baru}. Materi Operasi String",
                    "mengajarkan keduanya berbarengan dengan ${#teks}, ${berkas%.txt}, dan",
                    "${var:-bawaan} seolah satu keluarga. Padahal yang belakangan itu POSIX asli,",
                    "sedangkan substring dan penggantian teks murni bashism. Sekumpulan ${} yang",
                    "bentuknya mirip, nasibnya berbeda.",
                ],
            },
            {
                "heading": "posix.sh — pekerjaan yang sama, tanpa satu pun bashism",
                "code": """#!/bin/sh
# Jalan di dash, busybox ash, bash, zsh - sh mana pun.

nama="levi anggara"

case "$nama" in
    *anggara*) echo "1. case   : pola cocok, pengganti [[ == ]]" ;;
esac

# Tidak ada array di sh. Argumen posisi adalah satu-satunya daftar bawaan.
set -- apel jeruk mangga
echo "2. set -- : $2, jumlah $#"

besar=$(printf '%s' "$nama" | tr '[:lower:]' '[:upper:]')
echo "3. tr     : $besar"

pesan="halo"
pesan="$pesan dunia"
echo "4. gabung : $pesan"

n=0
n=$((n + 1))
n=$((n + 7))
echo "5. hitung : $n"

depan=${nama%% *}
belakang=${nama#* }
echo "6. potong : depan=$depan belakang=$belakang"

ls /folder/tidak/ada > /dev/null 2>&1
echo "7. 2>&1   : pesan error tadi terbuang rapi"

echo "warna=merah" > konfig.sh
. ./konfig.sh
echo "8. titik  : warna=$warna"
rm -f konfig.sh

if [ -n "$warna" ] && [ "$warna" = merah ]; then
    echo "9. [ ]    : satu = saja, dan dua [ ] disambung dengan &&"
fi""",
            },
            {
                "body": [
                    "Dua catatan dari posix.sh.",
                    "",
                    "  . ./konfig.sh    Titiknya wajib diikuti ./ kalau berkasnya di folder saat ini.",
                    "                   Tanpa garis miring, sh mencari berkas itu di PATH — dan",
                    "                   biasanya tidak menemukannya. bash lebih longgar soal ini,",
                    "                   jadi kebiasaan 'source konfig.sh' baru rusak di sh.",
                    "",
                    "  $(( n + 1 ))     Aritmatika $(( )) ITU POSIX. Yang bashism cuma bentuk ((n++))",
                    "                   yang berdiri sendiri sebagai perintah. Jangan sampai tertukar.",
                    "",
                    "Sekarang soal [ ] — dan kenapa ia bertebaran di kode nyata.",
                    "",
                    "Materi Percabangan (if, case) menyebut [ ] sebagai 'perintah lama' dan menyuruhmu",
                    "memakai [[ ]]. Itu benar, SELAMA shebang-mu bash. Begitu berkasnya #!/bin/sh, [[ ]]",
                    "tidak ada, dan [ ] jadi satu-satunya cara membandingkan apa pun. Jadi kalau kamu",
                    "membuka entrypoint sebuah image Docker dan isinya [ -z \"$1\" ] semua, penulisnya",
                    "bukan orang yang ketinggalan zaman — dia sengaja menulis untuk shell yang memang",
                    "tidak punya [[ ]].",
                    "",
                    "Kata 'perintah' di situ harfiah. [ benar-benar sebuah program, ada berkasnya:",
                    "  ls -l /usr/bin/[        -> ada, kembarannya bernama test",
                    "Karena ia perintah biasa, isi variabel dipecah oleh spasi DULU sebelum [ sempat",
                    "melihatnya. Itulah sebabnya:",
                    "  x=\"dua kata\" ; [ $x = ya ]   ->  bash: [: too many arguments",
                    "Di dalam [ ] petik ganda WAJIB, bukan anjuran seperti di [[ ]]. [[ ]] aman karena",
                    "ia sintaks yang dibaca shell sendiri, bukan perintah yang menerima daftar kata.",
                    "",
                    "Menguji portabilitas sebelum script dipakai orang lain:",
                    "",
                    "  sh -n script.sh        Cek sintaks tanpa menjalankan. Menangkap array dan <<<,",
                    "                         tapi TIDAK menangkap [[ ]] — bagi sh itu cuma nama",
                    "                         perintah, dan nama perintah baru dicari saat dijalankan.",
                    "  dash script.sh         Menjalankannya sungguhan di dash. Bukti paling jujur.",
                    "                         Pasang dulu: apt install dash",
                    "  shellcheck -s sh f.sh  shellcheck sudah dikenalkan di materi Debugging &",
                    "                         Praktik Baik. Bendera -s memaksanya menilai dengan aturan",
                    "                         sh, lalu ia menandai tiap bashism satu per satu berikut",
                    "                         padanan POSIX-nya.",
                    "  checkbashisms f.sh     Alat yang tugasnya cuma itu (paket devscripts di Debian).",
                    "",
                    "JEBAKAN BESAR saat menguji: di Fedora dan Arch, /bin/sh SENDIRI adalah bash. Jadi",
                    "'sh script.sh' di mesin seperti itu bisa lolos mulus padahal script-nya penuh",
                    "bashism — bash dalam mode sh tetap mengerti [[ ]], array, dan <<<. Lulus uji di",
                    "sana tidak membuktikan apa pun. Pasang dash, atau jalankan di container Alpine.",
                    "",
                    "Kapan pilih yang mana:",
                    "  - Pakai bash kalau script-nya untuk mesin yang kamu kendalikan, atau kamu butuh",
                    "    array, declare -A, regex =~, dan ${teks^^}. Tulis #!/usr/bin/env bash dan",
                    "    jangan minta maaf. Ini pilihan default yang sehat, bukan kemalasan.",
                    "  - Pakai sh kalau script-nya masuk image Docker minimal, jadi installer yang",
                    "    dipanggil lewat pipe, atau harus jalan di sistem yang tidak kamu kenal.",
                    "",
                    "Yang TIDAK boleh: menulis #!/bin/sh lalu tetap memakai [[ ]] dan array. Di mesinmu",
                    "ia jalan, karena sh-mu bash. Di mesin orang lain ia mati. Ini salah satu bug yang",
                    "paling sering dilaporkan pada script pemasangan. Pilih satu, lalu konsisten",
                    "sepenuhnya — shebang itu janji, dan isi berkas harus menepatinya.",
                ],
            },
        ],
    },
    {
        "title": "24. Fitur Bash Lanjutan",
        "sections": [
            {
                "body": [
                    "Bab ini mengumpulkan hal-hal yang sering muncul di script orang lain tapi",
                    "belum pernah disebut di sini. Bukan fitur eksotis - semuanya lazim di",
                    "script produksi, dan tiap satunya pernah membuat orang mengira bash-nya",
                    "rusak padahal cuma belum tahu aturannya.",
                    "",
                    "DECLARE BUKAN PERINTAH KHUSUS MAP",
                    "",
                    "Sejauh ini declare cuma muncul sekali, sebagai declare -A waktu membuat",
                    "associative array. Wajar kalau kamu mengira itu mantra khusus map.",
                    "Bukan. declare adalah perintah DEKLARASI UMUM: ia membuat variabel",
                    "sekaligus menempelkan SIFAT padanya.",
                    "",
                    "  declare -HURUF nama=nilai",
                    "",
                    "  -i   integer  isinya selalu dihitung sebagai bilangan",
                    "  -r   readonly sekali diisi tidak boleh diubah lagi",
                    "  -a   array    array biasa, indeks angka",
                    "  -A   map      associative array, indeks teks",
                    "  -x   export   ikut terbawa ke program yang dijalankan script ini",
                    "  -g   global   tembus keluar walaupun ditulis di dalam fungsi",
                    "  -n   nameref  variabel yang isinya NAMA variabel lain",
                    "  -p   print    cetak variabel apa adanya lengkap dengan sifatnya",
                    "",
                    "Ternyata ia satu keluarga dengan yang sudah kamu pakai sejak awal:",
                    "",
                    "  local nama=\"Andi\"     sama dengan   declare nama=\"Andi\"   (dalam fungsi)",
                    "  readonly VERSI=\"1.4\"  sama dengan   declare -r VERSI=\"1.4\"",
                    "  export PORT=8080      sama dengan   declare -x PORT=8080",
                    "",
                    "Kerangka script di materi Debugging & Praktik Baik memakai readonly dan",
                    "local di mana-mana. Keduanya cuma nama lain untuk declare dengan satu",
                    "sifat yang sudah dipilihkan.",
                    "",
                    "YANG PALING MENGEJUTKAN: declare -i",
                    "",
                    "  hitung=0             lalu hitung+=1 dua kali  ->  \"011\"",
                    "  declare -i hitung=0  lalu hitung+=1 dua kali  ->  2",
                    "",
                    "Operator += yang PERSIS SAMA berarti dua hal berbeda. Ingat, bash tidak",
                    "punya tipe data: += di variabel biasa artinya menyambung teks, jadi 0",
                    "disambung 1 disambung 1 menghasilkan string \"011\". Sifat -i menempel di",
                    "VARIABELNYA, bukan di operatornya, dan itulah yang mengubah artinya jadi",
                    "penjumlahan. Kalau sebuah += memberi hasil yang aneh, curigai ini dulu.",
                    "",
                    "declare -p adalah alat debugging yang paling sering terlupa:",
                    "",
                    "  declare -p umur",
                    "",
                    "Ia mencetak variabel apa adanya - isinya, dan sekaligus ia itu array,",
                    "map, readonly, atau integer. echo mendiamkan semua informasi itu; echo",
                    "\"$umur\" pada sebuah map bahkan tidak mencetak apa-apa dan membuat kamu",
                    "mengira datanya hilang.",
                ],
            },
            {
                "heading": "declare beraksi",
                "code": "#!/usr/bin/env bash\n\ndeclare -i hitung=0        # -i : bilangan\ndeclare -r VERSI=\"1.4\"     # -r : hanya-baca, sama dengan readonly\ndeclare -A umur=()         # -A : associative array\n\nhitung+=1\nhitung+=1\n\nbiasa=0\nbiasa+=1\nbiasa+=1\n\necho \"declare -i, dua kali +=  : $hitung\"\necho \"variabel biasa, dua kali : $biasa\"\n\n# Variabel -i selalu MENGHITUNG isinya, walau yang diisikan berupa teks\nhitung=\"7 * 6\"\necho \"variabel -i diisi '7 * 6': $hitung\"\n\n# declare -p: lihat isi DAN sifat sebuah variabel\ndeclare -p hitung\ndeclare -p VERSI\ndeclare -p umur\n\n# Menulis ke variabel readonly ditolak. Dicoba di dalam subshell ( ... )\n# supaya script ini tidak ikut mati saat penolakannya terjadi.\nif ( VERSI=\"2.0\" ) 2>/dev/null; then\n    echo \"VERSI berubah\"\nelse\n    echo \"VERSI ditolak: hanya-baca\"\nfi\n\npasang() {\n    declare -g SUDAH=\"ya\"      # -g : tembus keluar dari fungsi\n    local sementara=\"hilang\"   # local = declare biasa di dalam fungsi\n    echo \"di dalam fungsi : sementara=$sementara\"\n}\n\npasang\necho \"setelah fungsi  : SUDAH=$SUDAH sementara=${sementara:-<kosong>}\"",
            },
            {
                "heading": "Nameref: mengoper array ke fungsi",
                "body": [
                    "Materi Array mengajarkan cara membuat array. Materi Fungsi mengajarkan",
                    "cara membuat fungsi. Pertanyaan yang langsung muncul begitu keduanya",
                    "bertemu tidak pernah dijawab: bagaimana mengoper ARRAY ke sebuah fungsi?",
                    "",
                    "Jawaban naifnya tidak bekerja:",
                    "",
                    "  proses \"${buah[@]}\"",
                    "",
                    "Itu bukan mengirim satu array. Array-nya MELELEH jadi argumen terpisah:",
                    "$1=apel, $2=jeruk, $3=mangga. Fungsi tidak punya cara tahu di mana array",
                    "berakhir dan argumen lain mulai, dan sama sekali tidak bisa mengubah",
                    "array aslinya.",
                    "",
                    "Nameref menjawabnya. Kirim NAMA array-nya - tanpa tanda dolar - lalu di",
                    "dalam fungsi:",
                    "",
                    "  local -n daftar=\"$1\"",
                    "",
                    "Sekarang 'daftar' bukan salinan, melainkan nama lain untuk variabel yang",
                    "namanya tersimpan di $1. Menulis ke daftar berarti menulis ke array",
                    "aslinya. Ini satu-satunya cara rapi mengoper DAN mengubah array di dalam",
                    "fungsi. Perlu bash 4.3 ke atas.",
                    "",
                    "JEBAKAN nameref: nama lokalnya tidak boleh sama dengan nama yang dikirim.",
                    "",
                    "  tambah() { local -n daftar=\"$1\"; daftar+=(\"x\"); }",
                    "  daftar=(\"a\"); tambah daftar",
                    "",
                    "bash mengeluh 'circular name reference' karena diminta menunjuk dirinya",
                    "sendiri. Itu sebabnya kebiasaan yang berlaku adalah memberi awalan garis",
                    "bawah pada nameref: local -n _daftar=\"$1\".",
                    "",
                    "EKSPANSI TAK LANGSUNG ${!nama}",
                    "",
                    "Ini kembaran nameref versi sekali pakai: ambil nilai dari variabel yang",
                    "NAMANYA tersimpan di $nama.",
                    "",
                    "  warna=\"hijau\"; kunci=\"warna\"; echo \"${!kunci}\"   ->  hijau",
                    "",
                    "Dua bentuk yang mirip sekali tapi artinya jauh berbeda:",
                    "",
                    "  ${!kunci}      nilai variabel yang NAMANYA ada di $kunci",
                    "  ${!buah[@]}    DAFTAR INDEKS array buah (sudah dipakai di materi Array)",
                    "",
                    "Tanda seru yang sama, aturan yang lain sama sekali. Yang menentukan",
                    "adalah ada tidaknya [@] di belakangnya.",
                    "",
                    "EXPORT -F",
                    "",
                    "Variabel bisa di-export supaya terbawa ke proses anak. Fungsi TIDAK,",
                    "kecuali diminta:",
                    "",
                    "  export -f sapa",
                    "",
                    "Tanpa itu, fungsi yang dipanggil di dalam bash -c, xargs, atau",
                    "find -exec akan menghasilkan 'sapa: command not found' - pesan yang",
                    "membingungkan, karena fungsinya jelas-jelas ada beberapa baris di atas.",
                    "Yang berubah bukan keberadaannya, tapi SIAPA yang menjalankannya: itu",
                    "proses bash lain, dan proses itu belum pernah membaca script kamu.",
                ],
                "code": """#!/usr/bin/env bash

tambah() {
    local -n daftar="$1"      # daftar = nama lain untuk array di pemanggil
    daftar+=("$2")
}

ringkas() {
    local -n daftar="$1"
    echo "  isi (${#daftar[@]} item): ${daftar[*]}"
}

buah=("apel" "jeruk")
tambah buah "mangga"          # kirim NAMANYA saja, tanpa tanda dolar
ringkas buah

# Ekspansi tak langsung: nilai dari variabel yang namanya ada di $kunci
warna_favorit="hijau"
kunci="warna_favorit"
echo "nilai lewat \\${!kunci} : ${!kunci}"

# Bentuk mirip, arti beda: ini DAFTAR INDEKS, bukan tak langsung
echo "indeks buah          : ${!buah[@]}"

sapa() { echo "  halo $1, dari fungsi $FUNCNAME"; }
export -f sapa

echo "dipanggil dari proses bash anak:"
bash -c 'sapa "Andi"'

echo "dipanggil lewat xargs:"
printf '%s\\n' "Budi" "Citra" | xargs -I{} bash -c 'sapa "{}"'""",
            },
            {
                "heading": "PIPESTATUS: exit code tiap tahap pipeline",
                "body": [
                    "$? cuma memberi kode keluar perintah TERAKHIR. Di sebuah pipeline, yang",
                    "terakhir itu tahap paling kanan - dan tahap paling kanan sering cuma",
                    "penyalur yang hampir selalu sukses.",
                    "",
                    "  jalankan_tes | tee hasil.log",
                    "",
                    "Kalau jalankan_tes gagal tapi tee berhasil menulis log, $? bernilai 0.",
                    "Di CI, artinya build dinyatakan HIJAU padahal tesnya merah - kegagalan",
                    "yang bersembunyi di balik exit code milik tee. Bug seperti ini bisa",
                    "bertahan berbulan-bulan karena tidak ada satu pun yang terlihat salah.",
                    "",
                    "${PIPESTATUS[@]} adalah array berisi kode keluar SETIAP tahap:",
                    "",
                    "  ${PIPESTATUS[0]}    tahap pertama",
                    "  ${PIPESTATUS[-1]}   tahap terakhir, ini yang nilainya sama dengan $?",
                    "",
                    "Perbaikannya satu baris:  exit \"${PIPESTATUS[0]}\"",
                    "",
                    "JEBAKANNYA umurnya cuma satu perintah. PIPESTATUS ditulis ulang oleh",
                    "perintah BERIKUTNYA - termasuk oleh echo, oleh [[ ]], bahkan oleh",
                    "pengisian variabel biasa. Jadi ini salah:",
                    "",
                    "  uji | tee log",
                    "  echo \"selesai\"",
                    "  exit \"${PIPESTATUS[0]}\"     <- ini kode keluar echo, bukan uji",
                    "",
                    "Salin dulu, baru dipakai:  tahap=(\"${PIPESTATUS[@]}\")",
                    "",
                    "Kalau kamu tidak perlu tahu tahap mana yang gagal dan cuma ingin pipeline",
                    "dianggap gagal begitu ada bagian yang gagal, set -o pipefail dari materi",
                    "Argumen & Exit Code sudah cukup. PIPESTATUS dipakai saat kamu perlu",
                    "menunjuk tahap tertentu.",
                ],
                "code": """#!/usr/bin/env bash

# Tahap PERTAMA gagal, tahap terakhir (tee) sukses.
uji() {
    echo "3 tes dijalankan, 1 gagal"
    return 1
}

uji | tee hasil.log > /dev/null

# Disalin LEBIH DULU, sebelum perintah apa pun menimpanya
tahap=("${PIPESTATUS[@]}")

echo "kode keluar tiap tahap : ${tahap[*]}"
echo "yang terbaca lewat \\$?  : ${tahap[-1]}  <- milik tee, bukan milik uji"

if [[ "${tahap[0]}" -ne 0 ]]; then
    echo "tahap pertama gagal -> build harus dinyatakan MERAH"
fi

# Di CI, penutup script-nya begini supaya kegagalan tidak tersembunyi:
#   exit "${tahap[0]}"

rm -f hasil.log""",
            },
            {
                "heading": "shopt dan variabel khusus",
                "body": [
                    "set -e, set -u, dan set -o pipefail sudah kamu kenal. shopt adalah kotak",
                    "saklar yang LAIN, berisi puluhan opsi khusus bash:",
                    "",
                    "  shopt -s nama    nyalakan",
                    "  shopt -u nama    matikan",
                    "  shopt            lihat semuanya beserta statusnya",
                    "",
                    "nullglob dari materi Bekerja dengan File & Folder adalah salah satunya.",
                    "Empat lagi yang paling sering kamu temui di script orang:",
                    "",
                    "  globstar     ** cocok menembus subfolder:  src/**/*.js",
                    "               Tanpa ini, ** tidak lebih dari * biasa - satu tingkat saja.",
                    "  extglob      pola diperluas:",
                    "                 !(*.txt)   semua KECUALI yang berakhiran .txt",
                    "                 +(a|b)     satu kali atau lebih a atau b",
                    "                 @(x|y)     tepat satu dari x atau y",
                    "                 ?(x)       nol atau satu x",
                    "  nocasematch  [[ ]] dan case jadi abai huruf besar/kecil",
                    "  failglob     pola yang tidak cocok apa pun jadi ERROR, bukan didiamkan",
                    "",
                    "JEBAKAN extglob yang bikin bingung: shopt -s extglob mengubah cara bash",
                    "MEMBACA pola, bukan cuma cara mencocokkannya. Pola seperti !(*.txt) baru",
                    "SAH sebagai sintaks kalau extglob sudah menyala saat barisnya dibaca.",
                    "Dua akibat nyatanya:",
                    "",
                    "  - Taruh shopt -s extglob di paling atas script. Kalau ia dan polanya",
                    "    berada di dalam satu fungsi atau satu blok { } yang sama, bash sudah",
                    "    terlanjur membaca seluruh blok itu sebelum shopt sempat jalan, dan",
                    "    yang muncul adalah syntax error - bukan pola yang gagal cocok.",
                    "  - bash -n script.sh akan MELAPORKAN syntax error di pola extglob,",
                    "    padahal script-nya jalan mulus. bash -n cuma membaca, jadi shopt-nya",
                    "    tidak pernah dijalankan. Jangan buru-buru percaya laporan itu.",
                    "",
                    "Jalan aman yang tidak tersandung keduanya: simpan polanya di variabel,",
                    "",
                    "  bukan_txt='!(*.txt)'",
                    "  for f in demo/$bukan_txt; do ...",
                    "",
                    "Polanya baru terbentuk saat script berjalan, jadi pembacaannya tidak",
                    "pernah bermasalah. Itu bentuk yang dipakai di contoh di bawah.",
                    "",
                    "nocasematch layak diwaspadai: ia mengubah arti kode yang sudah ditulis,",
                    "diam-diam, dari kejauhan. Sebuah [[ \"$x\" == \"ya\" ]] di baris 200 bisa",
                    "berubah perilaku gara-gara satu shopt -s di baris 3, dan kodenya sendiri",
                    "tidak menunjukkan tanda apa pun. Nyalakan seperlunya, lalu matikan lagi.",
                    "",
                    "VARIABEL KHUSUS SISANYA",
                    "",
                    "  $RANDOM        bilangan acak 0-32767. Untuk main-main saja, JANGAN",
                    "                 untuk password atau token - polanya bisa ditebak.",
                    "  $SECONDS       detik sejak script mulai. Cara termurah mengukur durasi.",
                    "  $LINENO        nomor baris ini. Berguna di pesan debug.",
                    "  $FUNCNAME      nama fungsi yang sedang berjalan.",
                    "  $EUID          user id efektif. 0 berarti root.",
                    "  $PWD           folder saat ini.",
                    "  $OLDPWD        folder sebelumnya, yang dituju oleh  cd -",
                    "  $OSTYPE        linux-gnu, darwin23, msys, ... untuk kode yang perlu",
                    "                 berbeda perlakuan antar sistem.",
                    "  $BASH_VERSION  versi bash. Dipakai untuk menolak jalan di bash 3.",
                    "",
                    "DUA NAMA TERAKHIR, sekadar supaya tidak asing saat terbaca:",
                    "",
                    "  readarray -t baris < berkas.txt",
                    "    Baca semua baris jadi array sekaligus. Namanya juga mapfile - dua",
                    "    nama untuk perintah yang sama. -t membuang newline di tiap baris.",
                    "    Lebih ringkas daripada loop while read, tapi ia memuat seluruh isi",
                    "    ke memori, jadi jangan untuk berkas raksasa.",
                    "",
                    "  coproc SEBUT { perintah; }",
                    "    Menjalankan perintah di latar dengan pipa dua arah, sehingga script",
                    "    bisa berkirim-kiriman data dengannya. Jarang dibutuhkan; cukup tahu",
                    "    kata ini ada supaya tidak panik saat melihatnya.",
                ],
                "code": """#!/usr/bin/env bash

shopt -s globstar extglob nocasematch

mkdir -p demo/alat/dalam
: > demo/catatan.txt
: > demo/alat/pasang.sh
: > demo/alat/dalam/uji.sh

echo "== globstar: ** menembus semua subfolder =="
for f in demo/**/*.sh; do
    echo "   $f"
done

# Polanya disimpan di variabel supaya aman dibaca; lihat penjelasan di atas
bukan_txt='!(*.txt)'

echo "== extglob: !(*.txt) = semua KECUALI berakhiran .txt =="
for f in demo/$bukan_txt; do
    echo "   $f"
done

echo "== nocasematch: pencocokan jadi abai huruf besar/kecil =="
jawab="YA"
[[ "$jawab" == "ya" ]] && echo "   'YA' cocok dengan 'ya'"
shopt -u nocasematch
[[ "$jawab" == "ya" ]] || echo "   setelah dimatikan, 'YA' tidak cocok lagi"

echo "== variabel khusus =="
echo "   detik sejak script mulai : $SECONDS"
echo "   nomor baris ini          : $LINENO"
siapa() { echo "   nama fungsi ini          : $FUNCNAME"; }
siapa
echo "   jenis sistem             : $OSTYPE"
if [[ $EUID -eq 0 ]]; then
    echo "   dijalankan sebagai root"
else
    echo "   bukan root (EUID=$EUID)"
fi

# readarray: baris-baris jadi array, tanpa loop while read
readarray -t baris < <(printf 'satu\\ndua\\ntiga\\n')
echo "   readarray dapat ${#baris[@]} baris, yang kedua: ${baris[1]}"

rm -rf ./demo""",
            },
        ],
    },
    {
        "title": "25. Studi Kasus: Pengelola Catatan",
        "sections": [
            {
                "body": [
                    "Kita gabungkan semua yang sudah dipelajari menjadi satu",
                    "aplikasi CLI kecil: pengelola catatan sederhana.",
                    "",
                    "Fitur:",
                    "  - tambah <isi>   simpan catatan baru",
                    "  - daftar         tampilkan semua catatan bernomor",
                    "  - cari <kata>    cari catatan yang memuat kata",
                    "  - hapus <nomor>  hapus catatan nomor tertentu",
                    "  - hitung         tampilkan jumlah catatan",
                    "",
                    "Konsep yang dipakai:",
                    "  shebang, set -euo pipefail, fungsi, local, case,",
                    "  perulangan while read, argumen $@, exit code,",
                    "  operasi string, redirection, dan heredoc.",
                ]
            },
            {
                "heading": "catatan.sh",
                "code": """#!/usr/bin/env bash
set -euo pipefail

readonly BERKAS="${CATATAN_FILE:-$HOME/.catatan.txt}"
readonly NAMA="${0##*/}"

siapkan() {
    [[ -f "$BERKAS" ]] || touch "$BERKAS"
}

tambah() {
    local isi="$*"
    [[ -n "$isi" ]] || { echo "Isi catatan kosong" >&2; return 1; }
    echo "$isi" >> "$BERKAS"
    echo "Tersimpan: $isi"
}

daftar() {
    local n=0
    while IFS= read -r baris; do
        ((n++))
        printf "%3d. %s\\n" "$n" "$baris"
    done < "$BERKAS"
    [[ $n -eq 0 ]] && echo "(belum ada catatan)"
    return 0
}

cari() {
    local kata="$1"
    local n=0 ketemu=0
    while IFS= read -r baris; do
        ((n++))
        if [[ "${baris,,}" == *"${kata,,}"* ]]; then
            printf "%3d. %s\\n" "$n" "$baris"
            ((ketemu++))
        fi
    done < "$BERKAS"
    echo "Ditemukan $ketemu catatan."
}

hapus() {
    local target="$1"
    local total
    total=$(wc -l < "$BERKAS")
    if [[ ! "$target" =~ ^[0-9]+$ ]] || (( target < 1 || target > total )); then
        echo "Nomor tidak valid (1-$total)" >&2
        return 1
    fi
    sed -i "${target}d" "$BERKAS"
    echo "Catatan $target dihapus."
}

hitung() {
    echo "Total catatan: $(wc -l < "$BERKAS")"
}

bantuan() {
    cat << EOF
$NAMA - pengelola catatan sederhana

  $NAMA tambah <isi>
  $NAMA daftar
  $NAMA cari <kata>
  $NAMA hapus <nomor>
  $NAMA hitung
EOF
}

siapkan
perintah="${1:-bantuan}"
shift || true

case "$perintah" in
    tambah)  tambah "$@" ;;
    daftar)  daftar ;;
    cari)    cari "${1:-}" ;;
    hapus)   hapus "${1:-}" ;;
    hitung)  hitung ;;
    *)       bantuan ;;
esac"""
            },
            {
                "body": [
                    "Bagian menarik dari script ini:",
                    "",
                    "  \"${CATATAN_FILE:-$HOME/.catatan.txt}\"",
                    "    Lokasi file bisa diubah lewat variabel lingkungan.",
                    "    Ini membuat script mudah diuji tanpa mengotori data asli.",
                    "",
                    "  \"${baris,,}\" == *\"${kata,,}\"*",
                    "    Ubah keduanya jadi huruf kecil, lalu cocokkan dengan",
                    "    wildcard * di kiri-kanan. Ini pencarian yang mengabaikan",
                    "    besar-kecil huruf tanpa memanggil grep.",
                    "",
                    "  shift || true",
                    "    shift membuang argumen pertama. Kalau tidak ada argumen,",
                    "    shift gagal dan set -e akan menghentikan script.",
                    "    || true mencegah itu.",
                    "",
                    "  [[ ! \"$target\" =~ ^[0-9]+$ ]]",
                    "    Validasi input harus berupa angka sebelum dipakai",
                    "    di perhitungan. Jangan pernah percaya input user.",
                    "",
                    "Latihan lanjutan yang bisa kamu coba sendiri:",
                    "  - Tambah perintah 'ubah <nomor> <isi baru>'",
                    "  - Simpan tanggal pembuatan tiap catatan",
                    "  - Tambah penanda selesai/belum untuk tiap catatan",
                    "  - Tulis pengujian otomatisnya dengan bats",
                ]
            },
        ],
    },
]
