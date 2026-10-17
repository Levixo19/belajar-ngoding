FEDORA_EXERCISES = [
    {
        "title": "Latihan 1: Variabel & printf Berkolom",
        "difficulty": "Mudah",
        "question": [
            "Buat skrip yang menyimpan tiga variabel: distro=\"Fedora\",",
            "versi=44, dan basis=\"RPM\".",
            "Tampilkan ketiganya dengan printf, label rata kiri selebar",
            "8 karakter diikuti titik dua dan satu spasi.",
            "",
            "Keluaran yang diharapkan:",
            "  Distro  : Fedora",
            "  Versi   : 44",
            "  Basis   : RPM",
        ],
        "hints": [
            "Format berkolom dibahas di materi \"Skrip Otomasi: Menyatukan Semuanya\". Pakai printf, bukan echo, karena printf yang bisa mengatur lebar kolom.",
            "Mulai dengan shebang #!/usr/bin/env bash, simpan ketiga variabel, lalu panggil printf tiga kali dengan format yang sama: label rata kiri selebar 8 karakter, titik dua, satu spasi, lalu nilainya.",
            "Di format printf, %-8s berarti teks rata kiri dalam lebar 8 karakter. Contoh satu baris: printf '%-8s: %s\\n' \"Distro\" \"$distro\".",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

distro="Fedora"
versi=44
basis="RPM"

printf '%-8s: %s\\n' "Distro" "$distro"
printf '%-8s: %s\\n' "Versi" "$versi"
printf '%-8s: %s\\n' "Basis" "$basis"
""",
    },
    {
        "title": "Latihan 2: Membangun Struktur Direktori",
        "difficulty": "Mudah",
        "question": [
            "Buat skrip yang bekerja di direktori sementara hasil mktemp -d.",
            "Di dalamnya buat struktur: proyek/src, proyek/doc, proyek/uji",
            "dengan SATU perintah mkdir memakai brace expansion.",
            "Lalu buat berkas kosong proyek/src/main.sh.",
            "",
            "Tampilkan jumlah direktori dan jumlah berkas yang terbentuk",
            "di bawah proyek, lalu hapus direktori sementaranya.",
            "",
            "Keluaran yang diharapkan:",
            "  direktori: 4",
            "  berkas   : 1",
        ],
        "hints": [
            "Baca ulang bagian brace expansion di \"Membuat, Menyalin, Memindah & Menghapus\", lalu mktemp dan trap di \"Skrip Otomasi: Menyatukan Semuanya\".",
            "Buat direktori sementara dengan mktemp -d dan simpan namanya di variabel. Pasang trap EXIT yang menghapusnya, supaya tetap bersih walau skrip berhenti di tengah, lalu cd ke sana. Satu mkdir -p dengan kurung kurawal membuat ketiga subdirektori sekaligus, dan touch membuat berkasnya.",
            "find proyek -type d | wc -l menghitung direktori, termasuk proyek sendiri (makanya hasilnya 4). Ganti -type d jadi -type f untuk menghitung berkas.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT

cd "$kerja"
mkdir -p proyek/{src,doc,uji}
touch proyek/src/main.sh

printf 'direktori: %s\\n' "$(find proyek -type d | wc -l)"
printf 'berkas   : %s\\n' "$(find proyek -type f | wc -l)"
""",
    },
    {
        "title": "Latihan 3: Izin Berkas & Notasi Oktal",
        "difficulty": "Mudah",
        "question": [
            "Di direktori sementara, buat tiga berkas lalu setel izinnya:",
            "  rahasia.txt  jadi 600",
            "  skrip.sh     jadi 755",
            "  catatan.txt  jadi 644",
            "",
            "Tampilkan izin oktal dan nama tiap berkas, diurutkan menurut nama,",
            "memakai stat dengan format '%a %n'.",
            "",
            "Keluaran yang diharapkan:",
            "  644 catatan.txt",
            "  600 rahasia.txt",
            "  755 skrip.sh",
        ],
        "hints": [
            "Baca ulang notasi oktal di \"Izin Berkas & Kepemilikan\". Ingat: 6 = rw-, 7 = rwx, 5 = r-x, 4 = r--.",
            "Buat ketiga berkas dengan touch, setel izinnya dengan chmod, lalu tampilkan dengan stat memakai format '%a %n' (izin oktal, lalu nama). Jangan andalkan urutan dari shell glob; urutkan hasilnya secara eksplisit.",
            "Lewatkan keluaran stat ke sort -k2 supaya urut menurut kolom kedua, yaitu namanya.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

touch rahasia.txt skrip.sh catatan.txt
chmod 600 rahasia.txt
chmod 755 skrip.sh
chmod 644 catatan.txt

stat -c '%a %n' rahasia.txt skrip.sh catatan.txt | sort -k2
""",
    },
    {
        "title": "Latihan 4: Memisahkan stdout dan stderr",
        "difficulty": "Mudah",
        "question": [
            "Buat fungsi bernama lapor yang menulis pesan biasa ke stdout",
            "dan fungsi galat yang menulis ke stderr dengan awalan 'GALAT: '.",
            "",
            "Panggil lapor dua kali dan galat satu kali, lalu buktikan",
            "pemisahannya: arahkan stdout ke berkas keluar.txt dan stderr ke",
            "berkas galat.txt, lalu tampilkan jumlah baris masing-masing.",
            "",
            "Keluaran yang diharapkan:",
            "  stdout: 2 baris",
            "  stderr: 1 baris",
        ],
        "hints": [
            "Baca ulang \"Pipa, Redirect & Aliran Data\": stdout dan stderr adalah dua aliran terpisah yang bisa diarahkan ke tempat berbeda.",
            "Fungsi galat menulis lewat printf seperti lapor, tapi keluarannya dibelokkan ke stderr dengan >&2. Bungkus ketiga pemanggilan dalam { ... } supaya bisa di-redirect sekaligus: > untuk stdout dan 2> untuk stderr.",
            "Bentuknya { lapor a; galat b; } > keluar.txt 2> galat.txt. Sesudah itu wc -l < berkas memberi angkanya saja, tanpa nama berkas.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

lapor() {
    printf '%s\\n' "$*"
}

galat() {
    printf 'GALAT: %s\\n' "$*" >&2
}

{
    lapor "memuat konfigurasi"
    lapor "memeriksa layanan"
    galat "repositori tidak terjangkau"
} > keluar.txt 2> galat.txt

printf 'stdout: %s baris\\n' "$(wc -l < keluar.txt)"
printf 'stderr: %s baris\\n' "$(wc -l < galat.txt)"
""",
    },
    {
        "title": "Latihan 5: Menyaring Log dengan grep",
        "difficulty": "Menengah",
        "question": [
            "Buat berkas layanan.log dengan isi persis berikut:",
            "",
            "  Sep 22 08:01:14 sshd: koneksi diterima dari 192.168.1.10",
            "  Sep 22 08:02:03 sshd: ERROR gagal otentikasi untuk budi",
            "  Sep 22 08:02:55 nginx: permintaan GET /index.html",
            "  Sep 22 08:03:41 sshd: ERROR gagal otentikasi untuk budi",
            "  Sep 22 08:04:19 nginx: ERROR berkas tidak ditemukan",
            "  Sep 22 08:05:02 sshd: koneksi ditutup",
            "",
            "Tampilkan tiga hal:",
            "  1. Jumlah baris yang mengandung ERROR",
            "  2. Jumlah baris dari sshd yang BUKAN ERROR",
            "  3. Nomor baris tiap ERROR, dipisah koma tanpa spasi",
            "",
            "Keluaran yang diharapkan:",
            "  error       : 3",
            "  sshd bersih : 2",
            "  baris error : 2,4,5",
        ],
        "hints": [
            "Baca ulang opsi grep di \"Mencari Berkas & Isi Berkas\", dan bagian here-document di \"Membaca Isi Berkas\".",
            "Tulis log-nya dengan here-document (cat > berkas dengan penanda <<'EOF'). grep -c menghitung baris yang cocok. Untuk sshd yang bukan ERROR, saring sshd dulu lalu buang ERROR dengan grep -v. Untuk nomor baris, grep -n memberi 'nomor:isi'.",
            "Ambil nomornya dengan cut -d: -f1, lalu gabungkan jadi satu baris berpemisah koma dengan paste -sd, (tr '\\n' ',' juga bisa, tapi meninggalkan koma di ujung dan membuang baris barunya).",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > layanan.log <<'EOF'
Sep 22 08:01:14 sshd: koneksi diterima dari 192.168.1.10
Sep 22 08:02:03 sshd: ERROR gagal otentikasi untuk budi
Sep 22 08:02:55 nginx: permintaan GET /index.html
Sep 22 08:03:41 sshd: ERROR gagal otentikasi untuk budi
Sep 22 08:04:19 nginx: ERROR berkas tidak ditemukan
Sep 22 08:05:02 sshd: koneksi ditutup
EOF

printf 'error       : %s\\n' "$(grep -c 'ERROR' layanan.log)"
printf 'sshd bersih : %s\\n' "$(grep 'sshd' layanan.log | grep -vc 'ERROR')"
printf 'baris error : %s\\n' "$(grep -n 'ERROR' layanan.log | cut -d: -f1 | paste -sd,)"
""",
    },
    {
        "title": "Latihan 6: Membedah Berkas Berpembatas",
        "difficulty": "Menengah",
        "question": [
            "Buat berkas pengguna.txt bergaya /etc/passwd berisi persis:",
            "",
            "  root:x:0:0:root:/root:/bin/bash",
            "  daemon:x:2:2:daemon:/sbin:/sbin/nologin",
            "  vi:x:1000:1000:Vi:/home/vi:/bin/bash",
            "  budi:x:1001:1001:Budi:/home/budi:/bin/bash",
            "  nginx:x:988:988:Nginx:/var/lib/nginx:/sbin/nologin",
            "  siti:x:1002:1002:Siti:/home/siti:/usr/bin/zsh",
            "",
            "Tampilkan:",
            "  1. Nama pengguna ber-UID 1000 ke atas, dipisah spasi",
            "  2. Jumlah akun yang shell-nya nologin",
            "  3. Daftar shell unik beserta jumlah pemakainya, terbanyak dulu",
            "",
            "Keluaran yang diharapkan:",
            "  manusia : vi budi siti",
            "  nologin : 2",
            "  shell:",
            "    3 /bin/bash",
            "    2 /sbin/nologin",
            "    1 /usr/bin/zsh",
        ],
        "hints": [
            "Berkas berpembatas titik dua dibahas di \"sed & awk\" dan \"Mengolah Teks: cut, sort, uniq, tr\".",
            "Untuk UID, minta awk memakai : sebagai pemisah dan mencetak kolom 1 kalau kolom 3 >= 1000, lalu gabungkan barisnya dengan paste -sd' '. nologin cukup dihitung dengan grep -c. Untuk shell, ambil kolom 7 dengan cut -d: -f7, lalu pakai idiom penghitung frekuensi.",
            "Idiomnya sort | uniq -c | sort -rn. Keluaran uniq -c punya spasi di depan angkanya; rapikan dengan awk yang mencetak $1 dan $2, dan perhatikan dua spasi di depan tiap baris pada keluaran yang diharapkan.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > pengguna.txt <<'EOF'
root:x:0:0:root:/root:/bin/bash
daemon:x:2:2:daemon:/sbin:/sbin/nologin
vi:x:1000:1000:Vi:/home/vi:/bin/bash
budi:x:1001:1001:Budi:/home/budi:/bin/bash
nginx:x:988:988:Nginx:/var/lib/nginx:/sbin/nologin
siti:x:1002:1002:Siti:/home/siti:/usr/bin/zsh
EOF

printf 'manusia : %s\\n' \\
    "$(awk -F: '$3 >= 1000 {print $1}' pengguna.txt | paste -sd' ')"
printf 'nologin : %s\\n' "$(grep -c 'nologin$' pengguna.txt)"

printf 'shell:\\n'
cut -d: -f7 pengguna.txt | sort | uniq -c | sort -rn |
    awk '{printf "  %s %s\\n", $1, $2}'
""",
    },
    {
        "title": "Latihan 7: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Buat berkas catatan.txt berisi persis:",
            "",
            "  Fedora memakai DNF dan RPM",
            "  DNF menggantikan YUM di Fedora",
            "  RPM adalah format paket Fedora",
            "",
            "Hitung frekuensi tiap kata tanpa membedakan huruf besar kecil,",
            "lalu tampilkan tiga kata terbanyak dalam format 'jumlah kata'.",
            "",
            "Keluaran yang diharapkan:",
            "  3 fedora",
            "  2 dnf",
            "  2 rpm",
        ],
        "hints": [
            "Ini idiom penghitung frekuensi dari \"Mengolah Teks: cut, sort, uniq, tr\".",
            "Pecah teks jadi satu kata per baris dengan tr -s ' ' '\\n', seragamkan hurufnya dengan tr 'A-Z' 'a-z', buang baris kosong, lalu sort | uniq -c. Urutkan menurut jumlah dan ambil tiga teratas dengan head -3.",
            "dnf dan rpm sama-sama muncul 2 kali. Supaya urutannya stabil saat seri, beri kunci kedua: sort -k1,1nr -k2,2. Rapikan spasi depan dari uniq -c dengan awk.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > catatan.txt <<'EOF'
Fedora memakai DNF dan RPM
DNF menggantikan YUM di Fedora
RPM adalah format paket Fedora
EOF

tr -s ' ' '\\n' < catatan.txt |
    tr 'A-Z' 'a-z' |
    grep -v '^$' |
    sort |
    uniq -c |
    sort -k1,1nr -k2,2 |
    head -3 |
    awk '{printf "%s %s\\n", $1, $2}'
""",
    },
    {
        "title": "Latihan 8: Membersihkan Berkas Konfigurasi",
        "difficulty": "Menengah",
        "question": [
            "Buat berkas layanan.conf berisi persis:",
            "",
            "  # Konfigurasi layanan",
            "  Port 22",
            "",
            "  # Batasi akses root",
            "  PermitRootLogin yes",
            "      # komentar menjorok",
            "  MaxAuthTries 6",
            "",
            "Dengan sed, hasilkan versi bersih tanpa baris komentar (termasuk",
            "yang menjorok) dan tanpa baris kosong. Lalu ganti nilai",
            "PermitRootLogin menjadi no dan Port menjadi 2222.",
            "",
            "Tampilkan hasil akhirnya.",
            "",
            "Keluaran yang diharapkan:",
            "  Port 2222",
            "  PermitRootLogin no",
            "  MaxAuthTries 6",
        ],
        "hints": [
            "Baca ulang \"sed & awk\": perintah d untuk menghapus baris, dan perintah c untuk mengganti seluruh baris.",
            "Hapus dua jenis baris: komentar (boleh diawali spasi) dan baris yang kosong atau cuma berisi spasi. Sesudah itu ganti baris Port dan PermitRootLogin. Beberapa perintah sed bisa dipisah titik koma atau beberapa -e, atau rantaikan dua sed dengan pipa kalau lebih mudah dibaca.",
            "Pola '^[[:space:]]*#' cocok dengan komentar walau menjorok, dan '^[[:space:]]*$' dengan baris kosong. Perintah c mengganti seluruh baris: sed '/^Port/c Port 2222'.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > layanan.conf <<'EOF'
# Konfigurasi layanan
Port 22

# Batasi akses root
PermitRootLogin yes
    # komentar menjorok
MaxAuthTries 6
EOF

sed -e '/^[[:space:]]*#/d' -e '/^[[:space:]]*$/d' layanan.conf |
    sed -e '/^Port/c Port 2222' -e '/^PermitRootLogin/c PermitRootLogin no'
""",
    },
    {
        "title": "Latihan 9: Laporan Disk dengan awk",
        "difficulty": "Menengah",
        "question": [
            "Buat berkas disk.txt yang meniru keluaran df -h:",
            "",
            "  Filesystem      Size  Used Avail Use% Mounted",
            "  /dev/nvme0n1p3  476G  391G   82G  83% /",
            "  /dev/nvme0n1p2  974M  286M  621M  32% /boot",
            "  /dev/nvme0n1p1  599M   20M  580M   4% /boot/efi",
            "  /dev/sdb1       1.8T  1.7T   94G  95% /data",
            "",
            "Dengan awk, lewati baris judul dan laporkan filesystem yang",
            "pemakaiannya di atas 80 persen, diurutkan dari yang paling penuh.",
            "Tutup dengan jumlah temuannya.",
            "",
            "Keluaran yang diharapkan:",
            "  /data 95%",
            "  / 83%",
            "  total penuh: 2",
        ],
        "hints": [
            "Baca ulang \"sed & awk\": NR untuk nomor baris, dan gsub untuk mengganti teks di dalam kolom.",
            "Lewati judul dengan NR > 1, buang tanda persen dari kolom 5 dengan gsub, lalu cetak kolom 5 dan 6 kalau nilainya di atas 80. Cetak angka polos dulu supaya bisa diurutkan sort -rn, baru tempelkan % saat mencetak akhir. Simpan hasilnya di variabel supaya bisa dicetak sekaligus dihitung.",
            "Tambahkan 0 supaya teks diperlakukan sebagai angka: $5 + 0 > 80. Jumlah temuannya: printf '%s\\n' \"$penuh\" | wc -l.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > disk.txt <<'EOF'
Filesystem      Size  Used Avail Use% Mounted
/dev/nvme0n1p3  476G  391G   82G  83% /
/dev/nvme0n1p2  974M  286M  621M  32% /boot
/dev/nvme0n1p1  599M   20M  580M   4% /boot/efi
/dev/sdb1       1.8T  1.7T   94G  95% /data
EOF

penuh="$(awk 'NR > 1 { gsub(/%/, "", $5); if ($5 + 0 > 80) print $5, $6 }' disk.txt |
         sort -rn)"

printf '%s\\n' "$penuh" | awk '{printf "%s %s%%\\n", $2, $1}'
printf 'total penuh: %s\\n' "$(printf '%s\\n' "$penuh" | wc -l)"
""",
    },
    {
        "title": "Latihan 10: find & Wildcard yang Aman",
        "difficulty": "Menengah",
        "question": [
            "Di direktori sementara, buat berkas-berkas berikut:",
            "  laporan.log, akses.log, catatan.txt, gambar besar.png,",
            "  dan subdirektori arsip/ berisi lama.log",
            "",
            "Tampilkan:",
            "  1. Jumlah berkas .log di SELURUH pohon",
            "  2. Jumlah berkas .log di tingkat ATAS saja",
            "  3. Nama berkas yang mengandung spasi",
            "",
            "Keluaran yang diharapkan:",
            "  log semua : 3",
            "  log atas  : 2",
            "  berspasi  : gambar besar.png",
        ],
        "hints": [
            "Baca ulang \"Mencari Berkas & Isi Berkas\", terutama opsi -name dan -maxdepth.",
            "Kutip polanya, find . -name '*.log', kalau nggak shell yang mengembangkannya duluan. -maxdepth 1 membatasi pencarian ke tingkat atas, dan pola '* *' menangkap nama yang mengandung spasi. Tambahkan -type f supaya cuma berkas yang dihitung.",
            "-printf '%f\\n' mencetak nama berkas tanpa jalur direktorinya.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

mkdir -p arsip
touch laporan.log akses.log catatan.txt "gambar besar.png" arsip/lama.log

printf 'log semua : %s\\n' "$(find . -type f -name '*.log' | wc -l)"
printf 'log atas  : %s\\n' "$(find . -maxdepth 1 -type f -name '*.log' | wc -l)"
printf 'berspasi  : %s\\n' "$(find . -type f -name '* *' -printf '%f\\n')"
""",
    },
    {
        "title": "Latihan 11: Fungsi, Percabangan & Status Keluar",
        "difficulty": "Menengah",
        "question": [
            "Buat fungsi periksa_ambang yang menerima dua argumen: nama dan",
            "nilai persentase. Fungsi mengembalikan status 0 kalau nilai di",
            "bawah 80, dan status 1 kalau 80 ke atas.",
            "",
            "Panggil untuk empat pasangan berikut dan cetak barisnya:",
            "  cpu 45, memori 88, disk 72, swap 95",
            "",
            "Baris yang aman ditandai 'OK', yang melewati ambang ditandai",
            "'LEWAT'. Akhiri dengan jumlah yang melewati ambang.",
            "",
            "Keluaran yang diharapkan:",
            "  OK    cpu    45%",
            "  LEWAT memori 88%",
            "  OK    disk   72%",
            "  LEWAT swap   95%",
            "  melewati ambang: 2",
        ],
        "hints": [
            "Fungsi, [[ ]], dan status keluar dibahas di \"Skrip Otomasi: Menyatukan Semuanya\". Status 0 berarti berhasil, selain 0 berarti gagal, dan if membaca status itu.",
            "Di dalam fungsi pakai return (atau biarkan status perintah terakhirnya jadi statusnya), jangan exit karena exit menghentikan seluruh skrip. Bandingkan angka dengan -lt di dalam [[ ]], bukan dengan tanda <. Panggil fungsinya langsung sebagai kondisi if; set -e menghentikan skrip pada perintah gagal, tapi nggak pada kondisi if.",
            "Kerangkanya if periksa_ambang \"$nama\" \"$nilai\"; then ... else ... fi, dan printf '%-5s %-6s %s%%\\n' menjaga kolomnya sejajar.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

periksa_ambang() {
    local nilai="$2"
    [[ "$nilai" -lt 80 ]]
}

lewat=0

for pasangan in "cpu 45" "memori 88" "disk 72" "swap 95"; do
    set -- $pasangan
    nama="$1"
    nilai="$2"
    if periksa_ambang "$nama" "$nilai"; then
        printf '%-5s %-6s %s%%\\n' "OK" "$nama" "$nilai"
    else
        printf '%-5s %-6s %s%%\\n' "LEWAT" "$nama" "$nilai"
        lewat=$((lewat + 1))
    fi
done

printf 'melewati ambang: %s\\n' "$lewat"
""",
    },
    {
        "title": "Latihan 12: Membaca Berkas Baris demi Baris",
        "difficulty": "Menengah",
        "question": [
            "Buat berkas paket.txt berisi persis (perhatikan spasi di dalamnya):",
            "",
            "  htop|alat pemantau proses|terpasang",
            "  tmux|pengelola sesi terminal|terpasang",
            "  ncdu|penjelajah ukuran direktori|belum",
            "  ripgrep|pencari teks cepat|terpasang",
            "  btop|pemantau sumber daya|belum",
            "",
            "Baca baris demi baris dengan while read, pisahkan berdasarkan",
            "tanda |, lalu cetak hanya yang berstatus 'belum' dalam format",
            "'- nama: keterangan'. Hitung totalnya di akhir.",
            "",
            "PENTING: penghitung harus benar, jadi jangan memakai pipa ke while.",
            "",
            "Keluaran yang diharapkan:",
            "  - ncdu: penjelajah ukuran direktori",
            "  - btop: pemantau sumber daya",
            "  belum terpasang: 2",
        ],
        "hints": [
            "Baca ulang bagian while read dan IFS di \"Skrip Otomasi: Menyatukan Semuanya\".",
            "Menyetel IFS='|' khusus untuk read membuatnya memecah baris berdasarkan tanda |, jadi tiap kolom masuk ke variabelnya sendiri. Opsi -r mencegah backslash diterjemahkan. Arahkan berkasnya ke perulangan dengan redirect, bukan pipa: dengan pipa, perulangan jalan di subshell dan penghitungnya hilang.",
            "Redirect-nya ditulis sesudah done: done < paket.txt. Untuk mencetak baris yang diawali tanda hubung, pakai printf -- supaya - nggak dibaca sebagai opsi printf.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > paket.txt <<'EOF'
htop|alat pemantau proses|terpasang
tmux|pengelola sesi terminal|terpasang
ncdu|penjelajah ukuran direktori|belum
ripgrep|pencari teks cepat|terpasang
btop|pemantau sumber daya|belum
EOF

belum=0

while IFS='|' read -r nama ket status; do
    if [[ "$status" == "belum" ]]; then
        printf -- '- %s: %s\\n' "$nama" "$ket"
        belum=$((belum + 1))
    fi
done < paket.txt

printf 'belum terpasang: %s\\n' "$belum"
""",
    },
    {
        "title": "Latihan 13: Array & case untuk Sub-perintah",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi jalankan yang menerima satu sub-perintah dan",
            "menerjemahkannya dengan case:",
            "  install  -> 'memasang paket'",
            "  remove   -> 'menghapus paket'",
            "  upgrade  -> 'memperbarui sistem'",
            "  in|rm|up -> perlakukan sama seperti bentuk panjangnya",
            "  selain itu -> 'sub-perintah tidak dikenal' ke stderr, status 2",
            "",
            "Simpan daftar uji dalam array: install, up, rm, bongkar, upgrade.",
            "Untuk tiap elemen, cetak 'elemen -> hasil'. Untuk yang tidak",
            "dikenal, cetak 'elemen -> DITOLAK'. Akhiri dengan jumlah ditolak.",
            "",
            "Keluaran yang diharapkan:",
            "  install -> memasang paket",
            "  up -> memperbarui sistem",
            "  rm -> menghapus paket",
            "  bongkar -> DITOLAK",
            "  upgrade -> memperbarui sistem",
            "  ditolak: 1",
        ],
        "hints": [
            "Array dan case dibahas di \"Skrip Otomasi: Menyatukan Semuanya\".",
            "Di case, beberapa pola untuk satu cabang digabung dengan |, misalnya bentuk panjang dan pendeknya. Cabang *) menangkap sisanya: tulis pesannya ke stderr dan return 2. Simpan daftar uji di array, ulangi dengan for x in \"${uji[@]}\", dan tangkap keluaran fungsinya dengan $( ).",
            "Karena ada set -e, pemanggilan yang boleh gagal dibungkus if, misalnya if hasil=\"$(jalankan \"$x\" 2>/dev/null)\"; then ... else ... fi. Status if mengikuti status fungsinya, dan 2>/dev/null menyembunyikan pesan stderr-nya dari keluaran.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

jalankan() {
    case "$1" in
        install|in)
            printf 'memasang paket'
            ;;
        remove|rm)
            printf 'menghapus paket'
            ;;
        upgrade|up)
            printf 'memperbarui sistem'
            ;;
        *)
            printf 'sub-perintah tidak dikenal: %s\\n' "$1" >&2
            return 2
            ;;
    esac
}

declare -a uji=("install" "up" "rm" "bongkar" "upgrade")
ditolak=0

for x in "${uji[@]}"; do
    if hasil="$(jalankan "$x" 2>/dev/null)"; then
        printf '%s -> %s\\n' "$x" "$hasil"
    else
        printf '%s -> DITOLAK\\n' "$x"
        ditolak=$((ditolak + 1))
    fi
done

printf 'ditolak: %s\\n' "$ditolak"
""",
    },
    {
        "title": "Latihan 14: trap, mktemp & Pembersihan",
        "difficulty": "Sulit",
        "question": [
            "Tulis skrip yang membuat direktori kerja sementara, menulis tiga",
            "berkas di dalamnya, lalu membuktikan bahwa pembersihan lewat trap",
            "benar-benar berjalan.",
            "",
            "Caranya: simpan nama direktori sementara di variabel, jalankan",
            "seluruh pekerjaan di dalam subshell yang memasang trap EXIT, lalu",
            "setelah subshell selesai periksa apakah direktorinya masih ada.",
            "",
            "Keluaran yang diharapkan:",
            "  berkas dibuat : 3",
            "  izin direktori: 700",
            "  setelah trap  : sudah terhapus",
        ],
        "hints": [
            "Baca ulang bagian mktemp dan trap di \"Skrip Otomasi: Menyatukan Semuanya\". Trap EXIT jalan saat shell yang memasangnya selesai.",
            "Simpan nama direktori di variabel yang dibuat sebelum subshell. Jalankan bagian yang memasang trap di dalam ( ... ), supaya EXIT-nya terpicu saat subshell itu selesai. Sesudahnya, periksa dengan [[ -d \"$dir\" ]] apakah direktorinya sudah hilang.",
            "mktemp -d membuat direktori dengan izin 700 secara bawaan, dan stat -c '%a' direktori memberi izin oktalnya. Ukur izin direktori hasil mktemp, bukan subdirektori yang kamu buat sendiri dengan mkdir.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

induk="$(mktemp -d)"
kerja="$induk/sementara"

(
    mkdir -p "$kerja"
    trap 'rm -rf "$kerja"' EXIT

    touch "$kerja/satu.txt" "$kerja/dua.txt" "$kerja/tiga.txt"

    printf 'berkas dibuat : %s\\n' "$(find "$kerja" -type f | wc -l)"
    printf 'izin direktori: %s\\n' "$(stat -c '%a' "$induk")"
)

if [[ -d "$kerja" ]]; then
    printf 'setelah trap  : masih ada\\n'
else
    printf 'setelah trap  : sudah terhapus\\n'
fi

rm -rf "$induk"
""",
    },
    {
        "title": "Latihan 15: Audit Port yang Mendengarkan",
        "difficulty": "Sulit",
        "question": [
            "Buat berkas port.txt yang meniru keluaran ss -tulnp:",
            "",
            "  Netid State  Local:Port        Proses",
            "  tcp   LISTEN 127.0.0.1:631    cupsd",
            "  tcp   LISTEN 0.0.0.0:22       sshd",
            "  tcp   LISTEN 0.0.0.0:80       nginx",
            "  udp   UNCONN 127.0.0.1:323    chronyd",
            "  tcp   LISTEN [::]:22          sshd",
            "  tcp   LISTEN 127.0.0.1:5432   postgres",
            "",
            "Laporkan mana yang TERBUKA KE JARINGAN (alamatnya 0.0.0.0 atau",
            "[::]) dan mana yang hanya lokal. Untuk yang terbuka, tampilkan",
            "port dan namanya; hilangkan duplikat port.",
            "",
            "Keluaran yang diharapkan:",
            "  TERBUKA 22 sshd",
            "  TERBUKA 80 nginx",
            "  hanya lokal: 3",
        ],
        "hints": [
            "Baca ulang \"Diagnosis Jaringan: ip, ss, DNS\" soal 0.0.0.0 dan [::] (terbuka ke jaringan) dibanding 127.0.0.1 (cuma lokal), lalu while read dan case di \"Skrip Otomasi: Menyatukan Semuanya\".",
            "Lewati baris judul dengan tail -n +2 (atau NR > 1), baca tiap baris ke beberapa variabel, lalu putuskan dengan case apakah alamatnya diawali 0.0.0.0 atau [::]. Yang terbuka dikumpulkan sebagai 'port nama', sisanya cukup dihitung sebagai lokal. Port sshd muncul dua kali (IPv4 dan IPv6), jadi duplikatnya perlu dibuang.",
            "${alamat##*:} membuang semua sampai titik dua terakhir, jadi tinggal port-nya. sort -u -k1,1n menghilangkan duplikat port sekaligus mengurutkannya. Di pola case, kurung siku perlu di-escape: \\[::\\]:*.",
        ],
        "solution": """#!/usr/bin/env bash

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > port.txt <<'EOF'
Netid State  Local:Port        Proses
tcp   LISTEN 127.0.0.1:631    cupsd
tcp   LISTEN 0.0.0.0:22       sshd
tcp   LISTEN 0.0.0.0:80       nginx
udp   UNCONN 127.0.0.1:323    chronyd
tcp   LISTEN [::]:22          sshd
tcp   LISTEN 127.0.0.1:5432   postgres
EOF

lokal=0
terbuka=""

while read -r netid state alamat proses; do
    port="${alamat##*:}"
    case "$alamat" in
        0.0.0.0:*|\\[::\\]:*)
            terbuka+="$port $proses"$'\\n'
            ;;
        *)
            lokal=$((lokal + 1))
            ;;
    esac
done < <(tail -n +2 port.txt)

printf '%s' "$terbuka" | sort -u -k1,1n | awk 'NF {printf "TERBUKA %s %s\\n", $1, $2}'
printf 'hanya lokal: %s\\n' "$lokal"
""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Laporan Kesehatan Sistem",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Satukan semuanya. Buat skrip laporan kesehatan yang membaca tiga",
            "berkas data dan menghasilkan ringkasan berbagian.",
            "",
            "Buat berkas disk.txt:",
            "  /dev/nvme0n1p3 83 /",
            "  /dev/nvme0n1p2 32 /boot",
            "  /dev/sdb1 95 /data",
            "",
            "Buat berkas layanan.txt:",
            "  sshd active",
            "  firewalld active",
            "  nginx failed",
            "  chronyd active",
            "  postgresql failed",
            "",
            "Buat berkas jurnal.txt:",
            "  info sistem dimulai",
            "  err gagal memuat modul",
            "  warning sertifikat akan kedaluwarsa",
            "  err koneksi database putus",
            "  info layanan siap",
            "",
            "Syarat laporan:",
            "  - Bagian disk: filesystem dengan pemakaian di atas 80 persen,",
            "    terpenuh dulu.",
            "  - Bagian layanan: nama layanan yang gagal, urut abjad.",
            "  - Bagian jurnal: jumlah pesan per tingkat, terbanyak dulu.",
            "  - Tiap temuan menambah penghitung masalah.",
            "  - Baris terakhir menyebut total temuan.",
            "",
            "Keluaran yang diharapkan:",
            "  == Disk ==",
            "  /data 95%",
            "  / 83%",
            "  == Layanan gagal ==",
            "  nginx",
            "  postgresql",
            "  == Jurnal ==",
            "  2 err",
            "  2 info",
            "  1 warning",
            "  total temuan: 4",
        ],
        "hints": [
            "Proyek ini merangkum \"sed & awk\", \"Mengolah Teks: cut, sort, uniq, tr\", dan \"Skrip Otomasi: Menyatukan Semuanya\". Pisahkan tiap bagian laporan ke fungsinya sendiri supaya mudah dibaca.",
            "Pakai satu variabel penghitung global yang dinaikkan tiap temuan. Temuan cuma dihitung dari disk penuh dan layanan gagal, bukan dari jurnal (makanya totalnya 4). Hindari pipa ke while supaya penghitungnya nggak hilang; pakai done < <(...).",
            "Disk: awk '$2 > 80 {print $2, $3}' lalu sort -rn. Layanan: awk '$2 == \"failed\" {print $1}' lalu sort. Jurnal: awk '{print $1}' | sort | uniq -c | sort -k1,1nr -k2,2.",
        ],
        "solution": """#!/usr/bin/env bash
#
# laporan-sehat.sh -- ringkasan kesehatan sistem dari berkas data

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

cat > disk.txt <<'EOF'
/dev/nvme0n1p3 83 /
/dev/nvme0n1p2 32 /boot
/dev/sdb1 95 /data
EOF

cat > layanan.txt <<'EOF'
sshd active
firewalld active
nginx failed
chronyd active
postgresql failed
EOF

cat > jurnal.txt <<'EOF'
info sistem dimulai
err gagal memuat modul
warning sertifikat akan kedaluwarsa
err koneksi database putus
info layanan siap
EOF

readonly BATAS=80
temuan=0

judul() {
    printf '== %s ==\\n' "$1"
}

bagian_disk() {
    judul "Disk"
    while read -r pakai titik; do
        printf '%s %s%%\\n' "$titik" "$pakai"
        temuan=$((temuan + 1))
    done < <(awk -v b="$BATAS" '$2 + 0 > b { print $2, $3 }' disk.txt | sort -rn)
}

bagian_layanan() {
    judul "Layanan gagal"
    while read -r nama; do
        printf '%s\\n' "$nama"
        temuan=$((temuan + 1))
    done < <(awk '$2 == "failed" { print $1 }' layanan.txt | sort)
}

bagian_jurnal() {
    judul "Jurnal"
    awk '{ print $1 }' jurnal.txt |
        sort |
        uniq -c |
        sort -k1,1nr -k2,2 |
        awk '{ printf "%s %s\\n", $1, $2 }'
}

bagian_disk
bagian_layanan
bagian_jurnal

printf 'total temuan: %s\\n' "$temuan"
""",
    },
]
