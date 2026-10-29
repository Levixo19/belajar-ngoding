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
                "heading": "Shebang, cara menjalankan, dan sambung baris",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Teknisi yang ngurus server toko online atau lab komputer sekolah sering",
                    "mengetik deretan perintah yang sama tiap hari. Begitu deretan itu",
                    "disimpan jadi script, satu perintah cukup untuk menjalankan semuanya,",
                    "dan urutannya nggak pernah ketuker.",
                    "",
                    "Kasus kecil: tiap sore kamu mengetik mkdir cadangan, cp -r laporan/",
                    "cadangan/, lalu echo untuk menandai tugasnya selesai. Kamu mau cukup",
                    "mengetik ./cadangkan.sh.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis dulu perintahnya persis seperti yang biasa kamu ketik, urut",
                    "     dari atas ke bawah. Itulah isi script-nya.",
                    "  2. Tambahkan shebang di baris pertama, lalu simpan sebagai",
                    "     cadangkan.sh:",
                    "      #!/usr/bin/env bash",
                    "      mkdir cadangan",
                    "      cp -r laporan/ cadangan/",
                    "      echo \"Laporan sudah dicadangkan.\"",
                    "  3. Kasih izin eksekusi sekali dengan chmod +x cadangkan.sh, lalu",
                    "     jalankan ./cadangkan.sh dari folder yang berisi laporan/.",
                    "  4. Jalankan dua kali. Di percobaan kedua mkdir mengeluh folder",
                    "     cadangan udah ada, tapi baris sesudahnya tetap jalan. Baris di",
                    "     script berlaku seperti perintah yang dipisah titik koma: gagal di",
                    "     satu baris nggak menghentikan baris berikutnya.",
                    "",
                    "Jebakan: kalau baris cp kamu pecah pakai backslash lalu ada spasi",
                    "sesudahnya, cp menyalin laporan/ ke folder bernama satu spasi, dan",
                    "baris berikutnya dijalankan sebagai perintah sendiri.",
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
                "heading": "Izin dalam bentuk angka dan simbolik",
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
                "heading": "Kunci SSH, sudo, dan chown",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di hosting web, izin berkas menentukan apakah situs jalan atau malah",
                    "bocor. Script deploy perlu bit x supaya bisa dijalankan, sedangkan",
                    "berkas .env yang berisi password database toko online cuma boleh",
                    "dibaca pemiliknya. Pesan 'Permission denied' di server hampir selalu",
                    "urusan tiga huruf rwx ini.",
                    "",
                    "Kasus kecil: kamu mengunduh backup.sh dan .env dari lampiran email.",
                    "./backup.sh ditolak dengan exit code 126, dan ls -l menunjukkan .env",
                    "berizin -rw-r--r--, artinya semua akun di mesin itu bisa membaca",
                    "password-nya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca dulu keadaannya dengan ls -l. Kolom pertama memberi tahu",
                    "     golongan mana yang kurang atau kelebihan izin.",
                    "  2. Tentukan keadaan akhirnya: script 755 (semua boleh menjalankan,",
                    "     cuma kamu yang mengubah), berkas rahasia 600 (cuma untukmu).",
                    "  3. Pakai bentuk angka, karena hasilnya pasti apa pun izin lamanya:",
                    "      chmod 755 backup.sh",
                    "      chmod 600 .env",
                    "      stat -c '%a %A %n' backup.sh .env",
                    "     Hasilnya 755 -rwxr-xr-x backup.sh dan 600 -rw------- .env.",
                    "  4. Periksa kasus pinggir: chmod +x tanpa nyebut siapa disaring umask.",
                    "     Dengan umask 077, berkas 644 cuma jadi 744, jadi anggota grup tetap",
                    "     nggak bisa menjalankannya. Tulis 755 atau a+x kalau maksudnya semua",
                    "     orang.",
                    "",
                    "Jebakan: jangan beresin masalah izin pakai chmod 777. Script-mu jadi",
                    "bisa ditulis ulang oleh siapa pun yang punya akun di mesin itu.",
                ]
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
                "heading": "Ringkasan quoting dan variabel khusus",
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
                "heading": "$( ) membuka konteks kutip baru",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan dari kantor atau sekolah hampir selalu bernama panjang dan",
                    "berspasi, misalnya \"rekap nilai 7A.txt\". Script yang mengolah berkas",
                    "seperti itu bergantung pada variabel dan petik ganda. Satu petik yang",
                    "lupa bikin nama itu pecah jadi tiga kata, dan perintahnya bekerja pada",
                    "berkas yang salah.",
                    "",
                    "Kasus kecil: kamu mau menyalin \"rekap nilai 7A.txt\" jadi arsip",
                    "bernama arsip_<tahun>_rekap nilai 7A.txt, dengan tahun diambil otomatis",
                    "dari tanggal komputer.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah nama tujuannya jadi tiga bagian: teks tetap arsip_, tahun,",
                    "     dan nama berkas asli.",
                    "  2. Simpan nama berkas dan tahun di variabel. Tahunnya diambil lewat",
                    "     command substitution:",
                    "      berkas=\"rekap nilai 7A.txt\"",
                    "      tahun=$(date +%Y)",
                    "      cp \"$berkas\" \"arsip_${tahun}_$berkas\"",
                    "  3. Perhatikan kurung kurawal di ${tahun}. Kalau ditulis",
                    "     \"arsip_$tahun_$berkas\", bash mencari variabel bernama tahun_,",
                    "     yang nggak ada. Hasilnya arsip_rekap nilai 7A.txt, tanpa tahun",
                    "     dan tanpa pesan error. Garis bawah boleh jadi bagian nama",
                    "     variabel, jadi bash nggak tahu namanya berhenti di mana.",
                    "  4. Coba juga versi tanpa petik. cp $berkas tujuan membuat cp",
                    "     menerima rekap, nilai, dan 7A.txt sebagai tiga berkas terpisah,",
                    "     lalu menolak perintahnya.",
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
                "heading": "Opsi read, redirection, dan pipe",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Struk kasir, laporan stok warung, dan rekap absensi yang dicetak dari",
                    "terminal butuh kolom yang lurus. Script laporan harian memakai printf",
                    "untuk itu, lalu menyimpan hasilnya ke berkas lewat > atau >> supaya",
                    "bisa dikirim ke pemilik toko.",
                    "",
                    "Kasus kecil: warungmu punya tiga barang, yaitu gula (stok 12), minyak",
                    "goreng (3), dan telur (40). Kamu mau tabel stok yang rapi di stok.txt,",
                    "dengan judul kolom di baris pertama.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan bentuk satu baris: nama rata kiri, angka rata kanan.",
                    "     Formatnya %-10s untuk nama dan %5d untuk stok.",
                    "  2. Tulis judul dengan > supaya isi lama ditimpa, lalu isi tabel",
                    "     dengan >> supaya judulnya nggak hilang:",
                    "      printf '%-10s %5s\\n' \"Barang\" \"Stok\" > stok.txt",
                    "      printf '%-10s %5d\\n' gula 12 \"minyak goreng\" 3 telur 40 >> stok.txt",
                    "      cat stok.txt",
                    "  3. printf mengulang formatnya sampai argumen habis, jadi satu",
                    "     perintah cukup untuk ketiga barang. Nama yang berspasi wajib",
                    "     diberi petik.",
                    "  4. Lihat hasilnya. Baris minyak goreng menggeser angkanya ke kanan,",
                    "     karena namanya 13 huruf, lebih panjang dari lebar 10. Lebar di",
                    "     printf itu batas minimal. Ganti jadi %-14s di kedua baris, dan",
                    "     kolomnya lurus lagi.",
                    "",
                    "Jebakan: kalau baris isi ikut ditulis pakai >, judulnya tertimpa, dan",
                    "yang tersisa di stok.txt cuma barang-barangnya.",
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
                "heading": "Mendiamkan keluaran, exec, dan tee",
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
                "heading": "Here-string, membaca berkas, dan perintah kosong",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Script backup yang jalan sendiri tiap malam di server nggak punya",
                    "orang yang menonton layarnya. Jejaknya cuma berkas log, jadi stdout",
                    "dan stderr harus sama-sama masuk ke sana. Kalau pesan error cuma lewat",
                    "di layar, besok paginya kamu nggak tahu kenapa cadangannya kosong.",
                    "",
                    "Kasus kecil: backup.sh menyalin data/ ke cadangan/, dan kamu",
                    "menjalankannya dengan ./backup.sh 2>&1 > backup.log. Paginya folder",
                    "cadangan/ nggak ada, dan log-nya nggak memuat satu pun pesan error.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua aliran di kepala: stdout untuk hasil, stderr untuk",
                    "     pesan error. Keluhan cp yang gagal lewat stderr.",
                    "  2. Baca redirection-nya dari kiri ke kanan. 2>&1 dikerjakan duluan,",
                    "     waktu stdout masih menunjuk ke layar, jadi error ikut ke layar.",
                    "  3. Supaya nggak ada baris yang lupa dialihkan, alihkan seluruh script",
                    "     sekali di kepalanya dengan exec:",
                    "      #!/usr/bin/env bash",
                    "      LOG=\"backup.log\"",
                    "      exec >>\"$LOG\" 2>&1",
                    "      echo \"mulai backup\"",
                    "      cp -r data/ cadangan/",
                    "      echo \"selesai\"",
                    "  4. Uji dengan folder data/ yang sengaja nggak ada. Layar tetap",
                    "     kosong, dan backup.log berisi tiga baris: mulai backup, pesan cp",
                    "     yang menyebut data/ nggak ditemukan, lalu selesai.",
                    "",
                    "Ingat: sesudah exec >>\"$LOG\", echo apa pun ikut masuk log. Kalau masih",
                    "perlu menulis ke layar, simpan dulu tujuannya dengan exec 4>&1.",
                ]
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek bash yang dipakai tim jarang cuma satu berkas. Biasanya ada",
                    "config.sh berisi alamat database, dan script deploy yang memuatnya",
                    "dengan source. Script itu juga sering dipanggil dari folder lain,",
                    "misalnya oleh jadwal otomatis yang mulai di folder home.",
                    "",
                    "Kasus kecil: alat/deploy.sh memuat config dengan source config.sh.",
                    "Dari dalam folder alat semuanya lancar. Dari folder lain, keluar pesan",
                    "'config.sh: No such file or directory', lalu script lanjut menyambung",
                    "ke alamat kosong.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tanya dulu: config.sh dicari dari folder mana? Jalur relatif",
                    "     dihitung dari folder pemanggil, bukan dari folder script.",
                    "  2. Tetap pakai source, jangan bash config.sh. DB_HOST harus menempel",
                    "     di shell deploy.sh, dan cuma source yang nggak membuat proses",
                    "     baru.",
                    "  3. Hitung folder script-nya sendiri dengan idiom SCRIPT_DIR, lalu",
                    "     muat config dari situ:",
                    "      SCRIPT_DIR=\"$(cd \"$(dirname \"${BASH_SOURCE[0]}\")\" && pwd)\"",
                    "      source \"$SCRIPT_DIR/config.sh\"",
                    "      echo \"Menyambung ke $DB_HOST, database $DB_NAMA\"",
                    "  4. Uji dari dua tempat: bash alat/deploy.sh dari folder proyek, dan",
                    "     bash ../alat/deploy.sh dari folder lain. Dua-duanya harus mencetak",
                    "     alamat yang sama.",
                    "",
                    "Jebakan: berkas yang di-source bisa menjalankan perintah apa pun di",
                    "shell-mu. Isi config.sh cukup baris seperti DB_HOST=\"localhost\".",
                ]
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
                "heading": "Alias, riwayat perintah, dan prompt PS1",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak panduan pemasangan alat developer ditutup dengan kalimat",
                    "\"tambahkan folder ini ke PATH\". pip install --user, misalnya, menaruh",
                    "program di ~/.local/bin. Selama folder itu belum ada di PATH, bash",
                    "menjawab 'command not found' walaupun programnya ada.",
                    "",
                    "Kasus kecil: kamu menyimpan script buatanmu di folder ~/skrip, salah",
                    "satunya ~/skrip/rekap yang udah diberi chmod +x. Dari folder mana pun,",
                    "kamu mau cukup mengetik rekap, tanpa menulis jalur lengkapnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan dulu masalahnya memang PATH. command -v rekap nggak",
                    "     mencetak apa pun, dan echo \"$PATH\" | tr ':' '\\n' menunjukkan",
                    "     ~/skrip nggak ada di daftar. Di Fedora, ~/.bashrc bawaan udah",
                    "     memasukkan ~/.local/bin dan ~/bin, jadi dua folder itu biasanya",
                    "     nggak perlu ditambah lagi.",
                    "  2. Tambahkan satu baris export di akhir ~/.bashrc, dengan $PATH lama",
                    "     tetap disebut, lalu muat ulang:",
                    "      echo 'export PATH=\"$HOME/skrip:$PATH\"' >> ~/.bashrc",
                    "      source ~/.bashrc",
                    "      command -v rekap",
                    "  3. Petik tunggal di baris echo itu wajib. Dengan petik ganda, $PATH",
                    "     langsung diganti isinya yang sekarang, dan ~/.bashrc menyimpan",
                    "     daftar folder yang membeku.",
                    "  4. Buka tab terminal baru dan ketik rekap. Kalau di tab baru pun",
                    "     ketemu, setelannya udah permanen.",
                    "",
                    "Jebakan: pakai >>, jangan >. Satu tanda > menimpa seluruh isi ~/.bashrc",
                    "dengan baris itu, termasuk alias dan setelan yang udah ada.",
                ]
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Persentase kehadiran di rekap absensi dan total belanja di kasir",
                    "dihitung dengan bilangan bulat. Bash cocok untuk itu selama kamu ingat",
                    "dia selalu membuang pecahan. Rupiah aman karena memang bulat. Yang",
                    "perlu hati-hati adalah persentase.",
                    "",
                    "Kasus kecil: seorang siswa hadir 18 dari 22 hari sekolah. Wali kelas",
                    "minta persen kehadirannya untuk rapor.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua bilangan bulat, keluarannya persen. Rumusnya hadir",
                    "     dibagi hari, lalu dikali 100.",
                    "  2. Tulis apa adanya dulu, lalu bandingkan dengan urutan sebaliknya:",
                    "      hadir=18; hari=22",
                    "      echo $(( hadir / hari * 100 ))",
                    "      echo $(( hadir * 100 / hari ))",
                    "      echo \"scale=1; $hadir * 100 / $hari\" | bc",
                    "  3. Baris kedua mencetak 0. 18 / 22 dibulatkan ke bawah jadi 0",
                    "     duluan, lalu 0 dikali 100 tetap 0. Baris ketiga mengalikan dulu,",
                    "     jadi hasilnya 81.",
                    "  4. Kalau rapor butuh satu angka di belakang koma, pakai bc seperti",
                    "     baris keempat. Hasilnya 81.8.",
                    "",
                    "Jebakan: kalau hari bernilai 0, misalnya data bulan libur, bash",
                    "berhenti dengan pesan division by 0. Periksa angkanya sebelum dibagi.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online menghitung ongkos kirim dari kota tujuan dan berat paket.",
                    "Di belakang layar itu cuma rangkaian keputusan: kota ini masuk zona",
                    "mana, dan beratnya lewat batas atau nggak. case cocok untuk memilih",
                    "zona, dan (( )) cocok untuk syarat angka.",
                    "",
                    "Kasus kecil: tokomu memakai tarif sendiri. Jakarta dan Depok Rp9.000,",
                    "Bandung Rp12.000, kota lain Rp20.000. Tiap kilogram sesudah kilogram",
                    "pertama kena tambahan Rp5.000. Berapa ongkir paket 3 kg ke Bandung?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya nama kota dan berat dalam kilogram bulat. Keluarannya",
                    "     satu angka ongkir.",
                    "  2. Pecah jadi dua keputusan: tarif dasar per kota, lalu tambahan",
                    "     berat. Yang pertama memilih dari banyak pilihan, jadi pakai case",
                    "     dengan cabang * untuk kota lain:",
                    "      case \"$kota\" in",
                    "          [Jj]akarta|[Dd]epok) ongkir=9000 ;;",
                    "          [Bb]andung)          ongkir=12000 ;;",
                    "          *)                   ongkir=20000 ;;",
                    "      esac",
                    "      (( berat > 1 )) && ongkir=$(( ongkir + (berat - 1) * 5000 ))",
                    "  3. Hitung dengan tangan dulu: 12000 + 2 x 5000 = 22000. Script-nya",
                    "     harus memberi angka yang sama untuk kota=Bandung dan berat=3.",
                    "  4. Periksa kasus pinggir. Paket 1 kg nggak kena tambahan, karena",
                    "     syaratnya > 1. Pola [Jj] menerima Jakarta dan jakarta, tapi nama",
                    "     yang diketik kapital semua tetap jatuh ke tarif kota lain.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Operator sekolah sering menerima daftar siswa dari tata usaha berupa",
                    "berkas teks, satu nama per baris. Membuat folder tugas atau akun untuk",
                    "tiap nama adalah pekerjaan perulangan, dan while read menjaga nama",
                    "yang berspasi tetap utuh.",
                    "",
                    "Kasus kecil: siswa.txt berisi nama seperti Andi Pratama dan Siti",
                    "Aminah, dengan satu baris kosong di tengahnya. Kamu perlu satu folder",
                    "di dalam tugas/ untuk tiap siswa.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya berkas satu nama per baris, keluarannya satu folder",
                    "     per nama. Satuan kerjanya baris, bukan kata.",
                    "  2. Pakai pola baca berkas yang benar, dan lewati baris kosong dengan",
                    "     continue:",
                    "      while IFS= read -r nama; do",
                    "          [[ -z \"$nama\" ]] && continue",
                    "          mkdir -p \"tugas/$nama\"",
                    "      done < siswa.txt",
                    "  3. Jangan pakai for nama in $(cat siswa.txt). Bentuk itu memecah di",
                    "     spasi, jadi kamu dapat folder terpisah Andi, Pratama, Siti, dan",
                    "     Aminah.",
                    "  4. Periksa baris terakhir berkasnya. Kalau baris itu nggak diakhiri",
                    "     baris baru, read gagal di sana walaupun isinya udah terbaca, dan",
                    "     siswa terakhir nggak dapat folder. Tulis",
                    "     while IFS= read -r nama || [[ -n \"$nama\" ]]; do supaya baris itu",
                    "     tetap ikut.",
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
                "heading": "Associative array, memecah string, dan mapfile",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hitung cepat suara pemilihan ketua kelas, rekap pesanan per menu di",
                    "kantin, dan jumlah kunjungan per halaman di log server sama-sama",
                    "menghitung berapa kali tiap nama muncul. Associative array cocok untuk",
                    "itu, karena kuncinya boleh berupa teks.",
                    "",
                    "Kasus kecil: hasil pemilihan ketua kelas tercatat sebagai deretan nama",
                    "andi budi andi citra andi budi. Kamu perlu jumlah suara tiap calon,",
                    "urut abjad.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya daftar nama, keluarannya pasangan nama dan angka. Itu",
                    "     bentuk map: kuncinya nama calon, nilainya jumlah suara.",
                    "  2. Siapkan map dengan declare -A, naikkan nilainya tiap kali nama",
                    "     muncul, lalu urutkan kuncinya lewat tr dan sort:",
                    "      declare -A suara",
                    "      for c in andi budi andi citra andi budi; do (( suara[$c]++ )); done",
                    "      for k in $(echo \"${!suara[@]}\" | tr ' ' '\\n' | sort); do",
                    "          echo \"$k: ${suara[$k]} suara\"",
                    "      done",
                    "  3. Hasilnya tiga baris: andi: 3 suara, budi: 2 suara, dan citra: 1",
                    "     suara. Tanpa sort, urutan kunci map nggak terjamin.",
                    "  4. Coba hapus baris declare -A. bash menganggap suara array biasa,",
                    "     nama calon dihitung sebagai angka, dan karena variabel bernama",
                    "     andi nggak ada, semuanya jadi indeks 0. Hasilnya satu angka 6,",
                    "     tanpa pesan error.",
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
                "heading": "Nilai kembalian fungsi dan kata kunci local",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program kasir minimarket mengulang perhitungan yang sama ratusan kali",
                    "sehari: total per barang, cek uang pembeli cukup atau nggak, lalu",
                    "kembalian. Di script, perhitungan seperti itu dibungkus jadi fungsi",
                    "supaya ditulis sekali dan dipanggil berkali-kali.",
                    "",
                    "Kasus kecil: pembeli mengambil 3 bungkus kopi seharga Rp12.500 dan",
                    "membayar Rp50.000. Kasir perlu tahu uangnya cukup atau nggak, dan",
                    "berapa kembaliannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua jenis jawaban. Total adalah data berupa angka,",
                    "     sedangkan cukup atau nggak adalah status benar atau salah.",
                    "  2. Data dikirim lewat echo dan ditangkap dengan $( ). Status fungsi",
                    "     sama dengan status perintah terakhirnya, di sini (( )), jadi",
                    "     fungsinya bisa langsung dipakai di if:",
                    "      total() { echo $(( $1 * $2 )); }",
                    "      cukup() { (( $1 >= $2 )); }",
                    "      t=$(total 12500 3)",
                    "      if cukup 50000 \"$t\"; then echo \"kembalian $(( 50000 - t ))\"; fi",
                    "  3. Hasilnya kembalian 12500. Coba juga bayar 30000. cukup memberi",
                    "     status 1, dan baris kembalian nggak dicetak.",
                    "  4. Uji godaan yang paling sering: mengirim total lewat return.",
                    "     return $(( $1 * $2 )) untuk 37500 menghasilkan $? bernilai 124,",
                    "     karena return cuma bisa membawa 0 sampai 255, dan bash mengambil",
                    "     sisa bagi 256-nya.",
                ]
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Script di kantor jarang dipakai sendirian. Script lain, jadwal",
                    "otomatis, atau sistem CI memanggilnya dengan argumen, lalu membaca exit",
                    "code-nya untuk memutuskan langkah berikutnya. 0 berarti lanjut, angka",
                    "lain berarti berhenti dan kabari orang.",
                    "",
                    "Kasus kecil: staf tata usaha memakai kirim-laporan.sh dengan satu",
                    "argumen, yaitu nama berkas rekap. Kadang argumennya lupa diketik,",
                    "kadang nama berkasnya salah, dan script pemanggilnya perlu tahu bedanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar dulu kemungkinan gagalnya: argumen kurang, atau berkasnya",
                    "     nggak ada. Kasih tiap kegagalan angka sendiri, misalnya 1 dan 2.",
                    "  2. Periksa di awal script, kirim pesannya ke stderr, lalu exit:",
                    "      [[ $# -eq 1 ]] || { echo \"Cara pakai: $0 <berkas>\" >&2; exit 1; }",
                    "      [[ -f \"$1\" ]] || { echo \"Berkas '$1' tidak ada\" >&2; exit 2; }",
                    "      echo \"Mengirim $1\"",
                    "  3. Uji ketiga jalurnya dan cek $? tepat sesudah tiap percobaan. Tanpa",
                    "     argumen hasilnya 1, berkas salah hasilnya 2, dan",
                    "     ./kirim-laporan.sh \"rekap Mei.csv\" && echo beres mencetak beres.",
                    "  4. Periksa nama berspasi. Tanpa petik, rekap Mei.csv sampai sebagai",
                    "     dua argumen, dan script menolak dengan exit 1 padahal berkasnya",
                    "     ada.",
                    "",
                    "Jebakan: $? cuma menyimpan hasil perintah terakhir. Satu echo di",
                    "antaranya udah cukup untuk mengubahnya jadi 0.",
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
                "heading": "Script utuh dengan -h, -v, dan -o berkas",
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
                "heading": "Membaca baris getopts dan dua jebakannya",
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
                "heading": "Opsi panjang, penanda dua strip, dan bantuan",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Alat internal di tim IT hampir selalu punya opsi, misalnya -n untuk",
                    "uji coba tanpa mengubah apa pun, atau -o untuk nama berkas hasil.",
                    "Begitu script rekap penjualan mulai dipakai orang lain, permintaan",
                    "opsi baru datang, dan getopts yang menjaga cara pakai lamanya tetap",
                    "jalan.",
                    "",
                    "Kasus kecil: rekap.sh menerima satu atau beberapa berkas penjualan.",
                    "Pemilik UMKM minta bisa memilih bulan, misalnya rekap.sh -b 05",
                    "penjualan.csv, tanpa merusak cara pakai lama rekap.sh penjualan.csv.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bedakan yang wajib dan yang pilihan. Berkas tetap posisional,",
                    "     bulan jadi opsi -b yang membawa nilai, dengan nilai bawaan",
                    "     bulan=\"semua\" sebelum perulangan.",
                    "  2. Uraikan dengan getopts dalam mode senyap. Cabang * menangkap opsi",
                    "     yang nggak dikenal maupun -b yang nilainya lupa ditulis:",
                    "      while getopts \":b:\" opt; do",
                    "          case \"$opt\" in",
                    "              b) bulan=\"$OPTARG\" ;;",
                    "              *) echo \"opsi salah: -$OPTARG\" >&2; exit 2 ;;",
                    "          esac",
                    "      done",
                    "  3. Buang opsi yang udah terbaca dengan shift $((OPTIND - 1)). Sesudah",
                    "     itu \"$@\" cuma berisi nama berkas.",
                    "  4. Uji cara pakai lama dan baru: rekap.sh penjualan.csv tetap memberi",
                    "     bulan=semua, sedangkan -b 05 dan -b05 memberi bulan=05. Lalu coba",
                    "     rekap.sh penjualan.csv -b 05. getopts berhenti di argumen pertama",
                    "     yang bukan opsi, jadi -b dan 05 ikut terbaca sebagai nama berkas.",
                ]
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
                "heading": "Kosakata regex dan jebakan titik",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Formulir pendaftaran, aplikasi kasir dengan member, dan sistem absensi",
                    "memeriksa bentuk isian sebelum menyimpannya, misalnya nomor HP atau",
                    "kode pos. Di script bash, pemeriksaan itu ditulis dengan [[ =~ ]] dan",
                    "regex, jadi data yang salah ketik ditolak sejak awal.",
                    "",
                    "Kasus kecil: data member tokomu berisi nomor HP. Aturan tokomu: diawali",
                    "08, lalu 8 sampai 11 angka lagi, tanpa tanda hubung atau spasi. Kamu",
                    "mau memisahkan nomor yang sah dari yang perlu dicek ulang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Terjemahkan aturannya jadi potongan pola: awal teks ^, lalu 08,",
                    "     lalu [0-9]{8,11}, lalu akhir teks $.",
                    "  2. Simpan polanya di variabel, lalu pakai tanpa petik di sebelah",
                    "     kanan =~:",
                    "      pola='^08[0-9]{8,11}$'",
                    "      for hp in 081234567890 0812-3456-789 6281234567890; do",
                    "          if [[ $hp =~ $pola ]]; then echo \"$hp sah\"",
                    "          else echo \"$hp ditolak\"; fi",
                    "      done",
                    "  3. Hasilnya cuma nomor pertama yang sah. Yang kedua ditolak karena",
                    "     tanda hubung, yang ketiga karena diawali 62.",
                    "  4. Periksa batasnya: 0812345 (7 angka) dan nomor 14 angka sama-sama",
                    "     ditolak. Tanpa ^ dan $, nomor 14 angka malah lolos, karena di",
                    "     dalamnya ada potongan yang cocok.",
                    "",
                    "Jebakan: kalau ditulis =~ \"$pola\" dengan petik, polanya jadi teks",
                    "biasa, dan nomor yang sah pun ditolak.",
                ]
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak ponsel menamai fotonya seperti IMG_20240517_081230.JPG. Orang",
                    "yang merapikan dokumentasi kegiatan sekolah atau foto produk toko",
                    "online sering mengganti nama itu jadi bentuk yang lebih enak dibaca.",
                    "Operasi ${...} memotong nama seperti itu tanpa memanggil program lain.",
                    "",
                    "Kasus kecil: kamu mau nama IMG_20240517_081230.JPG jadi",
                    "2024-05-17_081230.jpg, supaya tanggalnya langsung terbaca dan",
                    "ekstensinya huruf kecil.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat bentuknya: awalan IMG_, delapan angka tanggal, garis bawah,",
                    "     jam, lalu titik dan ekstensi. Tiap bagian punya alat sendiri.",
                    "  2. Buang awalan dengan #, buang ekstensi dengan %, ambil ekstensi",
                    "     dengan ##, lalu rakit ulang pakai substring:",
                    "      nama=\"IMG_20240517_081230.JPG\"",
                    "      inti=\"${nama#IMG_}\"; inti=\"${inti%.*}\"",
                    "      ext=\"${nama##*.}\"",
                    "      baru=\"${inti:0:4}-${inti:4:2}-${inti:6:2}_${inti#*_}.${ext,,}\"",
                    "      echo \"$nama -> $baru\"",
                    "  3. Hasilnya IMG_20240517_081230.JPG -> 2024-05-17_081230.jpg. Cukup",
                    "     cetak dulu seperti ini tanpa mengganti nama apa pun, supaya kamu",
                    "     bisa memeriksa hasilnya.",
                    "  4. Coba nama yang nggak mengikuti pola, misalnya Screenshot_1.png.",
                    "     Hasilnya Scre-en-sh_1.png, nama ngawur tanpa pesan error. Lewati",
                    "     nama seperti itu dengan [[ \"$nama\" == IMG_* ]] sebelum diolah.",
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
                "heading": "Nullglob, berkas sementara, dan wc -l",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Folder Unduhan di laptop kantor cepat penuh dengan PDF surat, foto, dan",
                    "berkas pemasang program. Memindahkan berkas per jenis ke folder",
                    "tujuannya adalah pekerjaan glob, mv, dan mkdir -p.",
                    "",
                    "Kasus kecil: semua berkas .pdf di ~/Unduhan mau dipindah ke",
                    "~/Dokumen/pdf, termasuk \"surat tugas.pdf\" yang namanya berspasi. Di",
                    "akhir, kamu mau tahu berapa berkas yang dipindah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Siapkan tujuannya dulu dengan mkdir -p ~/Dokumen/pdf. Kalau",
                    "     foldernya udah ada, mkdir -p diam aja.",
                    "  2. Ulangi tiap berkas yang cocok dengan glob, lalu hitung yang",
                    "     berhasil dipindah:",
                    "      n=0",
                    "      for f in ~/Unduhan/*.pdf; do",
                    "          [[ -e \"$f\" ]] || continue",
                    "          mv \"$f\" ~/Dokumen/pdf/ && n=$((n + 1))",
                    "      done",
                    "      echo \"$n berkas dipindah\"",
                    "  3. Petik di \"$f\" menjaga surat tugas.pdf tetap satu nama. Tanpa",
                    "     petik, mv menerima .../surat dan tugas.pdf sebagai dua berkas yang",
                    "     nggak ada, dan berkas itu tertinggal di Unduhan.",
                    "  4. Jalankan dua kali. Di percobaan kedua nggak ada PDF lagi, pola",
                    "     ~/Unduhan/*.pdf dikirim mentah, dan [[ -e ]] melewatinya. Hasilnya",
                    "     0 berkas dipindah, tanpa error.",
                    "",
                    "Jebakan: kalau di ~/Dokumen/pdf udah ada berkas dengan nama yang sama,",
                    "mv menimpanya tanpa bertanya.",
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
                "heading": "Menjalankan aksi lewat -exec dan xargs",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Server toko online menulis berkas log baru tiap hari. Kalau dibiarkan,",
                    "log lama memenuhi disk sampai aplikasi gagal menyimpan data. Admin",
                    "server membersihkannya secara rutin dengan find dan -mtime.",
                    "",
                    "Kasus kecil: folder log/ punya subfolder api/ dan web/, berisi berkas",
                    ".log dari berbagai tanggal, salah satunya \"galat lama.log\". Aturan",
                    "kantormu: log yang lebih tua dari 30 hari boleh dihapus.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Susun saringannya dulu: berkas biasa, nama berakhiran .log, dan",
                    "     terakhir diubah lebih dari 30 hari lalu.",
                    "  2. Jalankan tanpa aksi, baca daftarnya, lalu hitung jumlahnya:",
                    "      find log/ -type f -name '*.log' -mtime +30 | sort",
                    "      find log/ -type f -name '*.log' -mtime +30 | wc -l",
                    "  3. Kalau daftarnya memang benar, baru taruh -delete di paling",
                    "     belakang. -delete aman untuk nama berspasi seperti galat lama.log,",
                    "     karena nama itu nggak lewat pemecahan kata oleh shell:",
                    "      find log/ -type f -name '*.log' -mtime +30 -delete",
                    "  4. Periksa batasnya. Berkas yang umurnya 30 hari lebih satu jam",
                    "     belum ikut, karena find membuang pecahan hari. -mtime +30 baru",
                    "     kena berkas yang berumur paling sedikit 31 hari.",
                    "",
                    "Jebakan: tanpa petik di '*.log', shell mengurai polanya duluan. Kalau",
                    "di folder kerjamu kebetulan ada satu berkas .log, find cuma mencari",
                    "nama itu, dan log lain lolos dari pembersihan.",
                ]
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
                "heading": "Heredoc, here-string, dan variabel bawaan awk",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Warung kopi dan UMKM lain biasanya punya catatan penjualan berbentuk",
                    "CSV dari aplikasi kasir atau spreadsheet. Pertanyaan pemilik seperti",
                    "\"berapa omzet kopi bulan ini?\" bisa dijawab satu baris awk, tanpa",
                    "membuka spreadsheet.",
                    "",
                    "Kasus kecil: penjualan.csv punya kolom tanggal, barang, jumlah, dan",
                    "harga, dengan baris judul di paling atas. Ada barang kopi, ada juga",
                    "kopi susu. Pemilik minta omzet kopi saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya baris-baris CSV, keluarannya satu angka. Omzet tiap",
                    "     baris adalah jumlah dikali harga, lalu semua baris kopi",
                    "     dijumlahkan.",
                    "  2. Coba hitung kasar dulu dengan grep -c kopi penjualan.csv. Kalau",
                    "     ada dua transaksi kopi dan satu kopi susu, hasilnya 3, karena",
                    "     kopi susu ikut terhitung.",
                    "  3. Pakai awk, yang membandingkan seluruh isi kolom kedua:",
                    "      awk -F',' '$2 == \"kopi\" {s += $3 * $4} END {print s}' penjualan.csv",
                    "     Untuk dua baris kopi, 3 gelas dan 1 gelas seharga 5000, hasilnya",
                    "     20000.",
                    "  4. Baris judul aman, karena kolom keduanya berisi kata barang. Kalau",
                    "     sama sekali nggak ada baris kopi, awk mencetak baris kosong. Tulis",
                    "     print s + 0 supaya keluarnya 0.",
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
                    "Sinyal adalah pesan pendek dari kernel ke sebuah proses.",
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
                    "Selalu jalankan pgrep dulu dan baca daftarnya, baru pkill. Dengan -f,",
                    "yang dicocokkan adalah seluruh baris perintah, termasuk argumennya,",
                    "jadi pola yang terlalu longgar bisa ikut membunuh editor atau terminal",
                    "yang kebetulan memuat kata itu di judulnya.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Minimarket yang punya beberapa cabang biasanya menarik rekap tiap",
                    "cabang di malam hari. Kalau tiap rekap makan beberapa menit dan",
                    "dikerjakan satu per satu, waktunya bertambah tiap ada cabang baru.",
                    "Menjalankannya bersamaan dengan & lalu menunggu tiap PID memotong",
                    "waktu itu, asal kegagalan satu cabang tetap ketahuan.",
                    "",
                    "Kasus kecil: rekap-cabang.sh mengolah satu cabang per panggilan. Ada",
                    "tiga cabang, yaitu bogor, depok, dan bekasi. Kamu mau ketiganya jalan",
                    "sekaligus, masing-masing dengan log sendiri, dan script induk keluar",
                    "dengan kode 1 kalau ada satu saja yang gagal.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah pekerjaannya: lepas tiga proses, simpan PID tiap proses,",
                    "     lalu tunggu satu per satu sambil mencatat yang gagal.",
                    "  2. Arahkan keluaran tiap cabang ke berkasnya sendiri, supaya tiga",
                    "     keluaran nggak bercampur di layar:",
                    "      for c in bogor depok bekasi; do",
                    "          ./rekap-cabang.sh \"$c\" > \"rekap-$c.log\" 2>&1 &",
                    "          pids+=(\"$!\")",
                    "      done",
                    "      gagal=0",
                    "      for p in \"${pids[@]}\"; do wait \"$p\" || gagal=1; done",
                    "  3. Tutup dengan exit \"$gagal\". $! disimpan tepat sesudah tiap &,",
                    "     karena & berikutnya langsung menimpanya.",
                    "  4. Uji dengan satu cabang yang sengaja gagal, misalnya depok keluar",
                    "     dengan kode 3. wait polos tanpa PID tetap memberi 0, jadi",
                    "     kegagalan itu cuma ketahuan lewat wait per PID seperti di atas.",
                ]
            },
        ],
    },
    {
        "title": "21. Alat Pendamping: curl, jq, date, tar",
        "sections": [
            {
                "body": [
                    "Script bash yang isinya murni bash hampir nggak ada. Kosakata bash",
                    "sendiri kecil: variabel, if, for, fungsi, dan pipe. Pekerjaan utamanya",
                    "dikerjakan program lain yang dipanggil oleh script, misalnya",
                    "mengunduh, membaca JSON, menghitung tanggal, dan mengemas berkas.",
                    "",
                    "Jadi bash itu perekat. Membaca script orang lain berarti mengenali",
                    "alat-alat yang direkatkannya. grep, sed, dan awk sudah kamu kenal dari",
                    "materi sebelumnya. Empat alat di materi ini muncul sama seringnya di",
                    "kode nyata. Kalau kamu belum kenal, script yang sederhana pun bakal",
                    "kelihatan seperti sandi.",
                    "",
                    "curl: mengambil dan mengirim data lewat jaringan",
                    "",
                    "Nama curl berasal dari \"client URL\". Secara bawaan, isi jawaban dari",
                    "server dicetak ke stdout. Jadi hasilnya bisa langsung dialirkan lewat",
                    "pipe, atau ditangkap dengan $(...).",
                    "",
                    "  curl https://contoh.id/data.json",
                    "",
                    "Rangkaian yang paling sering kamu lihat adalah -fsSL. Itu empat opsi",
                    "yang digabung, dan tiap hurufnya menutup satu masalah yang berbeda:",
                    "  - -f (--fail) membuat curl gagal kalau status HTTP-nya 4xx atau 5xx.",
                    "    Tanpa -f, curl menganggap halaman '404 Not Found' sebagai sukses.",
                    "    Exit code-nya tetap 0, dan isi halaman error itu ikut tersimpan.",
                    "  - -s (--silent) mematikan bilah progres.",
                    "  - -S (--show-error) tetap menampilkan pesan error. -s sendirian",
                    "    membuat curl diam total, termasuk waktu gagal. Makanya -s dan -S",
                    "    selalu dipasangkan.",
                    "  - -L (--location) mengikuti pengalihan 301 atau 302. Tanpa -L, yang",
                    "    tersimpan adalah halaman 'Moved Permanently' yang isinya nyaris",
                    "    kosong.",
                    "",
                    "Opsi lain yang wajib kamu kenali:",
                    "  - -o nama.json menyimpan hasilnya ke berkas bernama itu. Ingat o",
                    "    kecil: kamu yang menamai.",
                    "  - -O menyimpan hasilnya pakai nama dari URL-nya. Ingat O besar: curl",
                    "    yang menamai.",
                    "  - -H \"Judul: nilai\" menambah header permintaan. Contohnya:",
                    "      -H \"Authorization: Bearer $TOKEN\"",
                    "  - -d '{\"a\":1}' mengirim isi permintaan (request body). Begitu ada -d,",
                    "    metodenya otomatis jadi POST.",
                    "  - -X PUT menetapkan metode sendiri. Untuk POST, -X nggak perlu ditulis",
                    "    kalau sudah ada -d.",
                    "  - --max-time 30 membatasi total waktunya. Tanpa batas ini, script bisa",
                    "    menggantung selamanya.",
                    "  - --retry 3 mengulang kalau gagal karena masalah jaringan sementara.",
                    "  - -w '%{http_code}' cuma mencetak kode status, biasanya bersama",
                    "    -o /dev/null.",
                    "",
                    "Exit code curl yang sering ketemu:",
                    "  - 0: sukses.",
                    "  - 6: nama host nggak ketemu.",
                    "  - 7: nggak bisa menyambung ke server.",
                    "  - 28: kehabisan waktu.",
                    "  - 22: -f dipakai, dan servernya menjawab 4xx atau 5xx.",
                    "",
                    "wget mengerjakan hal yang mirip, dengan opsi yang beda. wget -qO- URL",
                    "setara dengan curl -s URL (hasilnya ke stdout). wget -q URL menyimpan",
                    "hasilnya ke berkas, seperti curl -O.",
                    "",
                    "Kenapa curl -fsSL URL | bash ada di mana-mana?",
                    "",
                    "Halaman pemasangan program suka memberi satu baris seperti itu, karena",
                    "baris itu jalan di distro apa pun tanpa package manager, yaitu program",
                    "pemasang paket seperti dnf atau apt.",
                    "",
                    "Hati-hati: baris itu menjalankan kode orang lain dengan hak aksesmu,",
                    "tanpa kamu pernah melihat isinya.",
                    "",
                    "Ada dua bahaya tambahan yang nggak kelihatan:",
                    "  - Server bisa mengirim isi yang berbeda ke curl dan ke browser. Yang",
                    "    kamu baca di browser belum tentu sama dengan yang dijalankan.",
                    "  - Kalau koneksi putus di tengah jalan, bash sudah telanjur menjalankan",
                    "    separuh script.",
                    "",
                    "Bentuk yang lebih aman cuma butuh satu langkah tambahan:",
                    "",
                    "  curl -fsSL https://contoh.id/pasang.sh -o pasang.sh",
                    "  less pasang.sh        # baca dulu",
                    "  bash pasang.sh",
                ],
            },
            {
                "heading": "jq: satu-satunya cara waras menangani JSON",
                "body": [
                    "Hampir semua API sekarang menjawab dengan JSON. API adalah pintu yang",
                    "disediakan sebuah layanan supaya program lain bisa meminta data. Bash",
                    "nggak punya tipe data untuk JSON. Buat bash, JSON cuma seuntai teks",
                    "panjang.",
                    "",
                    "Godaannya adalah memotong JSON pakai grep atau sed. Cara itu selalu",
                    "rapuh, dan ini bukan soal selera:",
                    "  - JSON nggak peduli baris baru. Server yang sama bisa mengirim JSON",
                    "    yang rapi hari ini, lalu satu baris panjang besok. Semua pola yang",
                    "    mengandalkan \"satu objek satu baris\" langsung rusak.",
                    "  - Urutan kunci nggak dijamin.",
                    "  - Nilai boleh memuat tanda kutip yang di-escape, kurung, bahkan",
                    "    potongan JSON lain.",
                    "  - Spasi di sekitar titik dua bebas.",
                    "",
                    "Aturan praktis: begitu kamu menulis regex kedua untuk JSON yang sama,",
                    "berhenti, lalu pasang jq.",
                    "",
                    "jq bukan bawaan sistem. Cara memasangnya: sudo dnf install jq",
                    "(Fedora), sudo apt install jq (Debian/Ubuntu), atau brew install jq",
                    "(macOS). Makanya script yang memakai jq sebaiknya mengecek dulu dengan",
                    "command -v, seperti di contoh di bawah. Dengan begitu pesannya jelas,",
                    "dan nggak berupa 'jq: command not found' di tengah proses.",
                    "",
                    "jq bekerja dengan filter, yaitu ekspresi pendek yang memberi tahu jq",
                    "bagian mana yang mau diambil. Filter berikut sudah mencukupi sebagian",
                    "besar kebutuhan:",
                    "",
                    "  .                 seluruh isi, sekaligus dirapikan dan diberi warna",
                    "  .kunci            ambil satu nilai",
                    "  .a.b.c            masuk ke dalam objek bersarang",
                    "  .daftar[]         buka array jadi banyak nilai, satu per baris",
                    "  .daftar[0]        elemen pertama",
                    "  .daftar[].nama    ambil satu kunci dari tiap elemen",
                    "  select(syarat)    teruskan yang memenuhi syarat saja",
                    "  length, add       jumlah elemen, dan jumlahkan angka di sebuah array",
                    "  sort_by(.gaji)    urutkan; beri tanda minus (-.gaji) untuk urutan menurun",
                    "  // \"cadangan\"     nilai pengganti kalau yang kiri null",
                    "",
                    "Tiga hal ini paling sering bikin bingung:",
                    "  1. Tanda | di dalam petik tunggal itu milik jq, bukan pipe shell.",
                    "     Bentuknya sama persis, tapi yang di dalam '...' dikerjakan jq",
                    "     sendiri, sedangkan yang di luar dikerjakan bash.",
                    "  2. Tanpa -r, string keluar lengkap dengan tanda kutipnya. Ini",
                    "     penyebab nomor satu variabel bash yang isinya \"Andi\" berikut tanda",
                    "     kutipnya. Akibatnya perbandingan == gagal terus, padahal di layar",
                    "     kelihatan sama. -r artinya raw: keluarkan teksnya saja.",
                    "  3. Kunci yang nggak ada menghasilkan null, dan nggak menghasilkan",
                    "     error. Dengan -r, null tercetak sebagai kata 'null', lalu masuk ke",
                    "     variabelmu tanpa ketahuan. Tutup kemungkinan itu dengan",
                    "     // \"nilai cadangan\".",
                    "",
                    "Untuk menyisipkan nilai dari shell ke dalam filter, pakai --arg nama",
                    "nilai, lalu rujuk nilainya sebagai $nama di dalam filter. Jangan",
                    "menempelkan \"$var\" langsung ke tengah filter. Itu lubang injeksi yang",
                    "bentuknya sama dengan SQL injection: isi variabelnya ikut dibaca",
                    "sebagai bagian dari perintah.",
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
                    "date tanpa argumen mencetak waktu sekarang dalam bentuk panjang untuk",
                    "dibaca manusia. Yang bikin bingung waktu membaca script adalah argumen",
                    "yang diawali +, seperti $(date +%Y) yang sempat muncul di materi",
                    "Variabel & Quoting.",
                    "",
                    "Argumen yang diawali + bukan opsi. Argumen itu adalah string format,",
                    "yaitu pola yang menentukan bentuk tanggal yang dicetak.",
                    "",
                    "Makanya bentuknya date +%Y, dan bukan date --year. Semua yang bukan",
                    "kode berawalan % di dalam string itu dicetak apa adanya. Jadi tanda",
                    "hubung di +%Y-%m-%d cuma teks biasa. Kalau formatnya memuat spasi,",
                    "bungkus dengan petik: date +'%F %T'.",
                    "",
                    "  %Y  tahun 4 digit      2024        %F  sama dengan %Y-%m-%d",
                    "  %m  bulan 2 digit      03          %T  sama dengan %H:%M:%S",
                    "  %d  tanggal 2 digit    15          %s  detik sejak 1 Januari 1970 (epoch)",
                    "  %H  jam 24 jam         08          %z  selisih zona waktu, mis. +0700",
                    "  %M  menit              30          %A  nama hari, mengikuti bahasa sistem",
                    "  %S  detik              45          %-d tanpa nol di depan: 5, bukan 05",
                    "",
                    "Epoch adalah titik nol hitungan waktu di komputer, yaitu 1 Januari 1970",
                    "pukul 00.00 UTC.",
                    "",
                    "date -u memakai UTC, dan nggak memakai zona waktu mesin. Ini bukan",
                    "detail sepele. Dua server di zona berbeda yang menulis ke log yang sama",
                    "bakal menghasilkan urutan waktu yang mustahil dibaca. Untuk log dan",
                    "nama arsip, pakai -u, atau simpan epoch (%s) yang memang nggak punya",
                    "zona.",
                    "",
                    "date -d \"teks\" menghitung waktu lain, bukan waktu sekarang. Dia paham",
                    "bahasa sehari-hari (dalam bahasa Inggris):",
                    "",
                    "  date -d 'yesterday' +%F        date -d '2 hours ago' +%T",
                    "  date -d '2024-03-15' +%A       date -d @1710491445 +%F     (@ berarti epoch)",
                    "",
                    "Ada dua jebakan date yang sering kena:",
                    "  1. -d (termasuk bentuk -u -d) cuma ada di date milik GNU coreutils,",
                    "     yaitu date di Linux. Di macOS dan BSD perintahnya lain sama",
                    "     sekali: date -v-1d +%F untuk kemarin, dan date -r 1710491445 untuk",
                    "     epoch. Script tanggal yang mulus di Linux bisa langsung gagal di",
                    "     laptop temanmu.",
                    "  2. Kalau teks waktunya sudah memuat jam, tanda + atau - sesudahnya",
                    "     dibaca sebagai zona waktu, bukan pergeseran hari. Hasilnya salah",
                    "     tanpa peringatan apa pun:",
                    "       date -u -d \"2024-03-15 08:30:45 + 7 days\"",
                    "         -> 2024-03-16 01:30:45   SALAH",
                    "       date -u -d \"2024-03-15 08:30:45 UTC + 7 days\"",
                    "         -> 2024-03-22 08:30:45   BENAR",
                    "     Di baris pertama, '+7' ditelan sebagai zona +0700, lalu sisa kata",
                    "     'days' dihitung sebagai 1 hari. Sebutkan zonanya, atau tulis tanpa",
                    "     tanda: '7 days' dan '1 day ago' aman.",
                    "",
                    "Untuk cap waktu di nama berkas, urutan dari besar ke kecil (%Y%m%d)",
                    "ada alasannya. Dengan urutan itu, urutan abjad sama dengan urutan",
                    "waktu, jadi ls dan sort langsung memberi hasil yang benar. Pakai juga",
                    "%H%M%S, jangan %T. %T menghasilkan titik dua, yang bermasalah di",
                    "Windows dan bikin repot waktu berkasnya disalin lewat scp.",
                ],
                "code": "#!/usr/bin/env bash\nset -euo pipefail\n\n# Tanggalnya sengaja DIPATOK supaya hasil contoh ini sama tiap kali dijalankan.\n# Di script sungguhan kamu membuang bagian -u -d \"$ACUAN\" dan memakai waktu\n# sekarang: date +%F, date +%s, dan seterusnya.\nACUAN=\"2024-03-15 08:30:45 UTC\"\n\np() { printf \"%-24s %s\\n\" \"$1\" \"$2\"; }\n\np \"tanpa format sama sekali\" \"$(date -u -d \"$ACUAN\")\"\np \"+%Y-%m-%d\"               \"$(date -u -d \"$ACUAN\" +%Y-%m-%d)\"\np \"+%F  (pintasan sama)\"    \"$(date -u -d \"$ACUAN\" +%F)\"\np \"+%H:%M:%S\"               \"$(date -u -d \"$ACUAN\" +%H:%M:%S)\"\np \"+%T  (pintasan sama)\"    \"$(date -u -d \"$ACUAN\" +%T)\"\np \"+%Y%m%d-%H%M%S\"          \"$(date -u -d \"$ACUAN\" +%Y%m%d-%H%M%S)\"\np \"+%s  (detik epoch)\"      \"$(date -u -d \"$ACUAN\" +%s)\"\np \"format berspasi\"         \"$(date -u -d \"$ACUAN\" +'%d/%m/%Y pukul %H.%M')\"\np \"sehari sebelumnya\"       \"$(date -u -d \"$ACUAN - 1 day\" +%F)\"\np \"seminggu sesudahnya\"     \"$(date -u -d \"$ACUAN + 7 days\" +%F)\"\n\necho\necho \"-- epoch cuma bilangan bulat, jadi selisih waktu itu pengurangan biasa --\"\nmulai=$(date -u -d \"$ACUAN\" +%s)\nselesai=$(( mulai + 95 ))\necho \"mulai   : $mulai -> $(date -u -d \"@$mulai\" +%T)\"\necho \"selesai : $selesai -> $(date -u -d \"@$selesai\" +%T)\"\necho \"lama    : $(( selesai - mulai )) detik\"\n\necho\necho \"-- cap waktu dipakai untuk menamai berkas --\"\necho \"berkas log   : app-$(date -u -d \"$ACUAN\" +%F).log\"\necho \"berkas arsip : backup-$(date -u -d \"$ACUAN\" +%Y%m%d-%H%M%S).tar.gz\"",
            },
            {
                "heading": "tar, gzip, checksum, rsync, envsubst",
                "body": [
                    "Dua alat ini sering dikira satu:",
                    "  - tar menggabungkan banyak berkas jadi satu, tanpa memampatkannya",
                    "    sedikit pun. Memampatkan artinya mengecilkan ukuran berkas.",
                    "  - gzip memampatkan satu berkas, tapi nggak bisa menggabungkan apa",
                    "    pun.",
                    "",
                    "Makanya ekstensinya bertingkat dua: .tar.gz artinya digabung dulu,",
                    "baru dimampatkan.",
                    "",
                    "Huruf-huruf opsi tar boleh ditulis tanpa tanda minus. Itu warisan dari",
                    "versi lama:",
                    "",
                    "  c  create, bikin arsip baru        z  lewatkan gzip  (.gz)",
                    "  x  extract, bongkar                j  lewatkan bzip2 (.bz2)",
                    "  t  table, lihat isinya saja        J  lewatkan xz    (.xz)",
                    "  f  berkas arsipnya bernama ...     v  verbose, sebutkan tiap berkas",
                    "",
                    "  tar czf arsip.tar.gz folder/    kemas",
                    "  tar tzf arsip.tar.gz            lihat isi, tanpa membongkar",
                    "  tar xzf arsip.tar.gz -C tujuan/ bongkar ke folder tertentu",
                    "",
                    "Ada tiga jebakan tar. Dua yang pertama bisa bikin datamu hilang:",
                    "  - f harus ditulis persis sebelum nama arsip, dan nama arsipnya ditulis",
                    "    duluan. Kalau urutannya terbalik jadi",
                    "    tar czf laporan.txt arsip.tar.gz, berkas laporan.txt yang ditimpa",
                    "    jadi arsip. Isinya hilang tanpa satu pun pertanyaan.",
                    "  - Selalu jalankan tar tzf dulu sebelum membongkar arsip dari",
                    "    internet. Ada arsip yang isinya langsung berhamburan ke folder saat",
                    "    ini, dan nggak rapi di dalam satu folder. Arsip seperti itu disebut",
                    "    tarbomb. Bongkar di folder kosong, atau pakai -C.",
                    "  - tar czf a.tar.gz /home/vi/demo menyimpan jalur panjang itu di dalam",
                    "    arsip, dan memberi peringatan 'Removing leading /'. Yang lebih rapi:",
                    "    tar czf a.tar.gz -C /home/vi demo.",
                    "",
                    "gzip berkas.txt mengganti berkasnya jadi berkas.txt.gz, dan berkas",
                    "aslinya hilang. Pakai gzip -k kalau mau menyimpan keduanya. Untuk",
                    "mengembalikannya, pakai gunzip. Untuk membaca isi .gz tanpa",
                    "membongkarnya dulu, pakai zcat atau zgrep.",
                    "",
                    "Memeriksa unduhan",
                    "",
                    "Unduhan yang terpotong di tengah tetap dianggap berhasil oleh curl,",
                    "kalau servernya nggak menyebutkan panjang berkasnya. Makanya berkas",
                    "rilis biasanya disertai berkas .sha256, yaitu sidik jari isi berkasnya:",
                    "",
                    "  sha256sum arsip.tar.gz > arsip.tar.gz.sha256  buat sidik jarinya",
                    "  sha256sum -c arsip.tar.gz.sha256              periksa -> 'OK' atau 'FAILED'",
                    "",
                    "md5sum bekerja dengan pola yang sama. Tapi md5 sudah lama nggak aman",
                    "untuk urusan keamanan. Anggap md5 cuma alat pemeriksa kerusakan, dan",
                    "jangan dipakai sebagai bukti keaslian.",
                    "",
                    "Menyalin antar tempat",
                    "",
                    "  rsync -av --delete sumber/ tujuan/",
                    "",
                    "Arti opsinya:",
                    "  - -a mempertahankan izin, waktu, dan link.",
                    "  - -v menyebutkan berkas yang disalin.",
                    "  - --delete menghapus berkas di tujuan yang sudah nggak ada di sumber.",
                    "",
                    "Kelebihan rsync dibanding cp -r: rsync cuma memindahkan bagian yang",
                    "berubah. Jadi backup kedua dan seterusnya jauh lebih cepat.",
                    "",
                    "Garis miring di ujung sumber menentukan hasilnya, dan ini kesalahan",
                    "klasik:",
                    "",
                    "  rsync -av data/ cadangan/  -> isi data masuk ke cadangan/",
                    "  rsync -av data  cadangan/  -> foldernya sendiri masuk, jadi cadangan/data/",
                    "",
                    "Hati-hati: garis miring yang salah ditambah --delete bisa menghapus isi",
                    "folder tujuan. Coba dulu dengan -n (--dry-run), yang cuma melaporkan",
                    "rencananya tanpa menyentuh apa pun.",
                    "",
                    "Untuk menyalin antar mesin, keduanya bisa lewat ssh:",
                    "",
                    "  scp berkas.txt user@host:/srv/app/          untuk sekali salin",
                    "  rsync -av data/ user@host:/srv/app/data/    untuk yang berulang",
                    "",
                    "envsubst mengganti tiap variabel berbentuk ${...} atau $... di sebuah",
                    "templat dengan nilai dari variabel lingkungan. Alat ini dipakai di",
                    "mana-mana untuk membuat berkas konfigurasi di dalam container, yaitu",
                    "lingkungan terpisah untuk menjalankan aplikasi (misalnya lewat Docker).",
                    "",
                    "Jebakannya besar. Tanpa daftar nama yang diizinkan, envsubst melahap",
                    "semua yang berbentuk variabel, termasuk $host milik nginx yang",
                    "seharusnya dibiarkan. Karena $host nggak ada di lingkungan, hasilnya",
                    "jadi kosong. Batasi dengan menyebutkan nama yang boleh diganti:",
                    "",
                    "  envsubst '${PORT} ${NAMA_APP}' < templat.conf",
                ],
                "code": "#!/usr/bin/env bash\nset -euo pipefail\n\nrm -rf contoh-arsip hasil-bongkar\nmkdir -p contoh-arsip/laporan\necho \"penjualan januari\"  > contoh-arsip/laporan/jan.txt\necho \"penjualan februari\" > contoh-arsip/laporan/feb.txt\necho \"catatan singkat\"    > contoh-arsip/README.txt\n\ncap=$(date -u -d \"2024-03-15 08:30:00 UTC\" +%Y%m%d-%H%M%S)\narsip=\"backup-$cap.tar.gz\"\n\n# c=create  z=gzip  f=nama berkas arsip. Nama arsip ditulis DULUAN.\ntar czf \"$arsip\" contoh-arsip\necho \"arsip dibuat: $arsip\"\n\necho\necho \"== t = daftar isi, tanpa membongkar apa pun ==\"\ntar tzf \"$arsip\"\n\necho\necho \"== sidik jari, supaya ketahuan kalau berkasnya rusak ==\"\nsha256sum \"$arsip\" > \"$arsip.sha256\"\nsha256sum -c \"$arsip.sha256\"\n\necho\necho \"== x = bongkar, -C = ke folder mana ==\"\nmkdir -p hasil-bongkar\ntar xzf \"$arsip\" -C hasil-bongkar\nfind hasil-bongkar -type f | sort\n\necho\necho \"== envsubst: isi templat dari variabel lingkungan ==\"\ncat > templat.conf << 'EOF'\nserver {\n    listen ${PORT};\n    server_name ${NAMA_APP}.contoh.id;\n    proxy_set_header Host $host;\n}\nEOF\nexport PORT=8080 NAMA_APP=tokoku\n\necho '-- envsubst polos: $host punya nginx ikut dimakan jadi kosong --'\nenvsubst < templat.conf\n\necho '-- dibatasi: hanya dua nama ini yang boleh diganti --'\nenvsubst '${PORT} ${NAMA_APP}' < templat.conf\n\nrm -rf contoh-arsip hasil-bongkar templat.conf \"$arsip\" \"$arsip.sha256\"",
            },
            {
                "heading": "Semuanya dalam satu script backup",
                "body": [
                    "Bentuk di bawah adalah kerangka yang berulang di ribuan script nyata:",
                    "ambil data, periksa isinya, kemas dengan nama bercap waktu, lalu catat",
                    "ke log. Urutan membacanya:",
                    "  1. Periksa dulu apakah semua alat yang dibutuhkan ada, sebelum",
                    "     mengerjakan apa pun. Gagal di awal jauh lebih baik daripada gagal",
                    "     sesudah setengah pekerjaan telanjur jalan.",
                    "  2. Berkas sementara dibuat dengan mktemp, lalu dihapus otomatis lewat",
                    "     trap:",
                    "       trap 'rm -f \"$tmp\"' EXIT",
                    "     Polanya sudah dipakai di materi Bekerja dengan File & Folder.",
                    "  3. curl -fsSL ... -o \"$tmp\" mengunduh. Karena ada -f dan set -e,",
                    "     status 404 langsung menghentikan script, jadi halaman error nggak",
                    "     ikut diarsipkan.",
                    "  4. jq membaca hasilnya sebagai data, bukan sebagai teks.",
                    "  5. tar czf dengan cap waktu di namanya, lalu sha256sum sebagai bukti",
                    "     bahwa arsipnya utuh.",
                    "  6. tee -a menaruh tiap kabar di layar dan di log sekaligus.",
                    "",
                    "Ada dua hal yang sengaja dipatok, supaya contoh ini bisa dijalankan",
                    "berulang kali dengan hasil yang persis sama:",
                    "  - Alamat sumber datanya memakai skema file://, karena curl memang",
                    "    bisa membaca berkas lokal. Di script sungguhan, alamatnya",
                    "    https://...",
                    "  - Cap waktunya diambil dari tanggal tetap. Aslinya",
                    "    cap=$(date +%Y%m%d-%H%M%S).",
                ],
                "code": "#!/usr/bin/env bash\nset -euo pipefail\n\n# --- Data contoh. Di dunia nyata bagian ini datang dari server. -------------\nmkdir -p data-gudang\ncat > data-gudang/pesanan.json << 'EOF'\n{\n  \"toko\": \"Cabang Selatan\",\n  \"pesanan\": [\n    {\"id\": \"P-001\", \"barang\": \"kopi\", \"jumlah\": 3, \"lunas\": true},\n    {\"id\": \"P-002\", \"barang\": \"gula\", \"jumlah\": 1, \"lunas\": false},\n    {\"id\": \"P-003\", \"barang\": \"teh\",  \"jumlah\": 5, \"lunas\": true}\n  ]\n}\nEOF\n\n# file:// dipakai supaya contoh ini jalan tanpa jaringan.\n# Di script sungguhan: SUMBER=\"https://api.contoh.id/pesanan.json\"\nSUMBER=\"file://$PWD/data-gudang/pesanan.json\"\nLOG=\"riwayat-backup.log\"\n\n# Cap waktu dipatok supaya hasilnya sama tiap dijalankan.\n# Aslinya: cap=$(date +%Y%m%d-%H%M%S) dan tanggal=$(date +%F)\ncap=$(date -u -d \"2024-03-15 08:30:00 UTC\" +%Y%m%d-%H%M%S)\ntanggal=$(date -u -d \"2024-03-15 08:30:00 UTC\" +%F)\n\ncatat() {\n    echo \"[$tanggal] $*\" | tee -a \"$LOG\"\n}\n\nfor alat in curl jq tar; do\n    command -v \"$alat\" >/dev/null || { echo \"Butuh $alat, belum terpasang.\" >&2; exit 1; }\ndone\n\ntmp=$(mktemp)\ntrap 'rm -f \"$tmp\"' EXIT\n\ncatat \"mengunduh $SUMBER\"\ncurl -fsSL \"$SUMBER\" -o \"$tmp\"\n\njumlah=$(jq '.pesanan | length' \"$tmp\")\nlunas=$(jq '[.pesanan[] | select(.lunas)] | length' \"$tmp\")\ncatat \"diterima $jumlah pesanan, $lunas sudah lunas\"\n\ncp \"$tmp\" data-gudang/pesanan.json\narsip=\"backup-$cap.tar.gz\"\ntar czf \"$arsip\" data-gudang\ncatat \"arsip $arsip dibuat\"\n\nsha256sum \"$arsip\" > \"$arsip.sha256\"\nsha256sum -c --quiet \"$arsip.sha256\" && catat \"sidik jari cocok\"\n\necho\necho \"== isi $LOG ==\"\ncat \"$LOG\"\n\nrm -rf data-gudang \"$arsip\" \"$arsip.sha256\" \"$LOG\"",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pemilik toko online perlu tahu situsnya bisa dibuka atau nggak sebelum",
                    "pelanggan mengeluh. Script kecil yang mengirim permintaan dengan curl,",
                    "mencatat kode status HTTP bersama tanggal, lalu dijalankan tiap pagi",
                    "adalah bentuk paling sederhana dari pemantauan situs.",
                    "",
                    "Kasus kecil: kamu mau satu baris log tiap pemeriksaan, misalnya",
                    "2024-05-17 https://tokoku.contoh.id 200, dan peringatan di stderr kalau",
                    "kodenya bukan 200.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Yang dibutuhkan cuma kode status. Buang isi halamannya dengan",
                    "     -o /dev/null, lalu cetak kodenya dengan -w.",
                    "  2. Batasi waktunya, supaya server yang diam nggak menggantung script:",
                    "      url=\"https://tokoku.contoh.id\"",
                    "      kode=$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 \"$url\")",
                    "      echo \"$(date +%F) $url $kode\" >> cek-situs.log",
                    "      [[ $kode == 200 ]] || echo \"situs bermasalah: kode $kode\" >&2",
                    "  3. date +%F menulis tahun-bulan-tanggal, jadi log yang diurutkan",
                    "     dengan sort tetap urut waktu.",
                    "  4. Uji tiga keadaan. Halaman yang ada memberi 200, halaman yang hilang",
                    "     memberi 404, dan server yang nggak bisa disambung memberi 000",
                    "     dengan exit code curl 7. Kode 000 artinya nggak ada jawaban sama",
                    "     sekali.",
                    "",
                    "Jebakan: kalau situsmu mengalihkan http ke https, curl tanpa -L",
                    "mencatat 301 atau 302, dan script melapor bermasalah padahal situsnya",
                    "sehat.",
                ]
            },
        ],
    },
    {
        "title": "22. Debugging & Praktik Baik",
        "sections": [
            {
                "body": [
                    "Debugging artinya mencari dan membetulkan bug. Ada enam cara untuk",
                    "men-debug script bash:",
                    "  1. bash -x script.sh menampilkan setiap perintah sebelum perintah itu",
                    "     dijalankan. Ini cara tercepat untuk melihat di mana script mulai",
                    "     salah jalan.",
                    "  2. set -x dan set +x di dalam script menyalakan dan mematikan",
                    "     pelacakan yang sama, cuma di bagian tertentu.",
                    "  3. bash -n script.sh cuma mengecek sintaks, tanpa menjalankan apa",
                    "     pun.",
                    "  4. shellcheck script.sh menjalankan linter khusus bash, yaitu alat",
                    "     yang membaca kodemu lalu menunjuk bagian yang mencurigakan. Pakai",
                    "     selalu. Alat ini menangkap bug yang nggak kelihatan mata, seperti",
                    "     variabel tanpa petik atau perbandingan yang salah. Cara",
                    "     memasangnya:",
                    "       sudo dnf install ShellCheck      (Fedora)",
                    "       sudo apt install shellcheck      (Debian/Ubuntu)",
                    "       brew install shellcheck          (macOS)",
                    "  5. echo bisa dipakai untuk melacak nilai variabel:",
                    "       echo \"DEBUG: nilai=$nilai\" >&2",
                    "     Kirim ke stderr seperti itu, supaya keluaran asli script nggak",
                    "     terganggu.",
                    "  6. Pasang baris ini di awal script:",
                    "       trap 'echo \"gagal di baris $LINENO\" >&2' ERR",
                    "     Begitu ada perintah yang gagal, nomor barisnya tercetak sendiri.",
                    "     Ini paling menolong di script panjang yang jalan dengan set -e,",
                    "     karena set -e menghentikan script tanpa memberi tahu di baris mana",
                    "     dia berhenti.",
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
                "heading": "Sepuluh praktik baik dan kesalahan pemula",
                "body": [
                    "Praktik baik yang dipakai di kerangka di atas:",
                    "  1. Shebang #!/usr/bin/env bash di baris pertama.",
                    "  2. Komentar penjelasan di kepala berkas.",
                    "  3. set -euo pipefail, supaya script berhenti begitu ada masalah.",
                    "  4. readonly untuk nilai yang nggak boleh berubah.",
                    "  5. Fungsi pesan() dan galat() supaya bentuk keluarannya seragam.",
                    "  6. Fungsi bantuan() yang memakai heredoc.",
                    "  7. Semua logika ditaruh di dalam fungsi utama().",
                    "  8. utama \"$@\" dipanggil di baris terakhir.",
                    "  9. local untuk semua variabel di dalam fungsi.",
                    "  10. Semua variabel dibungkus petik ganda.",
                    "",
                    "Ini kesalahan pemula yang paling sering:",
                    "  - Ada spasi di sekitar = waktu membuat variabel.",
                    "  - Lupa membungkus variabel dengan petik.",
                    "  - Pakai [ ] padahal [[ ]] lebih aman.",
                    "  - Pakai -eq untuk membandingkan teks. -eq itu untuk angka.",
                    "  - Mengira return mengirim data, padahal return cuma mengirim status.",
                    "  - Menjalankan rm -rf \"$folder/\"* tanpa memastikan $folder nggak",
                    "    kosong. Kalau $folder kosong, perintah itu berubah jadi rm -rf /*,",
                    "    yang mencoba menghapus seluruh isi sistem, termasuk semua berkas",
                    "    milikmu. Pengamannya: tulis \"${folder:?}\", supaya bash berhenti",
                    "    dengan pesan error kalau variabelnya kosong.",
                ]
            },
            {
                "heading": "Dua hal yang belum ada di kerangka itu",
                "body": [
                    "Kerangka di atas sudah cukup untuk script yang kamu pakai sendiri.",
                    "Begitu script itu dipakai orang lain, biasanya ada dua hal yang",
                    "ditambahkan.",
                    "",
                    "Yang pertama: periksa dependensi sebelum mulai bekerja. Dependensi",
                    "adalah program lain yang dibutuhkan script-mu. Pemeriksaan dengan",
                    "command -v beserta alasannya sudah dibahas di materi Proses, source,",
                    "dan Subshell. Yang baru di sini cuma bentuknya. Karena galat() sudah",
                    "tersedia, satu perulangan cukup untuk memeriksa berapa pun alat yang",
                    "dipakai:",
                    "",
                    "  for alat in jq curl; do",
                    "      command -v \"$alat\" >/dev/null 2>&1 || galat \"butuh $alat\"",
                    "  done",
                    "",
                    "Taruh perulangan itu di baris pertama utama(), jangan di kepala berkas.",
                    "Fungsi harus sudah terbaca sebelum dipanggil, dan galat() baru",
                    "didefinisikan di tengah berkas. Kalau perulangan itu ditaruh di atas",
                    "galat(), script yang kekurangan alat malah menjawab 'galat: command not",
                    "found', tepat di saat pesannya paling dibutuhkan.",
                    "",
                    "Yang kedua: uraikan opsi dengan getopts. Baris [[ \"${1:-}\" == \"-h\" ]]",
                    "di kerangka itu cuma mengenali -h, dan cuma kalau -h jadi argumen",
                    "pertama. Begitu opsinya bertambah, misalnya jadi -v, -o berkas, atau",
                    "gabungan seperti -hv, ganti dengan getopts. Caranya ada di materi Opsi",
                    "Baris Perintah & getopts.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Script yang udah lama jalan di server bisa tiba-tiba berhenti di",
                    "tengah tanpa pesan, biasanya sesudah ada yang mengubahnya sedikit.",
                    "Orang yang membereskannya jarang langsung tahu baris mana yang salah,",
                    "jadi dia mencari dulu pakai bash -x, bukan menebak.",
                    "",
                    "Kasus kecil: rekap-absen.sh diawali set -euo pipefail dan hadir=0,",
                    "lalu menghitung huruf H (hadir) di absen.txt. Kemarin temanmu merapikan",
                    "baris hadir=$((hadir + 1)) jadi ((hadir++)). Sejak itu script selesai",
                    "tanpa mencetak apa pun, dan echo $? memberi 1.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan bash -x rekap-absen.sh. Baris terakhir yang tercetak",
                    "     sebelum berhenti adalah + (( hadir++ )), dari bagian ini:",
                    "      while IFS= read -r status; do",
                    "          [[ $status == H ]] && ((hadir++))",
                    "      done < absen.txt",
                    "  2. Cocokkan dengan aturan yang udah kamu tahu: ((hadir++)) waktu",
                    "     hadir masih 0 memberi status 1, dan set -e menghentikan script di",
                    "     situ.",
                    "  3. Kembalikan ke hadir=$((hadir + 1)), yang selalu sukses. Untuk",
                    "     absen.txt berisi H, S, H, I, H, hasilnya hadir: 3 hari.",
                    "  4. Pasang penangkap di bawah baris set, supaya lain kali nomor baris",
                    "     yang gagal langsung tercetak:",
                    "      trap 'echo \"gagal di baris $LINENO\" >&2' ERR",
                    "  5. Uji juga data tanpa huruf H. Versi rusak lolos dengan data itu,",
                    "     jadi data uji seperti itu nggak akan menemukan bug ini.",
                ]
            },
        ],
    },
    {
        "title": "23. Bash vs sh: Portabilitas & POSIX",
        "sections": [
            {
                "body": [
                    "Semua contoh di kurikulum ini diawali shebang #!/usr/bin/env bash.",
                    "Sekarang kita lihat apa yang terjadi kalau baris itu diganti jadi",
                    "#!/bin/sh. Berkas seperti itu pasti bakal kamu temui, dan isinya",
                    "kelihatan aneh kalau kamu belum tahu sebabnya.",
                    "",
                    "Banyak orang mengira sh itu nama pendek dari bash. Padahal sh adalah",
                    "spesifikasi, yaitu daftar fitur minimum yang disepakati dalam standar",
                    "bernama POSIX. Program yang mengisi peran sh beda-beda di tiap sistem:",
                    "  - Debian dan Ubuntu: dash, ukurannya sekitar 120 KB.",
                    "  - Alpine (image Docker): busybox ash, satu biner untuk ratusan",
                    "    perintah.",
                    "  - Fedora dan Arch: bash dalam mode sh, ukurannya sekitar 1,5 MB.",
                    "  - macOS: bash 3.2 dalam mode sh.",
                    "",
                    "Image Docker adalah paket berisi sistem siap pakai untuk menjalankan",
                    "program di dalam container. Cek punya mesinmu sendiri:",
                    "",
                    "  ls -l /bin/sh",
                    "  readlink -f /bin/sh",
                    "",
                    "Kenapa Debian repot-repot memakai shell mungil, dan nggak pakai bash",
                    "aja? /bin/sh dipanggil ribuan kali waktu sistem menyala. dash menyala",
                    "jauh lebih cepat dan memakan memori jauh lebih sedikit. Alpine lebih",
                    "ekstrem lagi: di sana bash memang nggak terpasang. Ukuran kecil itu",
                    "memang tujuan desainnya, dan bukan kebetulan.",
                    "",
                    "Script sh bakal kamu temui di banyak tempat, mau atau nggak:",
                    "  - Dockerfile. RUN dan ENTRYPOINT dalam bentuk shell memanggil",
                    "    /bin/sh -c, dan nggak memanggil bash.",
                    "  - Image Alpine dan image 'slim' lain yang sengaja dipangkas.",
                    "  - Git hook (script yang dijalankan otomatis oleh Git) di",
                    "    .git/hooks/, script init di /etc/init.d, dan entri cron (jadwal",
                    "    tugas otomatis).",
                    "  - ./configure bawaan proyek C, dan installer bergaya",
                    "    'curl -fsSL ... | sh'.",
                    "",
                    "Installer model curl ... | sh menjalankan script dari internet tanpa",
                    "kamu baca dulu. Pakai cuma dari sumber yang kamu percaya.",
                    "",
                    "Fitur bash yang nggak ada di sh punya sebutan sendiri: bashism. Kata",
                    "itu bakal kamu lihat di laporan bug dan di komentar kode.",
                ],
            },
            {
                "heading": "bashisme.sh: mulus di bash, hancur di sh",
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
                "heading": "Pesan galat bashism dan padanannya di sh",
                "body": [
                    "Jalankan berkas di atas dengan bash: sembilan baris keluar rapi, tanpa",
                    "keluhan. Sekarang ganti baris pertamanya jadi #!/bin/sh, lalu jalankan",
                    "di Debian atau Alpine. Pesan yang keluar nggak satu pun menyebut kata",
                    "'bash'. Kalau tiap bashism dicoba satu per satu, pesannya seperti ini:",
                    "",
                    "  Syntax error: word unexpected (expecting \")\")  <- baris buah=(...)",
                    "  Syntax error: redirection unexpected           <- baris <<<",
                    "  [[: not found                                  <- [[ ]] bukan sintaks di sh",
                    "  Bad substitution                               <- ${nama^^}",
                    "  pesan+= dunia: not found                       <- += pada string",
                    "  n++: not found                                 <- (( )) dibaca jadi subshell",
                    "  source: not found                              <- sh cuma punya titik (.)",
                    "",
                    "Ada dua hal yang bikin pesan-pesan ini susah dikenali pemula.",
                    "",
                    "Pertama, soal urutan. Pesan 'Syntax error' muncul waktu sh membaca",
                    "sebuah baris, sebelum baris itu dijalankan, dan sh langsung berhenti",
                    "di situ. Jadi satu kali jalan cuma menghasilkan satu pesan seperti",
                    "itu. Di bashisme.sh, baris buah=(...) sudah ketemu sebelum echo yang",
                    "pertama, jadi script itu nggak mencetak apa-apa sama sekali. Nomor",
                    "baris di pesannya menunjuk ke tempat sh menyerah, yang belum tentu",
                    "baris yang salah.",
                    "",
                    "Kedua, soal kata 'not found'. Buat sh, [[, n++, dan source cuma nama",
                    "perintah biasa yang kebetulan nggak ada di PATH. sh nggak tahu kamu",
                    "bermaksud memakai fitur bash, jadi dia nggak bisa memberi tahu itu.",
                    "Pesan 'not found' untuk tanda kurung siku hampir selalu berarti satu",
                    "hal: script bash dijalankan oleh shell yang bukan bash.",
                    "",
                    "Yang paling berbahaya justru bashism yang nggak memunculkan pesan apa",
                    "pun:",
                    "",
                    "  ls /folder/tidak/ada &> /dev/null",
                    "",
                    "Di sh, & adalah operator \"jalankan di latar belakang\", dan & menutup",
                    "perintahnya. Jadi baris itu dibaca sebagai dua perintah. Yang pertama",
                    "ls ... &, yang dilepas ke latar belakang. Yang kedua > /dev/null,",
                    "perintah kosong yang cuma membuat berkas. Akibatnya pesan error tetap",
                    "tumpah ke layar, dan script jalan terus seolah semuanya beres.",
                    "",
                    "Kalau maksudmu cmd &> laporan.log, berkas laporan.log memang dibuat,",
                    "tapi lalu dikosongkan dan nggak pernah diisi apa-apa. Nggak ada error,",
                    "cuma hasilnya yang salah.",
                    "",
                    "Berikut daftar bashism dan padanan POSIX-nya. Kolom kanan jalan di",
                    "bash maupun di sh:",
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
                    "  local x=1                     ada di dash & busybox, tapi bukan janji POSIX",
                    "",
                    "Baris terakhir itu jebakan halus. local jalan di hampir semua sh yang",
                    "bakal kamu temui, jadi orang terus memakainya. Tapi local nggak",
                    "dijamin oleh standar. Kalau targetmu memang shell apa pun, pakai nama",
                    "variabel dengan awalan khas, misalnya _cetak_n.",
                    "",
                    "Lihat juga ${teks:0:5} dan ${teks/lama/baru}. Materi Operasi String",
                    "mengajarkan keduanya bareng ${#teks}, ${berkas%.txt}, dan",
                    "${var:-bawaan}, seolah semuanya satu keluarga. Padahal tiga yang",
                    "terakhir itu POSIX asli, sedangkan substring dan penggantian teks",
                    "murni bashism. Jadi bentuk ${...} yang mirip belum tentu jalan di sh.",
                ],
            },
            {
                "heading": "posix.sh: pekerjaan yang sama, tanpa satu pun bashism",
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
                "heading": "Perintah [ ] dan cara menguji portabilitas",
                "body": [
                    "Dua catatan dari posix.sh:",
                    "  - Perintah . ./konfig.sh: titiknya wajib diikuti ./ kalau berkasnya",
                    "    ada di folder saat ini. Tanpa garis miring, sh mencari berkas itu",
                    "    di PATH, dan biasanya nggak ketemu. bash lebih longgar soal ini,",
                    "    jadi kebiasaan source konfig.sh baru rusak waktu dijalankan sh.",
                    "  - Aritmatika $(( n + 1 )) itu POSIX. Yang bashism cuma bentuk",
                    "    ((n++)) yang berdiri sendiri sebagai perintah. Jangan sampai",
                    "    ketuker.",
                    "",
                    "Sekarang soal [ ], dan kenapa [ ] bertebaran di kode nyata.",
                    "",
                    "Materi Percabangan (if, case) menyebut [ ] sebagai \"perintah lama\"",
                    "dan menyuruhmu memakai [[ ]]. Saran itu benar selama shebang-mu bash.",
                    "Begitu berkasnya #!/bin/sh, [[ ]] nggak ada, dan [ ] jadi satu-satunya",
                    "cara membandingkan apa pun. Coba buka entrypoint sebuah image Docker,",
                    "yaitu script yang pertama dijalankan waktu container mulai. Kalau",
                    "isinya [ -z \"$1\" ] semua, penulisnya nggak ketinggalan zaman. Dia",
                    "sengaja menulis untuk shell yang memang nggak punya [[ ]].",
                    "",
                    "Kata \"perintah\" di situ harfiah. [ adalah sebuah program, dan",
                    "berkasnya ada:",
                    "",
                    "  ls -l /usr/bin/[        -> ada, kembarannya bernama test",
                    "",
                    "bash juga punya [ versi bawaan (builtin), dan aturannya sama: [",
                    "diperlakukan sebagai perintah biasa. Karena itu isi variabel sudah",
                    "dipecah per spasi sebelum [ sempat melihatnya:",
                    "",
                    "  x=\"dua kata\" ; [ $x = ya ]   ->  bash: [: too many arguments",
                    "",
                    "Di dalam [ ], petik ganda itu wajib. Di [[ ]], petik cuma anjuran.",
                    "[[ ]] aman karena dia sintaks yang dibaca shell sendiri, dan nggak",
                    "diperlakukan sebagai perintah yang menerima daftar kata.",
                    "",
                    "Cara menguji portabilitas sebelum script-mu dipakai orang lain:",
                    "  - sh -n script.sh mengecek sintaks tanpa menjalankan apa pun. Di sh",
                    "    yang bukan bash, perintah ini menangkap array dan <<<. Tapi [[ ]]",
                    "    nggak ketangkap, karena buat sh itu cuma nama perintah, dan nama",
                    "    perintah baru dicari waktu dijalankan.",
                    "  - dash script.sh menjalankannya sungguhan di dash. Ini bukti yang",
                    "    paling jujur. Kalau dash belum ada, pasang dulu: sudo dnf install",
                    "    dash di Fedora, atau sudo apt install dash di Debian dan Ubuntu",
                    "    (di sana dash biasanya sudah terpasang sebagai /bin/sh).",
                    "  - shellcheck -s sh f.sh. shellcheck sudah dikenalkan di materi",
                    "    Debugging & Praktik Baik. Opsi -s sh memaksanya menilai pakai",
                    "    aturan sh, lalu dia menandai tiap bashism satu per satu.",
                    "  - checkbashisms f.sh, alat yang tugasnya cuma itu. Di Debian, alat",
                    "    ini ada di paket devscripts.",
                    "",
                    "Jebakan saat menguji: di Fedora dan Arch, /bin/sh itu sendiri adalah",
                    "bash. Jadi sh script.sh di mesin seperti itu bisa lolos mulus padahal",
                    "script-nya penuh bashism, karena bash dalam mode sh tetap mengerti",
                    "[[ ]], array, dan <<<. Lulus uji di sana nggak membuktikan apa-apa.",
                    "Pasang dash, atau jalankan di container Alpine.",
                    "",
                    "Kapan pilih yang mana:",
                    "  - Pakai bash kalau script-nya untuk mesin yang kamu kendalikan, atau",
                    "    kalau kamu butuh array, declare -A, regex =~, dan ${teks^^}. Tulis",
                    "    #!/usr/bin/env bash tanpa perlu merasa bersalah. Ini pilihan",
                    "    bawaan yang sehat, dan bukan tanda malas.",
                    "  - Pakai sh kalau script-nya masuk ke image Docker minimal, jadi",
                    "    installer yang dipanggil lewat pipe, atau harus jalan di sistem",
                    "    yang nggak kamu kenal.",
                    "",
                    "Jangan menulis #!/bin/sh lalu tetap memakai [[ ]] dan array. Di",
                    "mesinmu script itu jalan, karena sh-mu bash. Di mesin orang lain dia",
                    "mati. Ini salah satu bug yang paling sering dilaporkan pada script",
                    "pemasangan. Pilih salah satu, lalu konsisten sampai akhir. Shebang",
                    "menentukan shell mana yang menjalankan berkasnya, jadi isi berkasnya",
                    "harus cocok dengan shell itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Image Docker berbasis Debian memakai dash sebagai /bin/sh, dan",
                    "entrypoint.sh di image seperti itu biasanya diawali #!/bin/sh. Script",
                    "yang ditulis di laptop Fedora, tempat sh adalah bash, bisa lolos semua",
                    "uji di sana lalu memunculkan pesan seperti '[[: not found' di container.",
                    "",
                    "Kasus kecil: entrypoint.sh lamamu memuat config dengan source, memeriksa",
                    "NAMA_APP dengan [[ -z ]], lalu diakhiri exec \"$@\". Di container berbasis",
                    "Debian keluar dua pesan not found. Config nggak termuat, dan",
                    "pemeriksaan NAMA_APP nggak pernah berlaku.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan dulu shell-nya. Shebang #!/bin/sh berarti isi berkas",
                    "     harus POSIX, jadi tiap bashism perlu padanannya.",
                    "  2. Ganti satu per satu pakai tabel di materi ini: [[ ]] jadi [ ]",
                    "     dengan petik ganda, source jadi . ./config.sh, dan nilai bawaan",
                    "     pakai ${PORT:-8080} yang memang POSIX:",
                    "      #!/bin/sh",
                    "      export PORT=\"${PORT:-8080}\"",
                    "      if [ -z \"$NAMA_APP\" ]; then",
                    "          echo \"NAMA_APP wajib diisi\" >&2; exit 1",
                    "      fi",
                    "      exec \"$@\"",
                    "  3. Perhatikan export di baris kedua. Tanpa itu, PORT cuma ada di",
                    "     shell entrypoint, dan aplikasi yang dijalankan exec nggak",
                    "     melihatnya.",
                    "  4. Jangan percaya uji di Fedora, karena di sana sh adalah bash, dan",
                    "     versi lama pun lolos. Uji dengan dash entrypoint.sh, dengan",
                    "     shellcheck -s sh, atau langsung di container-nya.",
                ]
            },
        ],
    },
    {
        "title": "24. Fitur Bash Lanjutan",
        "sections": [
            {
                "body": [
                    "Materi ini mengumpulkan hal-hal yang sering muncul di script orang",
                    "lain, tapi belum pernah dibahas di sini. Fiturnya nggak aneh-aneh.",
                    "Semuanya lazim di script produksi, dan masing-masing pernah bikin",
                    "orang mengira bash-nya rusak, padahal dia cuma belum tahu aturannya.",
                    "",
                    "declare, perintah deklarasi umum",
                    "",
                    "Sejauh ini declare cuma muncul sekali, yaitu sebagai declare -A waktu",
                    "membuat associative array. Wajar kalau kamu mengira declare itu mantra",
                    "khusus untuk map. Padahal declare adalah perintah deklarasi umum: dia",
                    "membuat variabel sekaligus menempelkan sifat pada variabel itu.",
                    "",
                    "  declare -HURUF nama=nilai",
                    "",
                    "  -i   integer  isinya selalu dihitung sebagai bilangan",
                    "  -r   readonly sekali diisi tidak boleh diubah lagi",
                    "  -a   array    array biasa, indeks angka",
                    "  -A   map      associative array, indeks teks",
                    "  -x   export   ikut terbawa ke program yang dijalankan script ini",
                    "  -g   global   tembus keluar walaupun ditulis di dalam fungsi",
                    "  -n   nameref  variabel yang isinya nama variabel lain",
                    "  -p   print    cetak variabel apa adanya lengkap dengan sifatnya",
                    "",
                    "Ternyata declare satu keluarga dengan perintah yang sudah kamu pakai",
                    "sejak awal:",
                    "",
                    "  local nama=\"Andi\"     sama dengan   declare nama=\"Andi\"   (dalam fungsi)",
                    "  readonly VERSI=\"1.4\"  sama dengan   declare -r VERSI=\"1.4\"",
                    "  export PORT=8080      sama dengan   declare -x PORT=8080",
                    "",
                    "Kerangka script di materi Debugging & Praktik Baik memakai readonly",
                    "dan local di mana-mana. Keduanya cuma nama lain untuk declare dengan",
                    "satu sifat yang sudah dipilihkan. Ada satu beda kecil: di dalam",
                    "fungsi, declare membuat variabel lokal, kecuali diberi -g. Jadi",
                    "declare -r dan declare -x di dalam fungsi cuma berlaku di fungsi itu,",
                    "sedangkan readonly dan export tetap mengenai variabel global.",
                    "",
                    "Yang paling mengejutkan: declare -i",
                    "",
                    "  hitung=0             lalu hitung+=1 dua kali  ->  \"011\"",
                    "  declare -i hitung=0  lalu hitung+=1 dua kali  ->  2",
                    "",
                    "Operator += yang sama persis punya dua arti. bash nggak punya tipe",
                    "data, jadi += di variabel biasa artinya menyambung teks. Angka 0",
                    "disambung 1, lalu disambung 1 lagi, menghasilkan teks \"011\". Sifat -i",
                    "menempel di variabelnya, dan nggak di operatornya. Sifat itulah yang",
                    "mengubah arti += jadi penjumlahan. Kalau sebuah += memberi hasil yang",
                    "aneh, curigai ini dulu.",
                    "",
                    "declare -p adalah alat debugging yang paling sering terlupa:",
                    "",
                    "  declare -p umur",
                    "",
                    "Perintah ini mencetak variabel apa adanya: isinya, sekaligus apakah",
                    "dia array, map, readonly, atau integer. echo menyembunyikan semua",
                    "informasi itu. Malah echo \"$umur\" pada sebuah map nggak mencetak",
                    "apa-apa, sehingga kamu mengira datanya hilang.",
                ],
            },
            {
                "heading": "declare beraksi",
                "code": "#!/usr/bin/env bash\n\ndeclare -i hitung=0        # -i : bilangan\ndeclare -r VERSI=\"1.4\"     # -r : hanya-baca, sama dengan readonly\ndeclare -A umur=()         # -A : associative array\n\nhitung+=1\nhitung+=1\n\nbiasa=0\nbiasa+=1\nbiasa+=1\n\necho \"declare -i, dua kali +=  : $hitung\"\necho \"variabel biasa, dua kali : $biasa\"\n\n# Variabel -i selalu MENGHITUNG isinya, walau yang diisikan berupa teks\nhitung=\"7 * 6\"\necho \"variabel -i diisi '7 * 6': $hitung\"\n\n# declare -p: lihat isi DAN sifat sebuah variabel\ndeclare -p hitung\ndeclare -p VERSI\ndeclare -p umur\n\n# Menulis ke variabel readonly ditolak. Dicoba di dalam subshell ( ... )\n# supaya script ini tidak ikut mati saat penolakannya terjadi.\nif ( VERSI=\"2.0\" ) 2>/dev/null; then\n    echo \"VERSI berubah\"\nelse\n    echo \"VERSI ditolak: hanya-baca\"\nfi\n\npasang() {\n    declare -g SUDAH=\"ya\"      # -g : tembus keluar dari fungsi\n    local sementara=\"hilang\"   # local = declare biasa di dalam fungsi\n    echo \"di dalam fungsi : sementara=$sementara\"\n}\n\npasang\necho \"setelah fungsi  : SUDAH=$SUDAH sementara=${sementara:-<kosong>}\"",
            },
            {
                "heading": "Nameref: mengoper array ke fungsi",
                "body": [
                    "Materi Fungsi sudah menunjukkan masalahnya. Array yang dikirim ke",
                    "fungsi cuma sampai sebagai salinan, dan cuma bisa satu array. Di",
                    "materi itu juga disebut bahwa jalan keluarnya ada di sini.",
                    "",
                    "Cara naif yang biasa dicoba orang:",
                    "",
                    "  proses \"${buah[@]}\"",
                    "",
                    "Baris itu nggak mengirim satu array. Isi array-nya meleleh jadi",
                    "argumen terpisah: $1=apel, $2=jeruk, $3=mangga. Fungsi nggak punya",
                    "cara untuk tahu di mana array-nya berakhir dan argumen lain mulai.",
                    "Fungsi juga sama sekali nggak bisa mengubah array aslinya.",
                    "",
                    "Jawabannya nameref, yaitu variabel yang menunjuk ke variabel lain",
                    "lewat namanya. Kirim nama array-nya, tanpa tanda dolar, lalu di dalam",
                    "fungsi tulis:",
                    "",
                    "  local -n daftar=\"$1\"",
                    "",
                    "Sekarang daftar adalah nama lain untuk variabel yang namanya tersimpan",
                    "di $1, dan nggak lagi salinan. Menulis ke daftar berarti menulis ke",
                    "array aslinya. Ini satu-satunya cara rapi untuk mengirim sekaligus",
                    "mengubah array di dalam fungsi. Nameref butuh bash 4.3 ke atas.",
                    "",
                    "Jebakan: nama lokal nameref nggak boleh sama dengan nama yang",
                    "dikirim.",
                    "",
                    "  tambah() { local -n daftar=\"$1\"; daftar+=(\"x\"); }",
                    "  daftar=(\"a\"); tambah daftar",
                    "",
                    "bash mengeluh 'circular name reference', karena nameref itu diminta",
                    "menunjuk dirinya sendiri. Makanya kebiasaan yang berlaku adalah",
                    "memberi awalan garis bawah pada nameref: local -n _daftar=\"$1\".",
                    "",
                    "Ekspansi tak langsung: ${!nama}",
                    "",
                    "Bentuk ini kembaran nameref versi sekali pakai. Dia mengambil nilai",
                    "dari variabel yang namanya tersimpan di $nama.",
                    "",
                    "  warna=\"hijau\"; kunci=\"warna\"; echo \"${!kunci}\"   ->  hijau",
                    "",
                    "Ada dua bentuk yang mirip sekali, tapi artinya jauh beda:",
                    "",
                    "  ${!kunci}      nilai variabel yang namanya ada di $kunci",
                    "  ${!buah[@]}    daftar indeks array buah (sudah dipakai di materi Array)",
                    "",
                    "Tanda serunya sama, aturannya lain sama sekali. Yang menentukan adalah",
                    "ada atau nggaknya [@] di belakangnya.",
                    "",
                    "export -f",
                    "",
                    "Variabel bisa di-export supaya terbawa ke proses anak, yaitu program",
                    "yang dijalankan dari script-mu. Fungsi nggak ikut terbawa, kecuali",
                    "kamu minta:",
                    "",
                    "  export -f sapa",
                    "",
                    "Tanpa export -f, fungsi yang dipanggil lewat bash -c menghasilkan",
                    "'sapa: command not found'. Pesan ini membingungkan, karena fungsinya",
                    "jelas ada beberapa baris di atas. Yang berubah adalah siapa yang",
                    "menjalankannya. bash -c memulai proses bash lain, dan proses itu belum",
                    "pernah membaca script-mu.",
                    "",
                    "Lewat xargs dan find -exec, fungsi juga harus dipanggil lewat bash -c.",
                    "xargs dan find menjalankan program secara langsung, jadi mereka sama",
                    "sekali nggak kenal fungsi bash, bahkan yang sudah di-export. Contoh di",
                    "bawah memakai xargs -I{} bash -c 'sapa \"{}\"' karena alasan itu.",
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
                    "$? cuma memberi kode keluar perintah terakhir. Di sebuah pipeline,",
                    "perintah terakhir itu tahap paling kanan. Padahal tahap paling kanan",
                    "sering cuma penyalur yang hampir selalu sukses.",
                    "",
                    "  jalankan_tes | tee hasil.log",
                    "",
                    "Kalau jalankan_tes gagal tapi tee berhasil menulis log, $? bernilai 0.",
                    "Di CI, yaitu sistem yang otomatis menjalankan tes tiap kali kode",
                    "diubah, build-nya dinyatakan hijau padahal tesnya merah. Kegagalannya",
                    "tertutup exit code milik tee. Bug seperti ini bisa lama nggak",
                    "ketahuan, karena nggak ada yang kelihatan salah.",
                    "",
                    "${PIPESTATUS[@]} adalah array berisi kode keluar tiap tahap:",
                    "",
                    "  ${PIPESTATUS[0]}    tahap pertama",
                    "  ${PIPESTATUS[-1]}   tahap terakhir, ini yang nilainya sama dengan $?",
                    "",
                    "Perbaikannya cukup satu baris:",
                    "",
                    "  exit \"${PIPESTATUS[0]}\"",
                    "",
                    "Jebakan: umur isi PIPESTATUS cuma satu perintah. Isinya ditulis ulang",
                    "oleh perintah berikutnya, termasuk oleh echo, oleh [[ ]], bahkan oleh",
                    "pengisian variabel biasa. Jadi kode ini salah:",
                    "",
                    "  uji | tee log",
                    "  echo \"selesai\"",
                    "  exit \"${PIPESTATUS[0]}\"     <- ini kode keluar echo, bukan uji",
                    "",
                    "Salin dulu isinya, baru dipakai:",
                    "",
                    "  tahap=(\"${PIPESTATUS[@]}\")",
                    "",
                    "Kadang kamu nggak perlu tahu tahap mana yang gagal. Kamu cuma ingin",
                    "pipeline dianggap gagal begitu ada satu bagian yang gagal. Untuk itu,",
                    "set -o pipefail dari materi Argumen & Exit Code sudah cukup.",
                    "PIPESTATUS dipakai kalau kamu perlu menunjuk tahap tertentu.",
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
                    "set -e, set -u, dan set -o pipefail sudah kamu kenal. shopt adalah",
                    "kotak saklar yang lain, berisi puluhan opsi khusus bash:",
                    "",
                    "  shopt -s nama    nyalakan",
                    "  shopt -u nama    matikan",
                    "  shopt            lihat semuanya beserta statusnya",
                    "",
                    "nullglob dari materi Bekerja dengan File & Folder adalah salah satunya.",
                    "Ada empat lagi yang paling sering kamu temui di script orang:",
                    "",
                    "  globstar     ** cocok menembus subfolder:  src/**/*.js",
                    "               Tanpa ini, ** tidak lebih dari * biasa, satu tingkat saja.",
                    "  extglob      pola diperluas:",
                    "                 !(*.txt)   semua kecuali yang berakhiran .txt",
                    "                 +(a|b)     satu kali atau lebih a atau b",
                    "                 @(x|y)     tepat satu dari x atau y",
                    "                 ?(x)       nol atau satu x",
                    "  nocasematch  [[ ]] dan case jadi abai huruf besar/kecil",
                    "  failglob     pola yang tidak cocok apa pun jadi error, bukan didiamkan",
                    "",
                    "Jebakan: shopt -s extglob mengubah cara bash membaca pola, dan nggak",
                    "cuma cara mencocokkannya. Pola seperti !(*.txt) baru sah sebagai",
                    "sintaks kalau extglob sudah menyala waktu barisnya dibaca. Ada dua",
                    "akibat nyata:",
                    "  - Taruh shopt -s extglob di paling atas script. Kalau shopt dan",
                    "    polanya ada di dalam satu fungsi atau satu blok { } yang sama, bash",
                    "    sudah telanjur membaca seluruh blok itu sebelum shopt sempat jalan.",
                    "    Yang muncul lalu syntax error, dan bukan pola yang gagal cocok.",
                    "  - bash -n script.sh bakal melaporkan syntax error di pola extglob,",
                    "    padahal script-nya jalan mulus. bash -n cuma membaca, jadi",
                    "    shopt-nya nggak pernah dijalankan. Jangan buru-buru percaya laporan",
                    "    itu.",
                    "",
                    "Jalan aman yang nggak tersandung dua-duanya: simpan polanya di",
                    "variabel.",
                    "",
                    "  bukan_txt='!(*.txt)'",
                    "  for f in demo/$bukan_txt; do ...",
                    "",
                    "Polanya baru terbentuk waktu script berjalan, jadi pembacaannya nggak",
                    "pernah bermasalah. Contoh di bawah memakai bentuk ini.",
                    "",
                    "nocasematch perlu diwaspadai. Opsi ini mengubah arti kode yang sudah",
                    "ditulis, dari tempat yang jauh. Sebuah [[ \"$x\" == \"ya\" ]] di baris 200",
                    "bisa berubah perilakunya gara-gara satu shopt -s di baris 3, dan",
                    "kodenya sendiri nggak menunjukkan tanda apa pun. Nyalakan seperlunya,",
                    "lalu matikan lagi.",
                    "",
                    "Variabel khusus lainnya:",
                    "",
                    "  $RANDOM        bilangan acak 0-32767. Untuk main-main saja, jangan",
                    "                 untuk password atau token, karena polanya bisa ditebak.",
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
                    "Dua nama terakhir, supaya nggak asing waktu kamu menemukannya.",
                    "",
                    "  readarray -t baris < berkas.txt",
                    "",
                    "readarray adalah nama lain mapfile, yang sudah kamu kenal dari materi",
                    "Array dan materi find, xargs, dan Pemrosesan Massal. Perintah ini",
                    "membaca semua baris jadi array sekaligus, dan -t membuang karakter",
                    "baris baru di tiap baris. Bentuk ini lebih ringkas daripada loop while",
                    "read, tapi seluruh isi berkas dimuat ke memori. Jadi jangan dipakai",
                    "untuk berkas raksasa.",
                    "",
                    "  coproc SEBUT { perintah; }",
                    "",
                    "coproc menjalankan perintah di latar belakang dengan pipa dua arah,",
                    "jadi script bisa berkirim data dengan perintah itu. Kata sesudah",
                    "coproc adalah nama yang kamu pilih untuk proses itu. Fitur ini jarang",
                    "dibutuhkan. Cukup tahu kata ini ada, supaya kamu nggak panik waktu",
                    "melihatnya.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem CI menjalankan tes tiap kali kode diubah, dan banyak langkahnya",
                    "berbentuk ./uji.sh | tee hasil-uji.log, supaya hasil tes tampil di",
                    "layar sekaligus tersimpan. Bentuk itu punya satu lubang: exit code yang",
                    "dilihat CI adalah milik tee.",
                    "",
                    "Kasus kecil: uji.sh mencetak \"12 tes jalan, 1 gagal\" lalu keluar dengan",
                    "kode 1. Langkah CI-mu tetap hijau, karena baris penutupnya cuma",
                    "./uji.sh | tee hasil-uji.log. Kamu juga mau tahu berapa detik tesnya",
                    "jalan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua angka: kode keluar uji.sh di tahap pertama, dan kode",
                    "     keluar tee di tahap terakhir. $? cuma memberi yang terakhir.",
                    "  2. Salin PIPESTATUS tepat di baris sesudah pipeline, sebelum perintah",
                    "     lain sempat menimpanya:",
                    "      mulai=$SECONDS",
                    "      ./uji.sh | tee hasil-uji.log",
                    "      tahap=(\"${PIPESTATUS[@]}\")",
                    "      echo \"uji selesai dalam $(( SECONDS - mulai )) detik\"",
                    "      exit \"${tahap[0]}\"",
                    "  3. Sekarang script keluar dengan kode 1, sama dengan uji.sh, dan",
                    "     langkah CI ikut merah.",
                    "  4. Coba versi yang keliru: echo dulu, baru exit \"${PIPESTATUS[0]}\".",
                    "     Kode keluarnya 0, karena PIPESTATUS udah diisi ulang oleh echo.",
                    "",
                    "Ingat: kalau cukup tahu ada yang gagal tanpa perlu tahu tahap mana,",
                    "set -o pipefail udah cukup.",
                ]
            },
        ],
    },
    {
        "title": "25. Studi Kasus: Pengelola Catatan",
        "sections": [
            {
                "body": [
                    "Sekarang semua yang sudah kamu pelajari digabung jadi satu aplikasi",
                    "baris perintah (CLI) kecil, yaitu pengelola catatan sederhana.",
                    "",
                    "Fiturnya:",
                    "  - tambah <isi>: simpan catatan baru.",
                    "  - daftar: tampilkan semua catatan, lengkap dengan nomornya.",
                    "  - cari <kata>: cari catatan yang memuat kata itu.",
                    "  - hapus <nomor>: hapus catatan bernomor tertentu.",
                    "  - hitung: tampilkan jumlah catatan.",
                    "",
                    "Konsep yang dipakai: shebang, set -euo pipefail, fungsi, local, case,",
                    "perulangan while read, argumen $@, exit code, operasi string,",
                    "redirection, dan heredoc.",
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
                "heading": "Bagian menarik script dan ide lanjutan",
                "body": [
                    "Beberapa bagian script ini yang menarik untuk diperhatikan:",
                    "",
                    "  \"${CATATAN_FILE:-$HOME/.catatan.txt}\"",
                    "",
                    "Lokasi berkas catatannya bisa diubah lewat variabel lingkungan",
                    "CATATAN_FILE. Kalau variabel itu nggak diisi, yang dipakai",
                    "$HOME/.catatan.txt. Dengan begitu script ini gampang diuji tanpa",
                    "mengotori catatan asli.",
                    "",
                    "  \"${baris,,}\" == *\"${kata,,}\"*",
                    "",
                    "Dua-duanya diubah jadi huruf kecil dulu, lalu dicocokkan dengan",
                    "wildcard * (tanda bintang yang cocok dengan teks apa pun) di kiri dan",
                    "kanan. Hasilnya pencarian yang nggak membedakan huruf besar dan kecil,",
                    "tanpa memanggil grep.",
                    "",
                    "  shift || true",
                    "",
                    "shift membuang argumen pertama. Kalau nggak ada argumen, shift gagal,",
                    "dan set -e bakal menghentikan script. || true mencegah itu.",
                    "",
                    "  [[ ! \"$target\" =~ ^[0-9]+$ ]]",
                    "",
                    "Baris ini memastikan masukannya berupa angka sebelum dipakai di",
                    "perhitungan. Jangan pernah langsung percaya masukan dari pengguna.",
                    "",
                    "Latihan lanjutan yang bisa kamu coba sendiri:",
                    "  - Tambah perintah 'ubah <nomor> <isi baru>'.",
                    "  - Simpan tanggal pembuatan tiap catatan.",
                    "  - Tambah penanda selesai atau belum untuk tiap catatan.",
                    "  - Tulis pengujian otomatisnya dengan bats, alat untuk menguji script",
                    "    bash.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Alat baris perintah seperti git status atau dnf install memakai bentuk",
                    "nama-alat subperintah argumen. catatan.sh memakai bentuk yang sama,",
                    "jadi fitur baru cukup berupa satu fungsi dan satu cabang case, tanpa",
                    "mengusik subperintah lain.",
                    "",
                    "Kasus kecil: salah satu latihan lanjutan di materi ini, perintah",
                    "ubah <nomor> <isi baru>. Catatan nomor 1, beli gula, mau diganti jadi",
                    "beli gula 1/2 kg & telur.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya nomor dan isi baru. Periksa nomornya dengan cara yang",
                    "     sama seperti di hapus(): harus angka, dan ada di antara 1 sampai",
                    "     jumlah baris.",
                    "  2. Godaannya sed -i \"${target}s/.*/$baru/\". Dengan isi tadi, sed",
                    "     menolak dengan pesan unknown option to s, karena garis miring di",
                    "     1/2 dibaca sebagai pemisah perintah sed. Tanda & juga diganti sed",
                    "     dengan teks lama, tanpa pesan apa pun.",
                    "  3. Pakai cara yang nggak menafsirkan isi sama sekali. Tulis ulang",
                    "     berkasnya baris demi baris ke $tmp hasil mktemp, lalu timpa:",
                    "      n=0",
                    "      while IFS= read -r baris; do",
                    "          n=$((n + 1))",
                    "          (( n == target )) && baris=\"$baru\"",
                    "          printf '%s\\n' \"$baris\"",
                    "      done < \"$BERKAS\" > \"$tmp\" && mv \"$tmp\" \"$BERKAS\"",
                    "  4. Uji isi yang memuat / dan &, hasilnya harus tersimpan apa adanya.",
                    "     Uji juga nomor 0 dan nomor yang melebihi jumlah catatan. Dua-duanya",
                    "     harus ditolak sebelum berkas disentuh.",
                ]
            },
        ],
    },
]
