BASH_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat script yang menampilkan tepat dua baris:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Bash.",
        ],
        "hints": [
            "Script bash itu kumpulan perintah yang dijalankan berurutan dari atas ke bawah. Baca ulang materi \"Pengenalan Shell & Bash\".",
            "Baris pertama adalah shebang, yang memberi tahu sistem bahwa ini script bash. Sesudah itu cukup satu perintah echo untuk tiap baris keluaran.",
            "Bungkus teksnya dengan petik ganda, dan salin tanda bacanya persis, termasuk koma, tanda seru, dan titik di akhir.",
        ],
        "solution": """#!/usr/bin/env bash

echo "Halo, namaku Andi!"
echo "Aku sedang belajar Bash." """,
    },
    {
        "title": "Latihan 2: Variabel & Kalkulator",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel a=15 dan b=4.",
            "Tampilkan hasil penjumlahan, pengurangan, perkalian,",
            "pembagian bulat, dan sisa bagi dengan format:",
            "  15 + 4 = 19",
            "  15 - 4 = 11",
            "  15 * 4 = 60",
            "  15 / 4 = 3",
            "  15 % 4 = 3",
        ],
        "hints": [
            "Soal ini tentang variabel dan aritmatika bilangan bulat. Baca ulang materi \"Variabel & Quoting\" dan \"Aritmatika & Angka\".",
            "Buat dua variabel tanpa spasi di sekitar tanda =. Tiap baris keluaran berisi teks biasa plus hasil hitung yang ditaruh di dalam $(( ... )).",
            "Di dalam $(( )) kamu boleh menulis a tanpa tanda dolar, misalnya $((a + b)). Pembagian / di bash membuang sisanya, jadi 15 / 4 memang 3.",
        ],
        "solution": """#!/usr/bin/env bash

a=15
b=4

echo "$a + $b = $((a + b))"
echo "$a - $b = $((a - b))"
echo "$a * $b = $((a * b))"
echo "$a / $b = $((a / b))"
echo "$a % $b = $((a % b))" """,
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka nilai dari input.",
            "Jika nilai lebih besar atau sama dengan 75 tampilkan 'Lulus',",
            "selain itu tampilkan 'Tidak Lulus'.",
            "",
            "Contoh: input 80 menghasilkan output Lulus",
        ],
        "hints": [
            "Kamu perlu membaca input lalu memilih satu dari dua jalan. Baca ulang materi \"Input & Output\" dan \"Percabangan (if, case)\".",
            "Baca angkanya dengan read ke sebuah variabel, lalu bandingkan dengan 75 di dalam if. Jangan cetak teks pembuka apa pun sebelum read, karena seluruh keluaran dinilai persis.",
            "Untuk angka, \"lebih besar atau sama dengan\" ditulis -ge di dalam [[ ]]. Blok if ditutup dengan fi.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["80\n", "60\n"],
        "solution": """#!/usr/bin/env bash

read -r nilai

if [[ $nilai -ge 75 ]]; then
    echo "Lulus"
else
    echo "Tidak Lulus"
fi""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20,",
            "satu angka per baris.",
            "Di baris terakhir tampilkan totalnya dengan format:",
            "  Total: 110",
            "",
            "Keluaran yang diharapkan:",
            "    2",
            "    4",
            "    6",
            "    8",
            "    10",
            "    12",
            "    14",
            "    16",
            "    18",
            "    20",
            "    Total: 110",
        ],
        "hints": [
            "Ini soal perulangan dengan syarat di dalamnya, plus satu variabel penampung total. Baca ulang materi \"Perulangan (for, while, until)\" dan \"Aritmatika & Angka\".",
            "Siapkan total bernilai 0 sebelum loop. Ulangi angka 1 sampai 20, cetak yang genap, dan tambahkan ke total. Baris Total dicetak sesudah loop selesai.",
            "Genap artinya sisa bagi 2 sama dengan 0, yaitu (( i % 2 == 0 )). Atau langsung pakai rentang berloncatan {2..20..2} supaya nggak perlu if.",
        ],
        "solution": """#!/usr/bin/env bash

total=0

for i in {1..20}; do
    if (( i % 2 == 0 )); then
        echo "$i"
        (( total += i ))
    fi
done

echo "Total: $total" """,
    },
    {
        "title": "Latihan 5: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka suhu dalam Celsius dari input.",
            "Konversikan ke Fahrenheit dengan rumus F = C * 9 / 5 + 32.",
            "Tampilkan dengan format:",
            "  25 C = 77 F",
            "",
            "Gunakan pembagian bulat biasa, tidak perlu desimal.",
        ],
        "hints": [
            "Ini soal aritmatika bilangan bulat dengan input. Baca ulang materi \"Aritmatika & Angka\".",
            "Baca suhu dengan read, hitung F di dalam satu $(( )), lalu cetak dengan format persis seperti contoh.",
            "Kalikan dulu baru bagi: C * 9 / 5 + 32. Kalau ditulis C * (9 / 5), bagian 9 / 5 langsung jadi 1 dan hasilnya salah.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["25\n", "0\n"],
        "solution": """#!/usr/bin/env bash

read -r c
f=$(( c * 9 / 5 + 32 ))

echo "$c C = $f F" """,
    },
    {
        "title": "Latihan 6: Tabel Perkalian",
        "difficulty": "Menengah",
        "question": [
            "Baca satu angka n dari input.",
            "Tampilkan tabel perkalian n dari 1 sampai 10 dengan format:",
            "  7 x 1 = 7",
            "  7 x 2 = 14",
            "  ...",
            "  7 x 10 = 70",
            "",
            "Untuk input 7, keluarannya:",
            "    7 x 1 = 7",
            "    7 x 2 = 14",
            "    7 x 3 = 21",
            "    7 x 4 = 28",
            "    7 x 5 = 35",
            "    7 x 6 = 42",
            "    7 x 7 = 49",
            "    7 x 8 = 56",
            "    7 x 9 = 63",
            "    7 x 10 = 70",
        ],
        "hints": [
            "Ini gabungan input dan perulangan dengan rentang tetap. Baca ulang materi \"Perulangan (for, while, until)\".",
            "Baca n dengan read, lalu ulangi i dari 1 sampai 10. Di tiap putaran cetak satu baris berisi n, huruf x, i, tanda =, dan hasil kalinya.",
            "Hasil kali bisa ditulis $(( n * i )) langsung di dalam teks echo. Perhatikan spasi di kiri dan kanan huruf x serta tanda = pada format keluaran.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["7\n", "12\n"],
        "solution": """#!/usr/bin/env bash

read -r n

for i in {1..10}; do
    echo "$n x $i = $(( n * i ))"
done""",
    },
    {
        "title": "Latihan 7: Grade dengan case",
        "difficulty": "Menengah",
        "question": [
            "Baca satu huruf grade (A, B, C, D, atau E) dari input.",
            "Gunakan case untuk menampilkan keterangannya:",
            "  A -> Sangat Baik",
            "  B -> Baik",
            "  C -> Cukup",
            "  D -> Kurang",
            "  E -> Sangat Kurang",
            "Selain itu tampilkan: Grade tidak dikenal",
            "",
            "Huruf kecil harus tetap dikenali (a sama dengan A).",
        ],
        "hints": [
            "case cocok untuk memilih satu dari banyak kemungkinan nilai. Baca ulang materi \"Percabangan (if, case)\".",
            "Baca hurufnya, lalu buat satu cabang per grade. Satu cabang boleh menerima lebih dari satu pola, jadi huruf besar dan kecil bisa digabung. Tambahkan cabang default paling akhir untuk huruf lain.",
            "Pola ganda ditulis A|a), tiap cabang ditutup ;;, cabang default memakai *), dan seluruh blok ditutup esac.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["B\n", "c\n", "Z\n"],
        "solution": """#!/usr/bin/env bash

read -r g

case "$g" in
    A|a) echo "Sangat Baik" ;;
    B|b) echo "Baik" ;;
    C|c) echo "Cukup" ;;
    D|d) echo "Kurang" ;;
    E|e) echo "Sangat Kurang" ;;
    *)   echo "Grade tidak dikenal" ;;
