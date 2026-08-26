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
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Quoting",
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
        ],
    },
    {
        "title": "3. Input & Output",
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
                ]
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
                    "Opsi read yang berguna:",
                    "  -p \"teks\"   tampilkan prompt lebih dulu",
                    "  -s          silent, ketikan tidak terlihat",
                    "  -r         jangan proses backslash (SELALU pakai ini)",
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
        "title": "4. Aritmatika & Angka",
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
        "title": "5. Percabangan (if, case)",
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
        "title": "6. Perulangan (for, while, until)",
        "sections": [
            {
                "body": [
                    "Bash punya tiga jenis perulangan utama.",
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
        ],
    },
    {
        "title": "7. Array",
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
                    "  - Butuh bash versi 4 ke atas. macOS bawaan masih bash 3.2.",
                    "    Cek dengan: echo $BASH_VERSION",
                    "",
                    "Memecah string jadi array:",
                    "  teks=\"a,b,c\"",
                    "  IFS=',' read -ra bagian <<< \"$teks\"",
                    "  echo \"${bagian[1]}\"   -> b",
                ]
            },
        ],
    },
    {
        "title": "8. Fungsi",
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
        "title": "9. Argumen & Exit Code",
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
        "title": "10. Operasi String",
        "sections": [
            {
                "body": [
                    "Bash punya banyak operasi string bawaan lewat ${}.",
                    "Ini lebih cepat daripada memanggil program luar seperti sed.",
                    "",
                    "Panjang string:",
                    "  ${#teks}",
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
        "title": "11. Bekerja dengan File & Folder",
        "sections": [
            {
                "body": [
                    "Perintah dasar yang paling sering dipakai di script:",
                    "",
                    "  ls        daftar isi folder",
                    "  cd        pindah folder",
                    "  pwd       tampilkan folder saat ini",
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
                ]
            },
        ],
    },
    {
        "title": "12. grep, sed, dan awk",
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
        "title": "13. Debugging & Praktik Baik",
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
        ],
    },
    {
        "title": "14. Studi Kasus: Pengelola Catatan",
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
