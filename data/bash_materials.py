BASH_MATERIALS = [
    {
        "title": "1. Pengenalan Shell & Bash",
        "sections": [
            {
                "body": [
                    "Apa itu shell?",
                    "  - Program yang menerjemahkan perintah teks jadi aksi sistem.",
                    "  - Jembatan antara kamu dan kernel sistem operasi.",
                    "  - Contoh shell: sh, bash, zsh, fish, dash, ksh.",
                    "",
                    "Bash = Bourne Again SHell.",
                    "  - Shell default di kebanyakan distro Linux dan WSL.",
                    "  - Dibuat Brian Fox tahun 1989 sebagai pengganti bebas dari sh.",
                    "  - macOS sekarang default-nya zsh, tapi bash tetap tersedia.",
                    "",
                    "Kenapa belajar Bash?",
                    "  - Otomatisasi tugas berulang: backup, deploy, konversi file.",
                    "  - Wajib untuk kerja di server, Docker, dan CI/CD.",
                    "  - Sudah terpasang di mana-mana, tidak perlu install apa pun.",
                    "",
                    "Cek versi bash kamu:",
                    "  bash --version",
                    "",
                    "Dua cara memakai bash:",
                    "  1. Interaktif  - ketik perintah satu per satu di terminal.",
                    "  2. Script      - kumpulan perintah disimpan di file .sh.",
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
                    "Penjelasan baris demi baris:",
                    "",
                    "  #!/usr/bin/env bash",
                    "    Disebut SHEBANG. Memberi tahu sistem: jalankan file ini",
                    "    dengan bash. Harus di BARIS PERTAMA, tanpa spasi di depan.",
                    "    Bentuk lain: #!/bin/bash",
                    "    Versi env lebih portabel karena mencari bash di PATH.",
                    "",
                    "  echo \"...\"",
                    "    Perintah untuk menampilkan teks ke layar.",
                    "",
                    "Cara menjalankan (ada 2):",
                    "  A. bash program.sh",
                    "       Paling gampang, tidak perlu izin eksekusi.",
                    "  B. chmod +x program.sh   lalu   ./program.sh",
                    "       chmod +x memberi izin 'boleh dieksekusi'.",
                    "       ./ berarti 'file di folder saat ini'.",
                    "",
                    "Komentar ditulis dengan tanda pagar:",
                    "  # ini komentar, diabaikan bash",
                    "",
                    "Bash TIDAK punya komentar multi-baris resmi. Pakai # tiap baris.",
                    "",
                    "Satu baris, beberapa perintah: pisahkan dengan titik koma.",
                    "  mkdir catatan ; cd catatan",
                    "  Keduanya dijalankan berurutan, apa pun hasil yang pertama.",
                    "",
                    "Satu perintah, beberapa baris: backslash di UJUNG baris",
                    "menyambungnya ke baris berikutnya.",
                    "",
                    "  cp -r \\",
                    "      laporan/ \\",
                    "      cadangan/",
                    "",
                    "  Bash membacanya sebagai satu perintah utuh. Dipakai supaya",
                    "  perintah panjang - curl dengan sepuluh opsi, docker run yang",
                    "  penuh flag - tetap enak dibaca dan enak di-diff.",
                    "",
                    "  JEBAKAN: backslash harus jadi karakter PALING akhir di baris",
                    "  itu. Satu spasi tersembunyi sesudahnya membatalkan sambungan:",
                    "  bash menganggap perintahnya sudah selesai di situ, lalu",
                    "  mengeluh soal argumen yang kurang atau menjalankan baris",
                    "  berikutnya sebagai perintah tersendiri. Spasi itu tidak",
                    "  kelihatan di layar, jadi ingat-ingat gejalanya.",
                ]
            },
        ],
    },
    {
        "title": "2. Izin Berkas & Hak Akses",
        "sections": [
            {
                "body": [
                    "Sejak perintah pertama kamu sudah melihat baris seperti ini, dan mungkin",
                    "melewatinya begitu saja:",
                    "",
                    "  $ ls -l",
                    "  -rw-r--r--  1 andi tim   142 Jan  5 09:11 catatan.txt",
                    "  -rwxr-xr-x  1 andi tim    59 Jan  5 09:12 sapa.sh",
                    "  drwxr-xr-x  2 andi tim  4096 Jan  5 09:12 arsip",
                    "",
                    "Kolom pertama itu bukan sandi rahasia. Sepuluh karakter, dibaca dari kiri:",
                    "",
                    "  -  rwx  r-x  r-x",
                    "  ^   ^    ^    ^",
                    "  |   |    |    +--- LAINNYA (other): siapa pun lagi di mesin ini",
                    "  |   |    +-------- GRUP (group): anggota grup pemilik berkas",
                    "  |   +------------- PEMILIK (user): akun yang memiliki berkas",
                    "  +----------------- jenis: - berkas biasa, d folder, l symlink",
                    "",
                    "Nama pemilik dan grupnya ada di kolom 3 dan 4 (andi dan tim di contoh atas).",
                    "",
                    "Tiga huruf di tiap golongan urutannya selalu r, w, x. Tanda - berarti mati.",
                    "",
                    "Arti r, w, x untuk BERKAS:",
                    "  r  boleh dibaca isinya (cat, grep, cp, editor)",
                    "  w  boleh diubah isinya",
                    "  x  boleh dijalankan sebagai program",
                    "",
                    "Arti yang sama untuk FOLDER, dan di sinilah orang paling sering salah paham:",
                    "  r  boleh melihat DAFTAR NAMA di dalamnya (ls)",
                    "  x  boleh MASUK dan menyentuh isinya (cd, membuka berkas di dalamnya)",
                    "  w  boleh menambah, mengganti nama, dan MENGHAPUS berkas di dalamnya",
                    "",
                    "Dari situ muncul dua hal yang kelihatan aneh tapi memang begitu aturannya:",
                    "  - Folder r tanpa x: nama berkasnya kelihatan, isinya tidak bisa dibuka.",
                    "  - Folder x tanpa r: daftarnya tidak bisa dilihat, tapi berkas yang namanya",
                    "    sudah kamu tahu tetap bisa dibuka.",
                    "",
                    "Untuk melihat izin FOLDER-nya sendiri, bukan izin isinya, pakai ls -ld:",
                    "  ls -ld arsip",
                    "",
                    "Perintah stat menampilkan hal yang sama dengan lebih ringkas:",
                    "  stat -c '%a %A %n' arsip",
                    "  (stat itu perintah GNU/Linux; di macOS opsinya beda, tapi ls -l sama saja",
                    "  di mana-mana.)",
                    "",
                    "TIGA JEBAKAN yang tidak ketahuan sampai kamu tertimpa sendiri:",
                    "",
                    "1. Golongan yang dipakai adalah yang PERTAMA cocok, bukan yang paling murah",
                    "   hati. Berkas milikmu ber-izin ----rwxrwx (77) tidak bisa KAMU baca, walau",
                    "   seisi mesin boleh. Kamu pemiliknya, jadi cuma tiga huruf pertama berlaku.",
                    "",
                    "2. Izin MENGHAPUS berkas ada di FOLDERNYA, bukan di berkas itu sendiri.",
                    "   Berkas ber-izin r-------- pun tetap terhapus kalau kamu boleh menulis di",
                    "   foldernya. rm cuma bertanya 'remove write-protected regular file?' lalu",
                    "   menurut begitu kamu jawab y.",
                    "",
                    "3. Bit x pada berkas cuma soal 'boleh dijalankan langsung'. Tanpa x, kamu",
                    "   masih bisa menjalankannya lewat 'bash sapa.sh', karena yang dijalankan",
                    "   adalah bash, dan bash cuma perlu MEMBACA berkasnya. Ini menjelaskan dua",
                    "   cara menjalankan script yang disebut di materi Pengenalan Shell & Bash.",
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
                    "Menulis sembilan huruf rwx setiap kali melelahkan, jadi ada bentuk ANGKA.",
                    "Tiap bit punya nilai:",
                    "",
                    "  r = 4      w = 2      x = 1",
                    "",
                    "Jumlahkan yang menyala, satu angka per golongan. Kemungkinannya cuma delapan:",
                    "",
                    "  0  ---  tidak boleh apa-apa       4  r--  baca saja",
                    "  1  --x  eksekusi saja             5  r-x  baca + eksekusi",
                    "  2  -w-  tulis saja                6  rw-  baca + tulis",
                    "  3  -wx  tulis + eksekusi          7  rwx  semuanya",
                    "",
                    "Tiga angka berurutan: pemilik, grup, lainnya. Yang lazim cuma segelintir:",
                    "",
                    "  755 = rwx r-x r-x   script & folder umum: semua boleh pakai, cuma pemilik ubah",
                    "  644 = rw- r-- r--   berkas biasa: semua boleh baca, cuma pemilik boleh ubah",
                    "  700 = rwx --- ---   folder pribadi: orang lain tidak bisa masuk sama sekali",
                    "  600 = rw- --- ---   berkas rahasia: cuma pemilik yang boleh membacanya",
                    "",
                    "Membacanya tinggal dibalik: r-x itu 4 + 0 + 1 = 5.",
                    "",
                    "Bentuk SIMBOLIK tidak menyebut angka, tapi siapa dan operasinya:",
                    "",
                    "  siapa    : u pemilik, g grup, o lainnya, a semua",
                    "  operasi  : + tambah, - cabut, = pasang persis (sisanya dimatikan)",
                    "",
                    "  chmod u+x sapa.sh      nyalakan x untuk pemilik saja",
                    "  chmod go-r rahasia     cabut r dari grup dan lainnya",
                    "  chmod a+r bacaan.txt   semua orang boleh baca",
                    "  chmod u=rw,go= data    pemilik rw, grup dan lainnya kosong (= 600)",
                    "",
                    "Kapan pakai yang mana:",
                    "  - ANGKA kalau kamu ingin memastikan KEADAAN AKHIR. 644 selalu berarti 644,",
                    "    tidak peduli izin sebelumnya apa. Ini yang dipakai di dalam script.",
                    "  - SIMBOLIK kalau kamu cuma mau mengubah SATU bit dan membiarkan sisanya.",
                    "",
                    "JEBAKAN: chmod +x tanpa menyebut siapa BUKAN sama dengan chmod a+x. Kalau",
                    "'siapa' dihilangkan, chmod menyaringnya dengan umask kamu:",
                    "",
                    "  umask 022, berkas 644  ->  chmod +x  ->  755",
                    "  umask 077, berkas 644  ->  chmod +x  ->  744   (grup & lainnya tidak kebagian)",
                    "",
                    "Script yang di mesinmu jalan lalu di mesin lain 'Permission denied' sering",
                    "lahir dari sini. Kalau memang mau semua orang bisa menjalankan, tulis",
                    "chmod a+x atau chmod 755 -- jangan bergantung pada umask yang kebetulan pas.",
                ],
            },
            {
                "heading": "umask, berkas rahasia, dan cek root",
                "body": [
                    "Izin sebuah berkas baru tidak muncul dari udara. Ada saringan bernama umask.",
                    "",
                    "  Berkas baru berangkat dari 666 (rw-rw-rw-), folder baru dari 777 (rwxrwxrwx).",
                    "  Bit yang tercantum di umask lalu DIMATIKAN.",
                    "  Berkas tidak pernah lahir dengan bit x -- itu sebabnya script baru selalu",
                    "  perlu satu kali chmod +x sebelum bisa dipanggil dengan ./",
                    "",
                    "  umask         lihat nilai sekarang, misalnya 0022",
                    "  umask 077     ubah, berlaku sampai shell ditutup",
                    "",
                    "HATI-HATI: umask itu operasi BIT, bukan pengurangan. Untuk 022 hasilnya",
                    "kebetulan sama (666 - 022 = 644), jadi orang mengira rumusnya pengurangan.",
                    "Untuk umask 023 hasilnya 644, bukan 643. Ingat cara kerjanya, bukan rumus",
                    "pengurangannya.",
                    "",
                    "Baris if [[ ... ]] di contoh berikut dibahas tuntas di materi Percabangan.",
                    "Untuk sekarang baca saja sebagai 'kalau ... maka ...'.",
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
                    "Kenapa 600 bukan sekadar saran: ssh MENOLAK jalan kalau kunci privatmu",
                    "terlalu longgar. Pakai kunci berizin 644 dan yang muncul adalah ini:",
                    "",
                    "  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                    "  @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @",
                    "  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                    "  Permissions 0644 for 'id_ed25519' are too open.",
                    "  This private key will be ignored.",
                    "  git@github.com: Permission denied (publickey).",
                    "",
                    "Perhatikan baris terakhirnya: yang tersisa cuma 'Permission denied', persis",
                    "seperti kuncinya salah atau belum didaftarkan. Orang bisa habis berjam-jam",
                    "membuat ulang kunci padahal obatnya dua perintah:",
                    "",
                    "  chmod 700 ~/.ssh",
                    "  chmod 600 ~/.ssh/id_ed25519",
                    "",
                    "Aturan yang sama berlaku untuk berkas .env, token API, dan konfigurasi",
                    "berisi password. Bukan karena tetangga akan mengintip, tapi karena program",
                    "lain memang menolak memakai berkas rahasia yang bisa dibaca umum.",
                    "",
                    "sudo menjalankan SATU perintah sebagai pengguna lain -- bawaannya root:",
                    "",
                    "  sudo dnf install git       jalankan perintah itu sebagai root",
                    "  sudo -u postgres psql      jalankan sebagai pengguna postgres",
                    "  sudo -i                    buka shell root sampai kamu ketik exit",
                    "",
                    "Root menembus semua bit rwx tanpa kecuali; tidak ada berkas yang bisa",
                    "menolaknya. Itu sebabnya menjalankan script asing sebagai root -- terutama",
                    "pola 'curl <alamat> | sudo bash' -- sama dengan menyerahkan seluruh mesin ke",
                    "penulis script itu tanpa sempat kamu baca satu baris pun. Unduh dulu ke",
                    "berkas, baca isinya, baru jalankan; dan tanpa sudo kalau memang tidak perlu.",
                    "",
                    "chown dan chgrp mengubah SIAPA pemiliknya, bukan izinnya:",
                    "",
                    "  sudo chown andi berkas.txt       ganti pemilik",
                    "  sudo chown andi:tim berkas.txt   ganti pemilik dan grup sekaligus",
                    "  sudo chgrp tim berkas.txt        ganti grup saja",
                    "  sudo chown -R andi:tim folder/   -R = seluruh isi folder ikut",
                    "",
                    "Menyerahkan berkas ke orang lain hampir selalu butuh root, jadi kalau kamu",
                    "kena 'Operation not permitted' di chown, itu memang aturannya, bukan bug.",
                    "",
                    "JEBAKAN yang paling banyak memakan waktu orang:",
                    "",
                    "  $ sudo echo '127.0.0.1 lokal' > /etc/hosts",
                    "  bash: /etc/hosts: Permission denied",
                    "",
                    "Sudah pakai sudo, kenapa masih ditolak? Karena tanda > dikerjakan oleh",
                    "SHELL-mu, sebelum sudo sempat jalan sama sekali. Yang naik jadi root cuma",
                    "echo; berkasnya terlanjur dibuka atas namamu, dan gagal di situ. Jalan",
                    "keluarnya dibahas di materi Aliran Data & Deskriptor.",
                    "",
                    "Sisa jebakan yang layak diingat:",
                    "  - chmod -R 777 supaya 'kelar dulu' berarti siapa pun boleh menulis ulang",
                    "    programmu. Di folder web itu setara mengundang orang menaruh kodenya.",
                    "  - 777 hampir tidak pernah jawaban yang benar. Cari golongan mana yang",
                    "    sebenarnya kurang, lalu berikan itu saja.",
                    "  - cp tanpa -p membuat salinan dengan izin BARU yang disaring umask, bukan",
                    "    izin aslinya. Salinan dari berkas 755 bisa mendarat jadi 700.",
                    "  - Cek root satu baris, lazim di kepala script:",
                    "      [[ $EUID -ne 0 ]] && { echo \"jalankan sebagai root\" >&2; exit 1; }",
                    "    Bentuk yang lebih portabel: [[ \"$(id -u)\" -ne 0 ]] -- $EUID itu fitur",
                    "    bash, sedangkan id -u ada di semua shell.",
                ],
            },
        ],
    },
    {
        "title": "3. Variabel & Quoting",
        "sections": [
            {
                "body": [
                    "Membuat variabel:",
                    "  nama=\"Andi\"",
                    "",
                    "ATURAN PALING SERING BIKIN ERROR:",
                    "  TIDAK BOLEH ada spasi di sekitar tanda sama dengan.",
                    "    nama=\"Andi\"     BENAR",
                    "    nama = \"Andi\"   SALAH -> bash mengira 'nama' adalah perintah",
                    "",
                    "Membaca variabel pakai tanda dolar:",
                    "  echo $nama",
                    "  echo ${nama}     <- bentuk aman, dipakai kalau menempel teks lain",
                    "",
                    "Kenapa ${} penting:",
                    "  echo \"$namaku\"    -> bash cari variabel bernama 'namaku'",
                    "  echo \"${nama}ku\"  -> bash cari 'nama', lalu tempel 'ku'",
                    "",
                    "Bash tidak punya tipe data. Semua nilai pada dasarnya STRING.",
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
                    "Ringkasan quoting:",
                    "",
                    "  \"petik ganda\"  -> variabel & $(...) diproses. INI YANG UMUM.",
                    "  'petik tunggal' -> semua literal, tidak ada yang diproses.",
                    "  $(perintah)     -> command substitution, ambil output perintah.",
                    "  $'...'          -> ANSI-C quoting: \\n, \\t, \\e jadi karakter ASLI.",
                    "",
                    "Bentuk keempat itu paling gampang salah dibaca, justru oleh orang",
                    "yang sudah hafal 'petik tunggal berarti apa adanya'. Tanda dolar di",
                    "depannya membalik aturan itu KHUSUS untuk escape:",
                    "",
                    "  echo 'a\\nb'    -> a\\nb       petik tunggal biasa, apa adanya",
                    "  echo $'a\\nb'   -> a          lalu b di baris berikutnya",
                    "",
                    "Dipakai kalau kamu butuh tab atau baris baru sebagai NILAI sebuah",
                    "variabel, bukan sebagai teks yang kebetulan berisi backslash:",
                    "  pemisah=$'\\t'          satu karakter tab sungguhan",
                    "  printf $'\\e[31m'       \\e = karakter escape, ini awalan kode warna",
                    "",
                    "ATURAN EMAS: selalu bungkus variabel dengan petik ganda.",
                    "  file=\"laporan akhir.txt\"",
                    "  rm $file      -> SALAH, dibaca sebagai 2 file: 'laporan' & 'akhir.txt'",
                    "  rm \"$file\"    -> BENAR, dibaca sebagai 1 nama file",
                    "",
                    "Variabel khusus bawaan:",
                    "  $0    nama script",
                    "  $1..$9  argumen ke-1 sampai ke-9",
                    "  $#    jumlah argumen",
                    "  $@    semua argumen (sebagai daftar terpisah)",
                    "  $?    kode keluar perintah terakhir (0 = sukses)",
                    "  $$    process ID script ini",
                    "",
                    "Variabel lingkungan (environment):",
                    "  echo $HOME $USER $PATH",
                    "  export API_KEY=\"rahasia\"   # supaya diwariskan ke proses anak",
                ]
            },
            {
                "heading": "$( ) membuka konteks kutip BARU",
                "body": [
                    "Aturan yang menyelamatkan banyak jam: apa pun di dalam $( ) dibaca",
                    "dari nol. Petik ganda di dalamnya TIDAK menutup petik ganda di",
                    "luarnya - keduanya tidak saling kenal.",
                    "",
                    "  echo \"Total: $(wc -l < \"$BERKAS\") baris\"",
                    "",
                    "Petik di sekitar $BERKAS itu BENAR dan memang harus ada. Sekilas",
                    "bagian \"Total: $(wc -l < \" kelihatan sudah menutup petiknya, lalu",
                    "orang menghapus petik yang di dalam supaya 'rapi'. Yang hilang",
                    "justru perlindungan untuk nama berkas berspasi - persis aturan emas",
                    "yang baru saja dilatih di atas.",
                    "",
                    "Aturan yang sama berlaku bertingkat: $( ) di dalam $( ) juga membuka",
                    "konteksnya sendiri lagi.",
                    "",
                    "Satu keterangan untuk contoh $(date +%Y) tadi. Tanda + di situ bukan",
                    "opsi dan bukan bagian nama perintahnya, melainkan penanda bahwa",
                    "sisanya adalah string FORMAT: %Y berarti tahun empat digit. Daftar",
                    "lengkap formatnya ada di materi Alat Pendamping: curl, jq, date, tar.",
                ]
            },
            {
                "heading": "IFS dan awalan variabel sekali pakai",
                "body": [
                    "IFS bukan mantra milik perintah tertentu. Ia variabel biasa yang",
                    "isinya DAFTAR KARAKTER pemisah kata. Bawaannya spasi, tab, dan",
                    "baris baru - itulah kenapa bash memecah kata di spasi.",
                    "",
                    "  IFS=','    -> yang dianggap pemisah tinggal koma",
                    "  IFS=       -> daftarnya KOSONG, tidak ada yang dipecah sama sekali",
                    "",
                    "Dua bentuk itu kelihatan berlawanan, dan memang berlawanan: yang",
                    "pertama MENGGANTI daftar pemisah, yang kedua MENGOSONGKANNYA. Nanti",
                    "kamu akan bertemu keduanya di tempat berbeda; yang membedakan cuma",
                    "ada tidaknya isi di kanan tanda sama dengan.",
                    "",
                    "AWALAN VARIABEL. Kalau penugasan ditulis di DEPAN sebuah perintah,",
                    "variabel itu hidup hanya selama perintah itu berjalan:",
                    "",
                    "  LC_ALL=C sort daftar.txt     sort diurut aturan C, shell tak berubah",
                    "  DEBUG=1 ./app.sh             app melihat DEBUG=1, terminalmu tidak",
                    "  IFS=',' read -ra bagian      IFS koma cuma untuk read yang ini",
                    "",
                    "Begitu perintahnya selesai, nilai lama kembali sendiri - tidak perlu",
                    "dipulihkan. Ini alasan bentuk IFS=',' read ... aman ditaruh di tengah",
                    "script tanpa merusak apa pun sesudahnya.",
                    "",
                    "Kalau IFS harus berubah untuk BEBERAPA perintah sekaligus, awalan",
                    "tidak bisa dipakai. Simpan dan pulihkan sendiri:",
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
                    "Menampilkan output:",
                    "  echo \"teks\"           paling umum",
                    "  echo -n \"teks\"        tanpa pindah baris di akhir",
                    "  echo -e \"a\\tb\"        aktifkan escape seperti \\t dan \\n",
                    "  printf \"%s\\n\" \"teks\"  lebih presisi, mirip C",
                    "",
                    "printf lebih bisa diandalkan daripada echo -e karena",
                    "perilakunya sama di semua shell.",
                    "",
                    "Format printf yang sering dipakai:",
                    "  %s    string",
                    "  %d    bilangan bulat",
                    "  %.2f  desimal 2 angka di belakang koma",
                    "  \\n    baris baru",
                    "  \\t    tab",
                    "",
                    "Angka di antara % dan hurufnya mengatur LEBAR kolom:",
                    "  %5d    lebar 5, rata KANAN            ->  '   42'",
                    "  %-5d   tanda minus = rata KIRI        ->  '42   '",
                    "  %-25s  teks rata kiri selebar 25 kolom",
                    "  %03d   lebar 3, sisanya diisi NOL     ->  '007'",
                    "",
                    "Isi yang lebih panjang dari lebar yang diminta tidak dipotong;",
                    "kolomnya yang melar. Jadi lebar itu jaminan MINIMAL, bukan batas.",
                    "",
                    "Inilah cara membuat tabel yang lurus tanpa menghitung spasi sendiri:",
                    "  printf \"%-10s %5d\\n\" \"apel\" 12",
                    "  printf \"%-10s %5d\\n\" \"semangka\" 3",
                    "",
                    "  apel          12",
                    "  semangka       3",
                    "",
                    "Kalau jumlah spasinya dihitung manual, satu huruf tambahan pada nama",
                    "sudah cukup untuk merusak seluruh kolom.",
                ]
            },
            {
                "heading": "printf mengulang formatnya sampai argumen habis",
                "body": [
                    "Ini beda printf yang paling sering bikin heran. Kalau argumennya",
                    "LEBIH BANYAK daripada spesifier %, printf tidak membuang sisanya.",
                    "Ia memakai formatnya lagi dari awal sampai semua argumen terpakai.",
                    "",
                    "  printf '%s\\n' apel jeruk mangga",
                    "",
                    "Satu %s, tiga argumen -> tiga baris, bukan cuma 'apel'. Karena itu",
                    "printf '%s\\n' adalah cara baku mencetak daftar apa pun satu per",
                    "baris, termasuk seluruh isi array nanti.",
                    "",
                    "Kalau formatnya punya dua spesifier, argumennya diambil dua-dua tiap",
                    "putaran - satu putaran jadi satu baris tabel.",
                    "",
                    "Kalau argumennya justru KURANG, yang kosong dianggap string kosong",
                    "atau angka 0, dan printf tidak mengeluh.",
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
                    "Dua bentuk di contoh tadi belum waktunya dijelaskan, jadi jangan",
                    "dicari-cari - keduanya dibahas utuh nanti:",
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
                    "Redirection (mengalihkan input/output):",
                    "  perintah > file     tulis output ke file (TIMPA isi lama)",
                    "  perintah >> file    tambahkan output ke akhir file",
                    "  perintah < file     ambil input dari file",
                    "  perintah 2> file    alihkan pesan error saja",
                    "  perintah &> file    alihkan output DAN error",
                    "  perintah > /dev/null  buang output (tempat sampah sistem)",
                    "",
                    "Pipe menyambung output satu perintah jadi input perintah lain:",
                    "  cat data.txt | grep \"error\" | wc -l",
                    "  Artinya: baca file -> saring baris ber-'error' -> hitung barisnya.",
                ]
            },
        ],
    },
    {
        "title": "5. Aliran Data & Deskriptor",
        "sections": [
            {
                "body": [
                    "Setiap perintah yang jalan di Linux lahir dengan tiga saluran sudah terbuka.",
                    "Ini bukan fitur bash, melainkan aturan sistem operasinya - berlaku juga untuk",
                    "python, java, curl, dan program apa pun yang kamu panggil dari script.",
                    "",
                    "  Nomor  Nama     Arah     Isinya",
                    "  0      stdin    masuk    data yang dibaca perintah",
                    "  1      stdout   keluar   hasil kerja yang sebenarnya",
                    "  2      stderr   keluar   pesan error dan peringatan",
                    "",
                    "Angka itu namanya FILE DESCRIPTOR, kita sebut saja DESKRIPTOR. Kernel tidak",
                    "mengenal kata 'stdout'; yang ia pegang cuma angka 1.",
                    "",
                    "Kenapa keluaran dipecah jadi dua jalur? Supaya hasil bisa disaring lewat pipe",
                    "tanpa kemasukan pesan error. Itu alasan di balik echo \"...\" >&2 yang dipakai",
                    "di materi Argumen & Exit Code.",
                    "",
                    "Redirection yang sudah kamu kenal sebenarnya cuma bentuk singkat:",
                    "",
                    "  perintah > berkas     sama saja dengan   perintah 1> berkas",
                    "  perintah < berkas     sama saja dengan   perintah 0< berkas",
                    "  perintah 2> berkas    alihkan stderr saja, hasil tetap ke layar",
                    "",
                    "Angka 1 dan 0 boleh dihilangkan karena itu yang paling sering dipakai. Angka 2",
                    "tidak punya bentuk singkat - memang harus ditulis.",
                    "",
                    "CARA MEMBACA N>&M",
                    "  'Sambungkan deskriptor N ke tempat yang SEKARANG ditunjuk deskriptor M.'",
                    "  Tanda & di situ berarti: yang berikut ini NOMOR deskriptor, bukan nama berkas.",
                    "",
                    "  2>&1    stderr ikut ke mana pun stdout sedang mengarah",
                    "  2>1     SALAH - membuat berkas bernama 1, lalu menaruh pesan error di dalamnya",
                    "",
                    "Salah ketik 2>1 tidak memberi peringatan apa pun. Script tetap jalan, pesan",
                    "errornya raib, dan di folder muncul berkas aneh bernama 1. Kalau kamu pernah",
                    "melihat berkas bernama 1 nangkring di server, sekarang kamu tahu asalnya.",
                    "",
                    "JEBAKAN URUTAN",
                    "  Redirection dikerjakan dari KIRI ke KANAN, dan 2>&1 menyalin tujuan stdout",
                    "  SAAT ITU JUGA - bukan tujuan stdout yang belakangan.",
                    "",
                    "  perintah >catatan.log 2>&1",
                    "    1 dipindah ke berkas, baru 2 menyusul ke tempat yang sama.",
                    "    Dua-duanya masuk berkas. Ini yang biasanya kamu maksud.",
                    "",
                    "  perintah 2>&1 >catatan.log",
                    "    2 disambungkan ke LAYAR (tempat 1 masih menunjuk waktu itu), baru",
                    "    sesudahnya 1 pindah ke berkas. Error tetap tumpah ke layar.",
                    "    Bug klasik: lognya kelihatan bersih padahal errornya cuma tidak tercatat.",
                    "",
                    "Satu catatan sebelum mencoba contoh di bawah: keluaran stderr ditampilkan di",
                    "panel terpisah dari keluaran biasa, jadi urutan barisnya bisa terlihat berbeda",
                    "dari di terminal. Itu bukan tanda gagal - justru itu buktinya: dua aliran,",
                    "dua tempat penampungan.",
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
                    "Idiom yang paling sering muncul di script orang lain:",
                    "",
                    "  perintah >/dev/null 2>&1    diamkan semuanya, hasil maupun error",
                    "  perintah 2>/dev/null        diamkan errornya saja, hasil tetap terlihat",
                    "",
                    "/dev/null berkas khusus yang menelan apa pun yang ditulis ke sana. Bentuk",
                    "pendek &>/dev/null dari materi Input & Output hasilnya sama persis, tapi &>",
                    "cuma dimengerti bash dan zsh. Kalau baris pertama scriptmu #!/bin/sh, tulis",
                    ">/dev/null 2>&1 - itu yang jalan di mana pun.",
                    "",
                    "exec TANPA nama perintah: mengalihkan aliran SCRIPT ITU SENDIRI, permanen",
                    "sampai script selesai.",
                    "",
                    "  exec >>\"$LOG\" 2>&1",
                    "    Ditaruh di kepala script. Sesudah baris ini semua echo, semua pesan",
                    "    error, dan keluaran semua perintah yang dipanggil masuk ke $LOG.",
                    "    Tanpa ini kamu harus menempelkan >>\"$LOG\" 2>&1 di tiap baris - dan",
                    "    satu baris yang kelupaan sudah cukup membuat log tidak lengkap.",
                    "",
                    "Setelah exec >>\"$LOG\", layar tidak bisa dipanggil balik begitu saja. Kalau",
                    "masih butuh, SIMPAN dulu tujuan lamanya di deskriptor cadangan:",
                    "",
                    "  exec 4>&1        salin tujuan stdout sekarang ke deskriptor 4",
                    "  exec >&4         kembalikan stdout ke tempat yang tadi disimpan",
                    "  exec 4>&-        tutup deskriptor 4, tanda minus artinya 'tutup'",
                    "",
                    "Deskriptor 3 ke atas bebas kamu pakai; 0, 1, dan 2 sudah ada pemiliknya.",
                    "  exec 3<data.txt   buka data.txt untuk dibaca lewat deskriptor 3",
                    "  read -r baris <&3 baca satu baris dari deskriptor 3, bukan dari stdin",
                    "  exec 3<&-         tutup lagi",
                    "",
                    "Gunanya: perulangan yang membaca berkas tapi di dalamnya masih perlu",
                    "bertanya ke pengguna. Kalau berkasnya disambungkan ke stdin biasa, read",
                    "yang di dalam loop akan ikut memakan baris berkas, bukan jawaban orangnya.",
                    "",
                    "exec DENGAN nama perintah artinya lain lagi: script MENGGANTI DIRINYA",
                    "dengan perintah itu - proses yang sama, PID yang sama, tidak ada proses anak.",
                    "",
                    "  exec \"$@\"",
                    "    Baris penutup entrypoint.sh di hampir semua image Docker. Script",
                    "    menyiapkan konfigurasi, lalu lenyap dan digantikan aplikasi aslinya.",
                    "    Karena PID-nya tidak berubah, sinyal stop dari Docker sampai ke",
                    "    aplikasi, bukan tersangkut di script pembungkus.",
                    "",
                    "tee membelah satu keluaran jadi dua tujuan: layar DAN berkas.",
                    "  perintah | tee catatan.log      timpa isi lama",
                    "  perintah | tee -a catatan.log   tambahkan di belakang (append)",
                    "",
                    "tee juga jalan keluar dari jebakan izin berkas: pada sudo perintah > /etc/x,",
                    "yang dijalankan sebagai root cuma 'perintah', sedangkan pengalihan > dikerjakan",
                    "shell-mu yang biasa sehingga tetap ditolak. Yang benar:",
                    "  echo \"isi baru\" | sudo tee /etc/contoh.conf >/dev/null",
                    "  Di sini tee-lah yang jalan sebagai root, jadi ia berhak menulis.",
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
                    "Tiga pintasan yang sudah dipakai diam-diam di materi lain, sekarang jelas",
                    "asalnya.",
                    "",
                    "1. HERE-STRING <<<  memberi SATU string sebagai stdin sebuah perintah.",
                    "     read -ra bagian <<< \"$teks\"   pecah string jadi array",
                    "     grep -q pola <<< \"$teks\"      periksa isi string tanpa berkas sementara",
                    "     jq . <<< \"$json\"              suapkan JSON yang sudah ada di variabel",
                    "   Tanpa ini kamu harus menulis echo \"$teks\" | read ... yang justru TIDAK",
                    "   jalan: sisi kanan pipe dijalankan di proses terpisah, jadi variabel yang",
                    "   diisi read di sana ikut lenyap begitu pipe selesai. <<< tidak membuat",
                    "   proses baru, makanya variabelnya bertahan.",
                    "   Catatan kecil: <<< menambahkan satu baris baru di ujung string.",
                    "",
                    "   Bedanya dengan heredoc << (dibahas di materi grep, sed, dan awk):",
                    "     <<< 'satu string', ditulis di baris yang sama",
                    "     <<  blok banyak baris, ditutup penanda tersendiri seperti EOF",
                    "",
                    "2. isi=$(<berkas.txt)  membaca seluruh isi berkas ke variabel.",
                    "   Sama hasilnya dengan $(cat berkas.txt) tapi tanpa menjalankan program",
                    "   cat sama sekali - bash membacanya sendiri. Keduanya membuang baris baru",
                    "   di ujung berkas, jadi jangan kaget kalau panjangnya berkurang.",
                    "",
                    "3. PERINTAH KOSONG :  tidak mengerjakan apa pun dan SELALU sukses (exit 0).",
                    "     : > berkas            kosongkan berkas; yang bekerja tanda >, bukan :",
                    "     while :; do           sama saja dengan while true, cuma lebih pendek",
                    "     : \"${VAR:?wajib diisi}\"  hentikan script kalau VAR kosong",
                    "",
                    "   Baris ketiga itu trik yang enak: ${VAR:?pesan} sudah bisa menghentikan",
                    "   script sendiri, tapi ia harus jadi bagian dari sebuah perintah. Ditulis",
                    "   sendirian, nilainya akan dicoba dijalankan sebagai perintah. Di depan",
                    "   diberi : supaya ada perintah yang tidak melakukan apa-apa - jadi yang",
                    "   tersisa cuma pemeriksaannya. Pesannya muncul begini lalu script berhenti:",
                    "     coba.sh: line 4: VAR: wajib diisi        (lalu keluar dengan kode 1)",
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
                    "Tiga cara menjalankan berkas .sh, dan ketiganya BERBEDA akibatnya:",
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
                    "Apa itu proses anak?",
                    "  Saat shell menjalankan sebuah program, ia membuat proses BARU",
                    "  lalu menyerahkan pekerjaan ke proses itu. Nomor proses inilah",
                    "  yang kamu lihat lewat $$ di materi Variabel & Quoting.",
                    "  Proses anak mewarisi bekal dari induknya, tapi hidupnya",
                    "  sendiri. Begitu ia selesai, semua yang ia ubah ikut lenyap",
                    "  bersama prosesnya.",
                    "",
                    "Akibatnya, dan ini yang paling sering bikin orang bingung:",
                    "  - cd di dalam ./x.sh TIDAK memindahkan folder terminalmu. Yang",
                    "    pindah adalah proses anak, dan proses itu sudah mati begitu",
                    "    script selesai.",
                    "  - Variabel yang dibuat di dalam ./x.sh tidak ada lagi setelah",
                    "    script usai.",
                    "  - Karena itu perintah semacam 'aktifkan virtualenv' atau 'muat",
                    "    ulang konfigurasi' SELALU dipakai dengan source. Kalau tidak,",
                    "    ia tidak berpengaruh apa pun, dan dari luar kelihatannya",
                    "    seperti tidak terjadi apa-apa.",
                    "",
                    "export sebenarnya cuma menjawab satu pertanyaan: variabel ini",
                    "ikut turun ke proses anak atau tidak?",
                    "",
                    "  nama=\"Andi\"      hanya ada di shell ini",
                    "  export nama      ikut turun ke setiap proses anak sesudahnya",
                    "  export API=\"x\"   membuat dan menandai sekaligus",
                    "",
                    "Arahnya SATU JALAN: ke bawah, tidak pernah ke atas.",
                    "  Anak boleh mengubah nilai warisannya sesuka hati; induknya",
                    "  tidak akan pernah tahu.",
                    "  Tidak ada cara membuat ./x.sh mengubah variabel di terminal",
                    "  yang memanggilnya. Kalau kamu memang butuh itu, jawabannya",
                    "  bukan export -- jawabannya source.",
                ],
            },
            {
                "heading": "Bukti: bash x.sh vs source x.sh",
                "body": [
                    "Berkas yang sama persis, dijalankan dua cara. Awasi warna dan pwd.",
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
                    "Baris kedua itu intinya. contoh-anak.sh SUDAH benar-benar",
                    "mengubah warna dan SUDAH benar-benar pindah folder -- hanya saja",
                    "di proses lain, yang langsung mati sesudahnya. Baris ketiga",
                    "menjalankan berkas yang sama persis, dan kali ini bekasnya",
                    "tertinggal, karena tidak ada proses baru yang lahir.",
                    "",
                    "Inilah sebabnya memecah proyek jadi beberapa berkas di bash",
                    "memakai source, bukan menjalankan berkasnya:",
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
                    "Titik sendirian di awal baris sering dikira salah ketik. Bukan.",
                    "'. berkas' dan 'source berkas' adalah perintah yang sama: titik",
                    "yang lebih tua dan lebih portabel, source yang lebih enak dibaca.",
                    "Di kode sungguhan kamu akan bertemu keduanya, kadang di berkas",
                    "yang sama.",
                    "",
                    "Berkas yang di-source TIDAK harus punya shebang dan tidak perlu",
                    "izin eksekusi. Ia tidak pernah dijalankan sebagai program, cuma",
                    "dibaca sebagai teks perintah. Konsekuensinya: berkas yang kamu",
                    "source bisa melakukan APA SAJA pada shell-mu. Jangan pernah",
                    "source berkas yang isinya tidak kamu percayai.",
                ],
            },
            {
                "heading": "Script yang tahu foldernya sendiri",
                "body": [
                    "Sebuah script hampir selalu punya berkas pendamping: lib/umum.sh,",
                    "config, template. Kalau ditulis 'source lib/umum.sh' begitu saja,",
                    "yang dicari adalah lib/umum.sh relatif terhadap folder ORANG YANG",
                    "MEMANGGIL, bukan folder script. Dipanggil dari folder lain,",
                    "script langsung gagal -- dan pesan errornya cuma 'No such file",
                    "or directory', yang tidak menjelaskan apa-apa.",
                    "",
                    "Jawabannya satu idiom yang muncul di ribuan script. Bedah dari",
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
                    "dirname, basename, dan realpath itu PROGRAM, bukan sintaks bash:",
                    "  dirname /home/andi/laporan.txt   -> /home/andi",
                    "  basename /home/andi/laporan.txt  -> laporan.txt",
                    "  basename laporan.txt .txt        -> laporan",
                    "  realpath ../data                 -> absolut, symlink lurus",
                    "",
                    "Kamu sudah punya jalan lain ke dua yang pertama, di materi",
                    "Operasi String: ${jalur%/*} sepadan dengan dirname, dan",
                    "${jalur##*/} sepadan dengan basename. Bentuk ${} tidak memanggil",
                    "program lain sehingga jauh lebih cepat di dalam perulangan;",
                    "dirname dan basename lebih enak dibaca dan lebih rapi menangani",
                    "kasus aneh seperti jalur tanpa garis miring sama sekali.",
                    "Dua-duanya wajar dipakai.",
                    "",
                    "Baris penjaga di contoh di bawah:",
                    "  if [[ \"${BASH_SOURCE[0]}\" == \"$0\" ]]; then",
                    "",
                    "Bacanya: 'berkas ini sedang dieksekusi langsung, bukan",
                    "di-source'. Ini padanan bash dari if __name__ == \"__main__\" di",
                    "Python. Gunanya: satu berkas bisa jadi pustaka (di-source supaya",
                    "fungsinya bisa dipakai) sekaligus program (dijalankan langsung",
                    "untuk mengerjakan sesuatu), tanpa keduanya saling mengganggu.",
                    "",
                    "Kenapa $0 sendirian tidak cukup? Karena saat sebuah berkas",
                    "di-source, $0 tetap berisi nama pemanggilnya, bukan nama berkas",
                    "yang sedang dibaca. Hanya BASH_SOURCE yang tahu berkas mana yang",
                    "isinya sedang dijalankan.",
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
                    "Dua tanda yang bentuknya mirip, artinya jauh berbeda:",
                    "",
                    "  { perintah1; perintah2; }  kelompokkan, TETAP di shell ini",
                    "  ( perintah1; perintah2 )   kelompokkan, jalan di SUBSHELL",
                    "",
                    "Dua aturan { } yang wajib hafal, karena melanggarnya memberi",
                    "pesan error yang sama sekali tidak menyebut penyebabnya:",
                    "",
                    "  1. WAJIB ada spasi setelah {",
                    "     '{echo a; }' gagal, karena '{echo' terbaca sebagai satu",
                    "     nama perintah.",
                    "  2. WAJIB ada ; atau baris baru sebelum }",
                    "     '{ echo a }' gagal, karena } tidak pernah dianggap penutup.",
                    "",
                    "  Yang muncul di layar: 'syntax error near unexpected token }'",
                    "  atau bahkan 'unexpected end of file'. Keduanya menunjuk ke",
                    "  tempat yang salah. Begitu melihat pesan itu, hal PERTAMA yang",
                    "  dicek adalah spasi dan titik komanya.",
                    "  ( ) bebas dari dua aturan ini; kurung sudah memisah sendiri.",
                    "",
                    "Yang tidak pernah bocor keluar dari ( ):",
                    "  - cd, variabel, set -x, shopt, umask -- semuanya kembali",
                    "    seperti semula begitu kurungnya ditutup.",
                    "  - exit di dalam ( ) hanya menutup SUBSHELL-nya; script induk",
                    "    jalan terus, dan angka exit itu jadi nilai $? sesudahnya.",
                    "  - Sebaliknya, exit di dalam { } menghentikan SELURUH script.",
                    "",
                    "Dua idiom yang akan sering kamu temui di kode orang:",
                    "",
                    "  (cd \"$dir\" && make)",
                    "    Kerjakan make di folder lain tanpa perlu cd balik. && bikin",
                    "    make batal kalau cd gagal -- penting, karena tanpa itu make",
                    "    akan berjalan di folder yang salah tanpa ada yang mencegah.",
                    "",
                    "  perintah || { echo \"pesan\" >&2; exit 1; }",
                    "    Kalau perintah gagal, kerjakan DUA hal sekaligus: cetak",
                    "    pesan ke stderr, lalu keluar. Di sini { } wajib, bukan ( ):",
                    "    exit-nya harus mematikan script yang sungguhan. Bentuk ini",
                    "    muncul lagi di kerangka script pada materi Debugging &",
                    "    Praktik Baik dan di studi kasus penutup.",
                    "",
                    "JEBAKAN PIPE. Setiap sisi sebuah pipe dijalankan di subshell-nya",
                    "sendiri. Jadi 'echo halo | read -r kata' memang mengisi kata --",
                    "di proses sebelah, yang mati begitu pipe selesai. Tidak ada",
                    "pesan error apa pun; variabelnya cuma kosong.",
                    "",
                    "Bentuk yang paling sering memakan korban adalah perulangannya:",
                    "  n=0",
                    "  cat data.txt | while read -r baris; do ((n++)); done",
                    "  echo \"$n\"    -> tetap 0, bukan jumlah baris",
                    "",
                    "  Perbaikannya: buang pipe-nya, alihkan berkasnya langsung.",
                    "  n=0",
                    "  while read -r baris; do ((n++)); done < data.txt",
                    "  echo \"$n\"    -> benar",
                    "",
                    "Begitu ada variabel yang 'ajaib jadi kosong lagi' setelah sebuah",
                    "perulangan, pertanyaan pertamanya selalu: apakah perulangan itu",
                    "ada di sisi kanan pipe?",
                    "",
                    "Memastikan program yang dibutuhkan benar-benar terpasang:",
                    "  command -v jq >/dev/null 2>&1 || { echo \"butuh jq\" >&2; exit 1; }",
                    "",
                    "  command -v mencetak lokasi program dan memberi status 0 kalau",
                    "  ketemu. >/dev/null 2>&1 membuang cetakannya; yang dipakai cuma",
                    "  statusnya. Taruh pemeriksaan seperti ini di awal script:",
                    "  berhenti di baris pertama dengan pesan jelas jauh lebih baik",
                    "  daripada gagal di tengah pekerjaan, saat separuh berkas sudah",
                    "  terlanjur dipindah.",
                    "  Jangan pakai 'which' untuk ini. Ia program luar, perilakunya",
                    "  beda-beda antar sistem, dan ia tidak tahu apa-apa soal fungsi",
                    "  maupun alias.",
                    "",
                    "type menjawab pertanyaan 'nama ini sebenarnya apa?':",
                    "  type -t echo       -> builtin   bawaan bash sendiri",
                    "  type -t sed        -> file      program di salah satu PATH",
                    "  type -t ll         -> alias     kalau kamu punya alias itu",
                    "  type namafungsimu  -> menampilkan seluruh isi fungsinya",
                    "",
                    "Ini alat pertama saat sebuah perintah berperilaku aneh: sering",
                    "ternyata nama itu sudah dibajak fungsi atau alias, bukan program",
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
                    "Setiap kali kamu membuka terminal baru, bash TIDAK mulai dari nol. Ia lebih dulu",
                    "membaca beberapa berkas setelan di folder home-mu, lalu menjalankan isinya baris",
                    "demi baris persis seolah kamu sendiri yang mengetiknya.",
                    "",
                    "Berkas setelan itu namanya diawali TITIK, jadi tidak muncul di 'ls' biasa.",
                    "Lihat dengan 'ls -a ~'. Orang menyebut kumpulan berkas ini DOTFILES.",
                    "",
                    "  ~/.bashrc         setelan shell interaktif: alias, prompt, riwayat, PATH",
                    "  ~/.bash_profile   setelan shell login: dijalankan saat kamu login",
                    "  ~/.profile        versi netral, dibaca juga oleh shell selain bash",
                    "  ~/.bash_history   bukan setelan - ini catatan perintah yang pernah diketik",
                    "",
                    "Tanda ~ berarti folder home-mu, jadi ~/.bashrc sama dengan /home/levi/.bashrc.",
                    "",
                    "KAPAN MASING-MASING DIBACA",
                    "",
                    "  Shell LOGIN         -> ~/.bash_profile (kalau tidak ada: ~/.bash_login,",
                    "                         kalau itu pun tidak ada: ~/.profile)",
                    "    Terjadi saat: masuk lewat SSH, login di layar teks, 'su - pengguna'.",
                    "",
                    "  Shell NON-LOGIN     -> ~/.bashrc",
                    "    Terjadi saat: membuka tab terminal baru di desktop. Ini yang paling sering.",
                    "",
                    "  Shell NON-INTERAKTIF -> tidak membaca dua-duanya.",
                    "    Terjadi saat: 'bash script.sh'. Script kamu TIDAK mewarisi isi ~/.bashrc.",
                    "",
                    "Dari sini muncul keluhan klasik \"setelanku kok tidak kepakai\":",
                    "  - Baris export ditaruh di ~/.bashrc, lalu kamu masuk lewat SSH. Yang dibaca",
                    "    ~/.bash_profile, jadi baris itu tidak pernah ikut jalan.",
                    "  - Baris export ditaruh di ~/.bash_profile, lalu kamu buka tab terminal baru.",
                    "    Yang dibaca ~/.bashrc. Hasilnya sama saja: tidak kepakai.",
                    "",
                    "Karena itu hampir semua distro memasang jembatan di ~/.bash_profile, supaya",
                    "cuma ada SATU berkas yang perlu kamu sunting seumur hidup:",
                    "",
                    "  # isi ~/.bash_profile",
                    "  [[ -f ~/.bashrc ]] && . ~/.bashrc",
                    "",
                    "Sesudah menyunting ~/.bashrc, perubahannya belum berlaku di terminal yang sedang",
                    "terbuka. Dua cara membuatnya berlaku:",
                    "  1. Tutup terminal lalu buka lagi.",
                    "  2. source ~/.bashrc      -> baca ulang di shell yang SEKARANG jalan.",
                    "",
                    "Harus 'source', bukan 'bash ~/.bashrc'. Alasannya ada di materi Proses, source,",
                    "dan Subshell: menjalankannya sebagai script bikin setelannya mati bersama proses",
                    "anaknya, dan terminalmu tidak berubah sedikit pun.",
                ],
            },
            {
                "heading": "Potongan khas isi ~/.bashrc",
                "code": "#!/usr/bin/env bash\n# Potongan yang khas ada di ~/.bashrc. Di sini ia dijalankan sebagai script\n# biasa supaya efek tiap barisnya kelihatan, tanpa mengubah setelan aslimu.\n\n# 1. PATH -- taruh folder program pribadi di DEPAN daftar bawaan\nexport PATH=\"$HOME/.local/bin:$PATH\"\n\n# 2. Alias -- nama pendek untuk perintah yang sering diketik\nalias ll='ls -alF'\nalias gs='git status'\nalias ..='cd ..'\n\n# 3. Riwayat perintah\nHISTSIZE=10000\nHISTFILESIZE=20000\nHISTCONTROL=ignorespace:erasedups\nshopt -s histappend\n\n# 4. Bentuk prompt: pengguna@mesin:folder$\nPS1='\\u@\\h:\\w\\$ '\n\n# 5. Menjalankan keluaran sebuah perintah sebagai kode\n# eval \"$(pyenv init -)\"\n\necho \"PATH kini diawali : ${PATH%%:*}\"\necho \"Definisi alias ll : $(alias ll)\"\necho \"Riwayat disimpan  : $HISTSIZE baris\"\necho \"Bentuk prompt PS1 : $PS1\"",
            },
            {
                "body": [
                    "ALIAS - nama pendek untuk perintah panjang",
                    "",
                    "  alias ll='ls -alF'        pakai petik TUNGGAL supaya isinya tidak diproses",
                    "  alias gs='git status'     sekarang di terminal.",
                    "  alias                     tampilkan semua alias yang aktif",
                    "  unalias ll                hapus satu alias",
                    "  \\ls                       jalankan 'ls' asli, lewati aliasnya",
                    "",
                    "  Alias hanya menggantikan KATA PERTAMA sebuah perintah, dan hanya di awal.",
                    "  Alias tidak bisa menerima argumen di tengah; untuk itu pakai fungsi.",
                    "",
                    "JEBAKAN TERBESAR: ALIAS TIDAK BERLAKU DI DALAM SCRIPT.",
                    "  Script berjalan di shell non-interaktif, dan bash sengaja mematikan",
                    "  penggantian alias di sana. Jadi script yang memakai 'll' atau 'gs' akan",
                    "  gagal dengan 'command not found' di mesin siapa pun, termasuk mesinmu.",
                    "  Alias itu kenyamanan mengetik, bukan bagian dari program. Di script,",
                    "  tulis perintah lengkapnya.",
                    "",
                    "  Jebakan turunannya: alias rm='rm -i' terasa aman karena selalu bertanya",
                    "  dulu. Tapi ia melatih jarimu menekan Enter tanpa membaca, dan di mesin",
                    "  orang lain - atau di dalam script - alias itu tidak ada. Yang hilang",
                    "  bukan cuma konfirmasinya, tapi juga kehati-hatianmu.",
                    "",
                    "RIWAYAT PERINTAH - kamu jarang perlu mengetik ulang",
                    "",
                    "  history            tampilkan perintah lama, bernomor",
                    "  !!                 ulangi perintah terakhir (sudo !!  = ulangi pakai sudo)",
                    "  !542               jalankan perintah nomor 542 dari daftar history",
                    "  !$                 argumen TERAKHIR dari perintah sebelumnya",
                    "  Ctrl-R             cari mundur sambil mengetik. Tekan lagi untuk yang",
                    "                     lebih lama, Enter untuk menjalankan, Esc untuk menyunting.",
                    "",
                    "  Setelan riwayat yang ditaruh di ~/.bashrc:",
                    "    HISTSIZE=10000              berapa baris disimpan di memori",
                    "    HISTFILESIZE=20000          berapa baris disimpan di ~/.bash_history",
                    "    HISTCONTROL=ignorespace     perintah yang DIAWALI SPASI tidak dicatat",
                    "    HISTCONTROL=erasedups       hapus duplikat lama",
                    "    shopt -s histappend         tambahkan ke berkas, jangan timpa isinya",
                    "",
                    "  ignorespace itu praktis: ketik satu spasi sebelum perintah berisi",
                    "  password atau token, dan perintah itu tidak masuk ~/.bash_history.",
                    "",
                    "PS1 dan PS2 - bentuk prompt",
                    "",
                    "  PS1 adalah tampilan prompt utama. \\u=pengguna, \\h=nama mesin, \\w=folder",
                    "  saat ini, \\$ jadi # kalau root. PS2 adalah prompt lanjutan, yang muncul",
                    "  sebagai '>' saat perintahmu belum selesai (misalnya petik belum ditutup).",
                    "  Cukup kenali namanya: begitu kamu buka .bashrc milik orang, deretan",
                    "  karakter aneh yang paling bikin pusing biasanya cuma PS1.",
                    "",
                    "CARA MEMBACA .bashrc MILIK ORANG LAIN",
                    "  Dotfiles adalah berkas yang paling sering disalin orang di GitHub, karena",
                    "  isinya hasil bertahun-tahun kebiasaan. Bacanya jangan dari atas ke bawah -",
                    "  pilah dulu per jenis: baris export (setelan lingkungan), baris alias",
                    "  (singkatan), baris PS1/PROMPT (tampilan), dan baris eval (kode yang",
                    "  ditempelkan alat lain). Sisanya biasanya penjaga 'kalau berkasnya ada,",
                    "  baca'. Salin sebarisnya saja tiap kali, lalu source dan lihat efeknya.",
                ],
            },
            {
                "heading": "PATH: daftar tempat shell mencari perintah",
                "body": [
                    "Saat kamu mengetik 'ls', bash tidak tahu di mana program bernama ls berada. Ia",
                    "melihat variabel PATH: SATU string berisi daftar folder yang dipisah TITIK DUA.",
                    "Bash memeriksa folder itu dari KIRI ke kanan dan berhenti di yang pertama cocok.",
                    "Kalau daftarnya habis dan tetap tidak ketemu, muncul 'command not found'.",
                    "",
                    "Menambahkan folder sendiri ke PATH selalu ditulis begini:",
                    "",
                    "  export PATH=\"$HOME/.local/bin:$PATH\"",
                    "",
                    "Bacanya: PATH yang baru = folder baru, titik dua, lalu SELURUH isi PATH yang lama.",
                    "  - $PATH di sebelah kanan itu wajib. Ia menyalin daftar lama supaya tidak hilang.",
                    "  - Menaruh folder baru DI DEPAN berarti versimu menang atas versi bawaan sistem.",
                    "    Ditaruh di belakang (\"$PATH:$HOME/.local/bin\") berarti yang bawaan menang duluan.",
                    "",
                    "KESALAHAN YANG BIKIN TERMINAL TERASA RUSAK",
                    "",
                    "  export PATH=\"$HOME/.local/bin\"      <- lupa menyebut $PATH lama",
                    "",
                    "  Sesudah baris itu, ls, mv, grep, bahkan nano tidak ditemukan lagi - /usr/bin",
                    "  sudah tidak ada di daftar. Terminalnya tidak rusak, ia cuma kehilangan alamat.",
                    "  Tutup terminal lalu buka lagi, semuanya normal. Yang gawat kalau baris itu",
                    "  terlanjur kamu simpan di ~/.bashrc: setiap terminal baru akan lahir rusak.",
                    "",
                    "JANGAN MEMASUKKAN TITIK (folder saat ini) KE PATH",
                    "",
                    "  export PATH=\".:$PATH\"      <- kelihatan praktis, sebenarnya berbahaya",
                    "",
                    "  Dengan itu, masuk ke sebuah folder lalu mengetik 'ls' bisa menjalankan berkas",
                    "  bernama ls MILIK FOLDER ITU, bukan ls yang asli. Cukup sekali kamu membuka",
                    "  folder hasil unduhan orang, dan perintah paling biasa berubah jadi jebakan.",
                    "  Kalau mau menjalankan program di folder saat ini, tulis ./program - itulah",
                    "  gunanya tanda ./ yang sudah kamu pakai sejak materi pertama.",
                    "",
                    "DI MANA MENARUHNYA SUPAYA PERMANEN",
                    "",
                    "  export PATH=... di dalam sebuah script cuma berlaku selama script itu jalan.",
                    "  Script adalah proses anak, dan begitu ia selesai PATH terminalmu tidak berubah",
                    "  sedikit pun - alasannya di materi Proses, source, dan Subshell. Jadi tidak ada",
                    "  script pemasang yang bisa mengubah PATH-mu secara langsung; yang bisa ia",
                    "  lakukan cuma MENAMBAHKAN barisnya ke ~/.bashrc. Itulah yang sebenarnya",
                    "  terjadi tiap kali panduan pemasangan menyuruhmu menutup dan membuka terminal.",
                    "",
                    "  Periksa hasilnya dengan:  command -v nama_program   (atau: which nama_program)",
                ],
                "code": "#!/usr/bin/env bash\n# Melihat PATH sebagai daftar folder biasa, bukan sebagai mantra.\n\ncontoh=\"/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin\"\n\necho \"1) PATH itu SATU string. Folder-foldernya dipisah titik dua:\"\necho \"   $contoh\"\n\necho\necho \"2) Dipecah per baris supaya urutannya kelihatan:\"\necho \"$contoh\" | tr ':' '\\n' | sed 's/^/   /'\n\necho\necho \"3) Shell mencari dari ATAS ke bawah lalu berhenti di yang pertama cocok.\"\nbaru=\"$HOME/bin:$contoh\"\necho \"   Menambah di depan -> ${baru%%:*} yang dicoba paling awal.\"\n\necho\necho \"4) Perintah 'ls' yang sebenarnya dipakai ada di:\"\necho \"   $(command -v ls)\"\n\necho\necho \"5) Perubahan berikut hanya hidup selama script ini berjalan:\"\nexport PATH=\"/tmp/binku:$PATH\"\necho \"   PATH sekarang diawali: ${PATH%%:*}\"\necho \"   Begitu script selesai, PATH terminalmu kembali seperti semula\"",
            },
            {
                "heading": "eval: menjalankan teks sebagai kode",
                "body": [
                    "Baris paling membingungkan di dotfiles orang biasanya berbentuk seperti ini:",
                    "",
                    "  eval \"$(pyenv init -)\"",
                    "  eval \"$(ssh-agent -s)\"",
                    "  eval \"$(dircolors -b)\"",
                    "",
                    "Bacanya dari dalam ke luar, dan pyenv di situ BUKAN nama fungsi yang dipanggil:",
                    "  1. 'pyenv init -' dijalankan. Keluarannya bukan hasil, melainkan TEKS berisi",
                    "     kode bash - beberapa export dan definisi fungsi.",
                    "  2. $( ... ) menangkap teks itu.",
                    "  3. eval menjalankan teks itu sebagai perintah, di shell yang sekarang.",
                    "",
                    "Kenapa berputar begitu? Karena pyenv adalah program terpisah, dan program",
                    "terpisah tidak bisa mengubah variabel shell yang memanggilnya - variabel cuma",
                    "turun ke bawah. Jadi ia menitipkan kodenya sebagai teks, dan shell-mu sendiri",
                    "yang menjalankannya. Buktikan dengan mata: jalankan 'ssh-agent -s' TANPA eval,",
                    "kamu akan melihat baris-baris export yang tercetak begitu saja tanpa efek apa pun.",
                    "",
                    "SISI BAHAYANYA",
                    "  eval menjalankan apa saja yang ada di dalam teksnya. Kalau sebagian teks itu",
                    "  berasal dari pengguna, dari nama berkas, atau dari jawaban server, maka",
                    "  pengguna itu bisa menjalankan perintah apa pun dengan hakmu - termasuk rm -rf.",
                    "  Ini persis yang diperingatkan shellcheck setiap kali ia melihat eval.",
                    "",
                    "  Aturan praktisnya: eval hanya untuk teks yang kamu percaya penuh, biasanya",
                    "  keluaran alat yang kamu pasang sendiri. Untuk kebutuhan lain hampir selalu",
                    "  ada jalan yang lebih aman - array untuk menyusun perintah, dan case untuk",
                    "  memilih di antara beberapa perintah tetap.",
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
                    "Bash memperlakukan semua sebagai string, jadi hitung-hitungan",
                    "butuh sintaks khusus.",
                    "",
                    "Cara utama: $(( ... ))",
                    "  hasil=$((5 + 3))",
                    "  echo $((10 / 3))     -> 3  (PEMBAGIAN BULAT, sisa dibuang)",
                    "  echo $((10 % 3))     -> 1  (sisa bagi)",
                    "  echo $((2 ** 8))     -> 256 (pangkat)",
                    "",
                    "Di dalam $(( )) tanda $ pada variabel boleh dilewat:",
                    "  a=5; b=3",
                    "  echo $((a + b))      -> sama saja dengan $(($a + $b))",
                    "",
                    "PENTING: bash TIDAK bisa desimal secara bawaan.",
                    "  echo $((10 / 4))     -> 2, bukan 2.5",
                    "",
                    "Untuk desimal, pakai bc atau awk:",
                    "  echo \"scale=2; 10/4\" | bc     -> 2.50",
                    "  awk 'BEGIN {printf \"%.2f\\n\", 10/4}'  -> 2.50",
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
                    "Operator penugasan singkat (di dalam (( )) ):",
                    "  ((x += 5))    sama dengan x = x + 5",
                    "  ((x -= 2))",
                    "  ((x *= 3))",
                    "  ((x++))       naikkan 1",
                    "  ((x--))       turunkan 1",
                    "",
                    "Perhatian pada ((x++)) di awal script:",
                    "  Kalau x bernilai 0, ((x++)) mengembalikan status 1 (dianggap",
                    "  gagal). Kalau script pakai 'set -e', script bisa berhenti.",
                    "  Amannya tulis: ((x++)) || true   atau   x=$((x + 1))",
                    "",
                    "let dan expr adalah cara lama:",
                    "  let \"hasil = 5 + 3\"",
                    "  hasil=$(expr 5 + 3)",
                    "  Keduanya masih jalan, tapi $(( )) lebih disukai sekarang.",
                ]
            },
        ],
    },
    {
        "title": "9. Percabangan (if, case)",
        "sections": [
            {
                "body": [
                    "Bentuk dasar if:",
                    "",
                    "  if [[ kondisi ]]; then",
                    "      perintah",
                    "  elif [[ kondisi_lain ]]; then",
                    "      perintah",
                    "  else",
                    "      perintah",
                    "  fi",
                    "",
                    "Penutupnya 'fi' (if dibalik). Wajib ada.",
                    "",
                    "Pakai [[ ]] (kurung siku ganda), bukan [ ] tunggal.",
                    "  [[ ]] adalah fitur bash: lebih aman, mendukung && || dan regex.",
                    "  [ ] adalah perintah lama, lebih rewel soal spasi & variabel kosong.",
                    "      'Lama' di sini bukan berarti usang. [ ] justru ada di SEMUA",
                    "      shell, sedangkan [[ ]] cuma milik bash. Selama shebang-mu",
                    "      bash, pakai [[ ]]. Begitu berkasnya #!/bin/sh, [ ] jadi",
                    "      satu-satunya pilihan - lihat materi Bash vs sh: Portabilitas",
                    "      & POSIX.",
                    "",
                    "Perbandingan ANGKA:",
                    "  -eq  sama dengan        -ne  tidak sama",
                    "  -gt  lebih besar        -ge  lebih besar atau sama",
                    "  -lt  lebih kecil        -le  lebih kecil atau sama",
                    "",
                    "Perbandingan TEKS:",
                    "  ==   sama dengan        !=   tidak sama",
                    "  <    urutan abjad lebih dulu",
                    "  -z   string KOSONG      -n   string TIDAK kosong",
                    "",
                    "Pemeriksaan FILE:",
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
                    "if tidak menuntut kurung siku. Yang dilihatnya cuma EXIT CODE dari",
                    "perintah yang kamu taruh sesudahnya: 0 berarti 'benar', selain 0",
                    "berarti 'salah'. [[ ]] sendiri sebetulnya juga cuma perintah yang",
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
                    "Perhatikan -q pada grep dan >/dev/null pada command. Keduanya",
                    "membungkam KELUARAN perintahnya, karena yang dipakai cuma statusnya.",
                    "Tanpa itu hasil pencarian ikut tumpah ke layar padahal tidak diminta.",
                    "",
                    "Tanda seru di depan membalik statusnya, sama seperti di dalam",
                    "[[ ]]. Jadi baris berikut terbaca wajar walau tidak ada satu pun",
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
                    "  - Tiap cabang ditutup dengan ;; (titik koma dua kali)",
                    "  - | memisahkan beberapa pola untuk satu cabang",
                    "  - * adalah cabang default (seperti else)",
                    "  - Penutup blok adalah 'esac' (case dibalik)",
                    "  - Pola mendukung wildcard: *.txt, [0-9], ??",
                    "",
                    "case jauh lebih rapi daripada if-elif berantai",
                    "kalau yang dibandingkan cuma satu variabel.",
                    "",
                    "Perbandingan aritmatika bisa juga pakai (( )):",
                    "  if (( nilai >= 75 )); then",
                    "  Di dalam (( )) kamu bisa pakai >, <, >= seperti bahasa lain.",
                ]
            },
        ],
    },
    {
        "title": "10. Perulangan (for, while, until)",
        "sections": [
            {
                "body": [
                    "Bash punya empat bentuk perulangan bawaan.",
                    "",
                    "1. for ... in  -> mengulang setiap item dalam daftar",
                    "2. for (( ))   -> gaya C, pakai penghitung",
                    "3. while       -> ulang SELAMA kondisi benar",
                    "4. until       -> ulang SAMPAI kondisi benar (kebalikan while)",
                    "",
                    "Blok perulangan diapit 'do' dan 'done'.",
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
                    "Pola membaca file baris demi baris:",
                    "  while IFS= read -r baris; do ... done < file",
                    "",
                    "  IFS=   mematikan pemotongan spasi, jadi spasi di awal/akhir",
                    "         baris ikut terbaca apa adanya.",
                    "  -r     mencegah backslash diproses sebagai escape.",
                    "",
                    "  Hafalkan pola ini. Ini cara BENAR membaca file di bash.",
                    "  Jangan pakai: for baris in $(cat file)  -- itu memecah",
                    "  berdasarkan spasi, bukan baris.",
                    "",
                    "Mengendalikan perulangan:",
                    "  break      keluar dari perulangan",
                    "  continue   lompat ke iterasi berikutnya",
                    "  break 2    keluar dari 2 tingkat perulangan sekaligus",
                    "",
                    "Perulangan tak berhingga:",
                    "  while true; do ... done",
                    "  Wajib ada break di dalamnya, atau script tidak akan berhenti.",
                ]
            },
            {
                "heading": "select: menu bernomor yang dibuatkan bash",
                "body": [
                    "Ada bentuk kelima yang jarang diajarkan tapi sering muncul di script",
                    "instalasi dan alat admin. select membuatkan menu bernomor dari sebuah",
                    "daftar, membaca ketikan pemakai, lalu mengulang terus sampai break.",
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
                    "Tiga hal yang perlu diingat:",
                    "  PS3     teks prompt-nya. Kalau tidak diisi, bash memakai '#?' yang",
                    "          tidak menjelaskan apa-apa ke pemakai.",
                    "  $REPLY  apa yang DIKETIK pemakai, apa adanya.",
                    "  $warna  nilai yang terpilih. KOSONG kalau ketikannya bukan nomor",
                    "          yang ada di daftar - itu sebabnya cabang *) di atas ada.",
                    "",
                    "select tidak berhenti sendiri. Tanpa break ia menampilkan menunya",
                    "berulang-ulang; pemakai baru bisa keluar dengan Ctrl-D.",
                ]
            },
        ],
    },
    {
        "title": "11. Array",
        "sections": [
            {
                "body": [
                    "Bash punya dua jenis array:",
                    "  1. Array biasa (indeks angka, mulai dari 0)",
                    "  2. Associative array / map (indeks berupa teks) - butuh bash 4+",
                    "",
                    "Membuat array biasa:",
                    "  buah=(\"apel\" \"jeruk\" \"mangga\")",
                    "",
                    "Mengakses:",
                    "  ${buah[0]}      item pertama",
                    "  ${buah[-1]}     item terakhir",
                    "  ${buah[@]}      SEMUA item",
                    "  ${#buah[@]}     JUMLAH item",
                    "  ${!buah[@]}     semua INDEKS",
                    "",
                    "PERHATIAN kurung kurawal:",
                    "  $buah      -> hanya memberi item pertama, bukan seluruh array!",
                    "  ${buah[@]} -> baru seluruh array.",
                    "",
                    "Selalu bungkus dengan petik: \"${buah[@]}\"",
                    "  Tanpa petik, item yang mengandung spasi akan terpecah.",
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
                    "Selain [@] ada [*]. Keduanya berarti 'seluruh isi array', dan",
                    "bedanya baru kelihatan begitu dibungkus petik ganda:",
                    "",
                    "  \"${buah[@]}\"   -> N kata terpisah, satu kata per elemen",
                    "  \"${buah[*]}\"   -> SATU kata, semua elemen disambung jadi satu",
                    "",
                    "Penyambungnya adalah karakter PERTAMA dari IFS, yang normalnya spasi.",
                    "",
                    "  buah=(\"apel\" \"jeruk manis\" \"mangga\")",
                    "  for b in \"${buah[@]}\"; do echo \"- $b\"; done",
                    "      -> tiga baris, 'jeruk manis' tetap utuh",
                    "  echo \"${buah[*]}\"",
                    "      -> apel jeruk manis mangga        (satu baris, satu kata)",
                    "",
                    "Aturan pakainya pendek saja:",
                    "  Mau MENGULANG atau meneruskan ke perintah lain -> \"${arr[@]}\".",
                    "  Mau MENCETAK isinya jadi satu baris ringkas    -> \"${arr[*]}\".",
                    "",
                    "  menipis=(\"susu\" \"telur\")",
                    "  echo \"Stok menipis: ${menipis[*]}\"   -> Stok menipis: susu telur",
                    "",
                    "Penyambungnya bisa diganti sebentar lewat IFS:",
                    "  LAMA=$IFS; IFS=,; echo \"${menipis[*]}\"; IFS=$LAMA   -> susu,telur",
                    "",
                    "Ini pasangan persis dari $@ dan $* pada argumen script, yang dibahas",
                    "di materi Argumen & Exit Code. Aturannya sama, cuma bendanya beda.",
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
                    "Catatan penting associative array:",
                    "  - WAJIB declare -A sebelum dipakai. Kalau lupa, bash",
                    "    memperlakukannya sebagai array biasa dan hasilnya kacau.",
                    "  - Urutan iterasi TIDAK terjamin. Kalau butuh urut,",
                    "    saring lewat sort:",
                    "      for k in $(echo \"${!umur[@]}\" | tr ' ' '\\n' | sort); do",
                    "",
                    "    tr di situ menukar karakter dengan karakter: tiap SPASI diganti",
                    "    baris baru. Perlu, karena ${!umur[@]} keluar sebagai satu baris",
                    "    berisi semua kunci, sedangkan sort mengurutkan BARIS - bukan kata",
                    "    di dalam satu baris. Tanpa tr, sort cuma menerima satu baris dan",
                    "    mengembalikannya apa adanya.",
                    "",
                    "  - Butuh bash versi 4 ke atas. macOS bawaan masih bash 3.2.",
                    "    Cek dengan: echo $BASH_VERSION",
                    "",
                    "Memecah string jadi array:",
                    "  teks=\"a,b,c\"",
                    "  IFS=',' read -ra bagian <<< \"$teks\"",
                    "  echo \"${bagian[1]}\"   -> b",
                    "",
                    "Mengisi array dari BERKAS, satu baris jadi satu elemen:",
                    "  mapfile -t baris < catatan.txt",
                    "  echo \"${#baris[@]} baris terbaca\"",
                    "",
                    "  -t membuang karakter baris baru di ujung tiap elemen; tanpa itu",
                    "  tiap elemen membawa baris barunya ikut serta. mapfile butuh bash 4+.",
                    "  Bentuk lengkapnya, termasuk mengisi array dari keluaran sebuah",
                    "  perintah, ada di materi find, xargs, dan Pemrosesan Massal.",
                ]
            },
        ],
    },
    {
        "title": "12. Fungsi",
        "sections": [
            {
                "body": [
                    "Dua cara menulis fungsi (sama saja hasilnya):",
                    "",
                    "  nama_fungsi() {",
                    "      perintah",
                    "  }",
                    "",
                    "  function nama_fungsi {",
                    "      perintah",
                    "  }",
                    "",
                    "Bentuk pertama lebih portabel, pakai itu saja.",
                    "",
                    "Fungsi HARUS didefinisikan sebelum dipanggil, karena bash",
                    "membaca script dari atas ke bawah.",
                    "",
                    "Memanggil fungsi seperti memanggil perintah biasa:",
                    "  sapa \"Andi\"          <- TANPA kurung, argumen dipisah spasi",
                    "  BUKAN sapa(\"Andi\")",
                    "",
                    "Argumen diakses dengan $1, $2, $3, dan seterusnya.",
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
                    "Dua cara fungsi 'mengembalikan' nilai:",
                    "",
                    "1. echo + command substitution (untuk DATA)",
                    "     jumlahkan() { echo $(($1 + $2)); }",
                    "     hasil=$(jumlahkan 3 4)",
                    "",
                    "2. return (hanya untuk STATUS, nilai 0-255)",
                    "     cek_genap() {",
                    "         if (( $1 % 2 == 0 )); then return 0; else return 1; fi",
                    "     }",
                    "     if cek_genap 4; then echo \"genap\"; fi",
                    "",
                    "INGAT: return di bash BUKAN untuk mengirim data seperti di",
                    "Python atau Java. return hanya mengirim kode status.",
                    "  0     = sukses / benar",
                    "  1-255 = gagal / salah",
                    "Ini kebalikan dari kebiasaan bahasa lain, hati-hati.",
                    "",
                    "Kata kunci 'local':",
                    "  Tanpa local, semua variabel di bash bersifat GLOBAL.",
                    "  Variabel di dalam fungsi bisa menimpa variabel di luar.",
                    "  SELALU pakai local untuk variabel di dalam fungsi.",
                ]
            },
            {
                "heading": "Mengoper array ke fungsi",
                "body": [
                    "Pertanyaan yang pasti muncul begitu kamu punya array dan punya",
                    "fungsi: bagaimana mengirim array-nya ke dalam fungsi?",
                    "",
                    "Fungsi bash menerima argumen sebagai DAFTAR KATA, bukan sebagai satu",
                    "objek. Jadi array dikirim dengan cara dilelehkan jadi argumen, lalu",
                    "dirakit ulang di dalam:",
                    "",
                    "  cetak_daftar() {",
                    "      local daftar=(\"$@\")",
                    "      echo \"${#daftar[@]} item\"",
                    "  }",
                    "",
                    "  buah=(\"apel\" \"jeruk manis\")",
                    "  cetak_daftar \"${buah[@]}\"",
                    "",
                    "Petik pada \"${buah[@]}\" wajib. Tanpa petik, 'jeruk manis' pecah jadi",
                    "dua argumen dan fungsi menerima tiga item, bukan dua.",
                    "",
                    "Dua batasnya, supaya tidak kaget nanti:",
                    "  - Yang sampai ke fungsi adalah SALINAN. Mengubah daftar di dalam",
                    "    fungsi tidak menyentuh buah yang di luar.",
                    "  - Cuma bisa satu array. Begitu ada argumen lain ikut dikirim,",
                    "    fungsi tidak punya cara tahu di mana array-nya berakhir.",
                    "",
                    "Kalau kamu butuh MENGUBAH array milik pemanggil, atau butuh mengirim",
                    "dua array sekaligus, jawabannya nameref (local -n) di materi Fitur",
                    "Bash Lanjutan.",
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
                    "Script bisa menerima argumen dari baris perintah:",
                    "  ./backup.sh /data /cadangan",
                    "",
                    "Di dalam script:",
                    "  $0   ./backup.sh   (nama script)",
                    "  $1   /data",
                    "  $2   /cadangan",
                    "  $#   2             (jumlah argumen)",
                    "  $@   semua argumen sebagai daftar terpisah",
                    "  $*   semua argumen sebagai SATU string",
                    "",
                    "Selalu pakai \"$@\", bukan \"$*\", saat meneruskan argumen.",
                    "",
                    "Exit code (kode keluar):",
                    "  Setiap perintah mengembalikan angka saat selesai.",
                    "    0        = SUKSES",
                    "    bukan 0  = GAGAL",
                    "  Ini kebalikan dari intuisi: 0 berarti berhasil.",
                    "",
                    "  Cek exit code perintah terakhir dengan $?",
                    "  Atur exit code script sendiri dengan: exit 0 atau exit 1",
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
                    "Perhatikan >&2 pada contoh di atas.",
                    "  Itu mengalihkan pesan ke stderr (aliran error), bukan stdout.",
                    "  Pesan error HARUS ke stderr supaya tidak mengotori output",
                    "  yang mungkin sedang di-pipe ke perintah lain.",
                    "",
                    "Menyambung perintah berdasarkan hasil:",
                    "  perintah1 && perintah2    jalankan 2 kalau 1 SUKSES",
                    "  perintah1 || perintah2    jalankan 2 kalau 1 GAGAL",
                    "  perintah1 ; perintah2     jalankan 2 apa pun hasilnya",
                    "",
                    "  mkdir data && cd data",
                    "  cd /folder/salah || echo \"Gagal masuk folder\"",
                    "",
                    "Tiga pengaman yang sebaiknya ada di setiap script serius:",
                    "  set -e   hentikan script saat ada perintah gagal",
                    "  set -u   error kalau ada variabel belum didefinisikan",
                    "  set -o pipefail   pipe dianggap gagal kalau ada bagian gagal",
                    "",
                    "Ditulis singkat di baris kedua script:",
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
                    "Kamu sudah bisa membaca argumen lewat $1, $2, dan $# (materi Argumen & Exit Code).",
                    "Sekarang perhatikan bagaimana perintah yang kamu pakai tiap hari sebenarnya dipanggil:",
                    "",
                    "  cp -r -v sumber/ tujuan/",
                    "  grep -n -i \"error\" catatan.log",
                    "  tar -c -z -f arsip.tar.gz folder/",
                    "",
                    "Ada DUA jenis argumen di situ, dan bedanya bukan soal selera penulisan:",
                    "",
                    "  ARGUMEN POSISIONAL   sumber/, tujuan/, catatan.log",
                    "    Artinya ditentukan URUTANNYA: yang pertama sumber, yang kedua tujuan.",
                    "    Biasanya wajib ada, dan kalau tertukar hasilnya salah tanpa ada yang protes.",
                    "",
                    "  OPSI (sering disebut flag atau switch)   -r, -v, -n, -i, -f arsip.tar.gz",
                    "    Artinya ditentukan HURUFNYA, bukan posisinya. Boleh ditukar urutannya, boleh",
                    "    tidak ditulis sama sekali. Yang tidak ditulis memakai nilai bawaan.",
                    "",
                    "Opsi sendiri ada dua macam:",
                    "  - Opsi SAKLAR tidak membawa nilai. -v, -r, -n. Ada berarti nyala, tidak ada berarti mati.",
                    "  - Opsi BERNILAI menelan satu argumen sesudahnya. -o hasil.txt, -f arsip.tar.gz.",
                    "",
                    "Kesepakatan yang dipatuhi hampir semua alat Unix - hafalkan bentuknya, bukan alatnya:",
                    "",
                    "  -abc            sama dengan -a -b -c; saklar boleh digabung jadi satu gerombolan",
                    "  -o hasil.txt    sama dengan -ohasil.txt; nilai boleh menempel ke hurufnya",
                    "  --verbose       bentuk panjang, lebih terbaca di script; ini gaya GNU, bukan POSIX",
                    "  --out=hasil     bentuk panjang yang membawa nilai lewat tanda sama dengan",
                    "  -h / --help     hampir selalu ada; alat yang tidak menyediakannya terasa rusak",
                    "  --              penanda 'opsi habis di sini', sisanya posisional apa pun bentuknya",
                    "",
                    "Kenapa alat sungguhan hampir selalu punya keduanya sekaligus? Karena yang WAJIB dan",
                    "yang PILIHAN butuh cara penyebutan yang berbeda. Kalau semua serba posisional, menambah",
                    "satu pilihan baru berarti menggeser arti argumen ke-3, dan setiap pemanggilan lama yang",
                    "sudah tertulis di script orang lain mendadak salah arti. Opsi bisa ditambah kapan saja",
                    "tanpa mengusik yang sudah ada - itu sebabnya blok penguraian opsi ada di 20-30 baris",
                    "PERTAMA sebuah script, dan jadi bagian yang paling dulu kamu baca saat ingin tahu",
                    "\"script ini dipanggil bagaimana?\".",
                    "",
                    "Bash punya bawaan untuk mengurai opsi PENDEK: getopts. Jangan tertukar dengan getopt",
                    "(tanpa huruf s) - itu program terpisah dari paket util-linux, bukan bawaan bash, dan",
                    "versi lamanya merusak argumen yang mengandung spasi. Yang dipakai di sini getopts.",
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
                    "Baris kuncinya kita baca pelan-pelan:",
                    "",
                    "  while getopts \":hvo:\" opt; do",
                    "",
                    "getopts dipanggil BERULANG-ULANG. Tiap panggilan mengambil SATU opsi berikutnya,",
                    "menaruh hurufnya di variabel opt, lalu memberi status 0 supaya while berputar lagi.",
                    "Begitu opsi habis, statusnya bukan 0 dan perulangan berhenti sendiri.",
                    "",
                    "String \":hvo:\" adalah daftar opsi yang DITERIMA. Titik duanya punya dua arti berbeda",
                    "tergantung letaknya - ini yang paling sering bikin bingung saat membaca kode orang:",
                    "",
                    "  titik dua SESUDAH huruf     o:    opsi ini wajib membawa nilai",
                    "  titik dua di PALING DEPAN   :hvo: mode senyap: getopts tidak mencetak pesan",
                    "                                    errornya sendiri, urusan salah diserahkan ke kamu",
                    "",
                    "Jadi \":hvo:\" berarti: tangani sendiri kesalahannya, terima -h dan -v tanpa nilai,",
                    "terima -o yang membawa nilai. Tanpa titik dua depan, getopts mencetak pesan versinya",
                    "sendiri dalam bahasa Inggris ke stderr, dan cabang :) tidak pernah kena sama sekali.",
                    "",
                    "Tiga variabel yang diisi getopts:",
                    "",
                    "  $opt      huruf opsi yang barusan ditemukan (nama variabelnya kamu yang pilih)",
                    "  $OPTARG   nilai milik opsi itu, kalau opsinya memang bernilai",
                    "  $OPTIND   nomor argumen berikutnya yang BELUM diurai. Dikelola getopts sendiri.",
                    "",
                    "Di mode senyap, $OPTARG dipakai ulang untuk dua hal lain: saat opsinya tak dikenal",
                    "atau nilainya kurang, $OPTARG berisi HURUF yang bermasalah. Itu yang membuat pesan",
                    "\"opsi -$OPTARG butuh sebuah nilai\" bisa menyebut huruf yang tepat.",
                    "",
                    "  shift $((OPTIND - 1))",
                    "",
                    "Ini baris yang tidak boleh lupa. Selesai perulangan, OPTIND menunjuk argumen pertama",
                    "yang bukan opsi. shift membuang semua opsi yang sudah dicerna, sehingga $1 kembali",
                    "berarti \"argumen posisional pertama\" dan $# kembali berarti \"berapa berkas yang",
                    "dikirim\". Lupa baris ini dan seluruh kode sesudahnya membaca $1 sebagai \"-v\".",
                    "",
                    "Dua cabang case yang selalu ada di kode nyata:",
                    "",
                    "  \\?)   opsi yang tidak ada di daftar. Backslash-nya WAJIB: di dalam case, tanda",
                    "        tanya sendirian adalah wildcard yang cocok dengan satu karakter apa pun,",
                    "        jadi tanpa backslash cabang ini juga menelan cabang :) di bawahnya.",
                    "  :)    opsi bernilai yang nilainya tidak diberikan, seperti -o di ujung baris.",
                    "",
                    "Keluar dengan status 2 di kedua cabang itu, bukan 1. Kesepakatan Unix: 1 untuk",
                    "\"pekerjaannya gagal\", 2 untuk \"cara memanggilnya salah\". Lihat materi Argumen &",
                    "Exit Code untuk arti angka keluar.",
                    "",
                    "JEBAKAN 1 - getopts BERHENTI di argumen non-opsi yang pertama.",
                    "  Coba lihat baris keluaran untuk 'coba laporan.txt -v' di atas: cerewet tetap 0.",
                    "  Begitu getopts bertemu laporan.txt, ia menganggap opsi sudah habis, dan -v masuk",
                    "  ke argumen posisional. Ini bukan bug, ini aturan POSIX. Beberapa alat GNU sengaja",
                    "  melanggarnya (ls berkas -l tetap jalan), sehingga banyak orang mengira semua alat",
                    "  begitu. Script bash kamu tidak. Tulis opsi DULU, baru berkasnya.",
                    "",
                    "JEBAKAN 2 - OPTIND tidak balik sendiri ke 1.",
                    "  OPTIND itu variabel biasa yang hidup sampai script selesai. Kalau penguraian opsi",
                    "  ditaruh di dalam fungsi dan fungsinya dipanggil dua kali, panggilan kedua mulai",
                    "  dari posisi terakhir - opsinya dilewati DIAM-DIAM tanpa satu pun pesan error.",
                    "  Itu sebabnya baris pertama fungsi jalan() berbunyi: local OPTIND=1",
                    "  Kalau tidak di dalam fungsi, tulis OPTIND=1 sebelum perulangannya.",
                    "",
                    "Catatan kecil saat mencoba: pesan error di contoh sengaja dikirim ke stderr (>&2),",
                    "jadi di aplikasi ini ia muncul di panel terpisah dari keluaran biasa. Itu memang",
                    "perilaku yang benar, bukan tanda gagal.",
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
                    "Batas getopts yang perlu kamu tahu sebelum mencari-cari opsinya di dokumentasi:",
                    "getopts HANYA mengerti opsi pendek satu huruf. Tidak ada saklar apa pun yang membuat",
                    "ia paham --verbose. Kalau script kamu butuh opsi panjang, penguraiannya ditulis",
                    "tangan seperti contoh di atas - dan itulah pola yang akan kamu temui di ribuan",
                    "script di GitHub, jadi kenali bentuknya sampai hafal.",
                    "",
                    "Cara membaca perulangannya:",
                    "  while [[ $# -gt 0 ]]   selama masih ada argumen tersisa",
                    "  case \"$1\" in           lihat argumen paling depan",
                    "  shift                  buang 1 argumen (saklar: hurufnya saja)",
                    "  shift 2                buang 2 argumen (opsi bernilai: namanya DAN nilainya)",
                    "  break                  keluar dari perulangan; sisanya posisional",
                    "",
                    "URUTAN CABANGNYA PENTING. case berhenti di kecocokan pertama, jadi cabang penangkap",
                    "-?* harus di BAWAH semua opsi yang dikenal - kalau ditaruh di atas, semua opsi kamu",
                    "sendiri dilaporkan sebagai \"tak dikenal\".",
                    "",
                    "Kenapa -?* dan bukan -* seperti yang sering ditulis orang? Karena -* juga cocok dengan",
                    "tanda strip SENDIRIAN, padahal menurut kesepakatan Unix satu strip berarti \"baca dari",
                    "stdin\" (cat - | ...) dan itu argumen yang sah, bukan opsi salah ketik. -?* menuntut",
                    "minimal satu karakter sesudah stripnya.",
                    "",
                    "PENANDA -- : \"opsi habis di sini\"",
                    "  Semua yang datang sesudah -- diperlakukan sebagai argumen biasa, walaupun diawali",
                    "  strip. Bukan basa-basi: nama berkas boleh saja diawali strip, dan tanpa -- alat",
                    "  yang kamu panggil akan membacanya sebagai opsi.",
                    "",
                    "  rm -- \"$berkas\"             aman walaupun isi $berkas ternyata \"-rf\"",
                    "  grep -- \"-pola\" data.txt    cari teks '-pola', bukan opsi -p -o -l -a",
                    "  git checkout -- berkas.txt  maksudnya berkas.txt, bukan cabang bernama berkas.txt",
                    "",
                    "  Biasakan menulis -- di setiap perintah yang menerima nama berkas dari variabel atau",
                    "  dari input orang lain. Ini pengaman yang harganya nol dan sekali waktu menyelamatkan.",
                    "",
                    "BANTUAN() DAN DAFTAR OPSI ADALAH DUA TEMPAT YANG MENGATAKAN HAL SAMA",
                    "  Teks di bantuan() dan string \":hvo:\" (atau daftar cabang case) tidak saling",
                    "  memeriksa. Tidak ada satu pun yang error kalau keduanya berbeda: pemakai membaca",
                    "  -q di bantuan, mencobanya, dan dibalas \"opsi tak dikenal\". Aturannya sederhana -",
                    "  tiap kali kamu menambah satu huruf ke daftar opsi, tambahkan satu baris ke",
                    "  bantuan() di saat yang sama, sebelum mengetik apa pun yang lain.",
                    "",
                    "  Dan bedakan dua situasi ini, karena keduanya sering ditukar:",
                    "    Pemakai MEMINTA bantuan (-h)  -> cetak ke stdout, exit 0. Ia dapat yang ia minta.",
                    "    Pemakai SALAH memanggil       -> pesan ke stderr, exit 2. Ini kegagalan.",
                    "  Kalau bantuan salah panggil dicetak ke stdout dengan exit 0, script yang memanggil",
                    "  script kamu akan mengira semuanya beres dan lanjut dengan data kosong.",
                    "",
                    "Daftar periksa saat membaca blok opsi di script orang lain:",
                    "  1. Huruf apa saja yang diterima, dan mana yang butuh nilai (lihat titik duanya).",
                    "  2. Ada shift $((OPTIND - 1)) tidak? Kalau tidak ada, $1 sesudahnya masih opsi.",
                    "  3. Opsi tak dikenal ditolak atau didiamkan?",
                    "  4. Apa nilai bawaan tiap variabel sebelum perulangan - itulah perilaku tanpa opsi.",
                ],
            },
        ],
    },
    {
        "title": "15. Pola: Glob dan Regex",
        "sections": [
            {
                "body": [
                    "Di bash ada DUA bahasa pola yang berbeda. Bentuknya mirip, artinya tidak, dan",
                    "keduanya adalah pasangan yang paling sering tertukar di seluruh shell.",
                    "",
                    "GLOB dipakai untuk NAMA BERKAS dan pencocokan sederhana:",
                    "  - nama berkas di baris perintah:  ls *.txt    rm foto?.jpg",
                    "  - pola di dalam 'case ... in'  (sudah kamu pakai di materi Percabangan)",
                    "  - operator == dan != di dalam [[ ]]",
                    "",
                    "REGEX dipakai untuk ISI TEKS:",
                    "  - operator =~ di dalam [[ ]]",
                    "  - grep, sed, dan awk",
                    "",
                    "JEBAKAN NOMOR SATU, dan ini betul-betul menjebak:",
                    "",
                    "  *  di GLOB  = 'apa saja, sepanjang apa pun, boleh kosong'",
                    "  *  di REGEX = 'nol kali atau lebih dari YANG TEPAT SEBELUMNYA'",
                    "",
                    "  ls data*          -> berkas yang namanya diawali 'data'",
                    "  grep 'data*' f    -> baris yang memuat 'dat' lalu nol atau lebih 'a'",
                    "                       jadi 'dat' saja sudah cocok. Bukan itu maksudmu.",
                    "",
                    "Tabel ini pantas dihafal:",
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
                    "Brace expansion {} sering dikira glob, padahal bukan:",
                    "  {jpg,png}   -> jpg png",
                    "  {1..5}      -> 1 2 3 4 5",
                    "  {01..03}    -> 01 02 03   (nol di depan ikut dipertahankan)",
                    "  Ia mekar LEBIH DULU dan tidak pernah melihat isi folder. Karena itu",
                    "  'echo bab-{a,b}.md' tetap mencetak dua nama walau berkasnya tidak ada.",
                    "",
                    "Kalau tidak ada satu pun berkas yang cocok, bash menyerahkan POLANYA APA ADANYA.",
                    "  Ini sumber bug klasik: 'for f in *.txt' tetap jalan satu putaran dengan f",
                    "  berisi teks '*.txt'. Penangkalnya sudah dipakai di materi Bekerja dengan",
                    "  File & Folder: [[ -e \"$f\" ]] || continue, atau shopt -s nullglob.",
                    "",
                    "Tiga hal kecil yang menghemat banyak kebingungan:",
                    "  - Pola yang DIKUTIP tidak mekar. ls \"*.txt\" mencari berkas bernama *.txt.",
                    "  - Berkas tersembunyi (namanya diawali titik) tidak pernah kena *.",
                    "  - Hasilnya diurutkan sebagai TEKS, bukan angka: foto10.jpg bisa muncul",
                    "    sebelum foto2.jpg.",
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
                    "Sekarang regex. Sekali kosakatanya masuk kepala, ia terpakai di =~, grep, sed,",
                    "awk, dan hampir semua bahasa pemrograman lain yang akan kamu temui.",
                    "",
                    "PENJANGKAR - menunjuk POSISI, bukan karakter:",
                    "  ^      awal baris.   ^andi cocok kalau baris DIMULAI dengan andi",
                    "  $      akhir baris.  txt$ cocok kalau baris DIAKHIRI txt",
                    "  ^...$  dipakai berpasangan artinya: SELURUH teks harus persis begini",
                    "",
                    "KARAKTER - masing-masing mewakili satu huruf:",
                    "  .          satu karakter apa pun",
                    "  [abc]      satu dari a, b, c",
                    "  [^abc]     satu karakter selain a, b, c   (regex pakai ^, glob pakai !)",
                    "  [a-z0-9]   rentang, boleh digabung",
                    "  \\          matikan arti khusus karakter sesudahnya",
                    "",
                    "PENGULANGAN - selalu mengacu ke SATU HAL DI SEBELAH KIRINYA:",
                    "  *      nol kali atau lebih",
                    "  +      satu kali atau lebih",
                    "  ?      nol atau satu kali (boleh ada, boleh tidak)",
                    "  {3}    tepat 3 kali",
                    "  {2,}   2 kali atau lebih",
                    "  {2,5}  antara 2 sampai 5 kali",
                    "",
                    "  ab*     -> a, ab, abbb        yang diulang cuma huruf b",
                    "  (ab)*   -> kosong, ab, ababab   yang diulang seluruh grup",
                    "  Salah membaca 'yang sebelumnya' inilah asal sebagian besar regex yang rusak.",
                    "",
                    "GRUP DAN PILIHAN:",
                    "  ( )    kelompokkan, sekaligus TANGKAP isinya supaya bisa diambil lagi",
                    "  |      atau.  ^(ya|tidak)$ cocok untuk 'ya' maupun 'tidak'",
                    "",
                    "TITIK ADALAH JEBAKAN PALING MAHAL DI REGEX:",
                    "  ^data.txt$    dibaca 'data', SATU KARAKTER APA PUN, lalu 'txt'.",
                    "                Jadi dataXtxt dan data-txt ikut dianggap cocok.",
                    "  ^data\\.txt$   barulah berarti titik yang sungguhan titik.",
                    "",
                    "  Pola yang lupa di-escape tidak error dan tidak protes. Ia cuma diam-diam",
                    "  menerima terlalu banyak, dan kamu baru sadar berbulan-bulan kemudian.",
                    "  Yang perlu di-escape kalau dimaksud harfiah:  . * + ? ( ) [ ] { } | ^ $ \\",
                    "",
                    "KELAS SIAP PAKAI, ditulis dengan kurung siku berlapis:",
                    "  [[:digit:]]   angka         setara [0-9]",
                    "  [[:alpha:]]   huruf         setara [A-Za-z]",
                    "  [[:alnum:]]   huruf & angka",
                    "  [[:space:]]   spasi, tab, baris baru",
                    "  [[:upper:]] [[:lower:]] [[:punct:]]",
                    "",
                    "  Kurung siku LUAR tetap kurung siku kelas karakter. Jadi 'angka atau titik'",
                    "  ditulis [[:digit:].] -- bukan [:digit:.]",
                    "  Bedanya dengan [0-9]: kelas POSIX ikut aturan bahasa sistem, sedangkan",
                    "  [0-9] selalu persis sepuluh angka ASCII itu saja.",
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
                    "Perhatikan tiga aturan dari contoh tadi, karena ketiganya sering bikin orang buntu:",
                    "  - Polanya TIDAK boleh dibungkus petik ganda. Begitu dikutip, bash membacanya",
                    "    sebagai teks harfiah dan =~ berubah jadi sekadar pembanding string.",
                    "  - Teks di sebelah KIRI justru sebaiknya dikutip, seperti biasa.",
                    "  - Menaruh pola di variabel lalu memakainya tanpa kutip adalah cara paling",
                    "    aman dan paling enak dibaca. Itu yang dilakukan fungsi cocok() di atas.",
                    "",
                    "Sekarang bagian yang menjelaskan backslash-backslash aneh di kode orang lain.",
                    "grep dan sed lahir sebelum regex punya bentuk baku, jadi ada DUA dialek:",
                    "",
                    "  BRE (Basic Regular Expression) - mode bawaan grep dan sed",
                    "      + ? { } ( ) | TIDAK istimewa. Supaya jadi metakarakter harus di-escape:",
                    "      \\+   \\?   \\{2,\\}   \\(   \\)   \\|",
                    "  ERE (Extended Regular Expression) - grep -E, sed -E, dan awk",
                    "      + ? { } ( ) | langsung istimewa, tanpa backslash sama sekali.",
                    "",
                    "Jadi dua baris ini artinya sama persis:",
                    "  grep 'a\\+' berkas",
                    "  grep -E 'a+' berkas",
                    "",
                    "Di BRE backslash terasa terbalik: \\( berarti grup, sedangkan ( cuma kurung",
                    "biasa. Di ERE justru sebaliknya. Itu sebabnya pola yang disalin dari contoh",
                    "grep sering mati begitu ditempel ke awk, dan sebaliknya.",
                    "",
                    "  bash [[ =~ ]]  -> ERE",
                    "  awk            -> ERE, tidak punya mode lain",
                    "  grep dan sed   -> BRE, kecuali diberi -E",
                    "",
                    "  Catatan: \\+ dan \\? di BRE adalah tambahan GNU, bukan POSIX. Di grep bawaan",
                    "  macOS atau BusyBox belum tentu ada. Kalau ragu, pakai -E.",
                    "",
                    "Membangun pola itu menyusun, bukan menyalin. Naikkan setingkat demi setingkat:",
                    "  ^[0-9]+$                  seluruh teks angka semua",
                    "  ^-?[0-9]+$                boleh ada tanda minus di depan",
                    "  ^-?[0-9]+(\\.[0-9]+)?$     boleh berdesimal, dan bagian desimalnya opsional",
                    "  ^[A-Za-z_][A-Za-z0-9_]*$  nama variabel: huruf/_ dulu, sisanya bebas",
                    "",
                    "  Pola terakhir menjelaskan karakter PERTAMA dan SISANYA secara terpisah.",
                    "  Cara pikir itu terpakai berulang kali di regex sungguhan.",
                    "",
                    "Di bawah, pola yang sama dijalankan lewat grep, sed, dan awk -- tiga alat yang",
                    "dibahas tuntas di materi berikutnya. Yang berubah cuma alatnya, bukan polanya.",
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
                    "Bash punya banyak operasi string bawaan lewat ${}.",
                    "Ini lebih cepat daripada memanggil program luar seperti sed.",
                    "",
                    "Panjang string:",
                    "  ${#teks}",
                    "",
                    "Menyambung string:",
                    "  lengkap=\"$depan $belakang\"    rakit langsung di dalam petik",
                    "  pesan=\"Halo\"",
                    "  pesan+=\" dunia\"               tempel di BELAKANG isi yang ada",
                    "",
                    "  += di situ arti KETIGA dari tanda yang sama. Di dalam (( )) ia",
                    "  menjumlahkan angka, pada array ia menambah elemen, pada string",
                    "  biasa ia menempel teks. Yang menentukan bukan tandanya, melainkan",
                    "  SIFAT variabelnya - bukan isinya. Variabel biasa yang kebetulan",
                    "  berisi angka tetap DITEMPEL, bukan dijumlahkan: n=0 lalu n+=1",
                    "  memberi \"01\", bukan 1. Cara membuat variabel yang benar-benar",
                    "  dihitung sebagai angka ada di materi Fitur Bash Lanjutan.",
                    "",
                    "  Pola yang paling sering butuh += adalah mengumpulkan hasil di",
                    "  dalam perulangan, sepotong demi sepotong (bentuk ${kata:i:1} di",
                    "  bawah ini dijelaskan di bagian Substring tepat sesudah blok ini):",
                    "    terbalik=\"\"",
                    "    for (( i = ${#kata} - 1; i >= 0; i-- )); do",
                    "        terbalik+=\"${kata:i:1}\"",
                    "    done",
                    "",
                    "Substring (potong):",
                    "  ${teks:4}       mulai indeks 4 sampai akhir",
                    "  ${teks:0:5}     mulai indeks 0, ambil 5 karakter",
                    "  ${teks: -3}     3 karakter terakhir (perhatikan spasi!)",
                    "",
                    "Ganti isi:",
                    "  ${teks/lama/baru}    ganti kemunculan PERTAMA",
                    "  ${teks//lama/baru}   ganti SEMUA kemunculan",
                    "  ${teks/#awal/baru}   ganti kalau ada di awal",
                    "  ${teks/%akhir/baru}  ganti kalau ada di akhir",
                    "",
                    "Buang pola:",
                    "  ${berkas%.txt}       buang '.txt' dari akhir (terpendek)",
                    "  ${berkas%%.*}        buang dari titik pertama (terpanjang)",
                    "  ${jalur#*/}          buang sampai '/' pertama dari awal",
                    "  ${jalur##*/}         buang sampai '/' terakhir -> nama file",
                    "",
                    "Ubah huruf besar/kecil (bash 4+):",
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
                    "Nilai bawaan dan validasi:",
                    "  ${var:-bawaan}   pakai 'bawaan' KALAU var kosong",
                    "  ${var:=bawaan}   sama, TAPI sekalian set var-nya",
                    "  ${var:?pesan}    error dengan 'pesan' kalau var kosong",
                    "  ${var:+isi}      pakai 'isi' KALAU var TIDAK kosong",
                    "",
                    "Sangat berguna untuk konfigurasi:",
                    "  PORT=\"${PORT:-8080}\"",
                    "  Artinya: pakai PORT dari environment, kalau tidak ada pakai 8080.",
                    "",
                    "Perbandingan pola dengan regex:",
                    "  if [[ \"$email\" =~ ^[a-z]+@[a-z]+\\.[a-z]+$ ]]; then",
                    "      echo \"Format email valid\"",
                    "  fi",
                    "",
                    "  Hasil tangkapan grup ada di array BASH_REMATCH:",
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
                    "Perintah dasar yang paling sering dipakai di script:",
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
                    "  basename /home/andi/laporan.txt   -> laporan.txt",
                    "  dirname  /home/andi/laporan.txt   -> /home/andi",
                    "",
                    "  Bash punya padanan bawaan untuk basename dan dirname, yaitu",
                    "  ${jalur##*/} dan ${jalur%/*} dari materi Operasi String. Bentuk",
                    "  bawaan lebih cepat karena tidak memanggil program luar; basename",
                    "  dan dirname lebih terbaca. Keduanya lazim dipakai.",
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
                    "Kalau tidak ada file .txt sama sekali, bash memberikan pola",
                    "mentah '*.txt' sebagai nama file. Pengecekan -e mencegah",
                    "script memproses nama file palsu itu.",
                    "",
                    "Alternatif: aktifkan nullglob di awal script",
                    "  shopt -s nullglob",
                    "Dengan itu, pola tanpa hasil menjadi daftar kosong.",
                    "",
                    "Membuat file sementara dengan aman:",
                    "  tmp=$(mktemp)",
                    "  trap 'rm -f \"$tmp\"' EXIT",
                    "",
                    "  trap menjalankan perintah saat script berakhir, termasuk",
                    "  kalau dihentikan paksa. Ini cara benar membersihkan file",
                    "  sementara supaya tidak menumpuk.",
                    "",
                    "  EXIT cuma SATU dari sekumpulan kejadian yang bisa ditangkap trap.",
                    "  Yang juga sering dipakai:",
                    "    INT    pemakai menekan Ctrl-C",
                    "    TERM   permintaan berhenti baik-baik, misalnya dari kill",
                    "    ERR    ada perintah yang gagal",
                    "  Boleh beberapa sekaligus: trap bersihkan EXIT INT TERM. Seluk-",
                    "  beluknya ada di materi Proses Latar Belakang, Sinyal, dan trap.",
                    "",
                    "Perhatikan juga bentuk pada contoh di atas:",
                    "  baris=$(wc -l < \"$berkas\")",
                    "",
                    "Kenapa pakai < dan bukan wc -l \"$berkas\"? Karena jawabannya beda:",
                    "  wc -l catatan.txt    ->  3 catatan.txt     angka DAN nama berkas",
                    "  wc -l < catatan.txt  ->  3                 angkanya saja",
                    "",
                    "Dengan <, wc tidak pernah tahu nama berkasnya - ia cuma menerima",
                    "isinya lewat stdin, jadi tidak ada nama yang bisa ikut dicetak.",
                    "Kalau angkanya mau dihitung atau dicetak sendiri, selalu pakai",
                    "bentuk <. Bentuk tanpa < berguna justru saat kamu MEMANG ingin",
                    "namanya ikut, misalnya wc -l *.txt untuk membandingkan banyak berkas.",
                ]
            },
        ],
    },
    {
        "title": "18. find, xargs, dan Pemrosesan Massal",
        "sections": [
            {
                "body": [
                    "Sejauh ini kamu mencari berkas dengan pola glob: for berkas in *.txt.",
                    "Glob cuma melihat SATU tingkat folder. Begitu berkasnya tersebar di anak",
                    "folder dan cucu folder, glob berhenti menolong.",
                    "",
                    "find menyusuri SELURUH pohon folder, lalu menyaring hasilnya dengan PREDIKAT.",
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
                    "  -size +10M       lebih besar dari 10 MB  (+ lebih dari, - kurang dari, k/M/G)",
                    "  -empty           berukuran nol",
                    "  -mtime +7        terakhir diubah LEBIH DARI 7x24 jam lalu (-7 = kurang dari)",
                    "  -mmin -30        terakhir diubah kurang dari 30 menit lalu",
                    "  -newer patokan   lebih baru daripada berkas bernama 'patokan'",
                    "  -user levi       milik pemakai tertentu",
                    "",
                    "JEBAKAN PERTAMA, dan hampir semua orang kena sekali: petik di -name.",
                    "",
                    "  find . -name *.log      SALAH",
                    "  find . -name '*.log'    BENAR",
                    "",
                    "  Tanpa petik, *.log dimakan SHELL lebih dulu (lihat materi Variabel &",
                    "  Quoting), dan find tidak pernah melihat polanya.",
                    "",
                    "  Kalau di folder saat ini kebetulan ada SATU berkas .log, find menerima",
                    "  nama berkas itu sebagai polanya. Semua .log di anak folder dilewatkan",
                    "  diam-diam, tanpa satu pun pesan error. Ini jenis bug yang paling mahal:",
                    "  perintahnya sukses, angkanya salah.",
                    "",
                    "  Kalau ada DUA atau lebih, find berhenti dengan:",
                    "    find: paths must precede expression: 'c.log'",
                    "    find: possible unquoted pattern after predicate '-name'?",
                    "  Baris keduanya itu petunjuk yang sesungguhnya. Masalahnya memang sudah",
                    "  selesai terjadi sebelum find sempat jalan.",
                    "",
                    "Menggabungkan predikat:",
                    "  -a          DAN  (boleh dihilangkan: dua predikat berdampingan sudah DAN)",
                    "  -o          ATAU",
                    "  !           BUKAN",
                    "  \\( ... \\)   tanda kurung untuk mengatur urutan",
                    "",
                    "  find . -type f -name '*.sh' -o -name '*.md'",
                    "    Dibaca: (berkas DAN *.sh) ATAU (*.md). Folder bernama *.md ikut kena.",
                    "  find . -type f \\( -name '*.sh' -o -name '*.md' \\)",
                    "    Baru ini yang kamu maksud: berkas, yang namanya *.sh atau *.md.",
                    "",
                    "  Kurungnya WAJIB di-escape. ( dan ) polos adalah sintaks subshell milik",
                    "  bash, jadi find tidak akan pernah melihatnya. Bentuk '(' berpetik sama sah.",
                    "",
                    "Terakhir, dan sering bikin heran: URUTAN HASIL find TIDAK DIJAMIN. Ia",
                    "mengikuti urutan direktori di sistem berkas, yang bisa beda antar mesin.",
                    "Kalau urutannya penting, sambung dengan | sort seperti di contoh berikut.",
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
                    "find tidak berhenti di mencetak nama. Ia bisa MENJALANKAN sesuatu untuk",
                    "tiap hasil, dan bentuknya ada dua.",
                    "",
                    "  -exec perintah {} \\;",
                    "    {} diganti nama berkas yang ketemu. Perintahnya dipanggil SEKALI PER",
                    "    BERKAS. Seribu berkas berarti seribu proses: benar, tapi lambat.",
                    "",
                    "  -exec perintah {} +",
                    "    Nama-nama berkas ditumpuk jadi satu daftar panjang dan perintahnya",
                    "    dipanggil sesedikit mungkin -- biasanya cukup sekali. Ini yang kamu",
                    "    mau untuk grep, wc, rm, chmod.",
                    "",
                    "  Kenapa titik-komanya di-escape? ; adalah pemisah perintah milik bash.",
                    "  Tanpa \\, bash memotong barisnya di situ dan find tidak pernah tahu",
                    "  bagian -exec-nya sudah habis. Bentuk ';' berpetik sama sah. Tanda +",
                    "  tidak perlu diapa-apakan.",
                    "",
                    "  -delete   menghapus yang ketemu, tanpa memanggil rm sama sekali.",
                    "",
                    "KEBIASAAN YANG MENYELAMATKAN: jalankan find-nya TANPA aksi lebih dulu.",
                    "",
                    "  find . -name '*.tmp'            <- lihat dulu daftar korbannya",
                    "  find . -name '*.tmp' -delete    <- baru hapus, kalau daftarnya memang benar",
                    "",
                    "  -delete tidak bertanya, tidak bisa dibatalkan, dan tidak punya keranjang",
                    "  sampah. Satu salah ketik di polanya sudah cukup. Taruh juga -delete di",
                    "  PALING BELAKANG: find membaca predikat dari kiri ke kanan, jadi",
                    "  'find . -delete -name x' menghapus dulu, menyaring belakangan.",
                    "",
                    "XARGS -- dan ini kerjanya BEDA dari pipe biasa, bukan variasinya.",
                    "",
                    "  echo berkas.txt | cat          cat menerima TEKS 'berkas.txt' di stdin",
                    "                                 lalu mencetak teks itu. Berkasnya tak dibuka.",
                    "  echo berkas.txt | xargs cat    xargs menyusun perintah 'cat berkas.txt'",
                    "                                 lalu menjalankannya. Isi berkasnya keluar.",
                    "",
                    "Jadi: pipe memberi data ke STDIN; xargs mengubah data itu jadi ARGUMEN.",
                    "Banyak perintah (rm, mv, mkdir, chmod) tidak membaca stdin sama sekali --",
                    "buat mereka xargs bukan kemewahan, ia satu-satunya jalan.",
                    "",
                    "Opsi xargs yang perlu kamu kenal:",
                    "  -0        pemisahnya byte NUL, bukan spasi/baris. Pasangan dari -print0.",
                    "  -n 1      maksimal 1 argumen tiap panggilan (2, 3, ... juga boleh)",
                    "  -I{}      taruh argumennya di posisi {} yang kamu pilih; otomatis -n 1",
                    "  -P 4      jalankan 4 panggilan sekaligus. Cepat, tapi keluarannya bisa",
                    "            saling menyela dan urutannya tidak lagi terjamin.",
                    "  -r        jangan jalankan apa pun kalau masukannya kosong. Tanpa ini,",
                    "            GNU xargs tetap memanggil perintahnya sekali tanpa argumen.",
                    "",
                    "PASANGAN PENGAMAN untuk nama berkas berspasi:",
                    "  find . -name '*.log' -print0 | xargs -0 rm --",
                    "",
                    "  Secara bawaan xargs memotong masukannya di SETIAP spasi. Nama 'laporan",
                    "  akhir.log' jadi dua argumen, dan rm menghapus apa pun yang kebetulan",
                    "  bernama 'laporan'. -print0 memisahkan nama dengan byte NUL -- satu-satunya",
                    "  byte yang tidak boleh muncul di dalam nama berkas -- dan -0 menyuruh",
                    "  xargs memakai pemisah itu. Ini aturan yang sama yang sudah kamu pakai",
                    "  sejak \"$berkas\": nama boleh berisi spasi, dan kodemu harus tetap benar.",
                    "",
                    "Kapan pakai yang mana? Kalau sumbernya memang find, -exec ... + biasanya",
                    "lebih pendek dan sudah aman tanpa trik NUL. xargs menang kalau sumbernya",
                    "BUKAN find (keluaran grep -l, isi sebuah berkas daftar) atau kalau kamu",
                    "butuh -P untuk kerja paralel.",
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
                    "Process substitution: <(perintah) berlaku persis seperti NAMA BERKAS.",
                    "",
                    "  Bash menjalankan perintahnya di latar, lalu menyerahkan jalur semu seperti",
                    "  /dev/fd/63 kepada perintah luar. Perintah luar mengira ia membuka berkas",
                    "  biasa. Ini menutup seluruh kasus 'perintah ini maunya berkas, sedangkan",
                    "  yang aku punya cuma keluaran perintah lain'.",
                    "",
                    "  diff <(sort a.txt) <(sort b.txt)   membandingkan tanpa 2 berkas sementara",
                    "  comm <(sort a.txt) <(sort b.txt)   melihat mana yang cuma ada di salah satu",
                    "",
                    "  >(perintah) arahnya kebalikan: yang DITULIS ke situ jadi stdin perintah",
                    "  itu. Contoh: perintah > >(gzip > catatan.gz)",
                    "",
                    "  Keduanya fitur bash, bukan sh. Script dengan shebang #!/bin/sh akan gagal.",
                    "",
                    "Ini juga jawaban dari jebakan pipe yang sudah kamu temui di materi Proses,",
                    "source, dan Subshell: perulangan di sisi kanan pipe jalan di subshell, jadi",
                    "variabel yang diubah di dalamnya lenyap begitu pipe selesai. Kalau sumbernya",
                    "berkas, obatnya < berkas. Kalau sumbernya PERINTAH, obatnya ini:",
                    "",
                    "  while IFS= read -r baris; do ... done < <(perintah)",
                    "",
                    "  Perhatikan SPASI di antara < dan <(. Kalau dirapatkan jadi <<, itu heredoc",
                    "  dan bash langsung mengeluh soal delimiter.",
                    "",
                    "mapfile (nama lainnya readarray) mengisi array dari baris-baris sekaligus:",
                    "  mapfile -t buah < daftar.txt",
                    "  mapfile -t berkas < <(find . -name '*.md' | sort)",
                    "",
                    "  -t membuang karakter baris-baru di ujung tiap item. Tanpa -t, tiap item",
                    "  masih menyimpan \\n di belakangnya dan perbandingan seperti",
                    "  [[ ${buah[0]} == apel ]] gagal tanpa alasan yang kelihatan.",
                    "",
                    "  mapfile butuh bash 4+. Kalau harus jalan di bash 3.2 bawaan macOS,",
                    "  kembali ke while read dengan array+=(\"$baris\") di dalamnya.",
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
                    "Tiga alat teks klasik. Menguasai ini melipatgandakan",
                    "kemampuan scripting kamu.",
                    "",
                    "GREP - mencari baris yang cocok",
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
                    "SED - stream editor, mengganti teks",
                    "  sed 's/lama/baru/' file      ganti pertama tiap baris",
                    "  sed 's/lama/baru/g' file     ganti SEMUA (g = global)",
                    "  sed -i 's/a/b/g' file        ubah file LANGSUNG",
                    "  sed -n '5p' file             cetak baris ke-5 saja",
                    "  sed '2d' file                hapus baris ke-2",
                    "  sed '/pola/d' file           hapus baris yang cocok pola",
                    "",
                    "AWK - pengolah data berkolom",
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
                    "Heredoc menulis blok teks banyak baris ke file atau perintah.",
                    "  << 'EOF'  dengan petik  -> isi apa adanya, $variabel TIDAK diproses",
                    "  << EOF    tanpa petik   -> $variabel DIPROSES",
                    "  <<- EOF   tanda minus   -> tab di awal baris diabaikan",
                    "",
                    "Penanda EOF boleh diganti kata lain, asal konsisten.",
                    "",
                    "Jangan tertukar dengan <<< (here-string) dari materi Aliran Data &",
                    "Deskriptor. Yang membedakan cuma BANYAKNYA tanda kurang-dari, dan",
                    "keduanya mirip sekali sampai saling menyamarkan:",
                    "  <<  EOF      blok BANYAK baris, ditutup penanda di baris sendiri",
                    "  <<< \"teks\"   SATU string, ditulis di baris yang sama",
                    "Keduanya sama-sama menyuapi stdin sebuah perintah; yang beda cuma",
                    "seberapa banyak teks yang disuapkan.",
                    "",
                    "Variabel bawaan awk yang berguna:",
                    "  $0    seluruh baris",
                    "  $1..  kolom ke-n",
                    "  NF    jumlah kolom di baris ini",
                    "  NR    nomor baris saat ini",
                    "  FS    pemisah kolom input",
                    "  OFS   pemisah kolom output",
                    "",
                    "  awk '{print NR, NF, $NF}' file",
                    "  -> cetak nomor baris, jumlah kolom, dan kolom TERAKHIR",
                ]
            },
        ],
    },
    {
        "title": "20. Proses Latar Belakang, Sinyal, dan trap",
        "sections": [
            {
                "body": [
                    "Perintah biasa MENAHAN shell: kamu tidak dapat giliran lagi sampai ia selesai.",
                    "Satu & di ujung baris mengubah itu.",
                    "",
                    "  ./laporan.sh      shell menunggu sampai selesai, baru lanjut",
                    "  ./laporan.sh &    shell melepasnya jalan sendiri, lalu LANGSUNG ke baris berikutnya",
                    "",
                    "& dan && cuma beda satu huruf, dan tidak ada hubungannya sama sekali:",
                    "",
                    "  a && b    jalankan b KALAU a sukses  (materi Argumen & Exit Code)",
                    "  a & b     lepas a ke latar belakang, lalu langsung jalankan b",
                    "",
                    "  mkdir data && cd data    benar",
                    "  mkdir data & cd data     bug: cd jalan tanpa menunggu mkdir selesai",
                    "",
                    "Salah ketik ini tidak pernah memberi pesan error. Ia cuma kadang-kadang gagal,",
                    "tergantung siapa yang kebetulan lebih cepat. Begitu melihat satu & di tempat yang",
                    "kamu kira && , curigai itu lebih dulu.",
                    "",
                    "Proses latar belakang tetap ANAK dari shell-mu -- lihat materi Proses, source, dan",
                    "Subshell. Ia mewarisi layar yang sama, jadi keluarannya tetap muncul, bercampur",
                    "dengan keluaran yang lain, kadang di tengah baris. Kalau ada beberapa, beri",
                    "masing-masing berkas lognya sendiri:",
                    "  ./tugas.sh satu > tugas-1.log 2>&1 &",
                    "  ./tugas.sh dua  > tugas-2.log 2>&1 &",
                    "",
                    "$! berisi PID proses latar belakang yang PALING BARU dilepas. Ia melengkapi",
                    "keluarga variabel khusus dari materi Variabel & Quoting:",
                    "",
                    "  $?   kode keluar perintah terakhir       $#   jumlah argumen",
                    "  $@   semua argumen                       $$   PID script ini sendiri",
                    "  $!   PID proses latar belakang terakhir",
                    "",
                    "Simpan SEGERA. Satu & berikutnya langsung menimpanya:",
                    "  ./server.sh &",
                    "  pid=$!         <- wajib persis di baris sesudahnya, bukan tiga baris kemudian",
                    "",
                    "wait menahan script sampai anak-anaknya selesai:",
                    "",
                    "  wait           tunggu SEMUA proses latar belakang; kodenya selalu 0",
                    "  wait \"$pid\"    tunggu satu proses, dan $? jadi kode keluar proses ITU",
                    "  wait -n        tunggu yang mana pun selesai duluan (bash 4.3+)",
                    "",
                    "Baca ulang baris pertama: wait polos tidak pernah memberi tahu ada yang gagal.",
                    "Bahkan set -e pun diam soal proses latar belakang -- kegagalannya terjadi di proses",
                    "lain, dan shell-mu tidak pernah melihatnya. Satu-satunya cara tahu adalah wait",
                    "per-PID lalu memeriksa $? sendiri, seperti di contoh berikutnya.",
                    "",
                    "Tanpa wait sama sekali, script yang selesai duluan meninggalkan anak-anaknya",
                    "setengah jalan. Hampir selalu wait yang kamu mau.",
                    "",
                    "Tiga perintah pendamping yang cuma berguna di terminal INTERAKTIF, bukan di script:",
                    "",
                    "  jobs      daftar pekerjaan shell ini, bernomor [1] [2] ...",
                    "  fg %1     tarik pekerjaan 1 kembali ke depan",
                    "  bg %1     lanjutkan pekerjaan yang sedang dijeda, kali ini di latar belakang",
                    "  Ctrl-Z    jeda pekerjaan yang sedang di depan, lalu pilih fg atau bg",
                    "",
                    "[1] itu nomor JOB, bukan PID: %1 dipakai jobs, fg, bg, dan kill; sedangkan PID",
                    "dari $! dipakai di mana saja. Di dalam script, jobs biasanya kosong dan fg tidak",
                    "ada gunanya -- tidak ada 'depan' kalau tidak ada orang yang menonton.",
                ],
            },
            {
                "heading": "Pola paralel: &, $!, lalu wait per-PID",
                "body": [
                    "Alasan utama orang berhenti mengerjakan sesuatu satu per satu: tiga pemeriksaan",
                    "yang masing-masing lambat tidak perlu antre. Awasi urutan keluarannya -- yang",
                    "dilepas PERTAMA justru selesai TERAKHIR, dan itulah buktinya mereka jalan bareng.",
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
                    "SINYAL adalah pesan sangat pendek dari kernel ke sebuah proses: cuma satu nama,",
                    "tanpa isi. Semacam ketukan pintu. Yang diketuk masih boleh menyiapkan diri --",
                    "menyimpan pekerjaan, menghapus berkas sementara -- sebelum benar-benar berhenti.",
                    "",
                    "  Nama  Nomor  Datang dari                              Bisa ditangkap?",
                    "  INT     2    kamu menekan Ctrl-C                      ya",
                    "  TERM   15    kill tanpa opsi; permintaan yang sopan   ya",
                    "  HUP     1    terminal ditutup, sesi SSH putus         ya",
                    "  QUIT    3    Ctrl-\\                                   ya",
                    "  KILL    9    kill -9                                  TIDAK PERNAH",
                    "  STOP   19    jeda paksa                               TIDAK PERNAH",
                    "",
                    "KILL dan STOP tidak pernah sampai ke programnya; kernel yang mengerjakannya",
                    "sendiri. Karena itu kill -9 TIDAK memberi kesempatan membersihkan diri: berkas",
                    "sementara tertinggal, berkas yang baru setengah tertulis dibiarkan rusak, kunci",
                    "tidak dilepas. Jadikan kill -9 pilihan TERAKHIR, bukan yang pertama.",
                    "",
                    "Mengirim sinyal:",
                    "",
                    "  kill 12345         kirim TERM (bawaan). Ini yang selalu dicoba pertama.",
                    "  kill -TERM 12345   sama saja, ditulis terang-terangan",
                    "  kill -9 12345      kirim KILL; sama dengan kill -KILL 12345",
                    "  kill -0 12345      TIDAK mengirim apa-apa, cuma menjawab 'masih ada atau tidak'",
                    "  kill -l            daftar semua nama sinyal di sistemmu",
                    "",
                    "Nama kill menyesatkan: yang ia lakukan adalah MENGIRIM SINYAL, tidak selalu",
                    "membunuh. kill -0 di atas contohnya -- ia justru dipakai untuk memeriksa.",
                    "",
                    "Kalau yang kamu tahu cuma namanya, bukan PID-nya:",
                    "  pgrep -f 'server.py'   cetak PID semua proses yang cocok",
                    "  pkill -f 'server.py'   kirim TERM ke semuanya sekaligus",
                    "",
                    "  Selalu pgrep dulu dan baca daftarnya, baru pkill. -f mencocokkan SELURUH baris",
                    "  perintah, bukan cuma nama programnya, jadi pola yang longgar bisa ikut",
                    "  membunuh editor atau terminal yang kebetulan memuat kata itu di judulnya.",
                    "",
                    "Menutup terminal mengirim HUP ke semua yang jalan di dalamnya. Proses latar",
                    "belakang ikut mati -- inilah sebabnya './lama.sh &' lalu logout sering berakhir",
                    "sia-sia, dan orang menyangka scriptnya yang rusak.",
                    "",
                    "  nohup ./lama.sh &                    kebal HUP; keluarannya ke nohup.out",
                    "  nohup ./lama.sh > jalan.log 2>&1 &   lebih rapi: tentukan sendiri lognya",
                    "  disown -h %1                         untuk yang TERLANJUR jalan tanpa nohup",
                    "",
                    "Untuk yang serius -- harus hidup lagi setelah mesin reboot -- jawabannya bukan",
                    "nohup, melainkan systemd, supervisor, atau tmux/screen.",
                    "",
                    "Proses yang mati karena sinyal nomor N memberi exit code 128 + N. Angka-angka",
                    "yang akan sering kamu temui saat membaca log atau hasil CI:",
                    "",
                    "  130 = 128 + 2    dihentikan Ctrl-C (INT)",
                    "  143 = 128 + 15   dihentikan kill biasa (TERM)",
                    "  137 = 128 + 9    dihentikan kill -9. Di Docker hampir selalu kehabisan memori.",
                    "  124              perintah timeout menyerah karena waktunya habis",
                    "  127              perintah tidak ditemukan: salah ketik, atau tidak ada di PATH",
                    "  126              berkasnya ada tapi tidak boleh dieksekusi (materi Izin Berkas)",
                ],
            },
            {
                "heading": "trap: memasang penangan lebih dulu",
                "body": [
                    "trap memasang penangan: 'kalau kejadian ini datang, kerjakan ini dulu'.",
                    "",
                    "  trap 'perintah' KEJADIAN [KEJADIAN ...]",
                    "  trap nama_fungsi KEJADIAN",
                    "",
                    "Kejadiannya boleh nama sinyal (INT, TERM, HUP) dan boleh kejadian buatan bash:",
                    "  EXIT    script berakhir, DENGAN CARA APA PUN",
                    "  ERR     ada perintah yang mengembalikan kode bukan 0",
                    "  DEBUG   sebelum setiap perintah; alat pelacak, jarang dipakai sehari-hari",
                    "",
                    "Materi Bekerja dengan File & Folder sudah memakai satu bentuknya:",
                    "  tmp=$(mktemp)",
                    "  trap 'rm -f \"$tmp\"' EXIT",
                    "",
                    "Yang belum disebut di sana: EXIT memang seluas namanya. Ia ikut jalan saat script",
                    "kena Ctrl-C dan saat kena kill biasa, bukan cuma saat selesai normal. Satu-satunya",
                    "yang lolos adalah kill -9, dan itu memang tidak bisa ditangkap siapa pun.",
                    "",
                    "Lalu kenapa banyak script menulis 'trap bersihkan EXIT INT TERM'? Karena",
                    "penulisnya mengira EXIT tidak cukup. Akibatnya nyata: saat Ctrl-C, bersihkan jalan",
                    "DUA KALI -- sekali dari trap INT, sekali lagi dari trap EXIT. Dengan rm -f tidak",
                    "ada yang kelihatan salah; dengan handler yang mencetak laporan atau mengirim",
                    "notifikasi, barulah ketahuan.",
                    "",
                    "Dua aturan yang menyelamatkan:",
                    "",
                    "  1. Pasang trap SEBELUM hal yang perlu dibersihkan bisa gagal, bukan sesudahnya.",
                    "  2. Handler pembersih harus AMAN dijalankan dua kali: rm -f, kill 2>/dev/null,",
                    "     mkdir -p. Kalau tidak bisa dibuat begitu, cabut trap-nya sendiri.",
                    "",
                    "Mencabut trap yang sudah dipasang:",
                    "  trap - EXIT        kembalikan EXIT ke perilaku bawaan, tanpa penangan",
                    "  trap - INT TERM    boleh beberapa sekaligus",
                    "  trap -p            tampilkan trap apa saja yang sedang terpasang",
                    "",
                    "  bersihkan() { rm -rf \"$kerja\"; }",
                    "  trap bersihkan EXIT",
                    "  trap 'bersihkan; trap - EXIT; exit 130' INT    <- cabut EXIT supaya tidak dobel",
                    "",
                    "JEBAKAN TERBESAR: penangan sinyal yang tidak memanggil exit membuat script LANJUT",
                    "ke baris berikutnya seolah tidak terjadi apa-apa. Tulis trap 'echo dibatalkan' INT",
                    "lalu tekan Ctrl-C: pesannya muncul, dan script terus berjalan. Orang akan menekan",
                    "Ctrl-C berkali-kali sambil bingung kenapa tidak mau berhenti. Penangan yang memang",
                    "dimaksudkan menghentikan script WAJIB diakhiri exit.",
                    "",
                    "Angkanya jangan asal: pakai exit 130 untuk INT dan exit 143 untuk TERM, supaya",
                    "siapa pun yang membaca kode keluarnya tahu script ini berhenti karena sinyal.",
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
                    "Pola yang muncul di hampir semua script uji dan skrip demo: nyalakan sesuatu,",
                    "pakai, lalu pastikan ia mati -- termasuk kalau kamu menekan Ctrl-C di tengah.",
                    "",
                    "  ./server.sh &",
                    "  pid=$!",
                    "  trap 'kill \"$pid\" 2>/dev/null' EXIT",
                    "  ...pakai servernya...",
                    "  wait \"$pid\"     kalau memang mau menemani sampai server berhenti sendiri",
                    "",
                    "Urutannya penting: & dulu, $! langsung, baru trap. Trap yang dipasang sebelum",
                    "$pid ada akan mengirim kill ke string kosong dan mengeluh 'not enough arguments'.",
                    "",
                    "Satu jebakan yang memakan banyak waktu orang: kill \"$pid\" membunuh proses yang",
                    "kamu lepas, BUKAN cucu-cucunya. Kalau yang dilepas adalah script pembungkus yang",
                    "di dalamnya memanggil program lain, yang mati cuma pembungkusnya -- programnya",
                    "tetap hidup memegang port, dan percobaan berikutnya gagal dengan 'address already",
                    "in use'. Dua jalan keluar: pakai exec di pembungkus (materi Aliran Data &",
                    "Deskriptor) supaya PID-nya tidak berubah, atau ikut membereskan anaknya dengan",
                    "pkill -P \"$pid\".",
                    "",
                    "sleep menjeda script. Satuannya detik, dan pecahan diterima di Linux dan macOS:",
                    "  sleep 5      sleep 0.5      sleep 2m      sleep 1h",
                    "",
                    "Gunanya bukan 'memperlambat program', tapi memberi jeda di antara percobaan:",
                    "  - menunggu layanan siap sebelum menembaknya (persis contoh di bawah)",
                    "  - mengulang permintaan yang gagal, dengan jeda yang makin panjang tiap kali",
                    "  - polling: memeriksa berkas atau status berkala tanpa menghabiskan CPU",
                    "",
                    "Jangan menulis 'sleep 30' asal-asalan sebagai pengganti pengecekan. Di mesin",
                    "lambat tetap kurang, di mesin cepat cuma membuang waktu. Perulangan",
                    "periksa-lalu-jeda dengan batas jumlah percobaan selalu lebih baik.",
                    "",
                    "timeout membatasi perintah yang bisa menggantung selamanya:",
                    "  timeout 30 curl -s https://contoh.com   menyerah setelah 30 detik",
                    "  timeout 5s ./mungkin-macet.sh           satuan boleh ditulis: s m h d",
                    "  timeout -s KILL 5 ./bandel              kirim KILL, bukan TERM",
                    "  timeout -k 5 30 ./bandel                TERM dulu; 5 detik masih hidup, baru KILL",
                    "",
                    "Kode keluarnya 124 kalau waktunya habis. Itu satu-satunya cara membedakan",
                    "'gagal menjawab' dari 'tidak pernah menjawab'. Bungkus setiap perintah jaringan",
                    "di script yang jalan otomatis dengan timeout; tanpa itu, satu server yang diam",
                    "sanggup menggantung seluruh pipeline sampai ada manusia yang menyadarinya.",
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