esac""",
    },
    {
        "title": "Latihan 8: Fungsi Faktorial",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi bernama faktorial yang menerima satu angka",
            "dan menampilkan hasil faktorialnya.",
            "Panggil fungsi itu untuk angka 1 sampai 6.",
            "",
            "Format output:",
            "  1! = 1",
            "  2! = 2",
            "  3! = 6",
            "  4! = 24",
            "  5! = 120",
            "  6! = 720",
        ],
        "hints": [
            "Kamu menulis fungsi yang dipanggil berulang kali dari dalam loop. Baca ulang materi \"Fungsi\".",
            "Di dalam fungsi, ambil argumen pertama, kalikan angka 2 sampai angka itu ke sebuah variabel hasil yang mulai dari 1, lalu cetak hasilnya dengan echo. Di luar fungsi, ulangi 1 sampai 6 dan tangkap keluaran fungsi dengan $(...).",
            "Argumen pertama ada di $1. Variabel di dalam fungsi sebaiknya local supaya nggak menimpa variabel loop di luar. Pemanggilannya di dalam teks: $(faktorial \"$n\").",
        ],
        "solution": """#!/usr/bin/env bash

faktorial() {
    local n=$1
    local hasil=1
    local i

    for (( i = 2; i <= n; i++ )); do
        (( hasil *= i ))
    done

    echo "$hasil"
}

