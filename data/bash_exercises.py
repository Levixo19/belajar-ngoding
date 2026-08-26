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
            "Mulai file dengan shebang: #!/usr/bin/env bash",
            "Gunakan echo untuk tiap baris.",
            "Bungkus teks dengan petik ganda.",
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
            "Ingat: tidak boleh ada spasi di sekitar tanda = saat membuat variabel.",
            "Aritmatika memakai $(( ... )).",
            "Di dalam $(( )) kamu boleh menulis a saja tanpa tanda dolar.",
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
            "Gunakan read untuk membaca input ke variabel.",
            "Bandingkan angka dengan -ge di dalam [[ ]].",
            "Blok if ditutup dengan fi.",
        ],
        "stdin": "80\n",
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
        ],
        "hints": [
            "Pakai for i in {1..20} lalu cek sisa baginya.",
            "Bilangan genap berarti $((i % 2)) sama dengan 0.",
            "Atau langsung pakai rentang berloncatan: {2..20..2}",
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
            "Kalikan dulu baru bagi, supaya hasilnya tidak terlanjur dibulatkan.",
            "C * 9 / 5 lebih tepat daripada C * (9 / 5) karena 9/5 jadi 1.",
            "Semua operasi di dalam satu $(( )).",
        ],
        "stdin": "25\n",
        "solution": """#!/usr/bin/env bash

read -r c
f=$(( c * 9 / 5 + 32 ))

echo "$c C = $f F" """,
    },
    {
        "title": "Latihan 6: Tabel Perkalian",
        "difficulty": "Sedang",
        "question": [
            "Baca satu angka n dari input.",
            "Tampilkan tabel perkalian n dari 1 sampai 10 dengan format:",
            "  7 x 1 = 7",
            "  7 x 2 = 14",
            "  ...",
            "  7 x 10 = 70",
        ],
        "hints": [
            "Gunakan for dengan rentang {1..10}.",
            "Hitung hasilnya dengan $(( n * i )).",
            "Perhatikan spasi di sekitar huruf x pada format output.",
        ],
        "stdin": "7\n",
        "solution": """#!/usr/bin/env bash

read -r n

for i in {1..10}; do
    echo "$n x $i = $(( n * i ))"
done""",
    },
    {
        "title": "Latihan 7: Grade dengan case",
        "difficulty": "Sedang",
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
            "Struktur: case \"$g\" in ... esac",
            "Satu cabang bisa punya beberapa pola: A|a)",
            "Tiap cabang ditutup dengan ;; dan default-nya adalah *)",
        ],
        "stdin": "B\n",
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
        "difficulty": "Sedang",
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
            "Definisikan fungsi dengan: faktorial() { ... }",
            "Argumen pertama fungsi ada di $1.",
            "Pakai local untuk variabel di dalam fungsi, lalu echo hasilnya.",
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
        "difficulty": "Sedang",
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
            "Buat array dengan: nilai=(80 65 90 45 75)",
            "Jumlah elemen ada di ${#nilai[@]}, semua isi di ${nilai[@]}.",
            "Cari tertinggi/terendah dengan membandingkan tiap elemen di dalam loop.",
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
        "difficulty": "Sedang",
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
            "Ambil satu karakter dengan ${kata:i:1}.",
            "Panjang string ada di ${#kata}.",
            "Bangun string terbalik dengan menempel karakter dari belakang ke depan.",
        ],
        "stdin": "katak\n",
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
            "Buat file dengan heredoc: cat > data.txt << 'EOF' ... EOF",
            "Baca dengan pola: while IFS= read -r baris; do ... done < data.txt",
            "Hitung kata dengan mengubah baris jadi array: read -ra kata <<< \"$baris\"",
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
            "Deklarasikan dulu: declare -A stok",
            "Urutan iterasi associative array acak, jadi urutkan kuncinya",
            "dengan: for k in $(printf '%s\\n' \"${!stok[@]}\" | sort); do",
            "Format kolom dengan: printf '%-7s: %s\\n' \"$k\" \"${stok[$k]}\"",
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
            "Cek angka dengan regex: [[ \"$1\" =~ ^[0-9]+$ ]]",
            "return mengirim exit code, tangkap dengan $? setelah memanggil fungsi.",
            "Gunakan case pada $? untuk memetakan kode ke pesan.",
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
            "Simpan tiap tugas satu baris dengan awalan '[ ] ' di file.",
            "Untuk menandai selesai, pakai sed pada baris ke-n:",
            "  sed -i \"${n}s/^\\[ \\]/[x]/\" \"$BERKAS\"",
            "Hitung yang selesai dengan grep -c '^\\[x\\]' \"$BERKAS\"",
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
]