for n in {1..6}; do
    echo "$n! = $(faktorial "$n")"
done""",
    },
    {
        "title": "Latihan 9: Array Nilai Siswa",
        "difficulty": "Lanjut",
        "question": [
            "Buat array berisi nilai: 80 65 90 45 75",
            "Tampilkan:",
            "  Jumlah data: 5",
            "  Total: 355",
            "  Rata-rata: 71",
            "  Tertinggi: 90",
            "  Terendah: 45",
            "",
            "Rata-rata memakai pembagian bulat.",
        ],
        "hints": [
            "Ini soal array: menyimpan banyak nilai di satu variabel lalu menelusurinya. Baca ulang materi \"Array\".",
            "Telusuri semua elemen dengan for. Di tiap putaran tambahkan ke total, lalu bandingkan dengan nilai tertinggi dan terendah sementara. Mulai tertinggi dan terendah dari elemen pertama, bukan dari 0.",
            "Semua isi array ada di \"${nilai[@]}\" dan jumlah elemennya di ${#nilai[@]}. Rata-rata adalah total dibagi jumlah, dengan pembagian bulat di $(( )).",
        ],
        "solution": """#!/usr/bin/env bash

nilai=(80 65 90 45 75)

total=0
tertinggi=${nilai[0]}
terendah=${nilai[0]}

for n in "${nilai[@]}"; do
    (( total += n ))
    (( n > tertinggi )) && tertinggi=$n
    (( n < terendah )) && terendah=$n
done

jumlah=${#nilai[@]}

echo "Jumlah data: $jumlah"
echo "Total: $total"
echo "Rata-rata: $(( total / jumlah ))"
echo "Tertinggi: $tertinggi"
echo "Terendah: $terendah" """,
    },
    {
        "title": "Latihan 10: Membalik String",
        "difficulty": "Lanjut",
        "question": [
            "Baca satu kata dari input.",
            "Tampilkan kata itu terbalik, lalu tentukan apakah palindrom.",
            "",
            "Format output untuk input 'katak':",
            "  Asli    : katak",
            "  Terbalik: katak",
            "  Palindrom: ya",
            "",
            "Kalau bukan palindrom, baris terakhir jadi 'Palindrom: bukan'.",
        ],
        "hints": [
            "Soal ini tentang operasi string: mengambil karakter satu per satu. Baca ulang materi \"Operasi String\".",
            "Telusuri kata dari indeks terakhir mundur ke 0 dan tempelkan tiap karakter ke string baru. Sesudah itu bandingkan kata asli dengan hasil baliknya untuk menentukan palindrom.",
            "Panjang string ada di ${#kata}, satu karakter di posisi i diambil dengan ${kata:i:1}, dan += menempel teks di ujung variabel. Perhatikan spasi di label Asli supaya titik duanya sejajar dengan Terbalik.",
        ],
        # Beberapa input supaya SEMUA cabang benar-benar diuji; dengan
        # satu input saja, jawaban yang di-hardcode ikut dinyatakan benar.
        "stdin_list": ["katak\n", "buku\n"],
        "solution": """#!/usr/bin/env bash

read -r kata

terbalik=""
for (( i = ${#kata} - 1; i >= 0; i-- )); do
    terbalik+="${kata:i:1}"
done

echo "Asli    : $kata"
echo "Terbalik: $terbalik"

if [[ "$kata" == "$terbalik" ]]; then
    echo "Palindrom: ya"
else
    echo "Palindrom: bukan"
fi""",
    },
    {
        "title": "Latihan 11: Menghitung Kata dari File",
        "difficulty": "Sulit",
        "question": [
            "Buat file bernama data.txt berisi 4 baris ini:",
            "  bash itu seru",
            "  belajar bash setiap hari",
            "  bash untuk otomatisasi",
            "  semangat belajar",
            "",
            "Lalu baca file itu baris demi baris dan tampilkan:",
            "  Baris 1: bash itu seru (3 kata)",
            "  Baris 2: belajar bash setiap hari (4 kata)",
            "  Baris 3: bash untuk otomatisasi (3 kata)",
            "  Baris 4: semangat belajar (2 kata)",
            "  Total baris: 4",
            "  Total kata: 12",
        ],
        "hints": [
            "Kamu membuat berkas, lalu membacanya baris demi baris. Baca ulang materi \"Aliran Data & Deskriptor\" (bagian heredoc) dan \"Perulangan (for, while, until)\".",
            "Tulis keempat baris ke data.txt dengan heredoc. Lalu baca berkasnya dengan while read: naikkan nomor baris tiap putaran, hitung kata di baris itu, dan jumlahkan ke total. Dua baris Total dicetak sesudah loop.",
            "Pola baca yang aman: while IFS= read -r baris; do ... done < data.txt. Kata dihitung dengan memecah baris jadi array lewat read -ra kata <<< \"$baris\", lalu ambil ${#kata[@]}.",
        ],
        "solution": """#!/usr/bin/env bash

cat > data.txt << 'EOF'
bash itu seru
belajar bash setiap hari
bash untuk otomatisasi
semangat belajar
EOF

nomor=0
total_kata=0

while IFS= read -r baris; do
    (( nomor++ ))
    read -ra kata <<< "$baris"
    jumlah=${#kata[@]}
    (( total_kata += jumlah ))
    echo "Baris $nomor: $baris ($jumlah kata)"
done < data.txt

echo "Total baris: $nomor"
echo "Total kata: $total_kata"

rm -f data.txt""",
    },
    {
        "title": "Latihan 12: Associative Array Stok Barang",
        "difficulty": "Sulit",
        "question": [
            "Gunakan associative array untuk menyimpan stok barang:",
            "  beras 25, gula 10, minyak 8, telur 30",
            "",
            "Tampilkan tiap barang URUT ABJAD dengan format:",
            "  beras  : 25",
            "  gula   : 10",
            "  minyak : 8",
            "  telur  : 30",
            "  Total stok: 73",
            "  Stok menipis: minyak",
            "",
            "Barang disebut menipis kalau stoknya di bawah 10.",
            "Gunakan printf dengan lebar 7 untuk nama barang.",
        ],
        "hints": [
            "Associative array menyimpan pasangan nama dan nilai. Baca ulang materi \"Array\", bagian associative array.",
            "Deklarasikan array-nya dengan declare -A, isi keempat barang, lalu telusuri kuncinya dalam urutan abjad. Di tiap putaran cetak barisnya, tambahkan ke total, dan catat barang yang stoknya di bawah 10.",
            "Urutan kunci associative array nggak bisa ditebak, jadi urutkan dulu: for k in $(printf '%s\\n' \"${!stok[@]}\" | sort). Kolom nama selebar 7 ditulis dengan printf '%-7s: %s\\n'.",
        ],
        "solution": """#!/usr/bin/env bash

declare -A stok
stok[beras]=25
stok[gula]=10
stok[minyak]=8
stok[telur]=30

total=0
menipis=()

for k in $(printf '%s\\n' "${!stok[@]}" | sort); do
    printf '%-7s: %s\\n' "$k" "${stok[$k]}"
    (( total += stok[$k] ))
    (( stok[$k] < 10 )) && menipis+=("$k")
done

echo "Total stok: $total"
echo "Stok menipis: ${menipis[*]}" """,
    },
    {
        "title": "Latihan 13: Validasi Argumen & Exit Code",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi validasi_umur yang menerima satu argumen.",
            "Fungsi mengembalikan exit code:",
            "  0 kalau argumen berupa angka 0-150",
            "  1 kalau bukan angka",
            "  2 kalau angka tapi di luar rentang",
            "",
            "Uji fungsi itu dengan nilai: 25, abc, 200, 0",
            "Tampilkan untuk tiap nilai:",
            "  25 -> valid",
            "  abc -> bukan angka",
            "  200 -> di luar rentang",
            "  0 -> valid",
        ],
        "hints": [
            "Fungsi bash mengirim status lewat exit code, bukan lewat nilai kembalian seperti di bahasa lain. Baca ulang materi \"Argumen & Exit Code\" dan \"Pola: Glob dan Regex\".",
            "Di dalam fungsi, periksa dulu apakah argumennya cuma berisi digit; kalau bukan, kembalikan 1. Kalau angka tapi lebih dari 150, kembalikan 2. Selain itu 0. Di luar fungsi, panggil fungsinya untuk tiap nilai uji, simpan $? saat itu juga, lalu ubah kodenya jadi pesan.",
            "Cek digit dengan [[ \"$1\" =~ ^[0-9]+$ ]], lalu petakan kode ke pesan dengan case. Simpan $? ke variabel sebelum menjalankan perintah lain, karena $? langsung tertimpa oleh perintah berikutnya.",
        ],
        "solution": """#!/usr/bin/env bash

validasi_umur() {
    local nilai="$1"

    if [[ ! "$nilai" =~ ^[0-9]+$ ]]; then
        return 1
    fi
    if (( nilai > 150 )); then
        return 2
    fi
    return 0
}

for uji in 25 abc 200 0; do
    validasi_umur "$uji"
    kode=$?

    case $kode in
        0) pesan="valid" ;;
        1) pesan="bukan angka" ;;
        2) pesan="di luar rentang" ;;
    esac

    echo "$uji -> $pesan"
done""",
    },
    {
        "title": "Latihan 14: Pengelola Tugas Mini",
        "difficulty": "Sulit",
        "question": [
            "Buat pengelola tugas sederhana dalam satu script.",
            "",
            "Simpan tugas di sebuah file. Buat fungsi:",
            "  tambah <isi>  - tambah tugas baru",
            "  daftar        - tampilkan semua tugas bernomor",
            "  selesai <n>   - tandai tugas nomor n dengan awalan [x]",
            "  hitung        - tampilkan jumlah tugas total dan yang selesai",
            "",
            "Uji dengan urutan: tambah 3 tugas, daftar, selesai 2, daftar, hitung.",
            "",
            "Output yang diharapkan:",
            "  == Daftar ==",
            "    1. [ ] belajar bash",
            "    2. [ ] kerjakan latihan",
            "    3. [ ] istirahat",
            "  == Daftar ==",
            "    1. [ ] belajar bash",
            "    2. [x] kerjakan latihan",
            "    3. [ ] istirahat",
            "  Total: 3, Selesai: 1",
        ],
        "hints": [
            "Ini proyek kecil yang menggabungkan fungsi, berkas, dan perulangan. Baca ulang materi \"Fungsi\" dan \"grep, sed, dan awk\".",
            "Simpan tiap tugas sebagai satu baris berawalan '[ ] ' di sebuah berkas, dan kosongkan berkasnya di awal script. tambah menulis baris baru ke ujung berkas, daftar membaca berkas sambil memberi nomor, selesai mengganti awalan di baris ke-n, dan hitung menghitung semua baris serta baris berawalan [x].",
            "Ganti awalan di baris ke-n: sed -i \"${n}s/^\\[ \\]/[x]/\" \"$BERKAS\". Hitung yang selesai: grep -c '^\\[x\\]' \"$BERKAS\". Jumlah baris: wc -l < \"$BERKAS\".",
        ],
        "solution": """#!/usr/bin/env bash
set -uo pipefail

BERKAS="tugas.txt"
: > "$BERKAS"

tambah() {
    echo "[ ] $*" >> "$BERKAS"
}

daftar() {
    echo "== Daftar =="
    local n=0
    while IFS= read -r baris; do
        (( n++ ))
        printf '  %d. %s\\n' "$n" "$baris"
    done < "$BERKAS"
}

selesai() {
    local n="$1"
    sed -i "${n}s/^\\[ \\]/[x]/" "$BERKAS"
}

hitung() {
    local total selesai_jml
    total=$(wc -l < "$BERKAS")
    selesai_jml=$(grep -c '^\\[x\\]' "$BERKAS" || true)
    echo "Total: $total, Selesai: $selesai_jml"
}

tambah "belajar bash"
tambah "kerjakan latihan"
tambah "istirahat"

daftar
selesai 2
daftar
hitung

rm -f "$BERKAS" """,
    },
    {
        'title': 'Proyek Akhir: Perapi Folder Unduhan',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Perapi Folder Unduhan',
        '',
        'Folder Unduhan siapa pun akhirnya jadi tumpukan. Buat skrip yang',
        'memilah berkas ke subfolder menurut jenisnya, melaporkan isinya, dan',
        'menandai berkas berukuran nol -- ciri unduhan yang putus di tengah.',
        '',
        'Skripnya TIDAK boleh menyentuh folder Unduhan sungguhan siapa pun.',
        'Ia membuat foldernya sendiri di direktori sementara, mengisinya dengan',
        'berkas contoh, lalu bekerja di situ -- dan membersihkannya saat keluar.',
        '',
        'Berkas contoh: laporan.pdf, data.csv, rapat.txt, logo.png, foto.jpg,',
        'pasang.sh, nilai.csv, dan kosong.txt (benar-benar kosong).',
        '',
        'Yang harus ada di programmu:',
        '  1. mktemp -d untuk folder kerja, dan trap ... EXIT untuk menghapusnya',
        '     apa pun yang terjadi.',
        '  2. Fungsi golongan() memakai case atas akhiran berkas:',
        '     pdf/txt/csv -> dokumen, png/jpg -> gambar, sh -> skrip.',
        '  3. Fungsi pilah() memindahkan tiap berkas ke rapi/<golongan>/.',
        '  4. Laporan berkolom dengan printf: golongan, jumlah berkas, jumlah',
        '     baris seluruh isinya.',
        '  5. Berkas berukuran nol dicari dengan find -size 0.',
        '  6. Tiap keluaran yang berasal dari daftar WAJIB melewati sort,',
        '     karena urutan find dan ls tidak dijamin sama di tiap mesin.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  PERAPI FOLDER UNDUHAN',
        '  ======================================',
        '  Golongan    Berkas     Baris',
        '  dokumen          5         7',
        '  gambar           2         2',
        '  skrip            1         2',
        '  --------------------------------------',
        '  Berkas kosong (unduhan gagal):',
        '    dokumen/kosong.txt',
        '  --------------------------------------',
        '  Berkas .csv dan isinya:',
        '    data.csv -> a,b,c',
        '    nilai.csv -> x,y',
        '  --------------------------------------',
        '  Total berkas dipindahkan : 8',
        '  Golongan terbentuk       : 3',
    ],
        'hints': [
            "Proyek ini menggabungkan case, fungsi, find, dan trap. Ulangi materi \"Bekerja dengan File & Folder\", \"find, xargs, dan Pemrosesan Massal\", dan \"Proses Latar Belakang, Sinyal, dan trap\".",
            "Urutannya: buat folder kerja dengan mktemp -d dan pasang trap untuk menghapusnya saat keluar, isi berkas contoh, pilah tiap berkas menurut akhirannya ke rapi/<golongan>/, lalu cetak laporan. Tiap daftar dari find atau ls wajib lewat sort sebelum dicetak, karena urutannya bisa beda di tiap mesin.",
            "Akhiran berkas: ${nama##*.} membuang segalanya sampai titik terakhir. trap 'rm -rf \"$KERJA\"' EXIT memastikan folder sementaranya hilang walaupun skripnya berhenti di tengah. Berkas kosong dicari dengan find rapi -type f -size 0.",
        ],
        'solution': """#!/usr/bin/env bash
# Perapi Folder Unduhan -- memilah berkas, membuat laporan, mengarsipkan.
set -u

KERJA="$(mktemp -d)"
trap 'rm -rf "$KERJA"' EXIT

siapkan_contoh() {
  cd "$KERJA" || exit 1
  mkdir -p unduhan
  # Berkas contoh dibuat di sini, bukan diambil dari komputer siapa pun:
  # skrip yang hasilnya bergantung isi folder nyata tidak bisa diuji.
  printf 'laporan tahunan\\n' > unduhan/laporan.pdf
  printf 'a,b,c\\n1,2,3\\n' > unduhan/data.csv
  printf 'catatan rapat\\nbaris kedua\\n' > unduhan/rapat.txt
  printf 'PNG\\n' > unduhan/logo.png
  printf 'JPEG\\n' > unduhan/foto.jpg
  printf '#!/bin/sh\\necho halo\\n' > unduhan/pasang.sh
  printf 'x,y\\n9,8\\n' > unduhan/nilai.csv
  : > unduhan/kosong.txt
}

golongan() {
  case "${1##*.}" in
    pdf|txt|csv) echo dokumen ;;
    png|jpg)     echo gambar ;;
    sh)          echo skrip ;;
    *)           echo lain ;;
  esac
}

pilah() {
  local berkas nama gol
  for berkas in unduhan/*; do
    nama="$(basename "$berkas")"
    gol="$(golongan "$nama")"
    mkdir -p "rapi/$gol"
    mv "$berkas" "rapi/$gol/$nama"
  done
}

laporan() {
  local gol jumlah
  echo "PERAPI FOLDER UNDUHAN"
  echo "======================================"
  printf '%-10s%8s%10s\\n' "Golongan" "Berkas" "Baris"
  for gol in $(ls rapi | sort); do
    jumlah=$(ls "rapi/$gol" | wc -l)
    baris=$(cat "rapi/$gol"/* 2>/dev/null | wc -l)
    printf '%-10s%8d%10d\\n' "$gol" "$jumlah" "$baris"
  done
  echo "--------------------------------------"
}

# Berkas berukuran nol sering sisa unduhan yang putus di tengah.
cari_kosong() {
  find rapi -type f -size 0 | sort | sed 's|^rapi/||'
}

siapkan_contoh
pilah
laporan

echo "Berkas kosong (unduhan gagal):"
kosong="$(cari_kosong)"
if [ -z "$kosong" ]; then
  echo "  -"
else
  echo "$kosong" | while read -r f; do echo "  $f"; done
fi

echo "--------------------------------------"
echo "Berkas .csv dan isinya:"
find rapi -name '*.csv' | sort | while read -r f; do
  echo "  $(basename "$f") -> $(head -1 "$f")"
done

echo "--------------------------------------"
total=$(find rapi -type f | wc -l)
echo "Total berkas dipindahkan : $total"
echo "Golongan terbentuk       : $(ls rapi | wc -l)"
""",
    },
]
